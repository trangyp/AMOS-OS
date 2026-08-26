---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.01933
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1911.01933_Training_Neural_Machine_Translation__NMT__Models_using_Tensor_Train_Decompositio

> Source: 1911.01933_Training_Neural_Machine_Translation__NMT__Models_using_Tensor_Train_Decompositio.pdf

> Pages: 10

---


## Page 1


arXiv:1911.01933v1  [cs.LG]  5 Nov 2019
Training Neural Machine Translation (NMT)
Models using Tensor Train Decomposition on
TensorFlow (T3F)
Amelia Drew and Alexander Heinecke
November 6, 2019
Abstract
We implement a Tensor Train layer in the TensorFlow Neural Machine
Translation (NMT) model using the t3f library. We perform training runs
on the IWSLT English-Vietnamese ’15 and WMT German-English ’16
datasets with learning rates ∈{0.0004, 0.0008, 0.0012}, maximum ranks
∈{2, 4, 8, 16} and a range of core dimensions. We compare against a tar-
get BLEU test score of 24.0, obtained by our benchmark run. For the
IWSLT English-Vietnamese training, we obtain BLEU test/dev scores of
24.0/21.9 and 24.2/21.9 using core dimensions (2, 2, 256)×(2, 2, 512) with
learning rate 0.0012 and rank distributions (1, 4, 4, 1) and (1, 4, 16, 1) re-
spectively. These runs use 113% and 397% of the ﬂops of the benchmark
run respectively. We ﬁnd that, of the parameters surveyed, a higher learn-
ing rate and more ‘rectangular’ core dimensions generally produce higher
BLEU scores. For the WMT German-English dataset, we obtain BLEU
scores of 24.0/23.8 using core dimensions (4, 4, 128)×(4, 4, 256) with learn-
ing rate 0.0012 and rank distribution (1, 2, 2, 1). We discuss the potential
for future optimization and application of Tensor Train decomposition to
other NMT models.
1
Introduction
Neural Machine Translation (NMT) is a deep learning model that provides a
robust method for machine translation using recurrent neural networks (RNNs).
Originally proposed in [1], NMT relies primarily on an encoder-decoder archi-
tecture that provides increased ﬂuency over phrase-based systems. This was
implemented successfully in [2] for fast, accurate use on very large datasets.
However, it has been suggested that there is signiﬁcant redundancy in the cur-
rent method of neural network parametrization [3], presenting the opportunity
for signiﬁcant speedup.
Tensor Train (TT) decomposition [4] is a method by which large tensors can
be approximated by the product of a ‘train’ of smaller matrices (see Section 2.2).
1


## Page 2


TT-decomposition has been proposed as a method of speeding up and reducing
the memory usage of machine translation systems with dense weight matrices
by reducing the number of parameters required to describe the system [3]. The
dense weight matrix of the fully-connected layers can be decomposed into the
Tensor Train format, creating what we will refer to as a ‘TT-layer’. This lower-
rank factorization can then be trained in a similar way to the original dense
weight matrix. In this work, we execute a TT-layer using t3f, a library which
enables straightforward implementation of TT-decomposition within Tensor-
Flow models. T3f provides an implementation with GPU support, eliminating
the need to rewrite core functionality from scratch, which has been necessary
for previous libraries (see [5]).
In Section 2, we provide an outline of Neural Machine Translation (NMT)
and the Tensor Train format, with our methodology outlined in Section 3. We
present the results of our training runs in Section 4 and our conclusions and
suggestions for further work are provided in Section 5.
2
Background
2.1
Neural Machine Translation
Neural Machine Translation (NMT) is a method of machine translation that
uses an encoder-decoder architecture to coherently translate whole sentences
by capturing long range dependencies. This creates more ﬂuent and accurate
results in contrast to previous phrase-based approaches [6]. The encoder and
decoder use recurrent neural networks (RNNs) to train the model, ﬁnally en-
abling translation of an input source vector x to an output y using the linear
transformation
y = Wx + b ,
(1)
where the weight matrix W and bias vector b are trained by the model.
There are a wide range of RNN models that diﬀer, for example, in terms
of directionality (unidirectional or bidirectional), depth (single- or multi-layer)
and type (straightforward RNN, Long Short-term Memory (LSTM), or a gated
recurrent unit (GRU)). Here, we use a deep multi-layer RNN with Long Short-
term Memory (LSTM) as a recurrent unit. This high level NMT model consists
of two recurrent neural networks; the encoder consumes input source words to
build a ‘thought’ vector, while the decoder processes the vector to emit a trans-
lation, thereby using information from the entire source sentence [7]. Further
information about this particular model can be found in [6].
2.2
Tensor Train Decomposition
The Tensor Train (TT) format can be used to represent the dense weight matrix
W of a fully-connected layer using fewer parameters. In this work, we implement
a ‘TT-layer’ as described in [3]; a fully-connected layer with the weight matrix
2


## Page 3


stored in the TT-format. The following outline follows the descriptions given in
[4] and [3] and uses similar notation.
A tensor A is said to be represented in the TT-format if there exist matrices
Gk(ik) such that all the elements of A can be computed by the matrix product
A(i1, i2, ..., id) = G1(i1)G2(i2)...Gd(id),
(2)
where ik index the tensor elements and Gk(ik) is an rk−1 × rk matrix, where
{rk}d
k=0 are the ‘ranks’ of the TT-representation. The values r0 and rd equal 1
in order to keep the matrix product (2), and hence each element of A, of size
1 × 1. Note that each matrix Gk(ik) is actually a (rk−1 × βk × rk) array with
elements Gk(αk−1, βk, αk) = Gk(ik)αk−1αk, using which we can write equation
(2) in index form:
A(i1, i2, ..., id) =
X
α0,...,αd−1,αd
G1(α0, i1, α1)G2(α1, i2, α2)...Gd(αd−1, id, αd) .
(3)
Each three-dimensional tensor Gk is referred to as a ‘core’ of the TT-decomposition.
The weight matrix W(i1, i2) ∈RM×N, where M = Qd
k=1 mk and N =
Qd
k=1 nk, can be written in Tensor Train form. We deﬁne bijections ν(i1) =
(ν1(i1), . . . , νd(i1)) and µ(i2) = (µ1(i2), . . . , µd(i2)), mapping the row and col-
umn indices i1 and i2 to d-dimensional vector-indices, whose k-th dimensions
are of length mk and nk respectively. In this case, the cores Gk((νk(i1), µk(i2))
are now described by a four dimensional (rk−1 × mk × nk × rk) array. We will
not go further into the mathematical details here, as the precise implementation
is handled by the t3f library. Further information can be found in [3].
In this paper, we use an explicit notation of the form (rk−1, mk, nk, rk)
to clarify the shape of the tensors that we are training.
We choose d =
3, splitting each weight matrix into 3 cores.
For example, for a rank dis-
tribution (r0, r1, r2, r3) = (1, 4, 4, 1) and an underlying weight matrix shape
(m1, m2, m3) × (n1, n2, n3) = (2, 2, 256) × (2, 2, 512), the shapes of the cores
being trained are given by Table 1.
Core
Tensor Shape
(rk−1, mk, nk, rk)
G1
(1, 2, 2, 4)
G2
(4, 2, 2, 4)
G3
(4, 256, 512, 1).
Table 1: Tensor Train dimensions for a weight matrix in TT-format with d = 3,
rank distribution (r0, r1, r2, r3) = (1, 4, 4, 1) and an underlying matrix shape
(m1, m2, m3) × (n1, n2, n3) = (2, 2, 256) × (2, 2, 512). For example, core G1 is a
2 × 2 array of 1 × 4 matrices.
3


## Page 4


3
Methodology
We implement the TT-format in the TensorFlow NMT model [6], decomposing
the weight matrix using the t3f library [5] as described in Section 2.2 to create a
TT-layer. We achieve this by creating a new BasicLSTMCell class, the code for
which is provided in the Appendix. The TT-decomposition itself is performed
using the key function t3f.to tt matrix as follows:
kernel TT = t 3 f . to tt ma tr ix ( s e l f . kernel ,
shape =((2 ,2 , input parameter ) ,
(2 ,2 , s e l f . num units )) ,
max tt rank =4) ,
where the maximum rank r = maxk=0,...,d rk is set by max tt rank and the
product of the core dimensions is determined by the original dimensions of the
weight matrix. The above code implements the speciﬁc example with the core
dimensions given in Table 1. The max tt rank and shape arguments can be
changed as necessary for diﬀerent conﬁgurations of ranks and core dimensions.
Note that, as outlined in Section 2.2, the core dimensions mk and nk must
be chosen such that M = Qd
k=1 mk and N = Qd
k=1 nk for a weight matrix
W ∈RM×N.
We test our TT model by training on two publicly available datasets. First,
we perform benchmark tests using the original TensorFlow NMT model and a
similar model which uses a low-rank approximation factorization. We then carry
out approximately 20 training runs with diﬀerent parameters using the IWSLT
English-Vietnamese ’15 dataset1 with 133K examples to determine which con-
ﬁgurations give results competitive with those achieved by the benchmarks.
Second, we train the WMT German-English ’16 dataset2 with 4.5M examples
to test the suitability of our model for larger datasets. All training runs are
performed on Nvidia Tesla P100 GPUs.
4
Results
4.1
IWSLT English-Vietnamese ’15
4.1.1
Benchmark
We ﬁrst perform a benchmark run against which to compare our TT model,
using similar hyperparameters to the IWSLT English-Vietnamese training in
[6]. We use a 2-layer LSTM with 512 hidden units, a bidirectional encoder (i.e.,
1 bidirectional layer for the encoder) and embedding dimension 512. LuongAt-
tention is used with scale=True, together with dropout probability 0.2. We use
the Adam optimizer with learning rate 0.0004. We train for 12K steps (∼12
epochs) where after 6K steps, we halve the learning rate every 600 steps.
We obtain a BLEU test/dev [8] score of 24.1/22.6, reaching a score of
24.0/22.4 after 7K steps.
For our Tensor Train runs, we would like to test
1https://sites.google.com/site/iwsltevaluation2015/
2http://www.statmt.org/wmt16/translation-task.html
4


## Page 5


whether we can reach a comparable accuracy with a comparable number (or
fewer) total ﬂops. We therefore choose the cutoﬀBLEU test = 24.0 as a target
against which to compare.
4.1.2
Low-Rank Approximation
We perform a second benchmark run with the weight matrix W decomposed
using a low-rank approximation factorization inspired by Singular Value De-
composition (SVD). We assume such a decomposition exists and initialise and
train the matrices W1 and W2 deﬁned by W = W1W2, changing the order of
computation of Wx in equation (1) from X(W1W2) to (XW1)W2. Reordering
the calculation in this way reduces the number of ﬂops from 2MNK, where K
is the batch size, to 2MKD +2KND, where D is an appropriately chosen SVD
dimension. It is implemented by splitting the tf.matmul as follows:
g a te inputs = t f . matmul( t f . matmul( t f . concat ( [ inputs , h ] ,
1) ,
s e l f .
ker nel svd 1 ) ,
s e l f .
ker nel svd 2 )
We perform one benchmark run on the IWSLT English-Vietnamese dataset
using the same parameters as in Section 4.1.1. We obtain a BLEU test/dev
score of 24.8/22.5 after 12K steps, reaching a score of 24.0/22.1 after 7K steps.
4.1.3
Tensor Train
We perform approximately 20 training runs on the IWSLT English-Vietnamese
dataset with the weight matrix W decomposed using Tensor Train decomposi-
tion. We use a range of maximum rank r ∈{2, 4, 8, 16} and initial core dimen-
sions (m1, m2, m3)×(n1, n2, n3) ∈{(2, 2, 256)×(2, 2, 512), (4, 4, 64)×(4, 4, 128),
(8, 8, 16)×(8, 8, 32)}. All tests were performed using the same parameters as the
benchmark runs, other than the learning rate, which is speciﬁed as necessary.
All runs were performed using one GPU and take approximately 1-2 hours. For
the runs which obtain BLEU test ≥24.0, we report the total percentage of
ﬂops used compared with the original model. For the rest, we report the BLEU
scores after 12000 training steps. The results are given in Table 2.
We ﬁnd that the IWSLT dataset obtains a BLEU test score ≥24.0 for core
dimensions (m1, m2, m3) × (n1, n2, n3) = (2, 2, 256) × (2, 2, 512) with learning
rate 0.0012 and rank distributions (1, 4, 4, 1) and (1, 4, 16, 1), for which we obtain
BLEU test/dev = 24.0/21.9 and 24.2/21.9 respectively. These runs use 113%
and 397% of the ﬂops of the benchmark run respectively. We also ﬁnd in general
that increasing the learning rate increases the BLEU score within a given number
of steps, as does a lower max mk and max nk.
4.2
WMT German-English ’16
For the WMT German-English dataset, we again use hyperparameters similar
to the corresponding experiment outlined in [6]. We train 4-layer LSTMs of 1024
units with a bidirectional encoder (i.e., 2 bidirectional layers for the encoder)
5


## Page 6


Rank Dist.
Weight Matrix Dimensions
Learning
BLEU
Flops
(r0, r1, r2, r3)
(m1, m2, m3) × (n1, n2, n3)
Rate
test/dev
%
Original Model:
24.0/22.4
100%
Low-Rank Model:
24.0/22.1
69%
(1, 2, 2, 1)
(2, 2, 256) × (2, 2, 512)
0.0012
23.3/21.8
84%
0.0008
21.7/20.1
-
0.0004
18.8/17.3
-
(1, 4, 4, 1)
(2, 2, 256) × (2, 2, 512)
0.0012
24.0/21.9
113%
-
0.0008
23.0/21.6
-
0.0004
21.5/19.9
-
(4, 4, 64) × (4, 4, 128)
0.0012
23.0/20.8
-
0.0008
22.3/20.7
-
0.0004
20.8/19.0
-
(8, 8, 16) × (8, 8, 32)
0.0012
22.3/20.8
-
0.0008
21.8/20.6
-
0.0004
19.9/18.6
-
(1, 4, 8, 1)
(2, 2, 256) × (2, 2, 512)
0.0012
23.9/22.1
-
0.0008
23.7/21.9
-
0.0004
23.0/21.3
-
(1, 8, 8, 1)
(4, 4, 64) × (4, 4, 128)
0.0012
23.2/21.6
-
0.0008
23.1/21.5
-
0.0004
21.8/20.4
-
(8, 8, 16) × (8, 8, 32)
0.0012
23.1/21.1
-
0.0008
22.3/20.6
-
0.0004
20.9/19.4
-
(1, 4, 16, 1)
(2, 2, 256) × (2, 2, 512)
0.0012
24.2/21.9
397%
0.0008
24.1/21.6
397%
0.0004
23.3/21.5
-
(1, 16, 16, 1)
(4, 4, 64) × (4, 4, 128)
0.0012
23.4/22.0
-
0.0008
23.1/21.2
-
0.0004
22.9/21.3
-
(8, 8, 16) × (8, 8, 32)
0.0012
23.0/21.5
-
0.0004
21.3/20.0
-
Table 2: Training results for IWSLT English-Vietnamese ’15 dataset.
The
weight matrix dimensions are the dimensions for the ﬁrst layer (later layers
have diﬀerent dimensions, which are taken into account when calculating the
percentage ﬂops). For runs which obtain BLEU test ≥24.0, the total percent-
age of ﬂops used compared with the original model is reported and highlighted
in bold. For the rest, we report the BLEU scores after 12000 training steps.
with embedding dimension 1024, using the Adam optimizer and a learning rate
0.0012. We train for 340K steps (∼10 epochs) where after 170K steps, we halve
the learning rate every 17K steps. The data is split into subword units using
6


## Page 7


BPE (32K operations).
We perform one training run using a rank distribution (1, 2, 2, 1) and core
dimensions (4, 4, 128) × (4, 4, 256). This run was performed using 4 GPUs and
took approximately 5 days. We obtain a ﬁnal BLEU test/dev score of 24.0/23.8.
We also attempted training runs using core dimensions (2, 2, 512)×(2, 2, 1024)
and a maximum rank r ∈{2, 4, 8}, also on 4 GPUs. We ﬁnd that for these conﬁg-
urations, the application crashes due to a lack of memory. As the total number
of parameters should be less than the original model when using Tensor Train
decomposition, we assume this is due to intermediate copies of the matrices
being stored. However, this requires further investigation.
5
Conclusion and Future Work
We have successfully implemented TT-layers for the TensorFlow NMT model
using the t3f Tensor Train library. We have performed training runs on two
datasets, the ﬁrst using the IWSLT English-Vietnamese ’15 dataset and the
second with the WMT German-English ’16 dataset. We ﬁnd that the IWSLT
model obtains a BLEU test score ≥24.0 for the core dimensions (m1, m2, m3)×
(n1, n2, n3) = (2, 2, 256) × (2, 2, 512) with learning rate 0.0012 and rank dis-
tributions (1, 4, 4, 1) and (1, 4, 16, 1), for which we obtain BLEU test/dev =
24.0/21.9 and 24.2/21.9 respectively.
We also ﬁnd that, of the parameters
surveyed, a higher learning rate and more ‘rectangular’ weight matrix decom-
position, i.e.
a lower max mk and max nk, generally produce higher BLEU
scores. We have also performed one successful training run using the larger
WMT German-English dataset, using core dimensions (4, 4, 128) × (4, 4, 256)
and rank distribution (1, 2, 2, 1). We obtained a ﬁnal BLEU test/dev score of
24.0/23.8.
This work shows that TT-layers can be straightforwardly introduced to the
TensorFlow NMT model and can obtain BLEU scores compatible with the origi-
nal. With optimization, there is potential for this model to enable more eﬃcient
model training using fewer ﬂops, less memory and less overall training time.
Training on larger datasets is currently limited by the memory consumption of
the model, despite the fact that Tensor Train decomposition should use fewer
parameters. This suggests that the t3f library stores intermediate copies of the
matrices, which could be addressed in future work on optimization. Finally,
there is further scope to apply this decomposition to the Transformer model [9],
which produces the best BLEU results at the time of writing, with the potential
to improve its eﬃciency.
Acknowledgements
This work was undertaken on the Fawcett supercomputer at the Department of
Applied Mathematics and Theoretical Physics (DAMTP), University of Cam-
bridge, funded by STFC Consolidated Grant ST/P000673/1. We would like
7


## Page 8


to thank Yang You for his work on the low-rank matrix format Singular Value
Decomposition, and Cole Hawkins for useful comments.
AD is supported by an EPSRC iCASE Studentship in partnership with Intel
(EP/N509620/1, Voucher 16000206).
References
[1] Ilya Sutskever, Oriol Vinyals, and Quoc V. Le. Sequence to sequence learning
with neural networks. Advances in Neural Information Processing Systems,
page 3104–3112, 2014.
[2] Yonghui Wu et al. Google’s neural machine translation system: Bridging
the gap between human and machine translation. arXiv:1609.08144, 2016.
[3] Alexander Novikov, Dmitry Podoprikhin1, Anton Osokin, and Dmitry
Vetrov. Tensorizing neural networks. arXiv:1509.06569, 2015.
[4] Ivan Oseledets. Tensor-train decomposition. SIAM J. Scientiﬁc Computing,
33(5):2295–2317, 2011.
[5] Alexander Novikov, Pavel Izmailov, Valentin Khrulkov, Michael Figurnov,
and Ivan Oseledets.
Tensor train decomposition on tensorﬂow (t3f).
arXiv:1801.01928, 2018.
[6] Minh-Thang Luong, Eugene Brevdo, and Rui Zhao. Neural machine trans-
lation (seq2seq) tutorial. https://github.com/tensorﬂow/nmt, 2017.
[7] Minh-Thang Luong. Neural machine translation. Dissertation, 2016.
[8] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu.
Bleu:
a method for automatic evaluation of machine translation. Proceedings of
the 40th Annual Meeting of the Association for Computational Linguistics
(ACL), 2002.
[9] Ashish Vaswani et al. Attention is all you need. arXiv:1706.03762, 2017.
Appendix
class BasicLSTMCellTT( t f . nn . r n n c e l l . BasicLSTMCell ) :
””” c . f .
t f . nn . r n n c e l l . BasicLSTMCell
h t t p s :// githu b .com/ tensorflow / tensorflow / blob /master/
tensorflow /python /ops/ r n n c e l l i m p l . py ”””
def
i n i t
( s e l f ,
num units ,
f o r g e t b i a s =1.0 ,
s t a t e i s t u p l e=True ,
a ctiva tio n=None ,
reuse=None , name=None ) :
super(BasicLSTMCellTT ,
s e l f ) .
i n i t
(
num units ,
f o r g e t b i a s ,
s t a t e i s t u p l e ,
activation ,
8


## Page 9


reuse , name)
def build ( s e l f ,
inputs shape ) :
i f
inputs shape [ 1 ] . value
i s None :
raise
ValueError (
”Expected inputs . shape [ −1 ]
to be known ,
saw shape : %s”
% inputs shape )
input depth = inputs shape [ 1 ] . value
h depth = s e l f . num units
s e l f .
ker nel = s e l f . add variable (
’ kernel ’ ,
shape=[ input depth + h depth ,
4 ∗
s e l f . num units ] )
input parameter = int ( s e l f .
ker nel . shape [ 0 ]
// 4)
kernel TT = t 3 f . to tt ma tr ix ( s e l f . kernel ,
shape =((2 ,2 , input parameter ) ,(2 ,2 , s e l f . num units )) ,
max tt rank=4)
s e l f . kernel TT 0 = s e l f . add variable (
’ kernel TT 0 ’ ,
shape=kernel TT . t t c o r e s [ 0 ] . get shape ( ) )
s e l f . kernel TT 1 = s e l f . add variable (
’ kernel TT 1 ’ ,
shape=kernel TT . t t c o r e s [ 1 ] . get shape ( ) )
s e l f . kernel TT 2 = s e l f . add variable (
’ kernel TT 2 ’ ,
shape=kernel TT . t t c o r e s [ 2 ] . get shape ( ) )
s e l f .
b i a s = s e l f . add variable (
’ bias ’ ,
shape=[4 ∗
s e l f . num units ] ,
i n i t i a l i z e r=t f . z e r o s i n i t i a l i z e r ( dtype=s e l f . dtype ))
s e l f . b u i l t = True
def
c a l l ( s e l f ,
inputs ,
sta te ) :
sigmoid = t f . sigmoid
one = t f . constant (1 ,
dtype=t f . int32 )
# Parameters
of
gates
are
concatenated
into
one
# mu ltiply
for
e f f i c i e n c y .
9


## Page 10


i f
s e l f .
s t a t e i s t u p l e :
c , h = sta te
else :
c , h = t f . s p l i t ( value=state ,
n u m o r s i z e s p l i t s =2,
a xis=one )
c o r e s t u p l e = ( s e l f . kernel TT 0 ,
s e l f . kernel TT 1 ,
s e l f . kernel TT 2 )
reconstructed kernel TT = t 3 f . TensorTrain ( c o r e s t u p l e )
g a te inputs = t 3 f . matmul( t f . concat ( [ inputs , h ] ,
1) ,
reconstructed kernel TT )
g a te inputs = t f . nn . bias add ( gate inputs ,
s e l f .
b i a s )
# i = input gate ,
j = new input ,
f = f o r g e t g a t e ,
#
o = ou tpu t gate
i ,
j ,
f ,
o = t f . s p l i t (
value=gate inputs ,
n u m o r s i z e s p l i t s =4, a xis=one )
f o r g e t b i a s t e n s o r = t f . constant ( s e l f .
f o r g e t b i a s ,
dtype=f . dtype )
add = t f . add
multiply = t f . multiply
new c = add( multiply ( c ,
sigmoid ( add( f ,
f o r g e t b i a s t e n s o r ) ) ) ,
multiply ( sigmoid ( i ) ,
s e l f .
a c t i v a t i o n ( j ) ) )
new h = multiply ( s e l f .
a c t i v a t i o n ( new c ) ,
sigmoid ( o ))
i f
s e l f .
s t a t e i s t u p l e :
new state = t f . nn . r n n c e l l . LSTMStateTuple ( new c ,
new h )
else :
new state = t f . concat ( [ new c ,
new h ] ,
1)
return new h ,
new state
10

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1911_01933_training_neural_machine_translation_nmt_models_using_tensor_train_decompositio
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1911_01933_TRAINING_NEURAL_MACHINE_TRANSLATION_NMT_MODELS_USING_TENSOR_TRAIN_DECOMPOSITIO.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
