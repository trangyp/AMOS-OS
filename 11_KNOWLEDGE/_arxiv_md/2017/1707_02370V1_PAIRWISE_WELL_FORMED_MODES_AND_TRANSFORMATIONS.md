---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.02370v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1707.02370v1_Pairwise_Well-Formed_Modes_and_Transformations

> Source: 1707.02370v1_Pairwise_Well-Formed_Modes_and_Transformations.pdf

> Pages: 12

---


## Page 1


Pairwise Well-Formed Modes and
Transformations
David Clampitt and Thomas Noll
Ohio State University, School of Music, USA
clampitt.4@osu.edu
Escola Superior de M´usica de Catalunya
Departament de Teoria, Composici´o i Direcci´o, Spain
thomas.mamuth@gmail.com
Abstract. One of the most signiﬁcant attitudinal shifts in the history
of music occurred in the Renaissance, when an emerging triadic con-
sciousness moved musicians towards a new scalar formation that placed
major thirds on a par with perfect ﬁfths. In this paper we revisit the
confrontation between the two idealized scalar and modal conceptions,
that of the ancient and medieval world and that of the early modern
world, associated especially with Zarlino. We do this at an abstract level,
in the language of algebraic combinatorics on words. In scale theory
the juxtaposition is between well-formed and pairwise well-formed scales
and modes, expressed in terms of Christoﬀel words or standard words
and their conjugates, and the special Sturmian morphisms that generate
them. Pairwise well-formed scales are encoded by words over a three-
letter alphabet, and in our generalization we introduce special positive
automorphisms of F3, the free group over three letters.
Keywords: pairwise well-formed scales and modes, well-formed scales
and modes, well-formed words, Christoﬀel words, standard words, central
words, algebraic combinatorics on words, special Sturmian morphisms.
1
Introduction: Authentic and Triadic Modes
Figure 1 shows a C-major scale with two diﬀerent interpretations of its step
interval pattern. In the annotation aaba|aab (above the staﬀ) the two letters a
and b designate the major and minor steps, respectively. The vertical stroke |
designates the authentic divider of the mode into a species of the ﬁfth aaba and
a species of a fourth aab. This pattern is called the Authentic division of the
Ionian Mode. In the annotation ac|ba||cab (below the staﬀ) the three letters a, c
and b designate the greater and lesser major and the minor steps, respectively.
Together they divide the major mode triadically into a species of the major third
ac, a species of the minor third ba and a species of the fourth cab. This pattern
shall be called the Triadic Division of the Ionian Major Mode.
The contrasting juxtaposition evokes several open questions of historical and
systematic nature about the particular relevance of these modes for diﬀerent
arXiv:1707.02370v1  [math.CO]  7 Jul 2017


## Page 2


2
David Clampitt and Thomas Noll
Fig. 1. Authenic Division of the Ionian and Triadic Di-
vision of the Ionian Major mode.
types of music and music analysis. Within the discourse of mathematical music
theory they point to the theory of well-formed scales and modes ([6], [5], [10],
[2]), on the one hand, and to the theory of pairwise well-formed scales ([4], [3]),
on the other. In the present article we therefore extend some transformational in-
novations within the theory of well-formed modes in order to make them fruitful
within a theory of pairwise well-formed modes. These investigations eventually
contribute to a deeper theoretical understanding of the juxtaposition in Fig. 1.
2
Non-Singular Pairwise Well-Formed Modes
In this section we revisit some important results from [4] about the structure
of non-singular pairwise well-formed scales and re-interpret them in a word-
theoretic context. The 3-letter word acbacab describes the species of the octave
of the Ionian Major mode, and thereby it is the step interval pattern of a pair-
wise well-formed scale. The motivation behind this concept is the following:
The two-letter word aabaaab, describing the Ionian species of the octave can
be obtained from acbacab by an identiﬁcation of the letter c with the letter a:
πc→a(acbacab) = aabaaab. In traditional music-theoretical terms this letter pro-
jection describes syntonic identiﬁcation, i.e., neglecting the diﬀerence between
the greater and lesser major steps. There are two more such letter identiﬁcations,
both of which lead to well-formed modes, whence the term pairwise well-formed.
One of them is πb→c(bacabac) = cacacac. It describes an identiﬁcation of the mi-
nor step with the lesser major step, i.e., neglecting their diﬀerence, what we may
call the (harmonic) apotome. This mode neutralizes also the diﬀerence between
the major and minor thirds and can be seen as a modal reﬁnement of the generic
third-generated scale. The third letter projection πa→b(bacabac) = bbcbbbc iden-
tiﬁes the minor step with the greater major step. The neglected interval is the
sum of the two previously mentioned ones, and so we can formally speak of an
apo-syntonic identiﬁcation. It is arguable, though, whether this third projection
bears a direct musical meaning. As an auxiliary construction it proves to be very
useful on a theoretical level. This becomes clear in the course of the article.
We will represent non-singular pairwise well-formed (PWWF) scales by words
over a three-letter alphabet A = {a, b, c}, as in [3], and we will henceforth refer
to PWWF words and drop the qualiﬁer “non-singular” (the singular case is
represented by the word abacaba and its word-theoretical conjugates). We denote
the set of all PWWF words by A ⊂{a, b, c}∗. From [4], [2], v ∈A if and


## Page 3


Pairwise Well-Formed Modes and Transformations
3
only if each of the three projections πx→y (described above) results in a well-
formed word, i.e., the conjugate of a Christoﬀel word, equivalently, of a standard
word (see [7], [1] for the relevant word theory background). For every word
v ∈A, the length |v| is odd, and the multiplicities of two of the letters are
the same: |v|b = |v|c. It follows that |v|a is odd. In light of these facts, given a
special standard word, we can always construct a PWWF word, by the bisecting
substitution deﬁned below.
Deﬁnition 2.1. Consider a special standard morphism f acting on the word
monoid {a, c}∗and consider the word w = f(ac) = w1w2 . . . wn. We further
suppose that |w| = n is odd and that |w|c is even. Then we deﬁne the bisection
of the word w as w≺= v = v1v2 . . . vn ∈{a, b, c}∗with
vk :=



a if wk = a,
b if wk = c and |w1 . . . wk|c is odd
c if wk = c and |w1 . . . wk|c is even.
The bisecting substitution σ : {a, b, c}∗→{a, b, c}∗is then deﬁned as
σ(a) = v1 . . . vm,
σ(b) = vm+1 . . . v2m,
σ(c) = v2m+1 . . . vn, where m = |f(a)|.
Remark: PWWF scales have distinct inversions, whereas the inversion of
a mode of a well-formed scale is a mode of that scale (e.g., Ionian inverted is
Phrygian). In word-theoretical language, if w is a standard word, the reversal
of w is in the conjugacy class of w. For w ∈A, the reversal of w is in its own
conjugacy class, distinct from that of w. For k ∈N, there are φ(k)/2 distinct
conjugacy classes of standard words of length k; for PWWF words (k odd), there
are φ(k) distinct conjugacy classes [4]. The deﬁning projections are insensitive
to reversal, however, up to trivial replacements of the letters, so we may pair
w with its reversal, and choose whichever is convenient as representive. There
is thus a bijection between conjugacy classes of standard words and classes of
PWWF words of odd length k.
For example, w = bacabac ∈A, and its reversal is w′ = cabacab. πc→a(w) =
baaabaa (representing Phrygian), πb→a(w) = aacaaac (representing Ionian),
and πb→c(w) = cacacac (representing, e.g., Dorian thirds); while πc→a(w′) =
aabaaab (Ionian), πb→a(w′) = caaacaa (Phrygian), and πb→c(w) = cacacac.
Therefore, we may depart from either PWWF representative.
Proposition 2.2. Consider a PWWF substitution σ and let f(a) = πb→c(σ(a)),
f(c) = πb→c(σ(bc)) denote its apotomic projection. Let Mf =
|f(a)|a |f(c)|a
|f(a)|c
|f(c)|c

denote the incidence matrix of f. Then the incidence matrix of σ is given as
˜
Mσ =





|f(a)|a
|f(a)|a
|f(c)|a −|f(a)|a
⌊|f(a)|c
2
⌋⌈|f(a)|c
2
⌉|f(c)|c −|f(a)|c
2
⌈|f(a)|c
2
⌉⌊|f(a)|c
2
⌋|f(c)|c −|f(a)|c
2




.


## Page 4


4
David Clampitt and Thomas Noll
3
Apo-syntonic Conversion
In addition to the letter projections πb→c, πa→b, πc→a on words v ∈A∗, we apply
them to substitutions as follows (using the same symbols):
Deﬁnition 3.1. Consider a substitution (a monoid morphism) σ : A∗→A∗.
Then we obtain three induced substitutions πb→c(σ) : {a, c}∗→{a, c}∗, πa→b(σ) :
{b, c}∗→{b, c}∗and πc→a(σ) : {a, b}∗→{a, b}∗by virtue of:
[πb→c(σ)](a) := πb→c(σ(a))
[πb→c(σ)](c) := πb→c(σ(bc))
[πa→b(σ)](b) := πa→b(σ(ab))
[πa→b(σ)](c) := πa→b(σ(c))
[πc→a(σ)](a) := πc→a(σ(ab))
[πc→a(σ)](b) := πc→a(σ(c))
We say that σ is an authentic PWWF substitution iﬀall three projections πb→c(σ),
πa→b(σ) and πc→a(σ) are Special Sturmian morphisms.
In the rest of this section we will assume that σ is the bisecting substitution asso-
ciated with a suitable special standard morphism f and hence f = πb→c(σ). Fur-
ther we use the symbols g and ˜g for the projections g = πa→b(σ) and ˜g = πc→a(σ)
The diagram in Figure 2 shows the interplay of σ with its three projections.
σ
g
f
˜g









+

3 A
A
A
A
AAU
QQQQQQQQQ
s
-
-
bisection
apo-syntonic conversion
conjugation
πb→c
πa→b
πc→a
Fig. 2. Interplay of a PWWF substitution σ with its projections f, g and ˜g.
Our goal is now to understand the interdependence between f and g.
Proposition 3.2. Consider an authentic (non-singular) PWWF mode σ ∈A
with the projections f = πb→c(σ), g = πa→b(σ) and ˜g = πc→a(σ). Then the
common incidence matrix Mg = M˜g of g and ˜g can be expressed in terms of the
coeﬃcients of the incidence matrix Mf =
|f(a)|a |f(c)|a
|f(a)|c
|f(c)|c

as follows:
Mg = M˜g =
2|f(a)|a + |f(a)|c |f(c)|a −|f(a)|a + 1
2(|f(c)|c −|f(a)|c)
|f(a)|c
1
2(|f(c)|c −|f(a)|cb)

.
Proof. The incidence matrix Mg can be obtained from adding the ﬁrst two
columns and the ﬁrst two rows of ˜
Mσ. Thus, after proposition 2.2 the upper left
entry of Mg becomes |f(a)|a +|f(a)|a +⌊|f(a)|c
2
⌋+⌈|f(a)|c
2
⌉= 2|f(a)|a +f(a)|c.
The upper right entry becomes |f(c)|a −|f(a)|a+ |f(c)|c −|f(a)|c
2
, the lower left


## Page 5


Pairwise Well-Formed Modes and Transformations
5
entry becomes ⌈|f(a)|c
2
⌉+ ⌊|f(a)|c
2
⌋= |f(a)|c. The lower right entry remains
|f(c)|c −|f(a)|c
2
.
In order to understand the connection between f and g more directly, rather
than via the substitution σ, we have a closer look at the structure of the linear
map: ˜β : GL2(R) →GL2(R) with
˜β(

a11 a12
a21 a22

) :=

2a11 + a21 a12 −a11 + (a22 −a21)/2
a21
(a22 −a21)/2

.
With R =

1 1
0 1

let Σ2 and Σ2 denote the following two subsets of SL2(N):
Σ2 =

R ·
2b11 b12
b21
b22

| b11, b12, b21, b22 ∈N, 2b11b22 −b12b21 = 1

Σ2 =
b11
b12
b21 2b22

· R
| b11, b12, b21, b22 ∈N, 2b11b22 −b12b21 = 1

Lemma 3.3. SL2(N) ∩˜β−1(SL2(N)) = Σ2 and ˜β(Σ2) = Σ2.
Proof. Consider an arbitrary matrix X =
c11 c12
c21 c22

∈SL2(N). Then we have
˜β−1(
c11 c12
c21 c22

) =
 c11−c21
2
c11−c21
2
+ c12 −c22
c21
c21 + 2c22

.
The entry c21 + 2c22 is larger than c21 and therefore ˜β−1(X) ∈SL2(N) iﬀ
Y = ˜β−1(X) · R−1 =
 c11−c21
2
c12 −c22
c21
2c22

∈SL2(N). But in order to have a
positive entry c12 −c22 it turns out that X ∈SL2(N) cannot be arbitrary. Also
Z = R−1 · X =
c11 −c21 c12 −c22
c21
c22

must be in SL2(N). And this implies
c11 ≥c21. Finally, we have to deal with the condition that the upper left entry
c11−c21
2
of ˜β−1(X) needs to be an integer. This implies that c11 −c21, which is
also the upper left entry of Z, is even, i.e., RZ = X ∈Σ2.
Corollary 3.4. The set Σ2 parametrizes the conjugation classes of all authentic
PWWF substitutions σ in terms of the incidence matrices Mf of their associated
apotomic projections: the special standard morphisms f = πb→c(σ). Also the
set Σ2 parametrizes these same conjugation classes by virtue of the incidence
matrices Mg of their associated apo-syntonic projections g = πa→b(σ).
This motivates the following deﬁnition:
Deﬁnition 3.5. The restriction of ˜β to the subset Σ2 is called the apo-syntonic
conversion:
β : Σ2 →Σ2.


## Page 6


6
David Clampitt and Thomas Noll
Let δ : SL2(N) →SL2(N) denote the main-diagonal-ﬂip
δ(
b11 b12
b21 b22

) :=
b22 b12
b21 b11

.
Lemma 3.6. δ mutually exchanges Σ2 and Σ2, i.e. δ(Σ2) = Σ2 and δ(Σ2) =
Σ2.
Proposition 3.7. We have the following commutative diagram
Σ2
Σ2
Σ2
Σ2
-

?
?
6
6
β
β
δ
δ
Proposition 3.8. Under the convention that the apotomic projection f is a
standard morphism, the apo-syntonic projection g also turns out to be a special
standard morphism.
Proof. As f is special standard we have a decomposition w = f(ac) = f(a)f(c) =
tcasac with a negative (= plagal) standard word tca and a positive (= authentic)
standard word sac. We have g(bc) = u1u2 . . . u|w| ∈{b, c}∗with
uk :=



b if wk = a,
b if wk = c and |w1 . . . wk|c is odd
c if wk = c and |w1 . . . wk|c is even.
The ﬁnal letter of u is c, because |w|c is even, so by deﬁnition of u above, the last
letter c is ﬁxed. Let v = cuc−1 ∈{b, c}∗denote the result of conjugating u with
c−1. In order to show that g is a special standard morphism, it is suﬃcient to
show that v = v1v2 . . . v|w| is the bad conjugate of u. Let m = |g(b)| denote the
length of g(b). It is suﬃcient to show that |v1 . . . vm|b diﬀers from |u1 . . . um|b =
|g(b)|b. Knowing that f(a) is a preﬁx of f(c) we write w = f(a)f(a)f(a−1c) =
tcatcarac and we may conclude that wm = a, and hence um = b = vm+1. But
in the light of v1 = c this implies |v1 . . . vm|b = |g(b)|b −1, i.e. v is the bad
conjugate.
4
PWWF Substitutions and Automorphisms of F3
In the two-dimensional situation of well-formed modes we may interpret the
Sturmian morphisms as positive automorphisms of the free group F2. In the
world of substitutions on words in three letters their analogues constitute dif-
ferent transformational concepts. The PWWF substitutions are well-adopted to
the family of (non-singular) pairwise well-formed modes. Still there is a small


## Page 7


Pairwise Well-Formed Modes and Transformations
7
subfamily of pairwise well-formed modes, where these substitutions are also au-
tomorphisms of the free group F3. This ﬁnal section is dedicated to their study.
To get a concrete idea about the role of F3-automorphisms, we look into the
Authentic and Triadic Divisions of the Phrygian mode (see Figure 3). In the
theory of well-formed modes one describes the species baaa and baa of the ﬁfth
and fourth as images of a and b under a word transformation ˜g(a) = baaa,
˜g(b) = baa. The left side of Figure 3 shows a decomposition of this compound
transformation into three elementary ones. First, the ﬁfth a is ﬁlled with a fourth
and a major step a 7→ba, then both fourths are ﬁlled with a minor third and
a major step b 7→ba and ﬁnally, both minor thirds are ﬁlled with a minor step
and a major step b 7→ba.
Fig. 3. Construction of the Authentic Phrygian and the
Triadic Phrygian Minor modes through substitutions.
The right side of Figure 3 shows an analogous procedure for the construction
of the Phrygian Minor mode ba|ca||bac. The fourth is ﬁlled with a minor third
and a lesser major step: c 7→bc. Then the major third is ﬁlled with a lesser
and and greater major step: a 7→ca and ﬁnally both minor thirds are ﬁlled
with a minor step followed by a greater major step: b 7→ba. This ﬁnal act in
the generation of the Phrygian Minor mode does not work analogously for the
Ionian Major mode, because there we ﬁnd two diﬀerent species of the minor
third: ba and ab.
The automorphism group Aut(Fn) of the free group Fn = ⟨x1, x2, . . . , xn⟩
is redundantly generated by the elementary Nielsen transformations (see [9],
[8], p. 162 ﬀ.), namely the letter transpositions xi 7→xk, xk 7→xi, cyclic letter
permutations x1 7→x2 7→· · · 7→xn 7→x1, letter inversions xi 7→x−1
i
and the
substitutions of the types xi 7→xixk or xi 7→xkxi. The automorphisms of F3,
which potentially coincide with PWWF substitutions, are necessarily positive,
so we don’t need to consider letter inversions here. This leads to the following
deﬁnition:


## Page 8


8
David Clampitt and Thomas Noll
Deﬁnition 4.1. An authentic PWWF substitution is called morphic, if it is a
positive automorphism of F3.
For two diﬀerent letters x, y ∈{a, b, c} let Ex,y, Axy, Pxy ∈Aut(F3) denote the
following positive automorphisms of the free group F3: Let z ∈{a, b, c} denote
the third letter, respectively.
Exy(x) = y,
Exy(y) = x, Exy(z) = z,
Axy(x) = xy, Axy(y) = y, Axy(z) = z,
Pxy(x) = yx, Pxy(y) = y, Pxy(z) = z.
Hence, a PWWF substitution σ : {a, b, c}∗→{a, b, c}∗is morphic, if it can
be written as a composition of a ﬁnite number of letter permutations Exy and
substitutions of the types Axy and/or Pxy. Now we inspect the seven conjugates
of the Phrygian minor mode to which also the Ionian major mode belongs. The
following proposition is thus the portrait of a very special conjugation class of
modes. As in the two-letter case it contains bad conjugates.
Proposition 4.2. Let σ : {a, b, c}∗→{a, b, c}∗with σ(b) = ba, σ(a) = ca
and σ(c) = bac denote the PWWF substitution, which is associated with the
Phrygian minor mode. The cycle of the single letter conjugations ba|ca||bac →
ac|ab||acb →ca|ba||cba →ab|ac||bac →ac|ba||cab →cb|ac||aba →ba|ca||bac
contains two bad conjugates and — accordingly — ﬁve PWWF modes. Four of
these PWWF modes are morphic. The exceptional good, but amorphous instance,
is the Ionian major mode. These seven conjugates together with their associated
projections under πb→c, πc→a(σ) and πa→b(σ) are listed below:
authentic
apotomic
syntonic
apo-syntonic
transform.
triadic mode
projection
projection
projection
type
ba|ca||bac
ca|cacac
baaa|baa
bbcb|bbc
morphic∗∗
ac|ab||acb
ac|acacc
aaab|aab
bcbb|bcb
morphic
ca|ba||cba
ca|cacca
aaba|aba
cbbb|cbb
morphic
ab|ac||bac
ac|accac
abaa|baa
bbbc|bbc
morphic
ba|cb||aca
ca|ccaca
baab|aaa
bbcb|bcb
bad∗
ac|ba||cab
ac|cacac
aaba|aab
bcbb|cbb
good∗
cb|ac||aba
cc|acaca
abaa|aba
cbbc|bbb
bad∗∗
Proof. In the left column of the table ba|ca||bac undergoes the full cycle of letter-
by-letter conjugations. In parallel the projections πb→c(σ), πc→a(σ) , πa→b(σ)
run through their corresponding conjugations. By virtue of proposition 3.8 the
conjugations of the apotomic and the apo-syntonic projections are “in sync”,
i.e. they start with special standard modes (marked as morphic∗∗) and they end
with bad modes (marked as bad∗∗). As a consequence there are only two bad
conjugates among the triadic modes. The generation of the four morphic modes
–up to letter permutations – is given below:
AbaPacPcb(b|a||c) = AbaPac(b|a||bc) = Aba(b|ca||bc) = ba|ca||bac
PcaAabPbc(c|a||b) = PcaAab(c|a||cb) = Pca(c|ab||cb) = ac|ab||acb
AbaPacAcb(a|b||c) = AbaPac(a|b||cb) = Aba(ca|b||cb) = ca|ba||cba
PcaAabPcb(b|a||c) = PcaAab(b|a||bc) = Pca(ab|c||bc) = ab|ac||bac


## Page 9


Pairwise Well-Formed Modes and Transformations
9
The obstacle for the “good” PWWF Ionian major mode to be generated by an
F3-automorphism is the co-existence of the two factors ab and ba.
In addition to the bad∗Locrian mode (with a bad syntonic projection) there
is the bad∗∗Dorian minor mode (with bad apotomic and apo-syntonic projec-
tions), whose structural defects have been discussed in 19th-century treatises,
such as Moritz Hauptmann’s 1853 Die Natur der Harmonik und der Metrik.
We show now that a similar picture arises in connection with a certain family
M of morphic PWWF modes and we conclude the article with the conjecture
that this family actually exhausts the morphic PWWF modes entirely. It is useful
to start the investigation of this family from the authentic standard modes, whose
bisecting transformations then yield the associated PWWF modes. The general
form of the standard morphism f, generating the single-divider mode f(a)|f(c) is
f = GkDG2n with n > 0 and k ≥0. The corresponding apo-syntonic conversion
of f, the standard morphism g, generating the ﬁrst of the two double divider
modes g(b)|g(c) is g = G2k+2DGn−1. Thus, we have the two sets
F = {GkDG2n | n > 0, k ≥0} and G = {G2nDGk | n > 0, k ≥0}
together with the apo-syntonic conversion θ : F →G, where θ(GkDG2n) :=
G2k+2DGn−1. Furthermore, we consider reversal map, i.e. the unique anti-auto-
morphism of rev : ⟨G, D⟩→⟨G, D⟩ﬁxing both G and D. This map rev sends
F to G and vice versa.
The following proposition speciﬁes the commutative diagram for matrices in
proposition 3.7 to the elements of the sets F and G:
Proposition 4.3. θ ◦rev ◦θ = rev.
Proof. Although the relation is a corollary of proposition 3.7 we give a direct
proof here:
θ(rev(θ(GkDG2n) = θ(rev(G2k+2DGn−1))
= θ(Gn−1DG2k+2)
= G2nDG2k+2 = rev(GkDG2n)
The third corresponding special Sturmian morphism ˜g, generating the syn-
tonic projection ˜g(a|b) of our PWWF mode has the following form:
˜g = ˜θ(f) = ˜θ(GkDG2n) = Gk ˜Gk+2DGn−1.
Thus, the morpism ˜g is preceded by precisely k + 2 conjugate morphisms in the
Zarlino ordering, namely by Gk+l ˜Gk+2−lDGn−1 for l = 1, . . . , k + 2. For the
corresponding incidence matrices we have:
Mf =
k + 1 2n(k + 1) + k
1
2n + 1

and
Mg = M˜g =
2k + 3 n(2k + 3) −1
1
n

Proposition 4.4. Consider the authentic PWWF three-letter mode
vk,n := akba|akca||(akba akca)n−1akba akc
Its apotomic, apo-syntonic and syntonic projections are πb→c(vk,n) = f(a|c),
πa→b(vk,n) = g(b|c) and πc→a(vk,n) = ˜g(a|b), respectively.


## Page 10


10
David Clampitt and Thomas Noll
Proof.
f(a|c) = GkDG2n(a|c) = GkD(a|a2nc) = Gk(ca|(ca)2nc)
= akca|(akca)2nakc = πb→c(vk,n)
g(b|c) = G2k+2DGn−1(b|c) = G2k+2D(b|bn−1c) = G2k+2(cb|(cb)n−1c)
= b2k+2cb|(b2k+2cb)n−1b2k+2c = πa→b(vk,n).
˜g(a|b) = Gk ˜Gk+2DGn−1(a|b) = Gk ˜Gk+2D(a|an−1b) = Gk ˜Gk+2(ba|(ba)n−1b),
= Gk ˜Gk+2(ba|(ba)n−1b) = Gk(bak+3|(bak+3)n−1bak+2)
= akbak+3|(akbak+3)n−1akbak+2 = πc→a(vk,n),
The subsequent proposition provides an explicit portrait of the full conjuga-
tion class of the authentic PWWF mode vk,n.
Proposition 4.5. The table below lists all letter-by-letter conjugations of the
authentic PWWF mode vk,n and characterizes them as morphic, good or bad.
The segment between the bad∗∗mode (with bad apotomic and apo-syntonic pro-
jections) and the bad∗-mode (with bad syntonic projection) is exclusively occupied
by morphic modes. The opposite segment between the bad∗-mode and the bad∗∗
mode is exclusively occupied by good modes:
akba
| akca
|| (akba akca)n−1(akba)(akc)
morphic∗∗
ak−1ba2
| ak−1ca2
|| (ak−1ba2 ak−1ca2)n−1(ak−1ba2)(ak−1ca)
morphic
. . .
ak−lbal+1 | ak−lcal+1 || (ak−lbal+1 ak−lcal+1)n−1(ak−lbal+1)(ak−lcal) morphic
. . .
bak+1
| cak+1
|| (bak+1 cak+1)n−1(bak+1)(cak)
morphic
ak+1c
| ak+1b
|| (ak+1c ak+1b)n−1(ak+1c)(akb)
morphic
. . .
cak+1
| bak+1
|| (cak+1 bak+1)n−1(cak)(bak+1)
morphic
ak+1b
| ak+1c
|| (ak+1b ak+1c)n−1(akb)(ak+1c)
morphic
. . .
bak+1
| cak+1
|| (bak+1 cak+1)n−2(bak+1 cak)(bak+1cak+1)
morphic
ak+1c
| ak+1b
|| (ak+1c ak+1b)n−2(ak+1c akb)(ak+1cak+1b)
morphic
. . .
cak+1
| bak+1
|| (cak+1 bak+1)n−2(cak bak+1)(cak+1bak+1)
morphic
ak+1b
| ak+1c
|| (ak+1b ak+1c)n−2(akb ak+1c)(ak+1bak+1c)
morphic
. . .
abak
| acak
|| bakacak(abakacak)n−1
morphic
bak+1
| cakb
|| (ak+1cak+1b)n−1ak+1cak+1
bad∗
ak+1c
| akba
|| (akcak+1ba)n−1akcak+1b
good∗
. . .
acak
| bak+1
|| (cak+1bak+1)n−1cak+1bak
good
cakb
| ak+1c
|| (ak+1bak+1c)n−1ak+1bak+1
bad∗∗
Proof. The following calculation shows that vk,n is morphic. The calculations
for the other morphic modes are analogous:


## Page 11


Pairwise Well-Formed Modes and Transformations
11
P k
baP k
caAbaPac(PcbPca)n−1PcbEab(a|b||c) = P k
baP k
caAbaPac(PcbPca)n−1Pcb(b|a||c)
= P k
baP k
caAbaPac(PcbPca)n−1(b|a||bc)
= P k
baP k
caAbaPac(b|a||(ba)n−1bc)
= P k
baP k
caAbaPac(b|a||(ba)n−1bc)
= P k
baP k
caAba(b|ca||(bca)n−1bc)
= P k
baP k
ca(ba|ca||(ba ca)n−1ba c)
= P k
ba(ba|akca||(ba akca)n−1ba akc)
= akba|akca||(akba akca)n−1akba akc
= vk,n
We try to write the good∗∗-mode γk,n = ak+1c|akba||(akcak+1ba)n−1akcak+1b
as an image f(a|b||c) under an automorphism f = fmfm−1 . . . f1f0, where the
fi(i = 1, .., m) are supposed to be productions of the type Axy or Pxy and where
f0 is letter permutation. First we observe that fm, the last of these morphisms,
cannot be a production of b’s or c’s: First of all, Abc, Acb, Pbc and Pbc are ex-
cluded because there are no letters c and b neighboring each other (even in the
case k = 0). But furthermore, not all instances of the letter a are followed or
preceded by either exclusively b or exclusively c, and so also the productions
Aac, Aab, Pac and Pac can be excluded excluded. The only remaining possibil-
ities are productions of the letter a. Among these the append-transformations
Aba and Aca both excluded, as the single-dividiver preﬁx ak+1c of γk,n ends on c
and the double-divider suﬃx (akcak+1ba)n−1akcak+1b ends on b. For k > 0 the
prepend-transformations Pba and Pca are suitable in order to produce γk,n from
shorter words. To be more precise: Pba and Pca commute with each other and
both can be applied k times in any order to the triple γ0,n = ac|ba||(caba)n−1cab
to produce γk,n. Here is one of them:
ak+1c|akba||(akcak+1ba)n−1akcak+1b = P k
ba(ak+1c|ba||(akcaba)n−1akcab)
= P k
ca(P k
ba(ac|ba||(caba)n−1cab))
A closer look at γ0,n shows that it is not an image of a shorter word-triple
under any of the 8 transformations of the type Axy or Pxy.
The similar line of argument works for any of the good modes. For 0 < l ≤k
the general form of a good mode is
aak−lcal|ak−lbala||(ak−lcalaak−lbala)n−1ak−lcalaak−lbal
= P k−l
ca (P k−l
ba (Al
ca(Al
ba(γ0,n))))
So all the good modes are images of the mode γ0,n. And this is the only
possibility to generate them from a shorter triple.
Conjecture 4.6. Consider an authentic PWWF substitution σ in the sense of
deﬁnition 3.1. The substitution σ is morphic (i.e. is a positive automorphism of
F3) iﬀits generated mode σ(a)|σ(b)||σ(c) — up to letter permutation — is an
instance of a morphic mode in proposition 4.5.


## Page 12


12
David Clampitt and Thomas Noll
5
Conclusion
Since the rise of the triad in its role as a governing concept in the music of
harmonic tonality, music theorists have been in a quandary as to how to adjust
the immemorial diatonic scale so as to be compatible with the triad’s new pri-
macy. The interval of the major third challenges the status of the perfect ﬁfth
as a scale generator, and in the course of this competition it undermines the
validity of other properties that are consequences of the ﬁfth-generatedness of
the diatonic scale, such as the well-formedness property. The concept of pair-
wise well-formedness oﬀers a reconciliation, insofar as it implements the idea
of a coexistence of three well-formed scale structures within one parent scale.
The letter projections mediate between the competing interpretations of a ﬁfth-
and a third-generated scale. The present paper oﬀers a transformational up-
grade to that earlier basic insight. Following the pattern of the investigation of
well-formed modes through automorphisms of the free group F2 it clariﬁes the
combinatorial behavior of all non-singular pairwise well-formed modes. For the
concrete case of the Ionian major mode ac|ba||cab, it turns out that the un-
derlying substitution is not an automorphism of the free group F3, which is an
exception in comparison to the Phrygian minor, Lydian major, Mixolydian ma-
jor and Aeolian minor modes. This exceptional status corresponds to the musical
fact that both, the species of major third ac and ca as well as those of the mi-
nor third ba and ab are diﬀerent. The mathematical status of the Dorian minor
mode as a bad mode has its musical counterpart in the fact that the species cbac
doesn’t form a proper ﬁfth. This fact in turn is reﬂected in the special treatment
some nineteenth-century theorists accorded the supertonic ii harmony in major,
as a sort of cousin to the diminished supertonic triad in minor.
References
1. Berth´e, V., A. de Luca, C. Reutenauer. On an involution of Christoﬀel words and
Sturmian morphisms. European Journal of Combinatorics 29/2 (2008): 535–553.
2. Clampitt, D., and T. Noll. Modes, the Height-Width Duality, and Handschin’s Tone
Character, Music Theory Online 17/1 (2011).
3. Clampitt, D. Mathematical and Musical Properties of Pairwise Well-Formed Scales.
In: Klouche, Timour and Thomas Noll (eds), Mathematics and Computation in
Music, Proceedings of the MCM 2007 in Berlin. Springer, 2007: pp. 464–468.
4. Clampitt, D. Pairwise well-formed scales: structural and transformational proper-
ties. Ph.D. diss. SUNY at Buﬀalo, 1997.
5. Carey, N., and D. Clampitt. Self-Similar Pitch Structures, Their Duals, and Rhyth-
mic Analogues, Perspectives of New Music 34/2 (1996): 62–87.
6. Carey, N., and D. Clampitt. Aspects of Well-Formed Scales, Music Theory Spectrum
11/2 (1989):187–206.
7. Lothaire, M. Algebraic combinatorics on words. Cambridge University Press, 2002.
8. Magnus, W., A. Karrass, D. Solitar. Combinatorial Group Theory. New York: Dover
Publications, 2004.
9. Nielsen, J. Die Isomorphismengruppe der freien Gruppen. Mathematische Annalen
91 (1924): 169–209.
10. Noll, T. Ionian Theorem. Journal of Mathematics and Music 3(3) (2009): 137–151.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]