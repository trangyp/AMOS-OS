---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.05210v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1911.05210v3_Double_cycle-consistent_generative_adversarial_network_for_unsupervised_conditio

> Source: 1911.05210v3_Double_cycle-consistent_generative_adversarial_network_for_unsupervised_conditio.pdf

> Pages: 12

---


## Page 1


Double cycle-consistent generative adversarial network for unsupervised
conditional generation
Fei Ding, Feng Luo, Yin Yang
School of Computing, Clemson University
{feid, luofeng, yin5}@clemson.edu
Abstract
Conditional generative models have achieved consider-
able success in the past few years, but usually require a
lot of labeled data. Recently, ClusterGAN combines GAN
with an encoder to achieve remarkable clustering perfor-
mance via unsupervised conditional generation. However,
it ignores the real conditional distribution of data, which
leads to generating less diverse samples for each class
and makes the encoder only achieve sub-optimal clustering
performance. Here, we propose a new unsupervised con-
ditional generation framework, Double Cycle-Consistent
Conditional GAN (DC3-GAN), which can generate diverse
class-conditioned samples. We enforce the encoder and the
generator of GAN to form an encoder-generator pair in ad-
dition to the generator-encoder pair, which enables us to
avoid the low-diversity generation and the triviality of la-
tent features. We train the encoder-generator pair using
real data, which can indirectly estimate the real conditional
distribution. Meanwhile, this framework enforces the out-
puts of the encoder to match the inputs of GAN and the prior
noise distribution, which disentangles latent space into two
parts: one-hot discrete and continuous latent variables.
The former can be directly expressed as clusters and the
latter represents remaining unspeciﬁed factors. This work
demonstrates that enhancing the diversity of unsupervised
conditional generated samples can improve the clustering
performance. Experiments on different benchmark datasets
show that the proposed method outperforms existing gen-
erative model-based clustering methods, and also achieves
the optimal disentanglement performance.
1. Introduction
Generative Adversarial Networks(GANs) have achieved
remarkable success in realistic image generation such as
class-conditioned generation [22, 21], but at the cost of col-
lecting massive amounts of annotated images. Given a large
number of unlabeled images available online, how to lever-
age them for conditional generation remains a challenging
problem. As an important unsupervised learning method,
clustering has been widely used in many computer vision
applications, such as image segmentation [8], visual fea-
tures learning [4], and 3D object recognition [46]. There-
fore, it’s natural to combine clustering and generative mod-
els for an unsupervised conditional generation.
When processing high-semantic and high-dimensional
images, most clustering methods such as DEC [51],
DCN [52], and ClusterGAN [37], have been proposed to
learn the ‘clustering-friendly’ latent representations, then
perform clustering algorithms, such as K-means [31] on
the latent space. Since there are multiple optimization ob-
jectives, such as adversarial training for generation, low-
dimensional representation learning, and distance-based
clustering algorithms for class assignments, it’s optimal to
effectively integrate them to achieve unsupervised condi-
tional generation in an end-to-end manner. Recently, the
ClusterGAN [37] provides a new clustering mechanism
based on the GAN and the inverse-mapping network. How-
ever, it only focuses on learning non-smooth latent space for
clustering, and ignores the estimation of the real conditional
distribution, leading to sub-optimal conditional generation.
In this paper, we introduce a novel unsupervised con-
ditional generative model called Double Cycle-Consistent
Conditional GAN (DC3-GAN). It can generate diverse sam-
ples for each class without labels, and then directly ob-
tains clusters without additional clustering methods. This
framework can accommodate conditional generation and
clustering in a uniﬁed and end-to-end manner. Moreover,
we introduce a solution for directly obtaining class assign-
ment by disentangling the latent space into two parts: the
one-hot discrete latent variables directly related to cate-
gorical cluster information, and the continuous latent vari-
ables related to other factors of variations. The disentangle-
ment of latent space is performing the clustering operation.
Unlike the existing distance-based clustering methods, our
method does not need any explicit clustering objectives or
distance/similarity calculations in the latent space.
The conditional generation usually requires labels to es-
arXiv:1911.05210v3  [cs.LG]  5 Apr 2021


## Page 2


timate the real conditional distribution. But this work fo-
cuses on the unsupervised conditional generation, hence we
propose to indirectly estimate the real conditional distri-
bution via two cycle-consistencies: the generator-encoder
pair and the encoder-generator pair. We ﬁrst construct the
generator-encoder pair with the generator of GAN and the
encoder, which involves the mapping from latent space to
data space, and back to latent space, to separate the la-
tent space into one-hot discrete variables and continuous
variables of other factors. Then, we utilize a weight shar-
ing strategy to form a deterministic encoder-generator pair
under the maximum mean discrepancy (MMD) regulariza-
tion [14]. Our method can be considered as the integra-
tion of the GAN and deterministic Autoencoder to achieve
the unsupervised conditional generation. A better generator
helps to guide the encoder for training, and a better encoder
in turn helps to generate better class-conditioned samples.
Therefore, we apply clustering as a proxy task to evalu-
ate the estimation of the real conditional distribution. This
framework includes three different types of regularizations:
an adversarial density-ratio loss in data space, MMD loss
in the continuous latent code, and cross-entropy loss in dis-
crete latent code. The source code and models are publicly
available at this link 1.
In summary, our contributions are as follows:
(1) We propose a new unsupervised conditional GAN
framework called DC3-GAN, which can achieve effective
conditional generation without labels, and directly obtain
cluster assignments without clustering methods.
(2) We combine the encoder-generator pair with the
generator-encoder pair to form two cycle-consistencies,
which help avoid the triviality on continuous latent variable
and enables estimation of the real conditional distribution.
(3) We evaluate the conditional generation quality of
DC3-GAN, and apply it to different benchmark datasets for
disentanglement and clustering. The experiments demon-
strate that it can achieve desirable disentanglement and clus-
tering performance in most cases.
2. Method
Given a collection i.i.d. samples x = {xi}N
i=1 (e.g., im-
ages) drawn from an unknown data distribution Px, where
xi is the i-th data sample and N is the size of the dataset,
the standard GAN [13, 15] consists of two components: the
generator Gθ and the discriminator Dψ. Gθ deﬁnes a map-
ping from the latent space Z to the data space X and Dψ
can be considered as a mapping from the data space X to
the probability of one sample being real or not. To achieve
unsupervised conditional generation, we need to introduce
an inference network Eφ to obtain the latent variables given
the data sample.
1after the paper is accepted
In this section, we ﬁrst conduct a comprehensive anal-
ysis of ClusterGAN [37], and observe that there is a key
loss item missing in the objective. To address this issue,
we introduce an MMD-based regularization to enforce the
inference network and the generator of standard GAN to
form a deterministic Autoencoder. Meanwhile, the method
enables us to disentangle the latent space z into the one-hot
discrete latent variables zc, and the continuous latent vari-
ables zn in an unsupervised manner. zc naturally represents
the categorical cluster information; zn is expected to con-
tain information of other variations.
2.1. Unsupervised conditional generation
ClusterGAN [37] provides a new clustering method us-
ing GANs, which utilizes a joint distribution of discrete and
continuous latent variables as the prior of GANs. Although
it focuses on projecting the data to the latent space for clus-
tering, it can be generalized to an unsupervised conditional
generation framework. And the optimization is based on the
combination of original GAN loss, cycle-consistency loss,
and cross-entropy loss.
min
G,E max
D LClus(G, D, E) =
Ex∼Px[q(Dψ(x))] + Ezc∼Pc,zn∼Pn[q(1 −Dψ(Gθ(zc, zn)))]
|
{z
}
1⃝
−λn Ezc∼Pc,zn∼Pn[c(Eφ(Gθ(zc, zn))n, zn)]
|
{z
}
2⃝
−λc Ezc∼Pc,zn∼Pn[c(Eφ(Gθ(zc, zn))c, zc)]
|
{z
}
3⃝
,
(1)
where Px is the real data distribution, Pc is the prior dis-
tribution of zc, and Pn is the prior distribution of zn. c(·, ·)
is any measurable cost function, λn and λc are hyperparam-
eters balancing these losses. For the original GAN [13], the
function q is chosen as q(t) = log t, and the Wasserstein
GAN [15] applies q(t) = t. This adversarial density-ratio
estimation [45] enforces Qx to match Px, as shown in term
1⃝, LGAN. The term 2⃝and 3⃝are two constraints to the
generator Gθ and the encoder Eφ, which correspond to the
cycle-consistency of zn and the cross-entropy loss on zc.
To analyze this clearly, the term 2⃝can be written as:
Ln(G, E) = −E(x,zn)∼Qxc[c(Eφ(x)n, zn)]
= Ezc∼Pc,zn∼Pn[||Eφ(Gθ(zc, zn)) −zn||].
(2)
Thus, this loss term attempts to keep the cycle-consistency
of zn during optimization. After adding the recovery of zn,
the information from zn can be utilized for generation to a
certain extent. However, since the dimension of x is much
larger than the dimensions of zc and zn, this constraint may


## Page 3


cz
nz
g
x
CE
L
n
L
Real/Fake
GAN
L
rx
! rx
AE
L
G
E
G
E
D
r
nz
MMD
L
nz!
cz!
r
cz
Figure 1. The architecture of DC3-GAN (G: generator, E: encoder,
D: discriminator). The latent representations are separated into
one-hot discrete latent variables zc and other factors of variation
zn. The zc and zn are concatenated and fed into the Gθ for gen-
eration and the Eφ maps the samples (xg and xr) back into latent
space. The Dψ is adopted for the adversarial training in the data
space. Note that all generators share the same parameters and all
encoders share the same parameters.
become trivial for the generator-encoder (G-E) pair, and re-
sult in the generation of low-diversity samples.
The term 3⃝is the cross-entropy loss on zc:
LCE(G, E) = −E(x,zc)∼Qxc[log(QE(zc|x))],
(3)
where QE(zc|x) is used to denote the conditional distribu-
tion induced by Eφ. Qzc|x is the conditional distribution
speciﬁed by the generator G. Therefore, minimizing loss
term LCE(G, E) is equivalent to minimizing the KL diver-
gence between Qzc|x and QE
zc|x. However, ClusterGAN
ignores the real data conditional distributions Pzc|x in the
objective, which usually requires real category information
to estimate. Even when the marginal distributions Px and
Qx match perfectly through the term 1⃝, ClusterGAN still
can not guarantee that two conditional distributions Pzc|x
and QE
zc|x are well matched. Only minimizing LCE(G, E)
makes G tend to generate data that are far from the decision
boundaries of Eφ. In other words, the generated images for
each category may be easily distinguishable by Eφ, but have
low intra-class diversity. It is thus essential to incorporate
Pzc|x in the objective function.
2.2. The encoder-generator pair
Our above analysis of ClusterGAN reveals that simply
adding an encoder cannot effectively achieve conditional
generation, which has two main problems: trivial contin-
uous latent variables recovery and missing real conditional
distribution term, Pzc|x. Therefore, we present to enforce
E and G to form an Autoencoder (E-G pair) by introducing
a distance-based regularizer. The real conditional distribu-
tion Pzc|x can also be estimated properly in an unsupervised
manner. We deﬁne the following objective:
min
G,E LE-G(G, E) =
EQφ(zn,zc|x) [log Pθ(x|zn, zc)] + λ · Dz (Qz, Pz) ,
(4)
where λ > 0 is a hyperparameter, Dz is an arbitrary di-
vergence between Qz and Pz, which encourages the en-
coded distribution Qz to match the prior Pz.
Because
the latent variables z = (zc, zn), and the prior distribu-
tion Pz(zc, zn) = Pc(zc)Pn(zn), these constraints can be
added by simply penalizing the discrete variables part and
the continuous variables part separately.
The constraint of continuous variables zn can be con-
sidered to apply similar regularizations in the generative
Autoencoder model like AAE [32] and WAE [44].
The
former uses the GAN-based density-ratio trick to estimate
the KL-divergence of distributions [45], and the latter min-
imizes the distance between distributions based on Max-
imum Mean Discrepancy (MMD) [14, 27].
We choose
adversarial density-ratio estimation for modeling the data
space because it can handle complex distributions. MMD-
based regularizer is stable for optimization and works well
with multivariate normal distributions [45]. Therefore, we
choose MMD to quantify the distance between the prior dis-
tribution Pn(zn) and the posterior distribution Qn(zn|x).
Compared with WAE, we only penalize the continuous la-
tent variables zn, not the whole latent variable. The regu-
larizer Dz based on MMD is expressed as:
LMMD(E) =
1
N(N −1)
X
ℓ̸=j
k
 zℓ
n, zj
n

+
1
N(N −1)
X
ℓ̸=j
k
 ˆzℓ
n, ˆzj
n

−2
N 2
X
ℓ,j
k
 zℓ
n, ˆzj
n

,
(5)
where k(·, ·) can be any positive deﬁnite kernel,
{z1
n, . . . , zN
n } are sampled from the prior distribution
Pn(zn), ˆzi
n is sampled from the posterior distribution
Qn(zn|x) and xi is sampled from the real data samples for
i = 1, 2, . . . , N.
The constraint of zc can’t be applied explicitly without
labels. Instead, we use a mean absolute error (MAE) crite-
rion to estimate the encoding distribution Qφ(z|x) and the
decoding distribution Pθ(x|z), which are taken to be deter-
ministic and can be replaced by Eφ and Gθ, respectively.
LAE(E, G) = Ex∼Px[|x −Gθ(Eφ(x))|].
(6)
2.3. The generator-encoder pair
In addition to the encoder-generator pair, it also neces-
sary to emphasize the generator-encoder pair for the dis-
entanglement between discrete and continuous latent vari-
ables, as shown in Figure 1. Most of the existing meth-
ods [17, 56, 41] leverage labels to achieve the disentangle-
ment of various factors. This work attempts to encourage


## Page 4


independence between Qn(zn|x) and Qc(zc|x) as much as
possible without labels.
We sample the latent variables z = (zc, zn) from the
discrete-continuous prior, through the generator-encoder
pair, it should output the identical discrete and continuous
latent variables (ˆzc, ˆzn). It enforces the generator to take
advantage of extra information from zc. Besides, the re-
covery of latent variables ensure that outputs of the encoder
Eφ are conditionally independent. When Eφ maps the real
data sample x to latent representations zr
c and zr
n, which
are expected to be conditionally independent. The cross-
entropy loss (Eq. 3) between zc and ˆzc can ensure that the
latent variables ˆzc only contain class-related information.
Besides, to ensure that the latent variables ˆzc or ˆzr
c don’t
contain any class-related information, it is necessary to ap-
ply additional regularizers to penalize ˆzn and ˆzr
n, which are
related to the loss Ln and LMMD.
2.4. Objective of DC3-GAN
The objective function of our approach is integrated into
the following form:
L = LGAN + LAE + β1LMMD + β2Ln + β3LCE.
(7)
where the regularization coefﬁcients β1 to β3 ≥0, bal-
ancing the weights of different loss terms. Each term of
Eq. 7 plays a different role for three components: gener-
ator Gθ, discriminator Dψ, and encoder Eφ. Both LGAN
and LAE are related to Gθ and Eφ, which constrain the
whole latent variables. The LGAN term is also related to
Dψ, which focuses on distinguishing the true data samples
from the fake samples generated by Gθ. LMMD and Ln
are related to continuous latent variables, and LCE and Lc
are related to discrete latent variables. All these loss terms
are used to ensure that our algorithm disentangles the latent
space generated from encoder into cluster information and
remaining unspeciﬁed factors. The training procedure of
DC3-GAN applies jointly updating the parameters of Gθ,
Dψ and Eφ, as described in Appendix. We empirically set
β1 = β2 to enable a reasonable adjustment of the relative
importance of continuous and discrete parts.
3. Experiments
In this section, we perform a variety of experiments to
evaluate the effectiveness of our proposed method, includ-
ing clusters assignment via zc and visualization studies of
zn. We also conduct ablation experiments to understand the
contribution of various loss terms.
Data sets. The clustering experiments are carried out
on seven datasets:
MNIST [25], Fashion-MNIST [50],
YouTube-Face (YTF) [49], Pendigits [1], 10x 73k [55],
COIL-100 [38], and CIFAR-10 [24]. The disentanglement
evaluation is conducted on dsprites [35]. Both of the ﬁrst
two datasets contain 70k images with 10 categories, and
each sample is a 28 × 28 grayscale image. YTF contains
10k face images of size 55×55, belonging to 41 categories.
The Pendigits dataset contains a time series of (x, y) coor-
dinates of hand-written digits. It has 10 categories and con-
tains 10992 samples, and each sample is represented as a
16-dimensional vector. The 10x 73k dataset contains 73233
data samples of single-cell RNA-seq counts of 8 cell types,
and the dimension of each sample is 720. The multi-view
object image dataset COIL-100 has 100 clusters and con-
tains 7200 images of size 128 × 128.
Implementation Details. We implement different neu-
ral network structures for Gθ, Dψ, and Eφ to handle dif-
ferent types of data. We provide details of models in the
Appendix.
For the prior distribution of our method, we
randomly generate the discrete latent code zc, which is
equal to one of the elementary one-hot encoded vectors
in RK, then we sample the continuous latent code from
zn ∼N(0, σ2Idn), here σ = 0.10. The sampled latent
code z = (zc, zn) is used as the input of Gθ to generate
samples. The dimensions of zc and zn are shown in Ta-
ble 9. We implement the MMD loss with RBF kernel [44]
to penalize the posterior distribution Qφ(zn|x). The im-
proved GAN variant with a gradient penalty [15] is used
in all experiments. To obtain the cluster assignment, we
directly use the argmax over all softmax probabilities for
different clusters. The following regularization parameters
work well during all experiments: λ = 10, β1 = β2 = 0.1,
β3 = 10. We implement the models using the TensorFlow
library and train them on one NVIDIA DGX-1 station.
3.1. Evaluation of generation quality
Table 1. Comparison of FID score to reveal the quality of gener-
ated samples from GAN methods (Lower is better).
Method
Ours
ClusterGAN
WGAN
InfoGAN
MNIST
0.15
0.81
0.88
1.88
Fashion
0.67
0.91
0.95
11.04
To demonstrate the quality and diversity of generated
samples from DC3-GAN, we ﬁrst calculate the Frechet
Inception Distance (FID) [19] score of generated sam-
ples, as shown in Table 1.
The FID scores on MINST
and Fashion are signiﬁcantly lower than those of Cluster-
GAN. Our method shows that the estimation of real con-
ditional distribution can improve the quality of generated
samples. Then we randomly sample 200 pairs of gener-
ated images from one category to calculate structural sim-
ilarity (SSIM) [48, 47] for diversity evaluation on MNIST
data. This evaluation method for diversity has also been
used in AC-GAN [40]. The SSIM scores range between 0.0
and 1.0, and lower mean scores indicate that samples from
the same class are less similar. As shown in Table 2, our


## Page 5


Table 2. Comparison of mean SSIM scores of 200 pairs to reveal the diversity of generated samples from GAN methods (Lower is better).
Class
0
1
2
3
4
5
6
7
8
9
ClusterGAN
0.362
0.599
0.263
0.314
0.315
0.282
0.351
0.388
0.340
0.427
Ours
0.343
0.576
0.231
0.316
0.312
0.259
0.322
0.392
0.336
0.377
Figure 2. Samples generated on ﬁxed discrete latent codes from
the models trained on MNIST.
method achieves lower SSIM scores on most classes, which
demonstrates that it can enhance the diversity of generation.
The diversity of generated images indicates that there exist
different latent variables for generative factors, except the
cluster information. To further understand these generative
factors, we change the value of one single dimension from
[−0.5, 0.5] in zn while ﬁxing other dimensions and the dis-
crete latent variables zc. As shown in Figure 2, the value
changing leads to semantic changes in generated samples.
The changed dimensions represent the tilt, style, and width
factors of digits, which shows the potential to disentangle
the latent space.
3.2. Evaluation of disentanglement
We further explore the disentanglement capability
of DC3-GANon dSprites dataset. We follow the same ex-
perimental settings and hyperparameters tuning as Factor-
VAE [23], InfoGAN [7] and InfoGAN-CR [28] for fair
comparisons. We provide the experimental details in Ap-
pendix, and focus on explaining the results in this section.
As shown in Table 3, our method also achieves excellent
disentanglement performance. Compared with InfoGAN-
CR, we implement the proposed double-cycle consistency
to replace the contrastive regularizer (CR) based on the In-
foGAN architecture, which has two latent variables. These
consistencies force the generator to generate different sam-
ples while ﬁxing one latent variable and changing another
latent variable. This is beneﬁcial for disentanglement, as
it simulates the latent traversal experiments and encourages
distinct changes in generated samples. In addition, Mod-
elCentrality is proposed by [28] for unsupervised model
selection to evaluate the trained models on an unlabelled
dataset. It’s naturally suitable for our unsupervised condi-
tional generation settings.
3.3. Evaluation of clustering algorithm
We argue that the clustering task can be considered as
a proxy to evaluate the real conditional distribution es-
timation.
To evaluate clustering results, we report two
standard evaluation metrics: Clustering Purity (ACC) and
Normalized Mutual Information (NMI). We compare DC3-
GAN with four clustering baselines: K-means [31], Non-
negative Matrix Factorization (NMF) [26]. We also com-
pare our method with the state-of-the-art clustering ap-
proaches based on GAN and Autoencoder, respectively.
For GAN-based approaches, ClusterGAN [37] is chosen as
it achieves the superior clustering performance compared
to other GAN models (e.g., InfoGAN). For Autoencoder-
based methods such as DEC [51], DCN [52] and DE-
PICT [10], Dual Autoencoder Network (DualAE) [54] are
used for comparison. In addition, the deep spectral clus-
tering (SpectralNet) [43] and joint unsupervised learning
(JULE) [53] are also included in the comparison.
Table 4 reports the best clustering metrics of different
models from 5 runs. Our method achieves signiﬁcant per-
formance improvement on Fashion-10, YTF, Pendigits, and
10x 73k datasets than other methods. Particularly, while
all other methods perform worse than K-means on the 16-
dimensional Pendigit dataset, our method signiﬁcantly out-
performs K-means in both ACC (0.847 vs. 0.793) and NMI
(0.803 vs. 0.730). DC3-GAN achieves the best ACC re-
sult on YTF dataset while maintaining comparable NMI
value. For MNIST dataset, DC3-GAN achieves close to the
best performance on both ACC and NMI metrics. To fur-
ther evaluate the performance of DC3-GAN on large num-
bers of clusters, we compare our clustering method with K-
means on Coil-100 dataset using three standard evaluation
metrics: ACC, NMI, and Adjusted Rand Index (ARI). As
shown in Table 5, DC3-GAN achieves better performance


## Page 6


Table 3. Comparison results based on different disentanglement metrics on the dSprites dataset.The score 1.0 denotes a perfect disen-
tanglement. All the baseline results are from [28]. The proposed DC3-GAN achieves desirable scores in most cases. The implemen-
tation of DC3-GAN is based on the source code of InfoGAN-CR, and MC (ModelCentrality) denotes an unsupervised model selection
scheme [28].
Model
FactorVAE
DCI
SAP
Explicitness
Modularity
MIG
BetaVAE
VAE
0.63 ± 0.06
0.30 ± 0.10
-
-
-
0.10
-
β-TCVAE
0.62 ± 0.07
0.29 ± 0.10
-
-
-
0.45
-
HFVAE
0.63 ± 0.08
0.39 ± 0.16
-
-
-
-
-
β-VAE
0.63 ± 0.10
0.41 ± 0.11
0.55
-
-
0.21
-
FactorVAE
0.82
-
-
-
-
0.15
-
FactorVAE (1.0)
0.79 ± 0.01
0.67 ± 0.03
0.47 ± 0.03
0.78 ± 0.01
0.79 ± 0.01
0.27 ± 0.03
0.79 ± 0.02
FactorVAE (10.0)
0.83 ± 0.01
0.70 ± 0.02
0.57 ± 0.0
0.79 ± 0.0
0.79 ± 0.0
0.40 ± 0.01
0.83 ± 0.0
FactorVAE (40.0)
0.82 ± 0.01
0.74 ± 0.01
0.56 ± 0.0
0.79 ± 0.0
0.77 ± 0.01
0.43 ± 0.01
0.84 ± 0.01
FactorVAE + MC
0.84 ± 0.0
0.73 ± 0.01
0.58 ± 0.0
0.80 ± 0.0
0.82 ± 0.0
0.37 ± 0.0
0.86 ± 0.0
IB-GAN
0.80 ± 0.07
0.67 ± 0.07
-
-
-
-
-
InfoGAN
0.82 ± 0.01
0.60 ± 0.02
0.41 ± 0.02
0.82 ± 0.0
0.94 ± 0.01
0.22 ± 0.01
0.87 ± 0.01
InfoGAN-CR + MC
0.92 ± 0.0
0.77 ± 0.0
0.65 ± 0.0
0.87 ± 0.0
0.99 ± 0.0
0.45 ± 0.0
0.99 ± 0.0
Ours + MC
0.936 ± 0.0
0.790 ± 0.0
0.634 ± 0.0
0.862 ± 0.0
0.985 ± 0.0
0.378 ± 0.0
0.998 ± 0.0
Table 4. Comparison of clustering algorithms on ﬁve benchmark datasets.
The results marked by (*) are from existing
sklearn.cluster.KMeans package. The dash marks (-) mean that the source code is not available or that running released code is not
practical, all other results are from [37] and [54]. SpecNet and ClusGAN mean SpectralNet and ClusterGAN.
Method
MNIST
Fashion-10
YTF
Pendigits
10x 73k
ACC
NMI
ACC
NMI
ACC
NMI
ACC
NMI
ACC
NMI
K-means
0.532
0.500
0.474
0.512
0.601
0.776
0.793∗
0.730∗
0.623∗
0.577∗
NMF
0.560
0.450
0.500
0.510
-
-
0.670
0.580
0.710
0.690
DEC
0.863
0.834
0.518
0.546
0.371
0.446
-
-
-
-
DCN
0.830
0.810
-
-
-
-
0.720
0.690
-
-
JULE
0.964
0.913
0.563
0.608
0.684
0.848
-
-
-
-
DEPICT
0.965
0.917
0.392
0.392
0.621
0.802
-
-
-
-
SpecNet
0.800
0.814
-
-
0.685
0.798
-
-
-
-
InfoGAN
0.890
0.860
0.610
0.590
-
-
0.720
0.730
0.620
0.580
ClusGAN
0.950
0.890
0.630
0.640
-
-
0.770
0.730
0.810
0.730
DualAE
0.978
0.941
0.662
0.645
0.691
0.857
-
-
-
-
Ours
0.976
0.941
0.693
0.669
0.721
0.790
0.847
0.803
0.905
0.820
on all three metrics.
3.4. Evaluation on more images
We also use the t-SNE [30] algorithm to visualize zn
of MNIST datasets and compare them to ClusterGAN and
the original data. As shown in Figure 3, we can observe
different categories in the original data. In ClusterGAN,
there are still several distinguishable clusters. In contrast,
our method can make these points more cluttered in latent
space, which doesn’t contain obvious category information
in the zn. Therefore, our method demonstrates another ex-
cellent capability: all these informative continuous factors
are independent of cluster information.
We ﬁrst evaluate the scalability of DC3-GAN to large
numbers of clusters on the COIL-100 dataset(100 clus-
ters).
Here, we compare our clustering method with K-
means on three standard evaluation metrics: ACC, NMI and
Table 5. The clustering results on the Coil-100 dataset, which has
a large number of clusters (K=100).
Method
ACC
NMI
ARI
K-means
0.668
0.836
0.574
ClusterGAN
0.615
0.797
0.487
Our method
0.822
0.911
0.764
Adjusted Rand Index (ARI). As shown in Table 5, DC3-
GAN
achieves better performance on all three metrics.
DC3-GAN even gains an increase of 0.154 on ACC metric.
We also perform image generation task on Coil-100 dataset,
to further verify the generative performance, which involves
mapping latent variables to the data space. Figure 4 shows
the generated samples by ﬁxing one-hot discrete latent vari-
ables, which are diverse and realistic. The continuous latent
variables represent meaningful factors such as the pose, lo-
cation and orientation information of objects. Therefore,


## Page 7


(a)
(b)
(c)
Figure 3. The t-SNE visualization of raw data (a), zn of ClusterGAN (b) and DC3-GAN (c) on MNIST dataset. The bulk of samples in the
right part of a(3) is a small group of “1” images. The reason that they are not well mixed may be due to their low complexity.
Figure 4. The samples generated on ﬁxed discrete latent variables
from the models trained on Coil-100 dataset. Each column corre-
sponds to a speciﬁc cluster.
the disentanglement of latent space not only provides the su-
perior clustering performance, but also retains the remark-
able ability of diverse and high-quality image generation.
Besides, we further evaluate the proposed method on
more complex dataset: CIFAR-10.
The implementation
is based on Google compare-gan framework 2. The spec-
tral normalization is used on both generator and discrim-
inator. We use the same class-conditional BatchNorm in
the generator as Lucic et al. [29], to incorporate the cate-
gory information from zn. For the encoder, we use the pre-
trained SimCLR [6] model to improving training efﬁciency,
and apply 2-layer MLP as project head to map the learned
representations to zn and zc.
The self-supervised Sim-
CLR model is pre-trained by following the ofﬁcial imple-
mentation 3. Table 6 shows that DC3-GAN achieves close
to the best clustering performance on ACC. Because our
2https://github.com/google/compare_gan
3https://github.com/google-research/simclr
method learns cluster memberships from conditional gener-
ation without labels, it’s also necessary to evaluate the gen-
eration results of images. As shown in Table 7, our method
also maintains the quality of image generation, which en-
ables to achieve the superior clustering results.
Table 6. CIFAR-10 images clustering results. All baseline results
are from [20]. The value marked by (*) is the best (mean) results
in [20], and they also report that avg. ± STD is 0.576 ± 0.050.
Method
ACC
NMI
K-means
0.229
0.087
DCGAN (2015) [42]
0.315
0.265
JULE (2016) [53]
0.272
0.192
DEC (2016) [51]
0.301
0.257
DAC (2017) [5]
0.522
0.396
DeepCluster (2018) [4]
0.374
-
ADC (2018) [18]
0.325
-
IIC (2019) [20]
0.617 (0.576)∗
0.513
GATCluster(2020) [39]
0.610
0.475
Ours
0.605
0.484
3.5. Ablative Analysis
We perform the ablative analysis of our losses (Table 8).
The LAE and LMMD are critical in our model.
The in-
ference network and the generator form a deterministic
encoder-decoder pair. To minimize the reconstruction loss
LAE, the generator Gθ needs to learn to generate realistic
and diverse data samples. It also indirectly forces the zr
c
Table 7. FID results on the CIFAR-10 dataset (smaller is better).
The results marked by (*) are from [33].
Method
FID Score
DCGANs [42]
29.7∗
WGAN-GP (2017) [15]
29.3
SN-SMMDGAN (2018) [2]
25.0
MSGAN (2019) [33]
28.7∗
Ours
28.5 ± 0.02


## Page 8


Table 8. Ablations on MNIST dataset. Each row shows the re-
moval of a loss term. The full setting includes all loss terms.
Ablative analysis
ACC
NMI
No LCE
0.899
0.863
No Ln
0.868
0.0.851
No LMMD
0.812
0.829
No LAE
0.672
0.488
Full setting
0.976
0.941
to contain only the category information. LMMD enforces
the posterior distribution Qφ(zn|x) to be close to the prior
distribution P(zn). The clustering performance gain is also
from the loss terms LCE and Ln.
4. Related works
Latent space clustering. A general method to avoid the
curse of dimensionality in clustering is mapping data sam-
ples to in a low-dimensional latent space and performing
clustering on latent space. Most existing latent space clus-
tering methods are based on Autoencoder [51, 9, 16, 52, 54],
which enables reconstructing data samples from the low-
dimensional representation. The training objectives usually
are coupled with reconstruction loss to avoid random dis-
criminative representations. However, it forces latent repre-
sentations to capture all key factors of variations and simi-
larities related to reconstruction, not class decision bound-
aries. Alternatively, recent contrastive learning utilizes in-
stance discrimination to achieve remarkable self-supervised
representation learning [6]. But it still has potential limita-
tions that instance-level pseudo labels are from hand-crafted
augmentations and cannot explicitly determine the under-
lying class boundaries. Such strategies may beneﬁt from
the good parameter initialization, but there is still a lack of
stable supervision signals to directly improve class assign-
ments. Furthermore, these latent space clustering methods
still depend on additional distance-based clustering algo-
rithms (e.g., K-means) to obtain the cluster assignments. In
contrast, our method accommodates the conditional gener-
ation and cluster assignments in an end-to-end manner.
Generative models. Learning disentangled representa-
tion can reveal the factors of variation in the data [3], and
provides interpretable semantic latent codes for generative
models. Generally, existing models can be mainly catego-
rized into VAE-based and GAN-based types. The VAE-
based methods involves extracting the label relevant and
irrelevant representations [34, 17, 56, 41]. For example,
Mathieu et al. [34] introduce a conditional VAE with ad-
versarial training to disentangle the latent representations
into label relevant and the remaining unspeciﬁed factors. Y-
AE [41] focuses on the standard Autoencoder to achieve
the disentanglement of implicit and explicit representations.
Meanwhile, two-step disentanglement methods based on
Autoencoder [17] or VAE [56] are also proposed. How-
ever, all of these methods need to leverage (partial) label
information. Besides, VAE usually can not achieve high-
quality generation in real-world scenarios
[11].
There-
fore, several studies begin to capture discrete and contin-
uous factors of variation based on GAN. InfoGAN [7] re-
veals the disentanglement of latent code by maximizing the
mutual information between the latent code and the gener-
ated data, but it is not speciﬁcally designed for clustering.
ClusterGAN [37] integrated GAN with an encoder network
for clustering by creating a non-smooth latent space. How-
ever, it ignores the real conditional distribution, which leads
to generate trivial latent features and less diverse samples.
Unlike conventional conditional GANs [36], our proposed
method integrates the Autoencoder and GAN by construct-
ing two cycle-consistencies, and separates the latent vari-
ables into two parts without any labels.
5. Conclusion
In this work, we present DC3-GAN, a new conditional
generation framework that can generate diverse samples
without labels and directly obtain the cluster assignments
without clustering methods.
Unlike most existing latent
space clustering algorithms, our method does not build
‘clustering-friendly’ latent space explicitly and does not
need extra clustering operation.
Therefore, our method
avoids the difﬁculty of integrating latent feature construc-
tion and clustering. Furthermore, our method does not dis-
entangle class relevant features from class non-relevant fea-
tures. The disentanglement in our method is targeted to ex-
tract “cluster information” from data. Although our method
does not depend on any explicit distance calculation in the
latent space, the distance between data may be implicitly
deﬁned by the neural networks.
The two cycle-consistencies (x →(zc, zn) →x, (zc,
zn) →x →(zc, zn) ) in DC3-GAN can help avoid the
triviality of zn, and then avoid the generation of low diver-
sity images in some degree. We have used the real images
to train the encoder-generation pair (x →(zc, zn) →x),
which can help the encoder to estimate the real conditional
distribution. However, due to the unsupervised fashion of
clustering, the conditional distribution Q(zc|x) speciﬁed by
the generator of GAN may not match well with the true
conditional distribution P(zc|x) in real data, which is the
case in both ClusterGAN and our DC3-GAN. This may
be another reason for the low diversity conditional gener-
ation [12]. Improving GAN to create more diverse images
is an important task for future work.
References
[1] Fevzi Alimoglu and Ethem Alpaydin. Methods of combin-
ing multiple classiﬁers based on different representations for


## Page 9


pen-based handwritten digit recognition. In Proceedings of
the Fifth Turkish Artiﬁcial Intelligence and Artiﬁcial Neural
Networks Symposium (TAINN 96). Citeseer, 1996.
[2] Michael Arbel, Dougal Sutherland, Mikołaj Bi´nkowski, and
Arthur Gretton. On gradient regularizers for mmd gans. In
Advances in Neural Information Processing Systems, pages
6700–6710, 2018.
[3] Yoshua Bengio, Aaron Courville, and Pascal Vincent. Rep-
resentation learning: A review and new perspectives. IEEE
transactions on pattern analysis and machine intelligence,
35(8):1798–1828, 2013.
[4] Mathilde Caron, Piotr Bojanowski, Armand Joulin, and
Matthijs Douze. Deep clustering for unsupervised learning
of visual features. In Proceedings of the European Confer-
ence on Computer Vision (ECCV), pages 132–149, 2018.
[5] Jianlong Chang, Lingfeng Wang, Gaofeng Meng, Shiming
Xiang, and Chunhong Pan.
Deep adaptive image cluster-
ing. In Proceedings of the IEEE International Conference
on Computer Vision, pages 5879–5887, 2017.
[6] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Ge-
offrey Hinton. A simple framework for contrastive learning
of visual representations. arXiv preprint arXiv:2002.05709,
2020.
[7] Xi Chen, Yan Duan, Rein Houthooft, John Schulman, Ilya
Sutskever, and Pieter Abbeel. Infogan: Interpretable repre-
sentation learning by information maximizing generative ad-
versarial nets. In Advances in neural information processing
systems, pages 2172–2180, 2016.
[8] Keh-Shih Chuang, Hong-Long Tzeng, Sharon Chen, Jay Wu,
and Tzong-Jer Chen. Fuzzy c-means clustering with spatial
information for image segmentation. computerized medical
imaging and graphics, 30(1):9–15, 2006.
[9] Nat Dilokthanakul, Pedro AM Mediano, Marta Garnelo,
Matthew CH Lee, Hugh Salimbeni, Kai Arulkumaran, and
Murray Shanahan.
Deep unsupervised clustering with
gaussian mixture variational autoencoders. arXiv preprint
arXiv:1611.02648, 2016.
[10] Kamran Ghasedi Dizaji, Amirhossein Herandi, Cheng Deng,
Weidong Cai, and Heng Huang. Deep clustering via joint
convolutional autoencoder embedding and relative entropy
minimization.
In Proceedings of the IEEE International
Conference on Computer Vision, pages 5736–5745, 2017.
[11] Partha Ghosh, Mehdi SM Sajjadi, Antonio Vergari, Michael
Black, and Bernhard Sch¨olkopf.
From variational to de-
terministic autoencoders. arXiv preprint arXiv:1903.12436,
2019.
[12] Mingming Gong, Yanwu Xu, Chunyuan Li, Kun Zhang, and
Kayhan Batmanghelich. Twin auxilary classiﬁers gan. In
Advances in Neural Information Processing Systems, pages
1328–1337, 2019.
[13] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing
Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and
Yoshua Bengio. Generative adversarial nets. In Advances
in neural information processing systems, pages 2672–2680,
2014.
[14] Arthur Gretton, Karsten M Borgwardt, Malte J Rasch, Bern-
hard Sch¨olkopf, and Alexander Smola. A kernel two-sample
test. Journal of Machine Learning Research, 13(Mar):723–
773, 2012.
[15] Ishaan Gulrajani, Faruk Ahmed, Martin Arjovsky, Vincent
Dumoulin, and Aaron C Courville.
Improved training of
wasserstein gans. In Advances in neural information pro-
cessing systems, pages 5767–5777, 2017.
[16] Xifeng Guo, Long Gao, Xinwang Liu, and Jianping Yin. Im-
proved deep embedded clustering with local structure preser-
vation. In IJCAI, pages 1753–1759, 2017.
[17] Naama Hadad, Lior Wolf, and Moni Shahar.
A two-step
disentanglement method. In Proceedings of the IEEE Con-
ference on Computer Vision and Pattern Recognition, pages
772–780, 2018.
[18] Philip Haeusser, Johannes Plapp, Vladimir Golkov, Elie Al-
jalbout, and Daniel Cremers. Associative deep clustering:
Training a classiﬁcation network with no labels. In German
Conference on Pattern Recognition, pages 18–32. Springer,
2018.
[19] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner,
Bernhard Nessler, and Sepp Hochreiter. Gans trained by a
two time-scale update rule converge to a local nash equilib-
rium. In Advances in neural information processing systems,
pages 6626–6637, 2017.
[20] Xu Ji, Jo˜ao F Henriques, and Andrea Vedaldi.
Invariant
information clustering for unsupervised image classiﬁcation
and segmentation. In Proceedings of the IEEE International
Conference on Computer Vision, pages 9865–9874, 2019.
[21] Tero Karras, Miika Aittala, Janne Hellsten, Samuli Laine,
Jaakko Lehtinen, and Timo Aila. Training generative adver-
sarial networks with limited data. In Proc. NeurIPS, 2020.
[22] Tero Karras, Samuli Laine, Miika Aittala, Janne Hellsten,
Jaakko Lehtinen, and Timo Aila. Analyzing and improving
the image quality of StyleGAN. In Proc. CVPR, 2020.
[23] Hyunjik Kim and Andriy Mnih. Disentangling by factoris-
ing. arXiv preprint arXiv:1802.05983, 2018.
[24] Alex Krizhevsky, Geoffrey Hinton, et al. Learning multiple
layers of features from tiny images. 2009.
[25] Yann LeCun, L´eon Bottou, Yoshua Bengio, Patrick Haffner,
et al. Gradient-based learning applied to document recogni-
tion. Proceedings of the IEEE, 86(11):2278–2324, 1998.
[26] Daniel D Lee and H Sebastian Seung. Learning the parts
of objects by non-negative matrix factorization.
Nature,
401(6755):788, 1999.
[27] Yujia Li, Kevin Swersky, and Rich Zemel. Generative mo-
ment matching networks.
In International Conference on
Machine Learning, pages 1718–1727, 2015.
[28] Zinan Lin, Kiran Thekumparampil, Giulia Fanti, and Se-
woong Oh. Infogan-cr and modelcentrality: Self-supervised
model training and selection for disentangling gans. In In-
ternational Conference on Machine Learning, pages 6127–
6139. PMLR, 2020.
[29] Mario Lucic, Michael Tschannen, Marvin Ritter, Xiao-
hua Zhai, Olivier Bachem, and Sylvain Gelly.
High-
ﬁdelity image generation with fewer labels. arXiv preprint
arXiv:1903.02271, 2019.
[30] Laurens van der Maaten and Geoffrey Hinton.
Visualiz-
ing data using t-sne. Journal of machine learning research,
9(Nov):2579–2605, 2008.


## Page 10


[31] James MacQueen et al.
Some methods for classiﬁcation
and analysis of multivariate observations. In Proceedings of
the ﬁfth Berkeley symposium on mathematical statistics and
probability, volume 1, pages 281–297. Oakland, CA, USA,
1967.
[32] Alireza Makhzani, Jonathon Shlens, Navdeep Jaitly, Ian
Goodfellow, and Brendan Frey. Adversarial autoencoders.
arXiv preprint arXiv:1511.05644, 2015.
[33] Qi Mao, Hsin-Ying Lee, Hung-Yu Tseng, Siwei Ma, and
Ming-Hsuan Yang. Mode seeking generative adversarial net-
works for diverse image synthesis.
In Proceedings of the
IEEE Conference on Computer Vision and Pattern Recogni-
tion, pages 1429–1437, 2019.
[34] Michael F Mathieu, Junbo Jake Zhao, Junbo Zhao, Aditya
Ramesh, Pablo Sprechmann, and Yann LeCun. Disentan-
gling factors of variation in deep representation using adver-
sarial training. In Advances in Neural Information Process-
ing Systems, pages 5040–5048, 2016.
[35] Loic Matthey, Irina Higgins, Demis Hassabis, and Alexander
Lerchner. dsprites: Disentanglement testing sprites dataset,
2017.
[36] Mehdi Mirza and Simon Osindero. Conditional generative
adversarial nets. arXiv preprint arXiv:1411.1784, 2014.
[37] Sudipto Mukherjee, Himanshu Asnani, Eugene Lin, and
Sreeram Kannan.
Clustergan: Latent space clustering in
generative adversarial networks.
In Proceedings of the
AAAI Conference on Artiﬁcial Intelligence, volume 33, pages
4610–4617, 2019.
[38] Sameer A Nene, Shree K Nayar, Hiroshi Murase, et al.
Columbia object image library (coil-20). 1996.
[39] Chuang Niu, Jun Zhang, Ge Wang, and Jimin Liang. Gat-
cluster: Self-supervised gaussian-attention network for im-
age clustering. In European Conference on Computer Vision,
pages 735–751. Springer, 2020.
[40] Augustus Odena, Christopher Olah, and Jonathon Shlens.
Conditional image synthesis with auxiliary classiﬁer gans. In
International conference on machine learning, pages 2642–
2651. PMLR, 2017.
[41] Massimiliano Patacchiola, Patrick Fox-Roberts, and Edward
Rosten. Y-autoencoders: disentangling latent representations
via sequential-encoding. arXiv preprint arXiv:1907.10949,
2019.
[42] Alec Radford, Luke Metz, and Soumith Chintala.
Un-
supervised representation learning with deep convolu-
tional generative adversarial networks.
arXiv preprint
arXiv:1511.06434, 2015.
[43] Uri Shaham, Kelly Stanton, Henry Li, Boaz Nadler, Ronen
Basri, and Yuval Kluger. Spectralnet: Spectral clustering us-
ing deep neural networks. arXiv preprint arXiv:1801.01587,
2018.
[44] Ilya Tolstikhin, Olivier Bousquet, Sylvain Gelly, and Bern-
hard Schoelkopf. Wasserstein auto-encoders. arXiv preprint
arXiv:1711.01558, 2017.
[45] Michael Tschannen, Olivier Bachem, and Mario Lucic. Re-
cent advances in autoencoder-based representation learning.
arXiv preprint arXiv:1812.05069, 2018.
[46] Chu Wang, Marcello Pelillo, and Kaleem Siddiqi. Dominant
set clustering and pooling for multi-view 3d object recogni-
tion. arXiv preprint arXiv:1906.01592, 2019.
[47] Zhou Wang and Alan C Bovik. Mean squared error: Love
it or leave it? a new look at signal ﬁdelity measures. IEEE
signal processing magazine, 26(1):98–117, 2009.
[48] Zhou Wang, Alan C Bovik, Hamid R Sheikh, and Eero P Si-
moncelli. Image quality assessment: from error visibility to
structural similarity. IEEE transactions on image processing,
13(4):600–612, 2004.
[49] Lior Wolf, Tal Hassner, and Itay Maoz. Face recognition
in unconstrained videos with matched background similarity.
In Proceedings of the IEEE Conference on Computer Vision
and Pattern Recognition, pages 529–534, 2011.
[50] Han Xiao, Kashif Rasul, and Roland Vollgraf.
Fashion-
mnist: a novel image dataset for benchmarking machine
learning algorithms. arXiv preprint arXiv:1708.07747, 2017.
[51] Junyuan Xie, Ross Girshick, and Ali Farhadi. Unsupervised
deep embedding for clustering analysis.
In International
conference on machine learning, pages 478–487, 2016.
[52] Bo Yang, Xiao Fu, Nicholas D Sidiropoulos, and Mingyi
Hong. Towards k-means-friendly spaces: Simultaneous deep
learning and clustering. In Proceedings of the 34th Interna-
tional Conference on Machine Learning, volume 70, pages
3861–3870. JMLR.org, 2017.
[53] Jianwei Yang, Devi Parikh, and Dhruv Batra. Joint unsuper-
vised learning of deep representations and image clusters.
In Proceedings of the IEEE Conference on Computer Vision
and Pattern Recognition, pages 5147–5156, 2016.
[54] Xu Yang, Cheng Deng, Feng Zheng, Junchi Yan, and Wei
Liu. Deep spectral clustering using dual autoencoder net-
work. In Proceedings of the IEEE Conference on Computer
Vision and Pattern Recognition, pages 4066–4075, 2019.
[55] Grace XY Zheng, Jessica M Terry, Phillip Belgrader, Paul
Ryvkin, Zachary W Bent, Ryan Wilson, Solongo B Ziraldo,
Tobias D Wheeler, Geoff P McDermott, Junjie Zhu, et al.
Massively parallel digital transcriptional proﬁling of single
cells. Nature communications, 8:14049, 2017.
[56] Zhilin Zheng and Li Sun.
Disentangling latent space for
vae by label relevant/irrelevant dimensions. In Proceedings
of the IEEE Conference on Computer Vision and Pattern
Recognition, pages 12192–12201, 2019.


## Page 11


A. Appendix
A.1. Training algorithm
Algorithm 1: The training procedure of DC3-GAN.
Input: θ, ψ, φ initial parameters of Gθ, Dψ and Eφ, the dimension of latent code dn, the number of clusters K, the
batch size B, the number of critic iterations per end-to-end iteration M, the regularization parameters β1 - β3
Output: The parameters of Gθ, Dψ and Eφ
Data: Training data set x
1 while not converged do
2
for i=1, . . . , M do
3
Sample zn ∼P(zn) a batch of random noise
4
Sample zc a batch of random one-hot vectors
5
z ←(zc, zn)
6
xg ←Gθ(z)
7
Sample xr ∼Px a batch of the training dataset
8
ψ ←∇ψ(Dψ(xr) −Dψ(xg))
9
Sample zn ∼P(zn) a batch of random noise
10
Sample zc a batch of random one-hot vectors
11
z ←(zc, zn), xg ←Gθ(z)
12
(ˆzc, ˆzn) ←Eφ(xg)
13
(zr
c, zr
n) ←Eφ(xr)
14
zr ←(zr
c, zr
n), ˆxr ←Gθ(zr)
15
θ ←∇θ(−Dψ(Gθ(z)) + |xr −ˆxr| + β1 MMD(zr
n, zn) + β2||zn −ˆzn||2
2 + β3H(zc, ˆzc))
16
φ ←∇φ(|xr −ˆxr| + β1 MMD(zr
n, zn) + β2||zn −ˆzn||2
2 + β3H(zc, ˆzc))
A.2. Implementation details
Table 9. The dimensions of zc and zn in DC3-GAN for different datasets. Note that the dimension of one-hot discrete latent variables zc
is equal to the number of clusters.
Dataset
MNIST
Fashion-10
YTF
Pendigits
10x 73k
COIL-100
CIFAR-10
zc
10
10
41
10
8
100
10
zn
25
40
60
5
30
100
128
Table 10. The structure summary of the generator (G), discriminator (D), and encoder (E) in DC3-GAN for different datasets.
Dataset
Layer Type
G-1/D-4/E-4
G-2/D-3/E-3
G-3/D-2/E-2
G-4/D-1/E-1
MNIST
Conv-Deconv
4 × 4 × 64
4 × 4 × 128
-
-
Fashion-10
Conv-Deconv
4 × 4 × 64
4 × 4 × 128
-
-
YTF
Conv-Deconv
5 × 5 × 32
5 × 5 × 64
5 × 5 × 128
5 × 5 × 256
Pendigits
MLP
256
256
-
-
10x 73k
MLP
256
256
-
-
Table 9 summarizes the dimensions of latent variables for different datasets. And Table 10 summarizes the network
structures for different datasets. For the image datasets (MNIST, Fashion-MNIST, and YTF), we employ the similar Gθ and
Dψ of DCGAN [42] with conv-deconv layers, batch normalization and leaky ReLU activations with a slope of 0.2. The Eφ
uses the same architecture as Dψ except for the last layer. For the Pendigits and 10x 73k datasets, the Gθ, Dψ, and Eφ are
the MLP with 2 hidden layers of 256 hidden units each. The model parameters have been initialized following the random
normal distribution.
We evaluate our method on dSprites for disentanglement using the architectures shown in Table 11. The generator’s Adam
learning rate is set to 0.001 and The learning rates of discriminator and encoder are set to 0.002. The total number of epoches
is 28.


## Page 12


Table 11. The network structure of the generator (G), discriminator (D), and encoder (E) for dSprites experiments from [23]. We set the
dimensions of continuous and noise variables to 5 as infoGAN-CR [28].
Discriminator D / Encoder E
Generator G
Input 64 × 64 binary image
Input ∈R10
4 × 4 conv. 32 lReLU. stride 2
FC. 128 ReLU. batchnorm
4 × 4 conv. 32 lReLU. stride 2. batchnorm
FC. 4 × 4 × 64 ReLU. batchnorm
4 × 4 conv. 64 lReLU. stride 2. batchnorm
4 × 4 upconv. 64 lReLU. stride 2. batchnorm
4 × 4 conv. 64 lReLU. stride 2. batchnorm
4 × 4 upconv. 32 lReLU. stride 2. batchnorm
FC. 128 lReLU. batchnorm (*)
4 × 4 upconv. 32 lReLU. stride 2. batchnorm
From *: FC. 1 sigmoid. (output layer for D)
4 × 4 upconv. 1 sigmoid. stride 2
From *: FC. 128 lReLU. batchnorm. FC 10 for E
Table 12. The network structure for CIFAR-10 dataset from https://github.com/google/compare_gan. The ResBlock is the
resample of the residual block with downsampling and upsampling. The input shape of images is 32 × 32 × 3. The kernel size is described
in the format [filter h, filter w, stride] and the output shape is described as h × w × channels.
Discriminator D
Generator G
LAYER
KERNEL
OUTPUT
LAYER
KERNEL
OUTPUT
ResBlock
[3,3,1]
16 × 16 × 128
z
-
128
ResBlock
[3,3,1]
8 × 8 × 128
Linear
-
4 × 4 × 256
ResBlock
[3,3,1]
8 × 8 × 128
ResBlock
[3,3,1]
8 × 8 × 256
ResBlock
[3,3,1]
8 × 8 × 128
ResBlock
[3,3,1]
16 × 16 × 256
ReLU, Mean Pooling
-
128
ResBlock
[3,3,1]
32 × 32 × 256
Linear
-
1
BN, ReLU
-
32 × 32 × 256
Conv, Sigmoid
[3,3,1]
32 × 32 × 3
We also evaluate our method on CIFAR-10 dataset in a fully unsupervised settings. The architectures are shown in
Table 12. We use the Adam optimizer with a learning rate 0.0002 for the generator, the discriminator and the encoder
(β1 = 0.5, β2 = 0.999). We train the model with 5 discriminator steps before each generator and encoder step. The
dimension of zn is ﬁxed to 128, and the batch size is set to 64. The spectral normalization is used on both generator and
discriminator. We use the same class-conditional BatchNorm in the generator as Lucic et al. [29], to incorporate the category
information from zn. For the encoder, we combine the pre-trained SimCLR [6] model and trainable 2-layer MLP with hidden
size 512 and output size 138 ( dimensions of zn and zc). The self-supervised SimCLR model is pre-trained by following
the ofﬁcial implementation 4. The reasons of choosing pre-trained SimCLR model are based on reducing the parameters
of encoder, and improving training efﬁciency. Different from previous experiments, we apply the following regularization
parameters on CIFAR-10 dataset: β1 = β2 = 1, β3 = 1.
4https://github.com/google-research/simclr

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]