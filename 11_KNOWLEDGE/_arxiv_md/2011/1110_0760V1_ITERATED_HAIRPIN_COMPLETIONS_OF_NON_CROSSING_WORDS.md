---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1110.0760v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1110.0760v1_Iterated_Hairpin_Completions_of_Non-crossing_Words

> Source: 1110.0760v1_Iterated_Hairpin_Completions_of_Non-crossing_Words.pdf

> Pages: 15

---


## Page 1


arXiv:1110.0760v1  [cs.FL]  4 Oct 2011
Iterated Hairpin Completions of Non-crossing
Words ∗
Lila Kari
Steﬀen Kopecki
Shinnosuke Seki
November 11, 2018
Abstract
Iterated hairpin completion is an operation on formal languages that is
inspired by the hairpin formation in DNA biochemistry. Iterated hairpin
completion of a word (or more precisely a singleton language) is always
a context-sensitive language and for some words it is known to be non-
context-free. However, it is unknown whether regularity of iterated hair-
pin completion of a given word is decidable. Also the question whether
iterated hairpin completion of a word can be context-free but not regu-
lar was asked in literature. In this paper we investigate iterated hairpin
completions of non-crossing words and, within this setting, we are able
to answer both questions. For non-crossing words we prove that the reg-
ularity of iterated hairpin completions is decidable and that if iterated
hairpin completion of a non-crossing word is not regular, then it is not
context-free either.
1
Introduction
On an abstract level, a DNA single strand can be viewed as a word over the four-
letter alphabet {A, C, G, T} where the letters represent the nucleobases adenine,
cytosine, guanine, and thymine, respectively. The Watson-Crick complement of
A is T and the complement of C is G. Two complementary single strands of
opposite orientation can bond to each other and form a DNA double strand.
Throughout the paper, we use the bar-notation for complementary strands of
opposite orientation.
In the same manner, a single strand can bond to itself if two of its substrands
are complementary and do not overlap with each other. Such an intramolecular
base pairing is called a hairpin. We are especially interested in hairpins of single
strands of the form σ = γαβα. Here, the substrand α can bond to the substrand
α. Then, by extension, a new single strand can be synthesized which we call a
hairpin completion of σ, see Figure 1. In this situation we call the substrands
that initiate the hairpin completion, α and α, primers.
In DNA computing hairpins and hairpin completions are often undesired
by-products. Therefore, sets of strands have been analyzed and designed that
∗This research was supported by the Natural Sciences and Engineering Research Council
of Canada Discovery Grant R2824A01 and Canada Research Chair Award to L. K., and by
the Funding Program for Next Generation World-Leading Researchers (NEXT Program) to
Yasushi Okuno, the current supervisor of S. S.
1


## Page 2


γ
α
β
α
γ
α
β
α
γ
γ
α
β
α
γ
annealing
denaturation
extension
Figure 1: Hairpin completion of a DNA single strand
are unlikely to form hairpins or lead to other undesireable hybridization, see
[1,2,7,8,10,18] and the references within.
However, there are DNA computational models that rely on hairpins, e. g.,
DNA RAM [9, 20, 21] and Whiplash PCR [5, 19, 22]. For the Whiplash PCR
consider a single strand just like in Figure 1, but where the length of extension
is controlled by stopper sequences. Repeating this operation, DNA can be used
to solve combinatorial problems like the Hamiltonian path problem.
Inspired by hairpins in biocomputing, the hairpin completion of a formal
language has been introduced by Cheptea, Mart´ın-Vide, and Mitrana in [3]. In
several papers hairpin completion and its iterated variant have been investi-
gated, see [4,12–17]. In this paper we consider iterated hairpin completions of
singletons, that is, informally speaking, iterated hairpin completions of words.
The class of iterated hairpin completions of singletons is denoted by HCS. It
is known that every language in HCS is decidable in NL (non-deterministic,
logarithmic space) as NL is closed under iterated hairpin completion [3]; hence,
HCS is a proper subclass of the context-sensitive languages. It is also known
that HCS contains regular as well as non-context-free languages [12]. In the
latter paper, two open problems have been stated:
1. Is it decidable whether the iterated hairpin completion of a singleton is
regular?
2. Does a singleton exist whose iterated hairpin completion is context-free
but not regular?
We solve both questions for non-crossing words (or rather, singletons con-
taining a non-crossing word).
A word w is said to be non-crossing if, for a
given primer α, the right-most occurrence of the factor α in w precedes the
left-most occurrence of the factor α in w, see Section 3. We provide a necessary
and suﬃcient condition for regularity of iterated hairpin completion of a given
non-crossing word (Theorem 4.6 and Corollary 4.9) and, since this condition is
decidable, we answer the ﬁrst question positively (Corollary 4.10). Furthermore,
we show that iterated hairpin completion of a non-crossing word is either reg-
ular or it is not context-free (Corollary 4.11). Thus, we give a negative answer
to the second question.
This paper is the continuation of the studies in [11].
2


## Page 3


2
Preliminaries
We assume the reader to be familiar with the fundamental concepts of language
theory, see [6].
Let Σ be an alphabet, Σ∗be the set of all words over Σ, and for an integer
k ≥0, Σk be the set of all words of length k over Σ. The word of length 0 is
called the empty word, denoted by ε, and we let Σ+ = Σ∗\ {ε}. A subset of
Σ∗is called a language over Σ. For a word w ∈Σ∗, we employ the notation w
when we mean the word as well as the singleton language {w} unless confusion
arises.
We equip Σ with a function
: Σ →Σ satisfying ∀a ∈Σ, a = a; such a
function is called an involution.
This involution
is naturally extended to
words as: for a1, . . . , an ∈Σ, a1a2 · · · an = an · · · a2a1. For a word w ∈Σ∗,
we call w the complement of w, being inspired by this application. A word
w ∈Σ∗is called a pseudo-palindrome if w = w. For a language L ⊆Σ∗, we let
L = {w | w ∈L}.
For words u, w ∈Σ∗, if w = xuy holds for some words x, y ∈Σ∗, then u is
called a factor of w; a factor that is distinct from w is said to be proper. If the
equation holds with x = ε (y = ε), then the factor u is especially called a preﬁx
(resp. a suﬃx) of w. The preﬁx relation can be regarded as a partial order ≤p
over Σ∗whereas the proper preﬁx relation can be regarded as a strict order <p
over Σ∗; u ≤p w means that u is a preﬁx of w and u <p w means that u is a
proper preﬁx of w. Analogously, by w ≥s u (or w >s u) we mean that u is a
suﬃx (resp. proper suﬃx) of w. Note that u ≤p w if and only if w ≥s u. For a
word w ∈Σ∗and a language L ⊆Σ∗, a factor u of w is minimal with respect to
L if u ∈L and none of the proper factors of u is in L.
2.1
Hairpin Completion
Let k be a constant that is assumed to be the length of a primer and let α ∈
Σk be a primer. If a given word w ∈Σ∗can be written as γαβα for some
γ, β ∈Σ∗, then its right hairpin completion (with respect to α) results in the
word γαβαγ. By w →RHα z, we mean that z can be obtained from w by right
hairpin completion (with respect to α). The left hairpin completion is deﬁned
analogously as an operation to derive γαβαγ from αβαγ, and the relation →LHα
is naturally introduced. We write w →Hα z if w →RHα z or w →LHα z. By
→∗
LHα, →∗
RHα, and →∗
Hα we denote the reﬂexive and transitive closure of →LHα,
→RHα, and →Hα, respectively. Whenever α is clear from the context, we omit
the subscript α and write →RH, →LH, or →H, respectively.
For a language L ⊆Σ∗, we deﬁne the set of words obtained by hairpin
completion from L, and the set of words obtained by iterated hairpin completion
from L, respectively, as follows:
Hα(L) = {z | ∃w ∈L, w →Hα z} ,
H∗
α(L) =

z
 ∃w ∈L, w →∗
Hα z
	
.
In this paper the hairpin completion is always considered with respect to
a ﬁxed primer α. However, in other literature the hairpin completion is often
considered with respect to the length k of primers instead of a speciﬁc primer
3


## Page 4


α and deﬁned as
Hk(L) =
[
α∈Σk
Hα(L),
H∗
k(L) =
[
i≥0
Hi
k(L).
3
Non-crossing Words and Their Properties
In this section, we describe some structural properties of non-crossing words and
their iterated hairpin completions and we introduce the notation of α-preﬁxes,
α-suﬃxes, and α-indexes.
For a word α, we say that w is non-α-crossing if the rightmost occurrence of
α precedes the leftmost occurrence of α on w (yet these factors may overlap).
If α is understood from the context, we simply say that w is non-crossing.
Otherwise, the word is α-crossing or crossing. The deﬁnition of a word w being
non-α-crossing becomes useful in our work only if w ∈αΣ∗or w ∈Σ∗α, and
therefore, α and α are primers; actually, we will assume both. The main purpose
of this paper is to prove a necessary and suﬃcient condition for the regularity of
the iterated hairpin completion H∗
α(w), where w ∈αΣ∗∩Σ∗α is non-α-crossing.
Note that if w ∈αΣ∗∩Σ∗α and α = α, then either w = α and H∗
α(w) = {w}
or w can be considered crossing.
Thus, whenever we consider non-crossing
words, we assume that α ̸= α.
Any word obtained from a non-crossing word by hairpin completion is non-
crossing. Though being easily conﬁrmed, this closure property forms the foun-
dation of our discussions in this paper.
Proposition 3.1. For a non-crossing word w ∈αΣ∗∩Σ∗α, every word in
H∗
α(w) is non-crossing.
Let us provide another characterization for a word w ∈αΣ∗∩Σ∗α to be
non-crossing. With Proposition 3.1, this characterization will bring a unique
factorization of any word z in H∗
α(w) as z = xwy for some words x, y (Corol-
lary 3.3).
Proposition 3.2. A word w ∈αΣ∗∩Σ∗α is non-crossing if and only if it
contains exactly one factor x which is minimal with respect to αΣ∗∩Σ∗α.
Proof. The word w contains at least one factor from αΣ∗∩Σ∗α and hence it
contains at least one minimal factor, too.
Suppose w contains exactly one minimal factor x from αΣ∗∩Σ∗α. If the
preﬁx α of x was proceeded in w by another factor α, then this factor is again
proceeded by α and we would ﬁnd a second minimal factor x′ ∈αΣ∗∩Σ∗α.
Hence, the preﬁx of x is the rightmost occurrence of α in w and, symmetrically,
the suﬃx of x is the leftmost occurrence of α in w. As the rightmost occurrence
of α precedes the leftmost occurrence of α, the word w is non-crossing.
Now suppose w contains at least two minimal factors x1, x2 from αΣ∗∩Σ∗α.
If these factors overlap and the overlapped part is of length at least k, we may
assume x1 = y1y2 and x2 = y2y3 for words y1, y2, y3 ∈Σ+ where y2, the
overlapping part, is at least k. We see that y2 ∈αΣ∗∩Σ∗α and that x1, x2 were
not minimal with respect to αΣ∗∩Σ∗α. Therefore, x1, x2 overlap in less than
k letters (or do not overlap at all) and w can be considered crossing.
Corollary 3.3. Let w ∈αΣ∗∩Σ∗α be non-crossing.
The factor w occurs
exactly once in every word from H∗
α(w).
4


## Page 5


3.1
α-Preﬁxes and α-Suﬃxes
Let u, v, w be words. We call u an α-preﬁx of w if uα ≤p w. This means, if α
is a suﬃx of w, then the suﬃx can bond to the factor α which directly follows
the preﬁx u (unless they overlap with each other) and wu can be obtained from
w by right hairpin completion. By Pα(w), we denote the set of all α-preﬁxes of
w. Note that if x, y ∈Pα(w) and |x| ≤|y|, then xα ≤p yα and x ∈Pα(yα).
Symmetrically, we call v an α-suﬃx if w ≥s αv and Sα(w) is the set of all
α-suﬃxes of w. If α ≤p w and |w| ≥|v| + 2k, then w →LH vw. Note that
Sα(w) = Pα(w). Therefore, all results we derive for α-preﬁxes also hold for the
complements of α-suﬃxes.
When m = |Pα(w)| and n = |Sα(w)| for a word w, then w is called (m, n)-
α-word (or simply (m, n)-word). Throughout the paper, it will be convenient
to let Pα(w) = {u0, . . . , um−1} and Sα(w) = {v0, . . . , vn−1} where the words
are ordered such that u0 <p · · · <p um−1 and vn−1 >s · · · >s v0. Note that
Pα(uiα) = {u0, . . . , ui} for 0 ≤i < m and Sα(αvj) = {v0, . . . , vj} for 0 ≤j < n.
Let us begin with a basic observation.
Lemma 3.4. For a word w ∈αΣ∗∩Σ∗α, the following statements hold:
1. For every x ∈Pα(w) ∪Sα(w), we have α ≤p xα.
2. For every x1, . . . , xℓ∈Pα(w) ∪Sα(w), we have α ≤p xℓ· · · x1α.
Proof. If x ∈Pα(w), the ﬁrst statement derives directly from the deﬁnition. If
x ∈Sα(w), then α is a suﬃx of αx, whence α ≤p xα.
The second statement follows by induction on ℓand the ﬁrst statement.
Consider w ∈αΣ∗∩Σ∗α. Note that this means u0 = v0 = ε. It is easy to
see that every word z which belongs to Hα(w) has a factorization z = wu for
some u ∈Pα(w) or z = vw for some v ∈Sα(w). By the previous lemma we see
that z ∈αΣ∗∩Σ∗α and by induction H∗
α(w) ⊆αΣ∗∩Σ∗α.
The next lemma tells if w ∈αΣ∗∩Σ∗α is a non-crossing (m, n)-word with
n ≥2, then the suﬃx α does not overlap with any of the factors α and, therefore,
w →RH wu for all u ∈Pα(w).
Lemma 3.5. Let w ∈αΣ∗∩Σ∗α be a non-crossing (m, n)-word with n ≥2 and
let um−1 be the longest α-preﬁx in Pα(w). Then |um−1| + 2k ≤|w| holds.
Proof. Let Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1 and Sα(w) =
{v0, . . . , vn−1} such that vn−1 >s · · · >s v0 as usual. Suppose that the inequality
|um−1| + |vn−2| + 2k ≤|w| did not hold (note that this inequality is stronger
than the one proposed in our claim). Being non-crossing, w can be written as
w = um−1xvn−2 for some word x ∈αΣ∗∩Σ∗α with |x| ≤2k. Hence x = x.
Let y be the nonempty word satisfying vm−1 = yvm−2. Since w is non-crossing,
xvn−2 ≥s vn−1 must hold, from which we have x ≥s αy. Combining this with
x = x enables us to ﬁnd an α-preﬁx um−1y of w, but this would be longer than
the longest α-preﬁx of w — a contradiction.
Since the analogous argument is valid for left hairpin completion, Lemma 3.5
leads us to one important corollary on non-crossing (m, n)-words for m, n ≥2.
5


## Page 6


Corollary 3.6. Let w ∈αΣ∗∩Σ∗α be a non-crossing (m, n)-word with m, n ≥2.
Hα(w) = {w} ∪wPα(w) ∪Sα(w)w.
Next, we concern the case when there is a preﬁx u ∈Pα(w) and a suﬃx
v ∈Sα(w) such that v ∈Pα(uα)∗and u ∈Sα(αv)∗.
Lemma 3.7. Let w ∈αΣ∗∩Σ∗α be an (m, n)-word.
For u ∈Pα(w) and
v ∈Sα(w),
1. if v ∈Pα(uα)∗, then Sα(αv) ⊆Pα(uα)∗.
2. if v ∈Pα(uα)∗and u ∈Sα(αv)∗, then Pα(uα)∗= Sα(αv)∗.
Proof. Let Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1 and Sα(w) =
{v0, . . . , vn−1} such that vn−1 >s · · · >s v0. We may assume u = us for some
0 ≤s < m. Recall that Pα(uα) = {u0, . . . , us}.
For the ﬁrst statement, let v = x1 · · · xℓwhere x1, . . . , xℓ∈{u0, . . . , us}. For
0 ≤j ≤t we have vjα ≤vα, hence, there is 1 ≤i ≤ℓsuch that vj = x1 · · · xi−1y
where y ≤p xi and yα ≤p xi · · · xℓα. By Lemma 3.4, we see that yα ≤p xiα ≤p w
and hence y ∈{u1, . . . , us}. Therefore, vj ∈{u1, . . . , us}∗.
The second statement follows immediately by the symmetry between preﬁxes
and complemented suﬃxes.
Lemma 4.3 and Corollary 4.4 in in Section 4 will describe the consequences
for the iterated hairpin completion of a non-crossing word w, if we ﬁnd such a
situation.
3.2
The α-Index
The α-index of a word x is the number of occurrences of the factor α in the
word xα except for the suﬃx. Formally, we deﬁne a function indα : Σ∗→N as
indα(x) = |Pα(xα)| −1.
Recall that Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1. Note
that, by this ordering, for all 0 ≤i < m we have indα(ui) = i and if x ∈Pα(w),
then x = uindα(x). Symmetrically, if x ∈Sα(w), then x = vindα(x).
Also note that for words x, y with indα(x) > indα(y) the word x cannot
be a factor of y as the positions of the factors α cannot match. Later we will
consider the α-indices of words from αΣ∗α−1 (Note that x ∈αΣ∗α−1 if and only
if α ≤p xα). If x ∈αΣ∗α−1 and y ∈Σ∗, then indα(yx) = indα(y) + indα(x).
These observations lead to the following properties.
Lemma 3.8. Let Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1, let
x ∈αΣ∗α−1, and let 0 ≤j < m. If x is a suﬃx of uj, then uj = uj−indα(x)x.
In particular, if w ∈αΣ∗and uj ≥s ui for 0 ≤i ≤j < m, then uj = uj−iui.
Proof. Let y such that uj = yx.
As α ≤p xα, we have yα ≤p ujα ≤p w,
and hence, y ∈Pα(w). As indα(y) = indα(uj) −indα(x), it follows that y =
uj−indα(x).
6


## Page 7


Lemma 3.9. Let Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1, let
1 ≤i < m, and let x be a word with indα(x) ≤i.
x ∈{u1, . . . , ui}∗
⇐⇒
x ∈

u1, . . . , uindα(x)
	∗.
Proof. The implication from right to left is plain.
Conversely, let x = y1 · · · yℓwith y1, . . . , yℓ∈{u1, . . . , ui}. As indα(x) ≥
indα(yj) for all 1 ≤j ≤ℓ, we see that, actually, y1, . . . , yℓ∈

u1, . . . , uindα(x)
	
.
Hence, x ∈

u1, . . . , uindα(x)
	∗, as desired.
4
Iterated Hairpin Completion of Non-crossing
Words
Now we are prepared to prove a necessary and suﬃcient condition for the reg-
ularity of H∗
α(w), where w ∈αΣ∗∩Σ∗α is a non-crossing (m, n)-word with
Pα(w) = {u0, . . . , um−1} and Sα(w) = {v0, . . . , vn−1} which are ordered as in
the previous section. (Keep in mind that u0 = v0 = ε.) By a result from [11] it
is enough to consider the case where m, n ≥2 and in this case, by Corollary 3.6,
Hα(w) = {w} ∪w {u1, . . . , um−1} ∪{v1, . . . , vn−1} w.
Theorem 4.1 (See [11]). If w ∈αΣ∗∩Σ∗α is a non-crossing (m, n)-word with
m = 1 or n = 1, then H∗
α(w) is regular.
The next two lemmas lead to a ﬁrst suﬃcient condition for the regularity of
H∗
α(w), see Corollary 4.4.
Lemma 4.2. For non-crossing w ∈αΣ∗∩Σ∗α,
H∗
α(w) ⊆

Pα(w) ∪Sα(w)
∗
w

Pα(w) ∪Sα(w)
∗
.
Proof. For every word z ∈H∗
α(w), by deﬁnition, we ﬁnd a series of words
w = w0, w1, . . . , wℓ= z for some ℓ≥0 such that
w0 →H w1 →H · · · →H wℓ.
We prove z = wℓ∈
 Pα(w)∪Sα(w)
∗w
 Pα(w)∪Sα(w)
∗by induction on ℓ. For
ℓ= 0 this is plain. Now we assume that any word which can be derived from w
by at most ℓ−1 hairpin completions is in this set. By induction hypothesis,
wℓ−1 = xs · · · x1wy1 · · · yt
for some s, t ≥0 and x1, . . . , xs, y1, . . . , ys ∈Pα(w)∪Sα(w). Hence, Pα(wℓ−1) ⊆
 Pα(w)∪Sα(w)
∗and Sα(wℓ−1) ⊆
 Pα(w)∪Sα(w)
∗. This proves our claim.
Lemma 4.3. Let w ∈αΣ∗∩Σ∗α be non-crossing. If for some u ∈Pα(w) and
v ∈Sα(w) we have v ∈Pα(uα)∗and u ∈Sα(αv)∗, then
Pα(uα)∗wPα(uα)∗= Sα(αv)∗wSα(αv)∗⊆H∗
α(w).
7


## Page 8


Proof. Let Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1 and Sα(w) =
{v0, . . . , vn−1} such that vn−1 >s · · · >s v0.
First we prove that for the special case when u = v, Pα(uα)∗wPα(uα)∗⊆
H∗
α(w). Afterwards, we will use this fact in order to prove our claim.
Suppose u = v ∈Pα(w) ∩Sα(w) and let ℓ= indα(u). This implies ui = vi
for all 0 ≤i ≤ℓ. Let
z = xs · · · x1wy1 · · · yt
where s, t ≥0 and x1, . . . , xs, y1, . . . , yt ∈{u0, . . . , uℓ} = Pα(uα). Let s′ and t′
be maximal such that indα(xs′) = ℓand indα(yt′) = ℓ; or 0 if no such index
exists. We let w′ = xs′ · · · x1wy1 · · · yt′. Note that αuℓis a suﬃx of w′ and
hence
w →∗
RH wy1 · · · yt′ →∗
LH xs′ · · · x1wy1 · · · yt′ = w′.
We have w′ ∈H∗
α(w) and z ∈{u0, . . . , uℓ−1}∗w′ {u0, . . . , uℓ−1}∗. We may
continue inductively and conclude z ∈H∗
α(w).
Now let v ∈Pα(uα)∗and u ∈Sα(αv)∗as in the claim and let ℓ≤indα(u)
be the minimal index such that v ∈{u0, . . . , uℓ}∗. Note that
Pα(uα)∗= Sα(αv)∗= {u0, . . . , uℓ}∗,
by Lemma 3.7. The minimality of ℓyields uℓ/∈{u0, . . . , uℓ−1}∗and uℓis a
factor of v, which means that ℓ≤indα(v) < n. We claim that uℓ= vℓ. Indeed,
if we had uℓ̸= vℓ, then uℓ∈{v0, . . . , vℓ−1}∗⊆{u0, . . . , uℓ−1}∗(see Lemma 3.9).
As uℓ= vℓ, our observations made for the special case apply and we may
conclude
Pα(uℓα)∗wPα(uℓα)∗= Pα(uα)∗wPα(uα)∗= Sα(αv)∗wSα(αv)∗⊆H∗
α(w).
Suppose that the longest α-preﬁx um−1 belongs to Sα(w)∗and the longest
α-suﬃx vn−1 belongs to Pα(w)∗. By Lemma 3.7, we see that Pα(w)∗= Sα(w)∗
and, by Lemmas 4.2 and 4.3, we infer H∗
α(w) = Pα(w)∗wPα(w)∗. (Note that
Pα(w) = Pα(um−1α).)
Corollary 4.4. Let w ∈αΣ∗∩Σ∗α be non-crossing, let um−1 be the longest
α-preﬁx of w, and let vn−1 be the longest α-suﬃx of w. If um−1 ∈Sα(w)∗and
vn−1 ∈Pα(w)∗, then H∗
α(w) is regular.
Our next result, Theorem 4.6, shows that if we can state a necessary and
suﬃcient condition for the special case where u1 = v1, then we can extend this
condition to the general case. We need a preliminary lemma in order to prove
Theorem 4.6.
Lemma 4.5. Let w ∈αΣ∗∩Σ∗α be a non-crossing (m, n)-word with m, n ≥2,
let Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1, and let Sα(w) =
{v0, . . . , vv−1} such that vn−1 >s · · · >s v0.
1. If u1 = v1, then H∗
α(w) ⊆u1αΣ∗∩Σ∗αu1.
2. If u1 ̸= v1, then H∗
α(wui)∩H∗
α(vjw) = ∅for all 1 ≤i < m and 1 ≤j < n.
3. Let 1 ≤i < j < m. If uj >s ui, then H∗
α(wuj) ⊆H∗
α(wui); otherwise,
H∗
α(wui) ∩H∗
α(wuj) = ∅.
8


## Page 9


Proof. Consider a word z with preﬁx u1α and suﬃx αu1. It is easy to see that
any word which is a hairpin completion of z has preﬁx u1α and suﬃx αu1, as
well. Statement 1 follows by induction.
Note that v1α is not a proper preﬁx of u1α; otherwise, v1 would be a α-preﬁx
of w which is longer than u0 = ε but shorter than u1. Symmetrically, u1α is not a
proper preﬁx of v1α. By the ﬁrst statement, we have H∗
α(wui) ⊆u1αΣ∗∩Σ∗αu1
and H∗
α(v1w) ⊆v1αΣ∗∩Σ∗αv1 for all 1 ≤i < m and 1 ≤j < n. Therefore,
if u1 ̸= v1, the intersection H∗
α(wui) ∩H∗
α(vjw) has to be empty which proves
statement 2.
For statement 3, assume ﬁrst uj >s ui. By Lemma 3.8 we obtain uj = uj−iui
and hence wuj = wuiuj−i ∈H∗
α(wui). We conclude H∗
α(wuj) ⊆H∗
α(wui).
Now assume ui is not a suﬃx of uj. As wui (resp. wuj) is a factor of every
word in H∗
α(wui) (resp. H∗
α(wuj)) and there is only one factor w in every word
from H∗
α(w), it is plain that the intersection H∗
α(wui) ∩H∗
α(wuj) is empty (see
Corollary 3.3).
Let us deﬁne the index sets
I =

i
 1 ≤i < m ∧ui /∈{u1, . . . , ui−1}∗	
,
J =

j
 1 ≤j < n ∧vj /∈{v1, . . . , vj−1}∗	
.
Thus, for all i ∈I, no proper suﬃx of ui belongs to Pα(w) and for all j ∈J, no
proper preﬁx of vj belongs to Sα(w), see Lemma 3.8. By the previous lemma,
if v1 ̸= u1, then H∗
α(w) is the disjoint union
H∗
α(w) = {w} ∪
[
i∈I
H∗
α(wui) ∪
[
j∈J
H∗
α(vjw).
Note that for every word wui with i ∈I or vjw with j ∈J, the shortest
α-preﬁx is complementary to the shortest α-suﬃx. This observation leads us to
an important theorem that allows us to reduce the general case to the special
case where u1 = v1.
Theorem 4.6. Let w ∈αΣ∗∩Σ∗α be a non-crossing (m, n)-word with m, n ≥
2, let Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1, let Sα(w) =
{v0, . . . , vv−1} such that vn−1 >s · · · >s v0, and deﬁne I, J as above.
For u1 ̸= v1, H∗
α(w) is regular if and only if H∗
α(wui) is regular for all i ∈I
and H∗
α(vjw) is regular for all j ∈J.
Proof. As we already stated
H∗
α(w) = {w} ∪
[
i∈I
H∗
α(wui) ∪
[
j∈J
H∗
α(vjw).
If every language in the union is regular, then the union itself is regular.
Conversely, assume H∗
α(wui) is not regular for some i ∈I, then the intersection
H∗
α(w) ∩(u1αΣ∗∩Σ∗αu1) ∩Σ∗wuiΣ∗= H∗
α(wui)
is not regular and hence H∗
α(w) is not regular either, by Lemma 4.5.
The
argument for non-regular H∗
α(vjw) with j ∈J is analogous.
9


## Page 10


Theorem 4.6 justiﬁes the assumption u1 = v1 that we make from now on.
The next two theorems prove a necessary and suﬃcient condition for the regu-
larity of H∗
α(w). We start by proving that the condition is suﬃcient.
Theorem 4.7. Let w ∈αΣ∗∩Σ∗α be a non-crossing (m, n)-word with m, n ≥2,
let Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1, and let Sα(w) =
{v0, . . . , vv−1} such that vn−1 >s · · · >s v0.
H∗
α(w) is regular if both of the following conditions hold:
1. for all 1 ≤s < m, either us ∈Sα(w)∗or Sα(w)∗⊆{u1, . . . , us}∗, and
2. for all 1 ≤t < n, either vt ∈Pα(w)∗or Pα(w) ⊆{v1, . . . , vt}∗t.
Proof. Assume that both the conditions 1 and 2 are satisﬁed. We may assume
that there is 1 ≤s < m such that us ̸∈Sα(w)∗or there is 1 ≤t < n such
that vt ̸∈Pα(w)∗; otherwise Corollary 4.4 yields the regularity. In addition,
we cannot assume the existence of both such s and t as us ̸∈Sα(w)∗implies
Sα(w)∗⊆{u1, . . . , us}∗due to the condition 1.
The symmetry in the roles
of conditions 1 and 2 enables us to assume that such s exists without loss of
generality, and moreover, we can assume that for all 1 ≤i < s, ui ∈Sα(w)∗and
for all s ≤i < m, ui ̸∈Sα(w)∗by Lemma 3.7.
Let R′ = Sα(w)∗w{u1, . . . , us−1}∗and for s ≤i < m, let
Ri = {u1, . . . , ui}∗w{u1, . . . , ui}∗ui{u1, . . . , ui}∗.
Then we let R = S
s≤i<m Ri ∪R′ and we claim H∗
α(w) = R.
Firstly, we prove that R ⊆H∗
α(w). Since m, n ≥2, Corollary 3.6 can be
used to see that w{u1, . . . , ui}∗ui ⊆H∗
α(w) for s ≤i < m, and by Lemma 4.3,
Ri = {u1, . . . , ui}∗w{u1, . . . , ui}∗ui{u1, . . . , ui}∗⊆H∗
α(w).
Consider z ∈R′. We may factorize z = xi · · · x1wy1 · · · yj where x1, . . . , xi ∈
Sα(w) and y1, . . . , yj ∈{u1, . . . , us−1}. Let 1 ≤t < n be minimal such that
vt /∈{u1, . . . , us−1}∗. As vt ∈{u1, . . . , us}∗, we see that us is a factor of vt
and t ≥s. By Lemma 3.9, us−1 ∈{v1, . . . , vt−1}∗and, by the minimality of
t, vt−1 ∈{u1, . . . , us−1}∗.
If indα(xℓ) < t for all 1 ≤ℓ≤i, then, due to
Lemma 4.3,
z ∈{v1, . . . , vt−1}∗w {v1, . . . , vt−1}∗⊆H∗
α(w).
Otherwise, let 1 ≤ℓ≤i be maximal such that indα(xℓ) ≥t and let w′ =
xℓ· · · x1w. Observe that w →∗
LH w′ and, again by Lemma 4.3,
z ∈{v1, . . . , vt−1}∗w′ {v1, . . . , vt−1}∗⊆H∗
α(w′) ⊆H∗
α(w).
Thus, R ⊆H∗
α(w).
Now we prove the opposite inclusion by induction on the length of a deriva-
tion to generate a word in H∗
α(w) from w. Clearly, w ∈R (base case). As
an induction hypothesis, we assume that any word which can be derived from
w by ℓ−1 hairpin completions is in R, and consider z ∈H∗
α(w) whose short-
est derivation from w by hairpin completions is of length ℓ.
Let w′ be the
word that precedes z on this shortest derivation, that is, w′ ∈Hℓ−1
α
(w); hence,
w′ ∈R by the induction hypothesis. Therefore, w′ must be either in Ri for
10


## Page 11


some s ≤i < m or in R′. Let us consider the ﬁrst case ﬁrst. If z is obtained
from w′ by right hairpin completion, then the complement of the extended part
is in {u1, . . . , ui}∗{ε, u1, . . . , um−1}, and hence, z ∈Rj for some i ≤j < m.
Otherwise (w′ →LH z), z ∈Ri because Sα(w′) ⊆{u1, . . . , us}∗⊆{u1, . . . , ui}∗.
Next we consider the case when w′ ∈R′. Since {u1, . . . , us−1}∗⊆Sα(w)∗it
is easy to see that if w′ →LH z, then z ∈R′ as well. Otherwise (w′ →RH z),
z ∈w′ {ε, u1, . . . , um−1} Sα(w)∗and, as Sα(w)∗⊆{u1, . . . , us}∗, if z /∈R′, this
word is covered by some language Ri where s ≤i < m.
Consequently, H∗
α(w) = R is regular.
Theorem 4.8. Let w ∈αΣ∗∩Σ∗α be a non-crossing (m, n)-word with m, n ≥
2, let Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1, let Sα(w) =
{v0, . . . , vv−1} such that vn−1 >s · · · >s v0, and let u1 = v1.
1. H∗
α(w) is not regular if there are 1 ≤s < m and 1 ≤t < n such that
us /∈{v1, . . . , vn−1}∗and vt /∈{u1, . . . , us}∗.
2. H∗
α(w) is not regular if there are 1 ≤s < m and 1 ≤t < n such that
us /∈{v1, . . . , vt}∗and vt /∈{u1, . . . , um−1}∗.
Proof. Let s and t be the minimal indices that satisfy the conditions in state-
ment 1. Note that s, t ≥2 and us, vt /∈u+
1 as u1 = v1. We will ﬁrst argue, why
the assumption s ≤t is no restriction.
Let us consider the case where the conditions in statement 1 are satisﬁed,
but the conditions in statement 2 are not satisﬁed.
It is easy to see that
us /∈{v1, . . . , vt}∗is satisﬁed anyway. By contradiction assume s > t. Due
to Lemma 3.9,
vt /∈{u1, . . . , us}∗
⇐⇒
vt /∈{u1, . . . , ut}∗
⇐⇒
vt /∈{u1, . . . , um−1}∗.
This satisﬁes the conditions of statement 2 and yields the contradiction. We
conclude s ≤t.
Now, let us consider the case where the conditions of both statements are
satisﬁed. Let s and t′ be the minimal indices such that us /∈{v1, . . . , vn−1}∗
and vt′ /∈{u1, . . . , um−1}∗. We may assume s ≤t′, by symmetry. Note that
vt′−1 ∈{u1, . . . , um−1}∗, by the minimality of t′. If vt′−1 ∈{u1, . . . , vs}∗, then
we see that s and t = t′ are the minimal indices that satisfy the conditions in
statement 1 and s ≤t. Otherwise, there is a factorization vt′−1 = xuiy where
x ∈{u1, . . . , us}∗, s < i < m, and y ∈{u1, . . . , um−1}∗.
Note that s and
t = indα(x) + s + 1 (hence vt = xus+1) are the minimal indices that satisfy the
conditions of statement 1 and, obviously, s ≤t.
Observe that the minimality of s yields u1, . . . , us−1 ∈{v1, . . . , vn−1}∗. If
x ∈{u1, . . . , us−1, v1, . . . , vn−1} was a suﬃx of us, then us = us−indα(x)x ∈
{v1, . . . , vn−1}∗, due to Lemma 3.8. Hence, none of these words is a suﬃx of us.
Symmetrically, none of the words u1, . . . , us, v1, . . . , vt−1 is a suﬃx of vt. This
observation will become crucial later.
We will now deﬁne a regular language R and show that the intersection
H∗
α(w) ∩R is not regular and, therefore, H∗
α(w) is not regular either. We let
R = usu≥n
1 vtwu1≥nus
11


## Page 12


and we claim
H∗
α(w) ∩R =

usuℓ
1vtwu1ℓus
 ℓ≥n
	
=: L,
which is obviously not regular. Note that for every ℓ≥n
w →∗
RH wu1ℓ→RH wu1ℓus →LH usuℓ
1vtwu1ℓus.
Hence, H∗
α(w) ∩R ⊇L.
Let z = usuℓ1
1 vtwu1ℓ2us for some ℓ1, ℓ2 ≥n, which is in R. We assume
z ∈H∗
α(w) and prove that this assumption requires ℓ1 = ℓ2. Let z′ be the right-
most word in the derivation w →∗
H z′ →∗
H z such that z′ = xwy for some words
x, y with uℓ1
1 vt ≥s x and y ≤p u1ℓ2; these conditions mean that x or y does
not overlap with the preﬁx us or the suﬃx us, respectively. By right-most we
mean that either z′ →LH x′z′ →∗
H z where x′x >s uℓ1
1 vt or z′ →RH z′y′ →∗
H z
where u1ℓ2 <p yy′; this means x′ or y′ overlaps with the preﬁx us or the suﬃx
us, respectively. Obviously, y ∈u1∗. Note that if x ̸= ε, then x cannot be a
proper suﬃx of vt; otherwise a word from u1 = v1, . . . , vt−1 would be a suﬃx of
vt which was excluded. Hence, x = ε or x ∈u∗
1vt.
First consider the case z′ →LH x′z′ →∗
H z where x′x >s uℓ1
1 vt. We show that
this case cannot occur. Let u′ ̸= ε be the suﬃx of us such that u′uℓ1
1 vt = x′x.
As x′ ∈u∗
1 {v1, . . . , vn−1} and u′α ≤p x′α, some word from u1 = v1, . . . , vn−1
would be a suﬃx of us.
Now consider the case z′ →RH z′y′ →∗
H z where u1ℓ2 <p yy′. Again, let
u′ ̸= ε be the suﬃx of us such that u1ℓ2u′ = yy′. As u′α is a preﬁx of xum−1α
and none of the words v1, . . . , vt, u1, . . . , us−1 is a suﬃx of us, we see that
u′ = us and x = ε.
Thus, in order to generate z from w by iterated hairpin completion, the
derivation process must be of the form
w →∗
RH wu1
ℓ2us →∗
LH usuℓ1
1 vtwu1
ℓ2us = z.
Let x be a (newly chosen) word such that wu1ℓ2us →LH xwu1ℓ2us is the
ﬁrst left hairpin completion in the derivation above. Therefore, xα is a preﬁx
of usuℓ2
1 vn−1α and x is a suﬃx of usuℓ1
1 vt. In particular, every suﬃx y of x
with indα(y) ≤t is a suﬃx of vt. Recall that indα(us) = s ≤t. If xα was a
preﬁx of usα, then some word from u1, . . . , us would be a suﬃx of vt which is
impossible. Verify that x ∈usu+
1 and x = usuℓ2
1 vj with 1 ≤j < t would also
impose a forbidden suﬃx for vt. Thus, we see that x = usuℓ2
1 vj with t ≤j < n.
The case j > t is not possible as it implies vtα <p vjα = uj−t
1
vtα and a word
from u1 = v1, . . . , vt−1 would be a suﬃx of vt. Therefore, x = usuℓ2
1 vt and since
x is a suﬃx of usuℓ1
1 vt and u1 is not a suﬃx of us we deduce usuℓ2
1 vt = usuℓ1
1 vt.
Consequentially, z ∈H∗
α(w) if and only if ℓ1 = ℓ2. This completes the proof
of H∗
α(w) ∩R = L.
Combining Theorems 4.7 and 4.8, we conclude:
Corollary 4.9. Let w ∈αΣ∗∩Σ∗α be a non-crossing (m, n)-word with m, n ≥
2, let Pα(w) = {u0, . . . , um−1} such that u0 <p · · · <p um−1, let Sα(w) =
{v0, . . . , vv−1} such that vn−1 >s · · · >s v0, and let u1 = v1.
H∗
α(w) is regular if and only if
12


## Page 13


1. for all 1 ≤s < m we have us ∈Sα(w)∗or Sα(w) ⊆{u1, . . . , us}∗and
2. for all 1 ≤t < n we have vt ∈Pα(w)∗or Pα(w) ⊆{v1, . . . , vt}∗.
Proof. Theorem 4.7 provides the if-part.
For the only-if-part, assume that condition 1 is breached. There exists 1 ≤
s < m such that us /∈Sα(w)∗and Sα(w) \ {u1, . . . , us}∗̸= ∅. Let 1 ≤t < n
such that vt ∈Sα(w) \ {u1, . . . , us}∗. We see that s, t are indices satisfying
the conditions of statement 1 in Theorem 4.8 and, therefore, H∗
α(w) is not
regular.
Thus, we provided a necessary and suﬃcient condition for the regularity of a
non-crossing (m, n)-word. As one can easily observe, this condition is decidable.
Corollary 4.10. For a given non-α-crossing word w, it is decidable whether or
not its iterated hairpin completion, H∗
α(w), is regular.
Furthermore, we can derive from the proof of Theorem 4.8 that if the iterated
hairpin completion of w is not regular, then the intersection of H∗
α(w) with
R = usu≥n
1 vtwu1≥nus is not a regular language (for suitable s, t and in case
u1 = v1). More precisely, we obtained the context-free language
H∗
α(w) ∩R =

usuℓ
1vtwu1
ℓus
 ℓ≥n
	
.
Consider we intersect H∗
α(w) with R′ = (usu≥n
1 vt)2wu1≥nus.
Using the
same arguments as we did within the proof of Theorem 4.8, we can show that
H∗
α(w) ∩R′ =

usuℓ
1vtusuℓ
1vtwu1ℓus
 ℓ≥n
	
,
which is a non-context-free language. Using this idea we can proof that if H∗
α(w)
is not regular, it is not context-free either. The details of this proof are left for
the interested reader.
Corollary 4.11. Let w be a non-α-crossing word. If its iterated hairpin com-
pletion H∗
α(w) is not regular, then H∗
α(w) is not context-free.
Final Remarks
We prove that regularity of iterated hairpin completion a given of non-crossing
word is decidable. The general case, including that of crossing words, remains
to be explored.
References
[1] Adleman, L.M.: Molecular computation of solutions to combinatorial prob-
lems. Science 266(5187), 1021–1024 (1994)
[2] Arita, M., Kobayashi, S.: DNA sequence design using templates. New Gen-
eration Computing 20, 263–277 (2002)
[3] Cheptea, D., Mart´ın-Vide, C., Mitrana, V.: A new operation on words
suggested by DNA biochemistry: Hairpin completion. Transgressive Com-
puting pp. 216–228 (2006)
13


## Page 14


[4] Diekert, V., Kopecki, S.: Complexity results and the growths of hairpin
completions of regular languages (extended abstract). In: Domaratzki, M.,
Salomaa, K. (eds.) CIAA. Lecture Notes in Computer Science, vol. 6482,
pp. 105–114. Springer (2010)
[5] Hagiya, M., Arita, M., Kiga, D., Sakamoto, K., Yokoyama, S.: Towards
parallel evaluation and learning of boolean µ-formulas with molecules. In:
Second Annual Genetic Programming Conf. pp. 105–114 (1997)
[6] Hopcroft, J.E., Ulman, J.D.: Introduction to Automata Theory, Languages
and Computation. Addison-Wesley (1979)
[7] Jonoska, N., Kephart, D., Mahalingam, K.: Generating DNA codewords.
Congressus Numerantium 156, 99–110 (2002)
[8] Jonoska, N., Mahalingam, K.: Languages of DNA based code words. In:
Chen, J., Reif, J. (eds.) Proc. of DNA Computing 9. Lecture Notes in
Computer Science, vol. LNCS 2943, pp. 61–73. Springer (2004, 61-73)
[9] Kameda, A., Yamamoto, M., Ohuchi, A., Yaegashi, S., Hagiya, M.: Unravel
four hairpins! Natural Computing 7, 287–298 (2008)
[10] Kari, L., Konstantinidis, S., Losseva, E., Sos´ık, P., Thierrin, G.: A formal
language analysis of DNA hairpin structures. Fundamenta Informaticae
71(4), 453–475 (2006)
[11] Kari, L., Kopecki, S., Seki, S.: On the regularity of iterated hairpin com-
pletion of a single word. Fundamenta Informaticae (to appear) (2011), also
in CoRR abs/1104.2385
[12] Kopecki, S.: On iterated hairpin completion. Theoretical Computer Science
412(29), 3629–3638 (July 2011)
[13] Manea, F.: A series of algorithmic results related to the iterated hairpin
completion. Theor. Comput. Sci. 411(48), 4162–4178 (2010)
[14] Manea, F., Mart´ın-Vide, C., Mitrana, V.: On some algorithmic problems
regarding the hairpin completion. Discrete Applied Mathematics 157(9),
2143–2152 (2009)
[15] Manea, F., Mitrana, V.: Hairpin completion versus hairpin reduction. In:
Cooper, S.B., L¨owe, B., Sorbi, A. (eds.) CiE. Lecture Notes in Computer
Science, vol. 4497, pp. 532–541. Springer (2007)
[16] Manea, F., Mitrana, V., Yokomori, T.: Two complementary operations
inspired by the DNA hairpin formation: Completion and reduction. Theor.
Comput. Sci. 410(4-5), 417–425 (2009)
[17] Manea, F., Mitrana, V., Yokomori, T.: Some remarks on the hairpin com-
pletion. Int. J. Found. Comput. Sci. 21(5), 859–872 (2010)
[18] P˘aun, G., Rozenberg, G., Yokomori, T.: Hairpin languages. International
Journal of Foundations of Computer Science 12(6), 837–847 (2001)
14


## Page 15


[19] Sakamoto, K., Kiga, D., Komiya, K., Gouzu, H., Yokoyama, S., Ikeda, S.,
Hagiya, M.: State transitions by molecules (1998)
[20] Takinoue, M., Suyama, A.: Molecular reactions for a molecular memory
based on hairpin DNA. Chem-Bio Informatics Journal 4, 93–100 (2004)
[21] Takinoue, M., Suyama, A.: Hairpin-DNA memory using molecular address-
ing. Small 2(11), 1244–1247 (2006)
[22] Winfree, E.: Whiplash PCR for O(1) computing. In: University of Penn-
sylvania. pp. 175–188 (1998)
15

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]