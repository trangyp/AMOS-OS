---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1803.09109v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1803.09109v1_DeepWarp__DNN-based_Nonlinear_Deformation

> Source: 1803.09109v1_DeepWarp__DNN-based_Nonlinear_Deformation.pdf

> Pages: 13

---


## Page 1


1
DeepWarp: DNN-based Nonlinear Deformation
Ran Luo, Student Member, IEEE, Tianjia Shao, Member, IEEE, Huamin Wang, Member, IEEE,
Weiwei Xu, Member, IEEE, Kun Zhou, Fellow, IEEE, and Yin Yang, Member, IEEE
Abstract—DeepWarp is an efﬁcient and highly re-usable deep neural network (DNN) based nonlinear deformable simulation
framework. Unlike other deep learning applications such as image recognition, where different inputs have a uniform and consistent
format (e.g. an array of all the pixels in an image), the input for deformable simulation is quite variable, high-dimensional, and
parametrization-unfriendly. Consequently, even though DNN is known for its rich expressivity of nonlinear functions, directly using DNN
to reconstruct the force-displacement relation for general deformable simulation is nearly impossible. DeepWarp obviates this difﬁculty
by partially restoring the force-displacement relation via warping the nodal displacement simulated using a simplistic constitutive model
– the linear elasticity. In other words, DeepWarp yields an incremental displacement ﬁx based on a simpliﬁed (therefore incorrect)
simulation result other than returning the unknown displacement directly. We contrive a compact yet effective feature vector including
geodesic, potential and digression to sort training pairs of per-node linear and nonlinear displacement. DeepWarp is robust under
different model shapes and tessellations. With the assistance of deformation substructuring, one DNN training is able to handle a wide
range of 3D models of various geometries including most examples shown in the paper. Thanks to the linear elasticity and its constant
system matrix, the underlying simulator only needs to perform one pre-factorized matrix solve at each time step, and DeepWarp is able
to simulate large models in real time.
Index Terms—deep neural network, machine learning, data-driven, nonlinear regression, deformable model, physics-based simulation
!
1
INTRODUCTION
Nonlinear shape deformation is ubiquitous in our every day life
and simulating deformable objects has long been considered as
an important yet challenging task for computer graphics and
animation. In the past ten years, the ﬁnite element method (FEM)
based frameworks [1] become more and more popular due to its
versatility of encoding various material behaviors. With the pre-
scribed external force fext, the dynamic equilibrium is forwarded
by solving a high-dimensional nonlinear system of f(u) = fext1 at
each time step. Most nonlinear solvers start with an initial guess
of the unknown displacement u and iteratively reﬁne the result
until the system converges in order to calculate the deformed
model shape. While conceptually straightforward, the requirement
of repetitive evaluations of the nonlinear internal force fint or/and
its gradient ∂fint/∂u makes the simulation rather computational
expensive.
Recently, the rapid development of the computing hardware
pushes forward the frontier of machine intelligence to an unprece-
dented extend, and we have witnessed tremendous successes of
utilizing carefully constructed deep neural networks (DNNs) [2]
•
Ran Luo and Yin Yang are with Department of Electrical and Computer
Engineering, University of New Mexico, NM, 87131
E-mail: {luoran|yangy}@unm.edu
•
Tianjia Shao is with the School of Computing, University of Leeds, UK,
LS29JT.
E-mail:tianjiashao@gmail.com
•
Huamin Wang is with Department of Computer Science and Engineering,
Ohio State University, OH, 43210.
E-mail: whmin@cse.ohio-state.edu
•
Weiwei Xu and Kun Zhou are with State Key Lab of CAD&CG at Zhejiang
University, China.
E-mail: weiwei.xu.g@gmail.com;kunzhou@acm.org
1. Here f(u) is the general internal force, which consists of standard
nonlinear internal force, damping force and inertial force. It is a function of
the unknown displacement u after time derivative terms are linearized based
on the chosen time integration method.
DNN
Figure 1. DeepWarp is a data-driven DNN-based nonlinear deformable
simulator. By learning from full FEM simulation poses, it yields more
accurate results than existing warping methods. We design three com-
pact contextual features making the DNN training highly re-usable. In
this example, the maple bonsai model consists of 255,552 elements,
and is decomposed into 1,771 domains. A single DNN trained using a
regular beam handles local dynamics for all the domains. High-quality
animations with well-preserved local high-frequency deformations are
produced at a near-interactive rate (5 FPS) without using model reduc-
tion.
in many classic computing problems like language processing [3],
speech recognition [4], [5], object tracking [6], [7] etc. With the
support of sufﬁcient ground truth data, DNN serves as a black box
mapping its input to the output without the necessity of an explicit
mathematical formulation. Since the FEM simulation is able to
provide us as many as needed noise-free data, can we also exploit
DNNs to deal with deformable simulation?
At the ﬁrst sight of the question, the answer seems to be
positive because deformable simulation is essentially the recon-
struction of the force-displacement relation of an elastic body,
and DNN is known to be skilled at expressing complex non-
arXiv:1803.09109v1  [cs.GR]  24 Mar 2018


## Page 2


2
linear relations [8], [9]. However, this problem is challenging
in practice because the nonlinear force-displacement relation
varies signiﬁcantly (and intrinsically) under different simulation
conﬁgurations such as domain geometry, discretization, boundary
condition, constitutive law etc. If one chooses to build a network
incorporating all the possible input permutations, the network
would indubitably be an extremely huge and complex one. Even
we manage to generate sufﬁcient training data and optimize the
network parameters to a reasonable level. A single forward pass of
the network itself could take a longer time than running a regular
FEM simulator due to the complexity of the network.
In this paper, we present a method, named DeepWarp, to
leverage DNNs to tackle intricate force-displacement relations
of different nonlinear materials with a simple and light-weight
network. As the name implies, our strategy is not to link the
standard input (fext) and output (u) of deformable simulation via
a neural network directly. Instead, we map or warp a simpliﬁed
constitutive model C0 to a more complex and nonlinear one C1
using DNNs. It is expected that, the calculated displacement
under C0 well encapsulates simulation conﬁgurations like force
magnitude, domain tessellation and boundary conditions so that
the remaining warp is local, and can be well ﬁt by a simple net.
To this end, we choose to use the linear elasticity for C0. The
reasons are twofold. First, the linear elasticity has long been used
to describe small-scale deformations (i.e. the inﬁnitesimal strain
theory). It is based on the Cauchy strain tensor, which is the ﬁrst-
order Taylor approximation of the full Green tensor. Second, as
long as the deformable model is nonlinear, either material-wise or
geometry-wise, the asymptotic complexity of simulating one time
step is O(N3) for the system of N degrees of freedom (DOFs).
Only the linear elasticity has O(N2) complexity because of its
constant system matrix. In other words, we gain a polynomial
performance proﬁt by setting C0 as a linear model.
DeepWarp uses a single node-wise DNN to correct the nodal
linear deformation to the corresponding nonlinear one. From
this perspective, our method is conceptually similar to stiffness
warping [10] and modal warping [11], in which a linear solver
is used after warping the deformed shape back to its undeformed
orientation. We contrive three novel discriminative features as the
input of the DNN, namely the geodesic, potential and digression.
We ﬁnd that with these three descriptors, DeepWarp becomes
fairly shape- and tessellation-independent, and the network trained
with a simple model can be used to warp deformable bodies
of distinctively different geometries making our DNN training
highly re-usable. This important advantage is further enhanced
when combined with the substructuring method [12], where we
decompose the input model into multiple convex domains, and run
DeepWarp on each domain separately. All the examples reported
in the paper except Fig. 10 are based on the DNN trained using a
regular rectangular beam model. DeepWarp is fast at both training
stage and simulation stage. We utilize the rotation invariant feature
of local deformation and compress the training set by at least an
order. During the simulation run time, as DeepWarp only needs to
perform a pre-factorized linear solve at each time step, it is able
to handle large-scale models interactively.
2
RELATED WORK
The concept of deep learning can be dated back to late 1980s [13]
in the machine learning community. Empowered by recent hard-
ware advance, deep neural networks of various architectures have
been harnessed to solve many long-standing computer vision prob-
lems such as recognition [14], [15], classiﬁcation [16], [17], [18],
[19] and segmentation [20], [21], [22]. Some existing methods are
able to match or even beat human’s vision perception system e.g.
see the report from the ImageNet Large Scale Visual Recognition
Challenge (ILSVRC) [23]. Given sufﬁcient training data, DNNs
provide a general “template” for the user to learn the input-
output correspondence, which could be otherwise difﬁcult or even
impossible to be analytically formulated.
Learning for animation
Indeed, the idea of learning is not
new to computer animation, and it is also widely-known as the
data driven method [24]. For the cloth animation, low-resolution
simulation can be enriched by using pre-computed high-resolution
results with detailed wrinkles [25], [26]. Wang et al. [27] built a
piecewise linear stretching and bending model based on measured
data to better depict the nonlinear dynamics of different cloth
materials. Miguel et al. [28] further enhanced this framework
and recorded more deformation behaviors of the cloth simulation.
Kim et al. [29] proposed a method to compress a large pre-
simulation dataset so that these poses can be used at run time
to improve the inertial cloth deformation. Following the similar
idea, Xu et al. [30] blended pre-computed cloth shapes to directly
synthesize the cloth deformation using the sensitivity analysis.
Learning-based methods have also been popular for motion and
control i.e. the reinforcement learning [31], [32], [33], [34]. DNNs
provide a convenient approach for further improving the learning
effects [35]. Following this direction, Liu et al. [36] employed the
deep Q-network to reorder existing control fragments and created
necessary responses to unseen disturbances. Peng et al. [37] used
a DNN to train a high-level controller and a low-level one,
which achieved robust locomotion coordinately. Holden et al. [38]
designed a phase-functioned neural network, whose weights are
computed using a cyclic function. For solid modeling, learning
is also a powerful tool, which allows the user to obtain actual
physical parameters based on captured point cloud sequences [39].
Xu and Barbiˇc [40] ﬁne-tuned the damping model based on a
few example deformations. Kim et al. [41] combined the physics-
based simulation and data-driven to produce realistic soft tissue
animation. Jones et al. [42] used the similar idea to simulate
plastic deformation with a skinning-alike method. An et al. [43]
proposed a learning-based numerical procedure named Cubature
to efﬁciently evaluate the internal force and the force gradient
during reduced deformable simulation. Deep learning also beneﬁts
the ﬂuid animation. For instance, Ladicky et al. [44] proposed
a random forest based regression method to accelerate ﬂuid
simulation by predicting the kinematic conﬁgurations of particles
based on a large training set. Chu and Thuerey [45] used the
convolutional neural networks (CNN) to extract necessary features
to augment a coarse simulation and add back high-frequency
details.
Nonlinear deformable simulation
Physics-based deformable
simulation has been an active research topic in graphics and
animation since the exemplar work by Terzopoulos et al. [46].
While particle-based methods [47], [48], [49] or mass-spring
systems [50], [51] are also legit, FEM becomes more widely-
used [52] for solid simulation. Wang et al. [53] proposed a
strain limiting method to increase the numerical stability for stiff
deformable bodies. Alternatively, Irving et al. [54] tweaked the
principle stress to resolve degenerated elements from extreme
deformations. Forming the deformable simulation as a nonlinear


## Page 3


3
optimization procedure, Hecht et al. [55] used an incremental
Cholesky factorization scheme to lower the frequency of matrix
re-factorization during the simulation. Zhu et al. [56] adopted
the multi-grid method to simulate high-resolution deformable
volumes. Bouaziz et al. [57] introduced a robust local-global
iterative solver named projective dynamics. This idea later was
generalized as the ADMM solver [58] and synergized with
Chebyshev [59], [60], L-BFGS [61] and GPU Gauss-Seidel [62].
Accelerating nonlinear simulation can also be achieved by pre-
computed models, for instance using modal analysis [63], [64],
[65] or recent fullspace simulations [66]. Also known as model
reduction methods, it is assumed that the deformed shape be a
linear combination of those pre-computed poses or modes so that
the simulation can be projected into the spanned subspace. In
an asymptotic sense however, model reduction is not better than
regular simulation as the time complexity remains cubic w.r.t. the
number of simulation DOFs.
Warping methods
In this paper, we re-investigate this classic
animation problem of nonlinear deformable simulation from a
data-driven angle by shaping it as a nonlinear regression using the
DNN. Unfortunately, the full spectrum of the force-displacement
relation is complex and sensitive to the variance of simulation
settings. For instance, modifying the boundary condition (the
anchor nodes of an FE mesh) could completely alter the deformed
shape even with other simulation parameters unchanged. Besides,
the dynamic simulation is essentially 4D – the kinematic status of
the deformable body does not only depend on its current external
stimuli but also on its motion trajectory. To circumvent these
two practical obstacles, we forge our regression based on the
simulation result obtained using the linear elasticity. This idea is
not new in graphics. An epic example would be the stiffness warp-
ing [10], which re-used the linear stiffness matrix by un-rotating
the external force back to the model’s rest shape orientation.
Similarly, modal warping [11] and rotation-strain coordinate [67],
[68] embedded a local coordinate frame at each node/element
to relieve the artifacts of the linear elasticity under rotational
deformation. This idea was also used for geometrically construct-
ing nonlinear modes [69]. These geometric warping techniques
have been proven effective for animation editing [70], [71], which
requires performing high-dimensional space-time optimization.
Solving the linear elasticity encodes many simulation param-
eters such as boundary condition, tessellation resolution, external
force etc. into the resulting linear displacement vector. On the
top of this, we train a neural network to further correct the
result to be a plausible and nonlinear one without worrying
about accommodating all the simulation settings into the net. Our
training is re-usable – we train a DNN using a regular model
of few thousand elements, and the network can then be used to
handle a wide range of geometrically complex deformable bodies.
During the simulation, because the system matrix for the linear
elasticity is constant and pre-factorized, we obtain O(N2) run-
time complexity in fullspace, which is polynomially faster than
existing nonlinear solvers.
3
DNN FEATURE VECTOR
The underlying mathematical relations between external forces
and displacements of elastic bodies could be intrinsically changed
under different simulation settings, and it is impossible in practice
to encode the entire simulation conﬁguration into a feature vector
and feed to a neural network. Therefore, the primary challenge we
are facing is to ﬁgure out an informative and compact feature vec-
tor as the DNN input. Informative refers to the discriminability of
the feature so that an irrelevant training instance does not interfere.
Compact means the feature should also be general so that the built
network is small and light-weight. In this section, we start with
a short review of the deformable model, pointing out that while
the simulation is sophisticated, the linear-nonlinear deformation
map of a small local volume is actually smooth. On the top of it,
we show that our heuristic feature vector augments the extracted
kinematic information and produces plausible results.
3.1
Deformable model: a quick review
Given an arbitrary material point x on the deformable body, its
deformation gradient F ∈R3×3 is computed as F = ∂x/∂¯x, where
¯x and x denote its rest shape position and the deformed position.
Alternatively, we can also express x using its displacement u as
x = ¯x + u. Let G = ∂u/∂¯x and we name this 3 by 3 tensor as
displacement gradient tensor. It is easy to verify that F = G + I.
Under the linear elasticity, the deformation is described using the
Cauchy strain: eε = 1
2(G+G⊤), and the strain energy density eΨ is:
eΨ =
k
2(1+ν)eε : eε +
kν
2(1+ν)(1−2ν)tr2(eε).
(1)
Here k and ν are the Young’s modulus and Poisson’s ratio. Clearly,
eΨ is a quadratic function of G. Therefore, the corresponding Piola
stress becomes a linear function of G:
eP =
k
2(1+ν)
 G+G⊤
+
kν ·tr(G)
(1+ν)(1−2ν)I.
(2)
For most other hyperelastic materials, the deformation is actually
described with the Green strain: ε = 1
2(FF⊤−I) = eε + 1
2GG⊤.
One can see that the Cauchy strain used in linear elasticity is
simply the linear portion of the Green strain. Take the St. Venant-
Kirchhoff (StVK) material an example, whose strain energy den-
sity is formulated by replacing eε by ε:
ΨStVK =
k
2(1+ν)ε : ε +
kν
2(1+ν)(1−2ν)tr2(ε),
(3)
which is a fourth-order polynomial of the displacement gradient
G, and its stress is cubically related to G. With the help of FEM,
the differential strain-stress relation is integrated and becomes the
macroscopic force-displacement relation that we are interested in.
0
0.5
1
1.5
2
Stress magnitude
Strain magnitude
linear
co-rotation
Neo-Hookean
StVK
In reality, the magnitude
of
a
deformation,
which
may be imprecisely under-
stood as |G|, is typically
small. For instance, dou-
bling the length of an elastic
rope by stretching is con-
sidered a very large defor-
mation where |G| = 1. Besides, strain-stress curves for various
materials are all aligned at the origin (a zero strain yields a zero
stress) and within the same monotonically increasing interval (a
larger strain yields a larger stress in general). This implies that
even though a linear function could deviate a lot from a cubic one
(or other nonlinear relations), the strain-stress curves of the linear
elasticity and a nonlinear elasticity do not fundamentally differ
from each other in regular deformable simulations. An example
is given in the inset ﬁgure, where we plot the strain-stress curves
of the linear, co-rotation, StVK and Neo-Hookean laws under a
rotation-free linear stretch.


## Page 4


4
Geometric warp
In fact, the dominant factor drives the linear
elasticity away from a nonlinear counterpart is not the material
nonlinearity, but the geometry nonlinearity. This is because a rigid,
deformation-free rotation leads to a non-zero Cauchy strain, which
produces unrealistic deformation effects. Under this consideration,
the modal warping (MW) technique [11] embeds each node on the
mesh a local frame. The curl of local displacement ﬁeld around
the i-th node is calculated: wi = ∇× ui. If it takes a unit time to
displace node i from ¯xi to ¯xi + ui, ui also represents its velocity
at t = 1. wi can then be understood as its angular velocity at the
same moment. Based on this assumption, MW linearly ramps the
angular velocity from the rest shape to the current time instance t
and calculates a warp transformation as:
WMW = 1
t
Z t
0 exp
τ
t [wi]×

dτ,
(4)
where [wi]× is the skew symmetric matrix of wi. Similarly, one
can use rotation-strain coordinate by decomposing the Gi into
a skew symmetric part: [wi]× = (Gi −G⊤
i )/2 and a symmetric
part: Si = (Gi +G⊤
i )/2 [67], [68]. The rotation-strain warp (RSW)
transformation can then be computed treating wi as an Euler
vector:
WRSW = exp([wi]×)(Si +I)−I.
(5)
While not physically accurate, these geometric warping methods
produce visually pleasing shapes and have been used in many
time-critical graphics applications [70], [71].
3.2
Linear-nonlinear correspondence
DeepWarp is inspired by the encouraging results from the existing
warping methods. However, DeepWarp does not explicitly assume
a ﬁxed nonlinear regression formula as Eqs. (4) or (5) do. Instead,
we train a DNN to obtain a more accurate regression based on full
simulations. The key question here is how to determine what is the
“right” deformation that corresponds to the one calculated using
the linear elasticity.
Figure 2. Different motion trajectories lead to different equilibrium
shapes even under the same external force (highlighted as the blue
arrow).
A na¨ıve thought is to solve the quasi-static equilibrium of
fint(u) = fext for a deformable body under the same external
force and boundary condition using the linear elasticity and a
nonlinear constitutive model. Unfortunately, this method is only
valid for small deformations. Under large external forces, the
nonlinear system could reach multiple local minima with different
shapes, and which one being reached is context-dependent i.e.
up to the history of the deformation trajectory (Fig. 2). From a
numerical point of view, the solution of fint(u) = fext depends on
the initial guess of u and the strategy of computing ∆u during the
iteration. The iteration may not converge to the global minimum
if the starting guess is far away from it.
Our solution to this problem is to register a linear deformation
sequence to a nonlinear one starting from the rest shape. Speciﬁ-
cally, given an external force fext, we compute a series of quasi-
static linear deformation by solving the Euler-Lagrange equation
with an increased mass damping so that the acceleration at each
time step is negligible. Each time step yields a linear displacement
vector eu, and we estimate a local rotation for the i-th node as:
Ri = exp
 h
∇×
 PiP⊤
i
−1P⊤
i Ui
i
×

,
(6)
where columns in Pi and Ui are rest shape positions and dis-
placements of neighbor nodes adjacent to i. In other words,
 PiP⊤
i
−1P⊤
i Ui gives a least-square evaluation of G around the
i-th node. The linear internal force at the current time step is
efint = Keu. Note that efint ̸= fexp until the ﬁnal equilibrium is
reached due to the existence of the damping. Afterwards, the
corresponding nonlinear deformation u is obtained by solving:
min
u |fint(u)−RKeu|,
(7)
where R is a block-diagonal matrix, and each of its 3 by 3 diagonal
block is the estimated nodal rotation computed via Eq. (6). We use
Newton’s method to solve Eq. (7) by setting the initial guess of u
as the solution in the previous time step. In our implementation,
we notice that Newton’s method occasionally fails during the
iteration. Therefore, we impose the Wolfe condition [72] to adjust
the step length.
In our DNN training, we simplify the external force setting
by only considering two types of fext: directional force ﬁeld and
circular force ﬁeld. The directional ﬁeld uses a prescribed force
direction, while the force direction in the circular ﬁeld follows the
tangent direction of a set of concentric circles. Such simpliﬁcation
frees us from generating an overwhelmingly large training set due
to diverse external force conditions. Its limitation is also obvious:
DeepWarp may lose some local deformation effects induced by
high-frequency external force.
3.3
Discriminative feature
With paired ⟨eu,u⟩, we can build a node-wise regression machine
using a DNN that replaces Eq. (4) or Eq. (5). For the i-th node,
in addition to its linear displacement eui, the rotation information
of its local displacement gradient Gi is directly pertinent to the
warp transformation, and should be passed to the DNN as the
input. To this end, we choose to use the skew symmetric part of
Gi and represent it as a 3-vector as in [67]. However, only feeding
these two pieces of information to the DNN is not enough, and the
resulting deformation appears jittery and non-smooth as shown in
Fig. 3. In this example, we use the Neo-Hookean elasticity, whose
strain energy is:
ΨNH =
k
4(1+ν)[I1 −log(I3)−3]+
kν
8(1+ν)(1−2ν) log2(I3).
(8)
I1 and I2 are the invariants of the deformation gradient, deﬁned
based on F’s singular values σ1, σ2 and σ3 such that: I1 = σ2
1 +
σ2
2 +σ2
3 and I3 = σ2
1 σ2
2 σ2
3 .
This artifact was also noticed and discussed in previous data-
driven simulation literature [44], which is because pure node-wise
kinematic features do not contain sufﬁcient contextual informa-
tion, and thus are not discriminative to reach a conclusive per-node
linear-nonlinear map. To further illustrate this artifact, we pick a
jittery node (marked as a red sphere in the ﬁgure) and inversely


## Page 5


5
…
no discriminative feature
nodes from training poses with similar feature (relative L2 error < 5%)
with geodesic
Figure 3. Only using kinematic feature as the input of DNN yields noticeable jittery artifacts. A node, because of its kinematic feature is not
discriminative, could be inﬂuenced by many irrelevant instances in the training date. Large discrepancies among these mis-matched nodes induce
high-frequency variations of the DNN mapping. Incorporating geodesic feature effectively eliminates this artifact.
query for nodes in our training set that have similar features (< 5%
relative L2 error w.r.t. the feature vector from the picked node). We
can see from the ﬁgure that there are a number of training poses
having multiple nodes (on the red areas) with very similar feature
vectors as the input. In other words, the ﬁnal displacement of the
picked node becomes a certain mixture of displacements of many
distant and irrelevant nodes. Such ambiguity of pure kinematic
feature is the primary reason behind this artifact.
One of our contribution is to design a compact contextual
feature to resolve this mis-math. While one could follow the
method used in [44] to use the integral features of local dynamic
parameters around a node, we found that our simple strategy yields
satisfying result. We speculate that this is because DOFs in solid
simulation are more tightly coupled than in ﬂuid simulation [44].
An important advantage of such compactness is that the DNN
training is also quite fast. Compared with state-of-the-art pre-
computed deformable models i.e. [43], we can ﬁnish training in
a few minutes, and the obtained DNN can be applied to a wide
range of models.
Discriminative feature I: geodesic
The geodesic of a node i,
gi is the normalized length of the shortest path from node i to its
nearest anchor node within the deformable body. For a training
model, we ﬁrst uniformly scale it to ﬁt a unit bounding sphere.
Then, we compute the shortest path using the Dijkstra’s algorithm
for all the un-anchored nodes. Lastly, calculated path lengths are
scaled by the maximum geodesic so that all the g values are
within the normalized interval of [0,1]. Our heuristic of choosing
the geodesic feature is based on the observation that if a node is
closer to an anchor node, it trends to have less deformation than
nodes that are away from it. By inducing the geodesic feature, a
node far from anchor nodes does not miss-pair to a node close
to anchor nodes only because the it undertakes a smaller external
force. Consequently, the jittery artifact is effectively removed as
shown in the rightmost snapshot in Fig. 3.
geodesic only
training nodes with similar feature geodesic + potential
stretched
compressed
Figure 4. Volume expansion artifact remains even with the geodesic
feature added. This is because the nodes with similar geodesic value
may have different internal tractions. We use the potential feature to sort
the training data to avoid this issue.
Discriminative feature II: potential
Including the geodesic
feature however, does not avoid the artifact of volume increase and
shrinkage. As shown in Fig. 4, bending the beam also increases
its volume noticeably, especially at curved areas. In order to dig
out the missing contextual information behind this issue, we use
the similar approach by picking a node within the problematic
area and query the instances from our training set that have a
similar feature of the selected one. We can see from the ﬁgure that,
thanks to the incorporated geodesic feature, now this selected node
only pairs with a training pose under a very similar deformation.
However, it still matches multiple nodes on this pose. This is
because the beam is a symmetric shape, and a loop of nodes on
its surface have similar geodesic values – among which, some
are stretched and some are compressed. Without being able to
distinguish these contexts, the volume of the warped model is
likely to shrink or expand unnaturally.
p
We notice that whether nodes
are being stretched or compressed
typically depends on their relative
positions in the applied force ﬁeld.
Therefore, we introduce another
scaler feature named potential p to
resolve this ambiguity. If a directional force ﬁeld is applied, for
each node on the mesh, we project its rest shape position onto the
force direction and re-map the resulting projections to the interval
of [0,1]. On the other hand, if a circular force ﬁeld is applied, the
potential of a node is the distance between its rest shape position
and the circular axis, as shown in the inset ﬁgure. This value is
also scaled to [0,1]. As we can see from Fig. 4, the deformation of
the beam model is almost identical to the one obtained using the
full simulation after we inject the potential feature into the DNN.
Discriminative feature III: digression So far, we generate a set
of registered linear and nonlinear poses of the beam model. Node-
wise linear to nonlinear deviation is learnt by a DNN, which is then
used to warp a linear displacement of the same model to obtain
its nonlinear shape. While the results are visually plausible, real-
world applications will require deformable animations of various
3D models. DeepWarp becomes cumbersome and less practical if
one needs to re-train a DNN for each different deformable body.
Unfortunately, if we alter the rest shape geometry of the beam
model as shown in Fig. 6, unrealistic jittery deformations are
observed again even after incorporating geodesic and potential
features. By querying the training set, we see that because the
updated shape is irregular and asymmetric, the most similar train-
ing poses become the ones under oblique force ﬁelds regardless
an upright gravity force ﬁeld is applied in the simulation. To
further correct this mis-match, we use the digression feature d


## Page 6


6
training model I
reduced tessellation
twice thicker
bigger mid
smaller mid
cylinder
bigger left
pentagon
smaller left
sphere
geodesic
potential
digression
DeepWarp
ground truth
training model II
two-end ﬁxed
Figure 5. We test the generality of the designed features on a variety of shapes. The training data are generated using the standard rectangular
beam (highlighted by a red box). The resulting DNN successfully handles many beam-like models but with distinctively different shapes. The
distributions of three features are also plotted.
…
geodesic + potential
training nodes with similar feature 
an irregular beam
ground truth
DeepWarp
geodesic + potential + digression
Figure 6. In order to make DeepWarp re-usable for various deformable
bodies, we use the digression as our third discriminative feature. With
this feature included, DNN is able to handle an irregular beam based on
the training set generated using a standard rectangular beam model.
to describe the nodal position w.r.t. the direction of the external
force. Speciﬁcally, the digression for node i is deﬁned as:
di = arccos
 ¯xi −¯xa
|¯xi −¯xa| · fext
|fext|

,
(9)
where ¯xa is the rest shape position of the anchor node that is
closest to node i. Indeed, digression sorts nodes based on their
local orientational deviations from the external force direction.
The digression feature ranges from 0 to π. If a circular force ﬁeld
is applied, the digression is simply set as −1. As shown in Fig. 6,
with geodesic, potential and digression included, the training data
generated using a rectangular beam model can also be used to
warp the irregular beam, and DeepWarp produces high-quality
nonlinear deformation.
Discussion
Our features allow the resulting DNN well handles
models with various shapes, different tessellations and altered
boundary conditions. More results can be found in Figs 5 and 7.
From these examples, readers may probably notice that geodesic,
potential and digression features actually provide a volumetric
parametrization of deformable bodies so that models of different


## Page 7


7
DeepWarp
ground truth
Figure 7. DeepWarp works well under circular force ﬁeld too. In this
case, the digression feature is set as -1 for all the nodes on the mesh.
geometries and tessellations are somehow registered in a meaning-
ful way, and node-wise DNN can then be applied. In fact, there are
many elegant algorithms in graphics and computational geometry
that generate the volumetric map between different shapes [73],
[74], [75]. However in the context of DeepWarp, this volumetric
map depends on the conﬁguration of external force and boundary
conditions. While existing methods may also be modiﬁed to
incorporate these additional conditions or constraints, we found
that our simple strategy sufﬁces in most cases. An exception is
reported in Fig. 8, and we ﬁnd that DeepWarp using a convex
training model often fails when the deformable body gets more
concave. Next, we will show how to walk around this limitation
without re-training a DNN based on the target shape.
Figure 8. When the shape becomes more concave, DNN trained using
a rectangular beam produces artifacts.
4
INCORPORATE COMPLEX SHAPES
training model
domain 
decomposition
domain graph

Figure 9. Building domain graph for
the domain decomposed model is
an easy and effective way to identify
shapes with similar concavity.
The exhaustiveness of 3D geo-
metric diversity is endless. Ob-
viously, training set generated
with a single rectangular beam
cannot cover all the different
feature combinations. We ﬁnd
that the DNN trained using the
beam model is able to deal
with many convex 3D shapes
(i.e. see Fig. 5). However, it
often fails when the target de-
formable body becomes more
concave (Fig. 8). A straightfor-
ward idea is to train the DNN
using a model with similar con-
cavity of the target deformable body, but how to describe the
similarity of concavity among 3D shapes?
We borrow the idea from the graph theory, and subdivide
a concave model into several convex components or domains.
Afterwards, we create a domain graph G by using a graph vertex to
represent each of the subdivided domains. An edge connects two
vertices if and only if the corresponding two domains are face-
connected on the original mesh. We ﬁnd that if the domain graph
G is isomorphic to the domain graph of the training model Gtrain
or G ≃Gtrain, DeepWarp typically yields satisfying results. An
example can be found in Fig. 9. The T-shape beam is decomposed
into three domains, each of which is convex and rectangular. Its
domain graph is isomorphic to many similar concave shapes like
the Y-shape beam, the arrow-shape beam, the crossing beam etc.
If we use the T-shape beam as the training model, the resulting
DNN is able to handle all of these variations as veriﬁed in Fig. 10.
Even utilizing the concept of graph isomorphism, one may still
have to re-train the DNN (and re-generate training poses) for an
arbitrary geometrically complex model, which is tedious and time
consuming. A more general and powerful solution maximizing
the re-usability of the DNN training is to use the substructuring
method [12]. This method wisely leverages the hierarchical propa-
gation of the deformation over a complicated structure and isolates
the deformable simulation at each individual domain sequentially.
While it loses some physics accuracy (mostly, the frequency of
the trajectory due to the mass lumping, which can also be ﬁxed
as in [76]), the resulting deformation is natural and realistic. After
the domain decomposition is complete so that each domain is a
convex 3D shape, we can use one representative convex model to
train the DNN. With the help of the proposed three discriminative
features, the resulting DNN is able to correct local dynamics of all
the domains.
In our DeepWarp version of substructuring, the dynamics of
the domain Dj is updated and corrected by DeepWarp. After
that, we calculate the best-ﬁtting linear transformation Aj,k for
the small patch of the mesh interfacing Dj and one of its children
domain say Dk as A j,k = (P j,kP⊤
j,k)−1P⊤
j,kQ j,k, where P j,k and Q j,k
store the rest shape and deformed positions of all the nodes on the
interface patch. We extract the relative rotation between Dj and
Dk using the polar decomposition as A j,k = Rj,kSj,k. Based on
this, the angular velocity ωj,k and the angular acceleration ˙ω j,k
can be calculated. Each domain is pinned to a local non-inertial
reference frame. Therefore, in addition to the regular external
forces, inertial forces originated from the accelerated linear and
angular motion of the interface should also be computed as the
system force and the interface force. We refer the reader to the
related reference from Barbiˇc and Zhao [12] for the detailed
formulation.
An example is given in Fig. 1, where the DeepWarp is
still based on a rectangular beam model. However, because we
decompose the maple tree into domains of branches and leaves, the
DNN well handles nonlinear dynamics for each domain regardless
how complex the original mesh is. Unlike other tree simulation
results in the literature [12], [65], [76], [77], the example given in
the ﬁgure is simulated in the fullspace without any reduction of
the simulation DOFs. Therefore, local high-frequency details are
well preserved. The simulation is close to interactive at 5 FPS –
this is roughly 1,000 times faster than running fullspace nonlinear
simulation using substructuring.
5
DNN CONFIGURATION AND TRAINING
The input of our DNN includes kinematic features of the linear
displacement of the i-th node eui and its instantaneous angular


## Page 8


8
Figure 10. While a simple rectangular beam is not able to handle highly concave shapes, by referring to the domain graph we can train a DNN
using a T-shape beam and the resulting network can be used to warp a wide range of concave beams whose domain graphs are isomorphic to the
T-shape beam.
velocity wi = ∇×
 PiP⊤
i
−1P⊤
i Ui as in Eq. (6). As to be dis-
cussed shortly, we further compress this pair of vectors into three
scalars utilizing the rotation invariance property of the isotropic
hyperelastic material. Doing so signiﬁcantly relieves the effort of
generating the training set. Besides, three discriminative features
of geodesic, potential and digression are also included. We ﬁnd
that the Young’s modulus k behaves more like a linear ampliﬁer.
Increasing Young’s modulus yields a deformation similar to the
one obtained by reducing the magnitude of the external force.
Therefore, this material parameter is not explicitly fed to the
DNN. However, Poisson’s ratio ν controls the volume change,
and its impact on the ﬁnal deformation is much more nonlinear.
This is also reﬂected in the strain energy formulation of Eqs. (1),
(3) and (8). As a result, the Poisson’s ratio is also an input
feature. Other simulation conﬁgurations like the external force,
tessellation, boundary conditions are not the DNN input since we
believe this information is well encoded during the linear solve.
The ﬁnal input DNN feature is a seven-dimension vector, and
the DNN outputs a 3D vector of δui corresponding to a node-
wise displacement ﬁx so that eui + δui is a well approximated
nonlinear nodal displacement for a target material model. We
use a different DNN for a different nonlinear material instead of
building a comprehensive one.
Training data alignment
The complexity of a neural network
highly depends on its input [9]. For instance, wi can be extracted
from the displacement gradient tensor Gi. Nevertheless, if we
simply put all the nine elements of Gi into the network, much
higher training and testing errors are observed, which could only
be improved by spanning the network depth and generating more
training data. In order to make the DNN as compact as possible,
we further align vectors eu and w based on the fact that a nodal
deformation measure can always be examined within a local
coordinate frame which is invariant under rotations.
Π
Π
Figure 11. Rotation invariance
allows us to further compress
the input DNN kinematic feature.
This procedure is illustrated in
Fig. 11. Suppose we have two
nodes i and
j. They are sur-
rounded by two inﬁnitesimal vol-
umes, which are small enough to
be considered as symmetric in all
the orientations. We ﬁrst rotate
these two volumes so that the linear
displacements eui and eu j are both
in the positive y direction. The follow-up rotation is around the
y axis. One can pick an arbitrary direction (the black vector in
the ﬁgure) within plane Π1, which is perpendicular to the y axis.
In our implementation, we set this direction as the negative x
axis. After that, wi and w j are rotated so that they both reside
in plane Π2 i.e. the xy plane in our implementation. Because the
second rotation is around the y axis, eui and euj remain aligned.
By doing so, pairs of eu and w only differ at the magnitude or
the norm of the linear displacement, the magnitude of w and the
angle between them. In other words, the real useful kinematic
information hidden behind vectors eu and w are only three scalars.
If one insists on putting the original eu and w into the DNN, DNN
must learn this double-rotation alignment out of the training data
ﬁrst and then ﬁts the linear-nonlinear map. Unfortunately, DNN
is not good at processing such rotation invariant features. For
instance, in existing works of using deep learning to perform
3D shape analysis [78], [79], in order to relieve the burden of
the analysis of rotation invariant shape features, it is common


## Page 9


9
to use rotation augmentation that duplicates a training data by
rotating it from multiple angles. The ﬁnal result is pooled out of
all the rotated duplicates. Using data alignment, the size of the
training set is reduced by over 10 times, and the training time is
also signiﬁcantly shortened. Fig. 12 plots the distribution of 1,000
randomly picked kinematic features.
0
20
40
60
80
100
120
140
160
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
1.2
0
0.2
0.4
0.6
0.8
1
0
20
40
60
80
100
120
140
160
0
0.5
1
1.5
|
|
| |
∠
|
|
∠
| |
Figure 12. The distribution of three kinematic features of 1,000 entries
after the alignment. ∠euw denotes the angle between aligned vectors eu
and w.
Generating training set
It is important to make sure that the
training set covers the feature space of the simulation, because
machine learning is known to have a relatively poor performance
for extrapolation. For the direction of the external force ﬁeld, we
evenly scatter samples over a unit semi-hemisphere surface for
the rectangular beam model. Speciﬁcally, we uniformly sample
two variables α and β from the interval of [0,π/2], which
correspond to the latitudinal and longitudinal spans on the semi-
hemisphere. The unit directional vector can be calculated as:
e = [sinβ cosα,cosβ,sinβ sinα]⊤. The magnitude of the external
force determines the magnitude of the linear displacement, which
could be an inﬁnitely large vector in theory. However, as we
have already normalized our training model into a unit sphere,
an excessively large displacement vector is unlike to occur in a
real simulation application. Therefore, we stop exserting bigger
external force if |ui| ≥2 during the training data generation.
The discriminative features g, p and d are essentially for
model registration. Therefore, how they are sampled depends
on the training model’s geometry and tessellation. In general, a
moderately ﬁne mesh should sufﬁce for these features. However,
if the training model is too coarse i.e. with few hundred elements,
one may observe artifacts after warping.
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0.10
0
5
10
15
20
Training error
# epoch
Figure 14. Training error vs epoch of
the Adam solver.
Training
speciﬁcations
In
our implementation, the beam
model for the DNN training
consists of 2,629 elements, and
we generate 20,829 training
poses
including
16,730,893
training
nodal
pairs
and
167,309 validation nodal pairs.
The test data is 1/7 of the
training data with 2,064,812
nodal
pairs.
Training
and
testing data are stored as binary ﬁles in .npy format with a
total size of 1.42 GB. Unlike [45], we do not need to load these
training poses during the simulation. Only the resulting network
parameters are needed. While the warping transformation is
regressed using a DNN, the network is not actually that deep –
the DNNs for co-rotation and Neo-Hookean materials only have
two hidden layers, and each of which has 16 neurons. For StVK
material, the DNN has three hidden layers with 16 neurons at
each layer.
The network is optimized using the Adam solver [80]. Dru-
ing the training, the neural network was built using Google
Tensowflow
[81]
and
optimized
with
Google
Cloud
Platform with 8 virtual CPUs. The training error over the
ﬁrst 20 epoches is plotted in Fig. 14. In practice however, we
typically stop at 10 epoches. The total training time is less than
10 minutes on Google Cloud. It takes similar time if one
performs the training on an i7 PC with a high-end video card. The
minibatch size is 1,024 and the learning rate is set as 0.001. Two
hyper-parameters β1 and β2 control the exponential decay rates of
moving averages, which are set as β1 = 0.9 and β2 = 0.999, and
ε = 1e −8. We use the tanh deﬁned as ex −e−x/ex + e−x as the
nonlinear activation function. We found that tanh outperforms the
widely-used ReLU in our experiment. We guess this is because the
input-output relation of the DNN is clearly a smooth nonlinear
function in our case, and ReLU may excel when the input-
output relation contains discontinuity and/or singularity as in many
computer vision problems like image recognition. Also, because
all the training data generated using FEM simulation are clear and
noise-free, and the data coverage is carefully controlled to avoid
over- and under-sampling of the input feature space, we do not
apply dropout during our training.
6
OTHER EXPERIMENTAL RESULTS
The simulator module was implemented using MS Visual C++
2013 on an Alienware desktop PC with an Intel i7 5960
CPU (at 3.0 GHz) and 32 GB memory. It also equips with an
nVidia GTX 970 GPU. We used Eigen C++ template for
most numerical computations. Some of our implementations also
used the published Vega library [82]. DeepWarp utilizes a
standard linear simulation running at background. The external
force applied at each node needs to be rotated back to its rest-shape
orientation as did in stiffness warping [10]. This local rotation is
computed by converting wi into a rotation matrix, which only
induces minor extra computing efforts since wi itself is also the
DNN input. The timing statistics of examples shown in the paper
are reported in Table 1. The source code (for both DNN and
simulator) and executables can be found in the supplementary ﬁle.
The training data (for the Neo-Hookean material) is also available
from an anonymous dropbox link provided in the supplementary
ﬁle.
Comparison with existing geometry warping methods
First
of all, we compare our method with existing geometry warping
methods including modal warping (MW) [11] and rotation-strain
warping (RSW) [67]. We stick with using the rectangular beam
as our training model, and simulate the bending deformation
of a Neo-Hookean toy statue using MW, RSW, DeepWarp and
fullspace FEM simulation. While all the methods demonstrate
plausible nonlinear bending effects, when putting together, one
can see that MW and RSW are actually quite different from the
ground truth result. On the other hand, DeepWarp yields a result
that is hardly distinguishable from the ground truth. Because MW
and RSM use a ﬁxed linear-nonlinear map template (i.e. Eqs (4)
and (5)), they show no difference with different hyperelastic
materials. However, DeepWarp is able to produce high-quality
results for various material models due to its data-driven nature.
Trajectory comparison
Another aspect we would like to in-
vestigate is the motion trajectory, and see how far DeepWarp
deviates from the ground truth along the simulation time. To this


## Page 10


10
rotation-strain warping
modal warping
DeepWarp
ground truth
DeepWarp
rotation-strain warping
modal warping
ground truth
Figure 13. Side-by-side comparison shows a clear advantage of DeepWarp over the existing warping techniques. Its data-driven nature makes the
result almost identical to the ground truth while the simulation is as fast as the linear elasticity. The training still uses the rectangular beam model.
 t
n
e
m
e
c
a
l
p
si
D
e
d
u
ti
n
g
a
m
Time
Neohookean 1/50
Neohookean 1/150
DeepWarp 1/50
DeepWarp 1/150
under damping
Figure 15. The deformable motion trajectory (at the nose tip of the wolf
head) generated using DeepWarp well matches the ground truth under
different time step sizes. The vibration frequency resembles the ground
truth as well. We use the Newmark integrator in this example.
end, we apply DeepWarp to a wolf totem model and plot the
displacement of the node at the nose tip of the wolf head w.r.t.
time. Our reference is the fullspace FEM simulation using the
Newmark integration and the material model is Neo-Hookean.
We compare the resulting trajectories with time step size set as
1/50 sec and 1/150 sec respectively. Surprisingly, the trajectory
generated using DeepWarp is very close to the ground truth in
both time step size settings. The vibration frequency is almost
identical to the ground truth. This is probably because DeepWarp
is essentially a fullspace simulator, where the mass inertial is
lossless unlike in reduced simulations. On the other hand, we
do observe an artiﬁcial under-damping issue as we can see from
the plotted trajectories. It seems that the linear Rayleigh damping
dissipates less energy (∼10% in this example) than the nonlinear
one. However, this issue should be ﬁxed by dynamically adjusting
the Rayleigh damping coefﬁcients as did in [77].
More examples & GPU implementation
With the help of
substructuring method [12], training a single model can be utilized
to handle geometrically complex deformable bodies. In addition
to the example shown in Fig. 1, Fig. 16 shows more results using
DeepWarp. The Armadillo, dinosaur and dragon models are of
StVK, co-rotation and Neo-Hookean materials respectively. The
DNN used is still based on a single rectangular beam model.
DeepWarp is node-wise. Its local correction of each nodal
displacement is independent and can be parallelized trivially on
GPU. We also implemented a shader version of DeepWarp. Deep-
Warp relies an underlying linear solver during the simulation run
time. It is known that the asymptotic time complexity of solving a
pre-factorized matrix is O(N2) while DeepWarp correction is just
O(N). In other words, the beneﬁt of the GPU implementation is
limited in general. It is easy to see that DeepWarp also synergizes
Figure 16. Substructuring allows us to re-use the training data of a
regular shape to handle complex deformable bodies. The Armadillo, di-
nosaur and dragon models use the StVK, co-rotation and Neo-Hookean
materials respectively. They use the DNN trained with the rectangular
beam.
well with model reduction. One can simply use the linear modal
analysis to construct a r-dimensional linear subspace. Because
the model reduction is applied to the linear solver, other more
expensive pre-computations like Cubature training [43] are not
needed. The DNN training for DeepWarp is much faster than
the Cubature training. More importantly, Cubature training is
model-dependant, while DeepWarp training is more general. With
the linear modal reduction, the cost for the diagonalized linear
solver is reduced to O(r), and one should expect more noticeable
accelerations by using the GPU. We do not report extra results
using model reduced DeepWarp since this is a natural extension
and not the primary contribution of this work, nevertheless the
simulation performance of the maple bonsai model shown in Fig. 1
can easily exceed 100 FPS with modal reduction.
When using the GPU-based DeepWarp, some extra cares are
needed for the deformation substructuring. This is because all


## Page 11


11
Model
# Tetrahedra
# Domains
Factorization
Solve
DeepWarp (CPU)
DeepWarp (Shader)
FPS (CPU/GPU)
Beam
2,629
1
6.9ms
< 1ms
1.5ms
< 1ms
333/666
Dragon
51,850
14
307ms
15ms
15ms
< 1ms
16/22
Armadillo
52,278
15
403ms
15ms
18ms
< 1ms
15/21
Dinosaur
54,796
14
334ms
18ms
15ms
< 1ms
18/24
Bunny
24,956
4
273ms
10ms
7ms
< 1ms
33/43
Maple bonsai
255,552
1,771
1,556ms
83ms
109ms
< 1ms
5/10
Table 1
Time performance of the examples reported in the paper. Factorization is the time needed to pre-factorize the system matrix of the linear
elasticity. We use SimplicialLLT solver shipped with Eigen. During the simulation, we only need to solve the system once. FPS reports both
CPU and GPU performance.
the information regarding the ﬁnal nonlinear displacement is in
the GPU memory, which prevents us to evaluate the system and
interface forces for per-domain dynamics at the CPU side. For the
interface force, since it is assumed that the number of nodes on the
domain’s interface is small, we compute a CPU-based DeepWarp
for all the interface nodes to obtain their corrected displacement.
For the system force, we treat an entire domain as a single mass
point and estimate a domain-level rotation to warp it to the local
non-inertial frame. Doing so compromises the physics accuracy,
but avoids expensive data exchange from GPU and CPU.
Figure 17. We can simulate free-ﬂoating deformable bodies by creating
an artiﬁcial boundary condition to constrain the element near the mass
center.
Free-ﬂoating deformable bodies
Free-ﬂoating objects do not
have boundary conditions, and our discriminative features are ill-
deﬁned under this situation. As an easy walk-round, we pick a
tetrahedron that is closest to the mass center of the deformable
body, constrain all of its four nodes and training the DNN based
on it. During the simulation, we couple a rigid body simulator
with the deformable simulation as in [83], where the DeepWarp
is applied within the reference frame attached to the rigid body
simulator (Fig. 17).
7
CONCLUSION
DeepWarp uses a node-wise light-weight DNN to correct a linear
displacement to be a nonlinear one. While it is conceptually
similar to existing geometry warping method like stiffness warp-
ing, modal warping and rotation-strain warping, DeepWarp yields
better simulation results in terms of both shape deformations
and motion trajectories. Observing that simply feeding kinematic
feature into the DNN leads to serious artifacts, we design three dis-
criminative features: geodesic, potential and digression to provide
sufﬁcient contextual information while these features are still quite
general so that a DNN training can be used for deformable bodies
of different shapes. Using the substructuring method, DeepWarp
can simulate large-scale and complex nonlinear deformable ob-
jects efﬁciently without repetitively generating new training poses
and training DNNs for unseen deformable bodies. The training
data alignment also signiﬁcantly reduces the training effort.
Limitation
While it shows some unique advantages over the ex-
isting methods like its efﬁciency, accuracy and re-useable training,
the current version of DeepWarp also has many limitations. First
of all, as a common drawback of learning-based methods, the per-
formance of DeepWarp drops rapidly if an extrapolation is needed.
In other words, if the training set does not cover the feature vectors
that appear in the simulation, DeepWarp may produce unrealistic
deformations. In our current setting, we only consider isotropic
hyperelastic materials. While we believe DeepWarp should be able
to handle more complicated anisotropic materials, doing so may
require a re-design of contextual features and more training efforts
since we cannot align training pairs within a local frame. We
use directional and rotational force ﬁelds as the external forces
in our current training data generation, both of which are low-
frequency forces. As a result, DeepWarp is less accurate when a
high-frequency external force is applied i.e. during the collision
and contact. One may observe popping artifact when the bunny
hits the ﬂoor in Fig. 17. A potential solution may be to use the idea
of condensation [84] by splitting the deformable body according
to its contact regions and rolling DeepWarp back to a regular
nonlinear solver to accurately simulate detailed denting effects, or
to exhaustively sample the high-frequency external forces during
the DNN training.
REFERENCES
[1]
K.-J. Bathe, Finite element method.
Wiley Online Library, 2008.
[2]
J. Schmidhuber, “Deep learning in neural networks: An overview,”
Neural networks, vol. 61, pp. 85–117, 2015.
[3]
J.-T. Huang, J. Li, D. Yu, L. Deng, and Y. Gong, “Cross-language
knowledge transfer using multilingual deep neural network with shared
hidden layers,” in Acoustics, Speech and Signal Processing (ICASSP),
2013 IEEE International Conference on.
IEEE, 2013, pp. 7304–7308.
[4]
G. E. Dahl, D. Yu, L. Deng, and A. Acero, “Context-dependent pre-
trained deep neural networks for large-vocabulary speech recognition,”
IEEE Transactions on audio, speech, and language processing, vol. 20,
no. 1, pp. 30–42, 2012.
[5]
J. Pan, C. Liu, Z. Wang, Y. Hu, and H. Jiang, “Investigation of deep neural
networks (dnn) for large vocabulary continuous speech recognition: Why
dnn surpasses gmms in acoustic modeling,” in Chinese Spoken Language
Processing (ISCSLP), 2012 8th International Symposium on.
IEEE,
2012, pp. 301–305.
[6]
L. Wang, W. Ouyang, X. Wang, and H. Lu, “Visual tracking with
fully convolutional networks,” in Proceedings of the IEEE International
Conference on Computer Vision, 2015, pp. 3119–3127.
[7]
M. Kristan, J. Matas, A. Leonardis, M. Felsberg, L. Cehovin,
G. Fern´andez, T. Vojir, G. Hager, G. Nebehay, and R. Pﬂugfelder, “The
visual object tracking vot2015 challenge results,” in Proceedings of the
IEEE international conference on computer vision workshops, 2015, pp.
1–23.
[8]
K. Hornik, “Approximation capabilities of multilayer feedforward net-
works,” Neural networks, vol. 4, no. 2, pp. 251–257, 1991.
[9]
G. Cybenko, “Approximation by superpositions of a sigmoidal function,”
Mathematics of Control, Signals, and Systems (MCSS), vol. 2, no. 4, pp.
303–314, 1989.


## Page 12


12
[10] M. M¨uller, J. Dorsey, L. McMillan, R. Jagnow, and B. Cutler, “Sta-
ble real-time deformations,” in Proceedings of the 2002 ACM SIG-
GRAPH/Eurographics symposium on Computer animation. ACM, 2002,
pp. 49–54.
[11] M. G. Choi and H.-S. Ko, “Modal warping: Real-time simulation of
large rotational deformation and manipulation,” IEEE Transactions on
Visualization and Computer Graphics, vol. 11, no. 1, pp. 91–101, 2005.
[12] J. Barbiˇc and Y. Zhao, “Real-time large-deformation substructuring,” in
ACM transactions on graphics (TOG), vol. 30, no. 4. ACM, 2011, p. 91.
[13] R. Dechter, Learning while searching in constraint-satisfaction problems.
University of California, Computer Science Department, Cognitive Sys-
tems Laboratory, 1986.
[14] A. Sharif Razavian, H. Azizpour, J. Sullivan, and S. Carlsson, “Cnn fea-
tures off-the-shelf: an astounding baseline for recognition,” in Proceed-
ings of the IEEE conference on computer vision and pattern recognition
workshops, 2014, pp. 806–813.
[15] K. Simonyan and A. Zisserman, “Very deep convolutional networks for
large-scale image recognition,” arXiv preprint arXiv:1409.1556, 2014.
[16] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classiﬁcation
with deep convolutional neural networks,” in Advances in neural infor-
mation processing systems, 2012, pp. 1097–1105.
[17] C. Farabet, C. Couprie, L. Najman, and Y. LeCun, “Learning hierarchical
features for scene labeling,” IEEE transactions on pattern analysis and
machine intelligence, vol. 35, no. 8, pp. 1915–1929, 2013.
[18] A. Karpathy, G. Toderici, S. Shetty, T. Leung, R. Sukthankar, and
L. Fei-Fei, “Large-scale video classiﬁcation with convolutional neural
networks,” in Proceedings of the IEEE conference on Computer Vision
and Pattern Recognition, 2014, pp. 1725–1732.
[19] K. He, X. Zhang, S. Ren, and J. Sun, “Delving deep into rectiﬁers:
Surpassing human-level performance on imagenet classiﬁcation,” in
Proceedings of the IEEE international conference on computer vision,
2015, pp. 1026–1034.
[20] L.-C. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and A. L.
Yuille, “Deeplab: Semantic image segmentation with deep convolu-
tional nets, atrous convolution, and fully connected crfs,” arXiv preprint
arXiv:1606.00915, 2016.
[21] H. Noh, S. Hong, and B. Han, “Learning deconvolution network for
semantic segmentation,” in Proceedings of the IEEE International Con-
ference on Computer Vision, 2015, pp. 1520–1528.
[22] R. Girshick, J. Donahue, T. Darrell, and J. Malik, “Region-based convo-
lutional networks for accurate object detection and segmentation,” IEEE
transactions on pattern analysis and machine intelligence, vol. 38, no. 1,
pp. 142–158, 2016.
[23] O. Russakovsky, J. Deng, H. Su, J. Krause, S. Satheesh, S. Ma, Z. Huang,
A. Karpathy, A. Khosla, M. Bernstein, A. C. Berg, and L. Fei-Fei,
“ImageNet Large Scale Visual Recognition Challenge,” International
Journal of Computer Vision (IJCV), vol. 115, no. 3, pp. 211–252, 2015.
[24] M. A. Otaduy, B. Bickel, D. Bradley, and H. Wang, “Data-driven
simulation methods in computer graphics: cloth, tissue and faces,” in
ACM SIGGRAPH 2012 Courses.
ACM, 2012, p. 12.
[25] H. Wang, F. Hecht, R. Ramamoorthi, and J. F. O’Brien, “Example-
based wrinkle synthesis for clothing animation,” in ACM Transactions
on Graphics (TOG), vol. 29, no. 4.
ACM, 2010, p. 107.
[26] L. Kavan, D. Gerszewski, A. W. Bargteil, and P.-P. Sloan, “Physics-
inspired upsampling for cloth simulation in games,” in ACM Transactions
on Graphics (TOG), vol. 30, no. 4.
ACM, 2011, p. 93.
[27] H. Wang, J. F. O’Brien, and R. Ramamoorthi, “Data-driven elastic
models for cloth: modeling and measurement,” in ACM Transactions on
Graphics (TOG), vol. 30, no. 4.
ACM, 2011, p. 71.
[28] E. Miguel, D. Bradley, B. Thomaszewski, B. Bickel, W. Matusik, M. A.
Otaduy, and S. Marschner, “Data-driven estimation of cloth simulation
models,” in Computer Graphics Forum, vol. 31, no. 2pt2.
Wiley Online
Library, 2012, pp. 519–528.
[29] D. Kim, W. Koh, R. Narain, K. Fatahalian, A. Treuille, and J. F.
O’Brien, “Near-exhaustive precomputation of secondary cloth effects,”
ACM Transactions on Graphics (TOG), vol. 32, no. 4, p. 87, 2013.
[30] W. Xu, N. Umetani, Q. Chao, J. Mao, X. Jin, and X. Tong, “Sensitivity-
optimized rigging for example-based real-time clothing synthesis.” ACM
Trans. Graph., vol. 33, no. 4, pp. 107–1, 2014.
[31] S. Coros, P. Beaudoin, and M. Van de Panne, “Robust task-based control
policies for physics-based characters,” in ACM Transactions on Graphics
(TOG), vol. 28, no. 5.
ACM, 2009, p. 170.
[32] Y. Lee, K. Wampler, G. Bernstein, J. Popovi´c, and Z. Popovi´c, “Motion
ﬁelds for interactive character locomotion,” in ACM Transactions on
Graphics (TOG), vol. 29, no. 6.
ACM, 2010, p. 138.
[33] X. B. Peng, G. Berseth, and M. Van de Panne, “Dynamic terrain traversal
skills using reinforcement learning,” ACM Transactions on Graphics
(TOG), vol. 34, no. 4, p. 80, 2015.
[34] L. Liu, M. V. D. Panne, and K. Yin, “Guided learning of control graphs
for physics-based characters,” ACM Transactions on Graphics (TOG),
vol. 35, no. 3, p. 29, 2016.
[35] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G.
Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski et al.,
“Human-level control through deep reinforcement learning,” Nature, vol.
518, no. 7540, pp. 529–533, 2015.
[36] L. Liu and J. Hodgins, “Learning to schedule control fragments for
physics-based characters using deep q-learning,” ACM Transactions on
Graphics (TOG), vol. 36, no. 3, p. 29, 2017.
[37] X. B. Peng, G. Berseth, K. Yin, and M. Van De Panne, “Deeploco: Dy-
namic locomotion skills using hierarchical deep reinforcement learning,”
ACM Transactions on Graphics (TOG), vol. 36, no. 4, p. 41, 2017.
[38] D. Holden, T. Komura, and J. Saito, “Phase-functioned neural networks
for character control,” ACM Transactions on Graphics (TOG), vol. 36,
no. 4, p. 42, 2017.
[39] B. Wang, L. Wu, K. Yin, U. M. Ascher, L. Liu, and H. Huang,
“Deformation capture and modeling of soft objects.” ACM Trans. Graph.,
vol. 34, no. 4, pp. 94–1, 2015.
[40] H. Xu and J. Barbiˇc, “Example-based damping design,” ACM Trans.
Graph., vol. 36, no. 4, pp. 53:1–53:14, Jul. 2017.
[41] M. Kim, G. Pons-Moll, S. Pujades, S. Bang, J. Kim, M. J. Black, and
S.-H. Lee, “Data-driven physics for human soft tissue animation,” ACM
Transactions on Graphics (TOG), vol. 36, no. 4, p. 54, 2017.
[42] B. Jones, N. Thuerey, T. Shinar, and A. W. Bargteil, “Example-based
plastic deformation of rigid bodies,” ACM Transactions on Graphics
(TOG), vol. 35, no. 4, p. 34, 2016.
[43] S. S. An, T. Kim, and D. L. James, “Optimizing cubature for efﬁcient
integration of subspace deformations,” in ACM transactions on graphics
(TOG), vol. 27, no. 5, 2008, p. 165.
[44] L. Ladick´y, S. Jeong, B. Solenthaler, M. Pollefeys, and M. Gross, “Data-
driven ﬂuid simulations using regression forests,” ACM Trans. Graph.,
vol. 34, no. 6, pp. 199:1–199:9, Oct. 2015.
[45] M. Chu and N. Thuerey, “Data-driven synthesis of smoke ﬂows with
cnn-based feature descriptors,” ACM Trans. Graph., vol. 36, no. 4, pp.
69:1–69:14, Jul. 2017.
[46] D. Terzopoulos, J. Platt, A. Barr, and K. Fleischer, “Elastically de-
formable models,” in ACM Siggraph Computer Graphics, vol. 21, no. 4,
1987, pp. 205–214.
[47] M. M¨uller, B. Heidelberger, M. Teschner, and M. Gross, “Meshless
deformations based on shape matching,” ACM transactions on graphics
(TOG), vol. 24, no. 3, pp. 471–478, 2005.
[48] M. Pauly, R. Keiser, B. Adams, P. Dutr´e, M. Gross, and L. J. Guibas,
“Meshless animation of fracturing solids,” ACM Transactions on Graph-
ics (TOG), vol. 24, no. 3, pp. 957–964, 2005.
[49] S. Martin, P. Kaufmann, M. Botsch, E. Grinspun, and M. Gross, “Uniﬁed
simulation of elastic rods, shells, and solids,” in ACM Transactions on
Graphics (TOG), vol. 29, no. 4, 2010, p. 39.
[50] M. Desbrun, P. Schr¨oder, and A. Barr, “Interactive animation of struc-
tured deformable objects,” in Graphics Interface, vol. 99, no. 5, 1999,
p. 10.
[51] T. Liu, A. W. Bargteil, J. F. O’Brien, and L. Kavan, “Fast simulation of
mass-spring systems,” ACM Transactions on Graphics (TOG), vol. 32,
no. 6, p. 214, 2013.
[52] E. Sifakis and J. Barbiˇc, “Fem simulation of 3d deformable solids: a
practitioner’s guide to theory, discretization and model reduction,” in
ACM SIGGRAPH 2012 Courses, 2012, p. 20.
[53] H. Wang, J. O’Brien, and R. Ramamoorthi, “Multi-resolution isotropic
strain limiting,” in ACM Transactions on Graphics (TOG), vol. 29, no. 6,
2010, p. 156.
[54] G. Irving, J. Teran, and R. Fedkiw, “Invertible ﬁnite elements for robust
simulation of large deformation,” in Proceedings of the 2004 ACM
SIGGRAPH/Eurographics symposium on Computer animation, 2004, pp.
131–140.
[55] F. Hecht, Y. J. Lee, J. R. Shewchuk, and J. F. O’Brien, “Updated sparse
cholesky factors for corotational elastodynamics,” ACM Transactions on
Graphics (TOG), vol. 31, no. 5, p. 123, 2012.
[56] Y. Zhu, E. Sifakis, J. Teran, and A. Brandt, “An efﬁcient multigrid method
for the simulation of high-resolution elastic solids,” ACM Transactions
on Graphics (TOG), vol. 29, no. 2, p. 16, 2010.
[57] S. Bouaziz, S. Martin, T. Liu, L. Kavan, and M. Pauly, “Projective
dynamics: fusing constraint projections for fast simulation,” ACM Trans-
actions on Graphics (TOG), vol. 33, no. 4, p. 154, 2014.


## Page 13


13
[58] R. Narain, M. Overby, and G. E. Brown, “Admm ⊇projective dynamics:
Fast simulation of general constitutive models,” in Proceedings of the
ACM SIGGRAPH/Eurographics Symposium on Computer Animation, ser.
SCA ’16, 2016, pp. 21–28.
[59] H. Wang, “A chebyshev semi-iterative approach for accelerating pro-
jective and position-based dynamics,” ACM Transactions on Graphics
(TOG), vol. 34, no. 6, p. 246, 2015.
[60] H. Wang and Y. Yang, “Descent methods for elastic body simulation on
the gpu,” ACM Transactions on Graphics (TOG), vol. 35, no. 6, p. 212,
2016.
[61] T. Liu, S. Bouaziz, and L. Kavan, “Quasi-newton methods for real-time
simulation of hyperelastic materials,” ACM Transactions on Graphics
(TOG), vol. 36, no. 3, p. 23, 2017.
[62] M. Fratarcangeli, V. Tibaldo, and F. Pellacini, “Vivace: a practical gauss-
seidel method for stable soft body dynamics,” ACM Transactions on
Graphics (TOG), vol. 35, no. 6, p. 214, 2016.
[63] A. Pentland and J. Williams, “Good vibrations: Modal dynamics for
graphics and animation,” in Proceedings of the 16th Annual Conference
on Computer Graphics and Interactive Techniques, ser. SIGGRAPH ’89,
1989, pp. 215–222.
[64] J. Barbiˇc and D. L. James, “Real-time subspace integration for st. venant-
kirchhoff deformable models,” in ACM transactions on graphics (TOG),
vol. 24, no. 3, 2005, pp. 982–990.
[65] Y. Yang, D. Li, W. Xu, Y. Tian, and C. Zheng, “Expediting precom-
putation for reduced deformable simulation,” To appear in ACM TOG,
vol. 34, no. 6, 2015.
[66] T. Kim and D. L. James, “Skipping steps in deformable simulation
with online model reduction,” in ACM transactions on graphics (TOG),
vol. 28, no. 5, 2009, p. 123.
[67] J. Huang, Y. Tong, K. Zhou, H. Bao, and M. Desbrun, “Interactive
shape interpolation through controllable dynamic deformation,” IEEE
Transactions on Visualization and Computer Graphics, vol. 17, no. 7,
pp. 983–992, 2011.
[68] Z. Pan, H. Bao, and J. Huang, “Subspace dynamic simulation using
rotation-strain coordinates,” ACM Transactions on Graphics (TOG),
vol. 34, no. 6, p. 242, 2015.
[69] C. von Tycowicz, C. Schulz, H.-P. Seidel, and K. Hildebrandt, “An
efﬁcient construction of reduced deformable objects,” ACM Transactions
on Graphics (TOG), vol. 32, no. 6, p. 213, 2013.
[70] J. Barbiˇc, F. Sin, and E. Grinspun, “Interactive editing of deformable
simulations,” ACM Transactions on Graphics (TOG), vol. 31, no. 4, p. 70,
2012.
[71] S. Li, J. Huang, F. de Goes, X. Jin, H. Bao, and M. Desbrun, “Space-time
editing of elastic motion through material optimization and reduction,”
ACM Transactions on Graphics (TOG), vol. 33, no. 4, p. 108, 2014.
[72] P. Wolfe, “Convergence conditions for ascent methods,” SIAM review,
vol. 11, no. 2, pp. 226–235, 1969.
[73] H. Xu, W. Yu, S. Gu, and X. Li, “Biharmonic volumetric mapping
using fundamental solutions,” IEEE Transactions on Visualization and
Computer Graphics, vol. 19, no. 5, pp. 787–798, 2013.
[74] X.-M. Fu, Y. Liu, and B. Guo, “Computing locally injective mappings by
advanced mips,” ACM Transactions on Graphics (TOG), vol. 34, no. 4,
p. 71, 2015.
[75] N. Aigerman and Y. Lipman, “Injective and bounded distortion mappings
in 3d,” ACM Transactions on Graphics (TOG), vol. 32, no. 4, p. 106,
2013.
[76] Y. Zhao and J. Barbiˇc, “Interactive authoring of simulation-ready plants,”
ACM Transactions on Graphics (TOG), vol. 32, no. 4, p. 84, 2013.
[77] B. Wang, Y. Zhao, and J. Barbiˇc, “Botanical materials based on biome-
chanics,” ACM Transactions on Graphics (TOG), vol. 36, no. 4, p. 135,
2017.
[78] P.-S. Wang, Y. Liu, Y.-X. Guo, C.-Y. Sun, and X. Tong, “O-cnn: Octree-
based convolutional neural networks for 3d shape analysis,” ACM Trans.
Graph., vol. 36, no. 4, pp. 72:1–72:11, Jul. 2017.
[79] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao, “3d
shapenets: A deep representation for volumetric shapes,” in Proceedings
of the IEEE Conference on Computer Vision and Pattern Recognition,
2015, pp. 1912–1920.
[80] D. Kingma and J. Ba, “Adam: A method for stochastic optimization,”
arXiv preprint arXiv:1412.6980, 2014.
[81] M. Abadi, A. Agarwal, P. Barham, E. Brevdo, Z. Chen, C. Citro, G. S.
Corrado, A. Davis, J. Dean, M. Devin et al., “Tensorﬂow: Large-scale
machine learning on heterogeneous distributed systems,” arXiv preprint
arXiv:1603.04467, 2016.
[82] F. S. Sin, D. Schroeder, and J. Barbiˇc, “Vega: Non-linear fem deformable
object simulator,” in Computer Graphics Forum, vol. 32, no. 1, 2013, pp.
36–48.
[83] D. Terzopoulos and A. Witkin, “Physically based models with rigid and
deformable components,” IEEE Computer Graphics and Applications,
vol. 8, no. 6, pp. 41–51, 1988.
[84] Y. Teng, M. Meyer, T. DeRose, and T. Kim, “Subspace condensation:
Full space adaptivity for subspace deformations,” ACM Transactions on
Graphics (TOG), vol. 34, no. 4, p. 76, 2015.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1803_09109v1_deepwarp_dnn_based_nonlinear_deformation
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1803_09109V1_DEEPWARP_DNN_BASED_NONLINEAR_DEFORMATION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
