---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1611.03519v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1611.03519v2_Evolutionary_optimization_of_a_charge_transfer_ionic_potential_model_for_Ta_Ta-o

> Source: 1611.03519v2_Evolutionary_optimization_of_a_charge_transfer_ionic_potential_model_for_Ta_Ta-o.pdf

> Pages: 35

---


## Page 1


1 
Evolutionary Optimization of a Charge Transfer Ionic Potential Model for Ta/Ta-
Oxide Hetero-interfaces 
 
Kiran Sasikumar,1,ξ,*  Badri Narayanan,1,ξ Mathew Cherukara,2 Alper Kinaci,1 Fatih G. Sen,1 Stephen K. 
Gray,1,3 Maria K. Y. Chan,1,3 and Subramanian K. R. S. Sankaranarayanan1,3,* 
 
1 Center for Nanoscale Materials, Argonne National Laboratory, Argonne, IL, 60439 
2 X-ray Sciences Division, Argonne National Laboratory, Argonne, IL, 60439 
3 Computation Institute, University of Chicago 
ξ Equal Contributions 
Abstract 
 
Heterostructures of tantalum and its oxide are of tremendous technological interest for a myriad 
of technological applications, including electronics, thermal management, catalysis and biochemistry. In 
particular, local oxygen stoichiometry variation in TaOx memristors comprising of thermodynamically 
stable metallic (Ta) and insulating oxide (Ta2O5) have been shown to result in fast switching on the sub-
nanosecond timescale over a billion cycles. This rapid switching opens up the potential for advanced 
functional platforms such as stateful logic operations and neuromorphic computation. Despite its broad 
importance, an atomistic scale understanding of oxygen stoichiometry variation across Ta/TaOx hetero-
interfaces, such as during early stages of oxidation and oxide growth, is not well understood. This is 
mainly due to the lack of a unified interatomic potential model for tantalum oxides that can accurately 
describe metallic (Ta), ionic (TaOx) as well as mixed (Ta/TaOx interfaces) bonding environments 
simultaneously. To address this challenge, we introduce a Charge Transfer Ionic Potential (CTIP) model 
for Ta/Ta-oxide system by training against lattice parameters, cohesive energies, equations of state (EOS), 
elastic properties, and surface energies of the various experimentally observed Ta2O5 polymorphs 
(hexagonal, orthorhombic and monoclinic) obtained from density functional theory (DFT) calculations. 
The best CTIP parameters are determined by employing a global optimization scheme driven by genetic 
algorithms followed by local Simplex optimization. Our newly developed CTIP potential accurately 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
*!Corresponding authors: ssankaranarayanan@anl.gov, ksasikumar@anl.gov!


## Page 2


2 
predicts structure, thermodynamics, energetic ordering of polymorphs, as well as elastic and surface 
properties of both Ta and Ta2O5, in excellent agreement with DFT calculations and experiments. We 
employ our newly parameterized CTIP potential to investigate the early stages of oxidation and atomic 
scale mechanisms associated with oxide growth on Ta surface at various temperatures. The CTIP 
potential developed in this work is an invaluable tool to investigate atomic-scale mechanisms and 
transport phenomena underlying the response of Ta/TaOx interfaces to external stimuli (e.g, temperature, 
pressure, strain, electric field etc.), as well as other interesting dynamical phenomena including the 
physics of switching dynamics in TaOx based memristors and neuromorphic devices. 
1. Introduction 
Tantalum and its oxide are materials of broad technological interest, owing to their exceptional 
physical, chemical, and opto-electronic properties [1, 2, 3, 4]. In the metallic form, tantalum and its alloys 
display excellent corrosion resistance [5], chemical inertness [6], high thermal stability [7], and 
exceptional strength [8]. This makes Ta alloys suitable for use in turbine blades, rocket nozzles and nose 
caps for supersonic aircraft [8]. As oxide, tantalum pentoxide (most stable TaOx), is an important 
dielectric material that has widespread applications in capacitors, dynamic random access memories 
(DRAMs), optical coatings, high-temperature reflectors and antireflection coatings [4, 9, 10, 11, 12, 13]. 
Amongst the various dielectrics, Ta2O5 has received distinct attention owing to its high dielectric constant 
(~ 35), high refractive index and chemical and thermal stability, as well as the promise of compatibility 
with microelectronics processing [4, 9, 12, 14]. To successfully employ thin film materials such as TaOx 
for device applications, it is crucial to develop sophisticated synthesis and processing techniques, which 
in turn depends on our understanding of the structure-property relationships. 
Hetero-structures of Ta and Ta2O5 are also being considered as potential platforms for 
neuromorphic computation [4, 15]. TaOx memristors have been shown to display unique switching 
properties on the sub-nanosecond timescale over more than a billion cycles [15]. Such reversibility was 
attributed to the motion of oxygen vacancies. The subsequent localized variations in oxygen


## Page 3


3 
stoichiometries in TaOx system, under an applied electric field, have been exploited to switch between the 
two thermodynamically stable states i.e. metallic Ta and insulating Ta2O5 [4, 15]. In order to realize the 
use of TaOx in emerging applications such as neuromorphic computing, it is highly desirable to identify 
optimal material systems (and their state variables), and develop predictive models of the underlying 
atomistic mechanisms governing their resistive switching. An atomistic scale understanding of the 
structure and dynamics across Ta/TaOx interfaces will allow us to predictively model and control the 
resistive state, thereby facilitating their integration into functional systems. 
In addition to the metal/oxide interfaces and hetero-structures of TaOx, the dynamical phenomena 
associated with the nanoscale oxidation [16, 17] and oxide growth processes in such systems are also of 
fundamental interest. Numerous experimental studies have focused on the thermal oxidation in bulk Ta 
and thin films of Ta [18, 19]. For example, Chandrasekaran et al. have used Auger depth profiling to 
study the thermal oxidation of 700 nm Ta thin films in the 600-1000 K range [18]. They find the oxide 
growth rate to be logarithmic at low temperatures <600 K and parabolic at high temperatures ~800 K. 
Similarly, Ruffel et al. have studied the formation and characterization of Ta2O5/TaOx (oxide/suboxide) 
hetero-structures via high fluence O ion-implantation into deposited Ta films [19]. Their study showed 
that oxygen stoichiometry in the hetero-structures can be tuned by O-ion implantation energy and fluence. 
While these studies have studied the microstructural evolution and formation of these oxide films, the 
nanoscale oxidation kinetics as well as atomistic details of the structure, stoichiometry and the limiting 
thickness of the Ta oxide thin films are largely unknown. 
Probing the early stages of nanoscale oxidation and oxide growth is often difficult with 
experiments. With the significant improvement in computational resources, atomistic simulations are now 
emerging as a viable alternative to study the structural and dynamical evolution of the metal/oxide 
interfaces. First principles approaches based on density functional theories have been primarily employed 
to study the initial stages of O2 reaction with metal surfaces, the dissociation processes involved in 
oxidation, and the stability of the various adsorption sites (top, bridge and hollow sites on FCC or HCP 
lattice) [20, 21]. Due to the computational cost, however, it is currently not feasible to use first principles


## Page 4


4 
approaches to directly model nanoscale oxide growth on metal surfaces. Classical molecular dynamics 
(MD) simulations based on semi-empirical potentials provide an ideal route to model dynamical 
phenomena associated with metal oxidation and oxide growth. There is, thus, a clear need for large-scale 
atomistic simulations employing semi-empirical potentials to study nanoscale oxidation of metals such as 
Ta. 
The success of classical MD in modeling metal/oxide systems hinges on the ability of the 
employed potential model to accurately describe interatomic interactions in both the metallic and oxide 
regions. Additionally, this potential model should accurately capture the structural, chemical, 
thermodynamic, elastic, and surface properties of Ta and TaOx phases. To date, however, there is only 
one semi-empirical Morse-BKS potential function for Tantalum oxide, developed by Trinastic et al. [22], 
which primarily targets amorphous, yet stoichiometric,) Ta2O5 systems. This model is, however, a fixed 
charge model and is not capable of capturing the multiple oxidation states encountered in oxide/metal 
hetero-interfaces. 
Here, we introduce a charge transfer ionic potential model for Ta/TaOx system that successfully 
captures the thermo-physical, structural and surface properties of both Ta and various polymorphs of 
Ta2O5 as well as their interfaces. For the potential formalism, we choose the charge transfer ionic 
interatomic potential developed by Zhou and Wadley [23, 24] since it allows the environment-dependent 
charges on the atoms to be dynamically deduced. During metal oxidation and oxide growth, metal ions 
attain significant positive charges whereas significant negative charges are attained by oxygen anions. 
Therefore, the atomic charges are environment dependent and dynamically vary during the course of the 
oxidation process. For instance, Ta charges in the stoichiometric oxide are expected to change 
continuously from a zero value in a fully metallic region to their valency-determined maximum value. To 
model such a scenario, one requires a potential model such as charge transfer ionic potential (CTIP) that 
seamlessly allows for switching between an environment dominated by ionic interactions in the oxide and 
metallic interactions in the metal region. This formalism has been successfully used in the past to 
investigate oxidation of several metal and alloy surfaces and nanoparticles [25, 26, 27, 28]. To determine


## Page 5


5 
the force-field parameters for complex functional forms like CTIP, we require a systematic approach that 
can enable efficient sampling of most of the available parameter space. We have recently demonstrated 
that evolutionary global optimization methods such as genetic algorithms (GA) represent a powerful 
strategy for fitting force fields [29, 30, 31, 32]. Here, we use a combination of GA to perform sampling of 
the parameter landscape, and local minimization methods (simplex) starting from promising parameter 
sets identified by GA to obtain an optimized CTIP potential model. 
Our paper is organized as follows: Section 2 describes variable charge potential model formalism 
i.e. the CTIP functional forms as well as the training data set, the fitting procedure and parameterization 
strategies employed by us for potential model development. We also describe the model setup used to 
investigate early stages of Ta oxidation. Section 3 reports our results on the evolutionary optimization, the 
optimized CTIP parameters obtained in this study, the various structural and energetic properties 
predicted by the optimized set of parameters, and their success in describing inter-atomic interactions in 
Ta2O5. In Section 4, we apply the newly developed CTIP parameter set to investigate structure and 
stoichiometry across Ta, Ta-oxide and their hetero-interfaces. Here, we provide a representative example 
on the application of our newly developed CTIP to study the early stages of oxidation and oxide growth 
on the (110) surface of body-centered cubic (bcc) Ta at various temperatures. Finally, Section 5 
summarizes the key findings and provides concluding remarks. 
2. Methods 
 
i. 
Charge transfer ionic potential (CTIP) 
 
We use the modified charge transfer potential model developed by Zhou et al. [23, 24]. This potential 
model comprises of two parts: ionic interactions in the oxide region are modeled using an electrostatic 
term (Ees), and the embedded atom method is used to model metallic interactions i.e. non-electrostatic 
contributions.  
m
es
t
E
E
E
+
=
                                                                   (2.1)


## Page 6


6 
In the CTIP model, charge bounds were imposed on cations and anions to prevent them from exceeding 
their valence charges. This overcomes the limitations of the original Streitz-Mintmire potential [33]. In 
the modified CTIP, the electrostatic energy is given as below [24]: 
Ees = E0 +
qiXi + 1
2
qiqjVij
j=1
N
∑
i=1
N
∑
i=1
N
∑
+
ω 1−qi −qmin,i
qi −qmin,i
#
$
%%
&
'
((
i=1
N
∑
(qi −qmin,i)
2 +
ω 1−qmax,i −qi
qi −qmax,i
#
$
%%
&
'
((
i=1
N
∑
(qi −qmax,i)
2            (2.2) 
where qmin,i and qmax,i are the charge bounds of atom i, qmin,i < qi < qmax,i. Coefficient ω imposes energy 
penalty on the metal atoms to gain electrons or lose inner shell electrons and on the oxygen atoms to lose 
electrons or receive more than two electrons. Xi represents self energy and Vij represents Coulomb 
interaction [24]. 
Xi = χi +
kc
j=i1
iN
∑Z j
j fi
"#
$%−fi fj
"#
$%
(
)                                                               (2.3) 
Vij = Jiδij +
kc
k=j(i1)
j(iN )
∑
fi fk
"#
$%
(
)                                                                   (2.4) 
In the above equations, χi refer to the electro-negativity and Ji refers to atomic hardness (or self Coulomb 
repulsion), respectively. As shown in Eqs. (2.5)-(2.7), Coulomb integrals such as a fb
!"
#$ and fa fb
!"
#$  are 
calculated assuming atomic charge density distribution for spherical Slater-type orbitals [23]: 
[
]
)
2
exp(
1
)
2
exp(
1
ab
b
ab
ab
b
b
ab
b
r
r
r
r
f
a
ξ
ξ
ξ
−
−
−
−
=
                                     (2.5) 
For
b
a
ξ
ξ
ξ
=
=
, fa fb
!"
#$= 1
rab
1−1+11
8
ξrab + 3
4
ξ
2rab
2 + 1
6
ξ
3rab
3
&
'(
)
*+exp(−2ξ rab)
!
",
#
$-                      (2.6) 
For 
b
a
ξ
ξ ≠
, [
]
2
2
4
2
2
4
)
(
)
(
)
2
exp(
)
(
)
(
)
2
exp(
1
b
a
b
a
ab
b
a
b
b
a
b
a
ab
a
b
a
ab
b
a
r
r
r
f
f
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
−
+
−
−
−
+
−
−
=
 
 
3
3
6
4
2
3
3
6
4
2
)
(
)
(
)
2
exp(
)
3(
)
(
)
(
)
2
exp(
)
3(
a
b
b
a
ab
ab
b
a
a
b
b
a
b
a
ab
ab
a
b
b
a
r
r
r
r
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
ξ
−
+
−
−
−
−
+
−
−
−
                                 (2.7) 
Here a=i,j, b=i,j and a≠b. Table 1 lists the optimized charge parameters χi, Ji,, ξ and Zi  as well as the 
charge bounds for the various elements.


## Page 7


7 
 
The embedded atom method (EAM) is used to represent the non-electrostatic interactions in the 
metallic region as follows [23, 33]: 
Em = 1
2
ϕij(rij)
j=i1
iM∑
i=1
N
∑
+
Fi
i=1
N
∑
(ρi)                                                     (2.8) 
In Eq. (2.8), Φij (rij) represents the pair-wise interaction energy between atoms i and j that are at distance rij 
apart. N is the total number of atoms and iM is the number of neighbors for atom i. For an alloy system, 
the generalized elemental pair potentials is given by [23]: 
20
20
1
1
exp
1
1
exp
)
(
!!
"
#
$$
%
&
−
+
(
)
*
+
,
-
!!
"
#
$$
%
&
−
−
−
!!
"
#
$$
%
&
−
+
(
)
*
+
,
-
!!
"
#
$$
%
&
−
−
=
λ
β
κ
α
φ
e
e
e
e
r
r
r
r
B
r
r
r
r
A
r
                                            (2.9) 
Fi represents the embedding energy i.e. energy required to embed an atom i into a local site with electron 
density ρi [23]: 
)
(
1
ij
N
i
i
i
r
f
∑
=
=
ρ
                                                                 (2.10) 
In the above expression, fi(rij) is the electron density at the site of atom i arising from atom j separated by 
distance rij, which is given by [23]: 
20
1
1
exp
)
(
!!
"
#
$$
%
&
−
+
!!
"
#
$$
%
&
!!
"
#
$$
%
&
−
−
=
λ
β
e
e
e
r
r
r
r
f
r
f
                                                             (2.11) 
The embedding energy functions F are selected to work well over a wide electron density range. For a 
smooth variation of the embedding energy, we fit spline functions across different density ranges [23].  
 
The metal-oxygen and oxygen-oxygen interactions are pairwise and of the same functional form 
as Eqn. 2.9. In addition to the pair terms, the oxygen interactions also have an embedding energy based on 
the local electron density. Equation (2.12) gives the functional form of the electron density: 
! ! = !
!!!!"# !!
!
!!!!!!
!!!
!
!!!!!
!"
                                                       (2.12)


## Page 8


8 
The embedding function is defined as follows [23, 24]: 
!! ! = !
!!,! !
!
!!,! −1
!
!
!!!
!;!!!"#,! ≤!! ≤!!!"#,!                         (2.13) 
Here, j varies from 0 to M (the number of metals in the alloy oxide; M=1, here). The optimized EAM 
parameters are listed in Tables 1-5. 
ii. Training data set 
 
Appropriate training and test datasets, that sufficiently sample the potential energy landscape, are 
necessary to develop accurate and transferable force fields. To train our CTIP model, we employ three 
experimentally reported crystalline polymorphs of Ta2O5 (see Fig. 1; Ref. [34, 35]), namely, monoclinic 
(C2/c), δ-hexagonal (P6/mmm) and β-orthorhombic (Pmmm). For each of these polymorphs, the lattice 
constants, internal coordinates, cohesive energy, and equation of state (energy vs. volume) from DFT+U 
calculations are included in the training set. In addition, the training set also consists of 13 independent 
elastic constants of the monoclinic phase. Surface energies of bcc Ta and monoclinic Ta2O5, the bulk 
modulus of all three polymorphs, and the structure and dynamics of the polymorphs at 300 K are not used 
in fitting but used for cross validation tests of the interatomic potential parameters. 
While experimental data can also be used in the evolutionary optimization and cross validation 
tests, there is insufficient experimental data on cohesive energies and elastic constants of different 
polymorphs of Ta2O5 to develop an extensive training set. The available DFT calculations in literature 
also have a range of reported values based on the exchange correlation functional and additional 
approximations. Hence, for consistency, we derived the values of these datasets directly from DFT 
calculations performed with the generalized gradient approximation (GGA) as parameterized by Perdew-
Burke-Ernzerhof (PBE) [35], along with a Hubbard U correction [34, 36, 37] on the Ta 5d electrons. The 
projector-augmented wave formalism as implemented in the Vienna Ab-initio Simulation Package 
(VASP) is used. We employ a plane wave energy cutoff of 500 eV and sample the Brillouin Zone (BZ) 
using Γ-centered Monkhorst-Pack k-point grids, of 2×6×4 for the monoclinic, 3×3×6 for the δ-hexagonal, 
and 6×6×4 for the β-orthorhombic structures. These particular grids were selected based on tests done for


## Page 9


9 
different BZ samplings using from 1 to 123 irreducible k-points. The chosen k-point grids (see supporting 
information Fig. SM5) yield cohesive energies that are within 1 meV/u.f. compared to those obtained 
with larger grid sizes. For the Hubbard U-correction, we choose U = 1.35 eV as derived from linear 
response by Ivanov et al. [34, 36]. For the structural optimization, and the subsequent calculation of 
cohesive energy, equation of state, elastic constants, and surface energies, the atoms were relaxed until 
the forces on each atom was less than 10-4 eV/Å.  
iii. Evolutionary strategy to optimize the CTIP parameters 
 
Single metal oxides under the CTIP formalism require 50 parameters to be appropriately trained. The 24 
EAM parameters for the metal-metal interactions in Ta have been previously optimized by Zhou et al. 
[38]. We adopt these parameters to describe the Ta-Ta interactions, and list them in Table 1. The 
remaining 26 parameters are appropriately trained using an evolutionary strategy. 
Interatomic potential parameterization involves minimizing the objective function (Δ), which is a 
measure of the error between the training set and the fit. For a 26-dimensional parameter set, the objective 
function landscape can be complex with multiple minima. Using local optimization strategies alone, the 
optimized parameters obtained will depend heavily on the initial guess as the objective settles into the 
nearest local minimum (e.g., see Fig. 1e for a schematic representation of the objective landscape of a 2-
dimensional parameter set). An evolutionary strategy such as genetic algorithm (GA) based global 
optimization offer a more efficient sampling of the parameter space. Such an approach has been 
successfully used for fitting force fields for a wide class of materials systems [29, 30, 31, 32]. 
Here, we start with a random population of Np = 50 parameter sets with 26 parameters each. 
Appropriate genetic operations such as crossover and mutation are performed to obtain derived (child) 
parameter sets [39]. The fitness of a particular parameter set (individual) is assessed by the accuracy of its 
predicted properties against the training set, i.e. Δ is defined as a weighted sum of errors in predicted 
properties (computed using MD package LAMMPS [40]). The value of Δ is evaluated for each individual


## Page 10


10 
and Np individuals with the lowest objective function values are chosen for the next iteration of genetic 
operations.  
Once the GA run converges, additional local optimization is performed starting from promising 
parameter sets (15 sets with the lowest error in prediction) using the Simplex algorithm. Test set 
validations are performed before deciding on the final set of optimized parameters (see Fig. 1 for the 
schematic representation of the evolutionary strategy used in this work). The optimized CTIP parameters 
are listed in Tables 2-5. 
iv. Oxidation Simulation Set-up  
 
The optimized parameters are used to investigate the initial stages of oxidation of metallic Ta by 
employing a similar approach used by Sankaranarayanan et al. [25, 26, 27]. The LAMMPS MD package 
[40] is used to perform all the simulations in this work. Two pristine Ta (110) surfaces 4.67!×!4.67!!"! 
are generated for the oxidation simulation by introducing vacuum slabs of 5.63 nm on each side of the 
metal substrate, along a direction normal to the surfaces (see Fig. 2). Periodic boundary conditions are 
applied in the plane of the surface. A sufficiently long cutoff (12 Å) is chosen for the short-range 
Coulomb interactions. Long-range Ewald summations [24] for the Coulomb interaction are performed 
only along the periodic directions.  
 
The slabs are thermalized by annealing in the temperature range 0 K to 300 K in steps of 50 K 
using a Nose-Hoover thermostat [41]. For each temperature, MD simulations are performed in the NVT 
ensemble for 5 ps. This first round of thermalization is performed by ignoring the dynamic charge transfer 
between tantalum atoms. This is appropriate since the charges are zero for a pure metallic system. An 
additional equilibration run of 100 ps is performed at the desired temperature by including the charge 
dynamics and allowing the box to relax in the x- and y- directions by using a Nose-Hoover barostat [42]. 
As expected, we find that the atomic charges fluctuate around a zero value in the pure metal with a 
magnitude of ±!0.05! at the two outer layers and of ±!0.01! in the bulk.


## Page 11


11 
 
The oxidation of the metal substrates is initiated by introducing either O2 molecules or atomic 
oxygen (in separate simulations) in the vacuum slab at at random x, y and z positions.  The velocities of 
the O2 or O are chosen from a Maxwell-Boltzmann distribution corresponding to the desired temperature 
ranging from 300-900 K. Additionally, reflecting boundary conditions are imposed on the molecules that 
might reach the z-direction simulation box boundaries. The gas pressure is maintained constant during the 
simulation by introducing a new O2 molecule or atomic oxygen only when the previous molecule 
dissociates and forms bonds with the metal atoms. This is achieved by tracking the planar position of the 
growing oxide-gas interface (calculated based on the average positions of the outermost metal ions). A 
new oxygen atom/molecule is inserted only when a previous one bonds with the metal ion at the oxide-
gas interface and enters into the oxide-gas interface (zoxygen!<=! zoxide/gas! interface).! The equations of 
motion are integrated using a velocity Verlet scheme with time steps of 0.5 fs for a total time of 200 ps 
for each simulation. The charge relaxation procedure used to minimize the electrostatic energy subject to 
the electro-neutrality principle is performed every MD step. 
3. Results and Discussion 
 
i. Optimization of CTIP parameters for Ta/Ta oxide 
 
Using a single-objective evolutionary optimization technique detailed in Fig. 1, we determine the 
EAM+QEq (CTIP) parameters for a Ta-O binary system by fitting against structural, thermodynamic, and 
elastic properties of the three main polymorphs of Ta2O5, namely, monoclinic (C2/c), hexagonal 
(P6/mmm) and orthorhombic (Pmmm). During each round of optimization, several 26-parameter space 
50-population GA runs are iterated for 100 generations (see pseudo-code in supporting information for 
GA optimization [39]). This allows for a more detailed sampling of the parameter space. Fifteen of the 
best sets from each round of optimization are used to further fine-tune the parameter ranges for the next 
round of optimization. This is continued till we obtained the optimized parameters, reported here, that 
have the lowest objectives with the training and the test sets. The optimized EAM+QEq parameters are 
listed in Tables 2-5.


## Page 12


12 
Table 1. EAM parameters for metal-metal interaction 
 
 
 
 
Table 2. CTIP parameters for the simulated elements 
Element 
qmin 
qmax 
χ (eV) 
J (eV) 
ξ(Å-1) 
Z(e) 
O  
-2.00 
0.00 
5.481730 
15.128200 
2.143957 
0.000000 
Ta  
0.00 
5.00 
0.000000 
10.758300 
1.036140 
1.159850 
 
Table 3. Optimized EAM parameters for pair potentials 
Pair 
re(Å) 
Α 
β 
A (eV) 
B (eV) 
κ 
λ 
O-Ta 
2.088696 
6.295628 
1.864984 
1.301541 
2.475937 
0.488616 
0.262364 
O-O  
3.668766 
5.931086 
4.104248 
0.415946 
0.706278 
0.240129 
0.753456 
 
Table 4. EAM parameters for oxygen electron density function 
fe 
γ 
ν 
1.888839 
2.708917 
0.694904 
 
Table 5. Optimized EAM parameters for oxygen embedding energy spline function 
i 
F0,i(eV) 
F1,i(eV) 
F2,i(eV) 
F3,i(eV) 
ρe,i 
ρmin,i 
ρmax,i 
0 
-1.576011 
-1.757687 
1.212659 
1.394335 
63.631547 
0 
63.631547 
1 
-1.866573 
-1.806293 
0.871914 
0.000000 
74.860644 
63.631547 
∞ 
Metal 
re(Å) 
fe 
ρe 
ρs 
α 
β 
A (eV) 
Ta 
2.860082 
3.086341 
33.787168 
33.787168 
8.489528 
4.527748 
0.611679 
Metal 
B(eV) 
κ 
λ 
Fn0 (eV) 
Fn1 (eV) 
Fn2(eV) 
Fn3 (eV) 
Ta 
1.032101 
0.176977 
0.353954 
-5.103845 
-0.405524 
1.112997 
-3.585325 
Metal 
F0(eV) 
F1(eV) 
F2(eV) 
F3+(eV) 
F3-(eV) 
η(eV) 
Fe(eV) 
Ta 
-5.14 
0.00 
1.640098 
0.221375 
0.221375 
0.848843 
-5.141526


## Page 13


13 
 
ii. Performance of the Newly Developed CTIP parameters 
Next, we assess the accuracy of our newly developed EAM+QEq parameters by comparing our predicted 
properties against the training and test sets. The fitted and test set properties of the three polymorphs are 
compared against experiments and first-principles calculations in Tables 6-10. The monoclinic structure, 
energy and elastic constant components (also see supporting information Fig. SM2) are captured with 
reasonable accuracy, and so are the structures and energies of the hexagonal and orthorhombic 
polymorphs. The energy ordering between the three polymorphs is also accurately computed by the CTIP 
parameters. In Fig. 3 we show the equation of state (energy vs. volume) for all the polymorphs along with 
the corresponding Murnaghan fit [43] used to compute the bulk modulus, using both CTIP and DFT 
calculations. We also report the surface energies of monoclinic Ta2O5 for the (001), (010) and (100) 
surfaces (see Fig. 4 for surface configurations). The predicted surface energies are compared against DFT 
values in Table 9. Finally, we also report bcc Ta surface energies and find excellent agreement between 
the predicted values, first-principles calculations and experiments (see Table 10). 
Table 6. Properties of monoclinic Ta2O5 given by the EAM+QEq (CTIP) interatomic potential parameters 
developed in this work in comparison with experiments and first-principles calculations. 
Monoclinic 
Properties 
Expt. [44] 
CTIP 
DFT-
GGA+U 
DFT-GGA [45] 
a (Å) 
12.79 
12.93 
12.93 
15.07 
b (Å) 
4.85 
4.71 
4.93 
4.93 
c (Å) 
5.53 
5.53 
5.59 
5.60 
α 
90 
90 
90 
90 
β 
104.26 
103.58 
103.24 
123.19 
γ 
90 
90 
90 
90 
Ec (eV/u.f.) 
- 
-64.53 
-64.49 
-68.31 
B (GPa) 
- 
196 
122 
137


## Page 14


14 
C11 (GPa) 
- 
263 
282 
208 
C22 (GPa) 
- 
297 
215 
173 
C33 (GPa) 
- 
230 
239 
272 
C44 (GPa) 
- 
90 
126 
83 
C55 (GPa) 
- 
52 
56 
107 
C66 (GPa) 
- 
32 
57 
68 
C12 (GPa) 
- 
132 
81 
63 
C13 (GPa) 
- 
129 
88 
112 
C15 (GPa) 
- 
-8 
-40 
0 
C23 (GPa) 
- 
152 
103 
114 
C25 (GPa) 
- 
-2 
-22 
0 
C35 (GPa) 
- 
-29 
-25 
0 
C46 (GPa) 
- 
8 
0 
0 
 
Table 7. Properties of δ-hexagonal Ta2O5 given by the EAM+QEq (CTIP) interatomic potential parameters 
developed in this work in comparison with experiments and first-principles calculations. 
Hexagonal 
Properties 
Expt. [46, 47, 48] 
CTIP 
DFT-GGA+U 
DFT [34, 46] 
a (Å) 
7.25 - 7.34 
7.11 
7.33 
7.12 - 7.32 
b (Å) 
7.25 - 7.34 
7.11 
7.33 
7.12 - 7.32 
c (Å) 
3.88 
3.96 
3.89 
3.83 - 3.88 
α 
90 
90 
90 
90 
β 
90 
90 
90 
90 
γ 
120 
120 
120 
120 
Ec (eV/u.f.) 
- 
-63.48 
-62.63 
-59.84, -60.34 
B (GPa) 
- 
268 
217 
- 
 
Table 8. Properties of β-orthorhombic Ta2O5 given by the EAM+QEq (CTIP) interatomic potential 
parameters developed in this work in comparison with experiments and first-principles calculations.


## Page 15


15 
Orthorhombic 
Properties 
Expt. [49, 50] 
CTIP 
DFT-
GGA+U 
DFT [35, 45, 
51, 52] 
a (Å) 
3.68 
3.62 
3.69 
3.55 - 3.75 
b (Å) 
3.90 
3.93 
3.89 
3.75 - 3.89 
c (Å) 
6.23 
6.24 
6.52 
6.53 – 7.9 
Ec (eV/u.f.) 
- 
-62.26 
-62.30 
-66.14 
ΔE – β-δ 
(eV/u.f.) 
- 
1.22 
0.33 
0.4 
B (GPa) 
- 
267 
197 
- 
 
Table 9. Surface energies in J/m2 of monoclinic Ta2O5. 
Surface 
CTIP 
DFT 
(100) 
5.32 
4.92 
(010) 
2.19 
1.06 
(001) 
3.72 
2.09 
 
Table 10. Surface energies in J/m2 of bcc Ta compared against experiments, first-principles and reported MD 
calculations. Though Zhou et al.’s EAM parameters for Ta (used in CTIP) were not explicitly trained against 
the surface energies, they are captured with reasonable accuracy. 
Surface 
CTIP 
EAM [53] 
DFT [45] 
Expt. [54] 
(110) 
1.96 
2.29 
2.34 
2.49 
(100) 
2.29 
2.75 
2.47 
- 
(111) 
2.31 
2.98 
2.70 
- 
 
4. Case study: Oxidation of Ta (110) surface 
We apply this newly developed force field to study the oxidation of a Ta (110) surface in the presence of 
atomic and molecular oxygen. MD simulations are performed up to 200 ps for temperatures ranging from


## Page 16


16 
300-900 K. Structure and stoichiometry information in the metal/oxide/gas interface is extracted from the 
MD simulation and used to gain insights into the evolution and morphology of the growing oxide film.  
Fig. 5 shows the oxidation kinetics curves for various temperatures. As expected, we see that the 
oxygen adsorption increases with temperature and that atomic oxygen is more active than molecular 
oxygen (Fig. 5 a, d). In addition, we observe that the oxide film thickness (see Fig. 5 b, e) reach a limiting 
value of ~0.7-0.9 nm. Similar self-limiting thicknesses have been obtained for the natural oxidation of Zr 
both from MD and experiments [25, 27, 55]. In addition, Mathieu et al. [56] reported natural oxide film 
thicknesses ranging from 0.2 – 5 nm for several metal oxides (Al, Fe, Ni) via Auger Electron 
Spectroscopy (AES) and x-ray photoelectron spectroscopy (XPS). However, experimental reports on self-
limiting thickness of the oxide film during natural oxidation of Ta are scarce. Most experimental work 
deals with anodic oxidation and plasma-enhanced chemical vapor-deposition to deposit films over 100 
nm thick [57, 58]. Available experimental data for natural oxidation have a wide variability in the 
reported film thicknesses – 0.7 nm via AES [56], 1.9 nm via XPS [56], and 3.0 nm via XPS [59]. 
Furthermore, these measurements are for longer oxidation times much beyond 100 s. Such time scales are 
not accessible to the current MD simulations, making direct comparison challeging. With regard to the 
atomic oxidation of Ta, to the best of our knowledge, there is no available experimental data in the 
simulated low-temperature range. However, the enhancement in oxidation kinetics observed in our 
simulations agrees well with previous reports for low-temperature atomic oxidation of Ag and Si (110) 
surfaces [60, 61, 62]. 
Carbera-Mott theory for oxidation kinetics at low temperature in ultrathin films [63, 64, 65] may 
be utilized to analyze the oxidation kinetics curves (Fig. 5) and used to estimate of the activation energy 
barrier for oxidation on Ta surfaces using O and O2. According to this theory, the driving force for 
oxidation is an induced internal electric field that drives the ionic transport, which accelerates the initial 
oxidation but is rapidly attenuated with increasing oxide film thickness. Such a model predicts a 
logarithmic growth rate for metal oxides. The expression for the rate equation is given as follows [25]:


## Page 17


17 
!"
!" = !!!"# −
!!!!
!!"#!!"
!!!
  
 
 
 
 
(3.14) 
where, L is the film thickness, W0 represents the intrinsic barrier for ionic jumps between two positions in 
the oxide film, q is the charge on the ion, 2a is the jump length, E is the electric field, λ is the structure 
term, T is the temperature, kB is the Boltzmann constant, and C is a constant. The solution to the above 
equation yields a direct logarithmic growth law given by [25]:  
! ! =
!!!
!
!" 1 + ! ! !   
 
 
 
 
(3.15) 
where ! ! =
!
!!! !!!"# −
!!!!
!!"#
!!!
 
 
 
 
(3.16) 
We fit the simulated film thickness data to ! ! = !!!ln!(1 + !") to obtain estimates for the structure 
term, ! =
!!!
!  and ! ! = !. The structure term λ/kB varies linearly with temperature if logarithmic 
growth law is valid. We observe the expected linear dependence for the temperature range 300-600 K for 
both natural and atomic oxidation (see Fig. 5 c, f). In addition, we see that atomic oxygen has lower 
values for structure term indicating lower energy barrier or faster kinetics for atomic oxidation than 
natural oxidation. Interestingly, we observe a deviation from the linear dependence in for !!vs. T at 900 K 
(see supporting information Fig. SM3). Such a deviation from logarithmic kinetics of Carbera-Mott 
theory has been observed for the oxidation of Ta above ~320oC [18, 66]. While the exact mechanism of 
high temperature oxidation is not clear from the current MD simulations, it is anticipated to have 
parabolic kinetics [18]. Longer simulation timescales than currently accessible from the current MD 
simulations is necessary to investigate this in detail and is subject of future studies. 
 
Oxide growth in metals can proceed via the following three mechanisms: (a) the metal ions alone 
migrate and the new oxide forms at the oxide/gas interface; (b) oxygen ions alone migrate and the new 
oxide forms at the oxide/metal interface; and (c) both the ions migrate and the new oxide layer can form 
at both interfaces and/or within the existing oxide [57]. It has been experimentally observed that the 
transport numbers for oxygen ions is thrice that of tantalum ions during oxide growth in the metal and 
that the oxide thickens through the formation of new oxide at both interfaces [57]. Hence, the kinetics of


## Page 18


18 
the process is limited by cation transport. An Arrhenius fit to Eqn. 3.16 can be used to estimate the overall 
energy barrier !! −
!
! !"#. We find this to be 0.13 ± 0.02 eV for molecular/natural oxidation and 
0.043 ± 0.015 eV for atomic oxidation, respectively. If the value of the induced internal electric field 
that drives the ionic transport (E) is known, we can get an exact estimate of the intrinsic energy barrier 
W0. This electric field lowers the energy barriers for the outward migration of cations in the developing 
oxide film. The induced internal electric field, E, has been experimentally estimated to be in the range 4-7 
MV/cm for Ta [67]. Other estimates for the Mott potential (VK) for the low temperature oxidation of Ta 
are in the 0.5-0.65 V range at 523 K [64]. For an ~0.8 nm thick oxide film (as obtained in this work at 500 
K), we calculate ! =
!!
!  in the range 6.25-8.13 MV/cm. We use ! = 6.25!MV/cm in our calculations 
here. This is similar to values used by Sankaranarayan et al.’s prior MD studies on oxidation of Zr and Al 
[25, 26, 27]. Using an estimated charge (q) of 4.65 ± 0.18! for the charge of Ta in Ta2O5 and a cation 
jump distance (a) of 3.14 ± 0.07Å for molecular oxidation and 3.13 ± 0.08Å for atomic oxidation 
(estimated from the first peak distance in the Ta-Ta radial distribution function within the oxide film), we 
obtain !! = 0.59 ± 0.05!!" for molecular oxidation and !! = 0.49 ± 0.04!!" for atomic oxidation. 
Experimental estimates for energy barriers for molecular oxidation of Ta for temperatures lower than 
~320oC are 0.54 eV [66], 0.62 eV for polycrystalline samples [68] and 1.2 eV for single crystal Ta (100) 
surface [68]. 
 
In Fig. 6, we show the atomistic representation of the time evolution of the oxidation process at a 
representative temperature of 600 K. We see that the oxide layer is amorphous and that the oxygen 
density on the substrate surface becomes more or less uniform within 200 ps. To further elucidate the 
structural characteristics of the oxide scale, we analyze the oxide structure using partial pair distribution 
functions (PDF) and bond-angle distributions (ADF) by averaging over 20 trajectories between 195 ps 
and 200 ps of the oxidation simulation. Fig. 7(a) and 7(c) show the Ta−O PDF in the oxide scale interior 
at various temperatures for natural and atomic oxidation, respectively. The position of the first peak in 
gTaO(r) gives the Ta−O bond length to be around 2.15 Å at all temperatures and for both molecular and


## Page 19


19 
atomic oxidation. This is consistent with Ta-O distances observed in amorphous Ta2O5 films under typical 
deposition conditions [51]. Fig. 7(b) and 7(d) show O−Ta−O bond-angle distribution in the interior of the 
oxide scale at various temperatures for Ta oxidation using O2 and O, respectively. For all cases, we find 
that the bond-angle distribution is spread over a broad range between 50° and 180° (indicative of the 
amorphous nature of the oxide scale). Additionally, we observe two distinct peaks at 70° and 135° in the 
bond-angle distribution throughout the oxide structure. This is typical of an amorphous and non-
stoichiometric oxide scale [27]. The ADF is relatively unaffected by temperature and atomic/molecular 
nature of the oxidizing species. 
 
We further analyze the time evolution of the oxide film composition (average O/Ta stoichiometry 
ratio) for both natural and atomic oxidation at different temperatures  spanning 300−900 K (Fig. 8 and 
supporting information Fig. SM4). The 2-d color-maps in Fig. 8 have time (in ps) along the horizontal-
axis, the spatial coordinate normal to the metal substrate surface along the vertical-axis, and is colored by 
the O/Ta stoichiometry ratio. We see that the oxide film thickness increases with temperature and that the 
O/Ta ratio (and consequently the charge distribution) shows a gradient with maximum stoichiometry ratio 
at the oxide/gas interface and minimum O/Ta ratio at the oxide/metal interface. Additionally, the O/Ta 
ratio of the self-limiting oxide film increases with temperature (see supporting information Fig. SM4). 
For atomic oxidation, the O/Ta ratio approaches 2.1-2.3 within 200 ps for temperatures from 300-900 K. 
On the other hand, the corresponding O/Ta ratio for molecular oxidation is significantly lower than the 
stoichiometric ratio and varies from approximately 1.48 at 300 K to 2.11 at 900 K (within 200 ps of 
oxidation). This lower O/Ta ratio is attributed to slower oxidation kinetics leading to O-deficient oxide 
films. Additionally, the O/Ta ratio is also lower than 2.5, which is the stoichiometric ratio in crystalline 
tantalum oxide. This further hints at the amorphous nature of the oxide scale. 
5. Conclusions 
We have developed the first variable-charge potential for TaOx material systems and used it to study Ta 
oxidation by both molecular (O2) and atomic (O) oxygen via molecular dynamics simulations. We adopt


## Page 20


20 
the charge-transfer ionic potential (CTIP) formalism to treat charge transfer among atoms and investigate 
the oxidation kinetics during the initial stages of tantalum oxide growth. Oxidation is studied as a function 
of both temperature and the atomic/molecular nature of the oxidizing species. We report intrinsic 
activation barriers of 0.59 eV and 0.49 eV for natural and atomic oxidation, respectively. The lower 
activation energy barrier for atomic oxidation is likely responsible for the observed increase in the oxide 
growth kinetics. We further characterize the structure and morphology of the oxide films formed during 
natural and atomic oxidation of Ta. Structural analysis reveals self-limiting thicknesses in the range of 
~0.7-0.9 nm for the amorphous oxide film obtained after 200 ps of simulation time at various 
temperatures. We also report a gradient in the O/Ta ratio (and consequently the charge distribution) 
through the oxide film, with maximum at the oxide/gas interface and minimum O/Ta ratio at the 
oxide/metal interface. Our findings are in good agreement with previous experiments on low-temperature 
Ta oxidation [56, 66, 68]. Furthermore, this CTIP potential is suitable for investigating the atomistic 
mechanisms responsible for the sub-nanosecond timescale switching behavior of TaOx memristors, and 
other transport phenomena at Ta/TaOx interfaces under external stimuli. 
 
Acknowledgement 
This research used resources of the National Energy Research Scientific Computing Center, a DOE 
Office of Science User Facility supported by the Office of Science of the U.S. Department of Energy 
under Contract No. DE-AC02-05CH11231. Use of the Center for Nanoscale Materials was supported by 
the U. S. Department of Energy, Office of Science, Office of Basic Energy Sciences, under Contract No. 
DE-AC02-06CH11357.


## Page 21


21 
Supporting Information 
Additional data comparing 1,2) equations of state from DFT vs. MD, 3) oxidation kinetic curve, 4) 
oxygen stoichiometry variation as a function of temperature, 5) DFT k-point convergence for all 
polymorphs, and 6) pseudo-code for the genetic algorithm employed in this work.


## Page 22


22 
 
Figure 1: (a) Schematic representation of the two-stage evolutionary optimization strategy employed here 
to parameterize the charge transfer interatomic potential for tantalum oxide. The structures, cohesive 
energies and energetic ordering of three polymorphs of Ta2O5, namely, (b) monoclinic, (c) hexagonal and 
(d) orthorhombic are included in the fit. (e) Schematic representation of the optimization for a sample 2-
dimensional problem. The optimized parameters obtained will depend heavily on the initial guess as the 
objective settles into an appropriate local minimum. An evolutionary algorithm/approach provide a route 
for a more efficient sampling of a multidimensional parameter space.


## Page 23


23 
 
 
Figure 2: Schematic showing the simulation set-up for the oxidation case study: unit cell of substrate and 
the vacuum slabs surrounding it. Note that the vacuum-facing Ta surfaces are (110).


## Page 24


24 
 
Figure 3: Comparison of the equation of state (EOS) near equilibrium predicted by our CTIP-EAM 
model with our DFT calculations. The equations of state for (a) monoclinic, (b) hexagonal and (c) 
orthorhombic Ta2O5 calculated using the EAM+Qeq parameters developed in this study (solid blue 
squares) and DFT calculations (solid red circles). The solid lines correspond to the Murnaghan fit. The 
energies are relative to the cohesive energy of the crystal at equilibrium (E0) as evaluated by the 
corresponding level of theory. The crystal volumes are normalized by the equilibrium value in the 
framework of the corresponding level of theory.


## Page 25


25 
 
Figure 4: Surface configurations of monoclinic Ta2O5 used in our test calculations. For clarity, the 
surface unit cell (whose edges are shown in black) is repeated as appropriate along the principal directions 
in the plane of the surface. The (001) and (100) surfaces are O-terminated, while the (010) surface is Ta-
terminated. Ta atoms are shown by green spheres and oxygen by red.


## Page 26


26 
 
Figure 5: Oxidation kinetics curves of Ta(110) as a function of temperature. (a), (b) and (c) show the 
number of adsorbed O atoms, oxide film thickness and the structure term obtained by assuming 
logarithmic kinetics, respectively, for molecular/natural oxidation. (d), (e) and (f) are the corresponding 
plots for atomic oxidation.


## Page 27


27 
 
Figure 6: Atomistic representation of the time evolution of the molecular oxidation process at 
representative temperature of 600 K. Top panel: Side view; Bottom panel: Top view of the Ta (110) 
surface. Ta atoms are shown by green spheres and oxygen by red. The oxygen molecules in the gaseous 
phase have been removed from the depiction above.


## Page 28


28 
 
Figure 7: Structural evolution of the oxide films as a function of temperature. (a) Ta-O radial distribution 
function (RDF), and (b) O-Ta-O bond angle distribution (ADF) in the grown oxide film for 
molecular/natural oxidation. (c) Ta-O RDF, and (d) O-Ta-O ADF for atomic oxidation. The distributions 
are shifted upwards for each temperature for better visualization.


## Page 29


29 
 
Figure 8: Evolution of O/Ta stoichiometry in the growing oxide film as a function of oxidation time for 
the oxidation of the bare Ta substrate at various temperatures. The 2-d color-maps have time (in ps) along 
the horizontal-axis, the spatial coordinate normal to the metal substrate surface along the vertical-axis, 
and is colored by the O/Ta stoichiometry ratio. Panels (a) to (e) are for molecular/natural oxidation with 
increasing temperature (300, 400, 500, 600, 900 K). Panels (f) to (j) are corresponding plots for atomic 
oxidation. The spatial bin size (vertical axis) is ~2.4 Å; the horizontal stripes are, thus, renderings of the 
bin boundaries. The gas region (identified by absence of Ta atoms) is colored maroon.


## Page 30


30 
 
REFERENCES 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[1] Y. Zhao, R. Wang, Z. Han, C. Li, Y. Wang, B. Chi, J. Li, X. Wang, “Electrooxidation Of Methanol 
And Ethanol In Acidic Medium Using A Platinum Electrode Modified With Lanthanum-Doped Tantalum 
Oxide Film”, Electrochim. Acta 151, 544-551 (2015). 
[2] Y. Takahara, J. N. Kondo, T. Takata, D. Lu, K. Domen, “Mesoporous Tantalum Oxide: 1. 
Characterization and Photocatalytic Activity for the Overall Water Decomposition”, Chem. Mater. 13 (4), 
1194-1199 (2001). 
[3] G. Xu, X. Shen, Y. Hu, P. Ma, K. Cai, “Fabrication Of Tantalum Oxide Layers Onto Titanium 
Substrates For Improved Corrosion Resistance And Cytocompatibility”, Surf. Coat. Technol. 272, 58-65 
(2015).!
[4] S. Kumar, C. E. Graves, J. P. Strachan, E. M. Grafals, A. L. D. Kilcoyne, T. Tyliszczak, J. N. Weker, 
Y. Nishi, R. S. Williams, “Direct Observation of Localized Radial Oxygen Migration in Functioning 
Tantalum Oxide Memristors”, Adv. Mater. 28, 2772–2776 (2016). 
[5] A. Robin, J. L. Rosa, “Corrosion Behavior Of Niobium, Tantalum And Their Alloys In Hot 
Hydrochloric And Phosphoric Acid Solutions”, Int. J. Refract. Met. Hard Mater. 18 (1), 13-21 (2000). 
[6] S. Rathnayake, J. Mongan, A. S. Torres, R. Colborn, D. -W. Gao, B. M. Yeh, Y. Fu, “In vivo 
Comparison Of Tantalum, Tungsten, And Bismuth Enteric Contrast Agents To Complement Intravenous 
Iodine For Double-Contrast Dual-Energy CT Of The Bowel”, Contrast Media Mol. Imaging 11, 254–261 
(2016).!
[7] S. Senderoff, “Electrodeposition of Refractory Metals”, Metall. Rev. 11 (1), 97-112 (1966). 
[8] R. W. Buckman, “New Applications For Tantalum And Tantalum Alloys”, JOM 52 (3), 40-41 (2000). 
[9] A. Y. Mao, K. -A. Son, D.A. Hess, L.A. Brown, J. M. White, D. L. Kwong, D. A. Roberts, R. N. 
Vrtis, “Annealing Ultra Thin Ta2O5 Films Deposited On Bare And Nitrogen Passivated Si(100)”, Thin 
Solid Films 349(1–2), 230-237 (1999).


## Page 31


31 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[10] R. Vladoiu, V, Ciupina, A. Mandes, V. Dinca, M. Prodan, G. Musa, “Growth And Characteristics Of 
Tantalum Oxide Thin Films Deposited Using Thermionic Vacuum Arc Technology”, J. Appl. Phys. 108, 
093301 (2010). 
[11] T. Doumuki, H. Tamada, M. Saitoh, “Highly Efficient CherenkovType Second Harmonic 
Generation In A Ta2O5/Ktiopo4 Waveguide”, Appl. Phys. Lett. 64, 3533-3535 (1994). 
[12] K. Koc, F. Z. Tepehan, G. G. Tepehan, “Antireflecting Coating From Ta2O5 And Sio2 Multilayer 
Films”, J. Mater. Sci. 40, 1363-1366 (2005).  
[13] F. Rubio, J. Denis, J.M. Albella, J.M. Martinez-Duart, “Sputtered Ta2O5 Antireflection Coatings For 
Silicon Solar Cells”, Thin Solid Films 90 (4), 405-408 (1982). 
[14] E. Pehlivan, K. Koc, F. Z. Tepehan, G. G. Tepehan, “Structural, Optical And Electrochromic 
Properties Of Tantalum Pentoxide-Doped Niobium Pentoxide Thin Films”, J. Sol-Gel Sci. Technol. 77, 
172-178 (2016). 
[15] P. R. Mickel, A. J. Lohn, B. J. Choi, J. J. Yang, M. –X. Zhang, M. J. Marinella, C. D. James, R. S. 
Williams, “A Physical Model Of Switching Dynamics In Tantalum Oxide Memristive Devices”, Appl. 
Phys. Lett. 102, 223502 (2013). 
[16] F.G. Sen, Y. Qi, A.C.T. Van Duin, A.T. Alpas, "Oxidation-assisted Ductility in Aluminum 
Nanowires", Nat. Commun. 5, 3959 (2014).  
[17] F.G. Sen, Y. Qi, A.C.T. Van Duin, A.T. Alpas, "Oxidation Induced Softening in Al Nanowires", 
Appl. Phys. Lett. 102, 051912 (2013).  
[18] R. Chandrasekharan, I. Park, R. I. Masel, M. A. Shannon, “Thermal Oxidation Of Tantalum Films At 
Various Oxidation States From 300 To 700°C”, J. Appl. Phys. 98, 114908 (2005). 
[19] S. Ruffell, P. Kurunczi, J. England, Y. Erokhin, J. Hautala, R.G. Elliman, “Formation And 
Characterization Of Ta2O5/Taox Films Formed By O Ion Implantation”, Nucl. Instrum. Methods Phys. 
Res., Sect. B 307, 491-494 (2013). 
[20] A. Eichler, F. Mittendorfer, J. Hafner, “Precursor-Mediated Adsorption Of Oxygen On The (111) 
Surfaces Of Platinum-Group Metals”, Phys. Rev. B 62, 4744-4755 (2000). 
[21] A. Ulvestad, K. Sasikumar, J. W. Kim, R. Harder, E. Maxey, J. N. Clark, B. Narayanan, S. A. 
Deshmukh, N. Ferrier, P. Mulvaney, S. K. R. S. Sankaranarayanan, O. G. Shpyrko, “In-situ 3D Imaging 
of Catalysis Induced Strain in Gold Nanoparticles”, J. Phys. Chem. Lett. 7, 3008-3013 (2016).


## Page 32


32 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[22] J. P. Trinastic, R. Hamdan, Y. Wu, L. Zhang, H. –P. Cheng, “Unified Interatomic Potential And 
Energy Barrier Distributions For Amorphous Oxides”, J. Chem. Phys. 139, 154506 (2013). 
[23] X. W. Zhou, H. N. G. Wadley, “A Charge Transfer Ionic-Embedded Atom Method Potential For The 
O-Al-Ni-Co-Fe System”, J. Phys.: Condens. Matter 17, 3619-3635 (2005). 
[24] X. W. Zhou, H. N. G. Wadley, J. –S. Filhol, M. N. Neurock, “Modified Charge Transfer-Embedded 
Atom Method Potential For Metal/Metal Oxide Systems”, Phys. Rev. B 69, 035402 (2004). 
[25] S. K. R. S. Sankaranarayanan, S. Ramanathan, “On the Low-Temperature Oxidation and Ultrathin 
Oxide Growth on Zirconium in the Presence of Atomic Oxygen: A Modeling Study”, J. Phys. Chem. 
C 112 (46), 17877–17882 (2008). 
[26] S. K. R. S. Sankaranarayanan, S. Ramanathan, “Molecular Dynamics Simulation Study Of 
Nanoscale Passive Oxide Growth On Ni-Al Alloy Surfaces At Low Temperatures”, Phys. Rev. B 78, 
085420 (2008). 
[27] S. K. R. S. Sankaranarayanan, E. Kaxiras, S. Ramanathan, “Electric Field Tuning Of Oxygen 
Stoichiometry At Oxide Surfaces: Molecular Dynamics Simulations Studies Of Zirconia”, Energy 
Environ. Sci. 2, 1196–1204 (2009). 
[28] S. Alavi, J. W. Mintmire, D. L. Thompson, “Molecular Dynamics Simulations of the Oxidation of 
Aluminum Nanoparticles”, J. Phys. Chem. B 109 (1), 209–214 (2005). 
[29] B. Narayanan, K. Sasikumar, Z. –G. Mei, A. Kinaci, F. G. Sen, M. J. Davis, S. K. Gray, M. K. Y. 
Chan, S. K. R. S. Sankaranarayanan, “Development of a Modified Embedded Atom Force Field for 
Zirconium Nitride Using Multi-Objective Evolutionary Optimization”, J. Phys. Chem. C 120 (31), 17475-
17483 (2016). 
[30] M. J. Cherukara, B. Narayanan, A. Kinaci, K. Sasikumar, S. K. Gray, M. K. Y. Chan, S. K. R. S. 
Sankaranarayanan, “Ab Initio-Based Bond Order Potential to Investigate Low Thermal Conductivity of 
Stanene Nanostructures”, J. Phys. Chem. Lett. 7 (19), 3752-3759 (2016). 
[31] F. G. Sen, A. Kinaci, B. Narayanan, S. K. Gray, M. J. Davis, S. K. R. S. Sankaranarayanan, M. K. Y. 
Chan, “Towards Accurate Prediction Of Catalytic Activity In Iro2 Nanoclusters Via First Principles-
Based Variable Charge Force Field”, J. Mater. Chem. A 3, 18970-18982 (2015). 
[32] B. Narayanan, A. Kinaci, F. G. Sen, M. J. Davis, S. K. Gray, M. K. Y. Chan, S. K. R. S. 
Sankaranarayanan, “Describing the Diverse Geometries of Gold from Nanoclusters to Bulk - A First-
Principles-Based Hybrid Bond-Order Potential”, J. Phys. Chem. C 120, 13787−13800 (2016).


## Page 33


33 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[33] F. H. Streitz, J. W. Mintmire, “Electrostatic Potentials For Metal-Oxide Surfaces And Interfaces”, 
Phys. Rev. B 50 (16), 11996-12003 (1994). 
[34] M. V. Ivanov, T. V. Perevalov, V. S. Aliev, V. A. Gritsenko, V. V. Kaichev, “Electronic Structure 
Of Δ-Ta2O5 With Oxygen Vacancy: Ab Initio Calculations And Comparison With Experiments”, J. Appl. 
Phys. 110, 024115 (2011). 
[35] R. Nashed, W. M. I. Hassan, Y. Ismail, N. K. Allam, “Unravelling The Interplay Of Crystal 
Structure And Electronic Band Structure Of Tantalum Oxide (Ta2O5)”, Phys. Chem. Chem. Phys. 15, 
1352-1357 (2013). 
[36] M. Cococcioni, S. de Gironcoli, “Linear Response Approach To The Calculation Of The Effective 
Interaction Parameters In The LDA+U Method”, Phys. Rev. B 71, 035105 (2005). 
[37] L. Wang, T. Maxisch, G. Ceder, “Oxidation Energies Of Transition Metal Oxides Within The 
GGA+U Framework”, Phys. Rev. B 73, 195107 (2006). 
[38] X. W. Zhou, R. A. Johnson, H. N. G. Wadley, “Misfit-Energy-Increasing Dislocations In Vapor-
Deposited Cofeõnife Multilayers”, Phys. Rev. B 69, 144113 (2004). 
[39]!K.!Sastry, D. E. Goldberg, G. Kendall, “Genetic Algorithms. In Search Methodologies: Introductory 
Tutorials in Optimization and Decision Support Techniques”, Burke, E. K.; Kendall, G., Eds.; Springer: 
Berlin, 2005; Chapter 4, pp. 97-125.!
[40] S. Plimpton, “Fast Parallel Algorithms for Short-Range Molecular Dynamics”, J. Comp. Phys. 117, 
1-19 (1995). 
[41] D. J. Evans, B. L. Holian, “The Nose–Hoover thermostat”, J. Chem. Phys. 83, 4069-4074 (1985). 
[42] G. J. Martyna, D. J. Tobias, M L. Klein, “Constant Pressure Molecular Dynamics Algorithms”, J. 
Chem. Phys. 101, 4177-4189 (1994). 
[43] B. Narayanan, I. E. Reimanis, E. R. Fuller Jr., C. V. Ciobanu, “Elastic Constants Of Β-Eucryptite 
Studied By Density Functional Theory”, Phys. Rev. B 81, 104106 (2010). 
[44] I. P. Zibrov, V. P. Filonenko, M. Sundberg, P. –E. Werner, “Structures And Phase Transitions Of B-
Ta2O5 And Z-Ta2O5: Two High-Pressure Forms Of Ta2O5”, Acta Cryst. B 56, 659-665 (2000). 
[45] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, 
G. Ceder, K. Persson, “The Materials Project: A Materials Genome Approach To Accelerating Materials 
Innovation”, APL Mater. 1, 011002 (2013).


## Page 34


34 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[ 46 ] A. Fukumoto, K. Miwa, “Prediction Of Hexagonal Ta2O5 Structure By First-Principles 
Calculations”, Phys. Rev. B 55 (17), 11155-11160 (1997). 
[47] N. Terao, “Structure Of Tantalum Oxides”, Jpn. J. Appl. Phys. 6, 21-34 (1967). 
[48] V. A. Shvets, V. Sh. Aliev, D. V. Gritsenko, S. S. Shaimeev, E. V. Fedosenko, S. V. Rykhlitski, V. 
V. Atuchin, V. A. Gritsenko, V. M. Tapilin, H. Wong, “Electronic Structure And Charge Transport 
Properties Of Amorphous Ta2O5 Films”, J. Non-Cryst. Solids 354 (26), 3025-3033 (2008). 
[49] L. A. Aleshina, S. V. Loginova, “Rietveld Analysis of X-ray Diffraction Pattern from β-Ta2O5 
Oxide”, Crystallogr. Rep. 47 (3) 415–419 (2002). 
[50] G. Bergerhoff, R. Hundt, R. Sievers, I. D. Brown, “The Inorganic Crystal Structure Data Base”, J. 
Chem. Inf. Comput. Sci. 2, 66-69 (1983). 
[51] R. Ramprasad, “First Principles Study Of Oxygen Vacancy Defects In Tantalum Pentoxide”, J. Appl. 
Phys. 94, 5609-5612 (2003).  
[52] S. –H. Lee, J. Kim, S. –J. Kim, S. Kim, G. –S. Park, “Hidden Structural Order in Orthorhombic 
Ta2O5”, Phys. Rev. Lett. 110, 235502 (2013). 
[53] Website: https://sites.google.com/site/eampotentials/Ta [Last accessed: Nov 7th 2016]. 
[54] W.R. Tyson, W.A. Miller, “Surface Free Energies Of Solid Metals: Estimation From Liquid Surface 
Tension Measurements”, Surf. Sci. 62 (1), Pages 267-276 (1977). 
[55] L. Jeurgens, A. Lyapin, E. Mittemeijer, “The Initial Oxidation Of Zirconium Oxide – Film 
Microstructure And Growth Mechanism”, Surf. Interface Anal. 38, 727-730 (2006). 
[56] H. J. Mathieu, M. Datta, D. Landolt, “Thickness Of Natural Oxide Films Determined By AES And 
XPS With/Without Sputtering”, J. Vac. Sci. Technol., A 3, 331-335 (1985). 
[57] J. P. S. Pringle, “Transport Numbers Of Metal And Oxygen During Anodic Oxidation Of Tantalum”, 
J. Electrochem. Soc.: Solid State Sci. Tech. 120 (3) 398-407 (1973). 
[58] M. Seman, J. J. Robbins, “Self-Limiting Growth Of Tantalum Oxide Thin Films By Pulsed Plasma-
Enhanced Chemical Vapor Deposition”, Appl. Phys. Lett. 90, 131504 (2007). 
[59] S. Lecuyer, A. Quemerais, G. Jezequel, “Composition Of Natural Oxide Films On Polycrystalline 
Tantalum Using XPS Electron Take-Off Angle Experiments”, Surf. Interface Anal. 18, 257-261 (1992). 
[60] M. Kisa, L. Li, J. Yang, T. K. Minton, W. G. Stratton, P. Voyles, X. Chen, K. van Benthem, S. J. 
Pennycook, “Homogeneous Silica Formed by the Oxidation of Si(100) in Hyperthermal Atomic


## Page 35


35 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Oxygen”, J. Spacecr. Rockets 43, 431-435 (2006).  
[61] M. Kisa, T. K. Minton, J. C. Yang, “Structural Comparisons Of Siox And Si|Siox Formed By The 
Exposure Of Silicon (100) To Molecular Oxygen And To Hyperthermal Atomic Oxygen”, J. Appl. Phys. 
97, 023520 (2005). 
[62] M. L. Zheludkevich, A. G. Gusakov, A. G. Voropaev, A. A. Vecher, E. N. Kozyrski, S. A. 
Raspopov, “Oxidation Of Silver By Atomic Oxygen”, Oxid. Met. 61, 39-48 (2004). 
[63] N. Cabrera, N. F. Mott. "Theory Of Oxidation Of Metals", Rep. Prog. Phys. 12, 163-184 (1948). 
[64] A. T. Fromhold, Jr., E. L. Cook, “Kinetics of Oxide Film Growth on Metal Crystals: Thermal 
Electron Emission and Ionic Diffusion”, Phys. Rev. 163 (3), 650-664 (1967). 
[65] S. K. R. S. Sankaranarayanan, S. Ramanathan, “Electric Field Control Of Surface Oxygen Dynamics 
And Its Effect On The Atomic Scale Structure And Morphology Of A Growing Ultrathin Oxide Film”, J. 
Phys. Chem. C 114, 6631-6639 (2010). 
[66] J. T. Waber, G. E. Sturdy, E. M. Wise, C. R. Tipton Jr., “A Spectrophotometric Study Of The 
Oxidation Of Tantalum”, J. Electrochem. Soc. 99 (3), 121-129 (1952). 
[67] L. Young, “Steady State Kinetics Of Formation Of Anodic Oxide Films On Tantalum In Sulphuric 
Acid”, Proc. R. Soc. London, Ser. A 258 (1295), 496-515 (1960). 
[68] K. Wang, Z. Liu, T. H. Cruz, M. Salmeron, H. Liang, “In Situ Spectroscopic Observation of 
Activation and Transformation of Tantalum Suboxides”, J. Phys. Chem. A 114, 2489–2497 (2010). 
 
 
 
 
Table of Contents Graphic

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]