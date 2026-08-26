---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0901.0168v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 0901.0168v3_Coding_for_Two-User_SISO_and_MIMO_Multiple_Access_Channels

> Source: 0901.0168v3_Coding_for_Two-User_SISO_and_MIMO_Multiple_Access_Channels.pdf

> Pages: 18

---


## Page 1


arXiv:0901.0168v3  [cs.IT]  9 Feb 2009
1
Coding for Two-User SISO and MIMO Multiple
Access Channels
J. Harshan and B. Sundar Rajan, Senior Member, IEEE
Abstract— Constellation Constrained (CC) capacity regions of
a two-user SISO Gaussian Multiple Access Channel (GMAC)
with ﬁnite complex input alphabets and continuous output are
computed in this paper. When both the users employ the same
code alphabet, it is well known that an appropriate rotation be-
tween the alphabets provides unique decodability to the receiver.
For such a set-up, a metric is proposed to compute the angle(s)
of rotation between the alphabets such that the CC capacity
region is maximally enlarged. Subsequently, code pairs based on
Trellis Coded Modulation (TCM) are designed for the two-user
GMAC with M-PSK and M-PAM alphabet pairs for arbitrary
values of M and it is proved that, for certain angles of rotation,
Ungerboeck labelling on the trellis of each user maximizes the
guaranteed squared Euclidean distance of the sum trellis. Hence,
such a labelling scheme can be used systematically to construct
trellis code pairs for a two-user GMAC to achieve sum rates
close to the sum capacity of the channel. More importantly, it
is shown for the ﬁrst time that ML decoding complexity at the
destination is signiﬁcantly reduced when M-PAM alphabet pairs
are employed with almost no loss in the sum capacity.
A two-user Multiple Input Multiple Output (MIMO) fading
MAC with Nt antennas at both the users and a single antenna
at the destination has also been considered with the assumption
that the destination has the perfect knowledge of channel state
information and the two users have the perfect knowledge of
only the phase components of their channels. For such a set-
up, two distinct classes of Space Time Block Code (STBC) pairs
derived from the well known class of real orthogonal designs are
proposed such that the STBC pairs are information lossless and
have low ML decoding complexity.
Index Terms— Multiple access channels, Ungerboeck partition-
ing, constellation constrained capacity, trellis coded modulation,
MIMO multiple access channel, space time coding and real
orthogonal designs.
I. INTRODUCTION AND PRELIMINARIES
Capacity regions of a two-user Gaussian Multiple Access
Channel (GMAC) with continuous input alphabets and con-
tinuous output is well known [1]-[5]. Such a model assumes
the users to employ Gaussian code alphabets and the additive
noise is assumed to be Gaussian distributed. Though, capacity
regions of such a channel provides insights in to the achievable
rate pairs (R1, R2) in an information theoretic sense, it fails
to provide information on the achievable rate pairs when
we consider ﬁnitary restrictions on the input alphabets and
analyze some real world practical signal constellations like
This work was supported partly through grants to B.Sundar Rajan by the
DRDO-IISc program on Advanced Research in Mathematical Engineering.
Part of the content of this paper is in the proceedings of IEEE International
Symposium on Information theory (ISIT 2008). Some parts of this paper is
submitted to IEEE ISIT 2009 to be held at Seoul, Korea. The authors are with
the Department of Electrical Communication Engineering, Indian Institute of
Science, Bangalore-560012, India. Email:{harshan,bsrajan}@ece.iisc.ernet.in.
M-QAM and M-PSK signal sets for some positive integer,
M. Gaussian multiple access channels with ﬁnite complex
input alphabets and continuous output was ﬁrst considered
in [6] with the assumption of random phase offsets in the
channel from every user to the destination. For such a channel
model, Constellation Constrained (CC) sum capacity has been
computed for some well known alphabets such as M-PSK
and M-QAM in [6] and trellis codes have also been proposed
in [7] and [8]. Note that the assumption of random phase
offsets in the channel naturally provides Uniquely Decodable
(UD) property to the receiver when all the users use the same
alphabet.
Subsequently, a K-user GMAC model with no random
phase offsets in the channel has been considered in [9] and
codes based on Trellis Coded Modulation (TCM) [10] have
been proposed wherein the UD property at the destination is
achieved by employing distinct alphabets for all the users. In
particular, an alphabet of size KM (example: KM-PSK or
KM- QAM) is chosen and it is appropriately partitioned in
to K groups such that every user uses one of the groups as its
code alphabet. Towards designing trellis codes, the authors of
[9] only propose steps to choose the labellings on the edges
of the trellises of all the users, but do not provide explicit
labellings on the individual trellises.
In this paper, a two-user GMAC with ﬁnite complex input
alphabets and continuous output is considered without the
assumption of random phase offsets in the channel (it is shown
that the assumption of random phase offsets in the channel
leads to loss in the CC sum capacity) and the impact of the
rotation between the alphabets of the two-users on capacity
regions is investigated. Code pairs based on TCM are also
proposed such that sum rates close to the CC sum capacity can
be achieved for some classes of alphabet pairs. Throughout
the paper, the mutual information value for a GMAC when
the symbols from the input alphabets are chosen with uniform
distribution is referred as the Constellation Constrained (CC)
capacity of the GMAC [11]. Henceforth, unless speciﬁed,
(i) input alphabet refers to a ﬁnite complex alphabet and a
GMAC refers to a Gaussian MAC with ﬁnite complex input
alphabets and continuous output alphabet and (ii) capacity
(capacity region) refers to the CC capacity (capacity region).
Throughout the paper, the terms alphabet and signal set are
used interchangeably.
The idea of rotation between the alphabets of the two
users is also exploited to construct Space Time Block Code
(STBC) pairs with low ML decoding complexity for a two-
user MIMO (Multiple Input Multiple Output) fading MAC.
For a background on space-time coding for MIMO-MAC, we


## Page 2


2
refer the reader to [12], [13]. Till date, we are not aware
of any work which address the design of STBC pairs with
low ML decoding complexity for a two-user MIMO-MAC.
Note that STBC pairs with minimum ML decoding complexity
have been well studied in the literature for collocated MIMO
channels [14], [15], [16], [17] and relay channels [18], [19]
as well. The contributions of the paper may be summarized
as below:
• For a two-user GMAC, when both the users employ
identical alphabet, it is well known that an appropriate
rotation between the alphabets can guarantee UD property
(See Deﬁnition 1) to the receiver [6]. For such a setup,
we identify that the primary problem is to compute
the angle(s) of rotation between the alphabets such that
the capacity region is maximally enlarged. A metric
to compute the angle(s) of rotation is proposed which
provides maximum enlargement of the capacity region
(See Theorem 1). Through simulations, such angles of
rotation are presented for some well known alphabets
such as M-PSK, M-QAM etc for some values of M
at some ﬁxed SNR values (See Table I).
• For a two-user GMAC, code pairs based on TCM are
designed with M-PSK and M-PAM alphabet pairs to
achieve sum rates close to the CC sum capacity of the
channel. In particular, trellis codes are explicitly designed
for each user by exploiting the structure of the sum
alphabets of M-PSK and M-PAM alphabet pairs.
• For each i = 1, 2, if User-i employs the trellis Ti labelled
with the symbols of the signal set Si, it is clear that the
destination sees the sum trellis, Tsum (See Deﬁnition 2)
labelled with the symbols of the sum alphabet, Ssum (See
Section II-A) in an equivalent SISO (Single Input Single
Output) AWGN channel. Recall that, for a SISO AWGN
channel, Ungerboeck labelling on the trellis maximizes
the guaranteed minimum squared Euclidean distance,
d2
g,min of the trellis and hence such a labelling scheme
has become a systematic method of generating trellis
codes to go close to the capacity [10]. However, when
TCM based trellis codes are designed for a two-user
GMAC, it is not clear if the two users can distributively
achieve Ungerboeck labelling on the sum trellis through
the trellises T1 and T2. In other words, it is not known
whether Ungerboeck labelling on T1 and T2 using S1 and
S2 respectively induces an Ungerboeck labelling on Tsum
using Ssum. In this paper, it is analytically proved that,
for the class of symmetric M-PSK signal sets, when the
relative angle is
π
M , Ungerboeck labelling on the trellis
of each user induces an Ungerboeck labelling on Tsum
which in-turn maximizes the d2
g,min of the Tsum (See
Theorem 2). Hence, such a labelling scheme can be used
as a systematic method of generating trellis code pairs for
a two-user GMAC to go close to the sum capacity. An
example for an alphabet pair is presented using which
a non-Ungerboeck labelling on the trellis of each user
maximizes the d2
g,min of the Tsum. (See Section III-C,
Example 2).
• Trellis code pairs are also designed in this paper with
M-PAM signal sets for a two-user GMAC (See Section
III-D). For such signal sets, it is shown that the relative
angle of rotation that maximally enlarges the CC capacity
region is
π
2 ∀M and for all values of SNR. Note that
the above structure on M-PAM alphabet pairs keep the
two users orthogonal to each other and hence trellis
codes designed for SISO AWGN channel with M-PAM
alphabets are applicable in this set-up. Hence the ML
decoding complexity is signiﬁcantly reduced when trellis
codes with M-PAM signal sets are employed. Through
simulations, it is shown that, for a particular SNR, the
sum capacity of 4-PAM signal sets (when used with
a relative rotation of
π
2 ) and QPSK signal sets (with
appropriate angles of rotation provided in [23]) are almost
the same and hence unlike in a SISO AWGN channel
there is no loss in the sum capacity by using 4-PAM
alphabets over QPSK signal sets in a two user GMAC.
Similar observations are also presented for Gaussian code
alphabets.
• A two-user MIMO fading MAC with Nt antennas at
both the users and a single antenna at the destination
is considered in this paper. The destination is assumed to
have the perfect knowledge of Channel State Information
(CSI) whereas the two users are assumed to have the
perfect knowledge of only the phase components of their
channels to the destination. For such a set-up, two classes
of Space Time Block Code (STBC) pairs are introduced
such that the code pairs are (i) information lossless and
(ii) have reduced ML decoding complexity for all values
of Nt. To the best of our knowledge, this is the ﬁrst paper
that addresses construction of STBC pairs for MIMO-
MAC with low ML decoding complexity as well as
information losslessness property. (See Section IV).
• The ﬁrst class of STBC pairs are from a class of complex
designs called Separable Orthogonal Designs (SOD) (See
Deﬁnition 5) which in-turn are constructed using the well
known class of Real Orthogonal Designs (ROD) [14],
[15]. It is shown that STBC pairs generated from SODs
are (i) information lossless for all values of Nt and (ii)
are two-group ML decodable [20]. (See Section IV-A).
• The second class of STBC pairs are generated straight
from RODs wherein certain restrictions on input alphabet
pairs are imposed. Such a class of STBC pairs are
shown to be information lossless for large values of
Nt. However, for smaller values of Nt, the loss in the
sum capacity is shown to be marginal. Importantly, the
proposed code pairs also have the single symbol ML
decodable property as they are generated straight from
RODs. Simulation results are presented which show that
STBC pairs from RODs perform better than those from
SODs in terms of total Bit Error Rate (BER). (See Section
IV-B).
Notations: For a random variable X which takes value from
the set S, we assume some ordering of its elements and use
X(i) to represent the i-th element of S. i.e. X(i) represents a
realization of the random variable X. Cardinality of the set S
is denoted by |S|. Absolute value of a complex number x is


## Page 3


3
Adder
AWGN
Destination
x
x
z
y
2
1
x1 + x2
User 1
User 2
Fig. 1.
Two-user Gaussian MAC model
denoted by |x| and E [x] denotes the expectation of the random
variable x. A circularly symmetric complex Gaussian random
vector, x with mean µ and covariance matrix Γ is denoted by
x ∼CN (µ, Γ). Also, the set of all real and complex numbers
are denoted by R and C respectively. For a, b ∈C, distance
between between a and b is denoted by d(a, b) whereas the
line segment connecting a and b is denoted by l(a, b).
The remaining content of the paper is organized as follows:
In Section II, we present CC capacity regions of a two-
user GMAC with ﬁnite alphabet pairs and provide details on
computing the angles of rotation between the alphabets such
that the CC capacity region is maximally enlarged. In Section
III, we discuss details on designing TCM schemes for a two-
user GMAC with M-PSK and M-PAM as input alphabet
pairs ∀M. In Section IV, a two-user MIMO-MAC model
is introduced and two distinct classes of low ML decoding
complexity STBC pairs are presented. Section V constitutes
conclusion and some directions for possible future work.
II. TWO-USER GMAC - SIGNAL MODEL AND
CONSTELLATION CONSTRAINED CAPACITY REGIONS
The model of a two-user Gaussian MAC is as shown in
Fig. 1 consists of two users that need to convey information
to a single destination. It is assumed that User-1 and User-
2 communicate to the destination at the same time and in
the same frequency band. Symbol level synchronization is
assumed at the destination. The two users are equipped with
alphabets S1 and S2 of size N1 and N2 respectively. When
User-1 and User-2 transmit symbols x1 ∈S1 and x2 ∈S2
respectively, the destination receives a symbol y given by,
y = x1 + x2 + z where z ∼CN
 0, σ2
.
(1)
We compute the mutual information values I(x2 : y) and
I(x1 : y | x2) when the symbols x1 and x2 are assumed
to take values form S1 and S2 with uniform distribution. By
symmetry, I(x1 : y) and I(x2 : y | x1) can also be computed.
Considering x1 + z as the additive noise, I(x2 : y) and
I(x1 : y | x2) can be computed and are presented in (2) and (3)
(shown at the top of the next page). Therefore, using (2) and
(3), the sum mutual information for both the users is I(x2 : y)
+ I(x1 : y | x2). Using Fano’s inequality, it is straightforward
to prove that rates (in bits per channel use) more than the
above mutual information values cannot be achieved. Hence,
the capacity region is as given below [1],
R1 < I(x1 : y | x2),
R2 < I(x2 : y | x1) and
R1 + R2 < I(x1, x2 : y) = I(x1 : y | x2) + I(x2 : y). (4)
Note that I(x2 : y) and I(x1 : y | x2) (similarly I(x1 : y)
and I(x2 : y | x1)) are only upper bounds on the achievable
rate pairs since coding schemes achieving rate pairs close to
the edges of the CC capacity region are yet to be identiﬁed.
A. Uniquely decodable alphabet pairs for GMAC
In this subsection, we formally deﬁne a UD alphabet
pair. Given two alphabets S1 and S2, we denote the sum
alphabet of S1 and S2 by Ssum deﬁned as Ssum
=
{x1 + x2 | ∀x1 ∈S1, x2 ∈S2}. The adder channel in the
two-user GMAC (as shown in Fig. 1) can be viewed as a map-
ping φ given by φ : S1 × S2 −→Ssum where φ((x1, x2)) =
x1 + x2.
Deﬁnition 1: An alphabet pair (S1, S2) is said to be
uniquely decodable if the mapping φ is one-one.
Example for a UD alphabet pair is S1 = {1, −1} and S2 =
{i, −i}. An example for a non-UD alphabet pair is given by
S1 = S2 = {1, −1}. Note that if S1 and S2 have more than
one element common, then the pair (S1, S2) is necessarily
non-UD. However, not having more than one common signal
point is not sufﬁcient for a pair to be UD, as exempliﬁed by
the pair S1 = {1, ω, ω2} and S2 = {−1, 1 +ω, 1 +ω2} where
ω is a cube root of unity.
It is clear that uncoded multi-user communication with non-
UD alphabet pair results in ambiguity while performing joint
decoding for the symbols of both users at the destination. In
order to circumvent this ambiguity, the two users can jointly
construct code pairs (C1, C2) (codes constructed by adding
redundancy across time) over the non-UD alphabet pair so
that the codewords of both users can be uniquely decoded.
Note that, there will be a loss in the rate of transmission (in
other words, there will be an expansion of the bandwidth) by
adopting such schemes. Therefore, for band-limited multiuser
Gaussian channels, coding across time is forbidden to achieve
the UD property and hence, the use of UD alphabets is
essential.
B. Capacity maximizing alphabet pairs from rotations
For a GMAC with S1 = S2, it is clear that if one of the
users employ an appropriate rotated version of the alphabet
used by the other, then UD property is attainable. Moving one
step further, we consider the problem of ﬁnding the optimal
angle(s) of rotation between the alphabet pair such that the
capacity region is maximally enlarged for a given of SNR.
For a given alphabet S1, let S2 denote the set of symbols
obtained by rotating all the symbols of S1 by θ degrees.
From (4), the capacity region is determined by the mutual
information values I(x1 : y | x2), I(x2 : y | x1) and I(x2 : y)
(or I(x1 : y)). Note that, the terms I(x1 : y | x2) and
I(x2 : y | x1) are functions of the Distance Distribution (DD)
of S1 and S2 respectively. Since, we start with a known S1
and S2 = eiθS1, the DD of S1 and S2 are the same. Hence
I(x1 : y | x2) and I(x2 : y | x1) are independent of θ.
However, from (2), the term I(x2 : y) is a function of the
DD of Ssum and the DD of Ssum changes with θ and hence
the term I(x2 : y) is a function of θ.


## Page 4


4
I(x2 : y) = log2(N2)−
1
N1N2
N1−1
X
k1=0
N2−1
X
k2=0
E
"
log2
"PN1−1
i1=0
PN2−1
i2=0 exp
 −|x1(k1) + x2(k2) −x1(i1) −x2(i2) + z|2/σ2
PN1−1
i1=0 exp (−|x1(k1) −x1(i1) + z|2/σ2)
##
.
(2)
I(x1 : y | x2) = log2(N1) −1
N1
N1−1
X
k1=0
E
"
log2
"PN1−1
i1=0 exp
 −|x1(k1) −x1(i1) + z|2/σ2
exp (−|z|2/σ2)
##
.
(3)
In the following theorem, we provide a criterion to choose
the value of θ such that I(x2 : y) is maximized which in-turn
maximally enlarges the capacity region in (4).
Theorem 1: Let (S1, S2) be an alphabet pair such that S2 =
eiθS1 and |S1| = N. The mutual information value, I(x2 : y)
in (2) is maximized by choosing the angle of rotation, θ∗such
that θ∗= arg minθ∈(0,2π) M(θ) where M(θ) is given in (5).
Proof:
Since
N1
=
N2
=
N
is
ﬁxed,
arg maxθ∈(0,2π) I(x2
:
y)
= arg minθ∈(0,2π) I
′(x2
:
y)
where I
′(x2 : y) is given in (6). Since the denominator
term inside the logarithm of I
′(x2 : y) is independent of θ,
arg minθ∈(0,2π) I
′(x2 : y) = arg minθ∈(0,2π) I
′′(x2 : y) where
I
′′(x2 : y) is given in (7). Applying Jensen’s inequality
on the individual terms, λ(k1, k2) of I
′′(x2
:
y) and
replacing each term of the form x2(.) by eiθx1(.), we have
I
′′(x2 : y) ≤M(θ). Hence, instead of ﬁnding θ which
minimizes I
′′(x2 : y), we propose to ﬁnd θ∗which minimizes
M(θ), an upper bound on I
′′(x2 : y).
Note that every individual term, λ(k1, k2) of I
′′(x2 : y) is
an expectation of a non linear function of the random variable
z and the closed form expressions of λ(k1, k2) ∀k1, k2 are
not available. Therefore, in the above theorem, we propose to
ﬁnd θ∗which minimizes M(θ), an upper bound on I
′′(x2 : y)
instead of I
′′(x2 : y) itself. Note that the values of θ obtained
by minimizing I
′′(x2 : y) can potentially provide larger
capacity regions than those obtained using θ∗.
Since M(θ) depends on the DD of Ssum, θ∗depends on
the average transmit power per channel use P1 (for User-1)
and P2 (for User-2) of the alphabets S1 and S2 respectively.
Note that, though the results of the Theorem 1 applies only
to alphabets such that S2 = eiθS1, its extension to the case
when S2 ̸= eiθS1 is straightforward.
C. Optimal rotations for some known alphabets
In this subsection, for a given alphabet S1 and for a given
value of P1 = P2, through simulations, using the metric
proposed in Theorem 1, we ﬁnd angle(s) of rotation, θ∗(in
degrees) that results in a DD of the sum alphabet which
maximizes I(x2 : y). For the simulation results, additive noise,
z is assumed to have unit variance per dimension. i.e. σ2 = 2.
The values of θ∗are calculated by varying the relative angle of
rotation from 0 to 180 in steps of 0.0625 degrees. In Table I,
for various values of P1/σ2 = SNR, values of θ∗are presented
for some well known alphabets such as M-QAM, M-PSK for
M = 4, 8 and 16. Against every signal set, a two-tuple (a, b) is
presented where a denotes θ∗and b represents the multiplicity
of θ∗since for some SNR values, there could be more than one
value of θ∗that minimizes M(θ) (Example : QPSK at SNR =
8 db, 16-PSK at SNR = 16 db). In general, if θ∗is calculated
by varying the angle of rotation with different intervals, then
the optimal θ∗and the multiplicity of the optimal θ∗will also
change. When there are multiple values of θ∗for a signal set,
only one of them is provided in the table. Among the several
angles, the one presented in the table reduces the complexity
at the transmitters compared to the rest of the angles (Example
: for BPSK, 90 degrees is chosen over other angles of rotation
at SNR = 10 db). However, when there is not much difference
in the complexity among the several values of θ∗, we present
the one with the least value (Example : for QPSK at SNR =
8 db, 16 db).
1) Capacity regions of a GMAC with S1 =BPSK: In Fig.
2, capacity regions using BPSK alphabet pair with optimal
rotation and without rotation are given at SNR = -2 db and
2 db. Capacity regions of a GMAC with Gaussian alphabets
are also given in Fig. 2 at -2 db and 2 db. The plot shows
that, for a given SNR, capacity region of the BPSK alphabet
pair is contained inside the capacity region of the Gaussian
code alphabet. Note that, with rotation, both users can transmit
at rates equal to SISO AWGN channel capacity with BPSK
alphabet simultaneously. This is because θ∗= 90 degrees (at
all SNR values) which makes S1 and S2 orthogonal. Hence
both users can achieve the rates close to I(x1 : y | x2)
and I(x2 : y | x1) respectively at all SNR values. From
Table I, note that there are several angles apart from 90
degrees which minimizes M(θ) even though they do not
provide orthogonality to the users. The reason being; for BPSK
constellation, the SNR values of 10 db and higher are enough
to make the additive noise at the destination is negligible and
hence a non zero angle of rotation (not necessarily 90) is
sufﬁcient for both users to communicate 1 bit each. In general,
multiple optimal angles exist for any alphabet at values of SNR
beyond which the capacity region saturates.
2) Capacity regions of a GMAC with S1 =QPSK: Capacity
regions for QPSK alphabet pair is shown with optimal rotation
and without rotation at different SNR values in Fig. 3. It is
to be observed that rotation provides enlarged capacity region
from the SNR value of 2 db onwards. However, at SNR = 0
db, capacity regions with optimal rotation and without rotation
coincides. The percentage increase in I(x2 : y) ranges from
4.3 percent at 2 db to 100 percent asymptotically. At SNR = 6
db, capacity region of a GMAC with Gaussian alphabets is also
provided and it can be observed that the capacity region with
Gaussian alphabets contains the capacity region of a GMAC
with QPSK alphabet.


## Page 5


5
M(θ) = arg
min
θ∈(0,2π)
N−1
X
k1=0
N−1
X
k2=0
log2
"N−1
X
i1=0
N−1
X
i2=0
exp
 −|x1(k1) −x1(i1) + eiθ(x1(k2) −x1(i2))|2/4σ2
#
.
(5)
I
′(x2 : y) =
N1−1
X
k1=0
N2−1
X
k2=0
E
"
log2
"PN1−1
i1=0
PN2−1
i2=0 exp
 −|x1(k1) + x2(k2) −x1(i1) −x2(i2) + z|2/σ2
PN1−1
i1=0 exp (−|x1(k1) −x1(i1) + z|2/σ2)
##
.
(6)
I
′′(x2 : y) =
N1−1
X
k1=0
N2−1
X
k2=0
E
"
log2
"N1−1
X
i1=0
N2−1
X
i2=0
exp
 −|x1(k1) + x2(k2) −x1(i1) −x2(i2) + z|2/σ2
##
|
{z
}
λ(k1,k2)
.
(7)
TABLE I
TWO-TUPLES (a, b) FOR M-PSK AND M-QAM ALPHABETS FOR SOME M : a - θ∗. b - MULTIPLICITY OF θ∗(FROM SNR = -2 DB TO SNR = 16 DB)
SNR in db
BPSK
QPSK
8-QAM
8-PSK
16-PSK
-2
(90, 1)
(45.0, 1)
(90, 1)
(22.5, 1)
(01.43, 1)
0
(90, 1)
(45.0, 1)
(90, 1)
(22.5, 1)
(09.12, 2)
2
(90, 1)
(45.0, 1)
(90, 1)
(22.5, 1)
(21.37, 1)
4
(90, 1)
(45.0, 1)
(90, 1)
(22.5, 1)
(11.25, 1)
6
(90, 1)
(45.0, 1)
(90, 1)
(22.5, 1)
(11.25, 1)
8
(90, 1)
(35.1, 2)
(110.12, 1)
(22.5, 1)
(11.25, 1)
10
(90, 118)
(58.1, 1)
(61.62, 1)
(18.5, 1)
(11.25, 1)
12
(90, 775)
(30.8, 1)
(119.25, 1)
(16.0, 1)
(09.50, 1)
14
(90, 1269)
(30.5, 1)
(118.75, 1)
(15.3, 1)
(10.56, 1)
16
(90, 1609)
(30.3, 2)
(118.0, 1)
(15.1, 1)
(08.31, 2)
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
R1
R2
snr = 2 db
without rotation
with rotation
snr = −2 db
Gaussian code
alphabet
Fig. 2.
Capacity regions of BPSK alphabet pair with optimal rotation and
without rotation at SNR = -2 and 2 db
D. Two-User GMAC with random phase-offsets
In this subsection, capacity regions of a GMAC computed
using the channel model presented in (1) are compared with
those of a GMAC when random phase offsets are introduced
in the channel. The GMAC channel model with random
offsets has been considered in [6], wherein the constellation
constrained capacity of the resulting sum alphabet has been
computed in an AWGN channel. For such a setup, it is clear
that the problem of designing UD alphabet pairs is completely
avoided. However, there will be a loss in the CC sum capacity
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
2.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
2.2
2.4
R1
R2
snr = 0 db
snr = 6 db
2 db
4 db
without rotation
with rotation
Gaussian alphabet
Fig. 3.
Capacity regions of QPSK alphabet pair with optimal rotation and
without rotation at SNR = 0, 2, 4 and 6 db
since the relative angle between the alphabets is a random
variable which can also take values other than θ∗. Since
I(x2 : y) is the only term which is variant to rotations,
we have plotted I(x2 : y) at different SNR values with and
without random offsets for BPSK and QPSK alphabet pairs in
Fig. 4 and Fig. 5 respectively. For the case with no random
offsets, values of θ∗presented in Table I are used to maximise
I(x2 : y).


## Page 6


6
0
2
4
6
8
10
12
14
16
18
0.55
0.6
0.65
0.7
0.75
0.8
0.85
0.9
0.95
1
SNR in db
I(x2:y)
with random offsets
with optimal angle
Fig. 4.
I(x2 : y) for BPSK alphabet pair with (i) random offsets and (ii)
without random offsets
0
2
4
6
8
10
12
14
16
18
0.5
1
1.5
2
SNR in db
I(x2:y)
with random offsets
with optimal rotation
Fig. 5.
I(x2 : y) for QPSK alphabet pair with (i) random offsets and (ii)
without random offsets
III. TRELLIS CODED MODULATION (TCM) FOR A
TWO-USER GMAC
In this section, we design code pairs based on TCM for
a two-user GMAC to achieve sum rates, R1 + R2 close to
the CC sum capacity of the channel (given in (4)). Towards
that direction, the following proposition indicates the need for
coding by both the users.
Proposition 1: For a two-user GMAC, if one of the users
is equipped with a TCM based trellis code, then the other user
also needs to employ a TCM based trellis code to achieve sum
rates close to the sum capacity.
Proof:
If User-1 employs TCM and User-2 performs
uncoded transmission, then for any trellis, T1 chosen by User-
1, since User-2 has a trivial trellis, the sum trellis, Tsum (See
Deﬁnition 2) will have parallel paths. For a trellis with parallel
paths, it is well known that the minimum accumulated squared
Euclidean distance of the trellis is equal to the minimum
squared Euclidean distance between the points labelled along
the parallel paths. Hence, in order to achieve larger values of
minimum accumulated Euclidean distance in the sum trellis,
both the users need to employ trellis codes with larger number
of states so that sum rates close to the CC sum capacity can
be achieved
i
−i
1
−1
w1
w2
w3
w4
Signal set − 1
Signal set − 2
Fig. 6.
Code alphabets used by User-1 and User-2
For each i = 1, 2, let User-i be equipped with a convo-
lutional encoder Ci with mi input bits and mi + 1 output
bits. Throughout the section, we consider convolutional codes
which add only 1-bit redundancy. Let the mi + 1 output bits
of Ci take values from a 2-dimensional signal set Si such that
|Si| = 2mi+1. Henceforth, the codes C1 (set of codewords
generated from C1) and C2 (set of codewords generated from
C2) are represented by trellises T1 and T2 respectively. The
sum trellis, Tsum for the trellis pair (T1, T2) is introduced in
the following deﬁnition:
Deﬁnition 2: Let
T1
and
T2
represent
two
trellises
with n + 1 stages having the state complexity proﬁles
{q1,0, q1,1, · · · q1,n} and {q2,0, q2,1, · · · q2,n} respectively. Let
Ea
1,i and Eb
2,i respectively denote the edge sets originating
from the state (a) of T1 and the state (b) of T2 in the i-th
stage where 1 ≤a ≤q1,i and 1 ≤b ≤q2,i. Let the edge
sets Ea
1,i and Eb
2,i be labelled with the symbols of the sets X a
i
and Yb
i respectively. For the above trellis pair, the sum trellis,
Tsum is a n + 1 stage trellis such that
• The state complexity proﬁle is,
{q1,0q2,0, q1,1q2,1, · · · q1,nq2,n}
where a particular state in the i-th stage is denoted by
(a, b) such that 1 ≤a ≤q1,i and 1 ≤b ≤q2,i.
• The edge set originating from the state (a, b) in the i-th
stage is given by E(a,b)
i
= Ea
1,i × Eb
1,i. In particular, if
2m1 and 2m2 edges originate from state (a) and state (b)
of T1 and T2 in the i-th stage respectively, then 2m1+m2
edges originate from the state (a, b) in the i-th stage.
• The edges of the set E(a,b)
i
are labelled with the symbols
of the set X a
i + Yb
i .
Example 1: For the trellis pair (shown in Fig. 8) labelled
with elements of S1 and S2 (shown in Fig. 6), the sum trellis
Tsum is as shown in Fig. 9 which is labelled with the elements
of Ssum (shown in Fig. 7).
We assume that the destination performs joint decoding
of the symbols of User-1 and User-2 by decoding for a
sequence over Ssum on the sum trellis, Tsum. For the trellis
pair (T1, T2) and the alphabet pair (S1, S2), the destination
views an equivalent SISO AWGN channel with a virtual source
equipped with the trellis, Tsum labelled with the elements of
Ssum. Recall that for a SISO AWGN channel, if the source
is equipped with a trellis, T and an alphabet S, the following
design rules have been suggested in [10] to construct good
trellis codes.
• All the symbols of S should occur with equal frequency


## Page 7


7
S1
S2
S4
S11
S12
S14
S15
S7
S8
S3
S13
S10
S9
S16
S6
S5
Fig. 7.
Sum alphabet, Ssum for the signal sets presented in Fig. 6.
1 
2
2
1 
2’
1’
1’
2’
T2
T1
( i, −i )
( −1, 1 )
( w1, w2 )
( w3, w4 )
Fig. 8.
Two state trellises of User-1 (T1) and User -2 (T2).
and with some amount of regularity.
• Transitions originating from the same state (or joining
the same state) must be labelled with subsets of S whose
minimum Euclidean distance is maximized.
Due to the existence of an equivalent AWGN channel in
the GMAC set-up, the sum trellis, Tsum has to be labelled
with the elements of Ssum satisfying the above design rules.
However, from the design point of view, such a labelling rule
can be obtained on Tsum only through the pairs (T1, T2) and
(S1, S2). Hence, in this section, we propose labelling rules on
T1 and T2 using S1 and S2 respectively such that Tsum is
labelled with the elements of Ssum as per Ungerboeck rules.
The problem statement has been elaborately explained below.
Since the number of input bits to Ci is mi, there are 2mi
edges diverging from (or converging to; henceforth, we only
refer to diverging edges) each state of Ti. Also, as there is only
one bit redundancy to be added by the code and |Si| = 2mi+1,
the edges diverging from each state have to be labelled with
the elements of a subset of Si of size 2mi. Therefore, for
each i, Si has to be partitioned in to two sets S1
i and S2
i and
the diverging edges from each state of Ti have to be labelled
with the elements of either S1
i or S2
i . From the deﬁnition of a
sum trellis, there are 2m1+m2 edges diverging from each state
of Tsum which gets labelled with the elements of one of the
(1, 1’)
(1, 2’)
(2, 1’)
(2, 2’)
(1, 1’)
(1, 2’)
(2, 1’)
(2, 2’)
( S1, S12, S16, S5 )
( S2, S9, S13, S6 )
( S3, S14, S10, S7 )
( S8, S15, S11, S4 )
Fig. 9.
Sum trellis, Tsum of trellises T1 and T2 presented in Fig. 8.
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
Fig. 10.
The structure of Ssum when S1 = 8-PSK and θ = π
8
following sets,
A =
n
Si
1 + Sj
2 ∀i, j = 1, 2
o
.
As per the Ungerboeck design rules, the transitions originating
from the same state of Tsum must be assigned symbols that are
separated by largest minimum distance. Hence, the problem
addressed in this section is to ﬁnd an optimal partitioning of
Si in to two sets S1
i and S2
i of equal cardinality such that the
minimum squared Euclidean distance of each one of the sets
in A is maximized. However, since dmin of the sets in A can
potentially be different, we try to ﬁnd an optimal partitioning
such that the minimum of the dmin values of the sets in A is
maximized.
In particular, we try to propose solution to the above
problem when S1 and S2 are symmetric M-PSK signal sets
such that S2 = eiθS1 for any θ satisfying 0 < θ <
2π
M
where M = 2r for r ≥1. Note that S2 = eiθS1 implies
m1 = m2. As a ﬁrst step towards solving the above problem,
in the following subsection, we study the structure of the sum
alphabet, Ssum of two M-PSK signal sets which are of the
form S2 = eiθS1 for any θ satisfying 0 < θ < 2π
M .
A. Structure of Ssum when S1 is a M-PSK signal set
Let S1 and S2 represent two symmetric M-PSK signal sets
such that S2 = eiθS1 where 0 < θ < 2π
M . Let x(n) and x′(n)
denote the points e
i2πn
M
and e
i2πn
M eiθ of S1 and S2 respectively


## Page 8


8
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
Fig. 11.
The structure of Ssum when S1 = 8-PSK and θ =
π
12
for 0 ≤n ≤M −1. The sum alphabet, Ssum of S1 and S2
is given by,
Ssum = S1 + S2 = {x(n) + x′(n′) | ∀0 ≤n, n′ ≤M −1} .
Alternatively, Ssum can be written as given in (8) (at the
top of the next page) where x(n) + x′(n + m) = e
i2πn
M
+
ei{ 2π(n+m)
M
+θ} and x(n) + x′(n −m −1)
=
e
i2πn
M
+
ei{ 2π(n−m)
M
−θ} such that x′(−p) = x′(M −p) for any 0 ≤p ≤
M −1. The phase components of the points x(n)+x′(n+m)
and x(n) + x′(n −m −1) are given by
2πn
M
+ πm
M + θ
2
and 2πn
M −π(m+1)
M
+ θ
2 respectively. For a ﬁxed m, the set
of points of the form x(n) + x′(n + m) lie on a circle of
radius 2cos( πm
M + θ
2) and let that circle be denoted by Om.
Similarly, for a ﬁxed m, the collection of points of the form
x(n)+x′(n−m−1) lie on a circle of radius 2cos( π(m+1)
M
−θ
2)
and the circle is denoted by Im. Therefore, Ssum takes the
structure of M concentric PSK signal sets (as shown in Fig.
11). The structure of Ssum for a 8-PSK signal set is shown in
Fig. 10 and Fig. 11 for θ = π
8 and θ =
π
12 respectively. The
set containing the radii of the M circles is given by
R =

2cos(πm
M + θ
2), 2cos(π(m + 1)
M
−θ
2 ) | ∀0 ≤m ≤M
2 −1
ﬀ
.
Henceforth, throughout the section, r(Om) and r(Im) denote
the radius of the circle Om and Im respectively. Note that
when θ = π/M, r(Om) = r(Im) and hence Ssum has the
structure of M
2 concentric PSK signal sets (as shown in Fig.
10). For θ ∈
 0, π
M

, it can be veriﬁed that the structure
of S1 + eiθS1 is identical to that of S1 + ei(θ+ π
M )S1 and
henceforth, we consider values of θ such that 0 < θ <
π
M .
Note that the elements of R satisﬁes the following relation,
r(IM/2−1) ≤r(OM/2−1) ≤r(IM/2−2) ≤r(OM/2−2) ≤· · · ≤r(O0).
For the elements of R, the following three propositions can
be proved using standard trigonometric identities :
Proposition 2: The sequence

r(Ok) −r(Ik)
	
from k = 0
to M/2 −1 is an increasing sequence.
Proposition 3: The
sequence

r(Ok) −r(Ik+1)
	
from
k = 0 to M/2 −2 is an increasing sequence.
Proposition 4: The
sequence

r(Ik) −r(Ok+1)
	
from
k = 0 to M/2 −2 is an increasing sequence.
Proposition 5: Using the phase information of each point
in Ssum, the following observations can be made:
1) The angular separation between the two points x(n) +
x′(n+m) and x(n′)+x′(n′+m) on Om is 2π(n−n′)
M
for
all m = 0 to M/2−1. Similarly, the angular separation
between the two points x(n) + x′(n −m −1) and
x(n′) + x′(n′ −m −1) on Im is
2π(n−n′)
M
for all
m = 0 to M/2 −1.
2) The angular separation between the point, x(n)+x′(n+
m) on Om and the point x(n′) + x′(n′ −m −1) on Im
is 2π(n−n′)
M
+ π(2m+1)
M
for all m = 0 to M/2 −1.
3) The angular separation between the point x(n)+x′(n+
m) on Om and the point x(n′)+x′(n′−(m−1)−1) on
Im−1 is 2π(n−n′)
M
+ π(2m)
M
for all m = 1 to M/2 −1.
4) The
angular
separation
between
the
point
x(n) + x′(n −m −1)
on
Im
and
the
point
x(n′)+x′(n′ +(m−1)) on Om−1 is 2π(n−n′)
M
−π(2m)
M
for all m = 1 to M/2 −1.
In the next subsection, ﬁrst, we partition each Si in to two
groups using Ungerboeck rules and then, exploiting the struc-
ture of Ssum, we compute the minimum Euclidean distance,
dmin of each one of the sets in A.
B. Structure of each one of the sets in A induced by the
Ungerboeck partitioning on S1 and S2
For each i = 1, 2, let Si be partitioned in to two sets of equal
size using Ungerboeck rules which results in two sets denoted
by Se
i and So
i such that dmin of Se
i and So
i is maximized.
Since the number of sets resulting from the partition is two,
the minimum angular separation, φmin between the points in
each set is 4π
M . The two sets of Si are of the form,
Se
i = {x(n) | n = 2m for 0 ≤m ≤M/2 −1} and
So
i = {x(n) | n = 2m + 1 for 0 ≤m ≤M/2 −1} .
It is clear that the sets Se
1 + So
2, Se
1 + Se
2, So
1 + So
2 and
So
1 + Se
2 ∈A form a partition of Ssum. In the rest of this
subsection, we obtain the dmin values of the above sets.
Throughout this section, the set Sα
1 + Sβ
2 and its minimum
distance
are
denoted
by
Sαβ
sum
and
dαβ
min
respectively
∀α, β = e and o. Without loss of generality, only the structure
of Seo
sum and See
sum are studied since the structure of Soe
sum
and Soo
sum are identical to that of Seo
sum and See
sum respectively.
1) Calculation of dmin of Se
1 + So
2: The elements of Se
1 +
So
2 (as given in (9)) are of the form x(n) + x′(n + m) and
x(n)+x′(n−m−1) where n takes even numbers while n+m
and n −m −1 take odd numbers. When m is odd, note that
n+m is odd and n−m−1 is even and hence Se
1 +So
2 will have
no points on Im and M/2 points on Om. Similarly, when m
is even, Se
1 + So
2 will have no points on Om and M/2 points
on Im. Therefore, Se
1 + So
2 will have points on the following
set of circles

OM/2−1, IM/2−2, OM/2−3, · · · , O1, I0	
.


## Page 9


9
Ssum = {x(n) + x′(n + m), x(n) + x′(n −m −1) | ∀0 ≤n ≤M −1 and 0 ≤m ≤M/2 −1}
(8)
Se
1 + So
2 = {x(n) + x′(n′) | n = 2m and n′ = 2m′ + 1 ∀m, m′ = 0 to M/2 −1} .
(9)
Since n takes only even values, using observation 1) of
Proposition 5, φmin between the points of Se
1 + So
2 on any
circle is
4π
M . Hence the points of Se
1 + So
2 are maximally
separated on every circle. Also, φmin between the points
placed on consecutive circles has to be calculated. From
observation 3) of Proposition 5, φmin between the points in
Oq and Iq−1 is 2π
M for all q = 1 to M/2 −1. Similarly φmin
between the points in Iq and Oq−1 is 0 for all q = 2 to
M/2 −2. It can be veriﬁed that the structure of So
1 + Se
2 is
identical to that of Se
1 + So
2.
Proposition 6: r(Iq−1) and r(Oq) satisfy the following
inequality for all q = 1 to M/2 −1,
d(r(Iq−1), r(Oq)ei 2π
M ) ≥d(r(Oq), r(Oq)ei 2π
M )
Proof: See Appendix I.
Proposition 7: For M ≥8, r(Oq) satisfy the following
inequality for all q = 1 to M/2 −3,
d(r(Oq), r(Oq)ei 2π
M ) ≥2r(OM/2−1)sin(2π
M ).
Proof: See Appendix II
Lemma 1: For 0 < θ <
π
M , the minimum distance of the
sets Seo
sum and Soe
sum are given by
doe
min = deo
min = min
„
d(r(Iq−1), r(Oq)ei 2π
M ), 4sin
„ π
M −θ
2
««
.
(10)
Proof: See Appendix III.
2) Calculation of dmin of Se
1 + Se
2: The set Se
1 + Se
2 is
as given in (11). The elements of Se
1 + Se
2 are of the form
x(n) + x′(n + m) and x(n) + x′(n −m −1) where n, n + m
and n −m −1 take even values. When m is odd, note that
n + m is odd and n −m −1 is even. Hence, the set Se
1 + Se
2
will have no points on Om and M/2 points on Im. Similarly,
when m is even, Se
1 +Se
2 has no points on Im and M/2 points
on Om.
Therefore, Se
1 + Se
2 will have points on the following set
of circles

IM/2−1, OM/2−2, IM/2−3, · · · , I1, O0	
. Since n
takes only even values, using observation 1) of Proposition 5,
φmin between the points of Se
1+Se
2 for a given m is 4π
M . Hence
the points of Se
1 +Se
2 are maximally separated on every circle.
From observation 4) of Proposition 5, φmin between the points
in Iq and Oq−1 is 2π
M for all q = 1 to M/2 −1. Similarly
φmin between the points in Oq and Iq−1 is 0 for all q = 2 to
M/2 −2. It can be veriﬁed that the structure of So
1 + So
2 is
identical to that of Se
1 + Se
2.
Proposition 8: For M ≥8, r(Iq) satisﬁes the following
inequality for q = 1 to M/2 −3,
d(r(Iq), r(Iq)ei 2π
M ) ≥2r(IM/2−1)sin(2π
M ).
Proof:
We
know
that
2r(IM/2−1)sin( 2π
M )
=
4sin( θ
2)sin( 2π
M ) and d(r(Iq), r(Iq)ei 2π
M ) = 4cos( π(q+1)
M
−
θ
2)sin( π
M ). Since q ≤M/2−3, π(q+1)
M
−θ
2 ≤π
2 −2π
M −θ
2 ≤π
2 .
Hence, for all values of θ and 1
≤
q
≤
M/2 −3,
cos( π
2 −2π
M −θ
2) ≥cos( π
2 −2π
M ) = sin( 2π
M ). Therefore,
2r(IM/2−1)sin( 2π
M )
d(r(Iq), r(Iq)ei 2π
M )
≤sin( θ
2)
sin( π
M ) ≤1.
This completes the proof.
Proposition 9: r(Oq−1) and r(Iq) satisﬁes the following
inequality for q = M/2 −1,
d(r(Oq−1), r(Iq)) ≥2r(IM/2−1)sin(2π
M ).
Proof: The inequality is straightforward to prove using
standard trigonometric identities.
Lemma 2: For 0 < θ <
π
M , the minimum distance of the
sets See
sum and Soo
sum is
dee
min = doo
min = 4sin
θ
2

sin
2π
M

.
(12)
Proof: See Appendix IV.
C. Optimality of Ungerboeck partitioning
In the preceding subsection, dmin values of each one of
the sets of A induced by Ungerboeck partition on S1 and S2
have been computed in (10) and (12). Note that when θ =
π
M ,
dee
min = deo
min. In this subsection, using these values, we show
that for θ =
π
M , a non-Ungerboeck partition on S1 and S2
results in a set A such that the dmin of at least one of the sets
in A is lesser than dee
min.
Theorem 2: For θ =
π
M , Ungerboeck partitioning on S1
and S2 in to two sets is optimal in maximizing the minimum
of the dmin values of the sets in A.
Proof: Let S1
i and S2
i be the two sets resulting from a
partition of Si for i = 1, 2. If either S1 or S2 is not Ungerboeck
partitioned, then it is shown that, dmin of at least one of the
sets in the set A =
n
Si
1 + Sj
2 | ∀i, j = 1, 2
o
is lesser than
4sin( π
2M )sin( 2π
M ) (we have substituted θ =
π
M in (12)). In
other words, φmin between the points of at least one of sets
in A is smaller than 4π
M on OM/2−1 (since θ =
π
M , note that
Om = Im for all m). It is assumed that there are exactly M/2
points on OM/2−1 in each set of A. Otherwise, at least one set
contains more than M/2 points and hence φmin between the
points in that set on OM/2−1 can be at most 3π
M . Therefore,
the sub-optimality of the partition is proved. Without loss of
generality, assume that x(a), x(a + 1) ∈S1
1 for some a such
that 0 ≤a ≤M −2. Irrespective of the partition of S2,
either x′(a + M
2 ) ∈S1
2 or x′(a + M
2 ) ∈S2
2. We assume that
x′(a + M
2 ) ∈S1
2. Hence, x′(a + M
2 ) + x(a), x′(a + M
2 ) +
x(a+1) ∈S1
1 + S1
2 which lie on OM/2−1. Note that, x′(a+ M
2 )
+ x(a) and x′(a+ M
2 ) + x(a+1) have an angular separation of
(N+1)π
N
. With this, the rest of the M/2 −2 points get placed
on OM/2−1 in one of the following two ways : (i) at least
M/4 −1 points appear between 0 and - π(M−1)
M
radians due


## Page 10


10
Se
1 + Se
2 = {x(n) + x′(n′) | n = 2m and n′ = 2m′ ∀m, m′ = 0 to M/2 −1} .
(11)
to which at most M/4 −1 points lie between 0 to π(M+1)
M
radians (ii) at least M/4 points appear between 0 and π(M+1)
M
radians due to which at most M/4 −2 points lie between 0
and - π(M−1)
M
radians. For the case in (i), at least M/4 points
have to appear from 0 and - π(M−1)
M
radians, due to which
φmin between them can at most be
4π(M−1)
M2
which is less
than 4π
M . Similarly, for the case in (ii), it can be shown that
φmin between the set of points which lie from 0 to π(M+1)
M
radians is lesser than 4π
M . This completes the proof.
For M-PSK signal sets, when θ ̸=
π
M , the optimal parti-
tioning on S1 and S2 is not known. However, we present an
example wherein for a particular value of θ, a non-Ungerboeck
partition on S1 and S2 results in a set A such that the dmin
of all the sets in A is larger than min (dee
min, deo
min).
Example 2: S1 is a uniform 8-PSK signal set with θ = π
25.
The partition of S1 and S2 are given by,
S1
1 = {x(1), x(2), x(4), x(6)} ,
S1
2 = {x′(1), x′(4), x′(5), x′(8)} ,
S2
1 = {x(3), x(5), x(7), x(8)} and
S2
2 = {x′(2), x′(3), x′(6), x′(7)} .
Nevertheless, in the following theorem, we show that, for
some class of partitions, (for any θ ∈
 0, π
M

), minimum
Euclidean distance of at least one of the sets in A is lesser
than min (dee
min, deo
min).
Theorem 3: For θ ∈
 0, π
M

, if the partition of S1 and S2
are such that x(a), x(a + 1) and x(a + 2) ∈Sj
1 for some
j = 1, 2 and 0 ≤a ≤M −3, then the dmin of at least one of
the sets in A is lesser than min (dee
min, deo
min).
Proof: Assume x(a), x(a+1) and x(a+2) ∈S1
1. Among
the three points, x′(a−M/2), x′(a+1−M/2) and x′(a+2−
M/2), two of them must belong to either S1
2 or S2
2. Without
loss of generality, assume two of them belong to S1
2. If x′(a−
M/2), x′(a + 1 −M/2) ∈S1
2, then x(a) + x′(a −M/2),
x(a + 1) + x′(a + 1 −M/2) ∈S1
1 + S1
2 such that the two
points lie on IM/2−1 with an angular separation of 2π
M . Hence
the distance between the two points is lesser than dee
min. Same
result can be proved if x′(a + 1 −M/2), x′(a + 2 −M/2) ∈
S1
2. Finally, if x′(a −M/2), x′(a + 2 −M/2) ∈S1
2, then
x(a) + x′(a −M/2), x(a + 2) + x′(a + 2 −M/2) ∈S1
1 + S1
2
lies on IM/2−1 with an angular separation of 4π
M .
D. TCM with M-PAM signal sets
In the previous subsection, a systematic method of labelling
the trellis pair (T1, T2) has been obtained when M-PSK signal
sets (with θ∗=
π
M ) are employed by both the users. In
this subsection, we consider designing TCM schemes with
M-PAM signal sets for both the users. For such a set-up,
using the metric presented in Theorem 1, it can be veriﬁed
that θ∗=
π
2 ∀M and for all values of SNR. Recall that,
when M-PSK signal sets are employed, Ssum takes the
structure of concentric PSK signal sets. However, when M-
PAM signal sets are used, Ssum is a regular M 2-QAM (since
∀SNR, θ∗= π
2 ). In this set-up, for a chosen trellis pair, the
destination sees the corresponding sum trellis, Tsum labelled
with symbols from a M 2-QAM signal set. If the destination
decodes for every l channel uses and x1 ∈Sl
1 (S1 = M-
PAM signal set) and x2 ∈Sl
2 (S2 = e
iπ
2 S1) represent the
codewords of User-1 and User-2 respectively, the received
sequence at the destination is given by y = xsum + n where
xsum = x1 + x2 ∈Sl
sum (where Ssum = M 2-QAM) and
n ∼CN
 0, σ2Il

. The decoding metric is given by,
ˆxsum = arg min
xsum ||y −xsum||2.
Since yI and yQ respectively are dependent on x1 and x2
only (where yI and yQ denote the in-phase and quadrature
components of y), the above decoding metric splits as follows,
ˆx1 = arg min
x1∈C1 ||yI −x1||2 and ˆx2 = arg min
x2∈C2 ||iyQ −x2||2.
Therefore, the destination can decode for a sequence over M-
PAM alphabet on the individual trellises T1 and T2 instead of
decoding for a sequence over M 2 QAM alphabet on Tsum.
Since, decoding for the symbols of one user is independent
of the decoding for the symbols of the other, trellises T1
and T2 has to be labelled based on Ungerboeck rules as
done for a SISO-AWGN channel. Hence, all the TCM based
trellis codes with M-PAM alphabets existing for SISO AWGN
are applicable in the two-user GMAC setup. With this, the
decoding complexity at the destination is signiﬁcantly reduced
as the state complexity proﬁle of the trellis over which the
decoder works is {qi,0, qi,1, · · · qi,n} (when decoding for
User-i) instead of {q1,0q2,0, q1,1q2,1, · · · q1,nq2,n}. In gen-
eral, when a complex signal set is used by either one of the
users, the destination has to necessarily decode for a sequence
over Ssum on Tsum which has high decoding complexity.
From the above discussion, it is clear that for a two-user
GMAC, one dimensional signal sets can be preferred over
complex signal sets for reducing the decoding complexity.
However, it is not clear if there is any loss in the CC sum
capacity by using single dimensional signal sets. As a ﬁrst
step towards answering the above question, in Fig. 12, we
have plotted the sum CC capacity (i.e. R1 +R2) as a function
of SNR for two scenarios; (i) when QPSK signal sets are used
with angles of rotation as given in Table I and (ii) when 4-
PAM signal sets are used with θ∗= π
2 . For both the scenarios,
average energy per symbol per user is made the same. As
shown in the plot, there is a marginal difference in the CC sum
capacity between the two schemes and in particular, at high
SNR the sum capacity of the later scheme is larger than the
former. Therefore, using 4-PAM signal sets provide reduced
decoding complexity with almost the same CC sum capacity as
that of QPSK signal sets. Similar curves have been obtained in
Fig. 13 for the following two scenarios (i) when User-1 and
User-2 uses QPSK and BPSK signal set respectively (with


## Page 11


11
0
2
4
6
8
10
12
14
16
18
1.5
2
2.5
3
3.5
4
SNR in db
sum capacity
QPSK alphabet pair
4−PAM alphabet pair
Fig. 12.
Capacity of the sum alphabet of QPSK signal sets and 4-PAM
signal sets with optimal rotation.
0
2
4
6
8
10
12
14
16
18
1.4
1.6
1.8
2
2.2
2.4
2.6
2.8
3
SNR in db
sum capacity
QPSK and BPSK with optimal rotation
4−PAM and BPSK with optimal rotation
Fig. 13.
Capacity of the sum alphabet of QPSK/BSK signal sets and 4-
PAM/BPSK signal sets with optimal rotation.
appropriate angle of rotation) and (ii) when User-1 uses 4-
PAM signal set, User-2 uses BPSK with θ∗= π
2 .
For arbitrary values of M, we conjecture that M-PAM
signal sets (with a relative rotation of
π
2 ) provide sum ca-
pacities which are marginally close to that of M-PSK and
M-QAM signal set pairs (with appropriate rotation) with
the same average energy. Note that the above relation can
also be observed in a two-user GMAC with Gaussian code
alphabets. If x1, x2 ∼CN
 0, ρ
2

, the received symbol at the
destination is given by y = x1 + x2 + n where we assume
that n ∼N
 0, 1
2

in each dimension. The sum capacity for
the above model is
log2(1 + ρ
2) + log2(1 +
ρ
2 + ρ) = log2(1 + ρ).
Note that, the capacities for User-1 and User-2 are log2(1+ ρ
2)
and log2(1 +
ρ
2+ρ) respectively. However, if x1 ∼N
 0, ρ
2

and x2 = ix′
2 such that x′
2 ∼CN
 0, ρ
2

, the capacity in each
(1)
(2)
(4)
(3)
(1)
(2)
(3)
(4)
Fig. 14.
Trellis structure employed by both the users.
dimension is
1
2log2(1 + ρ)
and hence the sum capacity is log2(1 + ρ) which is equal to
the sum capacity of complex Gaussian alphabets. For the later
scheme, the capacity for User-1 and User-2 is 1
2log2(1 + ρ).
When the individual capacities for each user are compared
between the two schemes, it is clear that, for one of the users,
the capacity will be larger in the later scheme and smaller in
the former scheme whereas for the other user, capacity will be
larger in the former scheme and smaller in the later scheme
there by making the sum capacity of both the schemes equal.
Hence, the capacity region of real Gaussian alphabets (with
θ = π
2 ) lies inside the capacity region of complex Gaussian
alphabets with only one point of intersection.
In a SISO AWGN channel, it is well known that, for a
given SNR, one dimensional signal sets incur some loss in the
CC capacity when compared to well packed complex signal
sets having the same average energy and equal number of
points. Note that, the CC capacity of individual signal sets,
S1 and S2 are of little importance in the GMAC set-up, since
for an input alphabet pair (S1, S2), the destination sees an
equivalent AWGN channel with the corresponding Ssum as
its input (neither S1 nor S2). Hence, in order to maximize
the sum capacity, the alphabet pair (S1, S2) has to be chosen
such that CC capacity of Ssum is maximized. Since we have
shown that, for a given SNR, the sum capacity of 4-PAM
alphabet pair is marginally close to that of a QPSK alphabet
pair, we conjecture that for any M, M-PAM alphabet pairs
(with θ∗= π
2 ) do not incur signiﬁcant loss in the sum capacity
when compared to M-PSK and M-QAM alphabet pairs in a
two-user GMAC.
1) Examples and Numerical results: In this subsection,
we present numerical results on the minimum accumulated
squared Euclidean distance, d2
free,min of Tsum when the trellis
presented in Fig. 14 is employed by both the users using QPSK
and 4-PAM signal sets. For the trellis in Fig. 14, Tsum is as
shown in Fig. 15. We compute d2
free,min for the following
two scenarios (i) when the individual trellises are labelled
with unit energy QPSK signal sets (with an angle of rotation
π
4 ) using the Ungerboeck rules. (ii) when the trellises are
labelled with 4-PAM signal sets,
p
( 1
5) {−3, −1, 1, 3} (with
θ∗= 90o) using Ungerboeck rules. For scenario (i), d2
free,min
is 5.8578 where as for scenario (ii), d2
free,min is 7.20. Hence,


## Page 12


12
(1,4’)
(2,2’)
(2,1’)
(2,3’)
(2,4’)
(3,1’)
(3,2’)
(3,3’)
(3,4’)
(4,1’)
(4,2’)
(4,3’)
(4,4’)
(1,3’)
(1,2’)
(1,1’)
(1,1’)
(1,2’)
(1,3’)
(1,4’)
(2,1’)
(2,2’)
(2,3’)
(2,4’)
(3,1’)
(3,2’)
(3,3’)
(3,4’)
(4,1’)
(4,2’)
(4,3’)
(4,4’)
Fig. 15.
Tsum for the trellis pair presented in Fig. 14.
the asymptomatic coding gain of 0.89 db can be obtained by
using 4-PAM signal sets over QPSK signal sets. When the
alphabets in the scenarios discussed are used on the trellis
pair presented in Fig. 8, the corresponding asymptotic coding
gain is 0.57 db.
IV. SPACE TIME CODING FOR TWO-USER MIMO-MAC
In this section, we introduce a two-user MIMO (Multiple
Input Multiple Output) MAC model and propose construction
of two different classes STBC pairs with certain nice prop-
erties. In the following subsection, the MIMO-MAC model
considered in this paper has been described.
A. Channel model of two-user MIMO-MAC
The two-user MIMO-MAC model considered in this paper
consists of two sources each equipped with Nt antennas and a
destination equipped with a single antenna. The channel from
the i-th antenna of the j-th user to the destination is a quasi-
static block fading channel denoted by hji ∀i = 1 to Nt and
j = 1, 2 where each hji ∼CN (0, 1) with the coherence time
interval of at least l channel uses. For each j, if xj ∈C1×Nt is
the vector transmitted by User-j such that every symbol of xj
has average unit energy, the received symbol at the destination
for every channel use is given by
y =
r ρ
2Nt
x1h1 +
r ρ
2Nt
x2h2 + n,
(13)
where n ∼CN (0, 1) is the additive noise at the destination,
hT
j
= [hj1 hj2 · · · hjNt] and ρ is the average receive SNR
at the destination. Throughout the paper, we assume the
perfect knowledge of CSI (Channel State Information) at the
destination which is commonly referred as CSIR. The two-
user MIMO-MAC model described above is referred as a
(Nt, Nt, 1) MIMO-MAC. It is clear that the sum capacity of a
(Nt, Nt, 1) MIMO-MAC is equal to the capacity of a 2Nt ×1
MIMO channel (with CSIR) which is given by
C(Nt, Nt, 1) = E

log2

1 +
ρ
2Nt
 h1hH
1 + h2hH
2

(14)
where the expectation is over the random variables |hji|2 ∀i, j.
We also assume the perfect knowledge of the phase component
of hji at the j-th user ∀i, j which we refer as CSIT-P. The
(Nt, Nt, 1) MIMO-MAC with the assumption of CSIT-P is
referred as the (Nt, Nt, 1, p) MIMO-MAC where p highlights
the assumption of CSIT-P in the channel model. Note that, we
do not assume the complete knowledge of hji at the transmit-
ters in which case, optimal power allocation techniques can be
applied to improve the system performance. Since CSIT-P is
known, each transmit antenna can compensate for the rotation
introduced by the channel and hence the channel equation (13)
can be written as
y =
r ρ
2Nt
x1˜h1 +
r ρ
2Nt
x2˜h2 + n,
(15)
where ˜h
T
j = [|hj1| |hj2| · · · |hjNt|]. Suppose, C(Nt, Nt, 1, p)
denotes the sum capacity of a (Nt, Nt, 1, p) MIMO-MAC with
CSIR, it is straightforward to verify that C(Nt, Nt, 1, p) =
C(Nt, Nt, 1). In the rest of this paper, a (Nt, Nt, 1, p) MIMO-
MAC is denoted as a Nt-MIMO-MAC.
The sum capacity of a Nt-MIMO-MAC (which is given by
C(Nt, Nt, 1, p)) is computed by assuming that independent
vectors are transmitted every time instant from both the
users. However, when a Space Time Block Code (STBC) pair
(C1, C2) is employed, the vectors transmitted at every time
instant will not be independent. Let the dimensions of the
STBC used by both the users be l × Nt (where l denotes
the number of complex channel uses). Throughout the paper,
we assume that STBCs for both the users have the same
dimensions. If the l × Nt matrices transmitted by User-1 and
User-2 are X and Y respectively, then the received vector,
y ∈Cl is given by
y =
r ρ
2Nt
X˜h1 +
r ρ
2Nt
Y˜h2 + n,
(16)
where n denoted the complex l×1 additive noise vector. If the
STBCs used are of rate R complex symbols per channel use,
then there are lR independent complex variables for each user
describing the corresponding matrix. Let the vector containing
lR variables of X and Y be denoted by x ∈ClR×1 and
y ∈ClR×1 respectively. Totally, there are 2lR independent
variables denoted by z ∈C2lR×1 where z =

xT yT T . If
X and Y are from linear designs, we can write (16) as given


## Page 13


13
below [22]
y =
r ρ
2Nt
˜Hz + n,
(17)
where ˜H ∈Cl×lR. The capacity of this new channel, ˜H is
the capacity of a collocated MIMO channel with lR transmit
antennas and l receive antennas given by
E

log2

det

Il +
ρ
2Nt
ˆHˆH
H
.
Therefore, after introducing the STBC pair (C1, C2), the max-
imum mutual information between the vector z and y, I(z :
y | ˜H) is given by
CSTBC(Nt, Nt, 1, p) = 1
l E

log2

det

Il +
ρ
2Nt
ˆHˆH
H
where the factor 1
l takes care of the rate loss due to coding
across time. It is clear that the above value cannot be more
than C(Nt, Nt, 1, p). On the similar lines of the deﬁnition of
information lossless STBCs for collocated MIMO channels
[21], information lossless STBC pairs are deﬁned below for a
Nt-MIMO-MAC.
Deﬁnition 3: If the maximum mutual information, I(z :
y | ˜H) when an STBC pair (C1, C2) is used for a Nt-MIMO-
MAC, is equal to the capacity of a 2Nt × 1 MIMO channel,
then the pair (C1, C2) is called an information lossless STBC
pair.
In the rest of the section, we propose two classes of STBC
pairs from Real Orthogonal Designs (RODs) for a Nt-MIMO-
MAC. For deriving certain properties of the codes that we are
going to propose, the following deﬁnition and theorem are
important.
Deﬁnition 4: Let the channel equation of a MISO (Multiple
Input Single Output) system with Nt transmit antennas be
represented by y = xh + n where y is the received symbol
at the destination, n is the additive noise, h is the Nt length
channel vector and x is the input vector to the channel of length
Nt. Such a MISO channel is referred as a single-dimensional
MISO channel whenever x, h ∈RNt.
Theorem 4: STBCs from the rate-1 ROD (which also in-
cludes rate-1 rectangular ROD) for Nt antennas are informa-
tion lossless for a single-dimensional Nt × 1 MIMO channel
for all values of Nt .
Proof: See Appendix V.
Throughout the section, we assume that the destination
performs joint decoding of the symbols of User-1 and User-2
by decoding for a l × 2Nt space-time codeword, Z = [X Y]
in a virtual 2Nt × 1 MIMO channel (where [X Y] denotes
juxtaposing of the matrices X and Y). Therefore, applying the
full diversity design criterion derived for space-time codes in
point to point coherent MIMO channels [14] on the set of
codewords of the form Z, the diversity order of the code pair
(C1, C2) in a Nt-MIMO-MAC is Nt provided each space-time
block code Ci is individually fully diverse for a point to point
coherent MIMO channel.
B. STBC pairs from Separable Orthogonal Designs (SODs)
for a Nt-MIMO-MAC
In this section, we construct STBC pairs (C1, C2) for a Nt-
MIMO-MAC such that the ML-decoding complexity at the
destination is reduced (where C1 is used by User-1 and C2
is used by User-2). The STBC pair (C1, C2) is speciﬁed by
presenting a complex design pair (X, Y) and a signal set pair
(S1, S2) such that C1 and C2 are generated by making the
variables of X and Y take values from S1 and S2 respectively.
In particular, we construct complex design pairs (X, Y) using
the well known class of RODs. The proposed class of complex
designs are introduced in the following deﬁnition.
Deﬁnition 5: Let the l × Nt matrix X represent a ROD in
k real variables for Nt antennas. If every real variable of X is
viewed as a complex variable, then X becomes a design in k
complex variables which we refer as a Separable Orthogonal
Design (SOD).
If a design X represents a SOD, then from Deﬁnition 5,
it is clear that XI and XQ are identical RODs. Also, since
rate-1 RODs exist for ∀Nt, rate-1 SODs (in complex symbols
per channel use) also exist for ∀Nt [15] (except for Nt = 2,
4 and 8, note that all other SODs are rectangular designs).
Throughout the paper, we only consider the class of rate-1
SODs. In the following example, we present a SOD pair for
4-MIMO-MAC in 4 complex variables per user.
Example 3: For Nt = 4, k = 4,
X =


x1
x2
x3
x4
−x2
x1
−x4
x3
−x3
x4
x1
−x2
−x4
−x3
x2
−x1

and
Y =


y1
y2
y3
y4
−y2
y1
−y4
y3
−y3
y4
y1
−y2
−y4
−y3
y2
−y1

.
Towards generating the STBC pair (C1, C2), we restrict the
complex variables of a SOD to take values from the class of
regular-QAM signal sets only. The variables are precluded to
take values from signal sets where the in-phase and quadrature
components are entangled, for example, M-PSK signal sets.
The advantage of choosing a regular-QAM signal set for S1
and S2 is described in the next subsection. When the SOD
pair (X, Y) is used, the received vector at the destination is of
the form
y =
r ρ
2Nt
X˜h1 +
r ρ
2Nt
Y˜h2 + n.
Since the variables of the two designs take values from regular
QAM signal sets and the channels ˜hj’s are real, the Nt-MIMO-
MAC with STBC pairs from SOD pair (X, Y) splits in to
two parallel single-dimensional Nt-MIMO-MACs with STBC
pairs from ROD pairs (XI, YI) and (XQ, YQ) respectively.
For each ♥= I, Q, the channel equation is given by
y♥=
r ρ
2Nt
X♥˜h1 +
r ρ
2Nt
Y♥˜h2 + n♥,


## Page 14


14
where n♥∼N
 0, 1
2IT

. Henceforth, we consider only one of
the single-dimensional channels for all the analysis purposes.
The following theorem shows that STBC pairs from SODs are
information lossless for a Nt-MIMO-MAC ∀Nt.
Theorem 5: For a Nt-MIMO-MAC, STBC pairs from the
rate-1 SOD pair are information lossless.
Proof: Let X and Y represent two l × Nt rate-1 SODs
for Nt antennas in the variables x1, x2 · · · xl and y1, y2 · · · yl
respectively. Using the above design pair, the channel equation
along the in-phase component is
yI =
r ρ
2Nt
XI˜h1 +
r ρ
2Nt
YI˜h2 + nI,
where XI
and YI
are identical RODs in the variables
x1I, x2I · · · xlI and y1I, y2I · · · ylI respectively. Note that X
and Y have the following column vector representations,
XI = [A1xI A2xI · · · ANtxI] ; YI = [B1yI B2yI · · · BNtyI]
where {Ai | i = 1 to Nt} and {Bi | i = 1 to Nt} are the sets
of column vector representation matrices of X and Y respec-
tively and xT
I = [x1I x2I · · · xlI], yT
I = [y1I y2I · · · ylI].
The channel equation along the in-phase component can also
be written as,
yI =
r ρ
2Nt
ˆHzI + nI where
(18)
where the l × 2Nt matrix, ˆH =
h
ˆ
H1 ˆ
H2
i
such that
ˆ
H1 =
PNt
i=1 |h1i|Ai, ˆ
H2 = PNt
i=1 |h2i|Bi and zI =

xT
I yT
I
T . The
capacity of the channel in (18) is
1
2E

log2

det

Il +
ρ
2Nt
ˆHˆH
H
.
Since Ai’s and Bi’s are unitary and AiAT
j + AjAT
i = 0T ×T ,
BiBT
j + BjBT
i
= 0T ×T ∀i, j such that i ̸= j, we have
ˆHˆH
H
=
 h1hH
1 + h2hH
2

Il and hence the capacity of a
single-dimensional Nt-MIMO-MAC along the in-phase com-
ponent with the SOD pair, (X, Y) is
1
2E

log2

1 +
ρ
2Nt
 h1hH
1 + h2hH
2

.
Similarly, the capacity of a single-dimensional Nt-MIMO-
MAC along the quadrature component with the SOD pair,
(X, Y) is
1
2E

log2

1 +
ρ
2Nt
 h1hH
1 + h2hH
2

.
Therefore, the sum capacity is
E

log2

1 +
ρ
2Nt
 h1hH
1 + h2hH
2

which is equal to C(Nt, Nt, 1, p). Hence the SOD pair, (X, Y)
is information lossless for a Nt-MIMO-MAC.
In the following subsection, we discuss the low ML decod-
ing property of SODs.
1) Low ML decoding complexity of SODs: In this subsec-
tion, we show that STBC pairs from SODs are two-group
decodable in a Nt-MIMO-MAC (in particular, we consider
rate-1 SODs). For more details on STBCs with multi-group
decodability for a collocated MIMO channel, we refer the
reader to [20]. Since the designs X and Y are constructed
using rate-1 RODs (wherein the number of real variables is
equal to the number of channel uses), the destination has to
decode a total of 4l real variables (2l for each user) for every
codeword use. Since a Nt-MIMO-MAC with STBC pairs from
the SOD pair (X, Y) breaks down in to two parallel single-
dimensional Nt-MIMO-MACs with STBCs from ROD pairs
(XI, YI) and (XQ, YQ) respectively, for each ♥= I, Q the
ML-decoding metric is given by
ˆX♥, ˆY♥= arg
min
C1♥,C2♥||y −
r α
2Nt
X♥˜h1 +
r α
2Nt
Y♥˜h2||2.
(19)
Therefore, along each dimension, the destination has to jointly
decode only 2l real variables (l variables of each user) for
every codeword use which constitutes l channel uses. For this
set-up, the destination can use a sphere decoder in Rl to decode
l of the 2l real variables where as the remaining l variables
can be decoded using brute force search. Note that when either
(i) CSIT-P is not available or (ii) if the users employ signal
sets wherein the in-phase and the quadrature components of
the complex variables are entangled, the destination has to
jointly decode for 4l real variables (2l variables of each user)
in R2l and hence the decoding complexity is increased. Note
that since CSIT-P is available, the complex signal set used
by one of the users can be relatively rotated with respect to
the other to improve the performance. However, such rotations
will only entangle the in-phase and quadrature components of
the symbols there by increasing the decoding complexity as
mentioned above.
C. STBC pairs from Real Orthogonal Designs for a Nt-
MIMO-MAC
When STBC pairs from SODs are employed for a Nt-
MIMO-MAC, it is clear that the signal transmitted by User-1
is an interference for User-2 and vice-verse. In this subsection,
we propose a new class of STBC pairs from RODs wherein
each user is interference free from the other. In the proposed
scheme, User-1 employs a rate-1 ROD, X for Nt antennas and
User-2 employs an identical ROD, Y. The variables of X take
values from a M-PAM signal set where as the variables of
Y take values from a signal set which is 90 degrees rotated
version of signal set used for X. In general, both users can use
PAM signal sets with different number of points. Since rate-1
RODs exist ∀Nt, the proposed scheme is also applicable for
a Nt-MIMO-MAC ∀Nt.
Example 4: For a 4-MIMO-MAC, the designs, X and Y are
as given in Example 3 where the variables x1, x2 · · · x4 can
take values from S1 = {−3, −1, 1, 3} and y1, y2 · · · y4 can
take values from S2 = {−3i, −1i, 1i, 3i}.


## Page 15


15
In the proposed scheme, the received vector at the destina-
tion is of the form
y =
r ρ
2Nt
X˜h1 +
r ρ
2Nt
Y˜h2 + n.
Since ˜hj’s are real vectors and the two designs take values
from orthogonal signal sets, it is clear that the two users are
interference free from each other. With this the Nt-MIMO-
MAC splits in to two parallel MISO channels (one for each
user) such that the MISO channel from (i) User-1 to the
destination and (ii) User-2 to the destination are given in (20)
and (21) respectively.
yI =
r ρ
2Nt
X˜h1 + nI.
(20)
iyQ =
r ρ
2Nt
Y˜h2 + inQ.
(21)
1) Capacity of a Nt-MIMO-MAC with RODs: Note that
the channels in (20) and (21) are single-dimensional MISO
channels with nI, nQ ∼N
 0, 1
2IT

. Hence, the average
receive SNR in every dimension is ρ. Since the rate-1 ROD for
Nt antennas is information lossless for a single dimensional
Nt×1 MIMO channel (Theorem 4), for j = 1, 2, the maximum
mutual information for User-j is
1
2E

log2

1 + ρ
Nt
hihH
i

.
Therefore, with overloading of notations, the sum capacity of
the proposed scheme is given by,
E

log2

1 + ρ
Nt
h2hH
2

(22)
which is equal to the capacity of a Nt × 1 collocated MIMO
channel for an average SNR value of ρ. However, the sum
capacity of a Nt-MIMO-MAC is given in (14) which is equal
to the capacity of a 2Nt×1 MIMO channel for an average SNR
value of of ρ. By comparing (22) with C(Nt, Nt, 1, p), it is
not clear whether the proposed scheme is information lossless
or information lossy for a Nt-MIMO-MAC ∀Nt. Through
simulations, in Fig. 16 (shown at the top of the next page),
the sum capacity of the proposed scheme is compared with
C(Nt, Nt, 1, p) for Nt = 2, Nt = 4 and Nt = 8 respectively
at different SNR values. Note that when Nt = 2 and 4,
the proposed scheme is information lossy by a small margin
and the difference in the capacity keeps diminishing as Nt
increases (See Fig. 16 for Nt = 8). In particular, using strong
law of large numbers, for large values of Nt, we have
lim
Nt→∞E

log2

1 + ρ
Nt
hhH

= C(Nt, Nt, 1, p).
and hence the proposed designs are information lossless for
large values of Nt. The above discussion can be summarized
in the following theorem,
Theorem 6: For large values of Nt, STBC pairs from rate-1
RODs are information lossless for a Nt-MIMO-MAC.
2) Minimum decoding complexity: Apart from having the
information lossless property for large values of Nt, the
proposed codes also have the single-symbol ML decodable
0
5
10
15
20
25
30
35
10
−6
10
−5
10
−4
10
−3
10
−2
10
−1
10
0
SNR in db
BER
2 X 2 SOD
2 X 2 ROD
4 X 4 ROD
4 X 4 SOD
Fig. 17.
BER comparison of STBC pairs from RODs and SODs
property. From (20) and (21), the ML-decoding metrics for
User-1 and User-2 are respectively given by
ˆX = arg min
C1 ||y −
r α
2Nt
X˜h1||2,
ˆY = arg min
C2 ||y −
r α
2Nt
Y˜h2||2.
Since ˜hj are real vectors, and the designs, X and Y are RODs,
for each user, every symbol can be decoded independent of the
rest of the symbols. For more details on decoding the class of
STBCs from RODs, we refer the reader to [14], [15]. To the
best of our knowledge, this is the ﬁrst paper that addresses the
design of STBC pairs with single symbol decodable property
for two-user MIMO-MAC.
D. Simulation Results
In this subsection, we provide simulation results for the
performance comparison of STBC pairs from SODs and RODs
for a Nt-MIMO-MAC when Nt = 2 and 4. We have used the
Bit Error Rate (BER) which corresponds to errors in decoding
the bits of both the users as error events of interest. For Nt = 2
and 4, the rate-1 SOD pairs have been used for simulations.
For both the cases the variables of the two users take values
from a 4-QAM signal set (with average energy per symbol
being unity). With this, each user transmits 2 bits per channel
use (bpcu). For the second class of STBC pairs, RODs for 2
and 4 antennas are used wherein the variables of the design
employed by User-1 take values from the 4-PAM signal set,
p
( 1
5) {−3, −1, 1, 3} whereas for User-2, the variables take
values from the set
p
( 1
5) {−3i, −1i, 1i, 3i}. With this, the
transmission rate of 2 bpcu-per user is maintained for both
the class of codes. For every codeword use, the destination
has to decode for 8 bits (4 bits of each user) and 16 bits
(8 bits for each user) for Nt = 2 and Nt = 4 respectively.
BER comparison of the two schemes using the above designs
is shown in Fig. 17 where the plots show that STBC pairs
from RODs perform better than the codes from SODs for both
Nt = 2 and 4. An intuitive reasoning for the above behaviour
is that for the class of STBC pairs from RODs, there is no
interference among the users. For the STBC pairs based on


## Page 16


16
−10
−5
0
5
10
15
20
0
1
2
3
4
5
6
7
SNR in db
Sum Capacity
Capacity of SISO fading channel
Capacity of 2 X 1 channel
Capacity of 4 X 1 channel
Capacity of 8 X 1 channel
Capacity of 16 X 1 channel
Loss in the sum capacity for using ROD in (2,2,1)
MIMO−MAC
Loss in the sum capacity for using ROD in (4,4,1)
MIMO−MAC
Loss in the sum capacity for using ROD in (8,8,1)
MIMO−MAC
Fig. 16.
Sum capacity of Nt-MIMO-MAC with RODs in comparison with C(Nt, Nt, 1) for Nt = 2, 4 and 8.
RODs, each real symbol is decoded in R whereas for the codes
from SODs, decoding is in R4 for Nt = 2 and R8 for Nt = 4.
V. DISCUSSION
We have computed CC capacity regions of a two-user
GMAC and proposed TCM schemes with the class of M-
PSK signal sets and M-PAM signal sets. We have studied
designing STBC pairs with low ML decoding complexity for a
two-user MIMO-MAC with Nt antennas at both the users and
single antenna at the destination with the assumption of CSIT-
P. Some possible directions for future work are as follows:
• As a generalisation to this work, CC capacity/capacity
regions for general multi terminal networks needs to be
computed since in practice, communication takes place
only with ﬁnite input alphabets. Also, design of coding
schemes achieving rate tuples close to the CC capacity
of general multi terminal networks is essential.
• The set partitioning result presented in this paper can be
generalized to the class of M-QAM alphabets.
• In this paper, we have assumed equal average power
constraint for both the users. It is clear that if unequal
power constraint is considered, then the UD property is
naturally attained. For such a setup, optimal labelling
rules on the individual trellis has to be proved depending
on the ratio of the average power constraints of the two
users. It is straightforward to show that when the ratio
of the average power constraints of the two users is
sufﬁciently large, then irrespective of the relative angle of
rotation between the alphabets, labelling of the individual
trellises based on Ungerboeck partitioning is optimal in
the sense of maximizing the criteria considered in this
paper.
• For a two-user GMAC, it has been shown that trellis
code pairs based on TCM with M-PAM alphabet pairs
signiﬁcantly reduce the ML decoding complexity at the
destination compared to TCM schemes with complex al-
phabet pairs. For a K-user GMAC with K > 2, designing
coding schemes with low ML decoding complexity is an
interesting direction of future-work.
• In Section IV, we considered designing STBC pairs with
low ML decoding complexity for a two-user MIMO-
MAC with Nt antennas at both the users and single
antenna at the destination with the assumption of CSIT-P.
Note that the assumption of CSIT-P has been exploited
to obtain STBC pairs with low ML decoding complexity
property. However, when the destination has multiple
antennas, every transmit antenna of each user views more


## Page 17


17
than one fading channel and hence phase compensation
by the users is not possible. Therefore, design of low
decoding complexity STBC pairs for such a set-up is not
straightforward. In particular, design of low complexity
STBC pairs for a MIMO-MAC without the assumption
of CSIT-P is challenging.
ACKNOWLEDGMENT
This work was partly supported by the DRDO-IISc Program
on Advanced Research in Mathematical Engineering.
REFERENCES
[1] Thomas M Cover and J. A. Thomas, ”Elements of information theory”,
second edition - Wiley Series in Telecommunications, 2004.
[2] Gallager R, ”A perspective on multiaccess channels” IEEE Trans. Inform.
Theory, vol. 31, no 2, March 1985, pp. 124-142.
[3] Ezio Bigleiri, Laszlo Gyorﬁ, ”Multiple Access Channels : Theory and
Practice” IOS press, published in cooperation with NATO public Diplo-
macy Division. 2007.
[4] R. Ahlswede, ”Multi-way Communication channels”, in the proceedings
of ISIT-1971, Armenian, S.S.R, 1971, pages 23-52
[5] H. Liao, ”A coding theorem for multiple access communications” in the
proceedings of ISIT-1972, Asilomar, CA, 1972.
[6] F. N. Brannstrom, T. M. Aulin and L. K. Rasmussen, ”Constellation-
Constrained capacity for Trellis code Multiple Access Systems” in the
proceedings of IEEE GLOBECOM 2001, vol. 2, San Antonio, Texas,
Nov, 2001, pp. 11-15.
[7] T. Aulin and R. Espineira, ”Trellis coded multiple access (TCMA)” in the
proceedings of ICC ’99, Vancouver, BC, Canada, June 1999, pp. 1177-
1181.
[8] Fredrik N Brannstrom, Tor M. Aulin and Lars K. Rasmussen ”Iterative
Multi-User Detection of Trellis Code Multiple Access using a posteriori
probabilities” in the proceedings of IEEE ICC 2001, Finland, June 2001,
pp. 11-15.
[9] Wei Zhang, C. D’Amours and A. Yongacoglu, ”Trellis Coded Modulation
Design form Multi-User Systems on AWGN Channels” in the proceedings
of IEEE Vehicular Technology Conference 2004, pp. 1722 - 1726.
[10] G. Ungerbeck, ”Channel coding with multilevel/phase signals,” IEEE
Trans. Inform. Theory, vol. 28, no. 01, 1982, pp. 55-67.
[11] Ezio Biglieri, ”Coding for wireless channels”, Springer-Verlag New
York, Inc, 2005.
[12] M.E. Gartner and H. Bolcskei, ”Multiuser space-time/frequency code
design”, in the proceedings of IEEE ISIT 2006, pp.2819-2823.
[13] M. Badr, J. C. Belﬁore, ”Distributed Space-Time Block Codes for the
MIMO Multiple Access Channel”, in the proceedings of IEEE ISIT 2008.
pp. 2553-2557. Online on arXiv:0804.1490v1 [cs.IT].
[14] V. Tarokh, H. Jafarkhani and A. R. Calderbank, ”Space time block codes
from orthogonal designs” IEEE Transactions on Information theory,
vol.45, no.05, 1999, pp.1456-1467.
[15] X Liang, ”Orthogonal designs with maximal rates”, IEEE Transactions
on Information theory, vol.49, no.10, 2003, pp. 2468-2503.
[16] Z. Khan and B. S. Rajan, ”Single symbol maximum likelihood decodable
linear STBCs”, IEEE Transactions on Information theory, vol.52, no.05,
2006, pp. 2062-2091.
[17] Karmakar, S. and B. S. Rajan, ”Minimum decoding complexity, max-
imum rate space time block codes from Clifford algebras”, IEEE ISIT
2006, pp. 788-792.
[18] Zhihang Yi and Il-Min Kim ”Single symbol ML decodable distributed
STBCs for cooperative networks”, IEEE Transactions on Information
theory, vol.53, no.8, 2007, pp. 2977-2985.
[19] J. Harshan and B. S. Rajan, ”Single-Symbol ML Decodable Precoded
DSTBCs for Cooperative Networks”, IEEE ICC 2008, pp. 991-995.
[20] Karmakar, S. and B. S. Rajan, ”Multigroup-Decodable STBCs from
Clifford Algebras,” IEEE Transactions on Information Theory, Vol. 55,
No. 01, Jan. 2009, pp. 223-231.
[21] V. Shashidhar, B. Sundar Rajan and B. A. Sethuraman, ”Information-
Lossless Space-Time Block Codes from Crossed-Product Algebras,” IEEE
Transactions on Information theory, Vol.52, No.9, Sept., 2006, pp.3913-
3935.
[22] B. Hassibi and B.M. Hochwald, ”High-rate codes that are linear in space
and time”, IEEE Transactions on Information theory, vol.48, no.7, Jul.
2002, pages 1804-24.
[23] J. Harshan and B. Sundar Rajan, ”Finite Signal-set Capacity of Two-
user Gaussian Multiple Access Channel” in the proceedings of IEEE
International Symposium on Information Theory, (ISIT 2008), Toronto,
Canada, July 06-11, 2008. pp. 1203 - 1207.
APPENDIX I
PROOF OF PROPOSITION 6
For a, b ∈C, let l(a, b) denote the line segment join-
ing a and b in R2. It is to be noted that the complex
points 0, r(Iq−1) and r(Iq−1)ei 2π
M form the three vertices’s
of an isosceles triangle in R2. Since r(Oq) ≤r(Iq−1),
we have d(0, r(Oq)ei 2π
M ) ≤d(0, r(Iq−1)ei 2π
M ). Therefore,
the four points r(Oq), r(Oq)ei 2π
M , r(Iq−1) and r(Iq−1)ei 2π
M
form the vertices’s of an isosceles trapezoid Υ such that
l(r(Oq), r(Oq)ei 2π
M ) is parallel to l(r(Iq−1), r(Iq−1)ei 2π
M ).
Also, note that d(r(Iq−1), r(Oq)ei 2π
M ) is the length of the
diagonal of the trapezoid Υ. Since the angle between the
line segments l(r(Oq), r(Oq)ei 2π
M ) and l(r(Oq), r(Iq−1)) is
obtuse, d(r(Iq−1), r(Oq)ei 2π
M ) ≥d(r(Oq−1), r(Oq−1)ei 2π
M ).
This completes the proof.
APPENDIX II
PROOF OF PROPOSITION 7
We
prove
the
inequality
2r(OM/2−1)sin( 2π
M )
≤
d(r(Oq), r(Oq)ei 2π
M ) which can be written the following ratio
:
2r(OM/2−1)sin( 2π
M )
d(r(Oq), r(Oq)ei 2π
M )
= sin( π
M −θ
2)sin( 2π
M )
cos( θ
2 + πq
M )sin( π
M ).
(23)
Since θ ≤
pi
M and q ≤M/2 −3, θ
2 + πq
M ≤pi
2 −5π
M < π
2 .
Hence for all values of θ and q, cos( θ
2 + πq
M ) ≥cos( pi
2 −5π
M ) =
sin( 5π
M ). Also, sin( π
N −θ
2) ≤sin( π
N ). Therefore, the ratio in
(23) satisﬁes the following inequality for M ≥8,
sin( π
M −θ
2)sin( 2π
M )
cos( θ
2 + πq
M )sin( π
M ) ≤sin( 2π
M )
sin( 5π
2M ) ≤1.
This completes the proof.
APPENDIX III
PROOF OF LEMMA 1
Since the structure of Seo
sum and Soe
sum are identical, we
ﬁnd the minimum distance of Seo
sum. Since the points of
Seo
sum are maximally separated on every circle and OM/2−1
is the innermost circle, d(r(OM/2−1), r(OM/2−1)ei 4π
M ) =
2r(OM/2−1)sin( 2π
M ) = d1 is a contender for deo
min. For this
to be true, it is to be shown that all other intra-distances
in the set are larger than or equal to d1. In particular, the
distances between the points on any two consecutive circles
must be larger than d1. Firstly, it is shown that a point on
Iq and a point on Oq−1 which have an angular separation of
0 radians are separated by a distance larger than d1 for all
q = 2 to M/2 −2. In that direction, the ﬁrst observation is
that r(O1) −r(I2) = d1. From the results of the Proposition
3, r(Ok) −r(Ik+1) ≥d1 for all k ≥2. Hence the points on
Iq and Oq−1 are separated by a distance larger than d1 for all
q = 2 to M/2 −2.
Secondly, it is to be veriﬁed if the point on Oq and the point
on Iq−1 are separated by a distance larger than d1 for all q = 1


## Page 18


18
to M/2−1. It is shown that the points on Oq and Iq−1 having
an angular separation of 2π
M are separated by a distance larger
than d1 only for q = 1 to M/2 −3 but not for q = M/2 −1.
For q = M/2 −1, d(r(Iq−1), r(Oq)ei 2π
M ) can be lesser than
2r(OM/2−1)sin( 2π
M ) for certain values of θ. Therefore, we
prove d(r(Iq−1), r(Oq)ei 2π
M ) ≥2r(OM/2−1)sin( 2π
M ) only for
q = 1 to M/2−3 using the following sequence of inequalities,
d(r(Iq−1), r(Oq)ei 2π
M ) ≥d(r(Oq), r(Oq)ei 2π
M ) ≥2r(OM/2−1)sin(2π
M ).
The ﬁrst inequality is proved in Proposition 6 whereas
the second inequality is proved in Proposition 7. Hence, the
points on Oq and Iq−1 are separated by a distance larger
than d1 for all q = 1 to M/2 −3. Therefore, deo
min =
min

d(r(Iq−1), r(Oq)ei 2π
M ), d1

. This completes the proof.
APPENDIX IV
PROOF OF LEMMA 2
Since the structure of See
sum and Soo
sum are the same,
we ﬁnd the minimum distance of See
sum only. Since the
points of See
sum are maximally separated with φmin
=
4π
M
on every circle and IM/2−1 is the innermost circle,
d(r(IM/2−1), r(IM/2−1)ei 4π
M ) = 2r(IM/2−1)sin( 2π
M ) = d2
is a contender dee
min. For this to be true, it is to be shown
that the distances between the points on any two consecutive
circles must be larger than d2. We show that a point on Oq
and a point on Iq−1 which have an angular separation of 0
radians are separated by a distance larger than d2 for all q = 2
to M/2 −2. In that direction, the ﬁrst observation is that
r(I1) −r(O2) = d2. From the result of the Proposition 4 in
Section I, r(Ik) −r(Ok+1) ≥d2 for all k ≥2. Hence the
points on Oq and Iq−1 are separated by a distance larger than
d2 for all q = 2 to M/2 −2 .
Secondly, it is shown that the point on Iq and the point on
Oq−1 are separated by a distance larger than d2 for all q = 1
to M/2 −1. i.e. we prove d(r(Oq−1), r(Iq)ei 2π
M ) ≥d2 for
q = 1 to M/2 −1. In that direction, for q = 1 to M/2 −3,
we show that
d(r(Oq−1), r(Iq)ei 2π
M ) ≥d(r(Iq), r(Iq)ei 2π
M ) ≥2r(IM/2−1)sin(2π
M ).
(24)
For the case when q = M/2 −1, we show that
d(r(Oq−1), r(Iq)ei 2π
M ) ≥d(r(Oq−1), r(Iq)) ≥2r(IM/2−1)sin(2π
M ).
(25)
The proof for the ﬁrst lower bounds of (24) and (25) are on
the similar lines of the proof for Proposition 6. The proofs of
the second lower bounds of (24) and (25) are in Proposition
8 and Proposition 9 respectively. Therefore, dee
min = d2 =
4sin
  θ
2)sin( 2π
M

. This completes the proof.
APPENDIX V
PROOF OF THEOREM 4
Let X represents the l × Nt ROD for Nt antennas in the
variables x1, x2 · · · xl. Note that the number of channel uses is
equal to the number of real variables since X is a rate-1 ROD.
Also, X has the following column vector representation,
X = [A1x A2x · · · ANtx]
where {Ai | i = 1 to Nt} is the set of column vector repre-
sentation matrices of X and xT = [x1 x2 · · · xl]. The MISO
channel equation with the above design is, y =
q
ρ
Nt Xh + n
where ρ is the average receive SNR and n ∼N (0, 1). The
above channel equation can also be written as
y =
r ρ
Nt
ˆHx + n
where ˆH = PNt
i=1 hiAi. If the channel from every antenna to
the destination is i.i.d Rayleigh distributed with unit mean, the
capacity of the above channel is
1
2E

log2

det

Il + ρ
Nt
ˆHˆH
H
.
Since Ai’s are unitary and AiAT
j + AjAT
i
= 0T ×T ∀i, j
such that i ̸= j, we have ˆHˆH
H =
PNt
i=1 h2
i

Il and hence
the capacity of a single-dimensional MISO channel with the
ROD, X is
1
2E
"
log2
 
1 + ρ
Nt
(
Nt
X
i=1
h2
i )
!#
.
This completes the proof.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]
