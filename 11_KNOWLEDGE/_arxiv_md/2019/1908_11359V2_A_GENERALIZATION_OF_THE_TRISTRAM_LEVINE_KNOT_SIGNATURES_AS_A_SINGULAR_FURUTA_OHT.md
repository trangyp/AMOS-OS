---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.11359v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1908.11359v2_A_Generalization_of_the_Tristram-Levine_Knot_Signatures_as_a_Singular_Furuta-Oht

> Source: 1908.11359v2_A_Generalization_of_the_Tristram-Levine_Knot_Signatures_as_a_Singular_Furuta-Oht.pdf

> Pages: 60

---


## Page 1


arXiv:1908.11359v2  [math.GT]  31 Jan 2021
A GENERALIZATION OF THE TRISTRAM-LEVINE KNOT SIGNATURES AS
A SINGULAR FURUTA-OHTA INVARIANT FOR TORI
MARIANO ECHEVERRIA
Abstract. Given a knot K inside an integer homology sphere Y , the Casson-Lin-Herald invari-
ant can be interpreted as a signed count of conjugacy classes of irreducible representations of the
knot complement into SU(2) which map the meridian of the knot to a ﬁxed conjugacy class. It
has the interesting feature that it determines the Tristram-Levine signature of the knot associated
to the conjugacy class chosen.
Turning things around, given a 4-manifold X with the integral homology of S1 × S3, and an
embedded torus T inside X such that H1(T; Z) surjects onto H1(X; Z), we deﬁne a signed count of
conjugacy classes of irreducible representations of the torus complement into SU(2) which satisfy
an analogous ﬁxed conjugacy class condition to the one mentioned above for the knot case. Our
count recovers the Casson-Lin-Herald invariant of the knot in the product case, thus it can be
regarded as implicitly deﬁning a Tristram-Levine signature for tori.
This count can also be considered as a singular Furuta-Ohta invariant, and it is a special
case of a larger family of Donaldson invariants which we also deﬁne. In particular, when (X, T)
is obtained from a self-concordance of a knot (Y, K) satisfying an admissibility condition, these
Donaldson invariants are related to the Lefschetz number of an Instanton Floer homology for
knots which we construct. Moreover, from these Floer groups we obtain Frøyshov invariants for
knots which allows us to assign a Frøyshov invariant to an embedded torus whenever it arises
from such a self-concordance.
1. Introduction
An observation of some analogies: deﬁning λF O(X, T, α).
The main impetus behind this work stems from the following observation: given an integer
homology sphere Y , Casson deﬁned [1] an invariant λC(Y ) ∈Z which morally can be regarded as
1/2 of a signed count of conjugacy classes of irreducible representations π1(Y ) →SU(2). Moving one
dimension up, if X is a four manifold with the same integral homology as S1 × S3, i.e, H∗(X; Z) ≃
H∗(S1 × S3; Z), Furuta and Ohta deﬁned [24] a Casson-type invariant λF O(X) ∈Z which again
can morally be interpreted as a signed count of conjugacy classes of irreducible representations
π1(X) →SU(2). Strictly speaking, X must satisfy additional conditions besides being a homology
S1 × S3, but it will always be the case that if one takes X = S1 × Y , then λF O(X) is well deﬁned,
and can be made to agree with λC(Y ).
Now, if we consider the case of a knot K inside Y , one can follow the same strategy and try
to deﬁne a signed count of conjugacy classes of irreducible representations π1(Y \K) →SU(2). As
will become clear soon, in this case it is natural to ﬁx the conjugacy class where the meridian of
the knot µK is being sent, regarded as the generator of the reducible representations H1(Y \K) ≃
Z[µK] →SU(2). This conjugacy class is speciﬁed by a (holonomy) parameter α ∈(0, 1/2), and
whenever △K(e−4πiα) ̸= 0, where △K is the Alexander polynomial of the knot, Herald showed [26,
Theorem 0.1] that a Casson-type count of representations can be made, which we will denote as
λCLH(Y, K, α) ∈Z. Here the L in λCLH stands for Lin, who had studied before Herald [44] the
1


## Page 2


Mariano Echeverria
2
case where the meridian is sent to a trace zero matrix, which corresponds to the parameter α = 1/4
(and using a symplectic rather than gauge theoretic approach).
The invariant λCLH recovers the Tristram-Levine knot signatures σK [58, 42], in the sense that
(with our orientation conventions) λCLH(Y, K, α) = 4λC(Y ) + 1
2σK(e−4πiα). This clearly begs the
question:
Question 1. Given an embedded torus T inside a four manifold X with the integer homology of
S1 × S3 and a number α ∈(0, 1/2), which conditions must be imposed on T and α so that one can
deﬁne an invariant λF O(X, T, α) ∈Z that satisﬁes the property that for any knot K ⊂Y and α
such that △K(e−4πiα) ̸= 0, λF O(S1 × Y, S1 × K, α) coincides with λCLH(Y, K, α) (perhaps up to
rescaling)?
Before stating such conditions, we recall quickly why it is possible to deﬁne λCLH(Y, K, α), since
the reader may be less aware of this construction. In fact, as far as we can tell there was no standard
notation for this invariant, which is why we decided to name it λCLH(Y, K, α). More context and
motivation can be found in an “annotated” version of this paper posted on the author’s website [15].
As mentioned before, given a knot K inside Y , suppose we want to deﬁne a (signed) count
of irreducible representations of π1(Y \K) into SU(2), analogous to the deﬁnition of the Casson
invariant λC(Y ) [1]. For any Casson type count, we need to understand ﬁrst the reducible represen-
tations, given that they correspond to singular points in the character variety R(Y \K, SU(2)) =
hom(π1(Y \K), SU(2))/SU(2) (or the space of ﬂat SU(2) connections mod gauge depending on
one’s preference).
The reducible representations are determined by H1(Y \K; Z) ≃Z[µK]. In particular, a reducible
representation ρ is completely speciﬁed by A = ρ(1) ∈SU(2), and up to conjugacy is determined by
its trace tr(A) ∈[−2, 2]. Thus the reducible representations inside R(Y \K, SU(2)) are in bijection
with [−2, 2].
This means that inside R(Y \K, SU(2)) the reducible representations are not isolated. In order
to isolate them, we can decompose this space as R(Y \K, SU(2)) = S
α Rα(Y \K, SU(2)), where
Rα(Y \K, SU(2)) consists of conjugacy classes of representations which map the meridian µK to
the conjugacy class of the matrix
µK →
 e−2πiα
0
0
e2πiα

Since the trace of this matrix is 2 cos(2πα), it suﬃces to take α ∈[0, 1/2] to exhaust all the possible
conjugacy classes where the meridian can be sent. We will assume that α ∈(0, 1/2) since the
endpoints correspond to representations of π1(Y ) into SU(2) or SO(3) (so K is not involved in
those cases). Inside each Rα(Y \K, SU(2)) there will be only one reducible representation θα, so
trying to make a (signed) count λCLH(Y, K, α) of the elements inside Rα(Y \K, SU(2)) is very
similar to the problem of deﬁning λC(Y ) as a (signed) count of elements inside R(Y, SU(2)), which
also contains only one reducible θ, the trivial representation of π1(Y ) into SU(2).
The only caveat with this analogy is that contrary to the case of Y , where θ is automatically
isolated from the irreducible representations, it may be the case that θα is not isolated from the irre-
ducible representations inside Rα(Y \K, SU(2)), thus making it impossible to deﬁne λCLH(Y, K, α).
In fact, as we will review in section 4, whenever △K(e−4πiα) ̸= 0, where △K is the Alexander poly-
nomial of the knot K, we can deﬁne λCLH(Y, K, α), i.e, for such α the reducible θα is isolated.
If we think of the representation θα as corresponding to a ﬂat SU(2) connection Aα on the
trivial bundle E = (Y \K) × C2 →Y \K, which is the point of view we will take, the condition
that △K(e−4πiα) ̸= 0 is equivalent to the vanishing of the cohomology group with local coeﬃcients


## Page 3


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 3
H1(Y \K; L⊗2
α ), where Aα determines a complex line bundle Lα →Y \K and a splitting E =
Lα ⊕L−1
α .
Going back to the case of an embedded torus T inside X, we will explain in Section 6 the
analogue of the spaces Rα(Y \K, SU(2)), which we denote Rα(X\T, SU(2)). The point is that we
need to understand again the reducible representations of π1(X\T ) →SU(2), which are completely
determined by H1(X\T ; Z). The natural condition for our problem is to assume that H1(T ; Z)
surjects onto H1(X; Z), so that homologically T behaves like S1 times a knot.
This condition
also tell us that H1(X\T ; Z) ≃Z ⊕Z, although for ﬁxed α only one of these Z factors will be of
importance. This means that inside Rα(X\T, SU(2)) the reducible representations should form a
one dimensional family, which is exactly what happens when one is trying to deﬁne λF O(X) using
R(X, SU(2)). Given these preliminaries we can ﬁnally state our answer to Question 1.
Theorem 2. Suppose that X is a closed oriented four manifold with the integral homology of
S1 × S3.
Let T denote an embedded and oriented torus such that H1(T ; Z) ։ H1(X; Z) is a
surjection. Consider a rational value α ∈Q ∩(0, 1/2) such that for all reducible representations
ρ : π1(X\T ) →SU(2) satisfying the holonomy condition 9 determined by α, i.e, elements of
Rα(X\T, SU(2)), we have that H1(X\T ; L⊗2
ρ ) vanishes. Here E = Lρ ⊕L−1
ρ
is the decomposition
induced by the ﬂat connection Aρ associated to ρ, and E is the trivial SU(2) bundle over X\T .
Then we can deﬁne a degree-zero Donaldson invariant, denoted the singular Furuta-Ohta
invariant λF O(X, T, α), which takes even values, i.e, λF O(X, T, α) ∈2Z.
It has the property that for X = S1 × Y , T = S1 × K, for an oriented knot K inside an
integer homology sphere Y , and a value of α ∈Q ∩(0, 1/2) such that △K(e−4πiα) ̸= 0, then
λF O(S1 × Y, S1 × K, α) can be deﬁned, and λF O(S1 × Y, S1 × K, α) = 2λCLH(Y, K, α).
Remark 3. The condition that H1(X\T ; L⊗2
ρ ) vanishes can be equivalently stated in terms of the
Alexander polynomial △T = △X\T of the knot complement.
Namely, we would require that
△T (ˆρ) ̸= 0 for all the characters associated to the reducible representations ρ which satisfy the
holonomy condition determined by α. The notation △T (ˆρ) ̸= 0 is explained in the Appendix of
the annotated version [15] although we will not use the interpretation in terms of the Alexander
polynomial in this paper.
It is important to point out that in order to study the representations of π1(X\T ) into SU(2),
we will use the framework of Kronheimer and Mrowka’s papers [32, 34] on singular gauge theory.
We will review the novel features of this approach in the next section, but the key points are the
following. For pairs (X, Σ) consisting of a closed, oriented four manifold X and an oriented surface
Σ, the SU(2) bundles E over (X, Σ) are now classiﬁed by a pair of two integers (k, l), called the
instanton and monopole numbers respectively.
Write E(k, l) for the corresponding SU(2) bundle associated to the pair (k, l). Then for each
such E(k, l), we can study the space of connections A(E(k, l), α) which have a prescribed singular
behavior along Σ. As before 0 < α < 1/2, and the solutions of the anti-self-dual connections F +
A = 0
for A ∈A(E(0, 0), α) can again be interpreted (mod gauge) as corresponding to representations
of π1(X\T ) →SU(2) which map the “meridian” of the torus µT to a speciﬁc conjugacy class, if
we take Σ = T . In general, the solutions of F +
A = 0 for A ∈A(E(k, l), α) will be called α-ASD
connections. The moduli space of (perturbed) α-ASD connections modulo gauge will be denoted
M(X, Σ, k, l, α). Finally, a gauge equivalence class will normally be denoted as [A], instead of A.
For technical reasons, we need to use an orbifold metric along Σ. This means that there will
be an integer parameter ν such that the orbifold metric along Σ has a cone angle of 2π/ν. Each
α determines a set of allowable cone parameters {ν}, but there is no cone parameter that works


## Page 4


Mariano Echeverria
4
simultaneously for all values of α. Moreover, it is convenient to take the parameter α as a rational
number, i.e, α ∈Q ∩(0, 1/2), so that we can talk about orbifold connections.
From this point of view, λF O(X, T, α) corresponds to a signed count of elements of the moduli
space M(X, Σ, 0, 0, α). Strictly speaking, we should write λF O(X, T, α, ν) and M(X, Σ, 0, 0, α, ν)
since we must always choose ﬁrst a cone angle compatible with α before deﬁning our invariants.
However, as we will mention near the end of the introduction the invariants do not depend on the
cone angle ν due to recent work of Langte Ma [45].
In section 8 we will give some examples of λF O(X, T, α), which arise from the mapping tori
associated to ﬁnite group actions on homology spheres, as well as certain circle bundles over a
3-manifold with the homology of S1 × S2. It will become clear that these are the orbifold versions
of the calculations of λF O(X) done in [52, 51].
An observation of more analogies: deﬁning HI(Y, K, α) and the splitting formula.
Now we describe the second motivation for this project. Thanks to Taubes [57], it is well known
that for an integer homology sphere Y , the instanton Floer homology HI(Y ) [17] categoriﬁes the
Casson invariant in the sense that χ(HI(Y )) = 2λC(Y ).
Moreover, Frøyshov deﬁned [18] a reﬁnement of HI(Y ) which is known as the reduced in-
stanton Floer homology HIred(Y ).
From it one can deﬁne the Frøyshov h-invariant h(Y ) =
1
2(χ(HIred(Y ))−χ(HI(Y ))), which is the precursor to the d-invariant in Heegaard Floer homology
and the Frøyshov invariant in monopole Floer homology. We should notice that our conventions are
slightly diﬀerent from those of Frøyshov, since we are working with the homology (not cohomology)
version of instanton Floer homology.
By the TQFT-like features of instanton Floer homology, a homology cobordism W : Y1 →
Y2 between two integer homology spheres will induce a map between the corresponding Floer
homologies HI(W) : HI(Y1) →HI(Y2). In particular, for a homology cobordism W : Y →Y from
Y to itself, there are maps HI(W) : HI(Y ) →HI(Y ) and HIred(W) : HIred(Y ) →HIred(Y ) for
the unreduced and reduced instanton Floer homologies. This is an interesting case since closing
up W one obtains a four manifold X which is a homology S1 × S3 and for which λF O(X) can be
deﬁned. In this case, Anvari proved [2, Theorem A] a splitting formula for λF O(X) in terms of the
Lefschetz number Lef(HI(W)) of the cobordism map, which reads (in our conventions)
λF O(X) = 1
2Lef(HI(W)) = 1
2Lef(HIred(W)) −h(Y )
and is the analogue of the splitting formula [43, Theorem A] Lin, Ruberman and Saveliev proved
for a similarly-constructed invariant λSW (X) which is deﬁned using the Seiberg-Witten equations
instead. Moreover, an argument due to Frøyshov [21, Theorem 8] for the case of λSW (X) (and which
is readily adapted to λF O(X)) shows that if X is obtained as the closure of a diﬀerent homology
cobordism W ′ : Y ′ →Y ′ then h(Y ) = h(Y ′) and thus it makes sense to talk about the h-invariant
of X, which we denote as h(X). In this way the splitting formula for λF O(X) reads
λF O(X) + h(X) = 1
2Lef(HIred(W))
This naturally leads to the following question:
Question 4. Is it possible to deﬁne instanton Floer homologies HI(Y, K, α), HIred(Y, K, α) for a
value of α satisfying △K(e−4πiα) ̸= 0, and corresponding Frøyshov h-invariants h(Y, K, α) for the
knot K so that whenever (W, Σ) : (Y, K) →(Y, K) is a self-concordance of K, there is a splitting
formula involving λF O(X, T, α) and Lef(HI(Y, Y, α)) (respectively Lef(HIred(Y, K, α)), h(Y, K, α))?
Moreover, can one deﬁne HI(Y, K, α) in such a way that χ(HI(Y, K, α)) = λCLH(Y, K, α)?


## Page 5


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 5
As the reader may expect, the answers to all of these questions are mostly in the aﬃrmative,
however, we need to point out some details ﬁrst. Our analytical framework will be based again on
the singular gauge theory developed by Kronheimer and Mrowka. In particular this means that
we will use a metric with a cone angle along the knot which will give rise to the structure of an
orbifold.
The reader may be aware that Collin and Steer [9] had developed almost two decades ago a similar
version of instanton Floer homology for knots. Many aspects of our construction are identical to
theirs, however, as Kronheimer and Mrowka point out in [36, Section 1.2.5], unless α = 1/4 (which
corresponds to the case k/n = 1/4 in Collin and Steer’s paper), the diﬀerential needed to deﬁne
the chain complex which gives rise to the Floer groups may be ill-deﬁned, since certain energy
bounds for the moduli spaces cannot be guaranteed, which are needed to appeal directly to some
compactness theorems which will be recalled in Section 4. This is usually referred as saying that for
α ̸= 1/4 we are in a non-monotone situation. Fortunately, as Kronheimer and Mrowka also point
out in that same section of their paper, there is a way to get out of this conundrum provided one
is willing to work with an appropriate local coeﬃcient system. The ﬁnite dimensional analogue of
this situation was ﬁrst studied by Novikov in [47], where an analogue of Morse theory for the case
of circle valued functions on a ﬁnite dimensional manifold was developed.
Although the Chern-Simons functional is typically circle valued (on the space of connections
mod gauge that is), the reason why instanton Floer homology is typically referred as an inﬁnite
dimensional Morse theory, rather than an inﬁnite dimensional Morse-Novikov theory, is that the
monotonicity condition usually holds, so the behavior of the Chern Simons functional is more
similar to the case of ordinary Morse theory and not the slightly more complicated Morse-Novikov
theory. On the other hand, the use of Floer-Novikov theories is certainly not a new thing on the
symplectic versions of Floer homologies, and was ﬁrst investigated by Hofer and Salamon [27] (see
also [41, 60, 22] for more recent, but in no way exhaustive references).
As will be explained in Section 3, there are at least three natural choices of local (Novikov)
systems we could use in our situation, although most of the time we will stick with what we call
the Universal Novikov/Local system, since it seems to require the fewest amount of extra choices
(for functoriality purposes, that is). The end result will be that rather than deﬁning the instanton
chain complex over a vector space, like Q or C, we will need to deﬁne it over a much larger vector
space Λ (the Novikov ﬁeld), but in the end the groups HI(Y, K, α) we will produce continue to be
ﬁnite dimensional over Λ, so formally many statements continue to hold. For example, the Euler
characteristic χΛ(HI(Y, K, α)) of HI(Y, K, α) with respect to the ﬁeld Λ recovers λCLH(Y, K, α).
What seems to be new is the idea that one can also deﬁne a reduced version HIred(Y, K, α) of
these groups, although for the case of α = 1/4, Christopher Scaduto and Aliakbar Daemi had also
realized this independently (and earlier as well [11]). We expect that their techniques could be used
to further understand the family of groups HI(Y, K, α), for arbitrary values of α. In any case, here
is the answer to Question 4.
Theorem 5. Suppose that K is an oriented knot inside an integer homology sphere Y and that a
parameter α ∈Q ∩(0, 1/2) is chosen so that △K(e−4πiα) ̸= 0.
There is a family of vector spaces HIi(Y, K, α) for i ∈Z/4Z , which are ﬁnite dimensional over
a Novikov ﬁeld Λ, and which we will call the instanton Floer-Novikov knot homology groups
of the knot K. They recover the Casson-Lin-Herald invariant (and hence the Tristram-Levine
knot signatures), in the sense that
χΛ(HI(Y, K, α)) = λCLH(Y, K, α) = 4λC(Y ) + 1
2σK(e−4πiα)


## Page 6


Mariano Echeverria
6
where we are using an absolute Z/2Z grading of these Floer groups in order to compute the Euler
characteristic with respect to Λ. Moreover, each such HIi(Y, K, α) admits a reﬁnement HIred,i(Y, K, α),
which again will be a ﬁnite dimensional vector space over the Novikov ﬁeld Λ, and which we will
call the reduced instanton Floer-Novikov knot homology groups of the knot K. Given
these two Floer groups one can deﬁne the Frøyshov knot-invariants
h(Y, K, α) = χΛ(HIred(Y, K, α)) −χΛ(HI(Y, K, α))
For the case of α = 1/4, no Novikov ﬁeld is needed and in fact the Floer groups can be deﬁned over
Q (for example).
Remark 6. In order to be completely accurate, we should specify the cone parameter being used
in the resulting groups, and write HI(Y, K, α, ν), HIred(Y, K, α, ν) and h(Y, K, α, ν). However, we
expect all of these to be independent of ν, which is why we will continue to suppress ν from our
notation.
Some examples/properties of these groups and the knot h-invariants will be discussed in Section
8, but now we have to answer the other part of Question 4, namely, what is the relation between
λF O(X, T, α) and Lef(HI(Y, K, α)) in the case of a self-concordance of a knot?
First of all, we must observe that currently the functoriality properties of the Floer groups
HI(Y, K, α) are weaker than their non-singular counterparts HI(Y ). By this we mean that a homol-
ogy concordance (W, Σ) : (Y1, K1) →(Y2, K2) for which both of HI(Y1, K1, α) and HI(Y2, K2, α)
are deﬁned, may not induce a cobordism map between the Floer groups.
The reason for this
has to do once again with the reducible connections on the cobordism. In the case where Σ is
not present, there are maps between HI(Y1) and HI(Y2) essentially because the trivial connec-
tion θW on the cobordism, which is the unique reducible up to gauge since H1(W; Z) = 0, is
automatically isolated and non-degenerate given that H1(W; gθW ) = H1(W; R) ⊗R3 = 0 and
H2,+(W; gθW ) = H2,+(W; R) ⊗R3 = 0.
In the case of a homology concordance there is still a unique reducible connection θW,α after we
have ﬁxed a choice of α since H1(W\Σ; Z) = Z, but now it is a priori not immediate that it will be
isolated or non-degenerate. The cobordisms for which this will happen will be called α-admissible,
and after we explain more of the setup we are using in sections 2 and 4 it will become clear that
the condition we are after is the following.
Deﬁnition 7. A homology concordance (W, Σ) : (Y1, K1) →(Y2, K2) between two knots K1 ⊂Y1
and K2 ⊂Y2 is a homology cobordism W : Y1 →Y2 together with an embedded annulus Σ : K1 →
K2.
The pair (W, Σ) will be called α-admissible for α ∈(0, 1/2), if △K1(e−4πiα) ̸= 0, △K2(e−4πiα) ̸=
0 and moreover H1(W\Σ; L⊗2
θW,α) = 0.
Here θW,α denotes the unique reducible (up to gauge)
compatible with the holonomy condition α, and E = LθW,α ⊕L−1
θW,α denotes the decomposition of
the trivial SU(2) bundle over W\Σ induced by θW,α.
We will discuss to what extent this condition on the cobordism is really needed at the end of this
section, but for now let’s assume that it holds. In that case it is straightforward to see that we have
cobordism maps HI(W, Σ, α) between HI(Y1, K1, α) and HI(Y2, K2, α) as explained in Section 4.
In order to obtain a splitting formula analogous to the one λF O(X) satisﬁes we need an additional
piece of data. In general, it is more accurate to regard λF O(X, T, α) as a degree zero Donaldson
invariant, associated to the moduli space M(X, T, 0, 0, α), since in practice one needs to perturb
the α-ASD equation F +
A = 0, not the α-ﬂat equation FA = 0, in order to deﬁne λF O(X, T, α).


## Page 7


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 7
Interestingly enough, in the case that α ̸= 1/4, there are other moduli spaces M(X, T, k, l, α)
whose expected dimension is zero (and are a priori non-empty), which means that there are addi-
tional candidates for degree zero Donaldson invariants. As we will explain in more detail in Section
6, whenever k is an integer such that k(1 −4α) ≥0, the moduli space M(X, T, k, −2k, α) is of ex-
pected dimension zero, and can in fact be used to deﬁne a Donaldson-type invariant D0(X, T, α, k)
(see deﬁnition 34 for a precise statement). In particular, we can create a formal power series
(1)
X
k∈Z
D0(X, T, α, k)T −Etop(X,T,k,−2k,α)
where Etop(X, T, k, −2k, α) denotes the topological energy of the moduli space M(X, T, k, −2k, α).
In fact, this energy is equal to the quantity k(1 −4α) which explains the restriction k(1 −4α) ≥0 ,
since negative energy moduli spaces of α-ASD instantons are always empty, just as in the ordinary
case where no holonomy condition is present. Now, the formal power series 1 is in fact the sort
of object a Novikov ﬁeld is equipped to handle, in other words, we can think of the series 1 as an
element of Λ.
This is a good thing, since the Lefschetz number of a degree-preserving linear transformation
L : V →V between two ﬁnite dimensional vector spaces over some ﬁeld F will be an element of F.
In the case of a self-concordance (W, Σ) : (Y, K) →(Y, K) which is α-admissible we should think
of V as being either HI(Y, K, α) (or HIred(Y, K, α)), F as the Novikov ﬁeld Λ and L as the map
on corresponding Floer groups induced by the cobordism. Therefore, one would expect that the
Lefschetz number of the map induced by the self-concordance equals 1.
That will be the case, modulo a ﬁnal caveat. There is an action of H1(X; Z/2) on the mod-
uli spaces M(X, T, k, −2k, α), which has been studied ad nauseam in other situations involving
Instanton Floer homology [5, 50, 51, 53, 54, 35]. Unless the action of H1(X; Z/2) is free on the
irreducible part M∗(X, T, k, −2k, α) of the moduli space, one cannot expect a relationship between
the formal power series and the Lefschetz number to hold, since there will be an ambiguity when
solving the gluing problem, as explained in [35, Section 5]. In fact, it will turn out that the action
of of H1(X; Z/2) on M∗(X, T, k, −2k, α) is free, in which case the splitting (or Lefschetz) formula
2 is essentially a consequence of [35, Proposition 5.5], which in Kronheimer and Mrowka’s situation
comes from the assumption that the subgroup φ∗⊂H1(W ∗, S∗, P∗) (in their notation) satisﬁes a
non-integral condition.
With these remarks in place, we can ﬁnish answering Question 4.
Theorem 8. Let K ⊂Y an oriented knot inside an oriented integer homology sphere and (W, Σ) :
(Y, K) →(Y, K) a self-concordance of K. Consider α ∈Q ∩(0, 1/2) such that △K(e−4πiα) ̸= 0.
If (W, Σ) is α-admissible then there are degree-preserving maps
HI(W, Σ, α) : HI(Y, K, α) →HI(Y, K, α)
HIred(W, Σ, α) : HI(Y, K, α) →HI(Y, K, α)
induced by the cobordism (W, Σ).
If (X, T ) is the pair obtained by closing up (Y, K) then for k ̸= 0 the invariants D0(X, T, α, k) are
always well deﬁned. Moreover, λF O(X, T, α) = D0(X, T, α, 0) can be deﬁned if and only if (W, Σ)
is α-admissible, and the following splitting formula holds
(2)
X
k∈Z
D0(X, T, α, k)T −E(X,T,k,−2k,α) = 2Lef(HI(W, Σ, α)) = 2Lef(HIred(W, Σ, α))−2h(Y, K, α)


## Page 8


Mariano Echeverria
8
Finally, if (X, T ) arises as the closure of another self-concordance (W ′, Σ′) : (Y ′, K′) →(Y ′, K′)
and △K′(e−4πiα) ̸= 0 as well, then
(3)
Lef(HIred(W, Σ, α)) = Lef(HIred(W ′, Σ′, α))
and hence
h(Y, K, α) = h(Y ′, K′, α)
In particular,we can deﬁne a Frøyshov torus invariant h(X, T, α) for the embedded torus as
h(Y, K, α) given an arbitrary “slice” (Y, K).
Remark 9. a) Again, a dependence on the cone angle is implicit.
b) The statement regarding the equality of the Lefschetz numbers 3 will follow the strategy
employed by Frøyshov in the case of λSW (X), which as we mentioned before can be found in [21,
Theorem 8]. The argument is essentially the same, the only thing one needs to verify is a suitable
version of [21, Lemma 10] for the case of matrices with coeﬃcients in a Novikov ﬁeld.
c) Besides the case of λF O(X) and λSW (X), there are other instances where a Lefschetz formula
has appeared in a similar context, in fact, in some ways more closely related to our situation. In
[29] Juhász and Zemke compute the eﬀect of concordance surgery on the Ozsváth-Szabó 4-manifold
invariant. One is given a smooth closed oriented 4-manifold X with b+
2 (X) ≥2 and a homologically
essential torus T ⊂X with trivial self-intersection. If (I × Y, Σ) is a self-concordance of a knot
K ⊂Y , then there is a natural torus TC inside S1 ×Y which they use to construct a 4-manifold XC
generalizing the Fintushel and Stern knot surgery [16]. Namely, one forms the 4-manifold XC =
(X\N(T )) ∪φ WC where N(T ) denotes a tubular neighborhood of T and WC = (S1 × Y )\N(TC),
while φ is a gluing diﬀeomorphism. In (knot) Heegaard-Floer homology there is a concordance map
ˆFC : \
HFK(Y, K) →\
HFK(Y, K)
and an associated graded Lefschetz number
Left(C) =
X
i∈Z
Lef

ˆFC | \
HF K(Y,K,i): \
HFK(Y, K, i) →\
HFK(Y, K, i)

ti
Then Theorem 1.1 in [16] shows that ΦXC;ω = Left1(C)ΦX;ω, where ΦX;ω denotes a version of the
Ozsváth-Szabó 4-manifold invariant twisted by a certain collection of closed 2-forms.
d) Another situation very close to our splitting formula is the one Kronheimer and Mrowka found
for the Seiberg-Witten invariants on a closed 4-manifold [38, Section 32.1]. More precisely, one is
given a closed oriented 4-manifold with b+
2 (X) ≥2 and within it a separating hypersurface Y , so
that X = X1 ∪X2 , ∂X1 = Y and ∂X2 = −Y . If ωX is a 2-form used to perturb the Seiberg
Witten equations on X and ω is the restriction of ωX to X, then for a torsion spin-c structure s
on Y , in general ω will induce a non-balanced perturbation in the sense of [38, Chapter 32], which
essentially means that a Novikov system Λ is required to deﬁne the corresponding monopole Floer
homology groups HM(Y, s, ω). Proposition 32.1.1 in [38] shows that
(4)
X
sX|Y =s
T −Etop
ωX (sX)SW(X, sX) = ⟨ψ+, ψ−⟩ωµ
Here the sum is taking place over all spin-c structures on X which restrict to the given one on Y ,
SW(X, sX) denotes the Seiberg-Witten invariant associated to such a spin-c structure, Etop
ωX is a
perturbed topological energy, and the right hand side denotes a pairing of two relative invariants
(ψ± being an element of HM(±Y, s, ω)), the pairing taking place with respect to the Novikov
ring. Notice that one can interpret our splitting formula 2 as an analogue of the pairing formula 4


## Page 9


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 9
when the 3-manifold is non-separating (rather than separating), and with the Donaldson invariants
(rather than the Seiberg-Witten invariants). From this perspective, the diﬀerent bundles E(k, −2k)
are playing a role analogous to the one the diﬀerent isomorphism classes of spin-c structures play
in the Seiberg-Witten context.
In section 8 we will give some applications of the splitting formula 2, including a proof that
λF O(S1 × Y, S1 × K, α) = 2λCLH(Y, K, α). But as a way to entice the reader, we now prove the
following.
Theorem 10. Suppose that K ⊂Y and K′ ⊂Y ′ are knots and there exists a concordance (C, A) :
(Y, K) →(Y ′, K′) where C is a homology [0, 1] × S3 and A an embedded annulus. Then for any
α ∈Q ∩(0, 1/2) such that (C, A) is α-admissible (if any), we have that h(Y, K, α) = h(Y ′, K′, α),
i.e, the knot h-invariants are α-concordance invariants.
In particular, h(Y ′, K′, α) will vanish whenever K′ is α-slice in the sense that there is an α-
concordance (C, A) : (S3, ◦) →(Y ′, K′), where ◦is the unknot.
Proof. Observe that we can form a self-concordance of the knot (Y, K) obtained by “stacking” (C, A)
with the opposite concordance ( ¯C, ¯A) : (Y ′, K′) →(Y, K) obtained by reversing orientations,
(W, Σ) = ( ¯C, ¯A) ◦(C, A) : (Y, K) →(Y, K)
From (W, Σ) we can close it up to obtain (X, T ). The corresponding closed 4-manifold (X, T ) can
also be obtained from doing the staking in the opposite order, namely (C, A) ◦( ¯C, ¯A), so the last
statement in the splitting formula (Theorem 8) implies that the knot h-invariants are the same, i.e,
h(Y, K, α) = h(Y ′, K′, α)
The last claim follows from the fact that for the unknot, for all α ∈Q ∩(0, 1/2), we have
HI(S3, ◦, α) = HIred(S3, ◦, α) = 0, and hence h(S3, ◦, α) = 0.
□
We conclude this section by mentioning the “ﬂip symmetry” property our Floer groups enjoy (in
the context of singular gauge theory on 4-manifolds it was introduced by Kronheimer and Mrowka,
[32, Lemma 2.12]).
Theorem 11. Let K ⊂Y be an oriented knot inside an oriented integer homology sphere and
choose α ∈Q ∩(0, 1/2) such that △K(e−4πiα) ̸= 0. Then there is a ﬂip isomorphism
F : HI(Y, K, α) →HI

Y, K, 1
2 −α

which is grading preserving, with an analogous isomorphism for the reduced groups HIred(Y, K, α).
In particular,
h(Y, K, α) = h

Y, K, 1
2 −α

Likewise, for a pair (X, T ) we have for all k ̸= 0 that
D0(X, T, k, α) = D0

X, T, −k, 1
2 −α

and a similar statement holds for λF O(X, T, α) whenever it can be deﬁned.


## Page 10


Mariano Echeverria
10
Some Updates. Since the ﬁrst version of this paper appeared on the arxiv, some important
developments have taken place which we now mention. The reader is referred to the section “Some
Speculations and Further Directions of Work” in the ﬁrst version of this paper if interested in some
speculations we had indulged ourselves in.
As mentioned before, λCLH(Y, K, α) = 4λC(Y ) + 1
2σK(e−4πiα), which can be rewritten as
λF O(S1 × Y, S1 × K, α) = 8λF O(S1 × Y ) + σK(e−4πiα)
This suggests that if one could ﬁnd a non-gauge theoretic deﬁnition of a tori signature σT for
T ⊂X, then the formula
(5)
λF O(X, T, α) = 8λF O(X) + σT (e−4πiα)
should hold [assuming that σT is normalized so that σS1×K = σK].
Regarding the non-gauge theoretic deﬁnition of a tori signature, Ruberman [49] deﬁned a signature-
type invariant for embedded tori σT on a homology S1 ×S3, which agrees with the Levine-Tristram
invariant in the product case.
So the question is whether σT satisﬁes formula (5) so that our
conjecture would hold.
In even more recent work, Langte Ma [45, Theorem 1.1] showed that the diﬀerence (whenever
deﬁned)
λF O(X, T, α) −8λF O(X)
equals ˜ρϕ2α(X0(T ), Q), which is a spectral invariant deﬁned by Ma in the spirit of the Atiyah-Singer
ρ invariant. The notation is explained in the introduction of [45], but since ˜ρϕ2α(X0(T ), Q) is a
topological invariant, Ma’s results shows the independence of λF O(X, T, α) on the cone angle being
used. Likewise, Ma shows [45, Theorem 1.2] that
˜ρϕ2α(X0(T ), Q) = σ2α(X, T )
where again the right hand side refers to the invariant deﬁned by Ruberman. Therefore, one can
conclude that [45, Corollary 1.3]
λF O(X, T, α) −8λF O(X) = σ2α(X, T )
Outline of the paper: In section 2 we review the main features of singular gauge theory as
developed by Kronheimer and Mrowka.
Sections 3, 4, 5 discuss how the monotonicity issue arises, the deﬁnition of HI(Y, K, α) and of
HIred(Y, K, α) respectively.
Sections 6 deﬁnes λF O(X, T, α) as well as its relatives D0(X, T, α).
Section 7 discusses the
splitting formula λF O(X, T, α) and D0(X, T, α) satisfy. Finally, section 8 includes some calcula-
tions of λF O(X, T, α) for certain tori inside mapping tori as well as some properties of the groups
HI(Y, K, α) and HIred(Y, K, α), like the usual duality isomorphisms under orientation reversal as
well as the ﬂip symmetry property.
In order to reduce the length of the paper, we deleted an appendix which includes a summary
of cohomology with local coeﬃcients and the Alexander polynomial for CW complexes, which can
still be found in the annotated version of the paper [15].
Acknowledgments:
The gestation and development of this project took place while the author was a visiting student
at the Massachusetts Institute of Technology so I would like to thank the MIT Mathematics De-
partment for their tremendous hospitality. Moreover, I would like to thank Tom Mrowka, Danny
Ruberman and Nikolai Saveliev for several discussions which were indispensable throughout the


## Page 11


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 11
development of the paper, as well as my advisor Tom Mark for his constant encouragement and
useful suggestions. I would also like to thank Langte Ma for pointing out a mistake in an earlier
version of this paper, involving the values of λF O(X, T, α) in the mapping torus case.
I would also like to thank Peter Kronheimer, Chris Herald, Christopher Scaduto, Aliakbar Daemi,
Jianfeng Lin, Matthew Stoﬀregen, Paul Feehan, Raphael Zentner, Jennifer Hom, Michael Usher,
Michael Miller and Donghao Wang for direct and indirect conversations on this project.
2. Review of the Orbifold Setup
As we mentioned in the introduction, the Floer homology we will construct for knots is based on
an orbifold approach, which was pioneered by Kronheimer and Mrowka in their papers on gauge
theory and embedded surfaces [32, 34]. Slightly diﬀerent versions of this setup have been employed
by them over the years [37, 36, 35], so the main purpose of this section is to give a brief review
of their orbifold construction, as well as discussing the advantages and disadvantages of diﬀerent
strategies for building Floer homologies for knots.
Let X be a smooth, oriented, closed four manifold and Σ any oriented, smoothly embedded
surface inside X. Similarly, suppose that Y is a smooth, oriented, closed three manifold and K
is an oriented knot or link inside Y . For either of the pairs (X, Σ), (Y, K), we want to do gauge
theory using connections on an SU(2) bundle which are singular along Σ (or K). The nature of
the singularity is precisely what distinguishes one approach from the other.
A natural strategy would be to work on either of the complements X\Σ , Y \K and to choose a
riemannian metric which is simply the restriction to one of these complements of a smooth metric
g deﬁned on all of X (or Y ). Analytically, this means that one is working on an open manifold
with an incomplete metric, which from the Sobolev package point of view is not a nice situation.
However, provided one works with weighted Sobolev spaces, one can still deﬁne a reasonable family
of function spaces [32, Section 3 (i)].
The next issue is whether one wants to work with an SU(2) bundle E which is deﬁned only on
the complement X\Σ (respectively Y \K). In this case the major problem is how to recover useful
topological information. This was called the extension problem by Kronheimer and Mrowka, and
discussed in some detail in [32, Section 2 (iv)].
The setup used in [32, 34, 36], which will follow as well, is one for which the bundle E is deﬁned
over the entire manifold X (or Y ), subject to the condition that topologically the bundle E admits
a reduction to a U(1) bundle along Σ (or K). For example, this means that for (X, Σ) an SU(2)
bundle E should decompose as
(6)
E |ν(Σ)= L ⊕L∗
where ν(Σ) is a closed tubular neighborhood of Σ , and L →ν(Σ) some complex line bundle com-
patible with the hermitian metric. In particular, this allows us to deﬁne two topological invariants,
the instanton number k
(7)
k = c2(E)[X]
as well as the monopole number l
(8)
l = −c1(L |Σ)[Σ]
Notice that the latter invariant is not present when Σ = ∅.
The reader may be interested in
knowing that for their “Khovanov is an unknot-detector” paper Kronheimer and Mrowka do work
with bundles which in principle are not deﬁned over the entire manifold [35, Section 2.1].


## Page 12


Mariano Echeverria
12
For the 3-manifold case, the bundle topology is not very interesting in our situation so we can
consider E simply as the trivial SU(2) bundle over Y , i.e, E = Y × SU(2), together with the trivial
U(1) sub-bundle corresponding to the diagonal embedding of U(1) in SU(2). In both cases what
we will be more interesting is the space of connections we will use, which we now describe.
These connections have the following singular behavior: after choosing a riemannian metric we
consider ν(Σ) as being diﬀeomorphic to the unit disk bundle of the normal bundle, and we choose
a connection 1-form iη for the circle bundle ∂ν(Σ), so that it coincides with the 1-form dθ on each
circle ﬁbre, where (r, θ) are polar coordinates in some local trivialization of the disk bundle (dr ∧dθ
orients the normal planes). By radial projection η is extended to ν(Σ)\Σ.
For each real number 0 < α < 1/2, we consider the matrix 1-form with values in su(2) which
behaves near Σ as
i
 α
0
0
−α

dθ
Locally, the holonomy of a connection A on X\Σ whose matrix connection coincides with the
previous matrix 1-form near Σ on the positively-oriented small circles of constant r is approximately
(9)
exp

−2πiα
0
0
2πiα

We are excluding the values α = 0, 1/2 because those cases give no new information, i.e, they
essentially correspond to the situation where the connections extend smoothly across the singularity
(as SU(2) or SO(3) connections more generally).
For a more global description, using the reduction (6), choose any smooth SU(2) connection A0
on E which reduces in the same way, i.e,
A0 |ν(Σ)=

b
0
0
−b

where b is a smooth connection on L. Deﬁne the model connection Aα on E |X\Σ as
(10)
Aα = A0 + iβ(r)
 α
0
0
−α

η
where β is a smooth cut-oﬀfunction equal to 1 in a neighborhood of 0 and equal to 0 for r ≥
1/2.
The model connection has holonomy around small linking circles asymptotically equal to
(9). The connections Kronheimer and Mrowka consider can be written as A = Aα + a, where
a ∈Ω1(X\Σ, su(2)), and as always necessary Sobolev spaces are needed [32, Eq. 2.2, 2.3].
Remark 12. In the 3-manifold case we can take A0 to be the (usual) trivial connection θ on the trivial
SU(2) bundle E from before. In the nomenclature of [35, Section 3.6], our situation corresponds to
one where △is trivial, where △is a local system determining the possible extensions of the bundle
across the singularity.
Most of the usual gauge theory technology can be extended to this setup: for example, one can
deﬁne moduli spaces of ASD connections with the singular behavior described before, compute
the expected dimension of the moduli space, as well as the energy of the connection in terms of
topological quantities. These moduli spaces are indexed by the instanton and monopole number,
so we will write them typically as M(X, Σ, k, l, α) or M(k, l), depending on the context.
We will remind the reader about the precise formulas once we explain the monotonicity condition
usually required before deﬁning Floer homologies. For now, it suﬃces to say that there is one key
aspect missing by working in the previous setup described. Namely, Kronheimer and Mrowka were


## Page 13


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 13
not able to show that if one has a sequence of ASD connections Ai belonging to some moduli space
M(X, Σ, k, l, α), then the limiting connection A∞, which in principle belongs to a diﬀerent moduli
space M(X, Σ, k′, l′, α) because of Uhlenbeck bubbling, must belong to a moduli space of lower
expected dimension. The fact that this should happen, that is, that after bubbling one should land
in a moduli space of smaller dimension, would follow if Conjecture 8.2 in [32] were proven true.
Fortunately, they were able to prove this fact by modifying slightly the previous setup and working
instead with orbifolds.
On a ﬁrst level, this means that instead of using the restriction of a smooth metric on X (or Y )
to X\Σ (or Y \K), we consider metrics which have a cone-like singularity along the surface (knot)
[32, Section 2, iii)]. This means that near the surface Σ, the metric is modeled on
ds2 = du2 + dv2 + dr2 +
 1
ν2

r2dθ2
where u, v are coordinates on Σ, and ν ≥1 is a real parameter. To obtain a global metric on ν(Σ)
of this form replace du2 + dv2 by the pull-back of any smooth metric on Σ, and replace the form
dθ by the 1-form η. The metric is then patched to a smooth one on the complement of ν(Σ) and
extended to the rest of X. The resulting metric has a cone-angle of angle 2π/ν in the normal planes
to Σ. When ν is an integer greater than 1 the metric is an orbifold metric: locally there is a ν-fold
branched cover on which the metric is smooth.
An advantage of the orbifold perspective is that it allow us to compute certain quantities (like
gradings for the generators of the Floer complex) in terms of equivariant indices on appropriate
branched covers along the knot (and/or surface). Moreover, in the orbifold setup one can still use
a Coulomb slice determined explicitly by ker ˇd∗
A , whereˇemphasizes that we are thinking of this
operator as being deﬁned on an orbifold. If we were to use instead the non-orbifold setup (with the
smooth metric and the weighted Sobolev spaces mentioned before), then the construction of the
slices is more subtle because of the lack of the usual d∗
A operator [32, Lemma 5.5].
However, as we pointed out in the introduction, a drawback of the orbifold approach is that cur-
rently there is no way to show that the groups one obtains are independent of the choice of orbifold
structure (cone angle) one uses. Moreover, each value of holonomy α determines an allowable set of
possible orbifold cone angles ν compatible with α one can use for deﬁning the Floer groups. These
values are described in Proposition 4.8, Lemma 4.9 (and the remark after it), as well as Proposition
4.17 of [32].
In practice we can think of the allowable ν in the following way [36, Remark p.894]. If our
holonomy parameter is a rational number α ∈Q ∩(0, 1/2), then ν > 0 can be taken to be any
integer satisfying the property that
(11)
exp

−2πiαν
0
0
2πiαν

∈Z(SU(2)) = ±Id2×2
Therefore, if we write α as p
q , where p, q are relatively prime, it is not diﬃcult to see from this
description that taking ν = q suﬃces.
However, if q happens to be even, then in fact ν =
q
2
also satisﬁes the condition 11. This is why for α = 1
4 one can choose ν = 2 , so that the metric
has a cone angle π along the knot (a bifold in the terminology of Kronheimer and Mrowka [37]).
If one is annoyed by this dependence on the cone angle, it is reasonable to choose the smallest
cone parameter ν that works for α as the “canonical” cone angle. Incidentally, notice that the this
canonical cone angle works simultaneously for α and 1
2 −α so that the ﬂip symmetry α →1
2 −α
can be analyzed with this common choice.


## Page 14


Mariano Echeverria
14
Remark 13. Besides describing the singular metric in the orbifold setup, one can also adapt the
notion of bundle and connections to this situation. The deﬁnitions given in [37] are particularly
convenient for our purposes (it also has the advantage of being suitable for the case that the bundle
does not extend across the singularity, which as we said is more general than what we will consider).
Every point in an orbifold has a neighborhood U which is the codomain of an orbifold chart
φ : ˜U →U
The map φ is a quotient map for an action of a ﬁnite group, which in our case will be either trivial
or Zν. A C∞SU(2) orbifold connection with respect to (X, Σ) (or (Y, K)) means an oriented
C2 vector bundle E over X\Σ (respectively Y \K) with an SU(2) connection A having the property
that the pull-back of (E, A) via any orbifold chart φ : ˜U →U extends to a smooth pair ( ˜E, ˜A) on
˜U.
If we have two SU(2) bifold connections (E, A) and (E′, A′), then an isomorphism between
them is a bundle map τ : E →E′ over X\Σ (respectively Y \K) such that τ ∗(A′) = A. The
group ΓE,A of automorphisms of (E, A) can be identiﬁed with the group of parallel sections of
the associated bundle. It is isomorphic to either the trivial group, the circle U(1) embedded as a
maximal torus inside SU(2), or all of SU(2).
Now that we have explained the geometric setup, we will describe of the space of connections
and gauge transformations that we will be working with, in the spirit of [36]. Suppose there is
an oriented link K inside an integer homology sphere Y . For α ∈Q ∩(0, 1/2) consider the model
connection Bα described before (10). We will typically use B when referring to connections deﬁned
on three-dimensional manifolds from now on. At the same time we choose an orbifold metric gν
compatible with α in the sense we mentioned before.
We will usually follow the convention of Kronheimer and Mrowka, and use theˇnotation when we
want to emphasize that the orbifold metric is being used in a speciﬁc construction. Hence, ˇLp
m,Bα
will denote the Sobolev spaces using the Levi-Civita derivative of gν and the covariant derivative
of Bα on gP . Taking p = 2 and an integer1 m > 2, the space of connections to be considered is
C(Y, K, α) =

B = Bα + b | b ∈ˇL2
m,Bα(T ∗Y |Y \K ⊗gP)
	
The gauge group G(Y, K, α) consists of those automorphisms of E which preserve the reducibility
of the model connection Bα. In fact, G(Y, K, α) turns out to be independent of α (and cone angle
used) so we will just denote it as G(Y, K).
Here is an useful way to think about G(Y, K) [34,
Appendix I]:
Let GK(Y, K) denote the subgroup of G(Y, K) consisting of those gauge transformations which
are the identity over K. Let GK(Y, K) denote the space of gauge transformations of the line bundle
L →K, that is, the space of maps from K to U(1). Then there is an exact sequence
(12)
1 →GK(Y, K) →G(Y, K) →r GK(Y, K) →1
In particular, we can think of G(Y, K) as the space of maps g : Y →SU(2) satisfying g(K) ⊂
U(1) ⊂SU(2). Moreover, GK(Y, K) is weakly homotopy equivalent to the space of smooth gauge
transformations which are the identity over a suﬃciently small neighborhood of the knot K. From
this we can see that for knots the topological information of the map g is carried by two integers,
corresponding to the degrees of g : Y →SU(2) and g |K: K →U(1).
1We denote this integer by m instead of k to avoid confusion with the instanton number k.


## Page 15


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 15
More generally, if the link K has r components, the space of components π0 (G(Y, K)) is isomor-
phic to [36, Section 3]
Z ⊕Zr
Also, there is a preferred homomorphism
(13)
d : G(Y, K) →Z ⊕Z
where the map to the second factor is obtained by taking the sum of all the entries in the factor
Zr. After introducing Sobolev completions, we will take our gauge group to be
G(Y, K) =

g | g ∈ˇL2
m+1,Bα(Aut(P))
	
The space of connections C(Y, K, α) is an aﬃne space, and on the tangent space TBC(Y, K, α) we
deﬁne an inner product (independent of B) by
⟨b, b′⟩L2 =
Z
ˇY
−tr(ad(∗b) ∧ad(b′))
where we are using the Killing form to contract the Lie algebra indices, and the Hodge star on Y
and the wedge product to contract the form indices. It is important to notice that the Hodge star
is the one deﬁned by the orbifold metric gν.
The Chern-Simons functional on C(Y, K, α) is deﬁned to be the unique function
CS : C(Y, K, α) →R
satisfying CS(Bα) = 0 and having gradient (with respect to the above inner product)
(gradCS)B = ∗FB
From this one obtains2
CS(Bα + b) =< ∗FBα, b >L2 +1
2 < ∗dBαb, b >L2 +1
6 < ∗[b ∧b], b >L2
The critical points B of CS then satisfy FB = 0. When restricted to Y \K , this gives rise to a
representation (here y0 is a base-point in the complement of the knot or link)
ρ : π1(Y \K, y0) →SU(2)
satisfying the constraint that for each oriented meridian µK, ρ(µK) is conjugate to
(14)
ρ(µK) ∼

exp(−2πiα)
0
0
exp(2πiα)

There is one such conjugacy class for each component of K, once the components are oriented.
As usual in the gauge theory context, we will need to perturb the ﬂatness equation (in fact, the
Chern-Simons functional) to obtain the necessary transversality properties for the moduli spaces.
The perturbations that we will use are described in section 3.2 of [36]. As we will see soon, the
support of these perturbations must stay away from the knot if we want to appeal to the relationship
Herald found between the count these ﬂat connections (modulo conjugacy) and the knot signatures
[26]. Kronheimer and Mrowka had to address a similar problem in their paper on Tait colorings
[37], although for diﬀerent purposes.
Before discussing this support condition, we will explain next how the monotonicity issue arises
when one tries to deﬁne a version of Instanton Floer homology for an arbitrary value of α.
2Notice that there is a factor of 1
2 missing in the last term of the formula in [36, Eq. 67].


## Page 16


Mariano Echeverria
16
3. Monotonicity and Novikov Systems
As usual, we would like to do “Morse theory” on
B(Y, K, α) = C(Y, K, α)/G(Y, K)
Notice that since G(Y, K) is independent of α, ν and C(Y, K, α) is contractible, the homotopy type of
the space B(Y, K, α) is independent of α, ν. As in the case when K is not present, the Chern-Simons
functional is no longer single-valued on B(Y, K, α). In fact CS is invariant only under the identity
component of the gauge group. If B ∈C(Y, K, α) is a connection and g a gauge transformation, we
can use the latter to form the bundle S1 ×g E over S1 × Y together with its reduction over S1 × K,
deﬁned by Bα. Then the map d from (13) becomes
d(g) = (k, l) ∈Z ⊕Z
where k and l are the instanton and monopole numbers respectively. In this case we have [36, p.
874]
(15)
CS(B) −CS(g(B)) = 32π2(k + 2αl)
More generally, we deﬁne for a path γ : [0, 1] →C(Y, K, α) the topological energy as twice the
drop in the Chern Simons functional, so that the last equation implies that a path from B to g(B)
has topological energy
(16)
E(k, l) = 64π2(k + 2αl)
For a path that formally solves the downward gradient-ﬂow equation for CS on C(Y, K, α), the
topological energy coincides with the modiﬁed path energy
Z 1
0
(∥˙γ(t)∥2 + ∥gradCS(γ(t))∥2)dt
Before comparing E(k, l) with the formula for the grading of two ﬂat connections, we discuss the
perturbations needed to achieve transversality, which involve using holonomy perturbations.
These will be the same as in [36, Section 3.2], and we will give more details about them in the next
section, where we will need to keep track on certain estimates involving their norms. The basic idea
is that each holonomy perturbation gives rise to a cylinder function
f : C(Y, K, α) →R
which depends on an l-tuple
q = (q1, · · · , ql)
of immersions qi : S1 × D2 →Y \K, i = 1, · · · , l and an SU(2)-invariant function h on SU(2)×l via
the formula
f(B) =
Z
D2 h(Holq(B))µ
Here µ is a non-negative 2-form supported in the interior of D2 and having integral 1. We assume
that h is invariant under the action of SU(2) on each of the l factors separately (see the remark
after deﬁnition 3.3 in [36]). It follows that each cylinder function is invariant under the full gauge
group, not just the identity component.
The space of perturbations one uses to achieve transversality involves taking a countable collec-
tion of cylinder functions with an l1 notion of convergence [36, Deﬁnition 3.6]. If P denotes the


## Page 17


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 17
Banach space of perturbations, then p ∈P induces a function fp, and the perturbed Chern-Simons
functional we consider is
CSp = CS + fp
The critical points are now connections satisfying the equation
∗FB + Vp(B) = 0
where Vp is the formal gradient of fp with respect to the L2 inner product. Proposition 3.10 in
[36] states that there is a residual subset of P such that, for all p all the irreducible critical points
of CS + fp are non-degenerate (we will return to the reducibles momentarily). The perturbed
topological energy is then deﬁned for a path γ : [0, 1] →C(Y, K, α) as
(17)
Ep(γ) = 2 ((CS + fp)(B(t0)) −(CS + fp)(B(t1)))
Notice that because the perturbations are invariant under the full gauge group, for a path from B
to g(B), the term fp(B) −fp(g(B)) will cancel, so the perturbed topological energy Ep on loops has
the same expression as the unperturbed case, namely, equation (16).
Returning to the grading question, deﬁne the (perturbed) Hessian of a connection B ∈C(Y, K, α)
as
(18)
HessB,p(b) = ∗dBb + DV |B (b)
where b ∈TBC(Y, K, α) and the (perturbed) extended Hessian [36, p. 881]
(19)
\
HessB,p =

0
−d∗
B
−dB
HessB,p

: ˇL2
j(Y ; gP ) ⊕Tj →ˇL2
j−1(Y ; gP ) ⊕Tj−1
To clarify the notation, here j ≤m is an integer, ˇL2
j(Y ; gP ) is a shorthand for ˇL2
j,Bα(Y \K; gP |Y \K),
and Tj is shorthand for sections of TBC(Y, K, α) with regularity Sobolev ˇL2
j−1,Bα .
For two irreducible, non-degenerate (perturbed) ﬂat connections B0, B1 ∈C(Y, K, α), the rela-
tive grading
gr(B0, B1) ∈Z
will be deﬁned by taking a path B(t) in C(Y, K, α) from B0 to B1 and letting gr(B0, B1) be equal to
the spectral ﬂow of the 1-parameter family d
HessB(t),p. This number only depends on the endpoints
and not the path since C(Y, K, α) is contractible. If
[β0] = [B0],
[β1] = [B1]
are the corresponding gauge equivalence classes in B = B(Y, K, α), then [B(t)] determines a path
ζ from [β0] to [β1], deﬁning a relative homotopy class z ∈π1([β0], B, [β1]). This relative homotopy
class only depends on B0, B1. Conversely, for a relative homotopy class of paths from [β0] to [β1],
we deﬁne
grz([β0], [β1]) ∈Z
via the above procedure.
For the case of a closed loop z based at a point [β] ∈B(Y, K, Φ), we obtain an element inside
π1(B(Y, K, α)) ≃π0(G(Y, K, α)). Lemma 3.14 in [36] shows that
(20)
grz([β], [β]) = 8k + 4l
where we think of z as being speciﬁed by a gauge transformation g as before, and d(g) = (k, l).
From this grading formula we can see that grz([β], [β]) ≡0 mod 4, which means that the Floer
homology we will deﬁne is Z/4Z graded. We will eventually show how to promote this relative


## Page 18


Mariano Echeverria
18
grading to an absolute grading. More importantly, comparing the energy and grading formulas on
loops we can see that
(21)
E(k, l) = 8π2grz([β], [β]) + 32π2l(4α −1)
which means that the only way for E(k, l) and grz([β], [β]) to be proportional regardless of the value
of (k, l) is if α = 1
4.
To explain what happens when α ̸= 1/4, we recall Proposition 3.23 in [36]. Let Mz([β0], [β1])
denote a connected component of the moduli space of ASD connections on R × Y limiting to [β0]
as t →−∞and [β1] as t →∞(with suitable perturbations thrown into the picture to guarantee
transversality).
Proposition 14. ([36, Proposition 3.23]) Given any C > 0, there are only ﬁnitely many [β0], [β1]
and z for which the moduli space Mz([β0], [β1]) is non-empty and has topological energy Ep(γ) at
most C.
Now suppose one wants to deﬁne the diﬀerential via the usual formula
∂[β0] =
X
[β1]|gr([β0],[β1])=1
X
z
nz([β0], [β1])[β1]
where we are taking the sum over all moduli spaces Mz([β0], [β1]) which are one-dimensional and
nz([β0], [β1]) ∈Z denotes the number (with orientations included) of trajectories inside the zero-
dimensional (compact) space ˇ
Mz([β0], [β1]) = Mz([β0], [β1])/R. The issue is that for ﬁxed [β1], the
sum
X
z
nz([β0], [β1])[β1]
could be inﬁnite! To see why, suppose that z, z′ represent two trajectories from [β0] to [β1] with
Mz([β0], [β1]) and Mz′([β0], [β1]) one dimensional. Then z−1 ◦z′ represents a loop based at [β0]
with grz−1◦z′([β0], [β0]) = 0. From (21) we see that the topological energy of this loop must be
32π2l(4α −1), which is a priori unbounded since α ̸= 1/4 and the monopole number l can in
principle be any integer. Since Ep(z) −Ep(z′) diﬀer (up to sign) by 32π2l(4α −1), we see there is
no way to guarantee the assumptions in Proposition (14).
The way to get out of this conundrum is via a Novikov system, but ﬁrst we recall a few facts
about the construction of homology groups using local coeﬃcients. A good reference for the
general construction is [12, Chapter 5]. We will use Γ to denote a local systems of coeﬃcients.
Also, if [β] ∈B(Y, K, α) , then o([β]) will denote3 the 2-element of orientations for [β] [36, Section
3.6].
Suppose that to each [β] we assign an abelian group Γ[β] and for each homotopy class of paths
z from [β0] to [β1] there is an isomorphism Γz from Γ[β0] to Γ[β1] satisfying the usual composition
law for paths.
Deﬁne the chain group C∗(Y, K, α; Γ) generated by irreducible critical points [β] of CSp as
C∗(Y, K, α; Γ) =
M
[β]∈C
Zo([β]) ⊗Γ[β]
3The notation Kronheimer and Mrowka use for the system of orientations is Λ([β]) but we will use Λ for the
Novikov ﬁeld so a sacriﬁce had to be made somewhere.


## Page 19


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 19
and the boundary map as
(22)
∂=
X
([α],[β],z)
X
[ ˇ
A]
ǫ[ ˇA] ⊗Γz
where [A] ∈Mz([β0], [β1]) belongs to a 1-dimensional space, [ ˇA] denotes the connection modulo
the R action, and
ǫ[ ˇA] : o[β0] →o[β1]
is an isomorphism obtained by comparing orientations. Written diﬀerently, we can think of the
diﬀerential as
∂(e) =
X
[β1]∈C
X
z
nz([β0], [β1])Γz(e),
e ∈Γ[β0]
which we will occasionally write as
∂[β0] =
X
[β1]∈C
X
z
nz([β0], [β1])Γz[β1]
After choosing trivializations for o([β0]) and o([β1]), the contribution for a given pair of critical
points in the diﬀerential takes the form
X
z
nzΓz
where z runs through all relative homotopy classes satisfying the conditions
grz([β0], [β1]) = 1
Now, deﬁne the support
sup([β0], [β1]) = {z | nz ̸= 0}
By Proposition (14), for all C, the intersection
sup([β0], [β1]) ∩{z | Ep(z) ≤C}
is ﬁnite. In the notation of deﬁnition 30.2.2 in [38], we will deﬁne a c-complete local system of
coeﬃcients which will allow us to make sense of inﬁnite sums like P
z nzΓz.
A deﬁnition of the c-complete condition can be found in our annotated version [15, Deﬁnition
18], as well as some additional details. For our purposes we will be content with describing the
c-complete local system we will be using throughout the paper, based on [38, Section 30.2], [27,
Section 4], [41, Section 2.2], [59] and [60, Section 2.1].
In fact, there are a couple of natural c-complete systems one could use, but in order to minimize
the number of auxiliary choices we have to make, we will stick with a particular local system which
we will call the universal Novikov ﬁeld/local system [60, Section 4]. Moreover, the universal
Novikov ﬁeld/local system has the advantage that the ﬁbers Γ[β] assigned to each [β] is independent
of α (which does not happen for the other candidates), so it might be a more suited candidate if
one wanted to compare the Floer homologies corresponding to diﬀerent values of α (though Γz will
depend on α which is to be expected as we will see in a moment).
First of all, if F is a ground ﬁeld and Γ ≤R an additive subgroup, then the Novikov ﬁeld ΛF,Λ
associated to F, Λ is
ΛF,Γ =
(X
r∈Γ
arT r | ar ∈F and #{r | ar ̸= 0, r > C} < ∞for all C ∈R
)


## Page 20


Mariano Echeverria
20
In other words, we allow inﬁnitely many terms in the negative direction. The example we will have
in mind most of the time is F = Q or F = C.
Now write π1(B) = π1(B(Y, K, α)) = Z ⊕Z, and consider the universal covering ˜B(Y, K, α) of
B(Y, K, α). This is the space we obtain after taking the quotient of C(Y, K, α) using only gauge
transformations g ∈G(Y, K) which satisfy d(g) = (0, 0) (so they are in the connected component
of the identity gauge transformation). The Chern-Simons functional CS becomes real valued on
˜B(Y, K, α) so we can regard it as a map
CS : ˜B(Y, K, α) →R
In this context ˜β ∈˜B(Y, K, α) will denote a lift of [β] ∈B(Y, K, α). On π1(B(Y, K, α)) we can also
deﬁne the period homomorphism
△CS : π1(B(Y, K, α)) →R
g →64π2(k + 2αl)
d(g) = (k, l)
as well as the spectral ﬂow map
sf : π1(B(Y, K, α)) →Z
z →sf(z)
whose kernel is the annihilator
Ann = ker sf ⊂π1(B(Y, K, α))
We also deﬁne the additive subgroup of R
I = im△CS ⊂R
The diﬀerent local systems we will now explain depend on how they are related to I, and each has
their own set of advantages and disadvantages.
• Minimal Novikov ﬁeld/Local System: here we work with Novikov ﬁeld ΛF,I′, where I′ is
deﬁned as
I′ = △CS(Ann)
Recalling the formula 20 for the grading, this means that we must evaluate △CS on those loops for
which
8k + 4l = 0
so in fact
I′ = {64π2k(1 −4α) | k ∈Z}
The appealing feature of ΛF,I′ is that when α = 1/4 (the monotone case), I′ collapses to {0}, in
which case working over ΛF,I′ is the same as working over F, as should be the case in the monotone
situation. The local system associated to ΛF,I′ will assign to each conﬁguration [β] a copy of ΛF,I′,
i.e, Γ[β] = ΛF,I′. To specify what happens on paths, i.e, what the maps Γz : Γ[β0] →Γ[β1] should
be, observe that since △CS : π1(B(Y, K, α)) →R is a homomorphism whose domain is a ﬁnitely
generated abelian group and whose image is torsion free, there is an exact sequence
ker △CS ֌ π1(B(Y, K, α)) ։ I
which splits, so π1(B(Y, K, α)) can be identiﬁed with ker △CS ⊕I, i.e,
(23)
π1(B(Y, K, α)) ≃ker △CS ⊕I


## Page 21


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 21
By the same token, there is an exact sequence
ker sf ֌ π1(B(Y, K, α)) ։ 4Z
which splits, so π1(B(Y, K, α)) can be identiﬁed with Ann ⊕4Z, i.e
(24)
π1(B(Y, K, α)) ≃Ann ⊕4Z
This allows us to construction a projection
p : I →I′
as follows. Regard I as a subset of π1(B(Y, K, α)) under the ﬁrst identiﬁcation 23. Then using the
second identiﬁcation 24, project I onto Ann and let p be △CS of this element. In other words
p(i) = △CS(πAnn(i))
Now, we can deﬁne Γz on loops as multiplication by T p(−Etop(z)). Fixing the map Γz on loops is
enough to pin down the local system up to isomorphism. The “issue” with this option is that it is
not obvious how the resulting Floer groups depend on the choice of projection p. In fact, we were
unable to write explicitly a projection p, so if one ever wanted to compute explicitly the resulting
homology groups, it is not clear what to do in this circumstance.
• Strongly c-complete Novikov ﬁeld/Local System: we call this intermediate case strongly
c-complete in analogy with the examples given by Kronheimer and Mrowka in [38, Section 30.2].
In this case we use ΛF,I (so I instead of I′) as the Novikov system and a local system which assigns
to [β] a copy of ΛF,I, i.e, Γ[β] = ΛF,I. On loops Γz will act as multiplication by T −Etop(z). Notice
that this system has the advantage that we no longer need to choose a projection p. However, in
order to specify actual groups (and not groups up to isomorphisms), further choices are needed,
since knowing how Γz is deﬁned on loops is not enough to specify a unique formula for how it
should act on paths. More precisely, for a path z : [β0] →[β1] we would like Γz : Γ[β0] →Γ[β1]
to be multiplication by T −Etop(z). However, notice that even for a simple element inside Γ[β0] like
T △CS(g) , for g ∈π1([β0], B(Y, K, α), [β0]) , there is no reason why we must have that ΓzT △CS(g) =
T −Etop(z)+△CS(g) can be written as T △CS(g′) for some g′ ∈π1([β1], B(Y, K, α), [β1]). However, with
additional choices we make sense of this formula. Namely, suppose that we choose a preferred lift
˜β for each [β] ∈B(Y, K, α). Then from formula (15) we have that △CS(g) = 2

CS(˜β) −CS(g ˜β)

,
which means that an element inside Γ[β0] can be rewritten as a formal power series
X
r=△CS(g)
crT △CS(g) = T 2CS( ˜β0)
X
r=△CS(g)
crT −2CS(g ˜β0)
Then Γz = Γz, ˜β0, ˜β1 can be taken to be
Γz, ˜β0, ˜β1


X
r=△CS(g)
crT △CS(g)

≡T 2CS( ˜β1)
X
r=△CS(g)
crT −2CS(z·g· ˜β0)
Notice that we added the “basepoints” in our notation to make it clear that an additional choice is
needed. Here z · g · ˜β0 means the following: regard g · ˜β0 as an element in ˜B(Y, K, α), projecting
to [β0] ∈B(Y, K, α), and use the path z to determine a (unique) element z · g · ˜β0, projecting to
[β1] ∈B(Y, K, α). Moreover, this formula uses implicitly the fact that if r = △CS(g) = △CS(g′) ,
i.e, CS(g′ ˜β) = CS(g ˜β) or equivalently g′ ◦g−1 ∈ker △CS, then CS(z · g · ˜β0) = CS(z · g′ · ˜β0). In
any case, these extra choices of basepoints will not make our lives any easier and do not gives us


## Page 22


Mariano Echeverria
22
much of an advantage, so we will prefer to use the universal Novikov/ local system, which we will
describe next.
• Universal Novikov ﬁeld/Local System: as the name suggests, here we are working with
ΛF,R. The local system assigns [β] a copy of ΛF,R, i.e, Γ[β] = ΛF,R. In order to deﬁne Γz for a path
z : [β0] →[β1], we lift z to a path ˜z : ˜β0 →˜β1 on the universal cover ˜B(Y, K, α) (where again CS
is real valued), and deﬁne
Γz ≡multiplication by T −2(CS( ˜β0)−CS( ˜β1))
The factor of 2 in the exponent is chosen so that on loops it acts as multiplication by T −Etop(z).
Because of the gauge invariance of the perturbation p we could also write this as
T −2(CSp( ˜β0)−CSp( ˜β1))T −2(fp([β1])−fp([β0]))
Notice that the second term is independent of the lift of [β0], [β1]. In a way, it would have been
more tempting to let Γz depend on the perturbation being used and deﬁne Γz,p as multiplication
by T −2(CSp( ˜β0)−CSp( ˜β1)). This would give the advantage that for gradient ﬂow-lines the exponent
−2(CSp(˜β0) −CSp(˜β1)) would always be negative, hence making automatic the condition that the
diﬀerential is well deﬁned on the chain complex. However, once we analyze the case of cobordisms,
it is more tricky to ﬁgure out what the right notion of perturbed topological energy is, given that we
have to use many diﬀerent kinds of holonomy perturbations, so this monotonicity property would
not be automatic anyways. In other words, there is no way to avoid the fact that some control
on the perturbations has to be imposed, and this is precisely what we will do in the next section
(based on ideas from [10]).
4. Floer-Novikov Homology and its Relationship To the Knot Signature
Recall that for the construction of the usual instanton Floer homology groups on an integer
homology sphere Y [17], the chain complex CI(Y ) is generated by (perturbed) irreducible ﬂat
connections and the proof that the diﬀerential ∂on CI(Y ) squares to zero requires showing that
no broken ﬂow lines can factorize through the trivial ﬂat connection θ, which cannot be eliminated
through the use of perturbations.
Moreover, the proof that the homology HI(Y ) one obtains does not depend on the choice of
metric and perturbations, requires using the fact that as we deform this data, we do not meet
reducibles, since once again they are singular points in the space of connections mod gauge.
To show these properties one uses the fact that the stabilizer of the trivial connection θ is
positive dimensional and that the trivial connection is isolated from the irreducible (perturbed)
ﬂat connections. Even if there were no need for using local coeﬃcients suitable analogues of these
results are needed in our situation, which is what we will proceed to discuss next.
Recall that the critical points B of the unperturbed Chern-Simons functional CS on (Y, K, α)
can be interpreted as ﬂat connections on Y \K, which modulo gauge will correspond to conjugacy
classes of representations
ρ : π1(Y \K, y0) →SU(2)
Since H1(Y \K; Z) ≃Z[µK] regardless of the pair (Y, K), the abelian representations of π1(Y \K, y0)
are completely determined by their action on an oriented meridian µK of the knot K, which we


## Page 23


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 23
already required to be conjugate to the matrix
ρ(µK) ∼
 exp(−2πiα)
0
0
exp(2πiα)

In other words, for any ﬁxed choice of α, there is only one reducible critical point of the unperturbed
Chern-Simons functional CS, which we denoted previously as [θα].
In general, a representation ρ : π1(Y \K, y0) →SU(2) will determine a local coeﬃcient system
gρ on Y \K, with ﬁber g = su(2). In turn this gives rise to cohomology groups Hi(Y \K; gρ). If we
identify ρ with a ﬂat connection B, then its gauge orbit [B] being isolated among the set of critical
points C of CS is equivalent to B being non-degenerate, that is, the kernel of the map
(25)
ker : H1(Y \K; gρ) →H1(µK; gρ)
is zero, where here µK is a collection of loops representing the meridians of all the components of
K (which will be one since we are focusing on the case of a knot).
Here is an explanation of this condition as well of the notation. The map (25) is simply the one
induced in cohomology by the inclusion of µK ֒→Y \K. When B is an irreducible ﬂat connection,
Lemma 3.13 in [36] shows that this condition is equivalent to the extended Hessian d
HessB deﬁned
in (19) being invertible.
At the reducible ﬂat connection θα, one can still use (25) as the criterion for being isolated, the
only thing that changes is that this condition does not imply that the extended Hessian d
Hessθα
is invertible, since at reducibles connections it will always have a non-trivial kernel [14, Section
2.5.4]. To better understand the requirement (25) at the reducible θα, notice that the Lie algebra
gθα ≃su(2) ≃so(3) decomposes as
gθα ≃R ⊕L⊗2
α
where E = Lα ⊕L−1
α
is the decomposition of the SU(2) bundle induced by θα. Hence
H1 (Y \K; gθα) ≃H1(Y \K; R) ⊕H1(Y \K; L⊗2
α ) = R ⊕H1(Y \K; L⊗2
α )
One should think of the R summand as being the directions in the Zariski tangent space ob-
tained from deforming the value of the holonomy α. Given that α is ﬁxed for our problem and
H1(Y \K; R) →H1(µK; gρ) is an injection since H1(µK; gρ) ≃H1(µK; R) [15, Lemma 63], the
condition (25) captures that we only need to worry about about the factor H1(Y \K; L⊗2
α ). As we
mentioned in the introduction, the condition (25) is only satisﬁed for certain values of α determined
by the Alexander polynomial △K(t) of K.
Lemma 15. Suppose that K is a knot and that △K(e−4πiα) ̸= 0. Then the reducible connection
[θα] is isolated from the irreducible ﬂat connections.
Proof. Again, it suﬃces to guarantee that H1(Y \K; L⊗2
α ) vanishes. In the notation of [15, Ap-
pendix], the reducible connection [θα] deﬁnes a local coeﬃcient system with ﬁber C where the
monodromy map ˆρα : H1(Y \K; Z) →C∗maps the meridian µK to e−4πiα. The vanishing of the
cohomology H1(Y \K; L⊗2
α ) now follows from [15, Corollary 65].
□
For completeness sake, we will now give more details to Lemma 3.13 in [36], since our method
of proof will generalize to the case of an embedded torus T inside a four manifold X with the
homology of S1 × S3.


## Page 24


Mariano Echeverria
24
Lemma 16. Suppose that ρ is a ﬂat connection corresponding to a critical point of CS and gρ
is the corresponding local system. Then the ﬁrst (orbifold) cohomology ˇH1( ˇY ; gρ) can be identiﬁed
with ker : H1(Y \K; gρ) →H1(µK; gρ).
Proof. For the proof we will follow the suggestion of Lemma 3.13 in [36] and use the Mayer-Vietoris
sequence for cohomology with local coeﬃcients. More precisely, for ǫ > 0 write ˇY as
ˇY = ( ˇY \ˇνǫ(K)) ∪ˇν(K)
where ˇνǫ(K), ˇν(K) are tubular neighborhoods of K, and ˇνǫ(K) ⊂ˇν(K). Then the ﬁrst terms in
the Mayer-Vietoris sequence for this decomposition read
· · · ˇH0(( ˇY \ˇνǫ(K)) ∩ˇν(K); gρ)
→ˇH1( ˇY ; gρ)
→(ı∗
ˇ
Y \ˇνǫ(K),ı∗
ˇν(K)) ˇH1( ˇY \ˇνǫ(K); gρ) ⊕ˇH1(ˇν(K); gρ)
→ˇH1(( ˇY \ˇνǫ(K)) ∩ˇν(K); gρ)
→ˇH2( ˇY ; gρ)
→· · ·
Here ı∗
ˇY \ˇνǫ(K) and ı∗
ˇν(K) denote the pullback in cohomology of the inclusions ı : ˇY \ˇνǫ(K) ֒→ˇY
and ı : ˇν(K) ֒→ˇY . Now using the usual properties of invariance of the cohomology groups under
deformation retractions we can rewrite the previous sequence as
· · ·H0(Tǫ; gρ)
→ˇH1( ˇY ; gρ)
→(ı∗
Y \K,ı∗
ˇν(K))H1(Y \K; gρ) ⊕ˇH1(ˇν(K); gρ)
→
i∗
Tǫ,ν(K)−i∗
Tǫ,Y \K H1(Tǫ; gρ)
→· · ·
where Tǫ = ∂ˇνǫ(K). Notice that we have dropped theˇnotation on the regions where the orbifold
singularity is not present.
Observe ﬁrst of all that since Tǫ has abelian fundamental group then the restriction of gρ to Tǫ
automatically becomes reducible and we can write
gρ |Tǫ= R ⊕L⊗2
ρ
Now, because of the holonomy condition, for ǫ suﬃciently small the local system deﬁned by L⊗2
ρ
is
non-trivial, which means in particular that
H•(Tǫ; L⊗2
ρ ) ≡0


## Page 25


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 25
by [15, Lemma 63]. If we write µK and λK for the meridian and longitudes of K, then the Mayer-
Vietoris sequence simpliﬁes to
· · ·R
→ˇH1( ˇY ; gρ)
(26)
→(ı∗
Y \K,ı∗
ˇν(K))H1(Y \K; gρ) ⊕ˇH1(ˇν(K); gρ)
(27)
→
i∗
Tǫ,ν(K)−i∗
Tǫ,Y \K R[µK] ⊕R[λK]
→ˇH2( ˇY ; gρ)
(28)
→· · ·
For computing ˇH1(ˇν(K); gρ) write
ˇν(K) = S1 × ˇD2
where we regard ˇD2 as an orbifold. In fact, we can think of ˇD2 as D2/Zν, where Zν denotes a
cyclic action determining the cone angle 2π/ν. If p : D2\{0} →ˇD2\{0} denotes the quotient map,
then as long as the cone angle is suﬃciently sharp and α is a rational value, the pullback of the ﬂat
connection ρ to D2\{0} extends smoothly to a ﬂat connection p∗ρ on all of D2, and in fact we can
identify ˇH1( ˇD2; gρ) with the equivariant cohomology H1,ν(D2; p∗gρ). Hence
ˇH1(ˇν(K); gρ) = H0(S1; gρ) ⊗H1,ν(D2; p∗gρ) ⊕H1(S1; gρ) ⊗H0,ν(D2; p∗gρ)
Now, the factor H1,ν(D2; p∗gρ) will vanish since D2 equivariantly retracts to the origin so that
H1,ν(D2; p∗gρ) ≃H1,ν({0}, p∗gρ) = 0
Likewise, we have that
H0,ν(D2; p∗gρ) ≃H0,ν({0}; p∗gρ) ≃R
since only one factor of R3 ≃p∗gρ |{0}⊂D2 is preserved under the group action.
To compute
H1(S1; gρ) we use again the fact that S1 has abelian fundamental group which in particular means
that gρ reduces to the system
gρ |S1≃R ⊕L⊗2
ρ
In this case, L⊗2
ρ
may or may not be the trivial system which means that
H1(S1; gρ) =
(
H1(S1; R)
if L⊗2
ρ
|S1 non-trivial
H1(S1; R) ⊗R3
if L⊗2
ρ
|S1 trivial
In any case that means that
(29)
ˇH1(ˇν(K); gρ) ≃H1(S1
λK; gρ)
so the maps in the Mayer-Vietoris sequence 27 become
ˇH1( ˇY ; gρ) →(ı∗
Y \K,ı∗
ˇν(K))
H1(Y \K; gρ) ⊕ˇH1(ˇν(K); gρ)
(30)
ˇω →
 ˇω |Y \K, ˇω |ˇν(K)

and
H1(Y \K; gρ) ⊕ˇH1(ˇν(K); gρ) →
i∗
Tǫ,ν(K)−i∗
Tǫ,Y \K
R[µK] ⊕R[λK]
(31)
(ω, ˇ̟) →
D
ω |S1µK , [µK]
E
,
D
(ω −ˇ̟) |S1
λK , [λK]
E


## Page 26


Mariano Echeverria
26
where the notation means that we are restricting the forms to the S1 factors generated by the
meridian and longitude respectively, and then using the pairing coming from the isomorphisms we
established previously. In particular, since Mayer-Vietoris is an exact sequence this means that for
any ˇω ∈ˇH1( ˇY ; gρ) we have

i∗
Tǫ,ν(K) −i∗
Tǫ,Y \K

◦(ı∗
Y \K, ı∗
ˇν(K))ˇω = 0
which according to the formulas 30 and 31 imply that
D
ˇω |S1µK , [µK]
E
= 0
In other words, there is a well deﬁned map
ı∗: ˇH1( ˇY ; gρ) →
n
ω ∈H1(Y \K; gρ) |
D
ω |S1µK , [µK]
E
= 0
o
ˇω →
ˇω |Y \K
or more succinctly ı∗: ˇH1( ˇY ; gρ) →ker :
 H1(Y \K; gρ) →H1(m; gρ)

as we wrote in the statement
of the lemma. We just need to show that this map is an isomorphism.
First we address the surjectivity of the map. Suppose that ω ∈H1(Y \K; gρ) and that
D
ω |S1
µK , [µK]
E
=
0. Using the isomorphism 29 we can consider the element

ω, ω |S1
λK

∈H1(Y \K; gρ) ⊕ˇH1(ˇν(K); gρ)
Because
D
ω |S1µK , [µK]
E
= 0 we have that

ω, ω |S1
λK

∈ker

i∗
Tǫ,ν(K) −i∗
Tǫ,Y \K

which means by
exactness of the Mayer-Vietoris sequence that

ω, ω |S1
λK

∈im(ı∗
Y \K, ı∗
ˇν(K)). In other words, there
is ˇω ∈ˇH1( ˇY ; gρ) such that ı∗(ˇω) = ω, which is what we wanted to show.
For injectivity we simply observe that if ı∗(ˇω) = [0] then ω = ˇω |Y \K is exact, that is, ω = dBξ
for some ξ ∈Ω0(Y \K; gρ) and B is the connection representative of the ﬂat connection ρ. Now we
can compute the norm of ˇω in the following way, which is essentially the same computation as in
[25, Proposition 2.10]
∥ˇω∥2
ˇL2( ˇY ) =
−lim
ǫ→0
Z
Y \ˇνǫ(K)
tr(∗ω ∧ω)
=
−lim
ǫ→0
Z
Y \ˇνǫ(K)
tr(∗ω ∧dBξ)
=
lim
ǫ→0
"Z
Y \ˇνǫ(K)
tr(dB(∗ω) ∧ξ) −
Z
Tǫ
tr(∗ω ∧ξ)
#
=
−lim
ǫ→0
Z
Tǫ
tr(∗ω ∧ξ)
=
0
where we have used that dB(∗ω) = ∗d∗
Bω = 0 since ˇω ∈ker ˇ△B = ker( ˇdB) ∩ker( ˇd∗
B).
That
limǫ→0
R
Tǫ tr(∗ω ∧ξ) = 0 vanishes is essentially a restatement that on orbifolds one can use inte-
gration by parts [40, Section 2.1]. Alternatively, one can follow the approximation scheme in the
proof of [32, Proposition 8.3]. Hence ∥ˇω∥2
ˇL2( ˇY ) = 0 which also means that ˇω = 0, which is what we
needed to show for the proof of injectivity.
□


## Page 27


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 27
Using values of α ∈Q ∩(0, 1/2) which satisfy △K(e−4πiα) ̸= 0, and with a local system which
satisﬁes the properties discussed in the previous section, we can deﬁne the chain complex
(C∗(Y, K, α; Γ, p), ∂)
where we are also indicating the dependence of the chain complex on the perturbation used to
achieve transversality. Again, the local coeﬃcient system we will have in mind is the universal
Novikov ﬁeld/local system described in the previous section, in order to minimize additional choices
to get an actual Floer group, rather than a group up to isomorphism.
We will choose our perturbation p as
p = pcrit + p∂
where pcrit and p∂mean the following. If pcrit is a perturbation which makes the critical set Cpcrit
non-degenerate, then we can approximate pcrit by a ﬁnite sum of holonomy perturbations. Since
the non-degeneracy of the compact set Cpcrit is an open condition, we can arrange that fpcrit is a
ﬁnite sum by truncating pcrit after ﬁnitely many terms. This guarantees that the support of the
holonomy perturbations do not meet a neighborhood of the knot K. This argument appears in
Proposition 3.1 of [37], although the setup in Kronheimer and Mrowka’s paper is more complicated
since they also need to guarantee certain ﬁniteness condition for the moduli spaces of ﬂow lines of
dimension less or equal to 2. Then p∂is the remaining perturbation needed to cut out the moduli
spaces of trajectories transversely.
Because of this support condition, we can appeal to Herald’s result [26, Theorem 0.1], which
relates the signed count of elements in the (ﬁnite) set Cpcrit to the Casson invariant and the knot
signature of K.
Theorem 17. Suppose that α ∈Q ∩(0, 1/2) satisﬁes △K(e−4πiα) ̸= 0. Then the signed count of
Cpcrit, which we denote #s|Cpcrit|, equals
(32)
#s|Cpcrit| = 4λC(Y ) + 1
2σK(e−4πiα)
where λC(Y ) is the Casson invariant of Y and σK(e−4πiα) the Tristram-Levine knot signature of
K evaluated at e−4πiα.
Moreover, as vector spaces over the Novikov ﬁeld Λ, we have that
χΛ(HI(Y, K, α)) = 4λC(Y ) + 1
2σK(e−4πiα)
Notice that the second part of previous statement implicitly assumed:
a) A choice for the orientation of the moduli spaces involved in the deﬁnition of Cpcrit and
HI(Y, K, α).
b) The claim that there is a well deﬁned diﬀerential ∂which squares to zero so that we can take
HI(Y, K, α) = ker ∂/im∂.
c) A proof that HI(Y, K, α) is independent of the perturbations used.
We will start by discussing the orientation of the moduli spaces, which we have kept under the
rug until this point. For our conventions we will follow closely the exposition in [55, Section 4.3],
which in turn are based on those used in [14, 35, 36]. They also agree with the conventions used
by Collin and Steer in their paper [9], which we used to pin down the signs in the formula (32).
The orientation set o([β]) of a critical point Cp refers to the 2-element set of orientations of the
real line det DA, where A is a connection on R × Y such that A |{t}×Y is (gauge) equivalent to
θα for t suﬃciently negative and (gauge) equivalent to β for t suﬃciently large. Here DA is the


## Page 28


Mariano Echeverria
28
Fredholm operator −d∗
A ⊕d+
A, after suitable Sobolev completions have been introduced. In general
any reference connection would work, but the advantage of using the reducible connection θα as
one of the limiting connections is that it will automatically gives us an absolute Z/4Z grading as
we will explain momentarily.
In general, given two connections β1 ∈C(Y1, K1, α) and β2 ∈C(Y2, K2, α2) and a cobordism
(W, Σ, α) : ∅→(−Y1, −K1, α) ⊔(Y2, K2, α)
one can consider the operator (for ǫ > 0 suﬃciently small)
D′
A = −d∗
A ⊕d+
A : ˇLp
m,φ′ǫ(Λ1 ⊗gP ) →ˇLp
m−1,φ′ǫ((Λ0 ⊕Λ+) ⊗gP ))
where A ∈C(W ∗, Σ∗, α) is a connection on the completion
W ∗= (R−× Y1) ∪W ∪(R+ × Y2)
Σ∗= (R−× K1) ∪W ∪(R+ × K2)
which is asymptotic to β1 for t suﬃciently negative and to β2 for t suﬃciently positive.
Here
ˇLp
m,φ′ǫ = eφ′
ǫ ˇLp
m denotes a weighted Sobolev space, weighted by a real function eφ′
ǫ, where φ′
ǫ is
a non-positive smooth function equal to ǫt for t suﬃciently negative on R−× Y1, to −ǫt for t
suﬃciently large on R+ × Y2 , and equal to 0 on W.
When β1 is a perturbed instanton on (Y1, K1, α, p1), with respect to the perturbation p1, and
similarly for β2 with respect to the perturbation p2 on (Y2, K2, α, p2), then the moduli space
M([β1], (W, Σ), [β2]) of perturbed α-ASD instantons, which we will denote as M([β1], ˇW, [β2])
will decompose into connected components
M([β1], ˇW, [β2]) =
[
z
Mz([β1], ˇW, [β2])
and the dimension of Mz([β1], ˇW, [β2]) can be computed as indD′
A, where A is an appropriate
representative of an element [A] ∈Mz([β1], ˇW, [β2]) . For a composite cobordism, one has the
additivity relation (assuming the critical points are non-degenerate) [55, eq. 4.3]
dim Mz′◦z([β0], ˇ
W ′ ◦ˇW, [β2])
= dim Mz([β0], ˇW, [β1]) + dim stab[β1] + dim Mz′([β1], ˇW ′, [β2])
(33)
When [β0], [β1] are irreducible (perturbed) ﬂat connections on (Y, K, α), we had deﬁned in Section
3 a relative grading gr([β0], [β1]) ∈Z/4Z in terms of the spectral ﬂow of the extended Hessian.
Since the spectral ﬂow of this operator can be interpreted as the index of the operator D′
A on the
cylinder R × Y , this means that the relative grading can be interpreted as the dimension (mod-4)
of the moduli space of ﬂow-lines between [β0] and [β1]:
gr([β0], [β1]) = dim M([β0], [β1])
mod 4
where again we are looking at moduli spaces asymptotic to [β0] as t →−∞and to [β1] as t →∞.
To make this an absolute grading, set
(34)
gr([β]) = −1 −dim M([θα], [β])
mod 4 = dim M([β], [θα])
mod 4


## Page 29


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 29
and give grading 0 to the reducible connection [θα]. Notice that because [θα] has a one-dimensional
stabilizer according to (33) we have that
gr([β0]) −gr([β1])
= dim M([θα], [β1]) −dim M([θα], [β0])
mod 4
= dim M([θα], [β1]) + dim M([β0], [θα]) + 1
mod 4
= dim M([β0], [β1])
mod 4
=gr([β0], [β1])
With respect to this absolute grading, if Cp,i denotes the set of critical points associated to the
perturbation p whose absolute grading is i ∈Z/4Z, then an expression like (32) means
#s|Cpcrit| = #|Cpcrit,0| + #|Cpcrit,2| −#|Cpcrit,1| −#|Cpcrit,3|
Now we must turn to a discussion of the properties of the perturbations used in order to guarantee
that we have a well deﬁned diﬀerential and that the homology groups we obtain are independent of
the perturbations used. First we need to understand what is at stake. Recall that we are assigning
to each element [β] ∈B(Y, K, α) a vector space Γ[β] which is a copy of the universal Novikov ﬁeld
ΛQ,R. In other words, an element of Γ[β] is a formal power series
(35)
X
r∈R
arT r
where ar ∈Q, and #{r | ar ̸= 0, r > C} < ∞for all C ∈R. Therefore, the power series can extend
indeﬁnitely in the negative direction, but not the positive one. Now, the diﬀerential ∂on the chain
complex C∗(Y, K, α, Γ, p) should be deﬁned by the formula (for [β1] ∈C(Y, K, α, p))
(36)
∂[β1] =
X
[β2]∈C(Y,K,α,p)|gr([β1],[β2])=1
mod 4
X
z
nz([β1], [β2])T −Etop(z)[β2]
Here
Etop(z) =
1
8π2
Z
R× ˇY
tr(FA ∧FA)
where [A] ∈Mz([β1], [β2]). In the absence of perturbations, i.e, p = 0 then Etop(z) would equal
1
8π2 ∥F −
A ∥L2 = 2(CS(β1) −CS(β2)), since A would solve the α-ASD equation F +
A = 0. Therefore,
the exponents in T −Etop(z) would always be non-positive and do not accumulate on any ﬁnite
subinterval, since they must always diﬀer from each other by some integer combination of 64π2 and
128π2α (this follows from the formula (16) for the topological energy in the closed 4-manifold case).
In other words, the candidate for the diﬀerential (36) does make sense as an element (35) of ΛQ,R .
In the presence of perturbations p, the inequality that is satisﬁed is
Etop(z) + fp([β1]) −fp([β2]) ≥0
Since fp is fully gauge equivariant as we mentioned when we introduced the holonomy perturbations,
the lower bound for Etop(z)
(37)
Etop(z) ≥fp([β2]) −fp([β1])
is independent of the speciﬁc moduli space Mz([β1], [β2]) we are looking at, so the expression (36)
continues to be well deﬁned as an element of ΛQ,R.


## Page 30


Mariano Echeverria
30
After we know that ∂makes sense, proving ∂2 = 0 is in this setting is no diﬀerent than the
situation for monopole Floer homology with local coeﬃcients [38, Section 30], except for two main
diﬀerences:
(1) In the instanton setup, bubbling in general can play a role.
(2) We have excluded the reducible ﬂat connection from our chain group, so we need to guaran-
tee that the broken trajectories considered to show that ∂2 = 0 do not include factorizations
through this reducible connection.
Regarding the ﬁrst point, this is not a problem for showing that ∂2 = 0, since bubbles drop the
dimension of the moduli spaces involve by at least 4 [36, Proposition 3.22], and our transversality
assumptions for the moduli space of ﬂow lines guarantee that negative dimensional moduli spaces
are empty.
The second point involves analyzing the non-degeneracy of the reducible connection and some
index formulas.
• Even after perturbations, there is still one reducible connection [θα] up to gauge, the same
one as the unperturbed case, since [θα] is isolated from the irreducible connections so one
can choose the holonomy perturbations in such a way that they vanish near [θα]. Notice
that [θα] is unobstructed since by Poincare duality ˇH2( ˇY ; gα) ≃ˇH1( ˇY ; gρ) = 0.
• If Mz([β0], [β2]) represents a d-dimensional moduli space, and there is a broken trajectory
belonging to Mz1([β0], [θα]) × Mz2([θα], [β2]) with dimensions d1, d2 respectively, the fact
that [θα] has one dimensional stabilizer implies that
dim Mz([β0], [β2]) = dim Mz1([β0], [θα]) + dim Mz2([θα], [β2]) + 1
so in particular the right hand side is bounded from below by 3, since each d1, d2 must be
at least one dimensional. Hence moduli spaces admitting Mz([β0], [β2]) such factorizations
through the reducible connection [θα] must be at least three dimensional, so they can be
ignored for the deﬁnition of the diﬀerential. Notice that this is the same as what happens
in the ordinary case of Instanton Floer homology for integer homology spheres, but in
that case the bound for the dimension is 5, since the stabilizer of the trivial connection is
three-dimensional.
This means that we can deﬁne the Instanton Floer-Novikov homology for knots HI(Y, K, α)
as ker ∂/im∂. Notice that our notation makes implicit that the homology we obtain is independent
of the choice of perturbation π ∈P. To see why this is true, we adapt the proof of independence
in [14, Section 5.3] to our situation, and discuss more generally the functoriality properties of these
instanton Floer-Novikov groups.
Suppose that (W, Σ) : (Y1, K1) →(Y2, K2) is a concordance of the knots K1, K2.
By this
we mean that Y1, Y2 will be both be integer homology spheres and W homology cobordism, i.e
H∗(W; Z) = H∗(Yi; Z) for i = 1, 2. Moreover, Σ will be an embedded annulus with ∂Σ = −K1⊔K2.
Finally, suppose that the cobordism (W, Σ) is α-admissible in the sense of Deﬁnition 7. Recall
that this means that for the unique reducible up to gauge θW,α we have H1(W\Σ; L⊗2
θW,α) = 0.
Since θY1,α and θY2,α also satisfy H1(Yi\Ki; L⊗2
θYi,α) = 0 for i = 1, 2, it is immediate that on the
completion H1(W ∗\Σ∗; L⊗2
θW∗,α) = 0, and an straightforward adaptation of Lemma 16 will imply
that for α-admissible cobordisms the reducible θW,α is isolated (and non-degenerate as well).
We want to deﬁne a cobordism map
m(W,Σ) : C∗(Y1, K1, α, Γp, p1) →C∗(Y2, K2, α, Γp, p2)


## Page 31


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 31
via the formula
(38)
m(W,Σ)[β1] =
X
[β2]
X
z:[β1]→[β2]
mz([β1], ˇW, [β2])T −Etop(z)[β2]
Here the sum is taking place over all homotopy classes z for which the moduli space Mz([β1], ˇW, [β2])
is zero dimensional, and the notation ˇ
W is emphasizing that we are regarding ˇW as an orbifold.
Before showing that mz([β1], ˇW, [β2]) is well deﬁned, let’s discuss ﬁrst how the cobordism maps
should interact with the gradings HIi(Y, K, α) of the Floer groups.
If gr([βi]) denotes the (absolute)
mod 4 grading of [βi] then [35, Proposition 4.4], [9, Section
4.3] shows that
(39)
dim Mz([β1], ˇ
W, [β2]) = gr([β1]) −gr([β2]) −3
2(χ(W) + σ(W)) −χ(Σ)
mod 4
In particular, given our assumptions on (W, Σ), we can see that the cobordism map m(W,Σ) is a
sum over all elements [β2] whose relative grading is the same as [β1]. What is left to see is why the
formula for m(W,Σ)[β1] deﬁnes an element in ΛQ,R.
This requires further discussion of how the ASD equation is perturbed on a cobordism. Here
we follow [36, Section 3.8], [10, Section 2.2], [31, Section 3.1] and [46, Section 4]. On the cobordism
W we choose a collar neighborhood of each boundary component, and if t denotes the coordinate
(say in the collar [0, 1) × Y1) , we choose a t -dependent holonomy perturbation pt equal to p1 on
the near [0, 1/4) × Y1. On (3/4, 1) × Y1 the perturbation pt vanishes and then we interpolate on
[1/4, 3/4] × Y1 choosing an auxiliary perturbation ˜p1 ∈PY1. The net eﬀect is that on [0, 1) × Y1 the
perturbed equations take the form
F +
A + β1(t)U1(A) + ˜β1(t) ˜U1(A) = 0
where β1, ˜β1 denote suitable cut-oﬀfunctions and U1, ˜U1 denote the perturbation terms associated
to β1, ˜β1. Similar remarks apply to Y2. These were the perturbations used in [36, Section 3.8]. To
deal with transversality issues involving ﬂat connections on the cobordism, we also need interior
holonomy perturbations, supported on a compact subset of W\nbd(Σ∪∂W), which were introduced
for closed 4-manifolds in [31], although analogous constructions appear for example in [13, 19].
These are constructed in a similar way to how cylinder functions were constructed on a 3 manifold.
We sketch the construction given in [36, Section 3.8], which also appears in [46, Deﬁnition 4.2].
Namely, one chooses a closed ball B ⊂W\nbd(∂W) and a ﬁnite collection of smooth submersions
qi : S1 × B →W\nbd(Σ ∪∂W) so that qi(1, b) = b and qi(−, b) is an immersion for all 1 ≤i ≤n
and b ∈B.
Choose also a self dual two form ω whose support is contained in B.
Then for
q = (q1, · · · , qn) we have a section
Vq,ω : C(W, Σ, α) →Ω2,+(W; gE)
given by
Vq,ω(A)(x) = Holq(A) ⊗ω(x)
Again, after introducing suitable completions one constructs a Banach space of secondary holo-
nomy perturbations with a notion of L1 convergence [46, p.51]. Therefore, on the cobordism with
cylindrical ends W ∗the perturbed α-ASD equations we must consider are of the form
(40)
F +
A + Up(A) + Vω(A) = 0


## Page 32


Mariano Echeverria
32
where the term Up(A) is generic notation for the cylindrical holonomy perturbations and Vω(A)
denotes the interior holonomy perturbations. The important property we need to know about Up
and Vω is that their L∞norms are uniformly bounded: that is, there exists K > 0 such that
• ∥Up(A)∥L∞≤K∥p∥P (this is statement iii) in [36, Proposition 3.7].
• ∥Vω(A)∥L∞≤K∥ω∥˜
P (this is statement 2) in [46, Proposition 4.4], which ﬁrst appeared
in [31, Section 3.2]).
In fact, for transversality purposes, which is the reason why these perturbations were introduced in
the ﬁrst place, for any given ǫ > 0, we can assume that we chose perturbations p and ω satisfying
∥p∥P, ∥ω∥˜
P < ǫ , so in particular that will mean that
|fp([β])| < ǫ
for all [β] ∈B(Y, K, α). To bound E(z) from below, we follow the proof of [10, Proposition 2.15]
and split W ∗into three regions
1
8π2
Z
W ∗tr(F(A) ∧F(A))
= 1
8π2
Z
R−× ˇY1
tr(F(A) ∧F(A)) +
1
8π2
Z
W
tr(F(A) ∧F(A)) +
1
8π2
Z
R+× ˇY2
tr(F(A) ∧F(A))
≥
h
fp([A |{0}× ˇY1]) −fp([β1])
i
+
1
8π2
Z
W
 |F −(A)|2 −|F +(A)|2
+
h
fp([β2]) −fp([A |{0}× ˇY2])
i
≥−2ǫ + fp([β2]) −fp([β1]) −
1
8π2
Z
W
|Up(A) + Vω(A)|2
≥−2ǫ + fp([β2]) −fp([β1]) −3ǫ2
8π2
In these steps we used the inequality 37 to deal the ﬁrst and third integrals while we used the
equation 40 on the second integral. The speciﬁc bound is not that important, only knowing that it
does not depend on the component of the moduli space that is being analyzed. Therefore m(W,Σ)[β1]
will deﬁne an element of ΛQ,R once we know that the numbers mz([β1], ˇW, [β2]) are well deﬁned.
For that we follow [14, Proposition 5.9]. That is, we want to show that the 0-dimensional moduli
spaces Mz([β1], ˇW, [β2]) with topological energy E(z) are compact. This is because if we start with
a sequence [Ai] in Mz([β1], ˇW, [β2]) (which is deﬁned using a bundle P([β1], [β2]), then it would
converge weakly to
• An ideal instanton ([A∞], x∞) on a bundle Q over W ∗, asymptotic on each cylindrical end to
[β′
1], [β′
2] respectively.
• A broken trajectory ([A1], x1) over R × Y1 connection [β1] and [β′
1], and a broken trajectory
([A2], x2) over R × Y2 connecting [β′
2] and [β2] .
Additivity of the index says that (again because the critical points are non-degenerate)
0 =
indP([β1], [β2])
(41)
=
ind[A∞] + ind[A1] + ind[A2] + dim ˇH0(Y1; gβ′
1) + dim ˇH0(Y2; gβ′
2) + 4(|x∞| + |x1| + |x2|)
• If [A∞] is irreducible then by transversality ind[A∞] ≥0 and since [A1], [A2] are both irreducible
given that at least one of their limits is irreducible, then ind[A1] ≥0, ind[A2] ≥0 by transversality.
Then the only way for the above equality to hold is if [β1] = [β′
1], [β2] = [β′
2] and there were no
bubbles, i.e, |x∞| = |x1| = |x2| = 0.


## Page 33


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 33
• If [A∞] is reducible then our assumptions on homology imply that H1(W\Σ; Z) ≃H1(W ∗\Σ∗; Z) ≃
Z and because of the holonomy condition [A∞] is determined to be the unique (up to gauge) re-
ducible with S1 stabilizer which is asymptotic to the reducibles [θα,Y1] and [θα,Y2] respectively. In
this case ind[A∞] can be computed from the dimension formula 39, with the caveat that the for-
mula as written only works assuming that the limits are irreducible connections. When the limits
are reducible, one needs to take into account the stabilizer in the formula and one concludes that
ind[A∞] = −1. Since dim ˇH0(Y1; gθα,Y1 ) = ˇH0(Y2; gθα,Y2 ) = 1 one ﬁnds in 41 that
−1 = ind[A1] + ind[A2] + 4(|x∞| + |x1| + |x2|) ≥0
which is impossible. Therefore, mz([β1], ˇW, [β2]) is well deﬁned.
Finally, to verify the chain property one needs to compute
(∂Y2mW + mW ∂1) [β1]
=
X
[β′
2]
X
z2
X
[β2]
X
z
mz([β1], ˇW, [β2])nz2([β2], [β′
2])T −Etop(z)T −Etop(z2)[β′
2]
+
X
[β2]
X
w
X
[β1]
X
z1
nz1([β1], [β′
1])mw([β′
1], ˇW, [β2])T −Etop(z1)T −Etop(w)[β2]
and show that it vanishes. Again, the usual argument will still work as long as one remember that
the topological energy is additive under concatenation of paths.
Similar arguments can be applied for showing that the composition law for α-admissible cobor-
disms holds, and in this way we have veriﬁed that HI(Y, K, α) is a topological invariant of the data
(Y, K, α), together with a choice of cone parameter ν, which has been omitted from our notation.
5. Reduced Version
Now we will deﬁne a reduced version HIred(Y, K, α) of the singular instanton Floer-Novikov
homology for knots HI(Y, K, α) we just construced, following [18]. As we also mentioned in the
introduction, the case of α = 1/4 , where local coeﬃcients are not needed, was deﬁned by Daemi
and Scaduto earlier [11].
Our conventions will diﬀer slightly from those of Frøyshov, since we are deﬁning the homology
version of the Floer groups, which means that our grading of the groups diﬀer, and in fact are closer
to the ones used in [14, Section 3.3.2], [55, Section 9].The key diﬀerence between the reduced and
unreduced versions of instanton Floer homologies is that the reduced version takes into account the
ﬂow-lines between the critical points and the reducible ﬂat connection. Moreover, in the reduced
version we can deﬁne a U-map, which in the situation of knots will arise from the µ-map evaluated
at a point x ∈K.
Now we want to deﬁne maps which take into account the interaction with the reducible connection
[θα]. Consider a critical point [β] with gr([β]) = 1. From the grading formula (34), we can see that
in principle there are non-empty moduli spaces M1([β], [θα]) asymptotic to [β] as t →−∞and
to [θα] as t →∞.
After taking the quotient by the R action, we get a 0-dimensional moduli
space
ˇ
M1([β], [θα]). We would like to deﬁne a map δ1[β] obtained by counting the points in this
0-dimensional moduli space. However, because of non-monotonicity there can be a priori inﬁnitely
many components of this moduli space
M1([β], [θα]) =
[
z
M1,z([β], [θα])


## Page 34


Mariano Echeverria
34
Therefore, we deﬁne
δ1 : CI1(Y, K, α, p) →Λ
[β] →
X
z
# ˇ
M1,z([β], [θα])T −Etop(z)
Recall that Λ is the Novikov ﬁeld, while CI1(Y, K, α, p) denotes the chain complex of p-perturbed
ﬂat connections whose absolute grading is 1. The formula for δ1[β] does give a well deﬁned element
in Λ for exactly the same reasons as the diﬀerential ∂from the previous section being well deﬁned.
Just as in the case where K is absent, it is straightforward to see that δ1 descends to a map in
homology, that is:
Lemma 18. The map δ1 satisﬁes δ1∂= 0, so it induces a map in homology δ1 : HI1(Y, K, α) →Λ.
Likewise, suppose that gr([β]) = 2, so that a priori there are non-empty moduli spaces M1([θα], [β]).
Analogous to δ1, deﬁne an element δ2 ∈CI2(Y, K, α, p) by the formula
δ2 =
X
[β]∈CI2
X
z
# ˇ
M1,z([θα], [β])T −Etop(z)[β]
As before, it is straightforward to check that:
Lemma 19. The element δ2, descends to an element in homology, i.e, ∂δ2 = 0 so that δ2 ∈
HI2(Y, K, α).
The next map to deﬁne is the µ -map, which we will denote µK, to emphasize the fact that it is
not the ordinary µ-map. First we need to understand the homotopy type of the space of connections
mod gauge, i.e, B(Y, K, α), since for x ∈K, µK(x) will be a degree 2 element in H∗(B(Y, K, α); Q).
The main idea is to take advantage of the fact that singular connections have a stronger notion of
framing than ordinary connections. We will follow the discussion in [48, Section 5] and [30, Section
4]. Recall that if G is a compact Lie group that acts on a topological space Z, then the homotopy
quotient Z//G is deﬁned as Z ×G EG, where EG is a contractible space with a free G action. The
natural map Z//G →Z/G induces a map H∗(Z/G, Z) →H∗(Z//G, Z), which is an isomorphism
when G acts freely. Lemma 5.1 in [48] shows the following:
Lemma 20. If U(1) acts on Z and the stabilizer of every point in Z is {±1}, then the pull-back
map H∗(Z/U(1), Q) →H∗(Z//U(1), Q) is an isomorphism.
When V is a complex vector bundle over Z with a lift of the G action to V , we can also deﬁne
V//G = V ×GEG and the G-equivariant Chern classes of V as ci,G(V ) = ci(V//G) ∈H2i(Z//G, Z).
These are the pull-backs of the Chern classes on Z/G.
For our setup, when we are working with the pair (X, Σ), the bundle E decomposes near Σ as
E = L ⊕L−1. Moreover, we wrote an exact sequence 12 for the gauge group, which in particular
implies that over Σ the SU(2) gauge is broken to an U(1) gauge. If x ∈Σ is a base-point and
Gx the gauge transformations which act trivially on Ex = Lx ⊕L−1
x , then we have the framed
conﬁguration space
Bo(X, Σ, α) = C(X, Σ, α)/Gx(X, Σ)
Since G/Gx ≃U(1), a residual gauge group isomorphic to U(1) acts on Bo(X, Σ, α), and Bo(X, Σ, α)/U(1) =
B(X, Σ, α). Now we are ready to deﬁne the universal SO(3) bundle and the corresponding µ map.


## Page 35


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 35
Deﬁnition 21. Deﬁne the universal SO(3) bundle
Ead = C(X, Σ, α) ×Gx gE →(B∗(X, Σ, α) × X)
Moreover, the U(1) bundle
(42)
Lo = C(X, Σ, α) ×Gx L →Bo(X, Σ, α) × Σ
descends to the universal U(1) bundle
L⊗2 →(B∗(X, Σ, α) × Σ)
Deﬁne for η ∈Hi(X; Q) and ηΣ ∈Hj(Σ; Q) the µ-maps
µ(η) = −1
4p1(Ead)/η ∈H4−i(B∗(X, Σ, α); Q)
µΣ(ηΣ) = −1
2e(L⊗2)/ηΣ ∈H2−j(B∗(X, Σ, α); Q)
Remark 22. 1) We follow the sign conventions of Kronheimer for µΣ [30, Section 2.1].
2) Notice that since the homotopy type of B∗(X, Σ, α) is independent of α, the µ-maps corre-
sponding to diﬀerent values of α can be identiﬁed with each other, which is why we do not indicate
the value of α in our notation.
3) We can also view these as elements in B(X, Σ, α), since the reducible connections form a
stratum of inﬁnite codimension in B(X, Σ, α).
4) Notice that our construction singles out one of the line bundles in the decomposition E =
L ⊕L−1. In fact, had we used L−1 instead of L, then µΣ would diﬀer only in sign.
Clearly a similar procedure can be used to deﬁne µK in the case of (Y, K): a cheap way to do
this is to consider X = [0, 1] × Y and Σ = [0, 1] × K. Therefore, for x ∈K we let
uK(x) : CI∗(Y, K, α, p) →CI∗−2(Y, K, α, p)
[β0] →
X
[β1]|gr([β0],[β1])=2
X
z
< uK(x), M2,z([β0], [β1]) > T −Etop(z)[β1]
Contrary to the case of δ1, δ2, uK(x) will not descend to a map between the Floer homology groups.
To see why this is the case, observe that the maps
∂uK −uK∂
involve considering three dimensional moduli spaces, for which we had said factorizations through
the reducibles can occur. More precisely, notice that for any [β0], we have [here we denote for
convenience < uK(x), M2,z([β0], [β1]) > as Uz([β0], [β1])]
(∂uK −uK∂)[β0]
(43)
=
X
[β2]|gr([β2],[β1])=1
X
z12
X
[β1]|gr([β0],[β1])=2
X
z01
Uz01([β0], [β1])nz12([β1], [β2])T −Etop(z01)T −Etop(z12)[β2]
−
X
[β2]|gr([β2],[β1])=2
X
w12
X
[β1]|gr([β1],[β0])=1
X
w01
nw01([β0], [β1])Uw12([β1], [β2])T −Etop(w01)T −Etop(w12)[β2]


## Page 36


Mariano Echeverria
36
The typical argument would look at a three dimensional moduli space M3([β0], [β2]) and consider
the possible ends of this moduli space. Some of the ends correspond to the terms in 43, but when
gr[β0] = 1, a priori it is also possible to have factorizations of the form
M1([β0], [θα]) × M1([θα], [β2])
which needs to be accounted for. In fact, we have the analogue of [18, Theorem 4], [21, Proposition
8] and [14, Lemma 7.6].
Lemma 23. The map uK satisﬁes the relation
(44)
∂uK −uK∂−1
2δ1 ⊗δ2 = 0
Proof. Of the references cited above, the closest to our argument is in fact [21, Proposition 8], since
the monopole case also uses a universal U(1) bundle to deﬁne the corresponding u-map. Therefore
we obtain the same formula as the one Frøyshov writes for the monopole case, except for the
diﬀerence in conventions for the constants in front of the µ-maps.
In fact, the only place where one needs to be careful with the previous argument is that any of
the proofs quoted above use the holonomy of a connection A along the path R × {x} ⊂R × Y .
More precisely, consider a 3-dimensional moduli space M3,z([β0], [β2]), and choose a representa-
tive A ∈M3,z([β0], [β1]) whose “centre of mass” is 0, i.e,
Z
R×Y
t|FA|2 = 0
If adβ0, adβ1 are the corresponding (perturbed) ﬂat SO(3) bundles corresponding to [β0], [β1], then
we can choose a base point y ∈Y , which is close to x ∈K, without being equal to it. Using a
normal neighborhood ν(K) of K, we may assume that y belongs to a normal disk to K, centered at
x, for which y has polar coordinates (r, θ). Since we are away from the knot, there is no controversy
as to what we mean by
hA(r, θ) = holA (R × {y})
That is, the holonomy of A along the path R × {y}, where y has coordinates (r, θ). Comparing the
frames for the ﬁbres of the bundles adβ0, adβ1, we get an element in SO(3), i.e, hA(r, θ) ∈SO(3).
Now, for ﬁxed θ, as r decreases the decomposition E = L ⊕L−1 , adE = R ⊕L⊗2, becomes
asymptotically parallel with respect to A. Therefore, we obtain an element
hA(θ) = lim
r→0 holA (R × {y}) ∈U(1)
which is obtained by comparing the frames for the ﬁbres of the U(1) bundles ]
adβ0, ]
adβ1, over the
U(1) line bundle L⊗2 →Σ [compare with the description of the universal bundle 42]. The existence
of this limit follows for example from [56], or one can also use the fact that we are working with
orbifold connections, as Kronheimer and Mrowka do in [39, Section 3.1].
However, we still need to analyze what happens as we vary the angle at which we approach the
point x. It is not diﬃcult to see that as we vary the angle by a full revolution, i.e, θ →θ + 2π, then
the holonomy picks out hA(θ) picks out the asymptotic holonomy factor e−4πiα, in other words
hA(θ + 2π) = e−4πiαhA(θ)
So in the case of rational holonomy, we can take
(
hA(x) ≡[hA(θ)]q
α = 2p+1
2q
hA(x) ≡[hA(θ)]2q+1
α =
2p
2q+1


## Page 37


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 37
as our desired holonomy map. For example, the case of α = 1
4 =
1
2q implies that we should square
the limiting holonomy maps, which is exactly what Kronheimer and Mrowka do in [39, Section 3.1].
The diﬀerence with their construction is mainly stylistically, since they pass ﬁrst to a local cover of
a neighborhood of x, where the pull-backs of the connections extend smoothly.
Once we know how to take the holonomy along a point on the knot x ∈K, the proof follows in
exactly the same way as in [21, Proposition 8], where the coeﬃcient of δ1 ⊗δ2 is the Euler number
of the rank 1 Hermitian vector bundle over S2 = D2 ∪S1 D2 whose “clutching map” S1 →U(1) has
degree 1.
□
Now we interpret the equation 44 to ﬁnd out how the reduced Floer groups should be deﬁned.
• Case when [β] ∈HI1(Y, K, α) and δ1[β] = 0: then ∂uK[β] −uK∂[β] = 0, which means that
uK descends to a map
uK : ker δ1 ⊂HI1(Y, K, α) →HI−1(Y, K, α) = HI3(Y, K, α)
• Case when [β0] ∈HI0(Y, K, α): abusing notation write a representative of [β0] as [β]+∂[β1],
where ∂[β] = 0 and [β1] ∈HI1(Y, K, α). Then
uK[β0] = uK[β] + uK∂[β1] = uK[β] + ∂uK[β1] −1
2δ1([β1])δ2
Therefore, we must identify elements which diﬀer by an element on the “ray” Λδ2 , in other
words, we get a map
uK : HI0(Y, K, α) →coker(δ2) = HI2(Y, K, α)/(Λδ2)
• On the other summands HI2(Y, K, α) and HI(Y, K, α) , the uK map is actually well deﬁned
without additional considerations so we get maps
(
uK : HI2(Y, K, α) →HI0(Y, K, α)
uK : HI3(Y, K, α) →HI1(Y, K, α)
The deﬁnition the reduced Floer homology groups is now identical to [18, Deﬁnition 1], since as
long as we work with α-admissible cobordism it is straightforward to adapt section 3 of [18] (which
analyzes the behavior of δ1, δ2, uK under cobordisms) to obtain:
Theorem 24. Let K ⊂Y be a knot and α ∈Q ∩(0, 1/2) be such that △K(e−4πiα) ̸= 0. The
reduced Instanton Floer homology groups HIred
i
(Y, K, α)
HIred
0
(Y, K, α) =
HI0(Y, K, α)/(
X
im(u2l+1
K
δ2)
(45)
HIred
1
(Y, K, α) =
∩l≥0 ker(δ1u2l
K) ⊂HI1(Y, K, α)
HIred
2
(Y, K, α) =
HI2(Y, K, α)/(
X
im(u2l
Kδ2))
HIred
3
(Y, K, α) =
∩l≥0 ker(δ1u2l+1
K
) ⊂HI3(Y, K, α)
are topological invariants of the data (Y, K, α), together with the choice of cone parameter ν used
to deﬁne the groups.
Moreover, the Frøyshov knot invariants
(46)
h(Y, K, α) = χΛ(HIred(Y, K, α)) −χΛ(HI(Y, K, α)) ∈Z
where χΛ denotes the Euler characteristic with respect to the Novikov ﬁeld Λ, are also invariants
of (Y, K, α) (and the cone parameter).


## Page 38


Mariano Echeverria
38
Remark 25. The usual h-invariants have a factor 1
2 in front of the diﬀerence in Euler characteristics.
We choose not to include this factor because in our case the Euler characteristics of the groups may
be odd, since these groups need not be 2-periodic as opposed to the 4-periodic instanton Floer
homology groups on Y , and we prefer to obtain an integer rather than a half-integer.
6. Singular Orbifold Furuta-Ohta and Tori Signature
In this section we deﬁne an analogue of the Furuta-Ohta invariant λF O(X) [24] to the case of an
embedded torus T inside X satisfying certain topological conditions.
In other words, we want to deﬁne an invariant λF O(X, T, α), which in the best case scenario
can be interpreted as a signed count of irreducible representations π1(X\T ) →SU(2) (modulo
conjugacy) satisfying a certain holonomy condition determined by the parameter α.
As usual,
perturbations of the ﬂatness equation will be needed, so the interpretation of λF O(X, T, α) as a
count of ﬂat connections is slightly more complicated. In any case, our construction will be cooked
up in such a way that when we take X = S1 × Y and T = S1 × K then λF O(X, T, α) agrees with
2λCH(Y, K, α).
First we want to explain why we consider only torus complements X\T , and not more general
surface complements X\Σ. Moreover, we will discuss what conditions are needed to make the
deﬁnition of λF O(X, T, α) work.
Recall from section 2 that SU(2) bundles E →X are characterized by two topological invariants,
the instanton number k and the monopole number l. The moduli space of α-ASD connections
M(X, Σ, k, l, α) satisfying the asymptotic condition 9 has the expected dimension [32, Eq 1.6]
(47)
dim M(X, Σ, k, l, α) = 8k + 4l −3(b+
2 −b1 + 1) −(2g −2)
while the formula for the topological energy is [32, Eq. 1.7]
(48)
E(X, Σ, k, l, α) =
1
8π2
Z
ˇ
X
tr(FA ∧FA) = k + 2αl −α2Σ · Σ
Since H∗(X; Z) ≃H∗(S1 × S3; Z) these formulas simplify to
dim M(X, Σ, k, l, α) = 8k + 4l −(2g −2)
(49)
E(X, Σ, k, l, α) = k + 2αl
Notice that α-ﬂat connections (i.e, ﬂat connections satisfying 9) are equivalent to energy zero α-
ASD instantons (i.e, ASD instantons satisfying 9). In particular, this means that α-ﬂat connections
only exist a priori on bundles whose monopole and instanton numbers are related as
k + 2αl = 0
Clearly k = l = 0 is always a solution of this equation. Since k, l must always be integers, for
irrational values of α, k = l = 0 is the only solution. In fact, the next lemma shows that this
continue to hold regardless of the value of α.
Lemma 26. Suppose that E is an SU(2) bundle over (X, Σ) with instanton and monopole numbers
(k, l). If E supports an α-ﬂat connection then (k, l) = (0, 0) and thus E is the trivial bundle over
X.
Proof. As discussed before, any α-ﬂat connection can only exist on a bundle E for which
k + 2αl = 0
If α is irrational we already explained that k = l = 0 is automatic.


## Page 39


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 39
For α rational, it suﬃces to show that l vanishes, since the previous equation will force k to
vanish and we will be done. To understand why l vanishes, we must use the fact that l can be
computed as [30, Eq 17]
(50)
l = λ + αΣ · Σ
Here we use the fact the orbifold connection has a locally well deﬁned restriction as an abelian
connection on Σ, so the curvature decomposes as
FA =
 ω
0
0
−ω

when regarded as a 2-form on Σ. The quantity λ can then be computed as
λ = i
2π
Z
Σ
(−ω)
In the case of a ﬂat connection it is clear that ω = 0 thus λ = 0. Since Σ · Σ = 0 equation 50 now
implies that l = 0, as desired.
□
This means that for counting α-ﬂat connections we can simply concentrate on the case k = l = 0,
for which the expected dimension of the moduli space is 49
dim M(X, Σ, 0, 0, α) = −2(g −1)
So it is now clear that the expected dimension of the moduli space of α-ﬂat connections is zero
dimensional if and only if g = 1, i.e, Σ must be an embedded torus T . In this case the energy and
dimension formulas become
dim M(X, T, k, l, α) = 8k + 4l
(51)
E(X, T, k, l, α) = k + 2αl
Our next objective will be to analyze which further hypothesis on T must be made in order to
have a well deﬁned invariant λF O(X, T, α).
But ﬁrst, we also analyze what are the possible α-ASD instantons which are reducible on (X, Σ).
Lemma 27. Suppose that E is an SU(2) bundle over (X, Σ) with instanton and monopole numbers
(k, l). If E supports an α-ASD connection which is reducible then (k, l) = (0, 0) and thus E is the
trivial bundle over X.
Proof. We follow the remarks after Proposition 5.9 in [32], more speciﬁcally the remark “iii)
Transversality”.
For an α-reducible ASD connection the bundle E must ﬁrst of all split glob-
ally as E = L ⊕L−1, where L is a complex line bundle which admits an α-ASD connection. This
in turn can be represented by a smooth, harmonic, anti-self-dual 2-form ω whose cohomology class
represents c1(L) + α[Σ]. Again, because b2(X) = 0 this means in fact that ω represents the class 0,
i.e, it must be an α-ﬂat twisted connection. But we already know from Lemma 26 that this forces
k and l to be both zero so we are done.
□
Back to the case where Σ = T , we need to discuss under which conditions we can expect to deﬁne
a count of α-representations π1(X\T ) →SU(2). As in the case of a knot K inside a homology sphere
Y , we have to guarantee that the α-reducible representations are isolated from the α-irreducible
representations. To analyze the α-reducible representations we need to consider the ﬁrst homology
of the torus complement, i.e, H1(X\T ; Z). Now, H1(X\T ; Z) will be sensitive on the embedding of
the torus, for example, T could be null-homologous or not. In fact, we are interested in the case


## Page 40


Mariano Echeverria
40
where T is homologically indistinguishable from the product situation S1 × K ⊂S1 × Y , so we will
make the following assumption.
Assumption 28. T will be an embedded torus inside X such that the natural map H1(T ; Z) ։
H1(X; Z) is a surjection.
More precisely, if we take our torus T to be the image of an embedding ıT : S1 × S1 ֒→X, then
we will assume that ϑ = (ıT )∗(S1 × {pt}) is a generator of H1(X; Z). A tubular neighborhood of T
looks like T × D2, and if we use polar coordinates (r, θ) for the second factor, then
H1(X\T ; Z) ≃Z[ϑ] ⊕Z[µT ]
where µT is a “meridian” for the torus T , and can be represented for example as (ıT ×D2)∗({pt} ×
S1 × (ǫ, 0)), where ǫ is suﬃciently small.
If ρ is an α ﬂat connection then we want to understand the Zariski tangent space ˇH1( ˇX; gρ).
Just as in Lemma 16 we have:
Lemma 29. Suppose α ∈Q ∩(0, 1/2) and that ρ is an α-ﬂat connection on the orbifold ˇX. Then
the ﬁrst (orbifold) cohomology ˇH1( ˇX; gρ) can be identiﬁed with ker : H1(X\T ; gρ) →H1(µT ; gρ).
Proof. The argument is completely analogous. Namely, after applying a Mayer-Vietoris decompo-
sition to
ˇX = ( ˇX\ˇνǫ(T )) ∪ˇν(T )
we end up with the analogue of equations 30 and 31
ˇH1( ˇX; gρ) →(ı∗
X\T ,ı∗
ν(T )) H1(X\T ; gρ) ⊕(R[λT ] ⊕R[ϑ]) →
i∗
Tǫ,ν(K)−i∗
Tǫ,Y \K R[µT ] ⊕R[λT ] ⊕R[ϑ]
The composition being 0 now says that ˇω →
D
ω |S1µT , [µT ]
E
vanishes, so there is a map ˇH1( ˇX; gρ) →
ker(H1(X\T ; gρ) →H1(µ; gρ)). The surjectivity and injectivity of this map are proven in exactly
the same way as before.
□
In particular, for an α-reducible representation ρ we have gρ = R ⊕L⊗2 and thus
ˇH1( ˇX; gρα)
≃ker
 H1(X\T ; R) ⊕H1(X\T ; L⊗2) →H1(µT ; R) ⊕H1(µT ; L⊗2)

≃ker
 R[ϑ] ⊕R[µT ] ⊕H1(X\T ; L⊗2) →R[ϑ]

≃R[µT ] ⊕H1(X\T ; L⊗2)
So at an α-reducible representation ρ, ˇH1( ˇX; gρα) is at least one dimensional, and for ρ to be
isolated from the irreducible representations it suﬃces to assume that H1(X\T ; L⊗2) vanishes.
Using [15, Corollary 65], we can characterize this in terms of the Alexander polynomial of the torus
complement X\T .
Corollary 30. Let α ∈Q ∩(0, 1/2) and T be an embedded oriented torus such that H1(T ; Z) ։
H1(X; Z). Then ˇH1( ˇX; gρ) is one dimensional for every α-reducible representation ρ if and only if
H1(X\T ; L⊗2
ρ ) = 0, where gρ = R⊕L⊗2
ρ . Equivalently, for every α-reducible representation we have
△X\T (ˆρ) ̸= 0, where ˆρ ∈
\
π1(X\T ) is the character determined by the local system H1(X\T ; L⊗2).
Remark 31. For the examples of embedded tori we will analyze, we ﬁnd it easier to verify directly
that H1(X\T ; L⊗2) = 0 vanishes, rather than using the condition on the Alexander polynomial,
since our constructions will arise from some operation on a knot inside an integer homology sphere.


## Page 41


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 41
It would be interesting to study an example of an embedded torus where it is easier to verify the
condition on the Alexander polynomial directly. It would probably need to be more four dimensional
in nature.
Notice that whenever the previous condition is satisﬁed then the obstruction space (i.e, the
second cohomology group ˇH2( ˇX; Aρ) of the deformation complex deﬁned by ρ as a solution of the
α-ASD equations) must vanish. This is because the Euler characteristic of the deformation complex
is (minus) the virtual dimension of the moduli space, which is zero in our situation, so
dim ˇH0( ˇX; Aρ) −dim ˇH1( ˇX; Aρ) + dim ˇH2( ˇX; Aρ) = 0
The ﬁrst factor is 1 because that is the dimension of the stabilizer of Aρ and the one in the middle
is also 1 by assumption so that forces ˇH2( ˇX; Aρ) to vanish.
Now we are ﬁnally ready to give a deﬁnition λF O(X, T, α).
Deﬁnition 32. Suppose that α ∈Q ∩(0, 1/2) and T be an oriented embedded torus such that
H1(T ; Z) ։ H1(X; Z).
Suppose moreover that for every α-reducible representation ρ we have
H1(X\T ; L⊗2) = 0, where gρ = R ⊕L⊗2. Choose a homology orientation for (X, T ), that is, an
orientation of H1(X; Z), which in turn is determined by the orientation of T . Given this homology
orientation, there is an orientation of the moduli spaces M(X, T, k, l, α) [34, Section 2.i)]. We deﬁne
the singular Furuta-Ohta invariant λF O(X, T, α) as follows.
Choose the trivial SU(2) bundle E →X corresponding to the instanton and monopole num-
bers k = l = 0.
Then, after perturbations if necessary, the irreducible α-ASD connections
M∗(X, T, 0, 0, α) will form a 0-dimensional compact moduli space. We deﬁne λF O(X, T, α) ∈Z as
the signed count of elements inside M∗(X, T, 0, 0, α).
Remark 33. The perturbations we have in mind for the statement of the previous theorem are
exactly the same as the interior holonomy perturbations that were needed to deﬁne the cobordism
maps for the Floer groups HI(Y, K, α).
Despite the fact that λF O(X, T, α) is morally deﬁned as a count of ﬂat connections, it is important
to notice that it is the equation F +
A = 0 which is perturbed, not the ﬂatness equation FA = 0. In
other words, λF O(X, T, α) is better interpreted as a degree 0 Donaldson invariant.
This raises the question of whether this is the only degree 0 Donaldson invariant which can be
deﬁned for the embedded torus T . In fact, it is possible to deﬁne additional invariants D0(X, T, α, k)
where k ∈Z is an integer, and provided α ̸= 1/4. Interestingly enough, for k ̸= 0, the invariants
D0(X, T, α, k) can be deﬁned for any embedded torus, independent of whether it is null-homologous
or not. To see why this is the case, we need to go back to the formulas 51 for the energy and
dimension of the moduli spaces
dim M(X, T, k, l, α) = 8k + 4l
E(X, T, k, l, α) = k + 2αl
Notice that M(X, T, k, l, α) is zero-dimensional whenever
l = −2k
The corresponding energy of this moduli space is
E(X, T, k, −2k, α) = k(1 −4α)
In particular, when α = 1/4, the energy of M(X, T, k, −2k, 1/4) is zero, which means it can only
consist of α-ﬂat connections. But we already know from Lemma 26 that this can only happen when


## Page 42


Mariano Echeverria
42
k = 0, which means that
k ̸= 0 =⇒M(X, T, k, −2k, 1/4) = ∅
However, when α ̸= 1/4, the moduli spaces M(X, T, k, −2k, α) are a priori non-empty, at least
provided that E(X, T, k, −2k, α) ≥0. A more important question is whether they are compact.
Since they are already 0 dimensional, the only way for M(X, T, k, −2k, α) to be non-compact is
if a sequence of α-ASD connections [Ai] inside M(X, T, k, −2k, α) bubbles oﬀand converges weakly
to an α-ASD connection [A∞] on some moduli space M(X, T, k′, l′, α) of negative dimension. In
fact, since bubbles drop dimensions by 4, dim M(X, T, k′, l′, α) ≤−4. Fortunately, by Lemma 27,
M(X, T, k′, l′, α) can admit no reducible α-ASD connections, so for generic perturbations there is
no risk in assuming that M(X, T, k′, l′, α) is empty (this is explained in great detail in [31, Sections
3 and 5]).
Therefore, for generic perturbations M(X, T, k, −2k, α) is in fact compact, and a count of signed
points in M(X, T, k, −2k, α) will be independent of the perturbation chosen, because a path of
perturbations will generically miss non-empty negative dimensional moduli spaces. Notice that for
k ̸= 0, α ̸= 1/4, M(X, T, k, −2k, α) has no reducibles to begin with, which in particular means
that the count of signed points inside M(X, T, k, −2k, α) can be made regardless of whether T is
null-homologous or not.
These observations allows us to deﬁne the additional invariants D0(X, T, k, α) we promised ear-
lier.
Deﬁnition 34. Suppose that α ∈Q ∩(0, 1/2) and k ∈Z\{0} is a non-zero integer such that
k(1 −4α) ≥0. Let T be a oriented embedded torus inside X (null-homologous or not). After
choosing an orientation of H1(X; R), deﬁne D0(X, T, k, α) as the signed count of points inside the
moduli space M(X, T, k, −2k, α) = M∗(X, T, k, −2k, α). When α = 1/4, set D0(X, T, k, 1/4) = 0.
Remark 35. Notice that the choice of homology orientation is no longer determined in a canonical
way by an orientation of T , if we allow T to be null-homologous.
Also, it is not all clear what is the geometric meaning of the invariants D0(X, T, α, k). It is
possible they may not contain any interesting topological information about the torus T .
For
example, if we could solve the issue of the implicit dependence of the invariants on the cone angle
being used, and moreover if we succeeded in deﬁning them for irrational values of α as well, then
one could try to use a deformation argument to show that for k ̸= 0, D0(X, T, α, k) must vanish,
since in this case D0(X, T, α, k) could be compared to D0(X, T, 1/4, k), which we already know
vanishes.
Likewise, we can construct an analogue of the invariants D0(X, T, α, k) for the case of an embed-
ded sphere S2 ֒→X. Namely, the expected dimension of the moduli spaces M(X, S2, k, −2k, α)
is now 2, as can be seen from the formula 49. As long as α ̸= 1/4 and k ̸= 0, some of these
moduli spaces could be non-empty, and they will be compact and free of reducibles by a similar
argument. Hence, by pairing them with µS2(x) for x ∈S2, we can deﬁne a degree-two Donaldson
invariant D2(X, S2, k, α). However, the fact that these invariants cannot be deﬁned when α = 1/4
(which is the best value α could take from many points of view), suggests to us these invariants
D2(X, S2, k, α) will probably end up giving no interesting topological information.
We ﬁnish this section by analyzing the action of H1(X; Z/2) on the moduli spaces M(X, T, k, −2k, α),
as was promised in the introduction. We follow [52, Section 4.6] and [54, Section 3] in order to
describe this action.
First of all, H1(X; Z2) = hom(π1(X); Z2) parametrizes isomorphism classes of complex line
bundles (with connection) χ with holonomy {±1} (along the loop ϑ in our case). Since χ lifts to


## Page 43


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 43
an integral homology class, the bundle Lχ is trivial and thus for any (k, l), the bundles E(k, l) and
E(k, l) ⊗Lχ are isomorphic. Thus the action of H1(X; Z2) on M(X, T, k, −2k, α) can be regarded
as the one which sends a connection [A] to [A ⊗χ].
In general this action may or may not be free. We only care about the freeness of the action
on the irreducible part of the moduli space M∗(X, T, k, −2k, α) (again, when k ̸= 0, this coincides
with the entire moduli space M(X, T, k, −2k, α)), which we will show in the next lemma.
Here we only need to analyze the action on the unperturbed moduli spaces, since the idea is
that once we know the action is free in the unperturbed case, one can ﬁnd perturbations that are
H1(X; Z2) equivariant and still guarantee transversality for the moduli spaces [52, section 4.6].
Lemma 36. Suppose that the (unperturbed) moduli space M∗(X, T, k, −2k, α) is non-empty. Then
H1(X; Z/2) acts freely on M∗(X, T, k, −2k, α).
Proof. Let [A] ∈M∗(X, T, k, −2k, α) be an irreducible α-ASD connection.
The connection A
induces a connection Aad on the adjoint bundle Ead(k, −2k) of E(k, −2k). On the adjoint bundle
it makes sense to consider the gauge group GSO(3)(X, T ) of all SO(3) gauge transformations (as
opposed to the SU(2) gauge transformations which are the ones we have been working with). As
in the non-singular case (i.e, when T is not present), it is still the case that [35, Section 5.1]
GSO(3)(X, T )/(G(X, T )/{±1}) ≃H1(X; Z/2)
Therefore, the action of H1(X; Z/2) is free on [A] if and only if the stabilizer of Aad with respect to
the full gauge group GSO(X, T ) is trivial. In general, since A is irreducible with respect to G(X, T ),
stabSO(3)Aad can only be one of three possibilities: 1, Z2 or the Klein-4 group V4. Therefore we
must rule out that Z2 and V4 can arises as potential stabilizers.
The case of V4 is easy: a connection A with stabilizer V4 must be ﬂat [54, Section 4], and
thus cannot belong to M(X, T, k, −2k, α) for k ̸= 0, since these a priori do not support any ﬂat
connections.
In the case that k = 0 but α ̸= 1/4, we just need to use the fact that every α-representation
ρ such that ρad has stabilizer V4 also has holonomy V4, hence ρad will correspond in general to
representations of π1(X\T ) with image into V4 ⊂SO(3) ([54, Section 4], [37, Examples 2.9]).
Given that every element of V4 has order 2, the only value of α compatible with V4 representations
corresponds to α = 1/4. Notice that ρ will then have image contained in the quaternionic subgroup
Q8 = {±1, ±i, ±j, ±k} when we identify SU(2) with the unit quaternions.
For the case of k = 0 and α = 1/4, we need to use the fact that the existence of Klein-4
representations is a homological phenomenon.
Namely, they exist whenever one can ﬁnd three
nontrivial real line bundles which are distinct [54, Section 3] on the manifold. In our case, the
manifold to consider is X\nbd(T ), where nbd(T ) is an open neighborhood of the torus T . Since
H1(X\nbd(T ); Z2) ≃Z2 ⊕Z2, one can ﬁnd three distinct nontrivial real line bundles which deter-
mines a Klein-4 representation. Call these (real) line bundles ǫ1, ǫ2, ǫ3 = ǫ1 + ǫ2, where ǫ1 generates
the ﬁrst factor of H1(X\nbd(T ); Z2), while ǫ2 generates the second factor. It is easy to see that in
this case
w2(Ead |X\nbd(T ))
=w2 (ǫ1 ⊕ǫ2 ⊕ǫ3)
=w1(ǫ1)w1(ǫ2) + w1(ǫ1)w1(ǫ3) + w1(ǫ2)w1(ǫ3)
=w1(ǫ1)w1(ǫ2) + [w1(ǫ1)]2 + w1(ǫ1)w1(ǫ2) + w1(ǫ2)w1(ǫ1) + [w1(ǫ2)]2
=w1(ǫ2)w1(ǫ1) ̸= 0


## Page 44


Mariano Echeverria
44
In other words, the Klein 4 representation we found exists on a bundle with non-trivial w2. How-
ever, the bundle Ead(0, 0) over X has vanishing w2 (since X is an integral homology S1 × S3, or
alternatively, because E(0, 0) was the trivial bundle to begin with), which means that its restriction
to the torus complement should have vanishing w2 as well by naturality of the Stiefel-Whitney
classes. Therefore, M∗(X, T, 0, 0, 1/4) is also free of connections with stabilizer V4 (with respect to
GSO(3)(X, T )).
The case of Z2 stabilizer corresponds to the so-called twisted reducibles [33, Section 2 i)]: these
are those connections which preserve a splitting gE = λ ⊕P , where now λ is a non-orientable real
line bundle and P is a non-orientable real two plane bundle with orientation bundle isomorphic to
λ. Now we can use the fact that our connections have a prescribed model near the surface T : as
explained before Lemma 2.22 in [33], if A were a twisted reducible, then P would have to coincide
with ±L⊗2 in a tubular neighborhood of T , and therefore λ must be trivial on T .
Now, because H1(T ; Z2) maps onto H1(X; Z2), then λ will be trivial on all of X, which means
that it is orientable, thus we obtain a contradiction. Notice that the paragraph we refer to from
[33] starts by stating that A must be a non-ﬂat connection. However, this condition is not used
in this argument, rather it was assumed by Kronheimer and Mrowka because they were interested
in obtaining a generic metrics theorem in the presence of twisted reducibles, and in general this
cannot be achieved whenever there are ﬂat connections.
□
Remark 37. Since for k ̸= 0, α ̸= 1/4, the moduli spaces M(X, T, k, −2k, α) are free of reducible
α-ASD connections, free of α-ﬂat connections and free of twisted reducible connections, one can
also obtain transversality for these moduli spaces using the generic metrics theorem, thanks to [33,
Lemma 2.17]. Hence, one could avoid using holonomy perturbations for deﬁning the invariants
D0(X, T, k, α) for k ̸= 0.
Before discussing some examples and properties of λF O(X, T, α, k), we will prove the splitting
formula for λF O(X, T, α, k), which was one of our main motivations for deﬁning the invariant.
7. The Splitting Formula
Our ﬁrst step for ﬁnding the splitting formula requires understanding how α-admissibility for
self-concordances (W, Σ) : (Y, K) →(Y, K) is related to the reducible representations being isolated
from the irreducible representations in the case of (X, Σ). The next lemma says that in fact both
notions are equivalent.
Lemma 38. Suppose that (W, Σ) : (Y, K) →(Y, K) is a self-concordance of a knot and we choose
a parameter α for which △K(e−4πiα) ̸= 0. Let (X, T ) be the closed 4-manifold obtained by closing
up (W, Σ). Then λF O(X, T, α) is well deﬁned if and only if the cobordism (W, Σ) is α-admissible.
Proof. We can think of (X, T ) as being obtained from (W, Σ) after attaching a tube (I × Y, I × K)
to the boundary of (W, Σ), where I is some interval. That is,
(X, T ) = (W, Σ) ∪(I × Y, I × K)
Then we want to apply Mayer-Vietoris to this decomposition of (X, T ), where we enlarged I a little
bit so that the overlap of (W, Σ) with (I × Y, I × K) is the disjoint union
(W, Σ) ∩(I × Y, I × K) = (I1 × Y, I1 × K) ⊔(I2 × Y, I2 × K)
where I1, I2 are two small subintervals. Recall that on the orbifold ˇW there is only one α-ﬂat
reducible θW,α , while on Y we have the reducible θα. For any α-ﬂat reducible Aρ on ˇX, it must


## Page 45


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 45
restrict to θW,α and θα on ˇW and ˇY respectively, which means that exact sequence for the (orbifold)
cohomology groups reads
0 →ˇH0( ˇX; gρ)
→ˇH0( ˇ
W; gθW,α) ⊕ˇH0(I × ˇY ; gθα)
→ˇH0(
 I1 ⊔I2 × ˇY

; gθα)
→ˇH1( ˇX; gρ)
→ˇH1( ˇ
W; gθW,α) ⊕ˇH1(I × ˇY ; gθα)
→ˇH1((I1 ⊔I2) × ˇY ); gθα)
→· · ·
Since △K(e−4πiα) ̸= 0, we have that ˇH1( ˇY ; gθα) = 0 so we can simplify the previous exact sequence
into
0 →R
→R ⊕R
→R ⊕R
→ˇH1( ˇ
X; gρ)
→ˇH1( ˇ
W ; gθW,α)
→0
→· · ·
From this we can conclude that the alternating sum of the dimensions of these vector spaces is zero,
which means that
dim ˇH1( ˇX; gρ) = 1 + dim ˇH1( ˇW; gθW,α)
Thus, if (W, Σ) is α-admissible (i.e, dim ˇH1( ˇW; gθW,α) = 0) then ˇH1( ˇX; gρ) vanishes for all α-
reducible representations ρ, and conversely, if λF O(X, T, α) can be deﬁned (i.e, dim ˇH1( ˇX; gρ) = 1)
then dim ˇH1( ˇ
W; gθW,α) must vanish which is the condition for the cobordism to be α-admissible.
□
We are ﬁnally ready to state the splitting formula.
Theorem 39. (Splitting Theorem) Suppose that (W, Σ) : (Y, K) →(Y, K) is a self-concordance
of a knot and we choose a parameter α ∈Q ∩(0, 1/2) for which △K(e−4πiα) ̸= 0. Let (X, T ) be
the closed 4-manifold obtained by closing up (W, Σ). Suppose that λF O(X, T, α) is well deﬁned, or
equivalently, that (W, Σ) is α-admissible. Then we have the splitting formula
(52)
X
k
D0(X, T, α, k)T −Etop(X,T,k,−2k,α) = 2Lef(W | HI(Y, K, α)) = 2Lef(W | HIred(Y, K, α))−2h(Y, K, α)
Proof. (ﬁrst equality of Theorem 39) The argument is standard and analogous to the one given in
[21, Section 11], [20, Section 11.1] and [43, Section 9]. In fact, since we already analyzed the action
of H1(X; Z/2) on the moduli spaces, as we mentioned in the introduction, it can be regarded as a
consequence of Proposition 5.5 in [35] and the remarks after it.
Namely, the idea is to compare the moduli spaces M∗(X, T, k, −2k, α) (k ∈Z) with the 0-
dimensional moduli spaces M0([β], W, [β]), i.e, those which are asymptotic to [β] as t →±∞.


## Page 46


Mariano Echeverria
46
Notice that because of the failure of monotonicity, specifying the dimension is not enough (when
α ̸= 1/4), i.e, M0([β], W, [β]) needs to be furthermore indexed by the energy of the moduli space
M0([β], W, [β]) =
[
k∈Z
M0,E(k)([β], W, [β])
Now, we can focus on one of the individual moduli spaces M∗(X, T, k, −2k, α) and introduce a
parameter R which keeps track of the length of the cylinder in the usual stretching the neck
argument, so that we are consider the manifold ˇX(R) where a cylinder of length 2R [−R, R] × ˇY
has been introduced along ˇY .
The gluing argument says that for R suﬃciently large, M∗(X, T, k, −2k, α) can be identiﬁed with
S
[β]∈C∗(Y,K,α) M0,E(k)([β], W, [β]). Notice that we do not need to worry about M0,E(k)([θα], W, [θα])
because of the α-admissibility condition.
However, this correspondence is two to one, since when we are closing the bundle over W ∗to
produce the bundle over X, there are two ways to do this since the stabilizer of [β] is Z2 = Z(SU(2)),
given that we are dealing with an irreducible connection [36, Remark p.893]. This explains the factor
of 2 in the statement of the theorem.
□
Now we will proof the second part of the Splitting Theorem. The proof is an adaptation word
by word of the one Anvari gives in [2], so we will just illustrate one of the cases needed to proof
this formula, the other one can be found in the annotated version [15].
Proof. (second equality of Theorem 39) We start by recalling the behavior of the maps
δ1,n =δ1un
K : HI1+2n(Y, K, α) →Λ
δ2,n =un
Kδ2 : Λ →HI2−2n(Y, K, α)
which appear implicitly in our deﬁnition of the reduced Floer groups 45. In the case of a self-
concordance (W, Σ), the induced cobordism map m ˇ
W : HI∗(Y, K, α) →HI∗(Y, K, α) acts on the
δ1,n and δ2,n as follows [18, Theorem 7]: there are integers aij, bij such that
δ1,nm ˇ
W =δ1,n +
n−1
X
i=0
ainδ1,n
(53)
m ˇ
W δ2,n =δ2,n +
n−1
X
i=0
binδ2,n
Since m ˇ
W preserves gradings we can see that ain = 0 and bin = 0 whenever i, n have opposite parity.
We will also use the fact (which follows from Lemma 44) that either δ1 or δ2 must vanish. Finally,
we also need the fact that for a commutative diagram of exact sequences of ﬁnite dimensional vector
spaces over an arbitrary ﬁeld Λ
0 →
V0 →
V1 →
V2
↓α
↓β
↓γ
0 →
W0 →
W1 →
W2
we have
(54)
tr(β) = tr(α) + tr(γ)
To show that
(55)
h(Y, K, α) = Lef(W | HIred(Y, K, α)) −Lef(W | HI(Y, K, α))


## Page 47


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 47
we make cases based on the vanishing of δ1, δ2.
Case δ2 = 0: In this situation the reduced Floer groups 45 simplify to









HIred
1
(Y, K, α) = ∩l ker(δ1,2l)
HIred
3
(Y, K, α) = ∩l ker(δ1,2l+1)
HIred
0
(Y, K, α) = HI0(Y, K, α)
HIred
2
(Y, K, α) = HI2(Y, K, α)
Therefore the diﬀerence in Lefschetz numbers simpliﬁes to
Lef(W | HIred(Y, K, α)) −Lef(W | HI(Y, K, α))
=Tr(W | HI1(Y, K, α) ⊕HI3(Y, K, α)) −Tr(W | HIred
1
(Y, K, α) ⊕HIred
3
(Y, K, α))
=Tr(W | HI1(Y, K, α)) −Tr(W | HIred
1
(Y, K, α)) + Tr(W | HI3(Y, K, α)) −Tr(W | HIred
3
(Y, K, α))
In this case h(Y, K, α) 46 simpliﬁes to
χΛ(HIred(Y, K, α)) −χΛ(HI(Y, K, α))
= −dimΛ HIred
1
(Y, K, α) −dimΛ HIred
3
(Y, K, α) + dimΛ HI1(Y, K, α) + dimΛ HI3(Y, K, α)
= dimΛ HI1(Y, K, α) −dimΛ HIred
1
(Y, K, α) + dimΛ HI3(Y, K, α) −dimΛ HIred
3
(Y, K, α)
= dimΛ(HI1(Y, K, α)/ ∩l ker(δ1,2l)) + dimΛ(HI3(Y, K, α)/ ∩l ker(δ1,2l+1))
So it clearly suﬃces to show that
dimΛ(HI1(Y, K, α)/ ∩l ker(δ1,2l)) = Tr(W | HI1(Y, K, α)) −Tr(W | HIred
1
(Y, K, α))
dimΛ(HI3(Y, K, α)/ ∩l ker(δ1,2l+1)) = Tr(W | HI3(Y, K, α)) −Tr(W | HIred
3
(Y, K, α))
to obtain our result. The argument is completely analogous in both cases, so let us do verify the
second identity. The result will be obtained from induction on the sequence of subspaces
Z3,k = ∩k
l=0δ1,2l+1
From 53 we can see that for k = 0 we have δ1m ˇ
W = δ1, which in other words means that there is
an exact sequence
0 →
Z3,0 →
HI3 →δ1
Λ
↓m3,0
↓m ˇ
W
↓id
0 →
Z3,0 →
HI3 →δ1
Λ
Here m3,0 denotes the restriction of the cobordism map to Z3,0. The additivity of the trace formula
54 now says that
tr(m ˇ
W ) = tr(m3,0) + tr(id) = tr(m3,0) + 1 = tr(m3,0) + dimΛ(HI3(Y, K, α)/Z3,0)
provided that δ1 ̸= 0 (which in any case is the only interesting situation since we already assumed
that δ2 = 0). An induction argument on k [2, p. 7] based on the identities 53 now says that
tr(m ˇ
W ) = tr(m3,k) + dim(HI3(Y, K, α)/Z3,k)
Since the sequence of the Z3,k stabilizer once k is large enough then we ﬁnd that
tr(m ˇ
W | HI3(Y, K, α)) −tr(mred
ˇ
W | HIred
3
(Y, K, α)) = dim(HI3(Y, K, α)/Z3,k)
Again, the case for HI1(Y, K, α) is completely analogous so 55 has been veriﬁed in this situation.


## Page 48


Mariano Echeverria
48
Finally, the case δ1 = 0 is dealt with in a similar way, but the interested reader can ﬁnd a proof
in [15].
□
Now we will show that under the previous circumstances (X, T ) can be assigned an h-invariant.
Theorem 40. Suppose that (X, T ) can be written as the closed-up version of two diﬀerent self-
concordances (W, Σ) : (Y, K) →(Y, K) and (W ′, Σ′) : (Y ′, K′) →(Y ′, K′) which satisfy △K(e−4πiα) ̸=
0 and △K′(e−4πiα) ̸= 0 for some α ∈Q ∩(0, 1/2). Suppose λF O(X, T, α) can be deﬁned, or equiv-
alently, either of the concordances (and hence the other) is α-admissible. Then
Lef(W | HIred(Y, K, α)) = Lef(W | HIred(Y ′, K′, α))
and thus we can use the splitting formula 52 to deﬁne h(X, T, α) as h(Y, K, α) = h(Y ′, K′, α).
Proof. The proof is indistinguishable from the one Frøyshov gives for monopole h-invariant in [21,
Section 13]. First Frøyshov proves Lemma 10 in [21], which in our case translates to the following
statement: let A, B be r×r matrices with coeﬃcients in the universal Novikov ﬁeld ΛC,R , and let m
be a natural number such that tr(An) = tr(Bn) for all natural numbers n satisfying m ≤n < 2r+m.
Then A and B have the characteristic polynomial, and in particular tr(A) = tr(B).
Frøyshov states this Lemma for matrices with coeﬃcients over the complex ﬁeld C, but a quick
inspection of the proof reveals that the only property used about C is that it is algebraically closed,
so that the characteristic polynomial of A (or B) has roots, which are the eigenvalues of A (or B).
That ΛC,R is algebraically closed is proven in [23, Lemma A.1]. Once we know this lemma holds,
the argument Frøyshov gives is the same, just replace every occurrence of X, W, Y, X∞, Xj,∞, Wj,n
,etc in his proof with their orbifold versions ˇX, ˇW, ˇY , ˇX∞, ˇXj,∞, ˇWj,n.
To give more details, as in [21, Section 13] one assumes that Y, Y ′ are the inverse images of maps
f : X →S1, f ′ : X →S1 in such a way that f −1(1) = Y , f ′−1(1) = Y ′. The important features
of these maps is that they were homotopic through some map F : [0, 1] × X →S1, since Y, Y ′
represented the same class in H3(X; Z) ≃H1(X; Z) ≃[X, S1].
Now, if we let XT = X\T denote the torus complement there is no problem in assuming that as
maps fT = f : XT →S1, f ′
T = f ′ : XT →S1, we also have that f −1(1) = Y \K, f −1(1) = Y ′\K′.
Since T ∩Y = K and T ∩Y ′ = K′, by restricting F to [0, 1] × XT , we ﬁnd out that that fT , f ′
T
are homotopic as well (as elements of [XT , S1]), which means that the inﬁnite cyclic covers they
determine are in fact diﬀeomorphic. After that Frøyshov’s argument goes through.
□
8. Some examples and Properties
Product Case.
As a corollary of the splitting theorem 39 we can verify our basic desiderata for λF O(X, T, α).
Corollary 41. Suppose that (Y, K) is such that △K(e−4πiα) ̸= 0 for α ∈Q ∩(0, 1/2). Then
λF O(X, T, α) can be deﬁned on (X, T ) = (S1 × Y, S1 × K).
Moreover, λF O(X, T, α) = 2λCLH(Y, K, α) and the additional degree zero Donaldson invariants
D0(X, T, α, k) vanish for k ̸= 0.
Proof. In this case the self-concordance is (W, Σ) = ([0, 1] × Y, [0, 1] × K) which will clearly be
α-admissible.
According to the splitting formula 52 we have for (X, T ) = (S1 × Y, S1 × K)
X
k
D0(X, T, α, k)T −E(X,T,k,−2k,α) = 2Lef(Id | HI(Y, K, α)) = 2χΛ(HI(Y, K, α)) = 2λCH(Y, K, α)


## Page 49


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 49
from which we will conclude that
(
λF O(S1 × Y, S1 × K, α) = 2λCH(Y, K, α)
D0(X, T, α, k) = 0
k ̸= 0
□
Remark 42. In particular, notice that one cannot use the invariants D0(X, T, α, k) (for k ̸= 0) to
obtain new invariants for knots, as one might have suspected all along.
Flip symmetry.
Now we brieﬂy discuss the proof of Theorem 11 from the introduction, i.e, the ﬂip symmetry
F obtained by changing the holonomy parameter from α to 1
2 −α. This is deﬁned similar to the
action of H1(X; Z/2), in the sense that there is a natural map F : M(X, T, k, l, α) →M(X, T, k +
l, −l, 1
2 −α) obtained by tensoring the bundle E(k, l) with a line bundle χ whose holonomy on the
small circles linking T is −1. The new values for k and l after the ﬂip symmetry is performed were
computed in [32, Section 2, iv)].
Moreover, in [34, Appendix 1, ii)] they discuss the eﬀect of F on the orientation of the moduli
spaces. In particular, F preserves or reverses orientation according to the parity of 1
4T ·T −(g −1),
which in our case vanishes, which means that F is orientation preserving.
Recalling that D0(X, T, k, α) was computed using M(X, T, k, −2k, α), this means that D0(X, T, k, α) =
D0
 X, T, −k, 1
2 −α

as was claimed in Theorem 11.
The eﬀect on the Floer homologies F : HI(Y, K, α) →HI(Y, K, 1
2 −α) can be analyzed in a
similar way. The only thing to worry about is about the eﬀect of F on the gradings of a critical point
before and after the ﬂip has been performed. Clearly F([θα]) = F([θ1/2−α]) and more generally
F(M([β], [θα]) = M([Fβ], [θ1/2−α]) which from the formula for the absolute grading 11 will imply
that gr([Fβ]) = gr([β]), in other words, F will be grading preserving. In particular, the Euler
characteristic is preserved under the ﬂip operation, which could also be checked directly from the
formula for λCLH(Y, K, α).
The eﬀect of F : HIred(Y, K, α) →HIred(Y, K, 1
2 −α) can be analyzed in a similar way. The only
thing to be aware of is that under F the u-map µK(x) changes sign, i.e, F(µK(x)) = −µK(x), as is
discussed in [30, Section 4.2]. However, changing the sign of the u map still is compatible with the
deﬁnition of the reduced Floer groups 45 so the Euler characteristic of HIred(Y, K, α) is preserved
under ﬂip symmetries. From the formula for the Frøyshov knot invariants 46 it is immediate that
h(Y, K, α) = h(Y, K, 1
2 −α), which was the ﬁrst statement of Theorem 11.
Duality. Just as for the non-singular versions, the Floer groups HI(Y, K, α) are related to those
of HI(−Y, −K, α), where (−Y, −K) denotes the pair (Y, K) with the opposite orientation on both
factors. When there is no knot present, the way to understand the Floer homology HI(−Y ) in
terms of the Floer homology HI(Y ) is standard, what we need to do discuss is that happens in the
presence of the knot K as well as the eﬀect on the local systems Γ[β]. We will follow the discussion
in [38, Sections 22.5 and 32.1], [55, Section 7.4].
The Chern-Simons functionals CS ˇY and CS−ˇY on the orbifolds ˇY and −ˇY are related as
CS ˇY = −CS−ˇY
Therefore the critical points of the functionals can be identiﬁed in a natural way with each other.
The perturbation on −Y can be taken to be −p, while the vector ﬁeld gradCS−ˇY is the negative
of gradCS ˇY . In other words, if γ(t) is a trajectory on ˇY of CS ˇY then γ(−t) is a trajectory on
−ˇY of CS−ˇY . The coeﬃcient system on −ˇY can be described as a coeﬃcient system on B( ˇY , α) =


## Page 50


Mariano Echeverria
50
B(Y, K, α), by saying that the ﬁber at each point is still ΛQ,R, but now along paths z from [β0] to
[β1] one multiplies by T +Etop(z) instead of T −Etop(z).
To obtain the grading formula, consider the cylinders R × ˇY and R × −ˇY . Let [β] ∈C(Y, K, α)
be a critical point and [¯β] the corresponding class in C(−Y, −K, α). Recall that 34
gr([β]) = −1 −dim M([θα], [β])
mod 4 = dim M([β], [θα])
mod 4
A ﬂow line on the moduli space M([¯β], [¯θα]) can be identiﬁed with a ﬂow line of the moduli space
M([θα], [β]), since the time direction has been reversed, which means
gr([¯β]) = M([¯β], [¯θα])
mod 4 = dim M([θα], [β])
mod 4 = −1 −gr([β])
Therefore we have found ([9, Proposition 4.3]):
Theorem 43. For each i ∈Z/4Z, there is an isomorphism
(56)
HIi(−Y, −K, α) ≃HI−i−1(Y, K, α)
Some examples of tori inside mapping tori.
These examples can be considered as the orbifold version of [51].
Before writing a general
statement, let’s consider a toy model. Suppose that we have a knot K′ inside an integer homology
sphere Y ′ and we choose holonomy α′ =
1
15 along the K′.
Moreover, assume that after taking the 3-fold branched cover along K′ we obtain a 3 manifold Y
which is still an integer homology sphere . Notice that Y comes with a natural Z3 action τ, whose
ﬁxed point set is a knot K. Now choose holonomy α = 1
5 along the knot K. Then the mapping
torus
Xτ = ([0, 1] × Y )/({0} × Y ∼τ {1} × Y )
of (Y, τ) will be a homology S1 × S3 with a natural torus Tτ obtained as the mapping torus of
K ⊂Y . In this situation the analogue of [51, Proposition 3.1] will tell us that there is a two to one
correspondence between α-representations on (Xτ, Tτ) and α-representations on (Y, K) which are
τ-equivariant.
Clearly, every α′- representation of (Y ′, K′) will pullback to an α-representation on (Y, K) which
is τ -equivariant. So the only question is whether this exhausts all the possibilities for being a
τ-equivariant representation. In fact, it does not! Suppose we had chosen holonomy ˜α′ =
6
15 along
K′. Then the pull-back of an ˜α′ representation of (Y ′, K′) will have holonomy 6/5 along K upstairs.
Recall that we are using the normalization for the holonomy to be between 0 and 1/2, and since
6
5 = 1
5 + 2 · 1
2
this means that after performing two half-twists, holonomy 6/5 is equivalent to holonomy 1/5.
As Langte Ma pointed out to the author, there are still more holonomy values allowed. Consider
for example ˜α′ = 11
15 . Since
11
5 = 1
5 + 4 · 1
2
after four half-twists, holonomy 11/5 is equivalent to holonomy 1/5. Moreover, since 1
2 < 11
15 < 1,
due to the normalization conventions we can take this one to be equivalent to holonomy 11
15 −1
2 =
7
30,
in other words,
11
5 ∼7
30


## Page 51


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 51
Holonomy
7
30 pulls up to holonomy
7
10 = 1
5 + 1
2 , which diﬀers from 1
5 by one half-twists. Moreover
σK′(e−4πi 11
15 ) = σK′(e−4πi( 7
30 + 1
2 )) = σK′(e−4πi 7
30 )
so the value of the knot signature is well deﬁned regardless of the identiﬁcation we use.
This exhaust all the possibilities, since
1
5 + 6 · 1
2 = 16
5
which would be induced by holonomy 16
15 downstairs, which is bigger than one, hence can be ignored.
In general all the allowable values of holonomy on (Y ′, K′) which give rise to holonomy α upstairs
will be of the form
α
p + n
p
where n is an any integer such that
0 < α
p + n
p < 1
which clearly means that there are only ﬁnitely many values n can take. In fact, since n must be
an integer and α < 1
2 the only possibilities are
n = 0, 1, · · · , ⌊p −α⌋= p −1
where ⌊⌋denotes the ﬂoor function. In our toy model p = 3 and α = 1/5 so n = 0, 1, 2 are the only
possibilities, which means that α′
0 =
1
15, α′
1 =
6
15 = 3
5, α′
2 = 11
15 are the only holonomy values that
have the desired properties.
Our claim is that in this case
λF O(Xτ, Tτ, α)
=2λCLH(Y ′, K′, α′
0) + 2λCLH(Y ′, K′, α′
1) + 2λCLH(Y ′, K′, α′
2)
=24λC(Y ′) + σK′(e−4πiα′
0) + σK′(e−4πiα′
1) + σK(e−4πiα′
2)
Besides the correspondence between the diﬀerent representation spaces, the other important thing
we need to check is how to compare the orientations between the diﬀerent moduli spaces, and how
to identify the representations in case perturbations are needed. We will address each of these issues
in stages, but ﬁrst we state the main result.
Theorem 44. Let (Y ′, K′) be a pair of an oriented knot inside an integer homology sphere and
take α′ =
r
pq , where p, q, r are all odd integers, relatively prime and such that 0 < α′ < 1
2. Suppose
moreover that 0 < r
q < 1
2 and assume that the p-fold branched cover along K′ is an integer homology
sphere Y . Let K denote the ﬁxed point set of the Zp action τ on Y , which will be another oriented
knot. For α = r
q = pα′ consider the p holonomy values
α0 = α′, α′
1 = α′ + 1
p, · · · , α′
p−1 = α′ + p −1
p
Assume furthermore that for each j = 0, · · · , p, △K′(e−4πiα′
j) ̸= 0 and that the reducible repre-
sentation θα is τ non-degenerate, i.e, ˇH1,τ( ˇY ; gθα) = 0. Denote (Xτ, Tτ) the τ-mapping torus of
(Y, K). Then λF O(Xτ, Tτ, α) is well deﬁned and moreover
λF O (Xτ, Tτ, α) =
p−1
X
j=0
2λCLH
 Y ′, K′, α′
j

= 8pλC(Y ′) +
p−1
X
j=0
σK′(e−4πiα′
j)


## Page 52


Mariano Echeverria
52
Remark 45. i) As mentioned in the acknowledgements section, the ﬁrst version of this paper had a
mistake in the previous formula since we did not count all the possible representations. We would
like to thank Langte Ma for pointing out this mistake.
ii) There are certainly inﬁnitely many examples that satisfy our assumptions. For example, the
Brieskorn spheres Σ(p, a, b) may be realized as the p-fold branched covering of S3 along a torus knot
T (a, b) [7]. A way to guarantee θα is τ isolated as an α representation of π1(Σ(p, a, b)\K) is for it
to be isolated in the ordinary sense, i.e, ˇH1( ˇΣ(p, a, b); gθα) = 0. Since the Alexander polynomial of
both K′ and K have at most a ﬁnite number of roots on the unit circle, there are inﬁnitely many
numbers of the form
r
pq which will serve our purposes.
iii) A statement involving one of the integers p, q being even would be slightly more complicated,
since the center of SU(2) is Z2 and there can be a lifting issue when one tries to lift an action of
Zp for p even on a 3-manifold to an SU(2) bundle [3].
iv) Notice that for 1
2 < α′
j = α′ + j
p < 1 we have σK′(e−4πi(α′
j−1
2 )) = σK′(e−4πiα′
j), so whether
or not we want to “renormalize” α′
j so that it belongs to the interval (0, 1/2) does not aﬀect the
formula.
To keep the proof manageable we will break it into several pieces: ﬁrst we will discuss the
identiﬁcation at the level of the critical sets, then we will address how the Zariski tangent spaces
are related, third we will discuss how to relate the critical sets after perturbations have been
introduced into the picture, and ﬁnally we will discuss how to relate the orientations of the moduli
spaces. Our steps should be regarded as the orbifold version of the corresponding statements in
[51].
First we need to review some brief facts about the orbifold fundamental group, as well as some
aspects about equivariant gauge theory. Our main sources are [3, 7, 8, 51].
At this point it is a matter of preference whether one wants to think we are working over Y \K
or the orbifold ˇY for analyzing the action, so we will change perspectives whenever it is more
convenient.
Over the manifold Y \K we have an action Zp and a principal SU(2) bundle P →Y \K. Let
τ denote the generator of Zp. When one is trying to understand the action of a group on some
principal bundle, one needs to make the assumption that
(57)
τ ∗(P) ≃P
Usually on a closed-4 manifold, this means verifying that the characteristic numbers of the bundle
are preserved (c2(P) in the SU(2) case for example). On any 3-manifold the SU(2) bundles are
necessarily trivial, so one may think that 57 is automatically guaranteed. However, we now need
to take into account that we are working with connections with a prescribed singularity along the
knot, so we need to check that the action of τ preserves the model connection. Conversely, from the
orbifold perspective, this is the same as checking that the isotropy data of the bundle is preserved
[9].
Recall that using a tubular neighborhood for the knot K, the model connection 10 in a trivial-
ization could be understood given by the matrix valued 1-form
i

α
0
0
−α

dθ
where (r, θ) are polar coordinates. We are choosing the action Zp in such a way that it becomes an
isometry and orientation preserving, and from the local model of a branched cover it is not diﬃcult


## Page 53


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 53
to see that Zp acts on the coordinates as
τ · (r, θ) = (r, θ + 2π/p)
Clearly this will preserve dθ and thus the local model of the connection. In other words, we have
veriﬁed the singular (orbifold) analogue of the condition 57. If G(Y, K, α) is the usual gauge group
and G (Y, K, α) the group of bundle automorphisms of P covering an element of Zp, then we have
an exact sequence
(58)
1 →G(Y, K, α) →G (Y, K, α) →Zp →1
There is an action of G (Y, K, α) by pullbacks on the space of connections C(Y, K, α). Let ˜τ : P →P
denote a lift of τ. By 58, for any two lifts ˜τ1, ˜τ2 of τ, there is a gauge transformation g ∈G(Y, K, α)
such that
˜τ2 = ˜τ1 · g
Thus there is a well deﬁned action τ∗on B∗(Y, K, α). We will denote the ﬁxed point set of τ ∗by
Bτ(Y, K, α). Let [B] ∈Bτ(Y, K, α). Then we can ﬁnd a representative B and a lift ˜τ ∈G (Y, K, α)
such that
˜τ ∗B = B
If there were another such ˜τ ′ then ˜τ ′ ◦˜τ −1 would be an element of G(Y, K, α) ﬁxing B, hence it
would belong to the stabilizer of B, which since we assume was irreducible must be Z/2. In other
words
˜τ ′ = ±˜τ
which means ˜τ is well deﬁned up to a sign. Moreover, (˜τ)p is an element of G(Y, K, α) ﬁxing B, so
by the same token
(˜τ)p = ±1
Therefore we can write
(59)
Bτ(Y, K, α) = ⊔[˜τ]B˜τ(Y, K, α)
where the disjoint union is over the lifts such that ˜τ p = ±1 and the equivalence relation is ˜τ1 ∼˜τ2
if and only if ˜τ2 = ±g · ˜τ1 · g−1 for some gauge transformation g ∈G(Y, K, α).
Each B˜τ(Y, K, α) can be described as follows: for a ﬁxed lift ˜τ, let C ˜τ(Y, K, α) denote the
irreducible connections B such that ˜τ ∗B = B. Deﬁne G˜τ(Y, K, α) = {g ∈G(Y, K, α) | g˜τ = ±˜τg}.
Then B˜τ(Y, K, α) = C ˜τ(Y, K, α)/G˜τ(Y, K, α).
We are after the analogue of [51, Proposition 2.1], which will be useful for the discussion of the
spectral ﬂow calculations. Namely, any lift ˜τ : P →P can be written in the base-ﬁber coordinates
as
˜τ(y, f) = (τ(y), σ(y)f)
where σ : Y \K →SU(2). Notice that when we regard it as an orbifold, then the automorphism
σ must be S1 valued along K, because the automorphisms of P, i.e G(Y, K, α), consists of maps
Y →SU(2) which restrict to S1 ⊂SU(2) along K.
Therefore, we will say that the lift ˜τ is constant if there exists u ∈S1 ⊂SU(2) such that
σ(y) = u for all y ∈ˇY . Notice for y ∈Fix(τ) we must have that
˜τ p(y, f) = (y, σp(y)f) = (y, ±f)
Since σ |K is circle valued, for ﬁxed y ∈K, σ(y) must be one of the p-th roots of ±1. Clearly this
is a discrete set, and given that we can assume that the gauge transformations are continuous, this
automatically says that σ |K is constant.


## Page 54


Mariano Echeverria
54
Let uj = ±

e−2πij/p
0
0
e2πij/p

and consider the constant lift
˜τu(y, f) = (τ(y), uf)
The orbifold bundles P ad/˜τ and P ad/˜τu have the same holonomy along K′, which is 2α′ + 2j
p
(modulo some twists to normalize it so that it belongs to the interval (0, 1/2) again), therefore they
are isomorphic. Take any isomorphism and pull it back to an (equivariant) gauge transformation
gad ∈GSO(3)(Y, K, α). Then as SO(3) orbifold bundles we have that
B˜τ
ad(Y, K, α) = Bu
ad(Y, K, α)
Since H1(Y ; Z/2) = 0 there is no obstruction to lifting gad to a gauge transformation g ∈G(Y, K, α),
in fact there are two choices for such a lift. Since G˜τ(Y, K, α) incorporates the ambiguity of the lift
already, we have as well that
B˜τ(Y, K, α) = Bu(Y, K, α)
We will start now discussing the relation between equivariant α- representations on (Y, K, α) and
the diﬀerent α′
j -representations on (Y ′, K′, α′).
Lemma 46. Assume the hypothesis of Theorem 44. Then there is a bijective correspondence between
Sp−1
j=0 R(Y ′, K′, α′
j) and Rτ(Y, K, α). Here
αj = α′ + j
p = α
p + j
p ∼
( α+j
p
if α+j
p
∈(0, 1/2)
α+j
p
−1
2
if α+j
p
∈(1/2.1)
Likewise, there is a two to one correspondence between R∗(Xτ, Tτ, α) and Rτ(Y, K, α).
Proof. From covering space theory, the covering
Y \K →Y ′\K′
induces a homotopy exact sequence
(60)
1 →π1(Y \K) →π1(Y ′\K′) →Zp →1
Recall that the orbifold fundamental group can be deﬁned in terms of the knot complement as
(61)
ˇπ1 (Y, K, q) = π1(Y \K)/ ⟨µq
K⟩
Moreover, τ induces an action τ∗on π1(Y \K) which we denote as τ · h for h ∈π1(Y \K). The
induced action on R(Y \K) is given by [7, Section 2]
τ ∗(ρ)(h) = ρ(τ · h)
This action descends to an action on the orbifold group and we denote the ﬁxed point as ˇπτ
1(Y, K, r/q).
From the exact sequence we obtain a split exact sequence
(62)
1 →ˇπ1(Y, K, q) →ˇπ1(Y ′, K′, pq) →Zp →1
Notice that every α′
j -representation of (Y ′, K′) (for any j = 0, · · · , p −1) can be regarded as an
element of ˇπ1(Y ′, K′, pq).
What we need to check is that the pull-back of any α′
l irreducible representation of (Y ′, K′)
continues to be an α- irreducible representation of (Y, K), and conversely, an τ-equivariant α-
irreducible representation of (Y, K) pushes down to an α′
l-irreducible representation of (Y ′, K′), for
some α′
l. The second statement will follow from the ﬁrst one, so let’s focus on the former. Since
the sequence 62 splits, we can write ˇπ1(Y ′, K′, pq) as a semi-direct product of ˇπ1(Y, K, q) and Zp.


## Page 55


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 55
As discussed in [4, Section 7.4], the representations of a semi-direct product, like ˇπ1(Y ′, K′, pq) ≃
ˇπ1(Y, K, q) ⋊Zp are determined in terms of the representations of ˇπ1(Y, K, q) and Zp.
Let ρ′ : ˇπ1(Y, K, q) →SU(2) be an α′
l representation and denote by ρ the induced α represen-
tation on ˇπ1(Y, K, q). If t is a generator of Zp (with unit 1) and e is the identity of π1(Y \K),
then ρ(h) = ρ′(h, 1) for h ∈π1(Y \K) and u = ρ′(t) = ρ′(e, t) ∈SU(2) determine the induced
representations from the semidirect product 62. Notice that
ρ′((h, tm))
=ρ′((e, tm) · (h, 1))
=ρ′((e, tm))ρ′(h, 1)
=umρ(h)
The fact that ρ must be τ equivariant implies that [28, Proposition 7.7]
τ ∗ρ = uρu−1
Now, if we assume that ρ is abelian, then τ ∗ρ is completely speciﬁed by how τ acts on H1(Y \K; Z).
Since τ is a diﬀeomorphism of odd order, it is not diﬃcult to check that τ∗= id on H1(Y \K; Z).
Hence u and ρ commute. Therefore we have
ρ′((h1, tm1) · (h2, tm2))
=um1ρ(h1)um2ρ(h2)
=um2ρ(h2)um1ρ(h1)
=ρ′((h2, tm2) · (h1, tm1))
This means that ρ′ vanishes on commutators hence it must be an abelian representation, giving
rise to a contradiction.
Therefore, irreducibility is preserved under pull back of connections and push-down of connec-
tions. Once we know this, that Sp−1
j=0 R∗(Y ′, K′, α′) and R∗,τ(Y, K, α) are in bijection is immediate.
The two to one correspondence between R∗(Xτ, Tτ, α) and R∗,τ(Y, K, α) is similar and follows
the proof of [51, Proposition 2.1]. First of all, we have a splitting exact sequence
1 →ˇπ1(Y, K, q) →ˇπ1(Xτ, Tτ, q) →Z →0
The same argument we just gave applies to show that the pullback of an irreducible α-representation
ρ ˇ
X of (Xτ, Tτ) gives rise to an irreducible ρ ˇY α-representation of (Y, K) (or one can also think about
this in terms of unique continuation coming from restricting the corresponding α -ﬂat connection
on (Xτ, Tτ) to a slice (Y, K)). Notice, that the pull back representation is equivariant, so we can
write as before
τ ∗ρ ˇY = uρ ˇY u−1
where u = ρ ˇ
X(e, t) and ρ ˇY = ρ ˇ
X(h, 1). The correspondence is two to one because replacing u by
−u gives rise to a new representation of (Xτ, Tτ) which induces the same representation ρ ˇY . This
is in fact coming from the action of H1(Xτ; Z/2), and the fact that the new representation is a
new one is granted by the freeness of this action, which is a true because of Lemma 36. That every
equivariant representation on (Y, K) induces one on (Xτ, Tτ) is also clear ([52, Theorem 6.1] and
[51, Proposition 3.1]).
□
Now we will discuss the non-degeneracy condition. First we will show that under the assumptions
of Theorem 44 that λF O(Xτ, Tτ, α) is well deﬁned. Likewise, we will show that the Zariski tangent


## Page 56


Mariano Echeverria
56
spaces of the α-representations on (Xτ, Tτ) can be identiﬁed with the equivariant Zariski tangent
spaces of the α-representations of (Y, K, α).
Lemma 47. Suppose that the conditions of Theorem 44 hold. Then λF O(Xτ, Tτ, α) is well deﬁned.
Moreover, the unperturbed moduli space M∗(X, T, 0, 0, α) use to compute λF O(Xτ, Tτ, α) is non-
degenerate if and only if R∗,τ(Y, K, α) is non-degenerate.
Proof. Our proof is essentially the same as the one in [51, Proposition 3.3]. Let ρ ˇ
X denote an α-
representation on (Xτ, Tτ). By restriction to a slice it induces an α representation ρ ˇY on (Y, K). To
study the non-degeneracy of the representation we use Lemma 29. Therefore, we want to compute
H1(X\T ; gρ ˇ
X).
From the ﬁbration X\T →S1 with ﬁber Y \K we have by Leray-Serre a spectral sequence whose
Epq
2
page is
Hp(S1, Hq(Y \K; gρ ˇ
Y ))
This spectral sequence collapses for all p ≥2 so
(63)
H1(X\T ; gρ ˇ
X) = H0(S1, H1(Y \K; gρ ˇ
Y )) ⊕H1(S1, H0(Y \K; gρ ˇ
Y ))
Now we analyze this decomposition in two cases:
• Case when ρ ˇ
X is a reducible α-ﬂat connection: in this situation gρ ˇ
X ≃R ⊕L⊗2
ρ ˇ
X and we just
need to analyze the L⊗2
ρ ˇ
X part of the decomposition 63. Since ρ ˇ
X induces the reducible connection
ρθα on Y \K 63 becomes
H1(X\T ; L⊗2
ρ ˇ
X) = H0(S1, H1(Y \K; L⊗2
θα )) ⊕H1(S1, H0(Y \K; L⊗2
θα ))
Observe that H0(Y \K; L⊗2
θα ) vanishes since dim H0(Y \K; R ⊕L⊗2
θα ) = dim stabθα = 1 and we
already know that dim H0(Y \K; R) = 1. Therefore H1(S1, H0(Y \K; L⊗2
θα )) vanishes.
To compute H0(S1, H1(Y \K; L⊗2
θα )) notice that the generator of π1(S1) acts on H1(Y \K; L⊗2
θα )
as τ ∗: H1(Y \K; L⊗2
θα ) →H1(Y \K; L⊗2
θα ), thus H0(S1, H1(Y \K; L⊗2
θα )) is the ﬁxed point set of τ∗,
which is the equivariant cohomology H1,τ(Y \K; L⊗2
θα ). This term must vanish by the assumption
on Theorem 44 that ˇH1,τ( ˇY ; gθα) = 0.
In conclusion, H1(X\T ; L⊗2
ρ ˇ
X) vanishes for all α-reducible representations ρ ˇ
X which is the condi-
tion needed for λF O(Xτ, Tτ, α) to be well deﬁned.
• Case when ρ ˇ
X is an irreducible α-ﬂat connection: since the restriction ρ ˇY is an irreducible α-
ﬂat connection then H0(Y \K; gρ ˇ
Y ) will vanish which means that the second term in 63 will vanish
as well.
As in the previous case, H0(S1, H1(Y \K; gρ ˇ
Y )) can be identiﬁed with H1,τ(Y \K; gρ ˇ
Y )). Also,
that the meridian µT restricts in a natural way to the meridian of µK, and any local system
restricted to either µT or µK always reduces (since the loops have abelian fundamental group so
any ﬂat connection becomes reducible). Because of the holonomy condition, it cannot be the trivial
local system ≃R3 in either case which means that
R ≃H1(µT ; gρ) ≃H1(µK; gˇρY ) ≃H1,τ(µK; gˇρY )
where the last isomorphism follows from the fact that τ restricts to the identity on the knot.
Therefore, ker : H1(X\T ; gρ) →H1(µT ; gρ) will vanish if and only if ker : H1,τ(Y \K; gρ ˇ
Y ) →
H1(µK; gˇρY ) vanishes, which means that M∗(X, T, 0, 0, α) is non-degenerate if and only if R∗,τ(Y, K, α)
is non-degenerate.
□


## Page 57


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 57
The case where perturbations are needed follow essentially the arguments in [51]. Namely, for
computing λF O(Xτ, Tτ, α) as well as the diﬀerent λCLH(Y ′, K′, α′) we can always use (ﬁnitely
many) holonomy perturbations whose stays away from the singularity (i.e, the torus or knot). This
was already discussed before the proof of Theorem 17, where we used this condition to identify the
Euler characteristic of our Floer groups with the Casson Lin Herald invariant. Since the support of
the holonomies do not meet the singularity, we can still ﬁnd equivariant perturbations pτ to achieve
transversality for R∗,τ(Y, K, α, pτ) as in [51, Section 5.1]. Since the action is free away from the
knot K, these equivariant holonomy perturbations can be pushed down to the quotient (Y ′, K′) in
such a way that they guarantee transversality for the diﬀerent moduli spaces Sl−1
j=0 R(Y ′, K′, α′, pτ),
as was done in [8, Section 3.8].
That the perturbations needed to achieve transversality for R∗,τ(Y, K, α) and R∗(Xτ, Tτ, α) can
be chosen in a consistent matter corresponds precisely to [51, Section 5.3]. Moreover, that the
correspondence between the perturbed versions of R∗,τ(Y, K, α) and R∗(Xτ, Tτ, α) continues to be
2 to 1 is proven in exactly the same way as [51, Proposition 5.3].
Finally, that the orientations of the moduli spaces for Sl−1
j=0 R(Y ′, K′, α′, pτ), R∗,τ(Y, K, α) and
R∗(Xτ, Tτ, α) can be chosen in a consistent way is a consequence of the analysis in [51, Section
3.5], where we just need to use the existence of a constant lift ˜τ , which we already know exist from
our previous discussion when we deﬁned the spaces B˜τ(Y, K, α).
Some tori inside circle bundles over homology S1 × S2.
Now we will work out an orbifold version of the examples discussed in [52, Section 8]. There
Ruberman and Saveliev analyzed a family of homologies S1×S3 for which λF O(X) can be computed,
and in fact vanishes identically.
The four manifolds X they considered arise as circle bundles
π : X →Y0 over a 3 manifold with the integral homology of S1 × S2 (i.e, a homology handle).
The manifolds Y0 can be obtained from doing 0 surgery on a knot K in an integral homology
sphere Y , and in order to guarantee that λF O(X) is well deﬁned, it is assumed that △K(t) ≡1 and
moreover that the Euler class e ∈H2(Y ; Z) = Z of the bundle satisﬁes e = 1. In order to be able to
compute λF O(X), they furthermore assume that π2(Y ) = 0 so that the homotopy exact sequence
of the S1 bundle π : X →Y0 allows them to consider π1X as a central extension of π1Y0 by the
integers
1 →Z →π1X →π∗π1Y0 →1
From here one can identify M∗(X, SO(3)) with R∗(Y, SO(3)) as well as the corresponding Zariski
tangent spaces.
The natural tori inside X that can be used for trying to compute λF O(X, T, α) are related to
the Longitudinal Floer Homology Kronheimer and Mrowka deﬁne in [36, Section 4.4]. First
of all, observe that Y0 contains a natural knot K0, which is the core of the solid torus used in the
surgery. Furthermore, K0 represents a primitive element in the ﬁrst homology of Y0, so in particular
H1(K0; Z) generates H1(Y0; Z).
Therefore, when we look at the inverse image of K0 under the map π : X →Y0 it is clear that
we obtain an embedded torus T satisfying the condition that H1(T ; Z) surjects onto H1(X; Z).
Example 48. Consider the unknot K = ◦⊂S3. After doing 0 -surgery on K we obtain Y0 =
S1 × S2. A natural S1 bundle over Y0 satisfying the our requirements is π : S1 × S3 →S1 × S2
where we are using the Hopf ﬁbration S3 →S2 on the second factor and the trivial projection
on the ﬁrst factor. Notice that in this case K0 can be identiﬁed with S1 × {pt} and therefore the
natural torus T is T = S1 × S1, where the second factor is the standard circle as well (an unknot).


## Page 58


Mariano Echeverria
58
It is clear in this case that for any α we have λF O(X, T, α) = 0, since the fundamental group of
X\T is abelian.
In fact, our expectation is that the previous example is the norm in the following sense:
Conjecture 49. Let π : X →Y0 as before and consider the torus T = π−1(K0). Then whenever
λF O(X, T, α) can be deﬁned it will vanish.
To give insight into why we are making this conjecture, we need to explain a bit more how
λF O(X) was shown to vanish by Ruberman and Saveliev and how this computation would be
modiﬁed in the case of λF O(X, T, α).
As we mentioned before, Ruberman and Saveliev identiﬁed M∗(X, SO(3)) with R∗(Y, SO(3))
in an orientation preserving way. The action of H1(X; Z2) continues to be free in this situation, so
in particular λF O(X) can be computed as one half the signed count of elements in R∗(Y, SO(3))
(after perturbations if needed). This count ends up being the same as △′′
K(1), which is zero in this
case.
The interesting feature of this calculation is that △′′
K(1) is the Euler characteristic of the Instan-
ton Floer homology Floer deﬁned for a homology S1 × S2. Therefore, we expect that λF O(X, T, α)
is related to the Euler characteristic of an orbifold version of Instanton Floer homology on ho-
mology handles. But this is precisely the Longitudinal Floer homology HIL(Y0, K0) Kronheimer
and Mrowka deﬁned in [36]!
Here the connections are allowed to have a singularity along the
knot K0, where they used holonomy α = 1/4 in order to avoid the compactness issues due to
non-monotonicity.
If one is willing to use local coeﬃcients, there is no diﬃculty in obtaining a version HIL(Y0, K0, α)
which is always well deﬁned, since there are no reducible α-ﬂat connections to worry about in
this situation (because we are now using the non-trivial SO(3) bundle over Y0).
They conjec-
tured that χ(HIL(Y0, K0)) should be 2△′′
K(1) in general, which in our situation would imply that
χ(HIL(Y0, K0)) vanishes.
For the other values of α there is a brief discussion in [6, Section 4.3], where it is promised that a
deﬁnition of what we are deﬁning as HIL(Y0, K0, α) would be constructed eventually. In any case,
based on the Property 3 Collin states in the survey we conjecture the following:
Conjecture 50. For α ∈Q ∩(0, 1/2) the Euler characteristic of HIL(Y0, K0, α) over the Novikov
ring Λ equals 2△′′
K(1). In particular, for the tori we are considering arising as π−1(K0) we would
have that λF O(X, T, α) vanishes in all of these cases.
Remark 51. Besides the fact that conjecture 50 might be used for computing λF O(X, T, α) for
this family of examples, it could be of independent interest to compute the Euler characteristic of
HIL(Y0, K0, α). In fact, we plan to verify this in the future, adapting the ideas of Floer as described
in [5].


## Page 59


A Generalization of the Tristram-Levine Knot Signatures as a Singular Furuta-Ohta Invariant for Tori 59
References
[1] Selman Akbulut and John D. McCarthy. Casson’s invariant for oriented homology 3-spheres, volume 36 of
Mathematical Notes. Princeton University Press, Princeton, NJ, 1990. An exposition.
[2] Nima Anvari. A splitting formula in instanton ﬂoer homology. arXiv:1901.02570v1, 2019.
[3] David M. Austin. SO(3)-instantons on L(p, q) × R. J. Diﬀerential Geom., 32(2):383–413, 1990.
[4] Rolf Berndt. Representations of linear groups. Vieweg, Wiesbaden, 2007. An introduction based on examples
from physics and number theory.
[5] P. J. Braam and S. K. Donaldson. Floer’s work on instanton homology, knots and surgery. In The Floer memorial
volume, volume 133 of Progr. Math., pages 195–256. Birkhäuser, Basel, 1995.
[6] Olivier Collin. Floer homology for knots and 3-manifolds and cyclic Dehn surgeries along knots. In Geometry
and topology of manifolds, volume 47 of Fields Inst. Commun., pages 39–50. Amer. Math. Soc., Providence, RI,
2005.
[7] Olivier Collin and Nikolai Saveliev. A geometric proof of the Fintushel-Stern formula. Adv. Math., 147(2):304–
314, 1999.
[8] Olivier Collin and Nikolai Saveliev. Equivariant Casson invariants via gauge theory. J. Reine Angew. Math.,
541:143–169, 2001.
[9] Olivier Collin and Brian Steer. Instanton Floer homology for knots via 3-orbifolds. J. Diﬀerential Geom.,
51(1):149–202, 1999.
[10] Aliakbar Daemi. Chern-simons functional and the homology cobordism group. arXiv:1810.08176v2, 2019.
[11] Aliakbar Daemi and Christopher Scaduto. Equivariant aspects of singular instanton ﬂoer homology. In prepa-
ration.
[12] James F. Davis and Paul Kirk. Lecture notes in algebraic topology, volume 35 of Graduate Studies in Mathe-
matics. American Mathematical Society, Providence, RI, 2001.
[13] S. K. Donaldson. The orientation of Yang-Mills moduli spaces and 4-manifold topology. J. Diﬀerential Geom.,
26(3):397–428, 1987.
[14] S. K. Donaldson. Floer homology groups in Yang-Mills theory, volume 147 of Cambridge Tracts in Mathematics.
Cambridge University Press, Cambridge, 2002. With the assistance of M. Furuta and D. Kotschick.
[15] Mariano
Echeverria.
A
generalization
of
the
tristram-levine
knot
signa-
tures
as
a
singular
furuta-ohta
invariant
for
tori
(annotated
version).
2019.
https://www.math.rutgers.edu/component/comproﬁler/userproﬁle/me498?Itemid=714.
[16] Ronald Fintushel and Ronald J. Stern. Knots, links, and 4-manifolds. Invent. Math., 134(2):363–400, 1998.
[17] Andreas Floer. An instanton-invariant for 3-manifolds. Comm. Math. Phys., 118(2):215–240, 1988.
[18] Kim A. Frø yshov. Equivariant aspects of Yang-Mills Floer theory. Topology, 41(3):525–552, 2002.
[19] Kim A. Frø yshov. An inequality for the h-invariant in instanton Floer theory. Topology, 43(2):407–432, 2004.
[20] Kim A. Frø yshov. Compactness and gluing theory for monopoles, volume 15 of Geometry & Topology Mono-
graphs. Geometry & Topology Publications, Coventry, 2008.
[21] Kim A. Frø yshov. Monopole Floer homology for rational homology 3-spheres. Duke Math. J., 155(3):519–576,
2010.
[22] Kenji Fukaya, Yong-Geun Oh, Hiroshi Ohta, and Kaoru Ono. Lagrangian intersection Floer theory: anomaly
and obstruction. Part I, volume 46 of AMS/IP Studies in Advanced Mathematics. American Mathematical
Society, Providence, RI; International Press, Somerville, MA, 2009.
[23] Kenji Fukaya, Yong-Geun Oh, Hiroshi Ohta, and Kaoru Ono. Lagrangian Floer theory on compact toric mani-
folds. I. Duke Math. J., 151(1):23–174, 2010.
[24] Mikio Furuta and Hiroshi Ohta. Diﬀerentiable structures on punctured 4-manifolds. Topology Appl., 51(3):291–
301, 1993.
[25] Benoit Gerard. Singular connections on three-manifolds and manifolds with cylindrical ends. ProQuest LLC,
Ann Arbor, MI, 1998. Thesis (Ph.D.)–Brandeis University.
[26] Christopher M. Herald. Flat connections, the Alexander invariant, and Casson’s invariant. Comm. Anal. Geom.,
5(1):93–120, 1997.
[27] H. Hofer and D. A. Salamon. Floer homology and Novikov rings. In The Floer memorial volume, volume 133 of
Progr. Math., pages 483–524. Birkhäuser, Basel, 1995.
[28] Daniel Ruberman Jianfeng Lin and Nikolai Saveliev. On the froyshov invariant and monopole lefschetz number.
arXiv:1802.07704v1, 2018.
[29] A. Juhász and I. Zemke. Concordance surgery and the ozsváth-szabó 4-manifold invariant. arXiv:1804.06221,
2018.


## Page 60


Mariano Echeverria
60
[30] P. B. Kronheimer. An obstruction to removing intersection points in immersed surfaces. Topology, 36(4):931–962,
1997.
[31] P. B. Kronheimer. Four-manifold invariants from higher-rank bundles. J. Diﬀerential Geom., 70(1):59–112, 2005.
[32] P. B. Kronheimer and T. S. Mrowka. Gauge theory for embedded surfaces. I. Topology, 32(4):773–826, 1993.
[33] P. B. Kronheimer and T. S. Mrowka. Embedded surfaces and the structure of Donaldson’s polynomial invariants.
J. Diﬀerential Geom., 41(3):573–734, 1995.
[34] P. B. Kronheimer and T. S. Mrowka. Gauge theory for embedded surfaces. II. Topology, 34(1):37–97, 1995.
[35] P. B. Kronheimer and T. S. Mrowka. Khovanov homology is an unknot-detector. Publ. Math. Inst. Hautes
Études Sci., (113):97–208, 2011.
[36] P. B. Kronheimer and T. S. Mrowka. Knot homology groups from instantons. J. Topol., 4(4):835–918, 2011.
[37] P. B. Kronheimer and T. S. Mrowka. Tait colorings, and an instanton homology for webs and foams. J. Eur.
Math. Soc. (JEMS), 21(1):55–119, 2019.
[38] Peter Kronheimer and Tomasz Mrowka. Monopoles and three-manifolds, volume 10 of New Mathematical Mono-
graphs. Cambridge University Press, Cambridge, 2007.
[39] Peter Kronheimer and Tomasz Mrowka. A deformation of instanton homology for webs. Geom. Topol.,
23(3):1491–1547, 2019.
[40] Claude Lebrun. Edges, orbifolds, and Seiberg-Witten theory. J. Math. Soc. Japan, 67(3):979–1021, 2015.
[41] Yi-Jen Lee. Reidemeister torsion in Floer-Novikov theory and counting pseudo-holomorphic tori. I. J. Symplectic
Geom., 3(2):221–311, 2005.
[42] J. Levine. Knot cobordism groups in codimension two. Comment. Math. Helv., 44:229–244, 1969.
[43] Jianfeng Lin, Daniel Ruberman, and Nikolai Saveliev. A splitting theorem for the Seiberg-Witten invariant of a
homology S1 × S3. Geom. Topol., 22(5):2865–2942, 2018.
[44] Xiao-Song Lin. A knot invariant via representation spaces. J. Diﬀerential Geom., 35(2):337–357, 1992.
[45] L. Ma. Equivariant torus signatures and periodic rho invariant, arxiv:2101.10243v1.
[46] S. Michael Miller. Equivariant instanton homology. arXiv:1907.01091, 2019.
[47] S. P. Novikov. Multivalued functions and functionals. An analogue of the Morse theory. Dokl. Akad. Nauk SSSR,
260(1):31–35, 1981.
[48] Johan Rå de. Singular Yang-Mills ﬁelds—global theory. Internat. J. Math., 5(4):491–521, 1994.
[49] D. Ruberman. A levine-tristram invariant for knotted tori, arxiv:2010.02355.
[50] Daniel Ruberman and Nikolai Saveliev. Rohlin’s invariant and gauge theory. I. Homology 3-tori. Comment.
Math. Helv., 79(3):618–646, 2004.
[51] Daniel Ruberman and Nikolai Saveliev. Rohlin’s invariant and gauge theory. II. Mapping tori. Geom. Topol.,
8:35–76, 2004.
[52] Daniel Ruberman and Nikolai Saveliev. Casson-type invariants in dimension four. In Geometry and topology of
manifolds, volume 47 of Fields Inst. Commun., pages 281–306. Amer. Math. Soc., Providence, RI, 2005.
[53] Daniel Ruberman and Nikolai Saveliev. Rohlin’s invariant and gauge theory. III. Homology 4-tori. Geom. Topol.,
9:2079–2127, 2005.
[54] Christopher Scaduto and Matthew Stoﬀregen. Klein-four connections and the Casson invariant for nontrivial
admissible U(2) bundles. Algebr. Geom. Topol., 17(5):2841–2861, 2017.
[55] Christopher W. Scaduto. Instantons and odd Khovanov homology. J. Topol., 8(3):744–810, 2015.
[56] L. M. Sibner and R. J. Sibner. Classiﬁcation of singular Sobolev connections by their holonomy. Comm. Math.
Phys., 144(2):337–350, 1992.
[57] Cliﬀord Henry Taubes. Casson’s invariant and gauge theory. J. Diﬀerential Geom., 31(2):547–599, 1990.
[58] A. G. Tristram. Some cobordism invariants for links. Proc. Cambridge Philos. Soc., 66:251–264, 1969.
[59] Michael Usher. Spectral numbers in Floer theories. Compos. Math., 144(6):1581–1592, 2008.
[60] Michael Usher and Jun Zhang. Persistent homology and Floer-Novikov theory. Geom. Topol., 20(6):3333–3430,
2016.
Department of Mathematics, Rutgers University.
E-mail address: mariano.echeverria@rutgers.edu

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]