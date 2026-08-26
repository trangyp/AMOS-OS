---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1711.08708v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1711.08708v1_Preconditioning_the_bidomain_model_with_almost_linear_complexity

> Source: 1711.08708v1_Preconditioning_the_bidomain_model_with_almost_linear_complexity.pdf

> Pages: 28

---


## Page 1


Preconditioning the bidomain model
with almost linear complexity
Charles Pierre ∗1
1 Laboratoire de Math´ematiques et de leurs Applications, UMR CNRS 5142,
Universit´e de Pau et des Pays de l’Adour, France.
30 September, 2011
Abstract
The bidomain model is widely used in electro-cardiology to simulate spreading
of excitation in the myocardium and electrocardiograms. It consists of a system
of two parabolic reaction diﬀusion equations coupled with an ODE system.
Its
discretisation displays an ill-conditioned system matrix to be inverted at each time
step: simulations based on the bidomain model therefore are associated with high
computational costs. In this paper we propose a preconditioning for the bidomain
model in an extended framework including a coupling with the surrounding tissues
(the torso). The preconditioning is based on a formulation of the discrete problem
that is shown to be symmetric positive semi-deﬁnite. A block LU decomposition of
the system together with a heuristic approximation (referred to as the monodomain
approximation) are the key ingredients for the preconditioning deﬁnition. Numerical
results are provided for two test cases: a 2D test case on a realistic slice of the thorax
based on a segmented heart medical image geometry, a 3D test case involving a
small cubic slab of tissue with orthotropic anisotropy. The analysis of the resulting
computational cost (both in terms of CPU time and of iteration number) shows
an almost linear complexity with the problem size, i.e. of type n logα(n) (for some
constant α) which is optimal complexity for such problems.
Keywords:
preconditioning, electro-cardiology, hierarchical matrices, reaction diﬀusion
equations
∗charles.pierre@univ-pau.fr
1
arXiv:1711.08708v1  [math.NA]  23 Nov 2017


## Page 2


Charles Pierre
1
Introduction
The bidomain model [39, 23, 1, 15, 40, 30, 10] is up to now the most physiologically
founded model to describe the heart electrical activity. The bidomain model is here con-
sidered in an extended version referred to as the coupled heart and torso bidomain model.
It includes a coupling of the cardiac electrical activity with the surrounding tissue elec-
trical activity, allowing in particular electrocardiogram simulations.
The bidomain model mathematical formulation is composed of a system of two PDEs
(parabolic reaction diﬀusion equations) describing the evolution of two potentials: the
intra- and extra-cellular potentials within the myocardium. This system is coupled with
a set of ODEs modelling the kinetic of ionic transfer across the cellular membrane.
The discretisation of the bidomain model displays an ill conditioned system matrix to be
inverted at each time step. This is essentially due to the nature of the model. Two rea-
sons are raised for this. The bidomain model can be formulated as a degenerate system
of two coupled parabolic equations [15], which degeneracy causes ill-conditioning. An-
other formulation of the bidomain model, made up of a single scalar semi-linear parabolic
equation, is studied in [8]. This formulation involves a non-local operator of second order
in space, referred to as the bidomain operator. The bidomain operator is deﬁned as the
harmonic mean between two elliptic operators. The non-locality of the bidomain operator
generates high computational costs.
On top of this structural ill-conditioning, the physical features of the modelled phenomena
(because of fast and sharp space and time variations of potential: namely transmembrane
potential wave fronts) necessitates to resort to ﬁne space and time grids. Ill conditioning
together with ﬁne meshes imply very high computational costs for the bidomain model
simulations that remain challenging for 3D realistic settings. For this, many eﬀorts were
devoted to the reduction of this cost, see e.g. [13, 16, 12, 38, 26, 18].
Few papers are dealing with the preconditioning of the bidomain model.
In [27]
Pavarino and Scacchi proposed a preconditioner designed to a parallel implementation
of the bidomain model. In [17] Gerardo-Giorda et al. introduced a very interesting pre-
conditioning strategy discussed deeper on at the end of this section.
The aim of this paper is to deﬁne a general preconditioning for the bidomain system of
equations. This preconditioning is based on two simple ideas (detailed hereafter in this
section): an algebraic block-LU factorisation together with a heuristic approximation. For
its implementation in practise, it only remains to deﬁne two local block preconditioners for
two matrices: obtained by discretising an elliptic and a parabolic type equations respec-
tively. A wide class of preconditioners for such problems already has been developed, ei-
ther sequential or parallel, with available implemented versions (see e.g. [21, 34, 36, 4, 22],
details follow). We actually can resort to any of these preconditioners to embed it into
the bidomain model preconditioning here presented. In this sense, our preconditioning
framework provides a lifting from preconditioners for elliptic problems to preconditioners
for the bidomain model.
The natural question raised by this is: “can we recover the (already available) high perfor-
mances of elliptic problem preconditioners for the bidomain equations ?”. This question



## Page 3


Preconditioning the bidomain model
is here addressed from the point of view of complexity. Let A denote a sparse matrix
with size n obtained by discretising an elliptic equation.
Optimal complexity to per-
form X 7→A−1X is in O(n log(n)α) (α constant) referred to as almost linear complexity
(developments on complexity matters are given in Sec. 5.3). Optimal complexity has
been obtained for elliptic problems for instance using multi-grid approaches [21, 36] or
hierarchical matrix factorisations [22, 5, 19, 20]. In this paper we numerically prove that
almost linear complexity can be reached for the bidomain model embedding a hierarchical
Cholesky decomposition into our general bidomain model preconditioning.
Several (equivalent) mathematical formulations of the bidomain model have been pro-
posed: we refer to [10] for a comprehensive review. The bidomain model can be set as a
system of two coupled degenerate parabolic equations: this formulation has been used to
prove existence of solutions in [15, 7] and numerically used e.g. in [35, 14, 27]. A second
formulation involves a coupled parabolic-elliptic system of two equations. This formula-
tion has been widely studied either for theoretical or numerical purposes: either using
non-symmetric versions (see for instance [17, 2]) or a self-adjoint positive semi-deﬁnite
version studied in [8]. We consider here a general discretisation of the self-adjoint formu-
lation. This discrete formulation of the bidomain model is here shown to be symmetric
positive semi-deﬁnite: this property holds including the coupling of the heart with the
surrounding tissues. This discrete formulation of the bidomain model has already been
used e.g. in [3, 6].
Embedding the strong structural properties of the bidomain model (i.e. symmetry and
positivity) at the discrete level is quite natural and should provide an eﬃcient imple-
mentation.
We personally experienced the diﬀerence between the symmetric positive
formulation here adopted and the non-symmetric one in [2]. A gain in CPU time of factor
more than 5 was made with the symmetric positive version and for a similar resolution
strategy.
Let us now detail the general preconditioning strategy. It relies on the symmetric pos-
itive semi-deﬁnite formulation of the coupled heart and torso bidomain model. Various
space discretisations (including classical Lagrange P k ﬁnite elements or various ﬁnite vol-
ume techniques) can be considered. For simplicity we adopted here an Euler semi-implicit
time discretisation but the technique generalises to more sophisticated time schemes. Once
discretised, this formulation involves the inversion of one system matrix (symmetric pos-
itive semi-deﬁnite) per time step. The two following points are used to precondition the
system matrix.
1- LU factorisation. The system matrix displays a 2 × 2 block structure that can be
factorised into a block-LU form.
2- Monodomain model heuristic. Among the blocks of the LU factorisation, all
blocks have a simple deﬁnition (they are sparse and do not lead to computational
diﬃculties) except one block. This block is shown to be symmetric positive deﬁnite
and to be the sum of a mass matrix and of a discrete bidomain operator (discrete
analogue of the bidomain operator mentioned earlier on) that is shown to be the



## Page 4


Charles Pierre
harmonic mean between two stiﬀness matrices. This block, that is not sparse, is not
computed but approximated using the monodomain model approximation detailed
below.
The monodomain model approximation basically consists in approximating the bidomain
operator in [8] (the harmonic mean between two diﬀusion operators) by a simple diﬀu-
sion operator. The monodomain model can provide an accurate approximation of the
bidomain model [11, 14, 29, 28]. It has been shown in [28] that a monodomain model
could provide activation time mappings in complex situations with 1% of relative error as
compared to the bidomain model predictions. The diﬀusivity tensor for the monodomain
model approximation will here be set to the harmonic mean of the intra- and extra-cellular
conductivity tensors.This approximation is heuristic, it is exact in dimension 1 and in case
of equal anisotropy ratio between the intra- and extra-cellular media.
In a recent paper [17], Gerardo-Giorda et al. introduced a preconditioner for the bido-
main model also based on a monodomain model heuristic approximation and on a lower
block triangular approximation. Let us point out the diﬀerences between these two pa-
pers. The LU factorisation presented here should provide more eﬃcient algorithms than
the lower bock-triangular approximation since this factorisation is exact. The formulation
in [17] is based on a non-symmetric formulation whereas we here considered a symmetric
positive semi-deﬁnite system matrix. We then can beneﬁt from symmetry and positivity
properties in terms of computational eﬃciency, for instance resorting to a conjugate gra-
dient linear solver. A draft of quantitative comparison between these two preconditioning
is made in the conclusion section 6.3.
The paper is organised as follows. The coupled heart and torso bidomain model is
stated in Sec. 2. Its numerical discretisation follows in Sec. 3. In Sec. 4 are stated and
proved the mathematical properties of the discretised bidomain problem system matrix:
it is shown to be symmetric positive semi-deﬁnite, its LU block factorisation is then anal-
ysed. The general preconditioning of the bidomain model is deﬁned in Sec. 5, sub section
5.3 is devoted to its practical implementation. Numerical results are in Sec. 6. The two
test cases are presented in 6.1. The complexity of the preconditioned system matrix in-
version is numerically studied in Sec. 6.2. Results are discussed in the conclusion section
6.3.
2
Bidomain model of the heart embedded in the torso
Let us denote by Ωand H two bounded open subsets such that H ⊂Ω⊂Rd with d = 2, 3
and with smooth boundaries. We moreover assume that ∂Ω∩∂H = ∅: Ωrepresents a
thorax and H the region occupied by the heart (assumed ﬁxed here). We also consider
T := Ω−H that will be referred to as the torso, see Fig. 1. We denote Q, QH and QT
the time-space cylinders R+ × Ω, R+ × H and R+ × T respectively.
Two potential ﬁelds will be involved, the transmembrane potential v : QH 7→R and
the potential u : Q 7→R. When restricted to H (resp. to T), the potential u is referred to



## Page 5


Preconditioning the bidomain model
the extra-cellular potential (resp. extra-cardiac potential). The transmembrane potential
v = ui −u|H is the diﬀerence between an intra-cellular potential ui :
QH 7→R and
the extra-cellular potential u|H; the intra-cellular potential will not be considered in the
following mathematical formulation of the problem.
The heart has a ﬁbrous organisation implying anisotropic electrical conductivities.
The cardiac ﬁbres rotate around the ventricular cavities, see Fig. 1. The ﬁbres remain
tangent to the cardiac boundaries. This anisotropy is taken into account by introducing
in H two tensors σi and σe. Introducing the 4 conductivity parameters gl
i,e, gt
i,e, they read
as follows:
σi(x) = Diag(gl
i, gt
i),
σe(x) = Diag(gl
e, gt
e),
in a moving system of coordinates whose principal orientation is given by the ﬁbre orien-
tation at point x. Of course, when written in a ﬁxed basis, these tensors no longer are
diagonal. Physically, the parameters gl
i,e and gt
i,e are the electrical conductivities longi-
tudinally and transversely to the ﬁbre direction (subscript l and t) and relatively to the
intra- or extra-cellular media (index i or e) respectively.
The torso region T is assumed to have an isotropic but heterogeneous electrical con-
ductivity. We deﬁne in T the conductivity tensor σT(x) = k(x)Id where the conductivity
k : T 7→R basically is piecewise constant on the diﬀerent organs considered in T.
The torso model consists in:
(
div(σT(x)∇u) = 0,
(t, x) ∈
QT,
∇u · n = 0
on
∂Ω,
(1)
where n denotes the outward unit normal to ∂Ω.
In the heart region, the bidomain model is composed of the three following equations
in H, for (t, x) ∈QH:





div((σi(x) + σe(x))∇u) = −div(σi(x)∇v),
χ (c∂tv + Iion(v, w) −Ist(t, x)) = div(σi(x)∇(u + v)),
∂tw = g(v, w).
(2)
In the second equation, c denotes the cell membrane surface capacitance, χ is the ratio
of cell membrane surface per unit volume, Ist :
QH 7→R is the stimulation current
(source term). Iion(v, w) (reaction term) denotes the surface ionic current distribution
on the membrane. The gating variable w : QH 7→Rp characterises the state of the cell
membrane, its evolution is ruled by the ODE system in the third equation. The deﬁnitions
of Iion and of g are ﬁxed by the chosen ionic model in Sec. 6.1.
Equations (2) are coupled with the torso model (1) with the following coupling condition:
on
∂H :
(
u|H = u|T ,
σe(x)∇u|H · n = σT(x)∇u|T · n,
σi∇u|H · n + σi∇v · n = 0.
(3)
where n denotes the outward unit normal to ∂H.



## Page 6


Charles Pierre
The model is closed by imposing initial conditions on v and w,
v(0, x) = v0(x),
w(0, x) = w0(x),
x ∈H.
(4)
Clearly, the potential ﬁeld u is deﬁned up to an additive constant. We therefore impose
the normalisation condition for all time t > 0:
Z
Ω
u(t, ·)dx = 0.
(5)
2.1
Weak formulation
We introduce the tensor σ1 on Ω:
σ1(x) =
(
σi(x) + σe(x),
x ∈H
σT(x),
x ∈T .
The weak formulation of the bidomain model (1), (2), (3) is the following: ∀ψ ∈H1(Ω),
∀φ ∈H1(H),







Z
Ω
σ1∇u · ∇ψdx +
Z
H
σi∇v · ∇ψdx = 0,
χc∂t
Z
H
vφdx + χ
Z
H
(Iion(v, w) −Ist(x, t))φdx = −
Z
H
σi∇(u + v) · ∇φdx,
(6)
The ﬁrst equation in (6) is obtained by multiplying (1) and the ﬁrst equation in (2) by
a test function ψ ∈H1(Ω), by integrating on Ωand by using the coupling conditions (3)
and the boundary condition (1). The second equation in (6) is obtained by multiplying
the second equation in (2) by a test function φ ∈H1(H), by integrating on H together
with (3).
2.2
Case of an isolated heart
We here address the case where the heart is considered as isolated from the surrounding
tissues. In this case we have H = Ωand T = ∅. Equations (2) only are considered and
the coupling conditions (3) are replaced by zero ﬂux boundary conditions on ∂H for v
and u.
3
Implementation
For simplicity, temporal discretisation is ﬁxed to a semi implicit Euler scheme: implicit
for the diﬀusion and explicit on the reaction. Extensions to other time schemes is possible
as discussed in remark 2.
The implementation strategy is similar for various space discretisations including P k
Lagrange ﬁnite elements or ﬁnite volume scheme such as the CVFE scheme (Control



## Page 7


Preconditioning the bidomain model
Volume Finite Element, see e.g. [9]) or such as the DDFV scheme in [2]. Assumptions
(H1) and (H2) on the space discretisation are detailed in Sec. 3.1 whereas the numerical
scheme itself is presented in Sec. 3.2.
3.1
Settings
Let us consider a mesh M of Ωand a mesh MH of the cardiac region H: we assume that
MH is a sub mesh of M, that is to say that all elements (or cells or control volumes) of
MH also are elements of M.
Relatively to the considered space discretisation, let us denote by RM, RMH the set of
discrete functions attached to these two meshes. Their dimensions are denoted N and NH
respectively. A “natural” basis usually is provided for RM and RMH, denoted (Ui)1≤i≤N
and (U H
i )1≤i≤NH respectively. In the case of P k ﬁnite element methods, these functions
simply are the standard P k Lagrange basis functions. Considering these basis induces
an isomorphism between RM and RN and between RMH and RNH. A discrete function
U = PN
i=1 ciUi will be considered either as a real function or as the real vectors (ci)i≤1≤N.
Using these identiﬁcations, the canonical Euclidian structures on RN and RNH extend to
RM and RMH. We denote by (·, ·)M and (·, ·)MH the associated scalar products.
We make the following ﬁrst assumption on the space discretisation method:
(H1) for all i, 1 ≤i ≤NH: Ui|H = U H
i
(where Ui|H denotes the restriction of the function
Ui to H).
In the case of the P k ﬁnite element methods, this ﬁrst assumption is true modulo a
reordering of the basis functions (Ui)1≤i≤N. Assumption (H1) allows us to deﬁne the
restriction operation:
Π :
U =
N
X
i=1
ciUi ∈RM 7→U|H =
NH
X
i=1
ciU H
i
∈RMH.
(7)
Equivalently, Π can be seen as a simple truncation operation:
Π :
U = (ci)1≤i≤N ∈RM 7→U|H = (ci)1≤i≤NH ∈RMH,
following the above described identiﬁcation between RM and RN and between RMH and
RNH. The transpose mapping TΠ for Π is:
TΠ :
U =
NH
X
i=1
ciU H
i
∈RMH 7→
NH
X
i=1
ciUi ∈RM.
We point out that in this discrete setting
TΠ does not match the prolongation by zero
outside H. The following property will be useful:
Π TΠ = idRMH .
(8)



## Page 8


Charles Pierre
Let us introduce the mass matrices M, MH and the stiﬀness matrices S1, Si so that:
∀U1, U2 ∈RM :
Z
Ω
U1U2dx = (MU1, U2)M,
Z
Ω
σ1∇U1 · ∇U2dx = (S1U1, U2)M
∀V1, V2 ∈RMH :
Z
H
V1V2dx = (MHV1, V2)MH,
Z
H
σi∇V1 · ∇V2dx = (SiV1, V2)MH
The second assumption on the space discretisation is the following:
(H2) Let us denote IΩand IH the characteristic functions of Ωand H respectively (con-
stant functions equal to one):
IΩ∈RM ,
IH ∈RMH.
(9)
Assumption (H2) is related with the considered boundary conditions here: homogeneous
Neumann on ∂Ωand transmission conditions on ∂H. It implies that the stiﬀness matrices
S1, Si (that are symmetric positive semi-deﬁnite) have for kernels the one dimensional
spaces IΩR and IHR respectively.
3.2
Scheme statement
The three unknowns v, u and w of the (continuous) bidomain model are represented by
the discrete functions U ∈RM, V ∈RMH and W ∈[RMH]p.
We have for all test function Ψ ∈RM:
Z
H
σi∇V · ∇Ψdx = (SiV, ΠΨ)MH = ( TΠSiV, Ψ)M
Discretisation of (6) thus is:



S1U n+1 + TΠSiV n+1 = 0,
χcMH
V n+1 −V n
∆t
+ χMH (Iion(V n, W n) −In
st) = −SiΠU n+1 −SiV n+1 .
(10)
We introduce the positive parameter γ:
γ := χc/∆t.
Resolution algorithm. The complete bidomain model (1) (2) (3) is numerically solved
applying the following three operations at each time step.
Being given V n ∈RM and W n ∈[RMH]p:
Step 1. Compute the right hand side Y :
Y :=
 0
MH (γV n −χ(Iion(V n, W n) −In
st)) .



## Page 9


Preconditioning the bidomain model
Step 2. ﬁnd the solution X = T[U n+1, V n+1] to ΛX = Y with
Λ :=
 S1
TΠSi
SiΠ
γMH + Si

that satisﬁes
Z
Ω
U n+1dx = 0.
(11)
Step 3. Update the gating variable by computing W n+1 according to the third equation in
equation (2).
This paper is devoted to Step 2 only. Proposition 1 states that step 2 is well posed.
4
Properties and LU factorisation of the system ma-
trix Λ
Let us precise that S1 : RM 7→RM and that Si : RMH 7→RMH. Then, Λ : RM × RMH 7→
RM × RMH.
Proposition 1. The system matrix Λ is symmetric positive semi-deﬁnite with kernel
Ker (Λ) = IΩR × {0}. By symmetry Λ has for range Ran (Λ) = I⊥
Ω× RMH. For all
(Y1, Y2) ∈I⊥
Ω× RMH, there exists a unique (U, V ) ∈RM × RMH such that
Λ
 U
V

=
 Y1
Y2

and
Z
Ω
Udx = 0.
(12)
The resolution of step 2 in the resolution algorithm proceeds in two steps: ﬁrst ﬁnd a
solution T[X1, X2], then normalise X1. We now focus on the ﬁrst step.
Deﬁnition 1 (Pseudo-inverses S
f
−1
1
and S
f
−1
i ). The stiﬀness matrices S1 and Si are isomor-
phisms on I⊥
Ω= Ran (S1) and on I⊥
H = Ran (Si) respectively. We introduce their pseudo
inverses S
f
−1
1
and S
f
−1
i : they are equal to the inverse of S1, Si on I⊥
Ω, I⊥
H respectively and
equal to 0 on IΩR, IHR respectively.
Considering pΩ(resp. pH) the orthogonal projection of RM on I⊥
Ω(resp. of RMH on I⊥
H),
we have:
S
f
−1
1 S1 = S1S
f
−1
1
= pΩ,
S
f
−1
i Si = SiS
f
−1
i
= pH .
Proposition 2. We have the block decomposition Λ = LU with:
L :=
 S1
0
SiΠ
K

,
U :=

idRM
S
f
−1
1
TΠSi
0
idRMH

,
(13)
The matrix K is symmetric, positive deﬁnite, it is deﬁned by:
K := γMH + Si −SiΠS
f
−1
1
TΠSi.
(14)



## Page 10


Charles Pierre
Remark 1 (About the matrix K). Let us consider the tensor
σe(x) =
(
σe(x),
x ∈H
σT(x),
x ∈T ,
and denote Se the associated stiﬀness matrix. Since S1 and Se have the same range I⊥
Ω,
one can deﬁne the pseudo-inverse S f
−1
e
for Se with the same meaning as for S1.
The matrix K in (14) can be rewritten as
K = γMH +
 S−1
i
+ ΠS−1
e
TΠ
−1 .
where all inverses are pseudo-inverses. This equality is precisely stated and proved in the
proof of proposition 2.
It is interesting to notice that the second term appears as the “harmonic mean” between
the stiﬀness matrices Si and Se.
At the discrete level, this is a transposition of the
“bidomain operator” as deﬁned in [8] that was introduced as the harmonic mean between
two diﬀusion operators.
Proposition 3. L has a pseudo inverse Lf
−1 in the following sense:
LL
f
−1 = L
f
−1L =
 pΩ
0
0
idRMH

,
U is invertible, U −1 and Lf
−1 are given by:
L
f
−1 =
"
S
f
−1
1
0
−K−1SiΠS
f
−1
1
K−1
#
,
U −1 =

idRM
−S
f
−1
1
TΠSi
0
idRMH

.
(15)
For Y ∈Ran (Λ), a solution to ΛX = Y is provided by X = U −1Lf
−1Y .
Remark 2 (About the time discretisation). Choosing another time discretisation scheme
will basically imply two changes: the computation of the right hand side (Step 1 in the
resolution algorithm above) and the deﬁnition of K. In general the global structure of
the system matrix Λ (which is symmetric positive semi-deﬁnite) as well as the positivity
of K will not be aﬀected by considering diﬀerent time discretisation: this is for instance
the case for the Crank-Nicolson scheme or for operator splitting schemes (Strang formula
e.g.).
Proof of proposition 1. For X = T(U, V ) ∈RM × RMH, we have:
TXΛX = (S1U, U)M + 2(SiΠU, V )MH + (SiV, V )MH + γ(MHV, V )MH
We consider Se and σe deﬁned in Rem. 1. Since σ1 −σe is equal to 0 on T and to σi
on H, S1 −Se is positive semi-deﬁnite.



## Page 11


Preconditioning the bidomain model
Equation (8) says that
  TΠV

|H = Π TΠV = V . Together with σ1 −σe = 0 outside
H one gets:
(SiV, V )MH =
Z
H
(σ1 −σe)∇V · V dx
=
Z
Ω
(σ1 −σe)∇TΠV · ∇TΠV dx =
 (S1 −Se) TΠV, TΠV

M
(SiΠU, V )MH =
Z
H
(σ1 −σe)∇ΠU · ∇V dx
=
Z
Ω
(σ1 −σe)∇U · ∇TΠV dx =
 (S1 −Se)U, TΠV

M .
From these two equalities we deduce that:
TXΛX = (SeU, U)M +
 (S1 −Se)(U + TΠV ), (U + TΠV )

M + γ(MHV, V )MH
so ensuring that Λ is positive semi-deﬁnite.
Assuming that ΛX = 0 implies that all
the terms on the right of the last equality are equal to zero. The mass matrix being
deﬁnite this means V = 0 and so S1U = 0. Thus U ∈Ker (S1) = IΩR and we then have
Ker (Λ) = IΩR × {0}.
Let X = T[U, V ] be a solution to ΛX = Y for Y ∈Ran (Λ). A simple computation
shows that Z = T[U−αIΩ, V ] is the unique solution to (12) iﬀα = (MU, IΩ)M/(MIΩ, IΩ)M,
so ending the proof.
Proof of proposition 2. We have:
LU =
 S1
pΩTΠSi
SiΠ
γMH + Si

,
and so LU = Λ iif pΩTΠSi = TΠSi. This last equality holds since for all V ∈RMH,
  TΠSiV, IΩ

Ω= (SiV, ΠIΩ)H = (SiV, IH)H = 0,
and so Ran
  TΠSi

⊂I⊥
Ω.
The symmetry of K is obvious. Let us prove it is positive deﬁnite.
We decompose K = γMH + K0 so with K0 := Si −SiΠS
f
−1
1
TΠSi. We will prove that K0
(which is symmetric) is positive semi-deﬁnite. This implies the positivity of K since γMH
is positive deﬁnite. Precisely: K0 clearly vanishes on IHR. Then I⊥
H is stable by K0. Let
us prove that K0 is positive deﬁnite on I⊥
H.
We consider again Se and σe deﬁned in Rem. 1. Let us ﬁrst prove that:
K0 = ΠSeS
f
−1
1
TΠSi
(16)
Firstly, we have: ∀U1.U2 ∈RM,
Z
Ω
(σ1 −σe)∇U1 · ∇U2dx =
Z
H
σi∇U1 · ∇U2dx,



## Page 12


Charles Pierre
and so TΠSiΠ = S1 −Se.
Secondly, multiplying K0 by Π TΠ = idRMH on the left gives:
K0 = Π TΠK0 = Si −Π TΠSiΠS
f
−1
1
TΠSi
= Si −Π(S1 −Se)S
f
−1
1
TΠSi
= Si −Π(pΩ−SeS
f
−1
1 ) TΠSi
= ΠSeS
f
−1
1
TΠSi + Si −ΠpΩ
TΠSi.
One already showed in this proof that pΩTΠSi =
TΠSi ensuring that ΠpΩTΠSi = Si.
This gives us (16).
Clearly S f
−1
e
and S
f
−1
i
are positive deﬁnite on I⊥
Ωand I⊥
H respectively. We moreover
have TΠ(I⊥
H) ⊂I⊥
Ωsince for all V ∈I⊥
H:
  TΠV, IΩ

Ω= (V, ΠIΩ)H = (V, IH)H = 0.
Then ΠS f
−1
e
TΠ is positive deﬁnite on I⊥
H. Let us deﬁne A := (S
f
−1
i
+ ΠS f
−1
e
TΠ): I⊥
H is
stable by A. A is positive deﬁnite and so invertible on I⊥
H. We will end this proof by
showing that K0 = A−1 on I⊥
H.
K0A = (ΠSeS
f
−1
1
TΠSi)(S
f
−1
i
+ ΠS
f
−1
e
TΠ)
= ΠSeS
f
−1
1
TΠpH + ΠSeS
f
−1
1
TΠSiΠS
f
−1
e
TΠ
= ΠSeS
f
−1
1
TΠpH + ΠSeS
f
−1
1 (S1 −Se)S
f
−1
e
TΠ
= ΠSeS
f
−1
1
TΠpH + ΠSe(pΩS
f
−1
e
−S
f
−1
i pΩ) TΠ
= ΠSeS
f
−1
1
TΠpH + ΠSe(S
f
−1
e
−S
f
−1
i ) TΠ
= ΠpΩ
TΠ + ΠSeS
f
−1
1
TΠ(pH −idRMH ).
Clearly, pH −idRMH vanishes on I⊥
H. Moreover, since TΠ(I⊥
H) ⊂I⊥
Ω, ΠpΩTΠ is the identity
on I⊥
H. Thus K0AV = V for all V ∈I⊥
H.
5
Preconditioning
The previously studied algebraic properties of the system matrix Λ naturally suggest a
block-LU designed preconditioner for Λ, here deﬁned in Sec. 5.1. This general algebraic
setting is the ﬁrst key ingredient towards the preconditioning of the bidomain model.
The second key ingredient is a heuristic approximation of the matrix K, presented in Sec.
5.2.
The last layer to practically implement the subsequent preconditioning indeed is discussed
in Sec. 5.3.



## Page 13


Preconditioning the bidomain model
5.1
Preconditioner deﬁnition
The practical strategy to solve (11) will be to use an iterative solver for the left precon-
ditioned system:
P −1
Λ ΛX = P −1
Λ Y,
for a global preconditioner PΛ deﬁned as follows.
Deﬁnition 2. Let us consider P1 a preconditioner for S1 and PK a preconditioner for K.
We deﬁne a global preconditioner PΛ for Λ as:
PΛ = LPUP ,
LP :=
 P1
0
SiΠ
PK

,
UP :=
 idRM
P −1
1
TΠSi
0
idRMH

.
(17)
The inversion of PΛ is achieved as follows. The solution X to PΛX = Y is given by
X = U −1
P L−1
P Y with:
L−1
P :=

P −1
1
0
−P −1
K SiΠP −1
1
P −1
K

,
U −1
P
:=
 idRM
−P −1
1
TΠSi
0
idRMH

.
(18)
Neglecting the vector additions, the operational cost to compute X = ΛY is:
- 2 multiplications by Si
- 1 multiplication by S1
- 1 multiplication by MH,
whereas the operational cost to compute X = P −1
Λ Y is:
- 2 inversions of P1,
- 1 inversion of PK,
- 2 multiplications by Si,
The symmetry and positivity properties of Λ allow to resort to a Preconditioned Conjugate
Gradient (PCG) algorithm to solve (11). The cost for this iterative solver (again neglecting
scalar products and vector additions) is for each step: one multiplication by Λ and one
inversion of P −1
Λ X = Y .
5.2
Heuristic approximation of K
The hard task for the deﬁnition of PΛ in (17) is the deﬁnition of PK. As developed in
Rem. 1, K has a complex structure:
K = γMH + K0,



## Page 14


Charles Pierre
where K0 is a non-sparse matrix obtained by making the harmonic mean between Si and
Se. Since K is a full matrix, it will never be computed and the alternative strategy to
deﬁne PK is to derive an approximation of K displaying a sparse pattern.
Let us consider the tensor σm:
σm(x) := (σ−1
e (x) + σ−1
i (x))−1 ,
x ∈H,
which is the harmonic mean between σi and σe. We introduce the stiﬀness matrix Sm
associated to σm acting on RMH. We make the following approximation:
K ≃Km := γMH + Sm.
This approximation is referred to as the monodomain model approximation [14].
The matrix Km has a simple structure. It is the discretisation matrix of a parabolic
equation. It is moreover symmetric, positive deﬁnite and sparse (with the same pattern
as Si).
5.3
Practical implementation of P1 and PK
The two preconditioners P1 and PK will be built from the matrices S1 and Km respectively.
These matrices (sparse, symmetric positive semi-deﬁnite) have classical structures arising
from the discretisation of elliptic and parabolic problems respectively. A wide literature
has been devoted to the preconditioning of such matrices: among classical choices we not
comprehensively quote incomplete decomposition methods (incomplete LU or incomplete
Cholesky, see e.g. [34]) multi-grid or multi-level methods, see [21, 36]. Fixing one of
these classical possible choices actually provide a fully deﬁned implementation of the here
presented bidomain model preconditioning.
We insist on the versatility of this bidomain model preconditioning. This versatility relies
on the freedom for the choice of P1 and PK.
Remark 3 (Parallelisation). At this stage, let us underline the consequences on paralleli-
sation induced by this versatility characteristic of the bidomain model preconditioning.
Once embedded into some iterative solver (e.g. CG or GMRes) the resolution of system
(11) preconditioned by PΛ only requires:
-
matrix vector multiplications by Λ,
-
inversions of PΛX = Y : as detailed in Sec. 5.3 this operation consists in matrix
vector multiplication and inversions of P1X = Y and of PKX = Y ,
-
various remaining operations, such as scalar products..
Except the inversions of P1X = Y and of PKX = Y , all these operations have trivial
parallelisation. But since P1 and PK are preconditioners for classical elliptic or parabolic
discretised PDEs, classical parallel versions for P1 and PK already are available. For in-
stance a review of algebraic methods (such as parallel version of incomplete factorisations)



## Page 15


Preconditioning the bidomain model
is provided in [4, 34]. Another wide class of parallelisation strategies based on domain
decomposition is analysed in [31] and also described in [34]. For instance the multi-level
additive Schwarz preconditioner, such as presented in [27] and applied to the bidomain
model, also could be incorporated inside the here presented general preconditioning frame-
work.
For this reason, the here presented preconditioning strategy for the bidomain model nat-
urally ﬁts with the constraints of parallelism.
Optimal complexity to solve a discretised elliptic problem AX = Y is O(n) with n the
system size: since X 7→AX has O(n) complexity one cannot hope better for Y 7→A−1Y
(A being sparse whereas A−1 is full). Although this optimality can be reached for some
particular problems (for instance in case A is tri-diagonal), in practise the most eﬃcient
algorithms have almost linear complexity: that is O(n log(n)α) with α a constant.
Hierarchical matrices preconditioning strategy [22, 5, 19, 20] provides such an almost
linear complexity (among various possible choices such as multi-grid methods [21]). This
method will be used for the numerical results in Sec. 6 to precondition S1 and Km. This
method proceeds in two steps. Firstly compute an approximation of the considered matrix
(here S1 or Km). This approximation is built using hierarchical matrices arithmetic (ba-
sically including block partition of the matrix and deﬁning a blockwise approximation by
low rank matrices), ensuring low storage cost. This approximation accuracy is controlled
by the parameter ϵ: in matrix norm the error goes to 0 with ϵ. Secondly perform the ex-
act decomposition (either LU or Cholesky) of this approximation. Hierarchical Cholesky
decomposition has been used here to build P1 and PK. Taking advantage of the hierar-
chical arithmetic, both the construction, storage and inversion of the preconditioners are
in O(n log(n)α), precisely with α = 2 (resp. 4) for the decomposition and α = 1 (resp. 2)
for the storage/inversion in dimension 2 (resp. 3).
The setting of the accuracy parameter ϵ strongly impacts the preconditioning eﬃciency.
Naturally the PCG convergence rate increases as ϵ goes to 0. A convergence in one single
PCG iteration is expected provided a small enough value for ϵ. Meanwhile the precondi-
tioner inversion cost increases as ϵ 7→0: thus the highest PCG convergence rate may not
correspond to the most eﬃcient setting of the preconditioner. An optimal value for ϵ (not
too small but not too large) has to be searched. PCG convergence rate for such optimal
value are shown in Sec. 6.2 for which 3 PCG iterations typically have to be performed.
In practise the construction of P1 and PK was made using the H-Lib library from L.
Grasedyck and S. B¨orm1. The sequential version of the code has been used: a parallel
version also is available.
6
Numerical results
The eﬃciency of the preconditioner presented in Sec. 5 is analysed in this section. The
bidomain model has been implemented following Sec. 3 and using the CVFE ﬁnite volume
1http://www.hlib.org/



## Page 16


Charles Pierre
Values
Unit
Cell membrane surface-to-volume ratio (2D)
χ = 1500
[cm−1]
Cell membrane surface-to-volume ratio (3D)
χ = 500
”
Membrane surface capacitance
c = 1.0
[µ F/cm2]
Longitudinal intra-cellular conductivity
gl
i = 1.741
[mS/cm]
Transverse intra-cellular conductivity
gt
i = 0.1934
”
Longitudinal extra-cellular conductivity
gl
e = 3.906
”
Transverse extra-cellular conductivity
gt
e = 1.970
”
Lung conductivity
0.5
”
Blood conductivity (ventricular cavities)
6.7
”
Remaining tissues conductivity
2.2
”
Table 1: Model parameters
spatial discretisation (see e.g. [9]). For this spatial discretisation the degrees of freedom
are located at the mesh vertices and the mass matrices are diagonal. Two test cases
are considered, they are detailed in Sec. 6.1. For these two test cases a depolarisation
potential wave is simulated. The spreading of depolarisation The cost for the inversion
of the preconditioned system (11) is measured during the spreading of the depolarisation
wave, that numerically is by far the stiﬀest part of the simulation. The dependence of this
cost on the problem size is then analysed. For this a series of meshes Mn is considered
with an increasing number of vertices DOF(n). We here aim to validate an almost linear
dependence of the cost on DOF(n).
The cost has been measured in two ways. Firstly in terms of CPU time. The averaged
CPU time spent on the inversion of system (11) during the depolarisation sequence is
denoted CPU(n). The logarithmic growth rate rn of CPU(n) relatively to DOF(n) will
be considered:
rn = log(CPU(n)/CPU(n −1))
log(DOF(n)/DOF(n −1) .
(19)
The CPU time measurements however might be perturbed by cache eﬀects and memory-
access diﬀerences for large-scale problems. To cope with this, the cost also is evaluated in
terms of number of iterations. The averaged number of iterations required by the PCG
algorithm to invert (11) during the depolarisation sequence is denoted Iter(n). Each step
of the PCG algorithm requires one multiplication by Λ and one inversion of PΛ. These
operations are of linear and almost linear complexity with DOF(n) respectively. Thus
a constant or logarithmic behaviour is expected for Iter(n) to validate an almost linear
complexity of the preconditioning.
Numerical results for the preconditioning complexity are presented and discussed in Sec.
6.2 and 6.3 respectively.



## Page 17


Preconditioning the bidomain model
6.1
Test cases
For the two test cases, the reaction terms Iion(v, w) and g(v, w) in (2) have been set to the
Luo and Rudy ionic model of class II [25] designed for mammalian ventricular cells and
for which the system of ODEs in (2) is of size 20 (i.e. w ∈R20). The model parameters
χ, c as well as the conductivities are displayed in Tab.1: these values are physiological
values taken from [24, 37].
2D test case. The domain Ωis an horizontal slice of a human thorax. This geometry
Figure 1: 2D test case description. Left: ﬁbrous anisotropic structure of the two ventricles.
Middle: 2D geometry Ωand its sub-domains. body surface potential (ECG) are recorded
at the vertices V1 to V6. Right: stimulation site locations.
has been obtained by segmentation of a medical image (CT-Scan, courtesy of the Ottawa
Heart Institute) with resolution 0.5 mm. We refer to [32, 33] for details on the segmen-
tation procedure. The segmented image is depicted in Fig. 1. It includes 4 sub-domains:
the two ventricles (H) and the torso (T) made of the ventricular cavities, the lungs and
the remaining tissues.
Four meshes (Mn)n=1...4 of Ωwill be considered: with DOF(1)=143 053, DOF(2)=344
408, DOF(3)=684 112 and DOF(4)=1 257 312. The associated time steps are ∆t = 0.07,
0.05, 0.035 and 0.025 milli seconds (ms) respectively.
The anisotropic structure of the two ventricles is displayed on Fig. 1: bundles of ﬁbres
rotating around the ventricular cavities have been considered. Inside the torso T, hetero-
geneous conductivities have been considered for each sub-domains: the lungs, ventricular
cavities and the remaining tissues conductivities are given in Tab. 1.
With these settings, a depolarisation potential wave is simulated. For this a stimulation
current Ist(x, t) (see equation (2)) is applied during 1 ms at four locations (stimulation
sites) on the ventricular cavities as depicted on Fig. 1; the right ventricle being stimulated
5 ms later than the left one.
The spreading of this potential wave across the myocardium is depicted on Fig. 2. The
transmembrane potential v in the heart is depicted 15, 30 and 45 ms after stimulation on
the left. Without entering the details: the region in blue is at rest potential (v ≃−90
mV) whereas the region in red is excited (v ≃50 mV). Downward: the excitation wave



## Page 18


Charles Pierre
starts at the stimulation site location and then spreads throughout the cardiac tissue. The
activation time φ(x) is computed pointwise as the time t = φ(x) so that v(φ(x), x) = −20
mV (the time instant when the depolarisation wave reaches the point x). Activation time
are depicted on Fig. 3.
The modiﬁcations on the extra-cellular (and extra-cardiac) potential u on Ω(heart and
torso) induced by the transmembrane depolarisation wave spreading also is depicted on
Fig. 2. The body surface potential (ECG) is recorded at 6 points on ∂Ω, their location
is depicted on Fig. 1 (points V1 to V6). These potentials (u(t, V i))i=1...6 are recorded at
each time step along a complete cardiac cycle (including depolarisation and repolarisa-
tion). Results are depicted on Fig. 3 on the right for the two electrodes V2 and V6.
3D test case. We here consider a small slab of tissue: a cubic domain with one
centimetre width (Ω= [0, 1]3). A series of 5 meshes (Mn)n=1...5 has been considered,
from 500 to 1 250 000 vertices (see Tab. 2 for exact ﬁgures). The mesh size being divided
by 2 from Mn to Mn+1, the time stepping ∆t also is divided by 2 and ranges from 0.2 to
0.0125 ms from the coarsest to the ﬁnest mesh. The heart is here considered as isolated:
no torso T is involved as described in Sec. 2.2. The cardiac tissue anisotropy is set to
be of orthotropic type, as deﬁned in [14]. Muscular ﬁbres are horizontal and independent
of x and y. The ﬁbre directions linearly rotate from +π/4 to −π/4 as z goes from 0 to
1. Orthotropic anisotropy represents the physiologically observed rotation of the cardiac
ﬁbres from +π/4 to −π/4 from the endo-cardium to the epi-cardium.
A depolarisation potential wave is simulated by applying a stimulation current at the
centre of the domain during 1 ms.
The spreading of transmembrane depolarisation wave is depicted on Fig. 4. Activation
time are here represented for three slices of the domain Ω= [0, 1]3: z = 0, z = 0.5
and z = 1. Each slice corresponds to the endo-cardium, middle wall and epi-cardium
respectively. The ﬁbre angle with ex is clearly visible on each slice: +π/4 for z = 0 (left),
0 for z = 0.5 (middle) and −π/4 for z = 1 (right).
6.2
Results
All ﬁgures and tables reported here have been obtained ﬁxing a tolerance of 10−6 for the
system (11) inversion; the residual being deﬁned as ∥ΛX −Y ∥/∥Y ∥in Euclidian vector
norm. The hierarchical Cholesky decompositions for P1 and PK have been built for various
values of the accuracy parameter ϵ introduced in Sec. 5.3. All computations were ran on
a clustered platform with processor cores of type AMD Opteron, 2.3 GHz.
Number of iterations. We ﬁrst investigate the cost for system (11) during the depo-
larisation sequence in terms of number of iterations Iter(n) for the PCG algorithm. As al-
ready developed in this section preamble, the global cost theoretically is in O(Iter(n)DOF(n) log(DOF(n)
The numerical results are reported in Tab. 5. In dimension 2, for ϵ = 10−2 Iter(n)
globally is multiplied by 1.18 between the coarsest and the ﬁnest meshes when meanwhile
the problem size is multiplied by almost 9. For ϵ ≤10−3 Iter(n) remains constant. In
dimension 3 Iter(n) increases very slowly: for ϵ = 10−2 (resp. 10−1) it is multiplied by 2



## Page 19


Preconditioning the bidomain model
Figure 2: 2D simulation. Left: depolarisation sequence of the heart, the transmembrane
potential v is represented 15, 30 and 45 ms after stimulation. Right: associated potential
u in the heart and in the extra cardiac region.
(resp. 4.66) when the problem size is multiplied by more than 2 500; for ϵ = 10−2 it even
decreases.
The very slow variation of Iter(n) with DOF(n) (when it is not constant) appears in
good agreement with a O(log(DOF(n))β) assumption ensuring almost linear complexity



## Page 20


Charles Pierre
Figure 3: 2D simulation. Left: activation time in the heart, isolines in black are separated
by 10 ms. Right: ECG recordings, the extra-cardiac potential is recorded on the torso
surface at two points located at electrodes V2 (above) and V6 (below), see ﬁgure 1 for
the electrode location.
Figure 4: 3D simulation. Activation times for three slices of the domain Ω= [0, 1]3:
z = 0, z = 0.5 and z = 1 from left to right. Isolines (in black) are separated by 1 ms.
n
DOF(n)
Iter(n)
ϵ = 10−2
ϵ = 10−3
ϵ = 10−4
1
143 053
3.19
3.00
3.00
2
344 408
3.82
3.00
3.00
3
684 112
4.00
3.00
3.00
4
1 257 312
4.54
3.00
3.00
n
DOF(n)
Iter(n)
ϵ = 10−1
ϵ = 10−2
ϵ = 10−3
1
497
2.40
2.00
2.00
2
3 220
4.03
2.79
2.76
3
22 256
5.14
3.00
3.00
4
162 981
7.43
3.24
3.00
5
1 253 910
11.20
3.96
2.00
(a) 2D case
(b) 3D case
Table 2: Average number of iterations for one system inversion.



## Page 21


Preconditioning the bidomain model
(a) 2D case
(b) 3D case
Figure 5:
Plot of DOF(n)×Iter(n) as a function of DOF(n) in (decimal) Log/Log Scale.
Left: 2D case for ϵ = 10−2. Right: 3D case for the three values of ϵ = 10−2, 10−3 and
10−3.
of the preconditioning global cost. It is unfortunately not possible to numerically estimate
β from these results since log(log(DOF(n))) has a too small range of variation. To have
a deeper insight on the behaviour of Iter(n) when it does not remain constant we instead
consider the cost indicator DOF(n)×Iter(n). An almost linear behaviour of this indicator
is expected. It has been represented as a function of DOF(n) in decimal logarithmic scale
on Fig. 5. In dimension 2 the curve has a global estimated slope of 1.15 using a linear
least square best approximation. In dimension 3 the slopes have been estimated to 1.19,
1.07 and 1.0 for ϵ = 10−1, 10−2 and 10−3 respectively. Again, these results are in good
agreement with the almost linear complexity assumption on the preconditioning.
n
DOF(n)
CPU(n)
ϵ = 10−2
ϵ = 10−3
ϵ = 10−4
1
143 053
1.73
1.57
1.78
2
344 408
6.32
4.34
4.42
3
684 112
10.49
8.75
8.39
4
1 257 312
23.96
17.04
13.46
n
rn
ϵ = 10−2
ϵ = 10−3
ϵ = 10−4
2
1.47
1.16
1.04
3
0.74
1.02
0.93
4
1.36
1.09
0.78
Table 3: CPU Time, 2D case.
Left: averaged CPU time in seconds for one system
inversion. Right: logarithmic growth of CPU(n)with respect to DOF(n).
CPU time consumption. The cost CPU(n) is reported in Tab. 3 (resp. Tab. 4)
in dimension 2 (resp. 3) together with the logarithmic growth rate rm of CPU(n) with
respect to DOF(n) deﬁned in (19). As for the iteration number, the behaviour of CPU(n)
is clearer for the smallest values of ϵ. For ϵ ≤10−3 (resp. ϵ ≤10−2) in dimension 2 (resp.



## Page 22


Charles Pierre
n
DOF(n)
CPU(n)
ϵ = 10−1
ϵ = 10−2
ϵ = 10−3
1
497
2.0 10−3
1.7 10−3
1.8 10−3
2
3 220
5.1 10−2
4.1 10−2
4.2 10−2
3
22 256
6.9 10−1
4.4 10−1
4.9 10−1
4
162 981
8.6
4.6
5.5
5
1 253 910
102.96
59.8
32.2
n
rn
ϵ = 10−1
ϵ = 10−2
ϵ = 10−3
2
1.75
1.70
1.70
3
1.34
1.22
1.27
4
1.27
1.19
1.21
5
1.22
1.25
0.86
Table 4: CPU Time, 3D case.
Left: averaged CPU time in seconds for one system
inversion. Right: logarithmic growth of CPU(n)with respect to DOF(n).
3), rn decreases with n and goes to 1 or even below 1.
The data in Tabs. 3 and 4 have been plotted on Fig. 6. The curve slopes have been
estimated using a least square best linear approximation. In dimension 2 the slopes are
of 1.17, 1.09 and 0.94 for ϵ = 10−2, 10−3 and 10−4 respectively. In dimension 3 they are
of 1.27, 1.21 and 1.12 for ϵ = 10−1, 10−2 and 10−3 respectively (and neglecting the ﬁrst
data point).
Firstly, since rn roughly decreases (starting with rates higher than 1.7 in dimension 3),
these computed slopes indeed are upper-bounds on the complexity. Secondly CPU time is
not a fully reliable cost measurement: because of cache eﬀects memory-access diﬀerences
for large-scale problems and because of the cluster load. For these two reasons we conclude
that these CPU data are in good agreement with an almost linear complexity of the
preconditioned system inversion, conﬁrming the study of Iter(n).
(a) 2D case
(b) 3D case
Figure 6: Cost of one inversion of ΛX = Y in terms of CPU Time as a function of the
problem size in (decimal) Log/Log scale.
PCG convergence rate. The convergence rate of the residual towards 0 for the



## Page 23


Preconditioning the bidomain model
preconditioned conjugate gradient algorithm has been measured in dimension 2 and 3 for
the accuracy parameter set to ϵ = 10−3. The (decimal) logarithm of the residual has been
plotted as a function of the iteration number on Fig. 7 for the four considered meshes in
dimension 2 and for 3 meshes in dimension 3. Due to the very small number of iterations
needed, this convergence rate obviously is quite large.
In dimension 3, for the ﬁnest mesh M5 with 1 250 000 vertices, the residual is divided
by more than 150 at step one and by more than 75 at step 2. For the two other meshes,
each PCG iteration divides the residual by at least 100.
In dimension 2, for all four meshes log(residual) displays the same global slope with respect
to the number of iterations that is equal to 1.6. Globally the residual is divided by 40 at
each time step. More precisely the residual is usually divided by 100 at the ﬁrst step, by
30 at the second one and by 20 at the third one.
(a) 2D case
(b) 3D case
Figure 7: PCG convergence rate.
Convergence of the residual of the preconditioned
system (11) as a function of the number of iterations. On both the 2D and the 3D cases,
the preconditioner is set with ϵ = 10−3. Left, 2D case: convergence is shown for each of
the four 2d meshes. Right, 3D case: convergence is depicted for the coarsest mesh (mesh
1), for the ﬁnest mesh (mesh 5) and on the intermediate mesh 3.
Cost calibration and proﬁling. Neither the CPU time nor the number of iterations
actually provides an absolute evaluation for the preconditioning cost in the following sense.
CPU time measurements are device dependent and the iteration number does not take
into account the cost for the inversion of P1 and PK that may be large. These indicators
are relevant and suﬃcient to evaluate the asymptotic complexity with DOF(n) but do
not allow practical comparison with other techniques.
To address this question we proceed as follows.
Firstly we consider the complete
algorithm proﬁling: we measure the amount of time spent on each task (RHS computation,
system inversion, normalisation...) at each time step and average these durations along
the depolarisation sequence. Secondly we compare the amount of time inside the PCG



## Page 24


Charles Pierre
algorithm spent on the two predominant operations X 7→P −1
Λ X and X 7→ΛX. The ratio
between these two times provides a calibration of the preconditioner PΛ inversion cost in
terms of matrix vector multiplication by Λ, which last operation has a fully established
operational cost.
We point out that this ratio makes sense because of the almost linear complexity with
DOF(n). Practically it varies suﬃciently slowly with DOF(n) to derive a typical ratio for
practically used problem size.
In dimension 2 (resp. 3), these typical ﬁgures are as follows:
- 70% (resp. 85 %) of the whole computational eﬀort is dedicated on the system (11)
inversion,
- each operation X 7→P −1
Λ X has cost 15 (resp. 25) matrix-vector multiplication by
Λ,
- considering an average number of iteration equal to 3, inverting X 7→Λ−1X has the
same cost has 50 (resp. 80) matrix-vector multiplication by Λ.
6.3
Conclusion
We introduced in this paper a new preconditioning for the bidomain model based on an
algebraic block-LU decomposition of its system matrix Λ and a heuristic approximation.
The complexity for solving the preconditioned system ΛX = Y with respect to the matrix
size has been numerically analysed using both a 2D and a 3D test case and a hierarchical
Cholesky preconditioning. This complexity has been numerically showed to be almost
linear; which is optimal in this context (see discussion in Sec. 5.3).
We ﬁrstly would like to recall that the notion of complexity is not suﬃcient to compare
algorithms in practise. The only certainty is that the resolution strategy presented here
will asymptotically become more eﬃcient than a second algorithm with worst complex-
ity (as the problem size goes to inﬁnity). Being ﬁxed a problem, the second algorithm
might be more eﬃcient. The calibration and proﬁling provided in Sec. 6.2 might however
help towards such comparisons and especially with the preconditioning developed in [17].
Firstly the data given in this paper do not indicate almost linear complexity. Precisely,
CPU time data rather ﬁt a complexity of 1.4 with the problem size. Despite the limita-
tions on CPU time measurements we already mentioned, it is likely that this complexity
is greater than 1. Iteration numbers also are reported (on a test case quite close to the
3D test case here on the mesh M4) that are of order 6 with a ﬂexible GMRes. Flexi-
ble GMRes performs m matrix-vector multiplications and preconditioner inversions per
iteration with m the restart number, typically of order 25. This would mean 150 matrix-
vector multiplications and preconditioner inversions. Each preconditioner inversion itself
uses an iLU(0) PCG: thus one matrix-vector multiplication and one iLU(0) inversion per
iteration. Even assuming a fast convergence of the PCG in a few steps, this may lead
to a calibration of the cost in terms of matrix-vector multiplications several times larger
than the one we obtained (equal to 80). The comparison of CPU times on the same case



## Page 25


Preconditioning the bidomain model
(almost the same processor has been used for the two papers) conﬁrms this option.
We eventually would like to underline that almost linear complexity for the resolution
of (11) does not mean almost linear complexity for the resolution of the bidomain model.
Assuming for simplicity a linear dependence for the cost on the number of nodes, this
still implies an h−d dependence of the cost on the mesh size h and with d the dimension.
Considering the global cost of the simulation and not only the cost of one inversion, this
now leads to an h−(d+1) dependence of the cost on the mesh size. For instance, consider-
ing some precision criterion e based on the activation time, that is of order 1 with h as
established in [2, 28], the complexity for the bidomain model with respect to e also is of
e−3 and e−4 in dimension 2 and 3 respectively.
Thus a linear dependence of one system inversion cost on the problem size still leads to
really heavy global costs for this type of problems.
References
[1] L. Ambrosio, P. Colli-Franzone, and G. Savar´e. On the asymptotic behaviour of
anisotropic energies arising in the cardiac bidomain model. Interfaces Free Bound.,
2(3):213–266, 2000.
[2] B. Andreianov, M. Bendahmane, K. H.. Karlsen, and C. Pierre.
Convergence of
DDFV schemes for the bidomain cardiac model. Networks and Heterogeneous Media,
In press, 2011.
[3] Y. Belhamadia, A. Fortin, and Y. Bourgault. A time-dependent adaptive remeshing
for electrical waves of the heart. IEEE Biomed. Eng., 55(2):443–452, 2008.
[4] Michele Benzi. Preconditioning techniques for large linear systems: a survey. J.
Comput. Phys., 182(2):418–477, 2002.
[5] S. Boerm, L. Grasedyck, and W. Hackbusch. An introduction to hierarchical matrices
with applications. Eng. Anal. Bound., 27:405–422, 2003.
[6] M. Boulakia, S. Cazeau, M. A. Fern´andez, J.F. Gerbeau, and N. Zemzemi. Math-
ematical modeling of electrocardiograms: a numerical study. Ann Biomed. Eng.,
38(3):1071–1097, 2010.
[7] M. Boulakia, M. A. Fern´andez, J.F. Gerbeau, and N. Zemzemi. A coupled system of
PDEs and ODEs arising in electrocardiograms modeling. Appl. Math. Res. Express.
AMRX, (2):2, 28, 2008.
[8] Y. Bourgault, Y. Coudi`ere, and C. Pierre. Existence and uniqueness of the solution
for the bidomain model used in cardiac electrophysiology. Nonlinear Analysis: Real
World Applications, 10(1):458–482, 2009.



## Page 26


Charles Pierre
[9] Z. Cai, J. Mandel, and S. McCormick. The ﬁnite volume element method for diﬀusion
equations on general triangulations. SIAM J. Numer. Anal., 28:392–403, 1991.
[10] R.H. Clayton, O. Bernus, E.M. Cherry, H. Dierckx, F.H. Fenton, L. Mirabella, A.V.
Panﬁlov, F.B. Sachse, G. Seemann, and H. Zhang. Models of cardiac tissue elec-
trophysiology: Progress, challenges and open questions. Progress in Biophysics and
Molecular Biology, 104:22–48, 2011.
[11] J.C. Clements, J. Nenonen, P K. Li, and M. Hor´acek.
Activation dynamics in
anisotropic cardiac tissue via decoupling. Annals Biomed. Eng., 32(7):984–990, 2004.
[12] P. Colli Franzone, P. Deuﬂhard, B. Erdmann, J. Lang, and L. F. Pavarino. Adaptivity
in space and time for reaction-diﬀusion systems in electrocardiology. SIAM J. Sci.
Comput., 28(3):942–962 (electronic), 2006.
[13] P. Colli Franzone and L.F. Pavarino. A parallel solver for reaction-diﬀusion systems
in computational electrocardiology. Math. Models Methods Appl. Sci., 14(6):883–911,
2004.
[14] P. Colli-Franzone, L.F. Pavarino, and B. Taccardi. Simulating patterns of excitation,
repolarization and action potential duration with cardiac Bidomain and Monodomain
models. Math. Biosci., 197(1):35–66, 2005.
[15] P. Colli-Franzone and G. Savar´e. Degenerate evolution systems modeling the cardiac
electric ﬁeld at micro- and macroscopic level. Evolution equations, semigroups and
functional analysis, 2002.
[16] M. Ethier and Y. Bourgault. Semi-implicit time discretization schemes for the bido-
main model. SIAM Journal of Numerical Analysis, 46(5):2443–2468, 2008.
[17] L. Gerardo-Giorda, L. Mirabella, F. Nobile, M. Perego, and A. Veneziani. A model-
based block-triangular preconditioner for the bidomain system in electrocardiology.
J. Comput. Phys., 228(10):3625–3639, 2009.
[18] L. Gerardo-Giorda, M. Perego, and A. Veneziani. Optimized Schwarz coupling of
bidomain and monodomain models in electrocardiology. M2AN, 2010.
[19] L. Grasedyck and W. Hackbusch. Construction and arithmetics of H-matrices. Com-
puting, 70(4):295–334, 2003.
[20] L. Grasedyck, R. Kriemann, and S. Le Borne. Parallel black box H-LU precondi-
tioning for elliptic boundary value problems. Comput. Vis. Sci., 11(4-6):273–291,
2008.
[21] W. Hackbusch. Multigrid methods and applications, volume 4 of Springer Series in
Computational Mathematics. Springer-Verlag, Berlin, 1985.



## Page 27


Preconditioning the bidomain model
[22] W. Hackbusch and B. N. Khoromskij. Towards H-matrix approximation of linear
complexity. 121:194–220, 2001.
[23] W. Krassowska and J.C. Neu. Homogenization of syncytial tissues. CRC Crit. Rev.
Biomed. Eng., 21(2):137–199, 1993.
[24] P. Le Guyader, F. Trelles, and P. Savard. Extracellular measurement of anisotropic
bidomain myocardial conductivities. I. theoretical analysis. Annals Biomed. Eng.,
29(10):862–877, 2001.
[25] C.H. Luo and Y. Rudy. A Dynamic Model of the Cardiac Ventricular Action Potential
I. Simulations of Ionic Currents and Concentration Changes. Circ. Res., 74:1071–
1096, 1994.
[26] B.F. Nielsen, T.S. Ruud, G.T. Lines, and A. Tveito.
Optimal monodomain ap-
proximations of the bidomain equations. Applied Mathematics and Computation,
184:276–290, 2007.
[27] L. F. Pavarino and S. Scacchi. Multilevel additive Schwarz preconditioners for the
bidomain reaction-diﬀusion system. SIAM J. Sci. Comput., 31(1):420–445, 2008.
[28] C. Pierre and Y. Bourgault. Comparing the bidomain and monodomain models in
electro-cardiology through convergence analysis. HAL Preprint, http://hal.archives-
ouvertes.fr/hal-00545888/fr/, 2010.
[29] M. Potse, B. Dube, J. Richer, A. Vinet, and RM. Gulrajani.
A comparison of
monodomain and bidomain reaction-diﬀusion models for action potential propagation
in the human heart. IEEE Trans. Biomed. Eng., 53(12):2425–2435, 2006.
[30] A. J. Pullan, M. L. Buist, and L. K. Cheng. Mathematically modelling the electrical
activity of the heart. World Scientiﬁc Publishing, 2005.
[31] A. Quarteroni and A. Valli. Domain decomposition methods for partial diﬀerential
equations. 1999. Oxford Science Publications.
[32] O. Rousseau. Geometrical modeling of the heart. PHD Thesis, University of Ottawa,
2010.
[33] O. Rousseau and Y. Bourgault. Heart segmentation with an iterative Chan-Vese
algorithm. HAL Preprint, http://hal.archives-ouvertes.fr/hal-00403627/fr/, 2009.
[34] Y. Saad.
Iterative methods for sparse linear systems.
Society for Industrial and
Applied Mathematics, Philadelphia, PA, second edition, 2003.
[35] S. Sanfelici. Convergence of the galerkin approximation of a degenerate evolution
problem in electrocardiology. Numer. Methods for Partial Diﬀerential Equations,
18:218–240, 2002.



## Page 28


Charles Pierre
[36] V. V. Shaidurov. Some estimates of the rate of convergence for the cascadic conjugate-
gradient method. Comput. Math. Appl., 31(4-5):161–171, 1996.
[37] N.P. Smith, M.L. Buist, and A.J. Pullan. Altered t wave dynamics in contracting
cardiac model. J. Cardiovascular Electrophysio., 14:5203–5209, 2003.
[38] J. Sundnes, B.F. Nielsen, K.A. Mardal, X. Cai, G.T. Lines, and A. Tveito. On the
computational complexity of the bidomain and the monodomain models of electro-
physiology. Annals of Biomedical Engineering, 34:1088–1097, 2006.
[39] L. Tung. A bidomain model for describing ischemic myocardial D-D properties. Ph.D.
thesis, M.I.T.., 1978.
[40] M. Veneroni. Reaction-diﬀusion systems for the microscopic cellular model of the
cardiac electric ﬁeld. Math. Methods Appl. Sci., 29(14):1631–1661, 2006.


---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]