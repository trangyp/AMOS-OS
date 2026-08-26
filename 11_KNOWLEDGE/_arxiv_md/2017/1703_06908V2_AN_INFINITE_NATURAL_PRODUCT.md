---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1703.06908v2
source: arxiv
tags: [arxiv, fractal, knowledge, math, reference]
---
# 1703.06908v2_An_infinite_natural_product

> Source: 1703.06908v2_An_infinite_natural_product.pdf

> Pages: 16

---


## Page 1


arXiv:1703.06908v2  [math.LO]  21 May 2017
AN INFINITE NATURAL PRODUCT
PAOLO LIPPARINI
Abstract. We study an inﬁnite countable iteration of the nat-
ural product between ordinals. We present an “eﬀective” way to
compute this countable natural product; in the non trivial cases
the result depends only on the natural sum of the degrees of the
factors, where the degree of a nonzero ordinal is the largest expo-
nent in its Cantor normal form representation. Thus we are able
to lift former results about inﬁnitary sums to inﬁnitary products.
Finally, we provide an order-theoretical characterization of the in-
ﬁnite natural product; this characterization merges in a nontrivial
way a theorem by Carruth describing the natural product of two
ordinals and a known description of the ordinal product of a pos-
sibly inﬁnite sequence of ordinals.
1. Introduction
The usual addition ` and multiplication ¨ between ordinals can be
deﬁned by transﬁnite recursion and have a clear order-theoretical mean-
ing; for example, α`β is the order-type of a copy of α to which a copy
of β is added at the top. However, ` and ¨ have very poor algebraic
properties; though both are associative, they are neither commutative
nor cancellative, left distributivity fails, etc. See, e. g., Bachmann [B],
Hausdorﬀ[Hau] and Sierpi´nski [S3] for full details.
In certain cases it is useful to consider the so-called natural opera-
tions # and b. These operations are deﬁned by expressing the operands
in Cantor normal form and, roughly, treating the expressions as if they
were polynomials in ω. The natural operations have the advantage of
satisfying good algebraic properties; moreover, in a few cases they have
found mathematical applications even outside logic. See e. g., Carruth
[Ca] and Toulmin [T]. Further references, including some variants and
historical remarks, can be found in Altman [A] and Ehrlich [E, pp.
24–25]. It is also interesting to observe that the natural operations
2010 Mathematics Subject Classiﬁcation. 03E10, 06A05.
Key words and phrases. Ordinal number; (inﬁnite) (natural) product, sum; (lo-
cally) ﬁnitely Carruth extension.
Work performed under the auspices of G.N.S.A.G.A. Work partially supported
by PRIN 2012 “Logica, Modelli e Insiemi”.
1


## Page 2


2
PAOLO LIPPARINI
are the restriction to the ordinals of the surreal operations on Conway
“Numbers” [Co]. Limited to the case of the ordinal natural sum, the
corresponding two-arguments recursive deﬁnition appears implicitly as
early as in the proof of de Jongh and Parikh [dJP, Theorem 3.4].
An inﬁnitary generalization of the natural sum in which the supre-
mum is taken at the limit stage has been considered in Wang [W] and
V¨a¨an¨anen and Wang [VW] with applications to inﬁnitary logics. This
inﬁnite natural sum has been studied in detail in [L1], where an order-
theoretical characterization has been provided. In the present note we
introduce and study the analogously deﬁned inﬁnitary product. The
computation of the inﬁnite natural product can be reduced to the com-
putation of some—possibly inﬁnite—natural sum; in particular, we can
directly transfer results from sums to products, rather than repeating
essentially the same arguments. Curiously, the method applies to the
usual inﬁnitary operations, too. See Theorem 2.8 and Corollary 2.9;
we are not aware of previous uses of this technique.
Order-theoretical characterizations of the ﬁnitary natural operations
have been provided in Carruth [Ca]. Some characterizations seem to
have been independently rediscovered many times, e. g., Toulmin [T]
and de Jongh and Parikh [dJP]. As we showed in [L1], Carruth charac-
terization of the ﬁnite natural sum cannot be generalized as it stands to
the inﬁnitary natural sum; see, in particular, the comments at the be-
ginning of [L1, Section 4]. A similar situation occurs for the inﬁnitary
natural product; see Subsection 3.4 below. In the case of the inﬁnite
natural sum the diﬃculty can be circumvented by imposing a ﬁniteness
condition to a Carruth-like description: see [L1, Theorem 4.7]. As we
shall show in Section 3, a similar result holds for the inﬁnite natural
product, though the situation gets technically more involved.
To explain our construction in some detail, it is well known that
the usual ﬁnite ordinal product is order-theoretically characterized by
taking the reverse lexicographical order on the product of the factors.
Less known, the same holds in the inﬁnite case, too, provided that in the
product one takes into account only elements with ﬁnite support. See
Hausdorﬀ[Hau, § 16] and Matsuzaka [Ma]. We show that the inﬁnite
natural product can be characterized by merging the representation by
Carruth and the just mentioned one; roughly, by using Carruth order
for a suﬃciently large but ﬁnite product of factors and then working as
in an ordinary product when we approach inﬁnity. Quite surprisingly,
a local version of the result holds. Namely, if ď1 is a linear order on the
ﬁnite-support-product of a sequence pαiqiăω of ordinals and ď1 is such
that, for every element c, the set of the ď1 predecessors of c is built in a
way similar to above, then ď1 is a well-order of order type less than or


## Page 3


AN INFINITE NATURAL PRODUCT
3
equal to the inﬁnite natural product of the αi’s. Moreover, the inﬁnite
natural product is actually the maximum of the ordinals obtained this
way, that is, the order-type of the product can always be realized in
the above way. See Section 3 and in particular Theorem 3.1 for full
details.
1.1. Preliminaries. We assume familiarity with the basic theory of
ordinal numbers. Unexplained notions and notations are standard and
can be found, e. g., in the mentioned books [B, Hau, S3]. Notice that
here sums, products and exponentiations are always considered in the
ordinal sense. The usual ordinal product of two ordinals α and β is
denoted by αβ or sometimes α ¨ β for clarity. The classical inﬁnitary
ordinal product is denoted by ś
iăω αi. Recall that every nonzero or-
dinal α can be expressed in Cantor normal form in a unique way as
follows
α “ ωξkrk ` ωξk´1rk´1 ` ¨ ¨ ¨ ` ωξ1r1 ` ωξ0r0
for some integers k ě 0, rk, . . . , r0 ą 0 and ordinals ξk ą ξk´1 ą ¨ ¨ ¨ ą
ξ1 ą ξ0. If β is another ordinal expressed in Cantor normal form, the
natural sum α # β is obtained by summing the two expressions as if
they were polynomials in ω. The natural product αbβ is computed by
using the rule ωξ bωη “ ωξ#η and then expanding again by “linearity”.
Both # and b are commutative, associative and cancellative (except
for multiplication by 0, of course). If pαiqiăω is a sequence of ordinals,
#iăω αi “ supnăωpα0 # α1 # ¨ ¨ ¨ # αn´1q. See [W, VW, L1] for further
details about #.
2. An infinite natural product
Deﬁnition 2.1. Suppose that pαiqiăω is a sequence of ordinals.
For i ă ω, let Pi denote the partial natural product α0bα1b¨ ¨ ¨bαi´1,
with the convention P0 “ 1.
Deﬁne Â
iăω αi “ limiăω Pi.
This means that Â
iăω αi “ 0 if at least one αi is 0 and Â
iăω αi “
supiăω Pi if each αi is diﬀerent from 0 (cf. Clause (5) in Proposition
2.2 below).
From now on, when not otherwise speciﬁed, pαiqiăω is a ﬁxed se-
quence of ordinals and the partial natural products Pi are always com-
puted as above and with respect to the sequence pαiqiăω.
We now state some simple facts about the inﬁnitary operation Â.
Only (2), (5) and (6) will be used in what follows.
Proposition 2.2. Let αi, βi be two sequences of ordinals and n, m ă ω.
(1) ś
iăω αi ď Â
iăω αi


## Page 4


4
PAOLO LIPPARINI
(2) If βi ď αi, for every i ă ω, then Â
iăω βi ď Â
iăω αi
(3) If π is a permutation of ω, then Â
iăω αi “ Â
iăω απpiq
(4) More generally, suppose that pFhqhăω is a partition of ω into
ﬁnite subsets, say, Fh “ tj1, . . . , jrphqu, for every h P ω. Then
â
iăω
αi “
â
hăω
â
jPFh
αj “
â
hăω
pαj1 b αj2 b ¨ ¨ ¨ b αjrphqq
Suppose in addition that αi ‰ 0, for every i ă ω.
(5) If i ă j, then Pi ď Pj; equality holds if and only if αi “ ¨ ¨ ¨ “
αj´1 “ 1.
(6) For every n ă ω, we have Pn ď Â
iăω αi; equality holds if and
only if αi “ 1, for every i ě n.
Proof. Easy, using the properties of the ﬁnitary b. We just comment
on (3). This is trivial if at least one αi is 0. Otherwise, every partial
product on the left is bounded by some suﬃciently long partial product
on the right (by monotonicity, associativity and commutativity of b,
and since all factors are nonzero by assumption); the converse holds as
well, hence the inﬁnitary products are equal.
Let us mention that (3) and (4) can be also proved by using The-
orem 2.6 below and the corresponding properties of # given in [L1,
Proposition 2.4(5)(6)].
□
Lemma 2.3. If pβiqiăω is a sequence of ordinals and β “ #iăω βi,
then
â
iăω
ωβi “ ωβ
Proof. Since ωβi is always diﬀerent from 0, we have Â
iăω αi “ supiăω Pi.
Here, of course, Pi is computed with respect to the sequence given by
αi “ ωβi, for i ă ω.
By a property of the natural product (or the deﬁnition, if you like),
we have Pi “ ωβ0 b ωβ1 b ¨ ¨ ¨ b ωβi´1 “ ωβ0#β1#¨¨¨#βi´1, for every i ă
ω.
Letting Bi “ β0 # β1 # ¨ ¨ ¨ # βi´1, we have by deﬁnition β “
#iăω βi “ supiăω Bi. But then Â
iăω αi “ supiăω Pi “ supiăω ωBi “
ωβ by continuity of the exponentiation.
□
Let α be a nonzero ordinal expressed as ωξkrk `¨ ¨ ¨`ωξ0r0 in Cantor
normal form. The ordinal dpαq “ ξk will be called the degree or the
largest exponent of α. The ordinal mpαq “ ωξkrk will be called the
leading monomial of α. By convention, we set mp0q “ 0. The following
lemma is trivial, but it will be useful in many situations.
Lemma 2.4. For every ordinal α,
mpαq ď α ď mpαq ` mpαq “ mpαq ¨ 2 ď mpαq b 2


## Page 5


AN INFINITE NATURAL PRODUCT
5
Lemma 2.5. If pαiqiăω is a sequence of ordinals which is not eventually
1, then
â
iăω
αi “
â
iăω
mpαiq
Proof. This is trivial if at least one αi is 0.
Hence suppose that αi ‰ 0, for all i ă ω, and that pαiqiăω is not
eventually 1. The inequality Â
iăω αi ě Â
iăω mpαiq is trivial by mono-
tonicity (Proposition 2.2(2)), since α ě mpαq, for every ordinal α.
To prove the converse, we show that, for every h ă ω, there is k ă ω
such that Â
iăh αi ď Â
iăk mpαiq. This is enough since if all the αi’s are
nonzero, then the succession of the partial products is nondecreasing
(Proposition 2.2(5)).
It is a trivial property of the ﬁnitary natural
product that mpÂ
iăh αiq “ Â
iăh mpαiq (by strict monotonicity of #).
Since pαiqiăω is not eventually 1, there is k ą h such that αk´1 ě
2. Then Â
iăk mpαiq ě
`Â
iăk´1 mpαiq
˘
b 2 ě pÂ
iăh mpαiqq b 2 “
m pÂ
iăh αiq b 2 ě Â
iăh αi, by Lemma 2.4.
□
Theorem 2.6. Let pαiqiăω be a sequence of ordinals and let β “
#iăω dpαiq. The inﬁnite natural product Â
iăω αi can be computed ac-
cording to the following rules.
â
iăω
αi “ 0
if (and only if) at least one αi is equal to 0;
(1)
â
iăω
αi “ α0 b ¨ ¨ ¨ b αn´1
if αi “ 1, for every i ě n;
(2)
â
iăω
αi “ ωdpα0q#¨¨¨#dpαn´1q`1 “ ωβ`1
if αi ‰ 0, for all i ă ω,
αi ă ω, for all i ě n, and the sequence is not eventually 1;
(3)
â
iăω
αi “
â
iăω
ωdpαiq “ ωβ
if none of the above cases applies,
(4)
that is, no element of the sequence is 0 and the members of
the sequence are not eventually ă ω.
Before proving Theorem 2.6, we notice that it gives an eﬀective way
to compute Â
iăω αi, for every sequence pαiqiăω of ordinals. Apply (1)
if at least one αi is equal to 0; if this is not the case, apply (2) if
the αi are eventually 1; if not, then exactly one of (3) or (4) occurs.
Notice that conditions (1) and (2) in Theorem 2.6 might overlap, and
n in (2) and (3) is not uniquely deﬁned, but the conditions give the
same outcome in any overlapping case. Notice also that the expression
dpα0q # ¨ ¨ ¨ # dpαn´1q ` 1 in (3) causes no ambiguity, since pdpα0q #
¨ ¨ ¨ # dpαn´1qq ` 1 “ dpα0q # ¨ ¨ ¨ # pdpαn´1q ` 1q.


## Page 6


6
PAOLO LIPPARINI
Proof. The result follows trivially from the deﬁnitions if some αi is
equal to 0 or when the sequence is eventually 1.
If we are in the case given by (3), then, for every ℓă ω, there is
h ą n such that there are at least ℓ-many αi ě 2, where the index i
varies between n and h. Thus Â
iăh`1 αi ě ωdpα0q b ¨ ¨ ¨ b ωdpαn´1q b 2ℓ
since α ě ωdpαq, for every nonzero ordinal α. Since ℓis arbitrary, we get
Â
iăω αi “ suphăω
Â
iăh`1 αi ě supℓăωpωdpα0q b ¨ ¨ ¨ b ωdpαn´1q b 2ℓq “
supℓăω ωdpα0q#¨¨¨#dpαn´1q2ℓ“ ωdpα0q#¨¨¨#dpαn´1q`1, since ωε b 2 “ ωε2 and
suppăω ωεp “ ωε`1, for every ordinal ε.
In the other direction, we have Â
iăω αi “ Â
iăω mpαiq from Lemma
2.5, hence it is enough to prove Â
iăω mpαiq ď ωdpα0q#¨¨¨#dpαn´1q`1. If
h ă ω, and, for every i ă ω, letting si be the only natural number such
that mpαiq “ ωdpαiqsi, then by associativity and commutativity of b,
we get Â
iăh`1 mpαiq “ ωdpα0q b s0 b ¨ ¨ ¨ b ωdpαhq b sh “ ωdpα0q b ¨ ¨ ¨ b
ωdpαhq b s0 b ¨ ¨ ¨ b sh ď ωdpα0q b ¨ ¨ ¨ b ωdpαn´1q b ω “ ωdpα0q#¨¨¨#dpαn´1q`1,
since dpαiq “ 0, for i ě n and, by construction, si ă ω, for every i ă ω.
Hence Â
iăω mpαiq “ suphăω
Â
iăh mpαiq ď ωdpα0q#¨¨¨#dpαn´1q`1.
The last identity in (3) follows from the already mentioned fact that
dpαiq “ 0, for i ě n, hence β “ #iăω dpαiq “ #iăn dpαiq.
The case given by (4) is similar and somewhat easier. The inequality
Â
iăω αi ě Â
iăω ωdpαiq is trivial by monotonicity.
For the converse, we use again the identity Â
iăω αi “ Â
iăω mpαiq
from Lemma 2.5. Arguing as in case (3), we have that, for every h ă ω,
Â
iďh mpαiq ď ωdpα0q b ¨ ¨ ¨ b ωdpαhq b ω, but there is some k ą h such
that αk ě ω, since the members of the sequence are not eventually ă ω.
Hence Â
iďh mpαiq ď ωdpα0q b ¨ ¨ ¨ b ωdpαhq b ω ď ωdpα0q b ¨ ¨ ¨ b ωdpαhq b
¨ ¨ ¨ b ωdpαkq ď Â
iăω ωdpαiq. In conclusion, Â
iăω αi “ Â
iăω mpαiq “
suphăω
Â
iďh mpαiq ď Â
iăω ωdpαiq.
The last identity is from Lemma 2.3.
□
Corollary 5.1 in [L1] can be used to provide a more precise evaluation
of β in case (4) in Theorem 2.6.
Corollary 2.7. Suppose that pαiqiăω is a sequence of ordinals such that
no element of the sequence is 0 and the members of the sequence are
not eventually ă ω (thus the sequence pdpαiqqiăω is not eventually 0).
Let ξ be the smallest ordinal such that ti ă ω | dpαiq ě ωξu is ﬁnite,
and enumerate those αi’s such that dpαiq ě ωξ as αi0, . . . , αik (the
sequence might be empty). Then Â
iăω αi “ ωβ, where β “ pdpαi0q #
¨ ¨ ¨ # dpαikqq ` ωξ.
We need the results analogous to Theorem 2.6 for the classical ordinal
product.


## Page 7


AN INFINITE NATURAL PRODUCT
7
Theorem 2.8.
(1) If pβiqiăω is a sequence of ordinals and β “
ř
iăω βi, then
ź
iăω
ωβi “ ωβ
(2) If pαiqiăω is a sequence of ordinals which is not eventually 1,
then
ź
iăω
αi “
ź
iăω
mpαiq
(3) Suppose that pαiqiăω is a sequence of nonzero ordinals which is
not eventually 1 and let β “ ř
iăω dpαiq. Then
ź
iăω
αi “ ωdpα0q`¨¨¨`dpαn´1q`1 “ ωβ`1
if αi ă ω, for all i ě n
ź
iăω
αi “
ź
iăω
ωdpαiq “ ωβ
if the sequence is not eventually ă ω
Proof. (1) Like the proof of Lemma 2.3, using the identity ωβ0ωβ1 . . .
ωβi´1 “ ωβ0`β1`¨¨¨`βi´1.
(2) Like the proof of Lemma 2.5. In fact, we do have mpś
iăh αiq “
ś
iăh mpαiq and this is enough for the proof.
(3) is proved as Theorem 2.6.
□
Theorems 2.6 and 2.8 can be used to “lift” some results from inﬁni-
tary sums to inﬁnitary products. To show how the method works, we
ﬁrst present a simple example, though only feebly connected with the
rest of this note.
Sierpi´nski [S1] showed that a sum ř
iăω αi of ordinals can assume
only ﬁnitely many values, by permuting the αi’s. A proof can be found
also in [L1]. Then Sierpi´nski in [S2] showed the analogous result for
an inﬁnite product. Using Theorem 2.8 we show that the result about
products is immediate from the result about sums.
Corollary 2.9. If pαiqiăω is a sequence of ordinals, one obtains only a
ﬁnite number of ordinals by considering all products of the form ś
iPI γi,
where pγiqiăω is a permutation of pαiqiăω, that is, there exists a bijec-
tion π : ω Ñ ω such that γi “ απpiq for every i ă ω.
Proof. This is trivial if some αi is 0, or if the αi’s are eventually 1, so
let us assume that none of the above cases occurs.
If the sequence is eventually ă ω, then the ﬁrst equation in Theorem
2.8(3) shows that we obtain only a ﬁnite number of products by taking
rearrangements of the factors, since the resulting products are given
by ωδ`1, where δ is a sum of dpα0q, . . . , dpαn´1q, taken in some order,
but there is only a ﬁnite number of rearrangements of this ﬁnite set,


## Page 8


8
PAOLO LIPPARINI
hence there are only a ﬁnite number of possibilities for δ (notice that
if αi ă ω, then dpαiq “ 0, hence the degrees of ﬁnite ordinals do not
contribute to the sum).
In the remaining case, the products obtained by rearrangements have
the form ωδ, with δ “ ř
iăω dpγiq, by the second equation in Theorem
2.8(3). The quoted result from [S1] shows that we have only a ﬁnite
number of possibilities for δ, hence there are only a ﬁnite number of
possibilities for the values of the rearranged products.
□
We now use Theorems 2.6 and 2.8 in a slightly more involved situa-
tion in order to transfer some results from [L1] about inﬁnite natural
sums to results about inﬁnite natural products.
Corollary 2.10. For every sequence pαiqiăω of ordinals there is m ă ω
such that, for every n ě m,
â
nďiăω
αi “
ź
nďiăω
αi
and
(5)
â
iăω
αi “ pα0 b ¨ ¨ ¨ b αn´1q ¨
â
nďiăω
αi
“ pα0 b ¨ ¨ ¨ b αn´1q ¨
ź
nďiăω
αi
(6)
and if, moreover, every αi is nonzero and the sequence is not eventually
1, then
â
iăω
αi “ ωβ0#¨¨¨#βn´1 ¨
â
nďiăω
αi
“ ωβ0#¨¨¨#βn´1 ¨
ź
nďiăω
αi
(7)
where βi “ dpαiq, for every i ă ω.
Proof. The result is trivial if the sequence is eventually 1; moreover,
(6) is trivial if some αi is 0. Furthermore, (5) is trivial if, for every
i ă ω, there is j ą i such that αj “ 0. Otherwise, by taking m large
enough, we have αi ą 0, for i ą m. Henceforth it is enough to prove
the result in the case when the sequence is not eventually 1 and all the
αi’s are nonzero.
We shall ﬁrst prove (5) and (7) and then derive (6). If the sequence
is eventually ă ω, then (5) is trivial, since in this case, for large enough
n, both sides are equal to ω. Then (7) is immediate from equation (3)
in Theorem 2.6, since ωβ0#¨¨¨#βn´1ω “ ωβ0#¨¨¨#βn´1`1.
Suppose now that the sequence pαiqiăω is not eventually ă ω, hence
the sequence pβiqiăω is not eventually 0. By [L1, Theorem 3.1], there
is m ă ω such that, for every n ě m, we have #nďiăω βi “ ř
nďiăω βi.


## Page 9


AN INFINITE NATURAL PRODUCT
9
Fixing some n ě m and letting β1 “ #nďiăω βi, we get Â
nďiăω αi “
ωβ1 “ ś
nďiăω αi from, respectively, equation (4) in Theorem 2.6 and
the last equation in Theorem 2.8(3). This proves (5).
Letting β “ #iăω βi, we notice that in [L1, Theorem 3.1] it has also
been proved that β “ pβ0 # ¨ ¨ ¨ # βn´1q ` β1. Using the above identity
and applying equation (4) in Theorem 2.6 twice, we get Â
iăω αi “
ωβ “ ωβ0#¨¨¨#βn´1ωβ1 “ ωβ0#¨¨¨#βn´1 Â
nďiăω αi, that is, (7) (the second
identity in (7) could be proved in the same way, but now it follows
immediately from (5)).
Equation (6) remains to be proved. We shall prove that in the non-
trivial cases the expressions given by (6) and (7) are equal. One direc-
tion is trivial, since ωβ0#¨¨¨#βn´1 “ ωβ0b¨ ¨ ¨bωβn´1 ď α0b¨ ¨ ¨bαn´1. For
the other direction, let us observe that, in the nontrivial cases, again
by Theorem 2.6, Â
nďiăω αi has the form ωβ, for some β ě 1. Then
pα0b¨ ¨ ¨bαn´1q¨Â
nďiăω αi “ pα0b¨ ¨ ¨bαn´1q¨ωβ ď mpα0b¨ ¨ ¨bαn´1q¨
2¨ωβ “ pmpα0qb¨ ¨ ¨bmpαn´1qq¨ωβ “ pωdpα0qs0b¨ ¨ ¨bωdpαn´1qsn´1q¨ωβ “
pωβ0 b ¨ ¨ ¨ b ωβn´1 b so . . . sn´1q ¨ ωβ “ ωβ0#¨¨¨#βn´1 ¨ so . . . sn´1 ¨ ωβ “
ωβ0#¨¨¨#βn´1 ¨ ωβ “ ωβ0#¨¨¨#βn´1 ¨ Â
nďiăω αi, where we used Lemma 2.4
and the facts that kωβ “ ωβ, whenever k ă ω and β ě 1, and that
ωξ b k “ ωξ ¨ k, for all ordinals k ă ω and ξ.
□
3. An order-theoretical characterization
3.1.
We refer to, e. g., Harzheim [Har] for a general reference about
ordered sets. As usual, when no risk of ambiguity is present, we shall
denote a (partially) ordered set pP, ďq simply as P. However, in many
situations, we shall have several diﬀerent orderings on the same set; in
that case we shall explicitly indicate the order. It is sometimes conve-
nient to deﬁne ď in terms of the associated ă relation and conversely.
As a standard convention, a ď b is equivalent to “either a “ b or a ă b”
(strict disjunction). We shall be quite informal about the distinction
and we shall use either ď or ă case by case according to convenience,
even when we are dealing with (essentially) the same order.
In order to avoid notational ambiguity, let us denote the cartesian
product of a family pAiqiPI of sets by Ś
iPI Ai. If each Ai is an ordered
set, with the order denoted by ďi, then a partial order ďˆ can be
deﬁned on Ś
iPI Ai componentwise. Namely, we put a ďˆ b if and only
if ai ďi bi, for every i P I. Apparently, for our purposes, the above
deﬁnition has little use when dealing with ordinals (more precisely,
order-types of well-ordered sets), since ordinals are linearly ordered,
but generally the above construction furnishes only a partially ordered
set. However, see below for uses of the ordered set pŚ
iPI Ai, ďˆq.


## Page 10


10
PAOLO LIPPARINI
3.2.
An order theoretical characterization of the ordinal product can
be given using lexicographic products. If pI, ďIq is reverse-well-ordered
and each Ai is an ordered set, then the anti-lexicographic order L˚
iPIAi “
pL˚
iPIAi, ď˚q on the set Ś
iPI Ai is obtained by putting
a ď˚ b if and only if either a “ b, or ai ăi bi, where i is the
largest element of I such that ai ‰ bi.
In other words, ď˚ orders L˚
iPIAi by the last diﬀerence. The deﬁnition
makes sense, since I is reverse-well-ordered. It turns out that if each
Ai is linearly ordered, then L˚
iPIAi is linearly ordered and if in addition
I is ﬁnite, then L˚
iPIAi is well-ordered. Moreover, for two ordinals α0
and α1, it happens that α0α1 is exactly the order-type of L˚
iă2 αi. This
can be obviously generalized to ﬁnite products.
A similar characterization can be given for inﬁnite products, but
some details should be made precise.
Suppose that each Ai is an
ordered set with order ďi and with a speciﬁed element 0i P Ai.
If
a P Ś
iPI Ai, the support supppaq of a is the set ti P I | ai ‰ 0iu.
Let Ś0
iPI Ai be the subset of Ś
iPI Ai consisting of those elements with
ﬁnite support. Of course, Ś0
iPI Ai inherits a partial order ď0
ˆ as a sub-
order of pŚ
iPI Ai, ďˆq. If I is linearly ordered, we can consider another
order L0
iPIAi “ pL0
iPIAi, ďLq on the set Ś0
iPI Ai deﬁned as follows.
(*) a ďL b if and only if either a “ b, or ai ăi bi, where i is the
largest element of supppaq Y supppbq such that ai ‰ bi.
The deﬁnition makes sense, since supppaq Y supppbq is ﬁnite and I is
linearly ordered. Of course, when I is ﬁnite, Ś0
iPI Ai and Ś
iPI Ai are
the same set and L0
iPI and L˚
iPI are the same order. It is known that,
for every sequence pαiqiăδ of ordinals, L0
iăδ αi is well-ordered and has
order-type ś
iăδ αi. Here the speciﬁed element 0i is always chosen to
be the ordinal 0. See [B, III, § 10 1.2 and § 11 Satz 7], Hausdorﬀ[Hau,
§ 16] and Matsuzaka [Ma] for details. Of course, we could have seen
just by cardinality considerations that Ś
iăδ Ai does not work in order
to obtain an order theoretical characterization of ś
iăδ αi in the case
when δ is inﬁnite.
3.3.
Dealing now with natural products, a characterization in the ﬁ-
nite case has been found by Carruth [Ca]. He proved that α0 b α1
is the largest ordinal which is the order-type of some linear extension
of the componentwise order on α0 ˆ α1. Here α0 ˆ α1 is ordered as
pŚ
iă2 αi, ďˆq in the above notation. Carruth result includes the proof
that such an ordinal exists, that is, that each such linear extension is a
well-order and that the set of order-types of such linear extensions has
a maximum, not just a supremum. From the modern point of view, this


## Page 11


AN INFINITE NATURAL PRODUCT
11
can be seen as a special case of theorems by Wolk [Wo] and de Jongh,
Parikh [dJP], since the product of two well quasi-orders (in particular,
two well-orders) is still a well quasi order. See, e. g., [Mi]. Carruth
result obviously extends to the case of any ﬁnite number of factors.
3.4.
Some diﬃculties are encountered when trying to unify the results
recalled in 3.2 and 3.3. Let us limit ourselves to the simplest inﬁnite
case of an ω-indexed sequence, which is the main theme of the present
note. It would be natural to consider the supremum of the order-types
of well-ordered linear extensions of the restriction ď0
ˆ of ďˆ to Ś0
iăω αi.
However, just considering Ś0
iăω 2, we see that pŚ0
iăω 2, ď0
ˆq has linear
extensions which are not well-ordered. Indeed, for every j ă ω, let
bj P Ś0
iăω 2 be deﬁned by bj
j “ 1 and bj
i “ 0 if i ‰ j. Then the bj’s
form a countable set of pairwise ď0
ˆ-incomparable elements of Ś0
iăω 2,
hence every countable linear order is isomorphic to a subset of some
linear extension of Ś0
iăω 2 (e. g., by [Har, Theorem 3.3]). Even if we
restrict ourselves to well-ordered extensions of Ś0
iăω 2, we get from
the above considerations that the supremum of their order-types is ω1,
hence this supremum is not a maximum and anyway it is too large to
have the intended meaning, that is, ω “ Â
iăω 2.
The situation is parallel to [L1] and, as in [L1], an order-theoretical
characterization can be found provided we restrict ourselves to linear
extensions satisfying some ﬁniteness condition.
3.5.
We need a bit more notation in order to state the next theorem.
Recall that if pαiqiăω is a sequence of ordinals, then Ś0
iăω αi is the
set of the sequences with ﬁnite support and the (partial) order ď0
ˆ is
deﬁned componentwise. If a, b P Ś0
iăω αi and a ‰ b, let diffpa, bq be
the largest element i of supppaq Y supppbq such that ai ‰ bi. Thus (*)
above introduces a linear order ăL on Ś0
iăω αi deﬁned by a ăL b if and
only if ai ă bi, for i “ diffpa, bq (here ă is the standard order on αi,
hence there is no need to explicitly indicate the index). By the results
recalled in Subsection 3.2, the above order ăL has type ś
iăω αi. On
the other hand, in the ﬁnite case, by Carruth theorem mentioned in
3.3, Â
iăn αi is the order-type of the largest linear extension of ďˆ on
Ś
iăn αi “ Ś0
iăn αi. We show that in the inﬁnite case Â
iăω αi can be
evaluated by combining the above constructions.
If a P Ś
iăω αi is a sequence and n ă ω, let aæn be the restriction
of a to n, that is, aæn is the element of Ś
iăn αi deﬁned as follows. If
a “ paiqiăω, then aæn “ paiqiăn. Here, as usual, we adopt the convention
n “ t0, 1, . . . , n ´ 1u.


## Page 12


12
PAOLO LIPPARINI
Let us say that a linear order ă1 on Ś0
iăω αi is ﬁnitely Carruth if ă1
extends ă0
ˆ and there are an n ă ω and an order ď2 extending ăˆ on
Ś
iăn αi and such that if a ‰ b P Ś0
iăω αi and i “ diffpa, bq, then
(1) if i ě n, then a ă1 b if and only if ai ă bi, and
(2) if i ă n, then a ă1 b if and only if aæn ă2 aæn.
A linear order ă1 on Ś0
iăω αi is locally ﬁnitely Carruth if ă1 extends
ă0
ˆ and, for every c P Ś0
iăω αi, there is n “ nc ă ω such that, for every
a ‰ b P Ś0
iăω αi, if a, b ă1 c and i “ diffpa, bq ě n, then a ă1 b if and
only if ai ă bi. In other words, for every c, (1) above holds, restricted
to those pairs of elements a, b which are ă1 c, while no version of (2) is
assumed.
Theorem 3.1. If pαiqiăω is a sequence of ordinals, then Â
iăω αi is the
order-type of some ﬁnitely Carruth linear order on Ś0
iăω αi.
Every (locally) ﬁnitely Carruth linear order on Ś0
iăω αi is a well-
order; moreover, Â
iăω αi is the largest order-type of all such orderings.
Proof. By Corollary 2.10, in particular, equation (6), there is some
m ă ω such that Â
iăω αi “ pα0 b ¨ ¨ ¨ b αm´1q ¨ ś
mďiăω αi. By Car-
ruth theorem, there is some linear extension ďC of ďˆ on Ś
iăm αi
such that P0 “ pŚ
iăm αi, ďCq has order-type Â
iăm αi. By the re-
sults recalled in Subsection 3.2, ś
mďiăω αi is the order-type of P1 “
pŚ0
mďiăω αi, ďLq. Then P “ L˚
hă2 Ph has order-type pα0 b¨ ¨ ¨bαm´1q¨
ś
mďiăω αi “ Â
iăω αi, since, as we mentioned, for two ordinals γ0
and γ1 the order-type of L˚
iă2 γi is γ0γ1. Through the canonical bi-
jection between Ś0
iăω αi and Ś
iăm αi ˆ Ś0
mďiăω αi, the order ă1 we
have constructed on L˚
iă2Pi is clearly ﬁnitely Carruth. Indeed, in the
deﬁnition of ﬁnitely Carruth, take n “ m and take ď2 as ďC.
If
i “ diffpa, bq ă m, then the ordering between a and b is determined
by their æm part, since sequences with the same P1-component are or-
dered according to their P0 component. Hence (2) holds. On the other
hand, if i “ diffpa, bq ě m, then ai ă bi if and only if a ă1 b, by the
deﬁnition of ďL, thus (1) holds. Obviously, ă1 extends ăˆ, since both
ďC and ďL extend ďˆ on their respective components. Hence Â
iăω αi
can be realized as the order-type of some ﬁnitely Carruth order on
Ś0
iăω αi and the ﬁrst statement is proved.
Since every ﬁnitely Carruth order on Ś0
iăω αi is obviously locally
ﬁnitely Carruth, it is enough to prove that every locally ﬁnitely Carruth
order on Ś0
iăω αi is a well-order of type ď Â
iăω αi. So let us assume
from now on that ă1 is locally ﬁnitely Carruth.


## Page 13


AN INFINITE NATURAL PRODUCT
13
Claim. If c P Ś0
iăω αi and C “ ta P Ś0
iăω αi | a ă1 cu, then pC, ă1
æCq
is a well-ordered set of type ď Â
iăω αi.
Proof. Let n “ nc be given by local Carruth ﬁniteness and, as above,
let P1 “ pŚ0
nďiăω αi, ďLq. Notice that, by Subsection 3.2, P1 is well-
ordered and has type ś
nďiăω αi. If a P Ś0
iăω αi, say, a “ paiqiăω, recall
that aæn is the element paiqiăn of Ś
iăn αi. Similarly, let aěn be the
element paiqiěn of Ś0
iěn αi. Thus the position a ÞÑ paæn, aěnq gives the
canonical bijection (mentioned but not described above) from Ś0
iăω αi
to Ś
iăn αiˆŚ0
nďiăω αi. If P “ td P Ś0
nďiăω αi | d “ aěn, for some a P
Ś0
iăω αi such that a ă1 cu, then P Ď P1 hence P as a suborder of P1
inherits a well-order of type ď ś
nďiăω αi. Moreover, by local Carruth
ﬁniteness, if a, b ă1 c and aěn ăL běn, then a ă1 b.
If d P P, let
Qd “ taæn | a P Ś0
iăω αi, a ă1 c and aěn “ du. Then, for every d P P,
the order ă1 induces an order ăd on Qd by letting aæn ăd bæn if and
only if a ă1 b (notice that, since we are assuming a, b P Qd, then a and
b have the same ě n components). Since, by assumption, ă1 extends
ăˆ on Ś0
iăω αi, then ăd extends the restriction of ăˆ on Ś
iăn αi to
Qd. Hence, by Carruth theorem, for every d P P we have that pQd, ădq
is well-ordered and has type ď Â
iăn αi.
The above considerations show that pC, ă1
æCq is isomorphic to the
lexicographical product LdPP Qd (recall that if a, b ă1 c and aěn ăL běn,
then a ă1 b).
Since, as we showed, P is a well-ordered set of type
ď ś
nďiăω αi and each Qd is a well-ordered set of type ď Â
iăn αi, then
pC, ă1
æCq is a well-ordered set of order-type ď Â
iăn αi ¨ ś
nďiăω αi.
If the m given by Corollary 2.10 is ď n, then we immediately get
from equation (6) that pC, ă1
æCq has order-type ď Â
iăω αi. Otherwise,
notice that if the condition for local Carruth ﬁniteness is satisﬁed for c
and for some nc, then the condition is satisﬁed for any n1 ě nc in place
of nc, hence it is no loss of generality to suppose that the m given by
Corollary 2.10 is ď n and we are done as before.
lClaim
To complete the proof of the theorem, we have from the Claim that,
for every c P Ś0
iăω αi, the set of the ă1-predecessors of c is well-ordered;
this implies that ă1 is a well-order.
It remains to show that ă1 has order-type ď Â
iăω αi. This is vac-
uously true if some αi is 0 and it follows from Carruth theorem if the
αi’s are eventually 1. Otherwise, local Carruth ﬁniteness implies that
ă1 has no maximum. Indeed, if a P Ś0
iăω αi, then there is k ă ω such
that ai “ 0, for i ą k. Since the sequence of the αi’s is not eventually 1
and no αi is 0, there is ¯ı ą k such that α¯ı ą 1. If b is equal to a on each
component, except that b¯ı “ 1, then a ăˆ b, hence a ă1 b, since, by


## Page 14


14
PAOLO LIPPARINI
assumption, ă1 extends ăˆ. Since a above has been chosen arbitrarily,
we get that ă1 has no maximum. Then the Claim implies that ă1 has
order-type ď Â
iăω αi.
□
Remark 3.2. For the sake of simplicity, we have limited our study here
to sequences of length ω. However, essentially all the results here admit
a reformulation for the case of ordinal-indexed transﬁnite sequences
of arbitrary length, modulo the case of the transﬁnite natural sums
studied in [L2]. It should be remarked that there are diﬀerent ways
to extend the natural sums and products to sequences of length ą ω.
See [L2, Section 5], in particular, Deﬁnitions 5.2 and Problems 5.6. We
just give here the relevant deﬁnitions relative to transﬁnite products.
Suppose that pαγqγă¯ε is a sequence of ordinals. The iterated natural
product ś#
γăδ αγ is deﬁned for every δ ď ¯ε as follows.
#
ź
γă0
αγ “ 1;
#
ź
γăδ`1
αγ “
˜ #
ź
γăδ
αγ
¸
b αδ
#
ź
γăδ
αγ “ lim
δ1ăδ
#
ź
γăδ1
αγ
for δ limit
Moreover, we set
âo
γăδ
αγ “ inf
π
#
ź
γăδ
απpγq
where π varies among all the permutations of δ. In the above deﬁnition
we are keeping δ ﬁxed. In the next deﬁnition, on the contrary, we let
the ordinal δ vary. Suppose that I is any set and pαiqiPI is a sequence
of ordinals. Deﬁne
â1
iPI
αi “ inf
δ,f
#
ź
γăδ
αfpγq
where δ varies among all the ordinals having cardinality |I| and f varies
among all the bijections from δ to I. Furthermore, let λ “ |I| and deﬁne
â‚
iPI
αi “ inf
f
#
ź
γăλ
αfpγq
where f varies among all the bijections from λ to I.
Acknowledgement. We thank an anonymous referee of [L1] for many in-
teresting suggestions concerning the relationship between natural sums


## Page 15


AN INFINITE NATURAL PRODUCT
15
and the theory of well-quasi-orders. We thank Harry Altman for stim-
ulating discussions. We thank Arnold W. Miller for letting us know of
Toulmin paper [T] in the MR review of [L1].
The literature on the subject of ordinal operations is so vast and
sparse that we cannot claim completeness of the following list of refer-
ences.
It is not intended that each work in the list has given equally signiﬁcant contributions to
the discipline. Henceforth the author disagrees with the use of the list (even in aggregate
forms in combination with similar lists) in order to determine rankings or other indicators
of, e. g., journals, individuals or institutions. In particular, the author considers that it
is highly inappropriate, and strongly discourages, the use (even in partial, preliminary or
auxiliary forms) of indicators extracted from the list in decisions about individuals (espe-
cially, job opportunities, career progressions etc.), attributions of funds, and selections or
evaluations of research projects.
References
[A]
H.
Altman,
Intermediate
arithmetic
operations
on
ordinal
numbers,
arXiv:1501.05747.
[B]
H. Bachmann, Transﬁnite Zahlen, Zweite, neubearbeitete Auﬂage, Ergebnisse
der Mathematik und ihrer Grenzgebiete, Band 1, Berlin-New York, 1967.
[Ca]
P. W. Carruth, Arithmetic of ordinals with applications to the theory of or-
dered Abelian groups, Bull. Amer. Math. Soc. 48 (1942), 262–271.
[Co]
J. H. Conway, On numbers and games, London Mathematical Society Mono-
graphs No. 6., 1976 (Second Edition, 2001).
[E]
P. Ehrlich, The rise of non-Archimedean mathematics and the roots of a
misconception. I: The emergence of non-Archimedean systems of magnitudes,
Arch. Hist. Exact Sci. 60 (2006), 1–121.
[Har] E. Harzheim, Ordered sets, Advances in Mathematics 7, New York, 2005.
[Hau] F. Hausdorﬀ, Mengenlehre, Berlin, 1927.
[dJP] D. H. J. de Jongh, R. Parikh, Well-partial orderings and hierarchies, Nederl.
Akad. Wetensch. Proc. Ser. A 80 = Indag. Math. 39 (1977), 195–207.
[L1]
P. Lipparini, An inﬁnite natural sum, Math. Log. Quart. 62 (2016), 1–12.
[L2]
P. Lipparini, Some transﬁnite natural sums, arXiv:1509.04078v2 (2016), 1–
29.
[Ma]
K. Matsuzaka, On the deﬁnition of the product of ordinal numbers (Japan-
ese), Sˆugaku, 8, 95–96 (1956/57).
[Mi]
E. C. Milner, Basic wqo- and bqo-theory, in Graphs and order (Banﬀ, Alta.,
1984) 487–502, NATO Adv. Sci. Inst. Ser. C Math. Phys. Sci., 147, Dor-
drecht, 1985.
[S1]
W. Sierpi´nski, Sur les s´eries inﬁnies de nombres ordinaux, Fund. Math. 36
(1949), 248–253.
[S2]
W. Sierpi´nski, Sur les produits inﬁnis de nombres ordinaux, Soc. Sci. Lett.
Varsovie. C. R. Cl. III. Sci. Math. Phys. 43 (1950), 20–24.
[S3]
W. Sierpi´nski, Cardinal and ordinal numbers. Second revised edition, Mono-
graﬁe Matematyczne, Vol. 34, Panstowe Wydawnictwo Naukowe, Warsaw
1965.


## Page 16


16
PAOLO LIPPARINI
[T]
G. H. Toulmin, Shuﬄing ordinals and transﬁnite dimension, Proc. London
Math. Soc. 4 (1954). 177–195.
[VW] J. V¨a¨an¨anen, T. Wang, An Ehrenfeucht-Fra¨ıss´e game for Lω1ω, MLQ Math.
Log. Q. 59 (2013), 357–370.
[W]
T. Wang, An Ehrenfeucht-Fra¨ıss´e game for Lω1ω, MSc Thesis, Universiteit
van Amsterdam, 2012.
[Wo]
E. S. Wolk, Partially well ordered sets and partial ordinals, Fund. Math. 60
(1967) 175–186.
Dipartimento Produttivo di Matematica, Viale della Ricerca Scien-
tifica, Universit`a di Roma “Tor Vergata”, I-00133 ROME ITALY
URL: http://www.mat.uniroma2.it/~lipparin

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1703_06908v2_an_infinite_natural_product
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1703_06908V2_AN_INFINITE_NATURAL_PRODUCT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
