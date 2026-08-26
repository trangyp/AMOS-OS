---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1308.4526v5
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1308.4526v5_Formalization__Mechanization_and_Automation_of_Gödel_s_Proof_of_God_s_Existence

> Source: 1308.4526v5_Formalization__Mechanization_and_Automation_of_Gödel_s_Proof_of_God_s_Existence.pdf

> Pages: 4

---


## Page 1


arXiv:1308.4526v5  [cs.LO]  3 Sep 2017
Formalization, Mechanization and Automation of
G¨odel’s Proof of God’s Existence⋆
Christoph Benzm¨uller1 and Bruno Woltzenlogel Paleo2
1 Dahlem Center for Intelligent Systems, Freie Universit¨at Berlin, Germany
c.benzmueller@gmail.com
2 Theory and Logic Group, Vienna University of Technology, Austria
bruno@logic.at
Update (31/08/2017): The abstract below, uploaded to arXiv on 21/08/2013, was the ﬁrst
communication of the computer-assisted formalization of G¨odel’s ontological proof. Since then, the
following longer papers have been published: [11,10,19,13,12,8,7,16,15,14,17,9,18,20,3,38,29,21,28].
Attempts to prove the existence (or non-existence) of God by means of abstract ontological
arguments are an old tradition in philosophy and theology. G¨odel’s proof [30,31] is a modern
culmination of this tradition, following particularly the footsteps of Leibniz. G¨odel deﬁnes God
as a being who possesses all positive properties. He does not extensively discuss what positive
properties are, but instead he states a few reasonable (but debatable) axioms that they should
satisfy. Various slightly diﬀerent versions of axioms and deﬁnitions have been considered by G¨odel
and by several philosophers who commented on his proof (cf. [36,2,27,1,26]).
Dana Scott’s version of G¨odel’s proof [35] employs the following axioms (A), deﬁnitions (D),
corollaries (C) and theorems (T), and it proceeds in the following order:3
A1 Either a property or its negation is positive, but not both:
∀φ[P(¬φ) ↔¬P(φ)]
A2 A property necessarily implied
by a positive property is positive:
∀φ∀ψ[(P(φ) ∧□∀x[φ(x) →ψ(x)]) →P(ψ)]
T1 Positive properties are possibly exempliﬁed:
∀ϕ[P(ϕ) →♦∃xϕ(x)]
D1 A God-like being possesses all positive properties:
G(x) ↔∀φ[P(φ) →φ(x)]
A3 The property of being God-like is positive:
P(G)
C
Possibly, God exists:
♦∃xG(x)
A4 Positive properties are necessarily positive:
∀φ[P(φ) →□P(φ)]
D2 An essence of an individual is
a property possessed by it and
necessarily implying any of its properties:
φ ess. x ↔φ(x) ∧∀ψ(ψ(x) →□∀y(φ(y) →ψ(y)))
T2 Being God-like is an essence of any God-like being:
∀x[G(x) →G ess. x]
D3 Necessary existence of an individual is
the necessary exempliﬁcation of all its essences:
NE(x) ↔∀φ[φ ess. x →□∃yφ(y)]
A5 Necessary existence is a positive property:
P(NE)
T3 Necessarily, God exists:
□∃xG(x)
Scott’s version of G¨odel’s proof has now been analysed for the ﬁrst-time with an unprecedent
degree of detail and formality with the help of theorem provers; cf. [40,39]. The following has been
done (and in this order):
– A detailed natural deduction proof.
– A formalization of the axioms, deﬁnitions and theorems in the TPTP THF syntax [37].
⋆This work has been supported by the German Research Foundation under grant BE2501/9-1.
3 A1, A2, A5, D1, D3 are logically equivalent to, respectively, axioms 2, 5 and 4 and deﬁnitions 1 and
3 in G¨odel’s notes [30,31]. A3 was introduced by Scott [35] and could be derived from G¨odel’s axiom 1
and D1 in a logic with inﬁnitary conjunction. A4 is a weaker form of G¨odel’s axiom 3. D2 has an extra
conjunct φ(x) lacking in G¨odel’s deﬁnition 2; this is believed to have been an oversight by G¨odel [32].


## Page 2


– Automatic veriﬁcation of the consistency of the axioms and deﬁnitions with Nitpick [24].
– Automatic demonstration of the theorems with the provers LEO-II [6] and Satallax [25].
– A step-by-step formalization using the Coq proof assistant [22].
– A formalization using the Isabelle proof assistant [34], where the theorems (and some additional
lemmata) have been automated with Sledgehammer [23] and Metis [33].
G¨odel’s proof is challenging to formalize and verify because it requires an expressive logical
language with modal operators (possibly and necessarily) and with quantiﬁers for individuals and
properties. Our computer-assisted formalizations rely on an embedding of the modal logic into
classical higher-order logic with Henkin semantics [5,4]. The formalization is thus essentially done
in classical higher-order logic where quantiﬁed modal logic is emulated.
In our ongoing computer-assisted study of G¨odel’s proof we have obtained the following results:
– The basic modal logic K is suﬃcient for proving T1, C and T2.
– Modal logic S5 is not needed for proving T3; the logic KB is suﬃcient.
– Without the ﬁrst conjunct φ(x) in D2 the set of axioms and deﬁnitions would be inconsistent.
– For proving theorem T1, only the left to right direction of axiom A1 is needed. However, the
backward direction of A1 is required for proving T2.
This work attests the maturity of contemporary interactive and automated deduction tools
for classical higher-order logic and demonstrates the elegance and practical relevance of the
embeddings-based approach. Most importantly, our work opens new perspectives for a computer-
assisted theoretical philosophy. The critical discussion of the underlying concepts, deﬁnitions and
axioms remains a human responsibility, but the computer can assist in building and checking rig-
orously correct logical arguments. In case of logico-philosophical disputes, the computer can check
the disputing arguments and partially fulﬁll Leibniz’ dictum: Calculemus — Let us calculate!
References
1. R.M. Adams. Introductory note to *1970. In Kurt G¨odel: Collected Works Vol. 3: Unpublished Essays
and Letters. Oxford University Press, 1995.
2. A.C. Anderson and M. Gettings. G¨odel ontological proof revisited. In G¨odel’96: Logical Foundations
of Mathematics, Computer Science, and Physics: Lecture Notes in Logic 6, pages 167–172. Springer,
1996.
3. Matthias Bentert, Christoph Benzm¨uller, David Streit, and Bruno Woltzenlogel Paleo. Analysis of an
ontological proof proposed by Leibniz. In Charles Tandy, editor, Death and Anti-Death, Volume 14:
Four Decades after Michael Polanyi, Three Centuries after G.W. Leibniz. Ria University Press, 2016.
4. C. Benzm¨uller and L.C. Paulson. Exploring properties of normal multimodal logics in simple type
theory with LEO-II. In Festschrift in Honor of Peter B. Andrews on His 70th Birthday, pages 386–406.
College Publications, 2008.
5. C. Benzm¨uller and L.C. Paulson. Quantiﬁed multimodal logics in simple type theory. Logica Univer-
salis (Special Issue on Multimodal Logics), 7(1):7–20, 2013.
6. C. Benzm¨uller, F. Theiss, L. Paulson, and A. Fietzke. LEO-II - a cooperative automatic theorem prover
for higher-order logic. In Proc. of IJCAR 2008, volume 5195 of LNAI, pages 162–170. Springer, 2008.
7. Christoph Benzm¨uller. G¨odel’s ontological argument revisited – ﬁndings from a computer-supported
analysis (invited). In Ricardo Souza Silvestre and Jean-Yves B´eziau, editors, Handbook of the 1st
World Congress on Logic and Religion, Jo˜ao Pessoa, Brazil, page 13, 2015. (Invited abstract).
8. Christoph Benzm¨uller, Leon Weber, and Bruno Woltzenlogel Paleo. Computer-assisted analysis of the
Anderson-H´ajek ontological controversy. In Ricardo Souza Silvestre and Jean-Yves B´eziau, editors,
Handbook of the 1st World Congress on Logic and Religion, Joao Pessoa, Brasil, pages 53–54, 2015.
(superseded by 2016 article in Logica Universalis).
9. Christoph Benzm¨uller, Leon Weber, and Bruno Woltzenlogel Paleo. Computer-assisted analysis of
the Anderson-H´ajek controversy. Logica Universalis, 11(1):139–151, 2017.
10. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo.
G¨odel’s God in Isabelle/HOL.
Archive of
Formal Proofs, 2013. (Formally veriﬁed).
11. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. G¨odel’s God on the computer. In S. Schulz,
G. Sutcliﬀe, and B. Konev, editors, Proceedings of the 10th International Workshop on the Implemen-
tation of Logics, 2013. (Invited paper).


## Page 3


12. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. Automating G¨odel’s ontological proof of God’s
existence with higher-order automated theorem provers. In Torsten Schaub, Gerhard Friedrich, and
Barry O’Sullivan, editors, ECAI 2014, volume 263 of Frontiers in Artiﬁcial Intelligence and Applica-
tions, pages 93 – 98. IOS Press, 2014.
13. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. G¨odel’s proof of God’s existence. In Jean-Yves
Beziau and Katarzyna Gan-Krzywoszynska, editors, Handbook of the World Congress on the Square
of Opposition IV, pages 22–23, 2014. (superseded by ECAI-2014 paper).
14. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. Experiments in computational metaphysics:
G¨odel’s proof of god’s existence.
In Subhash C. Mishram, Ramgopal Uppaluri, and Varun Agar-
wal, editors, Science & Spiritual Quest, Proceedings of the 9th All India Students’ Conference, 30th
October – 1 November, 2015, IIT Kharagpur, India, pages 23–40. Bhaktivedanta Institute, Kolkata,
www.binstitute.org, 2015. (Invited paper, superseded by article in Savijnanam).
15. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. Higher-order modal logics: Automation and
applications. In Adrian Paschke and Wolfgang Faber, editors, Reasoning Web. Web Logic Rules - 11th
International Summer School 2015, Berlin, Germany, July 31 - August 4, 2015, Tutorial Lectures,
number 9203 in LNCS, pages 32–74, Berlin, Germany, 2015. Springer.
16. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. Interacting with modal logics in the Coq proof
assistant. In Lev D. Beklemishev and Daniil V. Musatov, editors, Computer Science - Theory and
Applications - 10th International Computer Science Symposium in Russia, CSR 2015, Listvyanka,
Russia, July 13-17, 2015, Proceedings, volume 9139 of LNCS, pages 398–411. Springer, 2015.
17. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. On logic embeddings and G¨odel’s God. In Mihai
Codescu, Razvan Diaconescu, and Ionut Tutu, editors, Recent Trends in Algebraic Development Tech-
niques: 22nd International Workshop, WADT 2014, Sinaia, Romania, September 4-7, 2014, Revised
Selected Papers, number 9563 in LNCS, pages 3–6, Sinaia, Romania, 2015. Springer. (Invited paper).
18. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. The inconsistency in G¨odel’s ontological argu-
ment: A success story for AI in metaphysics. In Subbarao Kambhampati, editor, IJCAI 2016, volume
1-3, pages 936–942. AAAI Press, 2016.
19. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. The modal collapse as a collapse of the modal
square of opposition. In Jean-Yves B´eziau and Gianfranco Basti, editors, The Square of Opposition:
A Cornerstone of Thought (Collection of papers related to the World Congress on the Square of
Opposition IV, Vatican, 2014), http: // www. springer. com/ us/ book/ 9783319450612 , Studies in
Universal Logic. Springer International Publishing Switzerland, 2016.
20. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. An object-logic explanation for the inconsistency
in G¨odel’s ontological theory (extended abstract, sister conferences). In Malte Helmert and Franz
Wotawa, editors, KI 2016: Advances in Artiﬁcial Intelligence, Proceedings, LNCS, pages 244–250,
Berlin, Germany, 2016. Springer.
21. Christoph Benzm¨uller and Bruno Woltzenlogel Paleo. Experiments in Computational Metaphysics:
G¨odel’s proof of God’s existence. Savijnanam: scientiﬁc exploration for a spiritual paradigm. Journal
of the Bhaktivedanta Institute, 9:43–57, 2017.
22. Y. Bertot and P. Casteran. Interactive Theorem Proving and Program Development. Springer, 2004.
23. J.C. Blanchette, S. B¨ohme, and L.C. Paulson. Extending Sledgehammer with SMT solvers. Journal
of Automated Reasoning, 51(1):109–128, 2013.
24. J.C. Blanchette and T. Nipkow. Nitpick: A counterexample generator for higher-order logic based
on a relational model ﬁnder. In Proc. of ITP 2010, number 6172 in LNCS, pages 131–146. Springer,
2010.
25. C.E. Brown. Satallax: An automated higher-order prover. In Proc. of IJCAR 2012, number 7364 in
LNAI, pages 111 – 117. Springer, 2012.
26. R.
Corazzon.
Contemporary
bibligraphy
on
the
ontological
proof
(http://www.ontology.co/biblio/ontological-proof-contemporary-biblio.htm).
27. M. Fitting. Types, Tableaux and G¨odel’s God. Kluver Academic Press, 2002.
28. David Fuenmayor and Christoph Benzm¨uller. Automating emendations of the ontological argument
in intensional higher-order modal logic. In KI 2017: Advances in Artiﬁcial Intelligence 40th Annual
German Conference on AI, LNAI. Springer, 2017.
29. David Fuenmayor and Christoph Benzm¨uller. Types, Tableaus and G¨odel’s God in Isabelle/HOL.
Archive of Formal Proofs, 2017. Formally veriﬁed with Isabelle/HOL.
30. K. G¨odel. Ontological proof. In Kurt G¨odel: Collected Works Vol. 3: Unpublished Essays and Letters.
Oxford University Press, 1970.
31. K. G¨odel. Appendix A. Notes in Kurt G¨odel’s Hand, pages 144–145. In [36], 2004.
32. A.P. Hazen. On g¨odel’s ontological proof. Australasian Journal of Philosophy, 76:361–377, 1998.


## Page 4


33. J. Hurd. First-order proof tactics in higher-order logic theorem provers. In Design and Application of
Strategies/Tactics in Higher Order Logics, NASA Tech. Rep. NASA/CP-2003-212448, pages 56–68,
2003.
34. T. Nipkow, L.C. Paulson, and M. Wenzel. Isabelle/HOL: A Proof Assistant for Higher-Order Logic.
Number 2283 in LNCS. Springer, 2002.
35. D. Scott. Appendix B. Notes in Dana Scott’s Hand, pages 145–146. In [36], 2004.
36. J.H. Sobel. Logic and Theism: Arguments for and Against Beliefs in God. Cambridge U. Press, 2004.
37. G. Sutcliﬀe and C. Benzm¨uller. Automated reasoning in higher-order logic using the TPTP THF
infrastructure. Journal of Formalized Reasoning, 3(1):1–27, 2010.
38. B. Woltzenlogel Paleo. Leibniz’s characteristica universalis and calculus ratiocinator today. In Charles
Tandy, editor, Death and Anti-Death, Volume 14: Four Decades after Michael Polanyi, Three Centuries
after G. W. Leibniz. Ria University Press, 2016.
39. B.
Woltzenlogel
Paleo
and
C.
Benzm¨uller.
Computational
philosophy
repository
(https://gitlab.com/aossie/ComputationalPhilosophy/).
40. B.
Woltzenlogel
Paleo
and
C.
Benzm¨uller.
Formal
theology
repository
(https://github.com/FormalTheology/GoedelGod).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]