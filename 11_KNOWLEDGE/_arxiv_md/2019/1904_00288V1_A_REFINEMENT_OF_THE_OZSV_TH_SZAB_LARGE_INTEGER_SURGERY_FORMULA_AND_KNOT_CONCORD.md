---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1904.00288v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1904.00288v1_A_refinement_of_the_Ozsváth-Szabó_large_integer_surgery_formula_and_knot_concord

> Source: 1904.00288v1_A_refinement_of_the_Ozsváth-Szabó_large_integer_surgery_formula_and_knot_concord.pdf

> Pages: 14

---


## Page 1


A REFINEMENT OF THE OZSV´ATH-SZAB´O LARGE INTEGER
SURGERY FORMULA AND KNOT CONCORDANCE
LINH TRUONG
Abstract. We compute the knot Floer ﬁltration induced by the (n, 1)–cable of
the meridian of a knot in the manifold obtained by large integer surgery along
the knot. We give a formula in terms of the original knot Floer complex of the
knot in S3. As an application, we show that the concordance invariant a1(K) of
Hom can equivalently be deﬁned in terms of ﬁltered maps on the Heegaard Floer
homology groups induced by the two-handle attachment cobordism of surgery
along a knot in S3.
1. Introduction
Let S3
t (K) denote the manifold constructed as Dehn surgery along K ⊂S3 with
surgery coeﬃcient t.
In [OS04] Ozsv´ath and Szab´o construct a chain homotopy
equivalence between certain subquotient complexes of the full knot Floer chain com-
plex CFK∞(S3, K) and Heegaard Floer chain complexes c
CF(S3
t (K), sm) for suﬃ-
ciently large integers t for each spinc structure sm. This equivalence is known as the
large integer surgery formula.
The meridian µ of K naturally lies inside of the knot complement S3 \ K and the
surgered manifold S3
t (K). The meridian µ induces a ﬁltration on c
CF(S3
t (K), sm) for
each spinc structure sm. In [Hed07] Hedden gives a formula for the ﬁltered complex
[
CFK(S3
t (K), µ, sm) in terms of CFK∞(S3, K) for suﬃciently large t. As an appli-
cation of this formula, Hedden computes the knot Floer homology of Whitehead
doubles and the Ozsv´ath-Szab´o concordance invariant τ of Whitehead doubles. In
[HKL16] Hedden, Kim, and Livingston generalize Hedden’s formula by computing
the full knot Floer complex CFK∞(S3
t (K), µ, sm) in terms of CFK∞(S3, K) for suﬃ-
ciently large t. As an application to knot concordance, they show that the subgroup
of topologically slice knots of the concordance group contains a Z∞
2 subgroup.
K
µn
Figure 1. The two-component link µn and K for n = 5
The author was partially supported by NSF grant DMS-1606451.
1
arXiv:1904.00288v1  [math.GT]  30 Mar 2019


## Page 2


2
L. TRUONG
We reﬁne the theorems of Ozsv´ath-Szab´o, Hedden and Hedden-Kim-Livingston to
determine the ﬁltered chain homotopy type of CFK∞(S3
t (K), µn), where µn denotes
the (n, 1)–cable of the meridian of K, viewed as a knot in S3
t (K). See Figure 1.
For each spinc structure sm, we show that the complex CFK∞(S3
t (K), µn, sm) is
isomorphic to CFK∞(S3, K), but endowed with a diﬀerent Z ⊕Z ﬁltration and an
overall shift in the homological grading.
Theorem 1.1. Let K be a knot in S3 and ﬁx m, n ∈Z. Then there exists T =
T(m, n) > 0 such that for all t > T, the complex CFK∞(S3
t (K), µn, sm) is isomor-
phic to CFK∞(S3, K)[ϵ] as an unﬁltered complex, where [ϵ] denotes a grading shift
that depends only on m and t. Given a generator [x, i, j] for CFK∞(S3, K), the Z⊕Z
ﬁltration level of the same generator, viewed as a chain in CFK∞(S3
t (K), µn, sm),
is given by:
F([x, i, j]) =





[i, i]
if j ≤m + i
[j −m, j −m −k]
if j = m + i + k, where 1 ≤k < n
[j −m, j −m −n]
if j ≥m + i + n
As a corollary, the Z–ﬁltered complex [
CFK(S3
t (K), µn, sm) is isomorphic to a
subquotient complex of CFK∞(S3, K), endowed with an (n + 1) step ﬁltration F:
0 ⊆C{i<−n+1,j=m} ⊆· · · ⊆C{i<0,j=m} ⊆C{max(i,j−m)=0}
This ﬁltration is illustrated in Figure 2 in the case n = 3.
Corollary 1.2. Let K ⊂S3 be a knot, and ﬁx m, n ∈Z. Then there exists T =
T(m, n) > 0 such that for all t > T, the Z–ﬁltration on d
CF(S3
t (K), sm) induced by
µn ⊂S3
t (K) is isomorphic to the ﬁltered chain homotopy type of the (n + 1) step
ﬁltration on C{max(i, j −m) = 0} described above.
j
i
Figure 2. C{max(i, j −m) = 0} is the shaded region. The sub-
regions bounded by the colored dots represent subcomplexes of the
ﬁltration F in the case n = 3.
As an application, we show that the concordance invariant a1(K) of Hom [Hom14b]
can equivalently be deﬁned in terms of ﬁltered maps on the Heegaard Floer homol-
ogy groups induced by the two-handle attachment cobordism of surgery along a knot
K in S3. The rationally null-homologous knot µn ⊂S3
t (K) induces a Z-ﬁltration of
c
CF(S3
t (K), sτ) and c
CF(S3
−t(K), sτ), that is, a sequence of subcomplexes:
0 ⊂Fbottom ⊂Fbottom+1 ⊂· · · ⊂Ftop−1 ⊂Ftop = c
CF(S3
t (K), sτ).


## Page 3


A REFINEMENT OF THE SURGERY FORMULA AND CONCORDANCE
3
0 ⊂F′
bottom ⊂F′
bottom+1 ⊂· · · ⊂F′
top−1 ⊂F′
top = c
CF(S3
−t(K), sτ).
Using the knot ﬁltrations, an equivalent deﬁnition of a1(K) can be formulated in
terms of the ﬁltration F and F′ induced by µn as a knot inside S3
t (K) and S3
−t(K).
Theorem 1.3. Let n > 2g(K).
For suﬃciently large surgery coeﬃcient t, the
concordance invariant a1(K) is equal to:
a1(K) =

























max
(
m |
c
CF(S3
t K, sτ)/Ftop−1−m →c
CF(S3)
induces a trivial map on homology
)
if ε(K) = −1,
0
if ε(K) = 0,
min
(
m |
c
CF(S3) →F′
bottom+m ⊂c
CF(S3
−tK, sτ)
induces a trivial map on homology
)
if ε(K) = 1.
This interpretation of the invariant a1(K) oﬀers a topological perspective that
complements the original algebraic deﬁnition of a1(K). We will also include proper-
ties of the invariant a1(K) as well as computations of a1(K) for homologically thin
knots and L–space knots.
Acknowledgements. The author thanks her advisors, Peter Ozsv´ath and Zolt´an
Szab´o, for their guidance. Adam Levine for reading the version of this work which
appeared in the author’s PhD thesis and for helpful comments. The author would
also like to thank Matt Hedden, Jen Hom and Olga Plamenevskaya for helpful
conversations.
2. The knot Floer filtration of cables of the meridian in Dehn
surgery along a knot
In this section we will reﬁne the theorem of Ozsv´ath-Szab´o to determine the
ﬁltered chain homotopy type of the knot Floer complex of (S3
t (K), µn).
We begin by recalling the large integer surgery formula from Ozsv´ath and Szab´o
[OS04]. Let (Σg, α1, . . . , αg, γ1, . . . , γg, w, z) be a doubly-pointed Heegaard diagram
for CFK∞(S3, K), where
• the curve γg = µ is a meridian of the knot K
• the curve αg is a longitude for K
• there is a single intersection point in αg ∩γg = x0
• the basepoints w and z lie on either side of γg
Let β = {γ1, . . . , γg−1, λt} be the set of curves in γ, with γg replaced by a longitude
βg = λt winding t times around µ. Label the unique intersection point γg ∩βg = θ.
The Heegaard triple diagram (Σ, α, β, γ, w, z) represents a cobordism between S3
and S3
t (K). See Figure 3.
Let C{max(i, j −m)} = 0 denote the subquotient complex of CFK∞(S3, K)
generated by triples [x, i, j] with the i and j ﬁltration levels satisfying the speciﬁed
constraints.


## Page 4


4
L. TRUONG
x−1
x−2
x−3
x−4
x1
x2
x3
x0
θ
αg
βg
γg
w
z
Figure 3. Local picture of the winding region of the Heegaard triple
diagram (Σ, α, β, γ, w, z) for the cobordism between S3
t K and S3
Theorem 2.1 ([OS04]). Let K ⊂S3 be a knot, and ﬁx m ∈Z. Then there exists
T = T(m) > 0 such that for all t > T, the chain map
Φm : c
CF(S3
t (K), sm) →C{max(i, j −m) = 0}
deﬁned by
Φm([x]) =
X
y∈Tα∩Tγ
X
{ψ∈π2(x,θ,y) | nz(ψ)−nw(ψ)=m−F(y), µ(ψ)=0}
[y, −nw(ψ), m −nz(ψ)]
induces an isomorphism of chain complexes.
Remark 2.2. Here, as usual, the labeling of the spinc structures is determined by
the condition that sm can be extended over the cobordism −Wt from −S3
t (K) to
−S3 associated to the two-handle addition along K with framing t, yielding a spinc
structure rm satisfying
⟨c1(rm, [S])⟩+ t = 2m.
Above, S denotes a surface in Wt obtained from closing oﬀa Seifert surface for K
in S3 to produce a surface S of square t.
We reﬁne the theorem of Ozsv´ath-Szab´o to determine the ﬁltered chain homotopy
type of the knot Floer complex of (S3
t (K), µn). Consider the meridian µ = µK of a
knot K. The meridian µ naturally lies inside of the knot complement S3 \ K and
the surgered manifold S3
t (K). For n ∈N, µn denotes the (n, 1)–cable of µK, and
also lies inside S3 \K and the surgered manifold S3
t K. The knot µn is homologically
equivalent to n · [µ] in H1(S3
t (K)). When n = 1, µ1 = µ. See Figure 1 for a picture
of the two-component link K ∪µn.
For all n ≥1 there is a natural (n + 1)-step algebraic ﬁltration F on the subquo-
tient complex C{max(i,j−m)=0} of CFK∞(S3, K):
0 ⊆C{i<−n+1,j=m} ⊆· · · ⊆C{i<0,j=m} ⊆C{max(i,j−m)=0}.
This ﬁltration is illustrated in the case n = 3 in Figure 2.
Theorem 2.3 says that this algebraic ﬁltration F corresponds to a relative Z-
ﬁltration on c
CF(S3
t (K), sm) induced by µn ∈S3
t (K). This generalizes work of Hed-
den [Hed07] who studied the n = 1 case of the ﬁltered complex [
CFK(S3
t (K), µ, sm).
Theorem 2.3. Let K ⊂S3 be a knot, and ﬁx m, n ∈Z. Then there exists T =
T(m, n) > 0 such that for all t > T, the following holds: The ﬁltered chain homotopy
type of the (n+1) step ﬁltration F on C{max(i, j−m) = 0} described above is ﬁltered
chain homotopy equivalent to that of the ﬁltration on d
CF(S3
t (K), sm) induced by
µn ⊂S3
t (K).


## Page 5


A REFINEMENT OF THE SURGERY FORMULA AND CONCORDANCE
5
Proof. The key observation will be that the triple diagram (Σ, α, β, γ, w, z) used
to deﬁne Φm not only speciﬁes a Heegaard diagram for the knot (S3, K), but also
a Heegaard diagram for the knot (S3
t (K), µn) with the addition of a basepoint z′.
Place an extra basepoint z′ = zn so that it is n regions away from the basepoint w
in the Heegaard triple diagram representing the cobordism between S3 and S3
t (K)
as in Figure 4. (This can be accomplished if t is suﬃciently large, e.g. if t > 2n).
The knot represented by the doubly-pointed Heegaard diagram (Σ, α, β, w, zn) is µn
in S3
t (K).
An intersection point x′ ∈Tα ∩Tβ is said to be supported in the winding region if
the component of x′ in αg lies in the local picture of Figure 4. Intersection points in
the winding region are in t to 1 correspondence with intersection points x in Tα∩Tγ.
Fix a Spinc structure sm where m ∈Z. For t (the surgery coeﬃcient) suﬃciently
large, any generator x′ ∈Tα ∩Tβ representing Spinc structure sm is supported in
the winding region. In this case, there is a uniquely determined x ∈Tα ∩Tγ and a
canonical small triangle ψ ∈π2(x, θ, x′).
Suppose ψ ∈π2(x, θ, x′) is the canonical small triangle and x′ ∈Tα ∩Tβ is a
generator representing Spinc structure sm. If k = nz(ψ) ≥0 (so nw(ψ) = 0), then
the αg component of x′ is xk (and lies k units to the left of x0) in Figure 4. In
this case, Φm maps x′ to C{i = 0, j ≤m}. On the other hand, if x′ is a generator
with nz(ψ) = 0 and l = nw(ψ) > 0, then the αg component of x′ is x−l (and lies l
steps to the right of x0) in Figure 4. In this case, Φm maps x′ to the subcomplex
C{i ≤−l, j = m} ⊂C{i < 0, j = m}.
x1
x2
x3
x4
x−1
x−2
x−3
x−4
x0
θ
αg
βg
γg
w
z
z3
Figure 4. Local picture of the winding region of the Heegaard triple
diagram (Σ, α, β, γ, w, zn) for the cobordism between S3
t K and S3.
The basepoint zn is located n regions away from the basepoint w in
the Heegaard diagram (Σ, α, β, w, zn). Here we depict the basepoint
zn for n = 3.
The following lemma (which generalizes Lemma 4.2 of [Hed07]) will be used to
ﬁnish the proof.
Lemma 2.4. Let p ∈[
CFK(S3
t (K), µn, sm) be a generator supported in the winding
region, and let xi denote the αg component of the corresponding intersection point
in Tα ∩Tβ, where the xi are labeled as in Figure 4. Then
F(p) =





Ftop
i > 0;
Ftop+i
−n < i < 0;
Fbottom
i ≤−n.
Here, Ftop (respectively, Fbottom) denotes the top (respectively, bottom) ﬁltration
level of [
CFK(S3
t (K), µn, sm). Ftop−i denotes the ﬁltration level that is i lower than
Ftop. In addition Fbottom = Ftop−n, so this is an (n + 1)-step ﬁltration.


## Page 6


6
L. TRUONG
Proof. The Z-ﬁltration F is deﬁned by the relative Alexander grading A′
n induced
by µn on CF∞(S3
t K, sm). That is,
F(p) −F(q) = nzn(φ) −nw(φ)
where φ ∈π2(p, q) is a Whitney disk connecting p, q ∈Tα ∩Tβ.
Let p, q ∈[
CFK(S3
t K, µn, sm) be generators supported in the winding region, and
let xi, xj denote the αg components of the corresponding intersection points Tα∩Tβ.
Assume without loss of generality that i < j (so that xi lies to the right of xj).
We will deﬁne a set of n arcs δ1, . . . , δn on β as follows. Let δ1 denote the arc on
β connecting x1 to x−1. Let δk denote on the arc on β connecting x−(k−1) to x−k,
for k ∈{2, . . . , n}.
We will construct a Whitney disk φp,q ∈π2(p, q) with the following properties:
• If i > 0 and j > 0, (that is, xi, xj both lie on the left of x0), then ∂φp,q
doesn’t contain any arc δk. Therefore,
F(p) −F(q) = 0.
• If i ≤−n and j ≤−n, (that is, xi, xj both lie ≥n steps to the right of x0),
then ∂φp,q doesn’t contain any arc δk. Therefore,
F(p) −F(q) = 0.
• If i < −n and j > 0, (that is, xj lies to the left of x0 and xi lies i steps to the
right of x0), then ∂φp,q contains the n arcs δ1, . . . , δn, each with multiplicity
one. Therefore,
F(p) −F(q) = −n.
• If −n ≤i < 0 and j > 0, (that is, xj lies to the left of x0 and xi lies i
steps to the right of x0), then ∂φp,q contains the i arcs δ1, . . . , δi, each with
multiplicity one.
Moreover, ∂φp,q doesn’t contain the arcs δk for k > i.
Therefore,
F(p) −F(q) = −i.
• If −n < j < 0 and i ≤−n, (that is, xi lies ≥n steps to the right of x0
and xj lies j steps to the right of x0), then ∂φp,q contains the n + j arcs
δ|j|+1, . . . , δn, each with multiplicity one. Moreover, ∂φp,q doesn’t contain
the arcs δk for k ≤|j|. Therefore,
F(p) −F(q) = −n −j.
• If −n < i < 0 and −n < j < 0, (that is, xj lies j steps to the right of
x0 and xi lies i steps to the right of x0), then ∂φp,q contains the j −i arcs
δ|j|+1, . . . , δ|i|, each with multiplicity one. Therefore,
F(p) −F(q) = i −j.
Assuming the existence of such φp,q, the lemma follows immediately.
In [Hed07, Lemma 4.2] Hedden constructs a Whitney disk φp,q ∈π2(p, q). The
above enumerated properties of ∂φp,q will be immediate from the construction. We
restate his construction here. Note ﬁrst since p, q lie in the winding region, they
correspond uniquely to intersection points ˜p, ˜q ∈Tα ∩Tγ. These intersection points
˜p, ˜q can be connected by a Whitney disk φ ∈π2(˜p, ˜q) with nw(φ) = 0 and nz(φ) = k
for some k ∈Z≥0. This means that ∂φ contains γg with multiplicity k, which further
implies that the distance between xi and xj is k, that is, i −j = k. The domain


## Page 7


A REFINEMENT OF THE SURGERY FORMULA AND CONCORDANCE
7
of φp,q can then be obtained from the domain of φ by a simple modiﬁcation in the
winding region as described in [Hed07]. This modiﬁcation is shown in Figure 5.
It replaces the boundary component k · γg by a simple closed curve from an arc
connecting xi and xj along αg followed by an arc connecting xj to xi along βg, and
which wraps k times around the neck of the winding region.
□
This completes the description of the knot Floer complex [
CFK(S3
t (K), µn) in
terms of the complex CFK∞(S3, K).
□
(a) The domain of a disk φ ∈π2(˜p, ˜q).
x1
x2
x3
x4
x−1
x−2
x−3
x−4
x0
θ
αg
βg
γg
w
z
z3
(b) φp,q ∈π2(p, q) where p, q have αg components x−3, x−1. ∂φp,q contains arcs δ2 and δ3
on β drawn in violet.
x1
x2
x3
x4
x−1
x−2
x−3
x−4
x0
θ
αg
βg
γg
w
z
z3
(c) φp,q ∈π2(p, q) where p, q have αg components x−2, x−1.
x1
x2
x3
x4
x−1
x−2
x−3
x−4
x0
θ
αg
βg
γg
w
z
z3
(d) φp,q ∈π2(p, q) where p, q have αg components x1, x2.
x1
x2
x3
x4
x−1
x−2
x−3
x−4
x0
θ
αg
βg
γg
w
z
z3
(e) φp,q ∈π2(p, q) where p, q have αg components x−2, x1.
x1
x2
x3
x4
x−1
x−2
x−3
x−4
x0
θ
αg
βg
γg
w
z
z3
Figure 5. The domain of a disk φp,q ∈π2(p, q), for p, q ∈Tα ∩Tβ
in the winding region can be identiﬁed with the domain of a disk
φ ∈π2(˜p, ˜q).
Theorem 2.3 described the Z-ﬁltered chain homotopy type of knot Floer chain
complex [
CFK(S3
t (K), µn, sm) for t large with respect to m and n. In Theorem 1.1,
we describe the Z ⊕Z-ﬁltered chain homotopy type of CFK∞(S3
t K, µn, sm). This
generalizes Theorem 4.2 of Hedden-Kim-Livingston [HKL16] which studies the n = 1
case.


## Page 8


8
L. TRUONG
thick diagonal
C{max(i, j −4) = 0} →
i
j
A = 0
A = -1
A = -2
A = -3
A = -4
A = -5
A = -6
A = -7
Figure 6. CFK∞(S3, K) is supported along a thick diagonal of
width 2g(K) + 1.
The regions labeled A = 0, . . . , A = −7 have
constant Alexander grading A′
n induced by µn on CF∞(S3
t (K), sm).
For spinc structures sm where |m| ≤g(K), suﬃciently large surgery
coeﬃcient t, the algebraic ﬁltration i on C{max(i, j −m) = 0} corre-
sponds to the Z-ﬁltration induced by µn on CF∞(S3
t (K), sm) where
n > 2g(K).
Proof of Theorem 1.1. The isomorphism of chain complexes induced by the map
(deﬁned in [OS04])
Φm : CF∞(S3
t (K), sm) →CFK∞(S3, K)
respects the F[U, U−1]-module structure of both complexes, and hence determines
one of the Z-ﬁltrations (called the U-ﬁltration) of CFK∞(S3
t (K), µn, sm).
The knot µn ⊂S3
t (K) induces an additional Z-ﬁltration (the Alexander ﬁltra-
tion) on c
CF(S3
t (K), sm) and on CFK∞(Yt(K), sm). The additional Z-ﬁltration on
CFK∞(Yt(K), µn, sm) can be determined in exactly the same way as it was deter-
mined for the case of c
CF(S3
t (K), sm). Lemma 2.4 identiﬁes the Z-ﬁltration induced
on any given i = constant slice in CF∞(S3
t , sm) with a (n + 1)-step ﬁltration as
above. This yields the statement of the theorem.
Alternatively, the additional (Alexander) Z-ﬁltration on CFK∞(Yt(K), µn, sm)
can be obtained from the Alexander ﬁltration on [
CFK(Yt(K), µn, sm) by the fact
that the U variable decreases Alexander grading by one, i.e. we have the relation
A(U · x) = A(x) −1.
□
Corollary 2.5. Let K be a knot in S3 and ﬁx m, n ∈Z. Then there exists T =
T(m, n) > 0 such that for all t > T the following holds: Up to a grading shift,


## Page 9


A REFINEMENT OF THE SURGERY FORMULA AND CONCORDANCE
9
the pth ﬁltration level of CFK∞(S3
t (K), µn, sm) is described in terms of the original
Z ⊕Z−ﬁltered knot Floer homology CFK∞(S3, K) as
max(i, j −m −n) = p.
That is, each Alexander ﬁltration level p of CFK∞(S3
t (K), µn, sm) is a “hook”
shaped region in CFK∞(S3, K).
Proof. This follows from Theorem 1.1.
□
Proposition 2.6. Let m ∈Z with |m| ≤g(K) and let n > 2g(K). For suﬃciently
large surgery coeﬃcient t, the Alexander ﬁltration induced by µn on CF∞(S3
t (K), sm)
coincides with the algebraic i-ﬁltration on CFK∞(S3, K) under the correspondence
given by Φm.
Proof. Since [
CFK(Y, K) has degree equal to the Seifert genus of the knot, CFK∞(Y, K)
is supported along a thick diagonal of width 2g(K) + 1. By the hypothesis, we have
m + n > g(K).
Therefore the corner (p, m + n + p) of the hook region C{max(i, j −m −n) = p} of
each constant Alexander ﬁltration level p of CFK∞(S3
t K, µn, sm) lies above the thick
diagonal along which CFK∞(Y, K) is supported. See Figure 6. For spinc structures
sm where |m| ≤g(K), this means that the Alexander ﬁltration induced by µn
on CFK∞(S3
t (K), µn, sm) coincides with the algebraic i-ﬁltration on CFK∞(S3, K)
under the correspondence given by Φm.
□
Because the algebraic i-ﬁltration is used to deﬁne concordance invariants (such as
a1(K), which can be interpreted as an integer lift of the Hom ε invariant [Hom14a]),
the ﬁltration induced by µn on CF∞(S3
t (K), sm) can be used to study the concor-
dance class of a knot K. We will see that we can extract concordance invariants of
K from CFK∞(S3
t (K), µn, sm).
3. A knot concordance invariant
As an application for the results in the previous section on the Z–ﬁltration in-
duced on c
CF(S3
N(K), sm) by the (n, 1)–cable of the meridian µn, our main result
in this section (Theorem 3.5) shows that the concordance invariant a1(K) of Hom
[Hom14b], which has an algebraic deﬁnition in terms of maps on subquotient com-
plexes of CFK∞(K), can be equivalently deﬁned by studying ﬁltered maps on the
(hat version of the) Heegaard Floer homology groups induced by the two-handle at-
tachment cobordism of large integer surgery along a knot K in S3 and the ﬁltration
induced by the knot µn inside of the surgered manifold.
Our result is analogous to the statement that the concordance invariants ν(K) of
Ozsv´ath-Szab´o [OS11] and ε(K) of Hom [Hom14a] can be deﬁned algebraically or in
terms of maps on the (hat version of the) Heegaard Floer homology groups induced
by the two-handle attachment cobordism of large integer surgery along a knot K in
S3. Deﬁnition 3.1 gives an algebraic deﬁnition of ε(K) in terms of certain chain maps
on the subquotient complexes of the knot Floer chain complex CFK∞(K). Due to
the Ozsv´ath-Szab´o large integer surgery formula [OS04], ε(K) can equivalently be
deﬁned in terms of maps on the Heegaard Floer chain complexes induced by the
two-handle attachment cobordism of (large integer) surgery.


## Page 10


10
L. TRUONG
We begin by recalling the deﬁnition of the concordance invariants ε(K). Let N
be a suﬃciently large integer relative to the genus of a knot K. Consider the map
Fs : c
HF(S3) →c
HF(S3
−N(K), [s]),
induced by the two-handle cobordism W 4
−N. Here, [s] denotes the restriction to
S3
−N(K) of the Spinc structure ss over W 4
−N with the property that
⟨c1(ss), [ bF]⟩−N = 2s,
where |s| ≤N
2 and bF denotes the capped oﬀSeifert surface in the four-manifold.
We also consider the map
Gs : c
HF(S3
N(K), [s]) →c
HF(S3),
induced by the two-handle cobordism −W 4
N.
The maps Fs and Gs can be deﬁned algebraically by studying certain natural
maps on subquotient complexes of CFK∞(K), as in [OS04]. The map Fs is induced
by the chain map
C{i = 0} →C{min(i, j −s) = 0}
consisting of quotienting by C{i = 0, j < s} followed by the inclusion. Similarly,
the map Gs is induced by the chain map
C{max(i, j −s) = 0} →C{i = 0}
consisting of quotienting by C{i < 0, j = s} followed by the inclusion.
Deﬁnition 3.1 ([Hom14a], [Hom14b]). Let τ = τ(K) be the Ozsv´ath-Szab´o con-
cordance invariant. The invariant ε(K) is deﬁned as follows:
• ε(K) = 1 if Fτ is trivial (in which case Gτ is necessarily non-trivial).
• ε(K) = −1 if Gτ is trivial (in which case Fτ is necessarily non-trivial).
• ε(K) = 0 if Fτ and Gτ are both non-trivial.
In [Hom14b], Hom deﬁnes a concordance invariant a1(K) for knots with ε(K) = 1
that is a reﬁnement of ε(K).
Deﬁnition 3.2 ([Hom14b]). If ε(K) = 1 (Fτ is trivial), deﬁne
a1(K) = min{s | Hs : H∗(C{i = 0}) →H∗(C{min(i, j −τ) = 0, i ≤s}) is trivial}
We extend this deﬁnition of a1(K) to all knots (to include knots with ε(K) ̸= 1).
Consider the maps
G−s,τ : C{max(i, j −τ) = 0, i ≥−s} →C{i = 0}
Fs,τ : C{i = 0} →C{min(i, j −τ) = 0, i ≤s}
Deﬁnition 3.3. Given a knot K inside S3, deﬁne:
a1(K) =





max{−s | G−s,τ is trivial on homology} ,
if ε(K) = −1;
0,
if ε(K) = 0;
min{s | Fs,τ is trivial on homology} ,
if ε(K) = 1.
Note that a1(K) only depends on the doubly-ﬁltered chain homotopy type of the
knot Floer chain complex CFK∞(K), so it is a knot invariant.


## Page 11


A REFINEMENT OF THE SURGERY FORMULA AND CONCORDANCE
11
Remark 3.4. When ε(K) = 1, the deﬁnition of a1(K) agrees with the invariant a1(K)
deﬁned in Lemma 6.1 in [Hom14b]. As remarked in [Hom14b], a1(K) measures the
“length” of the horizontal diﬀerential hitting the special class generating the vertical
homology of c
CF(S3). Similarly, when ε(K) = −1, a1(K) measures the “length” of
the horizontal diﬀerential coming out of the special class generating the vertical
homology of c
CF(S3).
Recall that the rationally null-homologous knot µn ⊂S3
t (K) induces a Z-ﬁltration
of c
CF(S3
t (K), sτ) and c
CF(S3
−t(K), sτ), that is, a sequence of subcomplexes:
0 ⊂Fbottom ⊂Fbottom+1 ⊂· · · ⊂Ftop−1 ⊂Ftop = c
CF(S3
t (K), sτ).
0 ⊂F′
bottom ⊂F′
bottom+1 ⊂· · · ⊂F′
top−1 ⊂F′
top = c
CF(S3
−t(K), sτ).
Using Theorem 2.3 and Proposition 2.6, an equivalent deﬁnition of a1(K) can be
formulated in terms of the ﬁltration F and F′ induced by µn as a knot inside
S3
t (K) and S3
−t(K). This interpretation of the invariant a1(K) oﬀers a topological
perspective that complements the original algebraic deﬁnition of a1(K).
Theorem 3.5. Let n > 2g(K).
For suﬃciently large surgery coeﬃcient t, the
concordance invariant a1(K) is equal to
a1(K) =

























max
(
m |
c
CF(S3
t K, sτ)/Ftop−1−m →c
CF(S3)
induces a trivial map on homology
)
if ε(K) = −1,
0
if ε(K) = 0,
min
(
m |
c
CF(S3) →F′
bottom+m ⊂c
CF(S3
−tK, sτ)
induces a trivial map on homology
)
if ε(K) = 1.
Proof. Since |τ| ≤g4(K) ≤g(K), we can apply Proposition 2.6 which states that
in the spinc structure sτ, the algebraic i-ﬁltration on CFK∞(S3, K) coincides with
the ﬁltration induced by µn on c
CF(S3
N(K), sτ) under the identiﬁcation of the two
ﬁltered chain complexes in Theorem 2.3.
□
Remark 3.6. Recall that a1(K) is a concordance invariant (see Proposition 3.7) that
ﬁts into a family of concordance invariants studied by Dai, Hom, Stoﬀregen and the
author in [DHST19]. It would be interesting to see if an analogue of Theorem 3.5
exists for this entire family of algebraically deﬁned invariants corresponding to the
standard local representative (over F[U, V ]/(UV )) of the knot.
Proposition 3.7 ([Hom14b]). The invariant a1(K) is a concordance invariant.
Proof. Suppose K1 and K2 are concordant knots, i.e.
K1#K2 is slice.
Then
ε(K1#K2) = 0. By Proposition 3.11 in [Hom15], we may ﬁnd a basis for CFK∞(K1#K2)
with a distinguished element x that generates the homology HFK∞(K1#K2) and
splits oﬀas a direct summand of CFK∞(K1#K2). Similarly, we can ﬁnd a basis for
CFK∞(K2#K2) with a distinguished element y with the same properties. Then to
compute a1(K2#K1#K2), by the Kunneth principle [OS04] we can consider either
chain complex:
CFK∞(K1#K2) ⊗Z[U,U−1] CFK∞(K2)
or
CFK∞(K1) ⊗Z[U,U−1] CFK∞(K2#K2).


## Page 12


12
L. TRUONG
Using the special bases from above, the relevant summands to a1 are
{x} ⊗CFK∞(K2)
or
CFK∞(K1) ⊗{y}.
Thus, a1(K2) = a1(K2#K1#K2) = a1(K1).
□
Example 3.8 (Homologically thin knots). Model complexes for CFK∞of homologi-
cally thin knots are studied in [Pet13]. Petkova shows that if τ(K) = n, the model
complex contains a direct summand isomorphic to
CFK∞(T2,2n+1) if n > 0
and
CFK∞(T2,2n−1) if n < 0.
This summand supports H∗(CFK∞(K)) and thus determines the value of a1(K). It
is easy to see from the complex that a1(K) = sgn(τ(K)).
Proposition 3.9. The following are properties of a1(K):
(1) If K is smoothly slice, then a1(K) = 0.
(2) sgn(a1(K)) = ε(K).
(3) a1(K) = −a1(K).
(4) If a1(K) = 0, then a1(K#K′) = a1(K′).
Proof of (1). If K is smoothly slice, then ε(K) = 0; therefore, a1(K) = 0.
□
Proof of (2). By construction, if a1(K) > 0, then ε(K) = 1; if a1(K) < 0, then
ε(K) = −1.
If a1(K) = 0, we show that ε(K) = 0. Suppose ε(K) = −1. Then the vanishing
of
a1(K) = max{n | Gn,τ is trivial on homology}
implies that the map G0,τ : C{i = 0, j ≤τ} →C{i = 0} is trivial on homology,
which contradicts the deﬁnition of τ. Similarly, ε(K) ̸= 1 if a1(K) = 0.
Finally, according to [Hom14a], ε(K) = 0 implies that τ(K) = 0.
□
Proof of (3). The symmetry properties of CFK∞of Section 3.5 in [OS04] imply that
a1(K) = −a1(K).
□
Proof of (4). If a1(K) = 0, ε(K) = 0.
By Lemma 3.3 from [Hom14a], we may
ﬁnd a basis for CFK∞(K) with a distinguished element x which is the generator
of both vertical and horizontal homology. Then a1(K#K′) can be computed from
{x} ⊗CFK∞(K′).
□
In fact, we can extend Proposition 3.9(4) to describe the behavior of a1 under
connect sum in many (but not all) cases.
Proposition 3.10.
(1) If a1(K1) > 0 and a1(K2) < 0 and a1(K1) + a1(K2) < 0, then
a1(K1#K2) = a1(K1).
(2) If a1(K1) > 0 and a1(K2) < 0 and a1(K1) + a1(K2) > 0, then
a1(K1#K2) = a1(K2).
(3) If a1(K1) > 0 and a1(K2) > 0, then a1(K1#K2) = min(a1(K1), a1(K2)).
(4) If a1(K1) < 0 and a1(K2) < 0, then a1(K1#K2) = max(a1(K1), a1(K2)).
Proof. Note that we use −K to denote the mirror of a knot K.
(1) See the proof of Lemma 6.3 of [Hom14b].


## Page 13


A REFINEMENT OF THE SURGERY FORMULA AND CONCORDANCE
13
(2) The mirrors −K1 and −K2 satisfy the hypothesis of (1), so
a1(−K1# −K2) = a1(−K2).
Apply the symmetry property of a1 under mirroring (3.9):
−a1(K1#K2) = −a1(K2)
as desired.
(3) By Lemma 6.2 of [Hom14b], there exists a basis {xi} over F[U, U−1] for CFK∞(K1)
with basis elements x0 and x1 with the property that
(1) There is a horizontal arrow of length a1 from x1 to x0.
(2) There are no other horizontal arrows or vertical arrows to or from x0.
(3) There are no other horizontal arrows to or from x1.
Similarly, we may ﬁnd a basis {yi} over F[U, U−1] for CFK∞(K2) with basis ele-
ments y0 and y1 with the above properties. Without loss of generality, assume that
a1(K1) ≤a1(K2).
Notice x0y0 generates the vertical homology H∗(C({i = 0})) of CFK∞(K1#K2).
Let τ = τ(K1#K2). Consider the subquotient complex
A = C{min(i, j −τ) = 0}.
There is a direct summand of A consisting of the generators x0y0, x0y1, x1y0, and
x1y1, and four horizontal arrows as shown in Figure 7. The arrow x1y0 to x0y0 has
length a1(K1). Clearly, ε(K1#K2) = 1 and a1(K1#K2) = a1(K1).
x0y0
x1y0
x0y1
x1y1
Figure 7. A direct summand of A = C{min(i, j−τ) = 0} in Propo-
sition 3.10(3)
This is the summand that is relevant for computing a1, as it contains the generator
x0y0 of vertical homology H∗(C{i = 0}).
(4) The mirrors −K1 and −K2 satisfy the hypothesis of (3). So
−a1(K1#K2) = a1(−K1# −K2) = min(a1(−K1), a1(−K2)) = min(−a1(K1), −a1(K2))
= −max(a1(K1), a1(K2)).
□
Proposition 3.10 can be rewritten as the following.
Proposition 3.11. If a1(K1) ̸= 0 and a1(K2) ̸= 0:
(1) If a1(K1) + a1(K2) < 0, then a1(K1#K2) = max(a1(K1), a1(K2)).
(2) If a1(K1) + a1(K2) > 0, then a1(K1#K2) = min(a1(K1), a1(K2)).
Remark 3.12. If a1(K) ̸= 0 and a1(K′) ̸= 0, and a1(K)+a1(K′) = 0, then a1(K#K′)
is indeterminate. The next two examples illustrate this case.
Example 3.13. The connect sum of any knot K with the reverse of its mirror −K,
i.e. the inverse of K in the concordance group C, has vanishing a1(K# −K) = 0.


## Page 14


14
L. TRUONG
Example 3.14. The full knot Floer chain complexes CFK∞of the mirror −T2,3;2,5
of the (2, 5)-cable of the torus knot T2,3, the torus knot T2,9, and the connect sum
−T2,3;2,5#T2,9 are described in [HW14]. It is easy to see that a1(−T2,3;2,5) = −1,
a1(T2,9) = 1, and a1(−T2,3;2,5#T2,9) = −1.
We conclude with some computations of the a1–invariant.
Example 3.15. In [Hom16] Hom produces the relevant summand of CFK∞for
computing ε and hence a1 for the knot T4,5# −T2,3;2,5.
It is easy to see that
a1(T4,5# −T2,3;2,5) = 2.
Example 3.16. The Conway knot C2,1 has a1(C2,1) = 0. According to [Pet10], the
knot Floer chain complex CFK∞(C2,1) is generated as a F[U, U−1]−module by a
single isolated F at the origin plus a collection of null-homologous “boxes”.
Example 3.17. The knot Floer chain complex of an L-space knot is a given by
Theorem 2.1 in [OSS14]. If K is an L-space knot, with Alexander polynomial
∆K(t) =
k
X
i=0
(−1)itni,
where n0 > n1 > · · · > nk, then a1(K) = n0 −n1 by Lemma 6.5 [Hom14b].
References
[DHST19] Irving Dai, Jennifer Hom, Matthew Stoﬀregen, and Linh Truong, More concordance
homomorphisms from knot Floer homology, 2019, preprint, arXiv:1902.03333.
[Hed07]
Matthew Hedden, Knot Floer homology of Whitehead doubles, Geom. Topol. 11 (2007),
2277–2338. MR 2372849 (2008m:57030)
[HKL16]
Matthew Hedden, Se-Goo Kim, and Charles Livingston, Topologically slice knots of
smooth concordance order two, J. Diﬀerential Geom. 102 (2016), no. 3, 353–393.
MR 3466802
[Hom14a] Jennifer Hom, Bordered Heegaard Floer homology and the tau-invariant of cable knots,
J. Topol. 7 (2014), no. 2, 287–326. MR 3217622
[Hom14b]
, The knot Floer complex and the smooth concordance group, Comment. Math.
Helv. 89 (2014), no. 3, 537–570. MR 3260841
[Hom15]
, A survey on Heegaard Floer homology and concordance, arXiv:1512.00383
(2015).
[Hom16]
, A note on the concordance invariants epsilon and upsilon, Proc. Amer. Math.
Soc. 144 (2016), no. 2, 897–902. MR 3430863
[HW14]
Jennifer Hom and Zhongtao Wu, Four-ball genus bounds and a reﬁnement of the Ozsvath-
Szabo tau-invariant, arXiv:1401.1565 (2014).
[OS04]
Peter Ozsv´ath and Zolt´an Szab´o, Holomorphic disks and knot invariants, Adv. Math.
186 (2004), no. 1, 58–116. MR 2065507 (2005e:57044)
[OS11]
, Knot Floer homology and rational surgeries, Algebr. Geom. Topol. 11 (2011),
no. 1, 1–68. MR 2764036
[OSS14]
Peter Ozsv´ath, Andr´as Stipsicz, and Zolt´an Szab´o, Concordance homomorphisms from
knot Floer homology, arXiv:1407.1795 (2014).
[Pet10]
Thomas D. Peters, A concordance invariant from the Floer homology of +/- 1 surgeries,
arXiv:1003.3038 (2010).
[Pet13]
Ina Petkova, Cables of thin knots and bordered Heegaard Floer homology, Quantum
Topol. 4 (2013), no. 4, 377–409. MR 3134023
Department of Mathematics, Columbia University, New York, NY 10027
E-mail address: ltruong@math.columbia.edu

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]