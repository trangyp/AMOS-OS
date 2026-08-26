---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1802.07409v1
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1802.07409v1_Metastable_state_en_route_to_traveling-wave_synchronization_state

> Source: 1802.07409v1_Metastable_state_en_route_to_traveling-wave_synchronization_state.pdf

> Pages: 5

---


## Page 1


Metastable state en route to traveling-wave synchronization state
Jinha Park and B. Kahng∗
CCSS, CTP and Department of Physics and Astronomy, Seoul National University, Seoul 08826, Korea
The Kuramoto model with mixed signs of couplings is known to produce a traveling-wave syn-
chronized state. Here, we consider an abrupt synchronization transition from the incoherent state
to the traveling-wave state through a long-lasting metastable state with large ﬂuctuations. Our
explanation of the metastability is that the dynamic ﬂow remains within a limited region of phase
space and circulates through a few active states bounded by saddle and stable ﬁxed points. This
complex ﬂow generates a long-lasting critical behavior, a signature of a hybrid phase transition. We
show that the long-lasting period can be controlled by varying the density of inhibitory/excitatory
interactions. We discuss a potential application of this transition behavior to the recovery process
of human consciousness.
A hybrid phase transition (HPT) is a discontinuous
transition that accompanies critical phenomena.
Re-
cent hybrid percolation model studies [1–5] have discov-
ered that the system stays at a long-lasting metastable
preparatory step on the way to an explosive transition,
during which the so-called powder keg is accumulated [6].
In this regard, one may wonder if there exists a similar
metastable state in a synchronization transition. How-
ever, the presence of a metastable state has been rarely
highlighted in synchronization problems [7]. In this pa-
per, we reveal that such an intermediate metastable state
indeed exists on the way to a discontinuous synchroniza-
tion transition near the hybrid critical point. Moreover,
we show that this long-lasting metastable step can be
understood as persisting circulation inside a metastable
basin, characterized by balancing between saddle points
and stable ﬁxed points.
The Kuramoto model [8–12] has been successfully used
to investigate the properties of the synchronization tran-
sition (ST) and is expressed as
˙θi = ωi + K
N
N
X
k=1
sin(θk −θi),
(1)
where θi denotes the phase of each oscillator i; ωi is
the intrinsic frequency of an oscillator i, which follows
a distribution g(ω); K is the coupling constant; and
N is the number of oscillators in the system. STs are
characterized by a complex order parameter deﬁned as
Z(t) ≡PN
i=1 eiθi/N = ReiΨ(t), where R is the magni-
tude of the phase coherence; R = 0 for the incoherent
(IC) state, and R ̸= 0 for the coherent (C) state. For a
usual Gaussian g(ω), a continuous ST occurs at the criti-
cal coupling strength Kc. We instead use a uniform g(ω)
that exhibits an abrupt ST [8] with a post-jump critical-
ity β = 2/3 [13]. We remark that the bimodal g(ω) gives
a ﬁrst-order transition; however, it is not hybrid [14].
Here, the Kuramoto model with uniform g(ω) is ex-
tended to a mixture of two opposite-sign coupling con-
stants K1 < 0 and K2 > 0 to the fraction 1 −p and p,
motivated by excitatory and inhibitory couplings in neu-
ral networks [15, 16]. This extension further distinguishes
the C phase into π and traveling wave (TW) phases, and
is characterized by the steady rotation of the complex
angle of the order parameter Ω∼Ψ/t; Ω= 0 in the
π state, whereas Ω̸= 0 in the TW phase.
Hereafter,
we call our model the competing Winfree–Paz´o (c-WP)
model [8, 13, 15, 16], where ω and K of an oscillator
follow the probability distribution
g(ω, K) = 1
2γ Θ(γ −|ω|)

(1 −p)δ(K −K1) + pδ(K −K2)

,
(2)
where Θ represents the Heaviside step function. The co-
herent steady state is characterized by two groups of os-
cillators separated by an angle ∆in the phase space θ
that correspond to the inhibitory and excitatory pop-
ulations.
When ∆= π (π state), the two groups are
balanced and the steady-state rotation Ω= Ψ/t is zero.
When ∆̸= π, the TW order with Ω̸= 0 emerges.
We construct a self-consistency equation of the c-WP
model to obtain the steady-state order parameter solu-
tions (R, Ω) and perform numerical simulations to verify
their stabilities. Unexpectedly, a rich phase diagram in-
volving the HPT is obtained, as shown in Fig. 1. When
Q < 1, a supercritical HPT occurs and the behavior of
the order parameter is expressed as
R(p) =
 0
for p < pc,
Rc + a(p −pc)βp
for p ≥pc,
(3)
near the hybrid critical point Rc = γ/K2 and pc =
[Q + 4γ/(πK2)]/(Q + 1), with a noninteger exponent
βp = 2/3. When Q > 1, the critical exponent βp remains
the same while the post-jump branch has the opposite
direction and becomes unstable (Fig 2(a)). The transi-
tion from the IC phase to the π phase is ﬁrst-order and
exhibits a hysteresis curve in the region between pc and
pc,b. Notice that this subcritical HPT is diﬀerent from
the usual subcritical Hopf bifurcation. The unstable line
in the inset of Fig. 2(a) does not continuously drop to pc,
but instead has a ﬁnite gap of size γ/|K1|. On the other
hand, when g(ω) is Lorentzian [16], either a continuous
transition or a discontinuous transition occurs, and with-
arXiv:1802.07409v1  [cond-mat.stat-mech]  21 Feb 2018


## Page 2


2
0.2
0.4
0.6
γh
1
0
pc,b
pc
1
γt
γp
γc
0.25
0 pℓ
pc
pu
1
0.2
0.4
0.6
γh
1
0
pc,b
pc
1
Q=3
(a)
 
IC
H π
γt
γp
γc
0.25
0 pℓ
pc
pu
1
Q=0.5
(b)
■
 
▲
IC
π
H
TW
FIG. 1. (Color online) Phase diagram of synchronization tran-
sitions (STs) in the (p, γ) plane. p is the fraction of oscillators
with K2 > 0 and γ is the half width of the uniform distribu-
tion g(ω). The phase diagram contains the IC and π phases
in (a) and (b), and the TW phase when in (b). The solid line
represents a second-order transition, and both types of dashed
lines represent ﬁrst-order transitions, but the transition from
the IC phase to the π phase is hybrid. H represents a hystere-
sis zone. The symbol • at γh ≈0.78 in (a) corresponds to the
hybrid critical point of the Winfree–Paz´o (WP) model. The
symbols ▲at γc ≈0.18, • at γp ≈0.13, and ■at γt ≈0.064
in (b) represent critical points across which diﬀerent types of
phases or phase transitions emerge. The TW phase is absent
when Q > 1, or Q < 1 and γ > γc.
out any critical behaviors or presence of the metastable
states.
It is intriguing to check the stability of the self-
consistency solution. To perform this task, the so-called
empirical stability criterion proposed in Ref. [17] was
checked on the c-WP model. The stability matrix ˆS of
Ref. [17] is reproduced as follows:
 ˙δR
˙δψ

= A

(∂RFR) −1 R2∂ΩFR
R−1∂RFΩ
R∂ΩFΩ
 δR
δψ

≡A ˆS
δR
δψ

(4)
FR(R, Ω) ≡
Z
locked
dKdωg(ω, K)
q
1 −(ω/KR)2
FΩ(R, Ω) ≡
Z
drifting
dKdωg(ω, K)
q
(ω/KR)2 −1
(5)
where FR and FΩcorrespond to the real and imaginary
parts of the self-consistent order parameter.
The sys-
tem is (empirically) stable if and only if tr( ˆS) < 0 and
det( ˆS) > 0.
The result is presented by the blue solid
(stable) and dashed (unstable) curves in Figs. 2.
Our
numerical result suggests that this linear stability cri-
terion is partly fulﬁlled; some portions of the “stable”
π curve are not covered by the simulation data points
in the long-time limit. Interestingly, the order parame-
ter stays for quite a long time at these uncovered parts,
before it ﬁnally settles down in the stable stationary
line occupied by the symbols in Figs. 2(d)–2(e). These
parts uncovered by simulation data are not stable but
metastable. Fig. 3(a) shows the dynamic phase transi-
tion just above the hybrid critical point pc; a tiered ST
occurs from the IC phase to the TW phase through a
long-lasting metastable π phase. The order parameter
R exhibits large temporal and sample-to-sample ﬂuctu-
ations in this metastable interval. As p is increased fur-
ther, the ﬂuctuations decrease and the metastable period
becomes shorter (Figs. 3(c) and (d)). Subsequently, the
metastability is lost and the ST to the TW state occurs
directly. These behaviors terminate at pu.
The empirical linear ﬂows given by Eq. (5) around
each of the steady-state solutions (R, Ω) are shown in
Figs. 4(b)–4(d).
We remark that all TW solutions in
Figs. 4(b) and 4(c) exist in pairs owing to the symmetry
Ω↔−Ω. The red circle in Fig. 4(b) represents a TW
stable point, the green circle in Fig. 4(c) represents a TW
saddle point, and the red circle in Fig. 4(d) represents a
π state with neutral stability. In Fig. 4(d), the eigenvalue
in the Ωdirection is extremely small compared with that
of the R direction. Thus, the corresponding eigenvector
in the vertical Ωdirection can be eﬀectively understood
as a ˙Ω≈0 nullcline. The dotted blue line in Fig. 4(a)
and the blue line in Fig. 4(e) correspond to a trajectory
(R(t), Ω(t)) realized from simulation. In Fig. 4(e), the
system passes by the π state of Fig. 4(d) and is then
attracted by the saddle point of Fig. 4(c), forming unsta-
ble oscillations. It stays for a long time in the metastable
basin bounded by the Ωnullclines and the saddle point.
After escaping from the region, the dynamics ﬂows im-
mediately into the stable TW point.
We remark that
this trajectory is in fact a two-dimensional projection of
a higher-dimensional dynamics and all other degrees of
freedom do not vanish, inducing dynamic noise, until the
stable steady TW state is ﬁnally reached posterior to the
escapement.
Numerical simulations are performed using the fourth-
order Runge–Kutta method with ∆t = 0.01. The num-
ber of oscillators is N = 25 600 and total runtimes are
over t = 104 s, suﬃciently longer than the transient pe-
riods. Fluctuations in R and Ωat the stationary state
were averaged out over the last 10% of total runtime.
The stationary state may additionally depend on the ini-
tial coherence, especially in the hysteresis zone. Oscil-
lator phases are randomly assigned either in the range
[0, 2π] or [0, π/100], corresponding to the initially coher-
ent or incoherent state. Natural frequencies of oscillators
with K1 < 0 and K2 > 0 are regularly sampled between
[−γ, γ]. K2 is set to unity for convenience, leading to
K1 = −Q.
The two-step jump transition of Figs. 3 and 4(a)
near the hybrid critical point (pc, γt) closely resembles
those observed in the percolation on interdependent net-


## Page 3


3
FIG. 2.
(Color online) Diverse types of STs at Q = 3 and Q = 0.5. Green triangles and red circles denote data points of R(p)
obtained from simulations starting from the IC and C initial states, respectively. Solid(dashed) blue curves are self-consistency
solutions representing stable(unstable) states, according to the stability criterion, Eq.(5). In (a), a ﬁrst-order transition and
hysteresis occur between pc and pc,b.
The inset shows a close-up near pc.
We emphasize that the unstable line does not
continuously drop to pc, but instead has a ﬁnite gap of size γ/|K1|. In (b), a hybrid phase transition (HPT) occurs with the
critical exponent βp = 2/3 at pc. A close check of the exponent value is shown in the inset. The black line guides a slope of
2/3. (c) The TW phase emerges at γc and exists in the range [pℓ, pu]. When γt < γ < γc, IC ⇝π →TW →π occur with
increasing p. (d) At γ = γt, pc = pℓ; thus, IC 99K TW →π occur. The part of the π line (indicated by arrow) that is stable
according to the criterion is actually metastable. (e) When γ < γt (γ = 0.05), pℓ< pc < pu. R jumps from the IC state to the
TW state, and a hysteresis occurs between the IC and TW states at [pℓ, pc], where IC 99K TW →π occurs. Diﬀerent types of
arrows distinguish the types of phase transitions: continuous (→), discontinuous (99K), and hybrid (⇝).
works [1, 2], k-core percolation [3, 4] and the two-step
contagion model [5] near the critical point of the HPT.
In those systems, the order parameters also show a long-
lasting plateau with large ﬂuctuations, as we observed in
the metastable states of the c-WP model. During this
lengthy period, the system accumulates a so-called pow-
der keg for the later explosive transition [5, 6].
This
feature is also similar to the accumulation of similar-
size clusters near the transition point of the restricted
percolation model, which exhibits a HPT [18]. During
the metastable period of the c-WP model, the excita-
tory K2 oscillators form a number of velocity clusters,
i.e., clusters with similar velocities, when averaged over
short time intervals, as shown in Fig. 3(b). The number
of clusters discretely increases as the dynamics proceeds.
However, the divisions into small K2 clusters are tran-
sient. Eventually, those clusters merge into the largest
cluster and become monolithic in the TW state, whereas
the inhibitory K1 clusters break oﬀand become liquid.
It would be interesting to ﬁnd out whether those K2 clus-
ters play an equivalent role as a time bomb that sets oﬀ
an abrupt escapement of the metastable basin.
The c-WP synchronization model may have potential
applications to the recovery dynamics of human con-
sciousness from anesthetic-induced unconsciousness [19,
20]. Inhibitory anesthetics such as γ-aminobutyric acid
hinder cortical synchronization and the brain in turn
loses its ability to integrate information, vigilance, and
responsiveness [19]. Recent electroencephalogram (EEG)
experiments have revealed that the power spectrum of
the cortical local ﬁeld potentials during the conscious
state peak at a certain intrinsic frequency [20].
This
feature may be interpreted as an indicator of the TW
synchronization in the c-WP model. The consciousness
recovery dynamics of the anesthetic-induced brain passes
through a sequence of several discrete activity states.
Moreover, transitions between those metastable states
are abrupt [20]. A series of studies have previously mod-
eled the anesthetic recovery using Kuramoto-type syn-
chronization models [21, 22]. However, our model fur-
ther involves the metastable dynamic restoration of co-
herence by the discrete merging of velocity clusters. More
interestingly, it deals with excitatory and inhibitory neu-
ral interactions through a controllable parameter p and
the recovery period is reduced by increasing p beyond a
threshold pc, corresponding to the clinical ﬁndings that
the recovery time is reduced with lesser anesthetic con-
centration. We remark that reducing the inhibitory anes-
thetic concentration also corresponds to increasing p of
our model. Moreover, our analysis not only provides a vi-
sualization scheme but also opportunities to manipulate
the metastable terrain directly by controlling the saddle-
point position in the phase space.
In summary, we found that near the critical point of
the HPT, a tiered ST occurs from the IC state to the
TW state through the intermediate π state.
The dy-


## Page 4


4
2
3
4
1
FIG. 3.
(Color online) Tiered ST from the IC state to TW state through the metastable π state. R(t) was obtained at
various p for the system size N = 25 600, Q = 0.5, and γ = 0.064. (a) At p = 0.42, the TW state appears as the steady state,
and the state does as metastable. The solid and dashed lines correspond to R(t) and |Ω(t)|, respectively. Note that both the
temporal and sample-to-sample (inset) ﬂuctuations of R are large during the metastable period. In (b), the velocities of K2
oscillators are averaged over each speciﬁed time interval, as indicated by the corresponding colors and cluster numbers in (a).
The oscillators are indexed in ascending order of the intrinsic frequencies. We ﬁnd several intermediate states with diﬀerent
numbers of clusters composed of oscillators with similar velocities. The number of clusters increases as the stages proceed. In
(a), (c), and (d), as p is increased, the metastable period becomes shorter. Subsequently, the TW state is reached shortly.
FIG. 4.
(Color online) The ﬂow of the order parameter in the two-step synchronization transition. (a) Plot of blue dotted
curve R(t) vs t at p = 0.418. The time-averaged black curve ⟨R⟩is obtained using a sliding 40 -s time window centered at
each t with a window step of 1 s. (b)–(d) The linearized ﬂow in the (R, Ω) plane. Two stable points of π and TW states
are represented by red circles, and a saddle point of the TW state is shown in green. (e) An actual ﬂow is obtained from
simulations. x represents the starting point. (f) Frequencies of the dynamic ﬂow passing through each state in the phase space.
A few states (yellow) are active throughout the ﬂow.


## Page 5


5
namic process in the metastable state was explained as
the circulating ﬂow through a few active states in the
phase space, which exhibits large temporal and sample-
to-sample ﬂuctuations. We discussed that such a tiered
ST can be a potential model for the process by which
the brain recovers from pathological states to the awake
state.
This
work
was
supported
by
the
National
Re-
search Foundation of Korea by Grant No.
NRF-
2014R1A3A2069005.
∗bkahng@snu.ac.kr
[1] S. V. Buldyrev, R. Parshani, G. Paul, H. E. Stanley and
S. Havlin, Nature (London) 464, 1025 (2010).
[2] D. Zhou, A. Bashan, R. Cohen, Y. Berezin, N. Shnerb
and S. Havlin, Phys. Rev. E 90, 012803 (2014).
[3] G. J. Baxter, S. N. Dorogovtsev, K. E. Lee, J. F. F.
Mendes and A. V. Goltsev, Phys. Rev. X 5, 031017
(2015).
[4] D. Lee, M. Jo, and B. Kahng, Phys. Rev. E 94, 062307
(2016).
[5] D. Lee, W. Choi, J. Kert´esz and B. Kahng, Sci. Rep. 7,
5723 (2017).
[6] R. M. D’Souza and J. Nagler, Nat. Phys. 11, 531 (2015).
[7] P. Ji, T. K. DM. Peron, P. J. Menck, F. A. Rodrigues
and J. Kurths, Phys. Rev. Lett. 110, 218701 (2013).
[8] A. T. Winfree,
The Geometry of Biological Time
(Springer, Berlin, 1980).
[9] Y. Kuramoto, in International Symposium on Mathemat-
ical Problems in Theoretical Physics, edited by H. Araki,
Lecture Notes in Physics Vol. 30 (Springer, New York,
1975).
[10] S. H. Strogatz, Sync: The Emerging Science of Sponta-
neous Order (Hyperion, New York, 2003).
[11] G. V. Osipov, J. Kurths and C. Zhou, Synchronization
in Oscillatory Networks (Springer, Berlin, 2007).
[12] S. Boccaletti, The Synchronized Dynamics of Complex
Systems, (Elsevier, Oxford, U.K., 2008).
[13] D. Paz´o, Phys. Rev. E 72, 046211 (2005).
[14] E. A. Martens, E. Barreto, S. H. Strogatz, E. Ott, P. So
and T. M. Antonsen, Phys. Rev. E 79, 026204 (2009).
[15] C. B¨orgers, and N. Kopell, Neural Comput. 15, 509
(2003).
[16] H. Hong and S. H. Strogatz, Phys. Rev. Lett. 106, 054102
(2011).
[17] D. Iatsenko, S. Petkoski, P. V. E. McClintock and A.
Stefanovska, Phys. Rev. Lett. 110, 064101 (2013).
[18] Y. S. Cho, J. S. Lee, H. J. Herrmann and B. Kahng,
Phys. Rev. Lett. 116, 025701 (2016).
[19] M. T. Alkire, A. G. Hudetz, G. Tononi, Science
322,
876 (2008).
[20] A. E. Hudson, D. P. Calderon, D. W. Pfaﬀ, A. Proekt,
Proc. Natl. Acad. Sci. U.S.A. 111, 9283 (2014).
[21] J. Y. Moon, J. Kim, T. W. Koh, M. Kim, Y. Iturria-
Medina, J. H. Choi, J. Lee, G. A. Mashour, and U. Lee,
Sci. Rep. 7, 46606 (2017).
[22] U. Lee, M. Kim, K. Lee, C. M. Kaplan, D. J. Clauw, S.
Kim, G. A. Mashour and R. E. Harris, Sci. Rep. 8, 243.
(2018)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1802_07409v1_metastable_state_en_route_to_traveling_wave_synchronization_state
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1802_07409V1_METASTABLE_STATE_EN_ROUTE_TO_TRAVELING_WAVE_SYNCHRONIZATION_STATE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
