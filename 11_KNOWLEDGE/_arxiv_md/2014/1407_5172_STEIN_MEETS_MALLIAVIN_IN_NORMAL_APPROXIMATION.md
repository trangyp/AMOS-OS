---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1407.5172
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1407.5172_Stein_meets_Malliavin_in_normal_approximation

> Source: 1407.5172_Stein_meets_Malliavin_in_normal_approximation.pdf

> Pages: 31

---


## Page 1


arXiv:1407.5172v2  [math.PR]  8 May 2015
STEIN MEETS MALLIAVIN IN NORMAL
APPROXIMATION
Louis H. Y. Chen
National University of Singapore
2018-01-26
Abstract
Stein’s method is a method of probability approximation which hinges on
the solution of a functional equation. For normal approximation the func-
tional equation is a ﬁrst order diﬀerential equation. Malliavin calculus is an
inﬁnite-dimensional diﬀerential calculus whose operators act on functionals
of general Gaussian processes. Nourdin and Peccati (2009) established a
fundamental connection between Stein’s method for normal approximation
and Malliavin calculus through integration by parts. This connection is ex-
ploited to obtain error bounds in total variation in central limit theorems for
functionals of general Gaussian processes. Of particular interest is the fourth
moment theorem which provides error bounds of the order
p
E(F 4n) −3 in
the central limit theorem for elements {Fn}n≥1 of Wiener chaos of any ﬁxed
order such that E(F 2
n) = 1. This paper is an exposition of the work of Nour-
din and Peccati with a brief introduction to Stein’s method and Malliavin
calculus. It is based on a lecture delivered at the Annual Meeting of the
Vietnam Institute for Advanced Study in Mathematics in July 2014.
1
INTRODUCTION
Stein’s method was invented by Charles Stein in the 1960’s when he used
his own approach in class to prove a combinatorial central limit theorem
of Wald and Wolfowitz [40] and of Hoeﬀding [22]. Malliavin calculus was
developed by Paul Malliavin [25] in 1976 to provide a probabilistic proof
of the Hörmander criterion (Hörmander [23]) of hypoellipticity. Although
the initial goals of Stein’s method and Malliavin calculus are diﬀerent, they
are both built on some integration by parts techniques. This connection
was exploited by Nourdin and Peccati [28] to develop a theory of normal
approximation on inﬁnite-dimensional Gaussian spaces. They were moti-
vated by a remarkable discovery of Nualart and Peccati [34], who proved
1


## Page 2


that a sequence of random variables in a Wiener chaos of a ﬁxed order con-
verges in distribution to a Gaussian random variable if and only of their
second and fourth moments converge to the corresponding moments of the
limiting random variable. By combining Stein’s method and Malliavin cal-
culus, Nourdin and Peccati [28] obtained a general total variation bound in
the normal approximation for functionals of Gaussian processes. They also
proved that for {Fn} in a Wiener chaos of ﬁxed order such that E(F 2
n) = 1,
the error bound is of the order
p
E(F 4n) −3, thus providing an elegant rate
of convergence for the remarkable result of Nualart and Peccati [34]. We
call this result of Nourdin and Peccati [28] the fourth moment theorem.
The work of Nourdin and Peccati [28] has added a new dimension to
Stein’s method. Their approach of combining Stein’s method with Malli-
avin calculus has led to improvements and reﬁnements of many results in
probability theory, such as the Breuer-Major theorem [7]. More recently,
this approach has been successfully used to obtain central limit theorems
in stochastic geometry, stochastic calculus, statistical physics, and for zeros
of random polynomials. It has also been extended to diﬀerent settings as
in non-commutative probability and Poisson chaos. Of particular interest is
the connection between the Nourdin-Peccati analysis and information the-
ory, which was recently revealed in Ledoux, Nourdin and Peccati [24] and
in Nourdin, Peccati and Swan [32].
This paper is an exposition on the connection between Stein’s method
and Malliavin calculus and on how this connection is exploited to obtain a
general error bound in the normal approximation for functionals of Gaussian
processes, leading to the proof of the fourth moment theorem with some
applications.
It is an expanded version of the ﬁrst four sections and of
part of section 5 of Chen and Poly [13], with most parts rewritten and new
subsections added.
2
STEIN’S METHOD
2.1
A general framework
Stein’s method is a method of probability approximation introduced by
Charles Stein [38] in 1972. It does not involve Fourier analysis but hinges
on the solution of a functional equation. Although Stein’s 1972 paper was
on normal approximation, his ideas were general and applicable to other
probability approximations.
In a nutshell, Stein’s method can be described as follows. Let W and Z be
random elements taking values in a space S and let X and Y be some classes
of real-valued functions deﬁned on S.
In approximating the distribution
L (W) of W by the distribution L (Z) of Z, we write Eh(W) −Eh(Z) =
ELfh(W) for a test function h ∈Y, where L is a linear operator (Stein
2


## Page 3


operator) from X into Y and fh ∈X a solution of the equation
Lf = h −Eh(Z)
(Stein equation).
(2.1)
The error ELfh(W) can then be bounded by studying the solution fh and
exploiting the probabilistic properties of W. The operator L characterizes
L (Z) in the sense that L (W) = L (Z) if and only if for a suﬃciently large
class of functions f we have
ELf(W) = 0
(Stein identity).
(2.2)
In normal approximation, where L (Z) is the standard normal distribu-
tion, the operator used by Stein [38] is given by Lf(w) = f ′(w) −wf(w) for
w ∈R, and in Poisson approximation, where L (Z) is the Poisson distribu-
tion with mean λ > 0, the operator L used by Chen [10] is given by Lf(w) =
λf(w+1)−wf(w) for w ∈Z+. However the operator L is not unique even for
the same approximating distribution but depends on the problem at hand.
For example, for normal approximation L can also be taken to be the genera-
tor of the Ornstein-Uhlenbeck process, that is, Lf(w) = f ′′(w)−wf ′(w), and
for Poisson approximation, L taken to be the generator of an immigration-
death process, that is, Lf(w) = λ[f(w + 1) −f(w)] + w[f(w −1) −f(w)].
This generator approach, which is due to Barbour [2], allows extensions to
multivariate and process settings. Indeed, for multivariate normal approxi-
mation, Lf(w) = ∆f(w) −w · ∇f(w), where f is deﬁned on the Euclidean
space; see Barbour [3] and Götze [21].
Examples of expository articles and books on Stein’s method for normal,
Poisson and other probability approximations are Arratia, Goldstein and
Gordon [1], Chatterjee, Diaconis, and Meckes [9], Barbour and Chen [4],
Barbour, Holst and Janson [5], Chen, Goldstein and Shao [12], Chen and
Röllin [14], Diaconis and Holmes [19], and Ross [37].
2.2
Normal approximation
In his 1986 monograh [39], Stein proved the following characterization of
the normal distribution.
Proposition 2.1. The following are equivalent.
(i) W ∼N(0, 1);
(ii) E[f ′(W) −Wf(W)] = 0 for all f ∈C1
B.
Proof. By integration by parts, (i) implies (ii). If (ii) holds, solve
f ′(w) −wf(w) = h(w) −Eh(Z)
(2.3)
3


## Page 4


where h ∈CB and Z ∼N(0, 1). Its solution fh is given by
fh(w)
=
−e
1
2w2 Z ∞
w
e−1
2t2[h(t) −Eh(Z)]dt
=
e
1
2 w2 Z w
−∞
e−1
2 t2[h(t) −Eh(Z)]dt.
(2.4)
Using
R ∞
w e−1
2t2dt ≤w−1e−1
2 w2 for w > 0, we can show that fh ∈C1
B with
∥fh∥∞≤
√
2πe∥h∥∞and ∥f ′
h∥∞≤4∥h∥∞. Substituting fh for f in (ii)
leads to
Eh(W) = Eh(Z)
for
h ∈CB.
This proves (i).
The proof of Propostion 2.1 shows that the Stein operator L for normal
approximation, which is given by Lf(w) = f ′(w) −wf(w), is obtained by
integration by parts.
Assume EW = 0 and Var(W) = B2 > 0. By Fubini’s theorem, for f
absolutely continuous for which the expectations exist, we have
EWf(W) =
Z ∞
−∞
f ′(x)EWI(W > x)dx = B2Ef ′(W ∗)
where L (W ∗) is absolutely continuous with density given by B−2EWI(W >
x). The distribution L (W ∗) is called W-zero-biased. The notion of zero-
biased distribution was introduced by Goldstein and Reinert [20].
Now assume Var(W) = 1. By Propoition 2.1, L (W) = N(0, 1) if and
only if L (W ∗) = L (W). Heuristically this suggests that L (W ∗) is "close"
to L (W) if and only if L (W) is "close" to N(0, 1). Therefore, it is natural
to ask if can we couple W ∗with W in such a way that E|W ∗−W| provides a
good measure of the distance between L (W) and N(0, 1)? There are three
distances commonly used for normal approximation.
Deﬁnition 2.2. Let Z ∼N(0, 1), F(x) = P(W ≤x) and Φ(x) = P(Z ≤
x).
(i) The Wasserstein distance between L (W) and N(0, 1) is deﬁned by
dW(L (W), N(0, 1)) :=
sup
|h(x)−h(y)|≤|x−y|
|Eh(W) −Eh(Z)|.
(ii) The Kolmogorov distance between L (W) and N(0, 1) is deﬁned by
dK(L (W), N(0, 1)) := sup
x∈R
|F(x) −Φ(x)|.
(iii) The total variation distance between L (W) and N(0, 1) is deﬁned by
dTV(L (W), N(0, 1))
:=
sup
A∈B(R)
|P(W ∈A) −P(Z ∈A)|
=
1
2 sup
|h|≤1
|Eh(W) −Eh(Z)|.
4


## Page 5


Note that Eh(W) −Eh(Z) = E(h(W) −h(0)) −E(h(Z) −h(0)). So
dW(L (W), N(0, 1)) =
sup
|h(x)−h(y)|≤|x−y|,h(0)=0
|Eh(W) −Eh(Z)|.
Also note that |h(w)| ≤|h(w)−h(0)|+|h(0)| ≤|w|+|h(0)|. So |h(x)−h(y| ≤
|x −y| implies that h grows linearly. Since C1 functions h with ∥h′∥∞≤1 is
dense in the sup norm in the class of functions h with |h(x)−h(y)| ≤|x−y|,
we also have
dW(L (W), N(0, 1)) =
sup
h∈C1,∥h′∥∞≤1
|Eh(W) −Eh(Z)|.
By an application of Lusin’s theorem,
sup
|h|≤1
|Eh(W) −Eh(Z)| =
sup
h∈C,|h|≤1
|Eh(W) −Eh(Z)|.
Therefore,
dTV(L (W), N(0, 1)) = 1
2
sup
h∈C,|h|≤1
|Eh(W) −Eh(Z)|.
The proposition below concerns the boundedness properties of the so-
lution fh, given by (2.4), of the Stein equation (2.3) for h either bounded
or absolutely continuous with bounded h′. The use of these boundedness
properties is crucial for bounding the distances deﬁned in Deﬁnition 2.2.
Proposition 2.3. Let fh be the unique solution, given by (2.4), of the Stein
equation (2.3), where h is either bounded or absolutely continuous.
1. If h is bounded, then
∥fh∥∞≤
√
2π∥h∥∞,
∥f ′
h∥∞≤4∥h∥∞.
(2.5)
2. If h is absolutely continuous with bounded h′, then
∥fh∥∞≤2∥h′∥∞,
∥f ′
h∥∞≤
q
2/π∥h′∥∞,
∥f ′′
h∥∞≤2∥h′∥∞.
(2.6)
3. If h = I(−∞,x] where x ∈R, then, writing fh as fx,
0 < fx(w) ≤
√
2π/4,
|wfx(w)| ≤1,
|f ′
x(w)| ≤1,
(2.7)
and for all w, u, v ∈R,
|f ′
x(w) −f ′
x(v)| ≤1,
(2.8)
|(w + u)fx(w + u) −(w + v)fx(w + v)| ≤(|w| +
√
2π/4)(|u| + |v|).
(2.9)
The bounds in the proposition and their proofs can be found in Lemmas
2.3 and 2.4 of Chen, Goldstein and Shao [12].
In the case where W ∗is be coupled with W, that is, there is a zero-bias
coupling, we have the following result.
5


## Page 6


Theorem 2.4. Assume that EW = 0 and Var(W) = 1 and that W ∗and W
are deﬁned on the same probability space. Then
dW(L (W), N(0, 1)) ≤2E|W ∗−W|.
(2.10)
Proof. Let h be absolutely continuous with ∥h′∥∞≤1. Then by the deﬁni-
tion of zero-biased distribution and by (2.6),
|Eh(W) −Eh(Z)|
=
|E[f ′
h(W) −Wfh(W)]| = |E[f ′
h(W) −f ′
h(W ∗)]
=
|E
Z W ∗−W
0
f ′′
h(W + t)dt| ≤∥f ′′
h∥∞E|W ∗−W|
≤
2∥h′∥∞E|W ∗−W| ≤2E|W ∗−W|.
This proves the theorem.
Theorem 2.4 shows that E|W ∗−W| provides an upper bound on the
Wasserstein distance. We now construct a zero-bias coupling in the case
where W is a sum of independent random variables and show that E|W ∗−W|
indeed gives an optimal bound.
Let X1, . . . , Xn be independent random variables with EXi = 0, Var(Xi) =
σ2
i > 0 and E|Xi|3 < ∞. Let W = Pn
i=1 Xi and W (i) = W −Xi. Assume
Var(W) = 1(=⇒Pn
i=1 σ2
i = 1).
Deﬁne
(i) I to be such that P(I = i) = σ2
i for i = 1, · · · , n;
(ii) X∗
i to be Xi-zero-biased, i = 1, · · · , n;
(iii) I, X∗
1, · · · , X∗
n, X1, · · · , Xn to be independent.
Then for absolutely continuous f such that ∥f∥∞< ∞and ∥f ′∥∞< ∞,
EWf(W)
=
n
X
i=1
EXif(W (i) + Xi) =
n
X
i=1
σ2
i Ef ′(W (i) + X∗
i )
=
Ef ′(W (I) + X∗
I ) = Ef ′(W ∗).
(2.11)
So W ∗is coupled with W and W ∗−W = X∗
I −XI. Note that the density
of X∗
i is given by σ−2
i
EXiI(Xi > x).
Straightforward calculations yield
E|XI| ≤
n
X
i=1
E|Xi|3 and E|X∗
I | ≤1
2
n
X
i=1
E|Xi|3. Therefore
E|W ∗−W| = E|X∗
I −XI| ≤E|X∗
I | + E|XI| ≤3
2
n
X
i=1
E|Xi|3.
(2.12)
We immediately have the following corollary of Theorem 2.4.
6


## Page 7


Corollary 2.5. Let X1. · · · , Xn be independent with EXi = 0, Var(Xi) =
σ2
i and E|Xi|3 < ∞, i = 1, · · · , n.
Let W = Pn
i=1 Xi and assume that
Var(W) = 1. Then
dW(L (W), N(0, 1)) ≤3
n
X
i=1
E|Xi|3.
(2.13)
It is much more diﬃcult to obtain an optimal bound on the Kolmogorov
distance between L (W) and N(0, 1). Such a bound can be obtained by
induction or by the use of a concentration inequality. For induction, see
Bolthausen [6]. For the use of a concentration inequality, see Chen [11] and
Chen and Shao [16] for sums of independent random variables, and Chen
and Shao [17] for sums of locally dependent random variables.
See also
Chen, Goldstein and Shao [12]. For sums of independent random variables,
Chen and Shao [16] obtained a bound of 4.1 P E|Xi|3 on the Kolmogorov
distance. In the next subsection we will give a proof of an optimal bound
on the Kolmogorov distance using the concentration inequality approach.
In general, it is diﬃcult to construct zero-bias couplings such that E|W ∗−
W| is small for normal approximation. However, by other methods, one can
construct an equation of the form,
EWf(W) = ET1f ′(W + T2),
(2.14)
where T1 and T2 are some random variables deﬁned on the same probability
space as W, and f is an absolutely continuous function for which the ex-
pectations in (2.14) exist. Heuristically, in view of Proposition 2.1, L (W)
is "close" to N(0, 1) if T1 is "close" to 1 and T2 is "close" to 0. Examples
of W satisfying this equation include sums of locally dependent random
variables as considered in Chen and Shao [17] and exchangeable pairs as
deﬁned in Stein [39]. More generally, a random variable W satisﬁes (2.14)
if there is a Stein coupling (W, W ′, G) where W, W ′, G are deﬁned on a
common probability space such that EWf(W) = E
Gf(W ′) −Gf(W)
 for
absolutely continuous functions f for which the expectations exist (see Chen
and Röllin [15]). In all cases it is assumed that EW = 0 and Var(W) = 1.
Letting f(w) = w, we have 1 = EW 2 = ET1. The case of zero-bias coupling
corresponds to T1 = 1.
As an illustration, let (W, W ′) be an exchangeable pair of random vari-
ables, that is, (W, W ′) has the same distribution as (W ′, W). Assume that
EW = 0 and Var(W) = 1 and that E
W ′ −W|W
 = −λW for some λ > 0.
Since the function (w, w′) 7−→(w′ −w)(f(w′)+f(w)) is anti-symmetric, the
exchangeability of (W, W ′) implies
E
(W ′ −W)(f(W ′) + f(W))
 = 0.
7


## Page 8


From this we obtain
EWf(W) = 1
2λE
h
(W ′ −W)(f(W ′) −f(W))
i
= 1
2λE
h
(W ′ −W)2
Z 1
0
f ′(W + (W ′ −W)t)dt
i
= E
T1f ′(W + T2)

where T1 = 1
2λ(W ′ −W)2, T2 = (W ′ −W)U, and U uniformly distributed
on [0, 1] and independent of W, W ′, T1 and T2. The notion of exchange-
able pair is central to Stein’s method. It has been extensively used in the
literature.
Here is a simple example of an exchangeable pair. Let X1, · · · , Xn be
independent random variables such that EXi = 0 and Var(W) = 1, where
W = Pn
i=1 Xi. Let X′
1, · · · , X′
n be an independent copy of X1, · · · , Xn and
let W ′ = W −XI + X′
I, where I is uniformly distributed on {1, · · · , n} and
independent of {Xi, X′
i, 1 ≤i ≤n}. Then (W, W ′) is an exchangeable pair
and E[W ′ −W|W] = −1
nW.
Assume that EW = 0 and Var(W) = 1. From (2.3) and (2.14),
Eh(W) −Eh(Z)
=
E
f ′
h(W) −T1f ′
h(W + T2)

=
E
T1(f ′
h(W) −f ′
h(W + T2))
 + E
(1 −T1)f ′
h(W)
.
(2.15)
Diﬀerent techniques have been developed for bounding the error terms on
the right side of (2.15). Apart from zero-bias coupling, which corresponds
to T1 = 1, we will focus on the case where T2 = 0. This is the case if W
is a functional of independent Gaussian random variables as considered by
Chatterjee [8] or a functional of Gaussian random ﬁelds as considered by
Nourdin and Peccati [28]. In this case, (2.15) becomes
Eh(W) −Eh(Z) = E
(1 −T1)f ′
h(W)
 = E
(1 −E[T1|W])f ′
h(W)
.
Let h be such that |h| ≤1. Then, by Proposition 2.3, we obtain the following
bound on the total variation distance between L (W) and N(0, 1).
dTV(L (W), N(0, 1))
:=
1
2 sup
|h|≤1
|Eh(W) −Eh(Z)|
≤
1
2∥f ′
h∥∞E|1 −E[T1|W]|
≤
2∥h∥∞E|1 −E[T1|W]|
≤
2
q
Var(E[T1|W]),
where for the last inequality it is assumed that E[T1|W] is square integrable.
8


## Page 9


While Chatterjee [8] developed second order Poincaré inequalities to
bound 2
p
Var(E[T1|W]), Nourdin and Peccati [28] deployed Malliavin cal-
culus. In Sections 3 and 4, we will discuss how Malliavin calculus is used to
bound 2
p
Var(E[T1|W]).
2.3
Berry-Esseen theorem
In this subsection, we will give a proof of the Berry-Esseen theorem for sums
of independent random variables using zero-bias coupling and a concentra-
tion inequality.
Theorem 2.6 (Berry-Esseen). Let X1, · · · , Xn be independent random vari-
ables with EXi = 0, Var(Xi) = σ2
i , and E|Xi|3 = γi < ∞. Let W = Pn
i=1 Xi
and assume Var(W) = 1. Then
dK(L (W), N(0, 1)) ≤7.1
n
X
i=1
γi.
(2.16)
We ﬁrst prove two propositions using the same notation as in Theorem
2.6. Let W ∗be W-zero-biased and assume that it is coupled with W as
given in (2.11). Let Φ denote the distribution function of N(0, 1).
Proposition 2.7. For x ∈R,
|P(W ∗≤x) −Φ(x)| ≤2.44
n
X
i=1
γi.
(2.17)
Proof. Let fx be the unique bounded solution of the Stein equation
f ′(w) −wf(w) = I(w ≤x) −Φ(x)
(2.18)
where x ∈R. The solution fx is given by (2.4) with h(w) = I(w ≤x). From
this equation and by (2.9),
|P(W ∗≤x) −Φ(x)|
= |E[f ′
x(W ∗) −W ∗fx(W ∗)]|
= |E[(W (I) + XI)fx(W (I) + XI) −(W (I) + X∗
I )fx(W (I) + X∗
I )]|
≤E(|W (I)| +
√
2π
4
)(|XI| + |X∗
I |)
≤3
2(1 +
√
2π
4
)
n
X
i=1
γi ≤2.44
n
X
i=1
γi.
This proves Proposition 2.7.
Next we prove a concentration inequality.
9


## Page 10


Proposition 2.8. For i = 1, . . . , n and for a ≤b, a, b ∈R, we have
P(a ≤W (i) ≤b) ≤2
√
2
3 (b −a) + 4(
√
2 + 1)
3
n
X
i=1
γi.
(2.19)
Proof. This proof is a slight variation of that of Lemma 3.1 in Chen, Gold-
stein and Shao [12]. Let δ > 0 and let f be given by f((a + b)/2) = 0 and
f ′(w) = I(a −δ ≤w ≤b + δ). Then |f| ≤(b −a + 2δ)/2. Since Xj is
independent of W (i) −Xj for j ̸= i, Xi is independent of W (i), and since
EXj = 0 for j = 1, . . . , n, we have
EW (i)f(W (i)) −EXif(W (i) −Xi)
=
n
X
j=1
EXj[f(W (i)) −f(W (i) −Xj)]
=
n
X
j=1
EXj
Z 0
−Xj
f ′(W (i) + t)dt
=
n
X
j=1
EXj
Z 0
−Xj
I(a −δ ≤W (i) + t ≤b + δ)dt
≥
n
X
j=1
EXj
Z 0
−Xj
I(a −δ ≤W (i) + t ≤b + δ)I(|t| ≤δ)dt
≥EI(a ≤W (i) ≤b)
n
X
j=1
Xj
Z 0
−Xj
I(|t| ≤δ)dt
= EI(a ≤W (i) ≤b)
n
X
j=1
|Xj| min(|Xj|, δ)
≥P(a ≤W (i) ≤b)
n
X
j=1
E|Xj| min(|Xj|, δ)
−EI(a ≤W (i) ≤b)

n
X
j=1
[|Xj| min(|Xj|, δ) −E|Xj| min(|Xj|, δ)]

= R1 −R2,
(2.20)
where in the ﬁrst inequality in (2.20), we used the fact that
Xj
Z 0
−Xj
I(a −δ ≤W (i) + t ≤b + δ)dt ≥0 for j = 1, · · · , n.
10


## Page 11


Using the inequality, min(a, b) ≥a −a2
4b for a, b > 0, we obtain
R1
≥
P(a ≤W (i) ≤b){
n
X
j=1
EX2
j −1
4δ
n
X
j=1
E|Xj|3}
=
P(a ≤W (i) ≤b){1 −1
4δ
n
X
j=1
E|Xj|3}.
(2.21)
We also have
R2
≤
E

n
X
j=1
[|Xj| min(|Xj|, δ) −E|Xj| min(|Xj|, δ)]

≤
Var(
n
X
j=1
|Xj| min(|Xj|, δ))
1/2
≤

n
X
j=1
EX2
j min(|Xj|, δ)21/2
≤
δ

n
X
j=1
EX2
j
1/2 = δ.
(2.22)
Bounding the left hand side of (2.20), we obtain
EW (i)f(W (i)) −EXif(W (i) −Xi)
≤1
2(b −a + 2δ)(E|W (i)| + E|Xi|)
≤
1
√
2(b −a + 2δ)[(E|W (i)|)2 + (E|Xi|)2]1/2
≤
1
√
2(b −a + 2δ)[E(W (i)2) + E(X2
i )]1/2
=
1
√
2(b −a + 2δ).
(2.23)
The proof of Proposition 2.8 is completed by letting δ =
n
X
j=1
E|Xj|3 and
combining (2.20), (2.21), (2.22) and (2.23).
We now prove Theorem 2.6. By Proposition 2.7, we have
|P(W ≤x) −Φ(x)|
≤
|P(W ≤x) −P(W (I) + X∗
I ≤x)|
+2.44
n
X
i=1
γi
=
EI(x −XI ∨X∗
I ≤W (I) ≤x −XI ∧X∗
I )
+2.44
n
X
i=1
γi.
(2.24)
11


## Page 12


Using the independence between I and {Xi, X∗
i , 1 ≤i ≤n}, we have
EI(x −XI ∨X∗
I ≤W (I) ≤x −XI ∧X∗
I )
=
n
X
i=1
σ2
i EI(x −Xi ∨X∗
i ≤W (i) ≤x −Xi ∧X∗
i )
=
n
X
i=1
σ2
i EP(x −Xi ∨X∗
i ≤W (i) ≤x −Xi ∧X∗
i |Xi, X∗
i ).
Since W (i) is indpendent of Xi, X∗
i for i = 1, · · · , n, it follows from (2.19)
that
EI(x −XI ∨X∗
I ≤W (I) ≤x −XI ∧X∗
I )
≤
n
X
i=1
σ2
i E
h2
√
2
3 (|Xi| + |X∗
i |) + 4(
√
2 + 1)
3
n
X
i=1
γi
i
≤
 √
2 + 4(
√
2 + 1)
3
!
n
X
i=1
γi ≤4.65
n
X
i=1
γi.
(2.25)
The proof of Theorem 2.6 is completed by combining (2.24) and (2.25).
3
MALLIAVIN CALCULUS
3.1
Preamble
In this paper, the work of Nourdin and Peccati will be presented in the
context of the Gaussian process X = {
R ∞
0 f(t)dBt : f ∈L2(R+)}, where
(Bt)t∈R+ is a standard Brownian motion on acomplete probability space
(Ω, F, P), where F is generated by (Bt)t∈R+, and L2(R+) is the separable
Hilbert space of square integrable real-valued functions with respect to the
Lebesgue measure on R+. This Gaussian process is a centered Gaussian
family of random variables with the covariance given by
E
 Z ∞
0
f(t)dBt
Z ∞
0
g(t)dBt
 = ⟨f, g⟩L2(R+).
There will be no loss of generality since problems of interest are of distri-
butional nature and through an isometry these problems can be transferred
to X.
More speciﬁcally, let Y = {Y (h) : h ∈H} be a centered Gaussian process
over a real separable Hilbert space H with the covariance given by
E
Y (h1)Y (h2)
 = ⟨h1, h2⟩H.
Let ψ : H →L2(R+) be an isometry and let f1 = ψ(h1) and f2 = ψ(h2) for
h1, h2 ∈H. Then
E
 Z ∞
0
f1(t)dBt
Z ∞
0
f2(t)dBt
 = E[Y (h1)Y (h2)].
12


## Page 13


This implies that L (X) = L (Y ) and problems of distributional nature on
Y can be transferred to X.
The material in this section can be found in Nourdin [27] and Nourdin
and Peccati [29].
3.2
Multiple Wiener-Itô integrals and Wiener chaos
Let B = (Bt)t∈R+ be a standard Brownian motion on a complete probability
space (Ω, F, P), where F is generated by (Bt)t∈R+, and let f ∈L2(Rp
+)
where p is a positive integer. We deﬁne
Ip(f) =
X
σ
Z ∞
0
dBt1
Z t1
0
dBt2 . . .
Z tp−1
0
dBtpf(tσ(1), tσ(2), . . . , tσ(p))
(3.1)
where the sum is over all permutations σ of {1, 2, . . . , p}.
The random
variable Ip(f) is called the pth multiple Wiener-Itô integral.
The closed
linear subspace Hp of L2(Ω) generated by Ip(f), f ∈L2(Rp
+), is called the
pth Wiener chaos of B. We use the convention that H0 = R.
If f is symmetric, that is, f(t1, . . . , tp) = f(tσ(1), . . . , tσ(p)) for any per-
mutation σ of {1, . . . , p}, then
Ip(f) = p!
Z ∞
0
dBt1
Z t1
0
dBt2 . . .
Z tp−1
0
dBtpf(t1, t2, . . . , tp).
We deﬁne the symmetrization of f ∈L2(Rp
+) by
˜f(t1, . . . , tp) = 1
p!
X
σ
f(tσ(1, . . . , tσ(p)),
(3.2)
where the sum is over all permutations σ of {1, . . . , p}.
Let L2
s(Rp
+) be
the closed subspace of L2(Rp
+) of symmetric functions.
By the triangle
inequality,
∥˜f∥L2(Rp
+) ≤∥f∥L2(Rp
+),
we see that f ∈L2(Rp
+) implies ˜f ∈L2
s(Rp
+). The following properties of
the stochastic integrals Ip(·) can be easily veriﬁed:
(i) EIp(f) = 0 and Ip(f) = Ip( ˜f) for all f ∈L2(Rp
+).
(ii) For all f ∈L2(Rp
+) and g ∈L2(Rq
+),
E[Ip(f)Iq(g)] =
(
0
for
p ̸= q,
p!⟨˜f, ˜g⟩L2(Rp
+)
for
p = q.
(3.3)
(iii) The mapping f 7→Ip(f) from L2(Rp
+) to L2(Ω) is linear.
13


## Page 14


The multiple Wiener-Itô integrals are inﬁnite dimensional generalizations
of the Hermite polynomials. The kth Hermite polynomial Hk is deﬁned by
Hk(x) = (−1)ke
x2
2 dk
dxk

e−x2
2

, x ∈R.
If f ∈L2(R+) such that ∥f∥L2(R+) = 1, it can be shown that
Ik(f ⊗k) = Hk
Z ∞
0
f(t)dBt

,
(3.4)
where f ⊗k ∈L2(Rk
+) is the kth tensor product of f with itself deﬁned by
f(t1, . . . , tk) = f(t1) . . . f(tk). If φ = f ⊗k1
1
⊗· · · ⊗f ⊗kp
p
with (fi)1≤i≤p an
orthonormal system in L2(R+) and k1 + · · · + kp = k, (3.4) can be extended
to
Ik(φ) =
p
Y
i=1
Hki
Z ∞
0
fi(t)dBt

.
(3.5)
As in one-dimension where the Hermite polynomials form an orthogonal
basis for L2(R,
1
√
2πe−x2/2dx), the space L2(Ω) can be decomposed into an
inﬁnite orthogonal sum of the closed subspaces Hp. We state this funda-
mental fact about Gaussian spaces as a theorem below.
Theorem 3.1. Any random variable F ∈L2(Ω) admits an orthogonal de-
composition of the form
F =
∞
X
k=0
Ik(fk),
(3.6)
where I0(f0) = E[F], and fk ∈L2(Rk
+) are symmetric and uniquely deter-
mined by F.
Applying the orthogonality relation (3.3) to the symmetric kernels fk for F
in the Wiener chaos expansion (3.6),
∥F∥2
L2(Ω) =
∞
X
k=0
k!∥fk∥2
L2(Rk
+).
(3.7)
The random variables Ik(fk) inherit some properties from the algebraic
structure of the Hermite polynomials, such as the product formula (3.8)
below. To understand this we need the deﬁnition of contraction.
Deﬁnition 3.2. Let p, q ≥1 and let f ∈L2(Rp
+) and g ∈L2(Rq
+) be two
symmetric functions. For r ∈{1, . . . , p ∧q}, the rth contraction of f and g,
denoted by f ⊗r g, is deﬁned by
f ⊗r g(x1, . . . , xp−r, y1, · · · , yq−r)
14


## Page 15


=
Z
Rr
+
f(x1, · · · , xp−r, t1, · · · , tr)g(y1, · · · , yq−r, t1, · · · , tr)dt1 · · · dtr.
By convention, f ⊗0 g = f ⊗g.
The contraction f ⊗r g is not necessarily symmetric, and we denote by
f e⊗rg its symmetrization. Note that by the Cauchy-Schwarz inequality,
∥f ⊗r g∥L2(Rp+q−2r
+
) ≤∥f∥L2(Rp
+)∥g∥L2(Rq
+)
for
r = 0, 1, . . . , p ∧q,
and that f ⊗p g = ⟨f, g⟩L2(Rp
+) when p = q.
We state the product formula between two multiple Wiener-Itô integrals
in the next theorem.
Theorem 3.3. Let p, q ≥1 and let f ∈L2(Rp
+) and g ∈L2(Rq
+) be two
symmetric functions. Then
Ip(f)Iq(g) =
p∧q
X
r=0
r!
 
p
r
! 
q
r
!
Ip+q−2r(f e⊗rg).
(3.8)
3.3
Malliavin derivatives
Let B = (Bt)t∈R+ be a standard Brownian motion on a complete probabil-
ity space (Ω, F, P), where F is generated by B, and let X = {X(h), h ∈
L2(R+)} where X(h) =
R ∞
0 hdBt. The set X is a centered Gaussian family
of random variables deﬁned on (Ω, F, P), with covariance given by
E[X(h)X(g)] = ⟨h, g⟩L2(R+),
for h, g ∈L2(R+). Such a Gaussian family is called an isonormal Gaussian
process over L2(R+).
Let S be the set of all cylindrical random variables of the form:
F = g (X(φ1), . . . , X(φn)) ,
(3.9)
where n ≥1, g : Rn →R is an inﬁnitely diﬀerentiable function such that its
partial derivatives have polynomial growth, and φi ∈L2(R+), i = 1, . . . , n.
It can be shown that the set S is dense in L2(Ω). The Malliavin derivative
of F ∈S with respect to X is the element of L2(Ω, L2(R+)) deﬁned as
DF =
n
X
i=1
∂g
∂xi
(X(φ1), . . . , X(φn)) φi.
(3.10)
In particular, DX(h) = h for every h ∈L2(R+). By iteration, one can
deﬁne the mth derivative DmF, which is an element of L2(Ω, L2(Rm
+)) for
every m ≥2, as follows.
15


## Page 16


DmF =
n
X
i1,··· ,im=1
∂mg
∂xi1 · · · ∂xim
h
X(φ1), · · · , X(φn)
i
φi1 ⊗· · · ⊗φim. (3.11)
The Hilbert space L2(Ω, L2(Rm
+)) of L2(Rm
+)-valued functionals of B is
endowed with the inner product,
⟨u, v⟩L2(Ω,L2(Rm
+ )) = E⟨u, v⟩L2(Rm
+ ).
For m ≥1, it can be shown that Dm is closable from S to L2(Ω, Rm
+). So
the domain of Dm can be extended to Dm,2, the closure of S with respect
to the norm ∥· ∥m,2, deﬁned by
∥F∥2
m,2 = E
h
F 2i
+
m
X
i=1
E

∥DiF∥2
L2(Ri
+)

.
A random variable F ∈L2(Ω) having the Wiener chaos expansion (3.6)
is an element of Dm,2 if and only if the kernels fk, k = 1, 2, . . . satisfy
∞
X
k=1
kmk!∥fk∥2
L2(Rk
+) < ∞,
in which case,
E∥DmF∥2
L2(Rm
+ ) =
∞
X
k=m
(k)mk!∥fk∥2
L2(Rk
+),
where (k)m is the falling factorial.
In particular, any F having a ﬁnite
Wiener chaos expansion is an element of Dm,2 for all m ≥1.
The Malliavin derivative D, deﬁned in (3.10), obeys the following chain
rule.
If g : Rn →R is continuously diﬀerentiable with bounded partial
derivatives and if F = (F1, . . . , Fn) is such that Fi ∈D1,2 for i = 1, . . . , n,
then g(F) ∈D1,2 and
Dg(F) =
n
X
i=1
∂g
∂xi
(F)DFi.
(3.12)
The domain D1,2 can be described in terms of the Wiener chaos decom-
position as
D1,2 =
n
F ∈L2(Ω) :
∞
X
k=1
k∥Ik(fk)∥2
L2(Ω) < ∞
o
.
(3.13)
16


## Page 17


The derivative of F ∈D1,2, where F is of the form (3.6), can be identiﬁed
with the element of L2(R+ × Ω) given by
DtF =
∞
X
k=1
kIk−1 (fk(·, t)) ,
t ∈R+.
(3.14)
Here Ik−1(fk(·, t)) denotes the Wiener-Itô integral of order k−1 with respect
to the k −1 remaining coordinates after holding t ﬁxed. Since the fk are
symmetric, the choice of the coordinate held ﬁxed does not matter.
The Ornstein-Uhlenbeck operator L is deﬁned by the following relation
L(F) =
∞
X
k=0
−kIk(fk),
(3.15)
for F represented by (3.6). It expresses the fact that L is diagonalizable
with spectrum −N and the Wiener chaos as eigenspaces. The domain of L
is
Dom(L) = {F ∈L2(Ω) :
∞
X
k=1
k2k!∥fk∥2
L2(Rk
+) < ∞} = D2,2.
(3.16)
If F = g(X(h1), · · · , X(hn)), where g ∈C2(Rn) with bounded ﬁrst and
second partial derivatives, it can be shown that
L(F)
=
n
X
i,j=1
∂2g
∂xi∂xj
(X(h1), · · · , X(hn))⟨hi, hj⟩L2(R+)
−
n
X
i=1
X(hi) ∂g
∂xi
(X(h1), · · · , X(hn)).
(3.17)
The operator L−1, which is called the pseudo-inverse of L, is deﬁned as
follows.
L−1(F) = L−1h
F −E[F]
i
=
∞
X
k=1
−1
kIk(fk),
(3.18)
for F represented by (3.6). The domain of L−1 is Dom(L−1) = L2(Ω). It is
obvious that for any F ∈L2(Ω), we have L−1F ∈D2,2 and
LL−1F = F −E[F].
(3.19)
A crucial property of L is the following integration by parts formula. For
F ∈D2,2 and G ∈D1,2, we have
E[LF × G] = −E[⟨DF, DG⟩L2(R+)].
(3.20)
17


## Page 18


By the bilinearity of the inner product and the Wiener chaos expansion
(3.6), it suﬃces to prove (3.20) for F = Ip(f) and G = Iq(g) with p, q ≥1
and f ∈L2(Rp
+), g ∈L2(Rq
+) symmetric. When p ̸= q, we have
E[LF × G] = −pE[Ip(f)Iq(g)] = 0
and
E[⟨DF, DG⟩L2(R+)] = pq
Z ∞
0
E[Ip−1(f(·, t))Iq−1(g(·, t))]dt = 0.
So (3.20) holds in this case. When p = q, we have
E[(LF)G] = −pE[Ip(f)Iq(g)] = −pp!⟨f, g⟩L2(Rp
+)
and
E[⟨DF, DG⟩L2(R+)]
=
p2
Z ∞
0
E[Ip−1(f(·, t))Iq−1(g(·, t))]dt
=
p2(p −1)!
Z ∞
0
⟨f(·, t), g(·, t)⟩L2(Rp−1
+
)dt
=
pp!⟨f, g⟩L2(Rp
+).
So (3.20) also holds in this case. This completes the proof of (3.20).
Since L−1(F) ∈Dom(L) = D2,2 ⊂D1,2, for any F ∈D1,2 the quan-
tity ⟨DF, −DL−1F⟩L2(R+) is well deﬁned. As we can see in the next section,
⟨DF, −DL−1F⟩L2(R+) plays a key role in the normal approximation for func-
tionals of Gaussian processes.
In this section, we have only presented those aspects of Malliavin calculus
that will be needed for our exposition of the work of Nourdin and Peccati
in this paper. An extensive treatment of Malliavin calculus can be found in
the book by Nualart [33].
4
CONNECTING STEIN’S METHOD WITH MALLIAVIN
CALCULUS
As is discussed in Section 2, the Stein operator L for normal approximation
is given by Lf(w) = f ′(w) −wf(w) and the equation
E
f ′(W) −Wf(W)
 = 0
(4.1)
holds for all f ∈C1
B if and only if W ∼N(0, 1). It is also remarked there that
if W ∼N(0, 1), (4.1) is a simple consequence of integration by parts. Since
there is the integration by parts formula of Malliavin calculus for functionals
of general Gaussian processes, there is a natural connection between Stein’s
18


## Page 19


method and Malliavin calculus. Indeed, integration by parts has been used
in less general situations to construct the equation
E[Wf(W)] = E[Tf ′(W)]
(4.2)
which is a special case of (2.14). We provide two examples below.
Example 1. Assume E[W] = 0 and Var(W) = 1. Then we have E[T] = 1.
If W has a density ρ > 0 with respect to the Lebesgue measure, then by
integration by parts, W satisﬁes (4.2) with T = h(W), where
h(x) =
R ∞
x yρ(y)dy
ρ(x)
.
If ρ is the density of N(0, 1), then h(x) = 1 and (4.2) reduces to (4.1).
Example 2. Let X = (X1, . . . , Xd) be a vector of independent Gaussian
random variables and let g : Rd →R be an absolutely continuous func-
tion. Let W = g(X). Chatterjee in [8] used Gaussian interpolation and
integration by parts to show that W satisﬁes (4.2) with T = h(X) where
h(x) =
Z 1
0
1
2
√
tE

d
X
i=1
∂g
∂xi
(x) ∂g
∂xi
(
√
tx +
√
1 −tX)
dt.
If d = 1 and g the identity function, then W ∼N(0, 1), h(x) = 1, and again
(4.2) reduces to (4.1).
As the previous example shows (see Chatterjee [8] for details), it is pos-
sible to construct the function h when one deals with suﬃciently smooth
functionals of a Gaussian vector.
This is part of a general phenomenon
discovered by Nourdin and Peccati in [28]. Indeed, consider a functional F
of an isonormal Gaussian process X = {X(h), h ∈L2(R+)} over L2(R+).
Assume F ∈D1,2, E[F] = 0 and Var(F) = 1. Let f : R →R be a bounded
C1 function having a bounded derivative. Since L−1F ∈Dom(L) = D2,2, by
(3.19) and E[F] = 0, we have
F = LL−1F.
Therefore, by the integration by parts formula (3.20),
E[Ff(F)] = E[LL−1F × f(F)] = E[⟨Df(F), −DL−1F⟩L2(R+)]
and by the chain rule,
E[⟨Df(F), −DL−1F⟩L2(R+)] = E[f ′(F)⟨DF, −DL−1F⟩L2(R+)].
Hence
E[Ff(F)] = E[f ′(F)⟨DF, −DL−1F⟩L2(R+)]
(4.3)
19


## Page 20


and F satisﬁes (4.2) with T = ⟨DF, −DL−1F⟩L2(R+).
If F is standard normal, that is, F = I(ψ) =
R ∞
0 ψdBt where ψ = I[0,1].
Then DF = I[0,1] and by (3.18), L−1F = −I(ψ) = −F. So
⟨DF, −DL−1F⟩L2(R+) = ⟨I[0,1], DF⟩L2(R+) = ⟨I[0,1], I[0,1]⟩L2(R+) = 1. (4.4)
This and (4.3) give
EFf(F) = Ef ′(F),
which is the characterization equation for the standard normal distribution.
Now let fh be the unique bounded solution of the Stein equation (2.3)
where h : R →R is continuous and |h| ≤1. Then fh ∈C1 and ∥f ′
h∥∞≤
4∥h∥∞≤4, and we have
E[h(F)] −E[h(Z)]
=
E{f ′
h(F)[1 −⟨DF, −DL−1F⟩L2(R+)]}
=
E{f ′
h(F)[1 −E(⟨DF, −DL−1F⟩L2(R+)|F)]}.
Therefore
sup
h∈C,|h|≤1
|E[h(F)] −E[h(Z)]|
≤
∥f ′
h∥∞E
h
|1 −E(⟨DF, −DL−1F⟩L2(R+)|F)|
i
≤
4E
h
|1 −E(⟨DF, −DL−1F⟩L2(R+)|F)|
i
.
It follows that
dTV(L (F), N(0, 1))
:=
1
2 sup
|h|≤1
|E[h(F)] −E[h(Z)]|
=
1
2
sup
h∈C,|h|≤1
|E[h(F)] −E[h(Z)]|
≤
2E
h
|1 −E(⟨DF, −DL−1F⟩L2(R+)|F)|
i
.
If, in addition, F ∈D1,4, then ⟨DF, −DL−1F⟩L2(R+) is square-integrable
and
E
h
|1 −E(⟨DF, −DL−1F⟩L2(R+)|F)|
i
≤
q
Var[E(⟨DF, −DL−1F⟩L2(R+)|F)].
Thus we have the following theorem of Nourdin and Peccati [28].
Theorem 4.1. Let F ∈D1,2 such that E[F] = 0 and Var(F) = 1. Then
dTV(L (F), N(0, 1)) ≤2E
h
|1 −E(⟨DF, −DL−1F⟩L2(R+)|F)|
i
.
(4.5)
If, in addition, F ∈D1,4, then
dTV(L (F), N(0, 1)) ≤2
q
Var[E(⟨DF, −DL−1F⟩L2(R+)|F)].
(4.6)
If F is standard normal, (4.4) implies that the upper bound in (4.5) is
zero. This shows that the bound is tight.
20


## Page 21


5
THE FOURTH MOMENT THEOREM
5.1
The fourth moment phenomenon
The so-called fourth moment phenomenon was ﬁrst discovered by Nualart
and Peccati [34] who proved that for a sequence of multiple Wiener-Itô in-
tegrals {Fn} of ﬁxed order such that E[F 2
n] →1, the following are equivalent.
(i) L (Fn) →N(0, 1);
(ii) E[F 4
n] →3.
Combining Stein’s method with Malliavin calculus, Nourdin and Peccati
[28] obtained an elegant bound on the rate of convergence, which we will
call the fourth moment theorem.
Theorem 5.1. Let F belong to the kth Wiener chaos of B for k ≥2 such
that E[F 2] = 1. Then
dTV(L (F), N(0, 1)) ≤2
s
k −1
3k
q
E[F 4] −3.
(5.1)
Proof. This proof is taken from Nourdin [27].
Write F = Ik(fk) where
fk ∈L2
s(Rk) is symmetric. By (3.7), E[F 2] = k!∥fk∥2
L2(R+). By the equation
(3.14), we have DtF = DtIk(fk) = kIk−1(fk(·, t)). Applying the product
formula (3.8) for multiple integrals, we obtain
1
k∥DF∥2
L2(R+)
=
1
k⟨DF, DF⟩L2(R+)
=
k
Z ∞
0
Ik−1(fk(·, t))2dt
=
k
Z ∞
0
k−1
X
r=0
r!
 
k −1
r
!2
I2k−2−2r
fk(·, t)e⊗rfk(·, t)
dt
=
k
k−1
X
r=0
r!
 
k −1
r
!2
I2k−2−2r
Z ∞
0
fk(·, t)e⊗rfk(·, t)dt

=
k
k−1
X
r=0
r!
 
k −1
r
!2
I2k−2−2r
 fk e⊗r+1fk

=
k
k
X
r=1
(r −1)!
 
k −1
r −1
!2
I2k−2r
 fk e⊗rfk

=
k
k−1
X
r=1
(r −1)!
 
k −1
r −1
!2
I2k−2r
 fk e⊗rfk
 + k!∥f∥2
L2(R+)
=
k
k−1
X
r=1
(r −1)!
 
k −1
r −1
!2
I2k−2r
 fk e⊗rfk
 + E[F 2].
(5.2)
21


## Page 22


Note that since F = Ik(fk) and E[F] = 0, we have L−1F = −1
kF. So
⟨DF, −DL−1F⟩L2(R+) = 1
k⟨DF, DF⟩L2(R+) = 1
k∥DF∥2
L2(R+).
Letting f(F) = F in the Stein identity (4.3), we obtain
E
⟨DF, −DL−1F⟩L2(R+)
 = E[F 2].
Applying the orthogonality of the Wiener chaos and the formula (3.3),
Var

⟨DF, −DL−1F⟩L2(R+)

= Var
1
k∥DF∥2
L2(R+)

=
k−1
X
r=1
r2
k2 (r!)2
 
k
r
!4
(2k −2r)!∥fk e⊗rfk∥2
L2(R2k−2r).
(5.3)
By the product formula (3.8) again, we have
F 2 =
k
X
r=0
r!
 
k
r
!2
I2k−2r(fk e⊗rfk).
(5.4)
Applying the Stein identity (4.3), we have
E[F 4] = E[F × F 3]
=
3E
F 2 × ⟨DF, −DL−1F⟩L2(R+)

=
3E
F 2 × 1
k∥DF∥2
L2(R+)
.
(5.5)
This together with (5.2), (5.4) and the formula (3.3) yield
E[F 4]
=
3(E[F 2])2 + 3
k
k−1
X
r=1
r(r!)2
 
k
r
!4
(2k −2r)!∥fk e⊗rfk∥2
L2(R2k−2r
+
)
=
3 + 3
k
k−1
X
r=1
r(r!)2
 
k
r
!4
(2k −2r)!∥fk e⊗rfk∥2
L2(R2k−2r
+
).
(5.6)
Comparing (5.3) and (5.6) leads to
Var

⟨DF, −DL−1F⟩L2(R+)

≤k −1
3k

E[F 4] −3

.
(5.7)
Since Var[E(⟨DF, −DL−1F⟩L2(R+)|F)] ≤Var

⟨DF, −DL−1F⟩L2(R+)

, The-
orem 5.1 follows from (4.6).
As one can see from (5.6), E[F 4] ≥3 whenever F is a multiple Wiener-
Itô integral with variance 1. Theorem 5.1 also implies the result of Nualart
and Peccati [34] mentioned above. Without loss of generality, we assume
that E[F 2
n] = 1. The part of (ii) =⇒(i) follows immediately from (5.1).
22


## Page 23


For the part of (i) =⇒(ii) (which actually is independent of Theorem 5.1),
we observe that by the continuous mapping theorem, we have L (F 4
n) →
L (Z4) where Z ∼N(0, 1). Write Fn = Ik(fn). By the hypercontractivity
inequality (Nelson [26]),
E[|Ik(f)|r] ≤[(r −1)kk!]r∥f∥r
L2(Rk
+)
for
k ≥1, r ≥2, f ∈L2(Rk
+),
and the given condition that k!∥fn∥2
L2(Rk
+) = E[Ik(fn)2] = E[F 2
n] = 1, we
have supn E[|Fn|r] < ∞for r > 4.
This implies that {F 4
n} is uniformly
integrable and therefore E[F 4
n] →E[Z4] = 3, and (ii) follows.
From (5.6), we observe that (ii) is equivalent to ∥fk e⊗rfk∥2
L2(R2k−2r
+
) →0
for r = 1, · · · , k−1. This fact is also contained in the theorem of Nualart and
Peccati [34]. The equation (5.6) also shows that the calculation of E[F 4]−3
depends on that of ∥fk e⊗rfk∥2
L2(R2k−2r
+
) for r = 1, · · · , k −1.
In more recent work, Nourdin and Peccati [30] proved the following op-
timal fourth moment theorem, which improves Theorem 5.1.
Theorem 5.2. Let {Fn} be a sequence of random variables living in a
Wiener chaos of ﬁxed order such that E[F 2
n] = 1.
Assume that Fn con-
verges to Z ∼N(0, 1), in which case E[F 3
n] →0 and E[F 4
n] →3. Then there
exist two ﬁnite constants, 0 < c < C, possibly depending on the order of the
Wiener chaos and on the sequence {Fn}, but not on n, such that
cM(Fn) ≤dTV(L (Fn), N(0, 1)) ≤CM(Fn),
(5.8)
where M(Fn) = max{E[F 4
n] −3, |E[F 3
n]|}.
This shows that the bound in (5.1) is optimal if and only if
p
E[F 4n] −3
and |E[F 3
n]| are of the same order (typically
1
√n).
5.2
Breuer-Major theorem
In this subsection, we show how the fourth moment theorem, that is, Theo-
rem 5.1, can be applied to prove the Breuer-Major theorem [7]. We begin by
ﬁrst introducing the notion of Hermite rank of a function. It is well-known
that every φ ∈L2 R,
1
√
2πe−x2/2dx
 can be expanded in a unique way in
terms of the Hermite polynomials as follows.
φ(x) =
∞
X
q=0
aqHq(x).
(5.9)
We call d the Hermite rank of φ if d is the ﬁrst integer q ≥0 such that
aq ̸= 0. We now state the Breuer-Major theorem.
23


## Page 24


Theorem 5.3. Let {Xk}k≥1 be a centered stationary Gaussion sequence,
where each Xk ∼N(0, 1), and let φ ∈L2 R,
1
√
2πe−x2/2dx
 be given by
(5.9). Assume that a0 = E[φ(X1)] = 0 and that P
k∈Z |ρ(k)|d < ∞, where
ρ is the covariance function of {Xk}k≥1 and d the Hermite rank of φ. Let
Vn =
1
√n
Pn
k=1 φ(Xk). Then as n →∞, we have
L (Vn) →N(0, σ2)
(5.10)
where σ2 ∈[0, ∞) and is given by
σ2 =
∞
X
q=d
q!a2
q
X
k∈Z
ρ(k)q.
(5.11)
The original proof of Theorem 5.3 uses the method of moments, by which
one has to compute all the moments of Vn and show that they converge to
the corresponding moments of the limiting distribution. The fourth moment
theorem oﬀers a much simpler approach by which we only need to deal with
the fourth moment of Vn. We will give a sketch of the proof here that applies
the fourth moment theorem. A detailed proof can be found in Nourdin [27].
Proof. First we show that
Var(Vn) = E[V 2
n ] =
∞
X
q=d
q!a2
q
X
r∈Z
ρ(r)q(1 −|r|
n )I(|r| < n).
(5.12)
Since
q!a2
q|ρ(r)|q(1 −|r|
n )I(|r| < n) ≤q!a2
q|ρ(r)|q ≤q!a2
q|ρ(r)|d
and
∞
X
q=d
X
r∈Z
q!a2
q|ρ(r)|d = E[φ2(X1)]
X
r∈Z
|ρ(r)|d < ∞,
it follows by an application of the dominated convergence theorem that
E[V 2
n ] →σ2, where σ2 ∈[0, ∞) and is given by (5.11). If σ2 = 0, then there
is nothing to prove. So we assume that σ2 > 0.
The proof of (5.10) can be divided into three parts in increasing general-
ity of φ: (i) φ is a Hermite polynomial, (ii) φ is a real polynomial, and (iii)
φ ∈L2 R,
1
√
2πe−x2/2dx). We sketch the proof of part (i). Let H be the real
separable Hilbert space generated by {Xk}k≥1 and let ψ : H →L2(R+) be
an isometry. Deﬁne hk = ψ(Xk) for k ≥1. Then we have
Z ∞
0
hk(x)hl(x)dx = E[XkXl] = ρ(k −l).
Therefore
L {Xk : k ∈N} = L
 Z ∞
0
hk(t)dBt : k ∈N
	,
24


## Page 25


where B = (Bt)t≥0 is a standard Brownian motion.
Note that for each
k ≥1, ∥hk∥2
L2(R+) = E[X2
k] = 1. Since φ = Hq for some q ≥1, we have
Vn =
1
√n
n
X
k=1
Hq(Xk)
L=
1
√n
n
X
k=1
Hq
  Z ∞
0
hk(t)dBt

=
1
√n
n
X
k=1
Iq(h⊗q
k ) = Iq(fn,q)
where
fn,q =
1
√n
n
X
k=1
h⊗q
k .
It can be shown (see Nourdin [27] for details) that ∥fn,q e⊗rfn,q∥2
L2(R2k−2r
+
) →0
as n →∞for r = 1, · · · , k−1. By Theorem 5.1 and (5.6) taking into account
an appropriate scaling, part (i) is proved. Part (ii) follows from part (i)
by writing a polynomial as a linear combination of Hermite polynomials
and then applying a theorem of Peccati and Tudor [36], which concerns
the equivalence between marginal and joint convergence in distribution of
multiple Wiener-Itô integrals to the normal distributions.
For part (iii),
write
Vn
=
1
√n
n
X
k=1
N
X
q=1
aqHq(Xk) +
1
√n
n
X
k=1
∞
X
q=N+!
aqHq(Xk)
=
Vn,N + Rn,N.
Then apply part (ii) to Vn,N and show that supn≥1 E[R2
n,N] →0 as N →∞.
This completes the proof of Theorem 5.3.
Bounds on the rate of convergence in the Breuer-Major theorem have
been obtained by Nourdin, Peccati and Podoskij [31], who considered ran-
dom variables of the form Sn =
1
√n
Pn
k=1[f(Xk) −Ef(Xx)], n ≥1, where
{Xk}k∈Z is a d-dimensional stationary Gaussian process and f : Rd →R a
measurable function. They obtained explicit bounds on |Eh(Sn) −Eh(S)|,
where S is a normal random variable and h a suﬃciently smooth function.
Their results both generalize and reﬁne the Breuer-Major theorem and some
other central limit theorems in the literature. The methods they used are
based on Malliavin calculus, interpolation techniques and Stein’s method.
5.3
Quadratic variation of fractional Brownian motion
In this subsection, we consider another application of Theorem 5.1 and also
of Theorem 5.2. Let BH = (BH
t )t≥0 be a fractional Brownian motion with
25


## Page 26


Hurst index H ∈(0, 1), that is, BH is a centered Gaussian process with
covariance function given by
E[BH
t BH
s ] = 1
2(t2H + s2H −|t −s|2H),
s, t ≥0.
This BH is self-similar of index H and has stationary increments.
Consider the sum of squares of increments,
Fn,H = 1
σn
n
X
k=1
[(BH
k −BH
k−1)2 −1] = 1
σn
n
X
k=1
H2(BH
k −BH
k−1)
(5.13)
where H2 is the 2nd Hermite polynomial and σn > 0 is such that E[F 2
n,H] =
1. An application of the Breuer-Major theorem shows that for 0 < H ≤3
4,
L (Fn,H) →N(0, 1)
as
n →∞.
Nourdin and Peccati [29] applied Theorem 5.1 to prove the following theorem
which provides the rates of convergence for diﬀerent values of the Hurst index
H.
Theorem 5.4. Let Fn,H be as deﬁned in (5.13). Then
dTV(Fn,H, N(0, 1)) ≤cH













1
√n
if
H ∈(0, 5
8)
(log n)
3
2
√n
if
H = 5
8
n4H−3
if
H ∈(5
8, 3
4)
1
log n
if
H = 3
4.
(5.14)
Proof. We will give a sketch of the proof in Nourdin [27].
Consider the
closed linear subspace H of L2(Ω) generated by (BH
k )k∈N. As it is a real
separable Hilbert space, there exists an isometry ψ : H →L2(R+). For any
k ∈N, deﬁne hk = ψ(BH
k −BH
k−1). Then for k, l ∈N, we have
Z ∞
0
hk(x)hl(x)dx = E[(BH
k −BH
k−1)(BH
l −BH
l−1)] = ρ(k −l)
(5.15)
where
ρ(r) = 1
2(|r + 1|2H + |r −1|2H −2|r|2H).
(5.16)
Therefore
L {BH
k −BH
k−1 : k ∈N} = L
n Z ∞
0
hk(t)dBt : k ∈N
o
where B = (Bt)t≥0 is a standard Brownian motion. Consequently, without
loss of generality, we can regard Fn,H as
Fn = 1
σn
n
X
k=1
H2
  Z ∞
0
hk(t)dBt
.
26


## Page 27


Since for k ∈N, ∥hk∥2
L2(R+) = ρ(0) = 1 (by (5.15) and (5.16)), we have
Fn = 1
σn
n
X
k=1
I2(hk ⊗hk) = I2(fn)
(5.17)
where Ip, p ≥1, is the pth multiple Wiener-Itô integral with respect to B,
and
fn = 1
σn
n
X
k=1
hk ⊗hk.
Now straightforward calculations yield
σ2
n = 2
n
X
k,l=1
ρ2(k −l) = 2
X
|r|<n
(n −|r|)ρ2(r).
It can be shown that for H < 3
4, we have P
r∈Z ρ2(r) < ∞, and
lim
n→∞
σ2
n
n = 2
X
r∈Z
ρ2(r),
(5.18)
and for H = 3
4, we have
lim
n→∞
σ2
n
n log n = 9
16.
(5.19)
Now we come to calculating the bound
p
E[F 4n] −3 in Theorem 5.1. We
ﬁrst note that fn is symmetric, and so fn e⊗fn = fn⊗fn. Therefore, by (5.6),
we have
E[F 4
n] −3
=
48∥fn e⊗1fn∥2
L2(R2
+)
=
48∥fn ⊗1 fn∥2
L2(R2
+)
=
48
σ4n
n
X
i,j,k,l=1
ρ(k −l)ρ(i −j)ρ(k −i)ρ(l −j).
(5.20)
By bounding the extreme right of (5.20) (see Nourdin [27] for details), we
obtain
E[F 4
n] −3 ≤48n
σ4n

X
|k|<n
|ρ(k)|
4
3


3
.
(5.21)
From the asymptotic behavior of ρ(k) as |k| →∞, we can show that
X
|k|<n
|ρ(k)|
4
3 =





O(1)
if
H ∈(0, 5
8)
O(log n)
if
H = 5
8
O(n(8H−5)/3
if
H ∈(5
8, 1).
(5.22)
27


## Page 28


This, together with (5.18) and (5.21), implies
q
E[F 4n] −3 ≤cH







1
√n
if
H ∈(0, 5
8)
(log n)3/2
√n
if
H = 5
8
n(4H−3)
if
H ∈(5
8, 3
4).
For H = 3
4, combining (5.19), (5.21) and (5.22) gives
q
E[F 4n] −3 = O

1
log n

.
This proves Theorem 5.4
In Nourdin and Peccati [30], the bounds in (5.8) are applied to obtain
the following improvement of (5.14) for H ∈(0, 3
4).
Theorem 5.5. Let Fn,H be as deﬁned in (5.13). Then
dTV(Fn,H, N(0, 1)) ∝







1
√n
if
H ∈(0, 2
3)
(log n)2
√n
if
H = 2
3
n6H−9
2
if
H ∈(2
3, 3
4).
where for nonnegative sequences (un) and (vn), we write vn ∝un to mean
0 < lim inf vn/un ≤lim sup vn/un < ∞.
For H > 3
4, Fn,H does not converge to a Gaussian distribution. Instead,
it converges to the so-called Rosenblatt distribution, which belongs to the
second Wiener chaos and is therefore not Gaussian.
The expository paper by Nourdin [27], the survey paper by Peccati [35]
with an emphasis on more recent results, and the book by Nourdin and
Peccati [29], cover many topics and give detailed development of this new
area of normal approximation.
6
ACKNOWLEGMENT
I would like to thank Ivan Nourdin for some very helpful discussions during
the course of writing this paper and for reading the drafts of this paper and
giving very helpful comments. This work is partially supported by Grant C-
146-000-034-001 and Grant R-146-000-182-112 from the National University
of Singapore.
28


## Page 29


REFERENCES
[1] Arratia, R., Goldstein, L and Gordon, L. (1990). Poisson approximation
and the Chen-Stein method. Statist. Sci. 5, 403–434. With comments
and a rejoinder by the authors.
[2] Barbour, A. D. (1988). Stein’s method and Poisson process convergence.
J. Appl. Probab. 25A, 175-184.
[3] Barbour, A. D. (1990). Stein’s method for diﬀusion approximations.
Probab. Theory Related Fields 84, 297-322.
[4] Barbour, A. D. and Chen, L. H. Y. editors (2005a). An Introduction to
Stein’s Method, Lecture Notes Series No. 4, Institute for Mathematical
Sciences, National University of Singapore, Singapore University Press
and World Scientiﬁc Publishing.
[5] Barbour, A. D., Holst, L. and Janson, S. (1992). Poisson Approximation,
Oxford Studies in Probability No. 2, Oxford University Press.
[6] Bolthausen, E. (1984). An estimate of the remainder in a combinatorial
central limit theorem. Z. Wahrsch. Verw. Gebiete . 66. 379-386.
[7] Breuer, P., Major, P. (1983). Central limit theorems for nonlinear func-
tionals of Gaussian ﬁelds. J. Multivariate Anal., 13, no. 3, 425-441.
[8] Chatterjee, S (2009). Fluctuations of eigenvalues and second order
Poincaré inequalities. Probab. Theory Related Fields 143, 1-40.
[9] Chatterjee, S., Diaconis, P. and Meckes, E. (2005). Exchangeable pairs
and Poisson approximation. Probab. Surv. 2, 64–106.
[10] Chen, L. H. Y. (1975). Poisson approximation for dependent trials.
Ann. Probab. 3, 534–545.
[11] Chen, L. H. Y. (1998). Stein’s method: some perspectives with appli-
cations. Probability Towards 2000 (L. Accardi and C. C. Heyde, eds.),
Lecture Notes in Statistics No. 128, Springer Verlag, 97-122.
[12] Chen, L. H. Y., Goldstein, L. and Shao, Q. M. (2011). Normal Approx-
imation by Stein’s Method, Probability and its Applications, Springer.
[13] Chen, L. H. Y. and Poly, G. (2015). Stein’s method, Malliavin calculus,
Dirichlet forms and the fourth moment theorem. Festschrift Masatoshi
Fukushima (Z-Q Chen, N. Jacob, M. Takeda and T. Uemura, eds.),
Interdisciplinary Mathematical Sciences Vol. 17, World Scientiﬁc, 107-
130.
[14] Chen, L. H. Y. and Röllin, A. (2013). Approximating dependent rare
events. Bernoulli 19, 1243-1267.
[15] Chen, L. H. Y. and Röllin, A. (2013). Stein couplings for normal ap-
proximation. Preprint.
29


## Page 30


[16] Chen, L. H. Y. and Shao, Q.M. (2001). A non-uniform Berry-Esseen
bound via Stein’s method. Prob. Theo. Rel. Fields 120, no 3, 236-254.
[17] Chen, L. H. Y. and Shao, Q.M. (2004). Normal approximation under
local dependence. Ann. Prob. 32, no 3, 1727-2303.
[18] Chen, L. H. Y. and Shao, Q. M. (2005). Stein’s method for normal
approximation. An Introduction to Stein’s Method (A.D. Barbour and L.
H. Y. Chen, eds), Lecture Notes Series No. 4, Institute for Mathematical
Sciences, National University of Singapore, Singapore University Press
and World Scientiﬁc , 1-59.
[19] Diaconis, P. and Holmes, S. (2004). Stein’s Method: Expository Lec-
tures and Applications, IMS Lecture Notes Monogr. Ser. 46, Inst. Math.
Statist., Beachwood, OH.
[20] Goldstein, L. and Reinert, G. (1997). Stein’s method and the zero bias
transformation with application to simple random sampling. Ann. Appl.
Probab. 7, no 4, 837-1139.
[21] Götze, F. (1991). On the rate of convergence in the multivariate
CLT. Ann. Probab. 19, 724–739.
[22] Hoeﬀding, W. (1951). A combinatorial central limit theorem. Ann.
Math. Statist. 22, 558-566.
[23] Hörmander, L. (1967). Hypoelliptic second order diﬀerential equations.
Acta Math. 119, 147–171.
[24] Ledoux, M., Nourdin, I. and Peccati, G. (2015). Stein’s method, loga-
rithmic Sobolev and transport inequalities. Geom. Funct. Anal., 25, no,
1, 256-306.
[25] Malliavin, P. (1978). Stochastic calculus of variations and hypoellip-
tic operators. Proc. Int. Symp. on Stoch. Diﬀ. Equations, Kyoto 1976,
Wiley, 195-263.
[26] Nelson, E. (1973). The free Markoﬀﬁeld. J. Funct. Analysis, 12, 211-
227.
[27] Nourdin, I. (2013). Lectures on Gaussian approximations with Malli-
avin calculus. Sém. Probab. XLV, Springer, 3-89.
[28] Nourdin, I. and Peccati, G. (2009). Stein’s method on Wiener chaos.
Probab. Theory and Related Fields. 145, no. 1-2, 75-118.
[29] Nourdin, I. and Peccati, G. (2012). Normal Approximation with Malli-
avin Calculus: From Stein’s Method to Universality, Cambridge Tracts
in Mathematics Vol. 192, Cambridge University Press.
[30] Nourdin, I. and Peccati, G. (2013). The optimal fourth moment theo-
rem. Proc. Amer. Math. Soc., to appear.
30


## Page 31


[31] Nourdin, I, Peccati, G and Podolskij, M (2011). Quantitative Breuer-
Major theorems. Stoch. Proc. Appl. 121, no. 4, 793-812.
[32] Nourdin, I., Peccati, G. and Swan, Y. (2013). Entropy and the fourth
moment phenomenon. J. Funct. Anal. 266, 3170-3207.
[33] Nualart, D. (2006). The Malliavin Calculus and Related Topics, 2nd
edition, Springer.
[34] Nualart, D. and Peccati, G. (2005). Central limit theorems for se-
quences of multiple stochastic integrals. Ann. Probab. 33, 177-193.
[35] Peccati, G. (2014). Quantitative CLTs on a gaussian space: a survey of
recent developments. ESAIM Proc. and Surv. 44, 61-78.
[36] Peccati, G. and Tudor, C. A. (2005). Gaussian limits for vector-valued
multiple stochastic integrals. Sém. Probab. XXXVIII, Springer, 247-
262.
[37] Ross, N. (2011). Fundamentals of Stein’s method. Probab. Surv. 8, 210–
293.
[38] Stein, C. (1972). A bound for the error in the normal approximation
to the distribution of a sum of dependent random variables. In Pro-
ceedings of the Sixth Berkeley Symposium on Mathematical Statistics
and Probability (Univ. California, Berkeley, Calif., 1970/1971), Vol. II:
Probability Theory, 583–602, Univ. California Press, Berkeley, Calif.
[39] Stein, C. (1986). Approximate Computation of Expectations, IMS Lec-
ture Notes Monogr. Ser. 7, Inst. Math. Statist., Hayward, CA.
[40] Wald, A. and Wolfowitz, J. (1944). Statistical tests based on permuta-
tions of the observations. Ann. Math. Statist. 15, 358-372.
31

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]