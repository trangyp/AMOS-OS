---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1212.0032
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1212.0032_SUSY_FLAVOR_library_and_constraints_on__B_s__to_μ___μ_-__decay_rate

> Source: 1212.0032_SUSY_FLAVOR_library_and_constraints_on__B_s__to_μ___μ_-__decay_rate.pdf

> Pages: 5

---


## Page 1


arXiv:1212.0032v1  [hep-ph]  30 Nov 2012
SUSY FLAVOR library and constraints on B0
s →µ+µ−decay rate a
J. ROSIEK
Institute of Theoretical Physics, Physics Department, University of Warsaw, Poland
I present SUSY FLAVOR - a Fortran 77 program able to calculate simultaneously 29 low-energy
ﬂavor and CP-violating observables in the general R-parity conserving MSSM, including the
case of large ﬂavor violation in the sfermion sector. SUSY FLAVOR v2 performs also the resum-
mation of chirally enhanced corrections, arising in large tan β regime and/or large trilinear
soft mixing terms, to all orders of perturbation theory. I discuss an example of application of
SUSY FLAVOR to analysis of the B0
s →µ+µ−decay rate in the MSSM.
1
Introduction
Flavor physics was in the recent years one of the most active ﬁelds in the high energy physics.
New experiments helped to improve the accuracy of various measurements related to rare de-
cays and put strong constraints on the ﬂavor structure of physics beyond the Standard Model
(SM), in particular imposing stringent limits on the ﬂavor- and CP- violating parameters of the
Minimal Supersymmetric Standard Model (MSSM). It is then increasingly important to have
an universal computational tool which helps to compare new data with the predictions of the
MSSM. Developing such a tool is a non-trivial task requiring extensive and tedious calculations.
Numerous existing analyses usually consider only a few rare decays simultaneously and in most
cases they are restricted to the case of so-called Minimal Flavor Violation (MFV) scenario, where
the CKM matrix is the only source of CP and ﬂavour violation 1.
Based on a series of papers where many rare processes were analyzed within the general
MSSM 2−6, a library of relevant computer codes has been published as SUSY FLAVOR v1 7.
SUSY FLAVOR v2 8 is in addition capable of resumming leading chirally enhanced corrections,
important in the regime of large tan β or large trilinear A-terms9,10, to all orders of perturbation
theory and for any pattern of sfermion mass matrices - a unique feature not shared by other
publicly available programs. In this article I brieﬂy summarize the main features of SUSY FLAVOR
and present example of its application to estimating the B0
s →µ+µ−decay rate in the MSSM.
2
SUSY FLAVOR structure, input parameters and calculated observables
SUSY FLAVOR is capable of calculating physical observables within the most general R-parity
conserving MSSM, with one exception: currently it assumes massless neutrinos (and no right
neutrino/sneutrino ﬁelds 11), so the PMNS mixing matrix does not appear in the couplings.
SUSY FLAVOR has been in development long before the Les Houches Accord 12 (SLHA) for
common MSSM conventions was agreed on. Thus, the internal routines of the library follow
the conventions of earlier paper 13. However, by default SUSY FLAVOR can be initialized with
a SLHA2 compatible set of parameters - all translations are done internally.
Note that in
ato appear in proceedings of the Rencontres du Vietnam “Beyond The Standard Model of Particle Physics”,
Qui Nhon, Vietnam July 15-21, 2012


## Page 2


Table 1: One loop parton level formfactors implemented in SUSY FLAVOR. I, J, K, L denote ﬂavor indices.
Box
Penguin
Self energy
dIdJdKdL
Z ¯dIdJ, γ ¯dIdJ, g ¯dIdJ
dI-quark
uIuJuKuL
H0
i ¯dIdJ, A0
i ¯dIdJ
uI-quark
dIdJlKlL
H0
i ¯uIuJ, A0
i ¯uIuJ
charged lepton lI
dIdJνKνL
γ¯lIlJ
SUSY FLAVOR one can also use so-called “non-analytic A-terms” of the form A
′IJ
l
H2⋆LIEJ +
A
′IJ
d H2⋆QIDJ +A
′IJ
u H1⋆QIU J, which are not included in the standard SLHA2 parametrization.
Calculations in SUSY FLAVOR take the following steps 8:
1. Parameter initialization. Users can adjust the basic SM parameters and initialize all (or the
chosen subset of) Higgs sector parameters and supersymmetric soft masses and couplings (which
must be speciﬁed at the SUSY scale).
2. Calculation of the physical masses and the mixing angles. In the next stage, the eigenvalues
of the mass matrices of all MSSM particles and their mixing matrices at tree level are calculated
numerically, without any approximations.
3.
Resummation of the chirally enhanced eﬀects. In the regime of large tan β and/or large
trilinear SUSY breaking terms, large chirally enhanced corrections to Yukawa couplings and
CKM matrix elements arise9. They are resummed to all orders of perturbation theory using the
formalism developed in 10. The level of resummation (no resummation, approximate analytical
resummation in the decoupling limit, iterative numerical resummation) is a user deﬁned option.
4. Calculation of the Wilson coeﬃcients at the SUSY scale. In the current version, SUSY FLAVOR
calculates Wilson coeﬃcients generated by the diagrams listed in Table 1 (routines for given
formfactor accept fermion generation indices as input parameters).
5. Strong corrections. After evaluating virtual SUSY contributions, SUSY FLAVOR performs the
QCD evolution of the Wilson coeﬃcients from the high (SUSY or top quark mass) scale to the
low energy scale appropriate for a given decay. Necessary hadronic matrix element estimates
and other QCD related quantities are treated as external parameters, initialized to the default
values extracted from analyses done within the SM but also directly modiﬁable by users.
6. Evaluation of physical observables. Finally physical observables are calculated and printed
out. Current list of processes implemented in SUSY FLAVOR v2 is listed in Table 2.
3
Application of SUSY FLAVOR to analysis of the B →µ∗µ−decay rate.
One of the most promising signals for new physics at the LHC is the rare decay B0
s →µ+µ−.
It is suppressed as a loop-level ﬂavour-changing neutral current and by a lepton mass insertion
required for the ﬁnal state muon helicities. The LHC will be the ﬁrst experiment able to probe
this decay channel down to its SM-predicted branching ratio. The winter 2012 experimental
95% CL bounds14 and the SM prediction15 for B0
s →µ+µ−decay rate can be summarized as:
CMS
< 7.7 × 10−9
LHCb
< 4.5 × 10−9
SM Prediction
(3.35 ± 0.32) × 10−9
ATLAS, CMS and LHCb will be able soon to reconstruct the SM-like B0
s →µ+µ−signal with
signiﬁcance of 3σ, so that this very rare decay could be ﬁnally discovered and measured.
SUSY FLAVOR is an eﬃcient tool allowing to estimate the size of possible SUSY contributions
to the B0
s →µ+µ−channel. In the MSSM, even in the restricted MFV case, for large values of
tan β the B(B0
s →µ+µ−) can be strongly enhanced 4 (MA is the CP-odd Higgs boson mass):
B(B0
s →µ+µ−)
≈
5 · 10−7
tan β
50
6 300 GeV
MA
4
,
(1)


## Page 3


Table 2: List of observables calculated by SUSY FLAVOR v2 and their currently measured values.
Observable
Experiment
Observable
Experiment
∆F = 1
∆F = 0
B(µ →eγ)
< 2.8 × 10−11
1
2(g −2)e
(1159652188.4 ± 4.3) × 10−12
B(τ →eγ)
< 3.3 × 10−8
1
2(g −2)µ
(11659208.7 ± 8.7) × 10−10
B(τ →µγ)
< 4.4 × 10−8
1
2(g −2)τ
< 1.1 × 10−3
B(KL →π0νν)
< 6.7 × 10−8
|de|(ecm)
< 1.6 × 10−27
B(K+ →π+νν)
17.3+11.5
−10.5 × 10−11
|dµ|(ecm)
< 2.8 × 10−19
B(Bd →ee)
< 1.13 × 10−7
|dτ|(ecm)
< 1.1 × 10−17
B(Bd →µµ)
< 0.8 × 10−9
|dn|(ecm)
< 2.9 × 10−26
B(Bd →ττ)
< 4.1 × 10−3
∆F = 2
B(Bs →ee)
< 7.0 × 10−5
|ǫK|
(2.229 ± 0.010) × 10−3
B(Bs →µµ)
< 4.2 × 10−9
∆MK
(5.292 ± 0.009) × 10−3 ps−1
B(Bs →ττ)
−−
∆MD
(2.37+0.66
−0.71) × 10−2 ps−1
B(Bs →µe)
< 2.0 × 10−7
∆MBd
(0.507 ± 0.005) ps−1
B(Bs →τe)
< 2.8 × 10−5
∆MBs
(17.77 ± 0.12) ps−1
B(Bs →µτ)
< 2.2 × 10−5
B(B+ →τ +ν)
(1.65 ± 0.34) × 10−4
B(Bd→Dτν)
B(Bd→Dlν)
(0.407 ± 0.12 ± 0.049)
B(B →Xsγ)
(3.52 ± 0.25) × 10−4
This result can be further signiﬁcantly modiﬁed by non-vanishing ﬂavor-violating terms in the
sfermion mass matrices, leading to large contributions from box and Z-penguin diagrams. Apart
from enhancing the decay rate, the interference of these terms could also conceivably lead to a
cancellation that would suppress the branching ratio even below the SM prediction 5.
To quantitatively study the size of possible eﬀects, one needs to perform a scan over the
MSSM parameter space. The ranges of variation over MSSM parameters are shown in left panel
of Table 3 (all parameters in scan are real; “SUSY scale” refers to the common mass parameter
for the ﬁrst two squark generations; the trilinear soft breaking terms are set to At = Ab = M ˜QL
and A˜τ = M˜ℓ). Flavour violation is parametrized by the “mass insertions” 2, where I, J denote
quark ﬂavours, X, Y denote superﬁeld chirality, and Q indicates the sfermion ﬁeld:
δIJ
QXY
=
(M2
Q)IJ
XY
q
(M2
Q)IJ
XX(M2
Q)IJ
Y Y
.
(2)
Realistic estimate of the allowed range for B(B0
s →µ+µ−) requires taking into account
the experimental constraints from measurements of other rare decays. For that, all ∆F = 2
observables, B(B →Xsγ), B(KL →π0ν¯ν), B(K+ →π+ν¯ν) decay rates and the neutron and
electron electric dipole moments have been used out of quantities listed in Table 2. In addition,
bounds on SUSY particle masses listed in right panel of Table 3 have been used.
For the chosen bounds from Table 2 for which the experimental result and its error are
known, parameter point in scan was accepted if
|Qexp −Qth| ≤3∆Qexp + q|Qth|.
(3)
For the quantities for which only the upper bound is known,
(1 + q)|Qth| ≤Qexp
(4)
was required.
The ﬁrst and second terms on the right-hand side of Eq. 3 represent the 3σ
experimental error and the theoretical error respectively. The latter diﬀers from quantity to


## Page 4


Table 3: The range of input parameters and experimental constraints used for the numerical scan. All mass
parameters are in GeV.
Parameter
Min
Max
Step
tan β
2
30
varied
CKM phase γ
0
π
π/25
CP-odd Higgs MA
100
500
200
Higgs mixing µ
-450
450
300
SU(2) wino mass M2
100
500
200
Gluino mass M3
3M2
3M2
0
SUSY scale MSUSY
500
1000
500
Slepton Masses M˜ℓ
MSUSY
3
MSUSY
3
0
Left stop M ˜
QL
200
500
300
Right sbottom M˜bR
200
500
300
Right stop M˜tR
150
300
150
δ13
dLL, δ23
dLL
-1
1
0.1
δ13
dLR, δ23
dLR
-0.1
0.1
0.01
Mass
Constraint
mχ0
1
> 46
mχ±
1
> 94
m˜b
> 89
m˜t
> 95.7
mh
> 92.8-114 depending on sin2(α −β)
quantity and is usually smaller than the value q = 50% which was assume generically to account
for the limited density of a numerical scan (see ref. 6 for details).
Fig. 1 shows the predictions for B(B0
s →µ+µ−) over a general scan of 20 million points
according to Table 3. δ23
d LL (left panel) and δ23
d LR (right panel) were varied one at a time while
setting the other to zero, e.g. all δij
XY = 0 and only δ23
d LL ̸= 0 in the left panel. When δ23
d LL
is varied in the range [−1, 1], one ﬁnds B(B0
s →µ+µ−)min ≈10−9. This minimum is almost
independent of tan β. |δ23
d LL| can take on values up to ≈0.9 and still pass all imposed constraints,
though points beyond 0.3 are less dense. More interesting is the case when δ23
d LR is varied in
the range [−0.1, 0.1].
One can ﬁnd a narrow cancellation region around δ23
d LR ≈−0.01 and
tan β <∼10 where B(B0
s →µ+µ−)min ≈10−12. This is three orders of magnitude lower than the
SM prediction, making it eﬀectively unobservable at the LHC.
10-10
10-9
10-8
10-7
10-6
 5
 10
 15
 20
 25
 30
Br(Bs -> µ+ µ-)
tanβ
LL
10-12
10-11
10-10
10-9
10-8
10-7
10-6
 5
 10
 15
 20
 25
 30
Br(Bs -> µ+ µ-)
tanβ
LR
Figure 1:
Predictions for B(Bs →µ+µ−) vs tan β from the scan of MSSM parameters in Table 3. Left(right)
panel: δ23
d LL (δ23
d LR) varied. The dashed line shows the SM expectation.
4
Conclusions
I have presented SUSY FLAVOR, a tool capable of calculating simultaneously 29 important ﬂavor
observables in the general R-parity conserving MSSM. The calculation of the SUSY tree-level
particle spectrum and ﬂavor mixing matrices are performed exactly. SUSY FLAVOR v2 implements
also the resummation of chirally enhanced corrections, stemming from large values of tan β
and/or large trilinear A-terms. Thus SUSY FLAVOR v2 is valid for the whole parameter space


## Page 5


of the general R-parity conserving MSSM, without restrictions on the size of the oﬀ-diagonal
elements in the sfermion mass matrices - a unique feature currently not shared by other publicly
available programs calculating FCNC and CP violation in supersymmetric models. I hope that
SUSY FLAVOR becomes an important tool useful both for theorists and experimentalists who need
to perform multi-process ﬂavor analyses within the MSSM.
As an example of such analysis, SUSY FLAVOR has been used to perform a numerical explo-
ration of the MSSM parameter space and estimate of the B0
s →µ+µ−decay rate. Scan shows
that there exist cancellation regions where the contribution of diagrams with supersymmetric
particles interferes destructively with SM diagrams, thus allowing the branching ratio to be
signiﬁcantly smaller than the SM prediction. Such eﬀects may eﬀectively hide the dimuon B0
s
decay mode from the LHCb even though it is supposed to be one of the experiment’s benchmark
modes. Barring such cancellations, supersymmetric contributions typically tend to enhance the
branching ratio for B0
s →µ+µ−even for moderate values of tan β <∼10 so that an experimen-
tal measurement close to the SM prediction puts strong bounds on the size of allowed ﬂavour
violation in the squark sector.
SUSY FLAVOR can be downloaded from the address http://www.fuw.edu.pl/susy flavor.
References
1. G. D’Ambrosio, G. F. Giudice, G. Isidori and A. Strumia, Nucl. Phys. B 645, 2002 (155).
2. M. Misiak, S. Pokorski and J. Rosiek, “Supersymmetry and the FCNC eﬀects” Adv. Ser.
Direct. High Energy Phys. 15, 1998 (795) [arXiv:hep-ph/9703442];
3. S. Pokorski, J. Rosiek and C. Savoy, Nucl. Phys. B 570, 2000 (81); J. Rosiek, Acta Phys.
Polon. B 30, 1999 (3379); A. Buras, P. Chankowski, J. Rosiek and  L. S lawianowska, Nucl.
Phys. B 619, 2001 (434); J. Rosiek, arXiv:hep-ph/0108226; A. Buras, P. Chankowski,
J. Rosiek and  L. S lawianowska, Phys. Lett. B 546, 2002 (96); P. Chankowski and J. Rosiek,
Acta Phys. Polon. B 33, 2002 (2329); J. Rosiek, arXiv:0911.3339 [hep-ph].
4. A. Buras, P. Chankowski, J. Rosiek and  L. S lawianowska, Nucl. Phys. B 659, 2003 (3);
5. A. Dedes, J. Rosiek and P. Tanedo, Phys. Rev. D 79, 2009 (055006);
6. A. Buras, T. Ewerth, S. J¨ager and J. Rosiek, Nucl. Phys. B 714, 2005 (103);
7. J. Rosiek et al, Comput. Phys. Commun. 181, 2010 (2180).
8. A. Crivellin, J. Rosiek et al, arXiv:1203.5023 [hep-ph].
9. C. Hamzaoui, M. Pospelov and M. Toharia, Phys. Rev. D 59, 1999 (095005); M. Carena,
D. Garcia, U. Nierste and C. Wagner, Nucl.
Phys.
B 577, 2000 (88); K. Babu and
C. Kolda, Phys. Rev. Lett. 84, 2000 (228); G. Isidori and A. Retico, JHEP 0111, 2001
(001); A. Dedes and A. Pilaftsis, Phys. Rev. D 67, 2003 (015012).
10. A. Crivellin, L. Hofer and J. Rosiek, JHEP 1107, 2011 (017).
11. A. Dedes, H. Haber and J. Rosiek, JHEP 0711, 2007 (059).
12. P. Skands et al., JHEP 0407, 2004 (036); B. Allanach et al., Comput. Phys. Commun.
180, 2009 (8).
13. J. Rosiek, Phys. Rev. D 41, 1990 (3464); erratum arXiv:hep-ph/9511250.
14. “Search for the rare decays B(s) →µ+µ−at the LHC 0 with the ATLAS, CMS and LHCb
experiments”, LHCb-CONF-2012-017, CMS-PAS-BPH-12-009, ATLAS-CONF-2012-061.
15. M. Blanke, A. Buras, D. Guadagnoli and C. Tarantino, JHEP 0610, 2006 (003).

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]