---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1111.1742v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1111.1742v2_Spontaneous_chiral_symmetry_breaking_in_the_Tayler_instability

> Source: 1111.1742v2_Spontaneous_chiral_symmetry_breaking_in_the_Tayler_instability.pdf

> Pages: 4

---


## Page 1


arXiv:1111.1742v2  [astro-ph.SR]  9 Nov 2011
Comparative Magnetic Minima
Proceedings IAU Symposium No. 286, 2011
C. H. Mandrini, eds.
c⃝2011 International Astronomical Union
DOI:
Spontaneous chiral symmetry breaking in
the Tayler instability
Fabio Del Sordo1,2, Alﬁo Bonanno3, Axel Brandenburg1,2, and
Dhrubaditya Mitra1
1Nordita, Roslagstullsbacken 23, SE-10691 Stockholm, Sweden, email: fabio@nordita.org
2Department of Astronomy, Stockholm University, SE 10691 Stockholm, Sweden
3INAF- Catania Astrophysical Observatory, Via S.Soﬁa 78, 95123 Catania ITALY
Abstract. The chiral symmetry breaking properties of the Tayler instability are discussed.
Eﬀective amplitude equations are determined in one case. This model has three free parameters
that are determined numerically. Comparison with chiral symmetry breaking in biochemistry is
made.
Keywords. Sun: magnetic ﬁelds, dynamo, magnetic helicity
1. Introduction
An important ingredient to the solar dynamo is the α eﬀect. Mathematically speaking
α is a pseudo scalar that can be constructed using gravity g (a polar vector) and angular
velocity Ω(an axial vector): g · Ωis thus a pseudo scalar and is proportional to cos θ,
where θ is the colatitude. This pseudo scalar changes sign at the equator. This explanation
for large-scale astrophysical dynamos works well and therefore one used to think that
the existence of the α eﬀect in dynamo theory requires always the existence of a pseudo
scalar in the problem. This has indeed been general wisdom, although it has rarely been
emphasized in the literature. That this is actually not the case has only recently been
emphasized and demonstrated. One example is the magnetic buoyancy instability in
the absence of rotation, but with a horizontal magnetic ﬁeld B and vertical gravity g
being perpendicular to each other, so the pseudo scalar g · B vanishes (Chatterjee et al.
2011). Another example is the Tayler instability of a purely toroidal ﬁeld in a cylinder
(Gellert et al. 2011). Thus, the magnetic ﬁeld is again perpendicular to all possible polar
vectors that can be constructed, for example the gradient of the magnetic energy density
which points in the radial direction. In both cases, kinetic helicity and a ﬁnite α, both
of either sign, emerge in the nonlinear stage of the instability. In the former case, the
α tensor has been computed using the test-ﬁeld method. In the latter, the components
of the α tensor have been computed using the imposed-ﬁeld method (see Hubbard et al.
2009, for a discussion of possible pitfalls in the nonlinear case).
The purpose of the present paper is to examine spontaneous chiral symmetry break-
ing in the Tayler instability and to estimate numerically the coeﬃcients governing the
underlying amplitude equations. This allows us then to make contact with a model sys-
tem of chemical reactions that can give rise to the same type of spontaneous symmetry
breaking.
The connection with chemical systems is of interest because the question of sponta-
neous symmetry breaking has a long history ever since Pasteur (1853) discovered the
preferential handedness of certain organic molecules. The preferential handedness of
biomolecules is believed to be the result of a bifurcation event that took place at the
origin of life itself (Kondepudi & Nelson 1984; Sandars 2003; Brandenburg et al. 2005).
464


## Page 2


Symmetry breaking in the Tayler instability
465
Figure 1. Evolution of magnetic helicity for two initial conditions. diﬀering only in the parity
of their initial perturbations. After the exponential growth magnetic helicity levels oﬀ. In the
inset a detail of the exponential growth phase. Here, R ≡sin is used.
2. Numerical simulations
Our setup consists of an isothermal cylinder with a radial extent from sin to sout and
vertical size h. We solve the time dependent ideal MHD equations with periodic boundary
conditions in z, reﬂection in s and periodic in ϕ and a resolution ranging from 643 to
1283 in the three directions.
The azimuthal ﬁeld in the basic state is taken of the form
Bϕ = b0 (s/s0) exp[−(s −s0)2/σ2]
with b0 being a normalization constant; the axial ﬁeld Bz is chosen to be zero. In the basic
state, the Lorentz force is balanced with a gradient of pressure, and we have checked that
our setup was numerically stable if no perturbation was introduced in the system. For
the actual calculations we have chosen h = 2, sin = 1, sout = 3, s0 = 2 and σ2 = 0.2. The
sound speed is assumed to be much larger than the Alf´en speed (≈ten times), similar
to what happens in stellar interiors.
At the beginning of the simulation we perturb the magnetic ﬁeld. We add a pertur-
bation of amplitude 10−7 that of the background ﬁeld. The perturbing ﬁeld has a given
helicity that is either positive or negative. During the development of the instability we
observe a net increase of the helicity, as shown in Fig. 1 where we plot time series of
the normalized magnetic helicity, which exhibits an initial exponential growth, reaches a
peak and then levels oﬀ.
3. Amplitude equations
The linear stability analysis of this instability shows that there exists helical growing
modes. But the left handed and right handed modes have exactly the same growth
rate independent of their helicity. Hence the growth of helical perturbations cannot be
described by a linear theory. However a weakly nonlinear theory is able to describe it as
we show below. Let us begin by considering two helical modes of right handed and left
handed variety respectively each of which satisfy the Beltrami relation ∇×R = ΛR and
∇× L = −ΛL . We can deal with the Fourier transform of these modes, given by
L(x) =
Z
ˆL(q)ddq
and
R(x) =
Z
ˆR(q)ddq
(3.1)
For the left helical mode, total helicity and energy are given by
EL = 1
2
Z
 L2(x)ddx = 1
2
Z
ˆL · ˆL∗ddq
and
HL =
Z
 L · ∇×  Lddx = −2ΛEL,
(3.2)


## Page 3


466
Del Sordo et al.
where ∗denotes complex conjugation. We then have E = EL +ER being the total energy
and H = HL + HR the total helicity. An analogous relation holds for the right-handed
helical mode too.
In the weakly nonlinear regime the evolution of these modes can be described by
general equations of the form:
∂ˆL
∂t = δL
δ ˆL
and
∂ˆR
∂t = δL
δ ˆR
,
(3.3)
where the Lagrangian L can often by written down from symmetry considerations. In
the present case one has to consider the fact that under parity transformation L can
R interchanges into each other. With this additional symmetry the simplest Lagrangian
takes the following form (Fauve et al. 1991)
L[ ˆL, ˆR] =
Z
γ
h
| ˆL|2 + | ˆR|2i
−µ
h
| ˆL|4 + | ˆR|4 −µ∗| ˆL|2| ˆR|2ddq
i
ddq,
(3.4)
The coeﬃcients γ, µ and µ∗cannot be found from symmetry considerations. Note that
in order to show the simplest form, in writing down the Lagrangian we have ignored
dissipation. This gives rise to the following set of amplitude equations,
∂ˆL
∂t = γ ˆL −

µ| ˆL|2 + µ∗| ˆR|2
ˆL,
∂ˆR
∂t = γ ˆR −

µ| ˆR|2 + µ∗| ˆL|2
ˆR.
(3.5)
For certain range of parameters these coupled equations allow the growth of one mode
at the expense of the other (Fauve et al. 1991), a phenomenon known to biologists by
the name “mutual antagonism” (Frank 1953).
Using Eqs. (3.2) and (3.5) and deﬁning H = H/2Λ we can obtain evolution equations
for E and H as
dE
dt = 2γE −2(µ + µ∗)E2 −2(µ −µ∗)H2,
(3.6)
dH
dt = 2γH −4µEH.
(3.7)
Hence, by calculating the total energy and helicity from direct numerical simulations
(DNS) we can determine the unknown coeﬃcients γ, µ and µ∗.
To determine the coeﬃcients γ, µ, and µ∗, we deﬁne the instantaneous logarithmic
time derivatives of E and H, γE = 1
2d ln E/dt and γH = 1
2d ln H/dt, so we have
γ = γH + 2µE,
µ = (γ −γH)/2E,
µ∗= [(γ −γE)E −µ(E2 + H2)]/(E2 −H2). (3.8)
The result is shown in Fig. 2, where we can identify ﬁrst the value of γ ≈14 during the
initial linear growth phase of the instability, and then the values µ ≈10 and µ∗≈7
during the nonlinear stage.
4. Conclusions
The present work has demonstrated that the Tayler instability can produce parity-
breaking and that it is possible to determine empirical ﬁt parameters that reproduce
the nonlinear evolution of energy and helicity. So far, no rigorous derivation of the am-
plitude equations exists, so this would be an important next step. Comparing with the
chiral symmetry breaking instabilities in biochemistry, an important diﬀerence is that in
the present equations the nonlinearity is always cubic, while in biochemistry the domi-
nant nonlinearity tends to be quadratic. In this light, it would be useful to assess more


## Page 4


Symmetry breaking in the Tayler instability
467
Figure 2. Time dependence of γ, µ, and µ8, normalized in terms inner radius and sound
speed. The red lines give the ﬁt results γ ≈14, µ ≈10, and µ∗≈7 in the appropriate units.
closely the possible diﬀerences between biochemical and magnetohydrodynamical sym-
metry breaking.
References
Brandenburg, A., Andersen, A. C., H¨ofner, S., & Nilsson, M., Orig. Life Evol. Biosph. 35, 225
(2005).
Chatterjee, P., Mitra, D., Brandenburg, A., & Rheinhardt, M., Phys. Rev. E 84, 025403R (2011).
Frank, F. C., Biochim. Biophys. Acta 11, 459 (1953).
Gellert, M., R¨udiger, G., & Hollerbach, R., Mon. Not. R. Astron. Soc. 414, 2696 (2011).
Fauve, S., Douady, S., & Thual, O., J. Phys. II 1, 311 (1991).
Hubbard, A., Del Sordo, F., K¨apyl¨a, P. J., & Brandenburg, A., Mon. Not. R. Astron. Soc. 398,
1891 (2009).
Kondepudi, D. K., & Nelson, G. W., Phys. Lett. 106A, 203 (1984).
Pasteur, L., Ann. Phys. 166, 504 (1853).
Sandars, P. G. H., Orig. Life Evol. Biosph. 33, 575 (2003).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]