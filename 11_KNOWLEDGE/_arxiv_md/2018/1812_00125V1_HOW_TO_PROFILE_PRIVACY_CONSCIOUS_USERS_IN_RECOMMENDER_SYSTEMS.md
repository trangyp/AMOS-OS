---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1812.00125v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1812.00125v1_How_to_Profile_Privacy-Conscious_Users_in_Recommender_Systems

> Source: 1812.00125v1_How_to_Profile_Privacy-Conscious_Users_in_Recommender_Systems.pdf

> Pages: 6

---


## Page 1


arXiv:1812.00125v1  [cs.CR]  1 Dec 2018
How to Proﬁle Privacy-Conscious Users in
Recommender Systems
Fabrice Benhamouda
IBM Research
Yorktown Heights, NY, USA
Marc Joye
OneSpan
Brussels, Belgium
Abstract
Matrix factorization is a popular method to build a recommender system. In such
a system, existing users and items are associated to a low-dimension vector called
a proﬁle. The proﬁles of a user and of an item can be combined (via inner product)
to predict the rating that the user would get on the item. One important issue of
such a system is the so-called cold-start problem: how to allow a user to learn her
proﬁle, so that she can then get accurate recommendations?
While a proﬁle can be computed if the user is willing to rate well-chosen items
and/or provide supplemental attributes or demographics (such as gender), reveal-
ing this additional information is known to allow the analyst of the recommender
system to infer many more personal sensitive information. We design a protocol
to allow privacy-conscious users to beneﬁt from matrix-factorization-based rec-
ommender systems while preserving their privacy. More precisely, our protocol
enables a user to learn her proﬁle, and from that to predict ratings without the user
revealing any personal information. The protocol is secure in the standard model
against semi-honest adversaries.
1
Introduction
Matrix factorization [4, 8] is a popular method to build a recommender system. As exempliﬁed
by the Netﬂix Prize competition [14], it has become a dominant technology within collaborative-
ﬁltering recommenders. Matrix factorization provides a better predictive accuracy compared to
classical neighborhood methods while at the same time is scalable and offers much ﬂexibility for
modeling a variety of real-life situations [10].
The cold-start problem.
A major problem facing collaborative-ﬁltering recommender systems is
how to provide recommendations when rating data is too sparse for a subset of users or items. As
a special case, the so-called cold-start problem [20] is how to make recommendations to new users
who have not yet rated any item or to deal with new items that have not yet been rated by users.
The cold-start problem is usually addressed by incorporating additional input sources to compensate
for the lack of rating data. In addition to ratings, the analyst may for example collect certain user
attributes, such as gender, age, or other demographic information [1, 9].
Another approach for dealing with the cold-start problem is to ask users to rate a minimum number
of (well chosen) items [18].
Inference attacks.
Relying on additional input sources to address the cold-start problem may be
difﬁcult to deploy in practice as privacy-conscious users may be reluctant to supply some of their
attributes. The second approach does not require to collect extra information beyond the ratings and
is very efﬁcient. Unfortunately, the additional received ratings may reveal a lot of information about
32nd Conference on Neural Information Processing Systems (NIPS 2018), Montréal, Canada.


## Page 2


a user to the analyst. Recent research has indeed demonstrated that this can be used by the analyst
to infer private user attributes such as political afﬁliation [11, 19], sexual orientation [11], age [22],
gender [19, 22], and even drug use [11]. Further privacy threats are reported in [2, 3, 13].
A natural question therefore raised in [7] is how a privacy-conscious user can beneﬁt from recom-
mender systems while preventing the inference of her private information.
Contributions.
In this paper, we show how a privacy-conscious user can learn her proﬁle without
revealing any information to the analyst. The protocol is practical and proven secure against semi-
honest adversaries. The communication complexity of the protocol only grows with the square-root
of the number of items.
Once the privacy-conscious user learns her proﬁle u, she can run a straightforward protocol to
learn the predicted rating of any item j in the database. This indeed only requires to compute the
inner product between the user proﬁle u (known to the user) and the item proﬁle vj (known to the
analyst) [15, Sect. 4.1].
Related work.
In [7], Ioannidis et al. propose a learning protocol which enables the user to prevent
the analyst from learning some (previously deﬁned) private user attributes. This protocol perfectly
hides these chosen attributes to the analyst, in an information-theoretic way. The authors also prove
that no such protocol can be more accurate, when the analyst ends up knowing the resulting proﬁle,
nor can disclose less information for the same accuracy.
Unfortunately, this protocol has also several drawbacks, most of them inherent to the fact it is
information-theoretically secure and does not rely on computational assumptions. First, this pro-
tocol still needs to disclose some information about the analyst database to everybody. Second, this
protocol is not as accurate as a non-privacy-preserving protocol would be. This is inherent to the
fact that Ioannidis et al. restricted themselves to protocols where the analyst learns an approximate
proﬁle of the user at the end, so that the resulting user proﬁle shall not contain any information about
the private attribute. Third, it can only hide a small ﬁxed set of attributes: all attributes which are not
explicitly hidden may be recovered by the analyst. And it may be hard for a user to decide which
attributes are really important to her, due to the wide range of possible attributes. Finally, the analyst
needs to ask users1 to reveal which attributes they deem private. This may not only bother a lot these
users, but also brings up the question of the reliability of these data. No user will be likely admitting
she is a drug addict, for example, even if she is ensured that this data will not be disclosed.2
2
Preliminaries
R is the ﬁeld of real numbers. For any integer n, Zn is the ring of integers modulo n, while Z∗
n is its
multiplicative group. Vectors are always column vectors and are denoted as u or vj. Matrices are
denoted with capital letters.
2.1
Cryptographic tools
Public-key encryption.
A public-key encryption scheme is deﬁned by three algorithms: KeyGen,
Enc, and Dec. (pk, sk) ←KeyGen(1κ) generates a matching pair of public key pk and secret key
sk, given a security parameter 1κ (unary notation). The public key pk is used to encrypt a message
x ∈M into a ciphertext c: c ←Enc(pk, x). The secret key sk is used to decrypt a ciphertext c:
x ←Dec(sk, c). We assume that the encryption scheme is perfectly correct and semantically secure
(i.e., IND-CPA) [6].
Homomorphic encryption.
An additively homomorphic encryption scheme is such that the mes-
sage set M is an additive group, and there exists a randomized operation + such that Enc(pk, x) +
1In the simplest scenario, we have to restrict to non-privacy-conscious users. But it would also be possible
to compute item proﬁles using privacy-preserving matrix factorization [15].
2Notice in particular that, in the privacy-preserving matrix factorization protocol in [15], in case of collusion
between the CSP (Crypto Service Provider) and the analyst, it is possible to recover all data sent by the user.
This means that governmental agencies may force the recommendation systems to disclose these private user
attributes.
2


## Page 3


Enc(pk, y) is distributed identically to a fresh ciphertext of x + y. This operation can be extended
to a scalar multiplication by an integer k: k  Enc(pk, x) is a fresh ciphertext of k · x; that is,
x + x + · · · + x (k times).
To simplify the notation, we will sometimes use JxKpk for Enc(pk, x) and omit pk when clear from
the context. We so have Jx + yK = JxK + JyK and Jk · xK = k  JxK.
Example 1 (Paillier encryption scheme). We recall the Paillier encryption scheme [17], which is
an homomorphic encryption scheme that is semantically secure under the Decisional Composite
Residuosity (DCR) assumption. (pk, sk) ←KeyGen(1κ) generates two large equal-length primes p
and q, computes n = pq, and sets λ = lcm(p −1, q −1) and µ = λ−1 mod n. The public key is
pk = n while the secret key is sk = (n, λ, µ). c ←Enc(pk, x) picks a uniformly random integer
ρ ←[1, n) and returns c = (1 + x n)ρn mod n2. x ←Dec(sk, c) returns x = L(cλ mod n) ·
µ mod n where L(a) = (a−1)/n. The scheme is additively homomorphic: given cx ←Enc(pk, x)
and cy ←Enc(pk, y), cx + cy = cx · cy · θn mod n2 with θ ←[1, n).
Oblivious transfer.
A 1-out-of-M oblivious transfer (OT) protocol is a cryptographic protocol
between two parties: a sender and a receiver. The receiver has an index j∗∈{1, . . ., M} as input.
The sender knows a database {xj}j=1,...,M. At the end of the protocol, the receiver learns xj∗, while
the sender learns nothing.
As in our protocol M is the number of items in the database, we need to use practical OT protocols
with communication complexity sublinear in M. We propose to use as 1-out-of-M OT the basic PIR
(Private Information Retrieval) protocol in [16, Sect. 2.2] using the Paillier homomorphic encryption
scheme, together with a classical 1-out-of-
√
M OT [12] which is used to mask the PIR database. The
resulting OT has two rounds (one message from the receiver to the sender followed by one message
from the sender to the receiver) and its communication complexity is proportional to
√
M.
2.2
Matrix factorization
The goal of matrix factorization is to predict unobserved ratings ri,j for some user i and some item j,
given access to a set D of user/item pairs (i, j) for which a rating ri,j ∈R has been generated. Matrix
factorization provides d-dimensional vectors ui, vj ∈Rd such that
ri,j ≈ˆri,j := ⟨ui, vj⟩=
d
X
k=1
ui,k vj,k
for (i, j) ∈D .
(1)
This allows the analyst to predict missing ratings (i.e., those with (i, j) /∈D). Vector ui is referred
to as the proﬁle of user i while vector vj as the proﬁle of item j.
2.3
Learning the proﬁle of a user
Speciﬁcally, when a new user wishes to use the service, she submits a batch of s ratings {rj}j∈S
for a subset S of s ≥d items. Upon receiving these ratings, the analyst can estimate her proﬁle u
through the following least-squares estimation,3
arg min
u∈Rd
X
j∈S
 rj −⟨u, vj⟩
2 ,
(2)
and subsequently predict ratings for items j /∈S, using Eq. (1).
Deﬁning matrix VS = ( vj1
. . .
vjs ) ∈Rd×s and column vector r = (rj1, . . . , rjs)⊺∈Rs,
the proﬁle u of a user can be computed as follows:
u = (VS · V ⊺
S )−1 · VS · r =
 s
X
k=1
vjk · v⊺
jk
!−1
·
 s
X
k=1
rjk · vjk
!
.
(3)
3To ease the presentation, linear regression is considered but the proposed techniques readily apply to the
more general setting of ridge regression.
3


## Page 4


3
Our learning protocol
We design a two-round learning protocol between a privacy-conscioususer i and an analyst, allowing
the user to learn her proﬁle u from her (private) ratings {rj}j∈S, where S = {j1, . . . , js}. At the
end of the protocol, the analyst will learn nothing (except the size s of S), while the user will only
learn her proﬁle u and nothing else about the analyst database (except the dimension d, the database
of items and its size M, and bounds Br and Bv on entries of ratings rj and of proﬁles of items vj,
respectively).
We insist that our protocol hides the set of actual items S that the user is rating as they might already
leak signiﬁcant information about her. If an upper bound S on |S| is known, the exact size s of S
can trivially be masked by adding fake items (with proﬁle 0 and fake rating 0) so that the protocol
always uses a set S of size S.
3.1
Protocol
Consider the ring Zn. We assume that n is either a prime or is hard to factor, so that for all intents
and purposes Zn behaves as a ﬁeld (since a non-zero non-invertible element of Zn would yield a
factor of n). Up to using ﬁxed point arithmetic (e.g., by multiplying values by some integer 2ℓ), we
suppose that the entries of VS and r are integers, and so can be considered as elements of Zn.
Round 1.
The user generates a key pair (pk, sk) ←KeyGen(1κ) for the homomorphic encryption
scheme and encrypts her ratings rjk: ck ←JrjkK for 1 ≤k ≤s. She also initiates s independent
OT protocols as a receiver with respective selection indexes j1, . . . , js.
Round 2.
The analyst generates and computes the following matrices (over Zn and over the ci-
phertext space respectively):4
Ak,j = R0 · vj · v⊺
j + Rk ,
Jαk,jK = (R0 · vj)  ck + JρkK ,
where {Rk}1≤k≤s and {ρk}1≤k≤s are uniformly random matrices and vectors summing up to zero
in Zd×d
n
and Zd
n respectively, and R0 is a uniform matrix in GL(d, Zn) (the group of invertible
matrices in Zd×d
n
).
The analyst then answers the k-th OT message from the user, as an OT sender with database

xk,j =
(Ak,j, Jαk,jK)
	
1≤j≤M.
Final step.
The user receives xk,jk = (Ak,jk, Jαk,jkK) through the OT protocols. We write Ak =
Ak,jk and αk = Dec(sk, Jαk,jkK). We then remark that, in Zn:
(VS · V ⊺
S )−1 · VS · r =
 s
X
k=1
Ak
!−1
·
 s
X
k=1
αk
!
.
So if n is large enough, the user can compute back u using rational reconstruction [21, 5] (we recall
that u satisﬁes Eq. (3) over the rationals, and that u is not necessarily an integer).
Bounds for correctness.
The scheme is correct when the above rational reconstruction suc-
ceeds.
From [21, 5] and Hadamard’s inequality, we can show correctness when n
>
2dd+1/2s2d+1B4d+1
V
Br, where BV and Br are upper bounds on the absolute values of the coefﬁ-
cients of the item proﬁles vj and of the ratings rj, respectively. For example, if BV = 220, Br = 4,
d = 8, s = 10, this is already satisﬁed for an integer n of 806 bits.
Security.
Security against semi-honest adversaries follows from the security of the OT protocol,
the IND-CPA property of the homomorphic encryption scheme, and from the following fact: since
VS · V ⊺
S is invertible and GL(d, Zn) is a group, {Ak}k and {αk}k only reveal u.
4We slightly abuse notation here. For vectors, the bracket notation and + and  operators are applied
component-wise.
4


## Page 5


3.2
Instantiation using Paillier homomorphic encryption scheme
The scheme can be instantiated using the Paillier encryption scheme and the OT described in Sec-
tion 2. We can use the internal construction of the OT, to avoid sending ciphertexts of rjk. Con-
cretely, in the OT construction, the user encrypts a vector (0, . . . , 1, . . . , 0) used to “select” the
correct value to be received. If we use two OT protocols for each k, one for Ak and one for αk
(instead of a single one for the pair (Ak, αk)), then for the second OT, the user just encrypts rjk
instead of 1, she will receive rjk times the value to be received.
The resulting protocol for M = 100 items, dimension d = 8, and s = 10 ratings from the user
(modulus n of size 1024 bits for Paillier encryption scheme and an elliptic curve over a 256-bit
prime ﬁeld for the base OT [12]), has the following performance on a non-optimized single-thread
implementation (on a laptop, CPU Intel® i7-7567U, 3.5GHz, turbo 4GHz): less than 0.4s to gener-
ate the ﬁrst round by the user, less than 150s to generate the second round by the analyst, less than
1.4s to ﬁnalize the protocol by the user. The user requires less than 2s of computation (excluding
communication). The analyst time is mostly spent in the exponentiations required in the OT protocol
(modulo n2): there are M · (d2 + d) · s of them. These exponentiations can be trivially parallelized.
The communication complexity is less than 2MB and essentially grows linearly with
√
M.
References
[1] Gediminas Adomavicius and Alexander Tuzhilin. Toward the next generation of recommender
systems: A survey of the state-of-the-art and possible extensions. IEEE Transactions on Knowl-
edge and Data Engineering, 17(6):734–749, June 2005.
[2] Smriti Bhagat, Udi Weinsberg, Stratis Ioannidis, and Nina Taft.
Recommending with an
agenda: Active learning of private attributes using matrix factorization. In Alfred Kobsa et al.,
editors, 8th ACM Conference on Recommender Systems (RecSys 2014), pages 65–72. ACM
Press, October 2014.
[3] Joseph A. Calandrino, Ann Kilzer, Arvind Narayanan, Edward W. Felten, and Vitaly
Shmatikov. “You Might Also Like:” Privacy risks of collaborative ﬁltering. In 2011 IEEE
Symposium on Security and Privacy (S&P 2011), pages 231–246. IEEE Press, May 2011.
[4] Emmanuel J. Candès and Benjamin Recht. Exact matrix completion via convex optimization.
Foundations of Computational Mathematics, 9(6):717–772, 2009.
[5] Pierre-Alain Fouque, Jacques Stern, and Jan-Geert Wackers. Cryptocomputing with rationals.
In Matt Blaze, editor, 6th International Conference on Financial Cryptography (FC 2002),
volume 2357 of LNCS, pages 136–146. Springer, March 2003.
[6] ShaﬁGoldwasser and Silvio Micali. Probabilistic encryption. Journal of Computer and System
Sciences, 28(2):270–299, 1984.
[7] Stratis Ioannidis, Andrea Montanari, Udi Weinsberg, Smriti Bhagat, Nadia Fawaz, and Nina
Taft. Privacy tradeoffs in predictive analytics. In Sujay Sanghavi et al., editors, 2014 Interna-
tional Conference on Measurement and Modeling of Computer Systems (SIGMETRICS 2014),
pages 57–69. ACM Press, June 2014.
[8] Raghunandan H. Keshavan, Andrea Montanari, and Sewoong Oh. Learning low rank matrices
from O(n) entries. In 46th Annual Allerton Conference on Communication, Control, and
Computing, pages 1365–1372. IEEE Press, September 2008.
[9] Yehuda Koren. Factorization meets the neighborhood: A multifaceted collaborative ﬁltering
model. In Ying Li, Bing Liu, and Sunita Sarawagi, editors, 14th ACM International Conference
on Knowledge Discovery and Data Mining (KDD 2008), pages 426–434. ACM Press, August
2008.
[10] Yehuda Koren, Robert Bell, and Chris Volinsky. Matrix factorization techniques for recom-
mender systems. Computer, 42(8):30–37, August 2009.
[11] Michal Kosinskia, David Stillwella, and Thore Graepel. Private traits and attributes are pre-
dictable from digital records of human behavior. Proceedings of the National Academy of
Sciences of the United States of America, 110(15):5802–5805, April 2013.
5


## Page 6


[12] Moni Naor and Benny Pinkas. Efﬁcient oblivious transfer protocols. In S. Rao Kosaraju, editor,
12th Annual Symposium on Discrete Algorithms (SODA 2001), pages 448–457. ACM-SIAM,
January 2001.
[13] Arvind Narayanan and Vitaly Shmatikov. Robust de-anonymization of large sparse datasets.
In 2008 IEEE Symposium on Security and Privacy (S&P 2008), pages 111–125. IEEE Press,
May 2008.
[14] Netﬂix Prize. http://www.netflixprize.com/.
[15] Valeria Nikolaenko, Stratis Ioannidis, Udi Weinsberg, Marc Joye, Nina Taft, and Dan Boneh.
Privacy-preserving matrix factorization. In Ahmad-Reza Sadeghi, Virgil D. Gligor, and Moti
Yung, editors, 20th ACM Conference on Computer and Communications Security (ACM-CCS
2013), pages 801–812. ACM Press, November 2013.
[16] Rafail Ostrovsky and William E. Skeith III. A survey of single-database private information
retrieval: Techniques and applications (invited talk). In Tatsuaki Okamoto and Xiaoyun Wang,
editors, 10th International Conference on Practice and Theory in Public-Key Cryptography
(PKC 2007), volume 4450 of LNCS, pages 393–411. Springer, April 2007.
[17] Pascal Paillier.
Public-key cryptosystems based on composite degree residuosity classes.
In Jacques Stern, editor, 18th Annual International Conference on the Theory and Applica-
tions of Cryptographic Techniques (EUROCRYPT ’99), volume 1592 of LNCS, pages 223–238.
Springer, May 1999.
[18] Al Mamunur Rashid, Istvan Albert, Dan Cosley, Shyong K. Lam, Sean M. McNee, Joseph A.
Konstan, and John Riedl. Getting to know you: Learning new user preferences in recommender
systems. In 7th International Conference on Intelligent User Interfaces, pages 127–134. ACM
Press, January 2002.
[19] Salman Salamatian, Amy Zhang, Flávio du Pin Calmon, Sandilya Bhamidipati, Nadia Fawaz,
Branislav Kveton, Pedro Oliveira, and Nina Taft. How to hide the elephant –or the donkey–
in the room: Practical privacy against statistical inference for large data. In IEEE Global
Conference on Signal and Information Processing (GlobalSIP 2013), pages 269–272. IEEE
Press, December 2013.
[20] Andrew I. Schein, Alexandrin Popescul, Lyle H. Ungar, and David M. Pennock. Methods
and metrics for cold-start recommendations. In 25th Annual International ACM Conference
on Research and Development in Information Retrieval, pages 253–260. ACM Press, August
2002.
[21] Paul S. Wang, M. J. T. Guy, and James H. Davenport. P-adic reconstruction of rational num-
bers. SIGSAM Bull., 16(2):2–3, May 1982.
[22] Udi Weinsberg, Smriti Bhagat, Stratis Ioannidis, and Nina Taft. BlurMe: Inferring and obfus-
cating user gender based on ratings. In Padraig Cunningham et al., editors, 6th ACM Confer-
ence on Recommender Systems (RecSys 2012), pages 195–202. ACM Press, September 2012.
6

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1812_00125v1_how_to_profile_privacy_conscious_users_in_recommender_systems
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1812_00125V1_HOW_TO_PROFILE_PRIVACY_CONSCIOUS_USERS_IN_RECOMMENDER_SYSTEMS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
