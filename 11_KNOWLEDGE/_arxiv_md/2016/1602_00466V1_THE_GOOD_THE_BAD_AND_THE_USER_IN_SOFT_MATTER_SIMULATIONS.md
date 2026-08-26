---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1602.00466v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1602.00466v1_The_good__the_bad_and_the_user_in_soft_matter_simulations

> Source: 1602.00466v1_The_good__the_bad_and_the_user_in_soft_matter_simulations.pdf

> Pages: 36

---


## Page 1


The good, the bad and the user in soft matter simulations 
Jirasak Wong-ekkabut1,* and Mikko Karttunen2,* 
1Department of Physics, Faculty of Science, Kasetsart University, Bangkok, 10900, Thailand 
2Department of Mathematics and Computer Science & Institute for Complex Molecular 
Systems, Eindhoven University of Technology, MetaForum, 5600 MB Eindhoven, the 
Netherlands 
*Corresponding Authors 
E-mail address J.W.: jirasak.w@ku.ac.th, and M.K.: mkarttu@tue.nl 
Contents 
1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 
2. Case study 1: Unphysical flow of water inside a carbon nanotube. . . . . . . . . . . 4 
3. Case study 2: Unphysical flow inside a protein nanochannel. . . . . . . . . . . . . . . 7 
4. Long-range electrostatics ….. . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . .. 9 
5. The need to go beyond the Lorentz-Berthelot rules . . . . . . . . . . . . . . . . . .. . . . 12 
6. Force fields: A brief summary ……………………. . . . . . . . . . . . . . . . . . ..….14 
7. Thermostats – necessary evil. . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . .14 
8. Barostats: How about compressibility? . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . .17 
9. Epilogue: User - the most significant error source. . . . . . . . . . . . . . . . . . . . . . . 18 
Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .. . .19 
References . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 
Abstract 
Molecular dynamics (MD) simulations have become popular in materials 
science, biochemistry, biophysics and several other fields. Improvements in 
computational resources, in quality of force field parameters and algorithms have 
yielded significant improvements in performance and reliability. On the other hand, 
no method of research is error free. In this review, we discuss a few examples of 
errors and artifacts due to various sources and discuss how to avoid them. Besides 
bringing attention to artifacts and proper practices in simulations, we also aim to 
provide the reader with a starting point to explore these issues further. In particular, 
we hope that the discussion encourages researchers to check software, parameters, 
protocols and, most importantly, their own practices in order to minimize the 
possibility of errors. The focus here is on practical issues.


## Page 2


1. Introduction 
Computer simulations have become an extremely powerful tool and have 
firmly established their role as the third paradigm of research alongside theory and 
experiments as demonstrated by the 2013 Nobel Prize in Chemistry to Martin 
Karplus, Michael Levitt and Arieh Warshel "for the development of multiscale models 
for complex chemical systems". Simulations have predictive power. For example, they 
have predicted that proteins are dynamic entities, that their dynamics is essential for 
their biological functions[1], that highly hydrophobic carbon nanotubes can conduct 
water[2], and elucidated the functioning principles of aquaporins[3, 4]. In our own 
computational research, we have, e.g., resolved the decades old problem of lipid 
diffusion modes[5]. Recent reviews discussing the progress and success of 
simulations are provided, for example, by Schulten et al.[6], Dror et al.[7], and 
Karplus and McCammon[8]. In this review, we focus on classical level simulations 
and will not address ab initio simulations. A recent review discussing various aspects 
of ab initio simulations is provided by Kirchner et al.[9]. Although lattice Boltzmann 
simulations can contain embedded particles at the classical MD level, we will not 
discuss them or hybrid simulations. Instead, we refer the reader to Silva and 
Semiao[10] who discuss the lattice structure and truncation errors and Ollila et al.[11] 
who provide a method to properly include thermal fluctuations and thermostatting in 
lattice Boltzmann. 
In addition to being predictive, a less appreciated important fact about 
simulations is they can show the kind of disturbances experimental probes, for 
example fluorescent probes or local heating by laser, can cause[12, 13]. Another 
under-appreciated fact is that several experimental methods need at least a semi-
computational molecular model for interpretation of the experimental data. This is 
particularly the case with NMR (Nuclear Magnetic Resonance) and various scattering 
methods. Typically, such models are not true simulations but rather just models for 
interpretation of experimental data. Proper simulations, as already stated by Allen and 
Tildesley in their classic book “Computer Simulations of Liquids”[14], have the 
ability to be predictive and to provide exact results for a given model within 
algorithmic and numerical accuracy. This is indeed remarkable! No other method has 
the latter ability: No mean-field approximations are necessary and the disturbances of 
external probes are absent. Yet at the same time, all the positions and velocities of all


## Page 3


atoms are known and can be post-analyzed in any way desirable. Relations between 
experiments, computation and theory are illustrated in Figure 1. 
 
Figure 1. Computer simulations are firmly established as the third paradigm of research 
alongside with experiments and simulations. Figure (slightly modified) by courtesy and 
permission from Markus Miettinen[15]. 
 
The above does not mean that simulations are error free. As with all methods 
of research, there are errors, inherent, induced, accidental and due to ignorance. In 
this review, we will focus on practical issues in simulations rather than on a rigorous 
analysis of algorithms, numerical errors, errors due to finite precision and errors in 
data analysis. For integration algorithms, we refer to the book by Tuckerman[16]. He 
discusses a large number of integration methods and their derivations as well as 
constraint algorithms. Other recent discussions on integrators and algorithms can be 
found in Refs. [17-19]. For error analysis see, e.g., the article by Bond and 
Leimkuhler[20]. Sampling issues in MD have recently been reviewed by Grossfield 
and Zuckerman[21] and they are discussed in this issue in the article of Pomes et


## Page 4


al.[22].  In addition to algorithms and protocols, system preparation should be paid 
due attention as has been pointed out by Manna et al.[23]. As a side note, in the 
context of numerical analysis, it has been pointed out that it is not clear at all why MD 
even works! [24] 
Accidental errors can be loosely classified as programming errors and user 
errors including bad choices of simulations parameters. Even the best programmer 
makes about 15-50 errors per 1000 lines[25]. The advantage of open source software 
is, however, that errors are found very quickly. Indeed, the current authors have found 
and reported errors in open source software. The most dangerous category is errors 
due to ignorance, in other words, user error. Every error is ultimately a user error: The 
user has an obligation to check, verify and correct. 
In the following, we discuss a few cases of various known errors. We hope 
this discussion encourages researchers to check software, parameters, protocols and, 
most importantly, their own practices. Using “the standard protocol” without having 
first-hand knowledge is very irresponsible. It is impossible to avoid all errors but the 
possibility of errors should always be minimized.  
Before embarking on a more in-depth discussion, let us mention a couple well-
known cases. One of the first ones that got major attention were the hidden errors in 
random number generation[26, 27]. This lead to re-evaluation of pseudo-random 
number generation algorithms and the development of more rigorous algorithms and 
testing protocols. Another famous case, is the subtle programming error that lead to a 
retraction of several protein structure prediction papers in the early 2000’s[28]. This is 
significant because rather than blaming the programmer, one should always look at 
fundamental properties: In this case the protein structures predicted by the analysis 
code gave the wrong handedness (amino acids are left-handed, see e.g. Novotny and 
Kleywegt[29]). Despite this major issue, it took time to recognize the problem and the 
papers passed peer review in the so-called flagship journals and, most likely, 
influenced grant decisions concerning other researchers whose results did not agree 
with the faulty ones.  
The rest of this paper is organized as follows: Next, we discuss two Case 
Studies based on our own research. After that, we discuss issues related to 
thermostats, Lorentz-Berthelot rules, electrostatics and some other matters in more 
detail.


## Page 5


2. Case study I: Unphysical flow of water inside a carbon nanotube  
As our first Case Study, we discuss the behavior of water inside a carbon 
nanotube (CNT). The ability of water to enter the highly hydrophobic CNTs and the 
extremely rapid motions of water molecules inside a CNT were originally predicted 
by simulations[2] and  later confirmed by both experiments[30, 31] and follow-up 
simulations[32-39].  
Due to CNTs’ high hydrophobicity and the consequent near frictionless 
transport of ‘water, CNTs have emerged as promising candidates, e.g., for filtration 
applications[31, 33, 40]. As a consequence, many techniques to control the rate and 
direction of flow inside a CNT have been suggested[40-43]. Significant controversies, 
however, remain[32, 34, 40, 44-47]. This is what we will discuss next.  
A pristine CNT is charge-neutral. Recently, MD simulations reported by Gong 
et al.[40] used charge-decorated CNTs to show that charge-induced ordering of water 
leads to spontaneous and continuous unidirectional flow through a carbon nanotube 
(CNT), Figure 2. They accredited this observation to the three discrete stationary 
electric charges placed asymmetrically along the exterior of the CNT. They chose this 
charge distribution such as to mimic the electric field inside an aquaporin protein[3] 
and proposed the observed spontaneous flow as a basis for designing novel 
spontaneously operating molecular pumps[40, 48].


## Page 6


Figure 2. A carbon nanotube connecting two water reservoirs (shown in red and white) 
with three static charges (yellow spheres) placed beside the nanotube to mimic the 
placement of charged amino acids inside aquaporin. The nanotube is 2.3 nm long and 
the charges of +e, +e/2 and +e/2 are placed 0.37 nm, 1.09 nm and 1.21 nm from the 
bottom of the nanotube, respectively. The overall system is charge neutral. Fully 
periodic boundary conditions. 
 
2.1. Three critical issues to prevent artificial flow: 
Such a continuous flow without supplied energy is, however, a manifestation 
of perpetual motion and violation of the second law of thermodynamics. A simple 
gedanken experiment shows the impossibility of spontaneous unidirectional flux: If 
the observed flux was real, it would allow propelling a CNT in water without 
supplying any external energy[49]. A downward momentum of the flux would be 
compensated by an upward motion of the CNT. Gong et al. claimed that the energy 
required to produce the flow comes from the constraints imposed on the charges[40]. 
This is not the case[44]. Instead, the observed flow is a result of improper choice of 
simulation parameters and protocols: 1) Improper use of thermostatting, 2) careless 
application of a standard trick called neighbor list update frequency and, most of all,  
3) incorrect use of charge groups[44]. In brief, incorrect use of charge groups caused 
a mismatch between the interactions of the three imposed charges and water 
molecules in the CNT. Moreover, other sources of simulation artifacts, improper use 
of thermostatting and neighbor list update frequency, can also lead to an artificial 
temperature gradient build-up within the CNT and thus cause an unphysical flow. 
With the physically correct flat temperature profile the artificial flow ceases. In 
addition to our studies[44], these findings have been confirmed by another 
independent study[45]. A more detailed discussion follows in later sections. 
 
2.2 The effect of Lennard-Jones cutoff: 
 A net flux of water has also been observed in an uncharged CNT under an 
applied uniform electric field[50]. In this case, artifacts related to the treatment of the 
long-range part of the van der Waals interactions have been reported[51, 52]. In 
particular, Bonthuis et al.[45] simulated CNTs with different Lennard-Jones (LJ) 
cutoff lengths and two different truncation schemes: 1) simple cutoff, which sets the


## Page 7


force to zero and the LJ potential to a small constant value beyond a cutoff distance 
(rc). This results in a discontinuity at r = rc. 2) A shifted cutoff, which makes the force 
to decay smoothly to zero by adding a nonlinear function[53]. The results of Bonthuis 
et al. show that with a simple cutoff the magnitude of water flux decreases as rc 
increases and approaches zero at the limit rc→∞. With the shifted cutoff, the flux 
disappears for all rc.  
The above results cast doubt over the correctness of the implementation of the 
simple LJ cutoff in the GROMACS package[45, 51, 54]. Milicevic constructed a 
minimal model to examine the sensitivity of the simple cutoff scheme to the choice of 
rc[52]. MD simulations of an uncharged spherical LJ particle in water, both in the 
presence and absence of an external electric field, were performed using GROMACS. 
A non-zero van der Waals force on the LJ particle under an external electric field was 
observed with the cutoff while the force vanished with the shift and switch treatment. 
The average forces were about −6.6 pN in simulations with the standard setup in all 
studied Gromacs versions of 3.3.3, 4.5.5, and 4.6.4. The authors concluded the 
software does not have errors and the observed artifacts are due to the cutoff. This 
study further suggested that the non-zero force was generated by water molecules 
belonging to the first two hydration shells. Although, the result is sufficient to 
conclude that a non-zero force is produced by simple truncation of vdW forces, 
understanding of water’s first two hydration shells causing the non-zero forces has not 
been achieved [52]. 
One can also speculate that such effects might be due to integrator algorithms. 
Although we are not aware of systematic studies addressing the issue in this context, 
Toxvaerd and Dyre[55] studied cutoff and force shifting in Lennard-Jones systems 
and concluded that shifting the forces smoothly to zero is important. This is in line 
with Bonthuis et al.[45, 51] In addition, in a follow-up paper Toxvaerd used the 
smoothly shifted forces in his studies of stability of MD simulations and came to the 
conclusion that with normal time steps, the standard Verlet algorithm is indeed 
excellent.


## Page 8


3. Case study II: Unphysical flow inside a protein nanochannel  
 
 
Figure 3. Net flux of water molecules (n(t)) permeating from the cap to the stem 
as a function of time. The blue arrow indicates the direction of the net flow. Simulation 
parameters for each system are provided in the legend. Charge group (CG) and atomic 
group (atom)[53] were used as a basis to compute the neighboring cut-off. For charge 
groups, the default values of the Gromos 53A5 force field[56] were used. Thermostats: 
Berendsen weak coupling thermostat (BT)[57] and the velocity-rescale (VR) thermostat 
[58, 59]. Long-range electrostatic interactions: reaction field (RF)[60] and Particle Mesh 
Ewald (PME)[61, 62]. The neighbor list update frequency (NLUF) was varied between 1 
and 10 time steps[53]. Inset: A snapshot from a simulation. Protein (yellow ribbon) is 
embedded in a palmitoyloleoylphosphatidylcholine (POPC) lipid bilayer (green 
spheres). The system was hydrated by simple point charge (SPC) water molecules[63] 
(red spheres) with a density of about 1000 kg/m3. Periodic boundary conditions were 
applied. 
 
Artificial unidirectional flow also appears in membrane embedded protein 
systems when the simulation parameters are not chosen carefully[64]. Due to the 
complexity and inhomogeneity of the system, the combinations of simulation 
parameters such as the thermostat algorithm, treatment of electrostatic interactions, 
charge groups and neighbor list update frequency must all be carefully considered and 
tested[64] as in the case of CNTs. Figure 3 shows that an artificial net flux appears


## Page 9


very easily unless all the relevant simulation parameters are chosen properly. It is also 
important to notice that none of the parameter combinations shown in the Figure 3 
would produce artifacts in a pure membrane system. The introduction of a membrane 
embedded protein creates a very different (inhomgeneous) local environment. 
Next we discuss the parameter choices in more detail. As Figure 3 shows, the 
system appears to be particularly sensitive to the choice of the neighbor list update 
frequency (NLUF in the legend). Updating the neighbor lists is very time consuming, 
and thus less frequent updates are preferred for computational efficiency. Update 
frequency of 10 (every 10th time step) is the most commonly used choice in 
membrane simulations and also the default value in Gromacs. This technique is 
commonly used since it provides a significant speed up in the calculation of forces. 
However, some interactions could be missing from the calculation if the lists are not 
updated often enough. The situation is, however, somewhat more subtle. As Figure 3 
shows, the net flux with NLUF=1 may be even larger than with NLUF=10 depending 
on other parameters. This demonstrates an unexpected and potentially dangerous 
cancellation of errors. 
In addition to the neighbor list update frequency, the method of computing the 
electrostatic interactions has a major effect. As Figure 3 shows, simulations using the 
Particle Mash Ewald (PME) technique[61, 62] perform significantly better in 
comparison to the reaction field (RF) method (simple cutoff should never be used). 
Qualitatively, this difference can be traced to the fact that the dielectric constant of the 
system is not homogenous because of the molecular mixture of protein, lipids and 
water. PME takes these issues into account much more accurately than the reaction 
field which uses a mean-field beyond the immediate vicinity of each charge. In 
addition, at the RF cutoff, there is a discontinuity in the electrostatic potential and this 
may create an artificial force[55, 65]. Recently, Ni et al.[65, 66] reported that the use 
of a charge group based truncation with the reaction field can lead to an artificial 
repulsion between charged residues. We tested this by comparing simulations using 
NLUF=1 and NLUF=10 and atom based truncation. The results in Figure 3 show that 
the unidirectional flow persists.  
 The one remaining issue is thermostatting. In our previous study[44], we have 
shown that the Berendsen weak coupling thermostat could create an inhomogenous 
temperature inside a nanopore leading to a net flow. When the velocity-rescale 
algorithm[58, 59] was applied instead, the unidirectional artificial flow disappeared.


## Page 10


The effect is also visible in Figure 3, but it is weak compared to the other two effects 
discussed above. In summary, a safe protocol for simulations of systems containing 
pores and channels to avoid an artificial unidirectional flow should contain: i) PME 
(or comparable) for the treatment of long-range electrostatic interactions, ii) neighbor 
lists should be updated at every time step, and iii) the velocity-rescale thermostat 
instead of the Berendsen weak coupling thermostat[64]. 
 
4. Long-range electrostatics 
We start the more general discussion with electrostatic interactions. This topic 
was already mentioned in the two Case Studies above and has been discussed in 
numerous reviews, see e.g., see Refs. [67-71]. In general, since the computation of 
electrostatic interactions is time consuming, several methods have been introduced to 
deal with them. Earlier methods include truncation of the Coulomb interaction. It has 
been shown in a number of studies that it may lead to errors and severe artifacts. In an 
earlier paper, Saito showed that protein simulations are strongly influenced by 
truncation errors[72]. On membrane systems, one of us showed that evaluation of the 
long-range electrostatic interactions by cutoffs introduced spurious effects and even 
lead to a phase change in lipid bilayers[73, 74]. Currently, virtually all modern-day 
simulations are performed using Ewald summations based methods such the Particle-
Mesh Ewald (PME)[62] and Particle-Particle-Particle-Mesh (P3M)[75, 76]; methods 
such as the Fast Multipole Method[77, 78] and multigrid[79] would work too but they 
have yet to gain more popularity. 
The Ewald summation and other Ewald based methods have also been 
questioned. An earlier study suggested that there are finite-size artifacts related to the 
Ewald method which have their origin in the difficulty of defining the “zero of 
energy”[80]. The possible artificial periodicity and the resulting rotational properties 
were further studied by Smith and Pettitt[81] who concluded that for liquids with high 
dielectric constant (aqueous solutions) artifacts are negligible.  
 
Another issue related to electrostatics is boundary conditions as discussed in 
the above reviews. In general, the straightforward implementation of any of the Ewald 
methods requires periodic boundaries to be efficient, yet in many cases it might be 
interesting to simulate systems that do not have fully periodic boundaries. We will not 
discuss this in detail but refer the reader to Refs. [68, 82] In addition, there has been


## Page 11


recent interest in simulating systems with net charge. The Ewald based methods 
require charge neutrality. Extensions to non-charge neutral systems have been 
suggested and artifacts related to them have been recently discussed by Hub et al.[83]. 
Charge groups are used to increase performance for updating the Coulomb 
interactions of neighboring atoms and they can provide a remarkable speedup[53, 67]. 
Although the electrostatic interactions are calculated for all individual charges in the 
group, the locations of charge groups are defined by the averages of the coordinates of 
the charges belonging to the group, see Refs. [53, 67] for details. Unfortunately, it is 
very easy to reproduce the unphysical flow by using the default simulation 
parameters.  
Computational cost has been one of the main concerns with systems rich in 
charges (partial and otherwise) such as biomolecular systems. In the past, the most 
common technique was to use truncation instead of the full Ewald summation. That 
offers a considerable saving in time since truncation offers O(N) scaling whereas the 
plain Ewald summation scales as O(N2) or after some tricks as O(N3/2). The particle-
mesh approaches, Particle-Mesh-Ewald (PME) and Particle-Particle-Particle-Mesh 
(P3M), scale as O(N log N). There is a catch, though: As already mentioned above, 
several studies have shown that using truncation can lead to spurious effects and may 
have a strong influence on the physical and dynamical properties of biological 
systems[72, 73, 84-89]. There are several recent reviews discussing the treatment of 
electrostatic in soft matter systems[67, 68, 90, 91].  
 
4.1 Electrostatics and protein folding simulations 
In the area of protein folding simulations, the results can be sensitive to the 
choice of a specific scheme. For example, effective melting of a double-norleucine 
mutant of villin[92] has been observed at 380 K in simulations employing the PME 
method for the calculation of the long-range electrostatics and a 9.0 Å cutoff for van 
der Waals forces[93]. Meanwhile, a melting temperature of 300 K was reported when 
the reaction field method was employed for electrostatics with a cutoff of 8.0 Å[94, 
95]. Piana et al.[96] investigated how the treatment of electrostatic interactions affects 
the free energy of folding and the structural properties of proteins[97]. The 
simulations were performed with two different schemes, a cutoff-based force-shifting 
technique[98] and PME[99] for the treatment of electrostatic interactions. The length


## Page 12


of the atom-based cutoff was varied ranging between 8.0 and 12.0 Å to determine 
both electrostatic and van der Waals interactions. The simulation results showed that 
the free energy of folding of a small protein is insensitive to the choice of 
approximation methods when a cutoff beyond 9 Å is used but structural properties of 
the unfolded state depend more strongly on the approximation scheme and 
parameters[96]. 
 
4.2 Artifacts due to atom- and group-based truncations with reaction field 
electrostatics 
The treatment of non-bonded interactions is an extremely important issue in 
MD simulations[100, 101]. As already discussed, one of the most common and 
simplest approaches is truncation but the disadvantage is computational inaccuracy 
with possible severe artifacts [102, 103]. The LJ potential is considered to be of short-
range; generally, interactions are considered to be long-range if the exponent α in 
1/rα, satisfies α<d  where r is the interparticle distance and d is the dimension of 
space.   
With periodic boundary conditions, the PME method is widely used since it is 
more accurate than the truncation schemes, although it may be computationally more 
expensive than truncation. PME could, in principle, be also used for computing LJ 
interactions. Whether or not truncation is faster than PME depends, however, on the 
cutoff distance. Although generally not much of concern, some undesirable artifacts 
due to the interactions between the central cell and its periodic images have been 
reported[104, 105]. An alternative approach is based on continuum electrostatic 
theory, in which the continuum part is evaluated through a reaction field (RF)[60, 
106, 107]. Since only pairwise interactions are accounted for, the RF method is 
reasonably fast in comparison with PME. However, as already mentioned above, one 
the major disadvantages of the RF approach is that it was developed specifically for 
homogeneous systems[60, 106, 108]. In practice, several recent studies have used the 
RF-method in the simulations of ions[109], DNA/RNA/short peptide molecules in 
aqueous solutions[110-115] and lipid bilayers[84]. Some of these simulations[103, 
110] reported satisfactory results with the RF method while others[84, 116] did not.  
Recently, Baumketner [65] found that the success of the reaction-field method 
applied to ions critically depends on the implementation of truncation between the


## Page 13


solute and the solvent. Truncation using charge groups was reported to cause artificial 
repulsion between charged solutes, while using an atomic basis (each atom is a 
separate group) gave good agreement with PME [65]. Ni et al.[66] also studied how 
group- and atom-based truncations influence reaction-field simulations of proteins 
and DNA. Truncation based on charge groups was observed to disrupt native states 
even in short nanosecond simulations due to artificial repulsions between charged 
groups forcing the molecules to unfold. Atom-based truncation produced stable 
trajectories for both DNA and proteins, and the results were in good agreement with 
experiments and simulations using PME. Even though there are systems for which the 
group truncation is adequate[103, 110], it is difficult to formulate a quantitative 
criterion to avoid these artifacts. The decision whether to use group-based or atom-
based truncation should be carefully made on a case-by-case basis.  
 
5. The need to go beyond the Lorentz-Berthelot rules 
For simulations of mixtures of different atoms, virtually every book on 
molecular simulation introduces the Lorentz-Berthelot rules of mixing (see, e.g. [14]): 
When simulating a mixture of atoms of different types, the Lorentz-Berthelot rules 
state that the Lennard-Jones parameters, σ and ε can be obtained as simple arithmetic 
and geometric averages, respectively, as 
 
𝜎𝜎𝑖𝑖𝑖𝑖= 𝜎𝜎𝑖𝑖𝑖𝑖+ 𝜎𝜎𝑗𝑗𝑗𝑗
2
 
 
 
 
 
 
 
𝜀𝜀𝑖𝑖𝑖𝑖= ඥ𝜀𝜀𝑖𝑖𝑖𝑖𝜀𝜀𝑗𝑗𝑗𝑗, 
 
where the indices i and j denote the different atom types, and σii and εii for all i are 
known. The first part was introduced by Lorentz[117] in his 1881 article and the 
second part, the geometric mean for the depth of the energy well, is due to 
Berthelot[118]. The Berthelot rule is sometimes justified by using London’s 
dispersion theory (see e.g., Ref. [117]) and approximations for the ionization 
potentials and molecular sizes. See Rowlinson and Swinton[119] for a detailed 
discussion of the various aspects of the Lorentz-Berthelot mixing rules.  Although a 
derivation along the lines stated above can be provided, the Lorentz-Berthelot rules 
are essentially a pragmatic choice that works reasonably well in many cases.


## Page 14


The Lorentz-Berthelot rules are not the only possible choice, but they remain 
the most common one and are used, for example, in the CHARMM[120] and 
Amber[121] force fields. It is also possible to construct other combining rules based 
on the same theoretical approach but using different approximations with regard to 
ionization potentials, molecular sizes and not using the hard sphere approximation. 
For example, OPLS[122] uses the geometric mean for both σ and ε  as does the 
GROMOS[123-125] force field. Other combination rules, although based on a similar 
approach, are the more specific ones such as Waldman-Hagler[126], Kong[127], 
Halgren[128] and Fender-Halsey[129] rules. Since the Lorentz-Berthelot are used in 
some of the most popular force fields, it is clear that these specific rules are not as 
commonly used. This may change in the future. 
There has been growing interest in going beyond Lorentz-Berthelot. This is 
due to the increasing number of explicit demonstrations in which the Lorentz-
Berthelot rules fail in a rather spectacular manner[130-134]: For example, 
Delhommelle and Millié[130]showed that the application of the Lorentz-Berthelot 
rules may lead to incorrect thermodynamic properties for simple binary mixtures 
whereas using the Kong rules[127] yields good agreement with experiments. In 
another study, one of us demonstrated that in simulations of atoms in the gas phase 
interacting with a surface, the Lorentz-Berthelot rules give surface-gas interactions 
that are 10 times stronger than they should be[133, 135]. This study also showed that 
the standard Lennard-Jones potential may be too hard; the softer Morse potential[14] 
provided a much better fit to data from ab initio simulations. Chase et al. also found 
similar problems in obtaining the proper energy well depths[136]. 
From the above and other studies it has become evident that in addition to 
parameterization against experiments and quantum-chemical simulations, attention 
needs to be paid to the mixing rules / parametrization of unlike-atom interactions. As 
a very recent example, Nikitin et al.[137] proposed a new Amber-ii compatible force 
field for perfluoroalkanes not using the usual Lorentz-Berthelot rules. This new force 
field demonstrated good agreement with both experiments and quantum level 
calculations. The authors point out, however, that the new parameterization is no 
longer compatible with the common Amber/OPLS force field. Other works along 
these lines include Vlcek et al.[138], Hu and Jiang[139], Duarte et al.[140], Forsman 
and Woodward[132], and Moucka et al.[141], Rouha and Nezbeda[142]. Problems


## Page 15


with the standard forms were also noticed in water-protein interactions by Piana et 
al.[143]. We expect that similar new parameterizations will be introduced for other 
types of molecules as well.  
 
6. Force fields: A very brief summary 
We will not discuss force fields here. Force fields are discussed in this issue 
by Lyubartsev et al.[144] and for completeness, we also refer to some additional 
recent reviews [145, 146], tests [93, 147-149] and developments[150]. 
 
7. Thermostats – necessary evil 
 
MD simulations in their basic formalism are inherently in the NVE (constant 
particle number, volume and energy) ensemble. To simulate the experimentally 
relevant canonical (NVT) ensemble, a thermostat must be added to maintain constant 
temperature. The addition of a thermostat may significantly affect the thermal 
fluctuations in the system and cause energy drifts that sometimes have their origin in 
accumulation of numerical errors[151-155]. This is particularly the case when 
truncation schemes are used for interactions: Conservation of linear and angular 
momenta may be violated and although these quantities are initially set to zero, their 
values will unavoidably change due to numerical errors. 
In addition, thermostats can be roughly divided into local and global. Global 
thermostats apply a uniform change instantaneously to all the atoms of the system. 
Nosé-Hoover[156, 157] and the Berendsen weak coupling method[57] are examples 
of them. Local thermostats, on the other hand, act on individual atoms or pairs and 
typically employ fluctuation-dissipation relation from statistical mechanics. We will 
discuss both of these categories below. 
 
7.1 The “flying ice cube” effect and what to do about it 
 
One of the best known artifacts in MD simulations is the so-called “flying ice 
cube” discussed first by Harvey et al.[151]. The “flying ice cube” artifact gets its 
name from the fact that when a system suffers from it, its high-frequency motions 
drain to low-frequency modes and eventually the system freezes and becomes a flying 
ice cube; the center of mass motions, both rotation and translation, are low-frequency 
motions and gain energy due to the drain from high-frequency motions. In their


## Page 16


original paper, Harvey et al. pointed out that the flying ice cube artifact is a violation 
of the equipartition principle and is not specific to any simulation package but rather 
solely due to velocity rescaling – a technique applied by global thermostats including 
the commonly used Berendsen weak coupling method[57] and Nosé-Hoover[156, 
157]. This problem is typically associated with the Berendsen weak-coupling method 
but Wagner et al.[158] have shown that it also occurs in constrained internal 
coordinate simulations with the Nosé-Hoover thermostat with very large (20 fs) time 
steps. Harvey et al.[151] suggested three approaches to remedy the problem: The first 
one is velocity reassignment instead of rescaling. This essentially means using a local 
thermostat that acts on individual atoms or pairs, rather than on all the atoms with the 
same strength. Andersen[159], Lowe-Andersen[160], Langevin[161] and the 
dissipative particle dynamics thermostat[162] are examples of such; commonly used 
terminology for dissipative particle dynamics often refers to a soft conservative 
potential together with a fluctuation-dissipation relation, but the method is 
independent of the precise form of the conservative potential and can be considered as 
a momentum conserving Langevin thermostat[163]. These local thermostats apply 
Gaussian random noise to maintain the canonical ensemble. The other two 
suggestions were removal of center of mass motion and better algorithms for 
rescaling. The latter two are typically part of modern simulation protocols: In a 
typical simulation, center of mass motion is removed periodically during the 
simulation and on the algorithmic side the practical remedy is to use sufficiently large 
coupling times for global (such as Berendsen weak coupling) thermostats. A 
modification of the Berendsen weak coupling method, the so-called velocity rescale 
algorithm of Bussi, Donadio and Parrinello[58, 59] has been shown[64] to perform 
well and has lately become popular. 
An important question related to thermostats is sampling, i.e., how to 
determine if the ensemble is reproduced and sampled adequately. This is crucial for 
computing thermodynamic properties. An elegant procedure for testing this based on 
performing paired simulations and cancellation of system-dependent properties 
between them was recently introduced by Shirts[164]. He tested several thermostats 
and barostats and concluded that of the thermostats, “all tested thermostats except the 
Berendsen thermostat give statistically good results”. The tested thermostats included 
the Berendsen weak coupling[57], Nosé-Hoover[156, 157], the stochastic 
Langevin[161], Andersen[159] and the velocity rescale algorithm of Bussi, Donadio


## Page 17


and Parrinello[58, 59]. We will discuss the results for barostats below in Sec. 8. Shirts 
also provides tools and code as open source at http://simtk.org/home/checkensemble. 
For further reading on different aspects of thermostatting, please see also Refs. [165, 
166]. Finally, we would like to point out that in the case of non-equilibrium systems, 
thermostatting becomes even more complex[167].  
 
7.2 Failure of Nosé-Hoover for non-ergodic systems and the fix 
 
A lesser known, although well-documented issue is the failure of the Nosé -
Hoover thermostat for non-ergodic systems. Integrable systems are examples of such. 
In large ergodic systems – such as virtually all simulations of biological systems - no 
such problem exists. The solution was given by Martyna, Klein and Tuckerman[168] 
who connected a series of Nosé-Hoover thermostat to construct a Nosé-Hoover chain. 
In current protocols, Nosé-Hoover chains are commonly used in ab initio simulations. 
An excellent discussion of both the Nosé-Hoover method and Nosé-Hoover chains is 
provided in the book of Tuckerman which also discusses methods for Hamiltonian 
systems including the Nosé-Poincare method of Bond et al.[169].  
 
7.3 Hot solvent – cold solute problem 
In simulations of biological systems, such as membranes, it is common to 
apply separate thermostats to the solvent (water and ions) and the solute (e.g. a 
membrane). This is done to avoid stationary temperature gradients due to too slow 
exchange of kinetic energy in inhomogeneous solvent-solute systems: With a single 
(global) thermostat, the solvent and solute may acquire different temperatures. This is 
the so-called “hot solvent – cold solute problem”[170]. The simplest solution is 
indeed to apply thermostats separately the solute and solvent. In practice, the 
simulated system may consist of macromolecules and water, and a separate 
thermostat can perturb the dynamics of the macromolecule much more strongly than 
single global control. This may introduce large artifacts into the conformational 
dynamics of the macromolecules. Recently, Lingenheil et al.[171] proposed a strategy 
of controlling temperature based on the concept that an explicit solvent environment 
represents an ideal thermostat concerning the magnitude and time correlations of 
temperature fluctuations of the solute. This strategy can provide a homogeneous


## Page 18


temperature distribution with the correct statistical ensemble and minimal 
perturbation dynamics of the solute molecule. 
 
7.4 The effect of treatment of thermostat on protein folding in the replica 
exchange molecular dynamics (REMD) simulations 
Not only can the approximations of long-range interactions produce a 
significant problem in computations of thermodynamic, structural, and dynamic 
properties of proteins but a thermostat can also have an effect on the folded/unfolded 
state populations[153, 172]. The problem when using the Berendsen weak coupling 
thermostat in REMD simulations was pointed out by Rosta and Hummer[153, 173, 
174]. REMD is a method to enhance conformational sampling in MD simulations by 
using several copies of the physical system in parallel at different temperatures[175, 
176]. Then, attempts to exchange the structures between these systems are made at 
certain intervals to increase the efficiency of conformational sampling. The 
acceptance criterion to exchange conformation between any two temperatures is 
designed to maintain the canonical probability distribution in the configurational 
space. As already mentioned above, it has long been known that the Berendsen weak 
coupling thermostat does not correctly reproduce the canonical ensemble[154, 155]. 
Rosta and Hummer investigated its effects on protein folding[153] and observed a 
shift in the equilibrium folded/unfolded states of a small peptide in water. They 
showed this to be related to the weak coupling thermostat. The folded state was 
observed to be overpopulated and underpopulated at low and high temperatures, 
respectively. The population shift results from the narrowed down potential energy 
distribution due to the non-canonical ensemble[153]. Thus, REMD simulations of 
proteins folding should only be performed with thermostats that produce the canonical 
ensemble such as the Langevin thermostat[161, 177], Andersen thermostat[159], 
Nosé-Hoover thermostat[156, 157] or the velocity-rescale thermostat[58, 59].  
 
 
8. Barostats: How about compressibility? 
Simulations using the NpT (constant particle number, pressure and 
temperature) ensemble are typically needed in simulations of membrane systems. To 
simulate the NpT ensemble, a barostat is needed in addition to a thermostat. Common 
choices include the Langevin piston[178], the Rahman-Parrinello method[179], the


## Page 19


Martyna-Tuckerman-Tobias-Klein algorithm [180, 181] and, perhaps most 
commonly, the Berendsen barostat[57]. The Berendsen method is conceptually simple 
and hence it is very commonly used. It is often used in membrane simulations to 
evaluate compressibility but, strictly speaking, that is not entirely correct since this 
barostat does not produce the correct canonical distribution[182]. This is important 
since the area compressibility is typically evaluated using the formula 𝐾𝐾𝐴𝐴= 𝐴𝐴ቀ
𝜕𝜕𝜕𝜕
𝜕𝜕𝜕𝜕ቁ,  
where 𝐾𝐾𝐴𝐴 is area compressibility, A the area, and γ surface tension. The Parrinello-
Rahman barostat, although computationally more expensive, produces the correct 
distribution and does not suffer from such issues. Please see Waheed and 
Edholm[183] for an in-depth discussion about compressibility of bilayer systems. 
As discussed in Sec. 7.1, Shirts[164] also tested barostats. In his tests, the 
Martyna-Tuckerman-Tobias-Klein barostat performed the best and the Parrinnello-
Rahman was determined to be “acceptable”. For the commonly used Berendsen 
barostat Shirts writes: “Berendsen pressure control is simply wrong for any 
calculation where volume fluctuations are important.” In the context of membrane 
(and comparable) simulations using the NpT ensemble, this means that elastic moduli, 
such as compressibility, will not be correct. In addition, Shirts noticed abnormally 
long autocorrelation times when the Berendsen barostat was used together with the 
Bussi-Donadio-Parrinello velocity rescale thermostat. The reason remains unresolved. 
We would like to note that Shirts’ tests were carried out using a very long 8 fs time 
step (typical MD time step is 2 fs). Shirts used Gromacs 4.6 for the simulations. In 
another study, Rogge et al.[184] used metal-organic  frameworks and came to similar 
conclusion: The Martyna-Tuckerman-Tobias-Klein and Langevin barostats were 
shown to work well in such systems. The Rahman-Parrinello method was not tested. 
 
9. Epilogue: User - the most significant error source 
The above discussion listed some of the common sources of error in molecular 
simulations. We also presented two case studies to show some of the effects of such 
artifacts and how unexpected yet potentially dangerous cancellation of error may 
occur. It is important to notice that some of the topics discussed are not actual 
artifacts. For example, the trick of updating the neighbor lists only about every 10 
time steps is well validated and works extremely well in many cases. When used 
improperly it will not (unless used really recklessly) make a simulation crash.


## Page 20


Improper use will, however, yield unphysical results as discussed. One may ask, 
whose fault is it? The answer is simple: It is always the user’s fault. No matter how 
simple the simulation, the user must always check and validate all the parameter (as 
well as protocol) choices even if they have been used extensively before. Breaking the 
second law of thermodynamics like in Case Studies 1 and 2 demonstrates that 
anything is indeed possible and that such unphysical results may look very exciting. 
As with many other things in life, if something looks too good, it most likely is. This 
also explains why so many bad, uninformed, or sometimes old, choices still remain in 
simulation protocols: Validation is time consuming and thankless. The best case is 
that everything is ok. That is in some sense frustrating as it appears to be a waste of 
time. In the worst case, something appears to be wrong or suspicious and finding the 
origin may be extremely time consuming and tedious as anyone who has tried it 
knows very well. Sometimes there is a silver lining: A new protocol or method is 
established and published, serving the whole community.  
It may sound absurd and somewhat provoking, but available simulation 
software (i.e., not home grown programs) becoming very user friendly and easy to 
obtain can almost be seen as a negative development! It is very easy for anyone to 
download GROMACS [185-187], NAMD[188], LAMMPS[189] or any other 
powerful simulation package and set up simulation without having the faintest idea of 
the algorithms, protocols, tricks of the trade, analysis, etc. Since all of those packages 
represent the state-of-the-art, they are both very powerful and algorithmically stable – 
two features that may give an uninformed user the false feeling of power and 
knowledge: One does not become a theorist by buying chalk, experimentalist by 
buying a microscope or a computational scientist by downloading software. Chalk 
may be the most challenging for getting the initial results out, but with a microscope 
and software one gets, if nothing else, pretty pictures very easily. Pretty pictures are 
not results of rigorous research. In able hands, however, computational modeling is an 
extremely powerful tool that provides quantitative results, has true predictive power, 
and can steer research to a new track.  
Although we have discussed errors, artifacts and problems, we would like to 
emphasize that this is a sign of an active and healthy field – identification of problems 
leads to improvements, higher reliability, quantitative predictions and new 
developments. Computational research is at a very active and exciting state and we 
are positive that this trend will continue for a long time.


## Page 21


Finally, here are some recommendations that should serve as good starting 
points for basic biomolecular simulations based on current knowledge: The Bussi-
Donadio-Parrinello velocity-rescale thermostat[58, 59], the Martyna-Tuckerman-
Tobias-Klein[180, 181] and Langevin barostats[161]. If full Ewald-based summation 
is not used for Lennard-Jones, then forces should be shifted smoothly to zero. 
PME[61, 62] or P3M[190, 191] for long-range electrostatics (for the cases with non-
periodic boundary conditions, please see the discussions in Refs.[67, 68]). And 
always remember to test! 
 
Acknowledgements 
J.W. gratefully acknowledges financial supports from the Faculty of Science 
and Kasetsart University Research and Development Institute (KURDI) at Kasetsart 
University. 
 
References  
[1] M. Karplus, J. Kuriyan, Molecular dynamics and protein function, Proc. Natl. 
Acad. Sci. U.S.A., 102 (2005) 6679-6685. 
[2] G. Hummer, J.C. Rasaiah, J.P. Noworyta, Water conduction through the 
hydrophobic channel of a carbon nanotube, Nature, 414 (2001) 188-190. 
[3] B.L. de Groot, H. Grubmuller, Water permeation across biological membranes: 
mechanism and dynamics of aquaporin-1 and GlpF, Science, 294 (2001) 2353-2357. 
[4] E. Tajkhorshid, P. Nollert, M.O. Jensen, L.J. Miercke, J. O'Connell, R.M. Stroud, 
K. Schulten, Control of the selectivity of the aquaporin water channel family by 
global orientational tuning, Science, 296 (2002) 525-530. 
[5] E. Falck, T. Rog, M. Karttunen, I. Vattulainen, Lateral diffusion in lipid 
membranes through collective flows, J. Am. Chem. Soc., 130 (2008) 44-45. 
[6] E.H. Lee, J. Hsin, M. Sotomayor, G. Comellas, K. Schulten, Discovery Through 
the Computational Microscope, Structure, 17 (2009) 1295-1306. 
[7] R.O. Dror, R.M. Dirks, J.P. Grossman, H. Xu, D.E. Shaw, Biomolecular 
Simulation: A Computational Microscope for Molecular Biology, Ann. Rev. 
Biophys., 41 (2012) 429-452. 
[8] M. Karplus, J.A. McCammon, Molecular dynamics simulations of biomolecules, 
Nat. Struct. Biol., 9 (2002) 646-652.


## Page 22


[9] B. Kirchner, P. di Dio, J. Hutter, Real-World Predictions from Ab Initio Molecular 
Dynamics Simulations, in: B. Kirchner, J. Vrabec (Eds.) Multiscale Molecular 
Methods in Applied Chemistry, vol. 307, Springer Berlin Heidelberg, 2012, pp. 109-
153. 
[10] G. Silva, V. Semiao, Truncation errors and the rotational invariance of three-
dimensional lattice models in the lattice Boltzmann method, J. Comput. Phys., 269 
(2014) 259-279. 
[11] S.T.T. Ollila, C. Denniston, M. Karttunen, T. Ala-Nissila, Fluctuating lattice-
Boltzmann model for complex fluids, J. Chem. Phys., 134 (2011) 064902. 
[12] J. Repakova, J.M. Holopainen, M. Karttunen, I. Vattulainen, Influence of pyrene-
labeling on fluid lipid membranes, J. Phys. Chem. B, 110 (2006) 15403-15410. 
[13] M. Pourmousa, T. Róg, R. Mikkeli, l. Vattulainen, L.M. Solanko, D. Wüstner, 
N.H. List, J. Kongsted, M. Karttunen, Dehydroergosterol as an Analogue for 
Cholesterol: Why It Mimics Cholesterol So Well—or Does It?, J. Phys. Chem. B, 118 
(2014) 7345-7357. 
[14] M.P. Allen, D.J. Tildesley, Computer simulation of liquids, Clarendon Press, 
Oxford, 1987. 
[15] M.S. Miettinen, Computational Modeling of Cationic Lipid Bilayers in Saline 
Solutions, PhD Thesis, Aalto University, Espoo Finland, 2010. 
[16] M. Tuckerman, Statistical Mechanics: Theory and Molecular Simulation, Oxford 
University Press Oxford, UK, 2010. 
[17] P. Larsson, B. Hess, E. Lindahl, Algorithm improvements for molecular 
dynamics simulations, Wires Comput. Mol. Sci., 1 (2011) 93-108. 
[18] R.A. Lippert, C. Predescu, D.J. Ierardi, K.M. Mackenzie, M.P. Eastwood, R.O. 
Dror, D.E. Shaw, Accurate and efficient integration for molecular dynamics 
simulations at constant temperature and pressure, J. Chem. Phys., 139 (2013), 
164106. 
[19] C. Predescu, R.A. Lippert, M.P. Eastwood, D. Ierardi, H.F. Xu, M.O. Jensen, 
K.J. Bowers, J. Gullingsrud, C.A. Rendleman, R.O. Dror, D.E. Shaw, 
Computationally efficient molecular dynamics integrators with improved sampling 
accuracy, Mol. Phys., 110 (2012) 967-983. 
 
[20] S.D. Bond, B.J. Leimkuhler, Molecular dynamics and the accuracy of 
numerically computed averages, Acta Numer., 16 (2007) 1-65.


## Page 23


[21] A. Grossfield, D.M. Zuckerman, Quantifying Uncertainty and Sampling Quality 
in Biomolecular Simulations, Annu. Rep. Comput. Chem., 5 (2009) 23-48. 
[22] R. Pomes, BBA- Biomembranes, this issue(2016). 
[23] M. Manna, W. Kulig, M. Javanainen, J. Tynkkynen, U. Hensen, D.J. Müller, T. 
Rog, I. Vattulainen, How To Minimize Artifacts in Atomistic Simulations of 
Membrane Proteins, Whose Crystal Structure Is Heavily Engineered: β2-Adrenergic 
Receptor in the Spotlight, J. Chem. Theory Comput., 11 (2015) 3432-3445. 
[24] P.F. Tupper, A Conjecture about Molecular Dynamics, in: H. Munthe-Kaas, B. 
Owren (Eds.) Mathematics and Computation, vol. 3, Springer, Heidelberg, Germany, 
2008, pp. 95-108. 
[25] S. McConnell, Code Complete, 2nd Edition ed., Microsoft Press, Redmond (WA, 
USA), 2004. 
[26] A.M. Ferrenberg, D.P. Landau, Y.J. Wong, Monte Carlo simulations: Hidden 
errors from ``good'' random number generators, Phys. Rev. Lett., 69 (1992) 3382-
3384. 
[27] I. Vattulainen, T. Ala-Nissila, K. Kankaala, Physical Tests for Random Numbers 
in Simulations, Phys. Rev. Lett., 73 (1994) 2513-2516. 
[28] G. Miller, A Scientist's Nightmare: Software Problem Leads to Five Retractions, 
Science, 314 (2006) 1856-1857. 
[29] M. Novotny, G.J. Kleywegt, A Survey of Left-handed Helices in Protein 
Structures, J. Mol. Biol., 347 (2005) 231-241. 
[30] M. Majumder, N. Chopra, R. Andrews, B.J. Hinds, Nanoscale hydrodynamics: 
Enhanced flow in carbon nanotubes, Nature, 438 (2005) 930-930. 
[31] J.K. Holt, H.G. Park, Y.M. Wang, M. Stadermann, A.B. Artyukhin, C.P. 
Grigoropoulos, A. Noy, O. Bakajin, Fast mass transport through sub-2-nanometer 
carbon nanotubes, Science, 312 (2006) 1034-1037. 
[32] A. Kalra, S. Garde, G. Hummer, Osmotic water transport through carbon 
nanotube membranes, Proc. Natl. Acad. Sci. U.S.A., 100 (2003) 10175-10180. 
[33] S. Joseph, N.R. Aluru, Why are carbon nanotubes fast transporters of water?, 
Nano Lett., 8 (2008) 452-458. 
[34] B. Corry, Designing carbon nanotube membranes for efficient water desalination, 
J. Phys. Chem. B, 112 (2008) 1427-1434. 
[35] J.A. Thomas, A.J.H. McGaughey, Reassessing fast water transport through 
carbon nanotubes, Nano Lett., 8 (2008) 2788-2793.


## Page 24


[36] C. Song, B. Corry, Intrinsic Ion Selectivity of Narrow Hydrophobic Pores, J. 
Phys. Chem. B, 113 (2009) 7642-7649. 
[37] J.A. Thomas, A.J.H. McGaughey, O. Kuter-Arnebeck, Pressure-driven water 
flow through carbon nanotubes: Insights from molecular dynamics simulation, Int. J. 
Therm. Sci., 49 (2010) 281-289. 
[38] B. Corry, Water and ion transport through functionalised carbon nanotubes: 
implications for desalination technology, Energ. Environ. Sci., 4 (2011) 751-759. 
[39] K. Ritos, D. Mattia, F. Calabro, J.M. Reese, Flow enhancement in nanotubes of 
different materials and lengths, J. Chem. Phys., 140 (2014). 
[40] X.J. Gong, J.Y. Li, H.J. Lu, R.Z. Wan, J.C. Li, J. Hu, H.P. Fang, A charge-driven 
molecular water pump, Nat. Nanotechnol., 2 (2007) 709-712. 
[41] S.Y. Li, P. Xiu, H.J. Lu, X.J. Gong, K.F. Wu, R.Z. Wan, H.P. Fang, Water 
permeation across nanochannels with defects, Nanotechnol., 19 (2008) 105711. 
[42] H.J. Lu, X.J. Gong, C.L. Wang, H.P. Fang, R.Z. Wang, Effect of vibration on 
water transport through carbon nanotubes, Chin. Phys. Lett., 25 (2008) 1145-1148. 
[43] H.J. Lu, J.Y. Li, X.J. Gong, R.Z. Wan, L. Zeng, H.P. Fang, Water permeation 
and wavelike density distributions inside narrow nanochannels, Phys. Rev. B, 77 
(2008) 174115. 
[44] J. Wong-Ekkabut, M.S. Miettinen, C. Dias, M. Karttunen, Static charges cannot 
drive a continuous flow of water molecules through a carbon nanotube, Nat. 
Nanotechnol., 5 (2010) 555-557. 
[45] D.J. Bonthuis, K.F. Rinne, K. Falk, C. Nadir Kaplan, D. Horinek, A. Nihat 
Berker, L. Bocquet, R.R. Netz, Theory and simulations of water flow through carbon 
nanotubes: prospects and pitfalls, J. Phys. Condens. Matter, 23 (2011) 184110. 
[46] W.D. Nicholls, M.K. Borg, D.A. Lockerby, J.M. Reese, Water transport through 
(7,7) carbon nanotubes of different lengths using molecular dynamics, Microfluid 
Nanofluid, 12 (2012) 257-264. 
[47] J.Y. Su, H.X. Guo, Effect of Nanochannel Dimension on the Transport of Water 
Molecules, J. Phys. Chem. B, 116 (2012) 5925-5932. 
[48] B. Hinds, A blueprint for a nanoscale pump, Nat. Nanotechnol., 2 (2007) 673-
674. 
[49] R.D. Astumian, Thermodynamics and Kinetics of a Brownian Motor, Science, 
276 (1997) 917-922.


## Page 25


[50] S. Joseph, N.R. Aluru, Pumping of confined water in carbon nanotubes by 
rotation-translation coupling, Phys. Rev. Lett., 101 (2008) 064502. 
[51] D.J. Bonthuis, K. Falk, C.N. Kaplan, D. Horinek, A.N. Berker, L. Bocquet, R.R. 
Netz, Comment on "pumping of confined water in carbon nanotubes by rotation-
translation coupling", Phys. Rev. Lett., 105 (2010) 209401; author reply 209402. 
[52] Z. Milicevic, S.J. Marrink, A.S. Smith, D.M. Smith, Establishing conditions for 
simulating hydrophobic solutes in electric fields by molecular dynamics Effects of the 
long-range van der Waals treatment on the apparent particle mobility, J. Mol. Model., 
20 (2014) 2359. 
[53] B. Hess, C. Kutzner, D. van der Spoel, E. Lindahl, GROMACS 4: Algorithms for 
highly efficient, load-balanced, and scalable molecular simulation, J. Chem. Theory 
Comput., 4 (2008) 435-447. 
[54] D.J. Bonthuis, D. Horinek, L. Bocquet, R.R. Netz, Electrohydraulic Power 
Conversion in Planar Nanochannels, Phys. Rev. Lett., 103 (2009) 144503-144503. 
[55] S. Toxvaerd, J.C. Dyre, Communication: Shifted forces in molecular dynamics, 
J. Chem. Phys., 134 (2011) 081102. 
[56] C. Oostenbrink, A. Villa, A.E. Mark, W.F. Van Gunsteren, A biomolecular force 
field based on the free enthalpy of hydration and solvation: The GROMOS force-field 
parameter sets 53A5 and 53A6, J. Comput. Chem., 25 (2004) 1656-1676. 
[57] H.J.C. Berendsen, J.P.M. Postma, W.F. Vangunsteren, a. Dinola, J.R. Haak, 
Molecular-Dynamics with Coupling to an External Bath, J. Chem. Phys., 81 (1984) 
3684-3690. 
[58] G. Bussi, D. Donadio, M. Parrinello, Canonical sampling through velocity 
rescaling, J. Chem. Phys., 126 (2007) 014101. 
[59] G. Bussi, T. Zykova-Timan, M. Parrinello, Isothermal-isobaric molecular 
dynamics using stochastic velocity rescaling, J. Chem. Phys., 130 (2009) 074101. 
[60] I.G. Tironi, R. Sperb, P.E. Smith, W.F. Vangunsteren, A Generalized Reaction 
Field Method for Molecular-Dynamics Simulations, J. Chem. Phys., 102 (1995) 5451-
5459. 
[61] T. Darden, D. York, L. Pedersen, Particle Mesh Ewald - an N.Log(N) Method for 
Ewald Sums in Large Systems, J. Chem. Phys., 98 (1993) 10089-10092. 
[62] U. Essmann, L. Perera, M.L. Berkowitz, T. Darden, H. Lee, L.G. Pedersen, A 
Smooth Particle Mesh Ewald Method, J. Chem. Phys., 103 (1995) 8577-8593.


## Page 26


[63] H.J.C. Berendsen, J.P.M. Postma, W.F. van Gunsteren, J. Hermans, Interaction 
models for water in relation to protein hydration., in: B. Pullman (Ed.) Intermolecular 
Forces, D. Reidel, Dordrecht, The Netherlands, 1981, pp. 331-342. 
[64] J. Wong-ekkabut, M. Karttunen, Assessment of Common Simulation Protocols 
for Simulations of Nanopores, Membrane Proteins, and Channels, J. Chem. Theory 
Comput., 8 (2012) 2905-2911. 
[65] A. Baumketner, Removing systematic errors in interionic potentials of mean 
force computed in molecular simulations using reaction-field-based electrostatics, J. 
Chem. Phys., 130 (2009) 104106. 
[66] B. Ni, A. Baumketner, Effect of atom- and group-based truncations on 
biomolecules simulated with reaction-field electrostatics, J. Mol. Model., 17 (2011) 
2883-2893. 
[67] G.A. Cisneros, M. Karttunen, P.Y. Ren, C. Sagui, Classical Electrostatics for 
Biomolecular Simulations, Chem. Rev., 114 (2014) 779-814. 
[68] M. Karttunen, J. Rottler, I. Vattulainen, C. Sagui, Electrostatics in biomolecular 
simulations: Where are we now and where are we heading?, Computational Modeling 
of Membrane Bilayers, 60 (2008) 49-89. 
[69] C.J. Fennell, J.D. Gezelter, Is the Ewald summation still necessary? Pairwise 
alternatives to the accepted standard for long-range electrostatics, J. Chem. Phys., 124 
(2006) 234104. 
[70] C. Sagui, L.G. Pedersen, T.A. Darden, Towards an accurate representation of 
electrostatics in classical force fields: Efficient implementation of multipolar 
interactions in biomolecular simulations, J. Chem. Phys., 120 (2004) 73-87. 
[71] Y. Yonetani, Liquid water simulation: A critical examination of cutoff length, J. 
Chem. Phys., 124 (2006) 204501. 
[72] M. Saito, Molecular dynamics simulations of proteins in solution: Artifacts 
caused by the cutoff approximation, J. Chem. Phys., 101 (1994) 4055-4061. 
[73] M. Patra, M. Karttunen, M.T. Hyvonen, E. Falck, P. Lindqvist, I. Vattulainen, 
Molecular dynamics simulations of lipid bilayers: major artifacts due to truncating 
electrostatic interactions, Biophys. J., 84 (2003) 3636-3645. 
[74] M. Patra, M.T. Hyvonen, E. Falck, M. Sabouri-Ghomi, I. Vattulainen, M. 
Karttunen, Long-range interactions and parallel scalability in molecular simulations, 
Comput. Phys. Commun., 176 (2007) 14-22.


## Page 27


[75] R.W. Hockney, J.W. Eastwood, Computer Simulation Using Particles, CRC 
Press, 1988. 
[76] M. Deserno, C. Holm, How to mesh up Ewald sums. I. A theoretical and 
numerical comparison of various particle mesh routines, J. Chem. Phys., 109 (1998) 
7678-7693. 
[77] L. Greengard, V. Rokhlin, A Fast Algorithm for Particle Simulations, J. Comput. 
Phys., 73 (1987) 325-348. 
[78] K. Lorenzen, C. Wichmann, P. Tavan, Including the Dispersion Attraction into 
Structure-Adapted Fast Multipole Expansions for MD Simulations, J. Chem. Theory 
Comput., 10 (2014) 3244-3259. 
[79] C. Sagui, T. Darden, Multigrid methods for classical molecular dynamics 
simulations of biomolecules, J. Chem. Phys., 114 (2001) 6578-6591. 
[80] F. Figueirido, G.S. Del Buono, R.M. Levy, On finite‐size effects in computer 
simulations using the Ewald potential, J. Chem. Phys., 103 (1995) 6133-6142. 
[81] P.E. Smith, B.M. Pettitt, Ewald artifacts in liquid state molecular dynamics 
simulations, J. Chem. Phys., 105 (1996) 4289-4293. 
[82] M.M. Reif, C. Oostenbrink, Toward the correction of effective electrostatic 
forces in explicit-solvent molecular dynamics simulations: restraints on solvent-
generated electrostatic potential and solvent polarization, Theor. Chem. Acc, 134 
(2015) 2. 
[83] J.S. Hub, B.L. de Groot, H. Grubmüller, G. Groenhof, Quantifying Artifacts in 
Ewald Simulations of Inhomogeneous Systems with a Net Charge, J. Chem. Theory 
Comput., 10 (2014) 381-390. 
[84] M. Patra, M. Karttunen, M.T. Hyvonen, E. Falck, I. Vattulainen, Lipid bilayers 
driven to a wrong lane in molecular dynamics simulations by subtle changes in long-
range electrostatic interactions, J. Phys. Chem. B, 108 (2004) 4485-4494. 
[85] A. Robertson, E. Luttmann, V.S. Pande, Effects of long-range electrostatic forces 
onsimulated protein folding kinetics, J. Comput. Chem., 29 (2008) 694-700. 
[86] J.B. Klauda, B.R. Brooks, R.W. Pastor, Dynamical motions of lipids and a finite 
size effect in simulations of bilayers, J. Chem. Phys., 125 (2006). 
[87] S.E. Feller, R.W. Pastor, A. Rojnuckarin, S. Bogusz, B.R. Brooks, Effect of 
Electrostatic Force Truncation on Interfacial and Transport Properties of Water, J. 
Phys. Chem., 100 (1996) 17011-17020.


## Page 28


[88] J. Norberg, L. Nilsson, On the truncation of long-range electrostatic interactions 
in DNA, Biophys. J., 79 (2000) 1537-1553. 
[89] Y. Yonetani, A severe artifact in simulation of liquid water using a long cut-off 
length: Appearance of a strange layer structure, Chem. Phys. Lett., 406 (2005) 49-53. 
[90] J. Rottler, A.C. Maggs, Long-ranged electrostatics from local algorithms, Soft 
Matter, 7 (2011) 3260-3267. 
[91] A. Warshel, A. Dryga, Simulating electrostatic energies in proteins: Perspectives 
and some recent studies of pKas, redox, and other crucial functional properties, 
Proteins: Struct., Funct., Bioinf., 79 (2011) 3469-3484. 
[92] J. Kubelka, T.K. Chiu, D.R. Davies, W.A. Eaton, J. Hofrichter, Sub-microsecond 
Protein Folding, J. Mol. Biol., 359 (2006) 546-553. 
[93] S. Piana, How robust are protein folding simulations with respect to force field 
parameterization? (vol 100, pg L47, 2011), Biophys. J., 101 (2011) 1015-1015. 
[94] K.A. Beauchamp, D.L. Ensign, R. Das, V.S. Pande, Quantitative comparison of 
villin headpiece subdomain simulations and triplet-triplet energy transfer experiments, 
Proc. Natl. Acad. Sci. U.S.A., 108 (2011) 12734-12739. 
[95] D.L. Ensign, P.M. Kasson, V.S. Pande, Heterogeneity even at the speed limit of 
folding: Large-scale molecular dynamics study of a fast-folding variant of the villin 
headpiece, J. Mol. Biol., 374 (2007) 806-816. 
[96] S. Piana, K. Lindorff-Larsen, R.M. Dirks, J.K. Salmon, R.O. Dror, D.E. Shaw, 
Evaluating the Effects of Cutoffs and Treatment of Long-range Electrostatics in 
Protein Folding Simulations, Plos One, 7 (2012) e39918. 
[97] M.M. Reif, V. Krautler, M.A. Kastenholz, X. Daura, P.H. Hunenberger, 
Molecular Dynamics Simulations of a Reversibly Folding beta-Heptapeptide in 
Methanol: Influence of the Treatment of Long-Range Electrostatic Interactions, J. 
Phys. Chem. B, 113 (2009) 3112-3128. 
[98] P.J. Steinbach, B.R. Brooks, New spherical-cutoff methods for long-range forces 
in macromolecular simulation, J. Comput. Chem., 15 (1994) 667-683. 
[99] Y. Shan, J.L. Klepeis, M.P. Eastwood, R.O. Dror, D.E. Shaw, Gaussian split 
Ewald: A fast Ewald mesh method for molecular simulation, J. Chem. Phys., 122 
(2005) 054101. 
[100] W.F. van Gunsteren, D. Bakowies, R. Baron, I. Chandrasekhar, M. Christen, X. 
Daura, P. Gee, D.P. Geerke, A. Glattli, P.H. Hunenberger, M.A. Kastenholz, C. 
Ostenbrink, M. Schenk, D. Trzesniak, N.F.A. van der Vegt, H.B. Yu, Biomolecular


## Page 29


modeling: Goals, problems, perspectives, Angew. Chem. Int. Ed. Engl., 45 (2006) 
4064-4092. 
[101] A. Warshel, P.K. Sharma, M. Kato, W.W. Parson, Modeling electrostatic 
effects in proteins, BBA - Proteins Proteo, 1764 (2006) 1647-1676. 
[102] H. Schreiber, O. Steinhauser, Cutoff size does strongly influence molecular 
dynamics results on solvated polypeptides, Biochem., 31 (1992) 5856-5860. 
[103] A. Baumketner, J.E. Shea, The influence of different treatments of electrostatic 
interactions on the thermodynamics of folding of peptides, J. Phys. Chem. B, 109 
(2005) 21322-21328. 
[104] P.H. Hünenberger, J.A. McCammon, Effect of artificial periodicity in 
simulations of biomolecules under Ewald boundary conditions: a continuum 
electrostatics study, Biophys. Chem., 78 (1999) 69-88. 
[105] W. Weber, P.H. Hünenberger, J.A. McCammon, Molecular Dynamics 
Simulations of a Polyalanine Octapeptide under Ewald Boundary Conditions:  
Influence of Artificial Periodicity on Peptide Conformation, J. Phys. Chem. B, 104 
(2000) 3668-3675. 
[106] D. van der Spoel, P.J. van Maaren, H.J.C. Berendsen, A systematic study of 
water models for molecular simulation: Derivation of water models optimized for use 
with a reaction field, J. Chem. Phys., 108 (1998) 10220-10230. 
[107] P.H. Hünenberger, W.F. van Gunsteren, Alternative schemes for the inclusion 
of a reaction-field correction into molecular dynamics simulations: Influence on the 
simulated energetic, structural, and dielectric properties of liquid water, J. Chem. 
Phys., 108 (1998) 6117-6134. 
[108] G. Hummer, D.M. Soumpasis, M. Neumann, Computer-Simulations Do Not 
Support Cl-Cl Pairing in Aqueous Nacl Solution, Mol. Phys., 81 (1994) 1155-1163. 
[109] X. Rozanska, C. Chipot, Modeling ion–ion interaction in proteins: A molecular 
dynamics free energy calculation of the guanidinium-acetate association, J. Chem. 
Phys., 112 (2000) 9691-9694. 
[110] M. Nina, T. Simonson, Molecular dynamics of the tRNA(Ala) acceptor stem: 
Comparison between continuum reaction field and particle-mesh Ewald electrostatic 
treatments, J. Phys. Chem. B, 106 (2002) 3696-3705. 
[111] A.M.J.J. Bonvin, M. Sunnerhagen, G. Otting, W.F. van Gunsteren, Water 
molecules in DNA recognition II: a molecular dynamics view of the structure and 
hydration of the trp operator1, J. Mol. Biol., 282 (1998) 859-873.


## Page 30


[112] S. Gnanakaran, R. Nussinov, A.E. Garcia, Atomic-level description of amyloid 
beta-dimer formation, J. Am. Chem. Soc., 128 (2006) 2158-2159. 
[113] Y.G. Mu, L. Nordenskiold, J.P. Tam, Folding, misfolding, and amyloid 
protofibril formation of WW domain FBP28, Biophys. J., 90 (2006) 3983-3992. 
[114] H. Verli, A. Calazans, R. Brindeiro, A. Tanuri, J.A. Guimaraes, Molecular 
dynamics analysis of HIV-1 matrix protein: Clarifying differences between 
crystallographic and solution structures, J. Mol. Graph. Model., 26 (2007) 62-68. 
[115] T. Soares, M. Christen, K.F. Hu, W.F. van Gunsteren, Alpha- and beta-
polypeptides show a different stability of helical secondary structure, Tetrahedron, 60 
(2004) 7775-7780. 
[116] V. Kräutler, P.H. Hünenberger, Explicit-solvent molecular dynamics 
simulations of a DNA tetradecanucleotide duplex: lattice-sum versus reaction-field 
electrostatics, Mol. Simulat., 34 (2008) 491-499. 
[117] H.A. Lorentz, Ueber die Anwendung des Satzes vom Virial in der kinetischen 
Theorie der Gase, Ann. Phys. (Berlin), 248 (1881) 127-136. 
[118] D. Berthelot, Sur le mélange des gaz, C. R. Acad. Sci., 126 (1898) 1703–1855. 
[119] J.S. Rowlinson, F.L. Swinton, Liquids and Liquid Mixtures, 3rd edition ed., 
Butterworth Scientific, Oxford, UK, 1982. 
[120] B.R. Brooks, R.E. Bruccoleri, B.D. Olafson, D.J. States, S. Swaminathan, M. 
Karplus, Charmm - a Program for Macromolecular Energy, Minimization, and 
Dynamics Calculations, J. Comput. Chem., 4 (1983) 187-217. 
[121] W.D. Cornell, P. Cieplak, C.I. Bayly, I.R. Gould, K.M. Merz, D.M. Ferguson, 
D.C. Spellmeyer, T. Fox, J.W. Caldwell, P.A. Kollman, A Second Generation Force 
Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules, J. Am. 
Chem. Soc., 117 (1995) 5179-5197. 
[122] W.L. Jorgensen, J. Tirado-Rives, The OPLS [optimized potentials for liquid 
simulations] potential functions for proteins, energy minimizations for crystals of 
cyclic peptides and crambin, J. Am. Chem. Soc., 110 (1988) 1657-1666. 
[123] W.F. van Gunsteren, GROMOS. Groningen Molecular Simulation Program 
Package, University of Groningen, Groningen, 1987. 
[124] X. Daura, a.E. Mark, W.F. Van Gunsteren, Parametrization of aliphatic CHn 
united atoms of GROMOS96 force field, J. Comput. Chem., 19 (1998) 535-547.


## Page 31


[125] L.D. Schuler, X. Daura, W.F. Van Gunsteren, An Improved GROMOS96 Force 
Field for Aliphatic Hydrocarbons in the Condensed Phase, J. Comput. Chem., 22 
(2001) 1205-1218. 
[126] M. Waldman, A.T. Hagler, New combining rules for rare gas van der waals 
parameters, J. Comput. Chem., 14 (1993) 1077-1084. 
[127] C.L. Kong, M.R. Chakrabarty, Combining rules for intermolecular potential 
parameters. II. Rules for the Lennard-Jones (12–6) potential and the Morse potential, 
J. Chem. Phys., 59 (1973) 2464. 
[128] T.A. Halgren, The representation of van der Waals (vdW) interactions in 
molecular mechanics force fields: potential form, combination rules, and vdW 
parameters, J. Am. Chem. Soc., 114 (1992) 7827-7843. 
[129] B.E.F. Fender, G.D. Halsey, Second Virial Coefficients of Argon, Krypton, and 
Argon‐Krypton Mixtures at Low Temperatures, J. Chem. Phys., 36 (1962) 1881-
1888. 
[130] J. Delhommelle, P. MilliÉ, Inadequacy of the Lorentz-Berthelot combining 
rules for accurate predictions of equilibrium properties by molecular simulation, Mol. 
Phys., 99 (2001) 619-625. 
[131] D. Boda, D. Henderson, The effects of deviations from Lorentz–Berthelot rules 
on the properties of a simple mixture, Mol. Phys., 106 (2008) 2367-2370. 
[132] J. Forsman, C.E. Woodward, Limitations of the Derjaguin Approximation and 
the Lorentz-Berthelot Mixing Rule, Langmuir, 26 (2010) 4555-4558. 
[133] K.J. Daun, J.T. Titantah, M. Karttunen, Molecular dynamics simulation of 
thermal accommodation coefficients for laser-induced incandescence sizing of nickel 
particles, Appl. Phys. B, 107 (2012) 221-228. 
[134] D.-M. Duh, D. Henderson, R.L. Rowley, Some effects of deviations from the 
Lorentz-Berthelot combining rules for mixtures of Lennard-Jones fluids, Mol. Phys., 
91 (1997) 1143-1147. 
[135] K.J. Daun, J.T. Titantah, M. Karttunen, Molecular dynamics simulation of 
thermal accommodation coefficients for laser-induced incandescence sizing of nickel 
particles (vol 107, pg 221, 2012), Appl. Phys. B-Lasers O, 112 (2013) 599-600. 
[136] D. Chase, M. Manning, J.A. Morgan, G.M. Nathanson, R.B. Gerber, Argon 
scattering from liquid indium: Simulations with embedded atom potentials and 
experiment, J. Chem. Phys., 113 (2000) 9279-9287.


## Page 32


[137] A. Nikitin, Y. Milchevskiy, A. Lyubartsev, AMBER-ii: New Combining Rules 
and Force Field for Perfluoroalkanes, J. Phys. Chem. B, 119 (2015) 14563-14573. 
[138] L. Vlcek, A.A. Chialvo, D.R. Cole, Optimized Unlike-Pair Interactions for 
Water-Carbon Dioxide Mixtures Described by the SPC/E and EPM2 Models, J. Phys. 
Chem. B, 115 (2011) 8775-8784. 
[139] Z.Q. Hu, J.W. Jiang, Assessment of Biomolecular Force Fields for Molecular 
Dynamics Simulations in a Protein Crystal, J. Comput. Chem., 31 (2010) 371-380. 
[140] F. Duarte, P. Bauer, A. Barrozo, B.A. Amrein, M. Purg, J. Aqvist, S.C.L. 
Kamerlin, Force Field Independent Metal Parameters Using a Nonbonded Dummy 
Model, J. Phys. Chem. B, 118 (2014) 4351-4362. 
[141] F. Moucka, I. Nezbeda, W.R. Smith, Molecular Force Field Development for 
Aqueous Electrolytes: 1. Incorporating Appropriate Experimental Data and the 
Inadequacy of Simple Electrolyte Force Fields Based on Lennard-Jones and Point 
Charge Interactions with Lorentz-Berthelot Rules, J. Chem. Theory Comput., 9 
(2013) 5076-5085. 
[142] M. Rouha, I. Nezbeda, Non-Lorentz-Berthelot Lennard-Jones mixtures: A 
systematic study, Fluid Phase Equilibr., 277 (2009) 42-48. 
[143] S. Piana, A.G. Donchev, P. Robustelli, D.E. Shaw, Water Dispersion 
Interactions Strongly Influence Simulated Structural Properties of Disordered Protein 
States, J. Phys. Chem. B, 119 (2015) 5113-5123. 
[144] A.P. Lyubartsev, A.L. Rabinovich, Force field development for lipid membrane 
simulations, BBA- Biomembranes, this issue (2016). 
[145] S.J. Marrink, D.P. Tieleman, Perspective on the Martini model, Chem. Soc. 
Rev., 42 (2013) 6801-6822. 
[146] L. Monticelli, D.P. Tieleman, Force Fields for Classical Molecular Dynamics, 
in: L.S. Monticell, E. (Eds.) (Ed.) Biomolecular Simulations: Methods and Protocols. 
Methods in Molecular Biology, Springer Science + Business Media, 2013, pp. 197–
213  
[147] E.A. Cino, W.-Y. Choy, M. Karttunen, Comparison of Secondary Structure 
Formation Using 10 Different Force Fields in Microsecond Molecular Dynamics 
Simulations, J. Chem. Theory Comput., 8 (2012) 2725-2740. 
[148] K. Lindorff-Larsen, P. Maragakis, S. Piana, M.P. Eastwood, R.O. Dror, D.E. 
Shaw, Systematic Validation of Protein Force Fields against Experimental Data, Plos 
One, 7 (2012) e32131.


## Page 33


[149] K.A. Beauchamp, Y.-S. Lin, R. Das, V.S. Pande, Are Protein Force Fields 
Getting Better? A Systematic Benchmark on 524 Diverse NMR Measurements, J. 
Chem. Theory Comput., 8 (2012) 1409-1414. 
[150] A. Botan, F. Favela-Rosales, P.F.J. Fuchs, M. Javanainen, M. Kanduč, W. 
Kulig, A. Lamberg, C. Loison, A. Lyubartsev, M.S. Miettinen, L. Monticelli, J. 
Määttä, O.H.S. Ollila, M. Retegan, T. Róg, H. Santuz, J. Tynkkynen, Toward 
Atomistic Resolution Structure of Phosphatidylcholine Headgroup and Glycerol 
Backbone at Different Ambient Conditions, J. Phys. Chem. B, 119 (2015) 15075–
15088. 
[151] S.C. Harvey, R.K.Z. Tan, T.E. Cheatham, The flying ice cube: Velocity 
rescaling in molecular dynamics leads to violation of energy equipartition, J. Comput. 
Chem., 19 (1998) 726-740. 
[152] S.-W. Chiu, M. Clark, S. Subramaniam, E. Jakobsson, Collective motion 
artifacts arising in long-duration molecular dynamics simulations, J. Comput. Chem., 
21 (2000) 121-131. 
[153] E. Rosta, N.V. Buchete, G. Hummer, Thermostat Artifacts in Replica Exchange 
Molecular Dynamics Simulations, J. Chem. Theory Comput., 5 (2009) 1393-1399. 
[154] M. D'Alessandro, A. Tenenbaum, A. Amadei, Dynamical and Statistical 
Mechanical Characterization of Temperature Coupling Algorithms, J. Phys. Chem. B, 
106 (2002) 5050-5057. 
[155] T. Morishita, Fluctuation formulas in molecular-dynamics simulations with the 
weak coupling heat bath, J. Chem. Phys., 113 (2000) 2976-2982. 
[156] S. Nosé, A unified formulation of the constant temperature molecular dynamics 
methods, J. Chem. Phys., 81 (1984) 511-519. 
[157] W.G. Hoover, Canonical dynamics: Equilibrium phase-space distributions, 
Phys. Rev. A, 31 (1985) 1695-1697. 
[158] J.R. Wagner, G.S. Balaraman, M.J.M. Niesen, A.B. Larsen, A. Jain, N. Vaidehi, 
Advanced techniques for constrained internal coordinate molecular dynamics, J. 
Comput. Chem., 34 (2013) 904-914. 
[159] H.C. Andersen, Molecular dynamics simulations at constant pressure and/or 
temperature, J. Chem. Phys., 72 (1980) 2384-2393. 
[160] E.A. Koopman, C.P. Lowe, Advantages of a Lowe-Andersen thermostat in 
molecular dynamics simulations, J. Chem. Phys., 124 (2006) 204103.


## Page 34


[161] G.S. Grest, K. Kremer, Molecular dynamics simulation for polymers in the 
presence of a heat bath, Phys. Rev. A, 33 (1986) 3628-3631. 
[162] P. Español, P. Warren, Statistical Mechanics of Dissipative Particle Dynamics, 
Europhys. Lett., 30 (1995) 191-196. 
[163] T. Murtola, A. Bunker, I. Vattulainen, M. Deserno, M. Karttunen, Multiscale 
modeling of emergent materials: biological and soft matter, Phys. Chem. Chem. 
Phys., 11 (2009) 1869-1892. 
[164] M.R. Shirts, Simple Quantitative Tests to Validate Sampling from 
Thermodynamic Ensembles, J. Chem. Theor. Comput., 9 (2013) 909-926. 
[165] J.E. Basconi, M.R. Shirts, Effects of Temperature Control Algorithms on 
Transport Properties and Kinetics in Molecular Dynamics Simulations, J. Chem. 
Theor. Comput., 9 (2013) 2887-2899. 
[166] F. Jin, T. Neuhaus, K. Michielsen, S. Miyashita, M.A. Novotny, M.I. 
Katsnelson, H. De Raedt, Equilibration and thermalization of classical systems, New 
J. Phys., 15 (2013) 033009. 
[167] A.J. Page, T. Isomoto, J.M. Knaup, S. Irle, K. Morokuma, Effects of Molecular 
Dynamics Thermostats on Descriptions of Chemical Nonequilibrium, J. Chem. Theor. 
Comput., 8 (2012) 4019-4028. 
[168] G.J. Martyna, M.L. Klein, M. Tuckerman, Nosé–Hoover chains: The canonical 
ensemble via continuous dynamics, J. Chem. Phys., 97 (1992) 2635-2643. 
[169] S.D. Bond, B.J. Leimkuhler, B.B. Laird, The Nosé–Poincaré Method for 
Constant Temperature Molecular Dynamics, J. Comput. Phys., 151 (1999) 114-134. 
[170] P. Hunenberger, Thermostat algorithms for molecular dynamics simulations, 
Advanced Computer Simulation Approaches for Soft Matter Sciences I, 173 (2005) 
105-147. 
[171] M. Lingenheil, R. Denschlag, R. Reichold, P. Tavan, The “Hot-Solvent/Cold-
Solute” Problem Revisited, J. Chem. Theory Comput., 4 (2008) 1293-1306. 
[172] B. Cooke, S.C. Schmidler, Preserving the Boltzmann ensemble in replica-
exchange molecular dynamics, J. Chem. Phys., 129 (2008) 164112. 
[173] E. Rosta, G. Hummer, Error and efficiency of replica exchange molecular 
dynamics simulations, J. Chem. Phys., 131 (2009) 165102. 
[174] E. Rosta, G. Hummer, Error and efficiency of simulated tempering simulations, 
J. Chem. Phys., 132 (2010) 034102.


## Page 35


[175] Y. Sugita, Y. Okamoto, Replica-exchange molecular dynamics method for 
protein folding, Chem. Phys. Lett., 314 (1999) 141-151. 
[176] A.E. Garcia, K.Y. Sanbonmatsu, alpha-Helical stabilization by side chain 
shielding of backbone hydrogen bonds, Proc. Natl. Acad. Sci. U.S.A., 99 (2002) 
2782-2787. 
[177] R.W. Pastor, B.R. Brooks, A. Szabo, An analysis of the accuracy of Langevin 
and molecular dynamics algorithms, Mol. Phys., 65 (1988) 1409-1419. 
[178] S.E. Feller, Y. Zhang, R.W. Pastor, B.R. Brooks, Constant pressure molecular 
dynamics simulation: The Langevin piston method, J. Chem. Phys., 103 (1995) 4613-
4621. 
[179] M. Parrinello, A. Rahman, Polymorphic transitions in single crystals: A new 
molecular dynamics method, J. Appl. Phys., 52 (1981) 7182-7190. 
[180] G.J. Martyna, M.E. Tuckerman, D.J. Tobias, M.L. Klein, Explicit reversible 
integrators for extended systems dynamics, Mol. Phys., 87 (1996) 1117-1157. 
[181] M.E. Tuckerman, J. Alejandre, R. Lopez-Rendon, A.L. Jochim, G.J. Martyna, 
A Liouville-operator derived. measure-preserving integrator for molecular dynamics 
simulations in the isothermal-isobaric ensemble, J. Phys. A: Math. Gen., 39 (2006) 
5629-5651. 
[182] E. Lindahl, O. Edholm, Mesoscopic undulations and thickness fluctuations in 
lipid bilayers from molecular dynamics simulations, Biophys. J., 79 (2000) 426-433. 
[183] Q. Waheed, O. Edholm, Undulation Contributions to the Area Compressibility 
in Lipid Bilayer Simulations, Biophys. J., 97 (2009) 2754-2760. 
[184] S.M.J. Rogge, L. Vanduyfhuys, A. Ghysels, M. Waroquier, T. Verstraelen, G. 
Maurin, V. Van Speybroeck, A Comparison of Barostats for the Mechanical 
Characterization of Metal-Organic Frameworks, J. Chem. Theor. Comput., 11 (2015) 
5583-5597. 
[185] S. Pronk, S. Pall, R. Schulz, P. Larsson, P. Bjelkmar, R. Apostolov, M.R. 
Shirts, J.C. Smith, P.M. Kasson, D. van der Spoel, B. Hess, E. Lindahl, GROMACS 
4.5: a high-throughput and highly parallel open source molecular simulation toolkit, 
Bioinformatics, 29 (2013) 845-854. 
[186] M.J. Abraham, T. Murtola, R. Schulz, S. Páll, J.C. Smith, B. Hess, E. Lindahl, 
GROMACS: High performance molecular simulations through multi-level parallelism 
from laptops to supercomputers, SoftwareX, 1 (2015) 19-25.


## Page 36


[187] S. Páll, M. Abraham, C. Kutzner, B. Hess, E. Lindahl, Tackling exascale 
software challenges in molecular dynamics simulations with GROMACS, in:  Solving 
Software 
Challenges 
for 
Exascale; 
Markidis, S.; Laure, E., 
Eds.; Springer 
International Publishing: Switzerland, 8759 (2015) 3– 27. 
[188] J.C. Phillips, R. Braun, W. Wang, J. Gumbart, E. Tajkhorshid, E. Villa, C. 
Chipot, R.D. Skeel, L. Kale, K. Schulten, Scalable molecular dynamics with NAMD, 
J. Comput. Chem., 26 (2005) 1781-1802. 
[189] S. Plimpton, Fast Parallel Algorithms for Short-Range Molecular Dynamics, J. 
Comput. Phys., 117 (1995) 1-19. 
[190] A.Y. Toukmaji, J.A. Board Jr, Ewald summation techniques in perspective: a 
survey, Comput. Phys. Commun., 95 (1996) 73-92. 
[191] J.W. Eastwood, R.W. Hockney, D.N. Lawrence, P3M3DP-the three-
dimensional periodic particle-particle/particle-mesh program, Comp. Phys. Commun., 
35 (1984) 618-619.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]