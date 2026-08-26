---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.10628v2
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1908.10628v2_Changepoint_in_Linear_Relations

> Source: 1908.10628v2_Changepoint_in_Linear_Relations.pdf

> Pages: 24

---


## Page 1


Changepoint in Linear Relations
Michal Peˇsta
Charles University, Prague, Czech Republic.
E-mail: Michal.Pesta@mﬀ.cuni.cz
Abstract. Linear relations, containing measurement errors in input and output data, are con-
sidered. Parameters of these so-called errors-in-variables models can change at some unknown
moment. The aim is to test whether such an unknown change has occurred or not. For in-
stance, detecting a change in trend for a randomly spaced time series is a special case of the
investigated framework. The designed changepoint tests are shown to be consistent and in-
volve neither nuisance parameters nor tuning constants, which makes the testing procedures
eﬀortlessly applicable. A changepoint estimator is also introduced and its consistency is proved.
A boundary issue is avoided, meaning that the changepoint can be detected when being close
to the extremities of the observation regime. As a theoretical basis for the developed meth-
ods, a weak invariance principle for the smallest singular value of the data matrix is provided,
assuming weakly dependent and non-stationary errors. The results are presented in a simu-
lation study, which demonstrates computational eﬃciency of the techniques. The completely
data-driven tests are illustrated through a calibration problem, however, the methodology can
be applied to other areas such as clinical measurements, dietary assessment, computational
psychometrics, or environmental toxicology as manifested in the paper.
Keywords: changepoint, errors-in-variables, hypothesis testing, non-stationarity, nuisance-
parameter-free, singular value, weak invariance principle
1.
Introduction and main aims
If measured input and output data are supposed to be in some linear relations, then it is of
particular interest to detect whether impact of the input characteristics has changed over
time on the output observables. Moreover, only error-prone surrogates of the unobserv-
able input-output characteristics are in hand instead of a precise measurement. Despite
the fact that the relations and, consequently, suitable underlying stochastic models are
linearly deﬁned, the possible estimates and the corresponding inference may be highly
non-linear (Gleser, 1981). It becomes even more challenging to handle measurement er-
rors in input and output data simultaneously, when the linear relations are subject to
change at some unknown time point—changepoint.
There is a vast literature aimed at linear relations modeled through so-called measure-
ment error models or errors-in-variables models (for an overview, see Fuller (1987), Van
Huﬀel and Vandewalle (1991), Carroll et al. (2006), Buonaccorsi (2010), or Yi (2017)), but
very little has been explored in the changepoint analysis for these models yet. A change
in regression has been explored thoroughly, cf. Horv´ath (1995) or Aue et al. (2008). How-
ever, such a framework does not cover the case of measurement error models. Maximum
likelihood approach (Chang and Huang, 1997; Staudenmayer and Spiegelman, 2002) and
arXiv:1908.10628v2  [math.ST]  17 Jan 2020


## Page 2


2
M. Peˇsta
Bayesian approach (Carroll et al., 1999; G¨ossl and K¨uchenhoﬀ, 2001) to the changepoint
estimation in the measurement error models were applied, both requiring parametric dis-
tributional assumptions on the errors. Kukush et al. (2007) estimated the changepoint in
the input data only. A change in the variance parameter of the normally distributed errors
within the measurement error models was investigated by Dong et al. (2016). All of these
mentioned contributions dealt with the changepoint estimation solely. Our main goal is
to test for a possible change in the parameters relating the input and output data, both
encumbered by some errors. Consequently, if a change is detected, we aim to estimate
it. By our best knowledge, we are not aware of any similar results even for the indepen-
dent and identically distributed errors. Additionally to that, our changepoint tests are
supposed to be nuisance-parameter-free, distributional-free, and to allow for very general
error structures.
1.1.
Outline
The paper is organized as follows: In the next section, our data model for the changepoint
in errors-in-variables is introduced and several practical motivations for such a model are
given. Section 3 contains a spectral weak invariance principle for weakly dependent and
non-stationary random variables. It serves as the main theoretical tool for the conse-
quent inference. The technical assumptions are discussed as well. Two test statistics for
the changepoint detection are proposed in Section 4. Consequently, their asymptotic be-
havior is derived under the null as well as under the alternative hypothesis. Moreover,
a consistent changepoint estimator is introduced. Section 5 contains a simulation study
that compares ﬁnite sample performance of the investigated tests. It numerically em-
phasizes the advantages of the proposed detection procedures. A practical application
of the developed approach to a calibration problem is presented in Subsection 6.1. On
the other hand, a theoretical application to randomly spaced time series is performed in
Subsection 6.2. Afterwards, our conclusion follows. Proofs are given in the Appendix A.
2.
Changepoint in errors-in-variables
Errors-in-variables (EIV) or also called measurement error model
X = Z + Θ
(M)
and
Y = Zβ + ε
(H0)
is considered, where β ∈Rp is a vector of unknown regression parameters possibly subject
to change, X ∈Rn×p and Y ∈Rn×1 consist of observable random variables (X are
covariates and Y is a response), Z ∈Rn×p consists of unknown constants and has full
rank, ε ∈Rn×1 and Θ ∈Rn×p are random errors.
This setup can be extended to
a multivariate case, where β ∈Rp×q, Y ∈Rn×q, and ε ∈Rn×q, q ≥1, see Subsection 3.3.
The EIV model (M)–(H0) with non-random unknown constants Z is sometimes called
functional EIV model (Fuller, 1987; Booth and Hall, 1993). On the other hand, a dif-
ferent approach may handle Z as random covariates, which is called structural EIV


## Page 3


Changepoint in Linear Relations
3
model (Chang and Huang, 1997). Stefanski (2000) stated: ‘However, functional mod-
els played an important role in the study of measurement error models and in statistics
more generally.’ And here, we will concentrate on the functional EIV model not because
of this matter-of-fact quote, but because we wish to demonstrate a distributional-free ap-
proach, where ‘no, or only minimal, assumptions are made about the distribution of the
Xs’ (Carroll et al., 2006), as challenged in the introduction. Nevertheless with respect
to derivation of the forthcoming theory for the functional EIV model, changing some
technical assumptions would allow to prove suitable results for the structural case as well.
To estimate the unknown parameter β, one usually minimizes the Frobenius matrix
norm of the errors [Θ, ε], see Golub and Van Loan (1980). This approach leads to a to-
tal least squares (TLS) estimate ˆβ = (X⊤X −λmin([X, Y ]⊤[X, Y ])Ip)−1X⊤Y , where
λmin(M) is the smallest eigenvalue of the matrix M and Ip is a (p × p) identity matrix.
Geometrically speaking, the Frobenius norm tries to minimize the orthogonal distance be-
tween the observations and the ﬁtted hyperplane. Therefore, the TLS are usually known
as orthogonal regression. One can generalize this method by replacing the Frobenius norm
by any unitary invariance matrix norm, which surprisingly yields the same TLS estimate,
having interesting invariance and equivariance properties (Peˇsta, 2016). The TLS esti-
mate is shown to be strongly and weakly consistent (Gleser, 1981; Gallo, 1982a; Peˇsta,
2011) as well as to be asymptotically normal (Gallo, 1982b; Peˇsta, 2013b, 2017) under
various conditions.
We aim to detect a possible change in the linear relation parameter β. The interest lies
in testing the null hypothesis (H0) of all observations Yi’s being random variables having
expectations Zi,•β’s. Our goal is to test against the alternative of the ﬁrst τ outcome
observations have expectations Zi,•β’s and the remaining n −τ observations come from
distributions with expectations Zi,•(β + δ)’s, where δ ̸= 0. A ‘row-column’ notation for
a matrix M is used in this manner: Mi,• denotes the ith row of M and M•,j corresponds
to the jth column of M. Furthermore, if i ∈N0, then Mi stays for the ﬁrst i rows of M
and M−i represents the remaining n −i rows of M, when the ﬁrst i rows are deleted.
Now more precisely, our alternative hypothesis is
Yτ = Zτβ + ετ
and
Y−τ = Z−τ(β + δ) + ε−τ.
(HA)
Here, δ ≡δ(n) ̸= 0 is an unknown vector parameter representing the size of change and
is possibly depending on n. The changepoint τ ≡τ(n) < n is also an unknown scalar
parameter, which depends on n as well. Although, β is considered to be independent
of n. One may also think of the changepoint in errors-in-variables framework as segmented
regression with measurement errors, cf. Staudenmayer and Spiegelman (2002).
2.1.
Intercept and ﬁxed regressors
Note that the EIV model (M)–(H0) has no intercept and all the covariates are encumbered
by some errors. To overcome such a restriction, one can think of an extended regression
model, where some explanatory variables are subject to error and some are measured
precisely. I.e., Y = W γ + Zβ + ε, where W are observable true and Z are unobservable
true constants, both having full rank. Regression parameters γ and β remain unknown.
Then, the non-random (ﬁxed) intercept can be incorporated into the regression model by


## Page 4


4
M. Peˇsta
setting one column of the matrix W equal to [1, . . . , 1]⊤. Consequently, we may project
out exact observations using projection matrix R := In −W (W ⊤W )−1W ⊤. Notice that
R is symmetric and idempotent. Finally, one may work with RY = RZβ + Rε instead
of (H0).
2.2.
Motivations
The proposed class of models—errors-in-variables with changepoint—is very rich and gen-
eral. Our approach and results are motivated in the context of several applications taken
from chemistry, biological sciences, medicine, and epidemiological studies.
Case 1: Assessing agreement in clinical measurement.
Direct measurement of cardiac
stroke volume or blood pressure without adverse eﬀects is diﬃcult or even impossible. The
true values remain unknown. Indirect methods are, therefore, used instead. When a new
measurement technique is developed, it has to be evaluated by comparison with an estab-
lished technique rather than with the true quantity (Bland and Altman, 1986). Clinicians
need to test whether both measurement techniques agree suﬃciently. Thereafter, the old
technique may be replaced by the new one.
Case 2: Nutritional epidemiology.
Staudenmayer and Spiegelman (2002) analyzed data
from a nutritional study that investigates the relation between dietary folate intake (calo-
ries adjusted µg/day) on plasma homocysteine concentration (µmol/liter of blood). There
exists a suspicion that serum homocysteine is signiﬁcantly elevated when ingested folate
is below a certain changepoint. Moreover, the analysis used estimates of folate that were
developed with a food frequency questionnaire, which is recognized to be imperfect.
Case 3: Psychometric testing.
Let us think of two psychometric instruments: unspeeded
15-item vocabulary tests and highly speeded 75-item vocabulary tests, cf. Lord (1973).
The results of both tests are error-prone. Within a group of people, there is a speculation
that individuals with an unspeeded test’s result exceeding some unknown level should
perform dramatically better in the highly speeded test.
Case 4: Environmental toxicology.
A threshold limiting value in toxicology is the dose
of a toxin or a substance under which there is harmless or insigniﬁcant inﬂuence on some
response. In a dose-response relationship, both of them are measured with errors. And
the goal is to set the threshold limiting value. Such a problem was dealt by G¨ossl and
K¨uchenhoﬀ(2001) using fully Bayesian approach. Moreover, a similar task regarding the
NO2 concentration is discussed by Stefanski (2000).
Case 5: Device calibration.
Later on in Subsection 6.1, we concentrate in more details on
the calibration task and exemplify the proposed methodology through analysis of data from
a calibrated device and a casual device (needs to be calibrated) in order to demonstrate
practical eﬃciency of our detection method.
Besides that, there are many other applications of the changepoint within the linear
relations framework in, for instance, glaciology (Gleser and Watson, 1973), empirical
economics (Chang and Huang, 1997), dietary assessment (Carroll et al., 1999), or image
forensics (Ryu and Lee, 2014).


## Page 5


Changepoint in Linear Relations
5
3.
Spectral weak invariance principle
A theoretical device is going to be developed in order to construct the changepoint
tests. The smallest eigenvalue of Σ−1[X, Y ]⊤[X, Y ]—the squared smallest singular value
of [X, Y ]Σ−1/2, i.e., the data matrix [X, Y ] multiplied by the inverse of a matrix square
root from the error variance structure (cf. subsequent Assumption E)—plays a key role.
We proceed to the assumptions that are needed for deriving forthcoming asymptotic re-
sults. Henceforth,
P−→denotes convergence in probability,
D−→convergence in distribution,
D[0,1]
−−−→
n→∞weak convergence in the Skorokhod topology D[0, 1] of c`adl`ag functions on [0, 1],
and [x] denotes the integer part of the real number x.
3.1.
Assumptions
Firstly, a design assumption on the unobservable regressors is needed.
Assumption D. ∆t := limn→∞n−1Z⊤
[nt]Z[nt], ∆−t := limn→∞n−1Z⊤
−[nt]Z−[nt] for every
t ∈(0, 1), and ∆:= limn→∞n−1Z⊤Z are positive deﬁnite.
It basically says that the error-free design points do not concentrate to close to each
other (i.e., strict positive deﬁniteness) and, simultaneously, they do not spread-out too
far (i.e., existence of limits). For example in one-dimensional case (i.e., p = 1), a simple
equidistant design, where Zi,1 = i/(n + 1), provides ∆t = t3/3 and ∆= 1/3.
Prior to postulating an errors’ assumption, we summarize the notion of strong mix-
ing (α-mixing) dependence in more detail, which will be imposed on the model’s er-
rors.
Suppose that {ξn}∞
n=1 is a sequence of random elements on a probability space
(Ω, F, P). For sub-σ-ﬁelds A, B ⊆F, let α(A|B) := supA∈A,B∈B |P(A ∩B) −P(A)P(B)|.
Intuitively, α(·|·) measures the dependence of the events in B on those in A.
There
are many ways in which one can describe weak dependence or, in other words, asymp-
totic independence of random variables, see Bradley (2005).
Considering a ﬁltration
Fn
m = σ{ξi ∈F, m ≤i ≤n}, sequence {ξn}∞
n=1 of random variables is said to be
strong mixing (α-mixing) if α(ξ◦, n) = supk∈N α(Fk
1 |F∞
k+n) →0 as n →∞. Anderson
(1958) comprehensively analyzed a class of m-dependent processes. They are α-mixing,
since they are ﬁnite order ARMA processes with innovations satisfying Doeblin’s condition
(Billingsley, 1968, p. 168). Finite order processes, which do not satisfy Doeblin’s condi-
tion, can be shown to be α-mixing (Ibragimov and Linnik, 1971, pp. 312–313). Rosenblatt
(1971) provides general conditions under which stationary Markov processes are α-mixing.
Since functions of mixing processes are themselves mixing (Bradley, 2005), time-varying
functions of any of the processes just mentioned are mixing as well. This means that the
class of the α-mixing processes is suﬃciently large for the further practical applications
and that is why we chose such a mixing condition.
Assumption E. {[Θn,•, εn]}∞
n=1 is a sequence of α-mixing absolutely continuous random
vectors having zero mean and a variance matrix σ2Σ with an unknown σ2 > 0 and
a known positive deﬁnite Σ =
"
ΣΘ
ΣΘ,ε
Σ⊤
Θ,ε
1
#
such that α([Θ◦,•, ε◦], n) = O(n−1−ϖ) as
n →∞for some ϖ > 0, supn∈N Z2
n,j < ∞, supn∈N E |Θn,j|4+ω < ∞, j ∈{1, . . . , p}, and
supn∈N E |εn|4+ω < ∞for some ω > 0 such that ωϖ > 2.


## Page 6


6
M. Peˇsta
Let us emphasize that the sequence of the errors do not have to be stationary. The
assumption of an unknown σ2 and a known Σ implies that we know the ratio of any
pair of covariances in advance.
In the simplest situation, a homoscedastic covariance
structure of the within-individual errors [Θn,•, εn] can be assumed (i.e., Σ = Ip+1), if
prior experience or essence of the analyzed problem allow for that. On the other hand,
if the covariance matrix Σ is unknown, it can be estimated when possessing replicate
measurements or validation data as commented by Stefanski (2000). There are various
approaches proposed to serve this purpose. In order ot mention at least some of them, we
refer to Cheng and Riu (2006), Guo and Little (2011), Peˇsta (2013b), or Li et al. (2019).
On the top of that, we have to bear in mind that Σ cannot be completely unspeciﬁed.
Nussbaum (1977) showed that if Σ is unrestricted, no strongly consistent estimator for β
can exist even under normally distributed errors.
Furthermore, a variance assumption for the misﬁt disturbances is stated. It can be
considered as a typical assumption for the long-run variance of residuals. Let us denote
Σ−1/2 =
" ¯ΣΘ
¯ΣΘ,ε
¯Σ⊤
Θ,ε
¯Σε
#
a symmetric square root of Σ−1, where ¯Σε ∈R is a scalar.
Assumption V. There exist φ := ¯Σε −¯Σ⊤
Θ,ε( ¯ΣΘ + β ¯Σ⊤
Θ,ε)−1( ¯ΣΘ,ε + β¯Σε) ̸= 0 and
υ := limn→∞n−1 Var ∥Y −Xβ∥2
2 > 0.
Let us remark that ¯ΣΘ,ε = 0 for the uncorrelated error structure and, then, φ = ¯Σε.
3.2.
SWIP
Finally, the spectral weak invariance principle for the smallest eigenvalues is provided.
Let us denote λi := λmin(Σ−1[Xi, Yi]⊤[Xi, Yi]) for 2 ≤i ≤n, λ0 := λ1 := 0 and
eλi := λmin(Σ−1[X−i, Y−i]⊤[X−i, Y−i]) for 0 ≤i ≤n −2, eλn := eλn−1 := 0. Note that
λn ≡eλ0.
Proposition 3.1 (SWIP). Let M and H0 hold. Under Assumptions D, E, and V,
 1
√n

λ[nt] −[nt]σ2
t∈[0,1]
D[0,1]
−−−→
n→∞
(
φ2υ
1 + ∥α∥2
2
W(t)
)
t∈[0,1]
and
 1
√n

eλ[n(1−t)] −[n(1 −t)]σ2
t∈[0,1]
D[0,1]
−−−→
n→∞
(
φ2υ
1 + ∥α∥2
2
f
W(t)
)
t∈[0,1]
,
where {W(t)}t∈[0,1] is a standard Wiener process , f
W(t) = W(1) −W(t), and α =
( ¯ΣΘ + β ¯Σ⊤
Θ,ε)−1( ¯ΣΘ,ε + β¯Σε).
3.3.
Extension to multivariate case
Suppose that β ∈Rp×q, Y ∈Rn×q, and ε ∈Rn×q, q ≥1.
Let the singular value
decomposition (SVD) of the partial transformed data be
[X[nt], Y[nt]]Σ−1/2 = U(t)Γ(t)V ⊤(t) =
p+q
X
i=1
ς(t)(i)u(t)(i)v(t)(i)⊤,


## Page 7


Changepoint in Linear Relations
7
where u(t)(i)’s are the left-singular vectors, v(t)(i)’s are the right-singular vectors, and
ς(t)(i)’s are the singular values in the non-increasing order. One may replace λ[nt] by
Λ[nt] :=
q
X
j=1

ς(t)(p+j)2
in Proposition 3.1 (and analogously for eλ[n(1−t)]). Then, the SWIP can be derived again
(see the proof of Proposition 3.1), provided adequately extended assumptions on the errors
{εn,1}∞
n=1, . . . , {εn,q}∞
n=1 instead of the original ones {εn}∞
n=1. However, the consequent
proofs would become more technical.
4.
Nuisance-parameter-free detection
Consistent estimation of β can be performed via the generalized TLS approach (Gallo,
1982a; Van Huﬀel and Vandewalle, 1989). The optimizing problem
[b, ˆΘ, ˆε] :=
arg min
[Θ,ε]∈Rn×(p+1),β∈Rp



[Θ, ε] Σ−1/2


F
s.t.
Y −ε = (X −Θ)β,
where ∥·∥F stands for the Frobenius matrix norm, has a solution consisting of the estimator
b = (X⊤X −λnΣΘ)−1(X⊤Y −λnΣΘ,ε)
(4.1)
and the ﬁtted errors [ ˆΘ, ˆε] such that


[ ˆΘ, ˆε]Σ−1/2

2
F = λn.
(4.2)
We construct the changepoint test statistics based on property (4.2).
4.1.
Changepoint test statistics
Let us think of two TLS estimates of β: The ﬁrst one based on the ﬁrst i data lines [Xi, Yi]
and the second one based on the ﬁrst k data lines [Xk, Yk] such that 1 ≤i ≤k ≤n. Under
the null H0, these two TLS estimates should be close to each other. On the other hand,
under the alternative HA such that τ ∈{i, . . . , k}, they should be somehow diﬀerent.
A similar conclusion can be made for the goodness-of-ﬁt statistics coming from (4.2). It
means that
λi −i
kλk
should be reasonably small under the null H0. Under the alternative HA such that τ ∈
{i, . . . , k}, it should be relatively large. For the multivariate case described in previous
Subsection 3.3, one has to replace λk by Λk = Pq
j=1
 ς(k/n)(p+j)2.
We rely on self-normalized test statistics introduced by Shao and Zhang (2010), be-
cause the unknown quantity φ2υ/(1 + ∥α∥2
2) from Proposition 3.1 cancels out in the test
statistics. Our supremum-type self-normalized test statistic based on the goodness-of-ﬁt is
deﬁned as
Sn := max
1≤k<n
λk −k
nλn

max1≤i<k
λi −i
kλk
 + maxk<i≤n
eλi −n−i
n−k eλk

(4.3)


## Page 8


8
M. Peˇsta
and the integral-type self-normalized test statistic is deﬁned as
Tn :=
n−1
X
k=1
 λk −k
nλn
2
Pk−1
i=1
 λi −i
kλk
2 + Pn
i=k+1
 eλi −n−i
n−k eλk
2 .
(4.4)
Let us note that evaluations of the above deﬁned test statistics require just several
singular value decompositions, which is reasonably quick. Our new test statistics involve
neither nuisance parameters nor tuning constants and will work for non-stationary and
weakly dependent data. On the top of that, no boundary issue is present meaning that
the tests can detect the change close to the beginning or to the end of the studied regime.
Under the null hypothesis and the technical assumptions from Subsection 3.1, the test
statistics deﬁned in (4.3) and (4.4) converge to non-degenerate limit distributions (their
quantiles can be found in Subsection 4.2).
Theorem 4.1 (Under the null). Let M and H0 hold. Under Assumptions D, E, and V,
Sn
D
−−−→
n→∞
sup
t∈[0,1]
W(t) −tW(1)

sups∈[0,t]
W(s) −s
tW(t)
 + sups∈[t,1]
 f
W(s) −1−s
1−t f
W(t)

(4.5)
and
Tn
D
−−−→
n→∞
Z 1
0
W(t) −tW(1)
	2
R t
0
W(s) −s
tW(t)
	2ds +
R 1
t
 f
W(s) −1−s
1−t f
W(t)
	2ds
dt,
(4.6)
where {W(t)}t∈[0,1] is a standard Wiener process and f
W(t) = W(1) −W(t).
The null hypothesis is rejected at signiﬁcance level α for large values of Sn and Tn.
The critical values can be obtained as the (1−α)-quantiles of the asymptotic distributions
from (4.5) and (4.6). In order to describe limit behavior of the test statistics under the
alternative, an additional changepoint assumption is required.
Assumption C. For some ζ ∈(0, 1), as n →∞,
∥δ∥2 →0
and
(ηκ −ϕ⊤ϕ)√n →∞,
(4.7)
where κ := ( ¯Σ⊤
Θ,ε+ ¯Σεβ⊤)∆ζ( ¯ΣΘ,ε+β¯Σε)+( ¯Σ⊤
Θ,ε+ ¯Σε(β+δ)⊤)∆−ζ( ¯ΣΘ,ε+(β+δ)¯Σε),
ϕ := ( ¯ΣΘ + ¯ΣΘ,εβ⊤)∆ζ( ¯ΣΘ,ε + β¯Σε) + ( ¯ΣΘ + ¯ΣΘ,ε(β + δ)⊤)∆−ζ( ¯ΣΘ,ε + (β + δ)¯Σε),
and η := λmin(( ¯ΣΘ + ¯ΣΘ,εβ⊤)∆( ¯ΣΘ + β ¯Σ⊤
Θ,ε) + σ2Ip) −σ2.
This assumption may be considered as a changepoint detectability requirement for
local alternatives, because it manages the relationship between the size of the change,
the location of the change, and the noisiness of the data in order to be able to detect the
changepoint. In case of uncorrelated error structure, the previous formulae become simpler
due to ¯ΣΘ,ε = 0. Assumption C is automatically fulﬁlled, for instance, for an arbitrary
δ →0 and the one-dimensional equidistant design points Zi’s on (0, 1) with homoscedastic
error structure, because then ηκ −ϕ⊤ϕ = β2{ζ3 + (1 −ζ)3}{1 −ζ3 −(1 −ζ)3}/9 + O(δ)
as δ →0.
Furthermore, let us remark that ϑ := ¯ΣΘ + β ¯Σ⊤
Θ,ε has full rank under
Assumption V.
Now, the tests based on Sn and Tn are shown to be consistent, as the test statistics
converge to inﬁnity under some local alternatives, provided that the size of the change
does not convergence to zero too fast, cf. Assumption C where κ and ϕ depend on δ.


## Page 9


Changepoint in Linear Relations
9
Table 1. Simulated asymptotic critical values for Sn and Tn
100(1 −α)%
90%
95%
97.5%
99%
99.5%
S -based
1.209008
1.393566
1.571462
1.782524
1.966223
T -based
5.700222
7.165705
8.807070
10.597625
11.755233
Theorem 4.2 (Under local alternatives). Let M and HA hold such that τ = [nζ] for
some ζ ∈(0, 1). Under Assumptions C, D, E, and V,
Sn
P
−−−→
n→∞∞
P
←−−−
n→∞Tn.
(4.8)
Assumption C can be sharpened as remarked below with the corresponding proof in
the Appendix A.
Remark 4.3. The second part of relation (4.7) can be replaced by
{κ+η−
q
(κ + 2σ2 + η)2 −4(κ + σ2 −ϕ⊤(ϑ⊤∆ϑ + σ2Ip)−1ϕ)(σ2 + η)}√n →∞(4.9)
and the assertion of Theorem 4.2 still holds.
Basically, Theorem 4.2 discloses that in presence of the structural change in linear
relations, the test statistics explode above all bounds. Hence, the asymptotic distributions
from Theorem 4.1 can be used to construct the tests. Although, explicit forms of those
distributions stated in (4.5) and (4.6) are unknown.
4.2.
Asymptotic critical values
The critical values may be determined by simulations from the limit distributions Sn and
Tn from Theorem 4.1. Theorem 4.2 ensures that we reject the null hypothesis for large
values of the test statistics. We have simulated the asymptotic distributions (4.5) and (4.6)
by discretizing the standard Wiener process and using the relationship of a random walk to
the standard Wiener process. We considered 1000 as the number of discretization points
within [0, 1] interval and the number of simulation runs equals to 100000. In Table 1, we
present several critical values for the test statistics Sn and Tn.
4.3.
Changepoint estimator
If a change is detected, it is of interest to estimate the changepoint. It is sensible to use
ˆτn := argmax
1≤k≤n−1
λk −k
nλn
 +
eλk −n−k
n eλ0

max1≤i<k
λi −i
kλk
 + maxk<i≤n
eλi −n−i
n−k eλk

as a changepoint estimator.
Our next theorem shows that under the alternative, the
changepoint τ is consistently estimated by the estimator ˆτn.
Corollary 4.4 (Consistency). Let the assumptions of Theorem 4.2 hold. If
∀t ∈(ζ, 1) : {η(t)κ(t) −ϕ(t)⊤ϕ(t)}√n n→∞
−−−→∞;
(4.10)


## Page 10


10
M. Peˇsta
∀t ∈(0, ζ) : {˜η(t)˜κ(t) −˜ϕ(t)⊤˜ϕ(t)}√n n→∞
−−−→∞,
(4.11)
where κ(t) := ( ¯Σ⊤
Θ,ε+ ¯Σεβ⊤)∆ζ( ¯ΣΘ,ε+β¯Σε)+( ¯Σ⊤
Θ,ε+ ¯Σε(β+δ)⊤)(∆t−∆ζ)( ¯ΣΘ,ε+(β+
δ)¯Σε), ϕ(t) := ( ¯ΣΘ + ¯ΣΘ,εβ⊤)∆ζ( ¯ΣΘ,ε +β¯Σε)+( ¯ΣΘ + ¯ΣΘ,ε(β+δ)⊤)(∆t −∆ζ)( ¯ΣΘ,ε +
(β + δ)¯Σε), ˜κ(t) := ( ¯Σ⊤
Θ,ε + ¯Σεβ⊤)∆−ζ( ¯ΣΘ,ε + β¯Σε) + ( ¯Σ⊤
Θ,ε + ¯Σε(β + δ)⊤)(∆−t −
∆−ζ)( ¯ΣΘ,ε + (β + δ)¯Σε), ˜ϕ(t) := ( ¯ΣΘ + ¯ΣΘ,εβ⊤)∆−ζ( ¯ΣΘ,ε + β¯Σε) + ( ¯ΣΘ + ¯ΣΘ,ε(β +
δ)⊤)(∆−t −∆−ζ)( ¯ΣΘ,ε + (β + δ)¯Σε), η(t) := λmin(( ¯ΣΘ + ¯ΣΘ,εβ⊤)∆t( ¯ΣΘ + β ¯Σ⊤
Θ,ε) +
tσ2Ip)−tσ2, and ˜η(t) := λmin(( ¯ΣΘ+ ¯ΣΘ,εβ⊤)∆−t( ¯ΣΘ+β ¯Σ⊤
Θ,ε)+(1−t)σ2Ip)−(1−t)σ2,
then
ˆτn
n
P
−−−→
n→∞ζ.
Conditions (4.10) and (4.11) serve as a uniform intermediary between the size of the
change, the location of the change, the sample size, and the heteroscedasticity of the
disturbances for assuring changepoint estimator’s consistency.
These assumptions are
again automatically fulﬁlled for the case discussed below Assumption C.
In order to estimate more than one changepoint, it is possible to use an arbitrary
‘divide-and-estimate’ multiple changepoints method relying on our changepoint estimator,
for instance, wild binary segmentation by Fryzlewicz (2014).
5.
Simulation study
We are interested in the performance of the tests based on the self-normalized test statistics
Sn and Tn that are completely nuisance-parameter-free. We focused on the comparison
of the accuracy of critical values obtained by the simulation from the limit distributions.
In Figures 1–4, one may see size-power plots considering the test statistics Sn and
Tn under the null hypothesis and under the alternative. Figures 1 and 2 correspond to
one input covariate (i.e., p = 1) with choices of β = 1 and Zi,1 = 100i/(n + 1). A case
with two error-prone regressors (i.e., p = 2) is illustrated in Figures 3 and 4 for choices
of β = [1, 1]⊤and Zi,• = 100 × [i/(n + 1), (i/(n + 1))3/2]. Next, n ∈{200, 1000} and τ ∈
{n/4, n/2}. The size of change is δ ∈{0.1, 0.5} for p = 1 and δ ∈{[0.1, 0.1]⊤, [0.5, 0.5]⊤}
for p = 2. Especially smaller values of the break should represent the situations under
the local alternatives. In Figures 1 and 3, the empirical rejection frequency under the
null hypothesis (actual α-errors) is plotted against the theoretical size (theoretical α-
errors with α ∈{1%, 5%, 10%}), illustrating the size of the tests. The ideal situation
under the null hypothesis is depicted by the straight diagonal dotted line. The empirical
rejection frequencies (1−errors of the second type) under the alternative (with diﬀerent
changepoints and values of the change) are shown in Figures 2 and 4, illustrating the power
of the tests. Under the alternative, the desired situation would be a steep function with
values close to 1. For more details on the size-power plots we may refer, e.g., to Kirch
(2006). The standard deviation of the random disturbances was set to σ ∈{0.5, 1.0}
and the random error terms {Θn,1}∞
n=1, . . . , {Θn,p}∞
n=1, and {εn}∞
n=1 were independently
simulated as three time series:
• IID . . . independent and identically distributed random variables;
• AR(1) . . . autoregressive (AR) process of order one having a coeﬃcient of autore-
gression equal 0.5;


## Page 11


Changepoint in Linear Relations
11
• ARCH(1) . . . autoregressive conditional heteroscedasticity (ARCH) process with the
second coeﬃcient equal 0.5.
The standard normal distribution and the Student t-distribution with 3 degrees of
freedom are used for generating the innovations of the models’ errors. All of the time series
are standardized such that they have variance equal σ2. Let us remark that the setup of
Student t3-distribution does not satisfy Assumption E. However, it can be considered as
a misspeciﬁed model and one would like to inspect performance of our procedures on such
a model that violates our assumptions. In the simulations of the rejection rates, we used
10000 repetitions.
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
σ=0.5
N(0, 1)
σ=0.5
t3
σ=1.0
N(0, 1)
σ=1.0
t3
n=200
n=1000
0.01
0.05
0.10
0.01
0.05
0.10
0.01
0.05
0.10
0.01
0.05
0.10
0.0
0.1
0.2
0.3
0.0
0.1
0.2
0.3
Significance level α
Rejection rate
Errors
IID
AR(1)
ARCH(1)
Statistics
S (sup−type)
T (int−type)
H0
Figure 1. Size-power plots for Sn and Tn under H0 (p = 1)
In all of the subﬁgures of Figures 1 and 3 depicting a situation under the null hypothesis,
we may see that comparing the accuracy of α-levels (sizes) for diﬀerent self-normalized test
statistics, the integral-type (T -based) method seems to keep the theoretical signiﬁcance
level more ﬁrmly than the supremum-type (S -based) method. Comparing the case of
N(0, 1) innovations with the case of t3 innovations, the rejection rates under the null tend
to be slightly higher for the t3-distribution. In spite of the fact that the t3-distributed
errors violate Assumption E, the performance of our tests is still surprisingly satisfactory
in such case. As expected, the accuracy of the critical values tends to be better for larger n.
The more complicated dependence structure of errors is assumed, the worse performance
of the tests is obtained. Furthermore, the less volatile errors are set, the better tests’ sizes
are attained.
The T -method performs better under the null. However under the alternative, the S -
method has a tendency to have slightly higher power than the T -method (see Figures 2
and 4). We may also conclude that under HA with less volatile errors, the power of the
test increases. The power decreases when the changepoint is closer to the beginning or the
end of the input-output data. The heavier tails (t3 against N(0, 1)) give worse results in
general for both test statistics. Moreover, ‘more dependent’ scenarios reveal worsening of
the test statistics’ performance. Furthermore, the smaller size of the change is considered,


## Page 12


12
M. Peˇsta
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
δ=0.1
N(0, 1)
δ=0.1
t3
δ=0.5
N(0, 1)
δ=0.5
t3
τ=n/4
σ=0.5
n=200
τ=n/2
σ=0.5
n=200
τ=n/4
σ=1.0
n=200
τ=n/2
σ=1.0
n=200
τ=n/4
σ=0.5
n=1000
τ=n/2
σ=0.5
n=1000
τ=n/4
σ=1.0
n=1000
τ=n/2
σ=1.0
n=1000
0.01
0.05
0.10
0.01
0.05
0.10
0.01
0.05
0.10
0.01
0.05
0.10
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Significance level α
Rejection rate
Errors
IID
AR(1)
ARCH(1)
Statistics
S (sup−type)
T (int−type)
HA
Figure 2. Size-power plots for Sn and Tn under HA (p = 1)
the lower power of the test is achieved. And again, the power gets higher for larger n.
Afterwards, a simulation experiment is performed to study the ﬁnite sample proper-
ties of the changepoint estimator for a change in the linear relations’ parameter.
We
numerically present only the case of p = 1. In particular, the interest lies in the empir-
ical distributions of the proposed estimator visualized via boxplots, see Figure 5. The


## Page 13


Changepoint in Linear Relations
13
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
σ=0.5
N(0, 1)
σ=0.5
t3
σ=1.0
N(0, 1)
σ=1.0
t3
n=200
n=1000
0.01
0.05
0.10
0.01
0.05
0.10
0.01
0.05
0.10
0.01
0.05
0.10
0.0
0.1
0.2
0.3
0.0
0.1
0.2
0.3
Significance level α
Rejection rate
Errors
IID
AR(1)
ARCH(1)
Statistics
S (sup−type)
T (int−type)
H0
Figure 3. Size-power plots for Sn and Tn under H0 (p = 2)
simulation setup is kept the same as described above.
It can be concluded that the precision of our changepoint estimate is satisfactory
even for relatively small sample sizes regardless of the errors’ structure.
Less volatile
model errors provide more precise changepoint estimate. The less complicated dependence
structure is assumed, the higher accuracy of the estimator is obtained. Furthermore, the
disturbances with heavier tails yield less precise estimates than innovations with light
tails. One may notice that higher precision is obtained when the changepoint is closer to
the middle of the data. It is also clear that the precision of ˆτn improves markedly as the
size of change increases.
6.
Applications
6.1.
Practical application: Calibration
A company has two industrial devices, where the ﬁrst one is calibrated according to some
institute of standards and the second one is just a casual device. We want to test whether
the second device is calibrated according to the ﬁrst one. In this calibration problem, it
means to know whether the second device has approximately the same performance up
to some unknown multiplication constant as the ﬁrst one. Consequently, other devices of
the same type are needed to be calibrated as well. For some reasons, e.g., economic or
logistic, it is only possible to calibrate one device by the oﬃcial authorities.
Our data set, provided by a Czech steelmaker, contains 100 couples of speed values of
two hammer rams (see Figure 6), where the ﬁrst forging hammer is calibrated. We set the
same power level on both hammers and measure the speed of each hammer ram repeatedly
changing only the power level. Our measurements of the speed are encumbered with errors
of the same variability in both cases, because we use the same device for measuring the
speed and both forging hammers are of the same type.
Since the power set for the
forging hammer is directly proportional to the speed of the hammer ram, our goal is to


## Page 14


14
M. Peˇsta
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
δ=0.1
N(0, 1)
δ=0.1
t3
δ=0.5
N(0, 1)
δ=0.5
t3
τ=n/4
σ=0.5
n=200
τ=n/2
σ=0.5
n=200
τ=n/4
σ=1.0
n=200
τ=n/2
σ=1.0
n=200
τ=n/4
σ=0.5
n=1000
τ=n/2
σ=0.5
n=1000
τ=n/4
σ=1.0
n=1000
τ=n/2
σ=1.0
n=1000
0.01
0.05
0.10
0.01
0.05
0.10
0.01
0.05
0.10
0.01
0.05
0.10
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Significance level α
Rejection rate
Errors
IID
AR(1)
ARCH(1)
Statistics
S (sup−type)
T (int−type)
HA
Figure 4. Size-power plots for Sn and Tn under HA (p = 2)
test whether the ratio of two hammer rams’ speeds is kept constant over changing the
power level or not. Therefore, our changepoint in the EIV model is very suitable for this
setup—a linear dependence and errors in both measured speeds (with the same variance).
Both our changepoint tests—Sn = 83.2 and Tn = 861.4—reject the null hypothesis of
a constant linear coeﬃcient between two hammer rams’ speed values at the signiﬁcance


## Page 15


Changepoint in Linear Relations
15
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGG
GGGG
GGGG
GG
G
G
G
GGG
GGGGGGGG
GGGG
G
G
GGG
G
G
G
G
GGG
G
G
GGG
G
G
G
GGG
G
G
G
GGG
G
G
GG
G
GGGG
G
GGG
G
G
GGGGGGG
G
GGG
GG
G
GGG
G
GG
G
GGGGG
G
G
GG
G
G
GGGGG
G
G
GG
GGGGGG
G
GG
G
G
GG
G
G
G
GG
GGGG
G
G
G
G
GGGGG
GGGG
G
G
G
GGG
G
GG
GG
GGGGGGGGG
GG
GGG
G
G
GGG
G
G
GG
GG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGG
G
GGGGGGGGG
G
GGGGG
G
GGGGGGGGGGGGGGGGGGGGGG
G
GG
G
GGGGGGGG
G
GGGGGGGG
G
GGGGGGGGGGGGGGGGGGGGGGG
G
GGGGGGGGGGGGGGG
G
GGGGGG
G
GGGGGGGGG
G
GGGGGGGGGGG
G
G
G
G
GGGGG
GG
G
G
G
GGGGGGG
G
GGGG
G
GGGGGGGG
G
GGG
G
G
G
GG
G
G
G
G
GG
G
G
G
G
GG
G
GG
GG
G
G
G
G
G
GG
GG
G
G
G
G
G
G
G
G
GGG
G
G
G
G
G
G
G
GG
G
G
G
G
GGGG
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
GGG
G
G
G
G
GGG
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
GGG
GGGGGGGGGGGGGGGGGGGGG
GG
GGGGGGGGGGGGGGGGGGGG
GGGGG
G
GGGGGGGGGGGGGGGGGGGG
GGGGGGGG
GGGG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
GGG
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
GG
G
G
G
G
G
GGG
GGGGGGG
G
GG
G
G
G
G
GG
G
GG
G
G
G
G
G
G
GG
GG
G
G
G
G
G
G
G
G
GGG
G
G
GG
G
G
G
G
GG
G
G
G
GG
GG
G
G
G
G
G
G
GG
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
GG
G
GG
G
G
G
G
GG
G
G
G
G
GGGG
GG
G
G
GG
G
G
G
G
G
GG
GGG
G
G
G
G
GG
G
G
G
G
G
G
G
GG
G
G
G
G
G
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
G
G
G
G
GG
G
G
G
GG
G
GG
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
GG
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
GGG
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
GG
G
G
GGG
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
GGG
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GGG
GG
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
GG
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
GGG
G
G
G
G
G
GG
G
G
G
GGG
G
G
G
G
G
G
G
G
G
G
GGGG
G
G
G
GGGGGGGGGGGGGGGG
G
GGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGG
G
G
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
GG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
GGG
G
GGGGGG
GG
G
G
GGGGG
G
GG
G
GGGGG
G
GGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGG
G
GGGGGGGG
G
GGGG
GGGGGGGGGG
G
G
GGGGGGGGGGGG
G
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGG
G
GGGGGGGGGG
G
G
GGG
G
GG
GGG
G
G
GG
G
G
GG
G
GGG
G
GGG
G
GGGGGG
G
G
G
GGG
GG
G
GGG
GGGG
G
GGG
GG
G
GG
GGGG
G
G
G
GGGG
G
GG
GGGGGG
G
GGG
G
GGGGGG
G
GGG
G
G
GGGGG
G
GG
G
GG
G
GG
G
G
G
G
GGG
GG
G
G
G
GG
G
G
GGG
G
G
G
G
G
G
GG
G
G
G
G
GGGGGGG
G
G
G
G
G
G
G
G
G
GGG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GGGG
G
GGG
G
G
GG
G
G
G
G
GGGG
G
G
G
G
G
G
G
GGGGG
G
G
G
GGGG
G
G
G
GGGG
G
GGGG
G
G
G
GGGGGGGGG
G
G
GG
GGG
G
G
G
GGG
G
GG
G
G
G
G
G
GG
G
G
G
G
GG
G
G
G
G
G
GG
G
G
G
GG
G
G
G
G
G
GG
G
G
G
G
G
G
GGGG
G
G
G
G
G
G
GG
GGG
G
GGGG
GG
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
GGG
G
G
G
G
GG
G
G
G
GG
GGG
G
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGG
G
GGGGG
G
GGGGGGGGGGGGGG
G
G
GGGG
G
GGGG
GGGGGGGGGGGGGGGGG
G
GGGGG
G
GG
G
G
GGGGGG
G
G
G
GGGGGGGGGGGGG
GGG
G
GGGGGG
G
GGGGGGG
G
GGGGGGGG
G
GGGGGGGGGGGGGGG
GGGG
G
G
GGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
GGGGGGGGGG
G
GGGG
GGGGGGGG
G
G
G
GGG
G
GG
G
G
G
G
GG
G
GG
G
G
GG
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
GG
GG
G
G
G
G
G
GG
G
G
GG
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
GG
G
G
G
G
G
G
GG
G
G
GG
GG
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
GG
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
GGG
G
G
GG
G
G
G
G
G
GG
G
G
GGG
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
GG
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
GGG
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
GG
GG
G
GGGG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
GG
GG
G
G
G
G
G
G
G
G
G
G
GGG
G
G
G
G
G
G
GG
GG
G
GG
G
G
G
G
G
G
GG
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
GG
G
G
G
GGG
G
G
G
GG
G
G
G
GG
G
G
G
GG
G
G
G
G
G
GG
G
G
G
G
G
GG
GG
G
GG
G
G
G
G
G
GG
G
G
G
G
GG
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
GG
GG
G
G
G
G
G
GG
GG
GG
G
G
G
GG
G
G
GG
G
G
G
G
GG
G
G
G
GG
GG
G
GG
G
GGG
G
G
G
GGGGGGGGGG
G
GGGG
G
GGGGGGGGGGGGGGG
GGGGGGGGGGGG
G
G
G
G
G
G
G
GGGGGGGGGGGGGGGGGGGGGG
G
G
G
GGG
G
GG
G
GGG
GGGGGG
G
GGGGGGGGGGG
G
GGGGGGGG
GGGG
G
GGGGG
G
G
GGGGGGG
GG
G
G
G
GGGGGG
G
G
G
GGG
G
G
G
GGGG
G
GGGG
G
GGG
G
G
G
G
G
GG
G
GG
GG
G
G
G
GG
G
G
G
G
GG
G
G
G
G
G
G
GG
GGG
GG
G
GG
G
G
G
GG
G
GG
G
G
G
G
G
GGG
G
GG
G
GG
G
G
G
G
G
G
G
G
G
GGGG
GGGGGG
G
G
GGGG
G
GGGG
G
G
G
G
G
G
G
G
GG
G
G
G
GG
G
G
G
G
G
GGGG
G
G
GGGG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GGGGGGG
G
GGGG
G
G
G
G
G
G
G
G
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
G
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
GGGGGGG
GGGGGG
GGG
GG
G
GGGGGGG
GGGG
G
G
GG
GGGGGG
G
GGGGGGGGGG
GGGGGGGGGGGG
G
G
GGGG
G
G
G
G
G
G
G
GG
G
G
G
G
G
GG
G
GGG
G
G
G
G
G
GG
G
G
G
G
G
G
GG
G
G
G
G
G
GG
G
GG
G
G
G
G
G
G
G
G
G
G
G
GG
GG
GG
G
G
G
G
G
G
G
G
G
G
G
GGG
G
G
G
G
G
GG
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
GGG
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
GG
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
GG
G
G
GG
G
G
GG
G
G
G
G
G
G
G
G
G
G
GG
G
GGG
G
G
GG
G
G
G
G
GGGG
G
G
GG
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
GG
G
G
G
G
G
G
GG
G
G
G
G
G
GG
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
GG
GG
GG
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
GG
G
G
G
G
G
GGGGGG
G
G
GGGGG
G
G
G
G
GG
G
G
G
G
G
G
G
GGGG
G
GG
G
G
G
GG
G
G
GGG
G
GGG
G
G
G
GGGGGGG
G
GGG
G
GGGGG
G
GGG
G
GGGG
G
GGGGG
G
GGGG
G
G
G
G
G
G
G
G
G
GGG
G
GG
G
GGGGG
G
GG
GGG
GGGG
GGGGGGGGGGGGG
GG
G
G
GGGGG
G
G
G
G
G
G
G
GGGGG
G
G
G
G
G
G
G
G
GGGG
G
G
G
G
G
G
G
G
G
GG
GG
G
GGG
G
G
G
G
G
G
G
G
G
GGGG
G
GGGGG
G
GG
G
GG
G
GG
G
GG
G
GGGGGG
G
GG
G
G
G
G
G
G
GG
G
G
G
GGGGG
G
G
G
GGGGG
G
GG
G
GG
G
G
GG
G
GG
G
G
G
G
GGG
G
GGG
G
GGG
G
G
G
G
GG
GG
G
G
GG
G
GG
GG
G
G
G
G
G
G
G
GG
G
G
G
G
GGGGGG
GG
GGG
G
G
GG
GGGG
G
G
G
G
G
G
G
GGG
G
GGG
G
GG
G
G
G
G
GG
G
G
GGG
G
G
G
GG
G
G
G
G
G
G
GG
G
G
G
G
GG
G
G
G
G
G
G
G
G
G
G
G
G
GGGGG
GG
G
G
G
G
GG
G
G
GG
G
G
G
G
G
G
G
G
GG
G
G
G
G
G
GG
GGGGG
G
GGGGGGG
G
G
G
G
GG
G
GG
GGG
G
GG
GG
GGG
G
GG
G
G
GGGG
G
G
G
G
G
G
G
G
G
G
G
GG
G
G
G
GGGG
G
GGGGGGG
GGG
GGGGGGGGG
GGG
G
GGGGG
G
GGGGGGGGGG
GGG
G
GGG
G
G
G
GGGGGG
G
G
G
G
G
G
GG
G
G
GGG
G
G
G
GGG
G
G
G
GGGG
G
G
G
GG
G
G
GG
G
GGGG
G
G
G
G
G
GGG
G
GG
G
GG
G
GG
G
G
G
G
G
G
G
GG
G
G
GG
GG
G
GGG
G
G
G
G
GG
G
G
G
GG
G
G
G
G
GG
G
G
GG
G
GG
G
G
G
GG
GG
G
G
G
G
G
G
G
G
G
G
GGGGG
GGG
G
G
G
G
GG
G
G
GGG
G
GGG
G
GGG
G
G
GGGGGGGGGGGG
G
G
G
G
G
GGG
G
GGGG
δ=0.1
N(0, 1)
δ=0.1
t3
δ=0.5
N(0, 1)
δ=0.5
t3
σ=1.0
n=200
σ=0.5
n=200
σ=1.0
n=1000
σ=0.5
n=1000
n/4
n/2
n/4
n/2
n/4
n/2
n/4
n/2
0
50
100
150
200
0
50
100
150
200
0
250
500
750
1000
250
500
750
1000
τ
Errors
IID
AR(1)
ARCH(1)
Changepoint estimate
Figure 5. Boxplots of the estimated changepoint ˆτn (p = 1)
level of α = 0.5% (cf. Table 1; the signiﬁcance level for technical ﬁelds is usually smaller
than the standard 5%), indicating a changed performance of the second non-calibrated
hammer ram.
As an estimate for our change, we obtain ˆτn = 60 (depicted by a vertical line in Fig-
ure 6), which corresponds to the 60th measurement of pair of speeds. After this particular


## Page 16


16
M. Peˇsta
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
0
2000
4000
6000
0
2000
4000
6000
Two Hammer Rams
Figure 6. Speeds of two hammer rams, where the ﬁrst one displayed on the x-axis is calibrated. The
changepoint estimate corresponding to the technical issues of the second hammer ram after the 60th
measurement is depicted by the vertical line
measurement, we have background information that a technical issue appeared to the sec-
ond hammer ram—one of its oil tubes started to leak. Our procedure is indeed capable to
detect and, consequently, to estimate the changepoint in the ratio of the hammer rams’
speeds. And this is done fully automatically without expert knowledge about the oil tube
issue and also without setting tuning parameters. Moreover, the estimated ratio via the
TLS approach before the change is 1.000891 (the slope of the green line in Figure 6), which
basically says that the hammer rams work approximately in the same way. However, the
estimated ratio via the TLS approach after the change is 0.9892154 (the slope of the red
line in Figure 6), which is signiﬁcantly diﬀerent from constant 1 (see a formal statistical
test by Peˇsta (2013b)).
Other calibration examples, where our methodology is applicable, can be found in,
e.g., Cheng and Riu (2006) or Guo and Little (2011).
6.2.
Theoretical application: Randomly spaced time series
A motivation for the changepoint problem in randomly spaced time series comes from
the changepoint in the polynomial trending regression (Aue et al., 2009). Let us think
of a single regressor measured precisely such that Xi,1 ≡Zi,1 = i/(n + 1). This indeed
corresponds to a situation of a one-dimensional equally (regularly) spaced time series,
where the original time points {i}n
i=1 are ‘squeezed’ into the interval [0, 1] by dividing
of n + 1.
Now, let us assume that our outcome observations Yi’s are supposed to be measured at
some unknown time points Zi,1’s. However, due to some measurement imprecision or some
outer random inﬂuence, the actual observation Yi, which should correspond to Zi,1, is not
recorded at time point Zi,1, but at time point Xi,1. One can imagine a long-distance time
trial against the chronometer (e.g., an individual competition in cross-country skiing).
There are n intermediate spots on the track, where the athlete’s time is recorded. If we


## Page 17


Changepoint in Linear Relations
17
think of one particular athlete, we measure at the intermediate spot i her/his error-prone
competition time Xi,1, which was encumbered by some randomness, instead of the true
unobservable time is Zi,1.
This is because each race is speciﬁc and every athlete has
a unique performance during that particular race. We also observe a time lag Yi between
her/him and the current leader at that spot. Now, one is interested whether there is
a change in linear trend. This would help to analyze whether the particular athlete tried
to improve or not during the time trial. One can argue that a distance of the intermediate
spot should be taken into account instead of the athlete’s intermediate time. However,
the intermediate distance is also measured with error, for instance, a rounded value of the
true unobserved distance is provided. Another example of randomly spaced time series is
a case when the observation times are driven by the series itself. For instance, cumulative
counts of occurrences of a disease in a given area (Wright, 1986).
The unobservable sequence {Zi,1}n
i=1 can be regularly or irregularly spaced. The key
issue is to have satisﬁable Assumption D. Since the developed detection procedures rely
on the orthogonal regression, it is suﬃcient to transform the original randomly spaced time
series {Xi,1, Yi}n
i=1 into, e.g., {Xi,1/(maxi{|Xi,1|} + ϵ), Yi/(maxi{|Xi,1|} + ϵ)}n
i=1, where
a constant ϵ is reasonably large. Afterwards, the proposed tests remain valid when applied
to the transformed randomly spaced time series, because β stays unchanged after such
a transformation. Hence, one can test whether the linear trend has or has not changed
over time.
7.
Conclusions
Our changepoint problem in linear relations is linearly deﬁned, but comes with a highly
non-linear solution and inference. We have proposed two tests for changepoints with de-
sirable theoretical properties: The asymptotic size of the tests is guaranteed by a limit
theorem even under non-stationarity and weak dependency, the tests and the related
changepoint estimator are consistent. We are not aware of any similar results even for
independent and identically distributed errors. By combining self-normalization and the
proposed spectral weak invariance principle, there are neither tuning constants nor nui-
sance parameters involved in the whole testing procedure. Therefore, the detection meth-
ods are completely data-driven, which makes this framework eﬀortlessly applicable as
demonstrated. In our simulations, the tests show reliable performance.
A.
Proofs
Proof of Proposition 3.1. Let the singular value decomposition of the transformed ‘partial’
data matrix be
[X[nt], Y[nt]]Σ−1/2 = U(t)Γ(t)V (t)⊤=
p+1
X
i=1
ς(t)(i)u(t)(i)v(t)(i)⊤
for some t ∈(0, 1]. Note that we are in a situation of no change in the parameter β.
Bearing in mind Assumptions D and E, Gleser (1981, Lemma 2.1) and Peˇsta (2011,
Theorem 3.1) provide that 0 ̸= vp+1(t)(p+1) (i.e., the last element of the last right-singular


## Page 18


18
M. Peˇsta
vector v(t)(p+1) corresponding to the smallest singular value) with probability tending to
one as n increases. According to Gleser (1981, proof of Lemma 4.2), one gets
1
√n

λ[nt] −[nt]σ2
=

vp+1(t)(p+1)2
[a⊤
t , −1]
 1
√n (Dt −E Dt)
  at
−1

(A.1)
+

vp+1(t)(p+1)2√n[a⊤
t , −1]Σ−1/2
 Ip
β⊤
 1
nZ⊤
[nt]Z[nt][Ip, β]Σ−1/2
 at
−1

,
(A.2)
where at := ( ˜
X⊤
[nt] ˜
X[nt] −λ[nt]Ip)−1 ˜
X⊤
[nt] ˜Y[nt] is the TLS estimator for the transformed
data [ ˜
X[nt], ˜Y[nt]] := [X[nt], Y[nt]]Σ−1/2 and Dt := Σ−1/2[X[nt], Y[nt]]⊤[X[nt], Y[nt]]Σ−1/2.
With respect to Peˇsta (2011), we have

vp+1(t)(p+1)2
= 1 −



[v1(t)(p+1), . . . , vp(t)(p+1)]⊤


2
2 →
1
1 + ∥α∥2
2
almost surely as n →∞. Moreover, √n(at −α) = OP(1) as n →∞by Peˇsta (2013a).
The strong law of large numbers for α-mixing by Chen and Wu (1989) together with
Theorem 3.1 by Peˇsta (2011) lead to at −α = o(1) almost surely. Since Assumption D
holds, the expression in (A.2) is oP(1). Furthermore, the expression on the right hand
side of (A.1) is o(1) away from
1
1 + ∥α∥2
2
[α⊤, −1]
 1
√n (Dt −E Dt)
  α
−1

(A.3)
as n →∞. Hence, the process from the left hand side of (A.1) in D[0, 1] has approximately
the same distribution as the process (A.3).
Note that
[α⊤, −1]Dt
 α
−1

= (¯Σε −¯Σ⊤
Θ,εα)2

Y[nt] −X[nt]β


2
2.
Using the functional central limit theorem for α-mixing by Herrndorf (1983) or Lin and
Lu (1997, Corollary 3.2.1) in an analogous fashion as in the proof of Theorem 2.3 by Peˇsta
(2013a), one gets

[α⊤, −1]
 1
√n (Dt −E Dt)
  α
−1

t∈[0,1]
D[0,1]
−−−→
n→∞{φ2υW(t)}t∈[0,1]
due to Assumption V.
Similarly for
n
1
√n

eλ[n(1−t)] −[n(1 −t)]σ2o
t∈[0,1] and { f
W(t)}t∈[0,1].
Proof of Theorem 4.1. The spectral weak invariance principle from Proposition 3.1 and
Lemma 1 by Peˇsta and Wendler (2019) in combination with the continuous mapping
device complete the proof.
Proof of Theorem 4.2. Under HA, let us ﬁnd a lower bound for the smallest eigenvalue of
the positive semi-deﬁnite matrix
1
nΣ−1/2[X, Y ]⊤[X, Y ]Σ−1/2 = 1
n
" ˜
X⊤˜
X
˜
X⊤˜Y
˜Y ⊤˜
X
˜Y ⊤˜Y
#
=:
A
c
c⊤
d

,
(A.4)


## Page 19


Changepoint in Linear Relations
19
where [ ˜
X, ˜Y ] := [X, Y ]Σ−1/2. With respect to Dembo (1988, Theorem 1), we get
λmin
A
c
c⊤
d

≥d + ℓ
2
−
s
(d −ℓ)2
4
+ c⊤c,
(A.5)
where ℓis any lower bound on the smallest eigenvalue of the matrix A.
Recall that
Assumption E and the proof of Theorem 3.1 by Peˇsta (2011) provide
1
n ˜ε⊤˜ε →σ2, 1
n
˜Θ⊤˜ε →0, 1
n
˜Θ⊤˜Θ →σ2Ip, 1
n
˜Z⊤˜ε →0, 1
n
˜Z⊤˜Θ →0
(A.6)
almost surely as n →∞, where [ ˜Θ, ˜ε] := [Θ, ε]Σ−1/2 and ˜Z := Z[Ip, β]
" ¯ΣΘ
¯Σ⊤
Θ,ε
#
. By
Assumptions C and D, one can obtain
λ(A)min = λmin
 1
n( ˜Z + ˜Θ)⊤( ˜Z + ˜Θ)

→λmin
 
[ ¯ΣΘ, ¯ΣΘ,ε]
 Ip
β⊤

∆[Ip, β]
" ¯ΣΘ
¯Σ⊤
Θ,ε
#
+ σ2Ip
!
= σ2 + η
(A.7)
almost surely as n →∞. Relation (A.7) immediately provides a limit of a candidate for ℓ.
Now, (A.4) and (A.5) lead to
lim inf
n→∞λmin
 1
nΣ−1/2[X, Y ]⊤[X, Y ]Σ−1/2

≥
lim
n→∞
1
n
˜Y ⊤˜Y + σ2 + η
2
−
v
u
u
u
t

lim
n→∞
1
n
˜Y ⊤˜Y −σ2 −η
2
4
+ lim
n→∞




1
n
˜
X⊤˜Y




2
2
.
(A.8)
Assumptions C, D, and relations (A.6) yield
1
n
˜Y ⊤˜Y = 1
n
˜Y ⊤
τ ˜Yτ + 1
n
˜Y ⊤
−τ ˜Y−τ = ( ¯Σ⊤
Θ,ε + ¯Σεβ⊤)∆ζ( ¯ΣΘ,ε + β¯Σε)
+ σ2 + ( ¯Σ⊤
Θ,ε + ¯Σε(β + δ)⊤)∆−ζ( ¯ΣΘ,ε + (β + δ)¯Σε) + o(1) = κ + σ2 + o(1)
and
1
n
˜
X⊤˜Y = 1
n
˜
X⊤
τ ˜Yτ + 1
n
˜
X⊤
−τ ˜Y−τ = ( ¯ΣΘ + ¯ΣΘ,εβ⊤)∆ζ( ¯ΣΘ,ε + β¯Σε)
+ ( ¯ΣΘ + ¯ΣΘ,ε(β + δ)⊤)∆−ζ( ¯ΣΘ,ε + (β + δ)¯Σε) + o(1) = ϕ + o(1)
almost surely as n →∞. Thus,
1
n ˜Y ⊤˜Y + σ2 + η
2
−
v
u
u
t
  1
n ˜Y ⊤˜Y −σ2 −η
2
4
+




1
n
˜
X⊤˜Y




2
2
=
κ + η −
q
(κ −η)2 + 4ϕ⊤
2 ϕ2
2
+ σ2 + o(1)
(A.9)


## Page 20


20
M. Peˇsta
almost surely as n →∞. Hence, combining (A.8) and (A.9) ends up with
lim inf
n→∞λmin
 1
n[ ˜
X, ˜Y ]⊤[ ˜
X, ˜Y ]

−σ2 ≥lim
n→∞
2{ηκ −ϕ⊤ϕ}
κ + η +
q
(κ −η)2 + 4ϕ⊤ϕ
.
Then,
1
√n|λn −nσ2| a.s.
−−−→
n→∞∞
(A.10)
by Assumption C.
With respect to Assumptions D, E, V and according to the underlying proof of The-
orem 4.1,
1
√n max1≤i<τ
λi −i
τ λτ
 and
1
√n maxτ<i≤n
eλi −n−i
n−τ eλτ
 are OP(1) as n →∞.
Moreover,
1
√n
λτ −τσ2 = OP(1) as n →∞due to Proposition 3.1.
Note that there are no changes in the linear parameter corresponding to the ﬁrst τ
observations as well as to the last (remaining) n −τ observations. Let k = τ. Thus,
under HA,
Sn ≥
λτ −τ
nλn

max1≤i<τ
λi −i
τ λτ
 + maxτ<i≤n
eλi −n−i
n−τ eλτ

≥
1
√n

λτ −τσ2 −τ
n
nσ2 −λn


1
√n max1≤i<τ
λi −i
τ λτ
 +
1
√n maxτ<i≤n
eλi −n−i
n−τ eλτ

P
−−−→
n→∞∞,
because of (A.10).
Furthermore, again under HA,
Tn ≥
 λτ −τ
nλn
2
Pτ−1
i=1
 λi −i
τ λτ
2 + Pn
i=τ+1
 eλi −n−i
n−τ eλτ
2
≥
1
n
λτ −τσ2 −τ
n
nσ2 −λn

2
1
n
Pτ−1
i=1
 λi −i
τ λτ
2 + 1
n
Pn
i=τ+1
 eλi −n−i
n−τ eλτ
2
P
−−−→
n→∞∞,
because of similar arguments as in the case of Sn.
Proof of Remark 4.3. It is suﬃcient to replace Theorem 1 by Dembo (1988) with Theo-
rem 3.1 by Ma and Zarowski (1995) in the proof of Theorem 4.2.
Proof of Corollary 4.4. The estimator can be rewritten as
ˆτn = argmax
1≤k≤n−1
1
n
λk −k
nλn
 + 1
n
eλk −n−k
n eλ0

max1≤i<k
1
√n
λi −i
kλk
 + maxk<i≤n
1
√n
eλi −n−i
n−k eλk
.
(A.11)
We will treat the numerator Nn(k) and the denominator Dn(k) of the above stated ratio
separately. Let us use notations from the previous proofs and let us recall Assumption C,
D, and relations (A.6). If [nt] ≤τ, then
1
n
˜Y ⊤
[nt] ˜Y[nt] = ( ¯Σ⊤
Θ,ε + ¯Σεβ⊤)∆t( ¯ΣΘ,ε + β¯Σε) + tσ2 + o(1)


## Page 21


Changepoint in Linear Relations
21
almost surely as n →∞. Otherwise, if [nt] > τ, then
1
n
˜Y ⊤
[nt] ˜Y[nt] = ( ¯Σ⊤
Θ,ε + ¯Σεβ⊤)∆ζ( ¯ΣΘ,ε + β¯Σε) + tσ2
+ ( ¯Σ⊤
Θ,ε + ¯Σε(β + δ)⊤)(∆t −∆ζ)( ¯ΣΘ,ε + (β + δ)¯Σε) + o(1)
almost surely as n →∞. In both cases, we have
1
n[ ˜
X[nt], ˜Y[nt]]⊤[ ˜
X[nt], ˜Y[nt]]
a.s.
−−−→
n→∞
"
ϑ⊤∆tϑ + tσ2Ip
( ¯ΣΘ + ¯ΣΘ,εβ⊤)∆t( ¯ΣΘ,ε + β¯Σε)
( ¯Σ⊤
Θ,ε + ¯Σεβ⊤)∆t( ¯ΣΘ + β¯Σ⊤
Θ,ε)
( ¯Σ⊤
Θ,ε + ¯Σεβ⊤)∆t( ¯ΣΘ,ε + β¯Σε) + tσ2
#
= tσ2Ip+1 + Σ−1/2
 Ip
β⊤

∆t[Ip, β]Σ−1/2.
Therefore, for the Frobenius matrix norm ∥· ∥F,
lim
n→∞
λmin
 1
n[ ˜
X[nt], ˜Y[nt]]⊤[ ˜
X[nt], ˜Y[nt]]

−[nt]
n λmin
 1
n[ ˜
X, ˜Y ]⊤[ ˜
X, ˜Y ]
 
=: λdif(t) ≤




Σ−1/2
 Ip
β⊤

∆−t[Ip, β]Σ−1/2




F
uniformly in t almost surely, because |λmin(A) −λmin(B)| ≤∥A −B∥F due to Gallo
(1982b, proof of Lemma 2.3).
For k = τ, Proposition 3.1 together with the continuous mapping theorem yield that
the denominator from (A.11)
Dn(τ)
D
−−−→
n→∞
φ2υ
1 + ∥α∥2
2

sup
0≤t≤ζ
W(t) −t
ζ W(ζ)
 + sup
ζ<t≤1
 f
W(t) −1 −t
1 −ζ
f
W(ζ)


=: W,
where the limit W is strictly positive almost surely. We conclude that |Nn(τ)/Dn(τ)|
converge in distribution to the random variable λdif(ζ) + eλdif(ζ)/W such that eλdif(t) :=
limn→∞|eλ[nt] −n−[nt]
n
eλ0|. For k = [nt] with t > ζ, we obtain
max
1≤i<[nt]
1
√n
λi −
i
[nt]λ[nt]
 +
max
[nt]<i≤n
1
√n
eλi −
n −i
n −[nt]
eλ[nt]

≥
1
√n
λ[nζ] −[nζ]
[nt] λ[nt]
 ≥
1
√n

λ[nζ] −[nζ]σ2
 −[nζ]
[nt]
λ[nt] −[nt]σ2


≈
OP(1) −√nζ
t

λ[nt]
n
−tσ2


≈
OP(1) −2√nζ
t
η(t)κ(t) −ϕ(t)⊤ϕ(t)

κ(t) + η(t) +
q
(κ(t) −η(t))2 + 4ϕ(t)⊤ϕ(t)

P
−−−→
n→∞∞


## Page 22


22
M. Peˇsta
according to the proof of Theorem 4.2 and assumption (4.10). Similar arguments can
be applied in the case t < ζ and the convergence holds uniformly for all t outside any
ϵ-neighborhood of ζ. It follows that for an arbitrary ϵ > 0,
max
k:|k−τ|≥nϵ
|Nn(k)|
Dn(k) = OP

1
|η(t)κ(t) −ϕ(t)⊤ϕ(t)|√n

.
Now, let us chose a sequence dn →0 with dn|η(t)κ(t) −ϕ(t)⊤ϕ(t)|√n →∞. Then, for
any ϵ > 0,
P[|ˆτ/n −ζ| > ϵ] ≤P[|Nn(τ)/Dn(τ)| < dn] + P

max
k:|k−τ|≥nϵ |Nn(k)/Dn(k)| > dn

n→∞
−−−→0.
Acknowledgements
The research of Michal Peˇsta was supported by the Czech Science Foundation project
GAˇCR No. 18-01781Y.
References
Anderson, T. W. (1958). An Introduction to Multivariate Statistical Analysis. New York,
NY: John Wiley & Sons.
Aue, A., L. Horv´ath, M. Huˇskov´a, and P. Kokoszka (2008). Testing for changes in poly-
nomial regression. Bernoulli 14(3), 637–660.
Aue, A., L. Horv´ath, and M. Huˇskov´a (2009). Extreme value theory for stochastic integrals
of Legendre polynomials. J. Multivariate Anal. 100(5), 1029–1043.
Billingsley, P. (1968). Convergence of Probability Measures (1st ed.). New York, NY: John
Wiley & Sons.
Bland, J. M. and D. G. Altman (1986).
Statistical methods for assessing agreement
between two methods of clinical measurement. Lancet 1(8476), 307–310.
Booth, J. G. and P. Hall (1993). Bootstrap conﬁdence regions for functional relationships
in errors-in-variables models. Ann. Stat. 21(4), 1780–1791.
Bradley, R. C. (2005). Basic properties of strong mixing conditions. A survey and some
open questions. Probab. Surveys 2, 107–144.
Buonaccorsi, J. P. (2010). Measurement Error: Models, Methods, and Applications. Boca
Raton, FL: Chapman and Hall/CRC.
Carroll, R. J., K. Roeder, and L. Wasserman (1999). Flexible parametric measurement
error models. Biometrics 55(1), 44–54.
Carroll, R. J., D. Ruppert, L. A. Stefanski, and C. M. Crainiceanu (2006). Measurement
Error in Nonlinear Models: A Modern Perspective (2nd ed.). Boca Raton, FL: Chapman
and Hall/CRC.
Chang, Y.-P. and W.-T. Huang (1997). Inferences for the linear errors-in-variables with
changepoint models. J. Am. Stat. Assoc. 92(437), 171–178.


## Page 23


Changepoint in Linear Relations
23
Chen, X. and Y. Wu (1989). Strong law for mixing sequence. Acta Math. Appl. Sin. 5(4),
367–371.
Cheng, C.-L. and J. Riu (2006). On estimating linear relationships when both variables
are subject to heteroscedastic measurement errors. Technometrics 48(4), 511–519.
Dembo, A. (1988). Bounds on the extreme eigenvalues of positive-deﬁnite Toeplitz ma-
trices. IEEE T. Inform. Theory 34(2), 352–355.
Dong, C., C. Tan, B. Jin, and B. Miao (2016). Inference on the change point estimator
of variance in measurement error models. Lith. Math. J. 56(4), 474–491.
Fryzlewicz, P. (2014).
Wild binary segmentation for multiple change-point detection.
Ann. Stat. 42(6), 2243–2281.
Fuller, W. A. (1987). Measurement Error Models. New York, NY: Wiley.
Gallo, P. P. (1982a). Consistency of regression estimates when some variables are subject
to error. Commun. Stat. A-Theor. 11, 973–983.
Gallo, P. P. (1982b). Properties of Estimators in Errors-in-Variables Models. Ph. D.
thesis, University of North Carolina, Chapel Hill, NC.
Gleser, L. J. (1981). Estimation in a multivariate “errors in variables” regression model:
Large sample results. Ann. Stat. 9, 24–44.
Gleser, L. J. and G. S. Watson (1973).
Estimation of a linear transformation.
Biometrika 60(3), 525–534.
Golub, G. H. and C. F. Van Loan (1980). An analysis of the total least squares problem.
SIAM J. Numer. Anal. 17(6), 883–893.
G¨ossl, C. and H. K¨uchenhoﬀ(2001).
Bayesian analysis of logistic regression with an
unknown change point and covariate measurement error. Statist. Med. 20(20), 3109–
3121.
Guo, Y. and R. J. Little (2011).
Regression analysis with covariates that have het-
eroscedastic measurement error. Statist. Med. 30, 2278–2294.
Herrndorf, N. (1983). Stationary strongly mixing sequences not satisfying the central limit
theorem. Ann. Probab. 11(3), 809–813.
Horv´ath, L. (1995). Detecting changes in linear regressions. J. Am. Stat. Assoc. 26(3),
189–208.
Ibragimov, I. A. and Y. V. Linnik (1971).
Independent and Stationary Sequences of
Random Variables. The Netherlands: Wolters-Noordhoﬀ.
Kirch, C. (2006). Resampling Methods for the Change Analysis of Dependent Data. Ph.
D. thesis, University of Cologne, Germany.
Kukush,
A.,
I. Markovsky,
and S. Van Huﬀel (2007).
Estimation in a linear
multivariate measurement error model with a change point in the data.
Com-
put. Stat. Data An. 52(2), 1167–1182.
Li, M., Y. Ma, and R. Li (2019). Semiparametric regression for measurement error model
with heteroscedastic error. J. Multivariate Anal. 171(2019), 320–338.


## Page 24


24
M. Peˇsta
Lin, Z. and C. Lu (1997). Limit Theory for Mixing Dependent Random Variables. New
York, NY: Springer-Verlag.
Lord, F. M. (1973). Testing if two measuring procedures measure the same dimension.
Psychol. Bull. 79(1), 71–72.
Ma, E. M. and C. J. Zarowski (1995). On lower bounds for the smallest eigenvalue of
a Hermitian positive-deﬁnite matrix. IEEE T. Inform. Theory 41(2), 539–540.
Nussbaum, M. (1977). Asymptotic optimality of estimators of a linear functional relation
if the ratio of the error variances is known. Statistics 8(2), 173–198.
Peˇsta, M. (2011). Strongly consistent estimation in dependent errors-in-variables. Acta
Universitatis Carolinae. Mathematica et Physica 52(1), 69–79.
Peˇsta, M. (2013a).
Asymptotics for weakly dependent errors-in-variables.
Kyber-
netika 49(5), 692–704.
Peˇsta, M. (2013b). Total least squares and bootstrapping with application in calibration.
Statistics 47(5), 966–991.
Peˇsta, M. (2016). Unitarily invariant errors-in-variables estimation. Stat. Pap. 57(4),
1041–1057.
Peˇsta, M. (2017). Block bootstrap for dependent errors-in-variables. Commun. Stat. A-
Theor. 46(4), 1871–1897.
Peˇsta, M. and M. Wendler (2019).
Nuisance-parameter-free changepoint detection in
non-stationary series. TEST, doi.org/10.1007/s11749–019–00659–1, Online First.
Rosenblatt, M. (1971). Markov Processes: Structure and Asymptotic Behavior. Berlin:
Springer-Verlag.
Ryu, S.-J. and H.-K. Lee (2014). Estimation of linear transformation by analyzing the
periodicity of interpolation. Pattern Recogn. Lett. 36(2014), 89–99.
Shao, X. and X. Zhang (2010). Testing for change points in time series. J. Am. Stat. As-
soc. 105(491), 1228–1240.
Staudenmayer, J. and D. Spiegelman (2002). Segmented regression in the presence of
covariate measurement error in main study/validation study designs. Biometrics 58(4),
871–877.
Stefanski, L. A. (2000). Measurement error models. J. Am. Stat. Assoc. 95(452), 1353–
1358.
Van Huﬀel, S. and J. Vandewalle (1989). Analysis and properties of the generalized total
least squares problem AX ≈B when some or all columns in A are subject to error.
SIAM J. Matrix Anal. Appl. 10(3), 294–315.
Van Huﬀel, S. and J. Vandewalle (1991). The Total Least Squares Problem: Computational
Aspects and Analysis. Philadelphia, PA: SIAM.
Wright, D. J. (1986).
Forecasting data published at irregular time intervals using an
extension of holt’s method. Manage. Sci. 32(4), 499–510.
Yi, G. Y. (2017). Statistical Analysis with Measurement Error or Misclassiﬁcation. New
York, NY: Spriger.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]