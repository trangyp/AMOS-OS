---
canon-group: reference
rscf-state: source-claim
arxiv_id: 704.1427
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 0704.1427_Photo-assisted_shot_noise_in_Coulomb_interacting_systems

> Source: 0704.1427_Photo-assisted_shot_noise_in_Coulomb_interacting_systems.pdf

> Pages: 4

---


## Page 1


arXiv:0704.1427v1  [cond-mat.mes-hall]  11 Apr 2007
PHOTO-ASSISTED SHOT NOISE IN COULOMB INTERACTING SYSTEMS
A. CR´EPIEUX, M. GUIGOU, A. POPOFF, P. DEVILLARD, AND T. MARTIN
Centre de Physique Th´eorique, CNRS Luminy case 907, 13288 Marseille cedex 9, France
We consider the ﬂuctuations of the electrical current (shot noise) in the presence of a voltage
time-modulation. For a non-interacting metal, it is known that the derivative of the photo-
assisted noise has a staircase behavior. In the presence of Coulomb interactions, we show that
the photo-assisted noise presents a more complex proﬁle, in particular for the two following
systems: 1) a two-dimensional electron gas in the fractional quantum Hall regime for which
we have obtained evenly spaced singularities in the noise derivative, with a spacing related
to the ﬁlling factor and, 2) a carbon nanotube for which a smoothed staircase in the noise
derivative is obtained.
1
Introduction
In mesoscopic systems, the measurement of shot noise makes it possible to probe the eﬀective
charges which ﬂow in conductors. This has been illustrated experimentally and theoretically
when the interaction between electrons is less important 1 or when it is more relevant 2,3.
Additional informations can be obtained through the photo-assisted noise when an AC bias is
superposed to the DC bias. Experimentally, photo-assisted noise has been measured in diﬀusive
wires, diﬀusive junctions and quantum point contacts4. For normal metals, the noise derivative
displays steps5 at integer values of the ratio ω0/ω, where ω is the AC frequency and ω0 is related
to the DC voltage. We naturally expect that this behavior is modiﬁed in Coulomb interacting
systems. The present work deals with two speciﬁc one-dimensional correlated systems: a Hall
bar in the fractional quantum Hall regime, for which charge transport occurs via two counter-
propagating chiral edges states, and a carbon nanotube to which electrons are injected from a
Scanning Tunneling Microscope (STM) tip.
2
Photo-assisted noise in the fractional quantum Hall regime
The ﬁrst system we consider is a two-dimensional electrons gas in the fractional quantum
Hall regime which is described by the Hamiltonian H = H0 + HB. The kinetic term H0 =
(¯hvF /4π) P
r=R,L
R ds∂sφr(t))2 describes the right and left moving chiral excitations along the
edge states (φR and φL are the bosonic ﬁelds), and HB = A(t)Ψ†
R(t)ΨL(t) + h.c. describes the
transfer of quasiparticles from one edge to the other. ΨR(L) = FR(L)ei√νφR(L)(t)/
√
2πa where
FR(L) is a Klein factor, a, the short-distance cutoﬀand ν, the ﬁlling factor which characterizes
the charge e∗= νe of the backscattered quasiparticles. The backscattering amplitude between
the edge states has a time dependence due to the applied voltage V (t) = V0 + V1 cos(ωt):
A(t) = Γ0ei νe
¯h
R
dtV (t) = Γ0eiω0t+i ω1
ω sin(ωt) = Γ0
+∞
X
p=−∞
Jp
ω1
ω

ei(ω0+pω)t ,
(1)


## Page 2


where ω0 ≡νeV0/¯h and ω1 ≡νeV1/¯h. We have made an expansion in term of an inﬁnite
sum of Bessel functions Jp of order p, which is a signature of photo-assisted processes 6.
The backscattering current noise correlator is expressed with the help of the Keldysh contour:
S(t, t′) = P
η=±1⟨TK{IB(tη)IB(t′−η) exp(−i
R
K dt1HB(t1))}⟩/2 where IB(t) = iνeA(t)Ψ†
R(t)ΨL(t)−
h.c. is the current operator.
We are interested in the Poissonian limit only, so in the weak
backscattering case, one collects the second order contribution in the tunnel amplitude A(t).
The main purpose of this work is to analyze the double Fourier transform of the noise
S(Ω1, Ω2) ∝
R dt
R dt′S(t, t′) exp(iΩ1t + iΩ2t′) when both frequencies Ω1 and Ω2 are set to zero.
At zero temperature, the shot noise exhibits divergences 7 at each integer value of the ratio
ω0/ω which are not physical since they appear in a range of frequencies where the perturbative
calculation turns out to be no more valid. At ﬁnite temperature, the photo-assisted noise reads:
S(0, 0)
=
(e∗)2Γ2
0
2π2a2Γ(2ν)
 a
vF
2ν 2π
β
2ν−1
×
+∞
X
p=−∞
J2
p
ω1
ω

cosh
(ω0 + pω)β
2
 Γ

ν + i(ω0 + pω)β
2π

2
,
(2)
where Γ is the Gamma function and β = 1/kBT.
−3
−2
−1
0
1
2
3
−2.5
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
2.5
ω0/ω
dS(0,0)/dω0
−4
−3
−2
−1
0
1
2
3
4
−8
−6
−4
−2
0
2
4
6
8
ω0/ω
dS(0,0)/dω0
Figure 1: Noise derivative in the fractional quantum Hall regime as a function of ω0/ω = νV0/¯hω for (left)
ν = 1 at temperatures: kBT/¯hω = 0.01 (solid line) and kBT/¯hω = 0.1 (dashed line) and for (right) ν = 1/3 at
temperatures: kBT/¯hω = 0.05 (solid line) and kBT/¯hω = 0.15 (dashed line). We take ω1/ω = eV1/¯hω = 3/2.
We have tested the validity of our result by setting ν = 1 which corresponds to a non-
interacting system. The derivative of the noise according to the bias voltage exhibits staircase
behavior as shown on Fig. 1 (left). Steps occur every time ω0 is an integer multiple of the AC
frequency. This is in complete agreement with the results obtained be Lesovik and Levitov for
a Fermi liquid5. For a non-integer value of the ﬁlling factor (ν = 1/3), the shot noise derivative
exhibits evenly spaced singularities as seen on Fig. 1 (right), which are reminiscent of the tun-
neling density of states singularities for Laughlin quasiparticles. The spacing is determined by
the quasiparticle charge νe and the ratio of the bias voltage with respect to the AC frequency.
Photo-assisted transport can thus be considered as a probe for eﬀective charges at such ﬁlling
factors, and could be used in the study of more complicated fractions of the quantum Hall eﬀect.
3
Photo-assisted noise in carbon nanotube
We consider the following setup: an STM tip close to a carbon nanotube connected to leads
at both extremities. A voltage applied between the STM and the nanotube allows electrons to
tunnel in the center region of the nanotube. As a result, charge excitations propagate along


## Page 3


the nanotube towards the right and left leads. This system is described by the Hamiltonian
H = HN + HSTM + HT. The nanotube is a non-chiral Luttinger liquid 8:
HN
=
1
2
X
jδ
+∞
Z
−∞
dx vjδ(x)
h
Kjδ(x)(∂xφjδ)2 + K−1
jδ (x)(∂xθjδ)2i
,
(3)
where x is the position along the nanotube, φjδ and θjδ are non-chiral bosonic ﬁelds and
Kjδ is the Coulomb interactions parameter for each charge/spin, total/relative sectors jδ ∈
{c+, c−, s+, s−}.
We take Kc−= Ks+ = Ks−= 1, and we assume that Kc+ depends on
position 9 as depicted on Fig. 2a. The velocities satisfy vjδ(x) = vF/Kjδ(x).
The electrons in the metallic STM tip are assumed to be non-interacting. For convenience,
the electron ﬁeld cσ in the STM tip can be described in terms of a semi-inﬁnite Luttinger liquid
with Coulomb interactions parameters all equal to one. The tunnel Hamiltonian between the
STM tip and the nanotube at position x = 0 is HT(t) = P
rασ Γ(t)Ψ†
rασ(0, t)cσ(t) + h.c. where
r corresponds to the branch index, α to the mode index and σ to the spin. The fermionic ﬁelds
for electrons in the nanotube and in the STM tip are respectively deﬁned by: Ψrασ(x, t) =
Frασ eikFrx+iqFαx+iϕrασ(x,t)/
√
2πa and cσ(t) = fσ ei ˜ϕσ(t)/
√
2πa where a is the ultraviolet cutoﬀ
of the Luttinger liquid model, Frασ and fσ are Klein factors, kF is the Fermi momentum and qF
is the momentum mismatch associated with the two modes α.
In the presence of a voltage modulation superimposed on the constant DC voltage, V (t) =
V0+V1 cos(ωt), the tunnel amplitude becomes Γ(t) = Γ P+∞
p=−∞Jp (ω1/ω) exp(i(ω0+pω)t), where
Jp the Bessel function on order p, ω0 ≡eV0/¯h and ω1 ≡eV1/¯h. The calculation of noise is thus
analogous to the one which applies to the fractional quantum Hall eﬀect, except that here only
electrons tunnel in the nanotube. We thus obtain 10:
S(0, 0) = 4Γ2e2
π2a2
+∞
X
p=−∞
J2
p
ω1
ω
 Z +∞
0
dτ cos((ω0 + pω)τ)

1 +
  vF τ
a
2 1+ν
2
×
cos

(1 + ν) arctan
  vF τ
a
 + 1
8
P∞
n=1
 bn
c+
Kc+ + (−bc+)nKc+

arctan

2avF τ
a2+(nLKc+)2−(vF τ)2

Q∞
n=1
a2+(nLKc+)2−(vF τ)2
a2+(nLKc+)2
2 +

2avF τ
a2+(nLKc+)2
2 1
16
 bn
c+
Kc+ +(−bc+)nKc+

,
(4)
where bc+ = (Kc+ −1)/(Kc+ + 1) is the reﬂexion coeﬃcient at the nanotube contacts
x = ±L/2 and ν = P
jδ(1/Kjδ + Kjδ)/8.
The “standard” way 5 to display the results for photo-assisted transport is to consider the
noise derivative as a function of voltage: in particular, this allows to compare the results with
the non-interacting case where the noise derivative exhibits a staircase variation. In Fig. 2b, we
plot the numerically computed noise derivative as a function of the ratio ω0/ω in the presence
of Coulomb interactions (Kc+ = 0.2).
For ωL/ω = 0.1 (full line), we are in the limit where the wave packet spatial extension
is smaller that the nanotube length.
In this regime (except for a small region close to the
origin) the vast majority of the voltage scale lies in the regime where ω0 > ωL.
The noise
derivative diﬀers from the single electron behavior, in the sense that the sharp steps and plateaus
expected in this case are absent. Instead, because of Coulomb interactions eﬀects, the noise
derivative is smoothed out, but there is a clear reminiscence of the step positions: the slope of
dS(x, x; Ω= 0)/dω0 increases abruptly at the location of the steps. We attribute the smoothing
to the tunneling density of states on the nanotube which is modiﬁed by the Coulomb interactions
in the nanotube. For ωL/ω = 1.2 (dashed line), we are in an intermediate regime for which
electron wave packets are comparable to the nanotube length. For ωL/ω = 6 (dashed-dotted


## Page 4


                                    


      

  

   
V
Nanotube
STM
Γ0
K    (x)
c+
x
L / 2 
−L / 2
1
0
a)
0
1
2
3
4
0
0.5
1
1.5
2
ω0 / ω
dS(x,x;0) / dω0
b )
ωL/ω = 0.1
ωL / ω = 1.2
ωL / ω = 6
Figure 2: a) Picture of the system and spatial variation of the Coulomb interactions parameter Kc+; b) Shot
noise derivative in the nanotube for Kc+ = 0.2, ω1/ω = 2, ωc/ω = 100 and several values of ωL/ω.
line), we are in the limit where electron wave packets are larger than the nanotube length, and
as a consequence, the ﬁnite size eﬀects dominate over the Coulomb interactions eﬀects and a
stepwise behavior in dS(x, x; Ω= 0)/dω0, which is typical of non-interacting metals, can be
identiﬁed.
4
Conclusion
Photo-assisted noise is aﬀected by Coulomb interactions in one-dimensional systems. In the
fractional quantum Hall eﬀect, the photo-assisted noise shows evenly spaced singularities with a
spacing related to the ﬁlling factor. As a consequence, photo-assisted noise measurement in such
a system could be used to extract fractional charge. In carbon nanotube, Coulomb interactions
aﬀect the height and shape of the steps in the diﬀerential noise when ωL/ω is small. On the
contrary, when ωL/ω ≥1, ﬁnite size eﬀects play an important role and attenuate the Coulomb
interactions eﬀects.
References
1. M. Reznikov et al., Phys. Rev. Lett. 75, 3340 (1995); A. Kumar et al., ibid. 76, 2778
(1996); G. B. Lesovik, JETP Lett. 70, 208 (1999); M. B¨uttiker, Phys. Rev. Lett. 65,
2901 (1990); M. B¨uttiker, Phys. Rev. B 45, 3807 (1992); C.W.J. Beenakker and H. van
Houten, ibid. 43, 12066 (1991); T. Martin and R. Landauer, ibid. 45, 1742 (1992).
2. C. L. Kane and M. P. A. Fisher, Phys. Rev. Lett. 72, 724 (1994); C. de C. Chamon et
al., Phys. Rev. B 51, 2363 (1995); P. Fendley et al., Phys. Rev. Lett. 75, 2196 (1995).
3. L. Saminadayar et al., Phys. Rev. Lett. 79, 2526 (1997); R. de-Picciotto et al., Nature
389, 162 (1997).
4. R. J. Schoelkopf et al., Phys. Rev. Lett. 80, 2437 (1998); A. A. Kozhevnikov et al., ibid.
84, 3398 (2000); L. H. Reydellet et al., ibid. 90, 176803 (2003).
5. G. B. Lesovik and L. S. Levitov, Phys. Rev. Lett. 72, 538 (1994).
6. M. Grifoni and P. H¨anggi, Phys. Rep. 304, 229 (1998) ; G. Platero and R. Aguado, ibid.
395, 1 (2004).
7. A. Cr´epieux, P. Devillard, and T. Martin, Phys. Rev. B 69, 205302 (2004).
8. R. Egger and A. Gogolin, Eur. Phys. J. B 3, 781 (1998).
9. I. Saﬁand H. J. Schulz, Phys. Rev. B 52, 17040 (1995); D. L. Maslov and M. Stone, ibid.
52, 5539 (1995); V. V. Ponomarenko, ibid. 52, R8666 (1995).
10. M. Guigou, A. Popoﬀ, T. Martin, and A. Cr´epieux, cond-mat/0611627.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]