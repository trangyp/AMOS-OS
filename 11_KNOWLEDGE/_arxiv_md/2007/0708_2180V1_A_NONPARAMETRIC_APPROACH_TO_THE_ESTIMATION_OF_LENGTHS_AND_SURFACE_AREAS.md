---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0708.2180v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0708.2180v1_A_nonparametric_approach_to_the_estimation_of_lengths_and_surface_areas

> Source: 0708.2180v1_A_nonparametric_approach_to_the_estimation_of_lengths_and_surface_areas.pdf

> Pages: 22

---


## Page 1


arXiv:0708.2180v1  [math.ST]  16 Aug 2007
The Annals of Statistics
2007, Vol. 35, No. 3, 1031–1051
DOI: 10.1214/009053606000001532
c
⃝Institute of Mathematical Statistics, 2007
A NONPARAMETRIC APPROACH TO THE ESTIMATION OF
LENGTHS AND SURFACE AREAS
By Antonio Cuevas,1 Ricardo Fraiman1 and
Alberto Rodr´ıguez-Casal2
Universidad Aut´onoma de Madrid, Universidad de San Andr´es
and Universidad de Santiago de Compostela
The Minkowski content L0(G) of a body G ⊂Rd represents the
boundary length (for d = 2) or the surface area (for d = 3) of G. A
method for estimating L0(G) is proposed. It relies on a nonparamet-
ric estimator based on the information provided by a random sample
(taken on a rectangle containing G) in which we are able to identify
whether every point is inside or outside G. Some theoretical prop-
erties concerning strong consistency, L1-error and convergence rates
are obtained. A practical application to a problem of image analysis
in cardiology is discussed in some detail. A brief simulation study is
provided.
1. Introduction.
The estimation of the surface area of a body G in the
Euclidean space Rd (“surface area” amounts to “boundary length” in the
bidimensional case d = 2) has been extensively considered in stereology;
see [1, 2, 12]. We are concerned here with this problem from a diﬀerent
point of view, using the approach and tools of nonparametric statistics and,
more speciﬁcally, of nonparametric set estimation; see, for example, [6] for
a survey.
In a way, the length and surface area estimation problem can be seen
as a further, more diﬃcult, stage in set estimation theory, after the early
developments concerned with the estimation of volume (associated with the
L1 (measure) distance; see [8]), “visual” shape (associated with the Haus-
dorﬀmetric; see [5]), level sets [3, 13, 16, 19, 20] and boundaries [7]. We will
Received June 2005; revised March 2006.
1Supported in part by Spanish Grant MTM2004-00098.
2Supported
in
part
by
Spanish
Grants
MTM2005-00820
and
PGIDIT06PXIB207009PR.
AMS 2000 subject classiﬁcations. Primary 62G07; secondary 62G20.
Key words and phrases. Minkowski content, nonparametric set estimation, length esti-
mation, statistical image analysis.
This is an electronic reprint of the original article published by the
Institute of Mathematical Statistics in The Annals of Statistics,
2007, Vol. 35, No. 3, 1031–1051. This reprint diﬀers from the original in
pagination and typographic detail.
1


## Page 2


2
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
see, in fact, that, while the sample data in nonparametric set estimation
theory comes usually from random points selected inside the set of interest,
G, we will need here additional information given by sample points coming
from outside G (see the beginning of Section 2). The estimation of bound-
ary length has also some practical interest. For example, in medical imaging
the boundary length appears in connection with the notion of “Contour In-
dex” (see, e.g., [11]), a shape measurement used as an auxiliary diagnostic
criterion. These ideas are developed in more detail in Section 4.
At this point it might be useful to point out what we mean by “nonpara-
metric approach” in order to clarify its main diﬀerences with the stereological
point of view for these problems:
(a) Unlike the stereological approach, we are not concerned with unbi-
ased estimation, but with asymptotic properties such as consistency and
convergence rates.
(b) The proposed estimator is intended to work asymptotically in any di-
mension d under quite general shape restrictions. It depends on a smoothing
parameter which must be carefully chosen.
(c) Our method will provide as a by-product an estimator of the boundary
of the body G under study. In contrast, stereological methods are not usually
concerned with the global estimation of sets; they are rather focused on the
estimation of some real parameter (length, volume, surface area, . . . ).
(d) The sample data consists of randomly selected points. In stereology
the available information for estimating lengths and surface areas usually
comes either from one- or two-dimensional sections or from systematic grids.
Our aim is to obtain an easy-to-implement automatic method valid for
the analysis of a wide class of images. As a ﬁrst step we should clearly es-
tablish what we mean by “surface area.” The Hausdorﬀmeasure (see, e.g.,
[14]) provides a suitable general deﬁnition of this concept. This deﬁnition,
however, is not always very convenient from the point of view of mathemat-
ical handling and eﬀective evaluation. So we will use instead the following
simpler, less general notion (which coincides with the Hausdorﬀmeasure, up
to a constant factor, in regular cases): The surface area of a body G ⊂Rd is
given by the Minkowski content (see [14], Chapter 2),
L0(G) = lim
ε→0
µ(B(∂G,ε))
2ε
,
(1)
provided that this limit exists and it is ﬁnite. Here µ stands for the ordinary
Lebesgue measure on Rd, ∂G denotes the boundary of G and, for any A ⊂Rd,
B(A,ε) is the “outer parallel set” B(A,ε) := S
x∈A B(x,ε), where B(x,ε)
denotes the closed ball with center x and radius ε. While the Minkowski
content fails to satisfy some interesting properties, such as σ-additivity, it
has a clear intuitive basis and is suﬃcient for most practical purposes.


## Page 3


ESTIMATING LENGTHS AND AREAS
3
This paper is organized as follows. The estimator is introduced in Sec-
tion 2. Its basic statistical properties concerning asymptotic behavior, bias
and variability are established in Section 3. A real-data application in car-
diology is discussed in Section 4. A brief Monte Carlo study is presented in
Section 5. Section 6 is devoted to the proofs.
2. The sampling model and the proposed estimator.
Let G ⊂Rd be a
body whose Minkowski content L0 = L0(G) is well deﬁned, strictly positive
and ﬁnite. Our goal is estimating L0 which for d = 2 represents the boundary
length and for d = 3 the surface area. Without loss of generality, we will
assume that G is a subset of the open unit square (0,1)d.
The sampling information is given by i.i.d. observations (Z1,δ1),...,(Zn,δn)
of a random variable (Z,δ), where Z is uniformly distributed on the unit
square [0,1]d and δ = 1 if Z ∈G, δ = 0 if Z /∈G. This means that, with
probability one, given a sample of points on the unit square, we are able to
decide whether or not they belong to the “green area” G or to the “red”
one, R = [0,1]d \ G.
It will be convenient to use the following notation. Let us denote by PX
and PY the conditional distributions of the “green” and “red” observations,
that is, the distributions of Z|{δ = 1} and Z|{δ = 0}. Observe that PX and
PY are both uniform on G and R, respectively. Now, given z ∈[0,1]d and
ε ≥0, denote by Gz(ε) and Rz(ε), respectively, the numbers of green and
red sample observations belonging to the ball B(z,ε), that is,
Gz(ε) ≡Gn,z(ε) =
n
X
i=1
I{δi=1,∥Zi−z∥≤ε},
(2)
Rz(ε) ≡Rn,z(ε) =
n
X
i=1
I{δi=0,∥Zi−z∥≤ε}.
Clearly, Gz(ε) has a binomial distribution with parameters n and pX(z,ε) =
P(∥Z −z∥≤ε,δ = 1) = µ(G)PX(B(z,ε)). Similarly, Rz(ε) has a binomial
distribution with parameters n and pY (z,ε) = (1 −µ(G))PY (B(z,ε)).
Let {εn} be a deterministic sequence of positive numbers which converges
to zero as n tends to inﬁnity. Denote T = ∂G. We propose the following
estimator for the “dilated boundary,” B(T,εn):
Tn = {z ∈[0,1]d :Rz(εn) ≥1 and Gz(εn) ≥1}.
(3)
The simple intuitive idea behind Tn is to consider those points z in
whose vicinity green and red points coexist. Of course, we could “robus-
tify” this estimator by replacing the condition Rz(εn) ≥1 and Gz(εn) ≥1
with Rz(εn) ≥r1 and Gz(εn) ≥g1, for some ﬁxed integer numbers r1 > 1 and
g1 > 1. This modiﬁed estimator (which will not be considered here) would


## Page 4


4
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
be smoother and less noisy than the original version (3) at the expense of
some eﬃciency loss.
Finally, the deﬁnition (1) for Tn suggests the following natural estimator
for L0 = L0(G):
Ln = µ(Tn)
2εn
.
(4)
As usual, the nonparametric estimator (4) depends on a smoothing pa-
rameter εn which must be carefully chosen. In general, it should tend to
zero slowly enough. The theoretical results of Section 3 will provide some
additional insights in this respect.
Note that the proposed method could be useful even in those cases where
the image G is completely known (e.g., we could have a picture of G),
but it is too complicated for directly measuring its boundary. Then the
sample Z1,...,Zn can be artiﬁcially generated provided that we are able to
decide whether Zi belongs to G or not. So, in some sense, (4) can be seen
as a “stochastic” algorithm to approximate L0. This idea will be further
developed in Section 4.
3. Theoretical results.
We analyze in this section the properties of the
estimator Ln of the Minkowski content, L0 = L0(G).
3.1. Strong consistency.
The almost sure (a.s.) convergence of Ln to L0 is
established in Theorem 1 below. The “standardness” hypothesis (a) prevents
the set G from having “too sharp” inlets and peaks along the boundary T.
This condition has been previously used in set estimation (see, e.g., [7]).
Theorem 1.
Let us assume the following conditions.
(a) The sets G and R are both standard in T, that is, there exists a
constant C > 0 such that, for small enough ε,
PX(B(t,ε)) ≥Cµ(B(t,ε))
and
PY (B(t,ε)) ≥Cµ(B(t,ε))
for all t ∈T.
(b) The sequence {εn} satisﬁes
εn →0
and
nεd
n
log n →∞.
Then
Ln = µ(Tn)
2εn
→L0,
a.s.
Observe that the conditions imposed in (b) on the sequence εn of smooth-
ing parameters are identical to those required for the strong consistency of
kernel density estimators (see, e.g., [15]). However, as we will see below, the
role of the smoothing parameter is quite diﬀerent in both setups.


## Page 5


ESTIMATING LENGTHS AND AREAS
5
3.2. The function L(ε).
For a given value of n, the estimator Ln pro-
vides, in fact, an estimation for L(εn) := µ(B(T,εn))/(2εn) which, in turn,
is an approximation of the target value L0. Thus, in order to assess the ac-
curacy of the estimator Ln, it is interesting to get more precise information
on the diﬀerence |L(ε) −L0|. We next show that, under some smoothness
assumptions, L(ε) is diﬀerentiable at ε = 0, which entails |L(ε)−L0| = O(ε).
Indeed, note that
B(T,ε) = B(G,ε) ∩B(R,ε),
which leads to
µ(B(T,ε)) = µ(B(G,ε)) + µ(B(R,ε)) −µ(B([0,1]d,ε)).
(5)
Thus, the point is to have some idea about the structure of the “dilated
measures” on the right-hand side of (5), when considered as functions of ε.
If G is assumed to be convex, the classical Steiner formula (see, e.g., [17],
page 197) establishes that µ(B(G,ε)) is a polynomial in ε of degree at most
d. Unfortunately, this result is not useful in our case, as the hypothesis of
convexity for G could be too restrictive (e.g., in image analysis) and, in any
case, it cannot be assumed simultaneously for both G and R = [0,1]d \ G,
except in trivial situations. However, we will be able to prove the required
diﬀerentiability property for L(ε) by combining some ideas of mathematical
morphology (which we will use to impose the appropriate regularity condi-
tions on G) with a (partial) generalization of Steiner’s formula proved by
Federer [10]. He imposes a positive reach condition closely related to the fol-
lowing rolling condition often used in set estimation (see, e.g., Walther [20]):
It is said that a ball can roll along T = ∂G outside G ⊂Rd if there exists
r0 > 0 such that, for all r ≤r0 and x ∈T, there exists a closed ball of radius
r, Bx, such that Bx ∩G = {x}.
A deep study of this outer rolling condition, including some interesting
equivalences, is due to Walther [21], Theorem 1. This condition arises in
mathematical morphology, a branch of the huge current theory of image
analysis; see [18]. It has also appeared, under a slightly diﬀerent form, in
contexts not directly related to image analysis. In a similar vein, Federer [10]
deﬁnes the reach of G as the largest (possibly ∞) value r0 such that if x ∈Rd
and the distance from x to G is smaller than r0, then G contains a unique
point nearest to x. For our purposes of better understanding the nature of
the function L(ε), it will be particularly useful to employ a generalization
of Steiner’s formula obtained by Federer ([10], Theorem 5.6). This result
establishes that, for any set G of positive reach r0, the function µ(G,ε)
coincides locally [for ε ∈(0,r0)] with a polynomial of degree at most d whose
independent term is µ(G).
Thus, if we assume that both G and R satisfy the positive reach condition
we may use Federer’s theorem, together with (5), to conclude that µ(T,ε)


## Page 6


6
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
coincides in the interval (0,r0) with P(ε), where P denotes a polynomial of
degree at most d with a null independent term. Note that (by the assumption
made on the ﬁniteness of the Minkowski content L0) the coeﬃcient of ε in
P(ε) must necessarily coincide with 2L0 so that L(ε)−L0 is a polynomial in ε
with a null independent term. In particular, we get that L(ε) is diﬀerentiable
at ε = 0.
3.3. Bounds for E(Ln): L1-consistency and convergence rates, variability
and bias.
It is not hard to show (see the proof of Statement 1 in the proof
of Theorem 1) that, with probability one, Tn ⊂B(T,εn) and, therefore,
Ln ≤L(εn)
a.s.
(6)
This means that Ln tends to underestimate L0 for those “regular” sets where
the values of the function L(ε) = µ(B(T,ε))/(2ε) are very close to L(0) := L0
for small values of ε. In the bidimensional case the simplest example is given
by the circle, for which L(ε) ≡L0.
The following result provides a lower bound for E(Ln).
Theorem 2.
Assume that the standardness condition (a) in Theorem 1
holds. Assume also that the function F(ε) := µ(B(T,ε)) is diﬀerentiable in
a neighborhood of 0 and the derivative F ′ is continuous at 0. Then
E(Ln) ≥L(εn) −In,
(7)
where In = 1
εn
R
B(T,εn) exp(−Kn(εn −d(z,T))d)dz, K being a positive con-
stant and d(z,T) = inf{∥z −t∥:t ∈T}. Also,
In = O((nεd
n)−1/d).
(8)
The proof is given in Section 6. Note that, according to the discussion
in Section 3.2, if we assume that both G and R fulﬁll the positive reach
property, then the function F(ε) = µ(B(T,ε)) coincides in a neighborhood
of 0 with a polynomial of degree ≤d, so it is certainly diﬀerentiable at 0
with a continuous derivative.
The following corollary (the proof is in Section 6) provides a condition for
the L1-consistency, as well as an upper bound for the L1-convergence rate
of the estimator Ln.
Corollary 1.
(a) Under the same conditions of Theorem 2, we have
E|Ln −L0| ≤In + |L(εn) −L0|.
(9)
As a consequence, the standard conditions for consistency, εn →0 and nεd
n →
∞, are also suﬃcient here to ensure the L1-consistency E|Ln −L0| →0.
(b) By assuming further that G and R satisfy the positive reach condition
mentioned in Section 3.2, we have that the optimal order for the bound (9)
is O(n−1/2d), which is attained for εn = n−1/2d.


## Page 7


ESTIMATING LENGTHS AND AREAS
7
Not surprisingly, the bound O(n−1/2d) corresponds to a rather slow con-
vergence rate. We do not believe that the exact rate can improve much on
this bound. Recall that the typical rates for the much easier problem of con-
sistently estimating the boundary ∂G, with respect to the Hausdorﬀmetric,
are of type O((log n/n)1/d) [7] even under the assumption of convexity on G
[9]. Anyway, in some applications (see Section 4) the estimator Ln is based
on artiﬁcial (Monte Carlo) samples and the slow convergence rate is not so
crucial a problem, as the sample size can, in principle, be increased as much
as necessary.
As a further consequence of (6)–(8) we get [under the regularity assump-
tions imposed in Corollary 1(b)] the following bounds for the L1-variability
and the bias:
E|Ln −E(Ln)| ≤E|Ln −L(εn)| + |L(εn) −E(Ln)|
(10)
≤2In = O((nεd
n)−1/d),
L0 −E(Ln) = (L(εn) −E(Ln)) + (L0 −L(εn))
(11)
= O((nεd
n)−1/d) + O(εn).
Thus, the assumption nεd
n →∞guarantees the convergence to zero of the
variability around the mean, E|Ln −E(Ln)|. Note that this condition is
identical to that imposed in the classical (L2 or L1) theory of density es-
timation in order to control the variability term. However, expression (11)
shows that nεd
n →∞is also useful to make the bias term tend to zero. This
is in sharp contrast with the typical situation in nonparametric functional
estimation where εn →0 usually suﬃces to kill the bias. The situation here
is a bit diﬀerent: We do need the condition εn →0, but if the convergence
is too fast, the estimator Ln will be biased, underestimating the value of
L0. Thus, the bias is also controlled by the condition nεd
n →∞which is
used in the proof of Theorem 1 to prevent the boundary estimator Tn from
having spurious “holes” [that would lead to underestimation of µ(B(T,εn))
by µ(Tn)].
Let us also note that it is interesting to assess the magnitude of the “eﬀec-
tive bias” E(Ln)−L(εn). This is particularly useful in practical applications
(see Section 4 below) when one is willing to consider L(εn) as a reasonable
approximation for L0, thus, accepting a systematic bias which hopefully
would aﬀect in a similar way all the images under study. In these cases the
focus is on the diﬀerences E(Ln) −L(εn), analyzed above.
4. Applications to image analysis.
Let us ﬁrst emphasize that our ap-
proach is basically aimed at those cases where only partial (random) in-
formation is available, rather than dealing with completely known images.


## Page 8


8
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
These usually come in a digitized form, but the digitization process is itself
an approximation involving nontrivial problems, largely beyond the scope of
this paper. The classical book by Serra [18], pages 211–224, provides some
deep insights in this regard. Anyway, if we have a “known” image, either in a
digitized version or in a “exact” format (e.g., the area inside a known closed
curve: see Section 5), it is tempting to check the behavior of the estimator
(4), based on Monte Carlo random samples, when used to approximate the
boundary length.
In this section we develop this idea and apply it to a medical example.
4.1. The contour index. A case study in cardiology.
The irregularity
in the border of a tumor or an infarcted area is an auxiliary diagnostic
criterion for malignancy assessment. The so-called “contour index” (CI)
provides a size-independent quantitative measurement of boundary rough-
ness. It is deﬁned (for the case of bidimensional images) as the quotient
boundary length/√area. Its minimal value (2√π) is attained by the circle.
The CI has been used in oncology (see, e.g., [4]) and cardiology [11], but the
interpretation of this index in the two scientiﬁc ﬁelds is somewhat diﬀerent.
A high value of the CI in a tumor usually suggests a high dissemination ca-
pacity of the injured area. On the contrary, in cardiology the prognosis of an
infarction tends to be worse when the damage is highly concentrated with a
“regular” border (which will provide a small CI) rather than disseminated
in many small irregular patches.
In order to assess the applicability of our estimation method to real ex-
amples, we have analyzed an image (Figure 1, left) of the infarcted heart of
a pig. It corresponds to one side of a transversal section of the heart which
has been exposed to a histochemical reaction that dyes the living cells. Thus,
the infarcted cells fail to catch the color, appearing as a white-grayish area
in the upper-right side of the image. This area should not be confounded
with the endocardial endothelium (which covers the inner part of the heart).
It appears in deep white at the centre of the image. In fact, most of this
endothelium white area is not placed in the same plane as the considered
transversal section. The jpg ﬁle of the original color image (Figure 1, top left)
has been digitized in an array of 495 × 710 pixels. The information stored
in every pixel consists of a vector (x1,x2,x3) indicating the level (on the
scale 0–255) of primary colors (red, green and blue) at that point. So, if we
consider the position coordinates, every pixel is, in fact, a ﬁve-dimensional
observation.
4.2. A stochastic algorithm for calculating the CI.
In the example con-
sidered the goal is to identify the infarcted area and give an approximate
value for the CI. Our estimation method has been used with the following
steps:


## Page 9


ESTIMATING LENGTHS AND AREAS
9
1. Image identiﬁcation and cleaning. The image of interest (Figure 1, top
left) must be treated in order to clearly decide the precise shape of the
infarcted area (a bit blurred in the original picture) whose boundary
is to be measured. The problem is to decide whether or not a pixel in
the picture corresponds to the infarcted area. We have done this using
the classical Fisher linear discriminant function. To put this in more
precise terms, two large samples of pixels have been taken in the infarcted
and in the noninfarcted area. Then the classical linear discrimination
method was applied to classify the remaining points. The classiﬁcation
error was negligible except for the points in the white endothelial area
at the centre of the original image (that tended to be confounded with
the infarcted cells), where the error rate was appreciable. The result of
this automatic discrimination-based treatment is shown in Figure 1 (top
right) where the infarcted area has been colored in black but there are also
some patches of obviously misclassiﬁed endothelial tissue. Thus, a ﬁnal
“manual cleaning” was made to remove these patches. The result is given
in Figure 1 (bottom). This was the ﬁnal image (600×600 pixels) used for
Fig. 1.
An infarcted heart (top left). The estimated infarct area (top right). The
“cleaned” infarct area (bottom).


## Page 10


10
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
the quantitative analysis described in Section 4.3. Let us note that the
classiﬁcation algorithm has been based only on the “color” coordinates
of every point. We have disregarded the information provided by the
point positions because the use of a linear discrimination method looked
particularly unsuitable when these variables are involved.
By the way, this application of discriminant methods in image cleaning
shows the interest in studying discriminant theory from the point of view
of image analysis; this would amount to incorporating classiﬁcation crite-
ria based on shape preservation (connectedness, smoothness), in addition
to the usual notions relying on misclassiﬁcation probabilities.
2. Monte Carlo sampling and classiﬁcation. A large artiﬁcial uniform sample
Z1,...,Zn is drawn in [0,1]d. The classiﬁcation variable δi is obtained for
each Zi :δi = 1 when Zi belongs to the infarcted area, δi = 0 otherwise.
3. Estimation. As indicated in Section 3, the optimal order (under some
shape restrictions) for εn is n−1/2d. The estimator (4) (and the corre-
sponding boundary estimator Tn) is obtained for several values of the
smoothing parameter εn. The idea is to check the sensitivity of the esti-
mation process with respect to changes in the value of εn. Alternatively,
some procedure (cross-validation, bootstrap-based choice) for the opti-
mal selection of the smoothing parameter could be used. However, in real
applications (see Section 4.3 below) an optimal choice would be not so
crucial when the procedure is used to establish comparisons between sev-
eral images. In the case of a bi-color digitized image the calculation of
µ(Tn) (and that of the area that appears in the denominator of the CI)
is made by a simple count of the corresponding activated (black) pixels.
Note that, in practice, the ﬁrst stage could be omitted as, strictly speaking,
only the randomly selected points need to be classiﬁed. An interesting open
problem in this regard would be to consider a more realistic model incorpo-
rating the classiﬁcation error in the “red” or “green” areas, G and R (see
Section 2).
4.3. Results.
In the example of Figure 1 we have considered two sample
sizes, n = 50,000 and n = 100,000. The results are summarized in Table 1.
The choices of the values εn are of type Ckn−1/4, where the constants Ck,
for k = 1,2,3, are taken in order to consider small perturbations around the
reference value n−1/4. In the case n = 100,000 we have n−1/4 = 0.0562, so
we decided to take C1, C2 and C3 in order to get “exact” values (0.05, 0.02
and 0.01) for the smoothing parameter Ckεn. This entails that C1 = 0.8897,
C2 = 0.3559 and C3 = 0.1779 and we have kept these constants for the case
n = 50,000.
The output in Table 1 indicates that the CI value is about 5.4. Clearly,
the values (3.61, 3.96) obtained for the largest choices of εn correspond to


## Page 11


ESTIMATING LENGTHS AND AREAS
11
Fig. 2.
Oversmoothed boundary estimation of the infarct area in Figure 1.
oversmoothed estimations; recall that the CI for a circle is 3.5449. This is
apparent from the image of Figure 2, which shows the estimate Tn of the
infarct boundary for the case n = 50,000, εn = 0.05.
A remarkable fact in the results is their small variability. This means
that, in practice, we can use a given (not necessarily optimal) choice of εn
to perform comparisons between diﬀerent images. Maybe the true CI’s are
estimated with an appreciable bias, but this is, by far, the main source of
error. Thus, the estimated CI’s would allow us to get an assessment of the
relative importance of the diﬀerent cases from the point of view of infarct
geometry, and the value of εn corresponds, in some sense, to the resolution
level employed in the procedure.
It is also worthwhile to observe that due to the presence of εn in both
the numerator and denominator of (4), the variability of this estimator is
not a monotone function of εn. This is in contrast to the usual behavior of
nonparametric estimators (e.g., kernel density estimators).
The estimation CI ≃5.4 suggests a rather negative diagnostic for the
infarct shown in Figure 1. For example, in [11] the “infarct geometry” of a
control group of eight infarcted pigs was studied and compared with that
of another treatment group of eight individuals, also suﬀering a miochardial
infarct but receiving a drug called 2,3-butanedione monoxime. The values
found for the CI in the control and the treatment group are 7.7 ± 0.2 and
9.4 ± 0.7, respectively, which suggests a much better prognosis than that in
our example.
In the case of the digital images, the choice of the smoothing parameter
εn is obviously limited by the pixel size. In our case, each side of the square
Table 1
Average values and standard deviations along 100 replications of the CI estimation for
the infarct area in Figure 1
Sample size
n = 50,000
n = 100,000
εn
0.0119
0.0238
0.0595
0.01
0.02
0.05
Mean
5.2080
5.1265
3.6104
5.7257
5.53
3.96
Standard deviation
0.0042
0.00342
0.0129
0.0294
0.0213
0.0099


## Page 12


12
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
[0,1]×[0,1] was divided into 600 square pixels so that the minimum eﬀective
choice of εn would be 1/600 = 0.0017.
On the other hand, the large sample sizes (n = 50,000,100,000) used in
the study suggest the idea of using all the available pixels (360,000 in this
example). The practical implications of such an “exhaustive method” are
analyzed in some detail below [see paragraphs (g) and (h) in Section 5.2],
in connection with the simulation example considered there, where the true
value of the boundary length is exactly known.
The relative simplicity of the proposed method suggests the possibility
of generalizations to multicolor higher-dimensional images; these could ap-
pear in the context of magnetic resonance explorations where very precise
determinations are obtained for diﬀerent magnitudes as the pH or the ATP
(which measures the energy cell status).
5. Simulations.
The estimator (4) is designed for cases where only in-
complete information (given by “natural” sampling points on both sides of
the border) is available. In this sense, the proposed method can be seen as
a reﬁned version of the nonparametric method for estimating boundaries
discussed in [7]. The requirement of two samples (inside and outside the set)
can be formalized with diﬀerent models, but seems to be unavoidable in or-
der to estimate the surface measure, unless we are willing to impose strong
assumptions on the shape of G. On the other hand, the estimator (4) can be
based on Monte Carlo (artiﬁcial) samples, to be used in contexts not directly
related to image analysis, just as a stochastic device for approximating the
length of a closed curve or the surface area of a body in R3.
As an example, we have considered the so-called Tschirnhausen Cubic
(also known as Catalan’s trisectrix and l’Hospital’s cubic), a plane curve
whose polar equations are
r = asec3(θ/3),
for θ ∈(0,π),
r = asec3((2π −θ)/3),
for θ ∈(π,2π).
The reason for choosing this curve is the existence of closed simple ex-
pressions for both the length (L0 = 12a
√
3) of the loop and the area inside
(A = 72a2√
3/5). We have used our estimation method in order to approx-
imate L0 and A in the case a = 1 (see Figure 3), so the target values are
L0 = 20.7846 and A = 24.9415. The random samples, with sizes n = 30,000
and n = 10,000, are drawn in the square [−9,2] × [−5.5,5.5], which fully
includes the Tschirnhausen loop.
Before discussing the simulation experiment and output, we should con-
sider a practical issue regarding the eﬀective calculation of the estimator.


## Page 13


ESTIMATING LENGTHS AND AREAS
13
Fig. 3.
The Tschirnhausen Cubic.
5.1. Monte Carlo approximation of the estimator.
The estimator (4)
(and the corresponding boundary estimator Tn) must be computed for every
choice of εn considered. An important practical problem is that the direct
computation of µ(Tn) is not an easy task. However, it can be approximated
easily, with an arbitrary precision level, by using again the Monte Carlo
method. Let Z∗
1,...,Z∗
B be a random sample (independent of Z1,...,Zn)
from the uniform distribution on the unit square [0,1]d. Since, with proba-
bility one, Tn ⊂[0,1]d for n large enough, we have that µ(Tn) = P(Z∗
1 ∈Tn)
and therefore, for B large,
µB(Tn) =
PB
i=1 I{Z∗
i ∈Tn}
B
should be a good approximation of µ(Tn). Note that it is very easy to check
when a point Z∗belongs to Tn. This Monte Carlo method provides an
approximate evaluation for Ln,
L∗
n,B = µB(Tn)
2εn
.
An interesting question in order to apply the proposed method is how to
pick B (as a function of n) to ensure that L∗
n,B is a consistent estimator of
L0. The next theorem gives an answer to this question. The proof is given
in Section 6.
Theorem 3.
Besides the hypothesis of Theorem 1, let us assume that
Bεn
log n →∞.
(12)
Then L∗
n,B →L0, a.s.


## Page 14


14
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
5.2. Simulation output.
The results of our simulation study are summa-
rized in Table 2. The estimator Ln has been evaluated for 500 samples of
sizes n = 30,000 and n = 10,000. The resampling parameter B, used in the
Monte Carlo approximations of µ(Tn), was B = 1500 in all cases considered.
The output in Tables 2 (for n = 30,000) and 3 (for n = 10,000) provides the
average, standard deviation and median of Ln computed from the 500 repli-
cations, for diﬀerent values of εn. The output is obtained using the same
simulated samples for each value of εn. Thus the usual Monte Carlo area
estimate, which does not depend on a smoothing parameter, is the same in
all cases. The average, standard deviation and median obtained for this area
estimator are respectively 24.9196, 0.4458 and 24.9125 for n = 30,000 and
24.9485, 0.7842 and 24.9889 for n = 10,000.
Some direct conclusions can be drawn from these results:
(a) The true value L0 = 20.7846 is systematically underestimated with a
relative error about 4.7% (in the case n = 30,000) and 8.1% (for n = 10,000).
The gain obtained by increasing the sample size is mostly apparent in the
Table 2
Average, standard deviation and median of Ln computed over 500 replications with
n = 30,000
εn
0.76
0.78
0.80
0.82
0.84
0.86
0.88
Average
19.7301
19.7416
19.7621
19.7644
19.7918
19.7918
19.7859
Std. deviation
1.3940
1.3935
1.3793
1.3448
1.3470
1.3200
1.3072
Median
19.7548
19.7920
19.8274
19.7576
19.8930
19.8249
19.8081
εn
0.9
0.92
0.94
0.96
0.98
1.0
1.2
Average
19.7901
19.7949
19.8109
19.8208
19.8290
19.8230
19.8237
Std. deviation
1.2952
1.2917
1.2636
1.2331
1.2159
1.2031
1.0666
Median
19.8863
19.9150
19.8522
19.8804
19.8209
19.8804
19.8627
Table 3
Average, standard deviation and median of Ln computed over 500 replications with
n = 10,000
εn
0.76
0.78
0.80
0.82
0.84
0.86
0.88
Average
19.0026
18.8594
18.9512
18.9370
18.9507
19.0806
19.1083
Std. deviation
1.3908
1.3586
1.3260
1.2627
1.3075
1.3398
1.2467
Median
18.9736
18.9221
18.9791
18.9300
18.9842
19.0359
19.0852
εn
0.9
0.92
0.94
0.96
0.98
1.0
1.2
Average
19.0492
19.1409
19.1408
19.2057
19.2134
19.2384
19.3679
Std. deviation
1.2956
1.1936
1.1599
1.2460
1.2157
1.1777
1.0394
Median
19.0381
19.1774
19.1303
19.1735
19.2150
19.2548
19.3679


## Page 15


ESTIMATING LENGTHS AND AREAS
15
bias. The average (over all values of εn) of the average output is 19.0890 for
n = 10,000 and 19.7900 for n = 30,000.
(b) The simulation output shows a considerable stability with respect to
the values of the smoothing parameter εn. This stability remains even for
other smaller values of εn (not included in the tables) that we have checked.
For example, whereas the average of the average values of Ln obtained from
the 14 choices of εn included in Table 2 is 19.79, the corresponding average
for the other ﬁve equispaced values of εn, ranging from 0.64 to 0.72, is
19.5985.
(c) The sampling distributions are almost symmetric, with the median
very close to the mean in all cases.
(d) There is a slight, but consistent, decline of the variability around the
mean as the smoothing parameter increases.
(e) As could be predicted, the variability results tend to improve, at the
expense of some additional computational burden, by increasing the value
of the resampling parameter B. For example, the output for the average,
standard deviation and median of Ln with εn = 0.92, n = 30,000 and B =
2000 is 19.8341, 1.0790 and 19.8458, respectively. For n = 10,000, with the
same value of εn, the corresponding output for B = 3000 is 19.2229, 0.8490
and 19.1774. These results account for the small changes in the variability of
Ln from n = 10,000 to n = 30,000. They suggest that, for these sample size
magnitudes, most variability is due to the Monte Carlo approximation stage
of the numerator µ(Tn) in (4), controlled by the parameter B. The value
B = 1500, used in the simulations of Tables 2 and 3, should be considered as
a ﬁrst computationally aﬀordable choice, suitable for this preliminary study.
(f) The plots of the density estimators obtained from the values of Ln
suggest that the sampling distribution is, for all the considered choices of
εn, very close to normality. As a consequence, an interesting open problem
would be to establish the asymptotic normality of Ln. However, the proof
seems far from trivial in view of the special structure of Ln.
(g) In this example we have implemented our method in a case where an
exact equation for the border is known. So no digitization process is involved.
In practice, most real black-and-white images come in a digitized version.
In mathematical terms this amounts to replacing the original image G by a
ﬁnite union Gh of square pixels with sides of ﬁxed length h, parallel to the
coordinate axes. In such situations one could think of exactly measuring the
border length Lh of the “digital boundary” ∂Gh. This is just the number
of pixel sides separating regions of diﬀerent colors. This is computationally
feasible and avoids the use of any smoothing parameter. However, it is not
diﬃcult to see that this direct exhaustive procedure will fail, as Lh cannot
converge to L when h tends to 0. For example, if ∂G includes a segment A in-
side the diagonal x = y, the length of A will be overestimated by a factor
√
2
when G is approximated by Gh. This is empirically conﬁrmed in our case:


## Page 16


16
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
If we replace the region G inside the Tschirnhausen Cubic by a digitized
version, obtained by dividing the “frame square” [−9,2] × [−5.5,5.5] into
300×300 pixels, the direct exhaustive method gives an estimation Lh = 25.97
for the true value L0 = 20.78. Our method, with n = 10,000, provides much
more acceptable estimation around 19.7 (see Table 3). The use of a more
precise digitization does not improve things (in fact, it reveals a lack of con-
sistency in the exhaustive procedure). For example, a 600 × 600 digitization
leads to Lh ≃26.5, and with 1024×1024 pixels we get Lh ≃28.1875.
The exhaustive method could also been implemented in an indirect ver-
sion, based on measuring areas. The boundary length could be estimated by
Area(Ghb)/2h, where Ghb denotes the union of all “boundary pixels” in Gh.
This also fails: estimation for the 300×300 and 600×600 digitizations gives
respectively 19.36 and 19.32. Note that, in fact, this procedure uses implic-
itly a smoothing parameter (the pixel side length h). The failure should be
interpreted as a phenomenon of undersmoothing; see the comment about
the bias after (10) and (11).
(h) The use of all the available pixels is still a possibility, although, in
view of the previous comment it should always be done with an appropri-
ate amount of smoothing, along the lines indicated above. Although this
exhaustive procedure “with smoothing” is feasible in many cases, it is not
advisable in general, due to its lack of robustness against the “noise” (in
the form of disperse error pixels not belonging to the image). By contrast,
the method based on random samples will automatically ignore (with high
probability) the possible disperse noise, at the expense of higher variabil-
ity. We have checked this by randomly adding four patches of noise, in the
form of circular clusters (with radii 0.25) of black pixels, within the square
[−9,2] × [−5.5,5.5], where the loop of the Tschirnhausen Cubic is included.
In the worst case (when the four noise patches fall on the white background,
outside the black image), the amount of noise added to the image represents
less than 1% of the total number of pixels. The presence of the noise turned
out to have a devastating eﬀect in the exhaustive method with smoothing:
The average length obtained with this method for 500 of such noisy images
is 24.92 (standard deviation 1.63), whereas the random method applied with
a sample size n = 5000 and εn = 0.94 gave an average of 21.07 (standard de-
viation 0.9992). Curiously enough, the results for the latter method (recall
that the true value is 20.78) are even better than those obtained in the case
with no noise since the noise tends to increase the boundary length, thus
partially correcting the inherent underestimation bias.
6. Proofs.
Proof of Theorem 1.
The result is a consequence of the following
two claims.


## Page 17


ESTIMATING LENGTHS AND AREAS
17
Statement 1.
With probability one, Tn ⊂B(T,εn).
Statement 2.
For any 0 < α < 1, we have eventually, with probability
one,
B(T,ε′
n) ⊂Tn,
where ε′
n = αεn,0 < α < 1.
Proof of Statement 1.
For any z ∈Tn, we have that (with proba-
bility one) B(z,εn) meets G and its complementary R. Therefore, B(z,εn)
meets the boundary of G, T, which means that z belongs to B(T,εn). This
concludes the proof of Statement 1.
□
Proof of Statement 2.
By the Borel–Cantelli lemma, it is suﬃcient
to show that
∞
X
n=1
P(B(T,ε′
n) ⊈Tn) < ∞.
However,
P(B(T,ε′
n) ⊈Tn) ≤P(∃z ∈B(T,ε′
n):Gz(εn) = 0)
(13)
+ P(∃z ∈B(T,ε′
n):Rz(εn) = 0).
Now, we try to ﬁnd an upper bound for the ﬁrst probability on the right-
hand side. The other probability can be bounded by a similar argument.
For any z ∈B(T,ε′
n), there is an t ∈T for which B(t,βn) ⊂B(z,εn), where
βn = (1 −α)εn. Therefore,
P(∃z ∈B(T,ε′
n):Gz(εn) = 0) ≤P(∃t ∈T :Gt(βn) = 0).
Let T(βn) be a set [with cardinality D(βn)] of ball centres corresponding
to a minimal covering of T by balls of radius βn/2. So we consider a class
{B(s,βn/2):s ∈T(βn) ⊂T} such that
T ⊂
[
s∈T(βn)
B

s, βn
2

.
Since {∃t ∈T :Gt(βn) = 0} ⊂{∃s ∈T(βn):Gs(βn/2) = 0}, we have
P(∃t ∈T :Gt(βn) = 0) ≤P

∃s ∈T(βn):Gs
βn
2

= 0

≤
X
s∈T(βn)
P

Gs
βn
2

= 0



## Page 18


18
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
=
X
s∈T(βn)

1 −pX

s, βn
2
n
≤
X
s∈T(βn)
exp

−npX

s, βn
2

,
where in the last inequality we have used the fact that 1 −x ≤e−x for
0 ≤x ≤1. The right-hand side of the above inequality can easily be bounded
since, from the standardness hypothesis, for n large enough,
pX

s, βn
2

≥Cωdµ(G)βd
n
2d = K1εd
n,
where ωd = µ(B(0,1)) and K1 is a constant which depends on the dimension
d, α, µ(G) and C. Therefore,
P(∃z ∈B(T,ε′
n):Gz(εn) = 0) ≤D(βn)exp{−K1εd
n}.
Now, in order to bound the function D(ε), recall that it represents the
cardinality of a minimal covering C(ε/2) of T by balls of radii ε/2. This
entails (e.g. [14], page 78) that there exists a family of D(ε) disjoint balls
with radii ε/4 and centres at points of T. Then the sum of their measures
must be smaller than µ(B(T,ε/4)). Hence,
D(ε)(ε/4)dωd ≤µ(B(T,ε/4)).
Since L(ε) →L0, we get for ε small enough, D(ε) ≤Aε1−d for some constant
A. Therefore,
P(∃z ∈B(T,ε′
n):Gz(εn) = 0) ≤K2ε1−d
n
exp(−K1nεd
n),
where K2 = (1 −α)1−dA. The condition nεd
n/log n →∞ensures the con-
vergence of the series P∞
n=1 ε1−d
n
exp(−K1nεd
n). The other probability in
(13) can be bounded in a similar way. Note that the obvious inequality
D(ε) ≤Aε−d would also suﬃce for the purpose of convergence, but the above
simple argument provides a sharper bound for the probabilities. This con-
cludes the proof of Statement 2.
□
Now the proof of Theorem 1 is a straightforward consequence of State-
ments 1 and 2. Indeed, we have that, with probability one,
αL0 = lim
n
µ(B(T,ε′
n))
2εn
≤liminf
n
Ln ≤limsup
n
Ln ≤lim
n
µ(B(T,εn))
2εn
= L0.
This holds for any α ∈(0,1) and therefore, the conclusion of the theorem
follows.
□


## Page 19


ESTIMATING LENGTHS AND AREAS
19
Proof of Theorem 2.
The expected value of Ln can be written as
E(Ln) = E(µ(Tn))
2εn
=
1
2εn
E
Z
I{z∈Tn}µ(dz)

=
1
2εn
Z
E(I{z∈Tn})µ(dz)
=
1
2εn
Z
P(z ∈Tn)µ(dz) =
1
2εn
Z
B(T,εn)
P(z ∈Tn)µ(dz),
since, with probability one, Tn ⊂B(T,εn). It is clear that
P(z /∈Tn) ≤P(Gz(εn) = 0) + P(Rz(εn) = 0).
(14)
Remember that Gz(εn) has a binomial distribution with parameters n and
pX(z,εn). Therefore,
P(Gz(εn) = 0) = (1 −pX(z,εn))n ≤exp{−npX(z,εn)}.
Let PT z ∈T be the projection of z onto T. Since, for any z ∈B(T,εn),
B(PT z,εn −d(z,T)) ⊂B(z,εn),
using condition (a) of Theorem 1, we have that, for εn small enough,
PX(B(z,εn)) ≥Cωd(εn −d(z,T))d.
Hence,
P(Gz = 0) ≤exp{−K1n(εn −d(z,T))d},
where K1 is a positive constant which depends only on µ(G), C and the
dimension d. Similarly, we have that P(Rz = 0) ≤exp{−K2n(εn−d(z,T))d},
for a positive constant K2 which depends only on µ(R), C and d. Using these
bounds and (14), we get
P(z ∈Tn) ≥1 −2exp{−Kn(εn −d(z,T))d},
where K = min(K1,K2). Thus, we have that
E(Ln) =
1
2εn
Z
B(T,εn)
P(z ∈Tn)dz
≥
1
2εn
Z
B(T,εn)
(1 −2exp{−Kn(εn −d(z,T))d})dz
= L(εn) −1
εn
Z
B(T,εn)
exp{−Kn(εn −d(z,T))d}dz = L(εn) −In,
with
In = 1
εn
Z
B(T,εn)
gn(d(z,T))dz,


## Page 20


20
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
where gn(w) = exp{−Kn(εn −w)d}. By the change of variable formula, we
have that
In = 1
εn
Z εn
0
gn(w)F(dw),
(15)
where F(w) = µ({z :d(z,T) ≤w}) = µ(B(T,w)). By the assumption made
on the continuous diﬀerentiability of F at 0 and the existence and ﬁniteness
of the Minkowski content, we have F ′(0) = 2L0 so that, for w small enough,
F ′(ω) ≤3L0. Finally, for n large enough,
In ≤3L0
εn
Z εn
0
exp{−Kntd}dt = 3L0
εn
Z Knεd
n
0
exp(−u)
1
d(Kn)1/d u−(d−1)/d du
≤
3L0
dK1/d(εdnn)1/d
Z ∞
0
exp(−u)u−(d−1)/d du =
A
(εdnn)1/d ,
where in the ﬁrst inequality we have applied in (15) the change of variable
t = εn −w and then (for the ﬁrst equality) u = Kntd.
□
Proof of Corollary 1.
The bound (9) for the L1-error follows as a
direct consequence of the bounds (6)–(8) together with the triangle inequal-
ity. Now, the conclusion (a) follows from (8) and the deﬁnition of L0.
To show (b), note that the optimal convergence order for the bound (9)
is obtained by making equal the convergence orders of both terms on the
right-hand side. Under the smoothness conditions mentioned in Section 3.2,
we have |L(εn) −L0| = O(εn) (see [10], Theorem 5.6). Thus, from (8), the
optimal order for the bound (9) is O(n−1/2d), which is attained for εn =
n−1/2d.
□
Proof of Theorem 3.
Clearly, it is enough to show that L∗
n,B −Ln →
0, a.s. This can be proved showing that, for any ρ > 0,
X
n
P(|L∗
n,B −Ln| > ρ) < ∞.
(16)
This is not hard to do because, given Z1,...,Zn, L∗
n,B has (essentially) a bi-
nomial distribution with mean Ln and, therefore, we can use a concentration
inequality to control the size of its tail. Indeed,
P(|L∗
n,B −Ln| > ρ)
= E(P(|L∗
n,B −Ln| > ρ|Z1,...,Zn))
= E(P(|µB(Tn) −µ(Tn)| > 2ρεn|Z1,...,Zn))
≤E

2exp

−
4ρ2ε2
nB
2µ(Tn)(1 −µ(Tn)) + (4/3)ρεn

,


## Page 21


ESTIMATING LENGTHS AND AREAS
21
where in the last step we have used Bernstein’s inequality. It is not hard
to bound this last quantity because µ(Tn) goes to zero (with probability
one) as fast as εn when n tends to inﬁnity. To see this, note that in Theo-
rem 1 we proved that (with probability one) Tn ⊂B(T,εn) and, therefore,
µ(Tn) ≤µ(B(T,εn)). Since L(εn) →L0, we have that, for n large enough,
µ(B(T,εn)) ≤4L0εn. So, for n large enough,
E

2exp

−
4ρ2ε2
nB
2µ(Tn)(1 −µ(Tn)) + (4/3)ρεn

≤E

2exp

−
4ρ2ε2
nB
8L0εn + (4/3)ρεn

= 2exp{−Kρ,L0εnB},
where Kρ,L0 is a (positive) constant. Obviously, (12) ensures that, for any
ρ > 0,
X
n
exp{−Kρ,L0εnB} < ∞,
and, therefore, (16) holds. This concludes the proof of the theorem.
□
Acknowledgments.
We are most grateful to Dr. David Garc´ıa-Dorado
(Servei de Cardiologia, Hospital Vall d’Hebron, Barcelona) who provided
us with the material for the cardiology case-study and explained to us the
required medical concepts. We are also indebted to Professor Jes´us Gonzalo
(Departamento de Matem´aticas, Universidad Aut´onoma de Madrid) for his
very helpful geometrical insights on the Minkowski content notion. The third
author also wishes to thank the University of Vigo (Spain), where he carried
out part of his work on this paper. The constructive comments of two referees
are gratefully acknowledged.
REFERENCES
[1] Baddeley, A. J., Gundersen, H. J. G. and Cruz-Orive, L. M. (1986). Estimation
of surface area from vertical sections. J. Microscopy 142 259–276.
[2] Baddeley, A. J. and Jensen, E. B. V. (2005). Stereology for Statisticians. Chapman
and Hall/CRC, Boca Raton, FL. MR2107000
[3] Ba´ıllo, A. (2003). Total error in a plug-in estimator of level sets. Statist. Probab.
Lett. 65 411–417. MR2039885
[4] Canzonieri, V. and Carbone, A. (1998). Clinical and biological applications of
image analysis in non-Hodgkin’s lymphomas. Hematological Oncology 16 15–28.
[5] Cuevas, A. and Fraiman, R. (1997). A plug-in approach to support estimation.
Ann. Statist. 25 2300–2312. MR1604449
[6] Cuevas, A. and Rodr´ıguez-Casal, A. (2003). Set estimation: An overview and
some recent developments. In Recent Advances and Trends in Nonparametric
Statistics (M. G. Akritas and D. N. Politis, eds.) 251–264. North-Holland, Am-
sterdam.


## Page 22


22
A. CUEVAS, R. FRAIMAN AND A. RODR´IGUEZ-CASAL
[7] Cuevas, A. and Rodr´ıguez-Casal, A. (2004). On boundary estimation. Adv. in
Appl. Probab. 36 340–354. MR2058139
[8] Devroye, L. and Wise, G. L. (1980). Detection of abnormal behavior via nonpara-
metric estimation of the support. SIAM J. Appl. Math. 38 480–488. MR0579432
[9] D¨umbgen, L. and Walther, G. (1996). Rates of convergence for random approxi-
mations of convex sets. Adv. in Appl. Probab. 28 384–393. MR1387882
[10] Federer, H. (1959). Curvature measures. Trans. Amer. Math. Soc. 93 418–491.
MR0110078
[11] Garc´ıa-Dorado, D., Theroux, P., Duran, J. M., Solares, J., Alonso, J.,
Sanz, E., Mu˜noz, R., Elizaga, J., Botas, J. and Fern´andez-Avil´es, F.
(1992). Selective inhibition of the contractile apparatus. A new approach to
modiﬁcation of infarct size, infarct composition, and infarct geometry during
coronary artery occlusion and reperfusion. Circulation 85 1160–1174.
[12] Gokhale, A. M. (1990). Unbiased estimation of curve length in 3D using vertical
slices. J. Microscopy 159 133–141.
[13] Korostel¨ev, A. P. and Tsybakov, A. B. (1993). Minimax Theory of Image Re-
construction. Lecture Notes in Statist. 82. Springer, New York. MR1226450
[14] Matilla, P. (1995). Geometry of Sets and Measures in Euclidean Spaces. Fractals
and Rectiﬁability. Cambridge Univ. Press. MR1333890
[15] Prakasa Rao, B. L. S. (1983). Nonparametric Functional Estimation. Academic
Press, New York. MR0740865
[16] Polonik, W. (1995). Measuring mass concentrations and estimating density contour
clusters—an excess mass approach. Ann. Statist. 23 855–881. MR1345204
[17] Schneider, R. (1993). Convex Bodies: The Brunn–Minkowski Theory. Cambridge
Univ. Press. MR1216521
[18] Serra, J. (1984). Image Analysis and Mathematical Morphology. Academic Press,
London. MR0753649
[19] Tsybakov, A. B. (1997). On nonparametric estimation of density level sets. Ann.
Statist. 25 948–969. MR1447735
[20] Walther, G. (1997). Granulometric smoothing. Ann. Statist. 25 2273–2299.
MR1604445
[21] Walther, G. (1999). On a generalization of Blaschke’s rolling theorem and the
smoothing of surfaces. Math. Methods Appl. Sci. 22 301–316. MR1671447
A. Cuevas
Departamento de Matem´aticas
Universidad Aut´onoma de Madrid
28049 Madrid
Spain
E-mail: antonio.cuevas@uam.es
R. Fraiman
Departamento de Matem´atica
Universidad de San Andr´es
Argentina
E-mail: rfraiman@udesa.edu.ar
A. Rodr´ıguez-Casal
Departamento de Estat´ıstica e Inv. Operativa
Universidad de Santiago de Compostela
Spain
E-mail: alrodcas@usc.es

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]