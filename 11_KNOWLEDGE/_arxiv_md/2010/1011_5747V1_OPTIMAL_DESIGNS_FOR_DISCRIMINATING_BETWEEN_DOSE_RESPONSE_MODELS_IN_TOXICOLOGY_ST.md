---
tags: [knowledge, _arxiv_md, 2010, note, reference, arxiv]
---
arxiv_id: 1011.5747v1
source: arxiv
rscf-state: source-claim
canon-group: reference

# 1011.5747v1_Optimal_designs_for_discriminating_between_dose-response_models_in_toxicology_st

> Source: 1011.5747v1_Optimal_designs_for_discriminating_between_dose-response_models_in_toxicology_st.pdf

> Pages: 14

---


## Page 1


arXiv:1011.5747v1  [math.ST]  26 Nov 2010
Bernoulli 16(4), 2010, 1164–1176
DOI: 10.3150/10-BEJ257
Optimal designs for discriminating between
dose-response models in toxicology studies
HOLGER DETTE1, ANDREY PEPELYSHEV2,*, PITER SHPILEV2,** and
WENG KEE WONG3
1Faculty of Mathematics, Ruhr-Universit¨at Bochum, Universitatsstrasse 150, 44780 Bochum,
Germany. E-mail: holger.dette@ruhr-uni-bochum.de
2Department of Mathematics, St. Petersburg State University, Universitetskij pr. 28, St. Peters-
burg, 198504, Russia. E-mails: *andrey@ap7236.spb.edu; **pitsh@front.ru
3Department of Biostatistics, University of California at Los Angeles, 10833 Le Conte Avenue,
Los Angeles, CA 90095, USA. E-mail: wkwong@ucla.edu
We consider design issues for toxicology studies when we have a continuous response and the
true mean response is only known to be a member of a class of nested models. This class
of non-linear models was proposed by toxicologists who were concerned only with estimation
problems. We develop robust and eﬃcient designs for model discrimination and for estimating
parameters in the selected model at the same time. In particular, we propose designs that
maximize the minimum of D- or D1-eﬃciencies over all models in the given class. We show
that our optimal designs are eﬃcient for determining an appropriate model from the postulated
class, quite eﬃcient for estimating model parameters in the identiﬁed model and also robust
with respect to model misspeciﬁcation. To facilitate the use of optimal design ideas in practice,
we have also constructed a website that freely enables practitioners to generate a variety of
optimal designs for a range of models and also enables them to evaluate the eﬃciency of any
design.
Keywords: continuous design; locally optimal design; maximin optimal design; model
discrimination; robust design
1. Introduction
This paper addresses design issues for toxicology studies when the primary outcome is
continuous and it is not known a priori which model is an appropriate one to use. Such
design problems are common; see, for example, [1–3, 11, 12]. In this situation, we may
consider a class of plausible models within which we believe lies an adequate model for
ﬁtting the data. The issues of interest are how to design the study to choose the most
appropriate model from within the postulated class of models and, at the same time, be
able to estimate the parameters of the selected model eﬃciently. Our design decisions
This is an electronic reprint of the original article published by the ISI/BS in Bernoulli,
2010, Vol. 16, No. 4, 1164–1176. This reprint diﬀers from the original in pagination and
typographic detail.
1350-7265
c⃝
2010 ISI/BS


## Page 2


Optimal designs for discriminating between dose-response models
1165
include how to select the number of dose levels to observe the continuous outcome, where
these levels are and how many repeated observations to take at each of these levels. This
work assumes, for the sake of simplicity, that there is only one independent variable, the
dose level and only non-sequential designs are considered.
When we have competing models, a design should be able to discriminate among these
models and select the most appropriate ones. Dette [5–7] found optimal discrimination
designs for polynomial regression models, and Dette and Roeder [9] and Dette and Haller
[10] found optimal discrimination designs for trigonometric and Fourier regression models,
respectively. T -optimal designs are usually used to discriminate between homoscedastic
models with normal errors [1–3, 12]. For discriminating non-linear models, only numerical
results are possible; Lopez-Fidalgo et al. [16] investigated optimal designs maximizing a
weighted average of two T -criterion functions and Lopez-Fidalgo et al. [17] constructed
T -optimal designs for Michaelis–Menten-like models. When the design problem involves
model discrimination and another optimality criterion, the problem is more complicated.
Hill et al. [12] was among the ﬁrst to consider studies with two goals: model discrimination
and estimation of model parameters. Dette et al. [8] gave a concrete example where they
wanted to discriminate between the Michaelis–Menten-model and the Emax model and
estimate model parameters in an enzyme-kinetic study. A key reason for there having
been so little research into such design problems for non-linear models is that there are
serious technical diﬃculties.
The motivation for this work comes from recent proposals by Piersma et al. [23], Slob
[22], Slob and Pieters [24]) and Moerbeek et al. [18] to use the same class of models to
study a continuous outcome in toxicological studies. Their interest was only in estimation
problems and so they did not consider design issues. Our purpose here is to ﬁnd an
optimal design for identifying an appropriate model within the class of models and, at
the same time, provide reliable parameter estimates in the selected model. To do this, we
ﬁrst ﬁnd locally optimal designs [4]. These designs are the easiest to construct, but they
can be sensitive to nominal values and the model speciﬁcation. To overcome the risk of
selecting an inappropriate model, we propose maximin optimal designs that appear to be
robust to misspeciﬁcations in the model. These maximin optimal designs maximize the
minimum eﬃciency, regardless of which model in the class of models is the appropriate
one. As such, these optimal designs provide some global protection against selecting the
wrong model from the postulated class of models. As we will show, the designs also seem
quite robust to misspeciﬁcation in the nominal values of the model parameters.
In Section 2, we present some background and the proposed class of models. We de-
scribe relationships between models in the class and provide locally optimal designs for
discriminating between plausible models. We also show how optimal designs constructed
for one set of design parameters can be used to deduce the optimal design under another
set of design parameters. In Section 3, we construct maximin optimal designs for various
subclasses of plausible models and in Section 4, we show that maximin optimal designs
are robust to misspeciﬁcation of models in the postulated class. We oﬀer a conclusion in
Section 5 and an Appendix containing technical justiﬁcations of our results.


## Page 3


1166
Dette, Pepelyshev, Shpilev and Wong
2. A class of dose-response models
In a general non-linear regression model, the mean response of the outcome Y is given by
E[Y |t] = η(t,θ), where we assume the unknown parameter θ is m-dimensional. The class
of models proposed by toxicologists assumes all errors are independent and normally
distributed, and η(t,θ) has one of the following forms deﬁned on a user-selected interval
[0,T ]:
η(t,θ) = a;
m = 1,
θ = a > 0,
(2.1)
η(t,θ) = ae−bt;
m = 2,
θ = (a,b)T ,a > 0,b > 0,
(2.2)
η(t,θ) = ae−btd;
m = 3,
θ = (a,b,d)T ,a,b > 0,d ≥1,
(2.3)
η(t,θ) = a(c −(c −1)e−bt);
m = 3,
θ = (a,b,c)T,a,b > 0,c ∈[0,1],
(2.4)
η(t,θ) = a(c −(c −1)e−btd);
m = 4,
θ = (a,b,c,d)T,a,b > 0,c ∈[0,1],d ≥1.
(2.5)
The rationale for this class of models was given for dose-response relationships that
cannot be derived from biological mechanisms. The models are nested, in the sense that
the models with a smaller number of parameters can be obtained from another model
by setting speciﬁc values for the parameters. For instance, model (2.5) is an extension of
the models (2.4) and (2.3), model (2.3) is an extension of model (2.2) and model (2.4) is
an extension of the models (2.2) and (2.1). The hierarchy of the models is illustrated in
the following diagram.
(2.5)
d=1
=⇒(2.4)
c=1
=⇒(2.1)
⇓c = 0
⇓c = 0
(2.3)
d=1
=⇒(2.2)
We note that when b = 0, all of the models (2.2)–(2.5) reduce to the constant model
(2.1), this relation not being shown in the diagram.
Following [15], we consider only continuous designs. A continuous design is simply a
probability measure ξ with a ﬁnite number of support points, say t1,...,tn ∈[0,T ], and
corresponding weights ω1,...,ωn with ωi > 0 and Pn
i=1 ωi = 1. If we ﬁx the number of
observations N in advance, either by cost or time considerations, then, roughly, ni = Nωi
observations are taken at point ti, with Pn
i=1 ni = N. For many problems, continuous
designs are easier to describe and study analytically than exact designs.
Jennrich [13] showed that under regularity assumptions, the asymptotic covariance
matrix of the standardized least-squares estimator
p
N/σ2 ˆθ for the parameter θ in the
general non-linear model is given by the matrix M −1(ξ,θ), where
M(ξ,θ) =
Z T
0
f(t,θ)f T(t,θ)dξ(t)


## Page 4


Optimal designs for discriminating between dose-response models
1167
is the information matrix using design ξ and
f(t,θ) = ∂η(t,θ)
∂θ
= (f1(t,θ),...,fm(t,θ))T
(2.6)
is the vector of partial derivatives of the conditional expectation η(t,θ) with respect to
the parameter θ. Additionally, we consider only designs with a non-singular information
matrix. A suﬃcient condition for this property to hold is that the design has k support
points, where k is greater than or equal to the number of parameters in the model.
A locally optimal design maximizes a function of the information matrix M (ξ,θ) using
nominal values of θ [4]. There are several optimality criteria for estimating purposes and
for discriminating between models [1, 20]. We are interested in ﬁnding eﬃcient designs
for model selection among models deﬁned by (2.1)–(2.5) that also provide good and
robust estimates for the parameters in the selected model. Accordingly, we construct an
optimal design for pairs of competing models that fulﬁlls at least two of three following
requirements:
(1) The design should be able to test the hypotheses for discriminating between two
selected rival models. For example, the hypothesis for discriminating between the
models (2.4) and (2.2) is given by
H0 :c = 0
vs.
H1 :c ∈(0,1].
Van der Vaart [25] described properties of test statistics for testing such hypothe-
ses.
(2) The design should be able to eﬃciently estimate the parameters in the corre-
sponding pair of regression models and for all models which are submodels of the
model with the larger number of parameters. For example, for model (2.4), the
corresponding submodels are given by (2.2) and (2.3).
(3) The design should also be eﬃcient for discriminating between the diﬀerent submod-
els of the model with the larger number of parameters (which may also be nested).
For example, the optimal design for discriminating between the models (2.2) and
(2.4) should also be eﬃcient for discriminating between the models (2.1)/(2.4) and
(2.1)/(2.2).
To make these ideas concrete, consider the em-optimality criterion, where em =
(0,...,0,1)T and m is the larger of the number of parameters in the two models un-
der consideration. For ﬁxed θ, a locally em-optimal design minimizes
eT
mM −1(ξ,θ)em = det f
M(ξ,θ)
detM(ξ,θ),
(2.7)
where the matrix M(ξ,θ) is the information matrix in the model with the larger number
of parameters and the matrix f
M(ξ,θ) is obtained from M(ξ,θ) by deleting the mth row
and the mth column. A locally em-optimal design is just a special case of a c-optimal
design used for estimating cT θ, where the vector c is user-speciﬁed.


## Page 5


1168
Dette, Pepelyshev, Shpilev and Wong
The expression (2.7) is proportional to the asymptotic variance of the least-squares
estimate of eT
mθ, which is relevant for model discrimination. In particular, minimizing
the asymptotic variance (2.7) provides a design with maximal power for testing a simple
hypothesis for eT
mθ. For example, if we want to discriminate between models (2.4) and
(2.2), we have m = 3 and eT
mθ = (0,0,1)(a,b,c)T = c, and the cases c ̸= 0 and c = 0 give
the two rival models (2.4) and (2.2), respectively. Consequently, a design that minimizes
the ratio in (2.7) is optimal for discriminating between the two models.
We next construct locally em-optimal designs for discriminating between pairs of mod-
els (2.3)–(2.5).
2.1. Optimal discriminating designs for the models (2.2) and
(2.3)
For model (2.3) with θ = (a,b,d)T , the vector of partial derivatives in (2.6) is given by
f(t,θ) = f(t,a,b,d) = (e−btd,−atde−btd,−abtd ln(t)e−btd)T .
(2.8)
Our ﬁrst result establishes basic properties of locally e3-optimal designs for model (2.3).
Lemma 2.1. The locally e3-optimal design in model (2.3) does not depend on the pa-
rameter a. Moreover, if ti(b,d,T ) is a support point of a locally e3-optimal design on the
interval [0,T ] with corresponding weight ωi(b,d,T ), then for any r > 0 and d > 0,
ti(b,d,T 1/d) = ti(b,1,T )1/d,
ωi(b,d,T 1/d) = ωi(b,1,T ),
(2.9)
ti(rb,1,T ) = 1
r ti(b,1,rT ),
ωi(rb,1,T ) = ωi(b,1,rT ).
To ﬁnd an eﬃcient design for discriminating between models (2.2) and (2.3), we assume
that the initial parameter value of d is unity. From the lemma, it is enough to calculate
locally e3-optimal designs on a ﬁxed design space for various values of b after the remain-
ing parameters a and d are ﬁxed. Locally optimal designs on a diﬀerent design space
or having other values of the parameters can then be calculated using the relationships
given in the lemma.
To characterize locally e3-optimal designs, we recall that a set of functions h1,...,hk :I →
R is a Chebyshev system on the interval I if there exists an ε ∈{−1,1} such that the
inequality
ε ·

h1(t1)
...
h1(tk)
...
...
...
hk(t1)
...
hk(tk)

> 0
holds for all t1,...,tk ∈I with t1 < t2 < ··· < tk. From Karlin and Studden [14], Theorem
II 10.2, if {h1,...,hk} is a Chebyshev system, then there exists a unique function, say
Pk
i=1 c∗
i hi(t) = c∗T h(t), where h = (h1,...,hk)T , with the following properties:


## Page 6


Optimal designs for discriminating between dose-response models
1169
Table 1. Locally e3-optimal designs for models (2.3) and (2.4) on the design space [0,1] for
various values of the parameter b
b
Model (2.3)
Model (2.4)
t1
t2
t3
ω1
ω2
ω3
t1
t2
t3
ω1
ω2
ω3
0.1
0
0.355
1
0.311
0.500
0.189
0
0.492
1
0.242
0.500
0.259
0.5
0
0.305
1
0.294
0.493
0.213
0
0.458
1
0.212
0.492
0.296
1.0
0
0.251
1
0.276
0.473
0.251
0
0.418
1
0.180
0.469
0.351
2.0
0
0.167
1
0.241
0.403
0.356
0
0.343
1
0.127
0.384
0.490
3.0
0
0.112
0.751
0.232
0.381
0.387
0
0.281
1
0.083
0.267
0.650
(i) |c∗T h(t)| ≤1 ∀t ∈I;
(ii) there exist k points, t∗
1 < ··· < t∗
k, such that c∗T h(t∗
i ) = (−1)i,i = 1,...,k.
The function c∗T h(t) alternates at the points t∗
1,...,t∗
k and is called the Chebyshev poly-
nomial. The points t∗
1,...,t∗
k are called Chebyshev points and they are unique when
1 ∈span{h1,...,hk}, k ≥1 and I is a compact interval. In this case, we have t∗
1 = mint∈I t,
t∗
k = maxt∈I t. The following result characterizes the locally e3-optimal design.
Theorem 2.1. The components of the vector deﬁned by (2.8) form a Chebyshev sys-
tem on the interval [0,T ]. The locally e3-optimal design for model (2.3) is unique and
is supported at the three uniquely determined Chebyshev points, say t∗
1 < t∗
2 < t∗
3. The
corresponding weights ω∗
1, ω∗
2, ω∗
3 can be obtained explicitly as
ω∗= (ω∗
1,ω∗
2,ω∗
3)T =
JF −1e3
13JF −1e3
,
(2.10)
where the matrices F and J are deﬁned by F = (f(t∗
1,θ),f(t∗
2,θ),f(t∗
3,θ)), J = diag(1,
−1,1), respectively, and 13 = (1,1,1)T .
Table 1 displays selected locally e3-optimal designs for model (2.3).
2.2. Optimal discriminating designs for the models (2.3) and
(2.4), (2.1) and (2.4)
For model (2.4), we have θ = (a,b,c)T and when c = 0 or c = 1, model (2.4) reduces to
model (2.3) or (2.1), respectively. The e3-optimal design is optimal for discriminating
between models (2.3) and (2.4) and for discriminating between models (2.1) and (2.4).
The vector of partial derivatives in (2.6) is
f(t,θ) = f(t,a,b,c) = (c −(c −1)e−bt,a(c −1)te−bt,a(1 −e−bt))T
and its components form a Chebyshev system on [0,T ]. The locally e3-optimal design
is described in Theorem 2.2 and we observe that it does not depend on the parameter


## Page 7


1170
Dette, Pepelyshev, Shpilev and Wong
a. For other positive values of b and T , the support points ti(b,T ) and corresponding
weights ωi(b,T ) of the optimal design are found from ti(rb,T ) = 1
rti(b,rT ) and ωi(rb,T ) =
ωi(b,rT ).
Theorem 2.2. Let 0 ≤c < 1. The locally e3-optimal design for model (2.4) on [0,T ] is
unique and has three points at t∗
1 = 0, t∗
3 = T and (middle point)
t∗
2 = 1
b + t∗
1e−bt∗
1 −t∗
3e−bt∗
3
e−bt∗
1 −e−bt∗
3
,
and the corresponding weights ω∗
1, ω∗
2 and ω∗
3 can be obtained explicitly from formula
(2.10).
2.3. Optimal discrimination designs for the models (2.4) and
(2.5), (2.1) and (2.5), (2.3) and (2.5)
Model (2.5) with θ = (a,b,c,d)T reduces to model (2.3), (2.1) or (2.4) when c = 0,c = 1
or d = 1, respectively. For testing purposes, we want an e3-optimal design for estimating
the parameter c and an e4-optimal design for estimating the parameter d. The vector of
partial derivatives of η for model (2.5) is
f(t,θ) = (c −(c −1)e−btd,a(c −1)tde−btd,a(c −1)td ln(t)be−btd,a(1 −e−btd))T
(2.11)
and its components form a Chebyshev system on the interval [0,T ]. Arguments similar to
those given in the proof of Lemma 2.1 show that the support points ti(b,d,T ) and weights
ωi(b,d,T ) of a locally e3- or e4-optimal design on the interval [0,T ] satisfy relations (2.9).
Moreover, the optimal designs do not depend on the parameter a. Table 2 shows some
locally e3- and e4-optimal designs for model (2.5) obtained from Theorem 2.3 below. The
proof is similar to the proof of Theorem 2.1 and is therefore omitted.
Theorem 2.3. The e3- and e4-optimal designs for model (2.5) are uniquely supported at
the four Chebyshev points, say t∗
1 < t∗
2 < t∗
3 < t∗
4, corresponding to the Chebyshev system
deﬁned by the components in (2.11). The corresponding weights, ω∗
1,...,ω∗
4, are explicitly
given by
ω∗= (ω∗
1,...,ω∗
4)T =
JF −1ek
14JF −1ek
,
k = 3,4,
where the matrices F and J are deﬁned by F = (f(t∗
1,θ),f(t∗
2,θ),f(t∗
3,θ),f(t∗
4,θ)), J =
diag(1,−1,1,−1), respectively, 14 = (1,1,1,1)T and f(t,θ) is given in (2.11).


## Page 8


Optimal designs for discriminating between dose-response models
1171
Table 2. Locally e3- and e4-optimal designs for model (2.5) on the design space [0,1] for various
values of the parameter b
b
t1
t2
t3
t4
e3-optimal
e4-optimal
ω1
ω2
ω3
ω4
ω1
ω2
ω3
ω4
0.1
0
0.131
0.648
1
0.286
0.416
0.214
0.084
0.174
0.328
0.326
0.172
0.5
0
0.123
0.626
1
0.277
0.410
0.223
0.090
0.156
0.302
0.342
0.200
1.0
0
0.113
0.596
1
0.267
0.403
0.233
0.097
0.137
0.272
0.352
0.239
2.0
0
0.094
0.530
1
0.253
0.392
0.246
0.108
0.106
0.215
0.341
0.338
3.0
0
0.079
0.463
1
0.244
0.382
0.256
0.118
0.080
0.163
0.289
0.468
3. Maximin optimal discriminating designs
We now wish to ﬁnd an eﬃcient design for testing several hypotheses that discriminate
between models (2.3) and (2.2), (2.4) and (2.2), (2.5) and (2.3), and (2.5) and (2.4).
Let us ﬁrst ﬁnd an optimal design to discriminate between two models (2.i) and
(2.j) and let eﬀ(2.i)−(2.j)(ξ,θ) be the eﬃciency of the design ξ for discriminating be-
tween the two models. As an illustrative case, consider ﬁnding the locally optimal design
for discriminating between the models (2.3) and (2.2). This optimal design minimizes
eT
3 M −1
(2.3)(ξ,θ)e3 among all designs for which the matrix is regular (Theorem 2.1). Here,
the matrix M(2.3)(ξ,θ) is the information matrix under model (2.3). If ξ∗
3(θ) is the locally
optimal design for discriminating between models (2.3) and (2.2), then the eﬃciency of
a design ξ for discriminating between models (2.3)–(2.2) is deﬁned by
eﬀ(2.3)−(2.2)(ξ,θ) =
eT
3 M −1
(2.3)(ξ∗
3(θ),θ)e3
eT
3 M −1
(2.3)(ξ,θ)e3
.
This ratio is between 0 and 1; if the value is 0.5, this means that twice as many obser-
vations are required from the design ξ than the optimal design to discriminate between
the two models with the same level of precision. The eﬃciencies of ξ for discriminating
between other pairs of models are similarly deﬁned and denoted by eﬀ(2.4)−(2.2)(ξ,θ),
eﬀ(2.5)−(2.3)(ξ,θ) and eﬀ(2.5)−(2.4)(ξ,θ). Here, and elsewhere in our work, we remind
readers that we assume θ to be ﬁxed throughout and so all optimal designs are only
locally optimal.
Next, we use the maximin eﬃcient approach proposed by Dette [7] and M¨uller [19] to
ﬁnd eﬃcient designs for all four discrimination problems. For a ﬁxed θ, we call a design
a maximin optimal discriminating design for models (2.1)–(2.5) if it maximizes
min{eﬀ(2.3)−(2.2)(ξ,θ),eﬀ(2.4)−(2.2)(ξ,θ),eﬀ(2.5)−(2.3)(ξ,θ),eﬀ(2.5)−(2.4)(ξ,θ)}.
(3.1)
In practice, maximin optimal discriminating designs have to be found numerically. All
computations for the optimal designs were done sequentially using the Nelder–Mead al-


## Page 9


1172
Dette, Pepelyshev, Shpilev and Wong
gorithm in the MATLAB package. First, maximin designs were found by maximizing the
optimality criterion within the class of all 4-point designs. We started with four points
because that was the number of points required for obtaining all non-zero eﬃciencies in
(3.1). After the 4-point optimal design was found, we searched for the optimal design
within the class of all 5-points designs and repeated the procedure. Each time, we in-
creased the number of points by unity, until there was no further improvement in the
criterion value. Table 3 shows maximin optimal discriminating designs and their eﬃ-
ciencies when θ = (a,b,d,c)T = (1,b,1,0)T for diﬀerent values of b. We observe from the
rightmost columns in the table that the maximin optimal discriminating design has be-
tween 68–85% eﬃciency for discriminating between diﬀerent pairs of rival models from
the postulated class.
4. Eﬃciencies of maximin optimal designs for
estimating model parameters under model
uncertainty
We now investigate the performance of maximin discrimination designs for estimating
parameters in the diﬀerent models. We ﬁrst present results for estimating each parameter
in the model and D-eﬃciencies of the maximin discrimination design for estimating all
parameters in the model. We recall that D-eﬃciencies are computed relative to the D-
optimal design for the speciﬁc model and D-optimal designs are found by maximizing
the determinant of the expected information matrix over all designs on the design space.
D-optimal designs are appealing because they minimize the generalized variance and
thereby provide the smallest volume of the conﬁdence ellipsoid for all parameters in the
mean function.
Table 4 displays eﬃciencies of selected maximin optimal discriminating designs for
estimating the individual parameters in the four models. The eﬃciencies for estimating
the parameter a are consistently the lowest and eﬃciencies for estimating the parameters
b, c and d tend to be sequentially higher for each model. It is not surprising to observe
that the eﬃciencies are highest for estimating the particular parameter that sets the two
models apart.
Table 3. Maximin optimal discriminating designs for the optimality criterion (3.1) on the design
space [0,1] and their eﬃciencies
b
t1
t2
t3
t4
ω1
ω2
ω3
ω4
(2.3)–(2.2)
(2.4)–(2.2)
(2.5)–(2.3)
(2.5)–(2.4)
0.1 0
0.175 0.552 1
0.236 0.255 0.322 0.187 0.724
0.724
0.724
0.786
0.5 0
0.170 0.531 1
0.220 0.260 0.308 0.212 0.719
0.719
0.719
0.787
1.0 0
0.160 0.507 1
0.200 0.265 0.287 0.249 0.714
0.714
0.714
0.793
2.0 0
0.130 0.468 1
0.161 0.250 0.249 0.340 0.705
0.702
0.702
0.848
3.0 0
0.105 0.440 1
0.141 0.233 0.199 0.427 0.705
0.682
0.682
0.871


## Page 10


Optimal designs for discriminating between dose-response models
1173
Table 5 shows D-eﬃciencies of the maximin optimal discriminating designs in Table
3. These are eﬃciencies relative to each of the locally D-optimal designs found for each
model in the class. For the values of b in Table 5, all eﬃciencies are high. Recall that the
optimal discriminating designs were constructed for discriminating between models (2.2)
and (2.3). We observe that these eﬃciencies are highest for the most complicated model,
(2.5), averaging 96%, while the eﬃciencies are about 67% for the least complicated model,
(2.2). This implies that the maximin optimal designs are quite robust to misspeciﬁcation
of models within the class of models and also quite insensitive to small changes to the
nominal values of the parameter b common to all of the models. In models (2.2) and
(2.3), the D-eﬃciencies drop by roughly 15% when the nominal value of b is increased
from 2 to 3.
5. Conclusions
Our work is motivated by toxicologists’ recent interest in a class of non-linear nested
models for studying a continuous outcome. The toxicologists were primarily interested
in estimating parameters or a function of model parameters. The designs employed in
their studies lacked justiﬁcation. Our work addresses design issues for such a problem,
where there is model uncertainty and all candidate models are non-linear models nested
within one another. The proposed optimal designs are eﬃcient for model discrimination
and parameter estimation. Previous design work for discriminating between non-linear
models usually focused on two rival models; our work ﬁnds eﬃcient and analytic locally
optimal discriminating designs for discriminating between pairs of models within the
predetermined class.
Our proposed optimal designs were constructed using large-sample theory. The vari-
ances of the estimated parameters were obtained via the asymptotic covariance matrix
that our optimal designs used to minimize the asymptotic variances. It is reasonable to
ask whether the asymptotic variance is a good approximation to the actual variance of the
Table 4. Eﬃciencies of the maximin optimal discriminating designs in Table 3 for estimating
individual coeﬃcients in models (2.2)–(2.5); the ﬁrst two columns are eﬃciencies for estimating
a and b in model (2.2), the next three columns are for estimating a, b and d in model (2.3),
the next three columns are eﬃciencies for estimating a, b and c in model (2.4) and the last four
columns are for estimating a, b, c and d in model (2.5)
b
Model (2.2)
Model (2.3)
Model (2.4)
Model (2.5)
eﬀ1
eﬀ2
eﬀ1
eﬀ2
eﬀ3
eﬀ1
eﬀ2
eﬀ3
eﬀ1
eﬀ2
eﬀ3
eﬀ4
0.1
0.42
0.495
0.26
0.495
0.724
0.30
0.726
0.724
0.24
0.784
0.724
0.786
0.5
0.37
0.501
0.25
0.490
0.719
0.27
0.725
0.719
0.22
0.773
0.719
0.787
1.0
0.32
0.545
0.22
0.495
0.714
0.25
0.716
0.714
0.20
0.760
0.714
0.793
2.0
0.24
0.609
0.17
0.325
0.705
0.21
0.661
0.702
0.16
0.759
0.702
0.849
3.0
0.20
0.429
0.15
0.514
0.705
0.18
0.560
0.682
0.14
0.708
0.682
0.871


## Page 11


1174
Dette, Pepelyshev, Shpilev and Wong
Table 5. D-eﬃciencies of maximin designs in Table 3 under various model assumptions
b
eﬀ(2.2)
D
eﬀ(2.3)
D
eﬀ(2.4)
D
eﬀ(2.5)
D
0.1
0.710
0.851
0.851
0.963
0.5
0.737
0.862
0.861
0.968
1.0
0.786
0.873
0.869
0.972
2.0
0.703
0.864
0.860
0.959
3.0
0.525
0.716
0.820
0.917
estimated parameters encountered in practice with realistic sample size. We performed
a small simulation study using the setup in [23], where rats were prenatally exposed to
diethylstilbestrol and the design ξu had 6 animals in each of the 10 dose groups at 0, 1.0,
1.7, 2.8, 4.7, 7.8, 13, 22, 36 and 60 mg/kg body weight per day. In total, there were 60
observations from the dose interval [0,60]. The maximin optimal design ξmm for b = 0.1,
d = 1, c = 0 requires 7 rats at the 0 dose, 12 rats at the 3.6 dose, 13 rats at the 24 dose
and 28 at the 60 dose.
We simulated data with a = 1, σ = 0.05 and several values of the parameters b, d and c.
A total of 1000 repetitions were used in each simulation. In Table 6, we report simulated
normalized variances of least-squares estimated parameters that are most important for
discrimination. We see that in all of the cases we investigated, the variances using the
maximin optimal design ξmm are smaller than the variances obtained from the design ξu
of Piersma et al., in many cases by a huge margin. This shows the beneﬁts of incorporating
optimal design ideas into the design of a toxicology study. The design of Piersma et al.
was not theory-based and required more dose levels, which usually translated to higher
labor, material and time costs without gain in precision for the estimates relative to the
optimal design. Additional simulation results not shown here conﬁrm that the asymptotic
variances are close to the simulated variances.
Finally, we mention that, in principle, the approach presented here can be applied
to discriminate between models when the diﬀerence between the dimensions of the null
hypothesis and the alternative is greater than 1. For example, suppose that we wish to
discriminate between model (2.2) and the model with mean response given by a+b1ec1t +
b2t. In this case, the design maximizing the non-centrality parameter of the likelihood
ratio test depends on the values of the parameters of the larger model. The extension of
our procedure to Ds-optimal designs for minimizing the volume of the conﬁdence ellipsoid
for the parameters (b1,b2) would still work, but some eﬃciency would be lost.
To facilitate the use of optimal designs for practitioners, we have created a website
that freely generates diﬀerent types of tailor-made optimal designs for various popular
models.
We are currently reﬁning the computer algorithms for generating optimal designs dis-
cussed here and plan to upload them to the site at http://optimal-design.biostat.ucla.edu/
optimal. We hope that the site will stimulate interest in design issues, inform practitioners
and enable them to incorporate optimal design ideas into their work.


## Page 12


Optimal designs for discriminating between dose-response models
1175
Table 6. Simulated normalized variances of some parameters in models (2.4)–(2.6) for several
true values of parameters (left three columns)
b
d
c
Maximin design ξmm
Design ξu
(2.4)
(2.5)
(2.6)
(2.6)
(2.4)
(2.5)
(2.6)
(2.6)
var( ˆd)
var(ˆc)
var( ˆd)
var(ˆc)
var( ˆd)
var(ˆc)
var( ˆd)
var(ˆc)
0.10
1.0
0.0
58.85
2.02
71.07
2.48
62.73
5.53
88.42
7.81
0.10
0.8
0.0
30.38
5.39
83.93
28.91
34.93
26.72
86.34
58.80
0.10
1.0
0.2
11.86
1.96
103.40
2.79
18.43
4.83
138.97
7.77
0.10
0.8
0.2
19.39
4.21
135.00
35.91
23.57
10.88
148.29
81.56
0.06
1.0
0.0
61.67
3.91
103.78
7.17
61.62
11.35
115.70
23.33
0.08
1.0
0.1
22.58
2.47
92.44
3.68
36.83
6.48
113.39
10.80
Appendix: Proofs of Lemma 2.1 and Theorem 2.1
A.1. Proof of Lemma 2.1
Let I(t,a,b,d) = f(t,a,b,d)f T(t,a,b,d), where f(t,a,b,d) is given in (2.8). Lemma 2.1
follows from the identities
det
Z T
0
I(t,a,b,d)dξ(t) = γ det
Z T d
0
I(td,1,b,1)dξ(t) = γ det
Z T
0
I(t,1,b,1)dξ(t1/d)
and
det
Z T
0
I(t,a,rb,1)dξ(t) = γ′ det
Z T
0
I(rt,1,b,1)dξ(t) = γ′ det
Z T
0
I(t,1,b,1)dξ(t/r),
where γ and γ′ denote appropriate constants.
A.2. Proof of Theorem 2.1
Let g(t) = pT f(t) be an arbitrary linear combination of the functions e−bt,−te−bt and
−tln(t)e−bt. One can show that (g(t)ebt)′′ = c/t does not have any roots in the interval
[0,T ] and so the function g(t) has at most two roots. This proves that the system of
functions e−bt,−te−bt,−tln(t)e−bt has the Chebyshev property and this argument also
shows that there exist precisely three Chebyshev points.
The proof of the remaining part now follows by a standard argument in classical
optimal design theory. After showing that the functions e−bt,−te−bt form a Chebyshev
system on the interval [0,T ], we have

e−bt1
e−bt2
0
−t1e−bt1
−t2e−bt2
0
−t1 ln(t1)e−bt1
−t2 ln(t2)e−bt2
1

=

e−bt1
e−bt2
−t1e−bt1
−t2e−bt2
 ̸= 0


## Page 13


1176
Dette, Pepelyshev, Shpilev and Wong
for all 0 ≤t1 < t2 ≤T and, consequently, from [14], Theorem 7.7, the locally e3-optimal
design is supported at the Chebyshev points. The assertion on the weights of the locally
e3-optimal design follows from [21].
Acknowledgements
The authors are grateful to Martina Stein, who typed parts of this paper with con-
siderable technical expertise. The work of H. Dette was supported by the Collaborative
Research Center “Statistical modeling of non-linear dynamic processes” (SFB 823) of the
German Research Foundation (DFG) and in part by a NIH Grant award IR01GM072876
and the BMBF-Grant SKAVOE. The work of W.K. Wong was partially supported by
NIH Grant awards R01GM072876, P01 CA109091 and P30 CA16042-33. The work of A.
Pepelyshev and P. Shpilev was partially supported by an RFBR Grant, project number
09-01-00508.
References
[1] Atkinson, A.C., Donev, A.N. and Tobias, R.D. (2007). Optimum Experimental Designs.
Oxford: Oxford Univ. Press. MR2323647
[2] Atkinson, A.C. and Fedorov, V.V. (1975). Optimal design: Experiments for discriminating
between several models. Biometrika 62 289–303. MR0381163
[3] Box, G.E.P. and Hill, W.J. (1967). Discrimination among mechanistic models. Technomet-
rics 9 57–71. MR0223048
[4] Chernoﬀ, H. (1953). Locally optimal designs for estimating parameters. Ann. Math. Statist.
24 586–602. MR0058932
[5] Dette, H. (1990). A generalization of D- and D1-optimal designs in polynomial regression.
Ann. Statist. 23 1784–1804. MR1074435
[6] Dette, H. (1994). Discrimination designs for polynomial regression on a compact interval.
Ann. Statist. 22 890–904. MR1292546
[7] Dette, H. (1995). Optimal designs for identifying the degree of a polynomial regression.
Ann. Statist. 23 1248–1266. MR1353505
[8] Dette, H., Melas, V.B. and Wong, W.K. (2005). Optimal design for goodness-of-ﬁt of the
J. Amer. Statist. Assoc. 100 1370–1381. MR2236448
[9] Dette, H. and Roeder, I. (1997). Optimal discrimination designs for multi-factor experi-
ments. Ann. Statist. 25 1161–1175. MR1447745
[10] Dette, H. and Haller, G. (1998). Optimal discriminating designs for Fourier regression. Ann.
Statist. 26 1496–1521. MR1647689
[11] Dette, H. and Titoﬀ, S. (2009). Optimal discrimination designs. Ann. Statist. 37 2056–2082.
MR2533479
[12] Hill, W.J., Hunter, W.G. and Wichern, W.D. (1968). A joint design criterion for the dual
problem of model discrimination and parameter estimation. Technometrics 10 145–
160. MR0221680
[13] Jennrich, R.J. (1969). Asymptotic properties of non-linear least squares estimators. Ann.
Math. Statist. 40 633–643. MR0238419


## Page 14


Optimal designs for discriminating between dose-response models
1177
[14] Karlin, S. and Studden, W. (1966). TchebysheﬀSystems: With Application in Analysis and
Statistics. New York: Wiley. MR0204922
[15] Kiefer, J.C. (1974). General equivalence theory for optimum designs (approximate theory).
Ann. Statist. 2 849–879. MR0356386
[16] Lopez-Fidalgo, J., Tommasi, C. and Trandaﬁr, P.C. (2007). An optimal experimental design
criterion for discriminating between non-normal models. J. Roy. Statist. Soc. B 69 1–
12. MR2325274
[17] Lopez-Fidalgo, J., Tommasi, C. and Trandaﬁr, P.C. (2008). Optimal designs for discrim-
inating between some extensions of the Michaelis–Menten model. J. Statist. Plann.
Inference 138 3797–3804. MR2455967
[18] Moerbeek, M., Piersma, A.H. and Slob, W. (2004). A comparison of three methods for
calculating conﬁdence intervals for the benchmark dose. Risk Anal. 24 31–40.
[19] M¨uller, C.H. (1995). Maximin eﬃcient designs for estimating non-linear aspects in linear
models. J. Statist. Plann. Inference 44 117–132. MR1323074
[20] Pukelsheim, F. (1993). Optimal Design of Experiments. New York: Wiley. MR1211416
[21] Pukelsheim, F. and Torsney, B. (1991). Optimal weights for experimental designs on linearly
independent support points. Ann. Statist. 19 1614–1625. MR1126341
[22] Slob, W. (2002). Dose-response modeling of continuous endpoints. Toxicol. Sci. 66 298–312.
[23] Piersma, A.H., Verhoef, A., Sweep, C.G.J., de Jong, W.H. and van Loveren, H. (2002).
Developmental toxicity but no immunotoxicity in the rat after prenatal exposure to
diethylstilbestrol. Toxicology 174 173–181.
[24] Slob, W. and Pieters, M.N. (1998). A probabilistic approach for deriving acceptable human
intake limits and human health risks from toxicological studies: General framework.
Risk Anal. 18 787–798.
[25] van der Vaart, A.W. (1998). Asymptotic Statistics. Cambridge: Cambridge Univ. Press.
MR1652247
Received October 2008 and revised November 2009

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
