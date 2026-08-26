---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1704.04367v2
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1704.04367v2_Quantum_Biometrics_with_Retinal_Photon_Counting

> Source: 1704.04367v2_Quantum_Biometrics_with_Retinal_Photon_Counting.pdf

> Pages: 16

---


## Page 1


arXiv:1704.04367v2  [quant-ph]  26 Oct 2017
Quantum Biometrics with Retinal Photon Counting
M. Loulakis,1, ∗G. Blatsios,2 C. S. Vrettou,3 and I. K. Kominis4, ¶
1School of Applied Mathematical and Physical Sciences,
National Technical University of Athens, 15780 Athens, Greece
2Department of Ophthalmology, Medical University of Innsbruck, A-6020 Innsbruck, Austria
3First Department of Critical Care Medicine and Pulmonary Services,
National and Kapodistrian University of Athens Medical School, Evaggelismos General Hospital, Athens, Greece
4Department of Physics and Institute of Theoretical and Computational Physics, University of Crete, 71003 Heraklion, Greece
It is known that the eye’s scotopic photodetectors, rhodopsin molecules and their associated
phototransduction mechanism leading to light perception, are eﬃcient single photon counters. We
here use the photon counting principles of human rod vision to propose a secure quantum biometric
identiﬁcation based on the quantum-statistical properties of retinal photon detection. The photon
path along the human eye until its detection by rod cells is modeled as a ﬁlter having a speciﬁc
transmission coeﬃcient. Precisely determining its value from the photodetection statistics registered
by the conscious observer is a quantum parameter estimation problem that leads to a quantum secure
identiﬁcation method. The probabilities for false positive and false negative identiﬁcation of this
biometric technique can readily approach 10−10 and 10−4, respectively. The security of the biometric
method can be further quantiﬁed by the physics of quantum measurements. An impostor must be
able to perform quantum thermometry and quantum magnetometry with energy resolution better
than 10−9ℏ, in order to foil the device by non-invasively monitoring the biometric activity of a user.
I.
INTRODUCTION
In recent years there is an increasing need for secure
biometric identiﬁcation. Besides the traditional ﬁnger-
printing, the most advanced methods currently appear
to be the retina and iris scan.
For example, the dis-
tinctiveness of the acquired retinal image is due to the
subject-speciﬁc formation of blood vessels on the retina’s
surface. However, all existing methods [1] are ”classical”,
meaning that in principle they can be foiled, or equiva-
lently, (i) there is no law of physics prohibiting such a foil,
and (ii) their security is neither guaranteed nor quanti-
ﬁed by any fundamental law of physics, but relies on the
hope that the majority of potential impostors lack the
means to foil them.
We here propose and analyze a biometric method
based on the ”single-photon” detection ability of the hu-
man retina. The method relies on the quantum estima-
tion of α, a parameter describing the optical/detection
losses along particular optical paths ending on the retina.
The estimation follows from knowledge of the incident
number of photons and from the subject’s response re-
garding the perception or not of a series of light ﬂashes.
The proposed method can be termed ”quantum” for
three reasons. First, it is based on detecting coherent
light pulses containing a few tens of photons by the con-
scious subject supposed to be positively identiﬁed (call
her Alice), (ii) an impostor pretending to be Alice, call
her Eve, is forced by the physics and methodology of
this biometric technique to reply randomly to the bio-
metric device’s interrogations, no matter how technolog-
ically advanced she is, in particular, no matter how good
∗loulakis@math.ntua.gr
¶ ikominis@physics.uoc.gr
photon detectors she is equipped with, and (iii) in the
event that Eve is attempting by physical means to non-
invasively infer Alice’s particular biometric characteris-
tics while Alice is being interrogated by the biometric
device, the ability to do so can be quantiﬁed in the con-
text of energy resolution of quantum measurements.
In Sec. II we introduce the basic photon statistics of
low-intensity light perception by the retina and deﬁne
the parameter α that is to be estimated and used as
the biometric quantiﬁer. In Sec. III we introduce two
central performance metrics, the false-positive and false-
negative identiﬁcation probabilities, as well as some ba-
sic features of the biometric methodology. In Sec. IV we
brieﬂy comment on a naive biometric strategy, the quan-
tum estimation of the α-map across the retina, which re-
quires an impractically long interrogation time. In Sec.
V we introduce the central idea of the method, the ran-
dom illumination of either low-α or high-α spots, which
is further reﬁned by considering a Bayesian update of
the identiﬁcation probability conditioned on the running
record of responses. This approach leads to a realisti-
cally short interrogation time, which is further reduced
by introducing in Sec. VI a ”parallel” method based on
pattern recognition. With conservative assumptions we
obtain unprecedented performance metrics, in particular
a false positive and false negative probability at the level
of 10−10 and 10−4, respectively. In principle, both met-
rics can be readily reduced even further. Finally, in Sec.
VII we examine whether the proposed method can be
indeed termed ”quantum”. We then analyze the phys-
ical means by which an impostor could non-invasively
monitor the biometric activity of Alice, infer her biomet-
ric characteristics and then pass the test. The quantum
technology the impostor must possess in order to do so
amounts to performing quantum thermometry and mag-
netometry with an energy resolution better than 10−9ℏ.


## Page 2


2
II.
QUANTUM PARAMETER ESTIMATION OF
THE EYE’S ”TRANSMISSIVITY”
Quantum information science has turned the counter-
intuitive traits of quantum physics into potentially use-
ful technology, with examples like quantum communi-
cations [2–4] and cryptography [5–7] already leading to
commercial applications [8]. In the case of quantum cryp-
tography, security is guaranteed by the laws of quan-
tum physics. Coherent sources with few photons [9, 10]
and non-ideal photodetectors feature prominently in such
protocols.
Part of the recent quest to explore the possibilities bi-
ological systems oﬀer for novel quantum technology re-
alizations [11–13] has been the question of how well bio-
logical photodetectors, in particular rhodopsin molecules
in retinal rod cells [14], compare with modern photode-
tectors [15]. Historically, the role of photon statistics in
vision was addressed in the 1930’s [16] and elucidated
with human behavioral experiments in the 1940’s [17–
19], single cell responses have been recorded since the
1970’s [20–24], while it was only recently that the quan-
tum physics of human vision [25] was addressed with
the modern experimental [26–30] and theoretical [31–34]
tools of quantum optics.
It is now established that ﬂuctuations in the percep-
tion of light by a small number of rods are governed by
photon statistics. Indeed, the probability to see a ﬂash
of light of incident intensity I, illuminating a small area
of the retina (about 0.1 mm2) for a time τ is given by the
probability to count a number of photons, n, larger than
the visual system’s perception threshold, K. This proba-
bility, call it P[see], is a function of ˜I, where ˜I = Iτ is the
average incident photon number. The actual number of
detected photons, n, follows [35] a Poisson distribution
having average n = αIτ. As succinctly noted in [35], the
parameter α ”includes all messy details of what happens
to light on its way through the eyeball”. In particular,
the parameter α includes (a) the optical losses along the
beam’s path to the retina, i.e. the cornea, anterior cham-
ber, pupil, lens and vitreous body, as well as (b) the ab-
sorption probability of the particular spot of the retina
being illuminated, determined by the local surface den-
sity of rod cells and their quantum eﬃciency. Typical
values of α range from zero up to 0.2 [36–38]. Although
each human subject had a diﬀerent α, the data of the
early experiment [17], asking several individuals to re-
spond positively or negatively on the perception of weak
light ﬂashes, could be ﬁt by P[see] =
∞
P
n=K
p(n; α˜I), where
p(n; n) = e−nnn/n!, using a common threshold K. The
universal quantum noise properties of visual perception
were thus revealed.
We here turn the previous arguments around and view
P[see] from the perspective of quantum parameter esti-
mation [39–41], aiming to measure the unknown, and
subject-dependent parameter α. In other words, while
previous studies aimed at establishing single-photon de-
SPC
Filter with power 
transmission coefficient α
0
50
100
150
200
I 
~
0.0
0.2
0.4
0.6
0.8
1.0
P[see]
α=0.05
α=0.10
α=0.20
(a)
(b)
Detection Threshold K=6
~I photons 
per pulse
FIG. 1. (a) Equivalence of the proposed biometric measure-
ment with an optical setup consisting of a ﬁlter, the trans-
mission coeﬃcient, α, of which is to be estimated, followed
by an ideal (unit quantum eﬃciency) single photon counter
(SPC), having a threshold equal to the brain’s light perception
threshold of at least K = 6 photons illuminating a ganglion
receptive ﬁeld. The output of the SPC is then registered by
the conscious observer. The transmissivity of the ﬁlter cap-
tures the photon losses along the particular beam path ending
on a particular retinal spot, including the detection eﬃciency
of the illuminated rods. (b) Probability to see the ﬂash of
coherent light having average photon number ˜I for three in-
dicative values of the parameter α.
tection capability and threshold, treating the subject
variation of α as an unwanted nuisance, we take the for-
mer for granted and aim to measure α.
As shown in Fig.
1a, we model the particular light
beam path through the eye including its detection by the
rod cells as a ﬁlter, the power transmission coeﬃcient
of which, α, we wish to estimate. The ﬁlter is followed
by a single-photon counter, the output of which is regis-
tered by the conscious human brain. To estimate α we
use (i) a coherent laser beam of known average photon
number per pulse, and (ii) a conscious observer with a
given light perception threshold. In other words, know-
ing the incident photon number and the see/don’t see
responses of the tested subject, we estimate P[see], and


## Page 3


3
from the dependence of P[see] on α we infer α. Examples
of this dependence are shown in Fig. 1b. Interestingly,
the results of the quantum measurements leading to the
estimation of α are registered by Alice’s brain, oﬀering a
ﬁrst layer of security practically diﬃcult to bypass.
The proposed biometric identiﬁcation method rests on
two facts [42]. Firstly, the values of α vary signiﬁcantly
across the retinal surface of an individual, at the level of
40 dB, and (ii) for a geometrically similar spot on the
retina they vary signiﬁcantly between individuals, at the
level of at least 3 dB. Hence a precisely measured map of
α values can uniquely distinguish human subjects.
III.
BIOMETRIC PERFORMANCE METRICS
AND METHODOLOGY
We here introduce two central metrics for the perfor-
mance of the biometric method, the false-positive and
false-negative probabilities, pfp and pfn, respectively. The
former refers to the probability that an impostor, Eve,
presents herself as Alice and successfully passes the test.
The latter is the probability that Alice fails the test. The
required speciﬁcations for pfp and pfn will determine the
interrogation time.
Before proceeding with the analysis of the various iden-
tiﬁcation strategies, we make a few introductory remarks.
Consider a single spot on the retina being illuminated
with a coherent pulse of light having average photon
number ˜I when incident on the eyeball. The probabil-
ity to see the ﬂash depends on the eye’s ”transmissivity”
α corresponding to the particular light-path ending on
this particular spot. In order (i) to be able to serve mul-
tiple users, and (ii) to suppress the probability that Eve
foils the device, the test will rely on a whole map of reti-
nal spots, each with its own α value. We call this the
α-map.
All strategies to be presented have a common feature:
for the user to be positively identiﬁed, Alice, the device
has once measured and stored the user’s α-map.
The
methodology for this measurement is the following. Con-
sidering a given retinal spot with a given α parameter,
the probability to see the ﬂash of coherent light hav-
ing ˜I photons on average is P[see] =
∞
P
n=K
p(n; α˜I). The
sum can be evaluated in terms of the incomplete Gamma
function
GK(x) =
x
Z
0
dt tK−1e−t
(K −1)!,
(1)
and is equal to GK(α˜I) (see Appendix A). Repeating the
measurement for several values of ˜I, we can use GK(x) to
estimate α for that particular retinal spot. The same pro-
cedure is used for all other spots constituting the user’s
α-map, which can thus be measured and stored. Obvi-
ously, the users’ α-map should not be public or accessible
information. This is a common requirement of all current
biometric modalities, e.g. if the database containing ﬁn-
gerprints or retinal images is compromised, the particular
identiﬁcation method is prone to failure. We further com-
ment on this point in the closing remarks of Sec. VIII.
When Alice presents herself and asks to be identiﬁed,
the device uses the information on Alice’s α-map and
some identiﬁcation strategy to make an inference. We
next present several identiﬁcation strategies in order of
decreasing interrogation time, which besides the afore-
mentioned performance metrics, is also a central param-
eter relevant to the practicality of the method.
IV.
BIOMETRIC STRATEGY I: ESTIMATION
OF α-MAP
For this strategy, when the user Alice registers herself
at the device for the ﬁrst time, the value of α is mea-
sured and stored for each retinal spot as described before.
Then, when Alice presents herself and asks to be iden-
tiﬁed, the value of α is estimated again using the same
procedure and the result is compared with the stored val-
ues.
The test of a single spot is considered ”passed” if the
estimated α of the subject presenting herself as Alice is
within a given range of Alice’s stored α. The estimate
follows after a number ν of see/don’t see interrogations
illuminating the particular spot.
Then, the subject is
positively identiﬁed as Alice if she ”passes” the test for
at least µ diﬀerent retinal spots. Thus, the total num-
ber of see/don’t see interrogations is νµ. As we prove
in Appendix B, in order to achieve performance metrics
pfn < 10−4 and pfp < 10−10, the total number of re-
quired interrogations would be νµ ≈2500. That is, not
only in the registration process, but also every time Alice
wishes to be identiﬁed, such a large number of interro-
gations would be necessary, leading to a time consuming
and impractical test.
V.
BIOMETRIC STRATEGY II: SERIAL
ILLUMINATION OF HIGH-α AND LOW-α SPOTS
A much better strategy is to rely on Alice’s retinal
spots with markedly high or low α values. If the device
were to interrogate only low-α spots or only high-α spots,
Eve would eventually learn this interrogation strategy
and tune her responses appropriately.
Thus, the ﬁrst
central idea of this strategy is that in each interrogation
the biometric device will randomly (e.g. using a quantum
random number generator [43, 44]) choose to illuminate
a low-α or a high-α spot. Eve is unaware of what type of
spot is illuminated. The second central idea is that for
both low-α and high-α spots, the laser pulses will contain
on average the same number of photons.
Hence, even
if Eve is equipped with an ideal photodetector, she can
not extract any useful information from measuring the
photon number in each interrogation pulse. Not knowing


## Page 4


4
what type of retinal spot is being illuminated in each
interrogation pulse, Eve is forced to respond randomly
on perceiving or not the light ﬂash. Moreover, no matter
how many times Eve takes the test, she is always facing
the same average number of photons per pulse, and hence
she is always forced to respond randomly, i.e. there is no
information to be acquired by Eve with time. These ideas
underlie all three identiﬁcation strategies to be presented
next.
Low-α and high-α spots are deﬁned by αmin ≤α ≤
αL and αH ≤α ≤αmax, respectively.
As mentioned
in Sec.
II, it typically is αmax ≈0.2 [36–38], while α
varies by at least 40 dB across the retina. As will be
detailed in the following, the smaller amin the better for
the proposed identiﬁcation strategy. To be conservative
and thus underestimate the performance of the strategy,
we will consider throughout this work a 20 dB span of α,
and thus take αmin = 0.02 and αmax = 0.2.
For the following strategies, we assume that Alice’s
α-map has been measured and stored as classical infor-
mation. There are several statistical approaches to this
ﬁrst measurement (e.g. absolute estimate versus classi-
ﬁcation into low-α or high-α), which will be explored in
detail elsewhere. Now, when Alice presents herself and
asks to be identiﬁed, the biometric device can resort to
the following identiﬁcation protocols.
A.
Collective analysis of responses
For a ﬂash of coherent light having ˜I photons on av-
erage, the probabilities that Alice sees the ﬂash in the
low-α illumination and does not see the ﬂash in the
high-α illumination are bounded above by GK(αL ˜I) and
1 −GK(αH ˜I), respectively. The average photon number
per pulse, ˜I, is chosen so that
GK(αL ˜I) = 1 −GK(αH ˜I) =: q.
(2)
This gives
αH
αL
= G−1
K (1 −q)
G−1
K (q)
.
For example, choosing αH/αL = 3 and setting K = 6,
the preceding equation can be solved numerically and
determines the value of q ≃0.1. We can go back to (2)
to determine ˜I, according to Alice’s αL and αH values.
For instance, if αL = 0.05, then ˜I ≃62.
The parameter q represents the probability that Alice
responds wrongly, i.e. she perceives the light pulse if a
low-α spot is being interrogated, or she does not see the
light pulse if a high-α spot is interrogated. The smallness
of q reﬂects the advantage Alice has over Eve, who neces-
sarily responds randomly. To reduce q we can reduce αL
and/or increase αH. On a practical level, this should not
be done in a way that reveals to Eve what kind of spot
is illuminated. That is, on average α is reduced in the
periphery of the retina compared to the center. But one
should not take advantage of this reduction to suppress
the choice of αL, because the spatial distribution of the
illuminated spots would reveal their character. Instead,
one should locate neighboring spots with the highest ra-
tio αH/αL.
We now consider a series of N such interrogations. For
i = 1, 2, . . . , N we deﬁne the Bernoulli random variable
Xi. If in the i-th interrogation we illuminated a low-α
(high-α) spot, then Xi = 0 (Xi = 1) if the tested subject
did not, and Xi = 1 (Xi = 0) if the tested subject did
see the ﬂash. That is,
N
P
i=1
Xi counts the wrong responses.
The tested subject is identiﬁed as Alice, if
N
P
i=1
Xi < Nw
for some w ∈(q, 1
2) that will be determined later.
We use the same average photon number in all pulses,
hence when Alice is tested, we have PA

Xi = 1

≤q, for
all i = 1, 2, . . ., N. By Lemma 4.7.2 in [45], the probabil-
ity that Alice fails the test is
pfn = PA
" N
X
i=1
Xi ≥Nw
#
≤e−NH(w|q),
(3)
where H(x|y) = xlog( x
y ) + (1 −x)log( 1−x
1−y) is the relative
Shannon entropy.
On the other hand, the probability that Eve guesses
wrong is PE

Xi = 1

= 1
2, for i = 1, 2, . . ., N. Hence, the
probability that Eve passes the test is
pfp = PE
" N
X
i=1
Xi < Nw
#
≤e−NH(w| 1
2).
(4)
Now, since w ∈(q, 1
2), it follows that H
 w
 q) appearing
in (3) is an increasing function of w, whereas H
 w
 1
2)
appearing in (4) is a decreasing function of w. Hence the
respective bounds for N obtained from (3) and (4) have
the opposite w-dependence, and to minimize N we set
log
  1
pfn
)H
 w
 1
2

= log
  1
pfp
)H
 w
 q

,
solving which we obtain w. Inserting this into either (3)
or (4) we then obtain N. For instance, requiring pfn =
10−4 and pfp = 10−10, we get w ≃0.22 and N = 138
interrogations, which is an order of magnitude lower than
the ”naive” strategy of the previous section.
B.
Real-time Bayesian update of identiﬁcation
probability
We will now demonstrate that we can signiﬁcantly
speed up the process, by more than a factor of 2, ter-
minating the test when the conditional probability that
the tested subject is Alice, given her running record of
answers, reaches a satisfactory level.


## Page 5


5
In particular, let P[A] ∈(0, 1) be the a priori prob-
ability that the tested subject is Alice and for i ∈N
denote by P

A | Fi

the conditional probability that the
tested subject is Alice, given her answers to the ﬁrst i
interrogations.
We also deﬁne Si = 1 (0), if the re-
sponse of the tested subject to the i-th interrogation
is see (no see). Based on Bayes’s rule, we can update
the conditional probabilities P

A | Fi

. For instance, if
i = 1 and v ∈{0, 1}, then the conditional probability
P

A
α1 = α, S1 = v

is equal to
P

S1 = v
A, α1 = α

P[A]
P
X=A,E
P

S1 = v
X, α1 = α

P[X].
(5)
Here P[E] = 1 −P[A] is the a priori probability that the
tested subject presenting herself as Alice is not Alice, and
P

S1 = v
X, α1 = α

is the conditional probability that
the response is v, given the subject is X (where X=A,E)
and the tested spot has α1 = α.
For iterating the calculation it is helpful to deﬁne
ZA(α, v) = P

S1 = v
A, α1 = α

. We can write
ZA(α, v) =
(
GK(α˜I),
for v = 1
1 −GK(α˜I),
for v = 0.
To calculate (5), we need to set P

S1 = v
E, α1 = α

.
The choice of this parameter is made by the test de-
signer and reﬂects the designer’s belief to get the answer
S1 = v, given that the subject who claims to be Alice
is not. Intuitively, we could set this to 1/2, given that
Eve can not guess what type of spot (low-α or high-α)
the device illuminates. Another reasonable choice is to
set this parameter equal to p = Eα

GK(α˜I)

. After all,
this is the best guess one can make for the probability
that Alice sees a ﬂash without any information on the
value of α. It is readily shown (see Appendix C) that
p ∈( 1−q
2 , 1+q
2 ).
With this choice we can get analytically tractable and
nearly optimal bounds for the identiﬁcation thresholds
and interrogation time, regardless of the answering strat-
egy a potential impostor may follow. At the end, the
judicious choice of p is reﬂected in the success and opti-
mality of the identiﬁcation algorithm. To proceed, deﬁne
ZE(p, v) =
(
p
for v = 1
1 −p,
for v = 0.
(6)
From Bayes’s rule for i = 1 we ﬁnd
P

A
F1

=
ZA(α1, S1)P[A]
ZA(α1, S1)P[A] + ZE(p, S1)P[E].
Iterating this argument, it follows for any non-negative
integer i that
P

A
Fi

=
ZA(αi, Si)P

A
Fi−1

ZA(αi, Si)P

A
Fi−1

+ ZE(p, Si)P

E
Fi−1
.
If we deﬁne the odds ratio after i interrogations
Ri =
P

A
Fi

1 −P

A
Fi
 = P

A
Fi

P

E
Fi
,
the
updating
rule
takes
the
simple
form
Ri
=
ZA(αi, Si)Ri−1/ZE(p, Si), hence
Rn = R0
n
Y
i=1
ZA(αi, Si)
ZE(p, Si) .
1.
Identiﬁcation Thresholds
We may now set two thresholds x, y, with 0 < x < 1 <
y and stop the interrogation at the random time T ∈N as
soon as the ratio Rn/R0 falls outside the interval (x, y).
The tested subject is identiﬁed as Alice, if RT
R0 ≥y, and
is rejected, if RT
R0 ≤x. The thresholds x and y are set by
the desired speciﬁcations for pfp and pfn.
In Appendix D we prove that the process {R−1
n }n≥0 is
a martingale for Alice, and the process {Rn}n≥0 is a mar-
tingale for Eve, regardless of her answering strategy. A
stochastic process {Mn}n≥0 is a martingale when, given
the history up to any time n, its expected value at time
n+1 is the same as its value at time n, much like a gam-
bler’s fortune in a fair game. That is, the deﬁnition of a
martingale is
E

Mn+1
Fn

= Mn,
a consequence of which is that the martingale’s expecta-
tion is constant in time. Notably, this expectation does
not change even if we stop the martingale with a random
strategy such as the one discussed here. This is the op-
tional stopping theorem (cf. 10.10 in [46]), which we use
next to ﬁnd the expected values of RT and 1/RT for Eve
and Alice, denoted by EE

RT

and EA
 1
RT

, respectively.
For Eve we get
R0 = EE

RT

≥R0y PE
RT
R0
≥y

.
Hence, PE
 RT
R0 ≥y

≤
1
y, and it suﬃces to take y =
1
pfp to achieve the desired false positive probability. The
optional stopping theorem for Alice gives
1
R0
= EA
 1
RT

≥
1
xR0
PA
RT
R0
≤x

.
Hence, PA
 RT
R0 ≤x

≤x, and it suﬃces to take x = pfn
to achieve the desired false negative probability.


## Page 6


6
40
20
0
-20
-40
ln(Rn/R0)
0
20
40
60
80
≅
≅
E
E
T
T
[ ]
62
[ ]
19
A
E
1500
Counts
1000
500
0
100
Interrogation time T
≅
≅
E
E
T
T
[ ]
45
[ ]
10
A
E
0
20
40
60
80
100
Interrogation time T
(a)
(b)
(c)
(d)
Alice passes
Eve rejected
-ln(pfp)
ln(pfn)
FIG. 2. Random walks of ln(Rn/R0) (Alice blue and upwards, Eve red and downwards) and distribution of interrogation times
T . (a,b) Illumination of spots with (a) αL = 0.05 and αH = 0.15. For these values of αL and αH it is q = 0.096 and ˜I = 62.4.
(c,d) Illumination of spots with low-α and high-α uniformly distributed in [0.02,αL] and [αH,0.18], respectively. If ln(Rn/R0)
becomes higher (lower) than the upper (lower) threshold deﬁned by −ln(pfp) shown by the black solid line (ln(pfpn) shown by
the dashed black line) in (a,c), the interrogation stops and Alice is identiﬁed (Eve is rejected). The obtained mean values of T
shown in (b) and (d) are consistent with the bounds (9). In (a) and (c) we plot just 100 walks, the distributions (b) and (d)
were obtained from 5000 walks.
2.
Duration of Interrogation
We ﬁnally address the duration of the test for Alice
and Eve. Note ﬁrst that
ln
Rn
R0

=
n
X
i=1
ln
ZA(αi, Si)
ZE(p, Si)

.
(7)
The
test
ends
when
ln(Rn/R0)
exits
the
interval
(ln pfn, −ln pfp) and the test taker is identiﬁed as
Alice if
ln
 RT /R0

≥
−ln pfp,
or is rejected if
ln
 RT /R0

≤ln pfn.
Hence, we may view the test
as a random walk starting from 0, with increments
ln
 ZA(αi, Si)/ZE(p, Si)

. In Appendix C we establish
that Alice’s walk always has a drift to the right, while
Eve’s walk always has a drift to the left. As shown in
Appendix E, we can use (7) and the optional stopping
theorem to estimate the expected stopping times for Al-
ice and Eve. They read
EA

T

≤
ln
 2
(1−q)pfp

H
 q
 1
2)
(8)
EE

T

≤
2 ln
  2qminpfn
1+q

ln
 4q(1 −q)
,
(9)
where qmin = min{GK(αmin ˜I), 1 −GK(αmax ˜I)}. With
our choice of pfp = 10−10, pfn = 10−4, q = 0.1 and
αmin = 0.02 we obtain EA

T

≤65 and EE

T

≤28.
The above estimates on T are rigorous bounds and they
are sharp if we only target retinal spots with α = αL or
α = αH [52].
A Monte Carlo simulation for the random walk of
ln(Rn/R0) is shown in Fig.2. In Figs.2(a,b) we consider
the simple scenario of targeting spots with α = αL or
α = αH. Targeting spots with α < αL or α > αH im-
proves the running time of the algorithm. This is shown
in Figs.2(c,d), where we use a uniform distribution of α
in [0.02,0.05] for low-α, or in [0.15,0.18] for high-α.
It is seen that with a modest number of about 50 inter-
rogations (even fewer if we can increase αH and decrease


## Page 7


7
αL) we can identify Alice and meet the desired speciﬁ-
cations for pfp and pfn. This interrogation time is two
orders of magnitude smaller than the time needed to ab-
solutely estimate the α-map as discussed in Sec. IV
3.
Optimality of the Algorithm
For practical reasons, identifying Alice with the short-
est possible test duration is obviously of interest.
We
here evaluate the optimality of the previous identiﬁca-
tion algorithm, in particular the bound (8). To do so,
we ﬁnd the lower bound of interrogations N needed to
achieve a desired pfp in a series of questions having binary
answers, given the probability of an incorrect answer by
the subject supposed to pass the test.
This bound is
just dependent on binomial statistics and thus is general,
i.e. independent of any particular context and physical
realization of the questions.
If q is the probability of an incorrect answer by Alice,
the number of incorrect answers in N interrogations fol-
lows the binomial distribution, the median of which lies
in

[qN], [qN] + 1

, where [x] is the integer part of x.
By the deﬁnition of the median, the probability that at
least [qN] answers are incorrect is at least 1/2. To avoid
rejecting Alice as often as half of the times she is tested,
the tested subject has to be identiﬁed as Alice if she gives
at most [qN] incorrect answers.
Now suppose Eve answers randomly. N has to be large
enough so that the event Eq, that Eve gives at most [qN]
incorrect answers, has probability smaller than pfp. Eve’s
incorrect answers also follow a binomial distribution, so
Lemma 4.7.2 in [45] gives
pfp ≥P

Eq

≥
1
p
8NqN(1 −qN)
e−NH
 qN
 1
2

,
where qN = [qN]/N. Taking the approximation qN ≃q
this equation gives that
NH
 q
1
2

+ 1
2 ln
 8Nq(1 −q)

⪆ln 1
pfp
.
Comparing this lower bound for N with (8), we see that
the average number of interrogations required by the al-
gorithm we propose is close to the absolute lower bound.
For example, setting q = 0.1 and pfp = 10−10, we ﬁnd
N ≥57, to be compared with the upper bound of 65
found previously.
VI.
BIOMETRIC STRATEGY III: PATTERN
RECOGNITION
To even further reduce test time, we ﬁnally describe a
”parallel” interrogation scheme using a pattern recogni-
tion method. We will here not delve into discussing re-
ceptive ﬁelds and complex cognitive interactions among
them [53, 54], since we assume that we illuminate non-
overlapping ganglion receptive ﬁelds, which are roughly
[54] 0.2 mm wide, so we take a 2 cm×2 cm retinal surface
to approximately contain 10,000 pixels.
When Alice presents herself and asks to be identiﬁed,
the device picks among all possible retinal spots of Al-
ice a small subset with high α in such a way that they
form a particular pattern, e.g. the number ”2”. More-
over, the device picks another set of spots having low
α, and illuminates both the former and the latter with
the same average photon number. In Fig.3 we describe
how this method works. We ﬁrst generate a 100 × 100
matrix of retinal spots with α randomly picked for each
spot from the interval between αmin and αmax.
This
α-matrix is shown in Fig.3a, where black pixels denote
0.02 = αmin ≤α ≤0.04, grey pixels 0.04 ≤α ≤0.16 and
white pixels 0.16 ≤α ≤0.2 = αmax. Although the retina
has a spatial α-distribution far from random, this sim-
ulation is adequate to exhibit the features of our model
which can be extended to realistic spatial distributions.
In any case, the 10,000 pixels provide many possibilities
for picking a small subset (containing around 100 pixels),
which includes a recognizable pattern. This is not to im-
ply that 10,000 pixels ought to be measured in Alice’s
retina.
The simulation is just depicting that patterns
can be readily found in an array of randomly varying α.
For example, two such subsets are contained in the
two (yellow) boxes of Fig.3a. Among the pixels in those
boxes, we choose some having high-α in such a way that
they form the number ”2” (upper box) or the letter ”Y”
(lower box).
We augment those high-α pixels with a
larger number of low-α pixels, in such a way that the
combined set cannot reveal the pattern. We illuminate
all with pulses having the same average number of pho-
tons ˜I. An ideal photodetector would see the patterns in
Figs.3(c,e). This is what Eve would observe in the best
possible scenario she is equipped with an ideal photon
detector, and she would obviously be unable to infer any
pattern. In contrast, Alice would observe the patterns in
Figs.3(b,d) in the ideal case that the high-α pixels per-
ceive light, and the low-α pixels do not.
In reality, both high- and low-α pixels of Alice might or
might not perceive the light ﬂashes. To simulate that, we
sample independent Poisson variables for each of the illu-
minated pixels (i,j) with average αij ˜I, so that the pixel is
bright if the realization of the process exceeds the detec-
tion threshold K. Some of the possible realizations are
shown in Figs.3(f1-f6).
Alice is interrogated m times, asked to respond on
which symbol she saw, and given a choice of M symbols,
where M could easily be around 40 (alphabet, numbers,
etc.).
It is straightforward to calculate the false posi-
tive probability. Even if Eve is equipped with an ideal
photodetector, all she measures is an apparently random
pattern of illuminated spots with the same average num-
ber of photons. As she is unaware of Alice’s α-map, the
only option Eve has is to respond randomly given the
same choice of M symbols, hence the probability that


## Page 8


8
Alice  
Eve 
(a)
(b)
(c)
(d)
(e)
Alice’s retinal α-matrix
(f1)
(f2)
(f3)
(f4)
(f5)
(f6)
(g1)
(g2)
(g3)
(g4)
(g5)
(g6)
(g7)
(g8)
(g9)
(g10)
(g11)
(g12)
(g13)
(g14)
(g15)
(g16)
(g17)
(g18)
FIG. 3. Biometric Strategy. (a) We suppose Alice’s retina consists of 100 × 100 non-overlapping ganglion receptive cells that
can be individually addressed with a laser pulse. The light-path ending in each one of those is described by a characteristic α
value, which here takes a random value between αmin = 0.02 and αmax = 0.2 (we ignore the spatial dependence of α, i.e. in
a real retina the average α decreases going from center to periphery). The color coding in (a) is white for high-α values, i.e.
0.16 ≤α ≤0.2, grey for 0.04 ≤α ≤0.16 and black for low-α values, i.e. 0.02 ≤α ≤0.04. We can easily ﬁnd a number of
white pixels forming a pattern, for example the number ”2” (upper yellow box) or the letter ”Y” (lower yellow box). To the
set of pixels forming the pattern we add another set of low-α pixels so that in the combined set there is no discernible pattern.
However, Alice would ideally (only high-α pixels ﬁre) just see the pattern, as shown in (b) and (d). In contrast, even if Eve is
equipped with an ideal photodetector, all she would see is the combined set of pixels, shown in (c) and (e). Realistically, Alice
can miss some high-α pixels and see noise from some ﬁring low-α pixels. A few realizations of a Poisson simulation (a pixel
(i, j) is lighted if a Poisson random variable with average αij ˜I exceeds the detection threshold K = 6, where we used ˜I = 72)
are shown in (f1)-(f6) for the case of ”2”. (g1)-g(18) Example for realizing pfp ≈10−10 with m = 8 interrogations. Among the
illuminated spots of (c) we can form at least 18 patterns, in particular 2, 4, 6, S, v, 7, x, b, f, 3, h, t, q, d, Z, L, %, U. The
tested subject is oﬀered these 18 patterns from which she is supposed to pick her response. While Alice would most probably
perceive ”2”, since ”2” is the pattern formed by Alice’s high-α spots, Eve’s only option would be to randomly pick her response
among the 18 choices, thus after 8 interrogations one could achieve (1/18)8 ≈10−10 for the false-positive probability.
she correctly responds to m questions is pfp = (1/M)m.
For M = 40 and just m = 6 interrogations we obtain


## Page 9


9
pfp ≈10−10. Practically, m = 6 interrogations can be
realized in less than one minute of test time.
An example for the realization of the above scheme
is the following. In the illuminated set of spots shown
in Fig.3c, the tested subject could be oﬀered the choice
of M
= 18 patterns shown in Figs.3g1-g18.
These
patterns (and perhaps more) are formed by spots which
are a subset of the illuminated spots of Fig.3c. While
Alice would most probably perceive ”2”, since ”2” is
the pattern formed by the high-α spots of Alice, Eve
would be clueless as to which pattern Alice would
perceive and would have to randomly pick one of the 18
patterns as her response. Thus in this case, with m = 8
interrogations we can achieve pfp ≈10−10.
We
now calculate
the
probability
that
Alice
fails
the test. We assume that the pattern to be recognized is
formed by nH high-α spots. We also illuminate nL spots
of low-α to create noise for Eve. Suppose the probability
that Alice fails to see a pattern spot is bounded by pH,
while the probability to see a noise spot is bounded by
pL.
Without entering into cognitive issues of object
recognition, which would only increase Alice’s chances
to recognize the pattern, we assume that Alice fails
to recognize the pattern, if she wrongly gets at least
k > nHpH of the pattern spots, or if she sees at least
ℓ> nLpL noise spots.
Then, the probability P that
Alice fails to recognize the pattern satisﬁes
P ≤e−nHH
 k
nH |pH

+ e−nLH

ℓ
nL |pL

.
Thus the probability that Alice passes m questions is
larger than (1 −P)m, hence
pfn ≤1 −(1 −P)m
(10)
As in the examples of Figs.3(b,d) we take the pattern to
be composed of nH ≈25 pixels, and add another nL ≈75
”noise” pixels, so that in total we illuminate about 100
pixels. We assume that recognition is possible if Alice
misses at most 20% of the pattern’s pixels and at most
an equal number of noise pixels are perceived by her, i.e.
we take k = ℓ= 5. We choose the average photon number
per pixel ˜I by minimizing pfn and ﬁnd the minimum pfn =
5 × 10−4 occurs at ˜I = 72.
The achieved pfn depends dramatically on the values
of αL and αH.
Thus, if it is possible to create pat-
terns+noise by ﬁnding spots with lower αL and higher
αH, the probability that Alice will fail the test and will
have to retake it can be further reduced.
Finally, we
note that we refrained from introducing cognitive aspects
of object recognition into the calculation of pfn, i.e. we
chose as 20% what seems to be a reasonable percentage of
missed spots and added noise. We could have considered
maximum-likelihood image classiﬁcation strategies [55],
however the fundamental results would be unchanged.
VII.
THE QUANTUM ASPECT OF THIS
BIOMETRIC METHOD
There are several reasons why this biometric method
can be termed ”quantum”. (i) The method is essentially
a quantum parameter estimation process, where a classi-
cal parameter (here the optical loss of a particular light
path ending on a particular retinal spot) is estimated us-
ing a quantum process (here photodetection). Rod cells
realize the single photon detector, while the conscious
brain realizes the counter. (ii) While in this work we uti-
lize coherent light for illuminating the retinal spots, the
same measurement can in principle be performed with
single-photon sources [47, 48] or other non-classical light
sources. In fact, such sources provide an advantage for
the biometric methodology that will be explored else-
where. (iii) Finally, unlike other biometric methods, the
security of this method can be explicitly quantiﬁed by the
laws of quantum measurements and stated in terms of en-
ergy measurement resolution given in units of ℏ. This is
presented in detail in the following subsection.
A.
Quantum technology required to non-invasively
access the biometric information
As discussed previously, if an impostor, Eve, presents
herself as Alice and asks to be identiﬁed by the device,
no matter how technologically advanced Eve is, the only
strategy she has is to respond randomly to the device’s in-
terrogations. We will now entertain a diﬀerent way to foil
the device. Suppose that Eve is proximal to Alice (e.g.
1 m away), and while Alice is being interrogated by the
biometric device, Eve is secretly operating a highly ad-
vanced quantum sensor monitoring Alice’s activity. For
example, if Eve could measure the number of photons
scattered in Alice’s eye, and at the same time monitor
her brain activity, she might be possible to correlate these
observations and infer Alice’s α-map.
Before proceeding with the estimates, we note that in
the scenario of a single retinal spot being illuminated, if
Eve is aware of (or measures) the incident photon number
˜I, then she only needs to ”detect” brain activity in order
to infer α of that spot. We can easily force her to also re-
quire sensitive thermometry by changing (randomizing)
the incident photon number in each interrogation.
Now since α ≈0.1 on average, there will be on the
order of ns = 50 scattered photons for ˜I = 50 incident
photons. Eve could try to non-invasively detect a minute
temperature change in Alice’s eye (or in turn in the envi-
ronment), due to the energy deposited by the scattered
photons.
We use simple order-of-magnitude estimates
and consider just a single illuminated pixel, i.e. we ig-
nore the issue of spatial resolution of Eve’s measurement
needed for the multi-pixel scenario, and we also ignore
the thermal eye-environment contact as well as the eye’s
physiological cooling mechanisms (eye-body thermal con-
tact). So we will heavily underestimate the level of tech-


## Page 10


10
nology required by Eve.
Let us approximate the eye, having mass about m =
10 g, by water, the speciﬁc heat of which cw = 4 J/g/C.
Thus the ns scattered photons of wavelength λ = 532 nm
would deposit ns(hc/λ) of energy into the eye, so Eve
should be able to resolve the eye’s temperature change
δθ = ns(hc/λ)/mcw ≈10−19 ◦K. This would happen
during the pulse time τ = 0.1 s, so Eve should be able to
non-invasively measure the thermal energy deposited in
Alice’s eye with a resolution (kBδθ)τ ≈10−9ℏ.
Furthermore, it is known that the magnetic activity of
the brain can be modeled with current dipoles [50] pro-
ducing on the head’s surface, being about 10 cm away
from the dipoles, magnetic ﬁelds on the order of 1 fT
in the case of visual perception [51].
Hence at a dis-
tance 1 m away the ﬁelds will be attenuated (due to the
1/r3 distance dependence of dipolar ﬁelds) by a factor
103. Eve should thus be equipped with a magnetome-
ter having sensitivity at the 0.1 aT/
√
Hz level [56, 57].
Using the electron’s gyromagnetic ratio, this translates
to an energy resolution of 10−9ℏ. While modern optical
magnetometers [58, 59] are about three orders of mag-
nitude away from 10−9ℏ, quantum thermometers [60–62]
are many more orders of magnitude away.
VIII.
DISCUSSION
(i) The proposed biometric method resembles static vi-
sual perimetry [42, 63, 64], a diagnostic tool in ophthal-
mology used to assess e.g. glaucomatous disease. Perime-
try is the measurement of the diﬀerential light sensitivity,
i.e. the threshold of perception of a test object projected
on the visual ﬁeld against its background. Yet, there is a
signiﬁcant diﬀerence of our approach from visual perime-
try. The latter can hardly proﬁt from the idea of inter-
rogating only low-α or high-α spots in any of our serial,
Bayesian or ”parallel” pattern recognition schemes dis-
cussed in Secs. V-VI. The reason is that pathological pat-
terns could appear in any particular retinal spot or area,
and hence their detection requires the time-consuming
α-map estimate discussed in Sec.
IV. In other words,
detecting pathology poses a diﬀerent statistical inference
problem than verifying identity.
(ii) Even in the absence of some pathology, because of
the psychophysical character of the test, a ﬂuctuation in
the measured threshold at a particular testing point of
the same individual at diﬀerent times can be observed.
This could be related to the visual perception threshold
K, the exact value of which is still debated [30, 38]. More-
over, its value might depend on other physiological pa-
rameters and not even be constant for the same subject.
We used K = 6, but our estimates are robust and can
be extended to include a distribution of K. Similarly, it
is known that the parameter α is age-dependent. Again,
such issues can be mitigated by proper statistical anal-
ysis or slightly increased number of required interroga-
tions, i.e. they do not alter the fundamental principle or
the underlying statistics. Another technical point is the
ability to consistently target speciﬁc areas of the retina.
This is accomplished by fundus based eye-tracking [65]
as applied e.g. in optical coherence tomography [66].
(iii) We considered the perception threshold K to be
spatially constant across the retina. A spatial variation
of K could be considered to lead to a deterioration of
the identiﬁcation algorithm’s performance.
Counterin-
tuitively, the opposite is the case.
The reason is that
the algorithm is based on the variability of α across the
retina. But essentially, it is the variability of P

see

that
we take advantage of.
Now, the probability P

see

is
given by GK(α˜I). Tacitly assuming that K is constant,
the variability of α is translated into the variability of
P

see

. If the parameter K also varies independently, it
will add an independent channel of variability to P

see

,
and thus give the physical realization of the algorithm a
greater versatility.
(iv) Our method is a scotopic measurement, i.e. in the
dark-adapted eye, which is known to be tedious for the
human subject under examination. The required dark
adaptation (lasting at least half an hour) is a serious
limitation on the practicality of the method. However,
what we aim at in this work is the proof of principle of
the methodology using the rod response, which is well
studied and documented in terms of single-photon sensi-
tivity. We expect that cones and the light adapted eye,
which does not suﬀer from this limitation, will provide
similar capabilities for realizing the method. While cone
single photon detection capabilities are not broadly es-
tablished so far, cones have some unique characteristics,
like a much shorter integration time and a much faster
response/recovery time to repeated stimuli compared to
rods.
Furthermore they have a much wider dynamic
range, making ﬁne threshold determination easier. Thus
we expect we will be able to apply the same or a similar
methodology in photopic conditions.
(v) Any biometric method one can imagine suﬀers
from the possibility that the impostor, Eve, can have
access to the biometric data. For all biometric methods
known so far the biometric data are stored in a computer
database as classical information. If the privacy of these
databases is compromised, the security of all known bio-
metric methods can be readily thwarted. The biometric
method proposed here is not an exception in this respect,
i.e. it is assumed that the impostor cannot have access
to the stored biometric data of the device’s users.
(vi) Another common feature of all known biometric
modalities is that they cannot resist forceful tactics by
the impostor. The method proposed here is also prone
to failure if forceful tactics are allowed. Regarding for ex-
ample the pattern recognition strategy, Eve could force
Alice to reveal which j patterns she is perceiving (as-
suming in the worst case that not all M patterns can be
formed on Alice’s retina, i.e. j ≪M), so Eve could in-
crease here chances of success to (1/j)m. This scenario
can be easily mitigated by combining tests in both eyes,
eﬀectively doubling j and possibly requiring slightly more


## Page 11


11
interrogations than m = 6. Essentially, the M patterns
to choose from in order to reply to each interrogation
could be public information.
A more extreme scenario would be that Eve acquires
the biometric device, forcefully measures Alice’s α-map,
and then passes the test with a properly designed pho-
todetector mimicking Alice’s eye. We here wish to en-
tertain another scenario, because it has a scientiﬁc in-
terest in its own right. Since Alice would still have to
cooperate by properly responding to the light ﬂash in-
terrogations, in the event that she would not, Eve could
resort to a more subtle approach and measure (with Al-
ice either being conscious or sedated) Alice’s pupillary
light reﬂex [67–71], hoping to extract information on Al-
ice’s α-map. However, existing evidence suggest a higher
detection threshold for the pupillary reﬂex, and in gen-
eral, the relation of the physiological backgrounds of light
perception and pupillary reﬂex is poorly understood. In
any case, the relevance of this reﬂex measurement to the
proposed method, and its own potential for yet another
biometric quantiﬁer will be addressed elsewhere.
Summarizing, we have here presented the principal
workings of a quantum optical biometric identiﬁcation
method based on the photon counting capabilities of
the human retina, and the subsequent perception of
light. The method oﬀers an unprecedented level of se-
curity against malicious attacks.
In contrast with ex-
isting methods which work within classical physics, we
also placed limits on how technologically advanced an im-
postor has to be in quantum thermometry and quantum
magnetometry in order to foil the biometric device by
non-invasively monitoring the biometric activity of the
device’s users.
This work opens a venue for exploring
quantum optics in a biological context, having both a
fundamental scientiﬁc interest and the immediate poten-
tial for commercial applications in the security industry.
Appendix A
The probability P

see

that a coherent light pulse of
intensity I and duration T is perceived by a retinal spot
of loss parameter α is equal to GK(αIT ), where GK is
deﬁned in (1).
Proof:
Photons
are
incident
on
the
eyball
as
a
Poisson process of intensity I. Each incident photon is
detected at the retina with probability α independently
of others.
Hence, photons are detected as a Poisson
process of intensity αI ([72], pp 318). Interval lengths
between successive detections are independent exponen-
tial random variables with rate αI and the time TK
until the K-th detection follows the Erlang distribution
with scaling parameter αI and order parameter K ([72],
pp 316). That is, TK ∼
1
αI EK, where EK is a random
variable with cumulative distribution function GK. The
pulse will be perceived exactly if TK ≤T . Thus,
P

see

= P

TK ≤T

= P

EK ≤αIT

= GK(αIT ).
Appendix B
We will here derive the number of required interroga-
tions for the naive strategy of Sec. IV, namely the esti-
mation of the value of α. For a particular retinal spot
being interrogated ν times, the subject’s j-th response,
where j = 1, ..., ν, is a Bernoulli random variable Sj,
taking the values 1=see and 0=don’t see. Hence an esti-
mator for P[see] is 1
ν
νP
j=1
Sj. We will now calculate how
many times we have to interrogate a subject with pho-
ton pulses (number of pulses ν for each of the µ retinal
spots) in order to achieve a desired pfp and pfn. We will
obtain a lower bound on the number of interrogations
assuming an impostor, Eve, responds randomly to all νµ
interrogations.
A successful 1-spot test is deﬁned by an acceptance
region around Alice’s α parameter. In view of the re-
sult in Appendix A and the monotonicity of GK we
may recast the test in terms of the estimated P[see].
Call pC ≡GK(α˜I) the ”correct” probability and con-
sider integers nL, nR, to be determined later, such that
pL ≡
nL
ν
< pC <
nR
ν
≡pR.
We will consider that
the tested subject presenting herself as Alice passes the
1-spot test if nL < Pν
j=1 Sj < nR.
In terms of the
α-parameter the 1-spot test is passed if the estimated
α-value lies in the interval (aL, aR), where the left and
right acceptance limits are deﬁned by pL ≡GK(αL ˜I) and
pR ≡GK(αR ˜I) as shown in Fig.4a.
Let us now suppose that Eve chooses p uniformly in
(0, 1) and answers see with probability p, independently
for each interrogation. The number of see answers is then
uniformly distributed over the set [ν] = {0, 1, . . ., ν}. In-
deed, for k ∈[ν] we have
P

ν
X
j=1
Sj = k

=
Z 1
0
ν
k

pk(1 −p)ν−k dp
=
ν
k

k!(ν −k)!
(k + ν −k + 1)! =
1
ν + 1.
Hence, the probability that Eve successfully passes the
1-spot test is equal to nR−nL−1
ν+1
. Thus, given the desired
false positive probability, pfp, we must satisfy the follow-
ing inequality:
nR −nL −1
ν + 1
≤p1/µ
fp
.
(B1)
Next we will obtain a second inequality from the desired
false negative probability, pfn, which is the probability
that Alice fails the test. We will use Lemma 4.7.2 in [45]
to get a lower bound for the deviation of 1
ν
Pν
j=1 Sj from


## Page 12


12
α
αmin
αmax
αL
αR
α-acceptance
GK(αLI)
GK(αRI)
0
GK(αmaxI)
GK(αminI)
1
GK(αI)
GK-acceptance
~
~
~
~
~
GK(αI)
~
(a)
(b)
10-11
10-10
10-9
10-8
10-7
40
50
60
70
80
pfp
ν
pfn=10-3
pfn=10-4
pfn=10-5
pfn=10-6
pL
pR
pC
FIG. 4. (a) The desired level of precision in the estimate of the true α sets a range of acceptable values around the true α,
given by αL and αR, deﬁning the α-acceptance region, which lies within the possible α values, ranging from αmin to αmax. The
α-axis is mapped into the corresponding probability space by the function GK(x), which gives the probability to see a ﬂash
when x photons on average are detected by the tested spot of the retina. The inverse map leads from the measured P

see

to
α. (b) Number of interrogations per spot, ν, required to achieve a false-positive probability pfp for a test involving µ retinal
spots, for various values of the false negative probability pfn. For this plot we took µ = 50.
its expectation pC:
P
h
ν
X
j=1
Sj ≥nR
i
≥
1
p
8νpR(1 −pR)
e−νH
 pR
pC

P
h
ν
X
j=1
Sj ≤nL
i
≥
1
p
8νpL(1 −pL)
e−νH
 pL
pC

where H(x|y) is the relative Shannon entropy. Now, let
w = P
h
ν
X
j=1
Sj ≥nR
i
+ P
h
ν
X
j=1
Sj ≤nL
i
(B2)
be the probability that Alice fails the 1-spot test. The
probability that she fails the whole µ-spot test will then
be the probability that she fails at least one of the µ tests,
and this is equal to 1 −(1 −w)µ. This should be smaller
than the desired false-negative probability pfn. Using the
preceding estimates and the elementary inequality 4p(1−
p) ≤1 for all p ∈(0, 1) we arrive at the requirement
1 −
h
1 −
1
√
2ν

e−νH
 pR
pC

+ e−νH
 pL
pC
iµ
≤pfn
(B3)
To make further progress, suppose pR −pC ≃pC −pL,
and use Eq. (B1) to ﬁnd pR ≃pC + 1
2p1/µ
fp
and pL ≃
pC −1
2p1/µ
fp .
Using these in Eq.
(B3) and solving for
ν, we obtain the number of interrogations per spot that
are required to achieve a desired pfp and pfn for a given
number of spots µ. The result is shown in Fig.4b. For
example, to secure that by responding randomly Eve is
positively identiﬁed as Alice at most once per 10 billion
attempts, and that Alice would fail the test and hence
would have to be retested once per ten thousand times,
we require slightly more than 50 interrogations for each
of 50 retinal spots, i.e. a total of 2500 interrogations.
Appendix C
Deﬁne µA(i) = Ea
h
ln

ZA(αi,Si)
ZE(p,Si)
 Fi−1
i
and µE(i) =
EE
h
ln

ZA(αi,Si)
ZE(p,Si)
 Fi−1
i
. Then, for all i ∈N
µA(i) ≥H
 q
 1
2

> 0
(C1)
µE(i) ≤1
2 ln
 4q(1 −q)

< 0.
(C2)
Before we proceed with the proof of this assertion we
need to introduce some notation. Let us denote by π the
distribution of GK(α˜I) induced by the random choice of
α. This is a probability measure supported on [0, q]∪[1−
q, 1], such that for C ⊂[0, 1], π(C) = P

GK(α˜I) ∈C

.
In particular, we have p = E

GK(α˜I)

=
R
xdπ(x).
Since we randomly target a high-α or a low-α reti-
nal spot, we must have π([0, q]) = π([1 −q, 1]) =
1
2.
We will denote by πL (πH) the conditional distribu-
tion of GK(α˜I), given that we have selected to target
a low (high)-α spot. That is πL(C) = 2π(C ∩[0, q]) and
πH(C) = 2π(C ∩[1 −q, 1]). Finally, we will denote by qL
(respectively qH) the mean value of these measures, that
is
qL =
Z
x dπL(x) ≤q
and
qH =
Z
x dπH(x) ≥1 −q.
Hence,
p = qL + qH
2
∈(1 −q
2
, 1 + q
2
).


## Page 13


13
Proof: We condition ﬁrst on the value of αn to get
µA(i) = E
h
GK(αi ˜I) ln
 
GK(αi ˜I)
p
!
+
+
 1 −GK(αi ˜I)

ln
 
1 −GK(αi ˜I)
1 −p
! Fi−1
i
= E

H
 GK(αi ˜I)
p

,
since αi is independent of the information available up
to time i −1. Since π is the distribution of GK(α˜I),
µA(i) =
Z
H(x|p) dπ(x).
Recall that x 7→H(x|p) is decreasing in [0, p] and increas-
ing in [p, 1]. We may now split the integral over x ∈[0, q]
and x ∈[1 −q, 1]. Using that q < p < 1 −q, we further
obtain
µA(i) ≥1
2H(q|p) + 1
2H(1 −q|p)
= H
 q
 1
2

+ H(1
2|p) ≥H
 q
 1
2

.
We now turn to (C2).
µE(i) = EE
h
pi ln GK(αi ˜I)
p
+ (1−pi) ln 1 −GK(αi ˜I)
1 −p
Fi−1
i
≤max
n
E

ln GK(αi ˜I)
p

, E

ln 1 −GK(αi ˜I)
1 −p
o
= max
n Z
ln x
pdπ(x),
Z
ln 1 −x
1 −p dπ(x)
o
.
(C3)
We estimate the two terms in (C3) by Jensen’s inequality.
Z
ln x
p dπ(x) = 1
2
Z q
0
ln x
p dπL(x) + 1
2
Z 1
1−q
ln x
p dπH(x)
≤1
2
 ln qL
p + ln qH
p

= ln 2√qLqH
qL + qH
.
It is straightforward that, since qL ≤q < 1 −q ≤qH, the
last expression is maximized when qL = q and qH = 1−q.
Hence,
Z
ln x
p dπ(x) ≤ln
p
4q(1 −q).
Similarly,
Z
ln 1 −x
1 −p dπ(x) ≤ln
p
4q(1 −q),
and (C2) follows from (C3).
Appendix D
The process {R−1
n }n≥0 is a martingale for Alice, and
the process process {Rn}n≥0 is a martingale for Eve,
regardless of her answering strategy.
Proof: We have
EA

R−1
n
Fn−1

= R−1
n−1EA
h ZE(p, Sn)
ZA(αn, Sn)
Fn−1
i
If we condition ﬁrst on the value of αn, the righthand
side becomes
R−1
n−1E
h
GK(αn ˜I)
p
GK(αn ˜I)
+
 1 −GK(αn ˜I)

1 −p
1 −GK(αn ˜I)
Fn−1
i
= R−1
n−1.
Eve may have her own strategy and there is no reason for
her to answer see with probability p, as the test assumes.
The probability that she answers see may change form
one interrogation to another, may be random and may
even depend on previous answers. However, it may not
depend on α, as this information is undisclosed. Let us
denote by pn the probability that Eve answers see to the
n-th interrogation. We have
EE

Rn
Fn−1

= Rn−1EE
hZA(αn, Sn)
ZE(p, Sn)
Fn−1
i
= Rn−1EE

pn
GK(αn ˜I)
p
+ (1−pn)1−GK(αn ˜I)
1−p
Fn−1

.
There are two independent sources of randomness we are
integrating in the ﬁnal equation: Eve’s possibly random
choice of pn and the choice of αn. If we condition ﬁrst
on Eve’s answer the expression above becomes
Rn−1EE

pn
E

GK(αn ˜I)

p
+ (1−pn)1−E

GK(αn ˜I)

1 −p
Fn−1

= Rn−1EE

pn · 1 + (1−pn) · 1
Fn−1

= Rn−1.
It is useful to note at this point that the choice p =
E

GK(α˜I)

makes the preceding expression independent
of pn, leaving Eve no option to improve her odds by de-
vising a clever strategy.
Appendix E
An immediate consequence of (7) and (C1) is that
JA
n = ln

Rn
R0

−n H
 q
 1
2

is a submartingale for Alice.


## Page 14


14
We can apply once more the optional stopping theorem
to get
0 ≤EA

JA
T

= EA

ln RT
R0

−H
 q
1
2

EA

T ].
(E1)
By the deﬁnition of the stopping time T we must have
RT −1 < y R0, and since p ∈
  1−q
2 , 1+q
2

, we must have
min{p, 1 −p} ≥(1 −q)/2. Hence,
RT
R0
= RT −1
R0
ZA(αT , ST )
ZE(p, ST ) ≤
2
(1 −q)pfp
.
(E2)
The last two inequalities together imply that
EA

T

≤
ln
 2
(1−q)pfp

H
 q
 1
2)
.
(E3)
Likewise, JE
n
= ln

Rn
R0

−1
2 ln 4q(1 −q)n is a super-
martingale for Eve, and the optional stopping theorem
gives
EE

T

≤
2EE

ln RT
R0

ln
 4q(1 −q)
 ≤
2 ln
  2qminx
1+q

ln
 4q(1 −q)
,
where qmin = min{GK(αmin ˜I), 1 −GK(αmax ˜I)}.
[1] J. A. Unar, W. C. Seng and A. Abbasi, A review of bio-
metric technology along with trends and prospects, Patt.
Recogn. 47, 2674 (2014).
[2] C. H. Bennett, G. Brassard, C. Cr´epeau, R. Jozsa, A.
Peres, and W. K. Wootters, Teleporting an unknown
quantum state via dual classical and Einstein-Podolsky-
Rosen channels, Phys. Rev. Lett. 70, 1895 (1993).
[3] R. Ursin, F. Tiefenbacher, T. Schmitt-Manderbach, H.
Weier, T. Scheidl, M. Lindenthal, B. Blauensteiner, T.
Jennewein, J. Perdigues, P. Trojek, B. ¨Omer, M. F¨urst,
M. Meyenburg, J. Rarity, Z. Sodnik, C. Barbieri, H. We-
infurter and A. Zeilinger, Entanglement-based quantum
communication over 144 km, Nature Phys. 3, 481 (2007).
[4] K. A. Patel, J. F. Dynes, I. Choi, A. W. Sharpe, A. R.
Dixon, Z. L. Yuan, R. V. Penty, and A. J. Shields, Co-
existence of high-bit-rate quantum key distribution and
data on optical ﬁber, Phys. Rev. X 2, 041010 (2012).
[5] C. H. Bennett and G. Brassard, Quantum cryptography:
Public key distribution and coin tossing, Proceedings
of IEEE International Conference on Computers, Sys-
tems and Signal Processing, Bangalore, India, pp. 175-
179 (1984).
[6] A. K. Ekert, Quantum cryptography based on Bell’s the-
orem, Phys. Rev. Lett. 67, 661 (1991).
[7] N. Gisin, G. Ribordy, W. Tittel and H. Zbinden, Quan-
tum cryptography, Rev. Mod. Phys. 74, 145 (2002).
[8] J. Qiu, Quantum communications leap out of the lab,
Nature 508, 441 (2014).
[9] H.-K. Lo, X. Ma and K. Chen, Decoy state quantum key
distribution, Phys. Rev. Lett. 94, 230504 (2005)
[10] H.-K. Lo, M. Curty and B. Qi, Measurement-device-
independent quantum key distribution, Phys. Rev. Lett.
108, 130503 (2012).
[11] I. K. Kominis, The radical-pair mechanism as a paradigm
for the emerging science of quantum biology, Modern
Physics Letters B 29, 1530013 (2015).
[12] K. M. Vitalis and I. K. Kominis, Quantum-limited bio-
chemical magnetometers designed using the Fisher infor-
mation and quantum reaction control, Phys. Rev. A 95,
032129 (2017).
[13] M. A. Taylor and W. P. Bowen, Quantum metrology and
its application in biology, Phys. Rep. 615, 1 (2016).
[14] J. E. Dowling, The Retina (Harvard University Press,
Cambridge, 1987).
[15] R. H. Hadﬁeld, Single-photon detectors for optical quan-
tum information applications, Nature Photonics 3, 696
(2009).
[16] E.
Brumberg
and
S.
Vavilov,
Visuelle
messungen
der statistischen photonenschwankungen, Bulletin de
l’Acad´emie des Sciences de l’URSS. Classe des sciences
math´ematiques et naturelles 7, 919 (1933).
[17] S. Hecht, S. Shlaer and M. H. Pirenne, Energy, quanta
and vision, J. Gen. Physiol. 25, 819 (1942).
[18] H. L. deVries, The quantum character of light and its
bearing upon threshold vision, the diﬀerential sensitivity
and visual acuity of the eye, Physica 10, 553 (1943).
[19] A. Rose, The sensitivity performance of the human eye
on an absolute scale, J. Opt. Soc. Am. 38, 196 (1948).
[20] D. A. Baylor, T. D. Lamb and K.-W. Yau, Responses
of retinal rods to single photons, J. Physiol. 288, 613
(1979).
[21] F. Rieke and D. A. Baylor, Molecular origin of continuous
dark noise in rod photoreceptors, Biophys. J. 71, 2553
(1996).
[22] F. Rieke and D. A. Baylor, Origin of reproducibility in
the responses of retinal rods to single photons, Biophys.
J. 75, 1836 (1998).
[23] F. Rieke and D. A. Baylor, Single-photon detection by
rod cells of the retina, Rev. Mod. Phys. 70, 1027 (1998).
[24] F. Rieke and D. A. Baylor, Origin and functional impact
of dark noise in retinal cones, Neuron 26, 181 (2000).
[25] P. C. Nelson, Old and new results about single-photon
sensitivity in human vision, Phys. Biol. 13, 025001
(2016).
[26] P. Sekatski, N. Brunner, C. Branciard, N. Gisin and C.
Simon, Towards quantum experiments with human eyes
as detectors based on cloning via stimulated emission,
Phys. Rev. Lett. 103, 113601 (2009).
[27] N. Sim, D. Bessarab, C. M. Jones and L. A. Krivitsky,
Method of targeted delivery of laser beam to isolated
retinal rods by ﬁber optics, Biomed. Opt. Expr. 2, 2926
(2011).
[28] N. Sim, M. F. Cheng, D. Bessarab, C. M. Jones and L.
A. Krivitsky, Measurement of photon statistics with live


## Page 15


15
photoreceptor cells, Phys. Rev. Lett. 109, 113601 (2012).
[29] N. M. Phan, M. F. Cheng, D. A. Bessarab and L. A.
Krivitsky, Interaction of ﬁxed number of photons with
retinal rod cells, Phys. Rev. Lett. 112, 213601 (2014).
[30] J. N. Tinsley, M. I. Molodtsov, R. Prevedel, D. Wart-
mann, J. Espigul´e-Pons, M. Lauwers and A. Vaziri, Di-
rect detection of a single photon by humans, Nature
Communications 7, 12172 (2016).
[31] N. Brunner, C. Branciard and N. Gisin, Possible entan-
glement detection with the naked eye, Phys. Rev. A 78,
052110 (2008).
[32] F. Lucas and K. Hornberger, Incoherent control of the
retinal isomerization in rhodopsin, Phys. Rev. Lett. 113,
058301 (2014).
[33] R. Pizzi, R. Wang and D. Rossetti, Human visual system
as a double-slit single photon interference sensor: a com-
parison between modellistic and biophysical tests. PLoS
ONE 11, e0147464 (2016).
[34] A. Dodel, A. Mayinda, E. Oudot, A. Martin, P. Sekatski,
J.-D. Bancal, and N. Sangouard, Proposal for witnessing
non-classical light with the human eye, Quantum 1, 7
(2017).
[35] W. Bialek,
Biophysics (Princeton
University Press,
Princeton and Oxford, 2012).
[36] H. J. A. Dartnall and C. F. Goodeve, Scotopic luminos-
ity curve and the absorption spectrum of visual purple,
Nature 39, 409 (1937).
[37] H. B. Barlow, Vertebrate Photoreception (Ed. H. B. Bar-
low and P. Fatt, Academic, New York, 1977).
[38] G. D. Field, A. P. Sampath and F. Rieke, Retinal pro-
cessing near absolute threshold: from behavior to mech-
anism, Annu. Rev. Physiol. 67, 491 (2005).
[39] B. Teklu, S. Olivares and M. G. A. Paris, Bayesian es-
timation of one-parameter qubit gates, J. Phys. B: At.
Mol. Opt. Phys. 42, 035502 (2009).
[40] B. M. Escher, R. L. de Matos Filho and L. Davidovich,
General framework for estimating the ultimate precision
limit in noisy quantum-enhanced metrology, Nat. Phys.
7, 406 (2011).
[41] B. M. Escher, R. L. de Matos Filho and L. Davidovich,
Quantum metrology for noisy systems, Braz. J. Phys. 41,
229 (2011).
[42] A. Heijl and V. M. Patella, Essential Perimetry (Carl
Zeiss Meditec, California, 2002).
[43] M. Herrero-Collantes and J. C. Garcia-Escartin, Quan-
tum random number generators, Rev. Mod. Phys. 89,
015004 (2017).
[44] X. Ma, X. Yuan, Z. Cao, B, Qi and Z. Zhang, Quantum
random number generation, npj Quantum Inf. 2, 16021
(2016).
[45] R. B. Ash, Information Theory (Dover Publications, New
York, 1990).
[46] D. Williams, Probability with martingales (Cambridge
University Press, Cambridge UK, 1991).
[47] M. Oxborrow and A. G. Sinclair, Single-photon sources,
Contemp. Phys. 46, 173 (2005).
[48] G. S. Buller and R. J. Collins, Single-photon generation
and detection, Meas. Sci. Technol. 21, 012002 (2010).
[49] S. M. Barnett, Quantum Information (Oxford University
Press, Oxford, 2009).
[50] M. H¨am¨al¨ainen, R. Hari, R. J. Ilmoniemi, J. Knuu-
tila and O. V. Lounasmaa, Magnetoencephalography -
theory, instrumentation, and applications to noninvasive
studies of the working human brain, Rev. Mod. Phys. 65,
413 (1993).
[51] M. E. van de Nieuwenhuijzen,
A. R. Backus,
A.
Bahramisharif, C. F. Doeller, O. Jensen and M. A. J.
van Gerven, MEG-based decoding of the spatiotemporal
dynamics of visual category perception, NeuroImage 83,
1063 (2013).
[52] It is also possible to get bounds for other statistics
of the interrogation time T
by considering diﬀerent
(sub/super)-martingales related to the odds ratio Rn. For
instance, we can estimate the variance of T , or even prove
that it has exponentially decaying tails.
[53] T. Lindeberg, A computational theory of visual receptive
ﬁelds, Biol. Cyber. 107, 589 (2013).
[54] V. Balasubramanian and P. Sterling, Receptive ﬁelds and
functional architecture in the retina, J. Physiol. 587.12,
2753 (2009).
[55] M. N. Wernick and G. M. Morris, Image classiﬁcation at
low light levels, J. Opt. Soc. Am. A 3, 2179 (1986).
[56] D. Budker and M. V. Romalis, Optical magnetometry,
Nature Phys. 3, 227 (2007).
[57] H. Xia, A. B.-A. Baranga, D. Hoﬀman and M. V. Ro-
malis, Magnetoencephalography with an atomic magne-
tometer, Appl. Phys. Lett. 9, 211104 (2006).
[58] J. C. Allred, R. N. Lyman, T. W. Kornack, and M. V. Ro-
malis, High-sensitivity atomic magnetometer unaﬀected
by spin-exchange relaxation, Phys. Rev. Lett. 89, 130801
(2002).
[59] I. K. Kominis, T. W. Kornack, J. C. Allred and M. V.
Romalis, A subfemtotesla multichannel atomic magne-
tometer, Nature 422, 596 (2003).
[60] E. Mart´ın-Mart´ınez, A. Dragan, R. B. Mann and I.
Fuentes, Berry phase quantum thermometer, New J.
Phys. 15, 053036 (2013).
[61] C. Sab´ın, A. White, L. Hackermuller and I. Fuentes, Im-
purities as a quantum thermometer for a Bose-Einstein
condensate, Sci. Rep. 4, 6436 (2014).
[62] L. A. Correa, M. Mehboudi, G. Adesso and A. San-
pera, Individual quantum probes for optimal thermome-
try, Phys. Rev. Lett. 114, 220405 (2015).
[63] C. A. Johnson, M. Wall and S. h. Thompson, A history
of perimetry and visual ﬁeld testing, Opt. Vis. Sci. 88,
E8 (2011).
[64] M. Nebbioso, A. Barbato and N, Pescosolido, Scotopic
microperimetry in the early diagnosis of age-related mac-
ular degeneration: preliminary study, BioMed. Res. Int.,
671529 (2014).
[65] L. P. S. Ip, T. Q. Nguyen and D. U. Bartsch, Fundus
based eye tracker for optical coherence tomography, 26th
Annual Conf. on Engineering in Medicine and Biology :
EMBC-2004, Vol-1, 1-5 Sep, 2004, pp 1505- 1508.
[66] J. M. Schmitt, Optical Coherence Tomography (OCT):
A Review, IEEE J. Sel. Top. Quant. El. 5, 1205 (1999).
[67] O. Lowenstein, H. Kawabata and I. Loewenfeld, The
pupil as indicator of retinal activity. Am. J. Ophthalmol.
57, 569 (1964).
[68] M. E. Pennesi, A. L. Lyubarsky and E. N. Pugh Jr.,
Extreme responsiveness of the pupil of the dark-adapted
mouse to steady retinal illumination, Invest. Ophthalmol.
Vis. Sci. 39, 2148 (1998).
[69] M. T. H. Do, S. H. Kang, T. Xue, H. Zhong, H.-W.
Liao, D. E. Bergles and K.-W. Yau, Photon capture and
signalling by melanopsin retinal ganglion cells, Nature
457, 281 (2009).


## Page 16


16
[70] C. Kostic, S. V. Crippa, C. Martin, R. H. Kardon, M.
Biel, Y. Arsenijevic and A. Kawasaki, Determination of
rod and cone inﬂuence to the early and late dynamic of
the pupillary light response, Invest. Ophthalmol. Vis. Sci.
57, 2501 (2016).
[71] A. V. Rukmini, D. Milea, T. Aung and J. J. Gooley,
Pupillary responses to short-wavelength light are pre-
served in aging. Sci. Rep. 7, 43832 (2017).
[72] D. P. Bertsekas and J. N. Tsitsiklis, Introduction to Prob-
ability (Athena Scientiﬁc, Belmont, 2008).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]