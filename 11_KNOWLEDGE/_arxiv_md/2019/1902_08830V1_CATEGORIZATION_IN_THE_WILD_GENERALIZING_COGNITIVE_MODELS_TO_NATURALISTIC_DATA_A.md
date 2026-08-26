---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1902.08830v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1902.08830v1_Categorization_in_the_Wild__Generalizing_Cognitive_Models_to_Naturalistic_Data_a

> Source: 1902.08830v1_Categorization_in_the_Wild__Generalizing_Cognitive_Models_to_Naturalistic_Data_a.pdf

> Pages: 41

---


## Page 1


Categorization in the Wild: Generalizing Cognitive
Models to Naturalistic Data across Languages
Lea Frermanna,∗, Mirella Lapatab
aAmazon CoreAI
bUniversity of Edinburgh
Abstract
Categories such as animal or furniture are acquired at an early age and
play an important role in processing, organizing, and communicating world
knowledge. Categories exist across cultures: they allow to eﬃciently rep-
resent the complexity of the world, and members of a community strongly
agree on their nature, revealing a shared mental representation. Models of
category learning and representation, however, are typically tested on data
from small-scale experiments involving small sets of concepts with artiﬁcially
restricted features; and experiments predominantly involve participants of
selected cultural and socio-economical groups (very often involving western
native speakers of English such as U.S. college students) . This work investi-
gates whether models of categorization generalize (a) to rich and noisy data
approximating the environment humans live in; and (b) across languages and
cultures. We present a Bayesian cognitive model designed to jointly learn cat-
egories and their structured representation from natural language text which
allows us to (a) evaluate performance on a large scale, and (b) apply our
model to a diverse set of languages. We show that meaningful categories
comprising hundreds of concepts and richly structured featural representa-
tions emerge across languages. Our work illustrates the potential of recent
advances in computational modeling and large scale naturalistic datasets for
cognitive science research.
Keywords:
Categorization, Bayesian Modeling, Cognitive Modeling,
Natural Language Processing
∗Corresponding author. Email: uedi@frermann.de
Preprint submitted to Elsevier
February 26, 2019
arXiv:1902.08830v1  [cs.CL]  23 Feb 2019


## Page 2


1. Introduction
Categories such as animal or furniture are fundamental cognitive
building blocks allowing humans to eﬃciently represent and communicate the
complex world around them. Concepts (e.g., dog, table) are grouped into cat-
egories based on shared properties pertaining, for example, to their behavior,
appearance, or function.1 Categorization underlies other cognitive func-
tions such as perception [1, 2] or language [3, 4], and there is evidence that
categories are not only shaped by the world they represent, but also by the
language through which they are communicated [5, 6].
Although mental
categories exist across communities and cultures, their exact manifestations
diﬀer [7, 8, 9, 10]. For example, American English speakers prefer taxonomic
categorizations (e.g., mouse,squirrel) while Chinese speakers tend to prefer
to categorize objects relationally (e.g., tree, squirrel; [8]).
Given their prevalent function in human cognition, the acquisition and
representation of categories has attracted considerable attention in cogni-
tive science, and numerous theories have emerged [11, 12, 13, 14]. Empirical
studies of category acquisition and representation, have been predominantly
based on small-scale laboratory experiments. In a typical experiment, hu-
man subjects are presented with small sets of often artiﬁcial concepts, such
as binary strings [15] or colored shapes [16], with strictly controlled fea-
tures [17, 18, 19]. Hypotheses and principles of human categorization are
established based on the processes and characteristics of the categorizations
produced by the participants.
The distribution of subjects participating
in such studies is often skewed towards members of cultural and socioe-
conomic groups which are prevalent in the environment where the research
is conducted, and typically consists to a large proportion of western, ed-
ucated, wealthy and English-speaking participants often sampled from the
even more speciﬁc population of college students. The demographic and so-
cioeconomic bias has been long recognized, and the question of how this bias
might impact conclusions about human cognition in general [20] and category
learning speciﬁcally is under active debate [10]. Although laboratory studies
are invaluable for understanding categorization phenomena in a controlled
1We denote (superordinate level) categories (such as animal or vehicle) in small
caps; (basic level) concepts (such as cat or car) in italics, and feature types (such as
function or behavior) in true type. Individual features (such as {eats, sits, barks}) are
represented as {lists}.
2


## Page 3


Concept
Natural Language Stimuli
cat
Les chats sont poilus.
Cats are carnivores.
猫有尾巴和爪子。
Die Katze miaut!
dog
.اﻟﻜﻠﺐﻟﺪﻳﻪ اﻟﻔﺮاء
Hunde essen Fleisch.
Les chiens ont des queues.
Look, the dog is playing!
apple
I want to eat an apple.
苹果在树上生长。
¨Apfel sind rot oder gr¨un.
An apple contains seeds
kiwi
Can you cut me a kiwi?
.ﻛﻴﻮﻳﺲﻟﺪﻳﻬﺎﺑﺬور
Kiwis sind innen gr¨un.
Ce kiwi est savoureux.
Figure 1: Illustration of model stimuli for ﬁve languages. Each stimulus contains a mention
of a concept (e.g., cat or apple) in its local linguistic context. Concepts are grouped into
categories (e.g., animal or fruit) based on the similarity of the contexts they occur in.
environment, they are also expensive and time-consuming to conduct, and
consequently problematic to scale.
In this work, we scale the investigation of category learning and repre-
sentation along two axes: (1) the complexity of the learning environment,
and consequently the richness of learnable concept and category represen-
tations, and (2) the diversity of languages and cultures considered in eval-
uation. We present a novel knowledge-lean, cognitively motivated Bayesian
model which learns categories and their structured features jointly from large
natural language text corpora in ﬁve diverse languages: Arabic, Chinese,
English, French, and German. We approximate the learning environment
using large corpora of natural language text. Language has been shown to
redundantly encode much of the non-linguistic information in the natural
environment [21], and to inﬂuence the emergence of categories [5, 6]. Besides
text corpora can cover arbitrarily semantically complex domains, and are
available across languages, providing an ideal test environment for studying
categorization at scale.
Figure 1 illustrates example input to our model, and Figure 2 shows
example categories and associated features as induced by our model from the
English Wikipedia. Following prior work [22, 23], we create language-speciﬁc
sets of stimuli, each consisting of a mention of target concept2 (e.g., apple),
2Throughout this article we user the term concept to refer to Rosch’s [12] basic-level cat-
3


## Page 4


k1 woodpecker hawk
starling swan
chickadee ﬁnch buzzard
goose stork pigeon
k2 eel perch
minnow trout
cod catﬁsh
mackerel salmon
k3 coconut rhubarb
cranberry peach
plum walnut lemon
raisin grape prune
k4 strainer oven
dishwasher blender
ladle pan stove
colander grater
kettle toaster
k5 drum stereo
guitar keyboard
mixer rocker
g1 nest egg male tree
female bird ground
female prey water
g2 white brown dark
color yellow tail
wing colour grey red
g4 century market industry
sugar factory farm
mill product grow trade
g3 population habitat sea
whale seal water
island bird river animal
g5 oil acid seed juice
water product vegetable
fruit vitamin sugar
g6 cake milk cream
sugar chocolate bread
cheese sweet ﬂour eat
g7 system computer device
user signal frequency
network radio software service
g8 guitar rock release
record track music sound
studio recording release
Figure 2: Examples of categories (light red) and feature types (light blue) inferred by BCF
from the English Wikipedia. Connecting lines indicate associations learned between the
category and the respective feature type. For example, category fruit (k3) is associated
with feature types trade (g4) nutrition (g5), and processed food (g6).
within its local linguistic context (e.g., {contains, seeds}; cf., Figure 1). We
consider each stimulus an observation of the concept, i.e., the word referring
to the concept is an instance of the concept itself, and its context words
are a representation of its features. Our model infers categories as groups
of concepts occurring with similar features; and it infers feature types as
groups of features which co-occur with each other. The output of our model
(cf., Figure 2) are categories as clusters of concepts, each associated with a
set of feature types, i.e., thematically coherent groups of features. We train
a separate model on each of our target languages, each time presenting the
model with input stimuli from the relevant language.
Computational models in general, and Bayesian models in particular,
allow to investigate hypotheses about cognitive phenomena by systemati-
cally modifying the learning mechanism or available input while observing
the learning outcome. Bayesian models have been applied to a variety of
cognitive phenomena [24, 25, 26], and category acquisition is no exception.
Following from Anderson’s [15, 27, 28] seminal work, a number of models
have been developed, and tested in their ability to reproduce human behav-
ior in laboratory settings by exposing the models to small sets of controlled
inputs with restricted features. In this work we draw on the full potential of
egories, and the term category to refer to superordinate-level categories. (Superordinate-
level) categories are inferred based on the features observed with observations of (basic-
level) concepts.
4


## Page 5


computational modeling by exposing our models to (a) more complex data
reﬂecting the diversity of contexts in which concepts can be observed; and
(b) a input data in diﬀerent languages, shedding light on the applicability of
computational cognitive models beyond the prevalent English test language.
Categorization tasks in a laboratory environment typically involve stimuli
with a small set of features which are relevant to the categorization target,
eliminating the need to detect features, and discriminate them in their rele-
vance. In the real world, however, concepts are observed in contexts and a
substantial part of acquiring categorical knowledge involves learning which
features are useful to discriminate among concepts. In fact, research has
shown that humans learn features jointly with categories [29, 30] and that
these features are themselves structured so as to represent the diversity and
complexity of the properties exhibited in the world [31, 32, 33]. Our novel
model of category learning presented in this article, jointly learns categories
and their structured features from large sets of informationally rich data.
Our work exempliﬁes the opportunities that arise from computational
models and large data sets for investigating the mechanisms with which con-
ceptual representations emerge, as well as the representations themselves in
a broader context. We simulate the acquisition of categories comprising hun-
dreds of concepts by approximating the learning environment with natural
language text. Language has been shown to redundantly encode much of
the non-linguistic information in the natural environment [21], as well as
human-like biases [34], and to inﬂuence the emergence of categories [5, 6].
Text corpora are a prime example of naturally occurring large-scale data
sets [35, 36, 37]. In analogy to real-world situations, they encapsulate rich,
diverse, and potentially noisy, information. The wide availability of corpora
allows us to train and evaluate cognitive models on data from diverse lan-
guages and cultures.
We test our model on corpora from ﬁve languages,
derived from the online encyclopedia Wikipedia in Arabic, Chinese, French,
English, and German. Wikipedia is a valuable resource for our study be-
cause it (a) discusses concepts and their properties explicitly and can thus
serve as a proxy for the environment speakers of a language are exposed to;
and (b) allows us to construct corpora which are highly comparable in their
content across languages, controlling for eﬀects of genre or style.
We present a series of evaluations investigating the quality of the induced
categories and features. Leveraging a reference comprising hundreds of con-
cepts and more than 30 categories, we demonstrate that our model learns
meaningful categories in all ﬁve target languages.
We furthermore show,
5


## Page 6


through crowd-sourced evaluations involving native speakers of each target
language, that the induced feature types are (a) each thematically coherent
and interpretable; and (b) are associated with categories in comprehensible
ways. We discuss language-speciﬁc idiosyncrasies emerging from the induced
representations.
In the remainder of this article, we ﬁrst review related literature, before
we present a cognitively motivated model for learning categories and their
structured representations from large natural language corpora.
We then
evaluate the quality of the emerging representations, as well as the generaliz-
ability of our model across languages. Note that the primary goal of this work
is not to characterize diﬀerences in categories and features arising from dif-
ferent languages (even though this would be an interesting avenue for future
work). Rather, we aim to demonstrate the utility of large-scale naturalistic
datasets for cognitive modeling, and to verify mechanisms of categorization
known from laboratory studies at scale and across communities.
2. Related Work
In this work we leverage large-scale computational simulations to advance
our understanding of categories and features across languages and cultures.
Our research touches on the representation of categories, concepts, and their
features; the mechanisms with which these are learnt; and the use of com-
putational models and large-scale naturalistic data sets to investigate these
questions.
2.1. Feature Representations of Concepts and Categories
Even though much empirical research glosses over this observation, there
is strong evidence that human conceptual representations are structured (see [38]
for a recent critique and overview of cognitive studies of categorization). Cat-
egories mentally represent the complex structure of the environment. They
allow to make inferences about concepts or categories that go beyond their
perceived similarities capturing abstract and potentially complex properties
(for example, the nutritional value of food items, or the emotional
benefits of pets).
Much research on human categorization is based on
laboratory experiments where subjects are presented with artiﬁcial stimuli
represented by a restricted set of task-relevant features.
Observations of
natural concepts, however, are often noisy or incomplete so that a notion
6


## Page 7


of systematic relations among features might be more important here than
under artiﬁcial conditions in the lab [39].
The existence of structured features has received support through behav-
ioral results from a variety of categorization related tasks, such as typicality
rating [39] or category-based inductive inference [40, 33]. Experimental evi-
dence suggests that categories which on the surface do not seem to contain
a coherent set of members (e.g., the category pets) are represented by an
underlying set of abstract features which explain the coherence of the cate-
gory (e.g., {keeps company, lives in the house}). Varying the types of avail-
able features (e.g., providing functional information in addition to objects’
appearance) leads to diﬀerent categorization behavior both in adults [40]
and children [41, 42], and diﬀerent feature types vary in their predictive value
across categories. For example, 2-4-year old children categorize food items
based on their color, however, toys are classiﬁed based on their shape [43].
The structured nature of category features manifests itself in feature
norms.
Feature norms are verbalized lists of properties that humans as-
sociate with a particular concept [32]. Features collected in norming studies
naturally fall into diﬀerent types such as behavior, appearance or function.
This suggests that structure also emerges from verbalized representations of
concepts and features such as mentions in natural language corpora, used as
stimuli in this work. McRae et al. [32] collected a large set of feature norms
for more than 500 concepts in a multi-year study, and classiﬁed these us-
ing a variety of theoretically motivated schemata, including the feature type
classiﬁcation scheme developed in [44] and [45]. Their work puts forward
the hypothesis that humans perform a “mental simulation” when describ-
ing a concept, scanning the mental image they create as well as situations
associated with that image, and then verbalize it when producing features.
The model we present in this article aims to capture the evidence sum-
marized above, and represent categories as structured sets of features with
varying degrees of association. Category-speciﬁc features are structured into
types which relate to a particular kind of property of a category (e.g., the
behavior of animals). We also capture the observation that features are
deﬁning for diﬀerent categories to a varying degree [46, 47] in terms of
category-feature type associations (e.g., the feature function is highly deﬁn-
ing for (or associated with) the category artifact, but not for the category
animal).
7


## Page 8


2.2. Joint Learning of Categories and their Features
Although the majority of models of categorization assume a ﬁxed set
of features underlying the category acquisition and categorization process,
there is increasing evidence that “[...] a signiﬁcant part of learning a cate-
gory involves learning the features entering its representations.” [30, p. 681].
Experimental evidence suggests that not only do features underly the cat-
egorization process but features themselves are susceptible to change over
time and can be modiﬁed by the categories which emerge. Evidence ranges
from changing featural perception as a result of expert education (e.g., wine
tasters or doctors learning to interpret X-ray images) to neurological evidence
revealing enhanced neural activity in experts when presented with pictures
of their area of expertise (see [48] for an overview).
The inﬂuence of category learning on the perception and use of features
has been studied extensively using visual stimuli of varying degrees of natu-
ralness and familiarity. Experiments with drawings of 2-dimensional line seg-
ments [49] show that participants who were exposed to categorization train-
ing prior to a feature identiﬁcation task identiﬁed the presence of category-
deﬁning features faster than participants without prior training. When asked
to categorize pictures of (systematically manipulated) human faces, partic-
ipants showed higher sensitivity to features relevant for the categorization
task [29, 50].
To the best of our knowledge, we present the ﬁrst computational inves-
tigation in the joint emergence of categories and features from large sets
naturalistic input data.
2.3. Computational Models of Category and Feature Induction
The tasks of category formation and feature learning have been considered
largely independently in the context of computational cognitive modeling.
Bayesian categorization models pioneered by Anderson [15] and recently re-
formalized by Sanborn et al. [51] aim to replicate human behavior in small
scale category acquisition studies, where a ﬁxed set of simple (e.g., binary)
features is assumed. Informative features are pre-deﬁned and available to the
model. The BayesCat model [52] is similar in spirit, but was applied to large-
scale corpora, while investigating incremental learning in the context of child
category acquisition (see also [22] for a non-Bayesian approach). BayesCat
associates sets of features (context words) with categories as a by-product
of the learning process, however these feature sets are independent across
categories and are not optimized during learning.
8


## Page 9


A variety of cognitively motivated Bayesian models have been proposed
for the acquisition of complex domain knowledge. Shafto et al. [53] present
a joint model of category and feature acquisition in the context of cross-
categorization, i.e., the phenomenon that concepts are simultaneously or-
ganized into several categorizations and the particular category (and fea-
tures) that are relevant depend on the context (e.g., concepts of the category
food can be organized based on their nutritional or perceptual prop-
erties). However, while [53] present their model with category-speciﬁc data
sets tailored towards their learning objective, we are interested in acquir-
ing categories and structured associated features jointly from thematically
unconstrained corpora of natural text.
Another line of work [54, 55] models the joint learning of relevant features
and domain-speciﬁc feature type biases in children. They focus on the ac-
quisition of domain-speciﬁc representational structures (such as hierarchies
or clusters) and discuss results in the context of word learning.
In con-
trast to our work, their model assumes a priori established categories (such
as food and animals), and learns from task-speciﬁc data representations
in the form of objects described by a limited set of relevant features (even
though a weighting of those features is learnt). Perfors et al. [56] present a
Bayesian model which simultaneously learns categories (i.e., groupings of con-
cepts based on shared features) and learns to learn categories (i.e., abstract
knowledge about kinds of featural regularities that characterize a category).
They compare their model predictions against behavioral data from adult
participants, which limits the scope of their experiments to small data sets.
The ability to automatically extract feature-like information for concepts
from text would facilitate the laborious process of feature norming, i.e., elic-
iting features associated with concepts verbally from human annotators [32],
and improve the coverage of concepts and their features. A few approaches to
feature learning from textual corpora exist, and they have primarily focused
on emulating or complementing norming studies by automatically extract-
ing norm-like properties from corpora (e.g., elephant has-trunk, scissors
used-for-cutting). Steyvers [57] uses a ﬂavor of topic models to augment
data sets of human-produced feature norms. While vanilla topic models [58]
represent documents as sets of corpus-induced topics, [57] additionally use
topics derived from feature norms. The learnt topics yield useful extensions
of the original feature norms, with properties that were previously not cov-
ered, suggesting that corpora are an appropriate resource for augmenting
feature norms of concepts.
9


## Page 10


Another line of research concerns text-based feature extraction. A com-
mon theme in this line of work is the use of pre-deﬁned syntactic patterns
[59], or manually created rules specifying possible connection paths of con-
cepts to features in dependency trees [60, 61]. While the set of syntactic
patterns pre-deﬁnes the relation types the system can capture, the latter ap-
proach can extract features which are a priori unlimited in their relation to
the target concept. Once extracted, the features are typically weighted using
statistical measures of association in order to ﬁlter out noisy instances. Sim-
ilar to our own work, the motivation underlying these models is large-scale
unsupervised feature extraction from text. These systems are not cognitively
motivated acquisition models, however, due to (a) the assumption of involved
prior knowledge (such as syntactic parses or manually deﬁned patterns), and
(b) the two stage extraction-and-ﬁltering process which they adopt. Humans
arguably do not ﬁrst learn a large set of potential features for concepts, be-
fore they infer their relevance. The systems discussed above learn features
for individual concepts rather than categories.
To our knowledge, we propose the ﬁrst Bayesian model that jointly learns
categories and their features from large sets of naturalistic input data. Our
model is knowledge-lean, it learns from raw text in a single process, with-
out relying on parsing resources, manually crafted rule patterns, or post-
processing steps; it is more plausible from a cognitive point of view, and
language agnostic. We present simulations with the same model on several
languages varying in word order, morphology, and phonology.
3. Category and Feature Learning at Scale
Computational models as simulators of cognitive processes have been used
successfully to shed light on a wide variety of phenomena [25], including lan-
guage acquisition [28], generalization, and reasoning [62]. Bayesian models
in particular are amenable towards this goal, because they allow the mod-
eler to formalize hypotheses rigorously through sets of random variables and
their relations. They use the principled rules of Bayesian probability to select
“good” models which explain the observed data well. We present a Bayesian
model to investigate cognitive processes of categorization, in correspondence
to Marr’s [63] computational level of analysis, i.e., abstracting away from
the algorithms and biological substrates in which these processes are sit-
uated. Starting from Anderson’s [15] pioneering work on rational models
of categorization, a variety of models, both Bayesian [51, 53, 23] and non-
10


## Page 11


Bayesian [19, 22] have been proposed. Our work advances prior research by
investigating for the ﬁrst time joint category and feature learning from noisy
stimuli, across diverse languages.
We present BCF, a cognitively motivated Bayesian model for learning
Categories and structured Features from large sets of concept mentions and
their linguistic contexts (see Figure 1). Our model induces categories (as
groups of concepts), feature types which are shared across categories (as
groups of features or context words), and category-feature type associations.
Figure 2 shows example output of BCF as learnt from the English Wikipedia,
and Figure 4 shows example categories and features learnt for ﬁve additional
languages.
BCF is a statistical Bayesian model. Given a large set of stimuli, it learns
meaningful categories and features from a countably inﬁnite set of all possible
categorizations and representations. The probability (or ‘meaningfulness’) of
any hypothetical categorization and representation h under the stimuli data
d can be evaluated using Bayes’ rule:
p(h|d) ∝p(d|h)p(h),
(1)
where p(h) is the prior probability of h under the speciﬁed model and its as-
sumptions; and p(d|h) is the likelihood to observe data d given that hypothesis
h holds.
3.1. The BCF Model
BCF learns from an input corpus which consists of stimuli covering L
target concepts, where the set of target concepts is speciﬁed by the modeler
a priori. The model induces a categorization of these target concepts into
K categories; as well as a characterization of each category in terms of G dif-
ferent feature types pertaining to diﬀerent relevant properties. The number
of categories, K, and the number of feature types, G, are model parameters.
A notational overview is provided in Table 1. The generative story of
our model is displayed in Figure 3a, and Figure 3b shows the plate dia-
gram representation of BCF. The generative story proceeds as follows. We
assume a global multinomial distribution over categories Mult(θ). Its pa-
rameter vector θ is drawn from a symmetric Dirichlet distribution with hy-
perparameter α. For each target concept ℓ= [1...L], we draw a category kℓ
from Mult(θ). For each category k, we draw an independent set of multi-
nomial parameters over feature types, µk, from a symmetric Dirichlet dis-
tribution with hyperparameter β, reﬂecting the relative relevance of each
11


## Page 12


(a) Generative story of BCF.
Generate category distribution,
θ ∼Dir(α)
for concept type ℓ= 1..L do
Generate category,
kℓ∼Mult(θ)
for category k = 1..K do
Generate feature type distribution,
µk ∼Dir(β)
for feature type g = 1..G do
Generate feature distribution,
φg ∼Dir(γ)
for stimulus d = 1..D do
Observe concept cd and retrieve category kcd
Generate a feature type,
gd ∼Mult(µkcd)
for feature position i = 1..I do
Generate a feature
fd,i ∼Mult(φgd)
(b) Plate diagram of BCF.
g
c
f
kℓ
θ
α
µk
β
φ
γ
I
D
L
K
G
Figure 3: Top (a): The generative story of the BCF model. Observations f and latent
labels k and g are drawn from Multinomial distributions (Mult).
Parameters for the
multinomial distributions are drawn from Dirichlet distributions (Dir). Bottom (b): The
plate diagram of the BCF model. Shaded nodes indicate observed variables, clear nodes
denote latent variables, and dashed nodes indicate constant hyperparameters.
12


## Page 13


symbol
explanation
d ∈{1..D}
stimulus
(e.g., “This dog likes to catch balls.”)
c ∈{1..C}
concept mention in stimulus (e.g., “dog”)
i ∈{1..I}
context word positions in stimulus
ℓ∈{1..L}
concept types
(e.g., cat, dog, chair, table)
f ∈{1..V }
features
(e.g., {runs, barks, eats, red, made of wood})
k ∈{1..K}
categories
(e.g., animal, furniture)
g ∈{1..G}
feature types
(e.g., behavior, appearance)
θ
K-dimensional parameter vector of category distribution
{µk}K
k=1
G-dimensional parameter vectors of feature type distributions
{φg}G
g=1
V -dimensional parameter vectors of word distributions
Table 1: Notational overview of the BCF model (the category and feature type labels are
provided for illustration; BCF is an unsupervised clustering model which induces unlabeled
categories and feature types).
feature type towards this category. Finally, we associate each feature type
with representative words from our feature vocabulary f ∈1...V , by draw-
ing a multinomial distribution over features, Mult(φg), from a symmetric
Dirichlet distribution with hyperparameter γ. From this set of global rep-
resentations, we can generate sets of stimuli d = [1...D] as follows: we ﬁrst
retrieve the category kcd of an observed concept cd; we then generate a fea-
ture type gd from the category’s feature type distribution Mult(µkcd); and
ﬁnally, for each context position i = [1...I] we generate feature fd,i from the
feature type-speciﬁc feature distribution Mult(φgd).
According to the generative story outlined above, the joint probability
of the model over latent categories, latent feature types, model parameters,
and data factorizes as:
p(g, f, µ, φ, θ, k|c, α, β, γ) =
p(θ|α)
Y
ℓ
p(kℓ|θ)
Y
k
p(µk|β)
Y
g
p(φg|γ)
Y
d
p(gd|µkcd)
Y
i
p(f d,i|φgd).
(2)
Since we use conjugate priors throughout, we can integrate out the model
parameters analytically, and perform inference only over the latent variables,
namely the category and feature type labels associated with the stimuli.
In sum, our model takes as input a text corpus of concept mentions
in their local context, and infers a concept categorization, a global set of
13


## Page 14


Algorithm 1 The Gibbs sampling algorithm for the BCF model.
1: Input: model with randomly initialized parameters.
2: Output: posterior estimate of θ, φ, and µ.
3: repeat
4:
for stimulus d do
▷Sample stimulus-feature type assignments
5:
- decrement stimulus d-related counts
6:
- Sample
gd ∼p(gd
kcd = i|g−d
kcd, f −, kcd, β, γ)
Equation (5)
7:
- update stimulus d-related counts
8:
for concept c do
▷Sample concept-category assignments
9:
- retrieve category kc
10:
- decrement concept c-related counts
11:
- Sample
kc ∼p(kℓ= j|gkℓ, k−, α, β)
Equation (7)
12:
- update concept c-related counts
13: until convergence
feature types, as well as a distribution over feature types per category. After
integrating out model parameters where possible, we infer two sets of latent
variables:
(1) feature type-assignments to each stimulus {g}D,
(2) category-assignments to each concept type {k}L.
The next section introduces a learning algorithm in the form of a Gibbs
sampler for approximate estimation of these parameters.
3.2. Approximate Inference for BCF
Exact inference in the BCF model is intractable, so we turn to approxi-
mate posterior inference to discover the distribution over value assignments
to latent variables given the observed data.
In this section we introduce
a Gibbs sampling algorithm [64, 65] which is a Markov chain Monte Carlo
algorithm which iteratively computes values of individual random variables
in the model, based on the current value assignments of all other random
variables. The sampling procedure for BCF is summarized in Algorithm 1.
The Gibbs sampler repeatedly iterates over the training corpus and resam-
ples values of the latent variables. One Gibbs iteration for our model consists
of two blocks:
14


## Page 15


Resampling stimulus-feature type assignments. In the ﬁrst block we iterate
over input stimuli d, and resample each stimulus-feature type assignment gd
from its full conditional posterior distribution over feature types conditioned
on (a) the values assigned to all other latent variables unrelated to the current
variable of interest, i.e, all features except those in stimulus d,
 f −
, and
all stimulus-feature type assignments except the one to stimulus d,
 g−d
kcd

;
(b) the category currently assigned to d’s target concept c,
 kcd
; and (c) the
relevant hyperparameters
 β, γ

:
p(gd
kcd = i
|
g−d
kcd, f −, kcd = j, β, γ)
(3)
=
p(gd
kcd = i|g−d
kcd, kcd = j, β) ×
p(f d|f −, gd
kcd = i, γ) (4)
∝
(nj
i + β)
(P
i nj
i + β)
×
Q
v
Qfv
a=1(ni
v + γ + a)
Qf∗
a=1(P
v ni
v + γ + a)
.
(5)
The factorization of the posterior distribution in (4) follows from the model
structure as described above and shown in the plate diagram in Figure 3b.
The posterior distribution factorizes into the probability of a particular fea-
ture type i and the probability of the observed features in the stimulus given
that feature type. Because of the Dirichlet-Multinomial conjugacy in our
model, these two distributions can be straightforwardly computed using only
the counts of current value-assignments to all variables in the model except
the ones currently resampled (equation (5)): the probability of a hypothetical
feature type i is proportional to the number of times it has assigned previ-
ously to stimuli with observed category j, nj
i, smoothed by the Dirichlet
parameter β.
Similarly, the probability of the observed features of stim-
ulus d under hypothetical feature type i is proportional to the number of
times each individual feature v in d has been observed under feature type i,
ni
v (smoothed by the Dirichlet parameter γ). In the second term in (5), fv
refers to the count of any particular feature v in stimulus d, and f∗refers to
the number of features in d (irrespective of their value).
We compute the (unnormalized) probabilities of individual hypothetical
feature types i as explained above. These values are then normalized and a
new feature type is sampled from the resulting distribution.
Resampling concept-category assignments. The second block of our Gibbs
sampler performs a sweep over all concept types ℓ∈{1...L}, and resamples
15


## Page 16


each concept type ℓ’s category assignment kℓ. Similarly to the process de-
scribed above, the new category assignment of concept ℓis resampled from
its full conditional distribution over categories conditioned on (a) all concept-
category assignments except for kℓ,
 k−
; (b) the feature type assignments
relevant to concept ℓ,
 g−
kℓ

; and (c) all relevant hyperparameters
 α, β

:
p(kℓ= j|g−
kℓ, k−, α, β)
=
p(kℓ= j|k−, α) ×
p(gkℓ|g−
kℓ, kℓ= j, β) (6)
∝
(nj + α) ×
Q
g
Qfℓ
g
a=1(nj
g + β + a)
Qfℓ∗
a=1(P
g nj
g + β + a)
.
(7)
Based on the independence assumptions in our model, this probability factor-
izes into the prior probability of hypothetical category j and the probability
of feature types observed with concept ℓunder the hypothetical category j
(equation (6)). As above, these probabilities can be computed purely based
on counts of variable-assignments in the current sampler state (equation (7)).
In the second term of (7), f ℓ
g refers to the number of times feature type g
was assigned to a stimulus containing concept type ℓ, and f ℓ
∗to the number
of stimuli containing ℓ(irrespective of the assigned feature type).
Using the procedure described above we compute an (unnormalized) prob-
ability for each hypothetical category, normalize the probabilities and resam-
ple concept ℓ’s category kℓfrom the resulting distribution.
4. Experimental Setup
Can we simulate category acquisition from large amounts of textual data
using cognitively motivated computational models, and infer meaningful rep-
resentations across languages?
We approach this question by applying BCF to data sets in ﬁve languages:
English, French, German, Arabic, and Chinese. We train ﬁve models in total,
one per language, each time using stimuli from the respective language alone.
We evaluate induced categories by comparison against a human-created refer-
ence categorization; and collect judgments on the coherence of learnt feature
types, and their relevance to their associated categories from large crowds of
native speakers.
Is the structure and architecture of BCF appropriate and necessary for
category and structured feature learning? We answer this question by com-
paring BCF against a variety of related models. First, we report a random
16


## Page 17


en
ar
ch
fr
ge
concepts
491
394
450
484
482
features
5,898
5,870
6,516
6,416
6,981
stimuli
418,755
86,908
147,386
258,499
233,175
Table 2: Datasets obtained from language-speciﬁc Wikipedia dumps for Arabic (ar), Chi-
nese (ch), English, (en), French (fr), and German (ge). Number of stimuli (concept men-
tions in linguistic context), concepts, and features (context word types) are shown.
baseline which assigns concepts to categories at random. Secondly, we com-
pare against a model entirely based on word co-occurrence. Unlike BCF, the
co-occurrence model cannot learn categories and features jointly, and has no
notion of feature structure. It uses k-means clustering [66] to group con-
cepts into categories, and, subsequently, group features into feature types for
each category (see Section 4.2). Finally, we compare BCF against BayesCat,
a cognitively motivated Bayesian model of category acquisition [23]. Like
BCF, it draws inspiration from topic modeling, however, BayesCat does not
learn categories and features jointly, and does not acquire structured feature
representations.
In the following we describe our data set, as well as the set of models we
compare BCF against. Next, we present a series of simulations evaluating
the quality of the induced categories, their features, and their relevance to
the associated categories.
4.1. Experimental Stimuli
Our simulations focused on 491 basic-level concepts of living and non-
living things, taken from two previous studies of concept representation [32,
67], for which we learn (a) a categorization and (b) structured feature repre-
sentations. Human-created gold standard categorizations of the concepts into
33 categories are available [67, 68]. Since the original studies were conducted
in English, we collected translations of the target concepts and their cate-
gories into Arabic, Chinese, French, and German, created by native speakers
of the target language.
The ﬁnal number of concepts diﬀers across lan-
guages, because some English concepts do not exist (or do not have the same
translation) in the target language. Concept sets and categorizations for all
languages were made available as part of this submission.
We created language speciﬁc sets of input stimuli (as illustrated in Fig-
17


## Page 18


ure 1). For each target language we created a corpus as follows: We used a
subset of articles from the Linguatools Wikipedia dump3; we tokenized, POS-
tagged and lemmatized the corpus, and removed stopwords using language-
speciﬁc lists. From this data set we derived a set of input stimuli as mentions
of a concept from the reference set of concepts in sentence context (cf., Fig-
ure 1). In order to obtain balanced data sets, we automatically ﬁltered words
of low importance to a concept from contexts, using the term-frequency-
inverse-document-frequency (tf-idf) metric.
After ﬁltering, we only kept
stimuli with 3 ≤n ≤20 context words and at most 1,000 stimuli per target
concept. Table 2 summarizes the statistics of the resulting data sets. The
number of stimuli varies across languages as a function of the number of
target concepts, and the size of the respective Wikipedia corpus.
4.2. Comparison Models
We compared BCF against various models explained below. All experi-
ments follow the same experimental protocol, i.e., we train separate instances
of the same model on each language.
Strudel. Following a pattern-based approach, Strudel automatically extracts
features for concepts from text collections. It takes as input a part of speech-
tagged corpus, a set of target concepts and a set of 15 hand-crafted rules.
Rules encode general, but quite sophisticated linguistic patterns which plau-
sibly connect nouns to descriptive attributes (e.g., extract an adjective as a
property of a target concept mention if the adjective follows the mention,
and the set of tokens in between contain some form of the verb ‘to be’. [69]).
Strudel obtains a large set of concept-feature pairs by scanning the context
of every occurrence of a target concept in the input corpus, and extracting
context words that are linked to the target concept by one of the rules. Each
concept-feature pair is subsequently weighted with a log-likelihood ratio ex-
pressing the pair’s strength of association. Baroni et al. [59] show that the
learnt representations can be used as a basis for various tasks such as typical-
ity rating, categorization, or clustering of features into types. We obtained
Strudel representations from the same Wikipedia corpora used for extract-
ing the input stimuli for BCF and BayesCat. Note that Strudel, unlike the
two Bayesian models, is not a cognitively motivated acquisition model, but
3http://linguatools.org/tools/corpora/wikipedia-monolingual-corpora/
18


## Page 19


a system optimized with the aim of obtaining the best possible features from
data.
Co-occurrence Baseline. Strudel relies on manually constructed linguistic
patterns, and is consequently not directly applicable across languages. We
report a baseline which is constructed to resemble Strudel, but does not
rely on linguistic features. It allows us to assess whether pure co-occurrence
counts provide a strong enough learning signal for category and feature in-
duction across languages. This model represents each concept c as a vector
with dimensions corresponding to its co-occurrence counts with features f
(i.e., context words), capped by a minimum number of required observations,
approximating the concept-feature association:
assoc(c, f) = N(c, f).
(8)
We obtained categories by clustering concepts based on their vector represen-
tations using k-means clustering [70]. Based on these categories, we obtained
feature types by (1) collecting all features associated with at least half the
concepts in the category; and (2) clustering these features into feature types
using k-means clustering.
BayesCat. Similar to BCF, BayesCat is a knowledge-lean acquisition model
which can be straightforwardly applied to input from diﬀerent languages.
It induces categories z which are represented through a distribution over
target concepts c, p(c|z), and a distribution over features f (i.e., individual
context words), p(f|z). BayesCat, like BCF, is a Bayesian model and its
parameters are inferred using approximate MCMC inference, in the form of
a Gibbs sampler. Unlike BCF, however, BayesCat does not induce struc-
tured feature representations, and comparing it to BCF allows us to evalu-
ate the advantage of joint category and feature learning. BayesCat induces
categories represented through unstructured bags-of-features. As such, the
model structure of BayesCat is closely related to topic models such as Latent
Dirichlet Allocation (LDA; [58]). Comparing our proposed model against
BayesCat allows us to shed light on the beneﬁt of more sophisticated model
structure which allows to learn features jointly with categories, compared to
the information that can be captured in vanilla topic models. For our human
evaluation in Section 7 we construct feature types from BayesCat features
as follows. First we represent each feature f as its probability under each
19


## Page 20


category p(z|f). Based on this representation, we again employ k-means clus-
tering to group features into G global feature types g. Finally, we compute
category-featuretype associations as:
p(g|z) =
X
f∈g
p(f|z),
(9)
where p(f|z) is learnt by BayesCat.
While BCF induces a hard assignment of concepts to categories, BayesCat
learns a soft categorization. Soft assignments can be converted into hard
assignments by assigning each concept c to its most probable category z,
z(c) = max
z
p(c|z)p(z|c).
(10)
Model Parameters. Across all simulations we trained BCF to induce K = 40
categories and G = 50 feature types which are shared across categories. We
ran the Gibbs sampler for 1,000 iterations, and report the ﬁnal most likely
representation. We trained BayesCat on the same input stimuli as BCF,
with the following parameters: the number of categories was set to K = 40,
and the hyperparameters to α = 0.7, β = 0.1, and γ = 0.1. From the learnt
representations, we induced G = 50 global feature types as described above.
Again results are reported as averages over 10 runs of 1,000 iterations of the
Gibbs sampler. The co-occurrence model induces K = 40 categories, and,
subsequently, G = 5 feature types for each category.
5. Experiment 1: Category Quality
In this simulation, We evaluate the extent to which model-induced cat-
egories resemble the human created reference categorization. We report re-
sults on cluster quality for BCF, BayesCat, and the frequency baseline for
our ﬁve target languages.
For English, we additionally report results for
Strudel. We also lower-bound the performance of all models with a random
clustering baseline (random), which randomly assigns all concepts to K = 40
categories.
5.1. Method
The output clusters of an unsupervised learner do not have a natural
interpretation. Cluster evaluation in this case involves mapping the induced
clusters to a gold standard and measuring to what extent the two clusterings
20


## Page 21


(induced and gold) agree [71]. Purity (pu) measures the extent to which
each induced category contains concepts that share the same gold category.
Let Gj denote the set of concepts belonging to the j-th gold category and Ci
the set of concepts belonging to the i-th cluster. Purity is calculated as the
member overlap between an induced category and its mapped gold category.
The scores are aggregated across all induced categories i, and normalized by
the total number of category members N:
pu = 1
N
X
i
max
j
|Ci ∩Gj|
(11)
Inversely, collocation (co) measures the extent to which all members of a
gold category are present in an induced category. For each gold category
we determine the induced category with the highest concept overlap and
then compute the number of shared concepts. Overlap scores are aggregated
over all gold categories j, and normalized by the total number of category
members N:
co = 1
N
X
j
max
i
|Ci ∩Gj|
(12)
Finally, the harmonic mean of purity and collocation can be used to report a
single measure of clustering quality. If β is greater than 1, purity is weighted
more strongly in the calculation, if β is less than 1, collocation is weighted
more strongly:
Fβ = (1 + β) · pu · co
(β · pu) + co
(13)
We additionally report results in terms of V-Measure (VM, [72]) which is an
information-theoretic measure. VM is analogous to F-measure, in that it is
deﬁned as the weighted harmonic mean of two values, homogeneity (VH, the
precision analogue) and completeness (VC, the recall analogue):
VH
=
1 −H(G|C)
H(G)
(14)
VC
=
1 −H(C|G)
H(C)
(15)
VM
=
1 −(1 + β) · V H · V C
(β · V H) + V C
(16)
21


## Page 22


where H(·) is the entropy function; H(C|G) denotes the conditional entropy
of the induced class C given the gold standard class G and quantiﬁes the
amount of additional information contained in C with respect to G. The var-
ious entropy values involve the estimation of the joint probability of classes C
and G:
ˆp(C, G) = µ(C ∩G)
N
(17)
5.2. Results
model
PCF1
V-Measure
pu
co
F1
VH
VC
VM
English
BCF
0.552
0.432
0.484
0.652
0.598
0.623
BayesCat
0.551
0.429
0.482
0.646
0.577
0.609
Strudel
0.572
0.442
0.499
0.662
0.590
0.624
co-occ
0.550
0.394
0.459
0.626
0.559
0.591
random
0.193
0.135
0.159
0.317
0.282
0.298
German
BCF
0.454
0.400
0.425
0.545
0.523
0.534
BayesCat
0.458
0.378
0.414
0.563
0.513
0.537
co-occ
0.338
0.387
0.361
0.408
0.435
0.421
random
0.194
0.134
0.158
0.316
0.280
0.297
French
BCF
0.534
0.441
0.483
0.632
0.585
0.608
BayesCat
0.507
0.415
0.457
0.609
0.558
0.582
co-occ
0.459
0.365
0.407
0.544
0.509
0.526
random
0.197
0.134
0.160
0.319
0.283
0.300
Chinese
BCF
0.441
0.349
0.389
0.510
0.497
0.503
BayesCat
0.430
0.320
0.367
0.532
0.493
0.512
co-occ
0.367
0.327
0.345
0.408
0.422
0.415
random
0.208
0.135
0.164
0.325
0.291
0.307
Arabic
BCF
0.408
0.327
0.363
0.444
0.446
0.445
BayesCat
0.394
0.298
0.339
0.491
0.462
0.476
co-occ
0.261
0.308
0.283
0.312
0.344
0.327
random
0.214
0.125
0.158
0.329
0.296
0.312
Table 3: Quality of induced categories for BCF (this work), BayesCat, a co-occurrence
baseline, Strudel (for English only), and a random baseline.
Results are reported for
English, German, French, Chinese and Arabic.
22


## Page 23


Table 3 displays the results for all ﬁve languages. BCF learns categories
which most closely resemble the human gold standard, and both BCF and the
co-occurrence model clearly outperform the random baseline. The Bayesian
models, BCF and BayesCat, outperform the co-occurrence model across met-
rics and languages. For English, Strudel slightly outperforms BCF. Note,
however, that, BCF learns the categories from data, whereas for Strudel we
construct the categories post-hoc after a highly informed feature extraction
process (relying on syntactic patterns). It is therefore not surprising that
Strudel performs well, and it is encouraging to see that BCF learns cate-
gories of comparable quality.
We observe a slight drop in performance for languages other than English
which is likely due to smaller stimuli sets (see Table 2). BCF, nevertheless,
achieves purity scores of 0.4 or higher for all languages, meaning that on
average at least 40% of the members of a gold standard category are clus-
tered together by BCF (purity rises to 58% for English). This indicates that
meaningful categories emerge throughout. Qualitative model output shown
in Figures 2 (English) and 4 (all languages) corroborates this result. The
categories shown are intuitively meaningful; in particular vegetable and
clothing (Figure 4) are interpretable, and thematically consistent across
languages.
A few interesting idiosyncrasies emerge from our cross-lingual experimen-
tal setup, and the ambiguities inherent in language. For example, the En-
glish concepts tongue and bookcase were translated into French words langue
and biblioth`eque, respectively. The French BCF model induced a category
consisting of only these two concepts with highly associated feature types
{story, author, publish, work, novel} and {meaning, language, Latin, Ger-
man, form}. Although this category does not exist in the gold standard, it is
arguably a plausible inference. Another example concerns the concept barrel,
which in the English BCF output, is grouped together with concepts cannon,
bayonet, bomb and features like {kill, ﬁre, attack}. In French, on the other
hand, it is grouped with stove, oven and the features {oil, production, ton,
gas}.
We showed that BCF learns meaningful categories across languages which
are quantitatively better than those inferred by a simpler co-occurrence
model. Although generally consistent, categories are sometimes inﬂuenced
by characteristics of the respective training and test language. While the lit-
erature conﬁrms an inﬂuence of language on categorization [5, 6], this eﬀect
is undoubtedly ampliﬁed through our experimental framework.
23


## Page 24


krawatte gesicht
olive halstuch
mantel nachthemd
bluse puppe hemd
pelz jacke robe
kleid kappe schal
tie face olive
scarf coat
nightgown
blouse doll shirt
fur jacket robe
gown cap scarf
schwarz rot hose
hemd lang frauen
kleidung rock weiße
black red pants
shirt long women
clothing skirt white
frau lassen se-
hen haus nehmen
fahren bringen vater
woman leave see
house take drive
bring father
ﬁlm sehen erscheinen
geschichte bild lassen
nennen buch frau „die
movie see appear
story image leave call
book woman ”the
schwarz gefärbt hell
weeißen braun kehle
kopf rot gelb grau
black colored bright
white brown throat
head red yellow gray
lassen bringen
nehmen könig frau
töten ziehen fangen
leave bring take
king woman
kill pull catch
blouse slipper jacket shawl dress
vest swimsuit jean nightgown
cloak skirt hat gown leotard
woman dress white
shirt skirt hat jacket
clothing style red
white blue shirt uni-
form red green school
color dress dark
video scene music
show woman girl
dance stage sit dress
kill king power life
woman god magic
steal lose transform
kill home house car
woman door room
mother family steal
chemise-de-nuit
jupe pantalon
pantouﬂe maillot-
de-bain chapeau
écharpe robe-
du-soir cravate
nightgown skirt
pants slipper
swimsuit
hat scarf
nightgown tie
bleu noir pantalon
blanc blanche noire
couleur chemise
blue black pants
white white
black color shirt
protection protéger
vêtement chaussure
gant cuir main sac
protection protect
garment shoe glove
leather hand bag
produit marque fab-
rication entreprise
vêtement objet société
product brand con-
struction business
clothing object society
femme jeun mettre
scène découvrir
passer maison ﬁlle
woman young
putting scene ﬁnd
pass home girl
tête cheveu visage
femme forme long
oreille nez noir
head hair face
woman shape long
ear nose black
靴睡⾐⼿套鞋
⼤⾐⼿短裙背
⼼袍胸罩帽
⼦⽿罩凳⼦拖
鞋披肩娃娃帽
boot pajama glove
shoe coat hand skirt
vest gown bra hat
earmuff stool slipper
shawl doll hat
穿著戴穿⽩⾊⿊⾊
⿊⾊帽⼦⼥性⾊會
wearing wear wear
white black black
hat female color will
穿戴穿着服装⽩
⾊会⼥性⿊⾊
wear wear wearing
clothing white
will female black
作品電影故事部⻆
⾊作系列主⻆動畫
works movies stories
roles work series
protagonist animation
系統種功能包括設
計作⽅式出會成
system kind function
include design work
way occur will ﬁnish
要成與時為
隻們作死出
want ﬁnish and
time for only
plural do die occur
ﺟﺰﻣﺔﺑﺪﻟﺔ رﺑﻄﺔﻋﻨﻖ
ﺣﺒﻮب ذرةﺧﻮذة
دراﺟﺔﺛﻼﺛﻴﺔ اﻟﻌﺠﻼت
ذﻗﻦﺑﻴﺠﺎﻣﺔﻣﻌﺼﻢ
ﻓﺄسﻗﺒﻌﺔﻗﻤﻴﺺ
ﺣﺬاء رداءﺛﻮب اﻟﻨﻮم
shoe suit necktie
corn helmet
tricycle chin
pajama wrist ax
hat shirt boot
robe nightgown
ٱِرْﺗَﺪَىﻟَﻮْ ن أَﺑْﻴَﺾ أَﺣْﻤَﺮﻟَﻮْ ن
ﻃَﻮِﻳﻞ أَزْرَقﻗَﻤِﻴﺺ أَﺳَﺪ أَﺳْﻮَ د
wore color white
red color long blue
shirt lion black
ﻧَﻔْﺲ واﻟِﺪﻋﺎشﻗِﺼَّﺔﺣَﻴﺎة
ﺻَﺪِﻳﻖﺳَﺒَﺐ ٱِﺳْﻢ رَﺟُﻞﻣَﺮَّة
spirit father lived
story life friend rea-
son name man once
ﻳَﺪ رَأْسﺷَﻜْﻞ ٱِرْﺗَﺪَىﺣَﻤَﻞ
رَﺟُﻞﺻُﻮرَةﺳَﻴْﻒﻃَﻮِﻳﻞ إِﻟٰﻪ
hand head shape
wore carried man
portrait sword long god
ﻗَﺪَمﻛﺮة اﻟﻘﺪمﻣُﺒﺎراة أَوَّ ل
ﻓَﺮِﻳﻖ ٱِﺗِّﺤﺎدﻋﺎﻟَﻢ دَرَﺟَﺔ
foot football match
ﬁrst team union
world degree
ٱِﺑْﻦ راوَﻧْﺪ رَﺳُﻮل
اﷲَّ
ﻧَﺒِﻲّﺻَﻠَّﻰﺳَﻠَّﻢ
god son rhubarb
messenger prophet
prayed saluted
en
de
fr
ch
ar
(a) Category clothing
blumenkohl
zucchini limette
rettich gurke
zitrone pfeffer
brokkoli sellerie
zwiebel salat
cauliﬂower
zucchini lime
radish cucumber
lemon peppers
broccoli celery
onion lettuce
zwiebel salz ﬂeisch
gemüse kartoffel
gericht zubereitung
onion salt meat
vegetable potato
meal preparation
rot geschmack
bilden blätter blüten
form sorte farbe
red taste form
leaves ﬂowers
shape variety color
angebaut mais weizen
gemüse kartoffel anbau
bohnen getreide reis
grown corn wheat
vegetable potato crop-
ping beans grain rice
cm zentimeter
mm erreichen
durchmesser länge
cm centimeter
mm reach di-
ameter length
wort bedeuten
bezeichnung beze-
ichnen lateinisch
word mean
designation
designate latin
tomato garlic cauliﬂower zucchini
pepper cucumber lettuce radish cab-
bage parsley carrot onion eggplant
onion sauce vegetable
dish pepper meat
tomato potato garlic
crop potato vegetable
grow bean wheat
fruit tomato corn
oil acid seed juice water
product vegetable
fruit vitamin sugar
plant family leaf
grow ﬂower ﬂower-
ing root wild fruit
cake milk cream
sugar chocolate
bread cheese sweet
persil cornichon
concombre poivre
radi aubergine
chou-ﬂeur cour-
gette carotte
haricot pois
parsley pickle
cucumber pep-
per radish egg-
plant cauliﬂow-
er zucchini car-
rots beans peas
huile viande sauce
tomate oignons base
pommes ail légume
oil meat sauce tomato
onions base apples
garlic vegetable
légume tomate
plantes haricot
pommes fruit carotte
vegetable tomato
plants beans ap-
ples fruit carrots
culture production
maïs agriculture
sucre agricole fruit
cultivation production
corn agriculture sugar
agricultural fruit
fruit vin jus couleur
orange arôme
pomme blanc goût
fruit wine juice
color orange ﬂavor
apple white taste
viande porc boeuf
base poulet cuisine
spécialité plat
meat pork beef
base chicken cook-
ery specialty dish
李⼦⽣菜泡菜
南⽠菜花菠菜
茄⼦番茄芹菜
柚⼦草莓蛋糕
plum lettuce
pickles pumpkin
cauliﬂower spinach
eggplant tomato
celery grapefruit
strawberry cake
種蔬菜⽔果⻝物植物
包括吃成蛋糕⻝⽤
kind vegetables fruits
food plants include
eat ﬁnish cake eat
要成與時為
隻們作死出
want ﬁnish and
time for only plu-
ral do die occur
歌曲⾳節⽬⾳樂單
曲歌成唱⽚推出
song sound program
music singles song
ﬁnish record launch
选中轮位分第烂
中第媒体获得评价
select round position
number medium
media get review
菜吃⾁汤加⼊
成盐包括⾯包⻥
dish eat meat soup
join ﬁnish salt
include bread ﬁsh
ﺷﻤﻨﺪرﻣﻮظﺗﻮت
أزرقﺑﻘﺪوﻧﺲﺑﺼﻞ
ﺛﻮمﺑﺴﻜﻮﻳﺖﺷﻤﺎم
ﻛﻮز اﻟﻌﺴﻞﺑﺎذﻧﺠﺎن
beetroot moose
blackberry parsley
onion garlic
biscuit honey-
melon eggplant
ﻟَﺤْﻢﻧَﻮْ عﻟَﺤْﻢﻣِﺜْﻞ زَﻳْﺖ
ﻫِﻨْﺪﻋﺎدَةﺧُﺒْﺰﻃَﻌﺎم رُزّ
meat kind meat
like oil India habit
bread food rice
ﺷَﺠَﺮَة زَﻳْﺘُﻮنﻫِﻨْﺪﻣِﻨْﻄَﻘَﺔ
زِراﻋَﺔﻧَﻮْ عﺷَﺠَﺮَةﻓﺎﻛِﻬَﺔﻣِﺜْﻞ
tree olive India
area agriculture
type tree fruit like
ﻣِﻠْﻌَﻘَﺔﺻَﻐِﻴﺮﻣﺎءﻧِﺼْﻒﻣﺎء
ﺷَﺮِبﻛَﺒِﻴﺮﻣُﺪَّ ة وَﺿَﻊ
spoon small water
half water drank
large duration placed
ﻧَﻔْﺲ واﻟِﺪﻋﺎشﻗِﺼَّﺔﺣَﻴﺎة
ﺻَﺪِﻳﻖﺳَﺒَﺐ ٱِﺳْﻢ رَﺟُﻞﻣَﺮَّة
spirit father lived
story life friend rea-
son name man once
ﻓِﻴﻠْﻢﻓِﻴﻠْﻢ رِواﻳَﺔ أَوَّ ل
دَوْ ر ٱِﺳْﻢﺟﺎﺋِﺰَةﻗِﺼَّﺔ
ﬁlm ﬁlm novel
ﬁrst role name
award story
en
de
fr
ch
ar
(b) Category vegetables
Figure 4: Categories clothing (a) and vegetables (b) (light red), and their ﬁve most
highly associated feature types (light blue) for English (en), German (de), French (fr), Ara-
bic (ar), and Chinese (ch). Model output of languages other than English was translated
into English by native speakers.
6. Experiment 2: Feature Quality
We next investigate the quality of the features our model learns. We do
this by letting the model predict the right concept solely from a set of features.
24


## Page 25


model
pr@1
pr@10
pr@20
avg rank
English
BCF
0.07
0.34
0.48
61.9
BayesCat
0.05
0.31
0.44
63.6
Strudel
0.04
0.31
0.45
76.1
co-occ baseline
0.013
0.210
0.370
97.4
random baseline
0.002
0.020
0.040
–
German
BCF
0.07
0.31
0.42
90.5
BayesCat
0.07
0.32
0.41
66.3
co-occ baseline
0.007
0.110
0.137
177.6
random baseline
0.002
0.021
0.041
–
French
BCF
0.07
0.31
0.44
73.2
BayesCat
0.04
0.28
0.45
64.2
co-occ baseline
0.017
0.153
0.227
136.6
random baseline
0.002
0.021
0.041
–
Chinese
BCF
0.09
0.37
0.49
66.0
BayesCat
0.09
0.38
0.53
41.7
co-occ baseline
0.033
0.157
0.187
139.1
random baseline
0.002
0.022
0.044
–
Arabic
BCF
0.13
0.49
0.61
54.9
BayesCat
0.14
0.54
0.65
27.5
co-occ baseline
0.012
0.110
0.139
154.8
random baseline
0.003
0.025
0.050
–
Table 4: Model performance on the concept prediction task in terms of precision at rank
1, 10, 20, and average rank assigned. We compare BCF (this work), BayesCat, a co-
occurrence baseline, Strudel (for English only), and a random baseline. Results are re-
ported for English, German, French, Chinese and Arabic.
If the model has acquired informative features, they will be predictive of the
unknown concept. Speciﬁcally, the model is presented with a set of previously
unseen test stimuli with the target concept removed. For each stimulus, the
model predicts the missing concept based on the features f (i.e., context
words).
6.1. Method
Like in the category evaluation above, we compare the ranking perfor-
mance of BCF, BayesCat, the co-occurrence based model, and Strudel for
25


## Page 26


English. For the Bayesian models, we directly exploit the learnt distribu-
tions. For BCF, we compute the score of a target concept c given a set of
features as:
Score(c|f) =
X
g
P(g|c)P(f|g).
(18)
Similarly, for BayesCat we compute the score of a concept c given a set of
features as follows:
Score(c|f) =
X
k
P(c|k)P(f|k).
(19)
For both Strudel and the co-occurrence model, we rank concepts accord-
ing to the cumulative association over all observed features for a particular
concept c. For Strudel, association corresponds to log-likelihood ratio-based
association scores, while for the co-occurrence model it corresponds to co-
occurrence counts, concept c:
Score(c|f) =
X
f∈f
association(c, f).
(20)
We also report a baseline which randomly selects target concepts from the
full set of concepts.
We report precision at rank 1, 10, and 20. We also report the average
rank assigned to the correct concept. All results are based on a random test
set of previously unseen stimuli.
6.2. Results
Figure 5 depicts three English stimuli, together with concept predictions
from BCF and the co-occurrence model. Table 4 shows quantitative results
of the three models averaged over a corpus of 300 test stimuli for all lan-
guages.
Both BCF and the co-occurrence model outperform the random
baseline by a large margin, and BCF achieves consistently highest scores.
Both Bayesian models (BCF and BayesCat) outperform the co-occurrence
model across all metrics and conditions.
We assume that plain concept-
feature co-occurrence information might be too sparse to provide a strong
signal of concept relevance given a set of features. The Bayesian models, on
the other hand, learn complex correspondences between features and all con-
cepts in a category. BayesCat and BCF perform comparably given that they
26


## Page 27


clam
saltwater soft naked marine family
BCF
a
snail
clam
moth
hare
salamander
BayesCat
snail
mackerel
clam
squid
crab
Strudel
house
apartmentsnail
moth
beetle
Co-occ baseline
level
snail
otter
whale
dolphin
nylon
product parachute stocking silk
fibre
BCF
nylon
crayon
mat
birch
cedar
BayesCat
card
myg
bottle
doll
bag
Strudel
nylon
apple
spider
carpet
knee
Co-occ baseline
skirt
nightgownblouse
necklace
swimsuit
lamb
faithful consecrate service gift
BCF
candle
bouquet
bread
robe
lamb
BayesCat
cabinet
board
bin
level
whip
Strudel
train
bus
church
ship
chapel
Co-occ baseline
emu
ambulancetrain
hook
trolley
Figure 5: Illustration of the concept prediction task; we show the input presented to the
model (i.e., features) followed by its predictions (target concept). The top ﬁve predictions
for BCF, BayesCat, Strudel, and the co-occurrence model are shown (left to right) and
the correct answer is highlighted in bold face (if included in the top ﬁve predictions).
exploit local co-occurrence relations in similar ways. BCF learns feature as-
sociations which discriminate concepts more accurately, suggesting that the
joint learning objective and structured feature information is beneﬁcial. The
example predictions in Figure 5 corroborate this.
Cross-lingual comparisons reveal that, compared to BCF, the perfor-
mance of the co-occurrence model degrades more severely for languages other
than English. This suggests that BCF can leverage information more eﬃ-
ciently from smaller learning corpora (see Table 2). The number of concepts
(i.e., target items to be ranked) diﬀers across languages so that absolute
numbers are not directly comparable.
Figures 2 and 4 qualitatively support the claim that BCF learns meaning-
ful features across languages, which are overall coherent and relevant to their
associated category. Some interesting cultural diﬀerences emerge, for exam-
27


## Page 28


‘Select the intruder word.’
◦
◦
◦
◦
•
◦
color
green
blue
white
milk
red
◦
•
◦
◦
◦
◦
cell
violin
study
protein
human
disease
Figure 6: Example task for our feature coherence study, correct answers are marked with
a ﬁlled circle. The example task involves categories and features induced by BCF from
the English Wikipedia.
ple German is the only language for which a measurement feature type is
induced for vegetables (Figure 4b; de, 4th from left), while for clothing,
a fashion industry feature emerges in French (Figure 4a; fr, 3rd from left).
For the same category, a feature type pertaining to colour emerges for all ﬁve
languages (4a, bold margins). In addition, some features in other languages
were not straightforwardly translatable into English. For example, the 3rd
feature type for vegetables in Chinese (Figure 4b) includes the word 分
which refers to the extent to which food is cooked 4 and 烂which is the stage
when food starts to fall apart after cooking (stewing). In addition, the feature
types induced for the Chinese clothing category include two words which
both translate to the English word wear, but in Chinese are speciﬁc to wear-
ing small items (e.g., jewelery; 戴), and wearing clothes (穿), respectively.
Language-speciﬁc features are meaningful, and at the same time category-
feature associations across languages reﬂect culture-driven diﬀerences.
7. Experiment 3: Feature Relevance and Coherence
Given that our aim is to induce cognitive representations of the world,
the ultimate assessment of the model’s representations is their meaningful-
ness to humans, i.e., speakers of our target languages. To this end, we elicited
judgments of feature quality from native speakers using the crowd sourcing
platforms CrowdFlower5 and Amazon Mechanical Turk.6 Speciﬁcally, we are
interested in two questions: (1) Do induced feature types have a single co-
4Roughly equivalent to the English rare, medium, well-done, but applicable to all kinds
of food.
5https://www.crowdflower.com/
6https://www.mturk.com/
28


## Page 29


‘Select intruder feature type (right) wrt category (left).’
wasp ant
caterpillar hornet
moth houseﬂy
beetle honeydew
grasshopper
◦
insect beetle family larva spider
◦
tree leaf plant nest grow
•
guitar piano clarinet flute trumpet
◦
male female egg length cm
◦
white brown dark tail color
◦
population habitat bird forest water
Figure 7: An example task for our feature relevance study. The example task involves
categories and features induced by BCF from the English Wikipedia.
herent underlying theme such as color or function (feature coherence); (2)
Do feature types associated with a category relate to that category (feature
relevance)?
We compared the feature types learnt by BCF against the co-occurrence
model as well as BayesCat. For English we also include Strudel. We omit-
ted the random baseline from this evaluation since it was clearly inferior in
previous simulations.
7.1. Method
We adopted the topic intrusion experimental paradigm [73] for assessing
the induced features in two ways. Firstly, we examined whether the fea-
ture types our model learns are thematically coherent.
Participants were
presented features types (as lists of words), which were augmented with a
random ‘intruder’ feature, and their task was to correctly identify the in-
truder feature. Figure 6 displays an example task. If the feature types are
internally coherent we expect annotators to identify the intruder with high
accuracy.
We evaluated all 50 feature types as induced by BCF and the
co-occurrence model.
Secondly, we assessed the relevance of feature types assigned to any cat-
egory. An example task is shown in Figure 7. We presented participants
with a category and ﬁve feature types (each as a list of words), one of which
was randomly added and was not associated with the category in the model
output. Again, they needed to select the correct intruder. If category-feature
type associations induced by the model are generally relevant, annotators will
be able to identify the intruder with high accuracy. We evaluated all 40 in-
duced categories and their associated features for BCF and the co-occurrence
model.
29


## Page 30


For both elicitation studies, we obtained 10 responses per task (see Fig-
ures 6 and 7); participants judged a single concept and its features per task.
All participants were required to be native speakers of the language they
were evaluating, and we ﬁltered crowdworkers through their location of res-
idence and self-reported native language (using the functionality provided
by the crowdsourcing platforms). We additionally included test questions
among tasks for which the true answer was known, and discarded the data
from participants who failed to achieve high accuracy on these test questions.
Overall, we obtained 50×10 responses for the feature coherence study and
40×10 responses for feature relevance.
We report the average accuracy across participants of selecting the correct
intruder feature and intruder feature type, respectively. In addition we report
inter annotator agreement (IAA) using Fleiss Kappa [74].
The extent to
which annotators agree in their judgments allows us to evaluate the diﬃculty
of the task, as well as the reliability of the results.
7.2. Results
Table 5 displays the results for the feature relevance study and Table 6
the feature coherence study. Table 5 shows that humans are able to detect
intruder feature types with higher accuracy in the context of BCF-induced
representations, compared with all comparison models. Additionally, inter
annotator agreement (IAA) is consistently higher for BCF, indicating that
participants more frequently agreed on their selections and that selecting
intruders in the BCF output was an easier task for them compared to the
comparison models. Similar to the previous simulations, we observe that both
Bayesian models (BayesCat and BCF) outperform the count-based models.
In this evaluation, however, we also observe a clear advantage of BCF com-
pared to BayesCat, which does not learn structured feature types inherently.
BCF learns to associate relevant features to categories.
Table 6 shows the results of the feature coherence study, where the overall
pattern of results is similar as above. We can see that participants are able
to detect intruder features from the types learnt by BCF more reliably than
from those learnt by all comparison models. Again, both Bayesian models
outperform the count-based baselines both in terms of accuracy and inter an-
notator agreement. The superior performance of BCF compared to BayesCat
indicates that its ability to learn structured features jointly with categories in
a single process leads to higher quality feature representations. In particular,
in addition to associating relevant feature types with categories, the feature
30


## Page 31


model
accuracy
IAA
English
BCF
0.752
0.700
BayesCat
0.605
0.456
strudel
0.435
0.364
co-occ baseline
0.302
0.229
German
BCF
0.530
0.361
BayesCat
0.370
0.206
co-occ baseline
0.340
0.201
French
BCF
0.555
0.427
BayesCat
0.468
0.294
co-occ baseline
0.278
0.216
Chinese
BCF
0.468
0.419
BayesCat
0.261
0.108
co-occ baseline
0.390
0.310
Arabic
BCF
0.385
0.278
BayesCat
0.385
0.215
co-occ baseline
0.278
0.155
Table 5:
Results of our feature relevance study for BCF (this work), BayesCat, the
co-occurrence model (co-occ), and Strudel (for English only) in terms of accuracy (the
proportion of intruders identiﬁed correctly) and inter-annotator agreement (IAA; Fleiss
Kappa [74]) for ﬁve target languages.
types themselves are internally coherent, pertaining to diﬀerent aspects or
properties of the reference category.
Comparing results across languages we observe that scores for English
exceed scores for all other languages. At the same time, for almost all mod-
els and languages the IAA scores fall under the category of ‘fair agreement’
(0.20 < κ < 0.40) indicating that the elicitation task was feasible for crowd-
workers. This applies to both evaluations (Tables 5 and 6). We observed a
similar pattern in the results of Experiment 1 (Table 3). We believe there are
two reasons for this drop. Firstly, in order to perform cross-linguistic experi-
ments, we translated English categories into other languages. As mentioned
in Sections 5.2 and 6.2, such a direct correspondence may not always exist.
Consequently, annotators for languages other than English are faced with a
noisier (and potentially harder) task. Secondly, while it is straightforward to
recruit English native speakers on crowd sourcing platforms, it has proven
more challenging for the other languages. We suspect that our eﬀort to re-
31


## Page 32


model
accuracy
IAA
English
BCF
0.814
0.710
BayesCat
0.642
0.529
strudel
0.260
0.294
co-occ baseline
0.266
0.296
German
BCF
0.760
0.639
BayesCat
0.465
0.341
co-occ baseline
0.220
0.210
French
BCF
0.690
0.527
BayesCat
0.557
0.409
co-occ baseline
0.224
0.227
Chinese
BCF
0.574
0.723
BayesCat
0.269
0.234
co-occ baseline
0.228
0.227
Arabic
BCF
0.594
0.444
BayesCat
0.416
0.423
co-occ baseline
0.236
0.195
Table 6: Results from our feature coherence study for BCF (this work) , BayesCat, the
co-occurrence model (co-occ), and Strudel (for English only) in terms of accuracy (the
proportion of intruders identiﬁed correctly) and inter-annotator agreement (IAA; Fleiss
Kappa [74]) for ﬁve target languages.
cruit native speakers, might not have been entirely fail-safe for languages
other that English, and that the language competence of those crowdworkers
might have impacted the quality of their judgments.
Overall, we conclude that jointly inducing structured features together
with categories from natural language corpora in diﬀerent languages enables
BCF to learn feature types which are (1) internally coherent, referring to a
single underlying theme; and (2) informative about the categories with which
they are associated.
8. General Discussion
We presented the ﬁrst large-scale, cross-linguistic analysis of categoriza-
tion using naturally occurring data. We showed that rational Bayesian mod-
els of categorization can learn meaningful categories and their features from
32


## Page 33


complex environments resembling the natural world more closely than limited
laboratory settings.
We developed BCF, a cognitively motivated Bayesian model, and inves-
tigated its ability to learn categories (for hundreds of concepts) and their
structured features from corpora in ﬁve languages.
Like humans ‘in the
wild’, our model learns categories and relevant features jointly [29, 30], and
induces structured representations of categories [31, 32, 33]. Compared to a
simpler co-occurrence model and a Bayesian model with no access to these
mechanisms BCF learns better categories and features which are rated as
more relevant and coherent by humans. BCF models category acquisition as
a general, language-independent process. It neither utilizes language-speciﬁc
knowledge nor requires language-speciﬁc tuning, and as such paves the way
for future investigations involving more languages, or diﬀerent kinds of cor-
pora.
Our study sheds light on the acquisition of concrete concepts and their
features from text, and as such adopts a constrained view of both the learning
environment and the learning target. It suggests a number of interesting
suggestions for future research. First, this article considered natural language
input as an approximation of the environment from which categories and their
representations are learnt. While we showed that the linguistic environment
is a useful approximation of the full multimodal input a learner has access to,
it is clear that language cannot capture this multimodal environment is not
captured in its entirety. Computational models of word learning have been
trained on multimodal input data (albeit on smaller-scale problems; [75, 76]).
Advantageously, Bayesian models are ﬂexible with respect to the input data
they receive, so we expect the application of our model to multimodal data
to be a feasible avenue for future work. Applying our models to such data
sets would allow to compare the category acquisition process as well as the
acquired representations from multimodal input against those emerging from
language data alone.
A second direction for future work concerns the cognitive assumptions un-
derlying the learning setup. The models discussed in this article learn from
collections of natural language stimuli consisting of a target concept mention
and its surrounding context. This input is based on the rather bold assump-
tion that the learner already has substantial linguistic prior knowledge prior
to concept and feature learning: she has successfully mapped each target
concept to a word. As supported by an extensive literature [5, 6, 4], word
learning, itself a fundamental challenge for young infants, and concept learn-
33


## Page 34


ing exhibit a mutual inﬂuence. Our work remains agnostic about the fact
that the meaning of words itself needs to be acquired, and that knowledge
about concepts and categories will help tackle the word learning problem. A
fully faithful model would consider the problems of word and concept or cate-
gory learning jointly. Extending BCF to account for this joint optimization,
and investigating emerging acquisition patterns across diﬀerent languages,
will be a very interesting avenue for future research.
Humans not only categorize the physical world around them, but also
infer complex representations of abstract categories and concepts such as
political (e.g., parliament, socialist), legal (e.g., law, trial), or feelings
(e.g., mirth or embarrassment). Lacking any physical realization, and hence
perceivable properties, there is evidence that language plays a particularly
important role in acquiring the meaning of such abstract concepts [77]. A
data-driven study across languages would be particularly interesting in the
context of abstract categories, whose representations are expected to be more
sensitive to the cultural environment.
In conclusion, our investigations in to category and feature learning from
text across languages corroborate prior results [21] that the non-linguistic
learning environment is to some extent encoded in language. They addi-
tionally provide evidence for the stronger statement that the structure of
the world which aﬀords rich mental categorical representations is encoded in
language. We envision scalable testbeds which combine naturally occurring
data from multiple modalities, for example combining text data with im-
ages or video. Our work exempliﬁes the potential of interpretable statistical
models for gaining insights into the mechanisms which are at play in human
cognition. We demonstrated the potential of large naturalistic datasets for
the development and testing of computational models, and are conﬁdent that
computational cognitive models together with large naturally occurring data
set will open up novel opportunities for investigating human cognition at
scale.
Acknowledgments
This research was funded by the European Research Council (award num-
ber 681760). The funding body had no involvement in the study design, data
collection, analysis and interpretation. It was also not involved in the writing
of the report and the decision to submit the article for publication.
34


## Page 35


References
[1] P. G. Schyns, A. Oliva, Dr. angry and mr. smile: when categorization
ﬂexibly modiﬁes the perception of faces in rapid visual presentations,
Cognition 69 (1999) 243 – 265.
[2] R. L. Goldstone, Learning to perceive while perceiving to learn, in:
Perceptual organization in vision: Behavioral and neural perspectives,
pp. 233–278.
[3] S. R. Waxman, D. B. Markov,
Object properties and object kind:
twenty-one-month-old infants’ extensions of novel adjectives, Child De-
velopment 69 (1998) 1313–1329.
[4] A. Borovsky, J. Elman,
Language input and semantic categories: a
relation between cognition and early word learning, Journal of Child
Leanguage 33 (2006) 759–790.
[5] A. Gopnik, A. Meltzoﬀ,
The Development of Categorization in the
Second Year and Its Relation to Other Cognitive and Linguistic Devel-
opments, Child Development 58 (1987).
[6] S. R. Waxman, D. B. Markow, Words as invitations to form categories:
Evidence from 12- to 13-month-old infants, Cognitive Psychology 29
(1995) 257–302.
[7] B. Malt, Category coherence in cross-cultural perspective, Cognitive
Psychology 29 (1995) 85 – 148.
[8] L.-J. Ji, Z. Zhang, R. E. Nisbett, Is it culture or is it language? exam-
ination of language eﬀects in cross-cultural research on categorization,
Journal of Personality and Psychology 87 (2004) 57–65.
[9] S. J. Unsworth, C. R. Sears, P. M. Pexman, Cultural inﬂuences on cat-
egorization processes, Journal of Cross-Cultural Psychology 36 (2005)
662–688.
[10] D. L. Medin, S. J. Unsworth, L. Hirschfeld, Culture, categorization,
and reasoning, in: S. Kitayama, D. Cohen (Eds.), Handbook of cultural
psychology, Guilford Press, 2007.
35


## Page 36


[11] R. M. Nosofsky, Exemplar-based accounts of relations between classiﬁ-
cation, recognition, and typicality, Journal of Experimental Psychology:
Learning, Memory, and Cognition 14 (1988) 700–708.
[12] E. Rosch, Natural categories, Cognitive Psychology (1973) 328–350.
[13] J. E. Corter, M. A. Gluck, Explaining basic categories - feature pre-
dictability and information, Psychological Bulletin 111 (1992) 291–303.
[14] G. L. Murphy, D. L. Medin, The role of theories in conceptual coherence,
Psychological Review 92 (1985) 289–316.
[15] J. R. Anderson, The adaptive nature of human categorization., Psycho-
logical Review 98 (1991) 409–429.
[16] M. D. Lee, D. J. Navarro, Extending the ALCOVE model of category
learning to featural stimulus domains., Psychonomic Bulletin & Review
9 (2002) 43–58.
[17] M. H. Bornstein, C. Mash, Experience-based and on-line categorization
of objects in early infancy, Child Development 81 (2010) 884–897.
[18] D. L. Medin, M. M. Schaﬀer, Context theory of classiﬁcation learning,
Psychological Review 85 (1978) 207–238.
[19] J. K. Kruschke, Human category learning: Implications for backpropa-
gation models, Connection Science 5 (1993) 3–36.
[20] J. Henrich, S. J. Heine, A. Norenzayan,
The weirdest people in the
world?, Behavioral and brain sciences 33 (2010) 61–83.
[21] B. Riordan, M. N. Jones, Redundancy in perceptual and linguistic expe-
rience: Comparing feature-based and distributional models of semantic
representation, Topics in Cognitive Science 3 (2011) 303–345.
[22] T. Fountain, M. Lapata, Incremental models of natural language cate-
gory acquisition, in: Proceedings of the 33nd Annual Conference of the
Cognitive Science Society, pp. 255–260.
[23] L. Frermann, M. Lapata, Incremental bayesian category learning from
natural language, Cognitive Science 40 (2016) 1333–1381.
36


## Page 37


[24] T. L. Griﬃths, C. Kemp, J. B. Tenenbaum, Bayesian models of cog-
nition,
Cambridge Handbook of Computational Cognitive Modeling
(2008).
[25] N. Chater, M. Oaksford, U. Hahn, E. Heit, Bayesian models of cognition,
Wiley Interdisciplinary Reviews: Cognitive Science 1 (2010) 811–823.
[26] A. Perfors, J. B. Tenenbaum, T. L. Griﬃths, F. Xu, A tutorial introduc-
tion to bayesian models of cognitive development, Cognition 120 (2011)
302 – 321.
[27] A. N. Sanborn, T. L. Griﬃths, D. J. Navarro,
Rational approxima-
tions to rational models: Alternative algorithms for category learning.,
Psychological review 117 (2010) 1144–1167.
[28] F. Xu, J. B. Tenenbaum, Word learning as bayesian inference, Psycho-
logical Review 114 (2007) 245–272.
[29] R. L. Goldstone, Y. Lippa, R. M. Shiﬀrin, Altering Object Representa-
tions through Category Learning, Cognition 78 (2001) 27–43.
[30] P. G. Schyns, L. Rodet, Categorization creates functional features, Jour-
nal of Experimental Psychology: Learning, Memory, and Cognition 23
(1997) 681–696.
[31] W.-K. Ahn, Why are diﬀerent features central for natural kinds and
artifacts?: the role of causal status in determining feature centrality.,
Cognition 69 (1998) 135.
[32] K. McRae, G. S. Cree, M. S. Seidenberg, C. McNorgan, Semantic fea-
ture production norms for a large set of living and nonliving things.,
Behavioral Research Methods 37 (2005) 547–59.
[33] T. L. Spalding, B. H. Ross, Concept learning and feature interpretation,
Memory & Cognition 28 (2000) 439–451.
[34] A. Caliskan, J. J. Bryson, A. Narayanan, Semantics derived automat-
ically from language corpora contain human-like biases,
Science 356
(2017) 183–186.
37


## Page 38


[35] R. L. Goldstone, G. Lupyan, Discovering psychological principles by
mining naturally occurring data sets,
Topics in Cognitive Science 8
(2016) 548–568.
[36] M. Jones, Big Data in Cognitive Science, Frontiers of Cognitive Psy-
chology, Taylor & Francis, 2016.
[37] A. Paxton, T. L. Griﬃths, Finding the traces of behavioral and cog-
nitive processes in big data and naturally occurring datasets, Behavior
Research Methods 49 (2017) 1630–1638.
[38] L. J. Rips, E. E. Smith, D. L. Medin, Concepts and Categories: Memory,
Meaning and Metaphysics, in: K. J. Holyoak, R. G. Morrison (Eds.),
The Oxford Handbook of Thinking and Reasoning, Oxford University
Press, 2012, pp. 177–209.
[39] B. C. Malt, E. E. Smith, Correlated properties in natural categories,
Journal of Verbal Learning and Verbal Behavior 23 (1984) 250 – 269.
[40] E. Heit, J. Rubinstein,
Similarity and Property Eﬀects in Inductive
Reasoning,
Journal of Experimental Psychology: Learning, Memory
and Cognition 20 (1994) 411–422.
[41] B. Trauble, S. Pauen,
The role of functional information for infant
categorization, Cognition 105 (2007) 362–379.
[42] S. Jones, L. Smith, B. Landau,
Object properties and knowledge in
early lexical learning, Child development 62 (1991) 499–516.
[43] J. Macario, Young children’s use of color in classiﬁcation: Foods and
canonically colored objects, Cognitive Development 6 (1991) 17–46.
[44] L. Wu, L. W. Barsalou, Perceptual simulation in conceptual combina-
tion: Evidence from property generation, Acta Psychologica 132 (2009)
173 – 189.
[45] L. W. Barsalou,
Perceptual symbol systems,
Behavioral and Brain
Sciences 22 (1999) 577–609.
[46] F. C. Keil, Concepts, Kinds, and Cognitive Development, MIT Press,
1989.
38


## Page 39


[47] K. McRae, G. S. Cree, Factors underlying category-speciﬁc semantic
impairments,
in: E. M. E. Forde, G. Humphreys (Eds.), Category-
speciﬁcity in mind and brain, Psychology Press, 2002, pp. 211–248.
[48] R. L. Goldstone, E. Gerganov, D. L, M. E. Roberts, R. L. Goldstone,
Learning to see and conceive, in: The new cognitive sciences (Part of
the Vienna Series in Theoretical Biology), MIT Press, Cambridge, MA,
2008, pp. 163–188.
[49] R. Pevtzow, R. L. Goldstone, Categorization and the parsing of objects,
in: Proceedings of the 16th Annual Conference of the Cognitive Science
Society, Lawrence Erlbaum Associates, 1994, pp. 712–722.
[50] R. L. Goldstone, M. Steyvers, The sensitization and diﬀerentiation of di-
mensions during category learning, Journal of Experimental Psychology
130 (2001) 116–139.
[51] A. N. Sanborn, T. L. Griﬃths, D. J. Navarro, A more rational model
of categorization, in: Proceedings of the 28th Annual Conference of the
Cognitive Science Society, pp. 726–731.
[52] L. Frermann, M. Lapata, Incremental bayesian category learning from
natural language, Cognitive Science 40 (2016) 1333–1381.
[53] P. Shafto, C. Kemp, V. Mansinghka, J. B. Tenenbaum, A probabilistic
model of cross-categorization, Cognition 120 (2011) 1 – 25.
[54] C. Kemp, A. Perfors, J. B. Tenenbaum, Learning domain structures,
in: Proceedings of the 26th Annual Conference of the Cognitive Science
Society, Erlbaum, 2003, pp. 720–725.
[55] A. Perfors, C. Kemp, J. B. Tenenbaum, Modeling the acquisition of
domain structure and feature understanding, in: Proceedings of the 27th
Annual Conference of the Cognitive Science Society, pp. 1720–1725.
[56] A. Perfors, J. B. Tenenbaum, Learning to learn categories, in: Proceed-
ings of the 31st Annual Conference of the Cognitive Science Society, pp.
136–141.
[57] M. Steyvers, Combining feature norms and text data with topic models.,
Acta Psychologica 133 (2010) 234–243.
39


## Page 40


[58] D. M. Blei, A. Y. Ng, M. I. Jordan, Latent Dirichlet allocation, Journal
of Machine Learning Research 3 (2003) 993–1022.
[59] M. Baroni, B. Murphy, E. Barbu, M. Poesio, Strudel: A corpus-based
semantic model based on properties and types, Cognitive Science 34
(2010) 222–254.
[60] B. Devereux, N. Pilkington, T. Poibeau, A. Korhonen, Towards unre-
stricted, large-scale acquisition of feature-based conceptual representa-
tions from corpus data, Research on Language & Computation 7 (2009)
137–170.
[61] C. Kelly, B. Devereux, A. Korhonen, Automatic extraction of property
norm-like data from large text corpora,
Cognitive Science 38 (2014)
638–682.
[62] T. L. Griﬃths, J. B. Tenenbaum, Optimal predictions in everyday cog-
nition, Psychological Science 17 (2006) 767–773.
[63] D. Marr, Vision: A Computational Investigation into the Human Rep-
resentation and Processing of Visual Information, Henry Holt and Co.,
Inc., New York, NY, USA, 1982.
[64] S. Geman, D. Geman, Stochastic relaxation, Gibbs distributions and the
Bayesian restoration of images, IEEE Transactions on Pattern Analysis
and Machine Intelligence 6 (1984) 721–741.
[65] C. M. Bishop, Pattern Recognition and Machine Learning (Information
Science and Statistics), Springer-Verlag New York, Inc., Secaucus, NJ,
USA, 2006.
[66] D. J. C. MacKay, Information Theory, Inference & Learning Algorithms,
Cambridge University Press, New York, NY, USA, 2002.
[67] D. Vinson, G. Vigliocco, Semantic feature production norms for a large
set of objects and events, Behavior Research Methods 40 (2008) 183–
190.
[68] T. Fountain, M. Lapata, Meaning representation in natural language
categorization, in: Proceedings of the 32nd Annual Conference of the
Cognitive Science Society, pp. 1916–1921.
40


## Page 41


[69] M. Baroni, Detailed description of the Strudel algorithm, Technical Re-
port, 2010.
[70] S. Lloyd,
Least squares quantization in pcm,
IEEE transactions on
information theory 28 (1982) 129–137.
[71] J. Lang, M. Lapata, Unsupervised semantic role induction with graph
partitioning, in: Proceedings of the 2011 Conference on Empirical Meth-
ods in Natural Language Processing, pp. 1320–1331.
[72] A. Rosenberg, J. Hirschberg, V-measure: A conditional entropy-based
external cluster evaluation measure, in: Proceedings of the 2007 Joint
Conference on Empirical Methods in Natural Language Processing and
Computational Natural Language Learning, pp. 410–420.
[73] J. Chang, S. Gerrish, C. Wang, J. L. Boyd-graber, D. M. Blei, Reading
tea leaves: How humans interpret topic models, in: Y. Bengio, D. Schu-
urmans, J. Laﬀerty, C. Williams, A. Culotta (Eds.), Advances in Neural
Information Processing Systems 22, Curran Associates, Inc., 2009, pp.
288–296.
[74] J. L. Fleiss, Statistical Methods for Rates and Proportions, Wiley, New
York, 1981.
[75] M. C. Frank, N. D. Goodman, J. B. Tenenbaum, Using speakers’ ref-
erential intentions to model early cross-situational word learning, Psy-
chological Science 20 (2009) 579–575.
[76] C. Yu, L. B. Smith, Rapid Word Learning Under Uncertainty via Cross-
Situational Statistics, Psychological Science 18 (2007) 414–420.
[77] K. Wiemer-Hastings, A. C. Graesser, Contextually Representing Ab-
stract Concepts with Abstract Structures, in: Proceedings of the 22nd
Annual Meeting of the Cognitive Science Society, pp. 983–989.
41

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1902_08830v1_categorization_in_the_wild_generalizing_cognitive_models_to_naturalistic_data_a
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1902_08830V1_CATEGORIZATION_IN_THE_WILD_GENERALIZING_COGNITIVE_MODELS_TO_NATURALISTIC_DATA_A.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
