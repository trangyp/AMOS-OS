---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1306.4447v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1306.4447v1_Hacking_Smart_Machines_with_Smarter_Ones__How_to_Extract_Meaningful_Data_from_Ma

> Source: 1306.4447v1_Hacking_Smart_Machines_with_Smarter_Ones__How_to_Extract_Meaningful_Data_from_Ma.pdf

> Pages: 30

---


## Page 1


arXiv:1306.4447v1  [cs.CR]  19 Jun 2013
Hacking Smart Machines with Smarter Ones:
How to Extract Meaningful Data from Machine
Learning Classiﬁers
Giuseppe Ateniese1, Giovanni Felici2, Luigi V. Mancini1, Angelo Spognardi1,
Antonio Villani3, and Domenico Vitali1
1 Universit`a di Roma La Sapienza, Dipartimento di Informatica
{ateniese,mancini,spognardi,vitali}@di.uniroma1.it
2 Consiglio Nazionale delle Ricerche, Istituto di Analisi dei Sistemi ed Informatica
Roma giovanni.felici@iasi.cnr.it
3 Universit`a di Roma Tre, Dipartimento di Matematica villani@mat.uniroma3.it
Abstract. Machine Learning (ML) algorithms are used to train com-
puters to perform a variety of complex tasks and improve with experi-
ence. Computers learn how to recognize patterns, make unintended deci-
sions, or react to a dynamic environment. Certain trained machines may
be more eﬀective than others because they are based on more suitable
ML algorithms or because they were trained through superior training
sets. Although ML algorithms are known and publicly released, training
sets may not be reasonably ascertainable and, indeed, may be guarded
as trade secrets. While much research has been performed about the
privacy of the elements of training sets, in this paper we focus our at-
tention on ML classiﬁers and on the statistical information that can be
unconsciously or maliciously revealed from them. We show that it is pos-
sible to infer unexpected but useful information from ML classiﬁers. In
particular, we build a novel meta-classiﬁer and train it to hack other clas-
siﬁers, obtaining meaningful information about their training sets. This
kind of information leakage can be exploited, for example, by a vendor
to build more eﬀective classiﬁers or to simply acquire trade secrets from
a competitor’s apparatus, potentially violating its intellectual property
rights.
1
Introduction
Machine learning classiﬁers are designed to make eﬀective and eﬃcient predic-
tion of “patterns” from large data sets. Many applications have been proposed in
the literature (e.g., [27, 54, 49, 23, 25]) and machine learning algorithms pervade
several contexts of information technology. ML approaches (such as Support
Vector machines, Clustering, Bayesian network, Hidden Markov models, etc.)
rely on quite distinct mathematical concepts but generally they are employed
to solve similar problems. A machine learning algorithm consists of two phases:
training and classiﬁcation. During the training, the ML algorithm is fed with
a training set of samples. In this phase, the relationships and the correlations


## Page 2


implied in the training samples are gathered inside the model. Afterwards, the
model is used during the classiﬁcation phase to classify and evaluate new data.
ML classiﬁers are usually able to manage a large amount of data and to adapt
to dynamic environments. Their versatility makes them suitable for several im-
portant tasks. For example, classiﬁcation and regression models are employed
to analyze current and historical trends to make predictions in ﬁnancial mar-
kets [24, 33, 8], to study biological problems [54], to support medical diagnosis
[30, 42, 57], to classify network traﬃc or detect anomalies [22, 28, 39, 12, 49].
One may think that it is safe to release a classiﬁer, whether in hardware or
software, since intellectual property laws would prevent anyone from producing
a similar apparatus, for example, by copying its code or its design principles.
However, releasing a trained classiﬁer may be subject to unexpected informa-
tion leakages that make it possible to produce a competitive product without
violating any intellectual property rights.
Let us consider, for instance, a classiﬁer Ca that is less eﬀective than a classiﬁer Cb
produced by a competitor. The ML algorithms used in Cb may be publicly avail-
able or be inferred through reverse engineering. For example, commercial soft-
ware products for speech recognition, such as Nuance Dragon NaturallySpeak-
ing [1], utilize widely studied Hidden Markov Models. These algorithms, along
with their optimizations, are well-understood and quite standard. Thus, the com-
mon assumption is that anyone can easily replicate them. In particular, we could
assume that the training set used for Cb is superior, in the sense that makes Cb
more eﬀective than Ca even though both implement essentially the same ML
algorithms. What makes Cb better than Ca is the speciﬁc knowledge formed dur-
ing the training phase, inferred by the training set. For instance, a classiﬁer that
makes stock market predictions based on neural network holds its power in the
weights at its hidden layer (see A). But those weights depend exclusively on the
training set, hence valuable information that must be treasured.
Thus, it is fair to ask: Is it safe to release a proﬁtable ML classiﬁer? Would
selling a software/hardware classiﬁer reveal concrete hints about its training set,
uncovering the secrets of its eﬀectiveness and jeopardizing the vendor?
We show that a classiﬁer can be hacked and that it is possible to extract
from it meaningful information about its training set. This can be accomplished
because a typical ML classiﬁer learns by changing its internal structure to ab-
sorb the information contained in the training data. In particular, we devise and
train a meta-classiﬁer that can successfully detect and classify these changes and
deduce valuable information. However, we could not report on products released
by commercial vendors because we did not get legal permission to hack a propri-
etary product. Nevertheless, we analyzed the same ML algorithms employed by
commercial products. For example, we considered the HMM-based speech recog-
nition engine of the open-source package VoxForge which is similar to the ones
employed by commercial products, such as Nuance Dragon NaturallySpeking.
We note, in addition, that using open-source software makes our experiments
easily reproducible by others.


## Page 3


It is important to observe that we are not interested in privacy leaks, but
rather in discovering anything that makes classiﬁers better than others. In partic-
ular, we do not care about protecting the elements of the training set. Consider
the following example: a speech recognition software recognizes spoken words
better than competing products, even though they all implement the same ML
algorithms. The training set is composed of commonly spoken words, thus it
does not make sense to talk about privacy protection. However, we show how
to build a meta-classiﬁer trained to reveal that, for instance, the majority of
training samples came from female voices or from voices of people with marked
accents (e.g., Indian, British, American, etc.). Then, we can extrapolate certain
hidden attributes which are somehow absorbed by the learning algorithm, thus
possibly uncovering the secret sauce that makes the speech recognition software
stay ahead of the competition.
Therefore the type of leakage we are interested in is quite diﬀerent than that
considered in privacy preserving data mining and statistical databases [14] or
diﬀerential privacy [9, 19]. Indeed, in Section 4, we show that a system providing
Diﬀerential Privacy is utterly insecure in our model.
Remark: We introduce a novel type of information leakage and show that it
is inherent to learning. This is far from obvious and, indeed, quite unexpected:
Clearly, all learning algorithms must recognize patterns in their dataset. Thus,
classiﬁers will inherently reveal some information. The open question is whether
this information has any meaning. Indeed, classiﬁers are very opaque objects
and make it diﬃcult to infer anything useful at all. What we show here is that
it is still possible to extract something meaningful relating to properties of the
training set. This is surprising and achievable through a meta-classiﬁer that is
specially trained to expose this information. However, we do not attempt to
formally deﬁne this new type of information leakage nor provide mechanisms to
prevent it.
1.1
Contributions
Our results evince realistic issues facing machine learning algorithms. In partic-
ular, the main contributions of our work are:
1. We put forward a new type of information leakage that, to the best of our
knowledge, has not been considered before. We show that it is unsafe to
release trained classiﬁers since valuable information about the training set
can be extracted from them.
2. We propose a way to leverage the above information leakage, devising a gen-
eral attack strategy that can be used to hack ML classiﬁers. In particular, we
deﬁne a model for a meta-classiﬁer that can be trained to extract meaningful
data from targeted classiﬁers.
3. We describe several attacks against existing ML classiﬁers: we successfully
attacked an Internet traﬃc classiﬁer implemented via Support Vector Ma-
chines (SVMs) and a speech recognition software based on Hidden Markov
Models (HMMs).


## Page 4


We believe existing classiﬁers, whether commercial products or prototypes re-
leased to the research community, are susceptible to our general attack strategy.
We put forward the importance of protecting the training set and of the need for
novel machine learning techniques that would prevent determined competitors
from probing a ML classiﬁcator and learning trade secrets from it.
1.2
Organization of this paper
The rest of the paper is organized as follows: Section 2 describes the problem and
introduces an attack methodology that makes use of a ML model. Section 3 shows
how we successfully applied our proposed methodology to hack trained SVM and
HMM classiﬁers. In Section 4 we analyze the behavior of our attack methodology
when the training set is provided through diﬀerential privacy. Section 5 contains
some related works. Section 6 concludes our work with some remarks.
2
Hacking Machine Learning classiﬁers
In this paper we are interested in Machine Learning algorithms used for classi-
ﬁcation purposes, such as Internet traﬃc classiﬁers, speech recognition systems,
or for ﬁnancial market predictions. Our goal is to hack a trained classiﬁer to
obtain information that was implicitly absorbed from the elements the classiﬁer
received as input.
Consider for instance the Artiﬁcial Neural Networks (ANNs) based on Multi-
layer perceptron (please refer to A for details about this algorithm). Consider a
simple neural network that has to learn the identity function over a vector of
eight bits, only one of them set to 1 (this example is taken from the popular
book of Mitchell [47]). The network has a ﬁxed structure with eight input neu-
rons, three hidden units and eight output neurons. Using the backpropagation
algorithm over the eight possible input sequences, the network eventually learns
the target function. By examining the weights of the three hidden units, it is
possible to observe how they actually encode (in binary) eight distinct values,
namely all possible sequences over three bits (000, 001, 010, . . ., 111). The exact
values of the hidden units for one typical run of the backpropagation algorithm
are shown in Table 1. Basically, the hidden units of the network were able to
capture the essential information from the eight inputs, automatically discover-
ing a way to represent the inputs. Thus, it is possible to extract the (possibly
sensitive) cardinality of the training set by just looking at the trained network.
In the following section, we describe a method to extract this type of sensitive
information. Namely, we show in Section 3.2 that it is possible to determine if
a certain type of network traﬃc was included in the training set of an Internet
classiﬁer trained on Cisco network data ﬂows [53]. Similarly, we hacked a speech
recognition system and were able to determine the accent of speakers employed
during its training. This case study is reported in Section 3.1.


## Page 5


Input
Hidden Values
Output
10000000 →
.89 .04 .08
→10000000
01000000 →
.15 .99 .99
→01000000
00100000 →
.01 .97 .27
→00100000
00010000 →
.99 .97 .71
→00010000
00001000 →
.03 .05 .02
→00001000
00000100 →
.01 .11 .88
→00000100
00000010 →
.80 .01 .98
→00000010
00000001 →
.60 .94 .01
→00000001
Table 1. The weights of the hidden states, taken from Figure 4.7 of [47]
2.1
An attack strategy
In this section we devise a general attack strategy against a trained classiﬁer
that can make an attacker able to discover some statistical information about
the training set.
We deﬁne the training dataset D as a multiset where all the elements are couples
of the form {(a, l)|a = ⟨a1, a2, . . . , an⟩}; to simplify, we can assume without loss
of generality that ai ∈{0, 1}m, and l ∈{0, 1}ν. Each training element a is
represented as a vector of n features (the values ai of the vector) and has an
associated classiﬁcation label l. C is a generic machine learning classiﬁer trained
on D: it could be an Artiﬁcial Neural Network (ANN), a Hidden Markov Model
(HMM) or a simple Decision Tree (DT).
We assume that C is disclosed after the end of the training phase. This means that
in our model the adversary cannot taint C during the learning process. Instead,
we assume that the adversary is able to arbitrarily modify the behavior of C
during the classiﬁcation process. In fact, when C is disclosed, it includes the set
of instructions for the classiﬁcation task as well as the model deﬁnition; hence,
both the data structures and the instruction sequences are completely in the
hand of the adversary. The assumption that the adversary has complete access
to the classiﬁer is reasonable since it is possible to extract the plain classiﬁer also
from a binary executable through, for instance, dynamic analysis techniques [13].
Each classiﬁer C can be encoded in a set of feature vectors that can be used as
input to train a meta-classiﬁer MC. The set of feature vectors that represents
C are denoted by FC. For example, in the case of an SVM, the set FC would
contain the list of all the support vectors of the classiﬁer C.
In Figure 1, Cx is the trained classiﬁer that the adversary wants to examine
in order to infer some statistical information about the training set Dx. Let P
be the property that the adversary wants to learn about the undisclosed Dx.
We write P ≈D to say that the property P is preserved by the dataset D.
For instance, in the context of medical diagnosis applications, P could be: the
entries of the training set are equally balanced between males and females. To
discern whether P ≈Dx, the adversary can build a meta-classiﬁer MC, that is a
classiﬁer trained over a particular dataset DC composed of the elements a ∈FCi
labeled with l ∈{P, P}. The label is assigned according to the nature of the


## Page 6


Fig. 1. Attack methodology: the target training set Dx produced Cx. Using several
training sets D1, . . . , Dn with or without a speciﬁc property, we build C1, . . . , Cn, namely
the training set for the meta-classiﬁer MC that will classify Cx.
dataset used to train the classiﬁer Ci.
To train MC the adversary has to build the training set ﬁrst. For this purpose,
the adversary generates a vector of speciﬁc datasets D = (D1, . . . , Dn) in such
way that D contains a (possibly) balanced amount of instances reﬂecting P and
P. After this step, he trains the meta-classiﬁer MC as described in Algorithm 1.
The algorithm takes as input the created training sets D and their corresponding
labels. It starts with an empty data set (line 3). Then, it trains a classiﬁer Ci on
each created data set (line 5) and gets the representation of the classiﬁer as a
set of feature vectors (line 6). Then, it adds each feature vector to the dataset
DC (line 8). Finally, it trains the meta-classiﬁer using the resulting data set DC
(line 11).
Next, the adversary uses the meta-classiﬁer MC on FCx to predict which class
lx the classiﬁer Cx belongs to. This is already a new form of information leakage
since the adversary learns whether the original training data Dx preserves P or
not.
In practice, thanks to our attack, we are able to infer any key statistical property
P preserved by the training set performing a sort of brute-force attack on the
set of properties.
It is important to remark that with this methodology the adversary extracts
external information, NOT in the form of attributes of the dataset Dx. These
are essentially statistical properties inferred from the relationship among dataset
entries. For example, in Section 3.1 we show how to attack a speech recognition
classiﬁer by extracting information about the accent of the speakers. This in-
formation is not supposed to be captured explicitly by the model nor it is an
attribute of the training set.
To further improve the quality of the classiﬁcation process, some ﬁlters can
be applied to the set DC of models resulting from the training phase. The ﬁlters
depend on the problem domain and are used to ﬁnd optimal models for the


## Page 7


Input:
D: the array of training sets
l: the array of labels, where each li ∈{P, P}
Output: The meta-classiﬁer MC
1 TrainMC(D,l)
2 begin
3
DC = {∅}
4
foreach Di ∈D do
5
Ci ←train(Di)
6
FCi ←getFeatureVectors(Ci)
7
foreach a ∈FCi do
8
DC = DC ∪{a, li}
9
end
10
end
11
MC ←train(DC)
12
return MC
13 end
Algorithm 1: Training of the meta-classiﬁer
property P and get rid of less signiﬁcant entries. In some cases (as the example
in Section 3.2), this step can be simply assimilated into the training phase of
the meta-classiﬁer. In other cases, as the example in Section 3.1, we will discuss
a ﬁlter realized with the Kullback-Leibler divergence [43].
3
Case studies
In this section we provide two examples of attacks performed according with the
methodology introduced in Section 2.1. We probe two complex systems, one of
which is largely used by software vendors and research communities. As our ﬁrst
example, we attack a Speech Recognition system realized by Hidden Markov
Models; later, we consider a network traﬃc classiﬁer implemented by Support
Vector Machines. Our experiments are performed using Weka ([56]).
In each experiment, we use Decision Tree as meta-classiﬁer MC (more details
on Decision Tree are reported in B); we always use the C4.5’s implementation,
namely J48 module, included within the Weka framework. Clearly, the attack
could be replicated using meta-classiﬁers based on other ML algorithms.
The evaluation of our experiments is performed using standard metrics: (1) re-
call, that is the true positive rate, and (2) precision, that is the ratio of true
positive and the total number of positive predictions of the model.
Furthermore, (3) accuracy, namely the rate of correct predictions made by the
classiﬁer over the number of instances of the entire data set, can be easily derived
from the confusion matrices in Sections 3.1 and 3.2.
In order to evaluate the eﬀectiveness of our attack strategy, we crafted several


## Page 8


classiﬁers trained on strongly biased training sets. These classiﬁers would prob-
ably obtain very low performance during the classiﬁcation phase; as such, they
would be unlikely employed in a commercial product. Moreover, in our experi-
ments, we decided to focus on simple binary properties. Our aims are to provide
an attack strategy that could be easily generalized and to demostrate that it is
possible to infer information on the training set looking at the weights learned
by a classiﬁer.
Attacking commercial products is only a matter of tuning the generation of the
sets D1, . . . , Dn according to more complex properties.
To evaluate our attack strategy we make two assumptions: 1) the adversary
knows which machine learning algorithm is employed by the target 2) the adver-
sary has complete access to the classiﬁer. We claim that these two assumptions
are reasonable. In fact, the information about what algorithms are employed is
not considered a sensitive information, and sometimes it is advertised by the
vendor itself; for instance, the newest version of the NaturallySpeaking engine
(which is the version 12 at the time of writing) leverages HMM and ﬁve-grams to
perform speech recognition and this information can be gathered from Nuance’s
website and patents.
For what concerns the second assumption, note that in many cases vendors need
to hand out their classiﬁers to end-users embedding them within the software
executable or apparatuses; as such, an adversary would be able to extract the
classiﬁer using, for instance, techniques based on dynamic binary analysis. Per-
forming this type of analysis is orthogonal to our attack methodology and is out
of the scope of this work.
It is worth remarking that the structure of the training set (e.g., the list of at-
tributes) is not necessary to perform our attack; indeed, we are interested on
the external information about the training data and we do not consider the
attribute values.
3.1
Hidden Markov Models
Background A Markov Model is a stochastic process that can be represented
as a ﬁnite state machine in which the transition probability depends only on
the current state and is independent from any prior (and future) state of the
process. An Hidden Markov Model, introduced in [16], is a particular type of
Markov Model for modeling sequences that can be characterized by an underly-
ing process generating an observable sequence. Indeed, only the outputs of the
states are observed (the actual sequence of the states of the process cannot be
directly observed). One of the most elegant examples to describe HMMs was
conceived by Jason Eisner [26]: Suppose that, in the year 2799, a climate scien-
tist is studying the weather in Baltimore Maryland for the summer of 2007 by
examining a diary, which had recorded how many ice creams were eaten by Jason
every day of that summer. Only using this record (the observable sequence), is
it possible to estimate with a good approximation the daily temperature (the
hidden sequence). HMMs solve the sequential learning problem that is a special
learning problem where the data domain is sequential by its nature (e.g. speech


## Page 9


recognition problem). In Figure 2, a simple model M is represented that can be
2
q
3
q
1
q
Fig. 2. An example of Hidden Markov Model with three states.
described by:
– a set of hidden states Q = q1, q2, ..., qm
– a transition probability matrix
A =


a11 a12 . . . a1m
a21 a22 . . . a2m
...
...
...
...


where the element ai,j represents the probability of moving from state i to
state j
– an emission probability matrix B(m × n), where the element bj,k is the
probability to produce the observable ok from the state j, that is
bj,k = Bj(k) = P(ok|qj)
The HMM model is based on two main assumptions. The ﬁrst is the Markov
assumption, namely that given a sequence x1, . . . , xi−1 of transitions between
states, the probability of the next state depends only on the present state:
P(xi = qj|x1, x2, . . . , xi−1) = P(xi = qj|xi−1)
The second is the output independence assumption, namely that given a se-
quence x1, . . . , xT of transitions between states, where xi = qj, and the observed
sequence y1, . . . , yT , the emission probability of any observable ok depends only
on the present state and not on any other state or observable:
P(yi = ok|x1, . . . , xi, . . . , xT , y1, . . . , yT ) = P(ok|qj)
In Figure 2, three states (q1, q2 and q3) are shown: the transition probabilities
aij, and, for the three states, the emission probabilities (B1, B2, B3 respectively)
of the three observable (o1, o2, o3).


## Page 10


The HMM models are well-suited to solve three types of problems: likelihood,
decoding and learning [38]. Likelihood problems are related to evaluating the
probability of observing a given observable sequence y1, . . . , yT , given a complete
HMM model, where both matrices A and B are known. Decoding problems call
for the evaluation of the best sequence of hidden states x1, . . . , xT that can have
produced a given observable sequence y1, . . . , yT . Learning problems consist of
reconstructing the two matrices A and B of an HMM, given the set of states Q
and one (or more) observation sequence Y . For this task, the Viterbi and the
Baum-Welch algorithms are used respectively to train and tune the HMM.
HMM for speech recognition In this section we describe the attack to the
HMM in the speciﬁc case of Speech Recognition Engines (SRE). Speech Recogni-
tion (SR) is the process of converting a sound recorded through an acquisition
hardware to a sequence of written words. The applications of SR are manyfold:
dictation, voice search, hands-free command execution, audio archive searching,
etc. The predominant technology used to perform this task is the HMM [37],
many tools are nowadays available ([5, 41]).
We exploited our methodology to verify whether the HMM was trained with a
biased training set: according to the methodology described in 2.1, we are able
to detect with high conﬁdence whether the HMM was trained only with people
from the same nationality. To recognize a speech, SREs require two types of
input:
– an Acoustic Model, which is created by taking speech audio ﬁles, i.e., the
speech corpus, and their transcriptions, and combing them into a statistical
representation of the sounds that make up each word;
– and either a Language Model or a Grammar File. Both describe the set of
words that the statistical model will be able to classify. However, the ﬁrst
model contains the probabilities of sequences of words, while the second con-
tains a set of predeﬁned combinations of words. In the following experiment,
this paper uses only the Language Model.
Let us brieﬂy introduce the typical SRE workﬂow. An unknown speech waveform
is captured by the acquisition hardware, the Pulse Code Modulation provides the
digital representation of the analogical audio signal. This bitstream is now con-
verted in mel-frequency cepstral coeﬃcients (MFCCs), namely a representation
of the short-term power spectrum of sounds. The MFCCs are the observables of
a Hidden Markov Model that changes state over time and that generates one (or
more) observables once it enters into a new state.
In this scenario, the states of the HMM are all the possible subphonemes of
the language while the transition matrix contains the probability for each sub-
phoneme to cycle over itself or to move to the next subphoneme. The emission
probabilities are the probability to observe a certain MFCC from each sub-
phoneme. The only possible transitions between the states of each phonemes
are to themselves or to successive states, in a left-to-right fashion; the self-
loops makes it possible to deal with the variable length of each phoneme with


## Page 11


ease. Both transition and emission probabilities are built using the Viterbi algo-
rithm [32] over a large speech corpus.
Since the MFCC ﬁles are vectors of real-valued numbers, they are approximated
by the multivariate Gaussians distribution (note that the probability to have
exactly the same vector would be nearly 0). For any diﬀerent state (i.e., sub-
phoneme), each dimension of the vector has a certain mean and variance that
represent the likelihood of an individual acoustic observation from that state.
For the sake of our experiments, we build the Hidden Markov Models using
the Hidden Markov Model Toolkit (HTK) [60] toolkit. HTK consists of a set
of library modules and tools available in C. The HTK toolkit provides a high
level of modularity and is organized through a set of libraries with functions
(e.g., HMem for memory management, HSigP for signal processing ,. . . ) and a
small core. The MFCC ﬁles were gathered from the VoxForge project [2], the
most important speech corpus and acoustic model repository for open-source
speech recognition engines. Moreover, each speech ﬁle released by VoxForge is
associated with several categories such as gender, age range, and pronunciation
dialect. The aim of our experiment is to extract this information, which is im-
plicitly correlated with the contents, even if it does not appear as an attribute
in our data set.
Attack description The main objective of this attack is to build a meta-
classiﬁer for the following property P: the classiﬁer was trained only with people
who speak an Indian english dialect. We emphasize that this is external infor-
mation as introduced in Section 2.1: the speech dialect is NOT explicitly used
during the training process, but in practice it inﬂuences the output of the clas-
siﬁer.
The ﬁrst part of the experiment describes the encoding of the HMMs; next, we
describe the decision tree of the meta-classiﬁer; ﬁnally, we present an improved
version of the classiﬁer that uses a ﬁlter to improve the classiﬁcation.
To carry out the attack, we retrieved 11, 137 recordings from the VoxForge cor-
pus. In particular, for our experiment, we took only the MFCC ﬁles in the English
language. Each track comes with a form containing some meta-information (e.g.
gender, age, pronunciation dialect). We have partitioned the corpus according
to this meta-information; for this experiment, we have considered the partition
containing the recordings made with the same pronunciation dialect and similar
recording equiments. We preprocessed the corpus with the HTK toolkit in order
to minimize the environmental noise. Starting from this partition, we have cre-
ated D according to the rule deﬁned in Section 2.1. Then, we have trained each
classiﬁer Ci as described in Algorithm 1.
After that, we started with the encoding phase which is described below. Each
classiﬁer Ci, is represented in the HTK toolkit by an ASCII ﬁle containing
an HMM for each phoneme belonging to the English language. Each HMM is
composed of: a transition probability matrix A(n × n) which describes the tran-
sition between hidden states and the two vectors M = (µ1, µ2, . . . , µm) and
V = (σ1, σ2, . . . , σm) that are respectively mean and variance of the output


## Page 12


probability distribution from a given hidden state (see Sections 3.1 and 3.1).
In our experiments we took the default HTK values during the training step
(i.e. m = 25 and n = 5). To encode a single HMM we chose to focus only on
the output distributions, that is, the couple of vectors (M, V ). The idea is that
all these values are initialized in the early steps of the training, according to
a mean computed over the entire MFCC dataset: since all the values are iter-
atively reﬁned through the HTK toolkit, then we expect that these values are
correlated in some way with the voices of the learning set and, by extension,
with the pronunciation dialects. For this reason we set the feature vector a ∈FC
as follows:
a = (ph, µ1, µ2, . . . , µm, σ1, σ2, . . . , σm, li)
where ph is a string value representing a phoneme, µ1, µ2, . . . , µm and σ1, σ2, . . . , σm
are the output probability vectors and li ∈{Indian,not Indian} is the label of
the current row. It is important to notice that this encoding gives a row in
DC for each phoneme of the acoustic model. Our training set was composed
of 5, 420 tuples equally balanced over the two classiﬁcations considered for this
experiment (i.e. the 50% of training data were generated by Indian people and
the remaining 50% by people speaking with diﬀerent accent). The test set was
composed of 1, 016 instances: 774 of these are classiﬁed as not Indian and the re-
maining 242 are classiﬁed as Indian. The training ended up with a very complex
meta-classiﬁer: the decision tree was composed of more than 811 nodes with 610
leaves.
Indian not Indian classiﬁed as
220
22
Indian
72
702
not Indian
Table 2. The confusion matrix of the meta-classiﬁer
Precision Recall
NotIndian
0.97
0.91
Indian
0.75
0.91
Table 3. The precision and recall summary of the meta-classiﬁer
Table 2 reports the confusion matrix obtained from this experiment (we recall
that the confusion matrix shows how correctly a classiﬁer assigned the labels to
the elements of the input set). The not Indian classiﬁers are correctly classiﬁed
with precision of 0.97 whereas the Indian classiﬁers are recognized with precision
0.75. (Speciﬁcally: recall Indian: 0.909 and recall not Indian: 0.907.)
One of the most interesting features provided by the C4.5 algorithm consists of
the order in which the attributes decision tree appear. In fact C4.5 puts the most


## Page 13


0
50
100
150
200
250
300
350
400
 0
 1
 2
 3
 4
 5
 6
 7
 8
 9  10  11  12  13  14  15  16  17  18  19  20  21
Number of occurences
indian
not indian
Fig. 3. The frequency of the values of σ2 for all phonemes in the training data of the
meta-classiﬁer.
representative attributes at the higher level of the tree. In our experiment, one
of the most representative nodes is σ2. The frequencies of each value of σ2 in the
training data of the meta-classiﬁer are represented in ﬁgure 3. It is easy to notice
that the mean values of each distribution are considerably shifted and can be
easily recognized with respect to the class. Our meta-classiﬁer is very eﬀective in
catching those diﬀerences; hence, as our experiments show, it correctly classiﬁes
the most part of the test set.
To further improve the quality of MC, we have applied a ﬁlter to the training set
DC. Our goal was to extract the phonemes that better diﬀerentiate the language
dialect. To perform this task, we employed the Kullback-Leibler (KL) divergence
between the output probability distributions of the models. The KL divergence
is deﬁned as follows:
DKL(P||Q) =
X
i
P(i)log P(i)
Q(i)
(1)
A low DKL value means a high similarity of the two probability distributions,
while on the other hand, high divergence values correspond to an inferior simi-
larity. This means that the phonemes with the highest divergence are the ones
which better discriminate the Indian accent from others.
Since the output probabilities follow a Normal distribution, we used the following
equation to compute the KL divergence:
DKL(Xi||Xj) = (µi −µj)2
2σ2
i
+ 1
2
 
σ2
i
σ2
j
−1 −ln σ2
i
σ2
j
!
(2)
where Xi ∼N(µi, σi) and Xj ∼N(µj, σj).
We built 100 diﬀerent training sets without Indian records, obtaining the relative


## Page 14


acoustic models C = (C1, C2, . . . , C100). Then, we built the reference learning set
containing only Indian records, obtaining the relative acoustic model Cr. Then,
we compared the distance between the output probability distributions of Cr
with every Ci ∈C, obtaining the summed value of the divergence. Since the
same phoneme state has 25 possible output distributions, we have just computed
the mean distance value across all the distributions. Finally, we took the ﬁve
phonemes with the highest divergence and we rebuilt MC using only the entries
relative to these phonemes.
Indian not Indian classiﬁed as
169
6
Indian
2
137
not Indian
Table 4. The confusion matrix of the ﬁltered meta-classiﬁer
Precision Recall
NotIndian
0.98
0.96
Indian
0.95
0.98
Table 5. The precision and recall summary of the ﬁltered meta-classiﬁer
Table 4 shows the confusion matrix of the ﬁltered classiﬁer. The new results
are noticeably improved: the precision for the not Indian class is 0.98 as before
whereas the precision for the Indian class is increased to 0.95. (Speciﬁcally: recall
Indian: 0.986 and recall not Indian: 0.966.)
Also, the size of the decision tree has dropped down signiﬁcantly (the resulting
decision tree is composed only of 21 nodes with 11 leaves).
3.2
Support Vector Machines
Background Support Vector Machines (SVM) are supervised learning methods
related to statistical learning theory and ﬁrst introduced by Boser et al. in [17].
SVMs are largely used for classiﬁcation and regression analysis. In their basic
form, SVMs are ﬁrst trained with sets of input data classiﬁed in two classes and
are then used to guess the class for each new given input. This aspect makes
SVM a non-probabilistic binary linear classiﬁer. Support Vector classiﬁers are
based on the concept of separating hyperplanes, that are the hyperplanes in
the attribute space that deﬁnes the decision boundaries between sets of objects
belonging to diﬀerent classes.
During the training phase, the SVM receives a set of labeled examples, each of
them described by n numerical attributes (features) and thus represented as a set
of points in a n-dimensional space. For the sake of simplicity, we brieﬂy introduce


## Page 15


how an SVM works with data represented by two attributes and mapped into
two classes. The entry i of the training dataset is represented by a 2-dimensional
vector xi = ⟨xi1, xi2⟩and belongs to one and only one class yi:
(y1, x1), (y2, x2), . . . (yn, xm)
yj ∈−1, 1
(3)
Let us suppose that the training data is linearly separable, namely there exists
a vector w and a scalar value b such that:
w · xi + b ≥1 if yi = 1,
w · xi + b ≤1 if yi = −1
(4)
In order to deal with sets that are not linearly separable, the training vectors
xi can be mapped into a higher dimensional space by the function φ, the so
called kernel function: many kernel functions have been proposed, but the most
used are linear K(xi, xj) = xT
i xj, polynomial K(xi, xj) = (γxT
i xj + r)d, γ ≥0,
radial basis function, RBF, K(xi, xj) = exp(−γ∥xi −xj∥2), γ ≥0 and sigmoid
K(xi, xj) = tanh(γxT
i xj + r). The Support Vector classiﬁer ﬁnds the optimal
hyperplanes that separate the training data with a maximal margin in this higher
dimensional space; formally it resolves the system of equations:
yi(w0 · x + b0) = 0
(5)
It must be pointed out that, thanks to the nature of the training algorithm
adopted by SVM, the solution of (5) can be obtained at a reasonable compu-
tational cost regardless of the kernel function adopted. Intuitively, a good sep-
aration is achieved by the hyperplane that has the largest distance - or margin
- between the nearest training data points of diﬀerent classes: these points are
called the support vectors. Roughly speaking, the larger the margin, the lower
the generalization error of the classiﬁer.
It is easy to notice how the functional margin points determine the hyperplane
of separation. This information is trivially featured by the attribute values in the
training sets. Furthermore, we highlight that SVM can disclose more informa-
tion when several classiﬁers trained with diﬀerent kernel functions are provided.
Since a trained SVM is represented by a set of weights and a subset of the train-
ing sample, it is not easy to obtain useful information on the characteristics of
the complete training set directly from the SVM representation.
SVMs generated a signiﬁcant research activity which extends across the limits
of data mining area. Although SVMs were initially introduced to solve pattern
recognition problems in an eﬃcient way ([20]), nowadays they are suitable in
several contexts. In fact, SVMs are used for intrusion detection and anomaly
detection ([39, 34, 22]) or as part of complex systems for similar tasks ([48, 6]).
Other authors propose SVM-based systems for privacy-critical tasks, such as
cancer diagnostic [30, 7], text categorization [36], or face recognition [4].


## Page 16


SVM for network traﬃc classiﬁcation As shown by the extensive literature
on this topic [28, 27, 49, 15], network traﬃc classiﬁcation is commonly realized
by means of Machine Learning algorithms, like K-Means, HMM, decision trees,
and SVM.
In order to evaluate the information leakage of SVM classiﬁers, we set up a
simple Network Traﬃc Classiﬁer able to distinguish between DNS and WEB
traﬃc. In particular, we considered an SVM classiﬁer based on the SMO module
(Sequential Minimal Optimization [50]) of the Weka framework.
Our experiment uses a real netﬂow dataset, gathered by a national tier 2
Autonomous System. NetFlow is a CiscoTM protocol used by network adminis-
trators for gathering traﬃc statistics [53]. NetFlow is used to monitor data at
Layers 2-4 of the networking protocol stack and to provide an aggregated view
of the network status. In particular, NetFlow eﬃciently supports many network
tasks such as traﬃc accounting, network billing and planning, as well as Denial
of Service monitoring.
A netﬂow-enabled router produces one new record for each newly established
connection, collecting selected ﬁelds from its IP header. More precisely, a single
netﬂow record is deﬁned as a unidirectional sequence of packets all sharing the
following values: source and destination IP addresses, source and destination
ports (for UDP or TCP, 0 for other protocols), IP protocol, Ingress interface
index and IP Type of Service.
Other valuable information associated with the ﬂow, such as timestamp, du-
ration, number of packets and transmitted bytes, are also recorded. Then, we
consider a single netﬂow as a record that represents the data exchanged between
two hosts only in one direction. We consider a network traﬃc classiﬁer aimed
at correctly distinguishing the WEB and DNS traﬃc. The classiﬁer was trained
using a balanced set of netﬂows of WEB and DNS traﬃc. It is worth noting that
the WEB data set includes several traﬃc patterns. Namely, it contains the ﬂows
directed to national newspapers, advertising websites, and the Google search
engine website.
During the training phase of the experiment, we used all the ﬁelds of the netﬂow
entries, except the source and destination IP addresses of the tracked connec-
tions. In the literature there are examples of SVM Classiﬁers for traﬃc detec-
tion [28] able to distinguish a greater variety of network protocols; the method-
ology used in our experiment is similar, and can be considered appropriate to
highlight the statistical information leakage issues that are the target of our
research. Notice that the accuracy and the precision of the obtained classiﬁer
is optimal, thanks to the simplicity of the training samples: indeed, WEB and
DNS connections have well-separated traﬃc patterns, producing a large margin
for classiﬁcation.
Attack description In our experiment we investigate whether it is possible to
extrapolate the type of traﬃc that was used during the construction of the SVM
model. For example: Can we infer whether Google web traﬃc was used in the
training samples? (As before, Google traﬃc does NOT appear in the attributes


## Page 17


of the training set.) We proceed with our attack by creating several ad-hoc data
sets with well-deﬁned statistical properties and use them to build our meta-
classiﬁer MC. Namely, we created 70 ad-hoc data sets, selecting 20.000 ﬂows of
network traﬃc, distinct from the original training set. While all 70 classiﬁers
were trained with a non-speciﬁc DNS traﬃc, the ﬁrst half of the classiﬁers were
trained using WEB traﬃc directed only to Google search engine (property P). For
the remaining 35 classiﬁers, we used WEB traﬃc without any netﬂow directed
to Google search engine (property P).
Each classiﬁer was trained using a polynomial kernel function of degree 3
and was encoded by the list of the support vectors it contains, namely a set of
points (y, x) in the n−dimensional space (x = {x1, x2, . . . , xn}). The training
samples of the classiﬁer MC are composed of all the support vectors of the 70
classiﬁers, labeled according to the property P or P used for training:
DC =
[
Ci
{(y, ⟨x⟩, label)}
We evaluate the performance of MC using the cross validation strategy, a method
that divides the data into k mutually exclusive subsets (namely, the “folds”) of
approximately equal size. With cross validation, the accuracy estimate is the
average accuracy for the k folds.
Google not Google classiﬁed as
2312
101
Google
92
2786
not Google
Table 6. The confusion matrix of the meta-classiﬁer
Precision Recall
Google
0.95
0.93
not Google
0.94
0.96
Table 7. The precision and recall summary of the meta-classiﬁer
Table 6 summarizes the experiment results: with respect to the Google class,
we achieve a precision of 0.954 and a recall of 0.932. On the other hand, we
correctly classify not Google instances with a precision of 0.943 and a recall of
0.962.
As in the example with the HMMs, the experimental results show that we
were able to build an eﬀective meta-classiﬁer that infers whether the training
set given as input includes also a speciﬁc type of traﬃc.


## Page 18


4
Diﬀerential privacy
In this section we show that diﬀerential privacy is ineﬀective against our attack
strategy. More speciﬁcally, the information leakage we are after sits outside the
adversary model considered by diﬀerential privacy.
Diﬀerential privacy [19, 14, 9] protects against unintentional disclosure of
potentially sensitive information related to a single record of a database D. In
other words, diﬀerential privacy maximizes the accuracy of queries from statis-
tical databases and, at the same time, minimizes the ability to identifying single
records. To protect the privacy of database records, diﬀerential privacy opts for
basically three approaches:
1. The ﬁrst is to obfuscate the original database D and transform it into D′.
This strategy is completely ineﬀective in our model since D′ is the database
actually used during training and it is exactly what the adversary in our
model is after. That is, our adversary is not interested in D, or any of its
records, but it is rather eager for any information on D′, i.e., anything that
is the result of the transformations applied by diﬀerential privacy.
2. Another approach is to train a classiﬁer and then add noise to the output.
This is also ineﬀective since, in our model, the adversary has complete access
to the classiﬁer and could just disable the instruction that adds noise.
3. The third approach is more subtle. It consists of adding noise during train-
ing, thus eﬀectively obfuscating the learning process. This approach is still
ineﬀective against our adversary since, intuitively, the ﬁnal classiﬁer must
anyway converge to classify correctly the training set. Thus, the noise must
be somehow restrained and its eﬀect can easily be mitigated (see below).
It may be unclear why the third approach above fails to provide any protec-
tion against our adversary. Hence, we performed next an experiment showing how
to extract sensitive information from a classiﬁer trained within the framework
SuLQ, introduced in [9]. The SulQ authors improved several standard classiﬁers
to provide diﬀerential privacy. The main idea consists of adding a small amount
of noise, according to a Normal Distribution N(0, σ), to any access to the train-
ing set. The variance of N regulates the privacy property provided by diﬀerential
privacy.
Before introducing the experiment, we brieﬂy recall some concepts of K-
Means, which is the most popular clustering algorithm.
4.1
K-Means: the clusterization algorithm
Clustering is the task of partitioning unstructured data in such a way that objects
with an high level of similarity fall into the same partition. Clustering is a typical
example of unsupervised learning models where examples are unlabeled, i.e., they
are not pre-classiﬁed. The K-Means algorithm [3] is one of the most common
methods in this family and it has been used in many applications (e.g., [12, 59, 10,
11]). For example, in [12] the authors developed a real-time traﬃc classiﬁcation


## Page 19


method, based on K-Means, to identify SSH ﬂows from statistical behavior of
IP traﬃc parameters, such as length, arrival times and direction of packets.
In K-Means both training and classiﬁcation phases are very intuitive. Dur-
ing the learning process, the algorithm partitions a set of n observations into k
clusters. Then, the algorithm selects the centroid (i.e., the barycenter, or geo-
metric midpoint) of every cluster as a representative for that set of objects. More
formally, given a set of observations (x1, x2, . . . , xn), where each observation is
a d-dimensional real vector, K-Means partitions the n observations into k sets
(k ≤n) S = {S1, S2, . . . , Sk} in order to minimize the within-cluster function:
argmin
S
k
X
i=1
X
xj∈Si
∥xj −µi∥
(6)
where µi is the mean of points in Si.
To classify a given data set of d-dimensional elements with respect to k clus-
ters, K-Means runs a learning process that can be summarized by the following
steps:
1. Randomly pick k initial cluster centroids;
2. Assign each instance x to the cluster that has a centroid nearest to x;
3. Recompute each cluster’s centroid based on which elements are contained in
it;
4. Repeat Steps 2 and 3 until convergence is achieved;
4.2
Hacking models secured by Diﬀerential Privacy
We implemented two variants of a network traﬃc classiﬁer that makes use of
K-Means. We trained both classiﬁers with the same data set of the SVM experi-
ment of Section 3.2. The ﬁrst implementation directly uses the euclidian distance
as metric to revise the centroids in the iterative reﬁnement phase (equation 6).
The second version implements a privacy preserving version of K-Means, provid-
ing diﬀerential privacy. We implemented the latter within the SulQ framework,
introduced by Blum et al. [9].
We ran the two classiﬁers on 70 training sets, obtaining 70 distinct centroids.
Recall that our objective is to recognize whether there was Google traﬃc within
the traces.
With respect to the classiﬁer with no diﬀerential privacy, we represent the
centroids when there is traﬃc to Google.com in ﬁgure 4(a), and no traﬃc to
Google.com in ﬁgure 4(b). It is easy to see that the positions of the centroids
are quite diﬀerent, allowing us to easily distinguish between these two cases.
Similar results appear when we picture the centroids of the classiﬁer providing
diﬀerential privacy in ﬁgures 5(a) and 5(b), respectively. Even in this case, an
adversary can easily distinguish whether there is Google.com traﬃc or not.


## Page 20


✥
 ✥✥✥✥
✁✥✥✥✥✥
✁ ✥✥✥✥
✂✥✥✥✥✥
✂ ✥✥✥✥
✄✥✥✥✥✥
✄ ✥✥✥✥
☎✥✥✥✥✥
✥
 ✥
✁✥✥
✁ ✥
✂✥✥
✂ ✥
✄✥✥
✄ ✥
☎✥✥
❜
✆
✝
✞
✟
♣✠✡☛☞✌✍
❑
✎
☞✠
✏✍
✑☞
✏
✌✒✓✔✕
✍
✖
✔✌✗
✏✓
✘
✔✙✙
☞✒☞
✏
✌
✔
✠
✚
✛
✒
✔✜✠✡✢
✣✍✔✏
✤
✖
☞✦
✌✒✠
✙✙✔
✡
✖
✔✌✗
✧✓✓
✤
✚☞
✙✚✓✖
✍
✘❉★
✌✒✠
✙✙✔✡
✡☞
✏
✌✒✓✔✕
✍
❲✩✪
✌✒✠
✙✙✔
✡
♣
✓✔✏
✌
✍
(a) Training set contains Web traﬃc directed to Google.com
✥
 ✥✥✥✥
✁✥✥✥✥✥
✁ ✥✥✥✥
✂✥✥✥✥✥
✂ ✥✥✥✥
✄✥✥✥✥✥
✄ ✥✥✥✥
☎✥✥✥✥✥
✥
 ✥
✁✥✥
✁ ✥
✂✥✥
✂ ✥
✄✥✥
✄ ✥
☎✥✥
❜
✆
✝
✞
✟
♣✠✡☛☞✌✍
❑✎
☞✠
✏✍
✑☞
✏
✌✒✓✔✕✍
✖✔✌✗
✏
✓
✘✔✙✙
☞✒☞
✏
✌✔✠
✚
✛✒✔✜✠✡✢
✣✍
✔
✏
✤
✖
☞
✦
✌✒✠
✙✙✔✡
✖✔✌✗
✏
✓
✧
✓✓✤
✚☞
✙✚
✓✖
✍
✘❉★
✌✒✠
✙✙
✔✡
✡☞
✏
✌✒✓✔
✕✍
❲✩✪
✌✒✠
✙✙✔✡
♣✓✔✏
✌
✍
(b) Training set does not contain Web traﬃc directed to
Google.com
Fig. 4. Centroids of the K-Means traﬃc classiﬁer without diﬀerential privacy.


## Page 21


✥
 ✥✥✥✥
✁✥✥✥✥✥
✁ ✥✥✥✥
✂✥✥✥✥✥
✂ ✥✥✥✥
✄✥✥✥✥✥
✄ ✥✥✥✥
☎✥✥✥✥✥
✥
 ✥
✁✥✥
✁ ✥
✂✥✥
✂ ✥
✄✥✥
✄ ✥
☎✥✥
❜
✆
✝
✞
✟
♣✠✡☛☞✌✍
❑
✎
☞✠✏
✍
✑☞✏✌✒✓✔✕
✍
✖
✔
✌✗
✘
✔✙✙
☞
✒☞✏✌
✔
✠
✚
✛✒✔✜✠✡✢
✣✜✠✒
✂
✤✥
✦
✧✍✔✏★
✖☞✩
✌✒✠
✙✙✔
✡
✖✔✌✗
✪✓✓★
✚
☞
✙✚✓✖✍
✘❉✫
✌✒✠
✙✙✔✡
✡☞✏✌✒✓✔✕
✍
❲✬✭
✌✒✠
✙✙✔
✡
♣
✓✔
✏✌
✍
(a) Training set contains Web traﬃc directed to Google.com
✥
 ✥✥✥✥
✁✥✥✥✥✥
✁ ✥✥✥✥
✂✥✥✥✥✥
✂ ✥✥✥✥
✄✥✥✥✥✥
✄ ✥✥✥✥
☎✥✥✥✥✥
✥
 ✥
✁✥✥
✁ ✥
✂✥✥
✂ ✥
✄✥✥
✄ ✥
☎✥✥
❜
✆
✝
✞
✟
♣✠✡☛☞✌✍
❑✎
☞✠
✏✍
✑☞
✏
✌✒✓✔✕✍
✖✔✌✗
✘✔✙✙☞✒☞
✏✌✔✠✚
✛✒✔✜
✠✡
✢
✣✜
✠✒
✂✤✥
✦
✧
✍
✔✏★
✖☞
✩
✌✒✠✙✙✔✡
✖
✔✌
✗
✏
✓
✪
✓✓
★
✚☞
✙✚✓✖
✍
✘
❉✫
✌✒✠✙✙✔✡
✡☞
✏
✌✒✓✔
✕✍
❲✬✭
✌✒✠✙✙✔✡
♣✓✔✏
✌
✍
(b) Training set does not contain Web traﬃc directed to
Google.com
Fig. 5. Centroids of a K-Means Traﬃc Classiﬁer with diﬀerential privacy.


## Page 22


5
Related works
The research area closest to the issues addressed in our paper appears to be In-
formation Disclosure considered in privacy preserving data mining and statistical
databases. It is worth describing some of these related results, even though we
stress that the type of leakage we consider in this paper has not been considered
before.
As formalized by Dwork in [19], diﬀerential privacy deals with the general
problem of privacy preserving analysis of data. More formally, a randomized
mechanism M provides ǫ−diﬀerential privacy if, for a database D1 and D2,
which diﬀer by at most one element, and for any t:
Pr[M(D1) = t]
Pr[M(D2) = t] ≤eǫ
In the diﬀerential privacy model, a trusted server holds a database with sen-
sitive information. Answers to queries are perturbed by the addition of random
noise generated according to a random distribution (usually a Laplace distribu-
tion).
Two settings are deﬁned: non interactive, where the trusted server computes and
publishes statistics on the original data, and interactive, where the server sits in
the middle and directly alters the answers to user queries to guarantee speciﬁc
privacy properties.
Chaudhuri et al. [40] design a privacy preserving logistic regression algorithm
which works in the ǫ−diﬀerential privacy model ([31]). The idea is quite simple:
the result of the trained classiﬁer is perturbed with a dynamic amount of noise.
This approach does not consider the security issues due to the exposure of the
model generated during the learning phase of the linear regression algorithm.
Other machine learning algorithms, such as Decision Trees, Artiﬁcial Neural
Networks, Clustering, have been re-engineered to provide diﬀerential privacy
and several are deﬁned within the SulQ framework [9].
Privacy Preserving Data Mining (PPDM) [14] is a novel research area aimed
at developing techniques that perform data mining primitives while protecting
the privacy of individual data records. In [55], Verykios et al. classiﬁed PPDM
techniques in ﬁve classes. Among them, we mention the Privacy preservation
class which refers to techniques used to preserve privacy for selective modiﬁ-
cations of data records. This can be achieved through heuristic values (e.g.,
selecting the values that minimize the utility loss of the data), cryptographic pro-
tocols (e.g., via Secure Multiparty Computation [44]), or reconstruction-based
techniques (e.g., strategy aimed at reconstructing the original data distribution
using randomized data).
Some previous work exists related to extraction of information from classiﬁers.
For instance, in [29], the authors show how a bayesian learning algorithm can
be used to learn which words are employed by a classiﬁer to classify messages
as spam and ham. Similarly, in [45, 58], the authors describe some statistical
attacks against spam ﬁlters aimed at understanding message features that are
not correctly classiﬁed by the ﬁlters.


## Page 23


Although using learning algorithms against other learning algorithms is not
unprecedented([29, 46]), our approach is diﬀerent since we uncovered a new class
of information leakage that is inherent to the learning process and that has never
been discussed before.
6
Conclusions
In this paper we introduced a novel approach to extract meaningful data from
machine learning classiﬁers using a meta-classiﬁer. While previous works inves-
tigated privacy concerns of a single database record, our approach focuses on the
statistical information strictly correlated to the training samples used during the
learning phase. We showed that several ML classiﬁers suﬀer from a new class of
information leakage that is not captured by privacy-preserving models, such as
PPDM or diﬀerential privacy.
We devised a meta-classiﬁer to successfully distinguish the accent of users
involved in deﬁning the corpus of a speech recognition engine. Furthermore, we
attacked an Internet traﬃc classiﬁer to infer whether a speciﬁc traﬃc pattern
was used during training.
Our results evince realistic issues facing machine learning algorithms as we
put forward the importance of protecting the training set—the alluring recipe
that makes a classiﬁer better than the competition and that should be guarded
as a trade secret.


## Page 24


Bibliography
[1] http://www.nuance.com/dragon/index.htm.
[2] http://www.voxforge.org.
[3] Some methods of classiﬁcation and analysis of multivariate observations,
1967.
[4] Face Recognition by Support Vector Machines, FG ’00, Washington,
DC, USA, 2000. IEEE Computer Society.
ISBN 0-7695-0580-5.
URL
http://dl.acm.org/citation.cfm?id=795661.796198.
[5] Julius — an open source real-time large vocabulary recognition engine., Aal-
borg, Denmark, 2001.
[6] Intrusion detection using neural networks and support vector machines, vol-
ume 2, 2002.
[7] Morphological Classiﬁcation of Medical Images using Nonlinear Support
Vector Machines, 2004. IEEE.
[8] Application
of
modiﬁed
neural
network
weights’
matrices
explaining
determinants
of
foreign
investment
patterns
in
the
emerging
mar-
kets, MICAI’05, Berlin, Heidelberg, 2005. Springer-Verlag.
ISBN 3-
540-29896-7,
978-3-540-29896-0.
doi:
10.1007/11579427 73.
URL
http://dx.doi.org/10.1007/11579427_73.
[9] Practical privacy: the SuLQ framework, PODS ’05, New York, NY, USA,
2005. ACM.
ISBN 1-59593-062-0. doi: 10.1145/1065167.1065184. URL
http://doi.acm.org/10.1145/1065167.1065184.
[10] Traﬃc
classiﬁcation
using
clustering
algorithms,
MineNet
’06,
New
York,
NY,
USA,
2006.
ACM.
ISBN
1-59593-569-
X.
doi:
http://doi.acm.org/10.1145/1162678.1162679.
URL
http://doi.acm.org/10.1145/1162678.1162679.
[11] Traﬃc classiﬁcation on the ﬂy, volume 36, New York, NY, USA, April
2006. ACM.
doi: http://doi.acm.org/10.1145/1129582.1129589.
URL
http://doi.acm.org/10.1145/1129582.1129589.
[12] Real
Time
Identiﬁcation
of
SSH
Encrypted
Application
Flows
by
Using
Cluster
Analysis
Techniques,
NETWORKING
’09,
Berlin,
Heidelberg,
2009.
Springer-Verlag.
ISBN
978-3-642-01398-
0.
doi:
http://dx.doi.org/10.1007/978-3-642-01399-7 15.
URL
http://dx.doi.org/10.1007/978-3-642-01399-7_15.
[13] Automatic Reverse Engineering of Data Structures from Binary Execution,
2010. The Internet Society.
[14] Rakesh
Agrawal
and
Ramakrishnan
Srikant.
Privacy-
preserving
data
mining.
SIGMOD
Rec.,
29(2):439–450,
May
2000.
ISSN
0163-5808.
doi:
10.1145/335191.335438.
URL
http://doi.acm.org/10.1145/335191.335438.
[15] Tom Auld, Andrew W. Moore, and Stephen F. Gull. Bayesian neural net-
works for internet traﬃc classiﬁcation. IEEE Transactions on Neural Net-
works, 18(1):223–239, 2007.


## Page 25


[16] L. E. Baum and T. Petrie. Statistical inference for probabilistic functions of
ﬁnite state Markov chains. Annals of Mathematical Statistics, 37:1554–1563,
1966.
[17] Bernhard E. Boser, Isabelle M. Guyon, and Vladimir N. Vapnik. A training
algorithm for optimal margin classiﬁers. In Proceedings of the 5th Annual
ACM Workshop on Computational Learning Theory, pages 144–152. ACM
Press, 1992.
[18] Leo Breiman, J. H. Friedman, R. A. Olshen, and C. J. Stone. Classiﬁcation
and Regression Trees. Statistics/Probability Series. Wadsworth Publishing
Company, Belmont, California, U.S.A., 1984.
[19] Michele Bugliesi, Bart Preneel, Vladimiro Sassone, and Ingo Wegener, edi-
tors. Diﬀerential Privacy, volume 4052 of Lecture Notes in Computer Sci-
ence, 2006. Springer. ISBN 3-540-35907-9.
[20] Christopher J. C. Burges.
A tutorial on support vector machines
for pattern recognition.
Data Min. Knowl. Discov.,
2(2):121–167,
June 1998.
ISSN 1384-5810.
doi: 10.1023/A:1009715923555.
URL
http://dx.doi.org/10.1023/A:1009715923555.
[21] Yves Chauvin and David E. Rumelhart, editors. Backpropagation: theory,
architectures, and applications. L. Erlbaum Associates Inc., Hillsdale, NJ,
USA, 1995. ISBN 0-8058-1259-8.
[22] Rung Ching Chen, Kai-Fan Cheng, and Chia-Fen Hsieh.
Using rough
set and support vector machine for network intrusion detection. CoRR,
abs/1004.0567, 2010.
[23] Edith Cohen and Carsten Lund.
Packet classiﬁcation in large isps: de-
sign and evaluation of decision tree classiﬁers.
SIGMETRICS Perform.
Eval. Rev., 33(1):73–84, June 2005. ISSN 0163-5999. doi: 10.1145/1071690.
1064222. URL http://doi.acm.org/10.1145/1071690.1064222.
[24] Vasant Dhar.
Prediction in ﬁnancial markets: The case for small
disjuncts.
ACM Trans. Intell. Syst. Technol., 2(3):19:1–19:22, May
2011.
ISSN
2157-6904.
doi:
10.1145/1961189.1961191.
URL
http://doi.acm.org/10.1145/1961189.1961191.
[25] Ruisheng Diao, Kai Sun, Vijay Vittal, Robert J. O’Keefe, Michael R.
Richardson, Navin Bhatt, Dwayne Stradford, and Sanjoy K. Sarawgi.
Decision Tree-Based Online Voltage Security Assessment Using PMU
Measurements.
IEEE Transactions on Power Systems, 24(2):832–839,
May 2009.
ISSN 0885-8950.
doi: 10.1109/TPWRS.2009.2016528.
URL
http://dx.doi.org/10.1109/TPWRS.2009.2016528.
[26] Jason Eisner. An interactive spreadsheet for teaching the forward-backward
algorithm. In Proceedings of the ACL-02 Workshop on Eﬀective tools and
methodologies for teaching natural language processing and computational
linguistics - Volume 1, ETMTNLP ’02, pages 10–18, Stroudsburg, PA, USA,
2002. Association for Computational Linguistics.
doi: 10.3115/1118108.
1118110. URL http://dx.doi.org/10.3115/1118108.1118110.
[27] Jeﬀrey
Erman,
Anirban
Mahanti,
Martin
Arlitt,
Ira
Cohen,
and
Carey
Williamson.
Oﬄine/realtime
traﬃc
classiﬁcation
using
semi-supervised
learning.
Perform.
Eval.,
64:1194–1213,
Octo-


## Page 26


ber 2007.
ISSN 0166-5316.
doi: 10.1016/j.peva.2007.06.014.
URL
http://dl.acm.org/citation.cfm?id=1284907.1285040.
[28] Alice Este, Francesco Gringoli, and Luca Salgarelli.
Support vector
machines for tcp traﬃc classiﬁcation.
Computer Networks, 53(14):2476
– 2490, 2009. ISSN 1389-1286. doi: 10.1016/j.comnet.2009.05.003. URL
http://www.sciencedirect.com/science/article/pii/S1389128609001649.
[29] J. Graham-Cumming. How to beat an adaptive spam ﬁlter. In The MIT
Spam Conference, 2004.
[30] Isabelle Guyon, Jason Weston, Stephen Barnhill, and Vladimir Vapnik.
Gene selection for cancer classiﬁcation using support vector machines.
Mach. Learn., 46(1-3):389–422, March 2002. ISSN 0885-6125. doi: 10.1023/
A:1012487302797. URL http://dx.doi.org/10.1023/A:1012487302797.
[31] Shai Halevi and Tal Rabin, editors.
Calibrating Noise to Sensitivity in
Private Data Analysis, volume 3876 of Lecture Notes in Computer Science,
2006. Springer. ISBN 3-540-32731-2.
[32] J.F. Hayes.
The viterbi algorithm applied to digital data transmission.
Communications Magazine, IEEE, 40(5):26 –32, may 2002.
ISSN 0163-
6804. doi: 10.1109/MCOM.2002.1006969.
[33] Ypke Hiemstra.
Linear regression versus backpropagation networks to
predict quarterly stock market excess returns.
Comput. Econ., 9(1):67–
76, February 1996.
ISSN 0927-7099.
doi: 10.1007/BF00115692.
URL
http://dx.doi.org/10.1007/BF00115692.
[34] Wenjie Hu, Yihua Liao, and V. Rao Vemuri. Robust anomaly detection
using support vector machines. In In Proceedings of the International Con-
ference on Machine Learning. Morgan Kaufmann Publishers Inc.
[35] Anil K. Jain, Jianchang Mao, and K. Mohiuddin. Artiﬁcial neural networks:
A tutorial. IEEE Computer, 29:31–44, 1996.
[36] Thorsten Joachims.
Text categorization with support vector machines:
Learning with many relevant features. In Claire N´edellec and C´eline Rou-
veirol, editors, Machine Learning: ECML-98, volume 1398 of Lecture Notes
in Computer Science, pages 137–142. Springer Berlin / Heidelberg, 1998.
ISBN 978-3-540-64417-0. URL http://dx.doi.org/10.1007/BFb0026683.
10.1007/BFb0026683.
[37] B. H. Juang and L. R. Rabiner. Hidden markov models for speech recog-
nition. Technometrics, 33(3):251–272, August 1991. ISSN 0040-1706. doi:
10.2307/1268779. URL http://dx.doi.org/10.2307/1268779.
[38] Daniel Jurafsky and James H. Martin.
Speech and Language Pro-
cessing
(2nd
Edition)
(Prentice
Hall
Series
in
Artiﬁcial
Intelli-
gence).
Prentice Hall, 2 edition, 2008.
ISBN 0131873210.
URL
http://www.amazon.com/Language-Processing-Prentice-Artificial-Intelligence/dp/013187321
[39] Latifur Khan, Mamoun Awad, and Bhavani Thuraisingham.
A new
intrusion
detection
system
using
support
vector
machines
and
hi-
erarchical clustering.
The
VLDB
Journal,
16(4):507–521, October
2007.
ISSN
1066-8888.
doi:
10.1007/s00778-006-0002-5.
URL
http://dx.doi.org/10.1007/s00778-006-0002-5.


## Page 27


[40] Daphne Koller, Dale Schuurmans, Yoshua Bengio, and L´eon Bottou, editors.
Privacy-preserving logistic regression, 2008. Curran Associates, Inc.
[41] K.-F. Lee and H.-W. Hon. Large-vocabulary speaker-independent continu-
ous speech recognition using hmm. In Acoustics, Speech, and Signal Pro-
cessing, 1988. ICASSP-88., 1988 International Conference on, pages 123
–126 vol.1, apr 1988. doi: 10.1109/ICASSP.1988.196527.
[42] Ming Li and Zhi-Hua Zhou. Improve Computer-Aided Diagnosis With Ma-
chine Learning Techniques Using Undiagnosed Samples. IEEE Transactions
on Systems, Man, and Cybernetics - Part A: Systems and Humans, 37(6):
1088–1098, November 2007. ISSN 1083-4427. doi: 10.1109/TSMCA.2007.
904745. URL http://dx.doi.org/10.1109/TSMCA.2007.904745.
[43] Jianhua Lin. Divergence measures based on the shannon entropy. IEEE
Transactions on Information theory, 37:145–151, 1991.
[44] Yehuda Lindell and Benny Pinkas.
Secure multiparty computation for
privacy-preserving data mining.
IACR Cryptology ePrint Archive, 2008:
197, 2008.
[45] D. Lowd and C. Meek. Good word attacks on statistical spam ﬁlters. In In
Proceedings of the 2nd Conference on Email and Anti-Spam, 2005.
[46] Daniel Lowd and Christopher Meek.
Adversarial learning.
In Proceed-
ings of the eleventh ACM SIGKDD international conference on Knowledge
discovery in data mining, KDD ’05, pages 641–647, New York, NY, USA,
2005. ACM.
ISBN 1-59593-135-X. doi: 10.1145/1081870.1081950. URL
http://doi.acm.org/10.1145/1081870.1081950.
[47] T.
Mitchell.
Machine
Learning.
McGraw-Hill
Education
(ISE
Editions),
1st
edition,
October
1997.
ISBN
0071154671.
URL
http://www.amazon.com/exec/obidos/redirect?tag=citeulike07-20&path=ASIN/0071154671.
[48] Snehal A. Mulay, P.R. Devale, and G.V. Garje.
Article:intrusion detec-
tion system using support vector machine and decision tree. International
Journal of Computer Applications, 3(3):40–43, June 2010. Published By
Foundation of Computer Science.
[49] T.T.T. Nguyen and G. Armitage. A survey of techniques for internet traﬃc
classiﬁcation using machine learning. Communications Surveys Tutorials,
IEEE, 10(4):56 –76, quarter 2008. ISSN 1553-877X. doi: 10.1109/SURV.
2008.080406.
[50] J. Platt. Fast training of support vector machines using sequential min-
imal optimization.
In B. Schoelkopf, C. Burges, and A. Smola, editors,
Advances in Kernel Methods - Support Vector Learning. MIT Press, 1998.
URL http://research.microsoft.com/~jplatt/smo.html.
[51] J. R. Quinlan.
Induction of decision trees.
Mach. Learn., 1(1):81–106,
March 1986.
ISSN 0885-6125.
doi: 10.1023/A:1022643204877.
URL
http://dx.doi.org/10.1023/A:1022643204877.
[52] J. Ross Quinlan. C4.5: programs for machine learning. Morgan Kaufmann
Publishers Inc., San Francisco, CA, USA, 1993. ISBN 1-55860-238-0.
[53] Cisco Systems.
Cisco Systems NetFlow Services Export Version 9.
http://tools.ietf.org/html/rfc3954, 2004.


## Page 28


[54] Adi L Tarca, Vincent J Carey, Xue-wen Chen, Roberto Romero, and Sorin
Dr˘aghici. Machine learning and its applications to biology. PLoS Com-
put Biol, 3(6):e116, 06 2007.
doi: 10.1371/journal.pcbi.0030116.
URL
http://dx.doi.org/10.1371%2Fjournal.pcbi.0030116.
[55] Vassilios S. Verykios, Elisa Bertino, Igor Nai Fovino, Loredana Parasil-
iti Provenza, Yucel Saygin, and Yannis Theodoridis.
State-of-the-
art in privacy preserving data mining.
SIGMOD Rec., 33(1):50–57,
March 2004.
ISSN 0163-5808.
doi: 10.1145/974121.974131.
URL
http://doi.acm.org/10.1145/974121.974131.
[56] Weka
Machine
Learning
Project.
Weka.
URL
http://www.cs.waikato.ac.nz/˜ml/weka.
[57] M. Wernick, Yongyi Yang, J. Brankov, G. Yourganov, and S. Strother. Ma-
chine learning in medical imaging. Signal Processing Magazine, IEEE, 27
(4):25 –38, july 2010. ISSN 1053-5888. doi: 10.1109/MSP.2010.936730.
[58] Gregory L. Wittel and S. Felix Wu. On attacking statistical spam ﬁlters.
In IN PROC. OF THE CONFERENCE ON EMAIL AND ANTI-SPAM
(CEAS), MOUNTAIN VIEW, 2004.
[59] Guowu Xie, M. Iliofotou, R. Keralapura, M. Faloutsos, and A. Nucci. Sub-
ﬂow: Towards practical ﬂow-level traﬃc classiﬁcation. In INFOCOM, 2012
Proceedings IEEE, pages 2541 –2545, march 2012. doi: 10.1109/INFCOM.
2012.6195649.
[60] Steve Young.
A review of large-vocabulary continuous-speech.
Signal
Processing Magazine, IEEE, 13(5):45, sept. 1996. ISSN 1053-5888. doi:
10.1109/79.536824.


## Page 29


A
Artiﬁcial Neural Networks
The Artiﬁcial Neural Networks (ANNs) are a category of machine learning al-
gorithms able to solve a variety of problems in decision making, optimization,
prediction, and control, learning functions from real, discrete and vector valued
examples. The ANNs obtain good performances in problems where the training
data is retrieved by complex sensor, such as cameras or microphones. These al-
gorithms are also resilient to the presence of noise in the dataset. Several types
of ANN have been proposed [35]. We focus on a particular family of ANNs, the
ones based on Multilayer Perceptrons, and the related Backpropagation algorithm
([21]) used for their training.
The basic unit of an ANN is the Perceptron (or neuron), a unit that takes
a vector of real-valued inputs, calculates a linear combination of these inputs
and then outputs 1 if the result is greater than some threshold and -1 otherwise.
More formally a perceptron can be represented as a function
o(x1, . . . , xn) =

1
if Pn
i=0 wixi > 0
−1
otherwise
where we consider x0 to be always set to 1 to simplify the notation, and we call
net = Pn
i=1 wixi. Observe that −w0 is the threshold that makes the neuron to
output 1.
A single perceptron represents an hyperplane decision surface in the n−dimensional
space of instances. This kind of perceptron can only discriminate between lin-
early separable instances. To overcome this limitation, the sigmoid function σ is
used to decide the output value:
σ(net) =
1
1 −expnet
An ANN is a multi-layer network of neurons: a ﬁrst input layer receives the input
bits and provides modiﬁed inputs to a following layer, that, in turn, elaborates
them and feeds a new layer, and so on. The last layer outputs the result of the
ANN. The neurons that form the internal layers are called the hidden units.
The core function of the network resides in the weight of the hidden units in the
internal layers which are set through the backpropagation algorithm. Starting
from random weights, the algorithm tunes them using a training set of input-
output pairs: the inputs go forward to the network until they become output,
while the errors (namely, the diﬀerence between actual and expected outputs)
are back-propagated to correct the weights. The error is reduced iteratively until
a minimal and tolerable error is obtained. The backpropagation of the error is
inspired by the principle of gradient descent: in a nutshell, if the weight signiﬁ-
cantly contributes to the error then its adjustment will be greater.
B
Classiﬁcation and Regression Trees
A classiﬁcation or regression tree (introduce by Breiman et al. in [18] in 1984)
is a prediction model which maps observations in a decision tree.


## Page 30


The observations L = (x1, y1), (x2, y2), . . . , (xN, yN) constitute the training set
and are used to learn a decision tree. Both classiﬁcation and regression trees deal
with the prediction of a response variable y (let Y be the domain of y), given
the values of a vector of predictor variables x (let X be the domain of x). If y is
a continuous or discrete variable taking real values (e.g., the size of an object,
the number of occurrences of certain events), the problem is called regression; if
Y is a ﬁnite set of unordered values (e.g., the type of Iris plants), the problem
is called classiﬁcation.
The training phase produces a tree structure in which the leaves represent the
class labels and the branches represent conjunctions of features that lead to
the class labels of their leaves. Decision trees can be considered as disjunction
of conjunctions of constraints on the attribute-values of instances. Each path
from the tree root to a leaf corresponds to a conjunction of attribute tests, and
the tree itself to a disjunction of these conjunctions [47]. Decision trees work
better when the target function has discrete output (for example “yes or no”)
and the data instances are represented by attribute-value pairs. Furthermore,
decision trees perform well even when the training dataset contains errors or
missing values. These characteristics make decision tree a suitable solution for
many classiﬁcation problems and in a great variety of contexts. The most popular
implementation of decision trees is the C4.5 [52] algorithm, which is an extended
version of the ID3 algorithm [51]. top-down, greedy search through the space of
all possible decision trees. In detail, ID3 algorithm starts the search of decision
tree answering the question: which attribute should be used at the root of the
tree? Once the root is found, a descendent node of the root is created for each
possible value, then the same question is asked recursively at each new node,
until: (i) each attribute has been considered in the path through the tree, or (ii)
the training examples related to a speciﬁc leaf has the same attribute values.
The selection of the best attribute in each level of the tree is performed using
the concept of information gain. In fact, the information gain measures how well
a given attribute separates the training examples. Given a collection S of items,
for each attribute A, ID3 algorithm evaluates the gain of A with respect to S
via the equation:
Gain(S, A) = H(S) −
X
v∈Values(A)
|Sv|
|S| H(Sv)
where H(S) represents the Entropy of the entire dataset and Sv is the subset of
S for which attribute A has value v.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1306_4447v1_hacking_smart_machines_with_smarter_ones_how_to_extract_meaningful_data_from_ma
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2013/1306_4447V1_HACKING_SMART_MACHINES_WITH_SMARTER_ONES_HOW_TO_EXTRACT_MEANINGFUL_DATA_FROM_MA.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
