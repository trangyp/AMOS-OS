---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1212.6543v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1212.6543v1_Rethinking_set_theory

> Source: 1212.6543v1_Rethinking_set_theory.pdf

> Pages: 8

---


## Page 1


Rethinking set theory
Tom Leinster
As mathematicians, we often read a nice
new proof of a known theorem, enjoy the
diﬀerent approach, but continue to de-
rive our internal understanding from the
method we originally learned. This paper
aims to change drastically the way math-
ematicians think [. . . ] and teach.
—Sheldon Axler [1, Section 10].
Mathematicians manipulate sets with conﬁdence
almost every day of their working lives. We do
so whenever we work with sets of real or com-
plex numbers, or with vector spaces, topological
spaces, groups, or any of the many other set-based
structures.
These underlying set-theoretic ma-
nipulations are so automatic that we seldom give
them a thought, and it is rare that we make mis-
takes in what we do with sets.
However, very few mathematicians could ac-
curately quote what are often referred to as ‘the’
axioms of set theory.
We would not dream
of working with, say, Lie algebras without ﬁrst
learning the axioms. Yet many of us will go our
whole lives without learning ‘the’ axioms for sets,
with no harm to the accuracy of our work. This
suggests that we all carry around with us, more or
less subconsciously, a reliable body of operating
principles that we use when manipulating sets.
What if we were to write down some of these
principles and adopt them as our axioms for sets?
The message of this article is that this can be
done, in a simple, practical way. We describe an
axiomatization due to F. William Lawvere [3, 4],
informally summarized in Fig. 1.
The axioms
suﬃce for very nearly everything mathematicians
ever do with sets. So we can, if we want, aban-
don the classical axioms entirely and use these
instead.
Why rethink?
The traditional axiomatization of sets is known
as Zermelo–Fraenkel with Choice (ZFC). Great
things have been achieved on this axiomatic ba-
sis. However, ZFC has one major ﬂaw: its use
of the word ‘set’ conﬂicts with how most mathe-
maticians use it.
The root of the problem is that in the frame-
work of ZFC, the elements of a set are always sets
too. Thus, given a set X, it always makes sense in
ZFC to ask what the elements of the elements of
X are. Now, a typical set in ordinary mathemat-
ics is R. But accost a mathematician at random
and ask them ‘what are the elements of π?’, and
they will probably assume they misheard you, or
ask you what you’re talking about, or else tell
you that your question makes no sense. If forced
to answer, they might reply that real numbers
have no elements. But this too is in conﬂict with
ZFC’s usage of ‘set’: if all elements of R are sets,
and they all have no elements, then they are all
the empty set, from which it follows that all real
numbers are equal.
1
Composition of functions is associative and has identities
2
There is a set with exactly one element
3
There is a set with no elements
4
A function is determined by its eﬀect on elements
5
Given sets X and Y , one can form their cartesian product X × Y
6
Given sets X and Y , one can form the set of functions from X to Y
7
Given f : X −→Y and y ∈Y , one can form the inverse image f −1(y)
8
The subsets of a set X correspond to the functions from X to {0, 1}
9
The natural numbers form a set
10
Every surjection has a right inverse
Figure 1: Informal summary of the axioms. The primitive concepts are set, function and composition of
functions. Other concepts mentioned (such as element) are deﬁned in terms of the primitive concepts.
1
arXiv:1212.6543v1  [math.LO]  28 Dec 2012


## Page 2


Some of the actual axioms of ZFC are equally
at odds with ordinary mathematical usage. For
example, one states that every nonempty set X
has some element x such that x ∩X = ∅. When
X is an ordinary set such as R, this is a statement
that few would recognize as meaningful: what is
π ∩R, after all?
I will anticipate an objection to these criti-
cisms. The traditional approach to set theory in-
volves not only ZFC, but also a collection of meth-
ods for encoding mathematical objects of many
diﬀerent types (real numbers, diﬀerential opera-
tors, random variables, the Riemann zeta func-
tion, . . . ) as sets. This is similar to the way in
which computer software encodes data of many
types (text, sound, images, . . . ) as binary se-
quences. In both cases, even the designers would
agree that the encoding methods are somewhat
arbitrary. So, one might object, no one is claim-
ing that questions like ‘what are the elements of
π?’ have meaningful answers.
However, our understanding that the encod-
ing is not to be taken too seriously does not alter
the bare facts: that in ZFC, it is always valid
to ask of a set ‘what are the elements of its ele-
ments?’, and in ordinary mathematical practice,
it is not. Perhaps it is misleading to use the same
word, ‘set’, for both purposes.
Three misconceptions
The axiomatization presented below is Lawvere’s
Elementary Theory of the Category of Sets, ﬁrst
proposed half a century ago [3, 4].
Here it is
phrased in a way that requires no knowledge of
category theory whatsoever.
Because of the categorical origins of this
axiomatization, three misconceptions commonly
arise.
The ﬁrst is that the underlying motive is to
replace set theory with category theory. It is not.
The approach described here is not a rival to set
theory: it is set theory.
The second is that this axiomatization de-
mands more mathematical sophistication than
others (such as ZFC). This is false but under-
standable. Almost all of the work on Lawvere’s
axioms has taken place within topos theory: a
beautiful and profound subject, but not one eas-
ily accessible to outsiders.
It has always been
known that the axioms could be presented in a
completely elementary way, and although some
authors have emphasized this [3, 5, 6, 10, 11], it
is not as widely appreciated as it should be. This
paper aims to make it plain.
The third misconception is that because these
axioms for sets come from category theory, and
because the deﬁnition of category involves a col-
lection of objects and a collection of arrows, and
because ‘collection’ might mean something like
‘set’, there is a circularity: in order to axiomatize
sets categorically, we must already know what a
set is. But although our approach is categorically
inspired, it does not depend on having a general
deﬁnition of category. Indeed, our axiomatization
(Section 2) does not contain a single instance of
the word ‘category’.
Put another way, circularity is no more a
problem here than in ZFC. Informally, ZFC says
‘there are some things called sets, there is a binary
relation on sets called membership, and some ax-
ioms hold’. We will say ‘there are some things
called sets and some things called functions, there
is an operation called composition of functions,
and some axioms hold’. In neither case are the
‘things’ required to form a set (whatever that
would mean).
In logical terminology, both ax-
iomatizations are simply ﬁrst-order theories.
1
Prelude: elements as functions
The working mathematician’s vocabulary in-
cludes terms such as set, function, element, sub-
set, and equivalence relation. Any axiomatization
of sets will choose some of these concepts as prim-
itive and derive the others. The traditional choice
is sets and elements. We use sets and functions.
The formal axiomatization is presented in Sec-
tion 2. However, it will be helpful to consider one
aspect in advance: how to derive the concept of
element from the concept of function.
Suppose for now that we have found a char-
acterization of one-element sets without knowing
what an element is. (We do so below.) Fix a one-
element set 1 = {•}. For any set X, a function
1 −→X is essentially just an element of X, since,
after all, such a function f is uniquely determined
by the value of f(•) ∈X (Fig. 2(c)). Thus:
Elements are a special case of functions.
This is such a trivial observation that one is
apt to dismiss it as a mere formal trick. On the
contrary, similar correspondences occur through-
out mathematics. For example (Fig. 2):
• a loop in a topological space X is a continuous
map S1 −→X;
• a straight line in Rn is a distance-preserving
map R −→Rn;
• a sequence in a set X is a function N −→X;
• a solution (x, y) of the equation x2 +y2 = 1 in
a ring A is a homomorphism Z[X, Y ]/(X2 +
Y 2 −1) −→A.
2


## Page 3


S1
X
(a)
R
Rn
(b)
1
X
(c)
Figure 2: Mapping out of a basic object (S1, R, or 1) picks out ﬁgures of the appropriate type (loops,
lines, or elements).
In each case, the word ‘is’ can be taken either as
a deﬁnition or as an assertion of a canonical, one-
to-one correspondence. In the ﬁrst, we map out
of the circle, which is a ‘free-standing’ loop; in
the second, R is a free-standing line; in the third,
the elements 0, 1, 2, . . . of N form a free-standing
sequence; in the last, the pair (X, Y ) of elements
of Z[X, Y ]/(X2+Y 2−1) is the free-standing solu-
tion (x, y) of x2 + y2 = 1. Similarly, in our trivial
situation, the set 1 is a free-standing element, and
an element of a set X is just a map 1 −→X.
We could be fussy and write ¯x, say, for the
function 1 −→X with value x ∈X.
But we
will write ¯x as just x, blurring the distinction. In
fact, we will later deﬁne an element of X to be a
function 1 −→X.
This will make some readers uncomfortable.
There is, you will agree, a canonical one-to-one
correspondence between elements of X and func-
tions 1 −→X, but perhaps you draw the line at
saying that an element of X literally is a func-
tion 1 −→X. If so, this is not a deal-breaker.
We could adapt the axiomatization in Section 2
by adding ‘element’ to the list of primitive con-
cepts.
Then, however, we would need to com-
plicate it further by adding clauses to guarantee
that (among other things) there is a one-to-one
correspondence between elements of X and func-
tions 1 −→X, for any set X. It can be done, but
we choose the more economical route.
We have seen that elements are a special case
of functions. There is another fundamental way
in which functions and elements interact: given
a function f : X −→Y and an element x ∈X,
we can evaluate f at x to obtain a new element,
f(x) ∈Y . Viewing elements as functions out of
1, this element f(x) is nothing but the composite
of f with x:
f(x) = f ◦x.
1
x
/
f(x)

X
f

Y
Hence:
Evaluation is a special case of composition.
2
The axioms
Here we state our ten axioms on sets and func-
tions, in entirely elementary terms.
The formal axiomatization is in a diﬀerent
typeface, to distinguish it from the accompanying
commentary.
Some diagrams appear, but they
are not part of the formal statement.
First we state the data to which our axioms
will apply:
• Some things called sets;
• for each set X and set Y , some things called
functions from X to Y , with functions f from
X to Y written as f : X −→Y or X
f
−→Y ;
• for each set X, set Y and set Z, an operation
assigning to each f : X −→Y and g: Y −→Z
a function g ◦f : X −→Z;
• for each set X, a function 1X : X −→X.
This last item can be included in the list or
not, according to taste. See the comments after
the ﬁrst axiom, which now follows.
Associativity and identity laws
1. For all sets W, X, Y, Z and functions
W
f
−→X
g
−→Y
h
−→Z,
we have h ◦(g ◦f) = (h ◦g) ◦f. For all sets X, Y
and functions f : X −→Y , we have f ◦1X = f =
1Y ◦f.
If we wish to omit the identity functions from
the list of primitive concepts, we must replace the
second half of Axiom 1 by the statement that for
all sets X, there exists a function 1X : X −→X
such that g ◦1X = g for all g: X −→Y and
1X ◦f = f for all f : W −→X. These conditions
characterize 1X uniquely.
One-element set
We would like to say ‘there exists a one-element
set’, but for the moment we lack the expressive
power to say ‘element’. However, any one-element
set T should have the property that for each
set X, there is precisely one function X −→T.
3


## Page 4


Moreover, only one-element sets should have this
property. This motivates the following deﬁnition
and axiom.
A set T is terminal if for every set X, there is
a unique function X −→T.
2. There exists a terminal set.
It follows quickly from the deﬁnitions that
if T and T ′ are terminal sets then there is a
unique isomorphism from T to T ′. (A function
f : A −→B is an isomorphism if there is a
function f ′ : B −→A such that f ′ ◦f = 1A and
f ◦f ′ = 1B.) In other words, terminal sets are
unique up to unique isomorphism. It is therefore
harmless to ﬁx a terminal set 1 once and for all.
Readers worried by this are referred to the last
few paragraphs of this section.
Given a set X, we write x ∈X to mean
x: 1 −→X, and call x an element of X. Given
x ∈X and a function f : X −→Y , we write f(x)
for the element f ◦x: 1 −→Y of Y .
Empty set
3. There exists a set with no elements.
Functions and elements
A function from X to Y should be nothing more
than a way of turning elements of X into elements
of Y .
4. Let X and Y be sets and f, g: X −→Y func-
tions. Suppose that f(x) = g(x) for all x ∈X.
Then f = g.
Axioms 1, 2 and 4 imply that a set is terminal
if and only if it has exactly one element. This jus-
tiﬁes the usage of ‘one-element set’ as a synonym
for ‘terminal set’.
Cartesian products
We want to be able to form cartesian products
of sets.
An element of X together with an el-
ement of Y should uniquely determine an ele-
ment of X × Y . More generally, for any set I,
a function f1 : I −→X together with a function
f2 : I −→Y should uniquely determine a function
f : I −→X × Y , given by f(t) = (f1(t), f2(t)).
(To see that this really is ‘more generally’, take
I = 1.) We can recover f1 from f by compos-
ing with the projection p1 : X × Y −→X, and
similarly f2, as in the following deﬁnition.
Let X and Y be sets. A product of X and Y
is a set P together with functions X
p1
←−P
p2
−→Y ,
with the following property:
for all sets I and functions X
f1
←−I
f2
−→Y ,
there is a unique function (f1, f2): I −→P
such that p1 ◦(f1, f2) = f1 and p2 ◦(f1, f2) = f2.
I
P
X
Y
f1

f2

(f1,f2)

p1
u
p2
)
5. Every pair of sets has a product.
Strictly speaking, a product consists of not
only the set P but also the projections p1 and
p2. Any two products of X and Y are uniquely
isomorphic:
that is, given products (P, p1, p2)
and (P ′, p′
1, p′
2), there is a unique isomorphism
i: P −→P ′ such that p′
1 ◦i = p1 and p′
2 ◦i = p2.
As in the case of terminal sets, this makes it
harmless to choose once and for all a preferred
product (X ×Y, prX,Y
1
, prX,Y
2
) for each pair X, Y
of sets. Again, this convention is justiﬁed at the
end of the section.
Sets of functions
In everyday mathematics, we can form the set
Y X of functions from one set X to another set Y .
For any set I, the functions q: I ×X −→Y corre-
spond one-to-one with the functions ¯q: I −→Y X,
simply by changing the punctuation:
q(t, x) = (¯q(t))(x)
(1)
(t ∈I, x ∈X).
For example, when I = 1,
this reduces to the statement that the functions
X −→Y correspond to the elements of Y X.
In (1), we are implicitly using the evaluation
map
ε:
Y X × X
−→
Y
(f, x)
7−→
f(x).
Then
(1)
becomes
the
equation
q(t, x)
=
ε(¯q(t), x), as in the following deﬁnition.
Let X and Y be sets. A function set from X to
Y is a set F together with a function ε: F ×X −→
Y , with the following property:
for all sets I and functions q: I × X −→Y ,
there is a unique function ¯q: I −→F
such that q(t, x) = ε(¯q(t), x) for all t ∈I, x ∈X.
I × X
¯q×1X

q
#
F × X
ε
/ Y
6. For all sets X and Y , there exists a function set
from X to Y .
4


## Page 5


Inverse images
Ordinarily, given a function f : X −→Y and
an element y of Y , we can form the inverse
image or ﬁbre f −1(y).
The inclusion function
j : f −1(y) ,→X has the property that f ◦j has
constant value y. Moreover, whenever q: I −→X
is a function such that f ◦q has constant value y,
the image of q must lie within f −1(y); that is,
q = j ◦¯q for some ¯q: I −→f −1(y) (necessarily
unique).
Let f : X −→Y be a function and y ∈Y . An
inverse image of y under f is a set A together with
a function j : A −→X, such that f(j(a)) = y for
all a ∈A and the following property holds:
for all sets I and functions q: I −→X such that
f(q(t)) = y for all t ∈I,
there is a unique function ¯q: I −→A
such that q = j ◦¯q.
A
1
X
Y
I
j

/
f
/
y

q
"
'
¯q
(
7.
For every function f : X −→Y and element
y ∈Y , there exists an inverse image of y under f.
Inverse images are essentially unique:
if
j : A −→X and j′ : A′ −→X are both inverse
images of y under f, there is a unique isomor-
phism i: A −→A′ such that j′ ◦i = j.
Characteristic functions
Sometimes we want to deﬁne a function on a case-
by-case basis. For example, we might want to de-
ﬁne h: R −→R by h(x) = x sin(1/x) if x ̸= 0 and
h(0) = 0. A simple instance is the deﬁnition of
characteristic function.
Fix a two element-set 2 = {t, f} (for ‘true’
and ‘false’). The characteristic function of a sub-
set A ⊆X is the function χA : X −→2 deﬁned
by χA(x) = t if x ∈A and χA(x) = f otherwise.
It is the unique function χ: X −→2 such that
χ−1(t) = A.
This is how characteristic functions work ordi-
narily. To ensure that they work in the same way
in our set theory, we now demand that there exist
a set 2 and an element t ∈2 with the property
just described: whenever X is a set and A ⊆X,
there is a unique function χ: X −→2 such that
χ−1(t) = A.
Since we do not yet have a deﬁnition of sub-
set, we phrase the axiom in terms of injections
instead. This works because every subset inclu-
sion A ,→X is injective, and, up to isomorphism,
every injection arises in this way.
An injection is a function j : A −→X such that
j(a) = j(a′) =⇒a = a′ for a, a′ ∈A.
A subset classiﬁer is a set 2 together with an
element t ∈2, with the following property:
for all sets A, X and injections j : A −→X,
there is a unique function χ: X −→2 such that
j : A −→X is an inverse image of t under χ.
A
/
j

1
t

X
χ
/ 2
8. There exists a subset classiﬁer.
The notation 2 is merely suggestive. There is
nothing in the deﬁnition saying that 2 must have
two elements, but, nontrivially, our ten axioms do
in fact imply this.
Natural numbers
In ordinary mathematics, sequences can be de-
ﬁned recursively:
given a set X, an element
a ∈X, and a function r: X −→X, there is a
unique sequence (xn)∞
n=0 in X such that
x0 = a and xn+1 = r(xn) for all n ∈N.
A sequence in X is nothing but a function N −→
X, so the previous sentence is really a statement
about the set N. It also refers to two pieces of
structure on N: the element 0 and the function
s: N −→N given by s(n) = n + 1.
A natural number system is a set N together
with an element 0 ∈N and a function s: N −→N,
with the following property:
whenever X is a set, a ∈X, and r: X −→X,
there is a unique function x: N −→X such that
x(0) = a and x(s(n)) = r(x(n)) for all n ∈N.
1
0
/
11

N
s
/
x

N
x

1
a
/ X
r
/ X
9. There exists a natural number system.
Natural
number
systems
are
essentially
unique, in the usual sense that between any two
of them there is a unique structure-preserving iso-
morphism. This justiﬁes speaking of the natural
numbers N, as we invariably do.
5


## Page 6


Choice
A function with a right inverse is certainly sur-
jective. The axiom of choice states the converse.
A surjection is a function s: X −→Y such that
for all y ∈Y , there exists x ∈X with s(x) = y.
A right inverse of a function s: X −→Y is a
function i: Y −→X such that s ◦i = 1Y .
10. Every surjection has a right inverse.
A right inverse of a surjection s: X −→Y is
a choice, for each y ∈Y , of an element of the
nonempty set s−1(y).
This concludes the axiomatization.
The meaning of ‘the’
It remains to reassure any readers concerned by
the liberty taken in Axioms 2 and 5, where we
chose once and for all a terminal set and a carte-
sian product for each pair of sets.
This type of liberty is very common in math-
ematical practice. We speak of the trivial group,
the 2-sphere, the direct sum of two vector spaces,
etc., even though we can conceive of many trivial
groups or 2-spheres or direct sums, all isomorphic
but not equal.
Anyone asking ‘but which triv-
ial group?’ is likely to be met with a hard stare,
for good reason: no meaningful statement about
groups depends on what the element of the trivial
group happens to be called.
However, we should be able to state the ax-
ioms with scrupulous rigour, and we can.
One
way to do so is not to single out a particular ter-
minal set or particular products, but instead to
adopt some circumlocutions: for example, replac-
ing the phrase ‘for all elements x ∈X’ by ‘for all
terminal sets T and functions x: T −→X’.
More satisfactory, though, is to extend the list
of primitive concepts. To the existing list (sets,
functions, composition and identities) we add:
• a distinguished set, 1;
• an operation assigning to each pair of sets X, Y
a set X × Y and functions
X
X × Y
prX,Y
1
o
prX,Y
2
/Y.
(2)
Axiom 2 is replaced by the statement that 1 is
terminal, and Axiom 5 by the statement that for
all sets X and Y , the set X ×Y together with the
functions (2) is a product of X and Y .
This approach has the virtue of reﬂecting ordi-
nary mathematical usage. We usually speak as if
taking the product of two sets (or spaces, groups,
etc.) were a procedure with a deﬁnite output: the
product, not a product. But since products are
in any case determined uniquely up to unique iso-
morphism, whether or not we nominate one as
special makes no signiﬁcant diﬀerence.
3
Discussion
The ten axioms are familiar in their intuitive con-
tent, but less so as an axiomatic system. Here we
discuss the implications of using them as such.
Building on the axioms
Any axiomatization of anything is followed by a
period of lemma-proving. The present axioms are
no exception. Here is a very brief sketch of the
development.
It is convenient formally to deﬁne a subset
of a set X as a function X −→2, but we con-
stantly use the correspondence between functions
X −→2 and injections into X, provided by Ax-
iom 8. Two injections j, j′ into X correspond to
the same subset of X if and only if they have the
same image (that is, there exists an isomorphism
i such that j′ = j ◦i).
The main task is to build the everyday equip-
ment used for manipulating sets. For example,
given a function f : X −→Y , we construct the
image under f of a subset of X and the inverse
image of a subset of Y . An equivalence relation
∼on a set X is deﬁned to be a subset of X × X
with the customary properties, and the axioms al-
low us to construct the quotient set X/∼. Some
constructions are tricky: for instance, the axioms
imply that any two sets X and Y have a disjoint
union X ⊔Y , but this is by no means obvious.
We then deﬁne the usual number systems.
Addition, multiplication and powers of natural
numbers are deﬁned directly using Axiom 9.
From N we successively construct Z, Q, R and C,
in the standard way. For example, Z = (N×N)/∼,
where ∼is the equivalence relation on N×N given
by (m, n) ∼(m′, n′) if and only if m+n′ = m′+n.
As this illustrates, past a certain point, the de-
velopment is literally identical to that for other
axiomatizations of sets.
How strong are the axioms?
Most mathematicians will never use more prop-
erties of sets than those guaranteed by the ten
axioms. For example, McLarty [13] argues that
no more is needed anywhere in the canons of
the Grothendieck school of algebraic geometry,
the multi-volume works ´El´ements de G´eom´etrie
Alg´ebrique (EGA) and S´eminaire de G´eom´etrie
Alg´ebrique (SGA).
To get a sense of the reach of the axioms, let
us consider inﬁnite cartesian products. Let I be a
6


## Page 7


(possibly inﬁnite) set and (Xi)i∈I a family of sets.
Can we form the product Q
i∈I Xi? It depends
on what is meant by ‘family’. We could deﬁne
an I-indexed family to be a set X together with
a function p: X −→I, viewing the ﬁbre p−1(i)
as the ith member Xi. In that case, Q Xi can
be constructed as a subset of XI. Speciﬁcally, p
induces a function pI : XI −→II, and Q Xi is
the inverse image under pI of the element of II
corresponding to 1I.
However, we could interpret ‘I-indexed fam-
ily’ diﬀerently: as an algorithm or formula that
assigns to each i ∈I a set Xi.
It is not ob-
vious that we can then form the disjoint union
X = `
i∈I Xi, which is what would be necessary
in order to obtain a family in the previous sense.
In fact, writing P(S) = 2S for the power set of a
set S, the ten axioms do not guarantee the exis-
tence of the disjoint union
N ⊔P(N) ⊔P(P(N)) ⊔· · ·
(3)
unless they are inconsistent ([8], Section 9).
If we wish to change this, we can add an
eleventh axiom (or properly, axiom scheme),
called ‘replacement’ and informally stated as fol-
lows. Suppose we have a set I and a ﬁrst-order
formula that for each i ∈I speciﬁes a set Xi up to
isomorphism. Then we require that there exist a
set X and a function p: X −→I such that p−1(i)
is isomorphic to Xi for each i ∈I. (See Section 8
of [12] for a formal statement.) This guarantees
the existence of sets such as (3).
The relationship between our axioms and ZFC
is well understood. The ten axioms are weaker
than ZFC; but when the eleventh is added, the
two theories have equal strength and are ‘bi-
interpretable’ (the same theorems hold). More-
over, it is known to which fragment of ZFC the
ten axioms correspond: ‘Zermelo with bounded
comprehension and choice’.
The details of this
relationship were mostly worked out in the early
1970s [2, 14, 15]. Good modern accounts are in
Section VI.10 of [7] and Chapter 22 of [9].
A broader view
Our ten axioms are a standard rephrasing of Law-
vere’s Elementary Theory of the Category of Sets
(ETCS), published in 1964. It was some years be-
fore ETCS found its natural home, and that was
with the advent of topos theory.
The
notion
of
topos
was
invented
by
Grothendieck for reasons that had nothing to do
with set theory. For Grothendieck, a topos was a
generalized topological space. Formally, a topos
is a category with certain properties, and a topo-
logical space X is associated with the topos whose
objects are the sheaves of sets on X.
Lawvere and Tierney swiftly realized that, af-
ter a slight loosening of Grothendieck’s deﬁni-
tion, the ETCS axioms could be restated neatly
in topos-theoretic terms [16, 17]. Indeed, ETCS
says exactly that sets and functions form a topos
of a special sort: a ‘well-pointed topos with natu-
ral numbers object and choice’. So a topos is not
only a generalized space; it is also a generalized
universe of sets.
An attractive feature of ETCS is that each
of the axioms is meaningful in a broader context
than set theory. For example, Axiom 1 states that
sets and functions form a category. The job of the
remaining axioms is to distinguish sets from other
structures that form categories. Axioms 2 and 5
state that the category of sets has ﬁnite prod-
ucts. This important property is shared by (for
example) the categories of topological spaces and
smooth manifolds, which is exactly what makes
it possible to deﬁne ‘topological group’ and ‘Lie
group’. But for one detail, Axioms 1, 2, 5, 6, 7
and 8 state that sets and functions form a topos.
Skipping to Axiom 10, the axiom of choice
as formulated there highlights a special feature
of sets.
In most other categories of sets-with-
structure, it fails, and its failure is a point of in-
terest. For instance, not every continuous surjec-
tion between topological spaces has a continuous
right inverse, a typical example being the nonex-
istence of a continuous square root deﬁned on the
complex plane.
What kind of set theory should we teach?
As Fig. 1 indicates, we already teach a diluted
form of the ten axioms, even in introductory
courses. For example, we certainly tell our stu-
dents that an element of X×Y is an element of X
together with an element of Y , and we routinely
write a function f taking values in R2 as (f1, f2),
although we are less likely to state explicitly that
given functions f1 : I −→X and f2 : I −→Y ,
there is a unique function f : I −→X × Y with
f1 and f2 as components.
When it comes to teaching axiomatic set the-
ory, the approach outlined here has advantages
and disadvantages.
The big advantage is that
such a course is of far wider beneﬁt than one us-
ing the traditional axioms. It directly addresses a
diﬃculty experienced by many students: the con-
cept of function (and worse, function space). It
also introduces in an elementary setting the idea
of universal property. This is probably the hard-
est aspect of the axioms for a learner, but since
universal properties are important in so many
branches of advanced mathematics, the beneﬁts
are potentially far-reaching.
The disadvantages are perhaps only tempo-
7


## Page 8


rary. There is at present a lack of teaching mate-
rials (the book [5] being the main exception). For
example, the axioms imply that any two sets have
a disjoint union, and most books on topos theory
contain an elegant and sophisticated proof of a
generalization of this fact, but to my knowledge,
there is only one place where a purely elementary
proof can be found [18]. A second disadvantage is
that any student planning a career in set theory
will need to learn ZFC anyway, since almost all
research-level set theory is done with the iterated-
membership conception of set. (That is the cur-
rent reality, which is not to say that set theory
must be done this way.)
Reactions to an earthquake
Perhaps you will wake up tomorrow, check your
email, and ﬁnd an announcement that ZFC is in-
consistent.
Apparently, someone has taken the
ZFC axioms, performed a long string of logical
deductions, and arrived at a contradiction. The
work has been checked and re-checked. There is
no longer any doubt.
How would you react?
In particular, how
would you feel about the implications for your
own work? All your theorems would still be true
under ZFC, but so too would their negations.
Would you conclude that your life’s work had
been destroyed?
I believe that most of us would be interested
but not deeply troubled.
We would go on be-
lieving that our theorems were true in a sense
that their negations were not. We are unlikely to
feel threatened by the inconsistency of axioms to
which we never referred anyway.
In contrast, the ten axioms above are such
core mathematical principles that an inconsis-
tency in them would be devastating. If we cannot
safely assume that composition of functions is as-
sociative, or that repeatedly applying a function
f : X −→X to an element a ∈X produces a
sequence (f n(a)), we are really in trouble.
As the weaker system, the ten axioms are less
likely to be inconsistent than ZFC. But the ques-
tion of strength is peripheral to this article (and in
any case, if one wants a system of equal strength
to ZFC, all one needs to do is add the aforemen-
tioned eleventh axiom). The real message is this:
simply by writing down a few mundane, uncon-
troversial statements about sets and functions, we
arrive at an axiomatization that reﬂects how sets
are used in everyday mathematics.
Acknowledgements
I thank Fran¸cois Dorais,
Colin McLarty, Todd Trimble and the patrons of
the n-Category Caf´e.
This work was partially
supported by an EPSRC Advanced Research Fel-
lowship.
References
[1] S. Axler. Down with determinants!
American
Mathematical Monthly, 102:139–154, 1995.
[2] J. C. Cole. Categories of sets and models of set
theory. In J. Bell and A. Slomson, editors, Pro-
ceedings of the Bertrand Russell Memorial Logic
Conference, Uldum 1971, pages 351–399. 1973.
[3] F. W. Lawvere.
An elementary theory of the
category of sets.
Proceedings of the National
Academy of Sciences of the U.S.A., 52:1506–
1511, 1964.
[4] F. W. Lawvere. An elementary theory of the cat-
egory of sets (long version) with commentary.
Reprints in Theory and Applications of Cate-
gories, 12:1–35, 2005.
[5] F. W. Lawvere and R. Rosebrugh. Sets for Math-
ematics.
Cambridge University Press, Cam-
bridge, 2003.
[6] S. Mac Lane. Mathematics: Form and Function.
Springer, New York, 1986.
[7] S. Mac Lane and I. Moerdijk. Sheaves in Geom-
etry and Logic. Springer, New York, 1994.
[8] A. Mathias. The strength of Mac Lane set the-
ory. Annals of Pure and Applied Logic, 110:107–
234, 2001.
[9] C. McLarty. Elementary Categories, Elementary
Toposes. Oxford University Press, 1992.
[10] C. McLarty.
Numbers can be just what they
have to. Noˆus, 27:487–98, 1993.
[11] C. McLarty. Challenge axioms, ﬁnal draft. Email
to Foundations of Mathematics mailing list, 6
February 1998, archived at http://www.cs.nyu.
edu/pipermail/fom, 1998.
[12] C. McLarty. Exploring categorical structuralism.
Philosophia Mathematica, 12:37–53, 2004.
[13] C. McLarty. A ﬁnite order arithmetic foundation
for cohomology. arXiv:1102.1773, 2011.
[14] W. Mitchell.
Boolean topoi and the theory
of sets.
Journal of Pure and Applied Algebra,
2:261–274, 1972.
[15] G. Osius. Categorical set theory: a characteri-
zation of the category of sets. Journal of Pure
and Applied Algebra, 4:79–119, 1974.
[16] M. Tierney.
Sheaf theory and the continuum
hypothesis. In F. W. Lawvere, editor, Toposes,
Algebraic Geometry and Logic, volume 274 of
Lecture Notes in Mathematics, pages 13–42.
Springer, 1972.
[17] M. Tierney. Axiomatic sheaf theory: some con-
structions and applications. In P. Salmon, editor,
Proceedings of CIME Conference on Categories
and Commutative Algebra, Varenna, 1971, pages
249–326. Edizione Cremonese, 1973.
[18] T. Trimble. ETCS: building joins and coprod-
ucts.
http://ncatlab.org/nlab/show/Trimble+
on+ETCS+III, 2008.
School of Mathematics, University of Edinburgh,
Edinburgh EH9 3JZ, United Kingdom.
Tom.Leinster@ed.ac.uk
8

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1212_6543v1_rethinking_set_theory
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2012/1212_6543V1_RETHINKING_SET_THEORY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
