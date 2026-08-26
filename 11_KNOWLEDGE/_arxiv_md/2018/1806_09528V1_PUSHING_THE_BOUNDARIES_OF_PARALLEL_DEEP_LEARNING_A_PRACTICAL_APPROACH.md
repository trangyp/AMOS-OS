---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1806.09528v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1806.09528v1_Pushing_the_boundaries_of_parallel_Deep_Learning_--_A_practical_approach

> Source: 1806.09528v1_Pushing_the_boundaries_of_parallel_Deep_Learning_--_A_practical_approach.pdf

> Pages: 12

---


## Page 1


Pushing the boundaries of parallel Deep Learning – A
practical approach
Paolo Viviani
Computer Science Dept.
University of Torino, Italy
Noesis Solutions NV
pviviani@unito.it
Maurizio Drocco
Paciﬁc Northwest National Lab.
maurizio.drocco@pnnl.gov
Marco Aldinucci
Computer Science Dept.
University of Torino, Italy
aldinuc@di.unito.it
Abstract
This work aims to assess the state of the art of data parallel deep neural network
training, trying to identify potential research tracks to be exploited for performance
improvement. Beside, it presents a design for a practical C++ library dedicated at
implementing and unifying the current state of the art methodologies for parallel
training in a performance-conscious framework, allowing the user to explore novel
strategies without departing signiﬁcantly from its usual work-ﬂow.
1
Introduction
As deep learning techniques become more and more popular, there is the need to move these
applications from the data scientist’s Jupyter notebook to reliable and efﬁcient enterprise solutions.
This aim involves several steps to be taken, and this work advocates the need to push the current state
of the art in parallel training in order to achieve: 1. faster end-to-end training for large production
datasets; 2. distributed training on the edge, namely on a number of heterogeneous, low-power,
and loosely-coupled devices (i.e. for privacy constraints); 3. training code that can be redistributed,
possibly in form of binaries (i.e. to train models at customer’s premises without exposing sensitive
Python code). To practically implement this vision are required a number of advancements, this work
represents a ﬁrst step towards:
1. a better theoretical understanding of the different strategies of data parallelism in deep neural
networks;
2. a consistent way to compare different deployments and strategies.
Issues related to point 1 will be presented, addressing some of them and discussing how it is possible
to push further the model training efﬁciency; moreover, this paper will propose a design for a
programming framework that would address point 2.
Sec. 2 presents a survey of parallel techniques for deep neural network training, the next section
provides a further exploration of some theoretical highlights that can be exploited to improve training
scalability. Sec. 4 presents a design for an upcoming data parallel training framework and, ﬁnally,
sec. 5 provides an outlook of the potential impact of the presented results as well as the opportunities.
2
Background
Performance issues in deep neural networks (DNNs) have been extensively investigated from many
point of views: in particular it is possible to clearly discriminate between the training stage and the
inference stage. The latter is usually characterised by smaller computational workloads that are,
however, highly constrained by time, memory, and power consumption due to the deployment on
Preprint. Work in progress.
arXiv:1806.09528v1  [cs.DC]  25 Jun 2018


## Page 2


portable devices that need predictions almost in real-time. This paper is focused on the former stage
of deep neural network training. A comprehensive survey of the state of the art for parallel DNN
training been done by Ben-Nun and Hoeﬂer [1], it is among the goals of this paper to review a subset
of the relevant work, providing a more critical insight.
To further focus the research scope of this work, it is useful to highlight the main categorization
of parallel training: namely data parallelism vs. model parallelism. Data parallelism focuses on
distributing partitions of training data among workers, that cooperate to train replicas of the same
model; model parallelism involves the partition of the model computation graph among different
workers, that train different parts of the same model instance. While the latter (including layer
pipelining) has been proved to be an efﬁcient way to improve the performance of DNN training
[2, 3, 4, 5] it can be argued that its capacity to scale beyond the single machine is limited by the
higher frequency of communications with respect to data parallelism, especially if the distributed
workers are loosely coupled (i.e. cloud instances without dedicated interconnection, edge devices).
Moreover, model parallelism can be used transparently within a distributed data parallel set-up to
improve node-level performance, hence it represents an orthogonal direction of improvement with
respect to data parallelism. In fact, this aspect is not explored in this work, but it can be quickly
added to the data parallel strategies discussed later as a further optimization, without impacting the
following discussion.
2.1
Mathematical notation
Despite the many attempts to implement different optimizations strategies [6], back-propagation
[7, 8, 9, 10] with some ﬂavour of gradient descent [11] is still the most popular way to train deep
neural networks, mostly due to its high efﬁciency on modern architectures like GPUs [12]. This
section present some useful notation for gradient descent-based neural network training.
For the rest of this section it will be considered that a dataset X = {x1, . . . , xn}, is used to train a
neural network represented here as a collection of parameters (weights) w = {w1, . . . , wm}. Here-
after, neither the network type and topology (i.e. convolutional, recurrent, number of hidden layers)
nor the input dimensionality and shape are considered relevant, as the formalism is generally applied
to all of them. Mini-batch gradient descent [13, 14, 10] has quickly became the standard, combining
the faster convergence of Stochastic (on-line) Gradient Descent (SGD) [15, 16, 17], with the more
efﬁcient computation of batch gradient descent. The optimization step for training can be expressed
as the following weight update, computed with respect to a mini-batch X(i,nb) = {xi, . . . , xi+nb−1}:
wk(t + 1) = wk(t) −η
nb
i+nb−1
X
j=i
∂L (w(t), xj)
∂wk
(1)
where t represents the current gradient descent iteration (step), η is the so-called learning rate that
deﬁnes the size of the step to be taken in the direction of the steepest descent, and ∂L(w,xj)/∂wkis
the partial derivative of the loss function of the neural network with respect to the weight wk, when
calculated on the training sample xj. The partial derivative is averaged over all the samples belonging
to a given subset (the mini-batch) of the training dataset of size nb. It is useful to recall the deﬁnition
of all the versions of gradient descent by means of the value of nb:
• nb = 1, stochastic gradient descent
• 1 < nb ≪n, mini-batch gradient descent
• nb = n, batch gradient descent
Note that batch averaging, as opposite of just summing, has a non-trivial impact on the convergence
of the training [11]. It is also useful to deﬁne the gradient for all the weights of the model as following
∇L(w, xj) =
∂L (w, xj)
∂w1
, . . . , ∂L (w, xj)
∂wm

(2)
this represents the direction of steepest slope of the loss surface calculated with respect to xj in the
parameter’s space (L : Rm →R); it is trivial to obtain the gradient and the step with respect to the
2


## Page 3


Input
xi
DNN
w
Output
y(pred)
i
Loss
L(w, xi)
Labels
yi
Gradients
w ←w −η∇L(w, xi)
Figure 1: Back-propagation diagram for on-line gradient descent.
whole mini-batch X(i,nb) as
1
nb
i+nb−1
X
j=i
∇L(w, xj)
def
= ∆L(w, X(i,nb))
w(t + 1) = w(t) −η∆L(w, X(i,nb))
(3)
Equation 1 represents the simplest form of mini-batch gradient descent. Several algorithms have
been developed to improve the convergence rate of DNN training, a good review of them can be
found in literature [18, 19]. The key points of these evolved algorithms are: 1. variable learning rate,
η →η(t); 2. accounting for previous gradient steps (e.g. momentum [20]); 3. deﬁning a different
learning rate for each weight η(t) →η(t, wk) (e.g. ADAM [21]). These points have an impact on
parallel training implementation that will be discussed later.
2.2
Training parallelism
When considering the whole feed-forward/back-propagation [7] training process, it is important
to remark that it is, to some extent, intrinsically sequential. Figure 1 and equation (1) show how
the gradient value depend on the present w(t) conﬁguration and how its application through back-
propagation produces a new conﬁguration w(t + 1): the new weights represent a data dependency for
the feed-forward step for sample xi+1, that must come strictly after the back-propagation, otherwise
the gradient would be calculated based on outdated (stale) weights. In principle this prevents any kind
of input sample-based parallelism while, in fact, this is true strictly for on-line SGD: the concept itself
of batch (or mini-batch) gradient descent involves parallelism. The gradients related to all the samples
in the (mini-)batch are computed based on the same value of w and, possibly, at the same time. It is
worth noting that the data dependency depicted in ﬁgure 1, is introduced by on-line training algorithm
and not by the problem itself, hence there is room to relax this dependency, either with mini-batches
or with more sophisticated techniques that relax the dependencies between mini-batches. Figure 2
exempliﬁes a possible behaviour of SGD on a loss surface: it is not necessarily true that using always
the most recent gradient leads to the best training accuracy, even the red update could end up to
good loss minimum. In this sense is important to remember that the loss surface of DNNs is highly
non-linear and difﬁcult to describe globally [22, 23]: a certain amount of noise and randomness
associated to the gradient descent can be beneﬁcial to the training outcome in terms of generalization.
The next subsections will describe how this behaviour can be exploited to introduce some degree of
parallelism into the training process.
2.2.1
Synchronous parallelism
As stated before, mini-batch gradient descent combines the best of both on-line and batch training; in
particular, the fact that it can be expressed as a chain of matrix-matrix multiplication (GEMMs) [10]
that allow for a very efﬁcient implementation on multicore CPUs and GPUs [11], enabled a wide
adoption of deep learning due to the better training feasibility. From the parallel computing point
of view, mini-batches represent the most elementary approach to what is called synchronous data
parallel training, as a global synchronization happens at the end of each mini-batch.
The amount of available parallelism depends on the size of the mini-batches, that in turn affects the
convergence of the training. Apart from avoiding the extreme cases of on-line and batch gradient
descent, the choice of the right mini-batch size is not trivial, and there is interaction with other
hyper-parameters, like the learning rate, as widely discussed in literature [23, 24, 25, 26, 27, 28] often
3


## Page 4


w(0)
w(1) = w(0) + δ1
0
w(0) + δ2
0
w(1) + δ2
0
w(1) + δ2
1
Figure 2: Gradient descent in w space. δj
i = −η∇L(w(i), xj) represents the gradient calculated on
the weights updated up to step i, based on sample (or mini-batch) xj. Therefore, the red update based
on δ2
0 is outdated with respect to w(1), but its impact is not necessarily detrimental to the training.
The target function is L : Rm →R.
concerning the linear scaling of η. In principle, larger mini-batches allow to process more samples
per unit of time, while the convergence can be hindered if the size is too large.
Mini-batch parallelism is usually exploited by means of parallel GEMMs on suitable architectures
[12, 29, 30]. However, recent works [31, 32, 33] have demonstrated that it is possible to push the
mini-batch size further than previously expected without affecting the model convergence. These
works leverage distributed GPU architectures in order to allocate and efﬁciently compute such
large mini-batches, while relying on an all-reduce communication pattern to perform the global
synchronization. Ignoring the communication bottlenecks that will be discussed in Sec. 2.2.4, it can
be argued that this approach is problem-speciﬁc and can not always be pushed as far as [31] suggests.
In fact, smaller mini-batches (∼32) provide usually better generalization performance [10, 23, 28].
This induces a granularity problem: smaller batches can be effectively computed only if the size
of the network and the complexity of the individual data sample (e.g. large RGB picture vs. small
array of numerical data) are large enough to saturate the given platform even with only few samples
being processed concurrently. This issue can heavily affect the capability of certain models to scale
on large distributed clusters. A further issue is the so-called batch normalization (BN) [34], that
introduces data dependencies between different samples among the same mini-batch, such that a full
synchronization is required at each invocation of BN.
Parallelism at mini-batch level proved to be effective at node-level when implemented on GPUs,
multi-core CPUs or other dedicate hardware (e.g. Google TPUs [35]); still, the scalability of its
extension to distributed memory architectures is subject to a suitable problem granularity, that is far
from being granted apart from speciﬁc problems.
Further parallel implementation of DNN training usually take mini-batch parallelism for granted,
at least at node-level, considering mini-batches as atomic entities for which the data dependency
deﬁned in Figure 1 exists. From this point of view, mini-batches can be considered the only truly
synchronous kind of parallel training: while other strategies that will be presented in the next sections
might involve synchronizations at certain stages, they necessarily relax the dependency between
subsequent mini-batches. Indeed, in the rest of this paper mini-batches will be considered as atomic
entities, that cannot be further divided. Synchronous distributed parallelism at mini-batch level will
also be addresses as large mini-batch parallelism.
2.2.2
Asynchronous parallelism
The success of momentum as a method to accelerate the training convergence, show that the infor-
mation of previous gradients is deﬁnitely relevant even at the current iteration. Although the idea of
trading gradient staleness for computational efﬁciency can be also related a posteriori to the usage
of mini-batches, as highlighted by Masters and Luschi [28], this notion has been at ﬁrst exploited
for what is deﬁned asynchronous parallel training. As the name suggests, this strategy involves
multiple workers performing their own gradient descent for a certain amount of iterations, while their
ﬁndings (i.e. new weights, accumulated gradients) are shared with other workers without a global
synchronization at the mini-batch level.
There is a common categorization [1] between centralized and de-centralized implementations,
as well as based the degree of model consistency achieved. The latter is a property of a given
4


## Page 5


implementation that measures how different are the weights of each model replica at a certain instant
of time, while the former categorization regards the usage of a centralized parameter server to store a
“master copy” of the model weights or, otherwise, to coordinate the exchange of gradients without a
central authority. Sec. 3 will further discuss these classiﬁcations. Early notable implementations of
asynchronous parallel gradient descent are HOGWILD! [36] and its deep learning-focused derivatives
like Downpour SGD [2, 37]; followed by some other signiﬁcant works [38, 39, 40, 41, 42, 43, 44].
Apart from the DistBelief [2] and Project Adam [37] papers, that presented results previously not
achievable and moved deep learning resolutely into the HPC domain, most of other works, while
reporting solid scalability and timing results, were not able to provide a signiﬁcant legacy. In fact,
the dominating entries from DAWNBench [45], at the time of writing, are still relatively small-scale,
synchronous implementations.
While this review is far from being conclusive, it is possible to suggest some limitations that arguably
prevented widespread adoption of asynchronous techniques. For instance, the added complexity of a
parameter server or a sophisticated decentralized protocol might be perceived as not necessary since
synchronous, all-reduce-based, parallelism has mostly satisﬁed the quest for deep learning scalability
up to this point. Moreover, most of these works present asynchronous implementations of naive SGD,
while the state of the art is moving to more sophisticated algorithms like ADAM [21]. Some effort in
this directions exists [46], as well as a prominent theoretical work [47] that links gradient staleness to
momentum; still, the literature is lacking a comprehensive analysis of the asynchronous behaviour
of algorithm beyond SGD. Finally, results are usually reported as a collection of experiments on
speciﬁc use cases, lacking a generalization effort that might help to understand the validity of the
methodology. In this sense a relevant analysis has been performed by Lian et. al [48]: the theoretical
discussion of the convergence rate for an asynchronous, decentralized algorithm represent a good
starting point for a performance analysis. However, it can be argued that the real life behaviour
is affected by a large number of variables (e.g. weight update protocol,communication latencies,
etc.) that prevent this model to fully describe the performance of a given implementation. These
limitations, along with the lack of details on the code and framework used for experiments, lay the
ground for a research that aims to ﬁll the gap between sparse experimentation and mathematical
modelling of convergence rates.
2.2.3
Other approaches
Synchronous and asynchronous SGD are not the only ways to exploit concurrency in DNN training.
Model averaging [49, 50, 51] allow concurrent model replicas to perform training independently up
to a certain point (i.e. from several mini-batches to multiple epochs), then the weights are averaged
among the different replicas. Ensemble learning [52, 53] performs the whole training on different
model instances, then averages the predictions among them. As said before with respect to model
parallelism, ensemble learning represents an orthogonal direction of improvement with respect to
parallel gradient descent, hence it will not be discussed hereafter. On the other hand, model averaging
is strictly related to the techniques presented in Sec. 2.2.1 and 2.2.2 and, while it is out of the scope
of this paper to formally draw the connection, it will be investigated in the near future.
2.2.4
Further parallelism issues
As said in Sec. 2.2.1, mini-batch parallelism tends to be performed within a single node, either
in shared memory or distributed among multiple GPU. The computing horsepower provided by
GPUs or other dedicated hardware is usually enough for most applications, still, there is the need
to push the capability to train DNNs effectively beyond the single node. While large mini-batches
and asynchronous techniques can be applied also within a single machine when the problem is small
enough, representing an interesting research domain itself, they are born to be distributed; this raises
a number of issues related to the communication of gradient updates.
The size of the gradient set (∆L(w, X(i,nb)) for a state of the art DNN easily reaches a few hundred
MB [54]. This represents a serious bottleneck for distributed implementations and two main tech-
niques are used to reduce the size of the gradient set to be transmitted: quantization and sparsiﬁcation.
The former intends to reduce the precision of the gradient representation in order to reduce its overall
size and it is demonstrated that this technique works up to 1-bit representation [55, 39]; the latter
exploits the sparsity that naturally occurs in DNN gradients, where most of the components are
zero or almost zero. In this way the array gradient component can be represented as sparse and
5


## Page 6


w0
wA
1 = w0 + δA
1 (w0)
wA
1 + δA
2 (wA
1 )
Not received
wA
1 + δB
1 (w0)
+δA
2 (wA
1 + δB
1 (w(0))
Received
Worker A
wB
1 = w0 + δB
1 (w0)
wB
1 + δB
2 (wB
1 )
Not received
wB
1 + δA
1 (w0)
+δB
2 (wB
1 + δA
1 (w0))
Received
Worker B
δ?
−→
←−
time
Figure 3: Diagram of weights update between two workers. w0 is the common starting conﬁguration.
Assuming that all the updates that are not immediatly applied are queued somewhere, commutativity
and associativity of vector sum guarantee that A and B will always be consistent once the queues are
emptied.
compressed with well-known techniques [39]. A more recent work [54] also includes momentum in
the discussion and presents interesting results. Also in this case, apart from the 1-bit quantization
provided by Microsoft CNTK [56], the frameworks used are not mentioned nor the code is made
available.
More methodologies can be exploited to enhance the performance of distributed training, like the
optimization of the all-reduce pattern required by the large mini-batch training or the overlapping of
computation and communication during training. Even if these techniques fall more in the domain of
the implementation details than in the ﬁeld of parallel training algorithms, they play a non-negligible
role in the overall training performance: this paper highlights the need of a general purpose framework
that provides the tools to experiment with existing techniques at different levels (i.e. asyncronous vs.
synchronous, different communication patterns, quantization, etc.), as well as deﬁning and testing
new ones. Sec. 4 will discuss the requirements for such framework.
3
Theoretical discussion
Assuming that using very large mini-batches is not suitable for any application, end-to-end training
performance can be improved at two distinct levels:
1. at node level
• by implementing tensor operations in back-propagation even more efﬁciently;
• by developing new dedicated hardware that is better suited to handle small mini-batches;
2. at distributed level
• by improving parallel gradient descent without falling back-on large mini-batches;
• by developing a different optimization strategy that exploits parallelism better than
gradient descent.
Point 1 is being researched actively [57, 58] and it is clearly out of the scope of this paper. Also the
development of algorithms that departs completely from gradient descent is an interesting topic, still
this work is focused on improving on parallel gradient descent. In this sense it is possible to show
that, despite usually being treated as different approaches, all the techniques discussed in Sec. 2.2.1
and 2.2.2 can be placed on a spectrum of communication completeness, namely the property of
parallel implementation to distribute each gradient update from each worker to all the other workers,
regardless of the time at which this happens. It is indeed possible to argue that the model consistency
spectrum usually proposed [1], provides limited insight to understand what happens to model replicas
in implementations presented in previous works. A statement can be formulated in this sense that,
while being quite naïve, it is still important to understand the behaviour of model replicas
Statement 1 Assuming mini-batch SGD without momentum in a distributed setting, if all the gradient
updates (communications) are delivered to all the workers, regardless of the delay, all the model
replicas will be consistent.
Figure 3 presents the diagram of subsequent gradient updates for 2 workers: using commutativity and
associativity of the vector sum that represent the gradient update, it is trivial to prove that, if an event
6


## Page 7


triggers the application of all the pending updates (e.g. a global synchronization), whatever is the
state of both workers before the event, their state will be consistent afterwards. Of course statement 1
does not hold if, for instance, updates not yet received are simply dropped, instead of accumulated.
Moreover, it must be highlighted that having consistent model replicas does not mean that the result
is the same as the sequential implementation, but only that all the model replica will agree on the
value of w at a certain time. It is also important remark that consistency is not implied at any given
moment, but it is always achieved as most of the strategies proposed either accumulate all the updates
in a parameter server or require a synchronization at each epoch [39] or both.
In this sense there is also no need to distinguish between centralized and de-centralized set-ups if the
communication is complete; in fact there it becomes only matter of implementation to choose the
approach, while the model consistency is granted. While a centralized parameter server can simplify
the measurement of gradient staleness, it is still possible to envision a distributed system that takes
staleness into account.
This discussion is relevant as our goal is to exploit more parallelism without resorting to large
mini-batch training; however, workers in ﬁgure 3 always go through the received branch the outcome
is, not surprisingly, exactly equal to the large mini-batch strategy. Less trivially, it is possible to
ﬁgure that this is exactly what happens in an homogeneous, de-centralized set-up, where the load
is perfectly balanced and updates are broadcast by each worker to all the others [39], making an
asynchronous solution not different from a synchronous one. Of course it can be argued that not
enforcing explicit synchronization can beneﬁt scalability on very large-scale deployment, however, it
does not beneﬁt the training as it is bound to an approximation of very large mini-batches.
It is useful at this point to deﬁne a new spectrum to discriminate between strategies:
1. Synchronous communication (large mini-batches)
2. Complete communication with bound delay (stale-synchronous [40])
3. Complete communication with unbound delay (Downpour SGD [2])
4. Partial communication ([59, 60])
It is important to remark that, when applied in an homogeneous environment with high-bandwidth,
low-latency interconnection (i.e. any common HPC set-up), the ﬁrst three points are not signiﬁcantly
distinguishable in terms of training convergence. It is true that a centralized set-up with a parameter
server forces a degree of asynchrony since gradient updates are queued, still this is more a limitation
of the centralized implementation that a property of this strategy, moreover the centralized approach
introduces an obvious bottleneck. Point 4 would be, instead, a signiﬁcant departure from large
mini-batches, and its beneﬁt on the training convergence should be deﬁnitely investigated, while its
scalability can be expected to be almost linear in terms of samples processed per unit of time, as
it is for most of the asynchronous implementations. Moreover, this approach would signiﬁcantly
beneﬁt in loosely-coupled heterogeneous environments (e.g. edge), where the communication is
costly and unreliable. However, while partial communication has been explored theoretically in
generic optimization context [59], no deep learning-related investigation has been conducted.
It is clear that allowing partial communication deﬁnitely gives up on model consistency, even in
the long run. The impact of this on the training must be better understood, as well as the policy to
determine which model to choose as representative when the training ends. This last issue is also
strictly related to the possibility to terminate some workers at any given time without impacting the
overall convergence: this matter has been already discussed [2], but only from the point of view of
fault tolerance of the training system, not in terms of training accuracy. Finally, it is necessary to
investigate the impact of partial communication when more sophisticated optimization algorithms
are used in place of naïve SGD. Momentum arises implicitly when introducing stale gradients [47],
but there is no clear understanding of what happens in case of incomplete communication, as well
as for more sophisticated algorithms with variable learning rates. It is reasonable to expect that
the discussion made for the synchronous case by Goyal et al. [31] on momentum correction and
aggregation of gradients subject to momentum can be extended for asynchronous set-ups with also
implicit momentum and investigation is in progress in this sense.
To wrap up the discussion, asynchronous gradient descent with partial communication seems a
promising alternative to more popular methodologies. The next section will discuss the requirements
of a framework that can enable efﬁcient experimentation on this topic.
7


## Page 8


Tensorﬂow
PyTorch
MxNet
...
FAST tensor moving interface
FAST high-level strategies
C++ or Python business logic
Figure 4: FAST logical stack.
4
FAST C++ framework
This library is currently1 under development and not yet publicly available. In order to provide
a truly general purpose tool, as well as to exploit the peculiarities of the different deep learning
frameworks available, the proposed FAST (Flexible (A)synchronous Scalable Training) approach
intends to decouple the intra-node execution of the training from the parallel coordination of workers;
in fact it is reasonable that the user desires to keep using its framework of choice (e.g. Tensorﬂow,
PyTorch, MxNet).
The main feature will be a general purpose tensor moving interface that allows the developer to
send and receive any kind of tensor between model replicas, offering pre-deﬁned compression and
sparsiﬁcation strategies. To achieve performance without loosing the ﬂexibility and programmability
required to a general purpose tool, a novel, state of the art, take on distributed shared memory
will be leveraged [61]. This interface will be both proposed to the user as-is to experiment novel
approaches, and wrapped in a number of higher-level strategies based on literature, spanning the
whole spectrum presented in Sec. 3. GPU-GPU communication for device-based tensors will be
part of the implementation. Figure 4 presents the logical stack of components: this structure is also
expected to allow better reproducibility of previous results while factoring out all the node-level
performance optimizations, that are delegated to the underlying framework.
The library is designed from scratch with C++ training in mind, according to the aim of making
training code redistributable, while potentially target training in production and keeping the overhead
as low possible. However, due to the prevalence of Python for DNN training, Python wrappers will
be provided compatible with selected frameworks.
5
Conclusion and future work
It is very likely that the next breakthrough in training performance will either come from new
dedicated silicon architectures or from theoretical advancements in optimizations techniques that
departs from gradient descent. However, at this stage, the quest for training performance at scale has
been met mostly by synchronous, large mini-batch, parallelism; unfortunately this strategy is heavily
problem-dependent, moreover, it is not suitable for other platforms than conventional HPC clusters
and tightly coupled cloud instances.
This paper endorses a departure from both synchronous and conventional asynchronous training,
as they both perform similarly in terms convergence when working within a high-performance
infrastructure. Instead, asynchronous training with sparse communication is expected to introduce
a degree of randomization in the interleaving of updates coming from different mini-batches that
represents a novelty with respect to large mini-batches and might arguably be beneﬁcial to the
training.
This approach would require an effort on both the theoretical and experimental side, in order to
investigate the potential issues reported in Sec. 3. This work is currently taking place and tackles the
issues related to model inconsistency that derives from partial communications, while the development
of FAST library will allow to validate theoretical results on real models and datasets.
1Tuesday 26th June, 2018
8


## Page 9


References
[1] T. Ben-Nun and T. Hoeﬂer, “Demystifying Parallel and Distributed Deep Learning: An
In-Depth Concurrency Analysis,” CoRR, vol. abs/1802.09941, 2018. [Online]. Available:
http://arxiv.org/abs/1802.09941
[2] J. Dean, G. S. Corrado et al., “Large Scale Distributed Deep Networks,” in Proceedings
of the 25th International Conference on Neural Information Processing Systems - Volume
1, ser. NIPS’12.
USA: Curran Associates Inc., 2012, pp. 1223–1231. [Online]. Available:
http://dl.acm.org/citation.cfm?id=2999134.2999271
[3] J. Ngiam, Z. Chen et al., “Tiled convolutional neural networks,” in Advances in Neural
Information Processing Systems 23, J. D. Lafferty, C. K. I. Williams, J. Shawe-Taylor, R. S.
Zemel, and A. Culotta, Eds.
Curran Associates, Inc., 2010, pp. 1279–1287. [Online].
Available: http://papers.nips.cc/paper/4136-tiled-convolutional-neural-networks.pdf
[4] X.
Chen,
A.
Eversole,
G.
Li,
D.
Yu,
and
F.
Seide,
“Pipelined
Back-
Propagation
for
Context-Dependent
Deep
Neural
Networks,”
Microsoft
Research,
Sep. 2012. [Online]. Available:
https://www.microsoft.com/en-us/research/publication/
pipelined-back-propagation-for-context-dependent-deep-neural-networks/
[5] L. Deng, D. Yu, and J. Platt, “Scalable stacking and learning for building deep architectures,” in
2012 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP),
Mar. 2012, pp. 2133–2136.
[6] J. Schmidhuber, “Deep learning in neural networks:
An overview,” Neural Networks,
vol. 61,
no. Supplement C, pp. 85–117,
Jan. 2015. [Online]. Available:
http:
//www.sciencedirect.com/science/article/pii/S0893608014002135
[7] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” Nature, vol. 521, no. 7553,
p. 436,
May 2015. [Online]. Available:
https://www-nature-com.bibliopass.unito.it:
2443/articles/nature14539
[8] P. J. Werbos, “Applications of advances in nonlinear sensitivity analysis,” in System Modeling
and Optimization, ser. Lecture Notes in Control and Information Sciences.
Springer, Berlin,
Heidelberg, 1982, pp. 762–770. [Online]. Available: https://link.springer.com/chapter/10.1007/
BFb0006203
[9] Y. LeCun, “A theoretical framework for back-propagation,” in Proceedings of the 1988 Connec-
tionist Models Summer School, CMU, Pittsburg, PA, D. Touretzky, G. Hinton, and T. Sejnowski,
Eds.
Morgan Kaufmann, 1988, pp. 21–28.
[10] Y. LeCun, L. Bottou, G. B. Orr, and K.-R. Müller, “Efﬁcient BackProp,” in Neural Networks:
Tricks of the Trade, ser. Lecture Notes in Computer Science. Springer, Berlin, Heidelberg, 1998,
pp. 9–50. [Online]. Available: https://link.springer.com/chapter/10.1007/3-540-49430-8_2
[11] Y. Bengio, “Practical Recommendations for Gradient-Based Training of Deep Architectures,”
in Neural Networks: Tricks of the Trade, ser. Lecture Notes in Computer Science.
Springer,
Berlin, Heidelberg, 2012, pp. 437–478. [Online]. Available: https://link.springer.com/chapter/
10.1007/978-3-642-35289-8_26
[12] R. Raina, A. Madhavan, and A. Y. Ng, “Large-scale Deep Unsupervised Learning Using
Graphics Processors,” in Proceedings of the 26th Annual International Conference on Machine
Learning, ser. ICML ’09.
Montreal, Quebec, Canada: ACM, 2009, pp. 873–880. [Online].
Available: http://doi.acm.org/10.1145/1553374.1553486
[13] G. B. Orr, “Removing Noise in On-Line Search using Adaptive Batch Sizes,” in Advances
in Neural Information Processing Systems 9, M. C. Mozer, M. I. Jordan, and T. Petsche,
Eds.
MIT Press, 1997, pp. 232–238. [Online]. Available:
http://papers.nips.cc/paper/
1257-removing-noise-in-on-line-search-using-adaptive-batch-sizes.pdf
[14] M. Moller, “Supervised learning on large redundant training sets,” in Neural Networks for
Signal Processing II Proceedings of the 1992 IEEE Workshop, Aug. 1992, pp. 79–89.
[15] L. Bottou and O. Bousquet, “The Tradeoffs of Large Scale Learning,” in Advances in
Neural Information Processing Systems, J. Platt, D. Koller, Y. Singer, and S. Roweis, Eds.
NIPS Foundation (http://books.nips.cc), 2008, vol. 20, pp. 161–168. [Online]. Available:
http://leon.bottou.org/papers/bottou-bousquet-2008
9


## Page 10


[16] D. R. Wilson and T. R. Martinez, “The general inefﬁciency of batch training for gradient
descent learning,” Neural Networks, vol. 16, no. 10, pp. 1429–1451, Dec. 2003. [Online].
Available: http://www.sciencedirect.com/science/article/pii/S0893608003001382
[17] L. Bottou and Y. LeCun, “Large Scale Online Learning,” in Advances in Neural Information
Processing Systems 16, S. Thrun, L. K. Saul, and B. Schölkopf, Eds.
MIT Press, 2004, pp.
217–224. [Online]. Available: http://papers.nips.cc/paper/2365-large-scale-online-learning.pdf
[18] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning.
Cambridge, MA: MIT Press,
2016. [Online]. Available: http://www.deeplearningbook.org
[19] S. Ruder,
“An overview of gradient descent optimization algorithms,”
CoRR, vol.
abs/1609.04747, 2016. [Online]. Available: http://arxiv.org/abs/1609.04747
[20] N. Qian, “On the momentum term in gradient descent learning algorithms,” Neural
Networks,
vol. 12,
no. 1,
pp. 145–151,
Jan. 1999. [Online]. Available:
http:
//www.sciencedirect.com/science/article/pii/S0893608098001166
[21] D. P. Kingma and J. Ba, “Adam: A Method for Stochastic Optimization,” CoRR, vol.
abs/1412.6980, 2014. [Online]. Available: http://arxiv.org/abs/1412.6980
[22] A. Choromanska, M. Henaff, M. Mathieu, G. B. Arous, and Y. LeCun, “The Loss Surfaces of
Multilayer Networks,” in Proceedings of the Eighteenth International Conference on Artiﬁcial
Intelligence and Statistics, ser. Proceedings of Machine Learning Research, G. Lebanon and
S. V. N. Vishwanathan, Eds., vol. 38.
San Diego, California, USA: PMLR, May 2015, pp.
192–204. [Online]. Available: http://proceedings.mlr.press/v38/choromanska15.html
[23] N. S. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy, and P. T. P. Tang, “On
Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima,” CoRR, vol.
abs/1609.04836, 2016. [Online]. Available: https://arxiv.org/abs/1609.04836
[24] L. Bottou,
F. E. Curtis,
and J. Nocedal,
“Optimization Methods for Large-Scale
Machine Learning,”
CoRR, vol. abs/1606.04838,
2016. [Online]. Available:
https:
//arxiv.org/abs/1606.04838
[25] S. Jastrzebski, Z. Kenton et al., “Three Factors Inﬂuencing Minima in SGD,” CoRR, vol.
abs/1711.04623, 2017. [Online]. Available: https://arxiv.org/abs/1711.04623
[26] S. L. Smith, P.-J. Kindermans, and Q. V. Le, “Don’t Decay the Learning Rate, Increase the Batch
Size,” CoRR, vol. abs/1711.00489, 2017. [Online]. Available: https://arxiv.org/abs/1711.00489
[27] J. Chen, R. Monga, S. Bengio, and R. Józefowicz, “Revisiting Distributed Synchronous SGD,”
CoRR, vol. abs/1604.00981, 2016. [Online]. Available: http://arxiv.org/abs/1604.00981
[28] D. Masters and C. Luschi, “Revisiting Small Batch Training for Deep Neural Networks,” ArXiv
e-prints, 2018. [Online]. Available: https://arxiv.org/abs/1804.07612
[29] J. Bergstra, F. Bastien et al., “Theano: Deep Learning on GPUs with Python,” in Big Learn
Workshop, NIPS’11, 2011.
[30] S. Chetlur, C. Woolley et al., “cuDNN: Efﬁcient Primitives for Deep Learning,” CoRR, vol.
abs/1410.0759, 2014. [Online]. Available: https://arxiv.org/abs/1410.0759
[31] P. Goyal, P. Dollár et al., “Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour,”
CoRR, vol. abs/1706.02677, 2017. [Online]. Available: http://arxiv.org/abs/1706.02677
[32] M. Cho, U. Finkler et al., “PowerAI DDL,” CoRR, vol. abs/1708.02188, 2017. [Online].
Available: http://arxiv.org/abs/1708.02188
[33] T. Akiba, S. Suzuki, and K. Fukuda, “Extremely Large Minibatch SGD: Training ResNet-50
on ImageNet in 15 Minutes,” CoRR, vol. abs/1711.04325, 2017. [Online]. Available:
https://arxiv.org/abs/1711.04325
[34] S. Ioffe and C. Szegedy, “Batch Normalization: Accelerating Deep Network Training by
Reducing Internal Covariate Shift,” CoRR, vol. abs/1502.03167, 2015. [Online]. Available:
https://arxiv.org/abs/1502.03167
[35] N. P. Jouppi, C. Young et al., “In-Datacenter Performance Analysis of a Tensor Processing
Unit,” CoRR, vol. abs/1704.04760, 2017. [Online]. Available: https://arxiv.org/abs/1704.04760
[36] F. Niu, B. Recht, C. Ré, and S. J. Wright, “HOGWILD!: A Lock-Free Approach to
Parallelizing Stochastic Gradient Descent,” CoRR, vol. abs/1106.5730, 2011. [Online].
Available: http://arxiv.org/abs/1106.5730
10


## Page 11


[37] T. Chilimbi, Y. Suzue, J. Apacible, and K. Kalyanaraman, “Project Adam: Building an
Efﬁcient and Scalable Deep Learning Training System,” in 11th USENIX Symposium on
Operating Systems Design and Implementation (OSDI 14).
Broomﬁeld, CO: USENIX
Association, 2014, pp. 571–582. [Online]. Available: https://www.usenix.org/conference/
osdi14/technical-sessions/presentation/chilimbi
[38] T. Paine, H. Jin, J. Yang, Z. Lin, and T. S. Huang, “GPU Asynchronous Stochastic Gradient
Descent to Speed Up Neural Network Training,” CoRR, vol. abs/1312.6186, 2013. [Online].
Available: https://arxiv.org/abs/1312.6186
[39] N. Strom, “Scalable Distributed DNN Training Using Commodity GPU Cloud Computing,”
Dresden, Sep. 2015. [Online]. Available: http://www.isca-speech.org/archive/interspeech_2015/
i15_1488.html
[40] W.
Zhang,
S.
Gupta,
X.
Lian,
and
J.
Liu,
“Staleness-aware
Async-SGD
for
Distributed Deep Learning,” CoRR, vol. abs/1511.05950, 2015. [Online]. Available:
http://arxiv.org/abs/1511.05950
[41] S. Zheng, Q. Meng et al., “Asynchronous Stochastic Gradient Descent with Delay
Compensation for Distributed Deep Learning,” CoRR, vol. abs/1609.08326, 2016. [Online].
Available: http://arxiv.org/abs/1609.08326
[42] J. Keuper and F.-J. Pfreundt, “Asynchronous Parallel Stochastic Gradient Descent - A Numeric
Core for Scalable Distributed Machine Learning Algorithms,” CoRR, vol. abs/1505.04956,
2015. [Online]. Available: http://arxiv.org/abs/1505.04956
[43] J. Hermans, G. Spanakis, and R. Möckel, “Accumulated Gradient Normalization,” CoRR, vol.
abs/1710.02368, 2017. [Online]. Available: http://arxiv.org/abs/1710.02368
[44] X. Lian, C. Zhang et al., “Can Decentralized Algorithms Outperform Centralized Algorithms?
A Case Study for Decentralized Parallel Stochastic Gradient Descent,” CoRR, vol.
abs/1705.09056, 2017. [Online]. Available: https://arxiv.org/abs/1705.09056
[45] C. A. Coleman, D. Narayanan et al., “DAWNBench : An End-to-End Deep Learning Benchmark
and Competition,” 2017. [Online]. Available: http://dawn.cs.stanford.edu/benchmark/index.html
[46] J. Hermans, “On Scalable Deep Learning and Parallelizing Gradient Descent,” Aug.
2017, syntethic version: http://joerihermans.com/ramblings/distributed-deep-learning-part-
1-an-introduction/ Code https://github.com/cerndb/dist-keras. [Online]. Available:
http:
//cds.cern.ch/record/2276711
[47] I. Mitliagkas, C. Zhang, S. Hadjis, and C. Ré, “Asynchrony begets Momentum, with an
Application to Deep Learning,” CoRR, vol. abs/1605.09774, 2016. [Online]. Available:
http://arxiv.org/abs/1605.09774
[48] X. Lian, W. Zhang, C. Zhang, and J. Liu, “Asynchronous Decentralized Parallel Stochastic
Gradient Descent,” ArXiv e-prints, vol. 1710, p. arXiv:1710.06952, Oct. 2017. [Online].
Available: http://adsabs.harvard.edu/abs/2017arXiv171006952L
[49] B. Polyak and A. Juditsky, “Acceleration of Stochastic Approximation by Averaging,” SIAM
Journal on Control and Optimization, vol. 30, no. 4, pp. 838–855, Jul. 1992. [Online].
Available: https://epubs.siam.org/doi/abs/10.1137/0330046
[50] S. Zhang, A. Choromanska, and Y. LeCun, “Deep Learning with Elastic Averaging SGD,” in
Proceedings of the 28th International Conference on Neural Information Processing Systems -
Volume 1, ser. NIPS’15.
Cambridge, MA, USA: MIT Press, 2015, pp. 685–693. [Online].
Available: http://dl.acm.org/citation.cfm?id=2969239.2969316
[51] D. Povey, X. Zhang, and S. Khudanpur, “Parallel training of Deep Neural Networks with
Natural Gradient and Parameter Averaging,” CoRR, vol. abs/1410.7455, 2014. [Online].
Available: http://arxiv.org/abs/1410.7455
[52] S. Lee, S. Purushwalkam, M. Cogswell, D. J. Crandall, and D. Batra, “Why M Heads are Better
than One: Training a Diverse Ensemble of Deep Networks,” CoRR, vol. abs/1511.06314, 2015.
[Online]. Available: https://arxiv.org/abs/1511.06314
[53] G. E. Hinton, O. Vinyals, and J. Dean, “Distilling the Knowledge in a Neural Network,” CoRR,
vol. abs/1503.02531, 2015. [Online]. Available: http://arxiv.org/abs/1503.02531
11


## Page 12


[54] Y. Lin, S. Han, H. Mao, Y. Wang, and W. J. Dally, “Deep Gradient Compression: Reducing
the Communication Bandwidth for Distributed Training,” CoRR, vol. abs/1712.01887, 2017.
[Online]. Available: https://arxiv.org/abs/1712.01887
[55] F. Seide, H. Fu, J. Droppo, G. Li, and D. Yu, “1-Bit Stochastic Gradient Descent and
Application to Data-Parallel Distributed Training of Speech DNNs,” Microsoft Research,
Sep. 2014. [Online]. Available:
https://www.microsoft.com/en-us/research/publication/
1-bit-stochastic-gradient-descent-and-application-to-data-parallel-distributed-training-of-speech-dnns/
[56] D.
Yu,
A.
Eversole
et
al.,
“An
Introduction
to
Computational
Net-
works
and
the
Computational
Network
Toolkit,”
Microsoft
Research,
Aug.
2014.
[Online].
Available:
https://www.microsoft.com/en-us/research/publication/
an-introduction-to-computational-networks-and-the-computational-network-toolkit/
[57] N. Vasilache, O. Zinenko et al., “Tensor Comprehensions: Framework-Agnostic High-
Performance Machine Learning Abstractions,” CoRR, vol. abs/1802.04730, 2018. [Online].
Available: http://arxiv.org/abs/1802.04730
[58] S. Markidis, S. W. D. Chien, E. Laure, I. B. Peng, and J. S. Vetter, “NVIDIA Tensor Core
Programmability, Performance & Precision,” CoRR, vol. abs/1803.04014, 2018. [Online].
Available: https://arxiv.org/abs/1803.04014
[59] S. S. Ram, A. Nedic, and V. V. Veeravalli, “Asynchronous gossip algorithms for stochastic
optimization,” in 2009 International Conference on Game Theory for Networks, May 2009, pp.
80–81.
[60] T. Hoeﬂer, A. Barak, A. Shiloh, and Z. Drezner, “Corrected Gossip Algorithms for Fast
Reliable Broadcast on Unreliable Systems,” in 2017 IEEE International Parallel and Distributed
Processing Symposium (IPDPS), May 2017, pp. 357–366.
[61] M. Drocco, “Parallel Programming with Global Asynchronous Memory: Models, C++ APIs
and Implementations,” Ph.D. dissertation, Computer Science Department, University of Torino,
Oct. 2017. [Online]. Available: https://zenodo.org/record/1037585/ﬁles/Drocco_phd_thesis.pdf
12

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]