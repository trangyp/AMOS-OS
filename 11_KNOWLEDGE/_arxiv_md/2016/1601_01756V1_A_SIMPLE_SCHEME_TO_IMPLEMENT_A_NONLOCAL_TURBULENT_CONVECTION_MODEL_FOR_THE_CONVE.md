---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1601.01756v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1601.01756v1_A_simple_scheme_to_implement_a_nonlocal_turbulent_convection_model_for_the_conve

> Source: 1601.01756v1_A_simple_scheme_to_implement_a_nonlocal_turbulent_convection_model_for_the_conve.pdf

> Pages: 29

---


## Page 1


arXiv:1601.01756v1  [astro-ph.SR]  8 Jan 2016
A simple scheme to implement a nonlocal turbulent convection model for the
convective overshoot mixing
Q. S. Zhang1,2
zqs@ynao.ac.cn(QSZ)
ABSTRACT
The classical ’ballistic’ overshoot models show some contradictions and are not
consistence with numerical simulations and asteroseismic studies. Asteroseismic stud-
ies imply that overshoot is a weak mixing process. Diffusion model is suitable to deal
with it. The form of diffusion coefﬁcient in a diffusion model is crucial. Because
the overshoot mixing is related to the convective heat transport (i.e., entropy mixing),
there should be a similarity between them. A recent overshoot mixing model shows
consistence between composition mixing and entropy mixing in overshoot region. A
prerequisite to apply the model is to know the dissipation rate of turbulent kinetic en-
ergy. The dissipation rate can be worked out by solving turbulent convection models
(TCMs). But it is difﬁcult to apply TCMs because of some numerical problems and
the enormous time cost. In order to ﬁnd a convenient way, we have used the asymp-
totical solution and simpliﬁed the TCM to be a single linear equation for turbulent
kinetic energy. This linear model is easy to be implemented in the calculations of
stellar evolution with ignorable extra time cost. We have tested the linear model in
stellar evolution, and have found that the linear model can well reproduce the turbu-
lent kinetic energy proﬁle of full TCM, as well as the diffusion coefﬁcient, abundance
proﬁle and the stellar evolutionary tracks. We have also studied the effects of different
values of the model parameters and have found that the effect due to the modiﬁcation
of temperature gradient in the overshoot region is slight.
Subject headings: convection — stars: interior — stars: evolution
1Yunnan Observatories, Chinese Academy of Sciences, Kunming 650011, China.
2Key Laboratory for the Structure and Evolution of Celestial Objects, Chinese Academy of Sciences, Kunming,
650011, China.


## Page 2


– 2 –
1.
Introduction
The convective motion beyond the boundary of the local linear stability is called the con-
vective overshoot. The mixing caused by the convective overshoot is a major uncertainty of the
current stellar evolutionary theory, since it deeply affects the stellar structure but there is still not
any solid and easy to be used theory at present. The traditional treatment of overshoot is based
on non-local mixing length theories, e.g., ’ballistic’ models (Maeder 1975; Bressan et al. 1981;
Zahn 1991), which show an adiabatically stratiﬁed and completely mixed overshoot region with a
typical length about 0.2 ∼0.4HP where HP = −dr/dlnP is the local pressure scaleheight. Al-
though non-local mixing length models are easy to be implemented in stellar evolution codes and
are widely used, they have some contradictions and they do not have enough spatial resolution to
accurately describe the overshoot process (Renzini 1987). A property of non-local mixing length
models is that there is a jump of ∇(temperature gradient) from ∇ad (the adiabatic temperature
gradient) to ∇R (the radiative temperature gradient) at the boundary of overshoot region. For the
sun, the discontinuity of ∇predicted by non-local mixing length models leads to a characteristic
oscillatory component in the frequencies of solar p-modes (Gough 1990). This has been used to
estimated the length of the overshoot region below the solar convection zone, and an upper limit
has been found as 0.05HP (Roxburgh & Vorontsov 1994; Basu et al. 1994; Basu & Antia 1994;
Monteiro et al. 1994; Christensen-Dalsgaard et al. 1995; Basu 1997). That is too small compared
with the prediction of non-local mixing length models. Christensen-Dalsgaard et al. (2011) have
investigated the temperature gradient proﬁle below the base of the solar convection zone and have
found that, in order to improve the agreement between models and helioseismic constraints, we
actually need a smooth proﬁle of ∇which are outside the realm of the non-local mixing length
overshoot models. The helioseismic study may imply that the downward overshoot region below
the base of the solar convection zone can not be completely mixed. Because overshoot mixes
both entropy and composition (Zhang 2013), efﬁcient entropy and composition mixing lead to
dS/dr = 0 and dXi/dr = 0 in the overshoot region. Entropy and composition being constants
results in ∇= ∇ad, just like the case in the convection zone with efﬁcient convective heat trans-
port. In a recent asteroseismic study on KIC 10526294 (Moravveji et al. 2015), it is also found that
assuming a fully mixed overshoot region above the convective core is not the best choice.
For the convective overshoot such a non-local convection phenomenon, besides non-local
mixing length models, there are turbulent convection models (TCMs) which are based on statis-
tical equilibrium equations of auto and cross-correlations of velocity and temperature perturba-
tions (e.g., Xiong (1981, 1985); Xiong et al. (1997); Canuto (1997); Canuto & Dubovikov (1998);
Deng et al. (2006); Li & Yang (2007); Canuto (2011); Li (2012)).
Xiong’s (1981) TCM and
Li & Yang’s (2007) TCM have been applied in the solar structure models and have been found
to provide the required smooth ∇proﬁle (Zhang & Li 2012a; Zhang et al. 2012). The temperature


## Page 3


– 3 –
gradient proﬁle outside the Schwarzchild local convective boundary predicted by Xiong’s (1981)
TCM or Li & Yang’s (2007) TCM is different from the prediction of non-local mixing length mod-
els. Zahn (1991) has proposed to use two word ’penetration’ and ’overshoot’ to distinguish the
convective motions beyond the Schwarzchild boundary with high efﬁciency of convective heat
transport (’penetration’) and with low efﬁciency (’overshoot’), respectively, and the efﬁciency of
penetration convection is so high that the dominated region is nearly adiabatic stratiﬁed. This adi-
abatic penetration convection region has been predicted by the non-local mixing length models,
e.g., Maeder (1975); Bressan et al. (1981); Zahn (1991). In TCMs (e.g., Xiong (1981); Li & Yang
(2007)), however, that is not the case. TCMs show a continuous proﬁle of temperature gradient
with ∇R < ∇< ∇ad and there is no signiﬁcant adiabatic ’penetration’. Another property of the
TCMs is that ∇−∇R is signiﬁcant nonzero only in a thin layer near the Schwarzchild boundary
and ∇−∇R ≈0 in the further region in which turbulent kinetic energy is still nonzero. This means
that the TCMs predict a thin ’penetration’ layer (the convective heat ﬂux is signiﬁcant nonzero but
is not enough to result in ∇≈∇ad) and an thick ’overshoot’ region (the convective heat ﬂux is
too small to modify ∇). Theoretical analysis shows that the depth of the thin ’penetration’ layer
predicted by TCMs is about ∼1Hk (Hk =| dr/dlnk | is the scale height of turbulent kinetic
energy) regardless of what values of parameters are adopted (Zhang & Li 2012b). The thick ’over-
shoot’ region can cover many magnitude of order of turbulent kinetic energy. The main reason
resulting in such a distinction between TCMs and non-local mixing length models is that the lat-
ter include the assumption that vertical velocity and temperature ﬂuctuation is strongly correlated,
which results in signiﬁcant convective heat ﬂux making the stratiﬁcation outside the convective
boundary quasi-adiabatic (Petrovay & Marik 1995). Numerical solutions of TCMs (e.g., Xiong
(1985); Xiong & Deng (2001); Zhang & Li (2012b)) show that the correlation coefﬁcient between
vertical velocity and temperature ﬂuctuation changes from 1 to 0 near the convective boundary.
A weak correlation between vertical velocity and temperature ﬂuctuation leads to an exponential
solution of turbulent kinetic energy and a deep convective overshoot (Petrovay & Marik 1995),
which has been found in numerical solutions of TCMs. Flows penetrate from the convective un-
stable zone to the convective stable zone (corresponding to ’penetration’ of ’ﬂuid particles’) could
preserve strong correlation and contribute to convective heat ﬂux, but the ﬂows originally located
in the stable zone (corresponding to ’overshoot’ of kinetic energy) are of weak correlation thus
have little contribution to convective heat ﬂux. Those two kinds of ﬂows are the reason of the
decreasing correlation between vertical velocity and temperature ﬂuctuation (Petrovay & Marik
1995; Zhang 2013). It should be noticed that the latter which is caused by the convective transport
of the kinetic energy was usually ignored in non-local mixing length models. The weak correlation
between vertical velocity and temperature ﬂuctuation has been conﬁrmed in numerical simulations
(e.g., Singh et al. (1995); Meakin & Arnett (2007)). The numerical simulations of convective pen-
etration and overshoot (Brummell et al. 2002) have found that the convective penetration can not
establish an adiabatic stratiﬁcation even though the P´eclet number is much larger than unit. Those


## Page 4


– 4 –
results of simulations are inconsistent with non-local mixing length models.
Beside the traditional treatment, we could model the overshoot mixing as a diffusion pro-
cess (e.g., Deng et al. (1996); Ventura et al. (1998); Herwig (2000); Zhang & Li (2012a); Zhang
(2013)). The point in a diffusion model is the form of the adopted diffusion coefﬁcient. For ex-
ample, in Ventura et al. (1998), the diffusion coefﬁcient is D = uld/3 where u is characteristic
turbulent speed and ld is the convective scale length, as similar as in the convection zone, and
the characteristic turbulent speed u is assumed as exponential decreasing based on Xiong’s (1985)
turbulent convection model. This diffusion model predicts an exponential decreasing diffusion co-
efﬁcient D in overshoot region and the characteristic length for mixing in overshoot region is the
same as the characteristic length in convection zone. On the other hand, the form of the diffusion
coefﬁcient in overshoot mixing should be related to the convective heat transport in the overshoot
region because the latter is actually caused by the entropy mixing. In high P´eclet number over-
shoot region, the convective time scale is too short for ﬂows to exchange their entropy, as well as
their composition. The similarity between composition mixing and entropy mixing implies that
the form of both may be the same. Turbulent convection models show that the convective heat
ﬂux ur′T ′ in the overshoot region is (Xiong 1989; Deng et al. 1996; Li & Yang 2007; Zhang & Li
2012b; Li 2012):
ur′T ′ ∝−T
δgε
(1)
where g is the gravitational acceleration, T is temperature, δ = −(∂ln ρ/∂ln T)P is the dimen-
sionless expansion coefﬁcient and ε is the dissipation rate of turbulent kinetic energy. Therefore
the entropy ﬂux ur′S′ of the overshoot region is:
ur′S′ ≈cP
T ur′T ′ ∝−cP
δg ε ∼−ε
N2
∂S
∂r
(2)
where N2 describes the squared buoyancy frequency, S is entropy and cP is speciﬁc heat capacity
at constant pressure. This expression shows that the diffusion coefﬁcient for entropy mixing in high
P´eclet number overshoot region is DS ∝ε/N2. In Zhang’s (2013) convective mixing model, the
diffusion coefﬁcient is solved based on hydrodynamic equations and some closure assumptions.
The solution is that the diffusion coefﬁcient for convective mixing in the convection zone is of the
form D ∝k2/ε ∼ul and the diffusion coefﬁcient for convective overshoot mixing is of the form
D ∝ε/N2. The result is consistent with the convective entropy mixing in both convection zone
and overshoot region.
The prerequisite of applying Zhang’s (2013) convective mixing model is to know the dissipa-
tion rate of turbulent kinetic energy ε in the overshoot region. At present, an practicable option is
to use TCMs (e.g., Xiong (1981, 1985); Xiong et al. (1997); Canuto (1997); Canuto & Dubovikov


## Page 5


– 5 –
(1998); Deng et al. (2006); Li & Yang (2007); Canuto (2011); Li (2012)) which has been suggested
to deal with the convective overshoot by the helioseismic study (Christensen-Dalsgaard et al. 2011).
Those TCMs are based on hydrodynamic equations and closure assumptions, describe the evolu-
tion and distribution of averaged correlations of turbulent variables (ur′ur′, ur′T ′, T ′T ′, ε, etc. ) in
stellar interior. However, TCMs are highly nonlinear equations, too complicated to be applied in
stellar evolution. Sometimes it is difﬁcult to ﬁnd a solution satisfying both TCM equations and the
stellar structure equations due to numerical calculation problems. Even for the converged stellar
evolution models, the time cost is enormous (normal time cost multiplying by a factor of 50 ∼100)
(Zhang 2015). In order to apply the convective mixing model, it is necessary to simplify TCMs
to stably and quickly solve the distribution of turbulent kinetic energy ε in stellar interior. In this
paper, we introduce a simple scheme to implement Li & Yang’s (2007) TCM for the convective
overshoot mixing. The content of this paper is as follows: the overshoot mixing model is intro-
duced in section 2, the TCM and its properties are introduced in section 3, the details of the simple
scheme are described in section 4, the numerical results of the simple scheme are shown in section
5 and section 6 is a summary.
2.
The overshoot mixing model
In this paper, Zhang’s (2013) model of overshoot mixing is adopted. The model is derived
from ﬂuid dynamic equations and some assumptions. The model shows that the convective over-
shoot mixing in high P´eclet number region can be treated as a diffusion process with the diffusion
coefﬁcient as follow:
D = COV
ε
Nturb
2
(3)
where N2
turb is calculated as
Nturb
2 = −δg
HP
[∇−∇ad −
(4)
C1CA
I
X
i=1
(∂ln T
∂Xi
)
P,ρ,X−{Xi}
dXi
d ln P ]
where I is the number of independent elements, ε is the dissipation rate of turbulent kinetic energy,
∇ad is adiabatic temperature gradient, ∇is real temperature gradient in stellar interior, COV , C1
and CA are model parameters, Xi is the mass fraction of the i-th element, other symbols are with
their usual meanings. The parameter COV is a proportion factor which could be determined by
calibrations of ﬁtting observation, the parameter C1 is used to model the turbulent abundance-
abundance correlation X′
iX′
j and the parameter CA is used to model the dissipation of turbulent


## Page 6


– 6 –
temperature-abundance correlation T ′X′
j. N2
turb is similar to the squared Brunt-V¨ais¨al¨a frequency
N2 since N2
turb = N2 when C1CA = 1 which is assumed in Zhang (2013). However, according to
Canuto & Dubovikov (1998) and Canuto (2011), C1 = σt = 0.72 where σt is the turbulent Prandtl
number.
The representation of the diffusion coefﬁcient shows the image that the length scale (in ra-
dial) for mixing lmix =
√
k/Nturb and the lifetime τmix = τ = k/ε where k is the turbulent
kinetic energy, since the diffusion coefﬁcient is D ∝l2
mix/τmix. The diffusion coefﬁcient of matter
mixing has the same form to convective heat transport (i.e., entropy mixing) in high P´eclet num-
ber overshoot region (Zhang 2013), because the turbulent convection models (e.g., Xiong (1989);
Deng et al. (2006); Zhang & Li (2012b)) show that the convective heat ﬂux is proportion to the
dissipation rate of turbulent kinetic energy in high P´eclet number overshoot region. The physical
reason is that the convective heat transport in high P´eclet number region is equivalent to the en-
tropy mixing and the entropy mixing is an accessory of the matter mixing (Zhang 2013). The same
form for matter mixing and for convective heat transport implies the consistence between turbulent
convection models and the overshoot mixing model.
In order to apply the overshoot mixing model in stellar evolution, one must know the dissipa-
tion rate of turbulent kinetic energy, i.e., ε, in the overshoot region. At present, we can calculate the
dissipation rate of turbulent kinetic energy in the overshoot region by using turbulent convection
models.
3.
Li & Yang’s (2007) nonlocal turbulent convection model and its properties
The turbulent convection model (TCM) adopted in this paper was developed by Li & Yang
(2007):
∂
∂m[(dm
dr )2(2Cskrτ)∂kr
∂m] = 1
3kτ −1 −δg
T ur′T ′
(5)
+Ckτ −1(kr −k
3),
∂
∂m[(dm
dr )2(2Cskrτ) ∂k
∂m] = kτ −1 −δg
T ur′T ′,
(6)
∂
∂m[(dm
dr )2(4Ct1krτ)∂ur′T ′
∂m ] = −δg
T T ′T ′
(7)
−2kr
T
HP
(∇−∇ad) + Ct(1 + Pe
−1)τ −1ur′T ′,


## Page 7


– 7 –
∂
∂m[(dm
dr )2(Ce1krτ)∂T ′T ′
∂m ] = −ur′T ′ T
HP
(∇−∇ad)
(8)
+Ce(1 + Pe
−1)τ −1T ′T ′.
In above equations, the meanings of symbols are as follows: kr = u′ru′r/2 is the radial kinetic
energy, u′
rT ′ is the convective heat ﬂux, T ′T ′ is the temperature variance, τ = k/ε is the turbulent
dissipation time scale with the turbulent dissipation ε = k3/2/l in which l = αHP, Pe = l
√
k/DR
is the Pecl´et number in which the radiative diffusion coefﬁcient DR = λ/ρcP and the thermal
conduction coefﬁcient λ = 4acT 3/(3κρ), Cs, Ct, Ce, Ct1, Ce1, Ck and α are model parameters,
other symbols are with their usual meanings. The parameter Ce in this model is related to the
overshoot mixing model by COV = CA −Ce (Zhang 2013).
This TCM has been investigated in theoretical by Zhang & Li (2012b). Now we recall the
main results.
In the convection zone with high P´eclet number, turbulence is nearly in local equilibrium,
thus the localized model (ignoring the diffusion terms on the l.h.s. of the equations of the nonlocal
model) is reasonable to describe the turbulent convection (Li & Yang 2001). The approximate
solution of the localized model in high P´eclet convection zone shows that the temperature gradient
is very close to the adiabatic temperature gradient .
In the overshoot region, the diffusion of turbulent kinetic energy is necessary since the turbu-
lent energy in the convective overshoot region is supported by nonlocal convective transport. By
ignoring the diffusions of u′rT ′ and T ′T ′ (i.e., setting Ct1 = Ce1 = 0), it has been found that the
asymptotical solution in overshoot region with Pe ≫1:
k = kC( P
PC
)θ,
(9)
ur′T ′ = Max{−T
HP
DR(∇ad −∇R), −2Ceω T
δgε},
(10)
T ′T ′ = 2 T
HP
T
δg(∇ad −∇)ωk,
(11)
where kC is k at the Schwarzchild convective boundary where ∇R = ∇ad, ω = kr/k is the
anisotropic degree, θ = dlnk/dlnP is the exponential decreasing index of turbulent kinetic energy
in overshoot region.
The exponential decreasing index of turbulent kinetic energy in overshoot region θ is deter-
mined by:
θ = ± 1
α
r
1 + 2CeωO
3CsωO
,
(12)


## Page 8


– 8 –
where the sign depends on the direction of overshoot: positive for upward and negative for down-
ward.
The value of kC can be estimated by using the ’the maximum of diffusion’ method as:
kC
3
2 ≈1
ekB,Local
3
2 ≈1
eα[δgDR(∇R −∇ad)]B.
(13)
where location B is a point in the convection zone with the distance to the convective boundary
being:
|rB −rC| =
r
4CsωC
3
l
(14)
where rC is the radius at the convective boundary.
Some typical values of the anisotropic degree ω in some cases are as follows: ωCZ the
anisotropic degree in the convection zone:
ωCZ =
2
3Ck
+ 1
3,
(15)
ωC the anisotropic degree at the convective boundary:
ωC ≈1
2(ωCZ + 1
3),
(16)
and ωO the asymptotical equilibrium value of the anisotropic degree in overshoot region satisﬁes
the following equation:
2CeωO
2 −(Ck −1 + 2Ce)ωO + 1
3(Ck −1) = 0.
(17)
The parameter Ck should be larger than 1 and the smaller root of ωO is the physical root (see
Appendix A).
The above solution is for the turbulent convection model in overshoot region with Pe ≫1, and
the the diffusions of u′rT ′ and T ′T ′ are ignored. In the low Pe overshoot region, it is mathematically
required that turbulent variables must be cut off in a short distance. Therefore it is reasonable to
ignore the overshoot in low Pe region. The diffusions of u′rT ′ is ignorable since the diffusion is
much less than the local terms. The diffusions of T ′T ′ smoothes the proﬁle of u′
rT ′ and T ′T ′ near
the convective boundary but basically does not affect the proﬁle of k. For those reasons, we can
use the above approximate / asymptotical solution instead of the numerical solution of the TCM.


## Page 9


– 9 –
4.
Linear model of nonlocal turbulent convection model for overshoot mixing
By solving Li & Yang’s (2007) nonlocal turbulent convection model to obtain the dissipation
rate of turbulent kinetic energy ε = k3/2/l where l = αHP, one can apply the overshoot mixing
model. However, it is difﬁcult to apply such a nonlocal turbulent convection model in stellar
evolution (e.g., Zhang (2015)): the time cost is enormous and numerical instability can not be
totally resolved yet. It is necessary to ﬁnd a simple approach in order to work out the dissipation
rate conveniently. The asymptotical solution is simple to be used but the estimate of kC can not be
used for thin convection zone or a small convective core, and the accuracy of the estimate is not
high enough. We need to ﬁnd a better way.
The equation of turbulent kinetic energy in diffusion equilibrium Eq.(6) is equivalent to the
following equation:
∂
∂m[(dm
dr )2(4
3ωCsl)∂k
3
2
∂m ] = ε −δg
T ur′T ′.
(18)
As mentioned above, the temperature gradient in high P´eclet convection zone is near adiabatic
temperature gradient, and the convective heat ﬂux in high P´eclet overshoot region satisﬁes Eq.(10).
Therefore the convective heat ﬂux in high P´eclet region (no matter in convection zone or in over-
shoot region) satisﬁes Eq.(10):
ur′T ′ = Max{−T
HP
DR(∇ad −∇R), −2Ceω T
δgε}.
(19)
The point of junction at which −(T/HP)DR(∇ad −∇R) = −2Ceω(T/δg)ε locates in the over-
shoot region with the distance to the convective boundary being (Zhang & Li 2012b):
lad ≈ϕHP, ϕ =
α
q
4CsωC
3
e
2CeωC + 1.
(20)
Therefore the convective heat ﬂux in high P´eclet region can also be written as: for the case of
∇ad > ∇R and
ln P
PC
 > ϕ:
ur′T ′ = −2Ceω T
δgε,
(21)
where PC is the pressure of the closest convective boundary, and for other cases:
ur′T ′ = −T
HP
DR(∇ad −∇R).
(22)
Taking the representation of the convective heat ﬂux Eq.(21) and Eq.(22) into Eq.(18), and noting
that ε = k3/2/l, we get a linear equation of k3/2.


## Page 10


– 10 –
Another variable needed to be determined is the anisotropic degree ω. In the convection zone,
ω changes from ωC to ωCZ in the region near the convective boundary with the diffusion of k
dominating. In overshoot region, numerical calculations shows that ω changes from ωC to ωO
near the convective boundary in a typical length about 1Hk where Hk = |dr/dlnk| = HP/|θ| is
the scale height of turbulent kinetic energy. Thus, we estimate ω by using linear interpolation as
follows: for the case of ∇R ≥∇ad:
ω = Min(1, χ)ωCZ + Max(0, 1 −χ)ωC,
(23)
χ = 1
α
r
3
4CsωC
ln P
PC
 ,
and for the case of ∇R < ∇ad:
ω = Min(1, β)ωO + Max(0, 1 −β)ωC,
(24)
β =

1
θ ln P
PC
 ,
where PC is the pressure of the closest convective boundary.
A linear model of turbulent kinetic energy in diffusion equilibrium with Pe ≫1 comprises
Eqs. (18), (21), (22), (23) and (24). In order to solve the linear model, we need to set two boundary
conditions. A reasonable set of boundary conditions are zero ﬂux at the stellar center and the stellar
surface:
∂k
∂m

m=0
= ∂k
∂m

m=M
= 0.
(25)
The problem is that, in general, P´eclet number is low in a thin envelope of a star. This leads to some
mistakes when the linear model with the assumption Pe ≫1 is used. In thin convective envelope(s)
below the stellar surface, the ignorable radiative heat exchange leads to low P´eclet number so
that the temperature gradient is higher than the adiabatic temperature gradient. In this case the
convective heat ﬂux is smaller than the adiabatic heat ﬂux (e.g., Eq.(22)) so that the kinetic energy
should be smaller than the value determined by the linear model. However, the difference should
exist only in the low P´eclet layer extending by several typical diffusion length scale ∼l. Therefore
using those boundary conditions should not lead to mistake for the convective core overshooting
and the thick convective envelope downward overshooting. If the ﬁnal solution of turbulent kinetic
energy shows some regions with Pe = l
√
k/DR < 1 in overshoot region, we suggest to reset zero
turbulent kinetic energy in those region, for the reason that the turbulent convection model shows
that the turbulent variables quickly cut-off in low P´eclet region as mentioned in Section 3.


## Page 11


– 11 –
5.
Numerical results
We use the stellar evolution code YNEV (Zhang 2015) to test the linear model in overshoot
mixing. We use two approaches to calculate the stellar evolutionary models to compare with
each other. The ﬁrst approach is to implement the full nonlocal turbulent convection model (e.g.,
Eqs.(5-8) and the overshoot mixing model Eq.(3) in stellar evolution (see Zhang (2015), Section
3.2), denoted as ’full TCM’ approach. The MLT theory is replaced by the turbulent convection
model. The convective heat ﬂux determining the temperature gradient and the dissipation rate ε
determining the diffusion coefﬁcient of mixing in overshoot region are calculated by using the
turbulent convection model. The second approach is standard stellar model (use MLT to determine
the convective heat ﬂux) with an extra diffusion overshoot mixing (Eq.(3)) with the dissipation rate
ε determined by using the linear model, denoted as ’linear model’ approach. .
In the adopted stellar evolution code, the convection zone is artiﬁcially fully mixed at ﬁrst
and then we solve the overshoot mixing. This may lead a problem in using Eq.(4). Because the
artiﬁcial mixing may lead to a discontinuity at the convective boundary, N2
turb may not exist at the
boundary in that case if using Eq.(4) to calculate. In order to avoid this problem resulting from the
artiﬁcial mixing, we use this formula to calculate N2
turb:
Nturb
2 = −δg
HP
[∇−∇ad −
(26)
ψC1CA
I
X
i=1
(∂ln T
∂Xi
)
P,ρ,X−{Xi}
dXi
d ln P ]
where the parameter ψ is deﬁned as
ψ = Min[1, Max(0, ∇R −∇ad −d
d
)]
(27)
and d is a small value (we set d = 0.002) to determine the depth of the swap region between the
convective boundary and the location ψ = 1. Using that formula to calculate N2
turb is reasonable,
because the swap region is small and it should be efﬁciently mixed due to the high diffusion
coefﬁcient. In solving the diffusion equation of mixing:
∂Xi
∂t =
∂
∂m[(dm
dr )2D∂Xi
∂m ],
(28)
the diffusion coefﬁcient D is calculated by using Eq.(3) in overshoot region and its upper limit
is set to be D = 1010 (enough for ensure the full mixing), the boundary conditions are zero ﬂux
conditions at the stellar center and the stellar surface.
The OPAL equation of state tables EOS2005 (Rogers & Nayfonov 2002) are used to calcu-
late the thermodynamic functions. The Rosseland mean opacities in high and low temperature


## Page 12


– 12 –
region are interpolated from the OPAL tables (Iglesias & Rogers 1996) and the low-temperature
tables (Ferguson et al. 2005), respectively. The rates of all nuclear reactions are based on Angulo
(1999) and Caughlan & Fowler (1988) and enhanced by a factor due to weak electron screening
(Salpeter 1954). The composition in heavy elements are set as the GN93 (Grevesse & Noels 1993)
or AGSS09 (Asplund et al. 2009) solar composition. Except the overshoot mixing, non-standard
physical processes (settling, mass-loss, rotation and etc.) are not taken into account.
In our tests, the basic values of parameters are as follows. The convection parameters are
αMLT = 1.75 for MLT and α = 0.8 for the TCM. They are the typical value for solar calibrations.
Solar calibrations show that αMLT = (2.1 ∼2.2)α. Other TCM parameters are: Ct1 = Ce1 = 0,
Ct = 7.5, Ce = 0.2, Cs = 0.08 and Ck = 2.5. TCM parameters Ct, Ce, Cs and Ck are based on
the reproduction of the temperature gradient below the solar convection zone to the helioseismic
required proﬁle (Zhang & Li 2012a). The parameters in the overshoot mixing model are COV =
10−3 based on calibrations on some observations (Zhang 2013; Meng & Zhang 2014) and C1 =
0.72 (Canuto & Dubovikov 1998; Canuto 2011). In order to test the effects of different values of
parameters, the parameters are varied in large ranges around their basic values.
5.1.
validating the linear model
We calculate stellar evolutionary models with the mass range 1.5M⊙∼10M⊙from ZAMS
to the AGB phase (or RGB phase for the 1.5M⊙star). We then compare the model properties (e.g.,
turbulent kinetic energy, diffusion coefﬁcient, abundance in stellar interior and the stellar evolution
tracks) between two approaches of calculating the stellar evolutionary models: the ’full TCM’ and
the ’linear model’ approaches. Parameters of the TCM and the overshoot model are set as their
basic values.
Turbulent kinetic energy k is a direct indicator to check whether the linear model is a good
approximation of the full TCM. Figures 1 and 2 show the proﬁles of turbulent r.m.s. speed
√
k
obtained by using linear model and full TCM for 4M⊙and 7M⊙stellar models in different com-
position and state. The stellar models in Figs. 1a and 2a are in main sequence stage with the
hydrogen abundance in the center XC = 0.4. The turbulent r.m.s. speed proﬁles obtained by using
linear model and full TCM are almost identical, validating the linear model is a reasonable simpli-
ﬁcation of the full TCM. In the linear model, we cut-off k at about lgT = 6.85 because the P´eclet
number is smaller than unit in the overshoot layer with lgT < 6.85. The TCM shows as the dashed
line that k quickly decreases to zero in the overshoot region with Pe ≪1. The stellar models in
Figs. 1b and 2b are at the top of red giant branch where the center helium burning just begins.
There is a thick convective envelope and a convective helium burning core in each stellar model.
The linear model well reproduces the result of full TCM except the surface layer. The difference is


## Page 13


– 13 –
6.6
6.8
7.0
7.2
7.4
7.6
10
-6
10
-4
10
-2
10
0
10
2
10
4
10
6
a
Convective
    Core
 
 
S Q R T (k )
lgT
full TCM
linear model
4
5
6
7
8
10
-4
10
-2
10
0
10
2
10
4
10
6
10
8
convective He 
  burning core
convective envelope
 
 
S Q R T (k )
lgT
full TCM
linear model
b
Fig. 1.— Turbulent r.m.s. speed in cm/s for a 7M stellar model with X = 0.7, Z = 0.02 and
GN93 mixture: a - at the time XC = 0.4, b - at the top of RGB. The gray solid lines are calculated
by the using linear model of turbulent kinetic energy, and the black dashed lines are calculated by
the full nonlocal turbulent convection model. The dotted-lines indicate the convective boundaries.


## Page 14


– 14 –
6.6
6.8
7.0
7.2
7.4
7.6
10
-6
10
-4
10
-2
10
0
10
2
10
4
10
6
full TCM
 
 
S Q R T (k )
lgT
Convective
    Core
linear model
a
4
5
6
7
8
10
-4
10
-2
10
0
10
2
10
4
10
6
10
8
convective He
burning core
 
 
S Q R T (k )
lgT
convective envelope
b
linear model
full TCM
Fig. 2.— Similar to Fig.1, but for a 4M stellar model with X = 0.715, Z = 0.014 and AGSS09
mixture: a - at the time XC = 0.4, b - at the top of RGB.


## Page 15


– 15 –
due to Pe ≪1 in the surface layer so that the assumption of linear model does not stand. However,
as mentioned in Section 4, the difference exists only in the low P´eclet number layer extending by
several l and does not affect the mixing diffusion coefﬁcient in the overshoot regions.
The proﬁles of diffusion coefﬁcient of convective mixing for main sequence stellar models
with different mass are shown in Fig. 3. The result of linear model is almost identical to the
result of full TCM. We have not calculated the diffusion coefﬁcient in the convective core but set
to be 1010 which is large enough to ensure complete mixing. According to the convective mixing
model (Zhang 2013), the diffusion coefﬁcient in the convective core is ∼l
√
k which is much larger
than 1010 and leads to a fully mixed core. The convective mixing model shows that the form of
diffusion coefﬁcient transfers from D ∼l
√
k in the convective core to D ≈COV ε/N2
turb in the
overshoot region (Zhang 2013). This is shown in the ﬁgure that the diffusion coefﬁcient quickly
decreases near the convective boundary and exponentially decreases in the overshoot region. The
latter is because ε exponentially decreases and N2
turb changers much slower than ε in most part
of the overshoot region. The diffusion coefﬁcient in the overshoot region is not high enough to
ensure complete mixing. This leads to smooth proﬁle of abundance in stellar interior, as shown
in Fig. 4. The classical overshoot mixing model, which extends the fully mixing region from
convective boundary by a distance, can not obtain such smooth proﬁle of abundance. Figure 4
shows hydrogen abundance proﬁle in stellar interior for different mass in main sequence. The
nearly identical proﬁles validate that the linear model can be used to substitute the full TCM in
modeling overshoot mixing.
The stellar evolutionary tracks with linear model and full TCM for different mass are shown
in Fig. 5 and Fig. 6. The track with linear model are almost identical to the track with full TCM
in the all stage for different stellar mass. This validates that the linear model results in the same
strength of overshoot mixing comparing with the full TCM. In the red giant branch, there is a
small difference on temperature (about 50K) between stellar models with linear model and full
TCM. This is caused by the difference of turbulent heat transport efﬁciency between TCM and
MLT (adopted in the stellar models with linear model) in super-adiabatic convection zone near the
surface. In the solar case, in order to generate similar turbulent heat transport efﬁciency in super-
adiabatic convection zone, we requires αMLT = (2.1 ∼2.2)α as mentioned above. However,
this ratio may change a little for different stellar mass or different evolutionary stage. This effect
is ignorable for intermediate mass main sequence stars because the thin convective envelope is
dominated by the radiative heat transport and the convective core is almost adiabatic stratiﬁed,
regardless of which convection theory (MLT or TCM) is adopted.


## Page 16


– 16 –
6.4
6.8
7.2
7.6
10
-8
10
-4
10
0
10
4
10
8
10
12
6.8
7.2
7.6
10
-8
10
-4
10
0
10
4
10
8
10
12
full TCM
Core
 
 
D (c m
2
/s )
lgT
AGSS09
4M
Sun
  X
C
=0.40
linear model
full TCM
linear model
GN93
7M
Sun
  X
C
=0.40
 
lgT
Core
Fig. 3.— Diffusion coefﬁcient in convective core overshoot regions for two 4M⊙stellar models
with X = 0.715, Z = 0.014 and AGSS09 mixture and two 7M⊙stellar models with X = 0.7,
Z = 0.02 and GN93 mixture at the time XC ≈0.4. The gray solid lines are for the stellar models
calculated by the using linear model of turbulent kinetic energy and the overshoot mixing model,
and the black dashed lines are the stellar models calculated by the full nonlocal turbulent convec-
tion model and the overshoot mixing model. The dotted-lines indicate the convective boundaries.


## Page 17


– 17 –
0.0
0.2
0.4
0.6
0.8
1.0
0.4
0.5
0.6
0.7
4M
Sun
(AGSS09)
3M
Sun
(GN93)
full TCM
 
 
X
m/M
1.5M
Sun
(GN93)
7M
Sun
(GN93)
linear model
Fig. 4.— Hydrogen abundance in stellar interior for stellar models with X = 0.7, Z = 0.02
and GN93 mixture: two 1.5M⊙stellar models with XC ≈0.36, two 3M⊙stellar models with
XC ≈0.46 and two 7M⊙stellar models with XC ≈0.4. Two 4M⊙stellar models with X = 0.715,
Z = 0.014 and AGSS09 mixture at the time XC ≈0.4 are also shown. The gray solid lines are
for the stellar models calculated by the using linear model of turbulent kinetic energy and the
overshoot mixing model, and the black dashed lines are the stellar models calculated by the full
nonlocal turbulent convection model and the overshoot mixing model.


## Page 18


– 18 –
4.4
4.2
4.0
3.8
3.6
0
1
2
3
4
5
GN93, X=0.7, Z=0.02
full TCM
10
9
8
7
6
5
4
3
2
 
 
lg (L /L
S u n
)
lgT
eff
1.5
linear model
Fig. 5.— Stellar evolutionary tracks in HR diagram for stellar models with X = 0.7, Z = 0.02 and
GN93 mixture. The gray lines are calculated by the using linear model of turbulent kinetic energy
and the overshoot mixing model, and the black lines are calculated by the full nonlocal turbulent
convection model and the overshoot mixing model.


## Page 19


– 19 –
4.4
4.2
4.0
3.8
3.6
0
1
2
3
4
5
10
9
8
7
6
5
4
3
2
1.5
 
 
lg (L /L
s u n
)
lgT
eff
full TCM
linear model
AGSS09, X=0.715,Z=0.014
Fig. 6.— Similar to Fig.5, but for stellar models with X = 0.715, Z = 0.014 and AGSS09 mixture.


## Page 20


– 20 –
5.2.
Effects of the parameters
Parameters involved in the linear model of nonlocal turbulent convection model are Cs, Ce,
Ck and α, and parameters involved in the overshoot mixing model are COV and C1. We have
tested the effects of those parameters on 2M⊙(X = 0.715, Z = 0.014, AGSS09 composition)
stellar models. Figure 7 shows the evolutionary tracks in main sequence with different value of
parameters (for the parameters which are not speciﬁc, they are set as their basic values: Ce = 0.2,
Cs = 0.08, Ck = 2.5, α = 0.8, C1 = 0.72 and COV = 10−3). It is found that the overshoot mixing
is enhanced when Cs, α or COV becomes larger or C1 or Ce becomes smaller. Figure 7d shows that
tracks are insensitive to the parameter Ck. In Fig.7a and Fig.7e, the track for Cs = 0.08 is same
one to α = 0.8, the track for Cs = 0.02 is almost identical to the track for α = 0.4 and the track
for Cs = 0.32 is almost identical to the track for α = 1.6. Those seem to imply that changing Cs
by a factor a is almost equivalent to change α by the factor √a.
Those properties can be explained as follows. Since the linear model and the overshoot mixing
model affect the stellar evolutionary tracks via the diffusion coefﬁcient, let’s analyze the depen-
dence of diffusion coefﬁcient on parameters. As it is shown in Eq.(3), diffusion coefﬁcient is in
proportion to the turbulent dissipation rate which is determined by the linear model. By using
Eq.(9), Eq.(12) and Eq.(13), we ﬁnd:
ln ε
=
ln k
3
2
l ≈ln{[δgDR(∇R −∇ad)]B
eHP
( P
PC
)
3
2 θ}
(29)
≈
const. + f(α2Cs) + 3
2θ(α2Cs, Ce, Ck) ln( P
PC
)
=
const. + f(α2Cs) + 3
2
r
1 + 2CeωO
3α2CsωO
ln P,
where the function of α2Cs term f(α2Cs) represents the location of the point B depending on
α2Cs (see Eq.(14)). For the case of core overshoot, the positive value of θ is adopted and there is
f ′ > 0 in general case because local kinetic energy in the convective core decreases toward the
Schwarzchild boundary. It should be noticed that two parameters α and Cs can be combined to
one. This is the reason for changing Cs by a factor a being almost equivalent to changing α by
the factor √a. It is not difﬁcult to ﬁnd that dθ/d(α2Cs) < 0 and dθ/dCe > 0. This means that
the exponential index of the diffusion coefﬁcient becomes smaller when (α2Cs) becomes larger
or Ce becomes smaller. A smaller index of diffusion coefﬁcient leads to higher efﬁciency for
the mixing. Ck does affect ωO only. For the testing range of Ck, ωO changes a little so that the
tracks are insensitive to Ck. When C1 becomes larger, the weight of abundance gradient in N2
turb
is larger so that N2
turb increases and the diffusion coefﬁcient decreases. The diffusion coefﬁcient is
in proportion to the parameter COV so that the overshoot mixing is enhanced as COV increases.


## Page 21


– 21 –
3.95
3.90
3.85
3.80
1.2
1.4
1.6
1.8
3.95
3.90
3.85
3.80
3.95
3.90
3.85
3.80
1.2
1.4
1.6
1.8
1.2
1.4
1.6
1.8
3.95
3.90
3.85
3.80
3.95
3.90
3.85
3.80
3.95
3.90
3.85
3.80
1.2
1.4
1.6
1.8
=0.4, 0.8, 1.6
dL
tip
/d
 > 0
 
 
a
b
lgT
eff
lg ( L /L
s u n
)
 
 
C
1
=0.36, 0.72, 1.44, 2.88
dL
tip
/dC
1
 < 0
c
 
 
C
e
=0.1, 0.2, 0.4, 0.8, 1.6
dL
tip
/dC
e
 < 0
d
C
k
=1.25, 2.5, 5, 10
dL
tip
/dC
k
 < 0
 
 
e
C
s
=0.02, 0.04, 0.08, 0.16, 0.32
dL
tip
/dC
s
 > 0
 
 
f
lgC
OV
=-4, -3.5, -3, -2.5, -2
dL
tip
/dC
OV
 > 0
 
 
Fig. 7.— Evolutionary tracks for 2M⊙stellar models with X = 0.715, Z = 0.014 and AGSS09
mixture. The parameters α, Ce, Ck, Cs, C1 and COV are varied around their basic values. Ltip
is the luminosity at the tip. For a parameter C, the sign of dLtip/dC indicates the value of the
parameter for each evolutionary track.


## Page 22


– 22 –
5.3.
Effects of the modiﬁcation of temperature gradient in overshoot region
The convective heat ﬂux could modify the temperature gradient in the overshoot region. This
affects the value of Nturb
2 and thus affects the diffusion coefﬁcient of overshoot mixing. In the
previous calculations of stellar models based on ’linear model’, this effect was not taken into ac-
count since the temperature gradient is calculated in the traditional way (MLT in convection zones
and the radiative temperature gradient is adopted outside convection zones). In this subsection,
we investigate the effects of taking into account the modiﬁcation of temperature gradient in the
overshoot region.
We have implemented the modiﬁcation of temperature gradient in the overshoot region as
follows: step 1, solving the linear model to work out / update the convective heat ﬂux in overshoot
region (e.g., Eq(10)) before every iteration in solving the stellar structure equations; step 2, solving
the stellar structure equations by one iteration with the updated convective heat ﬂux in overshoot
region. The iterations stop when the required accuracy is achieved.
It is not difﬁcult to understand that the negative convective heat ﬂux in the overshoot region
should enlarge the temperature gradient and make it closer to the adiabatic temperature gradient,
thus reduce Nturb
2 and enlarge the diffusion coefﬁcient of mixing. It can be found in Eq.(20) that
enlarging parameters α2Cs or Ce enhances the modiﬁcation on temperature gradient. At here, we
take a large value of Ce = 0.8 for example. Other parameters are set as their basic values. We have
tried Ce = 1.6 but we can not get converged stellar models.
Based on the linear model, 2M⊙stellar models with X = 0.715, Z = 0.014 and AGSS09
mixture have been calculated, with or without the modiﬁcation of temperature gradient in the over-
shoot region. Figure 8 shows the temperature gradient near the convective core boundary for the
stellar model with the modiﬁcation at the moment XC ≈0.32. Temperature gradient modiﬁcation
is signiﬁcant in a range ∼0.1HP outside the convective core. Figure 9 shows the diffusion coefﬁ-
cient and hydrogen abundance proﬁle of that stellar model, as well as the stellar model without the
modiﬁcation of temperature gradient. It can be found that diffusion coefﬁcient near the convective
boundary has been enlarged due to the modiﬁed temperature gradient. However, the difference
between hydrogen abundance proﬁles of the two models is not signiﬁcant. This is because the
diffusion coefﬁcient near the convective boundary is very high so that the abundance is very close
to the abundance in the core as shown in the ﬁgure. In this case, enlarging the diffusion coefﬁ-
cient has little effects. The inhomogenous region is in low diffusion coefﬁcient region, in which
the convective heat ﬂux is ignorable so that the diffusion coefﬁcient is not affected. Therefore
the hydrogen abundance proﬁles of the two models are very close to each other. Figure 10 shows
the evolutionary tracks for the stellar models with and without the modiﬁcation of temperature
gradient in the overshoot region. It is also shown that, although the modiﬁcation can enhance the
overshoot mixing, the effect is not signiﬁcant. The comparison is for a large value of Ce = 0.8. If


## Page 23


– 23 –
16.6
16.7
16.8
16.9
17.0
0.30
0.35
0.40
0.45
0.50
R
 
 
te m p e ra tu re  g ra d ie n t
lgP
ad
Fig. 8.— Temperature gradient near the convective core boundary for a 4M⊙stellar model with
X = 0.715, Z = 0.014 and AGSS09 mixture at XC ≈0.32. The black solid line is temperature
gradient ∇, the gray solid line is the radiative temperature gradient ∇R and the gray dashed line is
the adiabatic temperature gradient ∇ad.


## Page 24


– 24 –
16.5
16.6
16.7
16.8
16.9
17.0
10
-2
10
0
10
2
10
4
10
6
10
8
10
10
10
12
X
X
 
D  (in  c m
2
/s )
lgP
D
0.3
0.4
0.5
0.6
0.7
Fig. 9.— Diffusion coefﬁcient and the hydrogen abundance near the convective core boundary for
a 2M⊙stellar model with X = 0.715, Z = 0.014 and AGSS09 mixture at XC ≈0.32, with and
without the temperature gradient modiﬁcation. The black lines are for the stellar model without
temperature gradient modiﬁcation and the gray lines are for the stellar model with temperature
gradient modiﬁcation.


## Page 25


– 25 –
4.00
3.95
3.90
3.85
3.80
1.1
1.2
1.3
1.4
1.5
1.6
1.7
TG modified
 
 
lg (L /L
sun
)
lgT
no TG modification
Fig. 10.— Evolutionary tracks of 2M⊙stellar models with X = 0.715, Z = 0.014 and AGSS09
mixture with and without the temperature gradient modiﬁcation. The black line are for the stellar
models without temperature gradient (TG) modiﬁcation and the gray line are for the stellar models
with temperature gradient modiﬁcation.


## Page 26


– 26 –
the basic value is adopted, the effect should be less important.
6.
Summary
Asteroseismic studies do not support the classical ’ballistic’ overshoot model and implies
that the convective overshoot is a weak mixing process. Zhang’s (2013) overshoot mixing model
describes the overshoot as a weak mixing process and the diffusion coefﬁcient shows consistence
with the overshoot entropy mixing. However, we need to know the dissipation rate of turbulent
kinetic energy in overshoot region before applying that mixing model. A practicable option to
work out the dissipation rate is to solve nonlocal turbulent convection models (TCMs), but this is
difﬁcult because of some numerical problems and the time costs is hard to bear.
In this paper, we have simpliﬁed the full nonlocal turbulent convection model developed by
Li & Yang (2007) to a linear model (e.g., Eqs. (18), (21), (22), (23) and (24)) in order to obtain
the dissipation rate of turbulent kinetic energy which is required in the overshoot mixing model.
The linear model is a single linear diffusion equation for turbulent kinetic energy. It is very easy to
be implemented in a stellar evolution code. The time cost of solving the linear model is ignorable
to compare with solving the full TCM. And there is no numerical difﬁculty in solving the linear
model. We have tested the linear model in stellar evolution code, and have found that the linear
model can well reproduce the turbulent kinetic energy proﬁle of full TCM, as well as the diffusion
coefﬁcient, abundance proﬁle and the stellar evolutionary tracks. We have also studied the effects
of different values of the model parameters and have found that the effect due to the modiﬁcation
of temperature gradient in the overshoot region is slight.
Many thanks to the anonymous referee for careful reading of the manuscript and providing
comments which improved the original version. Fruitful discussions with Y. Li are highly appre-
ciated. This work is co-sponsored by the National Natural Science Foundation of China through
grant No. 11303087 and the Chinese Academy of Sciences (”Light of West China” Program and
Youth Innovation Promotion Association).
A.
Analysis of the root of the quadratic equation of ωO
The asymptotical equilibrium value of the anisotropic degree in overshoot region ωO satisﬁes
the following equation:
2CeωO
2 −(Ck −1 + 2Ce)ωO + 1
3(Ck −1) = 0
(A1)


## Page 27


– 27 –
For convenient, we deﬁne c = (Ck −1)/(2Ce) thus the equation above can be written as:
F(ωO) ≡ωO
2 −(1 + c)ωO + c
3 = 0
(A2)
Since the discriminant is always positive, let ω1 and ω2 be the two roots of the quadratic
equation and ω1 < ω2. According to Vieta’s theorem, there are:
ω1ω2 = c
3,
(A3)
ω1 + ω2 = 1 + c.
(A4)
The values of function F at 0, 1/3 and 1 are:
F(0) = c
3, F(1
3) = −2
9, F(1) = −2c
3 .
(A5)
1. case A: Ck ≤1. In this case, c ≤0 so that ω1 ≤0 ≤ω2. Because F(1/3)F(1) ≤0, we
ﬁnd ω2 ≥1/3. Physically acceptable root should be 0 < ωO < 1/3 because the work of buoyancy
on the radial turbulent kinetic energy is negative in overshoot region, so that there is no acceptable
root when Ck ≤1.
2. case A: Ck > 1. In this case, c > 0, ω2 > (ω1 + ω2)/2 = (1 + c)/2 > 1/2 so that ω2 is not
acceptable. Because F(0)F(1/3) < 0, we ﬁnd 0 < ω1 < 1/3 which is physically acceptable root.
Finally, Ck must be larger than 1 and the physically acceptable root is the small one.
REFERENCES
Angulo, C., et al. 1999, Nucl. Phys. A, 656, 3
Asplund, M., Grevesse, N., Sauval, A. J., & Scott, P. 2009, ARA&A, 47, 481
Bressan, A. G., Bertelli, G., & Chiosi, C. 1981, A&A, 102, 25
Brummell, N. H., Clune, T. L., & Toomre, J. 2002, ApJ, 570, 825
Basu, S., Antia, H. M., & Narasimha, D. 1994, MNRAS, 267, 209
Basu, S., & Antia, H. M. 1994, MNRAS, 269, 1137
Basu, S. 1997, MNRAS, 288, 572


## Page 28


– 28 –
Caughlan, G. R., & Fowler, W. A. 1988, Atomic Data and Nuclear Data Tables, 40, 283
Canuto, V. M. 1997, ApJ, 482, 827
Canuto, V. M., & Dubovikov, M. 1998, ApJ, 493, 834
Canuto, V. M. 2011, A&A, 528, 76
Christenson-Dalsgaard J., Monteiro M. J. P. F. G., & Thompson M. J. 1995, MNRAS, 276, 283
Christensen-Dalsgaard, J., Monteiro, M. J. P. F. G., Rempel, M., & Thompson, M. J. 2011, MN-
RAS, 414, 1158
Deng, L., Bressan, A., & Chiosi, C. 1996, A&A, 313, 145
Deng, L., Xiong, D. R., & Chan, K. L. 2006, ApJ, 643, 426
Ferguson, J. W., Alexander, D. R., Allard, F., Barman, T., Bodnarik, J. G., Hauschildt, P. H.,
Heffner-Wong, A., & Tamanai, A. 2005, ApJ, 623, 585
Gough, D. O., 1990, in: Progress of Seismology of the Sun and Stars, eds. Y. Osaki and H. Shiba-
hashi, Lecture Notes in Physics 367, Springer-Verlag, p. 283
Grevesse, N., & Noels, A. 1993, in Origin and Evolution of the Elements, eds. N. Prantzos, E.
Vangioni-Flam, & M. Casse (Cambridge: Cambridge Univ. Press), 15
Herwig, F., 2000, A&A, 360, 952
Iglesias, C. A., & Rogers, F. J. 1996, ApJ, 464, 943
Li, Y. 2012, ApJ, 756, 37
Li, Y.,& Yang, J. Y. 2001, ChJAA, 1, 66
Li, Y.,& Yang, J. Y. 2007, MNRAS, 375, 388
Maeder, A. 1975, A&A, 40, 303
Meakin, C. A., & Arnett, D. 2007, ApJ, 667, 448
Meng, Y., & Zhang, Q. S. 2014, ApJ, 787, 127
Monteiro M. J. P. F. G., Christensen-Dalsgaard J., & Thompson M. J. 1994, A&A, 283, 247
Moravveji, E., Aerts, C., P´apics, P. I., Triana, S. A., & Vandoren, B. 2015, A&A, 580, 27


## Page 29


– 29 –
Petrovay, K., & Marik, M. 1995, in Ulrich R. K., Rhodes E. J., D¨appenW, eds, ASP Conf. Ser.
Vol. 76, Proc. GONG94: Helio- and Asteroseismology from Earth and Space. Astron. Soc.
Pac., San Francisco, p. 216
Renzini, A. 1987, A&A, 188, 49
Rogers, F. J., & Nayfonov, A. 2002, ApJ, 576, 1064
Roxburgh, I. W., & Vorontsov, S. V. 1994, MNRAS, 268, 880
Salpeter, E. E. 1954, Australian Journal of Physics, 7, 373
Singh, H. P., Roxburgh, I. W., & Chan, K. L. 1995, A&A, 295, 703
Ventura, P., Zeppieri, A., Mazzitelli, I., & D’Antona, F. 1998, A&A, 344, 953
Xiong, D. R. 1981, Sci. Sinica, 24, 1406
Xiong, D. R. 1985, A&A, 150, 133
Xiong, D. R. 1989, A&A, 213, 176
Xiong, D. R., & Deng, L., 2001, MNRAS, 327, 1137
Xiong, D. R., Cheng, Q. L.,& Deng, L. 1997, ApJS, 108, 529
Zahn, J. P., 1991, A&A, 252, 179
Zhang, Q. S., & Li, Y. 2012, ApJ, 746, 50
Zhang, Q. S., & Li, Y. 2012, ApJ, 750, 11
Zhang, Q. S. 2013, ApJS, 205, 18
Zhang, Q. S. 2015, Res. Astron. Astrophys., 15, 549
Zhang, C., Deng, L., Xiong, D. & Christensen-Dalsgaard, J. 2012, ApJ, 759, L14
This preprint was prepared with the AAS LATEX macros v5.2.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]