---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.02788v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1903.02788v2_Interpretable_Deep_Learning_in_Drug_Discovery

> Source: 1903.02788v2_Interpretable_Deep_Learning_in_Drug_Discovery.pdf

> Pages: 17

---


## Page 1


Interpretable Deep Learning in Drug Discovery
Kristina Preuer1, Günter Klambauer1, Friedrich Rippmann2, Sepp Hochreiter1,
and Thomas Unterthiner1
1 LIT AI Lab & Institute for Machine Learning,
Johannes Kepler University Linz, A-4040 Linz, Austria
2 Computational Chemistry & Biology, Merck KGaA,
64293 Darmstadt, Germany
Abstract. Without any means of interpretation, neural networks that
predict molecular properties and bioactivities are merely black boxes. We
will unravel these black boxes and will demonstrate approaches to under-
stand the learned representations which are hidden inside these models.
We show how single neurons can be interpreted as classiﬁers which de-
termine the presence or absence of pharmacophore- or toxicophore-like
structures, thereby generating new insights and relevant knowledge for
chemistry, pharmacology and biochemistry. We further discuss how these
novel pharmacophores/toxicophores can be determined from the network
by identifying the most relevant components of a compound for the pre-
diction of the network. Additionally, we propose a method which can be
used to extract new pharmacophores from a model and will show that
these extracted structures are consistent with literature ﬁndings. We en-
vision that having access to such interpretable knowledge is a crucial aid
in the development and design of new pharmaceutically active molecules,
and helps to investigate and understand failures and successes of current
methods.
Keywords: Deep Learning, Neural Networks, Drug Development, Tar-
get Prediction.
1
Introduction
The central goal of drug discovery research is to identify molecules
that act
beneﬁcially on the human (or animal) system, e.g., that have a certain thera-
peutic eﬀect against particular diseases. It is generally unknown how chemical
structures have to look like in order to induce the wanted biological eﬀects.
Therefore, a large number of molecules have to be investigated to ﬁnd a po-
tential drug, leading to long drug identiﬁcation times, and high costs. This is
typically done by means of High-Throughput Screening (HTS), where a bio-
logical screening experiment is used to identify whether a molecule at a given
concentration exhibits a certain biological eﬀect or not. However, running a large
To be published in "Interpretable AI: Interpreting, Explaining and Visualizing Deep
Learning"
arXiv:1903.02788v2  [cs.LG]  18 Mar 2019


## Page 2


number of these experiments is expensive and time-intensive. Therefore, using
computational models as a means of “Virtual Screening”, i.e. to predict these
biological eﬀects using computational methods and thereby avoiding physical
screening, has a long tradition in drug development [17,15].
In the past years, the advent of deep learning has allowed neural networks to
become the best-performing method for predicting biological activities based on
the chemical structure of the molecules [19,21] mostly because of their ability to
exploit the multi-task setting [31]. Recently, deep learning enabled automated
molecule generation [28,22,35], which has become a new interesting application
in the ﬁeld of drug design. However, some generative models still have problems
with mode collapse [33] and are hard to evaluate [25]. Interpretability of neural
networks both for predictions and automated drug design could further push
their performance, would increase their usability and would especially improve
acceptance.
Nowadays, mainly two types of deep neural networks are most frequently
used in Virtual Screening: descriptor-based feed-forward neural networks (see
Section 3) and graph convolutional neural networks (see Section 4). Descriptor-
based neural networks rely on predeﬁned features, so-called molecular descrip-
tors, whereas graph convolutional neural networks learn a continuous represen-
tation directly from the molecular graph. Neural networks take these discrete or
numerical representation of a chemical molecule and calculate their prediction
by feeding that representation through several layers of non-linear, diﬀerentiable
transformations with many, often millions of, adjustable parameters. Unfortu-
nately, the function that is encoded in such a neural network is typically impos-
sible to interpret by humans. In other words: how the neural network reaches a
conclusion is usually beyond the understanding of a human user. This work aims
at bridging this gap in our understanding of neural network predictions for drug
discovery. Although [9,2,27] have already focused on the diﬃcult question how
machine learning models can be interpreted, none of these works focus on an in
depth analysis of both descriptor based and graph based deep learning models
for QSAR predictions.
In this work, we ﬁrst show how a trained neural network can be used to
interpret which parts of a molecule are important for its biological properties,
and then demonstrate how graph convolutional neural networks can be used
to extract annotated chemical substructures, known as pharmacophores or toxi-
cophores. We will empirically show that neural networks rely on pharmacophore-
like features to reach their conclusions, similar to how a human pharmacologist
would. Concretely, we will show in subsection 3.1 that the units that form the
layers of a neural network are pharmacophore detectors. Furthermore, we will
demonstrate in subsection 3.2 how indicative substructures can be determined
for individual samples. In the second part of our analysis we will focus on graph
convolutional neural networks and show that the identiﬁed pharmacophores ex-
tracted directly from the network match well-known, annotated substructures
from the literature.


## Page 3


2
Learning from molecular structures
Fig. 1. Example of a 2 dimen-
sional structure representation of a
molecule.
There are multiple scales at which molecules
such as the example shown in Fig. 1 can
be represented. Molecules can be represented
by their molecular formula (1D), by their
structural formula (2D), by their confor-
mation (3D), by their mutual orientation
and time-dependent dynamics or combina-
tions of all these [5]. The choice of the
right representation is task dependent and
crucial for the learning algorithm. Most
commonly, molecules are described by so-
called Extended Connectivity Fingerprints
(ECFPs)[26]. These 2D-descriptors represent
the 2-dimensional structure as a bit vector
indicating the presence and absence of prede-
ﬁned substructures and showed a high predic-
tive performance in [32,20,24,18]. Therefore,
we will use these as descriptors for our ﬁrst experiments described in section 3.
However, newer approaches focus on direct end-to-end methods, where the
molecular representation is directly learned from the molecular graph [7,8,13].
These graph convolutional methods learn molecular representations during the
training process and are therefore able to learn wildcards and ﬂexible substruc-
tures. We will analyse the representations learned by a graph convolutional net-
work in section 4.
3
Descriptor-based Feed Forward Neural Networks
A feed forward neural network consists of several layers of computing units. Each
layer l takes as its input the vector of outputs hl of the layer below it. In the
ﬁrst layer, we use the input data h0 = x instead. The layer l transforms its input
according to some parameterized function to produce its own output
hl+1 = f(hlWl)
where f is an activation function that is applied to each element, or “hidden
unit”, hl
i of the vector individually. Each of these elements can be understood
as a feature detector, which detects the presence or absence of some feature
in its inputs. The nature of that feature is deﬁned by the learned parameters
Wl, but is usually very diﬃcult to interpret, as the features are typically a
highly abstract, non-linear function of the input features. However, we can show
that when learned on typical drug development tasks, these hidden units encode
features that are very similar to features used by pharmaceutical researchers for
decades.


## Page 4


3.1
Interpreting Hidden Neurons
A common way to analyze chemical properties of small molecules is by looking
at its structures. Atoms that are close together often form functional groups,
which may have speciﬁc roles for binding to the respective biological targets.
These functional groups form larger structures which then are responsible for
the biological eﬀect, by modulating a biological target (e.g. a protein or DNA).
work together to build reactive centers that steer chemical reactions. Binding
to a speciﬁc target can only take place when the necessary active centers are
present at exactly the right locations. The exact conﬁguration of active centers
is referred to as a pharmacophore [16]. In other words, a pharmacophore is a
molecular substructure, or a set of molecular substructures that is responsible
for a speciﬁc interaction between chemical molecules and biological targets. It is
our hypothesis that the hidden units of a neural network learn to detect pharma-
cophores. To investigate this, we employed a strategy similar to [3], and trained
a network that predicts the toxicology of molecules, using the data set from the
Tox21 Data Challenge [11]. The data set contains around 12 000 molecules, for
each of which twelve biological eﬀects were measured in wet lab experiments with
binary outcome (“toxic”, “non-toxic”). These twelve biological eﬀects served pose
a multi-task classiﬁcation problem. Deep Learning is the best performing method
for this task [20,14], and we follow the network architecture outlined in [14] for
our experiments, using a network with 4 hidden layers of 1024 hidden units with
SELU activation function. To represent our molecules, we use ECFPs [26] of ra-
dius 1, meaning that the input representation includes presence/absence calls of
single atoms and small substructures with at most 5 atoms, but gives no concrete
information about larger molecular substructures. The network still performed
relatively well, with an average AUC over the 12 targets of 0.77, which would
still place it among the top 10 models in the original Tox21 Data Challenge [20].
After training the network, we calculate the activation of the hidden units
for all molecules in the training set, and relate them with presence/absence calls
of pharmacophores calculated for the same molecules. For this, we used phar-
macophores known to be relevant in toxicology [30], the so-called toxicophores.
Starting from all the toxicophores in [30], we ﬁlter out those that were were
present in less than 20 of our molecules, leaving us with a total of about 650
toxicophores. For each hidden unit i and each toxicophore j, we then performed
a Mann–Whitney U-Test to see if there was a signiﬁcant diﬀerence in the acti-
vations between the molecules where a given toxicophore was present and the
ones where it was absent. We then looked at correlations that were signiﬁcant at
p ≤0.05 after adjusting for the multiple testing using a very conservative Bon-
feroni correction. This leaves us with a total of ≈290 toxicophores that were
signiﬁcantly correlated with hidden units of the network.
Next, we investigated whether the hierarchy of the layers is associated with
the complexity of the detected toxicophores. If a network learns some biologi-
cally meaningful information in one of its layers, it will still need to transport
this information through all other layers to use it in its ﬁnal prediction at the
top layer. This means that every important toxicophore which is discovered in


## Page 5


a lower layer will usually also reappear in all subsequent layers. Figure 2 shows
which layers are discovering our known pharmacophores. It appears that the
pharmacophores are primarily discovered in the ﬁrst few layers. The later layers
tend to mainly discover pharmacophores that are more complex. Here, we mea-
sure the complexity of a pharmacophore by the number of atoms involved in it.
The results are well in line with the usual view of deep learning constructing
more and more complex features in its higher layers [4].
We have demonstrated that neural networks learn pharmacophore detectors
by correlating the hidden units with known toxicophores. However, not all sam-
ples contain a known toxicophore. Hence, we will demonstrate in the next section
how indicative substructures can be identiﬁed for any input molecule.
1
2
3
4
5
6
7
8
Layer
0
20
40
60
80
Number of pharmacophores
1
2
3
4
5
6
7
8
Layer
3
4
5
6
7
8
Pharmacophore size (in atoms)
Fig. 2. Left: How many pharmacophores were found in each layer of the network.
Right: Average size of the pharmacophore (in number of involved atoms) that are ﬁrst
discovered in a given layer. Error bars are standard errors. Note that there are no error
bars for layer number 8, as only one pharmacophore was ﬁrst discovered here.
3.2
Interpreting the Importance of Input Components
Several ideas have been proposed to explain the predictions from a neural net-
work by attributing its decisions to speciﬁc input features. See Ancona et al. [1]
for a short overview of gradient-based methods. One of these methods is In-
tegrated Gradients [29], which calculates an attribution value ai(x) for each
input dimension i. The value ai(x) can be interpreted as the contribution of
i to changing the prediction from a baseline input F(x′) to some speciﬁc in-
put F(x). It fulﬁlls many useful properties, for example, it is guaranteed that
F(x)−F(x′) = P
i ai(x). Additionally, Integrated Gradients is the only method
that works well even when there are multiplicative interactions between features
of those considered by [1]. Furthermore, it is independent of the concrete choice
of architecture, activation function or other hyperparameters. The method works
by aggregating the gradients of the model’s output on the straight path between


## Page 6


x′ and the target x. When implementing the method, this integral is approxi-
mated by a sum:
ai(x) =
Z 1
α=0
∂F (γ(α))
∂γi(α)
∂γi(α)
∂α
dα
= (xi −x′
i)
Z 1
α=0
∂F (˜x)
∂˜xi

˜x=x′+α(x−x′)
dα
≈(xi −x′
i)
m
X
k=1
∂F (˜x)
∂˜xi

˜x=x′+ k
m (x−x′)
1
m
(1)
where γ(α) = x′ + α(x −x′) describes the interpolation path and m is the
number of steps in the approximation that controls how exact the results will
be. In our experiments, we obtained good results using an m of 1000. We used a
zero vector as baseline for the feed-forward network, which represents a molecule
in which all substructures are set to absent.
Alcohol Toy Data Set. As a proof of concept, we investigate if Integrated Gra-
dients can be used to extract interpretable pharmacophores from a feedforward
neural network. For this purpose we have constructed a toy data set which
classiﬁes compounds based on a simple rule: compounds containing an alcohol
group (i.e. a hydroxy group bound to saturated carbon) are classiﬁed as posi-
tive, whereas compounds containing no hydroxy groups and carboxylic acids are
classiﬁed as negative. The data set consists of 28 147 samples including 1 236
positives. The negative samples comprise 26 047 oxygen-free molecules and 864
carboxylic acids. The simplest rule which can be learned is that compounds
without hydroxyl groups are classiﬁed as negative. In a second step a rule has
to be found which discriminates between diﬀerent hydroxyl groups.
In this experiment, we used a fully connected network based on ECFPs of
radius 1. Radius 1 is suﬃcient for this task, because a hydroxyl group bound to
a saturated carbon can be distinguished from a carboxylic acid group. In this
experiment the model consisted of 4 layers of 1 024 units with SELU activation
and achieved a test set AUC of > 0.99. To investigate what was important for
the predictions, we used Integrated Gradients. The feed-forward network is based
on ECFPs, hence Integrated Gradients provide attributions for each ﬁngerprint.
Each ﬁngerprint consists of multiple atoms and one atom is part of multiple
ﬁngerprints. Hence, we calculated the atom-wise attribution as the sum of the
attributions of all ﬁngerprints in which this atom is part of.
Figure 3 shows the attributions for ﬁve randomly selected molecules for each
of the three diﬀerent molecule types. In the top, middle and bottom row nega-
tive samples without a hydroxyl group, negative samples with a carboxylic acid
group and positive samples are displayed, respectively. In the ﬁrst row, almost
all atoms obtain a negative attribution, which is reasonable since non of these
atoms are part of a hydroxyl group. Only in a small fraction (1.9%) of the tested
atoms small positive attributions were observed. In the second row atoms with
carboxylic acids are shown. Atoms not belonging to the acid group are in general


## Page 7


classiﬁed as negative, whereas the hydroxyl group obtains positive attributions.
This means that the network is still able to identify that the hydroxyl group is
important for a positive classiﬁcation. In the third row molecules with hydroxyl
groups are displayed. This group was identiﬁed as positively contributing to the
prediction in 0.83% of the atoms by the network and Integrated Gradients. Due
to the overlapping ﬁngerprints, neighboring atoms are also obtaining a slightly
positive attribution, whereas atoms further away are still clearly identiﬁed as
negative contributions. This toy example has shown that the Integrated Gradi-
ents can be used to extract the rules underlying the classiﬁcation.
After this toy experiment, in which we knew which rules had to be applied to
classify the samples, we will investigate whether the decisions for a more complex
task are still interpretable and reasonable. For this purpose, we used the Tox21
data set.
Tox21 Challenge data set. In this experiment, we investigated whether Inte-
grated Gradients can be used to extract chemical substructures which are im-
portant for classiﬁcation into toxic and non-toxic chemical compounds on the
largest available toxicity data set.
 
 
positive samples
negative samples 
carboxylic acid 
negative samples 
no hydroxyl 
Fig. 3. Attributions assigned to the atoms by the model for the three types of com-
pounds. 5 randomly chosen negative samples without hydroxyl groups, negative sam-
ples with carboxylic acid groups and positive samples are shown in the top, middle
and bottom row, respectively. Dark red indicates that these atoms are responsible for
a positive classiﬁcation, whereas dark blue atoms attribute to a negative classiﬁcation.


## Page 8


0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
0
100
200
300
400
Fig. 4. Illustration of atom-wise attribution for 12 randomly drawn positive Tox21
samples. Attributions were extracted from a model trained on ECFP_2 ﬁngerprints.
The network clearly bases its decision on larger structures, which were built inside the
model out of the small input features.
For this purpose, we trained a fully connected neural network consisting of
4 SELU layers with 2048 hidden units each 1024 ECFPs with radius 1 on the
Tox21 data set. This network achieved a mean test AUC of 0.78. We followed
the same procedure described above which consists of two major steps: applying
Integrated Gradients and summarizing feature-wise attributions into atom-wise
attributions. Figure 4 shows 12 randomly drawn, correctly classiﬁed positive test
samples. It can be observed that positive attributions cluster together and form
substructures. Please note that the model was trained only on small substruc-
tures, hence the formation of the larger pharmacophores is a direct result of
the learning process. Together with the fact that some attributions are negative
or close to zero, this indicates that the neural network is able to focus on cer-
tain atoms and substructures thereby diﬀerentiating between the indicative and
not relevant parts of the input. The substructures on which the network bases
its decision can be viewed as a pharmacophore-like substructure that indicates
toxicity, a so-called “toxicophore”.
Up to now, we have only considered feed-forward neural networks. In the
following sections, we will focus on the second prominent networks used for vir-


## Page 9


tual screen: graph convolutional neural networks. We will show how these net-
works can be used to extract annotated substructures, such as pharmacophores
and toxicophores, rather than focusing on interpreting individual samples. This
knowledge can be helpful for understanding the basic mechanisms of biological
activities.
4
Graph Convolutional Neural Networks
We implemented a new graph convolutional approach which is purely based
on Keras [6] 3. In our approach, we start similar to other approaches [7] with
an initial atom representation which includes the atom type and the present
bond type encoded in a one-hot vector. The network propagates this represen-
tation through several graph convolutional layers, whereas each layer performs
two steps. In the ﬁrst step, neighboring atoms are concatenated to form atom
pairs. The convolutional ﬁlters slide over these atom pairs to obtain a pair rep-
resentation. The second step is a summarization step, in which a new atom
representation is determined. To obtain a new atom representation an order in-
variant pooling operation is performed over the atom-neighbor pairs. This newly
generated representation is then fed into the next convolutional layer. This pro-
cedure is illustrated in Fig. 5 a). For training and prediction a summarization
step which performs a pooling over the atom representations gives a molecular
representation. This step is performed to have a molecular representation with
a ﬁxed number of dimensions so that the molecule can be processed by fully
connected layers. This steps are shown in Fig. 5 b).
Formally, this can be described as following. Let G be a molecular graph with a
set of atom nodes A. Each atom node v is initially represented by a vector h0
v
and has a set of neighboring nodes Nv. In every layer l the representations hl
v
and hl
w are concatenated (., .) if w is a neighboring node of v to form the pair
pl
vw. The pair representation hpvw is the result of the activation function f of
the dot product of the trainable matrix Wl of layer l and the pair pl
vw. The new
atom representation hl+1
v
is obtained as a result of any order invariant pooling
function g such as max, sum or average pooling.
pl
vw = (hl
v, hl
w)
∀w ∈Nv
(2)
hl
pvw = f(pl
vwWl)
(3)
hl+1
v
= g({hl
pvw|w ∈Nv})
(4)
A graph representation hl
G of layer l is obtained through an atom-wise pooling
step.
hl
G = g({hl
v|v ∈A})
(5)
3 The code is available at https://github.com/bioinf-jku/interpretable_ml_
drug_discovery


## Page 10


If skip connections are used, the molecule is represented by a concatenation of
all hl
G.
hG = (h0
G, h1
G, ..., hL
G)
(6)
Otherwise, the representation hL
G of the last layer L is used.
hG = hL
G
(7)
To ensure that our implementation is on the same performance level as other
state of the art graph convolutions, we used the ChEMBL benchmark data set.
For the comparisons we used the same data splits as the original publication [21],
therefore our results are directly comparable. Our approached achieved an AUC
of 0.714 ± 0.15, which is a 3% improvement compared to the best performing
graph convolutional neural network.
Fig. 5. a) illustrates the convolutional steps for the blue and the grey center atoms. A
new atom representation is formed by convolving over the atom pairs and a subsequent
pooling operation. b) shows the graph pooling step which follows the convolutional lay-
ers and the fully connected layers at the end of the network. These steps are performed
in the training and prediction mode. c) displays the forward pass which is performed
to obtain the most relevant substructures. Here, the graph pooling step is omitted and
the substructures are directly fed into the fully connected layers.


## Page 11


4.1
Interpreting convolutional ﬁlters
In this section, we aim at extracting substructures that induce a particular bio-
logical eﬀect. This information is useful for designing new drugs and for identi-
fying mechanistic pathways.
In graph convolutional neural networks the convolutional layers learn to detect
indicative structures, and later fully connected layers combine these substruc-
tures to a meaningful prediction. Our aim is to extract the indicative substruc-
tures which are learned within the convolutional layers. This can be achieved by
skipping the atom-wise pooling step of Eq. 5 and propagating the atom repre-
sentation hl
v through the fully connected layers as depicted in Fig. 5 c). Please
note, that we can skip this step, because pooling over the atoms results again
in a graph representation which has the same dimensions as the single atom
representations. Therefore, we can use the feature representations of individual
atoms in the same way as graph representations. Although the predictions are for
single atoms, each atom was inﬂuenced by its proximity, therefore the scores can
be understood as substructure scores. The receptive ﬁeld of each atom increases
with each convolutional layer by one, therefore hl
v represents substructures of
diﬀerent sizes, depending on how many layers were employed. The substructures
are centered at atom v and have a radius equal to the number of convolutional
layers. Scores close to one indicate that the corresponding substructure is in-
dicative for a positive label, whereas substructures with a score close to zero are
associated with the negative label.
Ames mutagenicity data set For this experiment we used a well studied muta-
genicity data set. This data set was selected because there exist a number of
well-known toxic substructures in the literature which we can leverage to assess
our approach. The full data set was published by [10], of which we used the
subset originally published by [12] as training set and the remaining data as test
set. The training set consisted of 4 337 samples comprising 2 401 mutagenic and
1 936 non mutagenic compounds. The test set consisted in total of 3 315 samples
containing 1 690 mutagens and 1 625 non mutagens. We trained a network with
3 convolutional layers with 1 024 ﬁlters each followed by a hidden fully connected
layer consisting of 512 units. The AUC of the model on the test set was 0.804.
To assess which substructures were most important for the network, we prop-
agated a validation set through the network and calculated the scores for each
substructure as described above. The most indicative substructures are shown in
Figure 6. Each substructure is displayed together with its SMILES representa-
tion and its positive predictive value (PPV) on the test set. These extracted sub-
structures coincide very well with previous ﬁndings in the literature [12,23,34].
In Figure 7 some genotoxic structures found in the literature are displayed with
a matching substructure identiﬁed by our method. The extracted substructures
are known to interact with the DNA. Most of the them form covalent bonds with
the DNA via uni-molecular and bi-molecular nucleophilic substitions (SN-1 and
SN-2 reactions). Subsequently these modiﬁcations can lead severe DNA damage
such as base loss, base substitutions, frameshift mutations and insertions [23].


## Page 12


Within this section we have demonstrated that our method for interpreting graph
convolutional neural networks yield toxicophores consistent with literature ﬁnd-
ings and the mechanistic understanding of DNA damage.
5
Discussion
Having a black box model with high predictive performance is often insuﬃcient
for drug development: a chemist is not able to derive an actionable hypothesis
from just a classiﬁcation of a molecule into “toxic” or “not toxic”. However, once
a chemist “sees” the structural elements in a molecule responsible for a toxic
eﬀect, he immediately has ideas how to modify a molecule to get rid of these
structural elements and thus the toxic eﬀect. Therefore it is an essential goal is
to gain additional knowledge and therefore it is necessary to shed light onto the
decision process within the neural network and to retrieve the stored informa-
tion. In this work, we have shown that the layers of a neural network construct
toxicophores and that larger substructures are constructed in the higher layers.
Furthermore, we have demonstrated that Integrated Gradients is an adequate
method to determine the indicative substructures in a given molecule. Addition-
ally, we propose a method to identify the learned toxicophores within a trai,ned
network and demonstrated that these extracted substructures are consistent with
the literature and chemical mechanisms.


## Page 13


c
test PPV: 0.83
SMILES: cc(c)N=[N+]=[N-]
c
test PPV: 0.83
SMILES: ccc(cc)N=[N+]=[N-]
c
test PPV: 1.00
SMILES: Cc1ccc(o1)[N+](=O)[O-]
c
test PPV: nan*
SMILES: Cc1csc(c1)[N+](=O)[O-]
c
test PPV: nan*
SMILES: CC(C)OS(C)(=O)=O
c
test PPV: 0.75*
SMILES: CCN(CC)N(O)N=O
c
test PPV: nan*
SMILES: cc(c)-c1c(oc(C)c1-c)[N+](=O)[O-]
c
test PPV: 0.75*
SMILES: CCOS(C)(=O)=O
c
test PPV: 1.00*
SMILES: CN(C)N(O)N=O
c
test PPV: 0.86
SMILES: CCN(N=O)C(=O)O
c
test PPV: 0.79
SMILES: CCN(N=O)C(N)=O
c
test PPV: nan*
SMILES: [NH3+]OCC(CO[NH3+])O[N+](=O)[O-]
c
test PPV: 1.00*
SMILES: CC1(O)C=C(C=O)C2(CC2(C)C1)C(O)O
c
test PPV: 0.92
SMILES: cN=[N+]=[N-]
c
test PPV: nan*
SMILES: O=CC(Cl)=C(Cl)C(=O)O
c
test PPV: 1.00*
SMILES: COCC1CO1
c
test PPV: 0.96
SMILES: CC(C)ON=O
c
test PPV: 1.00*
SMILES: cOCC1CO1
c
test PPV: 0.80
SMILES: CC=C(Cl)C=O
c
test PPV: 0.25*
SMILES: CCSC(Cl)=C(Cl)Cl
c
test PPV: 0.80
SMILES: ccc(oc)[N+](=O)[O-]
c
test PPV: 0.86
SMILES: coc(c(c)-c)[N+](=O)[O-]
c
test PPV: 0.80
SMILES: CC(C)OC1CC(C)(O)CC(C)O1
c
test PPV: 0.80
SMILES: CCC12OC1(C(=O)NC2(C)O)C(=O)OC
Fig. 6. This ﬁgure displays the structures extracted with our approach from the graph
convolutional neural network. Below the structures the corresponding SMILES repre-
sentation is shown together with the positive predictive value (PPV) on the test set.
PPVs which were calculated on less than 5 samples are marked with an asterisk.


## Page 14


toxicophore name
structure example
matching structure identified by 
our interpretability approach
azide
aromatic nitro
sulfonic ester
nitros amine
epoxide
monohaloalkene
alkyl nitrite
Fig. 7. This ﬁgure shows annotated SMARTS patterns identiﬁed in the literature as
mutagenic together with matching structures identiﬁed by our interpretability ap-
proach. The names of the structures are shown in the ﬁrst column, the SMARTS
patterns found in literature are displayed in the second column and the last column
shows a matching example of the top scoring substructures identiﬁed by our method.


## Page 15


References
1. Ancona, M., Ceolini, E., Öztireli, C., Gross, M.: Towards better understanding of
gradient-based attribution methods for deep neural networks. International Con-
ference on Learning Representations (ICLR) (2018)
2. Baehrens, D., Schroeter, T., Harmeling, S., Kawanabe, M., Hansen, K., Müller,
K.R.: How to explain individual classiﬁcation decisions. J. Mach. Learn. Res. 11,
1803–1831 (Aug 2010), http://dl.acm.org/citation.cfm?id=1756006.1859912
3. Bau, D., Zhou, B., Khosla, A., Oliva, A., Torralba, A.: Network dissection: Quan-
tifying interpretability of deep visual representations. In: Proceedings of the IEEE
Conference on Computer Vision and Pattern Recognition. pp. 6541–6549 (2017)
4. Bengio, Y.: Deep learning of representations: Looking forward. In: Proceedings of
the First International Conference on Statistical Language and Speech Processing.
pp. 1–37. SLSP’13, Springer-Verlag, Berlin, Heidelberg (2013)
5. Cherkasov, A., Muratov, E.N., Fourches, D., Varnek, A., Baskin, I.I., Cronin, M.,
Dearden, J., Gramatica, P., Martin, Y.C., Todeschini, R., Consonni, V., Kuz’min,
V.E., Cramer, R., Benigni, R., Yang, C., Rathman, J., Terﬂoth, L., Gasteiger, J.,
Richard, A., Tropsha, A.: QSAR modeling: Where have you been? where are you
going to? Journal of Medicinal Chemistry 57(12), 4977–5010 (jan 2014)
6. Chollet, F.: Keras. https://keras.io (2015)
7. Duvenaud, D.K., Maclaurin, D., Iparraguirre, J., Bombarell, R., Hirzel, T., Aspuru-
Guzik, A., Adams, R.P.: Convolutional networks on graphs for learning molecular
ﬁngerprints. In: Cortes, C., Lawrence, N.D., Lee, D.D., Sugiyama, M., Garnett,
R. (eds.) Advances in Neural Information Processing Systems 28, pp. 2224–2232.
Curran Associates, Inc. (2015)
8. Gilmer, J., Schoenholz, S.S., Riley, P.F., Vinyals, O., Dahl, G.E.: Neural message
passing for quantum chemistry. In: Precup, D., Teh, Y.W. (eds.) Proceedings of
the 34th International Conference on Machine Learning. Proceedings of Machine
Learning Research, vol. 70, pp. 1263–1272. PMLR, International Convention Cen-
tre, Sydney, Australia (06–11 Aug 2017)
9. Hansen, K., Baehrens, D., Schroeter, T., Rupp , M., Müller, K.R.: Visual inter-
pretation of kernel-based prediction models. Molecular Informatics 30(9), 817–826
(sep 2011)
10. Hansen, K., Mika, S., Schroeter, T., Sutter, A., ter Laak, A., Steger-Hartmann, T.,
Heinrich, N., M"uller, K.R.: Benchmark data set for in silico prediction of ames
mutagenicity. Journal of Chemical Information and Modeling 49(9), 2077–2081
(sep 2009)
11. Huang, R., Sakamuru, S., Martin, M., Reif, D., Judson, R., Houck, K., Casey, W.,
Hsieh, J., Shockley, K., Ceger, P., et al.: Proﬁling of the tox21 10k compound li-
brary for agonists and antagonists of the estrogen receptor alpha signaling pathway.
Scientiﬁc reports 4 (2014)
12. Kazius, J., McGuire, R., Bursi, R.: Derivation and validation of toxicophores for
mutagenicity prediction. Journal of Medicinal Chemistry 48(1), 312–320 (2005)
13. Kearnes, S., McCloskey, K., Berndl, M., Pande, V., Riley, P.: Molecular graph
convolutions: moving beyond ﬁngerprints. Journal of Computer-Aided Molecular
Design 30(8), 595–608 (aug 2016)
14. Klambauer, G., Unterthiner, T., Mayr, A., Hochreiter, S.: Self-normalizing neural
networks. Advances in Neural Information Processing Systems 30 (NIPS) (2017)
15. Lavecchia, A.: Machine-learning approaches in drug discovery: methods and appli-
cations. Drug Discovery Today 20(3), 318 – 331 (2015)


## Page 16


16. Lin, S.: Pharmacophore perception, development and use in drug design. edited by
osman f. güner. Molecules 5(7), 987–989 (2000)
17. Lionta, E., Spyrou, G., K. Vassilatis, D., Cournia, Z.: Structure-based virtual
screening for drug discovery: Principles, applications and recent advances. Cur-
rent Topics in Medicinal Chemistry 14(16), 1923–1938 (2014)
18. Lounkine, E., Keiser, M.J., Whitebread, S., Mikhailov, D., Hamon, J., Jenkins,
J.L., Lavan, P., Weber, E., Doak, A.K., Cote, S., Shoichet, B.K., Urban, L.:
Large-scale prediction and testing of drug activity on side-eﬀect targets. Nature
486(7403), 361–367 (Jun 2012). https://doi.org/10.1038/nature11159
19. Ma, J., Sheridan, R.P., Liaw, A., Dahl, G.E., Svetnik, V.: Deep neural nets as
a method for quantitative structure–activity relationships. Journal of Chemical
Information and Modeling 55(2), 263–274 (2015)
20. Mayr, A., Klambauer, G., Unterthiner, T., Hochreiter, S.: Deeptox: Toxicity pre-
diction using deep learning. Frontiers in Environmental Science 3, 80 (2016)
21. Mayr, A., Klambauer, G., Unterthiner, T., Steijaert, M., Wegner, J.K., Ceulemans,
H., Clevert, D.A., Hochreiter, S.: Large-scale comparison of machine learning meth-
ods for drug target prediction on chembl. Chemical science 9(24), 5441–5451 (2018)
22. Olivecrona, M., Blaschke, T., Engkvist, O., Chen, H.: Molecular de-novo design
through deep reinforcement learning. Journal of cheminformatics 9(1), 48 (2017)
23. Plošnik, A., Vračko, M., Dolenc, M.S.: Mutagenic and carcinogenic structural alerts
and their mechanisms of action. Archives of Industrial Hygiene and Toxicology
67(3), 169–182 (sep 2016)
24. Preuer, K., Lewis, R.P.I., Hochreiter, S., Bender, A., Bulusu, K.C., Klambauer,
G.: DeepSynergy: predicting anti-cancer drug synergy with deep learning. Bioin-
formatics 34(9), 1538–1546 (dec 2017)
25. Preuer, K., Renz, P., Unterthiner, T., Hochreiter, S., Klambauer, G.: Fréchet
ChemNet distance: A metric for generative models for molecules in drug discovery.
Journal of Chemical Information and Modeling 58(9), 1736–1741 (aug 2018)
26. Rogers, D., Hahn, M.: Extended-connectivity ﬁngerprints. Journal of Chemical
Information and Modeling 50(5), 742–754 (May 2010)
27. Schütt, K.T., Arbabzadah, F., Chmiela, S., Müller, K.R., Tkatchenko, A.:
Quantum-chemical insights from deep tensor neural networks. Nature Commu-
nications 8, 13890 (jan 2017)
28. Segler, M.H., Kogej, T., Tyrchan, C., Waller, M.P.: Generating focused molecule
libraries for drug discovery with recurrent neural networks. ACS Central Science
(2017)
29. Sundararajan, M., Taly, A., Yan, Q.: Axiomatic attribution for deep networks.
Proceedings of the 34th International Conference on Machine Learning (ICML)
(2017)
30. Sushko, I., Salmina, E., Potemkin, V.A., Poda, G., Tetko, I.V.: Toxalerts: A web
server of structural alerts for toxic chemicals and compounds with potential adverse
reactions. Journal of Chemical Information and Modeling 52(8), 2310–2316 (2012)
31. Unterthiner, T., Mayr, A., Klambauer, G., Steijaert, M., Wegner, J.K., Ceulemans,
H., Hochreiter, S.: Multi-task deep networks for drug target prediction. In: Work-
shop on Transfer and Multi-task Learning of NIPS2014. vol. 2014, pp. 1–4 (2014)
32. Unterthiner, T., Mayr, A., Klambauer, G., Steijaert, M., Wenger, J., Ceulemans,
H., Hochreiter, S.: Deep learning as an opportunity in virtual screening. Deep
Learning and Representation Learning Workshop (NIPS 2014) (2014)
33. Unterthiner, T., Nessler, B., Klambauer, G., Heusel, M., Ramsauer, H., Hochreiter,
S.: Coulomb GANs: Provably optimal nash equilibria via potential ﬁelds. Interna-
tional Conference of Learning Representations (ICLR) (2018)


## Page 17


34. Yang, H., Li, J., Wu, Z., Li, W., Liu, G., Tang, Y.: Evaluation of diﬀerent methods
for identiﬁcation of structural alerts using chemical ames mutagenicity data set as
a benchmark. Chemical Research in Toxicology 30(6), 1355–1364 (may 2017)
35. Yang, X., Zhang, J., Yoshizoe, K., Terayama, K., Tsuda, K.: ChemTS: an eﬃ-
cient python library for de novo molecular generation. Science and Technology of
Advanced Materials 18(1), 972–976 (2017)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1903_02788v2_interpretable_deep_learning_in_drug_discovery
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1903_02788V2_INTERPRETABLE_DEEP_LEARNING_IN_DRUG_DISCOVERY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
