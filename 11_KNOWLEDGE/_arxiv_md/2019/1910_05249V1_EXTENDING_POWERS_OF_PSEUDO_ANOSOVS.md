---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.05249v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1910.05249v1_Extending_powers_of_pseudo-Anosovs

> Source: 1910.05249v1_Extending_powers_of_pseudo-Anosovs.pdf

> Pages: 9

---


## Page 1


Extending powers of pseudo-Anosovs
Cristina Mullican
Abstract. Biringer, Johnson, and Minsky showed that a pseudo-Anosov map on a
boundary component of an irreducible 3-manifold has a power that partially extends
to the interior if and only if the (un)stable laminations of f is an R-projective limit
of meridians. We prove that the power required for a pseudo-Anosov map to partially
extend is not universally bounded. We construct a family of pseudo-Anosov maps fi
for all i = 1, 2... on a boundary component of a family of irreducible 3-manifolds Mi
such that f i
i partially extends to the interior of Mi but f j
i does not for j < i.
1
Introduction
Let M be a compact, orientable, and irreducible 3-manifold with some compressible bound-
ary component S. Then for a homeomorphism f : S →S, we say that f partially extends
to M if there is some nontrivial compression body C ⊂M with ∂+C = S and a homeo-
morphism φ : C →C such that φ|S = f.
Biringer, Johnson, and Minsky [1] prove the following:
Theorem (BJM, 2013). Let f : Σ →Σ be a pseudo-Anosov homeomorphism of some
compressible boundary component Σ of a compact, orientable and irreducible 3-manifold
M. Then the (un)-stable lamination of f is an R-projective limit of meridians if and only
if f has a power that partially extends to M.
Ackermann gives an alternate proof in [5] using earlier machinery of Casson and Long
(see [6] and [7]).
Maher and Schleimer give an alternate proof using train tracks and
subsurface projections (see [8]).
Partial extension comes up naturally when hyperbolizing 3-manifolds created as gluings.
For instance, in [2], Lackenby studied the hyperbolization of 3-manifolds obtained by ‘gen-
eralized Dehn surgery’, i.e. manifolds obtained by attaching a handlebody H to a compact
3-manifold M along some boundary component. He showed (modulo the Geometrization
Theorem) that if M is ‘simple’ and we choose any homeomorphism φ : ∂M →∂H and
a homeomorphism f : ∂H →∂H such that no power partially extends to H, then for
inﬁnitely many integers n, the manifold M ∪fn◦φ H is hyperbolic.
1
arXiv:1910.05249v1  [math.GT]  11 Oct 2019


## Page 2


Inspired by both of these theorems, it is natural to ask if there is some bound on the
power of f required to partially extend as this would imply there are only a ﬁnite number
of powers of f to check for partial extension and subsequent obstruction to hyperbolization.
We will show that there is no universal bound via construction in the proof of the following:
Theorem 1. For i = 1, 2, ... there is a compact, orientable and irreducible 3-manifold Mi
with compressible boundary component Σi and a pseudo-Anosov fi : Σi →Σi such that fi
i
partially extends to Mi and fj
i does not for j < i.
In section 2, we present background material and in section 3 we prove the main theo-
rem via a construction.
Acknowledgments: Many thanks to my advisor Ian Biringer for many helpful discussions
and thoughtful guidance.
2
Background
A compression body C is an orientable, compact, irreducible 3-manifold with a preferred
boundary component ∂+C that π1-surjects. We say ∂+C is the exterior boundary compo-
nent of C.
Deﬁnition 2. If we ﬁx a surface S to be the exterior boundary, an S-compression body is
a pair (C, m) where C is a compression body with a homeomorphism m : S →∂+C. Here,
m is the marking of C which is dropped when non-ambiguous.
Any S-compression body C can be constructed in the following way: Set {α1, ..., αn} to
be a maximal disjoint set of simple closed curves on S that bound disks in C. First consider
S × [0, 1] and attach 2-handles along annuli in S × {0} whose core curves are {αi} × {0}.
Then we attach 3-balls along any resulting boundary components that are homeomorphic
to S2. In this construction, ∂+C = S × {1}. For details see [3].
When an S-compression body can be constructed as above by attaching 2-handles along
simple closed curves {α1, ..., αn} and subsequent 3-balls, we denote it as S[α1, ..., αn]. The
trivial S-compression body is homeomorphic to S × I.
We call ∂C\∂+C the interior
boundary of C.
For S-compression bodies (C, m) and (D, n) we write (C, m) ⊂(D, n) if there exists an
embedding H : C →D such that n = H ◦m.
Two S-compression bodies (C, m) and (C′, m′) are equivalent if there exists a homeo-
morphism h : C →C′ such that the diagram below commutes.
∂+C′
S
∂+C
m′
m
h|∂+C
2


## Page 3


A homeomorphism f : S →S sends (C, m) to (C, mf−1). This action respects the
equivalence relation.
From here forward, we will drop all markings and will abusively
refer to compression bodies when we mean equivalence classes of compression bodies. In
particular, we denote this action as f(C).
Deﬁnition 3. Let C be an S-compression body and f : S →S a homeomorphism. We
say that f extends to C if there is a homeomorphism φ : C →C such that φ|∂+C = f.
Here we can write f(C) = C. Recall that we say f partially extends to C if there is an
S-compression body D ⊂C with a homeomorphism ψ : D →D such that ψ|∂+D = f.
Deﬁnition 4. Let α be a simple closed curve in ∂+C. If α bounds a disk in C then we
say α is a meridian of C and α compresses in C. Moreover, if there is some simple closed
curve α′ in the interior boundary of C such that α and α′ together bound an embedded
annulus in C we say α bounds an annulus.
Recall the following well known fact which is proved in detail in [10]:
Fact 5. Let C be an S-compression body. A Dehn twist Tα : S →S extends to C if α
compresses in C or bounds an annulus in C.
The idea of the proof is to deﬁne a Dehn twist of C by twisting in a neighborhood of
the disk or annulus bounded by α.
In the compression body S[α1, ..., αn] there are likely many curves besides the αi that
compress.
Fact 6. If two boundary components of an embedded pair of pants in ∂+C bound disks then
the third boundary component also bounds a disk.
Proof. Let P be a pair of pants embedded in ∂+C with boundary components c1, c2 and c3
such that c1, c2 bounding disks d1 and d2 respectively. Since P ∪d1 ∪d2 is homeomorphic
to a disk then c3 compresses.
Deﬁnition 7. An S-compression body C is small if it can be written as S[a] for some
simple closed curve a ∈S = ∂+C. A compression body is minimal if it does not contain
any (non-trivial) sub-compression bodies.
Minimality and smallness are related in the following work of Biringer and Vlamis.
Proposition 8 ([3], Cor. 2.7). An S-compression body is minimal if and only if it is a
solid torus or a small compression body obtained by compressing a separating curve.
A compression body can be built out of minimal compression bodies in the following
way:
3


## Page 4


Deﬁnition 9. A sequence of minimal compressions of an S-compression body C is a chain
S × [0, 1] = C0 ⊂C1 ⊂· · · ⊂Ck = C of S-compression bodies where Ci+1 is obtained from
Ci by gluing in a minimal Fi-compression body to Fi, an interior boundary component of
Ci. [3]
In this sequence, each compression body is obtained by gluing in either a solid torus or
obtained by compressing a single separating curve. Biringer and Vlamis give a formula for
the number of steps required to obtain a compression body from minimal compressions:
Proposition 10 ([3], Prop. 2.10). If C is any S-compression body with interior boundary
F1 ⊔· · · ⊔Fn, then the length k of any sequence of minimal compressions S × [0, 1] = C0 ⊂
C1 ⊂· · · ⊂Ck = C is h(C) := 2g(S) −1 −Pn
i=1(2g(Fi) −1), the height of C.
3
Main Theorem
We will prove Theorem 1 by constructing a family of manifolds and corresponding pseudo-
Anosovs. In fact, the manifolds we construct below are compression bodies. We restate
our Theorem 1 to reﬂect this:
Theorem 1. For g = 1, 2, ... there is an S2g-compression body Cg and a pseudo-Anosov
fg : S2g →S2g such that fg
g extends to Cg and fj
g does not partially extend to Cg for j < g.
Proof. Fix 2g, the genus of the exterior boundary component, and consider the compres-
sion body K1 := S2g[γ, α] as shown in Figure 1.
We will construct a pseudo-Anosov
homeomorphism fg : S2g →S2g such that fg
g extends to K1 but fj
g does not extend to any
sub-compression body of K1 for j ≤g.
γ
α
1
2
3
...g
r
Figure 1: Compression body K1 := S2g[γ, α]
4


## Page 5


Let r be the rotation of S2g by 2π
g . Deﬁne Kj := rj−1(K1) for 1 < j ≤g. Since rg is
the identity then rg extends to K1. Thus r(Ki) = K(i+1)mod(g).
Lemma 11. Each curve in the set K = {σ, ϕ, β, γ, α, b1, b2, b3} (see Figure 2) bounds a
disk or annulus in K1, ..., Kg.
γ
α
1
2
b1
b2
b3
σ
ϕ
Figure 2: Set K = {σ, ϕ, β, γ, α, b1, b2, b3}.
Proof. First, note that every curve in K bounds an annulus in Ki for i > 2 and every curve
in K\{σ} bounds an annulus in K2.
Clearly α and γ bound disks in K1. Also b2 and b3 bound annuli. Since α and b1
co-bound a pair of pants, by Fact 6, b1 also bounds a disk in K1. Also by Fact 6, curve ϕ′
bounds a disk in K1 as seen in Figure 3. Notice that ϕ is a band-sum of this disk. Thus
ϕ also bounds a disk in K1.
γ
1
2
ϕ
ϕ′
α
Figure 3: Curve ϕ, a bandsum of ϕ′
5


## Page 6


In Figure 4 in steps (a) through (d) we see that σ homotopes to ˜σ1 in K1 which bounds
an annulus.
Hence σ bounds an annulus in K1.
In Figure 5 we see that in K2, σ is
homotopic to ˜σ2 which co-bounds a pair of pants with r(γ) and r(α) which both compress
in K2. Thus σ bounds a disk in K2.
γ
α
1
2
σ
γ
α
1
2
γ
α
1
2
γ
α
1
2
˜σ1
(a)
(b)
(c)
(d)
Figure 4: Curve σ bounds an annulus in K1
r(γ)
1
2
σ
r(γ)
1
2
r(γ)
r(α)
1
2
˜σ2
r(α)
r(α)
Figure 5: Curve σ bounds a disk in K2
We will apply the following theorem of Fathi:
Theorem ([9], Theorem 0.2). Let h be a mapping class of surface a S and γ1, ..., γk be
simple closed curves on S. Suppose that the orbits under h of the γi are distinct and ﬁll
S. Then there exists an n ∈N such that for every (n1, ..., nk) ∈Zk with |ni| ≥n, the class
T nk
γk ...T n1
γ1 h is pseudo-Anosov.
The curves Sg
i=1 ri(K) ﬁll S2g as follows. Looking at Figure 2, we see that α, ϕ, σ, b1, b2,
and b3 ﬁll the genus 2 component of S2g\γ. Also, note that the genus 0 component of
S2g\ Sg−1
i=0 ri(γ) is ﬁlled by Sg−1
i=0 ri(σ). Hence the orbit of K under r ﬁlls S2g.
6


## Page 7


By Fathi’s theorem there exists ng1, · · · , ng7 ∈Z such that
T
ng1
γ
◦T
ng2
α
◦T
ng3
σ
◦T
ng4
ϕ
◦T
ng5
b1
◦T
ng6
b2
◦T
ng7
b3
◦r := fg
is pseudo-Anosov.
Lemma 12. The homeomorphism fg
g : S2g →S2g extends to K1 but fj
g does not extend to
K1 for j < g.
Proof. Recall that r(Ki) = K(i+1)mod(g). By Lemma 11, every curve in K bounds a disk or
annulus so applying Proposition 5 implies that Tc extends to Ki for all c ∈K and 1 ≤i ≤g.
Therefore, fg(Ki) = K(i+1)mod(g). Hence, fg
g (K1) = K1 and so fg
g extends to K1 but fj
g
does not for j < g.
We must now show that fj for j < g does not partially extend to K1. First, we prove
two lemmas.
Lemma 13. Every common meridian of Ki and Kj for i ̸= j is separating.
Proof. Let’s ﬁrst consider the homology of Ki. Set αi := ri−1(α) and γi := ri−1(γ). Hence
both αi and γi compress in Ki. Let Dαi and Dγi denote the disks in Ki bounded by αi
and γi respectively. Consider the following portion of the the Mayer-Vietoris long exact
sequence:
H1(S2g ∩(Dαi ⊔Dγi))
Φi
−→H1(S2g) ⊕H1(Dαi ⊔Dγi)
Ψi
−→H1(Ki).
Note that H1(Dαi ⊔Dγ) = 0 giving H1(S2g)
Ψi
−→H1(Ki). Also, S2g ∩(Dαi ⊔Dγi) =
{αi, γi}. By exactness of the Mayor-Vietoris sequence, Im(Φi) = Φi({αi, γi}) = ker(Ψi).
Moreover, γi is separating and hence Φi([γi]) = 0 in H1(S2g). Therefore, ker(Ψi) is gener-
ated by αi.
Note that the [αi] for i ∈{1, 2, ..., g} form a subset of a basis for H1(S2g). If ω is a
simple closed curve in S2g and a meridian of both Ki and Kj then [ω] ∈ker(Ψi)∩ker(Ψj) ⊂
H1(S2g). So [ω] ∈⟨[αi]⟩∩⟨[αj]⟩implying [ω] = 0 in H1(S2g). Therefore, ω is a separating
curve of S2g.
Lemma 14. Every S-compression body D ⊂Ki ∩Kj is small.
Proof. For all i, the interior boundary components of Ki are homeomorphic to S1 ⊔S2g−2.
Applying Proposition 10, for all i, the height of Ki is
h(Ki)
=
(2(2g) −1) −[2(1) −1] −[2(2g −2) −1]
=
4g −1 −1 −(4g −5)
=
3.
7


## Page 8


Let D be an S-compression body with D ⊂Ki ∩Kj. Then h(D) < 3.
If h(D) = 1 then S2g × [0, 1] = C0 ⊊C1 = D is a sequence of minimal compressions for
D. By Proposition 8, since D is not a solid torus, D is small.
If h(D) = 2 then S2g×[0, 1] = C0 ⊊C1 ⊊C2 = D is a sequence of minimal compressions
for D.
By Lemma 13, both compressions are along separating curves.
Therefore, the
interior boundary components of D are F1 ⊔F2 ⊔F3 where g(F1) + g(F2) + g(F3) = 2g
and g(Fℓ) > 0 for ℓ∈{1, 2, 3}. Recall that the interior boundary components of Ki are
S2g−2 ⊔S1. Then D ⊂Ki implies that g(Fℓ) ≥2g −2 for some ℓ∈{1, 2, 3}. Without loss
of generality, say g(F1) ≥2g −2. This forces g(F1) = 2g −2, g(F2) = 1 and g(F3) = 1.
There is some sequence of minimal compressions with S2g × [0, 1] = C0 ⊊C1 ⊊C2 =
D ⊊C3 = Ki. Thus we must compress a curve in F2 or F3 to obtain Ki (to preserve the
genus 2g −2 interior boundary component). Likewise, we must compress a curve in F2 or
F3 to obtain Kj. Therefore, Ki and Kj share F1, the same genus 2g −2 interior boundary
component. But this is false by construction of Ki and Kj. Therefore, h(D) ̸= 2.
Thus, D is a small compression body.
To prove Theorem 1 recall we must show that for all j < g, fj
g does not partially extend
to K1. Assume for sake of contradiction that there is some S2g-compression body K′ ⊊K1
with ℓ< g such that fℓ
g extends to K′. Then fℓ
g(K′) = K′. Since fℓ
g(K1) = Kℓ+1, this
implies that K′ ⊂Kℓ+1. Thus K′ ⊂K1 ∩Kℓ+1. By Lemma 14, K′ must be a small
S2g-compression body and by Lemma 13, K′ has exactly one meridian, a, a separating
curve. Then fℓ
g must map the disk bounded by a to itself. This implies that fℓ
g(a) = a
which contradicts the fact that fℓ
g is pseudo-Anosov.
Therefore, fg extends to K1 and no lesser power partially extends to K1. As the genus
to goes to inﬁnity, the power required for f to extend to the corresponding compression
body K1 also goes to inﬁnity.
References
[1] I. Biringer, J. Johnson, and Y. Minsky, Extending pseudo-Anosov maps into compres-
sion bodies, Journal of Topology 6 (2013), no. 4, 1019-1042.
[2] M. Lackenby, Attaching handlebodies to 3-manifolds. Geometry and Topology 6 (2002),
889-904.
[3] I. Biringer and N. Vlamis, Automorphisms of the compression body graph, Journal of
the London Mathematical Society 95 (2017) 94-114.
[4] W. Thurston, The geometry and topology of three-manifolds, Princeton (1980).
[5] R. Ackermann, An alternative approach to extending pseudo-Anosovs over compres-
sion bodies. Algebraic and Geometric Topology 15 (2015), no. 4, 2383-2391.
8


## Page 9


[6] A. J. Casson and D. D. Long, Algorithmic compression of surface automorphisms.
Inventiones mathematicae 81 (1985) 295-303.
[7] D. D. Long, Bounding laminations. Duke Mathematical Journal 56
(1988), no. 1,
1-16.
[8] J. Maher and S. Schleimer, The compression body graph has inﬁnite diameter.
arXiv:1803.06065v2 (2019).
[9] A. Fathi, Dehn twists and pseudo-Anosov diﬀeomorphisms. Inventiones Mathematicae
87 (1987), no. 1, 129-151.
[10] D. McCullough, Homeomorphisms which are Dehn twists on the boundary. Algebraic
and Geometric Topology 6 (2006), 1331-1340.
9

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1910_05249v1_extending_powers_of_pseudo_anosovs
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1910_05249V1_EXTENDING_POWERS_OF_PSEUDO_ANOSOVS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
