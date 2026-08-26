---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.09630v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1903.09630v3_How_the_Brain_Transitions_from_Conscious_to_Subliminal_Perception

> Source: 1903.09630v3_How_the_Brain_Transitions_from_Conscious_to_Subliminal_Perception.pdf

> Pages: 10

---


## Page 1


How the Brain Transitions from Conscious to Subliminal Perception
Francesca Arese Lucinia, Gino Del Ferraroa,b, Mariano Sigmanc,d,e, Hern´an A. Maksea
aLevich Institute and Physics Department, City College of New York, New York, NY 10031, USA
bDepartment of Radiology, Memorial Sloan Kettering Cancer Center, New York, NY 10065, USA
cLaboratorio de Neurociencia, Universidad Torcuato Di Tella, Av. Pres. Figueroa Alcorta 7350, Buenos Aires, Argentina
dCONICET (Consejo Nacional de Investigaciones Cientﬁcas y Tcnicas), Sarmiento 440, Buenos Aires, Argentina
eFacultad de Lenguas y Educaci´on, Universidad Nebrija,Calle de Sta. Cruz de Marcenado, 27, 28015 Madrid, Spain
Abstract–We study the transition in the functional networks that characterize the human brains’ conscious-state to an
unconscious subliminal state of perception by using k-core percolation. We ﬁnd that the most inner core (i.e., the most
connected kernel) of the conscious-state functional network corresponds to areas which remain functionally active when the
brain transitions from the conscious-state to the subliminal-state. That is, the inner core of the conscious network coincides
with the subliminal-state. Mathematical modeling allows to interpret the conscious to subliminal transition as driven by
k-core percolation, through which the conscious state is lost by the inactivation of the peripheral k-shells of the conscious
functional network. Thus, the inner core and most robust component of the conscious brain corresponds to the unconscious
subliminal state. This ﬁnding imposes constraints to theoretical models of consciousness, in that the location of the core of
the functional brain network is in the unconscious part of the brain rather than in the conscious state as previously thought.
Key words: conscious and subliminal perception, percolation theory, k-core percolation, brain networks
Introduction
The human brain as a natural system has received growing at-
tention. The scientiﬁc literature has explored, from a mathemat-
ical and theoretical physics perspective, the sensitivity and rel-
evance of diﬀerent properties of brain topology from a network
standpoint (Dehaene & Naccache, 2001; Greicius et al. , 2003;
Sporns et al. , 2005; Hagmann et al. , 2008; Van Den Heuvel &
Pol, 2010; Bullmore & Sporns, 2012; Gallos et al. , 2012; Crad-
dock et al. , 2013; Sporns, 2013; Deco et al. , 2014). Many
scales and levels of detail have been investigated, from com-
pletely deﬁned networks of hundreds of neurons in species with
particularly small brains (Yan et al. , 2017) to macroscopic sum-
maries of networks up to 100 billion neurons of the mammalian
brain (Sporns et al. , 2005; Sporns, 2013; Del Ferraro et al. ,
2018; Van Vugt et al. , 2018).
Earlier studies concentrated on the distribution of degree
(the number of neighbors on each node), the clustering (the
likelihood that co-neighbors of a node will also be neighbors),
or the diameter (the typical distance between two nodes of the
network) (Sporns et al. , 2005; Rubinov & Sporns, 2010; Bull-
more & Sporns, 2012; Bardella et al. , 2016). A second wave
of studies has combined these measures together, for instance
in the notion of small-world networks and weak links (Watts &
Strogatz, 1998; Gallos et al. , 2012).
Several other statistical markers of networks have been in-
vestigated and recently the idea of k-core (Seidman, 1983; Pit-
tel et al. , 1996) has received substantial attention in network
analysis since it provides a topological notion of the structural
skeleton of a network (Dorogovtsev et al. , 2006; Carmi et al.
, 2007; Alvarez-Hamelin et al. , 2008; Hagmann et al. , 2008;
Kitsak et al. , 2010). Theoretical analyses (Morone et al. , 2019)
have shown that, the k-core may also be an indicator for the sta-
bility of complex biological systems. Of particular importance
for the scope of this paper is the analysis done in (Hagmann
et al. , 2008; Lahav et al. , 2016), which demonstrate that the
k-core of the network is located in the posterior regions of the
brain.
In this work we use network measures as a tool to inquire
on one of the most challenging questions in brain science: the
signatures of conscious and subliminal perception. We use the
notion of k-core derived from theoretical physics, as a funda-
mental measure of centrality and robustness within a network,
to address the question arising from brain science concerning
what brain markers characterize the conscious →subliminal
transition.
Recent theoretical results (Morone et al. , 2019) highlight
how the resilience of neural dynamical systems is controlled by
the strength of the interaction couplings and that, furthermore,
the most robust part of the system under interaction coupling
change is the maximum k-core of the corresponding network.
This study inspired us to investigate the maximum k-core of the
network for the system under study and verify if it has a neu-
roanatomical correspondence. If one can give meaning to such
robust subset of the network, then the k-core percolation would
represent a meaningful method to model of the corresponding
transition.
We build on a classic study of human brain activations per-
formed by Dehaene et al.
(Dehaene et al. , 2001).
These
experiments measure, through functional Magnetic Resonance
Preprint submitted to Elsevier
May 30, 2019
arXiv:1903.09630v3  [q-bio.NC]  29 May 2019


## Page 2


Imaging (fMRI), participants that either record seeing an image
ﬂashed at millisecond intervals on a computer screen in front
of them (conscious state), or they do not (subliminal state). We
build the functional brain networks of the obtained conscious
state based on temporal similarity of activations.
The main theoretical question that we then ask is how the
transition from conscious to subliminal state can be modeled in
terms of network theory and what subset of the conscious-state
network describes the ﬁnal state of this transition to the sub-
liminal state. We contrast two possible hypotheses. A natural
idea is that the k-core decomposition method may index regions
that are more relevant for conscious processing. This intuition
comes from several theoretical studies of the neural substrate
of consciousness advanced by Dehaene, Tononi and collabo-
rators (Dehaene, 2014; Tononi et al. , 2016), which argue that
vast broadcasting, dense and ﬂexible connectivity may be a cen-
tral feature of consciousness. Diﬀerently, several psychological
theories, most notably deriving from the work of Benjamin Li-
bet (Libet, 1985), have implied that subliminal processing pro-
vides a kernel for all thought. In this view, consciousness is
‘merely’ a read-out of a vast and robust cascade of processes.
Discriminating between these two theories requires to un-
derstand whether the k-core of a set of conscious activations is
associated with speciﬁc nodes of the network that make this ac-
tivation conscious or, instead, with a subliminal stream which
serves as a structural core for subsequent conscious activations.
Our analysis supports the latter hypothesis: the functional net-
work which models the subliminal-state of the brain corresponds
to the maximum k-core of the more extended functional net-
work which models the conscious-state.
The article is organized as follows. First we give an illustra-
tion of the experiments performed by Dehaene et al. (Dehaene
et al. , 2001), of which we analyze all data, and we then provide
a corresponding deﬁnition of conscious- and subliminal-state of
the brain. In Section Experimental Procedure we describe the
methodology employed to construct functional brain networks
of the conscious-state and introduce the concept of k-core de-
composition as a trimming process to identify network struc-
tures. Section Results discusses our ﬁndings and shows that
nodes in the maximum k-core of the conscious-state network
correspond to the subliminal-state of fMRI activation, both at
the brain module- and node-level. In Section Discussion we
elaborate on the interpretation of our results by summarizing
the theory developed in Morone et al. (2019) on the role of
the k-core as indicator of network robustness. In the same sec-
tion we also contextualize our ﬁndings within two conscious-
ness theories developed by Libet and Dehaene-Tononi. Section
Conclusions summarizes the study and draws the conclusions.
Data
The data we use in our study and analysis were collected by
Dehaene et al. (2001) and are brieﬂy explained next. In the
investigation discussed in Dehaene et al. (2001) a subject en-
dures two diﬀerent experiments for a speciﬁc time interval. In
this time frame four letter words are presented to a participant
HELP
FAME
30 ms
70 ms
70 ms
70 ms
30 ms
70 ms
70 ms
70 ms
Time 
direction 
Conscious state
Subliminal state
70 ms
or
or
70 ms
Figure 1: Simpliﬁed sketch of the experiment (Dehaene et al. , 2001). The
left illustration portrays the stream sequence used to cause the conscious-state
perception, where the four lettered word is presented preceded and succeeded
by blank screens. The right illustration portrays the experiment where the word
is sandwiched between distractors, or masks, which inhibits the conscious per-
ception of the word and causes the subliminal-state activation. For each of
these two experiments a control sequence is presented in which blank images
are displayed instead of words.
who undergoes fMRI screening. Each word is ﬂashed on a com-
puter screen either sandwiched between blank pictures or pre-
ceded and succeeded by images on the screen called distractors
or masks (Dehaene et al. , 2001), as illustrated in Fig. 1. Words
in both scenarios are ﬂashed for 30ms and the sequence of blank
screens and words (or masks) is repeated, with a ﬁxed order, for
a total of 5 minutes.
In the ﬁrst type of experiments a word is ﬂashed on the
computer screen sandwiched between blank images, designed
to produce a conscious perception of the word by the subject,
who, indeed, reports to have seen the word on the screen af-
ter each stream of images. We will refer to the fMRI signal of
this state as conscious or unmasked (see Fig. 1). The second
type of experiments are, on the contrary, designed not to pro-
duce any active perception of the word, which is in fact ﬂashed
sandwiched between scrambled words. The distractor images,
indeed, act as ‘masks’ and the subject does not consciously de-
tect the word on the screen. We will refer to the fMRI signal
of this state as masked or subliminal (see Fig. 1). For each of
these two states a corresponding control sequence is presented
in which the progression of the images on the screen remains
the same for each case, but blank screens are displayed instead
of words (see Fig. 1). These control conditions are used to es-
timate the background brain activity in order to better evaluate
the activation of each brain voxel (Dehaene et al. , 2001). The
fMRI signal was obtained for 15 subjects, and each of them
repeated the experiment 5 times, thus data in Dehaene et al.
(2001) it was collected for 75 diﬀerent fMRI streams.
The acquired BOLD signal is processed using SPM99 (UCL,
1999). The fMRI time series are then analyzed by using the
widely adopted Generalized Linear model (Smith et al. , 2004),
which produces as output the activation map (AM). Fig. 2a
shows the AM of the conscious state (P < 10−6), for a repre-
2


## Page 3


C
A
Conscious state
Subliminal state
B
Fusiform 
Gyrus (L)
Fusiform 
Gyrus (R)
Precentral  
Gyrus (L)
Superior Occipital Gyrus (L)
Superior Occipital 
Gyrus (R)
SMA
Premotor Cortex (R)
Fusiform  
Gyrus (L); 
Inferior 
Temporal  
Gyrus (L)
Fusiform 
Gyrus (R)
Precentral 
Gyrus (L); 
Premotor  
Cortex (L); 
Middle frontal 
Gyrus (L)
Superior 
occipital  
Gyrus (L); 
Angular  
Gyrus (L)
Superior 
Occipital  
Gyrus (R); 
Angular  
Gyrus (R)
Premotor  
Cortex (R)
Supplementary 
Motor Area 
(SMA)
Figure 2: Activation map and functional network of the conscious-state. a) Activation map of the conscious-state network for a representative subject (P < 10−6),
left and right brain areas are abbreviated with L and R, respectively. Sagittal and axial view of the brain are shown. The fusiform gyrus and the inferior temporal lobe
are involved in visual and word processing/recognition. The middle frontal gyrus is involved in working memory and attention, whereas the premotor cortex, the
precentral gyrus, and the supplementary motor area (SMA) produce motor signaling. The superior occipital and the angular gyrus are involved in visual functions
and transfer of visual information. b) Resulting functional network relative to the activation map of panel a) constructed with the procedure described in ‘Functional
brain networks of the conscious state’ Section. c) Activation map of the subliminal-state network (P < 10−2), P-values are chosen accordingly to Ref. (Dehaene
et al. , 2001) in all panels.
sentative subject, whereas Fig. 2c illustrates the fMRI activa-
tion map of the subliminal state (P < 10−2) averaged across
subjects (P-values in both cases are chosen accordingly to (De-
haene et al. , 2001) and, for illustration, all the active nodes are
shown with the same activation). Voxels are classiﬁed as be-
longing to a certain brain area with respect to their anatomical
location and each brain area (module) is colored diﬀerently in
the ﬁgures. For brevity, in the following, we will refer to all the
active anatomical regions depicted with the same color in Fig. 2
with the name of the ﬁrst cluster in the legend, for each speciﬁc
color.
By comparing the activation map of the conscious and sub-
liminal state, shown respectively in Fig. 2a and Fig. 2c, we
note that some brain regions are active in both brain states, i.e.
the fusiform gyrus (yellow and red module) and the left precen-
tral gyrus (green module). These regions are, in addition, the
only ones characterizing the activation of the subliminal state.
The fMRI activation in each conscious experiment spreads fur-
ther and involves additional clusters, for the case shown in Fig.
2a, for instance, it involves the left and right superior occipital
gyrus (light blue and blue cluster respectively), the right pre-
motor cortex (pink cluster), and the supplementary motor area
(SMA) (purple cluster).
Experimental Procedure
This Section illustrates the procedure we employ to investi-
gate the transition from the conscious to the subliminal state,
as described in the Introduction Section. From the fMRI ac-
tivation map of the scans acquired during the conscious-state
experiment we construct the functional brain network of this
brain state, for each individual and for each single stream. Ac-
tive fMRI voxels constitute the nodes of the network and links
among these nodes are assigned by using pairwise correlations
between the fMRI time series of the active voxels, with a pro-
cedure that we describe next (Fig. 2b shows one instance of
this conscious network, corresponding to the fMRI activation
of Fig. 2a).
Ideally, we would aim to build similar functional brain net-
works for the subliminal state, by employing the same proce-
dure, so to have brain networks for the conscious- and subliminal-
state experiment and then study the transition from one to the
other. As discussed in Section Data though, the subliminal state
is characterized by a weaker overall fMRI activation, which
therefore requires to apply a higher P-value threshold. As a
consequence, noise eﬀects play a greater role on the fMRI time
series of the subliminal-state compared to the conscious-state
time signals. Furthermore, the choice of a higher P-value pro-
duces subliminal AMs (obtained by comparing this state to the
relative control stream) which present, in addition to clustered
activity, isolated voxels spread across the brain that we consider
3


## Page 4


false positives. In order to reduce these noise eﬀects and get rid
of this false positive activity, we averaged the activation maps
of the subliminal state across streams and subjects, obtaining
one ﬁnal activation map for this state where voxels are active if
appearing in at least 80% of all activation maps. Furthermore,
building a network for the subliminal state would not give any
relevant information needed to explain the conscious →sub-
liminal transition since the subliminal state is needed just to
compare the reduction of the conscious network to validate any
possible observation. Therefore, we limited the use of the sub-
liminal activation map as a benchmark for the study of the con-
scious →subliminal transition (Fig. 2c shows this ﬁnal map)
without constructing a subliminal-state functional network.
After we have built the functional brain networks for the
conscious-state we trim each of these structures by performing
removal of the nodes belonging to diﬀerent k-shells (peripher-
ical nodes deﬁned later in Sec. k-Core Percolation), from low
to high value of k. The purpose of this trimming process it to
identify those nodes which belong to each speciﬁc k-core and
investigate whether, from this analysis, we can identify some
pattern in the brain network structure of the conscious state,
across subjects. We then investigate whether there exist mark-
ers which can help us identify the network diﬀerences between
the conscious- and the subliminal-state as well as illuminate on
the transition between these brain states. This procedure is de-
scribed in details in Subsection k-core percolation.
Functional brain networks of the conscious state
For each subject and each fMRI stream of the conscious-state
experiment we construct the functional brain network, follow-
ing the approach described in (Bullmore & Sporns, 2009; Gal-
los et al. , 2012), for a total of 75 networks (15 subjects, 5 fMRI
streams each). As mentioned, the nodes in each of these net-
works are the active voxels in the corresponding fMRI activa-
tion map. Links are assigned based on the thresholded pairwise
correlations of the registered fMRI signal between node i and j,
denoted as Ci j, as we explain in more details in the following.
Brain networks show a modular organization (Sporns, 2013)
where diﬀerent brain regions are specialized in the performance
of diﬀerent cognitive tasks.
In order to depict this modular
structure, we group the active voxels in brain clusters according
to their anatomical location (see Fig. 2). This spatial organiza-
tion suggests to distinguish between links that connect nodes
within the same cluster, that we call in-links, and long range
edges connecting nodes in diﬀerent clusters, that we call out-
links, as described in (Gallos et al. , 2012).
Following standard literature (Bullmore & Sporns, 2009;
Gallos et al. , 2012), we assign the links by thresholding the
cross-correlation matrix in order to get rid of the weakest con-
nections, such that two nodes i and j are wired together with the
assigned weighted link Cij iﬀCij ≥λ, with λ a tunable thresh-
old parameter. Accordingly, each λ threshold value deﬁnes a
diﬀerent functional network, identiﬁed by the thresholded cor-
relation matrix that we denote as Cij(λ). The threshold param-
eter tunes the sparsity of this resulting network and therefore
the size of its giant connected component (GCC). For λ = 1 the
 0
 0.2
 0.4
 0.6
 0.8
 1
 0.65
 0.7
 0.75
 0.8
 0.85
 0.9
 0.95
 1
GC
threshold of the cij
Percolation plot for a brain network
0.65
0.85
0.8
0.75
0.7
0.9
0.95
1
Normalized size of network 
0.0
1.0
0.8
0.6
0.4
0.2
λ
λin
λo u t
100
200
300
400
500
600
700
800
100 200 300 400 500 600 700 800
0.8
0.6
0.4
0.2
0.0
1.0
A
B
Figure 3:
Functional network construction. a) Percolation plot, i.e. the
GCC of a network deﬁned by the correlation matrix Cij(λ) vs the penalization
parameter λ is shown. The orange dot in the plot indicates the value of λin
used to ﬁx the in-links within the two brain modules shown pictorially in the
panel. The green dot pictures the value of λout employed to ﬁx the out-links
connecting the same two modules together. b) Resulting thresholded correlation
matrix according to panel a) of the functional network obtained with the above
procedure.
threshold is maximum and the nodes are isolated, so the GCC
= 0. By decreasing λ, more and more nodes connect together
and the GCC of the resulting network increases continuously
until it reaches the unit value. Fig. 3a shows the behaviour of
GCC vs λ for a representative subject.
By following (Gallos et al. , 2012), we ﬁx the λ parameter
through a ‘percolation’ procedure described next. Each sharp
discontinuity in Fig. 3a is due to the merging of connected
brain clusters which abruptly increase the size of the GCC. At
each one of these transitions we assign the in- and out-links of
the brain clusters which connect together. An in-link between a
node i and j within each of these clusters is assigned by Ci j iﬀ
Ci j ≥λin, where λin is the value of λ right before the sharp tran-
sition at which the clusters merge occurs, coming from higher
to lower λ values (see orange dot in Fig. 3a). An out-link be-
tween a node i and j belonging to diﬀerent clusters is assigned
by the thresholded correlation matrix Ci j(λout), where λout is
the value of λ right after the sharp transition (green dot in Fig.
3a). Fig. 3a illustrates this procedure and the resulting network
pictorially, for a representative subject. The adjacency matrix
of the ﬁnal architecture is shown in Fig. 3b, where nodes are
ordered sequentially according to their cluster association, in
4


## Page 5


ks = 2
ks = 3
ks = 1
Figure 4:
Cartoon of a 3-core network. k-shells are deﬁned as the set of
nodes that belong to the k-core but not the k + 1-core. As illustrated, k-shells
are concentric; low k-shells are located in the outer part of the network, while
for increasing k, nodes are situated in the most focal part until one reaches the
highest k-shell, which corresponds to the maximum k-core, located at the center
of the graph.
order to show the brain network’s modular structure.
We note that other methods (Hermundstad et al. , 2013;
Anzellotti & Coutanche, 2018) could be used to build the func-
tional networks . Our choice on the use of the percolation pro-
cedure to build such architecture was driven by the constraint
that brain networks are sparse and such procedure guarantees
sparsity by not overestimating the number of links between dif-
ferent clusters. We stress that the wiring only reﬂects func-
tional relations among fMRI active voxels and, in general, dif-
fers from the structural wiring obtained, for instance, through
diﬀusion tensor imaging or other method of physical connec-
tivity (Honey et al. , 2009). Thus, all our analysis and re-
sults must be considered as grounded on the functional network
framework.
k-Core percolation
The concept of k-core has been ﬁrstly introduced in social sci-
ences (Seidman, 1983) to describe network cohesion and, since
then, it has been applied in many contexts, to describe robust-
ness of random networks (Dorogovtsev et al. , 2006), viral spread-
ing in social networks (Kitsak et al. , 2010) and large-scale
structure of the brain (Hagmann et al. , 2008).
For a given architecture, the k-core is the maximal sub-
graph, not necessarily globally connected, which consists of all
the nodes with at least k neighbours. This subnetwork can be
obtained by removing iteratively all the nodes which have less
than k connections. Thus, to extract the k-core one starts prun-
ing all the nodes with degree less than k. The removal of these
nodes reduces the degree of their neighbors that can then drop
below k. Thus, these nodes should be removed in turn, and the
procedure iterates until no more nodes can be removed. The
remaining structure is the k-core of the network (see Fig. 4).
For a given k, the k-core includes cores with higher k, thus
the 1-core includes the 2-core, the 2-core includes the 3-core
and so forth. Each k-core consists of the nodes in the periph-
ery which is called k-shell (labelled ks) and the resting k + 1-
core. The k-shell is, therefore, the region of the k-core which is
2
1
6
4
3
7
1
10
20
30
40
50
ks
0
20
10
30
40
50
60
70
80
90
1
10
20
30
40
50
Occupancy
Figure 5:
k-Shell occupancy for the conscious network of a representative
subject. The distribution presents a U-shape: high population of nodes in the
lowest and highest k-shells. We observe that shells with the lowest k are inhab-
ited by nodes which belong to all the 7 brain clusters which are fMRI active in
the brain. On the contrary, the maximum k-shell, the inner core of the network,
is made by nodes which belong to only 3 clusters which, more importantly, are
the only fMRI active clusters of the subliminal-state.
not included in the k + 1-core (see Fig. 4). Therefore the net-
work has a nested structure made of k-core subnetworks with
increasing k and k-shells of order ks. The innermost core of
the network corresponds to the structure with the maximum k-
core, called kmax
core, which is a topological invariant of the network
(Dorogovtsev et al. , 2006).
For each one of the 75 conscious-state network, we can then
compute the k-core and k-shell occupancy, i.e. the number of
nodes which occupy each k-core or k-shell with a given k. An
interesting property of these networks emerges when one ex-
amines the nodes and the nodes’ brain anatomical area in each
k-shell. We discuss the results of this analysis in the next ses-
sion.
Results
The maximal k-core of the conscious network corresponds
to the subliminal-state
Once we have performed the k-core trimming process as de-
scribed in the previous Section, we can calculate the occupancy
of each k-shell, for each subject, that is, the number of nodes
in each k-shell. Fig. 5 illustrates this occupancy for a repre-
sentative conscious-state network. We note that, interestingly,
the distribution presents a U-shape: it shows very high occu-
pancy values for both very small and very high k-shell values,
and low occupancy for the intermediate k-shell values. This
shape of the distribution is consistent throughout all the con-
scious networks analyzed. Reference Burlesson-Lesser et al.
(2019) attributes the U-shape of the occupancy distribution to
the stability of the system: the high population of nodes in the
lowest and highest k-shells suggests network robustness against
both random local and global failure, thus making the brain a
resilient system under these kind of perturbations. The same
feature is also observed in ecosystems and ﬁnancial networks
5


## Page 6


Subliminal state
Conscious state
  
b
0
10
20
30
40
50
0
100
200
600
500
400
300
# nodes in each
1-core
10-core
5-core
percolation
kmax
core
kcore
kcore
kcore
Fusiform Gyrus (L)
Fusiform Gyrus (R)
Precentral Gyrus (L)
10-core
1-core
5-core
kmax
core
C
A
B
Figure 6: k-Core decomposition illustrated both in the activation brain map and in the functional network. a) Eﬀect of the k-core trimming process on the activation
map of the conscious-state, for increasing k-values. Nodes located in the low k-cores belong to all the brain clusters, on the contrary, nodes in the kmax
core belong to
the fusiform gyrus and left precentral gyrus (yellow, red, and green modules). b) Number of nodes in each k-core c) Same k-core decomposition of panel a), with a
diﬀerent visualization made on the functional network. Same considerations on the kmax
core apply.
(Burlesson-Lesser et al. , 2019) and it is general feature of many
networks called the core-periphery structure (Corradino, 1990;
Krugman, 1996; Borgatti & Everett, 2000; Zhang et al. , 2015;
Verma et al. , 2016).
We further observe that for the subject shown in Fig. 5 the
k-shells with small k’s are populated by nodes that belong to
any fMRI active module and, therefore, nodes that are spread
across all the active brain regions. More interestingly, Fig. 5
emphasizes that nodes which inhabit the k-shells with the high-
est k (k = 50 for this subject) belong exclusively to those brain
modules that are the only active clusters in the subliminal-state,
namely the fusiform gyrus and the left precentral gyrus (yellow,
red and green in Fig. 2c).
Figure 6 shows pictorially the k-core decomposition process
for the same subject presented in Fig. 5. Figure 6a illustrates
the progressive inactivation of the fMRI active voxels, based
on their k-core in the conscious-state network, while Fig. 6b
shows the occupancy number in each of these k-cores, i.e. the
number of nodes in each k-core. Figure 6c shows the k-core
decomposition process by highlighting the network connectiv-
ity. As discussed for Fig. 5, Fig. 6c shows that the kmax
core for
this particular conscious-state network is made by the fusiform
gyrus (yellow and red cluster) and by the left precentral gyrus
(green cluster), which are the only fMRI active clusters in the
averaged subliminal-state activation map.
To verify whether these results are statistically signiﬁcant
we perform the following analysis. For each of the 75 conscious-
state graphs we generated 106 new architectures obtained by
randomly rewiring the original network and keeping constant
the degree of each node. We then apply k-core decomposition
to each of these 106 random networks and compute the k-shell
occupancy. The obtained occupancy is then averaged across the
generated random networks and compared with the k-shell oc-
cupancy of the conscious-state network from which the random
architectures are created. Results are shown in Fig. 7 for a rep-
resentative subject and illustrate two interesting points. First,
the functional conscious-state network has a much higher kmax
core
than the averaged random case. Second, the average occupancy
distribution of the random networks shows the same U-shape
feature that we found in all the functional conscious-state net-
works obtained from the fMRI signal. This suggests that the
source of this shape is related to the degree distribution of the
nodes, being this distribution the same both in real conscious-
state and randomly generated networks. We mention that al-
though Fig. 7 refers to a representative case, we found qualita-
tively the same results for all the 75 conscious-state networks.
As already noted, results of Fig. 6 illustrate that, for this
representative subject, nodes which populate the kmax
core of the
conscious-state network belong to those clusters which are the
only active ones in the averaged subliminal-state activation map
(see Fig. 2c). In order to check whether this result is consistent
across all the conscious-state networks we performed a group
analysis at the clusters level. For each of the 75 conscious net-
works we assign count 1 to the cluster of nodes belonging to
the kmax
core. For instance, for the particular network of Fig. 5 we
assign count 1 to clusters 1, 2 and 3 (yellow, red and green
respectively, which populate the kmax
core = 50). The normalized
occupation number of the clusters in the kmax
core across conscious-
state networks is shown in Fig. 8, where clusters have been
ordered progressively. The green histogram represents the fre-
quency with which each cluster appears in the kmax
core. These re-
sults are compared to random ones illustrated by the blue his-
togram. The probability that each cluster is, at random, in the
kmax
core is 1/7 of the sum of counts of all modules which, when
normalized with respect to the number of conscious networks
analyzed (75 networks), translates to a 30% chance to populate
the kmax
core (see Fig. 8).
This comparison not only shows that the fusiform gyrus and
the left precentral gyrus (cluster 1, 2 and 3 in Fig. 8) are those
which mostly populate the kmax
core of the conscious-state network
across subjects, it also points out that this is not due to a ran-
dom eﬀect (P = 10−5). As reported above, these clusters are the
6


## Page 7


ks
0
30
20
10
40
50
60
Occupancy
0
40
20
60
80
100
120
140
160
Figure 7: k-Shell occupancy distribution for a representative subject (all other
subjects show similar results). Comparison between real conscious-state and a
random control network generated as described in Section Results. Random
networks exhibit a lower value of the maximum k-shells compared to the real
network, a behavior common to all the conscious-state networks (p < 10−6).
only active ones in the subliminal-state experiment. The other
four clusters (4 to 7 in Fig. 8) populate the kmax
core with a normal-
ized frequency which is less than a random eﬀect, making their
presence in the maximum k-core statistically less signiﬁcant.
As a further test, we check whether the above group results
at the cluster level are also consistent at the node level. In other
words, we investigate whether, across networks, the nodes in
the kmax
core of the conscious-state are the same nodes which are
active in the subliminal-state.
For each conscious-state net-
work we compute how many nodes (nk) are in the kmax
core, and we
check how many of these nodes are also in the activation map
of the subliminal-state, we refer to this number as nx. Then,
in each conscious-state network we randomly select nk nodes
and check how many of them also belong to the activation map
of the subliminal-state. We repeat this random sampling 105
times in order to have a distribution of randomly selected nodes
in the conscious network which are also in the subliminal acti-
vation map and perform a t-test with the overlap nx described
above. In Fig. 9 we show the results for those networks which
passed the t-test. In details, the left panels show nodes which
are both part of the kmax
core of the conscious-state and of the AM
of the subliminal-state (show in the right panels for compari-
son), consistently across networks. Quantitatively, nearly 1/3
of the nodes in the AM of the subliminal-state also belong to
the kmax
core of all the conscious functional networks that pass the
t-test (precisely, 112 nodes over 340). This suggest that the
subliminal-state, which remains active during period of non-
conscious perception, constitutes a large part of the kmax
core of the
conscious state.
Discussion
In this Section we elaborate on the interpretation of the results
by introducing a dynamical model describing the time evolution
of mutualistic complex systems (Morone et al. , 2019) which
directly addressed the stability of the network and its relation
Cluster
Region
1
Fusiform  
Gyrus (L)
2
Fusiform  
Gyrus (R)
3
Precentral 
Gyrus (L)
4
Superior 
Occipital (L)
5
Superior 
Occipital (R)
6
Premotor 
Cortex (R)
7
Supplementary
motor area 
(SMA)
occupancy
random
cluster
1
2
3
4
5
6
7
0.5
0.4
0.3
0.2
0.1
0.0
conscious  
networks
kmax
core
Figure 8: Cluster occupancy of nodes in the maximum k-core (which coin-
cide with the maximum k-shell). Green bars show the normalized cluster occu-
pancy of nodes which populate the maximum k-core. If the occupation of the
k-core were due to a random eﬀect then one would ﬁnd a distribution of about
30% in each cluster (blue bars). We observe that the left and right fusiform
gyrus and the left prefrontal gyrus populate the maximum k-core more than
what is expected at random (P < 10−5).
Subliminal state activation map
Left hemisphere
Right hemisphere
Average          of all conscious networks
kmax
core
Figure 9: Statistical analysis at the node level. Left panels: nodes which
are in the kmax
core of all conscious-state networks that pass the t-test (p < 10−5)
when compared with the subliminal-state. Right panel: activation map of the
subliminal-state shown for comparison. Roughly 1/3 of the nodes which belong
to the kmax
core of the conscious-state also belong to the subliminal-state activation
map. The subliminal state (right panel) largely overlaps with the maximum
k-core of the conscious network (left panel).
to the k-core. The model of Morone et al. (2019) applies to
the complex networks with only positive interaction. Since the
correlations between nodes of the conscious-state networks turn
out to be positive, the dynamics of these brain networks can be
modeled with diﬀerential equations accounting for mutualistic
interplay proposed in Ref. Morone et al. (2019). Recent re-
sults (Morone et al. , 2019) show that, for such mutualistic sys-
tems, the kmax
core of the network is the most resilient structure, i.e.
the last architecture which collapses due to the weakening of
the interactions strength. Findings discussed in Section Results
show that the kmax
core of the conscious-state largely overlap with
the subliminal-state activation map. Thus, in short, the ﬁndings
of Morone et al. (2019) help us interpreting the subliminal-
state as the most resilient part of the conscious-state when the
7


## Page 8


correlations (interactions) strength is weakened.
This leads us to theorize that the conscious →subliminal
transition in the brain happens through the weakening of the
interactions strength in the network. In other words, regions
which are highly correlated in the conscious-state suddenly be-
come less correlated and, therefore, not fMRI active thus pro-
ducing a subliminal state of activation. We see this eﬀect in the
data through the activation map shown in Fig. 2 which shows
that, indeed, the subliminal state is characterized by much less
fMRI activation (compare Fig. 2a with Fig. 2c). Furthermore,
ﬁndings discussed in Section Results demonstrate that the resid-
ual activation of the subliminal-state largely matches with the
kmax
core of the functional conscious-state network. These two ev-
idences are consistent with the results discussed in (Morone
et al. , 2019) which help us interpreting the transition conscious
→subliminal as taking place through the activity collapse of
certain conscious-state area, due to decrease covariation among
these areas, leaving residually active only areas in the kmax
core. We
conclude that these areas are therefore the most resilient ones,
as shown in Morone et al. (2019), and, in our case, those which
characterize the subliminal brain activity.
In the next section we brieﬂy review the relevant results of
Ref. Morone et al. (2019) to the above discussion in order to
elaborate an interpretation of our ﬁndings and a description of
the conscious →subliminal transition at the functional network
level.
Dynamical model and k-core percolation
Dynamics of a neural network can be described by a model of
coupled interacting neurons through sigmoidal responses (Som-
polinsky et al. , 1988; Amit, 1989). Here, by coarse graining
the neural activity, we use the same model to describe the dy-
namical evolution of the fMRI signal in each voxel, with the
following nonlinear diﬀerential equations (Sompolinsky et al. ,
1988; Amit, 1989)
˙xi(t) = I −xi
R + 1
2
N
X
j=1
AijJij
1 + tanh(n(x j −α))
(1)
Here, xi(t) is the fMRI activity of voxel i, N is the number of
voxels, I is the background BOLD activity, R is the inverse of
the inactivation rate, n is the slope of the sigmoid function, α
is a BOLD activity threshold at the fMRI voxel level, Ai j is the
adjacency matrix, i.e. Aij = 1 if voxel i and j are connected and
zero otherwise and Ji j is the interaction strength between pair
of voxels where we take Jij = Cij as the strength of correlations
from the data. Notice that the theory is only valid in absence
of inhibition, i.e when Jij > 0. Let us note that the matrix
shown in Fig. 3b includes both the information encoded in Ai j
(whether a link is present or not) and in Jij (the strength of such
link). In Eq. (1) we employ this slightly diﬀerent formalism for
consistency with Ref. Morone et al. (2019).
For a given set of initial conditions, the ﬁxed point solu-
tion of Eq. (1) is completely determined by the values of the
dynamical parameters. Of particular interest is the identiﬁca-
tion of the tipping point by tuning of these parameters, i.e.
the point at which all nodes are inactive (xi = 0 for each i).
In general, the analytical derivation of the ﬁxed point solu-
tion of Eq. (1) is too cumbersome. Morone et al. in (Mo-
rone et al. , 2019) have shown, yet, that under the assumptions
of constant couplings (Ji j = J for all i, j) and by replacing
1
2
1 + tanh(n(x j −α)) ≈Θ(x j −α), where Θ(x) is the Heav-
iside function, it is possible to obtain an approximate solution
of this tipping point.
We observe that, in the data of the present experiments (De-
haene et al. , 2001), analyzed and discussed in the previous
Sections, the interactions among voxels are mainly positive (see
Fig. 3b). This outcome could be explained by noting that the
fMRI signal is stimulus-driven (words shown on a screen) and,
therefore, the correlation coeﬃcient among the fMRI activity of
two voxels which follow the same stimulus is most likely pos-
itive. If we then assume that these interactions (correlations)
have all the same strength J, by following the approximation of
Morone et al. (2019) for the sigmoidal function (n →∞), we
can write the steady-state solution of x∗
i from Eq. (1) as:
x∗
i (t) = IR + JR
N
X
j=1
Ai jΘ(x∗
j −α)
(2)
and, with the following change of variable
y∗
i = x∗
i −IR
JR
,
(3)
Eq. (2) can be written in terms of the reduced density y∗, in the
following form:
y∗
i (t) =
N
X
j=1
Ai jΘ(y∗
j −KJ),
(4)
with
KJ = α
JR −I
J .
(5)
The parameter KJ in Eq. (4) controls the threshold of mutualis-
tic beneﬁt (Morone et al. , 2019) which, in the case of study, is a
threshold of mutualistic signal enhancement between voxels. In
practice, KJ is the threshold in the Θ-function of Eq. (4) which
allows voxel i to increase its activation thanks to the interac-
tion with voxel j only when the densities y∗
i are greater than
KJ. Let us observe that KJ is inversely proportional to the inter-
action strength J. By weakening the interactions the threshold
increases and, thus, the ﬁnal activity of voxel i decreases. In
other words, by keep decreasing the interactions, the activity
of some of the voxels y∗
j falls under the threshold and therefore
confers no activation to y∗
i (see Eq. (4)). Hence, from Eqs. (4)
and (5) it is clear that there exist a critical value Jc, and thus a
critical threshold KJ(Jc), at which the only solution of Eq. (4)
is y∗
i = 0 for all i.
In Ref. Morone et al. (2019) the authors show that this crit-
ical threshold is related to the maximum k-core of the network.
Indeed, the reduced density y∗
i assumes only integer values in
the set y∗
i ∈{1, . . . , ki}, where ki is the degree of voxel i. For
a given threshold KJ, voxels with degree kj < KJ do not con-
tribute to Eq. (4), so they can be removed from the network.
8


## Page 9


After this removal, some of the remaining voxels will have a
smaller degree k′
j (due to the fact that they have lost some of
their neighbors with the removal). Voxels with k′
j < KJ can then
be removed in turn, because they will not contribute to Eq. (4),
and so forth. This process is exactly the algorithm for extract-
ing the KJ-core from a network and voxels remaining at the end
of this procedure are the voxels belonging to the KJ-core (Mo-
rone et al. , 2019). By increasing the threshold KJ from low to
higher values, voxels from the low-to-higher k-cores will cease
to contribute to the dynamics of the network, until the critical
threshold KJ(Jc) = kmax
core is reached. Above this threshold, the
only ﬁxed point solution is the network collapse y∗
i = 0 for all i.
From this ﬁndings it results that, as also mentioned at the
beginning of the Discussion Section, the kmax
core structure is the
most resilient part of a network to the decreasing of the inter-
actions strength. Based on these ﬁndings, we interpret the con-
scious →subliminal transition as a passage from high to lower
correlations among brain areas which ends in a ﬁnal state, i.e.
the subliminal, that corresponds to the kmax
core of the conscious-
state network. It is worth mentioning that this dynamical model
could be applied to any experiment on consciousness that re-
sults in positive interactions between active nodes assuming
that the underlying dynamics is the one described by Eq. (1).
Our results in light of Libet and Dehaene’s consciousness
theories
Two prominent theories of the relation between unconscious
information and conscious access have been developed by Ben-
jamin Libet and Stanislas Dehaene. The former stressed how,
through the analysis of EEG data, all external stimuli is pro-
cessed in the brain unconsciously a couple of hundred of mil-
liseconds before any voluntary act. According to this theory,
unconscious information is the spark for the initiation of all
conscious actions, and there is a role for consciousness and
executive control to regulate actions of information processed
subliminally (Libet, 1985). On the other hand, Stanislas De-
haene, has shown the existence of a large-scale versatile brain
system that involves regions in the parietal and frontal cortex
that set a temporary workspace to bind and share information
(Dehaene & Naccache, 2001; Dehaene, 2014; Van Vugt et al. ,
2018). This framework which allows exchange of information
through ﬁrst bottom up, followed by top down propagation, is
referred to as ignition; if the incoming stimuli does not acti-
vate voxels strongly enough, then the information will not be
manifested consciously by the brain.
Our ﬁndings add a new view which is consistent with these
theories. Both share the notion that, while conscious activation
involves the non-linear and massive activation of a broad set of
brain areas in an ignition process, the onset of this mechanism is
in local-circuits, which encode information for this speciﬁc pro-
cess that might eventually become conscious. Our work shows
that despite the massive propagation of information the core of
activity, which is at the seed of the unconscious-state, remains
at the deepest core, i.e. at the shell structure of the functional
networks. This ﬁnding is quite reminiscent of the ’theory of
vision’ proposed by David Mumford and colleagues (Lee et al.
, 1998). This theory argues that V1 is a high frequency func-
tional core of the brain. It buﬀers and holds temporarily (as in a
blackboard, or as in a workspace) information for which its re-
ceptive ﬁelds are optimally suited. In other words, a core shell
of conscious activation, may not be a common set of neurons
but, instead, it may vary according to the functional require-
ments of the speciﬁc conscious percept at any given time.
Summary
In this work we investigated the conscious →subliminal tran-
sition in the brain through the network analysis of fMRI data
collected in Ref. Dehaene et al. (2001) where two experiments
on human subjects were performed, speciﬁcally designed to in-
duce either a conscious or a non-conscious (subliminal) percep-
tion of a word ﬂashed on a screen.
From the data we ﬁrst observed that fMRI activation of
the subliminal-state is largely a subset of the activation of the
conscious-state. Furthermore, we note that links in the func-
tional brain network of the conscious-state, built from the fMRI
signal, are mostly positive.
These two observations from the data analysis, together with
the recent ﬁndings of Ref. Morone et al. (2019), led us to per-
form a k-core study of the conscious-state network structure.
The authors of Morone et al. (2019) recognized indeed that,
under certain approximations, neural dynamical systems with
positive interactions show a decrease of their activation to the
weakening of their interactions strength. The most resilient part
of the network to this kind of weakening, i.e. the last struc-
ture to remain active, is the kmax
core of the system. So, driven by
the above observations we investigated whether the subliminal-
state was related to the kmax
core of the conscious-state.
We found that, at the cluster level, the subliminal-state is
made of fMRI active clusters which are those that most popu-
late the kmax
core of the conscious-state network, across subjects and
experiments. At the node level, we found that roughly 1/3 of
the active voxels of the subliminal-state exactly overlap (node
by node) with the nodes in the kmax
core of the conscious-state net-
work, across fMRI streams. To verify that these results were not
due to chance, we also compared them with outcomes obtained
from suitable randomly generated models.
Overall, these ﬁndings are in agreement with the prediction
of Ref. (Morone et al. , 2019) and led us to conclude that the
conscious →subliminal transition may be interpreted as caused
by a decrease of the correlated fMRI activity among voxels,
due to the fMRI inhibition of certain brain areas. The areas
which survive this inhibition, i.e. those which constitute the
subliminal-state, are also those that, statistically, belong to the
most resilient structure of the conscious-state network: the kmax
core.
This not only sheds light on the nature of the conscious →sub-
liminal transition but, furthermore, motivates us to interpret the
subliminal-state activity as the most robust to the weakening of
the fMRI signal. Indeed, this state is the one which persists
as background fMRI activity when non-conscious perception is
present and the state from which conscious perception arises.
The conscious →subliminal transition is a profound and in-
9


## Page 10


triguing problem in neuroscience and this work certainly does
not answer all the questions that it rises. On the other hand,
from a system neuroscience perspective, we think our results
highlight the importance of studying network structures that
could unveil useful patterns or markers able to shed light on
similarity and diﬀerences between conscious and subliminal
awareness and on the transition from one to the other.
Acknowledgements. We thank Flaviano Morone and Lu-
cas Parra for useful discussions and insights and Luca Pasquini
for help with brain anatomy. We thank Stanislas Dehaene for
graciously sharing his data from Ref. Dehaene et al. (2001)
and allowing us to analyze this dataset. This work is supported
by NIH-NIGMS R01EB022720, NIH-NCI U54CA137788 /
U54CA132378 and NSF-IIS 1515022.
References
Alvarez-Hamelin, J I, Dall’Asta, L, Barrat, A, & Vespignani, A. 2008. K-core
decomposition of Internet graphs: hierarchies, self-similarity and measure-
ment biases. Netw. Heterog. Media, 3, 371–393.
Amit, D J. 1989. Modeling brain function: The World of Attractor Neural
Networks. Cambridge University Press.
Anzellotti, S, & Coutanche, M N. 2018. Beyond functional connectivity: In-
vestigating networks of multivariate representations. Trends Cogn. Sci., 22,
258–269.
Bardella, Giampiero, Bifone, Angelo, Gabrielli, Andrea, Gozzi, Alessandro, &
Squartini, Tiziano. 2016. Hierarchical organization of functional connectiv-
ity in the mouse brain: a complex network approach. Sci. Rep., 6, 32060.
Borgatti, S P, & Everett, M G. 2000. Models of core/periphery structures. Soc.
Netw., 21, 375–395.
Bullmore, E, & Sporns, O. 2009. Complex brain networks: graph theoretical
analysis of structural and functional systems. Nat. Rev. Neurosci., 10, 186.
Bullmore, E, & Sporns, O. 2012. The economy of brain network organization.
Nat. Rev. Neurosci., 13, 336.
Burlesson-Lesser, K, Morone, F, & Makse, H A. 2019. K-core robustness in
ecological and ﬁnancial networks. submitted.
Carmi, S, Havlin, S, Kirkpatrick, S, Shavitt, Y, & Shir, E. 2007. A model of
Internet topology using k-shell decomposition. Proc. Natl. Acad. Sci., 104,
11150–11154.
Corradino, C. 1990. Proximity structure in a captive colony of Japanese mon-
keys (Macaca fuscata fuscata): An application of multidimensional scaling.
Primates, 31, 351–362.
Craddock, R C, Jbabdi, S, Yan, CG, Vogelstein, J T, Castellanos, F X, Di Mar-
tino, Ad, Kelly, C, Heberlein, K, Colcombe, S, & Milham, M P. 2013. Imag-
ing human connectomes at the macroscale. Nat. Methods, 10, 524.
Deco, G, McIntosh, A R, Shen, K, Hutchison, R M, Menon, R S, Everling, S,
Hagmann, P, & Jirsa, V K. 2014. Identiﬁcation of optimal structural con-
nectivity using functional connectivity and neural modeling. J. Neurosci.,
34, 7910–7916.
Dehaene, S. 2014. Consciousness and the brain: Deciphering how the brain
codes our thoughts. Penguin.
Dehaene, S, & Naccache, L. 2001. Towards a cognitive neuroscience of con-
sciousness: basic evidence and a workspace framework. Cognition, 79, 1–
37.
Dehaene, S, Naccache, L, Cohen, L, Le Bihan, D, Mangin, JF, Poline, JB, &
Rivi`ere, D. 2001. Cerebral mechanisms of word masking and unconscious
repetition priming. Nat. Neurosci., 4, 752.
Del Ferraro, G, Moreno, A, Min, B, Morone, F, P´erez-Ram´ırez, ´U, P´erez-
Cervera, L, Parra, L C, Holodny, A, Canals, S, & Makse, H A. 2018. Finding
inﬂuential nodes for integration in brain networks using optimal percolation
theory. Nat. Comm., 9, 2274.
Dorogovtsev, S N, Goltsev, A V, & Mendes, J F F. 2006. K-core organization
of complex networks. Phys. Rev. Lett., 96, 040601.
Gallos, L K, Makse, H A, & Sigman, M. 2012. A small world of weak ties pro-
vides optimal global integration of self-similar modules in functional brain
networks. Proc. Natl. Acad. Sci., 109, 2825–2830.
Greicius, M D, Krasnow, B, Reiss, A L, & Menon, V. 2003. Functional connec-
tivity in the resting brain: a network analysis of the default mode hypothesis.
Proc. Natl. Acad. Sci., 100, 253–258.
Hagmann, P, Cammoun, L, Gigandet, X, Meuli, R, Honey, C J, Wedeen, V J,
& Sporns, O. 2008. Mapping the structural core of human cerebral cortex.
PLoS Biol., 6, e159.
Hermundstad, A M, Bassett, D S, Brown, K S, Aminoﬀ, E M, Clewett, D,
Freeman, S, Frithsen, A, Johnson, A, Tipper, C M, Miller, M B, et al. .
2013. Structural foundations of resting-state and task-based functional con-
nectivity in the human brain. Proc. Natl. Acad. Sci., 110, 6169–6174.
Honey, CJ, Sporns, O, Cammoun, L, Gigandet, X, Thiran, JP, Meuli, R, &
Hagmann, P. 2009. Predicting human resting-state functional connectivity
from structural connectivity. Proc. Natl. Acad. Sci., 106, 2035–2040.
Kitsak, M, Gallos, L K, Havlin, S, Liljeros, F, Muchnik, L, Stanley, H E, &
Makse, H A. 2010. Identiﬁcation of inﬂuential spreaders in complex net-
works. Nat. Phys., 6, 888.
Krugman, P R. 1996. The self-organizing economy. Blackwell Oxford.
Lahav, N, Ksherim, B, Ben-Simon, Etand Maron-Katz, A, Cohen, R, & Havlin,
S. 2016. K-shell decomposition reveals hierarchical cortical organization of
the human brain. New J. Phys., 18, 083013.
Lee, Tai Sing, Mumford, David, Romero, Richard, & Lamme, Victor AF. 1998.
The role of the primary visual cortex in higher level vision. Vision Res., 38,
2429–2454.
Libet, B. 1985. Unconscious cerebral initiative and the role of conscious will
in voluntary action. Behav. Brain Sci., 8, 529–539.
Morone, F, Del Ferraro, G, & Makse, H A. 2019. The k-core as a predictor of
structural collapse in mutualistic ecosystems. Nat. Phys., 15, 95–102.
Pittel, B, Spencer, J, & Wormald, N. 1996. Sudden Emergence of a Giantk-Core
in a Random Graph. J. Comb. Theory, Series B, 67, 111–151.
Rubinov, M, & Sporns, O. 2010. Complex network measures of brain connec-
tivity: uses and interpretations. Neuroimage, 52, 1059–1069.
Seidman, S B. 1983. Network structure and minimum degree. Soc. Netw., 5,
269–287.
Smith, S M, Jenkinson, M, Woolrich, M W, Beckmann, C F, Behrens, T EJ,
Johansen-Berg, H, Bannister, P R, De Luca, M, Drobnjak, I, Flitney, D E,
et al. . 2004. Advances in functional and structural MR image analysis and
implementation as FSL. Neuroimage, 23, S208–S219.
Sompolinsky, H, Crisanti, A., & Sommers, H J. 1988. Chaos in Random Neural
Networks. Phys. Rev. Lett., 61, 259–262.
Sporns, O. 2013. Structure and function of complex brain networks. Dialogues
Clin. Neurosci., 15, 247.
Sporns, O, Tononi, G, & K¨otter, R. 2005. The human connectome: a structural
description of the human brain. PLoS Comput. Biol., 1, e42.
Tononi, G, Boly, M, Massimini, M, & Koch, C. 2016. Integrated information
theory: from consciousness to its physical substrate. Nat. Rev. Neurosci.,
17, 450.
UCL. 1999. http://www.fil.ion.ucl.ac.uk/spm.
Van Den Heuvel, M P, & Pol, H E H. 2010. Exploring the brain network: a re-
view on resting-state fMRI functional connectivity. Eur. Neuropsychophar-
macol., 20, 519–534.
Van Vugt, B, Dagnino, B, Vartak, D, Safaai, H, Panzeri, S, Dehaene, S, &
Roelfsema, P R. 2018. The threshold for conscious report: Signal loss and
response bias in visual and frontal cortex. Science, 360, 537–542.
Verma, T, Russmann, F, Ara´ujo, NAM, Nagler, J, & Herrmann, H J. 2016.
Emergence of core–peripheries in networks. Nat. Comm., 7, 10441.
Watts, D J, & Strogatz, S H. 1998. Collective dynamics of small-world net-
works. Nature, 393, 440–442.
Yan, G, V´ertes, P E, Towlson, E K, Chew, Y L, Walker, D S, Schafer, W R,
& Barab´asi, A. 2017. Network control principles predict neuron function in
the Caenorhabditis elegans connectome. Nature, 550, 519.
Zhang, X, Martin, T, & Newman, M E J. 2015. Identiﬁcation of core-periphery
structure in networks. Phys. Rev. E, 91, 032803.
10

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]