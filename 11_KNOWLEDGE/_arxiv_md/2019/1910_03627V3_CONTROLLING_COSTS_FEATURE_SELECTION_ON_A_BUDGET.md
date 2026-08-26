---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.03627v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1910.03627v3_Controlling_Costs__Feature_Selection_on_a_Budget

> Source: 1910.03627v3_Controlling_Costs__Feature_Selection_on_a_Budget.pdf

> Pages: 23

---


## Page 1


Controlling Costs: Feature Selection on a Budget
Guo Yu∗
Daniela Witten†
Jacob Bien‡
Abstract
The traditional framework for feature selection treats all features as costing the
same amount. However, in reality, a scientist often has considerable discretion regard-
ing which variables to measure, and the decision involves a tradeoﬀbetween model
accuracy and cost (where cost can refer to money, time, diﬃculty, or intrusiveness).
In particular, unnecessarily including an expensive feature in a model is worse than
unnecessarily including a cheap feature. We propose a procedure, which we call cheap
knockoﬀs, for performing feature selection in a cost-conscious manner. The key idea
behind our method is to force higher cost features to compete with more knockoﬀs
than cheaper features.
We derive an upper bound on the weighted false discovery
proportion associated with this procedure, which corresponds to the fraction of the
feature cost that is wasted on unimportant features. We prove that this bound holds
simultaneously with high probability over a path of selected variable sets of increasing
size. A user may thus select a set of features based, for example, on the overall budget,
while knowing that no more than a particular fraction of feature cost is wasted. We
investigate, through simulation and a biomedical application, the practical importance
of incorporating cost considerations into the feature selection process.
1
Introduction
The traditional framework for feature selection ignores the fact that, in practice, diﬀerent
features may have diﬀerent costs. In reality, practitioners must balance the opposing de-
mands of model accuracy and budget considerations. For example, as we will see in Section
4, in medical diagnosis, doctors often have a wide range of options for what features to
measure: a laboratory result may provide highly relevant information yet is expensive in
terms of money, time, and the burden on patients; a simple questionnaire or even demo-
graphic information may be less informative but incurs lower costs. When a questionnaire
∗Department of Statistics and Applied Probability, University of California Santa Barbara, Santa Barbara,
California, 93110, guoyu@ucsb.edu
†Department of Statistics and Biostatistics, University of Washington, Seattle, Washington, 98195, dwit-
ten@uw.edu
‡Department of Data Sciences and Operations, Marshall School of Business, University of Southern
California, Los Angeles, CA 90089, jbien@usc.edu
1
arXiv:1910.03627v3  [stat.ME]  11 Feb 2023


## Page 2


would suﬃce for forming an accurate diagnosis, performing a laboratory examination would
be practically misguided. Likewise, how should we decide whether to sequence a patient’s
entire genome or simply to conduct some cheap lab tests? This same challenge appears in
other domains. For example, to determine the veracity of an online news article, do we re-
quire high-quality features based on an expert’s reading, or do features derived from natural
language processing suﬃce?
Consider the response of interest Y and a set of features X1, . . . , Xp, where for each
feature Xj, there is an associated cost ωj > 0. In this paper, we consider a very general
model where Y |X1, . . . , Xp follows an arbitrary distribution, and we assume that the joint
distribution of X1, . . . , Xp is known. Let H0 be the set of irrelevant features, i.e., j ∈H0 if
and only if Xj is independent of Y conditional on the other variables {Xk : k ̸= j} (Deﬁnition
1 in Candes et al., 2018). Given a set of selected features R ⊆{1, . . . , p}, the false discovery
proportion (FDP) is deﬁned as |R ∩H0|/|R|, i.e., it is the fraction of selected features that
are unnecessarily included.
Barber and Cand`es (2015) proposed the knockoﬀﬁlter, a feature selection procedure
that provably controls the false discovery rate, deﬁned as E(FDP). For each feature, they
construct a knockoﬀfeature, i.e., a carefully constructed fake copy of that feature. A feature
is then only selected if it shows considerably more association with the response than its
knockoﬀcounterpart. Katsevich and Ramdas (2018) showed that one can directly upper-
bound the false discovery proportion, with high probability, simultaneously for an entire
path of selected models, R1, . . . , Rp, where Rk ⊆Rk+1 for all k.
However, the false discovery proportion and the false discovery rate put all features on
an equal footing, and do not consider their costs ω1, . . . , ωp. To overcome this shortcoming,
the weighted false discovery proportion (wFDP; Benjamini and Hochberg 1997) is deﬁned
as wFDP(R) = C(R ∩H0)/C(R), i.e., the fraction of the total cost that is wasted, where
C(A) = P
j∈A ωj is the cost of measuring the features in A.
The weighted false discovery proportion and weighted false discovery rate are not new
(Benjamini and Hochberg, 1997; Benjamini and Heller, 2007), and the Benjamini-Hochberg
procedure (Benjamini and Hochberg, 1995) has been generalized to the weighted false dis-
covery rate setting. A related criterion is the penalty-weighted false discovery rate (Ram-
das et al., 2019), which can be controlled with the p-ﬁlter. However, the aforementioned
procedures only provably control the corresponding criteria under restrictive dependence as-
sumptions on the p-values (Benjamini and Yekutieli, 2001). Under arbitrary dependence, the
reshaping process (Benjamini and Yekutieli, 2001; Blanchard and Roquain, 2008; Ramdas
et al., 2019) needs to be applied, which can greatly reduce power. Basu et al. (2018) proposed
a procedure that has asymptotic control of a related quantity, namely E[C(R∩H0)]/E[C(R)],
in a mixture model under certain regularity conditions.
In this work, we adapt the ideas of knockoﬀs (Barber and Cand`es, 2015) and simultaneous
inference (Goeman and Solari, 2011; Katsevich and Ramdas, 2018) to the setting where
features have costs. The key to our method, which we call cheap knockoﬀs, is to construct
multiple knockoﬀs for each feature, with more expensive features having more knockoﬀs. A
feature is selected only if it beats all of its knockoﬀcounterparts; thus, costlier features have
2


## Page 3


more competition. This procedure yields a path of selected feature sets R1, . . . , Rp for which
wFDP(Rk) is bounded by a certain computable quantity with high probability, regardless
of how k is chosen. Unlike existing work on weighted false discovery rate control (Benjamini
and Hochberg, 1997; Benjamini and Heller, 2007; Ramdas et al., 2019), our method provably
bounds the weighted false discovery proportion under arbitrary dependence among features.
Yu et al. (2021) recently proposed a predictive modeling method in high-dimensional cost-
constrained linear regression problems. Diﬀerent from their focus which is on good prediction
performance under budget constraints, our method aims at recovering the true set of features
(as deﬁned in HC
0 ) with wFDP control.
2
Cheap knockoﬀs
2.1
A review of model-X knockoﬀs and simultaneous inference
Our method is based on the model-X knockoﬀprocedure (Candes et al., 2018) and its
multiple knockoﬀextension (Roquero Gimenez and Zou, 2018), which provably control the
false discovery rate for arbitrary sample size n and number of features p. For simplicity, we
focus on the following linear model setting
E [Y |X1, . . . , Xp] =
p
X
j=1
βjXj,
(X1, . . . , Xp)T ∼N(0, Σ).
(1)
We start by brieﬂy reviewing the model-X knockoﬀapproach in the simultaneous infer-
ence setting, applied speciﬁcally in the linear model (1). Throughout this paper, we denote
X ∈Rn×p as a data matrix, and y ∈Rn as a response vector, where (Xi1, . . . , Xip, yi) ∈
Rp × R are independently and identically distributed as (X1, . . . , Xp, Y ) for i = 1, . . . , n.
1. For each variable Xj, construct a knockoﬀvariable ˜Xj that satisﬁes:
(a) E( ˜Xj) = E(Xj);
(b) Cov( ˜Xj, ˜Xk) = Cov(Xj, Xk) for all k;
(c) Cov( ˜Xj, Xk) = Cov(Xj, Xk) −sj1{j = k} for some sj ≥0.
The knockoﬀvariables ˜X = ( ˜X1, . . . , ˜Xp) are constructed to resemble X without any
knowledge of the response Y . We denote ˜X ∈Rn×p as the constructed knockoﬀmatrix
of X in a way that ( ˜Xi1, . . . , ˜Xip) is a knockoﬀof (Xi1, . . . , Xip) for i = 1, . . . , n.
2. For each j ∈{1, . . . , p}, compute statistics Tj and ˜Tj for the variables Xj and ˜Xj,
respectively.
For example, these could be the absolute values of the coeﬃcients of
a lasso regression (Tibshirani, 1996) on the augmented design matrix Z = [X, ˜X] ∈
Rn×2p:
ˆθ(λ) = arg min
θ∈R2p
1
2 ∥y −Zθ∥2
2 + λ ∥θ∥1

,
(2)
3


## Page 4


with Tj = |ˆθ(λ)j| and ˜Tj = |ˆθ(λ)j+p|. The value of λ can be ﬁxed in advance, or selected
using cross-validation. The knockoﬀstatistics are then deﬁned as Wj = Tj−˜Tj. Barber
and Cand`es (2015) and Candes et al. (2018) discuss other choices of Tj’s and Wj’s.
Intuitively, a large value of Wj indicates that Xj is a genuine signal variable, i.e., the
distribution of Y depends on Xj, whereas a small or negative value of Wj indicates
that Xj may be irrelevant.
3. For any ordering of variables σ(1), . . . , σ(p), e.g., |Wσ(1)| ≥|Wσ(2)| ≥. . . ≥|Wσ(p)|,
report the sets of selected variables Rk =

σ(j) : σ(j) ≤σ(k), Wσ(j) > 0
	
, for k ∈
{1, . . . , p}.
Katsevich and Ramdas (2018) work within the simultaneous inference framework (Goe-
man and Solari, 2011), in which a practitioner wishes to obtain a ﬁnal set of selected variables
with false discovery proportion control when choosing among {Rk, k = 1, . . . , p}. To allow
for such behavior, Katsevich and Ramdas (2018) form a computable upper bound Uk such
that FDP(Rk) ≤Uk holds simultaneously over all k with some known probability.
2.2
Multiple knockoﬀs based on cost
The knockoﬀprocedure described in the previous section constructs a single knockoﬀvari-
able for each feature, and then selects features based solely on the values of W1, . . . , Wp.
Barber and Cand`es (2015) and Candes et al. (2018) discuss the possibility of constructing
K knockoﬀs per feature for some value K > 1 with the goal of achieving higher statistical
power and stability. This has been pursued in Roquero Gimenez and Zou (2018) and Emery
et al. (2019).
We make a simple yet crucial modiﬁcation to the multiple knockoﬀs idea, allowing diﬀer-
ent features to have diﬀerent numbers of knockoﬀs, so that an expensive irrelevant feature
will have a lower chance of entering the model than a cheap irrelevant feature. Assume that
the feature costs ω1, . . . , ωp are integers with ωj ≥2. We construct ωj −1 knockoﬀvariables
for each original variable Xj. If Xj is irrelevant, i.e., j ∈H0, then we expect it to be selected
with probability 1/ωj. We also incorporate costs into the construction of the sequence of
selected feature sets Rk. The cheap knockoﬀprocedure generalizes the multiple knockoﬀ
procedure of Roquero Gimenez and Zou (2018) to the cost-conscious setting:
1. For each variable Xj with cost ωj, denote ˜X(1)
j
= Xj and construct the knockoﬀ
variables ˜X(2)
j , ˜X(3)
j , . . . , ˜X
(ωj)
j
such that:
(a) E( ˜X(ℓ)
j ) = E(Xj) for ℓ∈{2, . . . , ωj}.
(b) Cov( ˜X(ℓ)
j , ˜X(m)
k
) = Cov(Xj, Xk) −sj1{j = k}1{ℓ̸= m} for all ℓ∈{1, . . . , ωj},
m ∈{1, . . . , ωk}, j, k ∈{1, . . . , p}, and some constant sj ≥0.
We denote ˜X(ℓ)
j
∈Rn as the constructed knockoﬀvariables of Xj, such that ( ˜X(ℓ)
ij )
ℓ=1,...,ωj
j=1,...,p
satisﬁes the condition above for (Xij)j=1,...,p for i = 1, . . . , n.
4


## Page 5


2. For each j ∈{1, . . . , p}, compute the statistics T (1)
j
(corresponding to the original
variable) and T (2)
j , . . . , T
(ωj)
j
(corresponding to the ωj −1 knockoﬀvariables).
For
example, these could be the absolute values of the coeﬃcients of the following lasso
regression:
{ˆθ(ℓ)
j (λ)}j≤p,ℓ≤ωj =
arg min
θ(ℓ)
j
:j≤p,ℓ≤ωj

1
2





y −
p
X
j=1
ωj
X
ℓ=1
˜X(ℓ)
j θ(ℓ)
j





2
2
+ λ
p
X
j=1
ωj
X
ℓ=1
|θ(ℓ)
j |

,
(3)
with T (ℓ)
j
= |ˆθ(ℓ)
j (λ)|. The value of λ in (3) can be selected using cross-validation. We
deﬁne
κj = arg max
1≤ℓ≤ωj
T (ℓ)
j .
(4)
3. For any ordering of variables σ(1), . . . , σ(p), report the sets of selected variables Rk =

σ(j) : σ(j) ≤σ(k), κσ(j) = 1
	
, for k ∈{1, . . . , p}.
In Step 1, various methods are available for constructing multiple knockoﬀs given that
the distribution of X is known (see, e.g., Candes et al., 2018; Roquero Gimenez and Zou,
2018). The computation of κj in Step 2 involves the ωj statistics T (1)
j , . . . , T
(ωj)
j
; κj = 1
indicates that the original variable beats all of its ωj −1 knockoﬀcopies.
We show in
the supplementary material that the probability of this occurring for an irrelevant feature
is inversely proportional to the feature’s cost. This is the key property used to show the
simultaneous control of the weighted false discovery proportion in the next section.
In principle, any ordering of variables can be used to obtain Rk. In simulations, we
consider a speciﬁc ordering such that τσ(1) ≥τσ(2) . . . ≥τσ(p), where τj = 2ω−1
j {T
(κj)
j
−
maxℓ̸=κj T (ℓ)
j }. One reason for this speciﬁc choice of τj is that when ω1 = . . . = ωp = 2, the
above procedure is exactly the same as the standard knockoﬀprocedure reviewed in Section
2.1. In particular, Wj > 0 if and only if κj = 1, and |Wj| = τj. Moreover, all else being
equal, we want to make use of cheap features over expensive features. For this reason, we
set τj to be inversely proportional to the feature cost.
2.3
Simultaneous control of the weighted false discovery propor-
tion
Having constructed a cost-conscious path of selected variable sets R1, . . . , Rp, we next
provide a simultaneous high-probability bound on the weighted false discovery proportion
along this path. The next theorem and the remark that follows establish that the com-
putable quantities ¯U(R1, c), . . . , ¯U(Rp, c), deﬁned below in (7), simultaneously upper bound
wFDP(R1), . . . , wFDP(Rp) with a known probability. This means that for any choice of
k, with high probability our selected feature set is not too wasteful (in terms of the fraction
of cost spent on irrelevant features).
5


## Page 6


Theorem 1. For any α ∈(0, 1), we have
P {wFDP (Rk) ≤U (Rk, c) for all k} ≥1 −α,
(5)
where for any constant c > 0,
U(Rk, c) = −log α


1 + c Pk
j=1 1 {j /∈Rk}
Pk
j=1 ωj1 {j ∈Rk}

∨1



max
k∈H0
ωk
log {ωk −(ωk −1) αc}

.
(6)
For the standard knockoﬀprocedure described in Section 2.1, we have ω1 = . . . = ωp = 2.
In that case, with c = 1, (6) reduces exactly to the bound from applying Theorem 2 of
Katsevich and Ramdas (2018) to the Selective and Adaptive SeqStep procedure (Barber and
Cand`es, 2015) with p∗= λ = 1/2.
As mentioned in Section 2.1, our procedure can be generalized to any known distribution
of X and any unknown conditional distribution of Y given X. For example, in the binary
classiﬁcation data example in Section 4, we consider the statistics {T (ℓ)
j } derived from ℓ1-
penalized logistic regression. Following the arguments Candes et al. (2018), we can show
that Theorem 1 also holds for this choice of {T (ℓ)
j }.
Remark 2. The weighted false discovery proportion upper bound U(Rk, c) depends on the
unknown set H0. In practice, we can use an upper bound
¯U(Rk, c) = −log α


1 + c Pk
j=1 1 {j /∈Rk}
Pk
j=1 ωj1 {j ∈Rk}

∨1



max
k
ωk
log {ωk −(ωk −1) αc}

.
(7)
Moreover, if an estimated set ˆH0 satisfying H0 ⊆ˆH0 is available, then (6) with the maximum
taken over ˆH0 gives a tighter bound in (5).
Our procedure yields a sequence of sets Rk of selected variables, and the bound in (5)
gives a speciﬁc description of the tradeoﬀbetween capturing enough of the signal variables
and incurring too much cost. The simultaneous nature of the bound means that wFDP(Rk)
is controlled regardless of the approach used to select k: the choice of k can depend on the
size of Rk, the cost of Rk, or in fact any function of the data.
3
Simulation studies
We now investigate the feature selection performance of cheap knockoﬀs in simulation. We
set n = 200 and p = 30. Each element of the design matrix X ∈Rn×p is independent and
identically distributed as N(0, 1). The response is generated from the linear model (1) with
Gaussian errors ε ∼N(0, σ2) and σ2 = (4n)−1∥Xβ∥2
2. We let β1 = . . . = β10 = 2, and βj = 0
for j > 10. We set the ﬁrst half of the relevant features to be expensive and the second half
to be cheap, i.e., ω1 = . . . = ω5 = 6, and ω6 = . . . = ω10 = 2. For the irrelevant features, i.e.,
for any j > 10, we set P(ωj = 6) = γ and P(ωj = 2) = 1−γ, where γ ∈{0, 0.25, 0.5, 0.75, 1}.
6


## Page 7


We construct multiple knockoﬀvariables using entropy maximization (Roquero Gimenez
and Zou, 2018), and we compute the statistics T (ℓ)
j
as the absolute value of the lasso coeﬃcient
estimates in (3), with the tuning parameter selected using cross-validation. In Appendix B
we report the wall-clock running time of cheap knockoﬀs in the numerical studies.
We
ﬁnd that the majority of computation is spent on generating multiple knockoﬀs, which is
challenging when p is large and (or) the feature costs are large (after dividing by their
greatest common factor). In such cases, alternative construction methods could be used.
For example, Roquero Gimenez and Zou (Appendix A.1. 2018) show that an equicorrelation
construction has a closed form expression, which is particularly favorable in computation
since it does not depend on the number of multiple knockoﬀs (and equivalently, the feature
costs).
We ﬁrst verify the bound in Theorem 1 and compare the performance of cheap knockoﬀs
to Katsevich and Ramdas (2018), which ignores feature costs. In particular, by carrying out
Steps 1-3 in Section 2.1 with ω1 = . . . = ωp = 2 in (7), the bound in (7) coincides with the
result in Katsevich and Ramdas (2018). We denote this approach as Katsevich and Ramdas
(2018). For both methods, we take α = 0.2 in (7). In Fig. 1 we report both the ratio
¯U(Rk, 1)−1wFDP(Rk) and the actual weighted false discovery proportion wFDP(Rk) for
each Rk for both methods in the settings where γ = 0, 0.5, and 1.
7


## Page 8


0.0
0.5
1.0
1.5
2.0
γ = 0
U(Rk, 1)−1wFDP(Rk)
0
5
10
15
20
25
30
0.0
0.1
0.2
0.3
k
wFDP(Rk)
0
1
2
3
4
γ = 0.5
0
5
10
15
20
25
30
0.0
0.1
0.2
0.3
0.4
0.5
k
0
1
2
3
4
5
6
7
γ = 1
0
5
10
15
20
25
30
0.0
0.1
0.2
0.3
0.4
0.5
0.6
k
Figure 1: Each line represents one of 100 simulated datasets. Jitter is applied to ease visual-
ization. The black dashed lines represent cheap knockoﬀs (our proposal) which incorporates
feature costs, and the red solid lines represent Katsevich and Ramdas (2018) which does not
make use of feature costs. Top panel: the cheap knockoﬀs approach controls the weighted
false discovery proportion with the desired probability (α = 0.2) whereas the Katsevich
and Ramdas (2018) procedure does not. Bottom panel: The cheap knockoﬀs attains lower
weighted false discovery proportion than the Katsevich and Ramdas (2018) procedure for
most values of k when γ is large.
As seen in Fig. 1, the ratio ¯U(Rk, 1)−1wFDP(Rk) for our cheap knockoﬀprocedure
is mostly below 1, indicating that the bound in Theorem 1 holds. Moreover, when γ is
large, the weighted false discovery proportion for the cheap knockoﬀprocedure is lower than
Katsevich and Ramdas (2018) for most values of k. Table 1 gives the estimated probability
that the bound is violated, i.e., bP(supk ¯U−1
k (Rk, 1)wFDP(Rk) > 1), for each method for
γ ∈{0, 0.25, 0.5, 0.75, 1}.
8


## Page 9


γ
0
0.25
0.5
0.75
1
Cheap knockoﬀs (our proposal)
0.08
0.05
0.08
0.07
0.04
Katsevich and Ramdas (2018)
0.01
0.05
0.12
0.25
0.31
Table 1: Proportion of 100 simulated datasets for which supk ¯U−1
k (Rk, 1)wFDP(Rk) > 1 is
violated. Our proposed cost-conscious procedure successfully controls the probability below
the α = 0.2 level for all values of γ, while Katsevich and Ramdas (2018) does not control
this probability when γ = 0.75 and γ = 1.
We see that the Katsevich and Ramdas (2018) procedure which is not cost-conscious
performs worse as γ increases, that is, when irrelevant variables are more likely to be expen-
sive. Since the method ignores cost, it may erroneously select expensive irrelevant features,
leading to poor weighted false discovery proportion.
While our proposal focuses on recovering the correct set of features with simultaneous
wFDP control, we show empirically that the set of features selected by cheap knockoﬀs
usually incurs low cost without compromising prediction accuracy. Speciﬁcally, for each set
of selected variables R1, . . . , Rp, we compute both the root mean squared prediction error
of the least squares model ﬁt to the variables in Rk, and the total cost P
j∈Rk ωj. We see
from Fig. 2 that for a given budget, the cheap knockoﬀprocedure attains smaller prediction
error than the procedure in Katsevich and Ramdas (2018), which is not cost-conscious. In
particular, the cheap knockoﬀprocedure tends to select all ﬁve of the cheap relevant features
before any expensive feature is let in the model, whereas Katsevich and Ramdas (2018)
does not take feature cost into consideration. For k ≥10, Rk for both methods includes
essentially all the relevant features, thus giving similar performance.
0
10
20
30
40
50
0
1
2
3
4
5
6
γ = 0
cost
root mean squared prediction error
G
G
G
G
G
G
G
G
G
G GGGGGGGGGG
0
10
20
30
40
50
60
0
1
2
3
4
5
6
γ = 0.5
cost
G
G
G
G
G
G
G
G
G
GGGGGGGGGGGGG
0
20
40
60
0
1
2
3
4
5
6
γ = 1
cost
G
G
G
G
G
G
G
G
G
GGGGGGGGGGGGGGGGG
Figure 2: Tradeoﬀbetween prediction accuracy and total cost (averaged over 100 simula-
tions). The line with dots in black represents the cheap knockoﬀprocedure, and the line
with crosses in red represents Katsevich and Ramdas (2018). The cost of the model selected
by our cost-conscious procedure can be much lower than that of the procedure in Katsevich
and Ramdas (2018) without sacriﬁcing predictive performance.
9


## Page 10


4
Data application
To gauge the performance of cheap knockoﬀs in a real dataset, we consider data from the
National Health and Nutrition Examination Survey (NHANES) (National Center for Health
Statistics 2018, processed in Kachuee et al. 2019a,b). The dataset contains 92062 samples
of survey participants. We consider 30 features, which can be broadly categorized into four
types: demographics, questionnaire-based, examination-based, and laboratory-based. For
each feature, medical experts suggest a corresponding integer-valued cost (ranging from 2
to 9) for that feature based on “the overall ﬁnancial burden, patient privacy, and patient
inconvenience” (Kachuee et al., 2019b). A brief summary of the 30 features can be found in
Table 2. Finally, each observation is associated with a label of pre-diabetes/diabetes (as one
category) or normal. The task is to select features that are closely associated with diabetes
while taking feature cost into consideration.
Examples
Cost
Demographics
Age; Income; Education level
2 to 4
Questionnaire
Average sleep length (in hours)
4
Examination
Diastolic Blood pressure; Systolic Blood Pressure
5
Laboratory
Cholesterol; Triglyceride; Fibrinogen
9
Table 2: Examples of the features in the NHANES dataset
We consider the cheap knockoﬀprocedure as in Section 2.2, modiﬁed so that the statis-
tics {T (ℓ)
j } computed in (3) are derived from ℓ1-penalized logistic regression (instead of ℓ1-
penalized least squares). Following the arguments in Candes et al. (2018), we can show that
Theorem 1 also holds for this choice of {T (ℓ)
j }.
To numerically verify Theorem 1, we would need to know the true set of relevant variables.
We test the cheap knockoﬀprocedure using partially-simulated data. To form a reasonable
ground truth, we start by performing logistic regression on a random set of 72062 samples.
In total, we retain 11 variables whose p-values are smaller than 0.01 / 30 (by Bonferroni
correction). We take these as the true set of relevant variables (see Appendix A for the
list of relevant variables).
We next generate responses for the remaining 20000 samples
from a logistic regression model using only these selected features. The coeﬃcient values
used correspond to those from the ﬁtted logistic regression estimates. We then randomly
divide these 20000 samples (with simulated responses) into 50 non-overlapping sets, each
containing 400 samples.
On each set, we run our method to obtain a path of selected
variables. Finally, we compute the estimated probability that the bound in (6) is violated,
i.e., bP(supk ¯U−1
k (Rk, 1)wFDP(Rk) > 1) for α ∈{0.05, 0.1, ..., 0.5}. We see from Table 3
that the estimated probability is lower than the corresponding value of α, indicating that
Theorem 1 holds for our proposed cost-conscious procedure.
10


## Page 11


α
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
0.45
0.50
Cheap knockoﬀs
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.04
0.06
Table 3: Proportion of 50 data subsets for which supk ¯U−1
k (Rk, 1)wFDP(Rk) > 1 is violated.
On each of the 50 non-overlapping data subsets, we further compute wFDP and cost
for the path of selected variables Rk returned by cheap knockoﬀs and the proposal in Kat-
sevich and Ramdas (2018), which ignores feature costs. Figure 3 reports the 20, 50, and
80 percentiles (over the 50 non-overlapping sets) of wFDP and cost, and shows that our
proposal eﬀectively attains a lower wFDP and a lower cost than the proposal in Katsevich
and Ramdas (2018) which is not cost-conscious.
0
5
10
15
20
25
30
0.0
0.1
0.2
0.3
0.4
k
wFDP(Rk)
G G G G G G G G G G G G G G G G G G G G G G G G G G G G G G
G G G G
G
G
G
G
G
G
G
G
G
G
G
G G G G G G G G G G G G G G G
0
5
10
15
20
25
30
0
10
20
30
40
50
k
cost(Rk)
G
G
G
G
G G G
G G G
G G G G G G G G G G G G G G G G G G G G
G
G
G
G
G
G
G
G
G
G G
G G G G G G G G G G G G G G G G G G G
G
Percentile
20
50
80
Cheap knockoffs
Katsevich & Ramdas(2018)
Figure 3: The 20, 50, and 80 percentiles of wFDP (left panel) and cost (right panel) over 50
non-overlapping data subsets of cheap knockoﬀs and the procedure in Katsevich and Ramdas
(2018).
Although prediction performance of the selected model is not the main theoretical focus
of our proposal, we next study the prediction performance and the total cost of the selected
variables. For comparison, we consider the following methods:
1. Katsevich & Ramdas(2018): the proposal of Katsevich and Ramdas (2018) applied
to the ‘Selective and adaptive SeqStep’ method. It is equivalent to our method if we
ignore the cost information, i.e., we set ω1 = ω2 = ... = ω30 = 2.
2. Logistic regression: logistic regression applied to all 30 features. This procedure is
not cost-conscious, and does not perform features selection. We use this as a benchmark
for classiﬁcation performance.
11


## Page 12


We run these methods on all 92062 observations. Given the large sample size, we expect
training error to be a good approximation of the generalization error.
Furthermore, to
highlight the eﬀects of feature costs, we consider exaggerating the feature costs by using the
squares of their actual costs.
0
5
10
15
20
25
30
0.55
0.60
0.65
0.70
0.75
|Rk|
AUC
0
5
10
15
20
25
30
0
200
400
600
800
|Rk|
Cost
0
200
400
600
800
0.55
0.60
0.65
0.70
0.75
Cost
AUC
Cheap knockoffs
Katsevich&Ramdas(2018)
Logistic regression
Figure 4: Left: The classiﬁcation performance (in terms of the area under the ROC curve)
for diﬀerent sizes of the selected model Rk (k = 1, . . . , 30). Center: The total cost for
diﬀerent sizes of the selected model. Right: The classiﬁcation performance versus the cost
of the selected model. In all three panels of this ﬁgure, we consider the squared costs to
highlight the eﬀects of feature costs.
From Figure 4, we see that cheap knockoﬀs can achieve favorable classiﬁcation perfor-
mance at a low feature cost. In particular, the ﬁrst two panels show that for a ﬁxed model
size, cheap knockoﬀs tends to achieve slightly worse classiﬁcation performance than the pro-
cedure of Katsevich and Ramdas (2018), which is not cost-conscious. However, our method
achieves this classiﬁcation performance at a lower cost. The right panel shows that for a
given model cost, our method can obtain favorable classiﬁcation performance compared with
the proposal of Katsevich and Ramdas (2018). Moreover, our method’s classiﬁcation per-
formance is close to the benchmark of logistic regression, while using a much cheaper set of
features.
In Figures 5 and 6, we show the path of variables selected by cheap knockoﬀs and that
of Katsevich and Ramdas (2018). Each point represents a variable added to a model (with
the feature name in the legend). For example, we see that both methods include Gender,
Height, Weight, and Triglyceride when the model size is 4. However, the cheap knockoﬀ
procedure tends to select cheaper features ﬁrst, adding the expensive laboratory feature
Triglyceride last among these four features. By comparison, the proposal of Katsevich
and Ramdas (2018) does not show any preference for inexpensive features. For the model
with two variables, cheap knockoﬀs selects Gender and Height, which has lower cost and
better classiﬁcation performance than the model of Height and Weight selected by Katsevich
and Ramdas (2018).
In addition, in Figure 6, we present the path of variables selected by cheap knockoﬀs ap-
plied with squared feature costs, where squaring has been performed to exaggerate the eﬀect
12


## Page 13


of the feature costs. Comparing with Figure 5, we see that cheap knockoﬀs tends to select less
expensive features, while still attaining comparable classiﬁcation performance. In particular,
when the costs are squared, cheap knockoﬀs no longer selects Diastolic BP(2nd), Systolic
BP(4th), Systolic BP(1st), Diastolic BP(3rd), Vigorous activity, and Upper leg
length. Among these omitted variables, only Upper leg length is considered relevant by
the logistic regression (see Appendix A).
5
Discussion
In this paper, we proposed cheap knockoﬀs, a procedure for performing feature selection
when features have costs. Cheap knockoﬀs is based on the idea of constructing multiple
knockoﬀs for each feature. In particular, cheap knockoﬀs forces more expensive features to
compete with more knockoﬀs, making it harder for expensive features to be selected. Our
method yields a path of selected feature sets, and we show that the weighted false discovery
proportion is simultaneously bounded with high probability along this path.
An interesting yet challenging future research direction is to develop a method based on
the multiple knockoﬀs idea that provably controls the weighted false discovery rate. The
martingale-type arguments used in the original knockoﬀpaper rely on certain symmetries
that are broken when the numbers of knockoﬀs constructed for diﬀerent features are not all
equal.
Finally, an R package named cheapknockoff, implementing our proposed method, is
available on https://github.com/hugogogo/cheapknockoff.
The simulation studies in
Section 3 use the simulator package (Bien, 2016), and the code to reproduce the simulation
results (in Section 3) and the NHANES data analysis (in Section 4) is available at https://
github.com/hugogogo/reproducible/tree/master/cheapknockoff. The NHANES dataset
(National Center for Health Statistics, 2018) is processed in Kachuee et al. (2019a,b) and is
available at https://github.com/mkachuee/Opportunistic.
6
Acknowledgments
The authors thank Will Fithian for suggesting the simultaneous inference framework. All
authors were supported by NIH Grant R01GM123993. Jacob Bien was also supported by
NSF CAREER Award DMS-1653017 and Daniela Witten was also partially supported by
NIH Grant DP5OD009145, NSF CAREER Award DMS-1252624, and a Simons Investigator
Award in Mathematical Modeling of Living Systems.
References
Rina Foygel Barber and Emmanuel J. Cand`es.
Controlling the false discovery rate via
knockoﬀs. The Annals of Statistics, 43(5):2055–2085, 10 2015.
13


## Page 14


G
G G
G G G GG G
G G G G G
G G G G G G G G
1
15
16
28
22
21
4
3
20
27
23
11
25
9
29
26
5
18
13
24
8
12
0.53
0.58
0.63
0.68
0.73
0.78
0
30
60
90
Cost
AUC
G
G
G
G
Demographics (Cost = 2)
Questionnaire (Cost = 4)
Examination (Cost = 5)
Laboratory (Cost = 9)
Cheap knockoffs
G G
G
G G GG
G GG G
G GG GGG GG GG GGGG GG
15
16
28
1 2221
4
27
20
3
24
29
23
9
19
11
13
26
5
18
10
25
8
12
6
17
7
0.53
0.58
0.63
0.68
0.73
0.78
0
50
100
Cost
AUC
1:Gender
3:Education
4:High blood pressure history
5:Relatives having diabetes
6:Income
7:Avg sleep hours
8:Age started smoking
9:Alcohol frequency
10:Moderate activity
11:Alcohol amount
12:Avg physical activity level
13:Vigorous activity
15:Height
16:Weight
17:Diastolic BP(4th)
18:Diastolic BP(3rd)
19:Systolic BP(2nd)
20:Systolic BP(3rd)
21:Waist circumference
22:Body mass index
23:Diastolic BP(2nd)
24:Upper leg length
25:Systolic BP(1st)
26:Systolic BP(4th)
27:Cholesterol
28:Triglyceride
29:LDL−cholesterol
Katsevich&Ramdas(2018)
Figure 5: The path of variables selected by cheap knockoﬀs (top) and the proposal of Kat-
sevich and Ramdas (2018) (bottom). Each point represents a newly selected feature in the
model. Variable indices are ordered from cheapest to most expensive.
14


## Page 15


G
G G
G
GG
GG G
GGGG G G
GG
1
15
16
22
21
3
28
4
20
27
9
5
11
17
23
29
13
0.53
0.58
0.63
0.68
0.73
0.78
0
100
200
300
400
500
Cost
AUC
G
G
G
G
Demographics (Cost = 4)
Questionnaire (Cost = 16)
Examination (Cost = 25)
Laboratory (Cost = 81)
1:Gender
3:Education
4:High blood pressure history
5:Relatives having diabetes
9:Alcohol frequency
11:Alcohol amount
13:Vigorous activity
15:Height
16:Weight
17:Diastolic BP(4th)
20:Systolic BP(3rd)
21:Waist circumference
22:Body mass index
23:Diastolic BP(2nd)
27:Cholesterol
28:Triglyceride
29:LDL−cholesterol
Cheap knockoffs (squared costs)
Figure 6: The path of variables selected by cheap knockoﬀs, with squared costs. Each point
represents a newly selected feature in the model. Variable indices are ordered from cheapest
to most expensive.
15


## Page 16


Pallavi Basu, T Tony Cai, Kiranmoy Das, and Wenguang Sun. Weighted false discovery rate
control in large-scale multiple testing. Journal of the American Statistical Association,
113(523):1172–1183, 2018.
Yoav Benjamini and Ruth Heller. False discovery rates for spatial signals. Journal of the
American Statistical Association, 102(480):1272–1281, 2007.
Yoav Benjamini and Yosef Hochberg. Controlling the false discovery rate: a practical and
powerful approach to multiple testing. Journal of the Royal statistical society: series B
(Methodological), 57(1):289–300, 1995.
Yoav Benjamini and Yosef Hochberg. Multiple hypotheses testing with weights. Scandinavian
Journal of Statistics, 24(3):407–418, 1997.
Yoav Benjamini and Daniel Yekutieli. The control of the false discovery rate in multiple
testing under dependency. The Annals of Statistics, 29(4):1165–1188, 2001.
J. Bien. The Simulator: An Engine to Streamline Simulations. ArXiv e-prints, June 2016.
Gilles Blanchard and Etienne Roquain. Two simple suﬃcient conditions for FDR control.
Electronic journal of Statistics, 2:963–992, 2008.
Emmanuel Candes, Yingying Fan, Lucas Janson, and Jinchi Lv. Panning for gold: ‘Model-X’
knockoﬀs for high dimensional controlled variable selection. Journal of the Royal Statistical
Society: Series B (Statistical Methodology), 80(3):551–577, 2018.
Kristen Emery, Syamand Hasam, William Staﬀord Noble, and Uri Keich. Multiple compe-
tition based FDR control. arXiv preprint arXiv:1907.01458, 2019.
Jelle J Goeman and Aldo Solari. Multiple testing for exploratory research. Statistical Science,
26(4):584–597, 2011.
Mohammad Kachuee, Orpaz Goldstein, Kimmo Karkkainen, Sajad Darabi, and Majid Sar-
rafzadeh. Opportunistic learning: Budgeted cost-sensitive learning from data streams.
arXiv preprint arXiv:1901.00243, 2019a.
Mohammad Kachuee, Kimmo Karkkainen, Orpaz Goldstein, Davina Zamanzadeh, and Majid
Sarrafzadeh. Cost-sensitive diagnosis and learning leveraging public health data. preprint
https://arxiv. org/abs/1902.07102, 2019b.
Eugene Katsevich and Aaditya Ramdas. Towards “simultaneous selective inference”: post-
hoc bounds on the false discovery proportion. arXiv preprint arXiv:1803.06790, 2018.
National Center for Health Statistics. National health and nutrition examination survey,
2018. URL https://www.cdc.gov/nchs/nhanes.
16


## Page 17


Aaditya K Ramdas, Rina F Barber, Martin J Wainwright, and Michael I Jordan. A uniﬁed
treatment of multiple testing with prior knowledge using the p-ﬁlter.
The Annals of
Statistics, 47(5):2790–2821, 2019.
J. Roquero Gimenez and J. Zou. Improving the Stability of the KnockoﬀProcedure: Multiple
Simultaneous Knockoﬀs and Entropy Maximization. ArXiv e-prints, October 2018.
Robert Tibshirani. Regression shrinkage and selection via the lasso. Journal of the Royal
Statistical Society: Series B (Methodological), 58(1):267–288, 1996.
Jean Ville. Etude critique de la notion de collectif. Bull. Amer. Math. Soc, 45(11):824, 1939.
Guan Yu, Haoda Fu, and Yufeng Liu.
High-dimensional cost-constrained regression via
nonconvex optimization. Technometrics, pages 1–13, 2021.
17


## Page 18


Appendices
A
NHANES dataset: signiﬁcant features in logistic re-
gression
In the order of increasing p-values (smaller than 0.01 / 30):
Name
p-value
Gender
1.73 × 10−262
Triglyceride
5.92 × 10−214
Height
1.17 × 10−184
Weight
1.98 × 10−102
Waist circumference
4.09 × 10−37
Body mass index
4.02 × 10−31
High blood pressure history
1.51 × 10−27
Cholesterol
4.92 × 10−24
Education
8.16 × 10−10
Upper leg length
3.17 × 10−5
Systolic BP(3rd)
1.01 × 10−4
B
Running time comparison in numerical studies
γ
0
0.25
0.5
0.75
1
Cheap knockoﬀs (our proposal)
2.796
2.772
2.784
2.798
2.812
Katsevich and Ramdas (2018)
0.273
0.250
0.258
0.251
0.253
Table 4: Wall-clock time comparison (in seconds, averaged over 100 simulated datasets)
between our proposal and Katsevich and Ramdas (2018) in generating Table 1.
Cheap knockoﬀs (our proposal)
7.284
Katsevich and Ramdas (2018)
2.678
Table 5: Wall-clock time comparison (in seconds, averaged over 50 non-overlapping data
subsets) between our proposal and Katsevich and Ramdas (2018) in generating Figure 3.
18


## Page 19


C
Properties of multiple knockoﬀs
We study the properties of the multiple knockoﬀs constructed in Step 1 of Section 2.2. Deﬁne
˜Z =

˜X(2)
1 , . . . , ˜X(ω1)
1
, ˜X(2)
2 , . . . , ˜X(ω2)
2
, . . . , ˜X(2)
p , . . . , ˜X(ωp)
p
T
∈R
P
j(ωj−1)
as the random vector of all knockoﬀfeatures, and
Z =

˜X(1)
1 , ˜X(2)
1 , . . . , ˜X(ω1)
1
, ˜X(1)
2 , ˜X(2)
2 , . . . , ˜X(ω2)
2
, . . . , ˜X(1)
p , ˜X(2)
p , . . . , ˜X(ωp)
p
T
∈R
P
j ωj, (8)
where ˜X(1)
j
= Xj is the original feature for j = 1, . . . , p. For any p-tuple of permutations
ς = (ς1, . . . , ςp) where ςj is a permutation on the set {1, . . . , ωj}, and for any vector v =
(v(1)
1 , . . . , v(ω1)
1
, . . . , v(1)
p , . . . , v(ωp)
p
) ∈R
P
j ωj, we deﬁne
vswap(ς) =

v(ς1(1))
1
, . . . , v(ς1(ω1))
1
, v(ς2(1))
2
, . . . , v(ς2(ω2))
2
, . . . , v(ςp(1))
p
, . . . , v(ςp(ωp))
p
T
∈R
P
j ωj.
Therefore, Zswap(ς) denotes the random vector where each ςj permutes the ωj knockoﬀfeatures
(including the original one) corresponding to Xj.
We generalize the deﬁnition of multiple model-X knockoﬀs (Deﬁnition 3.2 in Roquero
Gimenez and Zou, 2018) to our setting in which each feature can have a diﬀerent number of
knockoﬀs:
Deﬁnition 3. Consider any cost vector ω = (ω1, . . . , ωp), where ωj > 1 are integers. The
random vector ˜Z is a valid ω-knockoﬀof X = (X1, . . . , Xp) if
1. Zswap(ς) and Z are identically distributed for any tuple of permutations ς = (ς1, . . . , ςp);
2. ˜Z and Y are conditionally independent given X.
Under the assumption that X follows a multivariate Gaussian distribution, it can be
veriﬁed (see, e.g., Proposition 3.4 in Roquero Gimenez and Zou, 2018) that following Step
1 in Section 2.2, the vector ˜Z is a valid ω-knockoﬀof X. In particular, the second property
is guaranteed provided that the construction of ˜Z does not use Y , as in Roquero Gimenez
and Zou (2018).
The next lemma states the exchangeability property of the irrelevant features and their
knockoﬀs, i.e., we can permute an irrelevant feature and its knockoﬀs without changing the
joint distribution of Z and Y .
Lemma 4 (Exchangeability of irrelevant features and their knockoﬀs). Consider any tuple
of permutations ς = (ς1, . . . , ςp), where ςj is the identity permutation for j /∈H0, and ςj is
an arbitrary permutation over the set {1, . . . , ωj} for j ∈H0. If ˜Z is a valid ω-knockoﬀof
X, then (Z, Y ) and (Zswap(ς), Y ) are identically distributed.
Proof. By the property of a valid ω-knockoﬀ, Zswap(ς) and Z are identically distributed. So it
is left to show that Y |Z and Y |Zswap(ς) are identically distributed. This can be shown using
the same arguments as in the proof of Lemma 1 in Candes et al. (2018).
19


## Page 20


We denote
T =

T (1)
1 , . . . , T (ω1)
1
, T (1)
2 , . . . , T (ω2)
2
, . . . , T (1)
p , . . . , T (ωp)
p

∈R
P
j ωj,
for T (ℓ)
j
deﬁned in Step 2 of Section 2.2.
Furthermore, we deﬁne component-wise order
statistics on T,
Tordered =
 T1,(1), . . . , T1,(ω1), T2,(1), . . . , T2,(ω2), . . . , Tp,(1), . . . , Tp,(ωp)

∈R
P
j ωj
such that Tj,(1) ≥Tj,(2) ≥. . . ≥Tj,(ωj) for all j.
The following lemma characterizes the multiple knockoﬀstatistics {κj}p
j=1 computed in
Step 2 of Section 2.2. It essentially states that for j ∈H0, the statistics κj corresponding to
the irrelevant feature Xj is uniformly distributed on the set {1, . . . , ωj}, and is independent
of the statistics corresponding to all other features and the component-wise order statistics
Tordered. This property generalizes the “coin-ﬂip” property of the standard model-X knockoﬀ
(see, e.g., Lemma 2 in Candes et al., 2018), and is the key to the proof of Theorem 1.
Lemma 5 (Multiple knockoﬀstatistics). Suppose ˜Z is a valid ω-knockoﬀof Z. For any
j ∈H0, the statistic κj is uniformly distributed on the set {1, . . . , ωj}, and is independent of
{κk}k̸=j and the order statistics Tordered.
Proof. We adapt the proof idea in B.2 of Roquero Gimenez and Zou (2018). Consider any
tuple of permutations ς = (ς1, . . . , ςp), where ςj is the identity permutation for j /∈H0,
and ςj is an arbitrary permutation over the set {1, . . . , ωj} for j ∈H0. We ﬁrst show that
(ς1(κ1), . . . , ςp(κp), Tordered) has the same distribution as (κ1, . . . , κp, Tordered).
We denote ς−1 = (ς−1
1 , . . . , ς−1
p ) where ς−1
j
is the inverse permutation of ςj. Recall from
Step 2 of Section 2.2, combined with the deﬁnition of Z in (8), that T = f(Z, Y ) for some
map f, and observe that Tswap(ς−1) = f(Zswap(ς−1), Y ). So by Lemma 4, we have that Tswap(ς−1)
and T are identically distributed. For any kj ∈{1, . . . , ωj} and tjℓ∈R for j = 1, . . . , p and
ℓ= 1, . . . , ωj, we have
P
" p\
j=1
{κj = kj},
p\
j=1
ωj
\
ℓ=1
{Tj,(ℓ) = tjℓ}
#
=P
" p\
j=1
{T
(kj)
j
= Tj,(1) = tj1},
p\
j=1
ωj
\
ℓ=1
{Tj,(ℓ) = tjℓ}
#
=P
" p\
j=1
{T
(ς−1
j
(kj))
j
= Tj,(1) = tj1},
p\
j=1
ωj
\
ℓ=1
{Tj,(ℓ) = tjℓ}
#
=P
" p\
j=1
{κj = ς−1
j (kj)},
p\
j=1
ωj
\
ℓ=1
{Tj,(ℓ) = tjℓ}
#
=P
" p\
j=1
{ςj(κj) = kj},
p\
j=1
ωj
\
ℓ=1
{Tj,(ℓ) = tjℓ}
#
,
20


## Page 21


where the ﬁrst and the third equalities hold from the deﬁnition of κj’s, the second equal-
ity holds because Tswap(ς−1) and T are identically distributed, along with the fact that
(Tswap(ς−1))ordered = Tordered. Therefore, we have shown that
(ς1(κ1), . . . , ςp(κp), Tordered) and (κ1, . . . , κp, Tordered) are identically distributed.
(9)
For any j ∈H0, now we further assume that ςk is an identity permutation for all k ̸= j, and
ςj is an arbitrary permutation on the set {1, . . . , ωj}. The equality in joint distributions (9)
implies that ςj(κj) has the same distribution as κj. Since ςj is an arbitrary permutation on
the set {1, . . . , ωj}, we have that κj is uniformly distributed on the set {1, . . . , ωj}, i.e.,
P(κj = i) = ω−1
j
∀i ∈{1, . . . , ωj}.
(10)
Furthermore, for any ik ∈{1, . . . , ωk} for k ̸= j, and t ∈R
P
ℓωℓ,
P
"
ςj(κj) = i

\
k̸=j
{κk = ik} , Tordered = t
#
=
P
h
ςj(κj) = i, T
k̸=j {ςk(κk) = ik} , Tordered = t
i
P
hT
k̸=j {κk = ik} , Tordered = t
i
=
P
h
κj = i, T
k̸=j {κk = ik} , Tordered = t
i
P
hT
k̸=j {κk = ik} , Tordered = t
i
=P
"
κj = i

\
k̸=j
{κk = ik} , Tordered = t
#
,
where the ﬁrst equality holds from Bayes formula and the fact that ςk is the identity permuta-
tion for all k ̸= j, and the second equality holds from (9). Therefore, for any ik ∈{1, . . . , ωk}
for k ̸= j, and t ∈R
P
ℓωℓ, we have that
P
"
κj = i

\
k̸=j
{κk = ik} , Tordered = t
#
= ω−1
j
∀i ∈{1, . . . , ωj}.
(11)
Combining (10) and (11), we have that κj is independent of {κk}k̸=j and Tordered.
D
Proof of Theorem 1
Without loss of generality, we assume that the ordering in Step 3 of Section 2.2 is such that
σ(j) = j for j ∈{1, . . . , p}. Consider
V(Rk, c) =
c−1 + P
j 1 {j /∈Rk}
P
j ωj1 {j ∈Rk}

∨1
=
c−1 + Pk
j=1 1 {κj > 1}
Pk
j=1 ωj1 {κj = 1}

∨1
(12)
21


## Page 22


for some constant c. Recall that
wFDP(Rk) =
P
j ωj1 {j ∈H0 ∩Rk}
P
j ωj1 {j ∈Rk}

∨1
=
Pk
j=1 ωj1 {j ∈H0} 1 {κj = 1}
Pk
j=1 ωj1 {κj = 1}

∨1
.
We have the following key lemma:
Lemma 6. Let V(Rk, c) be deﬁned as in (12). Then for any α ∈(0, 1), there exists x > 0
such that
P

sup
k
wFDP(Rk)
V(Rk, c)
≥x

≤α.
(13)
Proof of Lemma 6. For any x > 0, from (12),
P

sup
k
wFDP(Rk)
V(Rk, c)
≥x

=P
(
sup
k
 k
X
j=1
ωj1 {κj = 1} 1 {j ∈H0} −x
k
X
j=1
1 {κj > 1}
!
≥c−1x
)
≤P
(
sup
k
 k
X
j=1
ωj1 {κj = 1} 1 {j ∈H0} −x
k
X
j=1
1 {κj > 1} 1 {j ∈H0}
!
≥c−1x
)
=P
"
sup
k
exp
"
θ
( k
X
j=1
ωj

1 {κj = 1} −x
ωj
1 {κj > 1}

1 {j ∈H0}
)#
≥exp
 c−1xθ

#
for any θ > 0. Deﬁne
Zk = exp
"
θ
( k
X
j=1
ωj

1 {κj = 1} −x
ωj
1 {κj > 1}

1 {j ∈H0}
)#
(14)
for k ≥1, and Z0 = 1. Next we ﬁnd a value of θ > 0 such that {Zk} is a super-martingale
with respect to a certain ﬁltration Fk. If such a value of θ exists, then from Ville’s maximal
inequality for super-martingales (Ville, 1939), we have that
P

sup
k
wFDP(Rk)
V(Rk, c)
≥x

≤P

sup
k
Zk ≥exp(c−1θx)

≤
E(Z0)
exp(c−1θx) = exp(−c−1θx). (15)
So it is left to show that Zk is a super-martingale with respect to a ﬁltration Fk, where
Fk is the σ-ﬁeld generated from {κj}j≤k,j∈H0. First we observe that Zk is adapted to Fk for
all k. By deﬁnition of a super-martingale, it is left to show that
E
 Zk
Zk−1
| Fk−1

= E

exp

ωkθ

1 {κk = 1} −x
ωk
1 {κk > 1}

1 {k ∈H0}

| Fk−1

≤1.
22


## Page 23


First, we observe that this holds trivially for k /∈H0. For k ∈H0, we have
E
 Zk
Zk−1
| Fk−1

=E

exp

ωkθ

1 {κk = 1} −x
ωk
1 {κk > 1}

| Fk−1

=E [1 {κk = 1} exp (ωkθ) | Fk−1] + E [1 {κk > 1} exp (−θx) | Fk−1]
= exp (ωkθ) P (κk = 1 | Fk−1) + exp (−θx) P (κk > 1 | Fk−1)
=exp (ωkθ)
ωk
+ (ωk −1) exp (−θx)
ωk
,
where the last equality holds from Lemma 5.
For any ﬁxed α ∈(0, 1), take x = θ−1(−c log α), which is equivalent to exp(−c−1θx) = α.
Then it remains to select θ such that for all k ∈H0,
E
 Zk
Zk−1
| Fk−1

= exp (ωkθ)
ωk
+ ωk −1
ωk
exp (c log α) ≤1,
(16)
which is satisﬁed for
θ ≤1
ωk
log {ωk −(ωk −1) αc} .
So we take
θ∗= min
k∈H0
1
ωk
log {ωk −(ωk −1) αc} .
Then (16) holds and thus from (15), the theorem holds with
x = −c log α
θ∗
= −c log α

max
k∈H0
ωk
log {ωk −(ωk −1) αc}

.
(17)
Now we have
U(Rk, c) = xV(Rk, c) = −log α


1 + Pk
j=1 c1 {κj > 1}
Pk
j=1 ωj1 {κj = 1}

∨1



max
k∈H0
ωk
log {ωk −(ωk −1) αc}

,
and the results in Theorem 1 follow.
23

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]