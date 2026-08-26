---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.03827v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1903.03827v1_Native_Chemical_Automata_and_the_Thermodynamic_Interpretation_of_Their_Experimen

> Source: 1903.03827v1_Native_Chemical_Automata_and_the_Thermodynamic_Interpretation_of_Their_Experimen.pdf

> Pages: 21

---


## Page 1


Native Chemical Automata and the
Thermodynamic Interpretation of Their
Experimental Accept/Reject Responses∗
Marta Dueñas-Díez†and Juan Pérez-Mercader‡
‡ To whom correspondence should be addressed.
Introduction
Computation—deﬁned as the pathway for information to be input, to be
processed mechanically, and to be output in a useful way (Evans 2011)—
takes place not only in the myriad of electronic devices we use daily but
also in living systems. Life carries out computations mostly by using
chemical support: inputs are chemical substances, the mechanical pro-
cessing occurs via chemical reaction mechanisms, and the result is chem-
ical as well. Machines carrying out computations are typically referred
∗To appear in: The Energetics of Computing in Life and Machines, edited by David H.
Wolpert, Chris Kempes, Joshua A. Grochow, and Peter F. Stadler. Santa Fe: SFI Press, 2019.
†Repsol Technology Center, Carretera de Extremadura S/N, 28935 Móstoles, Madrid,
Spain; Department of Earth and Planetary Sciences and Harvard Origins of Life Initia-
tive, Harvard University, 20 Oxford Street, Cambridge, Massachusetts 02138; martadue-
nasdiez@fas.harvard.edu
‡Department of Earth and Planetary Sciences and Harvard Origins of Life Initiative,
Harvard University, 20 Oxford Street, Cambridge, Massachusetts 02138; Santa Fe Institute,
1399 Hyde Park Road, Santa Fe, New Mexico 87501; jperezmercader@fas.harvard.edu
1


## Page 2


to as automata (Hopcroft, Motwani, and Ullman 2006); hence, to a large
extent, living systems can be viewed as chemical automata (Bray 2009).
Classic automata are arranged hierarchically from simplest to most pow-
erful (Hopcroft, Motwani, and Ullman 2006): ﬁnite automata, then push-
down automata, and, at the top of the hierarchy, Turing machines (Turing
1936).
Although the subject of this contribution already has an interesting
history, we give here a brief, personal, and short summary of some in-
teresting developments in the ﬁeld of chemical computation. Interest in
chemical computing dates back to the early 1970s, when Conrad (1972)
studied information processing in molecular systems and how it diﬀers
from electronic digital computing. A theoretical chemical diode was ﬁrst
suggested by Okamoto, Sakai, and Hayashi (1987), an idea that Hjelm-
felt, Weinberger, and Ross (1991) further developed to suggest that neu-
ral networks and chemical automata could be constructed connecting
such chemical diodes. In the 1990s, Magnasco (1997) studied the Tur-
ing completeness of chemical kinetics. The ﬁrst experimental realiza-
tion of chemical AND and OR logic gates using reaction diﬀusion was
achieved in 1995 by Tóth and Showalter (1995), followed by XOR gates
(Adamatzky and Lacy Costello 2002) and counters (Górecki, Yoshikawa,
and Igareshi 2003), and still is an active area of research due to the dif-
ﬁculties associated to linking many gates to carry out more advanced
computations. Computations carried out in a more native way, with-
out requiring diﬀusion, have been suggested using complex biomolecules
such as DNA (Adleman 1994; Benenson 2009) or chromatin (Prohaska,
Stadler, and Krakauer 2010; Bryant 2012). In summary, most artiﬁcial
approaches to chemical computing, inspired by living systems, focus on
reaction–diﬀusion systems mostly representing logic gates or use com-
plex biomolecules to solve very speciﬁc problems.
Our approach (Pérez-Mercader, Dueñas-Díez, and Case 2017) diﬀers
from the aforementioned work in that we use the power of chemistry, and
the molecular recognition associated with the occurrence of chemical re-
2


## Page 3


actions, in a one-pot reactor, that is, a single well-mixed container where
multiple rounds of reactions can take place, without using external ge-
ometrical aids or complex biomolecules and relying fully on the power
of molecular recognition and the robustness associated with Avogadroʟ
s number to carry out computations. We have recently demonstrated ex-
perimentally that this approach, without using biochemistry, can recog-
nize a language that only automata at the Turing machine level of the hi-
erarchy can recognize (Dueñas-Díez and Pérez-Mercader, Submitted 2018).
In this contribution, we apply the well-known natural connection be-
tween chemistry and thermodynamics (Donder 1927; Kondepudi and
Prigogine 2014) to study and interpret the chemical reject/accept sig-
natures of chemical automata in thermodynamic terms. We do this for
three examples, one at each main level of the three-level hierarchy in
computing automata theory (Hopcroft, Motwani, and Ullman 2006). Of
course, this connection is only a ﬁrst step toward quantifying the thermo-
dynamic cost of chemical computation and, more importantly, toward its
optimization (Bennett 1982; Landauer 1961). Indeed, the same thermo-
dynamic metrics we apply as the reject/accept signatures after a word is
processed can be applied during the course of the computation, not just
at its end. If we apply our metrics continuously during the computation
of a complete sequence, we can assess the thermodynamic cost of com-
putation as each symbol is processed and therefore determine how the
thermodynamic cost evolves as the input sequence length grows or even
compare the cost of diﬀerent types of rejects. We suggest using the three
languages chosen below, or other similar well-known languages and their
associated automata, as minimal complete examples to run quantitative
studies of the thermodynamic cost of computation.
One-Pot Native Chemical Computation
Our work focuses on demonstrating experimentally how computations
of diﬀerent complexity (in the sense of classical automata theory) can be
carried out by chemical means exclusively, in a homogeneous reactor, and
3


## Page 4


without requiring complex biomolecules. In our approach, the input to
be computed is represented by a sequence of symbols from a chemical
alphabet in which each letter corresponds to a certain constant amount,
or aliquot, of a carefully chosen reacting chemical species. The input
is sequentially added letter by letter, that is, aliquot by aliquot, to a one-
pot reactor at constant time intervals (Pérez-Mercader, Dueñas-Díez, and
Case 2017). The processing of each letter consists in selectively activat-
ing speciﬁc pathways in the chemical mechanism and, correspondingly,
altering the resulting chemical state/landscape in a systematic way. Fi-
nally, the output of the computation is in the form of a distinct chemical
response; that is, for a given automata/language combination, the chem-
ical behavior associated with a rejected sequence is diﬀerent from the
chemical behavior associated to that of an accepted sequence (Dueñas-
Díez and Pérez-Mercader, Submitted 2018). Naturally, we expect that
such distinct chemical responses correspond to some distinct thermody-
namic signatures as well.
To show that chemistry can carry out computations of diﬀerent com-
plexity levels, we carry out the following steps. First, we choose a speciﬁc
language of interest that a tailored chemical automaton should recognize,
that is, a speciﬁc problem to be solved. From classic automata theory,
we then identify the class of automata needed to recognize it and the
computational requirements as deﬁned by the corresponding automata
tuple. We translate this into speciﬁc requirements for the chemical re-
actions and their reactants, products, and intermediates, leading us to
select the alphabet description appropriately. Then, the speciﬁc quan-
titative recipes for initial conditions and alphabet aliquots are selected
so that the chemical reaction monitoring system allows detection of the
machineʟs response with suﬃcient/reasonable precision.
4


## Page 5


Chemical Finite Automaton Recognizing the Regular Lan-
guage L1 of All Words Containing at Least One “A” and One
“B”
Regular languages are the simplest languages in automata hierarchy (Hopcroft,
Motwani, and Ullman 2006). They do not require counting: their words
all contain or all exclude certain patterns of the alphabet symbols or af-
ﬁxes (Hopcroft, Motwani, and Ullman 2006; Cohen 1991). Regular lan-
guages are recognized by a ﬁnite automaton (FA), an abstract device that
at each given time is in one of a ﬁnite number of states, and the device
transitions states depending on the input using a ﬁnite set of rules. At
the end of a computation, that is, after a word is processed by the FA, the
device terminates in either an accept state or a reject state, depending on
whether the input word belongs to the regular language recognized by
the FA.
Following the intuitive notion that simple chemistries can recognize
regular languages, we reverse-formulate the question as follows: what
can a single bimolecular reaction of the type A + B →C + D compute?
If we represent the letters, a and b, in a language L1 by the aliquots of
A and B corresponding to this reaction, we see that such a bimolecular
reaction recognizes the regular language L1 of all words that contain at
least one a and one b. For an illustrative and visual implementation, we
can choose a precipitation reaction in an aqueous medium such as
KIO3 + AgNO3 →AgIO3(s) + KNO3.
(1)
If, during computation, a white precipitate of silver iodate is observed,
the input string has been recognized and accepted; if the solution is clear
from precipitate, the string has been rejected because there was no re-
action and the input string was therefore not recognized. The only re-
quirement in this example to choose the recipes of alphabet symbols a
5


## Page 6


(potassium iodate) and b (silver nitrate) quantitatively is that the prod-
uct of their concentrations, once one aliquot of each is added to the re-
actor, exceeds the solubility product constant of silver iodate at the op-
erating reactor temperature, thus guaranteeing the appearance of a pre-
cipitate. Fig. 1 shows the chemical representation of symbols a and b,
the bimolecular precipitation reaction, the corresponding theoretical FA
transition graph to recognize L1, and the results of testing two sequences
experimentally. Sequence aab gives a white precipitate, corresponding to
the ﬁnal state qf in the abstract FA. Sequence aaa shows no precipitate,
corresponding to state q1, and thus the input is rejected by the chemical
automaton.
Because this reaction is exothermic, the accept and reject states can
also be detected by monitoring temperature (if the temperature remains
constant, the sequence is rejected, but if the temperature increases, then
the sequence is accepted). Hence we see that the heat of reaction is the
thermodynamic equivalent to the chemical precipitate response.
Chemical 1-Stack PDA Recognizing the Context-Free Lan-
guage L2 of Balanced Parentheses
Next, we go one important step up in the hierarchy and consider the case
of context-free languages. We show how one-pot native chemistry recog-
nizes a language in which both counting and sequence order are relevant.
Context-free languages (CFL) are those whose words involve matching of
substrings, aﬃxes, or symbols and therefore require counting to one ar-
bitrarily high integer (Hopcroft, Motwani, and Ullman 2006). We choose
the Dyck language (Weisstein 2009), the language of balanced paren-
theses, as L2: a sequence of parentheses is balanced if, during its pro-
cessing, the number of closed parentheses never exceeds the number of
open parentheses, and at the end of the computation, the number of open
parentheses matches exactly the number of closed parentheses (Hopcroft,
Motwani, and Ullman 2006; Cohen 1991).
6


## Page 7


No Precipitate
aaa
No Heat
Released
ºC
Precipitate
aab
Heat
Released
ºC
Accept
Reject
q0, q1 or q2
qf
Interval
00:00:30
τ = 30s
Alphabet
a         b
KIO3   AgNO3
L1 = {Language of all words that have at least one a and at least one b}.
L1 is a regular language, and therefore is recognized by the FA
Chemically implemented by an acid/base reaction.
FA Computation
KIO3 (aq) + AgNO3 (aq)      AgIO3 (s) + KNO3 (aq)
L1 Transition Graph
q0
q1
q2
qf
a
a,b
b
a
b
a
b
+
+
Figure 1. Operation of a chemical ﬁnite-state automaton: language L1, described by
the regular expression (a + b)∗a(a + b)∗b(a + b)∗+ bb∗aa∗, is recognized by a FA and is
realized chemically by a precipitation reaction. In this example, once the full sequence
has been processed, if the solution contains a visible precipitate of AgIO3, or,
equivalently, heat has been released during computation, the input string has been
accepted as a word in L1. In contrast, if the solution does not contain any visible
precipitate, or, equivalently, no heat was released during computation, then the input
string was rejected. Input sequences aab and aaa were tested experimentally and in
the former a precipitate was observed, while no precipitate was observed in the latter.
7


## Page 8


In theoretical computer science, a CFL is recognized by a one-stack
pushdown automaton (PDA). This automaton diﬀers from a FA by being
endowed with an additional element, the stack, in which to store a string
of arbitrary length and that, furthermore, can be read and modiﬁed only
at its top, in a last-in-ﬁrst-out fashion (Hopcroft, Motwani, and Ullman
2006; Cohen 1991), just as in a cafeteria “stack of trays.” The transitions
in a PDA depend not only on the current input symbol and state but also
on the current symbol at the top of the stack. A transition may result not
only in changing the state of the automaton but also in pushing (adding)
an element to the top of the stack or popping (removing) an element
from the stack. The “accept” criterion is often associated with the set
of transitions leading to an empty stack at the end of the computation.
For our chosen language L2, the stack keeps track of the excess of open
parentheses with respect to the closed parentheses and, indeed, it has to
be empty at the end of the computation.
The requirement of a “stack” translates in native chemical comput-
ing into the condition of having a pathway in the reaction mechanism
in which there is an intermediate species that is produced (pushed) in
one subreaction and consumed (popped) in another subreaction. This in
turn leads us to select as an example for the actual implementation of a
chemical L2-PDA the language of Dyck words by means of a pH reaction
and with the following alphabet assignment: “(” is an aliquot of the base
(NaOH), “)” is an aliquot of the weak diprotic acid (CH2(COOH)2), and
“#”—the symbol that delimits the beginning- and end r
of-sequence—
is an aliquot of a pH indicator. The quantiﬁcation of the recipes of the
symbol aliquots is carried out so that one aliquot of “(” and one aliquot
of “)” neutralize each other to the midpoint in the pH curve (Petrucci
et al. 2011) and the pH indicator is selected to change color around the
midpoint (Methyl Red indicator in our implementation).
At the beginning of a computation, the L2-PDA reactor contains deion-
ized water and an aliquot of the pH indicator. The processing of the sym-
bols sequentially fed to the reactor leads to changes in pH whose value
8


## Page 9


we assign to the stack. The L2-PDA Accepts the input string if during the
computation the pH ≥midpoint-pH but is at midpoint-pH (empty stack)
at the end of computation, that is, after adding “#.” Conversely, the L2-
PDA rejects an input string if the pH falls below the midpoint-pH at any
stage during computation (excess of “)”, and attempting to “pop” from an
already empty stack), or if the pH is larger than the midpoint-pH value
at the end of computation (excess of “(”, or the stack is “not empty”) (cf.
Fig. 2).
The response given by the L2-PDA can again be interpreted in terms
of a thermodynamic measure: the enthalpy yield of the computation Y∆H
(%). This is deﬁned as the ratio between the enthalpy produced or con-
sumed during computation divided by the total formation enthalpy of
the chemical input:
Y∆H (%) = reaction heat during computation
formation heat of input string
× 100
(2)
Y∆H (%) =
!R
1
" tend
0
vi ∆Ho
r,idt
!n
1 [j]input∆Ho
f ,j
× 100
(3)
Here R is the number of the reactions in the kinetic mechanism (at the
level of coarse graining associated with the time between symbol pro-
cessing), vi is the velocity of reaction i (mol/(dm3 · s)), ∆Ho
r,i represents
the enthalpy of reaction i, J is the number of symbols in the language
alphabet, [j]input is the total change in concentration of species j due to
the input string, and ∆Ho
f ,j is the formation enthalpy of chemical species
j.
During computation, the dominant contribution to reaction heat oc-
curs whenever a pair of parentheses is compensated via reaction R3 (third
reaction) in the mechanism (cf. Fig. 2): OH−+ H+ →H2O. Hence the
9


## Page 10


Elapsed Time (s)
10
5
0
180
360
540
720
900
1080
Measured pH
1260
#()()()#
(            )
(            )
(            )
#
Elapsed Time (s)
10
5
0
180
360
540
720
900
1080
Measured pH
1260
#())())#
(            )
)            (
)            )
#
Experiment
Midpoint pH
Excess “)”
Attempt to
pop from an
empty stack
Excess “(”
Non empty
stack
q0
R1
R2
q1
qf
L2 = {Dyck Language of all words with balanced Parentheses}.
Chemically implemented by an acid/base reaction.
C3H4O4     C3H3O4 + H+
-
-
pH reaction
H+ + OH-     H2O
C15H15N3O2 + OH     C15H14N3 O2
H+ + C15H14N3 O2     C15H15N3O2
C3H3O4     C3H2O4  + H+
-
2-
L2 Transition Graph
Push
Push
Pop
{(,$;X$} 
{(,X;XX} 
{),X; ε} 
Reject
Reject
Accept
Acid pH
Basic pH
Midpoint pH
Interval
00:03:00
τ = 180s
{#,ε;$} 
{),$;$} 
{#,X;X} 
{#,$;$} 
Alphabet
( 
)
NaOH   Malonic
Figure 2. Operation of a chemical one-stack pushdown automata: L2 is recognized by
a one-stack PDA. Here the reaction pH acts as the stack. If pH ≥midpoint pH
(intermediate gray tone or lightest gray tone, respectively) during computation, and
pH = midpoint pH (lightest gray tone) at the end of computation, then the input
string is accepted. Otherwise, if pH < midpoint pH (darkest gray tone) any time
during computation, the string is rejected (attempting to “pop” from an empty stack).
Also, if the pH > midpoint pH at the end of computation (intermediate gray tone),
there is an excess of open parentheses and the string is rejected. Above are the
experimental results for rejected ())()) and accepted ()()() words.
10


## Page 11


enthalpy yield can be approximated as follows:
Y∆H (%) =
" tend
0
v ∆Ho
rdt
[malonic]input∆Hf ,malonic+[OH−(aq)]input∆Hf ,OH−(aq)
× 100
≈
npairsc ∆Ho
r
[malonic]input∆Hf ,malonic+[OH−(aq)]input∆Hf ,OH−(aq)
× 100
(4)
where npairs is the number of pairs of parentheses that have been bal-
anced and c is the change in molarity of the solution due to the addition
of each aliquot of malonic acid. For our pH reaction, the heat of the acid–
base neutralization reaction is ∆Hor = −55.89 kJ/mol, and the formation
enthalpies can be found in standard thermodynamic databases (Haynes
2014).
By chemical engineering design of our 1-PDA, Dyck words maximize
the enthalpy yield, whereas input strings that have excess of either open
or closed parentheses will result in smaller enthalpy yields than strings
with balanced parentheses.
This again provides us with a thermody-
namic metric to assess the result of the computation.
Chemical 2-Stack PDA/TM Recognizing Context-Sensitive
Language L3 = {anbncn, Where n > 0}
Finally, we demonstrate that our native chemical computing approach
can be used successfully to recognize a language that only a Turing ma-
chine (TM) can recognize. A TM is an automaton equipped with an in-
ﬁnite tape and a read-write head working together with a ﬁnite set of
transition rules. Initially, the input is written on the tape, each letter of
the string written on one cell. The head can move left or right, reading
and erasing and writing symbols on the tape based on the ﬁnite set of
rules. As a part of the state transition, the TM decides if the next cell
to be scanned is to the right or the left of the current scanned cell. The
inﬁniteness of the tape and the possibility of moving either to the left or
11


## Page 12


to the right of the tape are the factors that make the TM capable of recog-
nizing all computable languages (Hopcroft, Motwani, and Ullman 2006;
Turing 1936; Cohen 1991).
For our experimental implementation, we choose a well-deﬁned and
decidable language (Dueñas-Díez and Pérez-Mercader, Submitted 2018).
The language L3 = {anbncn, where n > 0}, is made up of words consisting
of n-repeats of a, followed by n-repeats of b, followed by n-repeats of
c. Note that L3 is a context-sensitive language not recognizable by either
a FA or a one-stack PDA (Cohen 1991), and though it is not the most
complex language a theoretical TM can recognize, it is quite convenient
for an experimental implementation, as it brings into play all the features
of a TM. Context-sensitive languages are recognized by a subclass of TMs,
linearly bounded automata (LBA), in which only the cells occupied by the
input are used for computation (Linz 2012).
TMs are equivalent to two-stack PDAs (Minsky 1961) because two
stacks can emulate the function of moving right and left on an inﬁnite
(or arbitrarily long) tape. Taken together with the requirement of two
interrelated stacks leads us to translate this into the chemical require-
ment of interrelated redox reactions and to oscillatory chemistry (Pérez-
Mercader, Dueñas-Díez, and Case 2017; Dueñas-Díez and Pérez-Mercader,
Submitted 2018). We have chosen arguably the best-known oscillatory
chemistry, the Belousov–Zhabotinsky (Belousov 1959; Zhabotinsky 1964)
reaction. As was the case before, alphabet symbols are carefully chosen to
map into distinct pathways in the reaction mechanism and, consequently,
to have distinct systematic eﬀects on the measured oscillatory behavior
(Dueñas-Díez and Pérez-Mercader, Submitted 2018): a is transcribed as
an aliquot of sodium bromate aﬀecting dominantly the autocatalytic pro-
duction of HBrO2 and catalyst oxidation, b is transcribed as an aliquot of
malonic acid dominantly aﬀecting the bromination of the weak acid and
the reduction of catalyst, c is transcribed as an aliquot of NaOH aﬀecting
the pH-dominated subset of reactions, and # is transcribed as an aliquot
of catalyst aﬀecting the redox-dominated subset of reactions. The quan-
12


## Page 13


titative recipes were selected and engineered to maintain the oscillatory
regime for as long a word as possible, while simultaneously providing
measurable changes in the oscillations. To implement this in a reactor,
we used a combination of simulation and experimental studies.
The results of this experimental implementation have been reported
in detail elsewhere (Dueñas-Díez and Pérez-Mercader, Submitted 2018).
A key ﬁnding is that each state in the abstract TM transition graph has its
own distinct chemical counterpart, for example, for our chosen language
L3, the reject due to the input containing ba has a diﬀerent chemical sig-
nature than a reject due to an excess of a. There is a systematic clustering
of chemical behaviors when mapping two basic phenomenological de-
scriptors of the ﬁnal oscillations (frequency and an oscillation amplitude-
related diﬀerence measure). Experimentally, we ﬁnd that words in the
language are placed in a locus in this map, while rejected sequences
(same as words, of course) lie either above or below (Dueñas-Díez and
Pérez-Mercader, Submitted 2018).
To ﬁnd a more intuitive criterion for acceptance/rejection, we intro-
duce a metric based on the integral of the ﬁnal oscillations (which we call
the area) A(Word) associated with the word undergoing processing in the
computation:
A(Word) = Vmax × τ′ −
# t#+τ
t#+30
Vosc (t)dt,
(5)
where t# is the time in reaction coordinates at which the end-of-expression
symbol is added, π′ is the time interval between symbols minus 30 sec-
onds (the ﬁrst 30 seconds are discarded in the integration to allow for fast
transients to dissipate), Vmax is the maximum redox potential (all catalyst
in oxidized form), and Vosc is the measured redox potential, which can be
well approximated by Nernst equation:
Vosc = V0 + RT
neF ln
⎛
⎜⎜⎜⎜⎜⎜⎝
'
Ru(bpy)3+
3
(
'
Ru(bpy)2+
3
(
⎞
⎟⎟⎟⎟⎟⎟⎠,
(6)
with [Ru(bpy)2+
3 ] and [Ru(bpy)3+
3 ], respectively, denoting the reduced and
oxidized form of the catalyst, which can in turn be written in terms of
13


## Page 14


Language L3 = {anbncn, n>0}
recognized by a Turing Machine
τ = 7.5minutes
a                  b                 c
Bromate  Malonic  NaOH
2-stack PDA/TM Computation
Simplified representation of BZ chemical oscillator
Bromate
Subnetwork
Ru(bpy)32+
Ru(bpy)33+
Br-
Bromomalonic
acid
Malonic
Acid
HBrO
Br2
105
110
100
95
90
85
80
75
2
4
6
8
10
12
14
16
ab2c
Words ∈ L3 on fitted constant line
Slope = 0.01 ⊥ 0.08
Intercept = 91.6 ⊥ 0.8
Chi-sq p-value = 0.999
a2b3c2
a2b2c3
a2b2c2
a2bc
a3b3c3
a3b2c2
a4b4c4
a5b5c5
abc
a3b3c4
a3b4c3
String Length
A(Word) (V . s)
#a2b2c2#
Redox Potential (mV)
a
a
b
b
c
c
#
450
550
850
Redox Potential (mV)
550
850
900 1350 1800 2250 2700
a
a
b
b
c
c
#
450
900 1350 1800 2250
c
2700 3150
Accept
#a3b2c2#
Reject
Figure 3. A Belousov–Zhabotinsky-based chemical Turing machine for L3 at work:
L3 is recognized by a two-stack PDA/TM, as shown by the constant area represented
by the thick black line joining words in L3 in the upper right-hand corner graph.
Words not in L3 lie elsewhere in the plot. During computation, if certain alphabet
patterns in the redox potential V are detected, the strings are rejected. The rejection is
speciﬁc for each type of reject. Here ﬁve words (in black font) were accepted and seven
strings (in gray font) were rejected (two due to excess as, three due to excess bs, and
two due to excess cs). The bottom panels compare the evolution of V for rejected
a3b2c2 (bottom right panel) and accepted a2b2c2 (bottom left panel).
14


## Page 15


the extent of reaction for the elementary redox reactions in the oxida-
tion and reduction subsets as appropriately coarse grained. The quantity
ne denotes the number of electrons involved in the reduction–oxidation
process and is = 1 for this reaction. The redox potential is related to the
Gibbs free energy ∆G (Kuhn and Försterling 2000) as
∆Gosc = −neFVosc.
(7)
We can thus rewrite the area deﬁned above in terms of the Gibbs free en-
ergy corresponding to full oxidation ∆G′ and the redox Gibbs free energy
∆Gosc:
A(Word) = −1
neF
,
∆G
′ × τ′ −
# t#+τ
t#+30
∆Gosc (t) dt
-
.
(8)
The recipes for the alphabet aliquots can now be optimized to achieve
a constant (i.e., n-independent or word length-independent) A(Word) for
words in L3, while rejected sequences lie either above or below this value
(cf. Fig. 3, top right). Hence, if the area A(Word) is constant and inde-
pendent of string length for the words in L3, so is the integral of ∆Gosc.
Finally, we point out that the dimensions of this area are the same as those
of the action in physics and that its origin reminds one of the mass-action
law in chemistry.
Conclusions
We have demonstrated experimentally that nonbiochemical chemistry in
a homogeneous one-pot reactor, where the chemical inputs to be com-
puted are fed sequentially at constant time intervals, has the capability
to run successful computations at the three fundamental levels in the hi-
erarchy of classical automata theory.
Our approach allows tailoring a chemical reactor to run a speciﬁc
computation, that is, recognizing a speciﬁc language of interest, iden-
tifying an appropriate chemical transcription/translation of the alphabet
and the chemistry of the automaton so that the reactor provides a dis-
tinctive thermodynamic/chemical response for those inputs that belong
15


## Page 16


to said language. The design and operation of each chemical automaton
follow similar principles, as the examples L1, L2, and L3 illustrate. The
elements of an automatonʟs tuple have chemical counterparts; for ex-
ample, there are as many types of chemical “reject” states in the practical
chemical automaton as “reject” states in the abstract automaton.
There are of course diﬀerences between abstract and actual automata.
Any experimental chemical (or otherwise actual) realization of a TM nec-
essarily has a noninﬁnite chemical tape; for that reason, it is most prac-
tical to implement the TM in the subclass of linear bounded automata.
Note, however, that this is not too restrictive: by optimizing the oper-
ational strategy, including choice of reactor type and recipes, one can
extend the tape to the needed length.
Computational versatility can also be enhanced by combining diﬀer-
ent chemical automata. The earlier discussed chemistries, including the
Belousov–Zhabotinsky oscillatory chemistry, can be reconﬁgured to solve
other languages of computational interest by appropriately selecting the
alphabet symbols and their recipes such that all abstract-tuple elements
have their chemical counterparts. The richness of time scales and non-
linearity in the Belousov–Zhabotinsky chemistry (or any other oscilla-
tory chemistry) can be further exploited for computation. The reactions
selected in this chapter are meant to provide illustrative examples for
each class of automata. Other reactions in the appropriate classes can of
course be used. Furthermore, other instances of speciﬁc computations
can also be designed and carried out based on other speciﬁc chemistries,
such as pH oscillators or biochemical oscillators. Finally, because abstract
automata can be connected to create new automata (Hopcroft, Motwani,
and Ullman 2006), we can imagine that chemical automata can likewise
be interconnected to carry out more complex computations or generaliza-
tions of our automata (e.g., from a TM to a universal TM) if the underly-
ing chemistries are compatible with each other, share common chemical
species, and can be deployed in the same solvent media.
For each of the three implemented languages, we have identiﬁed a
16


## Page 17


thermodynamic interpretation of the accept/reject states that is equiv-
alent to the chemical response. Translating the criterion from purely
chemical to its thermodynamic equivalent may simplify the interpreta-
tion of the acceptance/rejection of native chemical automata, as clearly
seen for the case of the context-sensitive language L3. In the examples
discussed here, the thermodynamic interpretation involves thermody-
namic potentials like enthalpy (languages L1 and L2) or Gibbs energy
(language L3). Such thermodynamic potentials were introduced in equi-
librium thermodynamics to describe how closed systems approach equi-
librium because, according to the extremum principles (Kondepudi and
Prigogine 2014; Callen 1985), these potentials reach an optimal value at
equilibrium. For example, in a closed system at constant pressure and
temperature, the Gibbs free energy is at a minimum in equilibrium. Our
chemical automata are open systems in nonequilibrium due to the semi-
batch feed of the chemical input, and hence these extremum principles
do not apply. However, in the same way that an open system can be main-
tained at a (nonequilibrium) stationary state by the inﬂux of matter and
energy, we can direct the thermodynamic potentials to certain values and
even to some (nonequilibrium) optimum values by feeding it with spe-
ciﬁc sequences in which matter and/or energy are inputs to the system.
In this case, when the system reaches a (nonequilibrium) optimum, it is
not as an (unavoidable) result from an extremum principle but driven
or directed by our sequential chemical inputs of the language of interest
and the speciﬁc recipes used. The chemical input directs the dominant
reaction pathways, which in turn direct the thermodynamic pathways as
well. This form of bootstrapping brings with it chemical control of the
nonlinear, out-of-equilibrium chemistry itself.
Connecting the topology of complex reaction networks, their dynam-
ics, and their thermodynamics is a recent and growing area of research
(Rao and Esposito 2016). In our native chemical automata, the connec-
tion between chemistry and thermodynamics can contribute to better
study and understanding of the energetic cost of computation, and prob-
17


## Page 18


ably how to control this cost in the quest to approach Landauer’s limit
(Landauer 1961), at least for the important case of chemical automata.
Furthermore, our approach does use liquid phase (dense) chemistry and
kinetics and is not restricted by any approximations relying on the dilute
gas approximation.
Nothing in the aforementioned precludes the extension of these re-
sults to biochemistry and biology. In particular, one can begin to think
about the application of the preceding information-processing thermo-
dynamics in the coming wave of new biochemistry-based oscillators (Novák
and Tyson 2008), DNA-based oscillators (Srinivas et al. 2017), and com-
puting ecologies of natural and synthetic bacteria—and ﬁnally, also to
the study of the metabolic eﬃciency and the cost of chemical informa-
tion processing and computation in extant living systems.
18


## Page 19


References
Adamatzky, A., and B. de Lacy Costello. 2002. “Experimental Logical
Gates in a Reaction-Diﬀusion Medium: The XOR Gate and Beyond.”
Physical Reviews E 66 (4): 046112.
Adleman, L. M. 1994. “Molecular Computation of Solutions to Combina-
torial Problems.” Science 266 (5187): 1021–1024.
Belousov, B. P. 1959. “A Periodic Reaction and Its Mechanism.” Compila-
tion of Abstracts on Radiation Medicine 147 (145): 1.
Benenson, Y. 2009. “Biocomputers: From Test Tubes to Live Cells.” Molec-
ular Biosystems 5:675–685.
Bennett, C. H. 1982. “The Thermodynamics of Computation—A Review.”
International Journal of Theoretical Physics 21 (12): 905–940.
Bray, D. 2009. Wetware: A Computer in Every Living Cell. New Haven, CT:
Yale University Press.
Bryant, B. 2012. “Chromatin Computation.” PLoS One 7 (5): e35703.
Callen, H. B. 1985. Thermodynamics and an Introduction to Thermostatis-
tics. Hoboken, NJ: John Wiley.
Cohen, D. I. A. 1991. Introduction to Computer Theory. 2nd ed. Hoboken,
NJ: John Wiley.
Conrad, M. 1972. “Information Processing in Molecular Systems.” Biosys-
tems 5 (1): 1–14.
Donder, T. de. 1927. Aﬃnité. Paris: Gauthier-Villars.
Dueñas-Díez, M., and J. Pérez-Mercader. Submitted 2018. “How Chem-
istry Computes: Language Recognition by Non-Biochemical Chemi-
cal Automata.”
Evans, D. 2011. “Introduction to Computing: Explorations in Language,
Logic, and Machines.” http://computingbook.org.
19


## Page 20


Górecki, J., K. Yoshikawa, and Y. Igareshi. 2003. “On Chemical Reactors
That Can Count.” Journal of Physical Chemistry A 107 (10): 1664–
1669.
Haynes, W. M., ed. 2014. CRC Handbook of Chemistry and Physics. 95th
ed. Boca Raton, FL: CRC Press.
Hjelmfelt, A., E. D. Weinberger, and John Ross. 1991. “Chemical Imple-
mentation of Neural Networks and Turing Machines.” Proceedings
of the National Academy of Sciences of the United States of America 88
(24): 10983–10987.
Hopcroft, J. E., R. Motwani, and J. D. Ullman. 2006. Introduction to Au-
tomata Theory, Languages, and Computation. 3rd ed. Boston, MA: Addison-
Wesley Longman.
Kondepudi, D., and I. Prigogine. 2014. Modern Thermodynamics: From
Heat Engines to Dissipative Structures. Hoboken, NJ: John Wiley.
Kuhn, H., and H. D. Försterling. 2000. Principles of Physical Chemistry.
Hoboken, NJ: John Wiley.
Landauer, R. 1961. “Irreversibility and Heat Generation in the Comput-
ing Process.” IBM Journal of Research and Development 5 (3): 183–191.
Linz, P. 2012. An Introduction to Formal Languages and Automata. 5th ed.
Burlington, MA: Jones / Bartlett Learning.
Magnasco, M. O. 1997. “Chemical Kinetics Is Turing Universal.” Physical
Review Letters 78 (6): 1190.
Minsky, M. L. 1961. “Recursive Unsolvability of Post’s Problem of Tag
and Other Topics in Theory of Turing Machines.” Annals of Mathe-
matics 74 (3): 437–455.
Novák, B., and J. J. Tyson. 2008. “Design Principles of Biochemical Oscil-
lators.” Nature Reviews Molecular Cell Biology 9:981–991.
20


## Page 21


Okamoto, M., T. Sakai, and K. Hayashi. 1987. “Switching Mechanism of
a Cyclic Enzyme System: Role as a ‘Chemical Diode’.” Biosystems 21
(1): 1–11.
Pérez-Mercader, J., M. Dueñas-Díez, and Daniel Case. 2017. Chemically-
Operated Turing Machine. U.S. Patent 9582771B2.
Petrucci, R. H., F. G. Herring, J. D. Madura, and C. Bissonette. 2011. Gen-
eral Chemistry: Principles and Modern Applications. 10th ed. Pearson
Prentice Hall.
Prohaska, S. J., P. F. Stadler, and D. C. Krakauer. 2010. “Innovation in
Gene Regulation: The Case of Chromatic Computation.” Journal of
Theoretical Biology 265 (1): 27–44.
Rao, R., and M. Esposito. 2016. “Nonequilibrium Thermodynamics of
Chemical Reaction Networks: Wisdom from Stochastic Thermody-
namics.” Physical Reviews X 6:041064.
Srinivas, N., J. Parkin, G. Seelig, E. Winfree, and D. Soloveichik. 2017.
“Enzyme-Free Nucleic Acid Dynamical Systems.” Science 358 (6369):
eaal2052.
Tóth, Á., and K. Showalter. 1995. “Logic Gates in Excitable Media.” Jour-
nal of Chemical Physics 103 (6): 2058–2066.
Turing, A. M. 1936. “On Computable Numbers, with an Application to
the Entscheidungsproblem.” Proceedings of the London Mathematical
Society 2:230–265.
Weisstein, E. W. 2009. CRC Encyclopedia of Mathematics. 3rd ed. Boca Ra-
ton, FL: CRC Press.
Zhabotinsky, A. M. 1964. “Periodic Oxidation of Malonic Acid in So-
lution (Investigation of the Kinetics of the Reaction of Belousov).”
Bioﬁzika 9:306–311.
21

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]