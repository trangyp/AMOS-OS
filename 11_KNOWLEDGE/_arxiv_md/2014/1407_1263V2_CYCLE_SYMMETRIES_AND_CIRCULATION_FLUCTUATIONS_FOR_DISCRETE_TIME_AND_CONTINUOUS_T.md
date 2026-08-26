---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1407.1263v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1407.1263v2_Cycle_symmetries_and_circulation_fluctuations_for_discrete-time_and_continuous-t

> Source: 1407.1263v2_Cycle_symmetries_and_circulation_fluctuations_for_discrete-time_and_continuous-t.pdf

> Pages: 30

---


## Page 1


Cycle symmetries and circulation ﬂuctuations for
discrete-time and continuous-time Markov chains
Chen Jia1,2,
Daquan Jiang1,3,
Minping Qian1
1LMAM, School of Mathematical Sciences, Peking University, Beijing 100871, P.R. China
2Beijing International Center for Mathematical Research, Beijing 100871, P.R. China
3Center for Statistical Science, Peking University, Beijing 100871, P.R. China
Abstract
In probability theory, equalities are much less than inequalities. In this paper, we ﬁnd a series
of equalities which characterize the symmetry of the forming times of a family of similar cycles
for discrete-time and continuous-time Markov chains. Moreover, we use these cycle symmetries
to study the circulation ﬂuctuations for Markov chains. We prove that the empirical circulations
of a family of cycles passing through a common state satisfy a large deviation principle with a
rate function which has an highly non-obvious symmetry. Finally, we discuss the applications of
our work in statistical physics and biochemistry.
Keywords: Haldane equality, current ﬂuctuations, ﬂuctuation theorems, large deviations, nonequi-
librium
Classiﬁcations: 60J10, 60J20, 60J27, 60J28, 60F10
1
Introduction
Markov chains are widely used to model various stochastic systems in physics, chemistry, bi-
ology, and engineering. The trajectory of a Markov chain constantly forms various kinds of cycles.
The cycle representation theory of Markov chains [1–7] not only possesses rich theoretical contents,
but has become a fundamental tool in dealing with nonequilibrium systems in natural sciences as
well. We refer to two books [8, 9] for the theoretical contents of the cycle representation theory
and refer to two papers [10, 11] for the applications of the cycle representation theory in physics,
chemistry, and biology.
The earliest theoretical result of the cycle representation theory is probably the Kolmogorov’s
criterion for reversibility [12], which claims that a stationary Markov chain is reversible if and only
if the product of transition probabilities (rates) along each cycle c and that along its reversed cycle
c−are the same. Illuminated by the diagram method [13, 14] developed by Hill in his study of cycle
kinetics in biochemical systems, the Qians’ [1–5] and Kalpazidou [6, 9] introduced the important
concept of circulations for Markov chains and further enriched the cycle representation theory. Let
Nc
t denote the number of cycle c formed by a Markov chain up to time t. The circulation Jc of cycle
c is a nonnegative real number deﬁned as the following almost sure limit:
Jc = lim
t→∞
1
t Nc
t ,
a.s.,
(1)
which represents the number of cycle c formed per unit time. It turns out that a stationary Markov
chain is reversible if and only if the circulations of each cycle c and its reversed cycle c−are the
arXiv:1407.1263v2  [math.PR]  18 Jul 2014


## Page 2


same. This explains why the cycle representation theory is naturally related to the nonequilibrium
(irreversible) phenomena in natural sciences.
Recently, biophysicists have applied the cycle representation theory to study single-molecule
enzyme kinetics and found an interesting relation named as the generalized Haldane equality [11, 15–
17]. Mathematically, each chemical reaction catalyzed by an enzyme can be modeled as a Markov
chain with three states (see Section 7.2). Let T c be the forming time of cycle c, which is deﬁned as
the time required for the Markov chain to form cycle c for the ﬁrst time, and let T c−be the forming
time of its reversed cycle c−. Qian and Xie [15] and Ge [16] proved that for three-state Markov
chains, although the distributions of T c and T c−can be different, their distributions, conditional on
the corresponding cycle is formed early than its reversed cycle, are the same:
P(T c ≤t|T c < T c−) = P(T c−≤t|T c−< T c).
(2)
This equality, which characterizes the symmetry of the forming times of a cycle and its reversed
cycle, is named as the generalized Haldane equality since it generalizes of what is known as the
Haldane relation for reversible enzyme kinetics [15].
Now that the generalized Haldane equality holds for three-state Markov chains, it is natural to
ask whether it holds for general Markov chains. If a Markov chain has only three states, then it has
only two “effective cycles” (clockwise and counterclockwise cycles) and the generalized Haldane
equality can be proved using the method of quasi-time reversal [16, 17]. However, this method
depends too much on the cyclic topology of three-state Markov chains and cannot be generalized to
general Markov chains with a large number of “effective cycles”.
In this paper, we establish some deep properties of taboo probabilities and use them to prove
the generalized Haldane equality for general discrete-time and continuous-time Markov chains with
denumerable state space. We ﬁnd that the generalized Haldane equality not only holds for a cycle and
its reversed cycle, but also holds for a family of similar cycles, which are deﬁned as cycles passing
through the same set of states (see Deﬁnition 9). Let c1, c2, · · · , cr be a family of similar cycles,
let Tc1, Tc2, · · · , Tcr be their forming times, and let T = min{Tc1, Tc2, · · · , Tcr}. In this paper,
we prove that although the distributions of Tc1, Tc2, · · · , Tcr can be different, their distributions,
conditional on the corresponding cycle is formed earlier than any other similar cycles, are the same:
P(Tc1 ≤t|T = Tc1) = P(Tc2 ≤t|T = Tc2) = · · · = P(Tcm ≤t|T = Tcm).
(3)
This equality also shows that the forming time T of two or more similar cycles is independent of
which one of these cycles is formed (see Corollary 1 and Remark 4), which is another important
aspect of the generalized Haldane equality. The generalized Haldane equality has many variations
which are closely related. These results, which include Theorems 1-4 and Corollaries 1-6, will be
collectively referred to as the generalized Haldane “equalities” in this paper.
The generalized Haldane equalities established in this paper have wide applications. One of the
most important applications of the generalized Haldane equalities is to study the circulation ﬂuc-
tuations for Markov chains. In recent two decade, the studies about the ﬂuctuations for stochastic
systems have become a central topic in nonequilibrium statistical physics [18]. Motivated by the
2


## Page 3


results of numerical simulations [19], Gallavotti and Cohen [20] gave the ﬁrst mathematical pre-
sentation of the ﬂuctuation theorem for a class of stationary nonequilibrium systems. They proved
that under suitable assumptions, the probability distribution of the phase space contraction averaged
along the trajectory satisﬁes a large deviation principle with a rate function which has a highly non-
obvious symmetry. Since then there has been a large amount of literature exploring various kinds
of generalizations of the ﬂuctuation theorem. In recent years, physicists become increasingly con-
cerned about the ﬂuctuations of circulations for Markov chains [18], since the entropy production,
as a central concept in nonequilibrium statistical physics, can be decomposed into different cycles
where the circulations emerge naturally (see Section 7.1). The entropy production ﬂuctuations have
been studied thoroughly [21–23]. However, the circulation ﬂuctuations for general Markov chains
remain poorly understood up till now.
Surprisingly, the generalized Haldane equalities established in this paper can be used to study
the circulation ﬂuctuations for Markov chains. The empirical circulation Jc
t of cycle c is deﬁned as
Jc
t = 1
t Nc
t .
(4)
It is easy to see that the circulations deﬁned in (1) are the almost sure limits of the empirical circu-
lations. In this paper, we prove that the empirical circulations of a family of cycles c1, c2, · · · , cr
passing through a common state satisfy a large deviation principle with rate t and good rate function
Ic1,c2,··· ,cr. Moreover, we apply the generalized Haldane equalities to prove that the rate function
Ic1,c2,··· ,cr has the following highly non-obvious symmetry: if ck and cl are similar, then
Ic1,c2,··· ,cr(x1, · · · , xk, · · · , xl, · · · , xr)
= Ic1,c2,··· ,cr(x1, · · · , xl, · · · , xk, · · · , xr) −

log γck
γcl

(xk −xl),
(5)
where γck and γcl are the strengths of ck and cl, respectively (see Deﬁnition 13). In applications, we
are more concerned about the ﬂuctuations of net circulations, where the empirical net circulation Kc
t
of cycle c is deﬁned as
Kc
t = Jc
t −Jc−
t
.
(6)
In this paper, we prove that the empirical net circulations of cycles c1, c2, · · · , cr also satisfy a large
deviation principle with rate t and good rate function Ic1,c2,··· ,cr
K
which has the following symmetry:
Ic1,c2,··· ,cr
K
(x1, · · · , xk, · · · , xr) = Ic1,c2,··· ,cr(x1, · · · , −xk, · · · , xr) −

log γck
γck−

xk.
(7)
This is actually the Gallavotti-Cohen-type ﬂuctuation theorem of net circulations. During the proof
of the above results, we also obtain other types of ﬂuctuation theorems as by-products, including
the transient ﬂuctuation theorem, the integral ﬂuctuation theorem, and the Lebowitz-Spohn-type
ﬂuctuation theorem. All these ﬂuctuation theorems, together with the generalized Haldane equalities,
characterize the symmetries of a family of similar cycles for Markov chains from different aspects.
At the end of this paper, we discuss the applications of our work in nonequilibrium statistical
physics and biochemistry. This shows that our work would have a board application prospect in
natural sciences.
3


## Page 4


2
Rigorous deﬁnitions of cycles and their forming times
In this section, we shall give the rigorous deﬁnitions of cycles and their forming times for
discrete-time and continuous-time Markov chains.
We ﬁrst give the deﬁnitions of cycles. Let X = (Xt)t≥0 be a time-homogeneous discrete-time
or continuous-time Markov chain with denumerable state space S deﬁned on some probability space
(Ω, F, P).
Deﬁnition 1. Let i1 →i2 →· · · →is →i1 and j1 →j2 →· · · →jr →j1 be two directed circuits
on complete graph with vertex set S. Then the two directed circuits are called equivalent if r = s
and if there exists 1 ≤k ≤s, such that ik+1 = j1, ik+2 = j2, · · · , ik+s = js, where we have used
the convention that is+l = il for each integer l.
According to the above deﬁnition, two directed circuits are called equivalent if one can be trans-
formed into the other by a cyclic permutation. For example, the three directed circuits, 1 →2 →
3 →1, 2 →3 →1 →2, and 3 →1 →2 →3, are equivalent.
Deﬁnition 2. Let i1, i2, · · · , is be distinct states in S. Then the equivalence class of the directed
circuit i1 →i2 →· · · →is →i1 under the equivalence relation described in Deﬁnition 1 is called a
cycle and is denoted by (i1, i2, · · · , is).
According to the above deﬁnition, two cycles are the same if one can be transformed into the
other by a cyclic permutation. For example, the three cycles, (1, 2, 3), (2, 3, 1), and (3, 1, 2), repre-
sent the same cycle.
We next give the deﬁnition of the forming times of cycles for discrete-time Markov chains. Let
X = (Xn)n≥0 be an irreducible and recurrent discrete-time Markov chain with denumerable state
space S and transition probability matrix P = (pij)i,j∈S.
To this end, we must introduce the concept of the derived chain. It can be proved that with
probability one, the trajectory of X will generate an inﬁnite sequence of cycles [8]. If we discard the
cycles formed by X and keep track of the remaining states in the trajectory, then we obtain a new
Markov chain Y called the derived chain. We shall give the rigorous deﬁnitions of the derived chain
later, but the basic ideas should be clear from the following example.
Example 1. If the trajectory of the Markov chain X is {1, 2, 3, 2, 4, 5, 2, 3, 1, · · · }, then the corre-
sponding trajectory of the derived chain Y and the cycles formed are as follows:
n
0
1
2
3
4
5
6
7
8
Xn
1
2
3
2
4
5
2
3
1
Yn
[1]
[1,2]
[1,2,3]
[1,2]
[1,2,4]
[1,2,4,5]
[1,2]
[1,2,3]
[1]
cycles formed
(2,3)
(2,4,5)
(1,2,3)
In order to give the rigorous deﬁnitions of the derived chain, we introduce several notations. We
denote an ﬁnite sequence i1, i2, · · · , is of distinct states by [i1, i2, · · · , is] and denote the collection
of all ﬁnite sequences of distinct states by [S], that is,
[S] = {[i1, i2, · · · , is] : s ≥1, i1, · · · , is are distinct states in S}.
(8)
4


## Page 5


We also deﬁne a map {·, ·} from [S] × S into [S] by
{[i1, i2, · · · , is], i} =



[i1, i2, · · · , is, i],
if i /∈{i1, i2, · · · , is}
[i1, i2, · · · , ik],
if i = ik for some 1 ≤k ≤s.
(9)
Deﬁnition 3. The derived chain Y = (Yn)n≥0 of X is deﬁned as Y0 = [X0] and Yn = {Yn−1, Xn}
for each n ≥1.
It can be proved that the derived chain Y is a time-homogeneous Markov chain with denumer-
able state space [S] [8].
Deﬁnition 4. Let c = (i1, i2, · · · , is) be a cycle. For each ω ∈Ω, we say that the trajectory X(ω)
forms cycle c at time n if there exists 1 ≤k ≤s and distinct states j1, j2, · · · , jr /∈{i1, i2, · · · , is}
such that Yn−1(ω) = [j1, j2, · · · , jr, ik, ik+1, · · · , ik+s−1] and Yn(ω) = [j1, j2, · · · , jr, ik], where
we have used the convention that is+l = il for each integer l.
Deﬁnition 5. Let c be a cycle. Then the forming time T c of cycle c by X is deﬁned as
T c(ω) = inf{n ≥1 : the trajectory X(ω) forms cycle c at time n}.
(10)
For each m ≥1, the m-th forming time T c
m of cycle c can be deﬁned inductively as the forming time
of cycle c by the Markov chain (XT c
m−1+n)n≥0, where T c
0 is understood as 0.
Lemma 1. Let c = (i1, i2, · · · , is) be a cycle.
(i) If pi1i2pi2i3 · · · pisi1 > 0, then T c
m < ∞almost surely for each m ≥1.
(ii) If pi1i2pi2i3 · · · pisi1 = 0, then T c
m = ∞almost surely for each m ≥1.
Proof. It is easy to see that (ii) holds. We next prove (i). To this end, we only need to prove that
T c < ∞almost surely. Let H = {i1, i2, · · · , is}. Let τ0 = inf{n ≥0 : Xn ∈H} and let
τm = inf{n > τm−1 : Xn = Xτ0} for each m ≥1. Since X is recurrent, it is easy to see that
τm < ∞almost surely for each m. Let
N(ω) = inf{m ≥1 : the trajectory X(ω) forms cycle c at time τm}.
(11)
We now ﬁx some 1 ≤k ≤s. By the strong Markov property, conditional on {Xτ0 = ik}, N follows
a geometric distribution with parameter pk ≥pi1i2pi2i3 · · · pisi1 > 0. This shows that N < ∞almost
surely conditional on {Xτ0 = ik}. By the arbitrariness of k, we obtain that N < ∞almost surely.
This implies that for almost every ω, the trajectory X(ω) will form cycle c in ﬁnite time, that is,
T c < ∞almost surely.
We ﬁnally give the deﬁnition of the forming times of cycles for continuous-time Markov chains.
Let X = (Xt)t≥0 be an irreducible and recurrent continuous-time Markov chain with denumerable
state space S and transition rate matrix Q = (qij)i,j∈S. Let (Jn)n≥0 be the jump times of X with the
convention of J0 = 0. For each n ≥0, let ¯Xn = XJn. Then ¯X = ( ¯Xn)n≥0 is the embedded chain
of X.
5


## Page 6


Deﬁnition 6. Let c be a cycle. Let ¯T c be the forming time of cycle c by the embedded chain ¯X.
Then the forming time T c of cycle c by X is deﬁned as
T c = J ¯T c.
(12)
For each m ≥1, let ¯T c
m be the m-th forming time of cycle c by the embedded chain ¯X. Then the
m-th forming time T c
m of cycle c by X is deﬁned as
T c
m = J ¯T c
m.
(13)
Lemma 2. Let c = (i1, i2, · · · , is) be a cycle.
(i) If qi1i2qi2i3 · · · qisi1 > 0, then T c
m < ∞almost surely for each m ≥1.
(ii) If qi1i2qi2i3 · · · qisi1 = 0, then T c
m = ∞almost surely for each m ≥1.
Proof. It is easy to see that (ii) holds. We next prove (i). Since X is irreducible and recurrent, the
embedded chain ¯X is also irreducible and recurrent. By Lemma 1, we see that ¯T c
m < ∞almost
surely. Since X is irreducible and recurrent, it is non-explosive, which means that Jn < ∞almost
surely for each n. The above two facts show that T c
m = J ¯T c
m < ∞almost surely.
We have deﬁned the forming time of a particular cycle. We shall now deﬁne the forming time
of two or more cycles.
Deﬁnition 7. Let c1, c2, · · · , cr be a family of cycles and let T c1, T c2, · · · , T cr be their forming
times. Then the forming time T of c1, c2, · · · , cr by X is deﬁned as
T = min{T c1, T c2, · · · , T cr}.
(14)
For each m ≥1, the m-th forming time Tm of c1, c2, · · · , cr can be deﬁned inductively as the
forming time of c1, c2, · · · , cr by the Markov chain (XTm−1+t)t≥0, where T0 is understood as 0.
3
Generalized Haldane equality for discrete-time Markov chains
In this section, we shall state and prove the generalized Haldane equality for discrete-time
Markov chains. Let X = (Xn)n≥0 be an irreducible and recurrent discrete-time Markov chain
with denumerable state space S and transition probability matrix P = (pij)i,j∈S.
Before we state the generalized Haldane equality, we give the following deﬁnitions.
Deﬁnition 8. Let i be a state and let c = (i1, i2, · · · , is) be a cycle. Then we say that cycle c passes
through state i if i ∈{i1, i2, · · · , is}.
Deﬁnition 9. Let c1 = (i1, i2, · · · , is) and c2 = (j1, j2, · · · , jr) be two cycles. Then c1 and c2 are
called similar if s = r and {i1, i2, · · · , is} = {j1, j2, · · · , jr}.
According to the above two deﬁnitions, two cycles are similar if they pass through the same
set of states. It is easy to see that similarity is an equivalence relation on the set of all cycles.
For example, the six cycles, c1 = (1, 2, 3, 4), c2 = (1, 2, 4, 3), c3 = (1, 3, 2, 4), c4 = (1, 3, 4, 2),
c5 = (1, 4, 2, 3), and c6 = (1, 4, 3, 2), are similar.
We next give the deﬁnition of the strengths of cycles for discrete-time Markov chains.
6


## Page 7


Deﬁnition 10. Let c = (i1, i2, · · · , is) be a cycle. Then the strength γc of cycle c is deﬁned as
γc = pi1i2pi2i3 · · · pisi1.
(15)
In the following discussion, the forming time of cycle c is always denoted by T c and the strength
of cycle c is always denoted by γc without further explanation.
The generalized Haldane equality, which characterizes the symmetry of the forming times of a
family of similar cycles, is stated in the following theorem.
Theorem 1. Let c1, c2, · · · , cr be a family of similar cycles. Let T = min{T c1, T c2, · · · , T cr}.
Then
(i) for each n ≥1 and any 1 ≤k, l ≤r,
P(T ck = n, T = T ck)
P(T cl = n, T = T cl) = P(T = T ck)
P(T = T cl) = γck
γcl ;
(16)
(ii) for each n ≥1,
P(T c1 = n|T = T c1) = P(T c2 = n|T = T c2) = · · · = P(T cr = n|T = T cr).
(17)
Remark 1. The above theorem, which seems a bit counter-intuitive at ﬁrst sight, shows that al-
though the distributions of the forming times of a family of similar cycles may not be the same, their
distributions, conditional on the corresponding cycle is formed earlier than any other similar cycles,
are the same. This is the ﬁrst aspect of the generalized Haldane equality.
Remark 2. If both the numerator and denominator in (16) are 0, then (16) is understood to hold
trivially. In addition, if P(T = T ck) = 0 for some k, then (17) is understood to hold trivially.
In order to prove the generalized Haldane equality, we need to establish some deep properties
of taboo probabilities. Let us ﬁrst recall the deﬁnition of taboo probabilities, also called transition
probabilities with a taboo set [24].
Deﬁnition 11. Let i, j be two states and H be a subset of S. Then the n-step transition probability
from state i to state j with taboo set H is deﬁned as
pH
ij (n) = Pi(Xn = j, X1, · · · , Xn−1 /∈H).
(18)
If the taboo set is the union of a set H and a ﬁnite number of states k1, · · · , ks, then we shall denote
the taboo probability by pH,k1,··· ,ks
ij
(n).
The next four lemma give some deep properties of taboo properties.
Lemma 3. Let H be a subset of S and let k /∈H. Then for each n ≥0 and any two states i, j,
pH
ij (n) = pH,k
ij (n) +
n−1
X
m=1
pH
ik(m)pH,k
kj (n −m).
(19)
7


## Page 8


Proof. When n = 0 or n = 1, it is easy to check that the theorem holds. We next prove the theorem
for n ≥2. Note that
pH
ij (n) = pH,k
ij (n) + Pi(Xn = j, X1, · · · , Xn−1 /∈H, k ∈{X1, · · · , Xn−1}).
(20)
Then by the Markov property, we obtain that
Pi(Xn = j, X1, · · · , Xn−1 /∈H, k ∈{X1, · · · , Xn−1})
=
n−1
X
m=1
Pi(Xn = j, X1, · · · , Xn−1 /∈H, Xm = k, Xm+1, · · · , Xn−1 ̸= k)
=
n−1
X
m=1
Pi(Xm = k, X1, · · · , Xm−1 /∈H)Pk(Xn−m = j, X1, · · · , Xn−m−1 /∈H ∪{k})
=
n−1
X
m=1
pH
ik(m)pH,k
kj (n −m).
This completes the proof of this lemma.
Lemma 4. Let H be a subset of S. Let i, j /∈H and i ̸= j. Then for each n ≥0,
n
X
m=0
pH
ii (m)pH,i
jj (n −m) =
n
X
m=0
pH
jj(m)pH,j
ii (n −m).
(21)
Proof. By Lemma 3, we have
n
X
m=0
pH
ii (m)pH,i
jj (n −m)
=
n
X
m=0
pH
ii (m)pH
jj(n −m) −
n
X
m=0
pH
ii (m)
n−m−1
X
l=1
pH
ji(l)pH,i
ij (n −m −l)
=
n
X
m=0
pH
ii (m)pH
jj(n −m) −
n
X
m=0
pH
ii (m)
n−m
X
l=0
pH
ji(l)pH,i
ij (n −m −l)
=
n
X
m=0
pH
ii (m)pH
jj(n −m) −
n
X
l=0
pH
ji(l)
n−l
X
m=0
pH
ii (m)pH,i
ij (n −m −l).
(22)
Using Lemma 3 again, we have
n−l
X
m=0
pH
ii (m)pH,i
ij (n −m −l) = pH,i
ij (n −l) +
n−l−1
X
m=1
pH
ii (m)pH,i
ij (n −m −l)
= pH,i
ij (n −l) + pH
ij (n −l) −pH,i
ij (n −l) = pH
ij (n −l).
(23)
Thus we obtain that
n
X
m=0
pH
ii (m)pH,i
jj (n −m) =
n
X
m=0
pH
ii (m)pH
jj(n −m) −
n
X
l=0
pH
ji(l)pH
ij (n −l).
(24)
Commuting i and j in the above equation, we ﬁnally obtain that
n
X
m=0
pH
jj(m)pH,j
ii (n −m) =
n
X
m=0
pH
jj(m)pH
ii (n −m) −
n
X
l=0
pH
ij (l)pH
ji(n −l)
=
n
X
m=0
pH
ii (m)pH
jj(n −m) −
n
X
l=0
pH
ji(l)pH
ij (n −l) =
n
X
m=0
pH
ii (m)pH,i
jj (n −m),
(25)
8


## Page 9


which gives the desired result.
Lemma 5. Let H be a subset of S. For any ﬁnite sequence i1, i2, · · · , is of distinct states, let
GH
n (i1, i2, · · · , is) =
X
n1+n2+···+ns=n
pH
i1i1(n1)pH,i1
i2i2 (n2) · · · pH,i1,··· ,is−1
isis
(ns).
(26)
Then for each n ≥0, GH
n (i1, i2, · · · , is) is invariant under any permutation of i1, · · · , is.
Proof. Since any permutation can be decomposed into the product of some transpositions of adjacent
elements, we only need to prove that GH
n (i1, i2, · · · , is) is invariant if we exchange two adjacent
elements, ik and ik+1, and keep all other elements ﬁxed. By Lemma 4, we obtain that
GH
n (i1, · · · , ik, ik+1, · · · , is)
=
X
n1+···+ns=n
pH
i1i1(n1) · · · pH,i1,··· ,ik−1
ikik
(nk)pH,i1,··· ,ik
ik+1ik+1 (nk+1) · · · pH,i1,··· ,is−1
isis
(ns)
=
n
X
m=0
X
n1+···+nk−1+nk+2+···+ns=n−m
pH
i1i1(n1) · · · pH,i1,··· ,ik−2
ik−1ik−1
(nk−1)
pH,i1,··· ,ik+1
ik+2ik+2
(nk+2) · · · pH,i1,··· ,is−1
isis
(ns)
X
nk+nk+1=m
pH,i1,··· ,ik−1
ikik
(nk)pH,i1,··· ,ik
ik+1ik+1 (nk+1)
=
n
X
m=0
X
n1+···+nk−1+nk+2+···+ns=n−m
pH
i1i1(n1) · · · pH,i1,··· ,ik−2
ik−1ik−1
(nk−1)
pH,i1,··· ,ik+1
ik+2ik+2
(nk+2) · · · pH,i1,··· ,is−1
isis
(ns)
X
nk+nk+1=m
pH,i1,··· ,ik−1
ik+1ik+1
(nk)pH,i1,··· ,ik−1,ik+1
ikik
(nk+1)
=
X
n1+···+ns=n
pH
i1i1(n1) · · · pH,i1,··· ,ik−2
ik−1ik−1
(nk−1)pH,i1,··· ,ik−1
ik+1ik+1
(nk)pH,i1,··· ,ik−1,ik+1
ikik
(nk+1)
pH,i1,··· ,ik+1
ik+2ik+2
(nk+2) · · · pH,i1,··· ,is−1
isis
(ns)
=
GH
n (i1, · · · , ik−1, ik+1, ik, ik+2, · · · , is).
This completes the proof of this lemma.
The following lemma will play a key role in the proof of the generalized Haldane equality.
Lemma 6. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Let T =
min{T c1, T c2, · · · , T cr}. Let ck = (i, ik
2, · · · , ik
s). Then for each n ≥1,
Pi(T ck = n, T = T ck) = F i
n(ik
2, · · · , ik
s)γck,
(27)
where F i
n(ik
2, · · · , ik
s), which is deﬁned in (29), is invariant under any permutation of ik
2, · · · , ik
s.
Proof. Note that the event {T ck = n, T = T ck} is equivalent to saying that X forms cycle ck at
time n and does not form cycles c1, c2, · · · , cr before time n. In order to make this event occur, the
Markov chain X must ﬁnish the following procedures.
First, X must take n1 steps to return from i to i without forming cycles c1, c2, · · · , cr, and then
jump from i to ik
2. Second, X must take n2 steps to return from ik
2 to ik
2 without entering i and without
forming cycles c1, c2, · · · , cr, and then jump from ik
2 to ik
3. Third, X must take n3 steps to return
9


## Page 10


from ik
3 to ik
3 without entering i, ik
2 and without forming cycles c1, c2, · · · , cr, and then jump from ik
3
to ik
4, and so on. Finally, X must take ns steps to return from ik
s to ik
s without entering i, ik
1, · · · , ik
s−1
and without forming cycles c1, c2, · · · , cr, and then jump from ik
s to i. Here, the steps n1, n2, · · · , ns
must satisfy (n1 + 1) + (n2 + 1) + · · · + (ns + 1) = n, that is, n1 + n2 + · · · + ns = n −s.
We make a crucial observation that if X does not enter i, it will never form any one of the cycles
c1, c2, · · · , cr since all these cycles pass through i. Let pc1,c2,··· ,cr
ii
(n1) denote the probability that X
takes n1 steps to return from i to i without forming cycles c1, c2, · · · , cr. According to the above
discussion, we obtain that
Pi(T ck = n, T = T ck)
=
X
n1+n2+···+ns=n−s
pc1,c2,··· ,cr
ii
(n1)piik
2pi
ik
2ik
2(n2)pik
2ik
3pi,ik
2
ik
3ik
3(n3)pik
3ik
4 · · · p
i,ik
1,··· ,ik
s−1
ik
sik
s
(ns)pik
si
=
" n−s
X
n1=0
pc1,c2,··· ,cr
ii
(n1)Gi
n−n1−s(ik
2, · · · , ik
s)
#
piik
2pik
2ik
3 · · · pik
si,
where
Gi
n−n1−s(ik
2, · · · , ik
s) =
X
n2+···+ns=n−n1−s
pi
ik
2ik
2(n2)pi,ik
2
ik
3ik
3(n3) · · · p
i,ik
1,··· ,ik
s−1
ik
sik
s
(ns).
(28)
By Lemma 5, Gi
n−n1−s(ik
2, · · · , ik
s) is invariant under any permutation of ik
2, · · · , ik
s. Let
F i
n(ik
2, · · · , ik
s) =
n−s
X
n1=0
pc1,c2,··· ,cr
ii
(n1)Gi
n−n1−s(ik
2, · · · , ik
s).
(29)
Then F i
n(ik
2, · · · , ik
s) is invariant under any permutation of ik
2, · · · , ik
s. This completes the proof of
this lemma.
Remark 3. The core idea in the above proof is to decompose the state transitions of each trajectory
in the event {T ck = n, T = T ck} into invalid transitions and valid transitions. During the invalid
transitions, X will walk around in circles without contributing to the forming of cycle ck. During
the valid transitions, however, X will jump along cycle ck. In this way, we can decompose the
probability Pi(T ck = n, T = T ck) into the product of an invalid part F i
n(ik
2, · · · , ik
s) and a valid
part γck. The invalid part is invariant under any permutation of ik
2, · · · , ik
s and the valid part is
independent of time n.
We are now in a position to prove the generalized Haldane equality.
Proof of Theorem 1. It is easy to see that (ii) is a direct corollary of (i). Thus we only need to
prove (i). Since c1, c2, · · · , cr are similar, they must pass through the same set of states, denoted by
H = {i1, i2, · · · , is}.
We ﬁrst prove (i) when X starts from a particular state i ∈H. Write ck = (i, ik
2, · · · , ik
s) and
cl = (i, il
2, · · · , il
s). By Lemma 6, we have
Pi(T ck = n, T = T ck) = F i
n(ik
2, · · · , ik
s)γck,
Pi(T cl = n, T = T cl) = F i
n(il
2, · · · , il
s)γcl,
(30)
10


## Page 11


where F i
n(ik
2, · · · , ik
s) is invariant under any permutation of ik
2, · · · , ik
s. Since ck and cl are similar,
ik
2, · · · , ik
s can be transformed into il
2, · · · , il
s by a permutation. This shows that
Pi(T ck = n, T = T ck)
Pi(T cl = n, T = T cl) = γck
γcl .
(31)
We next prove (i) when X starts from any initial distribution π = (πi)i∈S. Let τ = inf{n ≥0 :
Xn ∈H}. It is easy to see that
P(T ck = n, T = T ck)
=
n
X
m=0
P(T ck = n, T = T ck, τ = m)
=
P(T ck = n, T = T ck, τ = 0) +
n
X
m=1
P(T ck = n, T = T ck, τ = m)
=
X
i∈H
πiPi(T ck = n, T = T ck)
+
n
X
m=1
X
i/∈H
X
j∈H
πiPi(T ck = n, T = T ck, Xm = j, X1, · · · , Xm−1 /∈H).
By the Markov property, we have
Pi(T ck = n, T = T ck, Xm = j, X1, · · · , Xm−1 /∈H)
= Pi(Xm = j, X1, · · · , Xm−1 /∈H)Pj(T ck = n −m, T = T ck)
= pH
ij (m)Pj(T ck = n −m, T = T ck).
(32)
Thus we obtain that
P(T ck = n, T = T ck)
=
X
i∈H
πiPi(T ck = n, T = T ck)
+
n
X
m=1
X
i/∈H
X
j∈H
πipH
ij (m)Pj(T ck = n −m, T = T ck).
According to (31) and the above equation, we see that
P(T ck = n, T = T ck)
P(T cl = n, T = T cl) = γck
γcl .
(33)
Since the above equation holds for each n, we obtain the desired result.
The next corollary gives another aspect of the generalized Haldane equality.
Corollary 1. Let c1, c2, · · · , cr be a family of similar cycles. Let T = min{T c1, T c2, · · · , T cr}.
Then for each n ≥0 and each 1 ≤k ≤r,
P(T = n, T = T ck) = P(T = n)P(T = T ck).
(34)
Proof. By Theorem 1, the probability P(T = n|T = T ck) is the same for each k. This implies that
for each k,
P(T = n|T = T ck) = P(T = n).
(35)
11


## Page 12


Thus we obtain that
P(T = n, T = T ck) = P(T = n|T = T ck)P(T = T ck) = P(T = n)P(T = T ck),
(36)
which gives the desired result.
Remark 4. The notations are the same as in Corollary 1. Let ξ be a random variable deﬁned by
ξ =



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



c1,
if the trejectory of X forms cycle c1 at time T,
c2,
if the trejectory of X forms cycle c2 at time T,
· · · ,
cr,
if the trejectory of X forms cycle cr at time T.
(37)
Then Corollary 1 shows that T and ξ are independent. This suggests that the forming time of two or
more similar cycles is independent of which one of these cycles is formed. This is another important
aspect of the generalized Haldane equality.
In applications, we are more concerned about the symmetry of a cycle and its reversed cycle.
Thus we give the following deﬁnition.
Deﬁnition 12. Let c = (i1, i2, · · · , is) be a cycle. Then the reversed cycle c−of cycle c is deﬁned
as c−= (i1, is, · · · , i2). The cycles c and c−are called conjugate.
For example, the two cycles c = (1, 2, 3) and c−= (1, 3, 2) are conjugate. It is easy to see
that conjugate cycles must be similar. Now that the generalized Haldane equality holds for similar
cycles, it also holds for conjugate cycles. Thus we obtain the following corollary.
Corollary 2. Let c = (i1, i2, · · · , is) be a cycle. Then
(i) for each n ≥0,
P(T c = n, T c < T c−)
P(T c−= n, T c−< T c) = P(T c < T c−)
P(T c−< T c) = pi1i2pi2i3 · · · pisi1
pi1ispisis−1 · · · pi2i1
;
(38)
(ii) for each n ≥0,
P(T c = n|T c < T c−) = P(T c−= n|T c−< T c);
(39)
(iii) for each n ≥0,
P(T c ∧T c−= n, T c < T c−) = P(T c ∧T c−= n)P(T c < T c−).
(40)
Proof. This corollary follows directly from Theorem 1 and Corollary 1.
Remark 5. The above corollary generalizes the so-called generalized Haldane equality (see (2) in
Section 1) found by biophysicists in three-state Markov chains [11, 15, 16].
12


## Page 13


4
Generalizations of the generalized Haldane equality
We have seen that the most important intermediate step in the proof of the generalized Haldane
equality is Lemma 6, in which we decompose the probability Pi(T ck = n, T = T ck) into an invalid
part and a valid part. However, we notice that the conditions stated in Lemma 6 are much weaker
than those stated in Theorem 1. This suggests that the generalized Haldane equality can be further
generalized, as stated in the following theorem.
Theorem 2. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Let T =
min{T c1, T c2, · · · , T cr}. Assume that ck and cl are similar for some two indices 1 ≤k, l ≤r. Then
(i) for each n ≥1,
Pi(T ck = n, T = T ck)
Pi(T cl = n, T = T cl) = Pi(T = T ck)
Pi(T = T cl) = γck
γcl ;
(41)
(ii) for each n ≥1,
Pi(T ck = n|T = T ck) = Pi(T cl = n|T = T cl).
(42)
Proof. It is easy to see that (ii) is a direct corollary of (i). Thus we only need to prove (i). Write
ck = (i, ik
2, · · · , ik
s) and cl = (i, il
2, · · · , il
s). By Lemma 6, we have
Pi(T ck = n, T = T ck) = F i
n(ik
2, · · · , ik
s)γck,
Pi(T cl = n, T = T cl) = F i
n(il
2, · · · , il
s)γcl,
(43)
where F i
n(ik
2, · · · , ik
s) is invariant under any permutation of ik
2, · · · , ik
s. Since ck and cl are similar,
ik
2, · · · , ik
s can be transformed into il
2, · · · , il
s by a permutation. This shows that
Pi(T ck = n, T = T ck)
Pi(T cl = n, T = T cl) = γck
γcl .
(44)
Since the above equation holds for each n, we obtain the desired result.
Remark 6. There are two crucial differences between Theorem 1 and Theorem 2. The ﬁrst differ-
ence is that in Theorem 1, we require that the cycles c1, c2, · · · , cr are similar, while in Theorem 2,
we only require that the cycles c1, c2, · · · , cr pass through a common state. The second difference
is that Theorem 1 holds for Markov chains starting from any initial distributions, while Theorem 2
only holds for Markov chains starting from a particular state.
Now that the above theorem holds for similar cycles, it also holds for conjugate cycles. Thus we
obtain the following corollary.
Corollary 3. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Let T =
min{T c1, T c1−, · · · , T cr, T cr−}. Then
(i) for each n ≥1 and each 1 ≤k ≤r,
Pi(T ck = n, T = T ck)
Pi(T ck−= n, T = T ck−) = Pi(T = T ck)
Pi(T = T ck−) = γck
γck−;
(45)
(ii) for each n ≥1 and each 1 ≤k ≤r,
Pi(T ck = n|T = T ck) = Pi(T ck−= n|T = T ck−).
(46)
13


## Page 14


Proof. This corollary follows directly from Theorem 2.
Remark 7. We have seen that the generalized Haldane equality (Theorem 1) has many variations
which are closely related. These results, which include Theorems 1-2 and Corollaries 1-3, will be
collectively referred to as the generalized Haldane “equalities” in the following discussion.
5
Generalized Haldane equalities for continuous-time Markov chains
In this section, we shall state and prove the generalized Haldane equalities for continuous-time
Markov chains. Let X = (Xt)t≥0 be an irreducible and recurrent continuous-time Markov chain
with denumerable state space S and transition rate matrix Q = (qij)i,j∈S.
Before we state the generalized Haldane equality, we give the deﬁnition of the strengths of cycles
for continuous-time Markov chains.
Deﬁnition 13. Let c = (i1, i2, · · · , is) be a cycle. Then the strength γc of cycle c is deﬁned as
γc = qi1i2qi2i3 · · · qisi1.
(47)
The generalized Haldane equality, which characterizes the symmetry of the forming times of a
family of similar cycles, is stated in the following theorem.
Theorem 3. Let c1, c2, · · · , cr be a family of similar cycles. Let T = min{T c1, T c2, · · · , T cr}.
Then
(i) for each t > 0 and any 1 ≤k, l ≤r,
P(T ck ≤t, T = T ck)
P(T cl ≤t, T = T cl) = P(T = T ck)
P(T = T cl) = γck
γcl ;
(48)
(ii) for each t > 0,
P(T c1 ≤t|T = T c1) = P(T c2 ≤t|T = T c2) = · · · = P(T cr ≤t|T = T cr).
(49)
Proof. It is easy to see that (ii) is a direct corollary of (i). Thus we only need to prove (i). Let t > 0
be a ﬁxed time. For each m ≥1, let
Y m
n = Xnt/m.
(50)
Then Y m = (Y m
n )n≥0 is an irreducible and recurrent discrete-time Markov chain with transition
probability matrix Pm = (pij(t/m))i,j∈S, where pij(t/m) = Pi(Xt/m = j). Let T m,c be the
forming time of cycle c by Y m. Let T m = min{T m,c1, T m,c2, · · · , T m,cr}.
Since X is irreducible and recurrent, it is non-explosive, which implies that X can only jump
ﬁnite times before time t. Thus when m is sufﬁciently large, t/m is less than any of the waiting
times of X before time t. This means that the occurrence of the event {T ck ≤t, T = T ck} implies
the occurrence of the event {T m,ck ≤m, T m = T m,ck} when m is sufﬁciently large. Thus we
obtain that
{T ck ≤t, T = T ck} ⊂
∞
[
N=1
∞
\
m=N
{T m,ck ≤m, T m = T m,ck}.
(51)
14


## Page 15


Similarly, it is easy to see that the occurrence of the event {T ck > t} implies the occurrence of the
event {T m,ck > m} when m is sufﬁciently large and the occurrence of the event {T < T ck ≤t}
implies the occurrence of the event {T m < T m,ck ≤m} when m is sufﬁciently large. Thus we
obtain that
{T ck ≤t, T = T ck}c = {T ck > t} ∪{T < T ck ≤t}
⊂
 ∞
[
N=1
∞
\
m=N
{T m,ck > m}
! [  ∞
[
N=1
∞
\
m=N
{T m < T m,ck ≤m}
!
⊂
∞
[
N=1
∞
\
m=N
{T m,ck > m} ∪{T m < T m,ck ≤m}
=
∞
[
N=1
∞
\
m=N
{T m,ck ≤m, T m = T m,ck}c.
(52)
This shows that
∞
\
N=1
∞
[
m=N
{T m,ck ≤m, T m = T m,ck} ⊂{T ck ≤t, T = T ck}.
(53)
By (51) and (53), we have
{T ck ≤t, T = T ck} = lim
m→∞{T m,ck ≤m, T m = T m,ck}.
(54)
By the dominated convergence theorem, we obtain that
P(T ck ≤t, T = T ck) = lim
m→∞P(T m,ck ≤m, T m = T m,ck).
(55)
Write ck = (ik
1, ik
2, · · · , ik
s) and cl = (il
1, il
2, · · · , il
s). By Theorem 1, we have
P(T ck ≤t, T = T ck)
P(T cl ≤t, T = T cl) = lim
m→∞
P(T m,ck ≤m, T m = T m,ck)
P(T m,cl ≤m, T m = T m,cl)
= lim
m→∞
pik
1ik
2(t/m)pik
2ik
3(t/m) · · · pik
sik
1(t/m)
pil
1il
2(t/m)pil
2il
3(t/m) · · · pil
sil
1(t/m) = qik
1ik
2qik
2ik
3 · · · qik
sik
1
qil
1il
2qil
2il
3 · · · qil
sil
1
= γck
γcl .
(56)
Since the above equation holds for each t, we obtain the desired result.
Using the techniques in the proof of Theorem 3, we can obtain the following results parallel to
those for discrete-time Markov chains. The proofs of the following results are all omitted.
Corollary 4. Let c1, c2, · · · , cr be a family of similar cycles. Let T = min{T c1, T c2, · · · , T cr}.
Then for each t > 0 and each 1 ≤k ≤r,
P(T ≤t, T = T ck) = P(T ≤t)P(T = T ck).
(57)
Corollary 5. Let c = (i1, i2, · · · , is) be a cycle. Then
(i) for each t > 0,
P(T c ≤t, T c < T c−)
P(T c−≤t, T c−< T c) = P(T c < T c−)
P(T c−< T c) = qi1i2qi2i3 · · · qisi1
qi1isqisis−1 · · · qi2i1
;
(58)
15


## Page 16


(ii) for each t > 0,
P(T c ≤t|T c < T c−) = P(T c−≤t|T c−< T c);
(59)
(iii) for each t > 0,
P(T c ∧T c−≤t, T c < T c−) = P(T c ∧T c−≤t)P(T c < T c−).
(60)
Theorem 4. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Let T =
min{T c1, T c2, · · · , T cr}. Assume that ck and cl are similar for some two indices 1 ≤k, l ≤r. Then
(i) for each t > 0,
Pi(T ck ≤t, T = T ck)
Pi(T cl ≤t, T = T cl) = Pi(T = T ck)
Pi(T = T cl) = γck
γcl ;
(61)
(ii) for each t > 0,
Pi(T ck ≤t|T = T ck) = Pi(T cl ≤t|T = T cl).
(62)
Corollary 6. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Let T =
min{T c1, T c1−, · · · , T cr, T cr−}. Then
(i) for each t > 0 and each 1 ≤k ≤r,
Pi(T ck ≤t, T = T ck)
Pi(T ck−≤t, T = T ck−) = Pi(T = T ck)
Pi(T = T ck−) = γck
γck−;
(63)
(ii) for each t > 0 and each 1 ≤k ≤r,
Pi(T ck ≤t|T = T ck) = Pi(T ck−≤t|T = T ck−).
(64)
6
Large deviations and ﬂuctuations of empirical circulations
The generalized Haldane equalities established in this paper have wide applications. One of
the most important applications of the generalized Haldane equalities is to study the circulation
ﬂuctuations for Markov chains. In this section, we shall prove that the empirical circulations of a
family of cycles passing through a common state satisfy a large deviation principle with a good rate
function. Particularly, we shall use the generalized Haldane equalities to prove that the rate function
has a highly non-obvious symmetry, which is closely related to the Gallavotti-Cohen-type ﬂuctuation
theorem in nonequilibrium statistical physics.
6.1
Preliminaries
In order to establish the large deviations of empirical circulations, we need some results about the
large deviations for Markov renewal processes. To avoid misunderstanding, we give the following
deﬁnitions.
Deﬁnition 14. Let (µt)t>0 be a family of probability measures on a Polish space E. Then we say
that (µt)t>0 satisﬁes a large deviation principle with rate t and good rate function I : E →[0, ∞] if
(i) for each α ≥0, the level set {x ∈E : I(x) ≤α} is compact in E;
(ii) for each closed set F in E,
lim sup
t→∞
1
t log µt(F) ≤−inf
x∈F I(x);
(65)
16


## Page 17


(iii) for each open set U in E,
lim inf
t→∞
1
t log µt(U) ≥−inf
x∈U I(x).
(66)
Deﬁnition 15. Let ξ = (ξn)n≥0 be an irreducible discrete-time Markov chain with ﬁnite state space
E. Assume that each x ∈E is associated with a Borel probability measure φx on (0, ∞). Let
(τn)n≥1 be a sequence of positive and ﬁnite random variables such that conditional on (ξn)n≥0, the
random variables (τn)n≥1 are independent and have the distribution
P(τn ∈·|(ξn)n≥0) = φξn−1(·).
(67)
Then (ξn, τn+1)n≥0 is called a Markov renewal process.
The following lemma, which is due to Mariani and Zambotti [25], shows that the empirical ﬂow
of Markov renewal processes satisﬁes a large deviation principle with a good rate function.
Lemma 7. Let (ξn, τn+1)n≥0 be a Markov renewal process. Let Tn = Pn
k=1 τk be the n-th jump
time of the Markov renewal process. Let Nt = inf{n ≥0 : Tn+1 > t} be the number of jumps of
the Markov renewal process up to time t. Let Qt ∈C(E × E, [0, ∞)) be the empirical ﬂow of the
Markov renewal process up to time t deﬁned as
Qt(x, y) = 1
t
Nt
X
n=0
I{ξn=x,ξn+1=y}.
(68)
Then the law of Qt satisﬁes a large deviation principle with rate t and good rate function I : C(E ×
E, [0, ∞)) →[0, ∞]. Moreover, the rate function I is convex.
Proof. The proof of this theorem can be found in [25].
6.2
Large deviations of empirical circulations
Let X = (Xt)t≥0 be an irreducible and recurrent continuous-time Markov chain with denu-
merable state space S and transition rate matrix Q = (qij). In this paper, we only consider the
large deviations of the empirical circulations for continuous-time Markov chains. Using similar but
simpler techniques, we can obtain parallel results for discrete-time Markov chains.
Deﬁnition 16. Let T c
n be the n-th forming time of cycle c by X (see Deﬁnition 6). Let Nc
t =
inf{n ≥0 : T c
n+1 > t} be the number of cycle c formed by X up to time t. Then the empirical
circulation Jc
t of cycle c up to time t is deﬁned as
Jc
t = 1
t Nc
t
(69)
and the empirical net circulation Kc
t of cycle c up to time t is deﬁned as
Kc
t = Jc
t −Jc−
t
= 1
t (Nc
t −Nc−
t
).
(70)
17


## Page 18


The Qians’ [4] proved that the empirical circulation Jc
t of each cycle c converges almost surely
to a nonnegative real number Jc, which is deﬁned as the circulation of cycle c. The large deviations
of the empirical circulations are stated in the following theorem.
Theorem 5. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Then under
Pi, the law of (Jc1
t , Jc2
t , · · · , Jcr
t ) satisﬁes a large deviation principle with rate t and good rate
function Ic1,c2,··· ,cr : Rr →[0, ∞].
Remark 8. In general, it is very difﬁcult to obtain an explicit and computable expression of the
rate function Ic1,c2,··· ,cr. However, we can use the generalized Haldane equalities established in this
paper to prove that the rate function Ic1,c2,··· ,cr has a highly non-obvious symmetry, whose speciﬁc
form is given in Theorem 6.
If we only focus on the forming of cycles, instead of the speciﬁc state transitions, then the
corresponding process is a Markov renewal process, as stated in the following lemma.
Lemma 8. Let c1, c2, · · · , cr be a family of cycles passing through a common state i and assume
that γck > 0 for some 1 ≤k ≤r. Let Tn be the n-th forming time of c1, c2, · · · , cr by X (see
Deﬁnition 7). Let τn = Tn −Tn−1. Let ξn be a random variable deﬁned as
ξn =



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



c1,
if the trajetory of X forms cycle c1 at time Tn,
c2,
if the trajetory of X forms cycle c2 at time Tn,
· · · ,
cr,
if the trajetory of X forms cycle cr at time Tn.
(71)
Then under Pi, (ξn, τn)n≥1 is a Markov renewal process.
Proof. Since X starts from i and c1, c2, · · · , cr pass through i, it is easy to see that XTn = i for each
n. By the strong Markov property, the random sequence (ξn, τn)n≥1 is independent and identically
distributed. This shows that (ξn)n≥1 is a Markov chain with state space E = {c1, c2, · · · , cr}. Note
that γck > 0 for some k. By Lemma 2, we have Tn ≤T ck
n
< ∞almost surely for each n. This
shows that (τn)n≥1 is a sequence of positive and ﬁnite random variables.
Since (ξn, τn)n≥1 is independent and identically distributed, for any bounded measurable func-
tion f1, · · · , fn on (0, ∞), it is easy to see that
Ei(f1(τ1) · · · fn(τn)|(ξn)n≥1) = Ei(f1(τ1)|(ξn)n≥1) · · · Ei(fn(τn)|(ξn)n≥1).
(72)
Moreover, for any Borel set A in (0, ∞),
Pi(τn ∈A|(ξn)n≥1) = Pi(τn ∈A|ξn) = Pi(τ1 ∈A|ξ1 = x)|x=ξn = φξn(A).
(73)
where φx(A) = Pi(τ1 ∈A|ξ1 = x). The above two equations show each x ∈E is associated with a
Borel probability measure φx on (0, ∞) and conditional on (ξn)n≥1, the random variables (τn)n≥1
are independent and have the distribution Pi(τn ∈·|(ξn)n≥1) = φξn(·). This shows that (ξn, τn)n≥1
is a Markov renewal process.
18


## Page 19


We are now in a position to establish the large deviations of the empirical circulations.
Proof of Theorem 5. We only need to prove this theorem when γck > 0 for some k. Otherwise, we
have γck = 0 for each k. By Lemma 2, we see that T ck = ∞almost surely for each k. This shows
that Jck
t
= 0 almost surely for each k. In this case, the result of this theorem holds trivially.
We next assume that γck > 0 for some k. By Lemma 8, we see that (ξn, τn)n≥1 is a Markov
renewal process with state space E = {c1, c2, · · · , cr}. Let Nt = inf{n ≥0 : Tn+1 > t} be the
number of jumps of the Markov renewal process up to time t. Let Qt ∈C(E × E, [0, ∞)) be the
empirical ﬂow of the Markov renewal process up to time t deﬁned as
Qt(x, y) = 1
t
Nt
X
n=1
I{ξn=x,ξn+1=y}.
(74)
Note that for each k,
Jck
t
= 1
t Nck
t
= 1
t
Nt
X
n=1
I{ξn=ck} =
X
y∈E
Qt(ck, y).
(75)
We deﬁne a continuous map F : C(E × E, [0, ∞)) →Rr as
F(Q) =

X
y∈E
Q(c1, y), · · · ,
X
y∈E
Q(cr, y)

.
(76)
Thus we have
(Jc1
t , · · · , Jcr
t ) = F(Qt).
(77)
By Lemma 7, the law of Qt satisﬁes a large deviation principle with rate t and good rate function I :
C(E × E, [0, ∞)) →[0, ∞]. Using the contraction principle, we see that the law of (Jc1
t , · · · , Jcr
t )
satisﬁes a large deviation principle with rate t and good rate function Ic1,··· ,cr : Rr →[0, ∞] which
can be represented as
Ic1,··· ,cr(x) =
inf
Q∈F −1(x) I(Q).
(78)
This completes the proof of this theorem.
6.3
Circulation ﬂuctuations for Markov chains
We have proved that the empirical circulations of a family of cycles c1, c2, · · · , cr passing
through a common state satisfy a large deviation principle with rate t and good rate function Ic1,c2,··· ,cr.
In this section, we shall study the properties of the rate function Ic1,c2,··· ,cr. In fact, we can prove
that the rate function Ic1,c2,··· ,cr has a highly non-obvious symmetry, whose speciﬁc form is given in
the next theorem.
Theorem 6. The notations are the same as in Theorem 5. Assume that ck and cl are similar for some
two indices 1 ≤k, l ≤r. Then the rate function Ic1,c2,··· ,cr has the following symmetry:
Ic1,c2,··· ,cr(x1, · · · , xk, · · · , xl, · · · , xr)
= Ic1,c2,··· ,cr(x1, · · · , xl, · · · , xk, · · · , xr) −

log γck
γcl

(xk −xl).
(79)
19


## Page 20


In order to prove the above theorem, we need several lemmas.
Lemma 9. The rate function Ic1,c2··· ,cr is convex.
Proof. Note that the function F deﬁned in (76) is a linear function. This fact, together with (78),
shows that for any 0 < λ < 1 and any x, y ∈Rr,
Ic1,··· ,cr(λx + (1 −λ)y) =
inf
Q∈F −1(λx+(1−λ)y) I(Q)
≤
inf
Q∈λF −1(x)+(1−λ)F −1(y) I(Q) =
inf
Q∈F −1(x),R∈F −1(y) I(λQ + (1 −λ)R).
(80)
By Lemma 7, the rate function I is convex. Thus we obtain that
Ic1,··· ,cr(λx + (1 −λ)y) ≤
inf
Q∈F −1(x),R∈F −1(y) λI(Q) + (1 −λ)I(R)
= λ
inf
Q∈F −1(x) I(Q) + (1 −λ)
inf
R∈F −1(y) I(R) = λIc1,··· ,cr(x) + (1 −λ)Ic1,··· ,cr(y).
(81)
This completes the proof of this lemma.
The following lemma follows directly from the generalized Haldane equalities.
Lemma 10. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Assume that
ck and cl are similar for some two indices 1 ≤k, l ≤r. Let T = min{T c1, T c2, · · · , T cr}. Then for
each t > 0,
Pi(T ≤t, T = T ck) = Pi(T ≤t, T = T ck ∧T cl)Pi(T ck < T cl).
(82)
Proof. By Theorem 4(i), we have
Pi(T ≤t, T = T ck)
Pi(T ≤t, T = T cl) = Pi(T ≤t, T = T ck ∧T cl, T ck < T cl)
Pi(T ≤t, T = T ck ∧T cl, T cl < T ck) = γck
γcl .
(83)
Using Theorem 4(i) again, we have
Pi(T ck ∧T cl = T ck)
Pi(T ck ∧T cl = T cl) = Pi(T ck < T cl)
Pi(T cl < T ck) = γck
γcl .
(84)
Combining the above two equations, we obtain that
Pi(T ≤t, T = T ck ∧T cl|T ck < T cl) = Pi(T ≤t, T = T ck ∧T cl|T cl < T ck).
(85)
This implies that
Pi(T ≤t, T = T ck ∧T cl|T ck < T cl) = Pi(T ≤t, T = T ck ∧T cl).
(86)
Thus we obtain that
Pi(T ≤t, T = T ck) = Pi(T ≤t, T = T ck ∧T cl, T ck < T cl)
= Pi(T ≤t, T = T ck ∧T cl|T ck < T cl)Pi(T ck < T cl)
= Pi(T ≤t, T = T ck ∧T cl)Pi(T ck < T cl),
(87)
which gives the desired result.
20


## Page 21


We next use the generalized Haldane equalities to prove that the joint distribution of the empiri-
cal circulations has a certain symmetry.
Lemma 11. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Assume that
ck and cl are similar for some two indices 1 ≤k, l ≤r. Then for any n1, n2, · · · , nr ∈N,
Pi(Nc1
t
= n1, · · · , Nck
t
= nk, · · · , Ncl
t = nl, · · · , Ncr
t
= nr)
Pi(Nc1
t
= n1, · · · , Nck
t
= nl, · · · , Ncl
t = nk, · · · , Ncr
t
= nr) =
γck
γcl
nk−nl
.
(88)
Proof. We only need to prove this lemma when k = 1 and l = 2. The proof of the other cases is
totally the same. To simplify notations, let N = n1 + · · · + nr and let
p = Pi(T c1 < T c2),
q = Pi(T c2 < T c1).
(89)
Let Tn be the n-th forming time of c1, c2, · · · , cr by X. Let τn = Tn −Tn−1. Let ξn be the random
variable deﬁned in (71). Then we have
Pi(Nc1
t
= n1, · · · , Ncr
t
= nr)
=
X
A1,··· ,Ar
Pi(TN ≤t < TN+1, ξm = c1 for those m ∈A1, · · · , ξm = cr for those m ∈Ar),
where the sequence A1, · · · , Ar ranges over all partitions of {1, 2, · · · , N} such that Card(Ak) = nk
for each 1 ≤k ≤r. Then Lemma 10, together with the fact that (ξn, τn)n≥1 is independent and
identically distributed, shows that
Pi(Nc1
t
= n1, Nc2
t
= n2, Nc3
t
= n3, · · · , Ncr
t
= nr)
=
X
A1,··· ,Ar
Pi(TN ≤t < TN+1, ξm ∈{c1, c2} for those m ∈A1 ∪A2,
ξm = c3 for those m ∈A3, · · · , ξm = cr for those m ∈Ar)pn1qn2
=
X
B1,··· ,Br
Pi(TN ≤t < TN+1, ξm ∈{c1, c2} for those m ∈B2,
ξm = c3 for those m ∈B3, · · · , ξm = cr for those m ∈Br)Cn1
n1+n2pn1qn2
=
Pi(Nc1
t + Nc2
t
= n1 + n2, Nc3
t
= n3, · · · , Ncr
t
= nr)Cn1
n1+n2pn1qn2,
where the sequence B2, · · · , Br ranges over all partitions of {1, 2, · · · , N} such that Card(B2) =
n1 + n2 and Card(Bk) = nk for each 3 ≤k ≤r. By Theorem 4, it follows that
Pi(Nc1
t
= n1, Nc2
t
= n2, Nc3
t
= n3, · · · , Ncr
t
= nr)
= Pi(Nc1
t + Nc2
t
= n1 + n2, Nc3
t
= n3, · · · , Ncr
t
= nr)Cn1
n1+n2pn1qn2
= Pi(Nc1
t + Nc2
t
= n1 + n2, Nc3
t
= n3, · · · , Ncr
t
= nr)Cn1
n1+n2pn2qn1
p
q
n1−n2
= Pi(Nc1
t
= n2, Nc2
t
= n1, Nc3
t
= n3, · · · , Ncr
t
= nr)
γc1
γc2
n1−n2
,
(90)
which gives the desired result.
The next lemma shows that the moment generating function of the empirical circulations has a
certain symmetry.
21


## Page 22


Lemma 12. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Assume that
ck and cl are similar for some two indices 1 ≤k, l ≤r. Let
gt(λ1, · · · , λr) = Eieλ1N
c1
t +···+λrN cr
t
= Eiet(λ1J
c1
t +···+λrJ cr
t ).
(91)
Then for each t ≥0 and any λ1, · · · , λr ∈R,
gt(λ1, · · · , λk, · · · , λl, · · · , λr)
= gt(λ1, · · · , λl −log γck
γcl , · · · , λk + log γck
γcl , · · · , λr).
(92)
Proof. We only need to prove this lemma when k = 1 and l = 2. The proof of the other cases is
totally the same. By Lemma 11, we have
gt(λ1, λ2, λ3 · · · , λr) = Eieλ1N
c1
t +λ2N
c2
t +λ3N
c3
t +···+λrN cr
t
=
X
n1,··· ,nr∈N
eλ1n1+···+λrnrPi(Nc1
t
= n1, Nc2
t
= n2, Nc3
t
= n3, · · · , Ncr
t
= nr)
=
X
n1,··· ,nr∈N
eλ1n1+···+λrnrPi(Nc1
t
= n2, Nc2
t
= n1, Nc3
t
= n3, · · · , Ncr
t
= nr)
γc1
γc2
n1−n2
=
X
n1,··· ,nr∈N
e(λ1+log γc1
γc2 )n1+(λ2−log γc1
γc2 )n2+λ3n3+···+λrnrPi(Nc1
t
= n2, Nc2
t
= n1, Nc3
t
= n3, · · · , Ncr
t
= nr)
=
Eie(λ2−log γc1
γc2 )N
c1
t +(λ1+log γc1
γc2 )N
c2
t λ3N
c3
t +···+λrN cr
t
=
gt(λ2 −log γc1
γc2 , λ1 + log γc1
γc2 , λ3, · · · , λr),
which gives the desired result.
We also need the following lemma, whose original form is given by Varadhan [26].
Lemma 13. Let (µt)t>0 be a sequence of probability measures on a Polish space E which satisﬁes
a large deviation principle with rate t and good rate function I : E →[0, ∞]. Let F : E →R be
a continuous function. Assume that there exists γ > 1 such that the following moment condition is
satisﬁed:
lim sup
t→∞
1
t log
Z
E
eγtF(x)dµt(x) < ∞.
(93)
Then
lim
t→∞
1
t log
Z
E
etF(x)dµt(x) = sup
x∈E
(F(x) −I(x)).
(94)
Proof. The proof of this lemma can be found in [27].
Using the above lemma, we can obtain the following result.
Lemma 14. The notations are the same as in Lemma 12. Then for each λ ∈Rr,
lim
t→∞
1
t log gt(λ) = sup
x∈Rr{λ · x −Ic1,c2,··· ,cr(x)}.
(95)
22


## Page 23


Proof. Let λ = (λ1, · · · , λr). By Theorem 5, the law of (Jc1
t , · · · , Jcr
t ) satisﬁes a large deviation
principle with rate t and good rate function Ic1,··· ,cr. By Lemma 13, the result of this lemma holds
if the following moment condition is satisﬁed for each γ > 0:
lim sup
t→∞
1
t log Eieγt(λ1J
c1
t +···+λrJ cr
t ) < ∞.
(96)
Note that
Eieγt(λ1J
c1
t +···+λrJ cr
t ) ≤Eieγ|λ1|N
c1
t +···+γ|λr|N cr
t
≤Eieγα(N
c1
t +···+N cr
t ) = EieγαNt,
(97)
where α = max{|λ1|, · · · , |λr|} and Nt = inf{n ≥0 : Tn+1 > t} is the number of cycles
c1, · · · , cr formed by X up to time t. Since X starts from i, in order to form any one of the cycles
c1, · · · , cr, X must ﬁrst leave state i. This shows that the n-th forming time Tn of c1, · · · , cr by
X is larger than n independent exponential random variables with the same rate qi. where qi =
P
j̸=i qij. This further implies that Nt is stochastically dominated by a Poisson random variable Rt
with parameter qit. Thus we obtain that
EieγαNt =
Z ∞
−∞
γαeγαxPi(Nt ≥x)dx ≤
Z ∞
−∞
γαeγαxPi(Rt ≥x)dx
= EieγαRt =
∞
X
n=0
eγαn (qit)n
n!
e−qit = exp ((eγα −1)qit) .
(98)
This shows that
lim sup
t→∞
1
t log Eieγt(λ1J
c1
t +···+λrJ cr
t ) ≤lim sup
t→∞
1
t log EieγαNt ≤(eγα −1)qi < ∞.
(99)
This completes the proof of this lemma.
Remark 9. Lemma 14 shows that
lim
t→∞
1
t log gt(λ) = (Ic1,c2,··· ,cr)∗(λ),
(100)
where (Ic1,c2,··· ,cr)∗is the Legendre-Fenchel transform of the rate function Ic1,c2,··· ,cr. Recall that
the Legendre-Fenchel transform of a function f : Rr →[−∞, ∞] is a function f∗: Rr →[−∞, ∞]
deﬁned by
f∗(λ) = sup
x∈Rr{λ · x −F(x)}.
(101)
The following lemma, which is called the Fenchel-Moreau theorem, gives the sufﬁcient and
necessary conditions under which the Legendre-Fenchel transform is an involution. Recall that a
function f : Rr →[−∞, ∞] is called proper if f(x) < ∞for at least one x and f(x) > −∞for
each x.
Lemma 15. Let f : Rr →[−∞, ∞] be a proper function. Then f∗∗= f if and only if f is convex
and lower semi-continuous.
Proof. The proof of this lemma can be found in [28].
23


## Page 24


We are now in a position to prove the symmetry of the rate function Ic1,c2,··· ,cr.
Proof of Theorem 6. We only need to prove this theorem when k = 1 and l = 2. The proof of the
other cases is totally the same. By Lemma 14, we have
lim
t→∞
1
t log gt(λ1, · · · , λr) = (Ic1,··· ,cr)∗(λ1, · · · , λr).
(102)
By Lemma 12, we have
gt(λ1, λ2, λ3, · · · , λr) = gt(λ2 −log γc1
γc2 , λ1 + log γc1
γc2 , λ3, · · · , λr).
(103)
Combining the above two equations, we obtain that
(Ic1,··· ,cr)∗(λ1, λ2, λ3, · · · , λr)
= (Ic1,··· ,cr)∗(λ2 −log γc1
γc2 , λ1 + log γc1
γc2 , λ3, · · · , λr).
(104)
By Theorem 5 and Lemma 9, Ic1,··· ,cr is a good rate function which is also convex. This shows that
Ic1,··· ,cr is proper, convex, and lower semi-continuous. By Lemma 15, we obtain that Ic1,··· ,cr =
(Ic1,··· ,cr)∗∗. Thus we have
Ic1,··· ,cr(x1, x2, x3, · · · , xr) = (Ic1,··· ,cr)∗∗(x1, x2, x3, · · · , xr)
=
sup
λ1,··· ,λr∈R
{λ1x1 + · · · + λrxr −(Ic1,··· ,cr)∗(λ1, λ2, λ3, · · · , λr)}
=
sup
λ1,··· ,λr∈R
{λ1x1 + · · · + λrxr −(Ic1,··· ,cr)∗(λ2 −log γc1
γc2 , λ1 + log γc1
γc2 , λ3, · · · , λr)}
=
sup
λ1,··· ,λr∈R
{(λ1 −log γc1
γc2 )x1 + (λ2 + log γc1
γc2 )x2 + λ3x3 + · · · + λrxr −
(Ic1,··· ,cr)∗(λ2, λ1, λ3, · · · , λr)}
=
Ic1,··· ,cr(x2, x1, x3, · · · , xr) −

log γc1
γc2

(x1 −x2),
which gives the desired result.
Now that Theorem 5 and Theorem 6 hold for similar cycles, they also hold for conjugate cycles.
Thus we obtain the following corollary.
Corollary 7. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Then under
Pi, the law of (Jc1
t , Jc1−
t
, · · · , Jcr
t , Jcr−
t
) satisﬁes a large deviation principle with rate t and good
rate function Ic1,c1−,··· ,cr,cr−: R2r →[0, ∞]. Moreover, for each 1 ≤k ≤r, the rate function
Ic1,c1−,··· ,cr,cr−has the following symmetry:
Ic1,c1−,··· ,cr,cr−(x1, y1, · · · , xk, yk, · · · , xr, yr)
= Ic1,c1−,··· ,cr,cr−(x1, y1, · · · , yk, xk, · · · , xr, yr) −

log γck
γck−

(xk −yk).
(105)
Remark 10. The generalized Haldane equalities characterize the symmetry of the forming times
of a family of similar cycles. Theorem 6, Lemma 11, and Lemma 12, however, characterize the
symmetry of the empirical circulations of a family of similar cycles from different aspects.
24


## Page 25


7
Applications in natural sciences
7.1
Applications in nonequilibrium statistical physics
Markov chains are widely used to model various kinds of stochastic systems in physics, chem-
istry, and biology. In nonequilibrium statistical physics, one of the most important physical quan-
tities associated with a stochastic systems is the entropy production rate, which characterizes how
much entropy is produced by the system per unit time. Several research groups [21–23] have studied
the ﬂuctuations of the empirical entropy production rate for stochastic systems modeled by Markov
chains. Let X = (Xt)t≥0 be an irreducible and recurrent continuous-time Markov chain with denu-
merable state space S and transition rate matrix Q = (qij)i,j∈S. The empirical entropy production
rate Wt of X up to time t is deﬁned as
Wt = 1
t log
p0(X0)q ¯
X0 ¯
X1q ¯
X1 ¯
X2 · · · q ¯
X ˜
Nt−1 ¯
X ˜
Nt
pt(Xt)q ¯
X1 ¯
X0q ¯
X2 ¯
X1 · · · q ¯
X ˜
Nt ¯
X ˜
Nt−1
= 1
t log p0(X0)
pt(Xt) + 1
t
˜
Nt−1
X
i=0
log
q ¯
Xi ¯
Xi+1
q ¯
Xi+1 ¯
Xi
,
(106)
where pt = (pt(i))i∈S is the distribution of X at time t, ¯X = ( ¯Xn)n≥0 is the embedded chain of X,
and ˜Nt is the number of jumps of X up to time t. Physicists found that the empirical entropy pro-
duction rate Wt satisﬁes various kinds of ﬂuctuation theorems. This discovery has been considered
one of the most important results in nonequilibrium statistical physics in the last two decades.
Recently, physicists [8, 18] found that the empirical entropy production rate of Markov chains
can be decomposed into different cycles. Speciﬁcally, the empirical entropy production rate Wt can
be decomposed as
Wt = 1
2
X
c
Kc
t log γc
γc−+ W r
t ,
(107)
where c ranges over all cycles, Kc
t is the empirical net circulation of cycle c (see Deﬁnition 16), γc is
the strength of cycle c, and the remainder W r
t collects the contributions of those state transitions that
do not form a full cycle. This shows that the empirical net circulation Kc
t of cycle c is proportional
to the entropy production rate of X along cycle c. Thus it is nature to ask whether we can establish
ﬂuctuation theorems of the empirical net circulations for general Markov chains.
Fortunately, the generalized Haldane equalities established in this paper can be used to study the
circulation ﬂuctuations for Markov chains. To make the readers understand the relations between our
work and nonequilibrium statistical physics, we brieﬂy state various types of ﬂuctuation theorems
for the empirical net circulations.
We ﬁrst give the deﬁnition of the afﬁnities of cycles for Markov chains [18].
Deﬁnition 17. Let c be a cycle. Then the afﬁnity ρc of cycle c is deﬁned as
ρc = log γc
γc−.
(108)
Theorems of the following type are called transient ﬂuctuation theorems in nonequilibrium sta-
tistical physics. Transient ﬂuctuation theorems give the probability ratio of observing trajectories
that satisfy or violate the second law of thermodynamics.
25


## Page 26


Theorem 7. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Then for any
n1, n2, · · · , nr ∈Z,
Pi(Kc1
t
= n1/t, · · · , Kck
t
= nk/t, · · · , Kcr
t
= nr/t)
Pi(Kc1
t
= n1/t, · · · , Kck
t
= −nk/t, · · · , Kcr
t
= nr/t) = enkρck.
(109)
Proof. We only need to prove this theorem when k = 1. The proof of the other cases is totally the
same. By Lemma 11, we have
Pi(Kc1
t
= n1/t, · · · , Kck
t
= nk/t, · · · , Kcr
t
= nr/t)
=
Pi(Nc1
t −Nc1−
t
= n1, Nc2
t −Nc2−
t
= n2, · · · , Ncr
t
−Ncr−
t
= nr)
=
X
l1−m1=n1,··· ,lr−mr=nr
Pi(Nc1
t
= l1, Nc1−
t
= m1, Nc2
t
= l2, Nc2−
t
= m2, · · · ,
Ncr
t
= lr, Ncr−
t
= mr)
=
X
l1−m1=n1,··· ,lr−mr=nr
Pi(Nc1
t
= m1, Nc1−
t
= l1, Nc2
t
= l2, Nc2−
t
= m2, · · · ,
Ncr
t
= lr, Ncr−
t
= mr)e(l1−m1)ρc1
=
X
l1−m1=−n1,··· ,lr−mr=nr
Pi(Nc1
t
= l1, Nc1−
t
= m1, Nc2
t
= l2, Nc2−
t
= m2, · · · ,
Ncr
t
= lr, Ncr−
t
= mr)en1ρc1
=
Pi(Nc1
t −Nc1−
t
= −n1, Nc2
t −Nc2−
t
= n2, · · · , Ncr
t
−Ncr−
t
= nr)en1ρc1
=
Pi(Kc1
t
= n1/t, · · · , Kck
t
= −nk/t, · · · , Kcr
t
= nr/t)en1ρc1,
which gives the desired result.
Theorems of the following type are called Kurchan-Lebowitz-Spohn-type ﬂuctuation theorems
in nonequilibrium statistical physics.
Theorem 8. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Let
ht(λ1, · · · , λr) = Eiet(λ1K
c1
t +···+λrKcr
t ).
(110)
Then for each t ≥0 and any λ1, · · · , λr ∈R,
ht(λ1, · · · , λk, · · · , λr) = ht(λ1, · · · , −(λk + ρck), · · · , λr).
(111)
Proof. We only need to prove this theorem when k = 1. The proof of the other cases is totally the
same. By Theorem 7, we have
ht(λ1, λ2, · · · , λr) = Eiet(λ1K
c1
t +···+λrKcr
t )
=
X
n1,··· ,nr∈Z
eλ1n1+λ2n2+···+λrnrPi(Kc1
t
= n1/t, Kc2
t
= n2/t, · · · , Kcr
t
= nr/t)
=
X
n1,··· ,nr∈Z
eλ1n1+λ2n2+···+λrnrPi(Kc1
t
= −n1/t, Kc2
t
= n2/t, · · · , Kcr
t
= nr/t)en1ρc1
=
X
n1,··· ,nr∈Z
e(λ1+ρc1)n1+λ2n2+···+λrnrPi(Kc1
t
= −n1/t, Kc2
t
= n2/t, · · · , Kcr
t
= nr/t)
=
Eiet(−(λ1+ρc1)K
c1
t +λ2K
c2
t +···+λrKcr
t ) = ht(−(λ1 + ρc1), λ2, · · · , λr),
which gives the desired result.
26


## Page 27


Theorems of the following type are called integral ﬂuctuation theorems in nonequilibrium sta-
tistical physics.
Theorem 9. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Then for
each t ≥0,
Eie−t(K
c1
t ρc1+K
c2
t ρc2+···+Kcr
t ρcr) = 1.
(112)
Proof. By Theorem 8, for any λ1, · · · , λr ∈R,
Eiet(λ1K
c1
t +···+λrKcr
t ) = Eie−t((λ1+ρc1)K
c1
t +···+(λr+ρcr)Kcr
t ).
(113)
If we take λk = −ρck for each k in the above equation, we obtain the desired result.
The large deviations of the empirical net circulations and the symmetry of the rate function are
stated in the following theorem. Theorems of the following type are called Gallavotti-Cohen-type
ﬂuctuation theorems in nonequilibrium statistical physics.
Theorem 10. Let c1, c2, · · · , cr be a family of cycles passing through a common state i. Then under
Pi, the law of (Kc1
t , Kc2
t , · · · , Kcr
t ) satisﬁes a large deviation principle with rate t and good rate
function Ic1,c2,··· ,cr
K
: Rr →[0, ∞]. Moreover, for each 1 ≤k ≤r, the rate function Ic1,c2,··· ,cr
K
has
the following symmetry:
Ic1,c2,··· ,cr
K
(x1, · · · , xk, · · · , xr) = Ic1,c2,··· ,cr
K
(x1, · · · , −xk, · · · , xr) −ρckxk.
(114)
Proof. We only need to prove this theorem when k = 1. The proof of the other cases is totally the
same. Let F : R2r →Rr be a continuous map deﬁned as
F(x1, y1, · · · , xr, yr) = (x1 −y1, · · · , xr −yr).
(115)
Then we have
F(Jc1
t , Jc1−
t
, · · · , Jcr
t , Jcr−
t
) = (Kc1
t , · · · , Kcr
t ).
(116)
By Corollary 7, the law of (Jc1
t , Jc1−
t
, · · · , Jcr
t , Jcr−
t
) satisﬁes a large deviation principle with rate
t and good rate function Ic1,c1−,··· ,cr,cr−. Using the contraction principle, we see that the law of
(Kc1
t , · · · , Kcr
t ) satisﬁes a large deviation principle with rate t and good rate function
Ic1,··· ,cr
K
(z1, · · · , zr) =
inf
x1−y1=z1,··· ,xr−yr=zr Ic1,c1−,··· ,cr,cr−(x1, y1, · · · , xr, yr).
(117)
Thus we have
Ic1,··· ,cr
K
(z1, z2, · · · , zr)
=
inf
x1−y1=z1,··· ,xr−yr=zr Ic1,c1−,··· ,cr,cr−(x1, y1, x2, y2, · · · , xr, yr)
=
inf
x1−y1=z1,··· ,xr−yr=zr Ic1,c1−,··· ,cr,cr−(y1, x1, x2, y2, · · · , xr, yr) −ρc1(x1 −y1)
=
inf
y1−x1=−z1,x2−y2=z2,··· ,xr−yr=zr Ic1,c1−,··· ,cr,cr−(y1, x1, x2, y2, · · · , xr, yr) −ρc1z1
=
Ic1,··· ,cr
K
(−z1, z2, · · · , zr) −ρc1z1,
which gives the desired result.
27


## Page 28


7.2
Applications in biochemistry
One of the most important branch of biochemistry is enzyme kinetics, which studies chemical
reactions that are catalyzed by enzymes. Recently, it has been made possible to study enzyme
kinetics at the single-molecule level, in which case the concept of concentration makes no sense and
the behavior of enzymes must be studied in a single-molecule way.
Let us consider the following three-step reversible Michaelis-Menten enzyme kinetics [11, 16,
29]:
E + S GGGB
FGGG ES GGGB
FGGG EP GGGB
FGGG E + P,
(118)
where E is an enzyme involved in converting the substrate S into the product P. If there is only
one enzyme molecule, it may transition stochastically among three states: the free enzyme E, the
enzyme-substrate complex ES, and the enzyme-product complex EP. From the perspective of a
single enzyme molecule, the Michaelis-Menten enzyme kinetics (118) can be modeled by the three-
state Markov chain illustrated in Figure 1(a). However, single-substrate enzymes are actually rather
rare in biochemistry [17]. If the enzyme E can catalyze multiple chemical reactions simultaneously
with substrates S1, S2, · · · , Sn and products P1, P2, · · · , Pn, then the topology of the Markov chain
model will contain multiple cycles passing through a common state E, as illustrated in Figure 1(b).
E
ES
EP
E
ES1
EP1
ESn
ES2
EP2
EPn
many other cycles
(a)
(b)
Figure 1. Markov chain models of enzyme kinetics. (a) The Markov chain model of single-substrate enzyme
kinetics. (b) The Markov chain model of multiple-substrate enzyme kinetics.
We assume that the Markov chain illustrated in Figure 1(b) starts from state E. If the Markov
chain forms a clockwise cycle ck = (E, ESk, EPk), then the substrate Sk is converted into the
product Pk for one time. Similarly, if the Markov chain forms a counterclockwise cycle ck−=
(E, EPk, ESk), then the product Pk is converted into the substrate Sk for one time. Thus the empir-
ical net circulation Kck
t
of cycle ck represents the net number of conversions from the substrate Sk
into the product Pk per unit time and the quantity
W ck
t
= Kck
t ρck
(119)
represents the ﬂuctuating chemical work done along cycle ck [11, 15, 17], where ρck is the afﬁnity
of cycle ck (see Deﬁnition 17). In fact, the results of this paper can be directly applied to establish
28


## Page 29


the multivariate ﬂuctuation theorems of the empirical net circulations of cycles c1, c2, · · · , cn and
the ﬂuctuating chemical works done along cycles c1, c2, · · · , cn. This shows that our work would
have a board application prospect in biochemistry.
Acknowledgements
The authors gratefully acknowledge Prof. Hao Ge at Peking University for stimulating discus-
sions and gratefully acknowledge ﬁnancial support from NSFC 11271029 and NSFC 11171024.
The ﬁrst author also acknowledges ﬁnancial support from the Academic Award for Young Ph.D.
Researchers granted by the Ministry of Education of China.
References
[1] MP Qian and Min Qian. The decomposition into a detailed balance part and a circulation part of an
irreversible stationary markov chain. Scientia Sinica, Special Issue (II), 69, 1979.
[2] C Qian, Min Qian, and MP Qian. Markov chain as a model of hill’s theory on circulation. Scientia
Sinica, 24(10):1431–1448, 1981.
[3] Qian Minping, Qian Min, and Qian Cheng. Circulation distribution of a markov chain. Scientia Sinica
A, 25:31–40, 1982.
[4] Qian Minping and Qian Min. Circulation for recurrent markov chains. Probability Theory and Related
Fields, 59(2):203–210, 1982.
[5] MP Qian, M Qian, and C Qian. Circulations of markov-chains with continuous-time and the probabil-
ity interpretation of some determinants. SCIENTIA SINICA SERIES A-MATHEMATICAL PHYSICAL
ASTRONOMICAL & TECHNICAL SCIENCES, 27(5):470–481, 1984.
[6] S Kalpazidou. Asymptotic behaviour of sample weighted circuits representing recurrent markov chains.
Journal of applied probability, pages 545–556, 1990.
[7] MP Qian, Min Qian, and GL Gong. The reversibility and the entropy production of markov processes.
Contemp. Math, 118:255–261, 1991.
[8] Da-Quan Jiang and Min Qian. Mathematical theory of nonequilibrium steady states: on the frontier of
probability and dynamical systems. Number 1833. Springer, 2004.
[9] Sophia L Kalpazidou. Cycle representations of Markov processes, volume 28. Springer, 2007.
[10] Xue-Juan Zhang, Hong Qian, and Min Qian. Stochastic theory of nonequilibrium steady states and its
applications. part i. Physics Reports, 510(1):1–86, 2012.
[11] Hao Ge, Min Qian, and Hong Qian. Stochastic theory of nonequilibrium steady states. part ii: Applica-
tions in chemical biophysics. Physics Reports, 510(3):87–118, 2012.
[12] Andrei Kolmogoroff. Zur theorie der markoffschen ketten. Mathematische Annalen, 112(1):155–160,
1936.
[13] Terrell Hill. Free energy transduction in biology: the steady-state kinetic and thermodynamic formalism.
Elsevier, 2012.
[14] Terrell L Hill. Free Energy Transduction and Biochemical Cycle Kinetics. Courier Dover Publications,
2013.
[15] Hong Qian and X Sunney Xie. Generalized haldane equation and ﬂuctuation theorem in the steady-state
cycle kinetics of single enzymes. Physical Review E, 74(1):010902, 2006.
[16] Hao Ge. Waiting cycle times and generalized haldane equality in the steady-state cycle kinetics of single
enzymes. The Journal of Physical Chemistry B, 112(1):61–70, 2008.
[17] Hao Ge. Multivariable ﬂuctuation theorems in the steady-state cycle kinetics of single enzyme with
competing substrates. Journal of Physics A: Mathematical and Theoretical, 45(21):215002, 2012.
29


## Page 30


[18] Udo Seifert. Stochastic thermodynamics, ﬂuctuation theorems and molecular machines. Reports on
Progress in Physics, 75(12):126001, 2012.
[19] Denis J Evans, EGD Cohen, and GP Morriss. Probability of second law violations in shearing steady
states. Physical Review Letters, 71(15):2401, 1993.
[20] Giovanni Gallavotti and EGD Cohen. Dynamical ensembles in stationary states. Journal of Statistical
Physics, 80(5-6):931–970, 1995.
[21] Joel L Lebowitz and Herbert Spohn. A gallavotti–cohen-type symmetry in the large deviation functional
for stochastic dynamics. Journal of Statistical Physics, 95(1-2):333–365, 1999.
[22] Da-Quan Jiang, Min Qian, and Fu-Xi Zhang. Entropy production ﬂuctuations of ﬁnite markov chains.
Journal of Mathematical Physics, 44(9):4176–4188, 2003.
[23] Udo Seifert. Entropy production along a stochastic trajectory and an integral ﬂuctuation theorem. Phys-
ical review letters, 95(4):040602, 2005.
[24] Kai Lai Chung. Markov chains. Springer, 1967.
[25] Mauro Mariani, Yuhao Shen, and Lorenzo Zambotti. Large deviations for the empirical measure of
markov renewal processes. arXiv preprint arXiv:1203.5930, 2012.
[26] SR Srinivasa Varadhan, SR Srinivasa Varadhan, and SR Srinivasa Varadhan. Large deviations and appli-
cations, volume 46. SIAM, 1984.
[27] Amir Dembo and Ofer Zeitouni. Large deviations techniques and applications, volume 2. Springer,
1998.
[28] Jonathan M Borwein and Adrian S Lewis. Convex analysis and nonlinear optimization: theory and
examples, volume 3. Springer, 2010.
[29] Daniel A Beard and Hong Qian. Chemical biophysics: quantitative analysis of cellular systems. Cam-
bridge University Press, 2008.
30

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1407_1263v2_cycle_symmetries_and_circulation_fluctuations_for_discrete_time_and_continuous_t
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2014/1407_1263V2_CYCLE_SYMMETRIES_AND_CIRCULATION_FLUCTUATIONS_FOR_DISCRETE_TIME_AND_CONTINUOUS_T.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
