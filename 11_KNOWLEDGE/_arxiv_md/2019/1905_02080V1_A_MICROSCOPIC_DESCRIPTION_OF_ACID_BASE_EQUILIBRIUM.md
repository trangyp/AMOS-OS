---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.02080v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1905.02080v1_A_microscopic_description_of_acid-base_equilibrium

> Source: 1905.02080v1_A_microscopic_description_of_acid-base_equilibrium.pdf

> Pages: 18

---


## Page 1


A microscopic description of acid-base
equilibrium
Emanuele Grifoni,†,‡ GiovanniMaria Piccini,†,‡ and Michele Parrinello∗,†,‡,¶
†Department of Chemistry and Applied Biosciences, ETH Zurich, c/o USI Campus, Via
Giuseppe Buﬃ13, CH-6900 Lugano, Ticino, Switzerland
‡Institute of Computational Science, Universit della Svizzera italiana (USI), Via Giuseppe
Buﬃ13, CH-6900, Lugano, Ticino, Switzerland
¶Italian Institute of Technology, Via Morego 30, 16163 Genova, Italy
E-mail: parrinello@phys.chem.ethz.ch
Abstract
Acid-base reactions are ubiquitous in nature.
Understanding their mechanisms
is crucial in many ﬁelds, from biochemistry to industrial catalysis.
Unfortunately,
experiments only give limited information without much insight into the molecular
behaviour. Atomistic simulations could complement experiments and shed precious
light on microscopic mechanisms. The large free energy barriers connected to proton
dissociation however make the use of enhanced sampling methods mandatory. Here we
perform an ab initio molecular dynamics (MD) simulation and enhance sampling with
the help of methadynamics. This has been made possible by the introduction of novel
descriptors or collective variables (CVs) that are based on a conceptually new outlook
on acid-base equilibria. We test successfully our approach on three diﬀerent aqueous
solutions of acetic acid, ammonia, and bicarbonate. These are representative of acid,
basic, and amphoteric behaviour.
1
arXiv:1905.02080v1  [physics.chem-ph]  22 Jan 2019


## Page 2


Introduction
Acid-base reactions play a key role in many branches of chemistry. Inorganic complexation
reactions, protein folding, enzimatic processes, polymerization, catalytic reactions and many
other transformations in diﬀerent areas are sensitive to changes in pH. Understanding the
pH role in these reactions implies having control over their reactivity and kinetics.
The crucial importance of pH has stimulated the collection of a large amount of data
on acid-base equilibria. These are typically measured in gas and condensed phases using
spectroscopic and potentiometric techniques. However, there are practical limitations to the
accuracy of these methods especially in condensed phases.1 Furthermore it is very diﬃcult to
extract from experimental data a microscopic picture of the processes involved. It is thus not
surprising that acid-base equilibrium has been the subject of intense theoretical activity.1–12
The acidity of a chemical species in water can be expressed in terms of pKa, the negative
logarithm of the acid dissociation constant. There are two ways of calculating these values,
one static and the other dynamic.
The most standard approach is the static one in which solution-phase free energies,
and consequently pKas, are obtained closing a Born-Haber cycle composed by gas phase and
solvation free energies.1,3–7 While extremely successful in many cases, the static approach has
some limitations. A solvation model needs to be chosen and continuum solvent models have
a limited accuracy. This is particularly true in systems like zeolites or proteins characterized
by irregular cavities in which an implicit description of the solvent is challenging. Obviously
from such an approach dynamic information cannot be gained. Furthermore, there can be
competitive reactions that cannot be taken into account unless explicitly included in the
model.
In principle these limitations could be lifted in a more dynamical approach based on
MD simulations in which the solvent molecules are treated explicitly. If one had unlimited
computer time such simulation would explore all possible pathways and assign the relative
statistical weight to the diﬀerent states. Unfortunately the presence of kinetic bottlenecks
2


## Page 3


frustrates this possibility trapping the system in metastable states, since diﬀerent protonation
states are separated by large barriers. Furthermore in acid-base reactions chemical bonds
are broken and formed. This requires the use of ab initio MD in which the interatomic forces
are computed on the ﬂy from electronic structure theories. This makes the calculation more
expensive and reduces further the time scale that can be explored.
To overcome this diﬃculty, the use of enhanced sampling methods13 that accelerate
conﬁgurational space exploration becomes mandatory. A very popular class of enhanced
sampling methods is based on the identiﬁcation of the degrees of freedom that are involved
in the slow reaction of interest. These degrees of freedom are usually referred to as collec-
tive variables (CVs) and are expressed as explicit functions of the atomic coordinates R.
Sampling is then enhanced by adding a bias that is a function of the chosen CVs.14–16 Fur-
thermore, designing a proper set of good CVs has also a deeper meaning. Successful CVs
capture in a condensed way the physics of the problem, identify its slow degrees of freedom
and lead a useful modellistic description of the process.
In standard chemical reactions, this is relatively simple since well deﬁned structures can
be assigned to reactants and products.17–19 This is not the case for acid-base reactions in
which a proton is added to or subtracted from the solute. Once this process has taken place,
water ions (H+ or/and OH–) are solvated and their structure becomes elusive. In fact water
ions can rapidly diﬀuse in the medium via a Grotthuss mechanism.20 They became highly
ﬂuxional and the identity of the atoms taking part in their structure changes continuously.
The nature of these species is thus diﬃcult to capture in an explicit analytic funcion of
R. However, given the relevance of acid-base reactions, many attempts have been made
at deﬁning these entities.8–12 Unfortunately these CVs have an ad-hoc nature and, while
successful in this or that case, cannot be generally applied.
In order to build general and useful CVs we make two conceptual steps. One is to look at
the acid-base process as a reaction involving only a few moieties. Namely the whole solvent
and the reacting residues in the solvated molecule. For example when there is only one type
3


## Page 4


of dissociating residue we think of the acid-base equilibrium as a reaction of the type
A + H2NON −−⇀
↽−−Bq0 + H2N+q1ON
q1,
(1)
where N is the number of water molecules, A and B are a generic acid-base molecule in
solution and its conjugate species respectively, q0 and q1 are integers that can assume values
+1 and −1 according to the acid-base behaviour of the species and q1 + q0 = 0.
This implies that we do not look at the solvent as a set of molecules that compete to
react with the acid-base species. Rather we consider the solvent in its entirety as one of the
two adducts. Taking this point of view is especially relevant in polar solvents like water that
are characterized by highly structured networks. In this case the presence of an excess or
a deﬁciency of protons changes locally the network structure and this distortion propagates
along the entire network.
Since the very early days of Eigen and Zundel,21,22 researchers have struggled with how
many molecules should be included in the deﬁnition of the perturbation.23–25 Given the
absence of physical parameters capable of giving a clear and unequivocal answer to this
question, the idea of considering the solvent as a whole circumvents this problem. Thus
the solvent is not just a medium with a passive role, but it is looked at as an ensemble of
molecules that contribute collectively to the formation of the conjugate acid-base pair. This
point of view is much closer to the original one proposed by Brønsted and Lowry in which
the reaction can be seen as a simple exchange of an hydrogen cation between an acid-base
pair.
For the reaction to take place the center of the perturbation has to move away from
the solute. Thus the second important step is to monitor the center of the perturbation.
Due to Grotthuss-like mechanisms the perturbation moves along the network.
This can
lead to diﬀerent deﬁnitions of the defect center. However, if we tessellate the whole space
using Voronoi polyhedra centered on water oxygen atoms we can assign unequivocally every
4


## Page 5


hydrogen atom to one and only one of these polyhedra. The site whose Voronoi polyhedron
contains an anomalous number of protons is taken as the center of the perturbation (see
Fig. 1).
Figure 1: Two examples of partitioning the space.
On the left we show a convectional
approach in which the distance from oxygen atom is used to deﬁne its surrounding. Clearly
artiﬁcial superpositions can be seen. On the right the Voronoi tessellation does not suﬀer
from these shortcomings.
This new point of view gives the method a very general nature making it applicable to
every acid-base system, without the need of ﬁxing beforehand the reacting pairs. Thus it
is possible to explore all the relevant protonation states even in systems composed by more
than one acid-base pair.
This general approach allows deﬁning CVs without having to impose speciﬁc structures or
select the identity of the atoms involved. We test our method by performing metadynamics
simulations in a weak acid case (acetic acid), a weak base (ammonia) and in an ampho-
teric species (bicarbonate) chosen as benchmark because of their comparable strength, but
diﬀerent acid-base behaviour.
5


## Page 6


Methods
As discussed above we introduce two CVs, one related to the protonation state and the other
that locates the charge defects and measures their relative distance. Both of these CVs need
a robust deﬁnition for assigning the hydrogen atoms to the respective acid-base site. In order
to achieve this result we partition the whole space into Voronoi polyhedra centered on the
acid-base sites i located at Ri. The sites include all the atoms able to breaking and forming
bonds with an acid proton. The standard Voronoi space partition is described by a set of
index functions wi(r) centered on the diﬀerent Ris such that wi(r) = 1 if the i-th atom is
the closest to r, and equal to 0 otherwise. For their use in enhanced sampling methods CVs
need to be diﬀerentiable. To this eﬀect we introduce a smooth version of the index functions,
ws
i (r). These are deﬁned using softmax functions:
ws
i (r) =
e−λ|Ri−r|
X
m
e−λ|Rm−r|,
(2)
where i and m run all over the acid-base sites and λ controls the steepness with which the
curves decays to 0, that is the selectivity of the function. With an appropriate choice of λ
this deﬁnition achieves the desired result as shown in Fig. 2. In such a way, an hydrogen
atom in a position Rj is assigned to the polyhedron centered on the site i with the weight
wi(Rj). Then, the total number of hydrogen atoms assigned to the i-th acid-base site is:
Wi =
X
j∈H
ws
i (Rj),
(3)
where the summation on j runs all over the hydrogen atoms.
One can associate to each acid-base site a reference value W 0
i that counts the number
of bonded hydrogen atoms in the neutral state. The diﬀerence between the instantaneous
value of hydrogen atoms and the reference one is
6


## Page 7


Figure 2: Smooth tessellation of a 2D space with cells centered on the 3 water molecule
oxygen atoms. The ﬂat blue regions represent the portion of space in which the function
assumes a value of 1 and the yellow ones represent the borders among cells. This surface has
been obtained with a value of λ = 4.
δi = Wi −W 0
i .
(4)
When diﬀerent from zero δi will signal whether the i-th site has gained or lost a proton. In
the case of water oxygen atoms, a hydronium ion has a δi = +1 while a hydroxyde ion has
δi = −1.
We then group the acid-base sites in species. For instance in the case of the simplest
amino acid glycine in aqueous solition the number of species N s will be equal to 3. All water
oxygen atoms belong to one species, then one counts in another species the two carboxylic
oxygen atoms and ﬁnally one considers as the third species the nitrogen atom of the amino
group.
In the spirit of this work we count the total excess or defect of proton associated to each
species,
qk =
X
i∈k
δi.
(5)
This implies that we are not interested in the speciﬁc identity of the reacted site, but
whether or not the k-th species in its entirety has gained (qk = +1), lost (qk = −1) or has
7


## Page 8


not changed its number of protons. If we consider a solute with only one reactive moiety
then each possible state of the system can be described by one of the three two dimensional
vectors (0,0), (-1,1) or (1,-1).
In the general case each protonation state can be described by a vector ⃗q = (q0, q1, . . . qNs−1)
with dimension equal to the number of inequivalent reactive sites, N s. A more exhaustive
explanation is provided in the S.I.
For use in enhanced sampling these vectors need to be expressed as a scalar function
f = f(⃗q) such that, for each physically relevant ⃗q, f attains values able to distinguish the
diﬀerent overall protonation states. There are inﬁnite many ways of constructing a scalar
from a vector. Possibly the simplest choice is to write f(⃗q) = ⃗X·⃗q and, in order to distinguish
between diﬀerent protonation states, to choose ⃗X = (20, 21, 22, . . . 2Ns−1).
This leads to the following deﬁnition for the CV, that is used to describe the protonation
state of the system:
sp =
Ns−1
X
k=0
2k · qk,
(6)
where k are the indexes used to label the respective reactive site groups. In the appendix an
example is worked out in detail. Of course the CV is made continuous by the use of Wi in
the calculation of the δi needed to evaluate qk in Eq. 5.
The second CV is a summation of distances between every acid-base sites multiplied for
their partial charge δi.
sd =
X
i,m>i
−rim · δi · δm,
(7)
where the indexes i and m run all over the acid-base sites belonging to diﬀerent k groups,
and rim is the distance between the two atoms. In this way, just the acid-base pair that
has exchanged a proton gives a contribution diﬀerent from zero. Eq. 7 is valid only when
one single conjugate acid-base pair is present. However, due to the action of bias it may
occur occasionally that several acid-base pairs may be formed. In order to avoid sampling
these very unlikely events we apply a restraint on the number of pairs. Further details are
8


## Page 9


provided in the S.I.
Results
We have applied our method to three aqueous solution of acetic acid, ammonia and bicarbon-
ate as representations of a weak acid, a weak base and an amphoteric compound respectively.
The setup of all three simulation is identical except for the identity of the solvated molecules.
This ensures that the outcome reﬂects the diﬀerent chemistry of these three systems and that
there is no bias due to the initial condition.
Each simulation of the systems has been performed with Born-Oppenheimer MD simula-
tions combined with well-tempered metadynamics14,26 using CP2K package27 patched with
PLUMED 228 and SCAN functional29 for the xc energy, Exc. See the S.I. for details.
0
2
4
6
8
ï 1
ï 0.5
0
0.5
1
ï 1
ï 0.5
0
0.5
1
ï 1
ï 0.5
0
0.5
1
sd
sp
0
8
16
24
32
40
sp
8
16
24
32
40
sp
20
40
60
80
100
(a)
(b)
(c)
Figure 3: Free energy surfaces along sp and sd of acetic acid (a), ammonia (b) and bicarbonate
(c) in aqueous solution. Colorbars indicate the free energy expressed in kJ mol−1 units. The
CV sd is expressed in ˚A.
In Fig. 3 we plot the Free Energy Surfaces (FESs) as a function of sp and sd. These
FESs vividly reproduce the expected behaviour. They all have a minimum at sp = 0 that
correspond to the state in which no charges are present in the solvent. In the acetic acid
FES (Fig. 3-a) a second minimum close to sp = −1 reﬂects its acid behaviour. By contrast,
the ammonia FES (Fig. 3-b) shows a second minimum close to sp = 1.
The shape of
9


## Page 10


ammonia and acetic acid FES are approximately related by a mirror symmetry reﬂecting
their contrasting behaviour. Similarly the bicarbonate symmetric FES (Fig. 3-c) mirror its
amphoteric character.
As the conjugate pair is formed sd starts to assume positive values corresponding to the
separation and diﬀusion of the conjugate pair. Compared to the undissociated state in which
only sd = 0 is allowed, states where a conjugate pair is present show an elongated shape
of the basins along this variable. This is caused by the diﬀusive behaviour of hydronium e
hydroxide ion in solution that makes accessible a continuum range of distances. Moreover,
along this CV we can observe a barrier around 1.5 corresponding to the breaking of the
covalent bond between the hydrogen atom and the acid-base site.
Conclusions
The general applicability of this method to systems with diﬀerent nature is an important
step made in their understanding and description. The scheme can be extended to include
quantum nuclear eﬀects with the use of path integrals molecular dynamics.30 This would
be of quantitative signiﬁcance since for instance pKa values are aﬀected by deuteration.
Moreover, the absence of assumptions or impositions about reactive candidates or reaction
paths allows extending this method to systems of increasing complexity which cannot be
addressed with traditional methods. Examples of questions that can now be answered are
tautomeric equilibria in biochemical processes, acid behaviour in Zeolites and on the surface
of oxides exposed to water.
Acknowledgement
This research was supported by the European Union Grant No. ERC-2014-AdG-670227/VARMET.
Calculations were carried out on the ETH Euler cluster and on the M¨onch cluster at the
Swiss National Supercomputing Center (CSCS).
10


## Page 11


Supporting Information
CV1: sp
As described in the main text, the CV adopted to described the protonation state is
sp =
Ns−1
X
k=0
2k · qk.
(8)
Here, every component qk can assume a value equal to −1 for the k-th group whose
chemical behaviour is acid, +1 for a basic one, and equal to zero for unreacted groups.
Then, these values are summed with a diﬀerent weight given by the power of two of the
group index k. The prefactor 2k allows to linearly combine a multiplet of values with a
mathematical trick reducing the vector ⃗q ≡(q0,q1,. . . ,qNs−1) in a single unambiguous scalar
number. Assuming we don’t know anything about the reactivity of a system composed by 3
diﬀerent groups able to react, a priori we cannot exclude any of its 7 diﬀerent protonation
states (see Tab. 1).
Table 1: The three components of the vector ⃗q and the respective CV values.
q0
q1
q2
0
0
0
1
−1
0
−1
1
0
0
1
−1
0
−1
1
1
0
−1
−1
0
1
=⇒
sp
0
−1
1
−2
2
−3
3
As shown, all of these protonation states occupy diﬀerent positions in the CV space with-
out overlap among the states. This ensures the possibility to explore all of them starting
from the most energetically accessible until the highest one in energy. Moreover, this ap-
proach allows to address systems in which multiple and unknown competitive reactions are
present without beforehand ﬁx the reactive pairs.
11


## Page 12


CV2: sd
This CV returns a value proportional to the distance between the fully formed conjugate
acid-base pair. Once the proton transfer has taken place, two acid-base sites will have an
anomalous number of hydrogen atoms within their Voronoi polyhedra. We can deﬁne the
partial charge δi assigned to the i-th Voronoi polyhedron as
δi = Wi∈k′ −NH∈k′
Nk′ ,
(9)
where Nk′ and NH are constants indicating respectively the total number acid-base sites
belonging to the k′-th group and the hydrogen atoms bonded to them in the equilibrium
state, while Wi is the instantaneous number of hydrogen atoms assigned to the i-th acid-base
site.
This means, for example, that in an system composed by a molecule of acetic acid and
31 molecules of water, every water oxygen atoms has NH = 62 and N0 = 31 while the acid
ones have NH = 1 and N1 = 2. In the initial frame all the water sites have a values of Wi
close to 2, NH/N0 = 2 and therefore δi close to zero. After having subtracted a proton by
the acid molecule, one of the sites i of the solvent will assume a value of Wi′ close to 3 and
δi′ to 1. The two acetic acid oxygen atoms have only one hydrogen assigned to them and
then NH/N0 = 0.5. In the undissociated species Wi is 1 for the site bonded to the hydrogen
atom and 0 to the other one making the δi values equal to +0.5 and -0.5 respectively. After
the dissociation these sites must be indistinguishable and the acid molecule able to capture
again a proton with one of them without any preference. Then, the partial charges will be
-0.5 for both of the sites. This ensures that the opposite sign terms cancels each other in
the undissociated case (Fig. 4-A) and gives an averaged contribution in the dissociated one
(Fig. 4-B).
12


## Page 13


A
B
Xi
δ1 = −0.5
δ0 = −0.5
δ0 = + 0.5
r1i
sd = −0.5 · δi · r0i + 0.5 · δi · r1i
sd = 0.5 · δi · r0i + 0.5 · δi · r1i
= 0.5 · δi · (r0i + r1i) ≈r01 · δi
= 0.5 · δi · (r1i −r0i) ≈0
∗r0i ≈r1i
r0i
δ1 = −0.5
Xi
r1i
r0i
Figure 4: Schematic view of sd calculation between Acetic acid (A) or acetate (B), and a
generic species Xi.
Restraint: sr
A restraint has been applied in order to avoid the formation of more then one conjugate
acid-base pair.
sr =
X
i
q
δ2
i + α,
(10)
where i run all over the acid-base site indexes and α is a positive number much less than
1. With a proper value of α the square root term is a good approximation of the absolute
value that allows to avoid the singularity for δi = 0 (see Fig. 5)
This CV returns the summation of the all the partial charge moduli. This function can
be restrained limiting at the given time the number of reacted pairs simultaneously present.
Ab initio MD setup
As reported in the main text, all the simulations have been performed with Born-Oppenheimer
MD simulations using CP2K package27 patched with PLUMED2.28 Details and parameters
adopted in the ab initio MD simulations are reported in Tab. 2 .
13


## Page 14


0
0.5
1
−1
−0.5
0
0.5
1
f(δi)
δi
|δi|
q
δ2
i + α
Figure 5: Diﬀerent behaviour of absolute value function (blue line) and the smoothed version
(orange line) in proximity of δi = 0. The parameter α controls the smoothness of the curve.
In this plot the value of α has been set equal to 10−2.
Box thermalization
Each system, composed by 31 molecules of water and 1 of solute, has been thermalized as
reported in Tab. 3.
The reason for this somewhat odd looking schedule is that the NPT ensemble module of
CP2K does not support SCAN.
Well-tempered metadynamics setup
Parameters adopted for PLUMED2 settings are reported in Tab.4
References
(1) Ho, J.; Coote, M. L. First-principles prediction of acidities in the gas and solution
phase. Wiley Interdiscip Rev Comput Mol Sci 2011, 1, 649–660.
(2) Elstner, M.; Hobza, P.; Frauenheim, T.; Suhai, S.; Kaxiras, E. Hydrogen bonding
and stacking interactions of nucleic acid base pairs: A density-functional-theory based
treatment. J. Chem. Phys. 2001, 114, 5149–5155.
14


## Page 15


Table 2: Ab initio MD parameters.
ACETIC ACID
AMMONIA
BICARBONATE
Reactive molecule
1
1
1
Water molecules
31
31
31
Ensemble
NVT
NVT
NVT
Temperaure (K)
300
300
300
Thermostat
CSVR31
CSVR31
CSVR31
Cell length (˚A)
9.97
9.80
10.47
Basis sets
TZV2P-GTH
TZV2P-GTH
TZV2P-GTH
Potential
GTH-PBE
GTH-PBE
GTH-PBE
Energy cutoﬀ(Ry)
600
600
800
Relative cutoﬀ(Ry)
60
60
80
EPS SCF
1.0E-6
1.0E-6
1.0E-6
XC Functional
SCAN29
SCAN29
SCAN29
Time step (fs)
0.5
0.5
0.5
Length time (ps)
258
285
461
Table 3: Thermalization protocol.
Step
Type
Ensemble
Length time (ps)
XC funct.
1
Geom. Opt.
-
-
PBE32
2
MD
NVT
1
PBE32
3
MD
NPT
10
PBE32
4
MD
NVT
2.5
PBE32
5
MD
NVT
2.5
SCAN29
(3) Saracino, G. A.; Improta, R.; Barone, V. Absolute pKadetermination for carboxylic
acids using density functional theory and the polarizable continuum model. Chem.
Phys. Lett. 2003, 373, 411–415.
(4) Sch¨u¨urmann, G.; Cossi, M.; Barone, V.; Tomasi, J. Prediction of the pKa of Carboxylic
Acids Using the ab Initio Continuum-Solvation Model PCM-UAHF. J. Phys. Chem. A
1998, 102, 6706–6712.
(5) Ho, J.; Coote, M. L. A universal approach for continuum solvent pKa calculations: Are
we there yet? Theor. Chem. Acc. 2009, 125, 3–21.
(6) Silva, C. O.; da Silva, E. C.; Nascimento, M. A. C. Ab Initio Calculations of Absolute
15


## Page 16


Table 4: PLUMED parameters.
ACETIC ACID
AMMONIA
BICARBONATE
Gaussian hills heights
0.25
0.25
0.5
Gaussian hills widths (sp)
0.2
0.2
0.2
Gaussian hills widths (sd)
0.4
0.4
0.4
Bias factor
10
10
15
Temperature (K)
300
300
300
Hills deposition rate
100
100
100
λ (sp)
5
5
5
λ (sd)
8
8
8
λ (sr)
12
12
12
α (sr)
1.0E-4
1.0E-4
1.0E-4
p K a Values in Aqueous Solution II. Aliphatic Alcohols, Thiols, and Halogenated
Carboxylic Acids. J. Phys. Chem. A 2000, 104, 2402–2409.
(7) Rebollar-Zepeda, A. M.; Galano, A. Quantum mechanical based approaches for predict-
ing pK a values of carboxylic acids: evaluating the performance of diﬀerent strategies.
RSC Adv. 2016, 6, 112057–112064.
(8) Davies, J. E.; Doltsinis, N. L.; Kirby, A. J.; Roussev, C. D.; Sprik, M. Estimating pKa
values for pentaoxyphosphoranes. J. Am. Chem. Soc. 2002, 124, 6594–6599.
(9) Park, J. M.; Laio, A.; Iannuzzi, M.; Parrinello, M. Dissociation mechanism of acetic
acid in water. J. Am. Chem. Soc. 2006, 128, 11318–11319.
(10) Tummanapelli, A. K.; Vasudevan, S. Dissociation Constants of Weak Acids from ab
Initio Molecular Dynamics Using Metadynamics: Inﬂuence of the Inductive Eﬀect and
Hydrogen Bonding on p K a Values. J. Phys. Chem. B 2014, 118, 13651–13657.
(11) Ort´ız, A. P. D. A.; Tiwari, A.; Puthenkalathil, R. C.; Ensing, B. Advances in enhanced
sampling along adaptive paths of collective variables. J. Chem. Phys. 2018, 072320.
(12) Lee, J. G.; Asciutto, E.; Babin, V.; Sagui, C.; Darden, T.; Roland, C. Deprotonation
of solvated formic acid: Car-parrinello and metadynamics simulations. J. Phys. Chem.
B 2006, 110, 2325–2331.
16


## Page 17


(13) Bernardi, R. C.; Melo, M. C.; Schulten, K. Enhanced sampling techniques in molecular
dynamics simulations of biological systems. Biochim. Biophys. Acta 2015, 1850, 872–
877.
(14) Laio, A.; Parrinello, M. Escaping Free-Energy Minima. Proc. Natl. Acad. Sci. (USA)
2002, 99, 12562.
(15) Valsson, O.; Parrinello, M. Variational approach to enhanced sampling and free energy
calculations. Phys. Rev. Lett. 2014, 113, 1–5.
(16) Torrie, G. M.; Valleau, J. P. Nonphysical sampling distributions in Monte Carlo free-
energy estimation: Umbrella sampling. J. Comput. Phys. 1977, 23, 187–199.
(17) Piccini, G.; McCarty, J. J.; Valsson, O.; Parrinello, M. Variational Flooding Study of
a SN2 Reaction. J. Phys. Chem. Lett. 2017, 8, 580–583.
(18) Mendels, D.; Piccini, G.; Parrinello, M. Collective Variables from Local Fluctuations.
J. Phys. Chem. Lett. 2018, 9, 2776–2781.
(19) Piccini, G.; Polino, D.; Parrinello, M. Identifying Slow Molecular Motions in Complex
Chemical Reactions. J. Phys. Chem. Lett. 2017, 8, 4197–4200.
(20) Agmon, N. The Grotthuss mechanism. Chem. Phys. Lett. 1995, 244, 456–462.
(21) E. Wicke, T. A., M. Eigen ¨Uber den Zustand des Protons (Hydroniumions) in w¨aßriger
L¨osung. Z. Phys. Chem. 1954, 1, 340–364.
(22) Zundel, G.; Metzger, H. Energiebander der tunnelnden uberschu-protonen in ﬂussigen
sauren. Eine IR-spektroskopische untersuchung der natur der gruppierungen H5O2+.
Z. Phys. Chem. 1968, 58, 225–245.
(23) Marx, D.; Tuckerman, M. E.; Hutter, J.; Parrinello, M. The nature of the hydrated
excess proton in water. Nature 1999, 397, 601–604.
17


## Page 18


(24) Hulthe, G.; Stenhagen, G.; Wennerstr¨om, O.; Ottosson, C. H. Water clusters studied
by electrospray mass spectrometry. J. Chromatogr. A 1997, 777, 155–165.
(25) Iyengar, S. S.; Petersen, M. K.; Day, T. J.; Burnham, C. J.; Teige, V. E.; Voth, G. A.
The properties of ion-water clusters. I. the protonated 21-water cluster. J. Chem. Phys.
2005, 123, 1–9.
(26) Barducci, A.; Bussi, G.; Parrinello, M. Well-tempered metadynamics: A smoothly
converging and tunable free-energy method. Phys. Rev. Lett. 2008, 100, 1–4.
(27) Vandevondele, J.; Krack, M.; Mohamed, F.; Parrinello, M.; Chassaing, T.; Hutter, J.
Quickstep: Fast and accurate density functional calculations using a mixed Gaussian
and plane waves approach. Comput. Phys. Commun. 2005, 167, 103–128.
(28) Brandenburg, J. G.; Bates, J. E.; Sun, J.; Perdew, J. P. Benchmark tests of a strongly
constrained semilocal functional with a long-range dispersion correction. Phys. Rev. B
2016, 94, 17–19.
(29) Peng, H.; Yang, Z.-H.; Sun, J.; Perdew, J. P. Versatile van der Waals Density Functional
Based on a Meta-Generalized Gradient Approximation Haowei. Phys. Rev. X 2015,
041005, 1–15.
(30) Parrinello, M.; Rahman, A. Study of an F center in molten KCl. J. Chem. Phys. 1984,
80, 860–867.
(31) Bussi, G.; Donadio, D.; Parrinello, M. Canonical sampling through velocity rescaling.
J. Chem. Phys. 2007, 126.
(32) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made
simple. Phys. Rev. Lett. 1996, 77, 3865–3868.
18

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1905_02080v1_a_microscopic_description_of_acid_base_equilibrium
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1905_02080V1_A_MICROSCOPIC_DESCRIPTION_OF_ACID_BASE_EQUILIBRIUM.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
