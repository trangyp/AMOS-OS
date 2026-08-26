---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1210.6133
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1210.6133_Extracting_the_impact_parameter_dependence_of_the_nPDFs_from_the_EKS98_and_EPS09

> Source: 1210.6133_Extracting_the_impact_parameter_dependence_of_the_nPDFs_from_the_EKS98_and_EPS09.pdf

> Pages: 4

---


## Page 1


Extracting the impact parameter dependence of the
nPDFs from the EKS98 and EPS09 global ﬁts
I Helenius1,2, K J Eskola1,2, H Honkanen1,3 and C A Salgado4,5
1Department of Physics, P.O. Box 35, FI-40014 University of Jyv¨askyl¨a, Finland
2Helsinki Institute of Physics, P.O. Box 64, FIN-00014 University of Helsinki, Finland
3The Pennsylvania State University, 104 Davey Lab, University Park, PA 16802, USA
4Departamento de F´ısica de Part´ıculas and IGFAE, Universidade de Santiago de Compostela,
Galicia-Spain
5Physics Department, Theory Unit, CERN, CH-1211 Gen`eve 23, Switzerland
E-mail: ilkka.helenius@jyu.fi
Abstract.
As all the globally ﬁtted nuclear PDFs (nPDFs) have been so far impact parameter
independent, it has not been possible to calculate the hard process cross sections in diﬀerent
centrality classes consistently with the global analyses.
In [1] we have oﬀered a solution to
this problem by determining two spatially dependent nPDF sets, EPS09s and EKS98s, using
the A-systematics of the earlier global ﬁts EPS09 and EKS98 and an assumption that the
spatial dependence can be written as a power series of the nuclear thickness function. For a
data comparison, we have calculated the nuclear modiﬁcation factor of inclusive neutral pion
production in d+Au collisions at RHIC in four centrality bins at midrapidity and compared
these to a PHENIX measurement. In addition, we have also performed a similar calculation for
inclusive photon production in d+Au collisions at RHIC.
1. Introduction
In the collinear factorization framework [2, 3] the cross section for inclusive k production in a
hard process of a heavy ion collision between nuclei A and B can be computed as
dσAB→k+X =
X
i,j,X′
fA
i (x, Q2) ⊗fB
j (x, Q2) ⊗dˆσij→k+X′ + O(1/Q2),
(1)
where fA
i
(fB
j ) is the process-independent nuclear parton distribution function (nPDF) for a
parton ﬂavor i (j) in the nucleus A (B) and dˆσij→k+X′ represents the partonic pieces which
can be computed using perturbative QCD (pQCD). Similarly as the free proton PDFs, also
the nPDFs can be determined via a global analysis considering as many diﬀerent processes as
possible. Usually the nPDFs are determined in terms of the free proton PDFs, fN
i , (x, Q2) and
the nuclear modiﬁcation of the PDFs, RA
i (x, Q2), as
fA
i (x, Q2) = RA
i (x, Q2) fN
i (x, Q2).
(2)
So far all the globally analyzed nPDFs have been spatially independent. However, it is reasonable
to assume that as the nucleus itself is not spatially uniform, also the nuclear modiﬁcations of
the PDFs should somehow depend on the position of the nucleon inside the nucleus. In Ref. [1]
we have addressed this issue by considering the A-systematics of two globally ﬁtted nPDF sets,
EPS09 [4] and EKS98 [5] using the framework discussed in the next section.
arXiv:1210.6133v1  [hep-ph]  23 Oct 2012


## Page 2


2. Framework
First we introduce a nuclear modiﬁcation of the PDFs, rA
i (x, Q2, s), which now depends also on
the transverse position s of the nucleon inside the nucleus. For this we require that the spatial
average of the quantity gives back the spatially independent modiﬁcation,
RA
i (x, Q2) = 1
A
Z
d2s TA(s) rA
i (x, Q2, s),
(3)
for which we take the values from earlier global ﬁts (EKS98 or EPS09). This, however, does
not restrict the form of the spatial dependence in any way, so we have to make an assumption
for that. Motivated by the shadowing region at small x, we assume that the rA
i (x, Q2, s) can be
written as a power series of the nuclear thickness function TA(s):
rA
i (x, Q2, s) = 1 +
n
X
j=1
ci
j(x, Q2) [TA(s)]j ,
(4)
where now the ﬁt parameters ci
j(x, Q2) for each parton ﬂavor depend only on x and the scale
Q2 but not on A. This is important for correct mapping of the spatial dependence with the
A-dependence of the globally ﬁtted RA
i . In practice we obtain the values for our ﬁt parameters
ci
j(x, Q2) by minimizing the χ2 deﬁned as
χ2
i (x, Q2) =
X
A
"
RA
i (x, Q2) −1
A
R d2s TA(s)rA
i (x, Q2, s)
W A
i (x, Q2)
#2
(5)
in a (x, Q2) grid for all the parton ﬂavors. The weight factor W A
i (x, Q2) is set to 1 (1−RA
i (x, Q2))
for the EPS09 (EKS98) analysis. For the EPS09 analysis we perform this ﬁtting also for the 30
error sets both in leading (LO) and next-to-leading order (NLO). As can be seen from ﬁgure 1,
the A-systematics of RA
i is very well reproduced with the power series ansatz when we consider
A ≥16. In our analysis we found out that the ﬁrst four non-trivial terms of the power series in
equation 4 are enough for an accurate ﬁtting in the whole x and Q2 region, for all the diﬀerent
sets considered.
After the values for the ﬁt parameters ci
j(x, Q2) are obtained through this ﬁtting procedure,
we can calculate the rA
i (x, Q2, s) and determine the new spatially dependent nuclear modiﬁcation
sets, EPS09s and EKS98s, in which ”s” stands for ”spatial”. These are now published in our
website1. To illustrate the spatial dependence of the new nPDFs, the gluon modiﬁcation from
EPS09sNLO for lead nucleus is plotted in ﬁgure 2 as a function of x and the transverse distance
s = |s|. The general feature is that the nuclear eﬀects are larger in the dense center (small s) of
the nucleus and smaller at the sparse edge (large s).
3. Applications
The nuclear eﬀects of an observable can be quantiﬁed using the nuclear modiﬁcation factor
RAA. The improvement here is that now with the new nPDF sets one can compute the RAA
also for diﬀerent centrality classes in a manner which is consistent with the globally ﬁtted nuclear
modiﬁcations of the PDFs. Detailed instructions of the implementation of these new nPDFs
can be found in Ref. [1].
In ﬁgure 3 we have plotted the nuclear modiﬁcation factor Rπ0
dAu for inclusive π0 production
in d+Au collisions at √sNN = 200 GeV and y = 0 as a function of pT in four centrality classes.
The calculations are done in NLO (with the INCNLO-package2) using the CTEQ6M PDFs [6]
1 https://www.jyu.fi/fysiikka/en/research/highenergy/urhic/nPDFs
2 http://lapth.in2p3.fr/PHOX_FAMILY/readme_inc.html


## Page 3


0.4
0.5
0.6
0.7
0.8
0.9
1.0
0
50
100
150
200
250
300
EPS09LO
EPS09sLO
EPS09NLO
EPS09sNLO
RA
g (x, Q2)
A
x = 0.001
Q2 = 1.69 GeV2
Figure 1. The A-dependence of RA
g (x, Q2) at
ﬁxed x and Q2 values from the central sets of
EPS09NLO (crosses) and LO (pluses) and from
EPS09sNLO (green) and LO (blue). From [1].
0
0.166
0.332
0.498
0.664
0.83
0.996
0
2
4
6
8
10
0.2
0.4
0.6
0.8
1
1.2
1.4
10-6
10-5
10
-4
10
-3
10
-2
10
-1
1
x
s[fm]
rPb
g (x, Q2 = 1.69 GeV2, s)
Figure 2.
The gluon modiﬁcation in a lead
nucleus rPb
g (x, Q2, s) from EPS09sNLO as a
function of x and s at the EPS09 initial scale.
From [1].
with the EPS09s modiﬁcations [1] and three diﬀerent fragmentation functions (FFs), KKP [7],
AKK [8], and fDSS [9]. The uncertainty bands are calculated from the error sets of EPS09s with
the fDSS FFs. The centrality classes are deﬁned in terms of impact parameter intervals, which
are calculated using the optical Glauber model. The PHENIX datapoints [10] have been scaled
by overall factors which all are consistent with the overall normalization uncertainties given by
the experiment. The corresponding results for the forthcoming p+Pb collisions at the LHC can
be found in [1].
0.7
0.8
0.9
1.0
1.1
1.2
1.3
1.4
1.5
2
4
6
8
10
12
14
16
PHENIX
0
EPS09s KKP NLO
EPS09s AKK NLO
1.098*PHENIX
0-20%
GeV
0.7
0.8
0.9
1.0
1.1
1.2
1.3
1.4
1.5
2
4
6
8
10
12
14
16
EPS09s fDSS NLO
EPS09s errors fDSS
1.032*PHENIX
20-40%
0.7
0.8
0.9
1.0
1.1
1.2
1.3
1.4
0.7
0.8
0.9
1.0
1.1
1.2
1.3
1.4
2
4
6
8
10
12
14
16
[GeV/c]
2
4
6
8
10
12
14
16
1.009*PHENIX
40-60%
0.7
0.8
0.9
1.0
1.1
1.2
1.3
1.4
2
4
6
8
10
12
14
16
[GeV/c]
2
4
6
8
10
12
14
16
0.968*PHENIX
60-88%
Rπ0
dAu(pT )
√s = 200
y = 0
Rπ0
dAu(pT )
pT
pT
Figure 3. The nuclear modiﬁcation factor for inclusive π0 production in d+Au collisions at
RHIC in four centrality classes at midrapidity, calculated with the EPS09s nPDFs and diﬀerent
FFs. The data are from PHENIX [10]. From [1].


## Page 4


We have also performed similar calculations for inclusive photon production, Rγ
dAu, in
d+Au collisions at RHIC, which are shown in ﬁgure 4.
The results for the minimum bias
nuclear modiﬁcation factor for this process, calculated with diﬀerent nPDFs, can be found in
Ref. [11]. The inclusive photons consists of two components: direct and fragmentation. For the
fragmentation component we have used the BFG (set II) FFs [12], otherwise the setup is the
same as for the π0’s above. To quantify the isospin eﬀect, we have also plotted the Rγ
dAu using
the free nucleon PDFs in each panel. Similarly as for pions, also for the photons we can see that
the nuclear modiﬁcations are larger for central collisions than for peripheral collisions.
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
1.2
0
5
10
15
20
25
30
35
40
45
50
proton PDFs
0-20%
GeV
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
1.2
5
10
15
20
25
30
35
40
45
50
EPS09s BFG NLO
EPS09s errors BFG
20-40%
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
0
5
10
15
20
25
30
35
40
45
50
[GeV/c]
0
5
10
15
20
25
30
35
40
45
50
40-60%
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
5
10
15
20
25
30
35
40
45
50
[GeV/c]
5
10
15
20
25
30
35
40
45
50
60-88%
Rγ
dAu(pT )
√s = 200
y = 0
Rγ
dAu(pT )
pT
pT
Figure 4. The nuclear modiﬁcation factor for inclusive γ production in d+Au collisions at
RHIC in four centrality classes at midrapidity, computed with nPDFs (EPS09s) and proton
PDFs (CTEQ6M). From [13].
Acknowledgments
I.H. and K.J.E. thank the Magnus Ehrnrooth Foundation and Academy of Finland (Project 133005) for
ﬁnancial support. C.A.S. is supported by the European Research Council grant HotLHC ERC- 2001-
StG-279579, by Ministerio de Ciencia e Innovaci´on of Spain, and by Xunta de Galicia. H.H. is supported
by the U.S. Department of Energy under Grant DE- FG02-93ER40771.
References
[1] Helenius I, Eskola K J, Honkanen H and Salgado C A 2012 JHEP 1207 073 (Preprint 1205.5359)
[2] Collins J C, Soper D E and Sterman G F 1988 Adv.Ser.Direct.High Energy Phys. 5 1–91 (Preprint
hep-ph/0409313)
[3] Brock R et al. (CTEQ Collaboration) 1995 Rev.Mod.Phys. 67 157–248
[4] Eskola K J, Paukkunen H and Salgado C A 2009 JHEP 04 065 (Preprint 0902.4154)
[5] Eskola K J, Kolhinen V J and Salgado C A 1999 Eur.Phys.J. C9 61–68 (Preprint hep-ph/9807297)
[6] Pumplin J, Stump D R, Huston J, Lai H L, Nadolsky P M et al. 2002 JHEP 0207 012 (Preprint
hep-ph/0201195)
[7] Kniehl B A, Kramer G and Potter B 2000 Nucl.Phys. B582 514–536 (Preprint hep-ph/0010289)
[8] Albino S, Kniehl B A and Kramer G 2008 Nucl.Phys. B803 42–104 (Preprint 0803.2768)
[9] de Florian D, Sassot R and Stratmann M 2007 Phys.Rev. D75 114010 (Preprint hep-ph/0703242)
[10] Adler S S et al. (PHENIX Collaboration) 2007 Phys.Rev.Lett. 98 172302 (Preprint nucl-ex/0610036)
[11] Arleo F, Eskola K J, Paukkunen H and Salgado C A 2011 JHEP 1104 055 (Preprint 1103.1471)
[12] Bourhis L, Fontannaz M and Guillet J 1998 Eur.Phys.J. C2 529–537 (Preprint hep-ph/9704447)
[13] Helenius I and Eskola K J Work in progress

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1210_6133_extracting_the_impact_parameter_dependence_of_the_npdfs_from_the_eks98_and_eps09
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2012/1210_6133_EXTRACTING_THE_IMPACT_PARAMETER_DEPENDENCE_OF_THE_NPDFS_FROM_THE_EKS98_AND_EPS09.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
