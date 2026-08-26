---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1701.05157v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1701.05157v2_Integrated_information_and_dimensionality_in_continuous_attractor_dynamics

> Source: 1701.05157v2_Integrated_information_and_dimensionality_in_continuous_attractor_dynamics.pdf

> Pages: 13

---


## Page 1


1 
 
Integrated information and dimensionality in continuous attractor dynamics 
Satohiro Tajima1,2,*, Ryota Kanai3 
1. University of Geneva, Geneva, Switzerland. 
2. JST PRESTO, Saitama, Japan. 
3. Araya Brain Imaging, Tokyo, Japan. 
*satohiro.tajima@gmail.com 
Abstract 
There has been increasing interest in the integrated information theory (IIT) of consciousness, which 
hypothesizes that consciousness is integrated information within neuronal dynamics. However, the current 
formulation of IIT poses both practical and theoretical problems when we aim to empirically test the theory by 
computing integrated information from neuronal signals. For example, measuring integrated information 
requires observing all the elements in the considered system at the same time, but this is practically rather 
difficult. In addition, the interpretation of the spatial partition needed to compute integrated information 
becomes vague in continuous time-series variables due to a general property of nonlinear dynamical systems 
known as “embedding.” Here, we propose that some aspects of such problems are resolved by considering the 
topological dimensionality of shared attractor dynamics as an indicator of integrated information in 
continuous attractor dynamics. In this formulation, the effects of unobserved nodes on the attractor dynamics 
can be reconstructed using a technique called delay embedding, which allows us to identify the dimensionality 
of an embedded attractor from partial observations. We propose that the topological dimensionality represents 
a critical property of integrated information, as it is invariant to general coordinate transformations. We 
illustrate this new framework with simple examples and discuss how it fits together with recent findings based 
on neural recordings from awake and anesthetized animals. This topological approach extends the existing 
notions of IIT to continuous dynamical systems and offers a much-needed framework for testing the theory 
with experimental data by substantially relaxing the conditions required for evaluating integrated information 
in real neural systems.


## Page 2


2 
 
Introduction 
There has been increasing interest in the integrated information theory (IIT) of consciousness. The central 
hypothesis of IIT is that consciousness is integrated information within collective neuronal dynamics [1–5]. 
An attractive aspect of IIT is that it could relate basic properties of subjective experiences in consciousness to 
the physical mechanisms of biological (and even artificial) dynamical systems via the information theoretic 
framework [5]. Among the theories of consciousness, IIT is relatively new and still awaits empirical 
verification. To examine IIT with empirical neural recordings, however, its current implementation needs to 
address several issues from both practical and theoretical viewpoints. Although empirical studies have 
reported neural phenomena for which IIT could provide consistent explanations [6–10], it is still challenging 
to test the necessity of IIT directly with empirical datasets under its current formulation. For example, 
measuring integrated information in a rigorous sense requires observing all the elements at the same time, 
which imposes a serious bottleneck in testing the theory with neural recordings in living organisms. 
Moreover, as we discuss later in this paper, the interpretation of spatial partitioning becomes unclear when we 
regard a time sequence of continuous variables as a unit of “state” due to the local observability known as 
“embedding” [11,12] in general continuous dynamical systems.  
Here, we discuss an alternative implementation of IIT that could resolve some aspects of those problems. A 
key idea in our formulation is to index the integrated information in terms of the topological dimensionality of 
shared attractor dynamics. In this formulation, the effects of unobserved nodes on the attractor dynamics 
could be reconstructed using a technique called delay embedding. Remarkably, considering topological 
properties allows us to make use of, rather than suffer from, the puzzling effects of embedding in continuous 
dynamical systems. We illustrate how this formulation works with simple examples and discuss its relevance 
to the original formulation of IIT and our recent empirical findings from awake and anesthetized animals [13].  
The aim of the present perspective article is to illustrate the basic idea behind our formulation. For this 
purpose, we focus on intuitive rather than rigorous mathematical descriptions. 
Topological dimensionality as an indicator of integrated information in continuous 
dynamical systems 
To illustrate our formulation, let us consider simple dynamical systems consisting of only two nodes, with 
values of 𝑥1 and 𝑥2 (Figure 1). Suppose that each of 𝑥1 and 𝑥2 has self-feedback, which is generally 
nonlinear. For the sake of simplicity, here we assume that each node’s value is defined in one-dimensional 
continuous space (e.g., 𝑥1, 𝑥2 ∈ℝ), but the subsequent arguments are valid for general cases in which each 
node value is defined in higher-dimensional spaces.  
First, let us begin by considering a mutually interacting system (Figure 1a-i). We assume the system 
dynamics to be described with deterministic difference equations as (similar arguments apply to the cases with 
ordinary differential equations) 
𝑥1
𝑡= 𝑓(𝑥1
𝑡−1, 𝑥2
𝑡−1),  
 
 
 
 
 
(1) 
𝑥2
𝑡= 𝑔(𝑥1
𝑡−1, 𝑥2
𝑡−1),  
 
 
 
 
 
(2) 
where 𝑓 and 𝑔 are arbitrary continuous functions and 𝑡 denotes an arbitrary time point. In a general nonlinear 
system, the state (𝑥1
𝑡, 𝑥2
𝑡) could be distributed across an at most 2-dimensional manifold 𝐴 (the light gray


## Page 3


3 
 
 
Figure 1 
Schematic illustrations for the dimensionality-based index of integrated information. 
(a) A system with mutually interacting nodes. 
(b) A system comprising two disconnected nodes. 
(c) A partial observation of the system with mutually interacting nodes (the same system as in panel a). 
Insets: i) The schematic of the systems; ii) The inferred past states at time 𝑡−1; iii) The inferred past state at time 𝑡−
1, based on a partitioned observation; iv) The current states.


## Page 4


4 
 
square in the figure) in the phase space of (𝑥1, 𝑥2). For convenience, we call 𝐴 an “attractor” when the state 
stays within 𝐴 for a sufficiently long time. After a sufficient duration away from the initial state, attractor 𝐴 
provides a support of the joint probability density distribution 𝑝(𝑥1, 𝑥2). 
Suppose that we could identify both nodes’ values (𝑥1
𝑡, 𝑥2
𝑡) at time 𝑡 by observing them simultaneously (i.e., 
we could make the joint probability density distribution 𝑝(𝑥1
𝑡, 𝑥2
𝑡) be a delta function through the observation). 
If we consider the past state of those nodes, (𝑥1
𝑡−1, 𝑥2
𝑡−1), based on this observation, the uncertainty in the 
inference is described by the conditional distribution  𝑝(𝑥1
𝑡−1, 𝑥2
𝑡−1|𝑥1
𝑡, 𝑥2
𝑡). In a general nonlinear 
deterministic system, 𝑝(𝑥1
𝑡−1, 𝑥2
𝑡−1|𝑥1
𝑡, 𝑥2
𝑡) is supported by a finite number of points in attractor 𝐴, except for 
some special cases (such as that either function 𝑓 or 𝑔 is flat). To rephrase, identifying the system’s current 
state (𝑥1
𝑡, 𝑥2
𝑡) constrains its past state (𝑥1
𝑡−1, 𝑥2
𝑡−1) on a set of zero-dimensional manifolds (i.e., points). Figure 
1a-ii depicts a simple case in which the previous state is perfectly identified as a single point. 
What if we did not use the joint observation of two nodes’ values, 𝑝(𝑥1
𝑡, 𝑥2
𝑡) but rather inferred the past values 
of individual nodes separately based on marginal observations, 𝑝(𝑥1
𝑡) and 𝑝(𝑥2
𝑡)? Because we assumed no 
uncertainty in observing each node’s current value, 𝑝(𝑥1
𝑡, 𝑥2
𝑡), 𝑝(𝑥1
𝑡) and 𝑝(𝑥2
𝑡) are all delta functions, and we 
thus have 𝑝(𝑥1
𝑡, 𝑥2
𝑡) = 𝑝(𝑥1
𝑡)𝑝(𝑥2
𝑡). What about the inferred past state, 𝑝(𝑥1
𝑡−1, 𝑥2
𝑡−1|𝑥1
𝑡, 𝑥2
𝑡)? In fact, such an 
equality does not hold between the past state distributions, 𝑝(𝑥1
𝑡−1, 𝑥2
𝑡−1|𝑥1
𝑡, 𝑥2
𝑡) and 𝑝(𝑥1
𝑡−1|𝑥1
𝑡)𝑝(𝑥2
𝑡−1|𝑥2
𝑡). 
Indeed, the previous state generally cannot be identified by the marginal observation when the nodes interact 
with each other. Namely, 𝑝(𝑥𝑖
𝑡−1|𝑥𝑖
𝑡) is not described by a delta function of 𝑥𝑖
𝑡−1 (𝑖= 1,2), even if 𝑝(𝑥𝑖
𝑡) is a 
delta function, and thus generally 
𝑝(𝑥1
𝑡−1, 𝑥2
𝑡−1|𝑥1
𝑡, 𝑥2
𝑡) ≠𝑝(𝑥1
𝑡−1|𝑥1
𝑡)𝑝(𝑥2
𝑡−1|𝑥2
𝑡).   
 
 
 
(3) 
This fact could be understood intuitively as follows: for example, the set of states that fall in the support of the 
marginal distribution 𝑝(𝑥1
𝑡) is represented by the vertical red line in Figure 1a-iv, reflecting the uncertainty 
about the current value of 𝑥2
𝑡. This set is generally mapped to an oblique line (or a curve) in the previous time 
point (the red curve in Figure 1a-iii) due to the interaction between 𝑥1 and 𝑥2. Because we do not know 
where the actual past state was on this curve, we have 1-dimensional uncertainty in the past state of 𝑥1 when 
we consider the projection of this curve onto the 𝑥1-axis (as indicated by the non-zero length of the red bar on 
the horizontal axis in Figure 1a-ii, iii). The same argument applies to 𝑥2, and thus we have another 1-
dimensional uncertainty, now for 𝑥2, as shown by the blue bar on the vertical axis. Together, we have a 2-
dimensional uncertainty in the past state inferred from the separate (“partitioned”) observations 
𝑝(𝑥1
𝑡−1|𝑥1
𝑡)𝑝(𝑥2
𝑡−1|𝑥2
𝑡) in total (as depicted by the dark gray rectangle in Figure 1a-iii). Now, recalling that 
the inference based on a joint observation, 𝑝(𝑥1
𝑡−1, 𝑥2
𝑡−1|𝑥1
𝑡, 𝑥2
𝑡), had 0-dimensional uncertainty, we can 
understand that 𝑝(𝑥1
𝑡−1|𝑥1
𝑡)𝑝(𝑥2
𝑡−1|𝑥2
𝑡) generally differs from 𝑝(𝑥1
𝑡−1, 𝑥2
𝑡−1|𝑥1
𝑡, 𝑥2
𝑡). 
This inequality between the joint and partitioned conditional probability distributions is the key for 
characterizing the integrated information value (𝜑) in IIT [1,2,4,14,15]. (Note that basically the same 
argument applies to the relationships between the current and future states.) How to quantify the difference 
between the joint and partitioned distributions is arbitrary. Roughly speaking, IIT 2.0 used the Kullback-
Leibler divergence [2,15] and IIT 3.0 the earth mover’s distance (EMD) [4] to quantify the differences 
between the joint and partitioned probability distributions. Other information theoretic indices are proposed 
for practical applications [15–17].


## Page 5


5 
 
Here, we propose an alternative way of quantifying the difference in distributions based on the topological 
dimensionality of uncertainty rather than precise information-theoretic quantities. The idea is simple: for 
example, in the case we described above, 𝑝(𝑥1
𝑡−1, 𝑥2
𝑡−1|𝑥1
𝑡, 𝑥2
𝑡) is supported by a 0-dimensional manifold (i.e., 
point(s)), whereas 𝑝(𝑥1
𝑡−1|𝑥1
𝑡)𝑝(𝑥2
𝑡−1|𝑥2
𝑡) was supported by a 2-dimensional manifold (i.e., rectangle). Then, 
we say “the difference between those two distributions is 2 (= 2 – 0)”. Formally, if we denote the 
dimensionality of the support of a distribution 𝑝 by Dim[𝑝], the integrated information in terms of the 
topological dimensionality (𝜑Dim) can be written as follows: 
𝜑Dim ≡Dim[𝑝(𝑥1
𝑡−1|𝑥1
𝑡)𝑝(𝑥2
𝑡−1|𝑥2
𝑡)] −Dim[𝑝(𝑥1
𝑡−1, 𝑥2
𝑡−1|𝑥1
𝑡, 𝑥2
𝑡)].  
 
 
(4) 
In this example,  
𝜑Dim = 2.  
 
 
 
 
 
(5) 
Throughout this paper, we consider cases in which attractors have integer dimensions, and thus 𝜑Dim takes 
integer values, although we can extend the framework to indexes taking real values by considering non-
integer dimensionality such as fractal dimensions [18,19]. Note that, in contrast to the typical frameworks for 
IIT, the current dimensionality-based argument works in continuous dynamical systems.  
Dimensionality suggests no integration in a mechanistically disconnected system 
For a sanity check, let us now consider how the dimensionality-based quantification of the integrated 
information works in a physically/mechanistically separated system, as shown in Figure 1b-i. This system has 
self-feedback on each node but no interaction between the nodes:  
𝑥1
𝑡= 𝑓(𝑥1
𝑡−1),   
 
 
 
 
(6) 
𝑥2
𝑡= 𝑔(𝑥2
𝑡−1).   
 
 
 
 
(7) 
Although this system could form an apparently 2-dimensional attractor when we plot the trajectory of 
(𝑥1
𝑡, 𝑥2
𝑡), it is a product of two smaller dynamical systems. How does this fact affect our index of integrated 
information 𝜑Dim? As before, if we could identify the current state by observing the entire system (𝑥1
𝑡, 𝑥2
𝑡), 
the possible past state (𝑥1
𝑡−1, 𝑥2
𝑡−1) can be constrained to a finite number of points (again, except for some 
special cases). Then, let us say Dim[𝑝(𝑥1
𝑡−1, 𝑥2
𝑡−1|𝑥1
𝑡, 𝑥2
𝑡)] = 0. How about the partitioned observation, 
𝑝(𝑥1
𝑡−1|𝑥1
𝑡)𝑝(𝑥2
𝑡−1|𝑥2
𝑡)? Because there is no interaction between the nodes, each of 𝑥1 and 𝑥2 forms an 
autonomous dynamics by itself. This means that observing 𝑥1 alone provides sufficient information to 
constrain the past state to be on 0-dimensional manifold(s), and so does the observation of 𝑥2 alone. Namely, 
the uncertainty in the partitioned observation 𝑝(𝑥1
𝑡−1|𝑥1
𝑡)𝑝(𝑥2
𝑡−1|𝑥2
𝑡) is still 0-dimensional, and thus the 
partition does not increase the dimensionality of the uncertainty. This fact is intuitively represented by the red 
vertical and blue horizontal lines in Figure 1b-ii (notice the difference from the case in which there are 
interactions between the nodes; Figure 1a-ii). Therefore, in this system, Dim[𝑝(𝑥1
𝑡−1|𝑥1
𝑡)𝑝(𝑥2
𝑡−1|𝑥2
𝑡)] = 0, 
from which we have 
𝜑Dim = 0.  
 
 
 
 
 
(8) 
This is the desired result. The above example demonstrates that the dimensionality-based index of integrated 
information, 𝜑Dim, correctly captures the “absence of integration” in a disconnected system, just like in the 
original formulation of IIT.


## Page 6


6 
 
Dimensionality suggests integration in an attractor reconstructed from partial 
observation  
We have seen that the dimensionality-based index of integrated information seems to yield reasonable results 
for simple examples. However, what are the advantages of considering the dimensionality instead of the 
precise information quantity? To see this, we now turn to considering a case in which we do not observe the 
entire system but can access only part of it—say, 𝑥1 alone (Figure 1c). As in the first example, let us assume 
mutual interaction between the two nodes. In contrast to the previous cases, however, now we assume that we 
never have access to 𝑥2. 
Usually, there is no means of measuring the integrated information between 𝑥1 and 𝑥2 when we cannot 
observe 𝑥2’s state. However, because 𝑥1 and 𝑥2 are interacting, 𝑥2’s information could be implicitly coded by 
the temporal evolution of 𝑥1. If so, we might be able to reconstruct some aspects of the dynamics in the entire 
system from the observation of its subset. This is indeed the case in nonlinear, deterministic dynamical 
systems in general—known as the mathematical property called “delay embedding” [11,12]. Delay-
embedding theorems claim that, in short, the temporal pattern of a single variable has a smooth one-to-one 
mapping to the state of the entire system that the observed variable belongs to. In general, if we have an 
autonomous dynamical system comprising N variables (𝑥1, … , 𝑥𝑁) that interact with each other, the trajectory 
of (𝑥1
𝑡, … , 𝑥𝑁
𝑡) forms an attractor in this N-dimensional space. Let us say we can only observe the time series 
of 𝑥1
𝑡. According to the delay-embedding theorems, we can reconstruct the attractor’s topology (a shape 
defined based on connectivity) by plotting the trajectory of (𝑥1
𝑡, 𝑥1
𝑡−𝜏, … , 𝑥1
𝑡−(𝑑−1)𝜏) instead of (𝑥1
𝑡, … , 𝑥𝑁
𝑡) 
when 𝑑 is sufficiently large, where 𝜏 is called the unit delay and 𝑑 is called the embedding dimension. It is 
known that if 𝑑 is larger than the original attracter’s dimensionality, the attractor can be reconstructed almost 
anywhere on itself with an ignorable volume of overlaps with itself [12]. It might be somewhat surprising that 
the property of global dynamics could be reconstructed (in a topological sense) solely from the local 
observation, although it is proven to be the case in almost any type of nonlinear, deterministic dynamical 
system (and the fact that we can extract the information about the unobserved nodes via embedding may lead 
to an issue on the definition of “state” in a time series and the meaning of spatial partitioning, as we will 
reconsider later). 
Dimensionality is an aspect of such topological properties reconstructed through the delay embedding. Thus, 
it is tempting to expect that the present dimensionality-based index of integrated information could be inferred 
(at least to some extent) from the partial observation. This is indeed possible, although we need a bit of 
tweaking, as shown below. Now, let us see how this idea works in our simple example (Figure 1c). 
Because we can only observe 𝑥1, we consider a 2-dimensional delay coordinates (𝑥1
𝑡, 𝑥1
𝑡−𝜏) instead of the 
original 2-dimensional state space (𝑥1
𝑡, 𝑥2
𝑡). The unit delay 𝜏 could be chosen arbitrarily. Let 𝐴1 denote the 
reconstructed attractor. Precisely, these 2-dimensinal coordinates are generally not sufficient for embedding 
when the original attractor 𝐴’s dimensionality is 2, as the reconstructed attractor 𝐴1 includes overlaps with 
itself. Nonetheless, because the original attractor is 2-dimensional, identifying a 2-dimensional state 
(𝑥1
𝑡, 𝑥1
𝑡−𝜏) in these delay coordinates can constrain the original state (𝑥1
𝑡, 𝑥2
𝑡) within a finite set of points (0-
dimensional manifold), as long as the number of self-overlaps is finite (which seems to be the case except in 
pathological situations). This means that we can also infer the past state in the delay coordinates, 
(𝑥1
𝑡−1, 𝑥1
𝑡−𝜏−1), with 0-dimensional uncertainty.


## Page 7


7 
 
As the reader may notice, this situation is quite similar to the case in which we could observe the entire 
system (Figure 1a). Then, what happens if we consider the partitioned observation, just as before? Now, we 
cannot consider the spatial partition (because we observe only a single node!). Instead, let us introduce a new 
partition: a “temporal partition.” That is, we consider the partition between temporally distant observations 𝑥1
𝑡 
and 𝑥1
𝑡−𝜏. Applying the same arguments to this temporal partition reveals that observing either of 𝑥1
𝑡 and 𝑥1
𝑡−𝜏 
alone leads to 1-dimensional uncertainty about the past states 𝑥1
𝑡−1 and  𝑥1
𝑡−𝜏−1, respectively, and thus the net 
dimensionality of the uncertainty is 2 (Figure 1c). Therefore, the dimensionality-based index of the integrated 
information in the delay coordinates turns out to be 
𝜑1
Dim = 2.  
 
 
 
 
 
(9) 
Again, the result matches that of the case in which we could observe the entire system (Figure 1a). This fact 
is interesting because it means that we could reach the same result based on two distinct data: one from the 
complete observation of the entire system and the other from the partial observation of its subset. In particular, 
both results match the dimensionality of the attractor in the mutually interacting system we considered here. 
One may suspect that it is only a coincidence, but in fact, the dimensionality of the reconstructed attractor 
generally gives an upper bound of 𝜑Dim in the original space. Indeed, when we have a general 𝑑𝐴-dimensional 
attractor formed by 𝑁 mutually interacting nodes (𝑥1, … , 𝑥𝑁), the attractor can be reconstructed within 𝑑𝐴-
dimensional delay coordinates of node 𝑥𝑖,  (𝑥𝑖
𝑡, … , 𝑥𝑖
𝑡−(𝑑𝐴−1)𝜏), allowing 𝑑𝐴-dimensional self-overlaps. As 
long as the number of self-overlaps is finite, the same argument applies, resulting in 0-dimensiosnal 
uncertainty in inferring the past state with the joint observation. A temporal (bi-)partition, 
{(𝑥𝑖
𝑡, … , 𝑥𝑖
𝑡−𝑘+1), (𝑥𝑖
𝑡−𝑘, … , 𝑥𝑖
𝑡−(𝑑𝐴−1)𝜏)} (∀𝑘∈ℕ), leads to 𝑑𝐴−𝑘 and 𝑘-dimensional uncertainties for the 
individual partitioned observations, and thus the net uncertainty turns out to be 𝑑𝐴-dimensional. Together, 
𝜑𝑖
Dim = 𝑑𝐴. On the other hand, 𝜑Dim in the original system is upper-bounded by the attractor dimensions, 𝑑𝐴. 
When 𝑑𝐴< 𝑁, 𝜑Dim could be smaller than 𝑑𝐴. Interestingly, an appropriate projection of the original 𝑁-
dimensional space to a 𝑑𝐴-dimensional space (e.g., by clustering the nodes and averaging the node values 
within each cluster) can recover its upper bound, 𝜑Dim = 𝑑𝐴—which is analogous to the fact that integrated 
information could be maximized by appropriate coarse-graining [20–22]. 
Dimensionality suggests the “exclusion” of upstream nodes in an asymmetric 
interaction 
The previous examples show that 𝜑Dim in a mutually interacting system reflects the dimensionality of the 
attractor (whether the observation is about the whole or partial system), whereas 𝜑Dim = 0 in a disconnected 
system. Note that the apparent dimensionalities of the attractors were both 2 in those examples (Figures 1a 
and 1b). In this regard, we can interpret 𝜑Dim as an index of “interaction-relevant dimensionality” rather than 
the apparent dimensionality within the original phase space. 
The dimensionality-based characterization becomes even less trivial when we consider a system having a 
hierarchy in terms of the directionality of interactions. To see this, let us consider an example in which the 
nodes do not mutually interact but rather have a directed interaction (Figure 2a–c). Now, the node 𝑥2 affects, 
but is not affected by, node 𝑥1, which can be formally written as


## Page 8


8 
 
 
 
Figure 2 
Heterogeneity of dimensionality-based index of integrated information under a directed interaction. 
(a) The index derived based on the observation of the entire system. 
(b) The index derived based on the observation of the downstream node. 
(c) The index derived based on the observation of the upstream node. 
The inset conventions follow those of Figure 1.


## Page 9


9 
 
𝑥1
𝑡= 𝑓(𝑥1
𝑡−1, 𝑥2
𝑡−1),  
 
 
 
 
 
(10) 
𝑥2
𝑡= 𝑔(𝑥2
𝑡−1).   
 
 
 
 
 
(11) 
We can define 𝑥1 as the “downstream” and 𝑥2 as the “upstream” in the system. Note that the upstream node 
𝑥2 forms an autonomous dynamical system by itself, whereas the downstream node 𝑥1 belongs to the 
dynamical system formed by both 𝑥1 and 𝑥2. As we did before, we assume that the system has an apparently 
2-dimensional attractor in the phase space of (𝑥1, 𝑥2). 
Let us first consider the simultaneous observation of the entire system (Figure 2a). Applying the same 
analysis as before to this system, we find that identifying the system’s current state (𝑥1
𝑡, 𝑥2
𝑡) constrains its past 
state (𝑥1
𝑡−1, 𝑥2
𝑡−1) on a set of zero-dimensional manifolds. On the other hand, in the partitioned observations, 
identifying the upstream node 𝑥2
𝑡 constrains its own past state 𝑥2
𝑡−1 with 0-dimensinal uncertainty, as it forms 
a single-node dynamics by itself, whereas identifying the downstream node 𝑥1
𝑡 leaves a 1-dimensional 
uncertainty about its past state 𝑥1
𝑡−1, reflecting the unknown effect from the upstream. Together, the net 
uncertainty in the partitioned observation is 1-dimensional, and thus the index of integrated information in the 
system is 
𝜑Dim = 1.  
 
 
 
 
 
 
(12) 
Notably, this value of 𝜑Dim under the directed interaction is smaller than that under the mutual interaction 
(Figure 1a), which is qualitatively consistent with the result of the original IIT [2,4]. 
What if the observation is partial? There are two possibilities of partial observations: observing only the 
downstream node 𝑥1 (Figure 2b) or observing only the upstream node 𝑥2 (Figure 2c). First, when we observe 
the downstream alone, we can plot the state trajectory in the delay coordinates (𝑥1
𝑡, 𝑥1
𝑡−𝜏) to reconstruct the 
topology of the attractor being realized in the entire system (𝑥1, 𝑥2), which has 2 dimensions in this case 
(Figure 2b). This situation is the same as that in Figure 1c, and considering the same temporal partition 
reveals that the index of integrated information based on this reconstructed attractor is 
𝜑1
Dim = 2.  
 
 
 
 
 
 
(13) 
On the other hand, when we plot a similar trajectory in the 2-dimensional delay coordinates with the upstream 
(𝑥2
𝑡, 𝑥2
𝑡−𝜏), we can reconstruct only a 1-dimensional manifold (Figure 2c). Again, it is because the upstream 
node 𝑥2 receives no effect from its downstream, forming a smaller autonomous dynamical system. Because 
the reconstructed attractor is 1-dimensional, the temporal partition in this 2-dimensional delay coordinates 
does not increase the uncertainty, resulting in 
𝜑2
Dim = 0.  
 
 
 
 
 
 
(14) 
To summarize the results presented above, in this system with a directed interaction, 
𝜑1
Dim > 𝜑Dim > 𝜑2
Dim.   
 
 
 
 
(15) 
These inequalities illustrate that our dimensionality-based index of integrated information is maximized when 
it is quantified within the downstream node dynamics, not within the entire system. The integrated 
information maximized at the downstream agrees, again, with the results of the original formulation of IIT [4]. 
In particular, the higher integration in a subset of the system rather than the whole demonstrates the axiomatic


## Page 10


10 
 
property of “exclusion” assumed in IIT: namely, the physical substrate of conscious experience has unique 
borders (e.g., the contents of conscious experience can exclude the phenomenal distinction of feeling one’s 
blood pressure as being high or low) [3–5]. In the present framework, it is natural to interpret the system’s 
subset 𝑖 that maximizes 𝜑𝑖
Dim as an analogue of ‘complex’ in IIT, which determines the borders of subjective 
experiences. 
Discussion 
Relevance to the cross-embedding complexity 
We have seen that our dimensionality-based index of integrated information reflects the dimensions of 
attractors being realized in dynamical systems in a way sensitive to how the nodes in the systems interact with 
each other. For example, the value of 𝜑Dim could differentiate a mutual interaction (Figure 1a), a directed 
interaction (Figure 2a), and no interaction (Figure 1b). An alternative way to quantify the interaction-
relevant dimensionality (complexity) of the attractor dynamics is “cross-embedding,” which measures the 
embedding dimensions necessary for inferring a node’s value from the temporal pattern of another node’s 
value [13]. Interestingly, analogous to the present dimensionality-based measure of integrated information in 
the interacting and disconnected systems (Figures 3a and 3b), the cross-embedding indexes higher 
dimensionality for the downstream nodes than the upstream nodes, both in artificial systems and in the actual 
brain dynamics in conscious animals, and such strong heterogeneity was not observed in unconscious animals 
(Figures 3c and 3d) [13]. Indeed, the cross-embedding and the dimensionality-based integrated information 
share the basic idea that the high-dimensional attractor dynamics realized through interactions are relevant for 
 
Figure 3 
Comparison of the dimensionality-based index of integrated information and the interaction-relevant attractor 
dimensionality (“complexity”) revealed by cross-embedding in conscious and unconscious animals. 
(a) The system with a directed interaction between nodes (the same as in Figure 2a–c). 
(b) The system with no interaction (the same as in Figure 1b).  
(c, d) Summary figures modified from Ref. [13]. (c) The distribution of the attractor complexity revealed by a cross-
embedding analysis in awake (conscious) macaque monkeys. (d) The distribution of the attractor complexity revealed 
by a cross-embedding analysis in anesthetized (unconscious) macaque monkeys.


## Page 11


11 
 
consciousness. Moreover, similar to the cross-embedding [13], the present index of integrated information 
demonstrates that information about other nodes can be reconstructed from local dynamics through the delay-
embedding technique. This non-localized nature of integrated information can be taken as a form of 
information ‘broadcasting’ among nodes, which the Global Neuronal Workspace Theory associates with 
consciousness [23]. Future studies will investigate more detailed relationships between the cross-embedding 
and the dimensionality-based integrated information with theoretical analysis and neural recordings. 
Spatial partitions and coordinate transformations 
To assess the dimensionality of dynamics with partial observations, we introduced the idea of “temporal 
partitioning” in the attractor reconstructed within delay coordinates, based on the delay-embedding theorems. 
This is a key contribution of this study that could bridge IIT’s framework to empirical data, in which we often 
have access to only partial observations of the studied system. At the same time, the delay embedding and 
temporal partitioning may invite a new question about the meaning of the spatial partitions considered in the 
original formulations of IIT: because we can extract information about unobserved variables through delay 
embedding by regarding the temporal pattern in a subset of the system as a “state,” the conclusion derived 
from the spatial partition could be affected severely by the definition of state within each node. Although it 
was already partially addressed in a previous study how the spatiotemporal coarse-graining affects the 
effective information [20], it is yet to be elucidated how the information leveraging by the delay embedding 
changes the net integrated information. The present dimensionality-based indexing of integrated information 
allows us to make use of, rather than suffer from, the effects of embedding in continuous dynamical systems. 
Moreover, the dimensionality-based assessment could be robust to changes in the definition of states because 
the topological dimensionality is in many cases invariant to coordinate transformations. Note that this 
invariance is gained in exchange for a more detailed characterization of the information-theoretic quantity; the 
topological dimensionality is a much coarser measure than the usual measures of integrated information due 
to the topological invariance, but our point here is that such invariance could allow us to index a form of 
integrated information even with a partial observation of a system and to bridge that index to the original 
notions of integrated information. 
Limitations 
Although we believe that the present topology-based approach will provide insights to IIT from practical and 
theoretical viewpoints, there is still room for elaboration. A major limitation of the current framework is that it 
assumes that we can estimate the exact dimensionality of the attractors, which can be challenging in real data. 
To implement the computation described here requires an efficient algorithm for estimating the underlying the 
attractor dimensionality, but we expect that it should be possible by extending a dimensionality estimation 
algorithm similar to the one used in the cross-embedding method [13]. Another caveat of the current 
embedding-based argument is that mathematically rigorous claims can be applied only to continuous, 
deterministic systems. Although empirical studies with artificial and real data have shown that delay 
embedding works even in dynamical systems including some stochasticity [13,24–26], future theoretical 
studies are required for more thorough verifications of the method. Note also that in realistic situations 
including stochastic dynamics, some information could be lost in the communications among nodes due to 
noise or other constraints on signal transmissions (e.g., narrow-band temporal frequency responses) that make 
the downstream information degenerate. In such cases, the attractor dimensions are not always maximized at 
the system’s downstream as in the examples we discussed—which agrees with our intuition that the 
maximally integrated information should be observed in the central nervous system, rather than its peripheral 
downstream (e.g., muscles).


## Page 12


12 
 
Lastly, although the present study focused on the attractor dimensions and relating them to the integrated 
information quantity as a substrate for the level of consciousness, it remains to be investigated how we can 
characterize the quality (or contents) of consciousness within this topological framework. A potentially useful 
approach to characterizing the quality of consciousness is to look at more detailed structures of the attractors, 
such as the number of holes in each dimension or the higher-order relationships among multiple attractors 
reconstructed from the individual nodes’ dynamics. 
Conclusion 
Currently, the value of IIT is still a subject of debate, attracting both enthusiasm and criticism [27]. An 
important next step would be to test the fundamental concepts of IIT empirically. For practical and theoretical 
reasons, however, it has been difficult to perform a rigorous computation of integrated information from real 
neuronal data. Our present study offers one practical measure of integrated information from real neural data 
in which the observations are partial and the variables are continuous. Specifically, we have shown that in 
continuous attractor dynamics, the topological dimensionality of a reconstructed attractor can be used to index 
the degree of integrated information. We believe that this captures a critical aspect of integrated information 
as it is invariant to general coordinate transformations. This topological dimensionality-based characterization 
is not only consistent with the existing framework of IIT, but it also significantly relaxes the conditions 
required for evaluating the integrated information. As such, the topological dimensionality enables us to 
assess the integrated information even from partial observations and provides a much-needed framework for 
testing the theory with experimental data. 
References 
1.  Tononi G. An information integration theory of consciousness. BMC Neurosci. 2004;5: 42:1-22. 
doi:10.1186/1471-2202-5-42 
2.  Balduzzi D, Tononi G. Integrated information in discrete dynamical systems: motivation and theoretical 
framework. PLOS Comput Biol. 2008;4: e1000091. doi:10.1371/journal.pcbi.1000091 
3.  Tononi G. Consciousness as integrated information: a provisional manifesto. Biol Bull. 2008;215: 216–42.  
4.  Oizumi M, Albantakis L, Tononi G. From the Phenomenology to the Mechanisms of Consciousness: 
Integrated Information Theory 3.0. PLOS Comput Biol. 2014;10: e1003588:1-25. 
doi:10.1371/journal.pcbi.1003588 
5.  Tononi G, Boly M, Massimini M, Koch C. Integrated Information Theory: from consciousness to its physical 
substrates. Nat Rev Neurosci. Nature Publishing Group; 2016;17: 450–461. doi:10.1038/nrn.2016.44 
6.  Massimini M, Ferrarelli F, Huber R, Esser SK, Singh H, Tononi G. Breakdown of cortical effective 
connectivity during sleep. Science (80- ). 2005;309: 2228–32. doi:10.1126/science.1117256 
7.  Massimini M, Ferrarelli F, Esser SK, Riedner B a, Huber R, Murphy M, et al. Triggering sleep slow waves by 
transcranial magnetic stimulation. Proc Natl Acad Sci U S A. 2007;104: 8496–501. 
doi:10.1073/pnas.0702495104 
8.  Lee U, Mashour GA, Kim S, Noh GJ, Choi B. Propofol induction reduces the capacity for neural information: 
Implications for the mechanism of consciousness and general anesthesia. Conscious Cogn. 2009;18: 56–64. 
doi:10.1016/j.concog.2008.10.005 
9.  Casali AG, Gosseries O, Rosanova M, Boly M, Sarasso S, Casali KR, et al. A Theoretically Based Index of 
Consciousness Independent of Sensory Processing and Behavior. Sci Transl Med. 2013;5: 198ra105-198ra105. 
doi:10.1126/scitranslmed.3006294 
10.  Sasai S, Boly M, Mensen A, Tononi G. Functional split brain in a driving/listening paradigm. Proc Natl Acad 
Sci. 2016; 201613200. doi:10.1073/pnas.1613200113 
11.  Takens F. Detecting strange attractors in fluid turbulence. In: Rand DA, Young L-S, editors. Dynamical


## Page 13


13 
 
Systems and Turbulence, Lecture Notes in Mathematics. Berlin: Springer-Verlag; 1981. pp. 366–381.  
12.  Sauer T, Yorke JA, Casdagli M. Embedology. J Stat Phys. 1991;65: 579–616. doi:10.1007/BF01053745 
13.  Tajima S, Yanagawa T, Fujii N, Toyoizumi T. Untangling brain-wide dynamics in consciousness by cross-
embedding. PLOS Comput Biol. 2015;11: e1004537. doi:10.1371/journal.pcbi.1004537 
14.  Oizumi M, Tsuchiya N, Amari S. A unified framework for information integration based on information 
geometry. Proc Natl Acad Sci U S A. 2016; 1–6. doi:10.1088/0143-0807/36/6/065030 
15.  Oizumi M, Amari SI, Yanagawa T, Fujii N, Tsuchiya N. Measuring Integrated Information from the Decoding 
Perspective. PLoS Comput Biol. 2016;12. doi:10.1371/journal.pcbi.1004654 
16.  Barrett AB, Seth AK. Practical measures of integrated information for time-series data. PLOS Comput Biol. 
2011;7: e1001052. doi:10.1371/journal.pcbi.1001052 
17.  Tegmark M. Improved Measures of Integrated Information. PLoS Comput Biol. 2016;12: 1–34. 
doi:10.1371/journal.pcbi.1005123 
18.  Mandelbrot BB. Fractals—Form, Chance and Dimension. Freeman, San Francisco; 1977.  
19.  Grassberger P, Procaccia I. Characterization of strange attractors. Phys Rev Lett. 1983;50: 346–349. 
doi:10.1103/PhysRevLett.50.346 
20.  Hoel EP, Albantakis L, Tononi G. Quantifying causal emergence shows that macro can beat micro. Proc Natl 
Acad Sci. 2013;110: 19790–19795. doi:10.1073/pnas.1314922110 
21.  Hoel EP, Albantakis L, Marshall W, Tononi G. Can the macro beat the micro? Integrated information across 
spatiotemporal scales. Neurosci Conscious. 2016;1: 1–13. doi:10.1093/nc/niw012 
22.  Hoel EP. When the map is better than the territory. arXiv. 2016;1612.09592 [cs.IT].  
23.  Dehaene S, Changeux J-P. Experimental and theoretical approaches to conscious processing. Neuron. 2011;70: 
200–27. doi:10.1016/j.neuron.2011.03.018 
24.  Sugihara G, May R. Nonlinear forecasting as a way of distinguishing chaos from measurement error in time 
series. Nature. 1990;344: 734–741.  
25.  Sugihara G, May R, Ye H, Hsieh C, Deyle E, Fogarty M, et al. Detecting causality in complex ecosystems. 
Science (80- ). 2012;338: 496–500. doi:10.1126/science.1227079 
26.  Ye H, Sugihara G. Information leverage in interconnected ecosystems: Overcoming the curse of 
dimensionality. Science (80- ). 2016;353: 922–925.  
27.  Cerullo MA. The Problem with Phi: A Critique of Integrated Information Theory. PLoS Comput Biol. 
2015;11: 1–12. doi:10.1371/journal.pcbi.1004286

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]