---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1607.02197v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1607.02197v2_A_Complex_Network_Approach_for_Nanoparticle_Agglomeration_Analysis_in_Nanoscale_

> Source: 1607.02197v2_A_Complex_Network_Approach_for_Nanoparticle_Agglomeration_Analysis_in_Nanoscale_.pdf

> Pages: 10

---


## Page 1


Noname manuscript No.
(will be inserted by the editor)
A Complex Network Approach for Nanoparticle Agglomeration
Analysis in Nanoscale Images
Bruno Brandoli Machado · Leonardo Felipe Scabini · Jonatan Patrick
Margarido Oruˆe · Mauro Santos de Arruda · Diogo Nunes Gon¸calves ·
Wesley Nunes Gon¸calves · Raphaell Moreira · Jose F Rodrigues-Jr
Received: date / Accepted: date
Abstract Complex networks have been widely used in
science and technology because of their ability to rep-
resent several systems. One of these systems is found in
Biochemistry, in which the synthesis of new nanoparti-
cles is a hot topic. However, the interpretation of exper-
imental results in the search of new nanoparticles poses
several challenges. This is due to the characteristics of
nanoparticles images and due to their multiple intricate
properties; one property of recurrent interest is the ag-
glomeration of particles. Addressing this issue, this pa-
per introduces an approach that uses complex networks
to detect and describe nanoparticle agglomerates so to
foster easier and more insightful analyses. In this ap-
proach, each detected particle in an image corresponds
to a vertice and the distances between the particles de-
ﬁne a criterion for creating edges. Edges are created if
the distance is smaller than a radius of interest. Once
this network is set, we calculate several discrete mea-
sures able to reveal the most outstanding agglomerates
in a nanoparticle image. Experimental results using im-
ages of Scanning Tunneling Microscopy (STM) of gold
nanoparticles demonstrated the eﬀectiveness of the pro-
• Bruno Brandoli Machado, Leonardo F Scabini, Jonatan P
M Orue, Mauro S Arruda, Diogo N Goncalves and, Wesley N
Goncalves
CS Dept, Federal University of Mato Grosso do Sul
79907-414, Ponta Pora, MS, Brazil
E-mail: {bruno.brandoli,leo.scabini,jonatan.orue,m.arruda,
diogo.goncalves,wesley.goncalves}@ufms.br
• Raphaell Moreira
Freie Universitat BerlinTakustr
3, 14195, Berlin, Germany
moreira.raphaell@fu-berlin.de
• Jose F Rodrigues-Jr
CS Dept, University of Sao Paulo
13566-590, Sao Carlos, SP, Brazil
junio@usp.br
posed approach over several samples, as reﬂected by the
separability between particles in three usual settings.
The results also demonstrated eﬃcacy for both convex
and non-convex agglomerates.
Keywords nanoparticle cluster · agglomeration
analysis · complex networks
1 Introduction
Synthetic nanoparticles have been widely investigated
because of their applicability, including drug delivery in
medicine [33], cancer treatment and diagnostic tools [3],
and industrial products, such as cosmetics [24], semi-
conductor and photovoltaics [12], to name a few. They
are designed to have special physical and chemical prop-
erties that reﬂect in their structural characteristics and
interaction [26]. However, the development and use of
new nanoparticles are still constrained by the lack of
specialized tools to interpret experimental results, so
to characterize such particles [10]. A particular line of
investigation is the safety to human beings. This is be-
cause they are more chemically reactive and bioactive,
penetrating organs and cells easily. Actually, toxicologi-
cal studies [22] have shown that some nanoparticles are
harmful to humans.
To better understand the impact of real and syn-
thetic nanoparticles, material scientists use analytical
devices whose output are grayscale images of nanopar-
ticles. After the synthesis process and imaging of the
nanoparticles, an important task is to extract measure-
ments from such images. Hasselhov and Kaegi [18] de-
scribed key visual characteristics that need to be as-
sessed, including concentration, particle size distribu-
tion, particle shape, and agglomeration. Despite the im-
portance of nanoparticle assessment, there is a limited
arXiv:1607.02197v2  [physics.comp-ph]  13 Dec 2016


## Page 2


2
Bruno Brandoli et. al.
number of works on the characterization of nanoparti-
cles by means of image analysis.
Fisker et al. [15] developed an automatic method
to estimate the particle size distribution based on a
deformable ellipse model applied to ferromagnetic (a-
Fe1−x-Cx) and hematite (α-Fe2O3) nanoparticles. In
the work of Park et al. [30], the authors propose a semi-
automatic method to perform shape analysis over the
particles. In the work of Park et al. [30], the authors
used six images of Transmission Electron Microscopy
(TEM) to characterize the shape of gold nanoparti-
cles by representing boundary corners into a parametric
curve. Although the authors created a rotation invari-
ant approach, the reconstruction depends on the cor-
ners that the algorithm detects. This idea is sensitive
to the edges detected by Cany’s algorithm [7]. Further-
more, since the border detection fails for a number of
cases, they reconstruct the particles with incomplete
boundaries using functional-PCA (FPCA) [25] and the
gravity center of each shape. Since the dimensionality is
very high, the authors used the curve representation to
reduce the number of features with a multidimensional
projection method, named Isomap [35]. Finally, they
classiﬁed the shapes using graph-based clustering and a
k-nearest neighbors method over incomplete boundary
information. Although this approach presented good
accuracy for nanoparticle shape recognition, they did
not focus on analyzing the groups and interaction of
particles. Vural and Oktay [38] proposed a method to
segment Fe3O4 nanoparticles in TEM images by us-
ing Hough transform [11]. Similarly, a number of other
works [28] used a multi-level image segmentation for
measuring the size distribution of nanoparticles in TEM
images. However, these works disregarded the agglom-
eration of particles.
We can ﬁnd a rich literature with similar nanopar-
ticle problems in biomedical imaging, such as detection
and counting of cells [23], morphological cell classiﬁca-
tion [8], and cell tracking [40]. Unlike conventional cell
image analysis, agglomeration and interaction analysis
of nanoparticles are still a visual counting task. Such
task not only demands an extensive work, but it is
time-consuming. Therefore, modeling the relationship
of nanoparticles in images has emerged as an interesting
line of research to characterize their interaction and ag-
glomeration. In this scenario, complex networks deﬁne
a promising model to draw the relationships observed
in nanoparticle images, fostering the comprehension of
complex phenomena, most notably interaction, and ag-
glomeration.
Related Works on Complex Networks
Complex networks (CN) have emerged as a highly-active
research ﬁeld in the ﬁrst decade of the XXI century.
It came as an intersection between graph theory and
probability, resulting in a truly multidisciplinary ﬁeld,
building on top of mathematics, computer science, and
physics, leading to a large range of applications. Com-
plex networks are natural structures that represent many
real-world systems; its popularity comes from the fact
that it is able to model a large range of phenomena.
As an illustration, we can cite three developments that
have contributed to the research on complex networks:
(i) investigation of the random network model [13]; (ii)
investigation of small-world networks [39]; and (iii) in-
vestigation of scale-free networks [4]. Recently, works
have focused on the statistical analysis of such networks
in order to characterize them.
Complex networks have become an important topic
in science due to their ability to model a large number
of complex systems such as interaction in society [14],
processes in biology as protein interaction [1], ﬁnancial
markets [19], computer vision [17], and physics [16]. In
computer science, complex networks have been used to
understand the topology and dynamics of the Internet
[36], characterization of social networks [20], text sum-
marization [2], aspects of scientiﬁc co-authorship [29],
and citation networks [32].
Overview of Our Proposal
Beneﬁting from the potential of complex networks, we
propose a new approach to analyzing nanoparticle ag-
glomeration. As far as we know, this work is the ﬁrst
to report the use of complex networks on nanoparti-
cle images. In the proposed approach, similarly to the
work of Fisker et al. [15], each particle of a nanoscale
image is initially detected using 2D-template match-
ing, described in more details in by Brunelli [6]. Then,
each particle is mapped to a vertex of the complex net-
work. Systematically, a network is built by connecting
each pair of nodes by using a threshold for density es-
timation over a certain radius. For each nanoparticle,
we calculate its density, according to which two par-
ticles are linked only if the distance between them is
lesser than a radius and its density is higher than a
given threshold. Then, we represent our complex net-
work topology by calculating the spatial average degree,
and the max degree for networks, transformed by dif-
ferent values of radius and thresholds. We tested our
approach on real-image particles taken with Scanning
Tunneling Microscopy (STM), a technique that creates
high-resolution images of nanoparticle settings.


## Page 3


A Complex Network Approach for Nanoparticle Agglomeration Analysis in Nanoscale Images
3
This paper is organized as follows. Section 2 presents
a brief review of the complex network theory. In Section
3, the proposed approach for nanoparticle characteriza-
tion is described in detail. The experiments conducted
and the discussions of the results are presented in Sec-
tion 4. Finally, conclusions are given in Section 5.
2 Complex Networks
2.1 Overview
In general, works using complex networks have two steps:
(i) model the problem as a network; and (ii) extract
topological measures to characterize its structure. As
complex networks are represented by graphs, every dis-
crete structure such as lists, trees, networks, and images
can be suitably modeled. In this context, the main step
is to deﬁne the best approach to represent the given
problem as a set of vertices and connections, so that its
complex behavior can be measured as a CN.
2.2 Complex Networks Representation and Measures
Complex networks are represented by graphs. An undi-
rected weighted graph G = {V, E} is deﬁned wherein
V = {v1, ..., vn} is a set of n vertices and E = {evi,vj}
is a set of edges connecting two vertices; evi,vj repre-
sents the weight of the connection between the vertices
vi and vj. There are many measures that can be ex-
tracted from a CN to characterize it. The reader may
refer to the work of Costa et al. [9] for a review of diﬀer-
ent classes of measures. We focused in two simple and
important characteristics extracted from each vertex,
the degree and the strength. The degree of a vertex vi
is the number of its connections:
k(vi) =
X
evi,vj ∈E
1
(1)
The vertex strength is the sum of the weights of its
connections:
s(vi) =
X
evi,vj ∈E
evi,vj
(2)
The vertex degree and strength describe the inter-
action with neighboring vertices and can be used to an-
alyze the network structure. Globally, it is possible to
characterize the behavior of the vertices of the network
using the mean degree:
µk =
1
|V |
X
vi∈V
k(vi)
(3)
and the mean strength:
µs =
1
|V |
X
vi∈V
s(vi)
(4)
In this work, we analyze the degree and the strength
of the vertices to detect regions with strong connec-
tions, which are evidence of vertices agglomerates. In
the context of our application, these regions present
nanoparticle agglomeration, which is the focus of the
work.
3 Proposed Approach for Detection and
Agglomeration Analysis
In this section, we describe our approach for detection
and characterization of nanoparticle agglomerates. For
this purpose, we use template matching to detect the
positions of nanoparticles in nanoscale images. Subse-
quently, we build a CN with their relative positions.
Finally, the degree and strength of the resulting net-
work are used as features to support analysis.
3.1 Detection of the particles’ coordinates
In order to detect the coordinates of the nanoparti-
cles, we use the template matching technique [6]. This
technique uses a convolution mask tailored to a fea-
ture of interest; this mask corresponds to the template,
which must carry visual characteristics similar to those
of what we want to detect. The output of the convo-
lution will be high in the regions of the image whose
structure matches the template; the idea is to multiply
the image values by large template values – when there
is a match the product gets very high magnitudes com-
pared to the other parts of the image. The template is
constructed by picking a part of a sample image that
contains the pattern of interest – in our case, we picked
a well-deﬁned nanoparticle T(xt, yt), where (xt, yt) rep-
resents the pixels in the template. We refer to a given
search image as S(x, y). The convolution, then, is per-
formed by moving the center of the template T(xt, yt)
over each pixel S(x, y) of the image, calculating the
sum of products between the coeﬃcients of S and T
over the whole area spanned by the template. After the
convolution, the positions with the highest scores will
correspond to the patterns of interest – in our case, the
set of nanoparticles.


## Page 4


4
Bruno Brandoli et. al.
3.2 Modeling Complex Networks for Nanoparticle
Agglomeration Analysis
The CN is built after the spatial positions of the nanopar-
ticles in the image. The network is built considering
each nanoparticle as a vertex. To build the set E, the
weight of the connections is deﬁned according to the
Euclidean distance – shortly referred to as a function
dist : V × V →R. In order to connect only close ver-
tices, a radius r ∈[0, 1] is considered. First, the edges’
weights, evi,vj, are normalized into the interval [0, 1] di-
viding its Euclidean distance distvi,vj by the distance
between the two more distant vertices, as follows:
evi,vj =
p
(xi −xj)2 + (yi −yj)2
max(distvi,vj)
(5)
where xi and yi are the spatial coordinates of the nanopar-
ticles and max(distvi,vj) is the distance between the
two most distant nanoparticles.
Then, the connection between each pair of vertices is
maintained if its normalized Euclidean distance evi,vj is
less or equal to r. Moreover, we complement the normal-
ized weight evi,vj with respect to the threshold radius
r, as follows:
evi,vj =
r −evi,vj,
if evi,vj ≤r
0,
otherwise
(6)
It is important to notice that r −evi,vj inverts the
edge weight, which was originally the Euclidean dis-
tance. After this operation, the closer any two vertices
are, the higher is their weight. This is performed con-
sidering the vertex strength, that is, stronger vertices
represent higher interplays among neighbors.
The resulting CN contains connections between ver-
tices inside a given radius, according to the Euclidean
distances. However, this representation does not con-
sider the agglomeration level of the vertices, which is
the main purpose of the problem, i.e., the use of a ra-
dius to connect close vertices is not suﬃcient to prop-
erly represent agglomerates. To ﬁnally model the net-
work in a proper way, revealing the level of nanoparticle
agglomeration, we propose another transformation on
its topology. A new function is applied to calculate the
density of the vertices, which represents their relation
to their neighbors in terms of distance. This measure
can be calculated using the CN information obtained
so far. It becomes necessary to extract the degree k(vi)
and the strength s(vi) of the vertices (Equations 1 and
2), both measures depending on the neighborhood of
each vertice. The neighborhood is deﬁned by the radius
r, so each vertex inside the distance deﬁned by the ra-
dius value is analyzed. Given a resulting CN Gr built
with a radius r, and the respective degree and strength
of each vertex vi, its density is deﬁned by:
d(vi) = s(vi)
k(vi)
(7)
After calculating the density of each vertice, we nor-
malize the densities so to have a domain of values inside
the range [0, 1].
Since the degree is the number of connections and
the strength is the sum of its weights, the density d(vi)
refers to the average weight of a vertice’s neighbor-
hood. Following the complement operation deﬁned in
Equation 6, then, vertices with a larger number of close
neighbors tend to have greater densities.
With the density, it is possible to perform another
transformation to highlight the agglomerates of the net-
work. We proceed by considering only the connections
between vertices with density higher than a threshold
t, discarding the other ones. In this context, a new CN
Gr,t is obtained by analyzing each edge evi,vj, as fol-
lows:
evi,vj =
evi,vj,
if d(vi) and d(vj) ≥t
0,
otherwise
(8)
This ﬁnal transformation results in a CN that bet-
ter represents the agglomeration of the vertices, instead
of the limited distance analysis of the ﬁrst transfor-
mation. It means that the use of the density to deﬁne
connections allows selecting edges in regions of inter-
est, i.e., with high density. In the context of the current
application, the network now presents connections be-
tween nanoparticles that pertain to agglomerates; these
connections come according to the radius r and to the
density threshold t. In Figure 1, the positions in a real
image of nanoparticles is analyzed and a CN is mod-
eled using radius r = 0.04 and threshold t = 0.5. The
color indicates the density ranging from black/red (low
density) to white/yellow (high density).
3.3 Dynamic Analysis of Complex Networks
To analyze a nanoparticle image, it is necessary to con-
sider its corresponding CN in view of the range of pa-
rameters that inﬂuence the formation of agglomerates.
As mentioned earlier, we consider two parameters, the
radius r and the threshold t, which aﬀect the network
topology (set of edges) resulting in networks with dense
or sparse connections – illustrated in Figure 2. This
variable conﬁguration is useful to analyze the network


## Page 5


A Complex Network Approach for Nanoparticle Agglomeration Analysis in Nanoscale Images
5
(a) Input image.
(b) Complex Network built using the nanoparticle posi-
tions (absolute coordinates).
Fig. 1: Nanoparticle image modeled as a Complex Network according to the proposed approach. (a) Input image.
(b) Density of each nanoparticle (color-mapped) and connections of the resulting Complex Network.
considering diﬀerent analytical demands – it is possible,
for instance, to consider bigger or smaller agglomerates,
denser or sparser, separated or closer, depending on the
material and on the problem at hand. In fact, a network
characterization cannot be fully complete without con-
sidering the interplay between structural and dynamic
aspects [5].
Therefore, to perform a thorough analysis, one must
take into account a set of radii R = {r1, ..., rnr} and a
set of thresholds T = {t1, ..., tnt} able to characterize
the network in the amplitude of parameters r and t.
To do so, we build multiple topologies, each one given
by a combination of r and t. The problem, then, be-
comes how to put these multiple topologies together in
a coherent mathematical representation. We do it my
means of a feature vector whose dimensions are given by
measures extracted from each r −t Complex Network.
Feature Vector
Given two sets, R = {r1, ..., rnr} and T = {t1, ..., tnt},
we build |R| × |T| CNs, each one denoted Gr,t. From
each CN we calculate four measures: mean degree (Equa-
tion 3), max degree kmax = {k(vi)|k(vi) > k(vj), i ̸=
j, ∀vi ∈V, vj ∈V }, mean strength (Equation 4), and
max strength smax = {s(vi)|s(vi) > s(vj), i ̸= j, ∀vi ∈
V, vj ∈V }. Finally, the feature vector, denoted ϕ, is
formed by the concatenation of the sequence of four
measures of each CN Gr,t, as follows:
ϕ = [µr1,t1
k
, kr1,t1
max , ..., µkrnr,tnt, krnr,tnt
max
]
(9)
The number of features depends on the number of
radii, thresholds, and extracted measures; its cardinal-
ity is given by |ϕ| = nr∗nt∗m, where nr is the number
of radii, nt is the number of threshold values, and m
is the number of measures. For a consistent domain
of values considering any given vectors, the features
are numerically homogenized according to the standard
score [21] technique; that is, from each feature we sub-
tract the mean score and divide the result by the stan-
dard deviation of all features.
4 Results and Discussion
In this section, we evaluate the proposed approach. We
show results in real nanoparticle images by diﬀerenti-
ating three diﬀerent cases of agglomeration.
4.1 Image Dataset
We built a dataset of nanoparticle images with 10 sam-
ples labeled into 3 agglomeration cases: Case 1 – the
images have few groups and the nanoparticles are uni-
formly spread; Case 2 – the number of groups is larger
if compared to Case 1, with little nanoparticle agglom-
eration; Case 3 – the images have a strong level of ag-
glomeration and overlapping. Each kind of image can be
observed in Figure 3. Notice that nanoparticle agglom-
eration might happen in the 3D scenario, with a strong
incidence of overlapping; since our method works over
2D images, such cases are to be tackled with alternative
techniques (e.g., 3D reconstruction [37]), alternatively,
the samples shall be prepared according to a laboratory
protocol that reduces overlapping. For our experiments,
we have used STM images of gold nanoparticles; stan-
dard reference materials NIST 8011, 8012, and 8013
– NIST®, Gaithersburg, MD, U.S. The gold particles
were suspended in a solution of deionized (DI) water
at a concentration of 250,000 particles/mL. In order to


## Page 6


6
Bruno Brandoli et. al.
(a) r = 0.03, t = 0.2.
(b) r = 0.03, t = 0.5.
(c) r = 0.05, t = 0.2.
(d) r = 0.05, t = 0.5.
Fig. 2: Complex Network topology changes by varying the parameters r and t. Blue arrows correspond to the most
relevant areas aﬀected by changing the parameter values. Basically, if r and t are increased, new edges are created
or removed, depending on the intrinsic agglomeration.
(a) Case 1.
(b) Case 2.
(c) Case 3.
Fig. 3: Images for the three levels of nanoparticle agglomeration used in the experiments.
avoid dissolution of the gold nanoparticles, acid was not
added.
4.2 Assessing Parameters
A problem that raises in our methodology refers to the
choice of the best parameters r and t. These two pa-
rameters render a set of possibilities large enough to
impede the user ﬁnd the best conﬁguration. We treat
this issue by measuring the quality of the agglomera-
tions detected by each pair (r, t); to do so, we use the
well-known measure named silhouette coeﬃcient [34],
which was originally proposed to evaluate clustering al-
gorithms.
In our setting, the silhouette coeﬃcient shall mea-
sure the cohesion and the separation between the ag-
glomerates detected in a given Gr,t conﬁguration. Con-
sidering a nanoparticle vi belonging to an agglomerate,
its cohesion avi is given by the average of the distances


## Page 7


A Complex Network Approach for Nanoparticle Agglomeration Analysis in Nanoscale Images
7
between vi and all the other nanoparticles belonging
to the same agglomerate. In turn, the separation bvi is
given by the smallest distance between vi and all the
other nanoparticles belonging to the other agglomer-
ates. Once we calculate the cohesion and the separation
of a given partice vi, its silhouette value is given by:
silhouette(vi) =
bvi −avi
max(avi, bvi)
(10)
Given a set with n instances and a corresponding
clustering, the silhouette of the whole set is given by the
average of the silhouette (Equation 10) of all of its in-
stances. The average silhouette, Equation 11, provides
a number that characterizes how good is the clustering
(set of agglomerates).
S =
1
|V |
X
vi∈V
silhouette(vi)
(11)
The silhouette can range between −1 ≤S ≤1,
where larger values indicate better cohesion and sepa-
ration between agglomerates, that is, better agglomera-
tion. Negative values indicate instances (nanoparticles)
assigned to the wrong agglomerate; this is because the
distances indicate that particles from other agglomer-
ates are closer than the particles of the agglomerate to
which they were assigned.
4.3 Deﬁnition of the best values for r and t
We deﬁned the best interval of values by analyzing
the average silhouette (Equation 11) from CNs built
with diﬀerent values for parameters r ant t. The ra-
dius was analyzed by varying its value in the range
[r1 = 0, rnr = 0.06], while t was analyzed in the range
[t1 = 0.1, tnt = 0.9]. For each combination of values,
we calculated the silhouette value for each image. We
summarize the multiple silhouette values using mean;
hence, the y-axes of our images are labeled mean silhou-
ette. With this conﬁguration, we note that the domain
given by parameters r and t renders a 3D plot, that is,
a surface of silhouette values. We do not plot the sur-
face, since static 3D images are of little use; instead, we
present the best section of the surface in Figure 4. This
section includes the highest silhouette values of the r-t
domain.
The results allow to detect and discard values from
the radius interval that do not produce good detection
of agglomerates. We can observe that radius values in
the range 0 < r < 0.015 are not suﬃcient to con-
nect nanoparticles/vertices in the CN. In this settings,
0
0.015
0.035
0.048
0.06
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
radius (r)
mean silhouette
Fig. 4: Silhouette value in function of the radius r.
it was not possible to identify proper sets of agglom-
erates; therefore, it was not possible to calculate the
silhouette, which explains the silhouette 0. We also dis-
card values in the range [0.015, 0.035] due to the in-
constant results that are observed; although there is
a peak at radius 0.0215. By analyzing other values, it
is possible to notice that the best results are achieved
in the range [0.035, 0.048], a stable interval of silhou-
ette values. Following, there is a decrease of perfor-
mance probably caused by CNs with dense connections
that are not useful to discriminate the agglomerates.
Based on these results, we opt for the radius inter-
val [r1 = 0.03, rnr = 0.05]; accordingly, the radius set
R = {r1, ..., rnr} will be composed by nr equidistant
values ranging from 0.03 to 0.05. Notice that the curve
could be smoother had we used more images; this is
because with a larger number of values (one per im-
age), the expected average value would dominate the
plot, avoiding spikes. However, that would demand a
very large number of images, which were not available
and which is not usual in the corresponding literature
[15, 30, 31, 27].
We deﬁned the threshold best interval of values by
analyzing the average silhouette in the range [t1 =
0.1, tnt = 0.9] using nt equidistant values.
4.4 Evaluation of Complex Network Measures
To characterize the CN structure, 4 measures were eval-
uated: mean degree, max degree, mean strength, and
max strength – refer to Section 3.3. We consider each
possible combination among these measures to ﬁnd the


## Page 8


8
Bruno Brandoli et. al.
one that best reﬂects the silhouette of the agglomerates
identiﬁed using the best values of r and t, as explained
in Section 4.3. Each result can be observed in Table
1 along with the standard deviation of the silhouette
value.
Table 1: Mean silhouette in perspective of complex net-
work measures mean degree (µk), max degree (µs),
mean strength (µs), and max strength (smax). We used
parameter values as pointed out by the results of Sec-
tion 4.3.
µk
kmax
µs
smax
no. of features
silhouette
X
18
0.88 (±0.11)
X
18
0.15 (±0.13)
X
18
0.89 (±0.07)
X
18
0.24 (±0.35)
X
X
36
0.39 (±0.07)
X
X
36
0.91 (±0.07)
X
X
36
0.91 (±0.08)
X
X
36
0.27 (±0.11)
X
X
36
0.27 (±0.10)
X
X
36
0.33 (±0.18)
X
X
X
54
0.41 (±0.07)
X
X
X
54
0.40 (±0.07)
X
X
X
54
0.92 (±0.07)
X
X
X
54
0.28 (±0.12)
X
X
X
X
72
0.41 (±0.08)
According to these results, one notices that the max
degree and max strength do not provide good discrimi-
nation if used individually. However, the max strength
proved to be useful if combined with the mean strength
and mean degree, producing the best result (0.92) us-
ing 54 features. The means, individually and combined,
provided results close to the best (0.88, 0.89 and 0.91
combined), but on the other hand, they use fewer fea-
tures (18 individually and 36 combined). The combi-
nation of all the features proved to be not applica-
ble for agglomeration analysis. Finally, it is possible to
conclude that measures mean strength (µs) and max
strength (smax), together, have the highest represen-
tativeness with respect to the intrinsic agglomerative
properties of complex networks derived from nanopar-
ticle images.
5 Conclusion
The analysis of nanoparticles agglomeration is a topic
of recurrent relevance for the interpretation of experi-
ments in the ﬁeld of nanomaterials. Hence, in this work,
we proposed a novel approach for nanoparticle agglom-
eration analysis based on complex networks. Our method
innovates in the sense that its parameters allow for anal-
yses modeled by the interests of the user, including the
material and the problem at hand; besides, it adheres
to a visual analysis. During our experiments, we showed
how to identify the best conﬁguration of parameters by
using the metric of silhouette, usually used in clustering
problems. We conducted experiments on three levels of
agglomeration so to cover usual settings of experimen-
tal environments. The results were quantitatively con-
vincing, demonstrating the feasibility of the method,
which can handle a large number of particles at the
same time that it is much faster and less subjective
than commonly-used manual techniques.
The results support the idea that our approach can
be used in nanoparticle analysis in material engineering,
improving visual analyses for important industries, such
as cancer treatment, cosmetics, pharmaceutics, photo-
voltaics, and food.
Acknowledgements The authors are thankful to the AG
workgroup for the STM images. Bruno Brandoli was partially
supported by FAPESP under grant 02918-0. The authors also
acknowledge the support from FUNDECT.
References
1. A-L Barabasi ZO (2004) Network biology: under-
standing the cell’s functional organization. Nat
Rev Genet 5(2):101–113, DOI http://dx.doi.org/
10.1038/nrg1272
2. Antiqueira L, Oliveira-Jr O, da Fontoura Costa
L,
das
Gra¸cas
Volpe
Nunes
M
(2009)
A
complex
network
approach
to
text
summa-
rization.
Information
Sciences
179(5):584–599,
DOI
http://dx.doi.org/10.1016/j.ins.2008.10.032,
URL http://www.sciencedirect.com/science/
article/pii/S0020025508004520
3. B K, JH S, LM G, SB L (2011) Experimental
considerations on the cytotoxicity of nanoparticles.
Nanomedicine 6(5):929–941, DOI 10.2217/nnm.11.
77
4. Barab´asi AL, Albert R (1999) Emergence of scaling
in random networks. science 286(5439):509–512
5. Boccaletti S, Latora V, Moreno Y, Chavez M,
Hwang DU (2006) Complex networks: Structure
and dynamics. Physics reports 424(4):175–308
6. Brunelli R (2009) Template Matching Techniques
in Computer Vision: Theory and Practice. Wiley
Publishing
7. Canny J (1986) A computational approach to edge
detection. IEEE Trans Pattern Anal Mach Intell
8(6):679–698, DOI 10.1109/TPAMI.1986.4767851


## Page 9


A Complex Network Approach for Nanoparticle Agglomeration Analysis in Nanoscale Images
9
8. Chen S, Zhao M, Wu G, Yao C, Zhang J (2012)
Recent advances in morphological cell image anal-
ysis. Computational and Mathematical Methods in
Medicine 2012:101,536:1–101,536:10, DOI 10.1155/
2012/101536, URL http://dx.doi.org/10.1155/
2012/101536
9. Costa LdF, Rodrigues FA, Travieso G, Villas Boas
PR (2007) Characterization of complex networks:
A survey of measurements. Advances in Physics
56(1):167–242
10. Ding Y, Bukkapatnam STS (2015) Challenges and
needs for automating nano image processing for
material characterization. Proc SPIE 9556, Nano-
engineering: Fabrication, Properties, Optics, and
Devices XII 9556:95,560Z–955,607, DOI 10.1117/
12.2186251, URL http://dx.doi.org/10.1117/
12.2186251
11. Duda RO, Hart PE (1972) Use of the hough
transformation
to
detect
lines
and
curves
in
pictures. Commun ACM 15(1):11–15, DOI 10.
1145/361237.361242, URL http://doi.acm.org/
10.1145/361237.361242
12. Emin
S,
Singh
SP,
Han
L,
Satoh
N,
Is-
lam
A
(2011)
Colloidal
quantum
dot
solar
cells.
Solar
Energy
85(6):1264–1282,
DOI
http://dx.doi.org/10.1016/j.solener.2011.02.005,
URL http://www.sciencedirect.com/science/
article/pii/S0038092X11000338
13. Erdos P, Renyi A (1960) On the evolution of ran-
dom graphs. Publ Math Inst Hungar Acad Sci 5:17–
61
14. Eustace J, Wang X, Cui Y (2015) Commu-
nity
detection
using
local
neighborhood
in
complex networks. Physica A: Statistical Me-
chanics and its Applications 436:665–677, DOI
http://dx.doi.org/10.1016/j.physa.2015.05.044,
URL http://www.sciencedirect.com/science/
article/pii/S0378437115004598
15. Fisker
R,
Carstensen
J,
Hansen
M,
Bødker
F, Mørup S (2000) Estimation of nanoparticle
size distributions by image analysis. Journal of
Nanoparticle Research 2(3):267–277, DOI 10.1023/
A:1010023316775, URL http://dx.doi.org/10.
1023/A%3A1010023316775
16. Gon¸calves WN, Martinez AS, Bruno OM (2012)
Complex network classiﬁcation using partially self-
avoiding deterministic walks. Chaos: An Interdisci-
plinary Journal of Nonlinear Science 22(3):033,139,
DOI http://dx.doi.org/10.1063/1.4737515
17. Gon¸calves WN, Machado BB, Bruno OM (2015)
A complex network approach for dynamic texture
recognition. Neurocomputing 153:211–220, DOI
http://dx.doi.org/10.1016/j.neucom.2014.11.034,
URL http://www.sciencedirect.com/science/
article/pii/S0925231214015677"
18. Hassell¨ov M, Kaegi R (2009) Analysis and char-
acterization
of
manufactured
nanoparticles
in
aquatic environments. In: Environmental and Hu-
man Health Impacts of Nanotechnology, John
Wiley & Sons, Ltd, pp 211–266, DOI 10.1002/
9781444307504.ch6, URL http://dx.doi.org/10.
1002/9781444307504.ch6
19. Kaue Dalmaso Peron T, da Fontoura Costa L, Ro-
drigues FA (2012) The structure and resilience of
ﬁnancial market networks. Chaos 22(1):013,117
20. Kim DA, Hwong AR, Staﬀord D, Hughes DA,
O’Malley AJ, Fowler JH, Christakis NA (2015)
Social network targeting to maximise population
behaviour change: a cluster randomised controlled
trial. The Lancet 386(9989):145–153, DOI http:
//dx.doi.org/10.1016/S0140-6736(15)60095-2,
URL http://www.sciencedirect.com/science/
article/pii/S0140673615600952
21. Larsen RJ, Marx ML (2012) An introduction to
mathematical statistics and its applications; 5th ed.
Prentice Hall, Boston, MA
22. Li X, Wang L, Fan Y, Feng Q, Cui Fz (2012)
Biocompatibility and toxicity of nanoparticles and
nanotubes. Journal of Nanomaterials 2012:6–6,
DOI 10.1155/2012/548389, URL http://dx.doi.
org/10.1155/2012/548389
23. Liao M, qian Zhao Y, hua Li X, shan Dai
P, wen Xu X, kai Zhang J, ji Zou B (2016)
Automatic
segmentation
for
cell
images
based on bottleneck detection and ellipse ﬁt-
ting.
Neurocomputing
173(3):615–622,
DOI
http://dx.doi.org/10.1016/j.neucom.2015.08.006,
URL http://www.sciencedirect.com/science/
article/pii/S0925231215011406
24. Lorenz C, Goetz NV, Scheringer M, Wormuth M,
Hungerb¨uhler K (2011) Potential exposure of ger-
man consumers to engineered nanoparticles in cos-
metics and personal care products. Nanotoxicology
5(1):12–29,
DOI
10.3109/17435390.2010.484554,
URL
http://www.tandfonline.com/doi/
abs/10.3109/17435390.2010.484554,
http://www.tandfonline.com/doi/pdf/10.
3109/17435390.2010.484554
25. M C Jones JAR (1992) Displaying the important
features of large collections of similar curves. The
American Statistician 46(2):140–145, URL http:
//www.jstor.org/stable/2684184
26. Masciangioli T, Zhang WX (2003) Peer reviewed:
Environmental technologies at the nanoscale. En-
vironmental Science and Technology 37(5):102A–
108A, DOI http://dx.doi.org/10.1021/es0323998


## Page 10


10
Bruno Brandoli et. al.
27. Muneesawang P, Sirisathitkul C (2015) Size mea-
surement of nanoparticle assembly using mul-
tilevel segmented tem images. J Nanomaterials
2015:58:58–58:58, DOI 10.1155/2015/790508, URL
http://dx.doi.org/10.1155/2015/790508
28. Muneesawang P, Sirisathitkul C, Sirisathitkul Y
(2015) Multi-level segmentation procedure for mea-
suring the size distribution of nanoparticles in
transmission electron microscope images. Science
of Advanced Materials 7(4):769–783, DOI 10.
1166/sam.2015.1930, URL http://dx.doi.org/
10.1166/sam.2015.1930
29. Newman ME (2004) Who is the best connected sci-
entist?a study of scientiﬁc coauthorship networks.
In: Ben-Naim E, Frauenfelder H, Toroczkai Z (eds)
Complex Networks, Lecture Notes in Physics, vol
650, Springer Berlin Heidelberg, pp 337–370, DOI
10.1007/978-3-540-44485-5 16, URL http://dx.
doi.org/10.1007/978-3-540-44485-5_16
30. Park C, Huang JZ, Huitink D, Kundu S, Mallick
BK, Liang H, Ding Y (2012) A multi-stage, semi-
automated procedure for analyzing the morphology
of nanoparticles. IIE Transactions 7:507–522, DOI
10.1080/0740817X.2011.587867
31. Park C, Huang J, Ji J, Ding Y (2013) Segmenta-
tion, inference and classiﬁcation of partially over-
lapping nanoparticles. IEEE Transactions on Pat-
tern Analysis and Machine Intelligence 35(3):669–
681, DOI 10.1109/TPAMI.2012.163
32. Porter A, Rafols I (2009) Is science becoming more
interdisciplinary? measuring and mapping six re-
search ﬁelds over time. Scientometrics 81(3):719–
745, DOI 10.1007/s11192-008-2197-2, URL http:
//dx.doi.org/10.1007/s11192-008-2197-2
33. Sugahara
KN,
Teesalu
T,
Karmali
PP,
Ko-
tamraju VR, Agemy L, Girard OM, Hanahan
D,
Mattrey
RF,
Ruoslahti
E
(2009)
Tissue-
penetrating delivery of compounds and nanopar-
ticles into tumors. Cancer Cell 16(6):510–520,
DOI
http://dx.doi.org/10.1016/j.ccr.2009.10.013,
URL http://www.sciencedirect.com/science/
article/pii/S1535610809003821
34. Tan PN, Steinbach M, Kumar V (2005) Introduc-
tion to Data Mining. Addison-Wesley Longman
Publishing Co., Inc., Boston, MA, USA
35. Tenenbaum JB, Silva Vd, Langford JC (2000)
A
global
geometric
framework
for
nonlinear
dimensionality reduction. Science 290(5500):2319–
2323,
DOI
10.1126/science.290.5500.2319,
URL
http://science.sciencemag.org/content/290/
5500/2319,
http://science.sciencemag.org/
content/290/5500/2319.full.pdf
36. Tyler JR, Wilkinson DM, Huberman BA (2003)
Communities and technologies. Kluwer, B.V., De-
venter, The Netherlands, The Netherlands, pp 81–
96, URL http://dl.acm.org/citation.cfm?id=
966263.966268
37. Van Doren EA, De Temmerman PJR, Francisco
MAD, Mast J (2011) Determination of the volume-
speciﬁc surface area by using transmission electron
tomography for characterization and deﬁnition of
nanomaterials. Journal of nanobiotechnology 9(1):1
38. Vural U, Oktay A (2014) Segmentation of fe3o4
nano particles in tem images. In: Signal Process-
ing and Communications Applications Conference
(SIU), 2014 22nd, IEEE Computer Library, pp
1849–1852, DOI 10.1109/SIU.2014.6830613
39. Watts DJ, Strogatz SH (1998) Collective dynamics
of ‘small-world’networks. Nature 393(6684):440–
442
40. Zhang T, Jia W, Zhu Y, Yang J (2015) Au-
tomatic
tracking
of
neural
stem
cells
in
se-
quential
digital
images.
Biocybernetics
and
Biomedical
Engineering
36(1):66–75,
DOI
http://dx.doi.org/10.1016/j.bbe.2015.10.001,
URL http://www.sciencedirect.com/science/
article/pii/S0208521615000728

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]