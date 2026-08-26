---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.11495v2
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1907.11495v2_Entanglement_detection_under_coherent_noise__Greenberger-Horne-Zeilinger-like_st

> Source: 1907.11495v2_Entanglement_detection_under_coherent_noise__Greenberger-Horne-Zeilinger-like_st.pdf

> Pages: 13

---


## Page 1


arXiv:1907.11495v2  [quant-ph]  22 Oct 2019
Entanglement detection under coherent noise: Greenberger-Horne-Zeilinger-like states
You Zhou1, ∗
1Center for Quantum Information, Institute for Interdisciplinary
Information Sciences, Tsinghua University, Beijing 100084, China
(Dated: October 23, 2019)
Entanglement is an essential resource in many quantum information tasks and entanglement
witness is a widely used tool for its detection. In experiments the prepared state generally deviates
from the target state due to some noise. Normally the white noise model is applied to quantifying
such derivation and in the same time reveals the robustness of the witness. However, there may
exist other kind of noise, in which the coherent noise can dramatically “rotate” the prepared state.
In this way, the coherent noise is likely to lead to a failure of the detection, even though the
underlying state is actually entangled. In this work, we propose an eﬃcient entanglement detection
protocol for N-partite Greenberger-Horne-Zeilinger (GHZ)-like states. The protocol can eliminate
the eﬀect of the coherent noise and in the same time feedback the corresponding noise parameters,
which are beneﬁcial to further improvements on the experiment system. In particular, we consider
two experiment-relevant coherent noise models, one is from the unconscious phase accumulation
on N qubits, the other is from the rotation on the control qubit. The protocol eﬀectively realizes
a family of entanglement witnesses by postprocessing the measurement results from N + 2 local
measurement settings, which only adds one more setting than the original witness specialized for
the GHZ state. Moreover, by considering the trade-oﬀbetween the detection eﬃciency and the
white-noise robustness, we further reduce the number of local measurements to 3 without altering
the performance on the coherent noise. Our protocol can enhance the entanglement detection under
coherent noises and act as a benchmark for the state-of-the-art quantum devices.
I.
INTRODUCTION
Entanglement, as a unique feature of quantum me-
chanics, plays an essential role in many quantum informa-
tion processing tasks, such as quantum teleportation [1],
quantum cryptography [2, 3], non-locality test [4], quan-
tum computing [5], quantum simulation [6] and quantum
metrology [7, 8]. Consequently, it is quite signiﬁcant to
detect entanglement in experimental systems, which not
only acts as benchmark and calibration of the underlying
platform, but also certiﬁes useful quantum resources for
the further information processing. So far, tremendous
eﬀorts have been devoted to the realization of multipar-
tite entanglement in various systems [9–19]. In particu-
lar, the genuine multipartite entanglement is witnessed in
14-ion-trap-qubit [9], 10-superconducting-qubit [12], and
12-photon-qubit systems [16], with the target state being
the Greenberger-Horne-Zeilinger (GHZ) state.
The detection of genuine multipartite entanglement is
generally a challenging task, since the dimension of the
Hilbert space increases exponentially with respect to the
system size.
Compared with the unfeasible quantum
state tomography [20, 21], the entanglement witness is
an useful tool to realize it [22, 23]. The witness is usually
a Hermitian operator W, satisfying that Tr(Wσs) ≥0
for all separable states σs ∈Ssep, with Ssep the separa-
ble state set; Tr(W|Ψ⟩⟨Ψ|) < 0 for some entangled state
|Ψ⟩, such as the GHZ state. Consequently, if W returns
a negative value, one can conﬁrm that the prepared state
∗zyqphy@gmail.com
is entangled; a non-negative value tells nothing, denoted
as a null result.
A straightforward way to construct a witness is based
on the intuition that the prepared state ρpre is entangled
if it is close to an entangled target state, say |Ψ⟩. To be
speciﬁc,
W = αI −|Ψ⟩⟨Ψ|,
(1)
where α is the maximal ﬁdelity between |Ψ⟩and all sep-
arable states σs, i.e., α = sup{⟨Ψ|σs|Ψ⟩|σs ∈Ssep}.
On account of the convexity of Ssep, α can be deter-
mined by the maximal Schmit coeﬃcient of |Ψ⟩opti-
mized under all bipartitions [24]. For instance, α =
1
2
for the GHZ state. The expectation value of W shows,
Tr(Wρpre) = α−Tr(|Ψ⟩⟨Ψ|ρpre), which is directly related
to measuring ﬁdelity.
Normally, the multipartite projector |Ψ⟩⟨Ψ| is decom-
posed with a few of local measurement settings (LMSs)
[25, 26], for example the Pauli operator σ⊗N
x
, which can
be realized in experiments. Even for one LMS, it needs
thousands of times of the measurement to obtain the esti-
mation of the expectation value. Thus, the total number
of LMSs characterize the eﬃciency of the witness. For
the GHZ state, it needs N + 1 LMSs [27]. On the other
hand, the robustness is another key feature of a witness,
which benchmarks its detection ability. Generally, one
applies white noise tolerance to characterize the robust-
ness, i.e.,
ρ = (1 −p)|Ψ⟩⟨Ψ| + p I
2N ,
(2)
which moves the target state towards the maximal mixed
state.
The maximal pmax such that Tr(Wρ) ≤0 de-
scribes the robustness of the witness.


## Page 2


2
Since the witness W shown in Eq. (1) is designed
speciﬁcally for the target state |Ψ⟩, it may return null re-
sults for some other entangled states. This phenomenon
may become serious when the experiment system suﬀers
from the coherent noise, i.e.,
|Ψpre⟩= Unoise|Ψ⟩.
(3)
Since the unitary evolution can ”rotate” the state dra-
matically (not like the translation in the white noise
case), the white noise tolerance corresponding to the re-
sult state can decrease, and is possibly outside the de-
tection range of the witness in some case. See Fig. 1 for
an illustration.
Taking the GHZ state as an example,
according to Eq. (1), the ﬁdelity-based witness shows,
WGHZ = 1
2I −|GHZ⟩⟨GHZ|,
(4)
where |GHZ⟩=
1
√
2(|0⟩⊗N + |1⟩⊗N).
If the prepared
state becomes |Ψpre⟩=
1
√
2(|0⟩⊗N −|1⟩⊗N) under some
coherent error that aﬀects the phase, the witness gives a
null result Tr(WGHZ|Ψpre⟩⟨Ψpre|) = 1
2 > 0. Note that
here |Ψpre⟩is entangled but one cannot conﬁrm this by
using the witness WGHZ in Eq. (4).
To the best of our knowledge, the entanglement de-
tection under realistic coherent noises still lacks study-
ing. The investigation along this direction can oﬀer us
two main advantages. On the one hand, it can supply
useful tools to tackle with coherent noises and hence en-
hance our entanglement detection ability; on the other
hand, it is also helpful to the benchmarking and even the
calibration of experimental systems.
This is beneﬁcial
for the ultimate goal—fault-tolerant quantum computa-
tion [5, 28], as the coherent noise leads to a much worse
threshold than the stochastic ones [29].
In this work, we study the entanglement detection un-
der coherent noises and focus on the GHZ state, which
is essential in many quantum information tasks, such as
Bell-nonlocality [4], multipartite quantum key distribu-
tion [30], quantum secret sharing [31, 32], and quantum
metrology [7, 8].
We show an entanglement detection
protocol that can eﬀectively eliminate the inﬂuence of
certain types of coherent noises for the GHZ state. Our
protocol only adds 1 LMS than the original one, which
needs N + 1 LMSs. In particular, the protocol can ef-
fectively realize a family of entanglement witnesses with
respective to the coherent noise, and one can select the
optimal one by only postprocessing the measurement re-
sults. The protocol can also help us to estimate corre-
sponding noise parameters and further give feedback to
the experiment system. Moreover, we also consider the
reduction of the number of LMSs, which makes the ex-
perimental realizations more eﬃcient.
Our paper is organized as follows. In Sec. II, two co-
herent noise models of the GHZ state are proposed, one
is generated by the unconscious phase accumulation on
N qubits, the other is due to the rotation on the con-
trol qubit. The overall noise model is the combination of
the coherent part and the white noise part. In Sec. III,
we show the detection protocol with N + 2 LMSs, used
to witness the entanglement under coherent noises and
further feed back the noisy parameters. In Sec. IV, we
further reduce the number of LMSs to 3, and propose
more eﬃcient witnesses.
Sec. V is the conclusion and
outlook.
GHZ
W
noise
U
GHZ
sep
s
0
³
0
<
y
y
FIG. 1. The eﬀect of the coherent noise and the failure of the
entanglement detection. The blue disk labels the convex sep-
arable state set Ssep, and the witness WGHZ is represented
by the right solid line (a hyperplane in the state space) that
is tangent to the disk. The white noise displaces the GHZ
state towards the witness line, and the length of this dotted
arrowed line can reveal the white noise tolerance. The red
curve, labeling the coherent noise, “rotates” the GHZ state
to some |Ψ⟩. Due to the coherent noise, the white noise tol-
erance with respective to WGHZ decreases, as shown by the
shortening of the dotted line. Finally, |Ψ⟩can moves to the
other side of the hyperplane, thus its entanglement cannot be
witnessed using WGHZ.
II.
THE NOISE MODEL
In this section, we show two realistic coherent noise
models of the GHZ state, which will be analysed in the
following Sec III. One is caused by the unconscious phase
accumulating on all qubits, the other is due to the single
qubit rotation on the ﬁrst control qubit.
Let us ﬁrst review the white noise model. Usually, one
uses the white noise to analyse the noise tolerance of the
entanglement witness, i.e., mixing the original state with
the maximally mixed state,
Φp(ρ) = (1 −p)ρ + p I
2N .
(5)
For the GHZ state, the resulting state is
ρp
w = (1 −p)|GHZ⟩⟨GHZ| + p I
2N .
(6)
The corresponding noise tolerance is determined by
Tr(WGHZρp
w) = 0 where WGHZ is deﬁned in Eq. (4),


## Page 3


3
and it equals to,
pmax = 2(N−1)
2N −1 (≃0.5, N →∞).
(7)
The white noise is generated by the depolarizing chan-
nel, and it eﬀectively displaces the original state |GHZ⟩
towards the maximally mixed state in the state space, as
shown in Fig. 1. However, generally speaking, the co-
herent noise could appear in the experiment due to some
system errors, as we illustrated in the following sections.
A.
Model 1: Unconscious phase accumulation
In experimental realizations, the degree of freedom of
N-qubit is generally encoded in N two-level subsystems,
such as the ground state and the excited state of atoms.
There might appear unconscious phase accumulation be-
tween |0⟩and |1⟩of qubits that dramatically transforms
the state. To be speciﬁc, this kind of coherent error can
be modeled as,
Uz =
N
O
j=1
U z
j ,
U z
j = |0⟩j⟨0| + eiφj|1⟩j⟨1|,
(8)
where U z
j denote the rotation around the Z-basis on the
j-th qubit. If we apply the above coherent noise on the
GHZ state, it shows
|Ψφ⟩= Uz|GHZ⟩
=
N
O
j=1
U z
j |GHZ⟩
=
1
√
2

|0⟩⊗N + ei PN
j=1 φj|1⟩⊗N
=
1
√
2(|0⟩⊗N + eiφ|1⟩⊗N),
(9)
where φ .= PN
j=1 φj. Similar as the white noise case, the
tolerance of WGHZ in Eq. (4) under this coherent noise
is determined by
Tr(WGHZ|Ψφ⟩⟨Ψφ|) = −cosφ
2
< 0
(10)
which leads to φ ∈(−π
2 , π
2 ). Thus if the absolute value
of the phase |φ| ≥π
2 , the witness WGHZ cannot properly
detect the entanglement, while the prepared state |Ψφ⟩
is clearly an entangled one.
More generally, the realistic noise can be the combina-
tion of the white noise part Φp and the coherent part Uz,
thus the output state shows,
ρpre = Φp ◦Uz(|GHZ⟩⟨GHZ|)
= (1 −p)|Ψφ⟩⟨Ψφ| + p I
2N ,
(11)
where Uz(·) = Uz · U †
z, and note that Φp ◦Uz = Uz ◦Φp.
In this joint noise model, the noise tolerance range is
determined by Tr(WGHZρpre) < 0 with ρpre in Eq. (11).
The result is given by the following formula including the
coherent and white noise parameters φ and p,
cos φ >
p
1 −p,
(12)
as N →∞. The detailed derivation is left in Appendix
A. Comparing to Eq. (10), Eq. (12) shows that the range
of φ shrinks due to the introduction of white noise. On
the other hand, Eq. (12) can be rewritten as follows,
p < 1 −
1
cos φ + 1.
(13)
It indicates that the range of the white noise parameter
p also decreases on account of the coherent noise, com-
paring to Eq. (7).
B.
Model 2: Rotation on the ﬁrst control qubit
The GHZ state is normarlly generated by the following
circuit routine, as shown in Fig. 2.
• Initialize all the N qubits to be |0⟩.
• Apply a Hardmard gate H on the ﬁrst (control)
qubit, and transform it to |+⟩= 1
2(|0⟩+ |1⟩).
• Apply Controled-NOT (CNOT) gate on qubit pairs
(1, 2), (2, 3), (3, 4), · · ·(j, j + 1) · · · · · · (N −1, N) in
sequence, where j is the control qubit and j + 1 is
the target qubit.
It is clear to see that the CNOT gate sequence spreads
the superposition information of the ﬁrst qubit to all the
qubits, and thus builds the quantum correlation on the
whole system. Hence, the quality of the rotation on the
ﬁrst qubit signiﬁcantly aﬀects the preparation of the ﬁnal
GHZ state.
Suppose besides the ideal H gate, there is also another
uncontrolled unitary on the ﬁrst qubit, i.e.,
|ψ⟩1 = U1H1|0⟩1 = cos θ|0⟩1 + eiφ sin θ|1⟩1,
(14)
with θ ∈[0, π
2 ] and φ ∈[−π, π). Here the overall unitary
U ′
1 = U1H1 in principle can be any single qubit unitary,
thus |ψ⟩1 describes any single qubit state after ignoring
the irrelevant global phase. In addition, we also allow
the unconscious phase accumulation on the state at the
ﬁnal stage.
Consequently, the ﬁnal prepared state shows,
Ψθ
φ
E
= cos θ|0⟩⊗N + eiφ sin θ|1⟩⊗N,
(15)
where the accumulated phase at the ﬁnal stage is also
dropped into the parameter φ without confusion. Note
that the noisy state
Ψθ
φ
E
in Eq. (15) is more general


## Page 4


4
0
0
H
0
1
U
1 '
U
0
Zf
Zf
Zf
Zf
{
FIG. 2. The quantum circuit to generate the 4-qubit GHZ
state and the coherent noise on the 1st control qubit. The
overall noisy unitary is denoted by U ′
1 = U1H1. Note that
at the end of the circuit, we also allow the Z-basis phase
accumulation Zφ where φ needs not to be the same for each
qubit.
than |Ψφ⟩in Eq. (9), since
Ψθ
φ
E
allows unbalanced state
coeﬃcients besides the relative phase.
The noise tolerance of WGHZ in Eq. (4) under this
coherent noise is determined by
Tr(WGHZ
Ψθ
φ
ED
Ψθ
φ
) = 1
2 −1
2[1 + sin(2θ) cos(φ)] < 0
(16)
that is, sin(2θ) cos(φ) > 0, which leads to φ ∈(−π
2 , π
2 ).
As in Sec. II A, one can also consider the combination
of the coherent noise and the white noise, and the ﬁnal
state shows,
ρpre = (1 −p)
Ψθ
φ
ED
Ψθ
φ
 + p I
2N ,
(17)
Accordingly, the tolerance of WGHZ in this scenario
when N →∞shows,
sin(2θ) cos(φ) >
p
1 −p.
(18)
The detailed derivation is left in Appendix A. Compar-
ing to Eq. (12), one can see that the noise tolerance range
decreases further, after the introduction of the noise pa-
rameter θ. In addition, Eq. (18) can be rewritten as,
p < 1 −
1
sin(2θ) cos(φ) + 1,
(19)
and it is worse than Eq. (7) and (13). See Fig. 3 for an
illustration.
III.
ENTANGLEMENT DETECTION
PROTOCOL UNDER COHERENT NOISE
As shown in Sec. II, the witness WGHZ specialized for
the GHZ state potentially returns a null result when the
prepared state suﬀers from some coherent noise. Here
0
0.1
0.2
0.3
0.5
p
TUOYKZURKXGTIK
f
2
p
- 2
p
4
p
- 4
p
= 4
p
q
3
= 16
p
q
=16
p
q
= 8
p
q
p
-p
3
4
p
3
- 4
p
FIG. 3. The decrease of the noise tolerance range after in-
troducing coherent noises, as shown in Eq. (19). We plot the
white noise parameter p as a function of φ for diﬀerent θ. The
area under the curve labels the parameter region where the
corresponding state can be detected by the witness WGHZ in
Eq. (4). For the top (blue) curve with θ =
π
4 , one can see
that p decreases for larger coherent noisy parameter φ. Af-
ter further introducing the parameter θ, the noise tolerance
decreases further as θ departs from π
4 .
we propose an entanglement detection protocol that can
eliminate the eﬀect of coherent noises shown in the above
section. The protocol only involves N + 2 LMSs, which
only adds one LMS comparing to the previous witness
WGHZ specialized for the GHZ state [27].
Since the resulting state of noise model 2 in Sec II B
is more general than that of model 1 in Sec II A, for
clearness, in the following we ﬁrst apply the entanglement
detection protocol on the model 1, and then generalize it
to the model 2.
A.
Detection protocol under noise model 1
The protocol measures the ﬁdelity between ρpre and
|Ψφ⟩in Eq. (9) for any phase parameter φ with the same
N + 2 LMSs. As a result, one can eﬀectively detect the
entanglement by choosing the optimal witness in the fam-
ily,
WΨφ = 1
2I −|Ψφ⟩⟨Ψφ|,
(20)
by postprocessing the measurement results. See Fig. 4
for an illustration. Hereafter qubit Pauli operators are
denoted by {σx, σy, σz}, and we summarize the result
into the following Theorem.
Theorem 1. The family of witnesses WΨφ parameter-
ized by φ in Eq. (20) can be realized with totally N + 2
LMSs, i.e., σ⊗N
z
and
Mθk = (cos θkσx + sin θkσy)⊗N ,
(21)


## Page 5


5
Wy
noise
U
GHZ
0
<
0
³
sep
s
0
<
0
³
GHZ
W
y
FIG. 4. The illustration of the entanglement detection pro-
tocol. The blue disk labels the separable state set Ssep, and
the witness WGHZ is represented by the right solid line. The
length of this dotted arrowed line can reveal the white noise
tolerance.
The red curve, labeling the coherent noise, “ro-
tates” the GHZ state to some |Ψ⟩. Here we eﬀectively realize
a family of witnesses WΨ as shown in Eq. (20) and (29), and
select the optimal one by postprocessing the measurement
results. Comparing to the situation in Fig. 1, the protocol
makes the entanglement detection possible again.
where θk =
kπ
N+1 and k = 0, 1, · · · , N.
Proof. The projector |Ψφ⟩⟨Ψφ| can be written as,
|Ψφ⟩⟨Ψφ| = Z + X,
(22)
where Z denotes the summation of diagonal terms, i.e.,
Z =1
2(|0⟩⟨0|⊗N + |1⟩⟨1|⊗N),
(23)
and X is for oﬀ-diagonal terms
X = cos φX+ + sin φX−,
(24)
where
X+ = |0⟩⟨1|⊗N + |1⟩⟨0|⊗N
2
,
X−= |0⟩⟨1|⊗N −|1⟩⟨0|⊗N
2i
.
(25)
The diagonal part Z can be measured with the LMS
σ⊗N
z
. The oﬀ-diagonal part X+ and X−involved in X can
be further decomposed with LMSs Mθk given in Eq. (21)
as,
X+ =
1
N + 1
N
X
k=0
(−1)k cos(θk)Mθk
X−=
−1
N + 1
N
X
k=0
(−1)k sin(θk)Mθk.
(26)
The proof of these decompositions is based on discrete
Fourier transform, and we leave it in Appendix B.
To eliminate the eﬀect of the coherent noise due to
the unconscious phase accumulation, one should maxi-
mize the ﬁdelity between the prepared state ρpre and all
possible |Ψφ⟩based on measurement results, that is,
max
φ
⟨Ψφ|ρpre|Ψφ⟩= ⟨Z⟩+ max
φ ⟨X⟩
= ⟨Z⟩+ max
φ
{cos φ⟨X+⟩+ sin φ⟨X−⟩}
= ⟨Z⟩+
p
⟨X+⟩2 + ⟨X−⟩2,
(27)
where ⟨·⟩denotes the expectation value of the corre-
sponding operator on ρpre, and in the ﬁnal line we apply
the Cauchy-Schwarz inequality. Note that ⟨Z⟩and ⟨X±⟩
can be obtained from LMS σz and {Mθk}N
k=0, respec-
tively. The optimal φopt to saturate the maximal value
in Eq. (27) is determined by
tan φopt = ⟨X−⟩
⟨X+⟩
= −
PN
k=0(−1)k sin(θk)⟨Mθk⟩
PN
k=0(−1)k cos(θk)⟨Mθk⟩
.
(28)
where the second line is on account of Eq. (26),
and (cos φopt, sin φopt) is in the same quadrant with
(⟨X+⟩, ⟨X−⟩).
For instance, for the noisy state shown in Eq. (11),
one can eﬀectively choose the corresponding witness in
Eq. (20) to eliminate the eﬀect of the coherent noise and
detect the entanglement. Note that the parameter φopt is
determined by the measurement results. It is clear that
the noise tolerance now is the same as in the sole white
noise case, pmax in Eq. (7), no matter what value φ is.
Moreover, this protocol can further help to improve the
experiment system. That is, one can apply an reverse
unitary to amend the system according to the optimal
φopt abstracted from the measurement results. In par-
ticular, one can add a corresponding Z-basis rotation on
any qubit to eliminate the error.
B.
Detection protocol under noise model 2
In this section, we generalize the entanglement detec-
tion protocol proposed in Sec. III A and apply it to the
noise model 2.
The main strategy is similar, and here we realize the
following family of witnesses with the same N + 2 LMSs.
WΨθ
φ = max{cos2 θ, sin2 θ}I −
Ψθ
φ
ED
Ψθ
φ
,
(29)
where max{cos2 θ, sin2 θ} is the maximal Schmidt coeﬃ-
cient of
Ψθ
φ
E
deﬁned in Eq. (15). One can further choose
the optimal witness in the family by post-processing the
measurement results. We summarize this into the follow-
ing Theorem.


## Page 6


6
Theorem 2. The family of witnesses WΨθ
φ parameter-
ized by φ and θ in Eq. (29) can be realized with totally
N+2 LMSs, i.e., σ⊗N
z
and {Mθk}N
k=0 deﬁned in Eq. (21).
Proof. As in Eq. (22), the projector
Ψθ
φ
ED
Ψθ
φ
 can be
decomposed as follows,
Ψθ
φ
ED
Ψθ
φ
 = cos2 θZ0 + sin2 θZ1 + sin(2θ)X,
(30)
where Z0 and Z1 denote |0⟩⟨0|⊗N and |1⟩⟨1|⊗N, whose
expectation values can be evaluated from the LMS σ⊗N
z
;
X is given by Eq. (24) and (25), whose expectation value
can be obtained from LMSs {Mθk}N
k=0, as shown in
Eq. (26).
Similar as Sec. III A, we should ﬁnd the maximal ﬁ-
delity between the prepared state and all possible
Ψθ
φ
E
based on the measurement results,
max
φ,θ
D
Ψθ
φ
ρpre
Ψθ
φ
E
= max
φ,θ
n
cos2 θ⟨Z0⟩+ sin2 θ⟨Z1⟩+
sin(2θ)(cos φ⟨X+⟩+ sin φ⟨X−⟩)
o
= max
θ
n
cos2 θ⟨Z0⟩+ sin2 θ⟨Z1⟩+ sin(2θ)
p
⟨X+⟩2 + ⟨X−⟩2
o
= max
θ
n⟨Z0⟩+ ⟨Z1⟩
2
+ cos(2θ)⟨Z0⟩−⟨Z1⟩
2
+
sin(2θ)
p
⟨X+⟩2 + ⟨X−⟩2
o
= ⟨Z0⟩+ ⟨Z1⟩
2
+
r
1
4(⟨Z0⟩−⟨Z1⟩)2 + ⟨X+⟩2 + ⟨X−⟩2.
(31)
Here the maximization on the parameters φ and θ can
be conducted independently. In the second line, we take
the optimal φopt given by Eq. (28). The last line is due
to the Cauchy-Schwarz inequality, and the optimal θopt
takes the value,
tan(2θopt) = 2
p
⟨X+⟩2 + ⟨X−⟩2
⟨Z0⟩−⟨Z1⟩
,
(32)
with [cos(2θopt), sin(2θopt)] being in the same quadrant
with
h
⟨Z0⟩−⟨Z1⟩, 2
p
⟨X+⟩2 + ⟨X−⟩2
i
.
Then one can
choose the optimal witness in the family of Eq. (29) to
detect the entanglement, based on the ﬁdelity maximiza-
tion in Eq. (31) and the associated optimal parameters
φopt and θopt.
For instance, for the noisy state in Eq. (17), it is not
hard to see that the noise tolerance shows
p < min{cos2 θopt, sin2 θopt},
(33)
with N →∞, no matter what value φ is. The detailed
derivation is left in Appendix A. Note that the white
noise tolerance is still a function of θ, even if one can ob-
tain its value by postprocessing. The reason is because
the parameter θ, not like φ, indeed aﬀects the entangle-
ment.
On the other hand, one can also choose the optimal
witness in the family of Eq. (20) in Sec. III A on the
noise model 2 here. Since the optimization in Eq. (27)
can help to determine the corresponding noise parameter
φopt, the optimal witness shows,
WΨφopt = 1
2I −
Ψφopt

Ψφopt
.
(34)
As a result, for the noisy state in Eq. (17), the corre-
sponding white noise tolerance reads (see Appendix A
for the derivation),
p < 1 −
1
sin(2θ) + 1.
(35)
which shows a clear advantage comparing to Eq. (19)
with the original witness WGHZ.
Note that the term
cos(φ) is eliminated due to the postprocessing. Surpris-
ingly, the white noise tolerance in Eq. (35) is better than
the one in Eq. (33), as illustrated in Fig. 5. We give a
detailed comparison in Appendix C. The reason for this
phenomenon may be as follows. By using the family of
witnesses in Eq. (29), one maximizes the ﬁdelity between
Ψθ
φ
E
and the prepared state. However, the correspond-
ing ﬁdelity bound in the witness for the separable state,
i.e., max{cos2 θ, sin2 θ}, becomes larger and harder to vi-
olate.
0.5
0.4
0.3
0.2
0.1
0
p
TUOYKZURKXGTIK
q
2
p
4
p
8
p
3
8
p
+W
+W
FIG. 5. Comparison between the white noise tolerances in
Eq. (33) and (35). They are tolerances of the optimal witness
in Eq. (29) and Eq. (20) for the noisy state in Eq. (17), respec-
tively. Both of them increase and reach the maximal value 0.5
at θ = π/4, then decrease, since at this point the state co-
eﬃcients are balanced and the state possesses the maximal
entanglement. Except θ = 0, π/4, π/2, Eq. (35) always shows
a clear advantage to Eq. (33).
The entanglement detection protocol under the noise
model 2 employs the same set of N + 2 LMSs as that in
Sec. III A, but abstracts both noise parameters φopt and
θopt. This is because here we postprocess measurement
results more delicately. Even though the white noise tol-
erance of the corresponding witness in Eq. (29) is not bet-
ter than the one in Eq. (20), the experiment system can


## Page 7


7
be further improved with the noise parameters φopt and
θopt extracted from the measurement results. In partic-
ular, one can add an unitary U †
1 on the ﬁrst qubit when
preparing the GHZ state, which can be determined by
φopt and θopt.
IV.
ENTANGLEMENT DETECTION WITH
LESS LMS
In entanglement detection, the number of LMSs usu-
ally determines the eﬃciency of the witness, since even
for one setting it could take thousands of measurements
to obtain the accurate estimation of the expectation
value.
Thus, it is beneﬁcial to reduce the number of
LMSs and enhance the eﬃciency of the witness. In this
section, by utilizing the stabilizer formulation, we show
that one can detect entanglement of GHZ-like states with
only 3 LMSs under realistic coherent noises.
Comparing to the witness WGHZ using N + 1 LMSs
in Eq. (4), there is a more eﬃcient witness using 2 LMSs
[33], i.e.,
W2
GHZ = 1
2I −Z −1
4σ⊗N
x
,
(36)
where Z is deﬁned in Eq. (23). However, there is a trade-
oﬀbetween the eﬃciency and the white noise tolerance
[27, 34]. For the target GHZ state, the white noise tol-
erance of W2
GHZ is p =
1
3 as N →∞[33], while the
tolerance is p = 1
2 of WGHZ. Note that W2
GHZ employs
two settings, i.e., σ⊗N
z
and σ⊗N
x
.
In the following, we study the entanglement detection
under coherent noises with less LMSs, by adding another
LMS σy ⊗σ⊗N−1
x
to σ⊗N
z
and σ⊗N
x
. Actually, the σy
operator can be on any qubit due to the symmetry of
GHZ-like states.
With loss of generality, we set it on
the ﬁrst qubit. Similar as Sec. III, we ﬁrst consider the
entanglement detection under noise model 1, then noise
model 2 that contains more possible noisy states.
A.
Eﬃcient detection under noise model 1
We extend the witness W2
GHZ in Eq. (36) to a family
of witnesses, parameterized by the noisy parameter φ.
Similar as Sec. III A, one can eﬀectively detect entangle-
ment under the coherent noise by choosing the optimal
witness in this family, by postprocessing the measure-
ment results. We summarize the result in the following
theorem.
Theorem 3. The witness W2
Ψφ can detect entanglement
near the state |Ψφ⟩,
W2
Ψφ = 1
2I −Z −1
4(cos φMx + sin φM′
x),
(37)
where Z is deﬁned in Eq. (23), Mx = σ⊗N
x
, and M′
x =
σy ⊗σ⊗N−1
x
.
It is clear that the family of witness {W2
Ψφ} parame-
terized by φ can be realized by 3 LMSs, σ⊗N
z
, σ⊗N
x
, σy ⊗
σ⊗N−1
x
.
Proof. As given in Eq. (9), the possible state under the
coherent noise shows |Ψφ⟩=
1
√
2(|0⟩⊗N + eiφ|1⟩⊗N), and
it can be transformed from the standard GHZ state by
applying a single qubit unitary,
|Ψφ⟩= U z
1 ⊗I⊗N−1|GHZ⟩,
(38)
where U z
1 = |0⟩1⟨0| + eiφ|1⟩1⟨1| = eiφ/2e−iσzφ/2. For the
density matrix, one has the relation Ψφ = U z
1 GHZU z†
1 .
Since the witness W2
GHZ can detect entanglement near
the GHZ state, we have the following witness that can
detect entanglement near |Ψφ⟩based on Observation 1,
Wφ
2 = U z
1 W2
GHZU z†
1
= 1
2I −Z −1
4(e−iσzφ/2σxeiσzφ/2) ⊗σ⊗N−1
x
,
= 1
2I −Z −1
4(cos φσx + sin φσy) ⊗σ⊗N−1
x
.
(39)
In this way, we obtain a family of entanglement witnesses
parameterized by the phase φ, and they all need 2 LMSs,
i.e. σ⊗N
z
and (cos φσx−sin φσy)⊗σ⊗N−1
x
. In fact, one can
realize these witnesses with only 3 LMSs, Mz = σ⊗N
z
,
Mx = σ⊗N
x
and M′
x = σy ⊗σ⊗N−1
x
, since the result of
(cos φσx−sin φσy)⊗σ⊗N−1
x
can be obtained by the linear
combination of Mx and M′
x.
Observation 1. Suppose an entanglement witness W
can detect a entangled state ρ, i.e., Tr(Wρ) < 0 and
Tr(Wσs) ≥0, ∀σs ∈Ssep, the state ρ′ = UlocρU †
loc after
the transformation with local unitary operation Uloc can
be detected by the corresponding witness
W′ = UlocWU †
loc
(40)
where Uloc = U1 ⊗U2 · · · UN and Ui is the unitary on the
i-th qubit.
Proof. Note that ρ′ is still an entangled state, as local
unitary operations does not alter entanglement prop-
erty. Tr(W′ρ′) = Tr(UlocWU †
locUlocρU †
loc) = Tr(Wρ) <
0.
In addition, Tr(W′σsep) = Tr(UlocWU †
locσsep) =
Tr(WU †
locσsepUloc) ≥0, since U †
locσsepUloc is still a sepa-
rable state.
To eliminate the eﬀect of the coherent noise, similar as
Eq. (27), one should ﬁnd the minimal expectation value
of all the witnesses in the family, i.e., minφ Tr(W2
Ψφρpre).
Equivalently,
max
φ {cos φ⟨Mx⟩+ sin φ⟨M′
x⟩}.
(41)
The optimal φ is determined by
tan φopt = ⟨M′
x⟩
⟨Mx⟩.
(42)


## Page 8


8
and (cos φopt, sin φopt) is in the same quadrant with
(⟨Mx⟩, ⟨M′
x⟩).
For instance, for the noisy state shown in Eq. (11),
one can eﬀectively choose the corresponding witness in
Eq. (37) to detect entanglement. Now the noise tolerance
is the same as in the sole white noise case, i.e., p = 1
3
as N →∞, no matter what value φ is.
In addition,
this protocol can further help to improve the experiment
system by applying an correcting unitary according to
the optimal φopt.
B.
Eﬃcient detection under noise model 2
We further extend the witness W2
GHZ in Eq. (36) to a
family of witnesses, and have the following theorem.
Theorem 4. The witness W2
Ψθ
φ can detect entanglement
near the state
Ψθ
φ
E
,
W2
Ψθ
φ =2 max{cos2 θ, sin2 θ} + 1
4
I −Z
−1
4 cos(2θ)Mz −1
4 sin(2θ)(cos φMx + sin φM′
x),
(43)
where Z is deﬁned in Eq. (23), Mz = σz ⊗I⊗N−1, Mx =
σ⊗N
x
, and M′
x = σy ⊗σ⊗N−1
x
.
It is clear that in general
Ψθ
φ
E
can not be transformed
from the standard GHZ state by local unitary operations.
Thus, we cannot prove Theorem 4 with the approach
used in Theorem 3, and the following proof is based on
the generalized stabilizer formula.
Proof. The GHZ state is a stabilizer state that is uniquely
determined by the following N independent stabilizer op-
erators,
S1 = σ⊗N
x
, S2 = σ1
zσ2
z, S3 = σ2
zσ3
z, · · · , SN = σN−1
z
σN
z
(44)
and the witness W2
GHZ in Eq. (36) can be equivalently
written as,
2W2
GHZ = 3
2I −(P1 + P2)
(45)
with P1 and P2 two projectors determined by the stabi-
lizers,
P1 = I + S1
2
= I + σ⊗N
x
2
,
P2 =
N
Y
i=2
I + Si
2
≡2Z.
(46)
Due to the fact (I −P1)(I −P2) ≥0, one has
|GHZ⟩⟨GHZ| = P1P2 ≥(P1 + P2 −I),
(47)
As a result, the witness W2
GHZ is valid since 2W2
GHZ ≥
WGHZ given in Eq. (4) [33].
In the following, we construct the witness W2
Ψθ
φ in
Eq (43) by ﬁnding generalized stabilizers of
Ψθ
φ
E
. Here
“generalized” means that the stabilizer may be not in the
Pauli tensor form.
It is not hard to see that the last N −1 stabilizers
S2, S3, · · · SN in Eq (44) also stabilize
Ψθ
φ
E
. Thus, we
only need to ﬁnd the ﬁrst updated one S′
1.
The con-
struction is based on the following fact: if S stabilizes
|Ψ⟩, i.e., S|Ψ⟩= |Ψ⟩, USU † stabilizes U|Ψ⟩. Note that
Ψθ
φ
E
can be prepared from the noisy circuit described in
Fig. 2.
Initially, the stabilizers of the product state |0⟩⊗N is
σ1
z, σ2
z, · · · , σN
z ; after the single qubit unitary on the ﬁrst
qubit, σ1
z becomes
U ′
1σ1
zU ′†
1 = cos(2θ)σ1
z + sin(2θ)
 cos φσ1
x + sin φσ1
y

;
(48)
ﬁnally, after the successive application of CNOT gates,
the stabilizer shows,
S′
1 = UCNOT U ′
1σ1
zU ′†
1 U †
CNOT
(49)
where UCNOT
=
[CN−1XN] · · · [C2X3][C1X2] is the
CNOT gate sequence, with CiXj denoting the CNOT
gate on the qubit j controlled by the qubit i. One can
ﬁnd that
S′
1 = cos(2θ)σ1
z ⊗I⊗N−1+
sin(2θ)
 cos φσ⊗N
x
+ sin φσ1
y ⊗σ⊗N−1
x

(50)
on account the following relations,
CiXjσi
xCiXj = σi
xσj
x,
CiXjσi
yCiXj = σi
yσj
x,
CiXjσi
zCiXj = σi
z.
(51)
Similar as Eq. (46), we can deﬁne two projectors P ′
1
and P ′
2 associated with the stabilizers of the state
Ψθ
φ
E
,
that is, P ′
1 = 1
2(I + S′
1) and P ′
2 = P2. Then based on the
witness WΨθ
φ in Eq. (29), we have the new witness with
less LMSs,
W2
Ψθ
φ = 1
2

(max{cos2 θ, sin2 θ} + 1)I −(P ′
1 + P ′
2)

= 2 max{cos2 θ, sin2 θ} + 1
4
I −Z −1
4S′
1,
(52)
with S′
1 given in Eq. (50). Similar as Eq. (47), one can
verify 2W2
Ψθ
φ ≥WΨθ
φ and the witness W2
Ψθ
φ is valid.
Similar as Sec. IV A, one should ﬁnd the minimal
expectation value of all the witnesses in the family of


## Page 9


9
Eq. (43), i.e., minφ,θ Tr(W2
Ψθ
φρpre), parameterized by φ
and θ. Equivalently,
max
φ,θ {cos(2θ)⟨Mz⟩+ sin(2θ)(cos φ⟨Mx⟩+ sin φ⟨M′
x⟩)}
=
p
⟨Mz⟩2 + ⟨Mx⟩2 + ⟨M′x⟩2
(53)
The optimal φopt to saturate the maximal value is given
in Eq. (42), and the optimal θopt satisﬁes
tan(2θopt) =
p
⟨Mx⟩2 + ⟨M′x⟩2
⟨Mz⟩
,
(54)
and [cos(2θopt), sin(2θopt)] is in the same quadrant with

⟨Mz⟩,
p
⟨Mx⟩2 + ⟨M′x⟩2

.
Consequently, one can choose the optimal witness in
the family of Eq. (43) to detect the entanglement, based
on the associated optimal parameters φopt and θopt. For
instance, for the noisy state shown in Eq. (17), the cor-
responding white noise tolerance shows,
p < 2
3 min{cos2 θopt, sin2 θopt},
(55)
for N →∞no matter what value φ is, and the proof is
left in Appendix D.
On the other hand, similar as the discussion at the end
of Sec. III B, one can also apply the detection protocol
given in Sec. IV A on the noise model 2 here. That is,
using the optimal witness in the family of Eq. (37). The
optimization in Eq. (41) can determine the corresponding
noise parameter φopt and thus the optimal witness. For
the noisy state in Eq. (17), the corresponding white noise
tolerance reads,
p < 1 −
2
sin(2θ) + 2.
(56)
as N →∞. The proof is also left in Appendix D. Similar
as the comparison at the end of Sec. III B, the white noise
tolerance in Eq. (56) is better than the one in Eq. (55).
The eﬃcient detection protocol under the noise model
2 employs the same set of 3 LMSs as the one in Sec. IV A,
but abstracts both noise parameters φopt and θopt. This is
because here we post-process measurement results more
delicately. Even though the white noise tolerance of the
corresponding witness in Eq. (55) is not better than the
one in Eq. (56), the experiment system can be further im-
proved with the noise parameters φopt and θopt extracted
from the measurement results.
V.
CONCLUSION AND OUTLOOK
In this paper, by focusing on GHZ-like states, we pro-
pose an entanglement detection protocol to enhance the
detection ability under some practical coherent noises,
which only adds one LMS comparing to the original wit-
ness method. Our protocol can feedback the noisy pa-
rameters by postprocessing and further help to improve
the experimental system. The main idea behind the pro-
tocol is that we construct a set of measurements which
can tomography all possible states aﬀected by the co-
herent noise, and thus realize a family of entanglement
witnesses.
In addition, we further reduce the number
of LMSs to 3, which makes the experimental realization
more eﬃcient.
There are a few prospective problems that can be ex-
plored in the future. First, it is shown in the paper that
even if one can obtain more parameters about the pre-
pared state by delicate postprocessing, it may be not
beneﬁcial to the entanglement detection as shown by the
noise tolerance comparison in Fig. 5. Thus it is signiﬁcant
to investigate further whether it is a general phenomenon.
Second, it is interesting to extend the current protocol to
more general states, such as permutation-invariant states
[35, 36] and stabilizer states [5, 28], where quantum er-
ror correction or mitigation methods can be applied to
eliminate or reduce the eﬀect of coherent noises. Third,
it is also intriguing to study the entanglement detection
under other types of coherent noises, which appear in cer-
tain experimental systems. In addition, the detection of
more detailed multipartite entanglement structures [37–
39] under coherent noises is signiﬁcant to investigate.
ACKNOWLEDGMENTS
We thank Chenghao Guo, Xiongfeng Ma and Qi
Zhao for the insightful discussions.
This work was
supported by the National Natural Science Founda-
tion of China Grants No. 11875173 and No. 11674193,
and the National Key R&D Program of China Grant
No. 2017YFA0303900.
Appendix A: Derivation of miscellaneous noise
tolerances in Eq. (12), (18) , (33) and (35)
First, let us focus on Eq. (12) and (18), which are noise
tolerances of WGHZ in Eq. (4) for the noise model 1 and
2 respectively. Since the noisy state in Eq. (17) is more
general than that in Eq. (11), we only show the derivation
of Eq. (18) here.
Tr(WGHZρpre) = Tr
( 1
2I −|GHZ⟩⟨GHZ|


(1 −p)
Ψθ
φ
ED
Ψθ
φ
 + p I
2N
 )
= 1
2 −(1 −p)|⟨GHZ|Ψθ
φ⟩|2 −p
2N
= 1
2 −1 −p
2
[1 + sin(2θ) cos(φ)] −p
2N < 0.
(A1)


## Page 10


10
As N →∞, one has
sin(2θ) cos(φ) >
p
1 −p.
(A2)
Then, let us consider Eq. (33), which is the tolerance
of the optimal witness in Eq. (29) for the noisy state
in Eq. (17). Since the ﬁdelity optimization in Eq. (31)
helps us to determine the parameters φ and θ of the pre-
pared state in Eq. (17), one can choose the witness with
the same parameters in Eq. (29) and the noise tolerance
shows,
Tr(WΨθ
φρpre) = Tr
( h
max{cos2 θ, sin2 θ}I −
Ψθ
φ
ED
Ψθ
φ

i

(1 −p)
Ψθ
φ
ED
Ψθ
φ
 + p I
2N
 )
= max{cos2 θ, sin2 θ} −(1 −p) −p
2N < 0.
(A3)
As N →∞, one has
p < 1 −max{cos2 θ, sin2 θ} = min{cos2 θ, sin2 θ}. (A4)
Finally, let us derive Eq. (35), which is the tolerance
of the optimal witness in Eq. (20) for the noisy state
in Eq. (17). Since the ﬁdelity optimization in Eq. (27)
helps us to determine the parameter φ of the prepared
state in Eq. (17), one can choose the witness with the
same parameter φ in Eq. (20) and the noise tolerance
shows,
Tr(WΨφρpre) = Tr
( 1
2I −|Ψφ⟩⟨Ψφ|


(1 −p)
Ψθ
φ
ED
Ψθ
φ
 + p I
2N
 )
= 1
2 −(1 −p)|⟨Ψφ|Ψθ
φ⟩|2 −p
2N
= 1
2 −1 −p
2
[1 + sin(2θ)] −p
2N < 0.
(A5)
As N →∞, one has
p < 1 −
1
1 + sin(2θ).
(A6)
Appendix B: Proof of decompositions in Eq. (26)
First, note that the matrix form of cos θkσx + sin θkσy
shows,
cos θkσx + sin θkσy =

0
e−iθk
eiθk
0

= e−iθk|0⟩⟨1| + eiθk|1⟩⟨0|,
(B1)
Let l(b) = PN
i=0 bi denote the weight of the binary
string b ∈{0, 1}N, and ¯b is the bitwise inverse of b with
¯bi = (bi + 1) mod 2. We can further rewrite the product
operator Mθk in Eq. (21) in the computational basis as
follows.
Mθk =
X
b
ei[l(b)−l(¯b)]θk|b⟩

¯b

=
X
b
ei[2l(b)−N]θk|b⟩

¯b

=


e−iNθk
· · ·
eiNθk

.
(B2)
Here in the second line we use the fact l(b) + l(¯b) = N
and l(b) ∈{0, 1, · · · , N}. Note that Mθk only possesses
terms on oﬀ-diagonal positions. For the clearness of the
latter decomposition, we add a corresponding phase on
Mθk as,
M′
θk ≡eiNθkMθk =
X
b
ei2θkl(b)|b⟩

¯b

=
X
b
ei 2πk
N+1 l(b)|b⟩

¯b
.
(B3)
From Eq. (24) and (25) in Main Text, X contains two
terms X+and X−, and we rewrite them as,
X+ = 1
2X ′
+,
X−= 1
2iX ′
−,
(B4)
where X ′
+ and X ′
−having matrix forms in the computa-
tional basis as,
X ′
+ =





1
0
· · ·
0
1




,
X ′
−=





1
0
· · ·
0
−1




.
(B5)
Note that they show speciﬁc forms on the oﬀ-diagonal
positions.
In the following, we derive the decomposition of X ′
+
and X ′
−in terms of M′
θk using discrete Fourier transform.
Note that M′
θk shows the same coeﬃcient on the terms
|b⟩

¯b
, if they share the same l(b). Thus we only need
to care about the weight of the binary b and denote t =
l(b), which is the analog of the “time” domain, with t =
[0, 1, · · · , N].
It is clear that the function of M′
θk on
this domain is the Fourier basis function ei 2πk
N+1 t, with the
parameter k being the analog of the “frequency” domain.
The corresponding functions of X ′
+ and X ′
−on the time
domain are f+(t) = [1, 0 · · · , 1] and f−(t) = [1, 0 · · · , −1],


## Page 11


11
respectively. By applying discrete Fourier transform, one
has the coeﬃcients showing
F+(k) =
1
N + 1
N
X
t=0
e−i 2πk
N+1 tf+(t) = 1 + e−i 2πkN
N+1
N + 1
,
F−(k) =
1
N + 1
N
X
t=0
e−i 2πk
N+1 tf−(t) = 1 −e−i 2πkN
N+1
N + 1
.
(B6)
Combing these coeﬃcients with the operators, we have,
X+ = 1
2
N
X
k=0
F+(k)M′
θk,
= 1
2
N
X
k=0
1 + e−i 2πkN
N+1
N + 1
eiNθkMθk,
=
1
N + 1
N
X
k=0
cos( πkN
N + 1)Mθk,
=
1
N + 1
N
X
k=0
(−1)k cos(θk)Mθk,
(B7)
where the last line is on account of
πkN
N+1 = kπ −θk.
Similarly,
X−= 1
2i
N
X
k=0
F−(k)M′
θk,
= 1
2i
N
X
k=0
1 −e−i 2πkN
N+1
N + 1
eiNθkMθk,
=
1
N + 1
N
X
k=0
sin( πkN
N + 1)Mθk,
=
−1
N + 1
N
X
k=0
(−1)k sin(θk)Mθk.
(B8)
Appendix C: Comparison between the white noise
tolerances in Eq. (33) and (35)
Here, we compare the white noise tolerance in Eq. (33)
using a family of witnesses WΨθ
φ with that using a fam-
ily of witnesses WΨφ in Eq. (20), for the noisy state in
Eq. (17). In the following, we show the diﬀerence of them
denoted by the function,
g(θ) = [1 −
1
sin(2θ) + 1] −min{cos2 θ, sin2 θ} ≥0,
(C1)
where θ ∈[0, π
2 ] and g(θ) = 0 as θ = 0, π
4 , π
2 . Note that
g(θ) is symmetric with respective to θ =
π
4 . Thus we
only need to consider the regime θ ∈[0, π
4 ],
g(θ) =[1 −
1
sin(2θ) + 1] −sin2 θ
= cos2 θ −
1
sin(2θ) + 1
= cos2 θ −
1
(cos θ + sin θ)2 ≥0
(C2)
equivalently,
cos θ(cos θ + sin θ) −1
≥
0,
that is,
cos θ sin θ ≥sin2 θ →1 ≥tan θ or sin θ = 0. This true
since θ ∈[0, π
4 ].
Appendix D: Derivation of noise tolerances in
Eq. (55), (56) and the comparison
First, let us derive the noise tolerances in Eq. (55).
Hereafter, we use φ and θ to denote φopt and θopt without
confusion, and also denote f(θ) = max{cos2 θ, sin2 θ} in
W2
Ψθ
φ for simplicity.
Note that in Eq. (52), W2
Ψθ
φ is written in the following
form,
2W2
Ψθ
φ = (f(θ) + 1)I −(P ′
1 + P ′
2),
(D1)
where P ′
1 and P ′
2 are two projectors determined by the
stabilizers of the state
Ψθ
φ
E
.
The noise tolerance is determined by Tr(W2
Ψθ
φρpre) < 0.
Inserting the witness of Eq. (D1) and the noisy state ρpre
of Eq. (17), one has
Tr {[(f(θ) + 1)I −(P ′
1 + P ′
2)] ρpre}
= (f(θ) + 1) −Tr

(P ′
1 + P ′
2)

(1 −p)
Ψθ
φ
ED
Ψθ
φ
 + p I
2N

= (f(θ) + 1) −2(1 −p) −p
2N Tr(P ′
1 + P ′
2)
= (f(θ) + 1) −2(1 −p) −p(2N−1 + 2)
2N
< 0,
(D2)
where in the third line we use the fact that P ′
1 and P ′
2
stabilize
Ψθ
φ
E
, and in the ﬁnal line Tr(P ′
1) = 2N−1,
Tr(P ′
2) = 2. From Eq. (D2), it is not hard to see that
p =
2N−1
3 ∗2N−2 −1(1 −f(θ)) ≃2
3 min{cos2 θ, sin2 θ},
(D3)
as N →∞.
Second, let us derive Eq. (56), which is the tolerance
of the optimal witness in Eq. (37) for the noisy state in
Eq. (17). Since the optimization in Eq. (41) helps to de-
termine the parameter φ of the prepared state in Eq. (17),
one can choose the witness with the same parameter φ in
Eq. (37). Consequently, the white noise tolerance is the
same with the noisy state,
ρpre = (1 −p)
Ψθ
Ψθ + p I
2N ,
(D4)


## Page 12


12
where
Ψθ
= cos θ|0⟩⊗N + sin θ|1⟩⊗N, under the detec-
tion of the witness W2
GHZ in Eq. (36).
Tr(W2
GHZρpre)
= Tr
( 3
2I −(P1 + P2)
 
(1 −p)
Ψθ
Ψθ + p I
2N
 )
= 3
2 −(1 −p)[3
2 + 1
2 sin(2θ)] −p
2N Tr(P1 + P2)
= 3
2 −(1 −p)[3
2 + 1
2 sin(2θ)] −p(2N−1 + 2)
2N
< 0.
(D5)
Here in the second line we applies the formula of W2
GHZ
in Eq. (45). The second line is due to the fact that P2
stabilizes
Ψθ
and Tr(P1
Ψθ
Ψθ) = 1
2 + 1
2 sin(2θ), and
the ﬁnal line Tr(P1) = 2N−1, Tr(P2) = 2. From Eq. (D5),
it is not hard to see that
p <
sin(2θ)
sin(2θ) + 2 −22−N ≃1 −
2
sin(2θ) + 2,
(D6)
as N →∞.
Finally, let us compare the two noise tolerances in
Eq. (55) and (56). Similar as Appendix C, we deﬁne the
function l(θ) as the subtraction and consider the regime
θ ∈(0, π
4 ) due to the symmetry,
l(θ) =[1 −
2
sin(2θ) + 2] −2
3 sin2 θ
= 2
3
1
2 + cos2 θ −
3
sin(2θ) + 2

≥0.
(D7)
That is, ( 1
2 +cos2 θ)(sin(2θ)+2) ≥3. After simpliﬁcation,
it is equivalent to 2 + cos(2θ) ≥2 tan(θ), which is right
for θ ∈(0, π
4 ).
[1] C. H. Bennett, G. Brassard, C. Cr´epeau, R. Jozsa,
A. Peres,
and W. K. Wootters, Phys. Rev. Lett. 70,
1895 (1993).
[2] C. H. Bennett and G. Brassard, in Proceedings of IEEE
International Conference on Computers, Systems, and
Signal Processing (India, 1984) p. 175.
[3] A. K. Ekert, Phys. Rev. Lett. 67, 661 (1991).
[4] N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani, and
S. Wehner, Rev. Mod. Phys. 86, 419 (2014).
[5] M. A. Nielsen and I. L. Chuang, Quantum Computation
and Quantum Information: 10th Anniversary Edition,
10th ed. (Cambridge University Press, New York, NY,
USA, 2011).
[6] S.
Lloyd,
Science
273,
1073
(1996),
http://science.sciencemag.org/content/273/5278/1073.full.pdf.
[7] D. J. Wineland, J. J. Bollinger, W. M. Itano, F. L. Moore,
and D. J. Heinzen, Phys. Rev. A 46, R6797 (1992).
[8] V.
Giovannetti,
S.
Lloyd,
and
L.
Maccone,
Science
306,
1330
(2004),
http://science.sciencemag.org/content/306/5700/1330.full.pdf.
[9] T. Monz, P. Schindler, J. T. Barreiro, M. Chwalla,
D. Nigg, W. A. Coish, M. Harlander, W. H¨ansel, M. Hen-
nrich, and R. Blatt, Phys. Rev. Lett. 106, 130506 (2011).
[10] J. W. Britton, B. C. Sawyer, A. C. Keith, C. C. J.
Wang, J. K. Freericks, H. Uys, M. J. Biercuk, and J. J.
Bollinger, Nature 484, 489 EP (2012).
[11] D. Nigg, M. M¨uller, E. A. Martinez, P. Schindler,
M.
Hennrich,
T.
Monz,
M.
A.
Martin-
Delgado,
and R. Blatt, Science 345, 302 (2014),
https://science.sciencemag.org/content/345/6194/302.full.pdf.
[12] C. Song, K. Xu, W. Liu, C.-P. Yang, S.-B. Zheng,
H. Deng, Q. Xie, K. Huang, Q. Guo, L. Zhang, P. Zhang,
D. Xu, D. Zheng, X. Zhu, H. Wang, Y.-A. Chen, C.-Y.
Lu, S. Han, and J.-W. Pan, Phys. Rev. Lett. 119, 180511
(2017).
[13] M. Gong, M.-C. Chen, Y. Zheng, S. Wang, C. Zha,
H. Deng, Z. Yan, H. Rong, Y. Wu, S. Li, F. Chen,
Y. Zhao, F. Liang, J. Lin, Y. Xu, C. Guo, L. Sun, A. D.
Castellano, H. Wang, C. Peng, C.-Y. Lu, X. Zhu,
and
J.-W. Pan, Phys. Rev. Lett. 122, 110501 (2019).
[14] X.-L. Wang, L.-K. Chen, W. Li, H.-L. Huang, C. Liu,
C. Chen, Y.-H. Luo, Z.-E. Su, D. Wu, Z.-D. Li, H. Lu,
Y. Hu, X. Jiang, C.-Z. Peng, L. Li, N.-L. Liu, Y.-A. Chen,
C.-Y. Lu, and J.-W. Pan, Phys. Rev. Lett. 117, 210502
(2016).
[15] L.-K. Chen, Z.-D. Li, X.-C. Yao, M. Huang, W. Li, H. Lu,
X. Yuan, Y.-B. Zhang, X. Jiang, C.-Z. Peng, et al., Op-
tica 4, 77 (2017).
[16] H.-S. Zhong, Y. Li, W. Li, L.-C. Peng, Z.-E. Su, Y. Hu,
Y.-M. He, X. Ding, W. Zhang, H. Li, L. Zhang, Z. Wang,
L. You, X.-L. Wang, X. Jiang, L. Li, Y.-A. Chen, N.-L.
Liu, C.-Y. Lu,
and J.-W. Pan, Phys. Rev. Lett. 121,
250505 (2018).
[17] B. L¨ucke, J. Peise, G. Vitagliano, J. Arlt, L. Santos,
G. T´oth, and C. Klempt, Phys. Rev. Lett. 112, 155304
(2014).
[18] X.-Y. Luo,
Y.-Q. Zou,
L.-N. Wu,
Q. Liu,
M.-F.
Han, M. K. Tey, and L. You, Science 355, 620 (2017),
http://science.sciencemag.org/content/355/6325/620.full.pdf.
[19] K.
Lange,
J.
Peise,
B.
L¨ucke,
I.
Kruse,
G.
Vitagliano,
I.
Apellaniz,
M.
Kleinmann,
G. T´oth,
and C. Klempt, Science 360, 416 (2018),
https://science.sciencemag.org/content/360/6387/416.full.pdf.
[20] K. Vogel and H. Risken, Phys. Rev. A 40, 2847 (1989).
[21] M. Paris and J. e. Rehacek, in Lect. Notes Phys. (2004),
10.1007/b98673.
[22] B. M. Terhal, Linear Algebra and its Applications 323,
61 (2001).
[23] O. Guhne and G. Toth, Physics Reports 474, 1 (2009).
[24] M. Bourennane, M. Eibl, C. Kurtsiefer, S. Gaertner,
H. Weinfurter, O. G¨uhne, P. Hyllus, D. Bruß, M. Lewen-
stein,
and A. Sanpera, Phys. Rev. Lett. 92, 087902
(2004).
[25] B. M. Terhal, Theoretical Computer Science 287, 313
(2002), natural Computing.
[26] O. G¨uhne, P. Hyllus, D. Bruß, A. Ekert, M. Lewenstein,
C. Macchiavello,
and A. Sanpera, Phys. Rev. A 66,
062305 (2002).


## Page 13


13
[27] O. G¨uhne, C.-Y. Lu, W.-B. Gao, and J.-W. Pan, Phys.
Rev. A 76, 030305 (2007).
[28] D. Gottesman, arXiv: quant-ph/9705052 (1997).
[29] P. Aliferis, D. Gottesman, and J. Preskill, Quantum Info.
Comput. 6, 97 (2006).
[30] K. Chen and H.-K. Lo, Quantum Information & Compu-
tation 7, 689 (2007).
[31] M. Hillery, V. Buˇzek, and A. Berthiaume, Phys. Rev. A
59, 1829 (1999).
[32] R. Cleve, D. Gottesman, and H.-K. Lo, Phys. Rev. Lett.
83, 648 (1999).
[33] G. T´oth and O. G¨uhne, Phys. Rev. Lett. 94, 060501
(2005).
[34] Q. Zhao, G. Wang, X. Yuan, and X. Ma, Phys. Rev. A
99, 052349 (2019).
[35] G.
T´oth,
W.
Wieczorek,
D.
Gross,
R.
Krischek,
C. Schwemmer, and H. Weinfurter, Phys. Rev. Lett. 105,
250403 (2010).
[36] Y. Zhou, C. Guo, and X. Ma, Phys. Rev. A 99, 052324
(2019).
[37] M. Huber and J. I. de Vicente, Phys. Rev. Lett. 110,
030501 (2013).
[38] H. Lu, Q. Zhao, Z.-D. Li, X.-F. Yin, X. Yuan, J.-C. Hung,
L.-K. Chen, L. Li, N.-L. Liu, C.-Z. Peng, Y.-C. Liang,
X. Ma, Y.-A. Chen,
and J.-W. Pan, Phys. Rev. X 8,
021072 (2018).
[39] Y. Zhou, Q. Zhao, X. Yuan, and X. Ma, npj Quantum
Information 5, 83 (2019).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]