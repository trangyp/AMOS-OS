---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.03683
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1910.03683_Schwinger-based_QCD_formulation_s_derivation_of_elastic_pp_scattering

> Source: 1910.03683_Schwinger-based_QCD_formulation_s_derivation_of_elastic_pp_scattering.pdf

> Pages: 6

---


## Page 1


SCHWINGER-BASED QCD FORMULATION’S DERIVATION OF ELASTIC
PP SCATTERING
H.M. Fried, Y.M.Sheu, P.H.Tsanga
Brown University, Department of Physics, RI, USA
Y. Gabellini, T.Grandou
Institut de Physique de Nice, UMR 7010 CNRS, Site Sophia 06560 Valbonne, France
Using previously described functional techniques for some non-perturbative, gauge invariant,
renormalized QCD processes, a simpliﬁed version of the amplitudes - in which forms akin
to Pomerons naturally appear - provides ﬁts to ISR and LHC-TOTEM pp elastic scattering
data. Those amplitudes rely on a speciﬁc function φ(b) which describes the ﬂuctuations of
the transverse position of quarks inside hadrons.
Presented at EDS Blois 2019
The 18th Conference on Elastic and Diﬀractive Scattering
Quy Nhon, Vietnam,
June 2328, 2019
1
Introduction
This talk is covers the work in
1. Beginning with Schwinger’s Generating Functional and the
QCD Lagrangian, applying two procedures that were overlooked in the last four decades, an
analytic, gauge-invariant correlation functions for Non-Perturbative QCD is obtained.
This
formulation produces the following results thus far:
• First-principled dynamical quark conﬁning potential for quarks 2,
• A potential obtained from QCD that allows nucleons to be bounded, thus provided the
ﬁrst-principled model deuteron 3,
• New property of Eﬀective Locality, provides gauge-invariant summation of all gluonic
exchanges between quarks; more over, the interaction becomes a local interaction. 4.
• Obtained Chiral Symmetry Breaking for dynamical quarks out of the new property of
Eﬀective Locality 5.
• Extended Asymptotic freedom as supported by other non-perturbative approaches: Dyson
Schwinger Equation 6.
• A qualitative description of the Hadron Conﬁnement mass scale(s) 7.
aspeaker
arXiv:1910.03683v1  [hep-ph]  8 Oct 2019


## Page 2


• The full SU(3) algebraic content of QCD amplitudes, both C2 and C3 casimir invariants
are preserved 8.
• First-principled calculation of elastic proton-proton scattering at ISR and LHC energies.
This will be the focus of this talk 1.
1.1
Schwinger Generating Functional
The Schwinger Generating Functional can be rewritten into gaussian operations on gaussian
ﬁelds.
ZQCD[¯η, η, j] = Ne−i
2
R
∂
∂A·D(0)
F · ∂
∂A · e
i
4
R
F2+ i
2
R
A·(−∂2)·A · ei
R
¯η·GF[A]·+L[A]|A=
R
D(0)
F ·j
(1)
where GF (x, y|A) = [m + γ · (δ −igAτ)]−1, and L[A] = ln[1 −iγAτ[0]].
The F2 can be linearized with Halpern’s half a century old expression:
e−i
4
R
F2 = N
Z
d[χ]e
i
4
R
χ2+ i
2
R
F·χ
(2)
where χa
µν = −χa
νµ is anti symmetric tensor. It is this added χ ﬁeld that plays the central role
in the summation of all gluons in the non-perturbative regime.
1.2
Gauge-Invariance
Schwinger’s Generating Functional now becomes
ZQCD[¯η, η, j] = N
Z
d[χ]e
i
4
R
χ2eD(0)
A · e
i
2
R
χ·F+ i
2
R
A·(−∂)·Aei
R
¯η·GF [A]·η+L[A]|A=
R
D(0)
F ·j
(3)
Calculating 2n-point Fermionic Green’s functions (e.g. n=2), gives
= N
Z
d[χ]e
i
4
R
χ2eD(0)
A e
i
2
R
A·(D(0)
F )−1·AGF (1|gA)GF (2|gA)eL[A]|A=0
(4)
eDaF1[A] = exp[ i
2
Z
¯Q·D(0)
F ·(1−¯K·D(0)
F )−1· ¯Q−1
2Tr ln(1−DF · ˜K]·exp[1
2
Z
A· ¯K·(1−D(0)
F · ¯K)−1·A]
(5)
where
D(0)
F ·(1−¯K ·D(0)
F )−1 = D(0)
F ·[1−ˆK +(D(0)
F )−1)·D(0)
F ]−1 = −( ˜Kab
µν +gfabcχc
µν)−1 = −ˆK−1 (6)
with F1[A] = e
i
2
R
A· ¯
K·A+i
R ¯Q·A, F2[A] = eL[A] and < z| ¯Kab
µν|z′ >= [ ˜Kab
µν(z)+gfabcχc
µν(z)]δ(4)(z −
z′)+ < z|(D(0)
F )−1|ab
µν|z′ >.
We then have
(7)
eDAF1[A]F2[A] = exp[−i
2
Z
¯Q · ˆK−1 · ¯Q] + 1
2Tr ln ˆK + 1
2Tr ln(−D(0)
F )]
· exp[ i
2
Z
∂
∂A · D(0)
F ·
∂
∂A′ ]
· exp[ i
2
Z
∂
∂A′ · ˆK−1 ·
∂
∂A′ −
Z
¯Q · ˆK−1 ·
∂
∂A′ ]
· (eDAF2[A′])


## Page 3


and
(8)
eDAF1[A]F2[A] = Nexp[−i
2
Z
¯Q · ˆK−1 · ¯Q + 1
2Tr ln ˆK]
· exp[ i
2
Z
∂
∂A · ˆK−1 · ∂
∂A −
Z
¯Q · ˆK−1 · ∂
∂A] · exp(L[A])|A→0
From above, all explicit gauge dependencies are cancelled. That is, Gauge Invariance is
explicitly preserved by means of Gauge Independence.
−ˆK−1 ≡(f · χ)−1 represents all gluonic exchanges between quarks, a Gluon Bundle, ie, all
gluonic exchanges summed in the non-perturbative regime.
In QCD, where conﬁnement and chiral symmetry breaking hold, the impact parameter, b
must ﬂuctuate 10 11. At this stage, we choose a ﬂuctuating b by a deformed gaussian (gaussian
resulted in zero potentials).
ϕ(b) = µ2
π
1 −ξ/2
Γ(
1
1−ξ/2)e−(µb)(2−ξ)
(9)
where 0 < ξ << 1
With this, non-perturbative QCD processes becomes processes of gluon bundles, (f · χ)−1’s
and closed quark loops, L[A]’s. With the introduction of a particular renormalization scheme
as described in 9, functional integrals of Halpern’s χ’s reduces to ordinary integrals, where dχ4
becomes space-time integrals of inﬁnitesimal sizes, giving δ functions joining with closed quark
loops, L[A]’s.
2
Comparing theory with experimental proton-proton elastic scattering diﬀeren-
tial cross section at ISR and LHC energies.
As shown in 1, 9, the choice for δ2ℓ= κ/ ¯m results explicit 0 for all graphs except Quark Loop
Chain graphs.
The non-perturbative QCD scattering amplitude can thus be calculated as
T(s, ⃗q) =
is
2M2
Z
d2bei⃗q·⃗b[1 −eiXpp(s,⃗b)]
(10)
Where Xpp is the Eikonal of the proton-proton process where eiXpp = eiX(GluonBundle)eiX(QuarkLoopChain)
T(s, ⃗q) =
is
2M2
Z
dbei⃗q·⃗b[1 −e
√
igδ2
qϕ(⃗b)/2eg2δ2
q(κ/ ¯m2)∆¯ϕ/4]
(11)
Expanding above we get for one gluon bundle plus one quark loop chain exchange:
(12)
T1(s, ⃗q) =
s
2M2
g
2( λ
m)2(m
E )2p[−1
√
2e−q2/4m2 + i( 1
√
2e−q2/4m2 + g
2κ q2
¯m2 e−q2/2 ¯m2)]
giving a diﬀerential cross section, (green dotted curve in ﬁgures)
(13)
dσ1
dt (s, q2) = K 27
4π
g2
4 (λ
4 )4(6m
√s)4p[1
2e−q2/2m2 + ( 1
√
2e−q2/4m2 + g
2κ q2
¯m2 e−q2/2 ¯m2)2]
And for one gluon bundle plus two gluon bundles plus one quark loop chain exchange:
(14)
T2(s, ⃗q) =
s
2M2
g
2( λ
m)2(m
E )2p[(−1
√
2e−q2/4m2
+ 1
2
g
2δ2
q
m2
2π e−q2/8m2) + i( 1
√
2e−q2/4m2 + g
2κ q2
¯m2 e−q2/2 ¯m2)]


## Page 4


Figure 1 – ISR = 23.5 GeV
Figure 2 – ISR = 30.7 GeV
Figure 3 – ISR = 44.7 GeV
Figure 4 – ISR = 52.8 GeV
Figure 5 – ISR = 62.5 GeV
Figure 6 – ISR energies for elastic proton-proton scattering. Green dotted line for one Gluon Bundle and one
Quark Loop Chain. Red solid line for One Gluon Bundle plus two Gluon Bundles and one Quark Loop Chain.


## Page 5


Figure 7 – LHC-TOTEM = 7.0 TeV
Figure 8 – LHC-TOTEM = 8.0 TeV
Figure 9 – LHC-TOTEM = 13.0 TeV
Figure 10 – LHC-TOTEM energies for elastic proton-proton scattering. Green dotted line for one Gluon Bundle
and one Quark Loop Chain. Red solid line for One Gluon Bundle plus two Gluon Bundles and one Quark Loop
Chain.


## Page 6


with diﬀerential cross section (red solid line in ﬁgures)
(15)
dσ2
dt (s, q2) = K 27
4π
g2
4 ( λ
m)4(6m
√s)4p[(1
2e−q2/2m2
−g
2
λ2
4π(6m
√s)2pe−q2/8m2)2 + ( 1
√
2e−q2/4m2 + g
2κ q2
¯m2 e−q2/2 ¯m2)2]
K is conversion factor from mb to GeV at 0.44mbGeV −2. For the ISR data, we obtained
parameters: g=7.0, p=0.13, λ = 0.5, κ = −6.810−4, m = 0.23GeV ≈1.5mπ, ¯m = 0.64GeV ≈
4.5mπ.
For the LHC TOTEM data, we obtained g = 7.0, p = 0.55, λ = 0.72, κ = −4.210−3,
m = 0.16GeV ≈mπ, ¯m = 0.41GeV ≈3mπ.
Acknowledgments
This work was made possible by a generous grant from the Julian Schwinger Foundation.
References
1. H.M.Fried, Y. Gabellini, T. Grandou, Y.M. Sheu, P.H. Tsang. arXiv:1904.11083
2. H.M.Fried et al. Ann. Phys. 327, 2666-2690 (2012) DOI: 10.1016/j.aop.2012.07.008
3. Fried et al.
Ann.
Phys.
338, 2013 Volume 338, November 2013, Pages 107-122.
DOI:10.1016/j.aop.2013.07.006
4. T. Grandou et al.
Ann.
Phys.
327 (2012), Mod.
Phys.
Lett.
A, Vol.32(2017);
arXiv:1706.02264
5. T. Grandou, P.H.Tsang, arXiv:1905:05666 . to be published
6. H.M.Fried,
T.Grandou,
Y.M.Sheu,
Annals
of
Physics
344,
78-96
(2014),
DOI:10.1016/j.aop.2014.02.015
7. H.M.Fried, P.H. Tsang arXiv:1502.04378.
8. T.Grandou, EPL (Europhysics Letters), Volume 107, Number 1.
Article 11001.
DOI:doi.org/10.1209/0295-5075/107/11001
9. H.M.Fried, Y.Gabellini, T.Grandou, Y.M.Sheu, P.H.Tsang., Annals of Physics Volume
359, August 2015, Pages 1-19. DOI: 10.1016/j.aop.2015.03.024
10. A.Casher(1979) Chiral symmetry breaking in quark conﬁning theories.
Phys Lett B
83:395398.
11. S.J.Brodsky,
R.Shrock.
Proc.
Nat.
Acad.
Sci.
108:45-50,2011.
DOI:
10.1073/pnas.1010113107

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1910_03683_schwinger_based_qcd_formulation_s_derivation_of_elastic_pp_scattering
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1910_03683_SCHWINGER_BASED_QCD_FORMULATION_S_DERIVATION_OF_ELASTIC_PP_SCATTERING.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
