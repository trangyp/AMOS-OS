---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1805.02941v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1805.02941v1_Error_Rates_for_Unvalidated_Medical_Age_Assessment_Procedures

> Source: 1805.02941v1_Error_Rates_for_Unvalidated_Medical_Age_Assessment_Procedures.pdf

> Pages: 23

---


## Page 1


Error Rates for Unvalidated Medical Age
Assessment Procedures
Petter Mostad∗
Fredrik Tamsen†
May 9, 2018
Abstract
During 2014-15 Sweden received asylum applications from more than
240.000 people, of which more than 40.000 were termed unaccompanied
minors.
In a large number of cases, claims by asylum seekers of be-
ing below 18 years were not trusted by Swedish authorities. To handle
the situation, the Swedish national board of forensic medicine (R¨atts-
medicinalverket, RMV) was assigned by the government to create a cen-
tralized system for medical age assessments. RMV introduced a proce-
dure including two biological age indicators; x-ray of the third molars and
magnetic resonance imaging of the distal femoral epiphysis.
In 2017 a
total of 9617 males and 337 females were subjected to this procedure. No
validation study for the procedure was however published, and the ob-
served number of cases with diﬀerent maturity combinations in teeth and
femur were unexpected given the claims originally made by RMV. Such
unexpected results might be caused by systematic errors and need to be
analyzed thoroughly.
In the present paper we present a general stochastic model enabling
us to study which combinations of age indicator model parameters and
age population proﬁles are consistent with the observed 2017 data for
males.
We ﬁnd that, contrary to some RMV claims, maturity of the
femur, as observed by RMV, appears on average well before maturity
of teeth. Although results naturally contain much uncertainty, we ﬁnd
that classiﬁcation error rates for certain groups who based on the RMV
procedure are classiﬁed as above 18 years may be around 10-30%, possibly
as high as 50%.
1
Introduction
In medical age assessments certain biological processes that develop during child-
hood in a predictable sequence are used to assess a person’s chronological age.
∗Mathematical Sciences, Chalmers University of Technology and Gothenburg University,
Sweden (mostad@chalmers.se)
†Forensic Medicine, Department of Surgical Sciences, Uppsala University, Sweden
1
arXiv:1805.02941v1  [stat.AP]  8 May 2018


## Page 2


Examples of such processes are the development of teeth, bones, and sexual ma-
turity. We will use in this paper the term ”age indicator” to mean any observed
biological feature that develops through a series of clearly deﬁned states over
an age period relevant for age assessment.
Medical age assessments have been used for a long time in many countries,
but are always associated with debate. This debate can be divided into two
main lines. One concerns the very use of medical age assessment. Critics argue
that since biological processes always show such a wide variation in populations,
biological states can never be used to make suﬃciently certain assessments of
chronological age.
Others might argue that it is the biological and not the
chronological age that is the most relevant for the needs of an individual.
In most countries the age is important for the rule of law. Many countries
view the age of 18 as being the border between childhood and adulthood. Chil-
dren have other needs and rights than do adults, and punishments for crimes
might diﬀer whether the perpetrator is below or above 18. In the case of asylum
seekers, children are to be treated diﬀerently according to international conven-
tions. One might therefore argue that if a person’s age is unknown, a medical
age assessment may be necessary in order to protect the privileges of children.
The other line of debate concerns which methods are appropriate to use. A
compilation of methods used in the European Union shows that most countries
use two or more age indicators EASO [2018].
There are variations between
countries, but the two most commonly used methods are dental x-ray and x-ray
imaging of the hand/wrist. Another commonly used indicator is x-ray imaging
of the collar bone. These three age indicators are all included in the recommen-
dations by The Study Group on Forensic Age Diagnostics (Arbeitsgemeinschaft
f¨ur Forensische Altersdiagnostik; AGFAD), an international assembly of ex-
perts that has worked on this issue for the last 18 years Schmeling et al. [2008],
Schmeling et al. [2016].
During the last few years, many asylum seekers in Sweden have claimed to
be under 18 but have not been able to convince authorities about their claim.
To be able to treat children as children, and to not give child privileges to
adults, the government of Sweden has decided to oﬀer the possibility to make a
medical age assessment in these cases. When a wave of asylum seekers arrived
in 2014-15, there was no generally accepted system for medical ages assessments
in Sweden, and R¨attsmedicinalverket (RMV) was assigned by the government
to create one.
The method1 chosen by RMV uses two age indicators: Magnetic resonance
imaging of the distal femur (MRI knee), and x-ray imaging of the third molars
in the mandible (x-ray teeth) R¨attsmedicinalverket [2017]. The MRI knee and
x-ray teeth are independently evaluated by two radiologists and two dentists,
respectively.
For the knee to be assessed as mature, both radiologists must
agree on this assessment. If they disagree, the knee is assessed as immature.
The same procedure is used for teeth. These assessments are then combined
in such a way that if either the knee or the teeth are mature, the individual
1https://www.rmv.se/verksamheter/medicinska-aldersbedomningar/metoder/
2


## Page 3


Knees mature
Knees immature
No data knees
SUM
Teeth mature
4176
348
187
4711
Teeth immature
1735
1087
83
2905
No data teeth
1364
237
63
1664
SUM
7275
1672
333
9280
Table 1: Results for the 9280 males submitted to the RMV procedure during
2017.
is assessed as being 18 years or older2. During 2017 a total of 9617 males and
337 females were subjected to this age assessment procedure. The results for
males are given in Table 1. In 2018 RMV changed their assessments for females,
since a new study showed that the majority of females aged 16 and 17 years
had mature knees, see Ottow et al. [2017], Tamsen [2017]. Females now need
mature teeth to be assessed as being 18 years or older. In this paper, we will
only study the RMV data for males.
The maturity of the teeth is assessed according to the stages of Demirjian, in
which a tooth can be in one of eight stages A-H, see Demirjian et al. [1973]. H is
the ﬁnal stage and the teeth are termed ’mature’ if at least one of the mandibular
third molars are assessed as being in this stage. The knee is assessed as ’mature’
if it has reached stage 4 or 5 according to the classiﬁcation by Schmeling Kr¨amer
et al. [2014]. The diﬀerent stages of immature teeth and knees are not used in
the age assessments made by RMV. So, if the knee is mature, it doesn’t matter
if the most developed examined tooth is in stage G (one stage from mature) or
stage F (two stages from mature), the age assessment is still the same.
To date there exist six original articles and one letter to the editor on age
assessment with MRI knee: Dedouit et al. [2012], Kr¨amer et al. [2014], Saint-
Martin et al. [2015], Ekizoglu et al. [2016], Fan et al. [2016], Ottow et al. [2017],
Vieth et al. [2018]. Since there are diﬀerences in MRI techniques and grading
systems for maturity assessment, all studies cannot be compared with each
other. Three of the original studies use MRI techniques and grading systems
that are more or less comparable to the method used by RMV Kr¨amer et al.
[2014], Fan et al. [2016], Ottow et al. [2017].
However, the relatively small
number of participants in relevant ages and shifting results make it hard to
regard this method as validated. More and larger studies are needed.
Another aspect of validity is the application of the methods. Validation of
assessments is an obvious practice in the ﬁeld of medicine. Normally, an appren-
tice makes assessments under the supervision of an experienced assessor. When
the rate of correct assessments is suﬃciently high, the apprentice is allowed to
make them on his or her own. At least for the maturity assessments of MRI
2The exact wording of the conclusions produced by RMV have several forms. However, as
these conclusions are then mapped by the Swedish migratory authority to decisions about age,
the exact wording is of little consequence. We will in this paper simply refer to assessment of
above or below 18 years.
3


## Page 4


knee, RMV has not presented any external validation prior to the large amount
of assessments they now have performed.
In 137 cases where RMV assessed the knee as mature, an external second
opinion has been performed by German scientists3.
These scientists are the
ones who have developed and continued to study an MRI knee method close
to the one RMV uses. In 75 of these 137 cases (55%), the German scientists
came to the opposite conclusion that the knee was not mature.
The cases
that has undergone second opinions are the result of private initiatives and
they are thus not randomly selected.
Therefore one cannot generalize these
results to all people who have had their knees assessed as mature. However, one
cannot exclude general discrepancies and since RMV uses these German studies
as the most important foundation for their method, the results are alarming
and require a thorough analysis of the validity of the Swedish assessments.
When faced with this criticism RMV performed an analysis of reliability, but
no analysis of validity has yet been performed.
We are thus facing a situation where there is substantial uncertainty about
the true relationship between chronological age and the age indicators used by
RMV. There is of course also a large uncertainty about the true age distribution
of the population on which the procedure has been performed. The only ﬁrm
evidence is the information presented in Table 1. In this paper, we show how
simulation within a Bayesian framework may be used to obtain information
about the possible combinations of population proﬁles and age indicator models
that may explain this data. We also show how one may obtain some information
about likely classiﬁcation error rates in such a situation.
A simple statistical approach to medical age assessment is the following: An
age indicator that can take on discrete values I1, . . . , In is measured on a study
population with known chronological ages. The study population is subdivided
according to the age indicator, and the chronological ages within each subgroup
are modelled with some statistical model, possibly just a normal distribution.
Then, this statistical model is used to assess the chronological age of persons
whose observed age indicator corresponds to the group.
The main drawback of this simple and common approach is that it assumes
that, a priori, the distribution of the ages of the assessed persons corresponds
to the distribution of ages in the study population. This is clearly not the case
in most applications of age assessments, as the assessment is generally triggered
by circumstances related to age. For example, an immigration authority may
decide to require medical age assessment of all asylum seekers, of asylum seek-
ers they believe might be re-classiﬁed by the assessment, or of asylum seekers
whose age they are fully convinced are above the relevant age limit of 18 years.
Clearly diﬀerent decisions will lead to diﬀerent rates of erroneous classiﬁcation,
something that cannot be captured by the simple statistical procedure above.
In this paper, we instead use the following procedure: For each age indicator,
we use studies where the indicator has been observed in study populations with
known chronological ages to establish a statistical model predicting the value
3https://www.svd.se/rmv-andrar-aldersbedomning-efter-granskning
4


## Page 5


of the age indicator as a function of chronological age. When assessing the age
of a person with an observed age indicator, we combine an a priori distribution
for the persons age with the likelihood provided from the age indicator and the
statistical model to obtain the a posteriori distribution for the age of the person.
This Bayesian approach is discussed for example in Taroni et al. [2010] (relating
to forensics in general) and for example in Thevissen et al. [2010] (relating to
age assessments).
For each of the two age indicators appearing in this paper, we thus need
to establish a statistical model predicting the value of the age indicator from
chronological age. General models are discussed in Section 2.1. How to obtain
model parameters from publshed studies is discussed in Section 2.2. In this
paper, we assume that, given chronological age, the probability for observing
various values of one indicator is independent of the value observed for another
indicator. The relationship between maturation in the knee and the third mo-
lars has not been studied, but the study Gelbrich et al. [2015] on the wrist and
third molars found no correlation between these age indicators. Thus, an as-
sumption of conditional independence between the third molars and the knee is
not implausible.
For the approach above to work, one needs to establish an a priori distribu-
tion for the age of the person that is assessed. In case work, such a distribution
will be based on the circumstances of that person, and may vary from case to
case. In this paper, we consider data derived from age assessment of 9280 males,
and we use a common a priori distribution for these, based simply on the fact
that they have in a sense been required4 to submit themselves to the medical
age assessment procedure arranged by RMV in Sweden.
In initial computations, we use indicator model parameters derived directly
from published studies; for MRI knee we used Ottow et al. [2017] while for
x-ray teeth either Lucas et al. [2016] or Mincer et al. [1993]. Combining these
with a particular ﬁxed population proﬁle results in models that do not ﬁt the
observed data. Thus it is clear that we need to relax assumptions, either about
the indicator models, about the age distribution, or both.
In Section 2.2 we set up a series of reasonable possible priors for age indi-
cator models, taking the published age indicator studies as starting point. In
Section 2.3 we discuss population proﬁles, setting up a hierachical prior designed
to minimize the eﬀect on results of prior guesses about the proﬁle. In the re-
sults in Section 3 we combine the indicator model parameter priors with the
hierachical population prior and study the properties of the resulting models.
Any statistical investigation rests on a set of assumptions. In some contexts,
it may be easy to agree on reasonable assumptions, the exact nature of which
many then be discussed little or not at all. In our context, many reasonable
sets of assumptions are possible, with each set leading to somewhat diﬀerent re-
sults. We have confronted this challenge by presenting several possible models
in the main text, and also discussing a range of alternatives in the supplemen-
4The tests are not mandatory, and only those who have not been able to make their under-
age plausible are oﬀered the tests. However, if they then do not agree to take the tests, they
will most likely be assessed as adults.
5


## Page 6


tary material Mostad and Tamsen [2018] for this paper. Even if results vary
somewhat with diﬀerent models, there are some general conclusions we believe
can be drawn, and we present these in Section 3.2.
2
Methods
In Section 2.1 we present the stochastic model enabling us to do the computa-
tions speciﬁed above. In Section 2.2 we present the models we use for teeth and
knee age indicators while Section 2.3 contains a discussion on how we model
the age distribution. Finally, Section 2.4 contains some technical information
surrounding simulation with our model.
2.1
Stochastic model
We assume K diﬀerent age indicators are observed. We assume age indicator k
(k = 1, . . . , K) can take on nk diﬀerent discrete values, denoted Ik1, Ik2, . . . , Iknk.
For each age indicator k, we assume there is a model with parameters θk relating
the chronological age x of a person to the probabilities pkj(x | θk) of observing
indicator Ikj, so that we assume
ki
X
j=1
pkj(x | θk) = 1
for all x.
As an example, assume age indicator k has two diﬀerent values, Ik1 repre-
senting “immature” and Ik2 representing “mature”. In some cases, a reasonable
parametric model may be
pk2(x | θk) = Φ
x −θk1
θk2

(1)
where θk = (θk1, θk2) and Φ is the Probit function (i.e., the cumulative distri-
bution function for the standard normal distribution). We will consider models
where age indicator k can have a third possible value, Ik3, representing “not
assessible”. In fact, a model with a constant probability for such missing data
does not ﬁt the data considered in this paper. Thus, we use instead a linear
dependency of lack of data on age:
pk3(x | θk)
=
θk3 + θk4(x −20)
(2)
pk2(x | θk)
=
(1 −pk3(x | θk)) Φ
x −θk1
θk2

(3)
where now θk = (θk1, θk2, θk3, θk4).
For each age indicator k we use a probability density on the space of possible
parameters θk to model the uncertainty in the model. Speciﬁcally, consider the
6


## Page 7


model of Equations 2 and 3. As it is reasonable to think that, given age, lack
of data is independent of maturity of the indicator, we may write
π(θk) = π(θk1, θk2)π(θk3, θk4).
(4)
In our setting, the parameters θk3 and θk4 concerning lack of data will be well
informed by the data we are considering, so we will use ﬂat priors π(θk3, θk4) ∝1
for these. The priors π(θk1, θk2) will be based on information obtained from
various published studies and will be further discussed in Section 2.2. We now
deﬁne a joint prior
π(θ) = π(θ1)π(θ2) . . . π(θK)
where θ = (θ1, . . . , θK).
As mentioned above, we assume in this paper that, given chronological age
x, the probability for observing various values of one indicator is independent
of the value observed for another indicator. Thus, assuming a person has age
x, that a vector v = (z1, . . . , zK) of the K diﬀerent age indicators is observed
for this person, and given a value for θ, the probability of observing v can be
written as
p(v | x, θ) =
K
Y
k=1
pkzk(x | θk).
Aside from the parameters of the age indicator observation models used,
the major uncertainty in our situation lies in the distribution of chronological
ages in the population on which the observation procedure is applied. In this
paper, we will use a discretization, using the vector {x1, . . . , xT } to represent T
possible age values. A population proﬁle is then represented by a vector ψ =
(ψ1, . . . , ψT ), with ψi indicating the probability for age xi, so that P
i ψi = 1.
We will use a Dirichlet prior on ψ, with
(ψ1, . . . , ψT ) ∼Dirichlet(α/T, . . . , α/T).
for some parameter α. Under this prior, the expected value of each ψi is 1/T.
Starting with some distribution with cumulative density function F which can
be considered reasonable, we choose the xi so that F(xi) = i/T.
Thus the
uneven spread of the xi will reﬂect the population proﬁle speciﬁed by F. The
uncertainty around this target distribution is governed by the parameter α: We
get that
ψ1 + · · · + ψi ∼Beta
 i
T α, T −i
T
α

so that when α →∞we get increasingly little variation around the target
distribution, while α →0 gives increasing ﬂexibility.
To make computations, we include in the model a variable with information
about the actual ages of the persons subjected to the age assessment procedure.
Let v1, v2, . . . , vV be the possible values that an age indicator vector v can take
on, so that V = n1n2 · · · nK. Now let τ(vi, xj) represent the count of persons of
age xj having observational vector vi, and let
τ = {τ(vi, xj)}i=1,...,V ;j=1,...,T
7


## Page 8


so that τ is the collection of all these counts. Fixing θ and ψ, τ has a multinomial
distribution,
τ | θ, ψ ∼Multinomial

N, {r(vi, xj | θ, ψ)}i=1,...,V ;j=1,...,T

where N is the total number of persons observed and
r(vi, xj | θ, ψ) = ψip(vi | xj, θ)
is the probability that a person has age xj and observational vector vi.
The actual observations are contained in the vector y = (y1, . . . , yV ) where,
for i = 1, . . . , V ,
yi =
T
X
j=1
τ(vi, xj).
We have now formulated a full stochastic model for our variables:
π(y, τ, θ, ψ) = π(y | τ)π(τ | θ, ψ)π(θ)π(ψ).
Our strategy is to simulate from this joint distribution conditional on the ob-
served data y using a Metropolis Hastings algorithm. There are three diﬀerent
updating steps, where each of the variables τ, θ, and ψ are updated while the
other variables are kept ﬁxed.
For τ, we get
π(τ | y, θ, ψ) ∝π(y | τ)π(τ | θ, ψ)
and as π(y | τ) simply restricts the sums of counts in τ, we get for i = 1, . . . , V
that
(τ(vi, x1), . . . , τ(vi, xT )) ∼Multinomial

yi,
(
r(vi, xj | θ, ψ)
PT
k=1 r(vi, xk | θ, ψ)
)
j=1,...,T

.
For θ we get
π(θ | y, τ, ψ)
∝
π(τ | θ, ψ)π(θ)
∝


VY
i=1
T
Y
j=1
r(vi, xj | θ, ψ)τ(vi,xj)


K
Y
k=1
π(θk)
∝


VY
i=1
T
Y
j=1
p(vi | xj, θ)τ(vi,xj)


K
Y
k=1
π(θk)
which splits as a product over the diﬀerent age indicators:
π(θk | y, τ, ψ) ∝π(θk)
nk
Y
zk=1
T
Y
j=1
pkzk(xj | θk)τ ′(zk,xj)
8


## Page 9


where
τ ′(zk, xj) =
n1
X
z1=1
· · ·
nk−1
X
zk−1=1
nk+1
X
zk+1=1
· · ·
nK
X
zK=1
τ((z1, . . . , zK), xj).
In other words, the posterior probability for a parameter vector θk is propor-
tional to its prior probability times the product of the probabilities of observing
each of the ni indicator values at each of the possible ages to the power of the
count of the persons having this age and indicator value.
Using a random walk proposal function in the Metropolis Hastings proce-
dure, we can calculate the acceptance probability at each stage. See Section 2.4
for details.
For ψ we get
π(ψ | y, τ, θ) ∝π(τ | θ, ψ)π(ψ) ∝π(ψ)
T
Y
j=1
q(xj | ψ)τ ′′(xj) = π(ψ)
T
Y
j=1
ψτ ′′(xj)
j
where
τ ′′(xj) =
V
X
vi=1
τ(vi, xj).
Using the Dirichlet prior π(ψ) mentioned above, we may simulate ψ from
ψ | τ ∼Dirichlet (τ ′′(x1) + α/T, . . . , τ ′′(xT ) + α/T) .
2.2
Age indicator model parameter values
We now turn to how we can obtain estimates ˆθk1 and ˆθk2 for the parameters of
Equation 1 from published studies on the age indicator. Given the raw data from
such a study, i.e., a list of pairs of observed chronological ages and age indicators,
one may use maximum likelihood to ﬁt a model like that of Equation 1 and thus
obtain an estimate for the model parameters. However, age indicator studies
tend to not publish their raw data and a more indirect approach is necessary.
We have chosen to in each case construct a plausible raw data set based on the
information in the paper, and then estimate parameters based on this. As ways
of obtaining such raw data is not the main focus of this paper, we have chosen
fairly ad-hoc procedures.
In Lucas et al. [2016], a total of 1000 males are examined, subdivided accord-
ing to age into 20 groups of 50 males each. Each group consists of persons with
ages within a speciﬁed half-year interval; we approximated the ages to the mid-
dle value of each such interval. Table 2 in Lucas et al. [2016] reports the number
of males within each group that have ”mature” teeth. Maturity is deﬁned in
terms of stage H of Demirjian’s scale, as for the RMV procedure, but using only
the left mandibular third molar, when available. With no explicit information
about the right mandibular third molars in the study, we have chosen to ignore
this slight diﬀerence in deﬁnitions of age indicators.
9


## Page 10


With a raw data set reconstructed in this way, we can apply maximum
likelihood estimation, obtaining the estimates ˆθ11L = 18.6 and ˆθ12L = 0.7.
Details of our computations can be found in the available R code. According to
Equation 1, we can interpret the result for example as follows: We expect mature
teeth in about half of those aged around 18.6, about 85% of those aged around
18.6 + 0.7 = 19.3, and about 97.5% of those aged around 18.6 + 2 · 0.7 = 20.0.
In Mincer et al. [1993], the male study population has 271 individuals. The
number of males observed with each of the age indicators D, E, F, G, H for the
mandible is not reported, but we interpolate these values from Table 1 in the
paper, obtaining 37, 43, 45, 55, and 91, respectively. The quantiles of the ages of
the persons in each of these ﬁve groups are reported in Table 3 of the paper. In
order to construct actual ages within each group, we construct a picewise linear
transformation from the quantiles of the standard normal distribution to the
quantiles reported in the table. Starting with values evenly spread according to
the standard normal, we apply the transformation to obtain age values, making
sure the age limits of 14.1 and 24.9 reported in the study are observed. With a
raw data set reconstructed, we apply maximum likelihood estimation to obtain
the parameters ˆθ11M = 20.0 and ˆθ12M = 3.2. Note that the parameter estimates
based on Mincer et al. [1993] and Lucas et al. [2016] are quite diﬀerent.
Turning to knees, we derive parameter estimates from Ottow et al. [2017],
as this is by far the largest study on MRI knee that uses a method comparable
to that of RMV. Five diﬀerent stages of the age indicator occur in the study:
IIc, IIIa, IIIb, IIIc, and IV. Table 3 in Ottow et al. [2017] lists the number of
males in the study population for which each indicator value has been observed,
and also gives summary statistics for the ages within each group. We use from
these the minimum, maximum, and the three quartile values. With these values
as starting point, we reconstruct raw data in a similar way as for Mincer et al.
[1993], and apply maximum likelihood estimation.
The resulting values are
ˆθ21 = 18.5 and ˆθ22 = 1.5. As mentioned in the introduction, a small subset
of RMV’s cases has undergone second opinion.
In these, more than half of
the knees assessed as mature by RMV was deemed immature in the second
assessment. One cannot draw general conclusions from such a small and selected
subpopulation, but a worst case scenario might be that around half of all knees
that are ”almost mature” (i.e. stage IIIc) are incorrectly classiﬁed as mature in
RMV’s material. Based on that possibility, we have also estimated parameters
under the assumption that half of those 32 observations classiﬁed as stage IIIc
are counted together with staget IV as mature. Under this assumption we get
the estimates ˆθ21c = 17.8 and ˆθ22c = 1.7.
In contrast to the relatively few studies that exist on age assessment with
MRI knee, there are numerous studies on the third molars. We have not made a
comprehensive review of these, and the choice of Mincer and Lucas can probably
be discussed as to whether they are the most relevant ones. We have chosen
these for our analysis as they are among the few studies on teeth RMV refers
to in the description of their methodology, R¨attsmedicinalverket [2017]. Thus,
these studies have been used to motivate RMV’s choice of methods and ought
10


## Page 11


therefore be relevant to their procedure. As results based on the Mincer and
Lucas studies are quite diﬀerent, they cannot both correspond to the RMV
procedure, but they, and the Ottow study, provide information about what
parameter values are reasonable.
Technically, we deal with this by deﬁning prior distributions using the values
from the studies in diﬀerent ways. For the teeth parameters, we deﬁne three
priors. The ﬁrst is centered close to the Lucas parameter estimates and prescribe
limited variation around these. Mathematically we deﬁne
πLucas(θ11, θ12) ∝Normal(θ11; 18.6, 0.2) · Normal(θ12; 0.7, 0.2) · I(θ12 > 0).
In other words, the prior density is proportional to the product of two normal
densities, truncated so that θ12 is positive. A way to understand this prior is that
we are approximately 95% sure θ11 is in the interval [18.6 −0.4, 18.6 + 0.4] and,
independently, approximately 95% sure θ12 is in the interval [0.7−0.4, 0.7+0.4].
We also deﬁne a similar ”Mincer” prior that is centered on the values ˆθ11 = 20.0
and ˆθ12 = 3.2, and a ”wide” prior that is centered on values averaged from the
two studies, using 4 times as large standard deviation as the Lucas and Mincer
priors. Parameter values and 95% credibility intervals are listed in Table 2.
For the knee parameters, we also deﬁne three priors.
The ﬁrst two are
centered close to the Ottow parameter estimates, with the ﬁrst having the same
narrow variation as the Lucas and Mincer priors, and the second having the
wider variation. Finally, we deﬁne a third narrow prior centered close to the
estimated parameters ˆθ21c = 17.79 and ˆθ22c = 1.76 obtained by interpreting half
of observations in stage IIIc as mature. Parameter values and 95% credibility
intervals are listed in Table 2.
Figure 1 illustrates the narrow and wide knee parameter priors centered on
the Ottow estimates by plotting a sample of possible age indicator probability
curves under each prior. The middle solid curve in each of the plots corresponds
to the parameters ˆθ21 = 18.5 and ˆθ22 = 1.5. The dotted lines indicate how these
curves may vary under each prior.
2.3
Speciﬁcation of prior for the population proﬁle
Speciﬁcation of a prior age distribution for the population of males that have
been subjected to RMVs age determination procedure during 2017 is a diﬃcult
task. The prior for an individual should be based on all knowledge about this
individual excluding the age indicators. Such general knowledge can include
other observations of biological maturity made by medical personnel, observa-
tions of psychological maturity made by teachers or other qualiﬁed observers,
documentable circumstances surrounding the life situation, as well as of course
the reasons why the person has been required by the Swedish migration author-
ity to complete the RMV procedure. The age prior for the whole population
studied in this paper should represent an average over their individual priors.
The diﬃculties with establishing such a prior can lead some researchers to the
conclusion that frequentist statistical methods where a prior does not seem to be
11


## Page 12


16
18
20
22
24
26
0.0
0.2
0.4
0.6
0.8
1.0
Age
Probability
16
18
20
22
24
26
0.0
0.2
0.4
0.6
0.8
1.0
Age
Probability
Figure 1: The probability for observing mature knees as a function of age,
assuming the observation is not missing.
The continuous line in either plot
illustrates the most likely model, with parameters ˆθ21 = 18.5 and ˆθ22 = 1.5.
The dotted lines illustrate other possibilities under each prior: The left ﬁgure
uses the narrow Ottow prior while the right ﬁgure uses the wide prior.
12


## Page 13


needed are preferable to our Bayesian approach. However, when conclusions are
drawn using such frequentist methods, they generally correspond to the use of
a particular prior, as mentioned in the introduction. For example, the ”hidden”
prior assumption may be that the a priori age distribution corresponds to that
of a study population, or that it is uniform within some age interval, for example
between 14 and 25. So, the relevant question is whether we can establish a prior
that is more realistic than such hidden priors.
In this paper, we will use as a starting point an age proﬁle illustrated with
the solid line in the upper left-hand plot of Figure 2. This line represents the
cumulative prior probability that a person has an age below that given on the
x-axis. Thus, for example, the prior probability that a person is below 18 years
is about 35%. Mathematically, the prior is represented by a Gamma density
with parameters 4 and 1, translated to be at least 15 and truncated to the
interval between 15 and 30. As this distribution is rather arbitrarily chosen,
we use a hierarchical prior with a lot of uncertainty around this starting point.
The exact mathematical mechanism for specifying the hyperprior is discussed in
Section 2.1. We use here the hyperparameter α = 3 together with a discretiza-
tion into T = 100 ages. As can be seen in the upper left-hand plot of Figure 2,
95% credibility intervals for the prior percentage of persons that have reached
speciﬁc ages are quite wide. Thus, we believe the prior is ﬂexible enough so
that our choice of starting point will not inﬂuence results signiﬁcantly; this is
further discussed in the supplementary material Mostad and Tamsen [2018].
2.4
Convergence and accuracy
The MCMC simulation outlined in Section 2.1 uses a proposal function alter-
nating between changing the population proﬁle φ, changing the tooth model pa-
rameters θ1, and changing the knee model parameters θ2. Whereas Section 2.1
lists the exact conditional distribution for ψ, we use symmetric proposal func-
tions for θ1 and θ2, computing also acceptance probabilities. Speciﬁcally, the
proposals perturb the four parameters of each θk using normal distributions, see
the R code for details. Our choices led to slow but acceptable mixing rates.
With clearly unimodal posteriors, convergence is fairly easy to assess using
plots and multiple chains with diﬀerent starting points. In our implementation,
acceptance rates are around 0.1-0.2 for both teeth and knee parameters. For
ﬁnal results we simulated 1 million MCMC cycles for each model, using a burn-
in of 20000 cycles. Each such computation took around 20 minutes on a laptop.
However, similar accuracy was obtained with much smaller number of iterations.
The R code used is available from the supplementary material Mostad and
Tamsen [2018].
3
Results
In intial computations, we ﬁx knee parameters to those estimated from the Ot-
tow study (see Section 2.2) and use as a ﬁxed age proﬁle the starting point
13


## Page 14


proﬁle presented in Section 2.3. We then combine with teeth parameters es-
timated from either the Lucas or the Mincer study (see Section 2.2) and in
each case estimate the remaining model parameters using maximum likelihood.
For example, when using the Lucas numbers, we get ˆθ13 = 0.19, ˆθ14 = 0.023,
ˆθ23 = 0.03, and ˆθ24 = −0.003. Recall that ˆθ13 represents the probability for a
person aged 20 to have missing tooth data, while ˆθ14 represents the slope of the
line indicating how this probaility changes with age. ˆθ23 and ˆθ24 are the similar
parameters for the knee. The parameters are illustrated in the upper left-hand
corner of Figure 3.
Using either the Lucas or Mincer numbers, we can now make tables of pre-
dicted counts, similar to Table 1. The predicted tables, however, are quite dif-
ferent from Table 1. Indeed, in both cases, we can reject with p-values smaller
than 10−5 that the data in Table 1 can come from the models, and we can
safely discard these initial models. Details of the computations can be found in
Mostad and Tamsen [2018].
The natural question to ask is then: Which combinations of age distributions
and age indicator models could reasonably have produced the observed data?
A little thought will convince the reader that there will be no unique solution.
For example, if one age proﬁle and set of indicator models could produce the
data, then simply translating the ages in the age proﬁle and the models by the
same amount will give a result that ﬁts the data equally well. So our question
needs to be reﬁned further, we need to ask: Which combinations of reasonable
age distributions and reasonable age indicator models could reasonably have
produced the observed data?
It is possible to make computations where we relax only assumptions about
the population proﬁle or only those about the age indicator model parameters.
Such computations can be found in Mostad and Tamsen [2018]. However, the
most realistic option seems to be to relax assumptons about both model com-
ponents simultaneously. The population proﬁle is certainly unknown and will
probably not look exactly as the starting point proﬁle of Section 2.3. So from
now on, we use the hierachical prior of Section 2.3. The age indicator model
parameters are also uncertain; for example, the Mincer and the Lucas parameter
estimates cannot both be correct for the RMV procedure. However, there may
be diﬀerent opinions about the information the studies contain about what the
reasonable RMV parameters are. Thus, we have chosen to report results for ﬁve
diﬀerent models, each using the information from the age indicator studies in
diﬀerent ways.
Model 1 combines the prior centered on the Lucas parameter estimates with the
prior centered on the Ottow parameter estimates.
Model 2 is the same as model 1 except that the Lucas numbers are replaced with
the Mincer numbers.
Model 3 recognizes the large uncertainty in both knee and teeth parameters and
uses the wide prior centered on the average between the Mincer and Lucas
14


## Page 15


Prior
Posterior
Posterior
Posterior
Posterior
Posterior
Model 1
Model 2
Model 3
Model 4
Model 5
Lucas
θ11
18.6
19.1
18.8
18.2 – 19.0
18.8 – 19.3
18.5 – 19.1
θ12
0.7
0.9
1.0
0.3 – 1.1
0.8 – 1.2
0.8 – 1.2
Mincer
θ11
20.0
20.0
19.9
19.6 – 20.4
19.7 – 20.3
19.6 - 20.3
θ12
3.2
3.1
3.2
2.8 – 3.6
2.8 – 3.5
2.8 – 3.6
Wide
θ11
19.3
19.3
prior
17.7 – 20.9
18.3 – 20.4
teeth
θ12
2.0
1.9
0.4 – 3.6
0.9 – 3.2
Ottow
θ21
18.5
18.0
18.5
18.1 – 18.9
17.7 – 18.3
18.1 – 18.8
θ22
1.5
1.2
1.5
1.1 – 1.9
1.0 – 1.6
1.1 – 1.8
Wide
θ21
18.5
17.9
prior
16.9 – 20.1
16.9 – 18.9
knees
θ22
1.5
1.5
0.0 – 3.1
1.0 – 2.5
Ottow
θ21
17.8
17.5
17.8
IIIc
17.4 – 18.2
17.2 – 17.8
17.5 – 18.2
θ22
1.7
1.5
1.7
1.3 – 2.1
1.2 – 1.9
1.4 – 2.1
Table 2: Prior and posterior parameter distributions. The ranges indicate ap-
proximate 95% credibility intervals for each parameter.
parameters together with the wide prior centered on the Ottow parameter
estimates.
Model 4 combindes the prior centered on the Lucas parameter estimates with the
prior centered on the adjusted Ottow parameters computed in Section 2.2.
Model 5 is the same as model 4 except that the Lucas numbers are replace with
the Mincer numbers.
The actual age indicator parameter values used in the priors of each model
can be read from Table 2, which also lists information about the posteriors for
the parameters. A ﬁrst impression is that the distribution of parameter values
do not change very much from the prior to the posterior. The clearest change
is in model 1, where θ11 and θ21 are very close in the prior and more than one
year apart in the posterior. In fact, in all the posterior models, the diﬀerence
between the two parameters is at least 1.1 years, meaning that knees mature on
average at least one year before teeth.
15


## Page 16


16
18
20
22
24
26
0.0
0.4
0.8
Prior
Age
Probability
16
18
20
22
24
26
0.0
0.4
0.8
Model 1
Age
Probaility
16
18
20
22
24
26
0.0
0.4
0.8
Model 2
Age
Probaility
16
18
20
22
24
26
0.0
0.4
0.8
Model 3
Age
Probaility
16
18
20
22
24
26
0.0
0.4
0.8
Model 4
Age
Probaility
16
18
20
22
24
26
0.0
0.4
0.8
Model 5
Age
Probaility
Figure 2: Prior and posterior population proﬁles. The middle line in each plot
indicates the most likely proﬁles.
The other lines delineate the 2.5%, 25%,
75%, and 97.5% quantiles, respectively. Thus, vertical intervals between the
two dotted lines represent 95% credibility intervals.
16


## Page 17


To better interpret the models, we also need to look at their posterior age
population proﬁles, illustrated in Figure 2. As an example, consider the pos-
terior for model 2, which has a curious step-like shape. The central black line
roughly goes from around 0.4 to around 0.9 over the year between the ages of
22 and 23. This means that around half of the population is predicted to have
an age between 22 and 23 years. In other words, in order to explain the data of
Table 1 using the parameters of model 2, we need to accept that roughly half of
those going through the RMV procedure were exactly between 22 and 23 years,
while there were much fewer in any of the other age groups between 15 and 30.
In our opinion, this is unrealistic, and would tend to discount our trust in model
2. A similar thing happens with model 5, and even to some extent with model
3. Thus, in terms of posterior age proﬁles, we conclude that models 1 and 4 are
most realistic, whereas we put less trust in results for model 2 and 5, and to
some degree model 3.
How can the population proﬁle eﬀect above be explained? The data of Ta-
ble 1 show that there are substantially more persons with mature knees and
immature teeth than with immature knees and mature teeth. For this to hap-
pen, there needs to be a substantial age interval where it is substantially more
probable that knees are mature than that teeth are mature. The illustration
of the ﬁxed parameters model in Figure 3 shows how that model fails to fulﬁll
this criterion. The other models fulﬁll the criterium in diﬀerent ways. However,
we can notice that in models 2 and 5, the line for knee maturity crosses below
the line for tooth maturity at later ages than in the remaining models. Thus,
in models 2 and 5, the ages of those tested need to be more concentrated in a
particular short interval where the probability for knee maturity is substantially
higher than the probability for tooth maturity. This results in the population
”bumps” for these models observed in Figure 2.
It also explains why the θ21 parameter generally needs to be 1-2 years smaller
than the θ11 parameter for models to ﬁt the data. In fact, in models 1 through 4,
the posterior diﬀerence between these parameters is on average 1.1 to 1.5 years.
The diﬀerence is 2.1 in model 5, but as mentioned above, we put less trust in
the results of this model. Further computations, see Mostad and Tamsen [2018],
conﬁrm that the time where 50% of persons have attained a mature knee occurs
1 - 1.5 years before the time when 50% of persons have attained mature teeth.
Speciﬁcally, this time point for knees cannot occur after this time point for
teeth.
3.1
Classiﬁcation error rates
Each of the diﬀerent models have consequences for the actual error rates of the
current RMV procedure. In each stage of our simulation we can compute the
probability for a person in each of the 9 classiﬁcation groups to be over 18. The
results are given in Table 3 in the form of classiﬁcation error rates, using the
classiﬁcation rule employed by RMV and the Swedish migratory authority.
A ﬁrst observation may be that error rates are rather large. Although error
rates when classifying adults as children seem to be larger than those when
17


## Page 18


16
18
20
22
24
26
0.0
0.2
0.4
0.6
0.8
1.0
Fixed parameters
Age
Probability
16
18
20
22
24
26
0.0
0.2
0.4
0.6
0.8
1.0
Model 1
Age
Probability
16
18
20
22
24
26
0.0
0.2
0.4
0.6
0.8
1.0
Model 2
Age
Probability
16
18
20
22
24
26
0.0
0.2
0.4
0.6
0.8
1.0
Model 3
Age
Probability
16
18
20
22
24
26
0.0
0.2
0.4
0.6
0.8
1.0
Model 4
Age
Probability
16
18
20
22
24
26
0.0
0.2
0.4
0.6
0.8
1.0
Model 5
Age
Probability
Figure 3: Illustration of the posterior expected model parameters, under various
models. The straight lines indicate the posterior rates for missing data. The
dotted lines correspond to the knee model; the continuous lines to the teeth
model.
18


## Page 19


RMV
N
Model
Model
Model
Model
Model
classiﬁcation
1
2
3
4
5
Error rates when classifying as above 18
K+, T+
4176
1
1
2
2
3
0–3
0–3
0-8
0–8
0–7
K+, T-
1735
15
11
23
38
26
1–46
2–27
1-68
5–80
7–54
K+, T0
1364
3
3
6
8
7
0-10
0–7
0-18
1–20
1–15
K-, T+
348
9
50
35
20
57
0–35
15–85
0–88
1–63
19–90
K0, T+
187
1
2
3
2
4
0–4
0–7
0–10
0–9
1–10
Error rates when classifying as below 18
K-, T-
1087
49
26
28
28
23
10–96
4 – 68
2–89
4–79
3–61
K-, T0
237
66
36
43
48
31
32–98
8–75
6 –94
17–88
5–69
K0, T-
83
77
78
68
55
64
45–99
57–95
27–98
17–92
36–89
Table 3: Estimated error rates in percent when classifying as over 18.
The
ranges contain a 95% credibility interval.
19


## Page 20


classifying children as adults, the latter may be considered a larger problem,
because of the large consequences it has for a child to be classiﬁed as an adult.
Another observation is the huge uncertainty surrounding many error rates. This
uncertainty is a consequence of the lack of knowledge about the fundamental
parameters of this unvalidated age assessment procedure.
When interpreting these numbers, one should remember how the diﬀerent
models are meant to reﬂect diﬀerent assumptions about relevancy of diﬀerent
published studies for the RMV procedure. For example, in models 1 and 4, one
assumes the RMV procedure corresponds more closely to the one employed in
Lucas, while in models 2 and 5, one assumes it corresponds more closely the
the one employed in Mincer. Interpretation should also take into account that
models 2 and 5 seem unlikely in our study because they appear to require a
peculiar age proﬁle to ﬁt the data.
3.2
Conclusions
Firstly, it seems clear that the properties of the unvalidated RMV procedure
are quite uncertain. Studies that have been used to argue that the procedure
has certain properties seem to give quite diﬀerent parameter estimates, and the
uncertainties in important properties such as the classiﬁcation error rates are
large. In our view, it is unacceptable that a procedure with such unclear prop-
erties has the central role that RMVs procedure has in Sweden’s age assessment
of of asylum seekers and in some criminal cases.
Secondly, even with these uncertainties, some information can be obtained
from the study. For example, it seems a consistent conclusion is that the age
where 50% of knees are mature occur around 1-1.5 years before corresponding
age for teeth teeth, as measured by the RMV procedure, as other models would
require an unrealistic age proﬁle to explain the data.
Thirdly, even if there are large uncertainties, some information about the
error rates can be estimated. For some groups, in particular those that have
measured one mature age indicator and another immature, these rates seem
to be around 10-30%, and may be above 50%. In our view, these rates are
unacceptably high, taking into consideration the serious consequences for a child
to be classiﬁed as an adult.
4
Discussion
In this paper, we present a general method for studying the properties of an
unvalidated age assessment procedure. Although uncertainties in many results
are large, we show how it is possible to obtain some information about model
parameters and error rates using only classiﬁcation counts and priors guided by
published studies. A key reason is that two age indicators have been observed,
so that one can learn about the diﬀerences in their parameters. Applying our
model in a situation with three or more age indicators would probably further
strengthen results.
20


## Page 21


As with any elaborate stochastic model, one needs to ask how much results
depend on the particular technical assumptions and choices we have made.
For example, we have assumed conditional independence between age indica-
tors given age. Should evidence appear showing that knee and tooth maturity
are strongly correlated given age, conclusions from this paper would certainly
change to some degree. The particular form of our age indicator probability
model given in Equations 2 and 3 is of course also a simpliﬁcation. In par-
ticular, we do not attempt to adjust for the fact that the asylum seekers the
RMV procedure has been applied to generally have diﬀerent genetic and socioe-
conomic backgrounds compared to the study populations of most age indicator
studies. Further research on age indicators is likely to yield more complex mod-
els better adapted to reality. But in the context of the current paper, where
model uncertainty is already quite high, resulting adjustmens are likely to be
moderate.
We have made a substantial eﬀort to determine the inﬂuence on results of
our choice for hierarchical prior for the population age proﬁle. Although the
parametric model is fairly arbitrary, its properties, as illustrated in the top left-
hand plot of Figure 2, seem reasonable. In particular, there is a wide prior
uncertainty about the proportion of those tested that has an age below 18.
Figure 2 illustrates how the posterior distributions are fairly diﬀerent from the
prior, indicating that the prior has a limited inﬂuence.
The supplementary
material Mostad and Tamsen [2018] contains further discussions and studies
of the population age proﬁle prior, including results using an alternative prior.
Based on our work, we are conﬁdent that we would reach the conclusions listed
in Section 3.2 using any reasonable choice of population prior.
We have in this paper presented numerical results using a handful of diﬀerent
models. Although we believe these span a set of reasonable combinations of
age indicator model assumptions, there are cleary many more combinations for
which one could do simulations. Indeed, we hope that the R code developed for
this paper can be used for further investigations of the relationship between such
model assumptions and resulting error rate estimates. The R code is available
as part of the online supplementary material Mostad and Tamsen [2018].
As the RMV procedure is still in use, deciding the fate of hundreds of people
every month, there is an urgent need to learn more about its properties. One
possibility is to use ”second opinion data”, now available for some of those 9280
investigated, to calibrate our model. An even more powerful calibration could of
course be obtained using data where the current RMV procedure is performed
on as study population with known ages.
Another interesting possibility is to make our modelling of the RMV proce-
dure more detailed. In particular, as RMV uses two experts for each age indi-
cator and both experts need to agree on maturity for declaring the measured
body part as mature, there is a possibility that results depend on selection of
observers. However, requests for data from RMV which could could be used in
such an extended model have so far not been accommodated.
21


## Page 22


References
Fabrice Dedouit, Julien Auriol, Herv´e Rousseau, Daniel Roug´e, Eric Crub´ezy,
and Norbert Telmon. Age assessment by magnetic resonance imaging of the
knee: a preliminary study. Forensic science international, 217(1-3):232–e1,
2012.
Arto Demirjian, H Goldstein, and James Mourylian Tanner. A new system of
dental age assessment. Human biology, pages 211–227, 1973.
EASO. Practical guide on age assessment, second edition. Technical report,
EASO, 2018. doi:10.2847/29226.
Oguzhan Ekizoglu, Elif Hocaoglu, Ercan Inci, Ismail Ozgur Can, Sema Aksoy,
and Cemal Kazimoglu. Forensic age estimation via 3-t magnetic resonance
imaging of ossiﬁcation of the proximal tibial and distal femoral epiphyses: use
of a t2-weighted fast spin-echo technique. Forensic science international, 260:
102–e1, 2016.
Fei Fan, Kui Zhang, Zhao Peng, Jing-hui Cui, Na Hu, and Zhen-hua Deng.
Forensic age estimation of living persons from the knee: Comparison of mri
with radiographs. Forensic science international, 268:145–150, 2016.
Bianca Gelbrich, Carolin Frerking, Sandra Weiß, Sebastian Schwerdt, Angelika
Stellzig-Eisenhauer, Eve Tausche, and G¨otz Gelbrich. Combining wrist age
and third molars in forensic age estimation: how to calculate the joint age
estimate and its error rate in age diagnostics. Annals of human biology, 42
(4):389–396, 2015.
Jan Alexander Kr¨amer, Sven Schmidt, Kai-Uwe J¨urgens, Markus Lentschig,
Andreas Schmeling, and Volker Vieth. Forensic age estimation in living in-
dividuals using 3.0 t mri of the distal femur. International journal of legal
medicine, 128(3):509–514, 2014.
Victoria S Lucas, Manoharan Andiappan, Fraser McDonald, and Graham
Roberts. Dental age estimation: a test of the reliability of correctly iden-
tifying a subject over 18 years of age using the gold standard of chronological
age as the comparator. Journal of forensic sciences, 61(5):1238–1243, 2016.
Harry H Mincer, Edward F Harris, and Hugh E Berryman. The abfo study
of third molar development and its use as an estimator of chronological age.
Journal of Forensic Science, 38(2):379–390, 1993.
Petter Mostad and Fredrik Tamsen. Supplementary material to paper. http:
//www.math.chalmers.se/~mostad/age/, 2018.
Christian Ottow, Ronald Schulz, Heidi Pfeiﬀer, Walter Heindel, Andreas
Schmeling, and Volker Vieth. Forensic age estimation by magnetic resonance
22


## Page 23


imaging of the knee: the deﬁnite relevance in bony fusion of the distal femoral-
and the proximal tibial epiphyses using closest-to-bone t1 tse sequence. Eu-
ropean radiology, 27(12):5041–5048, 2017.
R¨attsmedicinalverket. Metodbeskrivning f¨or r¨attsmedicinalverkets medicinska
˚aldersbed¨omningar 18 ˚ars gr¨ansen. Diarienumber: D17-90200, 2017.
Pauline Saint-Martin, Camille R´erolle, Julien Pucheux, Fabrice Dedouit, and
Norbert Telmon. Contribution of distal femur mri to the determination of
the 18-year limit in forensic age estimation.
International journal of legal
medicine, 129(3):619, 2015.
A Schmeling, C Grundmann, A Fuhrmann, H-J Kaatsch, B Knell, F Ram-
sthaler, W Reisinger, T Riepert, S Ritz-Timme, FW R¨osing, et al. Criteria for
age estimation in living individuals. International journal of legal medicine,
122(6):457, 2008.
Andreas Schmeling, Reinhard Dettmeyer, Ernst Rudolf, Volker Vieth, and Gun-
ther Geserick.
Forensic age estimation: methods, certainty, and the law.
Deutsches ¨Arzteblatt International, 113(4):44, 2016.
Fredrik Tamsen.
En majoritet av ﬂickor n¨ara 18 ˚ar kan felbed¨omas
som
vuxna
med
mr-kn¨a.
L¨akartidningen
2017;114:EWFM,
2017.
http://lakartidningen.se/Opinion/Debatt/2017/10/
En-majoritet-av-flickor-nara-18-ar-kan-felbedomas-som-vuxna-med-MR-kna/.
Franco Taroni, Silvia Bozza, Alex Biedermann, Paolo Garbolino, and Colin
Aitken. Data analysis in forensic science: a Bayesian decision perspective,
volume 88. John Wiley & Sons, 2010.
PW Thevissen, Steﬀen Fieuws, and Guy Willems. Human dental age estimation
using third molar developmental stages: does a bayesian approach outperform
regression models to discriminate between juveniles and adults? International
journal of legal medicine, 124(1):35, 2010.
Volker Vieth, Ronald Schulz, Walter Heindel, Heidi Pfeiﬀer, Boris Buerke, An-
dreas Schmeling, and Christian Ottow. Forensic age assessment by 3.0 t mri of
the knee: proposal of a new mri classiﬁcation of ossiﬁcation stages. European
radiology, pages 1–8, 2018.
23

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]