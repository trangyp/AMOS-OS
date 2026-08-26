---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.13162
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1910.13162_An_Efficient_Model_for_Sentiment_Analysis_of_Electronic_Product_Reviews_in_Vietn

> Source: 1910.13162_An_Efficient_Model_for_Sentiment_Analysis_of_Electronic_Product_Reviews_in_Vietn.pdf

> Pages: 12

---


## Page 1


An Eﬃcient Model for Sentiment Analysis of
Electronic Product Reviews in Vietnamese ⋆
Suong N. Hoang1,2[0000−0002−3354−013X], Linh V. Nguyen1[0000−0003−0776−9480],
Tai Huynh1,2, and Vuong T. Pham1,3
1 Kyanon Digital, Ho Chi Minh City, Vietnam
{suong.hoang,linh.nguyenviet,tai.huynh,vuong.pham}@kyanon.digital
https://kyanon.digital
2 Advosights, Ho Chi Minh City, Vietnam
{suong.hoang,tai.huynh}@advosights.com
https://advosights.com
3 Saigon University, Ho Chi Minh City, Vietnam
vuong.pham@sgu.edu.vn
Abstract. In the past few years, the growth of e-commerce and digital
marketing in Vietnam has generated a huge volume of opinionated data.
Analyzing those data would provide enterprises with insight for better
business decisions. In this work, as part of the Advosights project, we
study sentiment analysis of product reviews in Vietnamese. The ﬁnal
solution is based on Self-attention neural networks, a ﬂexible architec-
ture for text classiﬁcation task with about 90.16% of accuracy in 0.0124
second, a very fast inference time.
Keywords: Vietnamese · sentiment analysis · electronics product re-
view.
1
Introduction
Sentiment analysis aims to analyze human opinions, attitudes, and emotions.
It has been applied in various ﬁelds of business. For instance, in our current
project, Advosights, it is used to measure the impact of new products and ads
campaigns through consumer’s responses.
In the past few years, together with the rapid growth of e-commerce and dig-
ital marketing in Vietnam, a huge volume of written opinionated data in digital
form has been created. As the result, sentiment analysis plays a more critical
role in social listening than ever before. So far, human eﬀort is the most common
solution for sentiment analysis problems. However, this approach generally does
not result in the desired outcomes and speed. Human check and labeling are time
consuming and error-prone. Therefore, developing a system that automatically
classiﬁes human sentiment is highly essential.
While we can easily ﬁnd a lot of sentiment analysis researches for English,
there are only a few works for Vietnamese. Vietnamese is a unique language
⋆Supported by Kyanon Digital
arXiv:1910.13162v1  [cs.CL]  29 Oct 2019


## Page 2


2
Suong et al.
and it diﬀers from English in a number of ways. To apply the same techniques
that work for English to Vietnamese would yield inaccurate results. This has
motivated our systematic study in sentiment analysis for Vietnamese. Since our
project, Advosights, initially served a well-known electronics brand, we decided
to focus our study on electronic product reviews. Broader scopes will be studied
in future works.
Our initial approach was to build a sentiment lexicon dictionary. Its ﬁrst ver-
sion was based on some statistical methods [4,5,6] to estimate the sentiment score
for each word from a list, collected manually based on Vietnamese dictionaries.
This approach did not work well because the dataset came from casual reviews,
that were practically spoken language with a lot of slang words and acronyms.
This fact made it almost impossible to build a dictionary that cover all of those
words. We then tried to use a simple neural network to learn sentiment lexicons
from corpus automatically [12]. This also did not work well because some words
in Vietnamese have same morphology, but they have diﬀerent meanings in dif-
ferent contexts. For example, the words “d˜a” in two sentences “nh`ın d˜a qu´a”
and “d˜a qu´a c˜u” have diﬀerent meanings. But by using the dictionary, they have
the same sentiment score.
Some machine learning-based approaches have been studied. For examples,
CountVectorizer and Term Frequency–Inverse Document Frequency (Tf-idf) were
used for word representations. Support Vector Machine (SVM) and Naive Bayes
were used as classiﬁers. However, the results were not very encouraging.
We also investigated various types of recurrent neural networks (RNNs) such
as long short-term memory(LSTM) [1], Bi-Directional LSTM (biLSTM) [2] or
gated recurrent unit (GRU) [9], etc. Although some of them achieved pretty good
accuracy, the models were heavy and had very long inference time. Our ﬁnal
model is based on the Self-attention neural network architecture Transformer
[16], a well known state of the art technique in machine translation. It provided
top accuracy and has very fast inference time when running on real data.
The paper is organized as follows. In section 2, some description of self-
attention is provided for motivation. In section 3, our architecture is presented.
The experiments are described in section 4. Finally, conclusions and remarks are
included in section 5.
2
Background
Inspired by human sight mechanism, Attention was used in the ﬁeld of visual
imaging about 20 years ago [3]. In 2014, a group from Google DeepMind applied
Attentions to the RNN for image classiﬁcation tasks [7]. After that, Bahdanau
et al. [8] applied this mechanism to encoder-decoder architectures in machine
translation task. It became the ﬁrst work to apply Attention mechanism to the
ﬁeld of Natural Language Processing (NLP). Since then, Attention became more
and more common for the improvement in various NLP tasks based on neural
networks such as RNN/CNN [10,11,14,15,19].


## Page 3


Sentiment Analysis of Electronic Product Reviews in Vietnamese
3
In 2017, Vaswani et al. ﬁrst introduced Self-attention Neural Network [16].
The proposed architecture, Transformer, did not follow the well-known idea of
recurrent network. This paper paved the way and Self-attention have become a
hot topic in the ﬁeld of NLP in the last few years. In this section, we describe
their approach in detail.
2.1
Attention
The ﬁrst description of Attention Mechanism in Machine Neural Translation [8]
was well known as a process to compute weighted average context vectors for
each state of the decoder si by incorporating the relevant information from all
of the encoder states hj with the previous decoder hidden state si−1, which is
determined by a alignment weights αij between each encoder state and previous
hidden state of the decoder, to predict next state of the decoder. It can be
summarized by the following equations:
ci =
n
X
j=1
αijhj
(1)
αij =
exp(eij)
Pn
k=1 exp(ejk)
(2)
eij = a(si−1, hj), where a(si−1, hj) is a function to compute the compatibility
score between si−1 and hj.
Scaled Dot-Product Attention: Let us consider si−1 as a query vector q.
And hj now duplicated, one is key vector kj and the other is value vector vj (in
current NLP work, the key and value vector are frequently the same, there for
hj can be considered as kj or vj). The equations outlined above generally look
like:
c =
n
X
j=1
αjvj
(3)
αj =
exp(ej)
Pn
k=1 exp(ek)
(4)
In [16] paper, Vaswani et al. using the scaled dot-product function for the
compatibility score function
ej = a(q, kj) =
qkT
j
√dmodel
(5)
where dmodel is dimension of input vectors or k vector (q, k, v have the same
dimension as input embedding vector).


## Page 4


4
Suong et al.
Self-attention: Self-attention is a mechanism to apply Scaled Dot-Product At-
tention to every token of the sentence for all others. It means for each token, this
process will compute a context output that incorporates informations of itself
and information about how it relates to others tokens in the sentence.
By using a linear feed-forward layer as a transformation to create three vec-
tors (query, key, value) for every token in sentence, then apply the attention
mechanism outlined above to get the context matrix. But it seems very slow and
takes a bunch of time for whole process. So, instead of creating them individually,
we consider Q is a matrix containing all the query vectors Q = [q1, q2, ..., qn], K
contains all keys K = [k1, k2, ..., kn], and V contains all values V = [v1, v2, ..., vn].
As the result, this process can be done in parallel [16].
Attention(Q, K, V ) = softmax( QKT
√dmodel
)V
(6)
Multi-head Attention Instead of performing Self-attention a single time with
(Q, K, V ) of dimensions dmodel. Multi-head Attention performs attention h times
with (Q, K, V ) matrices of dimensions dmodel/h, each time for applying Atten-
tion, it is called a head. For each head, the (Q,K,V) matrices are uniquely pro-
jected with diﬀerent dimensions dq, dk and dv (equal to dmodel/h), then self-
attention mechanism is performed to yield an output of the same dimension
dmodel/h [16]. After all, outputs of h heads are concatenated, and apply a linear
projection layer once again. This process can be summarized by the following
equations:
MultiHead(Q, K, V ) = Concat(head1, head2, ..., headh)W O
(7)
where headi = Attention(QW Q
i , KW K
i , V W V
i )
Where the projections are parameter matrices W Q
i
∈Rdmodel×dk, W K
i
∈Rdmodel×dk,
W V
i
∈Rdmodel×dv, W O ∈Rhdv×dmodel.
2.2
Positional Information Embedding Representation
Self-attention can provide context matrix containing information about how a
token relates with the others. However, this attention mechanism still has limit,
losing positional information problem. It does not care about the order of tokens.
That means outputs of this process is invariant with the same set of tokens with
order permutations. So, to make it work, neural networks need to incorporate
positional information to the inputs. Sinusoidal Positional Encoding technique
is commonly used to solve this problem.
Sinusoidal Position Encoding: This technique was proposed by Vaswani
et al. [16]. The main point of this technique is to create Position Encoding


## Page 5


Sentiment Analysis of Electronic Product Reviews in Vietnamese
5
(PE) using sinusoidal and cosinusoidal functions to encode the position. The
PE function can be write by following equation:
PE(position, 2i) = Sin(
position
100002i/dmodel )
(8)
PE(position, 2i + 1) = Cos(
position
100002i/dmodel )
(9)
where position starts from 1 and i is ith dimension of dmodel dimensions. It means
that for each dimension of the positional encoding corresponds to a diﬀerent
sinusoids.
The advantages of this technique is it can add positional information for
sentences longer than those in training dataset.
3
Our Approach
3.1
Model architecture
We proposed a simple model using a single modiﬁed 12 heads Self-attention
block (See Fig 2), described below.
Original Sinusoidal Position Encoding [16] used “adding” operation to incor-
porate positional informations as a input. That means while performing Self-
attention, representation informations(Word Embeddings) and positional infor-
mations(Positional Embeddings) have the same weights (these two information
are equal).
z = Embedding + PE
(10)
In Vietnamese, we assumed that the positional information has more contri-
butions to create contextual semantics than representation informations. There-
fore, we used “concatenate” operation to incorporate positional informations.
That made representation informations may have a diﬀerent weights with posi-
tional informations during the transformation process.
z = Concat(Embedding, PE)
(11)
We added a block inspired by paper “Squeeze-and-Excitation Networks”, Hu
et al. [18] for the average attention mechanism and the gating mechanism by
stacking a GobalAveragePooling1D layer then forming a bottleneck with two
fully-connected layers (see Fig. 1). The ﬁrst layer is dimensionality-reduction
layer with reduction ratio r (in our experiment default is 4) with a non-linear
activation and then the second layer is dimensionality-increasing layer to return
the result to dmodel dimension also with a sigmoid activation function, which
scale the feature value into range [0, 1]. It means this layer computes how much a
feature incorporates information to contextual semantics. We call this technique
Embedding Feature Attention.


## Page 6


6
Suong et al.
y = σ(Wfc2δ(Wfc1x))
(12)
Where x is input of block. y is output of block. σ is a non-linear activation
function. δ is a non-linear activation function. Wfc1,Wfc2 are trainable matrices.
Fig. 1. Squeeze-Excitation architecure.
Fig. 2. Self-attention Neural Networks ar-
chitecture for sentiments classiﬁcation task.
4
Experiments
We implemented from scratch some layers that are needed for this work, such
as: Scaled-dot product Attention, Multihead Attention, Feed-Forward Network
and re-trained word embeddings for Vietnamese spoken language.
All experiments were deployed on 26GB RAM, CPU Intel Xeon Processor
E31220L v2, GPU Tesla K80 for 20 epochs, 64 of batch size for comparison and
all neural network models used focal-crossentropy as the training loss.


## Page 7


Sentiment Analysis of Electronic Product Reviews in Vietnamese
7
4.1
Datasets
There is no public dataset for electronics product reviews in Vietnamese. We had
to crawl user reviews from several e-commerce websites, such as Tiki, Lazada,
shopee, Sendo, Adayroi, Dienmayxanh, Thegioididong, fptshop, vatgia. Based on
our purposes, we chose some data ﬁelds to collect and store. Some data samples
are presented in Tab. 1 below.
Table 1. Examples for crawled data from e-commerce websites.
username
product name
category review
rating
user 1
Samsung
Galaxy
A8+
điện
thoại
Ytt5ya 5t55
1/5
user 2
Philips E181
điện
thoại
đang chơi liên quân tựnhiên bịđơ
đơ. rồi tựnhảy lung tung. Bịnhư
vậy là do game hay do máy v mọi
người.
1/5
user 3
Philips E181
điện
thoại
Đặt màu vàng đồng mà giao màu
bạc
2/5
user 4
Oppo f7
điện
thoại
Oppo f7 đang có chương trình trả
trước 0% và trảgóp 0% đúng không
ạ?
2/5
user 5
Philips E181
điện
thoại
Giá đó mà không có camera kép,
Vivo V9 đẹp hơn.
2/5
user 6
Samsung Note 7
điện
thoại
Cho em hỏi máy m5c của em hay bị
tắt nguồn là do sao ạ?
4/5
user 7
Nokia 230 Dual SIM điện
thoại
điện thoại vs Máy dùng tốt
4/5
user 8
Oppo f7
điện
thoại
cho em hỏi giá oppo F7 hiện tại bên
mình là bao nhiêu ạ?
5/5
user 9
Samsung Note 7
điện
thoại
Có màu đen ko vậy?
5/5
After analyzing and visualizing, we found that the dataset was very im-
balanced (see the description below) and noisy. There were some meaningless
reviews (user1 in Tab. 1). Some of them did not have sentiments (user4, user8
and user9 in Tab. 1). Sometimes, the ratings do not reﬂect the sentiment of
reviews, (see user6 in Tab. 1). Therefore, a manual inspection step was applied
to clean and label the data. We also built a tool for labeling process to made it
smoothly and faster (see Fig. 3).
- Corpus have only 2 labels (positive and negative).
- Total 32,953 documents in labeled corpus:
– Positives: 22,335 documents.
– Negatives: 10,618 documents.


## Page 8


8
Suong et al.
Fig. 3. Sentiment checking tool interface.
Next, to make the dataset balanced, we duplicated some short negative doc-
uments and segmented the longer ones. In ﬁnal result we have over 43, 500 doc-
uments in corpus with 22, 335 positives and 21, 236 negatives.
Using for training models, we splitted corpus into 3 sets as following: training
set: 27, 489, validation set: 6, 873, test set: 8, 591.
4.2
Preprocessing
For automatic preprocessing, we mainly used available researches. We applied a
sentence tokenizer[21] for each documents. All links, phone numbers and email
addresses were replaced by “urlObj”, “phonenumObj” and “mailObj”, respec-
tively. Words tokenizer from Underthesea[20] for Vietnamese was also applied.
4.3
Embeddings
We used fastText[13] model for word embeddings. In many cases, users may type
a wrong word accidentally or intentionally. fastText deals with this problem very
well by encoding at the characters level. When users type wrong or very rare
words or out-of-vocabulary words, fastText still can represent those words with
an embedding vector that most similar to word met in trained sentences. This
has made fastText become the best candidate to represent user inputs.
There had been no fastText pre-trained model for Vietnamese spoken lan-
guage. Therefore, we trained fastText model for Vietnamese vocabulary as em-
bedding pre-trained weights from a corpus over 70, 000 documents of multi-
products reviews crawled from ecomerce sites mentioned in subsection 4.1 with
no label. Rare words that occur less than 5 times in the vocabulary were re-
moved. Embedding size was 384. After training, we had 5, 534 vocabularies in
total.


## Page 9


Sentiment Analysis of Electronic Product Reviews in Vietnamese
9
4.4
Evaluation results
We used the same word embeddings as mentioned above for all models and eval-
uated all models on test set which has 8591 documents. To demonstrate the
signiﬁcance of our model, we compare our model with 6 base line RNNs mod-
els such as Long-Short Term Memory (LSTM), Gated Recurrent Units (GRU),
bidirectional LSTM, bidirectional GRU, stacked bidirectional LSTM and stacked
bidirectional GRU with the following conﬁgurations.
- Vanilla LSTM and GRU: 1 layer with 1,024 units.
- Bidirectional model of LSTM and GRU: 1 layer with 1,024 units in forward
and 1,024 units in backward.
- Stacked bidirectional model of LSTM and GRU: 2 stacked layers with 1,024
units in forward and 1,024 units in backward for each layer.
Table 2 shows that our model gave the best inference time with top accuracy
in test set. Also, in fact, this model ran in prodution have shown good prediction
than the top of baseline models, stacked Bidirectional Long-short Term Memory,
especially with complex sentences such as “giá cao như này thì t mua con ss gala
S7 cho r”, “quảng cáo lm lốvl”, “với tôi thì trong tầm giá nv vẫn có thểchấp
nhận đk” or “Nhưng vì đây là dòng điện thoại giá rẻ, nên cũng k thểkì vọng
hơn đc.” (See Fig. 4, Fig. 5)
Table 2. Inference times and macro-f1 scores
Methods
Avg.inference time (s) Macro-f1 (%)
LSTM
0.4748
48.9(23)
bi-LSTM
0.9373
90.0(05)
stacked bi-LSTM
1.7967
90.1(32)
GRU
0.3738
48.9(23)
bi-GRU
0.5863
88.9(25)
stacked bi-GRU
1.4830
89.9(72)
Self-attention
0.0124
90.1(64)
5
Conclusion
In this paper we demonstrated that using Self-attention Neural Network is faster
than previous state of the art techniques with the best result in test set and
achieved exceptionally good results when ran in prodution (Predictions make
sense to human in unlabeled data with very fast inference time).
For future work, we plan to extend stacked multi-head self-attention archi-
tectures. We are also interested in seeing the behaviour of the models explored
in this work on much larger datasets (beyond the electronics product reviews)
and more classes.


## Page 10


10
Suong et al.
Fig. 4. Stacked bidirectional Long-Short term memory for Sentiments Analysis in Viet-
namese examples
Fig. 5. Self-attention Neural Network for Sentiments Analysis in Vietnamese examples


## Page 11


Sentiment Analysis of Electronic Product Reviews in Vietnamese
11
Acknowledgment
We thank our teammates, Tran A. Sang, Cao T. Thanh, and Ha H. Huy for
helpful discussions and supports.
References
1. Sepp Hochreiter and Jurgen Schmidhuber. Long short-term memory. In Neural
Computation, 9(8):1735–1780, 1997.
2. Mike Schuster and Kuldip K Paliwal. Bidirectional recurrent neural networks. In
IEEE Transactions on Signal Processing, 45(11):2673–2681, 1997.
3. Werner
X.
Schneider.
An
Introduction
to
“Mechanisms
of
Vi-
sual
Attention:A
Cognitive
Neuroscience
Perspective.
URL:
https://pdfs.semanticscholar.org/b719/918bdf2e71571a3cbb2a6aaaec3f1b6af9e6.pdf.,
1998.
4. Andrea Esuli and Fabrizio Sebastiani. Senti-wordnet: A publicly available lexical
resource for opinion mining. In Proceedings of LREC, volume 6, pages 417–422,
2006.
5. Stefano Baccianella, Andrea Esuli, and Fabrizio Sebastiani. Sentiwordnet 3.0: An
enhanced lexical resource for sentiment analysis and opinion mining. In Proceedings
of LREC, volume 10, pages 2200–2204, 2010.
6. Saif M. Mohammad, Svetlana Kiritchenko, and Xiaodan Zhu. Nrc-canada: Building
the state-of-the-art in sentiment analysis of tweets. In Proceedings of SemEval-2013.,
2013.
7. Volodymyr Mnih et al. Recurrent Models of Visual Attention. In Neural Informa-
tion Processing Systems Conference (NIPS), 2014. arXiv preprint arXiv:1406.6247,
2014.
8. Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio. Neural Machine Translation
by Jointly Learning to Align and Translate. accepted in International Conference
on Learning Representations (ICLR), 2015. arXiv preprint arXiv:1409.0473 , 2014.
9. Junyoung Chung, Caglar Gulcehre, KyungHyun Cho, Yoshua Bengio
Empirical
Evaluation of Gated Recurrent Neural Networks on Sequence Modeling.
arXiv
preprint arXiv:1412.3555 , 2014.
10. Jianpeng Cheng, Li Dong, and Mirella Lapata. Long short-term memory-networks
for machine reading. Computing Research Repository (CoRR), 2016. arXiv preprint
arXiv:1601.06733 , 2016.
11. Jiasen Lu, Jianwei Yang, Dhruv Batra, and Devi Parikh Hierarchical question-
image co-attention for visual question answering. Advances in Neural Information
Processing Systems 29, pages 289–297, Curran Associates, Inc., 2016.
12. Duy
Tin
Vo
and
Yue
Zhang.
Don’t
Count,
Predict!
An
Au-
tomatic
Approach
to
Learning
Sentiment
Lexicons
for
Short
Text.
URL:https://www.aclweb.org/anthology/P16-2036, 2016.
13. Piotr Bojanowski, Edouard Grave, Armand Joulin, Tomas Mikolov Enriching Word
Vectors with Subword Information. arXiv preprint arXiv:1607.04606, 2016.
14. Filippos Kokkinos and Alexandros Potamianos. Structural attention neural net-
works for improved sentiment analysis. arXiv preprint arXiv:1701.01811, 2017.
15. Michal Daniluk, Tim Rocktaschel, Johannes Welbl and Sebastian Riedel. Frus-
tratingly short attention spans in neural language modeling.
arXiv preprint
arXiv:1702.04521, 2017.


## Page 12


12
Suong et al.
16. Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan
N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In I.
Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and
R. Garnett, editors, Advances in Neural Information Processing Systems 30, pages
5998–6008, Curran Associates, Inc., 2017. arXiv preprint arXiv:1706.03762, 2017.
URL:http://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf, 2017.
17. Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, and Yann N Dauphin.
Convolutional sequence to sequence learning.
arXiv preprint arXiv:1705.03122,
2017.
18. Jie Hu, Li Shen, Samuel Albanie, Gang Sun, Enhua Wu. Squeeze-and-Excitation
Networks. arXiv preprint arXiv:1709.01507, 2017.
19. Yi Zhou, Junying Zhou, Lu Liu, Jiangtao Feng, Haoyuan Peng, and Xiao-
qing Zheng.
RNN-based sequence-preserved attention for dependency pars-
ing. URL:https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/17176 ,
2018.
20. Vu Anh et al. Underthesea. ULR: https://github.com/undertheseanlp/underthesea.
21. Natural Language Toolkit. URL: https://www.nltk.org/.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1910_13162_an_efficient_model_for_sentiment_analysis_of_electronic_product_reviews_in_vietn
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1910_13162_AN_EFFICIENT_MODEL_FOR_SENTIMENT_ANALYSIS_OF_ELECTRONIC_PRODUCT_REVIEWS_IN_VIETN.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
