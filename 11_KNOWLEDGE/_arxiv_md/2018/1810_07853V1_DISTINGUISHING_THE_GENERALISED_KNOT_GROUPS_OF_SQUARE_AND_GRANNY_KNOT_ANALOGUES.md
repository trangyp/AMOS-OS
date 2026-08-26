---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1810.07853v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1810.07853v1_Distinguishing_the_generalised_knot_groups_of_square_and_granny_knot_analogues

> Source: 1810.07853v1_Distinguishing_the_generalised_knot_groups_of_square_and_granny_knot_analogues.pdf

> Pages: 18

---


## Page 1


arXiv:1810.07853v1  [math.GT]  18 Oct 2018
DISTINGUISHING THE GENERALISED KNOT GROUPS OF SQUARE
AND GRANNY KNOT ANALOGUES
HOWIDA AL FRAN AND CHRISTOPHER TUFFLEY
Abstract. Given a knot K we may construct a group Gn(K) from the fundamental group of
K by adjoining an nth root of the meridian that commutes with the corresponding longitude.
For n ≥2 these “generalised knot groups” determine K up to reﬂection (Nelson and Neumann,
2008).
The second author has shown that for n ≥2, the generalised knot groups of the square knot
SK and the granny knot GK can be distinguished by counting homomorphisms into a suitably
chosen ﬁnite group. We extend this result to certain generalised knot groups of square and
granny knot analogues SKa,b = Ta,b#T−a,b, GKa,b = Ta,b#Ta,b, constructed as connect sums
of (a, b)-torus knots of opposite or identical chiralities. More precisely, for coprime a, b ≥2 and
n satisfying a certain coprimality condition with a and b, we construct an explicit ﬁnite group
G (depending on a, b and n) such that Gn(SKa,b) and Gn(GKa,b) can be distinguished by
counting homomorphisms into G. The coprimality condition includes all n ≥2 coprime to ab.
The result shows that the diﬀerence between these two groups can be detected using a ﬁnite
group.
1. Introduction
Given a knot K we may construct a group Gn(K) from the fundamental group of K by
adjoining an nth root of the meridian that commutes with the corresponding longitude. Topo-
logically, this corresponds to taking the fundamental group of the space Mn(K) obtained by
gluing a torus to the boundary of the exterior of K by a suitably chosen map: expressing the
boundary of the exterior as µ × λ, where µ and λ are curves representing the meridian and
longitude respectively, we use the map φ : µ × λ →S1 × S1 given by φ(z1, z2) = (zn
1 , z2). These
“generalised knot groups” are invariants of K, and were introduced independently by Wada [8]
and Kelly [3] in the early 1990s. In addition to the topological deﬁnition above, due to Wada,
they admit several other deﬁnitions, including one via a Wirtinger-type presentation. In this
presentation there is a generator xi for each arc, as usual, but the usual crossing relations
xk = x±1
j xix∓1
j
are replaced by relations of the form xk = x±n
j xix∓n
j . In particular, the group
G1(K) is simply the fundamental group of K.
In 2008 Nelson and Neumann [6] showed that for n ≥2 the generalised knot group Gn(K)
determines the knot K up to reﬂection. For n = 2 the space M2(K) is a closed nonorientable
manifold, and in this case they use the geometric version of the JSJ decomposition applied to
this manifold to show that one can recover the knot complement. By Gordon and Luecke [2]
this determines the knot up to reﬂection. For n ≥3 the space Mn(K) is not a manifold, and
in this case Nelson and Neumann establish the result using the Scott-Swarup version of JSJ
decomposition for groups.
The generalised knot groups were ﬁrst shown to carry more information about the knot than
the fundamental group does by the second author [7]. This was done by conﬁrming a conjecture
due to Lin and Nelson [5] that the generalised knot groups of the square knot SK and granny
2010 Mathematics Subject Classiﬁcation. Primary 57M27; Secondary 20F34.
Key words and phrases. Knot invariants, generalised knot groups, square and granny knot analogues, wreath
product.
1


## Page 2


2
HOWIDA AL FRAN AND CHRISTOPHER TUFFLEY
knot GK are nonisomorphic for all n ≥2, by showing that Gn(SK) and Gn(GK) can be
distinguished by counting homomorphisms into a suitably chosen ﬁnite group. In view of the
Nelson-Neumann result that Gn is a complete knot invariant up to reﬂection, this result shows
that the diﬀerence between Gn(SK) and Gn(GK) can be detected using a ﬁnite group (albeit
a large ﬁnite group: for example, for n coprime to 30 the group used has order 2 · 3 · 53 · q12,
where q is the least prime dividing n). The diﬀerence between these two groups can therefore
be detected using a ﬁnite group, and so can be detected algorithmically.
In this paper we extend Tuﬄey’s construction to detect the diﬀerence between generalised
knot groups of square and granny knot analogues built from (a, b)-torus knots instead of (2, 3)-
torus knots. For coprime integers a and b let Ta,b be the (a, b)-torus knot, and when a and b
are both positive let
SKa,b = Ta,b#T−a,b,
GKa,b = Ta,b#Ta,b.
Then the usual square and granny knots are SK2,3 and GK2,3 respectively.
We prove the
following theorem, which shows that (at least for certain n) the diﬀerence between Gn(SKa,b)
and Gn(GKa,b) can be detected by counting homomorphisms into a suitably chosen ﬁnite group:
Theorem 1.1. Let a, b, n ≥2 be positive integers such that gcd(a, b) = 1. Suppose that there are
prime numbers s|a and t|b such that gcd(st, n) = 1 (in particular, this holds if gcd(ab, n) = 1).
Then there is a ﬁnite group H such that
|Hom(Gn(GKa,b), H)| < |Hom(Gn(SKa,b), H)|.
The restriction on n is there to simplify the arguments and make the underlying ideas more
transparent. We expect that the result holds for all n, and that the techniques of Tuﬄey [7]
can be adapted to handle the remaining cases where gcd(ab, n) > 1.
The building blocks for our target groups will be groups of the form
Dq,r = (Zq)ordr(q) ⋊Zr,
where q and r are distinct primes and ordr(q) is the multiplicative order of q modulo r; that
is, the least positive integer d such that qd ≡1 mod r. Using these we will construct our target
groups as wreath products of two such groups, giving groups of the form
Wq,r
s,t = Dq,r ≀Ds,t = (Dq,r)sordt(s) ⋊Ds,t.
Here q, r, s and t are distinct primes, with s and t the primes dividing a and b, respectively,
given in the statement of the theorem. We construct these groups in Section 3.
1.1. Organisation. Section 2 is devoted to deﬁnitions. We deﬁne the generalised knot groups
in Section 2.1, and ﬁnd presentations for the generalised knot groups of the square and granny
knot analogues in Section 2.2. We then construct our target groups Wq,r
s,t and prove some needed
results about them in Section 3. We study homomorphic images of the meridian and longitude
of the (a, b)-torus knot group in Wq,r
s,t in Section 4, in preparation for ﬁnally proving our main
result in Section 5.
2. Definitions
2.1. Generalised knot groups. The generalised knot groups were deﬁned independently by
Kelly [3] and Wada [8], using diﬀerent approaches.
Kelly reportedly [5] reached them via
the knot quandle and Wirtinger presentations, while Wada’s approach was to look for group-
valued link invariants by studying representations ρ : Bn →Aut(Fn). His goal was to ﬁnd
what he called shift representations of the braid groups that are compatible with the Markov
moves, and so could be used to deﬁne a group-valued invariant of closed braids and hence of


## Page 3


GENERALISED KNOT GROUPS OF SQUARE AND GRANNY KNOT ANALOGUES
3
xk
xi
xj
xk
xi
xj
xk = xn
j xix−n
j
xk = x−n
j xixn
j
Figure 1. Crossing relations for Gn(K) at left- and right-handed crossings.
links. A computer search found seven diﬀerent types of shift representations, of which ﬁve were
compatible with the Markov moves. The “generalised knot groups” are his “group invariants
of type 4”.
The generalised knot group Gn(K) admits a Wirtinger-like presentation, in which the usual
crossing relations xk = x±1
j xix∓1
j
are replaced by relations of the form xk = x±n
j xix∓n
j
(see
Figure 1). However, the topological description of Gn(K) as the fundamental group of the space
Mn(K) constructed above typically leads to a simpler presentation. Suppose that π1(S3 −K)
has presentation
π1(S3 −K) = ⟨g1, . . . , gk|r1, . . . , rℓ⟩,
and let µ, λ be words in the generators representing the meridian and longitude respectively.
Then applying the Seifert-van Kampen Theorem to Mn(K) we obtain the presentation
Gn(K) = ⟨g1, . . . , gk, ν|r1, . . . , rℓ, νn = µ, νλ = λν⟩.
Note further that, since µ and ν commute, we are not required to use zero-framed longitudes,
and may freely replace λ with λ′ = µmλ for any m. We use this freedom in choosing the
longitude below, in ﬁnding presentations for the generalised knot groups of the square and
granny knot analogues.
2.2. The square and granny knot analogues. The square knot SK is the connect sum of
two trefoil knots with opposite chiralities, and the granny knot GK is the connect sum of two
trefoil knots with identical chiralities. Since the trefoil knot is the (2, 3)-torus knot T2,3, we
may construct analogues of the square and granny knots by taking connect sums of (a, b)-torus
knots instead. Accordingly, for coprime positive integers a and b we deﬁne the (a, b)-square
and -granny knot analogues SKa,b and GKa,b to be the knots
SKa,b = Ta,b#T−a,b,
GKa,b = Ta,b#Ta,b.
Thus, the (a, b)-square knot analogue is the connect sum of two (a, b)-torus knots with opposite
chiralities, and the (a, b)-granny knot analogue is the connect sum of two (a, b)-torus knots with
identical chiralities.
To obtain presentations for the generalised knot groups of the square and granny knot ana-
logues we make use of the following theorem describing the group Ga,b of the (a, b)-torus knot.
Of particular importance to us is part 2, which describes the meridian and longitude.
Theorem 2.1 (See Burde, Zieschang and Heusener [1, Prop 3.38 (p. 49)1]). Let (W, W ′) be a
standard Heegaard splitting of genus 1 of the oriented 3-sphere S3, and suppose that the torus
knot Ta,b lies on the torus W ∩W ′.
1Prop 3.28 (p. 45) in the original 1985 edition by Burde and Zieschang. The statement of the result diﬀers
slightly between the two editions; in particular, in the original edition the meridian is given as ucvd, where
ad + bc = 1. We have followed the newer edition.


## Page 4


4
HOWIDA AL FRAN AND CHRISTOPHER TUFFLEY
(1) The group Ga,b of the torus knot Ta,b can be presented as follows:
Ga,b = ⟨u, v|uav−b⟩= ⟨u|−⟩∗⟨ua=vb⟩⟨v|−⟩,
where u is the generator of π1(W ′), and v is the generator of π1(W). The amalgamating
subgroup ⟨ua⟩is an inﬁnite cyclic group; it represents the centre Z(Ga,b) ∼= Z, and
Ga,b/Z(Ga,b) ∼= Z|a| ∗Z|b|.
(2) The elements µ = vdu−c, λ = uaµ−ab, where ad−bc = 1, describe meridian and longitude
of Ta,b for a suitably chosen basepoint.
(3) Ta,b and Ta′,b′ have isomorphic groups if and only if |a| = |a′| and |b| = |b′|, or |a| = |b′|
and |b| = |a′|.
By the above theorem, the peripheral system of the (−a, b)-torus knot is described by
(G−a,b, µ, λ) = (⟨u, v|u−av−b⟩, vd′u−c′, u−aµab), where (−a)d′ −bc′ = 1. In what follows it will be
convenient to have a description that diﬀers from that of the (a, b)-torus knot only in the ex-
pression for the longitude. To achieve this, let t = v−1. Then G−a,b has presentation ⟨u, t|u−atb⟩,
and since the relation u−atb = 1 is equivalent to uat−b = 1 we may write G−a,b = ⟨u, v|uat−b⟩.
The meridian is then given by µ = t−d′u−c′, where (−a)d′ −bc′ = a(−d′) −bc′ = 1, and setting
d = −d′, c = c′ we obtain µ = tdu−c with ad −bc = 1. Thus, replacing t by v, the peripheral
systems of Ta,b and T−a,b are given by
(π1(K), µ, λ) =
(
(⟨u, v|uav−b⟩, vdu−c, uaµ−ab)
for K = Ta,b,
(⟨u, v|uav−b⟩, vdu−c, u−aµab)
for K = T−a,b,
diﬀering only in the expressions for the longitudes. Since we don’t require zero-framed longi-
tudes, in what follows we will use ua as the longitude for Ta,b, and u−a as the longitude for
T−a,b.
To ﬁnd presentations for the generalised knot groups of the square and granny knot analogues
we use the fact that if K1, K2 have peripheral systems (G1, µ1, λ1), (G2, µ2, λ2), then K1#K2
has peripheral system (G1 ∗⟨µ⟩G2, µ, λ1λ2), where µ = µ1 = µ2. Let
Ha,b = ⟨x, y, w, z|xa = yb, wa = zb, ydx−c = zdw−c⟩.
Then π1(GKa,b) ∼= π1(SKa,b) ∼= Ha,b, and the two knot groups have common meridian µ =
ydx−c = zdw−c, but diﬀerent (non-zero framed) longitudes λGKa,b = xawa and λSKa,b = xaw−a.
Then presentations for Gn(GKa,b) and Gn(SKab) are given by
Gn(GKa,b) ∼= ⟨x, y, w, z, ν|xa = yb, wa = zb, νn = ydx−c = zdw−c, xawaν = νxawa⟩,
Gn(SKa,b) ∼= ⟨x, y, w, z, ν|xa = yb, wa = zb, νn = ydx−c = zdw−c, xaw−aν = νxaw−a⟩.
Observe that the two presentations diﬀer only in the ﬁnal relation, expressing the fact that the
generator ν commutes with the longitude.
3. The target groups
3.1. Introduction. To detect the diﬀerence between the generalised knot groups of SK =
SK2,3 and GK = GK2,3 Tuﬄey [7] used as target groups wreath products of the form
Hq,r
p
= Dq,r ≀PSL(2, p),
where p, q, r are distinct primes and Dp,q is a semidirect product
Dq,r = (Z/qZ)r−1 ⋊(Z/rZ).
The key property of PSL(2, p) used was that it contains nontrivial solutions to the (2, 3)-torus
knot relation x3 = y2; and moreover, any solution to this equation satisﬁes either x3 = y2 = 1,


## Page 5


GENERALISED KNOT GROUPS OF SQUARE AND GRANNY KNOT ANALOGUES
5
or x = z2, y = z3 for some z (Theorem A.1 of [7], proved by David Savitt). By choosing p
coprime to n we can further ensure that there are homomorphisms G2,3 →PSL(2, p) such that
the image of the meridian has an nth root.
To detect the diﬀerence between the generalised knot groups of SKa,b and GKa,b we will
replace PSL(2, p) with a group where a similar characterisation holds for solutions to the
(a, b)-torus knot relation xa = yb. We will also replace Dq,r with a subgroup of itself of the form
Dq,r = (Z/qZ)d ⋊(Z/rZ),
where d is the smallest positive integer satisfying qd ≡1 mod r. This will ensure that Dq,r is
generated by any element of order q, together with any element of order r.
For distinct primes s and t such that s|a and t|b the group Ds,t will serve as a suitable
replacement for PSL(2, p). Thus, our target groups will be wreath products of the form
Wq,r
s,t = Dq,r ≀Ds,t.
We describe these groups in detail below.
3.2. The construction of the generalised dihedral groups Dq,r. Before constructing Dq,r
we ﬁrst review the construction of Dq,r [7]. We introduce the following notation:
Notation 3.1. Given a prime power α, we write Fα for the ﬁnite ﬁeld of order α.
For q and r distinct primes the group Dq,r is a semidirect product
Dq,r = (Zq)r−1 ⋊Zr.
To deﬁne multiplication in Dq,r we regard (Zq)r−1 as the additive group of the ﬁnite ﬁeld Fqr−1.
The multiplicative group F×
qr−1 is cyclic of order qr−1 −1 ≡0 mod r, and so contains an element
ζ of order r. Then for i ∈Zr and v ∈(Zq)r−1 the equation i · v = ζiv deﬁnes an action of Zr
on (Zq)r−1 by automorphisms, and we use this action to form the semidirect product. Thus,
multiplication in Dq,r is deﬁned by
(v, i) · (u, j) = (v + ζiu, i + j).
It is shown in [7, Lemma 3.2] that every element of Dq,r has order 1, q or r. To construct
Dq,r we will pass to a subgroup of Dq,r that has the property that it is generated by any
element of order q, together with any element of order r. We describe the construction of Dq,r
independently of the construction of Dq,r, so that it is clear that the isomorphism type depends
only on q and r.
Deﬁnition 3.2. Given distinct primes q and r, let (Fq)(r) be the rth cyclotomic ﬁeld over Fq
(the splitting ﬁeld of xr −1 over Fq), and let E(r)
q
⊆(Fq)(r) be the rth roots of unity in (Fq)(r).
Then with respect to multiplication E(r)
q
is a cyclic group of order r. Let V(r)
q
be the additive
group of (Fq)(r). We deﬁne the generalised dihedral group Dq,r to be the semidirect product
Dq,r = V(r)
q
⋊E(r)
q ,
where E(r)
q
acts on V(r)
q
by multiplication. That is, for v1, v2 ∈V(r)
q
and ζ1, ζ2 ∈E(r)
q , multipli-
cation in V(r)
q
⋊E(r)
q
is deﬁned by
(v1, ζ1) · (v2, ζ2) = (v1 + ζ1v2, ζ1ζ2).
By [4, Thm 2.47] we have [(Fq)(r) : Fq] = ordr(q), where ordr(q) is the multiplicative order of
q modulo r; that is, the least positive integer d such that qd ≡1 mod r. Thus we may identify
V(r)
q
with (Zq)ordr(q). Moreover, given a nontrivial choice of ζ ∈E(r)
q
we may identify E(r)
q
= ⟨ζ⟩


## Page 6


6
HOWIDA AL FRAN AND CHRISTOPHER TUFFLEY
with Zr. Therefore we may regard Dq,r as a semidirect product of the form Zordr(q)
q
⋊Zr, with
multiplication deﬁned by
(v, i) · (u, j) = (v + ζiu, i + j).
We necessarily have (Fq)(r) ≤Fqr−1, so Dq,r ≤Dq,r, with equality when q generates U(r), the
group of units mod r.
Remark 3.3. In the case r = 2 we have (Fq)(2) = Fq, E(2)
q
= {±1} and Dq,2 ∼= Zq ⋊Z2 ∼= Dq,
the dihedral group of order 2q given by the symmetries of a regular q-gon.
3.3. Properties of Dq,r. We establish some properties of Dq,r that will be used in what follows.
By construction V(r)
q
is a normal subgroup of Dq,r, and Dq,r/V(r)
q
∼= E(r)
q . Choosing 1 ̸= ζ ∈
E(r)
q
as above and identifying E(r)
q
= ⟨ζ⟩with Zr via ζi ↔i we therefore get a homomorphism
Dq,r →Zr. Given g ∈Dq,r we write [g] for the image of g in Zr under this map; thus if
g = (v, i) ∈V(r)
q
⋊Zr then [g] = i.
Our ﬁrst lemma, on elements of Dq,r, follows almost immediately from the corresponding
result [7, Lemma 3.2] for Dq,r.
Lemma 3.4.
(1) If g ∈Dq,r then the order of g is 1, q, or r.
(2) If g, h ∈Dq,r commute, then either g, h ∈V(r)
q , or g and h belong to the same cyclic
subgroup of order r.
(3) If g = (v, 0) ∈Dq,r has order q, then the conjugacy class of g is
{(ζiv, 0) : 0 ≤i ≤r −1},
and if g = (v, i) has order r then the conjugacy class of g is
{h : [h] = i} = {(v, i) : v ∈V(r)
q }.
Proof. Since Dq,r ≤Dq,r, parts (1) and (2) are immediate from [7, Lemma 3.2]. Part (3) then
follows by the same argument given there, which we now outline. By part (2) the centraliser
of g ∈Dq,r has order |V(r)
q | if g has order q, and order r if g has order r. Thus, the conjugacy
class of g has size r if g has order q, and size |V(r)
q | if g has order r. Part (3) now follows from
the fact that the conjugacy class of (v, 0) must contain the r element set consisting of the orbit
of v under the action of ⟨ζ⟩, and the fact that the conjugacy class of (v, i) is contained in the
set {h : [h] = i} of size |V(r)
q |.
□
Remark 3.5. Since q and r are prime, as a consequence of Lemma 3.4 we note that if g is a
nontrivial element of Dq,r, then g has an nth root in Dq,r if and only if the order of g is coprime
to n. In this case the nth root is unique and is equal to gk, where gk is the unique nth root of
g in ⟨g⟩. In particular, g has a unique nth root if gcd(qr, n) = 1.
We now show that Dq,r is generated by any element of order q, together with any element of
order r.
Lemma 3.6. Let α and β be elements of Dq,r of orders q and r, respectively. Then ⟨α, β⟩= Dq,r.
Proof. Let α = (u, 0), and without loss of generality let β = (v, 1). Write βj = (vj, j). Then
⟨α⟩= {(ku, 0) : 0 ≤k ≤q −1},
⟨β⟩= {(vj, j) : 0 ≤j ≤r −1}.


## Page 7


GENERALISED KNOT GROUPS OF SQUARE AND GRANNY KNOT ANALOGUES
7
Letting ⟨β⟩act on α by conjugation we see that
βjαβ−j = (vj, j)(u, 0)(vj, j)−1
= (vj, j)(u, 0)(−ζ−jvj, −j)
(since (vj, j)−1 = (−ζ−jvj, −j))
= (vj, j)(u −ζ−jvj, −j)
= (vj + ζj(u −ζ−jvj), j −j)
= (ζju, 0),
so (ζju, 0) belongs to ⟨α, β⟩for 0 ≤j ≤q −1.
Regarding V(r)
q
∼= (Zq)d as a vector space over Fq of dimension d = ordr(q) we claim that the
vectors u, ζu, . . ., ζd−1u are linearly independent, and therefore span V(r)
q . To show this we use
the fact that ζ is a root of the rth cyclotomic polynomial over Fq, which since r is prime and
coprime to q is given by
Qr(x) = xr −1
x −1 =
r−1
X
k=0
xr.
Moreover, by [4, Thm 3.47], Qr(x) factors over Fq into (r −1)/d monic irreducible polynomials
of degree d. In particular, this means that the irreducible polynomial of ζ over Fq has degree d.
Suppose now that
c0u + c1ζu + · · · + cd−1ζd−1u = 0,
(1)
where ci ∈Fq for i = 0, . . . , d −1. Factoring (1) we get
"d−1
X
i=0
ciζi
#
u = 0,
so Pd−1
i=0 ciζi = 0 ∈Fq. But then if some ci is nonzero ζ is a root of p(x) = Pd−1
i=0 cixi, a
polynomial over Fq of degree at most d −1. This is a contradiction, so we must have ci = 0 for
all i. Thus {ζiu : 0 ≤i ≤d −1} is a linearly independent set, as claimed.
We have now shown that V(r)
q
⊆⟨α, β⟩, which implies qd divides |⟨α, β⟩|. Since r necessarily
also divides |⟨α, β⟩|, the order of ⟨α, β⟩is divisible by qdr = |Dq,r|. It follows that we must have
⟨α, β⟩= Dq,r, as claimed.
□
A homomorphism from Ga,b to a group G corresponds to a solution to the equation xa = yb
in G. We make the following deﬁnition:
Deﬁnition 3.7. Let G be a group, and let a and b be positive integers. A solution (x, y) = (g, h)
to xa = yb in G is a cyclic solution if ⟨g, h⟩is a cyclic subgroup of G. Otherwise, the solution
is non-cyclic.
We now characterise when Dq,r has a non-cyclic solution to xa = yb, for a and b relatively
prime.
Lemma 3.8. Let a, b ≥2 be relatively prime positive integers. Any non-cyclic solution (x, y) =
(g, h) to xa = yb in Dq,r satisﬁes ga = hb = 1. Consequently, such a solution exists if and only
if q|a and r|b, or r|a and q|b.
Proof. Suppose that (x, y) = (g, h) is a solution to xa = yb in Dq,r such that ga = hb = k ̸= 1.
By Lemma 3.4 the subgroups ⟨g⟩and ⟨h⟩are each cyclic of prime order q or r, and as such
they are generated by any nontrivial element. Thus ⟨g⟩= ⟨h⟩= ⟨k⟩, and it follows that (g, h)
is a cyclic solution. Therefore any non-cyclic solution (g, h) must satisfy ga = hb = 1.


## Page 8


8
HOWIDA AL FRAN AND CHRISTOPHER TUFFLEY
Now let (x, y) = (g, h) be a non-cyclic solution to xa = yb in Dq,r. Then ga = 1, so a must
be divisible by at least one of q and r; and similarly hb = 1, so b must be divisible by at least
one of q and r also. But a and b are relatively prime, so it must be the case that either q|a and
r|b, or r|a and q|b.
Finally, we prove that a non-cyclic solution does exist if q|a and r|b, or r|a and q|b. Without
loss of generality, assume q|a and r|b. Let g be any element of order q, and let h be any element
of order r. Then ga = 1 = hb, so (x, y) = (g, h) is a solution to xa = yb; and moreover, it is a
non-cyclic solution because ⟨g, h⟩= Dq,r, by Lemma 3.6. This completes the proof.
□
Remark 3.9. Note that by Lemmas 3.6 and 3.8, any non-cyclic solution (x, y) = (g, h) to xa = yb
in Dq,r satisﬁes ⟨g, h⟩= Dq,r.
3.4. The construction of the wreath products Ws,t
q,r. We now describe the construction of
our target groups Wq,r
s,t as wreath products of the form Dq,r ≀Ds,t.
Deﬁnition 3.10. Given distinct primes q, r, s, t, let Cs,t ⊆Ds,t be the conjugacy class
Cs,t = {g ∈Ds,t : [g] = 1} = {g = (v, 1) ∈Ds,t : v ∈V(t)
s , 1 ∈Zt}.
For g ∈Cs,t and α ∈Ds,t we write the right action of Ds,t on Cs,t by conjugation as
g · α = α−1gα,
and we use this right action of Ds,t on Cs,t to deﬁne a left action of Ds,t on
(Dq,r)Cs,t = {ω = (ωg)g∈Cs,t : ωg ∈Dq,r}
by
(α · ω)g = ωg·α
for all α ∈Ds,t and ω ∈(Dq,r)Cs,t. (This is indeed a left action, because
(α · (β · ω))g = (β · ω)g·α = ω(g·α)·β = ωg·(αβ) = ((αβ) · ω)g,
and so α · (β · ω) = (αβ) · ω, as required.) We deﬁne Wq,r
s,t to be the semidirect product
Wq,r
s,t = Dq,r ≀Ds,t = (Dq,r)Cs,t ⋊Ds,t,
where Ds,t acts on (Dq,r)Cs,t as above.
Elements of Wq,r
s,t have the form α =
 (αg)g∈Cs,t, ˆα

, where αg ∈Dq,r for all g ∈Cs,t and
ˆα ∈Ds,t. The group operations are given by
(αβ)g = αgβg·ˆα,
c
αβ = ˆα ˆβ,
(α−1)g = (αg·ˆα−1)−1,
d
α−1 = ˆα−1.
Remark 3.11. We use Lemma 3.4 to describe the cycle structure of an element ˆα ∈Ds,t acting
on Cs,t by conjugation. Note that all elements of Cs,t have order t. If ˆα has order s, then
α ∈V(t)
s . Elements of order s and t do not commute, and therefore the action of ˆα on Cs,t
has no ﬁxed point and all cycles are of length s, because s is prime. If ˆα has order t, then it
commutes only with elements of ⟨ˆα⟩. Since ˆαk ∈Cs,t for a unique k satisfying 0 ≤k ≤t −1,
the action of ˆα on Cs,t has a unique ﬁxed point, and therefore all other cycles have length t,
because t is prime.
We now describe some subgroups and homomorphisms associated with Wq,r
s,t that will be of
use. The constructions parallel those of [7, Sec. 3.1]. The quotient map [·] : Dq,r →Zr induces
a quotient map
Wq,r
s,t →Zr ≀Ds,t = (Zr)Cs,t ⋊Ds,t,


## Page 9


GENERALISED KNOT GROUPS OF SQUARE AND GRANNY KNOT ANALOGUES
9
which is given by
[α] = (([αg])g∈Cs,t, ˆα).
This map splits, and it will be convenient to distinguish a subgroup of Wq,r
s,t isomorphic to
Zr ≀Ds,t. Fixing ξ ∈Dq,r of order r such that [ξ] = 1 we let
Ar
s,t = ⟨ξ⟩≀Ds,t = ⟨ξ⟩Cs,t ⋊Ds,t ≤Wq,r
s,t.
Since Zr is abelian we may quotient further to get a well deﬁned map
Wq,r
s,t →(Zr)Cs,t ⋊Dq,r →Zr,
given by
[[α]] =
X
g∈Cs,t
[αg].
3.5. Illustration. As an aid to understanding the construction and arguments we illustrate
the group operations in a group of the form G = H ≀D5,2, where H is an arbitrary group.
As noted in Remark 3.3 we have D5,2 = D5, the dihedral group of order 10, given by the
symmetry group of a regular pentagon. For k ∈Z5 deﬁne ρk, σk : Z5 →Z5 by
i · ρk = k + i,
i · σk = 2k −i.
We write the argument to the left of the function so that composition is from left to right.
Then
D5,2 = D5 ∼= {ρk, σk : k ∈Z5}.
In addition, V(2)
5
is the subgroup ⟨ρ1⟩= {ρk : k ∈Z5} of rotations, and C5,2 is the conjugacy
class {σk : k ∈Z} consisting of the reﬂections. We have
ρ−1
k σiρk = σk+i = σi·ρk,
σ−1
k σiσk = σ2k−i = σi·σk,
so the action of D5 on C5,2 by conjugation may be identiﬁed with the action of D5 on Z5. We
may therefore regard G = H ≀D5 as HZ5 ⋊D5.
An element γ of G has the form
 (γi)i∈Z5, ˆγ

, where γi ∈H for each i and ˆγ ∈D5. We may
represent γ as an edge labelled directed graph with vertex set Z5, where we draw a directed
edge labelled γi from vertex i to vertex i · ˆγ. Figures 2(i) and 2(ii) present such diagrams for
elements α and β such that ˆα = ρ1 and ˆβ = σ0. The action of D5 on Z5 is faithful, so for γ ∈G
we can completely recover γ from its associated edge labelled directed graph.
Given group elements γ and δ of G, to calculate the product γδ we follow each directed edge
of γ, and then follow the directed edge of δ beginning at its terminus, multiplying the labels.
This gives a directed edge from i to i· c
γδ = (i· ˆγ)· ˆδ for each i, with label γiδi·ˆγ. So for example,
in the diagram for αβ in Figure 2(iii), we get an edge from 0 to 4 labelled α0β1 by following
the edge of α labelled α0 from 0 to 1, and then following the edge of β labelled β1 from 1 to 4.
Inverses are found by reversing all arrows and inverting all labels, as shown in Figure 2(iv)
for the element α of Figure 2(i). Note that the edge labelled (αi)−1 now begins at i · ˆα instead
of i, and so (α−1)i = (αi·ˆα−1)−1.
3.6. The cycle product and applications. As in Tuﬄey [7], the main tools we require to
work with our target groups Wq,r
s,t are the cycle product, and the notion of an element of Wq,r
s,tin
reduced standard form. These are useful in understanding conjugacy classes, centralisers and
mth powers in Wq,r
s,t. Adapting the deﬁnitions from Hq,r
p
= Dq,r ≀PSL(2, p) to Wq,r
s,t = Dq,r ≀Ds,t
we deﬁne these as follows:


## Page 10


10
HOWIDA AL FRAN AND CHRISTOPHER TUFFLEY
(i)
0
1
2
3
4
α0
α1
α2
α3
α4
(ii)
0
1
2
3
4
β1
β2
β3
β4
β0
(iii)
0
1
2
3
4
α1β2
α3β4
α4β0
α0β1
α2β3
(iv)
0
1
2
3
4
(α0)−1
(α1)−1
(α2)−1
(α3)−1
(α4)−1
Figure 2. Illustrating the group operations in a group of the form G = H≀D5,2 =
H ≀D5. Diagrams representing elements (i) α with ˆα = ρ1; (ii) β with ˆβ = σ0;
(iii) αβ; and (iv) α−1.
Deﬁnition 3.12 (Tuﬄey [7, Sec. 3.4]). Given α ∈Wq,r
s,t and g ∈Cs,t, we let ℓg(ˆα) be the length
of the disjoint cycle of the action of ˆα on Cs,t that contains g. Then the cycle product of α
at g is the product
πg(α) =
ℓg(ˆα)−1
Y
r=0
αg·ˆαr = αgαg·ˆααg·ˆα2 · · · αg·ˆαℓg(ˆα)−1.
The cycle product is thus the ordered product, beginning at g, of αh for h in the disjoint cycle
of ˆα containing g. Observe that the value of the cycle product on a given cycle is dependent
on the beginning point g, while the conjugacy class is not, because πh·ˆα(α) = α−1
h πh(α)αh.
Deﬁnition 3.13 (See [7, Sec. 3.4]). Let γ belong to Wq,r
s,t. Then γ is in reduced standard
form if
γg·ˆγ = γg
for each g ∈Cs,t. In other words, γ is in reduced standard form if γg is constant on orbits of ˆγ.
Remark 3.14. In [7], an element satisfying the condition of Deﬁnition 3.13 is only said to be in
standard form, and to be in reduced standard form we further require that πg(γ) = γℓg(ˆγ)
g
= 1
if and only if γg = 1. We observe that these two notions co-incide in Wq,r
s,t, because the orders
of elements of Dq,r are coprime to the orders of elements of Ds,t. If πg(γ) = γℓg(ˆγ)
g
= 1 then


## Page 11


GENERALISED KNOT GROUPS OF SQUARE AND GRANNY KNOT ANALOGUES
11
ℓg(ˆγ) must divide the order of γg. But γg ∈Dq,r, so the order of γh is 1, q or r; and ℓg(ˆγ) is the
length of a cycle of ˆγ ∈Ds,t acting on Cs,t, so is 1, s or t. By construction q, r, s, t are distinct
primes, so if πg(γ) = 1 then γg = 1 also.
We now state as lemmas several applications of the cycle product to conjugacy classes,
centralisers and mth powers in Wq,r
s,t. Where proofs are not given see [7, Sec. 3.4]. Although the
proofs given there are for Hq,r
p
= Dq,r ≀PSL(2, p), they in fact apply to any group of the form
Dq,r ≀G = (Dq,r)X ⋊G or Dq,r ≀G = (Dq,r)X ⋊G, where G is a group and X is a right G-set.
This is because the structure of PSL(2, p) plays no role in the arguments: the arguments are
all carried out on the level of cycles and orbits of an element k ∈G acting on X, making use
of the properties of Dq,r given by [7, Lemma 3.2], or by Lemma 3.4 for Dq,r.
Our ﬁrst result is that every element of Wq,r
s,t may be conjugated to reduced standard form:
Lemma 3.15. Let α ∈Wq,r
s,t. Then α is conjugate to an element γ in reduced standard form
such that ˆγ = ˆα and πg(γ) is conjugate to πg(α) for all g ∈Cs,t.
Proof. Applying the argument of [7, Lemma 3.3], α is conjugate to such γ as required if ℓg(ˆα)
is coprime to the order of πg(α) for all g ∈Cs,t. But ℓg(ˆα) ∈{1, s, t} and ord(πg(α)) ∈{1, q, r}
for all g ∈Cs,t, and by construction q, r, s, t are distinct primes, so the coprimality condition is
always satisﬁed. Thus, the conclusion of the lemma holds for all α ∈Wq,r
s,t.
□
We now give some suﬃcient conditions for an element of Wq,r
s,t to be conjugate to an element
of Ar
s,t in reduced standard form:
Lemma 3.16 (See [7, Lemma 3.4]). Let α be an element of Wq,r
s,t in reduced standard form such
that αg has order 1 or r for all g ∈Cs,t. Then α is conjugate to an element γ of Ar
s,t in reduced
standard form such that ˆγ = ˆα and γg is conjugate to αg for all g.
Corollary 3.17. Let α be an element of Wq,r
s,t such that πg(α) has order 1 or r for all g ∈Cs,t.
Then α is conjugate to an element γ of Ar
s,t in reduced standard form such that ˆγ = ˆα.
Proof. By Lemma 3.15, α is conjugate to an element β in reduced standard form such that
ˆβ = ˆα and πg(β) is conjugate to πg(α) for all g ∈Cs,t. Thus, πg(β) has order 1 or r for all
g ∈Cs,t. Because β is in reduced standard form we have
πg(β) = βℓg(ˆβ)
g
,
where ℓg(ˆβ) ∈{1, s, t}. Since ord βg ∈{1, q, r}, and q and r are prime and coprime to st, it
must be the case that ord(βg) = ord(πg(β)), and so βg has order 1 or r for all g ∈Cs,t. Then
by Lemma 3.16 β, and hence also α, is conjugate to an element γ of Ar
s,t in reduced standard
form such that ˆγ = ˆβ = ˆα.
□
Next, we consider certain elements of the centraliser of an element in reduced standard form.
Lemma 3.18 (See [7, Lemma 3.5]). Let α ∈Wq,r
s,t be an element of Wq,r
s,t in reduced standard
form, and suppose that β commutes with α. If αg is constant on orbits of ˆβ, then βg commutes
with αg for all g ∈Cs,t, and βg is constant on orbits of ˆα.
In particular, the condition that αg is constant on orbits of ˆβ holds if ˆβ ∈⟨ˆα⟩. Finally, we
give a necessary condition for an element α of Wq,r
s,t to be an mth power:
Lemma 3.19 (See [7, Lemma 3.6]). Suppose that α = γm in Wq,r
s,t. Then ˆγm = ˆα and
πg(α) = (πg(γ))m/ gcd(ℓg(ˆγ),m).
In particular, the conjugacy class of πg(α) is constant on orbits of ˆγ; and if gcd(st, m) = 1 then
πg(α) = (πg(γ))m.


## Page 12


12
HOWIDA AL FRAN AND CHRISTOPHER TUFFLEY
4. Homomorphisms from Ga,b to Wq,r
s,t
4.1. Introduction. We will prove Theorem 1.1 in the following form:
Theorem 4.1. Let a, b, n ≥2 be positive integers such that gcd(a, b) = 1. Suppose that there
are prime numbers s|a and t|b such that gcd(st, n) = 1. Choose a prime q dividing n, and a
prime r coprime to 2nab. Then H = Wq,r
s,t satisﬁes the conclusion of Theorem 1.1; that is,
|Hom(Gn(GKa,b), Wq,r
s,t)| < |Hom(Gn(SKa,b), Wq,r
s,t)|.
The underlying strategy is identical to that used in [7] to distinguish the generalised knot
groups of the square and granny knots, SK = SK2,3 and GK = GK2,3. Both groups Gn(GKa,b),
Gn(SKa,b) are obtained from
Ha,b = π1(GKa,b) = π1(SKa,b) = ⟨x, y, z, w|xa = yb, wa = zb, ydx−c = zdw−c⟩
by adjoining an nth root of the common meridian µ = ydx−c = zdw−c that commutes with the
corresponding longitude λGKa,b = xawa or λSKa,b = xaw−a. Thus, to compare the number of
homomorphisms from Gn(GKa,b) and Gn(SKa,b) to a given ﬁnite group H we consider pairs
of the form (ρ, η), where ρ : Ha,b →H is a homomorphism and η ∈H is an nth root of ρ(µ).
We say that such a pair (ρ, η) is a map-root pair for Ha,b in H. For K = GKa,b or SKa,b a
map-root pair for Ha,b in H deﬁnes a homomorphism ˜ρ : Gn(K) →H precisely when it satisﬁes
the compatibility condition
ρ(λ)η = ηρ(λ).
For GKa,b this may be written in the form
ρ(xa)ρ(wa)η = ηρ(xa)ρ(wa)
or
ρ(x−a)ηρ(xa) = ρ(wa)ηρ(w−a),
while for SKa,b it may be written as
ρ(xa)ρ(w−a)η = ηρ(xa)ρ(w−a)
or
ρ(x−a)ηρ(xa) = ρ(w−a)ηρ(wa).
Thus, it suﬃces to prove the following:
(I) Every map-root pair for Ha,b in Wq,r
s,t that is compatible for GKa,b is also compatible for
SKa,b.
(II) There exist map-root pairs for Ha,b in Wq,r
s,t that are compatible for SKa,b but not GKa,b.
Since Ha,b = Ga,b∗⟨µ⟩Ga,b, a homomorphism ρ : Ha,b →H consists of a pair of homomorphisms
ρ1, ρ2 : Ga,b →H such that ρ1(µ) = ρ2(µ). We therefore begin by determining the possible
images of the meridian and longitude of Ga,b under a homomorphism Ga,b →Wq,r
s,t. The results
and proofs of this section parallel those of [7, Sec. 4].
4.2. The image and roots of the meridian. We characterise up to conjugacy solutions to
the equation ηn = α in Wq,r
s,t, with ˆα ̸= 1.
Lemma 4.2. Let n ≥2 be a positive integer, and let q, r, s, t be distinct primes such that q|n
and gcd(rst, n) = 1. If α ∈Wq,r
s,t is an nth power such that ˆα ̸= 1, then α is a conjugate to an
element of Ar
s,t in reduced standard form. Conversely, if α ∈Ar
s,t is in reduced standard form
and ˆα ̸= 1 then the solutions to ηn = α in Wq,r
s,t are described by
(1) ˆη = ˆαk, where ˆαk is the unique nth root of ˆα in ⟨ˆα⟩;
(2) ηg·ˆα = ηg for all g ∈Cs,t, and so also ηg·ˆη = ηg for all g ∈Cs,t;
(3) ηg = α1/n
g
∈⟨ξ⟩if αg ̸= 1, where 1/n is the multiplicative inverse of n in Zr; and
(4) ηg ∈V(r)
q
if αg = 1.
Consequently, the solutions to ηn = α in Wq,r
s,t are parameterised by (V(r)
q )c, where c is the
number of cycles of ˆα on which αg = 1.


## Page 13


GENERALISED KNOT GROUPS OF SQUARE AND GRANNY KNOT ANALOGUES
13
Proof. Suppose ηn = α. Then by Lemma 3.19 we have
πg(α) = (πg(η))n
for all g ∈Cs,t. Now q divides n, so πg(α) ∈Dq,r is a qth power in Dq,r and therefore πg(α)
has order 1 or r for all g. Therefore by Corollary 3.17 α is conjugate to an element of Ar
s,t in
reduced standard form, as claimed.
Now let α be an element of Ar
s,t in reduced standard form such that ˆα ̸= 1, and suppose that
η ∈Wq,r
s,t satisﬁes ηn = α. Then we must have ˆηn = ˆα in Ds,t, and since gcd(st, n) = 1, by
Remark 3.5 ˆη = ˆαk, where ˆαk is the unique nth root of ˆα in ⟨ˆα⟩. This establishes part (1).
The order of ˆα is prime, so the orbits of ˆη = ˆαk and the orbits of ˆα coincide. Therefore αg is
constant on orbits of ˆη, because α is in reduced standard form. Since α = ηn commutes with η,
Lemma 3.18 implies that αg commutes with ηg for all g ∈Cs,t, and that ηg is constant on the
orbits of ˆα. Thus ηg·ˆα = ηg for all g ∈Cs,t, and then also ηg·ˆη = ηg for all g, because ˆη = ˆαk.
This proves part (2).
We have now shown that η is in reduced standard form. We therefore have
αg = (ηn)g = (ηg)n
in Dq,r. By hypothesis n is divisible by q but not by r. Therefore, by Remark 3.5 either αg is
of order r and ηg is the unique nth root of αg in ⟨αg⟩= ⟨ξ⟩, or αg = 1 and then we can let
ηh = ηg = v for all h in the orbit of g under ˆη, for any v ∈V(r)
q . This proves parts (3) and (4).
These values (with v chosen independently on each orbit where αg = 1) together with ˆη = ˆαk
do in fact deﬁne nth roots, so the nth roots of α are parameterised by (V(r)
q )c, where c is the
number of cycles of ˆα on which αg = 1.
□
4.3. The image of the longitude. We now determine the form of the image of the longitude
xa = yb, under the assumption that the meridian maps to an element α of the form considered
in Lemma 4.2.
Lemma 4.3. Let a, b, n ≥2 be positive integers such that gcd(a, b) = 1, and let q, r, s, t be
distinct primes satisfying the conditions of Theorem 4.1. Let α be an element of Ar
s,t in reduced
standard form such that ˆα is nontrivial. Suppose that ρ : Ga,b →Wq,r
s,t is such that ρ(µ) = α
and let
ρ(x) = χ,
ρ(y) = ψ,
ρ(xa) = ρ(yb) = ε.
If ⟨ˆχ, ˆψ⟩is a cyclic subgroup of Ds,t then ⟨χ, ψ⟩is itself a cyclic subgroup of Wq,r
s,t, and ε = αab.
Otherwise, if ⟨ˆχ, ˆψ⟩is a non-cyclic subgroup of Ds,t then
(1) ˆε = 1;
(2) εg is constant on orbits of ˆα;
(3) the conjugacy class of εg is constant on Cs,t;
(4) [εg] =
ab
sordt(s)[[α]] ∈Zr for all g ∈Cs,t;
(5) εg = ξab[[α]]/sordt(s) if αg ̸= 1.
Proof. We consider the cases where ⟨ˆχ, ˆψ⟩is a cyclic and non-cyclic subgroup of Ds,t in turn.
4.3.1. The cyclic case. If ⟨ˆχ, ˆψ⟩is a cyclic subgroup of Ds,t, then the homomorphism ˆρ : Ga,b →
Ds,t given by ˆρ(ω) = d
ρ(ω) factors through the abelianisation Ga,b →Z. The abelianisation is
generated by the image of the meridian, so
ˆχ = ˆαb,
ˆψ = ˆαa,
ˆε = ˆαab.


## Page 14


14
HOWIDA AL FRAN AND CHRISTOPHER TUFFLEY
Now every nontrivial element of Ds,t has order s or t, and s|a and t|b, so ˆε = 1 and either ˆχ = 1
or ˆψ = 1.
The construction of Ds,t is not symmetric in s and t, so we cannot simply assume without
loss of generality that ˆχ = 1 ∈Ds,t. Nevertheless, the arguments in both cases are entirely
analogous so we just present one of them. Suppose then that ˆχ = 1 (that is, suppose that ˆα
has order t). Then the entries of ε = χa are simply given by
εg = χa
g
for each g ∈Cs,t. The primes q and r are coprime to a, so there are integers c and d such that
ac ≡1 mod q, and ad ≡1 mod r, and then by the Chinese Remainder Theorem there is an
integer k such that k ≡c mod q and k ≡d mod r. Then ak ≡1 mod qr. Noting that χg has
order 1, q or r we then get
εk
g = (χa
g)k = χak
g = χg,
and since ˆε = ˆχ = 1 we get χ = εk.
Recall that xa = yb generates the centre of Ga,b. Thus, ε commutes with ψ, and so χ = εk
commutes with ψ also. Therefore ρ(Ga,b) = ⟨χ, ψ⟩is abelian, so ρ itself factors through the
abelianisation Ga,b →Z. Since the abelianisation is generated by the meridian we have
χ = αb,
ψ = αa,
ε = αab.
4.3.2. The non-cyclic case. Suppose that ⟨ˆχ, ˆψ⟩is a non-cyclic subgroup of Ds,t. Then since
ˆχa = ˆψb = ˆε and ⟨ˆχ, ˆψ⟩is a non-cyclic subgroup of Ds,t, by Lemma 3.8 it must be the case that
ˆχ has order s, ˆψ has order t, and ˆε = 1 ∈Ds,t. Then αg is constant on the orbits of ˆε (since
each orbit is a singleton), and moreover α commutes with ε (since xa = yb generates the centre
of Ga,b). We may therefore apply Lemma 3.18 to conclude that εg commutes with αg for all
g ∈Cs,t, and εg is constant on orbits of ˆα. This proves parts (1) and (2).
To prove part (3) we apply Lemma 3.19 to ε = χa = ψb. Each orbit of ˆε acting on Cs,t is a
singleton, so εg = πg(ε) for all g and it follows that the conjugacy class of εg is constant on the
orbits of both ˆχ and ˆψ. But ⟨ˆχ, ˆψ⟩= Ds,t by Lemma 3.6 and Ds,t acts transitively on Cs,t, so
the conjugacy class of εg must be constant on Cs,t.
Since the conjugacy class of εg is constant on Cs,t, so is the value of [εg] ∈Zr. To prove
part (4) we evaluate this common value using the abelianisation [[·]] : Wq,r
s,t →Zr. On one hand
we have
[[ε]] =
X
h∈Cs,t
[εh] = |Cs,t| · [εg] = sordt(s)[εg],
and on the other we have
[[ε]] = [[χa]] = a[[χ]] = ab[[α]],
because α is the image of the meridian, which generates the abelianisation of Ga,b. Therefore
sordt(s)[εg] = ab[[α]] in Zr, and since s is coprime to r we may divide by sordt(s) to get [εg] =
ab[[α]]/sordt(s) in Zr.
Finally, to prove part (5), recall that αg ∈⟨ξ⟩for all g, and we have shown above that εg
commutes with αg for all g. By Lemma 3.4 nontrivial elements of ⟨ξ⟩commute only with other
elements of ⟨ξ⟩, so if αg ̸= 1 then εg ∈⟨ξ⟩also. Since [ξ] = 1 we must have εg = ξab[[α]]/sordt(s) if
αg ̸= 1.
□


## Page 15


GENERALISED KNOT GROUPS OF SQUARE AND GRANNY KNOT ANALOGUES
15
5. Proof of the Main Theorem
We now have all the ingredients we require to prove our main result by proving Theorem 4.1.
Recall that we will do this by proving the following two statements:
(I) Every map-root pair for Ha,b in Wq,r
s,t that is compatible for GKa,b is also compatible for
SKa,b.
(II) There exist map-root pairs for Ha,b in Wq,r
s,t that are compatible for SKa,b but not GKa,b.
The compatibility conditions are
GKa,b :
ρ(xa)ρ(wa)η = ηρ(xa)ρ(wa)
or
ρ(x−a)ηρ(xa) = ρ(wa)ηρ(w−a),
SKa,b :
ρ(xa)ρ(w−a)η = ηρ(xa)ρ(w−a)
or
ρ(x−a)ηρ(xa) = ρ(w−a)ηρ(wa).
To begin, let (ρ, η) be a map-root pair for Ha,b in Wq,r
s,t, and let ˆρ : Ha,b →Ds,t be the induced
map deﬁned by ˆρ(ω) = d
ρ(ω) for all ω ∈Ha,b. Our initial case division is according to whether
or not ˆρ is trivial. Since the conjugacy class of µ generates Ha,b, the map ˆρ is trivial if and only
if ˆρ(µ) = 1 ∈Ds,t.
5.1. Trivial induced maps to Ds,t. Suppose that ˆρ is trivial. Then we may regard the homo-
morphism ρ as a homomorphism Ha,b →(Dq,r)Cs,t, and as such it is a product of homomorphisms
ρg : Ha,b →Dq,r. Since ˆηn = ˆρ(µ) = 1 ∈Ds,t, and gcd(st, n) = 1, we must have ˆη = 1 ∈Ds,t
also. It follows that (ρ, η) decomposes as a collection of map-root pairs {(ρg, ηg) : g ∈Cs,t} for
Ha,b in Dq,r.
By hypothesis ab is coprime to qr, so by Lemma 3.8 any homomorphism Ga,b →Dq,r has
cyclic image. Consequently ρg(Ha,b) is cyclic too, generated by αg = ρg(µ). Then
ρg(xa) = ρg(wa) = αab
g = ηabn
g
,
so both ρg(xa) and ρg(wa) commute with ηg. It follows that (ρg, ηg) is compatible for both
GKa,b and SKa,b for all g ∈Cs,t, and hence that (ρ, η) is compatible for both GKa,b and SKa,b.
5.2. Nontrivial induced maps to Ds,t. Now suppose that ˆρ is nontrivial. Then ρ(µ) = ηn
is an nth power in Wq,r
s,t such that d
ρ(µ) ̸= 1, so by Lemma 4.2 it is conjugate to an element α
of Ar
s,t in reduced standard form. Let β ∈Wq,r
s,t be such that βρ(µ)β−1 = α, set η′ = βηβ−1,
and deﬁne ρ′ : Ha,b →Wq,r
s,t by ρ′(g) = βρ(g)β−1. Then (ρ′, η′) is a map-root pair for Ha,b in
Wq,r
s,t such that ρ′(µ) = α, and (ρ, η) is compatible for GKa,b or SKa,b if and only if (ρ′, η′) is.
So it suﬃces to prove statement (I) under the assumption that ρ(µ) = α is an element of Ar
s,t
in reduced standard form.
Let ε = ρ(xa), δ = ρ(wa). Then ε and δ are each described by Lemma 4.3, and the compati-
bility conditions may be written as
GKa,b :
ηεδ = εδη
or
ε−1ηε = δηδ−1,
SKa,b :
ηεδ−1 = εδ−1η
or
ε−1ηε = δ−1ηδ.
We consider two cases:
5.2.1. At least one of ε or δ is equal to αab. Without loss of generality suppose that δ = αab =
ηabn. Then δ commutes with η, so for both knots the compatibility condition is that ε commutes
with η also. Thus (ρ, η) is compatible for GKa,b if and only it is compatible for SKa,b.


## Page 16


16
HOWIDA AL FRAN AND CHRISTOPHER TUFFLEY
5.2.2. Neither ε nor δ is equal to αab. If ε ̸= αab ̸= δ then ε and δ are both described by
statements (1)–(5) of Lemma 4.3, and η is described by Lemma 4.2. We will make use of the
following lemma, with β equal to η, and γ equal to εδ and εδ−1 in turn:
Lemma 5.1. Suppose that β, γ ∈Wq,r
s,t are such that ˆβ, ˆγ ∈Ds,t commute, and βg·ˆγ = βg,
γg· ˆβ = γg for all g ∈Cs,t. Then βγ = γβ if and only if βgγg = γgβg for all g ∈Cs,t.
In particular, the hypotheses of Lemma 5.1 are satisﬁed if ˆγ = 1 and γg· ˆβ = γg for all g ∈Cs,t.
We will use the lemma in this special case.
Proof. Since ˆβ commutes with ˆγ we have c
βγ = ˆβˆγ = ˆγ ˆβ = c
γβ. Therefore βγ = γβ if and only
if (βγ)g = (γβ)g for all g ∈Cs,t. On the one hand since γg· ˆβ = γg for all g we have
(βγ)g = βgγg· ˆβ = βgγg.
On the other, since βg·ˆγ = βg for all g we have
(γβ)g = γgβg·ˆγ = γgβg.
The result follows.
□
Since ˆε = ˆδ = 1 ∈Ds,t we have bεδ = d
εδ−1 = 1 ∈Ds,t also, and
(εδ)g = εgδg·ˆε = εgδg,
(εδ−1)g = εg(δ−1)g·ˆε = εg(δ−1)g = εg(δg·ˆδ−1)−1 = εg(δg)−1.
Then by Lemma 4.3 part (2) we have
(εδ)g·ˆη = εg·ˆηδg·ˆη = εg·ˆαkδg·ˆαk = εgδg = (εδ)g,
(εδ−1)g·ˆη = εg·ˆη(δg·ˆη)−1 = εg·ˆαk(δg·ˆαk)−1 = εg(δg)−1 = (εδ−1)g,
so Lemma 5.1 applies with β = η and γ equal to either εδ or εδ−1.
We now check when ηg commutes with each of (εδ)g and (εδ−1)g. We consider two cases,
according to whether or not αg = 1:
(1) If αg ̸= 1 then ηg, εg and δg all belong to ⟨ξ⟩, and so ηg commutes with both (εδ)g and
(εδ−1)g. (In fact we have εg = δg = ξab[[α]]/sordt(s), so
(εδ)g = ξ2ab[[α]]/sordt(s),
(εδ−1)g = 1.)
(2) If αg = 1 then ηg ∈V(r)
q . Applying [·] : Dq,r →Zr to each of (ηδ)g and (εδ−1) we get
[(εδ)g] = [εg] + [δg] = 2ab[[α]]
sordt(s) ,
[(εδ−1)g] = [εg] −[δg] = 0,
and since r is chosen coprime to 2ab it follows that (εδ−1)g ∈V(r)
q
for all g, but (εδ)g ∈
V(r)
q
if and only if [[α]] = 0 ∈Zr. It follows that (εδ−1)g always commutes with ηg, but
(εδ)g only commutes with ηg if ηg = 1, or [[α]] = 0.
We conclude that when ε ̸= αab ̸= δ, every map-root pair is compatible for SKa,b, but (ρ, η)
is compatible for GKa,b only if [[α]] = 0, or if ηg = 1 whenever αg = 1. In the next section,
we will complete the proof of the theorem by showing that there exists ρ realising [[α]] ̸= 0,
together with αg = 1 for some g ∈Cs,t.


## Page 17


GENERALISED KNOT GROUPS OF SQUARE AND GRANNY KNOT ANALOGUES
17
5.3. Realisation. Choose ˆχ, ˆψ ∈Ds,t arbitrarily such that ˆχ has order s and ˆψ has order
t. Then since s|a and t|b there is a homomorphism ˆρ : Ga,b →Ds,t such that ˆρ(x) = ˆχ and
ˆρ(y) = ˆψ.
By Theorem 2.1 the meridian of Ta,b in Ga,b is given by µ = ydx−c, where ad −bc = 1. Both
c and d may be chosen to be positive, and we observe that gcd(c, s) = gcd(d, t) = 1, which
implies that ˆχc ̸= 1 ̸= ˆψd. Therefore ˆχc has order s, and ˆψd has order t. Let ˆβ = ˆρ(µ) = ˆψd ˆχ−c,
and note that ˆβ must have order t, because ˆχc belongs to V(t)
s
but ˆψd does not.
Since ˆβ has order t, by Remark 3.11 its action on Cs,t has a unique ﬁxed point f (namely,
whichever power of ˆβ lies in Cs,t). The ﬁxed point f cannot be the ﬁxed point of ˆψ, because
then f would be ﬁxed by ˆχc = ˆβ−1 ˆψd, which acts freely. Extend ˆχ, ˆψ to elements of Wq,r
s,t by
deﬁning χg = ξb for all g ∈Cs,t, and
ψg =





ξa+1,
if g = f · ˆψ−1;
ξa−1,
if g = f;
ξa,
otherwise.
The cycle of ˆψ acting on f is illustrated in Figure 3 in the case t = 7. Then it is seen (using
Figure 3 for the cycle of ˆψ containing f) that πg(ψ) = ξat for all g not the ﬁxed point of ˆψ. It
then follows that
(χa)g = (ψb)g = ξab
for all g ∈Cs,t. Since also ˆχa = ˆψb = 1, we have χa = ψb, and therefore ρ(x) = χ, ρ(y) = ψ
deﬁnes a homomorphism ρ : Ga,b →Wq,r
s,t. We may then obtain a homomorphism ρ : Ha,b →
Wq,r
s,t by setting ρ(w) = χ, ρ(z) = ψ also.
We now calculate χ−c and ψd in preparation for computing β = ρ(µ) = ψdχ−c. Since χg = ξb
for all g we have simply (χ−c)g = ξ−bc for all g; and referring again to Figure 3, we have
(ψd)g = ξad except at those points where the product
(ψd)g =
d−1
Y
k=0
ψg· ˆψk
begins at f or ends at f · ˆψ−1. The latter point is where g · ˆψd−1 = f · ˆψ−1, so g = f · ˆψ−d and
we have
(ψd)g =





ξad−1,
if g = f;
ξad+1,
if g = f · ˆψ−d;
ξad,
otherwise.
Then
βg = (ψdχ−c)g = (ψd)g(χ−c)g· ˆψd = (ψd)gξ−bc,
so
βg =





ξad−bc−1 = ξ0 = 1,
if g = f;
ξad−bc+1 = ξ2,
if g = f · ˆψ−d;
ξad−bc = ξ,
otherwise.
Note that [[β]] = sordt(s) ̸≡0 mod r, because gcd(r, s) = 1. By Lemmas 3.15 and 3.16 there
exists ω ∈Wq,r
s,t such that α = ωβω−1 is an element of Ar
s,t in reduced standard form, with


## Page 18


18
HOWIDA AL FRAN AND CHRISTOPHER TUFFLEY
f · ˆψ−1
f
f · ˆψ
f · ˆψ2
ξa
ξa
ξa
ξa
ξa
ξa−1
ξa+1
Figure 3. Diagram of the cycle of ˆψ containing f in the case where t = 7.
ˆα = ˆβ and
αg =





1,
if g = f;
ξ(t+1)/t,
if g ∈(f · ˆψ−d) · ⟨ˆα⟩;
ξ,
otherwise.
We still have [[α]] ̸= 0, so the homomorphism ρ′ : Ha,b →Wq,r
s,t deﬁned by ρ′(g) = ωρ(g)ω−1
realises the case where there are nth roots of ρ′(µ) = α that are compatible for SKa,b but not
GKa,b, namely, pairs (ρ′, η) where ηf ̸= 1. This establishes statement (II), and completes the
proof of Theorem 4.1.
References
[1] Gerhard Burde, Heiner Zieschang, and Michael Heusener. Knots, volume 5 of De Gruyter Studies in Math-
ematics. De Gruyter, Berlin, extended edition, 2014.
[2] C. McA. Gordon and J. Luecke. Knots are determined by their complements. J. Amer. Math. Soc., 2(2):371–
415, 1989.
[3] A. J. Kelly. Groups from link diagrams. Doctoral thesis, U. Warwick, 1990.
[4] Rudolf Lidl and Harald Niederreiter. Finite ﬁelds, volume 20 of Encyclopedia of Mathematics and its Appli-
cations. Cambridge University Press, Cambridge, second edition, 1997. With a foreword by P. M. Cohn.
[5] Xiao-Song Lin and Sam Nelson. On generalized knot groups. J. Knot Theory Ramiﬁcations, 17(3):263–272,
2008. Eprint arXiv:math.GT/0407050.
[6] Sam Nelson and Walter D. Neumann. The 2-generalized knot group determines the knot. Commun. Contemp.
Math., 10(suppl. 1):843–847, 2008. Eprint arXiv:0804.0807.
[7] Christopher Tuﬄey. Generalized knot groups distinguish the square and granny knots. J. Knot Theory
Ramiﬁcations, 18(8):1129–1157, 2009. With an appendix by David Savitt. Eprint arXiv:0706.1807.
[8] Masaaki Wada. Group invariants of links. Topology, 31(2):399–406, 1992.
Institute of Fundamental Sciences, Massey University, Private Bag 11 222, Palmerston
North 4442, New Zealand
E-mail address: c.tuffley@massey.ac.nz

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 1810_07853v1_distinguishing_the_generalised_knot_groups_of_square_and_granny_knot_analogues
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1810_07853V1_DISTINGUISHING_THE_GENERALISED_KNOT_GROUPS_OF_SQUARE_AND_GRANNY_KNOT_ANALOGUES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
