---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1810.03068v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1810.03068v2_Geometric_Scattering_for_Graph_Data_Analysis

> Source: 1810.03068v2_Geometric_Scattering_for_Graph_Data_Analysis.pdf

> Pages: 15

---


## Page 1


Geometric Scattering for Graph Data Analysis
Feng Gao 1 2 Guy Wolf 3 Matthew Hirn 1 4
Abstract
We explore the generalization of scattering trans-
forms from traditional (e.g., image or audio) sig-
nals to graph data, analogous to the generalization
of ConvNets in geometric deep learning, and the
utility of extracted graph features in graph data
analysis. In particular, we focus on the capacity
of these features to retain informative variability
and relations in the data (e.g., between individ-
ual graphs, or in aggregate), while relating our
construction to previous theoretical results that
establish the stability of similar transforms to fam-
ilies of graph deformations. We demonstrate the
application the our geometric scattering features
in graph classiﬁcation of social network data, and
in data exploration of biochemistry data.
1. Introduction
Over the past decade, numerous examples have established
that deep neural networks (i.e., cascades of linear operations
and simple nonlinearities) typically outperform traditional
“shallow” models in various modern machine learning appli-
cations, especially given the increasing Big Data availability
nowadays. Perhaps the most well known example of the ad-
vantages of deep networks is in computer vision, where the
utilization of 2D convolutions enable network designs that
learn cascades of convolutional ﬁlters, which have several
advantages over fully connected network architectures, both
computationally and conceptually. Indeed, in terms of super-
vised learning, convolutional neural networks (ConvNets)
hold the current state of the art in image classiﬁcation, and
have become the standard machine learning approach to-
wards processing big structured-signal data, including audio
and video processing. See, e.g., Goodfellow et al. (2016,
Chapter 9) for a detailed discussion.
Beyond their performances when applied to speciﬁc tasks,
1Department of Computational Math, Science and Engineering,
2Department of Plant, Soil & Microbial Sciences, 3Department
of Mathematics and Statistics, Universit´e de Montr´eal, Montreal,
QC, Canada 4Department of Mathematics, Michigan State Uni-
versity, East Lansing, MI, USA. Correspondence to: Guy Wolf
<guy.wolf@umontreal.ca>, Matthew Hirn <mhirn@msu.edu>.
pretrained ConvNet layers have been explored as image
feature extractors by freezing the ﬁrst few pretrained convo-
lutional layers and then retraining only the last few layers for
speciﬁc datasets or applications (e.g., Yosinski et al., 2014;
Oquab et al., 2014). Such transfer learning approaches pro-
vide evidence that suitably constructed deep ﬁlter banks
should be able to extract task-agnostic semantic information
from structured data, and in some sense mimic the opera-
tion of human visual and auditory cortices, thus supporting
the neural terminology in deep learning. An alternative
approach towards such universal feature extraction was pre-
sented in Mallat (2012), where a deep ﬁlter bank, known
as the scattering transform, is designed, rather than trained,
based on predetermined families of distruptive patterns that
should be eliminated to extract informative representations.
The scattering transform is constructed as a cascade of linear
wavelet transforms and nonlinear complex modulus opera-
tions that provides features with guaranteed invariance to
a predetermined Lie group of operations such as rotations,
translations, or scaling. Further, it also provides Lipschitz
stability to small diffeomorphisms of the inputted signal.
Following recent interest in geometric deep learning ap-
proaches for processing graph-structured data (see, for ex-
ample, Bronstein et al. (2017) and references therein), sev-
eral attempts have been made to generalize the scattering
transform to graphs (Zou & Lerman, 2018; Gama et al.,
2018) and manifolds (Perlmutter et al., 2018), which we
will generally term “geometric scattering”. These works
mostly focus on following the footsteps of Mallat (2012) in
establishing the stability of their respective constructions to
deformations of input signals or graphs. Their results essen-
tially characterize the type of disruptive information elimi-
nated by geometric scattering, by providing upper bounds
for distances between scattering features, phrased in terms
of a deformation size. Here, we further explore the notion
of geometric scattering features by considering the compli-
mentary question of how much information is retained by
them, since stability alone does not ensure useful features
in practice (e.g., a constant all-zero map would be stable
to any deformation, but would clearly be useless). In other
words, we examine whether a geometric scattering construc-
tion, deﬁned and discussed in Sec. 3, can be used as an
effective task-independent feature extractor from graphs,
and whether the resulting representations provided by them
arXiv:1810.03068v2  [cs.LG]  29 Jan 2019


## Page 2


Geometric Scattering for Graph Data Analysis
2
are sufﬁciently rich to enable intelligible data analysis by
applying traditional (Euclidean) methods.
We note that for Euclidean scattering, while stability is
established with rigorous theoretical results, the capacity of
scattering features to form an effective data representation in
practice has mostly been established via extensive empirical
examination. Indeed, scattering features have been shown
effective in several audio (e.g., Bruna & Mallat, 2013a;
And´en & Mallat, 2014; Lostanlen & Mallat, 2015; And´en
et al., 2018) and image (e.g., Bruna & Mallat, 2013b; Sifre
& Mallat, 2014; Oyallon & Mallat, 2015; Angles & Mallat,
2018) processing applications, and their advantages over
learned features are especially relevant in applications with
relatively low data availability, such as quantum chemistry
and materials science (e.g., Hirn et al., 2017; Eickenberg
et al., 2017; 2018; Brumwell et al., 2018).
Similarly, our examination of geometric scattering capacity
focuses on empirical results on several data analysis tasks,
and on two commonly used graph data types. Our results in
Sec. 4.1 show that on social network data, geometric scat-
tering features enable classic RBF-kernel SVM to match,
if not outperform, leading graph kernel methods as well
as most geometric deep learning ones. These experiments
are augmented by additional results in Sec. 4.2 that show
the geometric scattering SVM classiﬁcation rate degrades
only slightly when trained on far fewer graphs than is tradi-
tionally used in graph classiﬁcation tasks. On biochemistry
data, where graphs represent molecular structures of com-
pounds (e.g., Enzymes or proteins), we show in Sec. 4.3
that scattering features enable signiﬁcant dimensionality re-
duction. Finally, to establish their descriptive qualities, in
Sec. 4.4 we use geometric scattering features extracted from
enzyme data (Borgwardt et al., 2005a) to infer emergent
patterns of enzyme commission (EC) exchange preferences
in enzyme evolution, validated with established knowledge
from Cuesta et al. (2015). Taken together, these results illus-
trate the power of the geometric scattering approach as both
a relevant mathematical model for geometric deep learning,
and as a suitable tool for modern graph data analysis.
2. Graph Random Walks and Graph Wavelets
The Euclidean scattering transform is constructed using
wavelets deﬁned on Rd. In order to extend this construction
to graphs, we deﬁne graph wavelets as the difference be-
tween lazy random walks that have propagated at different
time scales, which mimics classical wavelet constructions
found in Meyer (1993) and more recent constructions found
in Coifman & Maggioni (2006). The underpinnings for this
construction arise out of graph signal processing, and in
particular the properties of the graph Laplacian.
Let G = (V, E, W) be a weighted graph, consisting of
n vertices V = {v1, . . . , vn}, edges E ⊆{(vℓ, vm) : 1 ≤
ℓ, m ≤n}, and weights W = {w(vℓ, vm) > 0 : (vℓ, vm) ∈
E}. Note that unweighted graphs are considered as a spe-
cial case, by setting w(vℓ, vm) = 1 for each (vℓ, vm) ∈E.
Deﬁne the n × n (weighted) adjacency matrix AG = A
of G by A(vℓ, vm) = w(vℓ, vm) if (vℓ, vm) ∈E and
zero otherwise, where we use the notation A(vℓ, vm) to
denote the (ℓ, m) entry of the matrix A so as to empha-
size the correspondence with the vertices in the graph and
to reserve sub-indices for enumerating objects. Deﬁne the
(weighted) degree of vertex vℓas deg(vℓ) = P
m A(vℓ, vm)
and the corresponding diagonal n × n degree matrix D
given by D(vℓ, vℓ) = deg(vℓ), D(vℓ, vm) = 0, ℓ̸= m.
Finally, the n × n graph Laplacian matrix LG = L on G
is deﬁned as L = D −A, and its normalized version is
N = D−1/2LD−1/2 = I−D−1/2AD−1/2. We focus on the
latter due to its close relationship with graph random walks.
The normalized graph Laplacian is a symmetric, real valued
positive semi-deﬁnite matrix, and thus has n non-negative
eigenvalues. Furthermore, if we set 0 = (0, . . . , 0)T to to
be the n × 1 vector of all zeroes, and d(vℓ) = deg(vℓ) to be
the n × 1 degree vector, then one has Nd
1/2 = 0 (where the
square root is understood to be taken entrywise). Therefore
0 is an eigenvalue of N and we write the n eigenvalues of
N as 0 = λ0 ≤λ1 ≤· · · ≤λn−1 ≤2 with corresponding
n × 1 orthonormal eigenvectors ϕ0, ϕ1, . . . , ϕn−1. If the
graph G is connected, then λ1 > 0. In order to simplify
the following discussion we assume that this is the case,
although the discussion below can be amended to include
disconnected graphs as well.
One can show ϕ0 = d
1/2/∥d
1/2∥, meaning ϕ0 is non-
negative. Since every other eigenvector is orthogonal to
ϕ0 (and thus must take positive and negative values), it is
natural to view the eigenvectors ϕk as the Fourier modes of
the graph G, with a frequency magnitude proportional to λk.
The fact that ϕ0 is in general non-constant, as opposed to
the zero frequency mode on the torus or real line, reﬂects the
non-uniform distribution of vertices in non-regular graphs.
Let x : V →R be a signal deﬁned on the vertices of the
graph G, which we will consider as an n × 1 vector with
entries x(vℓ). It follows that the Fourier transform of x
can be deﬁned as bx(k) = x · ϕk, where x · y is the stan-
dard dot product. This analogy is one of the foundations
of graph signal processing and indeed we could use this
correspondence to deﬁne wavelet operators on the graph G,
as in Hammond et al. (2011). Rather than follow this path,
though, we instead take a related path similar to Coifman
& Maggioni (2006) and Gama et al. (2018) by deﬁning the
graph wavelet operators in terms of random walks deﬁned
on G, which will avoid diagonalizing N and will allow us
to control the “spatial” graph support of the ﬁlters directly.
Deﬁne the n × n lazy random walk matrix as P =


## Page 3


Geometric Scattering for Graph Data Analysis
3
1
2
 I + AD−1
. Note that the column sums of P are all
one. It follows that P acts as a Markov operator, mapping
probability distributions to probability distribution. We refer
to P as a lazy random walk matrix since Pt governs the
probability distribution of a lazy random walk after t steps.
A single realization of a random walk is a walk (in the graph
theoretic sense) vℓ0, vℓ1, vℓ2, . . . in which the steps are cho-
sen randomly; lazy random walks allow for vℓi = vℓi+1.
More precisely, suppose that µ0(vℓ) ≥0 for each vertex
vℓand ∥µ0∥1 = 1, so that µ0 is a probability distribution
on G. We take µ0(vℓ) as the probability of a random walk
starting at vertex vℓ0 = vℓ. One can verify that µ1 = Pµ0
is also a probability distribution; each entry µ1(vℓ) gives
the probability of the random walk being located at vℓ1 = vℓ
after one step. The probability distribution for the location
of the random walk after t steps is µt = Ptµ0.
The operator P can be considered a low pass operator, mean-
ing that Px replaces x(vℓ) with localized averages of x(vℓ)
for any x. Indeed, expanding out Px(vℓ) one observes
that Px(vℓ) is the weighted average of x(vℓ) and the val-
ues x(vm) for the neighbors vm of vℓ. Similarly, the value
Ptx(vℓ) is the weighted average of x(vℓ) with all values
x(vm) such that vm is within t steps of vℓ.
Low pass operators deﬁned on Euclidean space retain the
low frequencies of a function while suppressing the high
frequencies. The random walk matrix P behaves simi-
larly.
Indeed, P is diagonalizable with n eigenvectors
φk = D
1/2ϕk and eigenvalues ωk = 1 −λk/2.
Let
yx = D−1/2x be a density normalized version of x and
set xt = Ptx; then one can show
yxt = c
yx(0)ϕ0 +
n−1
X
k=1
ωt
kc
yx(k)ϕk .
(1)
Thus, since 0 ≤ωk < 1 for k ≥1, the operator Pt pre-
serves the zero frequency of x while suppressing the high
frequencies, up to a density normalization.
High frequency responses of x can be recovered in mul-
tiple different fashions, but we utilize multiscale wavelet
transforms that group the non-zero frequencies of G into
approximately dyadic bands. As shown in Mallat (2012,
Lemma 2.12), wavelet transforms are provably stable op-
erators in the Euclidean domain, and the proof of Zou &
Lerman (2018, Theorem 5.1) indicates that similar results
on graphs may be possible. Furthermore, the multiscale
nature of wavelet transforms will allow the resulting geo-
metric scattering transform (Sec. 3) to traverse the entire
graph G in one layer, which is valuable for obtaining global
descriptions of G. Following Coifman & Maggioni (2006),
deﬁne the n × n wavelet matrix at the scale 2j as
Ψj = P2j−1 −P2j = P2j−1(I −P2j−1) .
(2)
A similar calculation as the one required for (1) shows that
j
(a) Sample graph of the bunny
manifold
j
(b) Minnesota road network
graph
Figure 1. Wavelets Ψj for increasing scale 2j left to right, applied
to Diracs centered at two different locations (marked by red circles)
in two different graphs. Vertex colors indicate wavelet values (cor-
responding to colorbars for each plot), ranging from yellow/green
indicating positive values to blue indicating negative values. Both
graphs are freely available from PyGSP (2018).
Ψjx partially recovers c
yx(k) for k ≥1. The value Ψjx(vℓ)
aggregates the signal information x(vm) from the vertices
vm that are within 2j steps of vℓ, but does not average the
information like the operator P2j. Instead, it responds to
sharp transitions or oscillations of the signal x within the
neighborhood of vℓwith radius 2j (in terms of the graph
path distance). The smaller the wavelet scale 2j, the higher
the frequencies Ψjx recovers in x. The wavelet coefﬁcients
up to the scale 2J are:
Ψ(J)x(vℓ) = [Ψjx(vℓ) : 1 ≤j ≤J] .
(3)
Figure 1 plots the wavelets on two different graphs.
3. Geometric Scattering on Graphs
A geometric wavelet scattering transform follows a similar
construction as the (Euclidean) wavelet scattering transform
of Mallat (2012), but leverages a graph wavelet transform.
In this paper we utilize the wavelet transform deﬁned in
(3) of the previous section, but remark that in principle any
graph wavelet transform could be used (see, e.g., Zou &
Lerman, 2018). In Sec. 3.1 we deﬁne the graph scattering
transform, in Sec. 3.2 we discuss its relation to other recently
proposed graph scattering constructions (Gama et al., 2018;
Zou & Lerman, 2018), and in Sec. 3.3 we describe several
of its desirable properties as compared to other geometric
deep learning algorithms on graphs.
3.1. Geometric scattering deﬁnitions
Machine learning algorithms that compare and classify
graphs must be invariant to graph isomorphism, i.e., re-
indexations of the vertices and corresponding edges. A
common way to obtain invariant graph features is via sum-
mation operators, which act on a signal x = xG that can
be deﬁned on any graph G, e.g., x(vℓ) = deg(vℓ). The
geometric scattering transform, which is described in the
remainder of this section, follows such an approach.
The simplest summation operator computes the sum of the
responses of the signal x. As described in Verma & Zhang


## Page 4


Geometric Scattering for Graph Data Analysis
4
(2018), this invariant can be complemented by higher order
summary statistics of x, the collection of which are statis-
tical moments, and which are also referred to as “capsules”
in that work. For example, the unnormalized qth moments
of x yield the following “zero” order scattering moments:
Sx(q) =
n
X
ℓ=1
x(vℓ)q,
1 ≤q ≤Q
(4)
We can also replace (4) with normalized (i.e., standardized)
moments of x, in which case we store its mean (q = 1),
variance (q = 2), skew (q = 3), kurtosis (q = 4), and so on.
In what follows we discuss the unnormalized moments since
their presentation is simpler. The invariants Sx(q) do not
capture the full variability of x and hence the graph G upon
which the signal x is deﬁned. We thus complement these
moments with summary statistics derived from the wavelet
coefﬁcients of x, which will lead naturally to the graph
ConvNet structure of the geometric scattering transform.
Observe, analogously to the Euclidean setting, that in com-
puting Sx(1), which is the summation of x(vℓ) over V , we
have captured the zero frequency of yx = D−1/2x since
Pn
ℓ=1 x(vℓ) = x · 1 = yx · d
1/2 = ∥d
1/2∥c
yx(0). Higher
order moments of x can incorporate the full range of fre-
quencies in x, e.g. Sx(2) = Pn
ℓ=1 x(vℓ)2 = Pn
k=1 bx(k)2,
but they are mixed into one invariant coefﬁcient. We can
separate and recapture the high frequencies of x by com-
puting its wavelet coefﬁcients Ψ(J)x, which were deﬁned
in (3). However, Ψ(J)x is not invariant to permutations of
the vertex indices; in fact, it is equivariant. Before summing
the individual wavelet coefﬁcient vectors Ψjx, though, we
must ﬁrst apply a pointwise nonlinearity. Indeed, deﬁne
1 = (1, . . . , 1)T to be the n × 1 vector of all ones, and
note that PT 1 = 1, meaning that 1 is a left eigenvector of
P with eigenvalue 1. It follows that ΨT
j 1 = 0 and thus
Pn
ℓ=1 Ψjx(vℓ) = Ψjx · 1 = 1T Ψjx = 0.
We thus apply the absolute value nonlinearity, to obtain
nonlinear equivariant coefﬁcients |Ψ(J)x| = {|Ψjx| : 1 ≤
j ≤J}. We use absolute value because it is equivariant to
vertex permutations, non-expansive, and when combined
with traditional wavelet transforms on Euclidean domains,
yields a provably stable scattering transform for q = 1.
Furthermore, initial theoretical results in Zou & Lerman
(2018) and Gama et al. (2018) indicate that similar graph
based scattering transforms possess certain types of stability
properties as well. As in (4), we extract invariant coefﬁcients
from |Ψjx| by computing its moments, which deﬁne the
ﬁrst order geometric scattering moments:
Sx(j, q) =
n
X
ℓ=1
|Ψjx(vℓ)|q, 1 ≤j ≤J, 1 ≤q ≤Q (5)
These ﬁrst order scattering moments aggregate complimen-
tary multiscale geometric descriptions of G into a collection
of invariant multiscale statistics. These invariants give a
ﬁner partition of the frequency responses of x. For exam-
ple, whereas Sx(2) mixed all frequencies of x, we see that
Sx(j, 2) only mixes the frequencies of x captured by Ψj.
First order geometric scattering moments can be augmented
with second order geometric scattering moments by iterating
the graph wavelet and absolute value transforms. These
moments are deﬁned as:
Sx(j, j′, q) =
n
X
ℓ=1
|Ψj′|Ψjx(vℓ)||q, 1 ≤j < j′ ≤J
1 ≤q ≤Q ,
(6)
which consists of reapplying the wavelet transform operator
Ψ(J) to each |Ψjx| and computing the summary statistics
of the magnitudes of the resulting coefﬁcients. The inter-
mediate equivariant coefﬁcients |Ψj′|Ψjx|| and resulting
invariant statistics Sx(j, j′, q) couple two scales 2j and 2j′
within the graph G, creating features that bind patterns of
smaller subgraphs within G with patterns of larger sub-
graphs (e.g., circles of friends of individual people with
larger community structures in social network graphs). The
transform can be iterated additional times, leading to third
order features and beyond, and thus has the general structure
of a graph ConvNet.
The collection of graph scattering moments Sx
=
{Sx(q), Sx(j, q), Sx(j, j′, q)} (illustrated in Fig. 2(a))
provides a rich set of multiscale invariants of the graph G.
These can be used in supervised settings as input to graph
classiﬁcation or regression models, or in unsupervised set-
tings to embed graphs into a Euclidean feature space for
further exploration, as demonstrated in Sec. 4.
3.2. Stability and capacity of geometric scattering
In order to assess the utility of scattering features for repre-
senting graphs, two properties have to be considered: stabil-
ity and capacity. First, the stability property aims to provide
an upper bound on distances between similar graphs that
only differ by types of deformations that can be treated as
noise. This property has been the focus of both Zou & Ler-
man (2018) and Gama et al. (2018), and in particular the
latter shows that a diffusion scattering transform yields fea-
tures that are stable to graph structure deformations whose
size can be computed via the diffusion framework (Coifman
& Maggioni, 2006) that forms the basis for their construc-
tion. While there are some technical differences between
the geometric scattering here and the diffusion scattering
in Gama et al. (2018), these constructions are sufﬁciently
similar that we can expect both of them to have analogous
stability properties. Therefore, we mainly focus here on the
complementary property of the scattering transform capac-
ity to provide a rich feature space for representing graph
data without eliminating informative variance in them.


## Page 5


Geometric Scattering for Graph Data Analysis
5
x
∥. . . ∥q
q
P2j−1
I −P2j−1
| . . . |
∥. . . ∥q
q
P2j−1
I −P2j−1
| . . . |
P2j′−1
I −P2j′−1
| . . . |
∥. . . ∥q
q
Sx
|
{z
}
Ψj
|
{z
}
Ψj′
|
{z
}
1≤q≤Q
(a) Representative zeroth-, ﬁrst-, and second-order cascades of the
geometric scattering transform for an input graph signal x.
G = (V, E, W)
x : V →R
Adjacency matrix:
A(vi, vj)
Signal vector:
x(vi)
Diffusion wavelets:
Ψj = P2j−1 −P2j
P = 1
2 (I + AD−1)
Ψj
Scattering
(a)
x 7→Sx
Traditional
Euclidean
algorithms
(e.g., SVM/PCA)
(b) Architecture for using geometric scattering of graph G and
signal x in graph data analysis, as demonstrated in Sec. 4.
Figure 2. Illustration of (a) the proposed scattering feature extraction (see eqs. 4, 5, and 6), and (b) its application for graph data analysis.
We note that even in the classical Euclidean case, while
the stability of scattering transforms to deformations can
be established analytically (Mallat, 2012), their capacity is
typically examined by empirical evidence when applied to
machine learning tasks (e.g., Bruna & Mallat, 2011; Sifre
& Mallat, 2012; And´en & Mallat, 2014). Similarly, in the
graph processing settings, we examine the capacity of our
proposed geometric scattering features via their discrimina-
tive power in graph data analysis tasks, which are described
in detail in Sec. 4. We show that geometric scattering en-
ables graph embedding in a relatively low dimensional Eu-
clidean space, while preserving insightful properties in the
data. Beyond establishing the capacity of our speciﬁc con-
struction, these results also indicate the viability of graph
scattering transforms as universal feature extractors on graph
data, and complement the stability results established in Zou
& Lerman (2018) and Gama et al. (2018).
3.3. Geometric scattering compared to other feed
forward graph ConvNets
We give a brief comparison of geometric scattering with
other graph ConvNets, with particular interest in isolating
the key principles for building accurate graph ConvNet clas-
siﬁers. We begin by remarking that like several other suc-
cessful graph neural networks, the graph scattering trans-
form is equivariant to vertex permutations (i.e., commutes
with them) until the ﬁnal features are extracted. This idea
has been discussed in depth in various articles, including
Kondor et al. (2018b), so we limit the discussion to ob-
serving that the geometric scattering transform thus propa-
gates nearly all of the information in x through the multiple
wavelet and absolute value layers, since only the absolute
value operation removes information on x. As in Verma &
Zhang (2018), we aggregate covariant responses via multi-
ple summary statistics (i.e., moments), which are referred
to there as a capsule. In the scattering context, at least, this
idea is in fact not new and has been previously used in the
Euclidean setting for the regression of quantum mechani-
cal energies in Eickenberg et al. (2018; 2017) and texture
synthesis in Bruna & Mallat (2018). We also point out
that, unlike many deep learning classiﬁers (graph included),
a graph scattering transform extracts invariant statistics at
each layer/order. These intermediate layer statistics, while
necessarily losing some information in x (and hence G),
provide important coarse geometric invariants that eliminate
needless complexity in subsequent classiﬁcation or regres-
sion. Furthermore, such layer by layer statistics have proven
useful in characterizing signals of other types (e.g., texture
synthesis in Gatys et al., 2015).
A graph wavelet transform Ψ(J)x decomposes the geom-
etry of G through the lens of x, along different scales.
Graph ConvNet algorithms also obtain multiscale repre-
sentations of G, but several works, including Atwood &
Towsley (2016) and Zhang et al. (2018), propagate infor-
mation via a random walk. While random walk operators
like Pt act at different scales on the graph G, per the anal-
ysis in Sec. 2 we see that Pt for any t will be dominated
by the low frequency responses of x. While subsequent
nonlinearities may be able to recover this high frequency
information, the resulting transform will most likely be un-
stable due to the suppression and then attempted recovery of
the high frequency content of x. Alternatively, features de-
rived from Ptx may lose the high frequency responses of x,
which are useful in distinguishing similar graphs. The graph
wavelet coefﬁcients Ψ(J)x, on the other hand, respond most
strongly within bands of nearly non-overlapping frequen-
cies, each with a center frequency kj that depends on Ψj.
Finally, graph labels are often complex functions of both
local and global subgraph structure within G. While graph
ConvNets are adept at learning local structure within G, as
detailed in Verma & Zhang (2018) they require many layers
to obtain features that aggregate macroscopic patterns in the
graph. This is due to the use of ﬁxed size ﬁlters, which often
only incorporate information from the neighbors of a vertex.
The training of such networks is difﬁcult due to the limited
size of many graph classiﬁcation databases (see the sup-
plementary information). Geometric scattering transforms
have two advantages in this regard: (a) the wavelet ﬁlters
are designed; and (b) they are multiscale, thus incorporating
macroscopic graph patterns in every layer/order.
4. Application & Results
To establish the geometric scattering features as an effective
graph representation for data analysis, we examine their
performance here in four graph data analysis applications.


## Page 6


Geometric Scattering for Graph Data Analysis
6
Namely, in Sec. 4.1 we consider graph classiﬁcation on
social networks (from Yanardag & Vishwanathan, 2015),
in Sec. 4.2 we consider the impact of low training data
availability on classiﬁcation, in Sec. 4.3 we examine di-
mensionality reduction aspects of geometric scattering, and
ﬁnally, in Sec. 4.4 we consider data exploration of enzyme
graphs, where geometric scattering enables unsupervised
(descriptive) recovery of EC change preferences in enzyme
evolution. A common theme in all these applications is the
application of geometric scattering as an unsupervised task-
independent feature extraction that embeds input graphs
of varying sizes (with associated graph signals) into a Eu-
clidean space formed by scattering features. Then, the ex-
tracted feature vectors are passed to traditional (Euclidean)
machine learning algorithms, such as SVM for classiﬁca-
tion or PCA for dimensionality reduction, to perform down-
stream analysis. Our results show that our scattering features
provide simpliﬁed representation (e.g., in dimensionality
and extrapolation ability) of input graphs, which we conjec-
ture is a result of their stability properties, while also being
sufﬁciently rich to capture meaningful relations between
graphs for predictive and descriptive purposes.
4.1. Graph classiﬁcation on social networks
As a ﬁrst application of geometric scattering, we apply it
to graph classiﬁcation of social network data taken from
Yanardag & Vishwanathan (2015). In particular, this work
introduced six social network data sets extracted from sci-
entiﬁc collaborations (COLLAB), movie collaborations
(IMDB-B & IMDB-M), and Reddit discussion threads
(REDDIT-B, REDDIT-5K, REDDIT-12K). There are also
biochemistry data sets often used in the graph classiﬁcation
literature; for completeness, we include in the supplemental
materials further results on these data sets. A brief descrip-
tion of each data set can also be found in the supplement.
The social network data provided by Yanardag & Vish-
wanathan (2015) contains graph structures but no associated
graph signals. Therefore we compute the eccentricity (for
connected graphs) and clustering coefﬁcient of each vertex,
and use these as input signals to the geometric scattering
transform. In principle, any general node characteristic
could be used, although we remark that x = d, the ver-
tex degree vector, is not useful in our construction since
Ψjd = 0. After computing the scattering moments1 of
these two input signals, they are concatenated to form a
single vector. This scattering feature vector is a consistent
Euclidean representation of the graph, which is indepen-
dent of the original graph sizes (i.e., number of vertices or
edges), and thus we can apply any traditional classiﬁer to
1We use the normalized scattering moments for classiﬁcation,
since they perform slightly better than the un-normalized moments.
Also we use J = 5 and q = 4 for all scattering feature generations.
it. In particular, we use here the standard SVM classiﬁer
with an RBF kernel, which is popular and effective in many
applications and also performs well in this case.
We evaluate the classiﬁcation results of our SVM-based
geometric scattering classiﬁcation (GS-SVM) using ten-
fold cross validation (as explained, for completeness, in
the supplament), which is standard practice in other graph
classiﬁcation works. We compare our results to 11 promi-
nent methods that report results for most, if not all, of the
considered datasets. Out of these, ﬁve are graph kernel
methods, namely: Weisfeiler-Lehman graph kernels (WL,
Shervashidze et al., 2011), propagation kernel (PK, Neu-
mann et al., 2012), Graphlet kernels (Shervashidze et al.,
2009), Random walks (RW, G¨artner et al., 2003), deep
graph kernels (DGK, Yanardag & Vishwanathan, 2015), and
Weisfeiler-Lehman optimal assignment kernels (WL-OA,
Kriege et al., 2016). The other six are recent geometric deep
learning algorithms: deep graph convolutional neural net-
work (DGCNN, Zhang et al., 2018), Graph2vec (Narayanan
et al., 2017), 2D convolutional neural networks (2DCNN,
Tixier et al., 2017), covariant compositional networks (CCN,
Kondor et al., 2018a), Patchy-san (PSCN, Niepert et al.,
2016, with k = 10), diffusion convolutional neural net-
works (DCNN, Atwood & Towsley, 2016), graph capsule
convolutional neural networks (GCAPS-CNN, Verma &
Zhang, 2018), recurrent neural network autoencoders (S2S-
N2N-PP, Taheri et al., 2018), and the graph isomorphism
network (GIN, Xu et al., 2019).
Following the standard format of reported classiﬁcation per-
formances for these methods (per their respective references,
see also the supplement), our results are reported in the form
of average accuracy ± standard deviation (in percentages)
over the ten cross-validation folds. We note that since some
methods are not reported for all datasets, we mark N/A
when appropriate. Table 1 reports the results.
The geometric scattering transform and related variants pre-
sented in Zou & Lerman (2018) and Gama et al. (2018)
is a mathematical model for graph ConvNets. However,
it is natural to ask if this model accurately reﬂects what
is done in practice. A useful model may not obtain state
of the art performance, but should be competitive with the
current state of the art, lest the model may not capture the
underlying complexity of the most powerful methods. Ex-
amining Table 1 one can see that the GS-SVM classiﬁer
matches or outperforms all but the two most recent meth-
ods, i.e., S2S-N2N-PP (Taheri et al., 2018) and GIN (Xu
et al., 2019). With regards to these two approaches, the
GS-SVM outperforms S2S-N2N-PP (Taheri et al., 2018) on
3/6 datasets. Finally, while GIN (Xu et al., 2019) outper-
forms geometric scattering on 5/6 datasets, the results on
COLLAB and IMDB-B are not statistically signiﬁcant, and
on the REDDIT datasets the geometric scattering approach


## Page 7


Geometric Scattering for Graph Data Analysis
7
Table 1. Comparison of the proposed GS-SVM classiﬁer with leading graph kernel and deep learning methods on social graph datasets.
COLLAB
IMDB-B
IMDB-M
REDDIT-B
REDDIT-5K
REDDIT-12K
WL
77.82 ± 1.45
71.60 ± 5.16
N/A
78.52 ± 2.01
50.77 ± 2.02
34.57 ± 1.32
Graph kernel
z
}|
{
Graphlet
73.42 ± 2.43
65.40 ± 5.95
N/A
77.26 ± 2.34
39.75 ± 1.36
25.98 ± 1.29
WL-OA
80.70 ± 0.10
N/A
N/A
89.30 ± 0.30
N/A
N/A
GK
72.84 ± 0.28
65.87 ± 0.98
43.89 ± 0.38
77.34 ± 0.18
41.01 ± 0.17
N/A
DGK
73.00 ± 0.20
66.90 ± 0.50
44.50 ± 0.50
78.00 ± 0.30
41.20 ± 0.10
32.20 ± 0.10
DGCNN
73.76 ± 0.49
70.03 ± 0.86
47.83 ± 0.85
N/A
48.70 ± 4.54
N/A
Deep learning
z
}|
{
2D CNN
71.33 ± 1.96
70.40 ± 3.85
N/A
89.12 ± 1.70
52.21 ± 2.44
48.13 ± 1.47
PSCN (k = 10)
72.60 ± 2.15
71.00 ± 2.29
45.23 ± 2.84
86.30 ± 1.58
49.10 ± 0.70
41.32 ± 0.42
GCAPS-CNN
77.71 ± 2.51
71.69 ± 3.40
48.50 ± 4.10
87.61 ± 2.51
50.10 ± 1.72
N/A
S2S-P2P-NN
81.75 ± 0.80
73.80 ± 0.70
51.19 ± 0.50
86.50 ± 0.80
52.28 ± 0.50
42.47 ± 0.10
GIN-0 (MLP-SUM)
80.20 ± 1.90
75.10 ± 5.10
52.30 ± 2.80
92.40 ± 2.50
57.50 ± 1.50
N/A
GS-SVM
79.94 ± 1.61
71.20 ± 3.25
48.73 ± 2.32
89.65 ± 1.94
53.33 ± 1.37
45.23 ± 1.25
trails only GIN (Xu et al., 2019). We thus conclude that the
geometric scattering transform yields a rich set of invariant
statistical moments, which have nearly the same capacity as
the current state of the art in graph neural networks.
4.2. Classiﬁcation with low training-data availability
Many modern deep learning methods require large amounts
of training data to generate representative features. On
the contrary, geometric scattering features are based on
each graph without any training processes. In this section,
we demonstrate the performance of the GS-SVM under
low training-data availability and show that the scattering
features can embed enough graph information that even
under extreme conditions (e.g. only 20% training data), they
can still maintain relatively good classiﬁcation results.
We performed graph classiﬁcation under four train-
ing/validation/test splits: 80%/10%/10%, 70%/10%/20%,
40%/10%/50% and 20%/10%/70%. We did 10-fold, 5-fold
and 2-fold cross validation for the ﬁrst three splits. For
the last split, we randomly formed a 10 folds pool, from
which we randomly selected 3 folds for training/validation
and repeated this process ten times. Detailed classiﬁcation
results can be found in the supplement. Following Sec. 4.1,
we discuss the classiﬁcation accuracy on six social datasets
(a)
(b)
Figure 3. (a) Box plot showing the drop in SVM classiﬁcation
accuracy over social graph datasets when reducing training set size
(horizontal axis marks portion of data used for testing); (b) Relation
between explained variance, SVM classiﬁcation accuracy, and
PCA dimensions over scattering features in ENZYMES dataset.
under these splits. When the training data is reduced from
90% to 80%, the classiﬁcation accuracy in fact increased
by 0.047%, which shows the GS-SVM classiﬁcation accu-
racy is not affected by the decrease in training size. Further
reducing the training size to 50% results in an average de-
crease of classiﬁcation accuracy of 1.40% while from 90%
to 20% causes an average decrease of 3.00%. Fig. 3 gives a
more nuanced statistical description of these results.
4.3. Dimensionality reduction
We now consider the viability of scattering-based embed-
ding for dimensionality reduction of graph data. As a repre-
sentative example, we consider here the ENZYMES dataset
introduced in Borgwardt et al. (2005b), which contains 600
enzymes evenly split into six enzyme classes (i.e., 100 en-
zymes from each class). While the Euclidean notion of
dimensionality is not naturally available in graph data, we
note that graphs in this dataset have, on average, 124.2 edges,
29.8 vertices, and 3 features per vertex. Therefore, the data
here can be considered signiﬁcantly high dimensional in its
original representation, which is not amenable to traditional
dimensionality reduction techniques.
To perform scattering-based dimensionality reduction, we
applied PCA to geometric scattering features extracted from
input enzyme graphs in the data, while choosing the number
of principal components to capture 99%, 90%, 80% and
50% explained variance. For each of these thresholds, we
computed the mean classiﬁcation accuracy (with ten-fold
cross validation) of SVM applied to the GS-PCA low dimen-
sional space, as well as the dimensionality of this space. The
relation between dimensionality, explained variance, and
SVM accuracy is shown in Fig. 3, where we can observe that
indeed geometric scattering combined with PCA enables
signiﬁcant dimensionality reduction (e.g., to R16 with 90%
exp. variance) with only a small impact on classiﬁcation
accuracy. Finally, we also consider the PCA dimension-
ality of each individual enzyme class in the data (in the
scattering feature space), as we expect scattering to reduce
the variability in each class w.r.t. the full feature space. In-
deed, in this case, individual classes have 90% exp. variance
PCA dimensionality ranging between 6 and 10, which is
signiﬁcantly lower than the 16 dimensions of the entire PCA


## Page 8


Geometric Scattering for Graph Data Analysis
8
space. We note that similar results can also be observed
for the social network data discussed in previous sections,
where on average 90% explained variances are captured by
nine dimensions, yielding a drop of 3.81% in mean SVM
accuracy; see the supplement for complete results.
4.4. Data exploration: Enzyme class exchange
preferences
Geometric scattering essentially provides a task independent
representation of graphs in a Euclidean feature space. There-
fore, it is not limited to supervised learning applications,
and can be also utilized for exploratory graph-data analysis,
as we demonstrate in this section. We focus our discussion
in particular on the ENZYMES dataset described in the pre-
vious section. Here, geometric scattering features can be
considered as providing “signature” vectors for individual
enzymes, which can be used to explore interactions between
the six top level enzyme classes, labelled by their Enzyme
Commission (EC) numbers (Borgwardt et al., 2005a). In
order to emphasize the properties of scattering-based feature
extraction, rather than downstream processing, we mostly
limit our analysis of the scattering feature space to linear
operations such as principal component analysis (PCA).
To explore the scattering feature space, and the richness of
information captured by it, we use it to infer relations be-
tween EC classes. First, for each enzyme e, with scattering
feature vector ve (i.e., with Sx for all vertex features x),
we compute its distance from class EC-j, with PCA sub-
space Cj, as the projection distance: dist(e, EC-j) = ∥ve −
projSjve∥. Then, for each enzyme class EC-i, we compute
the mean distance of enzymes in it from the subspace of each
EC-j class as D(i, j) = mean{dist(e, EC-j) : e ∈EC-i}.
These distances are summarized in the supplement, as well
(a) Observed
(b) Inferred
Figure 4. Comparison of EC exchange preferences in enzyme
evolution: (a) observed in Cuesta et al. (2015), and (b) in-
ferred from scattering features via pref(EC-i, EC-j) := wj ·
h
min
n
D(i,j)
D(i,i) , D(j,i)
D(j,j)
oi−1
; wj = portion of enzymes in EC-j
that choose another EC as their nearest subspace; D(i, j) = mean
dist. of enzymes in EC-i from PCA (90% exp. var.) subspace of
EC-j . Our inference (b) mainly recovers (a).
as the proportion of points from each class that have their
true EC as their nearest (or second nearest) subspace in the
scattering feature space. In general, 48% of enzymes select
their true EC as the nearest subspace (with additional 19%
as second nearest), but these proportions vary between in-
dividual EC classes. Finally, we use these scattering-based
distances to infer EC exchange preferences during enzyme
evolution, which are presented in Fig. 4 and validated with
respect to established preferences observed and reported
in Cuesta et al. (2015). We note that the result there is ob-
served independently from the ENZYMES dataset. In par-
ticular, the portion of enzymes considered from each EC is
different between these data, since Borgwardt et al. (2005b)
took special care to ensure each EC class in ENZYMES has
exactly 100 enzymes in it. However, we notice that in fact
the portion of enzymes (in each EC) that choose the wrong
EC as their nearest subspace, which can be considered as EC
“incoherence” in the scattering feature space, correlates well
with the proportion of evolutionary exchanges generally ob-
served for each EC in Cuesta et al. (2015), and therefore we
use these as EC weights (see Fig. 4). Our results in Fig. 4
demonstrate that scattering features are sufﬁciently rich to
capture relations between enzyme classes, and indicate that
geometric scattering has the capacity to uncover descriptive
and exploratory insights in graph data analysis.
5. Conclusion
We presented the geometric scattering transform as a deep
ﬁlter bank for feature extraction on graphs, which gener-
alizes the Euclidean scattering transform. A reasonable
criticism of the scattering theory approach to understanding
geometric deep learning is that it is not clear if the scatter-
ing model is a suitable facsimile for powerful graph neural
networks that are obtaining impressive results on graph clas-
siﬁcation tasks and related graph data analysis problems. In
this paper we showed that in fact, at least empirically, this
line of criticism is unfounded and indeed further theoretical
study of geometric scattering transforms on graphs is war-
ranted. Our evaluation results on graph classiﬁcation and
data exploration show the potential of the produced scatter-
ing features to serve as universal representations of graphs.
Indeed, classiﬁcation using these features with relatively
simple classiﬁer models, dimension reduced feature sets,
and small training sets nevertheless reach high accuracy re-
sults on most commonly used graph classiﬁcation datasets.
Finally, the geometric scattering features provide a new way
for computing and considering global graph representations,
independent of speciﬁc learning tasks. They raise the pos-
sibility of embedding entire graphs in Euclidean space and
computing meaningful distances between graphs, which can
be used for both supervised and unsupervised learning, as
well as exploratory analysis of graph-structured data.


## Page 9


Geometric Scattering for Graph Data Analysis
9
ACKNOWLEDGMENTS
F.G. is supported by the grant P42 ES004911 through the National Institute of Environmental Health Sciences of the National
Institutes of Health. M.H. is supported by the Alfred P. Sloan Fellowship (grant FG-2016-6607), the DARPA YFA (grant
D16AP00117), and NSF grant 1620216.
References
And´en, J. and Mallat, S. Deep scattering spectrum. IEEE Transactions on Signal Processing, 62(16):4114–4128, August
2014.
And´en, J., Lostanlen, V., and Mallat, S. Classiﬁcation with joint time-frequency scattering. arXiv:1807.08869, 2018.
Angles, T. and Mallat, S. Generative networks as inverse problems with scattering transforms. In International Conference
on Learning Representations, 2018.
Atwood, J. and Towsley, D. Diffusion-convolutional neural networks. In Advances in Neural Information Processing
Systems 29, pp. 1993–2001, 2016.
Borgwardt, K. M., Ong, C. S., Sch¨onauer, S., Vishwanathan, S., Smola, A. J., and Kriegel, H.-P. Protein function prediction
via graph kernels. Bioinformatics, 21(suppl 1):i47–i56, 2005a.
Borgwardt, K. M., Ong, C. S., Sch¨onauer, S., Vishwanathan, S., Smola, A. J., and Kriegel, H.-P. Protein function prediction
via graph kernels. Bioinformatics, 21(suppl 1):i47–i56, 2005b.
Bronstein, M. M., Bruna, J., LeCun, Y., Szlam, A., and Vandergheynst, P. Geometric deep learning: Going beyond euclidean
data. IEEE Signal Processing Magazine, 34(4):18–42, 2017.
Brumwell, X., Sinz, P., Kim, K. J., Qi, Y., and Hirn, M. Steerable wavelet scattering for 3D atomic systems with application to
Li-Si energy prediction. In NeurIPS Workshop on Machine Learning for Molecules and Materials, pp. arXiv:1812.02320,
2018.
Bruna, J. and Mallat, S. Classiﬁcation with scattering operators. In 2011 IEEE Conference on Computer Vision and Pattern
Recognition (CVPR), pp. 1561–1566, 2011.
Bruna, J. and Mallat, S. Audio texture synthesis with scattering moments. arXiv:1311.0407, 2013a.
Bruna, J. and Mallat, S. Invariant scattering convolution networks. IEEE Transactions on Pattern Analysis and Machine
Intelligence, 35(8):1872–1886, August 2013b.
Bruna, J. and Mallat, S. Multiscale sparse microcanonical models. arXiv:1801.02013, 2018.
Coifman, R. R. and Maggioni, M. Diffusion wavelets. Applied and Computational Harmonic Analysis, 21(1):53–94, 2006.
Cuesta, S. M., Rahman, S. A., Furnham, N., and Thornton, J. M. The classiﬁcation and evolution of enzyme function.
Biophysical Journal, 109(6):1082–1086, 2015.
Debnath, A. K., Lopez de Compadre, R. L., Debnath, G., Shusterman, A. J., and Hansch, C. Structure-activity relationship of
mutagenic aromatic and heteroaromatic nitro compounds. correlation with molecular orbital energies and hydrophobicity.
Journal of medicinal chemistry, 34(2):786–797, 1991.
Dobson, P. D. and Doig, A. J. Distinguishing enzyme structures from non-enzymes without alignments. Journal of molecular
biology, 330(4):771–783, 2003.
Eickenberg, M., Exarchakis, G., Hirn, M., and Mallat, S. Solid harmonic wavelet scattering: Predicting quantum molecular
energy from invariant descriptors of 3D electronic densities. In Advances in Neural Information Processing Systems 30
(NIPS 2017), pp. 6540–6549, 2017.
Eickenberg, M., Exarchakis, G., Hirn, M., Mallat, S., and Thiry, L. Solid harmonic wavelet scattering for predictions of
molecule properties. Journal of Chemical Physics, 148:241732, 2018.


## Page 10


Geometric Scattering for Graph Data Analysis
10
Gama, F., Ribeiro, A., and Bruna, J. Diffusion scattering transforms on graphs. arXiv:1806.08829, 2018.
G¨artner, T., Flach, P., and Wrobel, S. On graph kernels: Hardness results and efﬁcient alternatives. In Learning theory and
kernel machines, pp. 129–143. Springer, 2003.
Gatys, L., Ecker, A. S., and Bethge, M. Texture synthesis using convolutional neural networks. In Advances in Neural
Information Processing Systems 28, pp. 262–270, 2015.
Goodfellow, I., Bengio, Y., and Courville, A. Deep Learning. MIT Press, 2016. http://www.deeplearningbook.
org.
Hammond, D. K., Vandergheynst, P., and Gribonval, R. Wavelets on graphs via spectral graph theory. Applied and
Computational Harmonic Analysis, 30:129–150, 2011.
Hirn, M., Mallat, S., and Poilvert, N. Wavelet scattering regression of quantum chemical energies. Multiscale Modeling and
Simulation, 15(2):827–863, 2017. arXiv:1605.04654.
Kondor, R., Son, H. T., Pan, H., Anderson, B., and Trivedi, S. Covariant compositional networks for learning graphs. arXiv
preprint, pp. arXiv:1801.02144, 2018a.
Kondor, R., Son, H. T., Pan, H., Anderson, B., and Trivedi, S. Covariant compositional networks for learning graphs.
arXiv:1801.02144, 2018b.
Kriege, N. M., Giscard, P.-L., and Wilson, R. On valid optimal assignment kernels and applications to graph classiﬁcation. In
Lee, D. D., Sugiyama, M., Luxburg, U. V., Guyon, I., and Garnett, R. (eds.), Advances in Neural Information Processing
Systems 29, pp. 1623–1631. Curran Associates, Inc., 2016.
Lostanlen, V. and Mallat, S. Wavelet scattering on the pitch spiral. In Proceedings of the 18th International Conference on
Digital Audio Effects, pp. 429–432, 2015.
Mallat, S. Group invariant scattering. Communications on Pure and Applied Mathematics, 65(10):1331–1398, October
2012.
Meyer, Y. Wavelets and Operators, volume 1. Cambridge University Press, 1993.
Narayanan, A., Chandramohan, M., Venkatesan, R., Chen, L., Liu, Y., and Jaiswal, S. graph2vec: Learning distributed
representations of graphs. arXiv preprint, pp. arXiv:1707.05005, 2017.
Neumann, M., Patricia, N., Garnett, R., and Kersting, K. Efﬁcient graph kernels by randomization. In Joint European
Conference on Machine Learning and Knowledge Discovery in Databases, pp. 378–393. Springer, 2012.
Niepert, M., Ahmed, M., and Kutzkov, K. Learning convolutional neural networks for graphs. In International conference
on machine learning, pp. 2014–2023, 2016.
Oquab, M., Bottou, L., Laptev, I., and Sivic, J. Learning and transferring mid-level image representations using convolutional
neural networks. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 1717–1724,
2014.
Oyallon, E. and Mallat, S. Deep roto-translation scattering for object classiﬁcation. In Proceedings in IEEE CVPR 2015
conference, 2015. arXiv:1412.8659.
Perlmutter, M., Wolf, G., and Hirn, M. Geometric scattering on manifolds. In NeurIPS Workshop on Integration of Deep
Learning Theories, pp. arXiv:1812.06968, 2018.
PyGSP. Graph signal processing in python (https://pygsp.readthedocs.io/en/stable/index.html),
Accessed in September 2018.
Shervashidze, N., Vishwanathan, S., Petri, T., Mehlhorn, K., and Borgwardt, K. Efﬁcient graphlet kernels for large graph
comparison. In van Dyk, D. and Welling, M. (eds.), Proceedings of the 12th International Conference on Artiﬁcial
Intelligence and Statistics, volume 5 of Proceedings of Machine Learning Research, pp. 488–495, Hilton Clearwater
Beach Resort, Clearwater Beach, Florida USA, 2009. PMLR.


## Page 11


Geometric Scattering for Graph Data Analysis
11
Shervashidze, N., Schweitzer, P., Leeuwen, E. J. v., Mehlhorn, K., and Borgwardt, K. M. Weisfeiler-Lehman graph kernels.
Journal of Machine Learning Research, 12(Sep):2539–2561, 2011.
Sifre, L. and Mallat, S. Combined scattering for rotation invariant texture analysis. In Proceedings of the ESANN 2012
conference, 2012.
Sifre, L. and Mallat, S. Rigid-motion scattering for texture classiﬁcation. arXiv:1403.1687, 2014.
Taheri, A., Gimpel, K., and Berger-Wolf, T. Learning graph representations with recurrent neural network autoencoders. In
KDD Deep Learning Day, 2018.
Tixier, A. J.-P., Nikolentzos, G., Meladianos, P., and Vazirgiannis, M. Classifying graphs as images with convolutional
neural networks. arXiv preprint, pp. arXiv:1708.02218, 2017.
Toivonen, H., Srinivasan, A., King, R. D., Kramer, S., and Helma, C. Statistical evaluation of the predictive toxicology
challenge 2000–2001. Bioinformatics, 19(10):1183–1193, 2003.
Verma, S. and Zhang, Z.-L. Graph capsule convolutional neural networks. arXiv preprint, pp. arXiv:1805.08090, 2018.
Wale, N., Watson, I. A., and Karypis, G. Comparison of descriptor spaces for chemical compound retrieval and classiﬁcation.
Knowledge and Information Systems, 14(3):347–375, 2008.
Xu, K., Hu, W., Leskovec, J., and Jegelka, S. How powerful are graph neural networks? In International Conference on
Learning Representations, 2019.
Yanardag, P. and Vishwanathan, S. Deep graph kernels. In Proceedings of the 21th ACM SIGKDD International Conference
on Knowledge Discovery and Data Mining, pp. 1365–1374. ACM, 2015.
Yosinski, J., Clune, J., Bengio, Y., and Lipson, H. How transferable are features in deep neural networks? In Advances in
Neural Information Processing Systems 27, pp. 3320–3328, 2014.
Zhang, M., Cui, Z., Neumann, M., and Chen, Y. An end-to-end deep learning architecture for graph classiﬁcation. In AAAI
Conference on Artiﬁcial Intelligence, pp. 4438–4445, 2018.
Zou, D. and Lerman, G. Graph convolutional neural networks via scattering. arXiv:1804:00099, 2018.


## Page 12


Geometric Scattering for Graph Data Analysis
12
A. Detailed graph classiﬁcation comparison
Table 2. Comparison of the proposed graph scattering classiﬁer (GSC) with graph kernel methods and deep learning methods on
biochemistry & social graph datasets. (Remark1: DCNN using different training/test split)
NCI1
NCI109
D&D
PROTEINS
MUTAG
PTC
ENZYMES
WL
84.46 ± 0.45
85.12 ± 0.29
78.34 ± 0.62
72.92 ± 0.56
84.11 ± 1.91
59.97 ± 1.60
55.22 ± 1.26
Graph kernel
z
}|
{
PK
82.54 ± 0.47
N/A
78.25 ± 0.51
73.68 ± 0.68
76.00 ± 2.69
59.50 ± 2.44
N/A
Graphlet
70.5 ± 0.2
69.3 ± 0.2
79.7 ± 0.7
72.7 ± 0.6
85.2 ± 0.9
54.7 ± 2.0
30.6 ± 1.2
WL-OA
86.1 ± 0.2
86.3 ± 0.2
79.2 ± 0.4
76.4 ± 0.4
84.5 ± 1.7
63.6 ± 1.5
59.9 ± 1.1
GK
62.28 ± 0.29
62.60 ± 0.19
78.45 ± 0.26
71.67 ± 0.55
81.39 ± 1.74
57.26 ± 1.41
26.61 ± 0.99
DGK
80.3 ± 0.4
80.3 ± 0.3
73.09 ± 0.25
75.7 ± 0.50
87.4 ± 2.7
60.1 ± 2.5
53.4 ± 0.9
DGCNN
74.44 ± 0.47
N/A
79.37 ± 0.94
75.54 ± 0.94
85.83 ± 1.66
58.59 ± 2.47
51.00 ± 7.29
Deep learning
z
}|
{
graph2vec
73.22 ± 1.81
74.26 ± 1.47
N/A
73.30 ± 2.05
83.15 ± 9.25
60.17 ± 6.86
N/A
2D CNN
N/A
N/A
N/A
77.12 ± 2.79
N/A
N/A
N/A
CCN
76.27 ± 4.13
75.54 ± 3.36
N/A
N/A
91.64 ± 7.24
70.62 ± 7.04
N/A
PSCN (k = 10)
76.34 ± 1.68
N/A
76.27 ± 2.15
75.00 ± 2.51
88.95 ± 4.37
62.29 ± 5.68
N/A
DCNN
56.61 ± 1.04
57.47 ± 1.22
58.09 ± 0.53
61.29 ± 1.60
56.60 ± 2.89
561
42.44 ± 1.76
GCAPS-CNN
82.72 ± 2.38
81.12 ± 1.28
77.62 ± 4.99
76.40 ± 4.17
N/A
66.01 ± 5.91
61.83 ± 5.39
S2S-P2P-NN
83.72 ± 0.4
83.64 ± 0.3
N/A
76.61 ± 0.5
89.86 ± 1.1
64.54 ± 1.1
63.96 ± 0.6
GIN-0 (MLP-SUM)
82.70 ± 1.60
N/A
N/A
76.20 ± 2.80
89.40 ± 5.60
64.60 ± 7.00
N/A
GS-SVM
79.14 ± 1.28
77.95 ± 1.25
75.04 ± 3.64
74.11 ± 4.02
83.57 ± 6.75
63.94 ± 7.38
56.83 ± 4.97
COLLAB
IMDB-B
IMDB-M
REDDIT-B
REDDIT-5K
REDDIT-12K
WL
77.82 ± 1.45
71.60 ± 5.16
N/A
78.52 ± 2.01
50.77 ± 2.02
34.57 ± 1.32
Graph kernel
z
}|
{
PK
N/A
N/A
N/A
N/A
N/A
N/A
Graphlet
73.42 ± 2.43
65.4 ± 5.95
N/A
77.26 ± 2.34
39.75 ± 1.36
25.98 ± 1.29
WL-OA
80.7 ± 0.1
N/A
N/A
89.3 ± 0.3
N/A
N/A
GK
72.84 ± 0.28
65.87 ± 0.98
43.89 ± 0.38
77.34 ± 0.18
41.01 ± 0.17
N/A
DGK
73.0 ± 0.2
66.9 ± 0.5
44.5 ± 0.5
78.0 ± 0.3
41.2 ± 0.1
32.2 ± 0.1
DGCNN
73.76 ± 0.49
70.03 ± 0.86
47.83 ± 0.85
N/A
48.70 ± 4.54
N/A
Deep learning
z
}|
{
graph2vec
N/A
N/A
N/A
N/A
N/A
N/A
2D CNN
71.33 ± 1.96
70.40 ± 3.85
N/A
89.12 ± 1.7
52.21 ± 2.44
48.13 ± 1.47
CCN
N/A
N/A
N/A
N/A
N/A
N/A
PSCN (k = 10)
72.60 ± 2.15
71.00 ± 2.29
45.23 ± 2.84
86.30 ± 1.58
49.10 ± 0.7
41.32 ± 0.42
DCNN
52.11 ± 0.71
49.06 ± 1.37
33.49 ± 1.42
N/A
N/A
N/A
GCAPS-CNN
77.71 ± 2.51
71.69 ± 3.40
48.50 ± 4.1
87.61 ± 2.51
50.10 ± 1.72
N/A
S2S-P2P-NN
81.75 ± 0.8
73.8 ± 0.7
51.19 ± 0.5
86.50 ± 0.8
52.28 ± 0.5
42.47 ± 0.1
GIN-0 (MLP-SUM)
80.20 ± 1.90
75.10 ± 5.10
52.30 ± 2.80
92.40 ± 2.50
57.50 ± 1.50
N/A
GS-SVM
79.94 ± 1.61
71.20 ± 3.25
48.73 ± 2.32
89.65 ± 1.94
53.33 ± 1.37
45.23 ± 1.25
All results come from the respective papers that introduced the methods, with the exception of: (1) social network results of WL,
from Tixier et al. (2017); (2) biochemistry and social results of DCNN, from Verma & Zhang (2018); (3) biochemistry, except for D&D,
and social result of GK, from Yanardag & Vishwanathan (2015); (4) D&D of GK is from Niepert et al. (2016); and (5) for Graphlets,
biochemistry results from Kriege et al. (2016), social results from Tixier et al. (2017).


## Page 13


Geometric Scattering for Graph Data Analysis
13
B. Detailed tables for scattering feature space analysis from Section 4
Table 3. Classiﬁcation accuracy with different training/validaion/test splits over scattering features (unnorm. moments)
Dataset
SVM accuracy
80%/10%/10%
70%/10%/20%
40%/10%/50%
20%/10%/70%
NCI1
79.80 ± 2.24
78.13 ± 2.07
76.37 ± 0.27
73.60 ± 0.68
NCI109
77.66 ± 1.78
77.54 ± 1.44
74.41 ± 0.14
72.36 ± 0.74
D&D
76.57 ± 3.76
76.74 ± 2.32
76.32 ± 0.59
75.58 ± 0.81
PROTEINS
74.03 ± 4.20
74.30 ± 2.49
73.32 ± 1.68
73.01 ± 1.94
MUTAG
84.04 ± 6.71
82.99 ± 6.97
78.72 ± 3.19
77.47 ± 4.41
PTC
66.32 ± 7.54
64.83 ± 2.13
61.92 ± 1.45
56.75 ± 2.88
ENZYMES
53.83 ± 6.71
52.50 ± 5.35
44.50 ± 3.83
36.38 ± 1.93
COLLAB
76.88 ± 1.13
76.98 ± 0.97
76.42 ± 0.82
74.63 ± 1.05
IMDB-B
70.80 ± 3.54
70.60 ± 2.85
69.10 ± 1.90
67.81 ± 0.98
IMDB-M
48.93 ± 4.77
49.00 ± 1.97
47.20 ± 1.47
44.28 ± 1.87
REDDIT-B
88.30 ± 2.08
88.75 ± 0.96
86.40 ± 0.40
86.18 ± 0.32
REDDIT-5K
50.71 ± 2.27
50.87 ± 1.37
50.10 ± 0.41
48.37 ± 0.76
REDDIT-12K
41.35 ± 1.05
41.05 ± 0.70
39.36 ± 1.30
37.71 ± 0.42
Table 4. Classiﬁcation accuracy and dimensionality reduction with PCA over scattering features (unnorm. moments)
Dataset
SVM accuracy w.r.t variance covered
PCA dimensions w.r.t variance covered
50%
80%
90%
99%
50%
80%
90%
99%
NCI1
72.41 ± 2.36
73.89 ± 2.57
73.89 ± 1.33
78.22 ± 1.95
18
32
43
117
NCI109
70.85 ± 2.59
71.84 ± 2.38
72.33 ± 2.24
76.69 ± 1.02
19
32
43
114
D&D
75.21 ± 3.17
75.13 ± 3.68
74.87 ± 3.99
76.92 ± 3.37
10
35
44
122
PROTEINS
70.80 ± 3.43
74.20 ± 3.06
74.67 ± 3.33
74.57 ± 3.42
2
5
10
36
MUTAG
77.51 ± 10.42
80.32 ± 8.16
82.40 ± 10.92
84.09 ± 9.09
4
8
13
34
PTC
58.17 ± 8.91
60.50 ± 9.96
58.70 ± 6.93
63.68 ± 3.97
7
14
21
62
ENZYMES
29.67 ± 4.46
45.33 ± 6.62
50.67 ± 5.44
52.50 ± 8.89
3
9
16
44
COLLAB
62.86 ± 1.36
71.68 ± 2.06
73.22 ± 2.29
76.54 ± 1.41
2
6
9
32
IMDB-B
58.30 ± 3.44
66.10 ± 3.14
68.80 ± 4.31
68.40 ± 4.31
2
4
8
24
IMDB-M
41.00 ± 4.86
46.40 ± 4.48
45.93 ± 3.86
48.27 ± 3.23
2
5
8
20
REDDIT-B
71.05 ± 2.39
78.95 ± 2.42
83.75 ± 1.83
86.95 ± 1.78
2
5
8
24
REDDIT-5K
40.97 ± 2.06
45.71 ± 2.21
47.43 ± 1.90
49.65 ± 1.86
2
6
10
27
REDDIT-12K
28.22 ± 1.64
33.36 ± 0.93
34.71 ± 1.52
38.39 ± 1.54
2
5
9
27
Table 5. Dimensionality reduction with PCA over scattering features (unnorm. moments)
Dataset
SVM accuracy
PCA dimensions (> 90% variance)
PCA
Full
All classes
Per class
ENZYMES
50.67 ± 5.44
53.83 ± 6.71
16
9
8
8
9
10
6


## Page 14


Geometric Scattering for Graph Data Analysis
14
Table 6. EC subspace analysis in scattering feature space of ENZYMES (Borgwardt et al., 2005a)
Enzyme
Class:
Mean distance to subspace of class
True class as
EC-1
EC-2
EC-3
EC-4
EC-5
EC-6
1st
2nd
3rd-6th
measured via PCA projection/reconstruction distance
nearest subspace
EC-1
18.15
98.44
75.47
62.87
53.07
84.86
45%
28%
27%
EC-2
22.65
9.43
30.14
22.66
18.45
22.75
53%
24%
23%
EC-3
107.23
252.31
30.4
144.08
117.24
168.56
32%
7%
61%
EC-4
117.68
127.27
122.3
29.59
94.3
49.14
24%
12%
64%
EC-5
45.46
66.57
60
50.07
15.09
58.22
67%
21%
12%
EC-6
62.38
58.88
73.96
51.94
59.23
13.56
67%
21%
12%
C. Detailed Dataset Descriptions
The details of the datasets used in this work are as follows:
NCI1 (Wale et al., 2008) contains 4,110 chemical compounds as graphs, with 37 node features. Each compound is labeled according to
is activity against non-small cell lung cancer and ovarian cancer cell lines, and these labels serve as classiﬁcation goal on this data.
NCI109 (Wale et al., 2008) is similar to NCI1, but with 4,127 chemical compounds and 38 node features.
MUTAG (Debnath et al., 1991) consists of 188 mutagenic aromatic and heteroaromatic nitro compounds (as graphs) with 7 node features.
The classiﬁcation here is binary (i.e., two classes), based on whether or not a compound has a mutagenic effect on bacterium.
PTC (Toivonen et al., 2003) is a dataset of 344 chemical compounds (as graphs) with nineteen node features that are divided into two
classes depending on whether they are carcinogenic in rats.
PROTEINS (Borgwardt et al., 2005b) dataset contains 1,113 proteins (as graphs) with three node features, where the goal of the
classiﬁcation is to predict whether the protein is enzyme or not.
D&D (Dobson & Doig, 2003) dataset contains 1,178 protein structures (as graphs) that, similar to the previous one, are classiﬁed as
enzymes or non-enzymes.
ENZYMES (Borgwardt et al., 2005b) is a dataset of 600 protein structures (as graphs) with three node features. These proteins are
divided into six classes of enzymes (labelled by enzyme commission numbers) for classiﬁcation.
COLLAB (Yanardag & Vishwanathan, 2015) is a scientiﬁc collaboration dataset contains 5K graphs. The classiﬁcation goal here is to
predict whether the graph belongs to a subﬁeld of Physics.
IMDB-B (Yanardag & Vishwanathan, 2015) is a movie collaboration dataset with contains 1K graphs. The graphs are generated on two
genres: Action and Romance, the classiﬁcation goal is to predict the correct genre for each graph.
IMDB-M (Yanardag & Vishwanathan, 2015) is similar to IMDB-B, but with 1.5K graphs & 3 genres: Comedy, Romance, and Sci-Fi.
REDDIT-B (Yanardag & Vishwanathan, 2015) is a dataset with 2K graphs, where each graph corresponds to an online discussion thread.
The classiﬁcation goal is to predict whether the graph belongs to a Q&A-based community or discussion-based community.
REDDIT-5K (Yanardag & Vishwanathan, 2015) consists of 5K threads (as graphs) from ﬁve different subreddits. The classiﬁcation goal
is to predict the corresponding subreddit for each thread.
REDDIT-12K (Yanardag & Vishwanathan, 2015) is similar to REDDIT-5k, but with 11,929 graphs from 12 different subreddits.
Table 7 summarizes the size of available graph data (i.e., number of graphs, and both max & mean number of vertices within graphs) in
these datasets, as previously reported in the literature.
Graph signals for social network data:
None of the social network datasets has ready-to-use node features. Therefore, in the
case of COLLAB, IMDB-B, and IMDB-M, we use the eccentricity, degree, and clustering coefﬁcients for each vertex as characteristic
graph signals. In the case of REDDIT-B, REDDIT-5K and REDDIT-12K, on the other hand, we only use degree and clustering coefﬁcient,
due to presence of disconnected graphs in these datasets.


## Page 15


Geometric Scattering for Graph Data Analysis
15
Table 7. Basic statistics of the graph classiﬁcation databases
NCI1
NCI109
MUTAG
D&D
PTC
PROTEINS
# of graphs in data:
4110
4127
188
1178
344
1113
Max # of vertices:
111
111
28
5748
109
620
Mean # of vertices:
29.8
29.6
17.93
284.32
25.56
39.0
# of features per vertex:
37
38
7
89
22
3
Mean # of edges:
64.6
62.2
39.50
1431.3
51.90
72.82
# of classes:
2
2
2
2
2
2
ENZYMES
COLLAB
IMDB
REDDIT
B
M
B
5K
12K
600
5000
1000
1500
2000
5000
11929
126
492
136
89
3783
3783
3782
32.6
74.49
19.77
13
429.61
508.5
391.4
3
3
3
3
2
2
2
124.2
2457.78
96.53
65.94
497.75
594.87
456.89
6
3
2
3
2
5
11
D. Technical Details
The computation of the scattering features is based on several design choices, akin to typical architecture choices in neural networks. Most
importantly, it requires a choice of 1. which statistical moments to use (normalized or unnormalized), 2. the number of wavelet scales to
use (given by J), and 3. the number of moments to use (denoted by Q). In general, J can be automatically tuned by the diameter of the
considered graphs (e.g., setting it to the logarithm of the diameter), and the other choices can be tuned via cross-validation. However, we
have found the impact of such tuning to be minor, and thus for simplicity, we ﬁx our conﬁguration to use normalized moments, J = 5,
and Q = 4 throughout this work.
Cross validation procedure:
Classiﬁcation evaluation was done with standard ten-fold cross validation procedure. First, the entire
dataset is randomly split into ten subsets. Then, in each iteration (or “fold”), nine of them are used as training and validation, and the other
one is used for testing classiﬁcation accuracy. In total, after ten iterations, each of the subsets has been used once for testing, resulting in
ten reported classiﬁcation accuracy numbers for the examined dataset. Finally, the mean and standard deviation of these ten accuracies are
computed and reported.
It should be noted that during training, each iteration also performs automatic tuning of the trained classiﬁer, as follows. First, nine
iterations are performed, each time using eight subsets (i.e., folds) as training and the remaining one as validation set, which is used to
determine the optimal parameters for SVM. After nine iterations, each of the training/validation subsets has been used once for validation,
and we obtain nine classiﬁcation models, which in turn produce nine predictions (i.e., class assignments) for each data point in the test
subset of the main cross validation. To obtain the ﬁnal predicted class of this cross validation iteration, we select the class with the most
votes (from among the nine models) as our ﬁnal classiﬁcation result. These results are then compared to the true labels (in the test set) on
the test subset to obtain classiﬁcation accuracy for this fold.
Software & hardware environment:
Geometric scattering and related classiﬁcation code were implemented in Python. All
experiments were performed on HPC environment using an intel16-k80 cluster, with a job requesting one node with four processors and
two Nvidia Tesla k80 GPUs.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1810_03068v2_geometric_scattering_for_graph_data_analysis
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1810_03068V2_GEOMETRIC_SCATTERING_FOR_GRAPH_DATA_ANALYSIS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
