---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1803.07658v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1803.07658v3_Graph-based_regularization_for_regression_problems_with_alignment_and_highly-cor

> Source: 1803.07658v3_Graph-based_regularization_for_regression_problems_with_alignment_and_highly-cor.pdf

> Pages: 47

---


## Page 1


Graph-based regularization for regression problems with
alignment and highly-correlated designs
Yuan Li∗†, Benjamin Mark∗‡, Garvesh Raskutti† , Rebecca Willett§ , Hyebin Song† and David
Neiman†
Abstract: Sparse models for high-dimensional linear regression and machine learning have received
substantial attention over the past two decades. Model selection, or determining which features or co-
variates are the best explanatory variables, is critical to the interpretability of a learned model. Much
of the current literature assumes that covariates are only mildly correlated. However, in many modern
applications covariates are highly correlated and do not exhibit key properties (such as the restricted
eigenvalue condition, restricted isometry property, or other related assumptions). This work considers a
high-dimensional regression setting in which a graph governs both correlations among the covariates and
the similarity among regression coefﬁcients – meaning there is alignment between the covariates and re-
gression coefﬁcients. Using side information about the strength of correlations among features, we form
a graph with edge weights corresponding to pairwise covariances. This graph is used to deﬁne a graph
total variation regularizer that promotes similar weights for correlated features.
This work shows how the proposed graph-based regularization yields mean-squared error guarantees
for a broad range of covariance graph structures. These guarantees are optimal for many speciﬁc covari-
ance graphs, including block and lattice graphs. Our proposed approach outperforms other methods for
highly-correlated design in a variety of experiments on synthetic data and real biochemistry data.
1. Introduction
High-dimensional linear regression and inverse problems have received substantial attention over the past
two decades (see Hastie et al. (2015) for an overview). While there has been considerable theoretical and
methodological development, applying these methods in real-world settings is more nuanced since variables
or features are often highly correlated, while much of the existing theory and methodology is applicable
when features are independent or satisfy weak correlation assumptions such as the restricted eigenvalue
and other related conditions (see Candes and Tao (2007); Bickel et al. (2009); van de Geer and Buhlmann
(2009)). In this paper we develop an approach for parameter estimation in high-dimensional linear regression
with highly-correlated designs.
More speciﬁcally, we consider observations of the form
y = Xβ∗+ ϵ
(1)
where y ∈Rn is the response variable, X ∈Rn×p is the observation or design matrix, and ϵ ∼N(0, σ2In×n)
is Gaussian noise. Our goal is to estimate β∗based on (X, y) when X potentially has highly-correlated
columns and does not satisfy standard regularity assumptions. Speciﬁcally, we deﬁne Σ := 1
nE[X⊤X] and
consider settings where the minimum eigenvalue of Σ may be zero-valued or arbitrarily close to zero. We
consider a Gaussian linear model for simplicity of exposition but our ideas and results can be extended to
other settings. In Appendix K we discuss an extension to logistic regression.
∗These authors contributed equally to the manuscript.
†Department of Statistics, University of Wisconsin-Madison. Raskutti and Li were supported by NSF DMS 1407028. Song was
supported by NIH R01 GM131381-01.
‡Department of Mathematics, University of Wisconsin-Madison. Mark was supported by NSF Awards 0353079 and 1447449.
§Departments of Statistics and Computer Science, University of Chicago. Willett was supported by NIH Award 1 U54 AI117924-
01 and NSF Awards 0353079, 1447449, 1740707, and 1839338.
1
imsart-generic ver. 2014/10/16 file: simods.tex date: October 15, 2019
arXiv:1803.07658v3  [stat.ML]  13 Oct 2019


## Page 2


Highly-correlated or dependent features arise in many modern scientiﬁc problems, including the study
of enzyme thermostability (detailed in Section 1.1), genome wide association studies (GWAS) (Wu et al.,
2009; Viallon et al., 2016), neuroscience (Caoa et al., 2018), climate data (Barnston and Smith, 1996; Geisler
et al., 1985; DelSole and Banerjee, 2017; Mamalakis et al., 2018), and topic modeling.
As we discuss and expand upon in Section 1.4, there is a large body of work addressing the problem of
high-dimensional regression under highly correlated design (e.g., B¨uhlmann et al. (2013); Zou and Hastie
(2005)). The key challenge associated with highly-correlated columns is that estimates of β∗become very
sensitive to noise and, if columns are perfectly correlated, β∗may not be identiﬁable, which means additional
assumptions are required on β∗.
On the other hand, for many applications such as those mentioned above, there is known structure among
β∗since groups of covariates often exhibit similar inﬂuence on the response. There is also a large body
of work studying the high-dimensional linear model under additional assumptions on β∗including group
structure (e.g., Shen and Huang (2010); P. Zhao and Yu (2009)), graph structure (e.g., Sharpnack et al.
(2012); Hallac et al. (2015); Marial and Yu (2013); Wang et al. (2016)), and others.
In this work, we consider a case of highly correlated designs with additional structure on β∗. We use side
information to generate a covariance graph and then use an alignment condition to ensure a corresponding
graph structure on β∗. The alignment condition resolves the lack of identiﬁability by incorporating side
information about the covariance. Importantly, we develop novel theoretical guarantees for our procedure
under this alignment condition.
1.1. Motivating application: Biochemistry
In this section we apply the proposed GTV methodology to an application in biochemistry, speciﬁcally
protein analysis. In particular we focus on a speciﬁc protein of great interest, the cytochrome P450 enzyme,
which is an important protein in a number of environments. More speciﬁcally, cytochrome P450 proteins
are versatile biocatalysts which have been heavily employed for production of pharmaceutical products and
synthesis of other useful compounds (Guengerich, 2002). Additionally, thermostable proteins have great
industrial importance since they can withstand tough industrial process conditions (Niehaus et al., 1999).
We aim to understand how 3-D structural properties of proteins are related to the thermostability of the
proteins.
The dataset we use is a P450 chimeric protein dataset generated by the Romero Lab at UW-Madison∗.
The dataset contains thermostability measurements and features encoding the amino acid sequences and
describing structural properties of 242 chimeric P450 proteins. The chimeric proteins in the dataset are
created by recombining fragments of the genes of the three wild-type P450s (parent proteins) for eight blocks
(Li et al., 2007). Since the amino acid sequences for the parent proteins are known, the amino acid sequence
for a chimeric protein can be obtained from the recombination information for each block which parent
the gene fragment is inherited from. From the amino acid sequence information, 50 features describing the
structural properties of each protein were estimated by modeling 3-D structures of the chimeric enzymes via
the Rosetta biomolecular modeling suite (Alford et al., 2017). A full description of the 50 structural features
is provided in Table 2 in the Appendix. As our goal is to understand the relationship between the structure
and thermostability of the proteins, we use a linear model where the design matrix X ∈Rn×p consists of the
structure features and the response variable y ∈Rn contains the thermostability measurements for n = 242
and p = 50.
Importantly, many of the structural features are known to be highly correlated and we use side information
to estimate the covariance structure between the structural features. The side information consists of the
∗Raw data is available at https://github.com/Jerry-Duan/Structural-features
2


## Page 3


amino acid sequences for the P450 chimeric proteins. We use the sequence, structure, and function paradigm
for protein design in which a protein sequence determines the structure of the protein and the structure
determines the function of the protein. In particular, we exploit the sequence-structure relationship to obtain
a good estimate of the covariance matrix of the structural features. The combination of highly correlated
features and side information to estimate the covariance matrix makes this problem a natural ﬁt for out GTV
methodology. More details on the estimation of the covariance and the application are provided in Section 4.
1.2. Problem formulation and proposed estimator
First we deﬁne our model based on the standard linear model where data (X(i), y(i))n
i=1 ∈Rp×R are drawn
i.i.d. according to
y(i) = X(i)⊤β∗+ ϵ(i), where X(i) ∼N(0, Σp×p) and ϵ(i) ∼N(0, σ2).
Let y = (y(1), y(2), ..., y(n))⊤∈Rn, X = [X(1), X(2), ..., X(n)]⊤∈Rn×p and ϵ = (ϵ(1), ϵ(2), ..., ϵ(n))⊤∈
Rn. Hence the linear model can be expressed in the standard matrix-vector form:
y = Xβ∗+ ϵ.
Our goal is to estimates β∗. We are particularly interested in a setting where the columns of X may be highly
correlated (i.e., λmin(Σ) ≈0), but β∗is well-aligned with the covariance structure (i.e., correlated features
have similar weights in β∗).
We assume Σ is unknown and is estimated using either X or side information; let ˆΣ denote the estimate of
the covariance matrix. Deﬁne ˆsj,k := sign(ˆΣj,k). Based on the estimated covariance matrix ˆΣ, we consider
the following estimator for β∗:
ˆβ = arg min
β
1
n∥y −Xβ∥2
2 + λS
X
j,k
|ˆΣj,k|(βj −ˆsj,kβk)2
+ λ1(λTV
X
j,k
|ˆΣj,k|1/2|βj −ˆsj,kβk| + ∥β∥1),
(2)
where λS, λ1 and λTV are regularization parameters.
This estimator can be interpreted from a graph/network perspective by deﬁning the covariance graph
based on the covariance matrix ˆΣ. Let G = (V, E, W) be an undirected weighted graph where V =
{1, 2, ..., p} with edge weight wj,k (1 ≤j ̸= k ≤p) associated with edge (j, k) ∈E. The edge weights
corresponding to W = (wj,k) may be negative. Now we deﬁne our covariance graph. Let wj,k = ˆΣj,k,
which denotes the (j, k) entry of the covariance matrix ˆΣ. Then E := {(j, k) : wj,k ̸= 0, j ̸= k} and
the entries of the weight matrix W ∈Rp×p are Wj,k = wj,k. Given this graph, the regularization term
P
j,k |ˆΣj,k|1/2|βj −ˆsj,kβk| is a measure of the graph total variation of the signal β with respect to the graph
G and P
j,k |ˆΣj,k|(βj −ˆsj,kβk)2 corresponds to a graph Laplacian regularizer with respect to G.
Further let Γ be the weighted edge incidence matrix associated with the graph G. Speciﬁcally, we denote
the set of edges in our graph as (jℓ, kℓ) for ℓ= 1, . . . , m where m := |E| is the size of the edge set. Let
Γ =
m
X
ℓ=1
Γℓ,
where
Γℓ:= |ˆΣjℓ,kℓ|1/2uℓ
h
ejℓ−sign(ˆΣjℓ,kℓ)ekℓ
i⊤
∈Rm×p,
(3)
where uℓ∈Rm and eℓ∈Rp are the ℓth canonical basis vectors (all zeros except for a one in the ℓth element).
Then the ℓth row of Γ is
|ˆΣjℓ,kℓ|1/2 h
ejℓ−sign(ˆΣjℓ,kℓ)ekℓ
i⊤
.
3


## Page 4


Next suppose λ1 > 0 and λTV , λS ≥0. We deﬁne
˜X = ˜XλS :=

X
√nλSΓ

∈R(n+m)×p, ˜y :=

y
0m×1

∈Rn+m, and ˜Γ :=
λTVΓ
Ip×p

∈R(m+p)×p.
Using these deﬁnitions, we may write the estimator (2) equivalently as
ˆβ = arg min
β
1
n∥y −Xβ∥2
2 + λS∥Γβ∥2
2 + λ1(λTV∥Γβ∥1 + ∥β∥1)
(4)
= arg min
β
1
n∥˜y −˜Xβ∥2
2 + λ1∥˜Γβ∥1.
(5)
The three regularizers play the following roles:
• We refer to ∥Γβ∥2
2 = P
j,k |ˆΣj,k|(βj −ˆsj,kβk)2 as the Laplacian smoothing penalty; Hebiri and
van de Geer (2011) studied a variant of this regularizer with ˆΣj,k replaced with arbitrary non-negative
weights. Because each term is squared, it helps to reduce the ill-conditionedness of X when columns
are highly correlated, as reﬂected in our analysis.
• We refer to ∥Γβ∥1 = P
j,k |ˆΣj,k|1/2|βj −ˆsj,kβk| as the total variation penalty, as do Shuman et al.
(2013); Wang et al. (2016); Sadhanala et al. (2016); H¨utter and Rigollet (2016); it is closely related
to the edge LASSO penalty (Sharpnack et al., 2012). Note that these prior works consider general
weighted graphs (instead of graphs deﬁned by a covariance matrix ˆΣ, as we do). This regularizer
promotes estimates ˆβ that are well-aligned with the graph structure; for instance, a group of nodes
with large edge weights connecting them (i.e., a group of columns of X that are highly correlated) are
more likely to be associated with coefﬁcient estimates with similar values.
• We refer to ∥β∥1 as the sparsity regularizer. The combination of the sparsity regularizer and total
variation penalty amount to the fused LASSO (Tibshirani et al., 2005; Tibshirani and Taylor, 2011).
The combined effect of the three regularization terms is to ﬁnd estimates of β∗which are both a good
ﬁt to the data when the columns of X are highly correlated and well-aligned with the underlying graph.
This alignment structure may be desirable in a number of settings, including the neural decoding problem
considered in the introduction.
1.3. Contributions
This paper addresses the question of how to estimate β∗from observations in (1) when X has highly-
correlated columns. We propose a regularized regression approach in which the regularization function
depends upon the covariance of X. For a ﬁxed graph G, the proposed estimator is closely related to the
previously-proposed fused LASSO (Tibshirani et al., 2005), generalized LASSO (Tibshirani and Taylor,
2011), edge LASSO (Sharpnack et al., 2012), network LASSO (Hallac et al., 2015), trend ﬁltering (Wang
et al., 2016), and total-variation regularization (Shuman et al., 2013; H¨utter and Rigollet, 2016). In contrast to
these past efforts, our focus is on settings in which columns of X are highly correlated and these correlations
inform the choice of graph G.
On the other hand there is a large body of work on highly dependent features; in Section 1.4 we provide
a thorough comparison of our method with other related approaches. In this paper we make the following
contributions:
• A novel estimator with corresponding ﬁnite-sample theoretical guarantees for highly-correlated de-
sign matrices X. General theoretical guarantees for both mean-squared error and variable selection
4


## Page 5


consistency provide insight into the impact of the alignment of β∗with the covariance graph, and
properties of the covariance graph structure such as smallest and largest block-sizes and smallest
non-zero eigenvalue.
• New mean-squared error guarantees for three speciﬁc covariance graph structures, a block complete
graph, a chain graph, and a lattice graph. Our error bounds match the optimal rates in the independent
case where Σ is a diagonal matrix, and also match the optimal rates for the block and lattice covariance
graphs.
• A simulation study which shows that our method out-performs state-of-the-art alternatives such as the
Cluster Representative LASSO (CRL, B¨uhlmann et al. (2013)) and Ordered Weighted LASSO (OWL,
Bogdan et al. (2013)) in terms of mean squared error in a variety of settings.
• A validation of our method on real biochemistry data that demonstrates the adavantages of GTV.
The remainder of this paper is organized as follows: In Section 1.4 we discuss existing work and results
for this problem and its relationship to our estimator; in Section 2 we present our main theoretical results
for both mean-squared error and variable selection consistency; in Section 3 we carry out a simulation study
by comparing our methods to other state-of-the-art methods; in Section 4 we apply our method to a real
biochemistry dataset with comparison to other methods; we state our conclusions in Section 5; proofs are
provided in the Appendix.
1.4. Prior work
There is a large body of work related to our proposed estimator. Signiﬁcant effort has been devoted to
understanding estimators like (4) in the special case where X = I – that is, in a “denoising” setting in
which observations are direct measurements of the signal of interest, β. Variants of these estimators are
often referred to as the edge or network LASSO (Sharpnack et al., 2012; Hallac et al., 2015), a special
case of graph trend ﬁltering (Wang et al., 2016) or graph total variation estimation (Shuman et al., 2013).
Wang et al. (2016) consider a generalization of graph total variation to higher-order measures of variation
of signals for denoising piecewise-polynomial signals on graphs and derive squared error bounds for the
estimates. H¨utter and Rigollet (2016) also develop sharp oracle inequalities for the edge LASSO, with an
emphasis on a 2d lattice graph used in image processing applications.
In the high-dimensional regression setting, our approach may be viewed as a generalization of the clas-
sical fused LASSO (Tibshirani et al., 2005), where instead of promoting alignment between features with
adjacent indices, we instead promote alignment of features that are neighbors in a graph. Speciﬁcally, the
generalized LASSO of Tibshirani and Taylor (2011); Liu et al. (2013) consider the estimators of the form
ˆβ =arg min
β
1
n∥y −Xβ∥2
2 + λ∥Γβ∥1
(6)
for general X and Γ; note that both the fused LASSO and the estimator in (4) can be written in this form.
The works Caoa et al. (2018) and Viallon et al. (2016) use the generalized LASSO to mitigate correlation
effects similar to the approach described in this work, but without theoretical support. Caoa et al. (2018) aims
to predict Alzheimers disease outcomes using MRI measures as features. The authors use prior knowledge of
correlations between MRI features to construct a regularizer which promotes alignment between correlated
features. Viallon et al. (2016) seeks to predict outcomes in cancer patients based on gene expression data.
The authors leverage side information of gene regulatory networks and promote alignment between adjacent
vertices in the network. This work provides theoretical justiﬁcation for the approaches described in those
papers.
5


## Page 6


A related approach is the clustered LASSO (She, 2010), which takes the form
ˆβ =arg min
β
1
n∥y −Xβ∥2
2 + λTV
X
1≤j<k≤p
|βj −βk| + λ1∥β∥1.
In contrast to the fused LASSO, the clustered LASSO considers all pairwise differences of elements of β.
She (2010) conducts a classical asymptotic analysis (ﬁxed p and n →∞) of the clustered LASSO and its
generalization (6) and establishes consistency results that depend upon Σ−1.
Related work by Needell and Ward (2013b,a) consider the special case of the generalized LASSO of total
variation regularization on a grid for image reconstruction problems. That analysis, while elegant, relies
heavily upon the grid-like graph structure associated with pixels in images and does not generalize to the
setting of this paper.
A key focus of our work is the setting in which columns of X may be highly correlated. There are
several approaches developed to deal with the high-dimensional linear regression problem with some highly
correlated covariates. The Elastic Net estimator proposed by Zou and Hastie (2005) is
ˆβ =arg min
β
∥y −Xβ∥2
2 + λ1∥β∥1 + λS∥β∥2
2,
(7)
which encourages a grouping effect, in which strongly-correlated predictors tend to be in or out of the
support of the estimate together. Witten et al. (2014) propose a Cluster Elastic Net estimator which incor-
porates clustering information inferred from data to perform more accurate regression. The Elastic Corr-net
proposed by El Anbari and Mkhadri (2014) proposes combining an l1 penalty with a correlation based
quadratic penalty from Tutz and Ulbricht (2009).
An alternative approach explored by B¨uhlmann et al. (2013), called Cluster Representative LASSO (CRL),
clusters highly correlated columns of X, chooses a single representative for each cluster, and regresses over
the cluster centers. B¨uhlmann et al. (2013) also considered a Cluster Group LASSO (CGL) in which a group
sparsity regularizer was used with the original design matrix X and the group structure was determined by
a clustering of the columns of X. These two-stage approaches (ﬁrst cluster, then regress based on estimated
clusters) admitted encouraging statistical guarantees and empirical performance. However, (i) they depend
heavily upon our ability to ﬁnd a good clustering of the columns of X, where clusters must be disjoint
or non-overlapping; (ii) clustering decisions are “hard” and do not reﬂect varying degrees of correlation
among columns, and (iii) clusters are formed independently of the observed responses (y). We examine the
performance of CRL in this paper. Grouping pursuit (Shen and Huang, 2010) explores clustering columns
of X while leveraging y by using a non-convex variant of the fused LASSO.
Early work on the adaptive LASSO by Zou (2006) illustrated the impact of adaptivity in the correlated
design setting. Recent work on the Ordered Weighted LASSO (OWL) estimator (Bogdan et al., 2013) pro-
posed an alternative weighted LASSO regularizer in which the weights depend on the order statistics of β;
speciﬁcally,
ˆβ =arg min
β
∥y −Xβ∥2
2 + λ1
p
X
j=1
wj|β|[j],
where w1 ≥w2 ≥... ≥wp ≥0 and |β|[j] is the jth largest element in {|β1|, |β2|, ..., |βp|}, their paper shows
that this family of regularizers can be used for sparse linear regression with strongly correlated covariates.
A special case of OWL is the OSCAR estimator (Bondell and Reich, 2008). Figueiredo and Nowak (2016)
demonstrated that when two columns of X were identical, then OWL would assign the corresponding ele-
ments of β equal values. OWL adaptively groups highly correlated columns of X by assigning them equal
weights whenever their correlation exceeds a critical value – the grouping does not need to be pre-computed
and will depend on the value of y.
6


## Page 7


An estimator called Pairwise Absolute Clustering and Sparsity (PACS) estimator is proposed by Sharma
et al. (2013). Hebiri and van de Geer (2011) consider smooth S-LASSO estimators of the form
ˆβ =arg min
β
1
n∥y −Xβ∥2
2 + λS∥Γβ∥2
2 + λ1∥β∥1.
The ﬁrst regularization term, unlike the total variation term in (4), is a quadratic penalty similar to what
appears in the elastic net (7) (Zou and Hastie, 2005). The analyses by She (2010), Sharma et al. (2013)
and Hebiri and van de Geer (2011) do not consider settings in which X and Γ in (6) are related. A similar
approach to Hebiri and van de Geer (2011) is the weighted fusion estimator proposed by Daye and Jeng
(2009). Daye and Jeng (2009) focus their analysis on grouping effects, sign consistency, and limiting dis-
tributions, but do not consider ﬁnite sample error bounds of the type developed in this paper. The Sparse
Laplacian Shrinkage (SLS) estimator proposed by Huang et al. (2011) uses a minimum concave penalty
(MCP) to replace the LASSO penalty in a weighted fusion estimator to reduce bias.
2. Assumptions and Main Results
We ﬁrst introduce a set of assumptions needed for our main results. Throughout we use the induced matrix
norm notation
∥A∥p,q = sup
x̸=0
∥Ax∥q
∥x∥p
.
Speciﬁcally, note that ∥A∥1,2 is the maximum column norm of A and ∥A∥op = ∥A∥2,2. For a symmet-
ric positive semi-deﬁnite matrix A, let λmin(A) denote its minimum eigenvalue and λmax(A) denote its
maximum eigenvalue.
The notation Xn = OP (an) means that the set of values Xn
an is stochastically bounded. That is, for any
ϵ > 0, there exists a ﬁnite M > 0 and a ﬁnite N > 0 such that
P

Xn
an
 > M

< ϵ, ∀n > N.
Assumption 2.1. We assume that there exists an absolute constant cu > 0 such that
λmax(Σ) ≤cu.
Remark 2.1. This statement assumes that Σ is normalized such that the largest eigenvalue of Σ can be upper
bounded by a positive constant.
Assumption 2.2. There exists an absolute constant cℓ> 0 such that:
cℓ≤min
1≤j≤p
p
X
k=1
|Σj,k|.
Remark 2.2. Assumption 2.2 ensures the ℓ1 norm for each row/column is lower bounded by a constant.
This assumption is much milder than assuming the minimum eigenvalue of Σ is bounded away from 0.
As an example, Assumption 2.2 is satisﬁed when every diagonal entry of Σ is bounded below by cℓ. Note
that Assumption 2.1 automatically holds for appropriately normalized features. However the assumption
is nontrivial when considered jointly with Assumption 2.2, because normalization can potentially cause a
violation of Assumption 2.2. We show that both Assumptions 2.1 and 2.2 hold in the examples considered
in Section 2.2.
7


## Page 8


Assumption 2.3. The estimated covariance matrix ˆΣ that is used to construct the matrix Γ satisﬁes
∥ˆΣ −Σ∥1,1 = max
1≤j≤p
p
X
k=1
|ˆΣj,k −Σj,k| ≤cℓ
4 ,
where cℓis deﬁned in Assumption 2.2.
Remark 2.3. Assumption 2.3 states that we need a sufﬁciently accurate estimator ˆΣ for Σ. If Assumption 2.3
is satisﬁed then we can use ˆΣ to construct Γ for our optimization problem stated in (5). We estimate Σ using
side information that is not necessarily based on (X(i))n
i=1. For instance, in the cytochrome P450 enzyme
setting described in Section 1.1, we can leverage the recombination information of each chimeric protein to
help estimate Σ. We elaborate on this in Section 4.1. In an MRI context, one can leverage prior knowledge
of correlations between MRI features Caoa et al. (2018). In climate forecasting settings, physics-based
simulations can be used to generate accurate covariance estimates.
In some settings, our source of side information may not directly yield an estimate of Σ, but rather a
collection of m i.i.d. unlabeled feature vectors ( ˇX(i))m
i=1 that are potentially independent of the design
features (X(i))n
i=1 with ˇX(i) ∼N(0, Σp×p). In this case, we need to estimate Σ based on ( ˇX(i))m
i=1, and
there is a large literature on high-dimensional covariance estimation in high dimensions under different
structural assumptions (see Bickel and Levina (2008b,a); Cai and Liu (2011); Cai et al. (2016); Donoho
et al. (2013); Baik and Silverstein (2006)). As an example, we consider estimators based on thresholding the
sample covariance matrix under block structural assumptions developed by Bickel and Levina (2008a). We
show that when the covariance matrix is block structured with K blocks, and m = O(K2 log p), Assumption
2.3 is satisﬁed. See Appendix A for more details.
The performance of our estimator also depends upon the following two properties of the augmented edge
incidence matrix ˜Γ appearing in our regularizer:
Deﬁnition 2.1 (Compatibility factor kT , H¨utter and Rigollet (2016)). We deﬁne the compatibility factor kT
of matrix ˜Γ for a set T ⊂{1, 2, ..., p, p + 1, ..., p + m} as:
k∅:= 1, kT := inf
β∈Rp
p
|T|∥β∥2
∥(˜Γβ)T ∥1
for T ̸= ∅.
This compatibility factor kT reﬂects the degree of compatibility of the ℓ1-regularizer ∥(˜Γβ)T ∥1 and the
ℓ2-error norm ∥β∥2 for a set T. This compatibility factor appears explicitly in the bounds of our main
theorem.
Deﬁnition 2.2 (Inverse scaling factor ρ, H¨utter and Rigollet (2016)). Let S := ˜Γ† = [s1, ..., sm+p], where
˜Γ† is the Moore-Penrose pseudoinverse of the matrix ˜Γ, and deﬁne the inverse scaling factor as:
ρ := ∥˜Γ†∥1,2 =
max
j=1,2,...,m+p ∥sj∥2.
Remark 2.4. Deﬁnitions 2.1 and 2.2 are ﬁrst proposed in H¨utter and Rigollet (2016), though the deﬁnition
of ρ is based on ˜Γ rather than Γ. Later we will see that ρ and kT are crucial for our main results. The quantity
ρ
kT is similar in ﬂavour to the condition number of the matrix ˜Γ.
Finally, we deﬁne the estimated graph Laplacian L := Γ⊤Γ. Recall that Γ, and therefore L, are con-
structed using the estimated covariance matrix ˆΣ rather than Σ. Spectral properties of L will play a crucial
role in the mean-squared error bounds we derive.
8


## Page 9


Theorem 1. Suppose λ1 > 0 and Assumptions 2.1 to 2.3 are satisﬁed. If
λ1 ≥max
(
48
r
cuρ2σ2 log p
n
, 8λS∥Lβ∗∥∞
)
,
then there exist absolute positive constants Cu and C1 such that with probability at least 1 −C1
p we have
∥ˆβ −β∗∥2
2 ≤Cu min
T
max
(
λ2
1|T|
k2
T λ2
min(Σ + λSL), λ1∥(˜Γβ∗)T c∥1 + λ2
1∥(˜Γβ∗)T c∥2
1
λmin(Σ + λSL)
)
provided
λ2
1|T|
k2
T λ2
min(Σ+λSL) →0 (i.e., that the estimator is consistent).
Remark 2.5. Here λmin(Σ + λSL) plays the role of the restricted eigenvalue constant (see Bickel et al.
(2009) for more details about this condition). Recall that from the deﬁnition of L, if we deﬁne the diagonal
matrix D ∈Rp×p where each diagonal entry is Djj = Pp
k=1 |ˆΣj,k|, 1 ≤j ≤p, then
Σ + L := Σ −ˆΣ + D.
Hence if Σ and ˆΣ are “close” as is speciﬁed by Assumption 2.3, then Σ + L is “close” to a diagonal matrix
which ensures that λmin(Σ + λSL) may be bounded away from 0, even if λmin(Σ) = 0. The following
Lemma makes this statement precise:
Lemma 1. Suppose that Assumption 2.2 and 2.3 are satisﬁed and 0 ≤λS ≤1. Then
λmin(Σ + λSL) ≥(1 −λS)λmin(Σ) + λS
cℓ
2 .
Thus even if λmin(Σ) = 0, choosing λS bounded away from 0 results in a well-posed inverse problem.
On the other hand, in the classical LASSO analysis where λmin(Σ) > 0, we can choose λS = 0.
Remark 2.6. ∥Lβ∗∥∞can be seen as a measure of the misalignment of the signal β∗and the graph rep-
resented by the matrix Γ. Note that we require λ1 ≥8λS∥Lβ∗∥∞. Hence there is a clear trade-off in the
choice of λS. Choosing λS close to 1 ensures λmin(Σ + λSL) is bounded away from 0 but incurs a cost that
scales with ∥Lβ∗∥∞.
In general, if λmin(Σ) = 0, indicating high correlations, we require ∥Lβ∗∥∞≈0 (i.e., β∗is well-aligned
with L) in order to obtain consistent mean-squared error bounds. Note that analysis of OWL (Figueiredo
and Nowak, 2016) assumes Lβ∗= 0 (perfect alignment). If λmin(Σ) = 0 and ∥Lβ∗∥∞is bounded far away
from 0, we encounter identiﬁability challenges which leads to an inconsistent estimator of β∗, just like the
classical LASSO.
Remark 2.7. A natural question to consider is how the mean-squared error bound would change if the
graph Laplacian penalty λS∥Γβ∥2
2 were replaced by λS∥β∥2
2 as is used in the (Zou and Hastie, 2005). Going
through the analysis, λmin(Σ+λSL) would be replaced by λmin(Σ+λSIp×p) and hence pre-conditioning is
still achieved. However the important difference and why we prefer the graph Laplacian penalty is because
using our analysis the condition λ1 ≥8λS∥Lβ∗∥∞would be replaced by λ1 ≥8λS∥β∗∥∞. Hence if we
were in the strictly sparse case and λTV = 0 we would recover the mean-squared error bound:
∥ˆβ −β∗∥2
2 ⪯(log p
n
+ λ2
S∥β∗∥2
∞)∥β∗∥0
λ2
min(Σ + λSIp×p)
.
9


## Page 10


Note that this exactly matches the mean-squared error bound in (11) in Hebiri and van de Geer (2011)
by replacing ∥β∗∥2
2 with the bound ∥β∗∥0∥β∗∥2
∞. (The estimator of Hebiri and van de Geer (2011) is a
generalization of Elastic Net from Zou and Hastie (2005).) In general we can not expect ∥β∗∥∞to be close
to zero, but in the case where β∗is well-aligned with L, we would expect ∥Lβ∗∥∞to be close to zero which
would achieve sharper bounds.
Now we turn our attention to quantifying kT and ρ to provide a more interpretable bound. We ﬁrst have
the following lemma to bound kT :
Lemma 2. Suppose T = T1 ∪T2 with T1 ⊂{p + 1, p + 2, ..., p + m} and T2 ⊂{1, 2, ..., p}. Then we have
k−1
T
≤
λTV
q
2∥ˆΣ∥1,1|T1| +
p
|T2|
p
|T1| + |T2|
.
The proof for this lemma can be found in Appendix F.
Remark 2.8. The compatibility factor kT depends on the choice of support T. Usually T will be chosen as
T = Supp(˜Γβ) for some β; then T1 = Supp(Γβ) and T2 = Supp(β) and Lemma 2 can be reduced to
k−1
T
≤
λTV
q
2∥ˆΣ∥1,1∥Γβ∥0 +
p
∥β∥0
p
∥Γβ∥0 + ∥β∥0
.
To provide an upper bound for ρ we ﬁrst deﬁne the following graph-based quantities. If G has K con-
nected components where 1 ≤K ≤p, L is block-diagonal with K blocks. Let Lk denote the kth block of
L, Bk ⊂{1, 2, ..., p} denote the nodes corresponding to the kth block, and µk denote the smallest non-zero
eigenvalue of Lk.
Lemma 3. Let G denote the graph associated with ˆΣ. Then
ρ2 ≤max
1≤k≤K
 1
|Bk| +
2
1 + µkλ2
TV

,
where K is the number of connected components in G; |Bk| is the corresponding number of nodes in Bk;
and µk is the smallest nonzero eigenvalue of the weighted Laplacian matrix for the kth connected component.
By combining results from Lemmas 2 and 3 we have the following theorem:
Theorem 2. Suppose Assumptions 2.1 to 2.3 are satisﬁed and we choose
λ1 ≥48
s
σ2cu log p
n
max
1≤k≤K
 1
|Bk| +
2
1 + µkλ2
TV

+ 8λS∥Lβ∗∥∞.
Then there exist absolute positive constants C1 and C such that
∥ˆβ −β∗∥2
2 ≤C λ2
1∥β∗∥0 + min(λ2
1λ2
TV ∥ˆΣ∥1,1∥Γβ∗∥0, λ1λTV ∥Γβ∗∥1)
min(λ2
min(Σ + λSL), λmin(Σ + λSL))
,
with probability at least 1 −C1
p provided λ2
1∥β∗∥0+λ2
1λ2
T V ∥ˆΣ∥1,1∥Γβ∗∥0
λ2
min(Σ+λSL)
→0 and λ1λTV ∥Γβ∗∥1 ≤1.
10


## Page 11


The proof of Theorem 2 is provided in Section B. The upper bound involves a minimum where one term
depends on ∥Γβ∗∥0 and the other depends on ∥Γβ∗∥1 by using different choices of T. This minimum of
two terms also appears in H¨utter and Rigollet (2016). Theorem 2 captures the role of λTV and its impact
on the mean-squared error (MSE) bounds. As λTV increases, ∥β∗∥0 contributes less to the MSE, while
∥Γβ∗∥0 or ∥Γβ∗∥1 contributes more. To see this, note that the lower bound on λ1 decreases with λTV
and the ﬁrst term in the MSE scales as λ2
1∥β∗∥0. On the other hand the second term of the MSE scales
as λ2
1λ2
TV ∥ˆΣ∥1,1∥Γβ∗∥0 or λ1λTV ∥Γβ∗∥1 and the lower bound on λ1λTV increases as λTV increases.
Determining optimal error rates is in general a challenging problem. However, in the special cases of the
block and lattice graphs considered in Section 2.2 our bounds are consistent with known optimal rates. It
is straightforward to extend the proofs of Theorems 1 and 2 in order to derive prediction error bounds on
||X ˆβ −Xβ∗||2
2. This is discussed in more detail in Appendix D.
2.1. Discussion of main results
If we are in the setting where λmin(Σ) > C > 0, which corresponds to the classical LASSO setting, we can
set λS = λTV = 0. From Theorem 2 we can see that
∥ˆβ −β∗∥2
2 ⪯σ2cu log p
n
∥β∗∥0,
(8)
which is consistent with classical LASSO results. On the other hand if λmin(Σ) ≈0 (columns are highly cor-
related) and ∥Lβ∗∥∞≈0 (β∗is well-aligned with L), we can set 0 < λS ≤1 and λTV = C max1≤k≤K
q
|Bk|
µk ;
then we obtain the bound
∥ˆβ −β∗∥2
2 ⪯λ2
1∥β∗∥0 + min(λ2
1λ2
TV ∥ˆΣ∥1,1∥Γβ∗∥0, λ1λTV ∥Γβ∗∥1)
where λ2
1 = O(max1≤k≤K
σ2cu log p
n|Bk|
) and λ2
1λ2
TV = O(max1≤k≤K
|Bk|
µk max1≤k≤K
σ2cu log p
n|Bk|
). The upper
bound may be well below the classical LASSO bound in (8) when mink |Bk| ≫1 and Γβ∗≈0.
As mentioned earlier, if λmin(Σ) ≈0 (columns are highly correlated) but ∥Lβ∗∥∞> C > 0 (bad
alignment), our method cannot guarantee a consistent estimator for β∗; Cluster Representative LASSO and
Ordered Weighted LASSO will also fail in this case. Identiﬁability assumptions arise, since if two columns
of X are nearly identical but the corresponding elements of β∗are substantially different, no method will be
able to accurately estimate parameter values in the absence of additional structure.
We now discuss the roles of the various parameters associated with the MSE bound.
Role of λS
The smoothing penalty plays the role of a pre-conditioner where the trade-off is the addition of
another term λS∥Lβ∗∥∞. This can also be seen in the optimization problem (5) where X is transformed to
˜X, so even if the restricted eigenvalue condition is not satisﬁed for X, it is satisﬁed for ˜X. What distinguishes
our results from previous work using pre-conditioners for the LASSO (Jia et al., 2015; Wauthier et al., 2013)
is that prior work does not address the case where λmin(Σ) = 0, which is where the total variation penalty
is important. See also Remark 2.7.
Role of λTV
As mentioned earlier, the total variation penalty promotes estimates well-aligned with the
graph. As λTV increases, the sparsity parameter λ1 decreases while λ1λTV increases. By increasing λTV
we can also adapt to settings where β∗is not sparse provided that Γβ∗is sparse (see the examples of speciﬁc
graph structures below).
11


## Page 12


Graph-based quantities
Two important parameters of the covariance graph are µk (the smallest non-zero
eigenvalue of a block) and |Bk| (the block size). Clearly the larger µk and |Bk|, the lower the bound on
λ1 which potentially suggests lower mean-squared error. On the other hand, as we illustrate with speciﬁc
examples later, larger µk typically indicates higher correlation between more covariates and larger |Bk|
corresponds to nodes being correlated, which means λmin(Σ) is smaller.
2.2. Speciﬁc covariance graph structures
In this section we explore three speciﬁc graph structures and discuss suitable choices of λS, λ1 and λTV.
For each graph structure we assume
Σjj = a > 0 for 1 ≤j ≤p
and
Σjk = ar ∀(j, k) ∈E for some 0 < r ≤1;
we refer to r as the correlation coefﬁcient. Note that here a is a normalization parameter that we set to
ensure such that Assumptions 2.1 and 2.2 are satisﬁed. We will talk about the speciﬁc choices of a for each
graph structure below. Our general results allow us to quantify the impact of misspeciﬁcation of Σ, but for
interpretability and simplicity of exposition, we will assume in this section that ˆΣ = Σ – that is, that we
have perfect side information about the correlation graph.
2.2.1. Block covariance graph
We ﬁrst consider a block complete graph G that has K connected components and each connected compo-
nent is a complete graph with p
K nodes. The corresponding covariance matrix Σ (potentially after a suitable
permutation of rows and columns) is block diagonal with K blocks of size p
K × p
K . Each of these blocks
can be written as
ar1p/K1⊤
p/K + a(1 −r)Ip/K,
where 1p/K is the vector of p/K ones.
We set a = K
p to ensure that Assumptions 2.1 and 2.2 are satisﬁed. In the extreme case where K = p, we
are in the independent case and the estimator reduces to the standard LASSO estimator; whereas for K = 1,
we are in the fully-connected graph case.
The following lemma provides speciﬁc bounds on max1≤k≤K
1
|Bk|, µk, ρ, λmin(Σ + λSL):
Lemma 4. For a block complete graph with details described above, suppose that ˆΣ = Σ. Then we have
max
1≤k≤K
1
|Bk| = K
p ,
µk = r, for all k
ρ ≤
s
K
p +
2
1 + rλ2
TV
,
λmin(Σ + λSL) ≥(1 −λS)(1 −r)K
p + λSr.
The proof of Lemma 4 is deferred to Appendix H. Note that if r = 1 then λmin(Σ) = 0 but λmin(Σ +
λSL) ≥λS. Using Lemma 4, we have the following mean-squared error bound for the block complete
graph:
12


## Page 13


Corollary 1. For a block complete graph with details described above, suppose that ˆΣ = Σ. If
λ1 ≥48
s
σ2cu log p
n
K
p +
2
1 + rλ2
TV

+ 8λS∥Lβ∗∥∞
and λ1λTV ∥Γβ∗∥1 ≤1. Then with probability at least 1 −C1
p
∥ˆβ −β∗∥2
2 ≤
C
 λ2
1∥β∗∥0 + min{λ2
1λ2
TV ∥Γβ∗∥0, λ1λTV ∥Γβ∗∥1}

min{[(1 −λS)(1 −r)K
p + λSr], [(1 −λS)(1 −r)K
p + λSr]2}
given the estimator is consistent, where C1, C are absolute positive constants.
Consider a setting where r ≈1 and Γβ∗≈0 (near-perfect alignment which corresponds to the parameters
in each block having the same values). Let K1 ≤K denote the number of blocks which have features that
are active in β∗. If we choose λS ≍1, λ2
TV ≍p
K , and λ2
1 ≍K log p
pn
, then
∥ˆβ −β∗∥2
2 ⪯K1 log p
n
;
that is, the MSE is not determined by the number of nonzeros in β∗, but rather by K1, the number of clusters
of active nodes. In the case of perfect correlation between the blocks this matches the minimax optimal rate
up to log factors (Raskutti et al. (2011)). A similar scaling was derived in Figueiredo and Nowak (2016) also
under the assumption that Γβ∗≈0.
2.2.2. Chain covariance graph
The covariance matrix correspnding to the chain graph satisﬁes Σjj = 1 for all j and Σjk = r for all
(j, k) ∈E where E = {(1, 2), (2, 3), ..., (p −1, p)}. Assumptions 2.1 and 2.2 are clearly satisﬁed and
requiring r ∈(0, 1
2) ensures Σ is positive semi-deﬁnite. Note that the chain graph is fully connected so
K = 1 and B1 = {1, 2, ..., p}.
The following lemma provides bounds on ρ and λmin(Σ + λSL) for the chain covariance graph:
Lemma 5. For a chain graph with details described above, suppose that ˆΣ = Σ. Then
ρ ≤
r1
p +
2π
rλTV + 1,
λmin(Σ + λSL) ≥(1 −λS)(1 −2r) + λS.
Using Lemma 5 we have the following corollary for the chain graph:
Corollary 2. For a chain graph with details described above, suppose that ˆΣ = Σ. If we choose
λ1 > 48
s
σ2cu log p
n
1
p +
2π
rλTV + 1

+ 8λS∥Lβ∗∥∞
and λ1λTV ∥Γβ∗∥1 ≤1, then with probability at least 1 −C1
p we have
∥ˆβ −β∗∥2
2 ≤
C
 λ2
1∥β∗∥0 + min{λ2
1λ2
TV ∥Γβ∗∥0, λ1λTV ∥Γβ∗∥1}

min{[(1 −λS)(1 −2r) + λS], [(1 −λS)(1 −2r) + λS]2}
given the estimator is consistent, where C1, C are absolute positive constants.
13


## Page 14


We consider an example where the alignment between the chain graph and β∗is strong but imperfect.
Suppose that within β∗there are O(1) blocks which are active, and within each active block all the coefﬁ-
cients have identical magnitude. Further, suppose n ⪯p. In this setting, ∥Γβ∗∥0, ∥Γβ∗∥1 ≈1.
If we set λTV ≈
p
∥β∗∥0 and λS ≈0 then Corollary 2 says
MSEGTV ⪯
p
∥β∗∥0 log p
n
which is stronger than the LASSO guarantee of
MSELASSO ⪯∥β∗∥0 log p
n
.
2.2.3. Lattice covariance graph
We next consider a covariance structure corresponding to a lattice graph with p nodes (here p must be
a perfect square). Both sides of such a lattice have length √p and the corresponding covariance matrix
satisﬁes
Σj,k =











1,
if j = k,
r,
if |j −k| = 1 and min(j, k) ̸= 0 mod √p,
r,
if |j −k| = √p
0,
else.
We require r ∈(0, 1
4) so that Σ is positive semi-deﬁnite. Clearly Assumptions 2.1 and 2.2 are satisﬁed for
any r ∈(0, 1
4), and we note that the lattice graph is fully connected, so K = 1 and B1 = {1, 2, ..., p}. The
following lemma gives bounds on ρ and λmin(Σ + λSL):
Lemma 6. For a lattice graph with details described above, suppose that ˆΣ = Σ. Then
ρ ≤
s
1
p + 5π log(2 + rλTV )
r2λ2
TV + 1
+
10π
rλTV √p + 1,
λmin(Σ + λSL) ≥(1 −λS)(1 −4r) + λS.
Using Lemma 6 we have the following corollary for the lattice graph:
Corollary 3. For a lattice graph with details described above, suppose that ˆΣ = Σ. If we choose
λ1 > 48
v
u
u
tσ2cu log p
n
 s
1
p + 5π log(2 + rλTV )
r2λ2
TV + 1
+
10π
rλTV √p + 1
!
+ 8λS∥Lβ∗∥∞
and λ1λTV ∥Γβ∗∥1 ≤1, then with probability at least 1 −C1
p we have
∥ˆβ −β∗∥2
2 ≤
C
 λ2
1∥β∗∥0 + min{λ2
1λ2
TV ∥Γβ∗∥0, λ1λTV ∥Γβ∗∥1}

min{[(1 −λS)(1 −4r) + λS], [(1 −λS)(1 −4r) + λS]2}
given the estimator is consistent, where C1, C are absolute positive constants.
14


## Page 15


We again consider an example where the alignment between the graph and β∗is strong but imperfect.
Suppose that all the active nodes within a √p×√p lattice are contained in a
p
∥β∗∥0 ×
p
∥β∗∥0 sublattice,
and suppose all active nodes have equal magnitude. Then ∥Γβ∗∥0, ∥Γβ∗∥1 ≈
p
∥β∗∥0.
We assume n ⪯p and we set λTV ≈√n, λS ≈0 and λ1 ≈log p
n . Corollary 3 says
MSEGTV ⪯λ2
1∥β∗∥0 + λ2
1λ2
TV ∥Γβ∥0 ≈∥β∗∥0 log p
n2
+
p
∥β∗∥0 log p
n
≈
p
∥β∗∥0 log p
n
which is stronger than the LASSO guarantee of
MSELASSO ⪯∥β∗∥0 log p
n
.
Note that the MSEGTV bound from this example is identitcal to the MSEGTV bound from the example
considered in the chain graph section. On one hand, our bound on ρ is stronger in the lattice graph case.
This is consistent with H¨utter and Rigollet (2016) even though we study the inverse scaling factor of a
somewhat different matrix. However, this phenomenon is counterbalanced by the fact that it is easier to
construct near perfect alignment between the chain graph and β∗than between the lattice graph and β∗.
With the chain graph, for any value of ||β∗||0 we can have ||Γβ∗||0 ≈1. However, for the lattice graph it is
impossible to give a general bound on ||Γβ∗||0 which is independent of ||β∗||0. The best possible alignment
yields ||Γβ∗||0 ≈
p
||β∗||0. Our overall rate matches the optimal rates derived in the lattice graph denoising
setting considered in H¨utter and Rigollet (2016).
3. Simulation study
In this section we compare our proposed graph-based regularization method with other methods on the
block, chain and lattice graphs considered in the corollaries above. Speciﬁc details on how the covariance
matrix Σ is constructed for each graph structure is discussed in Section O in the Appendix. The data is
generated according to y = Xβ∗+ ϵ with X ∈Rn×p and y ∈Rn. Each row of X is independently
generated from N(0, Σp×p) and ϵ is generated from N(0, σ2In×n) with σ = 0.01. Additionally, we generate
Xind ∈R1000×p with each row of Xind independently generated from N(0, Σp×p). This Xind provides side
information that can be used to improve estimates of Σ. This Xind can be used for covariance estimation
(GTV) or clustering (CRL) before parameter estimation.
We show how our proposed graph-based regularization scheme compares to existing state-of-the-art
methods in terms of mean-squared error (MSE = ∥ˆβ −β∗∥2
2). For all methods, tuning parameters are
chosen based on ﬁve-fold cross-validation (in the case of GTV, we perform a three-dimensional search to
ﬁnd λ1, λTV and λS). We consider the following estimation procedures:
GTV-Esti (Our method)
Graph-based total variation (GTV) method using original design matrix X ∈
Rn×p for both covariance matrix estimation and parameter estimation. To implement GTV-Esti, we ﬁrst use
X to compute the estimated covariance matrix, ˆΣ, using hard thresholding of the sample covariance matrix
with a threshold is chosen by cross validation (see Bickel and Levina (2008a) for more details). We construct
the edge incidence matrix Γ based on ˆΣ and then estimate ˆβ using (5).
GTV-Indep (Our method)
This approach is equivalent to GTV-Esti (above), except that the side infor-
mation Xind is used to compute the estimated covariance matrix ˆΣ.
15


## Page 16


100
150
200
250
300
p
10-2
100
102
GTV Ind
OWL
Lasso
CRL Ind
EN
GTV Esti
CRL Esti
(a) Block Graph (n = 100, s = 84, r =
0.8)
100
150
200
250
300
p
10-2
100
102
(b) Chain Graph (n = 100, s = 80, r =
0.4)
100
150
200
250
300
p
10-2
100
102
(c) Lattice Graph (n = 250, s = 81,
r = 0.2)
60
70
80
90
100
110
120
n
10-2
100
102
MSE
(d) Block Graph (p = 280, s = 84, r =
0.8)
60
70
80
90
100
110
120
n
10-2
100
102
MSE
(e) Chain Graph (p = 280, s = 80, r =
0.4)
150
200
250
300
350
400
450
n
10-2
100
102
MSE
(f) Lattice Graph (p = 289, s = 81, r =
0.2)
FIG 1. MSE for varying covariance graph structures and values of n and p. Median of 100 trials are shown, and error bars denote
the standard deviation of the median estimated using the bootstrap method with 500 resamplings on the 100 mean-squared errors.
GTV-Esti yields lower MSEs than other methods for a broad range of n, p.
CRL-Esti
Cluster Representative LASSO (CRL) method of B¨uhlmann et al. (2013) using X for both
covariate clustering and parameter estimation. To implement CRL-Esti, we ﬁrst use X for covariate cluster-
ing using canonical correlations in X (see B¨uhlmann et al. (2013, Algorithm 1) for more details), then the
Cluster Representative LASSO is implemented based on the clusters.
CRL-Indep
This approach is equivalent to CRL-Esti (above), except that the side information Xind is
used to improve clustering of the covariates. That is, we run CRL as before, but based on the canonical
correlations computed from Xind.
LASSO
Standard LASSO (Tibshirani, 1996).
Elastic Net
Method from (Zou and Hastie, 2005) which includes both an l1 and an l2 penalty term in order
to encourage grouping strongly correlated predictors.
OWL
Ordered Weighted LASSO (Bogdan et al., 2013). We set the weights for OWL corresponding to the
OSCAR regularizer (Bondell and Reich, 2008), i.e., wi = λ1 + λ2(p −i) with 1 ≤i ≤p and λ1, λ2 ≥0.
We want to investigate how the mean-squared error (MSE) changes with number of observations n and
the number of covariates p. The results are summarized in Figure 1. We show the median MSE of 100 trials
and we add error bars with the standard deviation (of the median) estimated using the bootstrap method
with 500 resamplings on the 100 MSEs. We see that over the different graph structures and values of p, n,
GTV-Esti usually has lower MSE than CRL-Esti, OWL, Elastic Net and LASSO; if we have additional side
information we can achieve better results by using GTV-Indep or CRL-Indep. We can also see that the MSE
decreases as n increases and MSE increases as p or s increases, which is consistent with our theoretical
results.
We next test how the error scales with ∥Γβ∗∥0 and ∥Γβ∗∥1. In Figure 2a we take a chain graph with
p = 280 nodes and let the ﬁrst s = 80 nodes be active. For the active nodes we set β∗
j ∼N(1, σ2) for
16


## Page 17


0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
0.5
0.55
10-1
100
101
102
MSE
GTV Ind
OWL
Lasso
CRL Ind
EN
GTV Esti
CRL Esti
(a) Robustness to increases in σ. An increase in σ causes an in-
crease in ∥Γβ∗∥1 while holding ∥Γβ∗∥0 constant.
0
10
20
30
40
50
||  
||0
10-1
100
101
102
(b) Robustness to increases in ∥Γβ∗∥0.
FIG 2. Chain graph (p=280, n=100, s=80 and r=.4). On left, all active nodes are contained in one continuous block, and active
nodes are chosen from N(1, σ2). On right, active nodes are separated into an increasing number of distinct block, and all active
nodes are chosen from N(1, .012). Plots demonstrate that GTV performs well with moderate amounts of misalignment between the
graph and β∗. Medians of 100 trials are shown, and error bars denote the standard deviation of the median estimated using the
bootstrap method with 500 resamplings on the 100 mean-squared errors.
varying values of σ. In other words we change the value of ∥Γβ∗∥1 while holding ∥Γβ∗∥0 constant. We see
that GTV is reasonably robust to increases in ∥Γβ∗∥1 and still performs well with high levels of noise within
the active block.
In Figure 2b we again look at a chain graph with p = 280 nodes and s = 80 active nodes, but this time
we break up the active nodes into distinct blocks. Each active node is chosen from N(1, .012). We measure
MSE a function of the number of distinct blocks the active nodes are divided into. In other words, this setting
measures robustness to l0 misalignment as opposed to l1 misalignment. We see that GTV performs well
even when ∥Γβ∗∥0 is reasonably large, again suggesting that our methods are robust to moderate amounts
of misalignment between the graph and β∗.
4. Biochemistry application: Cytochrome P450 enzymes
In this section we describe an application of the proposed GTV methodology to protein thermostability
data. As described in Section 1.1, the thermostability data we use was provided by the Romero Lab at
UW-Madison. The data contains thermostability measurements for 242 proteins in the P450 protein family.
For each protein, 50 structure features were simulated via RosettaCommons (Alford et al., 2017) and the
goal is to understand the relationship between the 50 structural features and thermostability. Hence the
design matrix X ∈R242×50 consists of the structural features. The response variable y ∈R242 contains
the thermostability measurements. Additionally, we have side information in the form of the amino acid
sequences that make each of the 242 proteins; this is used to estimate the covariance matrix amongst the
structural features.
4.1. Estimation of the covariance matrix with side information
One advantage of our GTV method is that side information can be incorporated to estimate the strength of
correlations among features. It is a well known fact that the structure of the protein is a function of its amino
acid sequence. We exploit this sequence and structure relationship and model the structural features as linear
functions of sequence features. Then we use this model to obtain a better approximation of the covariance
of structural features.
17


## Page 18


P1
P2
P3
…
Chimera enzymes
Block1
Block2
Block3
Block4
Block5
Block6
Block7
Block8
FIG 3. A diagram of the process of creating Chimeras enzymes. P1, P2, and P3 are three parent proteins. They are each made up
of an amino acid sequence (represented by red, yellow, or blue). There are 8 pieces/blocks in each sequence. Chimera enzymes are
made from recombining blocks from the 3 parents. The P450 dataset we use consist of Chimeras.
The proteins were created by the recombination of 3 other proteins. Each protein’s amino acid sequence
can be thought of as having 8 pieces/blocks where each piece came from one of 3 parent proteins (Figure
3). So the amino acid sequence can be represented as 8 categorical features, each with 3 categories. Each
feature represents one piece of the sequence and indicates which parent that piece came from. We can use
the one-hot encoding of these 8 categorical features to obtain 24 binary features that represent an amino acid
sequence for a protein. Because each piece comes from one of three parents, the sum of the 3 binary features
for each piece of the sequence must be 1. So only 2 parameters are needed for each piece of the sequence.
Hence a model of the amino acid sequence has K = 16 parameters.
Hence we model p = 50 structural features as linear functions of K = 16 binary sequence features via a
multivariate linear regression model. More concretely, we assume a linear model
X(i) = AT S(i) + δ(i)
(9)
where X(i) ∈Rp is a vector of the ith structural feature and S(i) ∈(0, 1)K is the binary sequence features
of the ith enzyme in the dataset. The matrix A ∈RK×p is an unknown parameter matrix which determines
the relationship between X(i) and S(i), and we assume Gaussian noise δ(i) ∼N(0, σ2
δ) independent from
S(i) and ϵ(i). We note that the model assumption (9) amounts to assuming that the thermostability y can be
modeled by the sequence matrix S which is of rank K. Although modeling y directly via S is possible, the
results will not provide an understanding of how structural features contribute to the thermostability of a
protein, which is the goal of our analysis.
Exploiting the structure of X in (9), we estimate the covariance matrix of X given sequence S as
bΣind := c
Var(E[X(i)|S(i)]) = bAT c
Var(S(i)) bA = bAT bΣs bA,
where bΣs is an empirical covariance matrix of (S(i))n
i=1 and bA is the LSE of A, i.e.
bA = arg
min
A∈RK×p ∥X −SA∥2
F .
We note that the dimensions of A and Σs are K by p and K by K, respectively. Thus we reduce the
estimation problem of a p by p matrix to a smaller problem, with K = 16 being much less than p = 50.
18


## Page 19


4.2. Results
We compare our GTV method (with and without side information) with Ordered Weighted LASSO (OWL),
Cluster Representative LASSO (CRL), and the standard LASSO (LASSO), and the Elastic Net (EN) method.
For all models, the tuning parameters were selected via ﬁve-fold cross validation on the training set. For
OWL, the weights were set corresponding to the OSCAR regularizer.
To compare the performance of the ﬁve methods on the real P450 data, we considered two performance
criteria: prediction accuracy and stability of estimated coefﬁcients. To measure stability between estimated
coefﬁcients, we considered following two criteria:
1. Cor(ˆβi, ˆβj) where ˆβi and ˆβj are estimates from two different ﬁttings for the same model.
2. Tanimoto Distance (Kalousis et al., 2007):
D(i, j) := 1 −| supp(ˆβi)| + | supp(ˆβj)| −2| supp(ˆβi) ∩supp(ˆβj)|
| supp(ˆβi)| + | supp(ˆβj)| −| supp(ˆβi) ∩supp(ˆβj)|
where supp refers to the support set.
For prediction accuracy, we use 10-fold cross validation. We trained the six models on each training set and
evaluated the prediction performances on the test set. On the other hand, stability measures were calculated
by spliting the entire P450 dataset into ten non-overlapping subsamples and ﬁtting the six models using each
of the subsamples.
Table 1 summarizes prediction accuracy. The result for EN is excluded since the tuning parameter for the
l2 penalty λS was chosen to be 0 in all cross-validation folds, and the result for EN is the same as LASSO.
From the Table 1, we see that GTV Esti has the highest accuracy. GTV Ind (GTV with side information)
is the next most accurate. CRL Ind and CRL Esti show very bad prediction performance. CRL is expected
to perform badly in the case where variables are not grouped into tight clusters or coefﬁcients within a
group have opposite signs and their sum is close to zero B¨uhlmann et al. (2013). In our application, in most
cross-validation folds Algorithm 1 in B¨uhlmann et al. (2013) resulted in one huge cluster in the case of
CRL Esti, whose member features do not have similar effects on the response variable. We observed similar
phenomenon in the case of CRL Ind, although to a lesser extent than the CRL Esti, where we observed one
cluster with nine features with opposite effects and the remaining clusters are of size 1. As a result, both
CRL methods demonstrated very poor prediction results.
GTV Ind
GTV Esti
LASSO
CRL Ind
CRL Esti
OWL
MSE
5.10
5.08
5.11
13.78
31.21
5.35
TABLE 1
The average Mean Squared Error for each model on the P450 dataset.
Figure 4 demonstrates the correlation and variable selection stability. GTV Ind and GTV Esti show the
most stable performances overall. In terms of correlations, all ﬁve methods generated highly correlated coef-
ﬁcients across different ﬁts, except OWL which had a few outliers. For variable selection stability, both GTV
methods and OWL produced the same support sets in all ﬁts. On the contrary, the support sets from LASSO
and both CRL methods greatly varied across ﬁts. Only about 30% of the support sets overlap between any
pair of ﬁts. It appears that relatively strong correlation in the design but the lack of tightly grouped clusters
contributed to the instability of clustering and support recovery in LASSO and CRL methods.
19


## Page 20


0.5
0.6
0.7
0.8
0.9
1.0
CRL Esti
CRL Ind
GTV Esti
GTV Ind
LASSO
OWL
Method
Correlation
(a) Correlation stability
0.25
0.50
0.75
1.00
CRL Esti
CRL Ind
GTV Esti
GTV Ind
LASSO
OWL
Method
Tanimoto Distance
(b) Tanimoto distance
FIG 4. Box Plots of the two stability measures of each model on the P450 dataset. Correlation and Tanimoto distance were calcu-
lated between 10 different ﬁttings for each model, leading to 45 measurements per model for each kind of the stability measrue.
5. Conclusion
This paper describes a new graph-based regularization method for high-dimensional regression with highly-
correlated designs and alignment between the covariance and regression coefﬁcients. The structure of the
estimator leverages ideas behind the Elastic Net (Zou and Hastie, 2005), the Fused LASSO (Tibshirani et al.,
2005), the edge LASSO (Sharpnack et al., 2012), trend ﬁltering on graphs (Wang et al., 2016), and graph
total variation (Shuman et al., 2013; H¨utter and Rigollet, 2016). Under our model, the graph corresponding
to the covariance structure of the covariates also provides prior information about the similarities among
elements in the regression weights. Thus this graph allows us to effectively pre-condition our design matrix
and regularize regression weights to promote alignment with the covariance structure of the problem. We
are able to provide mean-squared error bounds in settings where covariates are highly dependent, provided
there is alignment between the β∗and graph. We also demonstrate in both simulations and a biochemistry
application superior performance of our method compared to LASSO, Elastic Net and CRL. The proposed
framework allows us to leverage correlation structure jointly with the response variable y, in contrast to
previous work that depended upon clustering covariates independent of the responses. In settings where
there exist very strong clusters (like the block graph studied above), clustering with and without responses
yield similar results. However, when correlations are too weak to reveal strong clusters and yet too strong for
the LASSO alone to be effective (like with the chain and lattice graphs studied above), the implicit response-
based clustering associated with our method can yield signiﬁcant performance beneﬁts. The results in this
paper suggest several exciting avenues for future exploration, including more reﬁned performance bounds
for additional classes of graphs and more extensive evaluations on real-world data.
6. Acknowledgement
The authors would like to thank Ian Kinsella for helpful discussions, suggestions, and preliminary experi-
ments. The authors would also like to thank Philip Romero and Jerry Duan for creating and providing access
to the biochemistry example.
20


## Page 21


References
Alford, R. F., A. Leaver-Fay, J. R. Jeliazkov, M. J. O’Meara, F. P. DiMaio, H. Park, M. V. Shapovalov,
P. D. Renfrew, V. K. Mulligan, K. Kappel, J. W. Labonte, M. S. Pacella, R. Bonneau, P. Bradley, R. L.
Dunbrack, Jr, R. Das, D. Baker, B. Kuhlman, T. Kortemme, and J. J. Gray (2017, June). The rosetta
All-Atom energy function for macromolecular modeling and design. J. Chem. Theory Comput. 13(6),
3031–3048.
Anderson, T. W. (1984). An Introduction to Multivariate Statistical Analysis. Wiley Series in Probability
and Mathematical Statistics. New York: Wiley.
Baik, J. and J. W. Silverstein (2006, July).
Eigenvalues of large sample covariance matrices of spiked
populations models. Journal of Multivariate Analysis 97(6), 1382–1408.
Barnston, A. G. and T. M. Smith (1996). Speciﬁcation and prediction of global surface temperature and
precipitation from global sst using cca. Journal of Climate 9(11), 2660–2697.
Bickel, P. and E. Levina (2008a). Covariance estimation by thresholding. The Annals of Statistics 36,
2577–2604.
Bickel, P. and E. Levina (2008b). Regularized estimation of large covariance matrices. The Annals of
Statistics 36, 199–227.
Bickel, P., Y. Ritov, and A. Tsybakov (2009). Simultaneous analysis of Lasso and Dantzig selector. The
Annals of Statistics 37(4), 1705–1732.
Bogdan, M., E. van den Berg, W. Su, and E. Candes (2013). Statistical estimation and testing via the ordered
ℓ1 norm. Technical Report arXiv:1310.1969.
Bondell, H. D. and B. J. Reich (2008). Simultaneous regression shrinkage, variable selection, and supervised
clustering of predictors with oscar. Biometrics 64(1), 115–123.
Boucheron, S., G. Lugosi, and P. Massart (2013). Concentration inequalities: A nonasymptotic theory of
independence. Oxford university press.
B¨uhlmann, P., P. R¨utimann, S. van de Geer, and C. Zhang (2013). Correlated variables in regression: clus-
tering and sparse estimation. Journal of Statistical Planning and Inference 143(11), 1835–1858.
Cai, T. T. and W. Liu (2011). Adaptive thresholding for sparse covariance matrix estimation. Journal of the
American Statistical Association 106(494), 672–684.
Cai, T. T., R. Zhao, and H. H. Zhou (2016). Estimating structured high-dimensional covariance and precision
matrices: Optimal rates and adaptive estimation. Electron. J. Statist. 10(1), 1–59.
Candes, E. and T. Tao (2007). The Dantzig selector: Statistical estimation when p is much larger than n.
The Annals of Statistics 35(6), 2313–2351.
Caoa, P., X. Liua, H. Liuc, J. Yanga, D. Zhaoa, M. Huang, and O. Zaiane (2018). Generalized fused group
lasso regularized multi-task feature learning for predicting cognitive outcomes in alzheimers disease.
Computer Methods and Programs in Biomedicine 162, 19–45.
Davidson, K. R. and S. J. Szarek (2001). Local operator theory, random matrices, and Banach spaces. In
Handbook of Banach Spaces, Volume 1, pp. 317–336. Amsterdan, NL: Elsevier.
Daye, Z. and X. Jeng (2009). Shrinkage and model selection with correlated variables via weighted fusion.
Computational Statistics & Data Analysis 53(4), 1284–1298.
DelSole, T. and A. Banerjee (2017). Statistical seasonal prediction based on regularized regression. Journal
of Climate 30(4), 1345–1361.
Donoho, D. L., M. Gavish, and I. M. Johnstone (2013). Optimal shrinkage of eigenvalues in the spiked
covariance model. arXiv preprint arXiv:1311.0851.
El Anbari, M. and A. Mkhadri (2014). Penalized regression combining the ℓ1 norm and a correlation based
penalty. Sankhya 76(1), 82102.
Figueiredo, M. and R. Nowak (2016). Ordered weighted ℓ1 regularized regression with strongly corre-
21


## Page 22


lated covariates: Theoretical aspects. In Proceedings of the 19th International Conference on Artiﬁcial
Intelligence and Statistics, pp. 930–938.
Geisler, J. E., M. L. Blackmon, G. T. Bates, and S. Munoz (1985). Sensitivity of january climate response
to the magnitude and position of equatorial paciﬁc sea surface temperature anomalies. Journal of the
atmospheric sciences 42(10), 1037–1049.
Guengerich, F. P. (2002, May). Cytochrome P450 enzymes in the generation of commercial products. Nat.
Rev. Drug Discov. 1(5), 359–366.
Hallac, D., J. Leskovec, and S. Boyd (2015). Network lasso: Clustering and optimization in large graphs.
In Proceedings of the 21th ACM SIGKDD international conference on knowledge discovery and data
mining, pp. 387–396. ACM.
Hastie, T., R. Tibshirani, and M. Wainwright (2015). Statistical learning with sparsity: the lasso and gener-
alizations. CRC press.
Hebiri, M. and S. van de Geer (2011). The smooth-lasso and other ℓ1+ℓ2-penalized methods. Electronic
Journal of Statistics 5, 1184–1226.
Huang, J., S. Ma, H. Li, and C.-H. Zhang (2011, 08). The sparse laplacian shrinkage estimator for high-
dimensional regression. Ann. Statist. 39(4), 2021–2046.
H¨utter, J. and P. Rigollet (2016).
Optimal rates for total variation denoising.
arXiv preprint
arXiv:1603.09388.
Jia, J., K. Rohe, et al. (2015). Preconditioning the lasso for sign consistency. Electronic Journal of Statis-
tics 9(1), 1150–1172.
Kalousis, A., J. Prados, and M. Hilario (2007). Stability of feature selection algorithms: a study on high-
dimensional spaces. Knowledge and information systems 12(1), 95–116.
Ledoux, M. and M. Talagrand (1991). Probability in Banach Spaces: Isoperimetry and Processes. New
York, NY: Springer-Verlag.
Li, Y., D. A. Drummond, A. M. Sawayama, C. D. Snow, J. D. Bloom, and F. H. Arnold (2007, September).
A diverse family of thermostable cytochrome p450s created by recombination of stabilizing fragments.
Nat. Biotechnol. 25(9), 1051–1056.
Liu, J., L. Yuan, and J. Ye (2013). Dictionary lasso: Guaranteed sparse recovery under linear transformation.
arXiv preprint arXiv:1305.0047.
Mamalakis, A., J.-Y. Yu, J. T. Randerson, A. AghaKouchak, and E. Foufoula-Georgiou (2018). A new
interhemispheric teleconnection increases predictability of winter precipitation in southwestern us. Nature
communications 9(1), 2332.
Marial, J. and B. Yu (2013). Supervised feature selection in graphs with path coding penalties and network
ﬂows. Journal of Machine Learning Research 14, 2449–2485.
Needell, D. and R. Ward (2013a). Near-optimal compressed sensing guarantees for total variation mini-
mization. IEEE Transactions on Image Processing 22(10), 3941–3949.
Needell, D. and R. Ward (2013b). Stable image reconstruction using total variation minimization. SIAM
Journal on Imaging Sciences 6(2), 1035–1058.
Negahban, S., P. Ravikumar, M. J. Wainwright, and B. Yu (2012). A uniﬁed framework for high-dimensional
analysis of m-estimators with decomposable regularizers. Statistical Science 27(4), 538–557.
Niehaus, F., C. Bertoldo, M. K¨ahler, and G. Antranikian (1999, June). Extremophiles as a source of novel
enzymes for industrial application. Appl. Microbiol. Biotechnol. 51(6), 711–729.
Noschese, S., L. Pasquini, and L. Reichel (2013). Tridiagonal toeplitz matrices: properties and novel appli-
cations. Numerical linear algebra with applications 20(2), 302–326.
P. Zhao, G. R. and B. Yu (2009). The composite absolute penalties family for grouped and hierarchical
variable selection. Annals of Statistics 37(6A), 3468–3497.
22


## Page 23


Raskutti, G., M. J. Wainwright, and B. Yu (2010). Restricted eigenvalue conditions for correlated Gaussian
designs. Journal of Machine Learning Research 11, 2241–2259.
Raskutti, G., M. J. Wainwright, and B. Yu (2011). Minimax rates of estimation for high-dimensional linear
regression over ℓq-balls. IEEE Transactions on Information Theory 57(10), 6976–6994.
Raskutti, G. and M. Yuan (2015). Convex regularization for high-dimensional tensor regression. arXiv
preprint arXiv:1512.01215.
Sadhanala, V., Y. Wang, and R. Tibshirani (2016). Total variation classes beyond 1d: Minimax rates, and the
limitations of linear smoothers. In Advances in Neural Information Processing Systems, pp. 3513–3521.
Sharma, D. B., H. D. Bondell, and H. H. Zhang (2013). Consistent group identiﬁcation and variable selection
in regression with correlated predictors. Journal of Computational and Graphical Statistics 22(2), 319–
340.
Sharpnack, J., A. Singh, and A. Rinaldo (2012). Sparsistency of the edge lasso over graphs. In Artiﬁcial
Intelligence and Statistics, pp. 1028–1036.
She, Y. (2010). Sparse regression with exact clustering. Electronic Journal of Statistics 4, 1055–1096.
Shen, X. and H.-C. Huang (2010). Grouping pursuit through a regularization solution surface. Journal of
the American Statistical Association 105(490), 727–739.
Shuman, D. I., S. K. Narang, P. Frossard, A. Ortega, and P. Vandergheynst (2013). The emerging ﬁeld of
signal processing on graphs: Extending high-dimensional data analysis to networks and other irregular
domains. IEEE Signal Processing Magazine 30(3), 83–98.
Slepian, D. (1962). The one-sided barrier problem for gaussian noise. Bell System Tech. J 41, 463–501.
Strang, G. (2007). Computational Science and Engineering. Wellesley, MA: Wellesley-Cambridge Press.
Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. Journal of the Royal Statistical
Society, Series B 58(1), 267–288.
Tibshirani, R., M. Saunders, S. Rosset, J. Zhu, and K. Knight (2005). Sparsity and smoothness via the fused
lasso. Journal of the Royal Statistical Society: Series B (Statistical Methodology) 67(1), 91–108.
Tibshirani, R. and J. Taylor (2011, 06). The solution path of the generalized lasso. The Annals of Statis-
tics 39(3), 1335–1371.
Tutz, G. and J. Ulbricht (2009). Penalized regression with correlation-based penalty. Statistics and Com-
puting 19(3), 239253.
van de Geer, S. (2000). Empirical Processes in M-Estimation. Cambridge University Press.
van de Geer, S. and P. Buhlmann (2009). On the conditions used to prove oracle results for the lasso.
Electronic Journal of Statistics 3, 1360–1392.
Viallon, V. andLambert-Lacroix, S., H. Hoeﬂing, and F. Picard (2016). On the robustness of the generalized
fused lasso to prior speciﬁcations. Statistics and Computing 26(1), 285–301.
Wang, Y., J. Sharpnack, A. Smola, and R. Tibshirani (2016). Trend ﬁltering on graphs. Journal of Machine
Learning Research 17(105), 1–41.
Wauthier, F. L., N. Jojic, and M. I. Jordan (2013). A comparative framework for preconditioned lasso al-
gorithms. In Advances in Neural Information Processing Systems 26, pp. 1061–1069. Curran Associates,
Inc.
Witten, D., A. Shojaie, and F. Zhang (2014, 2). The cluster elastic net for high-dimensional regression with
unknown variable grouping. Technometrics 56(1), 112–122.
Wu, T. T., Y. F. Chen, T. Hastie, E. Sobel, and K. Lange (2009). Genome-wide association analysis by lasso
penalized logistic regression. Bioinformatics 25(6), 714–721.
Zou, H. (2006). The adaptive lasso and its oracle properties. Journal of the American Statistical Associa-
tion 101(476), 1418–1429.
Zou, H. and T. Hastie (2005). Regularization and variable selection via the elastic net. Journal of the Royal
23


## Page 24


Statistical Society, Series B (67(2)), 301–320.
24


## Page 25


Appendix A: Covariance estimation
Assume we observe a collection of m i.i.d. unlabeled feature vectors ( ˇX(i))m
i=1 that may be independent
of the design features (X(i))n
i=1 with ˇX(i) ∼N(0, Σp×p). In this case, we need to estimate Σ based on
( ˇX(i))m
i=1, and there is a large literature on high-dimensional covariance estimation in high dimensions
under different structural assumptions (see Bickel and Levina (2008b,a); Cai and Liu (2011); Cai et al.
(2016); Donoho et al. (2013); Baik and Silverstein (2006)). As an example, we consider estimators based on
thresholding the sample covariance matrix under block and sparsity assumptions developed by Bickel and
Levina (2008a).
A.1. Sparse covariance matrix
To be speciﬁc, suppose the true covariance matrix Σ belongs to the following class:
Ω(q, c0(p), M) =
(
Σ : Σj,j ≤M,
p
X
k=1
|Σj,k|q ≤c0(p), for all j
)
,
where 0 ≤q < 1, c0(p) is a constant that depends on p and M is an absolute constant. Then Bickel and
Levina (2008a, Theorem 1) show that if we deﬁne the thresholded covariance matrix ˆΣj,k = Sj,k1(|Sj,k| ≥
t) for all 1 ≤j, k ≤p where S is the sample covariance matrix and t = O
q
log p
m

, then
∥ˆΣ −Σ∥1,1 = OP
 
c0(p)M
log p
m
 1−q
2
!
.
Though the original error bound result for ˆΣ−Σ in Bickel and Levina (2008a) was shown in operator norm,
they bounded ∥ˆΣ −Σ∥1,1 in the proof. In particular if q = 0 and c0(p) ≤s denotes the sparsity level,
∥ˆΣ −Σ∥1,1 = OP
 
s
r
log p
m
!
,
meaning if m = O(s2 log p), Assumption 2.3 is satisﬁed.
A.2. Block covariance matrix
On the other hand, if the covariance matrix Σ is not sparse but rather block-structured, we can use an
alternative bound developed in Bickel and Levina (2008a). If Σ has K identical blocks where each block
has p/K elements, we can ensure Assumptions 2.1 and 2.2 are satisﬁed if Σj,k = O(K
p ) for each non-zero
Σj,k. Then if we choose ˆΣ to be the sample covariance matrix, Bickel and Levina (2008a) prove that
max
j,k

ˆΣj,k −Σj,k
K/p
 = OP
 r
log p
m
!
(10)
since now we have Σj,j
K/p = O(1) for 1 ≤j ≤p. Thus by (10) we know that
max
j,k |ˆΣj,k −Σj,k| = OP
 
K
p
r
log p
m
!
(11)
25


## Page 26


and
∥ˆΣ −Σ∥1,1 = max
1≤j≤p
p
X
k=1
|ˆΣj,k −Σj,k| = OP
 
K
r
log p
m
!
by (11), so that when m = O(K2 log p) Assumption 2.3 is satisﬁed.
Appendix B: Proof of Theorem 1
Much of our analysis follows standard steps for analysis of regularized M-estimators (see Bickel et al.
(2009); Negahban et al. (2012); van de Geer (2000)), but we face two additional challenges not present in
these works. First, since the regularization penalty in Equation (5) is ∥˜Γβ∥1 rather than ∥β∥1 we need to
deal with error terms involving ˜X˜Γ† instead of ˜X. To address this we incorporate techniques from H¨utter
and Rigollet (2016) and Raskutti and Yuan (2015). Second, we need to establish a restricted eigenvalue
condition for ˜X rather than X. We incorporate techniques from Raskutti et al. (2010) in order to accomplish
this.
Based on the optimization problem (5), by the deﬁnition of ˆβ and the basic inequality,
1
n∥˜y −˜X ˆβ∥2
2 + λ1∥˜Γˆβ∥1 ≤1
n∥˜y −˜Xβ∗∥2
2 + λ1∥˜Γβ∗∥1.
By simple re-arrangement,
1
n∥˜X(ˆβ −β∗)∥2
2 ≤2
n(˜y −˜Xβ∗)⊤˜X(ˆβ −β∗) + λ1(∥˜Γβ∗∥1 −∥˜Γˆβ∥1).
For the remainder of the proof let ∆:= ˆβ −β∗. Then
1
n∥˜X∆∥2
2 ≤2
n(˜y −˜Xβ∗)⊤˜X∆+ λ1(∥˜Γβ∗∥1 −∥˜Γˆβ∥1).
First we control the term (˜y −˜Xβ∗)⊤˜X∆. Using basic algebra,
(˜y −˜Xβ∗)⊤˜X∆
=
ϵ⊤X∆−nλSβ∗⊤Γ⊤Γ∆.
Since ˜Γ†˜Γ = Ip×p, where ˜Γ† is the pseudo-inverse of ˜Γ. Therefore
ϵ⊤X∆
=
ϵ⊤X˜Γ†˜Γ∆
≤
∥(X˜Γ†)⊤ϵ∥∞∥˜Γ∆∥1.
We next bound nλSβ∗⊤Γ⊤Γ∆by
nλSβ∗⊤Γ⊤Γ∆
≤
nλS∥Γ⊤Γβ∗∥∞∥∆∥1
≤
nλS∥Lβ∗∥∞∥˜Γ∆∥1
≤
nλ1
8 ∥˜Γ∆∥1,
where the last inequality follows from the constraint that λ1 ≥8λS∥Lβ∗∥∞. Now recall the constraint
λ1 ≥48ρσ
q
cu log p
n
, the following lemma shows that with high probability we have λ1 ≥8
n∥(X˜Γ†)⊤ϵ∥∞.
26


## Page 27


Lemma 7. Suppose we have λ1 ≥48ρσ
q
cu log p
n
. Then with probability at least 1 −C1
p ,
λ1 ≥8
n∥(X˜Γ†)⊤ϵ∥∞
for absolute constant C1 > 0.
Combining the constraints for λ1 with the inequalities above,
2
n(˜y −˜Xβ∗)⊤˜X∆
≤
λ1
4 ∥˜Γ∆∥1 + λ1
4 ∥˜Γ∆∥1 = λ1
2 ∥˜Γ∆∥1.
Putting these pieces together we have
1
n∥˜X∆∥2
2
≤
λ1
2 (∥˜Γ∆∥1 + 2∥˜Γβ∗∥1 −2∥˜Γˆβ∥1).
(12)
Furthermore by the triangle inequality and the fact that 1
n∥˜X∆∥2
2 ≥0 we have
0 ≤∥˜Γ(ˆβ −β∗)∥1 + 2∥˜Γβ∗∥1 −2∥˜Γˆβ∥1
≤
3∥(˜Γ∆)T ∥1 −∥(˜Γ∆)T c∥1 + 4∥(˜Γβ∗)T c∥1.
Therefore ∆lies in the translated cone
C := {v : ∥(˜Γv)T c∥1
≤
3∥(˜Γv)T ∥1 + 4∥(˜Γβ∗)T c∥1}.
(13)
Moreover by the deﬁnition of kT we have
∥(˜Γ∆)T ∥1 ≤
p
|T|∥∆∥2
kT
;
from (12) we have
1
2n∥˜X∆∥2
2 ≤λ1∥(˜Γβ∗)T c∥1 + 3λ1
4kT
p
|T|∥∆∥2.
(14)
B.1. Restricted Eigenvalue Condition
From (12) and (13) we need to lower bound
∥˜X∆∥2
2
n
= ∆⊤
X⊤X
n
+ λSL

∆,
for all ∆belonging to the cone C deﬁned in (13). The result is stated in the following lemma:
Lemma 8. For all ∆belonging to the cone deﬁned in (13) if we have
λ1 ≤c2
s
λmin(Σ + λSL)
|T|
kT ,
(15)
then
∆⊤(X⊤X
n
+ λSL)∆≥c1λmin(Σ + λSL)∥∆∥2
2 −c3λ2
1∥(˜Γβ∗)T c∥2
1
(16)
holds with probability at least 1 −c4 exp(−c5n), where ci > 0 for i = 1, ..., 5 are positive constants.
The proof for this lemma is is based on a technique used in Raskutti et al. (2010).
27


## Page 28


B.2. Final Part for Proof
From (14) and (16),
c1λmin(Σ + λSL)∥∆∥2
2
−
c3λ2
1∥(˜Γβ∗)T c∥2
1 ≤2λ1∥(˜Γβ∗)T c∥1 + 3λ1
2kT
p
|T|∥∆∥2,
which is a quadratic inequality involving ∥∆∥2 as follows:
a∥∆∥2
2 −b∥∆∥2 −c ≤0
with
a
=
1,
b
=
3λ1
p
|T|
2c1kT λmin(Σ + λSL),
c
=
1
c1λmin(Σ + λSL)(2λ1∥(˜Γβ∗)T c∥1 + c3λ2
1∥(˜Γβ∗)T c∥2
1).
By solving this quadratic inequality,
∥∆∥2
2 ≤4 max{b2, |c|}.
Therefore these exists a positive constant Cu such that
∥ˆβ −β∗∥2
2 ≤Cu max
(
λ2
1|T|
k2
T λ2
min(Σ + λSL), λ1∥(˜Γβ∗)T c∥1 + λ2
1∥(˜Γβ∗)T c∥2
1
λmin(Σ + λSL)
)
.
Note that the above inequality is true for all T, thus
∥ˆβ −β∗∥2
2 ≤Cu min
T
max
(
λ2
1|T|
k2
T λ2
min(Σ + λSL), λ1∥(˜Γβ∗)T c∥1 + λ2
1∥(˜Γβ∗)T c∥2
1
λmin(Σ + λSL)
)
.
This completes the proof.
Appendix C: Proof of Theorem 2
The upper bound result ∥ˆβ −β∗∥2
2 stated in Theorem 1 holds for all choices of T. If we choose T =
supp(˜Γβ∗) then ∥(˜Γβ∗)T c∥1 = 0 and by Lemma 2,
k−1
T
≤
λTV
q
2∥ˆΣ∥1,1∥Γβ∗∥0 +
p
∥β∗∥0
p
∥Γβ∗∥0 + ∥β∗∥0
.
Then by Theorem 1 we have
∥ˆβ −β∗∥2
2 ≤
2Cu
λ2
min(Σ + λSL)(λ2
1∥β∗∥0 + 2λ2
1λ2
TV∥ˆΣ∥1,1∥Γβ∗∥0).
(17)
On the other hand if we choose T = supp(β∗), ∥(˜Γβ∗)T c∥1 = λTV∥Γβ∗∥1 and by Lemma 2, k−1
T
≤1.
Thus if λ1λTV∥Γβ∗∥1 ≤1 by Theorem 1
∥ˆβ −β∗∥2
2 ≤Cu

λ2
1∥β∗∥0
λ2
min(Σ + λSL) + 2λ1λTV∥Γβ∗∥1
λmin(Σ + λSL)

.
(18)
Theorem 2 follows by combining (17) and (18) and taking the minimum over these two choices of T.
28


## Page 29


Appendix D: Prediction Error Bounds
In this section we observe that the proofs of Theorems 1 and 2 also give rise to bounds on the prediction
error of our estimator. Starting from Equation (14) in the proof of Theorem 1,
1
2n∥˜X∆∥2
2 ≤λ1∥(˜Γβ∗)T c∥1 + 3λ1
4kT
p
|T|∥∆∥2.
(19)
The Restricted Eigenvalue condition in Lemma 8 gives that
∥∆∥2 ≤c
p
λmin(Σ + λSL) 1
√n∥X∆∥2.
Thus
1
2n∥˜X∆∥2
2 −
3cλ1
4kT
√n
p
|T|λmin(Σ + λSL)∥X∆∥2 −λ1∥(˜Γβ∗)T c∥1 ≤0.
(20)
As in the proof of Theorem 1, we can solve this quadratic inequality to conclude
Theorem 3 (Theorem 1 for Prediction Error). Suppose the conditions of Theorem 1 hold. Then with proba-
bility at least 1 −C1
p we have
1
n||X ˆβ −Xβ∗||2
2 ⪯min
T
max

λ2
1|T|
k2
T λmin(Σ + λSL), λ1||(˜Γβ∗)T c||1

This result holds for all choices of T. Choosing T to be supp(˜Γβ∗) and supp(β∗) as in the proof of
Theorem 2 gives an analogous result for prediction error.
Theorem 4 (Theorem 2 for Prediction Error). Suppose the conditions of Theorem 2 hold. Then with proba-
bility at least 1 −C1
p we have
1
n||X ˆβ −Xβ∗||2
2 ⪯
λ2
1||β∗||0
λmin(Σ + λSL) + min

2λ2
1λ2
TV ||ˆΣ||1,1||Γβ∗||0, 2λ!λTV ||Γβ∗||1

Appendix E: Proof of Lemma 1
First note that
λmin(Σ + λSL)
=
λmin((1 −λS)Σ + λS(Σ + L))
≥
(1 −λS)λmin(Σ) + λSλmin(Σ + L)
where the second inequality follows from Weyl’s inequality. For the remainder of the proof, we bound
λmin(Σ + L). Recall that
Σ + L = Σ −ˆΣ + D
(21)
where D ∈Rp×p is a diagonal matrix with
Djj =
p
X
k=1
|ˆΣj,k|, 1 ≤j ≤p.
29


## Page 30


Then
λmin(Σ + L) = λmin(Σ −ˆΣ + D) ≥λmin(Σ −ˆΣ) + λmin(D)
by Weyl’s inequality. Since
λmin(Σ −ˆΣ) = −λmax(ˆΣ −Σ) ≥−∥Σ −ˆΣ∥op ≥−∥Σ −ˆΣ∥1,1.
Hence
λmin(Σ + L)
≥
λmin(D) −∥Σ −ˆΣ∥1,1
≥
min
j
p
X
k=1
|ˆΣj,k| −cℓ
4 (by Assumption 2.3)
≥
min
j
" p
X
k=1
|Σj,k| −
p
X
k=1
|Σj,k −ˆΣj,k|
#
−cℓ
4
≥
min
j
p
X
k=1
|Σj,k| −max
j
p
X
k=1
|Σj,k −ˆΣj,k| −cℓ
4
≥
cℓ−cℓ
4 −cℓ
4 = cℓ
2 (by Assumptions 2.2 and 2.3).
Appendix F: Proof of Lemma 2
By the deﬁnition of kT we have
p
|T|k−1
T
= sup
β
∥(˜Γβ)T ∥1
∥β∥2
=
sup
β:∥β∥2=1
∥(˜Γβ)T ∥1
=
sup
β:∥β∥2=1
λTV∥(Γβ)T1∥1 + ∥βT2∥1
≤
sup
β:∥β∥2=1
λTV∥(Γβ)T1∥1 +
p
|T2|∥β∥2
≤
sup
β:∥β∥2=1
λTV∥(Γβ)T1∥1 +
p
|T2|.
Next we will bound the term ∥(Γβ)T1∥1. First note that
∥(Γβ)T1∥1 ≤
p
|T1|∥(Γβ)T1∥2
≤
q
|T1| P
(j,k)∈E T T1 |ˆΣj,k||βj −sign(ˆΣj,k)βk|2
≤
q
|T1| P
(j,k)∈E T T1 |ˆΣj,k|(2|βj|2 + 2|βk|2)
≤
r
|T1| Pp
j=1
P
k:(j,k)∈E T T1 2|ˆΣj,k|

|βj|2
≤
p
|T1|
r
max1≤j≤p
hP
k:(j,k)∈E T T1 2|ˆΣj,k|
iqPp
j=1 |βj|2
≤
p
|T1|
r
max1≤j≤p
hP
k:(j,k)∈E T T1 2|ˆΣj,k|
i
≤
p
|T1|
q
2∥ˆΣ∥1,1.
30


## Page 31


Thus
k−1
T
≤
λTV
q
2∥ˆΣ∥1,1|T1| +
p
|T2|
p
|T1| + |T2|
,
which completes the proof.
Appendix G: Proof of Lemma 3
Note that Γ is the edge incidence matrix and L = Γ⊤Γ is the weighted graph Laplacian matrix. Let the
singular value decomposition for Γ to be Γ = Um×pDp×pV ⊤
p×p. Next recall that ˜Γ =
λTVΓ
I

, then we have
˜Γ† =(λ2
TVΓ⊤Γ + I)−1 
λTVΓ⊤
I

=(λ2
TVV D2V ⊤+ I)−1 
λTVV DU⊤
I

=V (λ2
TVD2 + I)−1V ⊤
λTVV DU⊤
I

=
V (λ2
TVD2 + I)−1λTVDU⊤
|
{z
}
=:A
V (λ2
TVD2 + I)−1V ⊤
|
{z
}
=:B

.
From the deﬁnition of ρ we can see that the maximum diagonal entry of (˜Γ†)⊤˜Γ† will just be ρ2. Since
(˜Γ†)⊤˜Γ† =
A⊤A
A⊤B
B⊤A
B⊤B

,
we need to ﬁnd the maximum diagonal values for matrices A⊤A and B⊤B.
Suppose there are K connected components in the associated graph G. Thus the weighted graph Laplacian
matrix L is block diagonal, as is the matrix V (after appropriate permutation of rows and columns), with each
block corresponding to a different connected components. That is, each of the K connected components of
the graph has its own weighted graph Laplacian Lk = VkD2
kV ⊤
k , for k = 1, . . . , K and the diagonal blocks
of V are the Vks. Let µk be the minimum nonzero eigenvalue of Lk. Let Bk be the subset of vertices in
the k-th connected component and |Bk| be the number of vertices in that component, and let k(i) denote
which block contains vertex i. Now let v⊤
i be the ith row of V , u⊤
i be the ith row of U, and note that vi is
only supported on Bk(i). Further note that the ﬁrst (upper left) element of the k-th diagonal block of V is
1/
p
|Bk| if the minimum eigenvalue of Lk is 0. Then we have:
B⊤B =V (λ2
TVD2 + I)−2V ⊤,
31


## Page 32


and then the maximum diagonal element for B⊤B can be upper bounded as:
max diag(B⊤B) =
maxi∈{1,...,p} v⊤
i (λ2
TVD2 + I)−2vi
=
maxi∈{1,...,p}
Pp
j=1
v2
j,i
(λ2
TVD2
jj+1)2
=
maxi∈{1,...,p}
P
j∈Bk(i)
v2
j,i
(λ2
TVD2
jj+1)2
≤
maxi∈{1,...,p}



1
|Bk(i)| + P
j∈Bk(i):
D2
jj>0
v2
j,i
(λ2
TVD2
jj+1)2



(22)
≤
maxi∈{1,...,p}



1
|Bk(i)| +
1
(λ2
TVµk(i)+1)2
P
j∈Bk(i):
D2
jj>0
v2
j,i



≤
maxi∈{1,...,p}
n
1
|Bk(i)| +
1
(λ2
TVµk(i)+1)2
o
≤
maxk∈{1,...,K}
n
1
|Bk| +
1
(λ2
TVµk+1)2
o
.
On the other hand we note that
A⊤A =Uλ2
TVD2(λ2
TVD2 + I)−2U⊤,
similarly the maximum diagonal element for A⊤A can be upper bounded as:
max diag(A⊤A) =
maxi∈{1,...,m} u⊤
i λ2
TVD2(λ2
TVD2 + I)−2ui
=
maxi∈{1,...,m}
Pp
j=1
λ2
TVD2
jju2
j,i
(λ2
TVD2
jj+1)2
=
maxi∈{1,...,m}
Pp
j=1
(λ2
TVD2
jj+1−1)u2
j,i
(λ2
TVD2
jj+1)2
=
maxi∈{1,...,m}
Pp
j=1

u2
j,i
λ2
TVD2
jj+1 −
u2
j,i
(λ2
TVD2
jj+1)2

≤
maxi∈{1,...,m}
P
j∈{1,...,p}: D2
jj>0

u2
j,i
λ2
TVD2
jj+1

(23)
≤
maxi∈{1,...,m} maxj∈{1,...,p}: D2
jj>0
1
λ2
TVD2
jj+1
Pp
j=1 u2
j,i
≤
maxi∈{1,...,m} maxj∈{1,...,p}: D2
jj>0
1
λ2
TVD2
jj+1
≤
maxk∈{1,...,K}
1
λ2
TVµk+1.
Then by combining the results above we have
ρ2
≤
max
1≤k≤K
 1
|Bk| +
1
(λ2
TVµk + 1)2 +
1
λ2
TVµk + 1

≤
max
1≤k≤K
 1
|Bk| +
2
λ2
TVµk + 1

.
This completes the proof of Lemma 3.
32


## Page 33


Appendix H: Proof of Lemma 4
By the deﬁnition of the block complete graph in Section 2.2.1 we can see that |Bk| = p
K for 1 ≤k ≤K thus
we have max1≤k≤K
1
|Bk| = K
p . Note that µk is deﬁned to be the smallest non-zero eigenvalue of weighted
graph Laplacian matrix for the kth complete graph. It is known that the smallest non-zero eigenvalue for
un-weighted Laplacian matrix for complete graph is the number of nodes (see H¨utter and Rigollet (2016,
Section 4.1)). Thus, applying appropriate normalization µk = ar|Bk| = ar p
K = r since a = K
p . Hence
µk = r for 1 ≤k ≤K. Also note that λmin(Σ) = a(1 −r), so we have
λmin(Σ + λSL)
=
λmin[(1 −λS)Σ + λS(Σ + L)]
≥
(1 −λS)λmin(Σ) + λSλmin(Σ + L)
=
(1 −λS)a(1 −r) + λS[a + ar( p
K −1)] (by ((21)) and ˆΣ = Σ)
≥
(1 −λS)(1 −r)K
p + λSr (by using a = K
p ).
This completes the proof of Lemma 4.
Appendix I: Proof of Lemma 5
Let Γ be the edge incidence matrix for the chain graph and let Γ = UDV T denote the SVD of Γ. Note that
the chain graph has one connected component, so in the language of Lemma 3 we have |B1| = p. From
Equations (23) and (24) in the proof of Lemma 3 it follows that
ρ2 ≤max


max
i∈{1,...,p}
1
p +
X
j:D2
j,j>0
v2
j,i
(λ2
TV D2
j,j + 1)2 ,
max
i∈{1,...,p−1}
X
j:D2
j,j>0
u2
j,i
λ2
TV D2
j,j + 1


.
First note that if λTV = 0 then ρ2 ≤1
p + 1 and our bound is satisﬁed, so for the remainder of the proof we
assume λTV > 0.
Right singular vectors: We ﬁrst bound
1
p +
X
j:D2
j,j>0
v2
j,i
(λ2
TV D2
j,j + 1)2 .
(24)
The right singular vectors corresponding to the nonzero singular values are the normalized eigenvectors of
the Laplacian matrix which (see H¨utter and Rigollet (2016, Section B.2)) are of the form
vj,i =
r2
p cos
(i + 1/2)jπ
p

so in particular, v2
j,i ≤2
p for all i, j. Thus Equation (24) is
≤1
p + 2
p
X
j:D2
j,j>0
1
(λ2
TV D2
j,j + 1)2 .
33


## Page 34


The
D2
j,j
r2 are the nonzero eigenvalues of the unweighted Laplacian matrix for the path graph which are also
given in H¨utter and Rigollet (2016, Section B.2) as σj = 2 −2 cos( jπ
p ) for j = 1, . . . , p −1. We have
2 −2 cos( jπ
p ) ≥j2
p2 for 1 ≤k ≤p −1 so this is
≤
1
p + 2
p
p−1
X
j=1
1
(r2λ2
T V j2
p2
+ 1)2
=
1
p + 2p3
p−1
X
j=1
1
(r2λ2
TV j2 + p2)2
=
1
p +
2p3
r4λ4
TV
p−1
X
j=1
1
(j2 + (
p
rλT V )2)2 .
Because f(j) =
1
(j2+(
p
rλT V )2)2 is monotonically decreasing on R+ we get that this is
≤
1
p +
2p3
r4λ4
TV
Z ∞
x=0
1
(x2 + (
p
rλT V )2)2 dx
=
1
p +
2p3
r4λ4
TV
π
4(
p
rλT V )3 = 1
p +
π
2rλTV
.
(25)
Left singular vectors We next focus on bounding
X
j:D2
j,j>0
u2
j,i
λ2
TV D2
j,j + 1.
(26)
The uj are the normalized eigenvectors of ΓΓT . A computation shows that
ΓΓT
i,j =





2 if i = j
−1 if |i −j| = 1
0 otherwise
Strang (2007, Section 1.5), gives p −1 orthonormal eigenvectors uj of ΓΓT which are of the form uj,i =
q
2
p sin(πij
p )). In particular u2
j,i ≤2
p so Equation (26) is
≤2
p
X
j:D2
j,j>0
1
λ2
TV D2
j,j + 1.
(27)
As before, we have that the
D2
j,j
r2 are the nonzero eigenvalues of the unweighted Laplacian of the path graph,
so they are of the form 2 −2 cos( πj
p ) for j = 1, . . . p −1 and since 2 −2 cos( πj
p ) ≥j2
p2 for j = 1, . . . , p −1
34


## Page 35


we get that this is
≤
2
p
p−1
X
j=1
1
r2λ2
T V j2
p2
+ 1
=
2p
p−1
X
j=1
1
p2 + r2λ2
TV j2
=
2p
r2λ2
TV
p−1
X
j=1
1
j2 + (
p
rλT V )2 .
Since f(j) =
1
j2+(
p
rλT V )2 is montonically decreasing on R+ we have that this is
≤
2p
r2λ2
TV
Z ∞
x=0
1
x2 + (
p
rλT V )2 dx
=
2p
r2λ2
TV
rλTV
p
arctan
rλTV x
p
 
x=∞
x=0 =
π
rλTV
.
(28)
Moreover, since u2
i,j and v2
i,j are bounded by 2
p we immediately have the bound
ρ2 ≤1
p + 2.
Combining this with Equations (25) and (28) we conclude that
ρ2 ≤min
1
p + 2, max(
π
rλTV
, 1
p +
π
2rλTV
)

≤1
p +
2π
rλTV + 1
as claimed.
For the ﬁnal part of the proof, note that λmin(Σ) = a[1 + 2rcos(
p
p+1π)] (see Noschese et al. (2013,
Section 2)), so we have
λmin(Σ + λSL)
=
λmin[(1 −λS)Σ + λS(Σ + L)]
≥
(1 −λS)λmin(Σ) + λSλmin(Σ + L)
=
(1 −λS)a[1 + 2r cos(
p
p + 1π)] + λSa(1 + r) (by (21) and ˆΣ = Σ)
≥
(1 −λS)[1 + 2r cos(
p
p + 1π)] + λS (by using a = 1)
≥
(1 −λS)(1 −2r) + λS.
This completes the proof of Lemma 5.
Appendix J: Proof of Lemma 6
Note that the lattice graph has one connected component, so in the language of Lemma 3 we have |B1| = p.
Then from Equations (23) and (24) in the proof of Lemma 3 it follows that
ρ2 ≤max


max
i∈{1,...,p}
1
p +
X
j:D2
j,j>0
v2
j,i
(λ2
TV D2
j,j + 1)2 ,
max
i∈{1,...,p−1}
X
j:D2
j,j>0
u2
j,i
λ2
TV D2
j,j + 1


.
35


## Page 36


First note that if λTV = 0 then ρ2 ≤1
p + 1 and our bound is satisﬁed, so for the remainder of the proof we
assume λTV > 0.
Right singular vectors We ﬁrst bound
1
p +
X
j:D2
j,j>0
v2
j,i
(λ2
TV D2
j,j + 1)2 .
(29)
The vj correspond to the normalized eigenvectors of the unweighted Laplacian for the Lattice graph. We
denote the Laplacian LLat. Let L√p denote the unweighted Laplacian for the path graph with √p nodes.
Since the Lattice graph is the direct product of two copies of the path graph, we have
LLat = L√p ⊗I√p + I√p ⊗L√p.
Let {(wk}j=1,...,√p denote the normalized eigenvectors of L√p and σk the corresponding eigenvalues. Then
LLat(wk ⊗wl)
=
L√pwk ⊗I√pwl + I√pwk ⊗L√pwl
=
σkwk ⊗wl + wk ⊗σlwl = (σk + σl)(wk ⊗wl).
The tensor product of unit vectors is also a unit vector, so ∥wk ⊗wl∥2 = 1 and {wk ⊗wl}k,l=1,...,√p}
are the normalized eigenvectors vj of LLat. The wk were given in the proof of the path graph case as
wk,m =
q
2
√p cos

(m+1/2)kπ
√p

so in particular we have v2
j,i ≤4
p. Therefore Equation (29) is
≤1
p + 4
p
X
j:D2
j,j>0
1
(λ2
TV D2
j,j + 1)2 .
We have
D2
j,j
r2
= λj where λj denotes the jth eigenvalue of LLat. We concluded above that the eigenvalues
of LLat are of the form σk + σl where {σk}k=0,...,√p−1} are the eigenvalues of L√p. From the path graph
proof, we know these are of the form
σk + σl = 4 −2 cos( πk
√p) −2 cos( πl
√p) ≥k2 + l2
p
for k, l = 0, . . . , √p −1. Thus
1
p + 4
p
X
j:D2
j,j>0
1
(λ2
TV D2
j,j + 1)2 ≤1
p + 4
p
√p
X
k=0
√p
X
l=0
1(k,l)̸=(0,0)
(r2λ2
TV
k2+l2
p
+ 1)2 .
Algebraic rearrangement gives that this is
=
1
p + 4p
√p
X
k=1
√p
X
l=1
1
(r2λ2
TV (k2 + l2) + p)2 + 8p
√p
X
k=1
1
(r2λ2
TV k2 + p)2
=
1
p +
4p
r4λ4
TV
√p
X
k=1
√p
X
l=1
1
(k2 + l2 +
p
r2λ2
T V )2 +
8p
r4λ4
TV
√p
X
k=1
1
(k2 +
p
r2λ2
T V )2 .
36


## Page 37


The above functions are monotonically decreasing in k and l for k, l ≥0 and so we can say this is
≤
1
p +
4p
r4λ4
TV
Z ∞
x=0
Z ∞
y=0
1
(x2 + y2 +
p
r2λ2
T V )2 dydx +
8p
r4λ4
TV
Z ∞
x=0
1
(x2 +
p
r2λ2
T V )2 dx
=
1
p +
4p
r4λ4
TV
πr2λ2
TV
4p
+
8p
r4λ4
TV
πr3λ3
TV
4p3/2
= 1
p +
4π
r2λ2
TV
+
8π
rλTV √p.
(30)
Left singular vectors We next focus on bounding
X
j:D2
j,j>0
u2
j,i
λ2
TV D2
j,j + 1.
(31)
The uj are the normalized eigenvectors of ΓΓT . The eigenvectors of this matrix are nontrivial to derive, but
Wang et al. (2016) ﬁnds them in their proof of Corollary 8. Moreover, they show that after normalizing the
eigenvectors, each entry is bounded by
q
4
p. In particular, we have u2
j,i ≤4
p for all i, j and so Equation (31)
is
≤4
p
X
j:D2
j,j>0
1
λ2
TV D2
j,j + 1.
As in the right singular vector case, the
D2
j,j
r2 are the eigenvalues of the unweighted Laplacian for the lattice
graph, so they are of the form
σk + σl = 4 −2 cos( πk
√p) −2 cos( πl
√p) ≥k2 + l2
p
for k, l = 0, . . . , √p −1. Thus
4
p
X
j:D2
j,j>0
1
λ2
TV D2
j,j + 1 ≤4
p
√p
X
k=0
√p
X
l=0
1(k,l)̸=(0,0)
r2λ2
TV
k2+l2
p
+ 1
.
Algebraic manipulation gives that this is
=
4
√p
X
k=1
√p
X
l=1
1
r2λ2
TV (k2 + l2) + p + 8
√p
X
k=1
1
r2λ2
TV k2 + p
=
4
r2λ2
TV
√p
X
k=1
√p
X
l=1
1
k2 + l2 +
p
r2λ2
T V
+
8
r2λ2
TV
√p
X
k=1
1
k2 +
p
r2λ2
T V
.
And now we use an integral comparison as before to conclude that this is
≤
4
r2λ2
TV
Z √p
x=0
Z ∞
y=0
1
x2 + y2 +
p
r2λ2
T V
dydx +
8
r2λ2
TV
Z ∞
x=0
1
x2 +
p
r2λ2
T V
dx
=
2π
r2λ2
TV
Z √p
x=0
1
q
x2 +
p
r2λ2
T V
dx +
8
r2λ2
TV
πrλTV
2√p .
(32)
37


## Page 38


We compute this last integral explicitly as
Z √p
x=0
1
q
x2 +
p
r2λ2
T V
dx
=
π
2 log(
r
p
r2λ2
TV
+ x2 + x)

x=√p
x=0
=
π
2 log


q
p
r2λ2
T V + p + √p
q
p
r2λ2
T V

.
Some additional algebra, along with the fact that
√
a + b ≤√a +
√
b for a, b ≥0 gives that this is
≤π
2 log(2 + rλTV ).
Overall we’ve concluded that Equation (32) is
≤π2 log(2 + rλTV )
r2λ2
TV
+
8π
rλTV √p.
(33)
Moreover, since u2
i,j and v2
i,j are bounded by 4
p we immediately have the bound
ρ2 ≤5.
Combining this with Equations (30) and (33) we conclude that
ρ2 ≤min

5, 1
p + 4π log(2 + rλTV )
r2λ2
TV
+
8π
rλTV √p

≤1
p + 5π log(2 + rλTV )
r2λ2
TV + 1
+
10π
rλTV √p + 1
as claimed.
For the ﬁnal part of the proof recall that r ∈(0, 1
4). Thus Σ is diagonally dominant with Σi,i−P
j̸=i Σi,j ≥
1 −4r > 0 for all i and therefore λmin(Σ) ≥1 −4r. This implies that
λmin(Σ + λSL)
=
λmin[(1 −λS)Σ + λS(Σ + L)]
≥
(1 −λS)λmin(Σ) + λSλmin(Σ + L)
=
(1 −λS)(1 −4r) + λS(1 + 2r) (by (21) and ˆΣ = Σ)
≥
(1 −λS)(1 −4r) + λS.
This completes the proof of Lemma 6.
Appendix K: Extension to Logistic Regression
In the main body of the paper we consider only a linear model in the interest of simplicity. However, it
is straightforward to extend the theory in this paper to generalized linear models. In this section we need
to assume that ||β∗||1 ≤u for a universal constant u. We will informally sketch an extension to logistic
regression. Consider a logistic model where
yi ∼Bernoulli(λi)
λi =
1
1 + exp(−⟨β∗, Xi⟩).
38


## Page 39


Instead of using squared loss, we want to use the logistic loss function
L(β; X, y) =
n
X
i=1
log(1 + exp(⟨β∗, Xi⟩)) −yi⟨β∗, Xi⟩.
The GTV estimator for the logistic model takes the form
ˆβ = arg min
β:||β||1≤u
1
nL(β) + λS
X
j,k
|ˆΣj,k|(βj −ˆsj,kβk)2
+ λ1(λTV
X
j,k
|ˆΣj,k|1/2|βj −ˆsj,kβk| + ∥β∥1).
(34)
For convenience deﬁne
R(β) := λS
X
j,k
|ˆΣj,k|(βj −ˆsj,kβk)2 + λ1(λTV
X
j,k
|ˆΣj,k|1/2|βj −ˆsj,kβk| + ∥β∥1).
To derive similar theoretical bounds in this setting, ﬁrst note that by deﬁnition
1
nL(ˆβ) ≤1
nL(β∗) + (R(β∗) −R(ˆβ)).
We now use standard steps for the analysis of generalized models in order to reduce our problem to the
linear setting in the proof of Theorem 1. For the remainder of the section, we use the shorthand f(x) =
log(1 + exp(x)). Using the deﬁnition of L(β) and rearranging terms yields
n
X
i=1
1
nf(⟨ˆβ, Xi⟩) −f(⟨β∗, Xi⟩) −yi⟨△, Xi⟩≤R(β∗) −R(ˆβ).
Deﬁne ϵi := yi −E[yi|Xi] = yi −f′(⟨β∗, Xi⟩) and then
1
nf(⟨ˆβ, Xi⟩) −f(⟨β∗, Xi⟩) −f′(⟨β∗, Xi⟩)⟨△, Xi⟩≤1
n
n
X
i=1
ϵi⟨△, Xi⟩+ R(β∗) −R(ˆβ).
(35)
For x, y contained in an interval [−d, d], f is a strongly convex function so that
f(x) −f(y) −f′(y)(x −y) ≥ψ∥x −y∥2
2
for a strong convexity parameter ψ which depends on d. Applying this to Equation (35),
ψ
n ⟨△, Xi⟩2 ≤1
n
n
X
i=1
ϵi⟨△, Xi⟩+ R(β∗) −R(ˆβ).
(36)
Assuming ||β∗||1, ||ˆβ||1 ≤u for a universal constant u, the convexity parameter ψ is also bounded by a
universal constant. Rearranging terms and ignoring the factor of ψ, the inequality in Equation (36) is exactly
the inequality at the beginning of the proof of Theorem 1. Thus all the bounds derived in the linear setting
also apply in the logistic regression setting up to a factor of the convexity parameter ψ.
39


## Page 40


Appendix L: Proof of Lemma 7
We will use two classical Lemmas for Gaussian processes Anderson (1984); Slepian (1962) to prove our
results.
Lemma 9 (Anderson’s comparison inequality). Let X and Y be zero-mean Gaussian random vectors with
covariance ΣX and ΣY respectively. If ΣY −ΣX is positive semi-deﬁnite then for any convex symmetric set
C,
P(X ∈C) ≤P(Y ∈C).
Lemma 10 (Slepian’s Lemma). Let {Gs, s ∈S} and {Hs, s ∈S} be two centered Gaussian processes
deﬁned over the same index set S. Suppose that both processes are almost surely bounded. For each s, t ∈S,
if E(Gs −Gt)2 ≤E(Hs −Ht)2, then E[sups∈S Gs] ≤E[sups∈S Hs]. Further if E(G2
s) = E(H2
s ) for all
s ∈S, then
P{sup
s∈S
Gs > x} ≤P{sup
s∈S
Hs > x},
for all x > 0.
(X˜Γ†)⊤ϵ = Pn
i=1⟨˜Γ†, ϵiX(i)⟩and Cov(X) = Σ ⪯λmax(Σ)Ip×p. Then by Assumption 2.1 λmax(Σ) ≤
cu, and if we use Lemma 9, for any x > 0
P{sup
n
X
i=1
⟨˜Γ†, ϵiX(i)⟩≤x} ≥P{sup √cu
n
X
i=1
⟨˜Γ†, ϵigi⟩≤x},
where X(i) is the ith row of matrix X and {gi : i = 1, ..., n} is i.i.d. standard normal Gaussian vectors with
gi ∈Rp. Now let G ∈Rp be an i.i.d. standard norm Gaussian vector and deﬁne the zero-mean Gaussian
process √nσ⟨˜Γ†, G⟩, we can see that the conditions in Lemma 10 are satisﬁed for two centered Gaussian
processes Pn
i=1⟨˜Γ†, ϵigi⟩and √nσ⟨˜Γ†, G⟩thus we have
P{sup √cu
n
X
i=1
⟨˜Γ†, ϵigi⟩≤x} ≥P{sup σ√ncu⟨˜Γ†, G⟩≤x}.
Further, using known results on Gaussian maxima (Boucheron et al. (2013, Theorem 2.5)), sup⟨˜Γ†, G⟩≤
3ρ
p
log(m + p) with probability at least 1 −C1
p for some absolute constant C1 > 0. By choosing x =
3σρ
p
ncu log(m + p),
P{sup
n
X
i=1
⟨˜Γ†, ϵiX(i)⟩≤x} ≥P{sup σ√ncu⟨˜Γ†, G⟩≤x} ≥1 −C1
p .
Thus we have shown with high probability that ∥(X˜Γ†)⊤ϵ∥∞≤3σρ
p
ncu log(m + p). Since m is the num-
ber of edges, m ≤p(p−1)
2
, thus with probability at least 1−C1
p we have that ∥(X˜Γ†)⊤ϵ∥∞≤6σρ√ncu log p.
This completes the proof.
40


## Page 41


Appendix M: Proof of Lemma 8
The proof of Lemma 8 involves two parts.
Part 1: We ﬁrst show that the following inequality
∥X∆∥2
√n
≥1
4∥Σ1/2∆∥2 −9λ1
σ ∥˜Γ∆∥1
(37)
holds with probability at least 1−c4 exp(−c5n) by using similar techniques to those used to prove Theorem
1 in Raskutti et al. (2010).
First note that it is sufﬁcient to show (37) holds with ∥Σ1/2∆∥2 = 1. The reason is as follows: if
∥Σ1/2∆∥2 = 0 we can see that (37) holds trivially; otherwise when ∥Σ1/2∆∥2 > 0 we can deﬁne ˜∆=
∆
∥Σ1/2∆∥2 then we have ∥Σ1/2 ˜∆∥2 = 1. Since (37) is invariant with respect to the scale of ∆, if it holds for
˜∆, it also holds for ∆. Thus in the following proof we just assume that ∥Σ1/2∆∥2 = 1. To show (37) with
∥Σ1/2∆∥2 = 1 holds there are three main steps:
(1) Since we want to lower bound ∥X∆∥2
√n
in terms of ∥Σ1/2∆∥2 and ∥˜Γ∆∥1, we deﬁne the set V (r) :=
{∆∈Rp | ∥Σ1/2∆∥2 = 1, ∥˜Γ∆∥1 ≤r} for a ﬁxed radius r. Note that we are only concerned with choices
of r such the set V (r) is non-empty. Our ﬁrst step is to give an upper bound for E[M(r, X)], where M(r, X)
is deﬁned as:
M(r, X) := 1 −
inf
∆∈V (r)
∥X∆∥2
√n
=
sup
∆∈V (r)

1 −∥X∆∥2
√n

.
(2) The second step is to use concentration inequalities to show that with high probability for each ﬁxed
r > 0, the random quantity M(r, X) is sharply concentrated around E[M(r, X)].
(3) The third step is to use a peeling argument to show that the analysis holds uniformly over all possible
values of r with high probability, then we can show that (37) holds with high probability.
In the following proof we only provide details for proving step (1) since our proof for step (2) and (3)
will be identical to those in Raskutti et al. (2010). For step (1) we prove the following lemma:
Lemma 11. For any radius r > 0 such that V (r) is non-empty, we have
E[M(r, X)] ≤1
4 + 3rλ1
σ .
Proof. Deﬁne the Euclidean sphere of radius 1 to be Sn−1 = {u ∈Rn | ∥u∥2 = 1}. Then ∥X∆∥2 =
supu∈Sn−1 u⊤X∆. In order to write the quantity M(r, X) in a form that is easier to analyze, we deﬁne
Yu,∆:= u⊤X∆for each pair (u, ∆) ∈Sn−1 × V (r). Then we have
−
inf
∆∈V (r) ∥X∆∥2 = −
inf
∆∈V (r)
sup
u∈Sn−1 u⊤X∆=
sup
∆∈V (r)
inf
u∈Sn−1 Yu,∆.
Next we will use a Gaussian comparison inequality to upper bound the expected value of the quantity
sup∆∈V (r) infu∈Sn−1 Yu,∆. Here we use a form of Gordon’s inequality that is stated in Davidson and Szarek
(2001) for our analysis. Suppose that {Yu,∆, (u, ∆) ∈U × V } and {Zu,∆, (u, ∆) ∈U × V } are two zero-
mean Gaussian processes on U ×V . We denote σ(·) to be the standard deviation of a random variable. Using
Gordon’e inequality, if
σ(Yu,∆−Yu′,∆′) ≤σ(Zu,∆−Zu′,∆′), ∀(u, ∆) and (u′, ∆′) ∈U × V,
41


## Page 42


and this inequality holds with equality when ∆= ∆′, then
E[sup
∆∈V
inf
u∈U Yu,∆] ≤E[sup
∆∈V
inf
u∈U Zu,∆].
Now we consider the zero-mean Gaussian process Zu,∆with (u, ∆) ∈Sn−1 × V (r) as follows:
Zu,∆= g⊤u + h⊤Σ1/2∆,
where g ∼N(0, In×n) and h ∼N(0, Ip×p). It follows that (see Raskutti et al. (2010) for more details)
σ(Yu,∆−Yu′,∆′) ≤σ(Zu,∆−Zu′,∆′), ∀(u, ∆) and (u′, ∆′) ∈Sn−1 × V (r),
and the equality holds when ∆= ∆′. Thus we can apply Gordon’s inequality to conclude that
E[ sup
∆∈V (r)
inf
u∈Sn−1 Yu,∆]
≤
E[ sup
∆∈V (r)
inf
u∈Sn−1 Zu,∆]
=
E[ inf
u∈Sn−1 g⊤u] + E[ sup
∆∈V (r)
h⊤Σ1/2∆]
=
−E[∥g∥2] + E[ sup
∆∈V (r)
h⊤Σ1/2∆].
Next we bound the term E[sup∆∈V (r) h⊤Σ1/2∆] using the following lemma:
Lemma 12. Suppose we have λ1 ≥48ρσ
q
cu log p
n
, then we have that
λ1 ≥8 σ
√nE[∥(Σ1/2˜Γ†)⊤h∥∞].
with probability at least 1 −c
p for some absolute constant c > 0.
The proof for this lemma will be provided shortly. Thus
E[ sup
∆∈V (r)
|h⊤Σ1/2∆|]
=
E[ sup
∆∈V (r)
|h⊤Σ1/2˜Γ†˜Γ∆|]
≤
E[ sup
∆∈V (r)
∥h⊤Σ1/2˜Γ†∥∞∥˜Γ∆∥1]
≤
E[∥(Σ1/2˜Γ†)⊤h∥∞]r
≤
3rλ1
σ
√n,
where the last inequality holds with high probability from Lemma 12. Also by standard χ2 tail bounds
(Ledoux and Talagrand, 1991) when n ≥10 we have E[∥g∥2] ≥3
4
√n. By combining hese pieces together
E[−
inf
∆∈V (r) ∥X∆∥2] ≤−3
4
√n + 3rλ1
σ
√n.
Thus by dividing by √n and adding 1 to both sides we have
E[M(r, X)] = E[1 −
inf
∆∈V (r)
∥X∆∥2
√n
] ≤1
4 + 3rλ1
σ .
42


## Page 43


Then by following the rest proof in Raskutti et al. (2010) for step (2) and (3), we can show that with
probability at least 1 −c4 exp(−c5n),
∥X∆∥2
√n
≥1
4∥Σ1/2∆∥2 −9λ1
σ ∥˜Γ∆∥1.
Part 2: Next we can go to second part of the proof. From (12) and (13) we know that
∥˜Γ∆∥1
≤
4∥(˜Γ∆)T ∥1 + 4∥(˜Γβ∗)T c∥1
≤
4
p
|T|∥∆∥2
kT
+ 4∥(˜Γβ∗)T c∥1.
Then
∥X∆∥2
√n
≥1
4∥Σ1/2∆∥2 −9λ1
σ
 
4∥(˜Γβ∗)T c∥1 + 4
p
|T|∥∆∥2
kT
!
.
Thus there exist constants c′, c′′ > 0 such that
∆⊤
X⊤X
n
+ λSL

∆≥c′∆⊤(Σ + λSL)∆−c′′λ2
1

∥(˜Γβ∗)T c∥2
1 + |T|∥∆∥2
2
k2
T

.
Since
∆⊤(Σ + λSL)∆
≥
λmin(Σ + λSL)∥∆∥2
2,
then when λ1 satisﬁes (15) for some constant c2 > 0,
∆⊤(X⊤X
n
+ λSL)∆≥c1λmin(Σ + λSL)∥∆∥2
2 −c3λ2
1∥(˜Γβ∗)T c∥2
1,
for absolute constants c1, c3 > 0.
Appendix N: Proof of Lemma 12
Here we use similar techniques to the proof of Lemma 7. First note that Σ ⪯cuIp×p and by using Lemma 9
we have for any y > 0 the following inequality
P{sup[(Σ1/2˜Γ†)⊤h] ≤y} = P{sup⟨˜Γ†, Σ1/2h⟩≤y} ≥P{sup⟨˜Γ†, h⟩≤
y
√cu
}.
Since h ∼N(0, Ip×p) then also by known results on Gaussian maxima (Boucheron et al. (2013, Theorem
2.5)) we have sup⟨˜Γ†, h⟩≤3ρ
p
log(m + p) with probability at least 1 −c
p for some constant c > 0. Then
we can choose y = 3ρ
p
cu log(m + p) and
P{sup[(Σ1/2˜Γ†)⊤h] ≤y} ≥P{sup⟨˜Γ†, h⟩≤
y
√cu
} ≥1 −c
p.
Thus with high probability ∥(Σ1/2˜Γ†)⊤h∥∞≤3ρ
p
cu log(m + p), then using the fact that m ≤p(p−1)
2
,
∥(Σ1/2˜Γ†)⊤h∥∞≤6ρ√cu log p holds with probability at least 1 −c
p. This completes the proof of Lemma
12.
43


## Page 44


Appendix O: Simulation Details
The graphs and corresponding covariance structures are constructed as follows:
Block Complete Graph
Σ is block diagonal with K blocks, each of size p
K × p
K . Following the discussion
in Section 2.2.1, all the diagonal elements are set to K
p and all the off-diagonal elements in each block are
set to Kr
p
with r ∈(0, 1). Here r is the correlation coefﬁcient and will be set to different values in the
experiments. Speciﬁcally, let
B = K
p

r1p/K1⊤
p/K + (1 −r)Ip/K

and
Σ = IK ⊗B,
where ⊗denotes the Kronecker product. To set the true coefﬁcient vector β∗, we ﬁrst randomly choose ℓof
the K blocks to be “active blocks”. Then we set the elements in β∗that correspond to the ℓactive blocks to
be β∗
j ∼N(1, 0.012) when i belongs to these ℓactive blocks and all other elements in β∗to be 0 (inactive).
That is, let S ∈{0, 1}p indicate the indices in active blocks (and hence the support of β∗); then
β∗∼N(S, 0.012diag(S)).
Chain Graph:
Following the discussion in Section 2.2.2, we set elements in the main diagonal of Σ to be
one, the ﬁrst off-diagonal elements to be r with r ∈(0, 1
2), and all the other elements to be zero; i.e.,
Σj,k =





1,
if j = k,
r,
if |j −k| = 1,
0,
else.
The corresponding true coefﬁcient vector β∗is set to have β∗
j ∼N(1, 0.012) for 1 ≤j ≤s and the
remaining elements to be zero. That is, let S ∈{0, 1}p have its ﬁrst s < p elements be one and the
remaining be zero; then
β∗∼N(S, 0.012diag(S)).
Lattice Graph
Following the discussion in Section 2.2.3, we construct Σ as follows.
Σj,k =











1,
if j = k,
r,
if |j −k| = 1 and min(j, k) ̸= 0 mod √p,
r,
if |j −k| = √p
0,
else.
The corresponding true coefﬁcient vector β∗with s active elements is set to β∗
j ∼N(1, 0.012) if j ≤
√s mod √p and j ≤√ps and is set to β∗
j = 0 otherwise. This corresponds to an active √s × √s sublattice
within the √p × √p lattice. The remaining elements outside of this sublattice are set to zero.
44


## Page 45


Appendix P: Biochemistry Table
Structure Feature
Description
buried np AFILMVWY per res
Buried
nonpolar
surface
area
on
nonpolar
amino
acids/count buried and core residues.
buried np per res
Buried nonpolar surface area of the protein divided by
count buried non polar residues.
buried over exposed
buried np per res divided by solvent available surface area
(sasa) of hydrophobic residues.
buried over exposed AFILMVWY
buried np AFILMVWY per res divided by sasa of hy-
drophobic residues.
cbeta
A solvation term intended to correct for the excluded vol-
ume effect introduced by the simulation and favor com-
pact structures. It is based on the ratio of probabilities of a
residue having a given number of neighbors in a compact
structure vs. random coil and summed over all residues.
cenpack
A centroid energy term.
contact all per res
Count
sidechain
carbon-carbon
contacts
among
all
residues under the given distance cutoff divided by count
residues of the sequence modeled.
contact buried core boundary per res
Count sidechain carbon-carbon contacts among the buried
and boundary residues under the given distance cutoff di-
vided by count buried and boundary residues.
contact buried core per res
Count sidechain carbon-carbon contacts among the buried
residues under the given distance cutoff divided by count
buried residues.
degree core boundary per res
Count number of residues within a set distance of buried
and boundary residues divided by count buried and bound-
ary residues.
degree core per res
Count number of residues within a set distance of buried
residues divided by count buried residues.
degree per res
Count number of residues within a set distance of other
residues divided by count residues of the sequence mod-
eled.
env
A context-dependent one-body energy term that describes
the solvation of a particular residue (based on the hy-
drophobic effect). It is based on the probability of a residue
having the speciﬁed type given its number of neighboring
residues.
exposed hydrophobics per res
Sasa of hydrophobic residues divided by count residues of
the sequence modeled.
exposed polars per res
Sasa of polar residues divided by count residues of the se-
quence modeled.
exposed total per res
Sasa of whole protein divided by count residues of the se-
quence modeled.
45


## Page 46


Structure Feature
Description
fa atr
Lennard-Jones attractive.
fa dun
Internal energy of sidechain rotamers as derived from Dun-
brack’s statistics.
fa elec
Coulombic
electrostatic
potential
with
a
distance-
dependent dielectric. Supports canonical and noncanonical
residue types.
fa intra rep
Lennard-Jones repulsive between atoms in the same
residue.
fa intra sol xover4
Intra-residue LK solvation, counted for the atom-pairs
beyond torsion-relationship. Supports arbitrary residues
types.
fa rep
Lennard-Jones repulsive.
fa sol
Lazaridis-Karplus solvation energy.
hbond bb sc
Sidechain-backbone hydrogen bond energy.
hbond lr bb
Backbone-backbone hbonds distant in primary sequence.
hbond sc
Sidechain-sidechain and sidechain-backbone hydrogen
bond energy.
hbond sr bb
Backbone-backbone hbonds close in primary sequence.
hs pair
Describes packing between strands and helices. It is based
on the probability that two pairs of residues (1 pair in the
sheet and 1 pair in the helix) will have their current dihe-
dral angles given the separation (in sequence and physical
distance) between the helix and the strand.
lk ball wtd
Weighted sum of lk ball & lk ball iso (w1*lk ball +
w2*lk ball iso); w2 is negative so that anisotropic contri-
bution(lk ball) replaces some portion of isotropic contribu-
tion (fa sol=lk ball iso). Supports arbitrary residue types.
n charged
Number of charged residues.
netcharge
The total charge.
omega
Omega angles.
one core each
The fraction of secondary structure elements (helices and
strands) with one large hydrophobic residue (FILMVYW)
at a position in the core layer of the protein.
p aa pp
Probability of observing an amino acid, given its phi/psi
energy method declaration.
pack
Packing statistics. Calculated on whole protein.
pair
A two-body energy term for residue pair interactions (elec-
trostatics and disulﬁde bonds). For each pair of residues, it
is based on the probability that both of these two residues
will have their speciﬁed types given their sequence sepa-
ration and the physical distance between them, normalized
by the product of the probabilities that each residue will
have its speciﬁed type given the same information.
polar over hydrophobic
exposed polars per res
divided
by
ex-
posed hydrophobics per res.
46


## Page 47


Structure Feature
Description
pro close
Proline ring closure energy.
rama prepro
Backbone torsion preference term that takes into account
of whether preceding amono acid is Proline or not. Cur-
rently supports the 20 canonical alpha-amino acids, their
mirror-image D-amino acids, oligoureas, and N-methyl
amino acids. Arbitrary new building-blocks can also be
supported provided that an N-dimensional mainchain po-
tential can be generated somehow.
ref
Reference energy for each amino acid.
rg
Favors compact structures and is calculated as the root
mean square distance between residue centroids.
rsigma
Scores strand pairs based on the distance between them and
the register of the two strands.
sheet
Favors the arrangement of individual beta strands into
sheets. It is derived from the probability that a structure
with a given number of beta strands will have the current
number of beta sheets and lone beta strands.
ss contributes core
The fraction of secondary structure elements (helices and
strands) with one large hydrophobic residue (FILMVYW)
at a position in either the core or interface layer of the pro-
tein.
ss mis
Generate secondary structure predictions from sequence.
Calculated on whole protein.
ss pair
Describes hydrogen bonding between beta strands.
total score per res
The sum of all features, averaged by residue number.
two core each
The fraction of secondary structure elements (helices and
strands) with two large hydrophobic residues (FILMVYW)
at positions in the core layer of the protein.
vdw
Represents only steric repulsion and not attractive van der
Waals forces (those are modeled in terms rewarding com-
pact structures, such as the rg term; local interactions are
implicitly included from fragments). It is calculated over
pairs of atoms only in cases where: 1. the interatomic dis-
tance is less than the sum of the atoms’ van der Waals radii,
and 2. the interatomic distance does not depend on the tor-
sion angles of a single residue.
yhh planarity
Helps control the alcohol hydrogen in tyrosine.
Table 2: Description of structural features used in the biochemistry data analysis.
47

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]