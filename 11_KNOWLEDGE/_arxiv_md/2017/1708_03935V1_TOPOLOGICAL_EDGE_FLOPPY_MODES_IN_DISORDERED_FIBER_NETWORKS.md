---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1708.03935v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1708.03935v1_Topological edge floppy modes in disordered fiber networks

> Source: 1708.03935v1_Topological edge floppy modes in disordered fiber networks.pdf

> Pages: 11

---


## Page 1


Topological edge ﬂoppy modes in disordered ﬁber networks
Di Zhou,1 Leyou Zhang,1 and Xiaoming Mao1
1Department of Physics, University of Michigan, Ann Arbor, MI 48109-1040, USA
Disordered ﬁber networks are ubiquitous in a broad range of natural (e.g., cytoskeleton) and
manmade (e.g., aerogels) materials. In this paper, we discuss the emergence of topological ﬂoppy
edge modes in these ﬁber networks as a result of deformation or active driving. It is known that a
network of straight ﬁbers exhibits bulk ﬂoppy modes which only bend the ﬁbers without stretching
them. We ﬁnd that, interestingly, with a perturbation in geometry, these bulk modes evolve into
edge modes. We introduce a topological index for these edge modes and discuss their implications
in biology.
Introduction – Recent theoretical advances in applying
concepts of topological states of matter to mechanical
systems has led to the burgeoning new ﬁeld of “topologi-
cal mechanics”, where nontrivial topologies of the phonon
bands give rise to exotic mechanical and acoustic prop-
erties [1–20].
Among many diﬀerent types of topological mechani-
cal systems, a particularly interesting class consists of
“Maxwell lattices”, which are central-force lattices with
average coordination number ⟨z⟩= 2d where d is the spa-
tial dimension, and are thus at the verge of mechanical in-
stability [2, 3, 16–20]. Maxwell lattices host topologically
protected phonon edge modes at zero frequency (ﬂoppy
modes). These edge modes are governed by the topology
of the equilibrium and compatibility matrices of the lat-
tice in the ﬁrst Brillouin zone, which in turn, are governed
by the lattice geometry [2]. A simple two-dimensional ex-
ample of Maxwell lattice, the deformed kagome lattice, as
shown in Fig. 1, exhibit diﬀerent phases where the topo-
logical structure changes and the ﬂoppy modes localize
at diﬀerent edges [17].
In particular, what drives the
topological transition here is a soft strain that changes
the lattice geometry, where all bonds remain the same
length and only the bond angles alter. At the topologi-
cal transition, bonds form straight lines and ﬂoppy modes
penetrate inﬁnitely deep into the bulk, whereas in the two
phases below and above the transition, the ﬂoppy modes
localize at diﬀerent edges. In the topologically nontrivial
phase all ﬂoppy modes localize on the top edge leaving
the bottom edge rigid. This physics of the Maxwell lat-
tices make them both an interesting topic for theoretical
study [21–27] and good candidates for the design of novel
mechanical metamaterials where the edges can change
stiﬀness by orders of magnitude reversibly [17].
Most existing studies of topological mechanics are
based on periodic lattices, with only few exceptions [28,
29]. In general, topological order is robust against dis-
order, because topological attributes are integer valued
and remain invariant upon the addition of disorder until
they jump to a diﬀerent integer value. This robustness
has been demonstrated in various periodic lattice systems
with weak disorder. It is thus an intriguing question to
ask: can topological edge ﬂoppy modes exist in disor-
dered systems that are completely oﬀ-lattice?
In this paper, we study ﬂoppy edge modes in disor-
dered ﬁber networks which are not periodic in space
(Fig. 1b-d).
Fiber networks are ubiquitous in nature,
taking the form of cell cytoskeleton and extra-cellular ma-
trix, and in manmade materials, taking the form of ﬁber
hydrogels and aerogels, felt, etc., and exhibit fascinat-
ing physics [30–41]. Using both analytic theory and nu-
merical simulation, we show that topological ﬂoppy edge
modes exist in these disordered ﬁber networks, and their
existence lead to strongly asymmetric mechanical prop-
erties at opposite ends of the ﬁber network. These topo-
logical edge modes may have interesting consequences in
a wide range of problems, such as cell cytoskeleton under
active driving and the design of smart ﬁber materials.
Model and Results – We choose the “Mikado model”,
which is a completely oﬀlattice ﬁber network model [30,
31], and modify it for our study of topological edge
modes.
The original Mikado model consist of straight
ﬁbers randomly placed on a two-dimensional plane, with
all crossing points being free hinges (Fig. 1b). The Hamil-
tonian of a Mikado model can be written as
H =
Nfiber
X
i=1
ni−1
X
m=1
ki,m
2

|⃗Ri,m −⃗Ri,m+1| −ℓi,m
2
+
Nfiber
X
i=1
ni−1
X
m=2
κi,m
2
(∆θi,m)2 ,
(1)
where there are Nﬁber ﬁbers labeled by i, each has ni
crosslinks labeled by m, and ⃗Ri,m is the (displaced) po-
sition of the m-th crosslink on the i-th ﬁber. The ﬁrst
term denotes central force stretching energy of each ﬁber
segment (bond) between neighboring crosslinks (sites)
m, m + 1 along each ﬁber i, with stretching spring con-
stant ki,m and rest length ℓi,m. The second term denotes
bending energy of the ﬁber and ∆θi,m = θi,m −θi,m−1
is the angle change between the two segments meeting
at crosslink m along ﬁber i (here θi,m denotes the orien-
tation of the m-th segment on ﬁber i, and ∆θi,m = 0 if
ﬁber i is straight) with bending spring constant κi,m.
In typical ﬁber networks composed of long slender ﬁla-
ments, the bending stiﬀness is much smaller compared to
the stretching stiﬀness [κ/(kℓ2
0) ≪1 where ℓ0 is the char-
arXiv:1708.03935v1  [cond-mat.soft]  13 Aug 2017


## Page 2


2
acteristic mesh size, see discussion in the Supplementary
Information (SI)]. For our discussion of the topological
mechanics we ﬁrst ignore bending stiﬀness and treat all
ﬁber segments as central-force springs (κi,m = 0). Later
we use numerical simulations to verify that the essential
conclusion of the asymmetric mechanical properties due
to topological edge modes still holds in presence of small
bending stiﬀness.
The original Mikado network display an interesting
property:
all ﬂoppy modes (i.e., modes that do not
stretch or compress any bonds) are bulk modes.
This
can be seen by ﬁrst apply Maxwell counting to a
Mikado network.
The total number of crosslinks is
Ns = PNfiber
i=1
ni/2 (remember each crosslink is shared
by two ﬁbers) and the total number of bonds is Nc =
PNfiber
i=1
(ni −1) (dangling ends are removed since they
don’t contribute to mechanical stability). The number
of zero modes is thus equal to the number of ﬁbers
N0 = Nsd −Nc = Nﬁber.
A straightforward decom-
position of the Nﬁber zero modes is that each ﬁber car-
ries one zero mode corresponding to the longitudinal dis-
placement of that ﬁber, while keeping all other ﬁbers
intact (the ﬁber segments crossing the displaced ﬁber is
stretched only to second order of the mode), as shown in
Fig. 1d [34]. It is worth pointing out that these modes
are independent but not orthogonal to one another, and
they contain the rigid translations and rotation of the
whole network.
The original Mikado network can be seen as a disor-
dered analog of the critical state of the deformed kagome
lattice that lies between the topologically trivial and non-
trivial phase, in the sense that they both have straight
ﬁlaments which carry bulk ﬂoppy modes (Fig. 1a and b).
The deformed kagome lattice exhibit states (related by a
soft strain from the critical state) with diﬀerent topolo-
gies where the ﬂoppy modes localize at diﬀerent edges.
Can the Mikado network also exhibit such topological
transitions? The answer is yes.
Because what drives the topological transition and
the localization of the ﬂoppy modes in the deformed
kagome lattice is the change of lattice geometry (in this
case induced by the soft strain equivalent to the ⃗q = 0
bulk ﬂoppy mode), it is natural to consider following
bulk ﬂoppy modes the original Mikado model and ex-
amine their eﬀect on mode localization.
As shown in
Fig. 1c, we perturb the Mikado model to create a new
ground state as follows:
one arbitrarily chosen “cen-
tral ﬁber”, c, is longitudinally displaced by a small
amount U (0)
c
(each crosslink on this ﬁber displace by
⃗u(0)
c,m = U (0)
c
( sin(θc+Θc,m)
sin Θc,m
, −cos(θc+Θc,m)
sin Θc,m
) where θc is the
angle of the central ﬁber, and Θc,m is the intersecting
angle between the crossing ﬁber at crosslink m and the
central ﬁber) following one ﬂoppy mode of the original
Mikado model.
We choose the convention that if the
ﬁber is pulled in the direction pointing from crosslink 1
FIG. 1. (a) A deformed kagome lattice in its critical state
(middle, large) between two phases with diﬀerent topologies
in their phonon bands (left and right, small). These states
are related by a soft strain of the lattice that only change
the bond angles. Blue and red arrows show a pair of ﬂoppy
modes, under periodic boundary condition in the horizontal
(x) direction and open boundary condition in the y direction.
The pair of ﬂoppy modes are on the top and bottom edges
respectively in the topologically trivial phase (left). The red
mode becomes a bulk mode at the transition (middle, where
the cyan stripes show the straight lines of bonds) and shift to
the top edge in the topological phase (right). (b) An example
original Mikado network, showing one bulk ﬂoppy mode along
ﬁber i (red arrows). This ﬂoppy mode is characterized by a
constant longitudinal projection of displacements along the
ﬁber Ui (green arrows), and the displacement vectors of the
crosslinkes ⃗ui,m (red arrows) are perpendicular to the cross-
ing ﬁber so they are only stretched to second order. Dangling
ends are shown as dashed lines and are ignored in the analy-
sis. (c) Example original Mikado network, showing the bulk
ﬂoppy mode on the central ﬁber which is used to obtain the
modiﬁed Mikado model (red and green arrows showing ⃗u(0)
c,m
and U (0)
c
respectively, magniﬁed by 50 times). The zoomed
in ﬁgure below shows details of the displacements (⃗u(0)
c,m mag-
niﬁed by 10 times) of the central ﬁber in a local area [boxed
in (a)] that leads to the modiﬁed Mikado model. (d) Floppy
mode localized on the tail of the central ﬁber in the modiﬁed
Mikado model (⃗u(0)
c,m too small to be visible). (e) Projection
of the ﬂoppy mode to each segment Uc,m [green arrows in (d)]
exponentially decrease from tail (m = 1) to head (m = nc)
on the central ﬁber.
to nc on the central ﬁber (so crosslink nc is the “head”
of motion), U (0)
c
> 0, and vice versa, and we ignore the
resulting stress (which is second order in U (0)
c
). This ge-
ometric perturbation leads us to a new model which we
name “modiﬁed Mikado model”.


## Page 3


3
FIG. 2. (a) Illustration of the transfer matrix [Eq. (3)] ap-
plying on a crosslink. (b) Displacements propagation (along
arrows) and order of magnitude when applying the transfer
matrix on the network with boundary condition that only
crosslink 1 of the central ﬁber has input U (large blue arrows
for O(1), smaller arrows for higher order in ∆and red denotes
ﬂow back to the central ﬁber). (c) Asymmetric edge stiﬀness
at two ends of the central ﬁber. We perform numerical sim-
ulations to measure local stiﬀness klocal against point force
on two ends of the central ﬁber, in modiﬁed Mikado models
with diﬀerent U (0). We show results for both networks with
no bending stiﬀness κ = 0 and with bending stiﬀness (con-
trolled by ﬁber thickness a in unit of characteristic mesh size
ℓ0, and we normalize klocal using characteristic spring con-
stant of one segment ˜k). For more details see the SI. In all
cases, the head is signiﬁcantly more stiﬀthan the tail. (d)
Mikado network under active driving from active crosslinks
(marked with arrows) on the central ﬁber. The direction of
driving is determined by the chirality of the crossing ﬁbers,
such that the motors actively move to the “+” end. If all
crossing ﬁbers have correlated chirality such that their “+”
ends are on the left, from Eq. (15), we ﬁnd that the ﬂoppy
mode on the central ﬁber exponentially localizes to the left.
We then study mechanical properties of the modiﬁed
Mikado model using both analytical and numerical calcu-
lations. We ﬁnd that the “tail” of the central ﬁber (i.e.,
the opposite end to the direction of pulling) host an ex-
ponentially localized ﬂoppy mode in the modiﬁed Mikado
model (Fig. 1de). As a result, the local stiﬀness against
a point force is signiﬁcantly smaller at the tail compared
to that at the head of the central ﬁber (Fig. 2c, more
details in the SI).
The analytic method we adopt to study the modiﬁed
Mikado network is based on a transfer matrix that prop-
agate ﬂoppy modes through crosslinks in the network.
When the ﬁber is not straight, instead of a constant lon-
gitudinal displacement for the ﬂoppy modes in the orig-
inal Mikado model, the ﬂoppy-modes longitudinal dis-
placement is diﬀerent from segment to segment along a
ﬁber in the modiﬁed Mikado model. Thus, a ﬂoppy mode
can be characterized either by the displacement of each
crosslink, {⃗ui,m}, or the longitudinal projection of the
displacements on each ﬁber segment {Ui,m = ⃗ui,m·ˆni,m =
⃗ui,m+1 · ˆni,m}, where ˆni,m is the unit vector along the m-
th segment (between site m and m + 1) on ﬁber i. As
shown in Fig. 2a, the two representations are related by
four equations, Ui,m−1 = ⃗ui,m·ˆni,m−1, Ui,m = ⃗ui,m·ˆni,m,
Uj,n−1 = ⃗ui,m · ˆnj,n−1, and Uj,n = ⃗ui,m · ˆnj,n (assuming
the crosslink under consideration is both m-th on ﬁber i
and n-th on ﬁber j). Eliminating ⃗ui,m we get
M
 Ui,m−1
Uj,n−1

=
 Ui,m
Uj,n

(2)
with the transfer matrix
M =
 sin(Θi,m−∆θi,m)
sin Θi,m
sin ∆θi,m
sin Θi,m
−sin ∆θj,n
sin Θi,m
sin(Θi,m+∆θj,n)
sin Θi,m
!
(3)
where Θi,m ≡θj,n−1−θi,m−1, ∆θi,m = θi,m−θi,m−1, and
∆θj,n = θj,n −θj,n−1. This equation serves as a “transfer
matrix” for segment displacements at crosslinks for an ar-
bitrary ﬂoppy mode in the modiﬁed Mikado model. For
any input of boundary condition in terms of segment dis-
placements on one end of each ﬁber (remember the total
number of zero mode is equal to the number of ﬁbers), we
can calculate the ﬂoppy mode displacements throughout
the whole network.
With this transfer matrix, we can study general ﬂoppy
modes in the modiﬁed Mikado model.
We are partic-
ularly interested in what happens to the ﬂoppy mode
that was a bulk mode on the central ﬁber in the original
Mikado model (Fig. 1bc). To do this, we take the bound-
ary condition that the ﬁrst segment of every ﬁber is given
to be Ui,1 = 0 if i ̸= c and Ui,1 = U if i = c, i.e., only
the central ﬁber has a displacement input along segment
1 (which can be either the head or the tail of the central
ﬁber depending on the pulling that deﬁnes the modiﬁed
Mikado network ground state), while all other ﬁbers are
hold ﬁxed at their segment 1. We then use the transfer
matrix [Eq. (2)] to calculate the ﬂoppy displacement on
the rest of the network. Figure 1c show an example of
such exact calculation, where the resulting ﬂoppy mode
is no longer a bulk mode but instead localizes at the tail
of the central ﬁber.
To characterize such ﬂoppy mode localization we take
the following perturbative expansion. Because ﬁbers in
the modiﬁed Mikado model are close to straight (U (0)
c
is
small), all ∆θi,m are small, which permits a perturbative
expansion of the transfer matrix at small bending angles
(represented generally by ∆) and allows further analysis.
Following the central ﬁber, we ﬁnd that at each crosslink
(for more details see the SI),
Uc,m = [1 −∆θc,m cot Θc,m + O(∆θ2
c,m)]Uc,m−1 (4)
where Θc,m is the angle between the central ﬁber and
the crossing ﬁber at crosslink m, and we have used the
fact that the input Uj,n−1 from the ﬁber which crosses
the central ﬁber is either 0 (from boundary condition), or


## Page 4


4
of O(∆2) or higher (from other crosslinks on the central
ﬁber itself through a loop), as shown in Fig. 2b. Such
higher order displacements are visible in Fig. 1c where
we used the full transfer matrix [Eq. (3)]. Note that this
small ∆expansion also requires that the crossing angles
Θc,m are not too small (so cot Θc,m does not diverge), a
condition naturally satisﬁed in most ﬁber networks from
excluded volume repulsion.
Equation (15) governs the growth and decay of the
ﬂoppy mode along the central ﬁber.
If cot Θ > 0, we
have Uc,m > (<)Uc,m−1 if ∆θi,m < (>)0 [corresponding
to the central ﬁber bending up (down) at this crosslink],
and vice versa (see SI for examples of the geometry). This
is a very general geometric rule for edge ﬂoppy modes,
which applies to the case of topological kagome lattices
as well (e.g., following the two families of vertical lines up
in Fig. 1c one ﬁnds that U increase on both). This rule
can also be used to design new ordered or disordered
structures which exhibit tailored distribution of ﬂoppy
modes (see example in SI).
Now with the general rule of ﬂoppy mode evolution at
each crosslink, we come back to the question of where
the ﬂoppy mode localizes in the modiﬁed Mikado model.
It is straightforward to see that individually at each
crosslink (holding all other crosslinks ﬁxed) the displace-
ment U (0)
c,m points to the direction of ﬂoppy mode Uc,m
decrease along the central ﬁber if U (0)
c
> 0 (central ﬁber
pulled towards crosslink nc), and vice versa. However,
we need to rigorously prove that in the modiﬁed Mikado
model where all crosslinks are displaced along the central
ﬁber at the same time, the disorder averaged (denoted by
⟨. . .⟩) growth rate of the ﬂoppy mode
⟨λ⟩≡1 −
Uc,m+1
Uc,m

(5)
is positive when U (0)
c
> 0 and negative when U (0)
c
< 0
(ﬂoppy mode localizes on tail), given the condition that
diﬀerent ﬁbers have uncorrelated orientations. The proof
is included in the SI.
The analytic theory discussed above is at zero bend-
ing stiﬀness, but our numerical results show that when
bending stiﬀness is introduced, the asymmetric stiﬀness
is still signiﬁcant (Fig. 2c).
The ﬂoppy edge modes we ﬁnd in these disordered ﬁber
networks are of the same geometric origin as topologi-
cal edge ﬂoppy modes in periodic lattices. In discussions
above we constructed a real space transfer matrix method
that shows the exponential localization of ﬂoppy modes
on individual ﬁbers. Next we show that a topological in-
variant, a generalization of the “topological polarization”
deﬁned in Ref. [2] to disordered networks, can be deﬁned
on the central ﬁber that dictates its edge ﬂoppy mode. In
order to do this we start by introducing the compatibility
matrix Cβm which maps site displacements (projected to
bond m) Uc,m onto bond extension δlc,β
δlc,β =
nc
X
m=1
CβmUc,m.
(6)
The form of Cβm is determined by the transfer matrix, as
detailed in the SI. We then rewrite this equation in mo-
mentum space, where the compatibility matrix takes the
form ˜C(q1, q2). Note that it depends on two momenta as
a result of disorder (absence of translational invariance)
instead of one in the periodic lattice case. Existence of
ﬂoppy modes is determined by the equation det ˜C = 0
which generally has no solution under periodic bound-
ary condition. Edge ﬂoppy modes under open boundary
condition is captured by introducing an extra complex
component to the momenta, k = k′ + ik′′. The sign of
k′′, which governs which end of the ﬁber the ﬂoppy mode
localizes to, is determined by a topological invariant, the
winding number
Nc = 1
nc
1
2πi
I 2π
0
dk d
dk Im ln det ˜C(q1 + k, q2 + k),
(7)
such that Nc = 0, 1 correspond to ﬂoppy mode on the
right and left respectively. The actual solution k′′ is di-
rectly related to the decay rate λ on the ﬁber. An ex-
panded discussion of Nc is in the SI.
Discussions – In this paper we show that in disordered
ﬁber networks, when individual ﬁbers are pulled, a topo-
logical edge ﬂoppy mode localizes on the tail of the ﬁber.
In this section we generalize this conclusion and discuss
possible application to experimental systems.
First, the scenario of pulling a ﬁber in a network oc-
curs broadly in various situations. For example, in cell-
cell and cell-extracellular matrix interactions, actin ﬁla-
ments can exert active pulling on the network, leading
to the geometry of ﬁbers being pulled following the net-
work ﬂoppy modes, and thus asymmetric stiﬀness arises,
as we discuss above. The eﬀect that the site of pulling
(head) becomes stiﬀand the opposite end of the ﬁber
(tail) becomes soft, may have interesting consequences
in cell mechanics.
Although the above discussion spe-
cialize to the case of one single ﬁber being pulled, in the
SI, we include numerical results for networks in which
multiple ﬁbers are pulled simultaneously, where we show
edge ﬂoppy modes on each pulled ﬁber. Moreover, in the
modiﬁed Mikado network we ignored the (higher order)
stress generated in the ground state. Adding back these
residual stresses only shifts the equilibrium position of
the head and the tail of the ﬁbers, and the asymmetric
stiﬀness we discuss here remains true (see SI for more
discussion).
Second, although our discussion is based on the simple
geometric perturbation that one central ﬁber is pulled,
the transfer matrix method we develop actually applies
to more general situation of geometric perturbation of the
ﬁber network, because the exponential increase/decrease


## Page 5


5
of the ﬂoppy mode only depend on the relation between
the crossing ﬁber orientation and the direction of the
bending of the central ﬁber. This type of change of ge-
ometry in ﬁber networks can occur in a rich variety of
systems. For example, in a network where some or all of
the crosslinks are active motors which walk on particular
directions on the ﬁbers [42–44], such coherent change in
geometry can also happen. As shown in Fig. 2d, where
a central ﬁber is crosslinked to other ﬁbers via active
motors, and the chirality of the crossing ﬁbers are cor-
related, a topological edge ﬂoppy modes emerge on the
central ﬁber due to the active driving.
Acknowledgments – This work was supported by the
National Science Foundation Grant No.
NSF DMR-
1609051.
Appendix I: Small angle approximation and the
disorder averaged decay rate of the edge ﬂoppy
mode
In this SI section we start from the ﬂoppy mode trans-
fer matrix, Eq.(3) in the main text, discuss its approx-
imations at small U (0)
c
, and the resulting decay rate of
the ﬂoppy mode.
For small U (0)
c
the new ground state is very close to
the original Mikado model with straight ﬁbers. The only
diﬀerences are the small bending angles when the central
ﬁber meets the crossing ﬁbers. When the transfer matrix
is applied on these crosslinks, one can expand to ﬁrst
order in the small bending angles (generally denoted as
∆), which is equivalent to ﬁrst order in U (0)
c
, and ﬁnd
M =
 1 −∆θi,m cot Θi,m
∆θi,m csc Θi,m
−∆θj,n csc Θi,m
1 + ∆θj,n cot Θi,m

. (8)
We then use this asymptotic transfer matrix to study the
evolution of the ﬂoppy mode along the central ﬁber, with
the boundary condition described in the main text, that
a displacement U is input on site 1 on the central ﬁber
while site 1 on all other ﬁbers are ﬁxed. It is easy to
see that to O(∆), the ﬂoppy mode along the central ﬁber
evolve as
Uc,m = (1 −∆θc,m cot Θc,m)Uc,m−1
(9)
which is Eq. (4) in the main text.
Next we discuss the disorder average of the mode
growth/decay.
As discussed in the main text, when
the pulling aﬀect each crosslink m individually (take all
other ⃗uc,n̸=m = ⃗ui,n = 0), the factor 1 −∆θ cot Θc,m
has the sign such that the mode decays (grows) when
U (0)
c
> 0(< 0), corresponding to ﬂoppy mode localizing
at the tail of the pulled central ﬁber. Here we discuss
the full expression for the disorder averaged decay rate
(where all crosslinks displace at the same time)
λ ≡1 −
Uc,m+1
Uc,m

(10)
where ⟨·⟩denote disorder average. Using the fact that
the modiﬁed Mikado model ground state is obtained from
pulling the central ﬁber from the original Mikado model,
we have (from equation of ⃗u(0)
c,m in main text)
∆θc,m = U (0)
c
ℓc,m
(cot Θc,m −cot Θc,m+1) −
U (0)
c
ℓc,m−1
(cot Θc,m−1 −cot Θc,m) ,
(11)
to leading order in U (0)
c
, where ℓc,m is the length of the segment m on the central ﬁber. Plug this into the mode
evolution [Eq. (9)], we have the decay rate
λ =
*hU (0)
c
ℓc,m
(cot Θc,m −cot Θc,m+1) −
U (0)
c
ℓc,m−1
(cot Θc,m−1 −cot Θc,m)
i
cot Θc,m
+
.
(12)
Using the fact that the ﬁbers are randomly placed on the 2D plane with no correlation between diﬀerent ﬁbers, we
have that lc,m and Θc,m are independent random variables, thus
λ = U (0)
c
¯ℓ

−cot Θc,m+1 cot Θc,m −cot Θc,m−1 cot Θc,m + 2 cot Θ2
c,m

,
(13)
where ¯ℓis the average mesh size. Further, because Θc,m+1 and Θc,m are also independent variables, and ⟨cot Θc,m⟩= 0,
we have
λ = 2U (0)
c
¯ℓ
⟨cot Θ2
c,m⟩.
(14)
Therefore λ has the same sign as U (0)
c
, showing that the ﬂoppy mode always localize on the tail of the pulled central
ﬁber.


## Page 6


6
It is worth noting that ⟨cot Θ2
c,m⟩is actually divergent, which is an artifact of our small angle approximation. When
the two crossing ﬁbers are too close to parallel (Θc,m →0 or π), we have sin Θc,m →0 and the crosslink displacement
diverges, making the small angle ∆θc,m approximation invalid. In reality such near-parallel crossings are naturally
avoided by excluded volume interactions between the ﬁbers so the divergence is regularized.
Appendix II: Crosslink geometry for ﬂoppy mode
decay or growth
In this SI section we illustrate geometries that give rise
to growth or decay of the ﬂoppy mode (FM) as well as
using this principle to design new structures that exhibit
edge ﬂoppy modes.
In Fig. 3 we show various crosslink geometries, for dif-
ferent choices of crossing angle (from central ﬁber to the
crossing ﬁber) Θi,m and bending angle of the central ﬁber
at this crosslink ∆θi,m. Because from Eq. (4) in the main
text, that
Uc,m = (1 −∆θc,m cot Θc,m + O(∆θ2
c,m))Uc,m−1.(15)
The growth or decay of the ﬂoppy mode is simply con-
trolled by the combination ∆θc,m cot Θc,m. Thus we have
4 diﬀerent cases as shown in Fig. 3.
FIG. 3. 4 diﬀerent geometries of the crosslink and their re-
sulting ﬂoppy mode evolution. Fiber i is the horizontal one
and j is the vertical one. Note that whether the crossing ﬁber
bends or not is irrelevant for the ﬂoppy mode on the ﬁber i.
FIG. 4. A structure where crossing ﬁbers (vertical ones) of
alternating Θc,m are arranged, such that all horizontal ﬁbers
exhibit ﬂoppy edge modes localized on their left.
Using this principle we can design new ordered or dis-
ordered structures that exhibit ﬂoppy modes on chosen
edges. Fig. 4 show one such example.
Appendix III: Topological index of the ﬂoppy mode
in the modiﬁed Mikado model
The robustness of the ﬂoppy mode localization at the
tail of the central ﬁber in the modiﬁed Mikado model
calls for a deﬁnition of a topological index. In this SI
section we deﬁne this topological index, which extends
the “topological polarization” concept from Ref. [2] to
disordered ﬁber networks.
We start by introducing the compatibility matrix Cβm
that maps the displacement longitudinal projection Uc,m
to the bond extension δlc,β,
δlc,β =
nc
X
m=1
CβmUc,m
(16)
Using the ﬂoppy mode we derived in the main text and
in the SI Sec. (in small angle approximation), we have
Cβm = (1 −∆θc,m cot Θc,m)−1δβ+1,m −δβ,m. (17)
With open boundary condition (OBC) on both ends of
the central ﬁber, Cβm is a (nc−1)×nc matrix which maps
the nc-dimensional Uc space to the nc−1-dimensional δlc
space. Thus its null space at least contains one ﬂoppy
mode on the central ﬁber. In the rest of this section, for
simplicity we deﬁne cm ≡(1 −∆θc,m cot Θc,m)−1.
Similar to the discussion of in the periodic lattices, we
rewrite Eq. (16) in a “quasi” momentum space, where
although no periodic lattice structure exist, we Fourier
transform based on the crosslink labels along the central
ﬁber. The Fourier transform and its inverse are deﬁned
as
˜Uc(q) =
nc
X
m=1
Uc,me−iqm,
Uc,m = 1
nc
nc
X
j=1
˜Uc(q)eiqm,
(18)
where q = 2πj/nc with j being integers from 1 to nc. In
deﬁning this Fourier transform we have assumed periodic
boundary conditions (PBC), where the (nc + 1)th site is
the 1st site, and energy term between them is determined
by Θc,1. In this quasi-momentum space, Eq. (16) takes
the form
δ˜lc(q1) = 1
nc
X
q2
˜C(q1, q2) ˜Uc(q2).
(19)


## Page 7


7
It is worth noting that, unlike periodic lattices, where the
Fourier transform of the compatibility matrix reduces to
δ(q1 −q2) ˜C(q1) out of translational invariance, here the
compatibility matrix still depends on both momenta.
Nevertheless, ﬂoppy modes still correspond to null
space of ˜C(q1, q2) in momentum space. In order to have
ﬂoppy modes, the condition
det ˜C = 0
(20)
has to be met (where the determinant is taken in the
q1, q2 space). In particular, from Eq. (17) we have
˜C(q1, q2) = ˜c(q1 −q2)eiq1 −ncδj1,j2
(21)
where q1 = 2πj1/nc, q2 = 2πj2/nc,
˜cq =
nc
X
m=1
e−imqcm
(22)
is the Fourier transform of cm ≡(1 −∆θc,m cot Θc,m)−1.
Similar to the periodic lattices, in general the condi-
tion (20) is not satisﬁed if q1, q2 are real numbers (no
ﬂoppy modes on a ring). However, if we introduce an
imaginary part to the momentum, so that q →q + k
where k = k′ + ik′′ is a complex variable, the equa-
tion det ˜C = 0 can be solved.
The physical mean-
ing of introducing k is that instead of requiring PBC
Uc,m+nc = Uc,m, now
Uc,m+nc = Uc,me(ik′−k′′)nc
(23)
so we eﬀectively “decouple” the the two ends of chain.
Instead of being a “ring” under PBC, it is now a “spiral”
with the pitch determined by k. With ˜C(q1 +k, q2 +k) =
˜c(q1−q2)ei(q1+k)−ncδj1,j2 we ﬁnd that det ˜C = 0 reduces
to
1 −eiknc
nc
Y
m=1
cm = 0,
(24)
leading to the solution
k′ = 0,
k′′ = 1
nc
log
 nc
Y
m=1
cm
!
.
(25)
This agrees with the total decay of the ﬂoppy mode on
the ﬁber obtained in real space, that
Uc,nc/Uc,1 =
nc
Y
m=2
c−1
m .
(26)
Whether the ﬂoppy mode is localized on the left or
the right end of the ﬁber is captured by the sign of k′′,
which is determined by whether the product Qnc
m=2 cm is
less than or greater than 1. Following the construction
of the topological polarization in the regular lattices, this
is related to the winding number of the phase of det ˜C
when k goes around the ﬁrst Brillouin zone k = 0 →2π,
Nc = 1
nc
1
2πi
I 2π
0
dk d
dk Im ln det ˜C(q1 + k, q2 + k), (27)
where the factor of 1/nc comes from the fact that the
equation (24) is actually nc degenerate from the nc × nc
matrix determinant.
This winding number counts the
solution of k inside the unit circle, corresponding to k′′ <
0, which is a ﬂoppy mode on the right boundary. Thus,
when Nc = 0 the ﬂoppy mode is localized on the left, and
when Nc = 1 the ﬂoppy mode is localized on the right.
Finally we need to comment on the physical meaning
of the topological invariant Nc in the disordered ﬁber net-
work model. The whole formulation from compatibility
matrix to the deﬁnition of the topological invariant Nc is
rather general: we assume that the decay of the ﬂoppy
mode from site m −1 to m is controlled by the series
{cm},
Uc,m = c−1
m Uc,m−1.
(28)
When the ground state is generated by pulling the central
ﬁber, as described in the main text, cm is determined by
cm ≡(1 −∆θc,m cot Θc,m)−1.
The deﬁnition of the compatibility matrix and the
topological invariant is independent of the actual form
of cm. As long as we can write down Eq. (16), all discus-
sions in this section follows. Thus, it may seems surpris-
ing that for any disordered ﬁber network, as long as the
spectrum is gapped on the central ﬁber (meaning that
det ˜C has no solution under PBC), the topological in-
variant Nc can always be deﬁned. We have to point out
that although this is true (that one always get Nc = 0
or 1), it doesn’t automatically mean a well deﬁned local-
ized mode. The physical meaning of Nc in this discussion
is simply the sign of k′′ that characterizes the ratio be-
tween Uc,nc and Uc,1. It doesn’t guarantee a coherently
decaying or growing ﬂoppy mode through the ﬁber. The
rigorous “exponential localization” of the mode requires
that cm consistently > 1 or < 1 on most sites.
This
impose additional requirements on the details of the dis-
order.
The example of modiﬁed Mikado model, as we
discuss in the main text, is indeed characterized by co-
herent growth/decay along the central ﬁber, because it
has the special geometry of being generated by pulling
this ﬁber along the ﬂoppy mode of the straight state. In
the main text we discuss another case, where crosslinks
are active and the correlation of the ﬁber polarizations
guarantee the exponential localization. This type of con-
dition is usually not satisﬁed on a ﬁber network with
generic disorder. Thus, in order to have exponentially
localized edge ﬂoppy mode, we need to show that the
decay rate as deﬁned in Eq. (10) has consistent signs
throughout the chain.


## Page 8


8
Appendix IV: Numerical simulation of the modiﬁed
Mikado model and the addition of bending stiﬀness
In this section we discuss how we numerically simulate
the modiﬁed Mikado model, to characterize (i) ﬂoppy
modes localized on the tail of the central ﬁber, and (ii)
asymmetric edge stiﬀness, in presence of bending stiﬀ-
ness, as a result of the edge ﬂoppy mode.
A. Simulation protocol and calculating the edge
ﬂoppy mode
We ﬁrst generate samples of the original Mikado model
by creating Nﬁber = 50 straight ﬁbers.
The orienta-
tions of the ﬁbers, θi are randomly distributed from 0
to 2π, with the constraints
π
20 < |θi −θj| < π −π
20 or
π + π
20 < |θi −θj| < 2π −π
20, ∀i, j = 1, 2, ..., 50, to mimic
excluded volume interactions between the ﬁbers and such
that the small angle approximation of the transfer ma-
trix is valid. The centers of the ﬁbers are randomly dis-
tributed in an L × L box, with L = 10. The ﬁbers are
inﬁnitely long to start with, but then we keep only ﬁber-
ﬁber intersections (crosslinks) within the L × L box, and
remove the dangling ends of the ﬁbers.
The resulting
networks look like Fig. 1c in the main text. The mesh
size of the network is characterized by the length scale
ℓ0 = L/Nﬁber,
(29)
where L characterize the length scale of the ﬁbers and
Nﬁber characterize the number of crosslinks on one ﬁber.
In the networks we generated the measured mesh size
is ¯ℓ≃0.33 which diﬀer from ℓ0 = 0.2 by a geometric
constant of O(1).
We will later use ℓ0, the mesh size
length scale, as a natural length unit in presenting the
results.
The modiﬁed Mikado model is obtained by randomly
choosing a central ﬁber from the original Mikado model,
and apply the bulk ﬂoppy mode ⃗u(0)
c,m of the central ﬁber
on the original Mikado model, as described in the main
text.
We then calculate the ﬂoppy mode on the modiﬁed
Mikado model using the transfer matrix method we de-
rived in the main text. Taking U (0)
c
= 0.01, and the BC
that only a displacement Uc,1 > 0 is applied on site 1
of the central ﬁber while keeping site 1 of all other ﬁbers
ﬁxed, we apply the transfer matrix Eq. (3) from the main
text throughout the network to ﬁnd displacements of all
sites (the magnitude of Uc,1 is not important because we
are doing linear analysis). The result is shown in Fig. 1de.
B. Adding bending stiﬀness and measure
asymmetric local stiﬀness on two ends of the central
ﬁber
In this subsection we characterize the asymmetric local
stiﬀness in presence of ﬁber bending stiﬀness. In order
to provide a realistic mechanical description of a ﬁber
network, instead of assigning uniform ki,m to all segments
and κi,m to all crosslinks, we model the ﬁbers as thin rods
of radius a and Young’s modulus Y .
The continuum mechanics of thin rods is described by
the elastic energy
Hrod = 1
2Y πa2
Z ℓ
0
du
ds
2
ds + 1
2
Y πa4
4
Z ℓ
0
dθ
ds
2
ds,
(30)
where the ﬁrst term is the stretching energy and the sec-
ond term is the bending energy (s is the coordinate along
the arc length and u(s), θ(s) are the displacement and
angle at s).
Assuming segments from the ﬁber network are thin
rods described by this equation, we ﬁnd
ki,m = Y πa2
ℓi,m
,
κi,m = Y πa4
4
2
ℓi,m−1 + ℓi,m
.
(31)
where ki,m, κi,m are stretching and bending spring con-
stants in the Hamiltonian [Eq.(1) of the main text].
The ﬁrst equation on stretching spring constant is quite
straight forward from the deﬁnition of Young’s modu-
lus.
The second equation on bending spring constant
comes from the harmonic mean of the bending constants
of the two ﬁber segments meeting at site m. Note that al-
though the rod material is homogeneous along the ﬁber,
the bending spring constant [as deﬁned in Eq.(1) in the
main text] is a function of the segment length. The har-
monic mean comes from the fact that the two segments
are connected in series at site m. A similar construction
that discretize continuous bending of a rod onto a lat-
tice model was used in Ref. [36]. Following the detailed
discussion in Ref. [36] one can show that the bending en-
ergy of the whole ﬁber maps to a sum of discrete bend-
ing terms P
m
κi,m
2 (∆θi,m)2 [as appeared in Eq.(1) in the
main text].
Using these spring constants we then measure local
mechanical response of the modiﬁed Mikado model. The
purpose is to characterize the asymmetric local stiﬀness
of the head and the tail of the central ﬁber, as a result
of the exponentially localized ﬂoppy mode. In order to
do this, we apply a small force ft (direction along the
central ﬁber) on the measurement site (either site 1 or m)
on the central ﬁber, leaving the other end of the central
ﬁber free, while ﬁxing both ends of all other ﬁbers. We
equilibrate the network using gradient descent algorithm


## Page 9


9
FIG. 5. A modiﬁed Mikado network in which two ﬁbers are
pulled. Blue and red arrows show displacements of the two
ﬂoppy modes on these two ﬁbers (calculated separately using
the boundary condition described in the paper for generating
edge ﬂoppy mode on these two ﬁbers individually).
and measure the displacement of the measurement site
projected to the longitudinal direction, ut.
The local
stiﬀness at the measured end of the central ﬁber is then
given by
klocal = ft/ut.
(32)
The magnitude of ft is chosen to be small enough so that
the measurement is in the linear elasticity regime (where
ft vs ut curve is suﬃciently straight across positive and
negative ft).
We measure the local stiﬀness klocal as a function
of both U (0)
c
and bending stiﬀness.
We take U (0)
c
=
(−10, −9, ..., −1, 0, 1, ..., 9, 10) × 10−3 applied on the cen-
tral ﬁber along the direction from site 1 to site m. When
U (0)
c
> 0 the site 1 is the tail and the site m is the head,
and vice versa.
The choice of bending stiﬀness is based on the following
consideration. When we measure mechanical properties
in simulation, the actual control parameter that comes
from ﬁber properties is actually the dimensionless com-
bination
*
κi,m
ki,mℓ2
i,m
+
∼
 a
ℓ0
2
(33)
which is controlled by the ratio between the rod radius
and the characteristic mesh size. The overall factor of
the Young’s modulus can actually be factorized out in
the Hamiltonian. In practice, we keep the mesh size ﬁxed
while vary the ﬁber radius to obtain diﬀerent values of
this ratio, and express our measurement of stiﬀness in
unit of characteristic spring constant
˜k = Y πa2
ℓ0
.
(34)
Thus, we take 3 diﬀerent choices of bending stiﬀness:
(i) a/ℓ0 = 10−2 but take κi,m = 0 at all crosslinks (cen-
tral force network) and ki,m determined from Eq. (31),
(ii) a/ℓ0 = 10−2, and (iii) a/ℓ0 = 10−1. For both (ii) and
(iii) the spring constants are determined by Eq. (31).
Following this construction, we generate 10 samples of
modiﬁed Mikado models, and randomly take 100 ﬁbers
from these networks as the central ﬁber to collect the data
for local stiﬀness. In addition, in generating these net-
works we exclude ﬁber positions which lead to crosslinks
too close to one another (distance smaller than L/200),
to reﬂect ﬁnite size of the crosslinkers. Our results are
presented in Fig. 2c in the main text.
Appendix V: Additional results
A. Multiple pulled ﬁber
In Fig. 5 we show that in a modiﬁed Mikado network where multiple central ﬁbers are pulled simultaneously, each
of these ﬁbers individually host an edge ﬂoppy mode.
B. Keeping residual stress of pulling
In Fig. 6 we show the force-displacement curve of a central ﬁber in a Mikado network where residual stress is
kept, i.e., we do not ignore the stress generated by pulling the central ﬁber to reach the modiﬁed Mikado model.
Alternatively speaking, the force ft is exerted on site nc on the central ﬁber (ft = 0 correspond to the original


## Page 10


10
Mikado network, while the two ends of all other ﬁbers are ﬁxed), and we record the displacement of this site. When
ft > 0, ut > 0 the site nc is the head and exhibit large local stiﬀness (slope of the curve), and when ft < 0, ut < 0 the
site nc is the tail and exhibit small local stiﬀness. Note that the slope at ft = ut = 0 is 0, because we are exiting the
bulk ﬂoppy mode (in linear regime) of the original Mikado network.
Large stiffness at head
Small stiffness at tail
ut(n
C) = 0
ut(n
C) = -0.01
ut(n
C) = 0.01
-0.02
-0.015
-0.01
-0.005
0.005
0.01
0.015
0.02
-0.5
0.5
1
1.5
2
2.5
3
10-4
0
ft (nc)
ut(nc)
FIG. 6. Force-displacement curve of exerting force (parallel to ﬁber) at the end of one ﬁber in the Mikado network. ft > 0 is
pulling the site nc out and ft < 0 is pushing it in. This corresponds to generate the modiﬁed Mikado network while keeping
all residual stress in. The slope of the curve correspond to local stiﬀness, which is the same as what is measured in Fig.2c in
the main text (note that Fig.2c in the main text is the result of disorder average of 100 ﬁbers and the curve in this ﬁgure is
from 1 randomly chosen ﬁber).
[1] E. Prodan and C. Prodan, Phys. Rev. Lett. 103, 248101
(2009).
[2] C. L. Kane and T. C. Lubensky, Nat. Phys. 10, 39 (2014).
[3] T. C. Lubensky, C. Kane, X. Mao, A. Souslov,
and
K. Sun, Reports on Progress in Physics 78, 073901
(2015).
[4] P. Wang, L. Lu, and K. Bertoldi, Physical review letters
115, 104302 (2015).
[5] L. M. Nash, D. Kleckner, A. Read, V. Vitelli, A. M.
Turner, and W. T. Irvine, Proceedings of the National
Academy of Sciences 112, 14495 (2015).
[6] R. S¨usstrunk and S. D. Huber, Science 349, 47 (2015).
[7] S. H. Mousavi, A. B. Khanikaev, and Z. Wang, Nature
communications 6 (2015).
[8] Z. Yang, F. Gao, X. Shi, X. Lin, Z. Gao, Y. Chong, and
B. Zhang, Phys. Rev. Lett. 114, 114301 (2015).
[9] V. Peano, C. Brendel, M. Schmidt, and F. Marquardt,
Phys. Rev. X 5, 031011 (2015).
[10] C. Strohm, G. Rikken, and P. Wyder, Phys. Rev. Lett.
95, 155901 (2005).
[11] L. Sheng, D. Sheng, and C. Ting, Physical review letters
96, 155901 (2006).
[12] R. K. Pal, M. Schaeﬀer,
and M. Ruzzene, Journal of
Applied Physics 119, 084305 (2016).
[13] C. He, X. Ni, H. Ge, X.-C. Sun, Y.-B. Chen, M.-H. Lu,
X.-P. Liu, and Y.-F. Chen, Nature Physics (2016).
[14] R. S¨usstrunk and S. D. Huber, PNAS 113, E4767 (2016).
[15] M. Xiao, W.-J. Chen, W.-Y. He, and C. Chan, Nature
Physics (2015).
[16] D. Z. Rocklin, B. G. G. Chen, M. Falk, V. Vitelli, and
T. C. Lubensky, Physical Review Letters 116, 135503
(2016).
[17] D. Z. Rocklin, S. Zhou, K. Sun,
and X. Mao, Nature
Communications 8, 14201 (2017).
[18] J. Paulose, A. S. Meeussen, and V. Vitelli, PNAS 112,
7639 (2015).
[19] J. Paulose, B. G.-g. Chen, and V. Vitelli, Nature Physics
(2015).
[20] B. G.-g. Chen, N. Upadhyaya, and V. Vitelli, Proceed-
ings of the National Academy of Sciences 111, 13004
(2014).
[21] A. Souslov, A. J. Liu, and T. C. Lubensky, Phys. Rev.
Lett. 103, 205503 (2009).
[22] X. Mao, N. Xu, and T. C. Lubensky, Phys. Rev. Lett.
104, 085504 (2010).
[23] W. G. Ellenbroek and X. Mao, Europhys. Lett. 96 (2011).
[24] X. Mao and T. C. Lubensky, Phys. Rev. E 83, 011111
(2011).
[25] K. Sun, A. Souslov, X. Mao, and T. C. Lubensky, Proc.
Natl. Acad. Sci. U. S. A. 109, 12369 (2012).
[26] L. Zhang, D. Z. Rocklin, B. G.-g. Chen,
and X. Mao,


## Page 11


11
Phys. Rev. E 91, 032124 (2015).
[27] X. Mao, A. Souslov, C. I. Mendoza, and T. C. Lubensky,
Nature Communications 6, 5968 (2015).
[28] D. M. Sussman, O. Stenull, and T. Lubensky, Soft mat-
ter 12, 6079 (2016).
[29] N. P. Mitchell, L. M. Nash, D. Hexner, A. Turner, and
W. Irvine, arXiv preprint arXiv:1612.09267 (2016).
[30] D. A. Head, A. J. Levine, and F. C. MacKintosh, Phys.
Rev. Lett. 91, 108102 (2003).
[31] J. Wilhelm and E. Frey, Phys. Rev. Lett. 91, 108103
(2003).
[32] M. Gardel, J. Shin, F. MacKintosh, L. Mahadevan,
P. Matsudaira, and D. Weitz, Science 304, 1301 (2004).
[33] C. Storm, J. Pastore, F. MacKintosh, T. Lubensky, and
P. Janmey, Nature 435, 191 (2005).
[34] C. Heussinger and E. Frey, Phys. Rev. Lett. 97, 105501
(2006).
[35] C. P. Broedersz, X. Mao, T. C. Lubensky,
and F. C.
MacKintosh, Nat. Phys. 7, 983 (2011).
[36] X. Mao, O. Stenull, and T. C. Lubensky, Phys. Rev. E
87, 042601 (2013).
[37] X. Mao, O. Stenull, and T. C. Lubensky, Phys. Rev. E
87, 042602 (2013).
[38] C. P. Broedersz and F. C. MacKintosh, Reviews of Mod-
ern Physics 86, 995 (2014).
[39] A. Sharma, A. Licup, K. Jansen, R. Rens, M. Sheinman,
G. Koenderink, and F. MacKintosh, Nature Physics 12,
584 (2016).
[40] J. Feng, H. Levine, X. Mao, and L. M. Sander, Physical
Review E 91, 042710 (2015).
[41] J. Feng, H. Levine, X. Mao,
and L. M. Sander, Soft
matter 12, 1419 (2016).
[42] B. Alberts, A. Johnson, J. Lewis, M. Raﬀ, K. Roberts,
and P. Walter, Molecular Biology of the Cell, 4th ed.
(Garland, New York, 2008).
[43] C. P. Brangwynne, G. H. Koenderink, F. C. MacKintosh,
and D. A. Weitz, The Journal of cell biology 183, 583
(2008).
[44] J.-F. Joanny and J. Prost, HFSP journal 3, 94 (2009).

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]