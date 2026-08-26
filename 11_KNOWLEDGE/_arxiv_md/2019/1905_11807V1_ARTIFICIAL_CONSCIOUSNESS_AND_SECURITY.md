---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.11807v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1905.11807v1_Artificial_Consciousness_and_Security

> Source: 1905.11807v1_Artificial_Consciousness_and_Security.pdf

> Pages: 7

---


## Page 1


arXiv:1905.11807v1  [cs.AI]  11 May 2019
ARTIFICIAL CONSCIOUSNESS AND SECURITY
ANDREW POWELL
Abstract. This paper describes a possible way to improve computer security
by implementing a program which implements the following three features
related to a weak notion of artiﬁcial consciousness: (partial) self-monitoring,
ability to compute the truth of quantiﬁer-free propositions and the ability to
communicate with the user. The integrity of the program could be enhanced
by using a trusted computing approach, that is to say a hardware module that
is at the root of a chain of trust. This paper outlines a possible approach but
does not refer to an implementation (which would need further work), but the
author believes that an implementation using current processors, a debugger,
a monitoring program and a trusted processing module is currently possible.
1. Introduction
It is plausible to believe that the minimum condition that distinguishes an artiﬁ-
cially conscious computer from one that is not conscious is the ability to self-monitor
(an idea that is evident in the postscript to [Dennett84], and is explored in, for ex-
ample, [Sloman07]). There are many other approaches to artiﬁcial consciousness,
from ﬂat out denial of its possibility (usually based on a belief in a fundamen-
tally qualitative type of existence, qualia, which inanimate things do not possess),
through the views that consciousness is only to be associated with biological sys-
tems, that consciousness must be associated with language, that a conscious being
must have an internal representation of itself, that consciousness is an emergent
property of suﬃciently complex systems, to the view above that consciousness is a
function of the ability to self-refer or self-monitor and the even stronger view that
consciousness is a property of computations. [Chella07] contains a range of rea-
sonably current views on artiﬁcial consciousness and [Reggia13] and [Gamez08] are
recent surveys. This paper does not provide a critique of various views of artiﬁcial
consciousness, but instead advocates that three criteria should be tested empiri-
cally to investigate their adequacy for artiﬁcial consciousness in order to establish
a possibly weak notion of artiﬁcial consciousness which can be used to improve the
security of computer systems.
The three criteria are:
• Self-monitoring
• Ability to make judgements
• Ability to communicate, i.e.
at minimum respond with “yes” and “no”
answers to external questions
To be clear, these criteria are not seen as an anything more than framing an hy-
pothesis, which will need help from techniques in machine learning, expert systems
and machine visual representation in order to be tested. It may be that an au-
tonomous agent approach with consciousness as the broker between the activities
1


## Page 2


ARTIFICIAL CONSCIOUSNESS AND SECURITY
2
of the agents (see for example the LIDA parallel processing model of S. Franklin,
for example [Franklin, BaarsFranklin09, FranklinGraessner99], or the neural net-
work agents model of M. Shanahan, see [Shanahan06, ConnorShanahan10], or the
neural network state machine approach of I. Aleksander (see [Aleksander97]) may
produce machines which pass the test of consciousness as expressed by the three
criteria above. There is merit in the view that an artiﬁcially conscious entity does
need representations of objects in the world around us to make judgments that are
decidable by others (see Section 4), but in this paper it is argued that judgements
about the state1 of an entity’s own registers and memory has value for the purpose
of maintaining security.
In this paper the focus will be on a computer as the artiﬁcially conscious entity
and on the security implications of artiﬁcial consciousness, which exist even for a
weak notion of self-monitoring. Section 2 discusses how far self-monitoring can be
achieved. Section 4 explains why the ability to make judgements and the ability
to communicate are reasonable criteria for artiﬁcial consciousness and how judge-
ments and communications should be characterized. Sections 3 and 5 discuss the
implications for security of self-monitoring, judgment and communications of an
artiﬁcially conscious program and connections to the trusted computed initiative
implemented in recent computing platforms. In summary then, the notions of com-
munications, self-monitoring and judgement for a computer are explored and their
implications for improved security of computer systems are considered.
2. Self-monitoring
Self-monitoring is not the same as self-representation but does imply some kind
of self-awareness. Self-representation as a notion implies that a computer program
has a model of the self which it uses to validate references in judgements about
actions made by the self, but self-monitoring on the other hand only requires that
the program can check (some of) its own activities. Although self-representation is
not explicitly pursued in this paper, it may have utility as an aspect of a conscious-
ness because it is reasonable to suppose that the self can also be represented to the
self. However, self-monitoring is taken to be the more fundamental notion, as there
are limits to how faithful a representation of self can be (see the comments below
about the limits of self-monitoring). To be more precise about self-monitoring, a
computer program self-monitors if it is capable of checking the values of all the
registers or variables that it uses and the instruction that the program is currently
executing and the history of the state of the program (that is, the register values
and instructions executed, indexed by time). A computer process self-monitors if
it self-monitors as a computer program and it is able to monitor the state of any
interrupt sent to it by another process.
It is possible for a program or a process to self-monitor (if it has not crashed)2
because the self-monitoring function is very similar to what a debugger or instru-
mentation program does.
Strictly, a debugger is a program which enables any
1In this paper, state will refer to the values of all registers and the current instruction executed
at a speciﬁc time.
2A process has crashed if the program has not terminated and its execution cycles through a
sequence of states.


## Page 3


ARTIFICIAL CONSCIOUSNESS AND SECURITY
3
other program to be monitored without changing its computation steps or the
values of its variables; and it is of course true there will be registers and values
whose current values cannot be read, i.e. those registers which are used to check
the values of registers of the instrumented program.
Recent approaches to in-
strumenting a program by dynamically patching its execution path are given at
[Feiner12, Bungale07, Chachmon16]. In the present context such a limitation is
acceptable for two reasons. Firstly, self-monitoring is useful insofar as it concerns
monitoring the status of processes spawned by a given process, for example, to
check if the processes have crashed or are stuck in an endless loop, rather than
trying to determine whether the process itself is stuck in an endless loop (which is
in general is unsolvable because it is equivalent to the halting problem3). Secondly,
it is possible to check the value of all registers and the currently executing instruc-
tion with a time delay, as previously executed instructions and register values can
be archived. It is also possible for the values of the internal state of a process
to be monitored by a separate process which can set a ﬂag in one registers used
by the ﬁrst process if the ﬁrst process is behaving abnormally, with the limitation
that the ﬁrst process cannot reciprocally monitor the monitoring processing (which
would be equivalent to self-monitoring). So, for practical purposes programs and
processes can self-monitor. More theoretically, it is unreasonable to expect a mon-
itoring interface to expose everything about the monitoring program. Humans rely
on indirect reports from sensors, whereas an artiﬁcially conscious computer could
expose far more of its hardware state as well as the states of its processes.
The implications of a self-monitoring program are that the operating system (which
is a management program after all) can monitor all the programs and processes that
the operating system manages and can intervene if they crash, do not respond to
interrupts, or just behave abnormally (take up a lot of memory or get stuck in a
loop with no change in the value of the variables in the loop condition).
3. Security implications of self-monitoring
If it is possible to tell whether a process is behaving abnormally, it is plausible
to believe that the operating system can check whether a process or program other
than itself is operating insecurely. Of course security is diﬃcult to deﬁne in general
because security is relative to a set of speciﬁc security policies4, but in terms of
vulnerabilities not envisaged by the programmer, security means that the variables
have the values expected and that no memory structures used in the management
of program execution are modiﬁed other than by the operating system. A value of
a variable may be said to be expected if the program assigns data types to variables
and the value is in the range associated with the data type. In the case where
3This well known result is due to A. Turing [Turing36], but a modern approach is to deﬁne
f(e) = 1 if (∃x ∈N)({e}(e) = x) and f(e) = 0 otherwise, i.e. if {e}(e) is not deﬁned, where e
is the natural number code of (the syntax of) a program and {e} : N →N is the function that
the program implements, assumed to be a natural number function. Then if f were computable,
then f = {h} for some numerical program code h, and it follows that {h}(h) = 0 if {h}(h) is not
deﬁned, contradiction.
4There is a view in [ClarksonSchneider10] that security properties of computer programs are
properties of sets of execution paths (or traces), constraining those sets of traces in some way and
specifying which systems (sets of traces) a security policy relates to. This is an elegant way of
formulating security properties and formalizing security policies.


## Page 4


ARTIFICIAL CONSCIOUSNESS AND SECURITY
4
the operating system instruments every program by assigning data types to all
variables, checks whether all values of the variables are expected, and manages all
access to memory structures, it can be seen that a self-monitoring operating system
could identify programs which are operating insecurely and could instrument them
in such a way that evidence could be provided to a system administrator so that
the insecure program could be closed down.
In fact, we can even be bolder in our claims about what a self-monitoring operat-
ing system could monitor. It could monitor attempts to modify operating system
functions and libraries but, in general, not attempted changes to instrumentation
of those functions. It would be only be possible to address the risk of unauthorized
modiﬁcation of the operating system if there was a hierarchy of trust. If the operat-
ing system is trustworthy then it could assign a trustworthiness rating to programs
based on the number of security reports raised. It would be particularly useful to
combine this approach with a trusted computing approach5 which uses hardware
separation (i.e. trusted processing modules) to verify the integrity of the operating
system, to provide a chain of trust of programs run on the system, and to man-
age (via a virtualization layer) the execution of any programs (whether standard
user programs or high privilege programs such as kernel loadable modules). The
trusted computing module would prevent programs from having an impact if they
execute insecure code and the security veriﬁcation will check the trustworthiness of
the program.
4. Judgement and communication as criteria of artificial
consciousness
An artiﬁcial consciousness that could make judgements for itself would reduce
the decision-making burden on the user. The practical reason for including judge-
ments in the criteria for consciousness is that it seems impossible to make decisions
about what you are monitoring without the ability to make judgements. Thanks
to a line of logicians from G. Frege (see [Frege1884])6 onwards, we understand what
it is to make a judgement about a set of concepts and objects. That is, we can
in principle decide (i.e. compute the truth or falsehood of) a statement that does
not contain unbounded logical quantiﬁers (such as “for all” or “there exists”)7 but
may contain logical operators such as ”and”, “or”, “not” and “implies”. A judgment is
then a computable function (that is, a computation) from properties (or predicates)
and objects into the set that contains “true” and “false”. To be clear, we can apply
a program to a (natural number) code of a property that could apply to a set of
(codes of) input objects, and compute whether the property applies to a given set
of objects or not. For example, if we wish to decide where natural number c satisﬁes
the natural number relation a ≤x ≤b we could code a ≤x ≤b as ⌈a ≤x ≤b⌉
using a computable coding ⌈⌉and then substitute c for x in ⌈a ≤x ≤b⌉and decide
the truth of ⌈a ≤c ≤b⌉by means of a computable function. Of course, the types
of judgement that a computer can make will concern objective states of aﬀairs that
5See for example [Pearson02]. Trusted computing has been implemented on the motherboards
of some business-focussed personal computers and mobile computing platforms.
6Arguably the line originates from I. Kant (see [Stuart02]) and includes E. Husserl.
7In general dedidable propositions with quantﬁcation over an euumerable set S are of the form
(∃y)P (y, x) if x ∈S and (∃y)Q(y, x) if x /∈S, but most such propositions will not be decidable
by a computer with ﬁxed ﬁnite resources.


## Page 5


ARTIFICIAL CONSCIOUSNESS AND SECURITY
5
it can represent, such as whether a process is or is not responding to interrupts (in
a certain timescale), but not be about wishes or intentions.
It is worth stressing that the operating systems should make judgements about
all programs that the operating system manages (at least in the form of recom-
mendations to an administrator) on a frequent basis in terms of program health
(where they are caught in an endless loop or require too much system resources to
run), program security (against security policies and needing to pass vulnerability
checks) and program safety (against safety policies and needing to pass vulnerabil-
ity checks). The idea is that the operating system would run through all the tasks
it needs to perforn and compute each as a judgment, recording the results of the
judgements in a log.
It is also worth noting that not all properties are computably decidable8 and some
are not practically computably decidable (because any computation has a long run-
time), but it is nevertheless possible to decide whether for example a set of bits (a
pixel) represents the colour blue, whether a certain shape could represent a cat, or
whether indeed a certain process has not responded to an interrupt.9 If we allow
deep learning neural networks10, it is possible to represent concepts of diﬀering lev-
els of abstraction and to classify objects under those concepts. In order to decide
properties and make judgements, the artiﬁcially conscious program will need to
write and run programs of its own, i.e. spawn processes. In order to make judge-
ments about propositions that are not decidable but which are theorems of axiom
systems, we might want to allow the artiﬁcial consciousness to deduce theorems
from (codes of) axioms using inference rules, understand the axioms by verifying
that the axioms have a model11, and even to be able to propose new axioms by
producing models which satisfy those axioms (perhaps by using neural networks to
classify propositions as “theorems” or not). However, even without making the arti-
ﬁcially conscious program into a logician or a data scientist, the value of being able
to make judgments is considerable in terms of the ability of the artiﬁcial conscious-
ness to enforce security and safety policies and to improve clarity and eﬃciency of
interacting with the operating system for the user.
The reason why a program that can make judgements results in greater clarity
for the user is that the computations of decidable propositions will form a justi-
ﬁcation of the decisions that the program recommends. This approach will also
increase eﬃciency for the user because the operating system can make recommen-
dations to the user or take actions in a way that does not cause the user to try to
8In general arithmetical predicates containing any unbounded natural number quantiﬁers are
not decidable by means of a computation unless they have the speciﬁc form noted in Footnote 7.
9These examples are deliberately taken mainly from machine learning of visual representations
because that area provides a rich source of decidable judgements. Speech analytics is another such
area, as is of course the content of the computer’s own registers.
10Layers in convolutional neural networks, where the convolution operation picks out features,
naturally form a hierarchy of increasing abstraction.
11Ideally we would want to show that the axioms are true in a particular model of the axioms,
because truth in some model shows the consistency of the axioms.
In order to build models
computable representations of arbitrary elements and deﬁned functions/predicates of the model
will be needed. [Hodges85] is a very readable account of model theory, using games with ﬁnite
rule sets to build models.


## Page 6


ARTIFICIAL CONSCIOUSNESS AND SECURITY
6
guess at the cause of messages from the operating system.
The ability to communicate is included as a criterion of artiﬁcial consciousness
as a minimum condition for testing artiﬁcial consciousness, otherwise an external
user will have to monitor its state directly. An artiﬁcially conscious program needs
to communicate with the programs that it monitors, and operating systems are
expected to report to users on the the status of programs that are running and
to implement the users’ commands. The ability to communicate interactively and
faithfully would be desirable. For these reasons, the ability to communicate to other
programs and to users is essential. At minimum that communication could be “yes”
or “no” (i.e. one bit of information), although in practice data and functions of all
types could be passed through the program’s interface, including validation of the
accuracy of the information communicated.
5. Security implications of judgement and communications
The ability to form judgements could be used to prevent a user making mis-
takes and in coming to evidence-based decisions. When combined with the trusted
computing techniques noted in connection with self-monitoring, the artiﬁcially con-
scious program would have some evidence for the integrity of its own functioning
and for the soundness of its own judgements. The ability to communicate on the
other hand could introduce vulnerabilities into the program if the types and validity
of the value of program inputs are not checked, and the integrity of the messages
communicated would need to be assured (by cryptographic means for example).
Communication is necessary for the worth of the artiﬁcially conscious program to
be realized in terms of helping a user make decisions and to report back information.
In any case vulnerabilities in programs through specially crafted inputs are not new
for any operating system, nor is the need for integrity checking of communications.
Trusted computing could also provide integrity checking of communications.
6. Conclusions
In this paper an approach to artiﬁcial consciousness is suggested which is suf-
ﬁcient for increasing the security of operating systems, namely communications,
judgments and self-monitoring. It is also suggested that self-monitoring brings sig-
niﬁcant security beneﬁts in supporting the termination of programs which do not
respond to interrupts or otherwise exhibit unusual behaviour, that communications
is necessary for testing the functioning of an artiﬁcially conscious program, and
that the ability to make judgements is useful for user decision-support.
References
[Dennett84]
D.C. Dennett “Can machines think?”
and postscripts in Brainchildren,
MIT Press, 1998, 3-30, reprinted from M. G. Shafto (ed.), How We Know.
Harper & Row, 1984.
[Sloman07]
A. Sloman “Why Some Machines may Need Qualia and How They Can
Have Them: Including a Demanding New Turing Test for Robot Philoso-
phers” in AI and Consciousness: Theoretical foundations and current ap-
proaches AAAI Fall Symposium, 2007.
[Stuart02]
S.A J. Stuart & C. Dobbyn “A Kantian Prescription for Artiﬁcial Conscious
Experience” Leonardo Volume 35, Number 4, August 2002 407-411.
[Chella07]
Eds. A. Chella & R. Manzotti Artiﬁcial Consciousness Imprint Academic:
Exeter, 2007.


## Page 7


ARTIFICIAL CONSCIOUSNESS AND SECURITY
7
[Reggia13]
J. Reggia ”The rise of machine consciousness: Studying consciousness with
computational models” Neural Networks 44 (2013) 112–131.
[Gamez08]
D. Gamez “Progress in machine consciousness” Conscious Cognition 17(3)
(2008) 887-910.
[Franklin]
S. Franklin et al., ”The Mind According to LIDA – A Brief account”, S.
Franklin and the Cognitive Computing Research Group of the University
of Memphis, at corg.cs.memphis.edu, undated.
[BaarsFranklin09]
B. Baars & S. Franklin ”Consciousness is Computational: The LIDA of
Global Workspace Theory”, International Journal of Machine Conscious-
ness 1.01, 2009, 23-32.
[FranklinGraessner99] S. Franklin & ”A Software Agent Model of Consciousness”, Consciousness
and Cognition 8 (1999) 285–301.
[Shanahan06]
M. Shanahan “A cognitive architecture that combines internal simulation
with a global workspace” Consciousness and Cognition 15 (2006) 433–449.
[ConnorShanahan10]
D. Connor & M. Shanahan “A computational model of a global neu-
ronal workspace with stochastic connections” Neural Networks 23 (2010)
1139–1154
[Aleksander97]
I. Aleksander Impossible Minds: My Neurons, My Consciousness, Imperial
College Press: London, 1997.
[Turing36]
A.M. Turing, “On Computable Numbers, with an Application to the
Entscheidungsproblem” Proceedings of the London Mathematical Society
1936-7 Series 2 42 230-265.
[Chachmon16]
N. Chachmon, D. Richins, R. Cohn et al. “Simulation and Analysis Engine
for Scale-Out Workloads” In ICS ’16 Proceedings of the 2016 International
Conference on Supercomputing, Article 22, 2016.
[Feiner12]
P. Feiner, A. Demke Brown & A. Goel ”Comprehensive Kernel Instrumen-
tation via Dynamic Binary Translation” In the Seventeenth International
Conference on Architectural Support for Programming Languages and Op-
erating Systems (ASPLOS ’12), March 2012.
[Bungale07]
P.P. Bungale & C.-K. Luk “PinOS: A Programmable Framework for Whole-
System Dynamic Instrumentation” In International Conference on Virtual
Execution Environments (VEE’07), 2007.
[ClarksonSchneider10] M.R. Clarkson & F.B. Schneider “Hyperproperties” Journal of Computer
Security 18(2010) 1157-1210.
[Pearson02]
S. Pearson, “Trusted Computing Platforms, the Next Security Solution”
HP Laboratories Bristol HPL - 2002 - 221, 2002.
[Frege1884]
G. Frege The Foundations of Arithmetic Translated by J.L. Austin, Ox-
ford: Blackwell, 1950.
[Hodges85]
W. Hodges Building Models by Games Cambridge: Cambridge University
Press, 1985.
Dr. Andrew Powell, Honorary Senior Research Fellow, Institute for Security
Science and Technology, Level 2 Admin Office Central Library, Imperial College
London, South Kensington Campus, London SW7 2AZ, United Kingdom.
E-mail address: andrew.powell@imperial.ac.uk

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]