---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.05676v6
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1908.05676v6_Plato_and_the_foundations_of_mathematics

> Source: 1908.05676v6_Plato_and_the_foundations_of_mathematics.pdf

> Pages: 49

---


## Page 1


PLATO AND THE FOUNDATIONS OF MATHEMATICS
SAM SANDERS
Abstract. Plato is well-known in mathematics for the eponymous founda-
tional philosophy Platonism based on ideal objects. Plato’s allegory of the
cave provides a powerful visual illustration of the idea that we only have ac-
cess to shadows or reﬂections of these ideal objects. An inquisitive mind might
then wonder what the current foundations of mathematics, like e.g. Reverse
Mathematics and the associated G¨odel hierarchy, are reﬂections of. In this
paper, we identify a hierarchy in higher-order arithmetic that maps to the
Big Five of Reverse Mathematics under the canonical embedding of higher-
order into second-order arithmetic. Conceptually pleasing, the latter mapping
replaces uncountable objects by countable ‘codes’, i.e. the very practise of
formalising mathematics in second-order arithmetic. This higher-order hier-
archy can be deﬁned in Hilbert-Bernays’ Grundlagen, the spiritual ancestor
of second-order arithmetic, while the associated embedding preserves equiva-
lences. Also, in contrast to Kohlenbach’s hierarchy based on discontinuity, our
hierarchy can be formulated in terms of (classically valid) continuity axioms
from Brouwer’s intuitionistic mathematics. Moreover, the higher-order coun-
terpart of sequences is provided by nets, aka Moore-Smith sequences, while
the gauge integral is the correct generalisation of the Riemann integral. For
all these reasons, we baptise our higher-order hierarchy the Plato hierarchy.
1. Introduction
1.1. Plato, Platonism, and the Plato hierarchy. The Greek philosopher Plato
is perhaps best known in mathematics and related ﬁelds for the eponymous philos-
ophy of mathematics Platonism. The OED entry for Platonism reads as follows.
the theory that mathematical objects are objective, timeless enti-
ties, independent of the physical world and the symbols that rep-
resent them.
Platonism postulates the existence of ideal or abstract objects, while Plato’s al-
legory of the cave provides a powerful illustration of the idea that we only have
access to very limited reﬂections (or: shadows) of these ideal or abstract objects,
as expressed by G¨odel in [26, p. 323]. Taking this view seriously, we may ask the
following -perhaps uncomfortable- questions: what are the current foundations of
mathematics reﬂections of? What is the nature of this reﬂection? In this paper,
we provide precise answers to these questions for a fragment of the foundations of
mathematics, namely Reverse Mathematics and the G¨odel hierarchy. We hereafter
assume familiarity with these italicised notions; an introduction is in Section 1.2.
In a nutshell, we identify a hierarchy in higher-order arithmetic that maps to
the Big Five of Reverse Mathematics under the canonical ‘ECF’ (see Remark 2.5)
Department of Mathematics, TU Darmstadt
E-mail address: sasander@me.com.
2010 Mathematics Subject Classiﬁcation. 03B30, 03D65, 03F35.
Key words and phrases. reverse mathematics, nets, Moore-Smith sequences, hierarchies.
arXiv:1908.05676v6  [math.LO]  13 Aug 2020


## Page 2


2
PLATO AND THE FOUNDATIONS OF MATHEMATICS
embedding of higher-order into second-order arithmetic.
Conceptually pleasing,
ECF replaces uncountable objects by countable ‘codes’, i.e. the very practise of for-
malising mathematics in second-order arithmetic. Our higher-order hierarchy can
be deﬁned in Hilbert-Bernays’ Grundlagen der Mathematik ([33,34]), the spiritual
ancestor of second-order arithmetic, while the associated ECF embedding preserves
equivalences.
Moreover, the higher-order counterpart of sequences is provided
by nets (aka Moore-Smith sequences; see Section 2.3), while the gauge integral
([60, §3]) is the correct generalisation of the Riemann integral. The correct notion
of ‘open set’ shall be seen to be uncountable unions of open balls (and not character-
istic functions as in [64,74]). Finally, our higher-order hierarchy can be formulated
in terms of classically valid continuity axioms of intuitionistic mathematics, called
neighbourhood function principle, in contrast1 to Kohlenbach’s higher-order hier-
archy based on discontinuity from [42]. In this sense, our hierarchy constitutes a
‘return to Brouwer’ and is ‘orthogonal’ to the usual comprehension hierarchy.
For all the above reasons, we baptise the aforementioned higher-order hierarchy
the Plato hierarchy. We discuss our results in more detail in Section 1.3, while Sec-
tion 1.2 provides an introduction to Reverse Mathematics and the G¨odel hierarchy.
1.2. Hilbert, G¨odel, and classiﬁcation. During his invited lecture at the second
International Congress of Mathematicians of 1900 in Paris, David Hilbert presented
his famous list of 23 open problems ([31]) that would have a profound inﬂuence on
modern mathematics. Hilbert’s list contains a number of foundational/logical prob-
lems. For instance, Problem 2 pertains to the consistency of mathematics, i.e. the
fact that no contradiction can be proved in mathematics. Hilbert later elaborated
on Problem 2 by formulating Hilbert’s program for the foundations of mathematics
([32]); this program calls for a proof of consistency of all of mathematics using only
methods from so-called ﬁnitistic2 mathematics.
However, G¨odel’s famous incompleteness theorems ([27]) are generally believed
to show that Hilbert’s program is impossible: G¨odel namely showed that any logical
system rich enough to express arithmetic, cannot even prove its own consistency,
let alone that of all of mathematics. Moreover, one can build stronger and stronger
logical systems by consecutively appending the formula expressing the system’s
consistency (or inconsistency). This proliferation of logical systems has not led to
chaos, but to remarkable order and surprising regularity, as follows: as a positive
outcome of G¨odel’s negative solution to Hilbert’s program, the notion of consistency
gave rise to the G¨odel hierarchy presented in Figure 1: a collection of logical systems
linearly ordered via increasing consistency strength.
As to its import, the G¨odel hierarchy is claimed to capture all systems that are
natural or foundationally important . For instance, Simpson claims the following
regarding the G¨odel hierarchy and the consistency strength ordering ‘<’:
It is striking that a great many foundational theories are linearly
ordered by <. Of course it is possible to construct pairs of artiﬁcial
theories which are incomparable under <. However, this is not the
case for the “natural” or non-artiﬁcial theories which are usually
regarded as signiﬁcant in the foundations of mathematics. ([83])
1It should be noted that ECF converts the existence of a discontinuous function to ‘0 = 1’, as
discussed in Remark 2.5. The (classically valid) intuitionistic axiom in question is NFP from [91].
2The system PRA in Figure 1 is believed to capture Hilbert’s ﬁnitistic mathematics ([87]).


## Page 3


PLATO AND THE FOUNDATIONS OF MATHEMATICS
3
Burgess and Koellner corroborate Simpson’s claims in [15, §1.5] and [40, §1.1]; the
former refers to the G¨odel hierarchy as the Fundamental Series. Precursors to the
G¨odel hierarchy may be found in the work of Wang ([94]) and Bernays ([8, 11]).
Friedman ([21]) has studied the linear nature of the G¨odel hierarchy in great detail,
including many more systems than present in Figure 1. The importance of the
logical systems present in Figure 1 is discussed below the latter.
strong













large cardinals
...
ZFC
ZC
simple type theory
medium

















Z2 ≡∪kΠ1
k-CA0
...
Π1
2-CA0
Π1
1-CA0
ATR0
ACA0
weak







WKL0
RCA0
PRA
bounded arithmetic
Figure 1. The G¨odel hierarchy (taken from [83, p. 111])
We now discuss the systems in Figure 1 and their role in mathematics and computer
science. In this light, the G¨odel hierarchy becomes a central object of study in logic
to which all sub-ﬁelds contribute.
(i) Bounded arithmetic provides a logical framework for the study of polyno-
mial time computation, and hence the ‘P versus NP’ problem ([16, I, II]).
(ii) The system RCA0 is the ‘base theory’ of Reverse Mathematics (RM here-
after; see Section 2.1) and formalises ‘computable mathematics’.
(iii) The system WKL0 provides a partial realisation of Hilbert’s program ([80,
83]). The ‘ﬁnitistic’ mathematics as in this program, is shown by Tait to
be captured by the system PRA ([87]).
(iv) The system ATR0 is the upper limit of predicative mathematics ([79,83]).
(v) The system Z2, called second-order arithmetic, originates from the logical
system H used by Hilbert-Bernays in Grundlagen der Mathematik ([33,34]).
(vi) The system ZFC is Zermelo-Fraenkel set theory with the axiom of choice,
i.e. the standard/typical foundations of mathematics ([38]).
(vii) Large cardinal axioms express regularities of the universe of sets and settle
the truth of (certain) theorems independent of ZFC ([38]).
We refer to [81,82] for an overview of RM, and to [85] for an introduction. A brief
introduction to Kohlenbach’s higher-order RM may be found in Section 2.1.


## Page 4


4
PLATO AND THE FOUNDATIONS OF MATHEMATICS
Finally, the G¨odel hierarchy exhibits some remarkable robustness: we can per-
form the following modiﬁcations and the hierarchy remains largely unchanged.
(I) Instead of the consistency strength ordering, we can order via inclusion:
Simpson claims that inclusion and consistency strength yield the same3
G¨odel hierarchy as depicted in [83, Table 1] and Figure 1. Some exceptional
statements do fall outside of the inclusion-based G¨odel hierarchy.
(II) We can replace systems with their higher-order counterparts (see e.g. [42])
boasting a much richer language.
These higher-order systems generally
prove the same sentences as their second-order counterpart.
As suggested by item (I), there are some examples of theorems that fall outside of
the G¨odel hierarchy based on inclusion, like special cases of Ramsey’s theorem and
the axiom of determinacy from set theory ([35, 48]). The latter axiom restricted
to certain formula classes even yields a parallel hierarchy for the medium range of
the G¨odel hierarchy based on inclusion. By the results in [60–64], basic compact-
ness properties like the Heine-Borel theorem for uncountable covers or Pincherle’s
theorem, yield such parallel hierarchies in higher-order arithmetic.
1.3. Plato, G¨odel, and their hierarchies.
1.3.1. Introduction. We provide an overview of the results to be obtained in this
paper, including the Plato hierarchy. The following ﬁgure provides a neat summary,
while deﬁnitions may be found in Sections 1.3.2, 2.2, and 3.1. In this paper, we
establish the hierarchy on the right-hand side of Figure 2 and associated results.
6
RCA0
WKL0
ACA0
ATR0
⇧1
1-CA0
⇧1
1-CA0
+BOOT
proves ∆0
1-comprehension
$ Dini’s theorem.
$ countabe Heine-Borel
compactness
$ Riemann int. thms
$ Monotone conv. thm
$ Ascoli-Arzela
$ properties of closed sets
given by countable unions
$ range of f : N ! N exists
$ perfect set theorem for
closed sets as countable unions
$ Cantor-Bendixson for
closed sets as countable unions
6
RCA!
0
WKLu
BOOT
⌃-TR
second-order arithmetic
higher-order arithmetic
plus ∆-comprehension
or countable choice
$ Dini’s theorem for nets
$ uncountabe Heine-Borel
compactness
$ gauge integral thms
$ Monotone conv. thm for nets
$ Ascoli-Arzela for nets
$ properties of closed sets
given by uncountable unions
$ range of Y : NN ! N exists
$ perfect set theorem for closed sets
given by uncountable unions
$ ATR0 + BOOT
$ Cantor-Bendixson for
closed sets as uncountable unions
 −
ECF
 −
ECF
Figure 2. The connection between the Plato and G¨odel hierar-
chies: ECF converts the right to the left hierarchy.
The systems at the same height in Figure 2 have the same ﬁrst-order strength as
the ECF translation converts the right-hand side into the left-hand side, taking into
3Simpson mentions in [83] the caveat that e.g. PRA and WKL0 have the same ﬁrst-order
strength, but the latter is strictly stronger than the former.


## Page 5


PLATO AND THE FOUNDATIONS OF MATHEMATICS
5
account the caveat in Remark 1.1 regarding ECF (see Remark 2.5 for the latter). In
light of Figure 2, it is no exaggeration to claim that the Big Five and the associated
RM arise as special cases of higher-order RM via the lossy ECF translation. For
this reason, the hierarchy formed by BOOT and its ilk is called the Plato hierarchy,
inspired by Plato’s famous writings on ideal objects and their role in foundations
of mathematics, the allegory of the cave in particular.
We note that the RM of the gauge integral was studied in detail in [60, §3]. We
brieﬂy discuss this integral, and the associated RM-results, in Remark 4.28. We
note that nets and the gauge integral are well-known generalisations of sequences
and the Riemann integral (see Section 2.3 and Remark 4.28). We also note that ECF
translates the existence of discontinuous functions to ‘0 = 1’; since Kohlenbach’s
higher-order hierarchy ([42]) makes essential use of discontinuous functions, the
Plato hierarchy is seen to be markedly diﬀerent. In particular, as discussed below,
the Plato hierarchy constitutes a ‘return to Brouwer’ in a precise sense.
Moreover, the axioms in the Plato hierarchy are explosive in that combining
them with comprehension axioms from Kohlenbach’s hierarchy yields axioms much
stronger than the individual components. The following remark is indispensable.
Remark 1.1 (The nature of ECF). We discuss the meaning of the words ‘A is
converted into B by the ECF-translation’. Such statement is obviously not to be
taken literally, as e.g. [BOOT]ECF is not verbatim ACA0. Nonetheless, [BOOT]ECF
follows from ACA0 by noting that quantiﬁers over NN may be replaced by quantiﬁers
over N in case all functionals on NN are continuous (see Theorem 3.2). Similarly,
[HBU]ECF is not verbatim the Heine-Borel theorem for countable covers, but the
latter does imply the former by noting that for uncountable covers represented by
continuous functions, there is a trivial countable sub-cover enumerated by Q.
In general, that (continuous) objects have countable representations is the very
foundation of the formalisation of mathematics in L2, and identifying (continuous)
objects and their countable representations is routinely done. Thus, when we say
‘A is converted into B by the ECF-translation’, we mean that [A]ECF is about a
class of continuous objects to which B is immediately seen to apply, with a possi-
ble intermediate step involving representations. Since this kind of step forms the
bedrock of (second-order) RM, it would therefore appear harmless in this context.
Taking into account the previous remark, the literature already boasts some
results similar to the ones in Figure 2. For instance, the RM of the Vitali covering
theorem for uncountable covers, called WHBU, is studied in [62, §3]. Now, WHBU
has the ﬁrst-order strength of WWKL (see [82, X.1]) and the associated equivalences
in measure theory ﬁt between HBU/WKL and RCAω
0 /RCA0 in Figure 2.
Next, it was noted above Remark 1.1 that Kohlenbach’s hierarchy from [42] is
based on discontinuity, while the Plato hierarchy is markedly diﬀerent. Indeed,
BOOT and related principles map to quite fundamental axioms under ECF, i.e. the
replacement of higher-order objects by continuous-by-deﬁnition RM-codes. In light
of the previous, one might expect that BOOT and related principles are somehow
connected to continuity. We shall establish that these axioms are indeed equivalent
to fragments of a classically valid continuity axiom from Brouwer’s intuitionistic
analysis, called neighbourhood function principle (NFP). In particular, while higher-
order comprehension does not capture the Plato hierarchy, fragments of NFP can
capture the latter. Thus, the Plato hierarchy is a ‘return to Brouwer’ in the sense


## Page 6


6
PLATO AND THE FOUNDATIONS OF MATHEMATICS
that we avoid discontinuous functions and work with (classically valid) axioms from
intuitionistic mathematics.
Once the results of Figure 2 have sunk in, an obvious questions is: What is the
Plato hierarchy a reﬂection of? What is the nature of this reﬂection? We provide
a partial answer in this paper by generalising the equivalence between BOOT and
the monotone convergence theorem for nets indexed by Baire space to larger index
sets. We also provide a ‘translation’ that reduces the new equivalence to the old
one. Thus, a more apt name perhaps would have been the Plato universe.
Finally, while ECF is clearly a ‘lossy’ translation, results can also be ‘lifted’ in the
other direction in Figure 2, i.e. from second-order to higher-order arithmetic: the
proof of Theorem 3.19 establishes that the monotone convergence theorem for nets
in the unit interval implies BOOT using so-called ∆-comprehension. This proof is
an almost verbatim copy of the associated second-order proof in [82, p. 107], i.e.
there is also a connection at the level of proofs. This is not an isolated case: many
so-called recursive counterexamples give rise to reversals in RM, and these results
can be lifted to obtain higher-order results in many cases, as studied in detail in
[75, 76]. We caution the reader that these ‘lifted’ proofs are not optimal, in that
they generally do not go through in the weakest possible base theory.
1.3.2. The inhabitants of the Plato hierarchy. We discuss in detail the concepts
and axioms involved with (part of) the Plato hierarchy as depicted in Figure 2. We
shall introduce the notion of net and the bootstrap axiom BOOT, starting from the
former’s historical roots. We also discuss our ‘uncountable’ concept of open set to
be used in the Plato hierarchy.
Abstraction is an integral part of mathematics, from Euclid’s Elements to the
present day. In this spirit, E. H. Moore presented a framework called General Anal-
ysis at the 1908 ICM in Rome ([49]) that was to be a ‘unifying abstract theory’
for various parts of analysis.
Indeed, Moore’s framework captures various limit
notions in one abstract concept ([50]) and even includes a generalisation of the con-
cept of sequence to possibly uncountable index sets (called directed sets), nowadays
called nets or Moore-Smith sequences. These were ﬁrst described in [51] and then
formally introduced by Moore and Smith in [52]. They also established the generali-
sation from sequences to nets of various basic theorems due to Bolzano-Weierstrass,
Dini, and Arzel`a ([52, §8-9]). More recently, nets are central to the development
of domain theory (see [23, 24, 28]), including a deﬁnition of the Scott and Lawson
topologies in terms of nets. Moreover, sequences cannot be used in this context, as
expressed in a number of places:
[. . . ] clinging to ascending sequences would produce a mathemati-
cal theory that becomes rather bizarre, whence our move to directed
families. ([28, p. 59])
Turning to foundations, we feel that the necessity to choose chains
where directed subsets are naturally available (such as in function
spaces) and thus to rely on the Axiom of Choice without need, is a
serious stain on this approach. ([1, §2.2.4]).
Thus, nets enjoy a rich history, as well as a mainstream (and essential) status in
mathematics and computer science. Motivated by the above, the study of nets in
RM was undertaken in [72–74]. We continue the RM study of nets in this paper,
and the truly novel results in this paper are as follows.


## Page 7


PLATO AND THE FOUNDATIONS OF MATHEMATICS
7
(i) basic convergence theorems for nets ‘bootstrap’ themselves (or: explode)
to higher levels of the hierarchy when combined with Kohlenbach’s com-
prehension axioms from the medium range.
(ii) basic convergence theorems for nets are equivalent to the following compre-
hension axiom BOOT, plus potentially countable choice.
The axiom BOOT is deﬁned as follows, and discussed in detail in Section 3.1.
Deﬁnition 1.2. [BOOT] (∀Y 2)(∃X1)(∀n0)

n ∈X ↔(∃f 1)(Y (f, n) = 0)

.
Now, since uncountable index sets are ﬁrst-class citizens in the theory of nets,
we shall work in Kohlenbach’s higher-order RM (see Section 2.1). The exact for-
malisation of nets in higher-order RM is detailed in Deﬁnition 2.4 and Section 2.3.
In Sections 3.2.2 to 3.4.1, we restrict ourselves to nets indexed by subsets of Baire
space, i.e. part of third-order arithmetic, as such nets are already general enough to
obtain our main results in Figure 2. Our results for the monotone convergence the-
orem MCTC
net for nets in Cantor space indexed by subsets of Baire space, are neatly
summarised by Figure 3; the associated logical systems are deﬁned in Section 2.2.
strong









...
ZFC
ZC
simple type theory
ZΩ
2
Π1
k-CAω
0 + MCTC
net
medium



























Zω
2 + QF-AC0,1
...
Π1
k+1-CAω
0
...
Π1
2-CAω
0
Π1
1-CAω
0
ATRω
0
ACAω
0
Heine-Borel theorem
as in HBU, Dini’s
theorem for nets



weak











WKLω
0
RCAω
0
PRA
EFA
bounded arithmetic
Figure 3. The G¨odel hierarchy (based on inclusion and higher
types) with a parallel branch for the medium range
?
MCTC
net[↔BOOT]
-
?
Π1
k+1-CA0
















9
-

:

Y
b
b






) 
1
b
b
Of course, Figure 3 only provides one example and we shall obtain a number of
such parallel hierarchies in Section 3, based on the following theorems.
(i) The Bolzano-Weierstrass theorem for nets (Section 3.2).
(ii) The existence of moduli of convergence for nets (Section 3.2.2).


## Page 8


8
PLATO AND THE FOUNDATIONS OF MATHEMATICS
(iii) The Moore-Osgood theorem for nets (Section 3.3).
(iv) Numerous variations including the anti-Specker property and the Arzel`a
and Ascoli-Arzel`a theorems (Section 3.2) and Cauchy nets (Section 3.2.2).
We refer to the hierarchy formed by Π1
k-CAω
0 + MCTC
net for k ≥0 as the bootstrap
hierarchy as the logical strength (at least Π1
k+1-CA0) is ‘bootstrapped’ from two es-
sential parts, namely Π1
k-CAω
0 and MCTC
net that are weak(er) in isolation. To obtain
the aforementioned results, MCTC
net is shown to be equivalent to a new comprehen-
sion principle BOOT, and similar results for the other convergence theorems.
Next, we also study two ‘more general’ convergence theorems, respectively for
nets in function spaces and for nets involving index sets beyond Baire space. The
former theorem ‘bootstraps itself’, i.e. become stronger and stronger without the
need for additional comprehension, as discussed in Section 3.4.1. The latter theorem
carries us beyond second-order arithmetic, and shows that our proofs readily gen-
eralise to higher types. Nonetheless, results associated to index sets beyond Baire
space are still mapped into the lower regions of second-order arithmetic by ECF,
as discussed in Section 3.4.2. The results in the latter also provide an equivalence
BOOT1 ↔MCT1
net between two fourth-order principles; we deﬁne a lossy transla-
tion (but less lossy than ECF) that converts this equivalence into BOOT ↔MCTC
net,
i.e. an equivalence in third-order arithmetic. This (partially) answers a question
from the previous section, namely what the Plato hierarchy is a reﬂection of.
After some contemplation, one observes that BOOT and HBU cannot be cap-
tured (well or at all) in terms of the known comprehension axioms from [42,82] by
Figures 2 and 3. However, the main question of RM dictates that we ﬁnd a suitable
class of set existence axioms that capture BOOT and HBU.
To this end, we show in Section 5 that axioms from the Plato hierarchy are
equivalent to fragments of a continuity axiom from intuitionistic analysis called
special bar/Brouwer continuity SBC in [43] and neighbourhood function principle
NFP in [91]. Moreover, discontinuous functions are converted to ‘0 = 1’ by ECF,
while the Plato hierarchy does have rather meaningful translations under ECF. In
this light, Kohlenbach’s hierarchy from [42] is based on discontinuity and the Plato
hierarchy ‘by contrast’ has a natural formulation in terms of continuity.
Finally, a number of theorems in Figure 2 mentions open (and closed) sets. Open
sets are represented in RM by countable unions of open balls and it is a natural
question what the correct notion of open set in the Plato hierarchy is. As studied
in Section 4, uncountable unions of open balls are the correct notion (in contrast to
open sets represented by characteristic functions as in [64,74]), giving rise to nice
equivalences and the original RM-equivalences under ECF.
We shall study the Cantor-Bendixson theorem, the perfect set theorem, and
located sets. We wish to point out that ﬁnding the aforementioned correct notion
of open set is by no means obvious: we have previously studied (higher-order) open
sets represented by characteristic functions in [64, 74].
Interesting results were
deﬁnitely obtained (see Remark 4.1), but the concept of open set from [64,74] does
not seem to yield nice RM-equivalences try as one might.
It goes without saying that this paper constitutes a spin-oﬀfrom our joint project
with Dag Normann on the logical and computational properties of the uncountable.
The interested reader may consult [60] as an introduction.


## Page 9


PLATO AND THE FOUNDATIONS OF MATHEMATICS
9
2. Preliminaries
We introduce Reverse Mathematics in Section 2.1, as well as its generalisation to
higher-order arithmetic, and the associated base theory RCAω
0 . We introduce some
essential axioms in Section 2.2. We provide a brief introduction to nets and related
concepts in Section 2.3. As noted in Section 1.2, we mostly study nets indexed by
subsets of Baire space, i.e. part of third-order arithmetic; the associated bit of set
theory shall be represented in RCAω
0 as in Deﬁnition 2.4.
2.1. Reverse Mathematics. Reverse Mathematics is a program in the founda-
tions of mathematics initiated around 1975 by Friedman ([19, 20]) and developed
extensively by Simpson ([82]). The aim of RM is to identify the minimal axioms
needed to prove theorems of ordinary, i.e. non-set theoretical, mathematics.
We refer to [85] for a basic introduction to RM and to [81,82] for an overview of
RM. We expect basic familiarity with RM, but do sketch some aspects of Kohlen-
bach’s higher-order RM ([42]) essential to this paper, including the base theory
RCAω
0 (Deﬁnition 2.1). As will become clear, the latter is oﬃcially a type theory
but can accommodate (enough) set theory via Deﬁnition 2.4.
First of all, in contrast to ‘classical’ RM based on second-order arithmetic Z2,
higher-order RM uses Lω, the richer language of higher-order arithmetic. Indeed,
while the latter is restricted to natural numbers and sets of natural numbers, higher-
order arithmetic can accommodate sets of sets of natural numbers, sets of sets of sets
of natural numbers, et cetera. To formalise this idea, we introduce the collection of
all ﬁnite types T, deﬁned by the two clauses:
(i) 0 ∈T and (ii) If σ, τ ∈T then (σ →τ) ∈T,
where 0 is the type of natural numbers, and σ →τ is the type of mappings from
objects of type σ to objects of type τ. In this way, 1 ≡0 →0 is the type of functions
from numbers to numbers, and where n + 1 ≡n →0. Viewing sets as given by
characteristic functions, we note that Z2 only includes objects of type 0 and 1.
Secondly, the language Lω includes variables xρ, yρ, zρ, . . . of any ﬁnite type ρ ∈
T. Types may be omitted when they can be inferred from context. The constants
of Lω includes the type 0 objects 0, 1 and <0, +0, ×0, =0 which are intended to have
their usual meaning as operations on N. Equality at higher types is deﬁned in terms
of ‘=0’ as follows: for any objects xτ, yτ, we have
[x =τ y] ≡(∀zτ1
1 . . . zτk
k )[xz1 . . . zk =0 yz1 . . . zk],
(2.1)
if the type τ is composed as τ ≡(τ1 →. . . →τk →0). Furthermore, Lω also
includes the recursor constant Rσ for any σ ∈T, which allows for iteration on type
σ-objects as in the special case (2.2). Formulas and terms are deﬁned as usual.
One obtains the sub-language Ln+2 by restricting the above type formation rule to
produce only type n + 1 objects (and related types of similar complexity).
Deﬁnition 2.1. The base theory RCAω
0 consists of the following axioms.
(a) Basic axioms expressing that 0, 1, <0, +0, ×0 form an ordered semi-ring with
equality =0.
(b) Basic axioms deﬁning the well-known Π and Σ combinators (aka K and S
in [3]), which allow for the deﬁnition of λ-abstraction.
(c) The deﬁning axiom of the recursor constant R0: For m0 and f 1:
R0(f, m, 0) := m and R0(f, m, n + 1) := f(n, R0(f, m, n)).
(2.2)


## Page 10


10
PLATO AND THE FOUNDATIONS OF MATHEMATICS
(d) The axiom of extensionality: for all ρ, τ ∈T, we have:
(∀xρ, yρ, ϕρ→τ)

x =ρ y →ϕ(x) =τ ϕ(y)

.
(Eρ,τ)
(e) The induction axiom for quantiﬁer-free4 formulas of Lω.
(f) QF-AC1,0: The quantiﬁer-free Axiom of Choice as in Deﬁnition 2.2.
Deﬁnition 2.2. The axiom QF-AC consists of the following for all σ, τ ∈T:
(∀xσ)(∃yτ)A(x, y) →(∃Y σ→τ)(∀xσ)A(x, Y (x)),
(QF-ACσ,τ)
for any quantiﬁer-free formula A in the language of Lω.
We let IND be the induction axiom for all formulas in Lω. The system RCAω
0 +IND
has the same ﬁrst-order strength as Peano arithmetic.
As discussed in [42, §2], RCAω
0 and RCA0 prove the same sentences ‘up to lan-
guage’ as the latter is set-based and the former function-based. Recursion as in (2.2)
is called primitive recursion; the class of functionals obtained from Rρ for all ρ ∈T
is called G¨odel’s system T of all (higher-order) primitive recursive functionals.
We use the usual notations for natural, rational, and real numbers, and the
associated functions, as introduced in [42, p. 288-289].
Deﬁnition 2.3 (Real numbers and related notions in RCAω
0 ).
(a) Natural numbers correspond to type zero objects, and we use ‘n0’ and
‘n ∈N’ interchangeably. Rational numbers are deﬁned as signed quotients
of natural numbers, and ‘q ∈Q’ and ‘<Q’ have their usual meaning.
(b) Real numbers are coded by fast-converging Cauchy sequences q(·) : N →
Q, i.e. such that (∀n0, i0)(|qn −qn+i| <Q
1
2n ). We use Kohlenbach’s ‘hat
function’ from [42, p. 289] to guarantee that every q1 deﬁnes a real number.
(c) We write ‘x ∈R’ to express that x1 := (q1
(·)) represents a real as in the
previous item and write [x](k) := qk for the k-th approximation of x.
(d) Two reals x, y represented by q(·) and r(·) are equal, denoted x =R y, if
(∀n0)(|qn −rn| ≤2−n+1). Inequality ‘<R’ is deﬁned similarly. We some-
times omit the subscript ‘R’ if it is clear from context.
(e) Functions F : R →R are represented by Φ1→1 mapping equal reals to equal
reals, i.e. (∀x, y ∈R)(x =R y →Φ(x) =R Φ(y)).
(f) The relation ‘x ≤τ y’ is deﬁned as in (2.1) but with ‘≤0’ instead of ‘=0’.
Binary sequences are denoted ‘f 1, g1 ≤1 1’, but also ‘f, g ∈C’ or ‘f, g ∈2N’.
Elements of Baire space are given by f 1, g1, but also denoted ‘f, g ∈NN’.
(g) For a binary sequence f 1, the associated real in [0, 1] is r(f) := P∞
n=0
f(n)
2n+1 .
(h) Sets of type ρ objects Xρ→0, Y ρ→0, . . . are given by their characteristic
functions F ρ→0
X
≤ρ→0 1, i.e. we write ‘x ∈X’ for FX(x) =0 1.
The following special case of item (h) is singled out, as it will be used frequently.
Deﬁnition 2.4. [RCAω
0 ] A ‘subset D of NN’ is given by its characteristic function
F 2
D ≤2 1, i.e. we write ‘f ∈D’ for FD(f) = 1 for any f ∈NN. A ‘binary relation ⪯
on a subset D of NN’ is given by the associated characteristic function G(1×1)→0
⪯
,
i.e. we write ‘f ⪯g’ for G⪯(f, g) = 1 and any f, g ∈D. Assuming extensionality on
the reals as in item (e), we obtain characteristic functions that represent subsets of
4To be absolutely clear, variables (of any ﬁnite type) are allowed in quantiﬁer-free formulas of
the language Lω: only quantiﬁers are banned.


## Page 11


PLATO AND THE FOUNDATIONS OF MATHEMATICS
11
R and relations thereon. Using pairing functions, it is clear we can also represent
sets of ﬁnite sequences (of reals), and relations thereon.
Next, we mention the highly useful ECF-interpretation.
Remark 2.5 (The ECF-interpretation). The (rather) technical deﬁnition of ECF
may be found in [89, p. 138, §2.6]. Intuitively, the ECF-interpretation [A]ECF of a
formula A ∈Lω is just A with all variables of type two and higher replaced by count-
able representations of continuous functionals. Such representations are also (equiv-
alently) called ‘associates’ or ‘RM-codes’ (see [41, §4]).
The ECF-interpretation
connects RCAω
0 and RCA0 (see [42, Prop. 3.1]) in that if RCAω
0 proves A, then RCA0
proves [A]ECF, again ‘up to language’, as RCA0 is formulated using sets, and [A]ECF
is formulated using types, namely only using type zero and one objects.
In light of the widespread use of codes in RM and the common practise of iden-
tifying codes with the objects being coded, it is no exaggeration to refer to ECF as
the canonical embedding of higher-order into second-order RM. For completeness,
we also list the following notational convention for ﬁnite sequences.
Notation 2.6 (Finite sequences). We assume a dedicated type for ‘ﬁnite sequences
of objects of type ρ’, namely ρ∗. Since the usual coding of pairs of numbers goes
through in RCAω
0 , we shall not always distinguish between 0 and 0∗. Similarly, we
do not always distinguish between ‘sρ’ and ‘⟨sρ⟩’, where the former is ‘the object
s of type ρ’, and the latter is ‘the sequence of type ρ∗with only element sρ’. The
empty sequence for the type ρ∗is denoted by ‘⟨⟩ρ’, usually with the typing omitted.
Furthermore, we denote by ‘|s| = n’ the length of the ﬁnite sequence sρ∗=
⟨sρ
0, sρ
1, . . . , sρ
n−1⟩, where |⟨⟩| = 0, i.e. the empty sequence has length zero.
For
sequences sρ∗, tρ∗, we denote by ‘s∗t’ the concatenation of s and t, i.e. (s∗t)(i) = s(i)
for i < |s| and (s∗t)(j) = t(|s|−j) for |s| ≤j < |s|+|t|. For a sequence sρ∗, we deﬁne
sN := ⟨s(0), s(1), . . . , s(N −1)⟩for N 0 < |s|. For a sequence α0→ρ, we also write
αN = ⟨α(0), α(1), . . . , α(N−1)⟩for any N 0. By way of shorthand, (∀qρ ∈Qρ∗)A(q)
abbreviates (∀i0 < |Q|)A(Q(i)), which is (equivalent to) quantiﬁer-free if A is.
2.2. Some axioms of higher-order RM. We introduce some functionals which
constitute the counterparts of second-order arithmetic Z2, and some of the Big Five
systems, in higher-order RM. We use the formulation from [42,60].
First of all, ACA0 is readily derived from:
(∃µ2)(∀f 1)

(∃n)(f(n) = 0) →[(f(µ(f)) = 0) ∧(∀i < µ(f))f(i) ̸= 0]
(µ2)
∧[(∀n)(f(n) ̸= 0) →µ(f) = 0]

,
and ACAω
0 ≡RCAω
0 +(µ2) proves the same sentences as ACA0 by [36, Theorem 2.5].
The (unique) functional µ2 in (µ2) is also called Feferman’s µ ([3]), and is clearly
discontinuous at f =1 11 . . . ; in fact, (µ2) is equivalent to the existence of F : R →R
such that F(x) = 1 if x >R 0, and 0 otherwise ([42, §3]), and to
(∃ϕ2 ≤2 1)(∀f 1)

(∃n)(f(n) = 0) ↔ϕ(f) = 0

.
(∃2)
Secondly, Π1
1-CA0 is readily derived from the following sentence:
(∃S2 ≤2 1)(∀f 1)

(∃g1)(∀n0)(f(gn) = 0) ↔S(f) = 0

,
(S2)
and Π1
1-CAω
0 ≡RCAω
0 + (S2) proves the same Π1
3-sentences as Π1
1-CA0 by [70, The-
orem 2.2]. The (unique) functional S2 in (S2) is also called the Suslin functional


## Page 12


12
PLATO AND THE FOUNDATIONS OF MATHEMATICS
([42]). By deﬁnition, the Suslin functional S2 can decide whether a Σ1
1-formula as in
the left-hand side of (S2) is true or false. We similarly deﬁne the functional S2
k which
decides the truth or falsity of Σ1
k-formulas; we also deﬁne the system Π1
k-CAω
0 as
RCAω
0 +(S2
k), where (S2
k) expresses that S2
k exists. Note that we allow formulas with
function parameters, but not functionals here. In fact, Gandy’s Superjump ([22])
constitutes a way of extending Π1
1-CAω
0 to parameters of type two. We identify the
functionals ∃2 and S2
0 and the systems ACAω
0 and Π1
k-CAω
0 for k = 0.
Thirdly, full second-order arithmetic Z2 is readily derived from ∪kΠ1
k-CAω
0 , or from:
(∃E3 ≤3 1)(∀Y 2)

(∃f 1)Y (f) = 0 ↔E(Y ) = 0

,
(∃3)
and we therefore deﬁne ZΩ
2 ≡RCAω
0 + (∃3) and Zω
2 ≡∪kΠ1
k-CAω
0 , which are con-
servative over Z2 by [36, Cor. 2.6]. Despite this close connection, Zω
2 and ZΩ
2 can
behave quite diﬀerently, as discussed in e.g. [60, §2.2]. The functional from (∃3) is
also called ‘∃3’, and we use the same convention for other functionals.
Finally, the Heine-Borel theorem states the existence of a ﬁnite sub-cover for
an open cover of certain spaces. Now, a functional Ψ : R →R+ gives rise to the
canonical cover ∪x∈IIΨ
x for I ≡[0, 1], where IΨ
x is the open interval (x −Ψ(x), x +
Ψ(x)). Hence, the uncountable cover ∪x∈IIΨ
x has a ﬁnite sub-cover by the Heine-
Borel theorem; in symbols:
(∀Ψ : R →R+)(∃y1, . . . , yk ∈I)(∀x ∈I)(∃i ≤k)(x ∈IΨ
yi).
(HBU)
Note that HBU is almost verbatim Cousin’s lemma (see [17, p. 22]), i.e. the Heine-
Borel theorem restricted to canonical covers. The latter restriction does not make
much of a big diﬀerence, as studied in [71]. By [60,63], ZΩ
2 proves HBU but Zω
2 +
QF-AC0,1 cannot, and many basic properties of the gauge integral ([54, 86]) are
equivalent to HBU. Although strictly speaking incorrect, we sometimes use set-
theoretic notation, like reference to the cover ∪x∈IIΨ
x inside RCAω
0 , to make proofs
more understandable.
Such reference can in principle be removed in favour of
formulas of higher-order arithmetic.
2.3. An introduction to nets. We introduce the notion of net and associated
concepts. We ﬁrst consider the following standard deﬁnition from [39, Ch. 2].
Deﬁnition 2.7. [Nets] A set D ̸= ∅with a binary relation ‘⪯’ is directed if
(a) The relation ⪯is transitive, i.e. (∀x, y, z ∈D)([x ⪯y ∧y ⪯z] →x ⪯z).
(b) For x, y ∈D, there is z ∈D such that x ⪯z ∧y ⪯z.
(c) The relation ⪯is reﬂexive, i.e. (∀x ∈D)(x ⪯x).
For such (D, ⪯) and topological space X, any mapping x : D →X is a net in X.
We denote λd.x(d) as ‘xd’ or ‘xd : D →X’ to suggest the connection to sequences.
The directed set (D, ⪯) is not always explicitly mentioned together with a net xd.
Except for Section 3.4.2, we only use directed sets that are subsets of Baire space,
i.e. as given by Deﬁnition 2.4. Similarly, we only study nets xd : D →R where D
is a subset of Baire space. Thus, a net xd in R is just a type 1 →1 functional with
extra structure on its domain D provided by ‘⪯’ as in Deﬁnition 2.4, i.e. part of
third-order arithmetic.
The deﬁnitions of convergence and increasing net are of course familiar.


## Page 13


PLATO AND THE FOUNDATIONS OF MATHEMATICS
13
Deﬁnition 2.8. [Convergence of nets] If xd is a net in X, we say that xd converges
to the limit limd xd = y ∈X if for every neighbourhood U of y, there is d0 ∈D
such that for all e ⪰d0, xe ∈U.
Deﬁnition 2.9. [Increasing nets] A net xd : D →R is increasing if a ⪯b implies
xa ≤R xb for all a, b ∈D.
Deﬁnition 2.10. A point x ∈X is a cluster point for a net xd in X if every
neighbourhood U of x contains xu for some u ∈D.
The previous deﬁnition yields the following nice equivalence: a toplogical space
is compact if and only if every net therein has a cluster point ([4, Prop. 3.4]). All
the below results can be formulated using cluster points only, but such an approach
does not address the question what the counterpart of ‘sub-sequence’ for nets is.
Indeed, an obvious next step following Deﬁnition 2.10 is to take smaller and smaller
neighbourhoods around the cluster point x and (somehow) say that the associated
points xu net-converge to x. To this end, we consider the following deﬁnition, ﬁrst
introduced by Moore in [53], and used by Kelley in [39]. Alternative deﬁnitions
involve extra requirements (see [78, §7.14]), i.e. our deﬁnition is the weakest.
Deﬁnition 2.11. [Sub-nets] A sub-net of a net xd with directed set (D, ⪯D), is a
net yb with directed set (B, ⪯B) such that there is a function φ : B →D such that:
(a) the function φ satisﬁes yb = xφ(b),
(b) (∀d ∈D)(∃b0 ∈B)(∀b ⪰B b0)(φ(b) ⪰D d).
We point out that the distinction between ‘⪯B’ and ‘⪯D’ is not always made in
the literature (see e.g. [4,39]).
Finally, we need to discuss the connection between nets and sequences.
Remark 2.12 (Nets and sequences). First of all, N with its usual ordering yields
a directed set, i.e. convergence results about nets do apply to sequences. Of course,
a sub-net of a sequence is not necessarily a sub-sequence, i.e. some care is advisable
in these matters. Nonetheless, the Bolzano-Weierstrass theorem for nets does for
instance imply the monotone convergence theorem for sequences (see [74, §3.1.1]).
Secondly, the Bolzano-Weierstrass (or monotone convergence) theorem for count-
able (or continuous on Baire space) nets can be formulated in the language of
second-order arithmetic and constitutes a trivial extension of the original. Follow-
ing Remark 1.1, we do not distinguish between them.
On a historical note, Vietoris introduces the notion of oriented set in [93, p. 184],
which is exactly the notion of ‘directed set’. He proceeds to prove (among others)
a version of the Bolzano-Weierstrass theorem for nets. Vietoris also explains that
these results are part of his dissertation, written in the period 1913-1919, i.e. during
his army service for the Great War.
3. Main results I: convergence of nets
We introduce the axiom BOOT and related notions in Section 3.1.
In Sec-
tions 3.2-3.3, we establish equivalences involving basic convergence theorems for
nets and BOOT, as laid out in Section 1.3. We point out Section 3.2.3 in which
we re-obtain some of these implications by ‘lifting’ well-known second-order re-
sults to higher-order arithmetic. The aforementioned results deal with nets in the
unit interval and indexed by Baire space. In Section 3.4, we show that interesting
phenomena occur when either of these restrictions is lifted.


## Page 14


14
PLATO AND THE FOUNDATIONS OF MATHEMATICS
3.1. Introduction: the bootstrap hierarchy. The results in [72–74] establish
that basic convergence theorems for nets are extremely hard to prove, while the
limits therein are similarly hard to compute. In this paper, we show that the ﬁrst-
order strength of such theorems can also ‘explode’, i.e. increase dramatically when
combined with certain comprehension axioms. These results in turn give rise to
the hierarchy described in Section 1.3. To this end, we show in the next sections
that various convergence theorems for nets imply, or are even equivalent to, the
following higher-order comprehension axiom.
Deﬁnition 3.1. [BOOT] (∀Y 2)(∃X1)(∀n0)

n ∈X ↔(∃f 1)(Y (f, n) = 0)

.
The formula in the right-hand side of BOOT is called a ‘Σ-formula’. The name
‘BOOT’ derives from the word ‘bootstrap’. We refer to the hierarchy formed by
Π1
k-CAω
0 + BOOT as the bootstrap hierarchy as the logical strength of the latter
system (in casu at least Π1
k+1-CA0) is ‘bootstrapped’ from two essential parts,
namely Π1
k-CAω
0 and BOOT that are weak(er) in isolation.
Theorem 3.2. The system Π1
k-CAω
0 +BOOT proves Π1
k+1-CA0. The system RCAω
0 +
BOOT proves the same second-order sentences as ACA0. Moreover, RCA0 proves
ACA0 ↔[BOOT]ECF.
Proof. For the ﬁrst part, a Π1
k+1-formula from L2 is clearly equivalent to a formula
of the form (∀f 1)(Y (f, n) = 0) given S2
k.
For the second part, RCAω
0 + BOOT
readily proves ACA0, while the ECF-translation establishes that BOOT proves the
same second-order sentences as ACA0.
Indeed, as discussed in Remark 2.5, the
ECF-translation replaces the functional Y 2 in BOOT by a total associate α1, i.e.
the right-hand side of [BOOT]ECF is thus (∃f 1)(∃m0)(α(fm, n) = 1). Given ACA0,
there is clearly a set X that collects all n satisfying this formula.
□
The previous theorem is hardly surprising given the form of BOOT. By contrast,
the equivalence between BOOT and the monotone convergence theorem MCTC
net for
nets in Cantor space indexed by Baire space from Section 3.2 is rather surprising, in
our opinion. Moreover, the addition of moduli of convergence for nets gives rise to
an equivalence involving BOOT and countable choice in Section 3.2.2. The Moore-
Osgood theorem for nets is shown to exhibit similar behaviour in Section 3.3. By
Theorem 3.2, these convergence theorems give rise to the ‘bootstrap hierarchy’ and
variations. We note in passing that the usual ‘excluded middle’ trick yields the cute
disjunction ACA0 ↔[BOOT ∨(∃2)], which is converted into a tautology by ECF.
Following Remark 1.1, ECF maps equivalences like MCT[0,1]
net
↔BOOT, to well-
known RM-equivalences, like the equivalence between arithmetical comprehension
and the monotone convergence theorem for sequences ([82, III.2]). We stress that
the ECF-translation is the canonical embedding of higher-order into second-order
arithmetic, replacing as it does higher-order objects by the codes typical of the
practise of RM and second-order arithmetic. In the other direction, Theorems 3.19
and 3.31 show that certain second-order proofs, namely involving Specker sequences,
almost verbatim translate to proofs of MCT[0,1]
net
→BOOT and generalisations. The
latter proofs are however not ‘optimal’ as they use a non-trivial extension of RCAω
0 .
Finally, we study two ‘more complicated’ convergence theorems: for nets in the
function space [0, 1] →[0, 1] (Section 3.4.1) and for nets with index sets beyond
Baire space (Section 3.4.2). Section 3.4.1 is interesting as we obtain a convergence


## Page 15


PLATO AND THE FOUNDATIONS OF MATHEMATICS
15
theorem for nets in functions spaces -still in the language of third-order arithmetic-
that ‘bootstraps itself’, i.e. does not need additional comprehension axioms (like S2
k
or even ∃2) to become stronger and stronger. Section 3.4.2 shows that our proofs
easily generalise to higher types, while the general case is perhaps best treated in
a set-theoretic framework. Moreover, Section 3.4.2 provides (partial) answers to
the questions: What is the Plato hierarchy a reﬂection of? What is the nature
of this reﬂection?
Indeed, we provide a translation that yields the equivalence
MCTC
net ↔BOOT from a similar equivalence MCT1
net ↔BOOT1 involving index
sets beyond Baire space.
We ﬁnish this section with some historical remarks pertaining to BOOT.
Remark 3.3 (Historical notes). First of all, the bootstrap principle BOOT is de-
ﬁnable in Hilbert-Bernays’ system H from the Grundlagen der Mathematik; see
[34, Supplement IV]. In particular, the functional ν from [34, p. 479] immediately5
yields the set X from BOOT, viewing the type two functional Y 2 as a parameter;
the use of ‘unspoken higher-order parameters’ is common throughout [34, Supple-
ment IV]. Thus, the Plato and G¨odel hierarchies have the same historical roots.
Secondly, Feferman’s axiom (Proj1) from [18] is similar to BOOT. The former is
however formulated using sets, which makes it more ‘explosive’ than BOOT in that
full Z2 follows when combined with (µ2), as noted in [18, I-12]. The axiom (Proj1)
only became known to us after the results in this section were ﬁnished.
3.2. Convergence theorems for nets. We show that a number of convergence
theorems for nets gives rise to Π1
k+1-CA0 in combination with Π1
k-CAω
0 . This is done
by establishing the connection between these theorems and BOOT.
3.2.1. Bolzano-Weierstrass and related theorems. In this section, we study the Bolzano-
Weierstrass theorem for nets and related theorems.
Deﬁnition 3.4. [BWC
net] A net in Cantor space indexed by a subset of Baire space
has a convergent sub-net.
Theorem 3.5. The system ACAω
0 + BWC
net proves Π1
1-CA0.
Proof. A Σ1
1-formula ϕ(n) ∈L2 is readily seen to be equivalent to a formula
(∃g1)(Y (g, n) = 0) for Y 2 deﬁned in terms of ∃2. Let D be the set of ﬁnite se-
quences in Baire space and let ⪯D be the inclusion ordering, i.e. w ⪯D v if (∀i <
|w|)(∃j < |v|)(w(i) =1 v(j)). Now deﬁne the net fw : D →C as fw := λk.F(w, k)
where F(w, k) is 1 if (∃i < |w|)(Y (w(i), k) = 0), and zero otherwise. Using BWC
net,
let φ : B →D be such that limb fφ(b) = f. We now establish this equivalence:
(∀n0)

(∃g1)(Y (g, n) = 0) ↔f(n) = 1

.
(3.1)
For the reverse direction, note that for ﬁxed n0, if Y (g, n0) > 0 for all g1, then
fw(n0) = 0 for any w ∈D. The deﬁnition of limit then implies f(n0) = 0, i.e.
we have established (the contraposition of) the reverse direction. For the forward
direction in (3.1), suppose there is some n0 such that (∃g1)(Y (g, n0) = 0)∧f(n0) =
0. Now, limb fφ(b) = f implies that there is b0 ∈B such that for b ⪰B b0, we have
fφ(b)n0 = fn0, i.e. fφ(b)(n0) = 0 for b ⪰B b0. Let g1
0 be such that Y (g0, n0) = 0,
5The functional ν from [34, p. 479] is such that if (∃f1)A(f), the function (νf)A(f) is the
lexicographically least such f1. The formula A may contain type two parameters, as is clear from
e.g. [34, p. 481] and other deﬁnitions.


## Page 16


16
PLATO AND THE FOUNDATIONS OF MATHEMATICS
and use the second item in Deﬁnition 2.11 for d = ⟨g0⟩, i.e. there is b1 ∈B such
that φ(b) ⪰D ⟨g0⟩for any b ⪰B b1. Now let b2 ∈B be such that b2 ⪰B b0, b1 as
provided by Deﬁnition 2.7. On one hand, b2 ⪰B b1 implies that φ(b2) ⪰D ⟨g0⟩, and
hence fφ(b2)(n0) = F(φ(b2), n0) = 1, as g0 is in the ﬁnite sequence φ(b2) by the
deﬁnition of ⪯D. On the other land, b2 ⪰b0 implies that fφ(b2)(n0) = f(n0) = 0, a
contradiction. Hence, (3.1) follows, yielding {n : ϕ(n)}, as required by Π1
1-CA0.
□
The previous theorem is elegant, but hides an important result involving the
monotone convergence theorem for nets. As to its provenance, the latter theorem
can be found in e.g. [12, p. 103], but is also implicit in domain theory ([23, 24]).
Indeed, the main objects of study of domain theory are dcpos, i.e. directed-complete
posets, and an increasing net converges to its supremum in a dcpo.
Deﬁnition 3.6. [MCTC
net] Any increasing net in C indexed by a subset of NN
converges in C.
Note that we use the lexicographic ordering ≤lex on C in the previous deﬁnition,
i.e. f ≤lex g if either f =1 g or there is n0 such that fn = gn and f(n+1) < g(n+1).
Theorem 3.7. The system RCAω
0 proves that MCTC
net ↔BOOT.
Proof. We ﬁrst prove the equivalence assuming (∃2). For the forward direction, ﬁx
some Y 2 and consider fw from the proof of the theorem. Note that v ⪯D w →
fv ≤lex fw, i.e. this net is indeed increasing. Let f = limw fw be the limit provided
by MCTC
net and verify that (3.1) also holds in this case. In this way, we obtain the
equivalence required by BOOT. Note that ∃2 is necessary for deﬁning ‘⪯D’.
For the reverse direction, let xd : D →C be an increasing net in C and consider
the formula (∃d ∈D)(xd ≥lex σ ∗00 . . . ), where σ0∗is a ﬁnite binary sequence. The
latter formula is equivalent to a formula of the form (∃g1)(Y (g, n) = 0) where Y 2
is deﬁned in terms of ∃2 and n codes a ﬁnite binary sequence. To deﬁne the limit
f required by MCTC
net, f(0) is 1 if (∃d ∈D)(xd ≥lex 100 . . . ) and zero otherwise.
One then deﬁnes f(n + 1) in terms of fn in the same way, yielding the equivalence
MCTC
net ↔BOOT given (∃2).
Next, we establish the theorem assuming ¬(∃2), which implies that all func-
tionals on Baire space are continuous (see [42, §3]). In this light, BOOT reduces
to (essentially) ACA0 by the proof of Theorem 3.2. Similarly, any formula involv-
ing a type one quantiﬁer (∃d ∈D)(. . . xd . . . ) may be equivalently replaced by
(∃σ0∗)(σ ∗00 · · · ∈D ∧. . . xσ∗00... . . . ), which now involves a type zero quantiﬁer
(modulo coding). Thus, MCTC
net also reduces to (essentially) the monotone conver-
gence theorem for sequences, and the latter is equivalent to ACA0 by [82, III.2].
Hence, we have proved the theorem in both cases and the law of excluded middle
(∃2) ∨¬(∃2) ﬁnishes the proof.
□
We can formulate the previous theorem in terms of classical computability theory
as follows; let ‘≤T ’ be the usual Turing reducibility relation and let J(Y ) be the
set {n : (∃f 1)(Y (f, n) = 0)}. The forward direction of Theorem 3.7 becomes:
for any Y 2, there is a net xd : D →I such that x = limd xd →J(Y ) ≤T x.
Note that the net xd can be deﬁned in terms of Y 2 via a term of G¨odel’s T.
Moreover, ECF converts this statement into actual classical computability theory.


## Page 17


PLATO AND THE FOUNDATIONS OF MATHEMATICS
17
Let MCTC
seq be the monotone convergence theorem for sequences in C, which is
equivalent to ACA0 by [82, III.2]. The ECF-translation converts MCTC
net ↔BOOT
into MCTC
seq ↔ACA0 following Remark 1.1. Indeed, if a net xd is continuous in
d, then (∃d ∈D)(xd > y) is equivalent to a Σ0
1-formula and the ‘usual’ interval
halving proof goes through for [MCTC
net]ECF given ACA0.
Corollary 3.8. The systems Π1
k-CAω
0 +BWC
net and Π1
k-CAω
0 +MCTC
net prove Π1
k+1-CA0
(k ≥0). The system ZΩ
2 proves MCTC
net.
Proof. By Theorem 3.2 and the fact that (∃3) trivially proves BOOT.
□
By the second part of the corollary, the power, strength, and hardness of MCTC
net
have nothing to do with the Axiom of Choice. We actually study the connection
between the latter and the convergence of nets in Section 3.2.2.
Of course, there is nothing special about Cantor space in the previous results.
Let BW[0,1]
net
and MCT[0,1]
net
be respectively the Bolzano-Weierstrass and monotone
convergence theorem for nets in the unit interval indexed by subsets of Baire space.
Corollary 3.9. The system RCAω
0 + IND + X proves BOOT, for X equal to either
BW[0,1]
net
or MCT[0,1]
net .
Proof. It is well-known that ∃2 deﬁnes a functional η1→1 that converts real numbers
in [0, 1] into binary representation, choosing a tail of zeros whenever there are two
possibilities. Now consider the following alternative version of (3.1):
(∀n0)

(∃g1)(Y (g, n) = 0) ↔η(x)(n) = 1

,
(3.2)
where x is the limit provided by BW[0,1]
net for the sub-net of the net xw := r(λk.F(w, k)).
Note that (3.2) only holds in case x has a unique binary representation. In the case
of non-unique binary representation of x, there is n0 such that (∃g1)(Y (g, n) = 0 has
the same truth value for n ≥n0. Now use IND to establish that for every m0 ≥1,
there is w0 of length m such that (∀i < m)

(∃g1)(Y (f, i) = 0) →Y (w(i), i) = 0

.
Hence, the ‘non-unique’ case has been handled too. Finally, the net xw is increasing
(in the sense of ≤R), i.e. MCT[0,1]
net
also establishes the corollary.
□
The anti-Specker property for nets, denoted ASnet, is studied in [74, §3.1.3]. Now,
ASnet essentially expresses that if a net converges to an isolated point, it is eventually
constant. Since ASnet readily implies MCT[0,1]
net
using classical logic, the former also
implies BOOT by the previous corollary. The same holds for the Arzel`a and Ascoli-
Arzel`a theorems for nets studied in [74, §3.2.2]. As it turns out, the index sets used
in this section, essentially consisting of ﬁnite sets ordered by inclusion, are called
phalanxes by Tukey ([92]), a martial term that has not caught on.
3.2.2. Moduli of convergence. In this section, we study the additional power pro-
vided by modulus functions for convergence theorems pertaining to nets. We ﬁrst
discuss our motivation for this study.
First of all, given an ‘epsilon-delta’ deﬁnition, a modulus is a functional that
provides the ‘delta’ in terms of the ‘epsilon’ and other data. Bolzano already made
use of moduli of continuity (see [69]), while they are implicit in RM-codes for
continuous functions by [41, Prop. 4.4]. E.H. Moore also suggests using moduli in
[51, p. 632] in the context of ‘general limits’, a predecessor to nets and [52]. In
the case of convergent sequences in the unit interval, the existence of a modulus


## Page 18


18
PLATO AND THE FOUNDATIONS OF MATHEMATICS
is readily provable in ACA0; thus the extra information provided by a modulus (or
rate) of convergence does not change the associated RM-results for convergence
theorems as in [82, III.2]. By contrast, we show that enriching some of the above
theorems with a modulus gives rise to an equivalence involving countable choice.
Secondly, we need the notion of Cauchy net (see e.g. [39, p. 190]), deﬁned as
follows for R. It goes without saying that such nets are the generalisation of the
notion of Cauchy sequence to directed sets.
Deﬁnition 3.10. [Cauchy net] A net xd : D →R is Cauchy if (∀ε > 0)(∃d ∈
D)(∀e, f ⪰D d)(|xe −xf| < ε).
Deﬁnition 3.11. [Cauchy modulus] A net xd : D →R is Cauchy with a modulus
if there is Φ : R →D such that (∀ε > 0)(∀e, f ⪰D Φ(ε))(|xe −xf| < ε).
On one hand, the convergence of Cauchy sequences in the unit interval is equiv-
alent to ACA0 by [82, III.2.2], i.e. we expect the generalisation to Cauchy nets
to exhibit similar behaviour to MCT[0,1]
net
One the other hand, MCT[0,1]
net
obviously
follows from the two following facts:
(i) An increasing net in [0, 1] indexed by a subset of NN is Cauchy.
(ii) A Cauchy net in [0, 1] indexed by a subset of NN converges.
One readily shows that item (ii) gives rise to hierarchies as in Corollary 3.9, while
item (i) is provable in RCAω
0 + IND. Item (i) is therefore quite weak and we shall
enrich it with a Cauchy modulus, as follows.
Deﬁnition 3.12. [CAUmod] An increasing net in [0, 1] is Cauchy with a modulus.
Theorem 3.13. The system ACAω
0 + CAUmod proves Π1
1-CA0.
Proof. A Σ1
1-formula ϕ(n) ∈L2 is readily seen to be equivalent to a formula
(∃f 1)(Y (f, n) = 0) for Y 2 deﬁned in terms of ∃2.
Let D be the set of ﬁnite
sequences in Baire space and let ⪯D be the inclusion ordering, i.e. w ⪯D v if
(∀i < |w|)(∃j < |v|)(w(i) =1 v(j)). Now deﬁne the net xw : D →R as xw :=
r(λk.F(w, k)) where F(w, k) is 1 if (∃i < |w|)(Y (w(i), k) = 0), and zero other-
wise.
Note that xw is increasing by deﬁnition.
Let Φ : N →D be such that
(∀k0)(∀w, v ⪰D Φ(k))(|xw −xv| <
1
2k ). We now establish this equivalence:
(∀n0)

(∃f 1)(Y (f, n) = 0) ↔(∃g1 ∈Φ(n))(Y (g, n) = 0)

.
(3.3)
The reverse direction in (3.3) is trivial. For the forward direction, suppose there
is some n0 such that (∃f 1)(Y (f, n0) = 0) ∧(∀g1 ∈Φ(n0))(Y (g, n0) > 0). Let f 1
0
be such that Y (f0, n0) = 0, implying F(Φ(n0), n0) = 0 and F(w0, n0) = 1 for
w0 := Φ(n0) ∗⟨f0⟩. Hence |xΦ(n0) −xw0| ≥
1
2n0 and w0 ⪰D Φ(n0), a contradiction.
Thus, (3.3) holds and yields the set {n : ϕ(n)}, as required by Π1
1-CA0.
□
The proof of the theorem also yields a nice splitting as follows.
Corollary 3.14. The system RCAω
0 proves CAUmod ↔[BOOT + QF-AC0,1].
Proof. For the reverse implication, the proof of Theorem 3.7 yields BOOT →
MCT[0,1]
net
with minimal adaptation. Let xd : D →[0, 1] be an increasing net and let
x ∈[0, 1] be the limit provided by MCT[0,1]
net . Now apply QF-AC0,1 to the formula
(∀k0)(∃d ∈D)(|xd −x| <
1
2k ) and note that the resulting functional is a Cauchy
modulus since xd is an increasing net.


## Page 19


PLATO AND THE FOUNDATIONS OF MATHEMATICS
19
For the forward implication, we again use (∃2)∨¬(∃2). In case ¬(∃2), all functions
on Baire space are continuous by [42, §3]. In this case, QF-AC0,1 is immediate from
QF-AC0,0 (included in RCAω
0 ) and BOOT reduces to ACA0 as noted in the proof
of Theorem 3.7. In case of (∃2), the proof of the theorem yields (3.3); BOOT and
QF-AC0,1 are now immediate as the right-hand side of (3.3) is decidable.
□
The deﬁnition of a ‘modulus of net convergence’ is now obvious following Deﬁni-
tion 3.11. Let MCT[0,1]
mod and BW[0,1]
mod be resp. MCT[0,1]
net
and BW[0,1]
net
with the addition
of a modulus of convergence.
Corollary 3.15. The system ACAω
0 + BW[0,1]
mod proves BOOT + QF-AC0,1.
Proof. Immediate by the proof of the theorem and the observation that for an
increasing net, a modulus of convergence of a sub-net is also a Cauchy modulus for
the (original) net.
□
Corollary 3.16. The system RCAω
0 proves MCT[0,1]
mod ↔[BOOT + QF-AC0,1].
Proof. By Theorem 3.7 and Corollary 3.14.
□
A similar result can now be obtained for the Arzel`a and Ascoli-Arzel`a theorems
for nets studied in [74, §3.2.2]. Moreover, to derive BW[0,1]
net
from item (ii) at the
beginning of this section, one requires COHnet, i.e. the statement any net in the
unit interval contains a Cauchy sub-net. The associated property for sequences is
equivalent to COH from the RM zoo (see [44]). Clearly, COHnet upgraded with a
modulus would also give rise to e.g. a version of Corollary 3.15.
3.2.3. Lifting second-order results. We have obtained the equivalence MCT[0,1]
net
↔
BOOT in Section 3.2.1. In this section, we show that the forward implication can
also be obtained by ‘lifting’ the second-order proof of MCT[0,1]
seq
→ACA0 to higher-
order arithmetic; MCT[0,1]
seq
is the monotone convergence theorem for sequences. On
one hand, this result suggest that second-order and higher-order arithmetic are
not as fundamentally diﬀerent as often claimed (the author is guilty of some such
claims).
On the other hand, the ‘lifted’ proofs are not optimal as they need a
non-trivial extension of the base theory.
First of all, the crux of numerous reversals T →ACA0 is that the theorem T
(somehow) allows for the reduction of (certain) Σ0
1-formulas to ∆0
1-formulas. Since
∆0
1-comprehension is included in RCA0, one then obtains Σ0
1-comprehension or the
existence of the range of arbitrary functions, and ACA0 follows. We now show that
this technique elegantly extends to BOOT, which in turn allows us to lift proofs
from the second-order to the higher-order framework with minimal adaptation.
Secondly, ACA0 is equivalent to range, i.e. the existence of the range of any one-
to-one f : N →N, by [82, III.1.3]; BOOT satisﬁes a similar equivalence involving
the existence of the range of any type two functional, as follows.
Theorem 3.17. The system RCAω
0 proves that BOOT is equivalent to
(∀G2)(∃X1)(∀n0)

n ∈X ↔(∃f 1)(G(f) = n)].
(RANGE)
Proof. The forward direction is immediate. For the reverse direction, deﬁne G2 as
follows for n0 and g1: put G(⟨n⟩∗g) = n + 1 if Y (g, n) = 0, and 0 otherwise. Let
X ⊆N be as in RANGE and note that
(∀m0 ≥1)(m ∈X ↔(∃f 1)(G(f) = m) ↔(∃g1)(Y (g, m −1) = 0)).


## Page 20


20
PLATO AND THE FOUNDATIONS OF MATHEMATICS
which is as required for BOOT after trivial modiﬁcation.
□
It goes without saying that [RANGE]ECF is essentially range, i.e. the existence of
the range of any one-to-one f : N →N, following Remark 1.1.
Thirdly, our base theory plus countable choice proves the following higher-order
version of ∆0
1-comprehension, by Theorem 3.18.
(∀Y 2, Z2)

(∀n0)((∃f 1)(Y (f, n) = 0) ↔(∀g1)(Z(g, n) = 0))
(∆-comprehension)
→(∃X1)(∀n0)(n ∈X ↔(∃f 1)(Y (f, n) = 0)

Note that the ECF-translation converts ∆-comprehension into ∆0
1-comprehension,
while QF-AC0,1 becomes QF-AC0,0, following Remark 1.1. As shown in [65], ∆-
comprehension is perhaps the weakest comprehension principle that still implies
that there is no bijection from [0, 1] to N (using the usual deﬁnition from set theory).
Theorem 3.18. The system RCAω
0 + QF-AC0,1 proves ∆-comprehension.
Proof. The antecedent of ∆-comprehension implies the following
(∀n0)(∃g1, f 1)(Z(g, n) = 0 →Y (f, n) = 0).
(3.4)
Applying QF-AC0,1 to (3.4) yields Φ0→1 such that
(∀n0)
 (∀g1)(Z(g, n) = 0) →Y (Φ(n), n) = 0

,
(3.5)
and by assumption an equivalence holds in (3.5), and we are done.
□
The previous theorem demonstrates its importance in the following proof. In-
deed, the very ﬁrst reversal in Simpson’s monograph can be found in [82, III.2.2],
which is the implication MCT[0,1]
seq
→ACA0 via an intermediate step involving range;
the (second part of the) following proof is exactly Simpson’s proof of MCT[0,1]
seq
→
range, save for the replacement of sequences by nets.
Theorem 3.19. The system RCAω
0 + QF-AC0,1 proves MCT[0,1]
net
→BOOT.
Proof. In case ¬(∃2), note that MCT[0,1]
net
also implies MCT[0,1]
seq
as sequences are nets
with directed set (N, ≤N). By [82, III.2], ACA0 is available, which readily implies
BOOT for continuous Y 2, but all functions on Baire space are continuous by [42, §3].
In case (∃2), we shall establish RANGE and obtain BOOT by Theorem 3.17.
Now ﬁx some Y 2 and let (D, ⪯D) be a directed set with D consisting of the ﬁnite
sequences w1∗in NN such that (∀i, j < |w|)(Y (w(i) = Y (w(j))) →i = j) and
v ⪯D w if (∀i < |v|)(∃j < |w|)(v(i) =1 w(j)). Deﬁne the net cw : D →[0, 1] as
cw := P|w|−1
i=0
2−Y (w(i)). Clearly, cw is increasing and let c be the limit provided by
MCT[0,1]
net . Now consider the following equivalence:
(∃f 1)(Y (f) = k) ↔(∀w1∗)
 |cw −c| < 2−k →(∃g ∈w)(Y (g) = k)

,
(3.6)
for which the reverse direction is trivial thanks to limw cw = c. For the forward
direction in (3.6), assume the left-hand side holds for f = f 1
1 and ﬁx some w1∗
0 such
that |c −cw0| <
1
2k . Since cw is increasing, we also have |c −cw| <
1
2k for w ⪰D w0.
Now there must be f0 in w0 such that Y (f0) = k, as otherwise w1 = w0 ∗⟨f1⟩
satisﬁes w1 ⪰D w0 but also cw1 > c, which is impossible.
Note that (3.6) has the right form to apply ∆-comprehension (modulo some
coding), and the latter provides the set required by RANGE.
□


## Page 21


PLATO AND THE FOUNDATIONS OF MATHEMATICS
21
The net cw from the proof should be called a Specker net, similar to Specker
sequences, pioneered in [84]. In light of the previous (and [75, 76]), proofs from
classical RM can be ‘recycled’ as proofs related to the Plato hierarchy. The afore-
mentioned ‘reuse’ comes at a cost however: the proof of MCT[0,1]
net
→BOOT in
Theorem 3.7 does not make use of countable choice. The previous is not an iso-
lated case: many so-called recursive counterexamples give rise to reversals in RM,
and these results can often be lifted to obtain higher-order results, as studied in
[75, 76] for a variety of topics in RM. We list another example of the reuse of
recursive counterexamples (to even higher types) in Section 3.4.2.
3.3. The Moore-Osgood theorem for nets. We study the Moore-Osgood theo-
rem which provides a suﬃcient criterion for the existence of double limits. We show
that this theorem for nets is explosive in the same way as in the previous sections.
Our motivation is that the above proofs can be viewed as a kind of double limit
construction involving nets and sequences.
As to history, E. H. Moore’s version of the Moore-Osgood theorem apparently
goes back to 1900 (see [29, p. 100]), while Osgood’s version goes back to 1907 (see
[66]).
As expected, Moore-Smith deal with double (net) limits in [52, §7].
We
use the following version of the Moore-Osgood theorem, similar to [7, Lemma 2.3],
where D is assumed to be a subset of Baire space.
Deﬁnition 3.20. [MOT] Let (D, ⪯D) be a directed set with D ⊆NN.
For a
sequence of nets xd,n : (D × N) →[0, 1], if limn→∞xd,n = yd for some net yd : D →
[0, 1] and if the net λd.xd,n is uniformly Cauchy, then limd yd = z for z ∈[0, 1].
A sequence of nets xd,n is uniformly Cauchy if the d claimed to exist by Deﬁni-
tion 3.10 does not depend on the sequence parameter n. This deﬁnition is equivalent
to uniform convergence in ZΩ
2 +QF-AC0,1. We use uniform Cauchyness because one
generally needs non-trivial comprehension and choice to obtain a sequence of limits
from the existence of the individual limits limd xd,n for all n.
Theorem 3.21. The system ACAω
0 + IND + MOT proves Π1
1-CA0.
Proof. A Σ1
1-formula ϕ(n) ∈L2 is readily seen to be equivalent to a formula
(∃f 1)(Y (f, n) = 0) for Y 2 deﬁned in terms of ∃2.
Let D be the set of ﬁnite
sequences in Baire space and let ⪯D be the inclusion ordering, i.e. w ⪯D v if (∀i <
|w|)(∃j < |v|)(w(i) =1 v(j)). Now deﬁne F(w, k) as 1 if (∃i < |w|)(Y (w(i), k) = 0),
and zero otherwise, and deﬁne the sequence of nets xw,k := Pk
i=0
F (w,i)
2i+1 . By deﬁ-
nition, we have limk→∞xw,k = yw, where yw := P∞
i=0
F (w,i)
2i+1 . To prove that xw,k is
uniformly Cauchy, use IND to establish that for every m0 ≥1, there is w of length
m such that (∀i < m)

(∃g1)(Y (g, i) = 0) →Y (w(i), i) = 0

. For m ≥1 and such
w, note that xv,k is below xw,k+ 1
2m for any k and v ⪰D w, i.e. uniform Cauchyness.
Let z be the limit provided by MOT, i.e. limw yw = z. One now readily estab-
lishes the following equivalence for η as in the proof of Corollary 3.9:
(∀n0)

(∃g1)(Y (g, n) = 0) ↔η(z)(n) = 1

.
(3.7)
Clearly, (3.7) yields {n : ϕ(n)}, as required by Π1
1-CA0.
□
Finally, one can obtain BOOT from MOT in the same way as in the previous
sections, while introducing moduli would similarly yield QF-AC0,1. To establish
BOOT →MOT, note that yd is a Cauchy net due to the assumptions in MOT.


## Page 22


22
PLATO AND THE FOUNDATIONS OF MATHEMATICS
3.4. Stronger convergence theorems. We have previously studied the conver-
gence of nets in the unit interval indexed by Baire space. In this section, we show
that interesting phenomena occur when lifting some of these restrictions. In par-
ticular, we study the strength of convergence of nets in function spaces indexed by
Baire space (Section 3.4.1) and of nets in the unit interval with ‘larger’ index sets
beyond Baire space (Section 3.4.2)
3.4.1. Convergence in function spaces. In the previous sections, we have studied a
number of convergence theorems for nets that give rise to parallel hierarchies as
sketched in Figure 3. Of course, these theorems do not involve formula classes, but
the associated hierarchies are still based on formula classes via Π1
k-CAω
0 . In this
section, we formulate MON, a (third-order) convergence theorem for nets that does
not need Π1
k-CAω
0 to bootstrap to the next level, but rather ‘bootstraps itself’, i.e.
RCAω
0 + MON can prove Π1
k-CAω
0 for any k, via longer and longer proofs.
Now, we have previously considered nets in basic spaces like 2N and [0, 1]. While
Moore-Smith in [52] limited themselves to nets in R, Vietoris already studied nets
in (much) more general spaces in [93], even in the early days of nets. Hence, it is
a natural question how strong MCT[0,1]
net
becomes for nets in e.g. function spaces.
Note that this generalisation still is part of the language of third-order arithmetic.
In this section, we show that for nets in the function space [0, 1] →[0, 1], the
associated monotone convergence theorem MON becomes extremely powerful, in
that it implies Π1
k-CAω
0 for any k without additional axioms.
Deﬁnition 3.22. [MON] Let (D, ⪯D) be a directed set where D ⊆NN.
Any
increasing net Fd : D →(I →I) converges to some H : I →I.
Recall that a net Fd : D →(I →I) is increasing if we have that:
(∀x ∈I)(∀d, e ∈D)(d ⪯D e →Fd(x) ≤R Fe(x)).
Due to the boundedness property of Fd, for ﬁxed x ∈I, the net Fd(x) converges to
some limit, and the limit function from MON is obtained by putting all these indi-
vidual limits together. Note that MON implies BOOT by Corollary 3.9. However,
MON is much more ‘explosive’ than the latter by the following theorem.
Theorem 3.23. The system RCAω
0 + MON proves (S2).
Proof. First of all, we prove MON →(∃2). Let Fn be the piecewise linear function
that is zero for x = 0 and 1 for x ≥
1
2n . Consider the directed set (N, ≤) and the
net Fn. The latter is increasing in that (∀n, m ∈N)(∀x ∈[0, 1])(n ≤m →Fn(x) ≤
Fm(x)), and hence Fn has a limit H : I →I by MON. Clearly, H(0) = 0 and
H(x) = 1 for x ∈(0, 1], i.e. H is discontinuous, and [42, §3] yields (∃2).
Secondly, note that the variable ‘f’ in the deﬁnition of the Suslin funtional (S2)
can be restricted to Cantor space without loss of generality. Moreover, if f ∈C
is eventually constant 0 (resp. constant 1), then (∃g1)(∀n0)(f(gn) = 0) clearly
holds (resp. does not hold). Given ∃2, we can decide whether f ∈C is eventually
constant, i.e. we may restrict ourselves to f ∈C that are not eventually constant
when deﬁning the Suslin functional. Recall that ∃2 deﬁnes a functional η1→1 that
converts real numbers in [0, 1] into binary representation, choosing a tail of zeros
whenever there are two possibilities.
Now, let D be the set of ﬁnite sequences in Baire space and let ⪯D be the
inclusion ordering, i.e. w ⪯D v if (∀i < |w|)(∃j < |v|)(w(i) =1 v(j)). For w1∗∈D,


## Page 23


PLATO AND THE FOUNDATIONS OF MATHEMATICS
23
deﬁne the net Fw(f) as 1 if (∃g1 ∈w)(∀n0)(f(gn) = 0), and 0 otherwise. Deﬁne
Gw : D →(I →I) as Gw(x) := Fw(η(x)).
Note that for w ⪯D v, we have
Gw(x) ≤Gw(x) for all x ∈I, i.e. Gw is increasing in the sense of nets.
Let
H : I →I be the limit limw Gw and consider:
(∀f 1 ∈C)

H0(f) = 1 ↔(∃g1)(∀n0)(f(gn) = 0)

,
(3.8)
where H0(f) is H(r(f)) if r(f) has a unique binary representation, and otherwise
0 or 1 depending on whether f is eventually constant 0 or eventually constant 1.
For any f ∈C, (3.8) is immediate in the ‘otherwise’ case in H0(f), by the above.
In the unique representation case, if H0(f) = H(r(f)) = 1 then the deﬁnition of
limit implies that there is w ∈D such that for all v ⪰D w, we have Gv(r(f)) =
Fv(f) = 1, which immediately yields the right-hand side of (3.8).
Now let g1
0
be such that (∀n0)(f(g0n) = 0) in the unique representation case and suppose
H0(f) = H(r(f)) = 0. Again by the deﬁnition of limit, there is w ∈D such that
for all v ⪰D w, we have Gv(r(f)) = Fv(f) = 0. This yields a contradiction for
v = w ∗⟨g0⟩, and (3.8) follows. Clearly, the latter deﬁnes (S2).
□
Corollary 3.24. For any k, the system RCAω
0 + MON proves (S2
k).
Proof. To obtain (S2
2), (∃g1)(∀h1)(∃n0)(f(gn, hn) = 0) is equivalent to the formula
(∃g1)(Y (f, g) = 0), where Y 2 is deﬁned in terms of S2. Now repeat the proof of
the theorem step with ‘(∀n0)(f(gn) = 0)’ replaced by ‘Y (f, g) = 0’.
□
Finally, MON is not that much more ‘exotic’ than e.g. MCT[0,1]
net
by the following.
Theorem 3.25. The system RCAω
0 proves [MCT[0,1]
net + QF-AC1,1 + (∃2)] →MON.
Proof. Let Fd be as in MON. By MCT[0,1]
net , for ﬁxed x ∈I, the net Fd(x) converges
to some limit y ∈I, implying the following formula:
(∀x ∈I)(∃y ∈I)(∀k0)(∃d ∈D)(|Fd(x) −y| <
1
2k ).
Apply QF-AC0,1 to the underlined formula to obtain
(∀x ∈I)(∃y ∈I)(∃d0→1
n
)(∀k0)(|Fdk(x) −y| <
1
2k ),
which qualiﬁes for QF-AC1,1 in the presence of (∃2) and coding of the second ex-
istential quantiﬁer as a type one object. The resulting functional is the limit as
required for MON.
□
The previous proof actually provides a modulus of convergence for the limit
process limd Fd = H. Moreover, introducing a modulus of convergence in MON,
one obtains mutatis mutandis that the enriched principle implies QF-AC1,1, and
hence an equivalence in the previous theorem. One can also prove that MON is
equivalent to the following straightforward generalisation of BOOT:
(∀Y 2)(∃G2)(∀f 1)(G(f) = 0 ↔(∃g1)(Y (f, g) = 0)).
The proof is similar to that of Theorem 3.23, and we therefore omit it.


## Page 24


24
PLATO AND THE FOUNDATIONS OF MATHEMATICS
3.4.2. Index sets beyond Baire space. In this section, we study the Bolzano-Weierstrass
theorem for nets with index sets beyond Baire space, namely subsets of NN →N.
Such index sets are also studied in [74, Appendix A] in the context of computability
theory and RM, but we stress that these results are only given (here and in [74])
by way of illustration: the general study of nets is perhaps best undertaken in a
suitable set theoretic framework. That is not to say this section should be dismissed
as spielerei; our results come with conceptual motivation as follows:
(i) Index sets beyond Baire space do occur ‘in the wild’, namely in e.g. fuzzy
mathematics and gauge integration, by Remark 3.33.
(ii) It is a natural question whether the above proofs generalise to higher types.
(iii) In light of Corollary 3.8, it is a natural question whether nets with index
sets beyond Baire space take us beyond second-order arithmetic.
(iv) It is a natural question whether ECF maps results pertaining to index sets
beyond Baire space into second-order arithmetic.
(v) Nets with index sets beyond NN provide a partial answer to a question from
Section 1.3.1, namely what the Plato hierarchy is a reﬂection of.
As we will see below, the answer is positive for each of these questions.
Thus,
similar to Deﬁnition 2.4, we introduce the following.
Deﬁnition 3.26. [RCAω
0 ] A ‘subset E of NN →N’ is given by its characteristic
function F 3
E ≤3 1, i.e. we write ‘Y ∈E’ for FE(Y ) = 1 for any Y 2. A ‘binary
relation ⪯on the subset E of NN →N’ is given by the associated characteristic
function G(2×2)→0
⪯
, i.e. we write ‘Y ⪯Z’ for G⪯(Y, Z) = 1 and any Y, Z ∈E.
Deﬁnition 3.27. [BW1
net] Any net in Cantor space indexed by a subset of NN →N
has a convergent sub-net.
Theorem 3.28. The system ZΩ
2 + BW1
net proves Π2
1-CA0.
Proof. A Σ2
1-formula ϕ(n) ∈L3 is readily seen to be equivalent to a formula
(∃Y 2)(Z(Y, n) = 0) for Z3 deﬁned in terms of ∃3.
Let E be the set of ﬁnite
sequences in NN →N and let ⪯E be the inclusion ordering, i.e. w ⪯E v if
(∀i < |w|)(∃j < |v|)(w(i) =2 v(j)). Deﬁne the net fw : E →C as fw := λk.F(w, k)
where F(w, k) is 1 if (∃i < |w|)(Z(w(i), k) = 0), and zero otherwise. Using BW1
net,
let φ : B →E and f 1 be such that limb fφ(b) = f. We now establish that
(∀n0)

(∃Y 2)(Z(Y, n) = 0) ↔f(n) = 1

.
(3.9)
For the reverse direction, note that for ﬁxed n0, if Z(Y, n0) = 0 for all Y 2, then
fw(n0) = 0 for any w ∈E. The deﬁnition of limit then implies f(n0) = 0, i.e.
we have established (the contraposition of) the reverse direction. For the forward
direction in (3.9), suppose there is some n0 such that (∃Y 2)(Z(Y, n0) = 0)∧f(n0) =
0. Now, limb fφ(b) = f implies that there is b0 ∈B such that for b ⪰B b0, we have
fφ(b)n0 = fn0, i.e. fφ(b)(n0) = 0 for b ⪰B b0. Let Y 2
0 be such that Z(Y0, n0) = 0,
and use the second item in Deﬁnition 2.11 for d = ⟨Y0⟩, i.e. there is b1 ∈B such
that φ(b) ⪰E ⟨Y0⟩for any b ⪰B b1. Now let b2 ∈B be such that b2 ⪰B b0, b1 as
provided by Deﬁnition 2.7. On one hand, b2 ⪰B b1 implies that φ(b2) ⪰E ⟨Y0⟩, and
hence fφ(b2)(n0) = F(φ(b2), n0) = 1, as Y0 is in the ﬁnite sequence φ(b2) by the
deﬁnition of ⪯E. On the other land, b2 ⪰B b0 implies that fφ(b2)(n0) = f(n0) = 0,
a contradiction. Hence the forward direction follows and so does (3.9), yielding the
set {n : ϕ(n)}, as required by Π2
1-CA0.
□


## Page 25


PLATO AND THE FOUNDATIONS OF MATHEMATICS
25
We now generalise Theorem 3.7 to higher types. To this end, inspired by (3.9),
we generalise BOOT to NN →N as follows:
(∀Z3)(∃X1)(∀n0)(n ∈X ↔(∃Y 2)(Z(Y, n) = 0)).
(BOOT1)
Similarly, let MCT1
net be the monotone convergence theorem based on BW1
net.
Corollary 3.29. The system ZΩ
2 proves BOOT1 ↔MCT1
net.
The L2-sentence
[BOOT1]ECF is provable in Π1
2-CA0.
Proof. For the second part, let γ1 be a total associate for Z3 in BOOT1.
The
right-hand side of [BOOT1]ECF is
(∃α1)
 (∀β1)(∃m0)(α(βm) > 0) ∧(∃k0)(γ(αk, n) = 1)

,
(3.10)
and the set consisting of such n0 is clearly deﬁnable in Π1
2-CA0.
For the ﬁrst part, the reverse direction follows in the same way as the proof of
the theorem, i.e. (3.9) also goes through for the limit provided by MCT1
net. The
forward direction follows by the usual interval halving technique based on BOOT1,
i.e. as in the proof of Theorem 3.7.
□
A problem with the previous results is that (∃3) seems needed, but ECF converts
this axiom to ‘0 = 1’, and the same for (∃2). We now introduce a ‘weaker’ lossy
translation that behaves better in this regard. For any A ∈Lω, let [A]PECF be A
with any variable Y 2 restricted to Y 2 ∈C, i.e. we replace type two functionals
by continuous type two functionals (essentially as in ECF), but do not modify
higher types. We have the following result that suggests that PECF converts ‘ZΩ
2 ⊢
[BOOT1 ↔MCT1
net]’ to ‘ACAω
0 ⊢[BOOT ↔MCTC
net]’.
Theorem 3.30. The system RCAω
0 proves [(∃3)]PECF ↔(∃2), while ACAω
0 proves
[BOOT1]PECF ↔BOOT and [MCT1
net]PECF ↔MCTC
net.
Proof. First of all, any Y 2 ∈C has a type one associate given ACA0 by [41, §4].
Thus, (∃Y 2 ∈C)(Z(Y, n) = 0) is equivalent to (∃f 1)(Z(F(f), n) = 0), where F 1→2
is deﬁned as F(f)(g) := f
 g(µn)(f(gn) > 0)

−1. Similarly modify [MCT1
net]PECF
and [(∃3)]PECF to obtain principles provable from resp. MCTC
net and (∃2).
□
The previous provides a partial answer to a question from Section 1.3.1, namely
what the Plato hierarchy could be a reﬂection of. Our answer is only partial as
PECF does not have as nice properties as ECF: the former converts trivialities like
(∃3) →(∃2) into (∃2) →0 = 1. Perhaps a reﬁnement of PECF will be seen to have
better properties.
Next, Specker nets are used in the proof of Theorem 3.19 to establish MCT[0,1]
net
→
RANGE. We show that this proof also readily generalises as follows.
Theorem 3.31. The system ZΩ
2 + QF-AC0,2 + MCT1
net proves the following:
(∀G3)(∃X1)(∀n0)

n ∈X ↔(∃Y 2)(G(Y ) = n)].
(RANGE1)
Proof. A slight modiﬁcation of the proof of Theorem 3.19 goes through as follows:
let E be the set of ﬁnite sequences in NN →N and let ⪯E be the inclusion relation,
for which ∃3 is needed (instead of ∃2). The Specker net cw : E →[0, 1] is deﬁned in
exactly the same way as in Theorem 3.19, namely as cw := P|w|−1
i=0
2−Z(w(i)), where
Z3 is given. The associated version of (3.6) is:
(∃Y 2)(Z(Y ) = k) ↔(∀w2∗)
 |cw −c| < 2−k →(∃V ∈w)(Z(V ) = k)

,
(3.11)


## Page 26


26
PLATO AND THE FOUNDATIONS OF MATHEMATICS
where c = limw cw is provided by MCT1
net. Applying QF-AC0,2 to (3.11) as in the
proof of Theorem 3.18 yields the set X ⊂N required for RANGE1.
□
In light of the proofs of Theorem 3.28 and 3.31, it is now be clear that the above
proofs readily generalise to higher types.
To avoid repetition, we do not study
further generalisations of convergence theorems for nets in this paper. We do list
some nice results: let BWσ
net be the obvious generalisation of BW1
net to index sets of
type σ + 1 objects. A straightforward modiﬁcation of Theorem 3.28 implies that
RCAω
0 + (∃k+2) + BWk
net proves Πk+1
1
-comprehension for k ≥1. Hence, the general
Bolzano-Weierstrass theorem for nets is extremely hard to prove.
Recall Corollary 3.14 which implies CAUmod ↔QF-AC0,1 over ZΩ
2 . Let CAU2
mod
be the generalisation of CAUmod to index sets that are subsets of NN →N.
Corollary 3.32. The system RCAω
0 + (∃4) proves QF-AC0,2 ↔CAU2
mod.
Proof. Generalise the proof of Theorem 3.13 in the same way as Theorem 3.28.
□
Let CAUσ
mod be the obvious generalisation of CAU2
mod to sets of type σ+1 objects.
One then readily proves QF-AC0,k ↔CAUk
net over RCAω
0 + (∃k+2).
We ﬁnish this section with a conceptual remark on ‘large’ index sets and their
occurrence in mathematics and logic.
Remark 3.33 (Large index sets). First of all, Zadeh founded the ﬁeld of fuzzy
mathematics in [95]. The core notion of fuzzy set is a mapping that assigns values
in [0, 1], i.e. a ‘level’ of membership, rather than the binary relation from usual set
theory. The ﬁrst two chapters of Kelley’s General Topology ([39]) are generalised to
the setting of fuzzy mathematics in [68]. As an example, [68, Theorem 11.1] is the
fuzzy generalisation of the classical statement that a point is in the closure of a set
if and only if there is a net that converges to this point. However, as is clear from
the proof of this theorem, to accommodate fuzzy points in X, the net is indexed
by the space X →[0, 1].
Secondly, the iterated limit theorem (both the fuzzy and classical versions: [68,
Theorem 12.2] and [39]) involves an index set Em indexed by m ∈D, where D is
an index set. Thus, ‘large’ index sets are found in the wild.
Thirdly, by way of an exercise, the reader should generalise the well-known for-
mulation of the Riemann integral in terms of nets (see e.g. [39, p. 79]) to the gauge
integral as studied in [60, §3.3]. As will become clear, this generalisation involves
nets indexed by R →R-functions, and this very deﬁnition can also be found in the
literature, namely [45, §1.3].
Fourth, the results in [74, §4.3-4.5] connect continuity and open sets to nets, all
in R, while avoiding the Axiom of Choice. As is clear from the proofs (esp. the use
of the net xd := d), replacing R by a larger space requires the introduction of nets
with a similarly large index set. In particular, to show that a net-closed6 set C is
closed (see [74, Theorem 4.15] for C ⊆R), one seems to need nets with an index
set the same cardinality as C.
6A set C is net-closed if for any net in C that converges to x, we also have x ∈C ([39, p. 66]).


## Page 27


PLATO AND THE FOUNDATIONS OF MATHEMATICS
27
4. Main results II: open sets and Heine-Borel compactness
4.1. Introduction. In this section, we establish the results sketched in Section 1.3
pertaining to open sets and the axiom BOOT, as well as the connection to Heine-
Borel compactness. In particular, the latter connection is studied in Section 4.3,
while we identify the ‘correct’ notion of open set to be used in the Plato hierarchy
and obtain interesting RM-results in Section 4.2. As will become clear, some of
our results are straightforward generalisations of second-order equivalences, while
others yield genuine surprises, like the Cantor-Bendixson theorem. In particular,
the study of open sets in the Plato hierarchy directly inspires the higher-order
counterparts of ATR0 and Π1
1-CA0, as will become clear in Section 4.2.
We ﬁrst discuss the intended meaning of ‘correct’ notion of open set. While such
judgements are inherently subjective, we shall use the following two (more or less)
objective criteria to judge whether a new notion of open set is acceptable.
(I) The new notion of open set reduces to RM-codes of open sets under ECF.
(II) The new notion of open set yields (lots of) equivalences that reduce to
known (interesting) equivalences under ECF.
The ﬁrst criterion is a basic requirement that merits no further discussion, while the
second criterion is based on the so-called main theme of RM, expressed as follows:
very often, if a theorem of ordinary mathematics is proved from the
“right” set existence axioms, the statement of that theorem will be
provably equivalent to those axioms over some weak base system.
This opinion may be found in e.g. [14,19,82] and many other places. In Section 4.2,
we introduce a notion of open set consistent with the above items (I) and (II). We
shall obtain a number of equivalences involving nets rather than sequences. We
stress that ﬁnding the ‘correct’ generalisation of open set, namely uncountable
unions as in Deﬁnition 4.2, is non-trivial as follows.
Our initial motivation for the new notion of open set as in Deﬁnition 4.2, stems
from [64, 74]; in the latter, open sets in R are given by (possibly discontinuous)
characteristic functionals Y : R →R where ‘x ∈Y ’ is short for Y (x) >R 0. While
this deﬁnition begets plenty of interesting results, it does not yield the expected
reversals; Deﬁnition 4.2 is better this way in light of Theorem 4.4. In other words,
the concept of open set from [64,74] satisﬁes (I) and not (II), but yields interesting
results as follows.
Remark 4.1. First of all, nets obviate the (otherwise necessary) use of the Axiom
of Choice in [74] as part of the study of open and closed sets via sequences/nets.
Secondly, the ∆-functional from [64, §5] converts between two notions of open
set based on characteristic functions, namely from a realiser for the usual deﬁnition
of open set to a distance function for the complement. It is proved in [64] that:
(P1) ∆is not computable in any type 2 functional, but computable in any
Pincherle realiser (see [63]), a class weaker than Θ-functionals (see [58,59]).
(P2) ∆is unique, genuinely type 3, and adds no computational strength to ∃2
in terms of computing functions from functions.
It was previously believed that functionals with the above properties would be ad
hoc and could only be obtained via some complicated forcing construction.
We ﬁnish this section by noting that while our concept of open set is uncount-
able unions of basic opens (see Deﬁnition 4.2), we could obtain all the below results


## Page 28


28
PLATO AND THE FOUNDATIONS OF MATHEMATICS
working solely with countable unions of basic opens assuming the mainstream def-
inition of ‘countable’, as discussed in Remark 4.20.
4.2. Open sets via uncountable unions.
4.2.1. Open sets as uncountable unions. In this section, we introduce a notion of
open set consistent with items (I) and (II) from Section 4.1.
In particular, we
obtain some elegant equivalences involving locatedness and nets at the level of ACA0
(Section 4.2.2), and perfect sets at the level of ATR0 and Π1
1-CA0 (Section 4.2.3).
First of all, we shall make use of the following notion of open set. Hereafter,
‘open’ refers to the below deﬁnition, while ‘RM-open’ refers to the well-known RM-
deﬁnition from [82, II.5] involving countable unions of basic open balls.
Deﬁnition 4.2. [Open sets] An open set O in R is represented by a functional
ψ : R →R2. We write ‘x ∈O’ for (∃y ∈R)(x ∈Iψ
y ), where Iψ
y is the open interval
 ψ(y)(1), ψ(y)(1) + |ψ(y)(2)|

in case the end-points are diﬀerent, and ∅otherwise.
We write O = ∪y∈RIψ
y to emphasise the connection to uncountable unions. A closed
set is represented by the complement of an open set.
Intuitively, open sets are given by uncountable unions ∪y∈RIψ
y , just like RM-open
sets are given by countable such unions. Hence, our notion of open set reduces to the
notion RM-open set when applying ECF or when all functions on R are continuous.
Moreover, writing down the deﬁnition of elementhood in an RM-open set, one
observes that such sets are also open (in our sense). Finally, closed sets are readily
seen to be sequentially closed, and the same for nets instead of sequences.
The following ‘coding principle’ turns out to have nice properties. Note that
open, a weaker version of open+, was introduced and studied in [64]. We ﬁx an
enumeration of all basic open balls B(qn, rn) ⊂R for rational qn, rn with rn >Q 0.
Deﬁnition 4.3. [open+] For every open set Z ⊆R, there is X ⊂N such that
(∀n ∈N)(n ∈X ↔B(qn, rn) ⊆Z).
In the next section, we prove equivalences at the level of ACA0 involving BOOT
and open+. Equivalences at the level of ATR0 and Π1
1-CA0 are in Section 4.2.3.
4.2.2. At the level of ACA0. A number of theorems regarding RM-closed sets are
equivalent to ACA0; we now generalise some of these results, based on Deﬁnition 4.2.
Recall that a closed set C is called located (see [82, IV.2.17] for the RM-notion)
if the distance function d(x, C) := infy∈C d(x, y) exists as a continuous real-valued
function.
To be absolutely clear, ‘continuous’ refers to the usual ‘epsilon-delta’
deﬁnition, while ‘RM-continuous’ refers to the RM-deﬁnition as in [82, II.6.1].
Theorem 4.4. The following are equivalent over RCAω
0 + QF-AC0,1:
(a) open+ + ACA0,
(b) Every non-empty closed set in [0, 1] is located,
(c) For every non-empty closed set C ⊆[0, 1], the supremum sup C exists,
(d) Monotone convergence theorem for nets in [0, 1] indexed by subsets of NN,
(e) For closed C ⊆[0, 1] and f : R →R continuous on C, supx∈C f(x) exists,
(f) For closed C ⊆[0, 1] and f : R →R cont. on C, f attains its maximum,
(g) BOOT.
The axiom QF-AC0,1 is only used for BOOT →open+.


## Page 29


PLATO AND THE FOUNDATIONS OF MATHEMATICS
29
Proof. We ﬁrst prove (a) →(b) →(c) →(d) →(g) →(a).
The implication
(a)→(b) follows from the usual second-order equivalence between ACA0 and the
fact that any RM-closed set in the unit interval is located by [25, Theorem 3.8],
since open+ reduces open sets to RM-open sets. Indeed, an RM-code for Z as in
open+ is given by ∪n∈N(an, bn), where an = bn if n ̸∈X and (an, bn) = B(qn, rn)
otherwise. The implication (b) →(c) is immediate as either 1 is the supremum of
C, or 1 −d(1, C) is, where the locatedness of C begets the distance function d.
For the implication (c)→(d), ﬁx an increasing net xd : D →[0, 1]. In case this
net comes arbitrarily close to 1, we are done. If not, deﬁne the non-empty closed
set C by putting x ∈C if and only if (∀d ∈D)(x ≥R xd) for x ∈[0, 1]. Indeed, the
complement of C is open in [0, 1], as it is given by ∪d∈D[0, xd). Since C is closed,
sup C exists and the latter real is readily seen to be the limit of the net xd. Note
that C is not exactly as in Deﬁnition 4.2, but this does not matter: in case ¬(∃2),
the implication (c)→(d) reduces to a known second-order result; in case (∃2), we
can use ∃2 to freely convert between reals and elements of Cantor and Baire space,
modifying C to conform to Deﬁnition 4.2. The implication (d) →(g) is immediate
by Theorem 3.7.
We now prove the ‘crux’ implication BOOT →open+. In case ¬(∃2), all func-
tionals on R or NN are continuous by [42, §3]. Thus, an open set ∪y∈RIψ
y reduces
to the countable union ∪q∈QIψ
q , yielding open+ in this case. In case (∃2), let O be
an open set given by ψ : R →R2 as in Deﬁnition 4.2. Now use BOOT (and (∃2))
to deﬁne the following set X ⊂N × Q:
(∀n ∈N, q ∈Q)
 (n, q) ∈X ↔(∃y ∈R)
 B(q, 1
2n ) ⊂Iψ
y

.
(4.1)
Apply QF-AC0,1 to the forward direction in (4.1) to obtain Φ such that:
(∀n ∈N, q ∈Q)
 (n, q) ∈X →
 B(q, 1
2n ) ⊂Iψ
Φ(n,q)

.
(4.2)
The following formula (4.3) provides a representation of O as a countable union of
open balls, and of course gives rise to open+:
x ∈O ↔(∃n ∈N, q ∈Q)((n, q) ∈X ∧x ∈Iψ
Φ(n,q)).
(4.3)
For the reverse implication in (4.3), x ∈O follows by deﬁnition from the right-
hand side of (4.3). For the forward implication, x0 ∈O implies B(x0,
1
2n0 ) ⊂Iψ
y0
for some y0 ∈R and n0 ∈N by deﬁnition.
For n1 large enough, the rational
q0 := [x0](n1) is inside B(x0,
1
2n0+1 ). Hence, (q0, n0 + 1) ∈X by (4.1) for y = y0.
Applying (4.2) then yields B(q0,
1
2n0+1 ) ⊂Iψ
Φ(n0+1,q0). By assumption, we also have
x0 ∈B(q0,
1
2n0+1 ) ⊂Iψ
Φ(n0+1,q0), and the right-hand side of (4.3) follows.
What remains to prove is (a) →(f) →(e) →(d). The implication (a) →(f)
follows as in the ﬁrst paragraph of this proof. Indeed, ACA0 is equivalent to item (f)
for RM-closed sets by [82, IV.2.11] and open+ converts closed sets into RM-closed
sets. Clearly, (f) →(e) is trivial, while (e) →(d) follows as in the second paragraph
of this proof for the net xd. Indeed, consider the closed set deﬁned by x ∈C if and
only if (∀d ∈D)(x ≥R xd) and the function f(x) := −x + 1. The real supx∈C f(x)
readily provides the limit of the net xd, and we are done.
□
It should be noted that (c) →(d) in the proof is proved based on the proof of
[25, Theorem 3.8], but with sequences replaced by nets (indexed by NN). Moreover,
in light of the previous proof, we could restrict items (f) and (e) to RM-continuous


## Page 30


30
PLATO AND THE FOUNDATIONS OF MATHEMATICS
functions (or other notions). Since ECF converts open+ to a triviality, we do need
ACA0 in item (a). Moreover, it seems that QF-AC0,1 is essential in the previous
theorem, but a reversal is not possible: ZΩ
2 proves open+ by [64, Thm 3.22].
Finally, a separably RM-closed set S in a metric space is given in RM by a
sequence λn.xn and ‘x ∈S’ is then (∀k0)(∃n0)(d(x, xn) <
1
2k ), where d is the metric
of the space. Intuitively, a separably RM-closed set is represented by a countable
dense subset given by a sequence. We shall study this concept for sequences replaced
by nets as in Deﬁnition 4.5.
What follows is not just spielerei for the following reason: it is well-known that
ZF cannot prove that ‘R is a sequential space’, i.e. the equivalence between the
deﬁnition of closed and sequentially closed set; countable choice however suﬃces
(see [30, p. 73]). On the other hand, we can avoid the Axiom of Choice by replacing
sequences with nets everywhere, as shown in [74, §4.4]. In this light, the following
deﬁnition make sense.
Deﬁnition 4.5. A separably closed set S in R is given by a net xd : D →Q with
D ⊆NN and where x ∈S is given by (∀k0)(∃d ∈D)(|x −xd| <
1
2k ).
Principle 4.6 (CLO). A separably closed set in R is closed.
Note that ACA0 is equivalent to the RM-version of CLO by [13, Theorem 2.9].
Theorem 4.7. The system RCAω
0 + QF-AC0,1 proves CLO ↔BOOT.
Proof. The forward direction is immediate by the proof of [76, Theorem 3.19], in
light of Theorem 3.18. For the reverse direction, in case ¬(∃2), the implication
reduces to the known second-order result, following Remark 1.1.
In case (∃2),
let S and xd be as in CLO.
Now use (∃2) and BOOT to obtain a set X ⊂Q
such that (∀q ∈Q)(q ∈X ↔q ∈S).
By deﬁnition, for any x ∈R, we have
x ̸∈S ↔(∃k ∈N)([x](k) ̸∈S), and the latter is decidable thanks to ∃2 and the
aforementioned set X. Following this observation, for any x ̸∈S, we can ﬁnd k0 ∈N
using Feferman’s µ such that B(x,
1
2k0 ) does not intersect S. Thus, the complement
of S is an open set as in Deﬁnition 4.2, and we are done.
□
As it happens, the converse of CLO for RM-codes is equivalent to Π1
1-CA0 by
[13, Theorem 2.18], and we study systems at the level of the latter in Section 4.2.3.
We ﬁnish this section with a conceptual remark regarding the above results.
Remark 4.8 (The power of nets). As noted in Remark 2.12, nets with countable
index sets do not yield a stronger monotone convergence theorem, while uncountable
index sets like NN of course do, by the above. Thus, ‘larger’ index sets would seem to
yield stronger versions of the monotone convergence theorem. Moreover, the latter
seems intrinsically tied to arithmetical comprehension, as ECF translates BOOT to
ACA0. Both of the aforementioned suggestions are incorrect as follows: one can
show that MCT−
net, i.e. the monotone convergence theorem for nets in [0, 1] indexed
by 2N, is provable from the existence of the intuitionistic fan functional as follows:
(∃Ω3)(∀Y 2, f, g ∈2N)(fΩ(Y ) = gΩ(Y ) →Y (f) = Y (g)).
(MUC)
Hence, MCT−
net has the same ﬁrst-order strength as WKL0, as ECF converts MUC
into WKL by [47, p. 497]. Moreover, the same holds for the items from Theorem 4.4
for open sets represented by ∪y∈[0,1]IΨ
y and Ψ : R →Q2, and for many theorems
pertaining to nets from [74]; this is a sizable contribution to Hilbert’s program as


## Page 31


PLATO AND THE FOUNDATIONS OF MATHEMATICS
31
in [82, IX.3.18]. Moreover, over RCAω
0 , we have [ACA0 + MCT−
net] ↔MCTC
net, while
MUC →MCT−
net is also provable using intuitionistic logic, i.e. convergence theorems
for nets are not necessarily non-constructive, but can be (at least) intuitionistic.
In conclusion, the structure of the index set matters as much as its size, and these
results should be contrasted with [82, V.5.8].
4.2.3. At the level of ATR0 and Π1
1-CA0. We study theorems pertaining to perfect
sets based on our notion of open set from Deﬁnition 4.2. This will give rise to the
counterparts of ATR0 and Π1
1-CA0 in the Plato hierarchy.
First of all, the Cantor-Bendixson theorem for RM-closed sets is equivalent to
Π1
1-CA0 by [82, VI.1.6]. We study this theorem for closed sets as in Deﬁnition 4.2.
Principle 4.9 (CBT). For any closed set C ⊆[0, 1], there exist P, S ⊂C such that
C = P ∪S, P is perfect and closed, and S0→1 is a sequence of reals.
To be absolutely clear, the countable set S is given as a sequence of real numbers
S0→1, just like in second-order RM. We also study the following variation of CBT
involving the ‘usual’ deﬁnition of countable set, i.e. the existence of an injective
function from the set to N.
Principle 4.10 (CBT′). For closed C ⊆[0, 1], there is P, S ⊆C such that C =
P ∪S, P is perfect and closed, and S is a countable set of points of C.
By Theorem 4.11, the exact notion of countable set in CBT does not matter.
On one hand, theorems like e.g. item (b) from Theorem 4.4 only mention closed
sets in the outermost universal quantiﬁer, i.e. we are dealing with a straightforward
generalisation of the associated second-order theorem.
On the other hand, the
Cantor-Bendixson theorem as in CBT additionally states the existence of a (perfect)
closed set, i.e. it is not clear whether CBT is in fact a generalisation of the second-
order version in the absence of open+. Nonetheless, we have the following splitting.
Theorem 4.11. Over RCAω
0 +QF-AC0,1, we have [ACA0+CBT] ↔[ACA0+CBT′] ↔
[Π1
1-CA0 + BOOT].
Proof. Recall that Π1
1-CA0 is equivalent to the second-order version of CBT over
ACA0 ([82, VI.1.6]). Hence, the second reverse implication is immediate from open+
provided by Theorem 4.4. Moreover, it suﬃces to prove CBT′ →BOOT for the
forward implications as CBT →CBT′. Since the implication reduces to the second-
order result in case ¬(∃2), we may assume (∃2). Fix Y 2 and consider the following:
the formula (∃f 1)(Y (f, n) = 0) is equivalent to (∃X ⊂N2)(Y (F(X), n) = 0),
where F(X)(n) := (µm)((n, m) ∈X). Hence, (∃f 1)(Y (f, n) = 0) is equivalent to
a formula (∃f ∈2N)( ˜Y (f, n) = 0), where ˜Y is deﬁned explicitly in terms of Y and
∃2. Now deﬁne the functional Z : R →R as:
Z(x) :=









∅
if
n <R |x| ≤R n + 1 ∧
˜Y (η(x)(0), n) × ˜Y (η(x)(1), n) = 0
(n, n + 1
2) ∪
(n + 1
2, n + 1)
otherwise
,
(4.4)
where η(x) provides a pair consisting of the binary expansions of x −⌊x⌋; the pair
consists of identical elements if there is a unique such expansion. Note that ∃2 can
deﬁne such functionals Z and η1→(1×1). One readily converts Z into an open set


## Page 32


32
PLATO AND THE FOUNDATIONS OF MATHEMATICS
O as in Deﬁnition 4.2. Let C = P ∪S be the complement of O, where P, S are
provided by CBT′, i.e. S is just a countable set of points. Then for all n ∈N:
(∃f 1)(Y (f, n) = 0) ↔[(n + 1
2) ∈P],
(4.5)
and note that P is a closed set and hence ‘x ∈P’ has the form ‘(∀y ∈R)A(x, y)’
for arithmetical A(x, y) by Deﬁnition 4.2. Hence, BOOT follows from (4.5) as ∆-
comprehension is available by Theorem 3.18
□
The attentive reader has noted that the open set O deﬁned by Z in the previous
proof is actually a countable union of intervals in the usual sense of ‘countable’
from mainstream mathematics. We discuss this point in Remark 4.20. We also
note that (4.5) only holds because P is the largest perfect subset of C, i.e. it would
not necessarily work for other perfect subsets.
Next, we formulate another variation of CBT involving a characteristic function
for the countable set.
Principle 4.12 (CBT′′). For any closed set C ⊆[0, 1], there exist P, S ⊂C such
that C = P ∪S, P is perfect and closed, and there is a characteristic function for
the countable set S of points of C.
We have the following nice equivalence.
Corollary 4.13. Over RCAω
0 + QF-AC0,1, [ACA0 + CBT′′] ↔[(∃2) + BOOT].
Proof. In the light of the proof of the theorem and the fact that [BOOT + (∃2)] →
Π1
1-CA0, we only need to prove CBT′′ →(∃2), which is immediate by [42, §3].
□
Next, we study the converse of CLO from the previous section, as follows.
Principle 4.14 (OLC). A closed set in R is separably closed.
Note that the RM-version of OLC is equivalent to Π1
1-CA0 over RCA0 by (the
proof of) [13, Theorem 2.18]. The same caveats as for CBT apply to OLC, and we
have the following splitting.
Corollary 4.15. Over RCAω
0 + QF-AC0,1, we have OLC ↔[BOOT + Π1
1-CA0].
Proof. The reverse direction is immediate from the known second-order results, in
light of Theorem 4.4 and 4.7, and the fact that sequences are nets. For the forward
direction, consider the closed set C from the proof of Theorem 4.11. Then OLC
provides a net xd generating a set S equalling C. Note that we have for all n0:
(∃f 1)(Y (f, n) = 0) ↔(n + 1
2 is an isolated point of C)
↔(∀d ∈D)(xd ∈(n, n + 1) →xd = n + 1
2),
and ∆-comprehension (together with (∃2) as usual) yields BOOT. Note that in case
¬(∃2), the implication reduces to the known second-order results.
□
We included the previous result as it gives rise to the following conceptual re-
mark: in spaces ‘larger’ than R, it is natural to deﬁne open sets given by uncountable
unions indexed by NN →N, while separably closed sets are given by nets indexed by
NN →N. The associated generalisations of CLO and OLC then imply BOOT1. To
put it more bluntly, even if the reader does not share the author’s sense of wonder
about these results, that the latter generalise to all ﬁnite types with little eﬀort,
should at least come as a surprise.


## Page 33


PLATO AND THE FOUNDATIONS OF MATHEMATICS
33
Next, we study the perfect set theorem for closed sets as in Deﬁnition 4.2. This
theorem for RM-codes is equivalent to ATR0 by [82, V.5.5 and VI.1.5]. A subset C
of R is uncountable if for every sequence of reals λn.xn, there is y ∈C such that
(∀n ∈N)(xn ̸=R y); the same concept is used in RM, namely in [82, p. 193].
Principle 4.16 (PST). For any closed and uncountable set C ⊆[0, 1], there exist
P ⊆C such that P is perfect and closed.
The same caveats as for CBT apply to PST, and we have the following splitting.
Theorem 4.17. Over RCAω
0 + QF-AC0,1, [ACA0 + PST] ↔[ATR0 + BOOT].
Proof. Recall that ATR0 is equivalent to the second-order version of PST over ACA0
by [82, V.5.5]. The reverse implication is immediate from open+ provided by The-
orem 4.4. Moreover, it suﬃces to prove PST →BOOT for the forward implication.
Since the implication reduces to ATR0 →ACA0 in case ¬(∃2), we may assume (∃2).
Fix Y 2 and deﬁne the following functional:
Z(x) :=





(n, n + 1
2) ∪
(n + 1
2, n + 1)
if
n <R |x| ≤R n + 1 ∧
˜Y (η(x)(0), n) × ˜Y (η(x)(1), n) = 0
(n, n + 1)
otherwise
,
(4.6)
One readily converts Z into an open set O as in Deﬁnition 4.2.
Let C be the
complement of O and note the former only consists of isolated points, i.e. C cannot
have a perfect subset. Hence, the contraposition of PST provides a sequence λn.xn
that includes all the elements of C. We now have, for all n ∈N, that
(∃f 1)(Y (f, n) = 0) ↔(∃m ∈N)(n + 1
2 =R xm ∧xm ∈C).
(4.7)
Given QF-AC0,1, a formula of the form (∃m0)(∀f 1)(Y (f, n) = 0) is equivalent to
(∀g(0×0)→1)(∃m0)(Y (λm.g(n, m), n) = 0). Since (∃2) is given and since the right-
hand side of (4.7) has the aforementioned form, we observe that ∆-comprehension
applies to the latter, and and BOOT follows.
□
By Remark 4.8, open sets represented by ∪x∈[0,1]IΨ
x have a lot more ‘constructive’
properties than open sets represented by ∪x∈RIΨ
x . In fact, one readily shows that
MUC implies CBT and PST formulated using the former notion of open set indexed
by the unit interval. As noted in Remark 4.8, this means that these theorems have
the same ﬁrst-order strength as WKL0.
Inspired by the previous, ATR0 and Π1
1-CA0 now boast higher-order counterparts.
Deﬁnition 4.18. [BOOT2] For Y 2 such that λg1.Y (f, g, n) is continuous for all
f 1, n0, we have (∃X1)(∀n0)(n ∈X ↔(∃f 1)(∀g1)(Y (f, g, n) = 0)).
It is straightforward to show that BOOT2 ↔[BOOT + Π1
1-CA0] over RCAω
0 , which
combines nicely with Theorem 4.11 and similar equivalences.
Deﬁnition 4.19. [Σ-TR] For θ(n, g) ≡(∃f 1)(Z(f, g, n) = 0) where λg1.Z(f, g, n)
is continuous for any f 1, n0, we have:
(∀X1)(WO(X) →(∃Y 1)Hθ(X, Y )).
It is straightforward to show that the ECF-translation of Σ-TR is ATR0, while
[ATR0 + BOOT] ↔Σ-TR is immediate, which combines nicely with Theorem 4.17.
A related result is mentioned below Theorem 5.4.


## Page 34


34
PLATO AND THE FOUNDATIONS OF MATHEMATICS
Moreover, let T-SEP be the usual separation schema (see e.g. [82, I.11.7]) for
formulas ϕi(n) ≡(∃f 1
i )(∀g1
i )(Yi(fi, gi, n) = 0).
Imitating the proof that ATR0
follows from Σ1
1-separation in [82, V.5.1], one readily obtains T-SEP →Σ-TR. The
crucial part is that given countable choice as in QF-AC0,1, (∃Y 1)Hθ(X, Y ) has the
same form as the ϕi in T-SEP. Restricting to a continuous parameter gi seems
essential for a reversal.
Finally, with the gift of hindsight, we can now generalise Deﬁnition 4.2 and
Theorem 4.4 to any higher type. By way of an example, one can consider nets
indexed by subsets of NN →N, while the quantiﬁer ‘(∃y ∈R)’ in the deﬁnition of
open sets is similarly ‘bumped up one type’, namely from ranging over R to R →R.
The associated comprehension axiom is of course BOOT1. The equivalences in the
above theorems then go through over a suitable base theory. We leave the details
to be worked out. We ﬁnished this section with an important conceptual remark.
Remark 4.20 (A cardinality by any other name). Let us begin by recalling that if
∪n∈N(an, bn) is a countable union of basic open balls, then so is ∪f∈NN(aY (f), bY (f))
for any Y 2 and using the mainstream deﬁnition of ‘countable set’. Now note that
the open set O deﬁned by Z in (4.4) can be expressed in the latter form, i.e. it is also
a countable union of basic open balls. Thus, all the results in this section also hold
for CBT restricted to open sets given by countable unions, i.e. the generalisation to
uncountable unions is (technically) superﬂuous.
For the above reason, countable unions from RM like ∪n∈N(an, bn) should be
referred to as ‘sequential’ or ‘searchable’ or a similar term that captures the fact that
we are dealing with a sequence that one can search through ‘one by one’ in a weak
system. By contrast, the countable union ∪f∈NN(aY (f), bY (f)) is not searchable in
any reasonably sense. In conclusion, the lack of structure of O deﬁned by (4.4) is
what gives rise to the strength of CBT, not the cardinality of the index set. More
palatable examples based on countable ﬁelds can be found in [75,76].
We recall that a similar situation for nets exists, as discussed in Remark 4.8.
Moreover, deﬁning ‘w ≈D v’ as cw =R cv in the proof of Theorem 3.19, we observe
that the index set D only involves countably many equivalence classes modulo ≈D.
In this sense, the index set D of cw is also countable.
4.3. Heine-Borel compactness. In this section, we connect BOOT to HBU and
other higher-order axioms as in Figure 2.
We ﬁrst show that HBU follows from BOOT, in contrast to the known compre-
hension axioms of third-order arithmetic provided by Π1
k-CAω
0 .
Theorem 4.21. The system RCAω
0 + IND or RCAω
0 + QF-AC0,1 proves BOOT →
HBU while Zω
2 + QF-AC0,1 does not prove BOOT or HBU.
Proof. The ﬁrst negative result follows directly from Theorem 3.2, while Zω
2 +
QF-AC0,1 ̸⊢HBU has been established in [60,63]. For the positive result, we prove
HBUc, i.e. the Heine-Borel compactness of Cantor space, as follows
(∀G2)(∃f1, . . . , fk ∈C)(∀f 1 ∈C)(∃i ≤k)(f ∈[fiG(fi)]).
(HBUc)
Note that HBU ↔HBUc over RCAω
0 by the proof of [60, Theorem 3.3]. Fix G2 and
let A(σ) be the following formula
(∃g ∈C)

G(g) ≤|σ| ∧σ ∗00 · · · ∈[gG(g)]

,
(4.8)


## Page 35


PLATO AND THE FOUNDATIONS OF MATHEMATICS
35
where σ0∗is a ﬁnite sequence of natural numbers. Note that the formula in (4.8)
in square brackets is quantiﬁer-free. Thus, BOOT provides a set X ⊆N such that
(∀σ0∗)(σ ∈X ↔A(σ)), with minimal coding. Now, we have (∀f ∈C)(∃n0)A(fn)
since we may take g = f and n = G(f). Hence, we have (∀f ∈C)(∃n0)(fn ∈X)
and applying QF-AC1,0, there is H2 such that (∀f ∈C)(fH(f) ∈X) and H(f)
is the least such number. Obviously H2 is continuous on C and hence bounded
above on C by [41, §4]. Hence, there is N 0
0 such that (∀f ∈C)(∃n ≤N0)A(fn).
Let σ1, . . . , σ2N0+1 enumerate all binary sequences of length N0 + 1 and deﬁne
fi := σi ∗00 . . . for i ≤2N0+1. Intuitively speaking, we now apply (4.8) for fi and
obtain gi for each i ≤2N0+1. Then ⟨g1, . . . , g2N0+1⟩provides the ﬁnite sub-cover
for G. Formally, it is well-known that ZF proves the ‘ﬁnite’ axiom of choice via
mathematical induction (see e.g. [88, Ch. IV]). Similarly, one readily uses IND to
prove the existence of the aforementioned ﬁnite sequence based on (4.8). We can
replace IND by QF-AC0,1, which is applied to (4.8) to yield the ﬁnite sub-cover.
□
The ﬁnal part of the proof was ﬁrst used in [71] to prove without using the Axiom
of Choice the equivalence between HBU and a version involving more general covers.
Note that BOOT →HBU becomes ACA0 →WKL0 when applying ECF.
Secondly, WKL0 is equivalent to the separation axiom Σ0
1-SEP, i.e. the schema
(4.9) for L2-formulas ϕi ∈Σ0
1, by [82, IV.4.4]. We consider the separation axiom
Σ-SEP and note that HBU →Σ-SEP becomes WKL0 →Σ0
1-SEP under ECF.
Deﬁnition 4.22. [Σ-SEP] For ϕi(n) ≡(∃f 1
i )(Yi(fi, n) = 0), we have
(∀n0)(¬ϕ1(n) ∨¬ϕ2(n)) →(∃Z1)(∀n0)

ϕ1(n) →n ∈Z ∧ϕ2(n) →n ̸∈Z

. (4.9)
Theorem 4.23. The system RCAω
0 + IND + QF-AC1,1 proves HBU →Σ-SEP.
Proof. Suppose ϕi is as in Σ-SEP and satisﬁes the antecedent of (4.9). Note that
using IND, it is straightforward to prove that for every m0, there is a ﬁnite binary
sequence σ0∗such that |σ| = m and
(∀n < m)

ϕ1(n) →(σ(n) = 1) ∧ϕ2(n) →(σ(n) = 0)

.
(4.10)
Now let A(n, Z) be the formula in square brackets in (4.9) and suppose we have
(∀Z1)(∃n0)¬A(n, Z). Note that ¬A(n, Z) hides two existential quantiﬁers involv-
ing f1, f2.
Applying QF-AC1,1, we obtain G : C →N such that (∀Z1)(∃n ≤
G(Z))¬A(n, Z). Apply HBUc to the canonical cover ∪f∈C[fG(f)] and obtain a
ﬁnite sub-cover f0, . . . , fk, i.e. ∪i≤k[fiG(fi)] also covers C. Let k0 be maxi≤k G(fi)
and consider binary σ0 of length k0 + 2 satisfying (4.10). Then g0 := σ0 ∗00 . . .
is in some neighbourhood of the ﬁnite sub-cover, say g0 ∈[fjG(fj)]. By deﬁni-
tion, k0 ≥G(fj), i.e. g0G(fj) = σ0G(fj) = fjG(fj). However, (4.10) is false for
m = G(fj) and σ = fjG(fj), a contradiction.
□
The usual ‘interval halving’ proof (going back to Cousin in [17]) establishes
the reversal, also using countable choice, in the theorem. We have the following
corollary, variations of which are published in [58–60], all involving diﬀerent proofs.
Corollary 4.24. The system ACAω
0 + IND + QF-AC1,1 + HBU proves ATR0.
Proof. The schema (4.9) for L2-formulas ϕi ∈Σ1
1 is called Σ1
1-separation and equiv-
alent to ATR0 by [82, V.5.1]. This separation axiom immediately follows from (∃2)
and Σ-SEP, and hence the theorem ﬁnishes the proof.
□


## Page 36


36
PLATO AND THE FOUNDATIONS OF MATHEMATICS
Thirdly, there is a straightforward generalisation of WKL, equivalent to HBU.
Remark 4.25 (Uniform theorems). Dag Normann and the author study the RM
and computability theory of uniform theorems in [63]. A theorem is uniform if
the objects claimed to exist by the theorem depend on few of its parameters. For
instance, the contraposition of WKL0, aka the fan theorem, expresses that a binary
tree with no paths must be ﬁnite. It is readily seen that the latter is equivalent to
the following sentence with the underlined quantiﬁers swapped:
(∀G2)(∃m0)(∀T ≤1 1)

(∀α ∈C)(αG(α) ̸∈T) →(∀β ∈C)(βm ̸∈T)

.
(WKLu)
Note that WKLu expresses that a binary tree T is ﬁnite if it has no paths, and
the upper bound m only depends on a realiser G of ‘T has no paths’. For this
reason, WKLu is called uniform weak K¨onig’s lemma.
It is easy to show that
WKLu ↔HBU by adapting the proof of [58, Theorem 4.6]. It goes without saying
that most theorems from the RM of WKL0 have uniform versions that are equivalent
to HBU. For instance, uniform versions of the Pincherle, Heine, and Fej`er theorems
are studied in [63]. Moreover, as documented in [63, Appendix A], many proofs
from the literature actually establish the uniform version of the theorem at hand,
including the ﬁrst proof of Heine’s theorem in Stillwell’s introduction to RM ([85]).
Finally, the original K¨onig’s lemma (see e.g. [82, III.7]) can be given a similar
‘uniform’ treatment, something worthy of future study.
Fourth, WKL is equivalent to the Cantor intersection theorem for RM codes of
closed sets, even constructively (see e.g. [37]).
As a further litmus test for our
notion of closed set, we show in Theorem 4.27 that the Cantor intersection theorem
for closed sets is equivalent to HBU. Note that ECF yields the original equivalence
as QF-AC1,1 is translated to a triviality.
Deﬁnition 4.26. [CIT] Let Cn be a sequence of closed sets such that ∅̸= Cn+1 ⊆
Cn ⊆[0, 1]. Then ∩n∈NCn ̸= ∅.
Note that the contraposition of CIT is a version of the Heine-Borel theorem for
countable covers consisting of open sets.
Theorem 4.27. The system RCAω
0 + QF-AC1,1 proves HBU ↔CIT.
Proof. In case ¬(∃2), the usual second-order proofs go through. Indeed, all func-
tions on R are continuous by [42, §3] and HBU reduces to the Heine-Borel theorem
for the unit interval and countable covers, which is just WKL by [82, IV.1]. Similarly,
closed sets become RM-closed sets. We shall now prove the equivalence assuming
(∃2), and the law of excluded middle ﬁnishes the proof.
For the reverse direction, ﬁx Ψ : I →R+ and apply QF-AC1,0 to the formula
(∀x ∈I)(∃n0)(|IΨ
x | >
1
2n+1 ), we obtain Φ : I →Q
+ such that a ﬁnite sub-cover of
∪x∈IIΦ
x is also a ﬁnite sub-cover of ∪x∈IIΨ
x . In other words, we may restrict HBU
to functionals I →Q
+. Now suppose HBU is false for Ψ : I →Q+ and deﬁne the
open set On as follows using ∃2: x ∈On if and only if
(∃y ∈R)(x ∈I ∧x ∈IΨ
y ∧|IΨ
y | >R
1
2n ).
One readily obtains a deﬁnition of On as in Deﬁnition 4.2. Note that On ⊆On+1
and deﬁne the closed set Cn as the complement of On. By our assumption ¬HBU,
Cn ̸= ∅for any n. Applying CIT, there is x0 ∈∩n∈NCn. However, since x0 ∈IΨ
x0,


## Page 37


PLATO AND THE FOUNDATIONS OF MATHEMATICS
37
we have x0 ∈On0 in case |IΨ
x0| ≥
1
2n0 , a contradiction. Hence HBU must hold for
Ψ, in this case, and the reverse direction is done.
For the forward direction, let Cn be as in CIT, i.e. Cn is the complement of On =
∪y∈RIΨn
y
for some sequence Ψn : (R×N) →R. Now suppose (∀x ∈I)(∃n0)(x ̸∈Cn),
i.e. (∀x ∈I)(∃n0, y ∈R)(x ∈IΨn
y
). We may apply QF-AC1,1 to obtain Φ such that
(∀x ∈I)(x ∈I
ΨΦ(x)(1)
Φ(x)(2) ). Thus, ∪x∈II
ΨΦ(x)(1)
Φ(x)(2)
covers the unit interval and apply
HBU to ﬁnd a ﬁnite sub-cover, i.e. y0, . . . yk ∈I such that [0, 1] ⊂∪i≤kI
ΨΦ(yi)(1)
Φ(yi)(2) .
However, this implies [0, 1] ⊂∪i≤k0Oi for k0 := maxi≤k Φ(yi)(1) and Ck0+1 must
be empty, a contradiction. Hence, HBU →CIT follows, and we are done.
□
The use of the axiom of choice in Theorems 4.23 and 4.27 is somewhat unsatis-
factory. This shall be remedied in Section 5.
Sixth, we recall some results from [60,62,74] that complete Figure 2.
Remark 4.28 (Gauge integral). The gauge integral is a generalisation of the
Lebesgue and (improper) Riemann integral ([86]); it was introduced by Denjoy
(in a diﬀerent from) around 1912 and studied by Lusin, Perron, Henstock, and
Kurzweil. The latter two pioneered the modern formulation of the gauge integral
as the Riemann integral with the constant ‘delta’ from the usual ‘epsilon-delta’ deﬁ-
nition replaced by a function. The gauge integral boasts the most general version of
the fundamental theorem of calculus and is ‘maximally’ closed under improper in-
tegrals as in Hake’s theorem (see [5,6]). The gauge integral also provides a unique
and direct formalisation of Feyman’s path integral (see [54–57, 67]). Many basic
properties of the gauge integral, including the aforementioned theorems, are equiv-
alent to HBU, as shown in [60, 61]. Applying ECF to these results, one obtains
equivalences between WKL and theorems pertaining to the Riemann integral, as
gauge integrals are just Riemann integrals if all functions are continuous.
Remark 4.29 (Dini’s theorem). Dini’s theorem is equivalent to WKL, as shown
in [9, 10]. Dini’s theorem for nets is verbatim the same theorem except for the
replacement of ‘sequence’ by ‘net’. Dini’s theorem for nets is equivalent to HBU, as
shown in [74, §3.2.1].
Finally, ECF maps the Plato hierarchy from Figure 2 to the G¨odel hierarchy.
Now, ECF replaces higher-order objects by RM codes, continuous by deﬁnition.
For this reason, the existence of discontinuous functions as in (∃2) is mapped to
0 = 1 by ECF. By contrast, ECF interprets BOOT and HBU as quite meaningful
theorems. For this reason, it seemed obvious to us that BOOT and HBU should be
equivalent to certain continuity axioms. We explore this idea in the next section.
5. Main results III: continuity and neighourhoods
5.1. Introduction. In this section, we provide a formulation of the Plato hierar-
chy based on continuity. In particular, we show that BOOT, HBU, and related
principles are equivalent to fragments of a certain continuity axiom schema stem-
ming from intuitionistic analysis, called special bar/Brouwer continuity SBC in [43]
and neighbourhood function principle NFP in [91]. The latter is classically true and
connects axioms central to Brouwer’s intuitionistic mathematics (see [43,90,91]).
Our results should be contrasted with Kohlenbach’s approach from [42] based
on discontinuous functions like ∃2 and the Suslin functional. Indeed, ECF converts


## Page 38


38
PLATO AND THE FOUNDATIONS OF MATHEMATICS
the existence of a discontinuous function like ∃2 to 0 = 1, while BOOT is converted
to ACA0; in other words, it is to almost expected that BOOT has a formulation
in terms of continuity. In this light, Kohlenbach approach yields a discontinuity
hierarchy, while the Plato hierarchy is a continuity hierarchy and can be said to be
a ‘return to Brouwer’ in the aforementioned sense.
A conceptual motivation for the study of NFP is provided by the very aim of RM
itself, namely to ﬁnd the minimal (set existence) axioms needed to prove theorems
of ordinary mathematics. Now, Heine-Borel compactness (and related principles
like the Lindel¨of property) cannot be captured (well or at all) by higher-order
comprehension. Indeed, one of the main results in [60, 63] is that Zω
2 + QF-AC0,1
cannot prove HBU (and related principles like the Lindel¨of lemma), while ZΩ
2 of
course can; the ﬁrst-order strength of these systems is however massive compared
to HBU, i.e. anything remotely related to an equivalence is oﬀthe table. By contrast,
the continuity schema NFP will be seen to yield elegant equivalences.
Finally, as part of this study, we suggest new axioms to be added to the base
theory of higher-order RM, as discussed in Section 5.2.
One advantage is that
these new axioms readily equip continuous functionals on Baire space with RM-
codes, a topic studied by Kohlenbach in [41, §4]. It should be noted that the base
theory RCA0 contains weak comprehension axioms, i.e. it is only natural that the
RM-study of NFP also requires weak fragments of the latter in the base theory.
5.2. New axioms and some motivation. We introduce the new axioms Ai in
Section 5.2.1; we show in Section 5.3 that these axioms yield many elegant equiv-
alences, e.g. involving NFP. In particular, these new axioms obviate the use of the
Axiom of Choice in some of our above proofs. An overview of the arguments for
the extension of RCAω
0 with these axioms is found in Section 5.2.2.
5.2.1. The new axioms Ai. The development of RM starts with the deﬁnition of a
good base theory. So far, we have mostly used Kohlenbach’s RCAω
0 plus countable
choice. Nonetheless, Theorems 4.23 and 4.27 seem to need more choice, namely
QF-AC1,1, and it is a natural question whether these results also go through in ZF,
or even a suitable weak extension of RCAω
0 not involving (countable) choice.
In this section, we formulate such a weak extension and show that it yields
numerous elegant equivalences involving fragments of NFP, including the promised
‘choice-free’ improvement of Theorems 4.23 and 4.27. Other arguments in favour
of our new axioms Ai are in Section 5.2.2. We ﬁrst introduce the axiom schema
NFP, which intuitively speaking expresses that if there could be a continuous choice
functional (the antecedent of (5.1)), then there is one given by an associate (the
consequent of (5.1)).
Deﬁnition 5.1. [NFP] For any A(σ0∗) in Lω, we have
(∀f 1)(∃n0)A(fn) →(∃γ ∈K0)(∀f 1)A(fγ(f)),
(5.1)
where ‘γ ∈K0’ means that γ1 is a total associate on Baire space.
The schema NFP was used in [60] to obtain the Lindel¨of lemma inside ZΩ
2 +QF-AC0,1;
it was also proved in [74] that NFP →MCT[0,1]
net
→HBU over RCAω
0 .
Intuitively speaking, our new axioms Ai shall be a generalisation of QF-AC1,0 to
the following formula classes.


## Page 39


PLATO AND THE FOUNDATIONS OF MATHEMATICS
39
Deﬁnition 5.2. [Ci-formulas]
• A C0-formula A has the following form: A(n) ≡(∃f ∈2N)(Y (f, n0) = 0).
• A C1-formula A has the following form: A(n) ≡(∀f ∈2N)(Y (f, n0) = 0).
• A C2-formula A has the following form:
A(n) ≡(∃f ∈2N)(Y (f, n0) = 0) ∨(∀g ∈2N)(Z(g, n0) = 0).
Note that Ci-formulas can have parameters besides the number variable. Our new
axioms Ai are deﬁned as the following fragments of NFP. Note that the choice
functional in Ai need not be continuous, in contrast to NFP.
Deﬁnition 5.3. [Ai] For any Ci-formula A(σ0∗), we have
(∀f 1)(∃n0)A(fn) →(∃Φ2)(∀f 1)A(fΦ(f))
Besides its fruitful consequences listed below, there are good conceptual mo-
tivations for the previous axioms, as discussed in the next section. One ‘trivial’
argument is that (second-order) RM gauges the strength of theorems in terms of
set existence axioms; to this end, the base theory RCA0 contains a weak set exis-
tence axiom. Thus, if we are to develop RM based on NFP, it stands to reason that
our base theory should include some fragment of NFP.
5.2.2. Motivation for the Ai axioms. We discuss some of the arguments in favour
of a base theory that includes the new axioms Ai.
First of all, the equivalence [BOOT]ECF ↔ACA0 clearly suggests that one exis-
tential quantiﬁer over NN in BOOT gives rise to a numerical quantiﬁer under ECF.
Hence, one existential quantiﬁer over 2N should amount to (almost) the same as
quantiﬁer-free under ECF, as also suggested by Theorem 5.9.
In this light, the
axioms Ai yield an inconsequential extension of QF-AC1,0, included in RCAω
0 .
Secondly, HBU is formulated with a rather ‘eﬀective’ kind of cover, namely where
each x ∈I is covered by IΨ
x for Ψ : I →R+, which is exactly the deﬁnition used by
Cousin and Lindel¨of ([17, 46]). A generalisation of HBU to (more) general covers,
is studied in [71] as follows: the principle HBT deals with covers in which only
(∀x ∈I)(∃y ∈I)(x ∈Iψ
y ) is assumed for ψ : I →R, i.e. Iψ
x can be empty. One can
prove HBU ↔HBT over RCAω
0 +IND+A0 by [71, §3.5]. Similar results hold for the
Lindel¨of lemma and other basic topological theorems, i.e. A0 seems essential for an
elegant development of the RM of topology.
Thirdly, A1 readily implies the following ‘coding principle’: any Y 2 that is contin-
uous on 2N, has a continuous modulus of continuity on 2N, and hence an RM-code
by [41, Prop. 4.4]. Indeed, consider (∃2) ∨¬(∃2) and note that in the former case,
[41, Prop. 4.4 and 4.7] provides the required modulus (and RM code). In the latter
case, apply A1 to (5.2), where the underlined formula is a C1-formula:
(∀f ∈2N)(∃N 0)(∀g ∈2N)(fN = gN →Y (fN ∗00 . . . ) = Y (g)),
(5.2)
and note that the resulting Φ2 is continuous by [42, §3]. The study of the aforemen-
tioned coding principle in [41, §4] suggests that the RM of WKL does not change
upon the replacement of continuous functions by RM-codes; we show in [77] that
the RM of Tietze’s extension theorem and Ekeland’s variational principle (which
involves WKL0) does greatly depend upon coding.


## Page 40


40
PLATO AND THE FOUNDATIONS OF MATHEMATICS
Fourth, Pincherle’s theorem states that a locally bounded functional on 2N is
bounded; consider the following version, called PIT′
o in [63]:
(∀F 2)

(∀f ∈C)(∃n0)(∀g ∈C)

g ∈[fn] →F(g) ≤n

→(∃m0)(∀h ∈C)(F(h) ≤m)

.
It seems that the only way to prove HBU →PIT′
o is to apply A1 to the antecedent
and apply HBU to the canonical cover associated to the resulting Φ2. In general,
moduli are an important part of constructive and computational approaches to
mathematics, and A1 conveniently always seems to provide those.
Fifth, recall ∆-comprehension from Section 3.2.3, which plays an important role
in lifting proofs from second- to higher-order arithmetic. Indeed, the recursive coun-
terexample involving Specker sequences can be lifted to higher-order arithmetic by
Theorem 3.19, assuming ∆-comprehension; the latter plus WKL is also equivalent
to the separation of ranges of non-overlapping type two functionals (see [75, 76]).
Theorem 5.17 shows that RCAω
0 + IND + A0 proves ∆-comprehension.
Sixth, Kohlenbach studies generalisations of WKL to certain formula classes in
[41, §3]. Since [HBU]ECF is just WKL, it is a natural question whether there is a
generalisation of WKL that is equivalent to HBU. By Corollary 5.15, A0 suﬃces to
obtain an elegant such equivalence.
5.3. Some consequences of the Ai axioms. We use the new axioms Ai to obtain
some elegant equivalences involving BOOT, HBU, and related principles on one
hand, and fragments of NFP on the other hand.
First of all, we introduce the new formula class ‘Σ∨Π’. Now, the formula class
‘Σ0
1∧Π0
1’ is used in RM (see [82, VI.5]) to study fragments of the axiom of determi-
nacy from set theory. The formula class ‘Π0
1 ∨Σ0
1’ is mentioned in the title of [2]. A
formula of the form ‘(∃f 1)(Y (f, n) = 0)’ as in BOOT is called a ‘Σ-formula’, while
its negation is called a ‘Π-formula’. The formula class ‘Σ∨Π’ consists of disjunctions
‘S ∨P’ with S ∈Σ and P ∈Π.
Now let Σ∨Π-NFP be NFP restricted to Σ∨Π-formulas and let NFP0 be NFP with
‘(∃γ ∈K0)A(fγ(f))’ replaced by ‘(∃Φ2)A(fΦ(f))’, and the same for fragments.
The following theorem should be contrasted with the fact that comprehension does
not capture HBU or BOOT well7 at all.
Theorem 5.4. RCAω
0 + IND proves Σ∨Π-NFP ↔BOOT ↔[Σ ∨Π-NFP0 + HBU].
Proof. A proof of BOOT →Σ∨Π-NFP is as follows: BOOT replaces Σ∨Π-formulas
by equivalent quantiﬁer-free ones. Then QF-AC1,0 yields a (continuous) functional
G2 such that G(f) is the least n as in (∀f 1)(∃n0)A(fn). An RM-code for G2 is
then found as in [41, §4] using ACA0.
To prove the ﬁrst forward implication, IND implies that for any n0, there is a
ﬁnite binary sequence σ such that
(∀m ≤n)(σ(m) = 1 ↔(∃f 1)(Y (f, m) = 0)),
(5.3)
i.e. a kind of ‘ﬁnite comprehension’ principle. Suppose BOOT is false for Y 2
0 , i.e.
(∀X ⊂N)(∃n ∈N)

(n ∈X ∧(∀g1)(Y0(g, n) > 0)) ∨(n ̸∈X ∧(∃h1)(Y0(h, n) = 0))

.
7The system Zω
2 + QF-AC0,1 cannot prove BOOT or HBU, while ZΩ
2 can ([60, 63]). However,
the latter has the ﬁrst-order strength of Z2, while RCAω
0 + BOOT is conservative over ACA0.


## Page 41


PLATO AND THE FOUNDATIONS OF MATHEMATICS
41
Observe that the content of X beyond the number n is irrelevant for the previous
formula in square brackets. Now deﬁne the Σ∨Π-formula A(σ) as follows:
σ(|σ| −1) = 1 ∧(∀g1)(Y0(g, |σ| −1) > 0)
∨
σ(|σ| −1) = 0 ∧(∃h1)(Y0(h, |σ| −1) = 0).
Let B(σ) be A(˜σ), where ˜σ(n) = 1 if σ(n) > 0, and zero otherwise, for n < |σ|.
By assumption, we have (∀f 1)(∃n0)B(fn). Apply Σ∨Π-NFP and obtain an upper
bound for the resulting RM-code on Cantor space (using WKL0 by [82, IV.2]).
However, this upper bound contradicts (5.3) for large enough n.
To prove the second forward implication, proceed as in the previous part of the
proof: apply Σ∨Π-NFP0 to (∀f 1)(∃n0)B(fn) and let Φ be the resulting functional.
Obtain a ﬁnite sub-cover for the associated canonical cover ∪f∈2N[fΦ(f)] using
HBU. This provides an upper-bound that contradicts (5.3) for large enough n.
□
The theorem is not an isolated case: inspired by [82, V.5.2], Σ-TR is equivalent to
comprehension for Σ ∧Π-formulas ϕ(i, X) with continuous second-order parameter
as in Σ-TR and satisfying (∀i ∈N)(∃at most one X ⊆N)ϕ(i, X). The related
statement for trees in [82, V.5.2] can also be generalised, similar to Ci-WKL below.
Secondly, we obtain an equivalence result for the Lindel¨of lemma for NN and
NFP restricted to Σ-formulas. Note that the Lindel¨of lemma is studied in detail in
[60,63], including a version that implies countable choice as in QF-AC0,1. The ﬁnal
part of LIND(NN) indeed invites the application of the latter.
Deﬁnition 5.5. [LIND(NN)] For every G2, there is a sequence σ0→0∗
n
covering NN
such that (∀n ∈N)(∃f ∈NN)(σn =0∗fG(f)).
Let Σ-NFP be NFP restricted to Σ-formulas. The following theorem should be
contrasted with the fact that comprehension does not capture LIND(NN) well8.
Theorem 5.6. The system RCAω
0 + A0 proves LIN(NN) ↔Σ-NFP.
Proof. For the reverse implication, consider A(σ) deﬁned as follows:
(∃g1)

G(g) =0 |σ| −1 ∧σ =0∗gG(g)

,
(5.4)
We have (∀f ∈NN)(∃n0)A(fn) since we may take g = f and n = G(f). Apply
Σ-NFP to obtain (∀f ∈NN)A(fγ(f)) for some γ ∈K0. The sequence required by
LIND(NN) is given by σγ(σ ∗00 . . . ) for all σ0∗such that γ(σ ∗00 . . . ) ≥|σ| −1,
which can be formed in RCAω
0
For the forward direction, in case ¬(∃2), Σ-NFP and LIND(NN) are outright
provable as all functions on Baire space are continuous by [42, §3]. In case (∃2),
we may replace quantiﬁcation over 2N by quantiﬁcation over NN as in the proof
of Theorem 4.11.
Hence, the antecedent of Σ-NFP reduces to (∀f 1)(∃n0, g ∈
2N)(Y (g, fn) = 0). Now apply A0 to obtain Φ2 such that (∀f 1)(∃g ∈2N)(Y (g, fΦ(f)) =
0). Let σ0→0∗
n
be the sequence obtained from applying LIND(NN) to ∪f∈NN[fΦ(f)].
Then apply QF-AC1,0 to (∀f 1)(∃n0)(f ∈[σn]) and obtain (continuous by deﬁnition)
Ψ2 which produces the least such n0. Finally deﬁne Z2 as follows: Z(f) := |σΨ(f)|
8The system Zω
2 + QF-AC0,1 cannot prove LIND(NN), while ZΩ
2 + QF-AC0,1 can. However, the
latter has the ﬁrst-order strength of Z2, while RCAω
0 + LIND(NN) is conservative over RCA0.


## Page 42


42
PLATO AND THE FOUNDATIONS OF MATHEMATICS
and note that by [41, §4], this continuous function has an associate γ ∈K0. The
latter is as required by Σ-NFP, and we are done.
□
Let Σ-NFP↾C be Σ-NFP with all quantiﬁers over NN restricted to 2N. One then
proves the following corollary in the same way (also with IND replaced by QF-AC0,1).
Corollary 5.7. The system RCAω
0 + IND + A0 proves HBU ↔[Σ-NFP↾C + WKL].
Thirdly, let BOOTw be BOOT with the quantiﬁer over NN restricted to 2N. We
have the following nice splitting for BOOT, while the same result for HBU does not
seem to follow without additional axioms; this was the initial motivation for A1,
which yields an equivalence in the ﬁnal part by Corollary 5.10.
Theorem 5.8. The system RCAω
0 proves [ACA0 + BOOTw] ↔BOOT; RCAω
0 + IND
and RCAω
0 + QF-AC0,1 both prove [WKL + BOOTw] →HBU.
Proof. The ﬁrst reverse implication is immediate. The ﬁrst forward implication is
immediate in case ¬(∃2), as BOOT reduces to ACA0. In case (∃2), (∃f 1)(Y (f, n) =
0) can be equivalently written as (∃X ⊂N2)(Y (F(X), n) = 0) where F(X)(k) :=
λk.(µm0)((k, m) ∈X). Clearly, BOOTw applies to this equivalent formula.
For the ﬁnal implication, we prove HBUc. Fix G2 and let A(σ) be the following:
(∃g ∈C)

G(g) ≤|σ| ∧σ ∗00 · · · ∈[gG(g)]

,
(5.5)
where σ0∗is a ﬁnite sequence of natural numbers. Note that the formula in (5.5)
in square brackets is quantiﬁer-free. Thus, BOOTw provides a set X ⊆N such that
(∀σ0∗)(σ ∈X ↔A(σ)), with minimal coding. Now, we have (∀f ∈C)(∃n0)A(fn)
since we may take g = f and n = G(f). Hence, we have (∀f ∈C)(∃n0)(fn ∈X)
and applying QF-AC1,0, there is H2 such that (∀f ∈C)(fH(f) ∈X) and H(f) is
the least such number. Obviously H2 is continuous on C and hence bounded above
on C by [41, §4]. Hence, there is N 0
0 such that (∀f ∈C)(∃n ≤N0)A(fn). Now
obtain the ﬁnite sub-cover as in the proof of Theorem 4.21.
□
One readily adapts the ﬁnal part of the proof to [WWKL + BOOTw] →WHBU,
where the latter captures (the essence of) the Vitali covering theorem for uncount-
able covers, as studied at length in [62].
Clearly, BOOTw readily generalises to more general formulas only involving quan-
tiﬁers over Cantor space. The following theorem implies that such formulas can
‘almost’ be treated as quantiﬁer-free.
Theorem 5.9. The system WKL0 proves [BOOTw]ECF and [A2]ECF.
Proof. Let MUC be the intuitionistic fan functional from [42, §3] as deﬁned in
Remark 4.8. The system RCAω
0 + MUC readily proves BOOTw and A1. By [47,
p. 497], ECF converts MUC into WKL.
□
As promised, A2 yields an equivalence in the ﬁnal part of Theorem 5.8.
Corollary 5.10. RCAω
0 + IND proves [WKL + BOOTw] ↔[HBU + A2].
Proof. We ﬁrst prove the reverse implication. To this end, suppose ¬BOOTw, i.e.
there is Y 2
0 such that for all X ⊆N, there is n ∈N such that

[n ∈X ∧(∀f ∈C)(Y0(f, n) ̸= 0)] ∨[(∃g ∈C)(Y0(g, n) = 0) ∧n ̸∈X]

.
(5.6)


## Page 43


PLATO AND THE FOUNDATIONS OF MATHEMATICS
43
Let A(Xn) be the formula in (5.6) (modulo minimal modiﬁcation).
Clearly, A
is a C2-formula and A2 yields Φ2 such that (∀X ⊆N)A(XΦ(X)). Apply HBUc
for the canonical cover associated to Φ.
The resulting ﬁnite sub-cover provides
an upper bound k0 such that (∀X ⊆N)(∃n ≤k0)A(Xn). However, IND proves
‘ﬁnite comprehension’ for any C2-formula, and HBU →BOOTw follows. For the
forward implication, note that for any C2-formula A(σ0∗), there is X ⊂N such that
σ ∈X ↔A(σ) by BOOTw. Now apply QF-AC1,0 to (∀f 1)(∃n0)A(fn).
□
The previous splitting provides a nice motivation for A2, but there are other
arguments in favour of the latter: we now use this axiom to show that HBU is
equivalent to weak K¨onig’s lemma generalised to binary trees where elementhood
in the tree is given by a C1-formula. As to prior art, Kohlenbach studies similar
generalisations of weak K¨onig’s lemma in [41, §3].
Deﬁnition 5.11. [Ci-tree] We say that a Ci-formula A(σ0∗), is (or: represents)
a ‘Ci-tree T’ if the formula σ0∗∈T ≡¬A(σ) satisﬁes the usual tree property,
i.e. σ ∈T →τ ∈T for any initial segment τ of σ.
A Ci-tree T is inﬁnite if
(∀n0)(∃σ0∗)(|σ| = n ∧σ ∈T) and f 1 is a path in a Ci-tree T is (∀n0)(fn ∈T).
Deﬁnition 5.12. [Ci-WKL] Any inﬁnite binary Ci-tree has a path.
The ECF-translation of Ci-WKL is WKL by the following and Remark 1.1.
Theorem 5.13. For i = 0, 1, 2, RCA0 proves WKL ↔[Ci-WKL]ECF.
Proof. By [47, p. 497], WKL is equivalent to the ECF-translation of the intuitionistic
fan functional as in MUC. The latter reduces ﬁnding f ∈2N satisfying (Y (f, σ) >0
0) to a ﬁnite search, i.e. elementhood in C2-trees is decidable, reducing it to usual
WKL. Alternatively, MUC readily implies comprehension for C2-formulas, and the
ECF-interpretation of the former is just WKL.
□
At the risk of pedantry (and repetition by Remark 1.1), identifying continuous
functions and their codes is second nature in RM. In this light, there is no diﬀer-
ence between C1-trees (under ECF) and ‘normal’ trees in second-order arithmetic
(assuming WKL), i.e. [C1-WKL]ECF is just WKL if we are identifying continuous
functions and their codes; our identiﬁcation however goes in the ‘reverse’ direction.
Theorem 5.14. The systems RCAω
0 + QF-AC0,1 and RCAω
0 + IND both prove the
implication C1-WKL →HBU.
Proof. Fix G2 and deﬁne the formula A(σ) as (5.5). Clearly, A(σ) →A(τ) for
ﬁnite binary sequences σ, τ where σ is an initial segment of τ. In this light, the
formula ¬A(σ) deﬁnes a C1-tree T. Note that (∀f ∈2N)(∃n0)A(fn) by considering
g = f and n = G(f). Apply C1-WKL to (∀f ∈2N)(∃n0)(fn ̸∈T) to conclude
(∀f ∈2N)(∃n0 ≤n0)(fn ̸∈T) for some n0. Hence, HBU for G2 follows as in the
proof of Theorem 5.8.
□
Corollary 5.15. The system RCAω
0 + IND + A0 proves HBU ↔C1-WKL.
Proof. Apply A0 to (∀f ∈C)(∃n0)(fn ̸∈T) and apply HBU to the (canonical cover
for the) resulting functional Φ2. The resulting ﬁnite sub-cover readily provides the
bound required by C1-WKL.
□


## Page 44


44
PLATO AND THE FOUNDATIONS OF MATHEMATICS
The contraposition of C1-WKL can be interpreted as a version of the Heine-Borel
theorem for countable covers of closed sets as in the previous section. We establish
the following where C1-NFP is NFP restricted to C1-formulas.
Theorem 5.16. The system RCAω
0 + IND proves the following:
[WKL + BOOTw] ↔[HBU + A2] ↔C2-WKL ↔[WKL + C1-NFP].
(5.7)
Proof. The ﬁrst equivalence is given by Corolary 5.10. For the second equivalence,
we only need to prove C2-WKL →BOOTw. Now assume (∃2) and deﬁne:
A(σ0∗) ≡(∀i < |σ|)

σ(i) = 0 ↔(∃f ∈2N)(Y (f, i) = 0)

.
With minor modiﬁcation (using ∃2), this formula yields a binary C2-tree called
T. Using IND to establish ‘ﬁnite comprehension’ for C2-formulas, the C2-tree T is
inﬁnite. A path through T then immediately yields the required instance of BOOTw.
In case ¬(∃2), one uses (the proof of) [41, Prop. 4.10] to replace all (continuous)
functionals by RM-codes on 2N. The equivalence between WKL and [MUC]ECF from
[47, p. 497] and the implication MUC →BOOTw then ﬁnish this part.
The implication [WKL + BOOTw] →C1-NFP follows from the ﬁnal part of the
proof of Corollary 5.10 by noting that the function Φ2 from QF-AC1,0 can be taken
to be continuous in this case.
The associated associate has a trivial deﬁnition
(thanks to BOOTw).
Finally, the implication [WKL + C1-NFP] →HBU readily
follows as in the proof of Theorem 5.8 by noting that (5.5) is a C1-formula.
□
As to similar results, we could obtain equivalences involving MCT−
net from Re-
mark 4.8. Moreover, ACA0 is equivalent to K¨onig’s lemma (see [82, III.7]), and one
can also obtain an equivalent between the latter for Σ∨Π-formulas and BOOT. It
goes without saying that certain implications from (5.7) can also be obtained for
WWKL and WHBU (see [62] and [82, X.1]).
Next, we prove that ∆-comprehension indeed follows from A0.
Theorem 5.17. The system RCAω
0 + IND + A0 proves ∆-comprehension.
Proof. In case ¬(∃2), all functions on NN are continuous by [42, Prop. 3.4], and
∆-comprehension reduces to ∆0
1-comprehension. In case (∃2), we may replace in
∆-comprehension the quantiﬁers over NN by quantiﬁers over C as in the proof
of Theorem 4.11. Now suppose there are Y 2
0 , Z2
0 satisfying the antecedent of ∆-
comprehension such that for all X ⊆N, there is n ∈N such that

[n ∈X ∧(∀f ∈C)(Y0(f, n) ̸= 0)] ∨[(∃g ∈C)(Y0(g, n) = 0) ∧n ̸∈X]

,
(5.8)
and denote by A(Xn) the formula (5.8) (modulo the usual modiﬁcation).
At
ﬁrst glance, A(σ0∗) is a C2-formula, but since Y0, Z0 satisfy the antecedent of ∆-
comprehension, (5.8) is in fact in C0 and so is the formula B(σ) ≡[A(σ) ∧(∀i <
|σ| −1)¬A(σi)], which is readily proved using IND.
Again using IND, (∀X ⊆
N)(∃n0)A(Xn) implies (∀X ⊆N)(∃n0)B(Xn), and applying A0 yields a continu-
ous Φ2, by the deﬁnition of B. Now, Φ2 has an upper bound on C by WKL, and
this yields a contradiction as IND proves ‘ﬁnite comprehension’ (5.3).
□
We note in passing that HBU deals with uncountable covers, while WKL (up to
coding as in [82, IV.1]) deals with countable covers, and never the twain shall meet:
the logical hardness of the former is dwarfed by the latter (see [60, 63]). Despite
this huge diﬀerence, a slight generalisation of the scope of A2, namely closure under


## Page 45


PLATO AND THE FOUNDATIONS OF MATHEMATICS
45
∧, ¬, →, yields an axiom that establishes an equivalence between WKL and HBU,
based on the previous proof.
Finally, as promised, we obtain improved versions of Theorems 4.23 and 4.27.
Theorem 5.18. The system RCAω
0 + A0 proves HBU ↔CIT.
Proof. The equivalence amounts to the associated second-order result (see [37])
in case ¬(∃2). In case (∃2), we may replace the use of QF-AC1,1 in the proof of
Theorem 4.27 by A0, as Σ-formulas can now be written as C0-formulas as in the
ﬁrst part of the proof of Theorem 5.8. Note that since Cn is a sequence of closed
Π-sets, the formula (∀x ∈I)(∃n0)(x ̸∈Cn) implies (∀x ∈I)(∃m0)([x](m) ̸∈Cm) as
the complement is open and Cn+1 ⊆Cn.
□
Corollary 5.19. The system RCAω
0 + IND + A0 proves HBU →Σ-SEP.
Proof. As in the proof of the theorem, the use of QF-AC1,1 in the proof of Theo-
rem 4.23 is replaced by A1.
□
In light of the results obtained in this section, as well as the attendant discussion,
a base theory for higher-order RM as in the Plato hierarchy should include at least
A0 in addition to QF-AC1,0 to be found in RCAω
0 . However, A2 also makes HBU
‘much more explosive’: while ACAω
0 +HBU seems to prove no second-order theorem
beyond ATR0 (see [60,62]), adding A1 immediately results in Π1
1-CA0 by (5.7). This
is however unproblematic as the Plato hierarchy is intended to yield the G¨odel
hierarchy under ECF, i.e. no fragment of the former hierarchy implies the existence
of discontinuous functions, as ECF translates such fragments to ‘0 = 1’.
Acknowledgement 5.20. We thank Dag Normann, Adrian Mathias, Thomas
Streicher, Pat Muldowney, and Anil Nerode for their valuable advice. Our research
was supported by the John Templeton Foundation via the grant a new dawn of intu-
itionism with ID 60842 and by the Deutsche Forschungsgemeinschaft via the DFG
grant SA3418/1-1. Opinions expressed in this paper do not necessarily reﬂect those
of the John Templeton Foundation. The results in Section 4 were completed during
the stimulating BIRS workshop (19w5111) on Reverse Mathematics at CMO, Oax-
aca, Mexico in Sept. 2019. We express our gratitude towards the aforementioned
institutions. Results in Appendix A are due to myself and Dag Normann.
Appendix A. Other reflections of the Big Five
After the completion of this paper and [64, 65], it was noticed that the results
in the latter two papers also give rise to ‘reﬂections’ similar to (but diﬀerent from)
Figure 2. We sketch these results in this section for completeness.
For this section, we stress that the concept of ‘open set’ used in [64] is diﬀerent
from the one in this paper. Open sets are namely represented in [64] via charac-
teristic functions, yielding Figure 4 as below. We ﬁrst discuss some deﬁnitions as
follows.
(i) Open sets in R are represented in [64] by Y : R →R where ‘x ∈Y ’ is
|Y (x)| >R 0 and satisﬁes (∀x ∈Y )(∃r >R 0)(B(x, r) ⊂Y ). Closed sets are
the complement of open sets.
(ii) HBC expresses that countable open covers of closed sets (as in item (i)) in
the unit interval have ﬁnite sub-covers.
(iii) CLO expresses that a closed set (as in item (i)) in the unit interval is located.


## Page 46


46
PLATO AND THE FOUNDATIONS OF MATHEMATICS
(iv) CLOrm expresses that an RM-closed set in the unit interval is located.
(v) open expresses that an open set (as in item (i)) has an RM-code, and is
equivalent to the Urysohn lemma for closed sets (as in item (i)).
We chose item (i) as the deﬁnition of open set in [64] as it reduces to the usual RM-
deﬁnition under ECF and sequential compactness behaves as for the RM-deﬁnition;
elementhood in such open sets is also Σ0
1 with parameters. With the above in place,
the following picture emerges from [64]. We note that ECF converts the equiva-
lences on the right to those on the left.
6
RCA0
WKL0
CLOrm
ATR0
Π1
1-CA0
Π1
1-CA0 + open
proves ∆0
1-comprehension
↔countable Heine-Borel
↔a continuous function
on 2N is bounded
↔ACA0
↔perfect set theorem for
closed sets as countable unions
↔Cantor-Bendixson for
closed sets as countable unions
6
RCAω
0
WKL0
CLO
ATR0 + open
second-order arithmetic
higher-order arithmetic
plus QF-AC0,1
↔HBC
↔Pincherle’s theorem PITo
↔[ACA0 + open]
↔perfect set theorem for
closed sets as in item (i)
↔Cantor-Bendixson for
closed sets as in item (i)
←−
ECF
←−
ECF
Figure 4. Another higher-order hierarchy mapping to the Big Five
Clearly, Figure 4 is not as well-developed as Figure 2, but then the motivation
underlying [62] was never to obtain a hierarchy that yields the Big Five and equiv-
alences under ECF.
References
[1] Samson Abramsky and Achim Jung, Domain theory, Handbook of logic in computer science,
Vol. 3, Handb. Log. Comput. Sci., vol. 3, Oxford Univ. Press, 1994, pp. 1–168.
[2] Toshiyasu Arai, Epsilon substitution method for ID1(Π0
1 ∨Σ0
1), Ann. Pure Appl. Logic 121
(2003), no. 2-3, 163–208.
[3] Jeremy Avigad and Solomon Feferman, G¨odel’s functional (“Dialectica”) interpretation,
Handbook of proof theory, Stud. Logic Found. Math., vol. 137, 1998, pp. 337–405.
[4] Robert G. Bartle, Nets and ﬁlters in topology, Amer. Math. Monthly 62 (1955), 551–557.
[5]
, Return to the Riemann integral, Amer. Math. Monthly 103 (1996), no. 8.
[6]
, A modern theory of integration, Graduate Studies in Mathematics, vol. 32, American
Mathematical Society, 2001.
[7] Ralf Beckmann and Anton Deitmar, Two applications of nets, Ann. Funct. Anal. 6 (2015),
no. 3, 176–190.
[8] Paul Benacerraf and Hilary Putnam, Philosophy of Mathematics: Selected Readings, 2nd ed.,
Cambridge University Press, 1984.
[9] Josef Berger and Peter Schuster, Classifying Dini’s theorem, Notre Dame J. Formal Logic 47
(2006), no. 2, 253–262.


## Page 47


PLATO AND THE FOUNDATIONS OF MATHEMATICS
47
[10]
, Dini’s theorem in the light of reverse mathematics, Logicism, intuitionism, and for-
malism, Synth. Libr., vol. 341, Springer, 2009, pp. 153–166.
[11] Paul Bernays, Sur le Platonisme Dans les Math´ematiques, L’Enseignement Math´ematique
34 (1935), 52–69.
[12] Arlen Brown and Carl Pearcy, An introduction to analysis, Graduate Texts in Mathematics,
vol. 154, Springer, 1995.
[13] Douglas K. Brown, Notions of closed subsets of a complete separable metric space in weak
subsystems of second-order arithmetic, Logic and computation (Pittsburgh, PA, 1987), Con-
temp. Math., vol. 106, Amer. Math. Soc., Providence, RI, 1990, pp. 39–50.
[14]
, Notions of compactness in weak subsystems of second order arithmetic, Reverse
mathematics 2001, Lect. Notes Log., vol. 21, Assoc. Symbol. Logic, 2005, pp. 47–66.
[15] John P. Burgess, Fixing Frege, Princeton Monographs in Philosophy, Princeton University
Press, 2005.
[16] Samuel R. Buss, An introduction to proof theory, Handbook of proof theory, Stud. Logic
Found. Math., vol. 137, North-Holland, Amsterdam, 1998, pp. 1–78.
[17] Pierre Cousin, Sur les fonctions de n variables complexes, Acta Math. 19 (1895), 1–61.
[18] Solomon Feferman, How a Little Bit goes a Long Way: Predicative Foundations of Analysis,
2013. http://home.inf.unibe.ch/~ltg/em_bibliography/feferman13.pdf.
[19] Harvey Friedman, Some systems of second order arithmetic and their use, Proceedings of the
International Congress of Mathematicians (Vancouver, B. C., 1974), Vol. 1, 1975, pp. 235–242.
[20]
,
Systems of second order arithmetic with restricted induction, I & II (Abstracts),
Journal of Symbolic Logic 41 (1976), 557–559.
[21]
, Interpretations, According to Tarski, Interpretations of Set Theory in Discrete Math-
ematics and Informal Thinking, The Nineteenth Annual Tarski Lectures, http://u.osu.edu/
friedman.8/files/2014/01/Tarski1052407-13do0b2.pdf 1 (2007), pp. 42.
[22] Robin Gandy, General recursive functionals of ﬁnite type and hierarchies of functions, Ann.
Fac. Sci. Univ. Clermont-Ferrand No. 35 (1967), 5–24.
[23] G. Gierz, K. H. Hofmann, K. Keimel, J. D. Lawson, M. Mislove, and D. S. Scott, A com-
pendium of continuous lattices, Springer, 1980.
[24]
, Continuous lattices and domains, Encyclopedia of Mathematics and its Applications,
vol. 93, Cambridge University Press, 2003.
[25] Mariagnese Giusto and Stephen G. Simpson, Located sets and reverse mathematics, J. Sym-
bolic Logic 65 (2000), no. 3, 1451–1480.
[26] Kurt G¨odel, Collected works. Vol. III, Oxford University Press, 1995.
[27] Kurt G¨odel, On formally undecidable propositions of Principia Mathematica and related
systems. I, in: From Frege to G¨odel. A sourcebook in mathematical logic, 1879–1931, 1967,
pp. 592–617.
[28] Jean Goubault-Larrecq, Non-Hausdorﬀtopology and domain theory, New Mathematical
Monographs, vol. 22, Cambridge University Press, 2013.
[29] Lawrence M. Graves, The Theory of Functions of Real Variables, McGraw-Hill, 1946.
[30] Horst Herrlich, Axiom of choice, Lecture Notes in Mathematics, vol. 1876, Springer, 2006.
[31] David Hilbert, Mathematical problems, Bull. Amer. Math. Soc. (N.S.) 37 (2000), no. 4, 407–
436. Reprinted from Bull. Amer. Math. Soc. 8 (1902), 437–479.
[32]
, ¨Uber das Unendliche, Math. Ann. 95 (1926), no. 1, 161–190 (German).
[33] David Hilbert and Paul Bernays, Grundlagen der Mathematik. I, Zweite Auﬂage. Die
Grundlehren der mathematischen Wissenschaften, Band 40, Springer, 1968.
[34]
, Grundlagen der Mathematik. II, Zweite Auﬂage. Die Grundlehren der mathematis-
chen Wissenschaften, Band 50, Springer, 1970.
[35] Denis R. Hirschfeldt, Slicing the truth, Lecture Notes Series, Institute for Mathematical Sci-
ences, National University of Singapore, vol. 28, World Scientiﬁc Publishing, 2015.
[36] James Hunter, Higher-order reverse topology, ProQuest LLC, Ann Arbor, MI, 2008. Thesis
(Ph.D.)–The University of Wisconsin - Madison.
[37] Hajime Ishihara, Reverse mathematics in Bishop’s constructive mathematics, Philosophia
Scientiae (Cahier Sp´ecial) 6 (2006), 43-59.
[38] Thomas Jech, Set theory, Springer Monographs in Mathematics, Springer, 2003.
[39] John L. Kelley, General topology, Springer-Verlag, 1975. Reprint of the 1955 edition; Graduate
Texts in Mathematics, No. 27.


## Page 48


48
PLATO AND THE FOUNDATIONS OF MATHEMATICS
[40] Peter
Koellner,
Large
Cardinals
and
Determinacy,
The
Stanford
Encyclope-
dia
of
Philosophy,
2014.
https://plato.stanford.edu/archives/spr2014/entries/
large-cardinals-determinacy/.
[41] Ulrich Kohlenbach, Foundational and mathematical uses of higher types, Reﬂections on the
foundations of mathematics, Lect. Notes Log., vol. 15, ASL, 2002, pp. 92–116.
[42]
, Higher order reverse mathematics, Reverse mathematics 2001, Lect. Notes Log.,
vol. 21, ASL, 2005, pp. 281–295.
[43] G. Kreisel and A. S. Troelstra, Formal systems for some branches of intuitionistic analysis,
Ann. Math. Logic 1 (1970), 229–387.
[44] Alexander P. Kreuzer, The cohesive principle and the Bolzano-Weierstraßprinciple, MLQ
Math. Log. Q. 57 (2011), no. 3, 292–298.
[45] Solomon Leader, The Kurzweil-Henstock integral and its diﬀerentials, Monographs and Text-
books in Pure and Applied Mathematics, vol. 242, Marcel Dekker, Inc., New York, 2001. A
uniﬁed theory of integration on R and Rn.
[46] Ernst Lindel¨of, Sur Quelques Points De La Th´eorie Des Ensembles, Comptes Rendus (1903),
697–700.
[47] John Longley and Dag Normann, Higher-order Computability, Theory and Applications of
Computability, Springer, 2015.
[48] Antonio Montalb´an and Richard A. Shore, The limits of determinacy in second-order arith-
metic, Proc. Lond. Math. Soc. (3) 104 (2012), no. 2, 223–252.
[49] E. H. Moore, On a Form of General Analysis with Aplication to Linear Diﬀerential and
Integral Equations, Atti IV Cong. Inter. Mat. (Roma,1908) 2 (1909), 98–114.
[50]
, Introduction to a Form of General Analysis, Yale University Press, 1910.
[51]
, Deﬁnition of Limit in General Integral Analysis, Proceedings of the National Acad-
emy of Sciences of the United States of America 1 (1915), no. 12, 628–632.
[52] E. H. Moore and H. Smith, A General Theory of Limits, Amer. J. Math. 44 (1922), 102–121.
[53] E. H. Moore, General Analysis. Part I. The Algebra of Matrices, Memoirs of the American
Philosophical Society, Philadelophia, Vol. 1, 1935.
[54] P. Muldowney, A general theory of integration in function spaces, including Wiener and
Feynman integration, Vol. 153, Longman Scientiﬁc & Technical, Harlow; John Wiley, 1987.
[55] E. Nathanson, Path integration with non-positive distributions and applications to the
Schr¨dinger equation, PhD (Doctor of Philosophy) thesis, University of Iowa, https://doi.
org/10.17077/etd.k483ok3i. (2014).
[56] E. Nathanson and P. Jørgensen, A global solution to the Schr¨dinger equation: From Henstock
to Feynman, Journal of Mathematical Physics 56 (2015).
[57]
, Trotter’s limit formula for the Schr¨odinger equation with singular potential, Journal
of Mathematical Physics 58 (2017).
[58] Dag Normann and Sam Sanders, Nonstandard Analysis, Computability Theory, and their
connections, J. Symbolic Logic 84 (2019), no. 4, 1422–1465.
[59]
, The strength of compactness in Computability Theory and Nonstandard Analysis,
Annals of Pure and Applied Logic, Article 102710 170 (2019), no. 11.
[60]
, On the mathematical and foundational signiﬁcance of the uncountable, Journal of
Mathematical Logic, https://doi.org/10.1142/S0219061319500016 (2019).
[61]
, On the mathematical and foundational signiﬁcance of the uncountable, Updated
version of [61], arxiv: https://arxiv.org/abs/1711.08939 (2019).
[62]
, Representations in measure theory, Submitted, arXiv: https://arxiv.org/abs/
1902.02756 (2019).
[63]
, Pincherle’s theorem in reverse mathematics and computability theory, Ann. Pure
Appl. Logic 171 (2020), no. 5, 102788, 41.
[64]
, Open sets in Reverse Mathematics and Computability Theory, Journal of Logic and
Computability 30 (2020), no. 8, pp. 40.
[65]
, On the uncountability of R, Submitted, arxiv: https://arxiv.org/abs/2007.07560
(2020), pp. 29.
[66] W. F. Osgood, Lehrbuch der Funktionentheorie. Erster Band, Chelsea Publishing Co., New
York, 1965 (German).
[67] W. N. Polyzou and Ekaterina Nathanson, Scattering using real-time path integrals, arXiv:
https://arxiv.org/abs/1712.00046 (2017).


## Page 49


PLATO AND THE FOUNDATIONS OF MATHEMATICS
49
[68] Pao Ming Pu and Ying Ming Liu, Fuzzy topology. I. Neighborhood structure of a fuzzy point
and Moore-Smith convergence, J. Math. Anal. Appl. 76 (1980), no. 2, 571–599.
[69] Paul Rusnock, Bolzano’s contributions to real analysis, Academia Verlag, Beitr¨age zur
Bolzano-Forschung, Band 16, p. 99-116, 2003.
[70] Nobuyuki Sakamoto and Takeshi Yamazaki, Uniform versions of some axioms of second
order arithmetic, MLQ Math. Log. Q. 50 (2004), no. 6, 587–593.
[71] Sam Sanders, Reverse Mathematics of topology: dimension, paracompactness, and splittings,
Submitted, arXiv: https://arxiv.org/abs/1808.08785 (2018), pp. 17.
[72]
, Nets and Reverse Mathematics: initial results, Proceedings of CiE19, Lecture Notes
in Computer Science 11558, Springer (2019), pp. 12.
[73]
, Reverse Mathematics and computability theory of domain theory, Proceedings of
WoLLIC19, Lecture Notes in Computer Science 11541, Springer (2019), pp. 20.
[74]
, Nets and Reverse Mathematics: a pilot study, To appear in Computability, arxiv:
https://arxiv.org/abs/1905.04058 (2019), pp. 34.
[75]
, Lifting recursive counterexamples to higher-order arithmetic, To appear in Proceed-
ings of LFCS2020, Lecture Notes in Computer Science, Springer (2019).
[76]
, Lifting countable to uncountable mathematics, Submitted, arxiv: https://arxiv.
org/abs/1908.05677 (2019), pp. 21.
[77]
, The law of excluded middle as a no-go theorem, Submitted, arXiv: https://arxiv.
org/abs/1910.07913 (2019), pp. 12.
[78] Eric Schechter, Handbook of analysis and its foundations, Academic Press, Inc., San Diego,
CA, 1997.
[79] Stephen G. Simpson, Nonprovability of certain combinatorial properties of ﬁnite trees, Harvey
Friedman’s research on the foundations of mathematics, Stud. Logic Found. Math., vol. 117,
1985, pp. 87–117.
[80]
, Partial realizations of Hilbert’s Program, J. Symbolic Logic 53 (1988), no. 2, 349–363.
[81]
(ed.), Reverse mathematics 2001, Lecture Notes in Logic, vol. 21, ASL, La Jolla, CA,
2005.
[82]
, Subsystems of second order arithmetic, 2nd ed., Perspectives in Logic, CUP, 2009.
[83]
, The G¨odel hierarchy and reverse mathematics., Kurt G¨odel. Essays for his centennial,
2010, pp. 109–127.
[84] Ernst Specker, Nicht konstruktiv beweisbare S¨atze der Analysis, J. Symbolic Logic 14 (1949),
145–158 (German).
[85] J. Stillwell, Reverse mathematics, proofs from the inside out, Princeton Univ. Press, 2018.
[86] Charles Swartz, Introduction to gauge integrals, World Scientiﬁc, 2001.
[87] William W. Tait, Finitism, The Journal of Philosophy 78 (1981), 524-564.
[88] George Tourlakis, Lectures in logic and set theory. Vol. 2, Cambridge Studies in Advanced
Mathematics, vol. 83, Cambridge University Press, 2003. Set theory.
[89] Anne Sjerp Troelstra, Metamathematical investigation of intuitionistic arithmetic and anal-
ysis, Springer Berlin, 1973. Lecture Notes in Mathematics, Vol. 344.
[90] A. S. Troelstra, Choice sequences, Clarendon Press, Oxford, 1977. A chapter of intuitionistic
mathematics; Oxford Logic Guides.
[91] Anne Sjerp Troelstra and Dirk van Dalen, Constructivism in mathematics. Vol. I, Studies in
Logic and the Foundations of Mathematics, vol. 121, North-Holland, 1988.
[92] John W. Tukey, Convergence and Uniformity in Topology, Annals of Mathematics Studies,
no. 2, Princeton University Press, Princeton, N. J., 1940.
[93] Leopold Vietoris, Stetige Mengen, Monatsh. Math. Phys. 31 (1921), no. 1, 173–204 (German).
[94] Hao Wang, Eighty years of foundational studies, Dialectica 12 (1958), 466–497.
[95] L. A. Zadeh, Fuzzy sets, Information and Control 8 (1965), 338–353.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]