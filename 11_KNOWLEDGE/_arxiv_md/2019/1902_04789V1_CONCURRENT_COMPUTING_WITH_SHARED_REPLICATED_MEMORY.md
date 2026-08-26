---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1902.04789v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1902.04789v1_Concurrent_Computing_with_Shared_Replicated_Memory

> Source: 1902.04789v1_Concurrent_Computing_with_Shared_Replicated_Memory.pdf

> Pages: 23

---


## Page 1


arXiv:1902.04789v1  [cs.DC]  13 Feb 2019
Concurrent Computing with Shared Replicated Memory⋆
Rigorous Speciﬁcation and Analysis Using Concurrent Communicating
Abstract State Machines
Klaus-Dieter Schewe1, Andreas Prinz2, Egon B¨orger3
1 Zhejiang University, UIUC Institute, China, kdschewe@acm.org
2 University of Agder, Department of ICT, Agder, Norway, andreas.prinz@uia.no
3 Universit`a di Pisa, Dipartimento di Informatica, Pisa, Italy, boerger@di.unipi.it
Abstract. The behavioural theory of concurrent systems states that any concurrent system
can be captured by a behaviourally equivalent concurrent Abstract State Machine (cASM).
While the theory in general assumes shared locations, it remains valid, if diﬀerent agents can
only interact via messages, i.e. sharing is restricted to mailboxes. There may even be a strict
separation between memory managing agents and other agents that can only access the shared
memory by sending query and update requests to the memory agents. This article is dedicated
to an investigation of replicated data that is maintained by a memory management subsystem,
whereas the replication neither appears in the requests nor in the corresponding answers. We
show how the behaviour of a concurrent system with such a memory management can be speciﬁed
using concurrent communicating ASMs. We provide several reﬁnements of a high-level ground
model addressing diﬀerent replication policies and internal messaging between data centres. For
all these reﬁnements we analyse their eﬀects on the runs such that decisions concerning the
degree of consistency can be consciously made.
1
Introduction
Abstract State Machines (ASMs) have been used since their discovery in the 1990s to model
sequential, parallel and concurrent systems (see [10, Ch. 6, 9]). For sequential systems the
celebrated sequential ASM thesis [14] provides an elegant theoretical underpinning showing
that every sequential algorithm as stipulated by three simple, intuitive postulates are captured
by sequential ASMs. This was generalised in [11] for (synchronous) parallel systems4, and in
[7] for asynchronous concurrent systems5, in which a concurrent system is deﬁned by a family
of algorithms assigned to agents that is subject to a concurrency postulate6.
This characterisation can be applied to many diﬀerent models of concurrent computation
(see e.g. [1,3,12,18,25,26]). While the thesis has been grounded on the assumption that shared
locations are used, it was shown in [8] that the theory remains valid, if diﬀerent agents can
only interact via messages, i.e. sharing is restricted to mailboxes. This includes the case of
a strict separation between memory managing agents and other agents that can only access
the shared memory by sending query and update requests to the memory agents. Naturally,
⋆The research reported in this article was partly supported by the Austrian Science Fund for the project
Behavioural Theory and Logics for Distributed Adaptive Systems (FWF: [P26452-N15]).
4 The behavioural theory proven by Ferrarotti et al. simpliﬁes the previously developed parallel ASM thesis
[4,5] by exploiting the idea of multiset comprehension terms in bounded exploration witnesses, which was
stimulated by previous research on non-deterministic database transformations [23,24].
5 This closed the gap in the behavioural theory of concurrent systems, as the deﬁnition of partially ordered
runs in [13] was generally considered to be insuﬃcient. There are examples of concurrent systems satisfying
the intuitively clear property of sequential consistency [16] without having partially ordered runs.
6 Though the proof of the concurrent ASM thesis was ﬁrst only conducted for families of sequential algorithms,
the generalisation to families of parallel algorithms does not cause serious diﬃculties as sketched in [22].


## Page 2


the expectation of an agent a sending a request to a memory management agent b is that the
result is the same as if there had been a concurrent run with agent a executing its request
directly on the shared locations.
However, as observed in [20] this expectation can be violated by relaxed shared memory
management, in particular in combination with conﬂicting updates or data replication. Re-
garding conﬂicting updates, if agents a and a′ try simultaneously to update the value at a
location ℓto some new values v and v′, respectively, with v ̸= v′, a concurrent run would be
discarded. Instead of this, a memory management agent b receiving update requests from a
and a′ might randomly choose one of the possible values v or v′, so for one of the agents there
would be a lost update and its latest step would not have been executed properly.
Therefore, in [7] it is requested that “if the eﬀects of such techniques are behaviourally
relevant for the problem . . . , then this should be described by a precise model through which
a programmer can understand, check and justify that the code does what it is supposed to
do”. For the random selection such a precise model can be easily deﬁned by a memory agent
m with the following rule7:
FORALL ℓWITH ∃v.(ℓ, v) ∈∆CHOOSE v ∈{v′ | (ℓ, v′) ∈∆} IN ℓ:= v
If this behaviour is known, one can specify what an agent should do in case of possibly lost
updates, e.g. use strict transactions to avoid the situation to arise8, or integrate algorithms
for mutual exclusion [2,17], or ensure that an agent only continues after the memory agent m
(considered as part of the environment [10]) has terminated its step, etc.
In this article we investigate the case of replicated data maintained by a memory man-
agement subsystem, where the replication should not appear in the requests nor in the corre-
sponding answers, which is a standard requirement in distributed databases with replication
[19, Chap.13, pp.459ﬀ.]. Consider ﬁrst an example of undesirable behaviour with four agents
a1, . . . , a4 having the following respective programs (where ; denotes sequential execution, and
Print(x) means to read the value x and to copy it to some output):
x := 1 | y := 1 | Print(x); Print(y) | Print(y); Print(x)
Then there is no concurrent run where (1) initially x = y = 0, (2) each agent makes once
each possible move, (3) a3 prints x = 1, y = 0, and (4) a4 prints x = 0, y = 1. However, if x
and y are replicated, say that there are always two copies, and an update by the programs a1
or a2 aﬀects only a single copy, such a behaviour will indeed be enabled.
Therefore, our objective is that such behaviour must be understandable from the speciﬁca-
tion so that the developer of the system can see, whether the consequences of such behaviour
can be tolerated or additional consistency assurance measures have to be included. We as-
sume a rather simple model, where shared data is logically organised in relations with primary
keys, and data can only be accessed by means of the primary key values. We further assume
relations to be horizontally fragmented according to values of a hash function on the pri-
mary key values, and these fragments are replicated. Replicas are assigned to diﬀerent nodes,
and several nodes together form a data centre, i.e. that are handled by one dedicated data
management agent9.
7 Here a shared (set-valued) function symbol ∆denoting an update set is used.
8 See e.g. [9] for an ASM speciﬁcation of concurrent systems with transactional behaviour.
9 This is similar to the data organisation in the noSQL database system Cassandra [21], but otherwise the
Cassandra system is of no importance for this article. We may think of nodes as storage units and of data
centres as physical machines managing them.
2


## Page 3


In addition, values in replicas carry logical timestamps set by the data centres and stored in
the records in the nodes of the memory management subsystem. We further adopt Lamport’s
simple approach for the maintenance of timestamps [15], which basically advances a clock, if
its data centre receives a record with a future timestamp. This allows us to formulate and
investigate policies that guarantee certain to-be-speciﬁed levels of consistency (as known from
replication in relational databases).
For retrieval of a set of records a speciﬁed number of replicas has to be read, and for
each record always the one with the latest timestamp will be returned. Depending on how
many replicas are accessed the returned records may be (in the strict sense) outdated or
not. Likewise, for the update of a set of records timestamps will be created, and a speciﬁed
number of replicas of the records will be stored. Success of retrieval or update will be returned
according to speciﬁed read- and write-policies.
In Section 2 we will ﬁrst specify the behaviour of a concurrent system with shared data
requiring that all agents interact with this subsystem for data retrieval and updates using
appropriate SEND and RECEIVE actions. The memory management subsystem will be speciﬁed
by a separate collection of agents. In Section 3 we investigate a reﬁnement concerning policies
how many replicas are to be read or updated, respectively. We show that some combinations
of replication policies enable view compatibility, i.e. data consistency, which formalises the
expectation above. In Section 4 we reﬁne our speciﬁcation taking the communication between
data centres into account, and address the enforcement of the read and write policies. We
obtain a complete, though not necessarily correct reﬁnement, and as a consequence view
compatibility cannot be guaranteed anymore. In fact, we even show that view compatibility
implies view serialisability. That is, without exploiting the possibility of transactions—at least
for single read or write requests—consistency cannot be preserved. Finally, we conclude with
a brief summary and outlook.
2
Ground Model for Shared Memory Management with Replication
We assume some familiarity with Abstract State Machines (ASMs), which can be understood
as a form of pseudo-code with well-founded semantics10. The signature Σ of an ASM is a ﬁnite
set of function symbols f, each associated with an arity arf. A state S is a set of functions fS
of arity arf over some ﬁxed base set B, given by interpretations of the corresponding function
symbol f. Each pair (f, (v1, . . . , varf )) comprising a function symbol and arguments vi ∈B is
called a location, and each pair (ℓ, v) of a location ℓand a value v ∈B is called an update. A
set of updates is called an update set. The evaluation of terms is deﬁned as usual by
valS(f(t1, . . . , tarf )) = fS(valS(t1), . . . , valS(tarf )).
We say that fS(valS(t1), . . . , valS(tarf )) is the value at location (f, (valS(t1), . . . , valS(tarf )))
in state S. ASM rules r are composed using
assignments. f(t1, . . . , tarf ) := t0 (with terms ti built over Σ),
branching. IF ϕ THEN r+ ELSE r−,
parallel composition. FORALL x WITH ϕ(x) r(x),
bounded parallel composition. r1 . . . rn,
10 Here we do not repeat the formal deﬁnition of the semantics of ASMs—detailed deﬁnitions can be found in
the textbook [10, Sect.2.2/4].
3


## Page 4


choice. CHOOSE x WITH ϕ(x) IN r(x), and
let. LET x = t IN r(x).
Each rule yields an update set ∆(S) in state S. If this update set is consistent, i.e. it does
not contain two updates (ℓ, v), (ℓ, v′) with the same location ℓand diﬀerent values v ̸= v′,
then applying this update set deﬁnes a successor state S + ∆(S).
Regarding the function symbols in Σ we further distinguish static, dynamic and derived
functions. Only dynamic function symbols can appear as the outermost symbol on the left
hand side of an assignment.
2.1
Concurrent Communicating Abstract State Machines
A concurrent ASM (cASM) CM is deﬁned as a family {(a, asma)}a∈A of pairs consisting of
an agent a and an ASM asma.
Let Σa denote the signature of the ASM asma. Taking the union Σ = S
a∈A Σa we
distinguish between CM-states built over Σ and local states for agent a built over Σa; the
latter ones are simply projections of the former ones on the subsignature.
Deﬁnition 1. A concurrent CM-run of a concurrent ASM {(a, asma)}a∈A is a sequence
S0, S1, S2, . . . of CM-states, such that for each n ≥0 there is a ﬁnite set An ⊆A of agents
such that Sn+1 results from simultaneously applying update sets ∆a(Sj(a)) for all agents
a ∈An that have been built by asma in some preceding state Sj(a) (j(a) ≤n depending
on a), i.e. Sn+1 = Sn + S
a∈An ∆a(Sj(a)) and a /∈Sn−1
i=j(a) Ai.
Dynamic functions in Σa can further be private or shared. In the latter case they can be
updated also by other agents and thus appear in at least one other signature Σa′.
In order to isolate agents responsible for a memory management subsystem we exploit
communicating concurrent ASMs (ccASM) [8]. In a ccASM the only shared function symbols
take the form of mailboxes. Sending of a message m from a to b means to update the out-
mailbox of a by inserting m into it. This mailbox is a set-valued shared location with the
restriction that only the sender can insert messages into it and only the environment—in this
case understood as the message processing system—can read and delete them. The message
processing system will move the message m to the in-mailbox of the receiver b. Receiving a
message m by b means in particular that b removes m from its in-mailbox and performs some
local operation on m.
Therefore, in ccASMs the language of ASM rules above is enriched by the following con-
structs11:
Send. SEND(⟨message⟩, from:⟨sender⟩, to:⟨receiver⟩),
Receive. RECEIVE(⟨message⟩, from:⟨sender⟩, to:⟨receiver⟩),
Received. RECEIVED(⟨message⟩, from:⟨sender⟩, to:⟨receiver⟩), and
Consume. CONSUME(⟨message⟩, from:⟨sender⟩, to:⟨receiver⟩).
11 As explained in [8], instead of describing the details of the local RECEIVE action of an agent we only use
the corresponding RECEIVED(m) predicate; it means that m is in the mailbox of the agent who (or in
general whose mailbox manager) RECEIVED it (when the message processing system has inserted m into b’s
in-mailbox and deleted m from a’s out-mailbox).
4


## Page 5


Let us consider the situation, where all shared data is organised in relations with a unique
primary key. We can model this by a set of function symbols Σmem = {p1, . . . , pk}, where each
pi has a ﬁxed arity ai, and a ﬁxed “co-arity” ci, such that in each state S we obtain partial
functions pS
i : Bai →Bci, which are almost everywhere undeﬁned.
When dealing with a memory management subsystem we have to specify a subsystem
with separate agents that maintain the locations (pi, k). A read access by an agent a ∈A
aims at receiving a subset of relation pi containing those records with key values satisfying a
condition ϕ, i.e. the subsystem has to evaluate a term of the form pi[ϕ] = {(k, v) | ϕ(k)∧v ̸=
undef ∧pi(k) = v}. As pi is not in the signature Σa, the agent a, instead of using the term
pi[ϕ] in a rule, must send a read-request and wait for a response, i.e. it executes
SEND(read(pi, ϕ),from:a,to:home(a))
(the message just contains the name pi of the function symbol and the formula ϕ, and home(a)
denotes a not further speciﬁed receiver, which for agent a represents the memory management
subsystem), and waits until, once RECEIVED(answer(pi, ϕ),from:home(a),to:a) becomes true,
it can
RECEIVE(answer(pi, ϕ),from:home(a),to:a)
the requested value from the memory management subsystem. We abstract from the details
of the communication but assume the communication to be reliable (no message gets lost or
damaged). Where clear from the context for reasons of succinctness we notationally omit the
sender and receiver parameters in SEND and RECEIVE.
Naturally, the received answer corresponds to a unique previously sent read-request. As
in the sequel we concentrate on the handling of single message by the memory management
subsystem, the correct association of possibly several answers to several requests is of minor
importance for us.
The answer in the message must be a relation of arity ai + ci satisfying the key property
above. The agent can store such an answer using a non-shared function pa
i or process it in any
other way, e.g. aggregate the received values. This is part of the ASM rule in asma, which we
do not consider any further.
In the SEND and RECEIVE rules we use a ﬁxed agent home(a), with which the agent a
communicates. It will be unknown to the agent a, whether this agent home(a) processes the
read-request or whether it communicates with other agents to produce the answer.
Analogously, for bulk write access an agent a may want to execute the operation pi :& p
to update all records12 with a key deﬁned in p to the new values given by p. While this
would correspond to the ASM rule FORALL (k, v) ∈p pi(k) := v, the agent a must send a
write-request and wait for a response, i.e. it executes
SEND(write(pi, p),to:home(a))
(again, the message only contains the name of the function symbol pi and a relation p), and
waits to receive an acknowledgement to the write-request13, i.e. to
12 Note that in this way we capture a deletion of a record in pi with key k by having (k, undef ) ∈p. Also
insertions are subsumed by this operation: if (k, v) ∈p holds, but valS(pi, k) = undef , then a new record
in pi with key k is inserted.
13 Naturally, the remark above concerning the association of an answer to a unique previously sent request,
extends analogously to write requests.
5


## Page 6


RECEIVE(acknowledge(write,pi),from:home(a)).
We use the notation CM0 = {(a, asmc
a)}a∈A ∪{(db, asmdb)} for the concurrent communi-
cating ASM. Here for the sake of completeness we may think of a single memory agent db—in
particular, we have home(a) = db for all a ∈A—that receives read and write requests and
executes them in one step14. Thus, the rule of asmdb looks as follows:
IF
RECEIVED(read(pi, ϕ),from:a)
THEN
CONSUME(read(pi, ϕ),from:a)
LET answer(pi, ϕ) = {(k, v) | ϕ(k) ∧pi(k) = v ∧v ̸= undef } IN
SEND(answer(pi, ϕ),to:a)
IF
RECEIVED(write(pi, p),from:a)
THEN
CONSUME(write(pi, p),from:a)
FORALL (k, v) ∈p
pi(k) := v
SEND(acknowledge(write,pi),to:a)
2.2
Memory Organisation with Replication
In the previous subsection we assumed that logically (from the users’ point of view) all data
is organised in relations pi with a unique primary key. However, as we want to emphasise
replication, instead of a location (pi, k) there will always be several replicas, and at each
replica we may have a diﬀerent value. We use the notion cluster to refer to all (replicated)
locations associated with a logical relation pi.
Each cluster is associated with several data centres, and each data centre comprises several
nodes. The nodes are used for data storage, and data centres correspond to physical machines
maintaining several such storage locations. So let D denote the set of data centres, and let Di
(i = 1, . . . , k) be the sets of data centres for maintaining the relations pi, i.e. D = Sk
i=1 Di.
First let us assume that each relation pi is fragmented according to the values of a hash-
key. That is, for each i = 1, . . . , k we can assume a static hash-function hi : Bai →[m, M] ⊆
Z assigning a hash-key to each key value in Bai, i.e. those keys at which in the memory
management system possibly some value may be deﬁned. We further assume a partition
[m, M] = Sqi
j=1 rangej of the interval of hash-key values such that rangej1 < rangej2 holds
for all j1 < j2, so each range will again be an interval. These range intervals are used for
the horizontal fragmentation into qi fragments of the to-be-represented function pi: Fragj,i =
{k ∈Bai | hi(k) ∈rangej}.
All these fragments will be replicated and their elements associated with a value (where
deﬁned by the memory management system), using a ﬁxed replication factor ri for each cluster.
That is, each fragment Fragj,i will be replicated ri-times for each data centre d ∈Di. A set
of all pairs (k, v) with key k ∈Fragj,i and an associated value v in the memory management
system is called a replica of Fragj,i.
More precisely assume that each data centre d ∈Di consists of ni nodes, identiﬁed by
d and a number j′ ∈{1, . . . , ni}. Then we use a predicate copy(i, j, d, j′) to denote that the
node with number j′ in the data centre d ∈Di contains a replica of Fragj,i. To denote the
14 Note that the answer to a read request is a set, which may be empty.
6


## Page 7


values in replicas we use dynamic functions pi,j,d,j′ of arity ai and co-arity ci +1 (functions we
call again replicas). That is, instead of the logical function symbol pi we use function symbols
pi,j,d,j′ with j ∈{1, . . . , qi}, d ∈Di and j′ ∈{1, . . . , ni}, and we request hi(k) ∈rangej for all
k ∈Bai whenever copy(i, j, d, j′) holds and pi,j,d,j′(k) is deﬁned. For the associated values we
have pi,j,d,j′(k) = (v, t), where t is an added timestamp value, and values v may diﬀer from
replica to replica, i.e. there can be diﬀerent values v with diﬀerent timestamps in diﬀerent
replicas of Fragj,i.
Each data centre d maintains a logical clock clockd that is assumed to advance (with-
out this being further speciﬁed), and clockd evaluates to the current time at data centre d.
Timestamps must satisfy the following requirements:
1. Timestamps are totally ordered.
2. Timestamps set by diﬀerent data centres are diﬀerent from each other15.
3. Timestamps respect the inherent order of message passing, i.e. when data with a time-
stamp t is created at data centre d and sent to data centre d′, then at the time the message
is received the clock at d′ must show a time larger than t.
When the condition 3 is not met, a data centre may also adjust its clock for logical time
synchronisation according to Lamport’s algorithm in [15]. For clock adjustment let us deﬁne
adjust clock(d, t) ≡clockd := t′, where t′ is the smallest possible timestamp at data centre d
with t ≤t′.
2.3
Internal Request Handling for Replicated Memory
When dealing with a memory management subsystem with replication the request mes-
sages sent by agents a remain the same, but the internal request handling by the memory
management subsystem changes. This will deﬁne a reﬁned concurrent communicating ASM
CM1 = {(a, asmc
a)}a∈A ∪{(d, asmd)}d∈D.
Each agent a possesses a private version of the shared location (pi, k) parameterised by a
itself16. Consider a read request read(pi, ϕ) received from agent a by data centre d—let i be
ﬁxed for the rest of this section. Due to the fact that data is horizontally fragmented, we need
to evaluate several requests read(pi,j, ϕ) concerning keys k with hi(k) ∈rangej, one request
for each fragment index j, and then build the union so that pi[ϕ] = Sqi
j=1 pi,j[ϕ].
In order to evaluate pi,j[ϕ] several replicas of Fragj,i will have to be accessed. Here we will
leave out any details on how these replicas will be selected and accessed—this will be handled
later by means of reﬁnement. We only request that the selection of replicas complies with a
read-policy. Such a policy will also be left abstract for the moment and deﬁned later17.
When reading actual data, i.e. evaluating pi,j,d,j′(k) for selected key values k, we obtain
diﬀerent time-stamped values (v, t), out of which a value v with the latest timestamp is
15 This requirement can be fulﬁlled by assuming that a timestamp created by data centre d has the form n+od
with a positive integer n and an oﬀset od ∈(0, 1), such that oﬀsets of diﬀerent data centres are diﬀerent.
Equivalently, one might use integer values for timestamps plus a total order on data centres that is used for
comparisons in case two timestamps are otherwise equal.
16 An exact deﬁnition for this is given by the notion of ambient dependent function in [6].
17 We also leave out the treatment of nodes that are not reachable. It can be tacitly assumed that if node j at
data centre d cannot be reached, then all operations aﬀecting data at this node will be logged and executed
once the node becomes available again.
7


## Page 8


selected and sent to a as the up-to-date value of pi(k)18. The requirement that timestamps set
by diﬀerent data centres diﬀer implies that for given k the value v with the latest timestamp
is unique. All records obtained this way will be returned as the result of the read request to
the issuing agent a. Thus, we obtain the following ASM rule AnswerReadReq to-be-executed
by any data centre d upon receipt of a read request from an agent a:
AnswerReadReq =
IF RECEIVED(read(pi, ϕ), from:a) THEN
CONSUME(read(pi, ϕ), from:a)
FORALL j ∈{1, . . . , qi} CHOOSE Gi,j WITH
Gi,j ⊆{(d′, j′) | copy(i, j, d′, j′) ∧d′ ∈Di ∧1 ≤j′ ≤ni}
∧complies(Gi,j, read-policy)
LET tmax(k) = max{t | ∃v′, ¯d, ¯j.( ¯d, ¯j) ∈Gi,j ∧pi,j, ¯d,¯j(k) = (v′, t)} IN
LET answeri,j = {(k, v) | ϕ(k) ∧hi(k) ∈rangej ∧v ̸= undef ∧
∃d′, j′.((d′, j′) ∈Gi,j ∧pi,j,d′,j′(k) = (v, tmax(k)))} IN
LET answer(pi, ϕ) = Sqi
j=1 answeri,j IN
SEND(answer(pi, ϕ), to:a)
Note that the unique value v with pi,j,d′,j′(k) = (v, tmax(k)) may be undef and that the
returned answer(pi, ϕ) may be the empty set.
For a write request write(pi, p) sent by agent a to data centre d we proceed analogously.
In all replicas of Fragj,i selected by a write-policy the records with a key value in p will be
updated to the new value—this may be undef to capture deletion—provided by p, and a
timestamp given by the current time clockd. However, the update will not be executed, if the
timestamp of the existing record is already newer. In addition, clocks that “are too late” will
be adjusted, i.e. if the new timestamp received from the managing data centre d is larger
than the timestamp at data centre d′, the clock at d′ is set to the received timestamp. Thus,
we obtain the following ASM rule PerformWriteReq19 to-be-executed by any data centre d
upon receipt of an update request from an agent a:
PerformWriteReq =
IF RECEIVED(write(pi, p), from:a) THEN
CONSUME(write(pi, p), from:a)
FORALL j ∈{1, . . . , qi} CHOOSE Gi,j WITH
Gi,j ⊆{(d′, j′) | copy(i, j, d′, j′) ∧d′ ∈Di ∧1 ≤j′ ≤ni}
∧complies(Gi,j, write-policy)
LET tcurrent = clockself IN
FORALL (d′, j′) ∈Gi,j
FORALL (k, v) ∈p WITH hi(k) ∈rangej
18 When there is no record in relation pi,j,d,j′ with key k, we would normally write pi,j,d,j′(k) = undef in an
ASM, but in the replication context it will be simpler to write pi,j,d,j′(k) = (undef , −∞) instead, i.e. all
non-existing data are considered to carry the smallest possible timestamp denoted by −∞. Furthermore, if
a record is deleted, we keep a deletion timestamp, so we may also ﬁnd pi,j,d,j′(k) = (undef , t) with t > −∞.
As we will see, such a deletion timestamp t becomes obsolete, once the value (undef , t) has been assigned
to all replicas, i.e. the assumption of deletion timestamps does not disable physical removal of data from
the database.
19 Again, we dispense with the handling of write-requests at nodes that are not available. For this we can
assume an exception handling procedure that logs requests and executes them in the order of logging, once
a node has become alive again. This could give rise to a reﬁnement, which we omit here.
8


## Page 9


IF ∃v′, t.pi,j,d′,j′(k) = (v′, t) ∧t < tcurrent THEN
pi,j,d′,j′(k) := (v, tcurrent)
IF clockd′ < tcurrent THEN adjust clock(d′, tcurrent)
SEND(acknowledge(write, pi), to:a)
The clock adjustment is necessary to ensure that timestamps respect the inherent order
of message passing as requested above. Write requests with old timestamps may be lost in
case a value with a newer timestamp already exists. Then depending on the read-policy a
lost update on a single replica may be enough for the value never to appear in an answer to
a read-request. In the following we use the notions of complete and correct reﬁnement20 as
deﬁned in [10, pp.111ﬀ.].
Proposition 1. The concurrent communicating ASM CM1 = {(a, asmc
a)}a∈A∪{(d, asmd)}d∈D
is a complete reﬁnement of the concurrent communicating ASM CM0 = {(a, asmc
a)}a∈A ∪
{(db, asmdb)}.
Proof. The only diﬀerences between the two communicating concurrent ASMs are the follow-
ing:
– Instead of having home(a) = db for all a ∈A in the abstract speciﬁcation, home(a) ∈D
diﬀers in the reﬁnement. Nonetheless, in both cases the handling of a read or write request
is done in a single step.
– The rule fragment in the abstract speciﬁcation
LET answer(pi, ϕ) = {(k, v) | ϕ(k) ∧pi(k) = v ∧v ̸= undef } IN
SEND(answer(pi, ϕ),to:a)
dealing with a read request corresponds to a rule fragment
FORALL j ∈{1, . . . , qi} CHOOSE Gi,j WITH
Gi,j ⊆{(d′, j′) | copy(i, j, d′, j′) ∧d′ ∈Di ∧1 ≤j′ ≤ni}
∧complies(Gi,j, read-policy)
LET tmax(k) = max{t | ∃v′, ¯d, ¯j.( ¯d, ¯j) ∈Gi,j ∧pi,j, ¯d,¯j(k) = (v′, t)} IN
LET answeri,j = {(k, v) | ϕ(k) ∧hi(k) ∈rangej ∧v ̸= undef ∧
∃d′, j′.((d′, j′) ∈Gi,j ∧pi,j,d′,j′(k) = (v, tmax(k)))} IN
LET answer(pi, ϕ) = Sqi
j=1 answeri,j IN
SEND(answer(pi, ϕ), to:a)
in the rule AnswerReadReq in the reﬁnement.
– The rule fragment in the abstract speciﬁcation
FORALL (k, v) ∈p pi(k) := v
SEND(acknowledge(write,pi),to:a)
dealing with a write request corresponds to a rule fragment
FORALL j ∈{1, . . . , qi} CHOOSE Gi,j WITH
Gi,j ⊆{(d′, j′) | copy(i, j, d′, j′) ∧d′ ∈Di ∧1 ≤j′ ≤ni}
∧complies(Gi,j, write-policy)
LET tcurrent = clockself IN
FORALL (d′, j′) ∈Gi,j
20 Note that the notion of reﬁnement for ASMs is more general than data reﬁnement as discussed in [10, p.113].
In particular, correct reﬁnement does not imply the preservation of invariants.
9


## Page 10


FORALL (k, v) ∈p WITH hi(k) ∈rangej
IF ∃v′, t.pi,j,d′,j′(k) = (v′, t) ∧t < tcurrent THEN
pi,j,d′,j′(k) := (v, tcurrent)
IF clockd′ < tcurrent THEN adjust clock(d′, tcurrent)
SEND(acknowledge(write, pi), to:a)
in the rule PerformWriteReq in the reﬁnement.
Thus, each run of the abstract communicating concurrent ASM deﬁnes in a natural way
a run of the reﬁned communicating concurrent ASM21.
⊓⊔
Note that without further knowledge about the read- and write-policies it is not possible
to prove that the reﬁnement is also correct.
3
Reﬁnement Using Replication Policies
We deﬁne view compatibility, a notion for consistency that formalises the intuitive expectation
of the agents sending requests that the answers in case of replication remain the same as
without, because replication is merely an internal mechanism of the memory management
subsystem to increase availability, which is completely hidden from the requesting agents. We
then reﬁne the ASMs for internal request handling by concrete read- and write-policies, and
show that for particular combinations of read- and write-policies our abstract speciﬁcation
CM1 guarantees view compatibility, which further implies that the reﬁnement of CM0 by
CM1 is correct.
3.1
View Compatibility
Informally, view compatibility is to ensure that the system behaves in a way that whenever
an agent sends a read- or write-request the result is the same as if the read or write had been
executed in a state without replication or timestamps and without any internal processing
of the request22. However, it may be possible that parallel requests are evaluated in diﬀerent
states.
For a formal deﬁnition of this notion we have to relate runs of the concurrent communicat-
ing ASM with the memory management subsystem with runs, where in each state a virtual
location (pi, k) has only one well-deﬁned value v instead of computing such a value from the
diﬀerent replicas that may even originate from diﬀerent states. For this we ﬁrst introduce the
technical notion of a ﬂattening: we simply reduce the multiple values associated with replicas
of a location ℓto a single value.
Formally, consider runs of the concurrent ASM CM1 = {(a, asmc
a)}a∈A ∪{(d, asmd)}d∈D,
where the ASMs asmc
a sends read and write requests that are processed by the data centre
agents d ∈D, which return responses.
Deﬁnition 2. If S0, S1, S2, . . . is a run of CM1 = {(a, asmc
a)}a∈A ∪{(d, asmd)}d∈D, then we
obtain a ﬂattening S′
0, S′
1, S′
2, . . . by replacing in each state all locations (pi,j,d′,j′, k) by a
21 Actually, in this case the reﬁnement is a (1,1)-reﬁnement.
22 Note that view compatibility is a rather weak consistency requirement, as it only ensures that despite
replication up-to-date values are read. However, as we will show later in Section 4, even this weak concistency
requirement requires some form of transaction management.
10


## Page 11


single location (pi, k) and letting the value associated with (pi, k) in the considered state be
one of the values in the set
{v | ∃j, d′, j′.∃t.pi,j,d′,j′(k) = (v, t)}
in the considered state.
Obviously, a ﬂattening is a sequence of states of the concurrent ASM {(a, asmc
a)}a∈A, but
in most cases it will not be a run. So the question is, under which conditions we can obtain a
run. As we stated above that the system shall behave as if there is no replication, we have to
ensure that for each agent the following property holds: If the agent sends a write-request that
would update the value of a location ℓto v, the eﬀect would be the same in the ﬂattening.
Analogously, if the agent sends a read-request for location ℓ, the answer it receives would be
also the same as if a read is executed in the ﬂattening.
In order to formalise this property we deﬁne agent views, which emphasise only the moves
of a single agent a ∈A, while merging all other moves into activities of the environment as
deﬁned in [10].
Let us ﬁrst consider the agent view of a concurrent run S0, S1, . . . of our communicating
ASMs {(a, asmc
a)}a∈A. Let a ∈A be an arbitrary agent. Its view of the run is the subsequence
of states Sa,0, Sa,1, . . . in which a makes a move (restricted to the signature of a). Thus Sa,0
is a’s initial state, the state Sj (where j depends on a) in which a performs its ﬁrst step in
the given run. Given any state Sk = Sa,n, its successor state in the a-view sequence depends
on the move a performs in Sa,n.
1. If a in Sa,n performs a Send step—a write- or read-request to home(a)—it contributes to
the next state Sk+1 by an update set which includes an update of its out-mailbox, which in
turn is assumed to eventually yield an update of the mailbox of home(a). But Sk+1 is not
yet the next a-view state, in which a will perform its next move. This move is determined
by the following assumption:
Atomic Request/Reply Assumption for agent/db runs: If in a run an agent performs a Send
step to the memory management system, then its next step in the run is the corresponding
Receive step, which can be performed once the answer to the query sent by the memory
management system has been Received.
By this assumption the next a-view state Sa,n+1 = Sl is determined by (what appears to a
as) an environment action which enables the Receive step by inserting the reply message
into a’s mailbox and thereby making the Received predicate true in Sl for some l > k.
2. If a in Sa,n = Sk performs a Receive or an internal step, then besides the mailbox update
to Consume the received message it yields only updates to non-shared locations so that
its next a-view state is the result of applying these updates together with updates other
agents bring in to form Sk+1 = Sa,n+1.
Note that by the Atomic Request/Reply Assumption any agent can make ﬁnitely many
internal steps after and only after each Receive step. For the ease of exposition but without
loss of generality we synchronize internal steps of an agent with the global steps other agents
perform during such an internal computation segment so that the result of internal moves
becomes visible in the global run view.
We now deﬁne a notion of ﬂat agent view of a run S0, S1, . . . of the concurrent agent ASM
{(a, asmc
a)}a∈A ∪{(d, asmd)}d∈D, including the memory management subsystem.
11


## Page 12


Take an arbitrary subsequence S′
j0, S′
j1, . . . of an arbitrary ﬂattening S′
0, S′
1, . . . (restricted
to the signature of the agent a) of S0, S1, . . . . Then S′
j0, S′
j1, . . . is called a ﬂat view of agent
a of the run S0, S1, . . . if the following conditions hold:
– Whenever a performs a request in state Sk there is some S′
ji such that k = ji. If the
corresponding reply is received in state Sm for some m > k (so that a makes a Receive
move in state Sm), then S′
ji+1 = Sm. Furthermore there exists some n with k < n ≤m
such that the following holds:
• If the request is a write-request, then for each location ℓwith value v in this request
valS′n(ℓ) = v holds, provided there exists an agent reading23 the value v.
• If the request is a read-request, then for each location ℓwith value v in the answer
valS′n(ℓ) = v holds.
– Whenever a performs a Receive or an internal move in state Sk there is some ji such that
Sk = S′
ji and Sk+1 = S′
ji+1
Deﬁnition 3. We say that {(a, asmc
a)}a∈A ∪{(d, asmd)}d∈D is view compatible with the con-
current ASM {(a, asmc
a)}a∈A∪{(db, asmdb)} iﬀfor each run R = S0, S1, S2, . . . of {(a, asmc
a)}a∈A∪
{(d, asmd)}d∈D there exists a subsequence of a ﬂattening R′ = S′
0, S′
1, S′
2, . . . that is a run of
{(a, asmc
a)}a∈A∪{(db, asmdb)} such that for each agent a ∈A the agent a-view of R′ coincides
with a ﬂat view of R by a.
Note that in this deﬁnition of view compatibility we relate agent views with ﬂat agent
views, and in both these views we consider the restriction to the signature of the agent a.
Technically, the mailboxes associated with a belong to this signature, so every SEND and
RECEIVE state Si (for a) and its ﬂattening S′
i appears in the views. We can understand the
agent view and the ﬂat agent view in such a way, that the environment reads the request (i.e.
the message in the out-mailbox) in state S′
ji, evaluates it in state S′
n, and places the answer
into the in-mailbox of a in state S′
ji+1 (for ji < n < ji+1 as requested in the deﬁnition).
This can also formally be considered as a move by a single agent m representing the memory
management subsystem, which executes the ASM rules that are associated with each request.
The notion of view compatibility is closely related to sequential consistency as deﬁned by
Lamport. In Lamport’s work an execution is a set of sequences of operations, one sequence
per process. An operation is a pair (operation, value), where the operation is either read
or write and value is the value read or written. The execution is sequentially consistent iﬀ
there exists an interleaving of the set of sequences into a single sequence of operations that
is a legal execution of a single-processor system, meaning that each value read is the most
recently written value. (One also needs to specify what value a read that precedes any write
can obtain.) Our deﬁnition of view compatibility generalises this notion, as we always consider
bulk requests and also permit parallel operations.
3.2
Speciﬁcation of Replication Policies
In the speciﬁcation of ASM rules handling read and write requests by a ﬁxed data centre d
we used sets Gi,j ⊆Ci,j with Ci,j = {(d′, j′) | copy(i, j, d′, j′)} (i, j are given by the request
and the fragmentation) as well as an abstract predicate complies(Gi,j, policy). It is allowed to
23 Otherwise the update at location ℓwill be lost. For instance, this may happen in case of outdated timestamps.
12


## Page 13


specify diﬀerent policies for read and write, but only one policy is used for all read requests,
and only one for all write requests.
Let us now deﬁne diﬀerent such policies and reﬁne the ASMs for the data centre agents
d by means of these deﬁnitions. Basically, we distinguish policies that are global and those
that are local, the latter ones requesting that only replicas in the handling data centre d are
considered for the set Gi,j. Thus we can use the following deﬁnition:
local ≡∃d.∀d′, j′.(d′, j′) ∈Gi,j ⇒d′ = d
In addition the diﬀerent policies diﬀer only in the number of replicas that are to be
accessed. Major global policies are All, One, Two, Three, Quorum, and Each Quorum,
while the corresponding local policies are Local One and Local Quorum.
All. As the name indicates, the predicate complies(Gi,j, All) can be deﬁned by Gi,j = Ci,j,
i.e. all replicas are to be accessed.
One, Two, Three. Here, at least one, two or three replicas are to be accessed, which de-
ﬁnes complies(Gi,j, One), complies(Gi,j, Two) and complies(Gi,j, Three) by |Gi,j| ≥1,
|Gi,j| ≥2, and |Gi,j| ≥3, respectively.
Local One. Analogously, complies(Gj, Local One) is deﬁned by the conjunction local ∧
ONE.
Quorum(q). For a value q with 0 < q < 1 complies(Gi,j, Quorum(q)) is deﬁned by q·|Ci,j| <
|Gi,j|. By default, the value q = 1
2 is used, i.e. a majority of replicas has to be accessed.
Note that All could be replaced by Quorum(1).
Local Quorum(q). Analogously, complies(Gi,j, Local Quorum(q)) can be deﬁned by local ∧
Quorum(q).
Each Quorum(q). For this we have to consider each data centre separately, for which we
need Ci,j, ¯d = {(d′, j′) ∈Ci,j | d′ = ¯d} and Gi,j, ¯d = Gi,j ∩Ci,j, ¯d. Then the deﬁnition of
complies(Gi,j, Each Quorum(q)) becomes ∀¯d ∈Di.q · |Ci,j, ¯d| < |Gi,j, ¯d|.
3.3
Consistency Analysis
In the following we will analyse in more detail the eﬀects of the replication policies. For this
we need appropriate combinations of read- and write-policies:
– If the write policy is ALL, then the combination with any read policy is appropriate.
– If the read policy is ALL, then the combination with any write policy is appropriate.
– If the write-policy is Quorum(q) or Each Quorum(q) and the read-policy is Quorum(q′)
or Each Quorum(q′) with q + q′ ≥1, then the combination is appropriate.
Proposition 2. Let CM1 = {(a, asmc
a)}a∈A ∪{(d, asmd)}d∈D be the concurrent communi-
cating ASM with a memory management subsystem using data centres d ∈D as speciﬁed in
the previous section. If the combination of the read and write policies is appropriate, then the
system is view compatible with the concurrent ASM {(a, asmc
a)}a∈A.
Proof. We exploit that in our abstract speciﬁcation of the handling of write- and read-requests
all selected replicas are written and read in parallel. Thus, if the write-policy is All, then in
each state always the same value is stored in all replicas, so the proposition is obvious for the
policy All.
13


## Page 14


If the write-policy is Quorum(q) or Each Quorum(q), then for each location ℓthe
multiplicity of replica considered to determine the value with the largest timestamp is at
least ⌈m+1
2 ⌉with m being the total number of copies. For this it is essential that updates with
a smaller timestamp are rejected, if a value with a larger timestamp already exists.
Consequently, each read access with one of the policies Quorum(q′), Each Quorum(q′)
(with q + q′ ≥1) or All will read at least once this value and return it, as the value with the
largest timestamp will be used for the result. That is, in every state only the value with the
largest timestamp for each location uniquely determines the run, which deﬁnes the equivalent
concurrent run.
⊓⊔
Corollary 1. If CM1 = {(a, asmc
a)}a∈A ∪{(d, asmd)}d∈D is view compatible, then it is also
a correct reﬁnement of CM0 = {(a, asmc
a)}a∈A ∪{(db, asmdb)}.
Proof. Let R = S0, S1, . . . be a run of CM1. According to the deﬁnition of view compatibility
there exists a ﬂattened subrun R′ = S′
i0, S′
i1, . . . that is also a concurrent run of CM0 =
{(a, asmc
a)}a∈A ∪{(db, asmdb)} such that for each agent a ∈A the projections of R and R′
coincide.
⊓⊔
A stronger notion of consistency would be global consistency, for which we even require that
any run of the ASM with the memory management behaves in the same way as a concurrent
ASM, i.e. diﬀerent from the view compatibility we even require that parallel read- and write
requests can be seen as referring to the same state. Formally, this requires to strengthen the
requirements for a ﬂat view such that for parallel request the index n (with k < n ≤m) is
always the same. Then the speciﬁcation must be reﬁned to handle also all parallel requests
in parallel by the data cente agent.
4
Reﬁnement with Internal Communication
We will now address a reﬁnement of our speciﬁcation of the memory management subsystem.
So far in CM1 the home data centre agent d associated with an agent a manages in one
step the retrieval of data from or update of data of suﬃciently many replicas as speciﬁed
by the read- and write-policies, respectively. In doing so we abstracted from any internal
communication between data centres.
However, in reality data centres refer to diﬀerent physical machines, so the gist of the
reﬁnement is to treat the handling of a request as a combination of direct access to local
nodes, remote access via messages to the other relevant data centres, and collection and
processing of return messages until the requirements for the read- or write-policy are fulﬁlled.
That is, the validation of the policy accompanies the preparation of a response message and
is no longer under control of the home agent.
We ﬁrst show again that the reﬁnement is a complete ASM reﬁnement. Then we investigate
again view compatibility and show that it is not preserved by the reﬁnement. In fact, view
compatibility is linked to the reﬁnement being also correct, i.e. for each run of the concrete
concurrent system we ﬁnd a corresponding run of the abstract concurrent system. In general,
however, this is not the case. We can even show that view compatibility implies view serialis-
ability, which means that consistency (if desired) can only be guaranteed, if transactions (at
least for single requests) are used. On the other hand, transactions together with appropriate
read- and write-policies trivially imply view compatibility.
14


## Page 15


4.1
Request Handling with Communicating Data Centres
In Section 2 we speciﬁed how a data centre d (treated as an agent) handles a request received
from an agent a with home(a) = d. We distinguished read requests read(pi, ϕ) subject to a
read-policy and write requests subject to a write-policy. Now, we ﬁrst specify an abstract rule
which manages external requests, i.e. coming from an agent a and received by any data centre
d, where request is one of these read or write requests. Essentially an external request is for-
warded as internal request to all other data centres d′ ∈Di, where it is handled and answered
locally (see the deﬁnition of HandleLocally below), whereas collecting (in answer(pi, ϕ)) and
sending the overall answer to the external agent a is delegated to a new agent a′. SELF denotes
the data centre agent d which executes the rule.
DelegateExternalReq =
IF RECEIVED(request, from:a) THEN
LET tcurrent = clockSELF IN
LET a′ = new(Agent) IN
Initialize(a′)
HandleLocally(request, a′, tcurrent)
ForwardToOthers(request, a′, tcurrent)
CONSUME(request, from:a)
WHERE
ForwardToOthers(request, a′, tcurrent)=
FORALL d′ ∈Di WITH d′ ̸= SELF
SEND((request, a′, tcurrent), to:d′)
Initialize(a′) =
answera′ := ∅
FORALL 1 ≤j ≤qi
FORALL d′ ∈Di
counta′(j, d′) := 0
counta′(j) := 0
IF request = read(pi, ϕ)
THEN asma′ := CollectRespondToRead
ELSE asma′ := CollectRespondToWrite
requestora′ := a
mediatora′ := SELF
requestTypea′ := request
To Initialize a delegate a it is equipped with a set answera, where to collect the val-
ues arriving from the asked data centres and with counters counta(j, d) (for the number of
inspected replicas of the j-th fragment at data centre d) and counta(j) (for the number of
inspected replicas of the j-th fragment). The counters serve to check compliance with poli-
cies. The mediator and requestor information serves to retrieve sender and receiver once the
delegate could complete the answer to the request it has been created for.
In this way the request handling agent d simply forwards the request to all other data
centre agents and in parallel handles the request locally for all nodes associated with d.
The newly created agent (a ‘delegate’) will take care of collecting all response messages and
preparing the response to the issuing agent a. Request handling by any other data centre d′
is simply done locally using the following rule.
15


## Page 16


ManageInternalReq =
IF RECEIVED((request, a′, t), from:d) THEN
HandleLocally(request, a′, t)
CONSUME((request, a′, t), from:d)
That is we equip each data centre (agent) d (of a cluster Di related to pi) with the
following ASM program, where the components HandleLocally and the two versions of
CollectRespond are deﬁned below.
asmd =
DelegateExternalReq
ManageInternalReq
For local request handling we preserve most of what was speciﬁed in Section 2 with
the diﬀerence that checking the policy is not performed by the data centre agent but by
the delegate of the request; check the predicates all messages received and suﬃcient(policy)
below. We use a predicate alive to check, whether a node is accessible or not. A possible
interpretation of this liveness concept is that a node is inaccessible if it does not reply fast
enough. For a read request we specify HandleLocally(read(pi, ϕ), a′, tcurrent) as follows.
HandleLocally(read(pi, ϕ), a′, t)=
LET d′ = SELF IN
FORALL j ∈{1, . . . , qi}
LET
Gi,j,d′ = {j′ | copy(i, j, d′, j′) ∧alive(d′, j′)} IN
LET
tmax(k) = max({t | ∃v′, ¯j.¯j ∈Gi,j,d′ ∧pi,j,d′,¯j(k) = (v′, t)}) IN
LET
answeri,j,d′ = {(k, v, tmax(k)) | ϕ(k) ∧hi(k) ∈rangej ∧
∃j′ ∈Gi,j,d′.pi,j,d′,j′(k) = (v, tmax(k))} IN
LET
ans(d′) = Sqi
j=1 answeri,j,d′, x = (|Gi,1,d′|, . . . , |Gi,qi,d′|) IN
SEND(answer(ans(d′), x), to:a′)
Here we evaluate the request locally, but as the determined maximal timestamp may not
be globally maximal, it is part of the returned relation. Also the number of replicas that are
alive and thus contributed to the local result is returned, such that the delegate a′ responsible
for collection and ﬁnal evaluation of the request can check the satisfaction of the read-policy.
For this the created partial result is not returned to the agent d that issued this local request,
but instead to the delegate (the collection agent).
For the write requests we proceed analogously. For the handling of an update request the
rule HandleLocally(write(pi, p), a′, tcurrent) is speciﬁed as follows.
HandleLocally(write(pi, p), a′, t′)=
LET d′ =SELF IN
IF clockd′ < t′ THEN adjust clock(d′, t′)
LET Gi,d′(j) = {j′ | copy(i, j, d′, j′) ∧alive(d′, j′)} IN
FORALL j ∈{1, . . . , qi}
FORALL j′ ∈Gi,d′(j)
FORALL (k, v) ∈p WITH hi(k) ∈rangej
IF ∃v′, t.pi,j,d′,j′(k) = (v′, t) ∧t < t′
THEN pi,j,d′,j′(k) := (v, t′)
16


## Page 17


LET x = (|Gi,1,d′|, . . . , |Gi,qi,d′|) IN
SEND(ack write(pi, x), to:a′)
Again, the partial results acknowledging the updates at the nodes associated with data
centre d′ are sent to the collecting agent a′, which will verify the compliance with the write-
policy. Note that even a non-successful update at a location (pi,j,d′,j′, k)—this may result, if
already a value with a larger timestamp exists—will be counted for |Gi,j,d′|.
For the delegate a′ that has been created by d for a request with the task to collect partial
responses and to create the ﬁnal response to the agent a issuing the request we need predicates
suﬃcient(policy) to check, whether the read and write policies are fulﬁlled, in which case the
response to a is prepared and sent. These predicates are deﬁned for each i as follows.
suﬃcient(All) ≡∀j.(1 ≤j ≤qi ⇒count(j) = γi,j)
with γi,j = |{(d′, j′) | copy(i, j, d′, j′)}|
suﬃcient(One) ≡∀j.(1 ≤j ≤qi ⇒count(j) ≥1)
suﬃcient(Two) ≡∀j.(1 ≤j ≤qi ⇒count(j) ≥2)
suﬃcient(Three) ≡∀j.(1 ≤j ≤qi ⇒count(j) ≥3)
suﬃcient(Quorum(q)) ≡∀j.(1 ≤j ≤qi ⇒γi,j · q < count(j))
suﬃcient(Each Quorum(q)) ≡∀j.(1 ≤j ≤qi ⇒∀d ∈Di.δi,j,d · q < count(j, d))
with δi,j,d = |{j′ | copy(i, j, d, j′)}|
suﬃcient(Local Quorum(q, d)) ≡∀j.(1 ≤j ≤qi ⇒δi,j,d · q < count(j, d))
suﬃcient(Local One(d)) ≡∀j.(1 ≤j ≤qi ⇒count(j, d) ≥1)
It remains to specify the delegate rules CollectRespondToRead and CollectRespondToWrite,
the programs associated with the agent a′, which was created upon receiving a request from
an agent a. The CollectRespond action is performed until all required messages have been
received and splits into two rules for read and write requests, respectively.
While being alive, the delegate a′ collects the messages it receives from the data centres d′
to which the original request had been forwarded to let them HandleLocally (request, a′). If
the set of collected answers suﬃces to respond, the delegate sends an answer to the original
requester and kills itself.24 Thus each of the rules of CollectRespond has a Collect and a
Respond subrule with corresponding parameter for the type of expected messages.
CollectRespondToRead=
IF RECEIVED(answer(ans(d′), x), from:d′)
THEN Collect((ans(d′), x), from:d′)
IF suﬃcient(read-policy)
THEN Respond(requestTypeSELF)
WHERE
Respond(read(pi, ϕ))=
LET d=mediator(SELF), a=requestor(SELF) IN
LET answer(pi, ϕ) = {(k, v) | ∃t. (k, v, t) ∈answerSELF} IN
24 We leave it to the garbage collector to deal with later arriving messages, that is messages addressed to a
delegate which has been deleted already.
17


## Page 18


SEND(answer(pi, ϕ), from:d, to:a)
DELETE(SELF,Agent)
Collect((ans(d′), x), from : d′)=
FORALL k WITH ∃v, t. (k, v, t) ∈ans(d′)
LET (k, v, t) ∈ans(d′) IN
IF ∃v′, t′. (k, v′, t′) ∈answer(pi, ϕ)
THEN LET (k, v′, t′) ∈answer(pi, ϕ) IN
IF t′ < t
THEN
DELETE((k, v′, t′), answer(pi, ϕ))
INSERT((k, v, t), answer(pi, ϕ))
ELSE
INSERT((k, v, t), answer(pi, ϕ))
LET (x1, . . . , xqi) = x IN
FORALL j ∈{1, . . . , qi}
count(j, d′) := count(j, d′) + xj
count(j) := count(j) + xj
CONSUME((ans(d′), x), from:d′)
The analogous collection of messages for write requests is simpler, as the ﬁnal response is
only an acknowledgement.
CollectRespondToWrite=
IF RECEIVED(ack write(pi, x), from:d′) THEN
Collect(ack write(pi, x), from:d′)
CONSUME(ack write(pi, x), from:d′)
IF suﬃcient(write-policy) THEN
SEND(acknowledge(write, pi), from:mediator(SELF), to:requestor(SELF))
DELETE(SELF,Agent)
WHERE
Collect(ack write(pi, x), from:d′) =
LET (x1, . . . , xqi) = x IN
FORALL j ∈{1, . . . , qi}
count(j, d′) := count(j, d′) + xj
count(j) := count(j) + xj
Note that in our speciﬁcation we do not yet deal with exception handling. We may tacitly
assume that eventually all requested answers will be received by the collecting agent.
4.2
Analysis of the Reﬁnement
First we investigate the interaction of one agent a with the database. By CM1 we already
denoted the abstract concurrent ASM {(a, asmc
a)}a∈A ∪{(d, asmd)}d∈D from Section 2. Now
let CM2 denote the reﬁned concurrent ASM {(a, asmc
a)}a∈A ∪{(d, asm′
d)}d∈D∪Ext together
with the dynamic set Ext of delegates from Subsection 4.1. Note that the delegates are created
on-the-ﬂy by the agents d ∈D, needed for collecting partial responses for each request and
preparing the ﬁnal responses.
Let S0, S1, . . . be a concurrent run of CM1, which we ﬁrst look at from the perspective
of a single agent a ∈A. In each of its non purely local steps asmc
a produces an update set,
which together with update sets produced by other agents is applied to some state (one of
18


## Page 19


the Sj). Let S (another Si with j < i) denote the resulting state. Apart from updates to
non-shared locations with function symbols in Σa the updates brought into the state S are
read and write requests sent to the memory management subsystem. Then agent a continues
in some state S′ = Si+x evaluating the responses to the read and write requests it had sent.
Furthermore, there is another state S′′ = Si+y (y ≥x), where all updates issued by write
requests of a have been propagated to all replicas.
The transition from S to S′ is achieved by means of a step of asmd for d = home(a), and
the same holds for the transition from S′ to S′′. Therefore, there exist corresponding states
¯S, ¯S′ for CM2, in which the unchanged asmc
a brings in the same read and write requests and
receives the last response, respectively. In a concurrent run for CM2 the transition from ¯S to
¯S′ results from several steps by the subsystem {(d, asm′
d)}d∈D∪Ext.
With respect to each of the requests received from a the agent d = home(a) contributes
to a state ¯S1 with requests for each agent d′ ∈D, d′ ̸= d, the creation and initialisation of a
response collecting agent a′, and the local handling of the request at nodes associated with
data centre d. Then each agent d′ ∈D contributes to some state ¯Sk (k > 1), in which the
partial response to the request sent to d′ is produced. Concurrently the collection agent a′ on
receipt of a partial response updates its own locations—these comprise the read response ̺,
the acknowledgement responses and several counters—and thus contributes to some state ¯Sj
(j > 1). Finally, a′ will also produce and send the response to a. This response will be the
same as the one in state S′, if the reﬁned run from ¯S to ¯S′ uses the same selection of copies
for each request referring to pi and each fragment Fragj,i.
Furthermore, some partial responses may arrive in states ¯Sj with j > k for ¯S′ = ¯Sk. These
are not processed by a′ any more, but by the garbage collector. Thus the state ¯S′′ , when all
updates have been propagated, corresponds to state S′′. Taking these considerations together
we have shown the following lemma.
Lemma 1. The concurrent ASM CM2,a = {(a, asmc
a)} ∪{(d, asm′
d)}d∈D∪Ext is a complete
reﬁnement of CM1,a = {(a, asmc
a)} ∪{(d, asmd)}d∈D.
Now consider the actions of all agents a ∈A together. The arguments above remain valid,
except that for the sequence ¯S, ¯S1, ¯S2, . . . , ¯S′, . . . , ¯S′′ there are many intermediate states, in
which updates of other agents and other data centres for other requests are brought in. A
partial response for a request by a and the eﬀects on values in the replicas may in general
diﬀer, as diﬀerent partial responses may result depending on the order of request handling.
However, there exists a run of CM2 such that the projection to CM2,a is exactly the sequence
¯S, ¯S1, ¯S2, . . . , ¯S′, . . . , ¯S′′ investigated before. This gives us the following result.
Proposition 3. CM2 = {(a, asmc
a)}a∈A ∪{(d, asm′
d)}d∈D∪Ext is a complete reﬁnement of
CM1 = {(a, asmc
a)}a∈A ∪{(d, asmd)}d∈D.
4.3
Consistency Analysis
While we have obtained a complete reﬁnement, CM2 permits more possibilities to perform
updates to replicas and reading values from replicas, respectively, in diﬀerent orders. Unfortu-
nately, view compatibility (as in Proposition 2) cannot be preserved, as the following simple
counterexample shows:
Consider a single location (pi, k)) for a ﬁxed k. For simplicity forget about the relation
symbols pi and let this location simply be x. Assume that there are at least two replicas (say
19


## Page 20


x1 and x2), which both are set to the initial value 0 (with some timestamp t0). Let the write
policy be All and the read policy be One (which according to Proposition 2 is an appropriate
combination of policies that leads to view compatibility for the abstract speciﬁcation CM1).
Let a1 be an agent issuing a write request SEND(write(x,1)), and let a2 be another agent
issuing a sequence of two read requests SEND(read(x)). Then in CM2 the following sequence
is possible:
1. The write request by a1 gives rise to the update of replica x1, so the value is set to (1, t)
with some timestamp t > t0.
2. For the ﬁrst read request by a2 only the replica x1 is evaluated, and thus the returned
answer is 1.
3. For the following second read request by a2 only the replica x2 is evaluated, and thus the
returned answer is 0.
4. All other updates required for the completion of the write request by a1 happen after the
completion of the two read requests.
Obviously, there cannot be a run of the communicating concurrent ASM without replica-
tion that produces the same answers to the read and write requests.
From the counterexample we can even conclude that there is no reasonable weaker deﬁ-
nition of consistency such that an appropriate combination of read- and write-policies alone,
even under strong assumptions that no bulk requests are considered, suﬃces to guarantee
consistency. For such a deﬁnition the run in the counterexample would have to be called
“consistent”, which does not make much sense.
The question is whether additional conditions could be enforced in the speciﬁcation that
would lead again to view compatibility. As we will see, any such condition already implies
serialisability. Therefore, we conclude our analysis by showing this relationship between view
compatibility and (view) serialisability, which implies that the best and well explored way to
ensure consistency is to exploit transactions (at least for single read and write requests).
Let us ﬁrst deﬁne the notion of serialisability. For this consider an arbitrary run R =
S0, S1, . . . of CM2. A request is either a read request of the form (read(pi, ϕ), from:a) or a write
request of the form (write(pi, p), from:a). If Sj is the ﬁrst state, in which RECEIVED(r) holds
for such a request r, we call Sj the state, in which the request r is issued, and write σ(r) = j
as well as ag(r) = a. Analogously, a response r takes either the form (answer(pi, ϕ), to:a)
or (acknowledge(write, pi), to:a). We call the state Sk, in which SEND(r) becomes eﬀective,
the state, in which the response r is issued, and write also σ(r) = j as well as ag(r) = a.
Then σ deﬁnes a partial order ⪯on the set of requests and responses in the run as well as
an equivalence relation ∼for simultaneous requests and responses. Furthermore, there is a
bijection ans that maps each request to its corresponding response.
In a serial run a request is immediately followed by its corresponding response without
any other request or response in between, but requests may be handled in parallel. Thus,
formally we call the run R serial iﬀthe following two conditions hold:
1. If r is a request and r′ is another request or response with σ(r) ≤σ(r′) ≤σ(ans(r)), then
either r ∼r′ or r′ ∼ans(r) hold.
2. For two simultaneous requests r ∼r′ we also have ans(r) ∼ans(r′).
Deﬁnition 4. Two runs R and R′ are called view equivalent iﬀthe following two conditions
hold:
20


## Page 21


1. R and R′ contain exactly the same requests and responses. In particular, in a response
(answer(pi, ϕ), to:a) to a read request (read(pi, ϕ), from:a) the sets answer(pi, ϕ) of tuples
are identical in both runs.
2. For each agent a the sequence of its requests and responses is identical in both runs, i.e.
if σ(r) < σ(r′) ∧ag(r) = ag(r′) = a holds in R, it also holds in R′.
Then a run R is called view serialisable iﬀthere exists a serial run R′ that is view equivalent
to R.
Informally phrased, a run is view serialisable if there exists a serial run, in which for each
agent the requests and corresponding responses appear in the same order and the same results
are produced.
Proposition 4. If CM2 is view compatible with the concurrent ASM CM0 = {(a, asmc
a)}a∈A∪
{(db, asmdb)}, then every run R of CM2 is view serialisable.
Proof. Let R = S0, S1, . . . be a run of CM2. The deﬁnition of view compatibility implies that
there exists a subsequence of a ﬂattening R′ = S′
0, S′
1, S′
2, . . . that is a run of {(a, asmc
a)}a∈A ∪
{(db, asmdb)} such that for each agent a ∈A the agent a-view of R′ coincides with a ﬂat view
of R by a. Let ∆′
ℓbe the update set deﬁned by S′
ℓ+ ∆′
ℓ= S′
ℓ+1. Deﬁne
∆ℓ= {((pi,j,d,j′, k), (v, tℓ)) | ((pi, k), v) ∈∆′
ℓ∧copy(i, j, d, j′) ∧hi(k) ∈rangej}
using timestamps t0 < t1 < t2 < . . . . This deﬁnes a run ¯R = ¯S0, ¯S1, . . . of CM2 with
¯S0 = S0 and ¯Sℓ+1 = ¯Sℓ+ ∆ℓ. In this run the answer to a read request is executed in a single
step and all updates requested by a write request are executed in a single step. Thus R′ is
serial.
Furthermore, as for each agent a ∈A the agent a-view of R′ coincides with a ﬂat view
of R by a, the runs runs R and ¯R contain exactly the same requests and responses, and for
each agent a the sequence of its requests and responses is identical in both runs. That is, R
and ¯R are view equivalent.
⊓⊔
We can ﬁnally also show the inverse of the implication in Proposition 4, provided that an
appropriate combination of read- and write-policies is used.
Proposition 5. If all runs of CM2 are view serialisable and an appropriate combination of
a read and a write policy is used, then CM2 is also view compatible with the concurrent ASM
CM0 = {(a, asmc
a)}a∈A ∪{(db, asmdb)}.
Proof.
Let R′ be a run of CM2 and let R′ = S0, S1, . . . be a view equivalent serial run. It
suﬃces to show that that there exists a subsequence of a ﬂattening R′ = S′
0, S′
1, S′
2, . . . that
is a run of {(a, asmc
a)}a∈A ∪{(db, asmdb)} such that for each agent a ∈A the agent a-view of
R′ coincides with a ﬂat view of R by a.
For this we only have to consider states, in which a request or a response is issued to
obtain the desired subsequence, and the ﬂattening is deﬁned by the answers to the write
requests. As R is serial, the condition that for each agent a the a-view concides with a ﬂat
a-view follows immediately.
⊓⊔
21


## Page 22


5
Conclusions
In this paper we demonstrated the maturity of concurrent communicating ASMs (ccASMs)
[7,8] showing how they can be used to specify and analyse concurrent computing systems in
connection with shared replicated memory. Using ccASMs we ﬁrst speciﬁed a ground model,
in which all access to replicas is handled synchronously in parallel by a single agent.
We then reﬁned our ground model addressing the internal communication in the memory
management subsystem. This reﬁnement signiﬁcantly changes the way requests are handled,
as the replicas are not selected a priori in a way that complies with the read- or write-policy,
but instead the acknowledgement and return of a response depends on these policies. This
adds an additional level of ﬂexibility to the internal request handling.
We used the speciﬁcation to analyse consistency and showed that consistency, formalised
by the notion of view compatibility, cannot be preserved by the reﬁnement. To the contrary,
we could show that even such a rather weak notion of consistency can only be obtained by
adopting transactions for at least single requests.
The reﬁnements could be taken further to capture more and more details of the physical
data organisation. For instance, we did not yet tackle the means for handling inactive nodes
and for recovery. Nonetheless, while our reﬁned speciﬁcation is still rather abstract, it shows
the way how concurrent systems interact with replicative memory management subsystems,
and permits analysis of which consistency level can be obtained.
It seems straightforward to combine a transactional concurrent system as for example in
[9] with the speciﬁcation of a replicative storage system as done in this paper. In particular, it
is well known that replication strategies can be easily combined with transaction management.
This would then enable stronger consistency results.
References
1. G. Agha. A Model of Concurrent Computation in Distributed Systems. MIT Press, Cambridge, Mass.,
1986.
2. W. An. Formal speciﬁcation and analysis of asynchronous mutual exclusion algorithms. Master’s thesis,
JKU Linz, Austria, 2016.
3. E. Best. Semantics of sequential and parallel programs. Prentice Hall, 1996.
4. A. Blass and Y. Gurevich. Abstract State Machines capture parallel algorithms. ACM Trans. Computa-
tional Logic, 4(4):578–651, 2003.
5. A. Blass and Y. Gurevich. Abstract State Machines capture parallel algorithms: Correction and extension.
ACM Trans. Comp. Logic, 9(3), 2008.
6. E. B¨orger, A. Cisternino, and V. Gervasi. Ambient abstract state machines with applications. J. Comput.
Syst. Sci., 78(3):939–959, 2012.
7. E. B¨orger and K.-D. Schewe. Concurrent abstract state machines. Acta Inf., 53(5):469–492, 2016.
8. E. B¨orger and K.-D. Schewe. Communication in Abstract State Machines. J. Univ. Comp. Sci., 23(2):129–
145, 2017.
9. E. B¨orger, K.-D. Schewe, and Q. Wang. Serialisable multi-level transaction control: A speciﬁcation and
veriﬁcation. Sci. Comput. Program., 131:42–58, 2016.
10. E. B¨orger and R. F. St¨ark. Abstract State Machines. A Method for High-Level System Design and Analysis.
Springer, 2003.
11. F. Ferrarotti, K.-D. Schewe, L. Tec, and Q. Wang. A new thesis concerning synchronised parallel computing
– simpliﬁed parallel ASM thesis. Theor. Comp. Sci., 649:25–53, 2016.
12. H. J. Genrich and K. Lautenbach. System modelling with high-level Petri nets. Theoretical Computer
Science, 13:109–136, 1981.
13. Y. Gurevich. Evolving algebras 1993: Lipari guide. In E. B¨orger, editor, Speciﬁcation and Validation
Methods. Oxford University Press, 1995.
22


## Page 23


14. Y. Gurevich. Sequential abstract-state machines capture sequential algorithms. ACM Trans. Comp. Logic,
1(1):77–111, 2000.
15. L. Lamport. Time, clocks, and the ordering of events in a distributed system. Commun. ACM, 21(7):558–
565, 1978.
16. L. Lamport and N. Lynch. Distributed Computing: Models and Methods, chapter Handbook of Theoretical
Computer Science, pages 1157–1199. Elsevier, 1990.
17. N. Lynch. Distributed Algorithms. Morgan Kaufmann, 1996.
18. A. Mazurkiewicz. Trace theory. volume 255 of LNCS, pages 279–324. Springer, 1987.
19. M. T. ¨Ozsu and P. Valduriez. Principles of Distributed Database Systems, Third Edition. Springer, 2011.
20. A. Prinz and E. Sherratt. Distributed ASM – pitfalls and solutions. In Y. A¨ıt-Ameur and K.-D. Schewe,
editors, Abstract State Machines, Alloy, B, TLA, VDM and Z – Proceedings of the 4th International
Conference (ABZ 2014), volume 8477 of LNCS, pages 210–215. Springer, 2014.
21. T. Rabl, M. Sadoghi, H.-A. Jacobsen, S. G´omez-Villamor, V. Munt´es-Mulero, and S. Mankowskii. Solving
big data challenges for enterprise application performance management. PVLDB, 5(12):1724–1735, 2012.
22. K.-D. Schewe, F. Ferrarotti, L. Tec, Q. Wang, and W. An. Evolving concurrent systems – behavioural
theory and logic.
In Proceedings of the Australasian Computer Science Week Multiconference (ACSW
2017), pages 77:1–77:10. ACM, 2017.
23. K.-D. Schewe and Q. Wang. A customised ASM thesis for database transformations. Acta Cyb., 19(4):765–
805, 2010.
24. K.-D. Schewe and Q. Wang. XML database transformations. J. Univ. Comp. Sci., 16(20):3043–3072,
2010.
25. A. S. Tanenbaum and M. Van Steen. Distributed systems. Prentice-Hall, 2007.
26. G. Winskel and M. Nielsen. Models for concurrency. In S. Abramsky, D. Gabbay, and T. S. E. Maibaum,
editors, Handbook of Logic and the Foundations of Computer Science: Semantic Modelling, volume 4, pages
1–148. Oxford University Press, 1995.
23

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]