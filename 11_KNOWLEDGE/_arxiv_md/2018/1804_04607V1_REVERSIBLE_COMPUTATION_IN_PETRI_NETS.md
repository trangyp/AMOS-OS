---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1804.04607v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1804.04607v1_Reversible_Computation_in_Petri_Nets

> Source: 1804.04607v1_Reversible_Computation_in_Petri_Nets.pdf

> Pages: 25

---


## Page 1


Reversible Computation in Petri Nets
Anna Philippou
Department of Computer Science
University of Cyprus
annap@cs.ucy.ac.cy
Kyriaki Psara
Department of Computer Science
University of Cyprus
kpsara01@cs.ucy.ac.cy
Reversible computation is an unconventional form of computing where any executed sequence of
operations can be executed in reverse at any point during computation. It has recently been attracting
increasing attention in various research communities as on the one hand it promises low-power com-
putation and on the other hand it is inherent or of interest in a variety of applications. In this paper, we
propose a reversible approach to Petri nets by introducing machinery and associated operational se-
mantics to tackle the challenges of the three main forms of reversibility, namely, backtracking, causal
reversing and out-of-causal-order reversing. Our proposal concerns a variation of Petri nets where
tokens are persistent and are distinguished from each other by an identity which allows for transitions
to be reversed spontaneously in or out of causal order. Our design decisions are inﬂuenced by appli-
cations in biochemistry but the methodology can be applied to a wide range of problems that feature
reversibility. In particular, to demonstrate the applicability of our approach we use an example of
a biochemical system and an example of a transaction-processing system both of which naturally
embed reversible behaviour.
1
Introduction
Reversible computation is an unconventional form of computing where computation can be executed in
forward direction as effortlessly as it can be executed in backward direction. Any sequence of opera-
tions carried out by a system can be subsequently executed reversibly allowing the system to retrieve
any previous state at any point during computation. The motivation for reversible computing began
with Landauer’s observation that only irreversible computation generates heat [9] spawning a strong
line of research towards the creation of reversible logic gates and circuits. Subsequently, motivation for
studying reversibility has stemmed from a wide variety of applications which naturally embed reversible
behaviour. These include biological processes where computation may be carried out in forward or
backward direction [14, 8], and the ﬁeld of system reliability where reversibility can be used as means
of recovering from failures [6, 10].
Several subcategories of reversible computation have been identiﬁed and studied in the past years.
These include backtracking and the more general form of reversibility referred to as causal-order re-
versibility according to which a transition can be undone only if all its effects, if any, have been undone
beforehand. Attention has also turned towards reversing in out-of-causal order, a form of reversing
featured most notably in biochemical systems. These concepts have been studied within a variety of
formalisms. To begin with, a large amount of work has focused on providing a formal understanding of
reversibility within process calculi. The ﬁrst reversible process calculus dates back to 2004 when Danos
and Krivine proposed RCCS [5], a causal-consistent reversible extension of CCS, further developed in
[6, 7]. Soon after, Phillips and Ulidowski proposed a general method for reversing process calculi, with
their proposal of CCSK being a special instance of the methodology [13]. Constructs for controlling
reversibility were also proposed in reversible extensions of the π-calculus in [10, 12]. Most recently, the
study of out-of-causal-order reversibility continued with the introduction of a new operator for modelling
arXiv:1804.04607v1  [cs.LO]  10 Apr 2018


## Page 2


2
Reversible Computation in Petri nets
local reversibility in [8]. Furthermore, reversible computation was studied within event structures in [17].
The modelling of bonding within reversible processes and event structures was also considered in [15]
whereas a reversible computational calculus for modelling chemical systems composed of signals and
gates was proposed in [4].
Petri nets (PNs) are a graphical mathematical language that can be used for the speciﬁcation and
analysis of discrete event systems. They are associated with a rich mathematical theory and a variety of
tools, and they have been used extensively for modelling and reasoning about a wide range of applica-
tions. A property studied in the context of Petri nets is that of Petri net reversibility which describes the
ability of a system to return to the initial state from any reachable state. This, however, is in contrast to
the notion of reversible computation as discussed above where the intention is not to return to a state via
arbitrary execution but to reverse the effect of already executed transitions.
More recently the ﬁrst study of reversible computation within Petri nets was proposed in [2, 3]. In
these works, the authors investigate the effects of adding reversed versions of selected transitions in a
Petri net, where these transitions are obtained by reversing the directions of a transition’s arcs. They
then explore decidability problems regarding reachability and coverability in the resulting Petri nets.
Related to our study of causal reversibility is also work carried out regarding causality in Petri nets. We
mention [19, 18, 16] where the authors explore causal semantics in Petri nets by utilising the individual
token interpretation to distinguish tokens as well as the collective token interpretation.
Contribution. In this work we set out to study reversible computation in the context of Petri nets and
in particular to explore the modelling of the main strategies for reversing computation. Our aim is to
address the challenges of capturing the notions of backtracking, causal reversibility and out-of-causal-
order reversibility within the Petri net framework, thus proposing a novel, graphical methodology for
studying reversibility in a model where transitions can be taken in either direction.
Our proposal is motivated by applications from biochemistry where out-of-causal-order reversibility
is inherent, and it supports all the forms of reversibility that have been discussed above. In particular,
we consider a subclass of PNs which are acyclic and where tokens are persistent. We prove that the
amount of ﬂexibility allowed in causal reversibility indeed yields a causally consistent semantics. We
also demonstrate that out-of-causal reversibility is able to create new states unreachable by forward-only
execution which, nonetheless, respect causality with regard to connected components of tokens.
Paper organisation. In the next section we give an overview of the different types of reversibility
and their characteristics and we discuss the challenges of modelling reversibility in the context of Petri
nets. In Section 3 we introduce the formalism of Reversible Petri nets, and, in Section 4, we present
semantics for the models that capture backtracking, causal and out-of-causal-order reversibility. We
illustrate the framework with an example inspired by long-running transactions. Section 5 concludes the
paper. Missing proofs can be found in an appendix.
2
Forms of Reversibility and Petri Nets
Even though reversing computational processes in concurrent and distributed systems has many promis-
ing applications, it also has many technical and conceptual challenges. One of the most important ques-
tions that arise regards the strategy to be applied when going backwards. Several approaches have been
explored in the literature over the last decade which differ in the order in which steps are taken backwards.
The most prominent of these are backtracking, causal reversibility, and out-of-causal-order reversibility.
Backtracking is the process of rewinding one’s computation trace, that is, computational steps are
undone in the exact inverse order to the one in which they have occurred. This form of reversing ensures


## Page 3


A. Philippou & K. Psara
3
Figure 1: Causal Reversibility
that at any state in a computation there is at most one predecessor state. In the context of concurrent
systems, this form of reversibility can be thought of as overly restrictive since, undoing moves only in
the order in which they were taken, induces fake causal dependencies on backward sequences of actions:
actions, which could have been reversed in any order are forced to be undone in the precise order in
which they occurred.
A second approach to reversibility, named causal reversibility, relaxes the rigidity of backtracking.
It allows a more ﬂexible form of reversibility by allowing events to reverse in an arbitrary order assum-
ing that they respect the causal dependencies that hold between them. Thus, in the context of causal
reversibility, reversing does not have to follow the exact inverse order for independent events as long as
caused actions, also known as effects, are undone before the actions that have caused them.
For example consider the Petri net in Figure 1. We may observe that transitions t1 and t2 are inde-
pendent from each other, as they may be taken in any order, and they are both prerequisites for transition
t3. Backtracking the sequence of transitions ⟨t1,t2,t3⟩would require that the three transitions should be
reversed in exactly the reverse order, i.e. ⟨t3,t2,t1⟩. Instead, causal ﬂexibility allows the inverse compu-
tation to rewind t3 and then t1 and t2 in any order (but never t1 or t2 before t3).
Both backtracking and causal reversing are cause-respecting. There are, however, many real-life
examples where undoing things in an out-of-causal order is either inherent or could be beneﬁcial. In fact,
this form of undoing plays a vital role on mechanisms driving long-running transactions and biochemical
reactions. Consider every state of the execution to be a result of a series of actions that have causally
contributed to the existence of the current state. If the actions were to be reversed in a causally-respecting
manner then we would only be able to move back and forth through previously visited states. Therefore,
one might wish to apply out-of-order reversibility in order to create fresh alternatives of current states
that were formerly inaccessible by any forward-only execution path.
Since out-of-order reversibility contradicts program order by violating the laws of causality, it comes
with its own peculiarities that need to be taken into consideration while designing reversible systems.
To appreciate these peculiarities and obtain insights towards our approach on addressing reversibility
within Petri nets, we will use a standard example from the literature, namely the process of catalysis
from biochemistry.
Consider the catalyst c that helps the otherwise inactive molecules a and b to bond. The process
followed to achieve catalysis is element c bonding with a which then enables the bonding between a and
b. Next, the catalyst is no longer needed and its bond to the other two molecules is released. A Petri net
model of this process is illustrated in Figure 2. The Petri net executes transition t1 via which the bond ca
is created, followed by action t2 to produce cab. Finally, action t1 “reverses” the bond between a and c,
yielding ab and releasing c. (The ﬁgure portrays the ﬁnal state of the execution assuming that initially
exactly one token existed in places a, b, and c.)


## Page 4


4
Reversible Computation in Petri nets
Figure 2: Catalysis in classic Petri nets
This example illustrates that Petri nets are not reversible by nature, in the sense that every transition
cannot be executed in both directions. Therefore an inverse action, (e.g. transition t1 for undoing the
effect of transition t1, namely bond ca) needs to be added as a supplementary forward transition for
achieving the undoing of a previous action. This explicit approach of modelling reversibility can prove
cumbersome in systems that express multiple reversible patterns of execution, resulting in larger and
more complex systems. Furthermore, it fails to capture reversibility as a mode of computation. The
intention of our work is to study an approach for modelling reversible computation that does not require
the addition of new, reversed transitions but instead allows to execute transitions in both the forward as
well as the backward direction, and, thereby, explore the theory of reversible computation within Petri
nets.
However, when attempting to model the catalysis example while executing transitions in both the
forward and the backward directions, we may observe a number of obstacles. At an abstract level, the
behaviour of the system should exhibit a sequence of three transitions: execution of t1 and t2, followed by
the reversal of transition t1. The reversal of transition t1 should implement the release of c from the bond
cab and make it available for further instantiations of transition t1, if needed, while the bond ab should
remain in place. This implies that a reversing Petri net model should provide resources a, b and c as well
as ca, cab and ab and implement the reversal of action t1 as the transformation of resource cab into c and
ab. Note that resource ab is inaccessible during the forward execution of transitions t1 and t2 and only
materialises after the reversal of transition t1, i.e. only once the bond between a and c is broken. Given the
static nature of a Petri net, this suggests that resources such as ab should be represented at the token level
(as opposed to the place level). As a result, the concept of token individuality is of particular relevance to
reversible computation in Petri nets while other constructs/functions at token level are needed to capture
the effect and reversal of a transition.
Indeed, reversing a transition in an out-of-causal order may imply that while some of the effects of
the transition can be reversed (e.g. the release of the catalyst back to the initial state), others must be
retained due to computation that succeeded the forward execution of the next transition (e.g. token a
cannot be released during the reversal of t1 since it has bonded with b in transition t2). This latter point
is especially challenging since it requires to determine a model in a precise manner so as to identify
which effects are allowed to be “undone” when reversing a transition. We will now proceed to discuss
our design decisions towards our proposal for a reversing Petri net framework.
2.1
Design Choices
As highlighted by the catalyst example, reversing transitions in a Petri net model requires close monitor-
ing of token manipulation within a net and clear enunciation of the effects of a transition. In particular,


## Page 5


A. Philippou & K. Psara
5
Figure 3: Catalysis in reversing Petri nets
undoing a transition may result in some tokens to return to the in-places of the transition, while others
will not do so unless and/or until further transitions in which the tokens were involved are additionally
reversed. In order to achieve this one we would need to distinguish each individual token along with
sufﬁcient information regarding its causal path, i.e., the places and transitions it has traversed before
reaching its current state. This requirement is rather demanding and would require special care in the
case where transitions consume multiple tokens but release only a subset of the tokens or even a set of
new tokens.
In our approach we employ the notion of token individuality but, instead of maintaining extensive
histories for recording the precise evolution of each token through transitions and places, we have opted
to employ a novel approach inspired by out-of-causal reversibility in biochemistry as well as approaches
from related literature [15]. The resulting framework is light in the sense that no memory needs to
be stored per token to retrieve its causal path while enabling reversible semantics for the three main
types of reversibility. Furthermore, while inspired by biochemistry, the framework can be applied in
other contexts of reversible systems: for instance in Section 4.4 we provide an example of reversible
transactions.
Speciﬁcally, our approach similarly to Coloured Petri Nets allows the observation of token evolution
through transition ﬁring. We introduce two notions that intuitively capture tokens and their history: the
notion of base and a new type of tokens called bonds. A base is a persistent type of token which cannot
be consumed and therefore preserves its individuality through various transitions. For a transition to ﬁre,
the incoming arcs identify the required tokens/bonds and the outgoing arcs may create new bonds or
transfer already existing tokens/bonds along the places of a PN. Therefore, the effect of a transition is the
creation of new bonds between the tokens it takes as input and the reversal of such a transition involves
undoing the respective bonds. In other words, a bonded token is a coalition of bases connected via bonds
into a structure located in a place, thus presenting a single entity while individually representing each
base/bond.
Based on these ideas, we may describe the catalyst example in our proposed framework as shown
in Figure 3. In this new setting a and c are bases which during transition t1 are connected via a bond
into place x, while transition t2 brings into place a new bond between a and b. In Figure 3 we may see
the state that arises after execution of t1 and t2 and the reversal of transition t1. In this state, base c has
returned to its initial place u whereas bond a−b has remained in place y. A thorough explanation of the
notation is given in the next section.
The next design decision in our methodology is that we offer the ﬂexibility for transitions to take as
input a subset of the bonds and bases, thus denoting exactly the entities that are necessary for the ﬁring
of a transition by labelling the incoming arcs with necessary tokens. If further bases/bonds exist in a


## Page 6


6
Reversible Computation in Petri nets
place but are not featured in the incoming arcs to a transition, they do not necessarily need to exist for
the transition to ﬁre. Such absence of tokens may occur due to a previous reversal of a transition that
resulted in tokens backtracking along the net. However, if such bases/bonds do exist in an in-place, the
transition should output the respective tokens in its output places, thus preserving the bonds.
The ﬁnal design decision of our framework stems from the need to identify at each point in time the
history of execution, a necessary aspect for all forms of reversibility: observing a state of a Petri net,
with tokens scattered along its places, due to the nondeterministic nature of Petri nets, it is not possible
to discern the history that led to the speciﬁc state and consequently the precise transitions that can be
undone. While some aspects of this history are made available by the persistence of bases and the creation
of bonds, due to nondeterminism we need to distinguish the cause of a certain state among the several
possible alternatives. To achieve this, we associate transitions with a history where we store keys in
increasing order each time an instance of the transition is executed. This allows to backtrack computation
as well as to extract the causes of bonds as needed in causal and out-of-causal-order reversibility. These
identiﬁers can be removed from the history once the respective transition has been reversed.
As a ﬁnal note, we point out that in what follows we make the assumption that we may have no more
than one token for each base in a Reversible Petri net model and that models are acyclic. The assumptions
enable a clearer enunciation and presentation of our methodology. In case an application requires the
presence of a collection of identical components interacting with each other, e.g. the existence of two
molecules of hydrogen in H2O, this could be modelled via two autonomous tokens namely H1 and H2.
We expect that our theory can be extended to relax both of these assumptions by associating further
information to tokens and transitions in a system in order to distinguish between threads of execution
associated to different tokens of the same base as well multiple occurrences of the same transition.
3
Reversing Petri Nets
We are now ready to deﬁne a model of reversing Petri nets as follows:
Deﬁnition 1 A reversing Petri net (RPN) is a tuple (A,P,B,T,F) where:
1. A is a ﬁnite set of bases or tokens ranged over by a, b,.... A = {a | a ∈A} contains a “negative”
instance for each token and we write A = A∪A.
2. P is a ﬁnite set of places.
3. B ⊆A×A is a set of bonds ranged over by β, γ,.... We use the notation a−b for a bond (a,b) ∈B.
B = {β | β ∈B} contains a “negative” instance for each bond and we write B = B∪B.
4. T is a ﬁnite set of transitions.
5. F : (P×T ∪T ×P) →2A ∪B is a set of directed arcs.
A reversing Petri net is built on the basis of a set of bases or, simply, tokens. We take an individual-
token interpretation thus considering each token to have a unique name. In this way, tokens may be
distinguished from each other, their persistence can be guaranteed and their history inferred from the
structure of a Petri net (as implemented by function F, discussed below). Tokens correspond to the basic
entities that occur in a system. They may occur as stand-alone elements but as computation proceeds
they may also merge together to form bonds. Places and transitions have the standard meaning.
Directed arcs connect places to transitions and vice versa and are labelled by a subset of A ∪B where
A = {a | a ∈A} contains the set of “negative” tokens expressing token absence and B = {β | β ∈B} is a
set of “negative” bonds expressing bond absence. For a label ℓ= F(x,t) or ℓ= F(t,x), we assume that


## Page 7


A. Philippou & K. Psara
7
each token a can appear in ℓat most once, either as a or as a, and that if a bond (a,b) ∈ℓthen a,b ∈ℓ.
Furthermore, for ℓ= F(t,x), it must be that ℓ∩(A ∪B) = /0, that is, negative tokens/bonds may only
occur on arcs incoming to a transition. Intuitively, these labels express the requirements for a transition
to ﬁre when placed on arcs incoming the transition, and the effects of the transition when placed on the
outgoing arcs. Thus, if a ∈F(x,t) this implies that token a is required for the transition t to ﬁre, and
similarly for a bond β ∈F(x,t). On the other hand, a ∈F(x,t), expresses that token a should not be
present in the incoming places of t for the transition to ﬁre and similarly for bond β ∈F(x,t). Note
that negative tokens/bonds are close in spirit to inhibitor arcs of extended Petri nets. Finally, note that
F(x,t) = /0 implies that there is no arc from place x to transition t and similarly for F(t,x) = /0.
We introduce the following notations. We write ◦t = {x ∈P | F(x,t) ̸= /0} and t◦= {x ∈P | F(t,x) ̸=
/0} for the incoming and outgoing places of transition t, respectively. Furthermore, we write pre(t) =
S
x∈P F(x,t) for the union of all labels on the incoming arcs of transition t, and post(t) = S
x∈P F(t,x) for
the union of all labels on the outgoing arcs of transition t.
Deﬁnition 2 For a reversing Petri net to be well-formed, it should satisfy the following conditions for all
t ∈T:
1. A∩pre(t) = A∩post(t),
2. If a−b ∈pre(t) then a−b ∈post(t),
3. F(t,x)∩F(t,y) = /0 for all x,y ∈P, x ̸= y.
According to the above we have that: (1) transitions do not erase tokens, (2) transitions do not destroy
bonds, that is, if a bond a−b exists in an input place of a transition, then it is maintained in some output
place, and (3) tokens/bonds cannot be cloned into more than one outgoing places.
In a graphical representation, tokens are indicated by •, places by circles, transitions by boxes, and
bonds by lines between tokens. As with standard Petri nets, we employ the notion of a marking. A
marking is a distribution of tokens and bonds across places, M : P →A∪B where a−b ∈M(x), for some
x ∈P, implies a,b ∈M(x). In addition, we employ the notion of a history which assigns a memory to
each transition, H : T →ε ∪N. Intuitively, a history of ε captures that the transition has not taken place
and a history of n ∈N captures that the transition was executed and not reversed where n indicates the
order of execution amongst non-reversed actions. H0 denotes the initial history where H0(t) = ε for all
t ∈T. In a graphical representation histories are presented over the respective transitions as [m], where
m = H(t) for transition t. A pair of a marking and history describes a state of a PN based on which
execution is determined. We use the notation ⟨M,H⟩to denote states.
As the last piece of our machinery, we deﬁne a notion that identiﬁes connected components of tokens
within a place. Note that more than one connected component may arise in a place due to the fact that
various unconnected tokens may be moved to a place simultaneously by a transition, while the reversal
of transitions which results in the destruction of bonds may break down a connected component into
various subcomponents. We deﬁne con(a,C), where a is a base and C ⊆A∪B a set of connections, to be
the tokens connected to a via bonds as well as the bonds creating these connections according to set C.
con(a,C) = ({a}∩C)∪{β,b,c | ∃w s.t. path(a,w,C),β ∈w, and β = (b,c)}
where path(a,w,C) if w = ⟨β1,...,βn⟩, and for all 1 ≤i ≤n, βi = (ai−1,ai) ∈C ∩B, ai ∈C ∩A, and
a0 = a. We also write con(S,C), where S ⊆A, for S
a∈S con(a,C).
Returning to the example of Figure 3, we may see a reversing net with three tokens a, b, and c,
transition t1, which bonds tokens a and c within place x, and transition t2, which bonds the a of bond a−c
with token b into place y. The ﬁnal marking after executing t1 and consecutively t2 assigns a complex


## Page 8


8
Reversible Computation in Petri nets
of three bonded tokens named c−a−b into place y. By applying out-of-causal order reversibility we are
able to reverse transition t1 and release token c back to its initial place which is place u. The current
marking also indicates the bond a−b remaining intact in place y.
4
Semantics
We may now deﬁne the various types of execution within reversing Petri nets. In what follows we restrict
our attention to PNs (A,P,B,T,F) where F deﬁnes an acyclic graph with initial marking M0 such that
for all a ∈A, |{x | a ∈M0(x)}| = 1.
4.1
Forward Execution
Deﬁnition 3 Consider a reversing Petri net (A,P,B,T,F), a transition t ∈T, and a state ⟨M,H⟩. We say
that t is forward enabled in ⟨M,H⟩if the following hold:
1. if a ∈F(x,t), for some x ∈◦t, then a ∈M(x), and if a ∈F(x,t) for some x ∈◦t, then a ̸∈M(x),
2. if β ∈F(x,t), for some x ∈◦t, then β ∈M(x), and if β ∈F(x,t) for some x ∈◦t, then β ̸∈M(x),
3. if a ∈F(t,y1) and b ∈F(t,y2) where y1 ̸= y2 then b ̸∈con(a,M(x)) where x ∈◦t, and
4. if β ∈F(t,x) for some x ∈t◦and β ∈M(y) for some y ∈◦t then β ∈F(y,t).
Thus, t is enabled in state ⟨M,H⟩if (1), (2) all tokens and bonds required for the transition to take
place are available in the incoming places of t and none of the tokens/bonds whose absence is required
exists in an incoming place of the transition, (3) if a transition forks into out-places y1 and y2 then the
tokens transferred to these places are not connected to each other in the incoming places to the transition,
and (4) if a pre-existing bond appears in an outgoing arc of a transition, then it is also a precondition of
the transition to ﬁre. Contrariwise, if the bond appears in an outgoing arc of a transition (β ∈F(t,x) for
some x ∈t◦) but is not a requirement for the transition to ﬁre (β ̸∈F(y,t) for all y ∈◦t), then the bond
should not be present in an in-place of the transition (β ̸∈M(y) for all y ∈◦t). Thus, we deﬁne the effect
of a transition as
eﬀ(t) = post(t)−pre(t)
We observe that the effect of a transition is the set of new bonds created by the transition since, by
Deﬁnition 3(4), the bonds that are created by the transition are exactly those that occur in the postcondi-
tion of a transition but not in its precondition. This will subsequently enable the enunciation of transition
reversal by the destruction of exactly the bonds in eﬀ(t).
Deﬁnition 4 Given a reversing Petri net (A,P,B,T,F), a state ⟨M,H⟩, and a transition t enabled in
⟨M,H⟩, we write ⟨M,H⟩
t
−→⟨M′,H′⟩where:
M′(x)
=



M(x)−S
a∈F(x,t) con(a,M(x)),
if x ∈◦t
M(x)∪F(t,x)∪S
a∈F(t,x),y∈◦t con(a,M(y)),
if x ∈t◦
M(x),
otherwise
and
H′(t′)
=
 max{k|k = H(t′′),t′′ ∈T}+1,
if t′ = t
H(t′),
otherwise


## Page 9


A. Philippou & K. Psara
9
Figure 4: Forward and backtracking execution
According to the deﬁnition, when a transition t is executed, all tokens and bonds occurring in its
incomings arcs are relocated from the input places to the output places along with their connected com-
ponents. Moreover, history function H is extended to H′ by assigning to transition t the next available
integer key.
An example of forward transitions can be seen in the ﬁrst three steps of Figure 4 where transitions
t1 and t2 take place with the histories of the two transitions becoming [1] and [2], respectively. Note that
to avoid overloading ﬁgures, we omit writing the bases of bonds on the arcs of an RPN and recall that
within places we indicate bases by • and bonds by lines between relevant bases.
We may prove the following result:
Proposition 1 [Token and bond preservation.] Consider a RPN (A,P,B,T,F), a state ⟨M,H⟩such that
for all a ∈A, |{x ∈P | a ∈M(x)}| = 1, and a transition ⟨M,H⟩
t
−→⟨M′,H′⟩. Then (1) for each base a ∈A,
|{x ∈P | a ∈M′(x)}| = 1, and (2) for each bond β ∈B, |{x ∈P | β ∈M(x)}| ≤|{x ∈P | β ∈M′(x)}| ≤1.
Proof:
The proposition veriﬁes that bases are preserved during forward execution in the sense that
transitions neither erase nor clone them. As far as bonds are concerned, the proposition states that
forward execution may only create new bonds. The proof of the result follows the deﬁnition of forward
execution and relies on the well-formedness of reversing Petri nets.
Consider a RPN (A,P,B,T,F), a state ⟨M,H⟩such that |{x ∈P | a ∈M(x)}| = 1 for all a ∈A, and
suppose ⟨M,H⟩
t
−→⟨M′,H′⟩.
For the proof of clause (1) let a ∈A. Two cases exist:
1. a ∈con(b,M(x)) for some b ∈F(x,t). Note that x is unique by the assumption that |{x ∈P | a ∈
M(x)}| = 1. Furthermore, according to Deﬁnition 4, we have that M′(x) = M(x)−{con(c,M(x)) |


## Page 10


10
Reversible Computation in Petri nets
c ∈F(x,t)}, which implies that a ̸∈M′(x). On the other hand, note that by Deﬁnition 2(1), b ∈
post(t). Thus, there exists y ∈t◦, such that b ∈F(t,y). Note that this y is unique by Deﬁnition 2(3).
As a result, by Deﬁnition 4, M′(y) = M(y)∪F(t,y)∪{con(c,M(y′)) | c ∈F(t,y),y′ ∈◦t}. Since
b ∈F(x,t)∩F(t,y), a ∈con(b,M(x)), this implies that a ∈M′(y).
Now suppose that a ∈con(c,M(x)) for some c ̸= b, c ∈F(t,y′). Then, by Deﬁnition 3(3), it must
be that y = y′. As a result, we have that {z ∈P | a ∈M′(z)} = {y} and the result follows.
2. a ̸∈con(b,M(x)) for all b ∈F(x,t), x ∈P. This implies that {x ∈P | a ∈M′(x)} = {x ∈P | a ∈
M(x)} and the result follows.
To prove clause (2) of the proposition, consider a bond β ∈B, β = (a,b). We observe that, since
|{x ∈P | a ∈M(x)}| = 1 for all a ∈A, |{x ∈P | β ∈M(x)}| ≤1. The proof follows by case analysis as
follows:
1. Suppose |{x ∈P | β ∈M(x)}| = 0. Two cases exist:
• Suppose β ̸∈F(t,x) for all x ∈P. Then, by Deﬁnition 4, β ̸∈M′(x) for all x ∈P. Conse-
quently, |{x ∈P | β ∈M′(x)}| = 0 and the result follows.
• Suppose β ∈F(t,x) for some x ∈P. Then, by Deﬁnition 2(3), x is unique, and by Deﬁnition 4,
β ∈M′(x). Consequently, |{x ∈P | β ∈M′(x)}| = 1 and the result follows.
2. Suppose |{x ∈P | β ∈M(x)}| = 1. Two cases exist:
• β ̸∈con(c,M(x)) for all c ∈F(x,t). This implies that {x ∈P | β ∈M′(x)} = {x ∈P | β ∈
M(x)} and the result follows.
• β ∈con(c,M(x)) for some c ∈F(x,t). Then, according to Deﬁnition 4, we have that M′(x) =
M(x)−{con(c,M(x)) | c ∈F(x,t)}, which implies that β ̸∈M′(x). On the other hand, note
that by the deﬁnition of well-formedness, Deﬁnition 2(1), c ∈post(t). Thus, there exists
y ∈t◦, such that c ∈F(t,y). Note that this y is unique by Deﬁnition 2(3). As a result,
by Deﬁnition 4, M′(y) = M(y) ∪F(t,y) ∪{con(c,M(y′)) | c ∈F(t,y),y′ ∈◦t}. Since c ∈
F(x,t)∩F(t,y), β ∈con(c,M(x)), this implies that β ∈M′(y).
Now suppose that β ∈con(d,M(x)) for some d ̸= c, and c ∈F(d,y′). Then, by Deﬁnition 3,
and since con(c,M(x)) = con(d,M(x)), it must be that y = y′. As a result, we have that
{z ∈P | β ∈M′(z)} = {y} and the result follows.
2
4.2
Backtracking
Let us now proceed to the simplest form of reversibility, namely, backtracking.
Deﬁnition 5 Consider a reversing Petri net (A,P,B,T,F) a state ⟨M,H⟩and a transition t ∈T. We say
that t is bt-enabled in ⟨M,H⟩if H(t) = k ∈N with k ≥k′ for all k′ ∈N, k′ = H(t′), t′ ∈T.
Thus, a transition t is bt-enabled if it is the last transition to have been executed, i.e., it has the highest
H value. The effect of reversing a transition in a Petri net in a backtracking fashion is as follows:
Deﬁnition 6 Given a reversing Petri net (A,P,B,T,F), a state ⟨M,H⟩, and a transition t bt-enabled in
⟨M,H⟩, we write ⟨M,H⟩
t⇝b ⟨M′,H′⟩where:
M′(x)
=



M(x)∪S
y∈t◦,a∈F(x,t)∩F(t,y) con(a,M(y)−eﬀ(t)),
if x ∈◦t
M(x)−S
a∈F(t,x) con(a,M(x)),
if x ∈t◦
M(x),
otherwise


## Page 11


A. Philippou & K. Psara
11
and
H′(t′)
=
 ε,
if t′ = t
H(t),
otherwise
Thus, when a transition t is reversed in a backtracking fashion all tokens and bonds in the postcondi-
tion of the transition, as well as their connected components, will be transferred to the incoming places
of the transition and any newly-created bonds will be broken. Moreover, history function H is reﬁned
to H′ by setting H′(t) = ε, capturing that the speciﬁc transition has been reversed. In the last two steps
of Figure 4 we observe transitions t2 and t1 being reversed with the histories of the two transitions being
eliminated.
We may prove the following result:
Proposition 2 [Token preservation and bond destruction.] Consider a RPN (A,P,B,T,F), a state ⟨M,H⟩
such that for all a ∈A, |{x ∈P | a ∈M(x)}| = 1, and a transition ⟨M,H⟩t⇝b ⟨M′,H′⟩. Then, (1) for each
base a ∈A, |{x ∈P | a ∈M′(x)}| = 1, and (2) for each bond β ∈B, 1 ≥|{x ∈P | β ∈M(x)}| ≥|{x ∈P |
β ∈M′(x)}|.
Proof:
The proposition veriﬁes that bases are preserved during backtracking execution in the sense
that there exists exactly one instance of each base and backtracking transitions neither erase nor clone
them. As far as bonds are concerned, the proposition states that at any time there may exist at most one
instance of a bond and that backtracking transitions may only destroy bonds. The proof of the result
follows the deﬁnition of backward execution and relies on the well-formedness of reversing Petri nets.
Consider a RPN (A,P,B,T,F), a state ⟨M,H⟩such that |{x ∈P | a ∈M(x)}| = 1 for all a ∈A, and
suppose ⟨M,H⟩
t⇝b ⟨M′,H′⟩.
We begin with the proof of clause (1) and let a ∈A. Two cases exist:
1. a ∈con(b,M(x)) for some b ∈F(t,x). Note that by the assumption of |{x ∈P | a ∈M(x)}| = 1, x
must be unique. Let us choose b such that, additionally, a ∈con(b,M(x)−eﬀ(t)). Note that such
a b must exist, otherwise the forward execution of t would not have transferred a along with b to
place x.
According to Deﬁnition 6, we have that M′(x) = M(x)−{con(c,M(x)) | c ∈F(t,x)}, which implies
that a ̸∈M′(x). On the other hand, note that by the deﬁnition of well-formedness, Deﬁnition 2(1),
b ∈pre(t). Thus, there exists y ∈◦t, such that b ∈F(y,t). Note that this y is unique. If not, then
there exist y and y′ such that y ̸= y′ with b ∈F(y,t) and b ∈F(y′,t). By the assumption, however,
that there exists at most one token of each base, and Proposition 1, t would never be enabled, which
leads to a contradiction. As a result, by Deﬁnition 6, M′(y) = M(y)∪{con(c,M(y′)−eﬀ(t)) | c ∈
F(y,t)∩F(t,y′)}. Since b ∈F(y,t)∩F(t,x), a ∈con(b,M(x)−eﬀ(t)), this implies that a ∈M′(y).
Now suppose that a ∈con(c,M(x)−eﬀ(t)), c ̸= b, and c ∈F(y′,t). Since a ∈con(b,M(x)−eﬀ(t)),
it must be that con(b,M(x)−eﬀ(t)) = con(c,M(x)−eﬀ(t)). Since b and c are connected to each
other but the connection was not created by transition t (the connection is present in M(x)−eﬀ(t)),
it must be the connection was already present before the forward execution of t and, by token
uniqueness, we conclude that y = y′.
2. a ̸∈con(b,M(x)) for all b ∈F(t,x), x ∈P. This implies that {x ∈P | a ∈M′(x)} = {x ∈P | a ∈
M(x)} and the result follows.
Let us now prove clause (2) of the proposition. Consider a bond β ∈B, β = (a,b). We observe that,
since |{x ∈P | a ∈M(x)}| = 1 for all a ∈A, |{x ∈P | β ∈M(x)}| ≤1. The proof follows by case analysis
as follows:


## Page 12


12
Reversible Computation in Petri nets
1. β ∈con(c,M(x)) for some c ∈F(t,x), x ∈P. By the assumption of |{x ∈P | β ∈M(x)}| = 1, x
must be unique. Then, according to Deﬁnition 6, we have that M′(x) = M(x)−{con(c,M(x)) | c ∈
F(x,t)}, which implies that β ̸∈M′(x). Two cases exist:
• If β ∈eﬀ(t), then β ̸∈M′(y) for all places y ∈P.
• If β ̸∈eﬀ(t) then let us choose c such that β ∈con(c,M(x) −eﬀ(t)). Note that such a c
must exist, otherwise the forward execution of t would not have connected β with c. By the
deﬁnition of well-formedness, Deﬁnition 2(1), c ∈pre(t). Thus, there exists y ∈◦t, such that
c ∈F(y,t). Note that this y is unique (if not, t would not have been enabled). As a result, by
Deﬁnition 6, β ∈M′(y).
Now suppose that β ∈con(d,M(x)−eﬀ(t)), d ̸= c, and d ∈M′(y′). Since β ∈con(c,M(x)−
eﬀ(t)), it must be that con(c,M(x)−eﬀ(t)) = con(d,M(x)−eﬀ(t)). Since c and d are con-
nected to each other but the connection was not created by transition t (the connection is
present in M(x) −eﬀ(t)), it must be the connection was already present before the for-
ward execution of t and, by token uniqueness, we conclude that y = y′. This implies that
{z ∈P | β ∈M′(z)} = {y}.
The above imply that {z ∈P | β ∈M(z)} = {x} and {z ∈P | β ∈M′(z)} ⊆{y} and the result
follows.
2. β ̸∈con(c,M(x)) for all c ∈F(t,x), x ∈P. This implies that {x ∈P | β ∈M′(x)} = {x ∈P | β ∈
M(x)} and the result follows.
2
Let us now consider the combination of forward and backward moves in executions. We write 7−→b
for −→∪⇝b. The following result establishes that in an execution beginning in the initial state of a
Petri net, bases are preserved, bonds can have at most one instance at any time and a new occurrence
of a bond may be created during a forward transition that features the bond as its effect whereas a bond
can be destroyed during the backtracking of a transition that features the bond as its effect. This last
point clariﬁes that the effect of a transition characterises the bonds that are newly-created during the
transition’s forward execution and the ones that are being destroyed during its reversal.
Proposition 3 Given a RPN (A,P,B,T,F), an initial state ⟨M0,H0⟩and an execution ⟨M0,H0⟩
t1
7−→b
⟨M1,H1⟩
t2
7−→b ...
tn
7−→b ⟨Mn,Hn⟩, the following hold:
1. For all a ∈A and i, 0 ≤i ≤n, |{x ∈P | a ∈Mi(x)}| = 1.
2. For all β ∈B and i, 0 ≤i ≤n, 0 ≤|{x ∈P | β ∈Mi(x)}| ≤1, and,
(a) if ti is a forward transition with β ∈eﬀ(ti), then β ∈Mi(x) for some x ∈P and β ̸∈Mi−1(y)
for all y ∈P,
(b) if ti is a backtracking transition with β ∈eﬀ(ti) then β ∈Mi−1(x) for some x ∈P and β ̸∈
Mi(y) for all y ∈P, and
(c) if β ̸∈eﬀ(ti) then β ∈Mi−1(x) if and only if β ∈Mi(x).
Proof:
The proposition veriﬁes that (1) tokens are preserved throughout the execution of an RPN, (2)
bonds can be created (during forward execution), destructed (during backward execution), or preserved
through actions that do not operate directly on the bond.
To begin with, we observe that the proofs of clauses (1) and (2) follow directly from clauses (1) and
(2) of Propositions 1 and 2, respectively. Clause (3) follows from Deﬁnition 3(4) and, ﬁnally, clause (4)
stems from Deﬁnition 6 and can be proved as in the proof of Proposition 2(2), case (1).
2
In this setting we may establish a loop lemma:


## Page 13


A. Philippou & K. Psara
13
Lemma 1 (Loop) For any forward transition ⟨M,H⟩
t
−→⟨M′,H′⟩there exists a backward transition
⟨M′,H′⟩
t⇝b ⟨M,H⟩and vice versa.
Proof:
Suppose ⟨M,H⟩
t
−→⟨M′,H′⟩. Then t is clearly bt-enabled in H′. Furthermore, ⟨M′,H′⟩
t⇝b
⟨M′′,H′′⟩where H′′ = H. In addition, all tokens and bonds involved in transition t (except those in eﬀ(t))
will be returned from the out-places of transition t back to its in-places. Speciﬁcally, for all a ∈A, it is
easy to see by the deﬁnition of ⇝b that a ∈M′′(x) if and only if a ∈M(x). Similarly, by Proposition 3,
for all β ∈B, β ∈M′′(x) if and only if β ∈M(x). The opposite direction can be argued similarly, only
this time tokens and bonds involved in transition t will be moved from the in-places to the out-places of
transition t.
2
4.3
Causal Reversing
We now move on to consider causality between transitions in a Petri net and reversibility in a causal-
respecting order. The following deﬁnition shows that given a transition if all the causally linked tran-
sitions have either been reversed or not executed then the transition is co-enabled. Thus, we deﬁne the
notion of causally-ordered enabledness as follows:
Deﬁnition 7 Consider a reversing Petri net (A,P,B,T,F), a state ⟨M,H⟩, and a transition t ∈T. Then t
is co-enabled in ⟨M,H⟩if H(t) ∈N and, for all a ∈F(t,x), if a ∈M(y) for some y and con(a,M(y)) ∩
pre(t′) ̸= /0 for some t′ then either H(t′) = ε or H(t′) ≤H(t).
We may prove the following equivalent enunciation of the deﬁnition which reduces co-enabledness to
the availability of tokens in the outplaces of an executed transition. Acyclicity of RPNs is central for the
proof of this result.
Proposition 4 Consider a reversing Petri net (A,P,B,T,F), a state ⟨M,H⟩, and a transition t ∈T. Then
t is co-enabled in ⟨M,H⟩if and only if H(t) ∈N and for all a,β ∈F(t,x) we have a,β ∈M(x).
Proof:
Let us consider the “if” direction. This can be proved by contradiction. Suppose that transition
t is co-enabled in ⟨M,H⟩and there exist bonds and/or tokens that are not located on its out-places but
are required on its out-going arcs for the transition to reverse, i.e., there exist a and/or β ∈F(t,x) but
a,β ̸∈M(x). Since H(t) ∈N, the transition has been executed and not reversed. As a consequence of
Deﬁnition 4 it must be that all bonds and tokens in post(t) have been moved to the out-places of t. The
fact, however, that some of these are no longer available in these out-places suggests that some transition
t′ with t ◦∩◦t′ = /0 has been consequently executed and further moved these tokens in its out-places.
This implies that either a ∈pre(t′), or there exists b ∈pre(t′) with a being connected to b when t′ was
executed, thus moving a into the out-places of t′ when t′ was executed. Note that, by our assumption of
acyclicity of RPNs, this out-places must be different to the out-places of t. However, by the conditions
of co-enabledness, it must be that H(t′) = ε. This results in a contradiction and the result follows.
For the “only if” direction, suppose that for all a,β ∈F(t,x), a,β ∈M(x). Then, clearly, for all
t′, t ◦∩◦t′ = /0, if con(a,M(y)) ∩pre(t′) ̸= /0 it must be that H(t′) = ε for, if not, then a would have
been moved to the out-places of t′ and, by the acyclicity of the Petri net, a ̸∈M(x). Using an inductive
argument, this is true for all transitions t′ with con(a,M(y))∩pre(t′) ̸= /0. This completes the proof.
2
Reversing a transition in a causally-respecting order is implemented in exactly the same way as in
backtracking, i.e., the tokens are moved from the out-places to the in-places of the transition, all bonds
created by the transition are broken, and the reversal eliminates the history function.


## Page 14


14
Reversible Computation in Petri nets
Figure 5: Causal Order example
Deﬁnition 8 Given a reversing Petri net (A,P,B,T,F), a state ⟨M,H⟩, and a transition t co-enabled in
⟨M,H⟩we write ⟨M,H⟩
t⇝c ⟨M′,H′⟩for M′ and H′ as in Deﬁnition 6.
An example of causal-order reversibility can be seen in Figure 5. Here we have two independent
transitions, t1 and t2 causally preceding transition t3. Assuming that transitions were executed in the
order t1, t2, t3, the example demonstrates a causally-ordered reversal where t3 is (the only transition that
can be) reversed, followed by the reversal of its two causes t1 and t2. In general these can be reversed in
any order although in the example t1 is reversed before t2.
We may now establish the causal consistency of our semantics, as in [5]. First we deﬁne some
auxiliary notions. In what follows we write 7−→c for −→∪⇝c.
Given a transition ⟨M,H⟩
t
7−→c ⟨M′,H′⟩, we say that the action of the transition is t if ⟨M,H⟩
t
−→
⟨M′,H′⟩and t if ⟨M,H⟩
t⇝c ⟨M′,H′⟩and we may write ⟨M,H⟩
t
7−→c ⟨M′,H′⟩. We use α to range over
{t,t | t ∈T} and write α = α. We extend this notion to sequences of transitions and, given an execution
⟨M0,H0⟩
t1
7−→c ...
tn
7−→c ⟨Mn,Hn⟩, we say that the trace of the execution is σ = α1;α2 ...;αn, where αi is
the action of transition ⟨Mi−1,Hi−1⟩
ti
7−→c ⟨Mi,Hi⟩, and write ⟨M,H⟩
σ
7−→c ⟨Mn,Hn⟩.
Deﬁnition 9 Two actions α1 and α2 are said to be concurrent if whenever ⟨M,H⟩
α1
7−→c ⟨M1,H1⟩and
⟨M,H⟩
α2
7−→c ⟨M2,H2⟩then ⟨M1,H1⟩
α2
7−→c ⟨M′,H′⟩and ⟨M2,H2⟩
α1
7−→c ⟨M′,H′′⟩.
Thus, two actions are concurrent if execution of the one does not preclude the other.
Deﬁnition 10 Causal equivalence on traces, denoted by ≍, is the least equivalence relation closed under
composition of traces such that (i) if α1 and α2 are concurrent actions then α1;α2 ≍α2;α1, and (ii)
α;α ≍ε.
The ﬁrst clause states that in two causally equivalent traces concurrent actions may occur in any order
and the second clause states that it is possible to ignore transitions that have occurred in both the forward
and the reverse order.
We additionally deﬁne a notion of history equivalence (overloading operator ≍), according to which
two histories H and H′ are equivalent if and only if they record the same executed transitions that have
not been reversed:
Deﬁnition 11 History equivalence, denoted by ≍, is deﬁned such that H ≍H′ holds whenever H(t) = k
for some k ∈N if and only if H′(t) = m for some m ∈N. We extend this notion to states and write
⟨M,H⟩≍⟨M,H′⟩if and only if H ≍H′.


## Page 15


A. Philippou & K. Psara
15
When it is clear from the context we drop the subscript in the above relations and simply write ≍for
all ≍e, ≍h and ≍s. We may now prove the following results.
Proposition 5 Given a RPN (A,P,B,T,F), an initial state ⟨M0,H0⟩and an execution ⟨M0,H0⟩
t1
7−→c
⟨M1,H1⟩
t2
7−→c ...
tn
7−→c ⟨Mn,Hn⟩, the following hold:
1. For all a ∈A and i, 0 ≤i ≤n, |{x ∈P | a ∈Mi(x)}| = 1.
2. For all β ∈B and i, 0 ≤i ≤n, 0 ≤|{x ∈P | β ∈Mi(x)}| ≤1, and,
(a) if ti is a forward transition with β ∈eﬀ(ti), then β ∈Mi(x) for some x ∈P and β ̸∈Mi−1(y)
for all y ∈P,
(b) if ti is a reversing transition with β ∈eﬀ(ti) then β ∈Mi−1(x) for some x ∈P and β ̸∈Mi(y)
for all y ∈P, and
(c) if β ̸∈eﬀ(ti) then β ∈Mi−1(x) if and only if β ∈Mi(x).
Proof:
The proof follows along the same lines as that of Proposition 3 with ⇝b replaced by ⇝c.
2
Lemma 2 (Loop) For any forward transition ⟨M,H⟩
t
−→⟨M′,H′⟩there exists a backward transition
⟨M′,H′⟩
t⇝c ⟨M,H⟩and vice versa.
Proof:
The proof follows along the same lines as that of Lemma 1 with ⇝b replaced by ⇝c.
2
The main result, Theorem 1 below, states that if we have two computations beginning in the same
initial state, then they lead to equivalent states if and only if the sequences of executed transitions of the
two computations are causally equivalent. Speciﬁcally, if two executions from the same state reach the
same marking by executing transitions σ1 and σ2 containing the same executed but not reversed actions,
then σ1 and σ2 are causally equivalent and vice versa. This guarantees the consistency of the approach
since reversing transitions is in a sense equivalent to not executing the transitions in the ﬁrst place.
Reversal will not give rise to previously unreachable states, on the contrary, it will give rise to exactly the
same markings and causally equivalent histories due to the different keys being possibly assigned due to
the different ordering or (lack of) reversal of transitions.
Theorem 1 Consider traces σ1 and σ2. Then, σ1 ≍σ2 if any only if ⟨M0,H0⟩
σ1
7−→c ⟨M,H⟩and ⟨M0,H0⟩
σ2
7−→c
⟨M,H′⟩where ⟨M,H⟩≍⟨M,H′⟩.
For the proof of Theorem 1 we employ the following intermediate results. The lemma below states
that causal equivalence allows the permutation of inverse transitions that have no causal relations between
them. Therefore, computations are allowed to reach for the maximum freedom of choice going backward
and then continue forward.
Lemma 3 Let σ be a trace. Then there exist traces r,r′ both forward such that σ ≍r;r′.
Proof:
We prove this by induction on the length of σ and the distance from the beginning of σ to the
earliest pair of transitions that contradicts the property r;r′. If there is no such contradicting pair then the
property is trivially satisﬁed. If not, we distinguish the following cases:
1. If the ﬁrst contradicting pair is of the form t;t then since t;t = ε, we may remove the two transitions
from the sequence. Thus, the length of σ decreases and the proof follows by induction.


## Page 16


16
Reversible Computation in Petri nets
2. If the ﬁrst contradicting pair is of the form t;t′ then we observe that t and t′ must be concurrent
transitions: Since action t′ is being reversed it implies that all the actions that are causally depen-
dent on it have either not been executed up to this point or they have already been reversed. This
implies that action t′ is not causally dependent on t and it can be executed before or after its execu-
tion. That is, action t is forward enabled, meaning that tokens exist to its input places irrespectively
of whether t′ has or has not been reversed. As a result t and t′ can be swapped, resulting in a later
earliest contradicting pair. Thus by induction the result follows.
2
From the above lemma we may conclude the following corollary establishing that causal-order re-
versibility is consistent with standard forward execution in the sense that RPNs will not generate states
that are unreachable in forward execution:
Corollary 1
Suppose that H0 is the initial history. If ⟨M0,H0⟩
σ
7−→c ⟨M,H1⟩and σ is a trace with both
forward and backward transitions if and only if there exists a transition ⟨M0,H0⟩
σ′
7−→c ⟨M,H2⟩and σ′ a
trace of forward transitions.
Proof:
Proving the “only if’ part of the corollary is trivial since every forward computation in RPNs can
be simulated in reversible RPNs by only moving forward. To prove the “if” part, according to Lemma 3,
σ ≍r;r′ where both r and r′ are forward traces. Since, however, H0 is the initial history it must be that
r is empty. This implies that ⟨M,H0⟩
r′
7−→c ⟨M′,H2⟩, H1 ≍H2 and r′ is a forward trace. Consequently,
writing σ′ for r′, the result follows.
2
Lemma 4
Suppose ⟨M,H⟩
σ1
7−→c ⟨M′,H1⟩and ⟨M,H⟩
σ2
7−→c ⟨M′,H2⟩, where H1 ≍H2 and σ2 is a forward
trace. Then, there exists a forward trace σ′
1 such that σ1 ≍σ′
1.
Proof:
If σ1 is forward then σ1 = σ′
1 and the result follows trivially. Otherwise, we may prove the
lemma by induction on the length of σ1. We begin by noting that, by Lemma 3, σ1 ≍r;r′. Let t;t′
be the two successive transitions in r;r′ with opposite directions. Given that σ2 is a forward transition
that simulates σ1, it must be that r′ contains a forward execution of transition t. If not, H2 will contain
a forward token for transition t and H1 a reverse token leading to a contradiction since, by deﬁnition,
it would not hold that H1 ≍H2. Consider the earliest occurrence of t in r′ and let t∗be any transition
between the reversal of t and this forward occurrence. Since t∗∈r′, t∗is a forward transition that is not
reversed in the computation. Consequently, t∗must also occur in σ2. As a result, we observe that t∗is
enabled both after a forward execution on t, as in σ2, as well as after a backward execution of t, as in
r,r′. Thus, it must be that t and t∗are concurrent transitions. Since this holds for any t∗between the
occurrences of t and t, this implies that we may permute t with each such t∗within the trace to yield
the sequence t;t. Since t;t ≍ε, we may remove the pair of opposite transitions and obtain a shorter
equivalent trace, also equivalent to σ2 and conclude by induction.
2
We may now proceed with the proof of Theorem 1:
Proof of Theorem 1:
Suppose ⟨M0,H0⟩
σ1
7−→c ⟨M,H⟩and ⟨M0,H0⟩
σ2
7−→c ⟨M,H′⟩with ⟨M,H⟩≍⟨M′,H′⟩.
We prove that σ1 ≍σ2 by using a lexicographic induction on a pair consisting of the sum of the lengths
of σ1 and σ2 and the depth of the earliest disagreement between them. By Lemma 3 we may suppose
that σ1 and σ2 are permutable to coincide with the property r;r′. Call t1 and t2 the earliest transitions
where they disagree. There are three main cases in the argument depending on whether these are forward
or backward.


## Page 17


A. Philippou & K. Psara
17
1. If t1 is backward and t2 is forward, we have σ1 = r;t1;u and σ2 = r;t2;v for some r,u,v. Lemma 4
applies to t2;v which is forward and t1;u which contains both forward and backward actions and
thus, by the lemma, it has a shorter forward equivalent. Thus, σ1 has a shorter forward equivalent
and the result follows by induction.
2. If t1 and t2 are both forward then it must be that case that σ1 = r;t1;u and σ2 = r;t2,v, for some r,
u, v, where t1 ∈v and t2 ∈u. This is the case since, if we consider the ﬁnal states of the executions
H ≍H′, holds. Consequently, since H(t1) ∈N, H2(t1) ∈N should also hold. In words, t1 must
also be executed by σ2 and similarly for t2 and σ1. The question that now arises is whether t1 and
t2 are concurrent. Applying the same arguments as in the proof of Lemma 4 we may conclude that
the occurrence of t1 in σ2 can be moved forward within u, yielding σ2 ≍r;t1;u′. This results in an
equivalent execution of the same length with a later earliest divergence than with σ2 and the result
follows by the induction hypothesis.
3. If t1 and t2 are both backward, we have σ1 = r;t1;u and σ2 = r;t2;v for some r,u,v. Suppose
that both u and v are minimized according to Lemma 4. Then it must be that both t1 and t2 are
executed in v and u respectively. We may then argue that, e.g. t1 can be moved forward within v
yielding σ2 ≍r;t1;v′ This results in an equivalent execution of the same length with a later earliest
divergence than with σ2 and the result follows by the induction hypothesis.
2
4.4
Out-of-causal-order Reversibility
Finally, we consider out-of-causal-order reversibility. Let us begin by considering the example of Fig-
ure 7. In the ﬁrst net shown in the ﬁgure, we see that transitions t1, t2, and t3 have been executed in
this order and now all tokens are in the ﬁnal place z. Suppose that transition t1 is reversed out of order.
As we have already discussed, the effect of this reversal should be the destruction of the bond between
a and b. This means that the component d−a−b−c is broken into the bonds d−a and b−c which
should backtrack within the Petri net to capture the reversal of the transition. Nonetheless, the tokens
of d−a must remain at place z. This is because a bond exists between them that has not been reversed
and was the effect of the immediately preceding transition t3. However, in the cases of b and c the bond
can be reversed to place y which is the place where the two tokens are connected and from where they
could continue to participate in any further computation requiring their coalition. Once transition t2 is
subsequently reversed, the bond between b and c is destroyed and thus the two tokens are able to return
to their initial places as shown in the third net in the ﬁgure. Finally, if transition t3 is reversed, the bond
between d and a breaks and given that neither of d and a are connected to other elements, the tokens
can return to their initial places. From this example we observe that in out-of-causal-order reversibility,
once a transition is reversed we must reverse all the bonds that it has created and reverse the tokens of all
components created by the broken bond as far backwards as possible.
We begin by noting that in out-of-causal order reversibility any executed transition can be reversed
at any time.
Deﬁnition 12 Consider a reversing Petri net (A,P,B,T,F), a state ⟨M,H⟩and a transition t ∈T. We say
that t is o-enabled in ⟨M,H⟩, if H(t) ∈N.
The effect of reversing a transition is that all bonds created by the transition are undone. This may
result in tokens backtracking in the net. In particular, if the reversal of a transition causes the destruction
of a bond which results in a coalition of bonds to be broken down into a set of subcomponents, then,
each of these coalitions should ﬂow back, as far back as possible, to the last transition in which this


## Page 18


18
Reversible Computation in Petri nets
Figure 6: Out-of-Causal-Order example
sub-coalition participated. To capture the notion of “as far backwards as possible” we introduce the
following:
Deﬁnition 13 Given a RPN (A,P,B,T,F), a history H, and a set of bases and bonds C we write:
last(C,H)
=



t,
if ∃t, post(t)∩C ̸= /0, H(t) ∈N,
̸ ∃t′, post(t′)∩C ̸= /0, H(t′) ∈N, H(t′) > H(t)
⊥, otherwise
Thus, last(C,H) is deﬁned as follows: If the component C has been manipulated by some previously-
executed transition, then last(C,H) is the last executed such transition. Otherwise, if no such transition
exists (e.g. because all transitions involving C have been reversed), then last(C,H) is undeﬁned. Transi-
tion reversal in an out-of-causal order can thus be deﬁned as follows:
Deﬁnition 14 Given a RPN (A,P,B,T,F), an initial marking M0, a state ⟨M,H⟩and a transition t that is
o-enabled in ⟨M,H⟩, we write ⟨M,H⟩
t⇝o ⟨M′,H′⟩where H′ is deﬁned as in Deﬁnition 6 and we have:
M′(x)
=
M(x)−eﬀ(t)−{Ca,x | ∃a ∈M(x),x ∈t′◦,t′ ̸= last(Ca,x,H′)}
∪{Ca,y | ∃a,y, a ∈M(y),last(Ca,y,H′) = t′,F(t′,x)∩Ca,y ̸= /0}
∪{Ca,y | ∃a,y, a ∈M(y),last(Ca,y,H′) = ⊥,Ca,y ⊆M0(x)}
where we use the shorthand Cb,z = con(b,M(z)−eﬀ(t)) for b ∈A, z ∈P.
Thus, when a transition t is reversed in an out-of-order fashion all bonds that were created by the
transition in eﬀ(t) are undone. If the destruction of a bond divides a component into smaller connected
components then each of these components should be relocated (if needed) back to the place where the
complex would have existed if transition t never took place, i.e., exactly after the last transition that
involves tokens from the sub-complex. Speciﬁcally, the deﬁnition of M′ states that: If a token a and its
connected components last participated in some transition with out-place x other than y, then the sub-
component is removed from place y and returned to place x, otherwise it is returned to the place where it
occurred in the initial marking.
We may prove the following result where we write 7−→o for −→∪⇝o.
Proposition 6 Given a RPN (A,P,B,T,F), an initial state ⟨M0,H0⟩, and an execution ⟨M0,H0⟩
t1
7−→o
⟨M1,H1⟩
t2
7−→o ...
tn
7−→o ⟨Mn,Hn⟩. The following hold:


## Page 19


A. Philippou & K. Psara
19
1. For all a ∈A and 0 ≤i ≤n, |{x ∈P | a ∈Mi(x)}| = 1, and, if a ∈Mi(x) and t = last(con(a,Mi(x)),Hi),
if t = ⊥then x is such that a ∈M0(x), otherwise x ∈t◦and con(a,Mi(x))∩F(t,x) ̸= /0.
2. For all β ∈B and i, 0 ≤i ≤n, 0 ≤|{x ∈P | β ∈Mi(x)}| ≤1, and,
(a) if ti is a forward transition with β ∈eﬀ(ti) then β ∈Mi(x) for some x ∈P and β ̸∈Mi−1(y)
for all y ∈P,
(b) if ti is a reverse transition with β ∈eﬀ(ti) then β ∈Mi−1(x) for some x ∈P and β ̸∈Mi(y)
for all y ∈P, and
(c) if β ̸∈eﬀ(ti), β ∈Mi−1(x) if and only if β ∈Mi(x).
Proof:
Consider a RPN (A,P,B,T,F), an initial state ⟨M0,H0⟩and an execution ⟨M0,H0⟩
t1
7−→o ⟨M1,H1⟩
t2
7−→o
...
tn
7−→o ⟨Mn,Hn⟩. The proof is by induction on n.
Base Case.
For n = 0, by our assumption of token uniqueness, for all a ∈A, |{x ∈P | a ∈M0(x)}| = 1,
and, for all β ∈B , 0 ≤|{x ∈P | β ∈Mi(x)}| ≤1.
Induction Step.
Suppose the claim holds for all i, 0 ≤i < n and consider transition tn. Two cases exist,
depending on whether tn is a forward or a reverse transition:
• Suppose that tn is a forward transition. Then, by Proposition 4 for all a ∈A, |{x ∈P | a ∈Mn(x)}| =
1. Furthermore, we may show that if a ∈Mn(x) either t = last(con(a,Mn(x)),Hn) and x ∈t◦, or t =
⊥and x is such that a ∈M0(x) : On the one hand, if a ∈con(b,Mn−1(y)) for some b ∈F(tn,x), then
clearly t = last(con(a,Mn−1(y))) and a ∈Mn(x), x ∈t◦. On the other hand, if a ̸∈con(b,Mn−1(x))
for all b, y where b ∈F(tn,y), then a ∈Mn(y) for the place y such that a ∈Mn−1(y) and, by the
induction hypothesis if t = last(con(a,Mn(y))), then clearly t ̸= tn since tn ∩con(a,Mn−1(y)) = /0,
and the result follows by induction. Regarding clause (2), again by Proposition 4, for all β ∈B,
0 ≤|{x ∈P | β ∈Mn(x)}| ≤1, and if β ∈eﬀ(tn) then β ∈Mn(x) for some x ∈P and β ̸∈Mn−1(y)
for all y ∈P.
• Suppose that tn is a reverse transition and let a ∈A. Two cases exist:
– a ∈Cb,x = con(b,Mn−1(x)−eﬀ(tn)), where last(Cb,x,Hn) = t, and x ̸∈t◦or last(Cb,x,Hn) =
⊥. First, let us suppose that last(Cb,x,Hn) = t ̸= ⊥. Note that, by the induction hypothesis,
x must be the unique place in Mn−1 with a ∈Mn−1(x). Then, by Deﬁnition 14, a ̸∈Mn(x)
and a ∈Mn(y) where y ∈t◦such that Cb,x ∩F(t,y) ̸= /0. Suppose y is not unique, i.e., there
exists some y′ ̸= y with Cb,x ∩F(t,y′) ̸= /0. Further, suppose that c ∈Cb,x ∩F(t,y) and d ∈
Cb,x ∩F(t,y′). By the deﬁnition of last(C,H), we may conclude that H(t) ̸= ε, and thus t = ti
for some i < n. Note that during the (forward) execution of the transition, by Deﬁnition 4(3),
c ̸∈con(d,Mi−1(y)) for all y ∈◦ti. This implies that during the execution of ti+1,...tn, some
transition(s) created a connection between c and d, as existing inCb,x. Thus, there must exist a
transition j, i < j ≤n, with (c′,d′) ∈eﬀ(t), c′ ∈con(c,Mj−1(xj−1)), d′ ∈con(d,Mj−1(yj−1)),
xj−1,yj−1 ∈◦tj. However, this contradicts the choice of t = ti = last(Cb,x,Hn) since clearly t j
is a transition following ti and operating on Cb,x. Consequently, we conclude that y is unique.
Thus |{x ∈P | a ∈Mn(x)}| = |{y} = 1 and, furthermore, y ∈t◦, t = last(Cb,x,Hn(x)). On the
other hand, if last(Cb,x,Hn) = ⊥, by Deﬁnition 4 C ⊆Mn(y), if C ⊆M0(y). As before, y is
well deﬁned and unique because, no transition could have created the connections of C by
the deﬁnition of last() and the assumption of token uniqueness.


## Page 20


20
Reversible Computation in Petri nets
– a ∈Cb,x = con(b,Mn−1(x) −eﬀ(tn)), where last(Cb,x,Hn) = t, and x ∈t◦. Note that, by the
induction hypothesis, x must be the unique place in Mn−1 with a ∈Mn−1(x). Furthermore, by
Deﬁnition 14, a ∈Mn(x) and a ̸∈Mn(y) for all y ̸= x.
Now, let β ∈B. If tn is a forward transition and β ∈eﬀ(t), the result follows from Proposition 4. If
tn is a reverse transition and β ∈eﬀ(t), it is straightforward to see that β ̸∈Mn(x) for all x. Finally,
if β ̸∈eﬀ(t), we may see that β ∈Mn−1(x) if and only if β ∈Mn(x). This completes the proof. 2
We may now conﬁrm that during out-of-causal-order reversing, connected components are back-
tracked to the place where the components occurred as a stand-alone element in the last state of the
execution. Note that the component may have come into place various times during the forward and
backward execution of transitions and even into various places due to possible nondeterminism in the
Petri net. However, our semantics combined with the deﬁnition of last(C,H,M,M0) ensures that reversal
of an action moves the component to the place where it has last been used. In what follows we write
7−→o for −→∪⇝o.
We begin with a useful deﬁnition.
Deﬁnition 15 Consider executions ⟨M0,H0⟩
σ1
7−→o ⟨M1,H1⟩and ⟨M0,H0⟩
σ2
7−→o ⟨M2,H2⟩and a set of
bases and bonds C = con(a,M1(x)) ∩con(a,M2(y)) for some a ∈A and x, y ∈P. We deﬁne the fol-
lowing:
1. Traces σ1 and σ2 are C-equivalent, σ1 ≍C σ2, if last(C,H1) = last(C,H2).
2. Histories H1 and H2 are C-equivalent, H1 ≍C H2, if last(C,H1) = last(C,H2).
3. Markings M1 and M2 are C-equivalent, M1 ≍C M2, if x = y.
4. States ⟨M1,H1⟩and ⟨M2,H2⟩are C-equivalent, ⟨M1,H1⟩≍C ⟨M2,H2⟩, if M1 ≍C M2 and H1 ≍C H2.
Thus, two traces are considered to be C-equivalent for a component of tokens/bonds C when they
have the same last transition manipulating C (which could be undeﬁned if none of the transitions have
manipulated C). C-equivalence on histories is deﬁned in the same way whereas two markings are C-
equivalent if they contain component C in the same place. The notion is extended to states in the expected
manner.
The main result, Theorem 2 below, states that if we have two computations beginning in the same
initial state, then they lead the complex C to the same place if and only if the sequences of executed
transitions of the two computations are C-equivalent.
Theorem 2 Consider executions ⟨M0,H0⟩
σ1
7−→o ⟨M1,H1⟩and ⟨M0,H0⟩
σ2
7−→o ⟨M2,H2⟩and a complex of
bonds or bases C. Then, σ1 ≍C σ2 if and only if ⟨M1,H1⟩≍C ⟨M2,H2⟩
Proof:
Consider sequences of transitions ⟨M0,H0⟩
σ1
7−→o ⟨M1,H1⟩and ⟨M0,H0⟩
σ2
7−→o ⟨M2,H2⟩and a
complex of bonds and bases C, as speciﬁed by the theorem. First, let us assume that σ1 ≍C σ2. This
implies that last(C,H1) = last(C,H2) which also implies that H1 ≍C H2. To show that M1 ≍C M2 we
consider the following two cases:
• last(C,H1) = last(C,H2) = ⊥: By Proposition 6, C ⊆M1(x) and C ⊆M2(x) where C ⊆M0(x).
This implies that M1 ≍C M2, as required.
• last(C,H1) = last(C,H2) = t: By Proposition 6, for all a ∈C, a ∈M1(x), where a ∈t1◦, for
t1 = last(C,H1), C ∩F(t1,x) ̸= /0 and, similarly, a ∈M2(y), where a ∈t2◦, for t2 = last(C,H2),
C∩F(t2,y) ̸= /0. Since t = t1 = t2, x = y, thus C ⊆M1(x) and C ⊆M2(x) for some x, which implies
that M1 ≍C M2, as required.


## Page 21


A. Philippou & K. Psara
21
For the “only if” part of the theorem we observe that since ⟨M1,H1⟩≍C ⟨M2,H2⟩, H1 ≍C H2 and last(C,H1) =
last(C,H2). Then, by deﬁnition, σ1 ≍C σ2, and the result follows.
2
From this theorem we conclude the following corollary establishing that executing two causally-
equivalent sequences of transitions in the out-of-causal setting will give rise to causally equivalent states.
Corollary 2
Consider executions ⟨M0,H0⟩
σ1
7−→o ⟨M1,H1⟩and ⟨M0,H0⟩
σ2
7−→o ⟨M2,H2⟩. If σ1 ≍σ2 then
⟨M1,H1⟩≍⟨M2,H2⟩.
Proof:
Let us suppose that σ1 ≍σ2 and ⟨M0,H0⟩
σ1
7−→o ⟨M1,H1⟩and ⟨M0,H0⟩
σ2
7−→o ⟨M2,H2⟩. Suppose
C is a connected component in ⟨M1,H1⟩, i.e. C = con(a,M1(x)) for some x ∈P, a ∈A. Since σ1 ≍σ2,
H1 ≍H2. Furthermore, it must be that σ1 ≍C σ2. If not, then t1 = last(C,σ1) ̸= last(C,σ2) = t2 and t1,
t2 concurrent actions. However, note that t1 and t2 are transitions both manipulating C and their effect is
to forward C from the inplaces to the outplaces of the transitions. If these transitions are concurrent, and
therefore simultaneously enabled, and by the uniqueness of tokens, it must be that they share common
inplaces. Furthermore, being concurrent implies that they can be executed in any order. For this to hold,
each transition should forward C back to its inplaces to allow the other transition to ﬁre. However, by the
assumption of acyclicity of RPNs, this is not possible. Thus, we conclude that t1 = t2 which implies that
σ1 ≍C σ2 and, by Theorem 2, C ⊆M2(x). Since this argument holds for any component C, we deduce
that M1 = M2 and the result follows
In addition, the following corollary establishes that out-of-causal-order reversibility is consistent with
standard forward execution in the sense that out-of-causal reversibility will never return tokens to places
that are unreachable during forward execution.
Corollary 3
Consider executions ⟨M0,H0⟩
σ1
7−→o ⟨M1,H1⟩and ⟨M0,H0⟩
σ2
7−→o ⟨M2,H2⟩where σ1 is a
trace with both forward and backward transitions and σ2 is a trace with only forward transitions and
σ1 ≍C σ2. Then, for x ∈P, C ⊆M1(x) if and only if C ⊆M2(x).
Proof:
From Theorem 2 we know that since σ1 ≍C σ2, M1 ≍C M2. Thus, C ⊆M1(x), implies that
C ⊆M2(x) and the result follows.
2
Finally, we state the following result that demonstrates the relation between the three forms of re-
versibility, as proposed for RPN’s.
Proposition 7
⇝b⊂⇝c⊂⇝o.
Proof:
To prove the proposition consider a RPN (A,P,B,T,F), a state ⟨M,H⟩and suppose that tran-
sition t is bt-enabled and ⟨M,H⟩
t⇝b ⟨M′,H′⟩. Then, by deﬁnition of bt-enabledness, H(t) > H(t′) for
all t′ ̸= t, H(t) ∈N. This implies that t is also co-enabled, and by the deﬁnition of ⇝c, we conclude that
⟨M,H⟩
t⇝b ⟨M′,H′⟩. It is easy to see that the inclusion is strict, as for example illustrated in Figure 4.
For the second inclusion, let us suppose that transition t is co-enabled and ⟨M,H⟩t⇝c ⟨M1,H1⟩. Then,
by the deﬁnition of o-enabledness, t is o-enabled. Suppose ⟨M,H⟩
t⇝o ⟨M2,H2⟩. It is easy to see that in
fact H1 = H2 (the two histories are as H with the exception that H1(t) = H2(t) = ε). It remains to show
that M1 = M2.
Let a ∈A. We must show that a ∈M1(x) if and only if a ∈M2(x). Two cases exist:
• If a ̸∈con(b,M(y)) for all b ∈A, y ∈t◦, then a ∈M1(x) and a ∈M2(x) such that a ∈M(x).


## Page 22


22
Reversible Computation in Petri nets
• If a ∈con(b,M(y)) for some b ∈A, y ∈t◦, then consider x ∈◦t with con(a,M(y)) ∩F(x,t) ̸= /0.
Such a place exists, by Deﬁnition 2(3), and it is unique, by the assumption of uniqueness of tokens.
Note that by Deﬁnition 6, a ∈M1(x). Consider t′ such that x ∈t′◦and F(t′,x)∩con(a,M(y)) ̸= /0.
If such a transition exists by observing that t′ would not have been co-enabled since H(t) ̸= ε and
t′ and t manipulate common tokens in con(a,M(y)), we conclude that last(con(a,M(y)),H) = t′.
As a result a ∈M2(x), as required. On the other hand, if such a t′ does not exist, then it must be that
last(con(a,M(y)),H) = ⊥and, by the deﬁnition of ⇝o, a ∈M2(x) where a ∈M(x) as required.
Now let β ∈B. We must show that β ∈M1(x) if and only if β ∈M2(x). Two cases exist:
• If β ̸∈con(b,M(y)) for all b ∈A, y ∈t◦, then β ∈M1(x) if and only if β ∈M(x) if and only if
β ∈M2(x).
• If β ∈con(b,M(y)) for some b ∈A, y ∈t◦, then, if also β ∈eﬀ(t), then β ̸∈M1(x) for all x ∈P and,
similarly, for M2. If, however, β ̸∈eﬀ(t), then consider x ∈◦t with con(a,M(y)−eﬀ(t))∩F(x,t) ̸=
/0. Such a place exists, by Deﬁnition 2(3), and it is unique, by the assumption of uniqueness
of tokens. Note that by Deﬁnition 6, β ∈M1(x). Consider t′ such that x ∈t′◦and F(t′,x) ∩
con(a,M(y) −eﬀ(t)) ̸= /0. If such a transition exists by observing that t′ would not have been
co-enabled since H(t) ̸= ε and t′ and t manipulate common tokens in con(a,M(y) −eﬀ(t)), we
conclude that last(con(a,M(y)−eﬀ(t)),H) = t′. As a result a ∈M2(x), as required. On the other
hand, if such a t′ does not exist, then it must be that last(con(a,M(y)−eﬀ(t)),H) = ⊥and, by the
deﬁnition of ⇝o, a ∈M2(x) where a ∈M(x) as required.
Again, we may observe that the inclusion is strict given that out-of-causal reversal allows to reverse all
executed transitions and not only those whose effects have been undone. This completes the proof.
2
In the following example we illustrate how reversing Petri nets featuring out-of-causal-order re-
versibility can be used for modelling a simpliﬁed transactional system.
Example 1
Transaction processing manages sequences of operations, also called transactions, that can
either succeed or fail as a complete unit. Speciﬁcally, a long-running transaction consists of a sequence
of steps. Each of these steps may either succeed, in which case the ﬂow of control moves on to the next
atomic step in the sequence, or it may fail, in which case a compensating transaction is often used to
undo failed transactions and restore the system to a previous state. If all steps of the transaction execute
successfully then the transaction is considered as successful and it is committed.
In Figure 7 we consider a model of such a transaction. Due to the size of the net we restrict our
attention to a transaction with only one step which nonetheless illustrates sufﬁciently the mechanisms
needed to model the system. The intuition is as follows: for the execution of the transaction to commence
it is necessary for token i to be available. This token is bonded with token a in which case transition a
can be executed with the effect of creating the bond i−a in place u. At this stage there are two possible
continuations. The ﬁrst possibility is that the bond i−a will participate in transition s which models
the successful completion of step a as well as the transaction, yielding the bond i−a−s. The second
possibility is that step a fails. In this case, token f comes in place and the failure is implemented via
transitions f1 and f2 as follows: To begin with in action f1, token f is bonded with token a, whereas in
action f2 token i is bonded with token f. At this stage the compensation comes in place (token c) where
the intention is that step a should be undone. In our model, this involves undoing transition a. Note that
this will have to be done according to our out-of-causal-order deﬁnition since transition a was followed
by f1 and f2 which have not been undone. Only once this is accomplished, will the precondition of
transition c, namely a, be enabled. In this case, transition c can be executed leading to the creation of
bond i−c in place z.


## Page 23


A. Philippou & K. Psara
23
Figure 7: Transaction processing
Figure 7 shows a possible execution of the system beginning at the state where the sequence of
transitions a; f1; f2 has already taken place. Next, computation can not go forward as already explained,
but, as illustrated in the ﬁrst transition in the ﬁgure, transition a may be reversed, causing the destruction
of bond i−a. Next, transition f1 is reversed, causing the destruction of bond a−f, in which case token
a can return to its initial place, capturing that the step has been reversed. At this stage transition c can
be executed in the forward direction leading to the execution of the compensation. In the ﬁnal step, f2 is
reversed causing the reversal of the bond i−f and recovering the failure token back to its initial place.
5
Conclusions
This paper proposes a reversible approach to Petri nets that allows the modelling of reversibility as re-
alised by backtracking, causal reversing and out-of-causal-order reversing. To the best of our knowledge,
this is the ﬁrst such proposal, since the only related previous work of [2, 3], having a different aim, im-
plemented a very liberal way of reversing computation in Petri nets by introducing additional reversed
transitions. Indeed, our proposal allows systems to reverse at any time leading to previously visited states
or even to new ones without the need of additional forward actions. Moreover, this interpretation of Petri
nets has the capability for reversing without the need of an extensive memory.


## Page 24


24
Reversible Computation in Petri nets
Indeed, good models that can be easily understood and simulated, even by scientists with expertise
outside Computer Science, can prove very useful to understand complex systems. In particular, the
expressive power and visual nature offered by Petri nets coupled with reversible computation has the
potential of providing an attractive setting for studying, analysing, or even imagining alternatives in a
wide range of systems.
In our current research we are investigating the expressiveness relationship between RPNs and
coloured PNs where we expect that the global control implemented by histories can be encoded in
coloured PNs using additional transitions and places. We aim to provide and prove the correctness
of such a translation and analyse the associated trade-off in terms of Petri net size. Furthermore, we are
working on relaxing the restrictions we imposed in the RPN model of the present work such as allowing
multiple tokens of the same base/type to occur in a model, as well as the addition of cycles. Note that the
addition of cycles can in fact be achieved within our model by adopting histories in the form of a stack
for each transition that recalls all previous occurrences of the transition.
As future work, we are planning to extend our formalism by considering approaches for controlling
reversibility, as for instance in [6, 14, 11]. We plan to explore this direction with the use of probabilities
that can capture the likelihood of a transition executing in the forward or backward direction [1]. Finally,
we would like to further apply our framework in the ﬁelds of biochemistry and long-running transactions.
Acknowledgents: This research was partially supported by the EU COST Action IC1405. We are
grateful to K. Barylska, A. Gogolinska, L. Mikulski, and M. Piatkowski for interesting discussions on
previous drafts of this work.
References
[1] G. Bacci, V. Danos, and O. Kammar. On the statistical thermodynamics of reversible communicating pro-
cesses. In Proceedings of CALCO 2011, LNCS 6859, pages 1–18. Springer, 2011.
[2] K. Barylska, M. Koutny, L. Mikulski, and M. Piatkowski. Reversible computation vs. reversibility in Petri
nets. In Proceedings of RC 2016, LNCS 9720, pages 105–118. Springer, 2016.
[3] K. Barylska, L. Mikulski, M. Piatkowski, M. Koutny, and E. Erofeev. Reversing transitions in bounded
Petri nets. In Proceedings of CS&P 2016, volume 1698 of CEUR Workshop Proceedings, pages 74–85.
CEUR-WS.org, 2016.
[4] L. Cardelli and C. Laneve. Reversible structures. In Proceedings of CMSB 2011, pages 131–140. ACM,
2011.
[5] V. Danos and J. Krivine. Reversible communicating systems. In Proceedings of CONCUR 2004, LNCS
3170, pages 292–307. Springer, 2004.
[6] V. Danos and J. Krivine. Transactions in RCCS. In Proceedings of CONCUR 2005, LNCS 3653, pages
398–412. Springer, 2005.
[7] V. Danos and J. Krivine. Formal molecular biology done in CCS-R. Electronic Notes in Theoretical Computer
Science, 180(3):31–49, 2007.
[8] S. Kuhn and I. Ulidowski. A calculus for local reversibility. In Proceedings of RC 2016, LNCS 9720, pages
20–35. Springer, 2016.
[9] R. Landauer. Irreversibility and heat generation in the computing process. IBM Journal of Research and
Development, 5(3):183–191, 1961.
[10] I. Lanese, M. Lienhardt, C. A. Mezzina, A. Schmitt, and J. Stefani. Concurrent ﬂexible reversibility. In
Proceedings of ESOP 2013, LNCS 7792, pages 370–390. Springer, 2013.
[11] I. Lanese, C. A. Mezzina, A. Schmitt, and J. Stefani. Controlling reversibility in higher-order pi. In Proceed-
ings of CONCUR 2011, LNCS 6901, pages 297–311. Springer, 2011.


## Page 25


A. Philippou & K. Psara
25
[12] I. Lanese, C. A. Mezzina, and J. Stefani. Reversibility in the higher-order π-calculus. Theoretical Computer
Science, 625:25–84, 2016.
[13] I. Phillips and I. Ulidowski. Reversing algebraic process calculi. In Proceedings of FOSSACS 2006, LNCS
3921, pages 246–260. Springer, 2016.
[14] I. Phillips, I. Ulidowski, and S. Yuen. A reversible process calculus and the modelling of the ERK signalling
pathway. In Proceedings of RC 2012 Revised Papers, LNCS 7581, pages 218–232. Springer, 2012.
[15] I. Phillips, I. Ulidowski, and S. Yuen. Modelling of bonding with processes and events. In Proceedings of
RC 2013, LNCS 7947, pages 141–154. Springer, 2013.
[16] D. G. Stork and R. J. van Glabbeek. Token-controlled place reﬁnement in hierarchical Petri nets with appli-
cation to active document workﬂow. In Proceedings of ICATPN 2002, LNCS 2360, pages 394–413. Springer,
2002.
[17] I. Ulidowski, I. Phillips, and S. Yuen. Concurrency and reversibility. In Proceedings of RC 2014, LNCS
8507, pages 1–14. Springer, 2014.
[18] R. J. van Glabbeek. The individual and collective token interpretations of Petri nets. In Proceedings of
CONCUR 2005, LNCS 3653, pages 323–337. Springer, 2005.
[19] R. J. van Glabbeek, U. Goltz, and J. Schicke. On causal semantics of Petri nets. In Proceedings of CONCUR
2011, LNCS 6901, pages 43–59. Springer, 2011.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]