---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1808.05578v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1808.05578v1_LARNN__Linear_Attention_Recurrent_Neural_Network

> Source: 1808.05578v1_LARNN__Linear_Attention_Recurrent_Neural_Network.pdf

> Pages: 14

---


## Page 1


LARNN: Linear Attention Recurrent Neural Network
Guillaume Chevalier
Dept. of Computer Science and Software Engineering,
Laval University, Quebec, Canada
August 17, 2018
Abstract
The Linear Attention Recurrent Neural Network (LARNN) is a recurrent attention module
derived from the LSTM cell and ideas from the consciousness Recurrent Neural Network
(RNN). Yes, it LARNNs.
The LARNN uses attention on its past cell state values for a
limited window size k. The formulas are also derived from the Batch Normalized Long Short-
Term Memory (BN-LSTM) cell and the Transformer Network for its Multi-Head Attention
Mechanism. The Multi-Head Attention Mechanism is used inside the cell such that it can
query its own k past values with attention with restricted windowing on the k most recent
previous cell state. This has the eﬀect of augmenting the rank of the tensor with the attention
mechanism, such that the cell can perform complex queries to question its previous inner
memories, which should augment the long short-term eﬀect of the memory. With a clever
trick, the LARNN cell with attention can be easily used inside a loop on the cell state, just
like how any other Recurrent Neural Network (RNN) cell can be looped linearly through time
series. This is due to the fact that its state, which is looped upon throughout time steps
within time series, stores the inner states in a "ﬁrst in, ﬁrst out" queue which contains the k
most recent states and on which it is easily possible to add static positional encoding when
the queue is represented as a tensor. This neural architecture yields better results than the
plain, vanilla LSTM cells. It can obtain results of 91.924% for the test accuracy, compared to
the previously attained 91.653% using vanilla LSTM cells. Note that this is not to compare
to other research, where up to 93.349% is obtained, but by costly using 18 LSTM cells rather
than with 2 to 3 cells as analyzed here and in comparison. Finally, an interesting discovery is
made, such that adding activation within the multi-head attention mechanism’s linear layers
can yield better results in the context researched hereto.
1
Introduction
1.1
Prior Art
It have always been hard to replace the LSTM [HS97] since its discovery by Sepp Hochreiter and
Jürgen Schmidhuber, that it’d be for language models or other kind of time series processing with
neural networks, such as sensors signal.
Recently, Attention Mechanisms [BCB14] have been proven quite useful for Neural Machine
Translation (NMT) when paired with RNNs. However, Attention Mechanisms are so good that
they recently have been used alone without any kind of RNN nor Convolutional Neural Network
(CNN). This marks the apparition of the Transformer Network [VSP+17], claiming by the title of
the paper that Attention Is All You Need. Since then, people started to believe that RNNs could
be discarded in favor of attention mechanisms.
On the other side, there is Yoshua Bengio with his paper about The Consciousness Prior [Ben17],
in which he express consciousness as being recurrent through time, introducing the consciousness
RNN which, by any means, may retain fragments of the input representations through time in the
RNN cell as if it was attention.
1
arXiv:1808.05578v1  [cs.LG]  16 Aug 2018


## Page 2


1.2
Proof that RNNs are here to stay
However, RNNs can’t be replaced: they are O(n), while attention mechanisms are O(n2), where
n here represents the temporal axis along the processed time series.
Those are diﬀerent data
structures, and it is not true that attention models can fully replace recurrent models. And even
if the Attention Mechanisms would be stacked hierarchically (like rescursive pooling) with small
windows - similarly to how a Wavenet [VDODZ+16] would use convolutions with windowing) -
at best this neural architecture would require O(nlog(n)) time to process its input time series.
The advantages of O(n2) attention only appears when the sequence length is small enough to be
computed in O(1) within a huge graphic card having enough memory and cores to process the
whole thing all at once. All that being said, RNNs can’t simply disappear: it’s a fundamental
linear data structure. Articles claiming the fall of RNN have no reason to exist and twists the
facts. We shall not think of apples as oranges.
1.3
Logical reasoning leading to the idea of the LARNN
Althought Self-Attention Mechanisms are there to stay, it is not the case that RNNs can be fully
replaced. This is supported by Yoshua Bengio, as in his paper about The Consciousness Prior
[Ben17], where he formalizes that consciousness evolves linearly through time, just like an RNN or
like an LSTM such as seen in Figure 1. In his (yet still very underrated paper), he introduces the
consciousness RNN, which is deﬁned with the function C as such:
ct = C(ht, ct−1, zt)
where zt is a random source of noise, ct the conscious state, ct−1 the previous conscious state,
and ht a form of inputs’ representation state. Overall, it it stated that ct is a form of attention
which picked elements from ht. That being said, it’s quite reasonable to keep attentional neural
architectures to be linear in time to keep the consciousness ﬂowing through time, linearly. That
is: using Attention Mechanisms within RNNs!
Why wouldn’t such a consciousness be able to have attention over itself to digest information?
For example, let’s derive his equation such as to form a LARNN function with a consciousness C
which does not only examines its immediate past state:
ct = C(ht, ct−1, ct−2, ct−3, ..., ct−k, zt)
where k is an attention window which restricts how far the LARNN can see itself back in time,
and on which how gradients can ﬂow. This is now of complexity O(nk2) in time rather than O(n),
but the fact that k is set to be a constant is pleasing. This constant is the clever trick described
in the abstract. In practice, a queue can be used, and could have as ﬁrst item a tensor ﬁlled with
zeros, a random value, or an embedding encoding the initial setup. The queue can then be ﬁlled
through time steps and is self-contained as a single tensor which changes with every new state,
dropping too old states when the queue is full. This reduces the previous equation to:
vt = [[ct−1, ct−2, ct−3, ..., ct−k]]
ct = C(ht, vt, zt)
Note that here, we use [[·]] to denote a concatenation along the time dimension. Otherwise, we
will use [·] later to denote a concatenation along the features dimension.
2


## Page 3


Figure 1: The LSTM cell, which can be substituted by a consciousness RNN as introduced by
Yoshua Bengio. This visualization is freely available and is licensed under the CC-BY License, by
Guillaume Chevalier. For more information, visit https://github.com/guillaume-chevalier/
Linear-Attention-Recurrent-Neural-Network/tree/master/inkscape_drawings.
2
Model Architecture
2.1
Multi-Head Attention Mechanism
For a concrete implementation of the previous formula, a modiﬁed version of the Multi-Head
Attention can be used, similarly as seen in Attention Is All You Need [VSP+17], with optionally
some positional embedding to relatively index the keys back in time. Note that the positional
embedding here performs a concatenation on the features rather than an addition as originally, a
bit like a dense layer [HLWvdM17] rather than a residual layer[HZRS16]:
vt = [[ct−1, ct−2, ct−3, ..., ct−k]]
key = value = positionalEncoding(vt)
query = Wxh([xt, ht−1])
BNELUj(arg) = BatchNormj(elu(arg)) = BN(elu(arg))
at = MultiHeadSoftmax
query ∗BNELU1(key)
sqrt(dk)

∗BNELU2(values)
ct = C(ht, at, zt)
Where dk is the dimensionality of every attention head:
dk = numberFeatures/numberHeads = 2
The Batch Normalization is always 1-dimensional and applied on the features dimension, which
requires a temporary ﬂatten from a rank 3 tensor to a rank 2 tensor.
3


## Page 4


Figure 2: A concrete implementation of the LARNN and its usage of the multi-head attention
mechanism on a windowed queue of its past cell states.
K, V and Q are respectively the at-
tention mechanism’s input Keys, Values and only one Query. The most recent states c[t−1..t−k]
are arranged in a "ﬁrst in, ﬁrst out" queue of length k.
There is also the not-illustrated fact
that the query is formulated from a layer of the concatenation of ht−1 and xt on the innermost
(feature) axis. This visualization is freely available and is licensed under the CC-BY License, by
Guillaume Chevalier. For more information, visit https://github.com/guillaume-chevalier/
Linear-Attention-Recurrent-Neural-Network/tree/master/inkscape_drawings.
2.2
Special usage of Positional Encoding
The positional encoding discussed in Attention Is All You Need [VSP+17] uses a geometric series
of sines and cosines deﬁned by the following formula and as represented in Figure 3:
PE(pos, 2i) = sin(pos/100002i/dmodel)
PE(pos, 2i+1) = cos(pos/100002i/dmodel)
where dmodel is here the same as the hidden unit size, that is, the number of features in the
LARNN, akin the number of features (hidden size) in the LSTM. Their positional embedding may
contain a random phase so as to let their Neural Machine Translation (NMT) model generalize to
unknown sentences length.
In the case of the LARNN, no random phase is needed, because the LARNN always have a
window of a ﬁxed size. Therefore, the positional encoding is reversed and is therefore applied from
the most recent cell state as being the zero of the sines and cosines, then positively towards older
cell states ct (more details in the LSTM and LARNN equations later). Also, because the window
size is ﬁxed, it is no longer needed to express the encoding in function of the number of features,
but now rather in function of the window size. In the case of the LARNN, perfect exponents of
two were used for the wavelenghts, which yields its particularly "pixel-perfect" agreeable aspect,
rather than using multiples of 1000, which was originally used in Attention Is All You Need for a
reason that seems unknown reason to the best of my knowledge.
In Figure 5, it’s also possible to see that in the LARNN, the positional encoding is concatenated
to the features, rather than added to them as in Attention Is All You Need. This is to replicate
the eﬀect of a dense layer [HLWvdM17] rather than a residual layer[HZRS16].
4


## Page 5


Figure 3: The original positional encoding used in Attention Is All You Need [VSP+17], composed
of sines and cosines. Note that here, the sines and cosine has been split rather than interpolated,
and are used with a dmodel of 42 and a sequence length of 128.
Figure 4: The modiﬁed positional encoding used in the LARNN, composed of sines and cosines.
The window size is ﬁxed to 128 for visualization purposes here, which causes the greatest wavelength
to be of a quarter of its wavelength from zero to its ﬁrst peak in case of a sine. Therefore, this
type of encoding is such that its greatest wavelength is of at least four times the window size. In
practice, for the LARNN, the window size is for sure smaller than k = 128 to be linear, since in
the used dataset the sequence length is of 128, which represents 2.56 seconds worth of data. From
left to right would be placed, respectively, the most recent and the oldest windowed cell states ct.
Figure 5:
The windowed cell states ct are here represented above, concatenated on the se-
quence length (window size) temporal axis, whereas the encoding is concatenated below on
the feature size axis.
That is, there are 42 features in the cells’ states ct before the con-
catenation of the encoding which augments the number of such features to be processed
by the multi-head attention as a keys and values.
This visualization and the three pre-
vious ones are computed from the code of the project which can be found here:
https:
//github.com/guillaume-chevalier/Linear-Attention-Recurrent-Neural-Network/blob/
master/AnnotatedMultiHeadAttention.ipynb
5


## Page 6


2.3
Relationships with the Batch Normalized LSTM
We now want to place the formulas of the LSTM RNN in place of the consciousness RNN C, such
as in Figure 1. For convenience, here are some formulas for an LSTM cell. Note that here, with a
slight abuse of notation, ht is the output, and that xt is the input, whereas in the equations above,
ht is instead the input. Let’s continue by using the LSTM equations with Batch Normalization
(such as a BN-LSTM) [CBL+16], but here with an Exponential Linear Unit (ELU) activation
[CUH15], such as being:
ft =
σ(BN(Whf ht−1 + Wxf xt + bf))
it =
σ(BN(Whi ht−1 + Wxi xt + bi))
ot =
σ(BN(Who ht−1 + Wxo xt + bo))
gt = tanh(BN(Whc ht−1 + Wxc xt + bc))
Ct = BN(f ∗Ct−1 + i ∗xt ∗gt)
ht = BN(ot ∗elu(Ct))
2.4
Putting it all together
Let’s now deﬁne how it’s possible to merge the result of an attention query at inside the LSTM
formulas before incorporating this into C function to replace it with the LSTM. In fact, two
diﬀerent ways can be deﬁned as such, either one or the other - the residual or the layer mode of
joining the attention into the LSTM cell - by replacing the deﬁnition of gt as either:
gt residual mode = tanh(BN(Whc ht−1 + Wxc xt + Wac at + bc))
or:
gt layer mode = Wa([xt, ht−1, at]) + ba
With respect to the equations above to be merged and with the notation used in most of the LSTM
formulas with ht to be the output and xt the input, here, C is ﬁnally replaced by a BN-LSTM
cell with attention to create the LARNN. It is possible to ﬁnally obtain the following equations,
and with choosing optionally gt residual mode or gt layer mode, which are both listed. We obtain
something akin to what’s seen in the Figure 2 which is an oversimpliﬁed representation of the
LARNN implementation which goes like:
vt = [[ct−1, ct−2, ct−3, ..., ct−k]]
key = value = positionalEncoding(vt)
query = Wxh([xt, ht−1])
BNELUj(arg) = BatchNormj(elu(arg)) = BN(elu(arg))
at = MultiHeadSoftmax
query ∗BNELU1(key)
sqrt(dk)

∗BNELU2(values)
ft =
σ(BN(Whf ht−1 + Wxf xt + bf))
it =
σ(BN(Whi ht−1 + Wxi xt + bi))
ot =
σ(BN(Who ht−1 + Wxo xt + bo))
gt residual mode = tanh(BN(Whc ht−1 + Wxc xt + Wac at + bc))
gt layer mode = Wa([xt, ht−1, at]) + ba
Ct = BN(f ∗Ct−1 + i ∗xt ∗gt)
ht = BN(ot ∗elu(Ct))
Note again that in the experiments here made, the BN-LSTM was modiﬁed such as to have an
Exponential Linear Unit (ELU) activation [CUH15] in plus of Batch Normalization. This was a
cheap ineﬃcient trick to blindly try to obtain better results from an engineer’s point of view. Note
that such BN-ELU normalization was also added to the Multi-Head’s linear mappings of the keys
and values, which improved results too, as discussed in the analysis below.
6


## Page 7


3
Training Procedure and Results
The training of the concrete implementation of the LARNN was performed with Hyperopt using
the TPE algorithm [BYC13], which is yields better results than a random hyperparameter search
and a grid search [BB12]. Two rounds of the TPE algorithm were performed. In the ﬁrst round,
many hyperparameters were set to vary a lot in order for the search to be in diﬀuse mode, and then
later on in a second round, the search was set to a focused mode [RS07], that is, by restraining
the area of where the search is performed by ﬁxing some hyperparameters to their best value or
towards a good range of values. The dataset used was the Public Domain Dataset for Human
Activity Recognition using Smartphones [AGO+13] by Anguita, Davide, et al., as uploaded on
the UCI Machine Learning Repository. In this paper’s code, this dataset is named the UCIHAR
dataset.
3.1
Accuracies of Every Trained Model and Hyperparameters Analysis
It is possible to see in Figure 6 and in Figure 7 the accuracies obtained at, respectively, round 1
and round 2. Also, the eﬀect of every hyperparameters related to each other are visualized in two
scatter plots for the round 1 and the round 2 in Figure 8 and in Figure 9. Those plots are not an
ablation study, but are close to be. For example, sometimes diﬀerent types of LARNN modes are
used to create the layers, and sometimes the densely concatenated positional encoding is turned oﬀ.
The training was carried on Amazon AWS’s p3.2xlarge instances, that is, with NVIDIA Tesla
V100 GPUs of 16 GB RAM with 640 NVIDIA Tensor cores and 5’120 NVIDIA CUDA cores
oﬀering more than 100 TFLOPS. The total costs were of $344.17 USD at a cost of $3.06 USD per
hour, which means 112 hours of GPU usage.
From the charts, it’s possible to see that the positional encoding did not help. Also, it’s better to
stack the two or three cells in a residual fashion, such as to add their ht together at layer 1 and
layer 2 before the ﬁnal classiﬁcation layer which is placed at the last time step. Also, it appears
that the best LARNN mode is the "residual" one, while the "layer" one yields average results in
the round 2. It’s also possible to observe that the results are better when placing an activation
on the Multi-Head Attention’s linear mappings before the dot products and attention products
are made, as seen in Figure 10. which is quite interesting and may orient future research when
using Multi-Head Attention. As a reminder: the activation used is a Batch Normalization on an
ELU activation of the linears. The Batch Normalization is 1-dimensional on the features dimension.
It can obtain results of 91.924% for the test accuracy, compared to the previously attained
91.653% using vanilla LSTM cells.
7


## Page 8


Figure
6:
Plot
illustrating
the
test
accuracy
of
every
trials
through
25
epochs
for
the
round
1
of
hyperparameters
optimization.
For
more
information,
visit
https:
//github.com/guillaume-chevalier/Linear-Attention-Recurrent-Neural-Network/blob/
master/AnalyzeTestHyperoptResults_round_1.ipynb.
8


## Page 9


Figure
7:
Plot
illustrating
the
test
accuracy
of
every
trials
through
100
epochs
for
the
round
2
of
hyperparameters
optimization.
For
more
information,
visit
https:
//github.com/guillaume-chevalier/Linear-Attention-Recurrent-Neural-Network/blob/
master/AnalyzeTestHyperoptResults_round_2.ipynb.
9


## Page 10


Figure 8:
Scatter plot depicting the eﬀect of every hyperparameters in relation to each
other for the optimization round 1.
For more information,
visit https://github.com/
guillaume-chevalier/Linear-Attention-Recurrent-Neural-Network/blob/master/
AnalyzeTestHyperoptResults_round_1.ipynb.
10


## Page 11


Figure 9:
Scatter plot depicting the eﬀect of every hyperparameters in relation to each
other for the optimization round 2.
For more information,
visit https://github.com/
guillaume-chevalier/Linear-Attention-Recurrent-Neural-Network/blob/master/
AnalyzeTestHyperoptResults_round_2.ipynb.
11


## Page 12


Figure 10: Test accuracy throughout training for when batch-normalized ELU activation is used
on the keys and values’ linear layers of the Multi-Head Attention Mechanism. This is an interesting
discovery considering Multi-Head Attention Mechanisms are now, at the time of writing, the State
Of The Art (SOTA) methods in solving Natural Language Processing (NLP) problems such as Neu-
ral Machine Translation (NMT), as done in 2017 in the Attention Is All You Need paper [VSP+17],
and bringing NLP systems closer to Artiﬁcial General Intelligence (AGI) such as in the One Model
To Learn Them All paper [KGS+17] using a Multi-Head Dot-Product Attention. However, note
that the LARNN have still not been tested on NLP tasks as of today, it has only been tested on
the sensors dataset used here. For more information on how this ﬁgure was generated, visit https:
//github.com/guillaume-chevalier/Linear-Attention-Recurrent-Neural-Network/blob/
master/AnalyzeTestHyperoptResults_round_1.ipynb.
12


## Page 13


4
Conclusion
It is possible to infer new equations from the consciousness RNN and the Multi-Head Attention
Mechanisms to create a LARNN which makes use the attention to augment the range of its
consciousness.
Moreover, intesresting hyperparameter exploration yields insights on what is
useful to this neural architecture and what’s not. For example, positional encoding did not seem
to help speciﬁcally for this task if it is added in a dense manner, and also I discovered that
batch-normalized activation on the linear mappings of the multi-head attention mechanism helped
the model on the Test set predictions.
5
Acknowledgements
Thanks to Yu Zhao for having participated in the HAR-stacked-residual-bidir-LSTMs [ZYCG17]
project with me, which is licensed under the Apache 2.0 license, a project from which I reused
some code for loading the dataset. In turns, this code was originally derived from my own project
available at https://github.com/guillaume-chevalier/LSTM-Human-Activity-Recognition.
Also, thanks to Vooban for open-sourcing and sublicensing under the MIT License its derivative
of my code https://github.com/guillaume-chevalier/Hyperopt-Keras-CNN-CIFAR-100 now
at the address https://github.com/Vooban/Hyperopt-Keras-CNN-CIFAR-100, which I was able
to reuse here as boilerplate code to setup the hyperparameter search.
More details on the licenses can be obtained at the respective address of each project.
I’d
like
to
also
thanks
Philippe
Giguère,
Professor
at
Université
Laval,
who
cre-
ated a nice class on deep learning,
such as listed in my awesome resources:
https:
//github.com/guillaume-chevalier/Awesome-Deep-Learning-Resources.
I
especially
liked his rare visualization of the multi-head attention mechanism, which is available in his
slides at https://ulaval-damas.github.io/glo4030/, and more precisely, at the page 28 of his
slides here: http://www2.ift.ulaval.ca/~pgiguere/cours/DeepLearning/09-Attention.pdf.
The
LARNN
repository
is
available
at
https://github.com/guillaume-chevalier/
Linear-Attention-Recurrent-Neural-Network,
available
under
the
MIT
License,
and
coded with PyTorch [PGC+17].
13


## Page 14


References
[AGO+13]
Davide Anguita, Alessandro Ghio, Luca Oneto, Xavier Parra, and Jorge Luis Reyes-
Ortiz. A public domain dataset for human activity recognition using smartphones.
In ESANN, 2013.
[BB12]
James Bergstra and Yoshua Bengio. Random search for hyper-parameter optimiza-
tion. Journal of Machine Learning Research, 13(Feb):281–305, 2012.
[BCB14]
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine trans-
lation by jointly learning to align and translate. arXiv preprint arXiv:1409.0473,
2014.
[Ben17]
Yoshua Bengio. The consciousness prior. arXiv preprint arXiv:1709.08568, 2017.
[BYC13]
James Bergstra, Dan Yamins, and David D Cox. Hyperopt: A python library for
optimizing the hyperparameters of machine learning algorithms. In Proceedings of
the 12th Python in Science Conference, pages 13–20. Citeseer, 2013.
[CBL+16]
Tim Cooijmans, Nicolas Ballas, César Laurent, Çağlar Gülçehre, and Aaron
Courville. Recurrent batch normalization. arXiv preprint arXiv:1603.09025, 2016.
[CUH15]
Djork-Arné Clevert, Thomas Unterthiner, and Sepp Hochreiter.
Fast and ac-
curate deep network learning by exponential linear units (elus).
arXiv preprint
arXiv:1511.07289, 2015.
[HLWvdM17] Gao Huang, Zhuang Liu, Kilian Q Weinberger, and Laurens van der Maaten.
Densely connected convolutional networks. In Proceedings of the IEEE conference
on computer vision and pattern recognition, volume 1, page 3, 2017.
[HS97]
Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. Neural com-
putation, 9(8):1735–1780, 1997.
[HZRS16]
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning
for image recognition. In Proceedings of the IEEE conference on computer vision
and pattern recognition, pages 770–778, 2016.
[KGS+17]
Lukasz Kaiser, Aidan N Gomez, Noam Shazeer, Ashish Vaswani, Niki Parmar,
Llion Jones, and Jakob Uszkoreit. One model to learn them all. arXiv preprint
arXiv:1706.05137, 2017.
[PGC+17]
Adam Paszke, Sam Gross, Soumith Chintala, Gregory Chanan, Edward Yang,
Zachary DeVito, Zeming Lin, Alban Desmaison, Luca Antiga, and Adam Lerer.
Automatic diﬀerentiation in pytorch. In NIPS-W, 2017.
[RS07]
Marcus E Raichle and Abraham Z Snyder. A default mode of brain function: a brief
history of an evolving idea. Neuroimage, 37(4):1083–1090, 2007.
[VDODZ+16] Aaron Van Den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals,
Alex Graves, Nal Kalchbrenner, Andrew Senior, and Koray Kavukcuoglu. Wavenet:
A generative model for raw audio. arXiv preprint arXiv:1609.03499, 2016.
[VSP+17]
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N
Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Advances
in Neural Information Processing Systems, pages 6000–6010, 2017.
[ZYCG17]
Yu Zhao, Rennong Yang, Guillaume Chevalier, and Maoguo Gong.
Deep resid-
ual bidir-lstm for human activity recognition using wearable sensors.
CoRR,
abs/1708.08989, 2017.
14

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 1808_05578v1_larnn_linear_attention_recurrent_neural_network
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1808_05578V1_LARNN_LINEAR_ATTENTION_RECURRENT_NEURAL_NETWORK.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
