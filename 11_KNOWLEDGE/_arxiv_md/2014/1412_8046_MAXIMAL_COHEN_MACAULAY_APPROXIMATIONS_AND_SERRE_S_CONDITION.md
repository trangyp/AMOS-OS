---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1412.8046
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1412.8046_Maximal_Cohen-Macaulay_approximations_and_Serre_s_condition

> Source: 1412.8046_Maximal_Cohen-Macaulay_approximations_and_Serre_s_condition.pdf

> Pages: 7

---


## Page 1


arXiv:1412.8046v1  [math.AC]  27 Dec 2014
MAXIMAL COHEN–MACAULAY APPROXIMATIONS
AND SERRE’S CONDITION
HIROKI MATSUI AND RYO TAKAHASHI
Dedicated to Professor Ngo Viet Trung on the occasion of his sixtieth birthday
Abstract. This paper studies the relationship between Serre’s condition (Rn) and
Auslander–Buchweitz’s maximal Cohen–Macaulay approximations.
It is proved that
a Gorenstein local ring satisﬁes (Rn) if and only if every maximal Cohen–Macaulay
module is a direct summand of a maximal Cohen–Macaulay approximation of a (Cohen–
Macaulay) module of codimension n + 1.
1. Introduction
In the 1980s, Auslander and Buchweitz [2] introduced the notion of a maximal Cohen–
Macaulay approximation of a ﬁnitely generated module over a Cohen–Macaulay local ring
with a canonical module, which has been playing a fundamental role in the representation
theory of Cohen–Macaulay rings. Several years ago Kato [6] gave the following character-
ization theorem of Gorenstein local rings by maximal Cohen–Macaulay approximations.
We abbreviate Cohen–Macaulay to CM and maximal Cohen–Macaulay to MCM.
Theorem 1.1 (Kato). Let R be a d-dimensional Gorenstein local ring.
(1) The following are equivalent for d ≥1.
(a) R is a domain.
(b) Every MCM R-module is a MCM approximation of a (CM) R-module of codimen-
sion 1.
(2) The following are equivalent for d ≥2.
(a) R is a unique factorization domain.
(b) Every MCM R-module is a MCM approximation of a (CM) R-module of codimen-
sion 2.
It is natural to ask what happens if in the statements (b) of the above theorem we
weaken the condition of being a MCM approximation to that of being a direct summand
of a MCM approximation. The main purpose of this paper is to answer this question in
more general settings. Our main results yield the following theorem.
Theorem 1.2. Let R be a d-dimensional Gorenstein local ring. The following are equiv-
alent for each 0 ≤c ≤d.
Date: September 4, 2014.
2010 Mathematics Subject Classiﬁcation. 13C14, 13H10.
Key words and phrases. Cohen–Macaulay ring, Gorenstein ring, maximal Cohen–Macaulay module,
maximal Cohen–Macaulay approximation, Serre’s condition, nonfree locus, singular locus, syzygy, trans-
pose.
RT was partly supported by JSPS Grant-in-Aid for Scientiﬁc Research (C) 25400038.
1


## Page 2


2
HIROKI MATSUI AND RYO TAKAHASHI
(1) R satisﬁes Serre’s condition (Rc−1).
(2) Every MCM R-module is a direct summand of a c-th syzygy of a (CM) R-module of
codimension c.
(3) Every MCM R-module is a direct summand of a MCM approximation of a (CM)
R-module of codimension c.
Letting c = 1, 2 in the above theorem, we obtain the following result which is analogous
to Kato’s theorem. This gives the answer to the question raised above.
Corollary 1.3. Let R be a d-dimensional Gorenstein local ring.
(1) The following are equivalent for d ≥1.
(a) R is reduced.
(b) Every MCM R-module is a direct summand of a MCM approximation of a (CM)
R-module of codimension 1.
(2) The following are equivalent for d ≥2.
(a) R is normal.
(b) Every MCM R-module is a direct summand of a MCM approximation of a (CM)
R-module of codimension 2.
This paper is organized as follows. In Section 2, we consider over a CM local ring the
condition that all MCM modules are direct summands of syzygies of certain modules. In
Section 3, we study over a Gorenstein local ring the condition that all MCM modules are
direct summands of MCM approximations of certain modules. The proof of Theorem 1.2
is given at the end of this section.
2. MCM modules that are direct summands of syzygies
Throughout this paper, let R be a commutative Cohen–Macaulay local ring of Krull
dimension d. All R-modules are assumed to be ﬁnitely generated.
Let us begin with recalling some basic deﬁnitions.
Deﬁnition 2.1. (1) For an integer n ≥0 we denote by ΩnM an n-th syzygy of M, that
is, the image of the n-th diﬀerential map in a free resolution of M.
(2) For an integer n ≥−1 we say that R satisﬁes Serre’s condition (Rn) if the local ring
Rp is regular for all prime ideals p of R with ht p ≤n.
(3) The singular locus Sing R of R is by deﬁnition the set of prime ideals p of R such that
the local ring Rp is nonregular.
(4) Let M be an R-module. The nonfree locus NF(M) (respectively, the inﬁnite projective
dimension locus IPD(M)) of M is deﬁned as the set of prime ideals p of R such that the
Rp-module Mp is nonfree (respectively, is of inﬁnite projective dimension).
(5) Let V be a closed subset of Spec R. Then we set codim V = d −dim V and call this
the codimension of V . The codimension codim M of an R-module M is deﬁned as the
codimension of Supp M, whence codim M = d −dim M.
Remark 2.2. (1) If X, Y are n-th syzygies of an R-module M, then X ⊕F ∼= Y ⊕G for
some free R-modules F, G.
(2) By deﬁnition R always satisﬁes (R−1).


## Page 3


MCM APPROXIMATIONS AND SERRE’S CONDITION
3
(3) It is well-known and easy to see that the nonfree locus and the inﬁnite projective
dimension locus of an R-module are always closed subsets of Spec R in the Zariski topology.
(4) If M is a MCM R-module, then NF(M) is contained in Sing R.
In the following proposition we study how to represent each MCM module as a direct
summand of a syzygy of a certain CM module. This result will become a basis of our
main results.
Proposition 2.3. Let M be a MCM R-module. Then for each integer 0 ≤c ≤codim NF(M)
there exists a CM R-module N such that
(1) codim N = c,
(2) IPD(N) = NF(M) and
(3) M is isomorphic to a direct summand of a c-th syzygy of N.
Proof. By virtue of [5, Remark 5.2(1)], there exists an ideal I of R with NF(M) = V(I)
such that I · Exti
R(M, X) = 0 for all integers i > 0 and all R-modules X. As
dim NF(M) = dim R/I = d −ht I,
we have ht I = codim NF(M) ≥c, and can take an R-sequence x = x1, . . . , xc in I. Setting
N = M/xM, we see from [7, Proposition 2.2] that M is isomorphic to a direct summand
of ΩcN. The condition (3) is thus satisﬁed, and it is observed that N is a CM R-module
with codim N = d −dim N = c.
Now it remains to verify that N satisﬁes the condition (2). Fix a prime ideal p in the
union IPD(N)∪NF(M). Then it is easily observed that p contains the sequence x. Hence
by [3, Exercise 1.3.6] the equalities
pdRp Np = pdRp Mp/xMp = pdRp Mp + c
hold. This shows that the Rp-module Np has inﬁnite projective dimension if and only if
so does Mp. Since M is a MCM R-module, the Auslander–Buchsbaum formula implies
IPD(M) = NF(M). Therefore we obtain IPD(N) = NF(M).
■
As an immediate consequence of the above proposition, the following holds.
Corollary 2.4. Let M be a MCM R-module whose nonfree locus has dimension n. Then
there exists a CM R-module N of dimension n such that M is isomorphic to a direct
summand of Ωd−nN.
Proof. We have codim NF(M) = d −n. Apply Proposition 2.3 to c := d −n.
■
Applying the above corollary to n = 0, we obtain the following result, which recovers
[7, Corollary 2.6].
Corollary 2.5. Let M be a MCM R-module which is locally free on the punctured spec-
trum of R. Then there exists an R-module N of ﬁnite length such that M is isomorphic
to a direct summand of ΩdN.
Next we establish a criterion for R to satisfy Serre’s condition (Rn) in terms of the
codimensions of the nonfree loci of MCM R-modules.
Proposition 2.6. The following are equivalent for each 0 ≤c ≤d.


## Page 4


4
HIROKI MATSUI AND RYO TAKAHASHI
(1) The ring R satisﬁes (Rc−1).
(2) One has codim Sing R ≥c.
(3) One has codim NF(M) ≥c for all MCM R-modules M.
Proof. (1) ⇒(2): Let p be a prime ideal in Sing R. As R satisﬁes (Rc−1), the height of p
is at least c, whence dim R/p ≤d −c. Therefore dim Sing R ≤d −c, which means that
Sing R has codimension at least c.
(2) ⇒(3): Since NF(M) is contained in Sing R, we have dim NF(M) ≤dim Sing R.
Hence the (in)equalities
codim NF(M) = d −dim NF(M) ≥d −dim Sing R = codim Sing R ≥c
follow.
(3) ⇒(1): Let p be a prime ideal of R with ht p ≤c−1. Let M be a d-th syzygy of the R-
module R/p. Then M is a MCM R-module, and by assumption we have codim NF(M) ≥c,
or equivalently,
dim NF(M) ≤d −c.
Suppose that Rp is not regular. Then the Rp-module Mp is not free, for it is a d-th syzygy
of the Rp-module κ(p). Hence p belongs to NF(M), and there are inequalities
dim NF(M) ≥dim R/p ≥d −c + 1.
This contradiction shows that Rp is regular.
■
Let us now state and prove the main result of this section, which characterizes CM
local rings satisfying Serre’s (Rn)-condition.
Theorem 2.7. For every integer 0 ≤c ≤d the following are equivalent.
(1) The ring R satisﬁes (Rc−1).
(2) Every MCM R-module is isomorphic to a direct summand of a c-th syzygy of a CM
R-module of codimension c.
(3) Every MCM R-module is isomorphic to a direct summand of some syzygy of an R-
module of codimension at least c.
Proof. Propositions 2.3 and 2.6 show that (1) implies (2), and it is obvious that (2) implies
(3). Assume that (3) holds, and take any MCM R-module M. By assumption, there are
an R-module N with codim N ≥c and an integer b ≥0 such that M is isomorphic to
a direct summand of ΩbN. Then we have inclusions NF(M) ⊆NF(ΩbN) ⊆Supp N of
closed subsets of Spec R, which implies
dim NF(M) ≤dim NF(ΩbN) ≤dim Supp N = dim N ≤d −c.
Hence NF(M) has codimension at least c, and it is deduced from Proposition 2.6 that R
satisﬁes (Rc−1).
■
3. MCM modules that are direct summands of MCM approximations
Throughout this section, our ring R is further assumed to be Gorenstein. The following
is a celebrated result due to Auslander and Buchweitz [2, Theorem 1.8].


## Page 5


MCM APPROXIMATIONS AND SERRE’S CONDITION
5
Theorem 3.1 (Auslander–Buchweitz). For each R-module M there exists an exact se-
quence
(3.1.1)
0 →Y →X →M →0
of R-modules such that X is MCM and Y has ﬁnite projective dimension.
Deﬁnition 3.2. A MCM R-module X admitting an exact sequence of the form (3.1.1)
is called a MCM approximation of M.
For an R-module M we denote by TrM the (Auslander) transpose of M, that is, the
cokernel of the R-dual of the ﬁrst diﬀerential map in a free resolution of M. We denote by
MCM(R) the stable category of MCM R-modules. This is deﬁned as follows: the objects
of MCM(R) are precisely the MCM R-modules, and the hom-set HomMCM(R)(M, N) of
objects M, N in MCM(R) is the quotient of HomR(M, N) by the R-submodule consisting of
homomorphisms factoring through free R-modules. Since R is assumed to be Gorenstein,
MCM(R) is a triangulated category, and taking a syzygy and a transpose deﬁnes an
autoequivalence and a duality of MCM(R), respectively.
Ω: MCM(R)
∼
=−→MCM(R),
Tr : MCM(R)
∼
=−→MCM(R)op.
For details, we refer the reader to [1] and [4].
One can describe a MCM approximation by using syzygies and transposes:
Lemma 3.3. For any R-module M, the R-module
TrΩnTrΩnM
is a MCM approximation of M for all n ≥d −depth M.
Proof. Note that ΩnM is a MCM R-module. Since both Ωand Tr preserve the MCM
property, the R-module X = TrΩnTr(ΩnM) is also a MCM module. It follows from [1,
Proposition (2.21) and Corollary (4.22)] that there exists an exact sequence
(3.3.1)
0 →K →X →M →0
of R-modules such that K has projective dimension at most n −1. Consequently, X is a
MCM approximation of M.
■
A MCM approximation version of Corollary 2.4 also holds true:
Proposition 3.4. (1) Let M be a MCM R-module with n-dimensional nonfree locus.
Then there exists an n-dimensional CM R-module N such that M is isomorphic to a
direct summand of a MCM approximation of N.
(2) Let M be a MCM R-module that is locally free on the punctured spectrum of R. Then
there exists an R-module N of ﬁnite length such that M is isomorphic to a direct
summand of a MCM approximation of N.
Proof. (1) It is easy to see that NF(Ωd−nM) coincides with NF(M). Applying Corollary
2.4 to the MCM module Ωd−nM, we ﬁnd a CM module N of dimension n such that


## Page 6


6
HIROKI MATSUI AND RYO TAKAHASHI
Ωd−nM is isomorphic to a direct summand of Ωd−nN. Taking TrΩd−nTr yields that M is
isomorphic to a direct summand of
X := TrΩd−nTrΩd−nN ⊕F
for some free R-module F. Using Lemma 3.3, we easily see that X is a MCM approxi-
mation of N.
(2) The assertion follows from applying (1) to n = 0.
■
The main result of this section is the following characterization of Gorenstein local rings
satisfying Serre’s condition (Rn). This result can be viewed as a MCM approximation
version of Theorem 2.7.
Theorem 3.5. The following are equivalent for each 0 ≤c ≤d.
(1) R satisﬁes (Rc−1).
(2) Every MCM R-module is isomorphic to a direct summand of a MCM approximation
of a CM R-module of codimension c.
(3) Every MCM R-module is isomorphic to a direct summand of a MCM approximation
of an R-module of codimension at least c.
Proof. (1) ⇒(2): Let M be a MCM R-module. Using Theorem 2.7 for the MCM R-
module ΩcM, we get a CM R-module N of codimension c such that ΩcM is isomorphic to
a direct summand of ΩcN. Then applying TrΩcTr to this relation shows that TrΩcTrΩcM
is isomorphic to a direct summand of X := TrΩcTrΩcN up to free summands. By Lemma
3.3 the module X is a MCM approximation of N. Since we have a duality
TrΩc : MCM(R)
∼
=−→MCM(R),
the R-module TrΩcTrΩcM is isomorphic to M up to free summands. Therefore M is
isomorphic to a direct summand of X ⊕F for some free R-module F. It is easy to see
that X ⊕F is also a MCM approximation of N.
(2) ⇒(3): This implication is obvious.
(3) ⇒(1): Let M be a MCM R-module. Then N := TrΩdTrM is also a MCM R-
module. Applying the condition (3) to N, we observe that there exists an R-module L
of codimension at least c such that N is isomorphic to a direct summand of a MCM
approximation X of L. It follows from [2, Theorem B] and Lemma 3.3 that the R-module
X is isomorphic to TrΩdTrΩdL up to free summands. The functor
TrΩdTr : MCM(R)
∼
=−→MCM(R)
is an equivalence, so we see that M is isomorphic to a direct summand of ΩdL up to free
summands. Thus Theorem 2.7 implies that R satisﬁes Serre’s condition (Rc−1).
■
Proof of Theorem 1.2. The assertion follows by combining Theorems 2.7 and 3.5.
■
Acknowlegments. The authors are grateful to Olgur Celikbas for his helpful comments.
The authors also thank the referee for his/her careful reading.


## Page 7


MCM APPROXIMATIONS AND SERRE’S CONDITION
7
References
[1] M. Auslander; M. Bridger, Stable module theory, Mem. Amer. Math. Soc. No. 94, American
Mathematical Society, Providence, R.I., 1969.
[2] M. Auslander; R.-O. Buchweitz, The homological theory of maximal Cohen–Macaulay approx-
imations, Colloque en l’honneur de Pierre Samuel (Orsay, 1987), M´em. Soc. Math. France (N.S.)
No. 38 (1989), 5–37.
[3] W. Bruns; J. Herzog, Cohen–Macaulay rings, revised edition, Cambridge Studies in Advanced
Mathematics, 39, Cambridge University Press, Cambridge, 1998.
[4] R.-O. Buchweitz, Maximal Cohen-Macaulay modules and Tate-cohomology over Gorenstein rings,
Preprint (1986), http://hdl.handle.net/1807/16682.
[5] H. Dao;
R.
Takahashi,
The dimension of a subcategory of modules,
Preprint (2012),
arXiv:1203.1955v2.
[6] K. Kato, Syzygies of modules with positive codimension, J. Algebra 318 (2007), no. 1, 25–36.
[7] R. Takahashi, Classifying thick subcategories of the stable category of Cohen–Macaulay modules,
Adv. Math. 225 (2010), no. 4, 2076–2116.
Graduate School of Mathematics, Nagoya University, Furocho, Chikusaku, Nagoya,
Aichi 464-8602, Japan
E-mail address: m14037f@math.nagoya-u.ac.jp
Graduate School of Mathematics, Nagoya University, Furocho, Chikusaku, Nagoya,
Aichi 464-8602, Japan
E-mail address: takahashi@math.nagoya-u.ac.jp
URL: http://www.math.nagoya-u.ac.jp/~takahashi/

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1412_8046_maximal_cohen_macaulay_approximations_and_serre_s_condition
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2014/1412_8046_MAXIMAL_COHEN_MACAULAY_APPROXIMATIONS_AND_SERRE_S_CONDITION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
