---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1606.08313v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1606.08313v1_Integrated_Information_and_Metastability_in_Systems_of_Coupled_Oscillators

> Source: 1606.08313v1_Integrated_Information_and_Metastability_in_Systems_of_Coupled_Oscillators.pdf

> Pages: 5

---


## Page 1


Integrated Information and Metastability in Systems of Coupled Oscillators
Pedro A.M. Mediano,∗Juan Carlos Farah, and Murray Shanahan
Department of Computing, Imperial College London
(Dated: June 28, 2016)
It has been shown that sets of oscillators in a modular network can exhibit a rich variety of
metastable chimera states, in which synchronisation and desynchronisation coexist. Independently,
under the guise of integrated information theory, researchers have attempted to quantify the extent
to which a complex dynamical system presents a balance of integrated and segregated activity. In
this paper we bring these two areas of research together by showing that the system of oscillators
in question exhibits a critical peak of integrated information that coincides with peaks in other
measures such as metastability and coalition entropy.
Keywords: Synchronisation, chimera states, metastability, integrated information
I.
INTRODUCTION
Systems of coupled oscillators are ubiquitous both in
nature and in the human-engineered environment, making
them of considerable scientiﬁc interest [1]. A variety of
mathematical models of such systems have been devised
and their synchronisation properties have been the sub-
ject of much study. Typical studies of this sort, such as
the classic work of Kuramoto [2], examine the conditions
under which the system converges on a stable state of
either full synchronisation or desynchronisation, perhaps
identifying an order parameter that determines a critical
phase transition from one state to the other. The collec-
tion of known attractors of such systems was enlarged
with the discovery of so-called chimera states, in which
the system of oscillators partitions into two stable subsets,
one of which is fully synchronised while the other remains
permanently desynchronised [3].
Although systems of coupled oscillators that converge
on stable states are both mathematically interesting and
scientiﬁcally relevant, they are by no means representative
of all real-world synchronisation phenomena. For exam-
ple, the brain exhibits synchronous rhythmic activity on
multiple spatial and temporal scales, but never settles into
a stable state. Although it enters chimera-like states of
high partial synchronisation, these are only temporary. A
system of coupled oscillators that continually moves from
one highly synchronised state to another under its own
intrinsic dynamics is said to be metastable. In [4], it was
shown that a modular network of phase-lagged Kuramoto
oscillators will exhibit metastable chimera states under
certain conditions. Variants of this model have since been
used to replicate the statistics of the brain under a variety
of conditions, including the resting state [5], cognitive
control [6], and anaesthesia [7].
In a separate line of enquiry, a number of researchers
have attempted to pin down the notion of dynamical
complexity. A system is said to have high dynamical com-
plexity if it exhibits a balance of integrated and segregated
activity, where a system’s activity is integrated to the
∗pmediano@imperial.ac.uk
extent that its parts inﬂuence each other and segregated
to the extent that its parts act independently [8]. Promi-
nent among these attempts is the Integrated Information
Theory (IIT), originally proposed by Balduzzi and Tononi
[9], but extended by multiple authors ever since [10–12].
In the present paper, we connect these two lines of en-
quiry by demonstrating that modular networks of coupled
oscillators of the sort described in [4] not only exhibit
metastable chimera states, but also have high dynamical
complexity. Moreover, we show that measures of both
phenomena peak in the narrow critical region of the pa-
rameter space wherein the system is poised between order
and disorder, and IIT oﬀers a rich picture of dynamical
complexity in this critical regime. To our knowledge, this
is the ﬁrst description of a dynamical system in which the
three major complexity indicators of criticality, metasta-
bility, and integrated information all appear.
II.
METHODS
We examine a system of coupled Kuramoto oscillators,
extensively used to study non-linear dynamics and syn-
chronisation processes [13]. We build upon the work of [4]
with a community-structured network of oscillators. The
network is composed of 8 communities of 32 oscillators
each, with every oscillator being coupled to all other os-
cillators in its community with probability 1 and to each
oscillator in the rest of the network with probability 1/32.
The state of each oscillator i is captured by its phase θi,
the evolution of which is governed by the equation
dθi
dt = ω +
1
κ + 1
X
j
Kij sin (θj −θi −α) ,
(1)
where ω is the natural frequency of each oscillator, κ is the
average degree of the network, K is the connectivity matrix
and α is a global phase lag. We set ω = 1 and κ = 63.
To reﬂect the community structure, the coupling between
two oscillators i, j is Kij = 0.6 if they are in the same
community or Kij = 0.4 otherwise. We tune the system by
modifying the value of the phase lag, parametrised by β =
π/2 −α. We note that the system is fully deterministic,
i.e. there is no noise injected in the dynamical equations.
arXiv:1606.08313v1  [q-bio.NC]  27 Jun 2016


## Page 2


2
A.
Metastability
In this section we review the basic concepts behind
metastability and how it is quantiﬁed, following a similar
description to that of [4].
The building block of the dynamical quantities we study
in this article is the instantaneous synchronisation R, that
quantiﬁes the dispersion in θ-space of a given set of oscil-
lators. In general, we denote as Rc(t) the instantaneous
synchronisation of a community c of oscillators at time t,
given by
Rc(t) = |⟨eiθj(t)⟩j∈c| .
(2)
To quantify metastability, we use the metastability index
λ, which is deﬁned as the average temporal variance of
the synchrony of each community c, i.e.
λc = vart Rc(t)
(3a)
λ = ⟨λc⟩c .
(3b)
Last, we also deﬁne global synchrony ξ as the average
across time and space of instantaneous synchrony,
ξ =

Rc(t)

t,c
 .
(4)
According to Eq. (2), Rc (and therefore ξ) is bounded
in the [0, 1] interval. Rc(t) will be 1 if all oscillators in c
have the same phase at time t, and will be 0 if they are
maximally spread across the unit circle. This [0, 1] bound
on R allows us to place an upper bound on λ – assuming a
unimodal synchrony distribution, the maximum possible
value of λ is λmax = 1/9.
As deﬁned in Eq. (3a), λc represents the size of the
ﬂuctuations in the internal synchrony of a community.
A system that is either hypersynchronised or completely
desynchronised will have a very small λc, whereas one
whose elements ﬂuctuate in and out of synchrony will
have a high λc. In other words, a system of oscillators
exhibits metastability if its elements remain in the vicinity
of a synchronised state without falling into such a state
permanently.
B.
Integrated Information
Although other information-theoretic quantities have
also been linked to complexity in a neuroscience context
[7, 14], we take integrated information Φ as the main
informational measure of complexity in our study [9].
There are more modern accounts of the theory [15, 16],
but the latest versions have not been as thoroughly studied
and are not amenable to easy estimation from time series
data. For these reasons, we focus on the methods in [10]
to empirically estimate Φ from an observed time series.
The building block of integrated information is eﬀective
information, ϕ. Eﬀective information quantiﬁes how much
better a system X is at predicting its own future (or
decoding its own past) after a time τ when it is considered
as a whole compared to when it is considered as the
sum of two subsystems M {1,2}.
We refer to τ as the
integration timescale. In other words, ϕ evaluates how
much information is generated by the system but not
by the two subsystems alone. For a speciﬁc bipartition
B = {M 1, M 2}, the eﬀective information of the system
beyond B is
ϕ[X; τ, B] = I(Xt−τ, Xt) −
2
X
k=1
I(M k
t−τ, M k
t ) .
(5)
The main idea behind the computation of Φ is to ex-
haustively search all possible partitions of the system and
calculate the eﬀective information of each of them. Among
those we select the partition with lowest ϕ (under some
considerations, see below), termed the Minimum Informa-
tion Bipartition (MIB). Then, the integrated information
of the system is the eﬀective information beyond its MIB.
Given the above expression for ϕ, Φ is deﬁned as
Φ[X, τ] = ϕ[X; τ, BMIB]
(6a)
BMIB = argB min ϕ[X; τ, B]
K(B)
(6b)
K(B) = min

H(M 1), H(M 2)
	
,
(6c)
where K is a normalisation factor to avoid biasing Φ to
excessively unbalanced bipartitions. Deﬁned this way,
Φ can be understood as the minimum information loss
incurred by splitting the system into two subsystems.
It quantiﬁes the collective emergent behaviour that is
present in the whole system but not in any bipartition.
III.
RESULTS
We ran 1500 simulations with values of β distributed
uniformly at random in the range [0, 2π) using RK4 with
a stepsize of 0.05 for numerical integration. Each simula-
tion was run for 5 × 106 timesteps, of which the ﬁrst 104
are discarded to avoid eﬀects from transient states. All
information-theoretic measures are reported in bits.
We ﬁrst study the system from a purely dynamical per-
spective, following the analysis in [4]. Global synchrony
and metastability are shown in Fig. 1. The ﬁrst character-
istic we observe is that there are two well diﬀerentiated
dynamical regimes – one of hypersynchronisation and one
of complete desynchronisation, with strong metastability
appearing in the narrow transition bands between one
and the other.
It is in this transition region where the oscillators oper-
ate in a critical regime poised between order and disorder
and complex phenomena appear. As the system moves
from desynchronisation to full synchronisation there is a
sharp increase in metastability, followed by a smoother
decrease as the system becomes hypersynchronised. In
the region 0 < β < π/8, the system remains in a complex
equilibrium between an ordered and a disordered phase.


## Page 3


3
0
0.2
0.4
0.6 0
0.02
0.04
Metastability λ
0
0.2
0.4
0.6
0.8
1
Synchrony ξ
λ
ξ
0
π
2
π
3π
2
0
0.02
0.04
Phase lag β
λ
0
0.2
0.4
0.6
0.8
1
ξ
FIG. 1. Global synchrony and metastability for diﬀerent phase
lags β for the whole [0, 2π) range (bottom) and around the
critical transition region (top). Rapid increase of metastability
marks the onset of the phase transition. Note the diﬀerent β
ranges in both plots.
A.
Information-theoretic analysis
One feature of Φ (and of any other information-theoretic
measure), compared to λ, is that it does not need to be cal-
culated directly from the state of the system. According
to its deﬁnition, Φ is substrate-agnostic, meaning that the
relevant quantity for the calculation of Φ is not the physi-
cal state of the system, but some informational state – the
conﬁguration of the system that we consider to contain
information. Therefore, we must deﬁne an informational
state mapping, that extracts the information-bearing sym-
bols from the physical state of the system.
Although calculating Φ on the real-valued phases is
possible, for simplicity we choose the coalition conﬁgura-
tion of the system as the informational state, deﬁned as
the set of communities that are highly internally synchro-
nised. To calculate the coalition conﬁguration at time t
we calculate Rc(t) of each community and threshold it,
such that
Xc
t =
(
1
if Rc(t) > γ
0
otherwise.
We refer to γ as the coalition threshold. After calculat-
ing the coalitions, the history of the system is reduced to a
time series with 8 binary variables. Having a multivariate
discrete time series, it is now tractable to compute Φ. By
default, we use γ = 0.8 in all our analyses shown here.
As depicted in Fig. 2, Φ shows a similar behaviour
to λ – it peaks in the transition regions and shrinks in
the fully ordered and the fully disordered regimes. We
also compare Φ with arguably the simplest information-
theoretic measure – entropy H. The entropy of the state
of the network calculated on the coalitions Xt forms the
coalition entropy Hc.
0
0.1
0.2
0.3
0.4
0.50
0.5
1
1.5
2
2.5
Phase lag β
Integrated Information Φ
0
2
4
6
8
Coalition Entropy Hc
Φ
Hc
FIG. 2. Integrated information Φ and coalition entropy Hc in
the phase transition. Within the broad region between order
and disorder in which Hc rises there is a narrower band in
which complex spatiotemporal patterns generate high Φ.
Both Φ and Hc peak precisely at the same point. Al-
though both measures depend on the chosen coalition
threshold γ, the results are qualitatively the same for a
wide range of thresholds.
Although it peaks in the same region as λ and Hc,
we note that Φ reveals new properties of the system
by virtue of incorporating temporal information in its
deﬁnition.
That is, to have a high Φ a system must
exhibit complex spatial and temporal patterns. We can
verify this by performing a random time-shuﬄe on the
time series. This shuﬄing leaves λ and Hc unaltered, as
they don’t explicitly depend on time correlations, but has
a high impact on Φ, which shrinks to zero. This indicates
that Φ is sensitive to properties of the system that are
not reﬂected by other measures.
Furthermore, Φ can be used to investigate the behaviour
of the system at multiple timescales. Figure 3 shows the
behaviour of Φ for several values of τ, and compares it
with standard time-delayed mutual information (TDMI)
I(Xt−τ, Xt).
The ﬁrst thing we note is that Φ and TDMI have oppo-
site trends with τ. TDMI decreases for longer timescales
while Φ increases. At short timescales the system is highly
predictable – thus the high TDMI – but this short-term
evolution does not involve any system-wide interaction
– thus the low Φ. Furthermore, at these timescales Φ is
negative, which can be interpreted as an indication of
redundancy [17] in the evolution of the system: the parts
share some information, such that they separately con-
tain more information about their past than the whole
system about its past. For larger τ TDMI decreases, as
the evolution of the system becomes harder to track using
the coalition conﬁguration. Simultaneously, Φ becomes
higher, indicating that the remaining TDMI has a stronger
integrated component that is not accounted for by the
TDMI of the partitions of the system. Overall, we see a


## Page 4


4
0
0.1
0.2
0.3
0.4
0.5
0.0
1.0
2.0
Φ[X, τ]
τ = 1
τ = 10
τ = 100
0
0.1
0.2
0.3
0.4
0.5
0.0
2.0
4.0
6.0
Phase lag β
I(Xt−τ, Xt)
FIG. 3. Integrated information Φ and time-delayed mutual
information I(Xt−τ, Xt) for several timescales τ. See text for
details.
clear trend of TDMI diminishing at longer timescales but
becoming progressively more integrated in nature.
It might seem counterintuitive to the reader that both
TDMI and Φ converge to a non-zero value for arbitrarily
high τ. However, recall that the system is deterministic,
so there is no reason to expect TDMI to vanish even
in the τ →∞limit.
Perfect knowledge of all of the
oscillators’ phases at any given time step is enough to
reconstruct the whole history of the system. The reason
why we see a decreasing TDMI is because the informa-
tional state we chose (the coalition conﬁguration) is not
descriptive enough to capture the evolution of the system
perfectly. That is, this is not a result of stochasticity, but
of degeneracy.
Put another way, the TDMI of the whole system re-
mains non-zero in the τ →∞limit because we are dealing
with a causally closed system. Again, if we considered
the totality of the system’s state (i.e. the phases θi) then
TDMI would be maximal and constant for any τ. In
contrast, when considering the TDMI of any partition M
we start dealing with a causally open system, since one
partition is aﬀected by the other. This eﬀectively intro-
duces stochasticity in our observations Mt, which does
cause TDMI of the partition to vanish when τ →∞. This
explains that the TDMI of the whole system converges
to a non-zero value for large τ while the TDMI of any
partition fades to zero, leaving a positive Φ.
Finally, it is interesting to combine the insights from the
dynamical and information-theoretic analyses. Inspecting
Figs. 1 and 2 we see that the peak in Φ is much narrower
than the peaks in λ and Hc. While some values of β do
give rise to non-trivial dynamics, it is only at the centre
of the critical region that these dynamics give rise to
integration. A certain degree of internal variability is
necessary to establish integrated information, but not all
conﬁgurations with high internal variability lead to a high
Φ. This means that Φ is sensitive to more complicated
dynamic patterns than the other measures considered,
and is in that sense more discriminating.
We note that λ is a community-local quantity – that is,
the calculation of λc for each community is independent of
the rest. Conversely, Φ relies exclusively on the irreducible
interaction between communities. These two quantities
are nevertheless intrinsically related, insofar as internal
variability enables the system to visit a larger repertoire
of states in which system-wide interaction can take place.
B.
Robustness of Φ against measurement noise
We will now consider the impact of measurement noise
on Φ, wherein the system runs unchanged but our record-
ing of it is imperfect. For this experiment we run the
(deterministic) simulation as presented in the previous
section and take the binary time series of coalition con-
ﬁgurations. We then emulate the eﬀect of uncorrelated
measurement noise by ﬂipping each bit in the time series
with probability p, yielding the corrupted time series ˆX.
Finally we recalculate Φ on the corrupted time series,
and show the results in Fig. 4. To quantify how fast Φ
changes we calculate the ratio between the corrupted and
the original time series,
η = Φ[ ˆX, τ]
Φ[X, τ] .
(7)
In order to avoid instabilities as Φ[X, τ] gets close to
zero, we calculate η only in the region within 0.5 rad of
the centre of the peak, where Φ[X, τ] is large. The inset
of Fig. 4 shows the mean and standard deviation of η at
diﬀerent noise levels p.
0
0.1
0.2
0.3
0.4
0.5
0
0.5
1
1.5
2
Phase lag β
Φ[ ˆ
X, τ]
p = 0.00
p = 0.02
p = 0.04
p = 0.06
0
0.05 0.1 0.15 0.2
0
0.5
1
p
η
FIG. 4. Integrated information Φ for diﬀerent levels of mea-
surement noise p. Inset: (blue) Mean and variance of the ratio
η between Φ of the corrupted and the original time series.
(red) Exponential ﬁt η = exp(−p/ℓ), with ℓ≈0.04.


## Page 5


5
We ﬁnd that Φ monotonically decays with p, reﬂecting
the gradual loss of the precise spatiotemporal patterns
characteristic of the system. The distortion has a greater
eﬀect on time series with greater Φ, but preserves the
dominant peak in β ≈0.15. The inset shows that both
the mean and variance of η decay as a clean exponential
with p. Φ is highly sensitive to noise and undergoes a
rapid decline, as a measurement noise of 5% wipes out
70% of the perceived integrated information of the system.
IV.
CONCLUSION
We have presented a community-structured network
of Kuramoto oscillators and discussed their collective
behaviour in terms of metastability [4] and integrated
information [9]. We showed that the system undergoes
a phase transition whose critical region presents a sharp,
clear peak of integrated information Φ that coincides with
a strong increase in metastability. To our knowledge, this
is the ﬁrst description of a dynamical system in which
the three major complexity indicators of criticality, high
metastability, and high integrated information all appear.
The resulting conﬂuence of two major research directions
in complexity science suggests that this is a system that
merits further study.
In the context of the present model, the high internal
variability of the system’s components enables system-
wide interaction, which in turn leads to high Φ. As we
have seen, the system presents a region of high metasta-
bility, but notably it is only within an even narrower band
that we ﬁnd strong integrated information. Moreover, as
we have also seen, shuﬄing the time series data preserves
the peak of metastability, despite the fact that the result is
meaningless. By contrast, Φ only peaks when the relevant
temporal structure is present in the data. In this way we
provide evidence that complex dynamics – as quantiﬁed
by the metastability index λ – are a necessary but not
suﬃcient condition for complex information processing –
as quantiﬁed by integrated information Φ.
Dynamical and information-theoretic measures provide
diﬀerent lenses through which we can understand a sys-
tem, and oﬀer complementary views of its behaviour.
Our ﬁndings support the claim that Φ, despite having
some theoretical drawbacks [11], is a valuable tool for
understanding complex spatial and temporal behaviour
in dynamical systems, particularly when combined with
other analysis techniques.
[1] A. Pikovsky, M. Rosenblum,
and J. Kurths, Synchro-
nization: A Universal Concept in Nonlinear Sciences
(Cambridge University Press, Cambridge, 2001) p. 432.
[2] Y. Kuramoto, Chemical Oscillations, Waves and Turbu-
lence (Dover Publications, 1984) p. 164.
[3] M. J. Panaggio and D. M. Abrams, Nonlinearity 28, R67
(2015), arXiv:1403.6204.
[4] M. Shanahan, Chaos 20, 013108 (2010), arXiv:0908.3881.
[5] J. Cabral, E. Hugues, O. Sporns, and G. Deco, NeuroIm-
age 57, 130 (2011).
[6] P. J. Hellyer, G. Scott, M. Shanahan, D. J. Sharp, and
R. Leech, The Journal of Neuroscience 35, 9050 (2015).
[7] M. Schartner, A. Seth, Q. Noirhomme, M. Boly, M.-A.
Bruno, S. Laureys,
and A. B. Barrett, PloS One 10,
e0133532 (2015).
[8] M. Shanahan, Physical Review E 78, 041924 (2008).
[9] D. Balduzzi and G. Tononi, PLoS Computational Biology
4, e1000091 (2008).
[10] A. B. Barrett and A. K. Seth, PLoS Computational Biol-
ogy 7, e1001052 (2011).
[11] V. Griﬃth, arXiv:1401.0978.
[12] M. Tegmark, arXiv:1601.02626.
[13] D. M. Abrams, R. Mirollo, S. H. Strogatz,
and D. A.
Wiley, Physical Review Letters 101, 084103 (2008).
[14] J.-R. King, J. D. Sitt, F. Faugeras, B. Rohaut, I. El
Karoui, L. Cohen, L. Naccache, and S. Dehaene, Current
Biology 23, 1914 (2013).
[15] M. Oizumi, L. Albantakis, and G. Tononi, PLoS Compu-
tational Biology 10, e1003588 (2014).
[16] G. Tononi, Archives Italiennes de Biologie 150, 56 (2012).
[17] A. B. Barrett, arXiv:1411.2832.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]