---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1705.06785v3
source: arxiv
tags: [arxiv, fractal, knowledge, math, reference]
---
# 1705.06785v3_Robust_persistence_and_permanence_of_polynomial_and_power_law_dynamical_systems

> Source: 1705.06785v3_Robust_persistence_and_permanence_of_polynomial_and_power_law_dynamical_systems.pdf

> Pages: 26

---


## Page 1


arXiv:1705.06785v3  [math.DS]  21 Nov 2017
ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL
AND POWER LAW DYNAMICAL SYSTEMS
JAMES D. BRUNNER
AND GHEORGHE CRACIUN
Abstract.
A persistent dynamical system in Rd
>0 is one whose solutions have positive lower
bounds for large t, while a permanent dynamical system in Rd
>0 is one whose solutions have uniform
upper and lower bounds for large t.
These properties have important applications for the study
of mathematical models in biochemistry, cell biology, and ecology.
Inspired by reaction network
theory, we deﬁne a class of polynomial dynamical systems called tropically endotactic. We show that
two-dimensional tropically endotactic polynomial dynamical systems are permanent, irrespective of
the values of (possibly time-dependent) parameters in these systems. These results generalize the
permanence of two-dimensional reversible, weakly reversible, and endotactic mass action systems.
1. Introduction. Polynomial dynamical systems are used to model many phys-
ical, chemical, and biological processes. For example, systems of polynomial diﬀeren-
tial equations have come into use in the modeling and simulation of large biochemical
networks, population dynamics, and epidemiology [11][19]. The study of chemical and
biochemical reaction network models is especially concerned with dynamical systems
which have polynomial right-hand sides [12].
In order to understand global long term behavior of solutions of polynomial dy-
namical systems, we seek to determine whether or not solutions with positive ini-
tial conditions remain bounded, and bounded away from zero. A dynamical system
on Rd
>0 is said to be persistent if for any solution x(t) with x(0) ∈Rd
>0, we have
lim inft→∞xi(t) > 0 for all i ∈{1, ..., d}. In the context of population modeling, this
means that no species becomes extinct. The stronger property permanence means
that there exists a compact region R which does not intersect ∂Rd
>0 such that any
solution x(t) with x(0) ∈Rd
>0 ultimately resides inside R. In other words, there ex-
ists a compact attracting region in Rd
>0. Clearly, permanence implies persistence, and
additionally it implies that solutions are uniformly bounded, and uniformly bounded
away from ∂Rd
>0.
In recent work, it has been shown that two dimensional weakly reversible and
endotactic polynomial dynamical systems are permanent [10]. We will extend these
results to the larger class of tropically endotactic polynomial and power law dynam-
ical systems.
This class of dynamical systems has the advantage of being robust
with respect to changes in the parameters of the systems, which is often useful in
applications, because, in practice, it is often diﬃcult or impossible to measure these
parameters accurately. In future work, we will show that the tropically endotactic
condition is very close to being necessary and suﬃcient for permanence.
Other results about persistence of polynomial dynamical systems that result from
chemical reaction networks have been obtained by using Petri net-based methods
[3].
Furthermore, results about the global convergence properties of solutions to
polynomial dynamical systems that result from reaction networks have been obtained
by taking advantage of special properties of these networks[1][2][5][9][13][14][17][20].
In general, polynomial dynamical systems ∗have the form
(1)
˙x =
n
X
i=1
xsivi
∗Note that if we restrict si ∈Zd
≥0, then (1) is exactly the set of polynomial dynamical systems.
In this paper we allow the more general case si ∈Rd, often called power law systems.
1


## Page 2


2
J. D. BRUNNER AND G. CRACIUN
where x = (x1, ..., xd) ∈Rd, si ∈Rd, and vi ∈Rd. Vector exponentials in Rd of the
form xs are deﬁned by
(2)
xs =
d
Y
j=1
xsj
j
Here, we are concerned with the more general class of dynamical systems of the form
(3)
˙x =
n
X
i=1
κi(t)xsivi,
where we allow the coeﬃcients κi(t) ∈R to vary in time, but we assume that there
exist some ε > 0 such that ε < κi(t) < 1
ε for all t > 0. We refer to such systems as
variable κ polynomial (vκ-polynomial) dynamical systems.
In the analysis of vκ-polynomial dynamical systems, we make use of a special class
of diﬀerential inclusions. In general, diﬀerential inclusions are dynamical systems of
the form
(4)
˙x ∈F (x)
where F (x) is a set-valued map. Here, we introduce a class of diﬀerential inclusions
which captures the dynamics of the polynomial dynamical systems we are interested
in. These diﬀerential inclusions are called N-cone diﬀerential inclusions, where b
N =
log(N) is a complete fan in Rd (see Deﬁnitions 2.1 to 2.3 and Figure 1). N-cone
diﬀerential inclusions are piecewise constant in Rd
>0 on regions determined by b
N ∈b
N.
Furthermore they are autonomous and consist of a convex cone K(N) at each point
x in the region determined by b
N. If f(x, t) ∈F (x) for all x and t we say that the
dynamical system ˙x = f(x, t) is embedded in the diﬀerential inclusion ˙x ∈F (x).
Clearly, if a dynamical system is embedded in a diﬀerential inclusion, then solutions
of the dynamical system are also solutions of the diﬀerential inclusion. In particular,
if the solutions of a diﬀerential inclusion are persistent or permanent, then the same
is true for the solutions of a dynamical system embedded in it.
We show that if a two dimensional N-cone diﬀerential inclusion ˙x ∈F (x) is
tropically endotactic (see Deﬁnition 2.9) then its solutions remain bounded and do
not approach ∂R2
>0. This implies that if a vκ-polynomial dynamical system can be
embedded into a tropically endotactic diﬀerential inclusion, then its solutions are also
bounded and do not approach ∂R2
>0. Moreover, we then show that if this embedding
is strict (see Deﬁnition 2.6) then the polynomial dynamical system has the stronger
property of permanence. Finally, we give examples of polynomial dynamical systems
which are embedded in tropically endotactic diﬀerential inclusions.
More speciﬁcally, in order to study the persistence of an N-cone diﬀerential in-
clusion, we identify sets of “escape directions” Bδ(N) for each set N ∈N. Informally
speaking, these are directions along which trajectories may escape any compact region
that does not intersect ∂Rd
>0 while staying inside N (see Deﬁnition 2.8 and Figure 2
for details). For example, if the closure of N contains the y-axis, Bδ(N) contains any
vector v such that v · (1, 0) < 0 (i.e., the left half plane).
We deﬁne tropically endotactic diﬀerential inclusions by comparing the cones
K(N) of an N-cone diﬀerential inclusion to the escape directions Bδ(N) corresponding
to N.
We call a diﬀerential inclusion tropically endotactic when K(N) does not


## Page 3


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
3
intersect the interior of Bδ(N)† for all N ∈N (see Deﬁnition 2.9 and for an example
see Figure 11). This condition is easy to check in two dimensions. Furthermore, it
provides a suﬃcient condition for persistence of solutions of a diﬀerential inclusion:
Theorem 1.1. Let ˙x ∈F(x) be a diﬀerential inclusion deﬁned on R2
>0. If ˙x ∈
F(x) is tropically endotactic, then it is persistent and has bounded trajectories.
Therefore, we can use a tropically endotactic diﬀerential inclusion to conclude
persistence of a vκ-polynomial dynamical system which is embedded in it. We can
also obtain a stronger result when the embedding is into the interiors of the sets of
the diﬀerential inclusion. If ˙x = f(x, t) has the property that f(x, t) ∈F (x)◦for
every x and t, where F (x)◦is the interior of F (x), then we say that ˙x = f(x, t) is
strictly embedded in the diﬀerential inclusion ˙x ∈F (x). If a vκ-polynomial dynamical
system is strictly embedded in a tropically endotactic diﬀerential inclusion, we call
it a tropically endotactic vκ-polynomial dynamical system. We prove the following
theorem, which states that being tropically endotactic is a suﬃcient condition for
permanence of a (possibly non-autonomous) vκ-polynomial dynamical system:
Theorem 1.2. Any two-dimensional tropically endotactic vκ-polynomial dynam-
ical system is permanent.
Finally, we give examples of systems which are not endotactic but which are
tropically endotactic, and therefore permanent. We also show that Theorem 1.2 is
a generalization of the permanence of weakly reversible two dimensional systems as
described in [7].
2. Diﬀerential inclusions.
2.1. Piecewise Constant Cone Diﬀerential Inclusions. A diﬀerential in-
clusion is a dynamical system
˙x ∈F (x)
where F is a set-valued map. We are interested in the special case in which F (x) is
a cone, and is constant on regions of R2
>0.
We use a fan in R2 to deﬁne a cover of R2 and R2
>0. Deﬁnitions of fans and
cones follow [23] and [6]. With a set S ⊆Rd we associate the set Cone(S), the cone
generated by S, which we deﬁne as the closure of the set of all ﬁnite, nonnegative
linear combinations of the elements of S [6] ‡.
We will be concerned with the cones generated by ﬁnite sets of vectors S =
{v1, ..., vk}. In this case, a cone K is
K =
(
w =
k
X
i=1
aivi
 ai ≥0
)
and is called a polyhedral cone. In what follows, we will simply use the word “cone”
to mean polyhedral cone.
A cone K is solid if the interior of K is non-empty. A supporting hyperplane H of
a cone K is a hyperplane that intersects K at the origin and such that K is contained
in only one of the two half-spaces determined by H. A face of K is the intersection
between K and a supporting hyperplane.
†along with a technical condition on the cones K(N) and K(M) when c
M is a face of b
N
‡We use the deﬁnition from [6] and [23], which deﬁnes cones to be closed and convex. In other
sources, cones are not necessarily convex.


## Page 4


4
J. D. BRUNNER AND G. CRACIUN
Definition 2.1. [23] A fan (or polyhedral fan) in Rd is a ﬁnite family
b
N =
{ b
N1, b
N2, ..., b
Nn} of nonempty polyhedral cones such that:
(i) Every nonempty face of a cone in b
N is also a cone in b
N .
(ii) The intersection of any two cones in b
N is a face of both.
If the union of cones in the fan N is Rd, then N is called a complete fan. Because
we are concerned only with complete fans, we will use the word fan to mean complete
fan. A complete fan is a cover of Rd, and moreover, the collection of relative interiors
of the cones of the fan forms a partition of Rd. We can use a cover of Rd given by a
complete fan to construct a cover of Rd
>0, as described below.
Definition 2.2. A ﬁnite family of sets N = {N1, N2, ..., Nk} in Rd
>0 is called an
exponential fan if there exists a complete fan b
N = { b
N1, b
N2, ..., b
Nk} in Rd such that
Ni = exp( b
Ni) for i = 1, ..., k.
Notice that, because the map exp : Rd →Rd
>0 is bijective, an exponential fan deﬁnes
a cover of Rd
>0, and the collection of relative interiors form a partition of R2
>0. See
Figure 1 (a) and (b) for examples of a fan and exponential fan, respectively.
Given an exponential fan N of R2
>0, before we can deﬁne an N-cone diﬀerential
inclusion, we must deﬁne diﬀerent covers fat̺( b
N) and fat ̺(N) of R2 and R2
>0 re-
spectively, for some number ̺ ∈(0, 1), as in Figure 1 (c) and (d). First, we deﬁne a
compact region around the origin
(5)
fat̺(0) =
n
X ∈R2|dist(X, b
Nj) ≤| log(̺)|, for at least
two one-dimensional cones b
Nj
o
Then, we “fatten” the one dimensional cones of the fan b
N. Denote by R◦the interior
of a region R ⊂R2. For each one dimensional cone b
Nj of b
N, we deﬁne
(6)
fat̺( b
Nj) =
n
X ∈R2|dist(X, b
Nj) ≤| log(̺)|
o
\ fat̺(0)◦
which is a strip centered around b
Nj with an area near the origin removed. Finally,
we also must take into account regions in the two dimensional cones not included in
these strips. We thus deﬁne, for two dimensional cones b
Ni,
(7)
fat ̺( b
Ni) = b
Ni \


[
b
Nj|dim( b
Nj)≤1
fat̺( b
Nj)


◦
That is, fat ̺( b
Ni) is obtained from the original two dimensional cone b
Ni by removing
the regions fat̺( b
Nj) for lower dimensional cones b
Nj (except for the borders, so that all
regions remain closed). Then, we deﬁne fat̺( b
N) = {fat̺( b
Ni)| b
Ni ∈b
N}. See Figure 1
(c) for examples of the regions fat̺( b
Ni).


## Page 5


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
5
(a)
(b)
(c)
(d)
Fig. 1: (a) A fan b
N, which contains 13 cones b
Ni; 6 of these are one dimensional, 6 are
two dimensional, and one (the origin) is zero dimensional. (b)The exponential fan N =
exp( b
N). (c)The regions fat̺( b
Ni). The regions corresponding the two dimensional cones
are shown in white, those corresponding to one dimensional cones are shown in blue, and
fat̺(0) is shown in red. (d)The regions fat ̺(Ni) = exp(fat̺( b
Ni)).
These regions can be used to construct a cover of R2
>0. That is, if b
N = { b
Ni} is a
complete fan and N = exp( b
N) is its corresponding exponential fan, then we deﬁne
(8)
fat̺(Ni) =
n
x| log(x) ∈fat̺( b
Ni)
o
where Ni = exp( b
Ni), and we deﬁne fat ̺(N) = {fat̺(Ni)|Ni ∈N}. See Figure 1 (d)
for examples of the regions fat̺(Ni).
Finally, we can now deﬁne the class of diﬀerential inclusions of interest.
Definition 2.3. Consider an exponential fan N in Rd
>0. An N-cone diﬀerential
inclusion K(N) (with parameter ̺) is a dynamical system of the form
˙x ∈
[
{N|x∈fat̺(N)}
K(N)
for some ̺ > 0, where K(N) is a cone for each N ∈N.
Diﬀerential inclusions provide a framework for sacriﬁcing precise information
about a dynamical system in order to simplify the analysis in some way. We are
interested in analyzing polynomial dynamical systems which may be non-autonomous
and highly nonlinear. Such systems are in general diﬃcult to analyze. We therefore
replace these systems with N-cone diﬀerential inclusions, which are autonomous and
piecewise constant. Then, if we have that the right-hand side of the non-autonomous
polynomial dynamical system is contained in the right-hand side of the N-cone diﬀer-
ential inclusion, the properties of solutions to the diﬀerential inclusion will be satisﬁed
by solutions to the polynomial dynamical system. In order to make this rigorous, we
deﬁne a notion of embedding.
Definition 2.4. We say a dynamical system ˙x = f(x, t) is embedded into the
diﬀerential inclusion ˙x ∈F (x) in the domain Ωif f(x, t) ∈F (x) for every x ∈Ω
and for all t.
Similarly, we can embed one diﬀerential inclusion into another.
Definition 2.5. We say a diﬀerential inclusion ˙x ∈G(x) is embedded into the
diﬀerential inclusion ˙x ∈F (x) in the domain Ωif G(x) ⊆F (x) for every x ∈Ω.


## Page 6


6
J. D. BRUNNER AND G. CRACIUN
We will need a stronger notion of embedding to obtain some conclusions about
the systems of interest.
Definition 2.6. We say a dynamical system ˙x = f(x, t) is strictly embedded
into the diﬀerential inclusion ˙x ∈F (x) in the domain Ωif f(x, t) ∈F (x)◦for every
x ∈Ωand for all t.
2.2. Persistence. We are concerned with the long term behavior of solutions
to these diﬀerential inclusions.
In particular, we want to determine if an N-cone
diﬀerential inclusion allows solutions which reach ∂R2
>0. If the diﬀerential inclusion
does not allow such solutions, we call it persistent.
Definition 2.7. A d-dimensional dynamical system is called persistent on Rd
≥0
if for any solution x(t) deﬁned on an interval I containing t = 0 with initial condition
x0 ∈Rd
>0, there exists some ε > 0 such that we have
xi(t) > ε
for all i ∈{1, ..., d} and for all t ∈I ∩[0, ∞).[10]
In particular, we will say that an N-cone diﬀerential inclusion is persistent if all
absolutely continuous functions satisfying the diﬀerential inclusion [22] have the above
property.
2.3. Escape directions. Let b
N be a complete fan and N = exp( b
N ) be its
associated exponential fan. We will construct a cone Bδ(N) for each N ∈N, referred
to as the “escape directions of N”. Consider curves C(t) which have the property that
for any compact set R ⊂R2
>0, there exists some tR such that for t > tR, C(t) ̸∈R.
We will use the notation C(t) →∂Rd
>0 for curves with this property. Notice that
curves of the form exp(rt) with r ̸= 0 satisfy exp(rt) →∂R2
>0. The curves C(t)
described below provide a more general way to leave R while staying in or close to N.
Also, we use the notation [w]n to denote the unit vector in the direction of a vector
w ∈R2 and C′(t) to mean the tangent direction to C.
More precisely, we consider C(t) = exp (rt + g(t)p) where r ∈
b
N, ∥r∥= 1,
g(t) = 1 −αe−βt, β ≥0, α ∈R, and p ∈r⊥. If C(t) is such a curve and there exists
some t0 such that log(C(t)) ⊂fat̺( b
N) for t > t0, we call C(t) a ̺-escape curve of N.
Then, we deﬁne the set of δ-escape directions for N as follows.
Definition 2.8. The set of δ-escape directions for a region N ∈N and δ > 0 is
the cone
(9)
Bδ(N) =
\
̺<1
Cone ({[C′(t)]n| C(t) is a ̺-escape curve of N, t > 1/δ})
Intuitively, these are cones with the property that, for δ suﬃciently small, if a curve
y(t) has some point y(t0) ∈fat ̺(N) and tangent y′(t) ∈Bδ(N) for t > t0, then
y(t) →∂R2
>0 and y(t) ∈fat ̺(N) for t > t0. Clearly, if such a y(t) is a solution
to an N-cone diﬀerential inclusion, the diﬀerential inclusion is not persistent or does
not have bounded trajectories. Using Deﬁnition 2.8, these directions can be explicitly
calculated. All the qualitatively diﬀerent possible cones Bδ(Ni) are shown in Figure 2.
See (22)–(26) in section 5 for an example of how to calculate some cones Bδ(Ni). Such
calculations reveal that if a region Ni is not adjacent to the lines x = 0, or y = 0, and
does not contain some part of the line y = x, then the cone Bδ(Ni) approaches either
a vertical or a horizontal half-line as δ approaches 0.


## Page 7


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
7
Fig. 2: Cones Bδ(Ni) for a representative fan. Notice that if the relative interior of Ni
contains the half-line y = x < 1, then Bδ(Ni) = −R2
>0 does not depend on δ and if the
relative interior of Ni contains the half-line y = x > 1, then Bδ(Ni) = R2
>0 does not
depend on δ. Likewise, if Ni is adjacent to the line x = 0 or the line y = 0, then Bδ(Ni)
is a half-plane that does not depend on δ. The dependence on limiting tangents of curves
of the form of C(t) inspired the adjective “tropical”[18].
2.4. Tropically Endotactic Diﬀerential Inclusions. Now, we deﬁne the
class of diﬀerential inclusions that we are most interested in.
Definition 2.9. A diﬀerential inclusion in R2
>0 is tropically endotactic if it is
embedded in some N-cone diﬀerential inclusion K(N) such that for every N ∈N \{1},
there is some δ > 0 such that
K(N) ∩Bδ(N)◦= ∅
and if N ∈N is a face of M ∈N, then K(M) ⊆K(N).
3. Persistence of tropically endotactic diﬀerential inclusions.
Theorem 3.1. Let ˙x ∈F (x) be a diﬀerential inclusion deﬁned on R2
>0.
If
˙x ∈F (x) is tropically endotactic, then it is persistent and has bounded trajectories.
Furthermore, there exists a nested family of compact regions which do not intersect
∂R2
>0 which are forward invariant under ˙x ∈F (x), and this family covers R2
>0.
We will prove this theorem by constructing a forward invariant region with a
polygonal border. We do this by choosing line segments that the tropically endotactic
diﬀerential inclusion cannot cross, and connecting these segments to form the border
of the forward invariant region. Finally, we show that there is an exhaustive nested
family of such regions. This is achieved by “expanding” the ﬁrst region outward to
cover R2
>0.
In order to prove Theorem 3.1, we will ﬁrst need to prove two lemmas. The ﬁrst
lemma allows us to pick curves through points which will be used as scaﬀolding for
the construction of a forward invariant region, as in Figure 5 and Figure 7. These
curves will also give a framework to expand the forward invariant region and show
there exists an exhaustive family of such regions.
Lemma 3.2. Let b
N ̸= 0 be a cone of the fan b
N in R2 and N = exp( b
N). For any
point x ∈fat ̺(N), there exists some curve
(10)
S(t) = {(tm1, αtm2)}
m1, m2 ∈R, α > 0


## Page 8


8
J. D. BRUNNER AND G. CRACIUN
or
(11)
S(t) = {(αtm1, tm2)}
m1, m2 ∈R, α > 0
such that for some t0 > 1, we have {S(t)|t > t0} ⊂fat̺(N) and x = S(t0).
Proof. This lemma must be proved separately for one and two dimensional cones
b
N.
Let N = exp( b
N) be one dimensional, and let m = (m1, m2) be the direction of
the ray b
N. We have that
fat ̺( b
N) ⊂
n
X|dist(X, b
N) < | log(̺)|
o
and any point X ∈
n
X|dist(X, b
N) < | log(̺)|
o
lies on a line (m1t, m2t) + β[m⊥]n,
|β| < | log(̺)|. Furthermore, if dist(X, c
M) > | log(̺)| for M ̸= N ∈N, ∥Y ∥> ∥X∥
and Y lies on the same line (m1t, m2t) + β[m⊥]n, then dist(Y , c
M) increases with
∥Y ∥, so dist(Y , c
M) > | log(̺)|. Therefore, fat̺( b
N) is a union of aﬃne half-lines.
If x ∈fat̺(N) and m1 ̸= 0, then there is one such aﬃne half-line bS(t) such that
log(x) = bS(t0) and S(t) = exp(bS(t)) can be reparameterized to satisfy (10).
If
m1 = 0, bS(t) can be chosen such that S(t) can be reparameterized to satisfy (11).
Next, let b
N be a solid cone, and let µ1 be the direction of one face and µ2 the
direction of the other. Let c
M 1 and c
M 2 be the one dimensional faces of b
N, and X be
the unique intersection point fat ̺(c
M 1) ∩fat̺(c
M 2). Then
fat ̺( b
N) = {X + t(λµ1 + (1 −λ)µ2)|λ ∈[0, 1]}
Therefore, if x ∈fat̺(N), then log(x) ∈X + t(λµ1 + (1 −λ)µ2) = X + tµ =: bS(t)
for some λ ∈[0, 1]. Then again the curve S(t) = exp(bS(t)) satisﬁes the condition in
the lemma.
In the following lemma, we show that a line that intersects two curves of the
form (10) transversally will also intersect both of these curves at points further along
(as t increases), as in Figure 3. Later, when we construct a forward invariant region
for a tropically endotactic diﬀerential inclusion in the proof of Theorem 3.1, we will
construct a set of lines that solutions of the diﬀerential inclusion cannot cross. This
lemma will allow us to arrange these lines so that they form the border of a compact
forward invariant polygon. Furthermore, this lemma will ensure that, once we have
built one forward invariant polygon with sides along lines of the form {S(τ1) + sv|s ∈
R}, we can expand it into a continuous family of forward invariant polygonal regions
with sides along lines of the form {S(τ ∗) + sv|s ∈R}, where τ ∗> τ1 (see Figure 3).
Lemma 3.3. Let S1(τ) = (τ ˜
m1, ˜ατ ˜
m2) and S2(t) = (tm1, αtm2), t, τ > 1, such
that sgn(max{m1, m2}) = sgn(max{ ˜m1, ˜m2}) ̸= 0.
§ Assume there is some v ∈R2
such that
n(S1(τ)) · v ̸= 0, ∀τ ≥τ0
&
n(S2(t)) · v ̸= 0, ∀t ≥t0
where n(Si(t)) is the normal to Si at t.¶ Let Lτ(s) = S1(τ)+sv, consider the half-line
Lτ = {Lτ(s)|s > 0}
§ Informally, sgn(max{m1, m2}) = sgn(max{ ˜m1, ˜m2}) means that either both curves S1 and S2
or neither have logarithmic images in the third quadrant (with some exceptions along the boundary
of the third quadrant).
¶ Note, n(Si(t)) · v ̸= 0, ∀t ≥t0 means that v is not tangent to the curve Si(t) for t ≥t0.


## Page 9


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
9
S1(τ)
S2(t)
S1(τ1)
S2(t1)
v
Lτ1
S1(τ ∗)
S2(γ(τ ∗))
v
Lτ ∗
n(S1(τ))
n(S2(t))
Fig. 3: Given the segment Lτ1 intersecting two curves S1(τ) and S2(t) transversally (as in
the hypothesis of Lemma 3.3), this lemma insures that for τ ∗> τ1, the segment Lτ∗,
which is parallel to Lτ1, also intersects the two curves transversally at the points S1(τ ∗)
and S2(t∗) respectively, where t∗> t1. Notice that as t∗, τ ∗increase, the segment moves
closer to ∂R2
>0.
and assume that there is some τ1 ≥τ0 such that Lτ1 ∩S2(t) ̸= ∅, and let S2(t1) =
Lτ1(s0).
Then, there exists a continuous and invertible function γ(τ) with γ(τ1) = t1
such that S2(γ(τ)) ∈Lτ, and γ(τ) is strictly monotonically increasing. Furthermore,
limτ→∞γ(τ) = ∞.
Proof. If S2(t) ∈Lτ, then
(tm1, αtm2) = (τ ˜
m1 + sv1, ˜ατ ˜m2 + sv2)
for some s, or rewritten,
tm1 −sv1 = τ ˜
m1
αtm2 −sv2 = ˜ατ ˜
m2
Because one of v1, v2 is non-zero, this is equivalent to
(12)
g(τ, t) = v1(αtm2 −˜ατ ˜m2) −v2(tm1 −τ ˜
m1) = 0
We know a solution exists at (τ1, t1). Furthermore,
∂g
∂t = v1αm2tm2−1 −v2m1tm1−1 = v ·
 αm2tm2−1, −m1tm1−1
= v · n(S2(t))
and so ∂g
∂t (t) ̸= 0 for t ≥t1. Then the implicit function theorem tells us there is a
continuous, diﬀerentiable function γ such that g(τ, γ(τ)) = 0 for τ ∈[τ1, τ ∗) for some
τ ∗. Likewise the implicit function theorem proves the existence of γ−1 locally.
Now, let t = γ(τ). Using the chain rule,
γ′(τ) = −∂g/∂τ
∂g/∂t
= v ·
 ˜α ˜m2τ ˜
m2−1, −˜m1τ ˜
m1−1
v · (αm2tm2−1, −m1tm1−1) = v · n(S1(τ))
v · n(S2(t))
where both normal vectors are on the right-hand side of their respective curve with
respect to the positive tangent direction. Notice that together, these curves form the


## Page 10


10
J. D. BRUNNER AND G. CRACIUN
boundary of a simply connected region in R2
>0. The vector n(S1(t)) is an inward
normal to this region, while n(S2(t)) is an outward normal (because these two curves
have opposite orientation along the boundary of this region). The line Lτ = {S1(τ) +
sv|s > 0} enters this region across S1(t) and exits across S2(t). This gives us the fact
that
n(S1(τ)) · v > 0, ∀τ ≥τ0
&
n(S2(t)) · v > 0, ∀t ≥t0
Therefore, γ′(τ) > 0 for τ > τ1.
To show that γ exists for [τ1, ∞), we must show that if γ exists for [τ1, τ ∗), then
γ(τ ∗) exists and is ﬁnite. To do this, it is suﬃcient to show that γ(τ) is bounded in
[τ1, τ ∗). On the interval [τ1, τ ∗), we have that
v1αγ(τ)m2 −v2γ(τ)m1 = v1 ˜ατ ˜
m2 −v2τ ˜
m1
We must now treat two diﬀerent cases.
If sgn(max{m1, m2}) = sgn(max{ ˜m1, ˜m2}) > 0, we have some M1 such that
v1 ˜ατ ˜
m2 −v2τ ˜
m1 < M1
for τ ∈[τ1, τ ∗]. Therefore, we have that
|v1αγ(τ)m2 −v2γ(τ)m1| < M1
for t ∈[τ1, τ ∗). If m1 ̸= m2, then γ(τ) must be bounded on [τ1, τ ∗) because if not,
the diﬀerence |v1αγ(τ)m2 −v2γ(τ)m1| could not be bounded. If m1 = m2, we must
have α ̸=
v2
v1 .
This is because if m1 = m2, then n(S1(τ)) is parallel to (α, −1).
Therefore, α = v2
v1 would violate the assumption that v · n(S1(τ)) ̸= 0. Therefore
|v1αγ(τ)m2 −v2γ(τ)m1| = |γ(τ)m2(v1α−v2)| < M1 again implies that γ(τ) is bounded
in [τ1, τ ∗).
If sgn(max{m1, m2}) = sgn(max{ ˜m1, ˜m2}) < 0, there are three sub-cases to
consider. Again, we have that
v1αγ(τ)m2 −v2γ(τ)m1 = v1 ˜ατ ˜
m2 −v2τ ˜
m1
and we must in all cases show that v1 ˜ατ ˜m2 −v2τ ˜
m1 cannot be 0 on the compact
interval [τ1, τ ∗].
If ˜m1 = ˜m2, we again obtain ˜α ̸= v2
v1 and can conclude v1 ˜ατ ˜
m2 −v2τ ˜m1 ̸= 0 for
τ ∈[τ1, τ ∗].
If 0 > ˜m1 > ˜m2 then we recall
0 < n(S1(τ)) · v = v1 ˜α ˜m2τ ˜m2 −v2 ˜m1τ ˜
m1
which implies that
v2τ ˜
m1 > v1 ˜α ˜m2
˜m1
> v1 ˜ατ ˜m2
and so
v1 ˜ατ ˜
m2 −v2τ ˜
m1 ̸= 0
for τ ∈[τ1, τ ∗].
The last case, that 0 > ˜m2 > ˜m1 is analogous. Finally, we have that there is
some ǫ such that
|v1αγ(τ)m2 −v2γ(τ)m1| > ǫ


## Page 11


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
11
for τ ∈[τ1, τ ∗). Once more, if m1 = m2, then α ̸= v2
v1 , and we can conclude that γ(τ) is
bounded in [τ1, τ ∗). This, along with monotonicity of γ(τ), allows us to conclude that
limτ→τ ∗γ(τ) = γ(τ ∗) exists and is ﬁnite. Therefore, whenever γ(τ) can be deﬁned on
[τ1, τ ∗), it can be extended to [τ1, τ ∗].
If we assume that γ(τ) cannot be deﬁned on [τ1, ∞), then there exists some
interval [τ1, τ ∗∗) on which γ(τ) exists but cannot be extended to τ∗∗.
This is a
contradiction, so we conclude that γ(τ) exists on [τ1, ∞). Notice that the lemma is
symmetric in τ and t, and so we have also that γ(τ) →∞as τ →∞(by repeating
the above arguments for γ−1(t) to show that γ−1(t) exists on [t1, ∞)).
Proof of Theorem 3.1. Let N be a complete fan, and K(N) an N-cone diﬀerential
inclusion satisfying the hypothesis of Deﬁnition 2.9 such that ˙x ∈F (x) is embedded
in K(N). We will construct a family of nested, forward invariant regions for K(N).
Clearly, any region which is forward invariant under K(N) is forward invariant under
any diﬀerential inclusion that is embedded in K(N).
The regions constructed will be compact, will not intersect ∂R2
>0, and will cover
R2
>0. We construct the border of one such region R and show that a nested family
exists, all other members of which properly contain R. The construction proceeds
from one region fat ̺(N) to the next in clockwise manner about the point 1 = (1, 1),
so we number the regions Ni ∈N clockwise (excluding fat̺(1) from this numbering).
We will build R to be a (not necessarily convex) polygon together with its interior.
Each side of the polygon will be chosen so that if nj is the inward normal to that side
and the side intersects fat ̺(Ni), then w ·nj ≥0 for all w ∈K(Ni). That is, the sides
will be chosen to be supporting lines of the cones K(Ni). Each corner of the polygon
∂R will be chosen to be in the interior of a region fat ̺(Ni), so any two intersecting
edges of ∂R are supporting lines of the single cone K(Ni). An application of Theorem
5.2.7 of [4] shows that R constructed in this manner is forward invariant for K(N).
According to Lemma 3.2, we may choose the vertices of the polygon ∂R on curves
Si(t) = {(tm1, αtm2)} ⊆fat ̺(Ni), m1, m2 ∈R, α > 0, for t large. In our construction,
we will choose these curves ﬁrst, and choose one point on each curve sequentially
following line segments in the direction of supporting lines of the appropriate cones
K(Ni). These line segments then form the edges of ∂R. We number these curves
clockwise with respect to a neighborhood of the point 1 (some regions fat ̺(Ni) will
have more than one curve, we then label these as S′
i and S′′
i , see Figure 5 and Figure 7).
If we can connect two curves with a segment in some direction, and these curves
satisfy the conditions given by Lemma 3.3, we can also connect them with a segment
in that direction which intersects both curves at points closer to ∂R2
>0. This allows us
to adjust our segments so that adjacent segments intersect a curve at the same point.
This will also allow us to show that there is a family of forward invariant regions that
cover R2
>0.
We must determine nj, the inward normal of ∂R along edge j, using only local
information in order to distinguish inward and outward directions before completing
the construction of R. To do this, we specify vj to be the clockwise direction of an
edge, deﬁned to mean that vj points from Si to Si+1 (or S′
i to S′′
i , see Figure 5 and
Figure 7). In this way we have speciﬁed an orientation for the edges of ∂R. Then,
for x along this segment, n(x) = nj is the unit vector perpendicular to vj such that
if we take the determinant
det(nj, vj) > 0
We will call nj the clockwise normal to the segment with direction vj, and construct


## Page 12


12
J. D. BRUNNER AND G. CRACIUN
{x = x∗}
{y = y∗}
H1
H2
Fig. 4: Sketch of how R will be constructed.
The four parts of the construction are: a
segment of x = x∗, a segment of y = y∗, the polygonal line H1, and the polygonal line
H2.
R so that the inward normal to ∂R along an edge is the clockwise normal to that
edge.
We will construct ∂R in four parts. Two of these will be segments of the lines
{x = x∗}, {y = y∗} where x∗< 1 and y∗< 1 are chosen so that they do not intersect
fat̺(1). Note that these must be supporting directions of K(Ni) in regions fat̺(Ni)
such that {X = 0, Y < 0} ⊆b
Ni and {X < 0, Y = 0} ⊆b
Ni respectively, as seen
by calculating Bδ(Ni) for such regions. To draw ∂R through other regions, we can
connect points on these lines with the other two parts of ∂R, which will be polygonal
lines H1 and H2, as in Figure 4.
Throughout the proof, we will use {ˆx, ˆy} to denote the standard basis in R2.
Construction of polygonal line H1.
Notice ﬁrst that if the third quadrant is contained in some b
N, we connect the
lines x = x∗and y = y∗and we can take H1 to be their intersection point. Otherwise,
we number regions as in Figure 5 (a).
In this numbering, we have the segment
0 < x = y < c ⊂fat ̺(Nl) for some c ∈(0, 1). Next we choose curves for each Ni with
the form
S(t) = {(tm1, αtm2)}
m1, m2 < 0
so that there is some t0 where Si(t) ⊂fat̺(Ni) for t > t0. These curves are numbered
as in Figure 5 (b). Notice two such curves are chosen inside fat̺(Nl). We take, if
possible, m1 ̸= m2 for the curves S′
l and S′′
l . If this choice is not allowed, because
such curves are not contained in fat̺(Nl), we take α < 1 for S′
l and α > 1 for S′′
l .
We need to prove the following claim for each pair of adjacent curves in Figure 5
(b) (including one or both of the curves S′
l and S′′
l ). This claim states that for any
pair of adjacent curves, there exists a choice of direction vector v for a connecting line
segment which satisﬁes the hypothesis of Lemma 3.3 and can serve as the boundary
of an invariant region for the diﬀerential inclusion K(N) in the region between these
two curves.
Claim 3.4. Let S−(t) and S+(t), with S+ clockwise of S−, be adjacent curves as
constructed above and b
Nq be the one dimensional ray such that one of S−and S+ is
contained in fat̺(Nq), or Nq = Ni if S−, S+ ⊂Ni. Denote by n(S(t)) a clockwise
normal vector to the curve S at the point S(t). Then there exists a direction v with
clockwise normal nv such that
(a) for any w ∈K(Nq), we have w · nv ≥0
(b) there exists t1 > t0 such that n(S−(t)) · v ̸= 0 for t > t1


## Page 13


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
13
N1
Nk
Nl
N2
(a) Ordering the regions Ni.
S1
S2
S′
l
S′′
l
Sk
(b) Curves S1, ..., Sk to be connected
by
supporting
lines
of
K(Ni)
shown dashed.
Fig. 5: Labeling used in the construction of H1. The qualitative diﬀerence in limiting tangent
between S1, ..., Sl−1, S′
l and S′′
l , Sl+1, ..., Sk (with the possibility that S′
l and S′′
l are straight
lines) makes it necessary to treat three diﬀerent cases.
(c) there exists t2 > t1 such that the line Lt2 = S−(t2) + sv intersects S−at a point
x = S+(τ2) where τ2 > t0
(d) n(S+(τ)) · v ̸= 0 for τ ≥τ2
S−(t)
S+(τ)
v
Lt
K(Nq)
n(S−(t))
n(S+(τ))
Fig. 6: The line Lt intersects the curves S−(t) and S+(τ).
Proof of Claim 3.4. We need to consider three cases: S−∈{S1, ..., Sl−1}, S−= S′
l,
and S−∈{S′′
l , ..., Sk}, with the ﬁrst only if l > 2.
Assume that S−= Si ∈{S1, ..., Sl−1} and let q ∈{i, i + 1} be such that Nq is
one dimensional. Let v be contained in a line that separates the cones K(Nq) and
Bδ(Nq), chosen such that v · ˆy > 0 or v = −ˆx. Such a choice is always possible
because every line through the origin in R2 either intersects the open upper half plane
or is the x-axis. Then, we see that v satisﬁes Claim 3.4 by checking the requirements
in order.
(a) There exists some vector u arbitrarily close to −ˆx in Bδ(Nq)◦, and our choice
of v is such that det(u, v) < 0. Then, because v is a direction that separates
Bδ(Nq) and K(Nq), we can conclude for w ∈K(Nq) that det(w, v) ≥0 which
implies that w · nv ≥0.
(b) We have that n(Si(t)) →ˆy, n(Si(t)) · (−ˆx) →0 monotonically, and n(Si(t)) ·
(−ˆx) ̸= 0 for all ﬁnite t > t0. There is then t1 > t0 such that n(Si(t)) · v ̸= 0 for


## Page 14


14
J. D. BRUNNER AND G. CRACIUN
t > t1.
(c) Both curves Si and Si+1 approach horizontal and converge to the origin, and the
curve Si+1 is above the curve Si. For any direction v with v · ˆy > 0, there is some
t2 > t1 such that Lt2(s) = Si(t2) + svi intersects Si+1 at Si+1(τ2), τ2 > τ1. If
v = −ˆx, we again have this intersection because Si+1 →0.
(d) As in (b), We have that n(Si+1(t)) →ˆy, n(Si+1(t)) · −ˆx →0 monotonically, and
n(Si+1(t)) · (−ˆx) > 0 for all ﬁnite t > t0.
If S−= Sl−1 and S+ = S′
l has limiting tangent −ˆx, the preceding argument is
valid. However, we may have that S′
l is a line of positive slope. Then, Bδ(Nq) = −R2
>0
and we can choose v to be the direction of a separating subspace which has v · ˆy ≥0
and v · (−ˆx) ≥0. Then (a) and (b) are as in the previous case and we have that
(c) Here, S′
l is a line of positive slope, and Sl−1 is below this line. Also, v · ˆy ≥0 and
v · (−ˆx) ≥0, so we will have the intersection desired.
(d) Because S′
l is a line of positive slope, n(S′
l) · ˆy ≥0 and n(S′
l) · (−ˆx) ≥0. The
same is true of v, so (d) is easily satisﬁed.
Next, we need to prove the claim for S−= S′
l and S+ = S′′
l . Again, Bδ(Nl) =
−R2
>0 and we can choose v to be the direction of a separating subspace which has
v · ˆy ≥0 and v ·−ˆx ≥0. Then, (a) is as in the ﬁrst cases, and if S′
l and S′′
l are lines of
positive slope, (b),(c),(d) are as in the previous case. If not, (b) is as in the previous
case, (d) is analogous, reﬂected across the line y = x (and taking −v), and lastly:
(c) Note that S′′
l is above S′
l, while v · ˆy ≥0. Furthermore, S′′
l is to the left of S′
l,
and v · −ˆx ≤0. A segment starting at S′
l in the direction of v will not intersect
S′
l again, and so the desired intersection must occur.
For S−∈{S′′
l , ..., Sk}, we can reﬂect the previous argument across the line y = x.
Reﬂection gives a counterclockwise construction of each Lt, with directions that satisfy
v · ˆx > 0 or v = −ˆy. A continuing clockwise construction would instead use −v. This
concludes the proof of Claim 3.4.
Claim 3.4 gives us a way to construct line segments that serve as a boundary of
an invariant region for K(N) within the individual regions between curves S−(t) and
S+(t). Note that two such segments in adjacent regions do not necessarily intersect.
On the other hand, results (b),(c), and (d) of the claim are three of the four condi-
tions of Lemma 3.3. Furthermore, to construct H1 we only considered curves whose
logarithmic image is contained in the third quadrant, and so the last condition of
Lemma 3.3 is also satisﬁed. Therefore, by applying Lemma 3.3 we can “slide” each
segment so that segments in adjacent regions meet at a point. Therefore, a solution
of the diﬀerential inclusion K(N) cannot cross H1 in the outward direction.
Construction of polygonal line H2.
We number regions as in Figure 7 (a). In this numbering, we have the segment
c < x = y ⊂fat̺(Np), the segment {x = 1, y > c} ⊂fat̺(No), and the segment
{x > c, y = 1} ⊂fat̺(Nr) for some c ∈(1, ∞). Next we choose curves with the form
S(t) = {(tm1, αtm2)}
where either m1 > 0 or m2 > 0 so that there is some t0 where Si(t) ⊂fat ̺(Ni) for
t > t0. These curves are numbered as in Figure 7 (b). Notice two such curves are
chosen inside each of fat̺(No), fat̺(Np), and fat̺(Nr). We choose for S′
o that m1 ≤0
and S′′
o that m1 ≥0 with strict inequality if possible. Similarly, we choose for S′
r that
m2 ≥0 and for S′
r that m2 ≤0 with strict inequality if possible. We choose for S′
p,


## Page 15


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
15
Nh
Np
Nm
No
Nr
(a) Ordering the cones.
S′
p
S′′
p
S′′
o
S′
o
S′
r
S′′
r
Sh
Sm
(b) Curves Sh, Sh+1, ..., Sm to be con-
nected by supporting lines of Kδ
G(Di).
Fig. 7:
Labeling used in the construction of H2.
Notice that the logarithmic im-
ages of Sh, Sh+1, ..., S′
o are contained in the second quadrant, the logarithmic images
of S′′
o , So+1, ..., S′
r are contained in the ﬁrst quadrant, and the logarithmic images of
S′′
r , Sr+1, ..., Sm are contained in the fourth quadrant. The qualitative diﬀerence in limit-
ing tangent between the curves Sh, Sh+1, ..., Sm makes it necessary to treat several diﬀerent
cases.
m1 ≤m2 and α > 1 if m1 = m2, and for S′′
p , m2 ≤m1 and α < 1 if m1 = m2. We
choose m1 ̸= m2 for these curves if this is a possible choice.
Just as in the construction of H1, we need to prove a claim for each adjacent pair
S−(t), S+(t) (with some pairs including one or both of S′
o,S′′
o and S′
r, S′′
r and S′
p, S′′
p ).
As before, we will make the claim that for any pair of adjacent curves, there exists a
choice of direction vector for a connecting line segment which satisﬁes the hypothesis
of Lemma 3.3 and can serve as the boundary of an invariant region for the diﬀerential
inclusion K(N) in the region between these two curves. The diﬀerence between the
claim below and Claim 3.4 is that we are now dealing with curves whose logarithmic
images are outside of the third quadrant.
Claim 3.5. Let S−(t) and S+(t), with S+ clockwise of S−, be adjacent curves as
constructed above and let b
Nq be the one dimensional ray such that one of S−and S+
is contained in fat ̺(Nq), or Nq = Ni if S−, S+ ⊂Ni. Denote by n(S(t)) a clockwise
normal vector to the curve S at the point S(t). Then there exists a direction v with
clockwise normal nv such that
(a) for any w ∈K(Nq), we have w · nv ≥0
(b) there exists t1 > t0 such that n(S(t)) · v ̸= 0 for t > t1
(c) there exists t2 > t1 such that the line Lt2 = S−(t2) + sv intersects S+ at a point
x = S+(τ2) where τ2 > t0
(d) n(S+(τ)) · v ̸= 0 for τ ≥τ2
Proof of Claim 3.5. As in the proof of Claim 3.4, we have more than one case to
consider.
First, assume that S−= Si ∈{Sh, ..., So−1}. Let v be contained in a line that
separates the cones K(Nq) and Bδ(Nq), chosen such that v · ˆx > 0 if possible, and
otherwise v = ˆy. Then, we have
(a) There exists some vector u arbitrarily close to ˆy in Bδ(Nq)◦with det(u, ˆy) <
0.
Then, our choice of v is such that det(u, v) < 0.
Then, because v is a
direction that separates Bδ(Nq) and K(Nq), we can conclude for w ∈K(Nq)
that det(w, v) ≥0 which implies that w · nv ≥0.
(b) We have that n(Si(t)) →ˆx, n(Si(t))·(ˆy) →0 monotonically, and n(Si(t))·(ˆy) ̸= 0


## Page 16


16
J. D. BRUNNER AND G. CRACIUN
for all ﬁnite t > 1. There is then t1 such that there exists t1 > t0 such that
n(Si(t)) · v ̸= 0 for t > t1.
(c) Both Si and Si+1 approach vertical, and Si is to the left of Si+1. Therefore, if
v · ˆx > 0, the desired intersection occurs. If v = ˆy, we have that Si+1 approaches
the line x = 0 and is above the curve Si. Then, the desired intersection must
occur.
(d) If i < o −1 or S′
o is not a line, this is as in (b). If i = o −1 and S′
o is a line, it is
vertical and v ̸= ˆy, because ˆy ∈Bδ(No)◦.
The above holds as well if S−= S′
o, again because ˆy ∈Bδ(No)◦.
The above holds also for S−∈{S′′
o , ..., Sp−2} unless we have that the only sep-
arating line between K(Nq) and Bδ(Nq) is vertical. Then we take v = −ˆy and (b),
and (d) are the same, while
(a) There exists some vector u arbitrarily close to ˆy in Bδ(Nq)◦with det(u, −ˆy) < 0.
Then, because v is a direction that separates Bδ(Nq) and K(Nq), we can conclude
for w ∈K(Nq) that det(w, v) ≥0 which implies that w · nv ≥0.
(c) Both S−and S+ are curves of the form y = αxm with m > 1 with S−above S+.
Then, with vi = −ˆy, we have the desired intersection.
If S−= Sp−1 and S′
p has m1 < m2, then the preceding argument is valid. If S′
p is
a straight line, then Np is a ray and we have that Bδ(Np) = R2
>0. We can therefore
choose a direction v of a separating line of K(Nq) and Bδ(Nq) such that v · ˆx ≥0
and v · ˆy ≤0. Then, we have (a) and (b) as in the preceding case, and
(c) S′
p is a line of positive slope below the curve Sp−1, and so the choice of v · ˆy ≤0
and v · ˆx ≥0 guarantees this intersection occurs.
(d) S′
p has constant and strictly positive slope, so n(S′
p(t)) · v > 0 for all t > 1.
If S−= S′
p, we again have Bδ(Np) = R2
>0 and so again can choose v such that
v · ˆx ≥0 and v · ˆy ≤0. If S′
p and S′′
p are lines (note that they are either both lines
or neither are lines) then, (a)-(d) are satisﬁed because S′
p and S′′
p have positive slope
while Lt = S′
p(t) + sv has negative slope. Otherwise, (a) and (b) are the same as the
preceding argument, while (d) is the same reﬂected across the line y = x (and taking
−v). Finally,
(c) If v · ˆx ≥0 and v · ˆy < 0, then the line Lt = S′
p(t) + sv intersects the (aﬃne) half
line {x > 1, y = 1}, which is below S′′
p , making it clear that we have the desired
intersection. If v = ˆx, we notice that for any point on S′
p, there is some point on
S′′
p directly to the right, because S′′
p is of the form y = αxm for m > 0.
For S−∈{S′′
p , ..., Sm−1}, we can reﬂect the previous arguments across the line
y = x. Reﬂection gives a counterclockwise construction of each Lt with directions
that satisfy vi · ˆy > 0 or v = ˆx. A continuing clockwise construction would instead
choose −v. This concludes the proof of Claim 3.5.
Claim 3.5 gives us a way to construct line segments that serve as a boundary of
an invariant region for K(N) within the individual regions between curves S−(t) and
S+(t). Note that two such segments in adjacent regions do not necessarily have a
common point. On the other hand, results (b),(c), and (d) of the claim are three of
the four conditions of Lemma 3.3. Furthermore, to construct H2 we only considered
curves whose logarithmic image is not contained in the third quadrant, and so the last
condition of Lemma 3.3 is also satisﬁed. Therefore, by applying Lemma 3.3 we can
“slide” each segment so that segments in adjacent regions meet at a point. Therefore,
a solution of the diﬀerential inclusion K(N) cannot cross H2 in the outward direction.
We ﬁnally use Lemma 3.3 to connect H1, H2, and the lines {x = x∗}, {y = y∗}.
Together, these curves form the boundary ∂R of a forward invariant region.


## Page 17


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
17
A nested, continuous family of regions.
We have shown that we can build a forward invariant region R. We will now
show that there exists a continuous nested family of such regions which cover R2
>0.
Recall that the corner points used to construct R lie on the curves Si(t) =
(tm1, αtm2), where m1, m2 and α depend on i.
We have seen that there is some
t0 such that for t > t0, the curve Si(t) is contained in fat ̺(Ni).
To create a nested family of regions Rt, we ﬁrst choose the corner x1 of R lying
on S1 and let ˆt be such S1(ˆt) = x1. Likewise, label the corners of R as xi and let
vi = xi+1 −xi as before. Next, we let R = Rˆt and for t > ˆt, Rt is the region with
S1(t) ∈∂Rt with sides which are segments
Li
t = {Si(τ t
i ) + svi|s ∈[0, st
i]}
and corners lying on each Si(t). In addition, as we take t →∞, we take x∗→0
and y∗→0. Lemma 3.3 implies that all the corners of ∂Rt moves outwards along
the curves Si(t) as t increases. Therefore, we obtain a nested family of regions (with
disjoint boundaries) that covers R2
>0. All of these regions satisfy the condition that
w · ni(x) ≥0 for w ∈K(Ni), where ni(x) is the clockwise normal to the curve
at x ∈∂Rt. Therefore, they are all forward invariant under the N-cone diﬀerential
inclusion K(N). They are then also forward invariant under any diﬀerential inclusion
which is embedded in K(N).
4. Polynomial dynamical systems with variable coeﬃcients.
4.1. Deﬁnitions. A variable κ polynomial dynamical system (vκ-polynomial dy-
namical system) is a dynamical system on Rd
>0 which can be written
(13)
˙x = f(x, t) =
n
X
i=1
κi(t)xsivi
with x ∈Rd
>0, si, vi ∈Rd and xs = Qd
l=1 xsl
l such that there is some ε > 0 such that
ε ≤κi(t) ≤1
ε for all i and all t > 0. In particular, polynomial dynamical systems
with constant coeﬃcients are a special case of vκ-polynomial dynamical systems . ∥
In order to investigate the geometric properties of a vκ-polynomial dynamical
system, we can use a Euclidean embedded graph, as introduced in [7].
Definition 4.1. A Euclidean embedded graph G = (V, E) is a ﬁnite directed
graph whose nodes V are labeled with distinct elements of a ﬁnite set Y ⊂Rd.
We deﬁne, for each edge e ∈E, the source vector s(e) ∈Y to be the label of the source
node of e, the target vector t(e) ∈Y to be the label of the target node of e, and the
reaction vector v(e) = t(e) −s(e), to be the vector in Rd from the label of the source
to the label of the target. These deﬁnitions are inspired by the language of reaction
network theory, with the source vector corresponding to the “source complex” and the
target vector corresponding the “product complex” [12][10][15][16]. Given a Euclidean
embedded graph with edge set E, we can generate the vκ-polynomial dynamical system
˙x = f(x, t) =
X
e∈E
κe(t)xs(e)v(e)
∥Note that any polynomial dynamical system with constant coeﬃcients can be written
˙x =
Pn
i=1 xsivi.


## Page 18


18
J. D. BRUNNER AND G. CRACIUN
by making an arbitrary choice of {κe(t)} that satisﬁes ε ≤κe(t) ≤1
ε for all t. If a vκ-
polynomial dynamical system can be constructed in such a way for some Euclidean
embedded graph G, we then say that ˙x = f(x) is generated by G.
Notice that,
depending on choice of κe(t), two diﬀerent Euclidean embedded graphs G and G′
may generate the same vκ-polynomial dynamical system ˙x = f(x).
Remark 4.2. While our analysis depends on node labels in the Euclidean embed-
ded graph, we can sometimes obtain conclusions about the dynamics of a generated
system using only information about the unlabeled graph, such as reversibility and
weak reversibility [16][1].
It will be useful to group terms in the sum (13) with the same exponent vectors
s(e) = si. We can rewrite (13) as
(14)
˙x = f(x, t) =
n
X
i=1
xsi


mi
X
j=1
κij(t)vij


by renumbering source and reaction vectors. Note that the value of n in (14) may be
smaller than the value of n in (13).
Often of great interest in applications to biological and chemical modeling is
whether a polynomial dynamical system satisﬁes a condition called permanence or the
weaker condition called persistence. This paper is mainly concerned with permanence
on Rd
>0, the positive orthant.
Definition 4.3. A d-dimensional dynamical system on Rd
>0 is called permanent
if Rd
>0 is forward invariant and there exists δ > 0 such that for any solution x(t) with
positive initial condition x0 ∈Rd
>0 we have
δ < lim inf
t→∞xi(t)
&
lim sup
t→∞xi(t) < 1
δ
for all i ∈{1, ..., d}.[10]
Clearly, this condition implies persistence as introduced in Deﬁnition 2.7.
There is of course physical relevance to these conditions in chemical network
models, and more generally in models of population dynamics. The question of per-
manence or persistence in a chemical setting is informally the question of whether or
not some species in the network can be depleted.
We can also deﬁne a condition on vκ-polynomial dynamical systems and euclidean
embedded graphs similar to the tropically endotactic condition on diﬀerential inclu-
sions.
Definition 4.4. Let ˙x = f(x, t) be a two dimensional vκ-polynomial dynamical
system. We say that ˙x = f(x, t) is tropically endotactic if it is strictly embedded into
a tropically endotactic diﬀerential inclusion on R2
>0.
Definition 4.5. Let G be a Euclidean embedded graph in R2. We say that G
is tropically endotactic if any vκ-polynomial dynamical system generated by G is
tropically endotactic.
4.2. Permanence of tropically endotactic systems. It is clear from The-
orem 3.1 that a two dimensional tropically endotactic system is persistent. We will
prove also the stronger result that such systems are permanent. We show this by con-
structing a Lyapunov function outside of a compact attracting set, using the borders
of the regions constructed in the proof of Theorem 3.1 as level sets.


## Page 19


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
19
Theorem 4.6. Any two dimensional tropically endotactic vκ-polynomial dynam-
ical system is permanent.
Proof. If ˙x = f(x, s) is tropically endotactic, then there exists a complete fan N
and tropically endotactic N-cone diﬀerential inclusion K(N) into which ˙x = f(x, s)
is strictly embedded. For this diﬀerential inclusion, we construct a family of nested,
forward invariant regions Rt with disjoint boundaries such that they cover R2
>0, as in
the last step of the proof of Theorem 3.1. We do so by constructing one such region Rˆt
and showing that there exists a nested continuous family of regions which contain Rˆt.
We may also assume that fat̺(1) ⊂R◦
ˆt . We will show that this family of invariant
regions can be used to deﬁne a Lyapunov function for the system ˙x = f(x, s). Deﬁne
(15)
Λ(x) = inf{t ≥ˆt|x ∈Rt}
Note that each region Rt is polygonal, and Λ is smooth everywhere except at the
corner points of these polygons. Recall from the proof of Theorem 3.1 that these
corner points lie on curves denoted Si(t). Also, if Λ(x(0)) = t∗and x(s) ∈Rt∗\ Rˆt,
then ∥˙x(s)∥> ζ for some ζ > 0. This is because fat̺(1) ∩(Rt∗\ Rˆt) = ∅, which
implies that ˙x belongs to the interior of a cone which is not the whole of R2, so ˙x ̸= 0
on the (compact) closure of Rt∗\ Rˆt.
Choose some ˜t ∈(ˆt, t∗) and ǫ ∈(0, ˜t −ˆt). We will show that if x(s) is a solution
of ˙x = f(x, s) with Λ(x(0)) = t∗, then x(s) enters the forward invariant region
R˜t. We do this by showing that Λ is a strict Lyapunov function when restricted to
R2
>0 \ Rˆt+ǫ =: (Rˆt+ǫ)c. For this, we prove that if x(s) ∈Rt∗\ Rˆt+ǫ, then
(16)
lim sup
s→s0
Λ(x(s)) −Λ(x(s0))
s −s0
< −η
for some η > 0. We do so by showing that ∇Λ · ˙x < −η when x(s0) is a smooth point
of Λ and that
(17)
lim sup
s→s0
Λ(x(s)) −Λ(x(s0))
s −s0
< −η
when x(s0) in a neighborhood of some Si(t). Together, these imply that (16) holds.
First consider any compact region contained in Rt∗\ Rˆt+ǫ which does not inter-
sect any Si(t). Note, Λ is smooth in such regions and ∇Λ is precisely the outward
normal to ∂Rt.
The choice of edges of ∂Rt as supporting lines of K(Ni), along
with the strict embedding of ˙x = f(x, s) into K(N), guarantees that ∇Λ · ˙x < 0.
Compactness of the region then ensures that ∇Λ · ˙x < −η in this region for some
η > 0.
To deal with the curves {Si(t)|1 < t < ∞} along which Λ is not diﬀerentiable, we
must draw upon techniques of convex analysis, as detailed in [21].
For each curve Si, let Λi1 and Λi2 be the smooth functions with constant gradient
direction (and therefore with straight-line level sets) such that Λ = Λi1 on one side
of {Si(t)|1 < t < ∞} and Λ = Λi2 on the other and these functions extend onto a
neighborhood of Si.
In order to use some convex analysis results about lower C1 functions, we will
separate the proof into two cases. First, if the interior angle of each Rt along the curve
Si is less than or equal to π, then Λ(x) = max{Λi1(x), Λi2(x)} in some neighborhood
of the curve Si, and so Λ is lower C1 [21]. Second, if the interior angle of each Rt
along the curve Si is greater than π, then −Λ(x) = max{−Λi1(x), −Λi2(x)} and so
−Λ(x) is lower C1.


## Page 20


20
J. D. BRUNNER AND G. CRACIUN
In the ﬁrst case, consider a compact neighborhood Si of {Si(t)|1 ≤t ≤∞} ∩
(Rt∗\ Rˆt) contained in some fat̺(Nj) in which each Rt is convex, and so Λ is lower
C1. Recall that, for t large enough, Si(t) ⊂fat̺(Nj) for some j. Then the (general)
subgradient [21] of Λ at x along the curve Si(t) is the set
(18)
∂Λ(x) = {a∇Λi1(x) + (1 −a)∇Λi2(x)|a ∈[0, 1]}
The function Λ is strictly continuous in R2
>0, so we can apply the chain rule for
subgradients (Theorem 10.6 in [21]) to obtain that
(19)
∂(Λ ◦x)(s) ⊆{w · ˙x(s)|w ∈∂Λ(x(s))}
From the construction of the regions Rt and the fact that ˙x must be contained in the
strict interior of the cone K(Nj) of the diﬀerential inclusion, we have ˙x · ∇Λi1 < 0
and ˙x · ∇Λi2 < 0 on Si. This is because the edges of Rt and so the level sets of Λi1,
Λi2 were chosen to be supporting lines to K(Nj). Since Si is compact, it follows that
there is some η > 0 such that ˙x · ∇Λi1 < −η and ˙x · ∇Λi2 < −η in Si. Therefore,
according to (18) there is a η > 0 such that w · ˙x(s) < −η < 0 for all w ∈∂Λ(x(s))
in Si.
Because Λ is lower C1, from a generalized mean value theorem (Theorem 10.48 in
[21]) applied to the function (Λ ◦x)(s) it follows that for all s in some neighborhood
of s0 there is some τs ∈[s0, s] such that
(20)
Λ(x(s)) −Λ(x(s0)) = σs(s −s0) for some scalar σs ∈∂(Λ ◦x)(τs)
But, we have seen that σs < −η. Therefore, in Si, we have that
lim sup
s→s0
Λ(x(s)) −Λ(x(s0))
s −s0
< −η
In the second case, we have that the interior angle of each Rt along the curve Si is
greater than π. Again, we take this neighborhood to be contained in fat̺(Nj). Then,
completely analogously with the ﬁrst case, we can consider the lower C1 function
−Λ(x) and we obtain that −Λ is strictly increasing along trajectories x(s).
This
implies that Λ is strictly decreasing along trajectories x(s), and moreover we have
lim sup
s→s0
Λ(x(s)) −Λ(x(s0))
s −s0
< −η
for some η > 0.
Finally, note that the three types of regions we have considered (in which Λ is
smooth, Λ is lower C1, or −Λ is lower C1) cover the entirety of Rt∗\ Rˆt+ǫ. Therefore,
we obtain that (16) holds on Rt∗\ Rˆt+ǫ, and so Λ decreases along trajectories x(s)
at a rate that is bounded away from 0. Therefore, solutions to ˙x = f(x, s) must enter
the forward invariant region R˜t.
5. Example systems.
5.1. A modiﬁed Lotka-Volterra system. It has been shown that two dimen-
sional weakly reversible, or even endotactic systems are permanent [10]. Theorem 4.6
can be used to conclude permanence for systems which are neither weakly reversible
nor endotactic.


## Page 21


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
21
Consider the following modiﬁed version of the classical Lotka-Volterra predator-
prey model,
(21)
˙x = κ1(t)x

1
ǫ1

+ κ2(t)xy

−1
1

+ κ3(t)y

ǫ2
−1


for x = (x, y)T ∈R2
>0, such that ǫ1, ǫ2 ∈(0, 1) and there exists ε > 0 with ε < κi(t) <
1
ε. Note that if ǫ1 = ǫ2 = 0, the system (21) becomes a variable κ version of the
classical Lotka-Volterra model, and is not persistent, and therefore not permanent
[10].
We will show that the system (21) is permanent by embedding it into a tropically
endotactic diﬀerential inclusion. This means we must ﬁnd an exponential fan D =
{Di} and cones K(Di) (and parameter ̺) such that x ∈fat̺(Di) ⇒˙x ∈K(Di)◦,
and so that K(Di) does not intersect the δ-escape directions Bδ(Di) for some δ (see
Deﬁnition 2.9). We will construct D and the cones K(Di) by considering the relative
magnitude of the three monomials x, xy, and y.
We construct a complete fan bD such that the ordering of these monomials is
constant on the (relative) interiors of the regions Di of the exponential fan D =
exp( bD). To do this, we use the three curves x = xy, xy = y, and x = y, which
give rise to the one dimensional members of D. The regions fat ̺(Di) are shown in
Figure 9(b) and (c) in blue and white. We can calculate the cones Bδ(Di) by writing
̺-escape curves as
(22)
C(t) = exp (rt + g(t)p) = exp(r1t + g(t)p1)ˆx + exp(r2t + g(t)p2)ˆy
where g(t) = 1 −αe−βt, β ≥0, and α ∈R.
For example, consider the three cones such that (1, 1) ∈bDi ∗∗. Take r = (1, 1)
and p = (−p, p), so a ̺-escape curve can be written
(23)
C(t) = et+g(t)(−p)ˆx + et+g(t)pˆy
and so
(24)
[C′(t)]n =
h
(1 −g′(t)p)et−g(t)pˆx + (1 + g′(t)p)et+g(t)p ˆy
i
n
We then multiply by the scalar e−t to see that
(25)
[C′(t)]n =
h
(1 −g′(t)p)e−g(t)pˆx + (1 + g′(t)p)eg(t)pˆy
i
n
and so
(26)
lim
t→∞[C′(t)]n =

e−pˆx + epˆy

n
In the region fat̺(D0) in Figure 9 (c) (shown in blue), it is true that for any choice
of p, there is small enough ̺ so that C(t) as above is a ̺-escape curve (see Figure 8),
and so Bδ(D0) approaches Cone(ˆx, ˆy).
Considering D−1, as ̺ approaches 0, we
must have p approaching +∞(and so [C′(t)]n approaching ˆy) in order to ensure that
C(t) ⊂fat ̺(D−1) for large t. Checking other possibilities of r ∈bD−1 reveals that
Bδ(D−1) is as shown in Figure 9 (c).
∗∗fat̺(D0) shown in blue, fat̺(D−1) and fat̺(D1) shown in white in the upper right of Figure 9
(c)


## Page 22


22
J. D. BRUNNER AND G. CRACIUN
bD0
r
p
log(C(t))
Fig. 8: The cone bD0, the region fat ̺( bD0) (blue) and log(C(t)) for a ̺-escape curve C. Notice
that {rt + p|t > t0} ⊂fat̺( bD0) if ∥p∥< | log(̺)|, while {rt + p|t > t0} ⊂fat ̺( bD−1) if
∥p∥> | log(̺)|.
In choosing the cones K(Di), the key observation is that for small ̺, the largest
monomial is much larger than the others when (x, y)T ∈fat̺(Di), and so this term
“dominates” the sum (21). For example, when x ≫xy ≫y, then
[ ˙x]n ≈



1
ǫ1




n
and so in this region†† we take K(Di) to be a cone of directions close to the direction
(1, ǫ1)T . Furthermore, because xy is the second largest monomial, we can take K(Di)
to be only vectors to the counterclockwise side of (1, ǫ1)T , the same side as (−1, 1).
When two or more dominant monomials are of the same order of magnitude, we
deﬁne K(Di) to be the cone generated by their associated reaction vectors‡‡. We can
conclude that (21) is permanent for any allowable choice of κi(t). This system is not
endotactic, and in particular not weakly reversible.
Note that the diﬀerential inclusion constructed in this way is not tropically en-
dotactic for ǫ2 ≥1, and indeed the system (21) is not permanent in that case. The
diﬀerential inclusion remains tropically endotactic for ǫ1 ≥1, and so the system (21)
is permanent if ǫ1 ≥1.
5.2. An application to a chemical reaction system. Consider the reaction
network
(27)
Z + Y
κ1 / 2X + 2Y
W + X
κ2
/ X + Y
κ3
/ V
If we assume that the rates of these reactions are given by a combination of mass
action and Michaelis-Menten kinetics [11], and in addition we know that there is
some ε > 0 such that ε ≤W, Z ≤1
ε, then we obtain the following dynamical system
for the concentrations of X and Y :
††The white region on the bottom right side of Figure 9 (b).
‡‡As in the blue region in the right side of Figure 9 (b), where x, xy are the dominant monomials,
and their orders of magnitude are the same.


## Page 23


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
23
(a)
Euclidean
embedded
graph which generates
the system (21)
(b) D-cone diﬀerential in-
clusion
K(D),
shown
in orange.
D0
D−1
D1
(c) Cones Bδ(Di) for the
fan D, shown in red.
Fig. 9:
Analysis of the system (21).
Inspection of (b) and (c) shows that the D-cone
diﬀerential inclusion, shown in (b), is tropically endotactic, because for small enough δ,
none of the cones K(Di) of the diﬀerential inclusion shown in orange in (b) intersect the
interior of the corresponding cone Bδ(Di) shown in red in (c).
(28)
d
dt

x
y

= κ1(t)y

2
1

+ κ2(t)
1 + xy x

0
1

+ κ3(t)xy

−1
−1


The system (28) is not a polynomial dynamical system due to the rational second
term. However, multiplication by a positive scalar ﬁeld does not change the perma-
nence or persistence properties of a system. Therefore, we can replace (28) with the
polynomial dynamical system (29), obtained by multiplying the right-hand side of
(28) by the scalar ﬁeld (1 + xy).
(29)
d
dt

x
y

= κ1(t)y

2
1

+ κ1(t)xy2

2
1

+ κ2(t)x

0
1


+ κ3(t)xy

−1
−1

+ κ3(t)x2y2

−1
−1


It is not immediately apparent that this system should be permanent, or even that
it should have bounded trajectories. Let G be the Euclidean embedded graph shown
in Figure 10 (a). Then G generates the system (29). Again, we choose a fan based on
a comparison of the relative magnitudes of the monomials. For this example, we only
consider the which monomial is largest, rather than an ordering of the monomials as
in the previous example. We construct the exponential fan P by choosing regions on
which the largest monomial does not change. Notice that bP = log(P) is then the
normal fan [23] for the convex hull of the source labels of G (si in ﬁgure Figure 10
(a)) making this fan simple to construct. We use cones K(Pi) of directions which
are close to the direction of the reaction vector associated with the largest monomial.
The P-cone diﬀerential inclusion constructed in this way is tropically endotactic, and


## Page 24


24
J. D. BRUNNER AND G. CRACIUN
s1
s2
s3
s5
s4
(a) Euclidean embedded graph G.
P1
P2
P3
P4 P5 P6
P7
P8
(b) The fan bP.
Fig. 10:
(a) Euclidean embedded graph that generates the polynomial dynamical system
(29), with the convex hull of the source nodes shown dotted. (b) The normal fan bP for
the dotted polygon in (a). The exponential fan P = exp( bP) gives regions in which the
largest monomial does not change.
so we can conclude that the system (29) is permanent, and so the system (28) is
permanent as well.
Using a complete ordering of monomials, as we did for the system (21) may allow
us to choose smaller cones K(Di), and so has higher chances in general of resulting
in a tropically endotactic diﬀerential inclusion. However, in this case it is suﬃcient
to use the simpler exponential fan P.
To see that the polynomial dynamical system (29) is tropically endotactic, we can
check each cone K(Pi) and Bδ(Pi) for some small δ. A sample of the relevant analysis
is demonstrated in Figure 11.
Bδ(P1)
K(P1)
(a)
Bδ(P2)
K(P2)
(b)
Bδ(P7)
K(P7)
(c)
Fig. 11: Permanence of (29) can be concluded by determining the intersection of the cones
K(Pi) and Bδ(Pi)◦. For every pair, this intersection must be empty. We show here a
sample of the analysis. The remaining cones can be checked in the same way.
5.3. Weakly reversible polynomial dynamical systems. We can use The-
orem 4.6 to show that any weakly reversible system in two dimensions is permanent.
A weakly reversible system is a vκ-polynomial dynamical system generated by a Eu-
clidean embedded graph G such that every edge of G is contained in a (directed)
cycle. We can show that a weakly reversible system is tropically endotactic using T ,
the fan of the toric diﬀerential inclusion used in [7], Theorem 3.1. That theorem is
Theorem 5.1 (Theorem 3.1 of [7] and Theorem 4.1 of [8]). Any weakly reversible
vκ-polynomial dynamical system can be embedded into a toric diﬀerential inclusion.
Note that in [7], weakly reversible vκ-polynomial dynamical systems are called “k-
variable toric dynamical systems” (see page 7 of [7]). A toric diﬀerential inclusion with


## Page 25


ROBUST PERSISTENCE AND PERMANENCE OF POLYNOMIAL SYSTEMS
25
exponential fan T assigns to each region fat̺(Ti) the negative dual, or polar cone, −bT ∗
i
of the cone bTi of the polyhedral fan bT . Following the proof of Theorem 5.1 in [7], it
can be shown that when the vκ-polynomial dynamical system is two dimensional and
has no linear conserved quantities, the embedding implied above is strict.
Lemma 5.2. Any toric diﬀerential inclusion in R2
>0 is tropically endotactic.
Proof. Let F be a toric diﬀerential inclusion. F is a T -cone diﬀerential inclusion
with the property that if N ∈T is a face of M ∈T , then K(M) ⊆K(N). We need
only show that for every N ∈T besides 1,
K(N) ∩Bδ(N)◦= ∅
The construction of Bδ(N) implies that Bδ(N) ⊆b
N ∗or b
N ∗⊆Bδ(N) (see Figure 2),
where b
N ∗is the dual cone, while K(N) = −b
N ∗.
If Bδ(N) ⊆b
N ∗, then Bδ(N)◦
clearly does not intersect −b
N ∗. If b
N ∗⊆Bδ(N) ⊂H where H is a half-plane, then
the line ∂H is a supporting line of both −b
N ∗(because it is a supporting line of b
N ∗)
and Bδ(N). The line ∂H must also separate Bδ(N) and −b
N ∗, because it does not
separate Bδ(N) and b
N ∗.
We then obtain the following:
Corollary 5.3. Any weakly reversible vκ-polynomial dynamical system in R2
>0
with no linear conserved quantities is tropically endotactic.
This result can be used to prove the global attractor conjecture in three dimensions,
as in [10].
6. Future Work. We will in upcoming work introduce an algorithmic construc-
tion of an N-cone diﬀerential inclusion, which we call the dominance diﬀerential
inclusion, into which a given polynomial dynamical system is embedded.
In fact,
given a Euclidean embedded graph G and an exponential fan N, we can construct
the dominance diﬀerential inclusion DG(N) such that for any polynomial dynamical
system generated by G, there is some ̺ such that the system is strictly embedded
in DG(N).
The dominance diﬀerential inclusion was used to show permanence of
examples (21) and (29). We conjecture that this construction is minimal, in the sense
that if a polynomial dynamical system can be strictly embedded into some tropically
endotactic diﬀerential inclusion, then DG itself must be tropically endotactic.
We have shown in this paper that if a vκ-polynomial dynamical system is trop-
ically endotactic, it is permanent. On the other hand, we have found examples of
vκ-polynomial dynamical systems that are permanent and fail to be tropically endo-
tactic, so the property of being tropically endotactic is not necessary and suﬃcient
for permanence. However, in future work we will show that this property is closely
related to a necessary condition for permanence.
The deﬁnition of tropically endotactic diﬀerential inclusions can be extended to
higher dimensions, and in future work we will show that it gives rise to a necessary
condition for permanence in any dimension.
7. Acknowledgments. The authors have received partial support from NSF-
DMS-1412643.
REFERENCES


## Page 26


26
J. D. BRUNNER AND G. CRACIUN
[1] D. F. Anderson, A proof of the global attractor conjecture in the single linkage class case,
SIAM Journal on Applied Mathematics, 71 (2011).
[2] D. F. Anderson and A. Shiu, The dynamics of weakly reversible population processes near
facets, SIAM Journal on Applied Mathematics, 70 (2010), pp. 1840–1858.
[3] D. Angeli, P. de Leenheer, and E. Sontag, Persistence results for chemical reaction net-
works with time-dependent kinetics and no global conservation laws, SIAM Journal on
Applied Mathematics, 71 (2011), pp. 128–146.
[4] J.-P. Aubin and A. Cellina, Diﬀerential Inclusions, vol. 264 of Grundlehren der mathema-
tischen Wissenschaften, Springer-Verlag Berlin Heidelberg, 1984.
[5] M. Banaji and J. Mierczy´nski, Global convergence in systems of diﬀerential equations arising
from chemical reaction networks, Journal of Diﬀerential Equations, 254 (2013), pp. 1359 –
1374, https://doi.org/https://doi.org/10.1016/j.jde.2012.10.018.
[6] A. Berman and R. J. Plemmons, Nonnegative Matrices in the Mathematical Sciences, vol. 9
of Classics in Applied Mathematics, SIAM, 1994.
[7] G. Craciun, Toric diﬀerential inclusions and a proof of the global attractor conjecture, (2016),
https://arxiv.org/abs/1501.02860v2.
[8] G. Craciun, Polynomial dynamical systems and toric diﬀerential inclusions, (2017). Submit-
ted.
[9] G. Craciun, A. Dickenstein, A. Shiu, and B. Sturmfels, Toric dynamical systems, Journal
of Symbolic Computation, 44 (2009), pp. 1551–1565.
[10] G. Craciun, F. Nazarov, and C. Pantea, Persistence and permanence of mass action and
power law dynamical systems, SIAM Journal on Applied Mathematics, (2013).
[11] L. Edelstein-Keshet, Mathematical Models in Biology, vol. 46 of Classics in Applied Mathe-
matics, SIAM, 2005.
[12] M. Feinberg, Lectures on chemical reaction networks, (1979), http://www.crnt.osu.edu/
LecturesOnReactionNetworks.
[13] M. Feinberg and F. Horn, Dynamics of open chemical systems and the algebraic structure
of the underlying reaction network, Chemical Engineering Science, 29 (1973), pp. 775–787.
[14] M. Gopalkrishnan, E. Miller, and A. Shiu, A geometric approach to the global attractor
conjecture, SIAM Journal of Applied Dynamical Systems, 13 (2014), pp. 758–797.
[15] J. Gunawardena, Chemical reaction network theory for in-silico biologists, (2003), http://vcp.
med.harvard.edu/papers/crnt.pdf.
[16] F. Horn and R. Jackson, General mass action kinetics, Archive for Rational Mechanics and
Analysis, 47 (1972).
[17] M. D. Johnston, C. Pantea, and P. Donnell, A computational approach to persistence,
permanence, and endotacticity of biochemical reaction systems, Journal of Mathematical
Biology, 72 (2016), pp. 467–498, https://doi.org/10.1007/s00285-015-0892-1.
[18] D. Maclagan and B. Sturmfels, Introduction to Tropical Geometry:, Graduate Studies
in Mathematics, American Mathematical Society, 2015, https://books.google.com/books?
id=3DLMoQEACAAJ.
[19] J. Murray, Mathematical Biology I: An Introduction, vol. 17 of Interdisciplinary Applied
Mathematics, Springer, third ed., 2002.
[20] C. Pantea, On the persistence and global stability of mass-action systems, SIAM Journal of
Mathematical Analysis, 44 (2012), pp. 1636 – 1673.
[21] R. T. Rockafellar and R. J.-B. Wets, Variational Analysis, 3rd ed., 2002.
[22] G. V. Smirnov, Introduction to the Theory of Diﬀerential Inclusions, vol. 41 of Graduate
Studies in Mathematics, American Mathematical Society, 2002.
[23] G. M. Ziegler, Lectures on Polytopes, vol. 152 of Graduate texts in mathematics, Springer-
Verlag, 1995.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]