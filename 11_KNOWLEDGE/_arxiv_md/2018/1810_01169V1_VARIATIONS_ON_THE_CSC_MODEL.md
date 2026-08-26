---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1810.01169v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1810.01169v1_Variations_on_the_CSC_model

> Source: 1810.01169v1_Variations_on_the_CSC_model.pdf

> Pages: 10

---


## Page 1


1
Variations on the CSC model
Ives Rey-Otero, Jeremias Sulam, Michael Elad
Abstract—Over the past decade, the celebrated sparse repre-
sentation model has achieved impressive results in various signal
and image processing tasks. A convolutional version of this model,
termed convolutional sparse coding (CSC), has been recently
reintroduced and extensively studied. CSC brings a natural
remedy to the limitation of typical sparse enforcing approaches
of handling global and high-dimensional signals by local, patch-
based, processing. While the classic ﬁeld of sparse representations
has been able to cater for the diverse challenges of different
signal processing tasks by considering a wide range of problem
formulations, almost all available algorithms that deploy the CSC
model consider the same ℓ1 −ℓ2 problem form. As we argue in
this paper, this CSC pursuit formulation is also too restrictive as
it fails to explicitly exploit some local characteristics of the signal.
This work expands the range of formulations for the CSC model
by proposing two convex alternatives that merge global norms
with local penalties and constraints. The main contribution of
this work is the derivation of efﬁcient and provably converging
algorithms to solve these new sparse coding formulations.
Index Terms—sparse representation, convolutional sparse cod-
ing, parallel proximal algorithm, convex optimization.
I. INTRODUCTION
The sparse representation model [1] is a central tool for
a wide range of inverse problems in image processing, such
as denoising [2], [3], super-resolution [4], [5], image deblur-
ring [6], [7] and more. This model assumes that natural signals
can be represented as a sparse linear combination of a few
columns, called atoms, taken from a matrix called dictionary.
The problem of recovering the sparse decomposition of a
given signal over a (typically overcomplete) dictionary is
called sparse coding or pursuit. Such an inverse problem is
usually formulated as an optimization objective seeking to
minimize the ℓ0 pseudo-norm, or its convex relaxation, the
ℓ1-norm, while allowing for a good1 signal reconstruction. An
effective deployment of the sparse representation model calls
for the identiﬁcation of a dictionary that suites the data treated.
This is known as the dictionary learning problem, of ﬁnding
the best sparsifying dictionary that ﬁts a large set of signal
examples [8], [9].
Alas, when it comes to the need to process global high-
dimensional signals (e.g., complete images), the sparse rep-
resentation model hits strong barriers. Dictionary learning
is completely intractable in such cases due to its too high
memory and computational requirements. In addition, the
global pursuit fails to grasp local varying behaviors in the
signal, thus leading to inferior treatment of the overall data.
Because of these reasons, it has become a common practice
to split the global signal into small overlapping blocks, or
All authors are with the Computer Science Department, Technion - Israel
Institute of Technology
1The desired representation accuracy, or ﬁtting, is problem dependent and
it varies for different applications.
patches, identify the dictionary that best models these patches,
and then sparse code and reconstruct each of these blocks
independently before averaging them back into a global sig-
nal [2]. Although practical and effective [10], this patch-
based strategy is inherently limited since it does not account
for the natural dependencies that exist between adjacent or
overlapping patches, and therefore it cannot ensure a coherent
reconstruction of the global signal [11], [12].
This limitation of the patch-based strategy has been tackled
in two ways. One way maintains the patch-based strategy
while extending it by modifying the objective so as to bridge
the gap between local prior and global reconstruction. This
is achieved either by taking into account the self-similarities
of natural images [7], [3], by exploiting their multi-scale
nature [12], [13], [14], or by explicitly requiring the recon-
structed global signal to be consistent with the local prior [15],
[11]. The second way consists in dropping the heuristic patch-
based strategy altogether in favor of global, yet computation-
ally tractable and locally-aware, models. Such is the case of
the CSC [16], [17], [18], allowing the pursuit to be performed
directly on the global signal by imposing a speciﬁc banded
convolutional structure on the global dictionary. This implies,
naturally, that the signal of interest is a superposition of a few
local atoms shifted to different positions. And so, while the
CSC is a global model, it has patch-based ﬂavor to it and in
addition, learning its dictionary is within reach [19].
Recent years have seen a renewed interest in the CSC
model, including a thorough theoretical analysis along with
new pursuit and dictionary learning algorithms for it, and
its deployment to problems such as image inpainting, super-
resolution, dynamic range imaging, and pattern classiﬁca-
tion [19], [20], [21], [22], [23], [24], [25]. Nevertheless, the
research activity on the CSC model is still in its infancy.
In particular, while the classic sparse representation model
has assembled an extensive toolbox of problem formulations,
diverse sparsity promoting penalty functions along with count-
less pursuit algorithms (with greedy, relaxation and Bayesian
alternatives), most pursuit approaches to recover the CSC
representation Γ from a global signal X and a convolutional
dictionary D rely on minimizing the same ℓ2 −ℓ1 objective,
namely
minimize
Γ
1
2∥X −DΓ∥2
2 + λ∥Γ∥1,
(1)
where λ is a Lagrangian parameter. As we show in this work,
this problem formulation is too restrictive and dull. Indeed,
both terms in this formulation, the ℓ2 reconstruction term and
the ℓ1 sparsity promoting penalty, are global quantities - as is
the scalar Lagrangian parameter λ that controls the trade-off
between them. This contrasts with state-of-the-art patch-based
methods where sparsity is controlled locally, typically through
a per-patch constraint on the maximum number of non-zeros or
arXiv:1810.01169v1  [eess.SP]  2 Oct 2018


## Page 2


2
on the maximal allowed patch error [2]. While one would hope
for the CSC pursuit to optimally scatter non-zero coefﬁcients
in a way that best serves the signal, we unfortunately observe
that this not to be the case in practice. Instead, solutions to
the above problem typically exhibit sparsity patterns that have
little relation with the signal local complexity. This calls for
alternative problem formulations where local sparsity and local
representation errors are explicitly taken into account in the
global model.
An additional motivation for an alternative formulation of
the CSC pursuit stems from the ﬁndings of [26], which is the
ﬁrst work to derive a theoretical analysis framework for the
CSC model. In order to leverage the convolutional structure
in this pursuit problem, the authors in [26] advocate for
a new notion of local sparsity. In particular, they provide
recovery and stability guarantees conditioned on the sparsity of
each representation portion responsible for encoding individual
patches, as opposed to the traditional global ℓ0 norm. The
CSC pursuit formulations proposed in the present work aim
at explicitly controlling the sparsity level in these portions of
the representation vectors, called stripes. The ﬁrst formulation
employs the ℓ1,∞norm as the sparsity promoting function,
providing a convex relaxation of the ℓ0,∞pseudo-norm that
was introduced in [26] and explored further in [27], [28].
The second formulation controls the sparsity of the stripes
by considering the maximum reconstruction error on each
patch simultaneously, via an ℓ2,∞norm. Such an approach
is motivated by patch averaging techniques that have been
successfully deployed for denoising and other inverse prob-
lems [2], [10]. We derive, for each of these two formulations,
simple, efﬁcient, and provably converging algorithms.
The remainder of the paper is organized as follows. Sec-
tion II reviews common notations and deﬁnitions for the
CSC model. Section III examines the behavior of the classic
ℓ2 −ℓ1, in particular its tendency to overuse simple atoms
and encode the signal by aggregation of these coarse atoms
along with a spatial instability of the global representation.
We then propose two alternate formulations, the ℓ2 −ℓ1,∞
and ℓ2,∞−ℓ1 in Section IV and Section V, respectively. Both
sections focus on the derivation of algorithms to solve the
respective formulations along with experiments to illustrate
their behavior and performance. Section VI contains a ﬁnal
discussion.
II. CONVOLUTIONAL SPARSE CODING
This work uses the terminology ﬁrst introduced in [26].
The CSC model assumes that an image can be decomposed
as X = DΓ. An image of size H × W is represented in
its vectorized form as a vector X of length N = HW and
the corresponding global convolutional dictionary D is of
size N × Nm. D is built as the concatenation of m (block-
) circulant matrices of size N × N, each representing one
convolution. These convolutions employ small support ﬁlters
of size n × n, thus causing the above-mentioned circulant
matrices to be narrowly banded. Another way to describe D
is by combining all the shifted versions of a local dictionary
Dl ∈Rn2×m composed of the m vectorized 2D ﬁlters. Such
Fig. 1.
Illustration of the CSC model for the 1D case. At the global scale,
the image X can be decomposed into the product of the global convolutional
dictionary D and a global sparse representation Γ. At the patch scale, the
patch RiX can be decomposed into the product of the stripe dictionary Ω
and the stripe representation vector SiΓ.
construction is best illustrated by expressing the global signal
in terms of the local dictionary, X = PN
i=1 RT
i Dlαi, where
RT
i is the operator that positions the patch Dlαi in the ith
location and pads the rest of the entries with zeros. The
quantity Dlαi is called a slice, with αi being the portion of
the sparse representation vector Γ, called needle, that encodes
the slice. It is important to stress that slices are not patches but
rather simpler components that are combined to form patches.
To better understand which parts of the dictionary D and
of the sparse vector Γ represent an isolated patch, it is
convenient to consider the patch extraction operator Ri and
apply it to the system of equations X = DΓ. This yields
the system RiX = RiDΓ consisting of the n2 rows relating
to the patch pixels. Due to the banded structure of D, the
extracted rows RiD contain only a subset of (2n −1)2m
columns that are not trivially zeros. Denoting by ST
i
the
operator that extracts such columns and rewriting our system
of equations as RiX = RiDST
i SiΓ make two interesting
entities come to light. The ﬁrst is the vector SiΓ, a subset
of (2n −1)2m coefﬁcients of Γ called the stripe that entirely
encodes the patch RiX. The second entity is the sub-matrix
Ω= RiDST
i
∈Rn2×(2n−1)2m, called the stripe dictionary,
which multiplies the stripe vector SiΓ to reconstruct the patch.
Figure 1 summarizes these deﬁnitions and notations, employed
in the remainder of the paper.
III. THE NEED FOR STRUCTURED SPARSITY
To illustrate the problematic behavior of the CSC model
in its most common formulation, we examine the structure
obtained in the global representation vector in the following
experiment. A natural image X is sparse coded using the
ℓ1 −ℓ2 formulation2, resulting in the decomposition DΓCSC.
The local dictionary considered, Dl, is the DCT dictionary
(n = 8, m = 64) and λ is set so as to reach a reconstruction
error of 30 dB. For comparison, fully-overlapping patches
of the same image are sparse coded individually using the
Orthogonal Matching Pursuit (OMP) with the same local
2The ℓ1 −ℓ2 minimization is carried out using the slice-based algorithm
proposed in [29].


## Page 3


3
0
5
10
15
20
0
2
4
6
·104
(a)
0
5
10
15
20
0
1
2
3 ·105
(b)
Fig. 2.
Representation test for the image barbara. Number of non-
zero coefﬁcients for each of the 20 most commonly used atoms in each
representation. (a) CSC ℓ1 −ℓ2 formulation (b) sparse coding every patch
individually via OMP. The sparsity level in both representations is set so
as to reach a reconstruction error of 30dB. In both cases, the most popular
atom is the DC component. The ℓ1 −ℓ2 CSC formulation leads to one atom
being used predominantly. Since each patch is reconstructed independently,
the patch-based reconstruction leads to a denser global representation and uses
diverse local atoms.
dictionary. The error threshold in the OMP is set so as to
achieve a representation error of 30 dB after patch-averaging,
so as to match the CSC experiment. This results in a set of
needles, one per each patch, and these can be concatenated
into a global sparse representation ΓOMP that has the same
length and structure as ΓCSC.
Figures 2 (a) and (b) depict how often the ﬁrst 20 atoms in
the local dictionary are used in ΓCSC and ΓOMP respectively.
In the CSC representation vector, one atom is predominantly
used, namely the DC atom. In fact, most of the needles in
ΓCSC contain at most only one active atom, and many of
them (about 70%) remain completely empty. Note that while
the OMP algorithm in the patch-based approach encodes the
patches using the local dictionary atoms alone, the CSC pursuit
encodes the entire image using the atoms as well as their
shifts. This allows fewer local atoms to be used in the CSC
representation. Indeed, the system of equations X = DΓ
admits an inﬁnite number of solutions even with a local
dictionary Dl containing as few as two atoms, which would be,
on the other hand, insufﬁcient to reliably reconstruct individual
patches.
What these plots show in fact is that, in the CSC model,
the juxtaposition of the simplest atoms shifted at different
locations accounts for most of its expressiveness. This ten-
dency leads to a series of problems. On one hand, this is of
importance for any dictionary learning algorithm that builds
on the ℓ1 −ℓ2 formulation, since the predominant use of one
ﬁlter prevents most atoms from being properly updated and
learned.
Another tendency of the CSC model we would like to
expose is the fact that the global representation obtained is
spatially unstable. By putting too much emphasis on the spatial
arrangement of slices, the sparse representation at one point
−1
0
1
Fig. 3.
Spatial instability of the CSC sparse representation. (a) We consider
two crops setups (in green and blue) only differing by a vertical shift of 4
pixels. We sparse code each sub-image with the convolutional dictionary based
on the DCT. (b) Sparsity difference: each pixel in the ﬁgure corresponds to
the difference between the ℓ1-norm of the needles in each representation (after
shifting back the representation by 4 pixels so as to consider the needles that
are in both representations). Note that on smooth regions, representation is
spatially sparse and follows a grid pattern. The ℓ1 −ℓ2 formulation leads to
juxtaposition of slices, whose spatial arrangement is sensitive to the smallest
distant variations of the signal.
of the image is overly affected by a distant structure in the
image – as happens, for example, with the image borders.
To demonstrate this, let us consider two image crops shifted
from one another by a few pixels. The impact of the border
location on the spatial distribution of non-zero coefﬁcients is
illustrated in Figure 3, which shows the difference between
the respective sparsity maps (with proper compensation of the
shift). Oddly, the global distribution of atoms in the image
is globally affected most noticeably in smooth regions of the
image.
Note that it is common in practice to deploy the CSC
model not directly on the image itself but rather after applying
a local mean subtraction and contrast normalization of the
signal. This has the effect of mitigating, to some extent, the
spatial instability to large distance interaction by breaking the
connections between distant structure. However, this does not
prevent the inherent tendency of the ℓ1−ℓ2 global formulation
to use too few atoms and compensating for this by aggregating
overlapping shifts. We will see that by anchoring the CSC
pursuit locally, as in the proposed alternate formulations, it is
possible to get hold of such tendency.
IV. THE ℓ2 −ℓ1,∞CSC FORMULATION
The ﬁrst alternate formulation that we explore drops the
global ℓ1 as a sparsity promoting penalty and uses instead a
mixed norm function, adding an explicit and local control of
sparsity. This is motivated by the work in [26], whose analysis
centers around a new notion of local sparsity, the ℓ0,∞. This
measure, instead of quantifying the total number of non-zeros
in a vector, reports the ℓ0 norm of the densest stripe:
∥Γ∥0,∞= max
i
∥SiΓ∥0.
(2)
Such a localized norm is a somewhat more appropriate mea-
sure of sparsity in the convolutional setting, since with it one


## Page 4


4
is able to signiﬁcantly improve on the theoretical guarantees
for the CSC model [26]. Although that work established that
the ℓ2 −ℓ1 formulation approximates the solution to an ℓ0,∞
problem, it also conjectured that further improvement could be
achieved by considering a new ℓ1,∞-norm. This norm, deﬁned
as ∥Γ∥1,∞= maxi ∥SiΓ∥1, will be the center of our current
discussion: the ℓ2 −ℓ1,∞formulation,
min
Γ
1
2∥X −DΓ∥2
2 + λ∥Γ∥1,∞.
(3)
The ℓ1,∞is nothing but a mixed norm on the global repre-
sentation Γ. Mixed-norms have been commonly used in signal
processing to promote various types of structure in the sparsity
pattern [30]. In the context of the CSC model, using this
mixed norm is expected to promote a distribution of non-zero
coefﬁcients that makes use of more diverse local atoms and is
less affected by the global attributes of the image.
This formulation, in fact, ﬁrst appeared in the work of [28],
which proposed a global ADMM formulation to iteratively
minimize the loss in Equation (3). Unfortunately, one of the
steps in their proposed iterative process requires of yet another
ADMM solver, resulting in a generally inefﬁcient algorithm.
The complexity of this approach is aggravated by the need of a
multi-block ADMM, which requires careful parameter tuning
and does not enjoy the convergence properties of the standard
ADMM.
A. The proposed algorithm
Recalling the ℓ2−ℓ1,∞formulation in Equation (3), consider
N splitting variables {γi}N
i=1, so as to rewrite the problem
equivalently as
minimize
Γ,{γi}
1
2∥Y −DΓ∥2
2 + λ max
i
∥γi∥1
subject to
∀i, γi = SiΓ.
(4)
This constrained minimization problem is handled by consid-
ering its augmented Lagrangian:
minimize
Γ,{γi},{ui},
1
2∥Y −DΓ∥2
2 + λ max
i
∥γi∥1
+ ρ
2
X
i
∥γi −SiΓ + ui∥2
2,
(5)
where {ui}N
i=1 denote the scaled dual-variables associated
with each equality constraint γi = SiΓ. The ADMM algo-
rithm [31] minimizes this augmented Lagrangian by alterna-
tively updating the variable Γ and the set of splitting variables
{γi}N
i=1. Formally, an iteration of the ADMM algorithm
consists of the following steps:
Γ(k) := arg min
Γ
1
2∥Y −DΓ∥2
2
+ρ
2
X
i
∥γ(k−1)
i
−SiΓ + u(k−1)
i
∥2
2.
(6)
{γ(k)
i
} := arg min
{γi}
λ max
i
∥γi∥1
+ρ
2
X
i
∥γi −SiΓ(k) + u(k−1)
i
∥2
2.
(7)
u(k)
i
:=
u(k−1)
i
+ γ(k)
i
−SiΓ(k).
(8)
The update of Γ in Equation (6) is straightforward, as it is a
least-square minimization that boils down to solving the linear
system of equations
 
DT D + ρ
X
i
ST
i Si
!
Γ = DT Y
+ ρ
X
i
ST
i (γi + ui).
(9)
Bearing in mind that fast (possibly GPU) implementations are
available for the convolution DT and the transpose convo-
lution D, and using the fact that P
i ST
i Si = (2n −1)2I,
this regularized least-square minimization can be carried out
efﬁciently and reliably via a few iterations of the conjugate
gradient method [32].
The updates of the variables {γi}N
i=1 in Equation (7) are
seemingly more complicated, due to the max operation be-
tween the different stripes and the fact that they overlap. To
make it more manageable, we cast the Problem (7) in epigraph
form as
minimize
{γi},t
λt + ρ
2
X
i
∥γi −SiΓ(k+1) + u(k)
i
∥2
2,
subject to
∀i,
∥γi∥1 ≤t.
(10)
Here, the initial problem with variables {γi}N
i=1 has just
been replaced with an equivalent minimization over variables
{γi}N
i=1 and t. Note that, for a ﬁxed value of variable t,
this new objective in Equation (10) is now separable in the
variables {γi}N
i=1. More precisely, it can be broken down into
N separate minimization problems
¯γi(t) := arg min
γi
∥γi −SiΓ(k) + u(k−1)
i
∥2
2,
subject to
∥γi∥1 ≤t.
(11)
Each of these is simply a projection onto the ℓ1-ball [33] that
can be performed via the shrinkage operator3:
¯γi(t) = Sλ∗

SiΓ(k) −u(k−1)
i

,
(12)
where the shrinkage parameter λ∗can be efﬁciently estimated
by sorting the vector’s coefﬁcients and computing over them
a cumulative sum (see [33] for details).
In this way, solving the initial problem (7) boils down to
ﬁnding the optimal t leading to the minimum of the objective,
namely {γ(k)
i
}N
i=1 = {γi(t∗)}N
i=1 with
t∗:= arg min
t
 
λt +
X
i
∥¯γi(t) −SiΓ(k) + u(k−1)
i
∥2
2
!
.
(13)
As a sum of an afﬁne function and squared distances to the
ℓ1 ball of radius t, the previous objective is a convex function
of t. Indeed, the distance to the ℓ1 ball is a convex function
of the radius t (see Proposition 1 in Appendix A). and it can
therefore be minimized efﬁciently via a simple binary-search.
This simple algorithm, by not involving an over-sensitive
Lagrange multiplier setting, and by enjoying the convergence
properties of the standard ADMM compares favorably with
the method described in [28].
3 Sλ(x) denotes the shrinkage operator, formally Sλ(x) = sign(x) ⊙
max (|x| −λ, 0) , with ⊙denoting the element-wise product.


## Page 5


5
cat
pineapple
ℓ2 −ℓ1
ℓ2 −ℓ1,∞
ℓ2 −ℓ1
ℓ2 −ℓ1,∞
Fig. 4.
Noiseless texture-cartoon separation. Comparing the ℓ2 −ℓ1,∞and
ℓ2 −ℓ1 formulations. The input images consist of the test image cat and
pineapple.
B. Experiments
We illustrate the ℓ2 −ℓ1,∞formulation on the texture-
cartoon separation task. This problem consists in decomposing
an input image X into a piecewise smooth component (car-
toon) Xc and a texture component Xt such that X = Xc+Xt.
The typical prior for the cartoon component Xc is based on
the total variation norm, denoted ∥Xc∥TV, which penalizes
oscillations. In addition, we propose to assume that the texture
component Xt admits a decomposition Xt = DtΓ where Dt is
a convolutional texture dictionary and Γ is the solution of the
ℓ2 −ℓ1,∞CSC formulation. Under these assumptions, the task
of texture and cartoon separation boils down to a minimization
problem over three variables: the cartoon component Xc, the
CSC representation Γ and a convolutional texture dictionary
Dt, namely
minimize
Γ,Dt,Xc
1
2∥X −DtΓ −Xc∥2
2 + λ∥Γ∥1,∞+ ζ∥Xc∥TV, (14)
with parameter ζ controling the level of TV regularization
penalizing oscillations in Xc. Such minimization is carried out
iteratively in a block-coordinated manner until convergence.
Each iteration consists of the three following steps:
X(k+1)
c
:= arg min
Xc
1
2∥X −D(k)
t
Γ(k) −Xc∥2
2
+ ζ∥Xc∥TV
(15)
Γ(k+1) := arg min
Γ
1
2∥X −D(k)
t
Γ −X(k+1)
c
∥2
2
+ λ∥Γ∥1,∞
(16)
D(k+1)
t
:= arg min
Dt
1
2∥X −DtΓ(k+1) −X(k+1)
c
∥2
2.
(17)
A TV denoiser4 is used to solve Problem (15) while Prob-
lem (16) relies on our ℓ2 −ℓ1,∞solver. For the dictionary
update, one option is to use a standard patch-based dictionary
learning such as K-SVD using overlapping patches as training
sets and the needles of the current Γ estimate. However this
would not be consistent with the CSC model. Indeed, the
patch would then be assumed to stem from the local dictionary
alone, disregarding all the contributions of shifted atoms to its
reconstruction. We adopt instead a more coherent alternative
that was recently proposed in [27] in which standard dictionary
update procedures are adapted to a convolutional setting and
carried out via conjugate gradient descent [32] in conjunction
with fast convolution computations. The proposed method is
applied to the test images cat and pineapple, the results
of our method are shown in Figure 4 along with the results
from the ℓ1 −ℓ2 based method in [29]
V. THE ℓ2,∞−ℓ1 CSC FORMULATION
We move on to consider our second formulation, of ex-
plicitly incorporating a local control on the CSC model. This
is inspired by the patch-based strategy for image denoising
and other inverse problems. Recall that patch-based sparse
denoising methods [2], [10] control the sparsity level on each
patch by upper-bounding the patch reconstruction error. We
will borrow such an idea, and translate it into the convolutional
setting.
For a noisy image Y , patch methods rely on a global
objective of the form
minimize
{αi},X
λ
2 ∥X −Y ∥2
2 +
X
i
∥βi∥0
subject to
∀i, ∥Dlβi −RiX∥2
2 ≤T,
(18)
where βi is the sparse vector for the patch RiX and the
upper-bound T over the patch reconstruction error is typically
4The TV denoiser used here is the publicly available implementation
of [34].


## Page 6


6
set to Cn2σ2
noise, the assumed patch noise level (up to a
multiplicative constant). This is typically solved via a block-
coordinate descent algorithm, which means ﬁrst initializing
X = Y and seeking the sparsest αi for each patch via the set
of local problems
minimize
βi
∥βi∥0
subject to
∥Dlβi −RiY ∥2
2 ≤T,
(19)
which yields a reconstruction for each overlapping patch and,
in turn, an intermediary global reconstruction
1
n2
P
i RT
i DLβi.
While state-of-the-art methods typically consider approximate
solutions through greedy pursuit algorithms, it is also possible
to consider an ℓ1 relaxation of the same sparse coding problem.
We will employ the latter option in order to beneﬁt from the
resulting convexity of the problem.
The second stage of the block-coordinate descent algorithm
consists in updating the estimate of X, the restored image, by
solving the least-square problem in closed form [2] according
to:
X =

λI +
X
RT
i Ri
−1
 
λY +
X
i
RT
i DLβi
!
,
(20)
essentially averaging the input signal Y
with the patch-
averaging estimate
1
n2
P
i RT
i DLβi.
In order to bring this classic approach into a convolutional
setting, note that the CSC global representation Γ can be
decomposed into its constituent needles, and so P
i ∥αi∥1 =
∥Γ∥1. Recalling the deﬁnitions and notations in Section II, a
patch from the reconstructed image RiX in the CSC model
can be equivalently written as RiX = RiDΓ = ΩSiΓ.
With these elements, the problem in (18) can be naturally
transformed into
minimize
{αi},X
λ
2 ∥X −Y ∥2
2 + ∥Γ∥1
subject to
∀i, ∥ΩSiΓ −RiX∥2
2 ≤T.
(21)
One might indeed adopt a similar block-coordinate descent
strategy for this problem as well. After an initialization of X =
Y , the ﬁrst step considers the resulting ℓ2,∞−ℓ1 formulation:
minimize
Γ
∥Γ∥1
subject to
∀i, ∥ΩSiΓ −RiY ∥2
2 ≤T,
(22)
where the constraint on patch reconstruction considers the
stripe dictionary. Again, the second stage consists in updating
the estimate of X by solving the least-square problem
X =
 
λI +
X
i
RT
i Ri
!−1  
λY +
X
i
RT
i ΩSiΓ
!
.
(23)
whose solution, since P
i RT
i ΩSiΓ
=
n2DΓ and since
P
i RT
i Ri = n2I, boils down to an average between the
input image and the intermediary global reconstruction DΓ.
In this manner, and similarly to the patch-averaging strategy,
the trade-off between sparsity and reconstruction is controlled
locally via an upper-bound on the reconstruction error of
each individual patch. However, while in the original method
each vector βi encodes one patch in disregard with other
patches, now each needle αi becomes part of various stripes
SiΓ and therefore contributes in various patches. In other
words, the classic patch-averaging approach performs these
pursuit independently, whereas this convolutional counterpart
will need to update all needles jointly.
In what follows, we show that this seemingly complex
problem can in fact be addressed by using traditional ℓ1 solvers
such as the Fast Iterative Shrinkage-Tresholding Algorithm
(FISTA) [35] in conjunction with the Parallel Proximal Al-
gorithm (PPXA).
A. Proposed algorithm
PPXA is a generic convex optimization algorithm intro-
duced by Combettes and Pesquet [36], [37] that extends
the Douglas-Rachford algorithm and aims to minimize an
objective of the form
minimize
x
N
X
i
fi(x),
(24)
where each fi is a convex function that admits an easy-to-
compute proximal operator [38], [39]. Recall that the proxim-
ity operator proxfi(y) : RN →RN of fi is deﬁned by
proxfi(y) := arg min
x
fi(x) + 1/2∥x −y∥2
2.
(25)
In our context, PPXA offers a way to manage the explicit
use of overlapping stripes. Indeed, by encapsulating each
inequality constraint into its corresponding indicator function,
the objective in Equation (22) can be recast as a sum, namely
minimize
Γ
N
X
i=1
 1
N ∥Γ∥1 + I{∥ΩSiΓ−RiY ∥2
2≤T }

,
(26)
where I{∥ΩSiΓ−RiY ∥2
2≤T } denotes the indicator function5 on
the constraint feasibility set. The successful deployment of
the PPXA algorithm for this problem depends on our ability
to compute, for each patch, the proximal operator
proxfi(Γ) := arg min
ˆΓ
∥ˆΓ∥1 +
1
2Nµ∥Γ −ˆΓ∥2
2
+ I{∥ΩSiˆΓ−RiY ∥2
2≤T },
(27)
with parameter µ scaling the least-square term. The solution
to the above problem is also the solution to a Lagrangian
arg min
ˆΓ
∥ˆΓ∥1 +
1
2Nµ∥Γ −ˆΓ∥2
2 + λ∗
i ∥Ri(DˆΓ −Y )∥2
2, (28)
in which the Lagrange multiplier is set to an optimal value
λ∗
i : the smallest Lagrange multiplier such that the inequality
constraint is satisﬁed. Observe that, while transitioning from
Equation (27) to Equation (28), we moved from Ωto D, in
order to pose the algorithm w.r.t. the global dictionary. For-
tunately, for a given Lagrangian multiplier λi, such objective
can be efﬁciently minimized by a proximal gradient method
such as (ISTA) [40] or its fast version FISTA [35]. Indeed,
5The indicator function IS equals 0 inside the set S and ∞elsewhere.


## Page 7


7
denoting gi(ˆΓ, λi) :=
1
2Nµ∥Γ −ˆΓ∥2
2 + λi∥Ri(DˆΓ −Y )∥2
2,
ISTA and FISTA revolve around the update step
ˆΓ(k+1) = Stk

ˆΓ(k) + tk
∂gi
∂ˆΓ
(ˆΓ(k), λi)

,
(29)
where tk denotes the step-size6. The dominant effort here is
the evaluation of the gradient of gi with respect to ˆΓ. This boils
down to the computation of convolutions, for which fast GPU
implementations are available. Running FISTA successively
with warm-start initialization allows to estimate the minimizer
for different values of λi with only few extra iterations. This
allows to use a binary-search scheme to estimate the optimal
Lagrange multiplier λ∗
i which in turn provides the solution to
the proximal operator in Equation (27).
Armed with this procedure to compute the proximal oper-
ators, an iteration of the PPXA algorithm boils down to the
following steps:
1) Compute the proximal operators for each patch
∀i = 1 . . . N,
ˆΓ(l)
i
= proxfi(Γ(l)
i ),
(30)
following the procedure described above. The evalua-
tions can be carried out in parallel.
2) Aggregate the solutions
ˆΓ(l) = 1
N
N
X
i
ˆΓ(l)
i .
(31)
3) Update the estimate of Γ along with the auxiliary
variables Γi
∀i,
Γ(l+1)
i
= Γ(n)
i
+ ρl

2ˆΓ(l) −Γ(l) −ˆΓ(l)
i

, (32)
Γ(l+1) = Γ(l) + ρl(ˆΓ(l) −Γ(l)),
where ρl denotes the relaxation parameter 7 on this iteration.
The sequence of sparse vector estimates Γ(l) is proven to
converge to the solution of the ℓ2,∞−ℓ1 CSC problem (22)
[36]. Note that using FISTA in conjunction with PPXA makes
it possible to take full advantage of GPU hardware and high-
level libraries for fast convolutions, in contrast with most
sparse coding algorithm that operate in the Fourier domain
[20], [22].
B. Extension via weighted stripe dictionary
The method described above for the ℓ2,∞−ℓ1 formulation
brings an additional level of ﬂexibility by offering a generic
way to enforce a wider range of structured sparsity. Indeed,
because the proposed method splits the global pursuit into
parallel pursuits on each stripe, a speciﬁc local structure can be
imposed on individual stripes. This can be achieved naturally
by simply weighting the columns of the stripe dictionary, so
as to relatively promote or penalize the use of certain atoms.
Formally this corresponds to
minimize
Γ
∥Γ∥1
subject to
∀i, ∥ΩWiSiΓ −RiY ∥2
2 ≤T,
(33)
6For convergence, the step-size tk must satisfy tk
≤
1
λmax , where
λmax denotes the maximum eigenvalue of ∇gi which can be approximated
efﬁciently via the power method.
7To guaranty convergence, the relaxation parameters (ρl) must satisfy
P
l∈N ρl(2 −ρl) = +∞.
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
θ
∥n2 ¯DlSiΓ −RiY ∥2
∥ΩθSiΓ −RiY ∥2
T
(a)
0
1
2
3
·104
(b) θ = 0.1
0
1
2
3
·104
(c) θ = 0.8
Fig. 5.
Effect of replacing the stripe dictionary Ωwith the convex
combination Ωθ = (1 −θ)Ω+ θn2 ¯Dl to sparse-code the image barbara
after local contrast normalization. (a) The average reconstruction error
∥ΩθSiΓ −RiY ∥2 (in blue) and the average Euclidean distance between
patches and slices ∥n2 ¯DlSiΓ −RiY ∥2 (in red) as a function of θ. In
accordance to the inequality constraint, the reconstruction error remains below
the threshold T. By construction, overlapping slices must be combined to
approximate patches. However, as θ increases, individual slices n2 ¯DlSiΓ
become increasingly similar to patches. (b) and (c) Number of non-zero
coefﬁcients for each of the 20 most commonly used atoms for θ = 0.1
and θ = 0.8 respectively. As θ increases, more diverse local atoms are used.
where Wi denotes the weighting diagonal matrix relative to
the i-th patch8. In the context of the proposed algorithm, this
boils down to an extra weighting within each FISTA iterations.
One particularly interesting application of such strategy
consists in combining the CSC and patch-averaging models.
Such a combination allows for the beneﬁts of both the global
and local models, which respective performances on various
tasks are increasingly well understood. From an analysis stand
point, being able to examine the entire spectrum separating
the CSC model and the patch-averaging approach is highly
valuable, as the understand of their precise inter-relation has
been of interest to the image processing community [41]. With
the proposed method, such combination can be achieved via
a mere re-weighting of the columns that amounts to replacing
the stripe dictionary with the convex combination
Ωθ = (1 −θ)Ω+ θn2 ¯Dl,
(34)
with 0 ≤θ ≤1 and with ¯Dl denoting the local dictionary
padded with zero columns. The parameter θ allows to regulate
the level of patch aggregation that has been proven to be
critical in denoising problems [41]. Setting θ = 0 corresponds
8Note that to be consistent with the global CSC model, the set of matrices
{Wi} must satisfy the relation D =
1
n2
P RT
i ΩWiSi


## Page 8


8
to the ℓ1 −ℓ2,∞CSC formulation above. By increasing θ,
ﬁlters which locations are shifted with respect to the patch
are increasingly penalized. Setting θ = 1 is synonymous with
the patch averaging strategy in which the reconstruction relies
exclusively on Dl and none of its shifted atoms. The behavior
of the resulting problem
minimize
Γ
∥Γ∥1
subject to
∀i, ∥ΩθSiΓ −RiY ∥2
2 ≤T,
(35)
and the structure of its solution are examined in Figure 5.
Figure 5 (a) shows the average representation error ∥ΩθSi −
RiY ∥2 (in blue) and the average Euclidean distance between
individual slices and patches ∥n2 ¯DlSiΓ −RiY ∥(in red) as a
functions of the parameter θ. In accordance to the inequality
constraints in Problem (22), the patch reconstruction error
stays below the threshold T. On the other hand, and as
expected, the Euclidean distance between slices and patches
is above the threshold T, as it is the combination of over-
lapping slices, rather than an isolated slice, that approximates
the patch. However, as θ increases, the term ΩθSiΓ in the
representation error in Problem (35) is increasingly similar to
a slice n2Dlα. This in turn constrains the individual slices to
better approximate the corresponding patch. Additionally, the
constraint affects the diversity of local atoms used in the global
representation. Indeed, Figure 5 (b) and (c) show the number
of non-zero coefﬁcients for θ = 0.1 and θ = 0.8 respectively.
Even though the formulations for θ = 0.1 and θ = 0.8 are
both consistent with the global CSC model, the latter leads to
more diverse local atoms being used. We will see next how
this behavior brings additional practical beneﬁts.
C. Experiments
We illustrate the behavior of the ℓ2,∞−ℓ1 formulation
and its weighted variant on the classic problem of image
inpainting. Let us consider an image X and a diagonal binary
matrix M, which masks the entries in X in which Mi,i = 0.
Image inpainting is the process of ﬁlling in missing areas in
an image in a realistic manner. That is, given the corrupted
image Y = MX, the task consists in estimating the original
signal X.
Estimating the original signal via the ℓ2,∞−ℓ1 CSC requires
solving the problem
minimize
Γ
∥Γ∥1
subject to
∀i, ∥Ri(MDΓ −Y )∥2
2 ≤Ti,
(36)
where the constraint on the representation accuracy incorpo-
rates the binary matrix M, and where the threshold Ti is set on
a patch-by-patch basis to reﬂect the varying numbers of active
pixels in each patch. Minimizing this objective requires only a
slight modiﬁcation of the algorithm described above, namely
incorporating the mask into the function gi and its gradient.
The PPXA relaxation parameter is set to λl = 1.6 and the
scaling factor in the proximal operator is set to µ = 100.
Table I contains the peak signal-to-noise ratio (PSNR) on a
set of publicly available standard test images. In the ﬁrst block
of experiments, we adopt the benchmark framework proposed
in [20]. In particular, the local contrast normalization is applied
to the input image and the local dictionary is pretrained from
the fruit dataset, using the method from [29]. The method
based on the ℓ2,∞−ℓ1 formulation outperforms the method
proposed in [20] and slightly improves over the slice-based
approach of [29]. The best performance are obtained in general
with the weighted ℓ2,∞−ℓ1 (θ = 0.8), which formulation tends
to promote an averaging of similar local estimates. Signiﬁcant
additional improvements are achieved when learning the local
dictionary Dl from the corrupted image. The second block in
Table I contains the inpainting PSNR obtained in this scenario
for the sliced based method [29] and for the weighted ℓ2,∞−
ℓ1 used along the dictionary update proposed in [27]. In this
context, the weighting of the stripe dictionary is particularly
beneﬁcial as it encourages more atoms to be used and therefore
updated (see Figure 5).
VI. CONCLUSION
While enjoying a renewed interest in recent years, the
CSC model has been almost exclusively considered in its
ℓ2 −ℓ1 formulation. In the present work, we expanded the
formulations for the CSC with two alternative formulations,
namely the ℓ2 −ℓ1,∞and ℓ2,∞−ℓ1 formulations in which
mixed-norms, alter how the spatial distributions of non-zero
coefﬁcients are controlled. For both formulations, we derived
algorithms that rely on the ADMM and PPXA algorithms.
The algorithms are simple, easy to implement and can take
full advantage of fast GPU implementation of the convolution
operator. Their convergence naturally follows from the con-
vergence properties of the two standard convex optimization
framework they build on. We examined the performance and
behavior of the proposed formulation on two image processing
tasks: inpainting and cartoon texture separation. Furthermore,
we showed that the ℓ2,∞−ℓ1 formulation in particular opens
the door to a wide variety of structured sparsity, that could
bring additional practical beneﬁts while still being consistent
with the CSC model. An interesting example of such structured
sparsity was offered in the combination of the CSC and
patch-averaging models, showing that such a mixture provides
improved performance. Finally, we envision that similar com-
binations of global and local sparse priors, within the proposed
unifying framework, will allow to further beneﬁts in several
other restoration problems.
VII. ACKNOWLEDGEMENTS
The research leading to these results has received funding
in part from the European Research Council under EUs 7th
Framework Program, ERC under Grant 320649, and in part
by Israel Science Foundation (ISF) grant no. 1770/14.


## Page 9


9
barbara
lena
boat
hill
house
couple
man
Heide et al. [20]
11.00
11.77
10.29
10.37
10.18
11.99
11.60
Papyan et al. [29]
11.67
11.92
10.33
10.66
10.56
12.25
11.84
ℓ1 −ℓ2,∞
11.65
11.99
10.39
10.55
10.60
12.34
11.91
weighted ℓ1 −ℓ2,∞,
11.78
12.13
10.58
10.65
10.62
12.46
11.98
Papyan et al. [29] , image speciﬁc Dl
15.20
12.35
11.60
10.90
11.70
12.41
11.71
weighted ℓ1 −ℓ2,∞, image speciﬁc Dl
16.11
12.29
11.93
11.22
12.13
13.16
12.05
TABLE I
IMAGE INPAINTING. THE ℓ2 −ℓ1 BASED METHOD OF [29] AND [20] ARE COMPARED TO THE PROPOSED METHODS: THE ℓ2,∞−ℓ1 FORMULATION AND
THE FORMULATION WITH A WEIGHTED STRIPE DICTIONARY. IN THE FIRST BLOCK, THE LOCAL DICTIONARY IS PRETRAINED FROM THE F R U I T DATASET
USING THE METHOD FROM [29]. THE ℓ2,∞PRIOR IMPROVES OVER THE BEST ℓ2 −ℓ1 BASED METHOD FORMULATION. THE WEIGHTED STRIPE
DICTIONARY Ωθ WITH θ = 0.8 BRINGS AN ADDITIONAL IMPROVEMENT IN PSNR OVER THE STANDARD ℓ2,∞BY PROMOTING PATCH AVERAGING. IN
THE RESULT REPORTED IN THE SECOND BLOCK, THE LOCAL DICTIONARY USED IS LEARNED FROM THE CORRUPTED IMAGE. IN THIS SCENARIO, THE
WEIGHTED ℓ2,∞−ℓ1 FORMULATION WITH θ = 0.8 GENERALLY OUTPERFORMS [29].
REFERENCES
[1] Michael Elad, Sparse and Redundant Representations - From Theory to
Applications in Signal and Image Processing., Springer, 2010.
[2] Michael Elad and Michal Aharon,
“Image denoising via sparse and
redundant representations over learned dictionaries,” IEEE Transactions
on Image processing, vol. 15, no. 12, pp. 3736–3745, 2006.
[3] Julien Mairal, Francis Bach, Jean Ponce, Guillermo Sapiro, and Andrew
Zisserman,
“Non-local sparse models for image restoration,”
in
Computer Vision, 2009 IEEE 12th International Conference on. IEEE,
2009, pp. 2272–2279.
[4] Yaniv Romano, Matan Protter, and Michael Elad,
“Single image
interpolation via adaptive non-local sparsity-based modeling,”
IEEE
Transactions on Image Processing, 2014.
[5] Jianchao Yang, John Wright, Thomas S Huang, and Yi Ma, “Image
super-resolution via sparse representation,” IEEE transactions on image
processing, vol. 19, no. 11, pp. 2861–2873, 2010.
[6] Guoshen Yu, Guillermo Sapiro, and St´ephane Mallat, “Solving inverse
problems with piecewise linear estimators: From gaussian mixture
models to structured sparsity,” IEEE Transactions on Image Processing,
vol. 21, no. 5, pp. 2481–2499, 2012.
[7] Weisheng Dong, Lei Zhang, Guangming Shi, and Xin Li, “Nonlocally
centralized sparse representation for image restoration,” IEEE Transac-
tions on Image Processing, vol. 22, no. 4, pp. 1620–1630, 2013.
[8] Michal Aharon, Michael Elad, and Alfred Bruckstein, “K-svd: An algo-
rithm for designing overcomplete dictionaries for sparse representation,”
IEEE Transactions on signal processing, vol. 54, no. 11, pp. 4311–4322,
2006.
[9] Kjersti Engan, Sven Ole Aase, and J Hakon Husoy,
“Method of
optimal directions for frame design,” in Acoustics, Speech, and Signal
Processing, 1999. Proceedings., 1999 IEEE International Conference
on. IEEE, 1999, vol. 5, pp. 2443–2446.
[10] Julien Mairal, Michael Elad, and Guillermo Sapiro,
“Sparse repre-
sentation for color image restoration,”
IEEE Transactions on image
processing, vol. 17, no. 1, pp. 53–69, 2008.
[11] Jeremias Sulam and Michael Elad, “Expected patch log likelihood with
a sparse prior,”
in International Workshop on Energy Minimization
Methods in Computer Vision and Pattern Recognition. Springer, 2015,
pp. 99–111.
[12] Vardan Papyan and Michael Elad,
“Multi-scale patch-based image
restoration,” IEEE Transactions on image processing, vol. 25, no. 1,
pp. 249–261, 2016.
[13] Julien Mairal, Guillermo Sapiro, and Michael Elad, “Learning multiscale
sparse representations for image and video restoration,”
Multiscale
Modeling & Simulation, vol. 7, no. 1, pp. 214–241, 2008.
[14] Jeremias Sulam, Boaz Ophir, and Michael Elad,
“Image denoising
through multi-scale learnt dictionaries,”
in Image Processing (ICIP),
2014 IEEE International Conference on. IEEE, 2014, pp. 808–812.
[15] Daniel Zoran and Yair Weiss, “From learning models of natural image
patches to whole image restoration,” in Computer Vision (ICCV), 2011
IEEE International Conference on. IEEE, 2011, pp. 479–486.
[16] Roger Grosse, Rajat Raina, Helen Kwong, and Andrew Y Ng, “Shift-
invariance sparse coding for audio classiﬁcation,”
arXiv preprint
arXiv:1206.5241, 2012.
[17] Jayaraman Thiagarajan, Karthikeyan Ramamurthy, and Andreas Spanias,
“Shift-invariant sparse representation of images using learned dictionar-
ies,” in Machine Learning for Signal Processing, 2008. MLSP 2008.
IEEE Workshop on. IEEE, 2008, pp. 145–150.
[18] Cristian Rusu, Bogdan Dumitrescu, and Sotirios A Tsaftaris, “Explicit
shift-invariant dictionary learning,” IEEE Signal Processing Letters, vol.
21, no. 1, pp. 6–9, 2014.
[19] Hilton Bristow, Anders Eriksson, and Simon Lucey, “Fast convolutional
sparse coding,” in Proceedings of the IEEE Conference on Computer
Vision and Pattern Recognition, 2013, pp. 391–398.
[20] Felix Heide, Wolfgang Heidrich, and Gordon Wetzstein,
“Fast and
ﬂexible convolutional sparse coding,”
in Proceedings of the IEEE
Conference on Computer Vision and Pattern Recognition, 2015, pp.
5135–5143.
[21] Bailey Kong and Charless C. Fowlkes, “Fast convolutional sparse coding
(fcsc),”
Department of Computer Science, University of California,
Irvine, Tech. Rep, vol. 3, 2014.
[22] Brendt Wohlberg, “Efﬁcient convolutional sparse coding,” in Acoustics,
Speech and Signal Processing (ICASSP), 2014 IEEE International
Conference on. IEEE, 2014, pp. 7173–7177.
[23] Shuhang Gu, Wangmeng Zuo, Qi Xie, Deyu Meng, Xiangchu Feng, and
Lei Zhang, “Convolutional sparse coding for image super-resolution,” in
Proceedings of the IEEE International Conference on Computer Vision,
2015, pp. 1823–1831.
[24] Florence Yellin, Benjamin D. Haeffele, and Ren´e Vidal, “Blood cell de-
tection and counting in holographic lens-free imaging by convolutional
sparse dictionary learning and coding,” in Biomedical Imaging (ISBI
2017), 2017 IEEE 14th International Symposium on. IEEE, 2017, pp.
650–653.
[25] Ana Serrano, Felix Heide, Diego Gutierrez, Gordon Wetzstein, and
Belen Masia,
“Convolutional sparse coding for high dynamic range
imaging,” in Computer Graphics Forum. Wiley Online Library, 2016,
vol. 35, pp. 153–163.
[26] Vardan Papyan, Jeremias Sulam, and Michael Elad, “Working locally
thinking globally: Theoretical guarantees for convolutional sparse cod-
ing,”
IEEE Transactions on Signal Processing, vol. 65, no. 21, pp.
5687–5701, 2017.
[27] Elad Plaut and Raja Giryes,
“Matching pursuit based convolutional
sparse coding,” in Acoustics, Speech and Signal Processing (ICASSP),
2018 IEEE International Conference on. IEEE, 2018, IEEE SigPort.
[28] Brendt Wohlberg, “Convolutional sparse coding with overlapping group
norms,” arXiv preprint arXiv:1708.09038, 2017.
[29] Vardan Papyan, Yaniv Romano, Michael Elad, and Jeremias Sulam,
“Convolutional dictionary learning via local processing.,” in ICCV, 2017,
pp. 5306–5314.
[30] Matthieu Kowalski, “Sparse regression using mixed norms,” Applied
and Computational Harmonic Analysis, vol. 27, no. 3, pp. 303–324,
2009.
[31] Stephen Boyd, Neal Parikh, Eric Chu, Borja Peleato, Jonathan Eck-
stein, et al., “Distributed optimization and statistical learning via the
alternating direction method of multipliers,” Foundations and Trends R⃝
in Machine learning, vol. 3, no. 1, pp. 1–122, 2011.
[32] Carl T Kelley, Iterative methods for optimization, vol. 18, Siam, 1999.
[33] John Duchi, Shai Shalev-Shwartz, Yoram Singer, and Tushar Chandra,
“Efﬁcient projections onto the l 1-ball for learning in high dimensions,”
in Proceedings of the 25th international conference on Machine learn-
ing. ACM, 2008, pp. 272–279.
[34] Stanley H Chan, Ramsin Khoshabeh, Kristofor B Gibson, Philip E Gill,
and Truong Q Nguyen,
“An augmented lagrangian method for total
variation video restoration,” IEEE Transactions on Image Processing,
vol. 20, no. 11, pp. 3097–3111, 2011.
[35] Amir Beck and Marc Teboulle, “A fast iterative shrinkage-thresholding


## Page 10


10
algorithm for linear inverse problems,”
SIAM journal on imaging
sciences, vol. 2, no. 1, pp. 183–202, 2009.
[36] Patrick L Combettes and Jean-Christophe Pesquet,
“A proximal de-
composition method for solving convex variational inverse problems,”
Inverse problems, vol. 24, no. 6, pp. 065014, 2008.
[37] Patrick L Combettes and Jean-Christophe Pesquet, “Proximal splitting
methods in signal processing,”
in Fixed-point algorithms for inverse
problems in science and engineering, pp. 185–212. Springer, 2011.
[38] Neal Parikh, Stephen Boyd, et al., “Proximal algorithms,” Foundations
and Trends R⃝in Optimization, vol. 1, no. 3, pp. 127–239, 2014.
[39] Heinz H Bauschke, Patrick L Combettes, et al., Convex analysis and
monotone operator theory in Hilbert spaces, vol. 408, Springer, 2011.
[40] Ingrid Daubechies, Michel Defrise, and Christine De Mol, “An iterative
thresholding algorithm for linear inverse problems with a sparsity
constraint,”
Communications on Pure and Applied Mathematics: A
Journal Issued by the Courant Institute of Mathematical Sciences, vol.
57, no. 11, pp. 1413–1457, 2004.
[41] Diego
Carrera,
Giacomo
Boracchi,
Alessandro
Foi,
and
Brendt
Wohlberg, “Sparse overcomplete denoising: aggregation versus global
optimization,”
IEEE Signal Processing Letters, vol. 24, no. 10, pp.
1468–1472, 2017.
APPENDIX
Proposition 1. For a point y and the ℓ1-ball of radius r,
Br := {x, s.t.∥x∥1 ≤r}, the distance between y and the ball
d(y, Br) := inf {∥x −y∥2, | x ∈Br} ,
is a convex function of the ball radius r.
Proof. From the ℓ1-norm triangle inequality, it comes that for
any convex combination of two radii θr1 + (1 −θ)r2, with
0 ≤θ ≤1, we have the inclusion
θBr1 + (1 −θ)Br2 ⊂Bθr1+(1−θ)r2,
where θBr1 denotes the set of points {θx1|x1
∈Br1}.
In particular, for the nearest points to y in Br1 and Br2
respectively, i.e., for x1 ∈Br1 such that ∥y−x1∥2 = d(y, Br1)
and x2 ∈Br2 such that ∥y −x2∥2 = d(y, Br2), we have
θx1 + (1 −θ)x2 ∈Bθr1+(1−θ)r2,
and therefore
∥y −(θx1 + (1 −θ)x2)∥2 ≥d(y, Bθr1+(1−θ)r2).
Finally, from the Euclidean norm triangle inequality, it comes
that
θd(y, Br1) + (1 −θ)d(y, Br2) ≥d(y, Bθr1+(1−θ)r2)
which proves that r 7→d(y, Br) is convex.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]