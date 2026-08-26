---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1604.04739v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1604.04739v1_Inconclusive_quantum_measurements_and_decisions_under_uncertainty

> Source: 1604.04739v1_Inconclusive_quantum_measurements_and_decisions_under_uncertainty.pdf

> Pages: 16

---


## Page 1


arXiv:1604.04739v1  [quant-ph]  16 Apr 2016
Inconclusive quantum measurements and decisions under
uncertainty
V.I. Yukalov1,2,∗and D. Sornette1,3
1ETH Z¨urich
Department of Management, Technology and Economics
Z¨urich, CH-8092, Switzerland
2Bogolubov Laboratory of Theoretical Physics,
Joint Institute for Nuclear Research, Dubna 141980, Russia
3Swiss Finance Institute, c/o University of Geneva,
40 blvd. Du Pont d’Arve, CH 1211 Geneva 4, Switzerland
Abstract
We give a mathematical deﬁnition for the notion of inconclusive quantum measure-
ments. In physics, such measurements occur at intermediate stages of a complex measure-
ment procedure, with the ﬁnal measurement result being operationally testable. Since the
mathematical structure of Quantum Decision Theory has been developed in analogy with
the theory of quantum measurements, the inconclusive quantum measurements correspond,
in Quantum Decision Theory, to intermediate stages of decision making in the process of
taking decisions under uncertainty. The general form of the quantum probability for a com-
posite event is the sum of a utility factor, describing a rational evaluation of the considered
prospect, and of an attraction factor, characterizing irrational, subconscious attitudes of
the decision maker. Despite the involved irrationality, the probability of prospects can be
evaluated. This is equivalent to the possibility of calculating quantum probabilities without
specifying hidden variables. We formulate a general way of evaluation, based on the use of
non-informative priors. As an example, we suggest the explanation of the decoy eﬀect. Our
quantitative predictions are in very good agreement with experimental data.
Keywords: quantum measurements, decision theory, inconclusive events, quantum probability,
non-informative priors, decoy eﬀect
∗Correspondence: V.I. Yukalov
Department of Management, Technology and Economics,
ETH Z¨urich (Swiss Federal Institute of Technology at Z¨urich),
Scheuchzerstrasse 7, Z¨urich CH-8092, Switzerland
E-mail: yukalov@theor.jinr.ru
1


## Page 2


1
Introduction
The standard theory of quantum measurements (von Neumann 1955) is based on the projection
operator measure corresponding to operationally testable events. Simple measurements really
have to be operationally testable in order to possess physical meaning. However if a measurement
is composite, consisting of several parts, the intermediate stages do not have to necessarily be
operationally testable, but can be inconclusive.
As a typical example, we can recall the known double-slit experiment, when particles pass
through a screen with two slits and then are registered by particle detectors some distance away
from the screen. This experiment can be treated as a composite event consisting of two parts, one
being the passage through one of the slits and second, registration by detectors. The registration
of a particle by a detector is an operationally testable event, since the particle is either detected
or not, with the result being evident for the observer. But the passage of the particle through
one of the slits is not directly observed, and the experimentalist does not know which of the
slits the particle has passed through. In that sense, the passage of the particle through a slit
is an inconclusive event. The existence of this inconclusive event, occurring at the intermediate
stage of the experiment, is intimately associated with an interference eﬀect. Otherwise, if the
experimentalist would precisely determine the slit through which the particle has passed, the
interference pattern registered by the particle detectors would be destroyed. The existence of
interference is precisely due to the presence of the inconclusive event that happened at the
intermediate stage.
The occurrence of inconclusive events in decision making is even more frequent and important.
Practically any decision, before it is explicitly formulated, passes through a stage of deliberation
and hesitation accompanying the choice. That is, any decision is actually a composite event
consisting of an intermediate stage of deliberation and of the ﬁnal stage of taking a decision.
The ﬁnal stage of decision making is equivalent to an operationally testable event in quantum
measurements. While the intermediate stage of deliberation is analogous to an inconclusive event.
The analogy between the theory of quantum measurements and decision theory has been
mentioned by von Neumann (1955). Following this analogy, Quantum Decision Theory (QDT)
has been advanced (Yukalov and Sornette, 2008,2009a,2010,2011,2014a,2015a), with the mathe-
matical structure that is applicable to both decision making as well as to quantum measurements.
The generality of our framework, being equally suitable for quantum measurements and decision
making, is its principal diﬀerence from all other attempts that employ quantum techniques in
psychological sciences. An extensive literature on various quantum models in psychology and
cognitive science can be found in the books (Khrennikov, 2010; Busemeyer and Bruza, 2012;
Bagarello, 2013; Haven and Khrennikov, 2013) and review articles (Yukalov and Sornette, 2009b;
Sornette, 2014; Ashtiani and Azgomi, 2015; Haven and Khrennikov, 2016).
Any approach, applying quantum techniques to decision theory, is naturally based on the
notion of probability. This is because quantum theory is intrinsically probabilistic. Respectively,
the intrinsically probabilistic nature of quantum decision theory is what makes it principally dif-
ferent from stochastic decision theory, where the choice is treated as always being deterministic,
while in the process of choosing the decision maker acts with errors (Hey, 1995; Loomes and
Sugden, 1998; Carbone and Hey, 2000; Hey, 2005; Conte et al., 2010). Such stochastic decision
theories can be termed as “deterministic theories embedded into an environment with stochastic
noise”. The standard way of using a stochastic approach is to assume a probability distribution
over the values characterizing the errors made by the subjects in the process of decision mak-
ing. Then the parameters entering the distribution are ﬁtted to a posteriori empirical data by
2


## Page 3


maximizing the log-likelihood function. Such a procedure allows one to better ﬁt the given set of
data to the assumed basic deterministic decision theory, in particular due to the introduction of
additional ﬁtting parameters. However, it does not essentially change the structure of the under-
lying deterministic theory, although improving it slightly. And, being descriptive, the classical
stochastic approach does not provide quantitative predictions.
Contrary to classical stochastic theory, in the quantum approach, we do not assume that the
choice of a decision maker is deterministic, with just some weak disturbance by errors. Follow-
ing the general quantum interpretation, we consider the choice process, including deliberations,
hesitations, and subconscious estimation of competing outcomes, as intrinsically random. The
probabilistic decision, in the quantum case, is not just a stochastic decoration of a deterministic
process, but it is an unavoidable random part of any choice. The existence of the hidden, often
irrational subconscious feelings and deliberations, results in the appearance of quantum interfer-
ence and entanglement. The diﬀerence between classical stochastic decision theory and quantum
decision theory is similar to the diﬀerence between classical statistical physics and quantum the-
ory. In the former, all processes are assumed to be deterministic, with statistics coming into play
because of measurement uncertainties, such as no precise knowledge of initial conditions and
the impossibility of measuring exactly the locations and velocities of all particles. In contrast,
quantum theory is principally probabilistic, which becomes especially important for composite
measurements.
A detailed mathematical theory of quantum measurements in the case of composite events
has been developed in our previous papers (Yukalov and Sornette, 2013, 2015b, 2016). In the
present paper, we concentrate our attention on composite measurements including intermedi-
ate inconclusive events and on the application of this notion for characterizing decision making
under risk and uncertainty. The importance of composite events, including intermediate incon-
clusive events, in decision theory makes it necessary to pay a special attention to the correct
mathematical formulation of such events and to the description of their properties allowing for
the quantitative evaluation of the corresponding quantum probabilities. We show that, despite
uncertainty accompanying inconclusive events, it is possible to give quantitative evaluations for
quantum probabilities in decision theory, based on non-informative priors. Considering, as an
illustration, the decoy eﬀect, we demonstrate that even the simple non-informative priors provide
predictions in very good agreement with experimental data.
2
Composite quantum measurements and events
In this section, we give a brief summary of the general scheme for deﬁning quantum probabilities
for composite events. As we have stressed above, in our approach, the mathematics is the same
for describing either quantum measurements or decision making. Therefore, when referring to
an event, we can keep in mind either a fact of measurement or a decision action.
Let An be a conclusive operationally testable event labelled by an index n. And let B = {Bα}
be a set of inconclusive events labelled by α. Deﬁning the space of events as a Hilbert space H,
we associate with an event An a state |n⟩in this Hilbert space and an event operator ˆPn,
An →|n⟩→ˆPn = |n⟩⟨n| .
(1)
The event operator for an operationally testable event is a projector.
The set of inconclusive events B generates in the Hilbert space H the state |B⟩and the event
operator ˆPB,
B →|B⟩→ˆPB = |B⟩⟨B| ,
(2)
3


## Page 4


where the state reads
|B⟩=
X
α
bα|α⟩,
(3)
with coeﬃcients bα being random complex numbers. The event operator for an inconclusive event
is not necessarily a projector, but a member of a positive operator-valued measure (Yukalov and
Sornette, 2013, 2015a,b, 2016).
The space of events, in the quantum approach, is the Hilbert space
H = HA
O
HB
(4)
that is a tensor product of the spaces
HA = span{|n⟩} ,
HB = span{|α⟩} .
Each decision maker is characterized by an operator ˆρ that can be termed the strategic state of a
decision maker, which, in quantum theory, corresponds to a statistical operator. The pair {H, ˆρ},
in physics, is named a statistical ensemble, and in decision theory, it is a decision ensemble.
A composite event is called a prospect and is denoted as
πn = An
O
B .
(5)
A prospect πn generates a state |πn⟩in the Hilbert space of events H and a prospect operator
ˆPn,
πn →|πn⟩→ˆP(πn) = |πn⟩⟨πn| ,
(6)
with the prospect state
|πn⟩= |n⟩
O
|B⟩=
X
α
bα|nα⟩.
(7)
The prospect operator is a member of a positive operator-valued measure, which implies that
these operators satisfy the resolution of unity (Yukalov and Sornette, 2013, 2016). Since they
contain random quantities bα, the corresponding random resolution has to be understood not as
a direct equality between numbers, but, e.g., as the equality in mean (Kallenberg, 2001).
The prospect probability is
p(πn) = Tr ˆρ ˆP(πn) ,
(8)
with the trace over the space H. To form a probability measure, the prospect probabilities are
to be normalized:
X
n
p(πn) = 1 ,
0 ≤p(πn) ≤1 .
(9)
Taking explicitly the trace in expression (8) and separating diagonal and oﬀ-diagonal terms,
we see that the prospect probability
p(πn) = f(πn) + q(πn)
(10)
is represented as a sum of a positive-deﬁnite term
f(πn) =
X
α
|bα|2⟨nα|ˆρ|nα⟩
(11)
4


## Page 5


and a sign-undeﬁned term
q(πn) =
X
α̸=β
b∗
αbα⟨nα|ˆρ|nβ⟩.
(12)
The appearance of the sign-undeﬁned term is a purely quantum eﬀect responsible, in quantum
measurements, for interference patterns. The attenuation of this quantum term is called decoher-
ence. In quantum theory, decoherence can be due to external as well as to internal perturbations
and the inﬂuence of measurements (Yukalov, 2011, 2012a,b). And in quantum decision theory,
decoherence can occur due to the accumulation of information (Yukalov and Sornette, 2015c).
The disappearance of the quantum term implies the transition to classical theory. This is
formulated as the quantum-classical correspondence principle (Bohr, 1976), which in our case
reads as
p(πn) →f(πn) ,
q(πn) →0 .
(13)
This principle tells us that the term f(πn) plays the role of classical probability, hence is to be
normalized:
X
n
f(πn) = 1 ,
0 ≤f(πn) ≤1 .
(14)
When decisions concern a choice between lotteries, the classical term f(πn) has to be deﬁned
according to classical decision theory based either on expected utility theory or on some nonex-
pected value functional. This suggests to call f(πn) a utility factor, since it is deﬁned on rational
grounds and reﬂects the utility of a choice. The quantum term is caused by the interference
and entanglement eﬀects in quantum theory, which correspond, in decision making, to irrational
eﬀects describing the attractiveness of choice. Therefore it can be called the attraction factor.
From equations (9) and (14), it follows the alternation law
X
n
q(πn) = 0 ,
−1 ≤q(πn) ≤1 .
(15)
Note that, in quantum theory, the deﬁnition of the composite event in the form of prospect
(5) is valid for any type of operators, since they are deﬁned on diﬀerent spaces. No problem with
noncommutativity of operators deﬁned on a common Hilbert space arises. This way makes it
possible to introduce joint quantum probabilities for several measurements (Yukalov and Sornette,
2013, 2016). Contrary to this, considering operators on the same Hilbert space does not allow
one to deﬁne joint probabilities for noncommuting operators. Sometimes, one treats the L¨uders
probability of consecutive measurements as a conditional probability.
This, however, is not
justiﬁed from the theoretical point of view (Yukalov and Sornette, 2013, 2014b, 2016) and also
contradicts experimental data (Boyer-Kassem et al., 2015a,b). But deﬁning the quantum joint
probability according to expression (8) contains no contradictions.
In the present section, the general scheme of QDT is presented. Being limited by the length
of this paper, we cannot go into all mathematical details that have been thoroughly described
in our previous publications. However, we would like to stress that for the purpose of practical
applications, it is not necessary to study all these mathematical peculiarities, but it is suﬃcient
to employ the ﬁnal formulas following the prescribed rules. One can use the formulated rules
as given prescriptions, without studying their justiﬁcation. The main formulas of this section,
which are necessary for the following application, are: the form of the quantum probability (10),
the normalization conditions (9) and (14), and the alternation law (15). More details required
for practical application will be given in the sections below.
5


## Page 6


3
Non-informative prior for utility factors
To make the above scheme applicable to decision theory, it is necessary to specify how one should
quantify the values of the utility factors and attraction factors. Here we show how these values
can be deﬁned as non-informative priors.
Let us consider a set of lotteries Ln = {xi, pn(xi) : i = 1, 2, . . . , Nn}, enumerated by the index
n = 1, 2, . . . , NL, with payoﬀs xi and their probabilities pn(xi). The related expected utilities
U(Ln) = P
i u(xi)pn(xi) can be deﬁned according to the expected utility theory (von Neumann
and Morgenstern, 1953). For the present consideration, the utility functions u(x) do not need
to be speciﬁed. For instance, they can be taken as linear functions, since this choice has the
advantage of making the utility factors independent from the units measuring the payoﬀs.
In quantum decision theory, the act of choosing a lottery Ln, denoted as An, together with the
accompanying set of inconclusive events B, including the decision-maker hesitations (Yukalov and
Sornette, 2014a, 2014b), compose the prospect (5). Depending on whether the expected utilities
are positive on negative, there can be two cases.
If the expected utilities of the considered set of lotteries are all positive (non-negative), such
that
U(Ln) ≥0
(n = 1, 2, . . . , NL) ,
(16)
then it is reasonable to require that zero utility corresponds to zero utility factor:
f(πn) →0 ,
U(Ln) →0 .
(17)
The case where the utility factor is simply proportional to the related expected utility trivially
obeys this condition (17). Taking into account the normalization condition (14) gives the utility
factor
f(πn) =
U(Ln)
P
n U(Ln) .
(18)
When the expected utilities are negative, which happens in the domain of losses, such that
U(Ln) < 0
(n = 1, 2, . . . , NL) ,
(19)
the required condition is that an inﬁnite loss corresponds to zero utility factor:
f(πn) →0 ,
|U(Ln)| →∞.
(20)
The simplest way to satisfy this condition (20) is that the utility factor is inversely proportional
to the related expected utility. Taking into account the normalization condition, we get
f(πn) =
|U(Ln)|−1
P
n |U(Ln)|−1 .
(21)
The utility-factor forms (18) and (21) coincide with the choice probabilities in the Luce
choice axiom (Luce, 1959). It is possible to show that generalized forms for the utility factors
can be derived by maximizing a conditional Shannon entropy or from the principle of minimal
information (Yukalov and Sornette, 2009b; Frank, 2009; Batty, 2010).
In the case of positive expected utilities, we consider the information functional, taking into
account the normalization condition (14) and the expected log-likelihood Λ. This functional
reads as
I[ f(πn) ] =
X
n
f(πn) ln f(πn) + λ
"X
n
f(πn) −1
#
+ α
"X
n
f(πn)Λ(πn) −Λ
#
,
(22)
6


## Page 7


where
Λ(πn) = −ln U(Ln) ,
U(Ln) ≥0 .
Minimizing functional (22) results in the utility factor
f(πn) =
Uα(Ln)
P
n Uα(Ln)
(α > 0) ,
(23)
in which the positive sign of α is prescribed by the condition that the larger utility implies the
larger factor.
In the case of negative expected utilities, the information functional takes the form
I[ f(πn) ] =
X
n
f(πn) ln f(πn) + λ
"X
n
f(πn) −1
#
+ γ
"
Λ −
X
n
f(πn)Λ(πn)
#
,
(24)
where
Λ(πn) = −ln |U(Ln)| ,
U(Ln) < 0 .
Then its minimization yields the utility factor
f(πn) =
|U(Ln)|−γ
P
n |U(Ln)|−γ
(γ > 0) ,
(25)
with the positive sign of γ prescribed by the requirement that the larger cost implies the smaller
factor.
The utility factors (23) and (25) are the examples of power-law distributions that are known
in many applications (Frank, 2009; Batty, 2010; Saichev et al. 2010).
4
Non-informative prior for attraction factors
Although the attraction factor characterizes irrational features of decision making, it can be
estimated by invoking non-informative prior assumptions.
An important consequence of the
latter is the quarter law derived earlier (Yukalov and Sornette, 2009b, 2010, 2011). Here we ﬁrst
give the new, probably the simplest, derivation of the quarter law and, second, we show how
this law can be used for estimating the attraction factors in the case of an arbitrary number of
prospects.
Let us consider the sum
1
NL
NL
X
n=1
|q(πn)| =
Z 1
0
ϕ(x)x dx
(26)
of the attraction factor moduli, where
ϕ(x) ≡1
NL
NL
X
n=1
[ δ(x −q(πn)) + δ(x + q(πn)) ]
(27)
plays the role of the attraction-factor distribution. The latter is normalized as
Z 1
−1
ϕ(x) dx = 1 ,
(28)
7


## Page 8


since the attraction factors, in view of condition (15), vary in the interval [−1, 1]. If q(πn) does
not equal zero, then normalization (28) is evident. And when q(πn) = 0, then one should use the
identity
Z 1
0
δ(x) dx = 1
2
for the semi-integral of the Dirac function.
The use of a non-informative prior implies that the values of the attraction factor are not
known. A full ignorance is captured by a uniform distribution, which, according to normalization
(28), gives
ϕ(x) = 1
2 .
(29)
In that case, integral (26) results in the quarter law
1
NL
NL
X
n=1
|q(πn)| = 1
4 .
(30)
If the prospect lattice L = {πn} consists of NL prospects, we can always arrange the corre-
sponding attraction factors in the ascending order, such that
q(πn) > q(πn+1)
(n = 1, 2, . . . , NL −1) .
(31)
We denote the largest attraction factor as
qmax ≡q(π1) > 0 .
(32)
Given the unknown values of the attraction factors, the non-informative prior assumes that they
are uniformly distributed and at the same time they must obey the ordering constraint (31).
Then, the joint cumulative distribution of the attraction factors is given by
Pr[q(π1) < η1, q(π2) < η2, ..., q(πNL) < ηNL|η1 ≤η2 ≤... ≤ηNL] =
=
Z η1
0
dx1
Z η2
x1
dx2....
Z ηNL
xNL−1
dxNL ,
(33)
where the series η1 ≤η2 ≤... ≤ηNL of inequalities ensure the ordering. It is then straightforward
to show that the average values of the q(πn) are equidistant, i.e. the diﬀerence between any two
neighboring factors is on average
∆≡⟨q(πn)⟩−⟨q(πn+1)⟩= const
(independent of n) .
(34)
Taking their average values as determining their typical values, we omit the symbol ⟨.⟩repre-
senting the average operator and use equation (34) to represent the n-th attraction factor as
q(πn) = qmax −(n −1)∆.
(35)
With notations (32) and (34), the alternation condition (15) yields
qmax = NL −1
2
∆.
(36)
8


## Page 9


And the quarter law (30) leads to the gap
∆=
NL
2 P
n |NL + 1 −2n| .
(37)
If NL is even, then
NL
X
n=1
|NL + 1 −2n| = N2
L
2
(NL even) ,
while when NL is odd, then
NL
X
n=1
|NL + 1 −2n| = N2
L −1
2
(NL odd) .
This allows us to represent gap (37) as
∆=



1
NL
(NL even)
NL
N2
L−1
(NL odd) .
(38)
And for the largest attraction factor, we ﬁnd
qmax =



NL−1
2NL
(NL even)
NL
2(NL+1)
(NL odd) .
(39)
The above expressions make it possible to evaluate, on the basis of the non-informative prior,
the whole set
QNL ≡{q(πn) : n = 1, 2, . . . , NL}
(40)
of the attraction factors:
q(πn) =



1
2NL (NL −2n + 1)
(NL even)
NL
2(N2
L−1) (NL −2n + 1)
(NL odd) .
(41)
For example, in the case of two prospects, we have
∆= 1
2 ,
qmax = 1
4
(NL = 2) ,
which yields the attraction set
Q2 =
1
4 , −1
4

.
For three prospects, we get
∆= 3
8 ,
qmax = 3
8
(NL = 3) ,
hence
Q3 =
3
8 , 0 , −3
8

.
9


## Page 10


Similarly, for four prospects, we ﬁnd
∆= 1
4 ,
qmax = 3
8
(NL = 4) ,
with the attraction set
Q4 =
3
8 , 1
8 , −1
8 , −3
8

.
When there are ﬁve prospects, then
∆= 5
24 ,
qmax = 5
12
(NL = 5) ,
from where
Q5 =
 5
12 ,
5
24 , 0 , −
5
24 , −
5
12

.
Thus, we can evaluate the attraction factors for any number of prospects, obtaining a kind of a
quantized attraction set. In the case of an asymptotically large number NL of prospects, we have
∆≃1
NL
,
qmax ≃1
2
(NL ≫1) ,
(42)
and
q(πn) ≃1
2 −2n −1
2NL
.
(43)
The non-informative priors can be employed for predicting the results of decision making. This
makes the principal diﬀerence compared with the introduction into expected utility of adjustment
parameters that are ﬁtted post hoc to the given experimental data (Sinisalchi, 2009).
5
Quantitative explanation of decoy eﬀect
We now show how the non-informative priors of the attraction factors can be employed to explain
the decoy eﬀect and for quantitative prediction in decision-making. Throughout this section, we
denote, for simplicity, the objects of choice, say A, as well as the act of choosing an object A,
by the same letter A. As has been emphasized above, the act of choice under uncertainty is a
composite prospect. But, again for simplicity, we employ the same letter for denoting the action
A and the related prospect (5).
The decoy eﬀect was ﬁrst studied by Huber, Payne and Puto (1982), who called it the eﬀect
of asymmetrically dominated alternatives. Later this eﬀect has been conﬁrmed in a number of
experimental investigations (Simonson, 1989; Wedell, 1991; Tversky and Simonson, 1993; Ariely
and Wallsten, 1995). The meaning of the decoy eﬀect can be illustrated by the following example.
Suppose a buyer is choosing between two objects, A and B. The object A is of better quality, but
of higher price, while the object B is of slightly lower quality, while less expensive. As far as the
functional properties of both objects are not drastically diﬀerent, but B is cheaper, the majority
of buyers value the object B higher. At this moment, the salesperson mentions that there is a
third object C, which is of about the same quality as A, but of a much higher price than A.
This causes the buyer to reconsider the choice between the objects A and B, while the object C,
having the same quality as A but being much more expensive, is of no interest. Choosing now
between A and B, the majority of buyers prefer the higher quality but more expensive object
10


## Page 11


A. The object C, being not a choice alternative, plays the role of a decoy. Experimental studies
conﬁrmed the decoy eﬀect for a variety of objects: cars, microwave ovens, shoes, computers,
bicycles, beer, apartments, mouthwash, etc. The same decoy eﬀect also exists in the choice of
human mates distinguished by attractiveness and sense of humor (Bateson and Healy, 2005). It
is common as well for animals, for instance, in the choice of female frogs of males with diﬀerent
attraction calls characterized either by low-frequency and longer duration or by faster call rates
(Lea and Ryan, 2015).
The decoy eﬀect contradicts the regularity axiom in decision making telling that if B is
preferred to A in the absence of C, then this preference has to remain in the presence of C.
In the frame of QDT, the decoy eﬀect is explained as follows. Assume buyers consider an
object A, which is of higher quality but more expensive, and an object B, which is of moderate
quality but cheaper. Suppose the buyers have evaluated these objects A and B, which implies
that the initial values of the objects are described by the utility factors f(A) and f(B). In
experiments, the latter correspond to the fractions of buyers evaluating higher the related object.
When the decoy C, of high quality but essentially more expensive, is presented, it attracts the
attention of buyers to the quality characteristic. The role of the decoy is well understood as
attracting the attention of buyers to a particular feature of the considered objects, because of
which the decoy eﬀect is sometimes named the attraction eﬀect (Simonson, 1989). In the present
case, the decoy attracts the buyer attention to quality. The attraction, induced by the decoy, is
described by the attraction factors q(A) and q(B). Hence the probabilities of the related choices
are now
p(A) = f(A) + q(A) ,
p(B) = f(B) + q(B) .
Since the quality feature becomes more attractive, q(A) > q(B). According to the non-informative
prior, we can estimate the attraction factors as q(A) = 1/4 and q(B) = −1/4.
To be more precise, let us take numerical values from the experiment of Ariely and Wallsten
(1995), where the objects under sale are microwave ovens.
The evaluation without a decoy
results in f(A) = 0.4 and f(B) = 0.6. In the presence of the decoy, we predict that the choice
probabilities can be evaluated as
p(A) = f(A) + 0.25 ,
p(B) = f(B) −0.25 .
This gives p(A) = 0.65 and p(B) = 0.35. The experimental values for the choice between A
and B, in the presence of but excluding C, correspond to the fractions pexp(A) = 0.61 and
pexp(B) = 0.39, which is close to the predicted probabilities.
Another example can be taken from the studies of the frog mate choice (Lea and Ryan, 2015),
where frog males have attraction calls diﬀering in either low-frequency sound or call rate. The
males with lower frequency calls are denoted as A, while those with high call rate, as B. In an
experiment with 80 frog females, without a decoy, it was found that females evaluate higher the
fastest call rate, so that f(A) = 0.35 and f(B) = 0.65. In the presence of an inferior decoy,
attracting attention to the low-frequency characteristic, the non-informative prior predicts the
probabilities
p(A) = 0.35 + 0.25 = 0.6 ,
p(B) = 0.65 −0.25 = 0.4 .
The empirically observed fractions are found to be pexp(A) = 0.6 and pexp(B) = 0.4, in remar-
quable agreement with our predictions.
To make it clear how the decoy eﬀect ﬁts the title of the paper ”Inconclusive quantum
measurements and decisions under uncertainty”, it is worth extending the comments that have
been mentioned in the Introduction.
11


## Page 12


Our principal point of view is that decision making, generally, almost always deals with
composite events, since any choice is accompanied by subconscious feelings and irrational biases.
The latter are often diﬃcult to formalize and, even more, their weights usually are not known and
are practically unmeasurable. This is why these subconscious irrational factors can be treated
as what is called inconclusive events. When choosing between several possibilities, say An, one
actually considers composite prospects, as deﬁned in (5). And the composite nature of choices
requires the use of quantum techniques, as has been explained in our previous paper (Yukalov
and Sornette, 2014b). Otherwise, the probabilities of simple events could be characterized by
classical theory. It is the composite nature of the considered prospects that yields the appearance
of the quantum term q(πn) related to interference and coherence eﬀects. In that way, the choice
between the objects in the decoy eﬀect is also a composite prospect, being composed of the choice
as such and accompanying subconscious feelings forming an inconclusive set. This is why the use
of QDT here is necessary and why it gives so good results.
It is admissible to give a schematic picture of the choice in the decoy eﬀect by analogy with
the double-slit experiment in physics, which is mentioned in the Introduction. Thus making a
concrete selection of either an object A or B is the analog of the registration of the particle by
a detector. But before such a selection is done, there exists the uncertainty of deciding which of
the object features are actually more important. These not precisely deﬁned acts of hesitation
play the role of the slits, with the uncertainty associated with which of them the particle has
passed through. When it is known which of the slits the particle has passed through, then the
interference eﬀects in physics disappear. Similarly, in decision theory, if the values of each object
are clearly deﬁned, there are no hesitations, no interference, and the selection can be based on
classical rules. Such an objective evaluation in the decoy eﬀect happens in the absence of any
decoy, when a decision maker rationally evaluates the features of the given objects, say quality
and price. The appearance of a decoy induces hesitations concerning which of the features are
actually more important. These hesitations before the choice are the analogs of the uncertainty
of which slits will be visited by the traveling particle. The uncertainty results in the interference
and the arising quantum term, whether in the registration of a particle or in the ﬁnal choice of
a decision maker.
6
Discussion
We have presented a mathematical formulation for the concept of inconclusive quantum mea-
surements and events. This type of measurements in physics happens at intermediate stages of
composite measuring procedures, while the ﬁnal measurement stage is operationally testable. In
decision making, inconclusive events correspond to the intermediate stage of deliberations. Invok-
ing non-informative priors, it is possible to estimate the prospect probabilities, thus, predicting
the results of decision making.
Generally, invoking more information on the properties of the attraction factor, it is possible
to deﬁne its form more accurately than the value given by non-informative prior. For example,
from condition (9) it follows that
−f(πn) ≤q(πn) ≤1 −f(πn) .
Hence, for a positive q(πn), we have
0 ≤q(πn) ≤1 −f(πn) .
12


## Page 13


While for a negative q(πn), we get
−f(πn) ≤q(πn) ≤0 .
Therefore, the attraction factor has to satisfy the limits
q(πn) →+0 ,
f(πn) →1 ,
q(πn) →−0 ,
f(πn) →0 .
This suggests that the absolute value of the attraction factor can be modelled by an expression
proportional to
q(πn) ∝f µ(πn)[1 −f(πn)]ν ,
with µ and ν being positive parameters and the sign deﬁned by the ambiguity and risk aversion
principle (Yukalov and Sornette, 2009b, 2010, 2011, 2014a). More detailed study of such a form
will be given in a separate paper.
But it turns out that even the simple non-informative prior provides us a rather good estimate
allowing for quantitative predictions in decision making. And we have illustrated the approach
by the decoy eﬀect for which the non-informative priors yield quantitative predictions in very
good agreement with empirical data.
In this paper, decision making by separate subjects is considered. We think that the theory
can be generalized by considering societies of decision makers. The exchange of information in a
society should certainly inﬂuence the decisions of the society members. To develop a theory of
many agents, it is necessary to generalize the approach by treating a dynamical model of agents
exchanging information. Then, we think, it would be feasible to describe the behavior of the
agents operating in a ﬁnancial market and taking decisions about buying or selling shares in
the presence of information asymmetry. And it would be possible to explain the known stylized
facts in ﬁnancial markets, such as, for example, the fat tails of return distributions and volatility
clustering, as well as transient bubbles and crashes, which are connected with herding behavior.
Some ﬁrst results in that direction are reported in our previous papers (Yukalov and Sornette
2014a,20015c), where the role of additional information, received by decision makers, is analyzed
and it is shown that the amount of the additional information essentially inﬂuences the value
of the quantum term. Further work on the generalization of the approach towards a dynamical
theory of decison-maker societies is in progress.
Acknowledgment. Financial support from the ETH Z¨urich Risk Center is appreciated. We
are greateful for discussions to E.P. Yukalova.
Conﬂict of Interest Statement: The authors declare that the research was conducted in
the absence of any commercial or ﬁnancial relationships that could be construed as a potential
conﬂict of interest.
13


## Page 14


References
Ariely, D., and Wallsten, T.S. (1995). Seeking subjective dominance in multidimensional
space: an explanation of the asymmetric dominance eﬀect. Org. Behav. Human Decis. Process.
63, 223–232.
Ashtiani, M., and Azgomi, M.A. (2015). A survey of quantum-like approaches to decision
making and cognition. Math. Soc. Sci. 75, 49–50.
Bagarello, F. (2013). Quantum Dynamics for Classical Systems. Hoboken: Wiley.
Bateson, M., and Healy, S.D. (2006). Comparative evaluation and its implications for mate
choice. Trends Ecol. Evol. 20, 659–664.
Batty, M. (2010). Space, scale, and scaling in entropy maximizing. Geogr. Anal. 42, 395–421.
Bohr, N. (1976).
Collected Works.
The Correspondence Principle, Vol.
3.
Amsterdam:
North-Holland.
Boyer-Kassem, T., Duchˆen, S., and Guerci, E. (2015a).
Testing quantum-like models of
judgment for question order eﬀects. arXiv:1501.04901.
Boyer-Kassem, T., Duchˆen, S., and Guerci, E. (2015b). Quantum-like models cannot account
for the conjunction fallacy. Working paper, Tilburg University.
Busemeyer, J.R., and Bruza, P. (2012). Quantum Models of Cognition and Decision. Cam-
bridge: Cambridge University.
Carbone, E., and Hey, J.D. (2000). Which error story is best? J. Risk Uncert. 202, 161–176.
Conte, A., Hey, J.D., and Moﬀatt, P.G. (2011). Mixture models of choice under risk. J.
Econometr. 162, 79–88.
Frank, S.A. (2009). The common patterns of nature. J. Evol. Biol. 22, 1563–1585.
Haven, E., and Khrennikov, A. (2013). Quantum Social Science. Cambridge: Cambridge
University.
Haven, E., and Khrennikov, A. (2016). Quantum probability and mathematical modelling of
decision making. Philos. Trans. Roy. Soc. A 374: 20150105.
Hey, J.D. (1995). Experimental investigations of errors in decision making under risk. Eur.
Econ. Rev. 39, 633–640.
Hey, J.D. (2005). Why we should not be silent about noise. Exp. Econ. 8, 325–345.
Huber, J., Payne, J.W., and Puto, C. (1982). Adding asymmetrically dominated alternatives:
violations of regularity and similarity hypothesis. J. Consum. Res. 9, 90–98.
Kallenberg, O. (2001). Foundations of Modern Probability. Berlin: Springer.
Khrennikov, A. (2010). Ubiquitous Quantum Structure. Berlin: Springer.
Lea, A.M., and Ryan, M.J. (2015). Irrationality in mate choice revealed by tungara frogs.
Science 349, 964–966.
Loomes, G., and Sugden, R. (1998). Testing diﬀerent stochastic speciﬁcations of risky choice.
Economica 65, 581–598.
Luce, R.D. (1959). Individual Choice Behavior: A Theoretical Analysis. New York: Wiley.
14


## Page 15


Saichev, A., Malevergne, Y., and Sornette, D. (2010). Theory of Zipf’s Law and Beyond.
Heidelberg: Springer.
Simonson, I. (1989). Choice based on reasons: the case of attraction and compromise eﬀects.
J. Consum. Res. 16, 158–174.
Sinisalchi, M. (2009). Vector expected utility and attitudes toward variation. Econometrica
77, 801–855.
Sornette, D. (2014). Physics and ﬁnancial economics (1776–2014): puzzles, Ising and agent-
based models. Rep. Prog. Phys. 77: 062001.
Tversky, A., and Simonson, I. (1993). Context-dependent preferences.
Manag. Sci. 39,
1179–1189.
von Neumann, J. (1955).
Mathematical Foundations of Quantum Mechanics.
Princeton:
Princeton University.
von Neumann, J., and Morgenstern, O. (1953). Theory of Games and Economic Behavior.
Princeton: Princeton University.
Wedell, D.H. (1991). Distinguishing among models of contextuality induced preference rever-
sals. Learn. Memory Cogn. 17, 767–778.
Yukalov, V.I. (2011) Equilibration and thermalization in ﬁnite quantum systems. Laser Phys.
Lett. 8, 485–507.
Yukalov, V.I. (2012a) Equilibration of quasi-isolated quantum systems. Phys. Lett, A 376,
550–554.
Yukalov, V.I., (2012b). Decoherence and equilibration under nondestructive measurements.
Ann. Phys. (N.Y.) 327, 253–263.
Yukalov, V.I., and Sornette, D. (2008).
Quantum decision theory as quantum theory of
measurement. Phys. Lett. A 372, 6867–6871.
Yukalov, V.I., and Sornette, D. (2009a). Physics of risk and uncertainty in quantum decision
making. Eur. Phys. J. B 71, 533–548.
Yukalov, V.I., and Sornette, D. (2009b). Processing information in quantum decision theory.
Entropy 11, 1073–1120.
Yukalov, V.I., and Sornette, D. (2010). Mathematical structure of quantum decision theory.
Adv. Complex Syst. 13, 659–696.
Yukalov, V.I., and Sornette, D. (2011). Decision theory with prospect interference and en-
tanglement. Theor. Decis. 70, 283–328.
Yukalov, V.I., and Sornette, D. (2013). Quantum probabilities of composite events in quantum
measurements with multimode states. Laser Phys. 23: 105502.
Yukalov, V.I., and Sornette, D. (2014a). Manipulating decision making of typical agents.
IEEE Trans. Syst. Man Cybern. Syst. 44, 1155–1168.
Yukalov, V.I., and Sornette, D., (2014b). Conditions for quantum interference in cognitive
sciences. Top. Cogn. Sci. 6, 79–90.
Yukalov, V.I., and Sornette, D. (2015a). Positive operator-valued measures in quantum deci-
15


## Page 16


sion theory. Lect. Notes Comput. Sci. 8951, 146–161.
Yukalov, V.I., and Sornette, D. (2015b).
Quantum theory of measurements as quantum
decision theory. J. Phys. Conf. Ser. 594: 012048.
Yukalov, V.I., and Sornette, D. (2015c). Role of information in decision making of social
agents. Int. J. Inf. Technol. Dec. Mak. 14, 1129–1166.
Yukalov, V.I., and Sornette, D. (2016). Quantum probability and quantum decision making.
Philos. Trans. Roy. Soc. A 374: 20150100.
16

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1604_04739v1_inconclusive_quantum_measurements_and_decisions_under_uncertainty
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1604_04739V1_INCONCLUSIVE_QUANTUM_MEASUREMENTS_AND_DECISIONS_UNDER_UNCERTAINTY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
