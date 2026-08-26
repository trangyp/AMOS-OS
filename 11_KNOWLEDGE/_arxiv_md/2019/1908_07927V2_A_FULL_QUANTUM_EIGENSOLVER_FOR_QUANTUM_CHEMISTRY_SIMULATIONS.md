---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.07927v2
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1908.07927v2_A_Full_Quantum_Eigensolver_for_Quantum_Chemistry_Simulations

> Source: 1908.07927v2_A_Full_Quantum_Eigensolver_for_Quantum_Chemistry_Simulations.pdf

> Pages: 9

---


## Page 1


A Full Quantum Eigensolver for Quantum Chemistry Simulations
Shijie Wei,1, 2 Hang Li,2 and GuiLu Long2, 3, 1, 4, ∗
1Beijing Academy of Quantum Information Sciences, Beijing 100193, China
2State Key Laboratory of Low-Dimensional Quantum Physics and Department of Physics, Tsinghua University, Beijing 100084, China
3 Beijing National Research Center for Information Science and Technology
and School of Information Tsinghua University, Beijing 100084, China
4Frontier Science Center for Quantum Information, Beijing 100084, China
(Dated: 25th February 2020)
Quantum simulation of quantum chemistry is one of
the most compelling applications of quantum comput-
ing.
It is of particular importance in areas ranging
from materials science, biochemistry and condensed mat-
ter physics. Here, we propose a full quantum eigensolver
(FQE) algorithm to calculate the molecular ground en-
ergies and electronic structures using quantum gradient
descent. Compared to existing classical-quantum hybrid
methods such as variational quantum eigensolver (VQE),
our method removes the classical optimizer and performs
all the calculations on a quantum computer with faster
convergence. The gradient descent iteration depth has a
favorable complexity that is logarithmically dependent on
the system size and inverse of the precision. Moreover,
the FQE can be further simpliﬁed by exploiting perturba-
tion theory for the calculations of intermediate matrix ele-
ments, and obtain results with a precision that satisﬁes the
requirement of chemistry application. The full quantum
eigensolver can be implemented on a near-term quantum
computer. With the rapid development of quantum com-
puting hardware, FQE provides an efﬁcient and powerful
tool to solve quantum chemistry problems.
I.
INTRODUCTION
Quantum
chemistry
studies
chemical
systems
using
quantum mechanics. One primary focus of quantum chem-
istry is the calculation of molecular energies and electronic
structures of a chemical system which determine its chemical
properties. Molecular energies and electronic structures are
calculated by solving the Schr¨odinger equation within chem-
ical precision. However, the computational resources needed
scale exponentially with the system size on a classical com-
puter, making the calculations in quantum chemistry intract-
able in high-dimension.
Quantum computers, originally envisioned by Benioff,
Manin and Feynman [1–3], have emerged as promising tools
for tackling this challenge with polynomial overhead of com-
putational resources. Efﬁcient quantum simulations of chem-
istry systems promise breakthroughs in our knowledge for
basic chemistry and revolutionize research in new materials,
pharmaceuticals, and industrial catalysts.
The universal quantum simulation method [4] and the ﬁrst
quantum algorithm for simulating fermions [5] have laid
down the fundamental block of quantum chemistry simula-
tion. Based on these techniques and quantum phase estima-
tion algorithm [6], Aspuru-Guzik et al presented a quantum
algorithm for preparing ground states undergoing an adiabatic
evolution [7], and many theoretical and experimental works
[8–24] have been developed since then. In 2002, Somma et
al. proposed a scalable quantum algorithm for the simulation
of molecular electron dynamics via Jordan-Wigner transform-
ation [25]. The Jordan-Wigner transformation directly maps
the fermionic occupation state of a particular atomic orbital
to a state of qubits, which enables the quantum simulation of
chemical systems on a quantum computer. Then, the Bravyi-
Kitaev transformation [26–30] encodes both locality of occu-
pation and parity information onto the qubits, which is more
efﬁcient in operation complexity. In 2014, Peruzzo et al de-
veloped the variational quantum eigensolver (VQE) [18, 31],
which ﬁnds a good variational approximation to the ground
state of a given Hamiltonian for a particular choice of ansatz.
Compared to quantum phase estimation and trotterization of
the molecular Hamiltonian, VQE requires a lower number of
controlled operations and shorter coherence time. However,
VQE is a classical and quantum hybrid algorithm, the optim-
izer is performed on a classical machine.
Meanwhile, implementations of quantum chemistry simu-
lation have been developing steadily. Studies in present-day
quantum computing hardware have been carried out, such as
nuclear magnetic resonance system [32, 33], photonic sys-
tem [34–36], nitrogen-vacancy center system [37] , trapped
ion [38, 39] and superconducting system [40–42].
Rapid
development in quantum computer hardware with even the
claims of quantum supremacy, greatly stimulates the expect-
ation of its real applications. Quantum chemistry simualtion
is considered as a real application in Noisy Intermediate-Scale
Quantum (NISQ) computers [22, 43, 44]. The FQE is an effort
on this background. In FQE, not only calculation of Hamilto-
nian matrix part is done on quantum computer, but also the
optimization by gradient descent is performed on quantum
computer. FQE can be used in near-term NISQ computers,
and in future fault-tolerant large quantum computers.
arXiv:1908.07927v2  [quant-ph]  22 Feb 2020


## Page 2


2
II.
METHOD
A.
Preparing the Hamiltonian for Quantum Chemistry
Simulation
A molecular system, contains a collection of nuclear
charges Zi and electrons. The fundamental task of quantum
chemistry is to solve the eigenvalue problem of the molecu-
lar Hamiltonian. The eigenstates of the many-body Hamilto-
nian determine the dynamics of the electrons as well as the
properties of the molecule.
The corresponding Hamilto-
nian of the system includes kinetic energies of nuclei and
electrons, the Coulomb potentials of nuclei-electron, nuclei-
nuclei, electron-electron and it can be expressed in ﬁrst quant-
ization as
Ho = −
X
i
∇2
Ri
2Mi
−
X
i
∇2
ri
2 −
X
i,j
Zi
|Ri −r j|
+
X
i, j>i
ZiZj
|Ri −Rj| +
X
i, j>i
1
|ri −r j|,
(1)
in atomic units (ℏ= 1), where Ri, Zi, Mi and ri are the pos-
itions, charges, masses of the nuclei and the positions of the
electrons respectively. Under the Born-Oppenheimer approx-
imation which assumes the nuclei as a ﬁxed classical point,
this Hamiltonian is usually rewritten in the particle number
representation in a chosen basis
H =
X
i j
hija†
i a j + 1
2
X
ijkl
hijkla†
i a†
jakal + . . . ,
(2)
where · · · denotes higher order interactions and a†
i and aj are
the creation and annihilation operator of particle in orbital i
and j respectively. The parameters hij and hijkl are the one-
body and two-body integrations in the chosen basis functions
{ψi}. In Galerkin formulation, the scalar coefﬁcients in Eq. (2)
can be calculated by
hi j = ⟨ψi|
−∇2
i
2 −
X
A
ZA
|ri −RA|
|ψj⟩
(3)
hijkl = ⟨ψiψj|
1
ri −rj
|ψkψl⟩
In order to perform calculations on a quantum computer,
we need to map fermionic operators to qubit operators. We
choose Jordan-Wigner transformation to achieve this task due
to its straightforward expression.
The Jordan-Wigner transformation maps Eq. (2) into a
qubit Hamiltonian form
H =
X
i,α
hi
ασi
α +
X
i, j,α,β
hij
αβσi
ασj
β + . . . ,
(4)
where Roman indices i, j denote the qubit on which the op-
erator acts, and Greek indices α, β refer to the type of Pauli
operators, i.e., σi
x means Pauli matrix σx acting on a qubit at
site i. Apparently, H in Eq. (2) is a linear combination of unit-
ary Pauli matrices. The methods used in this paper ﬁnding the
molecular ground-state and its energy are all based on it.
In this work, we present the FQE to ﬁnd the molecular
ground-state energy by gradient descent iterations. Gradient
descent is one of the most fundamental ways for optimization,
that looks for the target energy value along the direction of the
steepest descent. Here it is performed in a quantum computer
with the help of linear combination of unitary operators. We
analyse the relationships between the gradient descent itera-
tion depth and the precision of the ground-state energy. The
explicit quantum circuit to implement the algorithm is con-
structed. As illustrative examples, the ground-state energies
and electronic structures of four molecules, H2, LiH, H2O and
NH3 are presented. Taking H2O and NH3 as examples, a com-
parison between the FQE and VQE, a representative hybrid
method, is given. FQE can be accelerated further by harness-
ing perturbation theory in chemical precision. Finally, we ana-
lyse the computation complexity of FQE and summarize the
results.
B.
Quantum Gradient Descent Iteration
The classical gradient descent algorithm is usually em-
ployed to obtain the minimum of an target function f(X). One
starts from an initial point X(0) = x0
1, x0
2, . . . , x0
N ∈RN, then
moves to the next point along the direction of the gradient of
the target function, namely
X(t+1) = X(t) −γ0∇f(X(t)),
(5)
where γ0 is a positive learning rate that determines the step
size of the iteration. In searching the minimum energy of a
Hamiltonian, the target function can be expressed as a quad-
ratic optimization problem in the form, f(X) = XTHX. At
point X, the gradient operator of the objective function can be
expressed as
∇f(X) = 2HX.
(6)
Then, the gradient descent iteration can be regarded as an
evolution of X under operator H,
|X(t+1)⟩=

|X(t)⟩−γH|X(t)⟩

,
(7)
where γ0 is redeﬁned as γ
= 2γ0.
In quantum gradi-
ent descent, vector X is replaced by quantum state |X⟩=
P
j xj| j⟩/∥X∥, where x j is the j-th elements of the vector, | j⟩is
the N-dimensional computational basis, and ∥X∥is the modu-
lus of vector X. Denoting Hg = I−γH and it can be expressed
as
Hg =
M
X
i=1
βiHg
i ,
(8)


## Page 3


3
where M is the number of Pauli product terms in Hg. Then
the gradient descent process can be rewritten as
|X(t+1)⟩= Hg|X(t)⟩=
M
X
i=1
βiHg
i |X(t)⟩,
(9)
where Hg is a linear combination of unitary operators(LCU)
which was proposed in [45] in designing quantum algorithms
and studied extensively [46–52]. This non-unitary evolution
can be implemented in a unitary quantum circuit by adding
ancillary qubits that transform it into unitary evolution in a
larger space [53]. The realization of LCU can be viewed as
a quantum computer wavefunction passing through M-slits,
and operated by a unitary operation in each slit, and then the
wavefunctions are combined and the result of the calculation
is readout by a measurement [49]. We perform the evolution
described by Eq. (9) with the following four steps.
Wave division: The register is a composite system which
contains a work system and an ancillary register. Firstly, the
initial point X = (x1, . . . , xN)T is efﬁciently mapped as an ini-
tial state |x(t)⟩of the work system.
In quantum chemistry,
Hartree-Fock (HF) product state is usually used as an initial
state. And the ancillary register is initialized from |0⟩m, where
m = log2M, to a speciﬁc superposition state |ψs⟩,
|ψs⟩= 1
C
M−1
X
i=0
βi|i⟩
(10)
where C =
qPM−1
i=0 β2
i is a normalization constant and |i⟩is
the computational basis. This is equivalent to let the state |x(t)⟩
pass through M-slits. βi is a factor describing the properties of
the slit, which is determined by the forms of the Hamiltonian
in Eq. (8). This can be done by the initialization algorithm in
[54]. Moreover, the quantum random access memory (qRAM)
approach can be used to prepare |x(t)⟩and |ψs⟩, which consume
O(log N) and O(log M) basic steps or gates respectively after
qRAM cell is established. We denote the whole state of the
composite system as |Φ⟩= |ψs⟩|x(t)⟩.
Entanglement: Then, a series of ancillary system controlled
operations PM−1
i=0 |i⟩⟨i| ⊗Hg
i are implemented on the work
qubits. The work qubits and the ancilla register are now en-
tangled , and the state is transformed into
|Φ⟩→1
C
  M−1
X
i=0
βi|i⟩Hg
i |x(t)⟩.
(11)
The corresponding physical picture is that different unitary
operations are implemented simultaneously in different sub-
spaces, corresponding to different slits.
Wave combination : We perform m Hadamad gates on an-
cillary register to combine all the wavefunctions from the M
different subspaces. We merely focus on the component in a
subspace where the ancillary system is in state |0⟩. The state
of the whole system in this subspace is
|Φ0⟩=
1
C
√
2m
 |0⟩
M−1
X
i=0
βiHg
i |x(t)⟩.
(12)
𝐻𝑀
Readout
|0⟩
|𝑥⟩
0
0
0
0
𝐻1
𝑔
𝐻2
𝑔
𝐻𝑀
𝑔
𝑬𝒏𝒕𝒂𝒏𝒈𝒍𝒆𝒎𝒆𝒏𝒕
0
0
0
1
M-1
……
𝑪𝒓𝒆𝒂𝒕𝒔𝒖𝒑𝒆𝒓𝒑𝒐𝒔𝒊𝒕𝒊𝒐𝒏
𝑪𝒐𝒎𝒃𝒊𝒏𝒂𝒕𝒊𝒐𝒏
𝑴𝒆𝒂𝒔𝒖𝒓𝒆𝒎𝒆𝒏𝒕
𝜓𝑠
Wave division        Entanglement       Wave combination  Measurement
Figure 1: Quantum circuit for gradient descent. |x⟩and |ψs⟩denote the ini-
tial state of the work system and ancilla syetem respectively. The controlled
operations acted on work system are PM−1
i=0 |i⟩⟨i|⊗Hg
i . HM denotes m = log2M
number Hadamard gates.At the end of the circuit, we measure the ﬁnal state
of the ancilla registers. If all ancilla qubits are |0⟩, the work systerm collapses
into state |x(t+1)⟩.
Measurement: Then, we measure the ancillary register. If
we obtain |0⟩, our algorithm succeeds and we obtain the
state
1
C
√
2m
 |0⟩PM−1
i=0 βiHg
i |x(t)⟩, where the work system is in
|x(t+1)⟩= Hg|x(t)⟩. And then this will be used as input for the
next iteration in the quantum gradient descent process. The
probability of obtaining |0⟩for the state is
Ps =∥Hg|x(t)⟩∥2 /C2M.
The successful probability after n measurements is 1 −(1 −
∥Hg|x(t)⟩∥2
C2M
)n, which is an exponential function of n. The num-
ber of measurements is C2M/ ∥Hg|x(t)⟩∥2.
The meas-
urement complexity will grow exponentially with respect to
the number of iteration steps [55].
Alternatively, one can
use the oblivious amplitude ampliﬁcation [51] to amplify the
amplitude of the desired term (ancillary qubits in state |0⟩)
up to a deterministic order with O(
√
M) repetitions before
the measurement. Then, the measurement complexity will
be the product of iteration depth k and O(
√
M), linearly de-
pendent on the number of iteration steps.
After obtaining
|0⟩, we can continue the gradient descent process by repeat-
ing the above four steps, with |x(t)⟩repalced by |x(t+1)⟩in
Wave-division step. We can pre-set a threshold deﬁned as
ε = |⟨xt|H|xt⟩−⟨xt+1|H|xt+1⟩|/⟨xt|H|xt⟩as criterion for stop-
ping the iteration. Thus, we judge if the iterated state satisﬁes
criterion by measuring the expectation value of Hamiltonian
around the expected number of iteration, which is easier than
constructing the tomography. If the next iterative state |x(t+1)⟩
does not hit our pre-set threshold, this output |x(t+1)⟩will be
regarded as the new input state |x(t)⟩and run the next itera-
tion. Otherwise, the iteration can be terminated and the state
|x(t+1)⟩is the ﬁnal result |xf ⟩, as one good approximation of
the ground state. The ground state energy can be calculated
by ⟨xf |H|x f ⟩.
Measuring the expectation values during the iteration pro-
cedure will destroy the state of the work system, stopping the
quantum gradient descent process. So, determing the iteration


## Page 4


4
depth k in advance is essential. After k times iterations, the
approximation error is limited to (ignoring constants)
ϵ ≤O
 
(1 −γλ2
1 −γλ1
)kN
!
,
where λ1 and λ2 are the two largest absolute values of the
eigenvalues of Hamiltonian H (see Supplemental Material for
proof). The iteration depth
k = O(log N
ϵ )
(13)
is logarithmically dependent on the system size and the in-
verse of precision. The algorithm may be terminated at a point
with a pre-set precision ϵ. It can be seen that the choise of γ
has little impact on converge rate when γ is large. This makes
this algorithm very robust to this parameter. The rate of con-
vergence primarily depends upon the ratio of λ1 and λ2. The
gap between the iterative result and the ground state depends
on the choice of initial point. If we choose an ansatz state
with a large overlap with the exact ground state, the iterative
process will converge to the the ground state in fewer itera-
tions. Usually, the mean-ﬁeld state which represents a good
classical approximation to the ground state of Hamiltonian H,
such as a Hartree-Fock (HF) product state, is chosen as an
initial state. Compared to VQE, FQE does not need to make
measurements of the expectation values of Hamiltonian dur-
ing each iteration procedure and this substantially reduces the
computation resources.
C.
Perturbation Theory
The FQE involves multi-time iterations to obtain an accur-
ate result, which is difﬁcult to implement in the present-day
quantum computer hardware. Here, we present an approxim-
ate method to ﬁnd the ground state and its energy by using the
gradient descent algorithm and perturbation theory. Perturba-
tion theory is widely used and plays an important role in de-
scribing real quantum systems, because it is impossible to ﬁnd
exact solutions to the Schr¨odinger equation for Hamiltonians
even with moderate complexity. The Hamiltonian described
by Eq. (4) can be divided into two classes, H0 and H′. H0
consists of a set of Pauli terms containing only σi
α=z and the
identity matrices, and Pauli terms σi
α=x,y belong to H′. H0 is a
diagonal matrix with exact solutions, that can be regarded as
a simple system. H′ usually is smaller compared to H0, and is
treated as a “perturbing” Hamiltonian. The energy levels and
eigenstates associated with the perturbed system can be ex-
pressed as “corrections” to those of the unperturbed system.
We begin with the time-independent Schr¨odinger equation:
H|ψn⟩= (H0 + H′)|ψn⟩= En|ψn⟩,
(14)
where En and |ψn⟩are the n-th energy and eigenstate re-
spectively. Unperturbed Hamiltonian H0, satisﬁes the time-
independent Schr¨odinger equation: H0|n⟩= E(0)
n |n⟩. Our goal
is to express En and |ψn⟩in terms of E0
n and |n⟩. Denote the
expectation value of H′ as H′
nn = ⟨n|H′|n⟩, and it is easily to
see that ⟨n|H′|n⟩is zero because H′ only contains Pauli terms
σi
α=x,y. In the ﬁrst order approximation, the energies and ei-
genstates are expressed as
En = E(0)
n ,
(15)
|ψn⟩= |n⟩−
X
m,n
H′
mn
E(0)
m −E(0)
n
|m⟩.
(16)
To second-order approximation, they are
En = E(0)
n +
X
m,n
|H′
mn|2
E(0)
m −E(0)
n
,
(17)
|ψn⟩= |n⟩−
X
m,n
H′
mn
E(0)
m −E(0)
n
|m⟩−1
2
X
m,n
|H′
mn|2
(E(0)
m −E(0)
n )2 |n⟩,
(18)
+
X
m,n

X
k,n
H′
mnH′
kn
(E(0)
m −E(0)
n )(E(0)
k
−E(0)
n )
|m⟩.
The matrix elements in the ﬁrst and second-order approxima-
tions can be obtained by one iteration of the quantum circuit
in Fig.(1). Here, we let H′ be equal to Hg. Explicitly, the
ﬁrst order approximation only involves H′
mn, a series of trans-
ition probabilities of the state after H′ implemented on state
|n⟩, and they can be obtained by performing the quantum cir-
cuit of Fig.(1) directly. For the second order approximation,
matrix elements such as value |H′
mn|2 and H′
mnH′
kn, can be cal-
culated by H′
mn. Then, the approximate ground energy and
ground state up to second-order are obtained. We will show
the performance of FQE and perturbation theory in next sec-
tion.
III.
RESULTS
A.
Calculations of Four Molecules
To demonstrate the feasibility of this FQE with gradient
descent iteration, we carried out calculations on the ground
state energy of H2, LiH diatomic molecules, and two relat-
ively complex molecules H2O and NH3. We used a common
molecular basis set, the minimal STO-3G basis. Via Jordan-
Wigner transformation, the qubit-Hamiltonians of these mo-
lecules are obtained. The Hamiltonians of H2, LiH, H2O and
NH3 contain 15 , 118, 252, and 3382 Pauli matrix product
terms respectively. The dimensions of the Hamiltonians of H2,
LiH, H2O and NH3 are 16 , 64, 4096, and 16384 respectively,
which corresponds 4, 6, 12, 14 number of qubits respectively.
In all four simulations, the work system was initialized to the
HF state |xh⟩and the learning rate is chosen as γ = 1. As
shown in Fig.(2), after about 120 iterations, the molecular en-
ergy of H2O converges to -74.94 a.u, only 0.0013346% dis-
crepancy with respect to the exact value of -74.93 a.u. ob-
tained via Hamiltonian diagonalization.
The NH3 calcula-
tion yields (-55.525 a.u.) after 80 iterations, matched very


## Page 5


5
0
10
20
30
40
50
Iteration, k
1.135
1.130
1.125
1.120
Energy(hartree)
H2
Noiseless
Gaussian Noise
Random Noise
Exact Value
0
20
40
60
80
100
Iteration, k
7.86220
7.86215
7.86210
7.86205
7.86200
7.86195
7.86190
7.86185
LiH
Noiseless
Gaussian Noise
Random Noise
Exact Value
0
50
100
150
Iteration, k
75.00
74.99
74.98
74.97
74.96
Energy(hartree)
H2O
Noiseless
Gaussian Noise
Random Noise
Exact Value
0
50
100
150
Iteration, k
55.52
55.51
55.50
55.49
55.48
55.47
55.46
NH3
Noiseless
Gaussian Noise
Random Noise
Exact Value
Figure 2: (a), (b), (c) and (d) show the convergence to ground state energies
by FQE for H2, LiH, H2O and NH3 molecules respectively. The numerical
simulations are carried out with ﬁxed interatomic distance. The exact value
corresponding to Hamiltonian diagonalization energy (red line). The initial
state is chosen as Hartree-Fock product state in all four cases. The ﬁnal values
of the lines for exact ground state energy (red line) and for the three iteration
results, noiseless case (blue line), random noisy case (green line) and Gaus-
sian noisy case (orange line).
Figure 3:
The exact comparison of FQE and VQE for searching ground
state energy of H2O and NH3 molecules respectively. The red color lines
labled as ’Theory Value’ are the exact values of ground state energy. The
labels of the right symbols denote different learning rates.
well with the diagonalization (-55.526 a.u.). For the study
of atomic molecular structures and chemical reactions, these
results are sufﬁciently accurate. For more complex basis set
STO-6G, the results are about the same, and the details are
given in Supplemental Material. The converge rates of the
four molecules depend on the system size and the ratio of the
two largest absolute eigenvalues of the Hamiltonian H, which
are consistent with the theoretical analysis above.
We also studied the infulence of noises which is also shown
in the Fig.(2). The noise term is chosen the form of PN
i=1 δαiσz
, added to the Hamiltonian to simulate decoherence. Then we
add a term |δ⃗x⟩on the iterative state |xk⟩to simulate meas-
urement error and renormalize the iterative state as |x(k)⟩→
(|x(k)⟩+ |δ⃗x⟩)/ ∥|x(k)⟩+ |δ⃗x⟩∥. We set a random noise ( amp-
litude 0.01) and a Gaussian noise (µ = 0, σ = 0.01/3) for H2
and LiH. For H2O and NH3, we choose a random noise (amp-
litude 0.02) and a Gaussian noise (µ = 0, σ = 0.02/3). The
results still converge to the exact values in chemical precision
(1.6 × 10−3 a.u). This indicates that our method is robust to
certain type of noise, which is important in the implement-
ation of quantum simulation on near term quantum devices.
For more noisy situations, see Supplemental Material for de-
tails, where the parameters of noise are 10 times of the above
values. The convergence deteriorates and some oscillations
accur as the number of iterations increases.
In Fig.(3), a comparison with VQE is shown for H2O and
NH3. In VQE calculation, the initial state |x0⟩is mapped to
an ansatz state by a parameterized unitary operation |x(⃗θ)⟩=
U(⃗θ)|x0⟩. VQE solves for the parameter vector ⃗θ with a clas-
sical optimization routine. Here we adopt the standard gradi-
ent descent method as the classical optimizer in VQE. The
parameter is updated by ⃗θ →⃗θ −γ f(⃗θ+∆⃗θ)−f(⃗θ)
∆⃗θ
. We performed
numerical simulations of VQE for the two molecules. When
the learning rate γ ≥10−3, VQE does not converge to the
ground state. So, in order to compare with each other, we
choose the proper learning rates in two methods seperately.
In both cases, the initial ansatz state is prepared as the HF
product state. In H2O and NH3, VQE converges most fast with
the learning rate γ = 10−3. FQE converges more and more
fast with larger and larger learning rate until a ﬁxed speed is
reached . As shown in Fig.(3), FQE generally converges faster
than VQE and the advantage will be more obvious in complex
molecules.
The above examples are calculated in ﬁxed interatomic dis-
tance of the molecules. If we want to calculate the interatomic
distance corresponding to the most stable structure, the vari-
ation of interatomic distances is necessary. In Fig.(4), four
examples are given to illustrate the performance of perturba-
tion theory. To obtain the potential-energy surfaces for H2,
LiH, H2O and NH3 molecules, we studied the dependence
of ground-state energy of their molecules on the variating in-
teratomic distances, between the two atoms in H2, LiH, and
the distance between the oxygen atom and one hydrogen atom
(the two hydrogen atoms are symmetric with respect to the
oxygen atom) in H2O, and the distance between the nitrogen
atom and the plane formed by the three hydrogen atoms in
NH3. The lowest energy in potential-energy surfaces corres-
ponds to the most stable structure of the molecules. As shown
in the picture, the ground-state energy of each molecule calcu-
lated under the second order approximation are already quite
close to their exact values, which is obtained from Hamilto-
nian diagonalizations. The energy values up to second-order
correction are compared with their exact values at the most
stable interatomic distance corresponding to the lowest energy
in Table.1. It can be seen that the second order approximation
has already given results in chemical precision.


## Page 6


6
Distance(Å)
Energy value(au) exact value zero-order value ﬁrst-order value second-order value
H2(0.7314)
-1.1373
-1.1171
-1.1372
-1.1372
LiH(1.5065)
-7.8637
-7.8634
-7.8637
-7.8637
H2O(1.0812)
-75.0038
-74.9622
75.0013
75.0032
NH3(0.4033)
-55.5247
-55.4530
-55.5193
-55.5237
Table I: Energy values calculated by perturbation method and the exact values in the most stable distance corresponding to the lowest ground energy.
(a)
(d)
(c)
(b)
Figure 4:
Theory results (blue lines), zero-order (orange lines), ﬁrst-order
(green lines) and second-order (red lines) energy plots of outcomes from
numerical simulations, for several interatomic distances for H2, LiH, H2O
(between the oxygen atom and one hydrogen atom) and NH3 (between the
nitrogen atom and the plane formed by the three hydrogen atoms).
B.
Analysis of Computational Complexity
Here we analyze the complexity of our algorithm. Usu-
ally, a quantum algorithm complexity involves two aspects:
qubit resources and gate complexity. For qubit resources, the
number of ancilla qubits is logM, where M is the number of
Pauli terms in qubit form Hamiltonian. For gate complex-
ity, the “Wave division” part needs O(logN + logM) basic
steps for state preparation. The dominate factor is the num-
ber of controlled operations in “Entanglement” part in Fig.
(1). Controlled Hg
i can be decomposed into O(MlogMlogN)
basic gates [56, 57]. The “Wave combination ” part just com-
prises logM Hadamard gates. Totally, FQE requires in each
iteration about O(MlogMlogN) basic gates for implementa-
tion. If the wavefunction is expressed by O(N) Gaussian or-
bitals, fermion Hamiltonians contain O(N4) second-quantized
terms, consequently the qubit Hamiltonians have M = O(N4)
Pauli terms. The qubit resource and gate complexity can be
reduced to O(N) and O(N4) respectively. In some applica-
tions, the perturbation theory only requires one iteration, and
an approximate result in chemical precision can be obtained.
IV.
SUMMARY
An efﬁcient quantum algorithm, Full Quantum Eigensolver
(FQE), for calculating the ground state wavefunction and the
ground energy using gradient descent (FQE) was proposed,
and numerical simulations are performed for four molecules.
In FQE, the complexity of basic gates operations is polylog-
arithmical to the number of single-electron atomic orbitals. It
achieves an exponential speedup compared with its classical
counterparts. It has been shown that FQE is robust against
noises of reasonable strengths. For very noisy situations that
do not allow many iterations, FQE can be combined with per-
turbation theory that give the ground state and its energy in
chemical precision with one time iteration. FQE is exception-
ally useful in quantum chemistry simulation, especially for
the near-term NISQ applications. FQE is a full quantum al-
gorithm, not only applicable for NISQ computers, but directly
applicable for future large-scale fault-tolerant quantum com-
puters.
Acknowledgements
This research was supported by National Basic Research
Program of China.
We gratefully acknowledges support
from the National Natural Science Foundation of China
under Grants No.
11974205, and No.
11774197.
The
National Key Research and Development Program of China
(2017YFA0303700); The Key Research and Development
Program of Guangdong province (2018B030325002); Beijing
Advanced Innovation Center for Future Chip (ICFC).
Author contributions
S.J.W conceived the algorithm.
H.L performed classical
simulations.
G.L.L initialized LCU scheme.
All authors
contributed to the discussion of results and writing of the
manuscript.
Competing interests
The authors declare no competing interests.
Data availability
The data that support the ﬁndings of this study are available
from the corresponding authors on reasonable request.
∗Electronic address: gllong@tsinghua.edu.cn
[1] Paul Benioff. The computer as a physical system: A micro-
scopic quantum mechanical hamiltonian model of computers as


## Page 7


7
represented by turing machines. Journal of Statistical Physics,
22(5):563–591, 1980.
[2] Ivanovich Manin. Vychislimoe i nevychislimoe. Sov. Radio,
1980.
[3] Richard P Feynman. Simulating physics with computers. Inter-
national Journal of Theoretical Physics, 21(6):467–488, 1982.
[4] Seth Lloyd.
Universal quantum simulators.
Science,
273(5278):1073–1078, 1996.
[5] Daniel S Abrams and Seth Lloyd. Simulation of many-body
fermi systems on a universal quantum computer. Physical Re-
view Letters, 79(13):2586, 1997.
[6] A Yu Kitaev. Quantum measurements and the abelian stabilizer
problem. arXiv preprint quant-ph/9511026, 1995.
[7] Al´an Aspuru-Guzik, Anthony D Dutoi, Peter J Love, and Mar-
tin Head-Gordon. Simulated quantum computation of molecu-
lar energies. Science, 309(5741):1704–1707, 2005.
[8] Ryan Babbush, Peter J Love, and Al´an Aspuru-Guzik. Adia-
batic quantum simulation of quantum chemistry. Scientiﬁc Re-
ports, 4:6603, 2014.
[9] Guan-Ru Feng, Yao Lu, Liang Hao, Fei-Hao Zhang, and Gui-
Lu Long.
Experimental simulation of quantum tunneling in
small systems. Scientiﬁc Reports, 3:2232, 2013.
[10] Yao Lu, Guan-Ru Feng, Yan-Song Li, and Gui-Lu Long. Exper-
imental digital quantum simulation of temporal–spatial dynam-
ics of interacting fermion system. Science Bulletin, 60(2):241–
248, 2015.
[11] Ryan Babbush, Jarrod McClean, Dave Wecker, Al´an Aspuru-
Guzik, and Nathan Wiebe.
Chemical basis of trotter-suzuki
errors in quantum chemistry simulation. Physical Review A,
91(2):022311, 2015.
[12] Shi-Jie Wei, Dong Ruan, and Gui-Lu Long. Duality quantum
algorithm efﬁciently simulates open quantum systems.
Sci-
entiﬁc Reports, 6:30727, 2016.
[13] Ryan Babbush, Dominic W Berry, Ian D Kivlichan, Annie Y
Wei, Peter J Love, and Al´an Aspuru-Guzik. Exponentially more
precise quantum simulation of fermions in second quantization.
New Journal of Physics, 18(3):033032, 2016.
[14] Ryan Babbush, Dominic W Berry, Yuval R Sanders, Ian D Kiv-
lichan, Artur Scherer, Annie Y Wei, Peter J Love, and Al´an
Aspuru-Guzik. Exponentially more precise quantum simula-
tion of fermions in the conﬁguration interaction representation.
Quantum Science and Technology, 3(1):015006, 2017.
[15] Ivan Kassal, Stephen P Jordan, Peter J Love, Masoud Mohseni,
and Al´an Aspuru-Guzik. Polynomial-time quantum algorithm
for the simulation of chemical dynamics. Proceedings of the
National Academy of Sciences, 105(48):18681–18686, 2008.
[16] Ian D Kivlichan, Nathan Wiebe, Ryan Babbush, and Al´an
Aspuru-Guzik. Bounding the costs of quantum simulation of
many-body physics in real space. Journal of Physics A: Math-
ematical and Theoretical, 50(30):305301, 2017.
[17] Borzu Toloui and Peter J Love.
Quantum algorithms for
quantum chemistry based on the sparsity of the ci-matrix. arXiv
preprint arXiv:1312.2579, 2013.
[18] Alberto Peruzzo, Jarrod McClean, Peter Shadbolt, Man-Hong
Yung, Xiao-Qi Zhou, Peter J Love, Al´an Aspuru-Guzik, and
Jeremy L Obrien. A variational eigenvalue solver on a photonic
quantum processor. Nature Communications, 5:4213, 2014.
[19] Jarrod R McClean, Jonathan Romero, Ryan Babbush, and Al´an
Aspuru-Guzik.
The theory of variational hybrid quantum-
classical algorithms. New Journal of Physics, 18(2):023023,
2016.
[20] Jarrod R McClean, Ryan Babbush, Peter J Love, and Al´an
Aspuru-Guzik. Exploiting locality in quantum computation for
quantum chemistry. The journal of Physical Chemistry Letters,
5(24):4368–4380, 2014.
[21] James D Whitﬁeld, Jacob Biamonte, and Al´an Aspuru-Guzik.
Simulation of electronic structure hamiltonians using quantum
computers. Molecular Physics, 109(5):735–750, 2011.
[22] Dave Wecker, Matthew B Hastings, and Matthias Troyer. Pro-
gress towards practical quantum variational algorithms. Phys-
ical Review A, 92(4):042303, 2015.
[23] Matthew B Hastings, Dave Wecker, Bela Bauer, and Matthias
Troyer. Improving quantum algorithms for quantum chemistry.
Quantum Information & Computation, 15(1-2):1–21, 2015.
[24] Oleksandr Kyriienko. Quantum inverse iteration algorithm for
near-term quantum devices. arXiv preprint arXiv:1901.09988,
2019.
[25] Pascual Jordan and Eugene P Wigner. About the pauli exclusion
principle. Z. Phys., 47:631–651, 1928.
[26] Sergey B Bravyi and Alexei Yu Kitaev. Fermionic quantum
computation. Annals of Physics, 298(1):210–226, 2002.
[27] Jacob T Seeley, Martin J Richard, and Peter J Love. The bravyi-
kitaev transformation for quantum computation of electronic
structure. The Journal of Chemical Physics, 137(22):224109,
2012.
[28] Andrew Tranter, Sarah Soﬁa, Jake Seeley, Michael Kaicher, Jar-
rod McClean, Ryan Babbush, Peter V Coveney, Florian Min-
tert, Frank Wilhelm, and Peter J Love. The bravyi-kitaev trans-
formation: Properties and applications. International Journal
of Quantum Chemistry, 115(19):1431–1441, 2015.
[29] Sergey Bravyi, Jay M Gambetta, Antonio Mezzacapo, and
Kristan Temme.
Tapering off qubits to simulate fermionic
hamiltonians. arXiv preprint arXiv:1701.08213, 2017.
[30] Ryan Babbush, Nathan Wiebe, Jarrod McClean, James Mc-
Clain, Hartmut Neven, and Garnet Kin-Lic Chan.
Low-
depth quantum simulation of materials.
Physical Review X,
8(1):011044, 2018.
[31] M-H Yung, Jorge Casanova, Antonio Mezzacapo, Jarrod Mc-
clean, Lucas Lamata, Alan Aspuru-Guzik, and Enrique Solano.
From transistor to trapped-ion computers for quantum chem-
istry. Scientiﬁc Reports, 4:3589, 2014.
[32] Jiangfeng Du, Nanyang Xu, Xinhua Peng, Pengfei Wang, San-
feng Wu, and Dawei Lu. Nmr implementation of a molecular
hydrogen quantum simulation with adiabatic state preparation.
Physical Review Letters, 104(3):030502, 2010.
[33] Zhaokai Li, Xiaomei Liu, Hefeng Wang, Sahel Ashhab, Jiangyu
Cui, Hongwei Chen, Xinhua Peng, and Jiangfeng Du. Quantum
simulation of resonant transitions for solving the eigenproblem
of an effective water hamiltonian.
Physical Review Letters,
122(9):090504, 2019.
[34] Pedram Roushan, Charles Neill, Anthony Megrant, Yu Chen,
Ryan Babbush, Rami Barends, Brooks Campbell, Zijun Chen,
Ben Chiaro, Andrew Dunsworth, et al.
Chiral ground-state
currents of interacting photons in a synthetic magnetic ﬁeld.
Nature Physics, 13(2):146, 2017.
[35] Benjamin P Lanyon, James D Whitﬁeld, Geoff G Gillett, Mi-
chael E Goggin, Marcelo P Almeida, Ivan Kassal, Jacob D Bia-
monte, Masoud Mohseni, Ben J Powell, Marco Barbieri, et al.
Towards quantum chemistry on a quantum computer. Nature
Chemistry, 2(2):106, 2010.
[36] Stefano Paesani, Andreas A Gentile, Raffaele Santagati, Jian-
wei Wang, Nathan Wiebe, David P Tew, Jeremy L OBrien, and
Mark G Thompson. Experimental bayesian quantum phase es-
timation on a silicon photonic chip. Physical Review Letters,
118(10):100503, 2017.
[37] Ya Wang, Florian Dolde, Jacob Biamonte, Ryan Babbush, Ville
Bergholm, Sen Yang, Ingmar Jakobi, Philipp Neumann, Al´an
Aspuru-Guzik, James D Whitﬁeld, et al. Quantum simulation


## Page 8


8
of helium hydride cation in a solid-state spin register. ACS nano,
9(8):7769–7774, 2015.
[38] Yangchao Shen, Xiang Zhang, Shuaining Zhang, Jing-Ning
Zhang, Man-Hong Yung, and Kihwan Kim. Quantum imple-
mentation of the unitary coupled cluster for simulating mo-
lecular electronic structure. Physical Review A, 95(2):020501,
2017.
[39] Cornelius Hempel, Christine Maier, Jonathan Romero, Jarrod
McClean, Thomas Monz, Heng Shen, Petar Jurcevic, Ben P
Lanyon, Peter Love, Ryan Babbush, et al. Quantum chemistry
calculations on a trapped-ion quantum simulator. Physical Re-
view X, 8(3):031022, 2018.
[40] Peter JJ OMalley, Ryan Babbush, Ian D Kivlichan, Jonathan
Romero, Jarrod R McClean, Rami Barends, Julian Kelly, Pe-
dram Roushan, Andrew Tranter, Nan Ding, et al.
Scalable
quantum simulation of molecular energies.
Physical Review
X, 6(3):031007, 2016.
[41] Abhinav Kandala, Antonio Mezzacapo, Kristan Temme, Maika
Takita, Markus Brink, Jerry M Chow, and Jay M Gambetta.
Hardware-efﬁcient variational quantum eigensolver for small
molecules and quantum magnets. Nature, 549(7671):242, 2017.
[42] Marc Ganzhorn, Daniel J Egger, P Barkoutsos, Pauline Ol-
litrault, Gian Salis, Nikolaj Moll, M Roth, A Fuhrer, P Mueller,
S Woerner, et al.
Gate-efﬁcient simulation of molecular ei-
genstates on a quantum computer. Physical Review Applied,
11(4):044092, 2019.
[43] Masoud Mohseni, Peter Read, Hartmut Neven, Sergio Boixo,
Vasil Denchev, Ryan Babbush, Austin Fowler, Vadim Smely-
anskiy, and John Martinis. Commercialize quantum technolo-
gies in ﬁve years. Nature News, 543(7644):171, 2017.
[44] Leonie Mueck. Quantum reform. Nature Chemistry, 7(5):361,
2015.
[45] Long Gui-Lu.
General quantum interference principle and
duality computer.
Communications in Theoretical Physics,
45(5):825, 2006.
[46] Stan Gudder. Mathematical theory of duality quantum com-
puters. Quantum Information Processing, 6(1):37–48, 2007.
[47] LONG Gui-Lu and Liu Yang.
Duality computing in
quantum computers. Communications in Theoretical Physics,
50(6):1303, 2008.
[48] Long Gui-Lu, Liu Yang, and Wang Chuan. Allowable gener-
alized quantum gates. Communications in Theoretical Physics,
51(1):65, 2009.
[49] Gui Lu Long. Duality quantum computing and duality quantum
information processing. International Journal of Theoretical
Physics, 50(4):1305–1318, 2011.
[50] Andrew M Childs and Nathan Wiebe. Hamiltonian simulation
using linear combinations of unitary operations. arXiv preprint
arXiv:1202.5822, 2012.
[51] Dominic W Berry, Andrew M Childs, Richard Cleve, Robin
Kothari, and Rolando D Somma. Simulating hamiltonian dy-
namics with a truncated taylor series. Physical Review Letters,
114(9):090502, 2015.
[52] Shi-Jie Wei and Gui-Lu Long. Duality quantum computer and
the efﬁcient quantum simulations. Quantum Information Pro-
cessing, 15(3):1189–1212, 2016.
[53] HuaiXin Cao, Li Li, ZhengLi Chen, Ye Zhang, and ZhiHua
Guo. Restricted allowable generalized quantum gates. Chinese
Science Bulletin, 55(20):2122–2125, 2010.
[54] Gui-Lu Long and Yang Sun. Efﬁcient scheme for initializing a
quantum register with an arbitrary superposed state. Physical
Review A, 64(1):014303, 2001.
[55] Patrick Rebentrost, Maria Schuld, Leonard Wossnig, Francesco
Petruccione, and Seth Lloyd. Quantum gradient descent and
newtons method for constrained polynomial optimization. New
Journal of Physics, 21(7):073023, 2019.
[56] Tao Xin, Shi-Jie Wei, Julen S Pedernales, Enrique Solano, and
Gui-Lu Long.
Quantum simulation of quantum channels in
nuclear magnetic resonance. Physical Review A, 96(6):062303,
2017.
[57] Shi-Jie Wei, Tao Xin, and Gui-Lu Long.
Efﬁcient univer-
sal quantum channel simulation in ibms cloud quantum com-
puter.
SCIENCE CHINA Physics, Mechanics & Astronomy,
61(7):70311, 2018.
[58] Maysum Panju. Iterative methods for computing eigenvalues
and eigenvectors. arXiv preprint arXiv:1105.1185, 2011.
V.
SUPPLEMENTAL MATERIAL
A.
Error estimation and iteration complexity
We analyse FQE’s convergence and estimate the approx-
imation error and iteration complexity [58]. Deﬁne |ψi⟩as
an normalized eigenvector for H ∈Rn×n with eigenvalue λi,
H|ψi⟩= λi|ψi⟩. Suppose that H has real and distinct eigenval-
ues set {λi} such that |λ1| > |λ2| > . . . > |λn|. We can express an
arbitrary state |ψ⟩as a linear combination of the eigenvectors
of H:
|ψ⟩= a1|ψ1⟩+ . . . + an|ψn⟩.
Deﬁne matrix Hg = I −γH and perform it on |ψ⟩, we have
Hg|ψ⟩= a1(1 −λ1)|ψ1⟩+ a2(1 −λ2)|ψ2⟩+ . . . + an(1 −λn)|ψn⟩
and so
(Hg)k|ψ⟩= a1(1 −γλ1)k|ψ1⟩+ c2(1 −γλ2)k|ψ2⟩
+ . . . + cn(1 −γλn)k|ψn⟩
= (1 −γλ1)k
a1|ψ1⟩+ a2
 (1 −γλ2)
(1 −γλ1)
!k
|ψ2⟩
+ . . . + an
 (1 −γλn)
(1 −γλ1)
!k
|ψn⟩

Since the eigenvalues are assumed to be real, distinct, and
ordered by decreasing magnitude, it follows that for all i =
2, . . . , n,
lim
k→∞
 (1 −γλi)
(1 −γλ1)
!k
= 0.
In the case of molecule Hamiltonian H, all of the eigenvalues
are less than 0. Note that |ψ1⟩is the ground state with ground
energy λ1. As k increases, (Hg)k|ψ⟩approaches the state a1(1−
λ1)k|ψ1⟩, and thus for large value of k,
|ψ1⟩≈
(Hg)k|ψ⟩
p
⟨ψ|(Hg)2k|ψ⟩
.


## Page 9


9
0
5
10 15 20 25 30 35 40 45
Iteration, k
1.145
1.140
1.135
1.130
1.125
Energy(hartree)
H2
Noiseless
Gaussian Noise
Random Noise
Exact Value
0
20
40
60
80
100
Iteration, k
7.95210
7.95205
7.95200
7.95195
7.95190
7.95185
7.95180
LiH
Noiseless
Gaussian Noise
Random Noise
Exact Value
0
50
100
150
Iteration, k
75.72
75.71
75.70
75.69
75.68
Energy(hartree)
H2O
Noiseless
Gaussian Noise
Random Noise
Exact Value
0
50
100
150
Iteration, k
56.06
56.05
56.04
56.03
56.02
56.01
56.00
55.99
NH3
Noiseless
Gaussian Noise
Random Noise
Exact Value
Figure 5: (a), (b), (c) and (d) show the gradient descent iteration process for
convergence of ground state energy of H2, LiH, H2O and NH3 respectively.
The qubit Hamiltonians of the four molecules are obtained by STO-6G basis,
which is more accurate than STO-3G basis.
The approximation error
ϵ = ⟨ψ|(Hg)kH(Hg)k|ψ⟩
⟨ψ|(Hg)k(Hg)k|ψ⟩−λ1
=
Pn
i=2 aiλi
 (1−γλi)
(1−γλ1)
k
Pn
i=1 ai
 (1−γλi)
(1−γλ1)
k
≤
 1 −γλ2
1 −γλ1
!k (n −1)a2λ2
a1
,
which decreases exponentially in the iteration depth k. If a
good initial state is chosen so that a1 is large, for instance HF
state, ϵ will be small in early iterations. With iteration increas-
ing, the state gets closer and closer to the ground |ψ1⟩. The
algorithm may be terminated at any point with a reasonable
accuracy ϵ to the ground state.
The rate of convergence primarily depends upon the ratio
of the two eigenvalues of largest absolute value. In the cir-
cumstance that the two largest eigenvalues have similar sizes,
the convergence will be slow in early stage. That case needs
special attention, and will not be discussed here.
B.
FQE with STO-6G basis as input
To make our method more plausible, we adopt STO-6G
basis sets to generate the qubit Hamiltonians of the four mo-
lecules. The noise parameters are as same as the parameters
in the maintext. The performance of our method is as same as
in STO-3G basis, shown in Fig.(5).
0
50
100
150
Iteration, k
1.135
1.130
1.125
1.120
Energy(hartree)
H2
Noiseless
Gaussian Noise
Random Noise
Exact Value
0
50
100
150
Iteration, k
7.862
7.860
7.858
7.856
7.854
LiH
Noiseless
Gaussian Noise
Random Noise
Exact Value
0
50
100
150
Iteration, k
75.00
74.99
74.98
74.97
74.96
Energy(hartree)
H2O
Noiseless
Gaussian Noise
Random Noise
Exact Value
0
50
100
150
Iteration, k
55.525
55.500
55.475
55.450
55.425
55.400
55.375
55.350
NH3
Noiseless
Gaussian Noise
Random Noise
Exact Value
Figure 6: Infulence of large noise on FQE in (a) H2, (b) LiH, (c) H2O and
(d) NH3 molecules respectively. The amplitude of the random noise is 0.1
and the Gaussian noise parameters are µ = 0, σ = 0.1/3.
C.
Performance of FQE with large noise
We show the performance of FQE in large noise situations.
As shown in Fig.(6), when random noise becomes large, FQE
will not converge to the ground state. Sometimes, it converges
to exited energy-levels, such as in H2O and NH3. In some
other situations, FQE behaves in a oscillation manner, such as
in H2 and LiH.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]