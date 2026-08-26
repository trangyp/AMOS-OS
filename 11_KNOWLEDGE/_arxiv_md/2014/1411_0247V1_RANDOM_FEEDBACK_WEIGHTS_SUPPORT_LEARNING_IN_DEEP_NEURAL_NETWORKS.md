---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1411.0247v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1411.0247v1_Random_feedback_weights_support_learning_in_deep_neural_networks

> Source: 1411.0247v1_Random_feedback_weights_support_learning_in_deep_neural_networks.pdf

> Pages: 27

---


## Page 1


Random feedback weights support learning
in deep neural networks
Timothy P. Lillicrap1*, Daniel Cownden2, Douglas B. Tweed3,4, Colin J. Akerman1
1Department of Pharmacology, University of Oxford, Oxford, United Kingdom
2Centre for the Study of Cultural Evolution, Stockholm University, Stockholm, Sweden
3Departments of Physiology and Medicine, University of Toronto, Toronto, Canada
4Centre for Vision Research, York University, Toronto, Canada
∗To whom correspondence should be addressed:
timothy.lillicrap@pharm.ox.ac.uk
colin.akerman@pharm.ox.ac.uk
Abstract
The brain processes information through many layers of neurons. This deep
architecture is representationally powerful1,2,3,4, but it complicates learning by
making it hard to identify the responsible neurons when a mistake is made1,5.
In machine learning, the backpropagation algorithm1 assigns blame to a neu-
ron by computing exactly how it contributed to an error. To do this, it multiplies
error signals by matrices consisting of all the synaptic weights on the neuron’s
axon and farther downstream. This operation requires a precisely choreographed
transport of synaptic weight information, which is thought to be impossible in the
brain1,6,7,8,9,10,11,12,13,14. Here we present a surprisingly simple algorithm for deep
learning, which assigns blame by multiplying error signals by random synaptic
weights. We show that a network can learn to extract useful information from sig-
nals sent through these random feedback connections. In essence, the network
learns to learn. We demonstrate that this new mechanism performs as quickly
and accurately as backpropagation on a variety of problems and describe the
principles which underlie its function.
Our demonstration provides a plausible
basis for how a neuron can be adapted using error signals generated at distal lo-
cations in the brain, and thus dispels long-held assumptions about the algorithmic
constraints on learning in neural circuits.
1
arXiv:1411.0247v1  [q-bio.NC]  2 Nov 2014


## Page 2


Networks in the brain compute via many layers of interconnected neurons15,16. To
work properly neurons must adjust their synapses so that the network’s outputs are
appropriate for its tasks. A longstanding mystery is how upstream synapses (e.g. the
synapse between α and β in Fig. 1a) are adjusted on the basis of downstream errors
(e.g. e in Fig. 1a). In artiﬁcial intelligence this problem is solved by an algorithm called
backpropagation of error1. Backprop works well in real-world applications17,18,19, and
networks trained with it can account for cell response properties in some areas of
cortex20,21. But it is biologically implausible because it requires that neurons send
each other precise information about large numbers of synaptic weights — i.e. it needs
weight transport1,6,7,8,12,14,22 (Fig. 1a, b). Speciﬁcally, backprop multiplies error signals
e by the matrix W T, the transpose of the forward synaptic connections, W (Fig. 1b).
This implies that feedback is computed using knowledge of all the synaptic weights W
in the forward path.
For this reason, current theories of biological learning have turned to simpler schemes
such as reinforcement learning23, and “shallow” mechanisms which use errors to ad-
just only the ﬁnal layer of a network4,11.
But reinforcement learning, which deliv-
ers the same reward signal to each neuron, is slow and scales poorly with network
size5,13,24. And shallow mechanisms waste the representational power of deep net-
works3,4,25.
Here we describe a new deep-learning algorithm that is as fast and accurate as back-
prop, but much simpler, avoiding all transport of synaptic weight information. This
makes it a mechanism the brain could easily exploit. It is based on three insights: (i)
The feedback weights need not be exactly W T. In fact, any matrix B will sufﬁce, so
long as on average,
eTWBe > 0
(1)
where e is the error in the network’s output (Fig. 1a). Geometrically, this means the
teaching signal sent by the matrix, Be, lies within 90◦of the signal used by backprop,
W Te, i.e. B pushes the network in roughly the same direction as backprop would. (ii)
Even if the network doesn’t have this property initially, it can acquire it through learning.
The obvious option is to adjust B to make equation (1) true, but (iii) another possibility
is to do the same by adjusting W. We will show this can be done very simply, even
with a ﬁxed, random B (Fig. 1c).
We ﬁrst demonstrate that this mechanism works for a variety of tasks, and then ex-
plain why it works. For clarity we consider a three-layer network of linear neurons (see
2


## Page 3


b
e
c
a
d
Figure 1: Random feedback weights can deliver useful teaching signals to preceding layers of a neural
network. a, The backprop learning algorithm is powerful, but requires biologically implausible trans-
port of individual synaptic weight information. For backprop, neurons must know each other’s synaptic
weights, e.g. the three coloured synapses on the feedback cell at bottom must have weights equal to
those of the corresponding coloured synapses on three cells in the forward path. On a computer it
is simple to use the synaptic weights in both forward and backward computations, but synapses in the
brain communicate information unidirectionally. b, Implemented in a computer, backprop computes how
to change hidden unit activities by multiplying the error vector, e = y∗−y, by the transpose matrix of
the forward weights, i.e., ∆hBP = W T e. c, Our feedback alignment method uses the counterintuitive
observation that learning is still effective if W T is replaced by a matrix of ﬁxed random weights, B, so
that ∆hFA = Be. d, Four algorithms learn to mimic a linear function: ‘shallow’ learning (light gray), re-
inforcement learning (dark gray), backprop (black), and feedback alignment (green). NSE is normalized
squared error. e, Angle between the hidden-unit update vector prescribed by feedback alignment and
that prescribed by backprop, i.e., ∆hFA∡∆hBP. Error bars are two standard deviations for a sliding
window of 10 examples.
3


## Page 4


Methods). The network’s output is y = Wh, where h is the hidden-unit activity vector,
given by h = W0x, where x is the input to the network. W0 is the matrix of synaptic
weights from x to h and W is the weights from h to y. The network learns to approxi-
mate a linear function, T (for “target”). Its goal is to reduce the squared error, or loss,
L = 1
2eTe, where the error e = y∗−y = Tx −y.
We trained the network using four algorithms (Fig. 1d). If only the output weights,
W, are adjusted, as in shallow methods, then the loss hardly decreases. If a fast
variant of reinforcement learning is used to adjust the hidden weights, W0, then there
is some progress but it is slow. In contrast, backprop sends the loss rapidly towards
zero. It adjusts the hidden-unit weights according to the gradient of the loss, ∆W0 ∝
(∂L/∂W0) = (∂L/∂h)(∂h/∂W0) = −(W Te)xT. Thus, backprop adjusts the hidden
units according to the vector: ∆hBP = W Te. Here and throughout ∆h denotes the
update sent to the hidden layer, rather than the change in the hidden units. Our new
algorithm adjusts W in the same way as backprop (∆W ∝(∂L/∂W) = −ehT), but
for ∆h it uses a much simpler formula, which needs no information about W or any
other synapses but instead sends e through a ﬁxed random matrix B,
∆h = Be
(2)
This algorithm, which we call feedback alignment drives down the loss as quickly as
backprop does (Fig. 1d).
The network learns how to learn — it gradually discovers how to use B, which then
allows effective modiﬁcation of the hidden units. At ﬁrst, the updates to the hidden layer
are not helpful, but they quickly improve by an implicit feedback process that alters W
so that eTWBe > 0. To reveal this, we plot the angle between the hidden-unit updates
prescribed by feedback alignment and backprop, ∆hFA∡∆hBP (Fig. 1e; see Methods).
Initially the angles average about 90◦. But they soon shrink, as the algorithm begins
to take steps that are closer to those of backprop. This alignment of the ∆h’s implies
that B has begun to act like W T. And because B is ﬁxed, the alignment is driven by
changes in the forward weights W. In this way, random feedback weights come to
transmit useful teaching signals to neurons deep in the network.
Feedback alignment learning also solves nonlinear, real-world problems. We ran it
on a benchmark classiﬁcation problem (Fig. 2a), learning to recognize handwritten
digits17 (see Methods). On this task, backprop brings the mean error on the test set
to 2.4% (average of n=20 runs). Feedback alignment learns as quickly as backprop,
reaches 2.1% mean error (n=20), and develops similar feature detectors (Supplemen-
4


## Page 5


c
a
d
0
1
2
3
4
}
}
} 3-layer models
} 4-layer models
b
0
5
10
15
10%
100%
2.4%
2.1%
7.2%
Chance
90% =
% Error on Test Set
Figure 2: Feedback alignment solves nonlinear, real-world problems. a, A 784–1000–10 network of
logistic units learns to recognize handwritten digits. Representative performance curves for backprop
(black), feedback alignment (green), and shallow learning (light grey) on 10,000 test images. b, Angle
between the hidden-unit update made by feedback alignment and that prescribed by backprop, i.e.,
∆hFA∡∆hBP. Error bars are one standard deviation around the time-averaged mean. c, Feedback
alignment can train deeper layers via random weights, e.g. B1 and B2. d, Normalized squared error
curves, each an average over 20 trials, for a nonlinear function-approximation task; three-layer net-
work trained with shallow learning (grey), backprop (black), and feedback alignment (green); four-layer
network trained with backprop (magenta) and feedback alignment (blue).
tary Fig. S1). As measured by the angle, ∆hFA∡∆hBP, feedback alignment quickly
learns to use the random weights to transmit useful error information to the hidden
units (Fig. 2b). Even when we randomly remove 50% of the elements of the W and
B matrices, so that neurons in h and y have a 25% chance of reciprocal connection,
feedback alignment still matches backprop (2.4% mean error; n=20).
Some tasks are better performed by networks with more than one hidden layer, but
for that we need a learning algorithm that can exploit the extra power of a deeper net-
work2,3,4 (Fig. 2c). Backprop assigns blame to a neuron by taking into account all of
its downstream synapses. Thus, the update for the ﬁrst hidden layer in a four-layer
network (Fig. 2c) is ∆h0
BP = W T
1 ((W T
2 e) ◦h′
1), where ◦is element-wise multiplication,
5


## Page 6


a
b
-2
-1
0
1
2
-2
-1
0
1
2
Figure 3: Network dynamics underlying feedback alignment.
a, Three-neuron network learning to
match a linear function, y∗= Tx, with T = 1 and B ‘randomly’ chosen to be 1. b, Vector ﬂow ﬁeld
(small arrows) demonstrates the evolution of W0 and W during feedback alignment. Thick lines are
solution manifolds (i.e. W0W = 1 = T) where: eWBe > 0 (grey), eWBe < 0 (black), or unstable
solutions (dashed black). There is a small region of weight space (shaded grey) from which the system
travels to the “bad” hyperbola at lower left, but this is simply avoided by starting near 0. Large arrow
traces the trajectory for the initial condition W0 = W = 0.
and h′
1 is the derivative of the h1 activation function. With feedback alignment the
update is instead, ∆h0
FA = B1((B2e) ◦h′
1), where B1 and B2 are random matrices
(Fig. 2c). On a non-linear function-ﬁtting task (see Methods), both backprop (t-test,
n = 20, p = 3 × 10−12; Fig. 2d) and feedback alignment (t-test, n = 20, p = 9 × 10−13;
Fig. 2d) deliver better performance with a four-layer network than with a three-layer
network. Thus, the algorithm builds useful feature detectors in the deepest layers
of a network by relaying errors via random connections. This ﬂexibility makes feed-
back alignment more plausible for the brain: learning proceeds even when error vec-
tors are indiscriminately broadcast via random feedback weights to multiple layers of
cells.
Why does feedback alignment work? Its mechanism arises from certain novel network
6


## Page 7


dynamics. To explain them, we consider a minimal network with just one linear neuron
in each layer (Fig. 3a, see Methods). We visualize (Fig. 3b) how the network’s two
weights, W0 and W, evolve when the feedback weight B is set to 1. The ﬂow ﬁeld
shows that the system moves along parabolic paths. From most starting points the
network weights travel to the hyperbola at upper right (Fig. 3b). This hyperbola is a set
of stable equilibria solutions where W > 0 and therefore eTWBe > 0 for all e – that
is, equation (1) is satisﬁed, which means W has evolved so that the feedback matrix
B is delivering useful teaching signals.
In higher dimensions we can identify conditions under which feedback alignment is
guaranteed to reduce errors to zero (Supplementary Proof 1). Importantly, the proof
holds for cases where the error can reach zero only if B transmits useful information
to the hidden neurons. The proof also demonstrates that high-dimensional analogues
of the pattern of parabolic paths seen in the minimal network (Fig. 3a, b), also hold
for networks with large numbers of units. Indeed, the proof hinges on the fact that
feedback alignment yields the relation BW + W TBT = W0W T
0 + C, where C is a
constant, i.e. the left-hand side is a quadratic function of W0.
Feedback alignment updates do not converge with backprop (Fig. 1e, Fig. 2b), super-
ﬁcially suggesting that they are merely suboptimal approximations of ∆hBP. Further
analysis shows this view is too simplistic. Our proof says that weights W0 and W
evolve to equilibrium manifolds, but simulations (Fig. 4) and analytic results (Supple-
mentary Proof 2) hint at something more speciﬁc: that when the weights begin near
0, feedback alignment encourages W to act like a local pseudoinverse of B around
the error manifold. This fact is important because if B were exactly W + (the Moore-
Penrose pseudoinverse of W), then the network would be performing Gauss-Newton
optimization (Supplementary Proof 3). We call this update rule for the hidden units
pseudobackprop and denote it by ∆hPBP = W +e. Experiments with the linear net-
work show that the angle, ∆hFA∡∆hPBP quickly becomes smaller than ∆hFA∡∆hBP
(Fig. 4b, c; see Methods). In other words feedback alignment, despite its simplicity,
displays elements of second-order learning.
In the 1980’s, new artiﬁcial network learning algorithms promised to provide insight into
brain function1. But the most powerful class of algorithms use error signals tailored to
each neuron and seemed impossible to implement in the brain because they required
weight transport6,7. More-plausible algorithms have been devised9,10,13,14,22,26,27,28,29,30,
but these either fall far short of backprop’s speed or call for a lot of additional process-
ing10,11,12,13,22. In marked contrast, the mechanism developed here is much simpler
than backprop, but still matches its speed and accuracy. Feedback alignment dispels
the central assumption of previous neuron-speciﬁc algorithms - that error information
7


## Page 8


a
b
c
0
1
2
10
-10
10
-5
10
0
Figure 4: If W0 and W start small then W learns to act like a local pseudoinverse of B. a, Each trace
is a single run of feedback alignment learning with the elements of W0 and W drawn uniformly from
[−ω, ω], where ω = [0.0001, 0.001, 0.01, 0.05, 0.1, 0.125, 0.15, 0.2, 0.25], corresponding to blue through
red, respectively. Loss is normalized squared error (NSE). b-c, Angle between the hidden unit changes
prescribed by feedback alignment versus backprop (panel b) and versus pseudobackprop (panel c).
8


## Page 9


must be precisely tailored for each neuron. Our work shows that it is far easier than
previously thought to send neuron-speciﬁc teaching signals through a deep network:
all you need is random feedback connections. Thus, the principles underlying feed-
back alignment learning are compatible with many brain circuits in which reciprocal
feedback connections exist, such as occur within, and between regions of the neocor-
tex15,16. This makes it an attractive basis for understanding various forms of learning in
deep networks, including the integration of sensory information and motor adaptation
processes. Finally, feedback alignment may offer new opportunities to integrate neu-
roscience with recent advances in machine learning which have highlighted the power
of deep architectures2,3,18,19,25.
Methods Summary
We trained feedforward networks on three tasks. In all cases the goal was to minimize
the square of the error, L = (1/2)eTe, where e = y∗−y is the difference between the
desired and actual output. Task (1): A 30–20–10 linear network learned to approximate
a linear function, T. Input/output training pairs were produced via, y∗= Tx, with
x ∼N(µ = 0, Σ = I). Output weights were adjusted via, ∆W ∝eTh. Hidden weights
were adjusted according to: (a) backprop: ∆W0 ∝(W Te)xT = ∆hBPxT, (b) feedback
alignment: ∆W0 ∝(Be)xT = ∆hFAxT where the elements of B were drawn from the
uniform distribution over [−0.5, 0.5], (c) a variant of reinforcement learning called node
perturbation23,24. We chose the learning rate η for each algorithm via manual search31
in order to optimize learning speed. Task (2): A 784–1000–10 network with standard
sigmoidal hidden and output units (i.e., σ(x) = 1/(1+exp(−x))) was trained to classify
images of handwritten digits, 0–9. Each unit had an adjustable input bias. Standard
1-hot representation was used to code desired output. The network was trained with
60,000 images from the standard MNIST dataset17, and performance was measured
as the percentage of errors made on a held aside test set of 10,000 images. Both
algorithms used a learning rate of, η = 10−3, and weight decay, α = 10−6. Parameter
updates were the same as those used in the linear case, but with ∆hFA = (Be) ◦σ′,
where ◦is element-wise multiplication and σ′ is the derivative of the output activations.
Task (3): A 30–20–10 and 30–20–10–10 network were trained to approximate the
output of a 30–20–10–10 target network. All three networks had tanh(·) hidden units,
linear output units, and an adjustable input bias for each unit. Input/output training
pairs were produced via, y∗= W2 tanh(W1 tanh(W0x + b0) + b1) + b2, with x ∼
N(µ = 0, Σ = I). The angle between two vectors, e.g. a∡b, was computed as:
θ = cos−1(||aTb||/(||a|| · ||b||)).
9


## Page 10


Acknowledgements This project was supported by the European Community’s Sev-
enth Framework Programme (FP7/2007-2013), NSERC, and the Swedish Research
Council (grant 2009-2390).
Author Contributions T.L., C.A. conceived the project; T.L., D.C., D.T. ran the simula-
tions; T.L., D.C., D,T. wrote the Supplementary Information; T.L., D.C., D.T., C.A. wrote
the manuscript.
Full Methods
Comparing the performance of different learning algorithms is notoriously tricky. In-
deed, the no-free-lunch theorems remind us that any comparison tells only one part
of the story32. We have used straightforward methodological approaches, allowing us
to focus on the novel aspects of our observation. Thus, ﬁxed learning rates, and sim-
ple methods for selecting hyperparameters have been used throughout. Performance
may be improved by more complicated schemes, but our simple approach ensures a
clear view of the fundamental ideas of the main text.
Task (1) Linear function approximation: The target linear function T mapped vec-
tors in a 30 dimensional space to 10 dimensions. The elements of T were drawn
at random, i.e.
uniformly from the range [−1, 1].
Once chosen, the target matrix
was ﬁxed, so that each algorithm tried to learn the same function. The sequence
of data points learned on was also ﬁxed for each algorithm.
That is, the dataset
D = {(x1, y∗
1), · · · (xN, y∗
N)} was generated once according to: y∗
i = Txi, with xi ∼
N(µ = 0, Σ = I). The elements of the network weight matrices, W0, W, were ini-
tialized by drawing uniformly from the range [−0.01, 0.01]. For node perturbation re-
inforcement learning we optimized the scale of the perturbation variance by manual
search23,24,25. Simulations for Fig. 4 were essentially the same as those for Fig. 1
except that the learning rate for the runs was set to η = 10−3.
Task (2) MNIST dataset: We manually optimized the initial scale of the W0 and W
weight matrices and the learning rate, η, to give good performance with the backprop
algorithm. That is, the elements of W0 and W were drawn from the uniform distribution
over [−ω, ω] where ω was selected by looking at ﬁnal performance on the test set. The
same scale for the forward matrices and learning rate were used with the feedback
alignment algorithm. In a similar fashion, the elements of the B matrix were drawn
from a uniform distribution over [−β, β] with β chosen by manual search. Empirically,
we found that many scale parameters for B worked well. In practice it required 5
10


## Page 11


restarts to select the scale used for B in the simulations presented here. Once a scale
for B was chosen, a new B matrix was drawn for each of the n=20 simulations. In
the experiments where 50% of the weights in W and B were removed, we drew the
remaining elements from the same uniform distributions as above (i.e. using ω and
β). Learning was terminated after the same number of iterations for each simulation
and for each algorithm. We selected the termination time by observing when backprop
began to overﬁt on the test set.
Task (3) Nonlinear function approximation: The parameters for the 30–20–10–
10 target network, T(·), were chosen at random and then ﬁxed for all of the corre-
sponding simulations. We sought a parameter regime for the target network in which
backprop gained an unambiguous advantage from having an additional hidden layer.
The sequence of data points learned on was ﬁxed for each algorithm. The dataset
D = {(x1, y∗
1), · · · (xN, y∗
N)} was generated once according to: y∗
i = T(xi), with
xi ∼N(µ = 0, Σ = I). A new set of random matrices were chosen for each of the
n=20 simulations, both for the forward synaptic weights and biases and the backward
matrices. 5000 data points were held aside as a test-set. Network performance was
evaluated as the normalized squared error on these points. Hidden unit updates with
feedback alignment were ∆h1
FA = (B2e), and ∆h0
FA = B1((B2e) ◦h′
1) for the deeper
hidden layer, where h′
1 is the derivative of the h1 activities and ◦is element-wise multi-
plication. The elements of B1 and B2 were drawn from uniform distributions with scale
parameters selected manually. Learning was terminated after the same number of it-
erations for each simulation and for each algorithm. We selected the termination time
by observing when backprop made negligible gains on the training error.
Flow Field in Fig. 3: To produce the ﬂow ﬁelds in Fig. 3, we computed the expected
updates made by feedback alignment, rendering deterministic dynamics. Details for
the deterministic dynamics can be found in Supplementary Proof 1.
Computational details:
All learning experiments were run using custom built code in Python with the Numpy
library. MNIST experiments were sped up using a GPU card with the Cudamat and
Gnumpy libraries33,34. The dynamics in Fig. 3b were simulated with custom-built code
in Matlab.
11


## Page 12


References
[1] David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams. Learning repre-
sentations by back-propagating errors. Nature, 323(9):533–536, 1986.
[2] G.E. Hinton, S. Osindero, and Y. Teh. A fast learning algorithm for deep belief
nets. Neural Computation, 18:1527–1554, 2006.
[3] G.E. Hinton and R.R. Salakhutdinov. Reducing the dimensionality of data with
neural networks. Science, 313(5786):504–507, 2006.
[4] Yoshua Bengio and Yann LeCun.
Scaling learning algorithms towards AI.
In
B. Léon, C. Olivier, D. DeCoste, and J. Weston, editors, Large Scale Kernel Ma-
chines. MIT Press, 2007.
[5] H. Sebastian Seung. Learning in spiking neural networks by reinforcement of
stochastic synaptic transmission. Neuron, 40:1063–1073, 2003.
[6] Stephen Grossberg. Competitive learning: From interactive activation to adaptive
resonance. Cognitive Science, 11:23–63, 1987.
[7] Francis Crick.
The recent excitement about neural networks.
Nature,
337(12):129–132, 1989.
[8] David G. Stork. Is backpropagation biologically plausible? In International Joint
Conference on Neural Networks, volume 2, pages 241–246, 1989.
[9] Pietro Mazzoni, Richard A. Anderson, and Michael I. Jordan. A more biologically
plausible learning rule for neural networks. Proceedings of the National Academy
of Sciences, 88:4433–4437, 1991.
[10] Xiaohui Xie and H. Sebastian Seung. Equivalence of backpropagation and con-
trastive hebbian learning in a layered network. Neural Computation, 15(2):441–
454, 2003.
[11] Alexandre Pouget and Lawrence H. Snyder. Computational approaches to sen-
sorimotor transformations. Nature Neuroscience, 3:1192–1198, 2000.
[12] Kenneth D. Harris. Stability of the ﬁttest: organizing learning through retroaxonal
signals. Trends in Neurosciences, 31(3):130–136, 2008.
[13] Robert Urbanczik and Walter Senn.
Reinforcement learning in populations of
spiking neurons. Nature Neuroscience, 12(3):250–252, 2009.
12


## Page 13


[14] L.V. Chinta and D.B. Tweed. Adaptive optimal control without weight transport.
Neural Computation, 24(6):1487–1518, 2012.
[15] D.C. Van Essen, C.H. Anderson, and D.J. Felleman. Information processing in the
primate visual system: An integrated systems perspective. Science, 255:419–
423, 1992.
[16] R.J. Douglas and K.A. Martin. Neuronal circuits of the neocortex. Annu. Rev.
Neurosci., 27:419–451, 2004.
[17] Yann LeCun, Leon Bottou, Yoshua. Bengio, and Patrick Haffner. Gradient-based
learning applied to document recognition. In Proceedings of the IEEE, volume 86,
pages 2278–2324, November 1998.
[18] D.C. Ciresan, U. Meier, L.M. Gambardella, and J. Schmidhuber. Deep big simple
neural nets for handwritten digit recognition. Neural Computation, 22(12):3207–
3220, 2010.
[19] Geoffrey E. Hinton, Nitish Srivastava, Alex Krizhevsky, Ilya Sutskever, and Ruslan
Salakhutdinov. Improving neural networks by preventing co-adaptation of feature
detectors. ArXiv, 1207.0580, 2012.
[20] David Zipser and Richard A. Andersen. A back-propagation programmed net-
work that simulates response properties of a subset of posterior parietal neurons.
Nature, 331:679–684, 1988.
[21] Timothy P. Lillicrap and Stephen H. Scott. Preference distributions of primary
motor cortex neurons reﬂect control solutions optimized for limb biomechanics.
Neuron, 77(1):168–179, 2013.
[22] M.N. Abdelghani, T.P. Lillicrap, and D.B. Tweed. Sensitivity derivatives for ﬂexible
sensorimotor learning. Neural Computation, 20:2085–2111, 2008.
[23] R.J. Williams. Simple statistical gradient-following algorithms for connectionist
reinforcement learning. Machine Learning, 8:229–256, 1992.
[24] Justin Werfel, Xiaohui Xie, and H. Sebastian Seung.
Learning curves for
stochastic gradient descent in linear feedforward networks. Neural Computation,
17:2699–2718, 2005.
[25] Pascal Lamblin and Yoshua Bengio. Important gains from supervised ﬁne-tuning
of deep architectures on large labeled sets. In Neural Information Processing
Systems, volume 24th of Deep Learning and Unsupervised Feature Learning
Workshop, pages 1–8, 2010.
13


## Page 14


[26] D.H. Ackley, G.E. Hinton, and T.J. Sejnowski. A learning algorithm for boltzmann
machines. Cognitive Science, 9(1):147–169, 1985.
[27] G.E. Hinton and J.L. McClelland. Learning representations by recirculation. In
D.Z. Anderson, editor, Neural Information Processing Systems, pages 358–366,
New York, 1988.
[28] John F. Kolen and Jordan B. Pollack. Back-propagation without weight transport.
In IEEE World Congress on Computational Intelligence, volume 3, pages 1375–
1380, Orlando, Florida, 1994.
[29] Randall C. O’Reilly. Biologically plausible error-driven learning using local acti-
vation differences: The generalized recirculation algorithm. Neural Computation,
8:895–938, 1996.
[30] Konrad P. Körding and Peter König.
Supervised and unsupervised learning
with two sites of synaptic integration. Journal of Computational Neuroscience,
11:207–215, 2001.
[31] James Bergstra and Yoshua Bengio. Random search for hyper-parameter opti-
mization. Journal of Machine Learning Research, 13:281–305, 2012.
[32] D.H. Wolpert. The lack of a priori distinction between learning algorithms. Neural
Computation, 8(7):1341–1390, 1996.
[33] Volodymyr Mnih. Cudamat: A cuda-based matrix class for python. Technical
Report UTML TR 2009-004, University of Toronto, November 2009.
[34] Tieleman. Gnumpy: an easy way to use GPU boards in python. Technical Report
UTML TR 2010-002, University of Toronto, July 2010.
14


## Page 15


Supplementary Information for “Random feedback weights sup-
port learning in deep neural networks”
Supplementary Figures.
Initial
Backprop
Feedback Alignment
Sparse Feedback
Alignment
Figure S1: Receptive ﬁelds for 100 randomly selected hidden units shown at the beginning of learning
(top left) and for the three learning variants discussed in the main text. Grey scale indicates the strength
of connection from each of 28×28 pixels in MNIST images (white denotes strong positive, black denotes
strong negative).
15


## Page 16


Introduction to analytic results.
Here we present three analytical results which provide insight into the efﬁcacy of feed-
back alignment. The ﬁrst result gives conditions under which feedback alignment is
guaranteed to reduce the error of a network function to 0. The second result demon-
strates that the backprop algorithm can be modiﬁed in a simple way to impliment the
second order Gauss-Newton method of error minimization, as contrasted with gradient
descent method employed by standard backprop. The third result hints at a possible
connection between feedabck alignment and this Gauss-Newton modiﬁcation of back-
prop.
Proof #1: Condition for alignment to reduce error to zero.
Although the empircal results presented in the main text suggest that feedback align-
ment is effective across a broad range of problems, we cannot, at this point, sharply
delinate the space of learning problems where feedback alignment is gaurenteed to
work. We are, however, able to establish a class of problems where feedback align-
ment is gaurenteed to reduce training error to 0. Importantly this class of problems
contains cases where useful modiﬁcations must be made to downstream synaptic
weights to achieve this error redcution. Thus, this theorem establishes that alignment
does indeed succeed in transmitting useful error information to neurons deep within
the network.
We consider a linear network which generates output y, from input x according to
h = Ax
(3)
y = Wh
(4)
For each data point x presented to the network, the desired output, ˜y, is given by
a linear transformation T so that ˜y = Tx, (T for target). Our goal is to modify the
elements of A and W, so that the network is functionally equivalent to T.
Some comments on notation. Vectors x, h, y, etc. are column vectors, and we use
standard matrix multiplication throughout. For example xTx is the inner product of x
with itself (resulting in a scalar) and xxT is the outer product of x with itself (resulting
in a matrix). For brevity and clarity the matrices of synaptic weights referred to as W0
and W in the main text are here referred to simply as A and W respectively. When
refering to the speciﬁc elements of A or W, we take Aj
i to be the weight from the ith
16


## Page 17


input element to the jth hidden element, and similarly we take W k
j to be the weight
from the jth hidden element to the kth output element.
Importantly, the transport of error problem still applies even for a linear network, with a
linear target function T, provided the number of output units is less than the number of
hidden units which is less than the number of input units, i.e. no < nh < ni. In this case
the null space of A (those input vectors which A maps to zero) must be a subspace of
the null space of T if the network function is to perfectly match the target function. The
probability of a randomly initialized A having this property is effectively zero. Thus, if
alignment is able to reduce error to zero, we can concluded that useful modiﬁcations
have been made to A. Presumably, such modiﬁcations are only possible if useful
information concerning the errors is employed when modifying A. In this section we
prove that transmitting errors to hidden neurons via a ﬁxed arbitrary matrix, B, provides
sufﬁceinetly useful information for updating A, and reducing error to zero.
For convenience we deﬁne:
E := T −WA,
(5)
so that our error is e = Ex. Then the parameter updates can be written as
∆W = ηExxTAT
(6)
∆A = ηBExxT.
(7)
Here, η is a small positive constant reffered to as the learning rate.
Instead of modifying the parameters A and W after experiencing a single training pair
(x, Tx), it is possible to expose the network to many training examples, and then make
a single parameter change proportional to the average of the parameter changes pre-
scribed by each training pair. Learning in this way is referred to as batch-learning. In
the limit as batch size becomes large the change in the parameters becomes deter-
ministic and proportional to the expected change from a data point.
∆W = η

ExxTAT
(8)
∆A = η

BExxT
(9)
Here [·], denotes the expected value of a random variable. Under the assumption
that the elements of x are i.i.d. standard normal random variables, i.e. mean 0 and
standard deviation 1, then

xxT
= I. Here and throughout I denotes an identity
matrix. Thus, under this normality assumption, in the limit as batch size becomes
17


## Page 18


large the learning dynamics simplify to
∆W = ηEAT
(10)
∆A = ηBE.
(11)
In the limit as the learning rate, η becomes small these discrete time learning dynamics
described converge to the continuous time dynamical system
˙W = EAT
(12)
˙A = BE.
(13)
We will work within the context of this continuous time dynamical system when proving
theorem 1.
Throughout the proof of theorem 1 we will use the following relation.
BW + W TBT = AAT + C
(14)
To see why equation 14 holds note that if we multiply equation 12 by B on the left and
mulitply equation 13 by AT on the right, we have
˙AAT = B ˙W
(15)
Z
˙AATdt =
Z
B ˙Wdt + C1.
(16)
Transposing this we have
Z
A ˙ATdt =
Z
˙W TBTdt + CT
1 .
(17)
Then since
Z
˙AATdt =
Z
A ˙ATdt = 1
2AAT + C
(18)
equation 14 follows. Note that C = C1 + CT
1 , so C is symmetric and constant.
We are now in a position to state and prove theorem 1.
Theorem 1. Given the learning dynamics
˙W = EAT
(19)
˙A = BE,
(20)
18


## Page 19


and assuming that the constant C in equation 14 is zero and that the matrix B satisﬁes
B+B = I
(21)
then
lim
t→∞E = 0.
(22)
Some notes on the conditions of the theorem. Here and throughout B+ denotes de-
notes the Moore-Penrose pseudoinverse of B, hereafter referred to simply as the
pseudoinverse. The condition B+B = I holds when the columns of B are linearly
independent, and B has at least as many rows as columns, i.e. no ≤nh.
Note
that if the elements of B are choosen uniformly at random then the columns of B
will be linearly independent with probability 1.
The condition C = 0 is met when
AAT = BW + W TBT. While there are many initializations of W, A and B which
satisfy this condition, the only way to ensure that the C = 0 condition is satisﬁed for all
possible B is for W and A to be initialized as zero matrices.
Proof. Our proof is loosely inspired by Lyapunov’s method, and makes use of Bar-
balat’s lemma. Consider the quantity
V := tr(BEETBT).
(23)
We will use Barbalat’s lemma to show that ˙V →0.
Lemma 1 (Barbalat’s Lemma). If V satisﬁes:
1. V is lower bounded,
2. ˙V is negative semi-deﬁnite,
3. ˙V is uniformly continuous in time, which is satisﬁed if ¨V is ﬁnite,
then ˙V →0 as t →∞.
Because B and E are real valued V is equivalent to ||BE||2. Here and throughout
|| · || refers to the Frobenius norm. Consequently V is bounded below by zero, and so
satisﬁes the ﬁrst condition of lemma 1.
Lemma 2. ˙V is negative semi-deﬁnite.
19


## Page 20


d
dttr(BEETBT) = tr(B ˙EETBT + BE ˙ETBT)
(24)
= tr(B ˙EETBT) + tr(BE ˙ETBT)
(25)
= 2tr(B ˙EETBT)
(26)
= 2tr(B(−˙WA −W ˙A)ETBT)
(27)
= −2tr(BEATAETBT) −2tr(BWBEETBT)
(28)
Now,
2tr(BWBEETBT) = tr(BWBEETBT) + tr(BWBEETBT)
(29)
= tr(BWBEETBT) + tr(BEETBTW TBT)
(30)
= tr(BWBEETBT) + tr(W TBTBEETBT)
(31)
= tr(AAT(BEETBT))
(32)
= tr(ATBEETBTA)
(33)
which gives us that
d
dttr(BEETBT) = −2tr(BEATAETBT) −tr(ATBEETBTA) ≤0
(34)
since each of these terms is of the form tr(XXT), i.e. the inner product of a vector
with itself.
Lemma 3. A is bounded.
Consider
s := tr(AAT).
(35)
Then
˙s = 2tr(BEAT)
(36)
= 2tr(BTAT −BWAAT)
(37)
= 2tr(BTAT) −tr(AATAAT).
(38)
Now AAT is an nh x nh symmetric matrix and hence diagonalizable, therfore
s ≤nhλ
(39)
20


## Page 21


where λ is the dominant eigenvalue of AAT. Then
tr(AATAAT) = ||AAT||
(40)
≥λ2
(41)
≥
 s
nh
2
.
(42)
It follows that
˙s ≤2tr(BTAT) −
 s
nh
2
.
(43)
Using the Cauchy-Schwarz inequality we have that
tr(BTAT)2 ≤tr(AAT) · tr(BTT TBT) = s||BT||2,
(44)
so that when s > ||BT||2, then tr(BTAT) ≤s. Therefore
˙s < 2s −s2
n2
h
(45)
when s > ||BT||2. This implies that
˙s < 0
(46)
when s > ||BT||2 and s > 2nh. We can conclude that
s ≤||BT||2 + 2nh
(47)
for all time.
Lemma 4. ¨V is bounded.
Differentiating equation 34 we have that
¨V = −4tr(B ˙EATAETBT) −4tr(BE ˙ATAETBT) −2tr( ˙ATBEETBTA) −2tr(ATB ˙EETBTA)
(48)
=4tr(BEATAATAETBT) + 4tr(BWBEATAETBT) −4tr(BEBEAETBT)
−2tr(BEBEETBTA) + 2tr(ATBEATAETBTA) + 2tr(ATBWBEETBTA)
(49)
21


## Page 22


Thus ¨V can be expressed in terms of the traces of products of the matrices B, E, A,
and BW, and the transposes of these matrices. B is constant so it is bounded, V is
bounded below by zero, and ˙V ≤0, so V must converge to some value, implying the E
is bounded. Lemma 3 shows that A is bounded. Recall that AAT = BW +W TBT, and
so A being bounded implies that BW and W TBT are also bounded. Taken together
we have that ¨V is bounded.
Thus the conditions of lemma 1 hold and in the limit as t →∞, ˙V →0.
Since
both addends of ˙V have the same sign, in the limit both must be identically zero. In
particular tr(BEATAETBT) = 0, therfore BEAT = 0. Here and for the remainder of
this proof when use W, A, T and E to refer to the value of these matrices in the limit
as t →∞. Since B is constant we have,
EAT = 0.
(50)
Recall that ˙W = EAT, and so W is constant. Together with B being constant this
implies that AAT = WB + BTW T is also constant. By deﬁnition, BEAT = BTAT −
BWAAT. Recall that BEAT = 0, and that B, W and AAT are all constant, and so
BTAT must also be constant. Note that
˙AT = ETBT, so a constant BTAT implies
that BTETBT = 0. Then we have
0 = BTETBT = B+TETBT(B+)T = TET = ET T.
(51)
By deﬁnition EET = ET T −EATW T, and since both addends are zero EET = 0.
Thus tr(EET) = ||E|| = 0 and that E is identically zero.
Proof #2: Gauss-Newton modiﬁcation of backprop
Here we will show that replacing the transpose matrix, W T, with the Moore-Penrose
pseudoinverse matrix, W +, in the backprop algorithm renders an update rule which
approximates Gauss-Newton optimization. That is, the pseudoinverse of the forward
matrix, W +, not only satisﬁes the ﬁrst condition from the main text, i.e. eTWW +e > 0,
it prescribes second order updates for the hidden units.
The Gauss-Newton method is a way of minimizing squared error: it ﬁnds the vector x∗
that minimizes a scalar valued function L(x) of the form L(x) = 1
2e(x)Te(x). It does
this by starting with a guess of the value x∗and iteratively improving this guess. When
L has this quadratic form its second derivative, with respect to x, or Hessian Lxx is
22


## Page 23


eT
xex + eTexx. When e is small this is close to eT
xex. Therefore the ∆x prescribed by
Newton’s method, −L−1
xxLT
x, is roughly −(eT
xex)−1eT
xe, which may be written as, e+
xe,
where e+
x is the Moore-Penrose inverse of ex.
Now suppose we have a 3-layer network with input signal x, weight matrices A and W,
monotonic squashing function σ, hidden-layer activity vector h = σ(Ax), and linear
output cells with activity,
y = Wh = Wσ(Ax)
(52)
If we want to adjust h using the Gauss-Newton method, the formula is
∆hGN = −e+
he = −W +e
(53)
Most learning networks don’t adjust activity vectors like h but rather synaptic weight
matrices like A and W. Computing the Gauss-Newton adjustment to A is compli-
cated, but a good approximation is obtained by replacing W T with W + in the backprop
formula. That is, backprop says
∆Ai
j BP = −ηP
k(∂L/∂ek)(∂ek/∂Ai
j) = −ηP
kek∂yk/∂Ai
j
= −ηP
kek∂
 P
lW k
l hl
/∂Ai
j = −ηP
kekP
lW k
l ∂hl/∂Ai
j
= −ηP
kekP
lW k
l Dσl∂
 P
mAl
mxm
/∂Ai
j = −ηP
kekP
lW k
l Dσ∂Ai
jxj/∂Ai
j
= −ηP
kekP
lW k
l Dσlδilxj = −ηP
kekW k
l Dσixj
= −ηP
kekW T i
kDσixj
(54)
where δil is the Kronecker delta and Dσi is the derivative of the i’th element of σ(Ax)
with respect to its argument, the i’th element of Ax.
Replacing W T by W + in the last line of equation 54, we get what we will call the
pseudobackprop adjustment:
∆Ai
j PBP = −ηP
kekW +i
kDσixj
(55)
23


## Page 24


This adjustment yields a change in h that approximates the Gauss-Newton one, ∆hGN
from equation 53. To see this, compute the ﬁrst order approximation to the change in
h,
∆hi
PBP = DσiP
j∆Ai
j PBPxj + o ((xj)2))
≈−ηDσiP
j
P
kekW +j
kDσixjxj
(56)
= −η(Dσi)2P
j(xj)2P
kekW +i
k
(57)
= η(Dσi)2P
j(xj)2∆hi
GN
(58)
That is, each element of the pseudobackprop (PBP) alteration to h approximates the
Gauss-Newton adjustment times a positive number. And that positive number is 1 if
we choose η = 1/(Dσi)2xTx. If instead we want a constant η then we can choose
one that keeps ∆hi
PBP ≤∆hi
GN, so we don’t step too far.
In the context of training an artiﬁcial network pseudobackprop may be of little interest.
The pseudoinverse is expensive to compute, and computational resources can be bet-
ter spent either by simply taking more steps using the transpose matrix, or by using
other, more efﬁcient, second order methods. Pseudobackprop does, however, bear
upon the results of the main text. We ﬁnd experimentally that the alignment algorithm
encourages W to act like B+, so that B begins to act like W + on the error vectors.
Thus alignment may be understood as an approximate implimentation of psuedoback-
prop.
Proof #3: B acts like the pseudoinverse of W
Here we will prove that, under fairly restrictive conditions, feedback alignment pre-
scribes hidden unit updates which are in the same direction as those prescriped by
psuedobackprop, i.e. ∆hFA∡∆hPBP = 0. Again we take a linear network which gen-
erates output y, from input x according to
h = Ax
(59)
y = Wh.
(60)
We consider the dynamics of the parameters for this network when it is trained on a
single input-output pair, (x, ˜y), using the forward alignment algorithm.
24


## Page 25


The dynamics of the network parameters under this training regime are
Wt+1 = Wt + ∆Wt
(61)
At+1 = At + ∆At,
(62)
with
∆W = ηWehT
(63)
∆A = ηABexT.
(64)
Here, as in proof #1, B is a random, ﬁxed, matrix of full rank. ηW and ηA are small
positive learning rates.
Because we will only present the network with a single input, x, we have that
ht+1 = At+1x
= (At + ∆At)x
= ht + ηABexTx
(65)
= ht + ηhBe.
Here, ηh = xTxηA. For a judicious choice of ηA, namely ηA = ηW/(xTx), we have
ηh = ηW = η. For this choice of ηA it sufﬁces to consider the simpler dynamics
Wt+1 = Wt + ∆Wt
(66)
ht+1 = ht + ∆ht
(67)
with
∆W = ηehT
(68)
∆h = ηBe.
(69)
We now establish a lemma concerning these simpliﬁed dynamics.
Lemma 5. In the special case of W and A initialized to zero at every time step there
is a scalar sh such that
h = shB˜y
(70)
and a scalar sw such that
W = sw˜y(B˜y)T.
(71)
25


## Page 26


Proof. In the ﬁrst time step, when h = 0 and W = 0, the conditions 70 and 71 are
trivially satisﬁed with sh = 0 and sw = 0. We note that when conditions 70 and 71 hold
we have that
y = Wh = swsh˜y(B˜y)T(B˜y) = sy˜y.
(72)
Here sy := swsh(B˜y)T(B˜y). Now,
e = ˜y −y = ˜y −sy˜y = (1 −sy)˜y.
(73)
Then
∆W = ηehT = η(1 −sy)sh˜y(B˜y)T
(74)
and
∆h = ηBe = η(1 −sy)B˜y.
(75)
This yeilds
st+1
h
= st
h + η(1 −st
y)
(76)
and
st+1
w
= st
w + η(1 −st
y)st
h.
(77)
By induction we can conclude that equations 70 and 71 hold for every time step.
With this lemma we are now able to state and prove theorem 2.
Theorem 2. Under the same conditions as Lemma 5, for the simpliﬁed dynamics de-
scribed in equations 66 through 69 we have that the hidden unit updates prescribed
by the the forward alignment algorith, ∆FAh, are always a positive scalar multiple of
the hidden unit updates prescribed by the pseudobackprop algorithm, ∆PBPh. That is
∆FAh = s∆PBPh
(78)
where s is a positive scalar.
Proof. By lemma 5 we have that W = sw˜y(B˜y)T, with sw a positive scalar, and that
e = (1 −sy)˜y, with (1 −sy) a positive scalar. Thus, since ∆FAh = η(1 −sy)B˜y
(equation 75) and ∆FAh = η(1 −sy)W +˜y it sufﬁces to show that
sB˜y =
 ˜y(B˜y)T+ ˜y,
(79)
26


## Page 27


with s a positive scalar. We show this by manipulating the left hand side of equation
79.
 ˜y(B˜y)T+ ˜y = (B˜y)T+ ˜y+˜y
= BT+˜yT+˜y+˜y
= BT+˜yT+˜yT ˜yT+˜y
(80)
= BT+˜yT+
= (B˜y)T+
= sB˜y
Here s = (B˜y)T (B˜y).
27

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]