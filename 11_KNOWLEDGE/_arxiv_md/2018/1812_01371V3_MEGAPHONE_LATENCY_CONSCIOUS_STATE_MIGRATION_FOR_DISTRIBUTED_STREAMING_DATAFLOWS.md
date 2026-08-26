---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1812.01371v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1812.01371v3_Megaphone__Latency-conscious_state_migration_for_distributed_streaming_dataflows

> Source: 1812.01371v3_Megaphone__Latency-conscious_state_migration_for_distributed_streaming_dataflows.pdf

> Pages: 14

---


## Page 1


Megaphone: Latency-conscious state migration for
distributed streaming dataﬂows
Moritz Hoffmann
Andrea Lattuada
Frank McSherry
Vasiliki Kalavri
John Liagouris
Timothy Roscoe
Systems Group, ETH Zurich
ﬁrst.last@inf.ethz.ch
ABSTRACT
We design and implement Megaphone, a data migration mechanism
for stateful distributed dataﬂow engines with latency objectives.
When compared to existing migration mechanisms, Megaphone has
the following differentiating characteristics: (i) migrations can be
subdivided to a conﬁgurable granularity to avoid latency spikes, and
(ii) migrations can be prepared ahead of time to avoid runtime coor-
dination. Megaphone is implemented as a library on an unmodiﬁed
timely dataﬂow implementation, and provides an operator interface
compatible with its existing APIs. We evaluate Megaphone on estab-
lished benchmarks with varying amounts of state and observe that
compared to na¨ıve approaches Megaphone reduces service latencies
during reconﬁguration by orders of magnitude without signiﬁcantly
increasing steady-state overhead.
PVLDB Reference Format:
Moritz Hoffmann, Andrea Lattuada, Frank McSherry, Vasiliki Kalavri, John
Liagouris, and Timothy Roscoe. Megaphone: Live state migration for dis-
tributed streaming dataﬂows. PVLDB, 12(xxx): xxxx-yyyy, 2019.
DOI: https://doi.org/10.14778/xxxxxxx.xxxxxxx
1
Introduction
Distributed stream processing jobs are long-running dataﬂows that
continually ingest data from sources with dynamic rates and must
produce timely results under variable workload conditions [1, 3].
To satisfy latency and availability requirements, modern stream
processors support consistent online reconﬁguration, in which they
update parts of a dataﬂow computation without disrupting its execu-
tion or affecting its correctness. Such reconﬁguration is required dur-
ing rescaling to handle increased input rates or reduce operational
costs [15, 16], to provide performance isolation across different
dataﬂows by dynamically scheduling queries to available workers,
to allow code updates to ﬁx bugs or improve business logic [7, 9],
and to enable runtime optimizations like execution plan switch-
ing [30] and straggler and skew mitigation [14].
Streaming dataﬂow operators are often stateful, partitioned across
workers by key, and their reconﬁguration requires state migration:
intermediate results and data structures must be moved from one
set of workers to another, often across a network. Existing state mi-
gration mechanisms for stream processors either pause and resume
This
work
is
licensed
under
the
Creative
Commons
Attribution-
NonCommercial-NoDerivatives 4.0 International License. To view a copy
of this license, visit http://creativecommons.org/licenses/by-nc-nd/4.0/. For
any use beyond those covered by this license, obtain permission by emailing
info@vldb.org. Copyright is held by the owner/author(s). Publication rights
licensed to the VLDB Endowment.
Proceedings of the VLDB Endowment, Vol. 12, No. xxx
ISSN 2150-8097.
DOI: https://doi.org/10.14778/xxxxxxx.xxxxxxx
100
101
102
103
104
105
 780  800  820  840
Latency [ms]
Time [s]
All-at-once (prior work)
max
p: 0.99
p: 0.5
p: 0.25
 780  800  820  840
Time [s]
Megaphone (fluid)
 780  800  820  840
Time [s]
Megaphone (optimized)
Figure 1: A comparison of service latencies in prior coarse-grained
migration strategies (all-at-once) with two of Megaphone’s ﬁne-
grained migration strategies (ﬂuid and optimized), for a workload
that migrates one billion keys consisting of 8GB of data.
parts of the dataﬂow (as in Flink [10], Dhalion [16], and SEEP [15])
or launch new dataﬂows alongside the old conﬁguration (as for ex-
ample in ChronoStream [28] and Gloss [24]). In both cases state
moves “all-at-once,” with either high latency or resource usage dur-
ing the migration.
State migration has been extensively studied for distributed data-
bases [8, 11, 13, 12]. Notably, Squall [12] uses transactions to mul-
tiplex ﬁne-grained state migration with data processing. These tech-
niques are appealing in spirit, but use mechanisms (transactions,
locking) not available in high-throughput stream processors and are
not directly applicable without signiﬁcant performance degradation.
In this paper we present Megaphone, a technique for ﬁne-grained
migration in a stream processor which delivers maximum laten-
cies orders of magnitude lower than existing techniques, based on
the observation that a stream processor’s structured computation
and logical timestamps allow the system to plan ﬁne-grained migra-
tions. Megaphone can specify migrations on a key-by-key basis, and
then optimizes this by batching at varying granularities; as Figure 1
shows, the improvement over all-at-once migration can be dramatic.
This paper is an extended version of a preliminary workshop publi-
cation [19]. In this paper, we describe a more general mechanism,
further detail its implementation, and evaluate it more thoroughly
on realistic workloads.
Our main contribution is ﬂuid migration for stateful streaming
dataﬂows: a state migration technique that enables consistent on-
line reconﬁguration of streaming dataﬂows and smoothens latency
spikes without using additional resources (Section 3) by employing
ﬁne-grained planning and coordination through logical timestamps.
Additionally, we design and implement an API for reconﬁgurable
stateful timely dataﬂow operators that enables ﬂuid migration to be
1
arXiv:1812.01371v3  [cs.DC]  16 Apr 2019


## Page 2


controlled simply through additional dataﬂow streams rather than
through changes to the dataﬂow runtime itself (Section 4). Finally,
we show that Megaphone has negligible steady-state overhead and
enables fast direct state movement using the NEXMark benchmarks
suite and microbenchmarks (Section 5).
Megaphone is built on timely dataﬂow,1 and is implemented
purely in library code, requiring no modiﬁcations to the underly-
ing system. We ﬁrst review existing state migration techniques in
streaming systems, which either cause performance degradation or
require resource overprovisioning. We also review live migration in
DBMSs and identify the technical challenges to implement similar
methods in distributed stream processors (Section 2).
2
Background and Motivation
A distributed dataﬂow computation runs as a physical execution
plan which maps operators to provisioned compute resources (or
workers). The execution plan is a directed graph whose vertices
are operator instances (each on a speciﬁc worker) and edges are
data channels (within and across workers). Operators can be state-
less (e.g., ﬁlter, map) or stateful (e.g., windows, rolling aggregates).
State is commonly partitioned by key across operator instances so
that computations can be executed in a data-parallel manner. At
each point in time of a computation, each worker (with its associ-
ated operator instances) is responsible for a set of keys and their
associated state.
State migration is the process of changing the assignment of
keys to workers and redistributing respective state accordingly. A
good state migration technique should be non-disruptive (minimal
increase in response latency during migration), short-lived (migra-
tion completes within a short period of time), and resource-efﬁcient
(minimal additional resources required during the migration).
We present an overview of existing state migration strategies in
distributed streaming systems and identify their limitations. We then
review live state migration methods adopted by database systems
and provide an intuition into Megaphone’s approach to bring such
migration techniques to streaming dataﬂows.
2.1
State migration in streaming systems
Distributed stream processors, including research prototypes and
production-ready systems, use one of the following three state mi-
gration strategies.
Stop-and-restart A straight-forward way to realize state migra-
tion is to temporarily stop program execution, safely transfer state
when no computation is being performed, and restart the job once
state redistribution is complete. This approach is most commonly
enabled by leveraging existing fault-tolerance mechanisms in the
system, such as global state checkpoints. It is adopted by Spark
Streaming [29], Structured Streaming [7], and Apache Flink [9].
Partial pause-and-resume In many reconﬁguration scenarios only
one or a small number of operators need to migrate state, and halt-
ing the entire dataﬂow is usually unnecessary. An optimization ﬁrst
introduced in Flux [26] and later adopted in variations by Seep [15],
IBM Streams [2], StreamCloud [17], Chi [21], and FUGU [18],
pauses the computation only for the affected dataﬂow subgraph.
Operators not participating in the migration continue without inter-
ruption. This approach can use fault-tolerance checkpoints for state
migration as in [15, 21] or state can be directly migrated between
operators as in [17, 18].
1https://github.com/frankmcsherry/timely-dataflow
Dataﬂow Replication To minimize performance penalties, some
systems replicate the whole dataﬂow or subgraphs of it and exe-
cute the old and new conﬁgurations in parallel until migration is
complete. ChronoStream [28] concurrently executes two or more
computation slices and can migrate an arbitrary set of keys between
instances of a single dataﬂow operator. Gloss [24] follows a similar
approach and gathers operator state during a migration in a central-
ized controller using an asynchronous protocol.
Current systems fall short of implementing state migration in a
non-disruptive and cost-efﬁcient manner. Existing stream proces-
sors migrate state all-at-once, but differ in whether they pause the
existing computation or start a concurrent computation. As Figure 1
shows, strategies that pause the computation can cause high latency
spikes, especially when the state to be moved is large. On the other
hand, dataﬂow replication techniques reduce the interruption, but at
the cost of high resource requirements and required support for in-
put duplication and output de-duplication. For example, for Chrono-
Stream to move from a conﬁguration with x instances to a new one
with y instances, x + y instances are required during the migration.
2.2
Live migration in database systems
Database systems have implemented optimizations that explicitly
target limitations we have identiﬁed in the previous section, namely
unavailability and resource requirements. Even though streaming
dataﬂow systems differ signiﬁcantly from databases in terms of data
organization, workload characteristics, latency requirements, and
runtime execution, the fundamental challenges of state migration
are common in both setups.
Albatross [11] adopts VM live migration techniques and is fur-
ther optimized in [8] with a dynamic throttling mechanism, which
adapts the data transfer rate during migration so that tenants in the
source node can always meet their SLOs. Prorea [25] combines
push-based migration of hot pages with pull-based migration of cold
pages techniques. Zephyr [13] proposes a technique for live migra-
tion in shared-nothing transactional databases which introduces no
system downtime and does not disrupt service for non-migrating
tenants.
The most sophisticated approach is Squall [12], which interleaves
state migration with transaction processing by (in part) using trans-
action mechanisms to effect the migration. Squall introduces a num-
ber of interesting optimizations, such as pre-fetching and splitting
reconﬁgurations to avoid contention on a single partition. In the
course of a migration, if migrating records are needed for process-
ing but not yet available, Squall introduces a transaction to acquire
the records (completing their migration). This introduces latency
along the critical path, and the transaction locking mechanisms can
impede throughput, but the system is neither paused nor replicated.
To the best of our knowledge, no stream processor implements such
a ﬁne-grained migration technique.
2.3
Live migration for streaming dataﬂows
Applying existing ﬁne-grained live migration techniques to a stream-
ing engine is non-trivial. While systems like Squall target OLTP
workloads with short-lived transactions, streaming jobs are long-
running. In such a setting, Squall’s approach to acquire a global
lock during initialization is not a viable solution. Further, many of
Squall’s remedies are reactive rather than proactive (because it must
support general transactions whose data needs are hard to antici-
pate), which can introduce signiﬁcant latency on the critical path.
The core idea behind Megaphone’s migration mechanism is to
multiplex ﬁne-grained state migration with actual data processing,
coordinated using logical timestamps common in stream proces-
sors. This is a proactive approach to migration that relies on the
2


## Page 3


Logical graph
A
H(m)
B
C
Worker 0
A0
B0
C0
Worker 1
A1
B1
C1
Worker 2
A2
B2
C2
Worker 3
A3
B3
C3
×
Process 0
Process 1
Figure 2: Timely dataﬂow execution model
prescribed structure of streaming computations, and the ability of
stream processors to coordinate with high frequency using logical
timestamps. Such systems, including Megaphone, avoid the need
for system-wide locks by pre-planning the rendezvous of data at
speciﬁc workers.
3
State migration design
Megaphone’s features rely on core streaming dataﬂow concepts
such as logical time, progress tracking, data-parallel operators, and
state management. Basic implementations of these concepts are
present in all modern stream processors, such as Apache Flink [10],
Millwheel [5], and Google Dataﬂow [6]. In the following, we rely
on the Naiad [22] timely dataﬂow model as the basis to describe
the Megaphone migration mechanism. Timely dataﬂow natively
supports a superset of dataﬂow features found in other systems in
their most general form.
3.1
Timely dataﬂow concepts
A streaming computation in Naiad is expressed as a timely dataﬂow:
a directed (possibly cyclic) graph where nodes represent stateful
operators and edges represent data streams between operators. Each
data record in timely dataﬂow bears a logical timestamp, and oper-
ators maintain or possibly advance the timestamps of each record.
Example timestamps include integers representing milliseconds or
transaction identiﬁers, but in general can be any set of opaque val-
ues for which a partial order is deﬁned. The timely dataﬂow system
tracks the existence of timestamps, and reports as processed time-
stamps no longer exist in the dataﬂow, which indicates the forward
progress of a streaming computation.
A timely dataﬂow is executed by multiple workers (threads) be-
longing to one or more OS processes, which may reside in one
or more machines of a networked cluster. Workers communicate
with each other by exchanging messages over data channels (shared-
nothing paradigm) as shown in Figure 2. Each worker has a local
copy of the entire timely dataﬂow graph and executes all operators in
this graph on (disjoint) partitions of the dataﬂow’s input data. Each
worker repeatedly executes dataﬂow operators concurrent with other
workers, sending and receiving data across data exchange channels.
Due to this asynchronous execution model, the presence of concur-
rent “in-ﬂight” timestamps is the rule rather than the exception.
As timely workers execute, they communicate the numbers of
logical timestamps they produce and consume to all other workers.
This information allows each worker to determine the possibility
that any dataﬂow operator may yet see any given timestamp in its
input. The timely workers present this information to operators in
the form of a frontier:
Deﬁnition 1. A frontier F is a set of logical timestamps such that
1. no element of F is strictly greater than another element of F,
2. all timestamps on messages that may still be received are
greater than or equal to some element of F.
In many simple settings a frontier is analogous to a low water-
mark in streaming systems like Flink, which indicates the single
smallest timestamp that may still be received. In timely dataﬂow a
frontier must be set-valued rather than a single timestamp because
timestamps may be only partially ordered.
Operators in timely dataﬂow may retain capabilities that allow
the operator to produce output records with a given timestamp. All
received messages come bearing such a capability for their time-
stamp. Each operator can choose to drop capabilities, or downgrade
them to later timestamps. The timely dataﬂow system tracks capa-
bilities held by operators, and only advances downstream frontiers
as these capabilities advance.
Timely dataﬂow frontiers are the main mechanism for coordina-
tion between otherwise asynchronous workers. The frontiers indi-
cate when we can be certain that all messages of a certain timestamp
have been received, and it is now safe to take any action that needed
to await their arrival. Importantly, frontier information is entirely
passive and does not interrupt the system execution; it is up to op-
erators to observe the frontier and determine if there is some work
that cannot yet be performed. This enables very ﬁne-grained coordi-
nation, without system-level intervention. Further technical details
of progress tracking in timely dataﬂows can be found in [22, 4].
We will use timely dataﬂow frontiers to separate migrations into
independent arbitrarily ﬁne-grained timestamps and logically co-
ordinate data movement without using coarse-grained pause-and-
resume for parts of the dataﬂow.
3.2
Migration formalism and guarantees
To frame the mechanism we introduce for live migration in stream-
ing dataﬂows, we ﬁrst lay out some formal properties that deﬁne
correct and live migration. In the interest of clarity we keep the
descriptions casual, but each can be formalized.
We consider stateful dataﬂow operators that are data-parallel
and functional. Speciﬁcally, an operator acts on input data that are
structured as (key, val) pairs, each bearing a logical timestamp. The
input is partitioned by its key and the operator acts independently on
each input partition by sequentially applying each val to its state in
timestamp order. For each key, for each val in timestamp order, the
operator may change its per-key state arbitrarily, produce arbitrary
outputs as a result, and it may schedule further per-key changes at
future timestamps (in effect sending itself a new, post-dated val for
this key).
operatorkey : (state, val) →(state′, [outputs], [(vals, times)])
The output triples are the new state, the outputs to produce, and
future changes that should be presented to the operator.
For a speciﬁc operator, we can describe the correctness of an
implementation. We introduce the notation of in advance of as fol-
lows.
Deﬁnition 2 (in advance of). A timestamp t is in advance of
1. a timestamp t′ if t is greater than or equal to t′;
2. a frontier F if t is greater than or equal to an element of F.
In-advance-of corresponds to the less-or-equal relation for par-
tially ordered sets. For example, a time 6 is in advance of 5.
Property 1 (Correctness). The correct outputs through time are
the timestamped outputs that result from each key from the time-
stamp-ordered application of input and post-dated records bearing
timestamp not in advance of time.
3


## Page 4


For each migrateable operator, we also consider a conﬁguration
function, which for each timestamp assigns each key to a speciﬁc
worker.
conﬁguration: (time, key) →worker
For example, the conﬁguration function could assign a key a to
worker 2 for times [4, 8) and to worker 1 for times [8, 16).
With a speciﬁc conﬁguration, we can describe the correctness of
a migrating implementation.
Property 2 (Migration). A computation is migrated according
to conﬁguration if all updates to key with timestamp time are per-
formed at worker conﬁguration(time, key).
A conﬁguration function can be represented in many ways, which
we will discuss further. In our context we will communicate any
changes using a timely dataﬂow stream, in which conﬁguration
changes bear the logical timestamp of their migration. This choice
allows us to use timely dataﬂow’s frontier mechanisms to coordinate
migrations, and to characterize liveness.
Property 3 (Completion (liveness)). A migrating computation is
completing if, once the frontiers of both the data input stream and
conﬁguration update stream reach F, then (with no further require-
ments of the input) the output frontier of the computation will even-
tually reach F.
Our goal is to produce a mechanism that satisﬁes each of these
three properties: Correctness, Migration, and Completion.
3.3
Conﬁguration updates
State migration is driven by updates to the conﬁguration function
introduced in 3.2. In Megaphone these updates are supplied as data
along a timely dataﬂow stream, each bearing the logical timestamp
at which they should take effect. Informally, conﬁguration updates
have the form
update: (time, key, worker)
indicating that as of time the state and values associated with key
will be located at worker, and that this will hold until a new update
to key is observed with a greater timestamp. For example, an update
could have the form of (time: 16, key: a, worker: 0), which would
deﬁne the conﬁguration function for times of 16 and beyond.
As conﬁguration updates are simply data, the user has the ability
to drive a migration process by introducing updates as they see ﬁt. In
particular, they have the ﬂexibility to break down a large migration
into a sequence of smaller migrations, each of which have lower
duration and between which the system can process data records.
For example, to migrate from one conﬁguration C1 to another C2,
a user can use different migration strategies to reveal the changes
from C1 to C2:
All-at-once migration To simultaneously migrate all keys from
C1 to C2, a user could supply all changed (time, key, worker)
triples with one common time. This is essentially an imple-
mentation of the partial pause-and-restart migration strategy
of existing streaming systems as described in Section 2.1.
Fluid migration To smoothly migrate keys from C1 to C2, a user
could repeatedly choose one key changed from C1 to C2,
introduce the new (time, key, worker) triple with the current
time, and await the migration’s completion before choosing
the next key.
Batched migration To trade off low latency against high through-
put, a user can produce batches of changed (time, key, worker)
triples with a common time, awaiting the completion of the
batch before introducing the next batch of changes.
L
(time, key, value)
(a) Original L-operator in a dataﬂow.
F
S
L
re-configuration
(time, key, value)
Output 
Probe
state
routing table
data
(b) Megaphone’s operator structure in a dataﬂow.
Figure 3: Overview of Megaphone’s migration mechanism
We believe that this approach to reconﬁguration, as user-supplied
data, opens a substantial design space. Not only can users perform
ﬁne-grained migration, they can prepare future migrations at spe-
ciﬁc times, and drive migrations based on timely dataﬂow compu-
tations applied to system measurements. Most users will certainly
need assistance in performing effective migration, and we will eval-
uate several speciﬁc instances of the above strategies.
3.4
Megaphone’s mechanism
We now describe how to create a migrateable version of an opera-
tor L implementing some deterministic, data-parallel operator as
described in 3.2. A non-migrateable implementation would have a
single dataﬂow operator with a single input dataﬂow stream of (key,
val) pairs, exchanged by key before they arrive at the operator.
Instead, we create two operators F and S. F takes the data stream
and the stream of conﬁguration updates as an additional input and
produces data pairs and migrating state as outputs. The conﬁgu-
ration stream can be ingested from an external controller such as
DS2 [20] or Chi [21]. S takes as inputs exchanged data pairs and ex-
changed migrating state, and applies them to a hosted instance of L,
which implements operator and maintains both state and pending
records for each key. Figure 3b presents a schematic overview of
the construction. Recall that in timely dataﬂow instances of all op-
erators in the dataﬂow are multiplexed on each worker (core). The
F and S on the same worker share access to L’s state.
This construction can be repeated for all the operators in the
dataﬂow that need support for migration. Separate operators can be
migrated independently (via separate conﬁguration update streams),
or in a coordinated manner by re-using the same conﬁguration up-
date stream. Operators with multiple data inputs can be treated like
single-input operators where the migration mechanism acts on both
data inputs at the same time.
Operator F Operator F routes (key, val) pairs according to the
conﬁguration at their associated time, buffering pairs if time is in
advance of the frontier of the conﬁguration input. For times in ad-
vance of this frontier, the conﬁguration is not yet certain as further
conﬁguration updates could still arrive. The conﬁguration at times
not in advance of this frontier can no longer be updated. As the data
frontier advances, conﬁgurations can be retired.
Operator F is also responsible for initiating state migrations. For
a conﬁguration update (time, key, worker), F must not initiate a
migration for key until its state has absorbed all updates at times
strictly less than time. F initiates a migration once time is present
in the output frontier of S, as this implies that there exist no records
at timestamps less than time, as otherwise they would be present in
the frontier in place of time.
4


## Page 5


(44, a, 3)
c: 3
d: 9
a: 7
b: 14
F0
F1
S0
S1
a,b→1
c,d→2
input queue
Routing table:
State:
control input
44
42
42
43
(43, c, 5)
42
42
(a) Before migrating
(46, c, 8)
c: 8
d: 9
a: 10
b: 14
F0
F1
S0
S1
a,b→1
c,d→2
(45, b, 2)
50
45
45
50
(45, b, 5)
45
45
(b) Receiving a conﬁguration update
(55, a, 6)
b:19
c: 16
d: 9
a: 10
F0
F1
S0
S1
a→1
b,c,d→2
56
55
55
53
53
53
(c) After migration
Figure 4: A migrating word-count dataﬂow executed by two workers. The example is explained in more detail in Section 3.5
Operator F initiates a migration by uninstalling the current state
for key from its current location in operator S, and transmitting it
bearing timestamp time to the instance of operator S on worker.
The state includes both the state for operator, as well as the list of
pending (val, time) records produced by operator for future times.
Operator S Operator S receives exchanged (key, val) pairs and
exchanged state as the result of migrations initiated by F. S imme-
diately installs any received state. S applies received and pending
(key, val) pairs in timestamp order using operator once their time-
stamp is not in advance of either the data or state inputs.
We provide details of Megaphone’s implementation of this mech-
anism in Section 4.
Proof sketch For each key, operatorkey deﬁnes a timeline corre-
sponding to a single-threaded execution, which assigns to each time
a pair (state, [(val, time)]) of state and pending records just before
the application of input records at that time. Let P(t) denote the
function from times to these pairs for key.
For each key, the conﬁguration function partitions this timeline
into disjoint intervals, [ta, tb), each of which is assigned to one op-
erator instance Sa.
Claim: F migrates exactly P(ta) to Sa.
First, F always routes input records at time to Sa, and so routes
all input records in [ta, tb) to Sa. If F also presents Sa with P(ta),
it has sufﬁcient input to produce P(tb). More precisely,
1. Because F maintains its output frontier at tb, in anticipation
of the need to migrate P(tb), Sa will apply no input records
in advance of tb. And so, it applies exactly the records in
[ta, tb).
2. Until Sa transitions to P(tb), its output frontier will be strictly
less than tb, and so F will not migrate anything other than
P(tb).
3. Because F maintains its output frontier at tb, and Sa is able
to advance its output frontier to tb, the time tb will eventually
be in the output frontier of S.
3.5
Example
Figure 4 presents three snapshots of a migrating streaming word-
count dataﬂow. The ﬁgure depicts operator instances F0 and F1 of
the upstream routing operator, and operator instances S0 and S1
of the operator instances hosting the word-count state and update
logic. The F operators maintain input queues of received but not yet
routable input data, and an input stream of logically timestamped
conﬁguration updates. Although each F maintains its own routing
table, which may temporarily differ from others, we present one
for clarity. Input frontiers are represented by boxed numbers, and
indicate timestamps that may still arrive on that input.
In Figure 4a, F0 has enqueued the record (44, a, 3) and F1 has
enqueued the record (43, c, 5), both because their control input fron-
tier has only reached 42 and so the destination workers at their
associated timestamps have not yet been determined. Generally, F
instances will only enqueue records with timestamps in advance of
the control input frontier, and the output frontiers of the S instances
can reach the minimum of the data and control input frontiers.
In Figure 4b, both control inputs have progressed to 45. The
buffered records (44, a, 3) and (43, c, 5) have been forwarded to
S1 and S2, and the count operator instances apply the state updates
accordingly, shown in bold. Additionally, both operators have re-
ceived a conﬁguration update for the key b at time 45. Should the
conﬁguration input frontier advance beyond 45, both F0 and F1
can integrate the conﬁguration change, and then react. Operator F0
would observe that the output frontier of S0 reaches 45, and initiate
a state migration. Operator F1 would route its buffered input at time
45, to S1 rather than S0.
In Figure 4c the migration has completed. Although the conﬁgu-
ration frontier has advanced to 55, the output frontiers are held back
by the data input frontier of F1 at 53. According to Deﬁnition 1,
the frontier guarantees that no record with a time earlier than 53
will appear at the input. If the conﬁguration frontier advances past
55 then operator F0 could route its queued record, but neither S
operator could apply it until they are certain that there are no other
data records that could come before the record at 55.
4
Implementation
Megaphone is an implementation of the migration mechanism de-
scribed in Section 3. In this section, we detail speciﬁc choices
made in Megaphone’s implementation, including the interfaces used
by the application programmer, Megaphone’s speciﬁc choices for
the grouping and organization of per-key state, and how we imple-
mented Megaphone’s operators in timely dataﬂow. We conclude
with some discussion of how one might implement Megaphone in
other stream processing systems, as well as alternate implementa-
tion choices one could consider.
4.1
Megaphone’s operator interface
Megaphone presents users with an operator interface that closely re-
sembles the operator interfaces timely dataﬂow presents. In several
cases, users can use the same operator interface extended only with
an additional input stream for conﬁguration updates. More gener-
ally, we introduce a new structure to help users isolate and surface
all information that must be migrated (state, but also pending future
records). These additions are implemented strictly above timely
dataﬂow, but their structure is helpful and they may have value in
timely dataﬂow proper.
5


## Page 6


fn state_machine(
control: Stream<ControlInstr>,
input: Stream<(K, V)>,
exchange: K -> Integer
fold: |Key, Val, State| -> List<Output>
) -> Stream<Output>;
fn unary(
control: Stream<ControlInstr>,
input: Stream<Data>,
exchange: Data -> Integer,
fold: |Time, Data, State, Notificator| -> List<Output>
) -> Stream<Output>;
fn binary(
control: Stream<ControlInstr>,
input1: Stream<Data1>, input2: Stream<Data2>,
exchange1: Data1 -> Integer,
exchange2: Data2 -> Integer,
fold: |Time, Data1, Data2, State, Notificator1,
Notificator2| -> List<Output>
) -> Stream<Output>;
Listing 1: Abstract deﬁnition of the Megaphone operator interfaces.
Arguments State and Notificator are provided as mutable
references which can be operated upon.
The simplest stateful operator interface Megaphone and timely
provide is the state_machine operator, which takes one input
structured as pairs (key, val) and a state update function which can
produce arbitrary output as it changes per-key state in response to
keys and values. In Megaphone, there is an additional input for con-
ﬁguration updates, but the operator signature is otherwise identical.
More generally, timely dataﬂow supports operators of arbitrary
numbers and types of inputs, containing arbitrary user logic, and
maintaining arbitrary state. In each case a user must specify a func-
tion from input records to integer keys, and the only guarantee
timely dataﬂow provides is that records with the same key are routed
to the same worker. Operator execution and state are partitioned by
worker, but not necessarily by key.
For Megaphone to isolate and migrate state and pending work
we must encourage users to yield some of the generality timely
dataﬂow provides. However, timely dataﬂow has already required
the user to program partitioned operators, each capable of hosting
multiple keys, and we can lean on these idioms to instantiate more
ﬁne-grained operators, partitioned not only by worker but further
into ﬁner-grained bins of keys. Routing functions for each input are
already required by timely dataﬂow, and Megaphone interposes to
allow the function to change according to reconﬁguration. Timely
dataﬂow per-worker state is deﬁned implicitly by the state captured
by the operator closure, and Megaphone only makes it more explicit.
The use of a helper to enqueue pending work is borrowed from an
existing timely dataﬂow idiom (the Notificator). While Mega-
phone’s general API is not identical to that of timely dataﬂow, it is
just a more crisp framing of the same idioms.
Listing 1 shows how Megaphone’s operator interface is struc-
tured. The interface declares unary and binary stateful operators for
single input or dual input operators as well as a state-machine op-
erator. The logic for the state-machine operator has to be encoded
in the fold-function. Megaphone presents data in timestamp order
with a corresponding state and notiﬁcator object. Here, migration is
transparent and performed without special handling by the operator
implementation.
Example Listing 2 shows an example of a stateful word-count data-
ﬂow with a single data input and an additional control input. The
stateful unary operator receives the control input, the state
type, and a key extraction function as parameters. The control input
worker.dataflow(|scope| {
// Introduce configuration and input streams.
let conf = conf_input.to_stream(scope);
let text = text_input.to_stream(scope);
// Update per-word accumulate counts.
let count_stream = megaphone::unary(
conf,
text,
|(word, diff)| hash(word),
|time, data, state, notificator| {
// map each (word, diff) pair to the accumulation.
data.map(|(word, diff)| {
let mut count = state.entry(word).or_insert(0);
*count += diff;
(word, count)
})
}
);
});
Listing 2: A stateful word-count operator. The operator reads (word,
diff)-pairs and outputs the accumulated count of each encountered
word. For clarity, the example suppresses details related to Rust’s
data ownership model.
carries information about where data is to be routed as discussed in
the previous section. During migration, the state object is converted
into a stream of serialized tuples, which are used to reconstruct the
object on the receiving worker. State is managed in groups of keys,
i.e. many keys of input data will be mapped to the same state object.
The key extraction function deﬁnes how this key can be extracted
from the input records.
4.2
State organization
State migration as deﬁned in Section 3.2 is deﬁned on a per-key
granularity. In a typical streaming dataﬂow, the number of keys can
be large in the order of million or billions of keys. Managing each
key individually can be costly and thus we selected to group keys
into bins and adapt the conﬁguration function as follows:
conﬁguration : (time, bin) →worker.
Additionally, each key is statically assigned to one equivalence class
that identiﬁes the bin it belongs to.
In Megaphone, the number of bins is conﬁgurable in powers of
two at startup but cannot be changed during run-time. A stateful
operator gets to see a bin that holds data for the equivalence class
of keys for the current input. Bins are simply identiﬁed by a num-
ber, wich corresponds to the most signiﬁcant bits of the exchange
function speciﬁed on the operator.2
Megaphone’s mechanism requires two distinct operators, F and
S. The operator S maintains the bins local to a worker and passes
references to the user logic L. Nevertheless, the S-operator does not
have a direct channel to its peers. For this reason, F can obtain a
reference to bins by means of a shared pointer. During a migration,
F serializes the state obtained via the shared pointer and sends it
to the new owning S-operator via a regular timely dataﬂow chan-
nel. Note that sharing a pointer between two operators requires the
operators to be executed by the same process (or thread to avoid
synchronization), which is the case for timely dataﬂow.
2Otherwise, keys with similar least-signiﬁcant bits are mapped to
the same bin; Rust’s HashMap-implementation suffers from colli-
sions for keys with similar least-signiﬁcant bits.
6


## Page 7


4.3
Timely instantiation
In timely dataﬂow, data is exchanged according to an exchange func-
tion, which takes some data and computes an integer representation:
exchange : data →Integer.
Timely dataﬂow uses this value to decide where to send tuples. In
Megaphone, instead of assigning data to a worker based on the ex-
change function, we introduce an indirection layer where bins are
assigned to workers. That way, the exchange function for the chan-
nels from F to S is by a speciﬁc worker identiﬁer.
Monitoring output frontiers Megaphone ties migrations to logi-
cal time and a computation’s progress. A reconﬁguration at a spe-
ciﬁc time is only to be applied to the system once all data up to that
time has been processed. The F operators access this information
by monitoring the output frontier of the S operators. Speciﬁcally,
timely dataﬂow supports probes as a mechanism to observe progress
on arbitrary dataﬂow edges. Each worker attaches a probe to the
output stream of the S operators, and provides the probe to its F
operator instance.
Capturing timely idioms For Megaphone to migrate state, it re-
quires clear isolation of per-key state and pending records. Although
timely dataﬂow operators require users to write operators that can
be partitioned across workers, they do not require the state and pend-
ing records to be explicitly identiﬁed. To simplify programming mi-
grateable operators, we encapsulate several timely dataﬂow idioms
in a helper structure that both manages state and pending records
for the user, and surfaces them for migration.
Timely dataﬂow has a Notificator type that allows an operator
to indicate future times at which the operator may produce output,
but without encapsulating the keys, states, or records it might use.
We implemented an extended notiﬁcator that buffers future triples
(time, key, val) and can replay subsets for times not in advance of an
input frontier. Internally the triples are managed in a priority queue,
unlike in timely dataﬂow, which allows Megaphone to efﬁciently
maintain large numbers of future triples. By associating data (keys,
values) with the times, we relieve the user from maintaining this
information on the side. As we will see, Megaphone’s notiﬁcator
can result in a net reduction in implementation complexity, despite
eliciting more information from the user.
4.4
Discussion
Up to now, we explained how to map the abstract model of Mega-
phone to an implementation. The model leaves many details to the
implementation, several of which have a large effect on an imple-
mentation’s run-time performance. Here, we want to point out how
they interact with other features of the underlying system, what pos-
sible alternatives are and how to integrate Megaphone into a larger,
controller-based system.
Other systems We implemented Megaphone in timely dataﬂow,
but the mechanisms could be applied on any sufﬁciently expressive
stream processor with support for event time, progress tracking, and
state management. Speciﬁcally, Megaphone relies on the ability of
F operators to 1. observe timestamp progress at other locations in
the dataﬂow, and 2. to extract state from downstream S operators
for migration. With regard to ﬁrst requirement, systems with out-of-
band progress tracking like Millwheel [5] and Google Dataﬂow [6]
also provide the capability to observe dataﬂow progress externally,
while systems with in-band watermaks like Flink would need to pro-
vide an additional mechanism. Extracting state from downstream
operators is straight-forward in timely dataﬂow where workers man-
age multiple operators. In systems where each thread of control
manages a single operator external coordination and communica-
tion mechanisms could be used to effect the same behavior.
Fault tolerance Megaphone is a library built on timely dataﬂow
abstractions, and inherits fault-tolerance guarantees from the sys-
tem. For example, the Naiad implementation of timely dataﬂow
provides system-wide consistent snapshots, and a Megaphone im-
plementation on Naiad would inherit fault tolerance. At the same
time, Megaphone’s migration mechanisms effectively provide pro-
grammable snapshots on ﬁner granularities, which could feed back
into ﬁner-grained fault-tolerance mechanisms.
Alternatives to binning Megaphone’s implementation uses bin-
ning to reduce the complexity of the conﬁguration function. An
alternative to a static mapping of keys to bins could be achieved
by the means of a preﬁx tree (e.g., a longest-preﬁx match as in In-
ternet routing tables). Extending the functionality of bins to split
bins into smaller sets or merge smaller sets into larger bins would
allow run-time reconﬁguration of the actual binning strategy rather
than setting it up during initialization without the option to change
it later on.
Migration controller We implemented Megaphone as a system
that provides an input for conﬁguration updates to be supplied by
an external controller. The only requirement Megaphone places on
the controller is to adhere to the control command format as de-
scribed in Section 3.3. A controller could observe the performance
characteristics of a computation on a per-key level and correlate this
with the input workload. For example, the recent DS2 [20] system
automatically measures and re-scales streaming systems to meet
throughput targets. Megaphone can also be driven by general re-
conﬁguration controllers and is not restricted to elasticity policies.
For instance, the conﬁguration stream could also be provided by
Dhalion [16] or Chi [21].
Independently, we have observed and implemented several details
for effective migration. Speciﬁcally, we can use bipartite matching
to group migrations that do not interfere with each other, reducing
the number of migration steps without much increasing the maxi-
mum latency. We can also insert a gap between migrations to allow
the system to immediately drain enqueued records, rather than dur-
ing the next migration, which reduces the maximum latency from
two migration durations to just one.
5
Evaluation
Our evaluation of Megaphone is in three parts. We are interested
in particular in the latency of streaming queries, and how they are
affected by Megaphone both in a steady state (where no migration
is occuring) and during a migration operation.
First, in Section 5.1 we use the NEXMark benchmarking suite [23,
27] to compare Megaphone with prior techniques under a realistic
workload. NEXMark consists of queries covering a variety of op-
erators and windowing behaviors. Next, in Section 5.2 we look at
the overhead of Megaphone when no migration occurs: this is the
cost of providing migration functionality in stateful dataﬂow oper-
ators, versus using optimized operators which cannot migrate state.
Finally, in Section 5.3 we use a microbenchmark to investigate how
parameters like the number of bins and size of the state affect mi-
gration performance.
We run all experiments on a cluster of four machines, each with
four Intel Xeon E5-4650 v2 @2.40 GHz CPUs (each 10 cores with
hyperthreading) and 512 GiB of RAM, running Ubuntu 18.04. For
each experiment, we pin a timely process with four workers to a
single CPU socket. Our open-loop testing harness supplies the input
at a speciﬁed rate, even if the system itself becomes less responsive
7


## Page 8


Table 1: NEXMark query implementations lines of code.
Q1
Q2
Q3
Q4
Q5
Q6
Q7
Q8
Native
12
14
58
128
73
130
55
58
Megaphone
16
18
41
74
46
74
54
29
(e.g., during a migration). We record the observed latency every
250 ms, in units of nanoseconds, which are recorded in a histogram
of logarithmically-sized bins.
Unless otherwise speciﬁed, we migrate the state of the main op-
erator of each dataﬂow. We initially migrate half of the keys on half
of the workers to the other half of the workers (25% of the total
state), which results in an imbalanced assignment. We then perform
and report the details of a second migration back to the balanced
conﬁguration.
5.1
NEXMark Benchmark
The NEXMark suite models an auction site in which a high-volume
stream of users, auctions, and bids arrive, and eight standing queries
are maintained reﬂecting a variety of relational queries including
stateless streaming transformations (e.g., map and ﬁlter in Q1 and
Q2 respectively), a stateful record-at-a-time two-input operator (in-
cremental join in Q3), and various window operators (e.g., sliding
window in Q5, tumbling window join in Q8), and complex multi-
operator dataﬂows with shared components (Q4 and Q6).
We have implemented all eight of the NEXMark queries in both
native timely dataﬂow and using Megaphone. Table 1 lists the lines
of code for queries 1–8. Native is a hand-tuned implementation,
Megaphone is implemented using the stateful operator interface.
Note that the implementation complexity for the native implemen-
tation is higher in most cases as we include optimizations from
Section 4 which are not offered by the system but need to be imple-
mented for each operator by hand.
To test our hypothesis that Megaphone supports efﬁcient migra-
tion on realistic workloads, we run each NEXMark query under
high load and migrate the state of each query without interrupting
the query processing itself. Our test harness uses a reference in-
put data generator and increases its rate. The data generator can be
played at a higher rate but this does not change certain intrinsic prop-
erties. For example, the number of active auctions is static, and so
increasing the event rate decreases auction duration. For this reason,
we present time-dilated variants of queries Q5 and Q8 containing
large time-based windows (up to 12 hours). We run all queries with
4 × 106 updates per second. For stateful queries, we perform a ﬁrst
migration at 400 s and perform and report a second re-balancing
migration at 800 s. We compare all-at-once, which is essentially
equivalent to the partial pause-and-restart strategy adopted by exist-
ing systems, and batched, Megaphone’s optimized migration strat-
egy which strikes a balance between migration latency and duration
(cf. Section 3.3). We use 212 bins for Megaphone’s migration; in
Section 5.2 we study Megaphone’s sensitivity to the bin count.
Figures 7 through 12 show timelines for the second migration
of stateful queries Q3 through Q8. Generally, the all-at-once mi-
grations experience maximum latencies proportional to the amount
of state maintained, whereas the latencies of Megaphone’s batched
migration are substantially lower when the amount of state is large.
Query 1 and Query 2 maintain no state. Q1 transforms the
stream of bids to use a different currency, while Q2 ﬁlters bids
by their auction identiﬁers. Despite the fact that both queries do
not accumulate state to migrate, we demonstrate their behavior to
establish a baseline for Megaphone and our test harness. Figures 5
and 6 show query latency during two migrations where no state is
thus transferred; any impact is dominated by system noise.
100
101
102
103
104
 0
 10
 20
Latency [ms]
Time [s]
max
p: 0.99
p: 0.5
p: 0.25
Figure 5: NEXMark query latency for Q1, 4 × 106 requests per
second, reconﬁguration at 10 s and 20 s. No latency spike occurs
during migration as the query does not accumulate state.
100
101
102
103
104
 0
 10
 20
Latency [ms]
Time [s]
max
p: 0.99
p: 0.5
p: 0.25
Figure 6: NEXMark query latency for Q2, 4 × 106 requests per
second, reconﬁguration at 10 s and 20 s. No latency spike occurs
during migration as the query does not accumulate state.
100
101
102
103
104
 780
 800
 820
 840
Latency [ms]
Time [s]
all-at-once
max
p: 0.99
p: 0.5
p: 0.25
 780
 800
 820
 840
Time [s]
Megaphone (batched)
(a) Query 3 implemented with Megaphone.
100
101
102
103
104
 780
 800
 820
 840
Latency [ms]
Time [s]
p: 1
p: 0.99
p: 0.5
p: 0.25
(b) Query 3 native implementation.
Figure 7: NEXMark query latency for Q3. A small latency spike
can be observed at 800 s for both all-at-once and batched migration
strategies, reaching more than 100 ms for all-at-once and 10 ms for
batched migration. Although the state for query 3 grows without
bounds, this did not bear signiﬁcance after 800 s.
8


## Page 9


Query 3 joins auctions and people to recommend local auctions
to individuals. The join operator maintains the auctions and people
relations, using the seller and person as the keys, respectively. This
state grows without bound as the computation runs. Figure 7 shows
the query latency for both Megaphone, and the native timely imple-
mentation. We note that while the native timely implementation has
some spikes, they are more pronounced in Megaphone, whose tail
latency we investigate further in Section 5.2.
Query 4 reports the average closing prices of auctions in a cat-
egory relying on a stream of closed auctions, derived from the
streams of bids and auctions, which we compute and maintain, and
contains one operator keyed by auction id which accumulates rele-
vant bids until the auction closes, at which point the auction is re-
ported and removed. The NEXMark generator is designed to have a
ﬁxed number of auctions at a time, and so the state remains bounded.
Figure 8 shows the latency timeline during the second migration.
The all-at-once migration strategy causes a latency spike of more
than two seconds whereas the batched migration strategy only shows
an increase in latency of up to 100 ms.
Query 5 reports, each minute, the auctions with the highest num-
ber of bids taken over the previous sixty minutes. It maintains up to
sixty counts for each auction, so that it can both report and retract
counts as time advances. To elicit more regular behavior, our imple-
mentation reports every second over the previous minute, effectively
dilating time by a factor of 60. Figure 9 shows the latency timeline
for the second migration; the all-at-once migration is an order of
magnitude larger than the per-second events, whereas Megaphone’s
batched migration is not distinguishable.
Query 6 reports the average closing price for the last ten auctions
of each seller. This operator is keyed by auction seller, and maintains
a list of up to ten prices. As the computation proceeds, the set of
sellers, and so the associated state, grows without bound. Figure 10
shows the timeline at the second migration. The result is similar
to query 4 because both have a large fraction of the query plan in
common.
Query 7 reports the highest bid each minute, and the results are
shown in Figure 11. This query has minimal state (one value) but
does require a data exchange to collect worker-local aggregations
to produce a computation-wide aggregate. Because the state is so
small, there is no distinction between all-at-once and Megaphone’s
batched migration.
Query 8 reports a twelve-hour windowed join between new peo-
ple and new auction sellers. This query has the potential to maintain
a massive amount of state, as twelve hours of auction and people
data is substantial. Once reached, the peak size of state is main-
tained. To show the effect of twelve-hour windows, we dilate the
internal time by a factor of 79. The reconﬁguration time of 800 s
corresponds to approximately 17.5 h of event time.
These results show that for NEXMark queries maintaining large
amounts of state, all-at-once migration can introduce signiﬁcant
disruption, which Megaphone’s batched migration can mitigate. In
principle, the latency could be reduced still further with the ﬂuid
migration strategy, which we evaluate in Section 5.3.
5.2
Overhead of the interface
We now use a counting microbenchmark to measure the overhead
of Megaphone, from which one can determine an appropriate trade-
off between migration granularity and this overhead. We compare
Megaphone to native timely dataﬂow implementations, as we vary
the number of bins that Megaphone uses for state. We anticipate that
this overhead will increase with the number of bins, as Megaphone
must consult a larger routing table.
100
101
102
103
104
 780
 800
 820
 840
Latency [ms]
Time [s]
all-at-once
max
p: 0.99
p: 0.5
p: 0.25
 780
 800
 820
 840
Time [s]
Megaphone (batched)
Figure 8: NEXMark query latency for Q4, 4 × 106 requests per
second, reconﬁguration at 800 s.
100
101
102
103
104
 780
 800
 820
 840
Latency [ms]
Time [s]
all-at-once
max
p: 0.99
p: 0.5
p: 0.25
 780
 800
 820
 840
Time [s]
Megaphone (batched)
Figure 9: NEXMark query latency for Q5, 4 × 106 requests per
second, reconﬁguration at 800 s with time dilation.
100
101
102
103
104
 780
 800
 820
 840
Latency [ms]
Time [s]
all-at-once
max
p: 0.99
p: 0.5
p: 0.25
 780
 800
 820
 840
Time [s]
Megaphone (batched)
Figure 10: NEXMark query latency for Q6, 4 × 106 requests per
second, reconﬁguration at 800 s.
100
101
102
103
104
 780
 800
 820
 840
Latency [ms]
Time [s]
all-at-once
max
p: 0.99
p: 0.5
p: 0.25
 780
 800
 820
 840
Time [s]
Megaphone (batched)
Figure 11: NEXMark query latency for Q7, 4 × 106 requests per
second, reconﬁguration at 800 s.
9


## Page 10


100
101
102
103
104
 780
 800
 820
 840
Latency [ms]
Time [s]
all-at-once
max
p: 0.99
p: 0.5
p: 0.25
 780
 800
 820
 840
Time [s]
Megaphone (batched)
Figure 12: NEXMark query latency for Q8, 4 × 106 requests per
second, reconﬁguration at 800 s with time dilation.
10-5
10-4
10-3
10-2
10-1
100
100
101
102
103
CCDF
Latency [ms]
4
6
8
10
12
14
16
18
20
Native
(a) CCDF of per-record latencies
Experiment
90%
99%
99.99%
max
4
4.46
7.60
18.87
25.17
6
4.46
6.55
13.11
26.21
8
4.46
6.03
9.96
16.78
10
4.19
6.82
16.25
23.07
12
4.98
7.08
19.92
24.12
14
8.13
11.53
23.07
30.41
16
20.97
27.26
60.82
83.89
18
159.38
192.94
209.72
226.49
20
1140.85
1409.29
1476.40
1543.50
Native
1.64
2.88
12.06
19.92
(b) Selected percentiles and their latency in ms
Figure 13: Hash-count overhead experiment with 256 × 106 unique
keys and an update rate of 4 × 106 per second. Experiment numbers
in (a) and (b) indicate log bin count.
The workload uses a stream of randomly selected 64-bit integer
identiﬁers, drawn uniformly from a domain deﬁned per experiment.
The query reports the cumulative counts of the number of times
each identiﬁer has occurred. In these workloads, the state is the per-
identiﬁer count, intentionally small and simple so that we can see the
effect of migration rather than associated computation. We consider
two variants, an implementation that uses hashmaps for bins (“hash
count”), and an optimized implementation that uses dense arrays to
remove hashmap computation (“key count”).
Each experiment is parameterized by a domain size (the number
of distinct keys) and an input rate (in records per second), for which
we then vary the number of bins used by Megaphone. Each experi-
ment pre-loads one instance of each key to avoid measuring latency
due to state re-allocation at runtime.
Figure 13 shows the complementary cumulative distribution func-
tion (CCDF) of per-record latency for the hash-count experiment
with 256 × 106 distinct keys and a rate of 4 × 106 updates per
second. Figure 14 shows the CCDF of per-record latency for the
key-count experiment with 256 × 106 distinct keys and a rate of
4 × 106 updates per second. Figure 15 shows the CCDF of per-
10-5
10-4
10-3
10-2
10-1
100
100
101
102
103
CCDF
Latency [ms]
4
6
8
10
12
14
16
18
20
Native
(a) CCDF of per-record latencies
Experiment
90%
99%
99.99%
max
4
1.64
3.67
12.58
19.92
6
1.64
2.75
11.01
20.97
8
1.70
2.49
9.44
19.92
10
1.70
2.36
7.08
15.20
12
1.77
2.88
9.96
20.97
14
2.49
4.46
7.86
19.92
16
22.02
26.21
32.51
46.14
18
234.88
268.44
301.99
335.54
20
838.86
1610.61
1879.05
1946.16
Native
1.51
1.70
4.46
14.16
(b) Selected percentiles and their latency in ms
Figure 14: Key-count overhead experiment with 256 × 106 unique
keys and an update rate of 4 × 106 per second. Experiment numbers
in (a) and (b) indicate log bin count.
record latency for the key-count experiment with 8192 × 106 dis-
tinct keys and a rate of 4 × 106 updates per second. Each ﬁgure
reports measurements for a native timely dataﬂow implementation,
and for Megaphone with geometrically increasing numbers of bins.
For small bin counts, the latencies remain a small constant factor
larger than the native implementation, but this increases noticeably
once we reach 216 bins. We conclude that while a performance
penalty exists, it can be an acceptable trade-off for ﬂexible state-
ful dataﬂow reconﬁguration. A bin-count parameter of up to 212
leads to largely indistinguishable results, and we will use this num-
ber when we need to hold the bin count constant in the rest of the
evaluation.
5.3
Migration micro-benchmarks
We now use the counting benchmark from the previous section to
analyse how various parameters inﬂuence the maximum latency and
duration of Megaphone during a migration. Speciﬁcally,
1. In Section 5.3.1 we evaluate the maximum latency and dura-
tion of migration strategies as the number of bins increases.
We expect Megaphone’s maximum latencies to decrease with
more bins, without affecting duration.
2. In Section 5.3.2 we evaluate the maximum latency and dura-
tion of migration strategies as the number of distinct keys
increases. We expect all maximum latencies and durations to
increase linearly with the amount of maintained state.
3. In Section 5.3.3 we evaluate the maximum latency and dura-
tion of migration strategies as the number of distinct keys
and bins increase proportionally. We expect that with a
constant per-bin state size Megaphone will maintain a ﬁxed
maximum latency while the duration increases.
4. In Section 5.3.4 we evaluate the latency under load during
migration and steady-state. We expect a smaller maximum
latency for Megaphone migrations.
5. In Section 5.3.5 we evaluate the memory consumption dur-
ing migration. We expect a smaller memory footprint for
10


## Page 11


10-5
10-4
10-3
10-2
10-1
100
100
101
102
103
CCDF
Latency [ms]
4
6
8
10
12
14
16
18
20
Native
(a) CCDF of per-record latencies
Experiment
90%
99%
99.99%
max
4
1.90
3.28
4.72
7.34
6
1.84
3.28
6.03
18.87
8
1.84
3.54
5.24
12.58
10
1.84
3.28
5.77
13.11
12
1.90
3.67
5.24
9.44
14
7.34
16.78
75.50
100.66
16
30.41
35.65
41.94
50.33
18
268.44
318.77
335.54
385.88
20
1006.63
1610.61
1811.94
1879.05
Native
1.57
2.36
4.98
14.68
(b) Selected percentiles and their latency in ms
Figure 15: Key-count overhead experiment with 8192 × 106 unique
keys and an update rate of 4 × 106 per second. Experiment numbers
in (a) and (b) indicate log bin count.
Megaphone migrations.
Each of our migration experiments largely resembles the shapes
seen in Figure 1, where each migration strategy has a well deﬁned
duration and maximum latency. For example, the all-at-once mi-
gration strategy has a relatively short duration with a large maxi-
mum latency, whereas the bin-at-a-time (ﬂuid) migration strategy
has a longer duration and lower maximum latency, and the batched
migration strategy lies between the two. In these experiments we
summarize each migration by the duration of the migration, and the
maximum latency observed during the migration.
5.3.1 Number of bins vary. We now evaluate the behavior of dif-
ferent migration strategies for varying numbers of bins. As we in-
crease the number of bins we expect to see ﬂuid and batched mi-
gration achieve lower maximum latencies, though ideally with rel-
atively unchanged durations. We do not expect to see all-at-once
migration behave differently as a function of the number of bins, as
it conducts all of its migrations simultaneously.
Holding the rates and bin counts ﬁxed, we will vary the number
of bins from 24 up to 214 by factors of four. For each conﬁguration,
we run for one minute to establish a steady state, and then initiate a
migration and continue for one another minute. During this whole
time the rate of input records continues uninterrupted.
Figure 16 reports the latency-vs-duration trade-off of the three
migration strategies as we vary the number of bins. The connected
lines each describe one strategy, and the common shapes describe
a common number of bins. We see that all all-at-once migration ex-
periments are in a low duration high latency cluster. Both ﬂuid and
batched migration achieve lower maximum latency as we increase
the number of bins, without negatively impacting the duration.
5.3.2 Number of keys vary. We now evaluate the behavior of dif-
ferent migration strategies for varying domain sizes. Holding the
rates and bin counts ﬁxed, we will vary the number of keys from
256 × 106 up to 8192 × 106 by factors of two. For each conﬁgu-
ration, we run for one minute to establish a steady state, and then
 0.01
 0.1
 1
 10
 100
 0.1
 1
 10
 100
 1000
Max latency [s]
Duration [s]
bins
16
64
256
1024
4096
16384
 0.01
 0.1
 1
 10
 100
 0.1
 1
 10
 100
 1000
 
 
migration
batched
fluid
all-at-once
Figure 16: Key-count migration latency vs. duration, varying bin
count for a ﬁxed domain of 4096 × 106 keys. The vertical lines in-
dicate that increasing the granularity of migration can reduce maxi-
mum latency for ﬂuid and batched migrations without increasing the
duration. The all-at-once migration datapoints remain in a cluster
independent of the migration granularity.
 0.01
 0.1
 1
 10
 100
 0.1
 1
 10
 100
 1000
Max latency [s]
Duration [s]
domain
256M
512M
1024M
2048M
4096M
8192M
16384M
32768M
 0.01
 0.1
 1
 10
 100
 0.1
 1
 10
 100
 1000
 
 
migration
batched
fluid
all-at-once
Figure 17: Key-count migration latency vs. duration, varying do-
main for a ﬁxed rate of 4 × 106. As the domain size increases the
migration granularity increases, and the duration and maximum la-
tencies increase proportionally.
initiate a migration and continue for one another minute. During
this whole time the rate of input records continues uninterrupted.
Figure 17 reports the latency-vs-duration trade-off of the three
migration strategies as we vary the number of distinct keys. The
connected lines each describe one strategy, and the common shapes
describe a common number of distinct keys. We see that for any
experiment, all-at-once migration has the highest latency and lowest
duration, ﬂuid migration has a lower latency and higher duration,
and batched migration often has the best qualities of both.
5.3.3 Number of keys and bins vary proportionally. In the pre-
vious experiments, we either ﬁxed the number of bins or the number
of keys while varying the other parameter. In this experiment, we
vary both bins and keys together such that the total amount of data
per bin stays constant. This maintains a ﬁxed migration granularity,
which should have a ﬁxed maximum latency even as the number of
keys (and total state) increases. We run the key count experiment
and ﬁx the number of keys per bin to 4 × 106. We then increase the
domain in steps of powers of two starting at 256 × 106 and increase
the number of bins such that the keys per bin stays constant. The
maximum domain is 32 × 109 keys.
Figure 18 reports the latency-versus-duration trade-off for the
three migration strategies as we increase domain and number of
bins while keeping the state per bin constant. The lines describe one
11


## Page 12


0.01
 0.1
 1
 10
 100
 0.1
 1
 10
 100
 1000
Max latency [s]
Duration [s]
bins
64
128
256
512
1024
2048
4096
8192
 0.01
 0.1
 1
 10
 100
 0.1
 1
 10
 100
 1000
 
 
migration
batched
fluid
all-at-once
Figure 18: Latency and duration of key-count migrations for ﬁxed
state per bin. By holding the granularity of migration ﬁxed, the
maximum latencies of ﬂuid and batched migration remain ﬁxed
even as the durations of all strategies increase.
 0.01
 0.1
 1
 10
 100
 1000
 0.25
 0.5
 1
 2
 4
 8
 16
 32
Max latency [s]
Throughput [million records/s]
batched
fluid
all-at-once
non-migrating
Figure 19: Offered load versus max latency for different migration
strategies for key-count. The migration is invariant of the rate up to
16 million records per second.
migration strategy and the points describe a different conﬁguration.
We can observe that for ﬂuid and batched migration the latency stays
constant while only the duration increases as we increase the do-
main. For all-at-once migration, both latency and duration increase.
We conclude that ﬂuid and batched migration offer a way to
bound the latency impact on a computation during a migration while
increasing the migration duration, whereas all-at-once migration
does not.
5.3.4 Throughput versus processing latency. In this experiment,
we evaluate what throughput Megaphone can sustain for speciﬁc la-
tency targets. As we increase the offered load, we expect the steady-
state and migration latency to increase. For a spciﬁc throughput
target, we expect the all-at-once migration strategy to show a higher
latency than batched, which itself is expected to be higher than ﬂuid.
To analyze the latency, we keep the number of keys and bins
constant, at 16 384 × 106 and 4096, and vary the offered load from
250 × 103 to 32 × 106 in powers of two. We measure the maximum
latency observed during both steady-state and migration for each of
the three migration strategies described earlier.
Figure 19 shows maximum latency observed when the system
is sustaining a certain throughput. All three migration strategies
and non-migrating show a similar pattern: Up to 16 × 106 records
per second they do not show a signiﬁcant increase in latency. At
32 × 106, the latency increases signiﬁcantly, indicating that the sys-
tem is now overloaded.
We conclude that the system’s latency is mostly throughput-in-
variant until the system saturates and eventually fails to keep up with
its input. Both ﬂuid and batched migration sustain a throughput of
0.0 B
10.0GB
20.0GB
30.0GB
40.0GB
50.0GB
60.0GB
70.0GB
80.0GB
90.0GB
 0
 200
 400
 600
 800
 1000
 1200
RSS
Time [s]
batched
fluid
all-at-once
Figure 20: Memory consumption of key-count per process over time
for different migration strategies. The ﬂuid and batched strategies
require less additional memory in each migration step than the all-
at-once migration, which migrates all state at once.
up to 4 × 106 per second for a latency target of 1 s: Megaphone’s
migration strategies can satisfy latency targets 10-100x lower than
all-at-once migration with similar throughput.
5.3.5 Memory consumption during migration. In Section 5.3.3
we analyzed the behavior of different migration strategies when
increasing the total amount of state in the system while leaving
the state per bin constant. Our expectation was that the all-at-once
migration strategy would always offer the lowest duration when
compared to batched and ﬂuid migrations. Nevertheless, we observe
for large amounts of data being migrated the duration for a all-at-
once migration is longer than for batched migration.
To analyze the cause for this behavior we compared the memory
consumption for the three migration strategies over time. We run the
key count dataﬂow with 16 × 109 keys and 4096 bins. We record the
resident set size (RSS) as reported by Linux over time per process.
Figure 20 shows the RSS reported by the ﬁrst timely process
for each migration strategy. Batched and ﬂuid migration show a
similar memory consumption of 35 GiB in steady state and do not
expose a large variance during migration at times 400 s and 800 s. In
contrast to that, all-at-once migration shows signiﬁcant allocations
of approximately additional 30 GiB during the migrations.
The experiment gives us evidence that a all-at-once migration
causes signiﬁcant memory spikes in addition to latency spikes. The
reason for this is that during a all-at-once migration, each worker
extracts and serializes the data to be migrated and enqueues it for
the network threads to send. The network thread’s send capacity is
limited by the network throughput, limiting the throughput at which
data can be transferred to the remote host. Batched and ﬂuid migra-
tion patterns only perform another migration once the previous is
complete and thus provide a simple form of ﬂow-control effectively
limiting the amount of temporary state.
6
Conclusion
We presented the design and implementation of Megaphone, which
provides efﬁcient, minimally disruptive migration for stream pro-
cessing systems. Megaphone plans ﬁne-grained migrations using
the logical timestamps of the stream processor, and interleaves the
migrations with regular streaming dataﬂow processing. Our evalu-
ation on realistic workloads shows that migration disruption was
signiﬁcantly lower than with prior all-at-once migration strategies.
We implemented Megaphone in timely dataﬂow, without any
changes to the host dataﬂow system. Megaphone demonstrates that
dataﬂow coordination mechanisms (timestamp frontiers) and data-
ﬂow channels themselves are sufﬁcient to implement minimally dis-
ruptive migration. Megaphone’s source code is available on https:
//github.com/strymon-system/megaphone.
12


## Page 13


7
References
[1] Bringing Pokemon GO to life on Google Cloud. https:
//cloudplatform.googleblog.com/2016/09/bringing-
Pokemon-GO-to-life-on-Google-Cloud.html.
[2] IBM Streams (accessed: November 2017). https://
www.ibm.com/ch-en/marketplace/stream-computing.
[3] New Tweets per second record, and how!
https://blog.twitter.com/engineering/en us/a/
2013/new-tweets-per-second-record-and-how.html.
[4] M. Abadi, F. McSherry, D. G. Murray, and T. L. Rodeheffer.
Formal analysis of a distributed algorithm for tracking
progress. In D. Beyer and M. Boreale, editors, Formal
Techniques for Distributed Systems, pages 5–19, Berlin,
Heidelberg, 2013. Springer Berlin Heidelberg.
[5] T. Akidau, A. Balikov, K. Bekiro˘glu, S. Chernyak,
J. Haberman, R. Lax, S. Mcveety, D. Mills, P. Nordstrom, and
S. Whittle. MillWheel: Fault-Tolerant Stream Processing at
Internet Scale. Proceedings of the VLDB Endowment,
6(11):1033–1044, 2013.
[6] T. Akidau, R. Bradshaw, C. Chambers, S. Chernyak, R. J.
Fern´andez-Moctezuma, R. Lax, S. McVeety, D. Mills,
F. Perry, E. Schmidt, and S. Whittle. The dataﬂow model: A
practical approach to balancing correctness, latency, and cost
in massive-scale, unbounded, out-of-order data processing.
Proc. VLDB Endow., 8(12):1792–1803, Aug. 2015.
[7] M. Armbrust, T. Das, J. Torres, B. Yavuz, S. Zhu, R. Xin,
A. Ghodsi, I. Stoica, and M. Zaharia. Structured streaming: A
declarative api for real-time applications in apache spark. In
Proceedings of the 2018 International Conference on
Management of Data, SIGMOD ’18, pages 601–613, 2018.
[8] S. Barker, Y. Chi, H. J. Moon, H. Hacig¨um¨us¸, and P. Shenoy.
”cut me some slack”: Latency-aware live migration for
databases. In Proceedings of the 15th International
Conference on Extending Database Technology, EDBT ’12,
pages 432–443. ACM, 2012.
[9] P. Carbone, S. Ewen, G. F´ora, S. Haridi, S. Richter, and
K. Tzoumas. State Management in Apache Flink: Consistent
Stateful Distributed Stream Processing. Proc. VLDB Endow.,
10(12):1718–1729, Aug. 2017.
[10] P. Carbone, A. Katsifodimos, S. Ewen, V. Markl, S. Haridi,
and K. Tzoumas. Apache Flink: Stream and batch processing
in a single engine. Data Engineering, 38(4), 2015.
[11] S. Das, S. Nishimura, D. Agrawal, and A. El Abbadi.
Albatross: Lightweight elasticity in shared storage databases
for the cloud using live data migration. Proc. VLDB Endow.,
4(8):494–505, May 2011.
[12] A. J. Elmore, V. Arora, R. Taft, A. Pavlo, D. Agrawal, and
A. El Abbadi. Squall: Fine-grained live reconﬁguration for
partitioned main memory databases. In Proceedings of the
2015 ACM SIGMOD International Conference on
Management of Data, SIGMOD ’15, pages 299–313, New
York, NY, USA, 2015. ACM.
[13] A. J. Elmore, S. Das, D. Agrawal, and A. El Abbadi. Zephyr:
Live migration in shared nothing databases for elastic cloud
platforms. In Proceedings of the 2011 ACM SIGMOD
International Conference on Management of Data, SIGMOD
’11, pages 301–312, New York, NY, USA, 2011. ACM.
[14] J. Fang, R. Zhang, T. Z. Fu, Z. Zhang, A. Zhou, and J. Zhu.
Parallel stream processing against workload skewness and
variance. In Proceedings of the 26th International Symposium
on High-Performance Parallel and Distributed Computing,
HPDC ’17, pages 15–26, 2017.
[15] R. C. Fernandez, M. Migliavacca, E. Kalyvianaki, and
P. Pietzuch. Integrating scale out and fault tolerance in stream
processing using operator state management. In Proceedings
of the 2013 ACM SIGMOD international conference on
Management of data, pages 725–736, 2013.
[16] A. Floratou, A. Agrawal, B. Graham, S. Rao, and
K. Ramasamy. Dhalion: Self-regulating stream processing in
heron. PVLDB, 2017.
[17] V. Gulisano, R. Jim´enez-Peris, M. Pati˜no-Mart´ınez,
C. Soriente, and P. Valduriez. StreamCloud: An elastic and
scalable data streaming system. IEEE Transactions on
Parallel and Distributed Systems, 2012.
[18] T. Heinze, Z. Jerzak, G. Hackenbroich, and C. Fetzer.
Latency-aware elastic scaling for distributed data stream
processing systems. In Proceedings of the 8th ACM
International Conference on Distributed Event-Based
Systems, DEBS ’14, pages 13–22, New York, NY, USA, 2014.
ACM.
[19] M. Hoffmann, F. McSherry, and A. Lattuada.
Latency-conscious dataﬂow reconﬁguration. In Proceedings
of the 5th ACM SIGMOD Workshop on Algorithms and
Systems for MapReduce and Beyond, page 1. ACM, 2018.
[20] V. Kalavri, J. Liagouris, M. Hoffmann, D. Dimitrova,
M. Forshaw, and T. Roscoe. Three steps is all you need: fast,
accurate, automatic scaling decisions for distributed
streaming dataﬂows. In 13th {USENIX} Symposium on
Operating Systems Design and Implementation ({OSDI} 18),
pages 783–798, 2018.
[21] L. Mai, K. Zeng, R. Potharaju, L. Xu, S. Suh,
S. Venkataraman, P. Costa, T. Kim, S. Muthukrishnan,
V. Kuppa, et al. Chi: a scalable and programmable control
plane for distributed stream processing systems. Proceedings
of the VLDB Endowment, 11(10):1303–1316, 2018.
[22] D. G. Murray, F. McSherry, R. Isaacs, M. Isard, P. Barham,
and M. Abadi. Naiad: A Timely Dataﬂow System. In
Proceedings of the 24th ACM Symposium on Operating
Systems Principles (SOSP). ACM, Nov 2013.
[23] NEXMark benchmark.
http://datalab.cs.pdx.edu/niagaraST/NEXMark.
[24] S. Rajadurai, J. Bosboom, W.-F. Wong, and S. Amarasinghe.
Gloss: Seamless live reconﬁguration and reoptimization of
stream programs. In ASPLOS, pages 98–112, 2018.
[25] O. Schiller, N. Cipriani, and B. Mitschang. Prorea: Live
database migration for multi-tenant rdbms with snapshot
isolation. In Proceedings of the 16th International
Conference on Extending Database Technology, EDBT ’13,
pages 53–64, New York, NY, USA, 2013. ACM.
[26] M. A. Shah, M. A. Shah, S. Chandrasekaran, J. M.
Hellerstein, J. M. Hellerstein, S. Ch, S. Ch, M. J. Franklin,
and M. J. Franklin. Flux: An adaptive partitioning operator
for continuous query systems. In ICDE, pages 25–36, 2002.
[27] P. Tucker, K. Tufte, V. Papadimos, and D. Maier.
NEXMark—A Benchmark for Queries over Data Streams
DRAFT. Technical report, OGI School of Science &
Engineering at OHSU, 2002.
[28] Y. Wu and K.-L. Tan. ChronoStream: Elastic stateful stream
computation in the cloud. In 2015 IEEE 31st International
Conference on Data Engineering, pages 723–734. IEEE, apr
2015.
[29] M. Zaharia, T. Das, H. Li, T. Hunter, S. Shenker, and I. Stoica.
Discretized streams: Fault-tolerant streaming computation at
13


## Page 14


scale. In Proceedings of the Twenty-Fourth ACM Symposium
on Operating Systems Principles, pages 423–438. ACM,
2013.
[30] Y. Zhu, E. A. Rundensteiner, and G. T. Heineman. Dynamic
plan migration for continuous queries over data streams. In
Proceedings of the 2004 ACM SIGMOD International
Conference on Management of Data, SIGMOD ’04, pages
431–442, 2004.
14

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]