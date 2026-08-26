---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1809.10301v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1809.10301v1_Characterizing_complex_networks_using_Entropy-degree_diagrams__unveiling_changes

> Source: 1809.10301v1_Characterizing_complex_networks_using_Entropy-degree_diagrams__unveiling_changes.pdf

> Pages: 21

---


## Page 1


Characterizing complex networks using Entropy-degree diagrams:
unveiling changes in functional brain connectivity
induced by Ayahuasca
A. Viol,1, 2, ∗Fernanda Palhano-Fontes,3 Heloisa Onias,3 Draulio
B. de Araujo,3 Philipp H¨ovel,4, 2 and G. M. Viswanathan5, 6, †
1Institute of Theoretical Physics, Technische Universit¨at,
Berlin, Hardenbergstraße 36, 10623 Berlin, Germany
2Bernstein Center for Computational Neuroscience Berlin,
Humboldt-Universit¨at zu Berlin, Philippstraße 13, 10115 Berlin, Germany
3Brain Institute, Universidade Federal do Rio Grande do Norte, 59078-970 Natal–RN, Brazil
4School of Mathematical Sciences, University College Cork, Western Road, Cork, Ireland
5Department of Physics, Universidade Federal do
Rio Grande do Norte, 59078-970 Natal–RN, Brazil
6National Institute of Science and Technology of Complex Systems
Universidade Federal do Rio Grande do Norte, 59078-970 Natal–RN, Brazil
(Dated: September 28, 2018)
1
arXiv:1809.10301v1  [q-bio.NC]  26 Sep 2018


## Page 2


Abstract
Open problems abound in the theory of complex networks, which has found successful applica-
tion to diverse ﬁelds of science. With the aim of further advancing the understanding of the brain’s
functional connectivity, we propose to evaluate a network metric which we term the geodesic en-
tropy. This entropy, in a way that can be made precise, quantiﬁes the Shannon entropy of the
distance distribution to a speciﬁc node from all other nodes. Measurements of geodesic entropy
allow for the characterization of the structural information of a network that takes into account
the distinct role of each node into the network topology. The measurement and characterization
of this structural information has the potential to greatly improve our understanding of sustained
activity and other emergent behaviors in networks, such as self-organized criticality sometimes seen
in such contexts. We apply these concepts and methods to study the eﬀects of how the psychedelic
Ayahuasca aﬀects the functional connectivity of the human brain. We show that the geodesic
entropy is able to diﬀerentiate the functional networks of the human brain in two diﬀerent states of
consciousness in the resting state: (i) the ordinary waking state and (ii) a state altered by ingestion
of the Ayahuasca. The entropy of the nodes of brain networks from subjects under the inﬂuence
of Ayahuasca diverge signiﬁcantly from those of the ordinary waking state. The functional brain
networks from subjects in the altered state have, on average, a larger geodesic entropy compared
to the ordinary state. We conclude that geodesic entropy is a useful tool for analyzing complex
networks and discuss how and why it may bring even further valuable insights into the study of
the human brain and other empirical networks.
∗aline.viol@bccn-berlin.de
† gandhi@ﬁsica.ufrn.br
2


## Page 3


I.
INTRODUCTION
In the last few decades, new scientiﬁc ﬁelds have taken advantages of complex network
approaches. This interest emerged, in part, by virtue of technological advances that gen-
erate new datasets in computational, social, biological, among others sciences. Examples
include modern brain mapping techniques, such as functional magnetic resonance imaging
(fMRI), that have provided previously inaccessible information about interaction patterns
in the human brain [1]. The theory of complex networks has proven to be a crucial tool to
understand the interactions and dynamics in large systems.
Attempts to characterize those new datasets bring up the challenge of extracting relevant
features regarding the network’s structure. One of the main concerns is to identify the role
of each node in the network and how the nodes cooperate to give rise to emergent behaviors.
The majority of measurements that have been proposed in the last few decades allow the
ranking of nodes’ importance by the number of connections, centrality, etc. [2–4].
Instead of ranking a node’s relative importance, we ask how the nodes contribute locally to
the global connectivity of the network, with the aim of better understanding the individualize
role played by each node in the network. We quantitatively describe these roles, as well as
the structural information of the diversity of interactions between nodes. The nodes in a
network interact with their neighbors and, indirectly, with the neighbors of neighbors; and
also with more distant nodes with even greater “neighborhood radius” (Figure 1).
We aim to quantify the diversity of inﬂuences on a given node, of all other nodes over the
whole network. For each node, we calculate the Shannon entropy functional [5] of the prob-
ability distribution of the geodesic distances between each node and all other nodes. We call
this measurement geodesic entropy. Nodes with a great diversity of inﬂuences (i.e., with high
geodesic entropy) may play an important role in, for example, to guarantee specialization
of functional patterns. Besides, nodes with a low diversity of inﬂuences may guarantee con-
straints relevant to network robustness. The “ﬁne tuning” of the distribution of distances,
quantiﬁed by the Shannon entropy, may be a key to understanding how emergent behaviors
arize.
We illustrate and apply our method to real network data. We use the geodesic entropy to
analyze human brain functional networks under the inﬂuence of the psychedelic Ayahuasca
– a brew from the Amazonian indigenous cultures that contains the serotonergic psychedelic
3


## Page 4


N, N-Dimethyltryptamine (DMT) and monoamine oxidase inhibitors (MAOi) [6].
Ayahuasca ingestion may cause deep changes in the cognition and perceptions, promoting
substantial alterations in the sense of the reality and the self [7, 8]. According to the neural
correlate hypothesis, we expect to ﬁnd features on functional brain networks that can be
correlated to this speciﬁc consciousness state. We evaluate the networks extracted from
fMRI data acquired from the same group of subjects in two sections: before and 40 minutes
after Ayahuasca intake.
The geodesic entropy is able to identify a speciﬁc behavior for
networks related to the psychedelic state of consciousness: the nodes of functional brain
networks under Ayahuasca eﬀects tend to have a greater geodesic entropy than the ordinary
condition.
II.
METHODS
A complex network is a schematic representation of the relations (links) between elements
(nodes) of a system with a nontrivial topology of interactions [9, 10].
Consider a non-
weighted undirected network G(ν, ξ), where ν is a set with N nodes and ξ is the set of links.
It is represented numerically by a N ×N adjacency matrix Ai,j: if a pair of nodes i and j are
connected, the matrix element is Ai,j = 1 and Ai,j = 0 otherwise. The nodes are connected if
the elements that they represent share some kind of information or have mutual inﬂuences.
The number of links that have each node is termed degree. The statistics of the degrees in
a network is quantiﬁed by the degree distribution, a histogram of degrees considering the
whole network [9].
Nodes directly connected are called ﬁrst neighbors. A node can also inﬂuence and be
inﬂuenced by the neighbors of its neighbors, called second neighbors. Considering a con-
nected network, the inﬂuences may be extended to all neighborhood radius. Our goal is to
quantify the amount of information involved in the diversity of inﬂuence extending over the
network. For this purpose, we calculated the Shannon entropy [5] considering the statistics
of distances between a node and all their neighborhood radius.
Distances in network theory are related to the paths lengths. By deﬁnition, a path length
Γi,j is the number of consecutive links between the pair of nodes i and j, following a speciﬁc
trail. The shortest path length (D(i, j) = min({Γi,j})) deﬁnes geodesic distance between
two nodes [11]. The geodesic distance has been used in several network characterizations
4


## Page 5


such as small-world networks [12].
By looking at the distribution of geodesic distances for a given node, we can better
understand the role played in the network by that particular node. Quantifying the diversity
of inﬂuences due the geodesic distances brings to light the rules of how the information is
distributed in the network.
We deﬁne Pi{pi(r), 1 ≤r ≤max(D(i, {j}} as a probability mass function of ﬁnd a node
in the neighborhood ratio r of the node i. That is, the probability of, in a random choose,
one selects a node j from the set of the remain nodes ({j} := j ∈ν/ j ̸= i) with the geodesic
distance D(i, j) = r. This probability is deﬁned as:
pi(r) =
1
(N −1)
X
{j}
δD(i,j),r ;
(1)
where neighborhood radius r assumes values according to the interval (1 ≤r ≤max(D(i, {j}).
See an illustration in Figure 1.
The distribution Pi(r) contains information about the connectivity across multiple links
of a network. For illustration, consider hypercubic lattices of dimension D with links only
between neighboring nodes. The distribution Pi(r) scales according to Pi(r) ∼rD−1, because
nodes a ﬁxed distance r away lie on the (hyper)surface of constant distance to the node i,
where in D dimensions, this surface has dimension D −1. Hence, it makes sense that the
characerization of the distribution Pi(r) has the potential to provide insights into network
connectivity.
The geodesic entropy is given by:
sg
i [Pi] = −
rmax
X
r=1
pi(r) log pi(r) ;
(2)
where rmax = max(D(i, {j}). The value of sg
i does not depend on the network size for
greater networks (N ≫rmax). The characteristic geodesic entropy of a network is deﬁned
by:
Sg = 1
N
N
X
i=1
sg
i ;
(3)
Distinct from the entropy of the degree distribution, that quantiﬁes the constraints im-
posed by the network degree distribution [13], the geodesic entropy quantiﬁes the information
due to the intrinsic conﬁguration of network structure. Networks with diﬀerent structures
5


## Page 6


can share the same degree distribution, that is, they can be degenerate in the entropy of
the degree distribution. The characteristic geodesic entropy can lift the degeneracy of those
networks. Besides, the geodesic entropy is a measurement more appropriate to characterize
the nodes role and the underlying trends in the network topology.
We brieﬂy compare and relate the geodesic entropy to similar quantities that have been
used to study networks. The use of geodesic distances to evaluate Shannon entropy was
ﬁrstly proposed by Chen and collaborators [14]. Instead deﬁne the entropy per node, they
deﬁned a global entropy (Ir(G)) considering only one speciﬁc value r of geodesic distance.
A recent work from Stella and Domenico proposes a similar formula proposed in this work
to characterize centrality by mean of Shannon entropy [15]. Their proposes diﬀerente from
ours by a normalization factor that depends on rmax. It limitates the entropy to be deﬁned
between 0 and 1. This normalization does not take in consideration the increase on entropy
due the increase of maximum radius rmax. In contrast to the above methods, the geodesic
entropy we propose here allows the evaluate the inﬂuence of the maximum neighborhood
radius, as well as its dependence of network size, and to depict the role of each node in the
network.
Figure 1. Schematic representation of neighborhood radius r and its probability distribution. The
left panel shows three neighborhood radius for the node i. The nodes within the neighborhood
r = 1, r = 2, r = 3 are, respectively, 1, 2 and 3 links distant from the node i. On the right is the
probability distribution of the geodesic distances for this network.
6


## Page 7


A.
Entropy-degree diagram
We introduce here the entropy-degree diagram, a viewer tool to help to map the role
of nodes into the network. Entropy-degree diagram is built plotting the geodesic entropy
(sg
i ) versus the nodal degree k normalized by the maximum number of connections possible
(k/(N −1)) for all nodes belonging to the network. This normalization allows we compare
networks with diﬀerent sizes. Figure 2 shows the entropy-degree diagram for 3 networks
that share the same number of nodes and links, have the same degree distribution but
have diﬀerent structures. Each marker (•) represents a node. We used here colors as a
didactic artifact to improve the visualization (it can be neglected to build the entropy-
degree diagram). The colors are deﬁned according to their maximum neighborhood radius
(rmax), that is, the greatest geodesic distance between the given node and the remaining
nodes. The watermark regions follow the same colors and delimit the space of possibilities
for each value of rmax. For example, the purple curve delimits the possible positions on the
diagram for nodes with ﬁrst and second neighbors. The region in blue delimits the positions
for nodes with ﬁrst, second and third neighbors and it follows for the others regions. The
up limit of each rmax region are peaked at (k ≈1/rmax, sg ≈ln rmax). Note the values
have no dependence with the network size. They depend only on the network structure.
The magnitude of the increment in the geodesic entropy due to the increase of rmax is
inversely proportional to rmax , (∆sg ≈r−1
max∆rmax). That means there is a limit in which
the increase of maximum geodesic distances (increase the sparsity) contributes signiﬁcantly
to the network entropy. The lower limits will be aﬀected by the size of the network and
converge to the ﬁrst curve (rmax = 2) for large networks. See Figure 3. We would like to let
open the question if it could explain some optimization patterns in real networks.
The entropy-degree diagram helps to visualize how the information is distributed across
the network. The nodes with high entropy comprise more information. Their interactions
into the networks are more “ﬂexible”. That is, they are in a position where the diversity of
interactions is arranged in a way that allows holding more information. The opposite can
be aﬃrmed to nodes with low entropy.
7


## Page 8


B.
Geodesic entropy of functional brain networks under Ayahuasca inﬂuence
We use the geodesic entropy to evaluate functional brain networks in diﬀerent states of
consciousness: ordinary state and psychedelic state induced by Ayahuasca. Ayahuasca is a
sacred brew from Amazonian indigenous culture made with two plants from Amazonian ﬂora
– the leaves of the bush Psychotria Viridis, that contains N, N-Dimethyltryptamine (DMT),
and the vine Banisteriopsis caapi, that contains monoamine oxidase inhibitors MAOi [6].
The DMT is a serotonergic psychedelic similar to LSD [16, 17], and mescaline but fast
metabolized by the human body. The MAOi’s act slowing down this degradation, allowing
the DMT to cross the blood-brain barrier and enabling hours of psychedelic experience [6].
For more information about Ayahuasca we referee [18–22].
1.
Data
The experimental procedures were performed in accordance with the guidelines and reg-
ulations approved by the Ethics and Research Committee of the University of S˜ao Paulo at
Ribeir˜ao Preto (process number 14672/2006). All volunteers sign a written informed con-
sent. The fMRI data were acquired from 10 healthy adult volunteers (mean age 31.3, from
24 to 47 years, 5 women) with no history of neurological or psychiatric disorders – evaluated
by DSM-IV structured interview [23]. They have at least 8 years of formal educational and
minimum Ayahuasca use time of 5 years. They were in absence of any medication for at least
3 months prior to the acquisition and also had not take nicotine, caﬀeine, and alcohol prior
to the acquisition. Each volunteer ingested about 120-200 mL (2.2 mL/kg of body weight)
of Ayahuasca. The chromatography analysis detected on the brew 0.8 mg/mL of DMT, 0.21
mg/mL of harmine and no harmaline at the threshold of 0.02 mg/mL [24]. The volunteers
were submitted to two sections of fMRI scanning: one before and other 40 minutes after
Ayahuasca intake when the subjective eﬀects can be observed. In both cases, volunteers
were requested to be in an awake resting state, that is lying with their eyes closed, without
performing any task. The samples of one volunteer were excluded from the dataset due to
excessive head movement.
8


## Page 9


2.
Obtaining functional networks from fMRI data
The methods to extract the networks from the fMRI data used here are the same per-
formed in the reference [13].
The pre-processing of fMRI data was made according to
standard guidelines. We performed spatial smoothing (Gaussian kernel, FWHM = 5 mm)
and correction of slice-timing and head motion. We evaluated 9 regressors using a General
Linear Model (GLM): 6 regressors to movement correction, 1 to white matter signal, 1 to
cerebrospinal ﬂuid and 1 to global signal [25]. The images were spatially normalized ac-
cording to the Montreal Neurologic Institute (MNI152 template) anatomical standard space
using a linear transformation. We evaluated the band-pass ﬁlter using maximum overlap
wavelet transform (MODWT), considering the Daubechies wavelet to split the signal into 4
scales of distinct frequency bands. We choose the scale 3 (frequency band ≈0.03 −0.07 Hz)
to be in agreement with the literature that considers the low frequency (≈0.01 to 0.1 Hz),
preeminent on resting states [26].
We parcellate each image into 110 cortical anatomical regions according to the Harvard-
Oxford cortical and subcortical structural atlas (threshold of > 25%, using FMRIB software,
an FSL library). We evaluated only 104 cortical regions because of an acquisition limitations
for some subjects. The cortical regions were used to deﬁne the nodes of the brain networks
and the correlation between their signals to deﬁne the links. The signals corresponding
to each cortical region were obtained averaging the time series of all voxels (3D regular
grid) into them (using Marsbar, SPM toolbox). We calculate the Pearson correlation of
temporal series of all possible pairs of cortical regions, yielding a cross-correlation matrix.
Thus, we have for each sample (before and after Ayahuasca of all subjects) a 104×104
correlation matrix considered as an estimative of the brain functional connectivity. Since
the cortical regions deﬁne the nodes, the correlation matrices were used to deﬁne the links
of the functional brain networks.
For each sample, we generated a set of symmetric binary adjacency matrices by thresh-
olding the absolute value of their correlation matrices. Precisely, whether the absolute value
of the element matrix is larger than the deﬁned threshold, a link is formed (Ai,j = 1), other-
wise, no link is formed (Ai,j = 0). We choose a range of thresholds that ensure the networks
were fully connected but also sparse. We adopted the same criteria of references [13, 27–29].
We consider the network with lower global eﬃciency and greater local eﬃciency than its
9


## Page 10


randomized version [30]. We ﬁxed the same band of thresholds for all samples, allowing a
more accurate comparison. It was necessary to exclude two subjects from our analysis due
to a trade-oﬀin the range, leaving 7 subjects (4 women). As long as we intend to evaluate
the diﬀerence between topological features of networks before and after Ayahuasca intake,
we compare networks with the same density of links. The chosen threshold correlation range
is 0.28 ≤η ≤0.37 that yield networks with mean degree in the range 24 ≤⟨k⟩≤39. Sum-
marizing, we created two sets of networks (before and after Ayahuasca intake) that allow 16
diﬀerent comparisons (i.e. of diﬀering mean degrees) for each subject’s sample. The reader
can ﬁnd further details in the reference [13].
III.
RESULTS
Figure 4 shows the entropy-degree diagram of one of the subjects before and after
Ayahuasca intake for networks with mean degree ⟨k⟩= 25 and ⟨k⟩= 32. Note that the nodes
in the entropy-degree diagram after Ayahuasca tend to have higher entropy. All subjects
presented similar behavior. See supplementary material. Figure 5 shows the divergences of
the characteristic geodesic entropies between after and before Ayahuasca for each subject
by comparing pair of networks with the same density of links. The boxplot depicts the
distribution of characteristic geodesic entropy diﬀerences (∆Sg = Sg
after −Sg
before) of net-
works with the same mean degree. Note the characteristic geodesic entropy increases for all
subjects after Ayahuasca intake. Figure 6 shows the contrast of the characteristic geodesic
entropy of networks with the same mean degree (same densities of links) averaged over all
subjects before (blue) and after (brown) Ayahuasca intake. The increasing also appear in
this graphic suggesting that characteristic geodesic entropy of functional networks under
Ayahuasca inﬂuence tends to be higher than in ordinary condition.
The black and gray curves show the characteristic geodesic entropy for the randomized
versions of the networks before and after Ayahuasca respectively. We used the Maslov algo-
rithm [30] to randomize the links of networks keeping their degree distribution unchanged.
In other words, the Maslov randomization breaks all structural trends that do not depend on
the degree distribution. Note that the randomization reduces the entropy in both conditions
and no considerable divergence was found between the randomized curves. These results
mean that the change in geodesic entropy we detected before and after Ayahuasca intake is
10


## Page 11


related to underlying trends of the network structure. They do not result from the known
changes in degree distribution [13].
IV.
DISCUSSION AND CONCLUSION
The (often non-trivial) rules of interactions among the nodes of a network determine the
nature of its emergent behaviors. In many cases, the network interactions are deﬁned by
the relative position of each node in the network structure. The role of a node in a network
depends on how it is contextualized inside the network. In a highly connected network, a
node does not interact only with its ﬁrst neighbors, but also interact indirectly with the
other nodes. The geodesic entropy quantiﬁes the statistics (i,e. the the entropy functional
of the probability distribution) of the geodesic distances from a given node to all other nodes
in the network, by classifying all nodes according to their neighborhood radii.
In summary, we evaluate the geodesic entropy of functional brain network of subjects
in the resting state before and after the ingestion of the psychedelic brew Ayahuasca. We
ﬁnd that nodes of the functional network during Ayahuasca experience tends to have greater
geodesic entropy than in the ordinary condition, resulting in networks with higher character-
istic geodesic entropy. Hence, the geodesic distances between nodes become less constrained
on average, i.e. their distribution becomes “wider.” In a previous work, we showed that
the entropy of the degree distribution of brain functional connectivity networks under the
inﬂuence of Ayahuasca is greather than in the ordinary state [13]. The entropy of degree
distribution is a global measurement and networks with diﬀerent patters can share the same
degree distribution. The result presented in this paper suggests that the patterns can be
less restricted under Ayahuasca inﬂuence than in ordinary condition and it does not depend
on the degree distributions. The diversity of geodesic distances are more well-distributed
contributing to the ﬂexibility of interaction of the networks.
The hypothesis of entropy increases in some aspect of brain in psychedelic states has
been discussed in the literature [31–33]. This entropic brain hypothesis predicts that the
psychedelics state is associated with greather entropy compared to the ordinary state. The
hypothesis could explain the increased ﬂexibility in thoughts, facility to access suppressed
memory, increase of creativity, among others [31].
In conclusion, we have shown how the geodesic entropy quantiﬁes locally the connectivity
11


## Page 12


to the network globally. Further, we have used entropy-degree diagrams to evaluate the
role of each node in the network, giving a clearer view of the network topology and global
connectivity. The application to fMRI-based functional connectivity networks sheds insights
on how the brain changes under the inﬂuence of external inﬂuences. In this study, we used
Ayahuasca, but there is no reason why the method could not be applied to a variety of drugs
or meditative states, etc. We hope that these ideas and methods ﬁnd use in furthering our
understanding of complex networks in general and in brain function networks speciﬁcally.
12


## Page 13


Figure 2.
Illustration of entropy-degree diagram for three diﬀerent artiﬁcially generated networks
with the same number of nodes, links, same degree distribution (⟨k⟩= 25), but diﬀerent structural
conﬁgurations. On the right side of each entropy-degree diagram is the adjacency matrix of the
corresponding network.The characteristic geodesic entropy are Sg = 1.26 nats, Sg = 0.98 nats, Sg =
0.52 nats reespectvely from panels up to down. The colors purple, blue, green and red are deﬁned
according to the maximum neighborhood radius rmax = 2, 3, 4 and 5.
The watermark regions
delimit the space of possibilities for each value of the maximum neighborhood. The minimum
entropies possible are delimited by the purple curve and depends on the node degree.
13


## Page 14


Figure 3. Universal relations for geodesic entropy. In the sk-diagram on left, the colored regions
delimit the regions of nodes with maximum neighborhood values (rmax) indicated by the labels.
The maximum value of each region is in sg
i ≈ln(rmax), that correspond to k ≈1\rmax. The middle
plot shows the variance in the maximum entropy due the increase of neighborhood radius rmax.
Its increases are inversely proportional to rmax (∆sg
max ≈r−1
max∆rmax). Note that for small values
of rmax, its increasing will result in an increase in contribution to the entropy. Nevertheless, for
large rmax the contribution does not change signiﬁcantly. Note that none of these values depend
on network size. The ﬁnite size eﬀect appears in the lower limit. For large networks, all regions
will be delimited within the ﬁst curve (rmax = 2). The lower limit will depend on the network size
for ﬁnite networks. The right plot shows the inﬂuence of the network size in the lower limits.
14


## Page 15


Figure 4. entropy-degree diagram before and after Ayahuasca. The panels depict the entropy-
degree diagrams for one of the subjects before (upper row) and after (bottom row) Ayahuasca
intake for networks with mean degree ⟨k⟩= 25 and ⟨k⟩= 32 respectively. The colors follow the
same rules of ﬁgure 2. Note the nodes after Ayahuasca tends to occupy populate regions in the
diagram of higher entropy.
15


## Page 16


Figure 5. Nodal entropy before and after Ayahuasca. The boxplot shows the averaged geodesic
entropy in 16 networks with the mean degree from < k >= 24 to < k >= 39 for each subject
before (blue) and after (green) Ayahuasca. The median value increases for all of them.
16


## Page 17


Figure 6.
Mean geodesic entropy before and after Ayahuasca.
The graphic shows the mean
geodesic entropy under all subjects for before and after Ayahuasca for networks with diﬀerent
densities (mean the degree from < k >= 24 to < k >= 39 ). The mean geodesic entropy is greater
for all networks densities.
17


## Page 18


V.
SUPPLEMENTARY INFORMATION
18


## Page 19


Figure 7. Geodesic entropy before and after Ayahuasca intake for all subjects. The ﬁrst column
depicts the curves to characteristic geodesic entropy for networks with the mean degree from
⟨k⟩= 24 to ⟨k⟩= 39 for before (blue) and after (brown) Ayahuasca intake.
The second and
third columns show the sk-diagram for before and after respectively ( networks with mean degree
⟨k⟩= 32 ). Note an increase of geodesic entropy for all subjects.
19


## Page 20


[1] J. D. Haynes and G. Rees, Nat. Rev. Neurosci. 7, 523 (2006).
[2] M. E. J. Newman, Social Networks05 2005 27, 39 (2005).
[3] M. P. van den Heuvel and O. Sporns, Trends Cogn. Sci. 17, 683 (2013).
[4] B. Hou, Y. Yao,
and D. Liao, Physica A: Statistical Mechanics and its Applications 391,
4012 (2012 2012/0).
[5] C. E. Shannon, The Bell System Technical Journal The Bell System Technical Journal 27,
379 (July 1948).
[6] J. Riba, M. Valle, G. Urbano, M. Yritia, A. Morte, and M. J. Barbanoj, Journal of Pharma-
cology and Experimental Therapeutics J Pharmacol Exp Ther 306, 73 83 10.1 (2003).
[7] B. Shanon, Antipodes of the Mind (Oxford University Press UK, 2002).
[8] R.-F. A. U. G. Riba, J., A.-R. M. M. C. J. C. Morte, A., and M. J. Barbanoj, Psychophar-
macology 154, 85 (2001 2001/0).
[9] M. E. J. Newman, Networks: an introduction (Oxford University Press, Inc., New York, 2010).
[10] R. Albert and A. L. Barabasi, Rev. Mod. Phys. 74, 47 (2002).
[11] M. Rubinov and O. Sporns, NeuroImage 52, 1059 (2010).
[12] D. J. Watts and S. H. Strogatz, Nature 393, 440 (1998).
[13] A. Viol, F. Palhano-Fontes, H. Onias, D. B. de Araujo, and G. M. Viswanathan, Sci. Rep. 7,
7388 (2017).
[14] Z. Chen, IEEE Trans. Control Network Syst. 1, 349 (2014).
[15] M. Stella and M. De Domenico, Entropy 20 (2018).
[16] A. Hofmann, J. Ott, and A. Feilding, LSD: My Problem Child (OUP Oxford, 2013).
[17] T. Passie, J. H. Halpern, O. D. Stichtenoth, H. M. Emrich, and A. Hintzen, CNS Neur. &
Ther. 14, 295 (2018).
[18] B. Shanon, The Antipodes of the Mind: Charting the Phenomenology of the Ayahuasca Expe-
rience (Oxford University Press, 2002).
[19] B. C. Labate and C. Cavnar, Ayahuasca Shamanism in the Amazon and Beyond, Oxford
Ritual Studies Series (Oxford University Press, 2014).
[20] B. C. Labate and C. Cavnar (Springer-Verlag, 2014).
[21] B. C. Labate and C. Cavnar, The Therapeutic Use of Ayahuasca (Springer-Verlag, 2013).
20


## Page 21


[22] J. Riba, A. Rodriguez-Fornells, G. Urbano, A. Morte, R. Antonijoan, M. Montero, C. J.
Callaway, and J. M. Barbanoj, Psychopharmacology 154, 85 (2001).
[23] A. P. Association and A. P. A. T. F. on DSM-IV., Diagnostic and Statistical Manual of Mental
Disorders: DSM-IV-TR, Diagnostic and Statistical Manual of Mental Disorders: DSM-IV-TR
(American Psychiatric Association, 2000).
[24] D. B. De Araujo, S. Ribeiro, G. A. Cecchi, F. M. Carvalho, T. A. Sanchez, J. P. Pinto, B. S.
de Martinis, J. A. Crippa, J. E. C. Hallak,
and A. C. Santos, Human Brain Mapping 33,
2550 (2012).
[25] We used FSL Software, a free library of statistical tools available by Oxford Centre for Func-
tional MRI of the Brain (http://www.ndcn.ox.ac.uk/divisions/fmrib).
[26] P. Fransson, Human Brain Mapping 26, 15 (2005).
[27] H. Onias, A. Viol, F. Palhano-Fontes, K. C. Andrade, M. Sturzbecher, G. Viswanathan, and
D. B. de Araujo, Epilepsy & Behavior 38, 71 (2014).
[28] M. S. Schroter, V. I. Spoormaker, A. Schorer, A. Wohlschlager, M. Czisch, E. F. Kochs,
C. Zimmer, B. Hemmer, G. Schneider, D. Jordan, and R. Ilg, Journal of Neuroscience 32,
12832 (2012).
[29] Y. Liu, M. Liang, Y. Zhou, Y. He, Y. Hao, M. Song, C. Yu, H. Liu, Z. Liu, and T. Jiang,
Brain 131, 945 (2008).
[30] S. Maslov and K. Sneppen, Science 296, 910 (2002).
[31] R. Carhart-Harris, R. Leech, P. J. Hellyer, M. Shanahan, A. Feilding, E. Tagliazucchi, D. R.
Chialvo, and D. Nutt, Frontiers in Human Neuroscience 8, 20 (2014).
[32] D. Papo, Frontiers in Human Neuroscience 10, 423 (2016).
[33] R. L. Carhart-Harris, Neuropharmacology (2018).
21

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]