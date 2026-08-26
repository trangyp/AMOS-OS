---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.08854v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1707.08854v1_First_integrals_of_a_class_of__n_-dimensional_Lotka-Volterra_differential_system

> Source: 1707.08854v1_First_integrals_of_a_class_of__n_-dimensional_Lotka-Volterra_differential_system.pdf

> Pages: 8

---


## Page 1


arXiv:1707.08854v1  [math.DS]  27 Jul 2017
FIRST INTEGRALS OF A CLASS OF n-DIMENSIONAL
LOTKA-VOLTERRA DIFFERENTIAL SYSTEMS
JAUME LLIBRE, ADRIAN C. MURZA AND ANTONIO E. TERUEL
Abstract. Lotka-Volterra model is one of the most popular in
biochemistry.
It is used to analyze cooperativity, autocatalysis,
synchronization at large scale and especially oscillatory behavior
in biomolecular interactions. These phenomena are in close rela-
tionship with the existence of ﬁrst integrals in this model. In this
paper we determine the independent ﬁrst integrals of a family of
n–dimensional Lotka-Volterra systems. We prove that when n = 3
and n = 4 the system is completely integrable. When n ≥6 is
even, there are three independent ﬁrst integrals, while when n ≥5
is odd there exist only two independent ﬁrst integrals. In each of
these mentioned cases we identify in the parameter space the con-
ditions for the existence of Darboux ﬁrst integrals. We also provide
the explicit expressions of these ﬁrst integrals.
1. Introduction and formulation of the problem
The real nonlinear ordinary diﬀerential systems are widely used to
model processes or reactions in a variety of ﬁelds of science, from biol-
ogy and chemistry to economy, physics and engineering. The qualita-
tive theory of dynamical systems is employed to analyze the behavior
of these dynamical systems. Within this analysis one of the important
features is the existence of ﬁrst integrals of the diﬀerential systems de-
ﬁned in Rn. This is mainly due to the fact that the existence of a
ﬁrst integral allows to reduce the dimension of the system by one. So
in the qualitative theory of the diﬀerential systems are important the
methods allowing to detect the presence of ﬁrst integrals.
In this paper we shall apply the Darboux theory of integrability to
real polynomial Lotka-Volterra diﬀerential systems. This theory pro-
vides a method of constructing ﬁrst integrals of polynomial diﬀeren-
tial systems, based on the number of invariant algebraic hypersurfaces
that they have. Since its publication in 1878, this theory originally
2010 Mathematics Subject Classiﬁcation. Primary: 34C07, 34C05, 34C40.
Key words and phrases. Lotka-Volterra system, Darboux ﬁrst integrals.
1


## Page 2


2
J. LLIBRE, A.C. MURZA AND A.E. TERUEL
developed by Darboux, has been extended and/or reﬁned by many au-
thors ﬁrst for polynomial diﬀerential systems in R2 see for instance
[2, 3, 4, 5, 7, 9, 13, 19], and later on for polynomial diﬀerential systems
in Rn see [11, 14, 15, 16, 17, 18, 20, 21].
The Lotka-Volterra diﬀerential systems (see [22, 25]) also called Kol-
mogorov diﬀerential systems (see [12]) are used to model a wide range
of experimental processes [1, 6, 8, 26]. In biochemistry, for example
the pioneering work of Wyman [26] models the autocatalytic chemical
reactions, called by Di Cera et al. [8] a “turning wheel” of one-step
transitions of the macromolecule. Turning wheels have multiple appli-
cations in biochemistry. For instance, enzyme kinetics [26], circadian
clocks [23] and genetic networks [1, 6] are just a few of them.
In [8] it has been proved that when the law of mass conservation ap-
plies, the autocatalytic chemical reactions between xi, i = 1, . . . , n are
governed by the following n-parameter family of nonlinear diﬀerential
equations diﬀerential equations
(1)
˙x1 = x1(k1x2 −knxn) = P1(x1, . . . , xn) = x1K1(x1, . . . , xn),
˙x2 = x2(k2x3 −k1x1) = P2(x1, . . . , xn) = x2K2(x1, . . . , xn),
...
˙xn = xn(knx1 −kn−1xn−1) = xnKn(x1, . . . , xn) = Pn(x1, . . . , xn),
where the parameters satisfy ki ∈R\{0}. This is only one of the mul-
tiple examples of n-dimensional Lotka-Volterra diﬀerential systems.
In the rest of the paper we will study the ﬁrst integrals of the diﬀer-
ential system (1) using the Darboux theory of integrability.
Let
(2)
X = P1
∂
∂x1
+ P2
∂
∂x2
+ . . . + Pn
∂
∂xn
,
be the vector ﬁeld associated to system (1). Let U be an open and
dense subset of Rn. A ﬁrst integral of system (1) is a non-constant
function H : U →R such that it is constant on the solutions of system
(1), i.e. XH = 0 in the points of U. Two ﬁrst integrals Hi : U →R
for i = 1, 2 of system (1) are independent if their gradients ∇H1 and
∇H2 are independent in all the points of U except perhaps in a zero
Lebesgue measure set of U. System (1) is completely integrable if there
exist n −1 independent ﬁrst integrals.
Our main result is the following one.


## Page 3


FIRST INTEGRALS FOR n-DIMENSIONAL LOTKA-VOLTERRA SYSTEMS
3
Theorem 1. For the Lotka-Volterra diﬀerential system (1) with ki ̸= 0
for i = 1, 2, . . . , n the following statements hold.
(a) H =
n
X
i=1
xi is a ﬁrst integral. So in particular for n = 2 the
system is completely integrable.
(b) For n ≥3 odd
H1 =
n
X
i=1
xi,
H2 = x1
n
Y
i=2
xµi
i ,
where
µj = k1k3 . . . kj−2
k2k4 . . . kj−1
if j ≥3 odd, µj = kj+1kj+3 . . . kn
kjkj+2 . . . kn−1
if j ≥2 even,
are two independent ﬁrst integrals.
(c) For n = 3 the system is completely integrable with the two in-
dependent ﬁrst integrals
H1 = x1 + x2 + x3,
H2 = x1x
k3
k2
2 x
k1
k2
3 .
(d) If n ≥4 is even and k1k3 · · · kn−1 = k2k4 · · · kn, then
H1 =
n
X
i=1
xi,
H2 = x1xµ3
3 . . . xµn−1
n−1 ,
H3 = x2xµ4
4 . . . xµn
n ,
where
µj = kj+1kj+3 . . . kn
kjkj+2 . . . kn−1
if j ≥3 odd,
µj = k2k4 . . . kj−2
k3k5 . . . kj−1
if j ≥4 even,
are three independent ﬁrst integrals.
(e) For n = 4 the system is completely integrable if k1k3 = k2k4,
with the three independent ﬁrst integrals
H1 = x1 + x2 + x3 + x4,
H2 = x1x
k4
k3
3 ,
H3 = x2x
k2
k3
4 .
Theorem 1 is proved in the next section.
Let U be an open and dense subset of Rn. The function M : U →R
is a Jacobi multiplier for the Lotka-Volterra diﬀerential system (1) if
n
X
i=1
∂(MPi)
∂xi
= 0.


## Page 4


4
J. LLIBRE, A.C. MURZA AND A.E. TERUEL
The so-called Jacobi Theorem, see Theorem 2.7 of [10], applied to our
system (1) says that if system (1) admits a Jacobi multiplier M and
n −2 independent ﬁrst integrals, then the system admits an extra ﬁrst
integral. An easy computation shows that the function
M(x1, . . . , xn) =
1
Qn
i=1 xi
is a Jacobi multiplier of system (1).
However we cannot use it to
improve the number of independent ﬁrst integrals, because when the
dimension is n = 3 and n = 4 the system is completely integrable,
while for n ≥5 we do not know n −2 independent ﬁrst integrals [24].
2. Proof of Theorem 1
Let f ∈R[x1, x2, . . . , xn] be a polynomial. The algebraic hypersur-
face f = 0 of Rn is an invariant algebraic hypersurface of the system (1)
if there exists a polynomial K ∈R[x1, x2, . . . , xn] such that Xf = Kf.
The polynomial K is called the cofactor of f. We note that an invariant
hypersurface f = 0 has the property that if an orbit of system (1) has
a point in f = 0, then the whole orbit is contained in f = 0, for more
details see for instance Chapter 8 of [9].
From the deﬁnition of invariant algebraic hypersurface it follows im-
mediately that for i = 1, . . . , n the hyperplanes xi = 0 are invari-
ant hyperplanes of system (1), and their corresponding cofactors are
Ki(x1, x2, . . . , xn).
The following result is due to Darboux, see [7], or Chapter 8 of [9].
Theorem 2. Suppose that the polynomial vector ﬁeld (1) admits n in-
variant algebraic surfaces fi = 0 with cofactors Ki for i = 1, 2, . . . , n. If
there exist λi ∈R not all zero such that
n
X
i=1
λiKi = 0, then the function
f λ1
1 f λ2
2 . . . f λn
n
is a ﬁrst integral of the vector ﬁeld (1).
Proof of statement (a) of Theorem 1. Let H =
n
X
i=1
xi. Then an easy
calculation shows that XH = 0, where X has been deﬁned in (2).
□
Proof of statement (b) of Theorem 1. Assume that n ≥3 is odd. From
statement (a) of Theorem 1 the function H1 is a ﬁrst integral. Now we
calculate the other ﬁrst integral.


## Page 5


FIRST INTEGRALS FOR n-DIMENSIONAL LOTKA-VOLTERRA SYSTEMS
5
For i = 1, 2, . . . , n we know that the hyperplane xi = 0 is invariant
for system (1), and that its cofactor is Ki(x1, x2, . . . , xn) = kixi+1 −
ki−1xi−1. From Theorem 2 if there exist λi not all zero and such that
n
X
i=1
λiKi = 0, then H = xλ1
1 xλ2
2 . . . xλn
n
is a ﬁrst integral of system (1).
Then we have
n
X
i=1
λiKi =
x1(knλn −k1λ2) + x2(k1λ1 −k2λ3)+
x3(k2λ2 −k3λ4) + x4(k3λ3 −k4λ5)+
...
xn−1 (kn−2λn−2 −kn−1λn) + xn(kn−1λn−1 −knλ1)
=
0,
or equivalently
(3)
knλn −k1λ2 = k1λ1 −k2λ3 = k2λ2 −k3λ4 = k3λ3 −k4λ5 =
...
kn−2λn−2 −kn−1λn = kn−1λn−1 −knλ1 = 0.
Then it is easy to check that the solutions λj’s of system (3) are
λj = k1k3 . . . kj−2
k2k4 . . . kj−1
λ1 if j ≥3 odd, λj = kj+1kj+3 . . . kn
kjkj+2 . . . kn−1
λ1 if j ≥2 even.
Since the unique free lambda is λ1, by Theorem 2 we can choose λ1 =
1 for obtaining the ﬁrst integral H2 of system (1) given in statement
(b).
Clearly that the integrals H1 and H2 are independent because the
gradient ∇H1 = (1, 1, . . . , 1) is independent of the gradient ∇H2.
□
Proof of statement (c) of Theorem 1. Statement (c) follows immediately
from statement (b).
□
Proof of statement (d) of Theorem 1. Assume that n ≥4 even. Now
we calculate the two additional ﬁrst integrals to the integral H1.
Taking into account that k1k3 · · · kn−1 = k2k4 · · · kn it is easy to check
that the solutions λj’s of system (3) can be written as
λj = kj+1kj+3 . . . kn
kjkj+2 . . . kn−1
λ1 if j ≥3 odd, λj = k2k4 . . . kj−2
k3k5 . . . kj−1
λ2 if j ≥4 even.


## Page 6


6
J. LLIBRE, A.C. MURZA AND A.E. TERUEL
Since the unique free lambdas are λ1 and λ2, we can choose the
following two choices: (λ1, λ2) = (1, 0) and (λ1, λ2) = (0, 1), and by
applying Theorem 2 we obtain the two independent ﬁrst integrals H2
and H3 given in the statement (d).
Clearly that these third integrals are independent since H2 has only
even coordinates, H3 only odd coordinates, and the combination of the
gradient vectors of H2 and H3 cannot provide the gradient of H1.
□
Proof of statement (e) of Theorem 1. Statement (e) follows immediately
from statement (d).
□
Acknowledgements
The ﬁrst author is partially supported by a FEDER-MINECO grant
MTM2016-77278-P, a MINECO grant MTM2013-40998-P, and an AGAUR
grant 2014SGR-568. The second author acknowledges partial support
from a grant of the Romanian National Authority for Scientiﬁc Re-
search and Innovation, CNCS-UEFISCDI, project number PN-II-RU-
TE-2014-4-0657.
References
[1] S. Alizon, M. Kucera and V.A.A. Jansen, Competition Between Cryptic
Species Explains Variations in Rates of Lineage Evolution, Proc. Natl. Acad.
Sci. U.S.A. 105 (2008), 12382–12386.
[2] J. Chavarriga, J. Llibre and J. Sotomayor, Algebraic solutions for poly-
nomial systems with emphasis in the quadratic case, Expositiones Math. 15
(1997), 161–173.
[3] C.J. Christopher, Invariant algebraic curves and conditions for a center,
Proc. Roy. Soc. Edinburgh 124A (1994), 1209–1229.
[4] C.J. Christopher and J. Llibre, Algebraic aspects of integrability for poly-
nomial systems, Qualit. Th. Dyn. Syst. 1 (1999), 71–95.
[5] C.J. Christopher and J. Llibre, Integrability via invariant algebraic curves
for planar polynomial diﬀerential systems, Ann. Diﬀ. Eqs. 16 (2000), 5–19.
[6] F. Coppex, M. Droz and A. Lipowski, Extinction Dynamics of Lotka-
Volterra Ecosystems on Evolving Networks, Phys. Rev. E 69 (2004), 061901.
[7] G. Darboux, M´emoire sur les ´equations diﬀ´erentielles alg´ebriques du premier
ordre et du premier degr´e (M´elanges), Bull. Sci. math. 2`eme s´erie 2 (1878), 60–
96; 123–144; 151–200.
[8] Di Cera, P.E. Phillipson and J. Wyman, Chemical Oscillations in Closed
Macromolecular Systems, Proc. Natl. Acad. Sci. U.S.A. 85 (1988), 5923–5926.
[9] F. Dumortier, J. Llibre and J.C. Art´es, Qualitative theory of planar
diﬀerential systems, UniversiText, Springer–Verlag, New York, 2006.
[10] A. Goriely, Integrability and Nonintegrability of Dynamical Systems, World
Scientiﬁc, 2001.


## Page 7


FIRST INTEGRALS FOR n-DIMENSIONAL LOTKA-VOLTERRA SYSTEMS
7
[11] J.P. Jouanolou, Equations de Pfaﬀalg´ebriques, Lectures Notes in Mathe-
matics 708, Springer-Verlag, New York/Berlin, 1979.
[12] A. Kolmogorov, Sulla teoria di Volterra della lotta per l’esistenza, Giornale
dell’ Istituto Italiano degli Attuari 7 (1936), 74–80.
[13] J. Llibre, Integrability of polynomial diﬀerential systems, Handbook of Diﬀer-
ential Equations, Ordinary Diﬀerential Equations, Eds. A. Ca˜nada, P. Drabek
and A. Fonda, Elsevier, 2004, 437–533 pp.
[14] J. Llibre and Y. Bola˜nos, Rational ﬁrst integrals for polynomial vector
ﬁelds on algebraic hypersurfaces of Rn+1, Int. J. Bifurcation and Chaos 22
(2012), 1250270–11 pp.
[15] J. Llibre and J.C. Medrado, On the invariant hyperplanes for d–
dimensional polynomial vector ﬁelds, J. Phys. A: Math. Gen. 40 (2007), 8385–
8391.
[16] J. Llibre and G. Rodr´ıguez, Invariant Hyperplanes and Darboux Integra-
bility for d-dimensional Polynomial Diﬀerential Systems, Bull. Sci. Math. 124
(2000), 599–619.
[17] J. Llibre and X. Zhang, Darboux Theory of Integrability in Cn taking into
account the multiplicity, J. of Diﬀerential Equations 246 (2009), 541–551.
[18] J. Llibre and X. Zhang, Rational ﬁrst integrals in the Darboux theory of
integrability in Cn, Bull. Sci. Math. 134 (2010), 189–195.
[19] J. Llibre and X. Zhang, On the Darboux integrability of the polynomial
diﬀerential systems, Qualit. Th. Dyn. Syst. 11 (2012), 129–144.
[20] J. Llibre and X. Zhang, Darboux theory of integrability for polynomial
vector ﬁelds in Rn taking into account the multiplicity at inﬁnity, Bull. Sci.
Math. 133 (2009), 765–778.
[21] J. Llibre and X. Zhang, Darboux integrability of real polynomial vector
ﬁelds on regular algebraic hypersurfaces, Rend. Circ. Mat. Palermo 51 (2002),
109–126.
[22] A.J. Lotka, Analytical Note on Certain Rhythmin Relations in Organic Sys-
tems, Proc. Natl. Acad. Sci. U.S. 6 (1920), 410–415.
[23] R.W. McCarley and J.A. Hobson, Neuronal Excitability Modulation over
the Sleep Cycle: a Structural and Mathematical Model, Science 189 (1975),
58–60.
[24] A.C. Murza and A.E. Teruel, Global Dynamics of a Family of 3−D Lotka-
Volterra Systems, Dyn. Syst. 25 (2010), 269–284.
[25] V. Volterra, Le¸cons sur la Th´eorie Math´ematique de la Lutte pour la vie,
Gautiers Villars, Paris, 1931.
[26] J. Wyman, The Turning Wheel: A Study in Steady States, Proc. Nat. Acad.
Sci. USA. 72 (1975), 3983–3987.
Jaume Llibre, Departament de Matem`atiques, Universitat Aut`onoma
de Barcelona, 08193 Bellaterra, Barcelona, Catalonia, Spain
E-mail address: jllibre@mat.uab.cat
Adrian C. Murza, Institute of Mathematics “Simion Stoilow” of the
Romanian Academy, Calea Grivit¸ei 21, 010702 Bucharest, Romania
E-mail address: adrian murza@hotmail.com


## Page 8


8
J. LLIBRE, A.C. MURZA AND A.E. TERUEL
Antonio E. Teruel, Departament de Matem`atiques i Inform`atica,
Universitat de les Illes Balears, Crta. de Valldemossa km. 7.5, 07122
Palma de Mallorca, Spain
E-mail address: antonioe.teruel@uib.es

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]