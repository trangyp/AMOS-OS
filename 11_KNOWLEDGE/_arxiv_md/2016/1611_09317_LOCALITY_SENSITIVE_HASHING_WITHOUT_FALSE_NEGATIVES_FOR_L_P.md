---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1611.09317
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1611.09317_Locality-Sensitive_Hashing_without_False_Negatives_for_l_p

> Source: 1611.09317_Locality-Sensitive_Hashing_without_False_Negatives_for_l_p.pdf

> Pages: 11

---


## Page 1


arXiv:1611.09317v1  [cs.DS]  28 Nov 2016
Locality-Sensitive Hashing without False Negatives for lp
Andrzej Pacuk∗
Piotr Sankowski∗
Karol Wegrzycki∗
Piotr Wygocki∗
[apacuk,sank,k.wegrzycki,wygos]@mimuw.edu.pl
Abstract
In this paper, we show a construction of locality-sensitive hash functions without false negatives, i.e.,
which ensure collision for every pair of points within a given radius R in d dimensional space equipped with
lp norm when p ∈[1, ∞]. Furthermore, we show how to use these hash functions to solve the c-approximate
nearest neighbor search problem without false negatives. Namely, if there is a point at distance R, we will
certainly report it and points at distance greater than cR will not be reported for c = Ω(
√
d, d1−1
p ). The
constructed algorithms work:
• with preprocessing time O(n log(n)) and sublinear expected query time,
• with preprocessing time O(poly(n)) and expected query
time O(log(n)).
Our paper reports progress on answering the open problem presented by Pagh [8], who considered the nearest
neighbor search without false negatives for the Hamming distance.
1
Introduction
The Nearest Neighbor problem is of major importance to a variety of applications in machine learning and
pattern recognition. Ordinarily, points are embedded in Rd, and distance metrics usually measure similarity
between points. Our task is the following: given a preprocessed set of points S ⊂Rd and a query point q ∈Rd,
ﬁnd the point v ∈S, with the minimal distance to q. Unfortunately, the existence of an eﬃcient algorithm
(i.e., whose query and preprocessing time would not depend exponentially on d), would disprove the strong
exponential time hypothesis [8, 10]. Due to this fact, we consider the c-approximate nearest neighbor problem:
given a distance R, a query point q and a constant c > 1, we need to ﬁnd a point within distance cR from point
q [4]. This point is called a cR-near neighbor of q.
Deﬁnition 1. Point v is an r-near neighbor of q in metric M iﬀM(q, v) ≤r.
One of the most interesting methods for solving the c-approximate nearest neighbor problem in high-
dimensional space is locality-sensitive hashing (LSH). The algorithm oﬀers a sub-linear query time and a
sub-quadratic space complexity. The rudimentary component on which LSH method relies is locality-sensitive
hashing function. Intuitively, a hash function is locality-sensitive if the probability of collision is much higher
for “nearby” points than for “far apart” ones. More formally:
Deﬁnition 2. A family H = {h : S →U} is called (r, c, p1, p2)-sensitive for distance D and induced ball
B(q, r) = {v : D(q, v) < r}, if for any v, q ∈S:
• if v ∈B(q, r) then P [h(q) = h(v)] ≥p1,
• if v /∈B(q, cr) then P [h(q) = h(v)] ≤p2.
For p1 > p2 and c > 1.
Indyk and Motwani [7] considered randomized c-approximate R-near neighbor (Deﬁnition 3).
Deﬁnition 3 (The randomized c-approximate R-near neighbor or (R,c)-NN ). Given a set of points in a P ⊂Rd
and parameters R > 0, δ > 0. Construct a data structure D such that for any query point q, if there exists a
R-near neighbor of q in P, D reports some cR-near neighbor of q in P with probability 1 −δ.
∗Institute of Informatics, University of Warsaw, Poland
1


## Page 2


In this paper, we study guarantees for LSH based (R,c)-NN such that for each query point q, every close
enough point ∥x −q∥p < R will be certainly returned, i.e., there are no false negatives.1 In other words, given
a set S of size n and a query point q, the result is a set P ⊆S such that:
{x : ∥x −q∥p < r} ⊆P ⊆{x : ∥x −q∥p ≤cr}.
Moreover, for each distant point (∥x−q∥p > cR), the probability of being returned is bounded by pfp– probability
of false positives. In [8] this type of LSH is called LSH without false negatives. The fact that the probability of
false negatives is 0 is our main improvement over Indyk and Motwani algorithm [7]. Furthermore, Indyk and
Motwani showed that p-stable distributions (where p ∈(0, 2]) are (r, c, p1, p2)-sensitive for lp. We generalized
their results on any distribution with mean 0, bounded second and fourth moment and any p ∈[1, ∞] (see
Lemma 1, for rigorous deﬁnitions). Finally, certain distributions from this abundant class guarantee that points
within given radius will always be returned (see Figure 1). Unfortunately, our results come with a price, namely
c ≥max{
√
d, d1−1/p}.
R
√
dR
cR
q
•p1
•p3
•p2
•p4
Figure 1: The presented algorithms guarantee that points in the dashed area (p1) will be reported as neighbors.
Points within the dotted circle (p2) will be reported as neighbor with high probability. Points (p3) within a
distance cR might be reported, but not necessarily. Points (p4) outside circle cR cannot be reported. The
schema picture presents an example for the euclidean distance (p = 2).
2
Related Work
2.1
Nearest neighbor in high dimensions
Most common techniques for solving the approximate nearest neighbor search, such as the spatial indexes or k-d
trees [3] are designed to work well for the relatively small number of dimensions. The query time for k-d trees is
O(n1−1
d ) and when the number of dimensions increases the complexity basically converges to O(n). For interval
trees, query time O(logd n) depends exponentially on the number of dimensions. The major breakthrough was
the result of Indyk and Motwani [7]. Their algorithm has expected complexity of O(dn
1
c ) for any approximation
constant c > 1 and the complexity is tight for any metric lp (where p ∈(0, 2]). Indyk and Motwani introduced
the following LSH functions:
h(v) =
⟨a, v⟩+ b
r

,
where a is the d-dimensional vector of independent random variables from a p-stable distribution and b is a real
number chosen uniformly from the range [0, r].
Our algorithm is based on similar functions and we prove compelling results for more general family of
distributions (we show bounds for any distribution with a bounded variance and an expected value equal to
0). Furthermore, our algorithm is correct for any p ∈[1, ∞]. Indyk and Motwani‘s LSH algorithm was showed
to be optimal for l1 metric. Subsequently, Andoni et al. [1] showed near optimal results for l2. Recently, data
dependant techniques have been used to further improve LSH by Andoni and Razenshteyn [2]. However, the
constant ρ in a query time O(nρ) remains:
ρ = log p1
log p2
.
When a formal guarantee that p1 = 1 is needed their algorithm does not apply.
1∥·∥p denotes the standard lp norm for ﬁxed p.
2


## Page 3


2.2
LSH without false negatives
Recently, Pagh [8] presented a novel approach to nearest neighbor search in Hamming space. He showed the
construction of an eﬃcient locality-sensitive hash function family that guarantees collision for any close points.
Moreover, Pagh showed that bounds of his algorithm for cr = log n/k (where k ∈N) essentially match bounds of
Indyk and Motwani (diﬀer by at most factor ln 4 in the exponent). More precisely, he showed that the problem
of false negatives can be avoided in the Hamming space at some cost in eﬃciency. He proved bounds for general
values of c. This paper is an answer to his open problem: whether is it possible to get similar results for other
distance measures (e.g., l1 or l2).
Pagh introduced the concept of an r-covering family of hash function:
Deﬁnition 4. For A ⊆{0, 1}d, the Hamming projection family HA is r-covering if for every x ∈{0, 1}d with
∥x∥H ≤r, there exist h ∈HA such that h(x) = 0.
Then, he presented a fast method of generating such an r-covering family. Finally, he showed that the
expected number of false positives is bounded by 2r+1−∥x−y∥H.
3
Basic Construction
We will consider the lp metric for p ∈[1, ∞] and n ﬁxed points in Rd space. Let v be a d-dimensional vector of
independent random variables drawn from distribution D. We deﬁne a function hp as:
hp(x) =
⟨x, v⟩
rρp

,
where ⟨, ⟩is a standard inner product and ρp = d1−1
p . The scaling factor ρp is chosen so that: ∥z∥1 ≤ρp∥z∥p.
The rudimentary distinction between the hash function hp and LSH is that we consider two hashes equal when
they diﬀer at most by one. In Indyk and Motwani [7] version of LSH, there were merely probabilistic guarantees,
and close points (say 0.99 and 1.01) could be returned in diﬀerent buckets with small probability. Since our
motivation is to ﬁnd all close points with absolute certainty, we need to check the adjacent buckets as well.
First, observe that for given points, the probability of choosing a hash function that will classify them as
equal is bounded on both sides as given by the following observations. The proofs of these observations are in
Appendices A and B.
Observation 1 (Upper bound on the probability of point equivalence).
P [|hp(x) −hp(y)| ≤1] ≤P [| ⟨x −y, v⟩| < 2ρpr] .
Observation 2 (Lower bound on the probability of point equivalence).
P [|hp(x) −hp(y)| ≤1] ≥P [| ⟨x −y, v⟩| < ρpr] .
Interestingly, using the aforementioned observations we can conﬁgure a distribution D so the close points
must end up in the same or adjacent bucket.
Observation 3 (Close points have close hashes). For distribution D such that every vi ∼D: −1 ≤vi ≤1 and
for x, y ∈Rd, if ∥x −y∥p < r then ∀hp|hp(x) −hp(y)| ≤1.
Proof. We know that ∥z∥1 ≤ρp∥z∥p and |vi| ≤1 (because vi is drawn from bounded distribution D), so:
ρp∥x −y∥p ≥∥x −y∥1 =
X
i
|xi −yi| ≥
X
i
|vi(xi −yi)|
≥
 P
i vi(xi −yi)

= | ⟨x −y, v⟩|.
Now, when points are close in lp:
∥x −y∥p < r ⇐⇒ρp∥x −y∥p < ρpr =⇒| ⟨x −y, v⟩| < ρpr.
Next, by Observation 2:
1 = P [| ⟨x −y, v⟩| < ρpr] ≤P [|hp(x) −hp(y)| ≤1] .
Hence, the points will inevitably hash into the same or adjacent buckets.
Now we will introduce the inequality that will help to bound the probability of false positives.
3


## Page 4


Observation 4 (Inequality of norms in lp). Recall that ρp = d1−1
p . For every z ∈Rd and p ∈[1, ∞]:
∥z∥2 ≥
ρp
max{d
1
2 , d1−1
p }
∥z∥p.
This technical observation is proven in Appendix C.
The major question arises: what is the probability of false positives? In contrast to the Indyk and Mot-
wani [7], we cannot use p-stable distributions because these distributions are not bounded. We will present the
proof for a diﬀerent class of functions.
Lemma 1 (The probability of false positives for general distribution). Let D be a random variable such that
E(D) = 0, E(D2) = α2, E(D4) ≤3α4 (for any α ∈R+). Deﬁne constant τ1 = 2
α max{d
1
2 , d1−1
p }.
When ∥x −y∥p > cr, x, y ∈Rd and c > τ1 then:
pfp1 = P [|hp(x) −hp(y)| ≤1] < 1 −

1 −τ 2
1
c2
2
3
,
for every metric lp, where p ∈[1, ∞] (pfp1 is the probability of false positive).
Proof. By Observation 4:
∥z∥2 ≥2∥z∥p
ατ1
ρp
Subsequently, let z = x −y and deﬁne a random variable X = ⟨z, v⟩. Therefore:
E(X2) = α2∥z∥2
2 ≥(2∥z∥p
τ1
ρp)2 > (2rρp
c
τ1
)2.
Because
c
τ1 > 1 we have θ =
(2rρp)2
EX2
< 1. Variable θ and a random variable X2 > 0 satisfy Paley-Zygmunt
inequality (analogously to [9]):
P [|hp(x) −hp(y)| > 1]
≥
P [| ⟨z, v⟩| ≥2rρp] ≥P

X2 > (2rρp)2
≥

1 −(2rρp)2
E(X2)
2 E(X2)2
E(X4) .
Eventually, we assumed that E(X4) ≤3(α∥z∥2)4:
P [|hp(x) −hp(y)| > 1] ≥

1 −
(2rρp)2
E(X2)
2
3
>

1 −τ 2
1
c2
2
3
.
Simple example of a distribution that satisﬁes both Observation 3 and Lemma 1 is a uniform distribution on
(−1, 1) with a standard deviation α equal to
q
1
3. Another example of such distribution is a discrete distribution
with uniform values {−1, 1}. As it turns out, Lemma 2 shows that the discrete distribution leads to even better
bounds.
Lemma 2 (Probability of false positives for the discrete distribution). Let D be a random variable such that
P [D = ±1] = 1
2. Deﬁne constant τ2 =
√
8 max{d
1
2 , d1−1
p }. Then for every p ∈[1, ∞], x, y ∈Rd and c > τ2 such
that ∥x −y∥p > cr, it holds:
pfp2 = P [|hp(x) −hp(y)| ≤1] < 1 −(1 −τ2
c )2
2
.
Proof. Because of Observation 4 we have the inequality:
∥z∥2 ≥
√
8∥z∥p
τ2
ρp.
Let z = x −y and X = ⟨z, v⟩, be a random variable. Then:
P [|hp(x) −hp(y)| > 1] ≥P [|X| > 2rρp] .
4


## Page 5


Khintchine inequality [5] states E|X| ≥∥z∥2
√
2 , so:
E(|X|) ≥∥z∥2
√
2 ≥2ρp∥z∥p
τ2
> 2rρp
c
τ2
.
Note that, a random variable |X| and θ =
2rρp
E(|X|) < 1, satisfy the Paley-Zygmunt inequality (because
c
τ2 > 1),
though:
P [hp(x) −hp(y)| > 1] ≥

1 −
2rρp
E(|X|)
2 E(|X|)2
E(|X|2)
>
 
1 −
2rρp
2rρp c
τ2
!2
1
2 =
 1 −τ2
c
2
2
.
Altogether, in this section we have introduced a family of hash functions hp which:
• guarantees that, with an absolute certainty, points within the distance R will be mapped to the same or
adjacent buckets (see Observation 3),
• maps “far away” points to the non-adjacent hashes with high probability (Lemma 1 and Lemma 2).
These properties will enable us to construct an eﬃcient algorithm for solving the c-approximate nearest neighbor
search problem without false negatives.
3.1
Tightness of bounds
We showed that for two distant points x, y : ∥x −y∥p > cr, the probability of a collision is small when c =
max{ρp,
√
d}. The natural question arises: Can we bound the probability of a collision for points ∥x−y∥p > c′r
for some c′ < c?
We will show that such c′ does not exist, i.e., there always exists ˜x such that ∥˜x∥p will be arbitrarily close
to cr, so ˜x and #»0 will end up in the same or adjacent bucket with high probability. More formally, for any
p ∈[1, ∞], for hp(x) =
j
⟨x,v⟩
rρp
k
, where coordinates of d-dimensional vector v are random variables vi, such that
−1 ≤vi ≤1 with E(vi) = 0. We will show that there always exists ˜x such that ∥˜x∥p ≈r max{ρp,
√
d} and
|hp(˜x) −hp(#»0 )| ≤1 with high probability.
For p ≥2 denote x0 = (rρp −ǫ, 0, 0, . . ., 0). We have ∥x0 −#»0 ∥p = rρp −ǫ and:
|hp(x0) −hp(#»0 )| =

rρp −ǫ
rρp
· v1

−0
 ≤1.
For p ∈[1, 2), denote x1 = rd−1
p + 1
2 −ǫ #»1 .
We have ∥x1∥p = rd
1
2 −ǫ and by applying Observation 2 for
complementary probabilities:
P

|hp(x1) −hp(#»0 )| > 1

≤
P [| ⟨x1, v⟩| ≥ρpr] = P
h
|

#»1 , v

| ≥d
1
2 +ǫi
=
P
"
Pd
i=1 vi
d
 ≥d−1
2 +ǫ
#
≤2 · exp
−d2ǫ
2

.
The last inequality follows from Hoeﬀding [6] (see Appendix D for technical details).
So the aforementioned probability for p ∈[1, 2) is bounded by an expression exponential in d2ǫ.
Even
if we would concatenate k random hash functions (see proof of Theorem 1 for more details), the chance of
collision would be at least (1 −2e
−d2ǫ
2
)k. To bound this probability, the number k needs to be at least Θ(e
d2ǫ
2 ).
The probability bounds do not work for ǫ arbitrary close to 0: we proved that introduced hash functions for
c = d1/2−ǫ do not work (may give false positives).2
Hence, to obtain a signiﬁcantly better approximation factor c, one must introduce a completely new family
of hash functions.
2However, one may try to obtain tighter bound (e.g., c = d1/2/ log(d)) or show that for every ǫ > 0, the approximation factor
c = d1/2 −ǫ does not work.
5


## Page 6


4
The algorithm
In this section, we apply the LSH family introduced in Section 3 to construct an c-approximate algorithm
without false negatives. To begin with, we will deﬁne a general algorithm that will satisfy our conditions.
Subsequently, we will show that complexity of the query is sublinear, and it depends linearly on the number of
dimensions.
Theorem 1. For any c > τ and the number of iterations k ≥0, there exists a c-approximate nearest neighbor
algorithm without false negatives for lp, where p ∈[1, ∞]:
• Preprocessing time: O(n(kd + 3k)),
• Memory usage: O(n3k),
• Expected query time: O(d(|P| + k + npfp
k)).
Where |P| is the size of the result and pfp is the upper bound of probability of false positives (note that pfp
depends on a choice of τ from Lemma 1 or Lemma 2).
Proof. Let g(x) := (h1
p(x), h2
p(x), . . . , hk
p(x)) be a hash function deﬁned as a concatenation of k random LSH
functions presented in Section 3. We introduce the clustering m : g(Rd) →2n, where each cluster is assigned to
the corresponding hash value. For each hash value α, the corresponding cluster m(α) is {x : g(x) = α}.
Since we consider two hashes to be equal when they diﬀer at most by one (see Observation 3), for hash α,
we need to store the reference for every point that satisﬁes ∥α −x∥≤1. The number of such clusters is 3k,
because the result of each hash function can vary by one of {−1, 0, 1} and the number of hash functions is k.
Thus, the memory usage is O(n3k) (see Figure 2).
k
Figure 2: Blue dots represent value of g(q) for query. Green dots are always distant by 1, hence green and blue
points are considered close. At least one red dot is distant from blue dot by more than 1, hence red dots will
not be considered close to blue. Thus, algorithm needs to check 3k various possibilities.
To preprocess the data, we need to compute the value of the function g for every point in the set and then
put its reference into 3k cells. Hence, the preprocessing time complexity equals O(n(kd + 3k)).
Eventually, to answer a query, we need to compute g(q) in time O(kd) and then for every point in ∥g(x) −
g(q)∥∞≤1 remove distant points ∥x −q∥p > cR. Hence, we need to look up every false-positive to check
whether they are within distance cr from the query point. We do that in expected time O(d(|P| + k + npfp
k)),
because npfp
k is the expected number of false positives.
The number of iterations k can be chosen arbitrarily, so we will choose the optimal value to minimize the
query time. This gives the main result of this paper:
Theorem 2. For any c > τ and for large enough n, there exists a c-approximate nearest neighbor algorithm
without false negatives for lp, where p ∈[1, ∞]:
• Preprocessing time: O(n(γd log n + ( n
d )γ)) = poly(n),
• Memory usage: O(n( n
d )γ),
• Expected query time: O(d(|P| + γ log(n) + γd)).
Where |P| is the size of the result, γ =
ln 3
−lnpfp and pfp and τ are chosen as in Theorem 1.
6


## Page 7


Proof. Denote a = −ln pfp, b = ln 3 and set k =
l ln na
d
a
m
.
Let us assume that n is large enough so that k ≥1. Then using the fact that x1/x is bounded for x > 0 we
have:
3k ≤3 · (3ln na
d )1/a = 3 · (na
d )b/a = O((n
d )b/a) = O((n
d )γ),
npfp
k = ne−ak ≤ne−a
ln( na
d )
a
= d
a = O(dγ),
k = O(γ log(n)).
Substituting these values in the Theorem 1 gives needed complexity guaranties.
There are two variants of Theorems 1, 2 and 3. In the ﬁrst variant, we show complexity bounds for very
general class of hashing functions introduced in Lemma 1. In the second one, we show slightly better guaranties
for hashing functions which are generated using discrete probability distribution on {0, 1} introduced in Lemma
2. For simplicity the following discussion is restricted only to the second variant which gives better complexity
guaranties. The deﬁnitions of constants pfp2 and τ2 used in this discussion are taken from Lemma 2 . For a
general case, i.e., pfp1 and τ1 taken from Lemma 1, we get only slightly worse results.
The complexity bounds introduced in the Theorem 2 can be simpliﬁed using the fact that ln(x) < x −1.
Namely, we have:
γ =
ln 3
−ln pfp2
=
ln 3
−ln(1 −(1−τ2
c )2
2
)
<
2 ln 3
(1 −τ2
c )2 .
However, the preprocessing time is polynomial in n for any constant c, it strongly depends on the bound for
probability pfp2 and c. Particularly when c is getting close to τ2, the exponent of the preprocessing time might
be arbitrarily large.
To the best of our knowledge, this is the ﬁrst algorithm that will ensure that no false negatives will be
returned by the nearest neighbor approximated search and does not depend exponentially on the number of
dimensions. Note that for given c, the parameter γ is ﬁxed. By Lemma 2, we have: pfp2 = 1 −
(1−
τ2
2
c2 )2
2
, so:
lim
c→∞γ = lim
c→∞
ln 3
−ln pfp2
= log2 3 ≈1.58.
If we omit terms polynomial in d, the preprocessing time of the algorithm from Theorem 2 converges to
O(n2.58) (O(n3.71) for general case - see Appendix E.).
4.1
Light preprocessing
Although the preprocessing time O(n2.58) may be reasonable when there are multiple, distinct queries and
the data set does not change (e.g., static databases, pre-trained classiﬁcation, geographical map). Still, unless
the number of points is small, this algorithm does not apply. Here, we will present an algorithm with a light
preprocessing time O(dn log n) and O(n log n) memory usage where the expected query time is o(n).
The algorithm with light preprocessing is very similar to the algorithm described in Theorem 1, but instead
of storing references to the point in all 3k buckets during preprocessing, this time searching for every point x
that matches ∥x −q∥∞≤1 is done during the query time.
The expected query time with respect to k is O(d(|P| + k + npfp
k) + 3k). During the preprocessing phase
we only need to compute k hash values for each of n points and store them in memory. Hence, preprocessing
requires O(kdn) time and uses O(nk) memory.
Theorem 3. For any c > τ and for large enough n, there exists a c-approximate nearest neighbor algorithm
without false negatives for lp, where p ∈[1, ∞]:
• Preprocessing time: O(nd log n),
• Memory usage: O(n log n),
• Expected query time: O(d(|P| + n
b
a+b ( b
a)
a
b+a )).
Where |P| is the size of the result, a = −ln pfp, b = ln 3, pfp and τ are chosen as in Theorem 1.
7


## Page 8


Proof. We set the number of iterations k =
l ln na
b
a+b
m
. Assume n needs to be large enough so that k ≥1. Since a
is upper bounded for both choices of pfp:
3k ≤3 · 3
ln( na
b )
a+b
= 3(na
b )
b
a+b = O(n
b
a+b ).
Analogously:
npfp
k = n(e−a)k ≤ne−a
ln( na
b )
a+b
= n ·
 b
a

a
a+b ·
 1
n

a
a+b = n
b
a+b
 b
a

a
a+b .
Hence, for this choice of k we obtain the expected query time is equal to:
O(d(|P| + k + npfp
k)) + 3k = O(d(|P| + log n + n
b
a+b
 b
a

a
a+b ) + n
b
a+b )
= O(d(|P| + n
b
a+b
 b
a

a
a+b ).
Substituting k, we obtain formulas for preprocessing time and memory usage.
Eventually, exactly as previously for a general distribution from Lemma 1, when c →∞we have: a →ln 3
2
(see Theorem 3 for the deﬁnition of constant a). Hence, for a general distribution we have a bound for complexity
equal to O(nlog4.5 3) ≈O(n0.73). For the discrete distribution from Lemma 2, the constant a converges to ln 2.
Hence, the expected query time converges to O(n0.61).
5
Conclusion and Future Work
We have presented the c-approximate nearest neighbor algorithm without false negatives in lp for all p ∈[1, ∞]
and c > max{
√
d, d1−1/p}. Due to this inequality our algorithm can be used cognately to the original LSH [7] but
with additional guarantees about very close points (one can set R′ =
√
dR and be certain that all points within
distance R will be returned). In contrast to the original LSH, our algorithm does not require any additional
parameter tunning.
The future work concerns relaxing restriction on the approximation factor c and reducing time complexity
of the algorithm or proving that these restrictions are essential. We wish to match the time complexities given
by [7] or show that achieved bounds are optimal. We show the tightness of our construction, hence to break
the bound of
√
d, one would need to introduce a new technique.
6
Acknowledgments
This work was supported by ERC PoC project PAAl-POC 680912 and FET project MULTIPLEX 317532. We
would also like to thank Rafa l Lata la for meaningful discussions.
References
[1] Alexandr Andoni and Piotr Indyk. Near-optimal hashing algorithms for approximate nearest neighbor in
high dimensions. Commun. ACM, 51(1):117–122, 2008.
[2] Alexandr Andoni and Ilya Razenshteyn. Optimal data-dependent hashing for approximate near neighbors.
In Rocco A. Servedio and Ronitt Rubinfeld, editors, Proceedings of the Forty-Seventh Annual ACM on
Symposium on Theory of Computing, STOC 2015, Portland, OR, USA, June 14-17, 2015, pages 793–801.
ACM, 2015.
[3] Jon Louis Bentley. K-d trees for semidynamic point sets. In Proceedings of the Sixth Annual Symposium
on Computational Geometry, SCG ’90, pages 187–197, New York, NY, USA, 1990. ACM.
[4] Mayur Datar and Piotr Indyk. Locality-sensitive hashing scheme based on p-stable distributions. In In
SCG 04: Proceedings of the Twentieth Annual Symposium on Computational Geometry, pages 253–262.
ACM Press, 2004.
[5] Uﬀe Haagerup. The best constants in the Khintchine inequality. Studia Mathematica, 70(3):231–283, 1981.
[6] Wassily Hoeﬀding. Probability inequalities for sums of bounded random variables. Journal of the American
Statistical Association, 58(301):13–30, March 1963.
8


## Page 9


[7] Piotr Indyk and Rajeev Motwani. Approximate nearest neighbors: Towards removing the curse of dimen-
sionality. In Proceedings of the Thirtieth Annual ACM Symposium on Theory of Computing, STOC ’98,
pages 604–613, New York, NY, USA, 1998. ACM.
[8] Rasmus Pagh. Locality-sensitive hashing without false negatives. In Robert Krauthgamer, editor, Pro-
ceedings of the Twenty-Seventh Annual ACM-SIAM Symposium on Discrete Algorithms, SODA 2016,
Arlington, VA, USA, January 10-12, 2016, pages 1–9. SIAM, 2016.
[9] Mark Veraar. On Khintchine inequalities with a weight. Proceedings of the American Mathematical Society,
138:4119–4121, 2010.
[10] Ryan Williams. A new algorithm for optimal 2-constraint satisfaction and its implications. Theor. Comput.
Sci., 348(2):357–365, December 2005.
9


## Page 10


A
Proof of Observation 1
Proof. We will use, the fact that for any x, y ∈R we have | ⌊x⌋−⌊y⌋| ≤1 ⇒|x −y| < 2. Then the following
implications hold:
|hp(x) −hp(y)| ≤1 ⇐⇒

j
⟨x,v⟩
ρpr
k
−
j
⟨y,v⟩
ρpr
k  ≤1
=⇒
⟨x, y⟩
ρpr
−⟨y, v⟩
ρpr
 < 2 ⇐⇒
⇐⇒
| ⟨x −y, v⟩| < 2ρpr.
So, based on the increasing property of the probability:
if A ⊂B then P [A] ≤P [B] ,
the inequality of the probabilities holds.
B
Proof of Observation 2
Proof. We will use the fact that for x, y ∈R : |x −y| < 1 ⇒| ⌊x⌋−⌊y⌋| ≤1).
 ⟨x −y, v⟩
 < ρpr ⇐⇒
 ⟨x,v⟩
ρpr −⟨x,v⟩
ρpr
 < 1
=⇒

⟨x, v⟩
ρpr

−
⟨x, v⟩
ρpr
  ≤1 ⇐⇒
⇐⇒
|hp(x) −hp(y)| ≤1
C
Proof of Observation 4
Proof. For every 0 < b ≤a vectors in Rd satisfy the inequality:
∥z∥a ≤∥z∥b ≤d( 1
b −1
a )∥z∥a.
(1)
For p > 2 we have max{d
1
2 , d1−1
p } = d1−1
p . Then, using ineqaulity (1) for a = p and b = 2 we have:
∥z∥2 ≥∥z∥p =
ρp
d1−1
p ∥z∥p =
ρp
max{d
1
2 , d1−1
p }
∥z∥p
For 1 ≤p ≤2 we have max{d
1
2 , d1−1
p } = d
1
2 . Analogously by using inequality (1) for a = 2 and b = p:
∥z∥p ≤d
1
p −1
2 ∥z∥2 = ∥z∥2
d
1
2
ρp
Hence, by dividing both sides we have:
∥z∥p
ρp
max{d
1
2 , d1−1
p }
≤∥z∥2
D
Hoeﬀding bound
Here we are going to show all technical details used in the proof in the Section 3.1. Let us start with the
Hoeﬀding inequality. Let X1, . . . , Xd be bounded independent random variables: ai ≤Xi ≤bi and X be the
mean of these variables X = Pd
i=1 Xi/d. Theorem 2 of Hoeﬀding [6] states:
P

|X −E

X

| ≥t

≤2 · exp
 
−
2d2t2
Pd
i=1(bi −ai)2
!
.
In our case, D1, . . . , Dd are bounded by ai = −1 ≤Di ≤1 = bi with EDi = 0. Hoeﬀding inequality implies:
10


## Page 11


P
"
Pd
i=1 Di
d
 ≥t
#
≤2 · exp
 
−
2d2t2
Pd
i=1(bi −ai)2
!
= 2 · exp

−dt2
2

.
Taking t = d−1/2+ǫ we get the claim:
P
"
Pd
i=1 Di
d
 ≥d−1/2+ǫ
#
≤2 · exp

−d2ǫ
2

.
E
Preprocessing complexity bounds for the distributions introduced
in Lemma 1
By Lemma 1, we have: pfp1 = 1 −
(1−
τ2
1
c2 )2
3
, so:
lim
c→∞γ = lim
c→∞
ln 3
−ln pfp1
= ln 3
ln 1.5 ≈2.71.
If we omit terms polynomial in d, the preprocessing time of the algorithm from Theorem 2 converges to
O(n3.71).
11

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1611_09317_locality_sensitive_hashing_without_false_negatives_for_l_p
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1611_09317_LOCALITY_SENSITIVE_HASHING_WITHOUT_FALSE_NEGATIVES_FOR_L_P.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
