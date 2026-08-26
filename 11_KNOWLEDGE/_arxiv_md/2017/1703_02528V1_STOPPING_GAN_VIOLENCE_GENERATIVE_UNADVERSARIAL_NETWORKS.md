---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1703.02528v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1703.02528v1_Stopping_GAN_Violence__Generative_Unadversarial_Networks

> Source: 1703.02528v1_Stopping_GAN_Violence__Generative_Unadversarial_Networks.pdf

> Pages: 7

---


## Page 1


Under review as a conference paper at SIGBOVIK 2017
STOPPING GAN VIOLENCE:
GENERATIVE UNADVERSARIAL NETWORKS
Samuel Albanie∗
Institute of Deep Statistical Harmony
Shelfanger, UK
S´ebastien Ehrhardt∗
French Foreign Legion
Location Redacted
Jo˜ao F. Henriques∗
Centre for Discrete Peace, Love and Understanding
Coimbra, Portugal
ABSTRACT
While the costs of human violence have attracted a great deal of attention from
the research community, the effects of the network-on-network (NoN) violence
popularised by Generative Adversarial Networks have yet to be addressed. In this
work, we quantify the ﬁnancial, social, spiritual, cultural, grammatical and der-
matological impact of this aggression and address the issue by proposing a more
peaceful approach which we term Generative Unadversarial Networks (GUNs).
Under this framework, we simultaneously train two models: a generator G that
does its best to capture whichever data distribution it feels it can manage, and a
motivator M that helps G to achieve its dream. Fighting is strictly verboten and
both models evolve by learning to respect their differences. The framework is
both theoretically and electrically grounded in game theory, and can be viewed
as a winner-shares-all two-player game in which both players work as a team to
achieve the best score. Experiments show that by working in harmony, the pro-
posed model is able to claim both the moral and log-likelihood high ground. Our
work builds on a rich history of carefully argued position-papers, published as
anonymous YouTube comments, which prove that the optimal solution to NoN
violence is more GUNs.
Takes skill to be real, time to heal each other
Tupac Shakur, Changes, 1998
1
INTRODUCTION
Deep generative modelling is probably important (see e.g. Bengio et al. (2013a), Bengio et al.
(2013b), Bengio et al. (2007a), Bengio et al. (2015) Bengio et al. (2007b) and (Schmidhuber et al.,
circa 3114 BC)). Justiﬁcations recently overheard in the nightclubs of Cowley1 include the ability
to accurately approximate data distributions without prohibitively expensive label acquisition, and
computationally feasible approaches to beating human infants at chess2. Deep generative modelling
∗Authors are listed according to the degree to which their home nation underperformed at the 2016 European
football championships
1The nightclubs of Cowley are renowned for their longstanding philosophical support for Dubstep, Grime
and Connectionism, and should not be confused with the central Oxford nightclub collective which leans more
towards Dubstep, Grime and Computationalism - speak to Old Man Bridge at 3am on a Friday morning under
the stairs of the smoking area for a more nuanced clariﬁcation of the metaphysical differences of opinion.
2Infants of other species (fox cubs, for example) remain an adorable open question in the ﬁeld.
1
arXiv:1703.02528v1  [stat.ML]  7 Mar 2017


## Page 2


Under review as a conference paper at SIGBOVIK 2017
Figure 1: The proposed unadversarial training protocol. The generator G proposes samples, PROPS,
and in return receives acknowledgements and praise, ACKS from the motivator M. As a direct
consequence of the sense of teamwork fostered by our optimisation scheme, synergy abounds. Note:
this ﬁgure best viewed at a distance, preferably at low resolution.
was broadly considered intractorable, until recent groundbreaking research by Goodfellow et al.
(2014) employed machiavellian adversarial tactics to demonstrate that methaphorical tractors could
in fact be driven directly through the goddamn centre of this previously unploughed research ﬁeld
(subject to EU agricultural safety and set-aside regulations).
The key insight behind Generative Adversarial Networks (commonly referred to as GANs, GANGs
or CAPONEs depending on sources of counterfeit currency) is to pit one model against another in a
gladiatorial quest for dominance. However, as ably illustrated by respected human actor and philan-
thropist Russell Crowe in the documentary Gladiator, being an actual gladiator isn’t all sunshine
and rainbows—although it’s possible to get a great tan, one still has to wear sandals.
Even though we are only in the introduction, we now bravely leap into a series of back-of-the-
envelope calculations to compute a lower bound on the cost of that violence for the case of middle
aged, median-income Generative Adversarial Networks living in comfortable, but affordable accom-
modation in the leafy suburbs of an appropriate class of functions.
Following the literature, we deﬁne the adversaries as two models, a discriminator D and a generator
G. However, since we don’t agree with the literature or wish to condone its violent actions in any
form, we immediately redeﬁne the models as follows:
D, G := G, D
(1)
Note that the equation above is valid and above board, since the current version of mathematics
(v42.1 at the time of writing) supports simultaneous assignment3. Therefore, in the following ex-
position, D represents the generator and G represents the discriminator. Next, we deﬁne a cost
function, C : V →$, mapping the space of model violence V into the space $ spanned by all
mattresses stuffed with U.S. dollars, as follows:
C(V ) = α
ˆ
βV (G)
(2)
in which βV is a violent and discriminatory mapping from the discriminator G to the closest math-
ematical structure which appears to be a human brain and α is a constant representing the cost of
human violence, to be determined by trawling through posts on social media. Note that βV may be
a violent function, but not crazy-violent (i.e. it must be Khinchin-integrable)4.
3We caution readers not to rely on this assumption in future versions. Mathematics has not supported
backwards compatability since Kurt “Tab-Liebehaber” G¨odel re-implemented the entire axiomatic foundations
of the language rather than be constrained to four-space equation indentation (see G¨odel (1931) for the details).
4Since Neuroscience tells us that human brains are AlexVGGIncepResNets almost-everywhere, in practice
we found that these functions need not be overly belligerent.
2


## Page 3


Under review as a conference paper at SIGBOVIK 2017
To evaluate this cost, we ﬁrst compute α with a melancholy search of Twitter, uniquely determining
the cost of violence globally as $1876 for every person in the world (Twitter, 2016). Integrating
over all discriminators and cases of probable discrimination, we arrive at a conservative value of 3.2
gigamattresses of cost. By any reasonable measure of humanity (ﬁnancial, social, spiritual, cultural,
grammatical or indeed dermatological), this is too many gigamattresses.
Having made the compelling case for GUNs, we now turn to the highly anticipated related work
section, in which we adopt a petty approach to resolving disagreements with other researchers by
purposefully avoiding references to their relevant work.
2
RELATED WORK
These violent delights have violent ends
Geoff Hinton, date unknown
Our work is connected to a range of adversarial work in both the machine learning and the machine
forgetting communities. To the best of our knowledge Smith & Wesson (1852) were the ﬁrst to
apply GUNs to the problem of generative modelling, although similar ideas have been explored in
the context of discriminative modelling as far back as the sixteenth century by Fabbrica d’Armi
Pietro Beretta in an early demonstration of one-shot learning. Unfortunately, since neither work
evaluated their approach on public benchmarks (not even on MNIST), the signiﬁcance of their ideas
remains under appreciated by the machine learning community.
Building on the approach of Fouhey & Maturana (2012)5, we next summarise the adversarial liter-
ature most closely related to ours, ordered by Levenshtein edit distance: GAN (Goodfellow et al.,
2014), WGAN (Arjovsky et al., 2017), DCGAN (Radford et al., 2015), LAPGAN (Denton et al.,
2015), InfoGAN (Chen et al., 2016), StackedGAN (Huang et al., 2016) and UnrolledGAN (Metz
et al., 2016)6.
Unadversarial approaches to training have also received some attention, primarily for models used
in other domains such as fashion (Crawford, 1992) and bodybuilding (Schwarzenegger, 2012)).
Some promising results have also been demonstrated in the generative modelling domain, most
notably through the use of Variational Generative Stochastic Networks with Collaborative Shaping
(Bachman & Precup, 2015). Our work makes a fundamental contribution in this area by dramatically
reducing the complexity of the paper title.
3
GENERATIVE UNADVERSARIAL NETWORKS
Under the Generative Unadversarial Network framework, we simultaneously train two models: a
generator G that does its best to capture whichever data distribution it feels it can manage and
a motivator M that helps G to achieve its dream. The generator is trained by learning a function
G(⃗z; θg) which transforms samples from a uniform prior distribution pz(⃗z) into the space graciously
accommodating the data7. The motivator is deﬁned as a function M(⃗x; θM) which uses gentle
gradients and persuasive language to encourage G to improve its game. In particular, we train G to
maximise log(M(G(⃗z)) and we simultaneously train M to maximise log(M(G(⃗z)). Thus, we see
that the objectives of both parties are aligned, reducing conﬂict and promoting teamwork.
The core components of our framework are illustrated in Figure 1. The GUN training scheme
was inspired largely by Clint Eastwood’s memorable performance in Dirty Harry but also in part
by the Transmission Control Protocol (TCP) three-way handshake (Postel et al., 1981), which was
among the ﬁrst protocols to build harmony through synergy, acknowledgements and the simple act of
5This innovative work was the ﬁrst to introduce the concept of an alphabetically-related, rather than
scientiﬁcally-related literature review.
6In the interest of an unadversarial literature review, we note that Bishop (2006) and Murphy (2012) make
equally good (up to ϵ = 10−6) references for further exploration of this area.
7The choice of the uniform prior prevents discrimination against prior samples that lie far from the mean.
It’s a small thing, but it speaks volumes about our inclusive approach.
3


## Page 4


Under review as a conference paper at SIGBOVIK 2017
Figure 2: (a) GUNs are trained by updating the generator distribution G (yellow line) with the help
and support of the motivator (red line) to reach its dream of the data distribution (blue dashed).
(b) With a concerted effort, the generator reaches its goal. (c) Unlike previous generators which
were content with simply reaching this goal, our generator is more motivated and gives it ‘110%’
moving it a further 10% past the data distribution. While this isn’t terribly helpful from a modelling
perspective, we think it shows the right kind of attitude.
Algorithm 1 Training algorithm for Generative Unadversarial Networks
1: procedure TRAIN
2:
for #iterations do
3:
Sample n noise samples from prior pz(⃗z) and compute G(⃗z(1); θg), ...G(⃗z(n); θg).
4:
Sample n data samples ⃗x(1), ...⃗x(n), from the data distribution.
5:
Let G show pairs (⃗x(i), G(⃗z(i); θg)) to M as slides of a powerpoint presentation8.
6:
Sample constructive criticism and motivational comments from M.
7:
Update the powerpoint slides and incorporate suggestions into θG.
shaking hands. A description of the training procedure used to train G and M is given in Algorithm
1.
Algorithm 1 can be efﬁciently implemented by combining a spare meeting room (which must have a
working projector) and a top notch deep learning framework such as MatConvNet (Vedaldi & Lenc,
2015) or Soumith Chintala (Chintala, 2012-present). We note that we can further improve training
efﬁciency by trivially rewriting our motivator objective as follows9:
θ∗
M = min
θM
˛
S(G)
log(R) + log(1 −ζ)
(3)
Equation 3 describes the ﬂow of reward and personal well-being on the generator network surface.
ζ is a constant which improves the appearance of the equation. In all our experiments, we ﬁxed the
value of ζ to zero.
8To guarantee polynomial runtime, it is important to ensure that the generator is equipped with the appro-
priate dongle and works through any issues with the projector before the presentation begins.
9If this result does not jump out at you immediately, read the odd numbered pages of (Amari & Nagaoka,
2000) . This book should be read in Japanese. The even-numbered pages can be ripped out to construct beautiful
orizuru.
4


## Page 5


Under review as a conference paper at SIGBOVIK 2017
Figure 3: Visualised samples from the GUN model trained on MNIST11(the nearest training exam-
ples are shown in the right hand column). Note that these samples have been carefully cherry picked
for their attractive appearance. Note how the GUN samples are much clearer and easier to read than
the original MNIST digits.
4
EXPERIMENTS
Give the people what they want (MNIST)
Yann LeCun, date unknown
In this section we subject the GUN framework to a rigorous qualitative experimental evaluation by
training unadversarial networks on MNIST. Rather than evaluating the model error-rate or proba-
bility on withheld test data, we adopt a less confrontational metric, opportunities for improvement.
We also assess samples generated by the trained model by gut feeling, enabling a direct comparison
with a range of competing generative approaches. Following academic best practices, key imple-
mentation details can be found in our private code repository10.
We warm-start the network with toy data taken from the latest Lego catalog. To nurture the right
kind of learning environment, we let the network ﬁnd its own learning rate and proceed by making
ϵ-greedy updates with an ϵ value of 1. We consider hard-negative mining to be a gratuitously harsh
training procedure, and instead perform easy-positive mining for gentler data digestion.
We now turn to the results of the experiment. Inspired by the Finnish education system, we do not
test our models during the ﬁrst formative epochs of development. A quantitative comparison with
two other popular generative approaches has been withheld from publication to respect the privacy
of the models involved. However, we are able to reveal that GUN had by far the most opportunities
for improvement. We observed a sharp increase in performance once we all agreed that the network
was doing well. By constrast, the adversarial nature of standard GAN methodologies usually elicits a
ﬁght-or-ﬂight behavior, which can result in vanishing gradients and runaway losses. Samples drawn
from the trained network are shown in Figure 3.
5
CONCLUSION
In this work, we have shown that network-on-network violence is not only unethical, it is also
unnecessary. Our experiments demonstrate that happy networks are productive networks, laying the
groundwork for advances in motivational machine learning. Indeed, unadversarial learning is an
area rife with opportunities for further development. In future work, we plan to give an expanded
treatment of important related subjects including nurtural gradients and k-dearest neighbours12.
10We also make available a public copy of this repository which almost compiles.
For the sake of
brevity, all code comments, variables and function calls have been helpfully removed and replaced cross-
platform, universally compatible ascii art. The code can be found at http://github.com/albanie/
SIGBOVIK17-GUNs.
11For ease of visualisation, the GUN samples were lightly post-processed with LATEX.
12While we have exhaustively explored the topic of machine learning GUNs, we leave the more controversial
topic of machine GUN learning to braver researchers.
5


## Page 6


Under review as a conference paper at SIGBOVIK 2017
ACKNOWLEDGEMENTS
The authors would like to acknowledge the quality of Karel Lenc’s homemade pancakes. This work
was supported by the NRA (National Research Association).
REFERENCES
Amari, Shun-ichi and Nagaoka, Hiroshi. Methods of information geometry, volume 191 of transla-
tions of mathematical monographs. American Mathematical Society, pp. 13, 2000.
Arjovsky, Martin, Chintala, Soumith, and Bottou, L´eon.
Wasserstein gan.
arXiv preprint
arXiv:1701.07875, 2017.
Bachman, Philip and Precup, Doina. Variational generative stochastic networks with collaborative
shaping. In ICML, pp. 1964–1972, 2015.
Bengio, Yoshua, Lamblin, Pascal, Popovici, Dan, Larochelle, Hugo, et al. Greedy layer-wise train-
ing of deep networks. Advances in neural information processing systems, 19:153, 2007a.
Bengio, Yoshua, LeCun, Yann, et al. Scaling learning algorithms towards ai. Large-scale kernel
machines, 34(5):1–41, 2007b.
Bengio, Yoshua, Courville, Aaron, and Vincent, Pascal. Representation learning: A review and new
perspectives. IEEE transactions on pattern analysis and machine intelligence, 35(8):1798–1828,
2013a.
Bengio, Yoshua, Yao, Li, Alain, Guillaume, and Vincent, Pascal.
Generalized denoising auto-
encoders as generative models. In Advances in Neural Information Processing Systems, pp. 899–
907, 2013b.
Bengio, Yoshua, Goodfellow, Ian J, and Courville, Aaron. Deep learning. Nature, 521:436–444,
2015.
Bishop, Christopher M. Pattern recognition. Machine Learning, 128:1–58, 2006.
Chen, Xi, Duan, Yan, Houthooft, Rein, Schulman, John, Sutskever, Ilya, and Abbeel, Pieter. Info-
gan: Interpretable representation learning by information maximizing generative adversarial nets.
In Advances in Neural Information Processing Systems, pp. 2172–2180, 2016.
Crawford, Cindy. Shape your body workout, 1992.
Denton, Emily L, Chintala, Soumith, Fergus, Rob, et al. Deep generative image models using a
laplacian pyramid of adversarial networks. In Advances in neural information processing systems,
pp. 1486–1494, 2015.
Fouhey, David F and Maturana, Daniel. The kardashian kernel, 2012.
G¨odel, Kurt. ¨Uber formal unentscheidbare s¨atze der principia mathematica und verwandter systeme
i. Monatshefte f¨ur mathematik und physik, 38(1):173–198, 1931.
Goodfellow, Ian, Pouget-Abadie, Jean, Mirza, Mehdi, Xu, Bing, Warde-Farley, David, Ozair, Sher-
jil, Courville, Aaron, and Bengio, Yoshua. Generative adversarial nets. In Advances in neural
information processing systems, pp. 2672–2680, 2014.
Huang, Xun, Li, Yixuan, Poursaeed, Omid, Hopcroft, John, and Belongie, Serge. Stacked generative
adversarial networks. arXiv preprint arXiv:1612.04357, 2016.
Metz, Luke, Poole, Ben, Pfau, David, and Sohl-Dickstein, Jascha. Unrolled generative adversarial
networks. arXiv preprint arXiv:1611.02163, 2016.
Murphy, Kevin P. Machine learning: a probabilistic perspective. MIT press, 2012.
Postel, Jon et al. Transmission control protocol rfc 793, 1981.
6


## Page 7


Under review as a conference paper at SIGBOVIK 2017
Radford, Alec, Metz, Luke, and Chintala, Soumith. Unsupervised representation learning with deep
convolutional generative adversarial networks. arXiv preprint arXiv:1511.06434, 2015.
Schwarzenegger, Arnold. Arnold: The education of a bodybuilder. Simon and Schuster, 2012.
Twitter. Erik solheim: Cost of violence globally = $1876 for every person in the world. global peace
index here: http://ow.ly/WouI3014Czf, 2016.
Vedaldi, Andrea and Lenc, Karel.
Matconvnet: Convolutional neural networks for matlab.
In
Proceedings of the 23rd ACM international conference on Multimedia, pp. 689–692. ACM, 2015.
AUTHORS’ BIOGRAPHIES
SAMUEL
Samuel started writing biographies at the tender age of 24, when he penned his ﬁrst short story
“Ouch that seriously hurt, keep your **** cat away from me” about the life of Jack Johnson, his
brother’s lovable albino cat with anger management issues. His career as a biographer has gone
from strength to strength ever since, ﬂourishing in several other phyla of the animal kingdom. He is
a noted expert on the much beloved native English Panda and is a self-award winning author on the
challenges of hunting them.
SEBASTIEN
Sebastien holds a self-taught liberal arts degree, and passed his driver’s license exam with highest
honours. Secretly a German national, he then joined the French Foreign Legion and was deployed
Sam– Don’t think that the redacted joke is funny enough to justify the loss of a biography - will
return to this later. Interestingly, this latex package does not redact full stops. Possible gap in the
market here? in Nicaragua, I of like, turtles.
Joao– Fixed it. Actually I quite like this bio, it has a certain mysterious quality to it. I wonder if
there’s a way to hack the PDF and read what’s written underneath. In any case I’m just gonna write
my groceries list here so I can easily access it on my phone when I’m in the shop, hope you don’t
mind.
- Eggs
- Milk
- Ammo
JO ˜AO
Jo˜ao El Tracko F. Henriques holds a joint bachelors degree in guerilla warfare tactics and cakemak-
ing from the University of Coimbra, where he has been tracking down the victims subjects of his
critically acclaimed biographies for over ﬁve years. Little did they know that his visual object track-
ing skills extend to real-life. Though some (all) of his subjects have since passed away, their legend
lives on his thoughtfully written monograph, “How to most effectively interview someone who is
trying desperately to escape from you”.
7

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]