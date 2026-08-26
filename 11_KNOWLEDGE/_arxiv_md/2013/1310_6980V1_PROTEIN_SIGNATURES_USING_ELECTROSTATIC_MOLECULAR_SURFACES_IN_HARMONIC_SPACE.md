---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1310.6980v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1310.6980v1_Protein_signatures_using_electrostatic_molecular_surfaces_in_harmonic_space

> Source: 1310.6980v1_Protein_signatures_using_electrostatic_molecular_surfaces_in_harmonic_space.pdf

> Pages: 9

---


## Page 1


Protein signatures using electrostatic molecular surfaces in harmonic space
C. Soﬁa Carvalho1,2,∗Dimitrios Vlachakis3, Georgia Tsiliki3, Vasileios Megalooikonomou4, and Sophia Kossida3†
1 Centro de Astronomia e Astrof´ısica da Universidade de Lisboa, Tapada da Ajuda, 1349–018 Lisbon, Portugal
2 Research Center for Astronomy and Applied Mathematics,
Academy of Athens, Soranou Efessiou 4, 11 527 Athens, Greece
3 Bioinformatics & Medical Informatics Team, Biomedical Research
Foundation of the Academy of Athens, 11 527, Athens, Greece and
4 Computer Engineering and Informatics Department,
School of Engineering University of Patras, 26 500 Patras, Greece
(Dated: June 8, 2021)
We developed a novel method based on the Fourier analysis of protein molecular surfaces to
speed up the analysis of the vast structural data generated in the post–genomic era. This method
computes the power spectrum of surfaces of the molecular electrostatic potential, whose three–
dimensional coordinates have been either experimentally or theoretically determined.
Thus we
achieve a reduction of the initial three–dimensional information on the molecular surface to the one–
dimensional information on pairs of points at a ﬁxed scale apart. Consequently, the similarity search
in our method is computationally less demanding and signiﬁcantly faster than shape comparison
methods. As proof of principle, we applied our method to a training set of viral proteins that are
involved in major diseases such as Hepatitis C, Dengue fever, Yellow fever, Bovine viral diarrhea
and West Nile fever. The training set contains proteins of four diﬀerent protein families, as well as a
mammalian representative enzyme. We found that the power spectrum successfully assigns a unique
signature to each protein included in our training set, thus providing a direct probe of functional
similarity among proteins.
The results agree with established biological data from conventional
structural biochemistry analyses.
Keywords: Protein similarity search; structural biology; harmonic space; electrostatic potentials;
drug design.
INTRODUCTION
The spatial structure of proteins encodes information
on their function, which is essential for a successful drug
design. In the post–genomic era, the search for functional
similarities among proteins is based mostly on identity
and/or similarity of genomic sequences rather than on
their spatial structure. An approach that has been widely
used is the application of self-organizing maps to the pro-
tein amino acid sequence in order to predict the protein
shape and to infer the protein function [1, 2]. This ap-
proach searches for local similarities in the amino acid
sequence and is based on the assumption that the pro-
teins have the same size and that the amino acid sequence
is a determinant of the protein structure. However, there
are many examples of proteins where sequence–based
searches are insuﬃcient to describe their biological func-
tion [3]. While self-organizing maps can classify proteins
into families, they fail at predicting the structure. Since
structure is more conserved than sequence, evolutionary
relationships among proteins, protein structure–function
predictions and comparative modelling should be based
on structural information, rather than on primary amino
acid or genomic sequence [4].
Other approaches have been developed that search
for functional similarities using the complete three–
dimensional information encoded in the spatial coordi-
nates of all the atoms within the protein structure, which
have been derived from X–ray or nuclear magnetic res-
onance experiments.
In these approaches, the three–
dimensional protein structure is modelled by a represen-
tation (or descriptor) based on topological characteris-
tics or structure elements (see e.g. Ref. [5] and refer-
ences therein). Although the structure–based approaches
are more informative on the function than the sequence–
based ones, structure comparison methods are too slow
and are thus rendered impractical to use in large–scale
experiments and real–life applications [6–8].
Other approaches use the protein solvent–accessible
surface, since it is a stronger determinant of the protein
function than sequence or structure [9]. Shape descrip-
tors have been developed based on spatial symmetries,
where the search for similarities consists of shape compar-
ison [10–12]. However, surface comparison methods are
computationally challenging, largely because they suﬀer
from ambiguity in spatial orientation and require that the
surfaces be aligned for an optimal matching (see Ref. [9]
and references therein).
Bioinformatics has become the new biomedical infor-
matics bottleneck, as the cost of genome sequencing and
the sheer quantity of genomic data has recently skyrock-
eted. It has been estimated that the unprocessed data
generated per sequencing machine can be of order at least
30 Gbs per day, which can scale up by a signiﬁcant factor
in the case of mapped/processed data. There is a clear
requirement for fast and eﬃcient analysis of the entire
genome/proteome sequencing data in the up–coming era
of personalized medicine. Due to the continuous improve-
ments in sequencing technologies and proteomic method-
arXiv:1310.6980v1  [q-bio.QM]  25 Oct 2013


## Page 2


2
ologies, the current scaling of available computing, stor-
age and analysis throughput is far lower than the scaling
of the data generation rate. The induced lag between the
processing potential and the processing requirements al-
ready poses problems to researchers and companies in the
bioinformatics ﬁeld. Since it is impossible to constantly
upgrade computer hardware to keep up with the increas-
ing data production rate, the only feasible solution is to
devise algorithms that can oﬀer a competing processing
scaling using the existing hardware at its full potential.
Here we propose a new approach to search for func-
tional similarities among proteins using their molecular
surfaces [13]. Protein molecular surfaces are determinant
of the protein biological activity, with diﬀerent types of
molecular surfaces encoding diﬀerent information about
the protein function. We choose to use surfaces of the
molecular electrostatic potential due to the importance
of the charge distribution in the protein–protein interac-
tions. Protein–protein interactions are essential for cell
signalling and cell function [14, 15]. These processes re-
quire a correct and fast molecular recognition, in which
interactions among electrostatic charges intervene. Dis-
turbances in these processes are in the origin of almost
every major disorder [16] and may lead to severe diseases
such as cancer [17–19]. Therefore the electrostatic po-
tential distribution on the protein molecular surfaces is
crucial to virtually all biological macromolecules involved
in key biochemical pathways [20–22].
Once we calculate the molecular surface for a partic-
ular ﬁlter, we proceed to measure the signal oﬀof the
molecular surface. For our signal analysis, we propose a
method based on the Fourier analysis of molecular sur-
faces. An advantage of Fourier analysis is that it most
easily separates large from small scales. The signal at
each point can be regarded as a realization of a distribu-
tion of ﬂuctuations around an average value of the molec-
ular surface [23, 24]. Instead of measuring information
on the individual points over the surface as shape de-
scriptors do, we measure information on the correlations
among the points, thus waiving the need that the surfaces
be aligned. The simplest statistic is the two–point corre-
lation function in Fourier space, which averages the sig-
nal over the whole volume and measures the variance in
the distribution. Hence our approach transforms three–
dimensional spatial data into one–dimensional frequency
data.
The manuscript is organized as follows.
First we
present the selected proteins and how we synthesise the
corresponding molecular surfaces.
Then we describe
our proposed method to extract functional information,
based on the Fourier analysis of molecular surfaces and
on a dimensionality reduction of the usable information.
Then we present the results and discuss further improve-
ments in the robustness of this method.
Finally we
outline an integrated solution for a functional similar-
ity search among proteins, which progresses towards a
Figure 1: Surfaces of the electrostatic molecular poten-
tial. Left panel: Hepatitis C helicase protein, Right panel:
Hepatitis C polymerase protein. The electrostatic potential
is measured in eV, with range as shown in the corresponding
colour bar.
dimensionality increase of the usable information and a
reduction of the protein sample size.
METHOD
Selected proteins
For our training set, we selected four distinct pro-
tein families, which include twelve helicase proteins, six
methyltransferase proteins, four polymerase proteins and
four glycoproteins. These proteins are mainly viral com-
ponents that are involved in major diseases such as Hep-
atitis C, Dengue fever, Yellow fever, Bovine viral diarrhea
and West Nile fever. We use the Mouse kinase protein
as a decoy, since it has a very diﬀerent function from all
the other proteins.
Helicases are responsible for the unwinding of dou-
ble stranded DNA or RNA during viral replication.
Polymerases are key enzymes that are used for copy-
ing the viral genetic material.
Methyltransferases or
methylases are transferase enzymes that are responsi-
ble for transferring methyl groups from a donor to an
acceptor.
Finally glycoproteins are used for molecu-
lar recognition by viruses. Protein treatments vary de-
pending on the needs of each comparison chart.
The
main treatment is the default X–ray crystallography
protein conformation as it is deposited in the RCSB
database [28]. The selected unedited proteins were the
following. Among the helicases, we selected: a) 1A1V
and 8OHM of the Hepatitis C virus (HCV), b) 1YMF,
1YKS and 2V80 of the Yellow fever virus (denoted by
YF 1YMF, YF 1YKS and YF 2V80 respectively), and c)
2JLU, 2BHR, 2BMF and 2JLQ of the Dengue fever virus
(denoted by DEN 2JLU, DEN 2BHR, DEN 2BMF and
DEN 2JLQ respectively). Among the polymerases, we
selected 2CJQ, 2HCS and 2HCN of the West Nile fever
virus (denoted by WN 2CJQ, WN 2HCS and WN 2HCN
respectively). Among the methyltransferase, we selected


## Page 3


3
3EVA, 3EVB, 3EVC, 3EVD, 3EVE and 3EVF of the
Yellow fever virus (denoted by YF 3EVA, YF 3EVB,
YF 3EVC, YF 3EVD, YF 3EVE and YF 3EVF respec-
tively).
Among the glycoproteins, we selected 1NB7,
4DVN, 4DW4 and 4DW3 of the bovine diarrhea virus
(denoted by BVDV 1NB7, BVDV 4DVN, BVDV 4DW4
and BVDV 4DW3 respectively).
In the Hepatitis C viral protein family, we considered
two HCV helicase proteins, namely the HCV helicase
strain A (the 1A1V entry, denoted by HCV helicaseStrA)
and the HCV helicase strain B (the 8OHM entry, de-
noted by HCV helicaseStrB), whose three-dimensional
coordinates were obtained from the RCSB database [28]
of X–ray protein crystallography structures.
Further-
more, we generated two simulations of the 1A1V pro-
tein crystal, namely the energy–minimized version (de-
noted by HCV helicaseEM) and the molecular dynam-
ics version (denoted by HCV helicaseMD). Both the
HCV helicaseEM and the HCV helicaseMD have been
energetically minimized up to a gradient of 0.05. The
HCV helicaseMD has additionally been subject to a
molecular dynamics simulation.
We also established
a homology model of the HCV helicase (denoted by
HCV helicaseHM) so that the in silico three–dimensional
model of HCV was included in our training set. We also
included an example of a non–helicase HCV viral protein,
namely the 1NB7 structure of the HCV polymerase (the
1NB7 entry, denoted by HCV polymerase).
Molecular surfaces of the selected proteins
Surfaces of the molecular electrostatic potential fol-
low the nonlinear Poisson–Boltzmann equation [25, 26].
We solved numerically for the electrostatic potential us-
ing the ﬁnite–diﬀerence method as implemented in the
APBS Software [27]. The potential was calculated on a
regular grid of size (65, 65, 65)1, with the grid–ﬁll–by–
solute parameter set to 80%. The dielectric constants of
the solvent and the solute were set to 80.0 and 2.0, re-
spectively. An ionic exclusion radius of 2.0 ˚A, a solvent
radius of 1.4 ˚A and a solvent ionic strength of 0.145 M
were applied. Default APBS charges and atomic radii
were used.
Energy
minimization
(EM)
removes
any
resid-
ual geometrical strain from each molecular system,
whereas molecular dynamics (MD) simulates a periodic
cytoplasm–like aqueous environment. Both EM and MD
were performed with the Gromacs suite [29–31] through
1
The size of the grid was kept small in order to speed up the
calculation and reduce the computational load. It was tested to
be suitable for this study, as higher detail would not change the
surface by much, while it would increase the computational load
signiﬁcantly.
our previously developed graphical interface [32]. Molec-
ular dynamics took place in a periodic environment,
which was subsequently solvated with the simple point–
charge water model using the truncated octahedron box
extending to 7 ˚A from each molecule.
Partial charges
were applied and the molecular systems neutralized with
counter–ions as required.
The temperature was set to
300 K, the pressure to 1 atm and the step size to 2 fs. The
total time elapsed at each molecular complex run was
50 ns, using constant number of atoms, volume and tem-
perature (NVT) throughout the calculation in a canoni-
cal environment. The results of the MD simulations were
collected in a molecular trajectory database for further
analysis.
The homology model was produced using Modeller [33,
34] and was evaluated using the Procheck utility [35].
This model was designed in order to include a computer
modelled structure in our training set, which however
shares high sequence identity with its template structure
(approximately 90%).
The RCSB/PDB entries of the selected proteins are
summarized in Table I. In Fig. 1 we show surfaces of the
electrostatic molecular potential for two HCV proteins,
namely the helicase and the polymerase.
The electro-
static potential is measured in eV. In these manuscript,
we used the Connolly representation for the molecular
surfaces [36].
Power spectrum of molecular surfaces
Molecular surfaces contain information on a property
of proteins along the three spatial dimensions. This prop-
erty, in this case the values of the electrostatic potential,
can be regarded as a ﬁeld F(x) deﬁned over points x on
the surface. Functional information is encoded not only
in the positions of the points but also in the correlations
among points. The simplest correlation function that we
can measure is that between pairs of points. The two-
point correlation function ξ of the ﬁeld F measures the
convolution of the ﬁeld over its complex conjugate (see
e.g. Ref. [37])
ξ(r) ≡⟨F ∗(x)F(x + r)⟩= 1
L3
Z
d3x F ∗(x)F(x + r).(1)
The angle brackets indicate an averaging over the nor-
malization volume, which here we take as the volume of
the molecular surface, L3.
We assume that the ﬁeld has a ﬂat geometry and can
be decomposed in a Fourier expansion of plane waves
F(x) =
X
k
Fk exp[−ik · x],
(2)
where the wavenumber k relates with the frequency ν
by k = 2π/ν. If the ﬁeld has a curved geometry, then a


## Page 4


4
Family
Protein
Size=[lx, ly, lz]
Helicase
HCV helicaseStrA
[72.4, 64.8, 55.1]
HCV helicaseEM
[72.8, 65.1, 55.5]
HCV helicaseMD
[72.3, 65.5, 56.3]
HCV helicaseHM
[71.5, 65.7, 55.9]
HCV helicaseStrB
[61.9, 69.6, 61.7]
DEN 2BHR
[93.5, 101.4, 76.8]
DEN 2BMF
[84.4, 111.7, 106.0]
DEN 2JLQ
[66.8, 69.6, 77.0]
DEN 2JLU
[80.4, 95.0, 85.0]
YF 1YKS
[62.2, 58.4, 67.8]
YF 1YMF
[63.6, 58.2, 67.8]
YF 2V8O
[49.2, 69.6, 67.6]
Polymerase
HCV polymerase
[59.0, 77.7, 65.0]
BVDV 2CJQ
[74.4, 69.5, 64.5]
WN 2HCN
[78.5, 75.4, 61.1]
WN 2HCS
[77.2, 75.2, 63.2]
Methyltransferase
YF 3EVA
[43.9, 56.2, 62.7]
YF 3EVB
[43.6, 56.4, 62.6]
YF 3EVC
[43.8, 56.0, 62.2]
YF 3EVD
[44.1, 55.5, 63.3]
YF 3EVE
[44.6, 55.9, 65.2]
YF 3EVF
[43.9, 56.1, 64.2]
Glycoproteins
BVDV 4DVN
[46.2, 67.2, 68.0]
BVDV 4DW3
[46.3, 68.5, 67.9]
BVDV 4DW4
[46.8, 73.4, 67.6]
Kinase
Mouse kinase
[52.5, 69.0, 48.8]
Table I: Input data. Protein families, protein PDB names
and sizes of the corresponding molecular surfaces along the
[x,y,z]–directions, measured in ˚A.
Fourier expansion in spherical harmonics should be used
instead. However, the diﬀerence between the two expan-
sions only matters in scales of order the size of the molec-
ular surface, which correspond to the smallest frequency.
The smallest frequency is the zero–mode in the Fourier
expansion and describes a global oﬀset. The two-point
correlation function becomes
ξ(r) =
*X
k
X
k′
F ∗
kFk′ exp[i(k −k′) · x] exp[−ik′ · r]
+
.(3)
Since the molecular surface is closed, the ﬁeld is periodic
within the size of the surface, which restricts the allowed
wavenumbers to the harmonic boundary condition kn =
(n2π/L)ˆek, where n ∈{0, 1, ...} is the order of the Fourier
modes. As a consequence, all the cross terms with k′ ̸= k
average to zero and the remaining sum is
ξ(r) =
 L
2π
3 Z
d3k |Fk|2 exp[−ik · r].
(4)
Hence the correlation function is the Fourier transform
of the power spectrum P(k) = |Fk|2. This relation-
ship is known as the Wiener-Khinchin theorem.
The
power spectrum measures amplitude correlations among
the modes, discarding however information on the phase.
We proceed to compute the Fourier transform Fk of
3
1 
k
P
1
P
P
2
2
k
12
12
k31
k23
P
P
Figure 2:
Schematic representation of point conﬁgu-
rations for correlations in harmonic space. Left panel:
The conﬁguration of the two-point correlation function con-
tains one free parameter, k12, which is the distance in har-
monic space between the two points P1 and P2. Right panel:
The conﬁguration of the three-point correlation function con-
tains two free parameters, e.g. k12 and k23, describing the
distances in harmonic space respectively between P1 and P2,
and between P2 and P3. The third parameter k13 is related to
the former two by the triangle condition k12 + k23 + k31 = 0.
the molecular surface inferred over a regular grid. The
Fourier–transformed surface measures the amplitude of
the plane waves whose combination reproduces the in-
formation on the original surface. The frequencies of the
plane waves range from the frequency corresponding to
the extension of the surface (i.e. to n = 1), up to the
Nyquist frequency corresponding to twice the bin size of
the grid (i.e. to n = N/2, where N is the number of bins
along a direction of the grid). The size of the molecular
surfaces ranges between 5−7 nm (Table I). The smallest
spatial scale of biological interest is the size of a typical
cluster of aminoacids, which is of order xball ∼0.3 nm.
We choose this spatial scale for the size of the grid, so
that the largest frequency scale that can be probed is of
order kball ∼10 nm−1.
Furthermore, we assume that the ﬁeld is isotropic, i.e.
that it does not have a preferential direction, so that the
power spectrum depends only on the distance between
each pair of points. (See Fig. 2 left panel for an illustra-
tion.) By assuming isotropy, we are discarding informa-
tion on the direction. We proceed to take the ensemble
average of P(k) so that the power at the mode k is the
sum of the power at all the points on a sphere of radius k
from the zero–mode, resulting in a one-dimensional func-
tion P(k). In this way, we collapse the information on the
three-dimensional ﬁeld over the molecular surface onto a
one-dimensional power spectrum over the wavenumbers
of the Fourier–transformed molecular surface.
For a given k, we are sampling a distribution, which
we assume to be Gaussian with mean value ⟨Fk⟩and
variance

|Fk|2
= P(k), from which the Fourier coeﬃ-
cients Fk are drawn. Hence there is a fundamental un-
certainty about the underlying variance, which depends
on the number of coeﬃcients sampled at a given k. Since
the number of k’s on a sphere of radius k scales as k2
and for any real ﬁeld it holds that F−k = Fk
∗, where
the asterisk stands for the complex conjugate, then the
uncertainty scales as ∆P(k)/P(k) =
p
2/k2.


## Page 5


5
Figure 3: Power spectrum of the molecular surfaces of
the selected proteins. Power spectra of the correspond-
ing white-noise molecular surfaces of some helicase and poly-
merase proteins. The values of k are measured in nm−1.
Figure 4: Power spectrum of the molecular surfaces of
the selected HCV helicase proteins. Power spectra of
the molecular surfaces divided by the power spectra of the
corresponding white-noise molecular surfaces. The symbols
depict the power spectra and the error bars depict the error
associated with the measurement. The values of k are mea-
sured in nm−1.
RESULTS
Power spectrum of the molecular surfaces of the
selected proteins
To test our method, we used for training set the pro-
tein simulations described above, containing four dif-
ferent protein families.
For each molecular surface of
the electrostatic potential, we computed its power spec-
trum and the corresponding white-noise power spec-
trum. The white–noise power spectrum was computed
from a surface synthesised as a Gaussian distribution
N(0, 1) times the mean value of the corresponding molec-
ular surface. We observe that the power spectra of all
Figure 5: Power spectrum of the molecular surfaces
of the selected Dengue virus helicase proteins. Power
spectra of the molecular surfaces divided by the power spec-
tra of the corresponding white-noise molecular surfaces. The
symbols depict the power spectra and the error bars depict
the error associated with the measurement. The values of k
are measured in nm−1.
Figure 6: Power spectrum of the molecular surfaces
of the selected Yellow fever virus helicase proteins.
Power spectra of the molecular surfaces divided by the power
spectra of the corresponding white-noise molecular surfaces.
The symbols depict the power spectra and the error bars de-
pict the error associated with the measurement. The values
of k are measured in nm−1.
molecular surfaces have comparable magnitudes, stabi-
lizing around 10−6 for suﬃciently large k (not shown),
whereas the white–noise power spectra have magnitudes
that range from 10−11 to 10−7 (Fig. 3).
This range
is populated by the HCV polymerase at the top, fol-
lowed by the HCV helicaseStrB and HCV helicaseHM in
the intermediary range, and ﬁnally the 1A1Vs helicase
HCV helicaseStrA and its models HCV helicaseEM and
HCV helicaseMD at the bottom. Hence the information
derived from the mean value alone, assuming an under-
lining Gaussian distribution, suggests a coarse clustering
of the proteins in helicases, polymerases and a mixed


## Page 6


6
Figure 7: Power spectrum of the molecular surfaces of
the selected polymerase proteins. Power spectra of the
molecular surfaces divided by the power spectra of the corre-
sponding white-noise molecular surfaces. The symbols depict
the power spectra and the error bars depict the error associ-
ated with the measurement. The values of k are measured in
nm−1.
Figure 8: Power spectrum of the molecular surfaces of
the selected methyltransferase proteins.
Power spec-
tra of the molecular surfaces divided by the power spectra of
the corresponding white-noise molecular surfaces. The sym-
bols depict the power spectra and the error bars depict the
error associated with the measurement. The values of k are
measured in nm−1.
cluster containing helicases and non–helicases.
For an easier comparison of the results, we divided the
power spectra of molecular surfaces by the mean of the
corresponding white–noise power spectra (Figs. 4, 5, 6,
7, 8, 9). For each molecular surface, the power at each
k is one realization of a distribution, hence the power
spectrum is noisy. This noise was estimated by the un-
certainty of the Fourier coeﬃcients at each k, given by
∆P(k) = P(k)
p
2/k2, which we used to compute the
error bars.
We also included the power spectrum of
Mouse kinase in all plots, which shows a nearly ﬂat spec-
trum punctuated by irregular peaks.
Figure 9: Power spectrum of the molecular surfaces of
the selected glycoproteins proteins. Power spectra of the
molecular surfaces divided by the power spectra of the corre-
sponding white-noise molecular surfaces. The symbols depict
the power spectra and the error bars depict the error associ-
ated with the measurement. The values of k are measured in
nm−1.
First we analyse the HCV helicase protein set, which il-
lustrates how our method performs at distinguishing dif-
ferent treatments and strains of the same protein. We
plotted the power spectra of the HCV helicase proteins
in Fig.
4.
We observe that the power spectra of
HCV helicaseStrA, HCV helicaseEM, HCV helicaseMD
and HCV helicaseStrB exhibit a similar pattern up to
k ≈10 nm−1 compatible with that of HCV helicaseHM.
A further inspection reveals details that distinguish
among the helicases.
In particular, we observe that
the power spectra of the models HCV helicaseEM and
HCV helicaseMD exhibit very similar patterns of peaks
attesting to their similar binding state.
Although
HCV helicaseStrA is in a diﬀerent binding state, its
power spectrum exhibits the same level of similarities
with both HCV models, with an anticipated HCV-like
grouping of peaks speciﬁc to our data. For k > 1 nm−1,
these three helicase proteins exhibit three strong peaks
at k ≈2.3, 4.6, 7.3 nm−1. From the distance between
peaks, we infer an average wavelength of λ ≈2.5 nm. The
power spectrum of HCV helicaseHM follows the same
pattern as that of HCV helicaseStrA shifted to smaller
k with a varying relative phase which most of the time
is close to π, with strong peaks at k ≈1.8, 3.6 nm−1.
In comparison with the HCV models, the power spec-
trum of HCV helicaseStrB exhibits diﬀerences in the po-
sition of the peaks (found at k ≈2.7, 3.6, 5.5 nm−1) and
in their amplitude ratios, which attest to the diﬀerent
treatment in HCV helicaseStrB from that in the HCV
models. As k increases, we observe a gradual damping
of the power of the helicases and an emerging tail remi-
niscent of shot noise in a Poisson power spectrum, more
prominent in HCV helicaseHM and HCV helicaseStrB,


## Page 7


7
which indicates the damping of the ﬂuctuations about
the mean value and thus the vanishing of the structural
signal. This damping is most visible for k > 6 nm−1.
This agrees with the observation above that sets the up-
per limit of k to the size of a typical cluster of aminoacids
and hence sets the minimum distance below which cor-
relations are not of biological interest nor can be reliably
probed by X–ray/NMR experiments.
We now proceed to analyse the remaining helicase
strains, which illustrates how our method performs at
distinguishing strains of the same family. We plotted the
power spectra of the Dengue virus (DEN) helicase pro-
teins in Fig. 5 and the Yellow fever virus (YF) helicase
proteins in Fig. 6.
The power spectra of both the YF helicase proteins and
the DEN helicase proteins exhibit a similar pattern with a
varying relative phase among the proteins of each strain,
with the diﬀerence between the two strains being in the
typical wavelength and amplitude. In particular, we ob-
serve that the DEN helicases have an underlying ﬂat
spectrum punctuate by peaks at k ≈2.0, 3.8, 5.5 nm−1
(DEN 2BHR), k ≈3.0, 5.0, 6.0 nm−1 (DN 2JLQ) and
k ≈3.5, 5.0, 6.5 nm−1 (DN 2JLU), that yield an average
λ ≈4.2 nm. The DEN 2BMF shows a diﬀerent pattern
characterized by a decreasing power law up to k ≈5, with
superposed peaks k ≈5.5, 7.0, 8.5 nm−1. In contrast, the
YF helicases have a nearly ﬂat spectrum punctuated by
small peaks at k ≈1.0, 3.5, 5.5 nm−1 (YF 1YKS) and
k ≈1.5, 5.5 nm−1 (YF 1YMF), that yield an average
λ ≈2.0 nm. The YF 2V80 shows a nearly ﬂat spec-
trum with barely no peaks, indicating a predominantly
isotropic distribution of power.
These families have a
similar pattern with the HCV helicases but the features
have smaller amplitudes. The global pattern attests to
the fact that these proteins are also helicases and have the
same treatment as the HCV, whereas the diﬀerences in
amplitude attest to the fact that are of diﬀerent strains.
We now proceed to analyse the non-helicase families,
which illustrates how our method performs at distin-
guishing protein families.
We plotted the power spectra of the polymerase pro-
teins in Fig. 7. We observe that all the polimerases have
the same pattern characterized by an underlying decreas-
ing power law with superposed peaks. In particular, the
West Nile strains have the same pattern at all scales and
a peak at k ≈8 nm−1, i.e. close to the smallest scale
accessible. The BVDV strain has a very similar power
law behaviour to the WN strains but is punctuated by
regular peaks namely at k ≈1.5, 3.0, 4.5, 6.0, 8.0 nm−1,
corresponding to an average λ ≈4 nm. The HCV poly-
merase has the steepest decreasing power law behaviour
and peaks at k ≈5.5, 7.5 nm−1.
We plotted the power spectra of the methyltrans-
ferase proteins in Fig. 8.
We observe that all the YF
methyltransferase have similar patterns characterized by
a nearly ﬂat, featureless power spectrum punctuated by
Figure 10: Power spectra of the molecular surfaces of
the HCV helicaseEM after being subject to molecular
dynamics simulations for 100 ps. Power spectra of the
molecular surfaces divided by the power spectra of the corre-
sponding white-noise molecular surfaces. The symbols depict
the power spectra and the error bars depict the error associ-
ated with the measurement. The values of k are measured in
nm−1.
irregular low–amplitude peaks.
Finally, we plotted the power spectra of the glycopro-
teins in Fig. 9. We observe that all the BVDV glycopro-
teins have the same pattern characterized by an underly-
ing a convex quadratic function with superposed peaks.
In particular both the strains 4DVN and 4DW3 have a
single peak at k ≈7.5 nm−1, whereas the 4DW4 have
peaks at k ≈2.0, 4.5, 6.0, 8.0 nm−1, corresponding to an
average λ ≈3.3 nm.
Power Spectrum of a dynamical simulation
To further test our method, we used the 1A1V tem-
plate energetically minimized up to a gradient of 10−5 to
generate ten dynamical realizations captured in ten time
frames separated by 10 ps. We then energetically mini-
mized the tenth frame up to a gradient of 10−5 [38–40]
We computed the power spectrum of each frame, gener-
ated the corresponding white noise surface and plotted
the results in Fig. 10.
The purpose of this test is to show how our method be-
haves when applied to controlled simulations. We observe
that there is no signiﬁcant diﬀerence among the diﬀerent
frames. This observation supports the fact that the sur-
faces do not change over time after energy minimization
(EM). Also we observe that the two simulations ener-
getically minimized up to a gradient 10−5 are in phase,
whereas the simulation with up to a gradient 5 × 10−2
is visibly out of phase with the former. This observation
supports the fact that there is a diﬀerence between crude
and ﬁne EM.


## Page 8


8
CONCLUSIONS
We presented a new method based on the Fourier anal-
ysis of protein molecular surfaces to extract functional
information on proteins. For a selected set of proteins
of HCV with diﬀerent structural features, we ﬁrst pro-
duced surfaces of the molecular electrostatic potential,
as well as the corresponding white–noise surfaces, and
then computed their two-point correlation function in
harmonic space (the power spectrum). We found that
this method can distinguish diﬀerent functional protein
groups. More speciﬁcally, in this manuscript we estab-
lished a helicase, a polymerase, a methyltransferase and
a glycoprotein group.
We also tested this method on
dynamical simulations after energy minimization.
An immediate extension of this work is the applica-
tion of this method to isolated structural subunits that
form larger structures within proteins.
Similarly sized
subunits will have a strong signal in the same frequency
range, which will add up in the protein power spectrum.
Hence, we must ﬁrst measure the contribution of each
subunit separately and produce a catalogue of subunit
signatures, so we can distinguish them in the combined
signal when running similarity searches.
By reducing the initial three–dimensional information
on the molecular surface to the one–dimensional informa-
tion on pairs of points at a ﬁxed scale apart, this method
allows for a fast similarity search. Further reﬁnements
in the similarity search will require methods that use in-
formation from higher–order correlation functions, such
as the correlation among three points at a ﬁxed trian-
gular conﬁguration or its Fourier–transformed (the bis-
pectrum).
(See Fig. 2 right panel for an illustration.)
The bispectrum measures phase correlations among the
modes and thus deviations from a Gaussian distribution.
Our ultimate goal is to integrate higher–order correla-
tions and to apply the resulting method to the RCSB
database so as to provide the biopharmaceutical and
structural research communities with a novel and easily
searchable reference without the three–dimensional infor-
mation compromising the speed of the calculation. This
method aims to coalesce techniques, which have been
extensively tested and used in other ﬁelds such as cos-
mology, into a fast and robust pipeline for the analysis
and processing of very large, three–dimensional biolog-
ical datasets in an eﬀort to speed up protein similarity
searches.
Acknowledgments CSC is funded by the FCT–Lisbon,
Grant no. SFRH/BPD/65993/2009. This work was sup-
ported in part by the European Union (European So-
cial Fund - ESF) and Greek national funds through the
Operational Program ”Education and Lifelong Learning”
of the National Strategic Reference Framework (NSRF)
- Research Funding Program: “Thales”.
Investing in
knowledge society through the European Social Fund.
∗Electronic address: cscarvalho@oal.ul.pt
† Electronic address: skossida@bioacademy.gr
[1] Kohonen T, (1982) Biol Cybern 43, 59–69
[2] Andrade MA, Casari G, Sander C and Valencia A (1997)
Biol Cybern 76, 441–450
[3] Dobson PD, Cai YD, Stapley BJ, Doig AJ (2004) Curr
Med Chem 11: 2135–2142
[4] Illerg˚ard K, Ardell DH, Elofsson A (2009) Proteins 15;
77(3): 499–508.
[5] Venkatraman V, Sael L and Kihara D (2009), Cell
Biochem Biophys 54: 23–32.
[6] Kolodny R, Koehl P, Levitt M (2005) J Mol Biol 346:
1173–1188.
[7] Mayr G, Domingues FS, Lackner P (2007) BMC Struct
Biol 7: 50.
[8] Berbalk C, Schwaiger CS, Lackner P (2009) Protein Sci
18: 2027–2035.
[9] Via A, Ferr`e F, Brannetti B and Helmer-Citterich M
(2000), Cell. Mol. Life Sci. 57, 1970–1977.
[10] Kazhdan M, Funkhouser T and Rusinkiewicz S (2003),
Proc 2003 Eurographics, 43: 156–164.
[11] Ritchie DW, Kozakov D and Vajda S (2008), Bioinfor-
matics 24(17): 1865–1873.
[12] Venkatraman V, Chakravarthy PR, and Kihara D (2009),
J Cheminformatics 1: 19.
[13] Vlachakis D, Tsiliki G, Tsagkrasoulis D, Carvalho CS,
Megalooikonomou V, Kossida S (2012) EMBnet J. 18(1):
6–9.
[14] Przytycka TM, Singh M, Slonim DK (2010) Brief Bioin-
form. 11 (1): 15–29.
[15] Berger-Wolf TY, Przytycka TM, Singh M, Slonim DK
(2010) Pac Symp Biocomput. 15: 120–122.
[16] Gire SK, Stremlau M, Andersen KG, Schaﬀner SF,
Bjornson Z, Rubins K, Hensley L, McCormick JB, Lan-
der ES, Garry RF, Happi C, Sabeti PC (2012) Science 9,
338(6108): 750–752.
[17] Elcock AH, Gabdoulline RR, Wade RC, McCammon JA.
(1999) J Mol Biol. 291(1): 149–162.
[18] Sept D, Elcock AH, McCammon JA. (1999) J Mol Biol.
294(5): 1181–1189.
[19] Wlodek ST, Shen T, McCammon JA. (2000) Biopoly-
mers. 53(3): 265–271.
[20] Honig B, Nicholls A. (1995) Science 268(5214): 1144–
1149.
[21] Wong GC, Pollack L. (2010) Annu Rev Phys Chem. 61:
171–189.
[22] McCammon JA. (2009) Proc Natl Acad Sci USA.
106(19): 7683–7684.
[23] Vlachakis D, Champeris–Tsaniras S, Kossida S. (2012)
Mol Biochem. 1(3): 144–149.
[24] Kandil S, Biondaro S, Vlachakis D, Cummins AC, Coluc-
cia A, Berry C, Leyssen P, Neyts J and Brancale A.
(2009) J Bioorg Med Chem Lett. 1; 19(11): 2935–2937.
[25] Konecny R, Baker NA, McCammon JA (2012) Comput
Sci Discov 26; 5(1) 015005.
[26] Unni S, Huang Y, Hanson RM, Tobias M, Krishnan S,
Li WW, Nielsen JE, Baker NA (2011) J Comput Chem.
32(7): 1488–1491.
[27] www.poissonboltzmann.org/apbs
[28] www.rcsb.org
[29] Hess B, Kutzner C, van der Spoel D, Lindahl E (2008) J


## Page 9


9
Chem Theory Comput 4: 435–447.
[30] Lindahl E, Hess B, van der Spoel D (2001) J Mol Model
7: 306–317.
[31] van der Spoel D, Lindahl E, Hess B, Groenhof G, Mark
AE, et al. (2005) J Comput Chem 26: 1701–18.
[32] Sellis D, Vlachakis D, Vlassi M (2009) Bioinform Biol
Insights 3: 99–102.
[33] ˘Sali A, Blundell TL (1993) J. Mol. Biol. 234: 779–815.
[34] Eswar N, John B, Mirkovic N, Fiser A, Ilyin VA, Pieper
U, Stuart AC, Mart´ı-Renom MA, Madhusudhan MS,
Yerkovich B, ˘Sali A (2003) Nucl Acids Res 31: 3375–
3380.
[35] Laskowski RA, Rullmannn JA, MacArthur MW, Kaptein
R, Thornton JM (1996) J. Biomol. NMR 8: 477–486.
[36] Connolly ML (1983), J. Appl. Cryst. 16: 548–558.
[37] Peacock JA (1999) Cosmological Physics, CUP.
[38] Vangelatos I, Vlachakis D, Sophianopoulou V, Diallinas
G (2009) Molecular membrane biology 26 (5-7): 356-370
[39] Sellis D, Drosou D, Vlachakis D, Voukkalis D, Gian-
nakouros T, Vlassi M (2012) Biochimica et Biophysica
Acta 1820 (1): 44–55
[40] Vlachakis D, Tsagrasoulis D, Megalooikonomou V, Kos-
sida S (2013) Bioinformatics 29 (1): 126-128

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1310_6980v1_protein_signatures_using_electrostatic_molecular_surfaces_in_harmonic_space
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2013/1310_6980V1_PROTEIN_SIGNATURES_USING_ELECTROSTATIC_MOLECULAR_SURFACES_IN_HARMONIC_SPACE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
