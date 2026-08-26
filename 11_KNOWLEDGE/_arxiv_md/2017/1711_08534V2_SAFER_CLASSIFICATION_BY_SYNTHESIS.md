---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1711.08534v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1711.08534v2_Safer_Classification_by_Synthesis

> Source: 1711.08534v2_Safer_Classification_by_Synthesis.pdf

> Pages: 12

---


## Page 1


Safer Classiﬁcation by Synthesis
William Wang, Angelina Wang, Aviv Tamar, Xi Chen & Pieter Abbeel
Dept. of Electrical Engineering and Computer Sciences
UC Berkeley
Berkeley, CA 94709
Abstract
The discriminative approach to classiﬁcation using deep neural networks has be-
come the de-facto standard in various ﬁelds. Complementing recent reservations
about safety against adversarial examples, we show that conventional discrimi-
native methods can easily be fooled to provide incorrect labels with very high
conﬁdence to out of distribution examples. We posit that a generative approach
is the natural remedy for this problem, and propose a method for classiﬁcation
using generative models. At training time, we learn a generative model for each
class, while at test time, given an example to classify, we query each generator for
its most similar generation, and select the class corresponding to the most similar
one. Our approach is general and can be used with expressive models such as
GANs and VAEs. At test time, our method accurately “knows when it does not
know,” and provides resilience to out of distribution examples while maintaining
competitive performance for standard examples.
1
Introduction
“What I cannot create, I do not understand.”
This famous quote by Richard Feynman stands in stark contrast to the majority of image classiﬁ-
cation breakthroughs of the last decade. The prevalent deep learning approach is discriminative,
where a deep network maps an observation into a probability over decisions, providing little to no
understanding of why a particular decision is chosen (e.g., Krizhevsky et al. 2012, Szegedy et al.
2015, He et al. 2016 among others). While this approach has demonstrated remarkable empirical
results, its opaque nature raises questions of safety and trust [Amodei et al., 2016].
For example, much attention has recently been focused on dealing with adversarial perturbations to
discriminative image classiﬁers, which make small image modiﬁcations that result in misclassiﬁca-
tion [Goodfellow et al., 2014b]. In this work we complement this view, by showing that discrim-
inative models can also be easily fooled to give erroneous predictions with a high conﬁdence for
out-of-distribution examples, which are signiﬁcantly different from examples in the data.
Motivated by the safety issues of discriminative classiﬁers, in this work we propose a safer genera-
tive image classiﬁcation paradigm. We build on recent breakthroughs in deep generative modelling
such as variational autoencoders (VAEs; Kingma and Welling 2014) and generative adversarial nets
(GANs; Goodfellow et al. 2014a), which have shown convincing results for generating complex
observations such as images directly from data. Our idea is to use labeled training data for building
generative models for images from each class. In these models (either GANs or VAEs), a random
input vector is transformed by a deep neural network into an image. At test-time, given an image to
classify, we search across the input vectors for an image that is sufﬁciently similar to the test image,
across all the generators. The corresponding class of the best image is taken as the classiﬁcation
result.
An immediate beneﬁt of this approach is interpretability – once a class decision is made, we know
exactly why it was chosen, since we readily know the image which our model imagined as most
arXiv:1711.08534v2  [cs.LG]  23 Jul 2018


## Page 2


representative of it. Another beneﬁt, which we show here to be signiﬁcant, is safety. When a
traditional discriminative model is trained to classify, say, road signs, we have no idea what it would
do when faced with an out-of-distribution example, say, of an elephant. This poses a severe problem
for safety critical systems such as self driving cars. Our model, by deﬁnition, would never generate
an image of an elephant if elephant images are not in the training data. Thus, distinguishing when
the model does not know becomes straightforward.
This brings us back to the premise in the Feynman quote. For objects that we understand, and can
therefore reliably generate, our model provides reliable classiﬁcation.
1.1
Related Work
Generative classiﬁcation is an old idea. Using shallow architectures, Ng and Jordan [2002] compared
discriminative and generative learning by investigating logistic regression and naive Bayes, and
observed improved performance of generative models in low-data regimes. Jaakkola and Haussler
[1999] used a generative model to extract kernels for a discriminative logistic regression classiﬁer.
In the seminal work of Hinton et al. [2006] on deep belief networks (DBNs), deep generative mod-
els for images and matching class labels were learned. For classiﬁcation using DBNs, the image
is used to calculate activations of a restricted Boltzman machine (RBM) for the image and label,
which are clamped, and MCMC sampling is then used to generate the corresponding label. Over
the last decade, DBNs have been outperformed by discriminative models trained using backpropa-
gation [Vincent et al., 2010, Krizhevsky et al., 2012].
More recently, generative models that can be trained using backpropagation have become popular.
VAEs [Kingma and Welling, 2014] and GANs [Goodfellow et al., 2014a] can be seen as extensions
of the Helmholtz machine model [Dayan et al., 1995], where a random vector with a known distri-
bution is mapped through a neural network to generate the data distribution. VAEs can be trained
using a variational lower bound, while GANs are trained using an adversarial method. While such
generative models have been used with success in semi-supervised learning [Kingma et al., 2014],
they have not yet been explored in the context of supervised learning. Given a test image, the VAE
recognition network can be used to sample from the distribution over latent variables, and generate
a similar image. For GANs, models that learn an inference network have been proposed [Donahue
et al., 2017, Dumoulin et al., 2017]. In this work we describe an alternative inference approach for
GANs that does not require a change to the training objective.
Selective classiﬁcation [Chow, 1957, El-Yaniv and Wiener, 2010] is an established approach for
improving classiﬁcation accuracy by rejecting examples that fall below a conﬁdence threshold. In
this work we use this method for rejecting out-of-distribution examples based on the conﬁdence
score. We build on the recent work of Geifman and El-Yaniv [2017], who investigated suitable
conﬁdence scores for deep neural networks. Very recently, Mandelbaum and Weinshall [2017]
studied different distance metrics for use as a conﬁdence score.
In concurrent work by other authors, generative models have been used to detect examples that
are outliers or outside the training distribution. Anonymous [2018a] uses a similar technique of
searching over the latent space of a GAN to discover outliers, but does not use such a technique for
classiﬁcation. Anonymous [2018b] trains GANs with feature matching loss to develop a model that
is capable of simultaneous classiﬁcation and novelty detection. While both of these use ROC curves
to benchmark their model, in our context of classiﬁcation, we believe that the risk-coverage analysis
is more appropriate, as it evaluate the conﬁdence of both classiﬁcation performance and novelty
detection. An ROC analysis of novelty detection, on the other hand, ignores information about the
classiﬁcation accuracy.
1.2
Our Contribution
In this work we make the following contributions.
1. Using the selective classiﬁcation paradigm, we show in a principled way that discrimina-
tively trained deep neural networks can easily be fooled by out-of-distribution examples.
2. We propose a general method for generative classiﬁcation, that can be used with either
GANs, VAEs, or even K-nearest neighbor methods as the generative model.
2


## Page 3


3. We show that our method can provide signiﬁcantly better resilience to out-of-distribution
examples, while maintaining competitive accuracy on within-class examples.
2
Preliminaries
Consider a classiﬁcation problem with K classes. The inputs (e.g., images) are denoted by x and
the outputs (classes) are denoted by y. Our data consists of pairs {xi, yi}, where xi ∼P(x) and
yi ∼P(y|xi).
Discriminative classiﬁcation learns a model Pθ(y|x) with parameters θ, typically by maximizing
the data log-likelihood maxθ
P
i log Pθ(yi|xi). A popular model for classiﬁcation is the softmax
Pθ(y = k|x) =
exp fθ,k(x)
P
j exp fθ,j(x), where fθ,k(x) for k = 1, ..., K are a deterministic functions, e.g., the
outputs of a neural network with weights θ.
2.1
Generative Models
The central component of our method is a generative mo del G, which takes as input a random
m-dimensional latent vector z from a distribution P(z) and learns to transform z into a sample
from P(x). Learning G is an unsupervised learning task, and recently, several efﬁcient training
methods that use backpropagation were proposed, such as GANs [Goodfellow et al., 2014a] and
VAEs [Kingma and Welling, 2014].
GANs are adversarially trained networks consisting of a generator and a discriminator. The gener-
ator network takes a latent vector and produces an image, while the discriminator network takes an
image and outputs a predicted probability that this image came from the distribution of the training
set. Training consists of a two-player game where the generator tries to produce images that the dis-
criminator is unable to distinguish from the training distribution, while the discriminator improves
its ability to discern between real data and generated images.
VAEs are trained using a variational lower bound, by learning a encoder network that maps a training
image into a corresponding distribution over the latent vector, and a decoder network that maps the
latent vector back into an image. The training balances the reconstruction loss of the decoder with
the Kullback-Leibler distance of the encoded latent vector distribution from P(z).
2.2
Selective Classiﬁcation
A central motivation for our approach is accurately identifying when the classiﬁer ‘does not know’
the correct class. This problem, typically explored in the context of discriminative classiﬁcation, is
known as selective classiﬁcation [Geifman and El-Yaniv, 2017].
Suppose we have a classiﬁer f which takes as input an image and outputs a predicted class along
with a measure of conﬁdence in its prediction. For example, f could be a CNN with the maximum
softmax output as its conﬁdence. Selective classiﬁers abstain from prediction if the conﬁdence score
is below a certain threshold θ.
The threshold parameter thus offers a balance between the proportion of the data classiﬁed and the
accuracy on this portion of the dataset. The coverage of a selective classiﬁer with threshold θ is
deﬁned as the proportion of test observations that are classiﬁed with conﬁdence greater than θ [El-
Yaniv and Wiener, 2010]. The empirical risk given θ is then deﬁned as the error rate on the subset
of the test set that was classiﬁed with conﬁdence greater than θ. A principled method for comparing
selective classiﬁers is to examine their risk-coverage plots, as exempliﬁed in Figure 1. Classiﬁers
with meaningful measures of conﬁdence should predict difﬁcult or out of distribution images with
lower conﬁdence, and thus, as the coverage is decreased, the risk should shrink to zero.
Recently, Geifman and El-Yaniv [2017] showed that for discriminatively-trained CNNs, threshold-
ing the softmax output provides state-of-the-art selective classiﬁcation, surpassing alternative conﬁ-
dence measures such as MC-Dropout [Gal and Ghahramani, 2016].
3


## Page 4


Figure 1: Risk-coverage plot for a CNN trained on MNIST. Observe that we can choose a conﬁdence
threshold such that around 90% of the data is covered, and for this data portion the classiﬁcation is
perfect. As we increase the desired coverage, the accuracy decreases (risk increases). Choosing a
threshold that covers more than 99 percent of the data will result in a sharp decrease in accuracy,
which indicates that the low-conﬁdence predictions generally correspond to misclassiﬁed data, as
we would expect.
3
Discriminative Models are Easily Fooled by Out-of-Distribution Examples
We begin our discussion by showing that a discriminatively trained CNN can easily be fooled to
give high-conﬁdence predictions to out-of-distribution examples – examples that are signiﬁcantly
different from any example in its training data, and that do not correspond to any particular class it
was trained to predict.
We present our results under the selective classiﬁcation paradigm, for a principled evaluation of
conﬁdence and accuracy. Consider the classiﬁcation task where a selective classiﬁer is trained on
data containing a certain set of classes, but is tested on data X1 ∪X2 where X1 contains data from
classes seen during training and X2 contains data that do not match any of the classes seen in the
training set. Obviously, the classiﬁer will be unable to correctly classify any points in X2, so we
expect it to abstain from prediction on these points. Concretely, we would like to pick a threshold
θ such that most points in X2 have conﬁdence less than θ and so are left unclassiﬁed, while most
points in X1 have conﬁdence greater than θ and are classiﬁed correctly. If the data in X1 and X2 is
signiﬁcantly different and our conﬁdence measure is reliable, we should be able to determine such a
threshold.
Unfortunately, as we show next, discriminative CNN classiﬁers are easily fooled to give high-
conﬁdence predictions for out-of-distribution examples that are wildly different from their training
data.
3.1
MNIST Augmented with Omniglot
We train a standard CNN on the well-known MNIST dataset and test its selectivity by running
predictions on MNIST augmented with 31460 rescaled images from the Omniglot dataset. The
Omniglot dataset, compiled by Lake et al. [2015], contains handwritten characters from 50 different
alphabets, such as in Figure 2b. The images were resized with nearest neighbor interpolation in
order to be the same 28 by 28 size as MNIST. We removed some ambiguous images such as those
in Figure 2c, where characters from different languages resembled digits to the point that even
a human would categorize them as numerical digits. Our augmented dataset is composed of 24
percent MNIST data and 76 percent Omniglot. Because the Omniglot images we chose to include
4


## Page 5


(a) MNIST
(b) Omniglot
(c) Removed Omniglot
Figure 2: MNIST and Omniglot data
Figure 3: Risk-coverage for CNN on augmented dataset. The lowest attainable risk is .061.
do not resemble the images from the MNIST training set, we should expect the CNN to predict
these images with low conﬁdence. Thus, we expect the risk-coverage plot1 to be similar to Figure 1
in that it starts off low and increases once the images the CNN is uncertain about are included
in classiﬁcation. Because MNIST composes 24 percent of our data and the CNN performs well
on the MNIST dataset, we expect a ﬂat line that begins to rise monotonically after the 24 percent
coverage mark. Further, we expect the risk to decrease towards 0 as we decrease the coverage -
this “vanishing risk” property reﬂects the idea that increased conﬁdence should be associated with
increased classiﬁcation accuracy, and can be observed in the MNIST experiment in Figure 1.
However, the risk-coverage plot we actually obtained for this experiment, shown in Figure 3, does
not exhibit the vanishing risk property. The lowest risk attainable by the CNN is .061 using the
maximum possible conﬁdence threshold of 1 (up to ﬂoating point precision) – in this case, 343
of the 5644 images classiﬁed with this threshold of conﬁdence were Omniglot images. These im-
ages, displayed in Figure 4, attain the highest level of conﬁdence despite not resembling any digit
from the MNIST training set, and thus there is no choice of threshold that will allow the CNN to
abstain from classifying these images. Combining the risk-coverage results from the MNIST and
augmented MNIST datasets, we see that if an image is classiﬁed with low conﬁdence, then it is likely
an incorrect classiﬁcation, but the converse is not true: if an image would be incorrectly classiﬁed,
then there is still a good chance that its prediction conﬁdence was high. Thus the CNN conﬁdence
metric does not accurately reﬂect the ability of the classiﬁer to make an precise prediction, given
out-of-distribution examples.
The results on this toy example may seem innocuous at ﬁrst glance. However, one can easily imagine
a scenario where such performance would lead to dire consequences. For example, a realistic sce-
nario for self-driving cars is to defer a decision about road signs to a human based on its conﬁdence
in prediction. From what we learned in this toy example, a CNN conﬁdence cannot be trusted if, say,
1For calculating the risk in the risk coverage plot with the augmented data set, every prediction of an
Omniglot image is considered to be wrong.
5


## Page 6


Figure 4: Omniglot Images Classiﬁed by CNN with Highest Conﬁdence
a new road sign is introduced, but also if any random object not seen during training is encountered
on the road.
Figure 5: An illustration of an out-of-distribution example with a discriminative classiﬁer. Here, a
classiﬁer discriminates between the square and circle examples. We can relate the conﬁdence of the
classiﬁer with the distance to the decision boundary. As shown, an out-of-distribution example that
is far away from this boundary will be classiﬁed with a high conﬁdence to belong, in this case, to
the class of circles.
In principle, the fact that a discriminative approach can be fooled by out-of-distribution examples
should not be very surprising. In Figure 5 we provide an explanation for this result in a simple
binary classiﬁcation task. Intuitively, the conﬁdence of a discriminative classiﬁer can be related to
the distance from the decision boundary. Therefore, we can imagine that there exists examples that
are very different from our data, but still lie far away from the decision boundary, and therefore have
a high conﬁdence value. While it is not immediate that the conclusion from this toy example carries
over to high-dimensional problems and expressive CNN classiﬁers, our results above suggest that
this is indeed the case.
From Figure 5 it is also clear that a viable solution for the out-of-distribution detection problem is to
identify examples that are too far, in some suitable distance metric, from the training data [Mandel-
baum and Weinshall, 2017]. The problem then becomes how to identify a suitable distance metric,
and how to compute the distance efﬁciently, as typically the distance computation scales with the
amount of training data. In the following we propose an alternative approach based on generative
models. The idea is that by learning to generate samples from a low-dimensional latent vector, we
would effectively learn the manifold for each class. The distance to each manifold is expected to be
a reliable measure for classiﬁcation conﬁdence.
4
Generative Approach to Classiﬁcation
We now propose a different approach to classiﬁcation, which, by relying on a generative model,
provides a better signal for knowing when an example from an unknown class is encountered.
6


## Page 7


4.1
Generative Classiﬁer Model
Our generative classiﬁer consists of class-conditional generative models Gk(z) and a similarity mea-
sure s(x1, x2). Each generator takes as input a latent variable (say, a random uniform variable over
[−1, 1]m) and outputs a generated image of its respective class. The similarity measure s(x1, x2)
could be the negative L2 or L1 distance between x1 and x22, or it could be a more complex function
such as a Siamese network [Koch et al., 2015] that predicts the probability the two images are of the
same class.
In this work we only consider the negative L2 distance, which allows a fair comparison with con-
ventional novelty detection approaches that use similarity metrics. In the future we will investigate
using alternative measures of similarity not exclusive to metrics.
To classify a test image x with class y, for each generator Gk, we solve the following optimization
problem:
z∗
k = arg max
z
s(x, Gk(z))
(1)
That is, for each class k, we ﬁnd the most similar image in the range of Gk to the test image x under
the similarity measure s, and keep track of the latent vector that produces it, z∗
k. Once we have the
optimal latent vectors for each class, we classify x as
arg max
k
s(x, Gk(z∗
k))
In practice, (1) is a non-convex optimization problem. As an optimization heuristic, we perform
Monte Carlo sampling from P(z), evaluate the similarity to the generated image for each latent
variable, and use the optimal latent vector as a starting point for a further non-linear optimization
method such as L-BFGS [Nocedal, 1980]. If the generative model is a VAE with a Gaussian latent
model, then we also have the option of feeding the test image into the encoder network to obtain a
parameter estimate for the mean of the Gaussian and use that as a heuristic to solve the optimization.
We ﬁnd that this method works better in practice for the goal of classiﬁcation accuracy.
4.2
Comparison with Nearest Neighbors
Our approach has parallels with the 1-nearest neighbor classiﬁer - in both methods, to classify a test
point, there is an optimization performed to ﬁnd the most similar match over some set of images
with known classes. For nearest neighbors, this is the training set, while for our generative classiﬁer,
this is the set of all images that are in the range of our generators. Because the generators are
presumably capable of reproducing the training set, we would expect our method to outperform
nearest neighbors in classiﬁcation accuracy, as long as the generator spaces for each class do not
intersect. Nearest neighbors can be improved on by using different distance metrics - for example,
the L3 distance is known to outperform the L2 distance on MNIST. Similarly, it would be possible
to use such distance metrics with our generative classiﬁer. While the runtime of nearest neighbors
increases with the number of training samples, our method does not, and its runtime is controlled by
hyperparameters for the optimization routine.
Nearest neighbors has the desirable property of interpretability - with any prediction, there is a ratio-
nale for the prediction in the form of the closest image to the test point and its metric score. By using
this score as a conﬁdence value, we can view KNN as a selective classiﬁer, and we would expect
that higher conﬁdence thresholds would lead to more accurate predictions. Our generative classiﬁer
retains these properties - for example, we can visualize the optimization procedure, yielding a set of
images that explains why our classiﬁer made its prediction (Figure 6). We can also take the max-
imum similarity as a conﬁdence measure for the purpose of selective classiﬁcation, and intuitively
this should accurately reﬂect the ability of the classiﬁer to accurately make a prediction.
7


## Page 8


Figure 6: MNIST classiﬁcation performed by a generative classiﬁer: test image on the left accom-
panied with generated images and their L2 distances to test point. All generators try their best to
match the test image, and the predicted class is the class of the image that most closely matches the
test image in L2 distance.
(a) The GAN and VAE misclassify the 6, but their
predicted classes disagree. Both generated images
exhibit a right slant to match the test image.
(b) The 8 and 6 generators for GAN and VAE re-
spectively are capable of producing an image sim-
ilar to the 5 in L2 distance.
Figure 7: The mistakes made by the generative classiﬁer can be interpretable - on the left we see
that the model has not learned how to reproduce the test image, resulting in an unconﬁdent, incorrect
prediction. On the right we see that the generator of an incorrect class is capable of reproducing the
test image to some extent, pointing to degeneracies in the generator space.
5
MNIST Experiments
5.1
Model Training
For the generative models, we trained DCGANs [Radford et al., 2015] with a 15-dimensional la-
tent space and VAEs with a 10-dimensional latent space - the dimensions were chosen by cross-
validation. For both generative models, we used an L2 similarity measure. To train the DCGANs,
we employed techniques such as label smoothing [Salimans et al., 2016], noise injection [Arjovsky
and Bottou, 2017], and weight normalization [Salimans and Kingma, 2016], which helped to im-
prove the quality of the images and stabilize training.
5.2
Results
Using a DCGAN as our generative model, we achieved an accuracy of 97.81 percent on MNIST.
Using a VAE with the encoder output in place of iterative optimization, we achieved an accuracy
of 98.35 percent. As a baseline, 1 nearest neighbor achieves an accuracy of 96.91 percent. In
addition, the mistakes made by the generative classiﬁcation method are readily interpretable - in
Figure 7a, both GAN and VAE models are unable to produce the 6 that is in the test set, which
demonstrates that this test 6 is dissimilar from the 6’s seen in the training set and thus is more
difﬁcult to correctly classify. Indeed, the conﬁdence for the GAN and VAE predictions lie within
the bottom 5.48 and 7.07 percentiles of the conﬁdences for these respective models. However, one
issue with this classiﬁcation method is that it highly depends on the regularity of the images that
are produced by the generators - if a test image is a 5 and the 8 generator is capable of producing
something that looks like the 5, then it is possible for our method to misclassify the 5 as an 8 - see
Figure 7b. We observed similar results when using various recent generative model formulations
that are known to produce high quality images such as Wasserstein GAN [Arjovsky et al., 2017].
One possible ﬁx is to try alternative similarity measures - the two images that are produced by the
generators in Figure 7b are similar to the test image in L2 distance, but they may not be close with
respect to another similarity measure. On the other hand, the optimization procedure can exploit
2These similarities would be the negative distance, since according to our convention, larger values of
s(x1, x2) should mean the images are more similar.
8


## Page 9


more complex neural network similarity metrics by ﬁnding images that do not visually resemble
the test image but still produce high similarity scores. Another approach would be to train the
generators in such a way that the search space for a certain conditional generator does not contain
examples from other classes. For example, BEGAN [Berthelot et al., 2017] is a variation of GAN
with a hyperparameter that controls the trade-off between image quality and image diversity, so it is
possible that emphasizing image quality would remove such out-of-distribution examples from each
conditional GAN’s search space.
Figure 8: MNIST images misclassiﬁed by KNN but correctly classiﬁed by VAE-based GC using
L2 distance from test image. Each horizontal triplet of images shows the test image, the nearest
neighbor in the data, and the VAE generated image. The VAE is able to produce images very similar
to the test image, while no such images of the correct class exist in the training set and so KNN
misclassiﬁes the data.
6
Out-of-Distribution Results for Generative Classiﬁers
We run the same out of distribution experiment on Omniglot-augmented MNIST using the gen-
erative classiﬁer models described above. We ﬁnd that although the generative classiﬁer with L2
distance has a lower baseline performance than the CNN on the original test set, it does possess the
vanishing risk property even with the inclusion of out-of-distribution examples, as demonstrated in
the risk-coverage plot in Figure 9b. This means that in contrast to the CNN, the risk can be driven
down to zero by increasing the selectivity - thus the conﬁdence measure really does reﬂect the clas-
siﬁer’s inherent ability to classify an image. As an example, Figure 10 displays the optimal images
produced by our generators on an Omniglot image that was classiﬁed by a CNN with the highest
possible conﬁdence. Our generators are unable to match this image, and the closest L2 distance
achieved is on the order of 10−2, as opposed to the L2 distances on the order of 10−3 on MNIST
images as seen in Figure 6. The lower conﬁdence score of the generative classiﬁer on Omniglot
reﬂects the fact that we cannot actually classify these images correctly, while the high conﬁdence of
the CNN on these images misleads us to believe that we are capable of doing so.
In order to improve the accuracy on MNIST while preserving our desirable selectivity properties,
we can ﬁrst use the generator conﬁdence to determine coverage – after thresholding appropriately,
we can use the CNN to make a ﬁnal classiﬁcation of the data. This procedure of generative novelty
detection and CNN classiﬁcation results in a risk-coverage curve that lies entirely at or below the
CNN curve (Figure 9a). Thus we are able to maintain the same performance on MNIST while
achieving the desired selectivity properties.
Future work in improving the generative models and selecting an appropriate similarity measure
may result in a generative classiﬁer that can simultaneously outperform the CNN in classiﬁcation
and serve as a novelty detector.
7
Conclusion
We proposed a general method for classiﬁcation using generative models that can be used with
various VAE and GAN models. As we have shown, the generative approach offers resilience to
misclassiﬁcation of out-of-distribution examples, and provides a reliable measure of classiﬁcation
conﬁdence.
Much more work is required to scale our approach to more challenging image recognition domains.
At present, we are not aware of generative models that can reliably capture the latent manifold of
9


## Page 10


(a) Using a GC as novelty detection globally
outperforms using the CNN softmax thresh-
old.
(b) The GC outperforms the CNN for low
values of coverage.
Figure 9: Risk-coverage for generative classiﬁer. Left: results for the generative classiﬁers (VAE
and GAN) vs. the discriminative CNN. Note that for low coverage, the generative classiﬁers perform
better (risk is lower and vanishes to zero). For higher coverage, the CNN outperforms the gener-
ative models due to its higher accuracy on in-distribution examples. Right: using the generative
models for novelty detection and the CNN for classiﬁcation, we obtain models that outperform the
discriminative CNN for all coverage values.
Figure 10: An Omniglot image classiﬁed with high conﬁdence by a CNN is classiﬁed with low
conﬁdence by a GAN-based generative classiﬁer. The L2 distance to the closest image is an order
of magnitude higher than that of the MNIST images in Figure 6.
complex realistic images such as in the Imagenet dataset [Deng et al., 2009], although considerable
progress has been made [e.g., the impressive results of Karras et al., 2017]. We believe that our
work provides additional motivation for further improving the performance of generative models.
Our work also offers a possible principled way of evaluating a generative model by its performance
when used as a generative classiﬁer. Future research in fundamentally understanding and controlling
the behavior of generative models will increase their effectiveness when applied to problems such
as safe prediction.
Acknowledgement
This work was funded in part by Siemens and by an ONR PECASE N000141612723.
References
Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Man´e. Con-
crete problems in ai safety. arXiv preprint arXiv:1606.06565, 2016.
Anonymous.
Anomaly detection with generative adversarial networks.
International Confer-
ence on Learning Representations, 2018a. URL https://openreview.net/forum?id=
S1EfylZ0Z.
Anonymous. Novelty detection with gan. International Conference on Learning Representations,
2018b. URL https://openreview.net/forum?id=Hy7EPh10W.
Martin Arjovsky and L´eon Bottou. Towards principled methods for training generative adversarial
networks. arXiv preprint arXiv:1701.04862, 2017.
10


## Page 11


Martin Arjovsky, Soumith Chintala, and L´eon Bottou.
Wasserstein gan.
arXiv preprint
arXiv:1701.07875, 2017.
David Berthelot, Tom Schumm, and Luke Metz. Began: Boundary equilibrium generative adversar-
ial networks. arXiv preprint arXiv:1703.10717, 2017.
Chi-Keung Chow. An optimum character recognition system using decision functions. IRE Trans-
actions on Electronic Computers, EC-6(4):247–254, 1957.
Peter Dayan, Geoffrey E Hinton, Radford M Neal, and Richard S Zemel. The helmholtz machine.
Neural computation, 7(5):889–904, 1995.
J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei. ImageNet: A Large-Scale Hierarchical
Image Database. In CVPR09, 2009.
Jeff Donahue, Philipp Kr¨ahenb¨uhl, and Trevor Darrell. Adversarial feature learning. In Proceedings
of the International Conference on Learning Representations (ICLR), 2017.
Vincent Dumoulin, Ishmael Belghazi, Ben Poole, Alex Lamb, Martin Arjovsky, Olivier Mastropi-
etro, and Aaron Courville. Adversarially learned inference. In Proceedings of the International
Conference on Learning Representations (ICLR), 2017.
Ran El-Yaniv and Yair Wiener. On the foundations of noise-free selective classiﬁcation. Journal of
Machine Learning Research, 11(May):1605–1641, 2010.
Yarin Gal and Zoubin Ghahramani. Dropout as a bayesian approximation: Representing model
uncertainty in deep learning. In international conference on machine learning, pages 1050–1059,
2016.
Yonatan Geifman and Ran El-Yaniv. Selective classiﬁcation for deep neural networks, 2017.
Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair,
Aaron Courville, and Yoshua Bengio. Generative adversarial nets. In Advances in neural infor-
mation processing systems, pages 2672–2680, 2014a.
Ian J Goodfellow, Jonathon Shlens, and Christian Szegedy. Explaining and harnessing adversarial
examples. arXiv preprint arXiv:1412.6572, 2014b.
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recog-
nition. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages
770–778, 2016.
Geoffrey E Hinton, Simon Osindero, and Yee-Whye Teh. A fast learning algorithm for deep belief
nets. Neural computation, 18(7):1527–1554, 2006.
Tommi Jaakkola and David Haussler. Exploiting generative models in discriminative classiﬁers. In
Advances in neural information processing systems, pages 487–493, 1999.
Tero Karras, Timo Aila, Samuli Laine, and Jaakko Lehtinen. Progressive growing of gans for im-
proved quality, stability, and variation. arXiv preprint arXiv:1710.10196, 2017.
Diederik P Kingma and Max Welling. Auto-encoding variational bayes. In Proceedings of the 2nd
International Conference on Learning Representations (ICLR), 2014.
Diederik P Kingma, Shakir Mohamed, Danilo Jimenez Rezende, and Max Welling. Semi-supervised
learning with deep generative models. In Z. Ghahramani, M. Welling, C. Cortes, N. D. Lawrence,
and K. Q. Weinberger, editors, Advances in Neural Information Processing Systems 27, pages
3581–3589, 2014.
Gregory Koch, Richard Zemel, and Ruslan Salakhutdinov. Siamese neural networks for one-shot
image recognition. In Proceedings of the 32nd international conference on Machine learning.
ACM, 2015.
11


## Page 12


Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. Imagenet classiﬁcation with deep convolu-
tional neural networks. In Advances in neural information processing systems, pages 1097–1105,
2012.
Brendan M Lake, Ruslan Salakhutdinov, and Joshua B Tenenbaum. Human-level concept learning
through probabilistic program induction. Science, 350(6266):1332–1338, 2015.
Amit Mandelbaum and Daphna Weinshall. Distance-based conﬁdence score for neural network
classiﬁers. arXiv preprint arXiv:1709.09844, 2017.
Andrew Y Ng and Michael I Jordan. On discriminative vs. generative classiﬁers: A comparison of
logistic regression and naive bayes. In Advances in neural information processing systems, pages
841–848, 2002.
Jorge Nocedal. Updating quasi-newton matrices with limited storage. Mathematics of computation,
35(151):773–782, 1980.
Alec Radford, Luke Metz, and Soumith Chintala. Unsupervised representation learning with deep
convolutional generative adversarial networks. arXiv preprint arXiv:1511.06434, 2015.
Tim Salimans and Diederik P Kingma. Weight normalization: A simple reparameterization to accel-
erate training of deep neural networks. In Advances in Neural Information Processing Systems,
pages 901–909, 2016.
Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen.
Improved techniques for training gans. In Advances in Neural Information Processing Systems,
pages 2234–2242, 2016.
Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Du-
mitru Erhan, Vincent Vanhoucke, and Andrew Rabinovich. Going deeper with convolutions. In
Proceedings of the IEEE conference on computer vision and pattern recognition, pages 1–9, 2015.
Pascal Vincent, Hugo Larochelle, Isabelle Lajoie, Yoshua Bengio, and Pierre-Antoine Manzagol.
Stacked denoising autoencoders: Learning useful representations in a deep network with a local
denoising criterion. Journal of Machine Learning Research, 11(Dec):3371–3408, 2010.
12

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]