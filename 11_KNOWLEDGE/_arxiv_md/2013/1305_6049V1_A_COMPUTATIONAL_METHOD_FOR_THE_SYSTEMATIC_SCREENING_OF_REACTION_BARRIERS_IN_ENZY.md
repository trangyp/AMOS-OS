---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1305.6049v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1305.6049v1_A_computational_method_for_the_systematic_screening_of_reaction_barriers_in_enzy

> Source: 1305.6049v1_A_computational_method_for_the_systematic_screening_of_reaction_barriers_in_enzy.pdf

> Pages: 60

---


## Page 1


1
A computational method for the systematic screening of
reaction barriers in enzymes: Searching for Bacillus circulans
xylanase mutants with greater activity towards a synthetic
substrate.
Martin R. Hediger1, Casper Steinmann2, Luca De Vico1, Jan H. Jensen1∗
1 Department of Chemistry, University of Copenhagen, Universitetsparken 5, DK-2100
Copenhagen, Denmark
2 Department of Physics, Chemistry and Pharmacy, University of Southern Denmark,
Odense, Denmark
∗Corresponding Author, Email: jhjensen@chem.ku.dk
Abstract
We present a semi-empirical (PM6-based) computational method for systematically estimating the eﬀect
of all possible single mutants, within a certain radius of the active site, on the barrier height of an
enzymatic reaction. The intent of this method is not a quantitative prediction of the barrier heights,
but rather to identify promising mutants for further computational or experimental study. The method
is applied to identify promising single and double mutants of Bacillus circulans xylanase (BCX) with
increased hydrolytic activity for the artiﬁcial substrate ortho-nitrophenyl β-xylobioside (ONPX2). The
estimated reaction barrier for wild-type (WT) BCX is 18.5 kcal/mol, which is in good agreement with
the experimental activation free energy value of 17.0 kcal/mol extracted from the observed kcat using
transition state theory (Joshi et al., Biochemistry 2001, 40, 10115). The PM6 reaction proﬁles for eight
single point mutations are recomputed using FMO-MP2/PCM/6-31G(d) single points. PM6 predicts
an increase in barrier height for all eight mutants while FMO predicts an increase for six of the eight
mutants. Both methods predict that the largest change in barrier occurs for N35F, where PM6 and FMO
predict a 9.0 and 15.8 kcal/mol increase, respectively. We thus conclude that PM6 is suﬃciently accurate
to identify promising mutants for further study. We prepared a set of all theoretically possible (342)
single mutants in which every amino acid of the active site (except for the catalytically active residues
E78 and E172) was mutated to every other amino acid. Based on results from the single mutants we
construct a set of 111 double mutants consisting of all possible pairs of single mutants with the lowest
barrier for a particular position and compute their reaction proﬁle. None of the mutants have, to our
knowledge, been prepared experimentally and therefore present experimentally testable predictions.
Introduction
Rational design of enzyme activity tends to be heuristic in that to varying degrees it is based on inspiration
derived from manual inspection of related protein structures [1–4]. One notable exception is the work by
Baker and co-workers [5–7] in which the desired transition state (TS) is found computationally for a small
idealized protein model using quantum mechanical (QM) methods followed by automated optimization
of protein scaﬀold to optimize the aﬃnity to the TS structure and catalytic side chain conformations.
While state-of-the-art, this work has not yet lead to the design of enzymes that are signiﬁcantly better
than those obtained by conventional means and additional computational approaches may be needed.
arXiv:1305.6049v1  [physics.chem-ph]  26 May 2013


## Page 2


2
We have recently published a computational methodology for directly estimating the eﬀect of mutations
on barrier heights [8] and shown that the method is suﬃciently fast to screen hundreds of mutants in a
reasonable amount of time while also being suﬃciently accurate to identify promising mutants [9]. As
with the methodology developed by Baker and co-workers, the intent of this method is not a quantitative
prediction of the barrier heights, but rather to identify promising mutants for further computational
or experimental study.
Since the method is designed to quickly screen hundreds of mutants several
approximations are made: the PM6 semiempirical QM method is used, a relatively small model of
the protein is used, and the eﬀect of solvent and structural dynamics is neglected. Furthermore, like
most computational studies of enzymatic catalysis, the focus is on estimating kcat rather than kcat/KM.
Nevertheless, in an initial application the method was found suﬃciently accurate to identify mutations
of Candida antarctica lipase B with increased amidase activity [9].
This paper presents several improvements to the method: (1) A systematic screening of single mutants
by automatic generation of all possible single mutations at sites within a certain radius of the active
site. (2) Use of the entire protein structure, rather than parts of it. (3) Inclusion of bulk solvent eﬀects
through a continuum model.
The method is applied to identify promising single and double mutants of Bacillus circulans xylanase
(BCX) with increased hydrolytic activity for the artiﬁcial substrate ortho-nitrophenyl β-xylobioside
(ONPX2). This system was chosen for several reasons: (1) To test the applicability of PM6 to model
this general type of chemical reaction. (2) Hydrolysis of ONPX2 by BCX is well-studied [10,11]. Since
the focus of this paper is solely the development of computational methodologies, the predicted mutants
are therefore presumably amenable to experimental testing by experimental groups.
Methods
Computational Details
Most geometry optimizations are performed using PM6 and the molecular orbital localization scheme
mozyme as implemented in mopac2012 [12–14]. From earlier work [8], it was found that the orthogonality
between the localized molecular orbitals is lost during the geometry optimization and it was suggested
to report results only from re-orthogonalized mozyme single point energy calculations (SPEs). In the
current work, however, we ﬁnd that when doing the SPE calculations, the mozyme routine frequently fails
to generate the same Lewis structure (required for the construction of the localized molecular orbitals)
as it did in the start of the geometry optimizations and so the energy from re-orthogonalization is not
comparable with the energy of the optimized structure.
The implications of this aspect are further
discussed below. The reported diﬃculty arises mainly for structures resembling the transition state, not
for stationary points. Thus the convergence of stationary point relative energies, depending on NDDO
cutoﬀand gradient convergence criterion (gnorm), is evaluated based on re-orthogonalization of the
mozyme wavefunction and a NDDO cutoﬀof 15˚A. Furthermore, the eﬀect of a solvent with dielectric
constant ϵr = 78 is described by the cosmo model [15].
Energetic reﬁnement of the mozyme structures is carried out using the two-body Fragment Molecular
Orbital method (FMO2) [16,17] with second order Møller-Plesset perturbation theory for correlation ef-
fects [18], and using the polarizable continuum model (PCM) [19,20] for solvation. All FMO2 calculations
are performed using GAMESS [21]. Inputs for the FMO2 calculations are prepared using FragIt [22].
In all FMO2 calculations, the reaction fragment consists of ONP, the ﬁrst xylose unit and Glu78 in order
to keep the reacting species and leaving group in one fragment. This fragment has 45 atoms. In all FMO2
SPEs we use the 6-31G(d) basis set [23, 24]. Pairs of fragments which are separated by more than two


## Page 3


3
van der Waals radii are calculated using a Coulomb expression for the interaction energy and correlation
eﬀects ignored (resdim=2.0 rcorsd=2.0 in $fmo). Optimizations using FMO are carried out with
the Frozen Domain and Dimers (FDD) approach [25] where only residues within 3 ˚A within the reaction
fragment are allowed to relax.
Estimating the Barrier Height for the WT
In this study we only model the ﬁrst, rate-determining [10, 11], step of the mechanism, which is the
formation of a glycosyl-enzyme complex (GE) from the enzyme substrate complex (ES) as illustrated
in Fig.
1.
The substrate is xylobioside-ortho-nitrophenol (ONPX2).
The energy barrier is obtained
O
O¡
O
Glu78
HO
O
Glu172
OR'
HO
HO
RO
O
O
Glu78
O
Glu172
OR'
H
OH
Glycosylation
x1
O
O
Glu78
O
Glu172
OR'
H
O
O
RO
HO
HO
b+
b<
O
RO
HO
HO
1
Figure 1. Conventional glycosylation step. x1: constrained reaction coordinate; R: xylose; R′:
ortho-nitrophenol (ONP). For discussion of proton transfer from E172 to substrate, see text. C1
indicating nucleophilic carbon of ﬁrst xylose unit.
from geometrical interpolation between the two stationary points of the rate-limiting glycosylation step
(enzyme-substrate complex, ES, and glycosyl-enzyme, GE). The various possible sequences of com-
putational steps to obtain the structure of these end points (for both wild-type and mutants) lead to
diﬀerent calculation pathways. In the following, we provide descriptions of the calculation pathways, the
implications of which are discussed in the results section.
In all calculations, the reaction coordinate is deﬁned by the distance between Oϵ and the carbon of the
ﬁrst xylose unit bonded to ONP, x1 in Fig. 1. The nucleophilic attack of E78 occurs on the bond between
ONP and the ﬁrst xylose unit. As described in our previous studies [8,9], the reaction barrier potential
energy is estimated from a linear interpolation procedure. Here the reaction coordinate is frozen to ten
intermediate values while the remaining active region is energy minimized to create a reaction proﬁle. In
the analysis, the barrier is deﬁned as the highest energy minus the lowest energy, which must be before
the highest energy point on the reaction proﬁle. If the last frame of the interpolation has the highest
energy, the barrier is not evaluated.
Upon insertion of the substrate in the active site by molecular modeling, the ONP unit is relaxed using
molecular mechanics in a ﬁxed enzyme environment. In extension of the initially proposed approach [8,9],
not only part of the enzyme but the full enzyme structure is used in the calculations. From this the
ambiguity of selecting an appropriate set of residues to model the active site is eliminated.
From careful analysis, we ﬁnd that the interpolation of the wild-type can be prepared by two slightly
diﬀerent procedures which are illustrated in Fig. 2. The modeling steps start (node “Start” in Fig. 2)
with the preparation of the glycosyl-enzyme complex since this structure is conformationally less mobile
due to the covalent link.


## Page 4


4
Figure 2. Calculation pathway for WT interpolations.
In the ﬁrst procedure, called “Interpolation 1”, the structure used as input for the optimization of the
GE (“WT GE” in Fig. 2), with ONP in the active site but not covalently bound to the ﬁrst xylose
unit, is prepared from the crystal structure with PDB ID 1BVV [26]. The ES complex, “WT ES”, is
formed by removing the covalent linkage between the substrate and E78 (step “Modify substrate (1)”).
The geometry of both structures is optimized (steps “Optimize”) without applying any constraints and
the resulting structures (referred to as “WT ES opt” and “WT GE opt”) are used for interpolation 1.
In the second procedure, “Interpolation 2”, WT GE optimized structure is used as a template for the ES
complex, referred to as “WT ES’ ” (the single prime indicating that the structure is derived from a wild-
type GE structure). The WT ES’ structure is again prepared by removing the covalent linkage between
the substrate and E78 (step“Modify substrate (2)”). To reduce the computational time required for the
geometry optimization, a set of Cartesian constraints K can be deﬁned (step “Deﬁne constraints K”) and
applied to spatially ﬁx an outer layer of residues away from the active site (step “Apply constraints K”).
These constraints are only applied to parts of the enzyme which are already optimized in a preceding
step. After optimization of WT ES’, the reaction barrier is mapped out by interpolation 2. Because
the structure of WT ES’ is optimized to a large degree, the time requirement is greatly reduced and the
results are found to be more reliable, see below.
Estimating Barrier Heights for the Mutants
Three diﬀerent interpolations procedures for mapping out the reaction barriers of mutants are deﬁned,
Fig. 3. In interpolation 3, the structures WT ES opt and WT GE opt are used in the preparation of
the corresponding mutant structures (“Mut ES opt” and “Mut GE opt”), which are used to prepare the
interpolation.


## Page 5


5
Figure 3. Calculation pathways for mutant interpolations. The diagram continues by the nodes “WT
ES opt” and “WT GE opt” from Fig. 2.


## Page 6


6
In interpolation 4, the structure of the ES complex of the mutants is based on the WT ES’ structure
and is referred to as “Mut ES’ opt”, the single prime again indicating that the structure is derived from
a WT GE structure).
In interpolation 5, the mutant ES structures are prepared from the Mut GE opt structure by replacing the
covalently bound substrate with the non-covalently bound substrate of WT ES’ (steps “Extract substrate”
and “Modify substrate (3)”). The mutant ES structures are referred to as Mut ES”, the double primes
indicate that the structure is derived from a mutant GE structure (as opposed to being derived from
a wild-type GE structure). We believe this way of preparing the structure of the ES
complex of the
mutants is most eﬃcient and readily implemented. Other options would be to prepare the ES complex
by docking procedures, which however would require considerable eﬀort if hundreds of mutants are to be
evaluated. As presented, the operation is a simple matter of command-line scripting.
The molecular structures of the mutant side chains are prepared using the PyMOL [27] mutagenesis
wizard in combination with local optimization of the mutated side chain using the PyMOL sculpting
function.
In interpolations 4 and 5, to reduce the time demand of the geometry optimizations, optionally the set of
constraints K can be applied. Constraints can not be meaningfully applied in interpolation 3 because the
interpolation between Mut ES and Mut GE produces (prior to being optimized) slightly diﬀerent input
coordinates which when ﬁxed result in enormous increases in energy.
Results and Discussion
Stationary Points in the WT Mechanism
MOPAC conﬁguration. The speed and accuracy of mozyme geometry optimizations are characterized
by the gradient convergence criterium (gnorm) and the cutoﬀdistance beyond which NDDO approxima-
tions are replaced by point charges (cutoff). Tab. 1 shows the energies of the optimized wild-type ES
and GE for diﬀerent conﬁgurations of mopac. The energies are relative to ES computed with gnorm
= 5.0 kcal/mol and cutoff = 9 ˚A. It is observed that the calculations converge for both ES and GE
Table 1. Relative energies [kcal/mol] for diﬀerent combinations of GNORM and CUTOFF. Energies
obtained as mozymeReortho//mozyme.
GNORM [kcal/(mol˚A)]
5.0
4.0
3.0
2.0
1.0
0.5
CUTOFF [˚A]
ES
9
0.0
-13.7
-14.1
-22.9
-19.4
-18.2
12
-5.5
-13.9
-14.0
-16.0
-26.1
-20.4
15
-34.0
-35.3
-35.2
-45.9
-48.9
-49.5
GE
9
-3.8
-7.3
-10.7
-14.2
-21.4
-19.7
12
-10.0
-10.9
-24.4
-24.4
-26.2
-24.5
15
-9.5
-25.4
-27.5
-27.6
-43.6
-40.6
when gnorm = 1.0kcal/(mol˚A) and the NDDO cutoﬀis 15˚A.


## Page 7


7
Tab. 2 shows the time requirements for the geometry optimization of ES and GE. As expected the
geometry optimization requires signiﬁcantly more time when using strict gradient convergence criteria.
However this appears to be required in order to obtain converged relative energies. In all of the following,
Table 2. Time requirements [h] for optimizations with diﬀerent combinations of GNORM and
CUTOFF.
GNORM [kcal/(mol˚A)]
5.0
4.0
3.0
2.0
1.0
0.5
CUTOFF [˚A]
ES
9
45.7
69.0
72.1
112.1
241.3
244.5
12
67.8
94.3
95.0
127.5
267.0
261.9
15
102.8
124.5
129.0
193.2
266.7
380.5
GE
9
53.3
57.3
76.5
111.7
147.7
156.2
12
69.4
64.2
104.3
117.3
176.5
174.6
15
92.7
110.2
144.1
198.2
411.4
424.3
unless otherwise stated, the NDDO cutoﬀis set to 15˚A and the gradient convergence is 1.0 kcal/(mol˚A).
Wild Type Mechanism and Reaction Barrier
As described in the methods section, the enzyme substrate complex for the wt is constructed in two
ways leading to two diﬀerent interpolation procedures “Interpolation 1” and “Interpolation 2” shown in
Fig. 2. Interpolation 1 yields an irregularly shaped reaction proﬁle (Fig. S1) from which it is impossible
to extract a reaction barrier. Unconstrained interpolation 2 yields a reasonably looking reaction proﬁle
(Fig. 4A) with a barrier of 18.5 kcal/mol, which is in good agreement with the experimental activation
free energy value of 17.0 kcal/mol extracted from the observed kcat [10] using transition state theory.
If the constraints K are not applied, the geometry optimization at each interpolation point along the
A
ï5
 0
 5
 10
 15
 20
 0
 2
 4
 6
 8
 10
Energy[kcal/mol]
Interpolation frame
UNCON. MOZ.
OPT 8Å,  MOZ.
OPT 10Å, MOZ.
OPT 12Å, MOZ.
B
 0
 50
 100
 150
 200
 250
 300
 350
 400
 450
 0
 2
 4
 6
 8
 10
Time[h]
Interpolation frame
WT, Interpolation 2,
GNORM=1.0[kcal/(molÅ)], CUTOFF=15[Å]
UNCON.
OPT 8Å
OPT 10Å
OPT 12Å
Figure 4. wt, Interpolation 2, ϵr = 78, Unconstrained and constrained optimizations. “UNCON.”: No
constraints applied in optimization, “MOZ.”: MOZYME.
A: Reaction barriers.
B: Time requirements.
reaction proﬁle requires between 100 and 300 CPU hours (Fig. 4B), a prohibitive cost if hundreds of


## Page 8


8
Figure 5. Hydrogen bonds between ONP leaving group and E172 proton in the optimized GE.
Distances in ˚A.
mutants are to be screened. The CPU time requirement can be reduced to less than 50 CPU hours by
only optimizing the geometry of residues close to the active site (Fig. 4B) and freezing the rest of the
coordinates to their values in the optimized GE complex. Optimizing only those residues within 8, 10
and 12 ˚A of the active site (OPT 8˚A, OPT 10˚A, OPT 12˚A in Fig. 4) reduces the predicted barrier to
10.0, 13.4 and 14.4 kcal/mol respectively (Fig. 4A). Much of this eﬀect will likely cancel when barriers
for mutants are compared to wt, but, based on these results it is advisable to recompute the barriers of
the most promising mutants without constraints. This is further discussed below.
Interestingly, for the GE intermediate the proton is found to reside on E172 rather than ONP as in the
canonical mechanism (Fig. 1) with hydrogen bonds to both the phenol oxygen and one of the oxygen
atoms on the nitro group (Fig. 5). A corresponding stationary point with a protonated ONP group
does not appear to exist. Geometry optimizations using FMO-MP2/6-31G(d):RHF show that there is a
stationary point both with protonated ONP and protonated E172 contrary to the ﬁndings by PM6 which
is in line with the canonical mechanism. It is therefore likely that the deprotonated ONP dissociates ﬁrst
followed by deprotonation of E172. Removal of the nitro-group leads to proton transfer to the phenol
group so this issue likely only applies to the ONPX2 substrate.
Interpolation Schemes for Mutants
Three interpolation schemes are tested for predicting reaction proﬁles of mutants as outlined in the
methods section and Fig. 3.
Interpolation 3. Interpolation 3 is most closely related to interpolation 1 for the wt and is tested for
six single point mutations where coordinates of all residues within 8 ˚A of the active site are optimized.
Like for the WT, this approach leads to irregularly shaped reaction proﬁles from which it is impossible
to extract reaction barriers (Fig. S2).


## Page 9


9
Interpolations 4 and 5. Interpolations 4 and 5 diﬀer on whether the mutant ES structure is constructed
from the WT ES structure (interpolation 4) or the mutated GE structure (interpolation 5).
Both
approaches are tested for eight single point mutations where the coordinates of all residues within 8 ˚A of
the substrate are optimized. The mutations are all within the active site and close proximity to the ONP
leaving group and E172. For the studied mutants, we ﬁnd that all reaction proﬁles appear conclusive in
shape and readily permit the estimation of a barrier height (Fig. 6).
A
ï10
0
10
20
MOZYME//MOZYME Barriers
Interpolation Frame
Relative Energy [kcal/mol]
W9F
N35F
V37F
Y69F
Y80F
A115F
P116F
I118F
Int 4
Int 5
Int 4
Int 5
 0
 10
 20
Int 4
Int 5
Int 4
Int 5
 0
 10
 20
Int 4
Int 5
Int 4
Int 5
 0
 10
 20
 1  2  3  4  5  6  7  8  9 10
Int 4
Int 5
 1  2  3  4  5  6  7  8  9 10
Int 4
Int 5
B
ï30
ï15
 0
 15
 30
FMOïMP2/PCM/6ï31G(d)//MOZYME Barriers
Interpolation Frame
Relative Energy [kcal/mol]
W9F
N35F
V37F
Y69F
Y80F
A115F
P116F
I118F
Int 4
Int 5
Int 4
Int 5
 0
 15
 30
Int 4
Int 5
Int 4
Int 5
ï10
 0
 10
 20
Int 4
Int 5
Int 4
Int 5
ï15
 0
 15
 30
 1  2  3  4  5  6  7  8  9 10
Int 4
Int 5
 1  2  3  4  5  6  7  8  9 10
Int 4
Int 5
Figure 6. Constrained interpolations 4/5, optimized layer: 8˚A.
A: Barriers from mozyme optimized structures.
B: FMO/PCM barriers based on SPE calculations of the mozyme optimized structures.
As shown in Fig. 7, the required time to calculate the barriers is mostly within the desired time frame
of two days when using interpolation procedure 5.
A
 0
 10
 20
 30
 40
 50
 60
 70
 80
 0
 2
 4
 6
 8
 10
Time[h]
Interpolation frame
Mutants, Interpolation 4,
GNORM=1.0[kcal/(molÅ)], CUTOFF=15[Å]
W9F
N35F
V37F
Y69F
Y80F
A115F
P116F
I118F
B
 0
 10
 20
 30
 40
 50
 60
 70
 80
 0
 2
 4
 6
 8
 10
Time[h]
Interpolation frame
Mutants, Interpolation 5,
GNORM=1.0[kcal/(molÅ)], CUTOFF=15[Å]
W9F
N35F
V37F
Y69F
Y80F
A115F
P116F
I118F
Figure 7. Time requirements, optimized layer of residues: 8˚A.
A: Interpolation procedure 4.
B: Interpolatin procedure 5.
The time requirements for interpolation 4 are found to be higher.


## Page 10


10
Furthermore, since two “Mutate”-modeling steps are involved in interpolation 4 (Fig. 3), local optimiza-
tion of the mutant side chain during the modeling process can result in diﬀerently oriented side chains
for the ES
complex
and GE intermediate of the mutant leading to non-physical structures in the
interpolation procedure. Interpolation 5 is in this sense more robust in that all mutated side chains, by
deﬁnition of the interpolation procedure, are identically oriented in both the ES and GE structures.
The PM6 reaction proﬁles shown in Figure 6A are recomputed using FMO-MP2/PCM/6-31G(d) single
points as shown in Figure 6B. We conﬁne our comparison to the interpolation 5 results as this is the
scheme we will use for the remaining mutants. The changes in barrier heights relative to WT computed
with PM6 compare well with the corresponding FMO values with an average error of 0.7 ± 5.3 kcal/mol.
The largest error (9.5 kcal/mol) occurs for I118F for which PM6 predicts a barrier height increase of 6.5
kcal/mol while FMO predicts a 3.0 kcal/mol decrease. More qualitatively, PM6 predicts an increase in
barrier height for all eight mutants while FMO predicts an increase for six of the eight mutants. Both
methods predict that the largest change in barrier occurs for N35F, where PM6 and FMO predict a 9.0
and 15.8 kcal/mol increase, respectively. We thus conclude that PM6 is suﬃciently accurate to identify
promising mutants for further study.
Computational High Throughput Screening of BCX Mutants
We prepared a set of all theoretically possible (342) single mutants in which every amino acid of the
active site (except for the catalytically active ones E78 and E172) was mutated to every other amino
acid. The active site is deﬁned as every residue that has at least one atom within 4 ˚A of the substrate.
However it was not possible to calculate the reaction barrier for every mutant because in some cases the
modeling procedure of the stationary points resulted in geometries for which MOPAC cannot generate a
Lewis structure or because MOPAC predicts a wrong total charge. In case MOPAC is unable to generate
a Lewis structure, it is not possible to start the calculation and so these mutants are identiﬁed when the
calculations are submitted. To check for correct computation of total charge, we use a computer script
which compares the value found by MOPAC, using the charges keyword, with the true value assuming
standard protonation of all ionizable residues. We have made no attempt to ﬁx these calculations but
simply discard them from the analysis.
Subsequent visual inspection of the mutants for which the
calculation did not start reveals that this was only the case when the newly introduced side chain is a
proline or a tyrosine and when the environment is very compact. To model the side chain conformations,
we use the PyMOL modeling and mutagenesis routines and also apply a local optimization of the mutated
side chain, keeping the environment ﬁxed. The PyMOL modeling routine only optimizes bond lengths,
angles and interatomic distances but does not consider electrostatic or electronic eﬀects. In the case of
proline we observe that the ring can be greatly distorted and in case of tyrosine the ring can be distorted
to a boat conformation when trying to place it in a sterically congested environment. An additional
reason for not being able to calculate the reaction barrier is that in some cases, one or more side chains
in the ES complex are oriented signiﬁcantly diﬀerent from the GE. In such cases, when the interpolation
frames are prepared, it can happen that two atoms are placed at very short distances to each other and
MOPAC will again not start the calculation for such a structure. Furthermore, we discarded a number
of double mutants if the optimization required more than ﬁve days. All discarded mutants are listed in
Tabs. S1 and S2 of the supporting material.
Finally, the reaction barrier was calculated for 317 single and 111 double mutants using an optimization
layer of 10 ˚A.
The calculated barriers are found to be mostly independent of reorthogonalization of the wavefunction
of the converged geometry, and the qualitative conclusions (lower/higher barrier compared to wild-type)


## Page 11


11
are the same in 80% of the cases with barriers lower than 34 kcal/mol, Fig. S3. Based on this observation
and on the above discussion, we therefore consider energies obtained without reorthogonalization.
The 20 single mutants with the lowest barriers are listed in Table 3. All barriers are lower than the WT
value, which is 13.4 kcal/mol for the 10 ˚A optimization. Based on results from the single mutants we
construct a set of double mutants consisting of all possible pairs of single mutants with the lowest barrier
for a particular position, using the same set of constraints K as for the single mutants. Just as for the
single mutants the PyMOL construction of some side chains resulted in unphysical structures which were
discarded from the analysis using the criteria discussed for the single mutants. Furthermore, in some
cases the optimization of some points on the reaction proﬁles of a double mutant failed to converge after
ﬁve days of CPU time and so the corresponding mutant was discarded as well. The average time for
optimization over all interpolation frames of double mutants is observed to be 29 hours. In total, the
barriers for 111 double mutants are calculated and the lowest twenty barriers for all single and double
mutants are listed in Tab. 3.
Reaction barriers[kcal/mol]
Single mutants
Double mutants
Q127W
6.9
Q7W-Q127W
4.6
S117P
8.5
W9E-Q127W
5.0
Q127K
8.6
Q127W-Y166V
5.0
A115I
8.7
W9E-Y65R
5.3
Q7W
8.7
Q7W-N35E
5.7
Q7R
8.8
N35E-Q127W
6.2
W9E
9.1
V37T-F125K
6.3
Q127H
9.5
W9E-F125K
6.4
N35E
9.6
Q7W-W129I
6.5
F125K
9.6
V37T-Q127W
6.7
Q127T
9.6
W9E-A115I
6.9
Q127I
9.6
Q127W-W129I
7.1
Q127V
9.9
P116C-Q127W
7.2
F125E
10.2
I118M-F125K
7.2
A115D
10.3
Q7W-Y65R
7.4
Q127L
10.3
F125K-Y174D
7.4
W9F
10.4
W9E-Y69E
7.5
Q127S
10.6
A115I-I118M
7.5
Q127F
10.6
I118M-Q127W
7.6
W9D
10.7
F125K-Q127W
7.8
Table 3. Twenty single and double mutants with lowest barriers.
An analysis of the distribution of single and double mutant barriers indicates that the eﬀects of single
mutations on the barriers are additive and contribute to a lowering of barriers on average, which is shown
in Fig. 8.
As discussed above, using the constraints on part of the enzyme decreases the computed barrier for the
WT by 5.1 kcal/mol (from 18.5 to 13.4 kcal/mol) if only residues within 10 ˚A of the active site are
optmized (Figure 4). The assumption is that the relative barriers will be less aﬀected, but ideally the
barriers of the most promising mutants listed in Tab. 3 should be recomputed without constraints.
Recomputing the reaction barriers of the best single and double mutants (Q127W and Q7W-Q127W)
without any applied constraints reveals that, as expected from the convergence study reported in Fig.
4A, the barriers increase (by 8.6 and 11.0 kcal/mol, respectively) but remain below the barrier obtained


## Page 12


12
Barrier [kcal/mol]
Mutant count
0
5
10
15
20
25
30
0
10
30
50
Single
Double
Figure 8. Barrier distribution of single and double mutants. Only datapoints below 30 kcal/mol
shown.
from the unconstrained WT optimization.
The constrained and unconstrained barriers are shown in
Fig. 9. This provides further evidence that these mutants indeed react faster than the wt and should be
A
B
ï15
ï10
ï5
 0
 5
 10
 15
 0
 2
 4
 6
 8
 10
Energy[kcal/mol]
Interpolation frame
Q127W
Q7WïQ127W
ï10
ï5
 0
 5
 10
 15
 0
 2
 4
 6
 8
 10
Energy[kcal/mol]
Interpolation frame
Q127W
Q7WïQ127W
Figure 9. Barriers of best single and double mutant.
A: Constrained optimization. Q127W: 6.9, Q7W-Q127W: 4.6 kcal/mol.
B: Unconstrained optimization. Q127W: 15.5, Q7W-Q127W: 15.6 kcal/mol. The starting geometries
for these optimizations are the structures optimized with constraints.
considered for further experimental evaluation. However, the computational cost is signiﬁcantly increased.
The average time to optimize all structures of the constrained interpolation is 28 (Q127W) and 37 (Q7W-
Q127W) hours while the average time to optimize all structures without any constraints is 110 (Q127W)
and 124 (Q7W-Q127W) hours per single processor (MOPAC2012 is not parallelized). So recomputing
the barriers of all 40 mutants listed in Table 3 would require a signiﬁcant investment of computer time.
Alternatively, one could use the constrained geometries as a starting point for conventional QM/MM
calculations with ab initio QM, at which point dynamical averaging could also be introduced. However,
given the time requirements associated with such an approach one might also consider going straight for
an experimental veriﬁcation for unequivocal answers. Either way, the key intent of the method is as an
additional tool for generating ideas for possible mutants that other, heuristic, approaches may miss.


## Page 13


13
While a complete discussion of all mutants listed in Tab. 3 is beyond the scope of this paper, we provide
a rationalization of a few exemplifying mutants in the following. These cases represent diﬀerent design
strategies such as enzyme-substrate complex destabilization or transition state stabilization.
As stated above, the single mutant with the lowest barrier is found to be Q127W. An inspection of the
structure shows that the Gln residue in the WT is likely stabilizing the negative charge on E78 in the
enzyme-substrate complex while removal of the hydrogen bond donor, Fig. 10A, and replacement by
Trp, which is of similar size (allowing to preserve structural integrity of the region), will likely increase
the energy of the enzyme-substrate complex and so lower the reaction barrier of the ﬁrst step. However,
with this mutation there is a danger that it will raise the barrier for the second step of the mechanism
where negative E78 is regenerated and so careful assessment of the full reaction cycle would be required
to fully characterize the eﬀects of the mutation on the total reaction.
A
B
Figure 10. Rationalization of reaction barriers.
A: Overlay of wt (black carbon spheres) and Q127W side-chain (green sticks) ES complex structures.
B: Coulombic interactions between (negative, red sticks) W9D/E, N35E and the nucleophilic carbon
(C1) on the substrate.
Distances in ˚A.
In terms of transition state stabilization, it is observed that the mutants W9D and W9E provide favourable
Coulombic interactions with the partial positive charge on the nucleophilic carbon of the ﬁrst xylose unit
(C1, Fig. 1) developing during the glycosylation, Fig. 10B. This interaction is likely to stabilize the
transition state, compared to WT, and so provides a lowering of the reaction barrier.
To the best of our knowledge, none of the mutations listed in Table 3 have been tested experimentally and
can thus be considered predictions. N35D has been shown experimentally to have a larger kcat than WT
using the ONPX2 substrate (14.5 vs. 9.6 s−1 for the wt [10]). The calculated barrier for N35D is 17.6
kcal/mol and considerably higher than the WT. However, Joshi et al. have presented evidence for D35
being protonated at the pH of interest, while our screening method only considers standard protonation
states for ionizable residues. Extending the automated screening method to non-standard protonation
states is considerably more complicated and a subject for future studies.


## Page 14


14
Conclusions
We present a computational method for systematically estimating the eﬀect of all possible single mutants,
within a certain radius of the active site, on the barrier height of an enzymatic reaction. The intent of this
method is not a quantitative prediction of the barrier heights, but rather to identify promising mutants
for further computational or experimental study.
Since the method is designed to quickly screen hundreds of mutants several approximations are made:
the PM6 semi-empirical quantum mechanical method is used, the transition state structure is estimated,
and the eﬀect of vibrational and structural dynamics is neglected. Furthermore, like most computational
studies of enzymatic catalysis, the focus is on estimating kcat rather than kcat/KM. Nevertheless, in an
initial application the method was found suﬃciently accurate to identify mutations of Candida antarctica
lipase B with increased amidase activity [9].
The method is applied to identify promising single and double mutants of Bacillus circulans xylanase
(BCX) with increased hydrolytic activity for the artiﬁcial substrate ortho-nitrophenyl β-xylobioside
(ONPX2). Since the focus of this paper is solely the development of computational methodologies, the
predicted mutants are therefore presumably amenable to experimental testing by experimental groups.
The estimated reaction barrier for wild-type (WT) BCX is 18.5 kcal/mol, which is in good agreement
with the experimental activation free energy value of 17.0 kcal/mol extracted from the observed kcat [10]
using transition state theory. The rate determining step is the formation of a glycosyl intermediate GE
starting with the enzyme-substrate complex ES. However, the geometry optimization at each interpola-
tion point along the reaction proﬁle requires between 100 and 300 CPU hours (Fig. 4B), a prohibitive
cost if hundreds of mutants are to be screened. The CPU time requirement can be reduced to less than
50 CPU hours by only optimizing the geometry of residues within 10 ˚A of the actives site the active site
(Fig. 4B) and freezing the rest of the coordinates to their values in the optimized GE complex. While
this decreases the reaction barrier (Fig. 4A) by up to 8.5 kcal/mol, we show for a few mutants that this
eﬀect partially cancels when applied to changes in barrier height so that promising mutants identiﬁed
with constraints remain promising after the constraints have been removed.
The PM6 reaction proﬁles for eight single point mutations are recomputed using FMO-MP2/PCM/6-
31G(d) single points as shown in Fig. 6B. PM6 predicts an increase in barrier height for all eight mutants
while FMO predicts an increase for six of the eight mutants. Both methods predict that the largest change
in barrier occurs for N35F, where PM6 and FMO predict a 9.0 and 15.8 kcal/mol increase, respectively.
We thus conclude that PM6 is suﬃciently accurate to identify promising mutants for further study.
We prepared a set of all theoretically possible (342) single mutants in which every amino acid of the
active site (except for the catalytically active residues E78 and E172) was mutated to every other amino
acid. The active site is deﬁned as every residue that has at least one atom within 4 ˚A of the substrate.
Twenty-ﬁve of these single mutations were discarded due to steric strain and similar reasons and the re-
action proﬁles where computed for the remaining 317 mutants. Based on results from the single mutants
we construct a set of 111 double mutants consisting of all possible pairs of single mutants with the lowest
barrier for a particular position and compute their reaction proﬁle. The twenty single and double mutants
with lowest barriers are listed in Table 3. The average time for optimization over all interpolation frames
of double mutants is observed to be 29 hours.
None of the mutants have, to our knowledge been prepared experimentally and therefore present experi-
mentally testable predictions. Alternatively, one could use the constrained geometries as a starting point
for conventional QM/MM calculations with ab initio QM, at which point dynamical averaging could
also be introduced. However, given the time requirements associated with such an approach one might
also consider going straight for an experimental veriﬁcation for unequivocal answers. Either way, the
key intent of the method is as an additional tool for generating ideas for possible mutants that other,
heuristic, approaches may miss.


## Page 15


15
Acknowledgments
Computational resources were provided by the Danish Center for Scientiﬁc Computing (DCSC). The
work was funded in part by the EU through the in silico rational engineering of novel enzymes (IRENE)
project.
Supporting material
Supporting material available: Figs. S1 – S3, Tabs. S1, S2. Graphs of all calculated barriers.


## Page 16


16
References
1. Patkar, S.;
Svendsen, A.;
Kirk, O.;
Clausen, I.;
Borch, K. Journal of Molecular Catalysis B:
Enzymatic 1997, 3, 51–54.
2. Nakagawa, Y.; Hasegawa, A.; Hiratake, J.; Sakata, K. Protein Engineering Design and Selection
2007, 20, 339–346.
3. Syr´en, P.; Hult, K. ChemCatChem 2011, 3, 853–860.
4. Syr´en, P.;
Hendil-Forssell, P.;
Aumailley, L.;
Besenmatter, W.;
Gounine, F.;
Svendsen, A.;
Martinelle, M.; Hult, K. ChemBioChem 2012, .
5. R¨othlisberger, D. et al. Nature 2008, 453, 190–195.
6. Jiang, L. et al. Science 2008, 319, 1387–1391.
7. Siegel, J. B.; Zanghellini, A.; Lovick, H. M.; Kiss, G.; Lambert, A. R.; St.Clair, J. L.; Galla-
her, J. L.; Hilvert, D.; Gelb, M. H.; Stoddard, B. L.; Houk, K. N.; Michael, F. E.; Baker, D.
Science 2010, 329, 309-313.
8. Hediger, M. R.; De Vico, L.; Svendsen, A.; Besenmatter, W.; Jensen, J. H. PLoS ONE 2012,
7, e49849.
9. Hediger, M. R.;
De Vico, L.;
Rannes, J. B.;
J¨ackel, C.;
Besenmatter, W.;
Svendsen, A.;
Jensen, J. H. ArXiv e-prints .
10. Joshi, M.; Sidhu, G.; Pot, I.; Brayer, G.; Withers, S.; McIntosh, L. Journal of molecular biology
2000, 299, 255–279.
11. Joshi, M.; Sidhu, G.; Nielsen, J.; Brayer, G.; Withers, S.; McIntosh, L. Biochemistry 2001, 40,
10115–10139.
12. Stewart, J. Journal of Computer-Aided Molecular Design 1990, 4, 1–103.
13. Stewart, J. International Journal of Quantum Chemistry 1996, 58, 133–146.
14. Stewart, J. Journal of Molecular Modeling 2007, 13, 1173–1213.
15. Klamt, A.; Sch¨u¨urmann, G. J. Chem. Soc., Perkin Trans. 2 1993, 799–805.
16. Nakano, T.; Kaminuma, T.; Sato, T.; Fukuzawa, K.; Akiyama, Y.; Uebayasi, M.; Kitaura, K.
Chemical Physics Letters 2002, 351, 475 - 480.
17. Fedorov, D. G.; Kitaura, K. The Journal of Physical Chemistry A 2007, 111, 6904-6914.
18. Fedorov, D. G.; Kitaura, K. The Journal of Chemical Physics 2004, 121, 2483–2490.
19. Tomasi, J.; Mennucci, B.; Cammi, R. Chemical Reviews 2005, 105, 2999-3094.
20. Fedorov, D. G.;
Kitaura, K.;
Li, H.;
Jensen, J. H.;
Gordon, M. S. Journal of Computational
Chemistry 2006, 27, 976–985.
21. Schmidt, M. et al. Journal of Computational Chemistry 1993, 14, 1347–1363.
22. Steinmann, C.; Ibsen, M. W.; Hansen, A. S.; Jensen, J. H. PLOS ONE 2012, 7, e44480.


## Page 17


17
23. Hariharan, P. C.; Pople, J. A. Theoretical Chemistry Accounts: Theory, Computation, and Mod-
eling (Theoretica Chimica Acta) 1973, 28, 213-222 10.1007/BF00533485.
24. Francl, M. M.;
Pietro, W. J.;
Hehre, W. J.;
Binkley, J. S.;
Gordon, M. S.;
DeFrees, D. J.;
Pople, J. A. The Journal of Chemical Physics 1982, 77, 3654-3665.
25. Fedorov, D. G.;
Alexeev, Y.;
Kitaura, K. The Journal of Physical Chemistry Letters 2011, 2,
282-288.
26. Sidhu, G.; Withers, S.; Nguyen, N.; McIntosh, L.; Ziser, L.; Brayer, G. Biochemistry 1999, 38,
5346–5354.
27. The PyMOL Molecular Graphics System, Schr¨odinger, LLC, 2010.


## Page 18


ESI-1
Electronic Supporting Information
A computational method for the systematic screening of reaction barriers in enzymes:
Searching for Bacillus circulans xylanase mutants with greater activity towards a synthetic
substrate.
Martin R. Hediger1, Casper Steinmann2, Luca De Vico1, Jan H. Jensen1∗
1 Department of Chemistry, University of Copenhagen, Universitetsparken 5, DK-2100
Copenhagen, Denmark
2 Department of Physics, Chemistry and Pharmacy, University of Southern Denmark,
Odense, Denmark
∗Corresponding Author, Email: jhjensen@chem.ku.dk


## Page 19


ESI-2
Figures
WT Interpolation 1 Reaction Barriers
A
ï10
ï5
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Energy[kcal/mol]
Interpolation frame
WT, Interpolation 1, GNORM=1.0[kcal/(molÅ)]
CUTOFF=9Å
CUTOFF=12Å
CUTOFF=15Å
B
ï20
ï15
ï10
ï5
 0
 5
 10
 15
 20
 0
 2
 4
 6
 8
 10
Energy[kcal/mol]
Interpolation frame
WT, Interpolation 1, GNORM=0.5[kcal/(molÅ)]
CUTOFF=9Å
CUTOFF=12Å
CUTOFF=15Å
Figure S1. wt, Interpolation 1, ϵr=78, cutoff referring to value used in geometry optimization. All
SPE calculations done using cutoff=15˚A.
A: gnorm=1.0kcal/(mol˚A).
B: gnorm=0.5kcal/(mol˚A).


## Page 20


ESI-3
Interpolation 3 Reaction Barriers
A
ï20
ï10
 0
 10
 20
 0
 2
 4
 6
 8
 10
Energy[kcal/mol]
Interpolation frame
Q7F
V37F
Y69F
W71F
Q127F
Y166F
B
 0
 50
 100
 150
 200
 250
 300
 0
 2
 4
 6
 8
 10
Time[h]
Interpolation frame
Figure S2. Interpolation 3 of mutants. In optimizations gnorm=0.5 kcal/(mol˚A), cutoff=12˚A. In
SPE calculations cutoff=15˚A.
A: Barriers.
B: Time requirements.


## Page 21


ESI-4
Qualitative Agreement Non-/Reorthogonalized Barriers
 0
 5
 10
 15
 20
 25
 30
 0
 5
 10
 15
 20
 25
 30
Reorthogonalized Barrier
[kcal/mol]
Nonïreorthogonalized Barrier
[kcal/mol]
(1)
(2)
(3)
(4)
WTNonïreortho=
13.9
WTreortho=
13.4
Figure S3. Dependence of reaction barriers of single mutants on reorthogonalization. Independent of
reorthogonalization, activity is qualitatively predicted the same for the datapoints within the
highlighted areas. The number of datapoints in each quadrant are 90(1), 14(2), 45(3) and 20(4),
quadrants indicated by “(i)” labels. Only datapoints lower than 34 kcal/mol shown.


## Page 22


ESI-5
Discarded mutants
Mutant
Reason for discarding
W9P
Local optimization of side chain gives unphysical structure
V37P
Y69P
Y80P
W71P
A115P
I118Y
Q7Y
Computed charge of GE structure not correct
V37H
Y80M
A115E
A115M
S117H
S117M
S117Q
S117R
S117W
Q127Y
Q7K
Computed charge of ES” wrong
A115C
Q127R
Q7E
Two atoms too close in automatically prepared structure
W9H
W71M
Y166R
Table S1. Discarded single mutants.


## Page 23


ESI-6
Mutant
Reason for discarding
Q7W-W9E
Geometry optimization time requirement too large
Q7W-P116C
Q7W-F125K
W9E-Y80D
W9E-R112D
W9E-W129I
W9E-Y174D
N35E-A115I
V37T-Y65R
V37T-Y69E
V37T-I118M
Y65R-R112D
Y65R-F125K
Y65R-Q127W
Y69E-Y80D
Y69E-Y174D
W71G-Y127W
W71G-R112D
W71G-S117P
W71G-W129I
W71G-Y166V
W71G-Y174D
W71G-Y80D
Y80D-Y116V
R112D-F125K
R112D-W129I
R112D-Y166V
A115I-P116C
P116C-I118M
S117P-F125K
S117P-Y174D
W129I-Y174D
N35E-R112D
Computed charge of ES” wrong
N35E-W129I
Y69E-S117P
W71G-P116C
S117P-Y166V
Q7W-W71G
Two atoms too close in automatically prepared structure
Q7W-Y69E
R112D-P116C
R112D-Q127W
R112D-S117P
Table S2. Discarded double mutants.


## Page 24


ESI-7
Single Mutant Barriers


## Page 25


ESI-8
Position 7
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Q7A
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7C
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Q7D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Q7G
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7H
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7I
 0
 20
 40
 60
 80
 100
 120
 0
 2
 4
 6
 8
 10
Q7L
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Q7M
-2
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
Q7N
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7P
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7R
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7V
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Q7W


## Page 26


ESI-9
Position 9
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W9A
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9C
-2
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
W9D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9G
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W9I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W9K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9L
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W9M
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9N
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9Q
 0
 100
 200
 300
 400
 500
 600
 700
 0
 2
 4
 6
 8
 10
W9R
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W9S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W9V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9Y


## Page 27


ESI-10
Position 35
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
N35A
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
N35C
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
N35D
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
N35E
-15
-10
-5
 0
 5
 10
 0
 2
 4
 6
 8
 10
N35F
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
N35G
-10
-5
 0
 5
 10
 15
 0
 2
 4
 6
 8
 10
N35H
-10
-5
 0
 5
 10
 15
 20
 0
 2
 4
 6
 8
 10
N35I
-14
-12
-10
-8
-6
-4
-2
 0
 2
 4
 0
 2
 4
 6
 8
 10
N35K
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
N35L
-10
-5
 0
 5
 10
 15
 0
 2
 4
 6
 8
 10
N35M
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 0
 2
 4
 6
 8
 10
N35P
 0
 5
 10
 15
 20
 25
 30
 35
 40
 0
 2
 4
 6
 8
 10
N35Q
-14
-12
-10
-8
-6
-4
-2
 0
 2
 0
 2
 4
 6
 8
 10
N35R
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 0
 2
 4
 6
 8
 10
N35S
-12
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 0
 2
 4
 6
 8
 10
N35T
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 0
 2
 4
 6
 8
 10
N35V
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
N35W
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
N35Y


## Page 28


ESI-11
Position 37
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
V37A
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
V37C
-500000
 0
 500000
 1e+06
 1.5e+06
 2e+06
 2.5e+06
 0
 2
 4
 6
 8  10
V37D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
V37E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
V37F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
V37G
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
V37I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
V37K
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
V37L
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
V37M
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
V37N
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
V37Q
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
V37R
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
V37S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
V37T
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
V37W
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
V37Y


## Page 29


ESI-12
Position 65
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y65A
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65C
-50
 0
 50
 100
 150
 200
 250
 0
 2
 4
 6
 8
 10
Y65D
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y65E
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y65F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65G
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65H
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y65I
-10
-5
 0
 5
 10
 15
 0
 2
 4
 6
 8
 10
Y65K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y65L
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y65M
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65N
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65P
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y65Q
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65R
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y65S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65W


## Page 30


ESI-13
Position 69
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y69A
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y69C
-10
-5
 0
 5
 10
 15
 0
 2
 4
 6
 8
 10
Y69D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y69E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y69F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y69G
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y69H
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y69I
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y69K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y69L
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y69M
 0
 10
 20
 30
 40
 50
 60
 70
 80
 90
 100
 0
 2
 4
 6
 8
 10
Y69N
 0
 10
 20
 30
 40
 50
 60
 70
 80
 90
 0
 2
 4
 6
 8
 10
Y69Q
-20
-15
-10
-5
 0
 5
 10
 15
 0
 2
 4
 6
 8
 10
Y69R
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y69S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y69T
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y69V
-10
-5
 0
 5
 10
 15
 0
 2
 4
 6
 8
 10
Y69W


## Page 31


ESI-14
Position 71
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W71A
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W71C
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W71D
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W71E
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W71F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W71G
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W71H
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W71I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W71K
-50
 0
 50
 100
 150
 200
 250
 300
 0
 2
 4
 6
 8
 10
W71L
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W71N
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W71Q
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W71R
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W71S
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W71T
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W71V
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W71Y


## Page 32


ESI-15
Position 80
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y80A
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y80C
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y80D
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y80E
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y80F
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y80G
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y80H
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y80I
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y80K
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y80L
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y80N
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y80Q
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y80R
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y80S
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y80T
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y80V
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y80W


## Page 33


ESI-16
Position 112
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112A
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112C
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
R112D
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
R112E
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112F
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
R112G
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
R112H
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112I
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
R112K
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
 0
 2
 4
 6
 8
 10
R112L
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112M
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112N
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112P
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112Q
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
R112T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
R112V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112W
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
R112Y


## Page 34


ESI-17
Position 115
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
A115D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
A115F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
A115G
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
A115H
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
A115I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
A115K
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
A115L
 0
 500000
 1e+06
 1.5e+06
 2e+06
 2.5e+06
 0
 2
 4
 6
 8  10
A115N
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
A115Q
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
A115R
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
A115S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
A115T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
A115V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
A115W
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
A115Y


## Page 35


ESI-18
Position 116
 0
 10
 20
 30
 40
 50
 60
 70
 80
 90
 0
 2
 4
 6
 8
 10
P116A
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
P116C
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
P116D
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
P116E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
P116F
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
P116G
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
P116H
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
P116I
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
P116K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
P116L
 0
 500000
 1e+06
 1.5e+06
 2e+06
 2.5e+06
 0
 2
 4
 6
 8  10
P116M
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
P116N
-50
 0
 50
 100
 150
 200
 250
 0
 2
 4
 6
 8
 10
P116Q
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
P116R
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
P116S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
P116T
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
P116V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
P116W
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
P116Y


## Page 36


ESI-19
Position 117
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
S117A
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
S117C
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
S117D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
S117E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
S117F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
S117G
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
S117I
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
S117K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
S117L
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
S117N
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
S117P
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
S117T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
S117V
-16
-14
-12
-10
-8
-6
-4
-2
 0
 0
 2
 4
 6
 8
 10
S117Y


## Page 37


ESI-20
Position 118
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
I118A
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
I118C
-50
 0
 50
 100
 150
 200
 250
 300
 0
 2
 4
 6
 8
 10
I118D
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
I118E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
I118F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
I118G
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
I118H
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 0
 2
 4
 6
 8
 10
I118K
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
I118L
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
I118M
-5
 0
 5
 10
 15
 20
 0
 2
 4
 6
 8
 10
I118N
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
I118P
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
I118Q
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
I118R
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
I118S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
I118T
 0
 5
 10
 15
 20
 25
 30
 35
 40
 0
 2
 4
 6
 8
 10
I118V
-500000
 0
 500000
 1e+06
 1.5e+06
 2e+06
 2.5e+06
 0
 2
 4
 6
 8  10
I118W


## Page 38


ESI-21
Position 125
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125A
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
F125C
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
F125D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125G
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
F125H
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125L
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125M
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
F125N
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125P
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125Q
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125R
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
F125V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
F125W
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
F125Y


## Page 39


ESI-22
Position 127
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q127A
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Q127C
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Q127D
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Q127E
-16
-14
-12
-10
-8
-6
-4
-2
 0
 2
 4
 0
 2
 4
 6
 8
 10
Q127F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q127G
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Q127H
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q127I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Q127K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q127L
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Q127M
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Q127N
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q127P
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q127S
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Q127T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q127V
-12
-10
-8
-6
-4
-2
 0
 2
 4
 6
 0
 2
 4
 6
 8
 10
Q127W


## Page 40


ESI-23
Position 129
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W129A
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W129C
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W129D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W129E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W129F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W129G
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W129H
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W129I
-4
-2
 0
 2
 4
 6
 8
 10
 0
 2
 4
 6
 8
 10
W129K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W129L
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W129M
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W129N
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W129P
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W129Q
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
W129R
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W129S
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W129T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W129V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
W129Y


## Page 41


ESI-24
Position 166
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y166A
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y166C
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y166D
-50
 0
 50
 100
 150
 200
 250
 0
 2
 4
 6
 8
 10
Y166E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y166F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y166G
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y166H
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y166I
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y166K
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y166L
-6
-4
-2
 0
 2
 4
 6
 8
 10
 0
 2
 4
 6
 8
 10
Y166M
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
Y166N
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y166P
-4
-2
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
Y166Q
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y166S
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y166T
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y166V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y166W


## Page 42


ESI-25
Position 174
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174A
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y174C
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174D
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y174E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174F
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174G
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174H
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y174L
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174M
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174N
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y174P
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174Q
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y174R
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174S
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y174V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y174W


## Page 43


ESI-26
Double Mutant Barriers


## Page 44


ESI-27
Position 7
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Q7W-A115I
-12
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 0
 2
 4
 6
 8
 10
Q7W-I118M
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7W-N35E
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
Q7W-Q127W
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Q7W-R112D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7W-S117P
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Q7W-V37T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Q7W-W129I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Q7W-Y166V
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Q7W-Y174D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Q7W-Y65R
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Q7W-Y80D


## Page 45


ESI-28
Position 9
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
W9E-A115I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W9E-F125K
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
W9E-I118M
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W9E-N35E
-500000
 0
 500000
 1e+06
 1.5e+06
 2e+06
 2.5e+06
 0
 2
 4
 6
 8  10
W9E-P116C
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 0
 2
 4
 6
 8
 10
W9E-Q127W
-10
-5
 0
 5
 10
 15
 0
 2
 4
 6
 8
 10
W9E-S117P
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9E-V37T
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
W9E-W71G
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W9E-Y166V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W9E-Y65R
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
W9E-Y69E


## Page 46


ESI-29
Position 35
-8
-6
-4
-2
 0
 2
 4
 6
 0
 2
 4
 6
 8
 10
N35E-F125K
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
N35E-I118M
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
N35E-P116C
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 0
 2
 4
 6
 8
 10
N35E-Q127W
-5
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
N35E-S117P
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
N35E-V37T
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
N35E-W71G
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
N35E-Y166V
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
N35E-Y174D
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
N35E-Y65R
 0
 5
 10
 15
 20
 25
 30
 0
 2
 4
 6
 8
 10
N35E-Y69E
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
N35E-Y80D


## Page 47


ESI-30
Position 37
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
 0
 2
 4
 6
 8
 10
V37T-A115I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
V37T-F125K
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
V37T-P116C
-12
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 0
 2
 4
 6
 8
 10
V37T-Q127W
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
V37T-R112D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
V37T-S117P
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
V37T-W129I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
V37T-W71G
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
V37T-Y166V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
V37T-Y174D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
V37T-Y80D


## Page 48


ESI-31
Position 65
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y65R-A115I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y65R-I118M
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Y65R-P116C
 0
 50
 100
 150
 200
 250
 0
 2
 4
 6
 8
 10
Y65R-S117P
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y65R-W129I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65R-W71G
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
Y65R-Y166V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y65R-Y174D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y65R-Y69E
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y65R-Y80D


## Page 49


ESI-32
Position 69
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Y69E-A115I
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Y69E-F125K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y69E-I118M
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Y69E-P116C
-10
-5
 0
 5
 10
 15
 20
 0
 2
 4
 6
 8
 10
Y69E-Q127W
-10
-5
 0
 5
 10
 15
 0
 2
 4
 6
 8
 10
Y69E-R112D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y69E-W129I
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
Y69E-W71G
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Y69E-Y166V


## Page 50


ESI-33
Position 71
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W71G-A115I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
W71G-F125K
-5
 0
 5
 10
 15
 20
 0
 2
 4
 6
 8
 10
W71G-I118M


## Page 51


ESI-34
Position 80
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
Y80D-A115I
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Y80D-F125K
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y80D-I118M
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Y80D-P116C
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 0
 2
 4
 6
 8
 10
Y80D-Q127W
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y80D-R112D
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
Y80D-S117P
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
Y80D-W129I
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
Y80D-Y174D


## Page 52


ESI-35
Position 112
 0
 500000
 1e+06
 1.5e+06
 2e+06
 2.5e+06
 0
 2
 4
 6
 8  10
R112D-A115I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
R112D-I118M
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
R112D-Y174D


## Page 53


ESI-36
Position 115
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
A115I-F125K
-5
-4
-3
-2
-1
 0
 1
 2
 3
 0
 2
 4
 6
 8
 10
A115I-I118M
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
A115I-Q127W
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
A115I-S117P
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 0
 2
 4
 6
 8
 10
A115I-W129I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
A115I-Y166V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
A115I-Y174D


## Page 54


ESI-37
Position 116
 0
 5
 10
 15
 20
 25
 0
 2
 4
 6
 8
 10
P116C-F125K
-10
-8
-6
-4
-2
 0
 2
 4
 6
 0
 2
 4
 6
 8
 10
P116C-Q127W
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
P116C-S117P
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
P116C-W129I
-4
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
P116C-Y166V
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
P116C-Y174D


## Page 55


ESI-38
Position 117
-2
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
S117P-I118M
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 0
 2
 4
 6
 8
 10
S117P-Q127W
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
S117P-W129I


## Page 56


ESI-39
Position 118
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
I118M-F125K
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 0
 2
 4
 6
 8
 10
I118M-Q127W
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
I118M-W129I
-2
 0
 2
 4
 6
 8
 10
 12
 14
 0
 2
 4
 6
 8
 10
I118M-Y166V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
I118M-Y174D


## Page 57


ESI-40
Position 125
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 0
 2
 4
 6
 8
 10
F125K-Q127W
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
F125K-W129I
 0
 2
 4
 6
 8
 10
 12
 14
 16
 18
 20
 0
 2
 4
 6
 8
 10
F125K-Y166V
 0
 2
 4
 6
 8
 10
 12
 14
 16
 0
 2
 4
 6
 8
 10
F125K-Y174D


## Page 58


ESI-41
Position 127
-10
-8
-6
-4
-2
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
Q127W-W129I
-8
-6
-4
-2
 0
 2
 4
 0
 2
 4
 6
 8
 10
Q127W-Y166V
-14
-12
-10
-8
-6
-4
-2
 0
 2
 4
 6
 0
 2
 4
 6
 8
 10
Q127W-Y174D


## Page 59


ESI-42
Position 129
-4
-2
 0
 2
 4
 6
 8
 10
 0
 2
 4
 6
 8
 10
W129I-Y166V


## Page 60


43
Position 166
-2
 0
 2
 4
 6
 8
 10
 12
 0
 2
 4
 6
 8
 10
Y166V-Y174D

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]