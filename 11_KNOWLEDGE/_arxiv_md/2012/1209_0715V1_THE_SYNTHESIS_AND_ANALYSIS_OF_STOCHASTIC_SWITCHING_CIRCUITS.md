---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1209.0715v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1209.0715v1_The_Synthesis_and_Analysis_of_Stochastic_Switching_Circuits

> Source: 1209.0715v1_The_Synthesis_and_Analysis_of_Stochastic_Switching_Circuits.pdf

> Pages: 15

---


## Page 1


arXiv:1209.0715v1  [cs.IT]  4 Sep 2012
1
The Synthesis and Analysis of Stochastic Switching
Circuits
Hongchao Zhou, Po-Ling Loh, Jehoshua Bruck, Fellow, IEEE
Abstract—Stochastic switching circuits are relay circuits that
consist of stochastic switches called pswitches. The study of
stochastic switching circuits has widespread applications in many
ﬁelds of computer science, neuroscience, and biochemistry. In
this paper, we discuss several properties of stochastic switching
circuits, including robustness, expressibility, and probability ap-
proximation.
First, we study the robustness, namely, the effect caused by
introducing an error of size ǫ to each pswitch in a stochastic
circuit. We analyze two constructions and prove that simple
series-parallel circuits are robust to small error perturbations,
while general series-parallel circuits are not. Speciﬁcally, the total
error introduced by perturbations of size less than ǫ is bounded
by a constant multiple of ǫ in a simple series-parallel circuit,
independent of the size of the circuit.
Next, we study the expressibility of stochastic switching cir-
cuits: Given an integer q and a pswitch set S = { 1
q , 2
q , . . . , q−1
q },
can we synthesize any rational probability with denominator qn
(for arbitrary n) with a simple series-parallel stochastic switching
circuit? We generalize previous results and prove that when q is
a multiple of 2 or 3, the answer is yes. We also show that when
q is a prime number larger than 3, the answer is no.
Probability approximation is studied for a general case of an
arbitrary pswitch set S = {s1, s2, . . . , s|S|}. In this case, we
propose an algorithm based on local optimization to approximate
any desired probability. The analysis reveals that the approxi-
mation error of a switching circuit decreases exponentially with
an increasing circuit size.
Index Terms—Stochastic Switching Circuits, Robustness, Prob-
ability Synthesis, Probability Approximation.
I. INTRODUCTION
I
N his master’s thesis of 1938, Claude Shannon demon-
strated how Boolean algebra can be used to synthesize and
simplify relay circuits, establishing the foundation of mod-
ern digital circuit design [12]. Later, deterministic switches
were replaced with probabilistic switches to make stochastic
switching circuits, which were studied in [15]. There are a
few features of stochastic switching circuits that make them
very similar to neural systems. First, randomness is inherent
in neural systems and it may play a crucial role in thinking
and reasoning. Switching (and relaying) technique provides
us a natural way of manipulating this randomness. Second,
in a switching system, each switch can be treated as either a
This work was supported in part by the NSF Expeditions in Computing
Program under grant CCF-0832824. This paper was presented in part at IEEE
International Symposium on Information Theory (ISIT), Seoul, Korea, June
2009.
H. Zhou and J. Bruck are with the Department of Electrical Engi-
neering, California Institute of Technology, Pasadena, CA, 91125. Email:
hzhou@caltech.edu, bruck@caltech.edu
P. Loh is with the Department of Statistics, University of California,
Berkeley, CA 94720. Email: ploh@berkeley.edu
memory element or a control element for computing. This
might enable creating an intelligent system where storage
and computing are highly integrated. In this paper, we study
stochastic switching circuits from a basic starting point with
focusing on probability synthesis. We consider two-terminal
stochastic switching circuits, where each probabilistic switch,
or pswitch, is closed with some probability chosen from a
ﬁnite set of rational numbers, called a pswitch set. By selecting
pswitches with different probabilities and composing them in
appropriate ways, we can realize a variety of different closure
probabilities.
Formally, for a two-terminal stochastic switching circuit C,
the probabilities of pswitches are taken from a ﬁxed pswitch
set S, and all these pswitches are open or closed independently.
We use P(C) to denote the probability that the two terminals
of C are connected, and call P(C) the closure probability of
C. Given a pswitch set S, a probability x can be realized if
and only if there exists a circuit C such that x = P(C). Based
on the ways of composing pswitches, we have series-parallel
(sp) circuits and non-series-parallel (non-sp) circuits. An sp
circuit consists of either a single pswitch or two sp circuits
connected in series or parallel, see the circuit in Fig. 1(a) and
1(b) as examples. The circuit in Fig. 1(c) is a non-sp circuit. A
special type of sp circuits is called simple-series-parallel (ssp)
circuits. An ssp circuit is either a single pswitch, or is built
by taking an ssp circuit and adding another pswitch in either
series or parallel. For example, the circuit in Fig. 1(a) is an
ssp circuit but the one in Fig. 1(b) is not.
In this paper, we ﬁrst study the robustness of different
stochastic switching circuits in the presence of small error
perturbations. We assume that the probabilities of individual
pswitches are taken from a ﬁxed pswitch set with a given error
allowance of ǫ; that is, the error probabilities of the pswitches
are bounded by ǫ. We show that ssp circuits are robust to
small error perturbations, but the error probability of a general
sp circuit may be ampliﬁed by adding additional pswitches.
These results might help us understand why local errors do
not accumulate in a natural system, and how to enhance the
robustness of a system when designing a circuit.
Next, we study the problem of synthesizing desired proba-
bilities with stochastic switching circuits. We mainly focus
on ssp circuits due to their robustness against small error
perturbations. Two main questions are addressed: (1) Express-
ibility: Given the pswitch set S = { 1
q , 2
q , . . . , q−1
q }, where
q is an integer, what kind of probabilities can be realized
using stochastic switching circuits? And how many pswitches
are sufﬁcient to realize them? (2) Approximation: Given an
arbitrary pswitch set S, how can we construct a stochastic


## Page 2


2
1/2
1/2
1/2
(a) ssp circuit. P (C) = 5
8.
1/2
1/2
1/2
1/2
(b) sp circuit, non-ssp.
P (C) =
7
16 .
1/2
1/2
1/2
1/2
1/2
(c) non-sp circuit. P (C) = 1
2.
Fig. 1.
Examples of ssp, sp, and non-sp circuits.
switching circuit using as a few as possible pswitches, to get
a good approximation of the desired probabilities?
The study of probability synthesis based on stochastic
switching circuits has widespread applications. Recently, peo-
ple found that DNA molecules can be constructed that closely
approximate the dynamic behavior of arbitrary systems of
coupled chemical reactions [13], which leads to the ﬁeld
of molecular computing [2]. In such systems, the quantities
of molecules involved in a reaction are often surprisingly
small, and the exact sequence of reactions is determined by
chance [4]. Stochastic switching circuits provide a simple and
powerful tool to manipulate stochasticity in molecular sys-
tems. Comparing with combinational logic circuits, stochastic
switching circuits are easier to implement using molecular re-
actions. Another type of applications is probabilistic electrical
systems without sophisticated computing components. In such
systems, stochastic switching circuits have many advantages
in generating desired probabilities, including its constructive
simplicity, robustness, and low cost.
The remainder of this paper is organized as follows: Section
II describes related work and introduces some existing results
on stochastic switching circuits. In Section III, we analyze the
robustness of different kinds of stochastic switching circuits.
Then we discuss the expressibility of stochastic switching
circuits in Section IV and probability approximation in Section
V, followed by the conclusion in Section VI.
II. RELATED WORKS AND PRELIMINARIES
There are a number of studies related to the problem of
generating desired distributions from the algorithmic perspec-
tive. This problem dates back to von Neumann [14], who
considered of simulating an unbiased coin using a biased coin
with unknown probability. Later, Elias [3] improved this algo-
rithm such that the expected number of unbiased random bits
generated per coin toss is asymptotically equal to the entropy
of the biased coin. On the other hand, people have considered
the case that the probability distribution of the tossed coin is
known. Knuth and Yao [9] have given a procedure to generate
an arbitrary probability using an unbiased coin. Han and Hoshi
[7] have demonstrated how to generate an arbitrary probability
using a general M-sided biased coin. All these works aim to
efﬁciently convert one distribution to another. However, they
require computing models and may not be applicable for some
simple or distributed electrical/molecular systems.
There are a number of studies focusing on synthesizing a
simple physical device to generate desired probabilities. Gill
[5] [6] discussed the problem of generating rational proba-
bilities using a sequential state machine. Motivated by neural
computation, Jeavons et al. provided an algorithm to generate
binary sequences with probability
a
qn from a set of stochastic
binary sequences with probabilities in { 1
q , 2
q , . . . , q−1
q } [8].
Their method can be implemented using the concept of linear
feedback shift registers. Recently, inspired by PCMOS tech-
nology [1], Qian et al. considered the synthesis of decimal
probabilities using combinational logic [11]. They have con-
sidered three different scenarios, depending on whether the
given probabilities can be duplicated, and whether there is
freedom to choose the probabilities. In contact to the forego-
ing contributions, we consider the properties and probability
synthesis of stochastic switching circuits. Our approach is or-
thogonal and complementary to that of Qian and Riedel, which
is based on combinational logic. Generally, each switching
circuit can be equivalently expressed by a combinational logic
circuit. All the constructive methods of stochastic switching
circuits in this paper can be directly applied to probabilistic
combinational logic circuits.
In the rest of this section, we introduce the original work
that started the study on stochastic switching circuits (Wilhelm
and Bruck [15]). Similar to resistor circuits [10], connecting
one terminal of a switching circuit C1 (where P(C1) = p1) to
one terminal of a circuit C2 (where P(C2) = p2) places them
in series. The resulting circuit is closed if and only if both
of C1 and C2 are closed, so the probability of the resulting
circuit is
pseries = p1 · p2.
Connecting both terminals of C1 and C2 together places the
circuits in parallel. The resulting circuit is closed if and only
if either C1 or C2 is closed, so the probability of the resulting
circuit is
pparallel = 1 −(1 −p1)(1 −p2) = p1 + p2 −p1p2.
Based on these rules, we can calculate the probability of any
given ssp or sp circuit. For example, the probability of the
circuit in Fig. 1(a) is
p(a) =
1
2 · 1
2

+ 1
2 −
1
2 · 1
2
 1
2 = 5
8,
and the probability of the circuit in Fig. 1(b) is
p(b) =
1
2 · 1
2

+
1
2 · 1
2

−
1
2 · 1
2
 1
2 · 1
2

= 7
16.
Let us consider the non-sp circuit in Fig. 1(c). In this circuit,
we call the pswitch in the middle a ‘bridge’. If the bridge is
closed, the circuit has a closure probability of
9
16. If the bridge


## Page 3


3
is open, the circuit has a closure probability of
7
16. Since the
bridge is closed with probability 1
2, the overall probability of
the circuit is
p(c) = 1
2 · 9
16 + 1
2 · 7
16 = 1
2.
An important and interesting question is that if S is uniform,
i.e., S = { 1
q , 2
q , . . . , q−1
q } for some q, what kind of probabili-
ties can be realized using stochastic switching circuits? In [15],
Wilhelm and Bruck proposed an optimal algorithm (called B-
Algorithm) to realize all rational probabilities of the form
a
2n
with 0 < a < 2n, using an ssp circuit when S = { 1
2}. In their
algorithm, at most n pswitches are used, which is optimal.
They also proved that given the pswitch set S = { 1
3, 2
3}, all
rational probabilities
a
3n with 0 < a < 3n can be realized by
an ssp circuit with at most n pswitches; given the pswitch set
S = { 1
4, 2
4, 3
4}, all rational probabilities
a
4n with 0 < a < 4n
can be realized by an ssp circuit with at most 2n−1 pswitches.
1/3
1/4
1/2
(a) Initial circuit. P = 1
4 .
1/2
3/4
2/3
(b) The dual. P = 3
4.
Fig. 2.
A circuit and its dual.
Wilhelm and Bruck also demonstrated the concept of duality
in sp circuits. The dual of a single pswitch of probability p
appearing in series is the corresponding pswitch of probability
1 −p appearing in parallel. Similarly, the dual of a pswitch of
probability p appearing in parallel is a pswitch of probability
1 −p appearing in series. For example, in Fig. 2, the circuit
in (b) is the dual of the circuit in (a), and vice versa. It can
be proved that dual circuits satisfy the following relation:
Theorem 1 (Duality Theorem [15]). For a stochastic series-
parallel circuit C and its dual C, we have
P(C) + P(C) = 1,
where P(C) is the probability of circuit C and P(C) is the
probability of circuit C.
III. ROBUSTNESS
In this section, we analyze the robustness of different kinds
of stochastic switching circuits, where the probabilities of
individual pswitches are taken from a ﬁxed pswitch set, but
given an error allowance of ǫ; i.e., the error probabilities
of the pswitches are bounded by ǫ. For a stochastic circuit
with multiple pswitches, the error probability of the circuit
is the absolute difference between the probability that the
circuit is closed when error probabilities of pswitches are
included, and the probability that the circuit is closed when
error probabilities are omitted. We show that ssp circuits are
robust to small error perturbations, but the error probability
of a general sp circuit may be ampliﬁed with additional
pswitches.
A. Robustness of ssp Circuits
Here, we analyze the susceptibility of ssp circuits to small
error perturbations in individual pswitches. Based on our
assumption, instead of assigning a pswitch a probability of
p, the pswitch may be assigned a probability between p −ǫ
and p + ǫ, where ǫ is a ﬁxed error allowance.
Theorem 2 (Robustness of ssp circuits). Given a pswitch set
S, if the error probability of each pswitch is bounded by ǫ,
then the total error probability of an ssp circuit is bounded by
ǫ
min(min(S), 1 −max(S)).
Proof: We induct on the number of pswitches. If we
have just one pswitch, the result is trivial. Suppose the
result holds for n pswitches, and note that for an ssp circuit
with n + 1 pswitches, the last pswitch will either be added
in series or in parallel with the ﬁrst n pswitches. By the
induction hypothesis, the circuit constructed from the ﬁrst n
pswitches has probability p + ǫ1 of being closed, where ǫ1
is the error probability introduced by the ﬁrst n pswitches
and |ǫ1| ≤
ǫ
min(min(S),1−max(S)). The (n + 1)st pswitch has
probability t + ǫ2 of being closed, where t ∈S and |ǫ2| ≤ǫ.
1e
+
p
2
e
+
t
(a) The last pswitch is added in
series.
1e
+
p
2
e
+
t
(b) The last pswitch is added in
parallel.
Fig. 3.
Robustness of ssp circuits.
If the (n + 1)st pswitch is added in series, see Fig. 3(a),
then the new circuit (with errors) has probability
(p + ǫ1)(t + ǫ2) = tp + ǫ2(p + ǫ1) + tǫ1
of being closed. Without considering the error probability of
each pswitch, the probability of the new circuit is tp. Hence,
the overall error probability of the circuit is e1 = ǫ2(p+ǫ1)+
tǫ1. By the triangle inequality and the induction hypothesis,
|e1|
≤
|ǫ2||(p + ǫ1)| + t|ǫ1| ≤|ǫ2| + t|ǫ1|
≤

t
min(min(S), 1 −max(S)) + 1

ǫ
≤
min(min(S), 1 −max(S)) + max(S)
min(min(S), 1 −max(S))
· ǫ
≤
ǫ
min(min(S), 1 −max(S)),
completing the induction.
Similarly, if the (n + 1)st pswitch is added in parallel, see
Fig. 3(b), then the new circuit (with errors) has probability
(p + ǫ1) + (t + ǫ2) −(p + ǫ1)(t + ǫ2)
=
(p + t −tp) + ǫ1(1 −t) + ǫ2(1 −p −ǫ1)
of being closed. Without considering the error probability of
each pswitch, the probability that the circuit is closed is p +


## Page 4


4
t −tp. Hence, the overall error probability of the circuit with
n + 1 pswitches is e2 = ǫ1(1 −t) + ǫ2(1 −p −ǫ1). Again
using the induction hypothesis and the triangle inequality, we
have
|e2|
≤
|ǫ2||(1 −p −ǫ1)| + (1 −t)|ǫ1|
≤
|ǫ2| + (1 −t)|ǫ1|
≤

1 −t
min{min(S), 1 −max(S)) + 1

ǫ
≤
min{min(S), 1 −max(S)) + 1 −min(S)
min{min(S), 1 −max(S))
· ǫ
≤
ǫ
min{min(S), 1 −max(S)).
This completes the proof.
The theorem above implies that ssp circuits are robust to
small error perturbations: no matter how big the circuit is, the
error probability of an ssp circuit will be well bounded by a
constant times ǫ. Let us consider a case that S = { 1
2}. In this
case, the overall error probability of any ssp circuit is bounded
by 2ǫ if each pswitch is given an error allowance of ǫ.
B. Robustness of sp Circuits
We have proved that for a given pswitch set S, the overall
error probability of an ssp circuit is well bounded. We want to
know whether this property holds for all sp circuits. Unfortu-
nately, we show that as the number of pswitches increases, the
overall error probability of an sp circuit may also increase. In
this subsection, we will give the upper bound and lower bound
for the error probabilities of sp circuits.
Theorem 3 (Lower bound for sp circuits). Given a pswitch set
S, if the error probability of each pswitch is ǫ (where ǫ →0),
then there exists an sp circuit of size n with overall error
probability O(log n)ǫ.
Proof: Suppose p ∈S, and without loss of generality,
assume ǫ > 0. We construct an sp circuit as shown in Fig. 4,
by connecting a + 1 strings of pswitches in parallel. Among
these strings, we have a strings of b pswitches and one string
of n−ab pswitches, and all pswitches have probability p. Now,
we let a and b satisfy the following relation:
a =
ln
b
m
−1, a =

(1
p)b

.
Without considering pswitch errors, the probability of the
circuit is
p1 = 1 −(1 −pb)a(1 −pn−ab).
Suppose we introduce an error of ǫ to each pswitch, such
that the probability of each pswitch is p + ǫ (assume ǫ > 0).
Then the probability of the circuit is
p2(ǫ) = 1 −(1 −(p + ǫ)b)a(1 −(p + ǫ)n−ab),
where p2(0) = p1.
•
•
•
•
pswitches
ab
n  
pswitches
b
strings
1
 
a
Fig. 4.
The construction of an sp circuit.
Assuming n is large enough, we have the following error
probability for the circuit:
e1
=
p2(ǫ) −p1
≃
p′
2(ǫ)ǫ
≃
−[(1 −(p + ǫ)b)a(1 −(p + ǫ)n−ab)]′ǫ
≃
−[e−a(p+ǫ)b(1 −(p + ǫ)n−ab)]′ǫ
≃
e−a(p+ǫ)bab(p + ǫ)b−1(1 −(p + ǫ)n−ab)ǫ
+e−a(p+ǫ)b(n −ab)(p + ǫ)n−ab−1ǫ
≃
[e−apbabpb−1(1 −pn−ab) + e−apb(n −ab)pn−ab−1]ǫ
≃
[e−1 b
p(1 −pn−ab) + e−1(n −ab)pn−ab−1]ǫ.
So when n is large enough, we have
e−1 1 −p
p
bǫ ≤|e1| ≤e−1 1
pbǫ.
Since b⌊( 1
p)b⌋< n ≤b(⌊( 1
p)b⌋+ 1) for large n, we have
b ∼log n
log 1
p
−log log n
log 1
p
+
log log 1
p
log 1
p
∼log n
log 1
p
.
Finally, we have |e1| ∼O(log n)ǫ, completing the proof.
In the following theorem, we will give the upper bound for
the error probabilities of sp circuits.
Theorem 4 (Upper bound for sp circuits). Given an sp circuit
with n pswitches taken from a ﬁnite pswitch set S, if each
pswitch has error probability bounded by ǫ, then the total
error probability of the circuit is bounded by c√nǫ, where
c = maxt∈S
1
√
t(1−t) is a constant.
Proof: Assume x is a pswitch in a stochastic circuit C,
and the actual probability of x is tx +ǫx, where ǫx is the error
part such that |ǫx| ≤ǫ. Let P(C|x = 1) denote the probability
of circuit C when x is closed, and let P(C|x = 0) denote the
probability of C when x is open.
Without considering the error probability of x, the proba-
bility of circuit C can be written as
Px(C) = txP(C|x = 1) + (1 −tx)P(C|x = 0).


## Page 5


5
Considering the error part of x, we have
P(C) = (tx + ǫx)P(C|x = 1) + (1 −tx −ǫx)P(C|x = 0).
In order to prove the theorem, we deﬁne a term called the
error contribution. In a circuit C, the error contribution of
pswitch x is deﬁned as
ex(C) = |P(C) −Px(C)| = ǫx|P(C|x = 1) −P(C|x = 0)|
≤ǫ(P(C|x = 1) −P(C|x = 0)).
In the rest of the proof, we have two steps.
(1) In the ﬁrst step, we show that given an sp circuit
with size n, there exists at least one pswitch such that its
error contribution is bounded by
c√
(1−P )P
√n
ǫ, where P is the
probability of the sp circuit and c = maxt∈S
1
√
t(1−t).
We induct on the number of pswitches. If the circuit has
only one pswitch, the result is trivial. Suppose the result holds
for k pswitches for all k < n. We need to prove that the result
holds for any sp circuit C with n pswitches.
Suppose circuit C is constructed by connecting two sp
circuits C1 and C2 in series, where C1 has n1 pswitches and
probability P1, and C2 has n2 pswitches and probability P2.
Note that n1 + n2 = n and n1 < n, n2 < n.
By the induction hypothesis, circuit C1 contains a pswitch
x1 with error contribution
ex1(C1) ≤c
p
(1 −P1)P1
√n1
ǫ.
In circuit C, the error contribution of pswitch x1 is
ex1(C) = |P(C) −Px1(C)| = P2|P(C1) −Px1(C1)|
= P2ex1(C1).
Similarly, in the circuit C2, there exists a pswitch x2 such
that the error contribution of x2 is
ex2(C2) ≤c
p
(1 −P2)P2
√n2
ǫ,
and the error contribution of x2 to circuit C is
ex2(C) = P1ex2(C2).
Since the circuit C is constructed by connecting circuits C1
and C2 in series, the probability of circuit C is P = P1P2.
Thus, we only need to prove that either ex1(C) or ex2(C) is
bounded by
c
p
(1 −P1P2)P1P2
√n1 + n2
ǫ,
This can be proved by contradiction as follows.
Assume
both
ex1(C)
and
ex2(C)
are
larger
than
c√
(1−P1P2)P1P2
√n1+n2
ǫ. Then we have
P2
c
p
(1 −P1)P1
√n1
> c
p
(1 −P1P2)P1P2
√n1 + n2
and
P1
c
p
(1 −P2)P2
√n2
> c
p
(1 −P1P2)P1P2
√n1 + n2
,
which can be simpliﬁed as
n1
n1 + n2
< (1 −P1)P2
1 −P1P2
and
n2
n1 + n2
< (1 −P2)P1
1 −P1P2
.
Adding the two inequalities yields
P1 + P2 −1 −P1P2 = −(1 −P1)(1 −P2) > 0,
which is a contradiction. So we conclude that at least one
of ex1(C) and ex2(C) is bounded by
c√
(1−P1P2)P1P2
√n1+n2
ǫ when
C is constructed by connecting two sp circuits in series. If
the circuit C is constructed by connecting two sp circuits
in parallel, using a similar argument, we can get the same
conclusion.
Finally, we get that given an sp circuit with size n, there
exists at least one pswitch such that its error contribution is
bounded by
c√
(1−P )P
√n
ǫ.
(2) In the second step, we prove the theorem based on the
result above.
We again induct on the number of pswitches. If we have
less than three pswitches, the result is trivial. Suppose the
result holds for any sp circuit with n ≥2 pswitches; we want
to prove that the result also holds for any circuit with n + 1
pswitches.
Based on the result in the ﬁrst step, we know that given an
sp circuit C with n + 1 pswitches, there exists a pswitch x
with error contribution bounded by
c
2√n+1ǫ.
By keeping pswitch x closed, we obtain an sp circuit
D1 with at most n pswitches. Please see Fig. 5(a)(b) as an
example. Without considering pswitch errors, D1 is closed
with probability p1; considering all pswitch errors, D1 is
closed with probability q1. According to our assumption, we
have
e1 = |q1 −p1| ≤c√nǫ.
A
B
C
D
(a) Circuit C.
B
C
D
(b) D1, A closed.
C
D
(c) D2, A open.
Fig. 5.
An illustration of keeping a pswitch A closed or open in an sp circuit
C.


## Page 6


6
By keeping pswitch x open, we obtain an sp circuit D2
with at most n pswitches. Please see Fig. 5(a)(c) as an
example. Without considering pswitch errors, D2 is closed
with probability p2; considering all pswitch errors, D2 is
closed with probability q2. According to our assumption, we
have
e2 = |q2 −p2| ≤c√nǫ.
For the initial sp circuit C with n + 1 pswitches, without
considering pswitch errors, the overall probability of the circuit
is given by
txp1 + (1 −tx)p2,
where tx is the probability of pswitch x.
Considering all pswitch errors, the overall probability of the
circuit is
(tx + ǫx)q1 + (1 −tx −ǫx)q2.
We know that the error contribution of pswitch x to the
circuit C is
ex(C) = ǫx|q2 −q1| ≤
c
2√n + 1ǫ.
Then by the triangle inequality, we can get the error
probability of the circuit C:
e
=
|(tx + ǫx)q1 + (1 −tx −ǫx)q2 −(txp1 + (1 −tx)p2)|
≤
tx|q1 −p1| + (1 −tx)|q2 −p2| + ǫx|q2 −q1|
≤
c
p
n(n + 1) + c
2
√n + 1
ǫ
≤
c(n + 1
2) + 1
2
√n + 1
ǫ
=
c
√
n + 1ǫ.
This ﬁnishes the induction.
C. Robustness of Non-sp Circuits
Here we extend our discussion to the case of general
stochastic switching circuits. We have the following theorem,
which clearly holds for sp and ssp circuits:
Theorem 5 (Upper bound for general circuits). Given a gen-
eral stochastic switching circuit with n pswitches taken from
a ﬁnite pswitch set S, if each pswitch has error probability
bounded by ǫ, then the total probability of the circuit is
bounded by nǫ.
Proof: We ﬁrst index all the pswitches in the circuit C
as x1, x2, . . . , xn, see Fig. 6 as an example.
Let ti+ǫi be the probability that xi is closed, where ǫi is the
error part such that |ǫi| ≤ǫ. Let P (k) denote the probability
that C is closed when we only take into account the errors of
x1, x2, . . . , xk, i.e.,
P (k) = P(t1 + ǫ1, . . . , tk + ǫk, tk+1, . . . , tn),
where P(a1, a2, . . . , an) indicates the probability of C if xi
is closed with probability ai for all 1 ≤i ≤n.
1x
2x
3x
4x
5x
Fig. 6.
An example of a general stochastic switching circuit.
The overall error probability of the circuit C can then be
written as
e
=
P (n) −P(0)
=
(P (n) −P (n−1)) + (P (n−1) −P (n−2)) + · · ·
+(P (1) −P (0)).
Now, we prove that |P (k) −P (k−1)| ≤ǫ for all 1 ≤k ≤n
|P (k) −P (k−1)|
=
|P(t1 + ǫ1, . . . , tk + ǫk, tk+1, . . . , tn)
−P(t1 + ǫ1, . . . , tk−1 + ǫk−1, tk, . . . , tn)|
=
|(tk + ǫk)P(t1 + ǫ1, . . . , 1, tk+1, . . . , tn)
+(1 −tk −ǫk)P(t1 + ǫ1, . . . , 0, tk+1, . . . , tn)
−tkP(t1 + ǫ1, . . . , tk−1 + ǫk−1, 1, . . . , tn)
−(1 −tk)P(t1 + ǫ1, . . . , tk−1 + ǫk−1, 0, . . . , tn)|
=
|ǫk[P(t1 + ǫ1, . . . , 1, tk+1, . . . , tn)
−P(t1 + ǫ1, . . . , 0, tk+1, . . . , tn)]|
≤
ǫ.
Therefore, we have
e ≤
n
X
k=1
|P (k) −P (k−1)| ≤nǫ,
as we wanted.
Note that in most of cases, the actual error probability of a
circuit is much smaller than nǫ when n is large. However, nǫ
is still achievable in the following case: by placing n pswitches
with probability p −ǫ in series, where ǫ →∞, we can get a
circuit whose probability is
(p −ǫ)n ≈pn −npn−1ǫ.
Without considering the errors, the probability of the circuit
is pn, so the overall error is n·pn−1ǫ. Choosing p sufﬁciently
close to 1, we can make the error probability of the circuit
arbitrarily close to nǫ.
IV. EXPRESSIBILITY
In the previous section, we showed that ssp circuits are
robust against noise. This property is important in natural
systems and useful in engineering system design, because
the local error of a system should not be ampliﬁed. In this
section, we consider another property of stochastic switching


## Page 7


7
TABLE I
THE EXPRESSIBILITY OF STOCHASTIC SWITCHING CIRCUITS
S = { 1
q , 2
q , . . . , q−1
q }
Can all
a
qn be realized?
upper bound of circuit size
q is even
yes, ssp circuit
⌈log2 q⌉(n −1) + 1
q is an odd multiple of 3
yes, ssp circuit
⌈log3 q⌉(n −1) + 1
q is a prime number larger than 3
no, not by sp circuits
–
other values of q
open problem
–
circuits, called expressibility. Namely, given a pswitch set
S = { 1
q , 2
q , . . . , q−1
q } for some integer q, the questions we
ask are: What kinds of probabilities can be realized using
stochastic switching circuits (or only ssp circuits)? How many
pswitches are sufﬁcient? Wilhelm and Bruck [15] proved that
if q = 2 or q = 3, all rational
a
qn , with 0 < a < qn, can be
realized by an ssp circuit with at most n pswitches, which is
optimal. They also showed that if q = 4, all rational
a
qn , with
0 < a < qn, can be realized using at most 2n −1 pswitches.
In this section we generalize these results:
1) If q is an even number, all rational
a
qn , with 0 <
a < qn, can be realized by an ssp circuit with at most
⌈log2 q⌉(n −1) + 1 pswitches (Theorem 7).
2) If q is odd and a multiple of 3, all rational
a
qn , with
0 < a < qn, can be realized by an ssp circuit with at
most ⌈log3 q⌉(n −1) + 1 pswitches (Theorem 8).
3) However, if q is a prime number greater than 3, there
exists at least one rational
a
qn , with 0 < a < qn, that
cannot be realized using an sp circuit (Theorem 11).
Table I summarizes these results. We see that when q = 2, 3,
or 4, our results agree with the results in [15].
A. Backward Algorithms
As mentioned in [15], switching circuits may be synthesized
using forward algorithms, where circuits are built by adding
pswitches sequentially, or backward algorithms, where circuits
are built starting from the “outermost” pswitch.
Fig. 7 gives a simple demonstration of a backward al-
gorithm. Assume that the desired probability is p1 and we
plan to insert three pswitches, namely x1, x2, x3 in backward
direction. Here, for simplicity, we use x1, x2, x3 to denote
the closure probabilities of the pswitches, rather than their
states (1 or 0). If x1 ≤p1, then x1 has to be inserted in
parallel. If x1 > p1, then x1 has to be inserted in series.
After the insertion, we can try to realize the inner box with
probability p2 such that p2 + x1 −p2x1 = p1. This process
is continued recursively until for some m, pm can be realized
with a single pswitch. Generally, in backward algorithms, we
use xk to denote the kth pswitch inserted in the backward
direction, and use pk to denote the probability that we want
to realize with pswitches xk, xk+1, xk+2, . . .
Backward algorithms have signiﬁcant advantages over for-
ward algorithms for probability synthesis. In a forward algo-
rithm, if we want to add one pswitch, we have 2|S| choices,
since each pswitch may be added in either series or parallel.
But in a backward algorithm, if we want to insert one pswitch,
we have only |S| choices. That is because the insertion (series
or parallel) of a pswitch xk simply depends on the comparison
1p
(a) Step 1: We assume that the de-
sired probability is p1.
2
p
1x
(b) Step 2: Insert x1 in parallel as
the last pswitch. Now we try to re-
alize p2 such that p2+x1−p2x1 =
p1.
3p
1x
2x
(c) Step 3: Insert x2 in series as
the last pswitch. Now we try to
realize p3 such that p3x2 = p2.
1x
2x
3x
(d) Last step: Replace p3 with a
single pswitch x3.
Fig. 7.
An example of the backward algorithm.
of xk and pk. Therefore, backward algorithms can signiﬁcantly
reduce the search space, hence are more efﬁcient than forward
algorithms. In this paper, most of the circuit constructions are
based on backward algorithms.
B. Multiples of 2 or 3
We consider the case that S = { 1
q , 2
q , . . . , q−1
q } and q is
a multiple of 2 or 3. We show that based on a backward
algorithm, all rational
a
qn , with 0 < a < qn, can be realized
using a bounded number of pswitches. Before describing the
details, we introduce a characteristic function called d for a
given probability
b
qw , that is
d
 b
qw

=
qw−1
gcd(b, qw−1).
Note that the function d is well deﬁned, i.e., the value of d
is unchanged when both b and qw are multiplied by the same
constant. From the deﬁnition of the characteristic function d,
we see that for any rational
a
qn with 0 < a < qn, d is a
positive integer. In each iteration of the algorithm, we hope to
reduce d(pk) such that it can reach 1 after a certain number of
iterations. If d = 1, this means the desired probability can be
realized using a single pswitch and the construction is done.
During this process, we keep each successive probability pk
in the form of
b
qw , since only this kind of probabilities can


## Page 8


8
100
71
1  
p
(a) Step 1 with d(p1) = 10.
3
2
10
275
 
p
10
6
(b) Step 2 with d(p2) = 4.
10
6
10
5
2
3
10
55
 
p
(c) Step 3 with d(p3) = 2.
10
6
10
5
10
5
10
1
4  
p
(d) Step 4 with d(p4) = 1.
Fig. 8.
The procedure to realize
71
100 for a given pswitch set S
=
{ 1
10 , 2
10 , . . . , 9
10 }.
be realized with the pswitch set S. Now, we describe the
algorithm as follows.
Algorithm 1 (Backward algorithm to realize p1 =
a
qn with
0 < a < qn and pswitch set S = { 1
q , 2
q , . . . , q−1
q }).
1) Set k = 1, starting with an empty circuit.
2) Let
h(xk, pk) =

pk
xk
if xk > pk (series),
pk−xk
1−xk
if xk < pk (parallel).
We ﬁnd the optimal xk ∈S that minimizes d(pk+1) with
pk+1 = h(xk, pk). If pk+1 =
b
qw , then
d(pk+1) = d
 b
qw

=
qw−1
gcd(b, qw−1).
3) Insert pswitch xk to the circuit. If xk > pk, the pswitch
is inserted in series; otherwise, it is inserted in parallel.
Then we set pk+1 = h(xk, pk).
4) Let k = k + 1.
5) Repeat steps 2–4 until pk can be realized using a single
pswitch. Then insert pk into the circuit.
In Algorithm 1, the characteristic function d(pk) strictly
decreases as k increases, until it reaches 1. Finally, pk can
be replaced by a single pswitch and the construction is done.
Fig. 8 gives an example of a circuit realized by this algorithm.
At the beginning, we have p1 =
71
102 , with d(p1) = 10.
Then we add the “best” pswitch to minimize d(p2), where the
optimal pswitch is
6
10. Since
6
10 <
71
100, we insert the pswitch
in parallel, making d(p2) = 4. Repeating this process, we have
p1 = 71
102 , p2 = 275
103 , p3 = 55
102 , p4 = 1
10,
with corresponding characteristic functions
d(p1) = 10, d(p2) = 4, d(p3) = 2, d(p4) = 1.
In the following theorem, we show that if q is a multiple
of 2 or 3, then Algorithm 1 realizes any rational
a
qn with
0 < a < qn.
)
,
(
kp
x
h
2
1
 
x
kp
(a) d(pk) is even and pk < 1
2 .
)
,
(
kp
x
h
2
1
 
x
kp
(b) d(pk) is even and pk > 1
2.
)
,
(
kp
x
h
q
x
s2
 
kp
(c) d(pk) is odd and pk < 1
2.
)
,
(
kp
x
h
q
q
x
s2
 
!
kp
(d) d(pk) is odd and pk > 1
2 .
Fig. 9.
When q is even, the way to add a pswitch x ∈S such that
d(h(x, pk)) < d(pk).
Theorem 6. Given a pswitch set S = { 1
q , 2
q , . . . , q−1
q }, if q
is a multiple of 2 or 3, then Algorithm 1 realizes any rational
a
qn with 0 < a < qn, using an ssp circuit with a ﬁnite number
of pswitches.
Proof: The characteristic function d(p1) of the initial
probability p1 is bounded by qn−1. We only need to prove that
there exists an integer m such that d(pm) = 1, i.e., pm can be
realized by a single pswitch. Hence the desired probability p1
can be realized by an ssp circuit with m pswitches. It is enough
to show that the characteristic function d(pk) decreases as k
increases.
First, we consider the case where q is even. We will
show that for any pk =
b
qw , there exists x ∈S such that
d(h(x, pk)) < d(pk). See Fig. 9, depending on the values
of pk and d(pk), we have four different cases of inserting a
pswitch x such that d(h(x, pk)) < d(pk).
1) If d(pk) is even and pk < 1
2, let x = 1
2 and insert the
pswitch in series.
2) If d(pk) is even and pk > 1
2, let x = 1
2 and insert the
pswitch in parallel.
3) If d(pk) is odd and pk < 1
2, let x = 2s
q with s = ⌊log2 q⌋
and insert the pswitch in series.
4) If d(pk) is odd and pk > 1
2, let x =
q−2s
q
with s =
⌊log2 q⌋and insert the pswitch in parallel.
By checking all the cases to insert a pswitch, it is straight-
forward to see that when d(pk) is even, d(h(x, pk)) ≤1
2d(pk),
and when d(pk) is odd,
d(h(x, pk)) ≤
2sd(pk)
gcd(q, 2sd(pk)) < d(pk).
Since xk is optimal in each step of Algorithm 1, we have
d(pk+1) = d(h(xk, pk)) ≤d(h(x, pk)) < d(pk).
Finally, we can conclude that when q is even, there exists
an integer m such that d(pm) = 1. Consequently, p1 can be
realized with at most m pswitches.


## Page 9


9
2
3
4
5
6
7
8
9
10
0
1
2
3
4
5
6
q
Average pswitch number
optimal size=3
optimal size=4
optimal size=5
Fig. 10.
For each q, the average number of pswitches used in Algorithm 1
to realize the rational probabilities when their optimal size is n.
Similarly, when q is odd and a multiple of 3, if pk =
b
qw ,
we can always insert a pswitch x ∈S such that d(h(x, pk)) <
d(pk), as follows:
1) If d(pk) mod 3 = 0 and pk ≤1
3, let x = 1
3, and insert
the pswitch in series.
2) If d(pk) mod 3 = 0 and 1
3 < pk ≤2
3 with even b, let
x = 2
3, and insert the pswitch in series.
3) If d(pk) mod 3 = 0 and 1
3 < pk ≤2
3 with odd b, let
x = 2
3, and insert the pswitch in parallel.
4) If d(pk) mod 3 = 0 and pk > 2
3, let x = 2
3, and insert
the pswitch in parallel.
5) If d(pk) mod 3 ̸= 0 and pk ≤
1
3, let x =
3s
q
with
s = ⌊log3 q⌋, and insert the pswitch in series.
6) If d(pk) mod 3 ̸= 0 and 1
3 < pk ≤2
3 with even b, let
x = 2·3s
q
with s = ⌊log3 q⌋, and insert the pswitch in
series.
7) If d(pk) mod 3 ̸= 0 and 1
3 < pk ≤2
3 with odd b, let
x = q−2·3s
q
with s = ⌊log3 q⌋, and insert the pswitch in
parallel.
8) If d(pk) mod 3 ̸= 0 and pk > 2
3, let x = q−3s
q
with
s = ⌊log3 q⌋, and insert the pswitch in parallel.
Finally, we can conclude that p1 can be realized with a ﬁnite
number of pswitches when q is odd and a multiple of 3.
For each value q ∈{2, 3, 4, 6, 8, 9, 10}, we enumerate all
rational numbers with optimal size n ∈(3, 4, 5). Here, we
say that a desired probability is realized with optimal size if
it cannot be realized with fewer pswitches. As a comparison,
we use Algorithm 1 to realize these rational numbers again.
Fig. 10 presents the average number of pswitches required
using Algorithm 1 when the optimal size is n. It is shown
that when q is a multiple of 2 or 3, Algorithm 1 can construct
circuits with almost optimal size.
The next theorem gives an upper bound for the size of the
circuits when q is even.
Theorem 7 (Upper bound of circuit size when q is even).
Suppose q is even. Given a pswitch set S = { 1
q , 2
q , . . . , q−1
q },
any rational
a
qn with 0 < a < qn can be realized by an ssp
circuit, using at most ⌈log2 q⌉(n −1) + 1 pswitches.
Proof: In order to achieve this upper bound, we use
a modiﬁed version of Algorithm 1. Instead of inserting the
optimal pswitch xk, we insert the pswitch x described in Fig. 9
as the kth pswitch. The resulting characteristic function has the
following properties:
(1) d(pk) decreases as k increases, and when d(pm) = 1
for some m, the procedure stops.
(2) If d(pk) is even, then d(pk+1) is a factor of d(pk)
2
.
(3) If d(pk) is odd, then d(pk+1) is a factor of
2sd(pk)
gcd(q,2sd(pk)).
We deﬁne
N = min{k|k ∈(1, 2, 3, . . .), d(pk) = 1},
then N is the number of required pswitches. We only need to
prove that N ≤⌈log2 q⌉(n −1) + 1. Since q is even, we can
write q = 2c or q = 2ct, where t > 1 is odd.
Let us ﬁrst consider the case of q = 2c. At the beginning,
d(p1) is a factor of qn−1, so according to property (2), we can
get
N ≤c(n −1) + 1 = ⌈log2 q⌉(n −1) + 1.
In the case of q = 2ct, let us deﬁne a set M as
M = {k|k > 0, d(pk) is odd},
and let Mi be the ith smallest element in M. According to
properties (2) and (3) and the fact that d(p1) is a factor of
qn−1, we see that d(pMi) is a factor of qn−i. Therefore, there
exits a minimal k, with k ≤n, such that d(pMk) = 1. Then
N = Mk.
Based on properties (2) and (3), we also see that
M1 ≤c(n −1) + 1,
and
Mi+1 −Mi ≤s −c.
Therefore,
N
≤
n−1
X
i=1
(Mi+1 −Mi) + M1 ≤s(n −1) + 1
=
⌈log2 q⌉(n −1) + 1.
This completes the proof.
Using the similar methods, we can prove the following
theorems as well when q is a multiple of 3 or 6. Note that
Theorem 7 also applies to the case that q is a multiple of 6,
but Theorem 9 provides a tighter upper bound.
Theorem 8 (Upper bound of circuit size when q is odd and
a multiple of 3). Given a pswitch set S = { 1
q , 2
q , . . . , q−1
q },
if q is odd and a multiple of 3, then any rational
a
qn with
0 < a < qn can be realized using an ssp circuit with at most
⌈log3 q⌉(n −1) + 1 pswitches.
Theorem 9 (Upper bound of circuit size when q is a multiple
of 6). Given a pswitch set S = { 1
q , 2
q , . . . , q−1
q }, if q is


## Page 10


10
multiple of 6, all rational
a
qn with 0 < a < qn can be realized
by an ssp circuit with at most N pswitches, where
N ≤







(2s)(n −1) + 1
(if 6s = q),
(2s + 1)(n −1) + 1
(if q
2 ≤6s < q),
(2s + 2)(n −1) + 1
(if q
3 ≤6s < q
2),
(2s + 3)(n −1) + 1
(if q
6 < 6s ≤q
3).
C. Prime Number Larger Than 3
We proved that if q is a multiple of 2 or 3, all rational
a
qn
can be realized with a ﬁnite number of pswitches. We want to
know whether this result also holds if q is an arbitrary number
greater than 2. Unfortunately, the answer is negative.
Lemma 10. Suppose q is a prime number. Given a pswitch
set S = { 1
q , 2
q , . . . , q−1
q }, if a rational
a
qn cannot be realized
by an sp circuit with n pswitches, then it cannot be realized
using an sp circuit with any number of pswitches.
Proof: Assume there exits a rational
a
qn which cannot be
realized by an sp circuit with n pswitches, but can be realized
with at least l > n pswitches. Further, suppose that this l is
minimal for all rationals with denominator qk. Under these
assumptions, we will prove that there exists a rational
a′
qn′
which cannot be realized with n′ pswitches but can be realized
with l′ pswitches such that l′ < l. This conclusion contradicts
the assumption that l is minimal.
According to the deﬁnition of sp circuits, we know that
a
qn
can be realized by connecting two sp circuits C1 and C2 in
series or in parallel. Assume C1 consists of l1 pswitches and
is closed with probability b1
ql1 , and C2 consists of l2 pswitches
and is closed with probability
b2
ql2 , where l1 + l2 = l.
If C1 and C2 are connected in series, we can get
b1
ql1 · b2
ql2 = a
qn .
Therefore, b1b2 = aql−n, where b1b2 is a multiple of q.
Since q is a prime number, either b1 or b2 is a multiple of q.
Without loss of generality, assume b1 is a multiple of q, and we
write b1 = cq. Consider the probability
c
ql1−1 , which can be
realized with C1, using l1 pswitches. Assume that the same
probability can also be realized with another sp circuit C3,
using l1−1 pswitches. By connecting C3 and C2 in series, we
can realize
a
qn with l1 −1+l2 = l−1 pswitches, contradicting
the assumption that
a
qn cannot be realized with less than l
pswitches. Therefore, we see that
c
ql1−1 cannot be realized
with l1 −1 pswitches, but it can be realized with l1 pswitches.
Since l1 < l, this also contradicts our assumption that l is
minimal.
If C1 and C2 are connected in parallel, we have
b1
ql1 + b2
ql2 −b1
ql1 · b2
ql2 = a
qn .
Therefore, b1b2 = b1ql2 + b2ql1 −aql−n. Using a similar
argument as above, we can conclude that either b1 or b2 is a
multiple of q. Then either (1) a
ql can be realized with less than
l pswitches or (2) l is not optimal, yielding a contradiction.
This proves the lemma.
Based on the lemma above, it is easy to get the following
theorem.
Theorem 11 (When q is a prime number larger than 3). For
a prime number q > 3, there exists an integer a, with 0 <
a < qn, such that
a
qn cannot be realized using an sp circuit
whenever n ≥2.
Proof: The conclusion follows Lemma 10 and the following
result in [15]: For any q > 3, no pswitch set containing all a
q ,
with 0 < a < q, can realize all Pr(C) =
b
q2 , with 0 < b < q2,
using at most 2 pswitches.
V. PROBABILITY APPROXIMATION
In this section, we consider a general case where given an
arbitrary pswitch set, we want to realize a desired probability.
Clearly, not every desired probability pd can be realized
without any error using a ﬁnite number of pswitches for
a ﬁxed pswitch set S. So the question is whether we can
construct a circuit with at most n pswitches such that it can
approximate the desired probability very well. Namely, the
difference between the probability of the constructed circuit
and the desired probability should be as small as possible.
A. Greedy Algorithm
Given an arbitrary pswitch set S with |S| ≥2, it is not easy
to ﬁnd the optimal circuit (ssp circuit) with n pswitches which
approximates the desired probability pd. As we discussed in
the last section, a backward algorithm provides |S| choices
for each successive insertion. To ﬁnd the optimal circuit, we
may have to search through |S|n different combinations. As
|S| or n increases, the number of combinations will increase
dramatically. In order to reduce the search space, we propose a
greedy algorithm: In each step, we insert m pswitches, which
are the “best” locally. Normally, m is a very small constant.
Since each step has complexity |S|m, the total number of
possible combinations is reduced to |S|m n
m, which is much
smaller than |S|n when |S| ≥2 and n is large. Now, we
describe this greedy algorithm brieﬂy. The same notations
x1, x2, . . . and p1, p2, . . . are used, as those described for the
backward algorithms: xk indicates the kth pswitch inserted
and pk indicates the desired probability of the subcircuit
constructed by xk, xk+1, . . .
Algorithm 2 (Greedy algorithm with step-length m).
1) Assume that the desired probability is p1. Set k = 1 and
start with an empty circuit.
2) Select the optimal xm = (x1, x2, . . . , xm) ∈Sm to
minimize f(xm, S, pk), which will be speciﬁed later, and
this xm is denoted as x∗= (x∗
1, x∗
2, . . . , x∗
m).
3) Insert m pswitches x∗
1, x∗
2, . . . , x∗
m one by one into
the circuit in backward direction. During this process,
calculate pk+1, pk+2, . . . , pk+m one by one and update
k as k + m.
4) Repeat steps 2 and 3 for ⌊n
m⌋times.
5) Construct a new circuit with n −⌊n
m⌋m pswitches such
that its probability is closest to pk, then replace pk with
this new circuit.


## Page 11


11
So far, according to the backward algorithm described in
Section IV-A, we know how to ﬁnish step 3, including how
to insert m pswitches one by one into a circuit in a backward
direction, and how to update pk. The only thing unclear in the
procedure above is the expression of f(xm, S, pk).
In order to get a good expression for f(xm, S, pk), we study
how errors propagate in a backward algorithm. Note that in
a backward algorithm, we insert pswitches x1, x2, . . . , xn one
by one: if xk > pk, then xk is inserted in series; if xk <
pk, then xk is inserted in parallel. Now, given a circuit C
with size n constructed using a backward algorithm, we let
C(k) denote the subcircuit constructed by xk1, xk1+1, . . . , xn
and call |P(C(k)) −pk| as the approximation error of pk,
denoted by ek. In the following theorem, we will show how
ek1 affects that of ek2 for k2 < k1 after inserting pswitches
xk2, . . . , xk1−1.
Lemma 12. In a backward algorithm, let pk denote the
desired probability of the subcircuit C(k) constructed by
xk, xk+1, . . . , xn, and let ek denote the approximation error
of pk. Then for any k2 < k1 ≤n, we have
ek2 =
 k2−1
Y
i=k1
r(xi)
!
ek1,
where
r(xi) =

xi
if xi is inserted in series,
1 −xi
if xi is inserted in parallel.
Proof: We only need to prove that for any k less than the
circuit size, the following result holds:
ek = r(xk)ek+1.
When xk = pk, we have ek = ek+1 = 0, so the result is
trivial.
When xk > pk, then xk is inserted in series. In this case,
we have
pk+1xk = pk,
and
P(C(k+1))xk = P(C(k)).
As a result, the approximation error of pk is
ek
=
|P(C(k)) −pk|
=
|P(C(k+1))xk −pk+1xk|
=
xkek+1.
When xk < pk, then xk is inserted in parallel. In this case,
we have
pk+1 + xk −pk+1xk = pk,
and
P(C(k+1)) + xk −P(C(k+1))xk = P(C(k)).
As a result, the approximation error of pk is
ek
=
|P(C(k)) −pk|
=
|P(C(k+1)) + xk −P(C(k+1))xk
−(pk+1 + xk −pk+1xk)|
=
(1 −xk)ek+1.
This completes the proof.
In each step of the greedy algorithm, our goal is to minimize
ek, the approximation error of pk. According to the lemma
above, we know that
ek =
 k+m−1
Y
i=k
r(xi)
!
ek+m,
where the term ek+m is unknown. But we can minimize
Qk+m−1
i=k
r(xi) such that ek is as small as possible.
Based on the above discussion, we express f(x, S, pk) as
f(x, S, pk) =
m
Y
i=1
r(xi),
(1)
with
r(xi) =

xi
if xi is inserted in series,
1 −xi
if xi is inserted in parallel.
In the rest of this section, based on this expression for
f(x, S, pk), we show that the greedy algorithm has good
performance in reducing the approximation error of pd.
B. Approximation Error when |S| = 1
When S has only one element, say S = {p}, the greedy
algorithm above can become really simple. If pk > pk, then
we insert one pswitch in parallel; otherwise, we insert it in
series. Fig. 11 demonstrates how to approximate 1
2 using four
pswitches with the same probability 1
3. Initially, p1 = 1
2 > 1
3,
so we insert 1
3 in parallel. As a result, p2 =
1
2 −1
3
1−1
3 = 1
4 < 1
3, so
we insert the second pswitch in series. The ﬁnal probability
of the circuit in Fig. 11 is 37
81, which is close to 1
2.
1/3
1/3
1/3
1/3
Fig. 11.
This circuit approximates 1
2 using 4 pswitches of probability 1
3 .
Note that in the greedy algorithm, when p is close to 1
2,
the probability of the resulting circuit will quickly converge
to the desired probability. But when p is close to 0 or 1, the
convergence speed is slower. In the following theorem, we
provide an upper bound for the approximation error of the
desired probability when |S| = 1.
Theorem 13 (Approximation error when |S| = 1). Given n
pswitches, each with probability p, and a desired probability
pd, the greedy algorithm (Algorithm 2) with m = 1 generates
an ssp circuit C with approximation error
e = |pd −P(C)| ≤(max{p, 1 −p})n
2
,


## Page 12


12
where equality is achieved when
pd = fn(p) =
(
1 −(max{p,1−p})n
2
if p < 1
2,
(max{p,1−p})n
2
if p > 1
2.
Proof: In the following proof, we only consider the case
when p < 1
2. From duality, the result will also hold for p > 1
2.
We induct on the number of pswitches. For one pswitch, the
result is trivial: the worst-case desired probability is p + 1−p
2 ,
with approximation error 1−p
2 . Now assume the result of the
theorem holds for n pswitches, we want to prove that it also
holds for n + 1 pswitches.
Let p1 = pd be approximated with n + 1 pswitches using
Algorithm 2. At the beginning, one pswitch is inserted in series
if pd < p, or in parallel if pd > p. According to Lemma 12,
we know that the approximation error of p1 is
e1 = r(p)e2,
where r(p) ≤max{p, 1 −p}, and e2 is the approximation
error of p2. According to our assumption, we know that
e2 ≤(max{p, 1 −p})n
2
.
So we have
e1 ≤(max{p, 1 −p})n+1
2
.
Note that equality is achieved if r(p) = max{p, 1 −p} and
e2 = (max{p,1−p})n
2
. In this case, p2 = fn(p) ≥1
2 > p and
the last pswitch is inserted in parallel. As a result, we have
fn+1(p) = fn(p) + p −fn(p)p = 1 −(1 −p)n+1
2
as described in the theorem. This completes the proof.
If we let p = 1
2, the theorem shows that for any desired
probability pd and any integer n, we can ﬁnd an ssp circuit
with n pswitches to approximate pd, such that the approxi-
mation error is at most
1
2qn . This agrees with the result in
[15]: Given a pswitch set S = { 1
2}, all rational
a
2n , with
0 < a < qn, can be realized using at most n pswitches.
C. Approximation Error when |S| > 1
In this subsection, we show that using the greedy algorithm
(Algorithm 2) with small m, such as 1 or 2, we can construct
a circuit to obtain a good approximation of any desired
probability. Here, given a pswitch set S = {s1, s2, . . . , s|S|},
we deﬁne its maximal interval ∆as
∆=
|S|
max
i=0 |si+1 −si|,
where we let s0 = 0 and s|S|+1 = 1. In the following
theorems, we will see that the approximation error of the
greedy algorithm depends on ∆, and can decrease rapidly as
n increases.
Let us ﬁrst consider the case m = 1:
Theorem 14 (Approximation error for m = 1). Assume we
have the pswitch set S = {s1, s2, . . . , s|S|} with maximal
interval ∆. For any desired probability pd and any integer
n, Algorithm 2 with m = 1 yields an ssp circuit with at most
n pswitches, such that the approximation error e satisﬁes
e ≤∆
2
(3 + ∆)∆
2
⌈n
2 ⌉−1
.
Proof: In the following proof, we only consider the case
that n is odd. If the result holds for odd n, then the result
will also hold for even n. In order to simplify the proof, we
assume that s0 = 0 and s|S|+1 = 1 also belong to S; i.e.,
there are pswitches with probability 0 or 1. This assumption
will not affect our conclusion.
We write n = 2k + 1 and induction on k. When k = 0, the
result is trivial, since the approximation error of one pswitch
satisﬁes e ≤∆
2 . Assume the result holds for 2k+1 pswitches.
We want to show that the result also holds for 2(k + 1) + 1
pswitches.
When m = 1 in the greedy algorithm, if we want to
approximate p1 = pd with 2(k + 1) + 1 pswitches, we should
insert a pswitch with probability arg minx f(x, S, p1) in the
ﬁrst step, where f(x, S, p1) is deﬁned in (1).
Let xupper = min{x ∈S|x > p1} and xlower = max{x ∈
S|x < p1}. Since 0 ∈S and 1 ∈S, we know that xupper and
xlower exist.
(1) We ﬁrst consider the case that 1 −xlower ≤xupper.
In this case, we insert xlower in parallel as the ﬁrst pswitch.
Therefore, we can get
p2 = p1 −xlower
1 −xlower
.
According to the deﬁnition of ∆, there exists a pswitch
x ∈S such that p2 ≤x < p2 + ∆. Assume in the algorithm,
we insert pswitch x∗as the second one. Since x∗is locally
optimal, we have
f(x∗, S, p2) ≤f(x, S, p2) < p2 + ∆.
Assume the approximation error of p3 is e3. According to
Lemma 12, we know that the approximation error of p1 = pd
is
e1
≤
(p2 + ∆)(1 −xlower)e3
=
(p1 −xlower
1 −xlower
+ ∆)(1 −xlower)e3
=
((p1 −xlower) + ∆(1 −xlower))e3
≤
∆(2 −xlower)e3
≤
∆(3 + xupper −xlower)
2
e3
≤
∆(3 + ∆)
2
e3.
According to our assumption,
e3 ≤∆
2 ((3 + ∆)∆
2
)k.
So
e1 ≤∆
2 ((3 + ∆)∆
2
)k+1.
This completes the induction.


## Page 13


13
(2) When 1 −xlower > xupper, we insert xupper in series as
the ﬁrst pswitch. Using a similar argument as above, we can
also prove that
e1 ≤∆
2 ((3 + ∆)∆
2
)k+1.
This completes the proof.
In the next theorem, we show that if we increase m from
1 to 2, the upper bound of the approximation error can be
reduced furthermore.
Theorem 15 (Approximation error for m = 2). Assume we
have the pswitch set S = {s1, s2, . . . , s|S|} with maximal
interval ∆. For any desired probability pd and any integer
n, Algorithm 2 with m = 2 yields an ssp circuit with at most
n pswitches, such that the approximation error e satisﬁes
e ≤∆
2
(2 + ∆)∆
2
⌈n
2 ⌉−1
.
Proof: As in the proof for m = 1, we only consider the
case when n is odd, so n = 2k + 1. In the proof, we use the
same notations as those in the case of m = 1, and assume S
includes 0 and 1.
Now we induct on k. When k = 0, the result of the theorem
is trivial. Assume the result holds for 2k + 1 pswitches; we
want to prove that it also holds for 2(k+1)+1 pswitches. Let
xupper = min{x ∈S|x > p1} and xlower = max{x ∈S|x <
p1}, we will consider two different cases as follows.
(1) If p1 ≤
xupper+xlower+∆(xupper+xlower−1)
2
, we consider
the following way to insert two pswitches: First insert x1 =
xlower in parallel, and we get
p2 = p1 −xlower
1 −xlower
.
There exists a pswitch x2 ∈S such that p2 ≤x2 < p2 + ∆.
Then we insert x2 in series as the second pswitch. In this case,
letting x = (x1, x2), we have
f(x, S, p1) ≤(p2 + ∆)(1 −xlower).
Let x∗= (x∗
1, x∗
2) be the two pswitches inserted by the
algorithm with m = 2, then the approximation error of p1 =
pd is
e1
=
f(x∗, S, p1)e3 ≤f(x, S, p1)e3
≤
(p2 + ∆)(1 −xlower)e3
=
p1 −xlower
1 −xlower
+ ∆

(1 −xlower)e3.
Since p1 ≤xupper+xlower+∆(xupper+xlower−1)
2
, we have
e1
≤
(xupper −xlower)(1 + ∆) + ∆
2
e3
≤
∆(2 + ∆)
2
e3.
According to our assumption, we have e3 ≤∆
2

(2+∆)∆
2
k
,
so
e1 ≤∆
2
(2 + ∆)∆
2
k+1
.
This completes the induction.
(2) If p1 >
xupper+xlower+∆(xupper+xlower−1)
2
, we consider
the following way to insert two pswitches: First insert x1 =
xupper in series, and we get
p2 =
p1
xupper
.
There exists a pswitch x2 ∈S such that p2 −∆≤x2 < p2.
Then we insert x2 in parallel as the second pswitch. In this
case, letting x = (x1, x2), we have
f(x, S, p1) ≤(1 −(p2 −∆))xupper.
Let x∗= (x∗
1, x∗
2) be the two pswitches inserted by the
algorithm with m = 2, then the approximation error of p1 =
pd is
e1
=
f(x∗, S, p1)e3
≤
f(x, S, p1)e3
≤
(1 −(p2 −∆))xuppere3
=
xupper −p1
xupper
+ ∆

xuppere3.
Since p1 > xupper+xlower+∆(xupper+xlower−1)
2
, we have
e1
≤
(xupper −xlower)(1 + ∆) + ∆
2
e3
≤
∆(2 + ∆)
2
e3.
Then we have the same result as the ﬁrst case.
According to the two theorems above, when we let ∆→
0, the approximation error for m = 1 is upper bounded by
∆
2
  3∆
2
k where k = ⌈n
2 ⌉−1; and the approximation error for
m = 2 is upper bounded by ∆
2 · ∆k. It shows that the greedy
algorithm has good performance in terms of approximation
error, even when m is very small. Comparing with the case of
m = 1, if we choose m = 2, the probability of the constructed
circuit can converge to the desired probability faster as the
circuit size n increases.
In the following theorem, we consider the special case S =
{ 1
q , 2
q , . . . , q−1
q } for some integer q. In this case, we obtain a
new upper bound for the approximation error when using the
greedy algorithm with m = 2. This bound is slightly tighter
than the one obtained in Theorem 15.
Theorem 16. Suppose S = { 1
q , 2
q , . . . , q−1
q } for some integer
q, with ∆= 1
q . For any desired probability pd and any integer
n, Algorithm 2 with m = 2 constructs an ssp circuit with at
most n pswitches such that its approximation error
e ≤∆
2 (∆(1 −∆))⌈n
2 ⌉−1 .
Proof: The proof is similar to the proof of Theorem 15,
so we simply provide a sketch. Assume that in each step, we
insert two pswitches in the following way (see Fig. 12):
(1) If pk ∈[0, 1
q ], we insert a pswitch x1 = 1
q in series, and
then insert a pswitch x2 = 1
q in series or in parallel. In this
case,
f
1
q , 1
q

, S, pk

≤1
q

1 −1
q

= ∆(1 −∆).


## Page 14


14
1
 
kp
q
1
(a) pk ∈[0, 1
q ].
q
q
1
 
1
 
kp
(b) pk ∈[ q−1
q , 1].
q
u
q
1
2
 
kp
(c) pk ∈[ u
q , u
q + 1
q −u2
q ] for some
u = {1, . . . , q −1}.
q
q
1
 
q
u
1
 
2
 
kp
(d) pk ∈[ u
q + 1
q −u2
q , u
q + 1
q ] for
some u = {0, 1, . . . , q −2}.
Fig. 12.
Inserting pswitches for different values of pk.
(2) If pk ∈[ q−1
q , 1], we insert a pswitch x1 =
q−1
q
in
parallel, and then insert a pswitch x2 = q−1
q
in series or in
parallel. In this case,
f
1
q , 1
q

, S, pk

≤1
q

1 −1
q

= ∆(1 −∆).
(3) If pk ∈[ u
q , u
q + 1
q −u2
q ] for some u = {1, . . . , q−1}, we
insert a pswitch x1 = u
q in parallel, and then insert a pswitch
x2 = 1
q in series. In this case,
f
u
q , 1
q

, S, pk

≤

1 −u
q
 1
q ≤∆(1 −∆).
(4) If pk ∈[ u
q + 1
q −u2
q , u
q + 1
q ] for some u = {0, 1, . . ., q−2},
we insert a pswitch x1 =
u+1
q
in series, and then insert a
pswitch x2 = q−1
q
in parallel. In this case,
f
u + 1
q
, q −1
q

, S, pk

≤
u + 1
q

1 −q −1
q

≤
∆(1 −∆).
Based on the above analysis, we know that for any pk ∈
(0, 1), we can always ﬁnd x = (x1, x2) such that
f((x1, x2), S, pk)) ≤∆(1 −∆).
Hence, the result of the theorem can be proved by induction.
This completes the proof.
Fig. 13 shows an example for demonstration. Assume
S = { 1
5, 2
5, 3
5, 4
5}, and suppose we want to realize
3
7 using
ﬁve pswitches. Using the greedy algorithm with m = 2, we
can get the circuit in Fig. 13, whose probability is 0.4278, and
approximation error is
e =

3
7 −0.4278
 = 7.3 × 10−4,
which is very small.
5
/
1
5
/
1
5
/
1
5
/
1
5
/
2
Fig. 13.
The circuit approximates 3
7 with 5 pswitches from the pswitch set
S = { 1
5, 2
5 , . . . , 4
5}.
VI. CONCLUSION
In this paper, we have studied the robustness and synthesis
of stochastic switching circuits. We have shown that ssp cir-
cuits are robust against small error perturbations, while general
sp circuits are not. As a result, we focused on constructing
ssp circuits to synthesize or approximate probabilities. We
generalized the results in [15] and proved that when q is a
multiple of 2 or 3, all rational fractions
a
qn can be realized
using ssp circuits when the pswitch set S = { 1
q , 2
q , . . . , q−1
q }.
However, this property does not hold when q is a prime
number greater than 3. For a more general case of an arbitrary
pswitch set, we proposed a greedy algorithm to construct ssp
circuits. This method can approximate any desired probability
with low circuit complexity and small errors.
REFERENCES
[1] L. Chakrapani, P. Korkmaz, B. Akgul, and K. Palem, “Probabilistic
system-on-a-chip architecture,” ACM Transactions on Design Automa-
tion of Electronic Systems, vol. 12, no. 3, pp. 1–28, 2007.
[2] M. Cook, D. Soloveichik, E. Winfree, J. Bruck, “Programmability of
chemical reaction networks,” Algorithmic Bioprocesses, Natural Com-
puting Series, pp. 543–584, 2009.
[3] P. Elias, “The efﬁcient construction of an unbiased random sequence,”
Ann. Math. Statist., vol. 43, pp. 865–870, 1972.
[4] B. Fett, J. Bruck, and M. D. Riedel, “Synthesizing stochasticity in bio-
chemical systems,” in Proc. Annual Conference on Design Automation
(DAC), pp. 640–645, 2007.
[5] A. Gill, “Synthesis of probability transformers,” Journal of the Franklin
Institute, vol. 274, no. 1, pp. 1–19, 1962.
[6] A. Gill, “On a weight distribution problem, with application to the design
of stochastic generators,” Journal of the ACM, vol. 10, no. 1, pp. 110–
121, 1963.
[7] T. S. Han and M. Hoshi, “Interval algorithm for random number
generation,” IEEE Trans. Inform. Theory, vol. 43, No. 2, pp. 599–611,
1997.
[8] P. Jeavons, D. A. Cohen, and J. Shawe-Taylor, “Generating binary
sequences for stochastic computing,” IEEE Trans. Inform. Theory, vol.
40, no. 3, pp. 716–720, 1994.
[9] D. E. Knuth and A. Yao, “The complexity of nonuniform random
number generation,” Algorithms and Complexity: New Directions and
Recent Results, pp. 357–428, 1976.
[10] P. A. MacMahon, “The combinations of resistances,” The Electrician,
28:601–602, 1892. (Reprinted in: Discr. Appl. Math., 54:225–228,
1994.).
[11] W. Qian, M. D. Riedel, H. Zhou, and J. Bruck, “Transforming probabil-
ities with combinational logic,” IEEE Trans. on Computer-Aided Design
of Integrated Circuits and Systems, vol. 30, pp. 1279–1292, 2011.
[12] C. E. Shannon. “A symbolic analysis of relay and switching circuits,”
Trans. AIEE, 57:713–723, 1938.
[13] D. Soloveichik, G. Seelig, and E. Winfree, “DNA as a universal substrate
for chemical kinetics,” PNAS 107, pp. 5393–5398, 2010.


## Page 15


15
[14] J. von Neumann, “Various techniques used in connection with random
digits,” Appl. Math. Ser., Notes by G.E. Forstyle, Nat. Bur. Stand., vol.
12, pp. 36–38, 1951.
[15] D. Wilhelm and J. Bruck, “Stochastic switching circuit synthesis,” in
Proc. IEEE International Symposium on Information Theory (ISIT), pp.
1388–1392, 2008.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]