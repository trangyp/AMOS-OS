---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1110.3161v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1110.3161v1_Intrinsic_adaptation_in_autonomous_recurrent_neural_networks

> Source: 1110.3161v1_Intrinsic_adaptation_in_autonomous_recurrent_neural_networks.pdf

> Pages: 24

---


## Page 1


arXiv:1110.3161v1  [cond-mat.dis-nn]  14 Oct 2011
Intrinsic adaptation in autonomous recurrent neural
networks
Dimitrije Markovi´c1 and Claudius Gros1
1Institute for Theoretical Physics, J. W. Goethe University, Frankfurt am Main,
Germany.
Keywords: information theory, non-synaptic adaptation, self-organization,
neural networks
Abstract
A massively recurrent neural network responds on one side to input
stimuli and is autonomously active, on the other side, in the absence of
sensory inputs. Stimuli and information processing depends crucially
on the qualia of the autonomous-state dynamics of the ongoing neural
activity. This default neural activity may be dynamically structured
in time and space, showing regular, synchronized, bursting or chaotic
activity patterns.
We study the inﬂuence of non-synaptic plasticity on the default dy-
namical state of recurrent neural networks. The non-synaptic adaption
considered acts on intrinsic neural parameters, such as the threshold
and the gain, and is driven by the optimization of the information en-
tropy. We observe, in the presence of the intrinsic adaptation processes,
three distinct and globally attracting dynamical regimes, a regular syn-
chronized, an overall chaotic and an intermittent bursting regime. The


## Page 2


intermittent bursting regime is characterized by intervals of regular
ﬂows, which are quite insensitive to external stimuli, interseeded by
chaotic bursts which respond sensitively to input signals. We discuss
these ﬁnding in the context of self-organized information processing
and critical brain dynamics.
1
Introduction
In the last couple of decades self organized processes have attracted the interests
of many researchers from various scientiﬁc areas, both in natural and in social
sciences.
A system is said to be self-organizing, quite generally, when a state
of high dynamical complexity arises reliably from relatively simple basic orga-
nization rules (Ashby, 1962; Camazine, Deneubourg, Franks, Sneyd, & Theraula,
2003; Gros, 2010).
It is often the case that the self-organization in dynamical systems is achieved
through an interplay or regulative forces involving positive and negative feed-
back, viz. through the interplay of internal drives which act destabilizing and
regulating, respectively, onto the dynamics of the system. In general one type
of feedback can dominate, driving the system towards a chaotic or towards an
ordered phase respectively. A proper balance of the two opposing drives can bring
the dynamical state at the point of a phase transition, a critical state. One speaks
of self-organized criticality (SOC) whenever this balance is not achieved through
the actions of an outside controller but through internal self-organizing processes
(Bak, Tang, & Wiesenfeld, 1987, 1998; , Bak, & Paczuski, 1995; Adami, 1995).
As a dynamical system approaches a critical point, its spatiotemporal com-
plexity rises.
It has been suggested that this rise in the complexity improves
the computational properties and the capability of dynamical systems to process
information (e.g., Sol´e, & Miramontes, 1995; Bertschinger, & Natschl¨ager, 2004;
Legenstein, & Maass, 2006). This notion of “Computation at the edge of chaos”
may also been seen in the broader context of “Life at the edge of chaos” (see
Zimmer, 1999; Gros, 2010); the dynamical systems at the underpinning of all
living have the tendency to self-organize themselves close to a critical state.
2


## Page 3


In recent years there have been many studies of the possible occurrence of SOC
in neural networks with synaptic plasticity. Most of these studies have concluded
that synaptic plasticity drives the dynamics generically far below a critical point
(e.g., Siri, Quoy, Delord, Cessac, & Berry, 2007; Siri, Berry, Cessac, Delord, & Quoy,
2008; Dauce, Quoy, Cessac, Doyon, & Samuelides, 1998), viz. it over-regulates the
network dynamics. Hence, an organizational principle is needed which will main-
tain an intermediate level of excitability in neural networks, preventing the occur-
rence of dynamical states which are non- or hyper-reactive to external inﬂuences.
It has been assumed for many years that the dominant driving force, shaping
the brain’s dynamical state, is the synaptic plasticity. Thus, little attention was
put to other forms of neural adaption, the non-synaptic adaptation of individual
neurons (Mozzachiodi, & Byrne, 2010), also known as intrinsic plasticity. Intrinsic
plasticity is mostly manifested as a change in the excitability of a neuron, where
this change is achieved through the adaptation on the level of membrane compo-
nents. Here, we investigate the role of non-synaptic plasticity in the formation of
complex patterns of neural activity.
We study a previously proposed model of intrinsic plasticity (see Triesch, 2005,
2007; Stemmler, & Koch, 1999), and its inﬂuence on the dynamical properties of
autonomous recurrent neural networks with rate encoding neurons in discrete time.
Within this model neurons aspire to achieve, as an average over time, a ﬁring-
rate distribution which maximizes the Shannon information entropy (Gros, 2010).
Therefore, the neurons are trying to homeostatically regulate an entire distribution
function, a mechanism denoted polyhomeostatic optimization (Markovic, & Gros,
2010).
Intrinsic plasticity in the form of polyhomeostatic optimization gives rise, for
random recurrent network topologies, to ongoing and self-sustained neural activi-
ties with non-trivial dynamical states. Depending on the target mean ﬁring rate
and network parameters, one observes three distinct phase states: synchronized
oscillations, an intermittent-bursting and a chaotic phase; all states being globally
attracting in their respective phase spaces.
In Section 2 we derived the stochastic learning rules for intrinsic adaptation.
This is followed by the analysis of a single self-coupled neuron with intrinsic plas-
3


## Page 4


ticity (Section 3) and the analysis of recurrent network with intrinsic plasticity
(Section 4). Concluding remarks and discussion are ﬁnally provided in Section 5.
2
Stochastic adaptation
We used a basic discrete-time, rate-encoding artiﬁcial neuron model. The ﬁring
rate y ∈[0, 1] of the neuron is given as a nonlinear transformation of the total
synaptic input current x ∈(−∞, +∞), y = g(x). The transfer function g has a
sigmoidal form, a usual choice being the logistic function
y(t + 1) = ga,b(x(t)),
ga,b(z) =
1
1 + e−az−b ,
(1)
where a is the gain and b the bias. The parameters of the transfer function, intrinsic
parameters, will eventually become slow variables with a stochastic learning rules
determining their time evolution.
Let us denote with px(x) the probability density function (PDF) of the total
input. Given the relation (1) between the input current x and the output activity
y we ﬁnd
pa,b(y) =
Z +∞
−∞
δ(y −ga,b(x)) px(x) dx = px(x)
g′
a,b(x)|x=g−1
a,b(y)
(2)
for pa,b(y), the PDF of the ﬁring rate. The main idea behind the derivation of
adaption rules for the intrinsic parameters a and b is the assumption that the
neuron’s excitability should change in a way which maximizes the entropy of the
ﬁring rate distribution pa,b(y), keeping at the same time the average activity at a
desired level (Triesch, 2005).
The rational for this procedure is the following: the maximization of the ﬁring
rate entropy implies that a neuron will use the entire range of available activity
states, optimizing the information transfer between neural input and output. Fur-
thermore, the regulation of the average ﬁring rate is present due to environmental
constraints on the neuron, e.g. the limited energy resources needed for metabolic
processes.
Having a positive-deﬁnite variable y, with a ﬁxed ﬁrst moment, the maximum
4


## Page 5


entropy PDF corresponds to the exponential distribution
pλ(y) =
1
Z(λ)e−λy,
y ∈[0, 1] ,
(3)
where Z(λ) =
R 1
0 e−λydy is the partition function. We will refer to the ﬁrst moment
of the PDF (3), denoted as µ, as the target average ﬁring rate. It is given by
µ =
Z 1
0
ypλ(y)dy = 1
λ −
1
eλ −1 .
(4)
In general the inverse function λ(µ) cannot be found, but for λ ≫1 we recover
the λ →1/µ, which is valid for exponential PDFs deﬁned on [0, ∞].
A natural way to introduce a distance measure between two PDFs is the
Kullback-Leibler (KL) divergence (Gros, 2010), deﬁned as
Dλ(a, b)
=
Z
pa,b(y) ln
pa,b(y)
pλ(y)

dy
=
−Epx[ln g′
a,b(x)] + λEpx[ga,b(x)] −H[px] + ln Z(λ) ,
(5)
where Epx[·] denotes the expectation value with respect to px(x), and H[px] denotes
the diﬀerential entropy functional. By minimizing Dλ(a, b) with respect to the
intrinsic parameters a and b one obtains the learning rules. In Eq. (5) only the
ﬁrst two terms are functions of a and b. The gradient descent hence gives the
following relation
−∂Dλ(a, b)
∂α
=
Epx
 ∂
∂α ln g′
a,b(x) −λ ∂
∂αga,b(x)

=
Z
px(x)
 ∂
∂α ln g′
a,b(x) −λ ∂
∂αga,b(x)

|
{z
}
≡∆α
dx ,
(6)
with α ∈{a, b}.
As the input distribution px(x) is in general unknown, it is
suitable to derive the adaption rules by using a stochastic gradient descent (Spall,
2005). Such adaption rules, for the update of the internal parameters a and b, are
obtained by using the expression between the brackets on the right-hand side of
Eq. (6) . An advantageous side eﬀect of this approach is that the adaptation rules
become local in time. Using Eq. (1) for the transfer function ga,b(x) to evaluate
∆a and ∆b, we obtain the stochastic learning rules
5


## Page 6


a(t + 1)
=
a(t) + ǫ∆a(t) = a(t) + ǫ (1/a(t) + x(t)∆(t))
b(t + 1)
=
b(t) + ǫ∆b(t) = b(t) + ǫ ∆(t) ,
(7)
where ǫ is the learning rate and
∆(t) = 1 −(2 + λ)y(t + 1) + λy(t + 1)2 .
The learning rate ǫ is assumed to be small; viz the time evolution of the internal
parameters is slow compared to the evolution of both x(t) and y(t). In this way the
stochastic adaptation, which depends only on the instantaneous values of the vari-
ables, can closely match the direction of the deterministic gradient Eq. (6). Also,
the input distribution can, in general, be non-stationary, therefore the minimum
of the cost function Dλ(a, b) could vary in time. For this reason, the learning rate
should also be large enough for the adaptation to follow the changing minimum.
However, any ﬁnite and constant learning rate ǫ > 0 doesn’t satisfy the condition
for exact convergence of internal parameters into the minimum of Kullback-Leibler
divergence (Spall, 2005). Still, if the learning rate decreases with every time step, a
condition needed for strict convergence, the intrinsic adaptation will react slower
with time to a variability in the position of the minimum of the cost function.
Thus, it’s more favorable to have here a constant learning rate which will result in
the oscillations of the intrinsic parameters around the minimum. The amplitude
of this oscillations roughly scales as ǫ (Bottou, 2004), thus a small learning rate
also ensures convergence within a small vicinity from the minimum of the cost
function Dλ(a, b).
3
Single neuron
We analyze initially a minimal network setup, a self-coupled neuron adapting
homeostatically the intrinsic parameters of the transfer function. A synaptic con-
nection between the axon and the dendrites of the same neuron is also known as
an autapse.
6


## Page 7


Figure 1: (Left) A dependence of relative parameter change ∆(Eq. 9) on output
activity y for diﬀerent target ﬁring rates µ. (Right) Critical value of the gain ac,
as a function of the average ﬁring rate µ. The colored area shows the region of
stability of the ﬁxpoint (y∗(λ), b∗(a, λ)), see Section 3.
Neurons with an autapse are not rare in the brain. They have been observed
in various brain regions and in diﬀerent types of neurons. The discovery of func-
tional autapses provides clues for possible physiological roles (Bekkers, 2003).
Herrmann, & Klaus (2004) suggest that autapses lead to oscillatory behavior in
otherwise non-oscillating neurons. We shall see below how this type of behav-
ior spontaneously arises in self-excitatory neurons with intrinsic plasticity. We
focused on the analysis of excitatory autapse and used it as a basis for under-
standing the observed behavior in a larger network setup (see Section 4). For the
case of self-inhibition please refer to a separate study (Markovic et al., 2010).
The autapse neuron is equivalent to the identiﬁcation x →y in Eqs. (1) and
(7). The complete set of evolution rules for the dynamical variables y(t), a(t) and
b(t) is then
y(t + 1)
=
ga(t),b(t)(y(t))
b(t + 1)
=
b(t) + ǫ∆(t)
(8)
a(t + 1)
=
a(t) + ǫ(1/a(t) + y(t)∆(t))
with
∆(t) = 1 −(2 + λ)y(t + 1) + λy2(t + 1) .
(9)
The right-hand side of (9) depends directly on y(t+1) and only implicitly on y(t),
as one can easily verify when going through the derivation of the rules (7) for the
7


## Page 8


Figure 2: (Top) The time dependence of ﬁring-rate y(t) (solid line), bias b(t)
(squares) and gain a(t) (circles) for the one-site problem (8), with a learning rate
ǫ = 0.01 and a target average ﬁring rate µ = 0.25; The gain a(t) is set initially
bellow a critical value and since ǫ ≪1 the system relaxes quickly to the ﬁxpoint of
y = ga,b(y). Once a(t) surpasses a certain threshold, compare Fig. 1, the ﬁxpoint
becomes unstable and the system follows a limiting cycle.
(Bottom) Maximal local Lyapunov λmax(t) exponent compared to a Lyapunov
exponent of a perturbation parallel to the ﬂow λ||(t). They were estimated along
the points of the trajectory (y(t), a(t), b(t)).
intrinsic plasticity. In plot at the left side of Fig. 1 we showed ∆(y) (Eq. (9))
for various target ﬁring rates µ. Note that ∆(y = 0) = 1 and ∆(y = 1) = −1,
independently of λ.
3.1
Stability analysis
We ﬁrst analyze a reduced model of the three evolution equations (8), obtained
by setting ∆a(t) = 0, viz considering a constant a = a(t) = a(t + 1). The reduced
system contains a ﬁxpoint (y∗(λ), b∗(λ, a)), where y∗= [(2+λ)−
√
4 + λ2]/2λ and
8


## Page 9


b∗= ln(y∗/(1−y∗))−ay∗. This ﬁxpoint deﬁnes a one dimensional manifold in the
complete phase space (y, b, a), where the stability of the manifold depends directly
on the given value of a and λ (see Fig. 1). For a < ac the dynamics is attracted
toward the ﬁxpoint (y∗, b∗), while for a > ac, the ﬁxpoint becomes repelling and
the activity of the neuron follows a limiting cycle. One can show that the critical
gain is ac = 1/y∗(1 −y∗).
The time evolution of the full set of equations (see Fig. 2, top) approaches
a limiting cycle, for all starting values of (y, b, a). The evolution rules (8) have
ﬁxpoint solutions also for a vanishing adaptation, viz. for ǫ →0. These ﬁxpoints
are turned for ǫ > 0 into attractor relics (Gros, 2007, 2009).
The trajectory
slows down close to the attractor relics, giving rise to the transient ﬁring states,
observable in Fig. 2.
This non-trivial activity pattern is a direct consequence
of the polyhomeostatic adaption principle.
The system cannot achieve, as an
average over time, a non-trivial ﬁring-rate distribution by settling into a steady
state. Polyhomeostatic adaption hence forces the neuron to remain autonomously
active, with varying ﬁring rates.
For an insight on the inﬂuence of external input signal on the dynamics, we have
estimated the maximal local Lyapunov exponent λmax(t) and the Lyapunov expo-
nent for a perturbation in the direction of the ﬂow λ|| (δ⃗r(t) ∝(∆y(t), ∆a(t), ∆b(t))).
They are presented in the bottom graph of Fig. 2. We see that the neuron is most
sensitive to a perturbation during the transition between two attractor relics (low
and high activity levels), since λmax is positive through these transition periods.
Also, λ|| ≈λmax during the fast transition between the attractor relics. We thus
conclude that the direction of maximal sensitivity to perturbations is aligned with
the direction of the ﬂow at this points. Note that the two attractor relics can be
stable during the same time period, although the activity settles in only one of
them. This means that a transition could be induced with a suﬃciently strong
perturbation.
9


## Page 10


Figure 3: Output distributions of the two neurons with highest (diamonds) and
lowest (circles) Kullback-Leibler divergence (5) compared to the mean output dis-
tribution (dashed line) and the target exponential output distribution (full line).
The network size N = 500 neurons and a target mean ﬁring rate µ = 0.28 (top)
and µ = 0.5 (bottom). The values are identical for all the neurons in the network
and fraction of excitatory links fexc = 0.5. Insets: Output distribution of the sin-
gle self-coupled neuron having the target average ﬁring rate µ at the same value
as the neurons in the network.
3.2
Noisy autapse
Let us consider the case of a noisy autapse, when
x(t) →wy(t) + ξ(t) .
(10)
The neuron receives, beside the autaptic signal ∼wy(t), a random input from
an external source ∼ξ(t) (e.g. from some other neurons in the network). The
non-autaptic component of the input is drawn from a Gaussian distribution, ξ ∼
N(0, σ), where N(0, σ) denotes a normal distribution with zero mean and variance
σ2.
The external input hence perturbs the signal coming from the autapse. From
10


## Page 11


Figure 4: The Kullback-Leibler (KL) divergence Dλ(a, b) of the neuronal ﬁring-
rate distribution relative to the target exponential distribution (3), as a function
of the standard deviation σ of a Gaussian input distribution px(x), in the presence
of an autapse (green dots, w = 1 in Eq. (10)) and in the absence of the autapse
(red dashed line, w = 0 in Eq. (10)). Target mean ﬁring rate µ is set to 0.3 .
Inset: Mean KL divergence ⟨Dλ⟩(see section 4) of the random recurrent neural
network with N = 1000 neurons and mean target ﬁring rate µ = 0.3, as a function
of the fraction of excitatory links fexc. Note that increase of fexc can be related to
the decrease in the noisy component of the input that each neuron receives (see
section 4.2).
Fig. 2 it is quite obvious that the output distribution of a self-coupled neuron with
ξ ≡0, viz. noiseless autapse, in Eq. (10), deviates substantially from the target
exponential distribution. The output distribution in the case of noiseless autapse
is presented in the insets of Fig. 3. However, as we increase the magnitude of
the external signal, the output distribution of the neuron approaches the opti-
mal distribution and the KL divergence decreases toward a minimum, see Fig. 4.
Obviously, when σ ≫ω, the external input dominates, and the two cases with
and without an autapse become equivalent. Nevertheless, even small amounts of
noise, that is σ < ω are suﬃcient to disrupt the oscillatory behavior of the output
activity. This happens because of the existence of the second stable ﬁxpoint, for
certain values of a and b in y = ga,b(y). As the standard deviation σ increases,
the probability that the ﬁring-rate y will transit toward the second ﬁxpoint also
11


## Page 12


0.1
0.5
0.9
0.9
0.9
0.5
0.5
0.1
0.1
Figure 5: (Left) Mean Kullback-Leibler (KL) divergence ⟨Dλ⟩(color coded) as a
function of the fraction of excitatory links fexc and target mean ﬁring rate µ in
a recurrent network of N = 1000 neurons and connectivity K = 100. (Right)
⟨Dλ⟩as a function of connectivity K and target mean ﬁring rate µ, with excita-
tory/inhibitory neurons (Top) and projections (Bottom). Fraction of excitatory
links fexc = 0.8 in both cases. Density plot was evaluated as a linear interpolation
of the experimentally obtained values represented with green dots.
increases. Thus, at a certain levels of noise, the activity stochastically escapes in
short time intervals from the stable ﬁxpoints, and the regular oscillatory behavior
is destroyed. This also implies that a certain level of decorrelation between the
input current and output activity has to be reached, if the ﬁring-rate distribution
is to come as close as possible to the desired target distribution.
4
Recurrent neural network
We studied numerically random recurrent neural networks (RRNN) of N poly-
homeostatically adapting neurons (7), where each neuron receives input from K
pre-synaptic neurons.
In a ﬁrst step we consider networks of dual neurons, i.e. a single neuron can
12


## Page 13


have both excitatory and inhibitory projections. In such setup, the synaptic input
that the ith neuron receives is expressed as
xi(t) =
K
X
j̸=i
wijyj(t) .
(11)
The synaptic weights are selected as wij = ±1/
√
K, with a probability fexc for
the weight to be positive. The learning rate in (7) is set to ǫ = 0.01. We consider
homogeneous networks where all neurons have identical target average ﬁring rate
µ, determined through (4), for the target output distributions pλ(y), see Eq. (3).
For a neuron to ideally map an arbitrary input to the exponential distribution
with speciﬁed mean, it needs a transfer function which can take any functional
form during the adaption process. This is obviously not the case for the logistic
function which has only two adaptable parameters. As a result of this limited ﬂex-
ibility of the transfer function, even when the input of the neuron is independent
from the output (Fig. 4 red dashed line), the output distribution will never ideally
match the target exponential distribution (Markovic et al., 2010; Triesch, 2005).
4.1
Dynamical behaviors
To examine the mean deviation of the output activity from the target exponential
distribution, we have estimated the KL divergence Dλ(ai, bi), see Eq. (5), for
all neurons in a network of N = 1000 neurons, and averaged over the entire
network and over n = 50 random network realizations. The obtained mean ⟨Dλ⟩is
presented in Fig. 5 as a function of target mean ﬁring rate µ, fraction of excitatory
links fexc and network connectivity K. Note that ⟨Dλ⟩is low for high target ﬁring-
rates and for balanced excitation/inhibition, or for low connectivity K.
We have observed three distinct dynamical regimes, a pure chaotic regime
characterized by low values of ⟨Dλ⟩, a synchronised oscillatory regime observed
in random networks with dominating excitatory connections and a intermittent-
bursting regime observed for balanced excitation/inhibition and small µ.
To illustrate the diﬀerence between these dynamical behaviors, we present in
Fig. 6 the average neural activity (yellow line) and the activity patterns of a ran-
domly selected neuron in the network of N = 1000 units. As we vary the fraction
13


## Page 14


Figure 6: Activity of one, randomly chosen, neuron from the network of N=1000
neurons with connectivity K=100, depending on the fraction of excitatory links
fexc (top; µ = 0.3) and the mean target ﬁring rate µ (bottom; fexc = 0.5), where
the yellow line represents average network activity. The right ordinate shows the
corresponding mean Kullback-Leibler divergence (see section 4).
of excitatory links fexc and keep µ ﬁxed (Fig. 6 Top) the dynamics shifts from
the chaotic phase into the phase of synchronised oscillations. On the other hand,
reducing the target mean ﬁring rate for balanced excitation/inhibition (Fig. 6 Bot-
tom) leads to a manifestation of bursts of chaotic activity alternated by periods of
nearly constant activity. On the right side of the graphs we give the values of the
corresponding mean Kullback-Leibler divergence ⟨Dλ⟩. In addition, from the oscil-
latory regime it is possible to transit back into a chaotic or intermittent-bursting
regime (depending on the value of µ) by reducing the network connectivity K.
This can be easily seen from the similarity of the density plots on the right and
left hand side in Fig. 5.
14


## Page 15


In Fig. 3 we give an example of the output distributions for two neurons, with
highest and lowest values of Dλ, when the dynamics of the neural network is set in
chaotic regime. The two output distribution are compared with a corresponding
target exponential distribution.
Alternatively to randomly selecting a single link as excitatory or inhibitory,
one can consider a case when a single neuron is selected as either excitatory or
inhibitory. Thus, all the projections from one neuron are of the same type. We
have shown ⟨Dλ⟩for such case on the upper right graph of Fig. 5. The absence
of a visible diﬀerence between the upper and the lower graph indicates that the
intrinsic adaptation, in the low K limit, leads to the same dynamical behavior
indipendent from having excitatory and inhibitory neurons separeted or neurons
with both types of projections.
4.2
Oscillatory behavior
The network dynamics makes a transition into a synchronized oscillatory regime
(see Fig. 6), as fexc, the fraction of excitatory links, is increased. To better un-
derstand this oscillatory behavior let us recall the discussion from the previous
section.
In the case of a single self-coupled neuron we showed how a certain
level of decorrelation, between the output activity and the input signal has to be
achieved in order for a neuron activity to properly match the target distribution
(see Fig. 4). The same argument holds in the case of RRNN. Thus, when the
input is uncorrelated with its output activity (corresponding to the fexc ≳0.5),
the output distribution pa,b(y) closely matches the target distribution pλ(y).
The total synaptic input a neuron receives can be divided into two compo-
nents. The ﬁrst component is correlated with its own output activity via excita-
tory recurrent connections. The second component corresponds to the noisy and
uncorrelated part of the input which results from the competition between inhibi-
tion and excitation. The ﬁrst correlated part of the input becomes dominant over
the noisy second contribution as we increase the fraction of excitatory links fexc.
The activity therefore starts to follow an oscillatory locked-in trajectory for large
fractions fexc.
In the inset of Fig. 4 we present the change of mean KL divergence as the
15


## Page 16


number of excitatory connections grows, but for a ﬁxed target mean ﬁring rate.
We can see that ⟨Dλ⟩increases rapidly once the number of excitatory connections
starts to dominate.
Note that the transition between two phases occurs in a
slightly diﬀerent manner compared to the case of the neuron with a noisy autapse.
One reason for this diﬀerence is that input/output correlations will be ampliﬁed
by additional delayed components of an excitatory feedback a neuron receives.
This reasoning can be shown to hold by simulating a single neuron with delayed
coupling autapses driven by the input x(t) →Pn−1
k=0 ωky(t −n) + ξ(t) .
4.3
Intermittent bursts of chaotic dynamics
In the second graph (Fig. 6 Bottom), the dynamics enters an intermediate phase,
characterized by intermittent bursting of chaotic neural activities, as the target
mean ﬁring rate is decreased. A closer look into the phase space of intrinsic param-
eters (ai, bi), of the ith neuron, reveals that the intrinsic parameters approach a
limiting cycle, similar to the case of a neuron with an autapse. During the regime
of nearly constant activity ∆i(t) ≈0 the gain steadily increases. Once the gains
of suﬃcient number of neurons crosses a certain critical value, the activity of the
entire network shifts into a chaotic regime. The activity during the chaotic regime
exceeds the target average activity level µ, thus the gains of all neuron are driven
back to sub-critical values. Even when reducing the learning rates by several or-
ders of magnitude this intermittent-bursting behavior persists. Nevertheless, when
considering constant and supercritical gains for all neurons and allowing only the
respective biases to adapt, we observe a pure chaotic behavior. This change, which
arises when reducing the number of degrees of freedoms by considering constant
gains ai, is not yet fully understood. A one possible cause could be the use of
“vanilla” gradient which doesn’t take into account the curvature of the manifold
of probability distributions pa,b(y) (see Amari, 1998), and therefore doesn’t point
into direction of maximal change of Dλ(a, b).
16


## Page 17


Figure 7: Nonlinear ﬁnite time Lyapunov exponent ¯λ(δ0, τ) (see section 4.4) at
the time step τ, for the various target average ﬁring rates, with N = 1000, K =
100, fexc = 0.5 and δ0 = 10−9 in all cases. Presented curves are the average of 104
random perturbations. Inset: The limit of dynamical predictability Tp deﬁned as
a time needed for an error to reach 98% of the saturation level.
4.4
Sensitivity to external perturbations
We have evaluated the nonlinear ﬁnite time Lyapunov exponent (FTLE), which
measures the short-term growth rate of initial perturbations without linearization
of the time evolution equations (Ding, & Li, 2007).
In practice the FTLE is estimated by considering a small perturbation of the
trajectory ⃗z(t) ∈R3N along a randomly selected direction ⃗δ(0) ∈R3N, and follow-
ing the deviation of the perturbated trajectory from the reference orbit, that is
⃗δ(τ) = ⃗z′(t + τ) −⃗z(t + τ). The FTLE is the obtained as λ(⃗z(t), δ0, τ) = 1
τ ln δ(τ)
δ0 ,
where δ(τ) = ||⃗δ(τ)|| and δ0 = ||⃗δ(0)|| ≪1. The FTLE depends on the starting
point ⃗z(t) of the initial perturbation and on the size of the initial displacement
δ0. The mean FTLE ¯λ(δ0, τ), which is independent from the starting point ⃗z(t)
is evaluated by taking the average of the FTLEs over various points along the
trajectory,
¯λ(δ0, τ) = ⟨λ(⃗z(t), δ0, τ)⟩t = 1
n
n
X
t=1
λ(⃗z(t), δ0, τ) .
The mean FTLE still depends on the initial displacement δ0. If δ0 is chosen to be
very small one observes initially an exponential growth of the perturbation. For
this time period the mean FTLE is essentially constant and reduces to the largest
17


## Page 18


Lyapunov exponent. The growth of the perturbation eventually enters a nonlinear
phase, which is maintained until the deviation from the reference orbit reaches a
saturation value. Note that FTLE (λ(⃗z(t), δ0, τ)) is not necessarily positive for
all τ and ⃗z(t), implying that an initial deviation can converge back towards the
reference trajectory.
When analysing the changes of the dynamical behavior as we reduced µ, while
keeping fexc constant at 0.5, we found that when µ is in the range which cor-
responds to small values of ⟨Dλ⟩(see lower right part of Fig. 5), the dynamical
behavior is in a pure chaotic dynamical state with the constant part of the mean
FTLE ¯λ(t) in the range [0.05, 0.1] . In this phase the FTLE is positive for all τ
and ⃗z(t), thus small initial displacements diverge along every point of the orbit
⃗z(t).
As the target mean ﬁring rate is decreased down to µ = 0.2 we observe a kink
in the FTLE, with a transition to a second linear time development, see Fig. 7.
The manifestation of the kink corresponds to the occurrence of periods of quasi-
constant activity as seen in the bottom plot of Fig. 6. This laminar periods are
characterised by a negative local Lyapunov exponent, that is small perturbations
are suppressed during the laminar periods, leading however to a growth of the
perturbation during the periods of chaotic bursting.
In this intermittent bursting phase the short term chaotic behavior (t ≲200)
describes the repulsion of two initially close trajectories mainly during the bursting
regime. The long term behavior (t ≫200) is also chaotic, as a consequence of
the intermittent chaotic bursts. The change in the growth of perturbations (see
Fig. 7) results from the interplay of the distinct characteristic timescales of the
intrinsic variables (ai and bi) and the ﬁring rates (yi), with the ﬁrst being slow
and the later being fast variables (Boﬀetta, Giuliani, Paladin, & Vulpiani, 1998).
The occurrence of transiently stable periods of activity also leads to an increase in
the time Tp, measuring the limit of dynamic predictability, as shown in the inset
of Fig. 7. The duration of predictability Tp is deﬁned here as the time needed for
a perturbation to reach 98% of the saturation level (Ding et al., 2007).
The dependency of the FTLE on the position of a perturbation along the orbit
in phase space is presented in Fig. 8. We compared the FTLE, that is λ(⃗z(t), δ0, τ),
18


## Page 19


Figure 8: Position dependent ﬁnite time Lyapunov exponent ¯λ(⃗z(t), δ0, τ) (see
section 4.4) along the orbit. We considered three cases: (bottom) a chaotic phase
with µ = 0.25 and fexc = 0.5, (middle) intermittent-bursting phase with µ = 0.15
and fexc = 0.5, (top) synchronised oscillatory phase with µ = 0.15 and fexc = 0.7.
The initial displacement δ0, number of neurons N and connectivity K were set to
10−9, 103 and 102, respectively.
as estimated from six diﬀerent points along the trajectory ⃗z(t), for all three dy-
namical regimes. The FTLE is then evaluated for 500 consecutive timesteps and
after the 500th timestep a new perturbation is introduced. In the pure chaotic
dynamical regime the FTLE is positive for all given initial perturbation points.
While, in intermittent bursting regime one can also notice negative values of the
FTLE when the perturbation is initiated within the laminar period. In contrast,
perturbations starting during the periods of bursts leads to a strictly positive
FTLEs. In the oscillatory regime the FTLE is negative along the orbit and, simi-
lar to the single neuron case, the trajectory is unstable during the fast transitions
from low to high activity states (and vice versa), which results in sharp, positive
valued, spikes in the FTLE.
Chaotic dynamics is also observed in the non-adapting limit with ǫ →0, when-
19


## Page 20


ever the static values of ai are above the critical value.
This is in agreement
with the results of a large-N mean ﬁeld analysis of an analogous continuous time
Hopﬁeld network (Sompolinsky, Crisanti, & Sommers, 1988). Subcritical static ai
lead, on the other hand, to regular dynamics controlled by point attractors.
5
Discussion
Our results show that the introduction of intrinsic plasticity in random recurrent
neural networks results in ongoing and self-sustained neural activities with non
trivial dynamical states. For large networks we have observed, depending on the
speciﬁed parameters, three self-organized distinct phases. The network parameters
include the fraction of excitatory connections, the average connectivity and the
target average ﬁring rate. These results show that non-synaptic adaptation plays
an important role in the formation of complex patterns of neural activity.
An important part of the sensory signals an organism receives result from the
reactions of the environment to the motor actions taken by the organism itself. The
complexity of this portion of sensory inputs will then depend on the complexity
of the organism’s own behavior. This consideration indicates that self-generated
and autonomously sustained neural activity is important for the generation of
non-trivial behavioral patterns. It is hence more likely that an animal will start
an explorative behavior if the brain, supporting the body, is able to maintain a
change in sensory input. In other words, if the dynamics of a neural controller
would approach, in the absence of sensory inputs, a state of stable and constant
activity, it would be capable of generating only trivial motor actions.
As mentioned in the introduction, synaptic plasticity alone drives the dynamics
of a recurrent network generically toward a frozen state, independent of the pres-
ence or absence of sensory input (Siri et al., 2007). Synaptic plasticity is thus in
general, for non-spiking neurons, not suﬃcient for achieving self sustained activity,
a likely essential precondition to complex behavioral patterns.
The relevance of critical brain dynamics for both non-linear sensory processing
(Kinouchi, & Copelli, 2006) and for self-sustained neural computation is being
investigated intensively. Levina, Herrmann, & Geisel (2007, 2009) have demon-
20


## Page 21


strated that critical neural activity can be achieved when the depletion of synaptic
vesicles is included into the dynamics of membrane potential. Under this setup,
they observe power law scaling of avalanches formed by the activity of spiking neu-
rons, a result in agreement with experimental observations (e.g., Chialvo, 2010),
which are supportive of the notion that the brain works in critical regime. How-
ever, without any form of adaptation to varying sensory stimuli, neurons would
perform only trivial computations and criticality, or other complex activity pat-
terns, would generically not arise. Thus, to properly understand the brain dynam-
ics and cognitive processes, one must include various forms of plasticity (Triesch,
2005, 2007).
Here we showed that intrinsic or non-synaptic plasticity will drive a system
of recurrently interacting neurons, under certain quite general conditions (net-
work connectivity, ratio of excitation versus inhibition), towards a chaotic phase.
Synaptic adaption rules, on the other side, are known to generically drive recurrent
neural networks into a subcritical or frozen state. Our results hence indicate that
self-organization of neural network dynamics into a critical regime could occur
whenever intrinsic and synaptic plasticity are both present and relevant. Critical
neural dynamics would then result from the interplay between synaptic and non
synaptic adaption processes.
An analogous line of arguments has been brought forward by Der, Hesse, & Martius
(2006), by demonstrating the relevance of self-organized criticality for the emer-
gence of exploratory behavior in autonomous agents. Optimal predictability of
the sensory-motor cycle is achieved when the neural controller works in a critical
regime (Der et al., 2006). We believe that self-organized criticality in biologically
inspired autonomous recurrent neural networks will exhibit similar patterns of
complex behavior. Certainly, the complex behavior should persist when including
the interaction between an agent and the environment, as we plan to do in future
investigation.
21


## Page 22


References
Adami, C. (1995). Self-organized criticality in living systems. Physics Letters A,
203,29–32.
Amari, S. I. (1998).
Natural Gradient Works Eﬃciently in Learning.
Neural
Computation, 10, 251–276.
Ashby, W. (1962). Principles of the self-organizing system. (pp. 255–278). Princi-
ples of Self-Organization: Transactions of the University of Illinois Symposium.
Bak, P., Tang, C., Wiesenfeld, K. (1987) Self-organized criticality: An explanation
of the 1/f noise. Physical Review Letters, 59,381–384.
Bak, P., Paczuski, M. (1995). Complexity, contingency, and criticality. Proceedings
of the National Academy of Sciences of the United States of America, 92,6689–
6696.
Bak, P., Tang, C., Wiesenfeld, K. (1998).
Self-organized criticality.
Physical
Review A, 38,364–374.
Bekkers, J. M. (2003). Synaptic Transmission: Functional Autapses in the Cortex.
Current Biology, 13,433–435.
Bertschinger, N., Natschl¨ager, T. (2004). Real-time computation at the edge of
chaos in recurrent neural networks. Neural computation, 16,1413–1436.
Boﬀetta, G., Giuliani, P., Paladin, G., Vulpiani, A. (1998). An extension of the
Lyapunov analysis for the predictability problem. Journal of the Atmospheric
Science, 55, 3409–3416.
Bottou, L. (2004). Stochastic learning. (pp.146–148). Lecture notes in Computer
Science.
Camazine, S., Deneubourg, J.-L., Franks, N. R., Sneyd, J., Theraula, G. (2003).
Self-organization in biological systems. (pp. 8–93). Princeton: University Press.
Chialvo, D. R. (2010). Emergent complex neural dynamics. Nature Physics, 6,
744–750.
22


## Page 23


Dauce, E., Quoy, M., Cessac, B., Doyon, B., Samuelides, M. (1998).
Self-
organization and dynamics reduction in recurrent networks : stimulus presen-
tation and learning. Neural Networks, 11, 521–533.
Der, R., Hesse, F., Martius, G. (2006). Rocking Stamper and Jumping Snakes
from a Dynamical Systems Approach to Artiﬁcial Life. Adaptive Behavior, 14,
105.
Ding, R., Li, J. (2007). Nonlinear ﬁnite-time Lyapunov exponent and predictabil-
ity. Physics Letters A, 364, 396–400.
Gros, C. (2007). Neural networks with transient state dynamics. New Journal of
Physics, 9, 109.
Gros, C. (2009). Cognitive Computation with Autonomously Active Neural Net-
works: An Emerging Field. Cognitive Computation, 1, 77–90.
Gros, C. (2010). Complex and adaptive dynamical systems: A primer. (pp. 145–
175). Springer, Second edition
Herrmann, C. S., Klaus, A. (2004). Autapse turns neuron into oscillator. Inter-
national Journal of Bifurcation and Chaos, 14, 623–633.
Kinouchi, O., Copelli, M. (2006). Optimal Dynamical Range of Excitable Networks
at Criticality. Nature Physics, 2, 348–351.
Legenstein, R., Maass, W. (2006). Edge of Chaos and Prediction of Computational
Performance for Neural Circuit Models. Neural Networks, (pp. 1–36).
Levina, A., Herrmann, J. M., Geisel, T. (2007).
Dynamical synapses causing
self-organized criticality in neural networks. Nature Physics, 3, 857–860.
Levina, A., Herrmann, J. M., Geisel, T. (2009). Phase Transitions towards Criti-
cality in a Neural System with Adaptive Interactions. Physical Review Letters,
102, 1–4.
Markovic, D., Gros, C. (2010). Self-Organized Chaos through Polyhomeostatic
Optimization. Physical Review Letters, 105.
23


## Page 24


Mozzachiodi, R., Byrne, J. H. (2010).
More than synaptic plasticity: role of
nonsynaptic plasticity in learning and memory. Trends in neurosciences, 33,
17–26.
Siri, B., Quoy, M., Delord, B., Cessac, B., Berry, H. (2007). Eﬀects of Hebbian
learning on the dynamics and structure of random networks with inhibitory and
excitatory neurons. Journal of Physiology, Paris, 101,136–148.
Siri, B., Berry, H., Cessac, B., Delord, B., Quoy, M. (2008). A mathematical
analysis of the eﬀects of Hebbian learning rules on the dynamics and structure of
discrete-time random recurrent neural networks. Neural Computation, 20,2937–
2966.
Sol´e, R. V., Miramontes, O. (1995). Information at the edge of chaos in ﬂuid
neural networks. Physica D: Nonlinear Phenomena, 80,171–180.
Sompolinsky, H., Crisanti, A., Sommers, H. J. (1998). Chaos in random neural
networks. Physical Review Letters, 61, 259–262.
Spall, J. C. (2005). Introduction to Stochastic Search and Optimization: Estima-
tion, Simulation, and Control. (pp. 126-147). New Jersey: Wiley, electronic
edition.
Stemmler, M., Koch, C. (1999). How voltage-dependent conductances can adapt to
maximize the information encoded by neuronal ﬁring rate. Nature Neuroscience,
2, 521–527.
Triesch, J. (2005). A gradient rule for the plasticity of a neurons intrinsic excitabil-
ity. Artiﬁcial Neural Networks: Biological InspirationsICANN 2005, Springer,
(pp. 65–70).
Triesch, J. (2007). Synergies between intrinsic and synaptic plasticity mechanisms.
Neural Computation, 909,885–909.
Zimmer, C. (1999). Life after chaos. Science, 284,83–86.
24

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]