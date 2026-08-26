---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.12362
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1905.12362_Practical_Statistics_for_Particle_Physics

> Source: 1905.12362_Practical_Statistics_for_Particle_Physics.pdf

> Pages: 49

---


## Page 1


Practical statistics for particle physics
R. J. Barlow
The University of Huddersﬁeld, Huddersﬁeld, United Kingdom
Abstract
This is the write-up of a set of lectures given at the Asia Europe Paciﬁc School
of High Energy Physics in Quy Nhon, Vietnam in September 2018, to an au-
dience of PhD students in all branches of particle physics. They cover the
different meanings of ‘probability’, particularly frequentist and Bayesian, the
binomial, the Poisson and the Gaussian distributions, hypothesis testing, es-
timation, errors (including asymmetric and systematic errors) and goodness
of ﬁt. Several different methods used in setting upper limits are explained,
followed by a discussion on why 5 sigma are conventionally required for a
‘discovery’.
Keywords
Lectures; statistics; particle physics, probability, estimation, conﬁdence limits.
1
Introduction
To interpret the results of your particle physics experiment and see what it implies for the relevant
theoretical model and parameters, you need to use statistical techniques. These are a part of your exper-
imental toolkit, and to extract the maximum information from your data you need to use the correct and
most powerful statistical tools.
Particle physics (like, probably, any ﬁeld of science) has is own special set of statistical processes
and language. Our use is in some ways more complicated (we often ﬁt multi-parameter functions, not
just straight lines) and in some ways more simple (we do not have to worry about ethics, or law suits).
So the generic textbooks and courses you will meet on ‘Statistics’ are not really appropriate. That’s why
HEP schools like this one include lectures on statistics as well as the fundamental real physics, like ﬁeld
theory and physics beyond the Standard Model (BSM).
There are several textbooks [1–6] available which are designed for an audience of particle physi-
cists. You will ﬁnd these helpful—more helpful than general statistical textbooks. You should ﬁnd one
whose language suits you and keep a copy on your bookshelf—preferably purchased—but at least on
long term library loan. You will also ﬁnd useful conference proceedings [7–9], journal papers (particu-
larly in Nuclear Instruments and Methods) and web material: often your own experiment will have a set
of pages devoted to the topic.
2
Probability
We begin by looking at the concept of probability. Although this is familiar (we use it all the time, both
inside and outside the laboratory), its use is not as obvious as you would think.
2.1
What is probability?
A typical exam for Statistics101 (or equivalent) might well contain the question:
Q1
Explain what is meant by the probability PA of an event A
[1]
© CERN, 2020, CC-BY-4.0 licence, doi:10.23730/CYRSP-2020-005.149, ISSN 0531-4283.
arXiv:1905.12362v2  [physics.data-an]  2 Feb 2021


## Page 2


The ‘1’ in square brackets signiﬁes that the answer carries one mark. That’s an indication that just
a sentence or two are required, not a long essay.
Asking a group of physicists this question produces answers falling into four different categories
1. PA is number obeying certain mathematical rules,
2. PA is a property of A that determines how often A happens,
3. For N trials in which A occurs NA times, PA is the limit of NA/N for large N, and
4. PA is my belief that A will happen, measurable by seeing what odds I will accept in a bet.
Although all these are generally present, number 3 is the most common, perhaps because it is often
explicitly taught as the deﬁnition. All are, in some way, correct! We consider each in turn.
2.2
Mathematical probability
The Kolmogorov axioms are: For all A ⊂S
PA ≥0
PS = 1
PA∪B = PA + PB if A ∩B = φ and A, B ⊂S
.
(1)
From these simple axioms a complete and complicated structure of theorems can be erected. This
is what pure mathematicians do. For example, the 2nd and 3rd axiom show that the probability of not-A
PA, is 1 −PA, and then the 1st axiom shows that PA ≤1: probabilities must be less than 1.
But the axioms and the ensuing theorems says nothing about what PA actually means. Kol-
mogorov had frequentist probability in mind, but these axioms apply to any deﬁnition: he explicitly
avoids tying PA down in this way. So although this apparatus enables us to compute numbers, it does
not tell us what we can use them for.
2.3
Real probability
Also known as Classical probability, this was developed during the 18th–19th centuries by Pascal,
Laplace and others to serve the gambling industry.
If there are several possible outcomes and there is a symmetry between them so they are all, in a
sense, identical, then their individual probabilities must be equal. For example, there are two sides to a
coin, so if you toss it there must be a probability 1
2 for each face to land uppermost. Likewise there are
52 cards in a pack, so the probability of a particular card being chosen is 1
52. In the same way there are 6
sides to a dice, and 33 slots in a roulette wheel.
This enables you to answer questions like ‘What is the probability of rolling more than 10 with
2 dice?’. There are 3 such combinations (5-6, 6-5 and 6-6) out of the 6 × 6 = 36 total possibilities,
so the probability is
1
12. Compound instances of A are broken down into smaller instances to which
the symmetry argument can be applied. This is satisfactory and clearly applicable—you know that if
someone offers you a 10 to 1 bet on this dice throw, you should refuse; in the long run knowledge of the
correct probabilities will pay off.
The problem arises that this approach cannot be applied to continuous variables. This is brought
out in Bertan’s paradoxes, one of which runs:
In a circle of radius R an equilateral triangle is drawn. A chord is drawn at random. What is the
probability that the length of the chord is greater than the side of the triangle?
Considering Fig. 1 one can give three answers:
150


## Page 3


Fig. 1: Bertan’s paradox
1. If the chord, without loss of generality, starts at A, then it will be longer than the side if the end
point is anywhere between B and C. So the answer is obviously 1
3.
2. If the centre of the chord, without loss of generality, is chosen at random along the line OD, then
it will be longer than the side of the triangle if it is in OE rather than ED. E is the midpoint of OD
so the answer is obviously 1
2.
3. If the centre of the chord, without loss of generality, is chosen at random within the circle, then it
will be longer than the side of the triangle if it lies within the circle of radius R
2 . So the answer is
obviously 1
4.
So we have three obvious but contradictory answers. The whole question is built on a false
premise: drawing a chord ‘at random’ is, unlike tossing a coin or throwing a dice, not deﬁned. An-
other way of seeing this is that a distribution which is uniform in one variable, say θ, is not uniform in
any non-trivial transformation of that variable, say cos θ or tan θ. Classical probability has therefore to
be discarded.
2.4
Frequentist probability
Because of such difﬁculties, Real Probability was replaced by Frequentist Probability in the early 20th
century. This is the usual deﬁnition taught in schools and undergraduate classes. A very readable account
is given by von Mises [10]:
PA = lim
N→∞
NA
N
.
N is the total number of events in the ensemble (or collective). It can be visualised as a Venn
diagram, as in Fig. 2.
The probability of a coin landing heads up is 1
2 because if you toss a coin 1000 times, one side will
come down ∼500 times. That is an empirical deﬁnition (Frequentist probability has roots in the Vienna
school and logical positivism). Similarly, the lifetime of a muon is 2.2µs because if you take 1000 muons
and wait 2.2µs, then ∼368 (that’s a fraction e−1) will remain.
With this deﬁnition PA is not just a property of A but a joint property of A and the ensemble. The
same coin will have a different probability for showing head depending on whether it is in a purse or
151


## Page 4


Fig. 2: Frequentist probability
in a numismatic collection. This leads to two distinctive properties (or, some would say, problems) for
frequentist probability.
Firstly, there may be more than one ensemble. To take an everyday example from von Mises,
German life insurance companies pay out on 0.4% of 40 year old male clients. Your friend Hans is 40
today. What is the probability that he will survive to see his 41st birthday? 99.6% is an answer (if he’s
insured). But he is also a non-smoker and non-drinker—so perhaps the ﬁgure is higher (maybe 99.8%)?
But if he drives a Harley-Davidson it should be lower (maybe 99.0%)? All these numbers are acceptable.
The individual Hans belongs to several different ensembles, and the probability will be different for each
of them.
To take an example from physics, suppose your experiment has a Particle Identiﬁcation (PID)
system using Cherenkov, time-of-ﬂight and/or dE
dx measurements. You want to talk about the probability
that a K+ will be correctly recognised by your PID. You determine this by considering many K+ mesons
and counting the number accepted to get P = Nacc/Ntot. But these will depend on the kaon sample you
work with. It could be all kaons, or kaons above a certain energy threshold, or that actually enter the
detector. The ensemble can be deﬁned in various ways, each giving a valid but different value for the
probability.
On the other hand, there may be no Ensemble. To take an everyday example we might want to
calculate the probability that it will rain tomorrow. This is impossible. There is only one tomorrow. It
will either rain or not rain. Prain is either 0 or 1, and we won’t know which until tomorrow gets here.
Von Mises insists that statements like ‘It will probably rain tomorrow’ are loose and unscientiﬁc.
To take an example from physics, consider the probability that there is a supersymmetric particle
with mass below 2 TeV. Again, either there is or there isn’t.
But, despite von Mises’ objections, it does seem sensible, as the pressure falls and the gathering
clouds turn grey, to say ‘It will probably rain’. So this is a drawback to the frequentist deﬁnition. We will
return to this and show how frequentists can talk meaningfully and quantitatively about unique events in
the discussion of conﬁdence intervals in Section 8.1.
2.5
Bayes’ theorem
Before presenting Bayesian statistics we need to discuss Bayes’ theorem, though we point out that Bayes’
theorem applies (and is useful) in any probability model: it goes right back to the Kolmogorov axioms.
First we need to deﬁne the conditional probability: P(A|B): this is the probability for A, given
that B is true. For example: if a playing card is drawn at random from a pack of 52, then P(♠A) =
1
52,
but if you are told that the card is black, then P(♠A|Black) = 1
26 (and obviously P(♠A|Red) = 0).
152


## Page 5


Bayes’ theorem is just
P(A|B) = P(B|A)
P(B)
× P(A)
.
(2)
The proof is gratifyingly simple: the probability that A and B are both true can be written in two
ways
P(A|B) × P(B) = P(A&B) = P(B|A) × P(A)
.
Throw away middle term and divide by P(B) to get the result.
As a ﬁrst example, we go back to the ace of spades above. A card is drawn at random, and you are
told that it is black. Bayes’ theorem says
P(♠A|Black) = P(Black|♠A)
P(Black)
P(♠A) = 1
1
2 × 1
52 = 1
26
;
i.e. the original probability of drawing ♠A,
1
52, is multiplied by the probability that the ace of spades
is black (just 1) and divided by the overall probability of drawing a black card ( 1
2) to give the obvious
result.
For a less trivial example, suppose you have a momentum-selected beam which is 90% π and 10%
K. This goes through a Cherenkov counter for which pions exceed the threshold velocity but kaons do
not. In principle pions will give a signal, but suppose there is a 5% chance, due to inefﬁciencies, that
they will not. Again in principle kaons always give no Cherenkov signal, but suppose that probability is
only 95% due to background noise. What is the probability that a particle identiﬁed as a kaon, as it gave
no signal, is truly one?
Bayes’ theorem runs
P(K|no signal) = P(no signal|K)
P(no signal) × P(K) =
0.95
0.95×0.1+0.05×0.9 × 0.1 = 0.68
,
showing that the probability is only 2
3. The positive identiﬁcation is not enough to overwhelm the 9:1
π : K ratio. Incidentally this uses the (often handy) expression for the denominator: P(B) = P(B|A)×
P(A) + P(B|A) × P(A).
2.6
Bayesian probability
The Bayesian deﬁnition of probability is that PA represents your belief in A. 1 represents certainty, 0
represents total disbelief. Intermediate values can be calibrated by asking whether you would prefer to
bet on A, or on a white ball being drawn from an urn containing a mix of white and black balls.
This avoids the limitations of frequentist probability—coins, dice, kaons, rain tomorrow, existence
of supersymmetry (SUSY) can all have probabilities assigned to them.
The drawback is that your value for PA may be different from mine, or anyone else’s. It is also
called subjective probability.
Bayesian probability makes great use of Bayes’ theorem, in the form
P(Theory|Data) = P(Data|Theory)
P(Data)
× P(Theory)
.
(3)
P(Theory) is called the prior: your initial belief in Theory. P(Data|Theory) is the Likelihood:
the probability of getting Data if Theory is true. P(Theory|Data) is the Posterior: your belief in
Theory in the light of a particular Data being observed.
So this all works very sensibly. If the data observed is predicted by the theory, your belief in that
theory is boosted, though this is moderated by the probabilty that the data could have arisen anyway.
Conversely, if data is observed which is disfavoured by the theory, your belief in that theory is weakened.
The process can be chained. The posterior from a ﬁrst experiment can be taken as the prior for a
second experiment, and so on. When you write out the factors you ﬁnd that the order doesn’t matter.
153


## Page 6


2.6.1
Prior distributions
Often, though, the theory being considered is not totally deﬁned: it may contain a parameter (or several
parameters) such as a mass, coupling constant, or decay rate. Generically we will call this a, with the
proviso that it may be multidimensional.
The prior is now not a single number P(Theory) but a probability distribution P0(a).
R a2
a1 P0(a) da is your prior belief that a lies between a1 and a2.
R ∞
−∞P0(a) da is your original
P(Theory). This is generally taken as 1, which is valid provided the possibility that the theory that
is false is matched by some value of a—for example if the coupling constant for a hypothetical particle
is zero, that accommodates any belief that it might not exist. Bayes’ theorem then runs:
P1(a; x) ∝L(a; x)P0(a)
.
(4)
If the range of a is inﬁnite, P0(a) may be vanishingly small (this is called an ‘improper prior’).
However this is not a problem. Suppose, for example, that all we know about a is that it is non-negative,
and we are genuinely equally open to its having any value. We write P0(a) as C, so
R a2
a1 P0(a) da =
C(a2 −a1). This probability is vanishingly small: if you were offered the choice of a bet on a lying
within the range [a1, a2] or of drawing a white ball from an urn containing 1 white ball and N black
balls, you would choose the latter, however large N was. However it is not zero: if the urn contained
N black balls, but no white ball, your betting choice would change. After a measurement you have
P1(a; x) =
L(a;x)
R
L(a′;x)Cda′ C, and the factors of C can be cancelled (which, and this is the point, you could
not do if C were exactly zero) giving P1(a; x) =
L(a;x)
R
L(a′;x)da′ or, P1(a; x) ∝L(a; x), and you can then
just normalize P1(a) to 1.
Fig. 3: Bayes at work
Figure 3 shows Eq. 4 at work. Suppose a is known to lie between 0 and 6, and the prior distribution
is taken as ﬂat, as shown in the left hand plot. A measurement of a gives a result 4.4 ± 1.0 , as shown
in the central plot. The product of the two gives (after normalization) the posterior, as shown in the right
hand plot.
2.6.2
Likelihood
The likelihood—the number P(Data|Theory)—is now generalised to the function L(a, x), where x is
the observed value of the data. Again, x may be multidimensional, but in what follows it is not misleading
to ignore that.
This can be confusing. For example, anticipating Section 3.2.2, the probability of getting x counts
from a Poisson process with mean a is
154


## Page 7


P(x, a) = e−a ax
x!
.
(5)
We also write
L(a, x) = e−a ax
x!
.
(6)
What’s the difference? Technically there is none. These are identical joint functions of two vari-
ables (x and a) to which we have just happened to have given different names. Pragmatically we regard
Eq. 5 as describing the probability of getting various different x from some ﬁxed a, whereas Eq. 6
describes the likelihood for various different a from some given x. But be careful with the term ‘like-
lihood’. If P(x1, a) > P(x2, a) then x1 is more probable (whatever you mean by that) than x2. If
L(a1, x) > L(a2, x) it does not mean that a1 is more likely (however you deﬁne that) than a2.
2.6.3
Shortcomings of Bayesian probability
The big problem with Bayesian probability is that it is subjective. Your P0(a) and my P0(a) may be
different—so how can we compare results? Science does, after all, take pride in being objective: it
handles real facts, not opinions. If you present a Bayesian result from your search for the X particle this
embodies the actual experiment and your irrational prior prejudices. I am interested in your experiment
but not in your irrational prior prejudices—I have my own—and it is unhelpful if you combine the two.
Bayesians sometimes ask about the right prior they should use. This is the wrong question. The
prior is what you believe, and only you know that.
There is an argument made for taking the prior as uniform. This is sometimes called the ‘Principle
of ignorance’ and justiﬁed as being impartial. But this is misleading, even dishonest. If P0(a) is taken
as constant, favouring no particular value, then it is not constant for a2 or √a or ln a, which are equally
valid parameters.
It is true that with lots of data, P1(a) decouples from P0(a). The ﬁnal result depends only on the
measurements. But this is not the case with little data—and that’s the situation we’re usually in—when
doing statistics properly matters.
As an example, suppose you make a Gaussian measurement (anticipating slightly Section 3.2.3).
You consider a prior ﬂat in a and a prior ﬂat in ln a. This latter is quite sensible—it says you expect
a result between 0.1 and 0.2 as being equally likely as a result between 1 and 2, or 10 and 20. The
posteriors are shown in Fig. 4. For an ‘accurate’ result of 3 ± 0.5 the posteriors are very close. For an
‘intermediate’ result of 4.0 ± 1.0 there is an appreciable difference in the peak value and the shape. For
a ‘poor’ measurement of 5.0 ± 2.0 the posteriors are very different.
So you should never just quote results from a single prior. Try several forms of prior and examine
the spread of results. If they are pretty much the same you are vindicated. This is called ‘robustness
under choice of prior’ and it is standard practice for statisticians. If they are different then the data are
telling you about the limitations of your results.
2.6.4
Jeffreys’ prior
Jeffreys [11] suggested a technique now known as the Jeffreys’ or objective prior: that you should
choose a prior ﬂat in a transformed variable a′ for which the Fisher information, I = −
D
∂2L(x;a)
∂a2
E
is
constant. The Fisher information (which is important in maximum likelihood estimation, as described
in Section 5.2) is a measure of how much a measurement tells you about the parameter: a large I has a
likelihood function with a sharp peak and will tell you (by some measure) a lot about a; a small I has
a featureless likelihood function which will not be useful. Jeffrey’s principle is that the prior should not
favour or disfavour particular values of the parameter. It is equivalently—and more conveniently—used
as taking a prior in the original a which is proportional to
√
I.
155


## Page 8


Fig. 4: Posteriors for two different priors for the results 3.0 ± 0.5, 4.0 ± 1.0 and 5.0 ± 2.0
It has not been universally adopted for various reasons. Some practitioners like to be able to
include their own prior belief into the analysis. It also makes the prior dependent on the experiment (in
the form of the likelihood function). Thus if ATLAS and CMS searched for the same new X particle
they would use different priors for P0(MX), which is (to some people) absurd.
So it is not universal—but when you are selecting a bunch of priors to test robustness—the Jef-
ferys’ prior is a strong contender for inclusion.
2.7
Summary
So mathematical probability has no meaning, and real probability is discredited. That leaves the Fre-
quentist and Bayesian deﬁnitions. Both are very much in use.
They are sometimes presented as rivals, with adherents on either side (‘frequentists versus
Bayesians’). This is needless drama. They are both tools that help us understand our results. Both
have drawbacks. Sometimes it is clear which is the best tool for a particular job, sometimes it is not and
one is free to choose either. It is said—probably accurately—that particle physicists feel happier with
frequentist probability as they are used to large ensembles of similar but different events, whereas astro-
physicists and cosmologists are more at home with Bayesian probability as they only have one universe
to consider.
What is important is not which version you prefer—these are not football teams—but that you
know the limitations of each, that you use the best deﬁnition when there is a reason to do so, and, above
all, that you are aware of which form you are using.
As a possibly heretical afterthought, perhaps classical probability still has a place? Quantum
Mechanics, after all, gives probabilities. If PA is not ‘real’—either because it depends on an arbitrary
ensemble, or because is a subjective belief—then it looks like there is nothing ‘real’ in the universe.
The state of a coin—or an electron spin—having probability 1
2 makes sense. There is a symmetry
that dictates it. The lifetime of a muon—i.e. probability per unit time that it will decay—seems to be a
well-deﬁned quantity, a property of the muon and independent of any ensemble, or any Bayesian belief.
The probability a muon will produce a signal in your muon detector seems like a ‘real well-deﬁned
quantity’, if you specify the 4 momentum and the state of the detector. Of course the inverse probability
156


## Page 9


‘What is the probability that a muon signal in my detector comes from a real muon, not background’ is
not intrinsically deﬁned, So perhaps classical probability has a place in physics—but not in interpreting
results. However you should not mention this to a statistician or they will think you’re crazy.
3
Probability distributions and their properties
We have to make a simple distinction between two sorts of data: integer data and real-number data1.
The ﬁrst covers results which are of their nature whole numbers: the numbers of kaons produced
in a collision, or the number of entries falling into some bin of a histogram. Generically let’s call such
numbers r. They have probabilities P(r) which are dimensionless.
The second covers results whose values are real (or ﬂoating-point) numbers. There are lots of
these: energies, angles, invariant masses . . . Generically let’s call such numbers x, and they have proba-
bility density functions P(x) which have dimensions of [x]−1, so
R x2
x1 P(x)dx or P(x) dx are probabili-
ties.
You will also sometimes meet the cumulative distribution C(x) =
R x
−∞P(x′) dx′.
3.1
Expectation values
From P(r) or P(x) one can form the expectation value
⟨f⟩=
X
r
f(r)P(r)
or
⟨f⟩=
Z
f(x)P(x) dx
,
(7)
where the sum or integral is taken as appropriate. Some authors write this as E(f), but I personally
prefer the angle-bracket notation. You may think it looks too much like quantum mechanics, but in fact
it’s quantum mechanics which looks like statistics: an expression like ⟨ψ| ˆQ|ψ⟩is the average value of an
operator ˆQ in some state ψ, where ‘average value’ has exactly the same meaning and signiﬁcance.
3.1.1
Mean and standard deviation
In particular the mean, often written µ, is given by
⟨r⟩= P
r rP(r)
or
⟨x⟩=
R
xP(x) dx
.
Similarly one can write higher moments
µk = ⟨rk⟩= P
r rkP(r)
or
⟨xk⟩=
R
xkP(x) dx
,
and central moments
µ′
k = ⟨(r −µ)k⟩= P
r(r −µ)kP(r)
or
⟨(x −µ)k⟩=
R
(x −µ)kP(x) dx
.
The second central moment is known as the variance
µ′
2 = V = P
r(r −µ)2P(r) = ⟨r2⟩−⟨r⟩2
or
R
(x −µ)2P(x) dx = ⟨x2⟩−⟨x⟩2
It is easy to show that ⟨(x −µ)2⟩= ⟨x2⟩−µ2. The standard deviation is just the square root of the
variance σ =
√
V .
Statisticians usually use variance, perhaps because formulae come out simpler. Physicists usually
use standard deviation, perhaps because it has the same dimensions as the variable being studied, and
can be drawn as an error bar on a plot.
You may also meet skew, which is γ = ⟨(x −µ)3⟩/σ3 and kurtosis, h = ⟨(x −µ)4⟩/σ4 −3.
Deﬁnitions vary, so be careful. Skew is a dimensionless measure of the asymmetry of a distribution.
Kurtosis is (thanks to that rather arbitrary looking 3 in the deﬁnition) zero for a Gaussian distribution
(see Section 3.2.3): positive kurtosis indicates a narrow core with a wide tail, negative kurtosis indicates
the tails are reduced.
1Other branches of science have to include a third, categorical data, but we will ignore that.
157


## Page 10


Fig. 5:
Examples of two dimensional distributions. The top right has positive covariance (and correlation), the
bottom left negative. In the top left the covariance is zero and x and y are independent; in the bottom right the
covariance is also zero, but they are not independent.
3.1.2
Covariance and correlation
If your data are 2-dimensional pairs (x, y), then besides forming ⟨x⟩, ⟨y⟩, σx etc., you can also form the
Covariance
Cov(x, y) = ⟨(x −µx)(y −µy)⟩= ⟨xy⟩−⟨x⟩⟨y⟩
.
Examples are shown in Fig. 5. If there is a tendency for positive ﬂuctuations in x to be associated
with positive ﬂuctuations in y (and therefore negative with negative) then the product (xi −x)(yi −y)
tends to be positive and the covariance is greater than 0. A negative covariance, as in the 3rd plot,
happens if a positive ﬂuctuation in one variable is associated with a negative ﬂuctuation in the other.
If the variables are independent then a positive variation in x is equally likely to be associated with a
positive or a negative variation in y and the covariance is zero, as in the ﬁrst plot. However the converse
is not always the case, there can be two-dimensional distributions where the covariance is zero, but the
two variables are not independent, as is shown in the fourth plot.
Covariance is useful, but it has dimensions. Often one uses the correlation, which is just
ρ = Cov(x, y)
σxσy
.
(8)
It is easy to show that ρ lies between 1 (complete correlation) and -1 (complete anticorrelation).
ρ = 0 if x and y are independent.
If there are more than two variables—the alphabet runs out so let’s call them (x1, x2, x3 . . . xn)—
then these generalise to the covariance matrix
Vij = ⟨xixj⟩−⟨xi⟩⟨xj⟩
and the correlation matrix
ρij = Vij
σiσj
.
The diagonal of V is σ2
i . The diagonal of ρ is 1.
3.2
Binomial, Poisson and Gaussian
We now move from considering the general properties of distributions to considering three speciﬁc ones.
These are the ones you will most commonly meet for the distribution of the original data (as opposed to
158


## Page 11


quantities constructed from it). Actually the ﬁrst, the binomial, is not nearly as common as the second,
the Poisson; and the third, the Gaussian, is overwhelmingly more common. However it is useful to
consider all three as concepts are built up from the simplest to the more sophisticated.
3.2.1
The binomial distribution
The binomial distribution is easy to understand as it basically describes the familiar2 tossing of coins. It
describes the number r of successes in N trials, each with probability p of success. r is discrete so the
process is described by a probability distribution
P(r; p, N) =
N!
r!(N −r)!prqN−r
,
(9)
where q ≡1 −p.
Some examples are shown in Fig. 6.
Fig. 6:
Some examples of the binomial distribution, for (1) N = 10, p = 0.6, (2) N = 10, p = 0.9, (3)
N = 15, p = 0.1, and (4) N = 25, p = 0.6.
The distribution has mean µ = Np, variance V = Npq, and standard deviation σ = √Npq.
3.2.2
The Poisson distribution
The Poisson distribution also describes the probability of some discrete number r, but rather than a ﬁxed
number of ‘trials’ it considers a random rate λ:
P(r; λ) = e−λ λr
r!
.
(10)
It is linked to the binomial—the Poisson is the limit of the binomial—as N →∞, p →0 with
np = λ = constant. Figure 7 shows various examples. It has mean µ = λ, variance V = λ, and
standard deviation σ =
√
λ = √µ.
The clicks of a Geiger counter are the standard illustration of a Poisson process. You will meet it
a lot as it applies to event counts—on their own or in histogram bins.
To help you think about the Poisson, here is a simple question (which describes a situation I have
seen in practice, more than once, from people who ought to know better).
2Except, as it happens, in Vietnam, where coins have been completely replaced by banknotes.
159


## Page 12


Fig. 7: Poisson distributions for (1) λ = 5, (2) λ = 1.5, (3) λ = 12 and (4) λ = 50
You need to know the efﬁciency of your PID system for positrons.
You ﬁnd 1000 data events where 2 tracks have a combined mass of 3.1 GeV (J/ψ) and the negative
track is identiﬁed as an e−(‘Tag-and-probe’ technique).
In 900 events the e+ is also identiﬁed. In 100 events it is not. The efﬁciency is 90%.
What about the error?
Colleague A says
√
900 = 30 so efﬁciency is 90.0 ± 3.0%,
colleague B says
√
100 = 10 so efﬁciency is 90.0 ± 1.0%.
Which is right?
Please think about this before turning the page...
160


## Page 13


Neither—both are wrong. This is binomial not Poisson: p = 0.9, N = 1000.
The error is √Npq = √1000 × 0.9 × 0.1 (or √1000 × 0.1 × 0.9) =
√
90 = 9.49 so the efﬁciency is
90.0 ± 0.9 %.
3.2.3
The Gaussian distribution
This is by far the most important statistical distribution. The probability density function (PDF) for a
variable x is given by the formula
P(x; µ, σ) =
1
σ
√
2πe
−(x−µ)2
2σ2
.
(11)
Pictorially this is shown in Fig. 8.
Fig. 8: The Gaussian distribution
This is sometimes called the ‘bell curve’, though in fact a real bell does not have ﬂared edges like
that. There is (in contrast to the Poisson and binomial) only one Gaussian curve, as µ and σ are just
location and scale parameters.
The mean is µ and the standard deviation is σ. The Skew is zero, as it is symmetric, and the
kurtosis is zero by construction.
In statistics, and most disciplines, this is known as the normal distribution. Only in physics is it
known as ‘The Gaussian’—perhaps because the word ‘normal’ already has so many meanings.
The reason for the importance of the Gaussian is the central limit theorem (CLT) that states: if the
variable X is the sum of N variables x1, x2 . . . xN then:
1. Means add: ⟨X⟩= ⟨x1⟩+ ⟨x2⟩+ . . . ⟨xN⟩,
2. Variances add: VX = V1 + V2 + . . . VN,
3. If the variables xi are independent and identically distributed (i.i.d.) then P(X) tends to a Gaussian
for large N.
(1) is obvious, (2) is pretty obvious, and means that standard deviations add in quadrature, and that
the standard deviation of an average falls like
1
√
N , (3) applies whatever the form of the original P(x).
161


## Page 14


Before proving this, it is helpful to see a demonstration to convince yourself that the implausible
assertion in (3) actually does happen. Take a uniform distribution from 0 to 1, as shown in the top left
subplot of Fig. 9. It is ﬂat. Add two such numbers and the distribution is triangular, between 0 and 2, as
shown in the top right.
Fig. 9: Demonstration of the central limit theorem
With 3 numbers, at the bottom left, it gets curved. With 10 numbers, at the bottom right, it looks
pretty Gaussian. The proof follows.
Proof. First, introduce the characteristic function ⟨eikx⟩=
R
eikxP(x) dx = ˜P(k).
This can usefully be thought of as an expectation value and as a Fourier transform, FT.
Expand the exponential as a series
⟨eikx⟩= ⟨1 + ikx + (ikx)2
2!
+ (ikx)3
3!
. . . ⟩= 1 + ik⟨x⟩+ (ik)2 ⟨x2⟩
2!
+ (ik3)⟨x3⟩
3! . . . . Take the
logarithm and use the expansion ln(1 + z) = z −z2
2 + z3
3 . . . This gives a power series in (ik), where
the coefﬁcient κr
r! of (ik)r is made up of expectation values of x of total power r
κ1 = ⟨x⟩, κ2 = ⟨x2⟩−⟨x⟩2 =, κ3 = ⟨x3⟩−3⟨x2⟩⟨x⟩+ 2⟨x⟩3 . . .
These are called the semi-invariant cumulants of Thièle . Under a change of scale α, κr →αrκr.
Under a change in location only κ1 changes.
If X is the sum of i.i.d. random variables, x1 + x2 + x3..., then P(X) is the convolution of P(x)
with itself N times.
The FT of a convolution is the product of the individual FTs,
the logarithm of a product is the sum of the logarithms,
so P(X) has cumulants Kr = Nκr.
To make graphs commensurate, you need to scale the X axis by the standard deviation, which
grows like
√
N. The cumulants of the scaled graph are K′
r = N1−r/2κr.
As N →∞, these vanish for r > 2, leaving a quadratic.
If the log is a quadratic, the exponential is a Gaussian. So ˜P(X) is Gaussian.
And ﬁnally, the inverse FT of a Gaussian is also a Gaussian.
162


## Page 15


Even if the distributions are not identical, the CLT tends to apply, unless one (or two) dominates.
Most ‘errors’ ﬁt this, being compounded of many different sources.
4
Hypothesis testing
‘Hypothesis testing’ is another piece of statistical technical jargon. It just means ‘making choices’—in a
logical way—on the basis of statistical information.
– Is some track a pion or a kaon?
– Is this event signal or background?
– Is the detector performance degrading with time?
– Do the data agree with the Standard Model prediction or not?
To establish some terms: you have a hypothesis (the track is a pion, the event is signal, the detector
is stable, the Standard Model is ﬁne . . . ). and an alternative hypothesis (kaon, background, changing,
new physics needed . . . ) Your hypothesis is usually simple i.e. completely speciﬁed, but the alternative
is often composite containing a parameter (for example, the detector decay rate) which may have any
non-zero value.
4.1
Type I and type II errors
As an example, let’s use the signal/background decision. Do you accept or reject the event (perhaps
in the trigger, perhaps in your ofﬂine analysis)? To make things easy we consider the case where both
hypotheses are simple, i.e. completely deﬁned.
Suppose you measure some parameter x which is related to what you are trying to measure. It
may well be the output from a neural network or other machine learning (ML) systems. The expected
distributions for x under the hypothesis and the alternative, S and B respectively, are shown in Fig. 10.
Fig. 10: Hypothesis testing example
You impose a cut as shown—you have to put one somewhere—accepting events above x = xcut
and rejecting those below.
This means losing a fraction α of signal. This is called a type I error and α is known as the
signiﬁcance.
You admit a fraction β of background. This is called a type II error and 1 −β is the power.
You would like to know the best place to put the cut. This graph cannot tell you! The strategy for
the cut depends on three things—hypothesis testing only covers one of them.
163


## Page 16


The second is the prior signal to noise ratio. These plots are normalized to 1. The red curve
is (probably) MUCH bigger. A value of β of, say, 0.01 looks nice and small—only one in a hundred
background events get through. But if your background is 10,000 times bigger than your signal (and it
often is) you are still swamped.
The third is the cost of making mistakes, which will be different for the two types of error. You
have a trade-off between efﬁciency and purity: what are they worth? In a typical analysis, a type II error
is more serious than a type I: losing a signal event is regrettable, but it happens. Including background
events in your selected pure sample can give a very misleading result. By contrast, in medical decisions,
type I errors are much worse than type II. Telling healthy patients they are sick leads to worry and perhaps
further tests, but telling sick patients they are healthy means they don’t get the treatment they need.
4.2
The Neymann-Pearson lemma
In Fig. 10 the strategy is plain—you choose xcut and evaluate α and β. But suppose the S and B curves
are more complicated, as in Fig. 11? Or that x is multidimensional?
Fig. 11: A more complicated case for hypothesis testing
Neymann and Pearson say: your acceptance region just includes regions of greatest S(x)
B(x) (the ratio
of likelihoods). For a given α, this gives the smallest β (‘Most powerful at a given signiﬁcance’)
The proof is simple: having done this, if you then move a small region from ‘accept’ to ‘reject’
it has to be replaced by an equivalent region, to balance α, which (by construction) brings more back-
ground, increasing β.
However complicated, such a problem reduces to a single monotonic variable S
B, and you cut on
that.
4.3
Efﬁciency, purity, and ROC plots
ROC plots are often used to show the efﬁcacy of different selection variables. You scan over the cut
value (in x, for Fig. 10 or in S/B for a case like Fig. 11 and plot the fraction of background accepted (β)
against fraction of signal retained (1 −α), as shown in Fig. 12.
For a very loose cut all data is accepted, corresponding to a point at the top right. As the cut is
tightened both signal and background fractions fall, so the point moves to the left and down, though
hopefully the background loss is greater than the signal loss, so it moves more to the left than it does
downwards. As the cut is increased the line moves towards the bottom left, the limit of a very tight cut
where all data is rejected.
164


## Page 17


Fig. 12: ROC curves
A diagonal line corresponds to no discrimination—the S and B curves are identical. The further
the actual line bulges away from that diagonal, the better.
Where you should put your cut depends, as pointed out earlier, also on the prior signal/background
ratio and the relative costs of errors. The ROC plots do not tell you that, but they can be useful in
comparing the performance of different discriminators.
The name ‘ROC’ stands for ‘receiver operating characteristic’, for reasons that are lost in history.
Actually it is good to use this meaningless acronym, otherwise they get called ‘efﬁciency-purity plots’
even though they deﬁnitely do not show the purity (they cannot, as that depends on the overall sig-
nal/background ratio). Be careful, as the phrases ‘background efﬁciency’, ‘contamination’, and ‘purity’
are used ambiguously in the literature.
4.4
The null hypothesis
An analysis is often (but not always) investigating whether an effect is present, motivated by the hope
that the results will show that it is:
– Eating broccoli makes you smart.
– Facebook advertising increases sales.
– A new drug increases patient survival rates.
– The data show Beyond-the-Standard-Model physics.
To reach such a conclusion you have to use your best efforts to try, and to fail, to prove the opposite:
the Null Hypothesis H0.
– Broccoli lovers have the same or small IQ than broccoli loathers.
– Sales are independent of the Facebook advertising budget.
– The survival rates for the new treatment is the same.
– The Standard Model (functions or Monte-Carlo) describe the data.
If the null hypothesis is not tenable, you’ve proved—or at least, supported—your point.
The reason for calling α the ‘signiﬁcance’ is now clear. It is the probability that the null hypothesis
will be wrongly rejected, and you’ll claim an effect where there isn’t any.
There is a mineﬁeld of difﬁculties. Correlation is not causation. If broccoli eaters are more in-
telligent, perhaps that’s because it’s intelligent to eat green vegetables, not that vegetables make you
intelligent. One has to consider that if similar experiments are done, self-censorship will inﬂuence which
results get published. This is further discussed in Section 9.
165


## Page 18


This account is perhaps unconventional in introducing the null hypothesis at such a late stage.
Most treatments bring it in right at the start of the description of hypothesis testing, because they assume
that all decisions are of this type.
5
Estimation
What statisticians call ‘estimation’, physicists would generally call ‘measurement’.
Suppose you know the probability (density) function P(x; a) and you take a set of data {xi}.
What is the best value for a? (Sometimes one wants to estimate a property (e.g. the mean) rather than a
parameter, but this is relatively uncommon, and the methodology is the same.)
xi may be single values, or pairs, or higher-dimensional. The unknown a may be a single parame-
ter or several. If it has more than one component, these are sometimes split into ‘parameters of interest’
and ‘nuisance parameters’.
The estimator is deﬁned very broadly: an estimator ˆa(x1 . . . xN) is a function of the data that gives
a value for the parameter a. There is no ‘correct’ estimator, but some are better than others. A perfect
estimator would be:
– Consistent. ˆa(x1 . . . xN) →a as N →∞,
– Unbiased: ⟨ˆa⟩= a,
– Efﬁcient: ⟨(ˆa −a)2⟩is as small as possible,
– Invariant: ˆf(a) = f(ˆa).
No estimator is perfect—these 4 goals are incompatible. In particular the second and the fourth; if
an estimator ˆa is unbiased for a then
√
ˆa is not an unbiased estimator of √a.
5.1
Bias
Suppose we estimate the mean by taking the obvious3 ˆµ = x
⟨ˆµ⟩=

 1
N
P xi

= 1
N
P µ = µ.
So there is no bias. This expectation value of this estimator of µ is just µ itself. By contrast
suppose we estimate the variance by the apparently obvious ˆV = x2 −x2.
Then
D
ˆV
E
=
D
x2E
−
D
x2E
.
The ﬁrst term is just
D
x2E
. To make sense of the second term, note that ⟨x⟩= ⟨x⟩and add and
subtract ⟨x⟩2 to get
D
ˆV
E
=
D
x2E
−⟨x⟩2 −(
D
x2E
−⟨x⟩2)
D
ˆV
E
= V (x) −V (x) = V −V
N = N−1
N V .
So the estimator is biased! ˆV will, on average, give too small a value.
This bias, like any known bias, can be corrected for. Using ˆV =
N
N−1(x2 −x2) corrects the bias.
The familiar estimator for the standard deviation follows: ˆσ =
qP
i(xi−x)2
N−1
.
(Of course this gives a biased estimate of σ. But V is generally more important in this context.)
3Note the difference between ⟨x⟩which is an average over a PDF and x which denotes the average over a particular sample:
both are called ‘the mean x’.
166


## Page 19


5.2
Efﬁciency
Somewhat surprisingly, there is a limit to the efﬁciency of an estimator: the minimum variance bound
(MVB), also known as the Cramér-Rao bound.
For any unbiased estimator ˆa(x), the variance is bounded
V (ˆa) ≥−
1
D
d2 ln L
da2
E =
1
D  d ln L
da
2E
.
(12)
L is the likelihood (as introduced in Section 2.6.2) of a sample of independent measurements, i.e.
the probability for the whole data sample for a particular value of a. It is just the product of the individual
probabilities:
L(a; x1, x2, ...xN) = P(x1; a)P(x2; a)...P(xN; a).
We will write L(a; x1, x2, ...xN) as L(a; x) for simplicity.
Proof. Proof of the MVB
Unitarity requires
R
P(x; a) dx =
R
L(a; x) dx = 1
Differentiate wrt a:
0 =
Z dL
da dx =
Z
Ld ln L
da
dx =
d ln L
da

(13)
If ˆa is unbiased ⟨ˆa⟩=
R
ˆa(x)P(x; a) dx =
R
ˆa(x)L(a; x) dx = a
Differentiate wrt a:
1 =
R
ˆa(x)dL
da dx =
R
ˆaLd ln L
da dx
Subtract Eq. 13 multiplied by a, and get
R
(ˆa −a)d ln L
da Ldx = 1
Invoke the Schwarz inequality
R
u2 dx
R
v2 dx ≥
 R
uv dx
2 with u ≡(ˆa −a)
√
L, v ≡d ln L
da
√
L
Hence
R
(ˆa −a)2L dx
R   d ln L
da
2 L dx ≥1
D
(ˆa −a)2E
≥1/
*dlnL
da
2+
(14)
Differentiating Eq. 13 again gives
d
da
R
Ld ln L
da dx =
R dL
da
d ln L
da dx +
R
Ld2 ln A
da2
dx =
D  d ln L
da
2E
+
D
d2 ln L
da2
E
= 0,
hence
D  d ln L
da
2E
= −
D
d2 ln L
da2
E
.
This is the Fisher information referred to in Section 2.6.4. Note how it is intrinsically positive.
5.3
Maximum likelihood estimation
The maximum likelihood (ML) estimator just does what it says: a is adjusted to maximise the likelihood
of the sample (for practical reasons one actually maximises the log likelihood, which is a sum rather than
a product).
Maximise ln L =
X
i
ln P(xi; a)
,
(15)
d ln L
da

ˆa
= 0
.
(16)
167


## Page 20


The ML estimator is very commonly used. It is not only simple and intuitive, it has lots of nice
properties.
– It is consistent.
– It is biased, but bias falls like 1/N.
– It is efﬁcient for the large N.
– It is invariant—doesn’t matter if you reparametrize a.
A particular maximisation problem may be solved in 3 ways, depending on the complexity
1. Solve Eq. 16 algebraically,
2. Solve Eq. 16 numerically, and
3. Solve Eq. 15 numerically.
5.4
Least squares
Least squares estimation follows from maximum likelihood estimation. If you have Gaussian measure-
ments of y taken at various x values, with measurement error σ, and a prediction y = f(x; a) then the
Gaussian probability
P(y; x, a) =
1
σ
√
2πe−(y−f(x,a))2/2σ2
gives the log likelihood
ln L = −P (yi−f(xi;a))2
2σ2
i
+ constants.
To maximise ln L, you minimise χ2 = P (yi−f(xi;a))2
σ2
i
, hence the name ‘least squares’.
Differentiating gives the normal equations: P (yi−f(xi;a))
σ2
i
f′(xi; a) = 0.
If f(x; a) is linear in a then these can be solved exactly. Otherwise an iterative method has to be
used.
5.5
Straight line ﬁts
As a particular instance of least squares estimation, suppose the function is y = mx + c, and assume
all σi are the same (the extension to the general case is straightforward). The normal equations are then
P(yi −mxi −c)xi = 0 and P(yi −mxi −c) = 0 , for which the solution, shown in Fig. 13, is
m = xy−x ,y
x2−x2 , c = y −mx .
Statisticians call this regression. Actually there is a subtle difference, as shown in Fig. 14.
The straight line ﬁt considers well-deﬁned x values and y values with measurement errors—if
it were not for those errors then presumably the values would line up perfectly, with no scatter. The
scatter in regression is not caused by measurement errors, but by the fact that the variables are linked
only loosely.
The history of regression started with Galton, who measured the heights of fathers and their (adult)
sons. Tall parents tend to have tall children so there is a correlation. Because the height of a son depends
not just on his paternal genes but on many factors (maternal genes, diet, childhood illnesses . . . ), the
points do not line up exactly—and using a high accuracy laser interferometer to do the measurements,
rather than a simple ruler, would not change anything.
Galton, incidentally, used this to show that although tall fathers tend to have tall sons, they are
not that tall. An outstandingly tall father will have (on average) quite tall children, and only tallish
grandchildren. He called this ‘Regression towards mediocrity’, hence the name.
168


## Page 21


Fig. 13: A straight line ﬁt
Fig. 14: A straight line ﬁt (left) and linear regression (right)
It is also true that tall sons tend to have tall fathers—but not that tall—and only tallish grandfathers.
Regress works in both directions!
Thus for regression there is always an ambiguity as to whether to plot x against y or y against x.
For a straight line ﬁt as we usually meet them this does not arise: one variable is precisely speciﬁed and
we call that one x, and the one with measurement errors is y.
5.6
Fitting histograms
When ﬁtting a histogram the error is given by Poisson statistics for the number of events in each bin.
There are 4 methods of approaching this problem—in order of increasing accuracy and decreasing
speed. It is assumed that the bin width W is narrow, so that f(xi, a) =
R xi+W
xi
P(x, a) dx can be
approximated by fi(xi; a) = P(xi; a) × W. W is almost always the same for all bins, but the rare cases
of variable bin width can easily be included.
1. Minimise χ2 = P
i
(ni−fi)2
ni
. This is the simplest but clearly breaks if ni = 0.
2. Minimise χ2 = P
i
(ni−fi)2
fi
. Minimising the Pearson χ2 (which is valid here) avoids the division-
by-zero problem. It assumes that the Poisson distribution can be approximated by a Gaussian.
3. Maximise ln L = P ln(e−fifni
i /ni!) ∼P ni ln fi −fi. This, known as binned maximum likeli-
hood, remedies that assumption.
4. Ignore bins and maximise the total likelihood. Sums run over Nevents not Nbins. So if you have
large data samples this is much slower. You have to use it for sparse data, but of course in such
cases the sample is small and the time penalty is irrelevant.
169


## Page 22


Fig. 15: Fitting a histogram
Which method to use is something you have to decide on a case by case basis. If you have bins
with zero entries then the ﬁrst method is ruled out (and removing such bins from the ﬁt introduces bias so
this should not be done). Otherwise, in my experience, the improvement in adopting a more complicated
method tends to be small.
6
Errors
Estimation gives you a value for the parameter(s) that we have called a. But you also—presumably—
want to know something about the uncertainty on that estimate. The maximum likelihood method pro-
vides this.
6.1
Errors from likelihood
For large N, the ln L(a, x) curve is a parabola, as shown in Fig. 16.
Fig. 16: Reading off the error from a Maximum Likelihood ﬁt
At the maximum, a Taylor expansion gives ln L(a) = ln L(ˆa) + 1
2(a −ˆa)2 d2 ln L
da2
. . .
170


## Page 23


The maximum likelihood estimator saturates the MVB, so
Vˆa = −1/
*
d2 ln L
da2
+
σˆa =
v
u
u
t−
1
d2 ln L
da2
.
(17)
We approximate the expectation value
D
d2 ln L
da2
E
by the actual value in this case d2 ln L
da2

a=ˆa (for a
discussion of the introduced inaccuracy, see Ref. [12]).
This can be read off the curve, as also shown in Fig. 16. The maximum gives the estimate. You
then draw a line 1
2 below that (of course nowadays this is done within the code, not with pencil and ruler,
but the visual image is still valid). This line ln L(a) = ln L(ˆa) −1
2 intersects the likelihood curve at the
points a = ˆa ± σˆa. If you are working with χ2, L ∝e−1
2 χ2
so the line is ∆χ2 = 1.
This gives σ, or 68% errors. You can also take ∆ln L = −2 to get 2 sigma or 95% errors, or −4.5
for 3 sigma errors as desired. For large N these will all be consistent.
6.2
Combining errors
Having obtained—by whatever means—errors σx, σy... how does one combine them to get errors on
derived quantities f(x, y...), g(x, y, ...)?
Suppose f = Ax + By + C, with A, B and C constant. Then it is easy to show that
Vf =
D
(f −⟨f⟩)2E
=
D
(Ax + By + C −⟨Ax + By + C⟩)2E
= A2(
D
x2E
−⟨x⟩2) + B2(
D
y2E
−⟨y⟩2) + 2AB(⟨xy⟩−⟨x⟩⟨y⟩)
= A2Vx + B2Vy + 2AB Covxy
.
(18)
If f is not a simple linear function of x and y then one can use a ﬁrst order Taylor expansion to
approximate it about a central value f0(x0, y0)
f(x, y) ≈f0 +
∂f
∂x

(x −x0) +
∂f
∂y

(y −y0)
(19)
and application of Eq. 18 gives
Vf =
∂f
∂x
2
Vx +
∂f
∂y
2
Vy + 2
∂f
∂x
 ∂f
∂y

Covxy
(20)
writing the more familiar σ2 instead of V this is equivalent to
σ2
f =
∂f
∂x
2
σ2
x +
∂f
∂y
2
σ2
y + 2ρ
∂f
∂x
 ∂f
∂y

σxσy
.
(21)
If x and y are independent, which is often but not always the case, this reduces to what is often
known as the ‘combination of errors’ formula
σ2
f =
∂f
∂x
2
σ2
x +
∂f
∂y
2
σ2
y
.
(22)
171


## Page 24


Extension to more than two variables is trivial: an extra squared term is added for each and an
extra covariance term for each of the variables (if any) with which it is correlated.
This can be expressed in language as errors add in quadrature. This is a friendly fact, as the result
is smaller than you would get from arithmetic addition. If this puzzles you, it may be helpful to think
of this as allowing for the possibility that a positive ﬂuctuation in one variable may be cancelled by a
negative ﬂuctuation in the other.
There are a couple of special cases we need to consider. If f is a simple product, f = Axy, then
Eq. 22 gives
σ2
f = (Ay)2σ2
x + (Ax)2σ2
y ,
which, dividing by f2, can be written as
σf
f
2
=
σx
x
2
+
σy
y
2
.
(23)
Furthermore this also applies if f is a simple quotient, f = Ax/y or Ay/x or even A/(xy).
This is very elegant, but it should not be overemphasised. Equation 23 is not fundamental: it only
applies in certain cases (products or quotients). Equation 22 is the fundamental one, and Eq. 23 is just a
special case of it.
For example: if you measure the radius of a cylinder as r = 123 ± 2 mm and the height
as h = 456 ± 3 mm then the volume πr2h is π × 1232 × 456 = 21673295 mm3 with error
q
(2πrh)2 × σ2
r + (πr2)2 × σ2
h = 719101, so one could write it as v = (216.73 ± 0.72) × 105 mm3.
The surface area 2πr2 + 2πrh is 2π × 1232 + 2π × 123 × 456 = 447470 mm2 with error
q
(4πr + 2πh)2σ2
r + (2πr)2σ2
h = 9121 mm2—so one could write the result as a = (447.5 ± 9.1) ×
103 mm2.
A full error analysis has to include the treatment of the covariance terms—if only to show that they
can be ignored. Why should the x and y in Eq. 20 be correlated? For direct measurements very often (but
not always) they will not be. However the interpretation of results is generally a multistage process. From
raw numbers of events one computes branching ratios (or cross sections...), from which one computes
matrix elements (or particle masses...). Many quantities of interest to theorists are expressed as ratios of
experimental numbers. And in this interpretation there is plenty of scope for correlations to creep into
the analysis.
For example, an experiment might measure a cross section σ(pp →X) from a number of observed
events N in the decay channel X →µ+µ−. One would use a formula
σ =
N
BηL ,
where η is the efﬁciency for detecting and reconstructing an event, B is the branching ratio for X →
µ+µ−, and L is the integrated luminosity. These will all have errors, and the above prescription can be
applied.
However it might also use the X →e+e−channel and then use
σ′ =
N′
B′η′L .
Now σ and σ′ are clearly correlated; even though N and N′ are independent, the same L appears
in both. If the estimate of L is on the high side, that will push both σ and σ′ downwards, and vice versa.
On the other hand, if a second experiment did the same measurement it would have its own N, η
and L, but would be correlated with the ﬁrst through using the same branching ratio (taken, presumably,
from the Particle Data Group).
172


## Page 25


To calculate correlations between results we need the equivalent of Eq. 18
Covfg = ⟨(f −⟨f⟩)(g −⟨g⟩)⟩
=
∂f
∂x
 ∂g
∂x

σ2
x
,
(24)
This can all be combined in the general formula which encapsulates all of the ones above
Vf = GVx ˜G
,
(25)
where Vx is the covariance matrix of the primary quantities (often, as pointed out earlier, this is diago-
nal), Vf is the covariance matrix of secondary quantities, and
Gij = ∂fi
∂xj
.
(26)
The G matrix is rectangular but need not be square. There may be more—or fewer—derived
quantities than primary quantities. The matrix algebra of G and its transpose ˜G ensures that the numbers
of rows and columns match for Eq. 25.
To show how this works, we go back to our earlier example of a cylinder. v and a are correlated:
if r or h ﬂuctuate upwards (or downwards), that makes both volume and area larger (or smaller). The
matrix G is
G =

2πrh
πr2
2π(2r + h)
2πr

=
352411
47529
4411
773

,
(27)
the variance matrix Vx is
Vx =
4
0
0
9

and Eq. 25 gives
Vf =
517.1 × 109
6.548 × 109
6.548 × 109
83.20 × 106

from which one obtains, as before, σv = 719101, σa = 9121 but also ρ = 0.9983.
This can be used to provide a useful example of why correlation matters. Suppose you want to
know the volume to surface ratio, z = v/a, of this cylinder. Division gives z = 21673295/447470 =
48.4352 mm.
If we just use Eq. 22 for the error, this gives σz = 1.89 mm. Including the correlation term, as in
Eq. 21, reduces this to 0.62 mm—three times smaller. It makes a big difference.
We can also check that this is correct, because the ration v
a can be written as
πr2h
2πr2+2πrh, and
applying the uncorrelated errors of the original r and h to this also gives an error of 0.62 mm.
As a second, hopefully helpful, example we consider a simple straight line ﬁt, y = mx + c.
Assuming that all the N y values are measured with the same error σ, least squares estimation gives the
well known results
m = xy −x y
x2 −x2
c = y x2 −xy x
x2 −x2
.
(28)
173


## Page 26


For simplicity we write D = 1/(x2 −x2). The differentials are
∂m
∂yi
= D
N (xi −x)
∂c
∂yi
= D
N (x2 −xix)
,
from which, remembering that the y values are uncorrelated,
Vm = σ2
D
N
2 X
(xi −x)2 = σ2 D
N
Vc = σ2
D
N
2 X
(x2 −xix)2 = σ2x2 D
N
Covmc = σ2
D
N
2 X
(xi −x)(x2 −xix) = −σ2xD
N
from which the correlation between m and c is just ρ = −x/
q
x2.
This makes sense. Imagine you’re ﬁtting a straight line through a set of points with a range of
positive x values (so x is positive). If the rightmost point happened to be a bit higher, that would push
the slope m up and the intercept c down. Likewise if the leftmost point happened to be too high that
would push the slope down and the intercept up. There is a negative correlation between the two ﬁtted
quantities.
Does it matter? Sometimes. Not if you’re just interested in the slope—or the constant. But suppose
you intend to use them to ﬁnd the expected value of y at some extrapolated x. Equation 21 gives
y = mx + c ±
q
x2σ2
m + σ2
c + 2xρσmσc
and if, for a typical case where x is positive so ρ is negative, you leave out the correlation term you will
overestimate your error.
This is an educational example because this correlation can be avoided. Shifting to a co-ordinate
system in which x is zero ensures that the quantities are uncorrelated. This is equivalent to rewriting the
well-known y = mx+c formula as y = m(x−x)+c′, where m is the same as before and c′ = c+mx.
m and c′ are now uncorrelated, and error calculations involving them become a lot simpler.
6.3
Asymmetric errors
So what happens if you plot the likelihood function and it is not symmetric like Fig. 16 but looks more
like Fig. 17? This arises in many cases when numbers are small. For instance, in a simple Poisson count
suppose you observe one event. P(1; λ) = λe−λ is not symmetric: λ = 1.5 is more likely to ﬂuctuate
down to 1 than λ = 0.5 is to ﬂuctuate up to 1.
You can read off σ+ and σ−from the two ∆ln L = −1
2 crossings, but they are different. The
result can then be given as a
+σ+
−σ−. What happens after that?
The ﬁrst advice is to avoid this if possible. If you get ˆa = 4.56 with σ+ = 1.61, σ−= 1.59 then
quote this as 4.6 ± 1.6 rather than 4.56+1.61
−1.59. Those extra signiﬁcant digits have no real meaning. If you
can convince yourself that the difference between σ+ and σ−is small enough to be ignored then you
should do so, as the alternative brings in a whole lot of trouble and it’s not worth it.
But there will be some cases where the difference is too great to be swept away, so let’s consider
that case. There are two problems that arise: combination of measurements and combination of errors.
174


## Page 27


Fig. 17: An asymmetric likelihood curve
6.3.1
Combination of measurements with asymmetric errors
Suppose you have two measurements of the same parameter a:
ˆa1
+σ+
1
−σ−
1 and ˆa2
+σ+
2
−σ−
2 and you want to
combine them to give the best estimate and, of course, its error. For symmetric errors the answer is well
established to be ˆa = ˆa1/σ2
1+ˆa2/σ2
2
1/σ2
1+1/σ2
2 .
If you know the likelihood functions, you can do it. The joint likelihood is just the sum. This is
shown in Fig. 18 where the red and green curves are measurements of a. The log likelihood functions
just add (blue), from which the peak is found and the ∆ln L = −1
2 errors read off.
Fig. 18: Combination of two likelihood functions (red and green) to give the total (blue)
But you don’t know the full likelihood function: just 3 points (and that it had a maximum at the
second). There are, of course, an inﬁnite number of curves that could be drawn, and several models have
been tried (cubics, constrained quartic...) on likely instances—see Ref. [13] for details. Some do better
than others. The two most plausible are
ln L = −1
2

a −ˆa
σ + σ′(a −ˆa)
2
and
(29)
ln L = −1
2
(a −ˆa)2
V + V ′(a −ˆa)
.
(30)
175


## Page 28


These are similar to the Gaussian parabola, but the denominator is not constant. It varies with the
value of a, being linear either in the standard deviation or in the variance. Both are pretty good. The ﬁrst
does better with errors on log a (which are asymmetric if a is symmetric: such asymmetric error bars are
often seen on plots where the y axis is logarithmic), the second does better with Poisson measurements.
From the 3 numbers given one readily obtains
σ = 2σ+σ−
σ+ + σ−
σ′ = σ+ −σ−
σ+ + σ−
(31)
or, if preferred
V = σ+σ−
V ′ = σ+ −σ−
.
(32)
From the total likelihood you then ﬁnd the maximum of sum, numerically, and the ∆ln L = −1
2
points.
Code for doing this is available on GitHub4 in both R and Root.
Fig. 19: Combining three asymmetric measurements
An example is shown in Fig. 19. Combining 1.9+0.7
−0.5, 2.4+0.6
−0.8 and 3.1+0.5
−0.4 gives 2.76+0.29
−0.27 .
6.3.2
Combination of errors for asymmetric errors
For symmetric errors, given x ± σx, y ± σy, (and ρxy = 0) the error on f(x, y) is the sum in quadrature:
σ2
f =

∂f
∂x
2
σ2
x +

∂f
∂y
2
σ2
y. What is the equivalent for the error on f(x, y) when the errors are asym-
metric, x+σ+
x
−σ−
x , y
+σ+
y
−σ−
y ? Such a problem arises frequently at the end of an analysis when the systematic
errors from various sources are all combined.
The standard procedure—which you will see done, though it has not, to my knowledge, been
written down anywhere—is to add the positive and negative errors in quadrature separately: σ+
f
2 =
σ+
x
2 + σ+
y
2,
σ−
f
2 = σ−
x
2 + σ−
y
2. This looks plausible, but it is manifestly wrong as it breaks the central
limit theorem.
To see this, suppose you have to average N i.i.d. variables each with the same errors which are
asymmetric: σ+ = 2σ−. The standard procedure reduces both σ+ and σ−by a factor 1/
√
N, but the
skewness remains. The positive error is twice the negative error. This is therefore not Gaussian, and
never will be, even as N →∞.
4https://github.com/RogerJBarlow/Asymmetric-Errors
176


## Page 29


You can see what’s happening by considering the combination of two of these measurements. They
both may ﬂuctuate upwards, or they both may ﬂuctuate downwards, and yes, the upward ﬂuctuation will
be, on average, twice as big. But there is a 50% chance of one upward and one downward ﬂuctuation,
which is not considered in the standard procedure.
For simplicity we write zi = ∂f
∂xi (xi −x0
i ), the deviation of the parameter from its nominal value,
scaled by the differential. The individual likelihoods are again parametrized as Gaussian with a linear
dependence of the standard deviation or of the variance, giving
ln L(⃗z) = −1
2
X
i

zi
σi + σ′
izi
2
or
−1
2
X
i
z2
i
Vi + V ′
i zi
,
(33)
where σ, σ′, V, V ′ are obtained from Eqs. 31 or 32.
The zi are nuisance parameters (as described later) and can be removed by proﬁling. Let u = P zi
be the total deviation in the quoted f arising from the individual deviations. We form ˆL(u) as the
maximum of L(⃗z) subject to the constraint P
i zi = u. The method of undetermined multipliers readily
gives the solution
zi = u
wi
P
j wj
,
(34)
where
wi = (σi + σ′
izi)3
2σi
or
(Vi + V ′
i zi)2
2Vi + V ′
i zi
.
(35)
The equations are nonlinear, but can be solved iteratively. At u = 0 all the zi are zero. Increasing
(or decreasing) u in small steps, Eqs. 34 and 35 are applied successively to give the zi and the wi:
convergence is rapid. The value of u which maximises the likelihood should in principle be applied as a
correction to the quoted result.
Programs to do this are also available on the GitHub site.
As an example, consider a counting experiment with a number of backgrounds, each determined
by an ancillary Poisson experiment, and that for simplicity each background was determined by running
the apparatus for the same time as the actual experiment. (In practice this is unlikely, but scale factors
can easily be added.)
Suppose two backgrounds are measured, one giving four events and the other ﬁve. These would
be reported, using ∆lnL = −1
2 errors, as 4+2.346
−1.682 and 5+2.581
−1.916. The method, using linear V , gives the
combined error on the background count as +3.333
−2.668.
In this simple case we can check the result against the total background count of nine events,
which has errors +3.342
−2.676. The agreement is impressive. Further examples of the same total, partitioned
differently, are shown in table 1.
Inputs
Linear σ
Linear V
σ−
σ+
σ−
σ+
4+5
2.653
3.310
2.668
3.333
3+6
2.653
3.310
2.668
3.333
2+7
2.653
3.310
2.668
3.333
2+7
2.653
3.310
2.668
3.333
3+3+3
2.630
3.278
2.659
3.323
1+1+1+1+1+1+1+1+1
2.500
3.098
2.610
3.270
Table 1: Various combinations of Poisson errors. The target value is σ−= 2.676, σ+ = 3.342
177


## Page 30


6.4
Errors in 2 or more dimensions
For 2 (or more) dimensions, one plots the log likelihood and deﬁnes regions using contours in ∆ln L (or
∆χ2 ≡−2∆ln L). An example is given in Fig. 20.
Fig. 20: CMS results on CV and CF , taken from Ref. [14]
The link between the ∆ln L values and the signiﬁcance changes. In 1D, there is a 68% probability
of a measurement falling within 1 σ. In 2D, a 1σ square would give a probability 0.682 = 47%. If one
rounds off the corners and draws a 1σ contour at ∆ln L = −1
2 this falls to 39%. To retrieve the full 68%
one has to draw a contour at ∆ln L = −1.14, or equivalently ∆χ2 = 2.27. For 95% use ∆χ2 = 5.99 or
∆ln L = −3.00.
The necessary value is obtained from the χ2 distribution—described later. It can be found by the
R function qchisq(p,n) or the Root function TMath::ChiSquareQuantile(p,n), where the desired
probability p and number of degrees of freedom n are the arguments given.
6.4.1
Nuisance parameters
In the example of Fig. 20, both CV and CF are interesting. But in many cases one is interested only in
one (or some) of the quantities and the others are ‘nuisance parameters’ that one would like to remove,
reducing the dimensionality of the quoted result. There are two methods of doing this, one (basically)
frequentist and one Bayesian.
The frequentist uses the proﬁle likelihood technique. Suppose that there are two parameters, a1
and a2, where a2 is a nuisance parameter, and so one wants to reduce the joint likelihood function
L(x; a1, a2) to some function ˆL(a1). To do this one scans across the values of a1 and inserts ˆˆa2(a1), the
value of a2 which maximises the likelihood for that particular a1
ˆL(x, a1) = L(a1, ˆˆa2(a1))
(36)
and the location of the maximum and the ∆ln L = 1
2 errors are read off as usual.
178


## Page 31


To see why this works—though this is not a very rigorous motivation—suppose one had a likeli-
hood function as shown in Fig. 21.
Fig. 21: Justiﬁcation of the likelihood proﬁle method
The horizontal axis is for the parameter of interest, a1, and the vertical for the nuisance parameter
a2.
Different values of a2 give different results (central and errors) for a1.
If it is possible to transform to a′
2(a1, a2) so that L factorises, then we can write L(a1, a′
2) =
L1(a1)L2(a′
2): this is shown in the plot on the right. We suppose that this is indeed possible. In the case
here, and other not-too-complicated cases, it clearly is, although it will not be so in more complicated
topologies with multiple peaks.
Then using the transformed graph, whatever the value of a′
2, one would get the same result for a1.
Then one can present this result for a1, independent of anything about a′
2.
There is no need to factorise explicitly: the path of central a′
2 value as a function of a1 (the central
of the 3 lines on the right hand plot) is the path of the peak, and that path can be located in the ﬁrst plot
(the transformation only stretches the a2 axis, it does not change the heights).
The Bayesian method uses the technique called marginalisation, which just integrates over
a2. Frequentists can not do this as they are not allowed to integrate likelihoods over the parameter:
R
P(x; a) dx is ﬁne, but
R
P(x; a) da is off limits. Nevertheless this can be a very helpful alternative to
proﬁling, specially for many nuisance parameters. But if you use it you must be aware that this is strictly
Bayesian. Reparametrizing a2 (or choosing a different prior) will give different results for a1. In many
cases, where the effect of the nuisance parameter is small, this does not have a big effect on the result.
6.5
Systematic errors
This can be a touchy subject. There is a lot of bad practice out there. Muddled thinking and following
traditional procedures without understanding. When statistical errors dominated, this didn’t matter much.
In the days of particle factories and big data samples, it does.
6.5.1
What is a systematic error?
Consider these two quotations, from eminent and widely-read authorities.
R. Bevington deﬁnes
179


## Page 32


‘Systematic error: reproducible inaccuracy introduced by faulty equipment, calibration,
or technique.’ [15],
whereas J. Orear writes
‘Systematic effects is a general category which includes effects such as background,
scanning efﬁciency, energy resolution, variation of counter efﬁciency with beam position,
and energy, dead time, etc. The uncertainty in the estimation of such a systematic effect is
called a systematic error.’ [16].
Read these carefully and you will see that they are contradictory. They are not talking about the
same thing. Furthermore, Orear is RIGHT and Bevington is WRONG—as are a lot of other books and
websites.
We teach undergraduates the difference between measurement errors, which are part of doing
science, and mistakes. They are not the same. If you measure a potential of 12.3 V as 12.4 V, with a
voltmeter accurate to 0.1V, that is ﬁne. Even if you measure 12.5 V. If you measure it as 124 V, that is a
mistake.
In the quotes above, Bevington is describing systematic mistakes (the word ‘faulty’ is the key)
whereas Orear is describing systematic uncertainties—which are ‘errors’ in the way we use the term.
There is a case for saying one should avoid the term ‘systematic error’ and always use ‘uncertainty’
or ’mistake’. This is probably impossible. But you should always know which you mean.
Restricting ourselves to uncertainties (we will come back to mistakes later) here are some typical
examples:
– Track momenta from pi = 0.3Bρi have statistical errors from ρ and systematic errors from B,
– Calorimeter energies from Ei = αDi + β have statistical errors from the digitised light signal Di
and systematic errors from the calibration α, β, and
– Branching ratios from Br = ND−B
ηNT
have statistical errors from ND and systematic errors from
efﬁciency η, background B, total NT .
Systematic uncertainties can be either Bayesian or Frequentist. There are clearly frequentist cases
where errors have been determined by an ancillary experiment (real or simulated), such as magnetic ﬁeld
measurements, calorimeter calibration in a testbeam, and efﬁciencies from Monte Carlo simulations.
(Sometimes the ancillary experiment is also the main experiment—e.g. in estimating background from
sidebands.) There are also uncertainties that can only be Bayesian, e.g. when a theorist tells you that
their calculation is good to 5% (or whatever) or an experimentalist afﬁrms that the calibration will not
have shifted during the run by more than 2% (or whatever).
6.5.2
How to handle them: correlations
Working with systematic errors is actually quite straightforward. They obey the same rules as statistical
uncertainties.
We write x = 12.2±0.3±0.4 ‘where the ﬁrst error is statistical and the second is systematic’, but
it would be valid to write x = 12.2±0.5. For single measurement the extra information given by the two
separate numbers is small. (In this case it just tells you that there is little to be gained by increasing the
size of the data sample). For multiple measurements e.g. xa = 12.2 ± 0.3, xb = 17.1 ± 0.4, all ± 0.5 the
extra information is important, as results are correlated. Such cases arise, for example, in cross section
measurements with a common luminosity error, or branching ratios with common efﬁciency.
Such a correlation means that taking more measurements and averaging does not reduce the error.
Also there is no way to estimate σsys from the data—hence no check on the goodness of ﬁt from a χ2
test.
180


## Page 33


6.5.3
Handling systematic errors in your analysis
It is useful to consider systematic errors as having three types:
1. Uncertainty in an explicit continuous parameter. For example an uncertainty in efﬁciency, back-
ground and luminosity in determining a branching ratio or cross section. For these the standard
combination of errors formula and algebra are usable, just like undergraduate labs.
2. Uncertainty in an implicit continuous parameter. For example: MC tuning parameters (σpT , po-
larisation . . . ). These are not amenable to algebra. Instead one calculates the result for different
parameter values, typically at ±σ, and observes the variation in the result, as illustrated in Fig. 22.
Fig. 22: Evaluating the effect of an implicit systematic uncertainty
Hopefully the effect is equal but opposite—if not then one can reluctantly quote an asymmetric
error. Also your analysis results will have errors due to ﬁnite MC statistics. Some people add these
in quadrature. This is wrong. The technically correct thing to do is to subtract them in quadrature,
but this is not advised.
3. Discrete uncertainties:
These typically occur in model choices.
Using a different Monte Carlo for background—or
signal—gives you a (slightly) different result. How do you include this uncertainty?
The situation depends on the status of the models. Sometimes one is preferred, sometimes they are
all equal (more or less).
With 1 preferred model and one other, quote R1 ± |R1 −R2| .
With 2 models of equal status, quote R1+R2
2
± |R1−R2
√
2
| .
With N models: take R ±
q
N
N−1(R
2 −R
2) or similar mean value.
2 extreme models: take R1+R2
2
± |R1−R2|
√
12
.
These are just ballpark estimates. Do not push them too hard. If the difference is not small, you
have a problem—which can be an opportunity to study model differences.
6.5.4
Checking the analysis
“As we know, there are known knowns. There are things we know that we know. There are known
181


## Page 34


unknowns. That is to say, there are things that we know we don’t know. But there are also unknown
unknowns. There are things we don’t know we don’t know."
Donald H. Rumsfeld
Errors are not mistakes—but mistakes still happen. Statistical tools can help ﬁnd them. Check
your result by repeating the analysis with changes which should make no difference:
– Data subsets,
– Magnet up/down,
– Different selection cuts,
– Changing histogram bin size and ﬁt ranges,
– Changing parametrization (including order of polynomial),
– Changing ﬁt technique,
– Looking for impossibilities,
– . . .
The more tests the better. You cannot prove the analysis is correct. But the more tests it survives
the more likely your colleagues5 will be to believe the result.
For example: in the paper reporting the ﬁrst measurement of CP violation in B mesons the BaBar
Collaboration [17] reported
‘. . . consistency checks, including separation of the decay by decay mode, tagging cat-
egory and Btag ﬂavour . . . We also ﬁt the samples of non-CP decay modes for sin 2β with
no statistically signiﬁcant difference found.’
If your analysis passes a test then tick the box and move on. Do not add the discrepancy to the
systematic error. Many people do—and your supervisor and your review committee may want you to do
so. Do not give in.
– It’s illogical,
– It penalises diligence, and
– Errors get inﬂated.
If your analysis fails a test then worry!
– Check the test. Very often this turns out to be faulty.
– Check the analysis. Find mistake, enjoy improvement.
– Worry. Consider whether the effect might be real. (E.g. June’s results are different from July’s.
Temperature effect? If so can (i) compensate and (ii) introduce implicit systematic uncertainty).
– Worry harder. Ask colleagues, look at other experiments.
Only as a last resort, add the term to the systematic error. Remember that this could be a hint of
something much bigger and nastier.
5and eventually even you
182


## Page 35


6.5.5
Clearing up a possible confusion
What’s the difference between?
Evaluating implicit systematic errors: vary lots of parameters, see what happens to the result, and
include in systematic error.
Checks: vary lots of parameters, see what happens to the result, and don’t include in systematic
error.
If you ﬁnd yourself in such a situation there are actually two ways to tell the difference.
(1) Are you expecting to see an effect? If so, it’s an evaluation, if not, it’s a check.
(2) Do you clearly know how much to vary them by? If so, it’s an evaluation. If not, it’s a check.
These cover even complicated cases such as a trigger energy cut where the energy calibration is
uncertain—and it may be simpler to simulate the effect by varying the cut rather than the calibration.
6.5.6
So ﬁnally:
1. Thou shalt never say ‘systematic error’ when thou meanest ‘systematic effect’ or ‘systematic mis-
take’.
2. Thou shalt know at all times whether what thou performest is a check for a mistake or an evaluation
of an uncertainty.
3. Thou shalt not incorporate successful check results into thy total systematic error and make thereby
a shield to hide thy dodgy result.
4. Thou shalt not incorporate failed check results unless thou art truly at thy wits’ end.
5. Thou shalt not add uncertainties on uncertainties in quadrature. If they are larger than chickenfeed
thou shalt generate more Monte Carlo until they shrink.
6. Thou shalt say what thou doest, and thou shalt be able to justify it out of thine own mouth; not the
mouth of thy supervisor, nor thy colleague who did the analysis last time, nor thy local statistics
guru, nor thy mate down the pub.
Do these, and thou shalt ﬂourish, and thine analysis likewise.
7
Goodness of ﬁt
You have the best ﬁt model to your data—but is it good enough? The upper plot in Fig. 23 shows the
best straight line through a set of points which are clearly not well described by a straight line. How can
one quantify this?
You construct some measure of agreement—call it t—between the model and the data. Conven-
tion: t ≥0, t = 0 is perfect agreement. Worse agreement implies larger t. The null hypothesis H0 is that
the model did indeed produce this data. You calculate the p−value: the probability under H0 of getting
a t this bad, or worse. This is shown schematically in the lower plot. Usually this can be done using
known algebra—if not one can use simulation (a so-called ‘Toy Monte Carlo’).
7.1
The χ2 distribution
The overwhelmingly most used such measure of agreement is the quantity χ2
χ2 =
N
X
1
yi −f(xi)
σi
2
.
(37)
In words: the total of the squared differences between prediction and data, scaled by the expected error.
Obviously each term will be about 1, so
D
χ2E
≈N, and this turns out to be exact.
183


## Page 36


Fig. 23: The best ﬁt to the data may not be good enough
The distribution for χ2 is given by
P(χ2; N) =
1
2N/2Γ(N/2)
χN−2e−χ2/2
(38)
shown in Fig. 24, though this is in fact not much used: one is usually interested in the p−value,
the probability (under the null hypothesis) of getting a value of χ2 as large as, or larger than, the
one observed. This can be found in ROOT with TMath::Prob(chisquared,ndf), and in R from
1-pchisq(chisquared,ndf).
Thus for example with N = 10, χ2 = 15 then p = 0.13. This is probably OK. But for N =
10, χ2 = 20 then p = 0.03, which is probably not OK.
If the model has parameters which have been adjusted to ﬁt the data, this clearly reduces χ2. It is
a very useful fact that the result also follows a χ2 distribution for NDF = Ndata −Nparameters where
NDF is called the ‘number of degrees of freedom’.
184


## Page 37


Fig. 24: The χ2 distribution for various N
If your χ2 is suspiciously big, there are 4 possible reasons:
1. Your model is wrong,
2. Your data are wrong,
3. Your errors are too small, or
4. You are unlucky.
If your χ2 is suspiciously small there are 2 possible reasons:
1. Your errors are too big, or
2. You are lucky.
7.2
Wilks’ theorem
The Likelihood on its own tells you nothing. Even if you include all the constant factors normally omitted
in maximisation. This may seem counter-intuitive, but it is inescapably true.
There is a theorem due to Wilks which is frequently invoked and appears to link likelihood and χ2,
but it does so only in very speciﬁc circumstances. Given two nested models, for large N the improvement
in ln L is distributed like χ2 in −2∆ln L, with NDF the number of extra parameters.
So suppose you have some data with many (x, y) values and two models, Model 1 being linear and
Model 2 quadratic. You maximise the likelihood using Model 1 and then using Model 2: the Likelihood
increases as more parameters are available (NDF = 1). If this increase is signiﬁcantly more than N
that justiﬁes using Model 2 rather than Model 1. So it may tell you whether or not the extra term in
a quadratic gives a meaningful improvement, but not whether the ﬁnal quadratic (or linear) model is a
good one.
Even this has an important exception. it does not apply if Model 2 contains a parameter which is
meaningless under Model 1. This is a surprisingly common occurrence. Model 1 may be background,
Model 2 background plus a Breit-Wigner with adjustable mass, width and normalization (NDF = 3).
The mass and the width are meaningless under Model 1 so Wilks’ theorem does not apply and the
improvement in likelihood cannot be translated into a χ2 for testing.
185


## Page 38


7.3
Toy Monte Carlos and likelihood for goodness of ﬁt
Although the likelihood contains no information about the goodness of ﬁt of the model, an obvious way
to get such information is to run many simulations of the model, plot the spread of ﬁtted likelihoods and
use it to get the p−value.
This may be obvious, but it is wrong [18]. Consider a test case observing decay times where the
model is a simple exponential P(t) = 1
τ e−t/τ, with τ an adjustable parameter. Then you get the Log
Likelihood P(−ti/τ −ln τ) = −N(t/τ + ln τ) and maximum likelihood gives ˆt = t =
1
N
P
i ti, so
ln L(ˆt; x) = −N(1 + ln t) . This holds whatever the original sample {ti} looks like: any distribution
with the same t has the same likelihood, after ﬁtting.
8
Upper limits
Many analyses are ‘searches for...’ and most of these are unsuccessful. But you have to say something!
Not just ‘We looked, but we didn’t see anything’. This is done using the construction of frequentist
conﬁdence intervals and/or Bayesian credible intervals.
8.1
Frequentist conﬁdence
Going back to the discussion of the basics, for frequentists the probability that it will rain tomorrow is
meaningless: there is only one tomorrow, it will either rain or it will not, there is no ensemble. The
probability Nrain/Ntomorrows is either 0 or 1. To talk about Prain is "unscientiﬁc" [10].
This is unhelpful. But there is a workaround.
Suppose some forecast says it will rain and studies show this forecast is correct 90% of the time.
We now have an ensemble of statements, and can say: ‘The statement ‘It will rain tomorrow’ has a 90%
probability of being true’. We shorten this to ‘It will rain tomorrow, with 90% conﬁdence’. We state X
with conﬁdence P if X is a member of an ensemble of statements of which at least P are true.
Note the ‘at least’ which has crept into the deﬁnition. There are two reasons for it:
1. Higher conﬁdences embrace lower ones. If X at 95% then X at 90%, and
2. We can cater for composite hypotheses which are not completely deﬁned.
The familiar quoted error is in fact a conﬁdence statement. Consider as an illustration the Higgs
mass measurement (current at the time of writing) MH = 125.09 ± 0.24 GeV. This does not mean that
the probability of the Higgs mass being in the range 124.85 < MH < 125.33 GeV is 68%: the Higgs
mass is a single, unique, number which either lies in this interval or it does not. What we are saying is
that MH has been measured to be 125.09 GeV with a technique that will give a value within 0.24 GeV
of the true value 68% of the time. We say: 124.85 < MH < 125.33 GeV with 68% conﬁdence. The
statement is either true or false (time will tell), but it belongs to a collection of statements of which (at
least) 68% are true.
So we construct conﬁdence regions also known as conﬁdence intervals [x−, x+] such that
R x+
x−P(x) dx = CL. We have not only a choice of the probability content (68%, 90%, 95%, 99%...)
to work with but also of strategy. Common options are:
1. Symmetric: ˆx −x−= x+ −ˆx ,
2. Shortest: Interval that minimises x+ −x−,
3. Central:
R x−
−∞P(x) dx =
R ∞
x+ P(x) dx = 1
2(1 −CL) ,
4. Upper Limit: x−= −∞,
R ∞
x+ P(x) , dx = 1 −CL , and
5. Lower Limit: x+ = ∞,
R x−
−∞P(x) , dx = 1 −CL .
186


## Page 39


For the Gaussian (or any symmetric PDF) 1-3 are the same.
We are particularly concerned with the upper limit: we observe some small value x. We ﬁnd a
value x+ such that for values of x+ or more the probability of getting a result as small as x, or even less,
is 1 −CL, or even less.
8.2
Conﬁdence belts
We have shown that a simple Gaussian measurement is basically a statement about conﬁdence regions.
x = 100 ± 10 implies that [90,110] is the 68% central conﬁdence region.
We want to extend this to less simple scenarios. As a ﬁrst step, we consider a proportional Gaus-
sian. Suppose we measure x = 100 from Gaussian measurement with σ = 0.1x (a 10% measurement—
which is realistic). If the true value is 90 the error is σ = 9 so x = 100 is more than one standard
deviation, whereas if the true value is 110 then σ = 11 and it is less than one standard deviation. 90 and
110 are not equidistant from 100.
This is done with a technique called a conﬁdence belt. The key point is that they are are constructed
horizontally and read vertically, using the following procedure (as shown in Fig. 25). Suppose that a is
the parameter of interest and x is the measurement.
Fig. 25: A conﬁdence belt for a proportional Gaussian
1. For each a, construct desired conﬁdence interval (here 68% central).
2. The result (x, a) lies inside the belt (the red lines), with 68% conﬁdence.
3. Measure x.
4. The result (x, a) lies inside the belt, with 68% conﬁdence. And now we know x.
5. Read off the belt limits a+ and a−at that x: in this case they are 111.1, 90.9. So we can report
that a lies in [90.9,111.1] with 68% conﬁdence.
6. Other choices for the conﬁdence level value and for the strategy are available.
This can be extended to the case of a Poisson distribution, Fig. 26.
The only difference is that the horizontal axis is discrete as the number observed, x, is integer. In
constructing the belt (horizontally) there will not in general be x values available to give Px+
x−= CL
187


## Page 40


Fig. 26: A conﬁdence belt for a Poisson
and we call, again, on the ‘at least’ in the deﬁnition and allow it to be Px+
x−≥CL.
Thus for a central 90% conﬁdence we require for each a the largest integer xlo and smallest xhi for
which Pxlo−1
x=0
e−a ax
x! ≤0.05 and P∞
x=xhi+1 e−a ax
x! ≤0.05. For the second sum it is easier to calculate
Pxhi
x=0 e−a ax
x! ≥0.95 .
Whatever the value of a, the probability of the result falling in the belt is 90% or more. We proceed
as for the Gaussian.
8.3
Coverage
This is an appropriate point to introduce coverage: the probability, given a, that the statement ‘alo ≤a ≤
ahi’ will be true. Ideally this would be the same as the conﬁdence level, however it may (because of the
‘at least’ clauses) exceed it (‘overcover’); this is allowed though in principle inefﬁcient. It should never
be less (‘undercover’).
For example: suppose we have a Poisson process with a = 3.5 and we want a 90% central limit.
There is a probability e−3.5 = 3% of getting zero events, leading to a+ = 3.0, which would be
wrong as 3.0 < 3.5 .
Continuing in sequence, there is a probability 3.5e−3.5 =11% of getting one event, leading to
a+ = 4.7, which would be right.
Right answers continue up to seven events (with probability 3.57e−3.5/7! =4% ): this gives a
safely large value for a+ and a−= 3.3, which is right as 3.3 < 3.5, though only just, The next outcome,
eight events (probability 2%) gives a−= 4.0 which is wrong, as are all subsequent results.
Adding up the probabilities for the outcomes 1 thru 7 that give a true answer totals 94%, so there
is 4% overcoverage.
Note that coverage is a function of the true value of the parameter on which limits are being placed.
Values of a other than 3.5 will give different coverage numbers—though all are over 90%.
188


## Page 41


8.4
Upper limits
The one-sided upper limit—option 4 in the list above—gives us a way of quantifying the outcome of a
null experiment. ‘We saw nothing (or nothing that might not have been background), so we say a ≤a+
at some conﬁdence level’.
One simple and enlightening example occurs if you see no events, and there is no expected back-
ground. Now P(0; 2.996) = 0.05 and 2.996 ∼3. So if you see zero events, you can say with 95%
conﬁdence that the true value is less than 3.0. You can then directly use this to calculate a limit on the
branching fraction, cross section, or whatever you’re measuring.
8.5
Bayesian ‘credible intervals’
A Bayesian has no problems saying ‘It will probably rain tomorrow’ or ‘The probability that 124.85 <
MH < 125.33 GeV is 68%’. The downside, of course, is that another Bayesian can say ‘It will probably
not rain tomorrow’ and ‘The probability that 124.85 < MH < 125.33 GeV is 86%’ with equal validity
and the two cannot resolve their subjective difference in any objective way.
A Bayesian has a prior belief PDF P(a) and deﬁnes a region R such that
R
R P(a) da = CL. There
is the same ambiguity regarding choice of content (68%, 90%, 95%...) and strategy (central, symmetric,
upper limit...). So Bayesian credible intervals look a lot like frequentist conﬁdence intervals even if their
meaning is different.
There are two happy coincidences.
The ﬁrst is that Bayesian credible intervals on Gaussians, with a ﬂat prior, are the same as Fre-
quentist conﬁdence intervals. If F quotes 68% or 95% or . . . conﬁdence intervals and B quotes 68% or
95% or . . . credible interval, their results will agree.
The second is that although the Frequentist Poisson upper limit is given by Pr=rdata
r=0
e−ahiar
hi/r!
whereas the Bayesian Poisson ﬂat prior upper limit is given by
R ahi
0
e−aardata/rdata! da, integration by
parts of the Bayesian formula gives a series which is same as the Frequentist limit. A Bayesian will also
say : ‘I see zero events—the probability is 95% that the true value is 3.0 or less.’ This is (I think) a
coincidence—it does not apply for lower limits. But it does avoid heated discussions as to which value
to publish.
8.6
Limits in the presence of background
This is where it gets tricky. Typically an experiment may observe ND events, with an expected back-
ground NB and efﬁciency η, and wants to present results for NS = ND−NB
η
. Uncertainties in η and NB
are handled by proﬁling or marginalising. The problem is that the actual number of background events
is not NB but Poisson in NB.
So in a straightforward case, if you observe twelve events, with expected background 3.4 and
η = 1 it is obviously sensible to say NS = 8.6 (though the error is
√
12 not
√
8.6)
But suppose, with the same background, you see four events, three events or zero events. Can you
say NS = 0.6? or −0.4? Or −3.4???
We will look at four methods of handling this, considering as an example the observation of three
events with expected background 3.40 and wanting to present the 95% CL upper limit on NS.
8.6.1
Method 1: Pure frequentist
ND −NB is an unbiased estimator of NS and its properties are known. Quote the result. Even if it is
non-physical.
The argument for doing so is that this is needed for balance: if there is really no signal, approxi-
mately half of the experiments will give positive values and half negative. If the negative results are not
189


## Page 42


published, but the positive ones are, the world average will be spuriously high. For a 95% conﬁdence
limit one accepts that 5% of the results can be wrong. This (unlikely) case is clearly one of them. So
what?
A counter-argument is that if ND < NB, we know that the background has ﬂuctuated downwards.
But this cannot be incorporated into the formalism.
Anyway, the upper limit from 3 is 7.75, as P3
0 e−7.757.75r/r! = 0.05, and the 95% upper limit on
NS = 7.75 −3.40 = 4.35 .
8.6.2
Method 2: Go Bayesian
Assign a uniform prior to NS, for NS > 0, zero for NS < 0. The posterior is then just the like-
lihood, P(NS|ND, NB) = e−(NS+NB) (NS+NB)ND
ND!
. The required limit is obtained from integrating
R Nhi
0
P(NS) dNS = 0.95 where P(NS) ∝e−(Ns+3.40) (Ns+3.4)3
3!
; this is illustrated in Fig. 27 and the
value of the limit is 5.21.
0
2
4
6
8
10
0.000
0.001
0.002
0.003
0.004
Ns
P
Fig. 27: The Bayesian limit construction
8.6.3
Method 3: Feldman-Cousins
This—called ‘the uniﬁed approach’ by Feldman and Cousins [19]—takes a step backwards and considers
the ambiguity in the use of conﬁdence belts.
In principle, if you decide to work at, say, 90% conﬁdence you may choose to use a 90% central
or a 90% upper limit, and in either case the probability of the result lying in the band is at least 90%.
This is shown in Fig. 28.
In practice, if you happen to get a low result you would quote an upper limit, but if you get a high
result you would quote a central limit. This, which they call ‘ﬂip-ﬂopping’, is illustrated in the plot by a
break shown here for r = 10.
Now the conﬁdence belt is the green one for r < 10 and the red one for r ≥10. The probability
of lying in the band is no longer 90%! Flip-ﬂopping invalidates the Frequentist construction, leading to
undercoverage.
190


## Page 43


Fig. 28: The ﬂip-ﬂopping problem
They show how to avoid this. You draw the plot slightly differently: r ≡ND is still the horizontal
variable, but as the vertical variable you use NS. (This means a different plot for any different NB,
whereas the previous Poisson plot is universal, but this is not a problem.) This is to be ﬁlled using
P(r; Ns) = e−(Ns+NB) (NS+NB)r
r!
.
For each NS you deﬁne a region R such that P
rϵR P(r; Ns) ≥90%. You have a choice of strategy
that goes beyond ‘central’ or ‘upper limit’: one plausible suggestion would be to rank r by probability
and take them in order until the desired total probability content is achieved (which would, incidentally,
give the shortest interval). However this has the drawback that outcomes with r < NB will have small
probabilities and be excluded for all NS, so that, if such a result does occur, one cannot say anything
constructive, just ‘This was unlikely’.
An improved form of this suggestion is that for each NS, considering each r you compare
P(r; NS) with the largest possible value obtained by varying NS. This is easier than it sounds be-
cause this highest value is either at NS = r −NB (if r ≥NB) or NS = 0 (if r ≤NB ). Rank on the
ratio P(r; NS)/P(r; Nbest
S
) and again take them in order till their sum gives the desired probability.
This gives a band as shown in Fig. 29, which has NB = 3.4. You can see that ‘ﬂip-ﬂopping’ occurs
naturally: for small values of r one just has an upper limit, whereas for larger values, above r = 7, one
obtains a lower limit as well. Yet there is a single band, and the coverage is correct (i.e. it does not
undercover). In the case we are considering, r = 3, just an upper limit is given, at 4.86.
Like other good ideas, this has not found universal favour. Two arguments are raised against the
method.
First, that it deprives the physicist of the choice of whether to publish an upper limit or a range. It
could be embarrassing if you look for something weird and are ‘forced’ to publish a non-zero result. But
this is actually the point, and in such cases one can always explain that the limits should not be taken as
implying that the quantity actually is nonzero.
Secondly, if two experiments with different NB get the same small ND, the one with the higher
NB will quote a smaller limit on NS. The worse experiment gets the better result, which is clearly
unfair! But this is not comparing like with like: for a ‘bad’ experiment with large background to get a
small number of events is much less likely than it is for a ‘good’ low background experiment.
191


## Page 44


Fig. 29: A Feldman-Cousins conﬁdence band
8.6.4
Method 4: CLs
This is a modiﬁcation of the standard frequentist approach to include the fact, as mentioned above, that
a small observed signal implies a downward ﬂuctuation in background [20]. Although presented here
using just numbers of events, the method is usually extended to use the full likelihood of the result, as
will be discussed in Section 8.6.6.
Fig. 30: The CLs construction
Denote the (strict frequentist) probability of getting a result this small (or less) from s + b events
as CLs+b, and the equivalent probability from pure background as CLb (so CLb = CLs+b for s = 0).
Then introduce
192


## Page 45


CLs = CLs+b
CLb
.
(39)
Looking at Fig. 30, the CLs+b curve shows that if s + b is small then the probability of getting
three events or less is high, near 100%. As s + b increases this probability falls, and at s + b = 7.75 the
probability of only getting three events or less is only 5%. This, after subtraction of b = 3.4, gives the
strict frequentist value.
The point s + b = 3.4 corresponds to s = 0, at which the probability CLb is 56% As s must
be non-negative, one can argue that everything to the left of that is unmeaningful. So one attempts to
incorporate this by renormalizing the (blue) CLs+b curve to have a maximum of 100% in the physically
sensible region, dividing it by 0.56 to get the (green) CLs curve. This is treated in the same way as the
CLs+b curve, reading off the point at s + b = 8.61 where it falls to 5%. This is a limit on s + b so
we subtract 3.4 to get the limit on s as 5.21. This is larger than the strict frequentist limit: the method
over-covers (which, as we have seen, is allowed if not encouraged) and is, in this respect ‘conservative’6.
This is the same value as the Bayesian Method 2, as it makes the same assumptions.
CLs is not frequentist, just ‘frequentist inspired’. In terms of statistics there is perhaps little in its
favour. But it has an intuitive appeal, and is widely used.
8.6.5
Summary so far
Given three observed events, and an expected background of 3.4 events, what is the 95% upper limit on
the ‘true’ number of events? Possible answers are shown in table 2.
Strict Frequentist
4.35
Bayesian (uniform prior)
5.21
Feldman-Cousins
4.86
CLs
5.21
Table 2: Upper limits from different methods
Which is ‘right’? Take your pick! All are correct. (Well, not wrong.). The golden rule is to say
what you are doing, and if possible give the raw numbers.
8.6.6
Extension: not just counting numbers
These examples have used simple counting experiments. But a simple number does not (usually) exploit
the full information.
Consider the illustration in Fig. 31. One is searching for (or putting an upper limit on) some
broad resonance around 7 GeV. One could count the number of events inside some window (perhaps 6
to 8 GeV?) and subtract the estimated background. This might work with high statistics, as in the left,
but would be pretty useless with small numbers, as in the right. It is clearly not optimal just to count an
event as ‘in’, whether it is at 7.0 or 7.9, and to treat an event as ‘out’, if it is at 8.1 or 10.1.
It is better to calculate the Likelihood ln Ls+b = P
i ln NsS(xi) + NbB(xi)
;
ln Lb =
P
i ln NbB(xi). Then, for example using CLs, you can work with Ls+b/Lb, or −2 ln (Ls+b/Lb). The
conﬁdence/probability quantities can be found from simulations, or sometimes from data.
6‘Conservative’ is a misleading word. It is used by people describing their analyses to imply safety and caution, whereas it
usually entails cowardice and sloppy thinking.
193


## Page 46


Fig. 31: Just counting numbers may not give the full information
Fig. 32: Signiﬁcance plot for the Higgs search
8.6.7
Extension: From numbers to masses
Limits on numbers of events can readily be translated into limits on branching ratios, BR =
Ns
Ntotal , or
limits on cross sections, σ =
Ns
R
Ldt .
These may translate to limits on other, theory, parameters.
In the Higgs search (to take an example) the cross section depends on the mass, MH—and so
does the detection efﬁciency—which may require changing strategy (hence different backgrounds). This
leads to the need to basically repeat the analysis for all (of many) MH values. This can be presented in
two ways.
The ﬁrst is shown in Fig. 32, taken from Ref. [21]. For each MH (or whatever is being studied) you
search for a signal and plot the CLs (or whatever limit method you prefer) signiﬁcance in a Signiﬁcance
Plot. Small values indicate that it is unlikely to get a signal this large just from background.
One often also plots the expected (from MC) signiﬁcance, assuming the signal hypothesis is true.
This is a measure of a ‘good experiment’. In this case there is a discovery level drop at MH ≈125 GeV,
which exceeds the expected signiﬁcance, though not by much: ATLAS were lucky but not incredibly
194


## Page 47


lucky.
The second method is—for some reason—known as the green-and-yellow plot. This is basically
the same data, but ﬁxing CL at a chosen value: in Fig. 33 it is 95%. You ﬁnd the limit on signal strength,
at this conﬁdence level, and interpret it as a limit on the cross section σ/σSM. Again, as well as plotting
the actual data one also plots the expected (from MC) limit, with variations. If there is no signal, 68% of
experiments should give results in the green band, 95% in the yellow band.
Fig. 33: Green and yellow plot showing the Higgs discovery
So this ﬁgure shows the experimental result as a black line. Around 125 GeV the 95% upper limit
is more than the Standard Model prediction indicating a discovery. There are peaks between 200 and
300 GeV, but they do not approach the SM value, indicating that they are just ﬂuctuations. The value
rises at 600 GeV, but the green (and yellow) bands rise also, showing that the experiment is not sensitive
for such high masses: basically it sees nothing but would expect to see nothing.
9
Making a discovery
We now turn from setting limits, to say what you did not see, to the more exciting prospect of making a
discovery.
Remembering hypothesis testing, in claiming a discovery you have to show that your data can’t be
explained without it. This is quantiﬁed by the p−value: the probability of getting a result this extreme (or
worse) under the null hypothesis/Standard Model. (This is not ‘The probability that the Standard Model
is correct’, but it seems impossible for journalists to understand the difference.)
Some journals (particularly in psychology) refuse to publish papers giving p−values. If you do
lots of studies, some will have low p−values (5% below 0.05 etc.). The danger is that these get published,
but the unsuccessful ones are binned.
Is p like the signiﬁcance α? Yes and no. The formula is the same, but α is a property of the test,
computed before you see the data. p is a property of the data.
9.1
Sigma language
The probability (p−value) is often translated into Gaussian-like language: the probability of a result
more than 3σ from the mean is 0.27% so a p−value of 0.0027 is a ‘3 σ effect’ (or 0.0013 depending on
whether one takes the 1-tailed or 2-tailed option. Both are used.) In reporting a result with a signiﬁcance
of ‘so many σ’ there is no actual σ involved: it is just a translation to give a better feel for the size of the
probability.
195


## Page 48


By convention, 3 sigma, p = 0.0013 is reported as ‘Evidence for’ whereas a full 5 sigma
p = 0.0000003 is required for ‘discovery of’.
9.2
The look-elsewhere effect
You may think that the requirement for 5 σ is excessively cautious. Its justiﬁcation comes from history—
too many 3- and 4- sigma ‘signals’ have gone away when more data was taken.
This is partly explained by the ‘look-elsewhere effect’. How many peaks can you see in the data
in Fig. 34?
Fig. 34: How many peaks are in this data?
The answer is that there are none. The data is in fact purely random and ﬂat. But the human eye is
very good at seeing features.
With 100 bins, a p−value below 1% is pretty likely. This can be factored in, to some extent,
using pseudo-experiments, but this does not allow for the sheer number of plots being produced by
hard-working physicists looking for something. Hence the need for caution.
This is not just ancient history. ATLAS and CMS recently observed a signal in the γγ mass around
750 GeV, with a signiﬁcance of 3.9σ (ATLAS) and 3.4σ (CMS), which went away when more data was
taken.
9.3
Blind analysis
It is said7 that when Michaelangelo was asked how he created his masterpiece sculpture ‘David’ he
replied ‘It was easy—all I did was get a block of marble and chip away everything that didn’t look like
David’. Such creativity may be good for sculpture, but it’s bad for physics. If you take your data and
devise cuts to remove all the events that don’t look like the signal you want to see, then whatever is left
at the end will look like that signal.
Many/most analyses are now done ‘blind’. Cuts are devised using Monte Carlo and/or non-signal
data. You only ‘open the box’ once the cuts are ﬁxed. Most collaborations have a formal procedure for
doing this.
This may seem a tedious imposition, but we have learnt the hard way that it avoids embarrassing
mistakes.
7This story is certainly not historically accurate, but it’s still a good story (quoteinvestigator.com:
https://
quoteinvestigator.com/2014/06/22/chip-away/).
196


## Page 49


10
Conclusions
Statistics is a tool for doing physics. Good physicists understand their tools. Don’t just follow without
understanding, but read books and conference proceedings, go to seminars, talk to people, experiment
with the data, and understand what you are doing. Then you will succeed. And you will have a great
time!
References
[1] R. J. Barlow, Statistics: A Guide to the Use of Statistical Methods in the Physical Sciences, (Wiley,
Chichester, 1989).
[2] G. Cowan, Statistical Data Analysis, (Oxford Univ. Press, Oxford,1998).
[3] I. Narsky and F. C. Porter, Statistical Analysis Techniques in Particle Physics, (Wiley, Weinheim,
2014), doi:10.1002/9783527677320.
[4] O. Behnke et al (Eds.) Data Analysis in High Energy Physics, (Wiley, Weinheim, 2013),
doi:10.1002/9783527653416.
[5] L. Lyons, Statistics for Nuclear and Particle Physicists, Cambridge Univ. Press, Cambridge,
1986).
[6] G. Bohm and G. Zech, Introduction to Statistics and Data Analysis for Physicists, 3rd revised ed.
(Verlag Deutsches Elektronen-Synchrotron, Hamburg, 2017), doi:10.3204/PUBDB-2017-08987.
[7] M. R. Whalley and L. Lyons (Eds) Advanced Statistical Techniques in Particle Physics, Durham
report IPPP/02/39, 2002, https://inspirehep.net/literature/601052.
[8] L. Lyons, R. Mount and R. Reitmayer (Eds.) Proceedings of PHYSTAT03, SLAC-R-703, 2003,
https://www.slac.stanford.edu/econf/C030908/.
[9] L. Lyons and M. K. Unel (Eds.) Proceedings of PHYSTAT05, (Imperial College Press, London,
2006), doi:10.1142/p446.
[10] R. von Mises, Probability, Statistics and Truth, reprint of the second revised 1957 English edition
(Dover, Mineola, NY, 1981).
[11] H. Jeffreys, Theory of Probability, 3rd ed. (Oxford Univ. Press, Oxford, 1961).
[12] R. J. Barlow, A note on ∆ln L = −1
2 Errors, arXiv:physics/0403046, 2004.
[13] R. J. Barlow, Asymmetric Statistical Errors, Proceedings of PHYSTAT05, Eds. L. Lyons and
M. K. Unel (Imperial College Press, London, 2006), p.56, doi:10.1142/9781860948985_0013,
arXiv:physics/0406120, 2004.
[14] CMS Collaboration, CMS 2D Cf-Cv Likelihood Proﬁle,
https://root.cern.ch/cms-2d-cf-cv-likelihood-profile, accessed 26 May 2019.
[15] P. R. Bevington, Data Reduction and Error Analysis for the Physical Sciences, 3rd ed.
(McGraw Hill, New York, NY, 2003).
[16] J. Orear, Notes on Statistics for Physicists, UCRL-8417, 1958,
http://nedwww.ipac.caltech.edu/level5/Sept01/Orear/frames.html
[17] B. Aubert et al. [BaBar Collaboration], Phys. Rev. Lett. 86 (2001) 2515,
doi:10.1103/PhysRevLett.86.2515, arXiv:hep-ex/0102030.
[18] J. G. Heinrich, CDF internal note CDF/MEMO/BOTTOM.CDFR/5639 (Many thanks to Jonas
Rademacker for pointing this out); L. Lyons, R. Mount and R. Reitmayer (Eds.) Proceedings of
PHYSTAT03, SLAC-R-703, 2003, p.52, https://www.slac.stanford.edu/econf/C030908/.
[19] G. J. Feldman and R. D. Cousins, Phys. Rev. D57 (1998) 3873, doi:10.1103/PhysRevD.57.3873,
arXiv:physics/9711021.
[20] A. L. Read, J. Phys. G28 (2002), 2693, doi:10.1088/0954-3899/28/10/313.
[21] ATLAS Collaboration, ATLAS Higgs Search Update,
https://atlas.cern/updates/atlas-news/atlas-higgs-search-update, accessed
26 May 2019.
197

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]