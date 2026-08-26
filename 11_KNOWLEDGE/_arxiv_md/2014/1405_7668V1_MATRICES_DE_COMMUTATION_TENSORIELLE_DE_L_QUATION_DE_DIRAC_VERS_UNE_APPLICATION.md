---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1405.7668v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1405.7668v1_Matrices_de_commutation_tensorielle__de_l_équation_de_Dirac_vers_une_application

> Source: 1405.7668v1_Matrices_de_commutation_tensorielle__de_l_équation_de_Dirac_vers_une_application.pdf

> Pages: 68

---


## Page 1


arXiv:1405.7668v1  [physics.gen-ph]  26 May 2014
i
UNIVERSITE D’ANTANANARIVO
FACULTE DES SCIENCES
FORMATION DOCTORALE EN PHYSIQUE
DEPARTEMENT DE PHYSIQUE
Laboratoire de Rhéologie des Suspensions
MEMOIRE D’HABILITATION A
DIRIGER DES RECHERCHES
option : Mécanique et physique des suspensions
sur :
MATRICES DE COMMUTATION TENSORIELLE :
DE L’EQUATION DE DIRAC VERS UNE
APPLICATION EN PHYSIQUE DES PARTICULES
présenté par
RAKOTONIRINA Christian
devant la commission d’examen composée de :
Président :
Monsieur RAKOTOMAHANINA RALAISOA
Emile
Professeur émérite
Rapporteurs :
Madame RANDRIAMANANTANY Zely Arivelo
Professeur titulaire
Madame RAZANAJATOVO Mariette
Professeur titulaire
Monsieur RAKOTOMALALA Jean Lalaina
Professeur
Examinateurs :
Monsieur RANAIVO-NOMENJANAHARY Flavien Professeur titulaire
Monsieur ANDRIAMAMPIANINA José
Professeur
Directeur de HDR :Monsieur RATIARISON Adolphe Andriamanga
Professeur titulaire


## Page 2


ii


## Page 3


MATRICES DE COMMUTATION
TENSORIELLE : DE L’EQUATION DE
DIRAC VERS UNE APPLICATION EN
PHYSIQUE DES PARTICULES
RAKOTONIRINA Christian
26 septembre 2018


## Page 4


ii
Abstract
We construct two sets of representations of the Dirac equation. They trans-
form themselves from one to another in multiplying by the tensor commu-
tation matrix (TCM) 2 ⊗2. The Gauss matrix can lead us to the Cholesky
decomposition. The TCMs can be used in order to obtain diﬀerent transforms
of some matrix equations to linear matrix equations of the form AX = B. A
TCM n ⊗n is expressed in terms of the n ⊗n-Gell-Mann matrices. In order
to generalize this expression to which of TCMs n⊗p, we introduced what we
call rectangle Gell-Mann matrices. The electric charge operator (ECO) for
eight leptons and quarks of the Standard Model (SM) of a same generation
proposed by Zenczykowski is expressed in terms of the TCM 2 ⊗2. An ECO
including all the fermions of the SM is constructed in terms of TCM 4 ⊗4.
Then the eigenvalues of a TCM take sense.
Keywords : Dirac equation, Dirac-Sidharth equation, Kronecker product,
Swap operator, System of linear equations, Cholesky, Generalized Gell-Mann
matrices, leptons, Quarks.
Résumé
Nous avons construit deux ensembles de représentations de l’équation de Di-
rac. Ils se transforment l’un en l’autre en multipliant par la matrice de com-
mutation tensorielle (MCT) 2⊗2. La méthode de Gauss matricielle peut nous
conduire à la d*écomposition de Cholesky. Les MCT peuvent être utilisées
aﬁn dŠobtenir diﬀérentes transformées de certaines équations matricielles en
équations matricielles linéaires de la forme AX = B. Une MCT n ⊗n a
été exprimée en termes de matrices de Gell-Mann n ⊗n. Aﬁn de génŕaliser
cette expression à celles des MCT n ⊗p, nous avons introduit ce que nous
appelons matrices de Gell-Mann rectangles. L’opérateur charges électriques
(OCE), pour huit leptons et quarks du modèle standard (MS) d’une même
génération proposé par Zenczykowski a été exprimé en termes de MCT 2⊗2.
Un OCE incluant tous les fermions du MS a été construit en termes de MCT
4 ⊗4. Alors, les valeurs propres d’une MCT ont pris sens.
Mots clés : Equation de Dirac, Equation de Dirac-Sidharth, produit de
Kronecker, Système d’´quations linéaires, Cholesky, Matrices de Gell-Mann
généralisées, leptons, quarks.


## Page 5


Avant-propos
Ce document présente un ensemble de travaux de recherches que nous
avons mené depuis l’obtention de notre doctorat en 2003. Nous avons ras-
semblons dans ce mémoire nos publications pour obtenir certaine cohérence.
Nous avons délibérément choisi de ne pas y inclure notre travail sur les équa-
tions diﬀérentielles. En eﬀet, l’inclusion de ce travail rendrait diﬃcile, pour
ne pas dire impossible, la cohérence. Ces activités se sont déroulées à l’Ins-
titut Supérieur de Téchnologie d’Antananarivo, IST-T, où nous enseignons
en tant que maître de conférences et à l’université d’Antananarivo, Départe-
ment de Physique, Laboratoire de Rhéologies des Suspensions, LRS, où nous
avons travaillé pour ﬁnir ce mémoire et avons encadré un étudiant en DEA.
Nous avons aussi travaillé avec Madagascar-Institut National des Sciences et
Techniques Nucléaires, Madagascar-INSTN, où nous avions travaillé de 1999
à 2003 pour preparer notre thèse de doctorat et avons encadré un étudiant
en DEA.
Ce travail est la suite logique de notre formation en mathématiques et notre
thèse de physique théorique. Il est incontestable que les mathématiques sont
des outils que tous les pays peuvent utiliser pour contribuer au dévelop-
pement des sciences. Réciproquement, les sciences, de par leurs développe-
ments, enrichissent les mathématiques. Comme son titre l’indique, ce travail
est un exemple qui met en évidence cette dialectique entre sciences, phy-
sique et mathématiques. En eﬀet, notre étude mathématiques de l’équation
de Dirac-Sidharth, qui est une équation relativiste des particules de spin- 1
2
nous conduit aux matrices que nous appelons matrices de commutation ten-
sorielle. Ces matrices sont très utiles en mathématiques, dans les résolutions
des équations matricielles. Elles se généralisent à ce que nous appelons ma-
trices de permutation tensorielles qui, à leur tour, ont une application en
mécanique quantique.
Nous avons exprimé ces matrices en termes de matrices de Gell-Mann généra-
lisées, qui sont des matrices de la physique des particules, en espérant trouver
application de ces matrices dans ce domaine de la physique. Nous pensons
que nous nous dirigeons vers l’application de ces matrices en physique des
iii


## Page 6


iv
particules lorsque, lors de la recherche que nous avons eﬀectué dans le La-
boratoire de Rhéologies des Suspensions, LRS, Université d’Antananarivo,
nous avons exprimé l’opérateur charges éléctrique des particules fermions du
Modèle Standard proposé par Zenczykowski en termes de matrice de com-
mutation tensorielle. Ainsi, ce travail s’inscrit dans le cadre de l’application
de l’algèbre linéaire et multilinéaire en physique.
L’insertion de la subsection sur la méthode de Cholesky dans ce mémoire
semble perturber un peu la cohérence. Mais comme cette subsection fait par-
tie de l’algèbre linéaire et qu’elle ﬁgure parmi les fruits de notre recherche
pédagogique eﬀectuée à l’Institut Supérieur de Technologie d’Antananarivo,
IST-T, nous nous excusons auprès des lecteurs cette incohérence apparente.
Nous disons "apparente" parce que pour un lecteur averti ce ne sera plus
du tout une incohérence, puisque cette subsection est un pont menant vers
l’application des matrices de commutation tensorielle aux études des équa-
tions matricielles. Cette subsection, constitue une partie d’un chapitre de
notre cours d’Analyse Numérique à l’Institut Supérieur de Technologie d’An-
tananarivo, IST-T, est donnée en anglais aux étudiants, mais expliquée en
Malagasy.


## Page 7


Table des matières
1
MCT A PARTIR DE L’EQUATION DE DIRAC-SIDHARTH
3
1.1
EQUATION DE DIRAC-SIDHARTH ET PRODUIT TEN-
SORIEL DE MATRICES
. . . . . . . . . . . . . . . . . . . .
3
1.1.1
Une derivation de l’équation de Dirac-Sidharth . . . . .
4
1.1.2
Résolution de l’équation de Dirac-Sidharth . . . . . . .
6
1.1.3
Representation de l’équation de Dirac-Sidharth
. . . .
7
2
MATRICES DE PERMUTATION TENSORIELLE
11
2.1
MATRICES DE COMMUTATION TENSORIELLE . . . . . .
11
2.1.1
Matrices de commutation tensorielle
. . . . . . . . . .
11
2.1.2
Expression d’un élément d’une matrice de commuta-
tion tensorielle
. . . . . . . . . . . . . . . . . . . . . .
13
2.2
MATRICES DE PERMUTATION TENSORIELLE . . . . . .
15
2.2.1
Opérateurs de permutation tensorielle . . . . . . . . . .
15
2.2.2
Expression d’un élément d’une matrice de permutation
tensorielle . . . . . . . . . . . . . . . . . . . . . . . . .
18
2.2.3
Décomposition d’une matrice de permutation tensorielle 18
2.3
MATRICES DE COMMUTATION TENSORIELLE ET EQUA-
TIONS MATRICIELLES
. . . . . . . . . . . . . . . . . . . .
21
2.3.1
Sur la méthode de Cholesky . . . . . . . . . . . . . . .
21
2.3.2
Matrices de commutation tensorielle et transformées
d’une équation matricielle
. . . . . . . . . . . . . . . .
28
3
VERS UNE APPLICATION EN PHYSIQUE DES PARTI-
CULES
29
3.1
MATRICES DE PERMUTATION TENSORIELLE ET MA-
TRICES DE GELL-MANN
. . . . . . . . . . . . . . . . . . .
29
3.1.1
MCT en termes de matrices de Gell-Mann généralisées
29
3.1.2
Matrices de Gell-Mann rectangles . . . . . . . . . . . .
36
3.1.3
Exprimer une matrice de permutation tensorielle p⊗n
en termes de matrices de Gell-Mann généralisées . . . .
39
v


## Page 8


vi
TABLE DES MATIÈRES
3.2
MCT ET CHARGES ELECTRIQUES DES FERMIONS . . .
42
3.2.1
Relation de Gell-Mann-Nishijima dans la formulation
dans l’espace des phases . . . . . . . . . . . . . . . . .
43
3.2.2
Opérateur charges électriques en termes de la MCT 2⊗2 44
3.2.3
Opérateur charges électriques en termes de MCT 3 ⊗3
46
3.2.4
Inclure tous les fermions du modèle standard . . . . . .
47
A Matrices. Une généralisation
53
B Produit Tensoriel de matrices
55


## Page 9


INTRODUCTION
Le produit tensoriel de matrices ou produit de kronecker ou encore produit
direct de matrices n’est pas commutatif en général. Cependant, le produit de
certaines matrices avec un produit tensoriel de matrices commute ce produit.
Ces matrices sont les matrices de commutation tensorielle (MCT) ou matrices
de commutation de kronecker (Cf. par exemple [1, 2, 3, 4]). Les MCT ont
des applications en mécanique quantique, en particulier en théorie quantique
de l’information (Cf. par exemple [2, 3, 4, 5, 6]). Nous avons découvert les
MCT quand nous travallions sur l’équation de Dirac [7, 8], qui est l’équation
quantique relativiste des particules de spin 1
2 telles qu’un électron. Cepen-
dant, dans ce mémoire c’est l’équation de Dirac-Sidharth qui nous conduit à
ces matrices. C’est une équation de Dirac modiﬁée. Les représentations qui
sont communes à ces équations sont ce qui nous y conduisent.
Nous pensons que ces matrices méritent plus d’attention puisqu’elles ont aussi
des applications en mathématiques, plus précisement pour les résolutions des
équations matricielles (Cf. par exemple [1, 10, 9]). Lorsque nous étudiions
[11], l’expression de la MCT 2 ⊗2 en termes de matrices de Pauli,
U2⊗2 = 1
2I2 ⊗I2 + 1
2
3
X
i=1
σi ⊗σi
(1)
nous a fait remarqué que ce MCT pourrait avoir applications en physique
des particules.
Les MCT se généralisent aux matrices de permutation tensorielle (MPT), qui
permutent le produit tensoriel de matrices. Les MPT ont aussi des applica-
tions en mécanique quantique.
Ce mémoire est divisé en trois chapitres de la manière suivante. Dans le
chapitre I, nous étudierons une équation de Dirac modiﬁée, l’équation de
Dirac-Sidharth. C’est là que la MCT 2 ⊗2
U2⊗2 =




1
0
0
0
0
0
1
0
0
1
0
0
0
0
0
1




1


## Page 10


2
TABLE DES MATIÈRES
nous apparaîtra comme quand nous étudiions l’équation de Dirac. Le chapitre
II est l’études et applications mathématiques des MCT et leur généralisation
aux MPT. Dans le chapitre III, nous généraliserons l’expression (1) à celle de
la MCT n⊗n en termes de matrices de Gell-Mann n×n, qui sont des matrices
de la physique des particules. Pour généraliser à son tour cette relation à celle
de MCT n ⊗p, nous introduirons ceux que nous appelons matrices de Gell-
Mann rectangles. Nous verrons aussi dans ce chapitre comment exprimer une
MPT en termes de matrices de Gell-Mann généralisées. A la ﬁn de ce chapitre,
nous exprimerons l’opérateur charges électriques (OCE) de fermions proposé
par Zenczykowski
Q = 1
2σ0 ⊗σ0 ⊗σ3 + 1
6
 
3
X
i=1
σi ⊗σi
!
⊗σ0
en termes de la MCT 2 ⊗2. Puis nous introduirons les MCT 3 ⊗3 et 4 ⊗4
pour obtenir des opérateurs charges électriques pour plus de fermions.


## Page 11


Chapitre 1
MCT A PARTIR DE
L’EQUATION DE
DIRAC-SIDHARTH
Ce chapitre est basé sur Ref. [12]
1.1
EQUATION DE DIRAC-SIDHARTH ET
PRODUIT TENSORIEL DE MATRICES
Nous allons construire l’équation de Dirac-Sidharth, à partir de l’hamil-
tonien de Sidharth, par quantiﬁcation de l’énergie et de l’impulsion dans
l’algèbre de Pauli. Nous allons résoudre cette équation en utilisant le produit
tensoriel de matrices.
Selon la relativité restreinte d’Einstein [13], la relation entre l’énergie et
l’impulsion est
E2 = c2p2 + m2c4
à partir de laquelle nous pouvons déduire l’équation de Klein-Gordon et
l’équation de Dirac. Cette théorie utilise le concept de l’espace-temps continu.
L’espace-temps quantiﬁé a été introduit pour la première fois par Snyder
[14, 15], sous le nom de géométrie non commutative de Snyder, à cause de
la modiﬁcation sur les relations de commutation. Dans cette théorie les rela-
tions de commutation sont [14, 15]
[xµ, xν] = iαℓ2c2
ℏ
(xµpν −xνpµ) ,
[xµ, pν] = iℏ

δµ
ν + iαℓ2c2
ℏ2 pµpν

,
3


## Page 12


4CHAPITRE 1. MCT A PARTIR DE L’EQUATION DE DIRAC-SIDHARTH
[pµ, pν] = 0
où ℓest une échelle de longueur quelconque en physique. Par exemple, ℓ=
ℓp =
q
ℏG
c3 ≈1.6×10−33cm la longueur de Planck , la longueur minimale pos-
sible de mesurer en physique, où G est la constante gravitationnelle. Comme
consequence, la relation entre énergie et implulsion est modiﬁée et devient
(en unité SUN, c = ℏ= 1)[16]
E2 = p2 + m2 + αl2p4
ou (en unité SI)[17, 18]
E2 = c2p2 + m2c4 + α
 c
ℏ
2
ℓ2p4
(1.1)
où α une constante adimensionnelle.
ǫ =
ℏc
√αℓ
(1.2)
est l’énergie de Planck dûe à l’échelle de longueur de Planck ℓ= ℓp [17, 18].
Alors, [18]
E2 = c2p2 + m2c4 + c4p4
ǫ2
Le rôle fondamental de ǫ est expliqué dans [17, 18, 19].
En fait, en appliquant l’hamiltonien de Snyder-Sidharth (1.1) Sidharth a
construit l’équation de Dirac-Sidharth [16, 20], i.e. l’équation de Dirac mo-
diﬁée dûe à la géométrie non commutative de l’espace de phase.
Dans la sous-section 1.1.1, nous construirons l’équation de Dirac-Sidharth,
à partir de la relation (1.1), par quantiﬁcation de l’énergie et l’impulsion.
Dans la sous-section 1.1.2, nous résoudrons l’équation de Dirac-Sidharth par
utilisation du produit tensoriel de matrices.
1.1.1
Une derivation de l’équation de Dirac-Sidharth
Pour établir l’équation de Dirac-Sidharth nous allons utiliser la méthode
de J.J. Sakurai [21] pour la dérivation de l’équation de Dirac.
La fonction d’onde d’une particule de spin- 1
2 doit être à deux composantes.
Ainsi, pour quantiﬁer la relation énergy-impulsion relativiste aﬁn d’obtenir
l’équation modiﬁée de Klein-Gordon [16, 20], ou équation de Klein-Gordon-
Sidharth, d’une particule de spin- 1
2, les operateurs qui prennent part dans la


## Page 13


1.1. EQUATION DE DIRAC-SIDHARTH ET PRODUIT TENSORIEL DE MATRICES 5
quantiﬁcation doivent être des matrices 2 × 2 . Ainsi, prenons comme règles
de quantiﬁcation
E −→iℏσ0 ∂
∂t = iℏ∂
∂t
⃗p −→−iℏσ1 ∂
∂x1 −iℏσ2 ∂
∂x2 −iℏσ3 ∂
∂x3 = −iℏ⃗σ⃗∇= ˆp1σ1 + ˆp2σ2 + ˆp3σ3
où
σ1 =
 0
1
1
0

, σ2 =
 0
−i
i
0

, σ3 =
 1
0
0
−1

sont les matrices de Pauli. Alors, nous avons d’abord l’équation de Klein-
Gordon-Sidharth
c2ℏ2
 ∂2
c2∂t2 −∆−m2c2 −α ℓ2
ℏ2 ⃗∇4

φ = 0

iℏ∂
∂t + icℏ⃗σ⃗∇

1
mc2
(+∞
X
k=0
(−1)k
i√α
mcℏℓ

−iℏ⃗σ⃗∇
2k)
×

iℏ∂
∂t −icℏ⃗σ⃗∇

φ =

mc2 + i√α c
ℏℓ

−iℏ⃗σ⃗∇
2
φ
dont l’operateur agit sur la fonction d’onde à deux composantes φ, qui est
solution de l’équation de Klein-Gordon-Sidharth. Soit
χ =
1
mc2
(+∞
X
k=0
(−1)k
i√α
mcℏℓ

−iℏ⃗σ⃗∇
2k) 
iℏ∂
∂t −icℏ⃗σ⃗∇

φ
alors, nous avons le système d’équations aux dérivées partielles suivantes





iℏ∂
c∂tχ + iℏ⃗σ⃗∇χ = mcφ + i√α ℓ
ℏ

iℏ⃗σ⃗∇
2
φ
iℏ∂
c∂tφ −iℏ⃗σ⃗∇φ = mcχ −i√α ℓ
ℏ

iℏ⃗σ⃗∇
2
χ
En additionnant et en soustrayant ces équations, et en transformant les
équations obtenues sous forme matricielle, nous avons l’équation de Dirac-
Sidharth
iℏγµ
D∂µψD −mcψD −i√αℓℏγ5
D∆ψD = 0
dans la representation de Dirac (ou "Standard") des γ-matrices, où
γ0
D =

σ0
0
0
−σ0

= σ3 ⊗σ0, γj
D =

0
σj
−σj
0

= iσ2 ⊗σj, j = 1, 2, 3,
γ5
D = iγ0
Dγ1
Dγ2
Dγ3
D =

0
σ0
σ0
0

= σ1 ⊗σ0, et ψD =

χ + φ
χ −φ

,


## Page 14


6CHAPITRE 1. MCT A PARTIR DE L’EQUATION DE DIRAC-SIDHARTH
∆=
∂2
∂x2
1 + ∂2
∂x2
2 + ∂2
∂x2
3.
Les matrices 4 × 4 (γµ
D)0≤µ≤3 satisfont les relations suivantes
γµ
Dγν
D + γν
Dγµ
D = 2gµνI4, µ, ν ∈{0, 1, 2, 3}
(1.3)
où gµν = 0 if µ ̸= ν,
gjj = −1, j ∈{1, 2, 3},
g00 = 1
Nous savons que [22]
Pγ5 = −γ5P
Il s’ensuit que l’équation de Dirac-Sidharth est non invariant sous l’opérateur
parité (ou réﬂexion dans l’espace) [23].
L’équation
iℏγµ
W∂µψW −mcψW −i√αℓℏγ5
W∆ψW = 0
est l’équation de Dirac-Sidharth dans la representation de Weyl (ou chiral),
où ψW =
χ
φ

.
Ainsi, χ et φ sont les composantes (ou chiralité) respectivement gauche et
droite.
1.1.2
Résolution de l’équation de Dirac-Sidharth
Dans cette section, nous cherchons les solutions de l’équation de Dirac-
Sidharth, en forme d’onde plane en utilisant le produit tensoriel de matrices.
Nous avions utilisé cette méthode pour résoudre l’équation de Dirac [8].
Ainsi, cherchons une solution sous la forme
ψD = U(p)e
i
ℏ(⃗p⃗x−Et)
Soit Ψ un spineur à quatre composantes qui est un état propre de ˆpj = −iℏ∂
∂xj
et de ˆE = iℏ∂
∂t, ⃗p =


p1
p2
p3

, et ⃗n = ⃗p
p =


n1
n2
n3

.
L’équation de Dirac-Sidharth devient
σ0 ⊗σ0U(p) −2
ℏcpσ1 ⊗
ℏ
2⃗σ⃗n

U(p) −mc2σ3 ⊗σ0U(p)
+ c√αp2 ℓ
ℏσ2 ⊗σ0U(p) = 0
Prenons U(p) sous la forme
U(p) = ϕ ⊗u


## Page 15


1.1. EQUATION DE DIRAC-SIDHARTH ET PRODUIT TENSORIEL DE MATRICES 7
où u est un vecteur propre de l’opérateur spin ℏ
2⃗σ⃗n. ϕ =

ϕ1
ϕ2

et u sont à
deux componsantes.
Comme u ̸= 0, donc

ηcpσ1 + mc2σ3 −c√αp2 ℓ
ℏσ2

ϕ = Eϕ
(1.4)
avec η =
(
+1
spin haut
−1
spin bas
En résolvant cette équation par rapport à ϕ1 et ϕ2, nous avons
Ψ+ =
r
E + mc2
2E
 
1
ηcp−i c
ℏ
√αp2ℓ
mc2+E
!
⊗se
i
ℏ(⃗p⃗x−Et)
la solution à énergie positive, où s =
1
√
2(1+n3)
−n1 + in2
1 + n3

spin haut, s =
1
√
2(1+n3)
 1 + n3
n1 + in2

spin bas.
D’après l’équation (1.4), cette méthode fait apparaître la matrice h =
ηcpσ1 −c√αp2 ℓ
ℏσ2 + mc2σ3, ou h = ηcpσ1 −c2p2
ǫ σ2 + mc2σ3 (si ℓest l’échelle
de longueur de Planck), dont les valeurs propres sont les énergies positive
et negative. h est comme un vecteur dans l’algèbre de Pauli. Ainsi, l’éner-
gie d’une particule de spin- 1
2 peut être considérée comme un vecteur dans
l’algèbre de Pauli, dont la longueur ou l’intensité est donnée par la relation
énergie-impulsion relativiste.
h2 = E2
1.1.3
Representation de l’équation de Dirac-Sidharth
Déﬁnition 1 Un système de matrices 4×4 (γµ)0≤µ≤3 satisfaisant la relation
(1.3), c’est-à-dire γµγν + γνγµ = 2gµνI4, est appelé une représentation de
l’équation de Dirac-Sidharth. Si de plus, (γµ)0≤µ≤3 est un système de matrices
unitaires , on dit qu’il est une représentation unitaire de l’équation de Dirac-
Sidharth.
Les théorèmes suivants concernent les relations entre diﬀérentes représenta-
tions [24].
Théorème 2 Théorème Fondamental de Pauli.
Pour deux représentations de l’équation de Dirac-Sidharth (γµ)0≤µ≤3,
 γ
′µ
0≤µ≤3,


## Page 16


8CHAPITRE 1. MCT A PARTIR DE L’EQUATION DE DIRAC-SIDHARTH
il existe une matrice S, déﬁnie à une constante multiplicative près et non sin-
gulier (det(S) ̸= 0), telle que
γµ = Sγ
′µS−1, µ = 0, 1, 2, 3.
Corollaire 3 Pour deux représentations unitaires de l’équation de Dirac-
Sidharth (γµ)0≤µ≤3,
 γ
′µ
0≤µ≤3, il existe une matrice unitaire U, déﬁnie à
une phase près
γµ = Uγ
′µU−1, µ = 0, 1, 2, 3.
Dans la section 1.1.1 nous avons vu comment les matrices gamma dans
la representation de Dirac peuvent être exprimées à l’aide des matrices de
Pauli. De manière analogue nous pouvons obtenir, en construisant l’équation
de Dirac-Sidharth six representations unitaires de cette equation, à savoir
(σ3 ⊗σ0, iσ2 ⊗σ1, iσ2 ⊗σ2, iσ2 ⊗σ3) Représentation de Dirac
(σ3 ⊗σ0, iσ1 ⊗σ1, iσ1 ⊗σ2, iσ1 ⊗σ3)
(σ2 ⊗σ0, iσ1 ⊗σ1, iσ1 ⊗σ2, iσ1 ⊗σ3)
(σ2 ⊗σ0, iσ3 ⊗σ1, iσ3 ⊗σ2, iσ3 ⊗σ3)
(σ1 ⊗σ0, iσ2 ⊗σ1, iσ2 ⊗σ2, iσ2 ⊗σ3) Représentation de Weyl
(σ1 ⊗σ0, iσ3 ⊗σ1, iσ3 ⊗σ2, iσ3 ⊗σ3)
et six autres représentations unitaires de l’équation de Dirac-Sidharth obte-
nues en commutant les produits tensoriels de matrices ci-dessus
(σ0 ⊗σ3, iσ1 ⊗σ2, iσ2 ⊗σ2, iσ3 ⊗σ2)
(σ0 ⊗σ3, iσ1 ⊗σ1, iσ2 ⊗σ1, iσ3 ⊗σ1)
(σ0 ⊗σ2, iσ1 ⊗σ1, iσ2 ⊗σ1, iσ3 ⊗σ1)
(σ0 ⊗σ2, iσ1 ⊗σ3, iσ2 ⊗σ3, iσ3 ⊗σ3)
(σ0 ⊗σ1, iσ1 ⊗σ2, iσ2 ⊗σ2, iσ3 ⊗σ2)
(σ0 ⊗σ1, iσ1 ⊗σ3, iσ2 ⊗σ3, iσ3 ⊗σ3)
.


## Page 17


1.1. EQUATION DE DIRAC-SIDHARTH ET PRODUIT TENSORIEL DE MATRICES 9
La matrice unitaire du corollaire qui transforme la première famille de six
représentations unitaires de l’équation de Dirac-Sidharth à la seconde famille
est la matrice unitaire
U2⊗2 =




1
0
0
0
0
0
1
0
0
1
0
0
0
0
0
1




puisqu’elle commute le produit tensoriel de deux matrices 2×2 quelconques,
A, B ∈C2×2 de la manière suivante
U2⊗2 · (A ⊗B) · U2⊗2 = B ⊗A
Nous l’appelons MCT 2 ⊗2. Elle commute aussi le produit tensoriel de deux
matrices complexes unicolonnes de la manière suivante. Pour a =

a1
a2

,
b =

b1
b2

∈C2×1 quelconques
U2⊗2. (a ⊗b) = b ⊗a
La MCT 2 ⊗2 est fréquemment trouvée en théorie quantique de l’infor-
mation [4], [25], [26], où on écrit à l’aide des matrices de Pauli [4],[25]
U2⊗2 = 1
2I2 ⊗I2 + 1
2
3
X
i=1
σi ⊗σi
(1.5)
La MCT 3 ⊗3 a été écrite par KAZUYUKI FUJII [4] de la manière suivante
U3⊗3 =
















1
0
0
0
0
0
0
0
0




0
0
0
1
0
0
0
0
0




0
0
0
0
0
0
1
0
0




0
1
0
0
0
0
0
0
0




0
0
0
0
1
0
0
0
0




0
0
0
0
0
0
0
1
0




0
0
1
0
0
0
0
0
0




0
0
0
0
0
1
0
0
0




0
0
0
0
0
0
0
0
1
















(1.6)
aﬁn d’obtenir une conjecture pour la forme de la MCT n ⊗n, pour tout
n ∈N⋆.
Dśignons par Un⊗p la MCT n ⊗p, n, p ∈N.


## Page 18


10CHAPITRE 1. MCT A PARTIR DE L’EQUATION DE DIRAC-SIDHARTH


## Page 19


Chapitre 2
MATRICES DE
PERMUTATION
TENSORIELLE
Ce chapitre est basé sur Refs. [27, 28, 29, 30]
2.1
MATRICES DE COMMUTATION TEN-
SORIELLE
2.1.1
Matrices de commutation tensorielle
Déﬁnition 4 Pour p, q ∈N, p ≥2, q ≥2, nous appelons MCT p ⊗q la
matrice de permutation Up⊗q ∈Cpq×pq, vériﬁant la propriété suivante
Up⊗q.(a ⊗b) = b ⊗a
(2.1)
pour tous a ∈Cp×1, b ∈Cq×1.
En considerant Up⊗q comme une matrice d’un tenseur d’ordre deux (Cf.
Annexe A), nous pouvons la construire en utilisant la règle suivante.
Règle 5 Commençons par mettre 1 sur la première ligne et première co-
lonne, puis passons à la deuxième colonne en descendant p lignes suivant
cette colonne plaçons 1 à cette place qui est la p + 1-ième ligne et deuxième
colonne. Puis passons à la troisième colonne en descendant p lignes suivant
cette colonne plaçons 1 à cette place qui est la 2p + 2-ième ligne et troisième
colonne, et ainsi de suite jusqu’à nous n’avons que p −1 lignes pour des-
cendre (alors nous avons comme nombre de 1 : q). Puis passons à la colonne
11


## Page 20


12
CHAPITRE 2. MATRICES DE PERMUTATION TENSORIELLE
suivante qui est la (q + 1)-ième colonne, mettre 1 sur la deuxième ligne de
cette colonne (puisque (p −1) + 1 = p) et répétons le processus jusqu’à nous
n’avons que p −2 lignes pour descendre (alors nous avons comme nombre de
1 : 2q). Après, passons à la colonne suivante qui est la (2q+1) -ième colonne,
mettre 1 sur la troisième ligne de cette colonne (puisque (p −2) + 2 = p) et
répétons le processus jusqu’à nous n’avons que p −3 lignes pour descendre
(alors nous avons comme nombre de 1 : 3q). En Continuant de cette manière
nous aurons que l’élément sur p × q-ième ligne et p × q-ième colonne est 1.
Les autres éléments sont 0.
Proposition 6 Pour n, p ∈N, n, p ⩾2,
Un⊗p =
(p,n)
X
(i,j)
E(i,j)
p×n ⊗E(i,j)t
p×n =
(p,n)
X
(i,j)
E(i,j)
p×n ⊗E(j,i)
n×p
où E(i,j)
p×n est la matrice p × n élémentaire formée par des zeros sauf l’élément
sur la i-ième ligne et j-ième colonne qui est égal à 1.
Preuve. Soient a =





a1
a2
...
an




∈Cn×1, b =





b1
b2
...
bp




∈Cp×1
Un⊗p · (a ⊗b) =
(p,n)
X
(i,j)
E(i,j)
p×n ⊗E(j,i)
n×p · (a ⊗b) =
(p,n)
X
(i,j)
(E(i,j)
p×n · a) ⊗(E(j,i)
n×p · b)
=
(p,n)
X
(i,j)
(δikaj)1⩽k⩽p ⊗(δjlbi)1⩽l⩽n =
(p,n)
X
(i,j)
(δikbi)1⩽k⩽p ⊗(δjlaj)1⩽l⩽n
=
(p,n)
X
(i,j)











0
...
0
bi
0
...
0











⊗











0
...
0
aj
0
...
0











= b ⊗a
où δij est le symbole de kronecker.


## Page 21


2.1. MATRICES DE COMMUTATION TENSORIELLE
13
Exemple 7 L’application de la règle 5 nous donne
U2⊗3 =








1
0
0
0
0
0
0
0
0
1
0
0
0
1
0
0
0
0
0
0
0
0
1
0
0
0
1
0
0
0
0
0
0
0
0
1








U2⊗3 =


1
0
0
0
0
0

⊗
1
0
0
0
0
0

+


0
1
0
0
0
0

⊗
0
0
0
1
0
0

+


0
0
1
0
0
0

⊗
0
1
0
0
0
0

+


0
0
0
1
0
0

⊗

0
0
0
0
1
0

+


0
0
0
0
1
0

⊗

0
0
1
0
0
0

+


0
0
0
0
0
1

⊗

0
0
0
0
0
1

Remarque 8 Considérons la fonction L de l’ensemble de toutes les matrices
de dimension ﬁnies vers l’ensemble des matrices unicolonnes . Pour une ma-
trice X =




x11
x12
. . .
x1p
x21
x22
. . .
x2p
. . .
. . .
. . .
. . .
xn1
xn2
. . .
xnp



,
L (X) =

























x11
x12
...
x1p
x21
x22
...
x2p
...
xn1
xn2
...
xnp

























. On peut obtenir facilement que Un⊗p · L (X) = L
 XT
.
2.1.2
Expression d’un élément d’une matrice de com-
mutation tensorielle
Ici n et p sont des éléments quelconques de N⋆, n, p ≥2. Ainsi, il s’agit
d’une généralisation de l’ expression d’un élément d’une MCT n ⊗n pour


## Page 22


14
CHAPITRE 2. MATRICES DE PERMUTATION TENSORIELLE
un n
∈
N⋆[4]. D’abord, étudions l’exemple ci-dessous pour conjecturer
l’expression pour le cas plus général. Ainsi, nous suivons la méthode de [4].
Ecrivons alors U3⊗5 de la façon suivante :
U3⊗5 =




























1
0
0
0
0
0
0
0
0
0
0
0
0
0
0




0
0
0
0
0
1
0
0
0
0
0
0
0
0
0




0
0
0
0
0
0
0
0
0
0
1
0
0
0
0




0
1
0
0
0
0
0
0
0
0
0
0
0
0
0




0
0
0
0
0
0
1
0
0
0
0
0
0
0
0




0
0
0
0
0
0
0
0
0
0
0
1
0
0
0




0
0
1
0
0
0
0
0
0
0
0
0
0
0
0




0
0
0
0
0
0
0
1
0
0
0
0
0
0
0




0
0
0
0
0
0
0
0
0
0
0
0
1
0
0




0
0
0
1
0
0
0
0
0
0
0
0
0
0
0




0
0
0
0
0
0
0
0
1
0
0
0
0
0
0




0
0
0
0
0
0
0
0
0
0
0
0
0
1
0




0
0
0
0
1
0
0
0
0
0
0
0
0
0
0




0
0
0
0
0
0
0
0
0
1
0
0
0
0
0




0
0
0
0
0
0
0
0
0
0
0
0
0
0
1




























Considérons les matrices rectangles In×p =
 δi
j

1≤i≤n,1≤j≤p, Ip×n =
 δi
j

1≤i≤p,1≤j≤n,
où δi
j est le symbole de Kronecker. La matrice np × np
Ip×n ⊗In×p =
 δi1i2
j1j2

=
 δi1
j1δi2
j2

où,
i1i2 = 11, 12, . . . , 1n, 21, 22, . . ., 2n, . . . , p1, p2, . . . , pn
indices de lignes,
j1j2 = 11, 12, . . ., 1p, 21, 22, . . ., 2p, . . . , n1, n2, . . . , np
indices de colonnes,
nous suggère la proposition suivante.
Proposition 9
Un⊗p =
 Ui1i2
j1j2

=
 δi1i2
j2j1

=
 δi1
j2δi2
j1

(2.2)
où,
i1i2 = 11, 12, . . . , 1n, 21, 22, . . ., 2n, . . . , p1, p2, . . . , pn
indices de lignes,
j1j2 = 11, 12, . . ., 1p, 21, 22, . . ., 2p, . . . , n1, n2, . . . , np
indices de colonnes,


## Page 23


2.2. MATRICES DE PERMUTATION TENSORIELLE
15
Preuve. Soient a = (aj1)1≤j1≤n ∈Cn×1, b = (bj2)1≤j2≤p ∈Cp×1
(a ⊗b)i1i2 −→(Un⊗p · (a ⊗b))i1i2 = δi1
j2δi2
j1aj1bj2 = δi1
j2bj2δi2
j1aj1 = bi1ai2
= (b ⊗a)i1i2
2.2
MATRICES DE PERMUTATION TENSO-
RIELLE
Dans cette section nous suivons l’idée dans [31], en algèbre linéaire et
multilinéaire, en établissant d’abord les théorèmes pour les opérateurs, de
façon intrinsèque, c’est-à-dire indépendamment des bases, puis les théorèmes
correspondant pour les matrices. Ainsi, nous allons d’abord parler d’opéra-
teurs de permutation tensorielle (OPT). Nous utiliserons aussi ses notations
pour les vecteurs et covecteurs, en surlignant les vecteurs, x, et en soulignant
les covecteurs, ϕ.
2.2.1
Opérateurs de permutation tensorielle
Déﬁnition 10 Considérons les C-espaces vectoriels de dimensions ﬁnies E1, E2, . . . , Ek
et une permutation σ sur {1, 2, . . . , k}. L’opérateur linéaire Uσ de E1 ⊗E2 ⊗
. . . ⊗Ek à Eσ(1) ⊗Eσ(2) ⊗. . . ⊗Eσ(k), Uσ ∈L(E1 ⊗E2 ⊗. . . ⊗Ek, Eσ(1) ⊗Eσ(2) ⊗
. . . ⊗Eσ(k)), déﬁni par
Uσ(x1 ⊗. . . ⊗xk) = xσ(1) ⊗. . . ⊗xσ(k)
pour tous x1 ∈E1, x2 ∈E2, . . . , xk ∈Ek est appelé un σ-OPT.
Si n = 2, alors nous disons que Uσ est un opérateur de commutation tenso-
rielle.
Proposition 11 Si Uσ est un σ-OPT, alors son transposé UT
σ est un σ−1-
OPT, Uσ−1 = U−1
σ .
Preuve. Considérons les C-espaces vectoriels E1, E2, . . . , Ek de dimen-
sions ﬁnies et E1
⋆, E2
⋆, . . . , Ek
⋆sont leurs espaces duaux. Uσ ∈L(E1
⊗
E2
⊗
. . .
⊗Ek, Eσ(1)
⊗
Eσ(2)
⊗
. . .
⊗
Eσ(k)) σ-OPT. Alors Uσ
T
∈
L(Eσ(1)
⋆⊗Eσ(2)
⋆⊗. . . ⊗Eσ(k)
⋆, E1
⋆⊗E2
⋆⊗. . . ⊗Ek
⋆).
Soient ϕσ(1) ∈Eσ(1)
⋆, ϕσ(2) ∈Eσ(2)
⋆, . . . ϕσ(k) ∈Eσ(k)
⋆, x1 ∈E1, x2 ∈E2, . . . ,


## Page 24


16
CHAPITRE 2. MATRICES DE PERMUTATION TENSORIELLE
xk ∈Ek.
Uσ
T ·
 ϕσ(1) ⊗ϕσ(2) ⊗. . . ⊗ϕσ(k)
(x1 ⊗x2 ⊗. . . ⊗xk)
= ϕσ(1) ⊗ϕσ(2) ⊗. . . ⊗ϕσ(k) [Uσ(x1 ⊗x2 ⊗. . . ⊗xk)]
(par déﬁnition de l’opérateur transposé [31])
= ϕσ(1) ⊗ϕσ(2) ⊗. . . ⊗ϕσ(k)(xσ(1) ⊗xσ(2) ⊗. . . ⊗xσ(k))
= ϕσ(1)(xσ(1))⊗ϕσ(2)(xσ(2))⊗. . .⊗ϕσ(k)(xσ(k)) = ϕσ(1)(xσ(1))ϕσ(2)(xσ(2)) . . . ϕσ(k)(xσ(k))
(puisque les ϕσ(i)(xσ(i)) sont des éléments de C)
= ϕ1(x1) ⊗ϕ2(x2) ⊗. . . ⊗ϕk(xk)
= (ϕ1 ⊗ϕ2 ⊗. . . ⊗ϕk)(x1 ⊗x2 ⊗. . . ⊗xk)
Nous avons
Uσ
T  ϕσ(1) ⊗ϕσ(2) ⊗. . . ⊗ϕσ(k)
(x1 ⊗x2 ⊗. . . ⊗xk)
= (ϕ1 ⊗ϕ2 ⊗. . . ⊗ϕk)(x1 ⊗x2 ⊗. . . ⊗xk)
pour tous x1 ∈E1, x2 ∈E2, . . . , xk ∈Ek.
D’où,
Uσ
T ·
 ϕσ(1) ⊗ϕσ(2) ⊗. . . ⊗ϕσ(k)
= ϕ1 ⊗ϕ2 ⊗. . . ⊗ϕk
Proposition 12 Considérons les C-espaces vectoriels de dimensions ﬁnies
E1, E2, . . . , Ek, F1, F2, . . . , Fk, une permutation σ sur {1, 2, . . . , k} et un
σ-OPT Uσ ∈L
 F1 ⊗. . . ⊗Fk, Fσ(1) ⊗. . . ⊗Fσ(k)

. Alors, pour tous φ1 ∈
L (E1, F1), φ2 ∈L (E2, F2), . . . , φk ∈L (Ek, Fk)
Uσ · (φ1 ⊗. . . ⊗φk) =
 φσ(1) ⊗. . . ⊗φσ(k)

· Vσ
où Vσ ∈L(E1 ⊗E2 ⊗. . . ⊗Ek, Eσ(1) ⊗Eσ(2) ⊗. . . ⊗Eσ(k)) est un σ-OPT.
Preuve. φ1 ⊗. . .⊗φk ∈L (E1 ⊗. . . ⊗Ek, F1 ⊗. . . ⊗Fk, ), donc Uσ ·(φ1 ⊗
φ2⊗. . .⊗φk) ∈L
 E1 ⊗. . . ⊗Ek, Fσ(1) ⊗. . . ⊗Fσ(k)

.
 φσ(1) ⊗φσ(2) ⊗. . . ⊗φσ(k)

·
Vσ
∈L
 E1 ⊗. . . ⊗Ek, Fσ(1) ⊗. . . ⊗Fσ(k)

Si x1 ∈E1, x2 ∈E2, . . . , xk ∈Ek, alors Uσ · (φ1 ⊗. . . ⊗φk) (x1 ⊗. . . ⊗xk) =
Uσ [φ1 (x1) ⊗φ2 (x2) ⊗. . . ⊗φk (xk)] = φσ(1)
 xσ(1)

⊗. . . ⊗φσ(k)
 xσ(k)

(puisque Uσ est un OPT)
=
 φσ(1) ⊗. . . ⊗φσ(k)
  xσ(1) ⊗. . . ⊗xσ(k)

=
 φσ(1) ⊗. . . ⊗φσ(k)

·Vσ (x1 ⊗. . . ⊗xk).
Déﬁnition 13 Considérons les C-espaces vectoriels E1, E2, . . . , Ek de di-
mensions n1, n2, . . . , nk et σ-OPT Uσ ∈
L(E1 ⊗E2 ⊗. . . ⊗Ek, Eσ(1) ⊗


## Page 25


2.2. MATRICES DE PERMUTATION TENSORIELLE
17
Eσ(2) ⊗. . . ⊗Eσ(k)). Soit
B1 = (e11, e12, . . . , e1n1) une base de E1 ;
B2 = (e21, e22, . . . , e2n2) une base de E2 ;
. . .
Bk = (ek1, ek2, . . . , eknk) une base de Ek.
Uσ la matrice de Uσ par rapport au couple de bases
 B1 ⊗B2 ⊗. . . ⊗Bk, Bσ(1) ⊗Bσ(2) ⊗. . . ⊗Bσ(k)

. La matrice carrée Uσ de di-
mension n1 × n2 × . . . × nk est indépendante des bases B1, B2,. . . , Bk. Nous
appelons cette matrice la σ-MPT n1 ⊗n2 ⊗. . . ⊗nk.
Proposition 14 Soient Uσ la σ-MPT n1 ⊗n2 ⊗. . . ⊗nk et Vσ la σ-MPT
m1⊗m2⊗. . .⊗mk. Alors, pour toutes matrices A1, A2,. . . , Ak, de dimensions
respectives, m1 × n1, m2 × n2, . . . , mk × nk
Uσ · (A1 ⊗. . . ⊗Ak) · VT
σ = Aσ(1) ⊗. . . ⊗Aσ(k)
(2.3)
Preuve. Soient A1 ∈L (E1, F1), A2 ∈L (E2, F2), . . . , Ak ∈L (Ek, Fk).
Leurs matrices par rapport aux couples de bases
 B1, B
′
1

,
 B2, B
′
2

,. . . ,
 Bk, B
′
k

sont respectivement A1, A2,. . . , Ak. Alors, A1⊗A2⊗. . .⊗Ak est la matrice de
A1 ⊗A2 ⊗. . . ⊗Ak par rapport à (B1 ⊗B2 ⊗. . . ⊗Bk, B′1 ⊗B′2 ⊗. . . ⊗B′k).
Cependant, A1 ⊗A2 ⊗. . . ⊗Ak
∈L (E1 ⊗E2 ⊗. . . ⊗Ek, F1 ⊗F2 ⊗. . . ⊗Fk) et Aσ(1) ⊗Aσ(2) ⊗. . . ⊗Aσ(k)
∈L
 Eσ(1) ⊗. . . ⊗Eσ(k), Fσ(1) ⊗. . . ⊗Fσ(k)

,
donc
Uσ·(A1 ⊗. . . ⊗Ak),
 Aσ(1) ⊗. . . ⊗Aσ(k)

·Vσ ∈L
 E1 ⊗. . . ⊗Ek, Fσ(1) ⊗. . . ⊗Fσ(k)

.
Aσ(1)⊗Aσ(2)⊗. . .⊗Aσ(k) est la matrice de Aσ(1)⊗Aσ(2)⊗. . .⊗Aσ(k) par rapport
à
 Bσ(1) ⊗. . . ⊗Bσ(k), B′σ(1) ⊗. . . ⊗B′σ(k)

. Par suite (Aσ(1)⊗. . .⊗Aσ(k))·Vσ
est celle de (Aσ(1)⊗. . .⊗Aσ(k))·Vσ par rapport à
 B1 ⊗. . . ⊗Bk, B′σ(1) ⊗. . . ⊗B′σ(k)

.
Uσ · (A1 ⊗A2 ⊗. . . ⊗Ak) est la matrice de Uσ · (A1 ⊗A2 ⊗. . . ⊗Ak) par
rapport au même couple de bases.
D’après la proposition 12, nous avons
Uσ · (A1 ⊗. . . ⊗Ak) =
 Aσ(1) ⊗. . . ⊗Aσ(k)

· Vσ
Proposition 15 La matrice Uσ est une σ-MPT n1 ⊗n2 ⊗. . . ⊗nk si, et
seulement si, pour tous a1 ∈Cn1×1, a2 ∈Cn2×1,. . . , ak ∈Cnk×1
Uσ · (a1 ⊗. . . ⊗ak)=aσ(1) ⊗. . . ⊗aσ(k)
Preuve. ” =⇒” C’est évident d’après la proposition 14.
” ⇐= ” Supposons que pour tous
a1 ∈Cn1×1, a2 ∈Cn2×1,. . . , ak ∈Cnk×1
Uσ · (a1 ⊗. . . ⊗ak)=aσ(1) ⊗. . . ⊗aσ(k)


## Page 26


18
CHAPITRE 2. MATRICES DE PERMUTATION TENSORIELLE
Soient a1 ∈E1, a2 ∈E2, . . . , ak ∈Ek et B1, B2,. . . , Bk bases de E1, E2,
. . . , Ek par rapport auxquelles les composantes de a1, a2,. . . , ak forment les
matrices colonnes a1, a2,. . . , ak. Le σ-OPT Uσ ∈
L(E1 ⊗E2 ⊗. . . ⊗Ek,
Eσ(1) ⊗Eσ(2) ⊗. . . ⊗Eσ(k)) dont la matrice par rapport à (B1⊗B2⊗. . . ⊗
Bk, Bσ(1)⊗Bσ(2)⊗. . . ⊗Bσ(k) ) est Uσ. Donc
Uσ(a1 ⊗. . . ⊗ak)= aσ(1) ⊗. . . ⊗aσ(k). Ceci est vraie pour tous a1 ∈E1, a2 ∈E2,
. . . , ak ∈Ek.
Puisque Uσ est un σ-OPT, Uσ est une σ-MPT n1 ⊗n2 ⊗. . . ⊗nk .
2.2.2
Expression d’un élément d’une matrice de permu-
tation tensorielle
Maintenant, nous allons généraliser la formule (2.2). Considérons les ma-
trices Inσ(r)×nr =
 δir
jr

1≤ir≤nσ(r),1≤jr≤nr, r = 1, 2, . . . , k.
Inσ(1)×n1 ⊗Inσ(2)×n2 ⊗. . . ⊗Inσ(k)×nk =
 δi1i2...ik
j1j2...jk

=
 δi1
j1δi2
j2 . . . δik
jk

,
est une matrice carrée n1n2 . . . nk × nσ(1)nσ(2) . . . nσ(k), qui nous suggère la
proposition suivante.
Proposition 16
Un1⊗n2⊗...⊗nk(σ) =
 Ui1i2...ik
j1j2...jk

=

δi1
jσ(1)δi2
jσ(2) . . . δik
jσ(k)

Preuve. Pour ar = (ajr
r )1≤jr≤nr ∈Cnr×1, r = 1, 2, . . . , k,
(a1 ⊗a2 ⊗. . . ⊗ak)i1i2...ik −→(Un1⊗n2⊗...⊗nk(σ) · (a1 ⊗a2 ⊗. . . ⊗ak))i1i2...ik =
= δi1
jσ(1)δi2
jσ(2) . . . δik
jσ(k)aj1
1 aj2
2 . . . ajk
k
= δi1
jσ(1)a
jσ(1)
σ(1) δi2
jσ(2)a
jσ(2)
σ(2) . . . δik
jσ(k)a
jσ(k)
σ(k)
= ai1
σ(1)ai2
σ(2) . . . aik
σ(k)
=
 aσ(1) ⊗aσ(2) ⊗. . . ⊗aσ(k)
i1i2...ik
2.2.3
Décomposition d’une matrice de permutation ten-
sorielle
Déﬁnition 17 Pour k ∈N, k > 2 et pour une permutation σ sur {1, 2, . . . , k},
nous appelons σ-matrice de transposition tensorielle n1 ⊗n2 ⊗. . . ⊗nk une


## Page 27


2.2. MATRICES DE PERMUTATION TENSORIELLE
19
σ-MPT n1 ⊗n2 ⊗. . . ⊗nk si σ est une transposition.
Considérons la σ-matrice de transposition tensorielle n1 ⊗n2 ⊗. . . ⊗nk,
Un1⊗n2⊗...⊗nk(σ) avec σ la transposition (i j).
Un1⊗n2⊗...⊗nk(σ) · (a1 ⊗. . . ⊗ai ⊗ai+1 ⊗. . . ⊗aj ⊗aj+1 ⊗. . . ⊗ak)
= a1 ⊗. . . ⊗ai−1 ⊗aj ⊗ai+1 ⊗. . . ⊗aj−1 ⊗ai ⊗aj+1 ⊗. . . ⊗ak
pour tous al ∈Cnl×1.
Si (Bli)1≤li≤njni,
 Blj

1≤lj≤ninj sont respectivement des bases de Cnj×ni et
Cni×nj, alors la MCT Uni⊗nj peut être decomposée comme une combinaison
linéaire de la base
 Bli ⊗Blj

1≤li≤njni,1≤lj≤ninj de Cninj×ninj. Nous voulons
prouver que Un1⊗n2⊗...⊗nk(σ) est une combinaison linéaire de
 In1n2...ni−1 ⊗Bli ⊗Ini+1ni+2...nj−1 ⊗Blj ⊗Inj+1nj+2...nk

1≤li≤njni,1≤lj≤ninj.
Pour ce faire, il nous suﬃt de prouver la proposition suivante.
Proposition 18 Supposons σ =

1
2
3
3
2
1

=
 1
3

permutation sur
{1, 2, 3}, (Bi1)1≤i1≤N3N1, (Bi3)1≤i3≤N1N3 sont respectivement des bases de CN3×N1
et CN1×N3. Si UN1⊗N3 =
N1N3
X
i1=1
N1N3
X
i3=1
αi1i3Bi1 ⊗Bi3, αi1i3 ∈C, alors
UN1⊗N2⊗N3 (σ) =
N1N3
X
i1=1
N1N3
X
i3=1
αi1i3Bi1 ⊗IN2 ⊗Bi3.
Preuve. Soient b1 ∈CN1×1, b3 ∈CN3×1.
Développons d’abord la relation
UN1⊗N3 · (b1 ⊗b3) = b3 ⊗b1
N1N3
X
i1=1
N1N3
X
i3=1
αi1i3 (Bi1 ⊗Bi3) . (b1 ⊗b3) = b3 ⊗b1
N1N3
X
i1=1
N1N3
X
i3=1
αi1i3 (Bi1.b1) ⊗(Bi3.b3) = b3 ⊗b1
En utilisant la proposition 39, de l’Annexe B,


## Page 28


20
CHAPITRE 2. MATRICES DE PERMUTATION TENSORIELLE
N1N3
X
i1=1
N1N3
X
i3=1
αi1i3 (Bi1.b1) ⊗b2 ⊗(Bi3.b3) = b3 ⊗b2 ⊗b1
N1N3
X
i1=1
N1N3
X
i3=1
αi1i3 (Bi1.b1) ⊗(IN2.b2) ⊗(Bi3.b3) = b3 ⊗b2 ⊗b1
N1N3
X
i1=1
N1N3
X
i3=1
αi1i3 (Bi1 ⊗IN2 ⊗Bi3) . (b1 ⊗b2 ⊗b3) = b3 ⊗b2 ⊗b1
D’où,
UN1⊗N2⊗N3 (σ) =
N1N3
X
i1=1
N1N3
X
i3=1
αi1i3Bi1 ⊗IN2 ⊗Bi3
Notation 19 Soit σ ∈Sn, c’est-à-dire σ est une permutation sur {1, 2, . . . ,
n}, p ∈N, p ≥2, nous notons la MPT Up ⊗p ⊗. . . ⊗p
|
{z
}
n−times
(σ) par Up⊗n (σ),
[31].
Nous utilisons les lemmes [32] suivants pour prouver la proposition ci-
dessous.
Lemme 20 Toute permutation σ ∈Sn peut s’écrire comme produit de trans-
positions. (Cette factorisation en un produit de transpositions n’est pas unique)
Cσ = (i1 i2 i3 . . . in−1 in) = (i1 i2) (i2 i3) . . . (in−1 in)
Lemme 21 Soit σ ∈Sn, dont le cycle est
Cσ = (i1 i2 i3 . . . in−1 in)
alors
Cσ = (i1 i2 i3 . . . in−1) (in−1 in)
Proposition 22 Pour n ∈N∗, n > 1, σ ∈Sn dont le cycle est
Cσ = (i1 i2 i3 . . . ik−1 ik)
avec k ∈N∗, k > 2. Alors,
Up⊗n (σ) = Up⊗n ((i1 i2 . . . ik−1)) · Up⊗n ((ik−1 ik))
ou
Up⊗n (σ) = Up⊗n ((i1 i2)) · Up⊗n ((i2 i3)) · . . . · Up⊗n ((ik−1 ik))
avec p ∈N∗, p > 2.


## Page 29


2.3. MATRICES DE COMMUTATION TENSORIELLE ET EQUATIONS MATRICIELLES 21
Ainsi, une MPT peut être exprimée comme un produit de matrices de trans-
position tensorielle.
Corollaire 23 Pour n ∈N∗, n > 2, σ ∈Sn dont le cycle est
Cσ = (i1 i2 i3 . . . in−1 n)
Alors,
Up⊗n (σ) =

Up⊗(n−1) ((i1 i2 . . . in−2 in−1)) ⊗Ip

· Up⊗n ((in−1 n))
2.3
MATRICES DE COMMUTATION TEN-
SORIELLE ET EQUATIONS MATRICIELLES
Les équations matricielles que nous allons voir dans cette section sont les
équations matricielles de la forme AX = B, A·X·B = C et A·X+X·B = C.
Pour la première équation une étude de la méthode de Cholesky sera donnée.
La deuxième et la troisième équations peut être ramenées à la première, et
c’est là que nous introduirons les MCT.
2.3.1
Sur la méthode de Cholesky
Les méthodes directes pour résoudre un système linéaire, méthode d’élimina-
tion de Gauss, décomposition LU et méthode de Cholesky sont bien connues.
Nous sommes d’accord avec certains auteurs [34, 35] que la décomposition LU
et la méthode de Cholesky sont très utiles pour résoudre plusieurs systèmes
linéaires dont la seule diﬀérence est les termes constants dans les seconds
membres.
La méthode d’élimination de Gauss avec ou sans choix de pivot peut
nous conduire à la décomposition LU. La méthode d’élimination de Gauss
avec choix de pivot ne peut pas nous conduire à la méthode de Cholesky car
le choix de pivot peut détruire la syméetrie. Cependant, quelques fois nous
n’avons pas besoin de choisir le pivot.
Comme la méthode d’élimination de Gauss peut nous conduire à la dé-
composition LU, nous pensons que c’est mieux de résoudre d’abord l’une de
ces équations par la méthode d’élimination de Gauss et les autres par la dé-
composition LU. Ainsi, nous serons permis de résoudre d’abord l’une de ces
équation par la méthode d’élimination de Gauss et les autres par la méthode
de Cholesky, dans le cas où la matrice est symétrique et déﬁnie positive, si la
méthode d’élimination de Gauss peut nous conduire à la décomposition de
Cholesky.


## Page 30


22
CHAPITRE 2. MATRICES DE PERMUTATION TENSORIELLE
Cette sous-section est arrangée de la façons suivante. Dans le paragraphe
ci-dessous nous allons présenter la décomposition LU en utilisant la méthode
d’élimination de Gauss. Dans le paragraphe suivant, nous prouverons avec
l’aide de la décomposition LU que nous pouvons obtenir la décomposition de
Cholesky à partir de la méthode d’élimination de Gauss sans choix de pivot.
Enﬁn, un exemple pour rendre plus claire la méthode sera présenté.
Elimination de Gauss
Considérons le système de n équations à n incon-
nues suivant :

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

a11x1 + a12x2 + . . . + a1nxn
= b1
a21x1 + a22x2 + . . . + a2nxn
= b2
. . . . . . . . . . . . . . . . . . . . . . . . . . .
ai1x1 + ai2x2 + . . . + ainxn
= bi
. . . . . . . . . . . . . . . . . . . . . . . . . . .
an1x1 + an2x2 + . . . + annxn
= bn
qui peut s’écrire sous forme matricielle
AX = B
(2.4)
où
A = (aij)1≤i,j≤n, X =





x1
x2
...
xn




, B =





b1
b2
...
bn





Si a11 ̸= 0, l’élimination de Gauss sur la première colonne s’écrit
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
a(0)
11 x1
+
a(0)
12 x2
+
. . .
+
a(0)
1n xn
= b(0)
1
a(1)
22 x2
+
. . .
+
a(1)
2n xn
= b(1)
2
. . .
. . .
. . .
. . .
. . .
. . . . . .
a(1)
i2 x2
+
. . .
+
a(1)
in xn
= b(1)
i
. . .
. . .
. . .
. . .
. . .
. . . . . .
a(1)
n2 x2
+
. . .
+
a(1)
nnxn
= b(1)
n
avec a(0)
1j = a1j et a(1)
ij = −ai1a1j−a11aij
a11
,
qui peut s’écrire, sous forme matricielle
A1X = B1
(2.5)
et peut être obtenue en multipliant (2.4) par la matrice triangulaire inférieure


## Page 31


2.3. MATRICES DE COMMUTATION TENSORIELLE ET EQUATIONS MATRICIELLES 23
[36, 37]
G1 =













1
0
0
. . .
0
−a(0)
21
a(0)
11
1
0
. . .
0
−a(0)
31
a(0)
11
0
1
. . .
0
...
...
...
...
...
−a(0)
n1
a(0)
11
0
0
. . .
1













A1 = G1A et B1 = G1B.
L’élimination de Gauss sur la deuxième colonne peut être obtenue par
multiplication à la relation (2.5) la matrice triangulaire inférieure
G2 =















1
0
0
0
. . .
0
0
1
0
0
. . .
0
0
−a(1)
32
a(1)
22
1
0
. . .
0
0
−a(1)
42
a(1)
22
0
1
. . .
0
...
...
...
...
...
...
0
−a(1)
n2
a(1)
22
0
0
. . .
1















L’équation matricielle (2.5) devient
A2X = B2
avec A2 = G2G1A et B2 = G2G1B.
En continuant ainsi, nous avons ﬁnalement,
UX = B′
(2.6)
avec U = Gn−1 . . . G2G1U une matrice triangulaire supérieure et B′ =
Gn−1 . . . G2G1B.


## Page 32


24
CHAPITRE 2. MATRICES DE PERMUTATION TENSORIELLE
Nous pouvons vériﬁer facilement que l’inverse de Gl est
G−1
l
=






















1
0
. . .
0
. . .
0
0
1
. . .
0
. . .
0
...
...
...
...
...
0
0
. . .
1
. . .
0
0
0
. . .
a(l−1)
(l+1)l
a(l−1)
ll
. . .
0
...
...
...
...
...
0
0
. . .
a(l−1)
nl
a(l−1)
ll
. . .
1






















Donc Gn−1Gn−2 · · · G2G1 est une matrice inversible et l’équation (2.6) de-
vient
LUX = B
avec L = G−1
1 G−1
2 · · · G−1
n−2G−1
n−1 et nous avons la décomposition de A comme
produit de matrice triangulaire inférieure par une matrice triangulaire supé-
rieure
A = LU
On peut vériﬁer facilement que
L =

























1
0
. . .
0
. . .
0
a(0)
21
a(0)
11
1
. . .
0
. . .
0
a(0)
31
a(0)
11
a(1)
32
a(1)
22
...
...
...
...
...
. . .
1
. . .
0
a(0)
(l+1)1
a(0)
11
a(1)
(l+1)2
a(1)
22
. . .
a(l−1)
(l+1)l
a(l−1)
ll
...
0
...
...
...
...
a(0)
n1
a(0)
11
a(1)
(n)2
a(1)
22
. . .
a(l−1)
nl
a(l−1)
ll
. . .
1



























## Page 33


2.3. MATRICES DE COMMUTATION TENSORIELLE ET EQUATIONS MATRICIELLES 25
Méthode de Cholesky
Maintenant, supposons A est une matrice symé-
trique et déﬁnie positive. Alors, la méthode de Cholesky consiste à décom-
poser A comme le produit
A = GTG
avec G est une matrice triangulaire supérieure et GT son transposée.
Laissons nous d’abord généraliser cette décomposition.
Déﬁnition 24 Soit A = (aij)1≤i,j≤n une matrice complexe symétrique. Nous
appelons matrice de Gauss de A la matrice triangulaire supérieure U(A),
obtenue en transformant A par l’élimination de Gauss ci-dessus.
Proposition 25 Soit A = (aij)1≤i,j≤n une matrice complexe symétrique,
telle que det(A) ̸= 0,
U(A) =





u11
u12
. . .
u1n
0
u22
. . .
u2n
...
...
...
...
0
0
. . .
unn





la matrice de Gauss de A. Alors A peut être décomposée comme le produit
A = GTG avec
G =





u11
√u11
u12
√u11
. . .
u1n
√u11
0
u22
√u22
. . .
u2n
√u22
...
...
...
...
0
0
. . .
unn
√unn





où √uii une racine carrée du nombre complexe uii.
Preuve.
U(A) =





a(0)
11
a(0)
12
. . .
a(0)
1n
0
a(1)
22
. . .
a(1)
2n
...
...
...
...
0
0
. . .
a(n−1)
nn







## Page 34


26
CHAPITRE 2. MATRICES DE PERMUTATION TENSORIELLE
L(A) =

























1
0
. . .
0
. . .
0
a(0)
21
a(0)
11
1
. . .
0
. . .
0
a(0)
31
a(0)
11
a(1)
32
a(1)
22
...
...
...
...
...
. . .
1
. . .
0
a(0)
(l+1)1
a(0)
11
a(1)
(l+1)2
a(1)
22
. . .
a(l−1)
(l+1)l
a(l−1)
ll
...
0
...
...
...
...
a(0)
n1
a(0)
11
a(1)
(n)2
a(1)
22
. . .
a(l−1)
nl
a(l−1)
ll
. . .
1

























A = L(A)D−1DU(A)
avec
D =








1
q
a(0)
11
0
. . .
0
0
1
q
a(1)
22
. . .
0
...
...
...
...
0
0
. . .
1
√
a(n−1)
nn








Soit G = DU(A). Comme A est symétrique, d’où L(A)D−1 = GT.
Exemple 26 Considérons les deux systèmes d’quations linéaires suivants







x1
−
x2
+
x4
= 3
−x1
+
5x2
+
2x3
−
3x4
= −5
2x2
+
5x2
+
x4
= −7
x1
−
3x2
+
x3
+
4x4
= 2







x1
−
x2
+
x4
= 3
−x1
+
5x2
+
2x3
−
3x4
= 1
2x2
+
5x2
+
x4
= 2
x1
−
3x2
+
x3
+
4x4
= 2


## Page 35


2.3. MATRICES DE COMMUTATION TENSORIELLE ET EQUATIONS MATRICIELLES 27
dont la seule diﬀérence est les seconds membres et leur matrice est symé-
trique. Ainsi, résolvons le premier par la méthode d’élimination de Gauss et
le second par la décomposition LU ou la méthode de Cholesky.




1
0
0
0
1
1
0
0
0
0
1
0
−1
0
0
1








1
−1
0
1
−1
5
2
−3
0
2
5
1
1
−3
1
4








x1
x2
x3
x4



=




1
0
0
0
1
1
0
0
0
0
1
0
−1
0
0
1








3
−5
−7
2








1
−1
0
1
0
4
2
−2
0
2
5
1
0
−2
1
3








x1
x2
x3
x4



=




3
−2
−7
−1








1
0
0
0
0
1
0
0
0
−1
2
1
0
0
1
2
0
1








1
−1
0
1
0
4
2
−2
0
2
5
1
0
−2
1
3








x1
x2
x3
x4



=




1
0
0
0
0
1
0
0
0
−1
2
1
0
0
1
2
0
1








3
−2
−7
−1








1
−1
0
1
0
4
2
−2
0
0
4
2
0
0
2
2








x1
x2
x3
x4



=




3
−2
−6
−2








1
0
0
0
0
1
0
0
0
0
1
0
0
0
−1
2
1








1
−1
0
1
0
4
2
−2
0
0
4
2
0
0
2
2








x1
x2
x3
x4



=




1
0
0
0
0
1
0
0
0
0
1
0
0
0
−1
2
1








3
−2
−6
−2








1
−1
0
1
0
4
2
−2
0
0
4
2
0
0
0
1








x1
x2
x3
x4



=




3
−2
−6
1




x4 = 1, 4x3 + 2 = −6, x3 = −2, 4x2 −4 −2 = −2, x2 = 1, x1 −1 + 1 = 3,
x1 = 3
Maintenant, passons au deuxième système, qui peut s’écrire, d’après la
Proposition 25, GTGX = B et être résolu en écrivant

GTY
= B
GX
= Y




1
0
0
0
−1
2
0
0
0
1
2
0
1
−1
1
1








y1
y2
y3
y4



=




3
1
2
2






## Page 36


28
CHAPITRE 2. MATRICES DE PERMUTATION TENSORIELLE
y1 = 3, 3 + 2y2 = 1, y2 = 2, 2 + 2y3 = 2, y3 = 0, 3 −2 + y4 = 2, y4 = 1




1
−1
0
1
0
2
1
−1
0
0
2
1
0
0
0
1








x1
x2
x3
x4



=




3
2
0
1




x4 = 1, 2x3 + 1 = 0, x3 = −1
2, 2x2 −1
2 −1 = 2, x2 = 7
4, x1 −7
4 + 1 = 3,
x1 = 15
4
2.3.2
Matrices de commutation tensorielle et transfor-
mées d’une équation matricielle
Dans cette sous-section, les transformées de certaines équations matri-
cielles, aux équations matricielles de la forme (2.4), se transforment l’une à
l’autre à aide d’une MCT.
A · X · B = C
Soient A, B, et C, matrices m × n, p × q et m × q, respecti-
vement. Considérons l’équation matricielle A · X · B = C, par rapport à X,
matrice n × q. Cette équation peut se transformer au système d’équations
linéaires dont l’équations matricielle est [38]
 A ⊗BT
· L (X) = L (C)
(2.7)
ou
 BT ⊗A

· L
 XT
= L
 CT
(2.8)
L’équation (2.8) s’obtient en multipliant l’équation (2.7) par la MCT Um⊗q
et en utilisant la remarque 8.
Réciproquement, l’équation (2.7) s’obtient en multipliant l’équation (2.8) par
la MCT Uq⊗m.
A · X + X · B = C
L’équation matricielle A · X + X · B = C, où A est une
matrice m × m, B est une matrice n × n et C est une matrice m × n, peut
se transformer au système d’équations linéaires dont l’équations matricielle
est [38]
 A ⊗In + Im ⊗BT
· L (X) = L (C)
(2.9)
où In est la matrice unité n × n, ou
 In ⊗A + BT ⊗Im

· L
 XT
= L
 CT
(2.10)
L’équation (2.10) s’obtient en multipliant l’équation (2.9) par la MCT Um⊗n.
Réciproquement, l’équation (2.9) s’obtient en multipliant l’équation (2.10)
par la MCT Un⊗m.


## Page 37


Chapitre 3
VERS UNE APPLICATION EN
PHYSIQUE DES PARTICULES
Ce chapitre est basé sur Refs. [28, 39, 40, 41]
3.1
MATRICES DE PERMUTATION TENSO-
RIELLE ET MATRICES DE GELL-MANN
3.1.1
MCT en termes de matrices de Gell-Mann géné-
ralisées
Soit n ∈N, n ≥2. Les matrices de Gell-Mann généralisées ou ma-
trices de Gell-Mann n × n sont des matrices hermitiennes et de trace nulles
Λ1,Λ2,. . . ,Λn2−1 qui satisfont la relation de commutation (Cf. par exemple
[42])
[Λa, Λb] = 2i
n2−1
X
a=1
fabcΛc
(3.1)
où fabc sont les constantes de structure qui sont réelles et totalement antisy-
métriques, et
Tr (Λa, Λb) = 2δab
avec δab le symbole de Kronecker.
Pour n = 2, les matrices de Gell-Mann 2 × 2 sont les matrices de Pauli ha-
bituelles. Pour n = 3, elles correspondent aux huit matrices de Gell-Mann
3 × 3, qui se construisent de la façon suivante : les trois premières sont des
matrices 3 × 3 obtenues en ajoutant aux trois matrices de Pauli troisième
ligne et troisième colonne formées de 0, à savoir
29


## Page 38


30CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
λ1 =


0
1
0
1
0
0
0
0
0

, λ2 =


0
−i
0
i
0
0
0
0
0

, λ3 =


1
0
0
0
−1
0
0
0
0


Les deux secondes matrices 3 × 3 sont obtenues en ajoutant aux deux ma-
trices Pauli non-diagonales deuxième ligne et deuxième colonne formées de
0, à savoir
λ4 =


0
0
1
0
0
0
1
0
0

, λ5 =


0
0
−i
0
0
0
i
0
0


Les deux troisième matrices 3 × 3 sont obtenues en ajoutant aux deux ma-
trices Pauli non-diagonales première ligne et première colonne formées de 0,
à savoir
λ6 =


0
0
0
0
0
1
0
1
0

, λ7 =


0
0
0
0
0
−i
0
i
0


Et ﬁnalement, la dérnière matrice est une matrice diagonale qui est hermi-
tienne, trace nulle avec
Tr
 λ8
2
= 2
à savoir
λ8 =
1
√
3


1
0
0
0
1
0
0
0
−2


De façon analogue, nous pouvons construire à partir des matrices de Gell-
Mann (n −1) × (n −1) les matrices de Gell-Mann n × n. Les premières
[(n −1)2 −1] matrices de Gell-Mann n × n sont obtenues en ajoutant n-
ième ligne et n-ième colonne formées de 0 à chaque matrices de Gell-Mann
(n−1) ×(n−1). Les (2n−2) matrices de Gell-Mann n×n sont les matrices
symétriques et les matrices antisymétriques non-diagonales suivantes
Λ(n−1)2 =









0
0
. . .
. . .
0
1
0
0
0
...
...
...
...
...
...
0
0
1
0
. . .
. . .
0
0









, Λ(n−1)2+1 =









0
0
. . .
. . .
0
−i
0
0
0
...
...
...
...
...
...
0
0
i
0
. . .
. . .
0
0









,


## Page 39


3.1. MATRICES DE PERMUTATION TENSORIELLE ET MATRICES DE GELL-MANN 31
Λ(n−1)2+2 =









0
0
. . .
. . .
0
0
0
0
1
...
...
0
0
...
...
0
0
0
1
. . .
. . .
0
0









, Λ(n−1)2+3 =









0
0
. . .
. . .
0
0
0
0
−i
...
...
0
0
...
...
0
0
0
i
. . .
. . .
0
0









,
...,
Λn2−3 =










0
0
. . .
. . .
0
0
...
0
...
...
...
...
...
...
0
0
1
0
. . .
. . .
. . .
1
0










, Λn2−2 =










0
0
. . .
. . .
0
0
...
0
...
...
...
...
...
...
0
0
−i
0
. . .
. . .
. . .
i
0










et ﬁnalement, la dérnière matrice est une matrice diagonale, hermitienne et
de trace nulle avec
Tr
 Λn2−1
2
= 2
à savoir
Λn2−1 =
1
√
C2n









1
0
. . .
. . .
. . .
0
0
1
...
...
...
...
...
...
1
0
0
. . .
. . .
. . .
0
−(n −1)









Elles satisfont aussi la relation d’anticommutation (Cf. par exemple[42])
{Λa, Λb} = 4
nδabIn + 2
n2−1
X
c=1
dabcΛc
(3.2)
où les constantes dabc sont réelles et totalement symétriques, et en utilisant
les relations (3.1) et (3.2), nous avons
ΛaΛb = 2
nδab +
n2−1
X
c=1
dabcΛc + i
n2−1
X
c=1
fabcΛc
(3.3)
Les constantes de structure satisfont la relation (Cf. par exemple[42])
n2−1
X
e=1
fabefcde = 2
n (δacδbd −δadδbc) +
n2−1
X
e=1
daceddbe −
n2−1
X
e=1
dadedbce
(3.4)


## Page 40


32CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
Pour la démonstration du Théorème 27 ci-dessous, notons, pour 1 ≤i <
j ≤n, les C2
n =
n!
2!(n−2)! matrices de Gell-Mann n × n qui sont symétriques
avec des éléments tous 0 sauf le i-ième ligne j-ième colonne et le j-ième ligne
i-ième colonne qui sont égaux à 1, par Λ(ij), les C2
n =
n!
2!(n−2)! matrices de
Gell-Mann n × n qui sont antisymétriques avec des éléments tous 0 sauf le
i-ième ligne j-ième colonne qui est égal à −i et le j-ième ligne i-ième colonne
qui est égal à i , par Λ[ij] et enﬁn, par Λ(d),1 ≤d ≤n−1, les (n−1) matrices
de Gell-Mann n × n suivantes, qui sont diagonales :
Λ(1) =










1
0
. . .
0
0
−1
0
...
...
...
...
0
. . .
0










, Λ(2) =
1
√
3










1
0
. . .
0
0
1
−2
...
...
0
...
0
. . .
0










,
. . . ,
Λ(n−1) =
1
√
C2n









1
0
. . .
0
0
1
1
...
...
...
1
0
. . .
−(n −1)









Théorème 27 Nous avons
Un⊗n = 1
nIn ⊗In + 1
2
n2−1
X
i=1
Λi ⊗Λi
(3.5)
Preuve.
In ⊗In =
 δi1i2
j1j2

=
 δi1
j1δi2
j2

Un⊗n =
 δi1
j2δi2
j1

(3.1.6)
où,
i1i2 sont des indices de ligne
j1j2 sont des indices de colonne [4].
Considérons d’abord les C2
n matrices de Gell-Mann n × n symétriques, qui


## Page 41


3.1. MATRICES DE PERMUTATION TENSORIELLE ET MATRICES DE GELL-MANN 33
peuvent s’écrire
Λ(ij) =

Λ(ij)l
k

1≤l≤n,1≤k≤n
=
 δilδj
k

1≤l≤n,1≤k≤n +
 δjlδi
k

1≤l≤n,1≤k≤n
=
 δilδj
k + δjlδi
k

1≤l≤n,1≤k≤n
Alors
Λ(ij) ⊗Λ(ij) =
 Λ(ij) ⊗Λ(ij)l1l2
k1k2

=
 δil1δj
k1 + δjl1δi
k1
  δil2δj
k2 + δjl2δi
k2

l1l2 indices de ligne, k1k2 indices de colonne.
C’est-à-dire
 Λ(ij) ⊗Λ(ij)l1l2
k1k2 = δil1δj
k1δil2δj
k2 +δil1δj
k1δjl2δi
k2 +δjl1δi
k1δil2δj
k2 +δjl1δi
k1δjl2δi
k2
Les C2
n matrices de Gell-Mann n × n, antisymétriques peuvent s’écrire
Λ[ij] =

Λ[ij]l
k

1≤l≤n,1≤k≤n =
 −iδilδj
k + iδjlδi
k

1≤l≤n,1≤k≤n
Alors
Λ[ij] ⊗Λ[ij] =
 Λ[ij] ⊗Λ[ij]l1l2
k1k2

 Λ[ij] ⊗Λ[ij]l1l2
k1k2 = −δil1δj
k1δil2δj
k2+δil1δj
k1δjl2δi
k2+δjl1δi
k1δil2δj
k2−δjl1δi
k1δjl2δi
k2
et
X
1≤i<j≤n
 Λ(ij) ⊗Λ(ij)l1l2
k1k2 +
X
1≤i<j≤n
 Λ[ij] ⊗Λ[ij]l1l2
k1k2
= 2
X
1≤i<j≤n
 δil1δj
k1δjl2δi
k2 + δjl1δi
k1δil2δj
k2

= 2
X
i̸=j
δil1δj
k1δjl2δi
k2
la l1l2-ième ligne k1k2-ième colonne de la matrice
X
1≤i<j≤n
Λ(ij) ⊗Λ(ij) +
X
1≤i<j≤n
Λ[ij] ⊗Λ[ij].
Maintenant, considérons les matrices de Gell-Mann n×n, diagonales. Soit
d ∈N, 1 ≤d ≤n −1,
Λ(d) =
1
√
C2
d+1
 
δl
k
d
X
p=1
δp
k −dδl
kδd+1
k
!


## Page 42


34CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
et la l1l2-ième ligne k1k2-ième colonne de la matrice Λ(d) ⊗Λ(d) est
 Λ(d) ⊗Λ(d)l1l2
k1k2 =
1
C2
d+1
δl1
k1δl2
k2
 
d
X
q=1
d
X
p=1
δq
k1δp
k2
!
−
1
C2
d+1
δl1
k1δl2
k2
 
dδd+1
k2
d
X
p=1
δp
k1
!
−
1
C2
d+1
δl1
k1δl2
k2
 
dδd+1
k1
d
X
p=1
δp
k2
!
+
1
C2
d+1
δl1
k1δl2
k2
 d2δd+1
k1 δd+1
k2

Λ(d) ⊗Λ(d) est une matrice diagonale, donc tout ce que nous devons à faire
est de calculer les éléments sur la diagonale, où l1 = k1 et l2 = k2. Alors,
n−1
X
d=1
 Λ(d) ⊗Λ(d)l1l2
k1k2 =
n−1
X
d=1
1
C2
d+1
 
d
X
q=1
δq
k1
!  
d
X
p=1
δp
k2
!
−
n−1
X
d=1
1
C2
d+1
dδd+1
k2
d
X
p=1
δp
k1
−
n−1
X
d=1
1
C2
d+1
dδd+1
k1
d
X
p=1
δp
k2
+
n−1
X
d=1
1
C2
d+1
d2δd+1
k1 δd+1
k2
la l1l2-ième ligne k1k2-ième colonne de la matrice diagonale
n−1
X
d=1
Λ(d) ⊗Λ(d)
avec l1 = k1 et l2 = k2.
Laissons nous distinguer deux cas.
1er cas : k1 ̸= 1 or k2 ̸= 1
cas1 : k1 ̸= k2


## Page 43


3.1. MATRICES DE PERMUTATION TENSORIELLE ET MATRICES DE GELL-MANN 35
Si k1 < k2,
n−1
X
d=1
 Λ(d) ⊗Λ(d)l1l2
k1k2 =
n−1
X
d=k2
1
C2
d+1
−k2 −1
C2
k2
= 2
" n−1
X
d=k2
1
d −
1
d + 1

−1
k2
#
= −2
n
De façon Similaire, si k1 > k2,
n−1
X
d=1
 Λ(d) ⊗Λ(d)l1l2
k1k2 = −2
n
cas2 : k1 = k2 ̸= 1
n−1
X
d=1
 Λ(d) ⊗Λ(d)l1l2
k1k2 =
n−1
X
d=k2
1
C2
d+1
+ (k2 −1)2
C2
k2
=
2
k2
−2
n + (k2 −1)2
C2
k2
= 2 −2
n
2e cas : k1 = k2 = 1
n−1
X
d=1
 Λ(d) ⊗Λ(d)l1l2
k1k2 =
n−1
X
d=1
1
C2
d+1
= 2 −2
n
Nous pouvons compacter ces cas en une seule formule
n−1
X
d=1
 Λ(d) ⊗Λ(d)l1l2
k1k2 = −2
nδl1
k1δl2
k2 + 2
n
X
i=1
δil1δi
k1δil2δi
k2
qui donne la diagonale de la matrice diagonale
n−1
X
d=1
Λ(d) ⊗Λ(d).
Pour toutes les matrices de Gell-Mann n × n nous avons


## Page 44


36CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
X
1≤i<j≤n
 Λ(ij) ⊗Λ(ij)l1l2
k1k2 +
X
1≤i<j≤n
 Λ[ij] ⊗Λ[ij]l1l2
k1k2 +
n−1
X
d=1
 Λ(d) ⊗Λ(d)l1l2
k1k2
= −2
nδl1
k1δl2
k2 + 2
n
X
i=1
δil1δi
k1δil2δi
k2 + 2
X
i̸=j
δil1δj
k1δjl2δi
k2
= −2
nδl1
k1δl2
k2 + 2
n
X
j=1
n
X
i=1
δil1δj
k1δjl2δi
k2
= −2
nδl1
k1δl2
k2 + 2δl1
k2δl2
k1
pour tous l1, l2, k1,k2 ∈{1, 2, . . . , n}.
D’où, en utilisant (3.1.6)
n2−1
X
i=1
Λi ⊗Λi = −2
nIn ⊗In + 2Un⊗n
et le théorème est prouvé.
3.1.2
Matrices de Gell-Mann rectangles
Dans cette sous-section nous voulons généraliser la formule (3.5) à l’ex-
pression de Un⊗p avec n ̸= p.
Nous avions essayé d’exprimer les MCT U2⊗3 et U3⊗2 comme combinaisons
linéaire des produits tensoriels des matrices de Pauli avec les matrices de
Gell-Mann 3 ×3, en espérant d’avoir des expressions qui mènent à la généra-
lisation de (3.5) à l’expression de Un⊗p avec n ̸= p. Cependant, les expressions
obtenues ne sont pas assez interéssant pour la généralisation voulue. Nous
avons remarqué que pour généraliser (3.5) à l’expression de Un⊗p, n ̸= p,
nous devons utiliser des matrices rectangles au lieu de matrices carrées. Nous
appelons matrices de Gell-Mann rectangles des telles matrices rectangles.
D’abord, laissons nous considérer quelques cas particuliers.
– Matrices de Gell-Mann 2 × 3
Etant inspiré par une façon de construire les matrices de Gell-Mann
n × n à partir des matrices de Gell-Mann (n −1) × (n −1), nous
ajoutons aux matrices de Pauli et I2 troisième colonne formée de zeros.
Alors, nous avons un système formé par
I2×3 =

1
0
0
0
1
0

, Λ1 =

0
1
0
1
0
0

, Λ2 =

0
−i
0
i
0
0

, Λ3 =

1
0
0
0
−1
0



## Page 45


3.1. MATRICES DE PERMUTATION TENSORIELLE ET MATRICES DE GELL-MANN 37
Et pour obtenir une base de C2×3, nous ajoutons au système les ma-
trices
Λ4 =

0
0
√
2
0
0
0

, Λ5 =
 0
0
0
0
0
√
2

. Nous pouvons vériﬁer faci-
lement que
U2⊗3 = 1
2I+
2×3 ⊗I2×3 + 1
2
5
X
a=1
Λ+
a ⊗Λa
où Λ+
a est le conjugué hermitien de Λa.
– Matrices de Gell-Mann 3 × 2
De façon analogue, mais cette fois nous ajoutons aux matrices de Pauli
et I2 une troisième ligne formé de zeros, au lieu de colonne. Alors, nous
avons un système (Λa)1⩽a⩽5 de matrices 3 × 2 qui satisfont
U3⊗2 = 1
2I+
3×2 ⊗I3×2 + 1
2
5
X
a=1
Λ+
a ⊗Λa
En eﬀet, Un⊗p = UT
n⊗p = U+
n⊗p, pour tous n, p ∈N, n, p ⩾2.
– Matrices de Gell-Mann 2 × 4
Utilisant encore la même manière, mais pour ce cas nous ajoutons aux
matrices de Pauli et I2 troisème et quatrième colonnes formées de ze-
ros. Alors, nous avons un système formé par quatre matrices 2 × 4
I2×4, Λ1, Λ2, Λ3. Et pour obtenir une base de C2×4, nous ajoutons au
système les matrices
Λ4 =

0
0
√
2
0
0
0
0
0

, Λ5 =
 0
0
0
0
0
0
√
2
0

, Λ6 =

0
0
0
√
2
0
0
0
0

,
Λ7 =
 0
0
0
0
0
0
0
√
2

. Le système satisfait la relation
U2⊗4 = 1
2I+
2×4 ⊗I2×4 + 1
2
7
X
a=1
Λ+
a ⊗Λa
Déﬁnition 28 Soient n, p ∈N, p ⩾n ⩾2. Nous appelons matrices de Gell-
Mann n×p les matrices n lignes et p colonnes Λ1, Λ2, ..., Λn2−1, Λn2, Λn2+1,
..., Λnp−1 telles que :
Λ1, Λ2, ..., Λn2−1 sont obtenues en ajoutant aux matrices de Gell-Mann
n × n, (n + 1)-ième, (n + 2)-ième, ..., p-ième colonnes, formées de zeros ;
Λn2 =
√
2E(1,n+1)
n×p
, Λn2+1 =
√
2E(2,n+1)
n×p
,..., Λn2+n−1 =
√
2E(n,n+1)
n×p
,
Λn2+n =
√
2E(1,n+2)
n×p
, Λn2+n+1 =
√
2E(2,n+2)
n×p
, ..., Λn2+2n−1 =
√
2E(1,n+2)
n×p
,
....................................................................................................................,
Λn(p−1) =
√
2E(1,p)
n×p , Λn(p−1)+1 =
√
2E(2,p)
n×p , ..., Λnp−1 =
√
2E(n,p)
n×p .


## Page 46


38CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
Alors, nous déﬁnissons les matrices de Gell-Mann p × n comme les matrices
obtenues en prenant les conjugués hermitiens des matrices de Gell-Mann
n × p.
Proposition 29 Pour n, p ∈N, p, n ⩾2, considérons le système de matrices
de Gell-Mann n × p, Λ1, Λ2, ..., Λnp−1. Alors,
Un⊗p =
1
inf(n, p)I+
n×p ⊗In×p + 1
2
np−1
X
a=1
Λ+
a ⊗Λa
(3.1.7)
Preuve. Supposons p ⩾n.
1
2
np−1
X
a=n2
Λ+
a ⊗Λa =
(n,p)
X
(j,l)=(1,n+1)
E(j,l)T
n×p ⊗E(j,l)
n×p
(3.1.8)
En utilisant la proposition 6 et la formule (3.5) nous avons
(n,n)
X
(j,l)=(1,1)
E(j,l)T
n×n ⊗E(j,l)
n×n = 1
nIn ⊗In + 1
2
n2−1
X
a=1
Λ(n)
a
⊗Λ(n)
a
(3.1.9)
En ajoutant, dans (3.1.9), aux termes à gauche de ⊗’s p −n lignes, (n + 1)-
ième, (n + 2)-ième, ..., p-ième lignes, et à droite p −n colonnes, (n + 1)-ième,
(n + 2)-ième, ..., p-ième colonnes, formées de zeros nous avons
(n,p)
X
(j,l)=(1,1)
E(j,l)T
n×p ⊗E(j,l)
n×p−
(n,p)
X
(j,l)=(1,n+1)
E(j,l)T
n×p ⊗E(j,l)
n×p = 1
nI+
n×p⊗In×p+1
2
n2−1
X
a=1
Λ+
a ⊗Λa
En utilisant la proposition 6 et (3.1.8) nous avons (3.1.7).
Maintenant, nous allons donner quelques proprités des matrices de Gell-
Mann rectangles.
Proposition 30 Pour n, p ∈N, p, n ⩾2, soit (Λa)1≤a≤np−1 un système de
matrices de Gell-Mann n × p. Alors, Tr(Λ+
a Λb) = 2δab.
Proposition 31 Pour n, p ∈N, p ⩾n ⩾2, soit (Λa)1≤a≤np−1 un système
de matrices de Gell-Mann n × p. Alors,
ΛaΛ+
b −ΛbΛ+
a = i
n2−1
X
c=1
fabcΛ(n)
c
où les fabc sont les composantes d’un tenseur totalement antisymétrique, avec
fabc = 0 si au moins un de a, b, c est dans {n2, n2 + 1, ..., np −1}.


## Page 47


3.1. MATRICES DE PERMUTATION TENSORIELLE ET MATRICES DE GELL-MANN 39
Conclusion
Etant inspiré par une façon de construire les matrices de Gell-Mann n×n
à partir des matrices de Gell-Mann (n−1)×(n−1), nous pouvons construire
une base de Cn×p, dont les éléments font la généralisation de l’expression de
Un⊗n en termes de matrices de Gell-Mann n × n à l’expression de Un⊗p.
3.1.3
Exprimer une matrice de permutation tensorielle
p⊗n en termes de matrices de Gell-Mann générali-
sées
Des théorèmes de la sous-section 2.2.3 et des relations sur les matrices
de Gell-Mann généralisées sont dont nous avons besoin pour exprimer une
matrice de permutation tensorielle en termes de matrices de Gell-Mann gé-
néralisées. Dans cette sous-section, nous traitons quelques exemples.
Un⊗3(σ)
1) σ = (1 2 3)
En utilisant le Lemme 21, σ = (1 2)(2 3), et par utilisation de la proposition
22
Un⊗3 ((1 2 3)) = Un⊗3 ((1 2)) · Un⊗3 ((2 3))
(3.1.10)
Nous pouvons vériﬁer facilement que
Un⊗3 ((1 2)) = 1
nIn ⊗In ⊗In + 1
2
n2−1
X
a=1
Λa ⊗Λa ⊗In
et
Un⊗3 ((2 3)) = 1
nIn ⊗In ⊗In + 1
2
n2−1
X
a=1
In ⊗Λa ⊗Λa
Ainsi, (3.1.10) devient
Un⊗3 ((1 2 3)) = 1
n2In ⊗In ⊗In + 1
2n
n2−1
X
a=1
In ⊗Λa ⊗Λa
+ 1
2n
n2−1
X
a=1
Λa ⊗Λa ⊗In + 1
4
n2−1
X
a=1
n2−1
X
b=1
Λa ⊗ΛaΛb ⊗Λb


## Page 48


40CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
D’où, à l’aide de la relation (3.3)
Un⊗3 ((1 2 3)) = 1
n2In ⊗In ⊗In + 1
2n
n2−1
X
a=1
In ⊗Λa ⊗Λa
+ 1
2n
n2−1
X
a=1
Λa ⊗Λa ⊗In + 1
2n
n2−1
X
a=1
Λa ⊗In ⊗Λa
−i
4
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
fabcΛa ⊗Λb ⊗Λc + 1
4
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
dabcΛa ⊗Λb ⊗Λc
(3.1.11)
2) σ = (1 3 2)
A l’aide du Lemme 21, σ = (1 3)(3 2), et de la proposition 18, nous avons
Un⊗3 ((1 3)) = 1
nIn ⊗In ⊗In + 1
2
n2−1
X
a=1
Λa ⊗In ⊗Λa
et par utilisation de la même méthode
Un⊗3 ((1 3 2)) = 1
n2In ⊗In ⊗In + 1
2n
n2−1
X
a=1
In ⊗Λa ⊗Λa
+ 1
2n
n2−1
X
a=1
Λa ⊗Λa ⊗In + 1
2n
n2−1
X
a=1
Λa ⊗In ⊗Λa
+ i
4
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
fabcΛa ⊗Λb ⊗Λc + 1
4
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
dabcΛa ⊗Λb ⊗Λc
La diﬀérence entre Un⊗3 ((1 2 3)) et Un⊗3 ((1 3 2)) est le signe moins devant
le cinquième terme.
Un⊗4(σ), σ = (1 2 3 4)
A l’aide du Lemme 21, σ = (1 2 3)(3 4), de la formule (3.1.11), de la
proposition 22 et des relations (3.3) et (3.4), nous avons


## Page 49


3.1. MATRICES DE PERMUTATION TENSORIELLE ET MATRICES DE GELL-MANN 41
Un⊗4(σ) = 1
n3In ⊗In ⊗In ⊗In +
1
2n2
n2−1
X
a=1
In ⊗Λa ⊗Λa ⊗In +
1
2n2
n2−1
X
a=1
Λa ⊗Λa ⊗In ⊗In
+
1
2n2
n2−1
X
a=1
Λa ⊗In ⊗Λa ⊗In +
1
2n2
n2−1
X
a=1
In ⊗In ⊗Λa ⊗Λa
+
1
2n2
n2−1
X
a=1
In ⊗Λa ⊗In ⊗Λa +
1
2n2
n2−1
X
a=1
Λa ⊗In ⊗In ⊗Λa
+ 1
4n
n2−1
X
a=1
n2−1
X
b=1
Λa ⊗Λa ⊗Λb ⊗Λb + 1
4n
n2−1
X
a=1
n2−1
X
b=1
Λa ⊗Λb ⊗Λb ⊗Λa
−1
4n
n2−1
X
a=1
n2−1
X
b=1
Λa ⊗Λb ⊗Λa ⊗Λb
+ 1
4n
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
dabcIn ⊗Λa ⊗Λb ⊗Λc −i
4n
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
fabcIn ⊗Λa ⊗Λb ⊗Λc
+ 1
4n
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
dabcΛa ⊗In ⊗Λb ⊗Λc −i
4n
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
fabcΛa ⊗In ⊗Λb ⊗Λc
+ 1
4n
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
dabcΛa ⊗Λb ⊗Λc ⊗In −i
4n
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
fabcΛa ⊗Λb ⊗Λc ⊗In
+ 1
4n
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
dabcΛa ⊗Λb ⊗In ⊗Λc −i
4n
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
fabcΛa ⊗Λb ⊗In ⊗Λc
+ 1
8
n2−1
X
a=1
n2−1
X
b=1
n2−1
X
c=1
n2−1
X
e=1
n2−1
X
g=1
(−ifabcdceg + idabcfceg + daecdbgc −dagcdcbe + dabcdceg)
Λa ⊗Λb ⊗Λg ⊗Λe
U2⊗3(σ), σ ∈S3
Maintenant, nous donnons la formule donnant U2⊗3(σ), en termes des
matrices de Pauli, bien attendu. En utilisant la relation (Cf. par exemple
[33])
σlσk = δlkI2 + i
3
X
m=1
εlkmσm


## Page 50


42CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
où εijk est totalement antisymétrique, qui est égal à 1 si (i j k) = (1 2 3),
nous avons
U2⊗3(1 2 3) = 1
4I2 ⊗I2 ⊗I2 + 1
4
3
X
l=1
I2 ⊗σl ⊗σl + 1
4
3
X
l=1
σl ⊗I2 ⊗σl
+ 1
4
3
X
l=1
σl ⊗σl ⊗I2 −i
4
3
X
i=1
3
X
j=1
3
X
k=1
εijkσi ⊗σj ⊗σk
et
U2⊗3(1 3 2) = 1
4I2 ⊗I2 ⊗I2 + 1
4
3
X
l=1
I2 ⊗σl ⊗σl + 1
4
3
X
l=1
σl ⊗I2 ⊗σl
+ 1
4
3
X
l=1
σl ⊗σl ⊗I2 + i
4
3
X
i=1
3
X
j=1
3
X
k=1
εijkσi ⊗σj ⊗σk
Conclusion
Partant du fait qu’une MPT est un produit de matrices de transposition
tensorielle, le théorème 18 et avec l’aide de l’expression d’une MCT en termes
des matrices de Gell-Mann généralisées, nous pouvons exprimer une MPT
comme combinaison linéaire des produits tensoriels des matrices de Gell-
Mann généralisées.
Nous n’avons pas l’intention de chercher une formule générale. Cependant,
nous avons montré que toute MPT peut être exprimé en termes de matrices
de Gell-Mann généralisées et puis l’expression peut être simpliﬁée en utilisant
les relations entre ces matrices.
3.2
MCT ET CHARGES ELECTRIQUES DES
FERMIONS
Les fermions ont les nombres quantiques I3, l’isospin et Y , l’hypercharge.
La charge électrique Q d’un fermion est donnée par la relation de Gell-Mann-
Nishijima
Q = I3 + Y
2
(3.2.1)
Pour les fermions du modèle standard (MS), ces nombres quantiques sont
donnés par le tableau suivant.


## Page 51


3.2. MCT ET CHARGES ELECTRIQUES DES FERMIONS
43
Q
I3
Y
Leptons Neutres
νeL, νµL, ντL
0
1/2
−1
Leptons Chargés
eL, µL, τL
−1
−1/2
−1
eR, µR, τR
−1
0
−2
Quarks u, c, t
ur
L, ub
L, ug
L, cr
L, cb
L, cg
L, tr
L, tb
L, tg
L
2/3
1/2
1/3
ur
R, ub
R, ug
R, cr
R, cb
R, cg
R, tr
R, tb
R, tg
R
2/3
0
4/3
Quarks d, s, b
dr
L, db
L, dg
L, sr
L, sb
L, sg
L, br
L, bb
L, bg
L
−1/3
−1/2
1/3
dr
R, db
R, dg
R, sr
R, sb
R, sg
R, br
R, bb
R, bg
R
−1/3
0
−2/3
Une relation matricielle de Gell-Mann-Nishijima pour huit leptons et
quarks du MS de la même generation a été proposée par [11], dans la formula-
tion dans l’espace des phases. Selon la formule (1.5) il est facile de remarquer
que cette relation matricielle de Gell-Mann-Nishijima peut être exprimée en
termes de U2⊗2. Dans cette section, nous allons écrire cette relation en cer-
taines formes dont une interpétation physique de l’action de MCT U2⊗2 sera
possible. Alors, les valeur propres et les vecteur propres de U2⊗2 prendront
des sens physiques. Dans la sous-section 3.2.3, pour inclure plus de fermions
du MS nous écrirons une formule matricielle donnant les charges électriques
en termes de la MCT 3 ⊗3,
U3⊗3 =














1
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
1
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
1
0
0
0
0
0
0
0
0
0
0
0
1
0
0
0
0
0
0
0
0
0
0
0
1














Alors le sens physique donné aux valeurs propres de la MCT U2⊗2 est main-
tenu. Dans la sous-section 3.2.4, pour inclure tous les fermions du MS nous
écrirons la matrice des charges électriques en termes de MCT U4⊗4. Pour les
calculs nous avons utilisé SCILAB, un logiciel libre pour l’analyse numerique.
3.2.1
Relation de Gell-Mann-Nishijima dans la formu-
lation dans l’espace des phases
Nous reécrivons ici la relation de Gell-Mann-Nishijima, qui donne l’OCE
des huit fermions, deux leptons et six quarks colorés, d’une seule génération


## Page 52


44CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
du MS, par exemple eL, νeL, ur
L, ub
L, ug
L, dr
L, db
L, et dg
L, dans l’approche dans
l’espace des phases [11].
Q = I3 + Y
2
(3.2.2)
oú
I3 = 1
2σ0 ⊗σ0 ⊗σ3
l’opérateur isospin ,
Y =
 
1
3
3
X
i=1
σi ⊗σi
!
⊗σ0
l’opérateur hypercharge.
Nous remarquons que les opérateurs I3 et Y agissent indépendamment
sur le champ de vecteur puisque dans l’expression de I3, σ3 est au côté droit
du produit tensoriel et dans l’expression de Y,
 
1
3
3
X
i=1
σi ⊗σi
!
est au côté
gauche.
3.2.2
Opérateur charges électriques en termes de la MCT
2 ⊗2
Selon la formule (1.5) nous pouvons introduire l’opérateur U2⊗2 dans
l’expression de l’opérateur hypercharge Y, et alors dans l’expression de l’OCE
Q.
Y = 2
3U2⊗2 ⊗σ0 −1
3σ0 ⊗σ0 ⊗σ0
D’où
Q = 1
2σ0 ⊗σ0 ⊗σ3 + 1
3

U2⊗2 ⊗σ0 −1
2σ0 ⊗σ0 ⊗σ0

(3.2.3)
ou
Q = σ0 ⊗σ0 ⊗
σ3
2 + ασ0
6

+ 1
3

U2⊗2 −1 + α
2
σ0 ⊗σ0

⊗σ0
(3.2.4)
avec α un paramètre réel.
Si α = 0, nous avons la relation (3.2.3), c’est-à-dire (3.2.2).


## Page 53


3.2. MCT ET CHARGES ELECTRIQUES DES FERMIONS
45
Si α = −3,
Q = σ0 ⊗σ0 ⊗QL + 1
3 (U2⊗2 + σ0 ⊗σ0) ⊗σ0
(3.2.5)
avec QL =

0
0
0
−1

dont la diagonale est formée par les charges électriques
de νeL et de eL.
Si α = 1,
Q = σ0 ⊗σ0 ⊗QQ + 1
3 (U2⊗2 −σ0 ⊗σ0) ⊗σ0
(3.2.6)
avec QQ =
2/3
0
0
−1/3

dont la diagonale est formée par les charges élec-
triques d’un quark u et d’un quark d.
Les quatre valeurs propres de U2⊗2 sont une fois −1 et trois fois +1.
1
√
2




0
−1
1
0



un vecteur propre de U2⊗2 associé à la valeur propre −1, qui
est, selon (3.2.5), associé aux leptons.




1
0
0
0



,
1
√
2




0
1
1
0



,




0
0
0
1



sont les vecturs propres associés à +1, qui est, selon
(3.2.6), associés aux trois quarks colorés.
La diagonale de QL =

0
0
0
−1

sont formée par les charges de eL et νeL.
La diagonale de QQ =

2/3
0
0
−1/3

sont formée par les charges de quark
u (up) et de quark d (down). Le nombre de valeur propre −1 de U2⊗2 est le
nombre de génération de leptons. +1 trois fois valeur propre de U2⊗2, c’est-
à-dire le nombre de couleurs. D’où, les valeurs propres de Q sont les charges
des huit fermions mentionés ci-dessus.


## Page 54


46CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
3.2.3
Opérateur charges électriques en termes de MCT
3 ⊗3
Soit, par exemple, QL =


0
0
0
0
−1
0
0
0
−1

dont la diagonale est formée par
la charge électrique d’un neutrino et les charges électriques de deux leptons
chargés et QQ =


2/3
0
0
0
−1/3
0
0
0
−1/3

dont la diagonale est formée par la
charge électrique d’un quark u (un quark c (charm) ou d’un quark t (top))
et les charges électriques d’un quarks d, d’un quarks s (strange) ou quarks b
(bottom).
QQ −QL = 2
3λ0
(3.2.7)
où λ0 est la matrice unitaire 3 × 3.
D’où,
λ0⊗λ0⊗QQ+ 1
3(U3⊗3−λ0⊗λ0)⊗λ0 = λ0⊗λ0⊗QL+ 1
3(U3⊗3+λ0⊗λ0)⊗λ0
Nous notons cette expression Q, comme un OCE.
Les valeurs propres de la MCT U3⊗3 sont −1 trois fois et +1 six fois. D’après
l’équation ci-dessus les valeurs propres −1 sont associées aux leptons tandis
que les valeurs propres +1 sont associées aux quarks. Les trois valeurs propres
−1 sont associées aux trois générations de leptons, tandis que les trois valeurs
propres +1 sont associées aux trois couleurs de quarks gauchers et les trois
autres sont associées aux trois couleurs de quarks droitiers. La diagonale de
QL sont formés par les charges des leptons du MS dans une même génération,
par exemple νeL, eL et eR. La diagonale de QQ sont formés par les charges
d’un quark u, d’un quark d et d’un quark s. D’où, les vingt sept valeurs
propres de Q, −1 six fois, 0 trois fois, −1/3 douze fois et +2/3 six fois,
peuvent être les charges des fermions du MS suivants : νeL, νµL, ντL, eL, µL,
τL, eR, µR, τR, ur
L, ub
L, ug
L, ur
R, ub
R, ug
R, dr
L, db
L, dg
L, dr
R, db
R, dg
R, sr
L, sb
L, sg
L, sr
R,
sb
R, sg
R.
QQ = 1
2λ3 +
1
2
√
3λ8
D’après la relation (3.5) pour n = 3, la MCT U3⊗3 peut s’écrire en termes
de matrices de Gell-Mann de la façon suivante
U3⊗3 = 1
3λ0 ⊗λ0 + 1
2
8
X
i=1
λi ⊗λi


## Page 55


3.2. MCT ET CHARGES ELECTRIQUES DES FERMIONS
47
Ainsi,
Q = λ0 ⊗λ0 ⊗

−2
9λ0 + 1
2λ3 +
1
2
√
3λ8

+ 1
6
 
8
X
i=1
λi ⊗λi
!
⊗λ0
Q peut s’écrire sous la forme de la relation (3.2.2), où
I3 = 1
2 (λ0 ⊗λ0 ⊗λ3 −τ1 ⊗τ1 ⊗τ1 −τ2 ⊗τ2 ⊗τ1 −τ3 ⊗τ3 ⊗τ1)
Y = τ1⊗τ1⊗τ1+τ2⊗τ2⊗τ1+τ3⊗τ3⊗τ1+ 1
√
3λ0⊗λ0⊗λ8+2
3 (U3⊗3 −λ0 ⊗λ0)⊗λ0
avec τ1 =


1
0
0
0
0
0
0
0
0

, τ2 =


0
0
0
0
1
0
0
0
0

et τ3 =


0
0
0
0
0
0
0
0
1

.
D’après (2.3), I3 et Y commutent, donc ils sont simultanément diagona-
lisables.
Si nous prenons QL =


0
0
0
0
0
0
0
0
−1

et QQ =


2/3
0
0
0
2/3
0
0
0
−1/3

la
relation ci-dessus entre QL et QQ sera maintenue. Les vingt sept valeurs
propres de l’OCE Q sont −1 trois fois, 0 six fois, −1/3 six fois et +2/3 douze
fois. Ces valeurs propres peuvent être les charges des fermions suivants : νeL,
νµL, ντL, νeR, νµR, ντR, eL, µL, τL, cr
L, cb
L, cg
L, cr
R, cb
R, cg
R, tr
L, tb
L, tg
L, tr
R, tb
R, tg
R,
br
L, bb
L, bg
L, br
R, bb
R, bg
R. Les neutrinos gauchers νeR, νµR, ντR dont la charge est
0 ne sont pas des fermions du MS.
3.2.4
Inclure tous les fermions du modèle standard
Pour inclure tous les fermions du MS, nous allons construire un OCE en
termes de la MCT U4⊗4.
Les valeurs propres de la MCT U4⊗4 sont −1 six fois et +1 dix fois. Donc,
l’OCE
Q = Λ0⊗Λ0⊗QQ+1
3(U4⊗4−Λ0⊗Λ0)⊗Λ0 = Λ0⊗Λ0⊗QL+1
3(U4⊗4+Λ0⊗Λ0)⊗Λ0


## Page 56


48CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
où Λ0 est la matrice unité 4 × 4 et QQ =




−1/3
0
0
0
0
2/3
0
0
0
0
−1/3
0
0
0
0
2/3



, QL =




−1
0
0
0
0
0
0
0
0
0
−1
0
0
0
0
0



. Q a soixante quatre valeurs propres.
La diagonale de QL est formée par les charges des quatre leptons d’une même
génération, par exemple eL, νeL, eR et νeR, tandis que la diagonale de QQ
est formée par les charges d’un quark u, d’un quark d, d’un quark s (ou d’un
quark b) et quark c (ou d’un quark t). Pour la MCT U4⊗4, les quatre valeurs
propres −1 sont associées aux quatre générations de leptons, les trois valeurs
propres +1 et une valeur propre −1, sont respectivement associées aux trois
couleurs de quarks gauchers et le lepton qui forment ensemble un leptoquark
gaucher du modèle de Pati-Salam [43]
ur
L
ub
L
ug
L
νeL
dr
L
db
L
dg
L
eL

=
ur
L
ub
L
ug
L
uw
L
dr
L
db
L
dg
L
dw
L

,
sr
L
sb
L
sg
L
νµL
cr
L
cb
L
cg
L
µL

=
sr
L
sb
L
sg
L
sw
L
cr
L
cb
L
cg
L
cw
L

tandis que les autres trois valeurs propres +1 et une valeur propre −1, sont
respectivement associées aux trois couleurs de quarks droitiers et le lepton
qui forment ensemble un leptoquark droitier du modèle de Pati-Salam

ur
R
ub
R
ug
R
νeR
dr
R
db
R
dg
R
eR

=

ur
R
ub
R
ug
R
uw
R
dr
R
db
R
dg
R
dw
R

,

sr
R
sb
R
sg
R
νµR
cr
R
cb
R
cg
R
µR

=

sr
R
sb
R
sg
R
sw
R
cr
R
cb
R
cg
R
cw
R

Ainsi, selon [44] nous avons considéré les leptons dans les leptoquarks
comme des quarks de couleur blanche.
Finalement, les dernières quatre valeurs propres +1 sont associées aux
quatre couleurs de quarks de la troisième génération, plus un quark de couleur
jaune, à savoir

tr
L
tb
L
tg
L
ty
L
br
L
bb
L
bg
L
by
L

,

tr
R
tb
R
tg
R
ty
R
br
R
bb
R
bg
R
by
R

,
et ça termine la liste des soixante quatre fermions fondamentaux, avec des
neutrinos droitiers y inclus.
Λ1 =




0
1
0
0
1
0
0
0
0
0
0
0
0
0
0
0



, Λ2 =




0
−i
0
0
i
0
0
0
0
0
0
0
0
0
0
0



, Λ3 =




1
0
0
0
0
−1
0
0
0
0
0
0
0
0
0
0



,


## Page 57


3.2. MCT ET CHARGES ELECTRIQUES DES FERMIONS
49
Λ4 =




0
0
1
0
0
0
0
0
1
0
0
0
0
0
0
0



, Λ5 =




0
0
−i
0
0
0
0
0
i
0
0
0
0
0
0
0



, Λ6 =




0
0
0
0
0
0
1
0
0
1
0
0
0
0
0
0



,
Λ7 =




0
0
0
0
0
0
−i
0
0
i
0
0
0
0
0
0



, Λ8 =
1
√
3




1
0
0
0
0
1
0
0
0
0
−2
0
0
0
0
0



Λ9 =




0
0
0
1
0
0
0
0
0
0
0
0
1
0
0
0



,
Λ10 =




0
0
0
−i
0
0
0
0
0
0
0
0
i
0
0
0



, Λ11 =




0
0
0
0
0
0
0
1
0
0
0
0
0
1
0
0



, Λ12 =




0
0
0
0
0
0
0
−i
0
0
0
0
0
i
0
0



,
Λ13 =




0
0
0
0
0
0
0
0
0
0
0
1
0
0
1
0



, Λ14 =




0
0
0
0
0
0
0
0
0
0
0
−i
0
0
i
0



, Λ15 =
1
√
6




1
0
0
0
0
1
0
0
0
0
1
0
0
0
0
−3




sont les matrices de Gell-Mann 4 × 4.
La formule (3.5) pour n = 4,
U4⊗4 = 1
4Λ0 ⊗Λ0 + 1
2
15
X
i=1
Λi ⊗Λi
donne
Q = Λ0⊗Λ0⊗
 
−1
12Λ0 −1
36Λ3 +
√
3
2 Λ8 −
1
6
√
6
Λ15
!
+1
6
 15
X
i=1
Λi ⊗Λi
!
⊗Λ0
Conclusion
Grâce à [11], nous avons un OCE pour deux leptons et six quarks colorés
du MS d’une seule génération. Cet OCE peut être exprimé en termes de la
MCT U2⊗2. Un OCE pour plus de fermions du MS en trois générations a été
obtenu en termes de la MCT U3⊗3.
L’expression de ces OCE, ainsi que celui qui est proposé par [11], peut être
obtenue à partir de la relation (3.2.7) entre les charges électriques des lep-
tons et quarks. Ces expressions permettent de dire que les valeurs propres
−1 d’une MCT sont associées aux leptons tandis que les valeurs propres +1
sont associées aux quarks.
D’après le sens que prend une valeur propre d’une MCT, pour obtenir un
OCE pour tous les fermions du MS en termes de la MCT U4⊗4, nous sommes
obligés d’introduire la quatrième génération de leptons, le modèle de lepto-
quark de Pati-Salam et les quarks de couleur jaune.


## Page 58


50CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES


## Page 59


Conclusion et perspectives
La MCT 2⊗2 nous est apparue lorsque nous avons étudié l’équation de Dirac
et sa modiﬁcation, l’équation de Dirac-Sidharth. Alors, nous avons construit
deux ensembles dont chacun contient six représentations de l’équation de
Dirac. L’un de ces ensembles contient la représentation de Dirac et celle de
Weyl. Ils se transforment l’un en l’autre par application de la MCT 2 ⊗2.
Dans le chapitre 2, nous avons généralisé les MCT aux MPT. Une façon de
décomposer les MPT Up⊗n (σ) en produit avec des matrices de transposition
tensorielle y a été construite. Les MCT peuvent être utilisées pour obtenir
diﬀérentes transformées de certaines équations matricielles en équations ma-
tricielles de la forme AX = B.
La généralisation de la relation (1.5) en termes de matrices de Gell-Mann gé-
néralisées, qui sont des matrices de la physique des particules, et qui consti-
tuent une généralisation des matrices de Pauli, nous permet d’espérer l’utili-
sation des MCT dans ce domaine de la physique. A l’aide de la décomposition
des MPT Up⊗n (σ) en produit avec des matrices de transposition tensorielle,
nous avons aussi obtenu une façon d’exprimer ces MPT en termes des ma-
trices de Gell-Mann généralisées.
Aﬁn de généraliser la relation (1.5) aux MCT Un⊗p, avec n ̸= p, nous avons
introduit ce que nous appelons matrices de Gell-Mann rectangles. L’article
[46] utilise les matrices élémentaires 3×2. Nous nous demandons ce que nous
pourrons obtenir si nous utilisons des matrices de Gell-Mann 3 × 2 au lieu
de matrices élémentaires 3 × 2.
Il existe d’autres généralisations des matrices de Pauli, entre autres les ma-
trices de Kibler [47], les nonions [48] et la généralisation par produits tenso-
riels des matrices de Pauli elles-mêmes [49, 50]. Notre tentative d’exprimer
la MCT 3 ⊗3 en termes de matrices de Kibler et de nonions nous fait penser
qu’il doit y avoir une autre généralisation des matrices de Pauli (Πi)1≤i≤n2−1
satisfaisant
Un⊗n = 1
nΠ0 ⊗Π0 + 1
n
n2−1
X
i=1
Πi ⊗Πi
51


## Page 60


52CHAPITRE 3. VERS UNE APPLICATION EN PHYSIQUE DES PARTICULES
avec Π0 la matrice unité n × n. Pour n = 2p, p entier naturel non nul, cette
relation est satisfaite par la généralisation par produits tensoriels des matrices
de Pauli [51].
Nous avons exprimé l’OCE, pour huit leptons et quarks du MS d’une même
génération, proposé par Zenczykowski dans la formulation dans l’espace des
phases, en termes de la MCT U2⊗2, sous une forme dont des interprètations
physiques seraient possibles. Nous avons remarqué que cet OCE peut être
obtenu à l’aide de la relation (3.2.7) entre les charges des leptons et des
quarks. A l’aide de cette même relation nous avons construit, en termes de la
MCT U4⊗4 un OCE incluant les fermions du MS. Ça nous oblige à introduire
la quatrième génération de leptons, le modèle de leptoquark de Pati-Salam
et les quarks de couleur jaune. Les expressions de ces OCE en termes de
MCT nous permettent de remarquer que les valeurs propres −1 d’une MCT
peuvent être associées aux leptons tandis que les valeurs propres +1 peuvent
être associées aux quarks.


## Page 61


Annexe A
Matrices. Une généralisation
Si les éléments d’une matrice sont considérés comme les composantes d’un
tenseur du second ordre, nous adoptons la notation habituelle pour une ma-
trice, sans crochets à l’intérieur. Tandis que si les éléments sont, par exemple,
considérés comme les composantes d’un tenseur du sixième ordre, trois fois
covariant et trois fois contravariant, alors nous représentons la matrice de la
manière suivante, par exemple
M =





1
0
1
1


1
1
3
2


0
0
0
0


1
1
1
1






1
0
1
2


7
8
9
0


3
4
5
6


9
8
7
6





 1
1
1
1

 0
0
3
2

 4
5
1
6

 1
7
8
9





 5
4
3
2

 1
0
1
2

 3
4
5
6

 7
8
9
0






1
2
3
4


9
8
7
6


5
6
7
8


5
4
3
2






9
8
7
6


5
4
3
2


1
0
1
2


3
4
5
6





(A.0.1)
M =
 Mi1i2i3
j1j2j3

i1i2i3 = 111, 112, 121, 122, 211, 212, 221, 222, 311, 312, 321, 322
indices de ligne
j1j2j3 = 111, 112, 121, 122, 211, 212, 221, 222
indices de colonne
Les premiers indices i1 et j1 sont les indices des crochets extérieurs que nous
appelons crochet du premier ordre ; les deuxième indices i2 et j2 sont les
53


## Page 62


54
ANNEXE A. MATRICES. UNE GÉNÉRALISATION
indices des crochets suivants que nous appelons les crochets du deuxièmes
ordre ; les troisièmes indices i3 et j3 sont les indices des crochets les plus in-
térieurs, de cet exemple, que nous appelons les crochets du troisièmes ordre.
Ainsi, par exemple, M321
121 = 5.
Si nous supprimons les crochets du troisièmes ordre, alors les éléments de
la matrice M sont considérés comme les composantes d’un tenseurs d’ordre
quatre, deux fois contravariant et deux fois covariant.
Considérons un cas plus général, M =
 Mi1i2...ik
j1j2...jk

où les éléments de M
sont considérés comme les composantes d’un tenseur d’ordre 2k, k fois contra-
variant et k fois covariant. Les crochets du premier ordre sont les crochets
d’une matrice n1 × m1 ; les crochets du deuxièmes ordre sont les crochets
d’une matrice n2 × m2 ; · · · ; les crochets du k-ième ordre sont les crochets
d’une matrice nk × mk. M = (γs
t )1 ≤s ≤n1n2...nk, 1 ≤t ≤m1m2...mk si les éléments
de M sont considérés comme les composantes d’un tenseur du second ordre,
une fois contravariant et une covariant. Alors, [45]
s = nk . . . n3n2(i1 −1)+nknk−1 . . . n3(i2 −1)+. . .+nk(ik−1 −1)+ik (A.0.2)
t = mk . . . m3m2(j1−1)+mkmk−1 . . . m3(j2−1)+. . .+mk(jk−1+jk (A.0.3)
Les éléments de la matrice N =
 Nij
k

=


 1
1
1
1


0
1
2
3


4
5
6
7

 8
9
0
1



, avec crochets inté-
rieurs, peut être considérés comme les composantes d’un tenseur d’ordre trois,
deux fois contravariant et une fois covariant. Alors, par exemple, (N12
2 ) = 1.


## Page 63


Annexe B
Produit Tensoriel de matrices
Déﬁnition 32 Considérons A = (Ai
j) ∈Cm×n, B = (Bi
j) ∈Cp×r. La ma-
trice déﬁnie par
A ⊗B =







A1
1B
. . .
A1
jB
. . .
A1
nB
...
...
...
Ai
1B
. . .
Ai
jB
. . .
Ai
nB
...
...
...
Am
1 B
. . .
Am
j B
. . .
Am
n B







obtenue après les multiplications par un scalar, Ai
jB, est appelée le produit
tensoriel de la matrice A par la matrice B.
A ⊗B ∈Cmp×nr
Propriété 33 Le produit tensoriel de matrices est associatif.
Propriété 34 Le produit tensoriel de matrices est distributif par rapport à
l’addition.
Propriété 35 (B1 · A1) ⊗(B2 · A2) = (B1 ⊗B2) · (A1 ⊗A2) pour toutes
matrices B1, A1, B2, B2 si les produits habituels de matrices B1 · A1 et
B2 · A2 sont déﬁnis.
Proposition 36 If A⊗B = O, then A = O or B = O, pour toutes matrices
A, B.
Proposition 37 In ⊗Im = Inm
Proposition 38 Considérons (Ai)1≤i≤n×m une base de Cn×m, (Bj)1≤j≤p×r
une base de Cp×r. Alors, (Ai ⊗Bj)1≤i≤n×m,1≤j≤p×r est une base de Cnp×mr.
55


## Page 64


56
ANNEXE B. PRODUIT TENSORIEL DE MATRICES
Propriété 39 Considérons (Ai)1≤i≤n un système d’éléments de Cp×r, (Bi)1≤i≤n
un système d’éléments de Cl×m, A ∈Cp×r et B ∈Cl×m. Si
A ⊗B =
n
X
i=1
Ai ⊗Bi
(B.0.1)
alors, pour toute matrice K,
A ⊗K ⊗B =
n
X
i=1
Ai ⊗K ⊗Bi
Preuve. Prenons K =
 Kj1
j2

∈Cq×s, Ai =

A
k1
(i)k2

, A =
 Ak1
k2

, Bi =

B
l1
(i)l2

, B =
 Bl1
l2

. Alors, Ak1
k2Kj1
j2 Bl1
l2 = Kj1
j2Ak1
k2Bl1
l2 et
n
X
i=1
A
k1
(i)k2Kj1
j2 B
l1
(i)l2 =
Kj1
j2
n
X
i=1
A
k1
(i)k2B
l1
(i)l2 sont respectivement les éléments de A⊗K ⊗B et
n
X
i=1
Ai⊗
K ⊗Bi sur la k1j1l1-ième ligne, k2j2l2-ième colonne. En utilisant (B.0.1),
Ak1
k2Bl1
l2 =
n
X
i=1
A
k1
(i)k2B
l1
(i)l2. Donc, Ak1
k2Kj1
j2Bl1
l2 =
n
X
i=1
A
k1
(i)k2Kj1
j2B
l1
(i)l2. Ceci est
vraie pour tous indices k1, j1, l1, k2, j2, et l2. D’où, A ⊗K ⊗B =
n
X
i=1
Ai ⊗
K ⊗Bi.


## Page 65


Bibliographie
[1] Lin M.M., On the T-Stein equation X = AXTB+C, arXiv : 1210.5731v1
[2] Zhang L. and Wu J., A Survey of Dynamical Matrices Theory, arXiv :
1009.2210v5
[3] Gilchrist A., Terno D.R. and Wood C.J., Vectorization of Quantum Ope-
rations and its Use, arXiv : 0911.2539v2
[4] Fujii K. : Introduction to Coherent States and Quantum Information
Theory, arXiv : quant-ph/0112090, prepared for 10th Numazu Meeting
on Integral System, Noncommutative Geometry and Quantum theory,
Numazu, Shizuoka, Japan, 7-9 Mai 2002(2002).
[5] Cheﬂes A., Gilson C.R. and Barnett S.M., Entanglement, Information
and Multiparticle Quantum Operations, arXiv : quant-ph/0006106v2
[6] Wilmott C. and Wild P., On Interchanging the States of a Pair of Qudits,
arXiv : 0811.1545v1
[7] Wang R.P., Varieties of Dirac Equation and Flavors of Leptons and
Quarks, arXiv : hep-ph/0107184v2.
[8] Rakotonirina, C. (2003). Produit Tensoriel de Matrices en Théorie de
Dirac, Thèse de Doctorat de Troisième Cycle, Université d’Antanana-
rivo, Antananarivo, Madagascar, (2003).
[9] Zhou B., Lam J. and Duan G-R., Toward Solution of Matrix Equation
X = Af(X)B + C, arXiv : 1211.0346v1
[10] Li N., Wang Q.-W., and Jiang J., An Eﬃcient Algorithm for the Re-
ﬂexive Solution of the Quaternion Matrix Equation AXB+CXHD = F,
Journal of Applied Mathematics, vol. 2013, Article ID 217540, 14 pages,
2013.
[11] Zenczykowski P., Space, Phase Space and Quantum Numbers of Elemen-
tary Particles, Acta Phys. Pol. B 38, 2053 (2007).
[12] Raoelina Andriambololona, Rakotonirina C. A Study of the Dirac-
Sidharth Equation, Electronic Journal of Theoretical Physics, EJTP 8,
No. 25 (2011) 177-182
57


## Page 66


58
BIBLIOGRAPHIE
[13] Einstein, A. On the Electrodynamics of Moving Bodies, Ann. der Phys.
17, 891-921(1905).
[14] Snyder, H.S., The Electromagnetic Field in Quantized Space-Time,
Phys.Rev., Vol.72, No.1, July 1, 68-71(1947).
[15] Snyder, H.S., Quantized Space-time, Phys.Rev., Vol.71, No.1, January
1, 38-41(1947).
[16] Sidharth,
B.G.,
Discrete
Space-Time
and
Lorentz
Symmetry,
Int.J.Th.Phys., Vol.43, No.9, September, 1857-1861(2004).
[17] Glinka, L.A. CP violation, massive neutrinos, and its chiral conden-
sate : new results from Snyder noncommutative geometry. Apeiron 17
(4), 2010, 223-242(2010).
[18] Glinka, L.A. Energy renormalization and integrability within the massive
neutrinos model, Apeiron 17 (4), 243-271(2010).
[19] Glinka, L.A. Æthereal Multiverse : Selected Problems of Lorentz
Symmetry Violation, Quantum Cosmology, and Quantum Gravity,
arXiv :1102.5002v2(2011).
[20] Sidharth, B.G., A Note on Non-commutativity and Mass Generation,
Int.J.Mod.Phys.E., Vol.14, No.6, , 927-929(2005).
[21] Sakurai, J.J., Advanced Quantum Mechanics, Addison Wesley Publi-
shing Company, 308-311(1967).
[22] Bjorken J.D. and Drell S.D., Relativistic Quantum Mechanics, Mc-Graw
Hill, New York, , 39(1964).
[23] Sidharth, B.G. The Mass of the Neutrinos, arXiv : 0904.3639v2(2009).
[24] Messiah A., Mécanique Quantique, Dunod, Paris (1958).
[25] Faddev L.D. :Algebraic Aspects of the Bethe Ansantz, Int.J.Mod.Phys.A,
10, No 13, May, 1848(1995).
[26] Verstraete F. : A Study of Entanglement in Quantum Informa-
tion Theory, Thèse de Doctorat, Katholieke Universiteit Leuven, 90-
93(2002).
[27] Rakotonirina C., Tensor Permutation Matrices in Finite Dimensions,
arXiv : math.GM/0508053 (2005)
[28] Rakotonirina
C.,
Hanitriarivo
Rakotoson,
Expressing
a
Tensor
Permutation
Matrix
p⊗n
in
Terms
of
the
Ge-
neralized
Gell-Mann
Matrices,
HEP-MAD-2007-317,
http ://www.slac.stanford.edu/econf/C0709107/pdf/317.pdf (2007)
[29] Rakotonirina C., On the Cholesky method, Journal of Interdisciplinary
Mathematics, Vol. 12(2009), No.6 , pp. 875-882


## Page 67


BIBLIOGRAPHIE
59
[30] Rakotonirina C., On the Tensor Permutation Matrices, arXiv :
1101.0910 (2011)
[31] Raoelina Andriambololona : Algèbre linéaire et Multilinéaire. Applica-
tions, tome 1, Collection LIRA, Madagascar, (1986).
[32] Merris.R, Multilinear Algebra, Gordon and Breach Sciences Publi-
shers,(1997).
[33] Raoelina Andriambololona, Etude des Matrices Carrées de Dimension
2 et quelques Applications, Ann.Univ.Madagascar, Série Sc. Nature et
Math, No 9, (1972).
[34] Démidovitch B. and Maron I., Eléments de Calcul Numérique. Editions
Mir, (1979).
[35] Nougier J.P., Méthodes de Calcul Numérique. Masson. Paris, (1987).
[36] Kincaid D. and Cheney W., Numerical Mathematics and Computing.
Brooks/Cole Publishing Co., Paciﬁc Grove, CA, fourth edition, (1999).
[37] Steven
E.P.,
Numerical
Methods
Course
Notes.
http ://scicomp.ucsd.edu/ spav/pub/numas.pdf
[38] Ikramov H., Recueil de Problèmes d’Algèbre linéaire, Edition Mir, Mos-
cou, (1977).
[39] Rakotonirina C., Expression of a Tensor Commutation Matrix in Terms
of the Generalized Gell-Mann Matrices, International Journal of Mathe-
matics and Mathematical Sciences, Volume 2007, Article ID 20672
[40] Rakotonirina C., Rectangle Gell-Mann Matrices, International Mathe-
matical Forum, Vol. 6, 2011, no. 2, 57 - 62
[41] Rakotonirina C., Ratiarison A.A., Swap Operators and Electric Charges
of Fermions, International Journal of Theoretical and Applied Physics
(IJTAP), Vol.3, No. I (June 2013), pp. 15-24.
[42] Narison S., Spectral Sum Rules, vol. 26 of World Scientiﬁc Lecture Notes
in Physics, World Scientiﬁc, Singapore, (1989).
[43] Pati J. and Salam A., Lepton Number as the Fourth Color, Phys. Rev.
D10, 275, (1974).
[44] Baez J. and Huerta J., The Algebra of Grand Uniﬁed Theories, Bull.
Am. Math. Soc. 47 (2010) 483-552 arXiv :0904.1556 [hep-th] (2009).
[45] Raoelina Andriambololona, Etude Intrinsèque et Représentation Ma-
tricielle des Produits Kroneckeriens et des Puissances Kroneckeriennes
d’Opérateurs Linéaires - Etude Générale, Ann.Univ.Madagascar, Série
Sc. Nature et Math, No 14, (1977).


## Page 68


60
BIBLIOGRAPHIE
[46] Pushpa, Bisht P. S., Tianjun Li and Negi O. P. S., Quaternion Octonion
Reformulation of Grand Uniﬁed Theories, arXiv : 1205.4617v1, (2012).
[47] Kibler M.R., An angular momentum approach to quadratic Fourier
transform, Hadamard matrices, Gauss sums, mutually unbiased bases,
the unitary group and the Pauli group, J. Phys. A : Math. Theor. 42
353001 (28pp) (2009).
[48] Volkov G., Ternary Quaternions and Ternary TU(3) algebra, arXiv :
1006.5627v1 (2010).
[49] Rigetti C., Mosseri R. and Devoret M., Geometric Approach to Digital
Quantum Information, Quantum Information Processing, Vol. 3, No. 6,
December 2004 (2004)
[50] Saniga M., Planat M. and Pracna P., Projective Ring Line Encompassing
Two-Qubits, hal-00111733, version 5 - 28 Dec 2006, (2006).
[51] Rakotonirina C., Rakotondramavonirina J., Tensor Commutation Ma-
trices and Some Generalizations of the Pauli Matrices, en préparation,
(2013).

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]