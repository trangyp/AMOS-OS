---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0902.1426v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 0902.1426v1_Optimal_designs_for_dose-finding_experiments_in_toxicity_studies

> Source: 0902.1426v1_Optimal_designs_for_dose-finding_experiments_in_toxicity_studies.pdf

> Pages: 23

---


## Page 1


arXiv:0902.1426v1  [stat.ME]  9 Feb 2009
Bernoulli 15(1), 2009, 124–145
DOI: 10.3150/08-BEJ152
Optimal designs for dose-ﬁnding experiments
in toxicity studies
HOLGER DETTE1, ANDREY PEPELYSHEV2 and WENG KEE WONG3
1Ruhr-Universit¨at Bochum, Fakult¨at f¨ur Mathematik, 44780 Bochum, Germany.
E-mail: holger.dette@ruhr-uni-bochum.de
2St. Petersburg State University, Department of Mathematics, St. Petersburg, Russia.
E-mail: andrey@ap7236.spb.edu
3Departament of Biostatistics, University of California, Los Angeles, CA 90095-1772, USA.
E-mail: wkwong@ucla.edu
We construct optimal designs for estimating fetal malformation rate, prenatal death rate and
an overall toxicity index in a toxicology study under a broad range of model assumptions. We
use Weibull distributions to model these rates and assume that the number of implants depend
on the dose level. We study properties of the optimal designs when the intra-litter correlation
coeﬃcient depends on the dose levels in diﬀerent ways. Locally optimal designs are found,
along with robustiﬁed versions of the designs that are less sensitive to misspeciﬁcation in the
initial values of the model parameters. We also report eﬃciencies of commonly used designs in
toxicological experiments and eﬃciencies of the proposed optimal designs when the true rates
have non-Weibull distributions. Optimal design strategies for ﬁnding multiple-objective designs
in toxicology studies are outlined as well.
Keywords: dose-ﬁnding experiment; locally c-optimal design; multiple-objective design; robust
optimal design; Weibull model
1. Introduction
Developmental toxicity studies play an important role in identifying substances that may
pose a danger to developing fetuses, including prenatal death and malformation among
live fetuses. Krewski and Zhu (1995) and Zhu, Krewksi and Ross (1994) demonstrate
that joint dose-response models for describing prenatal death and fetal malformation in
developmental toxicity experiments have a good agreement with real data. These models
can be used to estimate the eﬀective dose corresponding to a gene excess risk for both
these toxicological end-points, as well as for overall toxicity. It appears that toxicologists
are generally less receptive to a more rigorous treatment of design issues; see a recent
foreword/commentary in 2006 in Nature by Giles where the author expounded on the
This is an electronic reprint of the original article published by the ISI/BS in Bernoulli,
2009, Vol. 15, No. 1, 124–145. This reprint diﬀers from the original in pagination and
typographic detail.
1350-7265
c⃝
2009 ISI/BS


## Page 2


Optimal designs for dose-ﬁnding experiments
125
lack of sophistication in current designs for animal experiments. Very recently there
have been a handful of theoretical articles that utilize statistical principles to design
toxicology studies. This paper follows this trend and discusses how one may construct
eﬃcient designs for estimating malformation rate, prenatal death and overall toxicity
levels under a broad range of model assumptions. A scientiﬁcally sound and eﬃcient
study is crucial because toxicology studies are increasingly more expensive in terms of
time and labor. An eﬃcient design potentially also means that signiﬁcantly fewer animals
will be required in the experiment. In what is to follow, our designs for such experiments
are speciﬁed in terms of the number of doses to be used, the dose spacing, and the
proportion of animals to be assigned to each dose.
Krewski, Smythe and Fung (2002) studied locally optimal designs for the estimating
the eﬀective dose using joint Weibull dose-response models. The locally optimal designs
depend on the parameters of the Weibull model and the degree of intra-litter correlation.
This paper addresses several important design issues in toxicology, such as estimating
benchmark doses. Estimating benchmark doses has a long history in toxicological studies
and research continues to this day; some recent papers include (Woutersen et al. (2001),
Moerbeek et al. (2004), Slob et al. (2005)). As in Krewski, Smythe and Fung (2002),
we seek optimal experimental designs that minimize the variance of the estimated ef-
fective dose for prenatal death, or malformation or overall toxicity, given the number of
implants. (Here we recall an implant is an embryo that has been incorporated into the
maternal uterus.) These are two important and common end-points measuring tetrato-
genicity (embryotoxicity) in animal studies (Zhu, Krewski and Ross (1994)). Because
nonlinear models are employed in such studies, these authors used the simplest design
strategy and found numerical locally optimal designs for estimating the model models.
However, it is known that locally optimal designs can depend sensitively on the nominal
or initial values of the model parameters. In our work, we present a more sophisticated
approach to design developmental toxicity experiments so that the implemented design
is more robust to misspeciﬁcation in the initial values. Speciﬁcally, we ﬁrst derive analyt-
ical properties of locally optimal designs for estimating the benchmark dose of prenatal
death. In particular, we prove several results on the number and levels of doses and in-
variance properties of the locally optimal designs. We also correct an error in the work
of Krewski, Smythe and Fung (2002), who used the wrong information matrix for the
construction of the optimal designs. Second, we study the robustness properties of these
locally optimal designs with respect to misspeciﬁcation of the initial parameters. Third,
we construct locally optimal designs for estimating the eﬀective dose of overall toxicity
and investigate their sensitivities to misspeciﬁcation in the initial parameters. Fourth, we
construct designs that are robust with respect to misspeciﬁcation of the initial parame-
ters, and so mitigate a concern raised by some toxicologists. We also investigate relative
eﬃciencies of commonly used designs in developmental toxicity experiments.
Section 2 gives statistical background for our models, which were recently proposed
in the literature for developmental toxicity studies. In Section 3 we present analytical
results for locally optimal designs for estimating the eﬀective dose of prenatal death
and investigate the sensitivity of these designs with respect to misspeciﬁcation of the
unknown parameters. Section 4 considers similar problems for estimating the eﬀective


## Page 3


126
H. Dette, A. Pepelyshev and W.K. Wong
dose of overall toxicity, and in Section 5 the methodology is extended to obtain robust
and eﬃcient designs by a maximin approach. Section 6 evaluates eﬃciencies of commonly
used designs in animal studies and brieﬂy discusses eﬃciencies of optimal designs when
non-Weibull probability models are used. All justiﬁcations for all our results are deferred
to the Appendix.
2. Background for developmental toxicity studies
In developmental toxicity experiments with laboratory animals such as rats or mice,
pregnant females are usually exposed to one of several doses of the test agent (including
a control group at dose zero) during a speciﬁed period in gestation. Upon examining
the uterine contents of each dam, the status of each conceptus is classiﬁed and recorded.
A conceptus may either be dead or alive, and a live fetus may exhibit one or more
malformations. In industry, the number of litters examined per dose is generally 24 for
rats, which is one of the two standard species for segment II reproductive studies, at an
estimated cost of $63,000 for the rat portion of the study. Rabbits are the other standard
species in a segment II reproductive study and the number of rabbits required per dose
is usually 12 with the cost of the study of this species being roughly $72,000 (Klaassen
(2001), page 31–32).
Let mij denote the number of implants in the jth litter of the ith dose di, and let
rij be the number of prenatal deaths, sij be the number of live fetuses, and yij be the
number of fetal malformations. Summary observations from each dam yield a trinomial
response (rij,yij,sij −yij) conditional on mij for which we have
mij = rij + (sij −yij) + yij.
The fetal malformation rate yij/sij and the prenatal death rate rij/mij are of particular
interest. The joint probability of the observed outcome (yij,rij,mij) may be factored as
P(yij,rij,mij) = P(yij|sij,mij)P(rij|mij)P(mij),
where P(mij) is the marginal distribution of the implants number mij. Throughout, we
let π1 denote the probability of any malformation in a live fetus, π2 be the probability
of the prenatal death and let φi be the intra-litter correlation coeﬃcient within ith dose
group. Zhu, Krewski and Ross (1994) used generalized estimating equations in conjunc-
tion with an extended Dirichlet-multinomial covariance function, where the correlation
coeﬃcient is estimated separately. If zij = (yij,rij)T , the conditional covariance of the
observation zij is
Cov(zij|mij) = mij(1 + (mij −1)φi)

µ(1 −µ)
−µπ2
−µπ2
π2(1 −π2)

,
where µ = π1(1 −π2), 1/(1 −mij) < φi < 1.
For simplicity we assume that mij depends only on the dose level and not on the
individual litter, that is, mij = mi = m(di). As pointed out in Krewski, Smythe and Fung


## Page 4


Optimal designs for dose-ﬁnding experiments
127
(2002) this assumption avoids complicating the model with another level of estimation
and permits the development of informative designs. Following Zhu, Krewski and Ross
(1994) we use the Weibull model
πi(d) = 1 −e−ai−bidγi
to describe both probabilities π1 and π2, where d denotes the dose level. Here ai, bi > 0
and γi > 0 are unknown parameters (i = 1,2). We denote the parameters for the proba-
bility πi by θi. Following Catalano et al. (1993) and Zhu, Krewski and Ross (1994), the
overall toxicity is deﬁned by
π3(d) = 1 −(1 −π1(d))(1 −π2(d))
(2.1)
of either a death or malformation occurring. The eﬀective dose EDα for a particular
probability πi is deﬁned as the (unique) solution of the equation
π(EDα) −π(0)
1 −π(0)
= α,
where π(d) represents the probability of a response at dose d and α is a given excess risk.
The excess risk represents additional risk over background among animals that would
not have responded under control conditions. Typical values for α are 0.01 or 0.05, and
when α is set at a very low level, say 10−4, the excess risk is also sometimes called the
benchmark dose or the virtually safe dose (Ryan (1992), Al-Saidy et al. (2003)). Zhu,
Krewski and Ross (1994) proposed an estimate ˆθ for estimating θ, the three parameters
in the Weibull distribution. This estimate is based on quadratic estimating equations
and has been shown to have reasonable eﬃciencies for estimating θ. By the δ-method
(Van der Vaart (1998)) the variance of the estimator d
EDα for the eﬀective dose can be
approximated by
Var(d
EDα) ≈˜DT Cov(ˆθ) ˜D,
(2.2)
and
˜D = ∂
∂θEDα
(2.3)
is the gradient of EDα with respect to θ. We will denote the vector of parameters in πi
by θi and its corresponding estimate by ˆθi, i = 1,2.
Throughout, a design is speciﬁed by the number of diﬀerent dose levels, say k, the
speciﬁc dose levels d1,...,dk and the proportion of patients, say w1,...,wk allocated at
each of these dose levels. In this paper, we consider approximate designs, that is, prob-
ability measures ξ = {di,wi}k
i=1 with ﬁnite support (Silvey (1980), Pukelsheim (1993)).
For a given design ξ and total sample size n, the number of observations at each dose
level nj is obtained by rounding the quantities nwj to integers, such that Pk
j=1 nj = n
(Pukelsheim and Rieder (1992)). Throughout, we assume for the sake of simplicity that
the dose range is given by the interval [0,1], but the adaption of the methodology to other


## Page 5


128
H. Dette, A. Pepelyshev and W.K. Wong
dose intervals is straightforward. In what is to follow, we will only present our design
strategy and results for estimating the eﬀective dose of prenatal death. The strategy for
estimating the eﬀective dose for a given malformation rate is completely analogous and
we omit details and corresponding results for space considerations.
3. Optimal designs for estimating the eﬀective dose of
prenatal death
Under the Weibull model the eﬀective dose for prenatal death equals
EDα =

−ln(1 −α)
b2
1/γ2
.
Recalling that θT
2 = (a2,b2,γ2), the gradient (2.3) in the representation (2.2) is given by
˜D =
∂
∂θ2
EDα = −EDα
γ2


0
1/b2
ln(−ln(1 −α)/b2)/γ2


= −(−ln(1 −α)/b2)1/γ2
γ2


0
1/b2
ln(−ln(1 −α)/b2)/γ2

.
If ξ = {d1,d2,...,dn;w1,w2,...,wn} denotes an approximate design and
Di = ∂
∂θ2
π2(di) = (1 −π2(di))


1
dγ2
i
b2dγ2
i ln(di)

,
it follows that the covariance matrix of the estimate ˆθ2 is approximately
Cov(ˆθ2) ≈M −1(ξ,θ2),
where
M(ξ,θ2) =
n
X
i=1
wi
DiDT
i
Var(ri |mi )
=
n
X
i=1
wi
DiDT
i
mi(1 + (mi −1)φi)π2(di)(1 −π2(di))
(3.1)
is the information matrix of the design. Note that the summands in this matrix diﬀer
by the factors m2
i from the corresponding terms in the information matrix derived by
Krewski, Smythe and Fung (2002). There is, in fact, an error in that paper. Consequently


## Page 6


Optimal designs for dose-ﬁnding experiments
129
we obtain from (2.2) as ﬁrst-order approximation for the variance of the estimate of the
eﬀective dose
Var(d
EDα) ≈Ψ(ξ,θ2) = ˜DT M −1(ξ,θ2) ˜D
(3.2)
and a locally optimal design for estimating the eﬀective dose (of prenatal death) mini-
mizes the function Ψ among all designs for which the EDα is estimable.
It is clear that the information matrix of the optimal design depends on the parameters
of the model, and, in particular on the quantities mi = m(di) and φi = φ(di). The simplest
way to deal with this added complication is to use locally optimal designs proposed
by Chernoﬀ(1953). This strategy requires that a single prior guess for the unknown
parameters is available. In developmental toxicity experiments such knowledge is often
available from preliminary studies. The following results establish properties of locally
optimal designs for estimating the eﬀective dose of prenatal death. In essence, it says that
if the excess risk is not too extreme (i.e., near 0 or 1), the locally optimal design requires
only two doses; otherwise the locally optimal design requires three doses that include the
extreme levels in the dose interval. The proofs rely on the geometric characterization of
c-optimal designs of Elfving (1952) and are deferred to the Appendix.
Theorem 1. Let m and φ denote the functions deﬁning mi = m(di) and φi = φ(di). If
the function
d −→
(1 −π2(d))
m(d)(1 + (m(d) −1)φ(d))π2(d)
(3.3)
is decreasing, there exist numbers α and ¯α such that the following properties hold:
(a) If α ∈(0,α] ∪(¯α,1), the locally optimal design for estimating the eﬀective dose
of prenatal death is supported at three points, including the boundary points d∗
1 = 0 and
d∗
3 = 1 of the design space.
(b) If α ∈(α, ¯α), the locally optimal design for estimating the eﬀective dose of prenatal
death is supported at two points.
We note that if the function φ is increasing, the assumption of Theorem 1 is satisﬁed.
In particular, Bowman, Chen and George (1995) proposed a logistic-type function of the
form
φ(d) =
2
1 + eu1+u2d −1
(3.4)
for describing the relationship between intra-litter correlation and dose, which is widely
used in practice. If u2 < 0 this function satisﬁes the assumptions of Theorem 1. In what
is to follow, we will use this function to model the intra-class correlation using diﬀerent
values of u1 and u2. Of course the case of zero or no correlation is assumed when we set
u1 = u2 = 0.
The next result tells us that we can limit our search for the optimal design to the
protocol interval [0,1] and deduce the corresponding optimal design on the design interval
[0,T ].


## Page 7


130
H. Dette, A. Pepelyshev and W.K. Wong
Theorem 2. Assume that the quantity mi and the function φ are constant. The weights
of the locally optimal design for estimating the eﬀective dose of prenatal death do not
depend on the parameter γ2. Moreover, if d∗
i (a2,b2,γ2,T ) are the support points of the
locally optimal design for estimating the eﬀective dose of prenatal death on the interval
[0,T ], we have
d∗
i (a2,b2,γ2,1) = (d∗
i (a2,b2,1,1))1/γ2,
d∗
i (a2,b2,γ2,T ) = T d∗
i (a2,b2T γ2,γ2,1).
Our next result shows that if the locally optimal design for estimating the prenatal
death requires three dose levels, these dose levels do not depend on the value of the excess
risk α. It also provides a complete analytical description of the locally optimal design
when it is known in advance that the locally optimal design needs only two doses, and
one of them is the zero dose.
Theorem 3. Assume that the conditions of Theorem 1 are satisﬁed.
(a) The support points of the locally optimal design for estimating the eﬀective dose
of prenatal death with three support points do not depend on the value of α.
(b) If the support of a two-point locally optimal design for estimating the eﬀective
dose of prenatal death contains the point 0, then the second support point is equal to
EDα and its weight at EDα is equal to w2 = g(0)/(g(0) + g(EDα)), where
g(d) =
s
(1 −π2(d))
m(d)(1 + (m(d) −1)φ(d))π2(d).
In Table 1 we display numerical locally optimal designs for estimating the eﬀective dose
of prenatal death for various combinations of the parameters when the quantity mi and
the function φ are assumed to be constants. As stated in Theorem 1 the locally optimal
designs are either two-point designs or three-point designs because the monotonicity as-
sumption of the theorem is satisﬁed. In Table 2 we show some results for a non-constant
function φ of the form (3.4), which demonstrate that the assumption of monotonicity on
the function (3.3) is, in fact, needed. For example, if φ(d) = 2/(1 + ed−1) −1 the corre-
sponding function in (3.3) is not decreasing. The locally optimal design for estimating
the eﬀective dose of prenatal death is a 3-point design, but its support dose not contain
the minimal dose 0.
In Table 1 and other tables that follow, we also display on the extreme right column
the eﬃciency of an equally weighted design supported at ﬁve equally spaced points on
the interval [0, 1]. We denote this design by ξu and note that this is an example of a
uniform design where doses are equally spread out and an equal number of observations
are planned at each dose. Uniform designs are intuitively appealing because of their
simplicity. In practice, approximately uniform designs are used. For example, a recent
paper by Lee et al. (2006) used 0,0.5,1,2,3,3.5 (mg/kg) dose levels of cadmium, and
separately, 1,3,5,7.5 dose levels of all-trans-retinoic acid to study their individual and


## Page 8


Optimal designs for dose-ﬁnding experiments
131
combined eﬀects on the induction of forelimb ectrodactyly in C57BL/6 mice. In the cases
considered in both tables, the results show that this particular uniform design did not
perform well, averaging about 50%. This means that roughly twice as many rats will be
Table 1. Locally optimal design for estimating the eﬀective dose of prenatal death conditional
on the number of implants, assuming the functions φ and m are constants. The table also
shows the eﬃciency of the equidistant design ξu = {0,1/4,1/2,3/4,1;1/5,1/5, 1/5,1/5,1/5} (last
column)
α
a2
b2
γ2
d1
d2
d3
w1
w2
w3
ED
eﬀ(ξu)
0.05
0.13
0.15
3.33
0
0.725
0.455
0.545
0.725
0.506
0.05
0.13
0.2
3.33
0
0.696
1
0.429
0.545
0.025
0.665
0.539
0.05
0.13
0.25
3.33
0
0.689
1
0.404
0.547
0.049
0.621
0.557
0.05
0.13
0.3
3.33
0
0.682
1
0.387
0.549
0.064
0.588
0.568
0.05
0.13
0.35
3.33
0
0.676
1
0.373
0.551
0.075
0.562
0.575
0.05
0.13
0.4
3.33
0
0.670
1
0.363
0.554
0.083
0.540
0.579
0.05
0.01
0.27
3.33
0
0.607
0.285
0.715
0.607
0.481
0.05
0.05
0.27
3.33
0
0.653
1
0.371
0.593
0.036
0.607
0.541
0.05
0.1
0.27
3.33
0
0.678
1
0.390
0.558
0.051
0.607
0.558
0.05
0.15
0.27
3.33
0
0.690
1
0.399
0.543
0.058
0.607
0.564
0.05
0.2
0.27
3.33
0
0.698
1
0.404
0.535
0.061
0.607
0.568
0.05
0.25
0.27
3.33
0
0.703
1
0.407
0.529
0.063
0.607
0.570
0.03
0.13
0.27
3.33
0
0.686
1
0.367
0.538
0.095
0.519
0.590
0.04
0.13
0.27
3.33
0
0.686
1
0.381
0.543
0.076
0.567
0.577
0.05
0.13
0.27
3.33
0
0.686
1
0.396
0.548
0.056
0.607
0.562
0.06
0.13
0.27
3.33
0
0.686
1
0.412
0.554
0.034
0.642
0.546
0.07
0.13
0.27
3.33
0
0.686
1
0.430
0.560
0.010
0.674
0.526
0.08
0.13
0.27
3.33
0
0.703
0.433
0.567
0.703
0.507
0.1
0.13
0.27
3.33
0
0.754
0.420
0.580
0.754
0.499
Table 2. Locally optimal design for prenatal death conditional on the number of implants when
the function m is assumed to be constant and the function φ modeling the correlation is given
by (3.4) (a2 = 0.13, b2 = 0.27, γ2 = 3.33, α = 0.05). The table also shows the eﬃciency of the
equidistant design ξu = {0,1/4,1/2,3/4,1;1/5,1/5, 1/5, 1/5,1/5} (last column)
u1
u2
d1
d2
d3
w1
w2
w3
ED
eﬀ(ξu)
0
−1
0
0.636
1
0.284
0.691
0.025
0.607
0.490
0
−2
0
0.630
1
0.242
0.737
0.021
0.607
0.472
0
−3
0
0.633
1
0.220
0.757
0.023
0.607
0.464
−1
1
0.082
0.746
1
0.447
0.482
0.071
0.607
0.588
−2
2
0.071
0.762
1
0.445
0.487
0.068
0.607
0.569
−3
3
0.052
0.767
1
0.432
0.503
0.065
0.607
0.551


## Page 9


132
H. Dette, A. Pepelyshev and W.K. Wong
Table 3. Eﬃciency for estimating the eﬀective dose of prenatal death. ξ∗(θ0): locally optimal
design for θT
0 = (a2,b2,γ2) = (0.13,0.27,3.33) ξu equidistant design with ﬁve diﬀerent dose lev-
els (including the largest and smallest dose), and design ξmm = {0,0.694,1;0.349,0.515, 0.136}
which is standardized maximin optimal for estimating the eﬀective dose of prenatal death with
respect to Ω= [0.05,0.2] × [0.2,0.4] × [2.5,4.5]
a2
0.05
0.05
0.05
0.05
0.2
0.2
0.2
0.2
b2
0.2
0.2
0.4
0.4
0.2
0.2
0.4
0.4
γ2
2.5
4.5
2.5
4.5
2.5
4.5
2.5
4.5
eﬀ(ξ∗(θ0))
0.802
0.766
0.526
0.967
0.944
0.695
0.749
0.862
eﬀ(ξu)
0.522
0.475
0.563
0.521
0.550
0.496
0.588
0.544
eﬀ(ξmm)
0.808
0.740
0.663
0.923
0.920
0.665
0.872
0.822
needed in the uniform design to obtain estimates for the parameters as accurate as those
provided by the locally optimal design.
In general, our numerical results show that there are four types of locally optimal
designs for estimating the eﬀective dose of prenatal death, namely:
{0,d2,1;w1,w2,w3},
{0,d2;w1,w2},
{d1,d2,1;w1,w2,w3},
{d1,d2;w1,w2}.
Moreover, if the assumptions of Theorem 1 are satisﬁed, there exist only two types, that
is,
{0,d2,1;w1,w2,w3},
{d1,d2;w1,w2}.
Before any design is implemented, it is useful to investigate the robustness of the
locally optimal designs for estimating the eﬀective dose with respect to misspeciﬁca-
tion in the initial parameters. For this purpose we consider the locally optimal ξ∗(θ0) =
{0,0.686,1;0.396,0.548,0.056} for the parameter θT
0 = (a2,b2,γ2) = (0.13,0.27,3.33) and
calculate the eﬃciency
eﬀ(ξ) =
˜DT M −1(ξ,θ) ˜D
˜DT M −1(ξ,θ0) ˜D
(3.5)
for various values of θ. These results are listed in Table 3. We observe that lo-
cally optimal designs are not too sensitive with respect to changes of the param-
eter a2, but a misspeciﬁcation of the parameters b2 and γ2 has more serious ef-
fects. The table also shows the corresponding eﬃciencies of the equidistant design
ξu = {0,1/4,1/2,3/4,1;1/5,1/5,1/5,1/5,1/5}. In most cases these are smaller than the
eﬃciencies of the locally optimal design for estimating the eﬀective dose. In addition, the
table contains eﬃciencies of a maximin design ξmm, whose construction will be motivated
in Section 5. This design performs substantially better than the uniform design ξu and
achieves nearly the same eﬃciencies as the locally optimal design ξ∗(θ0) in those cases
where ξ∗(θ0) is very eﬃcient.


## Page 10


Optimal designs for dose-ﬁnding experiments
133
4. Dose-ﬁnding for overall toxicity conditional
number of implants
If two Weibull models with parameters θT
1 = (a1,b1,γ1) and θT
2 = (a2,b2,γ2) are used for
modeling the overall toxicity in (2.1), the eﬀective dose based on π3(d) is deﬁned as a
solution of the equation
α = 1 −exp(b1EDγ1
α + b2EDγ2
α ),
or, equivalently,
−ln(1 −α) = b1EDγ1
α + b2EDγ2
α .
The approximation for the variance of the estimator based on generalized estimating
equations is given by (2.2), where θT = (θ1,θ2) and
¯D = ∂
∂θEDα =
−1
b1γ1EDγ1−1
α
+ b2γ2EDγ2−1
α







0
EDγ1
α
b1EDγ1
α ln(EDα)
0
EDγ2
α
b2EDγ2
α ln(EDα)







.
If ξ = {d1,d2,...,dn;w1,w2,...,wn} denotes an approximate design we have
Cov(ˆθ) ≈M −1(ξ,θ),
where the information matrix is given by
M(ξ,θ) =

M1(ξ,θ)
0
0
M2(ξ,θ)

and the two non-vanishing blocks are deﬁned by
M1(ξ,θ) =
n
X
i=1
wi
D(1)iDT
(1)i
Var(yi |mi )
=
n
X
i=1
wi
D(1)iDT
(1)i
mi(1 + (mi −1)φi)π1(di)(1 −π2(di))(1 −π1(di)(1 −π2(di))),
M2(ξ,θ) =
n
X
i=1
wi
D(2)iDT
(2)i
Var(ri |mi )
=
n
X
i=1
wi
D(2)iDT
(2)i
mi(1 + (mi −1)φi)π2(di)(1 −π2(di)),


## Page 11


134
H. Dette, A. Pepelyshev and W.K. Wong
with
D(j)i = ∂
∂θj
πj(di) = (1 −πj(di))


1
dγj
i
bjdγj
i ln(di)

,
j = 1,2.
Note that M(ξ,θ) is a block-diagonal matrix and, as a consequence, the optimality crite-
rion minimizing the variance of the estimate for EDα can be interpreted as a composite
optimality criterion in the sense of L¨auter (1974), that is,
Var(d
EDα) ≈Φ(ξ,θ) = ¯DT M −1(ξ,θ) ¯D
= ˜DT
(1)M −1
1 (ξ,θ) ˜D(1) + ˜DT
(2)M −1
2 (ξ,θ) ˜D(2).
(4.1)
It is intuitively clear that locally optimal designs for estimating the EDα for overall
toxicity are three-point designs if the parameters in π1(d) and π2(d) are similar. In all
cases of practical interest these designs have to be calculated numerically. Some examples
of optimal designs are presented in Table 4 for constant functions mi and φi. Table 5
presents optimal designs for the case where the correlation is of the form (3.4) and
the mi’s are constants. We observe that in most cases, the locally optimal designs are
supported at three points, but there are also situations (in particular for large diﬀerences
between the parameters γ1 and γ2), where four diﬀerent dose levels are required for
the optimal estimation of the eﬀective dose of the overall toxicity. The results of our
investigation of the robustness properties of the locally optimal designs for estimating the
eﬀective dose with respect to misspeciﬁcation of the initial parameters are summarized
in Table 6.
We next investigate whether the locally optimal design for estimating the eﬀective dose
of prenatal death is eﬃcient for estimating the eﬀective dose of overall toxicity. We also
compare the optimal design with the equidistant design with ﬁve diﬀerent dose levels.
In Tables 7 and 8, we display eﬃciencies of the two designs for various combinations
of the parameter θ to study their robustness for estimating the eﬀective dose of overall
toxicity when the initial parameters have been misspeciﬁed and the design is optimal for
estimating the eﬀective dose of prenatal death.
We observe that the performance of the locally optimal design for estimating the
eﬀective dose of overall toxicity depends sensitively on changes of the parameters b1
and b2. If b1 is very diﬀerent from the parameter b2 used in the construction of the
locally optimal design for estimating the eﬀective dose of prenatal death, this design
becomes ineﬃcient for estimating overall toxicity. In such cases even the uniform design
performs better. Otherwise the locally optimal design for estimating the eﬀective dose of
prenatal death is at least as good as the uniform design (and in many cases substantially
better). The table also shows eﬃciencies of the design ξmm, which will be constructed
in the following section as a robust and eﬃcient alternative to locally optimal designs.
The design ξmm performs uniformly better than the locally optimal design ξ∗(θ0) for
estimating the eﬀective dose of prenatal death. In many cases, it is substantially more
eﬃcient than the uniform design ξu and in the cases where the equal allocation rule yields
the best eﬃciencies, the loss of eﬃciency obtained from ξmm is rather small.


## Page 12


Optimal designs for dose-ﬁnding experiments
135
Table 4. Locally optimal designs for estimating the eﬀective dose of overall toxicity conditional
on the number of implants. The functions m and φ are constant, α = 0.05 and ξu denotes the
equidistant design with ﬁve diﬀerent dose levels 0,1/4,1/2,3/4,1
a1
b1
γ1
a2
b2
γ2
d1
d2
d3
d4
w1
w2
w3
w4
eﬀ(ξu)
0.06
0.7
2
0.13
0.15
2
0
0.495
1
0.330
0.546
0.124
0.653
0.06
0.7
2
0.13
0.15
3.33
0
0.493
1
0.291
0.574
0.134
0.699
0.06
0.7
3.37
0.13
0.15
2
0
0.573
1
0.372
0.536
0.092
0.593
0.06
0.7
3.37
0.13
0.15
3.33
0
0.658
1
0.331
0.546
0.123
0.634
0.06
0.5
3.37
0.13
0.3
3.33
0
0.665
1
0.333
0.549
0.118
0.607
0.06
0.7
3.37
0.13
0.3
3.33
0
0.653
1
0.321
0.551
0.128
0.619
0.06
0.9
3.37
0.13
0.3
3.33
0
0.640
1
0.311
0.551
0.138
0.630
0.06
0.7
3.37
0.05
0.3
3.33
0
0.630
1
0.299
0.577
0.124
0.593
0.06
0.7
3.37
0.25
0.3
3.33
0
0.673
1
0.338
0.532
0.130
0.635
0.02
0.7
3.37
0.13
0.3
3.33
0
0.646
1
0.315
0.559
0.126
0.641
0.09
0.7
3.37
0.13
0.3
3.33
0
0.657
1
0.325
0.546
0.129
0.613
0.02
1.2
2.2
0.05
0.2
3.7
0
0.402
0.636
1
0.212
0.620
0.040
0.129
0.655
0.02
1.2
2.2
0.05
0.2
3.3
0
0.421
0.541
1
0.221
0.596
0.041
0.141
0.680
0.02
0.9
2.2
0.05
0.2
3.7
0
0.434
0.590
1
0.228
0.585
0.065
0.121
0.674
0.02
1.6
2.2
0.05
0.2
3.7
0
0.368
0.713
1
0.198
0.636
0.029
0.136
0.632
Table 5. Locally optimal designs for estimating the eﬀective dose of overall toxicity conditional
on the number of implants. The functions m is constant, while the correlation function φ is given
by (3.4), a1 = 0.06, b1 = 0.7, γ1 = 3.37, a2 = 0.13, b2 = 0.3, γ2 = 3.33, α = 0.05 and ξu denotes
the equidistant design with ﬁve diﬀerent dose levels 0,1/4,1/2,3/4,1
u1
u2
d1
d2
d3
w1
w2
w3
eﬀ(ξu)
0
−1
0
0.600
1
0.227
0.652
0.121
0.554
0
−2
0
0.594
1
0.192
0.690
0.118
0.538
0
−3
0
0.596
1
0.174
0.708
0.118
0.530
5. Robust and eﬃcient designs for prenatal death
As pointed out in the previous sections, locally optimal designs are not necessarily robust
with respect to a misspeciﬁcation of the unknown parameters. To obtain designs that
are eﬃcient and robust over a certain range of the parameters for the Weibull model, we
study a maximin approach proposed by M¨uller (1995) and Dette (1997), which assumes
that there is prior information on the range of plausible values of unknown parameters.
To be precise, we concentrate on optimal designs for estimating the eﬀective dose of
prenatal death, where the correlation function is given by the one parametric logistic


## Page 13


136
H. Dette, A. Pepelyshev and W.K. Wong
family
φ(d) =
2
1 + e−ud −1.
(5.1)
We assume that the experimenter has some knowledge about the location of the param-
eters, that is,
a2 ∈[a,a],
b2 ∈[b,b],
γ2 ∈[γ,γ],
u ∈[u,u].
For given θT = (a2,b2,γ2) and u, deﬁne ξ∗(θ,u) as the locally optimal designs for esti-
mating the eﬀective dose and, for a given design, deﬁne
eﬀall(ξ,θ,u) =
˜DT M −1(ξ∗(θ,u),θ,u) ˜D
˜DT M −1(ξ,θ,u) ˜D
.
(5.2)
A design ξmm is called standardized maximin optimal for estimating the eﬀective dose if
it maximizes the worst eﬃciency over some set of the parameters, that is,
ξmm = argmax
ξ
min
(θ,u)∈Ωeﬀall(ξ,θ,u).
(5.3)
Here the set Ωis deﬁned by Ω= [a,a]×[b,b]×[γ,γ]×[u,u] and is user-selected. Optimal
designs with respect to this robust criterion have to be calculated numerically in all cases
of practical interest. In Table 9 we display standardized maximin optimal designs with
respect to various sets Ωassuming the quantities mi and the correlation function (5.1)
are constants, that is, u = u = 0. We observe that in all situations the standardized
maximin optimal designs are supported at three points and they include the largest and
smallest doses. However, the results of Braess and Dette (2007) indicate that there will
also exist standardized maximin optimal designs for estimating the eﬀective dose with
Table
6. Eﬃciency
for
estimating
the
eﬀective
dose
of
overall
toxicity
using
three
designs:
ξ∗(θ0),
the
locally
optimal
design
for
θT
0
= (a1,b1,γ1,a2,b2,γ2)T =
(0.06,0.7,3.37,0.13,0.27,3.33), ξu the equidistant design with ﬁve diﬀerent dose levels (including
the largest and smallest dose) and the design ξmm = {0,0.694,1;0.349,0.515,0.136}, which is
standardized maximin optimal for estimating prenatal death with [0.05,0.2]×[0.2,0.4]×[2.5, 4.5]
a1
0.03
0.03
0.03
0.03
0.09
0.09
0.09
0.09
b1
0.4
0.4
0.9
0.9
0.4
0.4
0.9
0.9
γ1
2.7
4.2
2.7
4.2
2.7
4.2
2.7
4.2
a2
0.05
0.05
0.05
0.05
0.2
0.2
0.2
0.2
b2
0.2
0.2
0.4
0.4
0.2
0.2
0.4
0.4
γ2
2.5
4.5
2.5
4.5
2.5
4.5
2.5
4.5
eﬀ(ξ∗(θ0))
0.875
0.873
0.681
0.982
0.981
0.705
0.880
0.882
eﬀ(ξu)
0.588
0.566
0.594
0.584
0.606
0.574
0.619
0.614
eﬀ(ξmm)
0.730
0.965
0.531
0.942
0.906
0.871
0.743
0.984


## Page 14


Optimal designs for dose-ﬁnding experiments
137
Table
7. Eﬃciency
for
estimating
the
eﬀective
dose
of
overall
toxicity.
ξ∗(θ0) =
{0,0.686,1;0.396,0.548,0.056}: locally optimal design for estimating the eﬀective dose of pre-
natal death (θT
0 = (a2,b2,γ2)T = (0.13,0.27,3.33), constant correlation), ξu equidistant design
with ﬁve diﬀerent dose levels 0,1/4,1/2,3/4,1 and design ξmm = {0,0.694,1;0.349,0.515, 0.136},
which is standardized maximin optimal for estimating the eﬀective dose of prenatal death with
respect to Ω= [0.05,0.2] × [0.2,0.4] × [2.5,4.5]
a1
0.02
0.02
0.02
0.02
0.1
0.1
0.1
0.1
b1
0.3
0.3
1.1
1.1
0.3
0.3
1.1
1.1
γ1
2.5
4.5
2.5
4.5
2.5
4.5
2.5
4.5
eﬀ(ξ∗(θ0))
0.762
0.977
0.269
0.883
0.815
0.977
0.328
0.899
eﬀ(ξu)
0.669
0.583
0.770
0.611
0.618
0.594
0.644
0.598
eﬀ(ξmm)
0.901
0.986
0.437
0.984
0.935
0.980
0.520
0.995
a1
0.03
0.03
0.03
0.03
0.09
0.09
0.09
0.09
b1
0.4
0.4
0.9
0.9
0.4
0.4
0.9
0.9
γ1
2.7
4.2
2.7
4.2
2.7
4.2
2.7
4.2
eﬀ(ξ∗(θ0))
0.754
0.959
0.443
0.885
0.796
0.965
0.491
0.899
eﬀ(ξu)
0.652
0.589
0.708
0.609
0.622
0.592
0.646
0.599
eﬀ(ξmm)
0.902
0.991
0.646
0.984
0.931
0.991
0.703
0.993
a larger number of support points. The table also contains the minimal eﬃciency of the
standardized maximin optimal design for estimating the eﬀective dose, that is,
min
(θ,u)∈Ωeﬀall(ξ,θ,u),
Table
8. Eﬃciency
for
estimating
the
eﬀective
dose
of
overall
toxicity.
ξ∗(θ0) =
{0,0.686,1;0.396,0.548,0.056}: locally optimal design for estimating the eﬀective dose of pre-
natal death (θT
0 = (a2,b2,γ2)T = (0.13,0.27,3.33), constant correlation), ξu equidistant design
with ﬁve diﬀerent dose levels 0,1/4,1/2,3/4,1 and design ξmm = {0,0.694,1;0.349,0.515, 0.136}
which is standardized maximin optimal for estimating the eﬀective dose of prenatal death with
respect to Ω= [0.05,0.2] × [0.2,0.4] × [2.5,4.5]
a1
0.03
0.03
0.03
0.03
0.09
0.09
0.09
0.09
b1
0.4
0.4
0.9
0.9
0.4
0.4
0.9
0.9
γ1
2.7
4.2
2.7
4.2
2.7
4.2
2.7
4.2
a2
0.05
0.05
0.05
0.05
0.2
0.2
0.2
0.2
b2
0.2
0.2
0.4
0.4
0.2
0.2
0.4
0.4
γ2
2.5
4.5
2.5
4.5
2.5
4.5
2.5
4.5
eﬀ(ξ∗(θ0))
0.570
0.968
0.355
0.821
0.767
0.892
0.532
0.914
eﬀ(ξu)
0.588
0.566
0.594
0.584
0.606
0.574
0.619
0.614
eﬀ(ξmm)
0.730
0.965
0.531
0.942
0.906
0.871
0.743
0.984


## Page 15


138
H. Dette, A. Pepelyshev and W.K. Wong
Table 9. Standardized maximin optimal designs for estimating the eﬀective dose of prenatal
death conditional on the number of implants. The functions m and φ are constant, α = 0.05 and
ξu denotes the equidistant design with ﬁve diﬀerent dose levels 0,1/4,1/2,3/4,1
a2
a2
b2
b2
γ2
γ2
d1
d2
d3
w1
w2
w3
min eﬀ
mineﬀ(ξu)
0.1
0.12
0.25
0.3
3.1
3.5
0
0.681
1
0.387
0.551
0.063
0.976
0.549
0.1
0.15
0.25
0.3
3.1
3.5
0
0.684
1
0.389
0.546
0.065
0.972
0.549
0.1
0.17
0.22
0.3
3
3.7
0
0.696
1
0.390
0.536
0.073
0.930
0.533
0.08
0.18
0.21
0.33
2.6
4
0
0.691
1
0.371
0.524
0.105
0.809
0.514
0.07
0.19
0.2
0.34
2.5
4.1
0
0.690
1
0.366
0.519
0.115
0.757
0.502
Table 10. Standardized maximin eﬃcient optimal design for prenatal death conditional on the
number of implants. The function m is constant, while the correlation function is given by (5.1)
and α = 0.05. ξu denotes the equidistant design with ﬁve diﬀerent dose levels 0,1/4,1/2,3/4,1
and various sets are considered in the standardized maximin optimality criterion (5.3), Ω1(u,u) =
[0.07,0.19] × [0.19,0.34] × [2.5,4.1] × [u,u], Ω2(u,u) = [0.1,0.12] × [0.25,0.3] × [3.1,3.5] × [u,u]
u
u
d1
d2
d3
d4
w1
w2
w3
w4
min eﬀ(ξ∗)
mineﬀ(ξu)
0
1
0
0.469
0.721
1
0.269
0.258
0.400
0.073
0.654
0.412
Ω1(u,u)
0
2
0
0.460
0.722
1
0.232
0.282
0.417
0.069
0.640
0.392
1
2
0
0.545
0.665
1
0.239
0.110
0.535
0.117
0.655
0.392
0
1
0
0.653
1
0.343
0.599
0.058
0.896
0.469
Ω2(u,u)
0
2
0
0.649
1
0.327
0.615
0.057
0.873
0.449
1
2
0
0.637
1
0.254
0.700
0.046
0.946
0.449
and the minimal eﬃciencies of an equidistant design with ﬁve diﬀerent dose levels. Note
that the standardized maximin optimal designs yield reasonable eﬃciencies over the full
set Ωand that the minimal eﬃciency of the uniform design over this set is substan-
tially smaller. In Table 10 we consider the case where the correlation can be modeled by
the function (5.1). We observe that the standardized maximin optimal designs are sup-
ported at three or four points and, compared to Table 9, the eﬃciencies are smaller. This
is intuitively clear because we have incorporated more robustness with respect to the
assumption of a constant correlation in the construction of eﬃcient designs for estimat-
ing the eﬀective dose. Again the equidistant design yields substantially smaller minimal
eﬃciencies compared to the standardized maximin optimal design.
6. Eﬃciency of standard designs and concluding
remarks
It is interesting to evaluate the eﬃciencies of commonly used designs in developmental
toxicity studies. One such class is the set of uniform designs. These designs are equally


## Page 16


Optimal designs for dose-ﬁnding experiments
139
spread out in the dose interval of interest and an equal number of animals is allocated
to each dose. As such, they are intuitive and easy to implement. Krewski, Smythe and
Fung (2002) provided an overview of experimental designs for 11 developmental toxicity
studies conducted under the U.S. National Toxicology Program. In their Table 1, they
listed the doses employed in these studies that involved either rabbits, rats or mice. The
designs usually have a roughly equal number of animals at each dose and some of their
dose levels, after scaling to our protocol interval [0,1], are listed in our Tables 11 and 12.
Following Krewski, Smythe and Fung, we call these “standard” designs.
Tables 11 and 12 display the eﬃciencies of “standard” designs for estimating the pre-
natal death rates and the overall toxicity rate. We observe that the standard design can
perform poorly when model parameters are misspeciﬁed. For instance, the eﬃciencies
of the standard design listed in the ﬁrst row can be less than 30% for estimating the
prenatal death rate and the overall toxicity rate. Some standard designs have eﬃciencies
as low as 0.22 for estimating the prenatal death rate. Interestingly, the uniform design
with ﬁve doses has at least 50% for all cases shown in the tables. The second parts of the
two tables show the eﬃciencies of a uniform design with three support points (note that
the local optimal design usually has two or three support points). One observes that this
design yields very low eﬃciencies and cannot be recommended. In general, it is advisable
that the researcher assess the eﬃciencies of a design under diﬀerent optimality criteria
before its implementation.
In practice, there are usually several objectives in the study and these objectives may
not be of equal interest to the researcher. For instance, the researcher may be interested
in designing a study whose primary aim is to estimate the prenatal death rate, secondary
Table 11. Eﬃciency of “standard” designs for estimating EDα for prenatal death with diﬀerent
values of parameters, φ(d) ≡constant
a2
0.13
0.05
0.13
0.13
0.05
0.13
b2
0.27
0.27
0.15
0.27
0.15
0.27
d1
d2
d3
d4
d5
γ2
3.3
3.3
3.3
2
2
1
0
0.25
0.5
1
0.28
0.31
0.23
0.53
0.46
0.75
0
0.33
0.67
0.83
1
0.61
0.55
0.57
0.53
0.48
0.52
0
0.25
0.5
0.75
1
0.56
0.54
0.51
0.57
0.51
0.62
0
0.3
0.5
0.7
1
0.54
0.54
0.46
0.62
0.54
0.65
0
0.17
0.33
0.67
1
0.49
0.47
0.44
0.50
0.45
0.63
0
0.05
0.15
0.5
1
0.28
0.31
0.24
0.49
0.43
0.51
0
0.125
0.25
0.5
1
0.26
0.29
0.22
0.46
0.40
0.64
0
0.1
0.2
0.5
1
0.27
0.30
0.23
0.46
0.40
0.58
0
0.3
1
0.04
0.05
0.03
0.29
0.27
0.73
0
0.4
1
0.14
0.18
0.11
0.52
0.45
0.71
0
0.5
1
0.34
0.39
0.27
0.69
0.60
0.58
0
0.6
1
0.58
0.61
0.47
0.73
0.64
0.40
0
0.7
1
0.74
0.69
0.64
0.59
0.53
0.23


## Page 17


140
H. Dette, A. Pepelyshev and W.K. Wong
Table 12. Eﬃciency of “standard” designs for estimating EDα for overall toxicity with diﬀerent
values of parameters in the Weibull model with φ(d) ≡constant
a1
0.06
0.06
0.06
0.06
0.06
0.06
0.02
b1
0.7
0.7
0.7
0.7
0.7
0.2
0.7
γ1
3.37
3.37
3.37
3.37
1
3.37
3.37
a2
0.13
0.05
0.13
0.13
0.13
0.13
0.13
b2
0.3
0.3
0.1
0.3
0.3
0.3
0.3
d1
d2
d3
d4
d5
γ2
3.33
3.33
3.33
1
3.33
3.33
3.33
0
0.25
0.5
1
0.36
0.39
0.34
0.78
0.69
0.29
0.37
0
0.33
0.67
0.83
1
0.61
0.56
0.64
0.53
0.40
0.63
0.63
0
0.25
0.5
0.75
1
0.62
0.59
0.64
0.64
0.55
0.59
0.64
0
0.3
0.5
0.7
1
0.63
0.62
0.64
0.66
0.52
0.57
0.65
0
0.17
0.33
0.67
1
0.54
0.51
0.55
0.65
0.69
0.52
0.55
0
0.05
0.15
0.5
1
0.35
0.38
0.34
0.53
0.59
0.30
0.36
0
0.125
0.25
0.5
1
0.33
0.35
0.31
0.67
0.76
0.27
0.34
0
0.1
0.2
0.5
1
0.34
0.36
0.33
0.61
0.72
0.29
0.35
0
0.3
1
0.05
0.06
0.05
0.75
0.67
0.04
0.06
0
0.4
1
0.19
0.23
0.18
0.72
0.51
0.15
0.21
0
0.5
1
0.45
0.50
0.42
0.58
0.34
0.36
0.47
0
0.6
1
0.71
0.73
0.70
0.39
0.20
0.63
0.72
0
0.7
1
0.78
0.72
0.79
0.22
0.11
0.78
0.76
aim is to estimate the malformation rate and tertiary aim is to estimate the overall toxic-
ity rate as accurately as possible. To incorporate the multiple objectives in the study, one
may follow the strategy laid out in Cook and Wong (1994) to ﬁnd an optimal design that
provides user-speciﬁed eﬃciency for each objective. Clearly, the optimal design sought
should provide higher eﬃciencies for more important objectives and user-speciﬁed eﬃ-
ciencies reasonable enough so that the optimal design exists. For space consideration, we
do not provide multiple-objective optimal designs for simultaneously estimating the ef-
fective dose for prenatal death rate, malformation rate and overall toxicity rate, but note
that the key idea for ﬁnding such a design is to ﬁrst formulate each objective as a convex
function of the design information matrix and then combine all the convex objectives into
a single convex functional using a convex combination. As described in Cook and Wong
(1994), each set of weights used in the convex combination can be judiciously chosen to
satisfy the eﬃciency requirement for each objective. In the case of a two-objective design
problem, the weights and the dual-objective optimal design can be determined graphi-
cally via eﬃciency plots. Wong (1999) provided several illustrative applications of such
ideas to construct multiple-objective optimal designs in several biomedical problems.
One may be rightly concerned that the optimal designs are dependent on the para-
metric models. This dependence is inescapable but as we have advocated all along, the
user must check robustness properties of optimal designs to all assumptions before the
design is implemented. We focused on the simpler situation when we were concerned
about misspeciﬁcation of initial values, but if there is concern about other aspects in the


## Page 18


Optimal designs for dose-ﬁnding experiments
141
model assumptions, a similar strategy can be applied. For instance, one may question the
validity of the Weibull models to describe the malformation and prenatal death rates.
If scientiﬁc opinion suggests alternative models may be more appropriate, one can then
construct optimal designs for diﬀerent models and compare their eﬃciencies under the
competing models. The hope is that there is a design that remains eﬃcient under all
models on which experts may agree.
Here is a short illustration of the situation just discussed: Assume, as before, that both
the malformation and prenatal death rates have the same form and can be described using
two plausible models:
π(2)
2 (d) = 1 −
a2
1 + b2dγ2
and
π(3)
2 (d) = 1 −
a2
1 + e−b2+γ2d .
Suppose the sets of initial values are θ(2)
2
= (0.88,0.25,2.8), θ(3)
2
= (0.91,4.3,3.5), θ(2)
1
=
(0.94,1.3,5.1) and θ(3)
1
= (0.98,3.5,3.2). We recall that θ(1)
1
= (0.06,0.7,3.37) and θ(1)
2
=
(0.13,0.27,3.33). Here the superscripts denote the three diﬀerent models used to describe
the probability rates.
Table 13 lists the locally optimal designs for α = 0.05 and their eﬃciencies under dif-
ferent assumptions on the probability models. The robustness properties of each optimal
design under each set of probability models can be compared. For this setup, the eﬃ-
ciency results are quite reassuring because the smallest eﬃciency in the table is at least
0.76. Of course, diﬀerent assumptions on the sets of initial values may not yield the same
conclusions.
In summary, our proposed design strategy is quite general and possess several advan-
tages over existing methods. Unlike uniform designs, our approach is based ﬁrmly on
statistical principles and the proposed maximin optimal design provides good protection
against misspeciﬁcation in the initial values of the model parameters. The optimal design
allows prior information to be included in its construction and, if required, can also incor-
porate multiple objectives with possibly unequal interests. Consequently, the proposed
optimal design is able to meet the practical needs of the researcher more adequately than
current designs.
Appendix: Proofs
Proof of Theorem 1. From (3.1), the information matrix for a design ξ can be repre-
sented as
M(ξ,θ) =
k
X
i=1
wif(di)f T (di),


## Page 19


142
H. Dette, A. Pepelyshev and W.K. Wong
Table 13. Various locally optimal designs (leftpart) and their eﬃciencies under diﬀerent prob-
ability models for estimating of prenatal death (ﬁrst three rows), malformation rate (middle
three rows) and overall toxicity (last three rows)
Model
x1
x2
x3
w1
w2
w3
ξ(1)
ξ(2)
ξ(3)
weibull
0
0.686
1
0.396
0.548
0.056
1.000
0.910
0.869
model 2
0
0.624
1
0.417
0.546
0.037
0.911
1.000
0.968
model 3
0
0.630
1
0.354
0.561
0.086
0.853
0.940
1.000
weibull
0
0.616
1
0.297
0.602
0.101
1.000
0.954
0.832
model 2
0
0.662
1
0.284
0.592
0.123
0.918
1.000
0.503
model 3
0
0.535
1
0.290
0.610
0.100
0.882
0.768
1.000
weibull
0
0.654
1
0.323
0.550
0.127
1.000
0.885
0.726
model 2
0
0.581
1
0.357
0.521
0.121
0.825
1.000
0.910
model 3
0
0.544
1
0.297
0.564
0.138
0.761
0.942
1.000
where the vector f is deﬁned by
f(d) =
D(d)
p
m(1 + (m −1)φ(d))π2(d)(1 −π2(d))
=
s
(1 −π2(d))
m(d)(1 + (m(d) −1)φ(d))π2(d)


1
dγ2
b2dγ2 ln(d)

.
We now apply Elfving’s theorem (see Elfving (1952)), which gives a geometric charac-
terization of the optimal design. More precisely, from this result it follows that a design
ξ = {di,wi}k
i=1 is locally optimal if and only if there exist numbers ε1,...,εk ∈{−1,1}
such that for some ν ∈R the point
νP = ν

0,1/b2, 1
γ2
ln

−ln(1 −α)
b2
T
=
k
X
j=1
εjwjf(dj)
(A.1)
is a boundary point of the Elfving set
R = conv({εf(d) | d ∈[0,1],ε ∈{−1,1}}).
(A.2)
A typical picture of this set is presented in Figure A.1 for the case of constant functions
φ and m. We note that the curve
X = {f(d), d ∈[0,1]}
is contained in subspace {x = (x1,x2,x3)T ∈R3|x1 > 0} and the set
{(1,dγ2,b2dγ2 ln(d))|d ∈[0,1]}


## Page 20


Optimal designs for dose-ﬁnding experiments
143
Figure A.1. The Elfving set deﬁned in (A.2) for the parameters a = 0.133, b = 0.272, γ = 3.33.
The points f(d1), −f(d2) and f(d3) are denoted by A, C and B, respectively, while the point
νP is deﬁned in (A.1).
deﬁnes a U-shaped curve. From the monotonicity assumption for the function (3.3), it
follows that the curve X is also U-shaped (see also Figure A.1). We denote the end-points
of this curve by A and B and recall that the ﬁrst coordinate of the vector P is equal to
0 and that ν is the scaling constant such that νP touches the boundary of the Elfving
set R. Note that in the case α →0 we have that
P ≈c


0
0
1


for some constant c and, consequently, the vector νP touches the boundary at the plane
E spanned by the points A, B and C, where A and B correspond to the doses 0 and
1, respectively, and −C corresponds to a third dose, say d∗∈(0,1). Consequently, the
locally optimal design is a three-point design with support points 0, 1 and d∗, if α is
suﬃciently small. In the case where α →1, the situation is exactly the same and the
locally optimal design is also supported at three points, including the boundary points.
From the geometry of the Elfving set R we see that there is also direction P, where the
intersection with the Elfving set can be represented by two points of the curves X and
−X . In particular, this situation occurs if α ≈1 −e−b. In this case we have
P ≈c


0
1
0




## Page 21


144
H. Dette, A. Pepelyshev and W.K. Wong
for some constant c and the locally optimal design is supported by a two-point design.
Moreover, if α moves from 0 to 1, it follows from the geometry of the Elfving set that
the situation is changing continuously, which proves the assertion of the theorem.
□
Proof of Theorem 2. Multiplying the last coordinate of the vector equation (A.1) by
γ2 yields
νP = ν



0
1/b2
ln

−ln(1 −α)
b2




=
X
i
εiwi
s
(1 −π2(di))
m(1 + (m −1)φ)π2(di)


1
dγ2
i
b2dγ2
i ln(dγ2
i )


(A.3)
for the boundary point νP ∈R. If {d∗
i (1);w∗
i } denotes an optimal design for the param-
eter θ = (a2,b2,1), it follows that equation (A.3) holds for this design with γ2 = 1. Now
it is easy to see that (A.3) is also true for the design {(d∗
i (1))1/γ2;w∗
i } for the parameter
θ = (a2,b2,γ2), where γ2 > 0 is arbitrary. This proves the ﬁrst part of the theorem. The
second part follows by similar arguments, which are omitted by the sake of brevity.
□
Proof of Theorem 3. Part (a) of the Theorem follows directly from the geometry of the
Elfving set. If the locally optimal design is supported at three points, the corresponding
point νP touches the Elfving set in the plane spanned by the points A, B and C, which
does not depend on the value of α. For a proof of part (b) we note that, according to
Elfvings theorem, a locally optimal design of the form {0,d2,w1,w2} must satisfy the
equation
ν



0
1/b2
ln

−ln(1 −α)
b2



= εw1g(0)


1
0
0

−εw2g(d2)


1
dγ2
2
b2dγ2
2 ln(dγ2
2 )

,
where the function g is deﬁned by
g(d) =
s
(1 −π2(d))
m(d)(1 + (m(d) −1)φ(d))π2(d) .
It is easy to see that this equation yields
ν


1/b2
ln

−ln(1 −α)
b2



= −εw2
s
(1 −π2(d2))
m(d2)(1 + (m(d2) −1)φ(d2))π2(d2)

dγ2
2
b2dγ2
2 ln(dγ2
2 )

,


## Page 22


Optimal designs for dose-ﬁnding experiments
145
which simpliﬁes to the equation
ν

1
ln(EDγ2
α )

= −εw2
s
(1 −π2(d2))
m(d2)(1 + (m(d2) −1)φ(d2))π2(d2)b2dγ2
2

1
ln(dγ2
2 )

.
It follows that d2 = EDα. Since w1 = 1 −w2 from the equality for the ﬁrst coordinate,
we have that w2 = g(0)/(g(0) + g(EDα)).
□
Acknowledgements
The support of the Deutsche Forschungsgemeinschaft (SFB 475, “Komplexit¨atsreduktion
in multivariaten Datenstrukturen”) is gratefully acknowledged. The work of H. Dette and
W.K. Wong was supported in part by NIH Grant award IR01GM072876. Additionally,
Wong was supported by NIH Grant P30 CA16042-33.
References
Bowman, D., Chen, J. and George, E. (1995). Estimating variance functions in developmental
toxicity studies. Biometrics 51 1523–1528. MR1349907
Braess, D. and Dette, H. (2007). On the number of support points of maximin and Bayesian
optimal designs. Ann. Statist. 35 772–792. MR2336868
Catalano, P.J., Scharfstein, D.O., Ryan, L., Kimmel, C.A. and Kimmel, G.L. (1993). Statisti-
cal model for fetal death, fetal weight, and malformation in developmental toxicity studies.
Teratology 47 281–290.
Chernoﬀ, H. (1953). Local optimal designs for estimating parameters. Ann. Math. Statist. 24
586–602. MR0058932
Cook, R.D. and Wong, W.K. (1994). On the equivalence of constrained and compound optimal
designs. J. Amer. Statist. Assoc. 89 687–692. MR1294092
Dette, H. (1997). Designing experiments with respect to standardized optimality criteria. J.
Roy. Statist. Soc. Ser. B 59 97–110. MR1436556
Elfving, G. (1952). Optimum allocation in linear regression theory. Ann. Math. Statist. 23 255–
262. MR0047998
Giles, I.J. (2006). Animal experiments under ﬁre for poor design. Nature 444 981–981.
Klaassen, C.D. (2001). Casarett and Doull’s Toxicology: The Basic Science of Poisons, 6th ed.
New York: McGraw-Hill Publishing.
Krewski, D. and Zhu, Y. (1995). A simple data transformation for estimating benchmark doses
in developmental toxicity experiments. Risk Analysis 15 29–39.
Krewski, D., Smythe, R. and Fung, K.Y. (2002). Optimal designs for estimating the eﬀective
dose in development toxicity experiments. Risk Analysis 22 1195–1205.
L¨auter, E. (1974). Experimental design in a class of models. Mathematische Operationsforschung
und Statistik 5 379–398. MR0440812
Lee, G.S., Liao, X., Cantor, R. and Collins, M.D. (2006). Interactive eﬀects of Cadmium and
All-Trans-Retinoic acid on the induction of forelimb ectrodactyly in C57BL/6 mice.
Birth
Defects Research (Part A): Clinical and Molecular Teratology 76 19–28.


## Page 23


146
H. Dette, A. Pepelyshev and W.K. Wong
Moerbeek, M., Piersma, A.H. and Slob, W. (2004). A comparison of three methods for calculating
conﬁdence intervals for the benchmark dose. Risk Analysis 24 31–40.
M¨uller, C.H. (1995). Maximin eﬃcient designs for estimating nonlinear aspects in linear models.
J. Statist. Plann. Inference 44 117–132. MR1323074
Al-Saidy, O.M., Piegorsch, W.W., West, R.W. and Nitcheva, D.K. (2003). Conﬁdence bands for
low-dose risk estimation with quantal response data. Biometrics 59 1056–1062. MR2025130
Pukelsheim, F. (1993). Optimal Design of Experiments. New York: Wiley. MR1211416
Pukelsheim, F. and Rieder, S. (1992). Eﬃcient rounding of approximate design. Biometrika 79
763–770. MR1209476
Ryan, L. (1992). Quantitative risk assessment for developmental toxicity. Biometrics 48 163–
174.
Silvey, S.D. (1980). Optimal Design. London: Chapman and Hall. MR0606742
Slob, W., Moerbeek, M., Rauniomaa, E. and Piersma, A.H. (2005). A statistical evaluation of
toxicity study designs for the estimation of the benchmark dose in continuous endpoints.
Toxicological Sciences 84 167–185.
Van der Vaart, A. (1998). Asymptotic Statistics. Cambridge Univ. Press. MR1652247
Wong, W.K. (1999). Recent advances in constrained optimal design strategies. Statist. Neer-
landica 53 257–276.
Woutersen, R.A., Jonker, D., Stevension, H., Biesebeek, J.D. and Slob, W. (2001). The Bench-
mark approach applied to a 28-day toxicity study with Rhodorsil Silane in rats: The impact
of increasing the number of dose groups. Food and Chemical Toxicology 39 697–707.
Zhu, Y., Krewski, D. and Ross, W.H. (1994). Dose-response models for correlated multinomial
data from developmental toxicity studies. Appl. Statist. 43 583–598.
Received January 2008 and revised May 2008

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]
