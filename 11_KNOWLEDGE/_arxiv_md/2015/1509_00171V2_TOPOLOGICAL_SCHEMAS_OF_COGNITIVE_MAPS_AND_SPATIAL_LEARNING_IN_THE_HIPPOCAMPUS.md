---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1509.00171v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1509.00171v2_Topological_schemas_of_cognitive_maps_and_spatial_learning_in_the_hippocampus

> Source: 1509.00171v2_Topological_schemas_of_cognitive_maps_and_spatial_learning_in_the_hippocampus.pdf

> Pages: 22

---


## Page 1


Topological schemas of cognitive maps and spatial learning
A. Babichev1, S. Cheng2 and Yu. Dabaghian1∗
1Department of Neurology Pediatrics, Jan and Dan Duncan Neurological Research Institute,
Baylor College of Medicine, Houston, TX 77030 USA
Department of Computational and Applied Mathematics, Rice University, Houston, TX 77005 USA,
2Mercator Research Group “Structure of Memory” and Department of Psychology,
Ruhr-University Bochum, Universitaetsstrasse 150, 44801, Bochum, Germany
E-mail: babichev@bcm.edu, sen.cheng@rub.de, dabaghia@bcm.edu∗
(Dated: August 5, 2018)
Spatial navigation in mammals is based on building a mental representation of their environment—
a cognitive map. However, both the nature of this cognitive map and its underpinning in neural
structures and activity remains vague. A key diﬃculty is that these maps are collective, emergent
phenomena that cannot be reduced to a simple combination of inputs provided by individual neurons.
In this paper we suggest computational frameworks for integrating the spiking signals of individual
cells into a spatial map, which we call schemas. We provide examples of four schemas deﬁned by
diﬀerent types of topological relations that may be neurophysiologically encoded in the brain and
demonstrate that each schema provides its own large-scale characteristics of the environment—the
schema integrals. Moreover, we ﬁnd that, in all cases, these integrals are learned at a rate which is
faster than the rate of complete training of neural networks. Thus, the proposed schema framework
diﬀerentiates between the cognitive aspect of spatial learning and the physiological aspect at the
neural network level.
arXiv:1509.00171v2  [q-bio.NC]  20 Mar 2016


## Page 2


2
I.
INTRODUCTION
In the 1940’s, Tolman proposed that animals build an internal representation—a cognitive map—of
their environment and that this map allows the animal to perform space-dependent tasks such as navigat-
ing paths, ﬁnding shortcuts, and remembering the location of their nest or food source [1]. Three decades
later, O’Keefe and Dostrovsky discovered pyramidal neurons in the hippocampus, named place cells, that
become active only in a particular region of the environment—their respective place ﬁelds [2] (Figure 1A).
The striking spatial selectivity of these place cells led O’Keefe and Nadel [3] to suggest that they form a
neuronal basis of Tolman’s cognitive map, thus providing this abstract concept with a concrete neurophysio-
logical basis. In the ensuing decades, it was realized that there are many brain regions involved in cognitive
mapping of the environment [4], yet there is still no consensus on either the physiological mechanisms of
this phenomenon or the theoretical principles that explain them [5]. Overall, it is believed that individual
cells encode elements of the cognitive map, much like contributing pieces to a jigsaw puzzle. However, this
analogy is not direct: the spiking activity of each separate neuron has no intrinsic spatial or geometrical
properties—these properties appear only at the population level, emerging from the synchronous spiking
activity of large neuronal ensembles [6, 7]. The mechanism of this phenomenon remains unknown, i.e.,
there exists a disconnect between the level of individual neurons from which the preponderance of neuro-
physiological data is acquired and the level of neuronal ensembles where the large-scale representations of
space are believed to emerge [8].
In a recently proposed a model of spatial learning [9, 10], we attempted to bridge this gulf by combining
recent experimental results pointing out the topological nature of the hippocampal map [11–17] and methods
of Algebraic Topology. This model allowed demonstrating that place cell activity can encode an accurate
topological map of the environment and estimating the time needed to accumulate the required connectivity
information. Further analyses of the model suggested to us that it is indicative of a more general theoretical
framework that may lead to a systematic understanding of how spiking activity of neurons can be integrated
to produce large-scale characteristics of space. In this paper, we outline the general principle and provide
four speciﬁc models, which we call schemas, of integrating the activity of simulated neurons into a coherent
representation of the explored environment. For each schema we ﬁnd that a large-scale spatial map is
produced within a short, biologically plausible period, which could be used to estimate the spatial learning
time in diﬀerent environments.
II.
THEORETICAL FRAMEWORK
A.
The model
A schema model of a cognitive map contains the following three key components:
i. An abstract schema S(R, PS ) represents the spatial information contained in the map at any given
time. It consists of a set of formal regions R = {r1, r2, ..., rN} and a set of relationships, PS = {ρ1, ρ2, ..., ρM},
that express how these regions combine. We presume that each region ri in the schema can be related to
any other region rj through a chain of relationships with intermediate regions ρα(ri, rk), ρβ(rk, rl, rm),...,
ργ(rn, rj). A speciﬁc selection of the relationships included in PS determines the type of spatial information
encoded in the schema and the global arrangement of the encoded regions, which is crucial both for the
properties of the resulting map as well as for the information encoded in it.
ii. The neural implementation, NS , is a neural network that encodes the schema S. For the sake of
simplicity, we model NS using a basic, two layer, feed-forward neural network inspired by cell assembly
theory [18], which consists of a layer of cells that represent regions of space and another layer of readout
neurons that represent the relationships between these regions (Figure 1B). When a cell ci ﬁres a spike, we
say that the region ri is “active”; otherwise it is “latent” [19]. When a readout neuron ﬁres a spike, we


## Page 3


3
FIG. 1: Physiological components of the schema. A. The simulated trajectory in a 1 × 1 m environment (left) and
200 randomly scattered place ﬁelds (clusters of colored dots) produced by place cells with a mean ﬁring rate f = 12
Hz and a mean place ﬁeld size s = 20 cm. B. Schematic representation of three overlapping assemblies of place cells
(shown by black dots) that project synaptically onto their respective readout neurons (blue pentagons). The active
place cells (black dots with red centers) of the ignited cell assembly (in the middle of the ﬁgure) produce spike trains
that drive the spiking activity of the readout neuron (blue pentagon with the red center).
say that the corresponding relationship is “instantiated.” Thus, by construction, the relationships between
regions are represented via temporal relationships between the spike trains and by the parameters of synaptic
connections between the two layers in NS .
iii. The spatial map and the representing space. The goal of introducing schemas is to model the
assemblage of the cognitive maps from the cells’ spiking activity. However, in absence of a mechanism ex-
plaining how spatial representations emerge from the spike trains, this task remains undeﬁned. Statements
such as “a given place cell’s activity encodes a region” or “the coactivity of a set of place cells represents a
spatial overlap between the encoded regions” require an interpretation. In the analysis of electrophysiolog-
ical data, this interpretation is acquired by mapping the neuronal activity into an auxiliary, external space X
which is selected according to the experimenters’ best judgment. For example, constructing the place ﬁelds
by ascribing Cartesian x −y coordinates to the place cells’ spikes and identifying the areas where the spikes
cluster is one attempt to map the unobservable formal regions encoded in the cognitive map into observable
regions of the spatial environment [20]. In the following discussion, we will refer to this algorithm as to
standard place ﬁeld mapping. Spaces that have been used to interpret the activity of place cells and other
cells include Euclidean domains in one [21, 22] and in three dimensions [24, 25]; circles [26], tori [27],
spheres [28], and even Klein bottles [29]. To capture this aspect of cognitive map analysis, we deﬁne a
spatial mapping from the schema S to a representing space X,
f : S →X
(1)
in which the formal regions of S are mapped into the “concrete” regions of X, xk = f(rk). We will refer to
xk as the X-representations of the formal region rk and to the resulting layout of the representing regions in
X as the spatial map of the schema, MX(S).
Although the representing regions are selected to reproduce the relationships between the formal re-
gions as well as possible, the resulting map does not always capture the structure of the original schema:
some relationships may be lost in the mapping or the mapping may produce relationships between the rep-
resenting regions that are not encoded in S. For example, the place ﬁeld maps are believed to reﬂect an
animal’s cognitive map’s structure but their faithfulness has not been established or even addressed in the
neurophysiological literature. In the case when the set of relationships between the regions xk (PX) matches
the schematic relationships exactly, so that PX = PS , the mapping will be referred to as faithful. The corre-
sponding spatial map may then be viewed as a model of S, i.e., the structure of S can be deduced from the
layout of the representing regions.


## Page 4


4
Thus, each speciﬁc schema model includes these three components—the abstract schema S, its neuronal
network implementation NS and the spatial mapping (1) into a representing space X. For brevity, we will
refer to this triad as to “schema,” when no ambiguities can arise.
B.
Spatial learning
A key property of our approach, crucial for modeling spatial learning, is that schemas are dynamic
objects. As an animal explores a novel environment, new regions become represented by the activity of
place cells and new relationships are inferred from the spike trains’ temporal patterns [9, 10]. According
to the standard approach of neural network theory, the process of learning a schema may be viewed as
the process of training the readout neurons to represent the set PS by detecting repetitive patterns in the
incoming spike trains. From this perspective, a schema is learned after its network is trained, i.e., after the
readout neurons stop adopting their spiking responses to the patterns of the incoming spike trains.
On the other hand, from a cognitive perspective, the purpose of spatial learning is to acquire qualitative,
large-scale characteristics of the environment, which enable spatial planning, spatial navigation and spatial
reasoning, such as path connectivity, shortcuts and obstacles, geometric and topological properties, global
symmetries and so forth. Such large-scale characteristics of the environment that are captured through the
relationships of a given schema will be referred to as schema integrals, IS. Below we demonstrate that
the minimal time Tmin required for the schema’s integrals to emerge is typically shorter than the time, TN,
required to train all readout neurons, i.e., large-scale information can be extracted from a partially trained
network. Thus, the schema approach captures two complementary aspects of spatial learning: physiolog-
ical learning—the process of forming and training the cell assembly network and schematic or cognitive
learning—the emergence of information about the global structure of space, expressed as the corresponding
production of schema integrals.
C.
Topological Schemas
What aspect of space is represented in the hippocampal map? The answer to this question depends on the
information captured by the readout neurons in the hippocampal cell assemblies. Since correlating neuronal
spiking with geometrical properties of the representing space sometimes produces useful interpretations of
electrophysiological data, most authors assume that the spiking patterns of place cells encode geometric
properties of space [30, 31]. For example, it has been shown that combining the spiking activity of a
relatively small number of place cells with the information about the sizes, shapes, and locations of their
respective place ﬁelds allows a reconstruction of the animal’s trajectory in a typical experimental enclosure
on a moment-to-moment basis [32, 33].
However, the read-out neurons have access only to the place cells’ spikes, and not to their respective
place ﬁelds. Obtaining the shape and size of any given place ﬁeld, which is nothing but a cumulative spatial
histogram of spikes used for illustrational purposes, requires accumulating a substantial number of spikes
from the corresponding place cell. Yet the spike trains produced during the activity period of a given place
cell are short—typically hundreds of milliseconds in duration—and highly variable, not only because of
the animal’s movements, but also because of the intrinsic stochasticity of neuronal spiking [34]. Thus, the
spike trains of place cells contain little information about a place ﬁeld, such as its shape, location and other
computationally expensive parameters. Furthermore, recent experimental studies point out that these spike
trains do not provide the geometric information on the synaptic integration timescale of seconds or fractions
of a second [17, 22, 23].
Since the temporal pattern of place cell ﬁring is the only information available to downstream neurons, a
physiologically adequate class of schemas of the hippocampal map may be constructed based on capturing
qualitative, topological relationships between regions, e.g., overlap, adjacency, ordering and containment,


## Page 5


5
FIG. 2: Graph schema. A. A schematic illustration of the spike trains produced by seven place cells whose coactivity
is indicated by the dashed rectangles connecting the spike trains. B. The corresponding seven place ﬁelds traversed
by the animal’s trajectory (dashed line). C. The corresponding graph schema, the seven vertexes of which correspond
to seven formal regions encoded by the active place cells. The edges mark the relationships encoded in the schema,
e.g., the connection (r4, r5) is in the schema, but (r5, r1) is not.
from the temporal relationships between the spike trains [16, 35]. The resulting maps will then produce a
topological representation of space rather than a geometrical one [36, 37], in which the relative arrangement
of the locations is more important than mapping the precise positions. Topological schemas have several
advantages over the more precise geometric schemas, e.g., higher stability (e.g., faithfulness of a topological
map is not destroyed under continuous deformations of the representing space) and lower computational
cost, which may make them biologically more viable (see Discussion).
There remain many possibilities in which to read out qualitative information about the spike trains
and thus there are many topological schemas. In this perspective, a particular readout mechanism, which
responds to speciﬁc patterns of place cell coactivity, deﬁnes the type of spatial information encoded in the
schema. The following discussion presents four diﬀerent topological schemas based on diﬀerent qualitative
relations between regions and the rate at which these schemas are acquired.
III.
RESULTS
A.
Graph Schema G
The simplest topological schema is based on binary connections: its set of relationships consists of
pairs of connected regions, PG = {(ri, rj), (ri, rk), (rm, rn), ...}. Such schema can be viewed as a graph,
G, whose vertices are linked if the corresponding regions are related according to PG (Figure 2). The
corresponding neuronal implementation is produced by training the pair-coactivity detector readout neurons
to respond to nearly simultaneous spiking of their respective pair of presynaptic cells [38, 39]. In other
words, physiological learning of a graph schema G amounts to detecting pairs of cells that exhibit frequent
coactivity [42].
We modeled this process by simulating place cell spiking activity induced by a rat’s movements across
a place ﬁeld map in a small environment (Figure 1B). To simplify the analyses, we assume that as soon
as the coactivity occurs, the corresponding connection is immediately “learned,” i.e., incorporated into the
schema. As a result, at every moment of time t, the connectivity matrix of the graph is deﬁned by the
coactivity observed prior to that moment. Thus, Ci j = 1 if cells ci and cj coﬁred before t and Cij = 0
otherwise. Figure 3A shows that the number of links in the graph, which is the number of recruited pair-
coincidence detectors, grows as the schema is learned and saturates at ca. TN = 5 mins, i.e., after this time
new incoming spike trains do not produce new connections in NG.
The saturation of the schema could be a trivial result if the graph becomes fully connected or remains


## Page 6


6
FIG. 3: Spatial learning based on the graph schema. A. The number of links in the graph schema as a function of
time, computed for a simulated ensemble of 200 place cells with randomly scattered place ﬁelds (see Methods). The
blue line represents the mean and the red lines show the error margins. B. Graph schema entropy (blue) and place
ﬁeld map entropy (red) as a function of time. The green line shows the mutual information between the map and the
schema. Both entropies and the mutual information saturate at the time when the number of links saturates. C. The
probability of establishing a maximal length connection in the graph schema stabilizes in about 2.2 minutes, when
only 50% of connections appeared.
mostly empty. A simple characteristic capturing the eﬃciency of G, which generalizes to other schemas in
a natural way is its entropy [40, 41]. This is the speciﬁc entropy of the readout neurons,
HG = −pc log2(pc) −pd log2(pd),
where pc and pd = 1 −pc are the fractions of the connected and disconnected vertex pairs in the graph.
For a fully discrete (pc = 0) or a fully connected graph (pc = 1) the entropy vanishes and maximal entropy
HG = 1 is achieved for pc = 1/2 (in which case the absence of a link is as informative as its presence).
Figure 3B demonstrates that for the place cell ensemble used in our simulations (see Methods), the entropy
of the graph schema asymptotically approaches a maximal value of about HG ≈0.8 in about ﬁve minutes, a
value implying that the schema network NG is neither underloaded nor oversaturated.
To quantify the correspondence between the schema G and its place ﬁeld map MX(G), we calculated
the entropy HX, of the occurrences of place ﬁeld pairwise overlaps across time and compared HX to HG.
Figure 3B demonstrates that both entropies remain close throughout the entire learning period, indicating
that the complexity of the place ﬁeld layout remains similar to the complexity of the encoded relationships
at all times. In addition to this correspondence we also computed the mutual information (MI, see Methods)
between the place ﬁeld overlap and place cell coactivities, which also grows with the rat’s navigational
experience (Figure 3B). Thus, we have convergent lines of evidence indicating eﬃcient spatial learning
captured by the graph schema.
As a cognitive map model, the graph schema G provides a stratum for implementing graph-theoretical
navigation algorithms, that is, for establishing paths connecting spatial locations [43, 44]. Its integrals IG
are the global characteristics of the region-to-region connectivity graph, e.g., its partitioning, the colorabil-
ity of its vertexes and edges [45], its planarity, and the existence of a path between two given vertexes. As
an example of such large-scale characteristics we identiﬁed the shortest paths connecting pairs of the most
distant vertexes and computed the time required to establish these connections. The results shown in Fig-
ure 3C demonstrate that the animal establishes connections between the most distant locations in the graph
in about Tmin = 2.2 minutes, a time when only about 50% of the readout neurons are trained. Similarly,
emergence of the information required to establish existence of a circuit of the graph which traverses each
edge exactly once, called an Eulerian path, takes about 2.2 minutes, while the correct number of cliques in
G, which are sets of pairwise connected vertices, can be deduced within two minutes. These observations
suggest that the emergence of schema integrals before the network is trained may be a general phenomenon.


## Page 7


7
FIG. 4: Simplicial schema. A schematic representation of the connections between the vertexes associated with
the seven place cells and their spatial map shown on Figure 1B. B. The existence of the two-dimensional simplexes,
corresponding to higher order coactivity relationships, permits the links to be deformed. This is illustrated for paths
γ1 and γ2: the transformation can be visualized by slipping one path across the two-dimensional facets, thus demon-
strating the topological equivalence between paths γ1 and γ2. C. The nerve of the map shown on Figure 1B matches
the simplicial schema.
B.
Higher-order Overlap (Simplicial) Schema T
A topological schema may be based on representing not only binary, but also ternary, quaternary and
other higher-order connectivity relations between spatial domains. For example, a schema may represent
the overlaps between regions, including triple, quadruple, etc., overlaps. The key property of the overlap
relation is that if k regions, r1, r2, ..., rk, have a common intersection, then so does any subcollection of
them. The simplest mathematical object that is closed under the operation of taking non-empty subsets
is an abstract simplex, which can be viewed as a list of k elements [46]. Hence, a (k + 1)-order overlap
relationship ρ(r0, r1, ..., rk) may be represented by a k-dimensional simplex σ = [r1, r2, ..., rk]. A set of
overlap relationships therefore forms an abstract simplicial complex, T , and we will hence refer to a higher
order overlap schema as to simplicial schema.
Under the standard mapping of the place cell spiking activity into the environment, the simplicial
schemas’ relationships, PT , represent the overlaps between the place ﬁelds. For example, the place ﬁeld
map shown in Figure 2B can be faithfully encoded by a simplicial schema with four 3d order relationships
P3 = {(r6, r1, r7), (r7, r1, r2), (r1, r2, r4), (r2, r3, r4)} and an additional binary relation (r4, r5), as shown in Fig-
ure 4. The neuronal marker of these overlaps is the spiking coactivity: if the animal enters a location where
several place ﬁelds overlap, their respective place cells produce (with a certain probability) temporally over-
lapping spike trains. Hence the neural network implementation of a simplicial schema, NT , should be built
to detect the coactivity events, using coincidence detector readout neurons (which, in fact, corresponds to
the current view on the hippocampal cell assembly network organization [18, 47–49]).
Physiological learning of a simplicial schema hence amounts to training the readout neurons to detect
place cell coactivities. Our learning algorithm (see Methods) ensures that, at every stage of learning, only
the highest order relationships are kept while the redundant lower-order relationships are eliminated. For
example, pairwise connections between three neurons become redundant after a triple coactivity between
them is detected, at which point the three pair-detector readout neurons can be replaced with a single triple-
coincidence detector. Numerical simulations demonstrate that, as the rat explores the environment, the more
probable, lower-order coactivity events are captured ﬁrst and the less probable higher order coactivities
accumulate more slowly (Figure 5A). Moreover, although rapid changes of the readout neurons’ order stops
after ﬁve or six minutes, slow regroupings continue during the entire navigation period, T = 25 minutes.
Thus, unlike the pairwise overlaps in G that can be instantly identiﬁed, the orders of the readout neurons
cannot be deduced from a single coactivity event. In this sense, the orders of the readout neurons are integral
characteristics of place cells’ spiking activity, and therefore may be viewed as integrals of the simplicial


## Page 8


8
FIG. 5: Learning the simplicial schema. A. The development of the population of readout neurons as a function of
time. The typical order of co-activity is about 20, the highest order is 33. The population of the high order readout
neurons (order above 11) increases through the entire duration of the experiment (over 20 minutes). Other populations
reach a stable plateau (e.g., orders 9 and 10) or reach a maximum and then drop (e.g., order under 8). The decrease of
the number of the low order relationships after an initial increase indicates the elimination of redundant information.
B. The development of the overlap relationships between the standard representing regions as a function of time. The
typical overlap order is about 20, the highest order is 35. As in the case with the readout neurons, the number of
high-order overlaps (order above 17) saturates on the rise, unlike the lower order overlaps. C. The entropy of the
dimensions of registered simplexes (red) is similar to the entropy of the orders of the overlaps of the concrete regions
xk (blue). The mutual information between these two variables is computed along the trajectory (green).
schema.
There exists an additional important set of T -integrals, which capture the topology of the representing
space. This property of the simplicial schemas can be illustrated using the ˇCech theorem, which states that
the pattern of overlaps between regions U1, U2, ..., Un, covering a topological space X = ∪iUi, encodes
homological invariants of X, provided that every intersection Ui ∩U j ∩... ∩Uk is contractible [50, 51]. The
proof is based on building the “nerve” of the covering—a simplicial complex, the d-dimensional simplexes
of which correspond to the (d + 1)-fold overlaps between covering regions, and showing that it is topologi-
cally equivalent to X (Figure 4C). This theorem implies that the spatial map of a suﬃciently rich simplicial
schema may encode the topology of the space navigated by the rat, and suggests that if this map is faithful,
i.e., if the nerve of the spatial map matches the schema’s relationship set PT exactly, then the schema also
captures the large-scale topological representation of the space.
To study the correspondence between the simplicial schema and its map, we compared the schema’s
entropy HT , deﬁned by the probabilities for a readout neuron to become a kth-order co-activity detector,
to the entropy HX of the place ﬁeld map MX(T ), deﬁned via the probabilities of producing a kth-order
overlap between the place ﬁelds (Figure 5B). As shown on Figure 5C, both entropies closely follow one
another: they both grow initially and reach similar asymptotes in approximately four minutes. However,
the mutual information between these two series of events decreases with time. The reason for this eﬀect
lies in the idealized nature of the representing regions xk, built as convex hulls of the spike clusters in the
two-dimensional environment (for other place ﬁeld construction algorithms see [53, 54]). The xk’s crisp
boundaries produce high-order overlaps, which are not captured by the place cell coactivity and hence by
the schema—compare the orders of the readout neurons on Figure 5A with the orders of overlap between
the corresponding representing regions xk in Figure 5B.
This result can be viewed from several perspectives. First, it illustrates that the scope of reliable in-
formation that can be drawn from the spatial map is limited: only suﬃciently robust, qualitative aspects
of the place ﬁeld map, such as low dimensional overlaps, can be trusted. Second, the regions ri that were
originally introduced as “formal,” that is, devoid of intrinsic properties, should fundamentally be viewed as
“fuzzy” and not as Euclidean domains with crisp boundaries [55].
Direct computations show that the coactivity complexes do, in fact, capture the topology of the repre-


## Page 9


9
FIG. 6: Topological loops in simplicial schema. A sequence of the place cell combinations ignited along a path γ
(black line) corresponds to a sequence of simplexes—a simplicial path Γ that represents γ in T . B. The dynamics
of the total number of zero-dimensional loops (red) and one-dimensional loops (blue). Unlike the growing number
of links in the graph schema (Figure 2A), the number of topological loops decreases with time. Eventually, a single
loop survives. The margins of error are shown above and below each graph by a pair of pink and light-blue lines,
respectively. C. The barcodes—timelines of the one-dimensional loops in the simplicial complex. The topological
noise vanishes after ca. 4 minutes, which is the schematic estimate of the cognitive learning time.
senting space, provided that the place cells’ spiking parameters fall into the biological domain [9, 10, 47],
and hence that simplicial schemas provide a framework for representing topological information. For ex-
ample, cell assemblies ignited along the physical paths traversed by the animal correspond to sequences of
coactivity simplexes—the simplicial paths that represent the physical paths in T (Figure 6A). The structure
of the simplicial paths allows establishing topological (in)equivalences between navigational paths, e.g.,
topologically equivalent simplicial paths represent physical paths that can be deformed into one another, a
non-contractible simplicial path corresponds to a class of the physical paths that enclose inaccessible or yet
unexplored parts of the environment. As a result, the simplicial schema produces a qualitative description
of navigational routes: while the total number of paths grows exponentially, the number of topologically
distinct loops, which represent topologically distinct paths is small (Figure 6B).
However, this information does not emerge immediately: as the animal begins to navigate a new environ-
ment, most topological loops reﬂect transient connections. As the spiking information accumulates, these
“spurious” loops disappear and only the loops that correspond to the physical signatures of the environment
persist (Figure 6C). With methods drawn from persistent homology theory [56, 57] one can determine the
minimal period Tmin required for removing the spurious loops, which provides a theoretical estimate of the
time required to learn the environment [9, 10]. Figure 6C demonstrates that in our test map, after Tmin = 4
minutes most topological loops have vanished and only the loops that correspond to the physical holes in
the environment survive. Thus, as in the case of the graph schema, the topological connectivity of the cog-
nitive map is captured by the simplicial schema before the underlying neuronal network is fully trained,
Tmin < TN.
C.
Mereological Schema M
Although a suﬃciently rich simplicial schema can capture the topological invariants of the representing
space X as its integrals, it does not capture all the qualitative topological aspects of the connectivity between
regions. For example, the identical simplicial schema (represented by a tetrahedron) can faithfully represent
the overlap relationships in the two maps shown in Figure 7, because both maps contain the same set of
regions R = {r1, r2, r3, r4} and one fourth-order overlap relation PR = {(r1, r2, r3, r4)}, as well as all their
consequent ternary and binary sub-relations. However, these maps are topologically diﬀerent, since they
cannot be transformed from one into another by a continuous deformation of the plane R2. The obstruction


## Page 10


10
FIG. 7: Mereological schema. In A and B, the overlap pattern does not capture the cover relationship. Four regions,
x1, x2, x3 and x4 form a quadruple overlap in both cases. However, in map shown in A, the region x4 is contained in
the union of x1, x2 and x3. In the map shown in B, x4 is not covered. C. The cover and the overlap relationships in a
mereological schema corresponding to the map of Figure 1A. The covering regions are connected by red links (e.g.,
r6, r1, and r2) and the red arrows point to the covered region (e.g., r7). D. A neuronal implementation of the covering
relationship includes three inhibitory neurons (magenta) that provide inhibitory input into the readout neuron (purple).
If each inhibitory input of an active interneuron exceeds the excitatory input of the driving cell c7, the readout neuron
can spike only if the activity of the cell c7 is not accompanied by the inputs from any of the cells c1, c2 or c6. As
a result, the readout neuron will remain silent as long as the activity of the cells c1, c2 and c6 temporally covers the
activity of cell c7.
to such deformation is that the region x4 on Figure 7A is contained in the union of the regions x1, x2
and x3, i.e., x4 ⊂(x1 ∪x2 ∪x3), and no containment relationships exist between any combinations of the
regions on Figure 7B. Neither a graph schema G nor a simplicial schema T can capture this diﬀerence;
what is required is the additional covering relation, (x1, x2, ..., xl) ◀(y1, y2, ..., yk), (x′s are covered by y′s),
in terms of which the map on Figure 7A is described by the relationship r4 ◀(r1, r2, r3), whereas the regions
shown on Figure 7B produce no containment relation. The cover relation produces a new—mereological—
schema M, in which the information is encoded in terms of topological containment (Figure 7C). The
intuition behind neuronal implementation of the formal cover relation is the following. If the activity of
one ensemble of place cells, U = {c1, c2, ..., ck}, outlasts, or covers in time, the activity of cells in another
ensemble V = {d1, d2, ..., dl}, then the region XU, representing the U-ensemble, contains the region XV
representing the V-ensemble:
XV ⊂XU if V ◀U.
From this perspective, the set of covering cells provides contextual information about the covered cells, i.e.,
the cover relation combines the basic formal regions into more complex, composite regions.
The cover relationship can be implemented, e.g., by a combination of the excitatory and inhibitory
neurons shown on Figure 7D. In such a cell assembly, the readout neuron signals a violation of the cover
relationship, i.e., the latter is represented by an absence of the readout neurons’ spiking activity up to the
moment t. Hence, in contrast with simplicial schemas, where readout neurons learn to detect ever higher-
order coactivities, a readout neuron in a mereological schema M learns to detect ever larger groups of cells
that together inhibit its activity (Figure 7D).
Similarly to the overlap orders in T , the cover relationships, as a rule, cannot be deduced from a single
coactivity event. Thus, these relationships represent integral information that can be viewed as the M-
integrals which characterize the large-scale topology of a space. We are currently unaware of additional
mereological algorithms that would allow large-scale computations of the environment’s global topological
characteristics, similar to computing the homological invariants in a simplicial schema. Nevertheless, a
mereological schema encodes an important type of topological information, which may be used in physio-
logical neural networks to represent spatial maps.
In general, covering relationships can be established between arbitrary (including multiply connected)
regions. As a result, the number of possible combinations of covered and covering regions dramatically


## Page 11


11
FIG. 8: Learning the mereological schema. A. Time development of the covering relationships: a pair of covering
place cells, U = {ci, c j}, and a covered cell, V = {dk}. Each line corresponds to a speciﬁc choice of U and V. Each
line begins as soon as the covering relationship is detected and stops as soon as it is violated, that is, as soon as the
readout neuron shown in Figure 7D would ﬁre. Note that the majority of relationships are short-lived: a large number
of spurious relationships are detected at the beginning of exploration. After about seven minutes the majority of them
disappear, similar to the behavior of topological loops computed in the simplicial schema shown in Figure 6B. This
diagram shows about 1% of the detected pairs, selected at random. B. The number of detected cover relationships
between pairs of place cells and a single place cell as a function of time.
increases. Even if the covered region V = {d1, d2, ..., dl} is spatially “bundled” (e.g., if each pair di and dj is
coactive at some moment of time, so that V forms a connectivity clique) the selection of possible covering
regions remains very large. Therefore, in order to test the development of cover relationships in time, we
opted to limit our study to neuron pairs covering an individual neuron (k = 2 and l = 1).
The results of simulations show that the time required to learn second-order covering relationships in M
is comparable to the learning times in the graph schema G (Figure 8). As spatial exploration begins, a large
number of transient covering relationships is produced because of insuﬃcient spiking data. With accumu-
lating spike trains most cover relationships become violated, so that the number of surviving relationships
quickly drops. As the animal completes its ﬁrst turn around a central hole of the environment (Figure 1B),
a new set of (mostly transient) relationships is injected into the schema which produces the peak shown
in Figure 8B. Subsequently, the number of cover relations steadily diminishes to about 200 pairs, which
corresponds to a saturated schema. This result reﬂects qualitative behavior of higher order covering re-
lationships, though a full implementation of the algorithm for the higher-order covering combinations (k,
l > 1) is computationally substantially more complex.
D.
Complex Relations and the RCC Schema R
Qualitative Space Representations (QSR) are discrete, region-based versions of the conventional
point-set theoretical geometries and topologies [58] used to formalize “intuitive” qualitative spatial
reasoning [59, 67, 75], and thus are particularly important for modeling cognitive representations of
space [62–65]. Important examples of QSRs are the Region Connection Calculi (RCC)—formal log-
ical theories based on a family of binary topological relations between regions [66].
For example,
the most basic RCC theory, RCC5, which applies to the case of regions with fuzzy boundaries, is
built using the ﬁve relations shown in Figure 9A: disconnect (DR), partial overlap (PO), proper part
and its inverse (PP and PPi), and equality (EQ) [67].
In terms of these relations, the arrange-
ment of regions shown on Figure 2B is described by the following set of RCC5 relationships: P =
{PO12, PO14, PO16, PO17, PPi23, PO24, PO27, PP32, PP34, PPi43, PPi45, PO46, PP54, PO67; DR for all other
pairs} (Figure 9B). More elaborate RCC calculi can capture tangencies [66], convexity [67], qualitative di-


## Page 12


12
FIG. 9: Illustration of RCC5 schema. A. RCC5 relationships: ﬁve logically possible pairwise relations: “x is
discrete from y” (denoted as DR), “x partially overlaps with y” (PO), “x is a proper part of y” (PP), “y is a proper
part of x” (PPi), and “x is identical to y” (EQ). B. An RCC5 schema, R5, of the spatial map from Figure 2B. For
convenience, the DR connections are shown with gray dashed lines. The structure of the rest of the relations produces
a graph similar to the one shown in Figure 2C. The black lines indicate PO connections. Cyan and blue arrows show
the PP and PPi connections, respectively. C. A U-track having two dead ends and a W-track having three dead ends
and a junction, j, marked in red. Every time the rat visits the junction point it must choose between the left and the
right turn, indicated by the red and blue trajectories, respectively. D. Topological relationships between regions on a
U- and a W-track that allow capturing the tracks qualitative geometries. The endpoints, e1, e2 and e3 are regions that
overlap with only one other region. The midpoints, m1, m2 and m3, overlap with two regions and the junction overlaps
with three regions.
rections [68], and distances [69] as well as complex hierarchies of all these relationships [70]. As a result,
RCC methods can capture not only standard topological signatures of spaces, such as loops and holes [71],
but also more subtle qualitative features, such as branching points, linear sections, and dead ends. These
qualitative features produce fundamental diﬀerences in spatial reasoning required for navigating the corre-
sponding environments. For example, the junction point on the W-tracks, which are often used in behavioral
experiments (Figure 9C), forces an animal to choose between a right or left turn, which is reﬂected in the
place cell code [72, 73]. The RCC5 theory allows capturing such features, e.g., distinguishing between
the U- and W-tracks, which, from the perspective of algebraic topology, are but contractible manifolds
(Figure 9D).
To model spatial learning based on a speciﬁc RCC approach, one can construct an RCC schema, in
which the readout neurons are trained to recognize the appropriate set of binary relationships. However, an
important aspect of RCC constructions is that the set of relationships that can be simultaneously imposed
on a set of regions is restricted [74, 75]. For example, if x and y partially overlap and y is a proper subset
of z, then z and x must have a non-null intersection and z cannot be a subset of x. Therefore, we deﬁne an
RCC schema R as a schema with a set of consistent RCC relations between regions.
To model the process of physiological learning in the RCC5 (R5) schema, we trained ﬁve types of
readout neurons to recognize the ﬁve RCC5 relationships, starting from the initial DR relationship. This
however requires more complex algorithms than in G and T schemas: while the partial temporal overlap can
always be interpreted as partial spatial overlap, other temporal relationships cannot be uniquely assigned
to a spatial RCC5 relation (Figure 10A). For example, passing through two partially overlapping regions


## Page 13


13
FIG. 10: Temporal vs. spatial relationships. A. Temporal relationships between the spike trains (o overlap, s
separation, d during, id inverse d and e equal [114]) and the corresponding spatial relationships. The relationships
DRxy, PPxy, PPixy and EQxy between the regions can be imitated by partial overlap, depending on the shape of the
trajectory, which shows that these relations cannot be directly deduced from the spike train structure. B. The transitions
between the RCC5 relationships, showing the immediate conceptual neighborhood (continuity table) structure of
RCC5. These are the possible sequences of gradual transformation of the RCC5 relationships. For example, if at
some moment of time two regions, x and y, were disconnected (DRxy) then this relationship cannot instantly jump to
a containment relationship (PPxy or PPixy) without going through, at least instantaneously, the partially overlapping
(POxy) relationship.
along a particular trajectory can generate a temporal disconnect, a temporal cover, or a temporal equality
relationship between two spike trains which can be mistaken for spike trains produced by a DR, PP/PPi,
or EQ relationship, respectively. Because of this ambiguity, the spiking activity of the presynaptic cells
in the cell assemblies produced during individual runs through a pair of place ﬁelds can invoke diﬀerent
interpretations of the spatial relationships. Thus, learning a R5 schema rests on encoding, at each moment,
the best guesses for the relationships between pairs of regions and then updating them based on the available
spiking history and the qualitative analogue of continuity constraints, as shown in Figure 10B.
In our simulations, the relationships evolved rapidly and saturated within about TN ≈4 minutes from
the onset of the exploration (Figure 11A). Figure 11B shows that at the beginning of the exploration, the
number of inconsistencies between independently trained readout neurons is high. Subsequently, their
number quickly diminishes as the information about coactivity is acquired. An increase in the number of
PP relationships in Figure 11A produces a splash of inconsistencies occurring at about 3 minutes, which is
at the time when the animal completes its ﬁrst turn around the central hole. This phenomenon has the same
origin as the splash of transient cover relationships occurring in the mereological schema M (Figure 8).
As the statistical information about place cell coactivity accumulates, a stable set of RCC5 relationship
emerges. The schema’s speciﬁc entropy, deﬁned using the probabilities of observing all ﬁve relationships,
saturates about the same time, TN ≈4 minutes. The entropy of the RCC5 relationships between the
representing regions in the map MX(R) remains similar to the schema entropy during the entire course
of learning, reaching the asymptotic value of H ≈0.84 (Figure 11C). Moreover, the mutual information
between the map and the schema increases with the acquisition of information in a way similar to the case
of graph schema G but unlike the case of simplicial schema T (cf. Figures 11C, 3C and 5E). Once again,
this data indicates that spatial maps built on regions with diﬀuse boundaries may better reﬂect the nature
of the encoded regions. In the meantime, the integrals of the R5 schema, i.e., the combinations of RCC5
relationships that represent the junction and the endpoints on the W track, emerge from neuronal spiking in
under Tmin ≈2 minutes—much sooner than the readout neurons in R5 network are trained.


## Page 14


14
FIG. 11: Learning the RCC5 schema. A. Evolution of RCC5 relationships: at the beginning of the exploration of
the new space, the regions are mostly disconnected and the partial overlap of relationships is accumulated over time.
Similarly to the graph schema, the number of all types of relationships saturates in about ﬁve minutes. B. The number
of inconsistencies in the randomly initialized relational network is higher at the beginning of exploration and decays
to a low, steady level by the time the number of relationships stabilize. C. The entropy of the relations encoded in the
schema (red), the entropy of the RCC5 relationships in the map (blue), and the mutual information (green) between
them saturate at a similar time scale.
IV.
DISCUSSION
We have presented a framework for integrating the place cells’ spiking information into a global map of
space, implemented via simple cell assembly neural networks, wired to encode spatial relationships. The
approach is motivated by the experimental results [11–17, 78–83] and by the theoretical models proposed
in [9, 10] and in [42–44]. From the perspective of the current approach these models are particular imple-
mentations of the simplicial and the graph schema, respectively; the mereological and the RCC schemas
are new—to our knowledge, such models have not yet been considered.
In the following we outline several important aspects of this framework and provide a general context
for the model.
4.1 Emergence of the memory map in schemas. There is a clear parallel between a coherent repre-
sentation of space emerging from the integrated inputs of many individual neurons and a continuous state
of matter (e.g., a solid or a liquid) emerging from the collective dynamics of molecules. From a descriptive
point of view, the common element in both phenomena is that neither macro-system can be reduced to a
trivial aggregation of the properties of its elementary constituents. Even when the properties at both the
microscopic and macroscopic levels are well understood, it can be diﬃcult to correlate the properties at one
level with those at the other. For example, the measurement of the macroscopic properties of a liquid does
not allow one to determine its molecular structure. Conversely, a detailed description of the properties of a
water molecule does not explain directly key phenomena of the physics of water. In physics, the solution
to this problem historically proceeded from a simpliﬁed, phenomenological models, which bridged the gap
between the microscopic and macroscopic levels of matter. In a similar way, the present discussion oﬀers a
testbed model with which to bridge the gap between place cells and the large-scale spatial map.
4.2 Topological spatial maps. Topological maps have several biological advantages over geometric (or
topographic [36]) maps, which follow from the qualitative nature of topological relationships [16]. First,
natural environments are dynamic, so that it is often impossible for an animal to know when and how its
navigational task may change. Hence acquiring a qualitative map based on the invariants of the space of an
environment, may be biologically more eﬀective than spending time on producing a computationally costly
precise answer from mutable relationships between dynamic cues.
One implication of this hypothesis is that in morphing environments the place ﬁelds will retain the pat-
tern of topological connectivity and may adjust their shapes in order to compensate for the deformation of
the representing space. This hypothesis is supported by experiments which demonstrate that place ﬁelds


## Page 15


15
maintain their relative conﬁgurations in morphing environments [76–83] and that place cell coactivity pat-
tern in an animal traversing remains invariant over a signiﬁcant range of geometric transformations [17, 22].
If the map is Cartesian, i.e., based on precise coordinates, distances, angles and so forth, such deformation
can be achieved by redrawing the place ﬁelds at each stage of the deformation, via some complex path in-
tegration mechanism [5, 11, 12, 63, 84–86]. From the topological perspective, the observed deformation of
the place ﬁelds is simply a result of projecting the same stable neuronal map into a morphing environment,
which does not require extra computations and hence may be biologically more plausible.
4.3. Schemas constrain the generation of intrinsic sequences in the hippocampus. Place cells
become active in temporal sequences that either match with or are inverse to the spatial ordering of their
place ﬁelds during the active, resting, or sleep states. Initially, temporal sequences were observed after
or during the recording of the place ﬁelds, leading various authors to suggest that the observed temporal
sequences were a replay of sequences imprinted by sensory inputs [96, 97]. More recent experiments have
observed temporal sequences that corresponded to trajectories along which the animal had never traveled
[98]. Furthermore, experiments have revealed that temporal sequences observed before the animal entered
an environment for the ﬁrst time were predictive of the place ﬁeld sequence measured later [99, 100].
These observations strongly suggest that temporal sequences are not merely replays of previously imprinted
sequences [23, 98]. The better interpretation is that sequences are drawn from a pool of sequences that are
intrinsic to the hippocampal network and this network structure gives rise to the location of place ﬁelds
[101–103]. The CRISP (for Context Representation, Intrinsic Sequences, and Pattern completion) theory
goes further to argue that the intrinsic sequences in the hippocampus are crucial for the storage of episodic
memories [101]. However, this theory does not explain the origin or properties of such sequences.
In the schema framework, all neural activity produced in the hippocampus has to be consistent with its
schema. For example, in the graph schema, spontaneously replayed sequences of neural activity would have
to be consistent with the connectivity of the graph. In other words, a cell ci may ﬁre a spike after cell cj
only if the relationship ρij = (ri, r j), or a chain of intermediate relationships ρii1, ρi1i2, ..., ρin−1in=j, is present
in PR. Other schemas impose diﬀerent constraints on which sequences can be produced, and the elements
in the sequences may be ensembles of place cells, rather than single cells. In other words, schemas serve as
“topological templates” oﬀwhich sequences are generated.
Physiologically, this implies that the hippocampal network that implements a particular schema can
produce sequences with speciﬁc “grammar” which may not have been directly imprinted or previously
produced by the network. In fact, such oﬄine state sequences of place cell activations, which the animal
had never experienced, were recently observed in the experiments [99, 100]. Moreover, these sequences
were consistent with the topology of the spatial environment [15]. Thus, schemas can explain the intrinsic
sequences postulated by CRISP theory as well as in preplay and replay. This intimate relationship between
spontaneous sequences and schemas may be exploited in future investigations in order to infer the schema
based on recordings of sequences or to predict the properties of intrinsic sequences from a given schema.
4.4. Spatial vs. non-spatial memories. The hippocampus has been suggested to encode both spatial and
nonspatial memories [87–91]. For example, it plays a key role in the ability to remember visual, odor, action
and memory sequences, and to put a speciﬁc memory episode into the context of preceding and succeeding
events, as well as the ability to produce complete memory sequence from a single structured input [92–95].
The topological view on the hippocampal spatial representations [9, 17, 35] provides a common framework
for understanding both spatial and nonspatial memory functions as manifestations of a single mechanism,
which simply produces a topological arrangement of memory elements, irrespective of the nature of their
content. According to this view, there is no principal diﬀerence between the internalized topological map
of spatial locations and a topological map of memory sequences in the mnemonic domain.
4.5. Connections to experiment. Given the place cells’ spiking parameters and a hypothesis about how
the downstream neurons might process place cell (co)activity, a schematic computation can be used to assess
the eﬀectiveness of the corresponding spatial learning mechanism: how much time will be required to map
a space, how many integrals can such mapping produce, how quickly these integrals will emerge and how


## Page 16


16
stable they will be. This scope of computations suggests a possibility for experimental veriﬁcations of the
proposed framework. For example, a decline in spatial learning caused by neurodegenerative diseases (e.g.,
in Alzheimer’s rat models), by aging or by psychoactive substances is assessed in behavioral experiments in
terms of the extra times required to learn various memory tasks. On the other hand, such cognitive changes
are associated with changes in the place cell spiking parameters [104–109]. It may therefore be possible to
compare the downturn of spatial memory observed in topological learning tasks [11, 12] with the increase
of the learning time(s) estimated via a particular schema model for the same change in spiking variables.
Another alternative was suggested to us by our recent studies of hippocampal mapping of 3D spaces in
bats, using two types of simplicial schemas. The results suggest that in the 3D case, the readout neurons
in the place cell assemblies should operate by integrating synaptic inputs over working memory periods,
rather than detecting coactivities on synaptic plasticity timescale [110]. Of course, until these predictions
are proved or disproved experimentally, their value is discussable; meanwhile, the schema approach allows
theoretical reasoning and generates predictions about hippocampal neurophysiology.
V.
METHODS
Place cells. Spiking is produced by the rat’s movement through the environment covered by the place
ﬁelds (Figure 1A-B). The Poisson rate of the ﬁring of place cells is a function of the animal’s position r(t)
at time t,
λi(r) = fie
−(r−ri)2
2s2
i ,
where fi is the maximal ﬁring rate of cell ci, si deﬁnes the width of its ﬁring ﬁeld centered at ri [20]. In
an N-cell ensemble, the parameters fi, and si, i = 1, ..., N are modeled as random variables drawn from
stationary unimodal distributions characterized by their respective means ( f and s) and standard deviations
(see Figure 1 and Methods in [9]). For the computations we used an ensemble with N = 200 neurons, with
mean ﬁring rate f = 12 Hz and the mean place ﬁeld size s = 20 cm. Larger ensembles typically aﬀect the
numerical values of the computed quantities, but not the essence of the phenomena described in the paper.
This spiking is modulated by theta-oscillations, which are a subcortical EEG cycle in the hippocampus with
a frequency of ∼8 Hz (for details see [10]).
Learning Algorithm. The physiological processes responsible for emergence of cell assemblies with
readout neurons trained to integrate presynaptic inputs and to produce a particular response that “actualizes”
the information encoded by the place cell coactivity are complex and multifaceted [18]. For example, the
readout neurons that encode place ﬁeld overlap must identify a group of place cells and learn to respond
to the coactivity of this speciﬁc group. However, what matters for our study, are the qualitative results of
this process: the number of readout neurons , the order of the coactivity detected by these neurons, how
this order grows in a typical cell assembly during the learning process and so forth. Therefore, we set aside
a neural network simulation of schema learning and employ the following schematic, phenomenological
algorithm:
If a relationship ρ of an appropriate type is detected, then:
1. if ρ is already listed in PR, ignore;
2. else if ρ can be inferred from the known relationships, ignore;
3. if ρ provides nontrivial information, then add ρ to PR.
4. if the known relationships can be inferred from ρ, then remove the redundant relationships.
5. continue


## Page 17


17
Steps 2 and 3 ensure that only the highest order relationships are kept in the schema, eliminating re-
dundant, lower-order relationships. At the beginning, every state of the readout neurons can be empty and
trained as the simulated animal explores a novel environment, or these states can be randomly initialized
and then relearned. The transitions between the readout neuron types may be regarded as a rudimentary,
schematic model of the synaptic plasticity mechanisms. In novel environments, place ﬁelds stabilize in
about four minutes [111], even though cognitive learning of the environment may take days or even weeks
[112]. This implies that the readout neurons can be trained using constant spiking parameters fi and si.
Temporal relationships between the spike trains and the physiological mechanisms underlying the
downstream neurons’ readout process are in general very complex. For the sake of simplicity, we consider
only the rate-based representation of neuronal activity [113], which allows for a variety of possibilities
for encoding relationships. Such relationships may entail that the ﬁring rates of the pre- and postsynaptic
neurons may be required to fall within a particular interval of values and the period of activity of a neuron
ci may be required to precede, to follow, or to overlap with the activity of a neuron c j by a certain minimal,
maximal or ﬁxed amount of time [114]. The present analysis works from the three mutually exclusive
logical possibilities for the activity of any two neurons ci and cj :
1. there is an empty intersection of activity, i.e., the two cells are active at diﬀerent times;
2. there is a non-null intersection of activity, i.e., their activities overlap;
3. the activity of one cell is a proper subset of the other cell, i.e., the activity of one cell occurs entirely
within the timespan of the activity of the other cell.
The time window for deﬁning the co-activity of two or more cells is two θ-periods [10, 115].
Schema entropy and mutual information. For each relationship ρk of the schema we computed its nor-
malized frequency of appearance pk and evaluated the resulting speciﬁc entropy,
H = −Σkpk log2 pk.
The speciﬁc entropy for the corresponding spatial map was evaluated by identifying the relationships ρk′ that
obtain between the corresponding representing regions and computing their appearance probabilities pk′.
Following the trajectory of the animal (Figure 1B), we could also detect the joint probability of appearance
pk,k′ of a given pair of relationships, both in the schema as well as in the map (ρk, ρk′), and then compute
their mutual information between the map and the schema,
MI = −ΣkΣk′ pk,k′ log2
pk,k′
pkpk′ .
The computational software used for topological analysis is JPlex, an open-source package implement-
ing Persistent Homology Theory methods developed by the Computational Topology group at Stanford
University [116].
VI.
ACKNOWLEDGMENTS
We thank Robert Phenix, Vicky Brandt and Loren Frank for helpful comments. The work was supported
in part by Houston Bioinformatics Endowment Fund (A.B. and Y.D.), the W. M. Keck Foundation grant for
pioneering research (A.B. and Y.D.) and by the NSF 1422438 grant (A.B. and Y.D.), and by the German
Research Foundation (Deutsche Forschungsgemeinschaft, DFG): SFB 874, project B2 (S.C.), a grant from
the Stiftung Mercator (S.C.).


## Page 18


18
VII.
REFERENCES
[1] Tolman, E. (1948). Cognitive maps in rats and men, Psychol. Rev., 55: 189-208.
[2] Best, P., White, A., Minai, A. (2001). Spatial processing in the brain: the activity of hippocampal place cells.
Annual. Rev. Neurosci. 24: 459-486.
[3] O’Keefe, J., Nadel, L. (1978). The hippocampus as a cognitive map, New York: Clarendon Press; Oxford
University Press. xiv, 570 pp.
[4] Redish A., Touretzky D. (1997). Cognitive maps beyond the hippocampus, Hippocampus, 7: pp. 15-35.
[5] McNaughton B., Battaglia F., Jensen O., Moser E., Moser M. (2006). Path integration and the neural basis of
the ’cognitive map’, Nat. Rev. Neurosci. 7: 663-678.
[6] Eichenbaum, H. (1999). Conscious awareness, memory and the hippocampus, Nat. Neurosci., 2: 775-776.
[7] Pouget, A., Dayan, P., Zemel, R. (2000). Information processing with population codes, Nat. Rev. Neurosci. 1:
125-132.
[8] Harnad, S. (1994). Why and how we are not zombies, Journal of Consciousness Studies 1: 164-167.
[9] Dabaghian, Y., Mmoli, F., Frank, L., Carlsson, G. (2012). A Topological Paradigm for Hippocampal Spatial
Map Formation Using Persistent Homology, PLoS Comput. Biol. 8: e1002581.
[10] Arai, M., Brandt, V., Dabaghian, Y. (2014). The Eﬀects of Theta Precession on Spatial Learning and Simpli-
cial Complex Dynamics in a Topological Model of the Hippocampal Spatial Map, PLoS Comput. Biol. 10:
e1003651.
[11] Alvernhe, A., Sargolini, F., Poucet, B. (2012). Rats build and update topological representations through ex-
ploration, Anim. Cogn. 15: 359-368.
[12] Poucet, B., Herrmann, T. (2001). Exploratory patterns of rats on a complex maze provide evidence for topo-
logical coding, Behav. Processes 53: 155-162.
[13] Alvernhe, A., Save, E., Poucet, B. (2011). Local remapping of place cell ﬁring in the Tolman detour task, The
European Journal of Neuroscience, 33:16961705.
[14] Shapiro, M., Tanila, H., Eichenbaum, H. (1997). Cues that hippocampal place cells encode: dynamic and
hierarchical representation of local and distal stimuli, Hippocampus 7: 624-642.
[15] Wu, X., Foster, D. (2014). Hippocampal Replay Captures the Unique Topological Structure of a Novel Envi-
ronment, The Journal of Neuroscience, 34: 6459-6469.
[16] Chen, Z., Kloosterman, F., Brown, E., Wilson, M. (2012). Uncovering spatial topology represented by rat
hippocampal population neuronal codes, J. Comput. Neurosci., 33: 227-255.
[17] Dabaghian, Y., Brandt, V., Frank, L. (2014). Reconceiving the hippocampal map as a topological template,
eLife 3:03476.
[18] Buzsaki, G. (2010). Neural syntax: cell assemblies, synapsembles, and readers, Neuron 68: 362-385.
[19] Russell, B. (1921) The analysis of mind, London, New York,: G. Allen & Unwin ltd.; The Macmillan company.
[20] Barbieri, R., Frank, L., Nguyen, D., Quirk, M., Solo, V., Wilson, M., Brown, E. (2004). Dynamic analyses of
information encoding in neural ensembles, Neural Comput. 16: 277-307.
[21] Frank, L., Stanley, G., Brown, E. (2004). Hippocampal plasticity across multiple days of exposure to novel
environments, J. Neurosci. 24: 7681-7689.
[22] Diba, K., Buzsaki, G. (2008). Hippocampal network dynamics constrain the time lag between pyramidal cells
across modiﬁed environments, J. Neurosci., 28: 13448-13456.
[23] Cheng, J., Ji, D. (2013). Rigid ﬁring sequences undermine spatial memory codes in a neurodegenerative mouse
model, eLife 2:e00647.
[24] Hayman, R., Verriotis, M., Jovalekic, A., Fenton, A., Jeﬀery, K. (2011). Anisotropic encoding of three-
dimensional space by place cells and grid cells, Nat. Neurosci., 14: 1182-1188.
[25] Yartsev, M., Ulanovsky, N. (2013). Representation of Three-Dimensional Space in the Hippocampus of Flying
Bats, Science 340: 367-372.
[26] Taube, J. (2011). Head direction cell ﬁring properties and behavioural performance in 3-D space, J. Physiol.
589: 835-841.
[27] Finkelstein, A., Derdikman, D., Rubin, A., Foerster, J., Las, L., Ulanovsky, N. (2015). Three-dimensional
head-direction coding in the bat brain, Nature 517: 159-164.


## Page 19


19
[28] Chen, A., DeAngelis, G., Angelaki, D. (2011). Representation of Vestibular and Visual Cues to Self-Motion in
Ventral Intraparietal Cortex, J. Neurosci. 31: 12036-12052.
[29] Swindale, N. (1996). Visual cortex: Looking into a Klein bottle, Current Biol. 6: 776-779.
[30] Barry, C., Burgess, N. (2007). Learning in a geometric model of place cell ﬁring, Hippocampus, 17: 786-800.
[31] O’Keefe, J., Burgess, N. (1996). Geometric determinants of the place ﬁelds of hippocampal neurons, Nature
381: 425-428.
[32] Guger, C., Gener, T., Pennartz, C., Brotons-Mas, J., Edlinger, G., Bermudez i Badia, S., Verschure, P., Schaﬀel-
hofer, S., Sanchez-Vives, M. (2011). Real-time Position Reconstruction with Hippocampal Place Cells, Front.
Neurosci. 5:85.
[33] Brown, E., Frank, L., Tang, D., Quirk, M., Wilson, M. (1998). A statistical paradigm for neural spike train de-
coding applied to position prediction from ensemble ﬁring patterns of rat hippocampal place cells, J. Neurosci.,
18: 7411-7425.
[34] Fenton, A., Muller, R., (1998). Place cell discharge is extremely variable during individual passes of the rat
through the ﬁring ﬁeld, Proc. Natl. Acad. Sci. 95: 3182-3187.
[35] Dabaghian, Y., Cohn, A., Frank, L., (2011). Topological Coding of the Hippocampus. In: Igelnik B, editor,
Computational Modeling and Simulation of Intellect: Current State and Future Perspectives, BMI Research
Inc., USA. pp. 293-320
[36] Chen, Z., Gomperts, S., Yamamoto, J., Wilson, M. (2014). Neural representation of spatial topology in the
rodent hippocampus, Neural Comput. 26: 1-39.
[37] Stella, F., Cerasti, E., Treves, A. (2013). Unveiling the metric structure of internal representations of space,
Front. Neural Circuits 7:81.
[38] Katz, Y., Kath, W., Spruston, N., Hasselmo, M. (2007). Coincidence detection of place and temporal context
in a network model of spiking hippocampal neurons, PLoS Comput. Biol. 3: e234.
[39] Brette, R. (2012). Computing with Neural Synchrony, PLoS Comput. Biol., 8: e1002561.
[40] Dehmer, M., Mowshowitz, A. (2011). A history of graph entropy measures, Info. Sci. 181: 57-78.
[41] Mowshowitz, A. (1968). Entropy and the complexity of graphs: I. An index of the relative complexity of a
graph, Bulletin of Mathematical Biophysics 30, pp. 175-204.
[42] Muller, R., Stead, M., Pach, J. (1996). The hippocampus as a cognitive graph, J. Gen. Physiol., 107: 663-694.
[43] Trullier, O., Meyer, J-A. (2000). Animat navigation using a cognitive graph, Biol. Cybern., 83: 271-285.
[44] Chrastil, R., Warren, W. (2014). From Cognitive Maps to Cognitive Graphs, PLoS One 9: e112544.
[45] Berge, C. (1982). The theory of graphs and its applications, Westport, Conn.: Greenwood Press.
[46] Aleksandrov, P. (1965). Elementary concepts of topology, New York: F. Ungar Pub. Co. 63 pp.
[47] Babichev, A., Memoli, F., Ji, D., Dabaghian, Y. (2015). Combinatorics of Place Cell Coactivity and Hippocam-
pal Maps, (arXiv:1509.01677).
[48] Harris, K., Csicsvari, J., Hirase, H., Dragoi, G., Buzsaki, G. (2003). Organization of cell assemblies in the
hippocampus, Nature 424: 552-556.
[49] Harris, K. (2005). Neural signatures of cell assembly organization, Nat. Rev. Neurosci., 6: 399-407.
[50] Hatcher, A. (2002). Algebraic topology, Cambridge; New York: Cambridge University Press.
[51] Dubrovin, B., Fomenko, A., Novikov, S. (1992). Modern geometry–methods and applications. New York:
Springer-Verlag.
[52] Curto, C., Itskov, V. (2008) .Cell groups reveal structure of stimulus space, PLoS Comput. Biol., 4: e1000205.
[53] Maurer, P., Cowen, S., Burke, S., Barnes, C., McNaughton, B. (2006). Organization of hippocampal cell
assemblies based on theta phase precession, Hippocampus 16: 785-794.
[54] Muller, R., Kubie, J., Ranck, J. (1987). Spatial ﬁring patterns of hippocampal complex-spike cells in a ﬁxed
environment, J. Neurosci. 7: 1935-1950.
[55] Liu, Y-M., Luo, M-K. (1997). Fuzzy topology, River Edge, NJ: World Scientiﬁc Pub. x, 353 pp.
[56] Zomorodian, A., Carlsson, G. (2005). Computing persistent homology, Discrete & Computational Geometry
33: 249–274.
[57] Ghrist, R. (2008). Barcodes: The persistent topology of data, Bulletin of the American Mathematical Society
45: 61-75.
[58] Hazarika, S., Cohn, A. (2001). Qualitative Spatio-Temporal Continuity, Proceedings of the International
Conference on Spatial Information Theory: Foundations of GIS, Springer-Verlag., New York, pp. 92-107.
doi:10.1007/3-540-45424-17
[59] Gotts, N., Gooday, J., Cohn, A. (1996). A Connection Based Approach to Common-Sense Topological De-
scription and Reasoning The Monist 79: 51-75.


## Page 20


20
[60] Renz, J., Rauh, R., Knauﬀ, M. (2000). Towards Cognitive Adequacy of Topological Spatial Relations, In:
Freksa C, Habel C, Brauer W, Wender K, editors, Spatial Cognition II Springer Berlin Heidelberg. pp. 184-
197.
[61] Cohn, A., Hazarika, S. (2001). Qualitative Spatial Representation and Reasoning: An Overview, Fundam. Inf.,
46: 1-29.
[62] Knauﬀ, M., Rauh, R., Renz, J. (1997). A Cognitive Assessment of Topological Spatial Relations: Results from
an Empirical Investigation. Proceedings of the International Conference on Spatial Information Theory: A
Theoretical Basis for GIS, Springer-Verlag. pp. 193-206.
[63] Goodrich-Hunsaker, N., Howard, B., Hunsaker, M., Kesner, R. (2008). Human topological task adapted for
rats: Spatial information processes of the parietal cortex, Neurobiol. Learn Mem., 90: 389-394.
[64] Wallgrun, J. (2010). Qualitative Spatial Reasoning for Topological Map Learning, Spatial Cognition & Com-
putation, 10: 207-246.
[65] Zeithamova, D., Schlichting, M., Preston, A. (2012). The hippocampus and inferential reasoning: Building
memories to navigate future decisions, Front. Hum Neurosci., 6.
[66] Cui, Z., Cohn, A., Randell, D. (1993). Qualitative and Topological Relationships in Spatial Databases, Proceed-
ings of the Third International Symposium on Advances in Spatial Databases Springer-Verlag. pp. 296-315.
[67] Cohn, A., Bennett, B., Gooday, J., Gotts, N. (1997). Qualitative Spatial Representation and Reasoning with the
Region Connection Calculus. Geoinformatica, 1: 275-316.
[68] Li, S., Cohn, A. (2012). Reasoning with topological and directional spatial information, Computational Intel-
ligence 28: 579-616.
[69] Gerevini, A., Renz, J. (1998). Combining Topological and Qualitative Size Constraints for Spatial Reason-
ing, Proceedings of the 4th International Conference on Principles and Practice of Constraint Programming,
Springer-Verlag. pp. 220-234.
[70] Lehmann, F., Cohn, A. (1994). The EGG/YOLK reliability hierarchy: semantic data integration using sorts
with prototypes, Proceedings of the third international conference on Information and knowledge management,
Gaithersburg, Maryland, United States: ACM. pp. 272-279.
[71] Gotts, N. (1994). Deﬁning a ’doughnut’ made diﬃcult. In: C. Eschenbach C. Habel and B. Smith (Eds.),
Topological Foundations of Cognitive Science, University of Hamburg, Hamburg, pp. 105-130.
[72] Frank, L., Brown, E., Wilson, M. (2000). Trajectory encoding in the hippocampus and entorhinal cortex,
Neuron 27: 169-178.
[73] Huang, Y., Brandon, M., Griﬃn, A., Hasselmo, M., Eden, U. (2009). Decoding movement trajectories through
a T-maze using point process ﬁlters applied to place ﬁeld data from rat hippocampal region CA1, Neural
Comput., 21: 3305-3334.
[74] Bennett, B. (1998). Determining Consistency of Topological Relations, Constraints 3: 213-225.
[75] Renz, J. (2002). Qualitative spatial reasoning with topological information, Berlin ; New York: Springer.
[76] Muller, R., Kubie, J. (1987). The eﬀects of changes in the environment on the spatial ﬁring of hippocampal
complex-spike cells, J. Neurosci. 7: 1951-1968.
[77] Colgin, L., Leutgeb, S., Jezek, K., Leutgeb, J., Moser, E., McNaughton, B., Moser, MB. (2010). Attractor-map
versus autoassociation based attractor dynamics in the hippocampal network, J. Neurophys., 104: 35-50.
[78] Lever, C., Wills, T., Cacucci, F., Burgess, N., O’Keefe, J. (2002). Long-term plasticity in hippocampal place-
cell representation of environmental geometry, Nature 416: 90-94.
[79] Leutgeb, J., Leutgeb, S., Treves, A., Meyer, R., Barnes, C., McNaughton, L., Moser, MB., Moser, E. (2005).
Progressive transformation of hippocampal neuronal representations in “morphed” environments, Neuron 48:
345-358.
[80] Wills, J., Lever, C., Cacucci, F., Burgess, N., O’Keefe, J. (2005). Attractor dynamics in the hippocampal
representation of the local environment. Science 308: 873-876.
[81] Touretzky, D., Weisman, W., Fuhs, M., Skaggs, W., Fenton, A., Muller, R. (2005). Deforming the hippocampal
map, Hippocampus 15: 41-55.
[82] Gothard, K., Skaggs, W., McNaughton, B. (1996). Dynamics of mismatch correction in the hippocampal en-
semble code for space: interaction between path integration and environmental cues, J. Neurosci., 16: 8027-
8040.
[83] Gothard, K., Skaggs, W., Moore, K., McNaughton, B. (1996). Binding of hippocampal CA1 neural activity to
multiple reference frames in a landmark-based navigation task. J. Neurosci. 16: 823-835.
[84] Etienne, A., Jeﬀery, K. (2004). Path integration in mammals, Hippocampus 14: 180-192.
[85] McNaughton, B., Barnes, C., Gerrard, J., Gothard, K., Jung, M., Knierim, J., Kudrimoti, H., Qin, Y., Sk-


## Page 21


21
aggs, W., Suster, M., Weaver, K. (1996). Deciphering the hippocampal polyglot: the hippocampus as a path
integration system, J. Exp. Biol. 199: 173-185.
[86] Poucet, B. (1993). Spatial cognitive maps in animals: new hypotheses on their structure and neural mecha-
nisms, Psychol. Rev., 100: 163-182.
[87] Eichenbaum, H. (2000). A cortical-hippocampal system for declarative memory, Nat. Rev. Neurosci. 1: 41-50.
[88] Konkel, A., Cohen, N. (2009). Relational memory and the hippocampus: Representations and methods, Front.
Neurosci. 3(2): 166174.
[89] Shrager, Y., Bayley, P., Bontempi, B., Hopkins, R., Squire, L. (2007). Spatial memory and the human hip-
pocampus, Proc. Natl. Acad. Sci. 104: 2961-2966.
[90] Soei, E., Koch, B., Schwarz, M., Daum, I. (2008). Involvement of the human thalamus in relational and non-
relational memory, European J. Neurosci., 28: 2533-2541.
[91] Eichenbaum, H., Dudchenko, P., Wood, E., Shapiro, M., Tanila, H. (1999). The hippocampus, memory, and
place cells: is it spatial memory or a memory space? Neuron 23: 209-226.
[92] Wood, E., Dudchenko, P., Eichenbaum, H. (1999). The global record of memory in hippocampal neuronal
activity, Nature 397: 613-616.
[93] Fortin, N., Agster, K., Eichenbaum, H. (2002). Critical role of the hippocampus in memory for sequences of
events, Nat. Neurosci. 5: 458-462.
[94] Fortin, N., Wright, S., Eichenbaum, H. (2004). Recollection-like memory retrieval in rats is dependent on the
hippocampus, Nature 431: 188-191.
[95] Sauvage, M., Fortin, N., Owens, C., Yonelinas, A., Eichenbaum, H. (2008). Recognition memory: opposite
eﬀects of hippocampal damage on recollection and familiarity, Nat. Neurosci. 11: 16-18.
[96] Foster, D., Wilson, M. (2006). Reverse replay of behavioural sequences in hippocampal place cells during the
awake state, Nature 440: 680-683.
[97] Louie, K., Wilson, M. (2001). Temporally Structured Replay of Awake Hippocampal Ensemble Activity during
Rapid Eye Movement Sleep, Neuron 29: 145-156.
[98] Gupta, A., van der Meer M., Touretzky, D., Redish, A. (2010). Hippocampal Replay Is Not a Simple Function
of Experience, Neuron 65: 695-705.
[99] Dragoi, G., Tonegawa, S. (2011). Preplay of future place cell sequences by hippocampal cellular assemblies,
Nature 469: 397-401.
[100] Dragoi, G., Tonegawa, S. (2013). Distinct preplay of multiple novel spatial experiences in the rat Proc. Natl.
Acad. Sci., 110(22):9100-5.
[101] Cheng, S. (2013). The CRISP theory of hippocampal function in episodic memory, Front. Neural Circuits 7:88.
[102] Buhry, L., Azizi, A., Cheng, S. (2011). Reactivation, Replay, and Preplay: How It Might All Fit Together.
Neural Plast. vol. 2011, Article ID 203462.
[103] Azizi, A., Wiskott, L., Cheng, S. (2013). A computational model for preplay in the hippocampus, Front.
Comput. Neurosci. 7:161.
[104] Cacucci, F., Yi, M., Wills, T., Chapman, P., O’Keefe, J. (2008). Place cell ﬁring correlates with memory deﬁcits
and amyloid plaque burden in Tg2576 Alzheimer mouse model, Proc. Natl. Acad. Sci. 105: 7863-7868.
[105] Robbe, D., Montgomery, S., Thome, A., Rueda-Orozco, P., McNaughton, B., G. Buzsaki. (2006). Cannabinoids
reveal importance of spike timing coordination in hippocampal function, Nat. Neurosci., 9: 1526-1533.
[106] Silvers, J., Tokunaga, S., Berry, R., White, A., Matthews, D. (2003). Impairments in spatial learning and
memory: ethanol, allopregnanolone, and the hippocampus, Brain. Res. Rev., 43: 275-284.
[107] Gerrard, J., Kudrimoti, H., McNaughton, B., Barnes, C. (2001). Reactivation of hippocampal ensemble activity
patterns in the aging rat, Behav. Neurosci., 115: 1180-1192.
[108] Robitsek, R., Fortin, N., Koh, M., Gallagher, M., Eichenbaum, H. (2008). Cognitive aging: a common decline
of episodic recollection and spatial memory in rats, J. Neurosci., 28: 8945-8954.
[109] Wilson, I., Ikonen, S., Gureviciene, I., McMahan, R., Gallagher, M., Eichenbaum, H., Tanila, H. (2004).
Cognitive aging and the hippocampus: how old rats represent new environments, J. Neurosci. 24: 3870-3878.
[110] Hoﬀman, K., Babichev, A., Dabaghian, Y. (2016). Topological mapping of space in bat hippocampus,
(arXiv:1601.04253).
[111] Brown, N., Nguyen, D., Frank, L., Wilson, M., Solo, V. (2001). An analysis of neural receptive ﬁeld plasticity
by point process adaptive ﬁltering. Proc. Natl. Acad. Sci. 98: 12261-12266.
[112] Frank, L., Brown, E., Stanley, G. (2006). Hippocampal and cortical place cell plasticity: implications for
episodic memory, Hippocampus 16: 775-784.
[113] Ahmed, O., Mehta, M. (2009). The hippocampal rate code: anatomy, physiology and theory, Trends Neurosci.


## Page 22


22
32: 329-338.
[114] Ligozat, G. (2013). Allen’s Calculus. Qualitative Spatial and Temporal Reasoning, John Wiley & Sons, Inc.
Hoboken, NJ., pp. 1-28.
[115] Mizuseki, K., Sirota, A., Pastalkova, E., Buzsaki, G. (2009). Theta oscillations provide temporal windows for
local circuit computation in the entorhinal-hippocampal loop, Neuron 64: 267-280.
[116] (JPlex freeware). (2011). Computational Topology group, Stanford University.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]