---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1309.6518
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1309.6518_Higher-order_variational_problems_of_Herglotz_type

> Source: 1309.6518_Higher-order_variational_problems_of_Herglotz_type.pdf

> Pages: 9

---


## Page 1


arXiv:1309.6518v1  [math.OC]  25 Sep 2013
Higher-order variational problems of Herglotz type∗
Sim˜ao P. S. Santos
simsantos@gmail.com
Nat´alia Martins
natalia@ua.pt
Delﬁm F. M. Torres
delfim@ua.pt
CIDMA–Center for Research and Development in Mathematics and Applications
Department of Mathematics, University of Aveiro, 3810-193 Aveiro, Portugal
Abstract
We obtain a generalized Euler–Lagrange diﬀerential equation and transversality optimality
conditions for Herglotz-type higher-order variational problems. Illustrative examples of the
new results are given.
Keywords: Euler–Lagrange diﬀerential equations, natural boundary conditions, generalized
calculus of variations.
Mathematics Subject Classiﬁcation 2010: 34H05, 49K15.
1
Introduction
The generalized variational calculus proposed by Herglotz [7, 8] deals with an initial value problem
˙z(t) = L (t, x(t), ˙x(t), z(t)) ,
t ∈[a, b],
(1)
z(a) = γ,
γ ∈R,
(2)
and consists in determining trajectories x that extremize (minimize or maximize) the value z(b).
Observe that (1) represents a family of diﬀerential equations: for each function x a diﬀerent
diﬀerential equation arises. Therefore, z depends on x, a fact that can be made explicit by writing
z(t, x(t), ˙x(t)) or z[x; t], but for brevity and convenience of notation it is usual to write simply
z(t). The problem reduces to the classical fundamental problem of the calculus of variations (see,
e.g., [1]) if the Lagrangian L does not depend on the variable z: if
˙z(t) = L(t, x(t), ˙x(t)),
t ∈[a, b],
z(a) = γ,
γ ∈R,
then we obtain the classical variational problem
z(b) =
Z b
a
˜L(t, x(t), ˙x(t))dt −→extr,
(3)
where
˜L(t, x, ˙x) = L(t, x, ˙x) +
γ
b −a.
Herglotz proved that a necessary condition for a trajectory x to be an extremizer of the generalized
variational problem z(b) →extr subject to (1)–(2) is given by
∂L
∂x (t, x(t), ˙x(t), z(t)) −d
dt
∂L
∂˙x (t, x(t), ˙x(t), z(t)) + ∂L
∂z (t, x(t), ˙x(t), z(t)) ∂L
∂˙x (t, x(t), ˙x(t), z(t)) = 0,
(4)
∗This is a preprint of a paper whose ﬁnal and deﬁnite form will appear in Vietnam Journal of Mathematics,
ISSN: 2305-221X (Print) 2305-2228 (Online). Paper submitted 13-June-2013; revised 11-Sept-2013; accepted for
publication 24-Sept-2013.
1


## Page 2


t ∈[a, b]. This equation is known as the generalized Euler–Lagrange equation [6, 7, 12]. Observe
that for the classical problem of the calculus of variations (3) one has ∂L
∂z = 0, and the diﬀerential
equation (4) reduces to the classical Euler–Lagrange equation:
∂L
∂x (t, x(t), ˙x(t)) −d
dt
∂L
∂˙x (t, x(t), ˙x(t)) = 0.
The variational problem of Herglotz was the basis of the Ph.D. thesis [2]. The main goal of this
thesis, done under supervision of Ronald B. Guenther, was to generalize the well known Noether’s
theorems (see, e.g., [13]) to problems of Herglotz type [3, 4, 5]. As reported in [3, 4], unlike the
classical variational principle, the variational principle of Herglotz gives a variational description
of nonconservative processes, even when the Lagrangian is autonomous. For the importance to
include nonconservativism in the calculus of variations, we refer the reader to the recent book [9].
In this paper we generalize Herglotz’s problem by considering the following higher-order vari-
ational problem.
Problem (P). Determine the trajectories x ∈C2n([a, b], R) that extremize the value of the func-
tional z[x; b],
z(b) −→extr,
where z satisﬁes the diﬀerential equation
˙z(t) = L

t, x(t), ˙x(t), . . . , x(n)(t), z(t)

,
t ∈[a, b],
(5)
subject to the initial condition
z(a) = γ,
(6)
where γ is a ﬁxed real number. The Lagrangian L is assumed to satisfy the following hypotheses:
(H1) L is a C1(Rn+3, R) function;
(H2) functions t 7→
∂L
∂x(j)

t, x(t), ˙x(t), . . . , x(n)(t), z(t)

and t 7→∂L
∂z

t, x(t), ˙x(t), . . . , x(n)(t), z(t)

,
j = 0, . . . , n, are diﬀerentiable up to order n for any admissible trajectory x.
Clearly, problem (P) generalizes the classical higher-order variational problem: if the La-
grangian L is independent of z, then
˙z(t) = L

t, x(t), ˙x(t), . . . , x(n)(t)

,
t ∈[a, b],
z(a) = γ,
γ ∈R,
which implies that the problem under consideration is
z(b) =
Z b
a
˜L

t, x(t), ˙x(t), . . . , x(n)(t)

dt −→extr,
where
˜L

t, x, ˙x, . . . , x(n)
= L

t, x, ˙x, . . . , x(n)
+
γ
b −a.
The paper is organized as follows. In Section 2 we recall the necessary results from the classical
calculus of variations. Our results are then proved in Section 3: in Section 3.1 we obtain the
generalized Euler–Lagrange equation for problem (P) in the class of functions x ∈C2n([a, b], R)
satisfying given boundary conditions
x(a) = α0, . . . , x(n−1)(a) = αn−1,
x(b) = β0, . . . , x(n−1)(b) = βn−1,
(7)
where α0, . . ., αn−1, and β0, . . . , βn−1 are given real numbers. The transversality conditions (or
natural boundary conditions) for problem (P) are obtained in Section 3.2. We end with Section 4,
presenting some illustrative examples of application of the new results.
The results of the paper are trivially generalized for the case of vector functions x : [a, b] →Rm,
m ∈N, but for simplicity of presentation we restrict ourselves to the scalar case. Along the text,
we use the standard conventions x(0) = d0x
dt0 = x and Pj
k=1 Υ(k) = 0 whenever j = 0.
2


## Page 3


2
Preliminary results
We recall some results of the classical calculus of variations that are useful in the sequel.
Deﬁnition 1. We say that η ∈C2n ([a, b], R) is an admissible variation for problem (P) subject
to boundary conditions (7) if, and only if, η(a) = η(b) = · · · = η(n−1)(a) = η(n−1)(b) = 0.
Lemma 2 (Higher-order fundamental lemma of the calculus of variations – cf. [10]). Let f0, . . .,
fn ∈C([a, b], R). If
Z b
a
 n
X
i=0
fi(t)η(i)(t)
!
dt = 0
for all admissible variations η of problem (P) subject to boundary conditions (7), then
n
X
i=0
(−1)if (i)
i (t) = 0,
t ∈[a, b].
Lemma 3 (Higher-order integration by parts formulas – cf. [11]). Let n ∈N, a, b ∈R, a < b, and
f, g ∈Cn ([a, b], R). The following n equalities hold:
Z b
a
f(t)g(i)(t)dt =
"i−1
X
k=0
(−1)kf (k)(t)g(i−1−k)(t)
#b
a
+ (−1)i
Z b
a
f (i)(t)g(t)dt,
i = 1, . . . , n.
3
Main results
For simplicity of notation, we introduce the operator ⟨·, ·⟩n, n ∈N, deﬁned by
⟨x, z⟩n(t) :=

t, x(t), ˙x(t), . . . , x(n)(t), z(t)

.
3.1
Generalized Euler–Lagrange equation
The following result gives a necessary condition of Euler–Lagrange type for an admissible function
x to be an extremizer of the functional z[x; b], where z is deﬁned by (5), (6) and (7).
Theorem 4 (Generalized higher-order Euler–Lagrange equation). If x is a solution to problem
(P) subject to the boundary conditions (7), then x satisﬁes the generalized Euler–Lagrange equation
n
X
j=0
(−1)j dj
dtj

λ(t) ∂L
∂x(j) ⟨x, z⟩n(t)

= 0,
(8)
t ∈[a, b], where λ(t) := e−R t
a
∂L
∂z ⟨x,z⟩n(θ)dθ.
Proof. Suppose that x is a solution of (P) subject to (7), and let η ∈C2n([a, b], R) be an admissible
variation such that η(n)(a) = 0. Let ǫ be an arbitrary real number. Deﬁne ζ : [a, b] →R by
ζ(t) := d
dǫz[x + ǫη; t]

ǫ=0
= d
dǫz

t, x(t) + ǫη(t), ˙x(t) + ǫ ˙η(t), . . . , x(n)(t) + ǫη(n)(t)
 
ǫ=0
.
Obviously, ζ(a) = 0. Since x is a minimizer (resp., maximizer), we have
z

b, x(b) + ǫη(b), ˙x(b) + ǫ ˙η(b), . . . , x(n)(b) + ǫη(n)(b)

≥(resp. ≤) z

b, x(b), ˙x(b), . . . , x(n)(b)

.
3


## Page 4


Hence, ζ(b) =
d
dǫz[x + ǫη; b]

ǫ=0 = 0. Because
˙ζ(t) = d
dt
d
dǫz

t, x(t) + ǫη(t), ˙x(t) + ǫ ˙η(t), . . . , x(n)(t) + ǫη(n)(t)
 
ǫ=0
= d
dǫ
d
dtz

t, x(t) + ǫη(t), ˙x(t) + ǫ ˙η(t), . . . , x(n)(t) + ǫη(n)(t)
 
ǫ=0
= d
dǫL⟨x + ǫη, z⟩n(t)

ǫ=0
,
we conclude that
˙ζ(t) =
n
X
k=0
 ∂L
∂x(k) ⟨x, z⟩n(t)η(k)(t)

+ ∂L
∂z ⟨x, z⟩n(t) d
dǫz[x + ǫη; t]

ǫ=0
=
n
X
k=0
 ∂L
∂x(k) ⟨x, z⟩n(t)η(k)(t)

+ ∂L
∂z ⟨x, z⟩n(t)ζ(t).
Thus, ζ satisﬁes a ﬁrst order linear diﬀerential equation whose solution is found according to
˙y + Py = Q ⇔e−
R t
a P (θ)dθy(t) −y(a) =
Z t
a
e−
R τ
a P (θ)dθQ(τ)dτ.
Therefore,
e−
R t
a
∂L
∂z ⟨x,z⟩n(θ)dθζ(t) −ζ(a) =
Z t
a
e−
R τ
a
∂L
∂z ⟨x,z⟩n(θ)dθ


n
X
j=0
∂L
∂x(j) ⟨x, z⟩n(τ) η(j)(τ)

dτ.
Denoting λ(t) := e−
R t
a
∂L
∂z ⟨x,z⟩n(θ)dθ, we get
λ(t)ζ(t) −ζ(a) =
Z t
a
λ(τ)


n
X
j=0
∂L
∂x(j) ⟨x, z⟩n(τ)η(j)(τ)

dτ.
In particular, for t = b, we have
λ(b)ζ(b) −ζ(a) =
Z b
a
λ(τ)


n
X
j=0
∂L
∂x(j) ⟨x, z⟩n(τ)η(j)(τ)

dτ.
Since ζ(t) = 0, t ∈{a, b}, the left-hand side of the previous equation vanishes and we get
0 =
Z b
a
n
X
j=0
λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)η(j)(τ)dτ.
Using the higher-order fundamental lemma of the calculus of variations (Lemma 2), we obtain the
generalized Euler–Lagrange equation
n
X
j=0
(−1)j

λ(t) ∂L
∂x(j) ⟨x, z⟩n(t)
(j)
= 0,
t ∈[a, b], proving the intended result.
In order to simplify expressions, and in agreement with Theorem 4, from now on we use the
notation λ(t) := e−
R t
a
∂L
∂z ⟨x,z⟩n(θ)dθ. If n = 1, then the diﬀerential equation of problem (P) reduces
to ˙z(t) = L (t, x(t), ˙x(t), z(t)), which deﬁnes the functional z of Herglotz’s variational principle.
This principle is a particular case of our Theorem 4 and is given in Corollary 5.
4


## Page 5


Corollary 5 (See [7, 8]). Let z be a solution of ˙z(t) = L (t, x(t), ˙x(t), z(t)), t ∈[a, b], subject to the
boundary conditions z(a) = γ, x(a) = α and x(b) = β, where γ, α, and β are given real numbers.
If x is an extremizer of functional z[x; b], then x satisﬁes the diﬀerential equation
∂L
∂x (t, x(t), ˙x(t), z(t)) + ∂L
∂z (t, x(t), ˙x(t), z(t)) ∂L
∂˙x (t, x(t), ˙x(t), z(t)) −d
dt
∂L
∂˙x (t, x(t), ˙x(t), z(t)) = 0,
t ∈[a, b].
Our Euler–Lagrange equation (8) is also a generalization of the classical Euler–Lagrange equa-
tion for higher-order variational problems.
Corollary 6 (See, e.g., [1]). Suppose that x is a solution of problem (P) subject to (7), and that
the Lagrangian L is independent of z. Then x satisﬁes the classical higher-order Euler–Lagrange
diﬀerential equation
n
X
j=0
(−1)j dj
dtj
 ∂L
∂x(j)

t, x(t), . . . , x(n)(t)

= 0,
(9)
t ∈[a, b].
3.2
Generalized natural boundary conditions
We now consider the case when the values of x(a), . . ., x(n−1)(a), x(b), . . ., x(n−1)(b), are not
necessarily speciﬁed.
Theorem 7 (Generalized natural boundary conditions). Suppose that x is a solution to problem
(P). Then x satisﬁes the generalized Euler–Lagrange equation (8). Moreover,
1. If x(k)(b), k ∈{0, . . ., n −1}, is free, then the natural boundary condition
n−k
X
j=1
(−1)j−1 dj−1
dtj−1

λ(t)
∂L
∂x(k+j) ⟨x, z⟩n(t)
 
t=b
= 0
(10)
holds.
2. If x(k)(a), k ∈{0, . . ., n −1}, is free, then the natural boundary condition
n−k
X
j=1
(−1)j−1 dj−1
dtj−1

λ(t)
∂L
∂x(k+j) ⟨x, z⟩n(t)
 
t=a
= 0
(11)
holds.
Proof. Suppose that x is a solution to problem (P). Let η ∈C2n([a, b], R) and deﬁne the function
ζ just like in the proof of Theorem 4. From the arbitrariness of η, and using similar arguments as
the ones in the proof of Theorem 4, we conclude that x satisﬁes the generalized Euler–Lagrange
equation (8). We now prove (10) (the proof of (11) follows exactly the same arguments). Suppose
that x(k)(b), k ∈{0, . . . , n −1}, is free.
Deﬁne the function ζ(t) :=
d
dǫz[x + ǫη; t]

ǫ=0.
Let
J :=

j ∈{0, . . . , n −1} : x(j)(a) is given
	
. For any j ∈{0, . . . , n −1}, if j ∈J, then η(j)(a) = 0;
otherwise, we restrict ourselves to those functions η such that η(j)(a) = 0. For convenience, we also
suppose that η(n)(a) = 0. Using the same arguments as the ones used in the proof of Theorem 4,
we ﬁnd that ζ satisﬁes the ﬁrst order linear diﬀerential equation
˙ζ(t) = ∂L
∂x ⟨x, z⟩n(t)η(t) + ∂L
∂˙x ⟨x, z⟩n(t) ˙η(t) + · · · +
∂L
∂x(n) ⟨x, z⟩n(t)η(n)(t) + ∂L
∂z ⟨x, z⟩n(t)ζ(t),
whose solution is found by
λ(t)ζ(t) −ζ(a) =
Z t
a
n
X
j=0
λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)η(j)(τ)dτ.
5


## Page 6


Again, since ζ(t) = 0, for t ∈{a, b}, we get
Z b
a
n
X
j=0
λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)η(j)(τ)dτ = 0
and, therefore,
Z b
a
λ(τ)∂L
∂x ⟨x, z⟩n(τ)η(τ)dτ +
n
X
j=1
Z b
a
λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)η(j)(τ)dτ = 0.
Using the higher-order integration by parts formula (Lemma 3) in the second parcel we get
Z b
a
λ(τ)∂L
∂x ⟨x, z⟩n(τ)η(τ)dτ
+
n
X
j=1


"
λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)η(j−1)(τ) +
j−1
X
i=1
(−1)i

λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)
(i)
η(j−1−i)(τ)
#b
a
+(−1)j
Z b
a

λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)
(j)
η(τ)dτ
!
= 0,
which is equivalent to
Z b
a
n
X
j=0
(−1)j

λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)
(j)
η(τ)dτ
+
n
X
j=1
"
λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)η(j−1)(τ) +
j−1
X
i=1
(−1)i

λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)
(i)
η(j−1−i)(τ)
#b
a
= 0.
Using the generalized Euler–Lagrange equation (8) into the last equation we get
n
X
j=1
"
λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)η(j−1)(τ) +
j−1
X
i=1
(−1)i

λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)
(i)
η(j−1−i)(τ)
#b
a
= 0
and since η(a) = ˙η(a) = · · · = η(n−1)(a) = 0, we conclude that
n
X
j=1
 
λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)η(j−1)(τ) +
j−1
X
i=1
(−1)i

λ(τ) ∂L
∂x(j) ⟨x, z⟩n(τ)
(i)
η(j−1−i)(τ)
! 
τ=b
= 0.
This equation is equivalent to
n−1
X
i=0


n−i
X
j=1
(−1)j−1

λ(τ)
∂L
∂x(i+j) ⟨x, z⟩n(τ)
(j−1)
η(i)(τ)



τ=b
= 0.
Let I :=

i ∈{0, . . . , n −1} : x(i)(b) is given
	
. Note that k ̸∈I. For any i ∈{0, . . . , n −1}, if
i ∈I, then η(i)(b) = 0; otherwise, for i ̸= k, we restrict ourselves to those functions η such that
η(i)(b) = 0. From the arbitrariness of η(k)(b), it follows that
n−k
X
j=1
(−1)j−1

λ(τ)
∂L
∂x(k+j) ⟨x, z⟩n(τ)
(j−1) 
τ=b
= 0.
This concludes the proof.
6


## Page 7


Remark 8. If x is a solution to problem (P) without any of the 2n boundary conditions (7), then x
satisﬁes the generalized higher-order Euler–Lagrange equation (8) and n transversality conditions
(10) and n transversality conditions (11). In general, for each boundary condition missing in (7),
there is a corresponding natural boundary condition, as given by Theorem 7.
Next we remark that our generalized transversality conditions (10) and (11) are generalizations
of the classical transversality conditions for higher-order variational problems (cf. ψk = 0, k =
0, . . . , n −1, with ψk given as in [13, Section 5]).
Corollary 9. Suppose that x is a solution of problem (P) with L independent of z.
Then x
satisﬁes the classical Euler–Lagrange equation (9). Moreover,
1. If x(k)(b), k ∈{0, . . ., n −1}, is free, then the natural boundary condition
n−k
X
j=1
(−1)j−1 dj−1
dtj−1

∂L
∂x(k+j)
 
b, ˙x(b), . . . , x(n)(b)

= 0
holds.
2. If x(k)(a) is free, k ∈{0, . . . , n −1}, then the natural boundary condition
n−k
X
j=1
(−1)j−1 dj−1
dtj−1

∂L
∂x(k+j)
 
a, ˙x(a), . . . , x(n)(a)

= 0
holds.
4
Illustrative examples
We illustrate the usefulness of our results with some examples that are not covered by previous
available results in the literature. Let us consider the particular case of Theorem 4 with n = 2.
Corollary 10. Let z be a solution of ˙z(t) = L (t, x(t), ˙x(t), ¨x(t), z(t)), t ∈[a, b], subject to the
boundary conditions z(a) = γ, x(a) = α0, ˙x(a) = α1, x(b) = β0, and ˙x(b) = β1, where γ, α0, α1,
β0, and β1, are given real numbers. If x is an extremizer of functional z[x; b], then x satisﬁes the
diﬀerential equation
∂L
∂x ⟨x, z⟩2(t) + ∂L
∂z ⟨x, z⟩2(t)∂L
∂˙x ⟨x, z⟩2(t) −d
dt
∂L
∂˙x ⟨x, z⟩2(t) +
∂L
∂z ⟨x, z⟩2(t)
2 ∂L
∂¨x ⟨x, z⟩2(t)
−2∂L
∂z ⟨x, z⟩2(t) d
dt
∂L
∂¨x ⟨x, z⟩2(t) −
 d
dt
∂L
∂z ⟨x, z⟩2(t)
 ∂L
∂¨x ⟨x, z⟩2(t) + d2
dt2
∂L
∂¨x ⟨x, z⟩2(t) = 0,
(12)
t ∈[a, b], where ⟨x, z⟩2(t) = (t, x(t), ˙x(t), ¨x(t), z(t)).
We now apply Corollary 10 to concrete situations.
Example 11. Let us consider the following Herglotz’s higher-order variational problem:
z(1) −→min,
˙z(t) = ¨x2(t) + z2(t),
t ∈[0, 1],
z(0) = 1
2,
x(0) = 0,
˙x(0) = 1,
x(1) = 1,
˙x(1) = 1.
(13)
For this problem, the necessary optimality condition (12) asserts that
x(4)(t) −4z(t)x(3)(t) +
 4z2(t) −2 ˙z(t)

x(2)(t) = 0.
(14)
7


## Page 8


Solving the system formed by (14) and ˙z(t) = ¨x2(t) + z2(t), subject to the given boundary
conditions, gives the extremal
x(t) = t,
z(t) =
1
2 −t,
for which z(1) = 1.
Example 12. Consider problem (13) with z(0) = z0 free. We show that such problem is not well
deﬁned. Indeed, if a solution exists, we obtain the optimality system
(
x(4)(t) −4z(t)x(3)(t) +
 4z2(t) −2 ˙z(t)

x(2)(t) = 0
˙z(t) = ¨x2(t) + z2(t)
(15)
subject to x(0) = 0 and ˙x(0) = x(1) = ˙x(1) = 1. It follows that
x(t) = t,
z(t) =
z0
1 −z0t,
and we conclude that the problem has no solution: the inﬁmum is −∞obtained when z0 →1+.
Example 13. Consider now the following problem:
z(1) −→min,
˙z(t) = ¨x2(t) + z(t),
t ∈[0, 1],
z(0) = 1,
x(0) = 0,
˙x(0) = 1,
x(1) = 1,
˙x(1) = 0.
(16)
For problem (16), the necessary optimality condition (12) asserts that
x(4)(t) −2x(3)(t) + x(2)(t) = 0.
(17)
Solving the system formed by (17) and ˙z(t) = ¨x2(t)+z(t), subject to the given boundary conditions,
gives the extremal
x(t) = (1 −t)et+1 + (2t −1)et + (e −3)et −e + 1
e2 −3e + 1
,
z(t) =

(1 + t2)et+2 −2(2t2 + t + 2)et+1 + (4t2 + 4t + 5)et + e4 −6 e3 + 10 e2 −2 e −4

et
(e2 −3 e + 1)2
,
for which z(1) = (e2−e−4)e
e2−3e+1 ≳7, 78.
Our last example shows the usefulness of Theorem 7.
Example 14. We now consider problem (16) with ˙x(1) free. In this case, solving
(
x(4)(t) −2x(3)(t) + x(2)(t) = 0
˙z(t) = ¨x2(t) + z(t)
subject to the boundary conditions z(0) = 1, x(0) = 0, ˙x(0) = 1, x(1) = 1, and the natural
boundary condition (10) for n = 2 and k = 1, that in the present situation simpliﬁes to ¨x(1) = 0,
gives the extremal
x(t) = t,
z(t) = et,
for which ˙x(1) = 1 and z(1) = e ≲2, 72.
8


## Page 9


Acknowledgments
This work was supported by FEDER funds through COMPETE–Operational Programme Fac-
tors of Competitiveness (“Programa Operacional Factores de Competitividade”) and by Por-
tuguese funds through the Center for Research and Development in Mathematics and Applica-
tions (University of Aveiro) and the Portuguese Foundation for Science and Technology (“FCT–
Funda¸c˜ao para a Ciˆencia e a Tecnologia”), within project PEst-C/MAT/UI4106/2011 with COM-
PETE number FCOMP-01-0124-FEDER-022690. Torres was also supported by the FCT project
PTDC/EEI-AUT/1450/2012, co-ﬁnanced by FEDER under POFC-QREN with COMPETE ref-
erence FCOMP-01-0124-FEDER-028894. The authors are grateful to two anonymous referees for
their valuable comments and helpful suggestions.
References
[1] I. M. Gelfand and S. V. Fomin, Calculus of variations, Revised English edition translated
and edited by Richard A. Silverman, Prentice Hall, Englewood Cliﬀs, NJ, 1963.
[2] B. A. Georgieva, Noether-type theorems for the generalized variational principle of Herglotz,
ProQuest LLC, Ann Arbor, MI, 2001.
[3] B. Georgieva and R. Guenther, First Noether-type theorem for the generalized variational
principle of Herglotz, Topol. Methods Nonlinear Anal. 20 (2002), no. 2, 261–273.
[4] B. Georgieva and R. Guenther, Second Noether-type theorem for the generalized variational
principle of Herglotz, Topol. Methods Nonlinear Anal. 26 (2005), no. 2, 307–314.
[5] B. Georgieva, R. Guenther and T. Bodurov, Generalized variational principle of Herglotz for
several independent variables. First Noether-type theorem, J. Math. Phys. 44 (2003), no. 9,
3911–3927.
[6] R. B. Guenther, J. A. Gottsch and D. B. Kramer, The Herglotz algorithm for constructing
canonical transformations, SIAM Rev. 38 (1996), no. 2, 287–293.
[7] R. B. Guenther, C. M. Guenther and J. A. Gottsch, The Herglotz Lectures on Contact Trans-
formations and Hamiltonian Systems, Lecture Notes in Nonlinear Analysis, Vol. 1, Juliusz
Schauder Center for Nonlinear Studies, Nicholas Copernicus University, Tor´un, 1996.
[8] G. Herglotz,
Ber¨uhrungstransformationen,
Lectures at the
University of G¨ottingen,
G¨ottingen, 1930.
[9] A. B. Malinowska and D. F. M. Torres, Introduction to the fractional calculus of variations,
Imp. Coll. Press, London, 2012.
[10] N. Martins and D. F. M. Torres, Calculus of variations on time scales with nabla derivatives,
Nonlinear Anal. 71 (2009), no. 12, e763–e773. arXiv:0807.2596
[11] N. Martins and D. F. M. Torres, Necessary optimality conditions for higher-order inﬁnite
horizon variational problems on time scales, J. Optim. Theory Appl. 155 (2012), no. 2, 453–
476. arXiv:1204.3329
[12] J. C. Orum, R. T. Hudspeth, W. Black and R. B. Guenther, Extension of the Herglotz
algorithm to nonautonomous canonical transformations, SIAM Rev. 42 (2000), no. 1, 83–90.
[13] D. F. M. Torres, Proper extensions of Noether’s symmetry theorem for nonsmooth extremals
of the calculus of variations, Commun. Pure Appl. Anal. 3 (2004), no. 3, 491–500.
9

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]