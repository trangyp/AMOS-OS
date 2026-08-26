---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1611.00358v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1611.00358v1_Shannon_entropy_of_brain_functional_complex_networks_under_the_influence_of_the_

> Source: 1611.00358v1_Shannon_entropy_of_brain_functional_complex_networks_under_the_influence_of_the_.pdf

> Pages: 27

---


## Page 1


Shannon entropy of brain functional complex networks
under the inﬂuence of the psychedelic Ayahuasca
A. Viol,1, 2, 3, ∗Fernanda Palhano-Fontes,4 Heloisa Onias,4
Draulio B. de Araujo,4 and G. M. Viswanathan1, 5
1Department of Physics, Universidade Federal do
Rio Grande do Norte, 59078-970 Natal–RN, Brazil
2Computational Biology Center, T. J. Watson Research Center,
IBM, 10598 Yorktown Heights–NY, USA
3Department of Physics, Universidade Federal de Vi¸cosa, 36570-000 Vi¸cosa–MG,Brazil
4Brain Institute, Universidade Federal do Rio Grande do Norte, 59078-970 Natal–RN, Brazil
5National Institute of Science and Technology of Complex Systems
Universidade Federal do Rio Grande do Norte, 59078-970 Natal–RN, Brazil
(Dated: July 26, 2021)
Abstract
The entropic brain hypothesis holds that the key facts concerning psychedelics are partially
explained in terms of increased entropy of the brain’s functional connectivity.
Ayahuasca is
a psychedelic beverage of Amazonian indigenous origin with legal status in Brazil in religious
and scientiﬁc settings. In this context, we use tools and concepts from the theory of complex
networks to analyze resting state fMRI data of the brains of human subjects under two distinct
conditions: (i) under ordinary waking state and (ii) in an altered state of consciousness induced by
ingestion of Ayahuasca. We report an increase in the Shannon entropy of the degree distribution
of the networks subsequent to Ayahuasca ingestion. We also ﬁnd increased local and decreased
global network integration. Our results are broadly consistent with the entropic brain hypothesis.
Finally, we discuss our ﬁndings in the context of descriptions of “mind-expansion” frequently seen
in self-reports of users of psychedelic drugs.
∗aline.viol@ufv.br
1
arXiv:1611.00358v1  [q-bio.NC]  1 Nov 2016


## Page 2


Relatively little is known about how exactly psychedelics act on human functional brain
networks.
During the last few years, new neuroimaging techniques, such as functional
magnetic resonance imaging (fMRI) [1, 2], have allowed noninvasive investigation of global
brain activity in a variety of conditions, e.g., under anaesthesia, sleep, coma, and in altered
states of consciousness induced by psychedelic drugs [3–10]. Recently, Carhart-Harris et
al.
proposed a hypothesis known as the entropic brain, which holds that the stylized
facts concerning altered states of consciousness induced by psychedelics can be partially
explained in terms of higher entropy of the brain’s functional connectivity [11]. Although
the entropy of the brain has never been directly measured, the entropic brain hypothesis is
empirically supported by several recent studies. For example, Sarasso et al. have reported
complex spatiotemporal cortical activation pattern during anesthesia with ketamine, which
can induce vivid experiences (“ketamine dreams”) [12].
Similarly, Petri et al.
found
that after administration of the psychedelic psilocybin, the brain’s functional patterns
undergo a dramatic change characterized by the appearance of many transient low-stability
structures [13]. Perhaps the most convincing evidence supporting the hypothesis thus far has
come from the study undertaken by Tagliazucchi et al. [14], who reported a larger repertoire
of brain dynamical states during the psychedelic experience with psilocybin. They inferred
an increase in the entropy of the functional connectivity in several regions of the brain, by
studying the temporal evolution (i.e., dynamics) of the connectivity graphs. Here we directly
measure increases in entropy associated with the functional connectivity of the whole brain
under the inﬂuence of a psychedelic. Speciﬁcally, we analyze fMRI functional connectivity
of human subjects before and after they ingest the psychoactive brew Ayahuasca and report
an increase in the Shannon entropy. This is the ﬁrst time that the entropy of the functional
networks of the human brain has been directly measured in altered states of mind on a
global scale, i.e. considering the entire brain.
Ayahuasca is a beverage of Amazonian indigenous origin and has legal status in Brazil
in religious and scientiﬁc settings [15]. It contains the powerful psychedelic N, N- dimethyl-
tryptamine (DMT), together with harmala alkaloids that are known to be monoamine oxi-
dase inhibitors (MAOIs). The beverage is typically obtained by decoction of two plants from
the Amazonian ﬂora: the bush Psychotria viridis, that contains DMT, and the liana Baniste-
riopsis caapi, that contains MAOIs [16]. DMT is usually rapidly metabolized by monoamine
oxidase (MAO), but the presence of MAOI allows DMT to cross the blood-brain barrier and
2


## Page 3


to exert its eﬀects [17–22]. Similar to LSD, mescaline and psilocybin [17–22], Ayahuasca
can cause profound changes of perception and cognition, with users reporting increase of
awareness, ﬂexible thoughts, insights, disintegration of the self, and attentiveness [17, 23].
There is growing interest in Ayahuasca, partially due to recent ﬁndings showing that it
may be eﬀective in treating mental disorders, such as depression [24] and behavioral addic-
tion [25–27]. Similar therapeutic potential has also been pointed out for other psychedelics
[9, 21, 28–31].
For analysis we use tools and concepts from the ﬁeld of complex networks, a brief history
of which follows. The application of graph theory to phase transitions and complex systems
led to signiﬁcant progress in understanding a variety of cooperative phenomena over a period
of several decades. In the 1960s, the books by Harary, especially Graph Theory and Theo-
retical Physics [32], introduced readers to powerful mathematical techniques. The chapter
by Kastelyn, still considered to be a classic, showed that diﬃcult combinatorial problems
of exact enumeration could be attacked via graph theory, including the exact solution of
the two-dimensional Ising model (e.g., see Feynman [33]). In the 1980s, certain families
of neural network models were shown to be equivalent to Ising systems, e.g., the Hopﬁeld
network [34] is a content-addressable memory which is isomorphic to a generalized Ising
model [35]. Beginning in the 1990s, new approaches to networks, giving emphasis to concepts
such as the node degree distribution, clustering, assortativity, small-worldliness and network
eﬃciencies, led eventually to what has become the new ﬁeld of complex networks [36, 37].
These new tools and concepts [38–40] have found successful application in the study of
diverse phenomena, such as air transportation networks [41], terrorist networks [42], gene
regulatory networks [43], and functional brain networks [44–48]. We approach the human
brain from this perspective of complex networks [49, 50].
Ten healthy volunteers were submitted to two distinct scanning sessions: (i) before and
(ii) 40 minutes after Ayahuasca intake, when the subjective eﬀects are noticeable. In both
cases, participants were instructed to close their eyes and remain awake and at rest, without
performing any task. We performed a standard preprocessing on all samples of the fMRI
data (see Methods for details concerning data acquisition and preprocessing).
3


## Page 4


Data analysis consists of two main steps. In the ﬁrst step, we use fMRI data to generate
complex networks to represent the actual functional brain connectivity patterns. In the
second step, we use the networks generated in step 1 as inputs and calculate network
characteristics as output, using techniques from the theory of complex networks.
The
Methods section describes both steps in detail. More information about most of the methods
used here can be found in refs. [4, 51, 52]. Figure 1 shows the networks generated from one
subject before and after Ayahuasca intake, for one speciﬁc choice of mean node degree. The
spheres represent nodes, with sphere size proportional to the degree of the node. The lower
plots show histograms of node degrees.
The main result that we report here is an increase in the Shannon entropy of the degree
distribution for the functional brain networks subsequent to Ayahuasca ingestion. We also
ﬁnd that the geodesic distance increases during the eﬀects of Ayahuasca, i.e. qualitatively
the network becomes “larger.”
More generally, we also ﬁnd that these functional brain
networks become less connected globally but more connected locally.
The key technical innovation is the measurement of the Shannon entropy of the degree
distribution of the complex networks that represent the functional connectivity of the
human brain.
This novel use of the Shannon entropy allows the brain to be studied
from the perspective of information theory in a manner previously unexploited. Moreover,
the Shannon entropy is also very closely related to the Boltzmann-Gibbs entropy used
in statistical mechanics.
Hence, our approach to studying the brain experimentally is
grounded in two strong theoretical traditions: graph theory and complex networks on the
one hand, and information theory and statistical physics on the other.
Our study also
represents a signiﬁcant advance for the following additional reasons: (i) our results unveil
how Ayahuasca (and likely most other tryptamine psychedelics) alter brain function, both
locally and globally; (ii) it is the ﬁrst time that this speciﬁc approach has been applied
to characterize functional brain networks in altered states of consciousness; (iii) our study
of Ayahuasca covers all brain regions; and (vi) the method we have developed can be
immediately applied to study a variety of other phenomena (e.g., the eﬀects of medication
for mental health disorders).
4


## Page 5


RESULTS
Increase of the Shannon entropy of the degree distributions
We ﬁnd evidence of signiﬁcant changes in the functional brain networks of subjects before
and after ingestion of Ayahuasca. Figure 2 shows 2nd as well as 4th central moments of
the degree distributions for each subject. The individual values are calculated separately
for each network. We ﬁnd an increase of variance for all subjects after Ayahuasca intake
and a decrease of kurtosis for almost all of them (6 subjects). These ﬁndings indicate that
the degree distributions become less peaked and wider. This behavior is suggestive of an
increase of the Shannon entropy for the degree distributions after Ayahuasca ingestion.
Figure 3 shows the average Shannon entropy of the degree distributions as a function of
mean degree, considering networks from all subjects, before and after Ayahuasca intake. A
fair comparison of the “before” and “after” networks is possible by considering the entropy
of networks of identical mean degree. We ﬁnd an increase in the entropy of the degree
distributions after Ayahuasca ingestion. In order to better evaluate the consistency of this
result, we also calculate the average Shannon entropy subject-by-subject, before and after
Ayahuasca (Figure 4). We ﬁnd signiﬁcant increased entropy for all individual subjects.
Iso-entropic randomized networks
The degree distribution does not completely deﬁne a network, however it can have great
inﬂuence over other network properties. One can quantify this inﬂuence by comparing any
given network G to other networks chosen randomly from the ensemble of networks that have
exactly the same degree distribution. We refer to such networks as “randomized networks.”
By deﬁnition, all such randomized networks have the same entropy as the original network
G, i.e. they are iso-entropic to G.
An eﬃcient way of generating such randomized networks is the Maslov algorithm [53] (see
Methods). Whereas entropy is conserved by the Maslov algorithm, the clustering coeﬃcient,
geodesic distances and eﬃciencies are not. By comparing these non-conserved quantities
before and after randomization, we can distinguish eﬀects that are due solely to changes
in the degree distribution from those that are sensitive to how links are more speciﬁcally
arranged.
5


## Page 6


We generate a set of 30 iso-entropic randomized networks for each original network, for
all subjects both before and after Ayahuasca ingestion. Comparison of the original networks
with the randomized networks yields important information concerning to what degree the
changes in quantities such as geodesic distance, clustering coeﬃcients, and global and local
eﬃciencies can be accounted for by the changes in the degree distributions (see results
described below).
Decrease of global integration
Figure 5 shows an increase of mean geodesic distance and a decrease of global eﬃciency
after Ayahuasca ingestion. To determine how much of the change in geodesic distance is
due to the change in the degree distribution, we also calculated the geodesic distance and
global eﬃciency for the iso-entropic randomized networks. Note how the values for those
networks are quite diﬀerent compared to the non-randomized networks. We conclude that
the change in degree distribution cannot explain the entire change in geodesic distance. The
inset in the middle panels shows the change in the normalized mean geodesic distance and
global eﬃciency, which we deﬁne as the ratio D/Drand and similarly for the global eﬃciency
(see [4, 53]) . We see, indeed, that these ratios are not close to zero. If the change in degree
distribution could account for all the change in geodesic distance and eﬃciency, then the
change in these ratios would be close to zero. Signiﬁcant changes are also observed at the
individual level and are again consistent for all subjects (Figure 5 (e) and 5 (f)).
Increase of local integration
Figure 6 shows an increase of clustering coeﬃcients and local eﬃciency after Ayahuasca
ingestion.
In contrast to the behavior of the metrics discussed above, almost identical
changes are seen for iso-entropic networks. This result indicates that the variation in degree
distribution can account for most of the change in clustering and local eﬃciency. The insets
in the middle panel show the change in the normalized clustering and local eﬃciency, which
we deﬁne as the ratio C/Crand and similarly for the local eﬃciency (see [4, 53]). We see,
indeed, that these ratios are close to zero.
6


## Page 7


DISCUSSION
Our results reveal some remarkable ﬁndings, the most important of which is that the
entropy increases after Ayahuasca ingestion. The following also increase: geodesic distance,
clustering coeﬃcient and local eﬃciency. However, the global eﬃciency decreases. Overall,
we ﬁnd an increase of local integration and a decrease of global integration in the functional
brain networks.
We interpret these ﬁndings in the context of some well understood prototypical classes
of networks.
Regular lattices have ﬁxed coordination number, hence all nodes have the
same degree and the Shannon entropy of the degree distribution is thus zero. In contrast,
the entropy is high in networks with broad distributions of degree. In the context of the
Watts-Strogatz model [54], clustering and geodesic distance both decrease when highly
regular networks are transformed into small-world networks by randomly re-assigning the
links. Whereas clustering and geodesic distances decrease with increasing randomness in
such models, we ﬁnd the opposite behavior for Ayahuasca, i.e., randomness as measured by
the Shannon entropy of the node degree distribution increases in parallel with clustering
and geodesic distances. Hence, our ﬁndings cannot be reduced to simple explanations of
greater or lesser randomness. Locally, there is an increase in integration (as measured by
network eﬃciency), but globally there is a decrease in integration.
Indeed the increase
of geodesic distance and decrease of global eﬃciency after Ayahuasca intake signify that
the functional brain networks are less globally integrated. One possible interpretation of
these ﬁndings is that the increase of local robustness and the decrease of global integration
reﬂect a variation in modular structure of the network.
Recent studies have reported
the presence of modularity in functional brain networks on several scales [48, 55, 56].
Modular networks are characterized by the existence of reasonably well-deﬁned subnetworks
in which internal connections are denser than connections between distinct subnetworks
[48]. However, traditional algorithms [57–59] were not able to detect variation on modular
structure features between our sets of networks.
Our results are broadly consistent with the entropic brain hypothesis, hence we discuss
the latter in the context of our ﬁndings. The hypothesis maintains that the mental state
induced by psychedelics, which the original authors term “primary-state,” presents relatively
elevated entropy in some features of brain organization, compared to the ordinary waking
7


## Page 8


state (termed “secondary”) [11]. Although it may be somewhat counter-intuitive that the
psychedelic state is considered primary while ordinary consciousness is secondary, their
hypothesis is inherently plausible considering that a wider spectrum of experiences is possible
with psychedelics than in ordinary consciousness. In this sense, ordinary consciousness can
be thought of as a restriction or constrained special case of a more primary consciousness.
The hypothesized lower entropy of ordinary consciousness relative to primary consciousness
is attributed to this reduction of freedom. In fact, the idea that ordinary consciousness is not
primary was previously put forth by Alan Watts to describe what later became widely known
as mindfulness [60] Indeed, it is possible to interpret the eﬀects of Ayahuasca, and other
psychedelics, as being due to the temporary removal of the some of the restrictions that are
necessary for sustaining ordinary (adult trained) consciousness. Without these restrictions,
the mind reverts to the more ﬂexible state, in which self-referential narratives and thoughts
about the past or the future are no longer experienced as identical to the reality that they
are assumed to represent [60].
Relatively few studies have investigated entropy in brain functional networks, hence
additional comments are in order. Tagliazucchi et al. [14] showed that psilocybin (psychedelic
present in some species of mushrooms) may be responsible for increases of a diﬀerent entropy
measure in functional connectivity of the 4 regions of Default Mode Network (DMN), a
relevant functional network related to resting state. Recently, Yao et al. [61] correlated
entropy increases in the human brain with age. This study also supports the view that
entropy is correlated to brain function (and perhaps also its development). Moreover, in
agreement with our results, a study by Schroter et al. [4] similarly suggests that functional
network topology may have a central role in consciousness quality. They investigated the
eﬀects on the human brain of the anesthetic propofol, which can induce loss of consciousness
[62]. They reported a decrease of the clustering coeﬃcient, which is strongly inﬂuenced by
degree distribution (however, geodesic distance remained unchanged).
We brieﬂy comment on the limitations of our method: (i) the reduced number of subjects
and the fact that all of them were experienced with Ayahuasca do not allow population
inferences and do not elucidate whether the eﬀects observed here were only due the acute
administration or if previous experience also played a signiﬁcant role; (ii) expectancy and
suggestion were not controlled, as placebo was not used; (iii) networks were built upon a
number of critical choices, such as the atlas used to partition the brain, the method used to
8


## Page 9


build the correlation matrix, and the cutoﬀthresholds for generating the adjacency matrices
from correlation matrices [63, 64], which may aﬀect the ﬁnal results; (iv) the chosen range
of correlation values automatically limits the networks’ behavior to a small-world network.
Despite this limitation, it is important to highlight that several studies have consistently
demonstrated that brain networks exhibit a small-world behavior [65].
Finally, we speculate about whether or not our ﬁnding of larger mean geodesic distances
may have any relation to self-reports of “mind-expansion” by users of psychedelics. Could
there be a direct relation between entropy increases and the higher creativity reported
by users of psychedelics? Such questions merit further investigation. In conclusion, our
results are broadly consistent with the hypothesis that psychedelics increase the entropy in
brain functions. By calculating the Shannon entropy of the degree distribution of complex
networks generated from fMRI data, we have taken a new low-computational-cost approach
to investigating brain function under the inﬂuence of psychedelics.
METHODS
Data acquisition and preprocessing
The fMRI images were obtained in a 1.5 T scanner (Siemens, Magneton Vision), using an
EPI-BOLD like sequence comprising 150 volumes, with the following parameters: TR=1700
ms; TE=66 ms; FOV=220 mm; matrix 64×64; voxel dimensions of 1.72mm×1.72mm×1.72
mm. It also was acquired whole brain high resolution T1-weighted images (156 contiguous
sagittal slices) using a multiplanar reconstructed gradient-echo sequence, with the following
parameters: TR=9.7 ms; TE=44 ms; ﬂip angle 12◦; matrix 256×256; FOV= 256 mm,
voxel size= 1mm × 1mm × 1mm. The images were obtained from 10 healthy right-handed
adult volunteers (mean age 31.3, from 24 to 47 years), all who were experienced users of
Ayahuasca with at least 5 years use (twice a month) and at least 8 years of formal education.
The experimental procedure was approved by the Ethics and Research Committee of the
University of S˜ao Paulo at Ribeir˜ao Preto (process number 14672/2006). Written informed
consent was obtained from all volunteers, who belonged to the Santo Daime religious
organization.
Volunteers were not under medication for at least 3 months prior to the scanning session
9


## Page 10


and were abstinent from caﬀeine, nicotine and alcohol prior to the acquisition. They had no
history of neurological or psychiatric disorders, as assessed by DSM-IV structured interview
[66]. Subjects ingested 120-200 mL (2.2 mL/kg of body weight) of Ayahuasca known to
contain 0.8 mg/mL of DMT and 0.21 mg/mL of harmine. Harmaline was not detected via
the chromatography analysis, at the threshold of 0.02 mg/mL [7]. preprocessing steps were
conducted in FSL (http://www.ndcn.ox.ac.uk/divisions/fmrib) and include: slice-timing
correction, head motion correction and spatial smoothing (Gaussian kernel, FWHM = 5
mm). One volunteer was excluded from analysis due to excessive head movement (more
than 3mm in some direction), leaving 9 participants (5 women) to our analysis. All images
were spatially normalized to the Montreal Neurologic Institute (MNI152) [67] standard space,
using a linear transformation. We also evaluated 9 regressors of non-interest using a General
Linear Model (GLM): 6 regressors to movement correction, 1 to white matter signal, 1 to
cerebrospinal ﬂuid and 1 to global signal. Each volunteer was submitted to fMRI scanning
under two distinct conditions: (i) before and (ii) 40 minutes subsequent to Ayahuasca intake.
In both cases, volunteers were in an awake resting state: they were requested to stay lying
with eyes closed, without performing any task. One volunteer sample was excluded from
analysis due to excessive head movement, leaving 9 participants (5 women) to our analysis.
Complex network metrics
For a detailed overview of complex network theory, we refer readers to refs. [36, 39, 47].
Each element of a network is known as a node (or vertex), and the relation between a pair of
nodes is represented by a connecting link (or edge). Links can have weights associated with
them and can be directed or undirected (or, equivalently bi-directional). Nodes connected
by a single link are known as nearest neighbors [37]. Non-weighted undirected networks, i.e.
those with symmetric and unweighted links are isomorphic to a binary symmetric matrix
known as the adjacency matrix. When a pair of nodes i and j are neighbors, the adjacency
matrix element is ai,j = 1 and ai,j = 0 otherwise. Standard quantities of interest that help to
characterize the topology and complexity of networks [47, 51] include node degree, geodesic
distance, clustering coeﬃcient, and local and global network eﬃciencies.
Deﬁnitions:
(i) The degree kj of a node j is the number of links that it has with other nodes. The
10


## Page 11


degree distribution of a network is the normalized histogram of degrees over all nodes.
(ii) A geodesic path between two nodes is the shortest path from one to the other,
assuming such a path exists. The geodesic distance di,j between nodes i and j is the number
of links in the geodesic path. If there is no such path, the geodesic distance is deﬁned as
inﬁnite. Given a network G with N nodes, the mean geodesic distance is given by
D(G) =
1
N(N −1)
X
i̸=j
di,j .
(1)
(iii) The clustering coeﬃcient quantiﬁes the density of triads of linked nodes, e.g., the
fraction of the neighbors of a node that are themselves neighbors. The clustering coeﬃcient
is deﬁned by
C(G) = 1
N
X
i̸=j̸=h
2
ki(ki −1) ai,jaj,hah,i ,
(2)
where ki is the degree of node i and a is the adjacency matrix element.
(iv) The eﬃciency, typically deﬁned as the reciprocal of the harmonic mean of geodesic
distances, quantiﬁes the inﬂuence of the topology on ﬂux of information through the network.
Eﬃciency can be global as well as local. We deﬁne global eﬃciency as
Eg(G) =
1
N(N −1)
X
i̸=j∈G
1
di,j
,
(3)
and local eﬃciency as
El(G) = 1
N
X
i∈G

1
ni(ni −1)
X
j̸=h∈gi
1
dh,j

,
(4)
where gi are the subnetworks formed by neighbors of node i and ni is the number of nodes
of this subnetwork [68].
In addition to these standard network properties, we also use the Shannon entropy [69] to
quantify disorder or uncertainty. Speciﬁcally, we calculate the Shannon entropy functional of
the distribution of node degrees. Let P be the normalized probability distribution for node
degree k, i.e. P
k P(k) = 1. We deﬁne the Shannon entropy S[P] of the degree distribution
P(k) for a network with N nodes by:
S[P] = −
X
k
P(k) log P(k) .
(5)
Often the logarithm of base 2 is used [70] (e.g., in computer science), but we use the natural
logarithm instead, so the entropy values shown are in natural information units rather than
in bits.
11


## Page 12


Maslov algorithm for generating randomized networks
Given G, one can select two non-overlapping pairs (i, j) and (m, n) of linked nodes,
then unlink them, and cross-link the pairs according to (i, m) and (j, n). If this process is
repeated many times, the links become randomized, but the degree of each node remains
the same [53]. Hence the entropy of the degree distribution is also a conserved quantity.
Calculation of correlation matrix for brain regions
We segmented the brain images into 110 brain regions according to the Harvard-Oxford
cortical and subcortical structural atlas (threshold of > 25%, using FMRIB Software Library,
www.fmrib.ox.ac.uk/fsl). Six regions had to be excluded from further analysis, as they were
not sampled for all subjects, due to technical limitations during image acquisition. For each
of the 104 regions, an averaged fMRI time series was computed from all voxels (a voxel
is a 3D image block, analogous to the 2D pixel). within that region using Marsbar (SPM
toolbox). To reduce confounders, we applied a band-pass ﬁlter (≈0.03 −0.07 Hz) using the
maximum overlap wavelet transform (MODWT) with a Daubechies wavelet to divide the
signal into 4 scales of diﬀerent frequency bands. In keeping with the literature [4, 52], that
point that resting state typically leads to low frequency (≈0.01 to 0.1 Hz) [71], we choose
scale 3. We then calculated the Pearson correlation between these wavelet coeﬃcients from
all possible pairs, thus obtaining a 104×104 correlation matrix to represent each sample.
Only correlations with p < 0.05 were considered.
Construction of complex networks from fMRI images
A correlation matrix uniquely deﬁnes a weighted network. Nonetheless, we are interested
in generating non-weighted networks.
Hence, we need a function that maps correlation
matrices to adjacency matrices. We use a thresholding function for this purpose. Given a
correlation matrix, we obtain the adjacency matrix by applying a threshold to the absolute
value of the elements of the correlation matrix. Speciﬁcally, if the absolute value of the
correlation matrix element |ci,j| is larger than a deﬁned threshold η, then a link is assumed
and the adjacency matrix element is taken to be 1 (i.e., ai,j = 1), while otherwise there is
no link (ai,j = 0). In order to obtain better statistics, we choose not a single value of η but
12


## Page 13


a range of values instead. Then we analyze the behavior of the network properties over this
range. Using this approach, we create a number of networks for each fMRI sample, all with
the same number of nodes (104 nodes). For each of these networks, we choose η such that
the density of links is the same before and after Ayahuasca intake.
We choose a range for the mean network degree to ensure the networks were fully
connected but also sparse (to avoid random network behavior).
For this purpose, we
adopt the following criteria: the network must have lower global eﬃciency and greater
local eﬃciency than its randomized version. These criteria also ensure small-world behavior
of the networks [72] (according to the deﬁnition of Watts and Strogatz [54]). In order to
obtain the same threshold range for all subjects, it is necessary to exclude two of them from
the analysis, since there is no threshold range common between them and the other subjects.
Data from a second subject was also excluded due to excessive head movement. Following
the criteria described above, the threshold range is set to 0.28 ≤η ≤0.37. We generate
networks with mean degree in the range 24 ≤⟨k⟩≤39. We evaluate measures in degree
increments of ∆⟨k⟩= 1, thus obtaining 16 diﬀerent values of mean degree.
In summary, we have 7 human subjects suitable for both conditions (before and after
ingestion). The resulting sets of networks allow 16 diﬀerent comparisons (i.e. of diﬀering
mean degrees) for each subject before and after Ayahuasca ingestion.
We calculate the
topological measurements (using the Brain Connectivity Toolbox for Matlab [47]).
Statistical testing
Comparisons between the two conditions (i.e., before and after Ayahuasca) are obtained
from paired-sample Student’s t-tests.
The p-values shown in some of the ﬁgures are as
follows: values p < 0.05 in bold and p < 0.005 indicated by asterisks (*). The implicitly
assumed null hypothesis is that the diﬀerence of the paired values are normally distributed
with zero mean.
13


## Page 14


REFERENCES
[1] Buxton, R. Introduction to Functional Magnetic Resonance Imaging: Principles and Tech-
niques (Cambridge University Press, 2009).
[2] Heeger, D. J. & Ress, D. What does fMRI tell us about neuronal activity? Nature reviews.
Neuroscience 3, 142–151 (2002).
[3] Schrouﬀ, J. et al.
Brain functional integration decreases during propofol-induced loss of
consciousness. NeuroImage 57, 198–205 (2011).
[4] Schroter, M. S. et al.
Spatiotemporal Reconﬁguration of Large-Scale Brain Functional
Networks during Propofol-Induced Loss of Consciousness.
Journal of Neuroscience 32,
12832–12840 (2012).
[5] Noirhomme, Q. et al. Brain Connectivity in Pathological and Pharmacological Coma. Fron-
tiers in Systems Neuroscience 4, 160 (2010).
[6] Andrade, K. C. et al. Sleep spindles and hippocampal functional connectivity in human NREM
sleep. The Journal of Neuroscience 31, 10331–10339 (2011).
[7] De Araujo, D. B. et al. Seeing with the eyes shut: Neural basis of enhanced imagery following
ayahuasca ingestion. Human Brain Mapping 33, 2550–2560 (2012).
[8] Carhart-Harris, R. L. et al. Neural correlates of the psychedelic state as determined by fMRI
studies with psilocybin. Proceedings of the National Academy of Sciences 109, 1–6 (2012).
[9] Carhart-Harris, R. L. et al. Neural correlates of the LSD experience revealed by multimodal
neuroimaging. Proceedings of the National Academy of Sciences (2016).
[10] Palhano-Fontes, F. et al. The Psychedelic State Induced by Ayahuasca modulates the activity
and connectivity of the Default Mode Network. PloS one 10(2), 1–13 (2014).
[11] Carhart-Harris, R. L. et al. The entropic brain: a theory of conscious states informed by
neuroimaging research with psychedelic drugs. Frontiers in human neuroscience 8, 20 (2014).
[12] Sarasso, S. et al. Consciousness and Complexity during Unresponsiveness Induced by Propofol,
Xenon, and Ketamine. Current Biology 25, 3099–3105 (2016).
[13] Petri, G. et al. Homological scaﬀolds of brain functional networks. Journal of The Royal
Society Interface 11, 101 (2014).
[14] Tagliazucchi, E., Carhart-Harris, R., Leech, R., Nutt, D. & Chialvo, D. R. Enhanced repertoire
of brain dynamical states during the psychedelic experience.
Human Brain Mapping 35,
14


## Page 15


5442–5456 (2014).
[15] Labate, B. C. & Cavnar, C. Prohibition, Religious Freedom, and Human Rights: Regulating
Traditional Drug Use (Springer-Verlag, 2014).
[16] McKenna, D. J. Clinical investigations of the therapeutic potential of ayahuasca: Rationale
and regulatory challenges. Pharmacology and Therapeutics 102, 111–129 (2004).
[17] Shanon, B. The Antipodes of the Mind: Charting the Phenomenology of the Ayahuasca Expe-
rience (Oxford University Press, 2002).
[18] Huxley, A. The Doors of Perception and Heaven and Hell. Harper Perennial modern classics
(HarperCollins, 2004).
[19] Hofmann, A. LSD, my problem child: reﬂections on sacred drugs, mysticism, and science
(J.P. Tarcher, 1983).
[20] Hollister, L. E. & Hartman, A. M.
Mescaline, lysergic acid diethylamide and psilocybin:
Comparison of clinical syndromes, eﬀects on color perception and biochemical measures. Com-
prehensive Psychiatry 3, 235–241 (1962).
[21] Grof, S. LSD psychotherapy (Hunter House, 1980).
[22] Griﬃths, R. R., Richards, W. A., McCann, U. & Jesse, R.
Psilocybin can occasion
mystical-type experiences having substantial and sustained personal meaning and spiritual
signiﬁcance. Psychopharmacology 187, 268–283 (2006).
[23] Riba, J. et al. Subjective eﬀects and tolerability of the South American psychoactive beverage
Ayahuasca in healthy volunteers. Psychopharmacology 154, 85–95 (2001).
[24] Sanches, R. F. et al. Antidepressant Eﬀects of a Single Dose of Ayahuasca in Patients With
Recurrent Depression: A SPECT Study. Journal of clinical psychopharmacology 36, 77 (2016).
[25] Osorio, F. L. et al.
Antidepressant eﬀects of a single dose of ayahuasca in patients with
recurrent depression: a preliminary report. Revista Brasileira de Psiquiatria 37, 13–20 (2015).
[26] Labate, B. C. & Cavnar, C. The Therapeutic Use of Ayahuasca (Springer-Verlag, 2013).
[27] Nunes, A. A. et al. Eﬀects of Ayahuasca and its Alkaloids on Drug Dependence: A Systematic
Literature Review of Quantitative Studies in Animals and Humans. Journal of Psychoactive
Drugs 48, 195–205 (2016).
[28] Krebs, T. S. & Johansen, P. Lysergic acid diethylamide (LSD) for alcoholism: meta-analysis
of randomized controlled trials. Journal of Psychopharmacology 26, 994–1002 (2012).
15


## Page 16


[29] Johnson, M. W., Garcia-Romeu, A., Cosimano, M. P. & Griﬃths, R. R. Pilot study of the
5-HT2AR agonist psilocybin in the treatment of tobacco addiction. Journal of Psychophar-
macology (2014).
[30] Albaugh, B. J. & Anderson, P. O. Peyote in the treatment of alcoholism among American
Indians. American journal of Psychiatry 131, 1247–1250 (1974).
[31] Frederking, W. Intoxicant drugs (mescaline and lysergic acid diethylamide) in psychotherapy.
The Journal of nervous and mental disease 121, 262–266 (1955).
[32] Harary, F. Graph Theory and Theoretical Physics (Acad. Press, 1967).
[33] Feynman, R. P. Statistical Mechanics: A Set Of Lectures. Advanced Books Classics Series
(Westview Press, 1998).
[34] Hopﬁeld, J. J. Neural networks and physical systems with emergent collective computational
abilities. Proceedings of the National Academy of Sciences of the United States of America
79, 2554–2558 (1982).
[35] Amit, D. J. Modeling Brain Function: The World of Attractor Neural Networks (Cambridge
University Press, 1992).
[36] Barabasi, A. L. Linked: The New Science of Networks (Perseus Pub., 2002).
[37] Newman, M. E. J. Networks: An Introduction (Oxford University Press, 2010).
[38] Albert, R. & Barab´asi, A. L. Statistical mechanics of complex networks. Rev. Mod. Phys. 74,
47–97 (2002).
[39] Bornholdt, S. Schuster, H. G. Handbook of Graphs and Networks: From the Genome to
the Internet. In Handbook of graphs and networks: From the Genome to the Internet (ed. S.
Bornholdt and H. G. Schuster), 1–401 (2003).
[40] Caldarelli, G. Scale-Free Networks: Complex Webs in Nature and Technology. Oxford Finance
Series (Oxford University Press, 2013).
[41] Verma, T., Araujo, N. A. M. & Herrmann, H. J. Revealing the structure of the world airline
network. Scientiﬁc Reports 4, 5638 (2014).
[42] Battiston, F., Nicosia, V. & Latora, V. Structural measures for multiplex networks. Physical
Review E 89, 32804 (2014).
[43] Magtanong, L. et al.
Dosage suppression genetic interaction networks enhance functional
wiring diagrams of the cell. Nature Biotech. 29, 505–511 (2011).
[44] Sporns, O. Networks of the Brain (MIT Press, 2016).
16


## Page 17


[45] Bullmore, E. & Sporns, O. Complex brain networks: graph theoretical analysis of structural
and functional systems. Nature Review Neuroscience 10, 186–198 (2009).
[46] McKenna, T. M., McMullen, T. A. & Shlesinger, M. F. The brain as a dynamic physical
system. Neuroscience 60, 587–605 (1994).
[47] Rubinov, M. & Sporns, O.
Complex network measures of brain connectivity: Uses and
interpretations. NeuroImage 52, 1059–1069 (2010).
[48] Meunier, D., Lambiotte, R. & Bullmore, E. T.
Modular and hierarchically modular
organization of brain networks. Frontiers in Neuroscience 4, 1–11 (2010).
[49] Mainzer, K. Complex Systems and the Evolution of Mind–Brain. In Thinking in Complexity:
The Computional Dynamics of Matter, Mind and Mankind, 123–178 (Springer-Verlag, 2007).
[50] Telesford, Q. K., Simpson, S. L., Burdette, J. H., Hayasaka, S. & Laurienti, P. J. The Brain
as a Complex System: Using Network Science as a Tool for Understanding the Brain. Brain
Connectivity 1, 295–308 (2011).
[51] Onias, H. et al. Brain complex network analysis by means of resting state fMRI and graph
analysis: Will it be helpful in clinical epilepsy? Epilepsy & Behavior 38, 71–80 (2014).
[52] Liu, Y. et al. Disrupted small-world networks in schizophrenia. Brain 131, 945–961 (2008).
[53] Maslov, S. & Sneppen, K. Speciﬁcity and Stability in Topology of Protein Networks. Science
296, 910–913 (2002).
[54] Watts, D. J. & Strogatz, S. H. Collective dynamics of ‘small-world’ networks. Nature 393,
440–442 (1998).
[55] Ferrarini, L. et al. Hierarchical functional modularity in the resting-state human brain. Human
Brain Mapping 30, 2220–2231 (2009).
[56] Nicolini, C. & Bifone, A.
Modular structure of brain functional networks: breaking the
resolution limit by Surprise. Scientiﬁc Reports 6, 19250 (2016).
[57] Newman, M. E. J. & Girvan, M. Finding and evaluating community structure in networks.
Physical Review E 69, 026113 (2004).
[58] Guimera, R. & Nunes Amaral, L. A. Functional cartography of complex metabolic networks.
Nature 433, 895–900 (2005).
[59] Blondel, V. D., Guillaume, J.-L., Lambiotte, R. & Lefebvre, E. Fast unfolding of communities
in large networks. Journal of Statistical Mechanics: Theory and Experiment 10008, 6 (2008).
[60] Watts, A. W. The Wisdom of Insecurity (Knopf Doubleday Publishing Group, 2011).
17


## Page 18


[61] Yao, Y. et al. The Increase of the Functional Entropy of the Human Brain with Age. Scientiﬁc
Reports 3, 2853 (2013).
[62] Sarasso, S. et al. Consciousness and Complexity during Unresponsiveness Induced by Propofol,
Xenon, and Ketamine. CURBIO 25, 3099–3105 (2015).
[63] Smith, S. M. The future of FMRI connectivity. NeuroImage 62, 1257–1266 (2012).
[64] Langer, N., Pedroni, A. & J¨ancke, L. The Problem of Thresholding in Small-World Network
Analysis. PLoS ONE 8, 1–9 (2013).
[65] Bassett, D. S. & Bullmore, E. Small-world brain networks. The Neuroscientist : a review
journal bringing neurobiology, neurology and psychiatry 12, 512–523 (2006).
[66] Association, A. P. & on DSM-IV., A. P. A. T. F. Diagnostic and Statistical Manual of Mental
Disorders: DSM-IV-TR. Diagnostic and Statistical Manual of Mental Disorders: DSM-IV-TR
(American Psychiatric Association, 2000).
[67] Brett, M., Johnsrude, I. S. & Owen, A. M. The problem of functional localization in the
human brain. Nature Review Neuroscience 3, 243–249 (2002).
[68] Latora, V. & Marchiori, M. Eﬃcient behavior of small-world networks. Phys. Rev. Lett. 87,
198701 (2001).
[69] Shannon, C. A mathematical theory of communication. Bell System Technology Journal 27,
379:423, 623–656 (1948).
[70] Cover, T. M. & Thomas, J. A.
Elements Of Information Theory Notes.
Wiley Series in
Telecommunications and Signal Processing (Wiley, 2006).
[71] Fransson, P. Spontaneous low-frequency BOLD signal ﬂuctuations: An fMRI investigation of
the resting-state default mode of brain function hypothesis. Human Brain Mapping 26, 15–29
(2005).
[72] Achard, S. & Bullmore, E. Eﬃciency and cost of economical brain functional networks. PLoS
Computational Biology 3, 0174–0183 (2007).
18


## Page 19


ACKNOWLEDGEMENTS
We thank Santo Daime members for volunteering and for providing the Ayahuasca. We
thank Sidarta Ribeiro for discussions, Jos´e C. Cressoni, Marco A. A. da Silva, and Carlos Viol
for feedback and CAPES and CNPq for funding. AV thanks UFV and Science without
Borders (CAPES Grant No. 88881.030375/2013-01) for funding and Guillermo Cecchi and
Irina Rish for their hospitality and discussions during her year at IBM.
AUTHOR CONTRIBUTIONS
D.B.A. recruited the volunteers for data acquisition and conceived the study.
A.V.,
F.P.-F. and H.O performed fMRI data preprocessing, complex network construction and
evaluated standard network features. A.V. and G.M.V. performed complex network analysis
and statistical analysis. All authors contributed equally to the ﬁnal overall design of the
study.
COMPETING FINANCIAL INTERESTS
The authors declare no competing ﬁnancial interests.
19


## Page 20


(a)
Before
After
(b)
Figure 1. Illustrative example of functional brain networks. (a) 3 views of a complex
network generated from brain fMRI data of one of the subjects, before (left) and after (right)
Ayahuasca ingestion (mean node degree ⟨k⟩= 30). The spheres represent nodes and sphere size is
proportional to the node degree. (b) histograms of the node degrees, corresponding to the networks
shown in (a). After Ayahuasca intake, the distribution is wider, indicating a higher entropy. In
(a) we have used the BrainNet Viewer (http://www.nitrc.org/projects/bnv) for visualization.
20


## Page 21


(a)
(b)
Figure 2. Variance and kurtosis of the degree distribution. Mean ± 1 standard deviation
calculated over all 16 networks of the degree variance (a) and kurtosis (b), shown for each subject
(blue ▽) and after (green △) Ayahuasca ingestion. The individual values for the degree variance
and kurtosis are calculated separately for each network. We ﬁnd higher variance and (mostly) lower
kurtosis after Ayahuasca, hence the node distributions change shape and become less “peaked.”
Such behavior is again consistent with (if not suggestive of) a higher Shannon entropy after
Ayahuasca.
21


## Page 22


Figure 3. Entropy grows after Ayahuasca ingestion. Mean ± 1 standard deviation of the
Shannon entropy of the distribution of node degrees, calculated over all 7 subjects, as a function
of mean degree k, before (blue ▽) and after (green △) Ayahuasca intake. The bottom row lists
p-values for Student’s paired t-test, with values p < 0.005 indicated by asterisks (*). We thus see
evidence against the null hypothesis of no change in entropy. Indeed, we ﬁnd a signiﬁcant increase
in the entropy of the degree distributions after Ayahuasca ingestion. This entropy increase is the
main result that we report.
22


## Page 23


(a)
(b)
Figure 4. Entropy growth per subject. (a) Boxplot of the entropy distribution and before
(B) and after (A) Ayahuasca ingestion and (b) boxplot of entropy increase, for all 7 subjects. Note
the signiﬁcant increase in entropy after Ayahuasca ingestion. There are 16 values of entropy per
subject, as discussed in the text. The bars show minimum and maximum values and the box shows
the 2nd and 3th quartiles, with the median shown dividing the box (in red). The asterisks (*)
in the bottom rows in both plots indicate p-values p < 0.005 for Student’s paired t-test in (a)
and t-test for zero mean in (b). Subject-by-subject, we thus ﬁnd strong evidence against the null
hypothesis of no entropy change.
23


## Page 24


(a)
(b)
(c)
(d)
(e)
(f)
Figure 5. (See next page for caption.)
24


## Page 25


Figure 5. Global eﬃciency and integration decrease. Geodesic distance D (left column)
and global eﬃciency Eg (right column). Plots (a) and (b) show means ± 1 standard deviations,
calculated from the complex networks of all 7 subjects, as well as from their corresponding
iso-entropic randomized networks, for 16 diﬀerent mean degrees. Plots (c) and (d) show the change
in D and Eg after Ayahuasca ingestion. The inset shows normalized values (see text). Boxplots
(e) and (f) show the same information, subject-by-subject. As in previous ﬁgures, the rows below
the plots show p-values for the t-test, with asterisks (*) indicating p < 0.005.
25


## Page 26


(a)
(b)
(c)
(d)
(e)
(f)
Figure 6. (See next page for caption.)
26


## Page 27


Figure 6.
Local eﬃciency and integration increase. Clustering coeﬃcient C (right column)
and local eﬃciency El (left column).
Plots (a) and (b) show means ± 1 standard deviations,
calculated from the complex networks of all 7 subjects, as well as from their corresponding
iso-entropic randomized networks, for 16 diﬀerent mean degrees. Plots (c) and (d) show the change
in C and El after Ayahuasca ingestion. The inset shows normalized values (see text). Boxplots (e)
and (f) show the same information, subject-by-subject. As before, the rows below the plots show
p-values for the t-test, with asterisks (*) indicating p < 0.005.
27

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]