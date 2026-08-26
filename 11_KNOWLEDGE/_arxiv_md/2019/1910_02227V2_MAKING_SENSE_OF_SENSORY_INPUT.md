---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.02227v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1910.02227v2_Making_sense_of_sensory_input

> Source: 1910.02227v2_Making_sense_of_sensory_input.pdf

> Pages: 64

---


## Page 1


Making sense of sensory input
Richard Evansa,b,∗, Jos´e Hern´andez-Oralloc,d, Johannes Welbla, Pushmeet Kohlia, Marek Sergotb
aDeepMind, London
bImperial College London
cUniversitat Polit`ecnica de Val`encia
dCFI, University of Cambridge
Abstract
This paper attempts to answer a central question in unsupervised learning: what does it mean to “make sense”
of a sensory sequence? In our formalization, making sense involves constructing a symbolic causal theory that
both explains the sensory sequence and also satisﬁes a set of unity conditions. The unity conditions insist that the
constituents of the causal theory – objects, properties, and laws – must be integrated into a coherent whole. On our
account, making sense of sensory input is a type of program synthesis, but it is unsupervised program synthesis.
Our second contribution is a computer implementation, the Apperception Engine, that was designed to satisfy the
above requirements. Our system is able to produce interpretable human-readable causal theories from very small
amounts of data, because of the strong inductive bias provided by the unity conditions. A causal theory produced
by our system is able to predict future sensor readings, as well as retrodict earlier readings, and impute (ﬁll in the
blanks of) missing sensory readings, in any combination. In fact, it is able to do all three tasks simultaneously.
We tested the engine in a diverse variety of domains, including cellular automata, rhythms and simple nursery
tunes, multi-modal binding problems, occlusion tasks, and sequence induction intelligence tests. In each domain,
we test our engine’s ability to predict future sensor values, retrodict earlier sensor values, and impute missing
sensory data. The Apperception Engine performs well in all these domains, signiﬁcantly out-performing neural net
baselines. We note in particular that in the sequence induction intelligence tests, our system achieved human-level
performance. This is notable because our system is not a bespoke system designed speciﬁcally to solve intelligence
tests, but a general-purpose system that was designed to make sense of any sensory sequence.
1. Introduction
Imagine a machine, equipped with various sensors, that receives a stream of sensory information.
It must,
somehow, make sense of this stream of sensory data. But what does it mean, exactly, to “make sense” of sensory
data? We have an intuitive understanding of what is involved in making sense of the sensory stream – but can we
specify precisely what is involved? Can this intuitive notion be formalized?
∗Corresponding author
Email address: richardevans@google.com (Richard Evans)
Preprint submitted to Artiﬁcial Intelligence
July 15, 2020
arXiv:1910.02227v2  [cs.AI]  14 Jul 2020


## Page 2


One approach is to treat the sensory sequence as the input to a supervised learning problem1: given a sequence x1:t
of sensory data from time steps 1 to t, maximize the probability of the next datum xt+1. This family of approaches
seeks to maximize p(xt+1 | x1:t). More generally, as well as training the system to predict future sensor readings,
we may also train it to retrodict past sensor readings (maximizing p(x1 | x2:t)), and to impute missing intermediate
values (maximizing p(xi | x1:i−1, xi+1:t)).
We believe there is more to “making sense” than prediction, retrodiction, and imputation. Predicting the future
state of one’s photoreceptors may be part of what is involved in making sense – but it is not on its own suﬃcient.
The ability to predict, retrodict, and impute is a sign, a surface manifestation, that one has made sense of the input.
We want to deﬁne the underlying mental model that is constructed when one makes sense of the sensory input,
and to show how constructing this mental model ipso facto enables one to predict, retrodict, and impute.
In this paper, we assume that making sense of sensory input involves constructing a symbolic theory that explains
the sensory input [9, 10, 11, 12]. A number of authors, including Lake [16] and Marcus [15], have argued that
constructing an explanatory theory is a key component of common sense. Following Spelke and others [13, 14],
we assume the theory must posit objects that persist over time, with properties that change over time according
to general laws. Further, we assume, following John McCarthy and others [17, 18, 19], that making sense of the
surface sensory perturbations requires positing latent objects: some sensory sequences can only be made intelligible
by hypothesizing an underlying reality, distinct from the surface features of our sensors, that makes the surface
phenomena intelligible. The underlying reality consists of latent objects that causally interact with our sensors to
product the sensory perturbations we are given as input. Once we have constructed such a theory, we can apply
it to predict future sensor readings, to retrodict past readings, or to impute missing values.
Now constructing a symbolic theory that explains the sensory sequence is necessary for making sense of the
sequence.
But it is not, we claim, suﬃcient.
There is one further additional ingredient that we add to our
characterisation of “making sense”. This is the requirement that our theory exhibits a particular form of unity: the
constituents of our theory – objects, properties, and atoms – must be integrated into a coherent whole. Speciﬁcally,
our unity condition requires that the objects are interrelated via chains of binary relations, the properties are
connected via exclusion relations, and the atoms are uniﬁed by jointly satisfying the theory’s constraints. This
extra unity condition is necessary, we argue, for the theory to achieve good accuracy at prediction, retrodiction,
and imputation. 2
This paper makes two main contributions. The ﬁrst is a formalization of what it means to “make sense” of the
stream of sensory data. According to our deﬁnition, making sense of a sensory sequence involves positing a
symbolic causal theory – a set of objects, a set of concepts, a set of initial conditions, a set of rules, and a set of
constraints – that together satisfy two conditions. First, the theory must explain the sensory readings it is given.
Second, the theory must satisfy a particular type of unity. Our deﬁnition of unity involves four conditions. (i)
Spatial unity: all objects must be uniﬁed in space via a chain of binary relations. (ii) Conceptual unity: all concepts
1See, for example, [1, 2, 3, 4, 5]. See also the Predictive Processing paradigm: [6, 7, 8].
2We show, in the ablation experiments of Section 5, that without these unity conditions, our computer implementation is much less accurate
at prediction, retrodiction, and imputation.
2


## Page 3


must be uniﬁed via constraints. (iii) Static unity: all propositions that are true at the same time must jointly satisfy
the set of constraints. (iv) Temporal unity: all the states must be uniﬁed into a sequence by causal rules.
Our second contribution is a description of a particular computer system, the Apperception Engine3, that was
designed to satisfy the conditions described above4. We introduce a causal language, Datalog⊃−, that was designed
for reasoning about inﬁnite temporal sequences. Given a sensory sequence, our system synthesizes a Datalog⊃−
program that, when executed, generates a trace that both explains the sensory sequence and also satisﬁes the four
conditions of unity. This can be seen as a form of unsupervised program synthesis [22]. In traditional supervised
program synthesis, we are given input/output pairs, and search for a program that, when executed on the inputs,
produces the desired outputs. Here, in unsupervised program synthesis, we are given a sensory sequence, and
search for a causal theory that, when executed, generates a trajectory that both respects the sensory sequence and
also satisﬁes the conditions of unity.
The Apperception Engine has a number of appealing features. (1) Because the causal theories it generates are
symbolic, they are human-readable and hence veriﬁable. We can understand precisely how the system is making
sense of its sensory data5. (2) Because of the strong inductive bias (both in terms of the design of the causal
language, Datalog⊃−, but also in terms of the unity conditions that must be satisﬁed), the system is data-eﬃcient,
able to make sense of the shortest and scantiest of sensory sequences6. (3) Our system generates a causal model
that is able to accurately predict future sensory input. But that is not all it can do; it is also able to retrodict previous
values and impute missing sensory values in the middle of the sensory stream. In fact, our system is able to
predict, retrodict, and impute simultaneously7. (4) The Apperception Engine has been tested in a diverse variety
of domains, with encouraging results. The ﬁve domains we use are elementary cellular automata, rhythms and
nursery tunes, “Seek Whence” and C-test sequence induction intelligence tests [24], multi-modal binding tasks,
and occlusion problems. These tasks were chosen because they require cognition rather than mere classiﬁcatory
perception, and because they are simple for humans but not for modern machine learning systems, e.g. neural
networks8. The Apperception Engine performs well in all these domains, signiﬁcantly out-performing neural net
baselines. These results are signiﬁcant because neural systems typically struggle to solve the binding problem
(where information from diﬀerent modalities must somehow be combined into diﬀerent aspects of one uniﬁed
object) and fail to solve occlusion tasks (in which objects are sometimes visible and sometimes obscured from
view).
We note in particular that in the sequence induction intelligence tests, our system achieved human-level perfor-
mance. This is notable because the Apperception Engine was not designed to solve these induction tasks; it is not
3“Apperception” comes from the French ‘apercevoir’. The term is introduced by Leibniz in the New Essays Concerning Human Understanding
[20].Apperception, as we use it in this paper, is the process of assimilating sensory information into a coherent uniﬁed whole. See Dewey:
“Apperception is the relating activity which combines the various sensuous elements presented to the mind at one time into a whole, and which
unites these wholes, recurring at successive times, into a continuous mental life, thereby making psychical life intelligent” [21].
4Our code and datasets are publicly available at https://github.com/RichardEvans/apperception.
5Human readability is a much touted feature of Inductive Logic Programming (ILP) systems, but when the learned programs become large
and include a number of invented auxiliary predicates, the resulting programs become less readable (see [23]). But even a large and complex
machine-generated logic program will be easier to understand than a large tensor of ﬂoating point numbers.
6Our sensory sequences are less than 300 bits. See Table 4.
7See Example 3 for a case where the Apperception Engine jointly predicts, retrodicts, and imputes.
8Figure 7 shows how neural baselines struggle to solve these tasks.
3


## Page 4


a bespoke hand-engineered solution to this particular domain. Rather, it is a general-purpose9 system that attempts
to make sense of any sensory sequence. This is, we believe, a highly suggestive result [25].
In ablation tests, we tested what happened when each of the four unity conditions was turned oﬀ. Since the
system’s performance deteriorates noticeably when each unity condition is ablated, this indicates that the unity
conditions are indeed doing vital work in our engine’s attempts to make sense of the incoming barrage of sensory
data.
1.1. Related work
A human being who has built a mental model of the world can use that model for counterfactual reasoning,
anticipation, and planning [26, 27, 28].
Similarly, computer agents endowed with mental models are able to
achieve impressive performance in a variety of domains. For instance, Lukasz Kaiser et al. [29] show that a model-
based RL agent trained on 100K interactions compares with a state-of-the-art model-free agent trained on tens or
hundreds of millions of interactions. David Silver et al. [30] have shown that a model-based Monte Carlo tree
search planner with policy distillation can achieve superhuman level performance in a number of board games.
The tree search relies, crucially, on an accurate model of the game dynamics.
When we have an accurate model of the environment, we can leverage that model to anticipate and plan. But in
many domains, we do not have an accurate model. If we want to apply model-based methods in these domains, we
must learn a model from the stream of observations. In the rest of this section, we shall describe various diﬀerent
approaches to representing and learning models, and show where our particular approach ﬁts into the landscape
of model learning systems.
Before we start to build a model to explain a sensory sequence, one fundamental question is: what form should the
model take? We shall distinguish three dimensions of variation of models (adapted from [31]): ﬁrst, whether they
simply model the observed phenomena, or whether they also model latent structure; second, whether the model
is explicit and symbolic or implicit; and third, what type of prior knowledge is built into the model structure.
We shall use the hidden Markov model (HMM)10 [32, 33] as a general framework for describing sequential processes.
Here, the observation at time t is xt, and the latent state is zt. In a HMM, the observation xt at time t depends only
on the latent (unobserved) state zt. The state zt in turn depends only on the previous latent state zt−1.
The ﬁrst dimension of variation amongst models is whether they actually use latent state information zt to explain
the observation xt. Some approaches [34, 35, 36, 37, 38, 39] assume we are given the underlying state information
z1:t. In these approaches, there is no distinction between the observed phenomena and the latent state: xi = zi. With
this simplifying assumption, the only thing a model needs to learn is the transition function. Other approaches
9Although the algorithm is general-purpose (the exact same code is applied to many diﬀerent domains), domain-speciﬁc knowledge can be
injected as needed. For example, in the sequence induction tasks (Section 5.1.4), the successor relation on letters is provided to the system. But
this information is arguably part of the problem formulation, rather than part of the solution.
10Many systems predict state dynamics for partially observable Markov decision processes (POMDPs), rather than HMMs. In a POMDP, the
state transition function depends on the previous state zt and the action at performed by an agent. See Jessica Hamrick’s paper for an excellent
overview [31] of model-based methods in deep learning that is framed in terms of POMDPs. In this paper, we consider HMMs. Adding actions
to our model is not particularly diﬃcult, but is left for further work.
4


## Page 5


[40, 2, 41] focus only on the observed phenomena x1:t and ignore latent information z1:t altogether. These approaches
predict observation xt+1 given observation xt without positing any hidden latent structure. Some approaches take
latent information seriously [42, 43, 44, 5, 45]. These jointly learn a perception function (that produces a latent zt
from an observed xt), a transition function (producing a next latent state zt+1 from latent state zt) and a rendering
function (producing a predicted observation xt+1 from the latent state zt+1). Our approach also builds a latent
representation of the state. As well as positing latent properties (unobserved properties that explain observed
phenomena), we also posit latent objects (unobserved objects whose relations to observed objects explain observed
phenomena).
The second dimension of variation concerns whether the learned model is explicit, symbolic and human-readable,
or implicit and inscrutable. In some approaches [42, 43, 44, 5], the latent states are represented by vectors and the
dynamics of the model by weight tensors. In these cases, it is hard to understand what the system has learned.
In other approaches [46, 47, 48, 49], the latent state is represented symbolically, but the state transition function
is represented by the weight tensor of a neural network and is inscrutable. We may have some understanding
of what state the machine thinks it is in, but we do not understand why it thinks there is a transition from this
state to that. In some approaches [11, 12, 50, 51, 52, 53], both the latent state and the state transition function
are represented symbolically. Here, the latent state is a set of ground atoms11 and the state transition function is
represented by a set of universally quantiﬁed rules. Our approach falls into this third category. Here, the model is
fully interpretable: we can interpret the state the machine thinks it is in, and we can understand the reason why it
believes it will transition to the next state.
A third dimension of variation between models is the amount and type of prior knowledge that they include. Some
model learning systems have very little prior knowledge. In some of the neural systems (e.g. [2]), the only prior
knowledge is the spatial invariance assumption implicit in the convolutional network’s structure. Other models
incorporate prior knowledge about the way objects and states should be represented. For example, some models
assume objects can be composed in hierarchical structures [47]. Other systems additionally incorporate prior
knowledge about the type of rules that are used to deﬁne the state transition function. For example, some [51, 52, 53]
use prior knowledge of the event calculus [54]. Our approach falls into this third category. We impose a language
bias in the form of rules used to deﬁne the state transition function and also impose additional requirements on
candidate sets of rules: they must satisfy the four unity conditions introduced above (and elaborated in Section 3.3
below).
To summarize, in order to position our approach within the landscape of other approaches, we have distinguished
three dimensions of variation. Our approach diﬀers from neural approaches in that the posited theory is explicit
and human readable. Not only is the representation of state explicit (represented as a set of ground atoms) but
the transition dynamics of the system are also explicit (represented as universally quantiﬁed rules in a domain
speciﬁc language designed for describing causal structures). Our approach diﬀers from other inductive program
synthesis methods in that it posits signiﬁcant latent structure in addition to the induced rules to explain the
11A ground atom is a logical atom that contains no variables.
5


## Page 6


observed phenomena: in our approach, explaining a sensory sequence does not just mean constructing a set of
rules that explain the transitions; it also involves positing a type signature containing a set of latent properties
and a set of latent objects. Our approach also diﬀers from other inductive program synthesis methods in the type
of prior knowledge that is used: as well as providing a strong language bias by using a particular representation
language (a typed extension of datalog with causal rules and constraints), we also inject a substantial inductive
bias: the unity conditions, the key constraints on our system, represent domain-independent prior knowledge. Our
approach also diﬀers from other inductive program synthesis methods in being entirely unsupervised. In contrast,
OSLA and OLED [51, 52] are supervised, and SPLICE [53] is semi-supervised. See Section 7 for detailed discussion.
1.2. Paper outline
Section 2 introduces basic notation. Section 3 presents the main deﬁnition of what it means for a theory to count
as a uniﬁed interpretation of a sensory sequence. Section 4 describes a computer system that is able to generate
uniﬁed interpretations of sensory sequences. Section 5 describes our experiments in ﬁve diﬀerent types of task:
elementary cellular automata, rhythms and nursery tunes, “Seek Whence” sequence induction tasks, multi-modal
binding tasks, and occlusion problems. In Section 6, we show how our system is extended to robustly handle
noise. Related work is discussed in Section 7.
2. Background
In this paper, we use basic concepts and standard notation from logic programming [55, 56, 57]. A function-free
atom is an expression of the form p(t1, ..., tn), where p is a predicate of arity n ≥0 and each ti is either a variable or
a constant. We shall use a, b, c, ... for constants, X, Y, Z, ... for variables, and p, q, r, ... for predicate symbols.
A substitution σ is a mapping from variables to terms. For example σ = {X/a, Y/b} replaces variable X with
constant a and replaces variable Y with constant b. We write ασ for the application of substitution σ to atom α, so
e.g. p(X, Y)σ = p(a, b).
A Datalog clause is a deﬁnite clause of the form α1 ∧... ∧αn →α0 where each αi is an atom and n ≥0. It is
traditional to write clauses from right to left: α0 ←α1, ..., αn. In this paper, we will deﬁne a Datalog interpreter
implemented in another logic programming language, ASP (answer-set programming). In order to keep the two
languages distinct, we write Datalog rules from left to right and ASP clauses from right to left. A Datalog program
is a set of Datalog clauses.
A key result of logic programming is that every Datalog program has a unique subset-minimal least Herbrand
model that can be directly computed by repeatedly generating the consequences of the ground instances of the
clauses [58].
We turn now from Datalog to normal logic programs under the answer set semantics [59]. A literal is an atom α
or a negated atom not α. A normal logic program is a set of clauses of the form:
α0 ←α1, ..., αn
6


## Page 7


where α0 is an atom, α1, ..., αn is a conjunction of literals, and n ≥0. Normal logic clauses extend Datalog clauses
by allowing functions in terms and by allowing negation by failure in the body of the rule.
Answer Set Programming (ASP) is a logic programming language based on normal logic programs under the
answer set semantics. Given a normal logic program, an ASP solver ﬁnds the set of answer sets for that program.
Modern ASP solvers can also be used to solve optimization problems by the introduction of weak constraints [60].
A weak constraint is a rule that deﬁnes the cost of a certain tuple of atoms. Given a program with weak constraints,
an ASP solver can ﬁnd a preferred answer set with the lowest cost.
3. A computational framework for making sense of sensory sequences
What does it mean to make sense of a sensory sequence? In this section, we formalize what this means, before
describing our computer implementation. We assume that the sensor readings have already been discretized into
ground atoms of ﬁrst-order logic, so a sensory reading featuring sensor a can be represented by a ground atom p(a)
for some unary predicate p, or by an atom r(a, b) for some binary relation r and unique value b.12
Deﬁnition 1. An unambiguous symbolic sensory sequence is a sequence of sets of ground atoms. Given a sequence
S = (S1, S2, ...), every state St in S is a set of ground atoms, representing a partial description of the world at a discrete time
step t. An atom p(a) ∈St represents that sensor a has property p at time t. An atom r(a, b) ∈St represents that sensor a is
related via relation r to value b at time t. If G is the set of all ground atoms, then S ∈

2G∗.
Example 1. Consider, the following sequence S1:10. Here there are two sensors a and b, and each sensor can be
either on or oﬀ.
S1 = {}
S2 = {oﬀ(a), on(b)}
S3 = {on(a), oﬀ(b)}
S4 = {on(a), on(b)}
S5 = {on(b)}
S6 = {on(a), oﬀ(b)}
S7 = {on(a), on(b)}
S8 = {oﬀ(a), on(b)}
S9 = {on(a)}
S10 = {}
There is no expectation that a sensory sequence contains readings for all sensors at all time steps. Some of the
readings may be missing. In state S5, we are missing a reading for a, while in state S9, we are missing a reading for
b. In states S1 and S10, we are missing sensor readings for both a and b.
◁
The central idea is to make sense of a sensory sequence by constructing a uniﬁed theory that explains that sequence.
The key notions, here, are “theory”, “explains”, and “uniﬁed”. We consider each in turn.
3.1. The theory
Theories are deﬁned in a new language, Datalog⊃−, designed for modelling dynamics. In this language, one can
describe how facts change over time by writing a causal rule stating that if the antecedent holds at the current
12We restrict our attention to unary and binary predicates. This restriction can be made without loss of generality, since every k-ary relationship
can be expressed as k + 1 binary relationships [61].
7


## Page 8


time-step, then the consequent holds at the next time-step. Additionally, our language includes a frame axiom
allowing facts to persist over time: each atom remains true at the next time-step unless it is overridden by a new
fact which is incompatible with it. Two facts are incompatible if there is a constraint that precludes them from both
being true. Thus, Datalog⊃−extends Datalog with causal rules and constraints.
Deﬁnition 2. A theory is a four-tuple (φ, I, R, C) of Datalog⊃−elements where:
• φ is a type signature specifying the types of constants, variables, and arguments of predicates
• I is a set of initial conditions
• R is a set of rules describing the dynamics
• C is a set of constraints
We shall consider each element in turn, starting with the type signature.
Deﬁnition 3. Given a set T of types, a set O of constants representing individual objects, and a set P of predicates representing
properties and relations, let G be the set of all ground atoms formed from T , O, and P. Given a set V of variables, let U be
the set of all unground atoms formed from T , V, and P.
A type signature is a tuple (T, O, P, V) where T ⊆T is a ﬁnite set of types, O ⊆O is a ﬁnite set of constants representing
objects, P ⊆P is a ﬁnite set of predicates representing properties and relations, and V ⊆V is a ﬁnite set of variables. We
write κO : O →T for the type of an object, κP : P →T∗for the types of the predicate’s arguments, and κV : V →T for the
type of a variable.
Now some type signatures are suitable for some sensory sequences, while others are unsuitable, because they do
not contain the right constants and predicates. The following deﬁnition formalizes this:
Deﬁnition 4. Let GS = S
t≥1 St be the set of all ground atoms that appear in sensory sequence S = (S1, ...). Let Gφ be the
set of all ground atoms that are well-typed according to type signature φ. If φ = (T, O, P, V) then Gφ = {p(a1, ..., an) | p ∈
P, κP(p) = (t1, ..., tn), ai ∈O, κO(ai) = ti for all i = 1..n}. A type signature φ is suitable for a sensory sequence S if all the
atoms in S are well-typed according to signature φ, i.e. GS ⊆Gφ.
Next, we deﬁne the set of unground atoms for a particular type signature.
8


## Page 9


Deﬁnition 5. Let Uφ be the set of all unground atoms that are well-typed according to signature φ. If φ = (T, O, P, V) then
Uφ = {p(v1, ..., vn) | p ∈P, κP(p) = (t1, ..., tn), vi ∈V, κV(vi) = ti for all i = 1..n}. Note that, according to this deﬁnition, an
atom is unground if all its terms are variables. Note that “unground” means more than simply not ground. For example,
p(a, X) is neither ground nor unground.
Example 2. One suitable type signature for the sequence of Example 1 is (T, O, P, V), consisting of types T = {s},
objects O = {a:s, b:s}, predicates P = {on(s), oﬀ(s)}, and variables V = {X:s, Y:s}. Here, and throughout, we write a:s
to mean that object a is of type s, on(s) to mean that unary predicate on takes one argument of type s, and X:s to
mean that variable X is of type s. The unground atoms are Uφ = {on(X), oﬀ(X), on(Y), oﬀ(Y)}. There are, of course,
an inﬁnite number of other suitable signatures.
◁
Deﬁnition 6. The initial conditions I of a theory (φ, I, R, C) is a set of ground atoms from Gφ representing a partial
description of the facts true at the initial time step.
The initial conditions are needed to specify the initial values of the latent unobserved information. Some systems
(e.g. LFIT [12]) deﬁne a predictive model without using a set I of initial conditions. These systems are able to
avoid positing initial conditions because they do not use latent unobserved information. But any system that does
invoke latent information beneath the surface of the sensory stimulations must also deﬁne the initial values of the
latent information.
The rules deﬁne the dynamics of the theory:
Deﬁnition 7. There are two types of rule in Datalog⊃−. A static rule is a deﬁnite clause of the form α1 ∧... ∧αn →α0,
where n ≥0 and each αi is an unground atom from Uφ consisting of a predicate and a list of variables. Informally, a static
rule is interpreted as: if conditions α1, ...αn hold at the current time step, then α0 also holds at that time step. A causal rule
is a clause of the form α1 ∧... ∧αn ⊃−α0, where n ≥0 and each αi is an unground atom from Uφ. A causal rule expresses how
facts change over time. Rule α1 ∧... ∧αn ⊃−α0 states that if conditions α1, ...αn hold at the current time step, then α0 holds at
the next time step.
All variables in rules are implicitly universally quantiﬁed. So, for example, on(X) ⊃−oﬀ(X) states that for all objects
X, if X is currently on, then X will become oﬀat the next-time step.
The constraints rule out certain combinations of atoms13:
13Note that exclusive disjunction between atoms p1(X), ..., pn(X) is diﬀerent from xor between the n atoms. The xor of n atoms is true if an odd
number of the atoms hold, while the exclusive disjunction is true if exactly one of the atoms holds. We write p1(X) ⊕... ⊕pn(X) to mean exclusive
disjunction between n atoms, not the application of n −1 xor operations.
9


## Page 10


Deﬁnition 8. There are three types of constraint in Datalog⊃−. A unary constraint is an expression of the form ∀X, p1(X) ⊕
...⊕pn(X), where n > 1, meaning that for all X, exactly one of p1(X), ..., pn(X) holds. A binary constraint is an expression of
the form ∀X, ∀Y, r1(X, Y) ⊕... ⊕rn(X, Y) where n > 1, meaning that for all objects X and Y, exactly one of the binary relations
hold. A uniqueness constraint is an expression of the form ∀X, ∃!Y:t2, r(X, Y), which means that for all objects X of type
t1 there exists a unique object Y such that r(X, Y).
Note that the rules and constraints are constructed entirely from unground atoms. Disallowing constants prevents
special-case rules that apply to particular objects, and forces the theory to be general.14
3.2. Explaining the sensory sequence
A theory explains a sensory sequence if the theory generates a trace15 that covers that sequence. In this section, we
explain the trace and the covering relation.
Deﬁnition 9. Every theory θ = (φ, I, R, C) generates an inﬁnite sequence τ(θ) of sets of ground atoms, called the trace of
that theory. Here, τ(θ) = (A1, A2, ...), where each At is the smallest set of atoms satisfying the following conditions:
• I ⊆A1
• If there is a static rule β1 ∧... ∧βm →α in R and a ground substitution σ such that At satisﬁes βiσ for each antecedent
βi, then ασ ∈At
• If there is a causal rule β1 ∧...∧βm ⊃−α in R and a ground substitution σ such that At−1 satisﬁes βiσ for each antecedent
βi, then ασ ∈At
• Frame axiom: if α is in At−1 and there is no atom in At that is incompossible with α w.r.t constraints C, then α ∈At.
Two ground atoms are incompossible if there is some constraint c in C and some substitution σ such that the ground
constraint cσ precludes both atoms being true.
The frame axiom is a simple way of providing inertia: a proposition continues to remain true until something new
comes along which is incompatible with it. Including the frame axiom makes our theories much more concise:
instead of needing rules to specify all the atoms which remain the same, we only need rules that specify the atoms
that change.
Note that the state transition function is deterministic: At is uniquely determined by At−1.
14This restriction also occurs in some ILP systems [12, 62].
15In [12], the trace is called the orbit.
10


## Page 11


Theorem 1. The trace of every theory repeats after some ﬁnite number of steps. For any theory θ, there exists a k such that
τ(θ) = (A1, ..., Ak−1, Ak, Ak+1, ...) and for all i ≥0, Ai = Ak+i.
Proof. Since the set Gφ of ground atoms is ﬁnite, there must be a k such that A1 = Ak. The proof proceeds by
induction on i. If i = 0, the proof is trivial. When i > 0, note that the trace function τ satisﬁes the Markov condition
that the next state At+1 depends only on the current state At, and not on any earlier states. Hence if Ai = Ai+k, then
Ai+1 = Ai+k+1.
□
One important consequence of Theorem 1 is:
Theorem 2. Given a theory θ and a ground atom α, it is decidable whether α appears somewhere in the inﬁnite trace τ(θ).
Proof. Let τ(θ) be the inﬁnite sequence (A1, A2, ...). From Theorem 1, the trace must repeat after k time steps. Thus,
to check whether ground atom α appears somewhere in τ(θ), it suﬃces to test if α appears in A1, ..., Ak.
□
Next we deﬁne what it means for a theory to “explain” a sensory sequence.
Deﬁnition 10. Given ﬁnite sequence S = (S1, ..., ST) and (not necessarily ﬁnite) S′, S ⊑S′ if S′ = (S′
1, S′
2, ...) and Si ⊆S′
i for
all 1 ≤i ≤T. If S ⊑S′, we say that S is covered by S′, or that S′ covers S. A theory θ explains a sensory sequence S if the
trace of θ covers S, i.e. S ⊑τ(θ).
In providing a theory θ that explains a sensory sequence S, we make S intelligible by placing it within a bigger
picture: while S is a scanty and incomplete description of a fragment of the time-series, τ(θ) is a complete and
determinate description of the whole time-series.
Example 3. We shall provide a theory to explain the sensory sequence S of Example 1.
Consider the type signature φ = (T, O, P, V), consisting of types T = {s}, objects O = {a:s, b:s}, predicates P =
{on(s), oﬀ(s), p1(s), p2(s), p3(s), r(s, s)}, and variables V = {X:s, Y:s}. Here, φ extends the type signature of Example 2
by adding three unary predicates p1, p2, p3, and one binary relation r.16
Consider the theory θ = (φ, I, R, C), where:
I =

p1(b)
p2(a)
r(a, b)
r(b, a)

R =

p1(X) ⊃−p2(X)
p2(X) ⊃−p3(X)
p3(X) ⊃−p1(X)
p1(X) →on(X)
p2(X) →on(X)
p3(X) →oﬀ(X)

C =

∀X:s, on(X) ⊕oﬀ(X)
∀X:s, p1(X) ⊕p2(X) ⊕p3(X)
∀X:s, ∃!Y:s r(X, Y)

16Extended type signatures are generated by the machine, not by hand. Our computer implementation searches through the space of
increasingly complex type signatures extending the original signature. This search process is described in Section 4.1.
11


## Page 12


The inﬁnite trace τ(θ) = (A1, A2, ...) for theory θ begins with:
A1 = {on(a), on(b), p2(a), p1(b), r(a, b), r(b, a)}
A2 = {oﬀ(a), on(b), p3(a), p2(b), r(a, b), r(b, a)}
A3 = {on(a), oﬀ(b), p1(a), p3(b), r(a, b), r(b, a)}
A4 = {on(a), on(b), p2(a), p1(b), r(a, b), r(b, a)}
. . .
Note that the trace repeats at step 4. In fact, it is always true that the trace repeats after some ﬁnite set of time steps.
Theory θ explains the sensory sequence S of Example 1, since the trace τ(θ) covers S. Note that τ(θ) “ﬁlls in the
blanks” in the original sequence S, both predicting ﬁnal time step 10, retrodicting initial time step 1, and imputing
missing values for time steps 5 and 9.
◁
3.3. Unifying the sensory sequence
Next, we proceed from explaining a sensory sequence to “making sense” of that sequence. In order for θ to make
sense of S, it is necessary that τ(θ) covers S. But this condition is not, on its own, suﬃcient. The extra condition
that is needed for θ to count as “making sense” of S is for θ to be uniﬁed. We require that the constituents of the
theory are integrated into a coherent whole. A trace τ(θ) of theory θ is a (i) sequence of (ii) sets of ground atoms
composed of (iii) predicates and (iv) objects. For the theory θ to be uniﬁed is for unity to be achieved at each of
these four levels:
Deﬁnition 11. A theory θ is uniﬁed if each of the four conditions hold:
1. Objects are united in space (see Section 3.3.1)
2. Predicates are united via constraints (see Section 3.3.2)
3. Ground atoms are united into states by jointly respecting constraints and static rules (see Section 3.3.3)
4. States are united into a sequence by causal rules (see Section 3.3.4)
3.3.1. Spatial unity
Deﬁnition 12. A theory θ satisﬁes spatial unity if for each state At in τ(θ) = (A1, A2, ...), for each pair (x, y) of distinct
objects, x and y are connected via a chain of binary atoms {r1(x, z1), r2(z1, z2), ...rn(zn−1, zn), rn+1(zn, y)} ⊆At.
If this condition is satisﬁed, it means that given any object, we can get to any other object by hopping along
relations. Everything is connected, even if only indirectly.
12


## Page 13


Note that this notion of spatial unity is rather abstract: the requirement is only that every pair of objects are
indirectly connected via some chain of binary relations. Although some of these binary relations might be spatial
relations (e.g. “left-of”), they need not all be. The requirement is only that every pair of objects are connected via
some chain of binary relations; it does not insist that each binary relation has a speciﬁcally “spatial” interpretation.
3.3.2. Conceptual unity
A theory satisﬁes conceptual unity if every predicate is involved in some constraint, either exclusive disjunction
(⊕) or unique existence (∃!). The intuition here is that constraints combine predicates into clusters of mutual
incompatibility.
Deﬁnition 13. A theory θ = (φ, I, R, C) satisﬁes conceptual unity if for each unary predicate p in φ, there is some xor
constraint in C of the form ∀X:t, p(X) ⊕q(X) ⊕... containing p; and, for each binary predicate r in φ, there is some xor
constraint in C of the form ∀X:t1, ∀Y:t2, r(X, Y) ⊕s(X, Y) ⊕... or some ∃! constraint in C of the form ∀X:t, ∃!Y:t2, r(X, Y).
To see the importance of this, observe that if there are no constraints, then there are no exhaustiveness or exclu-
siveness relations between atoms. An xor constraint e.g. ∀X:t, on(X) ⊕oﬀ(X) both rules out the possibility that
an object is simultaneously on and oﬀ(exclusiveness) and also rules out the possibility that an object of type t is
neither on nor oﬀ(exhaustiveness). It is exhaustiveness which generates states that are determinate, in which it is
guaranteed every object of type t is e.g. either on or oﬀ. It is exclusiveness which generates incompossibility between
atoms, e.g. that on(a) and oﬀ(a) are incompossible. Incompossibility, in turn, is needed to constrain the scope of the
frame axiom (see Deﬁnition 9 above). Without incompossibility, all atoms from the previous time-step would be
transferred to the next time-step, and the set of true atoms in the sequence (S1, S2, ...) would grow monotonically
over time: Si ⊆Sj if i ≤j, which is clearly unacceptable. The purpose of the constraint of conceptual unity is to
collect predicates into groups, to provide determinacy in each state, and to ground the incompossibility relation
that constrains the way information persists between states.17
17A natural question to ask at this point is: why use exclusive disjunction to represent constraints? Why not instead represent constraints
using strong negation or negation as failure[63]? An exclusive disjunction can always be converted into a set of extended clauses representing
the predicates’ exclusiveness, and one normal clause representing their exhaustiveness. For example, ∀X : t, p(X) ⊕q(X) can be rendered as:
¬p(X) : - q(X)
¬q(X) : - p(X)
: - not p(X), not q(X), t(X)
In general, if we have an exclusive disjunction featuring n predicates, we can turn this into n ∗(n −1) clauses (using strong negation) to capture
the exclusiveness of the n predicates, and one clause (using negation as failure) to capture the exhaustiveness.
The exclusive disjunction constraint is a compact way of representing a lot of information about the connection between predicates. Although
the exclusive disjunction constraint can always be translated into a set of clauses (using both negation as failure and strong negation), the
representation using exclusive disjunction is much more compact.
One reason, then, for expressing the constraint as an exclusive disjunction is that it is a signiﬁcantly more compact representation than the
representation using negation as failure. But another, more substantial reason is that it means we can avoid the complexities involved in the
semantics if we added negation as failure to our target language Datalog⊃−. There are various semantics for normal logic programs that include
negation as failure (e.g. Clark completion [64], stable model semantics [59], well-founded models [65]), but each of them introduces signiﬁcant
additional complexities when compared with the least model of a deﬁnite logic program: the Clark completion is not always consistent (does
not always have a model), the stable model semantics assigns the meaning of a normal logic program to a set of models rather than a single
13


## Page 14


3.3.3. Static unity
In our eﬀort to interpret the sensory sequence, we construct various ground atoms. These need to be grouped
together, somehow, into states (sets of atoms). But what determines how these atoms are grouped together into
states?
Treating a set A of ground atoms as a state is (i) to insist that A satisﬁes all the constraints in C and (ii) to insist that
A is closed under the static rules in R:
Deﬁnition 14. A theory θ = (φ, I, R, C) satisﬁes static unity if every state (A1, A2, ...) in τ(θ) satisﬁes all the constraints
in C and is closed under the static rules in R.
Static unity is an uncontroversial requirement and is used in other ILP systems [66, 67]. Note that, from the
deﬁnition of the trace in Deﬁnition 9, all the states in τ(θ) are automatically closed under the static rules in R.
3.3.4. Temporal unity
Given a set of states, we need to unite these elements in a sequence. According to the fourth and ﬁnal condition of
unity, the only thing that can unite states in a sequence is a set of causal rules. These causal rules are universal in
two senses: they apply to all object tuples, and they apply at all times. A causal rule α1 ∧... ∧αn ⊃−α0 ﬁxes the
temporal relation between the atoms α1, ..., αn (which are true at t) and the atom α0 (which is true at t + 1):
Deﬁnition 15. A sequence (A1, A2, ...) of states satisﬁes temporal unity with respect to a set R⊃−of causal rules if, for each
α1 ∧... ∧αn ⊃−α0 in R⊃−, for each ground substitution σ, for each time-step t, if {α1σ, ..., αnσ} ⊆At then α0σ ∈At+1.
Temporal unity is an uncontroversial requirement and is also used in other ILP systems such as LFIT [12]. Note
that, from the deﬁnition of the trace in Deﬁnition 9, the trace τ(θ) automatically satisﬁes temporal unity.
3.3.5. The four conditions of unity
To recap, the trace of a theory is a sequence of sets of atoms. The four types of element are objects, predicates, sets
of atoms, and sequences of sets of atoms. Each of the four types of element has its own form of unity:
model, and the well-founded model uses a 3-valued logic where atoms can be true, false, or undeﬁned. Thus, the main reason for expressing
constraints using exclusive disjunction (rather than using negation as failure) is to restrict the rules to deﬁnite rules and avoid the complexities
of the various semantics of normal logic programs. (Although we do plan to extend our rules to include stratiﬁed negation, as this does not
complicate the semantics in the same way that unrestricted negation does). The inner loop of our program synthesis system is the calculation
of the trace τ(θ) by executing a Datalog⊃−program, so it is essential that the execution is as eﬃcient as possible. Hence our strong preference
for deﬁnite logic programs over normal logic programs.
Why do we not allow more complex constraints (e.g. allowing any ﬁrst-order sentence to be a constraint)? If we allowed any arbitrary
set of ﬁrst-order formulas as constraints, then computing the incompossibility relation would become much harder, given that computing
entailment in ﬁrst-order logic is only semi-decidable. The reason, then, why we focus on xor constraints is that they are the simplest construct
that generates the incompossibility relation needed to constrain the frame axiom.
14


## Page 15


1. Spatial unity: objects are united in space by being connected via chains of relations
2. Conceptual unity: predicates are united by constraints
3. Static unity: atoms are united in a state by jointly satisfying constraints and static rules
4. Temporal unity: states are united in a sequence by causal rules
Since temporal unity is automatically satisﬁed from the deﬁnition of a trace in Deﬁnition 9, we are left with only
three unity conditions that need to be explicitly checked: spatial unity, conceptual unity, and static unity. A trace
partially satisﬁes static unity since the static rules are automatically enforced by Deﬁnition 9; but the constraints
are not necessarily satisﬁed.
Note that both checking spatial unity and checking static unity require checking every time-step, and the trace is
inﬁnitely long. However, as long as the trace repeats at some point, Theorem 1 ensures that we need only check
the ﬁnite portion of the trace until we ﬁnd the ﬁrst repetition (the ﬁrst k such that A1 = Ak where τ(θ) = (A1, ...)).
3.4. Making sense
Now we are ready to deﬁne the central notion of “making sense” of a sequence.
Deﬁnition 16. A theory θ makes sense of a sensory sequence S if θ explains S, i.e. S ⊑τ(θ), and θ satisﬁes the four
conditions of unity of Deﬁnition 11. If θ makes sense of S, we also say that θ is a uniﬁed interpretation of S.
Example 4. The theory θ of Example 3 satisﬁes the four unity conditions since:
1. For each state Ai in τ(θ), a is connected to b via the singleton chain {r(a, b)}, and b is connected to a via {r(b, a)}.
2. The predicates of θ are on, oﬀ, p1, p2, p3, r. Here, on and oﬀare involved in the constraint ∀X:s, on(X) ⊕oﬀ(X),
while p1, p2, p3 are involved in the constraint ∀X:s, p1(X) ⊕p2(X) ⊕p3(X), and r is involved in the constraint
∀X:s, ∃!Y:s r(X, Y).
3. Let τ(θ) = (A1, A2, A3, A4, ...). It is straightforward to check that A1, A2, and A3 satisfy each constraint in C.
Observe that A4 repeats A1, thus Theorem 1 ensures that we do not need to check any more time steps.
4. Temporal unity is automatically satisﬁed by the deﬁnition of the trace τ(θ) in Deﬁnition 9.
Hence, θ makes sense of sensory sequence S of Example 1, since S ⊑τ(θ) (Example 3) and θ also satisﬁes the four
conditions of unity.
◁
In our search for interpretations that make sense of sensory sequences, we are particularly interested in parsimonious
interpretations. To this end, we deﬁne the cost of a theory18:
18Note that this simple measure of cost does not depend on the constraints in C or the type signature φ. There are various alternative more
complex deﬁnitions of cost. We could, for example, use the Kolmogorov complexity [68] of θ: the size of the smallest program that can generate
θ. Or we could use Levin complexity [69] and also take into account the log of the computation time needed to generate τ(θ), up to the point
where the trace ﬁrst repeats.
15


## Page 16


Deﬁnition 17. Given a theory θ = (φ, I, R, C), the cost of θ is
|I| +
X 
n + 1 | α1 ∧... ∧αn ◦α0 ∈R, ◦∈{→, ⊃−}

Here, cost(θ) is just the total number of ground atoms in I plus the total number of unground atoms in the rules of R.
The key notion of this section is the discrete apperception task.
Deﬁnition 18. The input to an apperception task is a triple (S, φ, C) consisting of a sensory sequence S, a suitable type
signature φ, and a set C of (well-typed) constraints such that (i) each predicate in S appears in some constraint in C and (ii)
S can be extended to satisfy C: there exists a sequence S′ covering S such that each state in S′ satisﬁes each constraint in C.
Given such an input triple (S, φ, C), the discrete apperception task is to ﬁnd the lowest cost theory θ = (φ′, I, R, C′) such
that φ′ extends φ, C′ ⊇C, and θ makes sense of S.
Note that the input to an apperception task is more than just a sensory sequence S. It also contains a type signature
φ and a set C of constraints. A natural question at this point is: why not simply let the input to an apperception
task be just the sequence S, and ask the system to produce some theory θ satisfying the unity conditions such that
S ⊑τ(θ)? The reason that the input needs to contain types φ and constraints C to supplement S is that otherwise
the task is severely under-constrained, as the following example shows.
Example 5. Suppose our sequence is S = ({on(a)}, {oﬀ(a)}, {on(a)}, {oﬀ(a)}, {on(a)}, {oﬀ(a)}). If we are not given any
constraints (such as ∀X : t, on(X) ⊕oﬀ(X)), if we are free to construct any φ and any set C of constraints, then
the following interpretation θ = (φ, I, R, C) will suﬃce, where φ = (T, O, P, V), consisting of types T = {t}, objects
O = {a:t}, predicates P = {on(t), oﬀ(t), p(t), q(t)}, and variables V = {X:t}, and suppose that I, R, C are deﬁned as:
I =

on(a)
oﬀ(a)

R =


C =

∀X:t, on(X) ⊕p(X)
∀X:t, oﬀ(X) ⊕q(X)

Here we have introduced two latent predicates p and q which are incompatible with on and oﬀrespectively. But in
this interpretation, on and oﬀare not incompatible with each other, so the degenerate interpretation (where both
on and oﬀare true at all times) is acceptable. This shows the need for including constraints on the input predicates
as part of the task formulation.
More generally, for any sensory sequence (S1, ..., ST) featuring predicates p1, ..., pn, but no constraints between
p1, ..., pn, we can always construct a degenerate interpretation by adding new predicates q1, ..., qn with an xor
constraint ∀X : t, pi(X) ⊕qi(X) between each predicate pi and the corresponding new predicate qi. In the degenerate
interpretation, the initial conditions I are S1∪...∪ST, and the rules R are empty. This shows that, without constraints
on the predicates appearing in the initial sequence, the problem is underspeciﬁed.
◁
16


## Page 17


The apperception task can be generalized to the case where we are given as input, not a single sensory sequence S,
but a set of m such sequences.
Deﬁnition 19. Given a set {S1, ..., Sm} of sensory sequences, a type signature φ and constraints C such that each (Si, φ, C) is
a valid input to an apperception task as deﬁned in Deﬁnition 18, the generalized apperception task is to ﬁnd a lowest-cost
theory (φ′, {}, R, C′) and sets {I1, ..., Im} of initial conditions such that φ′ extends φ, C′ ⊇C, and for each i = 1..m, (φ′, Ii, R, C′)
makes sense of Si.
3.5. Examples
In this section, we provide a worked example of an apperception task, along with diﬀerent uniﬁed interpretations.
We wish to highlight that there are always many alternative ways of interpreting a sensory sequence, each with
diﬀerent latent information (although some may have higher cost than others).
We continue to use our running example, the sensory sequence from Example 1. Here there are two sensors a and
b, and each sensor can be on or oﬀ.
S1 = {}
S2 = {oﬀ(a), on(b)}
S3 = {on(a), oﬀ(b)}
S4 = {on(a), on(b)}
S5 = {on(b)}
S6 = {on(a), oﬀ(b)}
S7 = {on(a), on(b)}
S8 = {oﬀ(a), on(b)}
S9 = {on(a)}
S10 = {}
Letφ = (T, O, P, V)whereT = {sensor}, O = {a, b}, P = {on(sensor), oﬀ(sensor)}, V = {X:sensor}. LetC = {∀X:sensor, on(X)⊕
oﬀ(X)}.
Examples 6, 7, and 8 below show three diﬀerent uniﬁed interpretations of Example 1.
Example 6. One possible way of interpreting Example 1 is as follows. The sensors a and b are simple state machines
that cycle between states p1, p2, and p3. Each sensor switches between on and oﬀdepending on which state it is
in. When it is in states p1 or p2, the sensor is on; when it is in state p3, the sensor is oﬀ. In this interpretation, the
two state machines a and b do not interact with each other in any way. Both sensors are following the same state
transitions. The reason the sensors are out of sync is because they start in diﬀerent states.
The type signature for this ﬁrst uniﬁed interpretation is φ′ = (T, O, P, V), where T = {sensor}, O = {a:sensor, b:sensor},
P = {on(sensor), oﬀ(sensor), r(sensor, sensor), p1(sensor), p2(sensor), p3(sensor)}, and V = {X:sensor, Y:sensor}. The three
unary predicates p1, p2, and p3 are used to represent the three states of the state machine.
17


## Page 18


Our ﬁrst uniﬁed interpretation is the tuple (φ′, I, R, C′), where:
I =

p2(a)
p1(b)
r(a, b)
r(b, a)

R =

p1(X) ⊃−p2(X)
p2(X) ⊃−p3(X)
p3(X) ⊃−p1(X)
p1(X) →on(X)
p2(X) →on(X)
p3(X) →oﬀ(X)

C′ =

∀X:sensor, on(X) ⊕oﬀ(X)
∀X:sensor, p1(X) ⊕p2(X) ⊕p3(X)
∀X:sensor, ∃!Y:sensor r(X, Y)

The update rules R contain three causal rules (using ⊃−) describing how each sensor cycles from state p1 to p2 to
p3, and then back again to p1. For example, the causal rule p1(X) ⊃−p2(X) states that if sensor X satisﬁes p1 at time
t, then X satisﬁes p2 at time t + 1. We know that X is a sensor from the variable typing information in φ′. R also
contains three static rules (using →) describing how the on or oﬀattribute of a sensor depends on its state. For
example, the static rule p1(Y) →on(X) states that if X satisﬁes p1 at time t, then X also satisﬁes on at time t.
The constraints C′ state that (i) every sensor is (exclusively) either on or oﬀ, that every sensor is (exclusively) either
p1, p2, or p3, and that every sensor has exactly one sensor that is related by r to it. The binary r predicate, or
something like it, is needed to satisfy the constraint of spatial unity.
In this ﬁrst interpretation, three new predicates are invented (p1, p2, and p3) to represent the three states of the state
machine. In the next interpretation, we will introduce new invented objects instead of invented predicates.
Given the initial conditions I and the update rules R, we can use our interpretation to compute which atoms hold at
which time step. In this case, τ(θ) = (A1, A2, ...) where Si ⊑Ai. Note that this trace repeats: Ai = Ai+3. We can use the
trace to predict the future values of our two sensors at time step 10, since A10 = {on(a), on(b), r(a, b), r(b, a), p2(a), p1(b)}.
As well as being able to predict future values, we can retrodict past values (ﬁlling in A1), or interpolate intermediate
unknown values (ﬁlling in A5 or A9).19 But although an interpretation provides the resources to “ﬁll in” missing
data, it has no particular bias to predicting future time-steps. The conditions which it is trying to satisfy (the unity
conditions of Section 3.3) do not explicitly insist that an interpretation must be able to predict future time-steps.
Rather, the ability to predict the future (as well as the ability to retrodict the past, or interpolate intermediate values)
is a derived capacity that emerges from the more fundamental capacity to “make sense” of the sensory sequence.
◁
Example 7. There are always inﬁnitely many diﬀerent ways of interpreting a sensory sequence. Next, we show a
rather diﬀerent interpretation of S1:10 from that of Example 6. In our second uniﬁed interpretation, we no longer
see sensors a and b as self-contained state-machines. Now, we see the states of the sensors as depending on their
left and right neighbours. In this new interpretation, we no longer need the three invented unary predicates (p1,
p2, and p3), but instead introduce a new object.
19This ability to “impute” intermediate unknown values is straightforward given an interpretation. Recent results show that current neural
methods for sequence learning are more comfortable predicting future values than imputing intermediate values.
18


## Page 19


Object invention is much less explored than predicate invention in inductive logic programming. But Dietterich et
al. [70] anticipated the need for it, and Inoue [18] uses meta-level abduction to posit unperceived objects.
Our new type signature φ′ = (T, O, P, V), where T = {sensor}, O = {a:sensor, b:sensor, c:sensor},
P = {on(sensor), oﬀ(sensor), r(sensor, sensor)}, and V = {X:sensor, Y:sensor}.
In this new interpretation, imagine there is a one-dimensional cellular automaton with three cells, a, b, and
(unobserved) c. The three cells wrap around: the right neighbour of a is b, the right neighbour of b is c, and the
right neighbour of c is a. In this interpretation, the spatial relations are ﬁxed. (We shall see another interpretation
later where this is not the case). The cells alternate between on and oﬀaccording to the following simple rule: if
X’s left neighbour is on (respectively oﬀ) at t, then X is on (respectively oﬀ) at t + 1.
Note that objects a and b are the two sensors we are given, but c is a new unobserved latent object that we posit
in order to make sense of the data. Many interpretations follow this pattern: new latent unobserved objects are
posited to make sense of the changes to the sensors we are given.
Note further that part of ﬁnding an interpretation is constructing the spatial relation between objects; this is not
something we are given, but something we must construct. In this case, we posit that the imagined cell c is inserted
to the right of b and to the left of a.
We represent this interpretation by the tuple (φ′, I, R, C′), where:
I =

on(a)
on(b)
oﬀ(c)
r(a, b)
r(b, c)
r(c, a)

R =

r(X, Y) ∧oﬀ(X) ⊃−oﬀ(Y)
r(X, Y) ∧on(X) ⊃−on(Y)

C′ =

∀X:sensor, on(X) ⊕oﬀ(X)
∀X:sensor, ∃!Y:sensor, r(X, Y)

Here, φ′ extends φ, C′ extends C, and the interpretation satisﬁes the unity conditions.
◁
Example 8. We shall give one more way of interpreting the same sensory sequence, to show the variety of possible
interpretations.
In our third interpretation, we will posit three latent cells, c1, c2, and c3 that are distinct from the sensors a and b.
Cells have static attributes: each cell can be either black or white, and this is a permanent unchanging feature of
the cell. Whether a sensor is on or oﬀdepends on whether the cell it is currently contained in is black or white.
The reason why the sensors change from on to oﬀis because they move from one cell to another.
Our new type signature (T, O, P, V) distinguishes between cells and sensors as separate types: T = {cell, sensor}, O =
{a : sensor, b : sensor, c1 : cell, c2 : cell, c3 : cell}, P = {on(sensor), oﬀ(sensor), part(sensor, cell), r(cell, cell), black(cell), white(cell)},
19


## Page 20


and V = {X : sensor, Y : cell, Y2 : cell}. Our interpretation is the tuple (φ, I, R, C), where:
I =

part(a, c1)
part(b, c2)
r(c1, c2)
r(c2, c3)
r(c3, c1)
black(c1)
black(c2)
white(c3)

R =

part(X, Y) ∧black(Y) →on(X)
part(X, Y) ∧white(Y) →oﬀ(X)
r(Y, Y2) ∧part(X, Y2) ⊃−part(X, Y)

C =

∀X:sensor, on(X) ⊕oﬀ(X)
∀Y:cell, black(Y) ⊕white(Y)
∀X:sensor, ∃!Y : cell, part(X, Y)
∀Y:cell, ∃!Y2 : cell, r(Y, Y2)

The update rules R state that the on or oﬀattribute of a sensor depends on whether its current cell is black or white.
They also state that the sensors move from right-to-left through the cells.
In this interpretation, there is no state information in the sensors. All the variability is explained by the sensors
moving from one static object to another.
Here, the sensors move about, so spatial unity is satisﬁed by diﬀerent sets of atoms at diﬀerent time-steps. For
example, at time-step 1, sensors a and b are indirectly connected via the ground atoms part(a, c1), r(c1, c2), part(b, c2).
But at time-step 2, a and b are indirectly connected via a diﬀerent set of ground atoms part(a, c3), r(c3, c1), part(b, c1).
Spatial unity requires all pairs of objects to always be connected via some chain of ground atoms at each time-step,
but it does not insist that it is the same set of ground atoms at each time-step.
◁
Examples 6, 7, and 8 provide diﬀerent ways of interpreting the same sensory input. In Example 6, the sensors are
interpreted as self-contained state machines. Here, there are no causal interactions between the sensors: each is an
isolated machine. In Examples 7 and 8, by contrast, there are causal interactions between the sensors. In Example
7, the on and oﬀattributes move from left to right along the sensors. In Example 8, it is the sensors that move, not
the attributes, moving from right to left. The diﬀerence between these two interpretations is in terms of what is
moving and what is static.
Note that the interpretations of Examples 6, 7, and 8 have costs 16, 12, and 17 respectively. So the theory of Example
7, which invents an unseen object, is preferred to the other theories that posit more complex dynamics.
3.6. Properties of interpretations
In this section, we provide some results about the correctness and completeness of uniﬁed interpretations.
Theorem 3. For each sensory sequence S = (S1, ..., St) and each uniﬁed interpretation θ of S, for each object x that features in
S (i.e. x appears in some ground atom p(x) or q(x, y) in some state Si in S), for each state Ai in τ(θ) = (A1, A2, ...), x features
in Ai. In other words, if x features in any state in S, then x features in every state in τ(θ).
Proof. Let θ = (φ, I, R, C) and φ = (T, O, P, V). Since object x features in sequence S, there exists some atom α
involving x in some state Sj in (S1, ..., St). Since θ is an interpretation, S ⊑τ(θ), and hence α ∈(τ(θ))j. Consider the
two possible forms of α:
20


## Page 21


1. α = p(x). Since θ satisﬁes conceptual unity, there must be a constraint involving p of the form ∀X : t, p(X) ⊕
q1(X)... ⊕qn(X) in C. Since φ is suitable for S, x ∈O and κO(x) = t. Let τ(θ) = (A1, A2, ...) and consider
any Ai in τ(θ). Since θ satisﬁes static unity, Ai satisﬁes each constraint in C and in particular Ai |= ∀X :
t, p(X) ⊕q1(X)... ⊕qn(X). Since κO(x) = t, Ai |= p(x) ⊕q1(x)... ⊕qn(x). Hence {p(x), q1(x), ..., qn(x)} ∩Ai , ∅i.e. x
features in Ai.
2. α = q(x, y) for some y. Since θ satisﬁes conceptual unity, there must be a constraint involving q. This constraint
can either be (i) a binary constraint of the form ∀X : t1, ∀Y : t2, q(X, Y) ⊕p1(X, Y) ⊕... ⊕pn(X, Y) or (ii) a
uniqueness constraint of the form ∀X : t1, ∃!Y : t2, q(X, Y).
Considering ﬁrst case (i), since φ is suitable for S, x, y ∈O, κO(x) = t1, and κO(y) = t2. Again, let τ(θ) =
(A1, A2, ...) and consider any Ai in τ(θ). Since θ satisﬁes static unity, Ai satisﬁes each constraint in C and
in particular Ai |= ∀X : t1, ∀Y : t2, q(X, Y) ⊕p1(X, Y) ⊕... ⊕pn(X, Y).
Since κO(x) = t1, κO(y) = t2, Ai |=
q(x, y) ⊕p1(x, y) ⊕... ⊕pn(x, y). Hence {q(x, y), p1(x, y), ..., pn(x, y)} ∩Ai , ∅i.e. x features in Ai.
For case (ii), again let τ(θ) = (A1, A2, ...) and consider any Ai in τ(θ). Since θ satisﬁes static unity, Ai satisﬁes
each constraint in C and in particular Ai |= ∀X : t1, ∃!Y : t2, q(X, Y). Since κO(x) = t1, Ai |= ∃!Y : t2, q(x, Y).
Therefore there must be some y such that κO(y) = t2 and q(x, y) ∈Ai.
□
Theorem 3 provides some guarantee that admissible interpretations that satisfy the unity conditions will always
be acceptable in the minimal sense that they always provide some value for each sensor. This theorem is important
because it justiﬁes the claim that a uniﬁed interpretation will always be able to support prediction (of future values),
retrodiction (of previous values), and imputation (of missing values).
Note that this theorem does not imply that the predicate of the atom in which x appears is one of the predicates
appearing in the sensory sequence S. It is entirely possible that it is some distinct predicate that appears in φ but
has never been observed in S. The following example illustrates this possibility.
Example 9. Suppose the sensory sequence is just S = ({p(a)}). Suppose the type signature (T, O, P, V) introduces
another unary predicate q, i.e. T = {t}, O = {a}, P = {p(t), q(t)}, and V = {X : t}. Suppose our interpretation is
(φ, I, R, C) where I = {p(a)}, R = {p(X)⊃−q(X)}, and C = {∀X : t, p(X)⊕q(X)}. Here, τ(θ) = ({p(a)}, {q(a)}, {q(a)}, {q(a)}, ...).
Note that q is a new predicate that does not appear in the sensory input; q is a “peer” of p (in that they are connected
by an xor constraint), but q was never observed.
◁
The next theorem is a form of “completeness”, showing that every sensory sequence has some admissible inter-
pretation that satisﬁes the unity conditions.
Theorem 4. For every apperception task (S, φ, C) there exists some interpretation θ = (φ′, I, R, C′) that makes sense of S,
where φ′ extends φ and C′ ⊇C.
Proof. First, we deﬁne φ′ given φ = (T, O, P, V). For each sensor xi that features in S, i = 1..n, and each state Sj in
S, j = 1..m, create a new unary predicate pi
j. The intention is that pi
j(X) is true if X is the i’th object xi at the j’th
21


## Page 22


time-step. If κO(xi) = t then let κP(pi
j) = (t). For each type t ∈T, create a new variable Xt where κV(Xt) = t. Let
φ′ = (T, O, P′, V′) where P′ = P ∪{pi
j | i = 1..n, j = 1..m}, and V′ = V ∪{Xt | t ∈T}.
Second, we deﬁne θ = (φ′, I, R, C′). Let the initial conditions I be:

pi
1(xi) | i = 1..n

Let the rules R contain the following causal rules for i = 1..n and j = 1..m −1 (where xi is of type t):
pi
j(Xt) ⊃−pi
j+1(Xt)
together with the following static rules for each unary atom q(xi) ∈Sj:
pi
j(Xt) →q(Xt)
and the following static rules for each binary atom r(xi, xk) ∈Sj (where xi is of type t and xk is of type t′):
pi
j(Xt) ∧pk
j(Yt′) →r(Xt, Yt′)
We augment C to C′ by adding the following additional constraints. Let Pt be the unary predicates for all objects
of type t:
Pt =

pi
j | κO(xi) = t, j = 1..m

Let Pt = {p′
1, ..., p′
k}. Then for each type t add a unary constraint:
∀Xt : t, p′
1(Xt) ⊕... ⊕p′
k(Xt)
It is straightforward to check that θ as deﬁned satisﬁes the constraint of conceptual unity, that the constraints
C′ are satisﬁed by each state in τ(θ), and that the sensory sequence is covered by τ(θ). To satisfy spatial unity,
add a new “world” object w of a new type tw and for each type t add a relation partt(t, tw) and a constraint
∀X : t, ∃!Y : tw, partt(X, Y). For each object x of type t, add an initial condition atom partt(x, w) to I. Thus, all the
conditions of unity are satisﬁed, and θ is a uniﬁed interpretation of S.
□
Example 10. Consider the following apperception problem (S, φ, C). Suppose there is one sensor a with values on
and oﬀ. Suppose the sensory sequence is S1:7 where:
S1 = {on(a)}
S2 = {oﬀ(a)}
S3 = {on(a)}
S4 = {oﬀ(a)}
S5 = {on(a)}
S6 = {oﬀ(a)}
S7 = {on(a)}
Let φ = (T, O, P, V) where T = {t}, O = {a : t}, P = {on(t), oﬀ(t)}, and V = {}. Clearly, φ is suitable for S. The constraints
C are just {∀X : t, on(X) ⊕oﬀ(X)}.
22


## Page 23


Applying Theorem 4, we generate 7 unary predicates p1, ..., p7. The type signature φ′ for this interpretation is
(T′, O′, P′, V′) where T′ = {t, tw}, O′ = {a, w}, P′ = P ∪{p1(t), p2(t), ..., p7(t), part(t, tw)}, and V′ = {X : t, Y : tw}. Our
interpretation is (φ′, I, R, C′) where:
I =

p1(a)
part(a, w)

R =

p1(X) ⊃−p2(X)
p2(X) ⊃−p3(X)
...
p6(Y) ⊃−p7(Y)
p1(X) →on(X)
p2(X) →oﬀ(X)
p3(X) →on(X)
p4(X) →oﬀ(X)
p5(X) →on(X)
p6(X) →oﬀ(X)
p7(X) →on(X)

C′ =

∀X : t, on(X) ⊕oﬀ(X)
∀X : t, p1(X) ⊕p2(X) ⊕... ⊕p7(X)
∀X : t, ∃!Y : tw part(X, Y)

◁
Note that the interpretation provided by Theorem 4 is degenerate and unilluminating: it treats each object entirely
separately (failing to capture any regularities between objects’ behaviour) and treats every time-step entirely
separately (failing to capture any laws that hold over multiple time-steps). This unilluminating interpretation
provides an upper bound on the complexity of the theory needed to make sense of the sensory sequence.
4. Computer implementation
The Apperception Engine is our system for solving apperception tasks.20 Given as input an apperception task
(S, φ, C), the engine searches for a type signature φ′ and a theory θ = (φ′, I, R, C′) where φ′ extends φ, C′ ⊇C and θ
makes sense of S. In this section, we describe how it is implemented.
Deﬁnition 20. A template is a structure for circumscribing a large but ﬁnite set of theories. It is a type signature together
with constants that bound the complexity of the rules in the theory. Formally, a template χ is a tuple (φ, N→, N⊃−, NB) where
φ is a type signature, N→is the max number of static rules allowed in R, N⊃−is the max number of causal rules allowed in R,
and NB is the max number of atoms allowed in the body of a rule in R.
Each template χ speciﬁes a large (but ﬁnite) set of theories that conform to χ. Let Θχ,C ⊂Θ be the subset of theories
(φ, I, R, C′) in Θ that conform to χ and where C′ ⊇C.
20The source code is available at https://github.com/RichardEvans/apperception.
23


## Page 24


Algorithm 1: The Apperception Engine algorithm in outline
input : (S, φ, C), an apperception task
output: θ∗, a uniﬁed interpretation of S
(s∗, θ∗) ←(max(ﬂoat), nil)
foreach template χ extending φ of increasing complexity do
θ ←argminθ{cost(θ) | θ ∈Θχ,C, S ⊑τ(θ), unity(θ)}
if θ , nil then
s ←cost(θ)
if s < s∗then
(s∗, θ∗) ←(s, θ)
end
end
if exceeded processing time then
return θ∗
end
end
Our method, presented in Algorithm 1, is an anytime algorithm that enumerates templates of increasing complexity.
For each template χ, it ﬁnds the θ ∈Θχ,C with lowest cost (see Deﬁnition 17) that satisﬁes the conditions of unity.
If it ﬁnds such a θ, it stores it. When it has run out of processing time, it returns the lowest cost θ it has found from
all the templates it has considered.
Note that the relationship between the complexity of a template and the cost of a theory satisfying the template is
not always simple. Sometimes a theory of lower cost may be found from a template of higher complexity. This is
why we cannot terminate as soon as we have found the ﬁrst theory θ. We must keep going, in case we later ﬁnd a
lower cost theory from a more complex template.
The two non-trivial parts of this algorithm are the way we enumerate templates, and the way we ﬁnd the lowest-cost
theory θ for a given template χ. We consider each in turn.
4.1. Iterating through templates
We need to enumerate templates in such a way that every template is (eventually) visited by the enumeration.
Since the objects, predicates, and variables are typed (see Deﬁnition 3), the acceptable ranges of O, P, and V depend
on T. Because of this, our enumeration procedure is two-tiered: ﬁrst, enumerate sets T of types; second, given
a particular T, enumerate (O, P, V, N→, N⊃−, NB) tuples for that particular T. We cannot, of course, enumerate all
(O, P, V, N→, N⊃−, NB) tuples because there are inﬁnitely many. Instead, we specify a constant bound (n) on the
number of tuples, and gradually increase that bound:
foreach (T, n) do
emit n tuples of the form (O, P, V, N→, N⊃−, NB)
end
In order to enumerate (T, n) pairs, we use a standard diagonalization procedure. See Table 1.
24


## Page 25


100
200
300
400
...
1
1
2
4
7
...
2
3
5
8
...
3
6
9
...
4
10
...
...
...
Table 1: Enumerating (t, n) pairs. Row t means that there are t types in T, while column n means there are n tuples of the form (O, P, V, N→, N⊃−, NB)
to enumerate. We increment n by 100. The entries in the table represent the order in which the (t, n) pairs are visited.
Once we have a (T, n) pair, we need to emit n (O, P, V, N→, N⊃−, NB) tuples using the types in T. One way of enumer-
ating k-tuples, where k > 2, is to use the diagonalization technique recursively: ﬁrst enumerate pairs, then apply
the diagonalization technique to enumerate pairs consisting of individual elements paired with pairs, and so on.
But this recursive application will result in heavy biases towards certain k-tuples. Instead, we use the Haskell func-
tion Universe.Helpers.choices to enumerate n-tuples while minimizing bias. The choices :: [[a]] -> [[a]]
function takes a ﬁnite number n of (possibly inﬁnite) lists, and produces a (possibly inﬁnite) list of n-tuples,
generating a n-way Cartesian product that is guaranteed to eventually produce every such n-tuple.
We use choices to generate 6-tuples (O, P, V, N→, N⊃−, NB) tuples by creating six inﬁnite streams: (i) SO: an inﬁnite
list of ﬁnite lists of typed objects, (ii) SP: an inﬁnite list of ﬁnite lists of typed predicates, (iii) SV: an inﬁnite list of
ﬁnite lists of typed variables, (iv) S→= {0, 1, ...}: the number of static rules, (v) S⊃−= {0, 1, ...}: the number of causal
rules, and (vi) SB = {0, 1, ...}: the max number of body atoms. Now when we pass this list of streams to the choices
function, it produces an enumeration of the 6-way Cartesian product SO × SP × SV × S→× S⊃−× SB.
Example 11. Recall the apperception problem from Example 1. There are two sensors a and b, and each sensor can
be on or oﬀ.
S1 = {}
S2 = {oﬀ(a), on(b)}
S3 = {on(a), oﬀ(b)}
S4 = {on(a), on(b)}
S5 = {on(b)}
S6 = {on(a), oﬀ(b)}
S7 = {on(a), on(b)}
S8 = {oﬀ(a), on(b)}
S9 = {on(a)}
S10 = {}
We shall start withaninitialtemplateχ0 = (φ = (T, O, P, V), N→, N⊃−, NB), whereT = {sensor, grid}, O = {a:sensor, b:sensor, g:grid},
P = {on(sensor), oﬀ(sensor), part(sensor, grid)}, V = {X:sensor, Y:sensor}, N→= 1, N⊃−= 3, and NB = 2. We use the
template enumeration procedure described above to generate increasingly complex templates χ1, χ2, ..., using χ0
as a base. This produces the following augmented templates :
∆χ1 = (∅, ∅, ∅, {V1:sensor}, 0, 0, 0)
∆χ2 = (∅, ∅, ∅, ∅, 0, 0, 1)
∆χ3 = (∅, ∅, {p1(sensor)}, ∅, 0, 0, 0)
∆χ4 = (∅, ∅, ∅, {V1:sensor}, 0, 0, 1)
∆χ5 = (∅, ∅, ∅, ∅, 0, 0, 2)
∆χ6 = (∅, {o1:sensor}, ∅, ∅, 0, 0, 0)
∆χ7 = (∅, ∅, {p1(sensor)}, ∅, 0, 0, 1)
∆χ8 = (∅, ∅, ∅, {V1:sensor}, 0, 0, 2)
∆χ9 = (∅, ∅, ∅, ∅, 0, 0, 2)
∆χ10 = (∅, ∅, {p1(sensor)}, {V1:sensor}, 0, 0, 0)
. . .
. . .
In the list above, we display the change from the base template χ0, so ∆χi means the changes in template χi from the
base template χ0. Each template χ = (φ = (T, O, P, V), N→, N⊃−, NB) is ﬂattened as a 7-tuple (T, O, P, V, N→, N⊃−, NB).
Many of these templates do not have the expressive resources to ﬁnd a uniﬁed interpretation. But some do. The
25


## Page 26


ﬁrst solution the Apperception Engine ﬁnds has the following type signature (the new elements are in bold):
T =

grid
sensor

O =

a : sensor
b : sensor
g : grid

P =

p1(sensor)
p2(sensor)
oﬀ(sensor)
on(sensor)
part(sensor, grid)

V =

S : sensor
S2 : sensor

together with the following theory θ = (φ, I, R, C), where:
I =

p1(a)
p2(b)
on(a)
part(a, g)
part(b, g)

R =

p2(S) →on(S)
p2(S) ⊃−p1(S)
p1(S) ∧on(S) ⊃−oﬀ(S)
oﬀ(S) ∧p1(S) ⊃−p2(S)

C =

∀X : sensor, p1(X) ⊕p2(X)
∀X : sensor, ∃!Y : grid, part(X, Y)

This solution uses the invented predicates p1 and p2 to represent two states of a state-machine. This is recognisable
as a compressed version of Example 6 above.
Later, the Apperception Engine ﬁnds another solution using the type signature φ = (T, O, P, V) (again, the aug-
mented parts of the type signature are in bold):
T =

grid
sensor

O =

a : sensor
b : sensor
g : grid
o1 : sensor

P =

r1(sensor, sensor)
oﬀ(sensor)
on(sensor)
part(sensor, grid)

V =

S : sensor
S2 : sensor

together with the following theory θ = (φ, I, R, C), where:
I =

oﬀ(o1)
on(a)
r1(a, o1)
r1(b, a)
r1(o1, b)
part(a, grid)
part(b, grid)
part(o1, grid)

R =

oﬀ(S) ∧r1(S, S2) →on(S2)
oﬀ(S2) ∧r1(S, S2) ∧on(S) ⊃−oﬀ(S)

C =

∀X:sensor, ∃!Y:grid, part(X, Y)
∀X:sensor, ∃!Y:sensor, r1(X, Y)

Here, it has constructed an invented object o1:sensor and posited a one-dimensional spatial relationship r1 between
the three sensors. This solution is recognisable as a variant of Example 7 above.
◁
26


## Page 27


X
P
Y
(a) Deduction
X
P
Y
(b) Abduction
X
P
Y
(c) Induction
X
P
Y
(d) Abduction and induction
Figure 1: The varieties of inference. Here, shaded elements are given, and unshaded elements must be generated. X and Y are sets of facts, while
P is a set of rules for transforming X into Y.
4.2. Finding the best theory from a template
The most complex part of Algorithm 1 is:
θ ←argmin
θ
{cost(θ) | θ ∈Θχ,C, S ⊑τ(θ), unity(θ)}
Here, we search for a theory θ with the lowest cost (see Deﬁnition 17) such that θ conforms to the template χ and
includes the constraints in C, such that τ(θ) covers S, and θ satisﬁes the conditions of unity. In this sub-section, we
explain in outline how this works.
Our approach combines abduction and induction to generate a uniﬁed interpretation θ.21 See Figure 1. Here,
X ⊆G is a set of facts (ground atoms), P : G →G is a procedure for generating the consequences of a set of facts,
and Y ⊆G is the result of applying P to X. If X and P are given, and we wish to generate Y, then we are performing
deduction. If P and Y are given, and we wish to generate X, then we are performing abduction. If X and Y are given,
and we wish to generate P, then we are performing induction. Finally, if only Y is given, and we wish to generate
both X and P, then we are jointly performing abduction and induction. This is what the Apperception Engine
does.22
Our method is described in Algorithm 2. In order to jointly abduce a set I (of initial conditions) and induce sets
R and C (of rules and constraints), we implement a Datalog⊃−interpreter in ASP. See Section 4.3 for the details.
This interpreter takes a set I of atoms (represented as a set of ground ASP terms) and sets R and C of rules and
constraints (represented again as a set of ground ASP terms), and computes the trace of the theory τ(θ) = (S1, S2, ...)
up to a ﬁnite time limit.
Concretely, we implement the interpreter as an ASP program πτ that computes τ(θ) for theory θ. We implement
the conditions of unity as ASP constraints in a program πu. We implement the cost minimization as an ASP
program πm that counts the number of atoms in each rule plus the number of initialisation atoms in I, and uses
an ASP weak constraint [60] to minimize this total. Then we generate ASP programs representing the sequence S,
the initial conditions, the rules and constraints. We combine the ASP programs together and ask the ASP solver
(clingo [72]) to ﬁnd a lowest cost solution. (There may be multiple solutions that have equally lowest cost; the
21For related work that also uses abduction, see [11, 71, 19].
22At a high level, our system is similar to XHAIL [11]. But there are a number of diﬀerences. First, our program P contains causal rules and
constraints as well as standard Horn clauses. Second, our conclusion Y is an inﬁnite sequence (S1, S2, ...) of sets, rather than a single set. Third,
we add additional ﬁlters on acceptable theories in the form of the unity conditions (see Deﬁnition 11).
27


## Page 28


ASP solver chooses one of the optimal answer sets). We extract a readable interpretation θ from the ground atoms
of the answer set. In Section 4.3, we explain how Algorithm 2 is implemented in ASP. In Section 4.4, we evaluate
the computational complexity. In Section 4.5, we describe the various optimisations used to prune the search. In
Section 5.2.4, we compare with ILASP, a state-of-the-art ILP system.
Algorithm 2: Finding the lowest cost θ for sequence S and template χ. Here, πτ computes the trace, πu checks that
the unity conditions are satisﬁed, and πm minimizes the cost of θ.
input : S, a sensory sequence
input : χ = (φ, N→, N⊃−, NB), a template
input : C, a set of constraints on the predicates of the sensory sequence
output: θ, the simplest uniﬁed interpretation of S that conforms to χ
πS ←gen input(S)
πI ←gen inits(φ)
πR ←gen rules(φ, N→, N⊃−, NB)
πC ←gen constraints(φ, C)
Π ←πτ ∪πu ∪πm ∪πS ∪πI ∪πR ∪πC
A ←clingo(Π)
if satisﬁable(A) then
θ ←extract(A)
return θ
end
return nil
4.3. The ASP encoding
Our Datalog⊃−interpreter is written in ASP. All elements of Datalog⊃−, including variables, are represented by ASP
constants. A variable X is represented by a constant var_x, and a predicate p is represented by a constant c_p.
Elements of the target language are reiﬁed in ASP, so an unground atom p(X) of Datalog⊃−is represented by a term
s(c_p, var_x), and a rule is represented by a set of ground atoms for the body, and a single ground atom for the
head. For example, the static rule p(X) ∧q(X, Y) →r(Y) is represented as:
rule_body(r1, s(c_p, var_x)).
rule_body(r1, s2(c_q, var_x, var_y)).
rule_head_static(r1, s(c_r, var_y)).
The causal rule on(X) ⊃−oﬀ(X) is represented as:
rule_body(r2, s(c_on, var_x)).
rule_head_causes(r2, s(c_off, var_x)).
Given a type signature φ, we construct ASP terms that represent every well-typed unground atom in Uφ, and
wrap these terms in the is_var_atom predicate. For example, to represent that r(C, C2) is a well-typed unground
atom, we write is_var_atom(atom(c_r, var_c, var_c2)). Similarly, we construct ASP terms that represent
every well-typed ground atom in Gφ using the is_ground_atom predicate.
The initial conditions I ⊆Gφ are represented by the init predicate. For example, to represent that I = {p(a), r(b, c)},
we write:
28


## Page 29


init(s(c_p, c_a)).
init(s2(c_r, c_b, c_c)).
Our meta-interpreter πτ implements τ : Θ →(2G)∗from Deﬁnition 9. We use holds(a, t) to represent that atom
a is true at time t (i.e. a ∈St where τ(θ) = (S1, S2, ..., St, ...)).
% initial conditions
holds(A, T) :-
init(A),
init_time(T).
% update for static rules
holds(GA, T) :-
rule_head_static(R, VA),
eval_body(R, Subs, T),
ground_atom(VA, GA, Subs).
% update for causal rules
holds(GC, T+1) :-
rule_head_causes(R, VC),
eval_body(R, Subs, T),
ground_atom(VC, GC, Subs),
is_time(T+1).
% frame axiom
holds(S, T+1) :-
holds(S, T),
is_time(T+1),
not -holds(S, T+1).
Since τ(θ) is an inﬁnite sequence (A1, A2, ...), we cannot compute the whole of it. Instead, we only compute the
sequence up to the max time of the original sensory sequence S.
Note that the frame axiom uses negation as failure and strong negation [63] to check that some other incompatible
atom has not already been added. Thus, the frame axiom is not restrictive and can be overridden as needed by the
causal rules, to handle predicates that are not inertial.
The conditions of unity described in Section 3.3 are represented directly as ASP constraints in πu. For example,
spatial unity is encoded as:
:-
spatial_unity_counterexample(X, Y, T).
Here, there is a counterexample to spatial unity at time T if objects X and Y are not related:
spatial_unity_counterexample(X, Y, T) :-
is_object(X),
is_object(Y),
is_time(T),
not related(X, Y, T).
Here, related is the reﬂexive symmetric transitive closure of the relation holding between X and Y if there is
some relation R connecting them. Note that related can quantify over relations because the Datalog⊃−atoms and
predicates have been reiﬁed into terms:
29


## Page 30


related(X, Y, T) :-
holds(s2(R, X, Y), T).
related(X, X, T) :-
is_object(X),
is_time(T).
related(X, Y, T) :- related(Y, X, T).
related(X, Y, T) :-
related(X, Z, T),
related(Z, Y, T).
When constructing a theory θ = (φ, I, R, C), the solver needs to choose which ground atoms to use as initial
conditions in I, which static and causal rules to include in R, and which xor or uniqueness conditions to use as
conditions in C.
To allow the solver to choose what to include in I, we add the ASP choice rule to πI:
{ init(A) } :- is_ground_atom(A).
To allow the solver to choose which rules to include in R, we add the following clauses to πR:
0 { rule_body(R, VA) : is_var_atom(VA) } k_max_body :- is_rule(R).
1 { rule_head_static(R, VA) : is_var_atom(VA) } 1 :- is_static_rule(R).
1 { rule_head_causes(R, VA) : is_var_atom(VA) } 1 :- is_causes_rule(R).
Here, k_max_body is the NB parameter of the template that speciﬁes the max number of body atoms in any rule.
The number of rules satisfying is_static_rule and is_causes_rule is determined by the parameters N⊃−and N→
in the template (see Deﬁnition 20).
The ASP program πm minimizes the cost of the theory θ (see Deﬁnition 17) by using weak constraints [60]:
:∼rule body(R, A). [1@1, R, A]
:∼rule head static(R, A). [1@1, R, A]
:∼rule head causes(R, A). [1@1, R, A]
:∼init(A). [1@1, A]
4.4. Complexity
This section describes the complexity of Algorithm 2.
We assume basic concepts and standard terminology from complexity theory. Let P be the class of problems
that can be solved in polynomial time by a deterministic Turing machine, NP be the class of problems solved in
polynomial time by a non-deterministic Turing machine, and EXPTIME be the class of problems solved in time
2nd by a deterministic Turing machine. Let ΣP
i+1 = NPΣP
i be the class of problems that can be solved in polynomial
time by a non-deterministic Turing machine with a ΣP
i oracle. If Π is a Datalog program, and A and B are sets of
ground atoms, then:
30


## Page 31


Predicate
# ground clauses
holds
|Σφ| · |Uφ| · (N→+ N⊃−) · t + |Gφ| · (t + 1)
eval_atom(VA, Subs, T)
|Σφ| · |Uφ| · t
eval_body(R, Subs, T)
|Σφ| · (N→+ N⊃−) · t
Table 2: The number of ground clauses in the ASP encoding of Algorithm 2.
• the data complexity is the complexity of testing whether Π ∪A |= B, as a function of A and B, when Π is ﬁxed
• the program complexity (also known as “expression complexity”) is the complexity of testing whether
Π ∪A |= B, as a function of Π and B, when A is ﬁxed
Datalog has polynomial time data complexity but exponential time program complexity: deciding whether a
ground atom is in the least Herbrand model of a Datalog program is EXPTIME-complete. The reason for this
complexity is because the number of ground instances of a clause is an exponential function of the number of
variables in the clause. Finding a solution to an ASP program is in NP [73, 74], while ﬁnding an optimal solution
to an ASP program with weak constraints is in ΣP
2 [75, 76].
Since deciding whether a non-disjunctive ASP program has a solution is in NP [73, 74], our ASP encoding of
Algorithm 2 shows that ﬁnding a uniﬁed interpretation θ for a sequence given a template is in NP. Since verifying
whether a solution to an ASP program with preferences is indeed optimal is in ΣP
2 [75, 76], our ASP encoding shows
that ﬁnding the lowest cost θ is in ΣP
2.
However, the standard complexity results assume the ASP program has already been grounded into a set of propositional
clauses.
To really understand the space and time complexity of Algorithm 2, we need to examine how the
set of ground atoms in the ASP encoding grows as a function of the parameters in the template χ = (φ =
(T, O, P, V), N→, N⊃−, NB).
Observe that, since we restrict ourselves to unary and binary predicates, the number of ground and unground
atoms is a small polynomial function of the type signature parameters23:
|Gφ|
≤
|P| · |O|2
|Uφ|
≤
|P| · |V|2
But note that the number of substitutions Σφ that is compatible with the signature φ is an exponential function of
the number of variables V:
|Σφ|
≤
|O||V|
Table 3 shows the number of ground clauses for the three most expensive clauses. The total number of ground
atoms for the three most expensive clauses is approximately 5 · |Σφ| · (N→+ N⊃−) · |Uφ| · t.
23The actual numbers will be less than these bounds because type-checking rules out certain combinations.
31


## Page 32


Clause
# ground clauses
# atoms
holds(GA, T) :-
rule_head_static(R, VA),
eval_body(R, Subs, T),
ground_atom(VA, GA, Subs).
|Σφ| · |Uφ| · N→· t
4
holds(GA, T+1) :-
rule_head_causes(R, VA),
eval_body(R, Subs, T),
ground_atom(VA, GA, Subs).
|Σφ| · |Uφ| · N⊃−· t
4
eval_body(R, Subs, T) :-
is_rule(R),
is_subs(Subs),
is_time(T),
eval_atom(V, Subs, T) :
rule_body(R, V).
|Σφ| · (N→+ N⊃−) · t
|Uφ| + 4
Table 3: The number of ground clauses in the ASP encoding of Algorithm 2.
4.5. Optimization
Because of the combinatorial complexity of the apperception task, we had to introduce a number of optimizations
to get reasonable performance on even the simplest of domains.
4.5.1. Reducing grounding with type checking
We use the type signature φ to dramatically restrict the set of ground atoms (Gφ), the unground atoms (Uφ), the
substitutions (Σφ), and rules Rφ. Type-checking has been shown to drastically reduce the search space in program
synthesis tasks [77].
4.5.2. Symmetry breaking
We use symmetry breaking to remove candidates that are equivalent. We remove programs that are equivalent up
to a variable renaming by using a strict ordering on variables. We also remove programs that are equivalent up to
a reordering of the rules by using a strict ordering on unground atoms.
4.5.3. Adding redundant constraints
ASP programs can be signiﬁcantly optimized by adding redundant constraints (constraints that are provably
entailed by the other clauses in the program) [78]. We speeded up solving time (by about 30%) by adding the
following redundant constraints:
:-
init(A),
init(B),
incompossible(A, B).
:-
rule_body(R, A),
rule_body(R, B),
32


## Page 33


incompossible_var_atoms(A, B).
:-
rule_body(R, A),
rule_head_static(R, A).
:-
rule_body(R, A),
rule_head_causes(R, A).
:-
rule_body(R, A),
rule_head_static(R, B),
incompossible_var_atoms(A, B).
:-
rule_body(R, A),
rule_head_causes(R, B),
incompossible_var_atoms(A, B).
5. Experiments
5.1. Five experimental domains
To evaluate the generality of our system, we tested it in a variety of domains: elementary (one-dimensional)
cellular automata, drum rhythms and nursery tunes, sequence induction tasks, multi-modal binding tasks, and
occlusion tasks. These particular domains were chosen because they represent a diverse range of tasks that are
simple for humans but are hard for state-of-the-art machine learning systems. The tasks were chosen to highlight
the diﬀerence between mere perception (the classiﬁcation tasks that machine learning systems already excel at) and
apperception (assimilating information into a coherent integrated theory, something traditional machine learning
systems are not designed to do).
5.1.1. Results
We implemented the Apperception Engine in Haskell and ASP. We used clingo [72] to solve the ASP programs
generated by our system. We ran all experiments with a time-limit of 4 hours on a standard Unix desktop.
Our experiments (on the prediction task) are summarised in Table 4. Note that our accuracy metric for a single task
is rather exacting: the model is accurate (Boolean) on a task iﬀevery hidden sensor value is predicted correctly.24
It does not score any points for predicting most of the hidden values correctly. As can be seen from Table 4, our
system is able to achieve good accuracy across all ﬁve domains.
5.1.2. Elementary cellular automata
An Elementary Cellular Automaton (ECA) [79, 80] is a one-dimensional Cellular Automaton. The world is a
circular array of cells. Each cell can be either on or oﬀ. The state of a cell depends only on its previous state and the
previous state of its left and right neighbours.
24The reason for using this strict notion of accuracy is that, as the domains are deterministic and noise-free, there is a simplest possible theory
that explains the sensory sequence. In such cases where there is a correct answer, we wanted to assess whether the system found that correct
answer exactly – not whether it was fortunate enough to come close while misunderstanding the underlying dynamics.
33


## Page 34


Domain
Tasks
(#)
Memory
(megs)
Input size
(bits)
Held out size
(bits)
Accuracy
(%)
ECA
256
473.2
154.0
10.7
97.3%
Rhythm & music
30
2172.5
214.4
15.3
73.3%
Seek Whence
30
3767.7
28.4
2.5
76.7%
Multi-modal binding
20
1003.2
266.0
19.1
85.0%
Occlusion
20
604.3
109.2
10.1
90.0 %
Table 4: Results for prediction tasks on ﬁve domains. We show the mean information size of the sensory input, to stress the scantiness of our
sensory sequences. We also show the mean information size of the held-out data. Our metric of accuracy for prediction tasks is whether the
system predicted every sensor’s value correctly.
0
1
1
0
1
1
1
0
Figure 2: Updates for ECA rule 110. The top row shows the context: the target cell together with its left and right neighbour. The bottom row
shows the new value of the target cell given the context. A cell is black if it is on and white if it is oﬀ.
Figure 2 shows one set of ECA update rules25. Each update speciﬁes the new value of a cell based on its previous
left neighbour, its previous value, and its previous right neighbour. The top row shows the values of the left
neighbour, previous value, and right neighbour. The bottom row shows the new value of the cell. There are 8
updates, one for each of the 23 conﬁgurations. In the diagram, the leftmost update states that if the left neighbour
is on, and the cell is on, and its right neighbour is on, then at the next time-step, the cell will be turned oﬀ. Given
that each of the 23 conﬁgurations can produce on or oﬀat the next time-step, there are 223 = 256 total sets of update
rules.
Given update rules for each of the 8 conﬁgurations, and an initial starting state, the trajectory of the ECA is
determined. Figure 3 shows the state sequence for Rule 110 above from one initial starting state of length 11.
In our experiments, we attach sensors to each of the 11 cells, produce a sensory sequence, and then ask our system
to ﬁnd an interpretation that makes sense of the sequence. For example, for the state sequence of Figure 3, the
25This particular set of update rules is known as Rule 110. Here, 110 is the decimal representation of the binary 01101110 update rule, as
shown in Figure 2. This rule has been shown to be Turing-complete [80].
110
? ? ? ? ? ? ? ? ? ? ?
Figure 3: One trajectory for Rule 110. Each row represents the state of the ECA at one time-step. In this prediction task, the bottom row
(representing the ﬁnal time-step) is held out.
34


## Page 35


sensory sequence is (S1, ..., S10) where:
S1
=
{oﬀ(c1), oﬀ(c2), oﬀ(c3), oﬀ(c4), oﬀ(c5), on(c6), oﬀ(c7), oﬀ(c8), oﬀ(c(), oﬀ(c10), oﬀ(c11)}
S2
=
{oﬀ(c1), oﬀ(c2), oﬀ(c3), oﬀ(c4), on(c5), on(c6), oﬀ(c7), oﬀ(c8), oﬀ(c(), oﬀ(c10), oﬀ(c11)}
S3
=
{oﬀ(c1), oﬀ(c2), oﬀ(c3), on(c4), on(c5), on(c6), oﬀ(c7), oﬀ(c8), oﬀ(c(), oﬀ(c10), oﬀ(c11)}
S4
=
{oﬀ(c1), oﬀ(c2), on(c3), on(c4), oﬀ(c5), on(c6), oﬀ(c7), oﬀ(c8), oﬀ(c(), oﬀ(c10), oﬀ(c11)}
S5
=
{oﬀ(c1), on(c2), on(c3), on(c4), on(c5), on(c6), oﬀ(c7), oﬀ(c8), oﬀ(c(), oﬀ(c10), oﬀ(c11)}
...
Note that we do not provide the spatial relation between cells. The system does not know that e.g. cell c1 is directly
to the left of cell c2.
Results. Given the 256 ECA rules, all with the same initial conﬁguration, we treated the trajectories as a prediction
task and applied our system to it. Our system was able to predict 249/256 correctly. In each of the 7/256 failure
cases, the Apperception Engine found a uniﬁed interpretation, but this interpretation produced a prediction which
was not the same as the oracle. For example, the dynamics found for Figure 3 above are:
R =

r(X, Y) ∧on(X) ∧oﬀ(Y) ⊃−on(Y)
r(X, Y) ∧r(Y, Z) ∧on(X) ∧on(Z) ∧on(Y) ⊃−oﬀ(Y)

These rules exactly capture the dynamics of the cells that change. The other cells retain their value from the previous
time-step, according to the frame axiom of Deﬁnition 9.
The initial conditions found by the Apperception Engine describe the initial values of the cells, and also specify
the latent r relation between cells:
I =

oﬀ(c1)
oﬀ(c2)
oﬀ(c3)
oﬀ(c4)
oﬀ(c5)
on(c6)
oﬀ(c7)
oﬀ(c8)
oﬀ(c9)
oﬀ(c10)
oﬀ(c11)
r(c1, c11)
r(c2, c1)
r(c3, c2)
r(c4, c3)
r(c5, c4)
r(c6, c5)
r(c7, c6)
r(c8, c7)
r(c9, c8)
r(c10, c9)
r(c11, c10)

Here, the system uses r(X, Y) to mean that cell Y is immediately to the right of cell X. Note that the system has
constructed the spatial relation itself. It was not given the spatial relation r between cells. All it was given was the
sensor readings of the 11 cells. It constructed the spatial relationship r between the cells in order to make sense of
the data.
5.1.3. Drum rhythms and nursery tunes
We also tested our system on simple melodies and rhythms. Here, each sensor is an auditory receptor that is tuned
to listen for a particular note or drum beat. In the tune tasks, there is one sensor for C, one for D, one for E, all
the way to HighC. (There are no ﬂats or sharps). In the rhythm tasks, there is one sensor listening out for bass
drum, one for snare drum, and one for hi-hat. Each sensor can distinguish four loudness levels, between 0 and 3.
35


## Page 36


When a note is pressed, it starts at max loudness (3), and then decays down to 0. Multiple notes can be pressed
simultaneously.
For example, the Twinkle Twinkle Little Star tune generates the following sensor readings (assuming 8 time-steps
for a bar):
S1
=
{v(sc, 3), v(sd, 0), v(se, 0), v(s f, 0), v(sg, 0), v(sa, 0), v(sb, 0), v(sc∗, 0)}
S2
=
{v(sc, 2), v(sd, 0), v(se, 0), v(s f, 0), v(sg, 0), v(sa, 0), v(sb, 0), v(sc∗, 0)}
S3
=
{v(sc, 3), v(sd, 0), v(se, 0), v(s f, 0), v(sg, 0), v(sa, 0), v(sb, 0), v(sc∗, 0)}
S4
=
{v(sc, 2), v(sd, 0), v(se, 0), v(s f, 0), v(sg, 0), v(sa, 0), v(sb, 0), v(sc∗, 0)}
S5
=
{v(sc, 1), v(sd, 0), v(se, 0), v(s f, 0), v(sg, 3), v(sa, 0), v(sb, 0), v(sc∗, 0)}
S6
=
{v(sc, 0), v(sd, 0), v(se, 0), v(sf, 0), v(sg, 2), v(sa, 0), v(sb, 0), v(sc∗, 0)}
...
Results. Recall that our accuracy metric is stringent and only counts a prediction as accurate if every sensor’s value
is predicted correctly. In the rhythm and music domain, this means the Apperception Engine must correctly
predict the loudness value (between 0 and 3) for each of the sound sensors. There are 8 sensors for tunes and 3
sensors for rhythms. When we tested the Apperception Engine on the 20 drum rhythms and 10 nursery tunes, our
system was able to predict 22/30 correctly. Note that the interpretations found are large and complex programs
by the standards of state-of-the-art ILP systems. In Three Blind Mice, for example, the interpretation contained 10
update rules and 34 initialisation atoms making a total of 44 clauses.
5.1.4. Seek Whence and C-test sequence induction intelligence tests
Hofstadter introduced the Seek Whence26 domain in [24]. The task is, given a sequence s1, ..., st of symbols, to
predict the next symbol st+1. Typical Seek Whence tasks include27:
• b, b, b, c, c, b, b, b, c, c, b, b, b, c, c, ...
• a, f, b, f, f, c, f, f, f, d, f, f, ...
• b, a, b, b, b, b, b, c, b, b, d, b, b, e, b, ...
Hofstadter called the third sequence the “theme song” of the Seek Whence project because of its diﬃculty. There is
a “perceptual mirage” in the sequence because of the sub-sequence of ﬁve b’s in a row that makes it hard to see the
intended pattern: (b, x, b)∗for ascending x.
26The name is a pun on “sequence”. See also the related Copycat domain [81].
27Hofstadter used natural numbers, but we transpose the sequences to letters, to bring them in line with the Thurstone letter completion
problems [82] and the C-test [83].
36


## Page 37


a,a,b,a,b,c,a,b,c,d,a, ...
a,b,c,d,e, ...
b,a,b,b,b,b,b,c,b,b,d,b,b,e, ...
a,b,b,c,c,c,d,d,d,d,e, ...
a,f,e,f,a,f,e,f,a,f,e,f,a, ...
b,a,b,b,b,c,b,d,b,e, ...
a,b,b,c,c,d,d,e,e, ...
a,b,c,c,d,d,e,e,e,f,f,f, ...
f,a,f,b,f,c,f,d,f, ...
a,f,e,e,f,a,a,f,e,e,f,a,a, ...
b,b,b,c,c,b,b,b,c,c,b,b,b,c,c, ...
b,a,a,b,b,b,a,a,a,a,b,b,b,b,b, ...
b,c,a,c,a,c,b,d,b,d,b,c,a,c,a, ...
a,b,b,c,c,d,d,e,e,f,f, ...
a,a,b,a,b,c,a,b,c,d,a,b,c,d,e, ...
b,a,c,a,b,d,a,b,c,e,a,b,c,d,f, ...
a,b,a,c,b,a,d,c,b,a,e,d,c,b, ...
c,b,a,b,c,b,a,b,c,b,a,b,c,b, ...
a,a,a,b,b,c,e,f,f, ...
a,a,b,a,a,b,c,b,a,a,b,c,d,c,b, ...
a,a,b,c,a,b,b,c,a,b,c,c,a,a,a, ...
a,b,a,b,a,b,a,b,a, ...
a,c,b,d,c,e,d, ...
a,c,f,b,e,a,d, ...
a,a,f,f,e,e,d,d, ...
a,a,a,b,b,b,c,c, ...
a,a,b,b,f,a,b,b,e,a,b,b,d, ...
f,a,d,a,b,a,f,a,d,a,b,a, ...
a,b,a,f,a,a,e,f,a, ...
b,a,f,b,a,e,b,a,d, ...
Figure 4: Sequences from Seek Whence and the C-test
Results. Given the 30 Seek Whence sequences, we treated the trajectories as a prediction task and applied our system
to it. Our system was able to predict 23/30 correctly. For the 7 failure cases, 4 of them were due to the system not
being able to ﬁnd any uniﬁed interpretation within the memory and time limits, while in 3 of them, the system
found a uniﬁed interpretation that produced the “incorrect” prediction.
The ﬁrst key point we want to emphasise here is that our system was able to achieve human-level performance28
on these tasks without hand-coded domain-speciﬁc knowledge.29 This is a general system for making sense of
sensory data that, when applied to the Seek Whence domain, is able to solve these particular problems. The second
point we want to stress is that our system did not learn to solve these sequence induction tasks after seeing many
previous examples.30 On the contrary: our system had never seen any such sequences before; it confronts each
sequence de novo, without prior experience. This system is, to the best of our knowledge, the ﬁrst such general
system that is able to achieve such a result.
5.1.5. Binding tasks
The binding problem [86] is the task of recognising that information from diﬀerent sensory modalities should be
collected together as diﬀerent aspects of a single external object. For example, you hear a buzzing and a siren in
your auditory ﬁeld and you see an insect and an ambulance in your visual ﬁeld. How do you associate the buzzing
and the insect-appearance as aspects of one object, and the siren and the ambulance appearance as aspects of a
separate object?
To investigate how our system handles such binding problems, we tested it on the following multi-modal variant
of the ECA described above. Here, there are two types of sensor. The light sensors have just two states: black and
white, while the touch sensors have four states: fully un-pressed (0), fully pressed (3), and two intermediate states
(1, 2). After a touch sensor is fully pressed (3), it slowly depresses, going from states 2 to 1 to 0 over 3 time-steps.
28See Meredith [84] for empirical results 25 students on the“Blackburn dozen” Seek Whence problems.
29The one piece of domain-speciﬁc knowledge we inject is the successor relation between the letters a, b, c, ...
30Machine learning approaches to these tasks need thousands of examples before they can learn to predict. See for example [85].
37


## Page 38


l1
l2
l3
l4
l5
l6
l7
l8
l9
l10
l11
t1
t2
W W W W W
B
W W W W W
0
0
W W W W
B
B
W W W W W
0
0
W W W
B
B
B
W W W W W
0
0
W W
B
B
W
B
W W W W W
3
0
W
B
B
B
B
B
W W W W W
3
0
B
B
W W W
B
W W W W W
2
0
B
B
W W
B
B
W W W W
B
1
3
W
B
W
B
B
B
W W W
B
B
0
3
B
B
B
B
W
B
W W
B
B
B
3
3
W W W
B
B
B
W
B
B
W W
2
2
?
?
?
?
?
?
?
?
?
?
?
?
?
110
Figure 5: A multi-modal trace of ECA rule 110 with eleven light sensors (left) l1, ..., l11 and two touch sensors (right) t1, t2 attached to cells 3 and
11. Each row represents the states of the sensors for one time-step. For this prediction task, the ﬁnal time-step is held out.
In this example, we chose Rule 110 (the Turing-complete ECA rule) with the same initial conﬁguration as in Figure
3, as described earlier. In this multi-modal variant, there are 11 light sensors, one for each cell in the ECA, and two
touch sensors on cells 3 and 11. See Figure 5.
Results. We ran 20 multi-modal binding experiments, with diﬀerent ECA rules, diﬀerent initial conditions, and the
touch sensors attached to diﬀerent cells. The engine achieved 85% accuracy.
5.1.6. Occlusion tasks
Neural nets that predict future sensory data conditioned on past sensory data struggle to solve occlusion tasks
because it is hard to inject into them the prior knowledge that objects persist over time. Our system, by contrast,
was designed to posit latent objects that persist over time.
To test our system’s ability to solve occlusion problems, we generated a set of tasks of the following form: there is
a 2D grid of cells in which objects move horizontally. Some move from left to right, while others move from right
to left, with wrap around when they get to the edge of a row. The objects move at diﬀerent speeds. Each object is
placed in its own row, so there is no possibility of collision. There is an “eye” placed at the bottom of each column,
looking up. Each eye can only see the objects in the column it is placed in. An object is occluded if there is another
object below it in the same column. See Figure 6.
The system receives a sensory sequence consisting of the positions of the moving objects whenever they are visible.
The positions of the objects when they are occluded is used as held-out test data to verify the predictions of the
model. This is an imputation task.
Results. We generated 20 occlusion tasks by varying the size of the grid, the number of moving objects, their
direction and speed. The Apperception Engine achieved 90% accuracy.
38


## Page 39


Legend
Speed: slow
Speed: medium
Visible object
Occluded object
eye
eye
eye
eye
eye
eye
eye
Figure 6: An occlusion task
5.2. Empirical evaluations
In this section, we test our system to evaluate the truth of the following hypotheses:
1. The ﬁve domains of section 5.1 are challenging tasks for existing baselines.
2. Our system handles retrodiction and imputation just as easily as prediction.
3. The features of our system (unity conditions, cost minimisation) are essential to its performance.
4. Our system outperforms state-of-the-art inductive logic programming approaches in the ﬁve domains.
We consider each in turn.
5.2.1. The ﬁve domains of section 5.1 are challenging tasks for existing baselines
To evaluate whether our domains are indeed suﬃciently challenging, we compared our system against four
baselines. The ﬁrst constant baseline always predicts the same constant value for every sensor for each time-step.
The second inertia baseline always predicts that the ﬁnal hidden time-step equals the penultimate time-step. The
third MLP baseline is a fully-connected multilayer perceptron (MLP) [87] that looks at a window of earlier time-
steps to predict the next time-step. The fourth LSTM baseline is a recurrent neural net based on the long short-term
memory (LSTM) architecture [88].
The neural baselines are designed to exploit potential statistical patterns that are indicative of hidden sensor states.
In the MLP baseline, we formulate the problem as a multi-class classiﬁcation problem, where the input consists
in a feature representation x of relevant context sensors, and a feed-forward network is trained to predict the
correct state y of a given sensor in question. In the prediction task, the feature representation comprises one-hot31
representations for the state of every sensor in the previous two time steps before the hidden sensor. The training
data consists of the collection of all observed states in an episode (as potential hidden sensors), together with the
respective history before. Samples with incomplete history window (at the beginning of the episode) are discarded.
31A one-hot representation of feature i of n possible features is a vector of length n in which all the elements are 0 except the i’th element.
39


## Page 40


eca
music
Seek-Whence
0
50
100
predictive accuracy
our system (AE)
constant baseline
inertia baseline
MLP baseline
LSTM baseline
Figure 7: Comparison with baselines. We display predictive accuracy on the held-out ﬁnal time-step.
The MLP classiﬁer is a 2-layer feed-forward neural network, which is trained on all training examples derived
from the current episode (thus no cross-episode transfer is possible). We restrict the number of hidden neurons to
(20, 20) for the two layers, respectively, in order to prevent overﬁtting given the limited number of training points
within an episode. We use a learning rate of 10−3 and train the model using the Adam optimiser [89] for up to 200
epochs, holding aside 10% of data for early stopping.
Given that the input is a temporal sequence, a recurrent neural network (that was designed to model temporal
dynamics) is a natural choice of baseline. But we found that the LSTM performs only slightly better than the
MLP on Seek Whence tasks, and worse on the other tasks. The reason for this is that the paucity of data (a single
temporal sequence consisting of a small number of time-steps) does not provide enough information for the high
capacity LSTM to learn desirable gating behaviour. The simpler and more constrained MLP with fewer weights is
able to do slightly better on some of the tasks, yet both neural baselines achieve low accuracy in absolute terms.
Figure 7 shows the results. Clearly, the tasks are very challenging for all four baseline systems.
5.2.2. Our system handles retrodiction and imputation just as easily as prediction
To evaluate whether our system is just as capable of retrodicting earlier values and imputing missing intermediate
values as it is at predicting future values, we ran tests where the unseen hidden sensor values were at the ﬁrst time
step (in the case of retrodiction) or randomly scattered through the time-series (in the case of imputation).32 We
made sure that the number of hidden sensor values was the same for prediction, retrodiction, and imputation.
32A deterministic transition dynamic is a function from a set of ground atoms to a set of ground atoms. If this function is not injective, then
information is lost as we go through time: there will be a unique next step from the current time-step, but there can be multiple previous steps
that transition into the current time-step. Our search procedure uses maximum a posteriori (MAP) estimation: we ﬁnd a single model with the
highest posterior (based on the likelihood – how well it explains the sequence, and on the prior – the program length), and use that model to
predict, retrodict, and impute. A more ambitious Bayesian approach would construct a probability distribution over rival theories, and use a
mixture model for retrodiction. But, given the computation complexity of ﬁnding a single solution (see Section 4.4), this ambitious approach is
– in the short term at least – prohibitively expensive.
40


## Page 41


eca
music
Seek-Whence
40
60
80
100
predictive accuracy
prediction
retrodiction
imputation
Figure 8: Comparing prediction with retrodiction and imputation. In retrodiction, we display accuracy on the held-out initial time-step. In
imputation, a random subset of atoms are held-out; the held-out atoms are scattered throughout the time-series. In other words, there may be
diﬀerent held-out atoms at diﬀerent times. The number of held-out atoms in imputation matches the number of held-out atoms in prediction
and retrodiction.
Figure 8 shows the results. The results are signiﬁcantly lower for retrodiction in the ECA tasks, but otherwise
comparable. The reason for retrodiction’s lower performance on ECA is that for a particular initial conﬁguration
there are a signiﬁcant number (more than 50%) of the ECA rules that wipe out all the information in the current
state after the ﬁrst state transition, and all subsequent states then remain the same. The results for imputation are
comparable with the results for prediction. Although the results for rhythm and music are lower, the results on
Seek Whence are slightly higher.
5.2.3. The features of our system are essential to its performance.
To verify that the unity conditions are doing useful work, we performed a number of experiments in which the
various conditions were removed, and compared the results. We ran four ablation experiments. In the ﬁrst, we
removed the check that the theory’s trace covers the input sequence: S ⊑τ(θ) (see Deﬁnition 16). In the second, we
removed the check on conceptual unity. Removing this condition means that the unary predicates are no longer
connected together via exclusion relations ⊕, and the binary predicates are no longer constrained by ∃! conditions.
(See Deﬁnition 13). In the third ablation test, we removed the check on spatial unity. Removing this condition
means allowing objects which are not connected via binary relations. In the fourth ablation test, we removed the
cost minimization part of the system. Removing this minimization means that the system will return the ﬁrst
interpretation it ﬁnds, irrespective of size.
The results of the ablation experiments are displayed in Table 5. The ﬁrst ablation test, where we remove the check
that the generated sequence of sets of ground atoms respects the original sensory sequence (S ⊑τ(θ)), performs
very poorly. Of course, if the generated sequence does not cover the given part of the sensory sequence, it is highly
unlikely to accurately predict the held-out part of the sensory sequence. This test is just a sanity check that our
evaluation scripts are working as intended.
41


## Page 42


ECA
Rhythm & Music
Seek Whence
Full system (AE)
97.3%
73.3%
76.7%
No check that S ⊑τ(θ)
5.1%
3.0%
4.6%
No conceptual unity
5.3%
0.0%
6.7%
No spatial unity
95.7%
73.3%
73.3%
No cost minimization
96.7%
56.6%
73.3%
Table 5: Ablation experiments. We display predictive accuracy on the ﬁnal held-out time-step.
The second ablation test, where we remove the check on conceptual unity, also performs poorly. The reason is that
without constraints, there are no incompossible atoms. Recall from Deﬁnition 9 that two atoms are incompossible
if there is some ⊕constraint or some ∃! constraint that means the two atoms cannot be simultaneously true. But
in Deﬁnition 9, the frame axiom forces an atom that was true at the previous time-step to also be true at the next
time-step unless the old atom is incompossible with some new atom: we add α to Ht if α is in Ht−1 and there is
no atom in Ht that is incompossible with α. But if there are no incompossible atoms, then all previous atoms are
always added. Therefore, if there are no ⊕and ∃! constraints, then the set of true atoms monotonically increases
over time. This in turn means that state information becomes meaningless, as once something becomes true, it
remains always true, and cannot be used to convey information.
When we remove the spatial unity constraint, the results for the rhythm tasks are identical, but the results for the
ECA and Seek Whence tasks are lower. The reason why the results are identical for the rhythm tasks is because the
background knowledge provided (the r relation on notes, see Section 5.1.3) means that the spatial unity constraint is
guaranteed to be satisﬁed. The reason why the results are lower for ECA tasks is because interpretations that fail to
satisfy spatial unity contain disconnected clusters of cells (e.g. cells {c1, ..., c5} are connected by r in one cluster, while
cells {c6, ..., c11} are connected in another cluster, but {c1, ..., c5} and {c6, ..., c11} are disconnected). Interpretations with
disconnected clusters tend to generalize poorly and hence predict with less accuracy. The reason why the results
are only slightly lower for the Seek Whence tasks is because the lowest cost uniﬁed interpretation for most of these
tasks also happens to satisfy spatial unity.
The results for the fourth ablation test, where we remove the cost minimization, are broadly comparable with the
full system in ECA and Seek Whence, but are markedly worse in the rhythm / music tasks. But even if the results
were comparable in all tasks, there are independent reasons to want to minimize the size of the interpretation.
Shorter interpretations are more human-readable, and transfer better to new situations (since they tend to be more
general, as they have fewer atoms in the bodies of the rules).
42


## Page 43


2
4
6
8
10
0
1,000
2,000
3,000
4,000
5,000
6,000
7,000
Number of cells in the ECA
Grounding size (in megabytes)
ILASP
Our system
Figure 9: Comparing our system and ILASP w.r.t. grounding size
5.2.4. Our system outperforms state-of-the-art inductive logic programming approaches in the ﬁve domains
In order to assess the eﬃciency of our system, we compared it to ILASP33 [95, 96, 97, 98], a state-of-the-art Inductive
Logic Programming algorithm34. Unlike traditional ILP systems that learn deﬁnite logic programs, ILASP learns
answer set programs35. ILASP is a powerful and general framework for learning answer set programs; it is able to
learn choice rules, constraints, and even preferences over answer sets [96].
ILASP is able to solve some simple apperception tasks. For example, ILASP is able to solve the task in Example 6.
But for the ECA tasks, the music and rhythm tasks, and the Seek Whence tasks, the ASP programs generated by
ILASP were not solvable because they required too much memory.
In order to understand the memory requirements of ILASP on these tasks, and to compare our system with ILASP
in a fair like-for-like manner, we looked at the size of the grounded ASP programs. Recall that both our system
and ILASP generate ASP programs that are then grounded into propositional clauses that are then passed to a SAT
solver. The grounding size determines the memory usage and is strongly correlated with solution time.
We took a sample ECA, Rule 245, and looked at the grounding size as the number of cells increased from 2 to 11.
The results are in Figure 9.
As we increase the number of cells, the grounding size of the ILASP program grows much faster than the cor-
responding Apperception Engine program. The reason for this marked diﬀerence is the diﬀerent ways the two
33We compared against ILASP rather than Metagol (another state-of-the-art inductive logic programming system [90, 91]) because (i) ILASP
is comparable in performance (it achieved slightly better results than Metagol in the Inductive General Game Playing task suite [92], getting
40% correct as opposed to Metagol’s 36%), and (ii) since ILASP also uses ASP we can compare the grounding size of our program with ILASP
and get a fair apples-for-apples comparison. We used ILASP rather than HEXMIL (the ASP implementation of Metagol [93]) because of scaling
problems with HEXMIL [94]. Our decision to use ILASP rather than Metagol for these tests was based on a number of discussions with Andrew
Cropper (the developer of Metagol) and Mark Law (the developer of ILASP). We are very grateful to both for their advice on this.
34Strictly speaking, ILASP is a family of algorithms, rather than a single algorithm. We used ILASP2 [96] in this evaluation.
35Answer set programming under the stable model semantics is distinguished from traditional logic programming in that it is purely
declarative and each program has multiple solutions (known as answer sets).
Because of its non-monotonicity, ASP is well suited for
knowledge representation and common-sense reasoning [99, 100].
43


## Page 44


approaches represent rules. In our system, rules are interpreted by an interpreter that operates on reiﬁed repre-
sentations of rules. In ILASP, by contrast, rules are compiled into ASP rules. This means, if there are |Uφ| unground
atoms and there are at most NB atoms in the body of a rule, then ILASP will generate |Uφ|NB+1 diﬀerent clauses.
When it comes to grounding, if there are |Σφ| substitutions and t time-steps, then ILASP will generate at most
|Uφ|NB+1 · |Σφ| · t ground instances of the generated clauses. Each ground instance will contain NB + 1 atoms, so
there are (NB + 1) · |Uφ|NB+1 · |Σφ| · t ground atoms in total.
Compare this with our system. Here, we do not represent every possible rule explicitly as a separate clause. Rather,
we represent the possible atoms in the body of a rule by an ASP choice rule:
0 { rule_body(R, VA) : is_unground_atom(VA) } k_max_body :- is_rule(R).
If there are N→static rules and N⊃−causal rules, then this choice rule only generates N→+ N⊃−ground clauses, each
containing |Uφ| atoms.
The most expensive clauses in our encoding are analysed in Table 3. Recall from Section 4.4 that the total number
of atoms in the ground clauses is approximately 5 · |Σφ| · (N→+ N⊃−) · |Uφ| · t.
To compare this with ILASP, let us set NB = 4 (which is representative). Then ILASP generates ground clauses with
5 · |Uφ|5 · |Σφ| · t ground atoms while our system generates clauses with 5 · |Σφ| · (N→+ N⊃−) · |Uφ| · t ground atoms.
The reason, then, why our system has such lower grounding sizes than ILASP is because (N→+ N⊃−) << |Uφ|4.
Intuitively, the key diﬀerence is that ILASP considers every possible subset of the hypothesis space, while our system
(by restricting to at most N→+ N⊃−rules) only considers subsets of length at most N→+ N⊃−.
6. Noisy apperception
So far, we have assumed that our sensor readings are entirely noise-free: some of the sensory readings may be
missing, but none of the readings are inaccurate.
If we give the Apperception Engine a sensory sequence with mislabeled data, it will struggle to provide a theoretical
explanation of the mislabeled input. Consider, for example, S1:20:
S1 = {p(a)}
S2 = {p(a)}
S3 = {q(a)}
S4 = {p(a)}
S5 = {p(a)}
S6 = {p(a)}
S7 = {p(a)}
S8 = {p(a)}
S9 = {p(a)}
S10 = {p(a)}
S11 = {p(a)}
S12 = {p(a)}
S13 = {p(a)}
S14 = {p(a)}
S15 = {p(a)}
S16 = {p(a)}
S17 = {p(a)}
S18 = {p(a)}
S19 = {p(a)}
S20 = {p(a)}
Here, S3 = {q(a)} is an outlier in the otherwise tediously predictable sequence.
If we give sequences such as this to the Apperception Engine, it attempts to make sense of all the input, including
44


## Page 45


the anomalies. In this case, it ﬁnds the following baroque explanation:
I =

p(a)
c1(a)

R =

q(X) →c3(X)
c3(X) ⊃−p(X)
c1(X) ⊃−c2(X)
c2(X) ⊃−q(X)

C′ =

∀X:s, p(X) ⊕q(X)
∀X:s, c1(X) ⊕c2(X) ⊕c3(X)

Here, the Apperception Engine has introduced three new invented predicates c1, c2, c3 in order to count how many
p’s it has seen, so that it knows when to switch to q. If we move the anomalous entry q(a) later in the sequence, or add
further anomalies, the engine is forced to construct increasingly complex theories. This is clearly unsatisfactory.
In order to handle noisy mislabeled data, we shall relax our insistence that the sequence S1:T is entirely covered by
the trace of the theory θ. Instead of insisting that S ⊑τ(θ), we shall minimise the number of discrepancies between
each Si and τ(θ)i, for i = 1..T.
We want to ﬁnd the most probable theory θ given our noisy input sequence S1:T:
arg max
θ
p (θ | S1:T)
(1)
By Bayes’ rule, this is equivalent to
arg max
θ
p(θ) · p (S1:T | θ)
p(S1:T)
(2)
Since the denominator does not depend on θ, this is equivalent to:
arg max
θ
p(θ) · p (S1:T | θ)
(3)
Since the probability of the state Si is conditionally independent of the previous state Si−1 given θ (this is the
assumption behind the Hidden Markov Model), the above is equivalent to:
arg max
θ
p(θ) ·
T
Y
i=1
p (Si | θ)
(4)
Now each Si depends only on τ(θ)i, the trace of θ at time step i. Thus we can rewrite to:
arg max
θ
p(θ) ·
T
Y
i=1
p (Si | τ(θ)i)
(5)
Since we assume a universal distribution on theories, the probability of θ is 2−len(θ). Let the probability of Si given
τ(θ)i be p (Si | τ(θ)i) = 2−|Si−τ(θ)i|. Then we can rewrite to:
arg max
θ
2−len(θ) ·
T
Y
i=1
2−|Si−τ(θ)i|
(6)
45


## Page 46


Thus, we deﬁne the costnoise of the theory to be:
costnoise = len(θ) + β
T
X
i=1
|Si −τ(θ)i|
(7)
and search for the theory with lowest cost.
Example 12. Consider, for example, the following sequence S1:10:
S1 = {}
S2 = {oﬀ(a), on(b)}
S3 = {on(a), oﬀ(b)}
S4 = {on(a), on(b)}
S5 = {on(b)}
S6 = {on(a), oﬀ(b)}
S7 = {on(a), on(b)}
S8 = {oﬀ(a), on(b)}
S9 = {on(a)}
S10 = {}
Because the sequence is so short, the lowest costnoise theory is:
I =


R =


C′ =

∀X:s, on(X) ⊕oﬀ(X)

This degenerate empty theory has cost 14 (the number of atoms in S) which is shorter than any “proper” explanation
that captures the regularities. But as the sequence gets longer, the advantage of a “proper” explanation over a
degenerate solution becomes more and more apparent. Consider, for example, the following extension S′
1:30:
S′
1 = {}
S′
2 = {oﬀ(a), on(b)}
S′
3 = {on(a), oﬀ(b)}
S′
4 = {on(a), on(b)}
S′
5 = {on(b)}
S′
6 = {on(a), oﬀ(b)}
S′
7 = {on(a), on(b)}
S′
8 = {oﬀ(a), on(b)}
S′
9 = {on(a)}
S′
10 = {}
S′
11 = {oﬀ(a), on(b)}
S′
12 = {on(a), oﬀ(b)}
S′
13 = {on(a), on(b)}
S′
14 = {oﬀ(a), on(b)}
S′
15 = {on(a), oﬀ(b)}
S′
16 = {on(a), on(b)}
S′
17 = {oﬀ(a), on(b)}
S′
18 = {on(a), oﬀ(b)}
S′
19 = {on(a), on(b)}
S′
20 = {oﬀ(a), on(b)}
S′
21 = {on(a), oﬀ(b)}
S′
22 = {on(a), on(b)}
S′
23 = {oﬀ(a), on(b)}
S′
24 = {on(a), oﬀ(b)}
S′
25 = {on(a), on(b)}
S′
26 = {oﬀ(a), on(b)}
S′
27 = {on(a), oﬀ(b)}
S′
28 = {on(a), on(b)}
S′
29 = {oﬀ(a), on(b)}
S′
30 = {}
Now the lowest costnoise theory is one that ﬁnds the underlying regularity:
I =

on(a)
p1(a)
p2(b)

R =

oﬀ(X) →p3(X)
p2(X) →on(X)
p1(X) ⊃−oﬀ(X)
p3(X) ⊃−p2(X)
p2(X) ⊃−p1(X)

C′ =

∀X:s, on(X) ⊕oﬀ(X)
∀X:s, p1(X) ⊕p2(X) ⊕p3(X)

We can see, then, that the noise-robust version of the Apperception Engine is somewhat less data-eﬃcient than the
noise-intolerant version described earlier.
◁
6.1. Experiments
We used the following sequences to compare the noise-intolerant Apperception Engine with the noise-robust
version:
46


## Page 47


0
10
20
30
40
50
0
0.25
0.5
0.75
1
Length
Accuracy
noise-intolerant
noise-robust
Figure 10: Comparing the data-eﬃciency of the noise-robust version of the Apperception Engine with the noise-intolerant version. We plot
mean percentage accuracy against length of the sequence. The noise-intolerant version achieves 100% accuracy when the sequence is length 10
or over, while the noise-robust version only achieves this level of accuracy when the length is over 30.
a,b,a,b,a,b,a,b,a,b,a,b, ...
a,a,b,a,a,b,a,a,b,a,a,b, ...
a,a,b,b,a,a,b,b,a,a,b,b, ...
a,a,a,b,a,a,a,b,a,a,a,b, ...
a,b,b,a,a,b,b,a,a,b,b,a, ...
a,b,c,a,b,c,a,b,c,a,b,c, ...
a,b,c,b,a,a,b,c,b,a,a,b,c,b,a, ...
a,b,a,c,a,b,a,c,a,b,a,c, ...
a,b,c,c,a,b,c,c,a,b,c,c, ...
a,a,b,b,c,c,a,a,b,b,c,c, ...
We chose these particular sequences because they are simple, noise-free, and the Apperception Engine is able to
solve them in a reasonably short time.
We performed two groups of experiments. In the ﬁrst, we evaluated how much longer the sequence needs to be
for the noise-robust version to capture the underlying regularity, in comparison with the noise-intolerant version
which is more data-eﬃcient.
Figure 10 shows the results.
We plot mean percentage accuracy (over the ten
sequences) against the length of the sequence that is provided to the Apperception Engine. Note that the noise-
intolerant version only needs sequences of length 10 to achieve 100% accuracy, while the noise-tolerant version
needs sequences of length 30.
In the second experiment, we evaluate how much better the noise-robust version of the Apperception Engine is
at handling mislabeled data. We take the same ten sequences above, extended to length 100, and consider various
perturbations of the sequence where we randomly mislabel a certain number of entries. Figure 11 shows the
results. We plot mean percentage accuracy (over the ten sequences) against the percentage of mislabellings. Note
that the noise-intolerant version deteriorates to random as soon as any noise is introduced, while the noise-robust
version is able to maintain reasonable accuracy with up to 30% of the sequence mislabeled.
47


## Page 48


0
10
20
30
40
50
0
0.25
0.5
0.75
1
Percentage of mislabelled data
Accuracy
noise-intolerant
noise-robust
Figure 11: Comparing the accuracy of the noise-robust version of the Apperception Engine with the noise-intolerant version. We plot mean
percentage accuracy against the number of mislabellings. The noise-intolerant version deteriorates to random as soon as any noise is introduced,
while the noise-robust version is able to maintain reasonable (88%) accuracy with up to 30% of the sequence mislabelled.
7. Related work
In this section, we describe particular systems that are related to our approach. For a general overview of the space
of diﬀerent approaches, see Section 1.1.
7.1. “Theory learning as stochastic search in a language of thought”
Ullman et al [66, 67] describe a system for learning ﬁrst-order rules from symbolic data. Recasting their approach
into our notation, their system is given as input a set S of ground atoms36, and it searches for a set of static rules R
and a set I of atoms such that R, I |= S.
Of course, the task as just formulated admits of entirely trivial solutions: for example, let I = S and R = {}. Ullman
et al rule out such trivial solutions by adding two restrictions. First, they distinguish between two disjoint sets
of predicates: the surface predicates are the predicates that appear in the input S, while the core predicates are the
latent predicates. Only core predicates are allowed to appear in the initial conditions I. This distinction rules out
the trivial solution above, but there are other degenerate solutions: for each surface predicate p, add a new core
predicate pc. If p(k1, ..., kn) is in S, add pc(k1, ..., kn) to I. Also, add the rule p(X1, ..., Xn) ←pc(X1, .., Xn) to R. Clearly,
R, I |= S but this solution is unilluminating, to say the least. To prevent such degenerate solutions, the second
restriction that Ullman et al add is to prefer shorter rule-sets R and smaller sets I of initial atoms. The idea is that
if S contains structural regularities, their system will ﬁnd an R and I that are much simpler than the degenerate
solution above.
Consider, for example, the various surface relations in a family tree: John is the father of William; William is the
husband of Anne; Anne is the mother of Judith; John is the grandfather of Judith. All the various surface relations
36Compare with our system, which is given a sequence (S1, ..., ST) of sets of ground atoms.
48


## Page 49


(father, mother, husband, grandfather...)
can be explained by a small number of core relations: parent(X, Y),
spouse(X, Y), male(X), and female(X). Now the surface facts S = {father(john, william), ...} can be explained by a small
number of facts involving core predicates I = {parent(john, william), male(john), ...} together with rules such as:
father(X, Y) ←parent(X, Y), male(X)
At the computational level, then, the task that Ullman et al set out to solve is: given a set S of ground atoms
featuring surface predicates, ﬁnd the smallest set I of ground atoms featuring only core predicates, and the smallest
set R of static rules, such that R, I |= S. Recasting this task in the language of probability, they wish to ﬁnd:
arg max
R,I
p(R, I | S)
Using Bayes’ rule this can be recast as:
arg max
R,I
p(R, I | S)
=
arg max
R,I
p(S | R, I)p(R, I)
p(S)
=
arg max
R,I
p(S | R, I)p(R, I)
=
arg max
R,I
p(S | R, I)p(R)p(I | R)
Here, the likelihood p(S | R, I) is the proportion of S that is entailed by R and I, the prior p(R) is the size of the rules,
and p(I | R) is the size of I.
At the algorithmic level, Ullman et al apply Markov Chain Monte Carlo (MCMC). MCMC is a stochastic search
procedure. When it is currently considering search element x, it generates a candidate next element x′ by randomly
perturbing x. Then it compares the scores of x and x′. If x′ is better, it switches attention to focus on x′. Otherwise,
if x′ is worse than x, there is still a non-zero probability of switching (to avoid local minima), but the probability is
lower when x’ is signiﬁcantly worse than the current search element x.
In their algorithm, MCMC is applied at two levels. At the ﬁrst level, a set R of rules is perturbed into R′ by adding
or removing atoms from clauses, or by switching one predicate for another predicate with the same arity. At the
second level, I is perturbed into I′ by changing the extension of the core predicates.
Given that the search space of sets of rules is so enormous, and that MCMC is a stochastic search procedure that
only operates locally, the algorithm needs additional guidance to ﬁnd solutions. In their case, they provide a
template, a set of meta-rules that constrain the types of rules that are generated in the outermost MCMC loop. A
meta-rule is a higher-order clause in which the predicates are themselves variables. For example, in the following
meta-rule for transitivity, P is a variable ranging over two-place predicates:
P(X, Y) ←P(X, Z), P(Z, Y)
Meta-rules are a key component in many logic program synthesis systems [90, 101, 102, 95, 98].
49


## Page 50


Ullman et al tested their system in a number of domains including taxonomy hierarchies, simpliﬁed magnetic
theories, kinship relations, and psychological explanations of action. In each domain, their system is able to learn
human-interpretable theories from small amounts of data.
At a high level, Ullman et al’s system has much in common with the Apperception Engine. They are both systems
for generating interpretable explanations from small quantities of symbolic data. While the Apperception Engine
generates a (φ, I, R, C) tuple from a sequence (S1, ..., ST), their system generates an (I, R) pair from a single set S
of atoms. But there are a number of signiﬁcant diﬀerences. First, our system takes as input a sequence (S1, ..., ST)
while their system considers only a single state S. Because they do not model facts changing over time, their
system only needs to represent static rules and does not need to also represent causal rules. Second, a uniﬁed
interpretation θ = (φ, I, R, C) in our system includes a set C of constraints. These constraints play a critical role in
our system: they are both regulative (ruling out certain incompossible combinations of atoms) and constitutive
(the constraints determine the incompossible relation that in turn grounds the frame axiom). There is no equivalent
of our constraints C in their system. A third key diﬀerence is that our system has to produce a theory that, as
well as explaining the sensory sequence, also has to satisfy the unity conditions: spatial unity, conceptual unity,
static unity, and temporal unity. There is no analog of our unity conditions in Ullman et al’s system. Fourth,
their system requires hand-engineered templates in order to ﬁnd a theory that explains the input. This reliance on
hand-engineered templates restricts the domain of application of their technique: in a domain in which they do
not know, in advance, the structure of the rules they want to learn, their system will not be applicable. Fifth, our
system posits latent objects as well as latent predicates, while their system only posits latent predicates. The ability
to imagine unobserved objects, with unobserved attributes that explain the observed attributes of observed objects,
is a key feature of the Apperception Engine.
At the algorithmic level, the systems are very diﬀerent. While we use a form of meta-interpretive learning (see
Section 4.2), they use MCMC. Our system compiles an apperception problem into the task of ﬁnding an answer set
to an ASP program that minimises the program cost. The ASP problem is given to an ASP solver, that is guaranteed
to ﬁnd the global minimum. MCMC, by contrast, is a stochastic procedure that operates locally (moving from one
single point in program space to another), and is not guaranteed to (in fact, in practice, it rarely does) ﬁnd a global
minimum.
7.2. “Learning from interpretation transition”
Inoue, Ribeiro, and Sakama [12] describe a system (LFIT) for learning logic programs from sequences of sets of
ground atoms. Since their task deﬁnition is broadly similar to ours, we focus on speciﬁc diﬀerences. In our
formulation of the apperception task, we must construct a (φ, I, R, C) tuple from a sequence (S1, ..., ST) of sets of
ground atoms. In their task formulation, they learn a set of causal rules from a set {(Ai, Bi)}N
i=1 of pairs of sets of
ground atoms.
In some respects, their task formulation is more general than ours. First, their input {(Ai, Bi)}N
i=1 can represent tran-
sitions from multiple trajectories, rather than just a single trajectory, and corresponds to a generalized apperception
50


## Page 51


task (see Deﬁnition 19). Second, they learn normal logic programs, allowing negation as failure in the body of a
rule, while our system only learns deﬁnite clauses.
But there are a number of other ways in which our task formulation is signiﬁcantly more general than LFIT. First,
our system posits latent information to explain the observed sequence, while LFIT does not construct any latent
information. Their system searches for a program P that generates exactly the output state. In our approach, by
contrast, we search for a program whose trace covers the output sequence, but does not need to be identical to it.
The trace of a uniﬁed interpretation typically contains much extra information that is not part of the original input
sequence, but that is used to explain the input information.
Second, our system abduces a set of initial conditions as well as a set of rules, while LFIT does not construct
initial conditions. Because of this, our system is able to predict the future, retrodict the past, and impute missing
intermediate values. LFIT, by contrast, can only be used to predict future values.
Third, our system generates a set of constraints as well as rules. The constraints perform double duty: on the one
hand, they restrict the sets of compossible atoms that can appear in traces; on the other hand, they generate the
incompossibility relation that grounds the frame axiom. Note that there is no frame axiom in LFIT.
In [12], Inoue et al use a bottom-up synthesis method to learn rules. Given a state transition (A, B) in E, they
construct a normal ground rule for each β ∈B:
^
α∈A
α ∧
^
α∈G−A
not α ⊃−β
Then, they use resolution to generalize the individual ground rules. It is important to note that this strategy is
quite conservative in the generalizations it performs, since it only produces a more general rule if it turns out to
be a resolvent of a pair of previous rules. While the Apperception Engine searches for the shortest (and hence
most general) rules, LFIT searches for the most speciﬁc generalization. In more recent work [103], LFIT has been
changed to perform top-down specialization, rather than bottom-up generalization. With this change, LFIT is
guaranteed to ﬁnd the shortest set of rules that explain the transitions.
LFIT was tested on Boolean networks and on Elementary Cellular Automata. It is instructive to compare our
system with LFIT on the ECA tasks. When LFIT is applied to the ECA task, it is provided with the one-dimensional
spatial relation between the cells as background knowledge. In our approach, by contrast, we do not hand-code
the spatial relation, but rather let the Apperception Engine generate the spatial relation itself as part of the initial
conditions. (See Section 5.1.2). It is precisely because our system is able to posit latent information to explain the
surface features that it is able to generate the spatial relation itself, rather than having to be given it.
In some situations, positing latent information allow us to constructer a simpler theory. In other situations, however,
positing latent information is absolutely essential to making sense of the sequence. There are many apperception
tasks for which every interpretation that makes sense of the sequence must include latent information: consider, for
example, learning the dynamics of the ECA without spatial information (Section 5.1.2), the Seek Whence sequences
(Section 5.1.4), or the binding tasks (Section 5.1.6). Even the following simple example shows the unavoidable
need to posit latent information:
51


## Page 52


Example 13. Consider the task (S, φ, C) where S = (S1, S2, S3, ..., Sn), S1 = S2 = {p(a)}, and S3 = S4 = ... = Sn = {q(a)}.
Here, φ contains one type t, one object a of type t, two unary predicates p and q, and one constraint ∀X : t, p(X)⊕q(X).
Since p and q are incompatible, the transition from p to q from state S2 to S3 must be explained by a causal rule
φ ⊃−q(X), where φ is a set of atoms. Now φ cannot be empty, or the rule would be unsafe, φ cannot be {p(X)}, or
else q(a) would be derivable at the second time-step, contradicting S2 = {p(a)}. Similarly, φ cannot be {q(X)}, or else
q(a) would not be derivable at time-step 3. Hence φ must contain an atom featuring a predicate distinct from p or
q. Hence, every interpretation that makes sense of S must invoke latent information.
One of the theories found by the Apperception Engine for this is θ = (φ, I, R, C), where:
I =

p(a)
r(a)

R =

r(X) ⊃−s(X)
p(X) ∧s(X) ⊃−q(X)

C =

∀X:t, p(X) ⊕q(X)
∀X:t, r(X) ⊕s(X)

Here, there are two latent predicates, r and s, that are used as counters, so the system can distinguish between the
two occurrences of p(a) in S1 and S2. Thus for some sequences, the positing of latent predicates, and the abduction
of initial conditions for the latent atoms, is unavoidable.
◁
LFIT has been extended in a number of ways, to increase the range of real-world problems that it can tackle. In
[104], LFIT was extended to learn probabilistic models. In [105], the system was extended from the Markov(1)
assumption (where the new state depends only on the current state) to the more general Markov(k) setting (where
the new state depends on the last k states).
In [106], LFIT was generalised so that as well as working with
deterministic models (where all state transitions happen simultaneously), it also can work with other semantics
(where only a subset of the transitions may happen at each time-step). In [107], LFIT was extended to work directly
with continuous sensor data, rather than assuming the continuous sensor data has ﬁrst been discretised by some
other process. In [108, 109], LFIT was reimplemented in a feed-forward neural network, so as to robustly handle
noisy and continuous data.
7.3. “Unsupervised learning by program synthesis”
Ellis et al [22] use program synthesis to solve an unsupervised learning problem. Given an unlabeled dataset
{xi}N
i=1, they ﬁnd a program f and a set of inputs {Ii}N
i=1 such that f(Ii) is close to xi for each i = 1..N. More precisely,
they use Bayesian inference to ﬁnd the f and {Ii}N
i=1 that minimizes the combined log lengths of the program, the
initial conditions, and the data-reconstruction error:
−logP f( f) +
N
X
i=1
 −logPx|z(xi | f(Ii)) −logPI(Ii)
where Pf( f) is a description length prior over programs, PI(Ii) is a description length prior over initial conditions,
and Px|z(· | zi) is a noise model. This system was designed from the outset to be robust to noise, using Bayesian
inference to calculate the desired tradeoﬀbetween the program length, the initial conditions length, and the data-
reconstruction error cost. They tested this system in two domains: reproducing two dimensional pictures, and
learning morphological rules for English verbs.
52


## Page 53


This system is similar to ours in that it produces interpretable programs from a small number of data samples.
Like ours, their program length prior acts as an inductive bias that prefers general solutions over special-case
memorized solutions. Like ours, as well as constructing a program, they also learn initial conditions that combine
with the program to produce the desired results37. At a high level, their algorithm is also similar: they generate
a Sketch program [110] from the dataset {xi}N
i=1 of examples, and use a SMT solver to ﬁll in the holes. They then
extract a readable program from the SMT solution, which they then apply to new instances, exhibiting strong
generalization.
As well as the high level architectural similarities, there are a number of important diﬀerences. First, their goal
was to generate an object f(Ii) that matches as closely as possible to the input object xi. Our goal is more general:
we seek to generate a sequence τ(θ) that covers the input sequence. The covering relation is much more general,
as Si only has to be a subset of (τ(θ))i, not identical to it. This allows the addition of latent information to the
trace of the theory. A second key diﬀerence is that we focus on generating sequences, not individual objects. Our
system is designed for making sense (unsupervisedly) of time series, sequences of states, not of reconstructing
individual objects. A third key diﬀerence is that we use a single domain-independent language, Datalog⊃−, for all
domains, while Ellis et al use a diﬀerent domain-speciﬁc imperative language for each domain they consider. A
fourth key diﬀerence is that we use a declarative language, rather than an imperative language. An individual
rule or constraint has a truth-conditional interpretation, and can be interpreted as a belief of the synthesising
agent. An individual line of an imperative procedure, by contrast, cannot be interpreted as a belief. A ﬁfth major
diﬀerence is that we synthesise constraints as well as rules. Constraints are the “special sauce” of our system:
exclusive disjunctions combine predicates into groups, enforce that each state is fully determinate, and ground the
incompossibility relation that underlies the frame axiom.
7.4. “Learning symbolic models of stochastic domains”
Pasula et al [10] describe a system for learning a state transition model from data. The model learns a probability
distribution p(s′ | s, a) where s is the previous state, a is the action that was performed and s′ is the next state.
Each state is represented as a set of ground atoms, just like in our system. They assume complete observability: they
assume they are given the value of every sensor and the task is just to predict the next values of the sensors.
They represent a state transition model by a set of “dynamic rules”: these are ﬁrst-order clauses determining the
future state given a current state and an action. These dynamic rules are very close to the causal rules in Datalog⊃−.
Unlike in our system, their rules have a probability outcome for each possible head. Note their system does not
include static rules or constraints.
In their semantics, they assume that exactly one dynamic rule ﬁres every time-step. This is a very strong assumption.
But it makes it easier to learn rules with probabilistic outcomes.
37In fact, they learn a diﬀerent set of initial conditions Ii for each data point xi. This corresponds to the generalized apperception task of
Deﬁnition 19.
53


## Page 54


They learn state transitions for the noisy gripper domain (where a robot hand is stacking bricks, and sometimes
fails to pick up what it attempts to pick up) and a logistics problem (involving trucks transporting objects from
one location to another). Impressively, they are able to learn probabilistic rules in noisy settings. They also verify
the usefulness of their learned models by passing them to a planner (a sparse sampling MDP planner), and show,
reassuringly, that the agent achieves more reward with a more accurate model.
At a strategic level, their system is similar in approach to ours. First, they learn ﬁrst-order rules, not merely
propositional ones. In fact, they show in ablation studies that learning propositional rules generalises signiﬁcantly
less well, as you would expect. Second, they use an inductive bias against constants (p.14), just as we do: “learning
action models which are restricted to be free of constants provides a useful bias that can improve generalisation
when training with small data sets”. Third, their system is able to construct new invented predicates.
But there are also a number of diﬀerences. In our system, many rules can ﬁre simultaneously. But in theirs, only one
rule can ﬁre in any state. Because of this assumption, they cannot model e.g. a cellular automaton, where each cell
has its own individual update rule ﬁring simultaneously. Another limiting assumption is that they assume they
have complete observability of all sensory predicates. This means they would not be able to solve e.g. occlusion
tasks.
7.5. “Nonmonotonic abductive inductive learning”
Ray [11] described a system, XHAIL, for jointly learning to abduce ground atoms and induce ﬁrst-order rules.
XHAIL learns normal logic programs that can include negation as failure in the body of a rule.
XHAIL is similar to the Apperception Engine in that as well as inducing general ﬁrst-order rules, it also constructs
a set of initial ground atoms. This enables it to model latent (unobserved) information, which is a very powerful
and useful feature. At the implementation level, it uses a similar strategy in that solutions are found by iterative
deepening over a series of increasingly complex ASP programs. The simpliﬁed event calculus [54] is represented
explicitly as background knowledge.
But there are also a number of key diﬀerences. First, it does not model constraints. This means it is not able
to represent the incompossibility relation between ground atoms. Also, XHAIL does not try to satisfy our other
unity conditions, such as spatial and conceptual unity. Second, the induced rules are compiled in XHAIL, rather
than being interpreted (as in our system). Representing each candidate induced rule explicitly as a separate ASP
rule means that the number of ASP rules considered grows exponentially with the size of the rule body38. Third,
XHAIL needs to be provided with a set of mode declarations to limit the search space of possible induced rules.
These mode declarations constitute a signiﬁcant piece of background knowledge. Now of course there is nothing
wrong with allowing an ILP system to take advantage of background knowledge to aid the search. But when
38It shares the same implementation strategy as ASPAL [111] and ILASP [95]. See Section 5.2.4 for discussion of the grounding problem
associated with this family of approaches. The discussion is speciﬁcally focused on ILASP, but we believe the same issue aﬀects ASPAL and
XHAIL mutatis mutandem.
54


## Page 55


an ILP system relies on this hand-engineered knowledge, then it restricts the range of applicability to domains in
which human engineers can anticipate in advance the form of the rules they want the system to learn39.
7.6. The Game Description Language and Datalog⊃−
Our language Datalog⊃−is an extension of Datalog that incorporates, as well as the standard static rules of Datalog,
both causal rules (Deﬁnition 7) and constraints (Deﬁnition 8). The semantics of Datalog⊃−are deﬁned according to
Deﬁnition 9. Unlike standard Datalog, the atoms and rules of Datalog⊃−are strongly typed (see Deﬁnitions 4, 5,
and 7).
At a high level, Datalog⊃−is related to the Game Description Language (GDL) [112]. The GDL is an extension
of Datalog that was designed to express deterministic multi-agent discrete Markov decision processes. The GDL
includes (stratiﬁed) negation by failure, as well as some (restricted) use of function symbols, but these extensions
were carefully designed to preserve the key Datalog property that a program has a unique subset-minimal Herbrand
model. The GDL includes special keywords, including init for specifying initial conditions (equivalent to the
initial conditions I in a (φ, I, R, C) theory), and next for specifying state transitions (equivalent to our causal rules).
The inductive general game playing (IGGP) task [113, 92] involves learning the rules of a game from observing traces
of play.
An IGGP task is broadly similar to an apperception task in that both involve inducing initial conditions and rules
from traces. But there are many key diﬀerences. One major feature of Datalog⊃−is the use of constraints to generate
incompossible sets of ground atoms. These exclusion constraints are needed to generate the incompossibility
relation which in turn is needed to restrict the scope of the frame axiom (see Deﬁnition 9).
The main diﬀerence between Datalog⊃−and the GDL is that the former includes exclusion constraints. The exclusion
constraints play two essential roles. First, they enable the theory as a whole to satisfy the condition of conceptual
unity. Second, they provide constraints, via the condition of static unity, on the generated trace: since the constraints
must always be satisﬁed, this restricts the rules that can be constructed. Satisfying these constraints means ﬁlling
in missing information. This is why a uniﬁed interpretation is able to make sense of incomplete traces where some
of the sensory data is missing.
7.7. Related application areas
We brieﬂy outline three related research areas where the Apperception Engine can be applied. One application
area is relational reinforcement learning [119, 120, 121]. Here, the agent works out how to optimize its reward in
an environment by constructing (using ILP) a ﬁrst-order model of the dynamics of that environment, which it then
uses to plan. Here, the Apperception Engine can be used to construct the dynamics model.
A second application area is learning game rules from player traces [122, 95]. Here, the learning system is presented
with traces (typically, sequences of sets of ground atoms), representing the state of the game at various points in
39See Appendix C of [62] for a discussion of the use of mode declarations as a language bias in ILP systems.
55


## Page 56


time, and has to learn the transition dynamics (or reward function, or action legality function) of the underlying
system.
A third related area is the predictive processing (PP) paradigm [123, 6, 7, 8], an increasingly popular model in
computational and cognitive neuroscience. Inspired by Helmholtz, the model learns to make sense of its sensory
stream by attempting to predict future percepts. When the predicted percepts diverge from the actual percepts,
the model updates its parameters to minimize prediction error. The PP model is probabilistic, Bayesian, and
hierarchical: probabilistic in that the predicted sensory readings are represented as probability density functions,
Bayesian in that the likelihood (represented by the information size of the misclassiﬁed predictions) is combined
with prior expectations [6], and hierarchical in that each layer provides predictions of sensory input for the layer
below; there are typically many layers. While PP focuses on prediction, the Apperception Engine generates an
interpretation that is equally adept at predicting future signals, retrodicting past signals, and imputing missing
intermediary signals. In our approach, the ability to predict future signals is a derived capacity, a capacity that
emerges from the more general capacity to construct a uniﬁed interpretation – but prediction is not singled out
in particular. The Apperception Engine is able to predict, retrodict, and impute – in fact, it is able to do all three
simultaneously using a single incomplete sensory sequence with elements missing at the beginning, at the end, and
in the middle.
7.8. Summary
In summary, there are various other systems that construct dynamic rules for explaining sequences. But these
systems are unable to posit latent hidden information to make sense of the sequence. These systems are able
to predict future elements of the sequence, but are not able to retrodict earlier elements, or impute missing
intermediary elements. For problems that require positing latent hidden information40, or problems that require
retrodiction and imputation as well as prediction, the Apperception Engine is particularly well suited.
8. Conclusion
This paper is an attempt to answer a key question of unsupervised learning: what does it mean to “make sense”
of a sensory sequence? Our answer is that making sense means constructing a symbolic theory containing a set
of objects that persist over time, with attributes that change over time, according to general laws. This theory
must both explain the sensory input, and satisfy the unity conditions of Section 3.3.
As well as providing a
precise formalization of this task, we also provide a concrete implementation of a system that is able to make sense
of the sensory stream. We have tested the Apperception Engine in a variety of domains; in each domain, we
tested its ability to predict future values, retrodict previous values, and impute missing intermediate values. Our
system achieves good results across the board, outperforming neural network baselines and also state-of-the-art
ILP systems.
40For example, making sense of the ECA sequences without spatial information (Section 5.1.2), or interpreting the Seek Whence sequences
(Section 5.1.4), or the binding tasks (Section 5.1.6).
56


## Page 57


Of particular note is that the Apperception Engine is able to achieve human performance on challenging sequence
induction intelligence tests. We stress, once more, that the system was not hard-coded to solve these tasks. Rather,
it is a general domain-independent sense-making system that is able to apply its general architecture to the particular
problem of Seek Whence induction tasks, and is able to solve these problems “out of the box” without human
hand-engineered help. We also stress, again, that the system did not learn to solve these sequence induction tasks
by being presented with hundreds of training examples41. Indeed, the system had never seen a single such task
before. Instead, it applied its general sense-making urge to each individual task, de novo.
Our architecture, an unsupervised program synthesis system, is a purely symbolic system, and as such, it inherits
two key advantages of ILP systems [62]. First, the interpretations produced are interpretable. Because the output is
symbolic, it can be read and veriﬁed by a human42. Second, it is very data-eﬃcient. Because of the language bias of
the Datalog⊃−language, and the strong inductive bias provided by the unity conditions, the system is able to make
sense of extremely short sequences of sensory data, without having seen any others.
However, the system in its current form has some limitations that we wish to make explicit. First, the sensory input
must be discretized before it can be passed to the system. We assume some prior system has already discretized
the continuous sensory values by grouping them into buckets. One possible approach to deal with continuous
sensory values is to combine the Apperception Engine with a neural network that maps the raw continuous inputs
into categories. We have recently developed such an extension, in which we discretize the input by simulating a
binary neural network. The binary neural network is implemented in ASP, so the weights of the network and the
rules of the theory can be found simultaneously by solving one large SAT problem.
Second, our implementation as described above assumes all causal rules are fully deterministic.
It is quite
straightforward to add non-determinism to the Datalog⊃−framework: we can deﬁne an extended theory as a
theory with initial conditions for each time-step (rather than only allowing initial conditions for the ﬁrst time-step,
as in Deﬁnition 2). An extended theory θ = (φ, {I1, ..., IT}, R, C) generates a trace τ(θ) = (A1, A2, ...) in exactly the
same way as in Deﬁnition 9, with one small exception: It ⊆At replaces I ⊆A1. In other words, new atoms can be
abduced at each time-step. This would allow us to handle non-determinism by abducing atoms that change their
truth-value according to {I1, ..., IT} instead of according to the rules in R.
Third, the size of the search space means that our system is currently restricted to small-to-medium-size problems.43
Going forward, we believe that the right way to build complex theories is incrementally, using curriculum learning:
the system should consolidate what it learns in one episode, storing it as background knowledge, and reusing it in
subsequent episodes.
We hope in future work to address these limitations. But we believe that, even in its current form, the Apperception
Engine shows considerable promise as a prototype of what a general-purpose domain-independent sense-making
machine must look like.
41Barrett et al [85] train a neural network to learn to solve Raven’s progressive matrices from thousands of training examples.
42Large machine-generated programs are not always easy to understand. But machine-generated symbolic programs are certainly easier to
understand than the weights of a neural network. See Muggleton et al [23] for an extensive discussion.
43This is not because our system is carelessly implemented: the Apperception Engine is able to synthesize signiﬁcantly larger programs than
state-of-the-art ILP systems (see the comparison with ILASP in Section 5.2.4).
57


## Page 58


Acknowledgements
We are very grateful to Andrew Cropper, Jessica Hamrick, Mark Law, Matko Bo˘snjak, Murray Shanahan, Nando
de Freitas, and the anonymous reviewers for extensive feedback.
References
References
[1] M. Mathieu, C. Couprie, Y. LeCun, Deep multi-scale video prediction beyond mean square error, arXiv
preprint arXiv:1511.05440.
[2] C. Finn, S. Levine, Deep visual foresight for planning robot motion, in: IEEE International Conference on
Robotics and Automation (ICRA), IEEE, 2017, pp. 2786–2793.
[3] T. Weber, S. Racani`ere, D. P. Reichert, L. Buesing, A. Guez, D. J. Rezende, A. P. Badia, O. Vinyals, N. Heess,
Y. Li, et al., Imagination-augmented agents for deep reinforcement learning, arXiv preprint arXiv:1707.06203.
[4] Z. Liu, R. A. Yeh, X. Tang, Y. Liu, A. Agarwala, Video frame synthesis using deep voxel ﬂow., in: ICCV, 2017,
pp. 4473–4481.
[5] L. Buesing, T. Weber, S. Racaniere, S. Eslami, D. Rezende, D. P. Reichert, F. Viola, F. Besse, K. Gregor,
D. Hassabis, et al., Learning and querying fast generative models for reinforcement learning, arXiv preprint
arXiv:1802.03006.
[6] K. Friston, The history of the future of the Bayesian brain, NeuroImage 62 (2) (2012) 1230–1233.
[7] A. Clark, Whatever next? Predictive brains, situated agents, and the future of cognitive science, Behavioral
and Brain Sciences 36 (3) (2013) 181–204.
[8] L. R. Swanson, The predictive processing paradigm has roots in Kant, Frontiers in Systems Neuroscience 10
(2016) 79.
[9] J. B. Tenenbaum, T. L. Griﬃths, C. Kemp, Theory-based bayesian models of inductive learning and reasoning,
Trends in cognitive sciences 10 (7) (2006) 309–318.
[10] H. M. Pasula, L. S. Zettlemoyer, L. P. Kaelbling, Learning symbolic models of stochastic domains, Journal of
Artiﬁcial Intelligence Research (JAIR) 29 (2007) 309–352.
[11] O. Ray, Nonmonotonic abductive inductive learning, Journal of Applied Logic 7 (3) (2009) 329–340.
[12] K. Inoue, T. Ribeiro, C. Sakama, Learning from interpretation transition, Machine Learning 94 (1) (2014)
51–79.
[13] E. S. Spelke, K. D. Kinzler, Core knowledge, Developmental Science 10 (1) (2007) 89–96.
[14] C. Diuk, A. Cohen, M. L. Littman, An object-oriented representation for eﬃcient reinforcement learning, in:
Proceedings of the 25th international conference on Machine learning, 2008, pp. 240–247.
[15] G. Marcus, E. Davis, Rebooting AI, Pantheon, 2019.
[16] B. M. Lake, T. D. Ullman, J. B. Tenenbaum, S. J. Gershman, Building machines that learn and think like
people, Behavioral and Brain Sciences 40.
58


## Page 59


[17] J. McCarthy, Challenges to machine learning: Relations between reality and appearance, in: International
Conference on Inductive Logic Programming, Springer, 2006, pp. 2–9.
[18] K. Inoue, Meta-level abduction., FLAP 3 (1) (2016) 7–36.
[19] T. Teijeiro, P. F´elix, On the adoption of abductive reasoning for time series interpretation, Artiﬁcial Intelligence
262 (2018) 163–188.
[20] G. W. Leibniz, G. W. F. von Leibniz, Leibniz: New essays on human understanding, Cambridge University
Press, 1996.
[21] J. Dewey, Leibniz’s New Essays Concerning the Human Understanding: A Critical Exposition, SC Griggs,
1888.
[22] K. Ellis, A. Solar-Lezama, J. Tenenbaum, Unsupervised learning by program synthesis, in: Advances in
Neural Information Processing Systems (NEURIPS), 2015, pp. 973–981.
[23] S. H. Muggleton, U. Schmid, C. Zeller, A. Tamaddoni-Nezhad, T. Besold, Ultra-strong machine learning:
comprehensibility of programs learned with ILP, Machine Learning 107 (7) (2018) 1119–1140.
[24] D. R. Hofstadter, Fluid Concepts and Creative Analogies, Basic Books, 1995.
[25] J. Hern´andez-Orallo, F. Mart´ınez-Plumed, U. Schmid, M. Siebers, D. L. Dowe, Computer models solving
intelligence test problems: Progress and implications, Artiﬁcial Intelligence 230 (2016) 74–107.
[26] K. J. W. Craik, The nature of explanation, Vol. 445, CUP Archive, 1967.
[27] P. L. Harris, The Work of the Imagination, Blackwell Publishers, Oxford, 2000.
[28] T. Gerstenberg, J. B. Tenenbaum, Intuitive theories, Oxford Handbook of Causal Reasoning (2017) 515–548.
[29] L. Kaiser, M. Babaeizadeh, P. Milos, Model based reinforcement learning for Atari, arXiv preprint
arXiv:1903.00374v2.
[30] D. Silver, T. Hubert, J. Schrittwieser, I. Antonoglou, M. Lai, A. Guez, M. Lanctot, L. Sifre, D. Kumaran,
T. Graepel, et al., A general reinforcement learning algorithm that masters chess, shogi, and go through
self-play, Science 362 (6419) (2018) 1140–1144.
[31] J. B. Hamrick, Analogues of mental simulation and imagination in deep learning, Current Opinion in
Behavioral Sciences 29 (2019) 8–16.
[32] L. E. Baum, T. Petrie, Statistical inference for probabilistic functions of ﬁnite state Markov chains, The Annals
of Mathematical Statistics 37 (6) (1966) 1554–1563.
[33] Z. Ghahramani, An introduction to hidden Markov models and Bayesian networks, in: Hidden Markov
models: Applications in Computer Vision, World Scientiﬁc, 2001, pp. 9–41.
[34] V. Feinberg, A. Wan, I. Stoica, M. Jordan, J. Gonzalez, S. Levine, Model-based value expansion for eﬃcient
model-free reinforcement learning, in: Proceedings of the 35th International Conference on Machine Learning
(ICML), 2018.
[35] A. Nagabandi, G. Kahn, R. S. Fearing, S. Levine, Neural network dynamics for model-based deep rein-
forcement learning with model-free ﬁne-tuning, in: 2018 IEEE International Conference on Robotics and
Automation (ICRA), IEEE, 2018, pp. 7559–7566.
[36] P. Battaglia, R. Pascanu, M. Lai, D. J. Rezende, et al., Interaction networks for learning about objects, relations
and physics, in: Advances in Neural Information Processing Systems (NEURIPS), 2016, pp. 4502–4510.
59


## Page 60


[37] M. B. Chang, T. Ullman, A. Torralba, J. B. Tenenbaum, A compositional object-based approach to learning
physical dynamics, arXiv preprint arXiv:1612.00341.
[38] D. Mrowca, C. Zhuang, E. Wang, N. Haber, L. F. Fei-Fei, J. Tenenbaum, D. L. Yamins, Flexible neural
representation for physics prediction, in: Advances in Neural Information Processing Systems (NEURIPS),
2018, pp. 8813–8824.
[39] A. Sanchez-Gonzalez, N. Heess, J. T. Springenberg, J. Merel, M. Riedmiller, R. Hadsell, P. Battaglia, Graph
networks as learnable physics engines for inference and control, arXiv preprint arXiv:1806.01242.
[40] A. Lerer, S. Gross, R. Fergus, Learning physical intuition of block towers by example, arXiv preprint
arXiv:1603.01312.
[41] A. Bhattacharyya, M. Malinowski, B. Schiele, M. Fritz, Long-term image boundary prediction, in: AAAI
Conference on Artiﬁcial Intelligence, 2018.
[42] J. Oh, X. Guo, H. Lee, R. L. Lewis, S. Singh, Action-conditional video prediction using deep networks in
Atari games, in: Advances in Neural Information Processing Systems (NEURIPS), 2015, pp. 2863–2871.
[43] S. Chiappa, S. Racaniere, D. Wierstra, S. Mohamed, Recurrent environment simulators, arXiv preprint
arXiv:1704.02254.
[44] D. Ha, J. Schmidhuber, Recurrent world models facilitate policy evolution, in: Advances in Neural Informa-
tion Processing Systems (NEURIPS), 2018, pp. 2455–2467.
[45] M. Janner, S. Levine, W. T. Freeman, J. B. Tenenbaum, C. Finn, J. Wu, Reasoning about physical interactions
with object-oriented prediction and planning, arXiv preprint arXiv:1812.10972.
[46] A. Zhang, A. Lerer, S. Sukhbaatar, R. Fergus, A. Szlam, Composable planning with attributes, Proceedings
of the International Conference on Machine Learning (ICML).
[47] Z. Xu, Z. Liu, C. Sun, K. Murphy, W. Freeman, J. Tennenbaum, J. Wu, Unsupervised discovery of parts,
structure, and dynamics, in: Proceedings of the International Conference on Learning Representations
(ICLR), 2019, pp. 1418–1424.
[48] M. Asai, A. Fukunaga, Classical planning in deep latent space: Bridging the subsymbolic-symbolic boundary,
in: AAAI Conference on Artiﬁcial Intelligence, 2018.
[49] M. Asai, Unsupervised grounding of plannable ﬁrst-order logic representation from images, arXiv preprint
arXiv:1902.08093.
[50] N. Katzouris, A. Artikis, G. Paliouras, Incremental learning of event deﬁnitions with inductive logic pro-
gramming, Machine Learning 100 (2-3) (2015) 555–585.
[51] E. Michelioudakis, A. Skarlatidis, G. Paliouras, A. Artikis, Online structure learning using background
knowledge axiomatization, in: Joint European Conference on Machine Learning and Knowledge Discovery
in Databases, Springer, 2016, pp. 232–247.
[52] N. Katzouris, A. Artikis, G. Paliouras, Online learning of event deﬁnitions, Theory and Practice of Logic
Programming 16 (5-6) (2016) 817–833.
[53] E. Michelioudakis, A. Artikis, G. Paliouras, Semi-supervised online structure learning for composite event
recognition, arXiv preprint arXiv:1803.00546.
[54] R. Kowalski, M. Sergot, A logic-based calculus of events, New Generation Computing 4 (1) (1986) 67–96.
60


## Page 61


[55] R. Kowalski, Predicate logic as programming language, in: IFIP congress, Vol. 74, 1974, pp. 569–544.
[56] K. R. Apt, Logic programming, Handbook of Theoretical Computer Science, Volume B: Formal Models and
Sematics (B) 1990 (1990) 493–574.
[57] J. W. Lloyd, Foundations of Logic Programming, Springer Science & Business Media, 2012.
[58] M. H. Van Emden, R. A. Kowalski, The semantics of predicate logic as a programming language, Journal of
the ACM (JACM) 23 (4) (1976) 733–742.
[59] M. Gelfond, V. Lifschitz, The stable model semantics for logic programming., in: Logic Programming: Proc.
Fifth International Conference on Logic Programming, Vol. 88, MIT Press, 1988, pp. 1070–1080.
[60] F. Calimeri, W. Faber, M. Gebser, G. Ianni, R. Kaminski, T. Krennwallner, N. Leone, F. Ricca, T. Schaub,
Asp-core-2: Input language format, ASP Standardization Working Group.
[61] R. Kowalski, Logic for Problem-Solving, Elsevier North-Holland, 1979.
[62] R. Evans, E. Grefenstette, Learning explanatory rules from noisy data, Journal of Artiﬁcial Intelligence
Research (JAIR) 61 (2018) 1–64.
[63] C. Baral, M. Gelfond, Logic programming and knowledge representation, The Journal of Logic Programming
19 (1994) 73–148.
[64] K. L. Clark, Negation as failure, in: Logic and data bases, Springer, 1978, pp. 293–322.
[65] A. Van Gelder, K. A. Ross, J. S. Schlipf, The well-founded semantics for general logic programs, Journal of
the ACM (JACM) 38 (3) (1991) 619–649.
[66] N. D. Goodman, T. D. Ullman, J. B. Tenenbaum, Learning a theory of causality., Psychological Review 118 (1)
(2011) 110.
[67] T. D. Ullman, N. D. Goodman, J. B. Tenenbaum, Theory learning as stochastic search in the language of
thought, Cognitive Development 27 (4) (2012) 455–480.
[68] A. N. Kolmogorov, On tables of random numbers, Sankhy¯a: The Indian Journal of Statistics, Series A (1963)
369–376.
[69] L. A. Levin, Universal sequential search problems, Problemy Peredachi Informatsii 9 (3) (1973) 115–116.
[70] T. G. Dietterich, P. Domingos, L. Getoor, S. Muggleton, P. Tadepalli, Structured machine learning: the next
ten years, Machine Learning 73 (1) (2008) 3.
[71] C. Henson, A. Sheth, K. Thirunarayan, Semantic perception: Converting sensory observations to abstractions,
IEEE Internet Computing 16 (2) (2012) 26–34.
[72] M. Gebser, R. Kaminski, B. Kaufmann, T. Schaub, Clingo= ASP+ control, arXiv preprint arXiv:1405.3694.
[73] R. Ben-Eliyahu, R. Dechter, Propositional semantics for disjunctive logic programs, Annals of Mathematics
and Artiﬁcial intelligence 12 (1-2) (1994) 53–87.
[74] E. Dantsin, T. Eiter, G. Gottlob, A. Voronkov, Complexity and expressive power of logic programming, ACM
Computing Surveys (CSUR) 33 (3) (2001) 374–425.
[75] G. Brewka, I. Niemel¨a, M. Truszczynski, Answer set optimization, in: Proceedings of the International Joint
Conference on Artiﬁcial Intelligence (IJCAI), Vol. 3, 2003, pp. 867–872.
[76] M. Gebser, R. Kaminski, T. Schaub, Complex optimization in answer set programming, Theory and Practice
of Logic Programming 11 (4-5) (2011) 821–839.
61


## Page 62


[77] R. Morel, A. Cropper, L. Ong, Typed meta-interpretive learning of logic programs, in: European Conference
on Logics in Artiﬁcial Intelligence - (JELIA), 2019, pp. 973–981.
[78] M. Gebser, R. Kaminski, B. Kaufmann, T. Schaub, Answer set solving in practice, Synthesis Lectures on
Artiﬁcial Intelligence and Machine Learning 6 (3) (2012) 1–238.
[79] S. Wolfram, Statistical mechanics of cellular automata, Reviews of Modern Physics 55 (3) (1983) 601.
[80] M. Cook, Universality in elementary cellular automata, Complex Systems 15 (1) (2004) 1–40.
[81] M. Mitchell, Analogy-Making as Perception, MIT Press, 1993.
[82] L. L. Thurstone, T. G. Thurstone, Factorial studies of intelligence., Psychometric Monographs.
[83] J. Hernandez-Orallo, N. Minaya-Collado, A formal deﬁnition of intelligence, in: Proceedings of International
Symposium of Engineering of Intelligent Systems (EIS 98), 1998, pp. 146–163.
[84] M. J. E. Meredith, Seek-whence: A model of pattern perception, Tech. rep., Indiana University (USA) (1986).
[85] D. G. Barrett, F. Hill, A. Santoro, A. S. Morcos, T. Lillicrap, Measuring abstract reasoning in neural networks,
arXiv preprint arXiv:1807.04225.
[86] A. Holcombe, The binding problem, The Sage Encyclopedia of Perception.
[87] K. P. Murphy, Machine Learning: a Probabilistic Perspective, MIT press, 2012.
[88] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural Computation 9 (8) (1997) 1735–1780.
[89] D. P. Kingma, J. Ba, Adam: A method for stochastic optimization, arXiv preprint arXiv:1412.6980.
[90] S. H. Muggleton, D. Lin, A. Tamaddoni-Nezhad, Meta-interpretive learning of higher-order dyadic datalog:
predicate invention revisited, Machine Learning 100 (1) (2015) 49–73. doi:10.1007/s10994-014-5471-y.
URL https://doi.org/10.1007/s10994-014-5471-y
[91] A. Cropper, S. H. Muggleton, Learning eﬃcient logic programs, Machine Learning (2018) 1–21doi:10.1007/
s10994-018-5712-6.
URL http://dx.doi.org/10.1007/s10994-018-5712-6
[92] A. Cropper, R. Evans, M. Law, Inductive general game playing, Machine Learning (2019) 1–42.
[93] T. Kaminski, T. Eiter, K. Inoue, Exploiting answer set programming with external sources for meta-
interpretive learning, Theory and Practice of Logic Programming 18 (3-4) (2018) 571–588.
[94] A. Cropper, R. Morel, S. Muggleton, Learning higher-order logic programs, Machine Learning (2019) 1–34.
[95] M. Law, A. Russo, K. Broda, Inductive learning of answer set programs, in: European Conference on Logics
in Artiﬁcial Intelligence - (JELIA), 2014, pp. 311–325. doi:10.1007/978-3-319-11558-0_22.
URL https://doi.org/10.1007/978-3-319-11558-0_22
[96] M. Law, A. Russo, K. Broda, Learning weak constraints in answer set programming, Theory and Practice of
Logic Programming 15 (4-5) (2015) 511–525.
[97] M. Law, A. Russo, K. Broda, Iterative learning of answer set programs from context dependent examples,
Theory and Practice of Logic Programming 16 (5-6) (2016) 834–848.
[98] M. Law, A. Russo, K. Broda, The complexity and generality of learning answer set programs, Artiﬁcial
Intelligence 259 (2018) 110–146.
[99] E. T. Mueller, Commonsense Reasoning, Morgan Kaufmann, 2014.
62


## Page 63


[100] M. Gelfond, Y. Kahl, Knowledge Representation, Reasoning, and the Design of Intelligent Agents, Cambridge
University Press, 2014.
[101] A. Cropper, S. H. Muggleton, Learning higher-order logic programs through abstraction and invention, in:
Proceedings of the International Joint Conference on Artiﬁcial Intelligence (IJCAI), IJCAI/AAAI Press, 2016,
pp. 1418–1424.
URL http://www.ijcai.org/Abstract/16/204
[102] A. Cropper, Eﬃciently Learning Eﬃcient Programs, Ph.D. thesis, Imperial College London, UK (2017).
URL http://hdl.handle.net/10044/1/58488
[103] T. Ribeiro, K. Inoue, Learning prime implicant conditions from interpretation transition, in: Inductive Logic
Programming, Springer, 2015, pp. 108–125.
[104] D. Mart´ınez, G. Alenya, T. Ribeiro, C. Torras, Relational reinforcement learning for planning with exogenous
eﬀects, The Journal of Machine Learning Research 18 (1) (2017) 2689–2732.
[105] T. Ribeiro, M. Magnin, K. Inoue, C. Sakama, Learning multi-valued biological models with delayed inﬂu-
ence from time-series observations, in: 2015 IEEE 14th International Conference on Machine Learning and
Applications (ICMLA), IEEE, 2015, pp. 25–31.
[106] T. Ribeiro, M. Folschette, M. Magnin, O. Roux, K. Inoue, Learning dynamics with synchronous, asynchronous
and general semantics, in: International Conference on Inductive Logic Programming, Springer, 2018, pp.
118–140.
[107] T. Ribeiro, S. Tourret, M. Folschette, M. Magnin, D. Borzacchiello, F. Chinesta, O. Roux, K. Inoue, Inductive
learning from state transitions over continuous domains, in: International Conference on Inductive Logic
Programming, Springer, 2017, pp. 124–139.
[108] S. Tourret, E. Gentet, K. Inoue, Learning human-understandable description of dynamical systems from feed-
forward neural networks, in: International Symposium on Neural Networks, Springer, 2017, pp. 483–492.
[109] Y. Phua, T. Ribeiro, S. Tourret, K. Inoue, Learning logic program representation for delayed systems with
limited training data, 2017.
[110] A. Solar-Lezama, L. Tancau, R. Bodik, S. Seshia, V. Saraswat, Combinatorial sketching for ﬁnite programs,
ACM Sigplan Notices 41 (11) (2006) 404–415.
[111] D. Corapi, A. Russo, E. Lupu, Inductive logic programming in answer set programming, in: Inductive Logic
Programming, Springer, 2012, pp. 91–97.
[112] M. Genesereth, N. Love, General game playing: Game description language speciﬁcation, Computer Science
Department, Stanford University, Stanford, CA, USA, Tech. Rep.
[113] M. Genesereth, Y. Bj¨ornsson, The international general game playing competition, AI Magazine 34 (2) (2013)
107–107.
[114] S. Moyle, Using theory completion to learn a robot navigation control program, in: International Conference
on Inductive Logic Programming, Springer, 2002, pp. 182–197.
[115] R. P. Otero, Induction of the indirect eﬀects of actions by monotonic methods, in: International Conference
on Inductive Logic Programming, Springer, 2005, pp. 279–294.
63


## Page 64


[116] K. Inoue, H. Bando, H. Nabeshima, Inducing causal laws by regular inference, in: International Conference
on Inductive Logic Programming, Springer, 2005, pp. 154–171.
[117] D. Corapi, D. Sykes, K. Inoue, A. Russo, Probabilistic rule learning in nonmonotonic domains, in: Interna-
tional Workshop on Computational Logic in Multi-Agent Systems, Springer, 2011, pp. 243–258.
[118] C. Rodrigues, P. G´erard, C. Rouveirol, H. Soldano, Active learning of relational action models, in: Interna-
tional Conference on Inductive Logic Programming, Springer, 2011, pp. 302–316.
[119] S. Dˇzeroski, L. De Raedt, K. Driessens, Relational reinforcement learning, Machine Learning 43 (1-2) (2001)
7–52.
[120] L. De Raedt, Logical and Relational Learning, Springer Science & Business Media, 2008.
[121] L. Bu, R. Babu, B. De Schutter, et al., A comprehensive survey of multiagent reinforcement learning, IEEE
Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) 38 (2) (2008) 156–172.
[122] J. Goodacre, Inductive Learning of Chess Rules using Progol, Ph.D. thesis, University of Oxford (1996).
[123] K. Friston, A theory of cortical responses, Philosophical Transactions of the Royal Society B: Biological
sciences 360 (1456) (2005) 815–836.
[124] A. Cropper, R. Morel, Learning programs by learning from failures, arXiv preprint arXiv:2005.02259.
64

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 1910_02227v2_making_sense_of_sensory_input
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1910_02227V2_MAKING_SENSE_OF_SENSORY_INPUT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
