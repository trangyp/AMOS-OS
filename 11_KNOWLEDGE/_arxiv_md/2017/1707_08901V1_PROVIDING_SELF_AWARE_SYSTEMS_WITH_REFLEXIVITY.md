---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.08901v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1707.08901v1_Providing_Self-Aware_Systems_with_Reflexivity

> Source: 1707.08901v1_Providing_Self-Aware_Systems_with_Reflexivity.pdf

> Pages: 16

---


## Page 1


Providing Self-Aware Systems with Reﬂexivity
Alessandro Valitutti1 and Giuseppe Trautteur2
1 University of Bari
2 University of Naples Federico II
Abstract. We propose a new type of self-aware systems inspired by
ideas from higher-order theories of consciousness. First, we discussed the
crucial distinction between introspection and reﬂexion. Then, we focus
on computational reﬂexion as a mechanism by which a computer pro-
gram can inspect its own code at every stage of the computation. Finally,
we provide a formal deﬁnition and a proof-of-concept implementation of
computational reﬂexion, viewed as an enriched form of program inter-
pretation and a way to dynamically “augment” a computational process.
Keywords: computational reﬂexivity, computational augmentation, self-
aware systems, self-representation, self-modiﬁcation, self-monitoring
1
Introduction
Self-aware computing is a recent area of computer science concerning autonomic
computing systems capable of capturing knowledge about themselves, maintain-
ing it, and using it to perform self-adaptive behaviors at runtime[1][2][3]. Almost
all self-aware systems share one or more of three properties dealt with exten-
sively in the AI literature: self-representation, self-modiﬁcation, and persistence.
Examples of self-aware behaviors are the introspection and reﬂection features
implemented in some programming languages such as Java. Type introspection
is the ability of a program to examine the type or properties of an object at
runtime, while reﬂection3 additionally allows a program to manipulate objects
and functions at runtime.
However, neither of them have all of the above three properties. In fact,
introspection implies self-representation but not self-modiﬁcation. Moreover, re-
ﬂection is temporally-bound, since it occurs in a small portion of the program
execution. Even self-monitoring, considered as a periodic sequence of introspec-
tive events, implies persistence but not self-modiﬁcation. We may wonder if
we could have a type of computational self-awareness in which persistent self-
representation and self-modiﬁcation would occur simultaneously and yet being
functionally distinct.
In this paper, we address this issue and present a computational architecture
provided with this property, which we call computational reﬂexivity. Speciﬁcally,
3 The term reﬂection should not be confused with the term reﬂexion, which will be
discussed in Sections 2.3 and 3.
arXiv:1707.08901v1  [cs.AI]  27 Jul 2017


## Page 2


we propose to introduce introspection and reﬂection at every step of the exe-
cution, enriching the interpretation loop with additional instructions aimed to
represent the program at a meta level, combine local and global information,
and perform a second-order execution. The enriched interpreter is thus capable
of running a program and, concurrently, generating and executing a correspond-
ing modiﬁed (or “augmented”) version.
This separation between “observed” (or target) and “observing” (or aug-
mented) process allows the system to perform self-modiﬁcation at a virtual
level (i.e., on the augmented process). As a consequence, the system can choose
whether and when the modiﬁcation should be applied to the target process.
In addition to the formal deﬁnition of computational reﬂexivity, we provide a
proof-of-concept prototype, implemented through the modiﬁcation of a meta-
circular interpreter. It allows us to demonstrate that the proposed mechanism is
computationally feasible and even achievable with a small set of instructions.
In our deﬁnition of computational reﬂexivity, we have been inspired by sev-
eral concepts discussed in the literature on consciousness studies. Some of them
will be reported in the following sections. Our main source of inspiration is,
however, the notion of self-conscious reﬂexivity, as discussed in higher-order the-
ories of consciousness, and the attempts to describe it in neuroscientiﬁc [4] and
computational [5] terms.
The rest of the paper is organized as follows. In the next section, we present
an overview of self-awareness, introspection, and reﬂexion in the context of both
computer science and consciousness studies. Section 3 introduces the formal
deﬁnitions of computational reﬂexion, and Section 4 introduces the prototype.
Finally, we present a short discussion in Section 5 and draft possible applications
and next research steps in Section 6.
2
Background
2.1
Procedural Introspection
In the context of the present work, we use the term computational introspection
to indicate a program capable of accessing itself, create a self-representation,
and manipulate it. A crucial distinction should be made between the meaning
of “knowledge” underlying the notion of “representation” and “manipulation”.
For this reason, we distinguish between procedural knowledge and declarative
knowledge, the former based on computable functions, and the latter on logical
statements. Depending on which meaning of “knowledge” is adopted, there are
two diﬀerent ways to deﬁne computational introspection, called here procedural
introspection and declarative introspection, respectively.
Batali [6] claims that “introspection is the process of thinking about one’s
own thoughts and feelings. [...] To the degree that thoughts and feelings are
computational entities, computational introspection would require the ability of
a process to access and manipulate its own program and its current context” (See
Valdemir and Neto [7] on self-modifying code). In other words, computational


## Page 3


introspection corresponds to the ability of a program to process its own code as
data and modify it4.
By contrast, in declarative introspection, the access corresponds to the gen-
eration of a set of logical statements, while their manipulation is performed by
logical inference [8][9]. Batali [6] says that “The general idea is that a computa-
tional system (an agent preferably) embodies a theory of reasoning (or acting,
or whatever). This is what traditional Al systems are – each system embodies a
theory of reasoning in virtue of being the implementation of a program written
to encode the theory.”
As discussed by Cox [10], “From the very early days of AI, researchers have
been concerned with the issues of machine self-knowledge and introspective ca-
pabilities. Two pioneering researchers, Marvin Minsky and John McCarthy, con-
sidered these issues and put them to paper in the mid-to-late 1950s. [...] Minsky’s
[11] contention was that for a machine to adequately answer questions about the
world, including questions about itself in the world, it would have to have an ex-
ecutable model of itself. McCarthy [8] asserted that for a machine to adequately
behave intelligently it must declaratively represent its knowledge. [...] Roughly
Minsky’s proposal was procedural in nature while McCarthy’s was declarative.”
On the basis of these ideas, Stein and Barnden performed a more recent work
to enable a machine to procedurally simulate itself [12].
Interestingly, Johnson-Laird [13], inspired by Minsky, proposes a deﬁnition of
procedural introspection closer to the concept of computable function. He claims
that “Minsky’s formulation is equivalent to a Turing machine with an interpreter
that consults a complete description of itself (presumably without being able to
understand itself), whereas humans consult an imperfect and incomplete mental
model that is somehow qualitatively diﬀerent.” According to Smith [14], “the
program must have access, not only to its program, but to fully articulated
descriptions of its state available for inspection and modiﬁcation.” [...] Moreover,
“the program must be able to resume its operation with the modiﬁed state
information, and the continued computation must be appropriately aﬀected by
the changes.”
Unlike the use of ‘procedural’ discussed above, actually consisting of a “declar-
ative” representation of the “procedural knowledge”, we employ the term in a
more restrictive way. Procedural introspection is here limited to program code
access and modiﬁcation, without any logical modeling and inference. In this way,
we want to avoid the possible dependence of a particular declarative modeling
from the choices of the human designer, instead focusing on aspects connected
to program access and modiﬁcation.
2.2
Introspection in Consciousness Studies
Historically, all the uses of the term ‘introspection’ in computer science have been
inﬂuenced by the meaning of the same term in philosophy of mind and, later
4 In this deﬁnition, we put together self-representation and self-modiﬁcation and, thus,
the introspection and reﬂection features mentioned in Section 1.


## Page 4


on, neurosciences and cognitive science. In consciousness studies, introspection is
often discussed in the context of the so-called higher-order (HO) theories, based
on the assumption that there are diﬀerent “levels” or “orders” of mental states.
Perceptions, emotions, and thoughts are instances of ﬁrst-order mental states.
Higher-order mental states are mental states about other mental states. For
example, a thought about thinking something. Introspection is considered as “an
examination of the content of the ﬁrst-order states” [15]. It is not clear, however,
if introspection itself is a high-order state or it is involved in the occurrence of
ﬁrst-order states.
2.3
Self-Conscious Reﬂexivity
Introspection is not generally considered the main characteristic of conscious
states. In contrast, as claimed by Peters [16], “consciousness is reﬂexivity”, where
reﬂexion is the “awareness that one is perceiving”. Unlike other deﬁning char-
acteristics, such as intentionality, reﬂexivity is the only one that is considered
unique to consciousness. Trautteur remarked that Damasio was the ﬁrst scientist
to describe reﬂexion in the context of neuroscience [5]. Damasio’s deﬁnition of
reﬂexion (referred to by the term core self ) is reported in the following state-
ment:
–
It is the process of an organism caught in the act of “representing its own
changing state as it goes about representing something else” ([4, p. 170]).
This deﬁnition is meant to be based on biological (and, thus, physicalist,
objective) terms since the term ‘representation’ here denotes speciﬁc neural pat-
terns. The next statement expresses the attempt by Trautteur to translate the
above “metaphorical” deﬁnition in computational terms:
– [It] is the process of an agent “processing its own processing while processing
an input5.”
In this version, the organism is reformulated as a computational agent and
representation as a computational process. Both the above statements present a
logical issue. We refer to it as the identity paradox. It consists of the fact that
the object and the subject of the experience are perceived as the same entity. It
is a violation of the identity principle, also detectable in other expressions used
by the same and other authors such as “presence o the self to itself” or “the
identity of the owner (of experience) and the owned” [5].
2.4
Elements of Inspiration and Informal Deﬁnition of
Computational Reﬂexivity
To overcome this logical contradiction, in the present research we moved the fo-
cus from identity to simultaneity. This frame shifting was inspired by Van Gulick
5 This statement is extracted from unpublished notes by Trautteur.


## Page 5


[17], which emphasizes the simultaneity of observed and observer: “what makes
a mental state M a conscious mental state is the fact that it is accompanied by
a simultaneous and non-inferential higher-order (i.e., meta-mental) state whose
content is that one is now in M”. The above statement triggered the insight
that reﬂexion can be seen as the simultaneous occurrence of two distinct and
synchronized processes. It implies three underlying assumptions in it: temporal
extension (i.e., ‘state’ means that we are dealing with processes), distinction
(i.e., we have two separate processes), and synchronicity (i.e., the two processes
are simultaneous). Because of the temporal extension, the term ‘simultaneity’
is employed here in the sense of interval simultaneity, which refers to sequences
of events [18]. Interval simultaneity does not necessarily imply, here, the simul-
taneity of the single events. Our assumption of synchronicity requires that each
step in one of the two processes must occur only after a corresponding step in
the other one. As shown in the next section, each pair of steps are part of the
same interpretation loop.
Using the second statement as a reference, we informally deﬁne computational
reﬂexion as the concurrent (i.e. at every step of the interpretation loop) and
synchronized execution of a computer program and manipulation of its code.
Correspondingly, an interpreter capable of performing computational reﬂexion
is said to be provided with computational reﬂexivity. This deﬁnition implies that
computational reﬂexivity is a characteristic of a particular class of universal
machines.
3
Formal Deﬁnition of Computational Reﬂexion
In this section, we provide, a step a time, all building blocks for the formal deﬁni-
tion of computational reﬂexion. We assume reﬂexivity as a property applicable
to the execution of any computer program, instead of a property of a single
program. For this reason, it must rely on a particular type of program interpre-
tation. From the point of view of an interpreter, the execution of a program can
be reduced to a number of iterations of the same interpretation loop. We use
the term step to denote a single occurrence of the interpretation loop, despite
its internal complexity. We unravel below the deﬁnition of computational reﬂex-
ivity as a sequence of incremental enrichments of the interpretation loop. Each
enrichment, referred by both a textual symbol and a graphic mark, is meant to
induce a corresponding modiﬁcation at the process level.
1. Lower Step and Standard Execution
The original computational step
(i.e., the unmodiﬁed interpretation loop) is called here lower step, indicated by
the symbol (SL) and the graphic mark
. At the process level, we call target
process the overall program execution.
2. Single Introspection and Tracing
In this modiﬁed step, the interpreter
executes a local procedural introspection on the current step, returning the code of
the current instruction. It is called single introspection, indicated by the symbol
(SL, IS) and the graphic mark of the interpretation loop is
. At the process


## Page 6


level, the system generates a trace of execution, similar to the one produced by
a debugger.
3. Single Upper Step and Mirroring
The interpreter executes the in-
struction just extracted by introspection. We call it upper step, denoted by
(SL, IS, SSU). The overall loop is graphically represented as
. At the pro-
cess level, we have two identical programs simultaneously executed. We use the
term mirroring to indicate this real-time duplication of the target process.
4. Double Upper Step and Augmentation
Here the interpretation loop is
enriched with two further operations: the modiﬁcation of the current step of the
“mirrored program” by introduction of an additional instructions, and the next
step execution6. The term double upper step, with the symbol (SL, IS, SDU), in-
dicates the execution of the “mirrored” instruction and the additional one. The
overall loop is graphically represented as
. We call computational augmenta-
tion the modiﬁcation of the interpretation loop performed so far. Correspond-
ingly, we have two simultaneous processes: the target process and the augmented
process. The latter one is based on the former but modiﬁed at the step level.
5. Double Introspection and Reﬂexion
Now, we consider a particular
type of computational augmentation, in which the additional instruction of the
double upper step is a further operation of global procedural introspection. While
the local introspection returns the code of the current instruction of the target
program (i.e., the lower step deﬁned above), the global introspection returns the
code of the entire target program or a subset of it. In this case, the upper step
consists of an execution of the mirrored instructions of the target program plus
additional global instructions about it. We call double introspection this type
of double upper step, and denote it by the symbol (SL, ID, SDU). The overall
loop is represented by the graphical mark
. Finally, we deﬁne computational
reﬂexion as the process generated by the loop composed by lower step, double
introspection and double upper step.
Table 1 summarizes the schema of all components. Each row reports the
symbolic representation, the graphical mark, and the corresponding terminol-
ogy at both step and process level. In summary, the addition of speciﬁc groups
of instructions to the interpretation loop underlies the generation of diﬀerent
processes, each built on the previous one: standard execution, tracing, mirroring,
augmentation, and reﬂexion. Given a target process, the enriched interpreter
executed the related program and a concurrent version executed, at every step,
with its own code. Our deﬁnition of computational reﬂexion is thus a formal
speciﬁcation of the informal one reported in Section 2.4.
6 Although a more general class of code modiﬁcation is conceivable, we limit the focus
on the modiﬁcation by instruction insertion. As explained in the next point, the aim
is to enrich the second process with information about the target process.


## Page 7


Symbol
Step Components
Process Creation
Process
(SL)
Lower Step
Standard Execution
Target Process
(SL, IS)
+ Single Introspection
Tracing
Execution Trace
(SL, IS, SSU)
+ Single Upper Step
Mirroring
Mirror Process
(SL, IS, SDU)
→Double Upper Step
Augmentation
Augmented Process
(SL, ID, SDU)
→Double Introspection
Reﬂexion
Reﬂexive Process
Table 1. Diﬀerent versions of the interpretation loop, with the addition of step com-
ponents, and related computational processes.
4
Prototypical Implementation
As a proof of concept of the feasibility to implement computational introspection,
as deﬁned in the previous section, we developed a prototypical version. Specif-
ically, we employed and modiﬁed the code of a Lisp meta-circular interpreter
[19][20] (i.e., an interpreter of the Lisp programming language, implemented in
the same language), called here Lisp in Lisp. The main reason for using Lisp in
Lisp is that it is one of the simplest ways to implement a general-purpose inter-
preter. Indeed, it is a speciﬁc model of computation based on Church’s Lambda
Calculus [21,?]. As reported by McCarthy [23], “Another way to show that Lisp
was neater than Turing machines was to write a universal Lisp function and show
that it is briefer and more comprehensible than the description of a universal
Turing machine. This was the Lisp function eval [...]” The program is just a few
lines of code and the deﬁnition of its main function, eval, is based on the com-
position of a few primitive operators. The eval function is what is performing
the interpretation (or evaluation) process.
In this case, we call computational step (and, equivalently, interpretation
loop) the Lisp in Lisp execution between two next calls of the eval function.
Therefore, using the sequence of steps described in the previous section, we
modiﬁed the deﬁnition of eval adding additional function calls. For example,
the single introspection event correspond to a call of the function quote, which
returns the code of the argument (i.e. the instruction under execution). The com-
plete code of the program and applied examples of executions are free available
for research purpose
5
Discussion
The intuitions formalized in this paper are aimed to envision a new type of self-
aware systems. While almost all state-of-the-art systems are based on introspec-
tion, we propose to consider reﬂexion as the main aspect of self-awareness. We


## Page 8


could intuitively deﬁne computational reﬂexion as “a mechanism for making a
computational process continuously self-informed”. The expression “mechanism
of making” expresses the fact that reﬂexion is deﬁned as a particular type of
interpreter. Indeed, we focused on the interpretation loop and modiﬁed it. Re-
ﬂexion is not the property of a speciﬁc class of computer programs but, instead,
something that can be provided to any executable programs through this form
of interpretation. Through reﬂexion, the standard program execution (i.e., the
target process) is dynamically “reﬂected” into the execution of its augmented
counterpart (i.e., the reﬂexive process).
As explained in Section 3, each instruction of the target program is executed
twice: the ﬁrst time (as sequence of lower steps) to achieve the standard execu-
tion (and generate the target process), and the second time (as sequence of upper
steps) as part of the reﬂexive process. In the above deﬁnition, the term “self” is
not referring to a single entity but to a couple of mutually interactive entities.
This duality between the two processes is the way we theoretically address the
identity paradox mentioned in Section 2.3.
6
Possible Applications and Future Work
The properties identiﬁed in the previous section allow us to conceive some inter-
esting uses of the reﬂexive augmentation of program execution. For example, we
could see the execution of the target program and the corresponding reﬂexive
augmentation as performed by two separate but synchronized devices. Speciﬁ-
cally, we could have an autonomous agent (e.g. a robot in a physical environment)
and an interfaced web service implementing reﬂexion. Therefore, computational
reﬂexion could be used as a way to provide a system with a temporary “stream-
ing of self-awareness”.
The aimed next steps of our research are focused on the following aspects.
Firstly, we intend to further develop the proposed formalization and achieve pos-
sible interesting implications as formal theorems. Secondly, we aim to study the
degree to which the reﬂexive process should give feedback to the target process
and modify the related program. In other words, we would like to investigate
aspects of run-time “virtual” self-modiﬁcation, not yet taken into account, at
this stage of the research, in our prototype.
A crucial issue is about eﬃciency. We need to investigate to what degree
the combination of step-level local and global introspection and corresponding
execution can be feasible performed. If the target program is suﬃciently complex,
there is a limitation in the number of instructions capable of being executed along
the duration of the interpretation loop. In this case, the procedural modeling
of the target process should be optimized. Finally, we intend to investigate the
extent to which computational reﬂexivity could be employed to achieve a form of
self organization, using the information gathered by the step-level introspective
acts to train a self-reinforcement system.


## Page 9


References
1. P. R. Lewis, A. Chandra, F. Faniyi, K. Glette, T. Chen, R. Bahsoon, J. Torresen,
X. Yao, Architectural aspects of self-aware and self-expressive computing systems:
from psychology to engineering, Computer 48 (8) (2015) 62–70.
2. J. Torresen, C. Plessl, X. Yao, Self-aware and self-expressive systems, Computer
48 (7).
3. E. Amir, M. Anderson, V. K. Chaudhri, Report on DARPA Workshop on self-
aware computer systems, Tech. rep., Artiﬁcial Intelligence Center SRI Interna-
tional, Washington DC (2004).
4. A. Damasio, The Feeling of What Happens: Body and Emotion in the Making of
Consciousness, Harcourt Brace, New York, 1999.
5. G. Trautteur, Some remarks about consciousness, Networks 3-4 (2004) 165–172.
6. J. Batali, Computational introspection, Tech. Rep. AI-M-701, Massachussetts In-
stitute of Technology (MIT), Cambridge, MA US (1983).
7. A. Valdemir, J. Neto, Adaptivity in programming languages, Transactions on In-
formation Science and Applications 4 (4) (2007) 779–786.
8. J. McCarthy, Programs with common sense, in: Proceedings of the Teddington
Conference on the Mechanization of Thought Processes, London, 1959.
9. R. Weyhrauch, Prolegomena to a theory of formal reasoning, Artiﬁcial intelligence
13 (1).
10. M. T. Cox, Metacognition in computation: a selected research review, Artiﬁcial
Intelligence 169 (2) (2005) 104–141.
11. M. Minsky, Matter, mind, and models, in: M. Minsky (Ed.), Semantic Information
Processing, MIT Press, Cambridge, MA, 1969, pp. 425–432.
12. G. Stein, J. Barnden, Towards more ﬂexible and common-sensical reasoning about
beliefs, in: M. Cox, M. Freed (Eds.), Proceedings of the 1995 AAAI Spring Sympo-
sium on Representing Mental States and Mechanisms, AAAI Press, Menlo Park,
CA, 1995, pp. 127–135.
13. P. N. Johnson-Laird, A computational analysis of consciousness, Cognition and
Brain Theory 6 (1983) 499–508.
14. B. Smith, Reﬂection and semantics in a procedural language, Tech. Rep. 272, MlT
Laboratory of Computer Science (1982).
15. M. Overgaard, J. Mogensen, An integrative view on consciousness and in-
trospection, Review of Philosophy and Psychology (2016) 1–13doi:10.1007/
s13164-016-0303-6.
URL http://dx.doi.org/10.1007/s13164-016-0303-6
16. F. Peters, Theories of consciousness as reﬂexivity, The Philosophical Forum 44
(2013) 341–372.
17. R. Van Gulick, Consciousness, in: E. N. Zalta (Ed.), The Stanford Encyclopedia
of Philosophy, spring 2014 Edition, The Metaphysics Research Lab, 2014.
18. M. Jammer, Concept of simultaneity: from antiquity to Einstein and beyond, The
Johns Hopkins University Press, 2006.
19. C. Landauer, K. L. Bellman, Self-modeling systems, in: Proceedings of the 2nd
international conference on Selfadaptive software: applications (IWSAS’01), Bala-
tonf¨ured, Hungary, 2001, pp. 238–256.
20. P. Graham. The roots of lisp [online] (18 January 2002) [cited 5 September 2016].
21. A. Church, The Calculi of Lambda-Conversion, Princeton University Press, Prince-
ton, N.J., 1941.


## Page 10


22. J. McCarthy, Recursive functions of symbolic expressions and their computation
by machine, part i, Communications of the ACM 3 (1960) 184–195.
23. J. McCarthy, History of lisp, ACM SIGPLAN Notices - Special issue: History of
programming languages conference 13 (8) (1978) 217–223.
24. G. L. Steele, Common Lisp the Language, 2nd Edition, Digital Press, 1990.
Appendix A: Code Description
The following integrative material is provisionally provided as appendix of the
paper. In the ﬁnal version, this material will be provided in a website.
We employed the code of an interpreter of the Lisp programming language,
implemented in the same language, and called here Lisp in Lisp. Speciﬁcally,
since the term Lisp is currently used to denote an entire family of programming
languages sharing common characteristics, we tested and run the code in Com-
mon Lisp [24]. Rather than the original formulation of eval by McCarthy [22],
we adopted the simpler version by Paul Graham [20], which also found a bug in
the original version and removed it7.
In this context, we deﬁne computational step (and, equivalently, interpre-
tation loop) as the Lisp in Lisp execution between two next calls of the eval
function. Appendix 6 contains the code of the Lisp in Lisp (i.e., the eval. func-
tion) and its modiﬁed version (called eval-augment) implementing reﬂexion.
Appendix B: Components of Computational Reﬂexion
In the same way proceeded in the previous section, we focused on the interpre-
tation loop and gradually enriched to obtain the version implementing compu-
tational reﬂexion.
1. Lower Step.
It is equivalent to the interpretation loop deﬁned above.
2. Single (Local) Introspection.
The current eval call returns the code
of the current instruction, consisting of a function call.
3. Single Upper Step.
The code of the current function call, produced by
the local introspection, is in turn executed (i.e. eval is called on it).
4. Double Upper Step.
The code generated by local introspection is en-
riched with additional instructions. As an example, we added a print call
to the output of the current call. In this way, the interpreter will display on
the terminal the trace of execution.
7 We have found a small bug in Graham’s code as well. In the deﬁnition body of
the <pair.> function, there is a call to the <list> function, which is a system
function. Since the set of primitive operators should not include <list>, we deﬁned
the function <list.> and used it to replace all the occurrences of <list> in the
deﬁnition body of <pair.> In this note, we rounded the function names with angular
parenthesis to separate them more clearly from the rest of the text.


## Page 11


5. Double Introspection.
Finally, the interpretation loop is enriched with
the instruction for global introspection. In other words, it returns the code
of the entire program.
In summary, at any stage of the computation, the interpreter accesses and
executes the code both locally and globally. In particular, the program code
could be modiﬁed at each step and, thus, inﬂuence the next execution.
As a speciﬁc example, Appendix 7 shows the Lisp deﬁnition of the function
my-last, which gets a list as input and returns its last element as output.
Appendix C: Lisp Code
The code of the function eval. corresponds to the version of the Lisp in Lisp
by Paul Graham [20]. We modiﬁed it and deﬁned eval-augment, as a proof-of-
concept version of the reﬂexive interpreter, with the following instruction:
(augment input output pred).
The function augment applies the predicate pred to the input and output
of the current step. The speciﬁc implementation of pred in this example is
*pred*, which extract the code of the current instruction and execute it again,
thus performing the “mirroring” discussed in Section 3 of the paper.
(defun eval .
( e a )
(cond
((atom e )
( assoc .
e a ))
((atom ( car
e ))
(cond
(( eq ( car
e )
’ quote )
( cadr
e ))
(( eq ( car
e )
’atom)
(atom
( eval .
( cadr
e ) a ) ) )
(( eq ( car
e )
’eq)
(eq
( eval .
( cadr
e ) a )
( eval .
( caddr e ) a ) ) )
(( eq ( car
e )
’ car )
( car
( eval .
( cadr
e ) a ) ) )
(( eq ( car
e )
’ cdr )
( cdr
( eval .
( cadr
e ) a ) ) )
(( eq ( car
e )
’ cons )
( cons
( eval .
( cadr
e ) a )
( eval .
( caddr e ) a ) ) )
(( eq ( car
e )
’cond)
( evcon .
( cdr
e ) a ))
( ’ t
( eval .
( cons ( assoc .
( car
e ) a )
( cdr
e ))
a ) ) ) )
(( eq ( caar
e )
’ l a b e l )
( eval .
( cons ( caddar e )
( cdr
e ))
( cons ( l i s t .
( cadar
e )
( car
e ))
a ) ) )
(( eq ( caar
e )
’ lambda )
( eval .
( caddar e )
(append .
( pair .
( cadar
e )
( e v l i s .
( cdr
e ) a ))
a ) ) ) ) )


## Page 12


(defun null .
(x)
(eq x
’ ( ) ) )
(defun and .
(x y)
(cond (x (cond (y
’ t )
( ’ t
’ ( ) ) ) )
( ’ t
’ ( ) ) ) )
(defun not .
(x)
(cond (x
’ ( ) )
( ’ t
’ t ) ) )
(defun append .
(x y)
(cond (( null .
x) y)
( ’ t
( cons ( car x)
(append .
( cdr x) y ) ) ) ) )
(defun
l i s t .
(x y)
( cons x ( cons y
’ ( ) ) ) )
(defun pair .
(x y)
(cond ((and .
( null .
x)
( null .
y ))
’ ( ) )
((and .
(not .
(atom x ))
(not .
(atom y ) ) )
( cons ( l i s t .
( car x)
( car y ))
( pair .
( cdr x)
( cdr y ) ) ) ) ) )
(defun assoc .
(x y)
(cond
(( null .
y)
’ ( ) )
(( eq ( caar y) x)
( cadar y ))
( ’ t
( assoc .
x ( cdr y ) ) ) ) )
(defun evcon .
( c a )
(cond (( eval .
( caar
c ) a )
( eval .
( cadar
c ) a ))
( ’ t
( evcon .
( cdr
c ) a ) ) ) )
(defun
e v l i s .
(m a )
(cond (( null . m)
’ ( ) )
( ’ t
( cons ( eval .
( car m) a )
( e v l i s .
( cdr m) a ) ) ) ) )
(defun eval−augment ( e a pred )
( let ∗
(( input
( l i s t
e a ))
( output
(cond
((atom e )
( assoc .
e a ))
((atom ( car
e ))
(cond
(( eq ( car
e )
’ quote )
( cadr
e ))


## Page 13


(( eq ( car
e )
’atom)
(atom
( eval−augment ( cadr
e ) a pred ) ) )
(( eq ( car
e )
’eq)
(eq
( eval−augment ( cadr
e ) a pred )
( eval−augment ( caddr e ) a pred ) ) )
(( eq ( car
e )
’ car )
( car
( eval−augment ( cadr
e ) a pred ) ) )
(( eq ( car
e )
’ cdr )
( cdr
( eval−augment ( cadr
e ) a pred ) ) )
(( eq ( car
e )
’ cons )
( cons
( eval−augment ( cadr
e ) a pred )
( eval−augment ( caddr e ) a pred ) ) )
(( eq ( car
e )
’cond)
( evcon .
( cdr
e ) a ))
( ’ t
( eval−augment ( cons ( assoc .
( car
e ) a )
( cdr
e ))
a pred ) ) ) )
(( eq ( caar
e )
’ l a b e l )
( eval−augment ( cons ( caddar e )
( cdr
e ))
( cons ( l i s t .
( cadar
e )
( car
e ))
a )
pred ))
(( eq ( caar
e )
’ lambda )
( eval−augment ( caddar e )
(append .
( pair .
( cadar
e )
( e v l i s .
( cdr
e ) a ))
a )
pred ) ) ) ) )
( augment input
output
pred )
output ))
(defun augment ( input
output
pred )
( setq
∗done∗(append ∗done∗( l i s t
( l i s t
input
output ) ) ) )
( funcall
pred ∗done ∗))
( setq
∗pred∗#’(lambda ( done )
( let ∗
(( next
( car
( last
done ) ) )
( input
( car
next ))
( e
( car
input ))
( a ( cadr
input ))
( output1
( eval .
e a ) ) )
(format t
( concatenate
’ string
( write−to−string
input ) ”˜%”
”−> ” ( write−to−string
output1 ) ”˜%” ))
t ) ) )


## Page 14


7
Appendix E: Examples of Execution
As a simple example, the function augment and the predicate *pred* are applied
to simple data (the atom a with value 1, and the function car returning the ﬁrst
element of the list (a b). In particular, it is applied to the simple recursive
function my-last, returning the last element of a list.
CL−USER( 3 5 6 ) :
( eval−augment
’ a
’ ( ( a
1)) ∗pred2 ∗)
1
CL−USER( 3 5 7 ) :
( eval−augment
’ a
’ ( ( a
1)) ∗pred1 ∗)
(A ((A 1 ) ) )
−> 1
1
CL−USER( 3 6 0 ) :
( eval .
’( car
’( a b ))
n i l )
A
CL−USER( 3 6 1 ) :
( eval−augment
’( car
’( a b ))
n i l
∗pred2 ∗)
A
CL−USER( 3 6 2 ) :
( eval−augment
’( car
’( a b ))
n i l
∗pred1 ∗)
( ’ (A B) NIL)
−> (A B)
((CAR ’(A B)) NIL)
−> A
A
CL−USER( 3 7 0 ) :
( setq
e
’( my−last
’( a b c ) ) )
(MY−LAST ’(A B C))
CL−USER( 3 7 1 ) :
( setq
a
’(
( my−last ( l a b e l
my−last
( lambda (x)
(cond
(( null .
x)
’ n i l )
(( null .
( cdr x ))
( car x ))
( ’ t
( my−last ( cdr x ) ) )
) ) ) )
( null .
( l a b e l
null .
( lambda (x)
(eq x
n i l ) ) ) )
))
((MY−LAST (LABEL MY−LAST (LAMBDA (X)
(COND # # #))))
(NULL.
(LABEL NULL.
(LAMBDA (X)
(EQ X NIL ) ) ) ) )
CL−USER( 3 7 2 ) :
( eval .
e a )
C
CL−USER( 3 7 3 ) :
( eval−augment e a ∗pred2 ∗)
C
CL−USER( 3 7 4 ) :
( eval−augment e a ∗pred1 ∗)
((COND ((NULL. X)
’NIL)
((NULL.
(CDR X))
(CAR X))
( ’T (MY−LAST (CDR X) ) ) )


## Page 15


((X (A B C))
(MY−LAST
(LABEL MY−LAST
(LAMBDA (X)
(COND ((NULL. X)
’NIL)
((NULL.
(CDR X))
(CAR X))
( ’T (MY−LAST (CDR X) ) ) ) ) ) )
(MY−LAST
(LABEL MY−LAST
(LAMBDA (X)
(COND ((NULL. X)
’NIL)
((NULL.
(CDR X))
(CAR X))
( ’T (MY−LAST (CDR X) ) ) ) ) ) )
(NULL.
(LABEL NULL.
(LAMBDA (X)
(EQ X NIL ) ) ) ) ) )
−> C
( ( (LAMBDA (X)
(COND ((NULL. X)
’NIL)
((NULL.
(CDR X))
(CAR X))
( ’T (MY−LAST (CDR X) ) ) ) )
’(A B C))
((MY−LAST
(LABEL MY−LAST
(LAMBDA (X)
(COND ((NULL. X)
’NIL)
((NULL.
(CDR X))
(CAR X))
( ’T (MY−LAST (CDR X) ) ) ) ) ) )
(MY−LAST
(LABEL MY−LAST
(LAMBDA (X)
(COND ((NULL. X)
’NIL)
((NULL.
(CDR X))
(CAR X))
( ’T (MY−LAST (CDR X) ) ) ) ) ) )
(NULL.
(LABEL NULL.
(LAMBDA (X)
(EQ X NIL ) ) ) ) ) )
−> C
( ( (LABEL MY−LAST
(LAMBDA (X)
(COND ((NULL. X)
’NIL)
((NULL.
(CDR X))
(CAR X))
( ’T (MY−LAST (CDR X) ) ) ) ) )
’(A B C))
((MY−LAST
(LABEL MY−LAST
(LAMBDA (X)
(COND ((NULL. X)
’NIL)
((NULL.
(CDR X))
(CAR X))
( ’T (MY−LAST (CDR X) ) ) ) ) ) )
(NULL.
(LABEL NULL.
(LAMBDA (X)
(EQ X NIL ) ) ) ) ) )
−> C
((MY−LAST ’(A B C))
((MY−LAST


## Page 16


(LABEL MY−LAST
(LAMBDA (X)
(COND ((NULL. X)
’NIL)
((NULL.
(CDR X))
(CAR X))
( ’T (MY−LAST (CDR X) ) ) ) ) ) )
(NULL.
(LABEL NULL.
(LAMBDA (X)
(EQ X NIL ) ) ) ) ) )
−> C
C

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]