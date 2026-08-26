---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1202.4219v2
source: arxiv
tags: [arxiv, fractal, knowledge, math, reference]
---
# 1202.4219v2_Turbulent_convection_model_in_the_overshooting_region__II__Theoretical_analysis

> Source: 1202.4219v2_Turbulent_convection_model_in_the_overshooting_region__II__Theoretical_analysis.pdf

> Pages: 32

---


## Page 1


arXiv:1202.4219v2  [astro-ph.SR]  21 Feb 2012
Turbulent convection model in the overshooting region: II. Theoretical
analysis
Q.S. Zhang1,2,3 and Y. Li1,2
zqs@ynao.ac.cn(QSZ); ly@ynao.ac.cn(YL)
Received
;
accepted
1National Astronomical Observatories/Yunnan Observatory, Chinese Academy of Sciences,
P.O. Box 110, Kunming 650011, China.
2Laboratory for the Structure and Evolution of Celestial Objects, CAS.
3Graduate School of Chinese Academy of Sciences, Beijing 100039, China.


## Page 2


– 2 –
ABSTRACT
Turbulent convection models are thought to be good tools to deal with the convec-
tive overshooting in the stellar interior. However, they are too complex to be applied
in calculations of stellar structure and evolution. In order to understand the physical
processes of the convective overshooting and to simplify the application of turbulent
convection models, a semi-analytic solution is necessary. We obtain the approximate
solution and asymptotic solution of the turbulent convection model in the overshoot-
ing region, and ﬁnd some important properties of the convective overshooting: I. The
overshooting region can be partitioned into three parts: a thin region just outside the
convective boundary with high efﬁciency of turbulent heat transfer, a power law dis-
sipation region of turbulent kinetic energy in the middle, and a thermal dissipation
area with rapidly decreasing turbulent kinetic energy. The decaying indices of the tur-
bulent correlations k, u′rT ′, and T ′T ′ are only determined by the parameters of the
TCM, and there is an equilibrium value of the anisotropic degree ω. II. The overshoot-
ing length of the turbulent heat ﬂux u′
rT ′ is about 1Hk(Hk = | dr
dlnk|). III. The value
of the turbulent kinetic energy at the convective boundary kC can be estimated by a
method called the maximum of diffusion. Turbulent correlations in the overshooting
region can be estimated by using kC and exponentially decreasing functions with the
decaying indices.
Subject headings: convection — diffusion — turbulence


## Page 3


– 3 –
1.
Introduction
Convective overshooting is an important physical process in the stellar structure and
evolution. Phenomenologically, the acceleration of a ﬂuid element is zero at the convective
boundary, but its speed is not zero. It is able to go across the convective boundary into
the dynamically stable zone. This phenomenon is called the convective overshooting. The
convective overshooting transports heat and matter, and affects the structure and evolution of
stars. A phenomenological theory of the overshooting was developed by Zahn(1991), which
predicts an adiabatic overshooting region. However, Xiong & Deng(2001) pointed out that
the turbulent velocity and the temperature are strongly correlated in Zahn’s theory. Recently,
Christensen-Dalsgaard et al.(2011) found that the convective overshooting only described by the
turbulent convection models could be in agreement with the helioseismic data.
The turbulent convection models (TCMs) are based on fully hydrodynamic moment
equations, and applied on investigating the convective overshooting(Xiong 1981, 1985,
1989; Xiong & Deng 2001; Canuto 1997; Canuto & Dubovikov 1998; Canuto 1998, 1999;
Marik & Petrovay 2002; Deng & Xiong 2006; Li & Yang 2007; Deng & Xiong 2008; Zhang & Li
2009). There are two main difﬁculties restricting the applications of the TCMs. One is to solve
the equations of the TCMs, which are highly non-linear and unstable in numerical calculations.
The other is to incorporate the TCMs into a stellar evolution code. In general, solving the TCMs
needs the parameters of the stellar structure(e.g. temperature T, density ρ, pressure P, radius
r, luminosity L, and elements abundance vector), and solving the equations of stellar structure
requires the temperature gradient ∇which is determined by the TCMs. Thus, in order to apply
the TCMs, one must solve both the TCMs and the equations of stellar structure, which shows
enormous difﬁculty. Although developing numerical technique is very important, getting an
approximate solution of the TCMs is more interesting because an approximate solution helps to
understand the physical processes and may signiﬁcantly simplify the application of the TCMs.


## Page 4


– 4 –
Xiong(1989) found the asymptotic solution of his TCM in the overshooting region, the turbulent
correlations being exponentially decreasing in the overshooting region. However, his solution of
the heat ﬂux u′rT ′ is not suitable near the convective boundary, and the initial turbulent kinetic
energy k0 is unknown so that the value of the turbulent correlations in the overshooting region
actually can not be determined without numerical calculations.
In this paper, we investigate the properties of the convective overshooting by analyzing Li &
Yang’s TCM(Li & Yang 2007), which was tested in the solar convection zone(Li & Yang 2007;
Yang & Li 2007). We try to get a semi-analytical solution of the TCM in the overshooting region.
We introduce the TCM in Section 2, investigate the properties of the overshooting in Section 3,
and summarize the conclusions in Section 4.
2.
Turbulent Convection Model
The closure assumptions of Li & Yang’s TCM are(Li & Yang 2001, 2007): the three-order
moment terms are modeled with a gradient-type scheme; the dissipation rate ε of the turbulent
kinetic energy k is assumed to be local; the dissipation rates of the turbulent heat ﬂux u′
rT ′
and the turbulent ﬂuctuation of temperature T ′T ′ are assumed to be determined by both the
reciprocal timescale of the turbulent dissipation τ −1
1
=
ε
k and the thermal dissipation one
τ −1
2
=
λ
ρcP
ε2
k3. According to those closure assumptions, fully hydrodynamic moment equations
on the quasi-steady approximation result in the complete equations of two-order moment
terms(Li & Yang 2007):
1
ρr2
∂
∂r

Csρr2k
εu′ru′r
∂u′
ru′
r
∂r

= 2
3ε + 2βgr
T
u′rT ′ + Ck
ε
k

u′ru′r −2
3k

(1)
1
ρr2
∂
∂r

Csρr2k
εu′
ru′
r
∂k
∂r

= ε + βgr
T u′
rT ′
(2)
2
ρr2
∂
∂r

Ct1ρr2k
εu′ru′r
∂u′rT ′
∂r

= −T
HP
(∇−∇ad)u′ru′r + βgr
T T ′T ′ + Ct
ε
k + λ
ρcP
ε2
k3

u′rT ′ (3)


## Page 5


– 5 –
1
ρr2
∂
∂r

Ce1ρr2k
εu′
ru′
r
∂T ′T ′
∂r

= −2T
HP
(∇−∇ad)u′
rT ′ + 2Ce
ε
k + λ
ρcP
ε2
k3

T ′T ′
(4)
The temperature gradient is calculated as:
∇= ∇R −HP
T
ρcP
λ u′rT ′
(5)
The meaning of those equations and each term in them were described in previous
works(Li & Yang 2007; Zhang & Li 2009) in detail. We simply introduce them here:
Equations (1-4) describe the equilibrium(time-independent) structure of the radial kinetic
energy u′ru′r, the turbulent kinetic energy k, the turbulent heat ﬂux u′rT ′ and the turbulent
ﬂuctuation of temperature T ′T ′, respectively. On the left side of those equations, there is the
non-local term(i.e. the diffusion term) of each turbulent correlation. On the right side, there are
the local terms which describe the generation and the dissipation of each turbulent correlation.
In Eq.(1) and (2), ε is the turbulent dissipation rate of k and ε = k
3
2
l where l = αHP, and the
second term on the right side is the generation rate of the kinetic energy due to the contribution of
the buoyancy. The last term in Eq.(1) is the return to isotropy term which attempts to make the
turbulent motion be isotropic. In Eq.(3), the ﬁrst two terms on the right side is the generation rate
of the turbulent heat ﬂux u′rT ′, and the last one is the dissipation rate that comprises the turbulent
dissipation and the thermal dissipation. In Eq.(4), the ﬁrst term on the right side is the generation
rate of the turbulent ﬂuctuation of temperature T ′T ′, and the last one is the dissipation rate.
Meanings of other symbols are: HP = −dr
dlnP is the local pressure scale height, β = −( ∂lnρ
∂lnT )P
the expansion coefﬁcient, gr = −GMr
r2
the radial component of gravity acceleration, ∇= dlnT
dlnP
the temperature gradient in the stellar interior, ∇ad = ( ∂lnT
∂lnP )S the adiabatic temperature gradient,
λ = 4acT 3
3κρ the thermal conduction coefﬁcient, cP = ( ∂H
∂T )P the speciﬁc heat, Ck the parameter of
the return to isotropy term, (Cs, Ct1, Ce1) the diffusion parameters and (α, Ct, Ce) the dissipation
parameters of turbulent variations(k, u′rT ′, T ′T ′).


## Page 6


– 6 –
In Eqs.(1-4), overbars are only used in three turbulent correlations u′
ru′
r, u′
rT ′ and T ′T ′. The
other variations(density ρ and the temperature T, etc.) are all mean state quantities which should
use overbars but we ignore them for convenience.
Equation (5) describes the energy transport in the stellar interior by both turbulent motions(i.e.
convection and overshooting) and radiation. ∇R is the radiative temperature gradient.
3.
Theoretical analysis of TCM in the overshooting region
In the previous work (Zhang & Li 2009), we applied the TCM in the solar overshooting
region and found some properties of the overshooting region: u′rT ′ < 0, ∇R < ∇< ∇ad, and
the peak of T ′T ′, which are similar to Xiong’s(1985) and Xiong & Deng’s(2001) works. In this
section, we attempt to get semi-analytical solutions of the TCM.
Some approximations are adopted to simplify Eqs.(1-5) in the overshooting region:
Approximation I. P´eclet number Pe ≫1, where Pe = ρCP l
√
k
λ
. That is ε
k ≫
λ
ρcP
ε2
k3 which
means the turbulent dissipation is much stronger than the thermal dissipation. This assumption is
reasonable in most cases except for the region near the surface of a star or with very small k.
Approximation II. All variations, except the turbulent ﬂuctuations, are thought to be constant
because the turbulent ﬂuctuations change much faster than others in the overshooting region.
Approximation III. Far away from the convective boundary, ∇≈∇R. This assumption is
acceptable if the heat ﬂux u′
rT ′ is small.


## Page 7


– 7 –
3.1.
Turbulent heat transport in the overshooting region
Deﬁning the anisotropic degree ω = u′ru′r
2k which is the ratio of radial kinetic energy to total
kinetic energy, and applying Approximation II and Eq.(5), we can rewrite Eq.(3) to:
∂
∂r

4Ct1ωl
√
k∂u′rT ′
∂r

= −T
HP
(∇R −∇ad)u′ru′r + βgr
T T ′T ′ + [2ωPe + Ct(1 + P −1
e )]
√
k
l u′rT ′ (6)
In the last bracket in Eq.(6), Approximation I(Pe ≫1) makes the dissipation term
Ct(1 + P −1
e )
√
k
l u′
rT ′ be ignorable. And, by using Eq.(5) and Approximation II, it is easy to ﬁnd
that the diffusion term is on the same order of the ignorable dissipation term:
∂
∂r

4Ct1ωl
√
k∂u′rT ′
∂r

≈2Ct1α2ω dlnk
dlnP · dln(∇R −∇)
dlnP
(
√
k
l u′rT ′) ∼Pe0(
√
k
l u′rT ′)
(7)
Therefore the diffusion term is also ignorable. Equation (3) is in local equilibrium:
−T
HP
(∇−∇ad)u′ru′r + βgr
T T ′T ′ ≈0
(8)
In the overshooting region, the most important process is the diffusion of the kinetic energy.
Thus, we ignore the diffusion of T ′T ′(i.e., setting Ce1 = 0). The solution of the TCM with
Ce1 = 0 can be thought as the zero-order solution of the TCM.
Ignoring the diffusion of T ′T ′ and the diffusion and dissipation terms of u′rT ′, using
Approximations I & II, one can rewrite Eqs.(1-4) as:
2Csl
k
∂
∂r(ωk
5
2 ∂ω
∂r ) = (Ck −1)(ω −1
3)k
3
2
l + βgr
T u′rT ′(1 −ω)
(9)
2Csl ∂
∂r(ωk
1
2 ∂k
∂r ) = k
3
2
l + βgr
T u′rT ′
(10)
0 = −2T
HP
(∇−∇ad)ωk + βgr
T T ′T ′
(11)


## Page 8


– 8 –
0 = −2T
HP
(∇−∇ad)u′
rT ′ + 2Ce
ε
kT ′T ′
(12)
Equation (9) results from Eq.(1) and (2), describing the equilibrium structure of the
anisotropic degree ω. The left side is the diffusion of ω. The ﬁrst term in the right side is the
dissipation rate due to return to isotropy term in Eq.(1). The last term is the generation rate of ω
due to the buoyancy.
Equations (11) and (12) show:
0 = (∇−∇ad)(u′rT ′ + 2Ceω T
βg
k
3
2
l )
(13)
The solution is u′rT ′ = −2Ceεω T
βg or ∇= ∇ad. The latter is equivalent to u′rT ′ =
−T
HP
λ
ρcP (∇ad −∇R). Because u′
rT ′ is close to zero near the convective boundary and gradually
decreases far away from the convective boundary(Xiong 1989; Xiong & Deng 2001; Zhang & Li
2009), the physically acceptable result is:
u′
rT ′ = Max{−T
HP
λ
ρcP
(∇ad −∇R), −2Ceω T
βg
k
3
2
l }
(14)
Equation (14) shows that there is an adiabatic stratiﬁcation zone in the overshooting region
in the case of Ce1 = 0. In order to investigate the property of heat transport in the overshooting
region, we must know the length of the adiabatic stratiﬁcation zone. It is found in Eq.(14) that the
boundary of the adiabatic stratiﬁcation is the location where
T
HP
λ
ρcP (∇ad −∇R) = 2Ceω T
βg
k
3
2
l .
Solving the equation of ω is not easy because it is nonlinear. However, this problem is avoidable.
Turbulent motions are isotropic when ω = 1
3. In the convection zone, ω > 1
3 because the buoyancy
boosts radial turbulent motion. In most part of overshooting region, ω should be less than 1
3
because the buoyancy prevents radial turbulent motion. Therefore ω should be not far away from
1
3 near the convective boundary. Further more, taking ω as a constant, one can rewrite Eq.(10) as:
2Cslω ∂
∂r(k
1
2 ∂k
∂r ) = k
3
2
l + βgr
T u′
rT ′
(15)


## Page 9


– 9 –
Substituting Eq.(14) into the above equation, one can get the approximate solution:
k
3
2 ≈k
3
2
Cexp(−
r
3
4Csω|r −rC
l
|)
(16)
if
T
HP
λ
ρcP (∇ad −∇R) ≤2Ceω T
βg
k
3
2
l , and:
k
3
2 = k
3
2
Aexp(−
s
3(1 + 2Ceω)
4Csω
|r −rA
l
|)
(17)
if
T
HP
λ
ρcP (∇ad −∇R) > 2Ceω T
βg
k
3
2
l .
In Eq.(16), point C, which is the convective boundary where ∇ad = ∇R, is set to be the initial
point, kC and rC being k and r here. The contribution of the buoyancy term(i.e. the last term
in Eq.(15)) is ignored in obtaining the solution Eq.(16). In the deep convection zone, turbulent
motions are almost in local equilibrium, thus the ratio of −βgr
T u′rT ′ to k
3
2
l is about 1. However,
near the convective boundary, buoyancy is about zero, meanwhile the diffusion of k dominates.
Those make the ratio be much less than 1. Therefore the buoyancy term is ignorable.
In Eq.(17), point A, where k = kA and r = rA, is the boundary of the adiabatic overshooting
region. In the region beyond point A, the ratio of −βgr
T u′rT ′ to k
3
2
l is 2Ceω which is on the order of
1, thus the buoyancy term remains.
The exponentially decreasing function of k is due to the fact that there is no generation in the
overshooting region. Contrary to the situation in the convection zone, the buoyancy dissipates k
because it prevents the radial motion of ﬂuid elements in the overshooting region. The distribution
of k results from the equilibrium between the diffusion and the dissipation. k should decrease
faster if the buoyancy is as effective as the turbulent dissipation, which is found by comparing the
exponential indices of Eq.(16) and (17).
The location of point A is determined by
T
HP
λ
ρcP (∇ad −∇R) = 2Ceω T
βg
k
3
2
l . Using Eq.(16),
we get a property of point A:
k
3
2
Cexp(−
r
3
4Csω|rA −rC
l
|) =
1
2Ceω
αβgλ
ρcP
(∇ad −∇R,A)
(18)


## Page 10


– 10 –
The relation between rA and ∇R,A is needed in order to solve this equation and to locate
point A. Near the convective boundary, there is:
|∇ad −∇R,A| ≈∇ad|χ(lnPA −lnPC)| = ∇ad|χ| lad
HP
(19)
where lad = |rA −rC| is the length of the adiabatic overshooting region, PA and PC the pressure
at point A and C, and χ = dln∇R
dlnP which is approximately a constant.
Substituting Eq.(19) into Eq.(18), one ﬁnds:
k
3
2
Cexp(−1
α
r
3
4Csω
lad
HP
) =
1
2Ceω
αβgλ
ρcP
∇ad|χ| lad
HP
(20)
lad can be worked out if kC is known. In the deep adiabatic convection zone, turbulent
diffusion is ignorable, and the localized TCM shows k
3
2
Local = αβgλ(∇R−∇ad)
ρcP
(see Appendix A).
However, kC can not be estimated as that because ∇R = ∇ad thus kLocal = 0 at the convective
boundary. Actually, the turbulent diffusion of k is effective near the convective boundary, and kC
is determined by the diffusion. We can estimate kC by a simple approach which will be referred to
as the maximum of diffusion hereafter. Setting point B at where the diffusion becomes dominative
in the convection zone, we get the relation between kC and kB by solving Eq.(15):
k
3
2
C = k
3
2
Bexp(−
r
3
4Csω|rC −rB
l
|)
(21)
where k
3
2
B ≈αβgλ(∇R,B−∇ad)
ρcP
. Equation (21) shows that kC is a function of rB. In reality, the
diffusion leads to the maximum of kC. Therefore rB makes the derivation of the right side of
Equation (21) be zero. Noting that ∇R,B −∇ad is approximately proportional to rB −rC, one can
easily work out the location of point B:
r
3
4Csω|rC −rB
l
| ≈1
(22)
It is found in Fig.1 that k ≈kLocal in the deep convection zone because the turbulent diffusion
can be ignored here, and the turbulent diffusion dominates in the layer beyond point B.


## Page 11


– 11 –
Using above results, we obtain:
k
3
2
C = 1
e
αβgλ(∇R,B −∇ad)
ρcP
≈1
e
r
4Csω
3
α2βgλ∇ad|χ|
ρcP
(23)
Generally, lad
HP is very small. According to Eq.(20), the length of the adiabatic overshooting
region is:
lad ≈
q
4Csω
3
e
2Ceω + 1l
(24)
In the area |r −rC| ≤|rA −rC| in the overshooting region, the temperature gradient ∇is
almost equal to the adiabatic one. In the area |r −rC| > |rA −rC|, however, according to Eq.(14),
Eq.(17), and Eq.(5), the temperature gradient ∇is gradually close to ∇R:
∇−∇R = (∇ad −∇R,A) · exp[−
s
3(1 + 2Ceω)
4Csω
|r −rA
l
|]
(25)
Although ω in Eq.(24) and Eq.(25) is still unknown, we can estimate it roughly. Equation
(24) and (25) describe the turbulent motion near the convective boundary, thus we can use ω ≈ωC
where ωC is ω at the convective boundary. In the deep convection zone, ω is almost equal to the
equilibrium value ωcz =
2
3Ck + 1
3 which is derived from the localized TCM (see Appendix A).
ωC < ωcz because the buoyancy is zero at the boundary, and ωC > 1
3 because the diffusion of ω.
Therefore the typical value of ωC can be taken as the average, i.e. ωC ≈1
2(ωcz + 1
3). If Eq.(25) is
used in the region far away from the convective boundary(beyond the peak of T ′T ′), ω ≈ωC is
not appropriate. One can use ω = ωo, where ωo is the equilibrium value of ω in the overshooting
region which is introduced in the next subsection.
Another turbulent correlation is T ′T ′, which can be worked out by using Eq.(11):
T ′T ′ ≈0, (|r −rC| ≤|rA −rC|)
(26)
And:
T ′T ′ = 2T
HP
T
βg(∇ad −∇)ωk, (|r −rC| > |rA −rC|)
(27)


## Page 12


– 12 –
Equation (26) seems to against Cauchy’s theorem u′
ru′
rT ′T ′ ≥u′
rT ′2. Actually, T ′T ′ ≈0 is
only an approximate solution on the order of (Pe1
√
k
l u′rT ′), because Eq.(8) is an approximation on
that order. Numerical calculations show no conﬂiction.
Results obtained above are based on Ce1 = 0. Numerical results of ∇with both Ce1 = 0 and
Ce1 ̸= 0 are shown in Fig.2. It is found that the effects of the diffusion of T ′T ′ are only making
∇be smoother. However, there is no adiabatic overshooting region when the diffusion of T ′T ′
is present, because T ′T ′ increases near the convective boundary due to the turbulent diffusion
thus ∇decreases according to Eq.(8). Numerical results of the turbulent correlations in both
Ce1 = 0 and Ce1 ̸= 0 with different TCM parameters and for different stellar models are shown
in Figs.3-5. It is found that the theoretical solutions well ﬁt the numerical solutions in the case of
Ce1 = 0. This also validates that the boundary value kC derived from the maximum of diffusion
is a good approximation. The diffusion of T ′T ′ modiﬁes and smoothes the proﬁle of T ′T ′ and
u′rT ′. However, k is insensitive to the diffusion of T ′T ′ because that k is mainly dominated by the
diffusion of itself. The diffusion of T ′T ′ doesn’t signiﬁcantly change the integral value of T ′T ′.
According to Eq.(8), the integral value of ∇or u′
rT ′ is also insensitive to the diffusion of T ′T ′,
which is found in Figs.(2-5).
The distribution of T ′T ′ reveals an important property of the overshooting. In the
nonadiabatic overshooting region, using ∇≈∇R, one ﬁnds that T ′T ′ ∝T(∇ad −∇R)k
according to Eq.(27). This result indicates a maximum of T ′T ′(Xiong 1985; Zhang & Li 2009)
which is shown in Figs.3-5. Beyond the location of the maximum of T ′T ′, the temperature of a
turbulent element is gradually close to the temperature of the environment, and the efﬁciency of
heat transport signiﬁcantly decreases. Therefore the area between the convective boundary and
the location of the maximum of T ′T ′ can be thought as the overshooting region of u′
rT ′. It is
found in Figs.3-5 that the width of the valley of u′rT ′ is approximately equal to the distance from
the convective boundary to the location of the maximum of T ′T ′. In order to get the overshooting


## Page 13


– 13 –
length of heat transport, we need to locate the maximum of T ′T ′.
Using Eq.(17), deﬁning θ0 = dlnk
dlnP = ± 1
α
q
(1+2Ceω)
3Csω
as the decaying index of k (in the case
of Ce1 = 0), we get:
T ′T ′ ∝T(∇ad −∇R)P θ0
(28)
The derivative of T ′T ′ is zero at the peak of T ′T ′. We get ∇R there(denoted as ∇∗
R):
(∇∗
R + θ0)(∇ad −∇∗
R) −χ∇∗
R ≈0
(29)
∇∗
R is determined by only one turbulent parameter θ0.
The typical overshooting length of u′rT ′ (or ∇) can be estimated with ∇∗
R:
|χ| = |dln∇R
dlnP | ≈|ln∇R,C −ln∇∗
R
lnPC −lnP ∗| = |ln∇ad −ln∇∗
R
lnPC −lnP ∗| =
ln∇ad
∇∗
R
l∇
HP
(30)
where ∇R,C is ∇R at the convective boundary, l∇is the distance from the convective boundary to
the location of the maximum of T ′T ′ and also the typical overshooting length of ∇.
l∇is worked out as:
l∇≈1
|χ|ln∇ad
∇∗
R
HP
(31)
Usually, |θ0| is much larger than |χ| and ∇ad, and ∇∗
R can be approximately solved from
Eq.(29):
∇∗
R ≈(1 −χ
θ0
)∇ad
(32)
Finally, we ﬁnd:
l∇≈HP
|θ0| = Hk
(33)


## Page 14


– 14 –
where Hk is the scale height of turbulent kinetic energy k deﬁned by Hk = | dr
dlnk|. The result
indicates that ∇is remarkably modiﬁed by the overshooting only in about 1Hk. It is found in
Fig.3 that l∇= lnkC
k∗Hk ≈0.8Hk, which is in agreement with Eq.(33). It is shown in Fig.2 that ∇
is remarkably modiﬁed only in 1Hk.
3.2.
Asymptotic analysis
In above subsection, we have discussed the turbulent heat transport and the solution of
turbulent correlations in the overshooting region near the convective boundary based on the
assumption Ce1 = 0. The diffusion of T ′T ′ only modiﬁes turbulent correlations to be smoother
near the convective boundary. However, it makes more effects on turbulent motions in the
overshooting region further than 1Hk away from the convective boundary. In this subsection, we
investigate the turbulence properties in the outer overshooting region(beyond 1Hk).
In the numerical calculations of the TCM, we found that the anisotropic degree ω always
showed an equilibrium value in the overshooting region. A typical numerical result is shown
in Fig.6. In order to understand it, we discuss the behave of the anisotropic degree ω in both
convection zone and overshooting region. ω should be larger than 1
3 in the convection zone
because the buoyancy boosts radial movement of turbulent elements. Actually, ω is almost equal
to the equilibrium value in the convection zone ωcz =
2
3Ck + 1
3(see Appendix A) due to the
equilibrium between the buoyancy and the return to isotropy term. When turbulent elements go
across the convective boundary into the overshooting region, the buoyancy prevents convective
elements moving, thus ω decreases to less than 1
3 near the convective boundary. However, as u′rT ′
exponentially decreasing, the equilibrium of ω is established again in the overshooting region.
This results in an asymptotic property of the overshooting region: there is an equilibrium value of
ω in the overshooting region, ω ≈ωo.


## Page 15


– 15 –
By using the asymptotic property ω ≈ωo and Approximations I, II & III, it is easy to get the
asymptotic solution of TCM in the overshooting region(see Appendix B):
u′
rT ′ = (Ck −1)(ωo −1
3)
(1 −ωo)
T
βg
k
3
2
l
(34)
T ′T ′ = 2ωo(∇ad −∇R)
T 2
βgHP
k
(35)
k = k0( P
P0
)θ
(36)
where θ is the asymptotic solution of dlnk
dlnP :
θ = ± 1
α
s
1
3Csωo
[1 −(Ck −1)(ωo −1
3)
(1 −ωo)
]
(37)
k takes the decreasing expression in the overshooting region, which means: ′+′ is adopted in the
upward overshooting region and ′−′ in the downward one.
The equilibrium value ωo is determined by:
(2CsCe −Ce1Ck)ωo
2 + [1
3Ce1(Ck + 2) −Cs(Ck + 2Ce −1)]ωo + 1
3Cs(Ck −1) = 0
(38)
The equilibrium value ωo is only a function of turbulent parameters (Ce, Ce1, Cs, Ck). The
fact that the buoyancy prevents the radial movement of turbulent elements in the overshooting
region restricts the turbulent parameters to ensure ωo < 1
3.
An important thing is where ω reaches its equilibrium value ωo. According to Eq.(9), the
equilibrium of ω can be realized only if the buoyancy term synchronically decreases with k
decreasing. Therefore ω starts to reach its equilibrium value ωo beyond the peak of T ′T ′ due to
|u′
rT ′| being decreasing.
Setting Ce1 = 0 in Eq.(38), we ﬁnd that the asymptotic solution is the same as the results
in the overshooting region with |r −rC| ≥|rA −rC| by setting ω = ωo in Eq(14),(17) & (27).


## Page 16


– 16 –
Because Eq.(8) is correct whether Ce1 = 0 or not, the conclusion that the maximum of T ′T ′ is
located at about 1Hk is also correct in both cases.
It must be mentioned that we have used Approximation I(i.e. Pe ≫1), which means that the
turbulent dissipation is much larger than the thermal dissipation. If k decreases enough to satisfy
Pe ≪1, the thermal dissipation should become signiﬁcant thus T ′T ′ and the turbulent kinetic
energy k should rapidly decrease to zero. Then ω also rapidly decreases as shown in Fig.6. In
another word, turbulent movement can hardly overshoot into the thermal dissipation zone where
Pe ≪1.
According to discussions above, we can separate the overshooting region into three parts as
shown in Fig.7: the overshooting region of u′rT ′ or ∇with the length of about 1Hk, the turbulent
dissipation region in which the asymptotic solution holds, and the thermal dissipation region in
which the turbulent movement quickly vanishes. The boundaries among those parts are the peak
of T ′T ′ and the location of Pe = 1.
4.
Conclusions and discussions
Turbulent convection models are better tools in dealing with the convective overshooting
than non-local mixing length theories. However, they are often too complex to be applied in
the calculations of stellar structure and evolution. In order to investigate the property of the
convective overshooting and to make it easy to apply turbulent convection models, we have
analyzed the TCM developed by Li & Yang (Li & Yang 2007) and obtained approximate and
asymptotic solutions of the TCM in the overshooting region with Pe ≫1. The main conclusions
and corresponding discussions are listed as follows:
1. The overshooting region can be partitioned into three parts: a thin turbulent heat
ﬂux overshooting region, a power law dissipation region of turbulent kinetic energy, and a


## Page 17


– 17 –
thermal dissipation area with rapidly decreasing k. The turbulent ﬂuctuations k, u′
rT ′, and T ′T ′
exponentially decrease in the overshooting region as Eqs.(34-36). The equilibrium value of the
anisotropic degree ωo and the exponential indices of the turbulent ﬂuctuations are only determined
by the parameters of the TCM. The decaying behaviors of the turbulent ﬂuctuations are similar to
Xiong & Deng’s results(Xiong 1989; Xiong & Deng 2001).
2. The peak of T ′T ′ in the overshooting region is located at about 1Hk away from the
convective boundary. In this distance, the modiﬁcation of ∇caused by the overshooting is
remarkable. An approximate proﬁle of ∇comprises an adiabatic overshooting region with the
length of lad and an exponentially decreasing function, as described in Eq.(24) and (25). Beyond
1Hk, the modiﬁcation of ∇is ignorable and ∇≈∇R. It should be noted that the result of 1Hk
overshooting distance of turbulent heat transfer is independent of the parameters of TCM, so it
may be a general property of the overshooting. Our result is similar to Marik & Petrovay(2002)
whose result shows that the length between the peak of T ′T ′ and the convective boundary is about
1.2Hk. Meakin & Arnett(2010) simulated the turbulent convection of a 23M⊙star, the data of the
turbulent kinetic energy and the convective ﬂux in the overshooting region being shown in Fig.8.
It is found that the overshooting length of the convective ﬂux u′rT ′ is about 0.5 ∼2Hk which is in
agreement with our result.
3. The value of the turbulent kinetic energy at the convective boundary kC can be estimated
by a method called the maximum of diffusion. The value of turbulent ﬂuctuations in the
overshooting region can be estimated by using the exponentially decreasing functions and the
initial value kC. This may signiﬁcantly simplify the application of the TCM in calculations of the
stellar structure and evolution.
There is a distinction between the non-local model of Zahn(1991) and our results, i.e. the
temperature gradient jumps from nearly adiabatic to radiative in Zahn’s model but continuously
changes in our results (see Fig.2). This is caused by the assumption in Zahn’s model that the


## Page 18


– 18 –
turbulent velocity and temperature ﬂuctuation are strongly correlated(Xiong & Deng 2001). In
our results, the correlativity of turbulent velocity and temperature ﬂuctuation RV T =
u′rT ′
√
2ωkT ′T ′
quickly decreases to zero then turns to be negative near the convective boundary(see Fig.9),
and the asymptotic solution shows that RV T ∝
√
k and exponentially decreases in the turbulent
dissipation overshooting region. Our result is in agreement with three-dimension simulations such
as Fig.6 in Singh et al.(1995) and Fig.15 in Meakin & Arnett(2007).
We thank the anonymous referee for valuable comments which help to improve the paper.
And we thank C. A. Meakin for providing the numerical data of Fig.8. Fruitful discussions with
J. Su, X. J. Lai and C. Y. Ding are highly appreciated. This work is co-sponsored by the National
Natural Science Foundation of China through grant No.10673030 and No.10973035 and Science
Foundation of Yunnan Observatory No.Y0ZX011009.
A.
The localized TCM in convection zone.
The localized TCM results from Eqs.(1-4) by ignoring the diffusion terms. It is a good
approximate of the TCM in the convection zone(Li & Yang 2001). We attempt to work out the
solution in this appendix.
Some symbols are deﬁned for conveniences: U = u′rT ′, V = T ′T ′, W =
√
k,
A =
T
HP (∇R −∇ad), B = −βgr
T , D =
λ
ρCP , f =
∇−∇ad
∇R−∇ad.
Ignoring the diffusion terms of Eqs.(1-4), we get the localized TCM:
0 = 2
3
W 3
l
−2BU + 2Ck(ω −1
3)W 3
l
(A1)
0 = W 3
l
−BU
(A2)
0 = −2ωfAW 2 −BV + Ct(1 + P −1
e )WU
l
(A3)


## Page 19


– 19 –
0 = −2fAU + 2Ce(1 + P −1
e )WV
l
(A4)
U = AD(1 −f)
(A5)
Equation (A1) and (A2) show:
ω =
2
3Ck
+ 1
3
(A6)
This is the equilibrium value ωcz in convection zone.
Describing W, V , U by f and Pe(= lW
D ), we ﬁnd:
f =
CtCeP −1
e (1 + P −1
e )2
CtCeP −1
e (1 + P −1
e )2 + 2Ceω(1 + P −1
e ) + 1
(A7)
W, V can be worked out as:
W 3 = ABDl(1 −f)
(A8)
V =
AfW 2
CeB(1 + P −1
e )
(A9)
According to Pe = lW
D , Eq.(A8) and Eq.(A7), we get the equation of Pe:
aP 4
e + (b + 1)P 3
e + 2bP 2
e + (b −at)Pe −t = 0
(A10)
where a = 1 +
1
2ωCe, b = Ct
2ω, t = ABl4
D2 . f is determined by f = 1 −P 3
e
t according to Eq.(A8).
Solving Eq.(A10), we can obtain all turbulent ﬂuctuations of the localized TCM by using
Eq.(A5), (A8), (A9) and (A11).
An important case is t ≫1, thus Pe ≫1 according to Eq.(A10). In that case, Eq.(A7) shows:
f = CeCtP −1
e
2Ceω + 1 ≈0
(A11)


## Page 20


– 20 –
which corresponds to the adiabatic convection.
Finally, we obtain the turbulent ﬂuctuations according to Eq.(A8), (A5) & (A9):
W 3 ≈ABDl
(A12)
V ≈
Ct
2Ceω + 1
AD
Bl W
(A13)
U ≈AD
(A14)
and the correlativity of turbulent velocity and temperature RV T:
RV T =
U
√
2ωW 2V
≈
r
2Ceω + 1
2Ctω
(A15)
B.
Details of deriving the asymptotic solution of the TCM in overshooting region.
There are the details of obtaining the asymptotic solution of the TCM in overshooting region.
Some symbols are deﬁned for conveniences: U = u′rT ′, V = T ′T ′, W =
√
k,
A = −T
HP (∇−∇ad) ≈−T
HP (∇R −∇ad) (Approximation III is used), B = −βgr
T .
Applying the asymptotic property ω = ωo and Approximations I, II & III, one can rewrite
TCM as:
0 = (Ck −1)(ωo −1
3)W 3
l
−BU(1 −ωo)
(B1)
lCsωo
∂
∂r(W ∂W 2
∂r ) = W 3
l
−BU
(B2)
0 = −BV + 2AωoW 2
(B3)
lCe1ωo
∂
∂r(W ∂V
∂r ) = AU + Ce
l WV
(B4)


## Page 21


– 21 –
Equation (B1) is equivalent to:
U = (Ck −1)(ωo −1
3)
(1 −ωo)
W 3
Bl
(B5)
Taking it into Eq.(B2), one gets the equation of W:
∂2W 3
∂r2
=
3
4Csωol2[1 −(Ck −1)(ωo −1
3)
(1 −ωo)
]W 3
(B6)
Equation (B3) is equivalent to:
V = 2Aωo
B
W 2
(B7)
According to Eq.(B4), (B5) and (B7), one gets another equation of W:
∂2W 3
∂r2
=
3
4Ce1ωo2l2[(Ck −1)(ωo −1
3)
(1 −ωo)
+ 2Ceωo]W 3
(B8)
Comparing Eq.(B6) with Eq.(B8), one ﬁnds:
3
4Ce1ωo2l2[(Ck −1)(ωo −1
3)
(1 −ωo)
+ 2Ceωo] =
3
4Csωol2[1 −(Ck −1)(ωo −1
3)
(1 −ωo)
]
(B9)
Therefore the equation of ωo is:
(2CsCe −Ce1Ck)ωo
2 + [1
3Ce1(Ck + 2) −Cs(Ck + 2Ce −1)]ωo + 1
3Cs(Ck −1) = 0
(B10)
The asymptotic solution of W is derived from Eq.(B6):
W = W0exp{± 1
2α
s
1
3Csωo
[1 −(Ck −1)(ωo −1
3)
(1 −ωo)
]ln( P
P0
)}
(B11)
W takes the decreasing expression in the overshooting region: ′+′ is adopted in the upward
overshooting region and ′−′ in the downward one.


## Page 22


– 22 –
REFERENCES
Canuto V. M., 1997, ApJ, 489, L71
Canuto V. M., & Dubovikov M., 1998, ApJ, 493, 834
Canuto V. M., 1998, ApJ, 508, 767
Canuto V. M., 1999, ApJ, 524, 311
Christensen-Dalsgaard, J., Monteiro, M.J.P.F.G., Rempel, M., & Thompson, M.J., 2011, MNRAS,
414, 1158
Deng L., & Xiong D. R., 2006, ApJ, 643, 426
Deng L., & Xiong D. R., 2008, MNRAS, 386, 1979
Li Y.,& Yang J. Y., 2001, ChJAA, 1, 66
Li Y.,& Yang J. Y., 2007, MNRAS, 375, 388
Marik D.,& Petrovay K., 2002, A&A, 396, 1011
Meakin C. A. & Arnett D., 2007, ApJ, 667, 448
Meakin C. A.,& Arnett W. D., 2010, ApSS, 328, 221
Singh H. P., Roxburgh I. W., Chen K. L., 1995, A&A, 295, 703
Xiong D. R., 1981, Sci. Sinica, 24, 1406
Xiong D. R., 1985, A&A, 150, 133
Xiong D. R., 1989, A&A, 213, 176
Xiong D. R.,& Deng L., 2001, MNRAS, 327, 1137


## Page 23


– 23 –
Yang J. Y.,& Li Y., 2007, MNRAS, 375, 403
Zahn J. P., 1991, A&A, 252, 179
Zhang Q. S., & Li Y., 2009, RAA, 9, 585
This manuscript was prepared with the AAS LATEX macros v5.2.


## Page 24


– 24 –
31.0
31.2
31.4
31.6
31.8
32.0
0
1000
2000
3000
4000
5000
6000
 
 
 
W
Local
lnP
W
Convection zone
Convective
  boundary
       (C)
B
Fig. 1.— Numerical results of W =
√
k, and WLocal ≈
3q
αβgλ(∇R−∇ad)
ρcP
which is the solution
of localized TCM (See Appendix A), for the solar model at present age. TCM parameters are:
α = 0.84, Ck = 2.5, Cs = 0.1, Ce1 = 0, Ce = 0.2, Ct = 7.0, and Ct1 = 0.01, but Ct, Ct1 and Ce1
are insensitive to the results. Point C is the boundary of the convection zone, the location of point
B is calculated by using Eq.(22).


## Page 25


– 25 –
31.5
31.6
31.7
31.8
31.9
32.0
0.25
0.30
0.35
0.40
0.45
 
 
 
lnP
 
0
 
T
 
1
 
ad
 
R
Convective
 boundary
Convection zone
A
Fig. 2.— Numerical results of temperature gradient near the convective boundary in both Ce1 = 0
and Ce1 ̸= 0, ∇0 being the temperature gradient of the model with Ce1 = 0, and ∇1 corresponding
to Ce1 = 0.01. Dotted line ∇T, which is almost identical to ∇0, is theoretical solution of the
temperature gradient with Ce1 = 0. The stellar model and other TCM parameters are the same as
Fig.1. Point A is the boundary of the adiabatic overshooting region. Our theoretical result shows
lad ≈0.013HP in those TCM parameters set, the numerical calculation being 0.015HP.


## Page 26


– 26 –
31.6
31.7
31.8
31.9
32.0
-2000
0
2000
4000
6000
 
 
 
lnP
Convective boundary
Convection zone
V
W
U
30
Fig. 3.— Numerical results of T ′T ′, u′rT ′, k near the convective boundary in both Ce1 = 0 and
Ce1 ̸= 0, where U = u′
rT ′, W =
√
k, V = T ′T ′. Dashed lines correspond to Ce1 = 0, solid lines
to Ce1 = 0.01. Dotted lines are the theoretical solutions with Ce1 = 0. The stellar model and other
TCM parameters are the same as Fig.1.


## Page 27


– 27 –
22.40
22.45
22.50
22.55
22.60
22.65
22.70
-400000
-200000
0
200000
400000
 
 
 
U
V
3
lnP
W
6
Convective boundary
Convection
 zone
Fig. 4.— Numerical results of T ′T ′, u′rT ′, k near the convective boundary in both Ce1 = 0 and
Ce1 ̸= 0, where U = u′
rT ′, W =
√
k, V = T ′T ′. Dashed lines correspond to Ce1 = 0, solid lines
to Ce1 = 0.01. Dotted lines are the theoretical solutions with Ce1 = 0. The stellar model is a 7M⊙
star model at the top of RGB phase. Others TCM parameters are: α = 1.0, Ck = 2.2, Cs = 0.1,
Ce = 1.0, and Ct = 4.0, Ct1 = 0.01.


## Page 28


– 28 –
37.2
37.3
37.4
37.5
37.6
37.7
-4000
-2000
0
2000
4000
6000
8000
 
 
 
V/6
W
lnP
U
10
Convective boundary
Convection
     core
Fig. 5.— Numerical results of T ′T ′, u′rT ′, k near the boundary of the convective core in both
Ce1 = 0 and Ce1 ̸= 0, where U = u′
rT ′, W =
√
k, V = T ′T ′. Dashed lines correspond to
Ce1 = 0, solid lines to Ce1 = 0.01. Dotted lines are the theoretical solutions with Ce1 = 0.
The stellar model is an early main sequence model of a 3M⊙star. Others TCM parameters are:
α = 1.0, Ck = 2.1, Cs = 0.2, Ce = 0.5, and Ct = 3.0, Ct1 = 0.01.


## Page 29


– 29 –
31.0
31.5
32.0
32.5
33.0
0.0
0.2
0.4
0.6
0.8
1.0
 
 
lnP
P
e
=1
Convective boundary
Convection
     zone
Fig. 6.— Numerical result of the structure of ω in overshooting region. The stellar model is the
solar model at present age. Ce1 = 0.01. The others TCM parameters are the same as Fig.1, except
α = 0.2 in order to enlarge θ to show the thermal dissipation region in which Pe ≪1. With those
parameters, the equilibrium value in convection zone is ωcz = 0.6, and the equilibrium value in
overshooting region is ωo = 0.293 which denoted as the dotted line.


## Page 30


– 30 –
31.0
31.5
32.0
32.5
33.0
33.5
1E-20
1E-10
1
1E10
Pe=0.1
 
lnP
 K
 U
2
 V
Pe
2
Convection
 zone
Convective 
boundary
Peak of V
Pe=1
Turbulent dissipation region
Thermal dissipation region
Overshooting 
region of 
Fig. 7.— The structure of the overshooting region. K = k, U = u′rT ′, V = T ′T ′. The stellar
model is the solar model at present age. Ce1 = 0.01, the others TCM parameters are the same as
Fig.1, except α = 0.2. With those parameters, in the turbulent dissipation region with Pe ≫1,
theoretical result shows θ = 17.5 vs the numerical result 17.6, theoretical result of exponential
decreasing index of U2 being 26.3 vs the numerical result about 25.6. K is almost parallel to V ,
which is in consistent with the asymptotic solution. In the thermal dissipation region with Pe ≪1,
turbulent motion vanishes.


## Page 31


– 31 –
0.62
0.63
0.64
0.65
0.66
0.67
-3
-2
-1
0
1
 
 
 
R  (10
9
cm)
 U
40
 lnK
Fig. 8.— Numerical data of Meakin & Arnett (2010)’s results. The data of model ’h1’ in their
paper are plotted, where U = FC = ρCPu′rT ′. Only the downward overshooting region is shown.
The distance from the convective boundary (where u′
rT ′ = 0, about R = 0.62 × 109cm) to the
right part of the valley of u′rT ′ is about 0.5 ∼2Hk.


## Page 32


– 32 –
30.5
31.0
31.5
32.0
32.5
-0.2
0.0
0.2
0.4
 
 
R
VT
lnP
 C
e1
=0.01
   C
e1
=0
Convective
  boundary
Convection zone
Fig. 9.— Numerical results of the correlativity of turbulent velocity and temperature RV T. The
stellar model is the solar model at present age. Other TCM parameters are the same as Fig.1. RV T
rapidly decreases to zero in the overshooting region. In the convection zone near the convective
boundary, the diffusion signiﬁcantly enlarges T ′T ′ when Ce1 ̸= 0 (see Fig.3), and then RV T is very
small. In the interior of convection zone, localized TCM shows the equilibrium value of RV T is
RV T,cz =
q
2ωczCe+1
2ωczCt
(see Appendix A). The TCM parameters show RV T,cz = 0.384.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]