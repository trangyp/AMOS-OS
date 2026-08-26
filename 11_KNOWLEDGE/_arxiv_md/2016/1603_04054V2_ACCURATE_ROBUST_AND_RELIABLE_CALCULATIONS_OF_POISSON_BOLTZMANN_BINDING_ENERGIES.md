---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1603.04054v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1603.04054v2_Accurate__robust_and_reliable_calculations_of_Poisson-Boltzmann_binding_energies

> Source: 1603.04054v2_Accurate__robust_and_reliable_calculations_of_Poisson-Boltzmann_binding_energies.pdf

> Pages: 23

---


## Page 1


Accurate, robust and reliable calculations of
Poisson-Boltzmann binding energies
Duc D. Nguyen,†,§ Bao Wang,†,§ and Guo-Wei Wei∗,†,‡,¶
Department of Mathematics
Michigan State University, MI 48824, USA, Department of Electrical and Computer Engineering
Michigan State University, MI 48824, USA, and Department of Biochemistry and Molecular
Biology
Michigan State University, MI 48824, USA
E-mail: wei@math.msu.edu
Abstract
Poisson-Boltzmann (PB) model is one of the most popular implicit solvent models in bio-
physical modeling and computation. The ability of providing accurate and reliable PB estima-
tion of electrostatic solvation free energy, ∆Gel, and binding free energy, ∆∆Gel, is important
to computational biophysics and biochemistry. Recently, it has been warned in the literature
(Journal of Chemical Theory and Computation 2013, 9, 3677-3685) that the widely used grid
spacing of 0.5Å produces unacceptable errors in ∆∆Gel estimation with the solvent exclude
surface (SES). In this work, we investigate the grid dependence of our PB solver (MIBPB)
∗To whom correspondence should be addressed
†Department of Mathematics
Michigan State University, MI 48824, USA
‡Department of Electrical and Computer Engineering
Michigan State University, MI 48824, USA
¶Department of Biochemistry and Molecular Biology
Michigan State University, MI 48824, USA
§The ﬁrst two authors contribute equally to this work
1
arXiv:1603.04054v2  [q-bio.BM]  9 Jun 2016


## Page 2


with SESs for estimating both electrostatic solvation free energies and electrostatic binding
free energies. It is found that the relative absolute error of ∆Gel obtained at the grid spacing of
1.0Å compared to ∆Gel at 0.2Å averaged over 153 molecules is less than 0.2%. Our results
indicate that the use of grid spacing 0.6Å ensures accuracy and reliability in ∆∆Gel calcula-
tion. In fact, the grid spacing of 1.1Å appears to deliver adequate accuracy for high throughput
screening.
1
Introduction
Electrostatics is ubiquitous in biomolecular and cellular systems and of paramount importance to
biological processes. Accurate and reliable prediction of electrostatic binding free energy, ∆∆Gel,
is crucial to biophysical modeling and computation. The prediction of ∆∆Gel plays a vital role
in the study of many cellular processes, such as signal transduction, gene expression, and protein
synthesis. Additionally, many pharmaceutical applications, specially in the ﬁnal stage of the drug
design, rely on the accurate and reliable calculation of binding free energy. Technically, the accu-
racy and reliability of electrostatic binding energy prediction depend essentially on the quality of
electrostatic solvation (∆Gel) estimation, which can be achieved by solving the Poisson-Boltzmann
(PB) equation in the implicit solvent model.1–5 In past decades, the development of a robust PB
solver catches much attention in computational biophysics and biochemistry. Mathematically, most
PB solvers reported in the literature are based on three major approaches, namely, the ﬁnite dif-
ference method (FDM),6 the ﬁnite element method (FEM),7 and the boundary element method
(BEM).8,9 Among them, the FDM is prevalently used in the ﬁeld due to its simplicity in imple-
mentation. The emblematic solvers in this category are Amber PBSA,10,11 Delphi,12,13 APBS14
and CHARMM PBEQ.6
Recently, it has been warned that “the widely used grid spacing of 0.5 Å produces unacceptable
errors in ∆∆Gel”.15 Although all results were obtained with the adaptive Cartesian grid (ACG)
ﬁnite difference PB equation solver16 in this work, similar results were reported in a later study17
by using APBS, DelPhi and PBSA. Therefore, these studies have arisen serious concerns about
2


## Page 3


the validity of using PB model for biomolecular electrostatic binding analysis at an affordable grid
spacing of 0.5 Å.
In the past few years, there have been many attempts to develop highly accurate PB solvers
using advance techniques for interface treatments.16,18–20 The later verison of the ACG solver16,18
has somewhat remedied the grid-dependence issue for estimates of binding energy. However, no
conﬁrmation for the reliable use of grid spacing of 0.5 Å in ∆∆Gel has been given. In this work,
we investigate the grid dependence of our PB solver (MIBPB)21,22 in estimating both electrostatic
solvation free energies and electrostatic binding free energies. The MIBPB solver is by far the only
existing method that is second-order accurate in L∞norm for solving the Poisson-Boltzmann equa-
tion with discontinuous dielectric constants, singular charge sources, and geometric singularities
from the solvent excluded surfaces (SESs) of biomolecules.21 Here the L∞norm means the max-
mum absolute error measure and “second order accurate” means that the error reduces four times
when the grid spacing is halved. Contrary to the ﬁndings in the literature,15 our results indicate
that the use of grid spacing 0.6 Å ensures accuracy and reliability in ∆∆Gel calculation. In fact,
a grid spacing of 1.1 Å appears to deliver adequate accuracy for high throughput screening. We
therefore believe that when it is used properly, the PB methodology is able to deliver accurate and
reliable electrostatic binding analysis.
2
Methods
2.1
MIBPB package
In the current work, we employ the our MIBPB package21,22 to predict the electrostatic solvation
free energy. The MIBPB package is a second-order convergence PB solver for dealing with the
SESs of biomolecules. Numerically, there are three major obstacles in constructing accurate and
reliable PB solvers. First, commonly used solvent-solute interfaces, i.e., the van der Walls (vdW)
surface, solvent accessible surface (SAS), and the solvent excluded surface (SES)23,24 admit ge-
ometric singularities, such as sharp tips, cusps and self-intersecting surfaces,25 which make the
3


## Page 4


rigorous enforcement of interface jump conditions a formidable task in PB solvers. An advanced
mathematical interface techniques, the matched interface and boundary (MIB) method,26–31 is
employed in the MIBPB package to achieve the second order accuracy in handling biomolecu-
lar SESs. Additionally, the atomic singular charges described by the delta functions give rise to
another difﬁculty in constructing highly accurate PB solver. A Dirichlet-to-Neumann map tech-
nique has been developed in the MIBPB package to avoid the numerical approximation of singular
charges by using the analytical Green’s functions.32 Finally, the nonlinear Boltzmann term can
affect solver efﬁciency when handled inappropriately, particularly for BEMs. A quasi-Newton
algorithm is implemented in the MIBPB package21,22 to take care the nonlinear term.21,22
2.2
Interface generation
Many studies suggest that SES is able to deliver the state of the art accurate modeling of the sol-
vated molecule.7,9,13 As a result, much effort has been paid to developing an accurate and robust
SES software.25,33 However, the MSMS software25 generates a Lagrangian representation of the
SES and is inconvenient for the Cartesian domain implementation of PB solvers. A Lagrangian
to Eulerian transformation is required to convert MSMS surfaces for our Cartesian based MIBPB
solver.4 Most recently, we have developed a new SES software, Eulerian solvent excluded sur-
face (ESES), to directly generate the SESs in the Eulerian representation.34 Our ESES software
enables the MIBPB solver to produce a reliable ∆Gel. Both MSMS and ESES are supported by
our MIBPB software. By increasing the MSMS surface density, the electrostatic solvation free
energies calculated by using MSMS converge to those obtained by using ESES.34 Therefore, only
results employing ESES are shown in this work.
2.3
Data sets
In the present work, we adopt three sets of biomolecular complexes employed in the literature15
for solvation free energy and binding free energy estimations. Speciﬁcally, the ﬁrst set, Data
Set 1, is a collection of DNA-minor groove drug complexes having a narrow range of ∆∆G.
4


## Page 5


The Protein Data Bank (PDB) IDs (PDBIDs) for this set are as follows: 102d, 109d, 121d,
127d, 129d, 166d, 195d, 1d30, 1d63, 1d64, 1d86, 1dne, 1eel, 1fmq, 1fms, 1jtl, 1lex, 1prp,
227d, 261d, 164d, 289d, 298d, 2dbe, 302d, 311d, 328d, and 360d. The second set, Data Set
2, includes various wild-type and mutant barnase-barstar complexes.
Its PDBIDs are as fol-
lows: 1b27, 1b2s, 1b2u, 1b3s, 2aza4, 1x1w, 1x1y, 1x1u, and 1x1x. In the last set, Data Set 3,
we investigate RNA-peptide complexes with following PDBIDs: 1a1t, 1a4t, 1biv, 1exy, 1g70,
1hji, 1i9f, 1mnb, 1nyb, 1qfq, 1ull, 1zbn, 2a9x, and 484d. The detail of the structural prepos-
sessing can be found in Ref.
Harris et al..
The data sets can be downloaded from website
http://www.sb.fsu.edu/˜mfenley/convergence/downloads/convergence_pqr_sets.tar.gz. They are also
available from the present authors upon request.
2.4
Poisson-Boltzmann calculation details
The electrostatics binding free energy is a measure of binding afﬁnity of two compounds due to
the electrostatics interaction. Based on the free energy cycle, the electrostatics binding free energy
can be calculated by the following formula35
∆∆Gel = (∆Gel)AB −(∆Gel)A −(∆Gel)B +(∆∆Gel)Coulomb ,
(1)
where (∆Gel)AB is the electrostatic solvation free energy of the bounded complex AB, (∆Gel)A and
(∆Gel)B are the electrostatic solvation free energies of the unbounded components A and B, and
(∆∆Gel)Coulomb is the electrostatic binding free energy of the two components in vacuum.
The electrostatic solvation free energies ∆Gel are obtained by using MIBPB software21,22 while
the binding energy (∆∆Gel)Coulomb is easily evaluated analytically via the following formula
(∆∆Gel)Coulomb = ∑
i,j
qiq j
εmri j
,
∀i ∈A, j ∈B,
(2)
where qi and qj are the corresponding charges of the given pair of atoms, and ri j is the distance be-
tween this pair. Here, εm is the dielectric constant of the solute region. Table S3 (in the supporting
5


## Page 6


(a) PDBID: 121d
(b) PDBID: 1b3s
(c) PDBID: 1biv
Figure 1: Illustration of surface electrostatic potentials (in units of kcal/mol/e) for three complexes,
generated by Chimera software.36 (a) PDBID: 121d (in Drug-DNA complexes); (b) PDBID: 1b3s
(in barnase-barstar complexes); (c) PDBID: 1biv (in RNA-peptide complexes).
information) lists (∆∆Gel)Coulomb values of 51 studied complexes.
In all our calculations, the absolute temperature of the ionic solvent is chosen to be T = 298 K,
the dielectric constants for solute and solvent are 1 and 80, and the ionic strength is 0.1 M NaCl.
The PBE is solved by the linearized solver, but the nonlinear one does not produce any notably
differences. The incomplete LU biconjugate gradient squared (ILUBGS) solver is employed to
solve all linear systems risen by the MIBPB approach. To maintain consistent computations of
the PB solver at different grid sizes, the criteria convergence of ILUBGS solver measured by L2-
norm is set to be 10−6, and the maximum iteration number is set to 100,000. The predictions of
MIBPB solver on ∆Gel and ∆∆Gel are conﬁrmed by other solvers such as PBSA,10,11 Delphi,12,13
and APBS14 at the grid size of 0.2 Å, see Table S2 of Supporting Information.
3
Results and discussion
As described above, we consider three sets of binding complexes, namely, drug-DNA, barnase-
barstar and RNA-peptide systems. For the sake of illustration, three sample surface electrostatic
potentials, each from one distinct set, are depicted in Fig. 1. PDBIDs for these three complexes
6


## Page 7


Table 1: R2 values and best ﬁtting lines of electrostatic solvation free energies with different grid
sizes.
Grid sizes (pair)
R2
Best ﬁtting line
DNA-drug
(0.2,0.3)
1.0000
y = 1.0000x−0.0196
(0.2,0.4)
1.0000
y = 1.0000x−0.0081
(0.2,0.5)
1.0000
y = 1.0001x−0.0621
(0.2,0.6)
1.0000
y = 1.0001x−0.2230
(0.2,0.7)
1.0000
y = 1.0003x−0.2537
(0.2,0.8)
1.0000
y = 1.0003x−0.4161
(0.2,0.9)
1.0000
y = 1.0003x−0.2999
(0.2,1.0)
1.0000
y = 1.0005x−0.0066
(0.2,1.1)
1.0000
y = 1.0004x−0.2485
Barnase-barstar
(0.2,0.3)
1.0000
y = 1.0002x+0.1590
(0.2,0.4)
1.0000
y = 1.0005x+0.3524
(0.2,0.5)
1.0000
y = 1.0012x+0.8735
(0.2,0.6)
1.0000
y = 1.0010x−0.2246
(0.2,0.7)
1.0000
y = 1.0017x−0.3748
(0.2,0.8)
1.0000
y = 1.0009x−0.9576
(0.2,0.9)
0.9999
y = 1.0015x+0.4749
(0.2,1.0)
0.9999
y = 0.9986x−2.9739
(0.2,1.1)
0.9997
y = 0.9972x−4.3801
RNA-peptide
(0.2,0.3)
1.0000
y = 1.0000x−0.0445
(0.2,0.4)
1.0000
y = 1.0000x−0.1333
(0.2,0.5)
1.0000
y = 1.0000x−0.3343
(0.2,0.6)
1.0000
y = 1.0000x−0.1916
(0.2,0.7)
1.0000
y = 1.0001x−0.5377
(0.2,0.8)
1.0000
y = 1.0001x−0.8198
(0.2,0.9)
1.0000
y = 1.0002x−0.9564
(0.2,1.0)
1.0000
y = 1.0003x−0.8868
(0.2,1.1)
1.0000
y = 1.0005x−2.2504
are respectively 121d (in Drug-DNA complexes), 1b3s (in barnase-barstar complexes), and 1biv
(in RNA-peptide complexes). In the rest of this section, we explore the inﬂuence of grid spacing
in Poisson-Boltzmann equation solvation and binding free energy estimations using our MIBPB
solver.
7


## Page 8


Figure 2: Electrostatic solvation free energy, for all complexes and unbounded components of
three data sets, with different grid sizes plotted against the one computed with a ﬁnest grid size
of h = 0.2Å. (a) DNA-drug with pair (0.2Å,0.3Å); (b) DNA-drug with pair (0.2Å,0.7Å); (c)
DNA-drug with pair (0.2Å,1.1Å); (d) Barnase-barstar with pair (0.2Å,0.3Å); (e) Barnase-barstar
with pair (0.2Å,0.7Å); (f) Barnase-Barstar with pair (0.2Å,1.1Å); (g) RNA-peptide with pair
(0.2Å,0.3Å); (h) RNA-peptide with pair (0.2Å,0.7Å); (i) RNA-peptide with pair (0.2Å,1.1Å).
3.1
The inﬂuence of grid spacing in ∆Gel estimation
We ﬁrst examine the accuracy and robustness of our MIBPB solver in predicting the electrostatic
solvation free energies of the aforementioned three data sets. Some previous literature37,38 has
8


## Page 9


Figure 3: Averaged relative absolute error of the electrostatic solvation free energies for all the 153
molecules with mesh size reﬁnements from 1.1Å to 0.2Å.
recognized that a grid size of h = 0.5Å is small enough to produce a reliable ∆Gel. Such an
observation certainly remains for the MIBPB solver. In fact, our PB solver is able to deliver a very
well-convergent calculations of electrostatic solvation free energies at as coarse grid sizes as 1.0Å
and 1.1Å.
In the current calculations, the ﬁnest grid size is chosen to be 0.2Å, and the coarser grid sizes
are between 0.3Å and 1.1Å. Figure 2 depicts the correlations of ∆Gel at various meshes for all
complexes and unbounded components of three data sets. The electrostatic solvation free ener-
gies obtained at the ﬁnest grid spacing of 0.2Å are plotted against those computed from coarser
grid spacings of 0.3Å, 0.7Å and 1.1Å. Obviously, the best ﬁtting lines for these data at var-
ious coarse grid spacings produce near perfect alignments between the ﬁnest mesh results and
those from coarse meshes. As shown in Table 1, R2 and slope values at the pair of grid sizes
(0.2Å,1.1Å) for DNA-drug, barnase-barstar and RNA-peptide are, respectively, (1.0000,1.0004),
(0.9997,0.9972), and (1.0000,1.0005). These results indicate the accuracy and robustness in the
9


## Page 10


MIBPB prediction of electrostatic solvation free energies (∆Gel). Table S1, in the Supporting In-
formation, reports the values ∆Gel for all the 51 complexes and associated 102 components studied
in this work. Finally, we examine the performance of our solver by considering the relative abso-
lute error, the difference between results obtained with coarser and the ﬁnest grid spacings, deﬁned
as follows
Relative absolute error .=

∆Gel,h −∆Gel,h=0.2
∆Gel,h=0.2
.
(3)
Figure 3 illustrates the averaged relative absolute errors, i.e., the average of relative absolute
errors designated in Eq. (??) over all the 153 discussed molecules, at different mesh sizes. It can be
seen from Fig. 3 that the averaged relative absolute errors at all studied cases are less than 0.31%,
and for any grid spacing smaller than 1.1Å, these errors are always below 0.2%. This behavior
further indicates the grid size independence of our PB solver over the normal grid-size range in
molecular biophysical applications.
3.2
The inﬂuence of grid spacing in ∆∆Gel estimation
Motivated by well-converged estimations of electrostatic solvation free energies at very coarse grid
spacings as previously discussed, we are interested in predicting the binding free energies for all
RNA-drug, barnase-barstar, and RNA-peptide complexes using our MIBPB package.
Similar to the study of the convergence of ∆Gel, we correlate the binding free energy calculated
at the ﬁnest grid spacing, h = 0.2Å, and ones estimated at coarser mesh sizes, h = 0.3Å,··· ,1.1Å.
Figure 4 illustrates these relationships with the regression lines whose parameters are revealed in
Table 2. Since the previous discussion conﬁrms MIBPB solver can produce very good R-squared
values even at very coarse grid spacings, it is interesting to explore whether a similar behavior can
be found for binding energy estimation. Indeed, the PB binding energy estimation behaves the
same as the PB solvation calculation in our MIBPB technique. Speciﬁcally, R2 is always 1 at the
ﬁne mesh, h = 0.3Å. Moreover, these values are still satisfactory at relatively coarser mesh sizes.
For example, at the grid spacing of h = 1.1, the R2 and slope of the regression line for DNA-drug,
10


## Page 11


Figure 4: Electrostatic binding free energy, for all complexes with different grid sizes plotted
against the one computed with a ﬁnest grid size of h = 0.2Å. (a) DNA-drug with pair (0.2Å,0.3Å);
(b) DNA-drug with pair (0.2Å,0.7Å); (c) DNA-drug with pair (0.2Å,1.1Å); (d) Barnase-barstar
with pair (0.2Å,0.3Å); (e) Barnase-barstar with pair (0.2Å,0.7Å); (f) Barnase-barstar with pair
(0.2Å,1.1Å); (g) RNA-peptide with pair (0.2Å,0.3Å); (h) RNA-peptide with pair (0.2Å,0.7Å);
(i) RNA-peptide with pair (0.2Å,1.1Å).
barnase-barstar, and RNA-peptide complexes are, respectively, (0.9747,1.0081), (0.8002,0.8187),
and (0.9998, 0.9937). In contrast, the R-squared values reported in Ref.,15 computed between
0.3Å and 1.0Å, are unacceptable for SESs, and usually less than 0.62. Our statistical measures
11


## Page 12


Table 2: R2 values and best ﬁtting lines of electrostatic binding free energies with different grid
sizes.
Grid sizes (pair)
R2
Best ﬁtting line
DNA-drug
(0.2,0.3)
1.0000
y = 0.9993x+0.0194
(0.2,0.4)
0.9999
y = 0.9987x+0.0273
(0.2,0.5)
0.9998
y = 1.0028x+0.0164
(0.2,0.6)
0.9991
y = 1.0047x+0.2256
(0.2,0.7)
0.9982
y = 1.0074x+0.1394
(0.2,0.8)
0.9966
y = 1.0110x+0.1484
(0.2,0.9)
0.9906
y = 0.9655x+1.2385
(0.2,1.0)
0.9875
y = 0.9827x+0.5894
(0.2,1.1)
0.9747
y = 1.0081x+0.0709
Barnase-barstar
(0.2,0.3)
0.9999
y = 0.9974x+0.2035
(0.2,0.4)
0.9995
y = 0.9997x−0.0492
(0.2,0.5)
0.9923
y = 1.0318x−2.7755
(0.2,0.6)
0.9946
y = 0.9878x+1.5525
(0.2,0.7)
0.9932
y = 1.0090x+0.1819
(0.2,0.8)
0.9883
y = 0.9766x+3.7333
(0.2,0.9)
0.9493
y = 0.9382x+5.3970
(0.2,1.0)
0.9384
y = 1.0912x−3.8377
(0.2,1.1)
0.8002
y = 0.8187x+18.2837
RNA-peptide
(0.2,0.3)
1.0000
y = 0.9997x−0.0655
(0.2,0.4)
1.0000
y = 1.0001x−0.1106
(0.2,0.5)
1.0000
y = 1.0012x−0.2755
(0.2,0.6)
1.0000
y = 0.9999x+0.2021
(0.2,0.7)
0.9999
y = 1.0037x−0.3756
(0.2,0.8)
1.0000
y = 1.0004x+0.6673
(0.2,0.9)
0.9999
y = 0.9927x+1.9755
(0.2,1.0)
0.9997
y = 0.9923x+2.8775
(0.2,1.1)
0.9998
y = 0.9937x+1.7992
strongly support the reliable binding energy prediction of our solver at coarse grid sizes. Table 3
displays the binding free energy for all complexes with different grid spacings. As can be seen from
Table 3, the difference between binding energies at coarse meshes and the ﬁnest mesh, h = 0.2Å,
is mostly less than 10 kcal/mol for all complexes.
The trend of binding free energy at different grid spacings can be seen clearly in Figs. 5 which
plots ∆∆Gel against grid sizes varying between 0.2Å and 1.1Å for DNA-drug complexes. Similar
12


## Page 13


Table 3: Electrostatic binding free energies (in units of kcal/mol), ∆∆Gel, for all of the
complexes used in this study at different grid sizes.
complexes
1.1Å
1.0Å
0.9Å
0.8Å
0.7Å
0.6Å
0.5Å
0.4Å
0.3Å
0.2Å
DNA-drug
102d
9.45
10.50
8.73
10.01
10.21
10.76
10.53
10.45
10.34
10.31
109d
3.61
2.18
2.30
3.72
2.63
2.07
2.66
2.69
2.82
2.72
121d
23.95
23.99
23.80
24.05
22.84
23.65
24.10
23.94
23.96
23.93
127d
27.60
28.80
28.45
28.89
28.88
28.93
29.27
29.16
29.12
29.12
129d
37.58
40.23
39.92
39.03
39.52
39.90
40.04
40.15
40.20
40.24
166d
15.04
16.60
13.97
14.93
14.91
15.49
15.47
15.62
15.67
15.67
195d
2.74
3.73
2.80
2.63
2.77
2.77
2.63
2.69
2.72
2.73
1d30
11.27
10.01
10.71
9.31
10.26
10.12
10.40
10.75
10.53
10.59
1d63
15.51
12.83
7.08
12.56
12.07
11.24
12.10
12.29
12.34
12.39
1d64
14.98
14.11
14.26
14.03
14.86
14.24
14.51
14.57
14.59
14.58
1d86
27.37
25.53
24.50
25.88
25.04
25.57
25.39
25.44
25.50
25.54
1dne
22.26
22.73
22.32
22.92
22.48
22.62
22.58
22.74
22.83
22.81
1eel
16.71
17.06
14.94
14.82
14.77
14.60
15.08
14.85
15.15
15.07
1fmq
12.35
13.40
14.28
14.72
15.27
15.09
15.30
15.36
15.36
15.37
1fms
27.08
26.14
25.17
24.52
25.41
25.93
25.82
25.75
25.71
25.74
1jtl
11.62
10.99
11.80
11.47
11.30
11.28
11.37
11.28
11.41
11.45
1lex
13.47
10.37
9.79
9.44
8.74
9.74
9.81
9.70
9.70
9.70
1prp
11.30
11.93
10.78
10.88
11.01
11.55
11.55
11.49
11.61
11.61
227d
6.28
4.79
5.96
3.79
5.47
5.16
5.80
5.75
5.46
5.58
261d
1.91
3.00
1.75
1.55
2.60
2.79
2.97
2.76
2.80
2.85
264d
33.64
32.35
31.57
30.83
32.09
31.97
32.07
32.20
32.31
32.34
289d
15.32
15.71
17.94
16.70
16.57
16.21
16.22
16.56
16.59
16.56
298d
11.65
15.94
14.81
15.89
14.87
14.88
15.38
15.45
15.50
15.41
2dbe
3.48
5.06
3.49
6.14
5.51
5.77
5.76
5.88
5.68
5.81
302d
23.28
25.22
24.91
25.49
24.95
25.00
24.87
25.29
25.17
25.19
311d
11.76
3.36
7.15
9.72
11.12
8.17
8.98
9.34
9.30
9.32
328d
14.25
16.21
17.38
17.85
16.79
17.14
17.84
17.68
17.54
17.54
360d
54.41
54.72
56.63
54.59
55.38
54.56
55.44
55.80
55.61
55.57
Barnase-barstar
1b27
86.80
83.08
95.40
82.48
87.05
89.40
87.35
87.96
86.96
87.05
1b2s
67.80
66.33
68.81
71.75
70.03
71.47
72.32
71.93
72.25
72.12
1b2u
85.97
76.39
74.78
78.29
75.29
77.35
77.15
78.38
78.87
78.57
1b3s
48.41
56.58
49.61
46.02
49.87
48.17
53.44
49.38
49.07
49.25
1x1u
61.75
66.86
74.53
75.07
77.56
76.56
75.06
76.41
76.06
75.95
1x1w
90.62
87.91
99.13
93.67
94.65
93.55
95.53
95.32
95.47
95.30
1x1x
115.79
110.40
110.45
112.19
113.51
114.45
115.30
114.65
114.62
114.65
1x1y
67.27
88.13
89.80
90.39
87.87
87.24
88.54
88.91
89.20
89.21
2za4
74.13
70.86
70.64
69.80
72.45
73.22
73.26
74.18
74.00
74.35
RNA-peptide
1a1t*
62.24
58.24
61.71
61.89
62.94
63.18
62.88
62.75
62.95
63.00
1a4t*
72.37
72.44
69.76
69.94
71.19
72.46
72.41
72.39
72.24
72.27
1biv*
41.80
40.73
42.07
44.90
45.66
44.70
44.69
44.75
44.86
44.76
1exy*
178.36
178.17
178.16
176.29
178.70
176.91
177.52
177.50
177.70
177.36
1g70
133.22
131.38
132.83
132.75
132.83
133.85
133.94
134.37
134.34
133.53
1hji
46.78
46.06
49.80
50.70
51.51
51.26
51.21
51.42
51.17
51.23
1i9f
-19.78
-22.55
-22.49
-19.44
-19.31
-19.20
-19.18
-19.18
-19.20
-19.22
1mnb
126.65
129.00
127.74
126.95
127.80
127.82
128.30
128.15
128.15
128.20
1nyb
-14.63
-13.07
-13.62
-12.58
-11.16
-13.04
-12.79
-12.45
-12.41
-12.61
1qfq
18.09
19.84
16.64
20.52
21.19
20.03
22.60
20.66
20.19
20.32
1ull*
-53.38
-58.11
-54.20
-53.61
-51.66
-53.28
-52.52
-52.76
-52.66
-52.75
1zbn*
216.31
214.29
215.60
214.96
214.84
216.05
215.70
215.95
215.94
215.74
2a9x
385.99
384.41
385.18
385.36
385.05
385.20
385.36
385.36
385.43
385.44
484d*
129.72
129.65
133.42
132.09
131.34
132.03
132.79
133.20
133.23
133.38
* Results are signiﬁcantly different (>50 kcal/mol) from those in Ref. 15
ﬁgures for barnase-barstar and RNA-peptide complexes can be referred to Figs. S1 and S2 in the
Supporting Information. Based on these ﬁgures, our solver can rank the binding free energy for
DNA-drug complexes at grid spacing of 0.6Å, barnase-barstar complexes at grid spacing of 0.6Å,
13


## Page 14


Figure 5: Binding electrostatic energy for DNA-drug complexes with grid sizes from 0.2Å to
1.1Å. The markers and PDBIDs are as follows yellow circle : 102d, magenta circle : 109d, cyan
circle : 121d, green circle : 127d, red circle : 129d, blue circle : 166d, black circle : 195d, yellow
diamond : 1d30, magenta diamond : 1d63, cyan diamond : 1d64, green diamond : 1d86, red
diamond : 1dne, blue diamond : 1eel, black diamond : 1fmq, yellow square : 1fms, magenta
square : 1jtl, cyan square : 1lex, green square : 1prp, red square : 227d, blue square : 261d, black
square : 264d, yellow triangle: 289d, magenta triangle: 298d, cyan triangle: 2dbe, green triangle:
302d, red triangle: 311d, blue triangle: 328d, black triangle: 360d.
Figure 6: Averaged absolute error of the binding free energies for all the 51 complexes with mesh
size reﬁnements from 1.1Å to 0.2Å.
and RNA-peptide complexes at signiﬁcantly coarse grid spacing of 1.1Å. To further assess the
reliable estimates of binding energy of our MIBPB solver, we consider the absolute difference
14


## Page 15


Figure 7: Binding energies of two complexes PDB IDs: 360d (marked by circle) and 1hji (marked
by square) at 30 different grid positions.
between results computed at a coarser grid spacing and the ﬁnest grid spacing deﬁned by
δ∆∆Gel =
∆∆Gel,h −∆∆Gel,h=0.2
.
(4)
Figure 6 plots the averaged absolute errors, δ∆∆Gel, i.e., the average of absolute errors deﬁned
in Eq. (??) over all 51 complexes, at different mesh sizes. It is seen that even the use of grid
spacing of 0.7Å still delivers an averaged binding calculation error under 1 kcal/mol for this set of
complexes. Therefore, we can draw a conclusion that the common use of grid size being 0.5Å is
still adequate for predicting the binding energy free without producing a misleading result.
Grid positioning error is another feature to validate the robustness and accuracy of a PB solver.
To examine such numerical error for our MIBPB solver, we consider two protein complexes with
PDBIDs: 360d and 1hji. To estimate the standard deviation, σbd in ∆∆Gel, we randomly generate
29 grid positions around the initial origin with the amplitude of the random seed being ±0.5h,
where h = 0.5 Å is the grid spacing. Then ∆∆Gel is evaluated at all of the 30 grid positions.
Figure 7 plots electrostatic binding energies at 30 distinct samples of grid positions, including
the original one marked by Sample 0 on the graph. The σbd values of complexes 360d and 1hji
are found to be 0.18 and 0.21, respectively. These results indicate that the MIBPB solver is not
15


## Page 16


sensitive to grid position.
Note that in Table 3, some binding energies obtained in our calculations, all from RNA-peptide
complexes, differ signiﬁcantly from those reported in Ref.,15 i.e., more than 50 kcal/mol at the
ﬁnest grid spacing, under the same parametrization and data inputs. However, overall, our results
have a good agreement with those in Ref.15 with R2 = 0.9135 for RNA-peptide complexes. To
further support our calculations, we have employed PBSA, Delphi, and APBS for electrostatic
energy calculations at the grid size of 0.2 Å. We note that results obtained from these solvers are
in excellent agreements, i.e., R2 > 0.98, with ours. The electrostatic energies calculated by PBSA,
Delphi, and APBS solvers are listed in Table S2 of Supporting Information.
4
Concluding remarks
Poisson-Boltzmann (PB) theory is an established model for biomolecular electrostatic analysis
and has been widely used in electrostatic solvation ∆Gel and binding energy ∆∆Gel estimations.
However, doubt has been cast on the validity of the commonly used grid spacing of 0.5 Å for
producing converged estimates of ∆∆Gel due to the unacceptable errors observed in the calcula-
tion using the solvent excluded surface (SES) and the adaptive Cartesian grid (ACG) ﬁnite differ-
ence PB equation solver.15 Three sets of biomolecular complexes, namely, DNA-drug complexes,
barnase-barstar complexes, and RNA-peptide complexes, are employed in the study. The discrep-
ancies between results obtained from different surface deﬁnitions were also utilized to support the
general pessimism for the PB methodology.
In this work, we employ the MIBPB software21,32 to estimate electrostatic solvation free en-
ergy, ∆Gel, and binding free electrostatic energy, ∆∆Gel, for the three sets of biomolecular com-
plexes used in Ref.15 The popular SES is adopted in the present work. In our ∆Gel estimation, the
averaged relative absolute error computed at a relatively coarse grid size of 1.1Å against the ﬁnest
grid size of 0.2 Å over 153 studied biomolecules is less than 0.31%. The same error obtained at
the grid size of 1.0Å is less than 0.2%. These results indicate the reliability of using the MIBPB
16


## Page 17


solver at the grid spacing of 1.0Å or even 1.1Å for electrostatic solvation analysis. The robustness
and accuracy of MIBPB solver for estimates of ∆Gel have been reported for 24 proteins in the
literature.21,32 This characteristics has been conﬁrmed again in the present work for DNA-drug
complexes, barnase-barstar complexes, and RNA-peptide complexes.
The well-converged ∆Gel produced by our solver enables a promising performance in predict-
ing ∆∆Gel at a coarse grid spacing. Indeed, numerical estimates of ∆∆Gel in the current work
reveals that ∆∆Gel obtained at a 1.1Å grid spacing mostly differ by less than 10 kcal/mol from
that achieved by using a 0.2Å grid spacing. Moreover, MIBPB solver conducted at grid size of
0.6Å perfectly produces a well-converged ∆∆Gel, and qualitatively ranks the complexes in term
of their binding free energies. Therefore, the current results support an opinion that the widely
used grid size of 0.5Å can give reliable and accurate enough predictions of both electrostatic free
energy39,40 and binding free energy.
To develop highly accurate, robust and reliable PB solvers for biomolecular electrostatics, it is
crucial to validate one’s numerical methods by appropriate norms and against realistic problems.
We emphasize that as an elliptic interface problem, it is important to measure the convergence of
PB solvers in the L∞norm, or maximum absolute error, because integral norms, such as L1 and
L2, are insensitive to the performance of numerical methods near the interface. Additionally, the
convergence should be tested by solving the PB equation, rather than by calculating the solvation
free energy. Finally, validation should be carried out by using the SESs of proteins, rather than
smooth surfaces, such as a sphere.
Supporting Information Available
Electrostatic free energies calculated by different solvers, namely MIBPB, DELPHI, PBSA and
APBS; Coulombic binding energies; binding energy plots for barnase-barstar and RNA-peptide
complexes (ﬁlename: jctc_si_bdenergy.pdf).
This material is available free of charge via the Internet at http://pubs.acs.org/.
17


## Page 18


Acknowledgement
This work was supported in part by NSF Grant Nos. IIS- 1302285 and DMS-1160352, NIH Grant
No. R01GM-090208 and MSU Center for Mathematical Molecular Biosciences Initiative. DDN
and GWW thank the Mathematical Biosciences Institute for its hospitality and support during their
visit in Ohio State University, where this manuscript was ﬁnalized. This manuscript was reviewed
by Professors Emil Alexov and Ray Luo prior its submission.
References
(1) Gilson, M. K.; Sharp, K.; Honig, B. Calculating the Electrostatic Potential of Molecules in
Solution: Method and error assessment. J. Comp. Chem. 1987, 9, 327–335.
(2) Gilson, M. K.; Davis, M. E.; Luty, B. A.; McCammon, J. A. Computation of electrostatic
forces on solvated molecules using the Poisson-Boltzmann equation. Journal of Physical
Chemistry 1993, 97, 3591–3600.
(3) Talley, K.; Ng, C.; Shoppell, M.; Kundrotas, P.; Alexov, E. On the electrostatic component of
protein-protein binding free energy. PMC Biophysics 2008, 1:2, 1–23.
(4) Zhou, Y. C.; Feig, M.; Wei, G. W. Highly accurate biomolecular electrostatics in continuum
dielectric environments. Journal of Computational Chemistry 2008, 29, 87–97.
(5) Ren, P.; Chun, J.; Thomas, D. G.; Schnieders, M. J.; Marucho, M.; Zhang, J.; Baker, N. A.
Biomolecular electrostatics and solvation: a computational perspective. Quarterly reviews of
biophysics 2012, 45(04), 427–491.
(6) Jo, S.; Vargyas, M.; Vasko-Szedlar, J.; Roux, B.; Im, W. PBEQ-Solver for online visualization
of electrostatic potential of biomolecules. Nucleic Acids Research 2008, 36, W270 –W275.
(7) Baker, N. A.; Sept, D.; Holst, M. J.; Mccammon, J. A. The adaptive multilevel ﬁnite element
solution of the Poisson-Boltzmann equation on massively parallel computers. IBM Journal
of Research and Development 2001, 45, 427–438.
18


## Page 19


(8) Geng, W. H.; Krasny, R. A treecode-accelerated boundary integral Poisson-Boltzmann solver
for continuum electrostatics of solvated biomolecules. J. Comput. Phys. 2013, 247, 62–87.
(9) Lu, B.; Cheng, X.; Huang, J.; McCammon, J. A. AFMPB: An Adaptive Fast Multipole
Poisson-Boltzmann Solver for Calculating Electrostatics in Biomolecular Systems. Comput.
Phys. Commun. 2013, 184, 2618–2619.
(10) Wang, J.; Tan, C. H.; Tan, Y. H.; Lu, Q.; Luo, R. Poisson-Boltzmann solvents in molecular
dynamics Simulations. Communications in Computational Physics 2008, 3(5), 1010–1031.
(11) Cai, Q.; Hsieh, M. J.; Wang, J.; Luo, R. Performance of Nonlinear Finite-Difference Poisson-
Boltzmann Solvers. Journal of Chemical Theory and Computation 2009, 6(1), 203–211.
(12) Li, L.; Li, C.; Sarkar, S.; Zhang, J.; Witham, S.; Zhang, Z.; Wang, L.; Smith, N.; Petukh, M.;
Alexov, E. Delphi: a comprehensive suite for Delphi software and associated resources. BMC
Biophysics 2012, 5:9, 2046–1682.
(13) Rocchia, W.; Sridharan, S.; Nicholls, A.; Alexov, E.; Chiabrera, A.; Honig, B. Rapid grid-
based construction of the molecular surface and the use of induced surface charge to calculate
reaction ﬁeld energies: Applications to the molecular systems and geometric objects. Journal
of Computational Chemistry 2002, 23, 128 – 137.
(14) Baker, N. A.; Sept, D.; Joseph, S.; Holst, M. J.; McCammon, J. A. Electrostatics of nanosys-
tems: Application to microtubules and the ribosome. Proceedings of the National Academy
of Sciences of the United States of America 2001, 98, 10037–10041.
(15) Harris, R. C.; Boschitsch, A. H.; Fenley, M. O. Inﬂuence of Grid Spacing in Poisson-
Boltzmann Equation Binding Energy Estimation. Journal of Chemical Theory and Computa-
tion 2013, 9, 3677–3685.
(16) Boschitsch, A. H.; Fenley, M. O. Chapter 4, The Adaptive Cartesian Grid-Based Poisson–
Boltzmann Solver: Energy and Surface Electrostatic Properties, in Computational Electro-
19


## Page 20


statics for Biological Applications: Geometric and Numerical Approaches to the Descrip-
tion of Electrostatic Interaction Between Macromolecules, Rocchia, W., Spagnuolo, M., Eds.
Cham, 2015 2015, 73–110.
(17) Sorensen, J.; Fenley, M. O.; Amaro, R. E. Chapter 3, A Comprehensive Exploration of
Physical and Numerical Parameters in the Poisson-Boltzmann Equation for Applications to
Receptor-Ligand Binding, in Computational Electrostatics for Biological Applications: Ge-
ometric and Numerical Approaches to the Description of Electrostatic Interaction Between
Macromolecules, Rocchia, W., Spagnuolo, M., Eds. Cham, 2015 2015, 39–71.
(18) Fenley, M. O.; Harris, R. C.; Mackoy, T.; Boschitsch, A. H. Features of CPB: A Poisson–
Boltzmann solver that uses an adaptive cartesian grid. J. Comput. Chem. 2015, 36, 235–243.
(19) Wang, C.; Wang, J.; Cai, Q.; Li, Z.; Zhao, H. K.; Luo, R. Exploring accurate Poisson–
Boltzmann methods for biomolecular simulations. Comput. Theor. Chem. 2014, 1:2, 34–44.
(20) Mirzadeh, M.; Theillard, M.; Gibou, F. A second-order discretization of the nonlinear
Poisson–Boltzmann equation over irregular geometries using non-graded adaptive Cartesian
grids. J. Comput. Phys. 2011, 230, 2125–2140.
(21) Chen, D.; Chen, Z.; Chen, C.; Geng, W. H.; Wei, G. W. MIBPB: A software package for
electrostatic analysis. J. Comput. Chem. 2011, 32, 657 – 670.
(22) Wang, B.; Nguyen, D. D.; Zhao, Z.; Cang, Z.; Wei, G.-W. MIBPB: An accurate and reliable
software package for electrostatic analysis. Preprint 2015,
(23) Richards, F. M. Areas, Volumes, Packing, and Protein Structure. Annual Review of Biophysics
and Bioengineering 1977, 6, 151–176.
(24) Connolly, M. L. Analytical molecular surface calculation. Journal of Applied Crystallogra-
phy 1983, 16, 548–558.
20


## Page 21


(25) Sanner, M. F.; Olson, A. J.; Spehner, J. C. Reduced surface: An efﬁcient way to compute
molecular surfaces. Biopolymers 1996, 38, 305–320.
(26) Zhou, Y. C.; Wei, G. W. On the ﬁctitious-domain and interpolation formulations of the
matched interface and boundary (MIB) method. J. Comput. Phys. 2006, 219, 228–246.
(27) Zhou, Y. C.; Zhao, S.; Feig, M.; Wei, G. W. High order matched interface and boundary
method for elliptic equations with discontinuous coefﬁcients and singular sources. J. Comput.
Phys. 2006, 213, 1–30.
(28) Yu, S. N.; Geng, W. H.; Wei, G. W. Treatment of geometric singularities in implicit solvent
models. Journal of Chemical Physics 2007, 126, 244108.
(29) Yu, S. N.; Zhou, Y. C.; Wei, G. W. Matched interface and boundary (MIB) method for elliptic
problems with sharp-edged interfaces. J. Comput. Phys. 2007, 224, 729–756.
(30) Yu, S. N.; Wei, G. W. Three-dimensional matched interface and boundary (MIB) method for
treating geometric singularities. J. Comput. Phys. 2007, 227, 602–632.
(31) Xia, K. L.; Zhan, M.; Wei, G. W. MIB Galerkin method for elliptic interface problems. Jour-
nal of Computational and Applied Mathematics 2014, 272, 195– 220.
(32) Geng, W.; Yu, S.; Wei, G. W. Treatment of charge singularities in implicit solvent models.
Journal of Chemical Physics 2007, 127, 114106.
(33) Decherchi, S.; Rocchia, W. A general and robust ray-casting-based algorithm for triangulating
surfaces at the nanoscale. PLoS ONE 2013, 8, e59744.
(34) Liu, B.; Wang, B.; Zhao, R.; Tong, Y.; Wei, G. W. ESES: software for Eulerian solvent
excluded surface. Preprint 2015,
(35) Harris, R. C.; Bredenberg, J. H.; Silalahi, A. R. J.; Boschitsch, A. H.; Fenley, M. O. Under-
standing the physical basis of the salt dependence of the electrostatic binding free energy of
mutated charged ligand-nucleic acid complexes. Biophysical Chemistry 2011, 156, 79–87.
21


## Page 22


(36) Pettersen, E. F.; Goddard, T. D.; Huang, C. C.; Couch, G. S.; Greenblatt, D. M.; Meng, E. C.;
Ferrin, T. E. UCSF Chimera–a visualization system for exploratory research and analysis. J.
Comput. Chem. 2004, 25, 1605–1612.
(37) Feig, M.; Onufriev, A.; Lee, M. S.; Im, W.; Case, D. A.; Brooks, I., C. L. Performance com-
parison of generalized Born and Poisson methods in the calculation of electrostatic solvation
energies for protein structures. Journal of Computational Chemistry 2004, 25, 265–284.
(38) Reyes, C. M.; Kollman, P. A. Structure and thermodynamics of RNA-protein binding: using
molecular dynamics and free energy analyses to calculate the free energies of binding and
conformational change. Journal of molecular biology 2000, 297, 1145–1158.
(39) Nicholls, A.; Mobley, D. L.; Guthrie, J. P.; Chodera, J. D.; Bayly, C. I.; Cooper, M. D.;
Pande, V. S. Predicting small-molecule solvation free energies: an informal blind test for
computational chemistry. Journal of Medicinal Chemistry 2008, 51, 769–779.
(40) Shivakumar, D.; Williams, J.; Wu, Y.; Damm, W.; Shelley, J.; Sherman, W. Prediction of
absolute solvation free energies using molecular dynamics free energy perturbation and the
OPLS force ﬁeld. Journal of Chemical Theory and Computation 2010, 6, 1509–1519.
22


## Page 23


23

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]