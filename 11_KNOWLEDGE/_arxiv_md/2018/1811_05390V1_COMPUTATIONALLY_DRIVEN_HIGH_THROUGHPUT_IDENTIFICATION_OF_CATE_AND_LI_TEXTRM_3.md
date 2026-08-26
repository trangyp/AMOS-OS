---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.05390v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1811.05390v1_Computationally-driven__high_throughput_identification_of_CaTe_and_Li___textrm_3

> Source: 1811.05390v1_Computationally-driven__high_throughput_identification_of_CaTe_and_Li___textrm_3.pdf

> Pages: 26

---


## Page 1


Computationally-driven, high throughput identiﬁcation of CaTe and Li3Sb as
promising candidates for high mobility p-type transparent conducting materials
Viet-Anh Ha,1 Guodong Yu,1, ∗Francesco Ricci,1 Diana Dahliah,1 Michiel J. van
Setten,1, † Matteo Giantomassi,1 Gian-Marco Rignanese,1 and Geoﬀroy Hautier1, ‡
1Institute of Condensed Matter and Nanoscience (IMCN), Universit´e catholique de Louvain (UCLouvain),
Chemin ´etoiles 8, bte L7.03.01, Louvain-la-Neuve 1348, Belgium
(Dated: November 14, 2018)
High-performance p-type transparent conducting materials (TCMs) must exhibit a rare combi-
nation of properties including high mobility, transparency and p-type dopability. The development
of high-mobility/conductivity p-type TCMs is necessary for many applications such as solar cells,
or transparent electronic devices. Oxides have been traditionally considered as the most promising
chemical space to dig out novel p-type TCMs.
However, non-oxides might perform better than
traditional p-type TCMs (oxides) in terms of mobility. We report on a high-throughput (HT) com-
putational search for non-oxide p-type TCMs from a large dataset of more than 30,000 compounds
which identiﬁed CaTe and Li3Sb as very good candidates for high-mobility p-type TCMs. From our
calculations, both compounds are expected to be p-type dopable: intrinsically for Li3Sb while CaTe
would require extrinsic doping. Using electron-phonon computations, we estimate hole mobilities at
room-temperature to be about 20 and 70 cm2/Vs for CaTe and Li3Sb, respectively. The computed
hole mobility for Li3Sb is quite exceptional and comparable with the electron mobility in the best
n-type TCMs.
I.
INTRODUCTION
Transparent conducting materials (TCMs) are neces-
sary in many applications ranging from solar cells to
transparent electronics.
So far, n-type oxides (e.g.,
In2O3, SnO2 and ZnO) are the highest performing
TCMs, allowing them to be used in commercial de-
vices [1–5].
On the other hand, p-type TCMs show
poorer performances, especially in terms of carrier mo-
bility. This hinders the development of new technologies
such as transparent solar cells or transistors [3, 6]. Tak-
ing advantage of the predictive power of density func-
tional theory (DFT) calculations, we have set up a high-
throughput (HT) computational framework to identify
novel p-type TCMs focusing ﬁrst on oxide compounds [7–
9].
The analysis of the calculated HT data conﬁrmed that
on average p-type oxides have inherently higher eﬀec-
tive masses than n-type oxides [7]. This could be traced
back to the strong oxygen p-orbital character in the va-
lence band of most oxides and has rationalized the cur-
rent gap in mobility between the best p-type and n-type
oxides. This inherent diﬃculty in developing high-hole-
mobility oxides justiﬁes moving towards non-oxide TCM
chemistries including ﬂuorides [10], sulﬁdes [11, 12], ox-
ianions [13], or germanides [14].
Recently, we started
extending our HT computing approach to search for non-
oxide TCMs. Phosphides were identiﬁed to be among the
lowest hole eﬀective mass materials and more speciﬁcally
∗Present address:
School of Physics and Technology (SPT),
Wuhan University (WHU), Wuhan 430072, China
† Present address: IMEC, 75 Kapeldreef, B-3001 Leuven, Belgium
‡ E-mail: geoﬀroy.hautier@uclouvain.be
boron phosphide (BP) was detected as a very promising
p-type TCM candidate [15]. We note that subsequent
computational studies focusing on selected binaries and
ternaries reported also on the computational screening
of non-oxide TCMs [16, 17].
In the present work, we
extend our HT computing approach to a larger space
of chemistries and investigate some selected candidates.
We screen all non-oxide compounds in a large computa-
tional data set (>34,000 semiconductors) [18]. Combin-
ing DFT-based HT computations with higher accuracy
methods such as GW, hybrid functionals and electron-
phonon coupling computations (to assess the relaxation
time and thus the mobility), we identify that CaTe and
Li3Sb would be of great interest as high mobility p-type
TCMs.
II.
METHODS
All the considered materials originate from the Inor-
ganic Crystal Structure Database (ICSD) [19]. Their re-
laxed crystal structures and electronic band structures
were obtained from the Materials Project database [20,
21].
These rely on DFT high-throughput computa-
tions which were performed with VASP [22, 23] using
the Perdew-Burke-Ernzerhof (PBE) exchange-correlation
(XC) functional [24] within the projector augmented
wave (PAW) framework [25].
One of the ﬁrst selection criteria for TCMs is their sta-
bility. Here, it is assessed by the energy above hull Ehull
in the Materials Project database [20]. For a compound
stable at 0K, Ehull = 0 meV/atom, and the stability de-
creases as Ehull increases.
In the beginning of the screening procedure, the PBE
band gap can be used as a ﬁlter. However, since PBE
is known to systematically underestimate the band gap
arXiv:1811.05390v1  [cond-mat.mtrl-sci]  13 Nov 2018


## Page 2


2
compared to experiments, more accurate calculations are
needed in the subsequent steps (though with a limited
number of materials). So, the fundamental and direct
band gaps were also calculated with VASP for about
a hundred materials using the Heyd-Scuseria-Ernzerhof
(HSE) hybrid XC functional [26, 27] and adopting the
same computational parameters as for the PBE calcu-
lations.
For the ﬁnal candidates (CaTe and Li3Sb),
G0W0 calculations were performed with ABINIT [28–31].
In these calculations, optimized norm-conserving (NC)
pseudopotentials including semi-core electrons were used
which were generated with ONCVPSP [32, 33]. The ki-
netic cut-oﬀenergy for the wavefunctions were set to 51
and 52 Ha for CaTe and Li3Sb respectively, as recom-
mended in the PseudoDojo table [33]. The convergence
of these calculations with respect to the kinetic energy
cut-oﬀEc for the dielectric function and the number of
bands Nb was tested using automatic GW workﬂows [34]
based on the pymatgen [35] and AbiPy packages [31, 36].
For CaTe, the convergence of the gap at the Γ point (with
a truncation error smaller than 0.01 eV) was obtained
for Ec = 12 Ha and Nb = 480. In the case of Li3Sb,
the convergence is signiﬁcantly faster: using Ec = 10 Ha
and Nb = 240 guarantee a truncation error smaller than
0.01 eV. More details about the convergence tests are
available in the supplementary document. For the calcu-
lations of the screening and the quasi-particle self-energy,
10 × 10 × 10 and 8 × 8 × 8 k-point meshes were used
for CaTe and Li3Sb, respectively. The band structures
are then interpolated from these k-point meshes using
AbiPy [31, 36].
The point defect computations were performed using
the supercell technique [37] adopting 3 × 3 × 3 supercells
of the primitive cells. We calculated the defect forma-
tion energies ﬁrst using the PBE XC functional but also
with the more accurate HSE functional for Li3Sb and
CaTe [26, 27]. For the latter, the screening length and
fraction of exact exchange were set to the common val-
ues of 0.2 ˚A and 25 % respectively. The kinetic energy
cut-oﬀfor the wavefunctions was set to 19.1 Ha (520 eV)
and the relaxations are stopped when the change in total
energy between two ionic relaxation-steps is smaller than
3.67×10−4 Ha (0.01 eV). The formation energy of defect
D in charged state q can be written as [38, 39]
Ef[Dq] =E[Dq] + Ecorr[Dq] −E[bulk] −Σiniµi
+ q(ϵVBM + ∆v + ∆ϵF )
(1)
where E[Dq] and E[bulk] are the total energies of the
supercell with a defect D in the charge state q and with-
out any defects, respectively; ni is the number of atoms
of type i removed (ni < 0) or added (ni > 0); and,
µi is the corresponding chemical potential. ϵVBM is the
energy of the valence band maximum (VBM), and ∆ϵF
is the Fermi level referenced to ϵVBM.
The correction
terms Ecorr[Dq] and ∆v are introduced to take care of
the spurious image-charge interactions and the poten-
tial alignment for charged defects, respectively. The de-
fect states with the charge q were corrected using the
extended Freysoldt’s (Kumagai’s) scheme [40, 41].
All
defects computations were performed using the PyCDT
package [42].
The eﬀective masses were calculated with BoltzTrap
(based on Boltzmann transport theory framework) [43]
using the pymatgen [35] interface and the Fireworks
workﬂow package [44]. All the raw eﬀective mass data is
freely available in a separate paper which covers around
48,000 inorganic materials
[18]. The mobility depends
on the eﬀective mass m∗through µ = eτ/m∗where
the relaxation time τ (inverse of the scattering rate) de-
pends on diﬀerent scattering mechanisms. Carriers can
be scattered by phonons, ionized and neutral impurities,
grain boundaries,... In this work, we only took into ac-
count the scattering of electrons by phonons which is
likely to be an important component of scattering and
is an intrinsic mechanism, diﬃcult to control through
purity and microstructure.
The carriers scattering by
phonons can be computed theoretically if the electron-
phonon matrix elements are known. In principle, one can
employ Density Functional Perturbation Theory (DFPT)
to obtain all the electron-phonon matrix elements from
ﬁrst principles. However, converging the relevant phys-
ical properties (such as the scattering rate of electrons
by phonons) often requires very dense k-point and q-
point meshes for electrons and phonons respectively lead-
ing to a considerable increase of computational time.
The recently developed interpolation techniques based
on Wannier functions oﬀer a very practical and eﬃcient
solution to overcome this obstacle.
In this work, we
used the EPW code [45, 46] interfaced with Quantum
ESPRESSO [47, 48] to calculate the relaxation-time τnk
(n and k are band index and wave vector of a Bloch’s
state, respectively). More details on the theory and the
implementation can be found in Ref. 46. The τn,k were
interpolated on a dense 40 × 40 × 40 mesh for both k-
points (for electrons) and q-points (for phonons) starting
from the DFPT values on a 6 × 6 × 6 mesh. The latter
(together with the structural relaxation, self-consistent,
non self-consistent calculations which are needed to run
EPW) were obtained using Quantum ESPRESSO with
NC pseudopotentials and very stringent parameters for
convergence, e.g. high cut-oﬀenergy of 40 Ha. These τn,k
are then used as an input to compute the carrier mobility
by solving the Boltzmann transport equation by means of
the BoltzTrap package [43]. In the latter calculations, the
DFT band-energies (computed on a ﬁnite number of k-
points) are interpolated using star functions (see section 2
of Ref. 43). Here, we have implemented another interpo-
lation for the relaxation time in BoltzTrap in order to ob-
tain the same very dense k-point grid as the one used for
band-energies. The physical principle for this implemen-
tation is that the symmetries of the quasi-particle ener-
gies are the same as those of band-energies [49] (τn,k due
to the interaction with phonons can be calculated from
the imaginary part of the electron-phonon self-energy).


## Page 3


3
III.
RESULTS
Starting from the Materials Project database, our ﬁrst
step was to extract materials with a low hole eﬀective
mass (< 1 mo, where mo is the free electron mass) and
a large enough fundamental gap (> 0.5 eV) and direct
gap (> 1.5 eV), based on PBE calculations.
Regard-
ing the eﬀective masses, in the most general form, they
are represented by a tensor.
As most TCMs are used
as polycrystalline ﬁlms, materials with isotropic or close
to isotropic transport are easier to use in practical ap-
plications. Therefore, for the screening, we focus on the
three principal values of this tensor and sort the materi-
als based on the highest of the three principal hole eﬀec-
tive masses. There were about 390 compounds passing
through this ﬁrst ﬁlter.
We then screened out very unstable materials select-
ing only those with an energy above hull lower than
24 meV/atoms. This threshold corresponds to the typical
standard deviation of computational errors (compared
with experiment) of DFT formation-energies [50].
For
the 107 materials passing these criteria, more accurate
fundamental and direct gaps were calculated using the
HSE hybrid functional. All the results of this step are
presented in Table SI of the Supplemental Material [51].
For sake of clarity, Table I shows a selection of 63 mate-
rials with a direct band gap ≥2.8 eV. The materials are
sorted in decreasing order as a function of the computed
direct band gap.
TABLE I: Formula, space group, Materials Project identiﬁcation number (MP-id) [20, 21], fundamental Eg and direct gaps
Ed
g computed by HSE functional (in eV), energy above hull Ehull (in meV /atom), principal components m1, m2 and m3
of the hole eﬀective mass tensor (in atomic units), veriﬁcation of the absence of toxic/rare-earth (T/RE) elements (Be, As,
Cd, Yb, Hg, Pb and Th) and of the p-type dopability (when computed here or obtained from the existing literature) for the
selected compounds (see text). The materials are sorted as a function of the direct band gap in decreasing order.
Formula
Space group
MP-id
Ed
g
Eg
Ehull
m1
m2
m3
T/RE
p-dopability
BeS
F43m
422
6.89
4.05
0.0
0.65
0.65
0.65
×
-
KMgH3
Pm3m
23737
5.76
3.58
0.0
0.75
0.75
0.75
✓
-
SiC
F43m
8062
5.75
2.25
0.7
0.58
0.58
0.58
✓
✓[52–55]
CsPbCl3
Amm2
675524
5.69
5.69
0.0
0.30
0.32
0.33
×
-
BeSe
F43m
1541
5.27
3.36
0.0
0.55
0.55
0.55
×
-
BeCN2
I42d
15703
5.21
5.21
0.0
0.75
0.75
0.78
×
-
RbPbF3
Cc
674508
5.20
4.84
0.0
0.71
0.83
0.95
×
-
MgS
Fm3m
1315
4.95
3.84
0.0
0.98
0.98
0.98
✓
-
RbHgF3
Pm3m
7482
4.90
2.11
0.0
0.93
0.93
0.93
×
-
AgCl
Fm3m
22922
4.81
2.28
0.0
0.83
0.83
0.83
✓
-
CsHgF3
Pm3m
561947
4.59
2.20
0.0
0.89
0.89
0.89
×
-
Be2C
Fm3m
1569
4.56
1.63
0.0
0.37
0.37
0.37
×
-
SrMgH4
Cmc21
643009
4.52
3.78
0.0
0.84
0.90
0.95
✓
-
Li2Se
Fm3m
2286
4.36
3.70
0.0
0.95
0.95
0.95
✓
-
BP
F43m
1479
4.35
2.26
0.0
0.34
0.34
0.34
✓
✓[15]
CaS
Fm3m
1672
4.28
3.34
0.0
0.88
0.88
0.88
✓
-
LiCa4B3N6
Im3m
6799
4.25
3.38
0.0
0.86
0.86
0.86
✓
-
BaSrI4
R3m
754852
4.22
4.22
21.8
0.73
0.73
0.80
✓
-
LiSr4B3N6
Im3m
9723
4.18
3.22
0.0
0.89
0.89
0.89
✓
-
NaSr4B3N6
Im3m
10811
4.08
3.14
0.0
0.92
0.92
0.92
✓
-
K2LiAlH6
Fm3m
24411
4.04
3.70
9.1
0.65
0.65
0.65
✓
-
BeTe
F43m
252
4.04
2.45
0.0
0.42
0.42
0.42
×
-
Ba3SrI8
I4/mmm
756235
4.02
4.02
7.5
0.70
0.81
0.81
✓
-
CaSe
Fm3m
1415
4.01
2.95
0.0
0.77
0.77
0.77
✓
-
LiH
Fm3m
23703
3.97
3.97
0.0
0.46
0.46
0.46
✓
×
AlP
F43m
1550
3.90
2.50
0.0
0.56
0.56
0.56
✓
×
YbS
Fm3m
1820
3.76
2.96
0.0
0.76
0.76
0.76
×
-
Na2LiAlH6
Fm3m
644092
3.75
3.75
3.9
0.66
0.66
0.66
✓
-
SrSe
Fm3m
2758
3.68
3.03
0.0
0.83
0.83
0.83
✓
-
BaLiH3
Pm3m
23818
3.62
3.26
0.0
0.36
0.36
0.36
✓
×
CsPbF3
Pm3m
5811
3.59
3.59
4.6
0.39
0.39
0.39
×
-
Cs3ZnH5
I4/mcm
643702
3.58
3.58
0.0
0.69
0.93
0.93
✓
-
Al2CdS4
Fd3m
9993
3.56
3.55
20.0
0.78
0.78
0.78
×
-
K2LiAlH6
R3m
23774
3.52
3.52
0.0
0.68
0.84
0.84
✓
-
BaMgH4
Cmcm
643718
3.51
3.26
4.8
0.48
0.55
0.70
✓
-
CaTe
Fm3m
1519
3.50
2.18
0.0
0.60
0.60
0.60
✓
✓
Cs3MgH5
P4/ncc
23947
3.49
3.49
0.3
0.88
0.93
0.93
✓
-
Cs3MgH5
I4/mcm
643895
3.49
3.49
0.0
0.83
0.94
0.94
✓
-
Continued on next page


## Page 4


4
TABLE I – continued from previous page
Formula
Space group
MP-id
Ed
g
Eg
Ehull
m1
m2
m3
T/RE
p-dopability
YbSe
Fm3m
286
3.48
2.43
0.0
0.67
0.67
0.67
×
-
ZnS
F43m
10695
3.46
3.46
0.0
0.81
0.81
0.81
✓
✓[12]
TaCu3S4
P43m
10748
3.46
2.95
0.0
0.98
0.98
0.98
✓
-
Al2ZnS4
Fd3m
4842
3.46
3.43
0.0
0.66
0.66
0.66
✓
×
Li2ThN2
P3m1
27487
3.46
3.33
0.0
0.85
0.95
0.95
×
-
Mg2B24C
P4n2
568556
3.42
3.41
0.0
0.77
0.93
0.93
✓
-
Li2GePbS4
I42m
19896
3.33
3.20
0.0
0.61
0.61
0.98
×
-
Cs3H5Pd
P4/mbm
643006
3.32
3.09
0.0
0.79
0.83
0.83
✓
-
SrTe
Fm3m
1958
3.24
2.39
0.0
0.67
0.67
0.67
✓
×
MgTe
F43m
13033
3.24
3.24
0.9
0.95
0.95
0.95
✓
-
CsTaN2
I42d
34293
3.22
3.22
0.0
0.71
0.71
0.92
✓
-
Cs3MnH5
I4/mcm
643706
3.21
3.18
0.0
0.82
0.96
0.96
✓
-
LiMgP
F43m
36111
3.18
2.00
0.0
0.65
0.65
0.65
✓
-
BaS
Fm3m
1500
3.17
3.02
0.0
0.85
0.85
0.85
✓
-
LiAlTe2
I42d
4586
3.11
3.11
0.0
0.52
0.83
0.83
✓
-
YbTe
Fm3m
1779
3.09
1.76
0.0
0.54
0.54
0.54
×
-
Li3Sb
Fm3m
2074
3.06
1.15
0.0
0.24
0.24
0.24
✓
✓
SrAl2Te4
I422
37091
3.06
2.66
0.0
0.42
0.79
0.80
✓
-
TaCu3Te4
P43m
9295
3.05
2.50
0.0
0.63
0.63
0.63
✓
-
TaCu3Se4
P43m
4081
2.98
2.43
0.0
0.82
0.82
0.82
✓
-
BaSe
Fm3m
1253
2.95
2.59
0.0
0.76
0.76
0.76
✓
-
KAg2PS4
I42m
12532
2.87
2.53
0.0
0.67
0.82
0.82
✓
-
AlAs
F43m
2172
2.84
2.12
0.0
0.50
0.50
0.50
×
-
LiErS2
I41/amd
35591
2.80
2.80
10.4
0.62
0.99
0.99
✓
-
GaN
F43m
830
2.80
2.80
5.2
0.94
0.94
0.94
✓
-
Among the materials at the top of the list, SiC is a
well-known wide band gap semiconductor. This material
exhibits polymorphism (e.g. cubic: 3C, Rhombohedral:
15R, hexagonal: 6H, 4H, 2H) [56] and can be doped both
n- and p-type [52–55]. A high hole mobility of 40 cm2/Vs
was obtained for the cubic phase [57]. The indirect opti-
cal absorption of cubic phase is very weak at room tem-
perature with a coeﬃcient of 103 cm−1 at 3.1 eV [58].
We suggest that SiC can be considered as a good p-type
TCM. The main disadvantage of this compound is the
diﬃculty of hole doping. Most known impurities such as
Al, B, Ga and Sc create deep doping-levels leading to
rather low concentrations of holes which were typically
measured to be lower than 1018 cm−3 [57] and is suitable
for transistor applications.
Next comes a series of beryllium based compounds
(BeS, BeSe, BeCN2, Be2C and BeTe). While their com-
puted performance in terms of band gap and hole eﬀec-
tive masses are very attractive, the toxicity of beryllium
lowers their interest for technological applications. Like-
wise, the many lead-based halide perovskites (CsPbCl3,
RbPbF3, and CsPbF3) and Li2GePbS4 also present tox-
icity issues. It is interesting however to see these halide
perovskites being of great interest as solar absorbers
when they are made in chemistries showing smaller
gaps [59, 60]. Toxicity is also an issue with the series of
arsenides, e.g. AlAs. These arsenides are also very anal-
ogous to the phosphides such as BP and AlP that were
identiﬁed in a previous work [15]. Some of the materi-
als in the list contain rare-earth elements which might
present some cost issues. We consider that further as-
sessment of all these materials in terms of dopability and
mobility is not a priority. Therefore, in the penultimate
column of Table I, the absence of toxic or rare-earth ele-
ments is veriﬁed, as indicated by a checkmark.
Continuing to explore the list of materials, many hy-
drides appear to be of interest with low hole eﬀective
mass and large direct band gaps for LiH, BaLiH3 and
CsH. Unfortunately, our subsequent defect computations
indicate that these hydrides have low-lying hole-killing
defects especially the hydrogen vacancy making unlikely
their eﬃcient p-type doping (see the Supplemental Ma-
terial [51]).
A few sulﬁdes are also identiﬁed by our
screening: ZnS and ZnAl2S4. ZnS has been indeed re-
cently studied as a good performance p-type TCM [12].
ZnAl2S4, on the other hand, is less studied but our defect
computation indicates that it is very unlikely to be p-type
dopable because Zn-Al anti-site defects form easily and
act as hole-killers. Al2CdS4 is likely to present the same
issues. The defect formation energies computed by DFT
for ZnAl2S4 are given in the Supplemental Material [51].
Among the diﬀerent materials in the table, two promis-
ing candidates, Li3Sb and CaTe, also attracted our at-
tention. The rest of the paper is dedicated to the further
computations that were performed for these compounds.
The conventional cells of CaTe and Li3Sb are shown
in Fig. 1 (a) and (e). Ca atoms in CaTe are surrounded
by six Te atoms forming an octahedral local environment.
In Li3Sb, the cation ﬁlls tetrahedral and octahedral sites.
Both CaTe and Li3Sb are cubic phases with high sym-
metry, which explains for their isotropy in hole eﬀective


## Page 5


5
masses (m1 = m2 = m3). CaTe and Li3Sb exhibit very
low hole eﬀective masses with the eigenvalues being 0.60
and 0.25 mo (mo-mass of free electron), respectively. It is
worth noting that the lowest hole eﬀective masses found
so far in a computational database for a p-type conduct-
ing oxides K2Sn2O3 [7, 61] is 0.27 mo. The promising
non-oxide p-type TCM reported recently [15], BP, shows
an eﬀective mass around 0.35 mo. Current Cu-based p-
type TCOs show eﬀective masses around 1.5 to 2 mo [7].
The direct gaps of CaTe and Li3Sb calculated using HSE
hybrid functional are 3.5 and 3.06 eV respectively. Next
to hybrid functional computations, we performed G0W0
to conﬁrm the value of these band gaps.
Fig. 1 (b) shows DFT band structure with a scissor
shift to ﬁt G0W0 fundamental gap (G0W0 band structure
of CaTe is shown in Fig. S6 of the Supplemental Mate-
rial [51]). The G0W0 fundamental gap (Γ−X) is 2.95 eV
while the direct gap is located at X-point and has a value
of 4.14 eV. The G0W0 direct gap is consistent with the
optical gap of 4.1 eV measured experimentally [62]. We
expect such a large band gap to lead to transparency in
the visible region. Li3Sb is also an indirect semiconduc-
tor. In the same way, the DFT electronic band structure
with a scissor shift is presented in Fig. 1 (f) (see Fig. S7
of the Supplemental Material [51] for G0W0 band struc-
ture). The G0W0 band gap and direct gap are 1.37 and
3.17 eV, respectively. The G0W0 direct gap (located at
the Γ-point) of 3.17 eV. This is consistent with a ex-
perimental value of 3.1 eV measured recently [63] but
much lower than another experimental value of 3.9 eV
reported earlier [64]. The indirect band gap is narrow
and will lead to some absorption in the visible range.
However, the indirect nature of the absorption makes it
phonon-assisted and is expected to lead to weak absorp-
tion. To quantify this absorption, we computed the opti-
cal absorption including phonon-assisted processes using
EPW [45, 46]. Details about computational method can
be found in Ref. 65. The result in Fig. 2 shows quite
weak absorption in the visible range with the average in-
tensity about 5 × 103 cm−1, which means that a 100-nm
ﬁlm still allows more than 70 % of visible light energy
to get through. This is suitable for applications and de-
vices using thin-ﬁlm form of Li3Sb. The weak indirect
optical absorption computed here is similar to that of
established p-type TCOs such as SnO [66] or recently
proposed p-type TCMs such as BP [15].
CaTe and Li3Sb show very low hole eﬀective mass (0.60
and 0.24 mo within DFT). Indeed, both materials have
threefold degeneracy at VBM (Γ point), therefore, the
transport of holes occurs in three bands with some lighter
and some heavier. Our deﬁnition of eﬀective mass takes
into account the competition among these three bands
and give an average value that is representative of the
transport which will happen in the diﬀerent bands. More
details about formulas and calculation techniques can be
found in Ref. [18, 67]. This should be kept in mind when
comparing our results to other studies which sometimes
only focus on one band when several competing bands are
present [16, 68]. Fig. 1 shows projected density of states
(DOS) for (c) CaTe and (g) Li3Sb. For both compounds,
the top of valence band is mainly of anionic p-orbital
characters (Sb3– or Te2–) with some mixing from the
cations. The eﬀective masses are directly related to over-
lap and energy diﬀerence between orbitals [67]. The lower
value of hole eﬀective masses obtained in these non-oxide
compounds can be associated to both a better alignment
between the anionic and cationic states than in oxides
and larger anionic p-orbitals (5p and 4p versus 2p for
oxides).
The eﬀective mass is an important factor driving car-
rier mobility but not the only one.
Scattering rate or
relaxation time also aﬀects the mobility. There are sev-
eral mechanisms which can inﬂuence relaxation time as
mentioned in II. Phonon scattering is the most intrinsic
factor as it is not aﬀected by purity and microstructure.
The evaluation of relaxation time from phonon scattering
can be performed ab initio using electron-phonon cou-
pling matrices obtained from DFPT phonon computa-
tions. Fig. 3 shows phonon band structures (fat bands)
and projected DOS of phonons for (a) CaTe and (b)
Li3Sb. The fat bands represent qualitatively character-
istics of vibrational modes including what type of atoms
participates in the phonon modes at a given energy, their
direction and amplitude. The absence of modes with neg-
ative (purely imaginary) frequencies show that these ma-
terials are dynamically stable at 0 K. The lighter atoms
(Ca and Li) mainly contribute to the optical modes at
high frequencies (3 and 9 modes in CaTe and Li3Sb, re-
spectively) while the heavier elements (Te and Sb) play
an important role in the three acoustic modes at low fre-
quencies.
Using the DFPT phonon computations and EPW, we
can extract electron-phonon coupling matrices and the
relaxation time τnk on a dense k-point grid (see Eq. S1
of the Supplemental Material [51]). Fig. 1 (d) and (h)
show the scattering rate and lifetime (inverse of scatter-
ing rate) as a function of energy at 300 K for CaTe and
Li3Sb respectively (see Eq. S2 of the Supplemental Ma-
terial [51]). As commonly observed, the scattering rate is
proportional to the DOS. A higher DOS oﬀer more states
available for the scattered electrons. At the doping hole
concentration of 1018 cm−3, the Fermi levels are 90.5 and
120.8 meV above the VBMs for CaTe and Li3Sb, respec-
tively. For the highest doping of 1021 cm−3, the Fermi
levels lie below VBMs of 264.5 and 168.5 meV for CaTe
and Li3Sb, respectively. The transport of holes, there-
fore, takes place around VBMs (Γ-points). The DOS at
Γ-point of Li3Sb is larger than that of CaTe but the scat-
tering rate of Li3Sb are fairly similar (see Fig. 1 (d) and
(h)) indicating that a slightly weaker electron-phonon
coupling is present in Li3Sb.
We computed scattering rates at temperatures of 300
and 400 K. Fig. 4 shows the hole mobilities as a func-
tion of hole concentrations at 300 and 400 K for both
CaTe and Li3Sb. The mobilities decreases with hole con-
centrations. As the Fermi levels shifts deeper below the


## Page 6


6
τ (fs)
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
0
5
10
15
0
1
2
3
4
5
1/τ (x 1014 s-1)
(h)
(d)
DOS (states/eV)
0
1
2
total
Sb-p
Sb-d
Li-d
Li-p
Li-s
(g)
0
1
2
Ca-s
Ca-p
Ca-d
Te-p
Te-d
total
(c)
Wave vector
Γ
X W K
Γ
L
U W
L
K
-4
-2
0
2
4
E (eV)
(f)
Γ
X W K
Γ
L
U W
L
K
-4
-2
0
2
4
6
E (eV)
(b)
(e)
(a)
Conventional cell
FIG. 1. From the left to the right, the conventional cells, band structures, projected density of states (DOS) and relaxation
time and scattering rate. Sub-ﬁgures (a)-(d) and (e)-(h) show data of CaTe and Li3Sb respectively. The conventional cells
present local environments around cations Ca (blue) and Li (green). (b) and (f) plot DFT band structures with a rigid shift
of the conduction bands (scissor operator) to ﬁt the fundamental gaps computed by G0W0. (d) and (h) show relaxation time
τ (in femto-second) and scattering rate 1/τ (in 1/second) as functions of energy at temperature 300 K. The projected DOS in
(c) and (g) are computed by DFT. The band gaps of DOS and relaxation time are also shifted to ﬁt G0W0 values.
Energy (eV)
0.0
0.5
1.0
1.5
2.0
2.5
3.0
10-2
10-1
100
101
102
103
104
α (cm-1)
FIG. 2.
The indirect optical absorption of Li3Sb due to
phonon-assisted transitions.
VBMs, the DOS increases as well as the scattering rate
(see Fig. 1 (d) and (h)). CaTe shows values of hole mo-
bility around 20 cm2/Vs that is comparable with the mo-
bility of Ba2BiTaO6, a recently reported p-type TCO [9],
and larger than mobilities of the traditional p-type TCOs
such as CuAlO2 [69] and SnO [70].
Li3Sb exhibits an
exceptional hole mobility up to about 70 cm2/Vs at
room-temperature.
This value nearly reaches the val-
ues of the electron mobilities of the best current n-TCOs
such as SnO2, ZnO, In2O3 and Ga2O3 which are around
100 cm2/Vs (see Table SII of the Supplemental Mate-
rial [51]).
It is worth noting that the mobility mea-
sured experimentally take into account other scattering
processes.
Our computed mobilities as they only take
into account phonon scattering can be seen as an upper
bound.
Our ﬁnal assessment focuses on the dopability of CaTe
and Li3Sb. While we have assumed so far that the Fermi
level of these two materials could be tuned to generate
hole carriers, it remains to be seen if the defect chemistry
is favorable to hole generation. To answer this question,
we performed defect calculations using a HSE following
the procedure described in section II. Fig. 5 (a) presents
the defect formation energy for both intrinsic and extrin-
sic defects for each sort of defect in CaTe. The chemical
potentials are chosen in conditions which lead to the most
favorable p-type doping tendency for this material. The
chemical potentials corresponding to diﬀerent conditions
in the phase diagrams are available in Fig.
S8 of the
Supplemental Material [51]. Focusing ﬁrst on intrinsic
defects only including vacancies, anti-site defects and in-
terstitial atoms, defect formation energies of these are
plotted in Fig. 5 (a) with chemical potentials extracted
in Te-rich condition of the phase diagram. Intrinsically,
CaTe is unlikely to present p-type doping as no intrinsic


## Page 7


7
0
10
20
30
0
10
20
30
Ca
Te
0
20
40
60
0
20
40
60
Sb
Li
Energy (meV)
Energy (meV)
Energy (meV)
Energy (meV)
Phonon DOS
Phonon DOS
(b)
(a)
X WK
L
K W
Γ
Γ
L
K
X WK
L
K W
Γ
Γ
L
K
FIG. 3. Phonon band structures with fat bands representing displacements of atomic vibrations. The width of fat bands gives
qualitative understanding of the vibrational modes such as what are the atomic types involved in the vibrations at a given
energy, their direction of oscillation and the amplitude (related to the displacement). The projected DOS of phonons on each
type of atom are correspondingly shown next to the band structures. (a) CaTe and (b) Li3Sb.
μh (cm2/V.s)
nh (cm-3)
CaTe
Li3Sb
1018
1019
1020
1021
300 (K)
400 (K)
400 (K)
300 (K)
70
60
50
40
30
20
10
0
FIG. 4. Hole mobilities as a function of hole concentrations
of CaTe and Li3Sb at temperatures 300 and 400 K.
defect acts as a low lying acceptor. The vacancy of Ca
will be in competition with the hole killing vacancy of Te
leading to a fermi level far from the valence band. How-
ever, the Te vacancy is not low enough in energy that
it would prevent extrinsic p-type doping. When extrin-
sic defects with Na, K and Li substituting onto Ca-sites
are considered, we ﬁnd that all these substitutions of-
fer shallow acceptor very competitive compared to the
Te vacancy. The Ca by Na substitution is the lowest in
energy. Extrinsic doping by Na might therefore lead to
p-type doping in CaTe. The plots of formation energies
of KCa, NaCa and LiCa in Fig. 5 (a) were achieved with
chemical potentials extracted from KTe−CaTe−K2Te3,
NaTe3−CaTe−Na2Te and Li2Te−CaTe−Te facets of the
three-element phase diagrams (see Fig. S8 of the Sup-
plemental Material [51]). For Li3Sb, Fig. 5 (b) shows an
intrinsic tendency for hole doping with the lithium va-
cancy (VacLi) acting as a shallow acceptor with a very
low formation energy and no competing hole-killer. This
plot is produced with chemical potentials computed in
Li3Sb−Li2Sb facet of the phase diagram (see Fig. S9 of
the Supplemental Material [51]).
IV.
DISCUSSIONS
The discovery of the quite unanticipated Li3Sb with
a potential for very high hole mobility demonstrates the
interest of our HT screening strategy. Li3Sb is an unex-
pected compound for TCM applications and would have
been diﬃcult to intuitively identify. Among other A3B
compounds (A = Li, Na, K and Rb; and B = N, P, As and
Sb), Li3Sb is exceptional because of its very low hole ef-
fective masses (see Table SIII in the Supplemental Mate-
rial [51]). We suggest that the energy diﬀerence between
A-ns1 (n = 2, 3, 4, 5 for Li, Na, K and Rb, respectively)
and B-np3 (n = 2, 3, 4, 5 for N, P, As and Sb, respec-
tively) orbitals of valence electrons (A and B) might play
important role here. In fact, the energy diﬀerence be-
tween Li-2s1 and Sb-5p3 is about 1.954 (eV) [33] and is
the smallest value among many other ones of A-ns1/B-
np3 pairs.
This leads to a small orbital-energy diﬀer-
ence and strong s/p (anti-)bonding, which results in low
hole eﬀective mass. While we only focus on CaTe and
Li3Sb as they are likely the most potential candidates,
there are other interesting materials with hole eﬀective
masses from 0.6 to 1.0 mo and high direct gaps (see Ta-
ble I) such as CaS, SrSe, SrTe, LiCa4B3N6, LiSr4B3N6,
NaSr4B3N6...
Defects calculations for these materials
have not performed in this work and we, therefore, can-
not adjudge their p-type doping-tendency.
By going beyond oxides, we identiﬁed compounds with
very high hole mobility.
However, several other issues
also arise and need to be considered. The processing of
antimonides or tellurides might be more diﬃcult than


## Page 8


8
VacCa
VacTe
TeCa
CaTe
NaCa
KCa
LiCa
Cai(tet,Te4)
Tei(tet,Te4)
Fermi energy (eV)
Defect formation energy (eV)
0.0
0.5
1.0
1.5
2.0
-1
0
1
2
3
4
0
-1
VacLi-1
VacLi-2
VacSb
LiSb
SbLi-1
SbLi-2
Lii(oct,Sb2Li4)
Lii(oct,SbLi5)
Sbi(oct,Sb2Li4)
Sbi(oct,SbLi5)
Fermi energy (eV)
0.0
0.2
0.4
0.6
0.8
1.0
-1
0
1
2
3
4
Defect formation energy (eV)
0
-1
0
-1
+1
+2
0
0
-1
-2
0
+1
+2
+2
0
-1
0
-1
0
0
+1
+2
-1
0
+1
+1
0
0
-1
+1
0
+1
+2
(a)
(b)
FIG. 5. The defect formation energy as a function of Fermi level of intrinsic and extrinsic defects for (a) CaTe and (b) Li3Sb.
For CaTe, the intrinsic defects include vacancies (VacCa and VacTe), anti-sites (TeCa and CaTe) and interstitial atoms inserted
into the tetrahedral hollows formed by 4 Te atoms (Cai(tet,Te4) and Tei(tet,Te4)) while Na, K and Li are used as the extrinsic
defects substituting Ca atoms (NaCa, KCa and LiCa). For Li3Sb, the intrinsic defects include vacancies (VacLi-1, VacLi-2 and
VacSb), anti-sites (LiSb, SbLi-1 and SbLi-2) and interstitial atoms inserted into the octahedral hollows formed by Sb and Li
atoms (Lii(oct, Sb2Li4), Lii(oct, SbLi5), Sbi(oct, Sb2Li4) and Sbi(oct, SbLi5)). In both cases, the VBM is set to zero.
oxides.
They are, however, very common chemistries
in other applications such as thermoelectrics with sev-
eral exemplary compounds such as PbTe, Bi2Te3 [71], or
more recently Mg3Sb2 [72–74]. The band gaps in non-
oxide compounds are narrower, which lowers in average
their transparency in the visible light. As we already dis-
cussed [15], this can be overcome by exploiting the indi-
rect gaps and weak phonon-assisted optical transitions.
Lower band gaps are useful for p-dopability though as
lower band gap materials tend to be easier to dope [75].
We note that the defect chemistry of non-oxide can
be diﬀerent than in traditional TCOs. For oxides, the
cation-anion anti-site defects (replacement of anions on
cations’ sites and vice versa) are unlikely to be favor-
able energetically because of the large electronegativity
diﬀerence between cations and anions. In non-oxide com-
pounds, e.g. CaTe, the cation-anion anti-sites are more
likely to be present leading to potentially diﬀerent hole-
killing defects.
While the anion (oxygen) vacancy va-
cancy is the most common hole-killer in oxides, we see
our non-oxide materials presenting anti-sites cation-anion
defects lower in energy than the anion vacancy such as in
CaTe. We also identify that the hydride chemistry while
oﬀering attractive electronic structures presents dopabil-
ity issues (i.e., a low lying hydrogen vacancy acting as
hole killer) preventing them for further consideration in
p-type TCMs.
V.
CONCLUSIONS
Using a large database and appropriate ﬁltering strate-
gies, we report on a high-throughput search for non-oxide
p-type TCMs. We identiﬁed two materials to be of inter-
est: CaTe and Li3Sb. We performed extensive follow-up
computational investigation of these candidates, evaluat-
ing their band structure using beyond DFT techniques,
their transport and phonon-assisted optical properties
using electron-phonon computations as well as their de-
fect chemistry. Both CaTe and Li3Sb present very attrac-
tive properties for p-type TCM applications. The Li3Sb
shows a very high hole mobility of around 70 cm2/Vs,
which is close to electron mobility in the best n-type
TCMs. Our work motivates further experimental inves-
tigation of these two materials for TCM applications.
VI.
ACKNOWLEDGMENTS
V.-A.H. was funded through a grant from the FRIA.
G.-M.R. is grateful to the F.R.S.-FNRS for ﬁnancial
support.
G.H., G.-M.R., G.Y. and F.R. acknowledge
the F.R.S.-FNRS project HTBaSE (contract N◦PDR-
T.1071.15) for ﬁnancial support. We acknowledge access
to various computational resources: the Tier-1 supercom-
puter of the F´ed´eration Wallonie-Bruxelles funded by the
Walloon Region (grant agreement N◦1117545), and all
the facilities provided by the Universit´e catholique de


## Page 9


9
Louvain (CISM/UCLouvain) and by the Consortium des
´Equipements de Calcul Intensif en F´ed´eration Wallonie
Bruxelles (C´ECI). The authors thank Dr. Samuel Ponc´e
and Professor Emmanouil Kioupakis for helpful discus-
sions on the technical aspects of the electron-phonon
computations.
[1] H. Ohta and H. Hosono, Mater. Today 7, 42 (2004).
[2] A. Facchetti and T. J. Marks, eds., “Transparent elec-
tronics: From synthesis to applications,” (Wiley, 2010).
[3] K. Ellmer, Nat. Photonics 6, 809 (2012).
[4] P. Barquinha, R. Martins, L. Pereira,
and E. Fortu-
nato, “Transparent oxide electronics: From materials to
devices,” (Wiley, 2012).
[5] E. Fortunato, P. Barquinha,
and R. Martins, Adv.
Mater. 24, 2945 (2012).
[6] S. C. Dixon, D. O. Scanlon, C. J. Carmalt,
and I. P.
Parkin, J. Mater. Chem. C 4, 6946 (2016).
[7] G. Hautier, A. Miglio, G. Ceder, G.-M. Rignanese, and
X. Gonze, Nat. Commun. 4, 2292 (2013).
[8] J. B. Varley, V. Lordi, A. Miglio, and G. Hautier, Phys.
Rev. B 90, 045205 (2014).
[9] A. Bhatia, G. Hautier, T. Nilgianskul, A. Miglio, J. Sun,
H. J. Kim, K. H. Kim, S. Chen, G.-M. Rignanese,
X. Gonze, and J. Suntivich, Chem. Mater. 28, 30 (2016).
[10] H. Yanagi, J. Tate, S. Park, C.-H. Park, and D. Keszler,
Appl. Phys. Lett. 82, 2814 (2003).
[11] S. Park, D. A. Keszler, M. M. Valencia, R. L. Hoﬀman,
J. P. Bender,
and J. F. Wager, Appl. Phys. Lett. 80,
4393 (2002).
[12] R. Woods-Robinson, J. K. Cooper, X. Xu, L. T. Schelhas,
V. L. Pool, A. Faghaninia, C. S. Lo, M. F. Toney, I. D.
Sharp, and J. W. Ager, Adv. Electron. Mater. 2, 1500396
(2016).
[13] K. Ueda,
S. Inoue,
S. Hirose,
H. Kawazoe,
and
H. Hosono, Appl. Phys. Lett. 77, 2701 (2000).
[14] F. Yan, X. Zhang, Y. G. Yu, L. Yu, A. Nagaraja, T. O.
Mason, and A. Zunger, Nat. Commun. 6, 7308 (2015).
[15] J. B. Varley, A. Miglio, V.-A. Ha, M. J. van Setten, G.-
M. Rignanese, and G. Hautier, Chem. Mater. 29, 2568
(2017).
[16] R. K. M. Raghupathy, T. D. K¨uhne, C. Felser,
and
H. Mirhosseini, J. Mater. Chem. C 6, 541 (2018).
[17] R. K. M. Raghupathy, H. Wiebeler, T. D. K¨uhne,
C. Felser,
and H. Mirhosseini, Chem. Mater.
(2018),
10.1021/acs.chemmater.8b02719.
[18] F. Ricci, W. Chen, U. Aydemir, G. J. rey Snyder, G.-M.
Rignanese, A. Jain, and G. Hautier, Sci. Data 4, 170085
(2017).
[19] “Inorganic Crystal Structure Database,” https://www.
fiz-karlsruhe.de/de/leistungen/kristallographie/
icsd.html (2013), [FIZ Karlsruhe: Karlsruhe, Germany,
2013].
[20] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards,
S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder,
and K. A. Persson, APL Materials 1, 011002 (2013).
[21] “The
Materials
Project,”
https://www.
materialsproject.org/
(2013),
[accessed
Septem-
ber 1, 2013].
[22] G. Kresse and J. Furthm¨uller, Comput. Mater. Sci. 6, 15
(1996).
[23] G. Kresse and J. Furthm¨uller, Phys. Rev. B 54, 11169
(1996).
[24] J. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett.
77, 3865 (1996).
[25] P. E. Bl¨ochl, Phys. Rev. B 50, 17953 (1994).
[26] J. Heyd, G. E. Scuseria,
and M. Ernzerhof, J. Chem.
Phys. 118, 8207 (2003).
[27] E. N. Brothers,
A. F. Izmaylov,
J. O. Normand,
V. Barone,
and G. E. Scuseria, J. Chem. Phys. 129,
011102 (2008).
[28] X. Gonze,
J.-M. Beuken,
R. Caracas,
F. Detraux,
M. Fuchs, G.-M. Rignanese, L. Sindic, M. Verstraete,
G. Zerah, F. Jollet, M. Torrent, A. Roy, M. Mikami,
P. Ghosez, J.-Y. Raty, and D. C. Allan, Comput. Mater.
Sci. 25, 478 (2002).
[29] X. Gonze, Z. Kristallogr. 202, 558 (2005).
[30] X. Gonze, B. Amadon, P.-M. Anglade, J.-M. Beuken,
F. Bottin, P. Boulanger, F. Bruneval, D. Caliste, R. Cara-
cas, M. Cˆot´e, T. Deutsch, L. Genovese, P. Ghosez, M. Gi-
antomassi, S. Goedecker, D. R. Hamann, P. Hermet,
F. Jollet, G. Jomard, S. Leroux, M. Mancini, S. Mazevet,
M. J. T. Oliveira, G. Onida, Y. Pouillon, T. Rangel, G.-
M. Rignanese, D. Sangalli, R. Shaltaf, M. Torrent, M. J.
Verstraete, G. Zerah,
and J. W. Zwanziger, Comput.
Phys. Commun. 180, 2582 (2009).
[31] X. Gonze, F. Jollet, F. A. Araujo, D. Adams, B. Amadon,
T. Applencourt, C. Audouze, J.-M. Beuken, J. Bieder,
A. Bokhanchuk, E. Bousquet, F. Bruneval, D. Caliste,
M. Cˆot´e, F. Dahm, F. D. Pieve, M. Delaveau, M. D.
Gennaro, B. Dorado, C. Espejo, G. Geneste, L. Genovese,
A. Gerossier, M. Giantomassi, Y. Gillet, D. R. Hamann,
L. He, G. Jomard, J. L. Janssen, S. L. Roux, A. Levitt,
A. Lherbier, F. Liu, I. Lukaˇcevi´c, A. Martin, C. Martins,
M. J. T. Oliveira, S. Ponc´e, Y. Pouillon, T. Rangel, G.-
M. Rignanese, A. H. Romero, B. Rousseau, O. Rubel,
A. A. Shukri, M. Stankovski, M. Torrent, M. J. V. Setten,
B. V. Troeye, M. J. Verstraete, D. Waroquiers, J. Wiktor,
B. Xu, A. Zhou,
and J. W. Zwanziger, Comput. Phys.
Commun. 205, 106 (2016).
[32] D. R. Hamann, Phys. Rev. B 88, 085117 (2013).
[33] M. J. van Setten, M. Giantomassi, E. Bousquet, M. J.
Verstraete, D. R. Hamann, X. Gonze,
and G.-M. Rig-
nanese, Comput. Phys. Commun. 226, 39 (2018).
[34] M. J. van Setten, M. Giantomassi, X. Gonze, G.-M. Rig-
nanese, and G. Hautier, Phys. Rev. B 96, 155207 (2017).
[35] S. P. Ong,
W. D. Richards,
A. Jain,
G. Hautier,
M. Kocher, S. Cholia, D. Gunter, V. L. Chevrier, K. A.
Persson,
and G. Ceder, Comput. Mater. Sci. 68, 314
(2013).
[36] M. Giantomassi et al., “Open-source library for analyzing
the results produced by ABINIT,” https://github.com/
abinit/abipy (2014).
[37] C. Freysoldt, B. Grabowski, T. Hickel, J. Neugebauer,
G. Kresse, A. Janotti,
and C. G. Van de Walle, Rev.
Mod. Phys. 86, 253 (2014).


## Page 10


10
[38] H.-P. Komsa, T. T. Rantala, and A. Pasquarello, Phys.
Rev. B 86, 045112 (2012).
[39] S. B. Zhang and J. E. Northrup, Phys. Rev. Lett. 67,
2339 (1991).
[40] C. Freysoldt, J. Neugebauer,
and C. G. Van de Walle,
Phys. Status Solidi B 248, 1067 (2011).
[41] Y. Kumagai and F. Oba, Phys. Rev. B 89, 195205 (2014).
[42] D. Broberg, B. Medasani, N. E. Zimmermann, G. Yu,
A. Canning, M. Haranczyk, M. Asta,
and G. Hautier,
Comput. Phys. Commun 226, 165 (2018).
[43] G. K. H. Madsen and D. J. Singh, Comput. Phys. Com-
mun. 175, 67 (2006).
[44] A. Jain, S. P. Ong, W. Chen, B. Medasani, X. Qu,
M. Kocher, M. Brafman, G. Petretto, G.-M. Rignanese,
G. Hautier, D. Gunter,
and K. A. Persson, Concurr.
Comput. Pract. Exp. 27, 5037 (2015).
[45] J. Noﬀsinger, F. Giustino, B. D. Malone, C.-H. Park,
S. G. Louie, and M. L. Cohen, Comput. Phys. Commun.
181, 2140 (2010).
[46] S. Ponc´e, E. R. Margine, C. Verdi,
and F. Giustino,
Comput. Phys. Commun. 209, 116 (2016).
[47] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car,
C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococ-
cioni, I. Dabo, A. Dal Corso, S. de Gironcoli, S. Fabris,
G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis,
A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari,
F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello,
L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A. P.
Seitsonen, A. Smogunov, P. Umari,
and R. M. Wentz-
covitch, J. Phys.: Condens. Matter 21, 395502 (2009).
[48] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau,
M. Buongiorno Nardelli, M. Calandra, R. Car, C. Cavaz-
zoni, D. Ceresoli, M. Cococcioni, N. Colonna, I. Carn-
imeo, A. Dal Corso, S. de Gironcoli, P. Delugas, R. A.
DiStasio, A. Ferretti, A. Floris, G. Fratesi, G. Fugallo,
R. Gebauer, U. Gerstmann, F. Giustino, T. Gorni, J. Jia,
M. Kawamura, H.-Y. Ko, A. Kokalj, E. K¨u¸c¨ukbenli,
M. Lazzeri, M. Marsili, N. Marzari, F. Mauri, N. L.
Nguyen, H.-V. Nguyen, A. O. de-la Roza, L. Paulatto,
S. Ponc´e, D. Rocca, R. Sabatini, B. Santra, M. Schlipf,
A. P. Seitsonen, A. Smogunov, I. Timrov, T. Thonhauser,
P. Umari, N. Vast, X. Wu, and S. Baroni, J. Phys.: Con-
dens. Matter 29, 465901 (2017).
[49] M. Giantomassi, Core-electrons and self-consistency in
the GW approximation from a PAW perspective, Ph.D.
thesis, Universit´e catholique de Louvain (2009), chapter
5 and appendix B.
[50] G. Hautier, S. P. Ong, A. Jain, C. J. Moore,
and
G. Ceder, Phys. Rev. B 85 (2012), 10.1103/phys-
revb.85.155208.
[51] See See Supplemental Material at [URL will be inserted
by publisher].
[52] K. Furukawa, A. Uemoto, M. Shigeta, A. Suzuki,
and
S. Nakajima, Appl. Phys. Lett. 48, 1536 (1986).
[53] Y.
Kondo,
T.
Takahashi,
K.
Ishii,
Y.
Hayashi,
E. Sakuma, S. . Misawa, H. Daimon, M. Yamanaka, and
S. . Yoshida, IEEE Electron Device Lett. 7, 404 (1986).
[54] K. Shibahara, N. Kuroda, S. Nishino,
and H. Mat-
sunami, Jpn. J. Appl. Phys. 26, 1815 (1987).
[55] R. Weing¨artner, P. J. Wellmann, M. Bickermann, D. Hof-
mann, T. L. Straubinger, and A. Winnacker, Appl. Phys.
Lett. 80, 70 (2002).
[56] W. J. Choyke and G. Pensl, MRS Bull. 22, 25 (1997).
[57] H. Morko¸c, S. Strite, G. B. Gao, M. E. Lin, B. Sverdlov,
and M. Burns, J. Appl. Phys. 76, 1363 (1994).
[58] H. R. Philipp, Phys. Rev. 111, 440 (1958).
[59] M. Liu, M. B. Johnston, and H. J. Snaith, Nature 501,
395 (2013).
[60] M. A. Green, A. Ho-Baillie, and H. J. Snaith, Nat. Pho-
tonics 8, 506 (2014).
[61] V.-A. Ha, F. Ricci, G.-M. Rignanese, and G. Hautier, J.
Mater. Chem. C 5, 5772 (2017).
[62] G. A. Saum and E. B. Hensley, Phys. Rev. 7, 1019 (1959).
[63] T. J. Richardson, Solid State Ionics 165, 305 (2003).
[64] R. Gobrecht, Phys. Status Solidi 13, 429 (1966).
[65] J. Noﬀsinger, E. Kioupakis, C. G. Van de Walle, S. G.
Louie, and M. L. Cohen, Phys. Rev. Lett. 108, 167402
(2012).
[66] N. F. Quackenbush, J. P. Allen, D. O. Scanlon, S. Sal-
lis, J. A. Hewlett, A. S. Nandur, B. Chen, K. E. Smith,
C. Weiland, D. A. Fischer, J. C. Woicik, B. E. White,
G. W. Watson,
and L. F. J. Piper, Chem. Mater. 25,
3114 (2013).
[67] G. Hautier, A. Miglio, D. Waroquiers, G.-M. Rignanese,
and X. Gonze, Chem. Mater. 26, 5447 (2014).
[68] K. Kuhar, M. Pandey, K. S. Thygesen,
and K. W. Ja-
cobsen, ACS Energy Lett. 3, 436 (2018).
[69] J. Tate, H. L. Ju, J. C. Moon, A. Zakutayev, A. P.
Richard, J. Russell,
and D. H. McIntyre, Phys. Rev.
B 80, 165206 (2009).
[70] Y.
Ogo,
H.
Hiramatsu,
K.
Nomura,
H.
Yanagi,
T. Kamiya, M. Hirano,
and H. Hosono, Appl. Phys.
Lett. 93, 032113 (2008).
[71] E. Maci´a-Barber, “Thermoelectric materials: Advances
and applications,” (Pan Stanford, 2015).
[72] T. Kajikawa, N. Kimura, and T. Yokoyama, in Proceed-
ings ICT’03. 22nd International Conference on Thermo-
electrics (IEEE Cat. No.03TH8726) (2003).
[73] C. L. Condron, S. M. Kauzlarich, F. Gascoin, and G. J.
Snyder, J. Solid State Chem. 179, 2252 (2006).
[74] J. Zhang, L. Song, A. Mamakhel, M. R. V. Jørgensen,
and B. B. Iversen, Chem. Mater. 29, 5371 (2017).
[75] A. Zunger, Appl. Phys. Lett. 83, 57 (2003).


## Page 11


Supplemental Material for
“Computationally-driven, high throughput identiﬁcation of CaTe and Li3Sb as
promising candidates for high mobility p-type transparent conducting materials”
Viet-Anh Ha,1 Guodong Yu,1, ∗Francesco Ricci,1 Diana Dahliah,1 Michiel van
Setten,1, † Matteo Giantomassi,1 Gian-Marco Rignanese,1 and Geoﬀroy Hautier1, ‡
1Institute of Condensed Matter and Nanoscience (IMCN), Universit´e catholique de Louvain (UCLouvain),
Chemin ´etoiles 8, bte L7.03.01, Louvain-la-Neuve 1348, Belgium
(Dated: November 14, 2018)
I.
COMPUTATIONAL DETAILS
All details of electron-phonon interaction computations can be found from the Refs. 1 and 2. Here, we rewrite the
formulas for the scattering rate (inverse of the relaxation time) and the electron-phonon coupling strength for speciﬁc
phonon mode and phonon wave-vector. The scattering rates at given temperature:
1
τnk
=2π
ℏ
X
mν
Z
dq
ΩBZ
|gnmν(k, q)|2
× [(1 −fmk+q + nqν)δ(ϵnk −ℏωqν −ϵmk+q) + (fmk+q + nqν)δ(ϵnk + ℏωqν −ϵmk+q)] ,
(S1)
where, τnk is relaxation time of carriers at band n and wave-vector k, ΩBZ is volume of Brillouin zone (BZ), gnmν(k, q)
is the ﬁrst-order electron-phonon matrix element from initial Kohn-Sham state nk (eigenvalue ϵnk) to ﬁnal one mk+q
(eigenvalue ϵmk+q) associated with a phonon mode ν and wave-vector q, fmk+q = [exp((ϵnk+q −ϵF )/kBT) + 1]−1
is Fermi-Dirac distribution of carriers at Fermi energy ϵF and temperature T, nqν = [exp(ℏωqν/kBT) −1]−1 is
Bose-Einstein distribution of phonons with frequencies ωqν at temperature T.
The scattering rates (inverse of relaxation time) as a function of energy is computed by averaging all states as
1
τ(ϵ) =
1
N(ϵ)
X
nk
1
τnk
δ(ϵnk −ϵ),
(S2)
where, N(ϵ) = P
nk δ(ϵnk −ϵ) is density of states.
The electron-phonon coupling strength of a speciﬁc phonon mode ν and wave-vector q
λqν =
1
N(ϵF )ℏωqν
X
nm
Z
dk
ΩBZ
|gnmν(k, q)|2 δ(ϵnk −ϵF )δ(ϵmk+q −ϵF ),
(S3)
where N(ϵF ) is density of state at Fermi level. We kept our materials intrinsic by setting the Fermi level at the
mid-gap and in the very general approach of EPW, all phonon modes, both inter-band and intra-band scattering
mechanisms are taken into account in the computation of scattering rates.
The hole mobilities µh can then be calculated as
µh = σh/nhe,
(S4)
where σh, nh and e are conductivity tensor, density of holes and elementary charge respectively. In order to calculate
conductivity tensor, we solve semi-classical Boltzmann transport equation (BTE). The conductivity tensor is given
by
σαβ(n, k) = e2τnkvα(n, k)vβ(n, k),
(S5)
∗Present address: School of Physics and Technology (SPT), Wuhan University (WHU), Wuhan 430072, China
† Present address: IMEC, 75 Kapeldreef, B-3001 Leuven, Belgium
‡ E-mail: geoﬀroy.hautier@uclouvain.be
arXiv:1811.05390v1  [cond-mat.mtrl-sci]  13 Nov 2018


## Page 12


2
where e is elementary charge and vα(n, k) the group velocity deﬁned through the ﬁrst-derivative of the band-energy
ϵn,k with respect to the wave-vector k
vα(n, k) = 1
ℏ
∂ϵn,k
∂kα
.
(S6)
The conductivity tensor can be expressed as a function of energy by multiplying Eq. S5 by a Dirac delta and then
summing over all bands and k points in the Brillouin zone as
σαβ(ϵ) = 1
N Σn,kσαβ(n, k)δ(ϵ −ϵn,k),
(S7)
where N is the number of k points. Finally, the conductivity tensor as a function of temperature T and Fermi level
µ (electronic chemical potential) is computed through σαβ(ϵ) as
σαβ(T; µ) = 1
Ω
Z
σαβ(ϵ)

−∂fµ(T; ϵ)
∂ϵ

dϵ,
(S8)
where fµ is the Fermi-Dirac distribution and Ωis the volume of the unit cell. The Fermi level µ is deﬁned corre-
spondingly to a given doping carrier concentration.
Here, we used the BoltzTrap package [3] to solve BTE. In practice, BoltzTrap interpolates the DFT band-energies
(computed on a ﬁnite number of k-points) using star functions (see section 2 of Ref. 3). Hence, the group velocities
in Eq. S6 can be easily obtained on a much denser k-point grid thus facilitating the numerical convergence of the ﬁnal
results. In constant relaxation-time approximation, the calculations based on the interpolation of band-energies can
produce many transport quantities such as conductivity, mobility, Seebeck coeﬃcient, etc. as long as the relaxation-
time is known. In this work, we go beyond this approximation using τn,k computed by EPW. We implement an
interpolation for relaxation time in BoltzTrap on the same very dense k-point grid used for band-energies.
The
physical principle for this implementation is that the symmetries of the self-energy are the same as those of band-
energies [4] (τn,k can be calculated from the imaginary part of the electron self-energy in interaction with phonons).
II.
RESULTS
Table SI shows information of 107 materials passing through the ﬁrst two ﬁlters and then computed with HSE to
obtain more accurate band gaps and direct gaps.
TABLE SI: Formula, space group (SG), Materials Project identiﬁcation number [5, 6], three principal hole eﬀective masses
m1, m2 and m3 (in mo-free electron mass) (the data of eﬀective masses is reported in the previous work[7]), stability measured
by the energy above hull Ehull in the phase diagram (in meV/atom), fundamental Eg and direct gaps Ed
g (in eV) computed
using PBE and HSE [8, 9].
Eg
Ed
g
Formula
SG
MP-id
m1
m2
m3
Ehull
PBE
HSE
PBE
HSE
BeS
F43m
422
0.65
0.65
0.65
0.0
3.14
4.05
5.62
6.89
KMgH3
Pm3m
23737
0.75
0.75
0.75
0.0
2.46
3.58
4.51
5.76
SiC
F43m
8062
0.58
0.58
0.58
0.7
1.39
2.25
4.53
5.75
CsPbCl3
Amm2
675524
0.30
0.32
0.33
0.0
2.46
5.69
2.41
5.69
BeSe
F43m
1541
0.55
0.55
0.55
0.0
2.69
3.36
4.22
5.27
BeCN2
I42d
15703
0.75
0.75
0.78
0.0
3.85
5.21
3.85
5.21
RbPbF3
Cc
674508
0.71
0.83
0.95
0.0
3.81
4.84
4.10
5.20
MgS
Fm3m
1315
0.98
0.98
0.98
0.0
2.79
3.84
3.61
4.95
RbHgF3
Pm3m
7482
0.93
0.93
0.93
0.0
0.65
2.11
2.70
4.90
AgCl
Fm3m
22922
0.83
0.83
0.83
0.0
0.95
2.28
2.89
4.81
CsHgF3
Pm3m
561947
0.89
0.89
0.89
0.0
0.76
2.20
2.43
4.59
Be2C
Fm3m
1569
0.37
0.37
0.37
0.0
1.19
1.63
4.12
4.56
SrMgH4
Cmc21
643009
0.84
0.90
0.95
0.0
2.74
3.78
3.27
4.52
Li2Se
Fm3m
2286
0.95
0.95
0.95
0.0
3.00
3.70
3.36
4.36
BP
F43m
1479
0.34
0.34
0.34
0.0
1.24
2.26
3.39
4.35
CaS
Fm3m
1672
0.88
0.88
0.88
0.0
2.39
3.34
3.18
4.28
LiCa4B3N6
Im3m
6799
0.86
0.86
0.86
0.0
2.21
3.38
2.98
4.25
Continued on next page


## Page 13


3
TABLE SI – continued from previous page
Eg
Ed
g
Formula
SG
MP-id
m1
m2
m3
Ehull
PBE
HSE
PBE
HSE
BaSrI4
R3m
754852
0.73
0.73
0.80
21.8
3.37
4.22
3.35
4.22
LiSr4B3N6
Im3m
9723
0.89
0.89
0.89
0.0
2.09
3.22
2.95
4.18
NaSr4B3N6
Im3m
10811
0.92
0.92
0.92
0.0
1.99
3.14
2.78
4.08
K2LiAlH6
Fm3m
24411
0.65
0.65
0.65
9.1
2.45
3.70
2.93
4.04
BeTe
F43m
252
0.42
0.42
0.42
0.0
2.02
2.45
3.62
4.04
Ba3SrI8
I4/mmm
756235
0.70
0.81
0.81
7.5
3.23
4.02
3.23
4.02
CaSe
Fm3m
1415
0.77
0.77
0.77
0.0
2.09
2.95
2.99
4.01
LiH
Fm3m
23703
0.46
0.46
0.46
0.0
3.02
3.97
2.97
3.97
AlP
F43m
1550
0.56
0.56
0.56
0.0
1.63
2.50
3.09
3.90
YbS
Fm3m
1820
0.76
0.76
0.76
0.0
2.22
2.96
2.91
3.76
Na2LiAlH6
Fm3m
644092
0.66
0.66
0.66
3.9
2.64
3.75
2.89
3.75
SrSe
Fm3m
2758
0.83
0.83
0.83
0.0
2.23
3.03
2.80
3.68
BaLiH3
Pm3m
23818
0.36
0.36
0.36
0.0
2.27
3.26
2.55
3.62
CsPbF3
Pm3m
5811
0.39
0.39
0.39
4.6
3.05
3.59
2.92
3.59
Cs3ZnH5
I4/mcm
643702
0.69
0.93
0.93
0.0
2.75
3.58
2.79
3.58
Al2CdS4
Fd3m
9993
0.78
0.78
0.78
20.0
2.47
3.55
2.47
3.56
K2LiAlH6
R3m
23774
0.68
0.84
0.84
0.0
2.58
3.52
2.90
3.52
BaMgH4
Cmcm
643718
0.48
0.55
0.70
4.8
2.32
3.26
2.58
3.51
CaTe
Fm3m
1519
0.60
0.60
0.60
0.0
1.55
2.18
2.62
3.50
Cs3MgH5
P4/ncc
23947
0.88
0.93
0.93
0.3
2.61
3.49
2.63
3.49
Cs3MgH5
I4/mcm
643895
0.83
0.94
0.94
0.0
2.59
3.49
2.61
3.49
YbSe
Fm3m
286
0.67
0.67
0.67
0.0
1.97
2.43
2.77
3.48
ZnS
F43m
10695
0.81
0.81
0.81
0.0
2.02
3.46
2.02
3.46
TaCu3S4
P43m
10748
0.98
0.98
0.98
0.0
1.95
2.95
2.34
3.46
Al2ZnS4
Fd3m
4842
0.66
0.66
0.66
0.0
2.49
3.43
2.52
3.46
Li2ThN2
P3m1
27487
0.85
0.95
0.95
0.0
2.18
3.33
2.34
3.46
Mg2B24C
P4n2
568556
0.77
0.93
0.93
0.0
2.63
3.41
2.62
3.42
Li2GePbS4
I42m
19896
0.61
0.61
0.98
0.0
2.25
3.20
2.31
3.33
Cs3H5Pd
P4/mbm
643006
0.79
0.83
0.83
0.0
2.28
3.09
2.38
3.32
SrTe
Fm3m
1958
0.67
0.67
0.67
0.0
1.77
2.39
2.48
3.24
MgTe
F43m
13033
0.95
0.95
0.95
0.9
2.32
3.24
2.32
3.24
CsTaN2
I42d
34293
0.71
0.71
0.92
0.0
2.15
3.22
2.21
3.22
Cs3MnH5
I4/mcm
643706
0.82
0.96
0.96
0.0
1.65
3.18
1.66
3.21
LiMgP
F43m
36111
0.65
0.65
0.65
0.0
1.56
2.00
2.39
3.18
BaS
Fm3m
1500
0.85
0.85
0.85
0.0
2.16
3.02
2.30
3.17
LiAlTe2
I42d
4586
0.52
0.83
0.83
0.0
2.44
3.11
2.44
3.11
YbTe
Fm3m
1779
0.54
0.54
0.54
0.0
1.47
1.76
2.46
3.09
Li3Sb
Fm3m
2074
0.24
0.24
0.24
0.0
0.72
1.15
2.28
3.06
SrAl2Te4
I422
37091
0.42
0.79
0.80
0.0
1.50
2.66
1.55
3.06
TaCu3Te4
P43m
9295
0.63
0.63
0.63
0.0
1.14
2.50
1.59
3.05
TaCu3Se4
P43m
4081
0.82
0.82
0.82
0.0
1.63
2.43
2.03
2.98
BaSe
Fm3m
1253
0.76
0.76
0.76
0.0
1.96
2.59
2.19
2.95
KAg2PS4
I42m
12532
0.67
0.82
0.82
0.0
1.27
2.53
2.05
2.87
AlAs
F43m
2172
0.50
0.50
0.50
0.0
1.52
2.12
1.77
2.84
LiErS2
I41/amd
35591
0.62
0.99
0.99
10.4
1.99
2.80
1.99
2.80
GaN
F43m
830
0.94
0.94
0.94
5.2
1.57
2.80
1.56
2.80
CsPbCl3
Pm3m
23037
0.26
0.26
0.26
5.5
2.40
2.75
2.19
2.75
GaP
F43m
2490
0.45
0.45
0.45
0.0
1.59
1.97
1.59
2.69
LiSmS2
I41/amd
34477
0.93
0.93
0.99
0.0
1.92
2.69
1.92
2.69
LiGaTe2
I42d
5048
0.37
0.70
0.70
0.0
1.59
2.69
1.59
2.69
ThSnI6
P31c
28815
0.55
0.57
0.57
20.8
1.99
2.32
2.23
2.66
BaTe
Fm3m
1000
0.64
0.64
0.64
0.0
1.59
2.22
1.97
2.65
CuI
F43m
22895
0.86
0.86
0.86
6.0
1.14
2.65
1.13
2.65
NbCu3Se4
P43m
4043
0.82
0.82
0.82
0.0
1.40
2.12
1.79
2.64
TaSbRu
F43m
31454
0.73
0.73
0.73
0.0
0.71
1.30
1.84
2.63
Nd2TeS2
P3m1
10933
0.45
0.72
0.72
0.0
1.62
2.23
1.95
2.63
Zr2SN2
P63/mmc
11583
0.40
0.54
0.54
0.0
0.56
1.38
1.62
2.62
Ca3PCl3
Pm3m
29342
0.63
0.63
0.63
0.0
1.84
2.60
1.84
2.60
Continued on next page


## Page 14


4
TABLE SI – continued from previous page
Eg
Ed
g
Formula
SG
MP-id
m1
m2
m3
Ehull
PBE
HSE
PBE
HSE
BaMg2P2
P3m1
8278
0.62
0.62
0.88
0.0
1.15
1.69
1.75
2.60
WS2
R3m
9813
0.79
0.91
0.91
3.8
1.34
2.12
1.84
2.60
Ca3AsCl3
Pm3m
28069
0.58
0.58
0.58
0.0
1.84
2.57
1.84
2.57
BaSnS2
P21/c
12181
0.44
0.57
0.85
0.0
1.62
2.40
1.69
2.54
LiZnP
F43m
10182
0.40
0.40
0.40
0.0
1.36
1.69
1.50
2.51
ScCuS2
P3m1
6980
0.75
0.75
0.87
0.0
0.88
1.77
1.50
2.50
SbIrS
Pca21
9270
0.50
0.52
0.89
4.5
1.04
1.76
1.54
2.43
Cd2P3Cl
Cc
29246
0.41
0.76
0.80
9.1
1.12
2.06
1.58
2.42
CsPbBr3
Pnma
567629
0.25
0.28
0.29
0.0
2.01
2.39
2.01
2.39
Hg2P3Cl
C2/c
28875
0.40
0.82
0.99
2.3
1.13
1.89
1.56
2.38
Cd2P3Br
C2/c
29245
0.44
0.78
0.87
6.8
1.05
2.01
1.57
2.37
CsNbN2
Fd3m
8978
0.53
0.53
0.53
8.2
1.53
2.36
1.53
2.36
RbGeBr3
Pna21
28558
0.32
0.42
0.47
0.0
1.99
2.34
1.99
2.34
SbIrS
P213
8630
0.39
0.39
0.39
0.0
1.42
2.18
1.56
2.34
Ca3AsBr3
Pm3m
27294
0.57
0.57
0.57
0.0
1.67
2.34
1.67
2.34
LiYSe2
I41/amd
37879
0.55
0.83
0.83
17.6
1.55
2.33
1.55
2.33
ZrCoBi
F43m
31451
0.80
0.80
0.80
0.0
1.15
1.28
1.66
2.31
NaLi2Sb
Fm3m
5077
0.41
0.41
0.41
0.0
0.71
1.04
1.61
2.27
ZnP2
P41212
2782
0.37
0.65
0.65
0.0
1.47
2.14
1.59
2.27
KHgF3
Pm3m
7483
0.87
0.87
0.87
0.0
0.64
2.26
2.82
2.26
LiHoSe2
I41/amd
33322
0.52
0.83
0.83
16.8
1.58
2.25
1.58
2.25
LiDySe2
I41/amd
35717
0.55
0.81
0.82
16.0
1.56
2.23
1.56
2.23
P2Pt
Pa3
730
0.25
0.25
0.25
0.0
1.06
1.79
1.51
2.22
TbLiSe2
I41/amd
38695
0.61
0.78
0.78
15.4
1.54
2.20
1.54
2.20
MgGeP2
I42d
34903
0.26
0.61
0.61
13.0
1.51
2.16
1.54
2.16
LiSmSe2
I41/amd
35388
0.72
0.72
0.75
0.0
1.51
2.15
1.51
2.15
LiNdSe2
I41/amd
37605
0.72
0.72
0.84
7.6
1.52
2.15
1.52
2.15
SrMg2Sb2
P3m1
9566
0.53
0.55
0.55
0.0
0.98
1.42
1.51
2.06
RbAu
Pm3m
30373
0.24
0.24
0.24
0.0
0.57
0.49
1.80
2.02
CsAu
Pm3m
2667
0.25
0.25
0.25
0.0
1.02
1.25
1.73
1.99
LiNbS2
P63/mmc
7936
0.61
0.61
0.68
0.0
0.73
1.06
1.56
1.95
Ag3SbS3
R3c
4515
0.49
0.49
1.00
2.3
1.00
1.30
1.54
1.94
Table SII shows information of current n-type TCMs. Most of them exhibits mobility at the order of 100 cm2/Vs.
TABLE SII: The current n-type TCMs, fabrication methods (abbreviations of some methods are at the bottom of this table),
sorts of dopants used, electron carrier concentrations C (in cm−3) and mobilities µ (in cm2/Vs). These values are extracted
from experimental measurements (as cited references) at room-temperature. The values of mobility depend on morphologies
of fabricated-samples such as single crystal, polycrystalline, amorphous, thin-ﬁlm,...
n-TCMs
Processing
Dopants
C (cm−3)
µ (cm2/Vs)
SnO2
CVD
Sb
8.5 × 1015
260 [10]
CVD
Sb
8.6 × 1016
240 [10]
CVD
Sb
2.2 × 1018
150 [10]
PLD
Ta
2.7 × 1020
83 [11]
PLD
Sb
∼1 × 1019
∼40 [12]
ZnO
VPT
Undoped
6 × 1016
205 [13]
†
†
1015 −1020
50-230 [14, 15]
PLD
Undoped
3 × 1016
155 [16]
Sputtering
Al
3.6 × 1020
41.3 [17]
Sputtering
Al
8 × 1020
17 [18, 19]
In2O3
PVD
-
3 −9 × 1017
160 [20]
ST
Sn
0.1 −6 × 1020
30-70 [21]
Sputtering
Undoped
1017 −1020
< 10 [22]
VEM
Undoped
3.5 × 1019
25 −60 [23]
VEM
Undoped
4.69 × 1020
74 [24]
Continued on next page


## Page 15


5
TABLE SII – continued from previous page
n-TCMs
Processing
Dopants
C (cm−3)
µ (cm2/Vs)
EBE
Sn
0.46 −8.6 × 1020
43 −79 [25]
Flux
Sn
1.6 × 1020
100 [26]
Sputtering
Sn
6 × 1020
∼25 [27]
TRE
Mo
2.5 −3.5 × 1020
80 −130 [28]
PLD
Mo
1.9 × 1020
95 [29]
Sputtering
H
1.4 −1.8 × 1020
98 −130 [30]
Sputtering
H
1.5 × 1020
140 [31]
Sputtering
Sn
1 × 1021
40 [32]
Ga2O3
Verneuil
Undoped
1 × 1018
80 [33]
FZM
Undoped
1.2 −5.2 × 1018
2.6 −46 [34]
EFG
Undoped
1 × 1017
153 [35]
-
Undoped
8 × 1016
∼150 [36]
CVD: Chemical vapor deposition
PLD: Pulsed laser deposition
VPT: Vapor phase transport
†: Reviewed from many papers
PVD: Physical vapor deposition
ST: Spray technique
VEM: Vacuum evaporation method
EBE: e-beam evaporation
TRE: Thermal reactive evaporation
FZM: Floating zone method
EFG: Edge-deﬁned ﬁlm-fed growth
Table SIII shows information for diﬀerent A3B compounds (A = Li, Na, K, Rb and Cs; and B = N, P, As and Sb).
The very unstable compounds are not considered here. The data of compounds with narrow gap Eg < 0.4 eV is not
presented because the values of eﬀective masses are not reliable.
TABLE SIII: Formula, space group (SG), Materials Project identiﬁcation number [5, 6], fundamental Eg computed with
DFT (in eV), three principal hole eﬀective masses m1, m2 and m3 (mo-free electron mass) and stability measured by energy
above hull Ehull in the phase diagram (in meV/atom).
Formula
SG
MP-id
Eg
m1
m2
m3
Ehull
Li3N
P6/mmm
2251
0.98
1.09
1.09
5.30
0.0
Li3N
P63/mmc
2341
1.22
1.60
1.60
3.66
10.0
Li3P
P63/mmc
736
0.70
0.84
0.84
2.41
0.0
Li3As
P63/mmc
757
0.64
0.74
0.74
2.10
0.0
Li3Sb
P63/mmc
7955
0.48
0.61
0.61
1.75
3.0
Li3Sb
Fm3m
2074
0.85
0.24
0.24
0.24
0.0
Na3P
P63/mmc
1598
0.41
1.61
1.61
6.52
0.0
Na3Sb
P63/mmc
7956
0.40
1.10
1.10
3.85
0.0
K3Sb
Fm3m
10159
0.68
5.22
5.22
5.22
29.0
Rb3Sb
Fm3m
33018
0.43
1.71
1.71
1.71
34.0
Cs3Sb
Fm3m
10378
0.61
1.03
1.03
1.03
0.0
Fig. S1 presents scattering rate of both CaTe and Li3Sb as a functions of energy at room temperature (valence band
maximums (VBM) are set to zeros). The speciﬁc contributions of acoustic (the ﬁrst three modes) and optical (the
remaining ones) phonon-modes are also shown. We can see that the optical modes are the main source of scattering
in both cases.
Fig. S2 shows electron-phonon coupling strength (see Eq. S3) for six phonon modes of CaTe computed with a
dense q-point mesh of 40 × 40 × 40. The Fermi energy in Eq. S3 was set to 146 meV below the VBM in order to
assure this quantity to be deﬁned (N(ϵF ) > 0). Moreover, the Fermi level corresponding to very high doping of 1021
cm−3 lies 264.5 meV below the VBM so the value of 146 meV can give us the picture in the considering range of
hole concentrations. The electron-phonon coupling strength λqν, therefore, can depict the intensity of interactions
between hole carriers (around VBM) and each phonon mode. The average values of λqν over all q-points (shown as
red lines) point out that the hole carriers interacts with optical modes (mainly mode-6) around 5 times stronger than
with acoustic modes.
In the same way, Fig. S3 presents electron-phonon coupling strength for twelve phonon modes of Li3Sb computed
with a dense q-point mesh of 40 × 40 × 40. The Fermi energy in Eq. S3 was set to 100 meV below the VBM (the


## Page 16


6
acoustic
optical
E (eV)
0
1
2
3
-1
-2
-3
Scattering rates (s
-1)
x10
14
0
1
2
3
4
5
6
7
total
acoustic
optical
total
E (eV)
0
1
2
3
4
-3
-2
-1
0
1
2
3
(a)
(b)
x 10
14
FIG. S1.
Scattering rates of (a) CaTe and (b) Li3Sb at temperature of 300 K. The contributions of acoustic and optical
phonon-modes are shown as well.
0.0
0.1
0.2
0.3
0.4
q
mode-1
0.0
0.1
0.2
0.3
0.4
mode-2
0.0
0.1
0.2
0.3
0.4
mode-3
0
25000 50000
q-point
0.00
0.05
0.10
0.15
0.20
q
mode-4
0
25000 50000
q-point
0.00
0.05
0.10
0.15
0.20
mode-5
0
25000 50000
q-point
0.0
0.2
0.4
0.6
0.8
mode-6
FIG. S2. The electron-phonon coupling strength of CaTe for speciﬁc mode ν and phonon wave-vector q. There are 6 phonon
modes including 3 acoustic (1-3) and 3 optical ones (4-6). The number of q-points are 64000 corresponding to 40 × 40 × 40
mesh in the full Brillouin zone. To reduce size of the ﬁgure, q-points with λνq < 1 × 10−3 are not shown in the subﬁgures. The
red lines are average values of λνq over 64000 q-points.
Fermi level at doping of 1021 cm−3 is 168.5 meV lower than VBM). In this case, the intensity of interactions (between
hole carriers and phonons) with optical modes is about 19 times stronger than with acoustic modes.
We performed convergence tests for G0W0 calculations over the number of bands (Nb) and the kinetic energy cut-oﬀ
for dielectric tensor (Ec). These two parameters will be simultaneously investigated in speciﬁc ranges, then we can
choose appropriate values those give acceptable convergence of band gap. Fig. S4 and Table SIV show how band gap


## Page 17


7
0.00
0.05
0.10
0.15
0.20
q
mode-1
0.00
0.05
0.10
0.15
0.20
mode-2
0.00
0.05
0.10
0.15
0.20
mode-3
0.00
0.05
0.10
0.15
0.20
q
mode-4
0.00
0.05
0.10
0.15
0.20
mode-5
0.0
0.2
0.4
0.6
mode-6
0.00
0.05
0.10
0.15
0.20
q
mode-7
0.00
0.05
0.10
0.15
0.20
mode-8
0.00
0.05
0.10
0.15
0.20
mode-9
0
25000 50000
q-point
0.00
0.05
0.10
0.15
0.20
q
mode-10
0
25000 50000
q-point
0.00
0.05
0.10
0.15
0.20
mode-11
0
25000 50000
q-point
0.00
0.05
0.10
0.15
0.20
mode-12
FIG. S3. The electron-phonon coupling strength of Li3Sb for speciﬁc mode ν and phonon wave-vector q. There are 12 phonon
modes including 3 acoustic (1-3) and 9 optical ones (4-12). The number of q-points are 64000 corresponding to 40 × 40 × 40
mesh in the full Brillouin zone. To reduce size of the ﬁgure, q-points with λνq < 0.5 × 10−2 are not shown in the subﬁgures.
The red lines are average values of λνq over 64000 q-points.


## Page 18


8
at Γ point of CaTe evolves with the change of Nb and Ec. Here, Nb = [75, 150, 300, 450] and Ec = [6, 8, 10, 12, 14] Ha.
In the same way, Fig. S5 and Table SV present how band gap at Γ point of Li3Sb converges with the change of number
of band and energy cut-oﬀfor the dielectric tensor. In the case, Nb = [80, 160, 240, 320] and Ec = [4, 6, 8, 10, 12] Ha.
In both cases, energy cut-oﬀfor kinetic energy is set to 46 Ha and k-point mesh is 6 × 6 × 6.
Ec (Ha)
6
7
8
9
10 11
12
13
14
Nb
100150
200250300
350400450
5.34
5.35
5.36
5.37
5.38
5.39
5.40
5.40
5.41
5.42
Eg (eV)
Γ
5.36
5.37
5.38
5.39
5.40
5.41
FIG. S4. The convergence test for the gap at Γ point of CaTe in G0W0 computation.
4
5
6
7
8
9
10
11
12
100
150
200
250
300
3.33
3.34
3.35
3.36
3.37
3.38
3.38
3.39
3.40
3.41
3.36
3.37
3.38
3.39
3.40
Ec  (Ha)
Nb
Eg (eV)
Γ
FIG. S5. The convergence test for the gap at Γ point of Li3Sb in G0W0 computation.
In comparison, Fig. S6 and Fig. S7 show band structures of CaTe and Li3Sb computed by both G0W0 (red) and
DFT (blue).
Fig. S10, Fig. S11, Fig. S12, Fig. S13 and Fig. S14 show defect formation energies and phase diagrams of AlP,
LiH, BaLiH3, CsH, SrTe and Al2ZnS4 (computed by DFT), correspondingly. The facets of phase diagrams in which


## Page 19


9
TABLE SIV. The evolution of the gap at Γ point of CaTe EΓ
g (in eV) with the change of number of bands Nb and kinetic
energy cut-oﬀfor dielectric tensor Ec (in Ha).
Nb
75
75
75
75
75
150
150
150
150
150
Ec
6.0
8.0
10.0
12.0
14.0
6.0
8.0
10.0
12.0
14.0
EΓ
g
5.41558
5.42030
5.42063
5.42239
5.42275
5.39362
5.39570
5.39460
5.39418
5.39352
Nb
300
300
300
300
300
450
450
450
450
450
Ec
6.0
8.0
10.0
12.0
14.0
6.0
8.0
10.0
12.0
14.0
EΓ
g
5.36266
5.36771
5.36552
5.36260
5.36077
5.34078
5.34818
5.34680
5.34287
5.34034
TABLE SV. The evolution of the gap at Γ point of Li3Sb EΓ
g (in eV) with the change of number of bands Nb and kinetic energy
cut-oﬀfor dielectric tensor Ec (in Ha).
Nb
80
80
80
80
80
160
160
160
160
160
Ec
4.0
6.0
8.0
10.0
12.0
4.0
6.0
8.0
10.0
12.0
EΓ
g
3.33445
3.34410
3.34744
3.34911
3.35034
3.37762
3.39112
3.39166
3.39208
3.39262
Nb
240
240
240
240
240
320
320
320
320
320
Ec
4.0
6.0
8.0
10.0
12.0
4.0
6.0
8.0
10.0
12.0
EΓ
g
3.37743
3.40028
3.39860
3.39749
3.39752
3.37587
3.40757
3.40897
3.40748
3.40683
Γ
X
W
K
Γ
L
U
W
L
K
−4
−2
0
2
4
6
GGA
G0W0
Wave vector
Energy (eV)
FIG. S6. The band structure of CaTe computed by DFT (blue) and G0W0 (red).
the chemical potentials of elements were estimated are marked to corresponding defect formation energies. It worth
noting that although DFT calculations using GGA underestimate band gap, the defect formation energy computed
with it is still reliable[37]. In HSE computations, the VBM shifts down while the CBM shifts up, therefore, the general


## Page 20


10
Γ
X
W
K
Γ
L
U
W
L
K
Wave vector
−4
−2
0
2
4
6
GGA
G0W0
Energy (eV)
FIG. S7. The band structure of Li3Sb computed by DFT (blue) and G0W0 (red).
VacCa
0.0
0.5
1.0
1.5
2.0
Fermi energy (eV)
Defect formation energy (eV)
-1
0
1
2
3
4
VacTe
TeCa
CaTe
NaCa
KCa
LiCa
Cai(tet,Te4)
Tei(tet,Te4)
0
+1
+2
0
-1
-2
0
0
+1
+2
-1
0
-1
0
-1
0
-1
+2
Formation energy (eV/atom)
Fraction
Te
Ca
CaTe
-2.0
0.0
-0.5
-1.5
-1.0
0.0
0.2
0.4
0.6
0.8
1.0
CaTe
Ca
Te
K
KTe K2Te
K2Te3
Te
Ca
Na
CaTe
Na2Te
NaTe3
Ca
CaTe
Te
Li
Li2Ca
Li2Te
FIG. S8. The defect formation energy as a function of Fermi level of intrinsic and extrinsic defects for CaTe (left) and the phase
diagrams with chemical potentials of each element in speciﬁc facets (right). The intrinsic defects include vacancies (VacCa
and VacTe), anti-sites (TeCa and CaTe) and interstitial atoms inserting into the tetrahedral hollows formed by 4 Te atoms
(Cai(tet,Te4) and Tei(tet,Te4)) while Na, K and Li are used as the extrinsic defects substituting onto Ca-sites (NaCa, KCa and
LiCa). The chemical potential of elements are obtained from phase diagrams of Ca-Te and Ca-Te-X (X=Na, K and Li) for
intrinsic and extrinsic defects, respectively. The VBM is set to zero.
trend of defect formation energy is similar to that in DFT-GGA computations. The change of formation energy is
small as well[37].


## Page 21


11
Fermi energy (eV)
Defect formation energy (eV)
0.0
VacLi-1
VacLi-2
VacSb
LiSb
SbLi-1
SbLi-2
Lii(oct, Sb2Li4)
Lii(oct, SbLi5)
Sbi(oct, Sb2Li4)
Sbi(oct, SbLi5)
0.2
0.4
0.6
0.8
1.0
-1
0
1
2
3
4
0
+1
0
+1
0
-1
+1
+2
0
0
-1
+1
0
+1
+2
0
-1
0
-1
Formation energy (eV/atom)
Fraction
Li2Sb
Li3Sb
Sb
Li
0.0
0.2
0.4
0.6
0.8
1.0
0.0
-0.2
-0.4
-0.6
-0.8
FIG. S9. The defect formation energy as a function of Fermi level of intrinsic defects for Li3Sb (left) and the phase diagram
with chemical potentials of each element in a speciﬁc facet (right). The intrinsic defects include vacancies (VacLi-1, VacLi-2 and
VacSb), anti-sites (LiSb, SbLi-1 and SbLi-2) and interstitial atoms inserting into the octahedron hallows formed by Sb and Li
atoms (Lii(oct, Sb2Li4), Lii(oct, SbLi5), Sbi(oct, Sb2Li4) and Sbi(oct, SbLi5)). The chemical potentials of Li and Sb are obtained from
their phase diagram. The VBM is set to zero.
Defect formation energy (eV)
Fermi energy (eV)
0
2
4
6
8
10
12
0
1
2
3
VacAl
VacP
AlP
PAl
Defect formation energy (eV)
Fermi energy (eV)
0
-2
2
4
6
8
10
12
14
0
1
2
3
VacAl
VacP
PAl
AlP
Phase diagram
0.0
0.25
0.50
0.75
0.10
-0.6
-0.5
-0.4
-0.3
-0.2
-0.1
0.0
Formation energy (eV/fu)
Fraction
AlP
Al
P
FIG. S10. The phase diagram and defect formation energies of AlP in Al-rich and P-rich conditions.


## Page 22


12
LiH
VacH
VacLi
HLi
Fermi energy (eV)
Defect formation energy (eV)
0
1
2
3
4
0
2
4
6
8
Fermi energy (eV)
Defect formation energy (eV)
0
1
2
3
4
-2
1
2
4
6
LiH
VacH
VacLi
HLi
H2
Li
LiH
Fraction
Formation energy (eV/fu)
0.0
0.2
0.4
0.6
0.8
1.0
-0.5
-0.4
-0.3
-0.2
-0.1
0.0
H-rich
Li-rich
Phase diagram
FIG. S11. The phase diagram and defect formation energies of LiH in H-rich and Li-rich conditions.


## Page 23


13
Li
Ba
H2
LiH
BaH2
BaLiH3
Fermi energy (eV)
Defect formation energy (eV)
0
VacLi
VacBa
VacH
1
2
3
-1
0
1
2
3
4
5
6
Fermi energy (eV)
Defect formation energy (eV)
0
1
2
3
-3
-2
-1
0
1
2
3
4
VacLi
VacBa
VacH
1 2
Fermi energy (eV)
Defect formation energy (eV)
VacLi
VacBa
VacH
0
1
2
3
-1
0
1
2
3
4
5
6
3
Fermi energy (eV)
Defect formation energy (eV)
0
1
2
3
-3
-2
-1
0
1
2
3
4
VacLi
VacBa
VacH
4
Fermi energy (eV)
Defect formation energy (eV)
VacLi
VacBa
VacH
0
1
2
3
-1
0
1
2
3
4
5
6
5
1
2
3
4
5
FIG. S12. The phase diagram and defect formation energies of BaLiH3 in diﬀerent conditions corresponding to the numbers
marked in diﬀerent facets.


## Page 24


14
Fraction
0
0.25
0.5
0.75
1.0
-1.75
-1.5
-1.25
-1.0
-0.75
-0.5
-0.25
0.0
Formation energy(eV/fu)
SrTe
Te
Sr
0.0
0.5
1.0
1.5
2.0
2.5
3.0
-0.5
-2
0
2
4
6
8
Defect formation energy (eV)
Fermi energy (eV)
VacSr
VacTe
SrTe
TeSr
Defect formation energy (eV)
Fermi energy (eV)
0.0
0
-2
2
4
6
8
10
12
-0.5
0.5
1.0
1.5
2.0
2.5
3.0
VacSr
VacTe
SrTe
TeSr
Sr-rich
Te-rich
Phase diagram
FIG. S13. The phase diagram and defect formation energies of SrTe in Sr-rich and Te-rich conditions.


## Page 25


15
Zn
ZnS
S
Al
Al2S3
Al2ZnS4
ZnAl
AlS
ZnS
VacAl
SAl
VacS
VacZn
SZn
AlZn
Fermi energy (eV)
0
1
2
3
4
Defect formation energy (eV)
0
2
4
6
8
-2
-4
-6
1
1
ZnAl
AlS
ZnS
VacAl
SAl
VacS
VacZn
SZn
AlZn
Fermi energy (eV)
Defect formation energy (eV)
0
1
2
3
4
4
6
2
0
-2
2
ZnAl
AlS
ZnS
VacAl
SAl
VacS
VacZn
SZn
AlZn
Fermi energy (eV)
Defect formation energy (eV)
0
1
2
3
4
-2
0
2
4
6
2
3
3
ZnAl
AlS
ZnS
VacAl
SAl
VacS
VacZn
SZn
AlZn
Fermi energy (eV)
Defect formation energy (eV)
0
1
2
3
4
-2
0
2
4
6
4
5
ZnAl
AlS
ZnS
VacAl
SAl
VacS
VacZn
SZn
AlZn
Fermi energy (eV)
Defect formation energy (eV)
0
1
2
3
4
-6
-4
-2
0
2
4
6
8
4
5
FIG. S14. The phase diagram and defect formation energies of Al2ZnS4 in diﬀerent conditions corresponding to the numbers
marked in diﬀerent facets.


## Page 26


16
[1] S. Ponc´e, E. R. Margine, C. Verdi, and F. Giustino, Comput. Phys. Commun. 209, 116 (2016).
[2] F. Giustino, Rev. Mod. Phys. 89, 015003 (2017).
[3] G. K. H. Madsen and D. J. Singh, Comput. Phys. Commun. 175, 67 (2006).
[4] M. Giantomassi, Core-electrons and self-consistency in the GW approximation from a PAW perspective, Ph.D. thesis,
Universit´e catholique de Louvain (2009), chapter 5 and appendix B.
[5] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder, and
K. A. Persson, APL Materials 1, 011002 (2013).
[6] “The Materials Project,” https://www.materialsproject.org/ (2013), [accessed September 1, 2013].
[7] F. Ricci, W. Chen, U. Aydemir, G. J. rey Snyder, G.-M. Rignanese, A. Jain, and G. Hautier, Sci. Data 4, 170085 (2017).
[8] J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. 118, 8207 (2003).
[9] E. N. Brothers, A. F. Izmaylov, J. O. Normand, V. Barone, and G. E. Scuseria, J. Chem. Phys. 129, 011102 (2008).
[10] C. G. Fonstad and R. H. Rediker, J. Appl. Phys. 42, 2911 (1971).
[11] S. Nakao, N. Yamada, T. Hitosugi, Y. Hirose, T. Shimada, and T. Hasegawa, Appl. Phys. Express 3, 031102 (2010).
[12] J. E. Dominguez, L. Fu, and X. Q. Pan, Appl. Phys. Lett. 81, 5168 (2002).
[13] D. C. Look, D. C. Reynolds, J. R. Sizelove, R. L. Jones, C. W. Litton, G. Cantwell,
and W. C. Harsch, Solid State
Commun. 105, 399 (1998).
[14] K. Ellmer, Nature Photon. 6, 809 (2012).
[15] D. S. Ginley, H. Hosono, and D. C. Paine, eds., “Handbook of transparent conductors,” (Springer, 2010).
[16] E. M. Kaidashev, M. Lorenz, H. von Wenckstern, A. Rahm, H.-C. Semmelhack, K.-H. Han, G. Benndorf, C. Bundesmann,
H. Hochmuth, and M. Grundmann, Appl. Phys. Lett. 82, 3901 (2003).
[17] C. Agashe, O. Kluth, J. H¨upkes, U. Zastrow, B. Rech, and M. Wuttig, J. Appl. Phys. 95, 1911 (2004).
[18] K. Ellmer, F. Kudella, R. Mientus, R. Schieck, and S. Fiechter, Semicond. Sci. Technol. 247, 15 (1994).
[19] K. Ellmer, J. Phys. D: Appl. Phys. 33, 17 (2000).
[20] R. L. Weiher, J. Appl. Phys. 33, 2834 (1962).
[21] R. Groth, Phys. stat. sol. 14, 69 (1966).
[22] H. K. M¨uller, Phys. Status Solidi 27, 723 (1968).
[23] S. Noguchi and H. Sakata, J. Phys. D : Appl. Phys. 13, 1129 (1980).
[24] C. A. Pan and T. P. Ma, J. Electron. Mater. 10, 43 (1981).
[25] I. Hamberg and C. G. Granqvist, J. Appl. Phys. 60, 123 (1986).
[26] S. J. Wen, G. Couturier, J. P. Chaminade, E. Marquestaut, J. Claverie, and P. Hagenmuller, J. Solid State Chem. 101,
203 (1992).
[27] M. Sawada and M. Higuchi, Thin Solid Films 317, 157 (1998).
[28] Y. Meng, X.-L. Yang, H.-X. Chen, J. Shen, Y.-M. Jiang, Z.-J. Zhang, and Z.-Y. Hua, Thin Solid Films 394, 219 (2001).
[29] C. Warmsingh, Y. Yoshida, D. W. Readey, C. W. Teplin, J. D. Perkins, P. A. Parilla, L. M. Gedvilas, B. M. Keyes, and
D. S. Ginley, J. Appl. Phys. 95, 3831 (2004).
[30] T. Koida, H. Fujiwara, and M. Kondo, Jpn. J. Appl. Phys. 46, 685 (2007).
[31] T. Koida, H. Fujiwara, and M. Kondo, Sol. Energy Mater Sol. Cells 93, 851 (2009).
[32] N. Oka, Y. Kawase, and Y. Shigesato, Thin Solid Films 520, 4101 (2012).
[33] M. R. Lorenz and J. F. W. R. J. Gambino, J. Phys. Chem. Solids 28, 403 (1967).
[34] N. Ueda, H. Hosono, R. Waseda, and H. Kawazoe, Appl. Phys. Lett. 71, 933 (1997).
[35] T. Oishi, Y. Koga, K. Harada, and M. Kasu, Appl. Phys. Express 8, 031101 (2015).
[36] N. Ma, N. Tanen, A. Verma, Z. Guo, T. Luo, H. Xing, and D. Jena, Appl. Phys. Lett. 109, 212101 (2016).
[37] H. Peng, D. O. Scanlon, V. Stevanovic, J. Vidal, G. W. Watson, and S. Lany, Phys. Rev. B 88, 115201 (2013).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]