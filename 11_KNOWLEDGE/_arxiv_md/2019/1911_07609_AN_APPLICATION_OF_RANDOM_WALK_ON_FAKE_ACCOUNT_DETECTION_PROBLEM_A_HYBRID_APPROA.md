---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1911.07609
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1911.07609_An_Application_of_Random_Walk_on_Fake_Account_Detection_Problem__A_Hybrid_Approa

> Source: 1911.07609_An_Application_of_Random_Walk_on_Fake_Account_Detection_Problem__A_Hybrid_Approa.pdf

> Pages: 6

---


## Page 1


arXiv:1911.07609v1  [cs.SI]  18 Nov 2019
An Application of Random Walk on Fake Account
Detection Problem: A Hybrid Approach
Ngoc C. Lˆe
School of Applied Mathematics and Informatics
Hanoi University of Science and Technology
Institution of Mathematics
Vietnam Academy of Science and Technology
lechingoc@yahoo.com
Manh-Tuan Dao
iCOMM Media & Tech, Jsc
tuan.dao@icomm.vn
Hoang-Linh Nguyen
School of Applied Mathematics and Informatics
Hanoi Univ of Science and Technology
linh.nh5015@gmail.com
Tuyet-Nhi Nguyen
School of Applied Mathematics and Informatics
Hanoi Univ of Science and Technology
nguyennhiaktf@gmail.com
Hue Vu
School of Applied Mathematics and Informatics
Hanoi Univ of Science and Technology
hue.hnue@gmail.com
Abstract—Social networks play a signiﬁcant role in today’s
world. The importance of social networks, for example Facebook
or Twitter, are undeniable. However, they also have many issues.
One of which is the need for a defense mechanism against
fake accounts. It is obviously not a trivial task to separate
fake accounts from authentic ones. In this paper, we propose
a ranking scheme, comprising of both graph based and feature
based approaches to aid the detection of fake Facebook proﬁles.
Utilizing Support Vector Machine (SVM) [4] and SybilWalk [8],
the model achieved high accuracy over the set of ten thousands
Vietnamese Facebook accounts.
Index Terms—Fake Account, Network Theory, Ramdom Walk,
Support Vector Machine, SVM, SybilWalk
I. INTRODUCTION
The last decade witnessed dramatic growth in size as well
as inﬂuence of online social networks (OSNs) such as Twitter,
LinkedIn and especially Facebook. As of 2018, Facebook has
more than two billions active users. For better or worse, these
sites have had a huge impact not only on social interaction, but
also on education, employment, business, etc. Communication
and information sharing are easier than ever. However, what
follows is a lot of issues with privacy, cyber bullying, social
engineering, online impersonation and so on.
A fake account can be deﬁned as an account which is not
representative of a real person or organization. This is not to be
confused with clones, whose identity is that of an actual person
but possessed by some others for malevolent deeds. Facebook
estimated up to six to ten percents of its user base are either
fake or duplicate accounts in 2017 [7]. However, this number
can greatly ﬂuctuate since there are a lot of new ones being
created everyday and Facebook taking measures to cope with
them. Presumably, fake accounts are still very much elusive
to Facebook security measures, known as Facebook Immune
System (FIS) [3], [16]. The detection of fake accounts remains
a problematic case for Facebook as well as in social network
security research.
Since false positives can heavily damage the experience of
users if actions are taken to suspend accounts assumed non -
genuine right away, the task of ﬁltering out fake accounts has
not been successfully brought to automation. Social networks
providers have had to resort to inefﬁcient and costly manual
labor. For example, Tuenti Technologies employs an inspection
team which must review well over ten thousands reports per
day. However, only about 5% of the reviewed accounts are
indeed fake [2].
In this paper, we present a procedure to help identify fraud-
ulent accounts (human inspections and decision making are
still required). We tried to capture both the characteristics of
fake proﬁles as well as the relationships between these and the
authentic proﬁles. The result is promising over a set of twelve
millions accounts of the test set.
The rest of the paper is organized as following. Section
II introduces the background knowledge and reviews some
of the related works. In Section III, the details about the
proposed model and the features selected for machine learning
modules are given. Results are given in section IV. Section V
gives some perspectives and comments about effectiveness and
limitations of the scheme, as well as future directions.
II. BACKGROUND AND RELATED WORK
A. Background
1) Support Vector Machines (SVM): Support Vector Ma-
chines is a supervised learning method mostly used for clas-
siﬁcation and regression analysis. Given a training dataset
{Xi, Yi}n
i=1, where Xi represents the n-dimensional input vec-
tor and Yi ∈{1, −1} represents the class or label memberships
(also positive and negative samples), a decision hyperplane is
constructed that best separates the two classes in the sense that
it has the largest distance to the nearest training-data point of
any class (also known as functional margin). SVM can perform
both linear as well as non-linear classiﬁcation, with the latter
requires a little more data preprocessing through the so-called
kernel function.


## Page 2


The decision hyperplane obtained from training is deﬁned by
the equation
c⊤x −b = 0
where c ∈Rn, b ∈R. Given a new input vector X, we can,
for example, classify X into label 1 if c⊤X −b < 0 and into
label −1 if c⊤X −b ≥0.
x1
x2
Fig. 1. Example of a linear Support Vector Machine
Let z = c⊤X −b, we can normalize z with the sigmoid
function
S(z) =
1
1 + e−z .
As z approaches positive inﬁnity, S(z) approaches 1. In the
case z approaches negative inﬁnity, S(z) approaches 0. We
can let S(z) represents the possibility that z has label −1,
which is exactly what we are going to do in our detection
scheme.
2) Social network graph: A graph is a discrete structure
used to model objects and pairwise relations between them.
Graph theory is a strong tool when it comes to networks
researches. A graph, G = (V, E), is a pair of vertex set V
edge set E.
For our application, we shall model the social network Face-
book as a graph, in which each node u ∈V represents a user
and each edge e ∈E represents an established relationship
(e.g friendship, commenting in the same posts, ...) between
two nodes. We may also denote an edge by its two end nodes,
i.e uv. The graph is undirected and contains no loop (an edge
connecting a node with itself). The degree of node u is the
number of edges connected to u. adj(u) is the set of nodes
adjacent to u (connected to u by an edge).
The term Sybil which is used widely in graph-based network
Real accounts
Fake accounts
Attack Edge
Fig. 2. The social network graph
security research refers to a forged, pseudonymous identity
in peer-to-peer networks. It was derived from the book of
the same name, a case study of a woman diagnosed with
dissociative identity disorder [13]. Later researches into social
networks impersonation also use this term to refer to a fake
node in the users network graph. An attack edge is an edge
connecting a benign user and a Sybil.
3) Random Walk: A random walk [10] on a graph G can
be described as a succession of nodes u1, u2, ..., uk, where
each node is chosen from the neighbors of the last randomly.
Given that a random walk is long enough, it can land on any
node of the graph with uniform degree-normalized probability
(the probability that the random walk ends up in u divided
by the degree of u is roughly the same for every u). This is
known as the convergence of a random walk to its stationary
distribution. A graph is said to have fast-mixing property if this
convergence happens in a relatively small number of steps. In
our application we shall use a variation of a random walk
algorithm developed in [8].
B. Related work
So far, the approaches for the Sybil accounts detection
problem can be divided in to two groups: (1) Feature-based
approaches using features of accounts and (2) Graph-based
approaches using the relations between accounts.
1) Feature-based approaches: Feature-based (e.g Machine-
Learning based) methods have long been used in OSNs
security. Take spam detection for example, in [12], the authors
ﬁrst proposed a Bayesian approach to ﬁlter spam emails
considering domain-speciﬁc features. Since then, spam mail
ﬁltering techniques has matured over time and achieved high
accuracy. However, it is an entirely different challenge when
moving from the context of email systems to massive net-
works. As evident in [18], automated Machine-Learning-based
fake account detection suffers from high false negative and
positive rates. Much similar to why Machine Learning has
not been effective in network intrusion [15], these approaches


## Page 3


could not fully cover the diverse activities and properties of
intruders, and are subject to overﬁtting. High false positive rate
is particularly harmful to social networks providers, as users
deﬁnitely do not respond well to their account being wrongly
suspended. Besides, there are also issues with scalability,
lacking in ﬂexibility (attackers can easily adapt to avoid traits
recognized by the classiﬁers),... just to name a few reasons
why there has not been a feasible solution.
2) Graph-based approaches: Graph-based Sybil detection
has long been studied in peer-to-peer systems. As stated every
networks can be modeled as a graph G = (V, E). Graph-
based solutions, also called random walk - based solutions,
rely on social graph properties to uncover fake users. Notable
examples include [5], [19], [20].
Presumably, Sybils have a disproportionately small number of
connections to real users. Existing works are largely based
on this assumption [2], [5]. Naturally, graph-based solutions
uncover Sybils from the perspectives of known non-Sybil
nodes. Take SybilInfer [5] for example, a set of traces T are
generated and stored by performing special random walks over
the social graph G. Once the probabilistic model is deﬁned,
calculate for any set of nodes X and the generated trace T , the
probability that X consists of honest nodes. We can calculate
the probability of any node in the system being honest or dis-
honest. SybilGuard [19] and SybilLimit [20] also infer Sybils
based on a large number of random walk traces. SybilRank [2],
widely used in many applications, outputs perceived likelihood
of a node being fake. It relies on the observation that an early-
terminated random walk starting from a non-Sybil node has
a higher degree normalized probability to land at a non-Sybil
node than a Sybil node. From a collection of know benign
users, known as trust seeds, SybilRank then uses short random
walks to assign trust score to other nodes. Unfortunately, the
problem of multi-community structure in social graphs (high
connectivity in each community but low inter-community
connectivity), imposed difﬁculty as non-Sybils that do not
belong to the communities of trust seeds may be mistaken
for Sybils.
Given that a graph has fast-mixing property and homophily
property [9] (two nodes sharing a same edge has high prob-
ability of belonging to the same class), graph-based methods
have guaranteed performance and accuracy [8]. However, these
assumptions do not always hold in the case of real world social
graph. Leveraging only either benign users or Sybils also limits
the potential of these methods.
III. PROPOSED MODEL
The ﬁrst phase of our scheme consists of training a regres-
sion model with SVM from labeled data (accounts that have
been veriﬁed as real or fake). After training, the model is able
to output and assign a normalized score ranging from 0 to 1
to each account, which is a rough estimate of the probability
each account being fake. Then, the social graph is constructed.
From the initial scores obtained from the regression model, we
can better characterize the network to produce more precise
output, rather than just randomly or uniformly assign a number
to each node. A number of iterations of SybilWalk algorithm
is then carried out to calculate the ﬁnal probability score for
each node. A higher score means the node is more likely to
be a Sybil.
A. Features selection for regression model
There are some features that we mimic from [12], [15],
[18]. We have eliminated some by using entropy [14] analysis
and add some more based on the Facebook speciﬁcation.
The ﬁnal chosen features are showed in the following table.
Feature
Justiﬁcation
How long an account
has been active
Fake accounts can be mass pro-
duced and are usually only ac-
tive for a short time.
Number of friends a user
has
Real accounts are expected to
make more friends.
Number of groups a user
has joined
Fake accounts usually join a lot
of groups to post spam.
Number of posts a user
has made
Fake accounts normally do not
bother with writing own posts.
Number of posts on a
user’s wall
Fake accounts normally do not
bother with posts on walls
Number of posts a user
has been tagged in
Real
accounts
have
much
higher chance to be tagged in
other users’ posts.
Number of times a user
has reacted to a post
Fake accounts, especially con-
trolled by a bot are expected to
react to a post much more often
than real accounts.
Number of comments a
user has made
Spam messages can also take
the form of comments, so fake
accounts are likely to make
greater number of comments
than real accounts.
Number
of
likes
all
posts of a user has re-
ceived
Spam messages posted by fake
accounts are unlikely to be
liked by users.
Number of comments on
every posts of a user
Spam messages posted by fake
accounts are unlikely to receive
comments by users.
Number
of
times
a
user’s posts have been
shared
Spam messages posted by fake
accounts are unlikely to be
shared by users.
Number of tags on a
user’s posts (other users
and pages alike).
Real accounts use tags much
more frequently.
Number of users that a
user has tagged in his or
her posts
Real accounts use tags much
more frequently.
Number of pages that a
user has tagged in his or
her posts
Fake accounts may tag more
pages to popularize them.
Number of posts that a
user has shared
Naturally fake accounts has a
much greater share count.


## Page 4


Number of users that a
user has tagged in his or
her comments
Real users have real friends,
therefore
they
tag
and
are
tagged much more frequently.
Number of times a user
has been tagged in other
users’ comments
Real users have real friends,
therefore
they
tag
and
are
tagged much more frequently.
Number of pages that a
user has tagged in his or
her comments
Again, fake accounts may tag
more pages to popularize them.
Extracting and selecting meaningful features from user iden-
tities and activities is a crucial but difﬁcult and time consuming
task. A lot more features may be taken into consideration,
however they may be difﬁcult to extract or completely non-
present due to privacy settings.
B. Building the social graph
Benign Region
Sybil Region
wuv
Attack Edge
lb
ls
Fig. 3. Label-augmented social network
In order to leverage random walks, a model called label-
augmented social network [8] was build. The model consists of
the usual social graph, which can be divided into benign region
(the subgraph induced by benign nodes) and Sybil region (the
subgraph induced by Sybil nodes). Then, two nodes are added
to represent each label. We denote by lb the benign label node
and ls the Sybil label node. lb and ls are connected to every
nodes of their corresponding label (see Fig. 3). Each edge is
given a weight wuv which is the number of mutual friends
between the two nodes, normalized by the maximum number
of mutual friends. As for lb and ls, every edges connected to
them are assigned weight 1. Learning edge weights to better
characterize structural relation between nodes is an interesting
future direction as well.
C. Calculating and assigning probability score to each node
using random walks
Intuitively, if a node is structurally close to known Sybils,
it must have a high probability of being a Sybil itself. We can
theoretically perform any number of random walks starting
from a node u. At each step, the random walks picks a neigh-
bor v of u with probability
wuv
P
t∈adj(u) wut
.The probability
of u being a Sybil, is the probability of this random walk
reaching ls before lb. This makes efﬁcient use of both social
graph structure as well as the ground truth (the known real
and fake nodes). However, in implementation, performing so
many random walks is impractical because the number of
random walks should be sufﬁciently large to approximate the
probability score with high conﬁdent, and there is no real way
to know how many is ”sufﬁciently large” for a particular graph.
In [8], the authors addressed this problem with an algorithm
to compute the score probability of each node via a weighted
combination of neighboring nodes. Suppose u has k neigh-
boring nodes v1, v2, ..., vk with probability score p1, p2, ..., pk
respectively. If from u, the random walk reaches vi with
probability puvi, then it reaches lb via ui with probability
puvipi. By law of total probability, we can calculate the
probability score for u by
p =
k
X
i=1
puvipi
where puvi =
wuvi
P
t∈adj(u) wut
as mentioned before is the
probability a random walk chooses vi as the next step from
u. This is the general idea behind the SybilWalk algorithm.
The convergence of SybilWalk algorithm is only relative.
Algorithm 1 SybilWalk
Input
: Label-augmented, ǫ and T
Output: pu for every u
1: Initialize p(0)
u
for every u
2: Initialize p(0)
lb = 0
3: Initialize p(0)
ls = 1
4: Initialize t = 1
5: while do P
u(p(t)
u −p(t−1)
u
)2 ≥ǫ && t < T
6:
for u in V do
7:
p(t)
u = P
v∈adj(u)
wuv
P
t∈adj(u) wuv
p(t−1)
u
8:
end for
9:
t = t + 1
10: end while
Therefore, it is important to have a good initial guess. This is
why we use SVM to obtain the initial probability scores for
each accounts and reﬁne them using random walk. Our model
of computation can be summarized in diagram 4.
IV. IMPLEMENTATION AND EVALUATION
A. Acquiring and labeling data
The need for fake account analysis arose when we were
looking into Facebook rumors and communication crises. A
rumor breaks out when there are a considerable number of
posts circulating about the same subject, attracting many


## Page 5


Facebook
accounts
SVM
Building the
network graph
SybilWalk
Features
Initial
estimates
Fig. 4. Model of computation
people to comment, like and share. However there may be
malicious seeders who want to direct the rumor’s spreading
to their liking. They will almost always use fake accounts
for this purpose, and it’s crucial to identify these accounts
from genuine ones. We ran a crawler to collect all posts on
Facebook regarding some controversial incidents in 2017 -
2018 in Vietnam. Then, we extracted all the accounts (around
ten thousands) which participated in these posts. Following
that, we proceeded to label the accounts to train and validate
our detection scheme. The information of those accounts were
acquired using Facebook’s User Proﬁle API [17].
B. Evaluation
We ran our model of computation with 5-fold cross valida-
tion. The best result is given in Table I.
Fake accounts
Real accounts
Precision
0.9
0.96
Recall
0.85
0.97
F1
0.87
0.96
TABLE I
Precision, Recall and F1 score for the combined model
The model converged after only over 50 iterations. Compare
this with the result when we use only SVM instead of the
two-phase scheme in Table II
Fake accounts
Real accounts
Precision
0.8
0.92
Recall
0.73
0.95
F1
0.76
0.94
TABLE II
Precision, Recall and F1 score for SVM detection
It is obvious that a better performance has been achieved.
V. CONCLUSION AND PERSPECTIVES
In this work, we have proposed a ranking scheme for the
detection of fake Facebook user accounts which incorporates
both feature-based approaches and graph-based approaches to
overcome their respective limits. Normalized SVM output ﬁrst
give a rough estimate on the probability score, providing a
better initial guess for the SybilWalk algorithm. The compu-
tational cost is moderate and can be scaled and deployed to
handle large data sets. For future work, there are a few aspects
to improve, for example
• Learning edge weights to better represent the relationship
between nodes.
• Evaluate the impacts of features chosen to characterize
fake accounts.
• Real time detection for application.
The
source
code
and
the
data
set
can
be
found
at
https://github.com/nhisnow1996/Facebook-Fake-Account-Detection.
ACKNOWLEDGMENT
The ﬁrst author also has receive the support from Institute of
Mathematics, Vietnam Academy of Science and Technology,
Year 2019. This work is also supported by iCOMM Media &
Tech, Jsc. We would like to thank the iCOMM RnD team for
supported resources and text data that we used during training
and experiments our model.
REFERENCES
[1] L. Bilge, T. Strufe, D. Balzarotti, and E. Kirda, ”All Your Contacts Are
Belong to Us: Automated Identity Theft Attacks on Social Networks”,
In Proceedings of the 18th WWW, pp. 551–560, 2014.
[2] Q. Cao, M. Sirivianos, X. Yang, and T. Pregueiro, ”Aiding the De-
tection of Fake Accounts in Large Scale Social Online Services”, In
USENIX/ACM Symposium on Networked Systems Design and Imple-
mentation (NSDI), 2012.
[3] M. Conti, R. Poovendran, and M. Secchiero, ”Fakebook: Detecting
fake proﬁles in on-line social networks”, In Proceedings of the 2012
International Conference on Advances in Social Networks Analysis and
Mining, pp. 10711078, 2012.
[4] C. Cortes and V. N. Vapnik, ”Support-vector networks”, Machine
Learning, Vol. 20:3, pp. 273-297, 1995.
[5] G. Danezis and P. Mittal, ”SybilInfer: Detecting Sybil Nodes Using
Social Networks”, NDSS, Feb. 2009.
[6] A. Gupta and R. Kaushal, ”Towards Detecting Fake User Accounts on
Facebook”, In Asia Security and Privacy (ISEASP), 2017.
[7] A.
Heath,
”Facebook
quietly
updated
two
key
numbers
about
its
user
base”,
https://www.businessinsider.com/facebook-raises-duplicate-fake-account-estimates-q3-
Accessed: 2018-07-15.
[8] J. Jinyuan, W. Binghui, and Z. G. Neil, ”Random Walk Based Fake
Account Detection in Online Social Networks”, 2017 47th Annual
IEEE/IFIP International Conference on Dependable Systems and Net-
works (DSN), pp.273–284, 2017.
[9] D. A. Levin, Y. Peres, and E. L. Wilmer Markov chains and mixing
times, 2nd Ed., AMS, 2017.
[10] K. Pearson, ”The Problem of the Random Walk”, Nature, 72 (1865):294,
1905.
[11] R.
Richmond,
”Stolen
Facebook
Accounts
for
Sale”,
http://www.nytimes.com/2010/05/03/technology/internet/03facebook.html,
Accessed: 2018-02-21.
[12] M. Sahami, S. Dumais, D. Heckerman, and E. Horvitz, ”A Bayesian
Approach to Filtering Junk E-Mail”, In AAAI Workshop on Learning
for Text Categorization, 1998.
[13] F. R. Schreiber, ”Sybil”, Kirkus Reviews, 1973.
[14] C. E. Shannon, ”A Mathematical Theory of Communication”, Bell
System Technical Journal, Vol. 27:3, pp. 379-423, 1948.
[15] R. Sommer and V. Paxson, ”Outside the Closed World: On Using
Machine Learning for Network Intrusion Detection”, In 2010 IEEE
Symposium on Security and Privacy, USA, May 2010, pp. 305–316,
2010.
[16] T. Stein, E. Chen, and K. Mangla, ”Facebook immune system”, In
Proceedings of the 4th Workshop on Social Network Systems, Vol. 11,
pp. 8–15, 2011.
[17] User Proﬁle API, https://developers.facebook.com/docs/messenger-platform/identity/user
Accessed: 2018-01-30.
[18] Z. Yang, C. Wilson, X. Wang, T. Gao, B. Y. Zhao, and Y. Dai,
”Uncovering Social Network Sybils in the Wild”, IMC ’11 Proceedings
of the 2011 ACM SIGCOMM conference on Internet measurement
conference, Germany, Nov. 2011, pp. 259–268, 2011.


## Page 6


[19] H. Yu, M. Kaminsky, P. B. Gibbons, and A. Flaxman, ”Sybilguard: de-
fending against sybil attacks via social networks”, SIGCOMM Comput.
Commun. Rev, Vol. 36:4, pp.267–278, 2006.
[20] H. Yu, P. B. Gibbons, M. Kaminsky and F. Xiao, ”Sybillimit: A
near-optimal social network defense against sybil attacks”, In IEEE
Symposium on Security and Privacy, pp. 305–317, 2008.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1911_07609_an_application_of_random_walk_on_fake_account_detection_problem_a_hybrid_approa
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1911_07609_AN_APPLICATION_OF_RANDOM_WALK_ON_FAKE_ACCOUNT_DETECTION_PROBLEM_A_HYBRID_APPROA.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
