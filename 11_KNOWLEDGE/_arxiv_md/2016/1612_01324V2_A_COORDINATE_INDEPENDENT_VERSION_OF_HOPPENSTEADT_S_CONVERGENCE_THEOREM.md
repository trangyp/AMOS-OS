---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1612.01324v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1612.01324v2_A_coordinate-independent_version_of_Hoppensteadt_s_convergence_theorem

> Source: 1612.01324v2_A_coordinate-independent_version_of_Hoppensteadt_s_convergence_theorem.pdf

> Pages: 26

---


## Page 1


arXiv:1612.01324v2  [math.CA]  15 Mar 2017
A coordinate-independent version of
Hoppensteadt’s convergence theorem
Christian Lax, Katrin Seliger, Sebastian Walcher
Lehrstuhl A für Mathematik
RWTH Aachen
52056 Aachen, Germany
April 3, 2018
Abstract
The classical theorems about singular perturbation reduction (due
to Tikhonov and Fenichel) are concerned with convergence on a com-
pact time interval (in slow time) as a small parameter approaches zero.
For unbounded time intervals Hoppensteadt gave a convergence theo-
rem, but his criteria are generally not easy to apply to concrete given
systems.
We state and prove a convergence result for autonomous
systems on unbounded time intervals which relies on criteria that are
relatively easy to verify, in particular for the case of a one-dimensional
slow manifold. As for applications, we discuss several reaction equa-
tions from biochemistry.
MSC2010: 34E15, 92C45, 34C45
Keywords: singular perturbations, reduction, reaction system, Lyapunov
1
Introduction
Singular perturbation phenomena occur frequently in the modelling and
analysis of chemical or biological systems, in particular for reaction equa-
tions, and are highly relevant for reducing the dimension of a problem. For
reaction equations (involving a small parameter ε), such phenomena may
often be interpreted in the context of quasi-steady state (QSS) or partial
equilibrium approximations (PEA). In many instances, the classical work of
1


## Page 2


Tikhonov [24] and Fenichel [6] provides a method to obtain a reduced equa-
tion.
The theorems of Tikhonov and Fenichel guarantee convergence on some ﬁxed
compact time interval as ε →0. But beyond this result, in many applications
one expects convergence for all positive times after a short initial phase, i.e.
with slow time ranging in [τ0, ∞) for some τ0 > 0. (In general convergence
does not hold on an unbounded interval; see Fenichel [6], p. 68 for a well-
known example involving the van der Pol equation).
Hoppensteadt [13] stated and proved a convergence theorem for singularly
perturbed systems which guarantee convergence on unbounded intervals, es-
sentially resolving the matter up to coordinate transformations. However, in
many potential applications these transformations (which eﬀect a separation
of variables into “slow” and “fast”) cannot be determined explicitly, and the
hypotheses of the theorem are diﬃcult to verify. In fact, even if a system
is given in slow-fast coordinates, Hoppensteadt’s crucial conditions may not
be readily veriﬁable. In the literature one ﬁnds some applications of this
theorem where an explicit coordinate transformation is determined and the
validity of Hoppensteadt’s conditions is veriﬁed directly. Thus, Cavallo and
Natale [4], Teel et al. [23], and Back and Shim [2] discuss applications to
control theory. For the classical Michaelis-Menten enzyme model (with low
enzyme concentration), no doubt was ever expressed about the validity of the
reduction for all positive times, and the direct estimates given in Segel and
Slemrod [20] do imply convergence for the case of irreversible product for-
mation. For the reversible case, it seems that a convergence proof was given
only relatively recently, in [19]. This proof uses Hoppensteadt’s criteria, and
the crucial part invokes explicit knowledge of a ﬁrst integral for the fast
system. The argument cannot be extended to familiar variants of Michaelis-
Menten, e.g. those including inhibition or cooperativity. One purpose of the
present work is to provide more easily applicable criteria for reaction systems.
The paper is organized as follows. We start the main section (Section
2) with an auxiliary result on Lyapunov functions and asymptotic stability.
Then we proceed to a version of Hoppensteadt’s theorem for autonomous
systems that are written in slow-fast coordinates with special properties.
Following this, we do not only specialize (and thus simplify) Hoppensteadt’s
conditions for autonomous systems but we also replace one of the conditions
with another that is somewhat stronger, but readily veriﬁable. We next re-
call Tikhonov-Fenichel reduction for singularly perturbed systems with no
a priori separation of slow and fast variables [9]. Finally we give additional
conditions which guarantee convergence to solutions of the reduced system
2


## Page 3


on unbounded intervals, with Theorem 2.7 the main result. Some of the con-
ditions we impose (e.g. eigenvalue conditions) are relatively easy to verify in
applications, but for others veriﬁcation may still be problematic. In particu-
lar this concerns the existence of a global parameterization of the asymptotic
slow manifold, and the existence of a Lyapunov function for the reduced sys-
tem on this manifold. But at least for the case of a one-dimensional slow
manifold, which is highly relevant for QSS in biochemistry, these problems
can be resolved completely, and one obtains readily applicable criteria. In
Section 3 we discuss a number of examples.
Some of the results presented are based on work in the theses [21] and [15].
The Appendix (Section 5) contains a list of Hoppensteadt’s conditions and
the corresponding theorem for easy reference.
2
Hoppensteadt’s theorem for autonomous systems
The goal of this section is to state and prove a version of Hoppensteadt’s
convergence theorem [13] for autonomous systems which is readily applica-
ble to the investigation of a reasonably large class of diﬀerential equations.
In the main result we will not require any a priori separation of fast and
slow variables, and we will focus on conditions that are amenable to explicit
veriﬁcation.
We ﬁrst prove an auxiliary result on Lyapunov functions, and then an au-
tonomous version of the convergence theorem for special slow-fast coordi-
nates, before turning to a general coordinate-free version. The result is, in
particular, easily applicable to systems with a one-dimensional slow mani-
fold.
Let U ⊂Rm be open, and p ∈C1(U; Rm).
We consider the diﬀerential
equation
x′ = p(x)
(2.1)
on U, with the prime (here and in the following) denoting diﬀerentiation
with respect to the independent variable τ.
2.1
An auxiliary result
Lemma 2.1. Let Y ⊂Rm be a submanifold and bK ⊂U compact such that
Y ∩bK is positively invariant with respect to (2.1). Assume there exists a
neighborhood S ⊂U of Y ∩bK and a function ϕ ∈C1(S) that satisﬁes the
following conditions:
3


## Page 4


(i) The inequality ϕ(x) ≥0 holds for all x ∈Y ∩bK, and there exists exactly
one z ∈Y ∩bK such that ϕ(z) = 0.
(ii) Given a norm ∥·∥on Rm there exist c1, c2 > 0, a positive integer a,
and ρ > 0 such that for all x ∈Y ∩Bρ(z) the inequalities
c1 ∥x −z∥a ≤ϕ(x) ≤c2 ∥x −z∥a
are satisﬁed. (Here z is from (i), and Bρ(z) denotes the open ball with
center z and radius ρ.)
(iii) There exist ν > 0 and k ≥1 such that the Lie derivative of ϕ with
respect to p satisﬁes
Lp(ϕ)(x) ≤−νϕ(x)k
for all x ∈Y ∩bK. (Recall Lp(ϕ)(x) = Dϕ(x) · p(x) for all x.)
Then there exists c > 0 such that for all x0 ∈Y ∩bK, x0 ̸= z the solution
Φ(τ, x0) of the initial value problem x′ = dx
dτ = p(x), x(0) = x0 satisﬁes the
inequality
∥Φ(τ, x0) −z∥≤c ∥x0 −z∥γ(τ),
with
γ(τ) =
 e−ντ/a
for
k = 1,
((k −1)ντϕ(x0)k−1 + 1)1/[a(1−k)]
for
k > 1
strictly decreasing to 0 as τ →∞.
Proof. The function
ϕ(x)
∥x −z∥a
is continuous on bK ∩{x ∈Rm; ∥x −z∥≥ρ} and therefore bounded below
and above by positive constants. Hence there exist 0 < c∗
1 < c∗
2 such that for
all x ∈Y ∩bK the inequalities
c∗
1 ∥x −z∥a ≤ϕ(x) ≤c∗
2 ∥x −z∥a
(2.2)
hold.
Now use condition (iii) and recall a result on diﬀerential inequalities (e.g.
Amann [1], Lemma 16.4): Since the initial value problem
w′ = −νwk,
w(0) = ϕ(x0) > 0
4


## Page 5


in R is solved by
eγ(τ) =
 ϕ(x0)e−ντ
for
k = 1,
((k −1)ντ + ϕ(x0)1−k)1/(1−k)
for
k > 1,
the solution Φ(τ, x0) satisﬁes
ϕ(Φ(τ, x0)) ≤eγ(τ) ≤c∗
2 ∥x0 −z∥a γ(τ)
due to (ii). By virtue of (2.2) we obtain
∥Φ(τ, x0) −z∥≤

1
c∗
1 ϕ(Φ(τ, x0))
1/a
≤
 c∗
2
c∗
1
1/a
∥x0 −z∥γ(τ).
The assertion follows.
2.2
Systems in Tikhonov standard form
Here we will prove an intermediate result for systems written in special co-
ordinates. With the exception of (ASII) below, the conditions are patterned
after Hoppensteadt [13], conditions (I) through (VII).
In the following denote by |·|1 the 1-norm, let s and r be positive integers
and m = s + r. For R > 0 we deﬁne
SR
:=
{y = (y1, y2) ∈Rs+r, |y|1 = |y1|1 + |y2|1 ≤R},
S1,R
:=
{y1 ∈Rs, |y1|1 ≤R},
S2,R
:=
{y2 ∈Rr, |y2|1 ≤R}.
(2.3)
We consider a singularly perturbed autonomous system in Tikhonov stan-
dard form
y′
1 = f(y1, y2, ε)
(2.4)
y′
2 = ε−1g(y1, y2, ε)
(2.5)
as well as its counterpart in fast time t = τ/ε, viz.
˙y1 = εf(y1, y2, ε)
(2.6)
˙y2 = g(y1, y2, ε)
(2.7)
subject to the following conditions:
(AS0) Both f and g are C2 functions in an open subset eU of Rs × Rr × R,
and eU contains SR × [0, ε0) for some R > 0 and ε0 > 0.
5


## Page 6


(ASI) The system
y′
1 = f(y1, y2, 0)
(2.8)
0 = g(y1, y2, 0)
(2.9)
admits the stationary point 0 ∈Rs × Rr.
(ASII) For all y1 ∈S1,R one has g(y1, 0, 0) = 0, and there is a constant ν > 0
such that all eigenvalues of D2g(y1, 0, 0) have real part ≤−ν.
(Here and in the following Di denotes the partial derivative with re-
spect to yi.)
(ASIII) The hypotheses of Lemma 2.1 hold with p(y) = f(y1, 0, 0), Y
=
{(y1, 0) ∈SR} and z = 0.
Invoking a compactness argument, it would suﬃce in (ASII) to require that
the eigenvalues of D2g(y1, 0, 0) have real part < 0 for all y1 ∈S1,R.
Proposition 2.2. Whenever assumptions (AS0) through (ASIII) hold, there
exists a compact neighborhood K × [0, ε∗
0] ⊆SR × [0, ε0) of 0 ∈Rs+r+1 with
the following properties: Given y0 := (y1,0, y2,0) ∈K and ε ∈(0, ε∗
0], the
solution Φ(τ, y0) of (2.4)–(2.5) exists for 0 ≤τ < ∞.
As ε →0, this
solution converges uniformly on all closed subsets of (0, ∞) to the solution
of (2.8)–(2.9) with respect to the initial value y1(0) = y1,0.
Proof. One has to verify conditions (I) through (VII) in Hoppensteadt [13];
for the reader’s convenience these are recalled in Section 5 below. Clearly
(AS0) and (ASI), together with the fact that the system is autonomous,
ensure that conditions (I) through (V) hold. (In the autonomous case the
uniformity requirements follow readily by continuity and compactness.) Con-
dition (VI) is a consequence of (ASIII) and Lemma 2.1.
There remains to show that (ASII) implies the validity of (VII). In principle
one could refer to Fenichel [6], but we give a proof with some details here.
(i) From g(y1, 0, 0) = 0 for all y1 ∈S1,R and by Hadamard’s Lemma (see
e.g. Nestruev [18], Lemma 2.8) there exists a C1 function bR such that
g(y1, y2, 0) = bR(y1, y2)y2
for all (y1, y2) ∈SR. Furthermore
bR(y1, y2)y2 = (A(y1) + R(y1, y2)) y2
where y1 7→A(y1) = bR(y1, 0) ∈Rr×r is C1 and ∥R(y1, y2)∥→0 as
∥y2∥→0, uniformly in y1.
According to (ASII), for y1 ∈S1,R all
eigenvalues of A(y1) have real part ≤−ν < 0.
6


## Page 7


(ii) We denote by φ(·, ·) the standard Euclidean scalar product on Rr, and
thus have
φ(y2, y2) = ∥y2∥2
2.
Denote by C the unit sphere in Rr with respect to ∥· ∥2. For every y1
there exists a θ(y1) > 0 such that
2φ(y2, A(y1)y2)
≤
−2θ(y1)∥y2∥2
2
for all y2 ∈Rr,
2φ(y2, A(y1)y2)
≤
−2θ(y1)
for all y2 ∈C.
The proof of the ﬁrst inequality follows by the arguments in Walter [25]
(§30, IV(d) and proof of §29, VIII). These imply that there exists some
positive deﬁnite symmetric bilinear form ψ such that
2ψ(y2, A(y1)y2) ≤−ν/2 · ψ(y2, y2) for all y2,
and the assertion follows by the equivalence of all norms on Rr. The
second inequality is a simple consequence but it shows that one can
choose −2θ(y1) as the maximum of the left hand side function on C.
(iii) Given y∗
1 ∈S1,R there exists a neighborhood U(y∗
1) such that
φ(y2, A(y1)y2) ≤−θ(y∗
1)∥y2∥2
2 for all y2 ∈Rr, y1 ∈U(y∗
1).
This follows by the estimates in (ii), the continuity of the map
S1,R × C →R,
(y1, y2) 7→φ(y2, A(y1)y2),
and the homogeneity of φ. In conjunction with the compactness of S1,R
this estimate implies the existence of some β > 0 such that
φ(y2, A(y1)y2) ≤−2β∥y2∥2
2 for all (y1, y2) ∈SR.
(iv) Moreover there exists ρ > 0 such that
|2φ(y2, R(y1, y2)y2)| ≤β · ∥y2∥2
2 for all y1 ∈S1,R, y2 ∈S2,ρ
due to uniform convergence with respect to y1 (again, see Walter [25],
loc.cit.). Altogether one obtains
Lg(φ)(y2) = 2φ(y2, A(y1)y2) + 2φ(y2, R(y1, y2)y2) ≤−β∥y2∥2
2
for all (y1, y2) ∈S1,R × S2,ρ.
7


## Page 8


(v) Denote the solution of x′
2 = g(y1, x2, 0) with initial value y2 by Γ(y1, y2, τ).
Then by Amann [1], Lemma 16.4 one ﬁnds
φ(Γ(y1, y2, τ)) ≤∥y2∥2
2 · exp(−βτ),
hence
∥Γ(y1, y2, τ)∥≤∥y2∥· exp(−βτ/2).
Hoppensteadt’s condition (VII) follows via the equivalence of all norms
on Rr.
Remark 1. Hoppensteadt [13] develops his conditions (for non-autonomous
systems) from a more general setting in a step-by-step manner, with cer-
tain normalizations (that can not necessarily be carried out explicitly) being
invoked at various stages; see Section 5. Eventually his crucial conditions
require the special setting which we consider above (and furthermore restrict
to autonomous systems).
2.3
General systems
The goal of this subsection is to extend Proposition 2.2 to settings where no
a priori separation of “slow” and “fast” variables is given. Thus we consider
a system
˙x = h(x, ε) = h(0)(x) + εh(1)(x) + ε2h∗(x, ε)
(2.10)
with right-hand side C2 in (x, ε), and (x, ε) is in some open subset of Rm×R
that contains (x0, 0) for some x0. We will also work with the time-scaled
version (τ = εt as in subsection 2.2), thus
x′ = dx
dτ = ε−1h(x, ε) = ε−1h(0)(x) + h(1)(x) + . . .
(2.11)
of this equation. We ﬁrst recall a coordinate-free version of standard (Tikhonov-
Fenichel) singular perturbation reduction from [9], Theorem 1. (The theo-
rem was stated for systems with rational right-hand side, but as noted in [9],
Remark 2, suﬃcient diﬀerentiability already guarantees existence.) The fol-
lowing conditions are relevant.
(TF0) There exists a point x0 in the zero set V(h(0)) such that rank Dh(0)(x) =
r < m for all x ∈Rm in some neighborhood of x0.
8


## Page 9


Remark 2. By the implicit function theorem, (TF0) implies the existence of
a neighborhood U of x0 such that V := U ∩V(h(0)) is a (m −r)-dimensional
submanifold.
(TFI) There is a direct sum decomposition
Rm = ker Dh(0)(x) ⊕im Dh(0)(x)
for all x ∈V . (In other words, one requires that algebraic and geomet-
ric multiplicity of the eigenvalue zero of Dh(0)(x) are equal.)
For details and proofs concerning the next two results we refer to [9].
Proposition 2.3. Let (TF0) and (TFI) be given. Then the following hold.
(a) (Product decomposition) On some neighborhood eU ⊆U of x0 there exist
C1 maps
P : eU →Rm×r
and
µ: eU →Rr
with rank P(x0) = rank Dµ(x0) = r, such that
h(0)(x) = P(x)µ(x),
x ∈eU.
Moreover, the zero set Y of µ satisﬁes Y = V ∩eU = V(h(0)) ∩eU. The
entries of µ may be taken as any r entries of h(0) that are functionally
independent at x0.
(b) The system
x′ = q(x) := Q(x) · h(1)(x)
(2.12)
with
Q(x) := Id −P(x)(Dµ(x)P(x))−1Dµ(x),
is deﬁned in eU, and the manifold Y is an invariant set of (2.12). More-
over, every entry of µ is a ﬁrst integral of (2.12).
We will call (2.12) the Tikhonov-Fenichel reduction of (2.11). The result
holds for every connected component of Y , hence we may and will assume
that Y is connected.
Remark 3. (a) Conditions (TF0) and (TFI) ensure the existence of a co-
ordinate transformation that puts (2.11) into Tikhonov standard form,
and the reduced system (2.12) corresponds to the familiar reduction with
slow and fast variables; see [19].
9


## Page 10


(b) As was shown in [9], for rational h(0) one may choose P and µ rational,
and the decomposition can be obtained constructively by methods of
algorithmic algebra.
The next condition guarantees local convergence of solutions to solutions
of the reduced system.
(TFII) All nonzero eigenvalues of Dh(0)(x), x ∈Y , have negative real part.
With these assumptions one can state a coordinate-free local version of
(Tikhonov’s and) Fenichel’s reduction theorem; see [9], Theorem 1.
Proposition 2.4. Assume that (TF0), (TFI) and (TFII) hold. Then there
exists T > 0 and a neighborhood U ∗⊂U of Y such that solutions of (2.11)
starting in U ∗converge uniformly on [τ0, T] to solutions of the reduced system
(2.12) on Y as ε →0, for any τ0 with 0 < τ0 < T.
Remark 4. (a) The submanifold V is called the asymptotic slow manifold
(or critical manifold).
(b) Concerning the question of ﬁnding the appropriate initial values on
Y (which was in principle also settled by Fenichel [6], Theorem 9.1),
we brieﬂy summarize the discussion in [9] Proposition 2: The system
˙x = h(0)(x) admits m −r independent ﬁrst integrals in a neighborhood
of x0, and the intersection of a common level set of the ﬁrst integrals
with Y consists (locally) of a single point. To project an initial value of
system (2.10) to an initial value of (2.12) on Y , choose the correspond-
ing intersection point. Thus, a solution of (2.11) starting at x0 ∈U ∗
converges to the solution of (2.12) starting at the projected initial value.
(c) In the situation of Proposition 2.4 we sometimes call (2.12) a convergent
Tikhonov-Fenichel reduction of (2.11); in contrast to a formal reduction
whenever only (TF0) and (TFI) hold.
(d) The proof of Proposition 2.4 (see [19] Proposition 2.3 and [9] Theo-
rem 1) shows that the coordinate transformation which puts (2.11) into
Tikhonov standard form (see Remark 3 (a)) also maps solutions of the
reduced system (2.12) to solutions of the corresponding reduced system
(2.8)–(2.9) in Tikhonov standard form.
Up to this point we focussed on conditions which ensure convergence of
singular perturbation reduction on some compact subinterval of (0, ∞). We
now introduce additional conditions to guarantee validity of the reduction on
10


## Page 11


unbounded intervals. The ﬁrst of these conditions could be weakened, but it
is convenient for applications and it is satisﬁed for many relevant systems,
in particular reaction systems.
(CIS) There exists a compact neighborhood K ⊆eU of x0 which is positively
invariant for all diﬀerential equations (2.10) with 0 < ε < ε0.
By continuous dependence one obtains:
Lemma 2.5. Under the assumptions of Proposition 2.4 and given condition
(CIS), the set K ∩Y is positively invariant for the reduced system (2.12).
Next come the crucial conditions.
(GP) There exists a contractible open subset W of Rs, s = m −r, and a
global injective C2 immersion Λ∗: W →Y .
Remark 5. (a) We introduce condition (GP) to make the reasoning more
transparent, and in order to state the following Lemma in a more general
context. But below we will introduce a further condition (LC) which
actually implies (GP). Indeed, as an argument in the proof of Theorem
2.7 will show, by global asymptotic stability there exists a ﬂow on W
which contracts to a point (see also Corollary 2.8).
(b) We (may and) will assume that S1,R ⊆W for some R > 0.
(c) In the statement of (GP) one may replace Y by a relatively open neigh-
borhood of Y ∩K in Y .
Lemma 2.6. Under the assumptions of Proposition 2.4 and given conditions
(CIS) and (GP) there is a compact set K∗⊇K ∩Y with nonempty interior,
some 0 < ρ ≤R and a C2-diﬀeomorphism
Λ: Sρ →K∗,
with Λ|S1,ρ×{0} = Λ∗|S1,ρ×{0}.
(Thus, there are open neighborhoods of Sρ resp. K∗that are mapped to each
other by Λ and its inverse.)
Proof. The normal bundle N of Y is trivial, since W is simply connected;
see Hirsch [11], Ch. 4, Corollary 2.5. Now the assertion follows by injectivity
of Λ∗and Hirsch [11], Ch. 4, Theorem 5.1.
The ﬁnal condition we require is as follows.
11


## Page 12


(LC) The reduced system (2.12) admits one and only one stationary point
z in Y ∩K, and the conditions in Lemma 2.1 are satisﬁed.
With these assumptions the convergence statement of Proposition 2.2
carries over.
Theorem 2.7. For system (2.11) assume that (TF0)–(TFII) as well as
(CIS), (GP) and (LC) are satisﬁed. Then there exist a compact eK ⊆Λ(Sρ)
with nonempty interior, z ∈eK, and ε∗
0 > 0 with the following properties:
Given y0 ∈eK and 0 < ε < ε∗
0, the solution Φ(t, y0) of (2.4)–(2.5) exists for
0 ≤t < ∞. As ε →0, this solution converges uniformly on all closed subsets
of (0, ∞) to the solution of (2.12) with initial value according to Remark 4
b).
Proof. Use Λ: Sρ →K∗to deﬁne
eh(x, ε) := DΛ(x)−1h(Λ(x, ε)).
By construction, the diﬀeomorphism Λ sends solutions of ˙x = eh(x, ε) to so-
lutions of ˙x = h(x, ε); and it is suﬃcient to verify conditions (AS0) through
(ASIII) for the former system.
(i) For ε = 0 one has the identity
DΛ(x)eh(0)(x) = h(0)(Λ(x)),
with eh(0)(x) := eh(x, 0). Let x = (x1, x2), with x1 ∈Rs and x2 ∈Rr.
Since Λ extends Λ∗, we have
eh(0)((x1, 0)) = DΛ((x1, 0))−1h(0)(Λ((x1, 0))) = 0,
and we obtain the conjugacy property
Deh(0)((x1, 0)) = DΛ((x1, 0))−1Dh(0)(Λ((x1, 0)))DΛ((x1, 0))
by diﬀerentiation, noting that the second term on the right hand side
vanishes due to h(0)(Λ((x1, 0))) = 0.
(ii) Moreover ˙x = eh(0)(x) may be assumed to be in the particular form
˙x1
=
0
˙x2
=
g(0)(x1, x2)
12


## Page 13


with g(0)(x1, 0) = 0. In other words, ˙x = eh(x, ε) is in Tikhonov stan-
dard form and (AS0), (ASI) hold.
To verify this, note that (TFII) holds and use Fenichel [6], Lemma 5.3.
(A diﬀerent proof for analytic systems makes use of the fact that the
diﬀerential equation ˙x = eh(0)(x) admits s independent ﬁrst integrals in
the neighborhood of any stationary point; see [19], Proposition 2.2.)
(iii) By conjugacy of Jacobians, (TFII) and compactness one sees that
(ASII) is satisﬁed.
(iv) There remains to verify the existence of a Lyapunov function so that
(ASIII) holds. The reduced system corresponding to eh will be called
x′ = eq(x). It has the special form
x′
1
=
f (1)(x1, 0)
x′
2
=
0
with the slow manifold being given by x2 = 0. Due to Remark 4 (d),
the map Λ sends solutions of ˙x = eq(x) to solutions of ˙x = q(x). Now
the Lyapunov function ϕ for q satisﬁes Lq(ϕ) ≤−ν · ϕk, and with the
well-known identity
Leq(ϕ ◦Λ) = Lq(ϕ) ◦Λ
one obtains that eϕ := ϕ ◦Λ is a Lyapunov function for eq, and that the
inequality
Leq(eϕ) ≤−ν eϕk
holds. Moreover, obviously eϕ ≥0 with 0 the only zero. Finally, since
Λ−1 is a diﬀeomorphism and its derivative is bounded on the com-
pact set Sρ, the mean value estimate shows the existence of positive
constants k1 and k2 such that
k1 ∥x −z∥≤


Λ−1(x) −Λ−1(z)


 ≤k2 ∥x −z∥
for all x ∈Sρ. This implies condition (ii) from Lemma 2.1.
Corollary 2.8. If Y is the graph of some smooth function Γ: W →Rr,
with W ⊆Rm−r contractible and open, and (CIS) and (LC) are satisﬁed in
addition to (TF0)–(TFII), then (GP) and thus the conclusion of Theorem
2.7 hold.
Remark 6. In the setting of Theorem 2.7, it suﬃces to require the existence
of a Lyapunov function ϕ for q on Y ∩K (rather than in some neighborhood
of Y ), since eϕ can be extended to Sρ by setting bϕ(x1, x2) := eϕ(x1).
13


## Page 14


2.4
One-dimensional slow manifolds
For a general system (2.11) the veriﬁcation of condition (LC) on Y a pri-
ori requires explicit knowledge of a Lyapunov function. However, for one-
dimensional slow manifolds a simple condition will imply (LC). We ﬁrst note
a property of diﬀerential equations on real intervals which is essentially com-
mon knowledge (since diﬀerential equations in R are gradient systems); a
proof is included for the reader’s convenience.
Lemma 2.9. Let U ⊆R be an open interval containing 0, and p ∈C1(U)
with p(0) = 0. Moreover let K ⊂U be compact with 0 ∈K, and 0 the only
stationary point of x′ = p(x) in K. If 0 is linearly asymptotically stable (i.e.
p′(0) < 0) then
eϕ(x) = −
Z x
0
p(y) dy
is a Lyapunov function of x′ = p(x) which satisﬁes the hypotheses of Lemma
2.1 on K, with a = 2 and k = 1.
Proof. By Hadamard’s lemma
p(x) = x · bp(x), with bp continuous and bp(0) = −θ < 0;
moreover bp is negative throughout K. This implies that K is positively in-
variant and that eϕ is nonnegative, with 0 its only zero. In some neighborhood
eU of 0 one has the estimates
−2θ · x ≤p(x) ≤−θ/2 · x for x > 0,
−θ/2 · x ≤p(x) ≤−2θ · x for x < 0,
which imply
θ/2 · x2 ≤eϕ(x) ≤2θ · x2
for all x ∈eU. Therefore condition (ii) from Lemma 2.1 holds on K, since
eϕ and Lp(eϕ) are continuous and the complement of eU in K is compact. By
construction Lp(eϕ)(x) = −p2(x), and the above estimate shows
Lp(eϕ)(x) = −x2 · 4θ2
in eU, whence conditions (ii) and (iii) in Lemma 2.1 hold in eU with a = 2
and k = 1, and (by compactness and continuity arguments) on all of K.
Now we can state our result.
14


## Page 15


Proposition 2.10. For system (2.11) assume that (TF0)–(TFII) and (CIS)
are satisﬁed. Moreover assume that Y ∩K is one-dimensional, connected,
contains exactly one stationary point z, and that the linearization of the
reduced equation ˙x = q(x) at z admits a negative eigenvalue.
Then the
conclusion of Theorem 2.7 holds.
Proof. We ﬁrst note that the one-dimensional compact and connected mani-
fold is homeomorphic to a compact interval or to a circle; see e.g. Milnor [17].
But the latter is incompatible with the existence of a single stationary point
that is asymptotically stable. The curve Y admits a global parameterization
by curve length, and therefore (GP) is satisﬁed. According to Proposition
2.3, there are m −1 functionally independent deﬁning equations for Y near
any of its points, and these are ﬁrst integrals for the reduced equation (see
also Proposition 2.4). Therefore the linearization at z admits the eigenvalue
0 with geometric multiplicity ≥m−1 at z, and the eigenspace of the nonzero
(negative) eigenvalue must be equal to the tangent space to Y at z. Now
Lemma 2.9 and Theorem 2.7 apply.
3
Examples
In this section we will discuss some reaction equations, with an emphasis on
one-dimensional slow manifolds. Let Rn
+ be the set of all vectors x ∈Rn
with nonnegative entries. Moreover, the concentration of a chemical species
Z will be denoted with a lowercase letter z.
3.1
Michaelis-Menten reaction and variants
The well-known (reversible) Michaelis-Menten reaction is deﬁned by the re-
action scheme
E + S
k1
−−⇀
↽−−
k−1 C
k2
−−⇀
↽−−
k−2 E + P;
see Michaelis and Menten [16], and also Briggs and Haldane [3]. The con-
centrations of each chemical species will be denoted by the corresponding
lower-case letter.
By mass-action kinetics, using the linear ﬁrst integrals
e + c and s + c + p from stoichiometry and assuming that initially no com-
plex C or product P are present, one obtains the following two-dimensional
problem:
˙s = −k1e0s + (k1s + k−1)c
˙c = k1e0s −(k1s + k−1 + k2)c + k−2(e0 −c)(s0 −s −c).
15


## Page 16


3.1.1
Small enzyme concentration
The standard approach takes the assumption of small initial enzyme con-
centration e0 = εe∗
0. By the results in [19] and [8], there exists a convergent
Tikhonov-Fenichel reduction to
s′ = −e∗
0
(k1k2 + k−1k−2)s −k−1k−2s0
k1s + k−1 + k2 + k−2(s0 −s) ,
the slow manifold being V = {(s, 0) ∈R2
+}. Using an explicit transformation
to Tikhonov standard form and employing some straightforward but elab-
orate computations, convergence on unbounded time intervals was already
proven in [19]. (As mentioned before, Segel and Slemrod [20] gave a proof
by direct estimates for the irreversible case k−2 = 0.) We use this example
only to illustrate how Proposition 2.10 greatly simpliﬁes convergence proofs.
Indeed, the validity of (TF0)–(TFII) and (CIS) is easy to verify, and clearly,
the reduced equation admits exactly one stationary point
s∗=
k−1k−2s0
k1k2 + k−1k−2
which is linearly asymptotically stable. Thus, Proposition 2.10 shows con-
vergence (with the irreversible case included for k−2 = 0.)
3.1.2
Slow product formation for the irreversible system
There are other choices for a “small parameter” that yield convergent Tikhonov-
Fenichel reductions of the Michaelis-Menten reaction (see [10] for an exhaus-
tive discussion). All of these admit one-dimensional slow manifolds and it
is easy to check the validity of the hypotheses of Proposition 2.10. For in-
stance, assuming slow, irreversible product formation (i.e., k2 = εk∗
2 small
and k−2 = 0), one ﬁnds the reduction
s′ =
−(k1s + k−1)k1k∗
2e0s
k1k−1e0 + (k1s + k−1)2 ,
on V = {(s, c) ∈R2
+, k1e0s = (k1s + k−1)c}. Again, Proposition 2.10 is
applicable to show convergence on [τ0, ∞) for any τ0 > 0.
3.1.3
Competitive inhibition
As an extension of the Michaelis-Menten model we discuss an irreversible
enzyme reaction with inhibition (see e.g.
Keener and Sneyd [14]).
The
16


## Page 17


reaction scheme is given by
E + S
k1
−−⇀
↽−−
k−1
C1
k2
−→E + P
E + I
k3
−−⇀
↽−−
k−3
C2.
We assume the usual initial values c1(0) = c2(0) = 0, s(0) = s0 > 0,
e(0) = e0 > 0 and i(0) = i0 > 0. Using the linear ﬁrst integrals
ψ1(e, s, c1, c2, p, i) = e + c1 + c2,
ψ2(e, s, c1, c2, p, i) = s + c1 + p,
ψ3(e, s, c1, c2, p, i) = i + c2
from stoichiometry, one obtains a three-dimensional system. Again we as-
sume that the initial enzyme concentration is low, thus e0 = εe∗
0, and obtain
the diﬀerential equation
˙s
=
k−1c1 + k1s(c1 + c2)
−
εe∗
0k1s
˙c1
=
−k1s(c1 + c2) −(k−1 + k2)c1
+
εe∗
0k1s
˙c2
=
−k3(c1 + c2)(i0 −c2) −k−3c2
+
εe∗
0k3(i0 −c2)
The reduction was computed in [8], subsection 3.2; in particular (TF0)-
(TFII) (GP) and (CIS) hold for the slow manifold Y deﬁned by c1 = c2 = 0,
and the reduced equation
s′ = −e∗
0
k1k2k−3s
k−3(k1s + k−1) + (k−1 + k2)k3i0 + k2k−3
admits the only stationary point 0, which is linearly asymptotically stable.
By Proposition 2.10 we obtain convergence on every interval [τ0, ∞), with
τ0 > 0. (The same holds true for reversible product formation.)
For this system the method employed in [19] is not feasible, since an explicit
transformation to Tikhonov standard form (in particular the requisite ﬁrst
integrals) seems to be unavailable.
3.2
Maltose transport
In order to further illustrate the range of applicability of Proposition 2.10,
we discuss an example which is less straightforward from a computational
perspective. Thus, we continue the discussion in [9], Section 4, of a reaction
equation proposed by Stiefenhofer [22] for maltose transport. According to
the model, in order to pass through the cell membrane, a maltose molecule X
17


## Page 18


ﬁrst reacts with a binding protein Z to a complex Y1. The latter reacts with
the membrane-bound receptor R, forming a complex Y2, which subsequently
degrades, releasing maltose into the cell. This last process is modelled by a
reaction involving the maltose concentration Xi in the interior of the cell.
Moreover, Stiefenhofer assumes a direct reaction between the binding protein
and the membrane receptors, modelled by a further reaction. Altogether, the
transport mechanism is modelled by the network
Y2
k1
−→R + Z + Xi,
Z + X
k2
−−⇀
↽−−
k−2 Y1
Y1 + R
k3
−−⇀
↽−−
k−3
Y2,
Z + R
k4
−−⇀
↽−−
k−4
Y3.
In order to reduce notational and computational complexity, we follow Stiefen-
hofer by setting all rate constants equal to to 1, except for k1 = ε. More-
over we deﬁne v := (x, z, r, ξ, y1, y2, y3), ¯v := (ξ, y1, y2, y3) and assume
y1(0) = y2(0) = y3(0) = 0. Now we can use the stoichiometric ﬁrst inte-
grals
ψ1(v) = z + y1 + y2 + y3,
ψ2(v) = r + y2 + y3,
ψ3(v) = x + ξ + y1 + y2
to write the reaction rates in the form
ˆE1(v) = −y2 =: E1(¯v),
ˆE2(v) = y1 −zx
= y1 −(z0 −(y1 + y2 + y3))(x0 + ξ0 −(ξ + y1 + y2)) =: E2(¯v)
ˆE3(v) = y2 −y1r
= y2 −y1(r0 −(y2 + y3)) =: E3(¯v)
ˆE4(v) = y3 −zr
= y3 −(z0 −(y1 + y2 + y3))(r0 −(y2 + y3)) =: E4(¯v).
Thus the reaction is described by the following system
˙ξ = −εE1(¯v)
˙y1 = −E2(¯v) + E3(¯v)
˙y2 = εE1(¯v) −E3(¯v)
˙y3 = −E4(¯v).
18


## Page 19


As proven in [9], there exists a (formal) reduction to
ξ′ = y2
y′
1 = y2(y1 + y2 + y3 −z0)
n(¯v)
y′
2 = −y2 −y2(ξ −ξ0 + 2(y1 + y2) + y3 −(x0 + z0 + 1))
n(¯v)
y′
3 = y2((y2 + y3)(y1 + y2 + y3 −r0 −z0) + r0(z0 −y1))
n(¯v)
where
n(¯v) = ξ0 −ξ + (y1 + y2 + y3 −z0)(y2 + y3 −r0 −1) −(y1 + y2) + 1 + x0.
The system is given on K := L ∩Y , where
L := {¯v ∈R4
+, y1 + y2 + y3 ≤z0, y2 + y3 ≤r0, ξ + y1 + y2 ≤ξ0 + x0}
is the chemically relevant region (determined by stoichiometry) and the curve
Y := {¯v ∈R4
+, E2(¯v) = E3(¯v) = E4(¯v) = 0}
is the slow manifold.
We ﬁrst complete the discussion in [9] by showing that all nonzero eigenvalues
of the Jacobian have negative real parts; in particular we have convergence
of the reduction. To this end, note that with ε = 0 the Jacobian of the
reaction equation can be written as




0
0
0
0
∗
−1 −a −b −c
−a −b + 1 + d
−a + d
∗
c
−1 −d
−d
∗
−c
−b −c
−1 −b −c




with
a
:=
x0 + ξ0 −(ξ + y1 + y2)
b
:=
z0 −(y1 + y2 + y3)
c
:=
r0 −(y2 + y3)
d
:=
y1
all of which are nonnegative in view of the ﬁrst integrals ψ1, ψ2 and ψ3 and
nonnegativity of concentrations. The characteristic polynomial
x3 + A1x2 + A2x + A3
19


## Page 20


of the lower right 3 × 3 minor has all roots with negative real parts if (and
only if) A1 > 0, H2 := A1A2 −A3 > 0 and A3 > 0; see the Hurwitz-Routh
criterion (Gantmacher [7], Ch. V, §6). A straightforward computation (using
the Maple software package) shows
A1
=
3 + 2b + 2c + d + a
H2
=
a2b + a2c + a2d + 3 ab2 + 7 abc + 4 abd + 3 ac2 + 4 acd
+
ad2 + 2 b3 + 7 b2c + 3 b2d + 7 bc2 + 6 bcd
+
bd2 + 2 c3 + 3 c2d + cd2 + 2 a2 + 10 ba + 9 ca + 6 da + 10 b2
+
21 cb + 10 db + 9 c2 + 10 cd + 2 d2 + 8 a + 16 b + 14 c + 8 d + 8
A3
=
b2c + bc2 + bcd + ba + ca + da + b2 + 2 cb + db + a + 2 b + c + d + 1
and the nonnegativity of a, . . . , d implies positivity of A1, H2 and A3. Thus
condition (TFII) holds.
Now we address global convergence. No explicit parameterization of Y
seems to be known. Nonetheless in [9] the existence of exactly one stationary
point in K was shown, and also its linear asymptotic stability on Y and
global asymptotic stability on K. By Theorem 2.10 we obtain the desired
convergence result.
3.3
A two-dimensional slow manifold
Some variants of Michaelis-Menten may lead to two-dimensional slow man-
ifolds, depending on the parameters. We consider again competitive inhi-
bition with irreversible product formation (see subsection 3.1.3), but now
with small parameters k1 = εk∗
1, k−1 = εk∗
−1 and k2 = εk∗
2. The diﬀerential
equation is
˙s = ε

k∗
−1c1 −k∗
1s(e0 −c1 −c2)

˙c1 = ε

k∗
1s(e0 −c1 −c2) −(k∗
−1 + k∗
2)c1

˙c2 = k3(e0 −c1 −c2)(i0 −c2) −k−3c2
on the (chemically relevant) positively invariant compact set
L := {(s, c1, c2) ∈R3
+, c1 + c2 ≤e0, s + c1 ≤s0, c2 ≤i0}.
20


## Page 21


A short computation (see [10], p. 1175 f.) shows that (TFII) is satisﬁed, and
that there exists a convergent Tikhonov-Fenichel reduction to
s′ = k∗
−1c1 −k∗
1s(e0 −c1 −c2)
(3.1)
c′
1 = k∗
1s(e0 −c1 −c2) −(k∗
−1 + k∗
2)c1
(3.2)
c′
2 = −(i0 −c2)[k∗
1s(e0 −c1 −c2) −(k∗
−1 + k∗
2)c2]
κ + e0 + i0 −c1 −2c2
(3.3)
in L ∩Y with the two-dimensional asymptotic slow manifold
Y := {(s, c1, c2) ∈R3
+, (e0 −c1 −c2)(i0 −c2) −κc2 = 0}
and κ := k−3
k3 . (Note that κ + e0 + i0 −c1 −2c2 > 0 on L ∩Y .)
Thus, with
c2 = ϑ(c1) := κ + e0 + i0 −c1 −
p
(κ + e0 + i0 −c1)2 −4i0(e0 −c1)
2
, (3.4)
L ∩Y is contained in the graph of a function of s and c1, and it suﬃces to
analyze (3.1)–(3.2) in the positively invariant compact set
eL := {(s, c1) ∈R2
+, c1 + ϑ(c1) ≤e0, s + c1 ≤s0, ϑ(c1) ≤i0}.
We will abbreviate this system as
 s
c1
′
= q
 s
c1

.
It is easy to see that (0, 0) is the only stationary point in eL. We construct a
suitable Lyapunov function. Let α > 0 and note that
ϕ1
:=
s + c1
satisﬁes
Lq(ϕ1) = −k∗
2c1,
ϕ2
:=
αs
satisﬁes
Lq(ϕ2) = α(k∗
−1 + k∗
1s)c1 −αk∗
1s(e0 −ϑ(c1)).
On L ∩Y we have 0 ≤k∗
−1 + k∗
1s ≤k∗
−1 + k∗
1s0, and furthermore e0 −c2 > 0.
The ﬁrst of these assertions is obvious.
To verify the second, note that
e0 −c1 −c2 ≥0 by stoichiometry, whence e0 −c2 = 0 implies c1 = 0 and, by
the deﬁning equation for Y ,
0 = (e0 −c1 −c2)(i0 −c2) = κc2 = κe0 > 0,
a contradiction.
By compactness, there exists β > 0 such that e0 −c2 ≥β for all points in L.
Now choose α > 0 such that
α · (k∗
−1 + k∗
1s0) < k∗
2,
21


## Page 22


and deﬁne ϕ := ϕ1 + ϕ2. Then, by the previous estimates we have on eL:
Lq(ϕ)(s, c1)
≤
−(k∗
2 −α · (k∗
−1 + k∗
1s0))c1 −αk∗
1βs
≤
−ν · ((1 + α)s + c1) = −ν · ϕ
for some ν > 0. Thus (LC) holds, and by Theorem 2.7 convergence to the
reduced system holds for all positive times.
4
Concluding remarks
We ﬁnish with a few observations, and some comments on possible extensions
and generalizations.
• The results of the present paper will be hardly surprising to application-
oriented readers (e.g. with a background in biochemistry) although
the underlying mathematical argument (essentially due to Hoppen-
steadt [13]) is far from trivial, and not easy to transfer to applications.
This gap between intuition (where matters may seem obvious) and rig-
orous proofs (which may require an extensive technical build-up) can
be observed quite frequently. The authors’ main goal was to facilitate
the applicability of Hoppensteadt’s theorem to relevant settings.
• By its nature Theorem 2.7 is local, but the domain of attraction of Y
may properly contain eK. There remains, however, the question how
fast a solution approaches the slow manifold.
In the setting of reaction equations it is known from the work of Horn
and Jackson [12] and Feinberg [5] that global Lyapunov functions of-
ten exist; for instance this is the case for deﬁciency zero and complex
balanced systems. Given a system with slow and fast reactions, a Lya-
punov function for the fast subsystem could imply a condition akin to
Hoppensteadt’s condition (VII), with reasoning similar to (and extend-
ing) Lemma 2.1. But the Lyapunov functions from the cited papers do
not generally satisfy the hypotheses of the Lemma; thus a case-by-case
analysis would be in order.
• In Lemma 2.9, if K is a neighborhood of 0 then it suﬃces that p changes
sign at 0, with the lowest (necessarily odd) order nonzero derivative at
0 being negative. By analogous estimates one obtains conditions (ii)
and (iii) of Lemma 2.1, with exponents a > 2 and k > 1. In order to
transfer this to systems with one-dimensional slow manifold one would
have to generalize Proposition 2.10 by requiring suitable properties of
the Poincaré-Dulac normal form at z.
22


## Page 23


5
Appendix: Hoppensteadt’s conditions
For the reader’s convenience we recall here the conditions and the main result
from Hoppensteadt’s original paper [13]. Recall the notation SR from (2.3).
Hoppensteadt considers a non-autonomous system that is given in Tikhonov
standard form
y′
1 = f(τ, y1, y2, ε)
(5.1)
y′
2 = ε−1g(τ, y1, y2, ε)
(5.2)
with f and g deﬁned on an open set
[0, ∞) × D × [0, ε0) ⊆[0, ∞) × Rs × Rr × [0, ε0) →Rr
which satisﬁes SR ⊆D for some R > 0, and f, g having values in Rs and
Rr, respectively. Assume that the following conditions hold:
(I) The system
y′
1 = f(τ, y1, y2, 0)
(5.3)
0 = g(τ, y1, y2, 0)
(5.4)
admits a solution Y : [0, ∞) →Rs+r, τ 7→Y (τ). With a suitable
transformation of (5.3)–(5.4) one may assume that eY ≡0 is a solution
of the transformed system.
From here on, it will be assumed that
(5.3)–(5.4) admits the solution eY ≡0.
(II) The functions f, g and their partial derivatives with respect to τ, y1,
y2 respectively satisfy
f, g, D1f, D2f, ∂τg, D1g, D2g ∈C([0, ∞) × SR × [0, ε0]).
(III) There exists an isolated and bounded C2-solution Y2 = Y2(τ, y1) of the
implicit equation
g(τ, y1, Y2(τ, y1), 0) = 0
for all τ ∈[0, ∞) and y1 ∈S1.
By a transformation ey1 = y1 and
ey2 + Y (τ, y1) = y2, one may obtain that Y2(τ, ey1) = 0 for all (τ, ey1) ∈
[0, ∞) × S1. This will be assumed for the original system (5.1)–(5.2)
in the following.
(IV) f(·, ·, 0, 0) is uniformly continuous in [0, ∞)×S1,R, and moreover f(·, ·, 0, 0)
and D1f(·, ·, 0, 0) are bounded in [0, ∞) × S1,R.
23


## Page 24


(V) g(·, ·, ·, 0) is uniformly continuous in [0, ∞)×SR, and moreover g(·, ·, ·, 0),
∂τg(·, ·, ·, 0), D1g(·, ·, ·, 0) D2g(·, ·, ·, 0) are bounded in [0, ∞) × SR.
(VI) The solution eY ≡0 of
y′ = f(τ, y, 0, 0)
(5.5)
is uniformly asymptotically stable in the following sense: There exist
a continuous, strictly increasing function
d: [0, ∞) →[0, ∞)
with d(0) = 0
and a continuous, strictly decreasing function σ: [0, ∞) →[0, ∞) with
lims→∞σ(s) = 0, such that for every solution Φ(τ, z) of (5.5) with
initial value y1(0) = z ∈S1,R and all τ ≥0 one has
|Φ(τ, z)|1 ≤d(|z|1) · σ(τ).
(VII) For all (α, β) ∈[0, ∞) × S1,R the solution eY ≡0 of
˙x = g(α, β, x, 0)
is uniformly asymptotically stable in the following sense: There exist
a continuous, strictly increasing function
e: [0, ∞) →[0, ∞)
with e(0) = 0
and a continuous, strictly decreasing function ρ: [0, ∞) →[0, ∞) with
lims→∞ρ(s) = 0, such that for every solution Ψ(t, x0; α, β) of the equa-
tion with initial value x(0) = x0 ∈S2,R and parameters (α, β) ∈
[0, ∞) × S1,R and all t ≥0 one has
|Ψ(t, x0; α, β)|1 ≤e(|x0|1) · ρ(t).
Given these assumptions, Hoppensteadt’s main result [13] can be stated
as follows:
Theorem 5.1. There exists a compact neighborhood K ⊂SR of 0 and ε∗
0 ∈
(0, ε0) such that the solution Φ(t, y0, ε) of (5.1)–(5.2) with initial value y(0) =
y0 := (y1,0, y2,0) ∈K at τ = 0 exists for all positive times provided that
0 < ε < ε∗
0. Moreover Φ(t, y0, ε) converges uniformly on all closed subsets of
(0, ∞) towards the solution of (5.3)–(5.4) with initial value y1(0) = y1,0, as
ε →0.
24


## Page 25


References
[1] H. Amann: Ordinary Diﬀerential Equations. An Introduction to Non-
linear Analysis. Walter de Gruyter, Berlin - New York (1990).
[2] J. Back, H. Shim: Adding robustness to nominal output-feedback con-
trollers for uncertain nonlinear systems: A nonlinear version of distur-
bance observer. Automatica 44, 2528–2537 (2008).
[3] G. E. Briggs and J. B. S. Haldane. A note on the kinetics of enzyme
action. Biochem. J., 19:338–339, 1925.
[4] A. Cavallo, C. Natale: Output feedback control based on a high-order
sliding manifold approach. IEEE Transactions on Automatic Control
48, 469–472 (2003).
[5] M. Feinberg: The existence and uniqueness of steady states for a class
of chemical reaction networks. Arch. Ration. Mech. Anal. 132, 311–370
(1995).
[6] N. Fenichel: Geometric singular perturbation theory for ordinary diﬀer-
ential equations. J. Diﬀerential Equations 31, 53–98 (1979).
[7] F.R. Gantmacher: Applications of the theory of matrices. Dover Publ.,
Mineola, NY (2005).
[8] A. Goeke, C. Schilli, S. Walcher, E. Zerz: Computing quasi-steady state
reductions. J. Math. Chem. 50, 1495–1513 (2012).
[9] A. Goeke, S. Walcher: A constructive approach to quasi-steady state
reductions. J. Math. Chem. 52, 2596–2626 (2014).
[10] A. Goeke, S. Walcher, E.
Zerz: Determining “small parameters” for
quasi-steady state. J. Diﬀerential Equations 259, 1149–1180 (2015).
[11] M.W. Hirsch: Diﬀerential Topology. Springer, New York (1976).
[12] F. Horn, R. Jackson: General mass action kinetics. Arch. Ration. Mech.
Anal. 47, 8–116 (1972).
[13] F.C.
Hoppensteadt: Singular Perturbations on the Inﬁnite Interval.
Trans. Amer. Math. Soc. 123, 521–535 (1966).
[14] J. Keener, J. Sneyd: Mathematical physiology I: Cellular physiology,
Second Ed. Springer-Verlag, New York (2009).
25


## Page 26


[15] C. Lax: Analyse und asymptotische Analyse von Kompartimentsyste-
men. Doctoral dissertation, RWTH Aachen (2016).
[16] L. Michaelis and M. L. Menten.
Die Kinetik der Invertinwirkung.
Biochem. Z., 49:333–369, 1913.
[17] J.W. Milnor:
Topology from the Diﬀerentiable Viewpoint. Princeton
University Press, Princeton (1997).
[18] J. Nestruev: Smooth manifolds and observables. Springer, New York
(2003).
[19] L. Noethen, S.
Walcher: Tikhonov’s theorem and quasi-steady state.
Discrete Contin. Dyn. Syst. Ser. B 16, 945–961 (2011).
[20] L.A. Segel, M. Slemrod: The quasi-steady-state assumption: A case
study in perturbation. SIAM Review 31, 446 - 477 (1989).
[21] K. Seliger: Singuläre Störungen auf unbeschränkten Intervallen. Mas-
ter’s thesis, RWTH Aachen (2015).
[22] M. Stiefenhofer: Quasi-steady-state approximation for chemical reaction
networks. J. Math. Biol. 36, 593–609 (1998).
[23] A.R. Teel, L. Moreau, D. Nesic: A uniﬁed framework for input-to-state-
stability in systems with two time scales. IEEE Transactions on Auto-
matic Control 48, 1526–1544 (2003).
[24] A.N. Tikhonov: Systems of diﬀerential equations containing a small
parameter multiplying the derivative (in Russian). Math. Sb. 31, 575–
586 (1952).
[25] W. Walter: Ordinary diﬀerential equations. Springer-Verlag, New York
(1998).
26

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]