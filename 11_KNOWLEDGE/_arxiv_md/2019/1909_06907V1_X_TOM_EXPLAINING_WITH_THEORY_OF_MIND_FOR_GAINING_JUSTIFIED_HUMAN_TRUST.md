---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.06907v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1909.06907v1_X-ToM__Explaining_with_Theory-of-Mind_for_Gaining_Justified_Human_Trust

> Source: 1909.06907v1_X-ToM__Explaining_with_Theory-of-Mind_for_Gaining_Justified_Human_Trust.pdf

> Pages: 36

---


## Page 1


X-ToM: Explaining with Theory-of-Mind for Gaining
Justiﬁed Human Trust
Arjun R. Akula1∗†, Changsong Liu1∗†, Sari Saba-Sadiya3∗†, Hongjing Lu1∗†,
Sinisa Todorovic2∗†, Joyce Y. Chai3∗†, Song-Chun Zhu1∗†
1Center for Vision, Cognition, Learning, and Autonomy,
University of California, Los Angeles, CA 90025 USA
2Oregon State University, Corvallis, OR 97331 USA
3Michigan State University, East Lansing, MI 48824 USA
Abstract
We present a new explainable AI (XAI) framework aimed at increasing justiﬁed human
trust and reliance in the AI machine through explanations. We pose explanation as an
iterative communication process, i.e. dialog, between the machine and human user.
More concretely, the machine generates sequence of explanations in a dialog which
takes into account three important aspects at each dialog turn: (a) human’s intention
(or curiosity); (b) human’s understanding of the machine; and (c) machine’s under-
standing of the human user. To do this, we use Theory of Mind (ToM) which helps
us in explicitly modeling human’s intention, machine’s mind as inferred by the human
as well as human’s mind as inferred by the machine. In other words, these explicit
mental representations in ToM are incorporated to learn an optimal explanation policy
that takes into account human’s perception and beliefs. Furthermore, we also show
that ToM facilitates in quantitatively measuring justiﬁed human trust in the machine by
comparing all the three mental representations.
We applied our framework to three visual recognition tasks, namely, image classi-
ﬁcation, action recognition, and human body pose estimation. We argue that our ToM
based explanations are practical and more natural for both expert and non-expert users
∗Corresponding Author
†Email Addresses: aakual@ucla.edu (A.Akula), liucs.msu@gmail.com (C. Liu), sadiyasa@cse.msu.edu
(S. Sadiya), hongjing@ucla.edu (H. Lu), sinisa@oregonstate.edu (S. Todorovic), jchai@cse.msu.edu (J.Y.
Chai), sczhu@stat.ucla.edu (S.C. Zhu)
Preprint submitted to
(under review)
September 17, 2019
arXiv:1909.06907v1  [cs.AI]  15 Sep 2019


## Page 2


to understand the internal workings of complex machine learning models. To the best
of our knowledge, this is the ﬁrst work to derive explanations using ToM. Extensive hu-
man study experiments verify our hypotheses, showing that the proposed explanations
signiﬁcantly outperform the state-of-the-art XAI methods in terms of all the standard
quantitative and qualitative XAI evaluation metrics including human trust, reliance,
and explanation satisfaction.
Keywords: Explainable Artiﬁcial Intelligence, Theory of Mind, Interpretability.
1. Introduction
1.1. Motivation and Objective
From low risk environments such as movie recommendation systems and chatbots
to high risk environments such as self-driving cars, drones, military applications and
medical-diagnosis and treatment, Artiﬁcial Intelligence (AI) systems are becoming in-
creasingly ubiquitous [1, 2, 3, 4]. AI is ﬁnding its way into a wide array of applications
in education, ﬁnance, healthcare, telecommunication, and law enforcement. In partic-
ular, AI systems built using black box machine learning (ML) models – such as deep
neural networks and large ensembles [5, 6, 7, 8, 9, 10, 11, 12, 13] – perform remark-
ably well on a broad range of tasks and are gaining widespread adoption. However
understanding the behavior of these systems remains a signiﬁcant challenge as they
cannot explain why they reached a speciﬁc recommendation or a decision. This is
especially problematic in high risk environments such as banking, healthcare, and in-
surance, where AI decisions can have signiﬁcant consequences. Therefore, much hope
rests on explanation methods as tools to understand the decisions made by these AI
systems.
Explainable AI (XAI) models, through explanations, make the underlying infer-
ence mechanism of AI systems transparent and interpretable to expert users (system
developers) and non-expert users (end-users) [5, 6, 7, 14]. Explanations play a key role
in integrating AI machines into our daily lives, i.e. XAI is essential to increase social
acceptance of AI machines. As the decision making is being shifted from humans to
machines, transparency and interpretability achieved with reliable explanations is
2


## Page 3


central to solving AI problems such as Safety (e.g. how to operate self-driving cars
safely), Bias & Fairness (e.g. how to detect and mitigate bias in ML models), Justiﬁed
Human Trust in ML models (e.g. how to trust the output of these AI systems to inform
our decisions), Model Debugging (e.g. how to improve my model by identifying points
of model failure), and Ethics (e.g. how to ensure that ML models reﬂect our values)
(Figure 1).
Figure 1: An AI machine that explains its predictions to human users will ﬁnd more social acceptance.
Therefore, XAI models are the key in addressing the issues such as Safety in AI, Bias/Fairness in AI, Trust
in AI, Model Debugging, and Ethics in AI.
In this work, we focus mainly on measuring and increasing Justiﬁed Positive Trust
(JPT) and Justiﬁed Negative Trust (JNT) [15] in AI systems. We measure JPT and
JNT by evaluating the humans understanding of the machines (M) decision-making
process. For example, let us consider an image classiﬁcation task. Suppose if the
machine M predicts images in the set C correctly and makes incorrect decisions on the
images in the set W. Intuitively, JPT will be computed as the percentage of images in
C that the human subject felt M would correctly predict. Similarly, JNT (also called as
mistrust), will be computed as the percentage of images in W that the human subject
felt M would fail to predict correctly. Note that this deﬁnition of justiﬁed positive and
negative trust is domain generic and can be applied to any task. For example, in an
AI-driven clinical world, our deﬁnitions of JPT and JNT can effectively measure how
3


## Page 4


much doctors and patients understand the AI systems that assist in clinical decisions.
1.2. Introducing X-ToM: Explaining with Theory-of-Mind for Increasing JPT and JNT
Our work is motivated by the following three key observations:
1. Attention is not a Good Explanation: Previous studies have shown that trust
is closely and positively correlated to the level of how much human users un-
derstand the AI system — understandability — and how accurately they can
predict the system’s performance on a given task — predictability [14, 5, 15, 7].
Therefore there has been a growing interest in developing explainable AI sys-
tems (XAI) aimed at increasing understandability and predictability by provid-
ing explanations about the system’s predictions to human users [5, 6, 7, 8]. Cur-
rent works on XAI generate explanations about their performance in terms of,
e.g., feature visualization and attention maps [9, 10, 11, 12, 13, 16]. However,
solely generating explanations, regardless of their type (visualization or atten-
tion maps) and utility, is not sufﬁcient for increasing understandability and pre-
dictability [17]. We verify this in our experiments (see Section 4).
2. Explanation is an Interactive Communication Process: We believe that an
effective explanation cannot be one shot and involves iterative process of com-
munication between the human and the machine. The context of such interac-
tion plays an important role in determining the utility of the follow-up explana-
tions [18]. As humans can easily be overwhelmed with too many or too detailed
explanations, interactive communication process helps in understanding the user
and identify user-speciﬁc content for explanation. Moreover, cognitive stud-
ies [7] have shown an explanation can only be optimal if it is generated by taking
user’s perception and belief into account.
3. Deﬁning a Collaborative Task for the Communication Process: In our ex-
periments, we found that it is difﬁcult to evaluate the effectiveness of explana-
tions without constraining the communication process. In our framework, we
constrain the communication by explicitly deﬁning a collaborative task for the
human user to solve through the explanations. Based on how many tasks that are
4


## Page 5


Figure 2: XAI as Collaborative Task Solving: Our interactive and collaborative XAI framework based on
the Theory of Mind. The interaction is conducted through a dialog where the user poses questions about
facts in the environment (W-QA) and explanation seeking questions (E-QA).
successfully solved by the user (and the number of explanations in the dialog),
we measure the effectiveness of the explanations.
1.2.1. X-ToM Framework
Based on the above three key observations, we introduce an interactive explanation
framework, X-ToM. In our framework, the machine generates sequence of explana-
tions in a dialog which takes into account three important aspects at each dialog turn:
(a) human’s intention (or curiosity); (b) human’s understanding of the machine; and (c)
machine’s understanding of the human user. To do this, we use Theory of Mind (ToM)
which helps us in explicitly modeling human’s intention, machine’s mind as inferred
by the human as well as human’s mind as inferred by the machine. The ability to reason
about other’s perception and beliefs, in addition to one’s own perception and beliefs, is
often referred to as the Theory-of-Mind [19, 20, 21].
More speciﬁcally, in X-ToM, the machine and the user are positioned to solve a
collaborative task, but the machine’s mind (M) and the human user’s mind (U) only
have a partial knowledge of the environment (see Figure ref2). Hence, the machine
5


## Page 6


and user need to communicate with each other, using their partial knowledge, other-
wise they would not be able to optimally solve the collaborative task. The communica-
tion consists of two different types of question-answer (QA) exchanges — namely, a)
Factoid question-answers about the environment (W-QA), where the user asks “WH”-
questions that begin with what, which, where, and how; and b) Explanation seeking
question-answers (E-QA), where the user asks questions that begin with why about the
machine’s inference. At each turn in the collaborative dialog, our X-ToM updates a
model of human perception and beliefs, and uses this model for optimizing explana-
tions in the next turn.
We argue that our interactive explanation framework based on ToM is practical and
more natural for both expert and non-expert users to understand the internal workings
of complex machine learning models. Furthermore, we also show that ToM facilitates
in quantitatively measuring justiﬁed human trust in the machine by comparing all the
three mental representations. To the best of our knowledge, this is the ﬁrst work to
derive explanations using ToM.
We applied our framework to three visual recognition tasks, namely, image classiﬁ-
cation, action recognition, and human body pose estimation. Using Amazon Mechan-
ical Turk, we have collected explanation dialogs by interacting with turkers through
X-ToM framework. From there, X-ToM learned an optimal explanation policy that
takes into account user perception and beliefs. Through our extensive human studies,
we show that X-ToM allows the user to achieve a high success rate in visual recogni-
tion on blurred images, and does so very efﬁciently in a few dialog exchanges. We also
found that the most popularly used attribution based explanations (viz. saliency maps)
are not effective to improve human trust in AI system, whereas our Theory-of-Mind
inspired approach signiﬁcantly improves human trust in AI by providing effective ex-
planations.
1.3. Related Work
Generating explanations or justiﬁcations of predictions or decisions made by an AI
system has been widely explored in AI. Most prior work has focused on generating
explanations using feature visualization and attribution.
6


## Page 7


Feature visualization techniques typically identify qualitative interpretations of
features used for making predictions or decisions. Recently, there has been an increased
interest in developing feature visualizations for deep learning models, especially for
Convolutional Neural Nets (CNNs) in computer vision applications, and Recurrent
Neural Nets (RNNs) in NLP applications. For example, gradient ascent optimization
is used in the image space to visualize the hidden feature layers of unsupervised deep
architectures [22]. Also, convolutional layers are visualized by reconstructing the in-
put of each layer from its output [11]. Recent visual explanation models seek to jointly
classify the image and explain why the predicted class label is appropriate for the im-
age [23]. Other related work includes a visualization-based explanation framework for
Naive Bayes classiﬁers [24], an interpretable character-level language models for an-
alyzing the predictions in RNNs [25], and an interactive visualization for facilitating
analysis of RNN hidden states [26].
Attribution is a set of techniques that highlight pixels of the input image (saliency
maps) that most caused the output classiﬁcation. Gradient-based visualization meth-
ods [27, 28] have been proposed to extract image regions responsible for the network
output. The LIME method proposed by [6] explains predictions of any classiﬁer by ap-
proximating it locally with an interpretable model. Inﬂuence measures [29] have been
used to identify the importance of features in affecting the classiﬁcation outcome for
individual data points.
More recently, apart from feature visualization and attribution techniques, other
important lines of research in explainable AI explore dimensionality reduction tech-
niques [30, 31] and focus on building models which are intrinsically interpretable [32,
33]. There are few recent works in the XAI literature that go beyond the pixel-level
explanations. For example, the TCAV technique proposed by [34] aims to generate
explanations based on high-level user deﬁned concepts. Contrastive explanations are
proposed by [35] to identify minimal and sufﬁcient features to justify the classiﬁcation
result. [36] proposed counterfactual visual explanations that identify how the input
could change such that the underlying vision system would make a different decision.
More recently, few methods have been developed for building models which are in-
trinsically interpretable [32]. In addition, there are several works [7, 37, 38] on the
7


## Page 8


goodness measures of explanation which aim to understand the underlying character-
istics of explanations.
1.4. Contributions
The contributions of this work are threefold: (i) a new interactive XAI framework
based on the Theory-of-Mind; (ii) a new collaborative task-solving game in the domain
of visual recognition for learning collaborative explanation strategies; and (iii) a new
objective measure of trust and quantitative evaluation of how humans gain increased
trust in a given vision system.
2. X-ToM Framework
Our X-ToM consists of three main components:
• A Performer that generates image interpretations (i.e., machine’s mind repre-
sented as pgM) using a set of computer vision algorithms;
• An Explainer that generates maximum utility explanations in a dialog with the
user by accounting for pgM and pgUinM using reinforcement learning;
• An Evaluator that quantitatively evaluates the effect of explanations on the hu-
man’s understanding of the machine’s behaviors (i.e., pgMinU) and measures
human trust by comparing pgMinU and pgM.
2.1. X-ToM Game
An X-ToM game consists of two phases. The ﬁrst phase is the collaborative task
phase. The user is shown a blurred image and given a task to recognize what the image
shows. X-ToM has access to the original (unblurred) image and the machine’s (i.e.
Performer’s) inference result pgM (see Section 2.2). The user is allowed to ask ques-
tions regarding objects and parts in the image that the user ﬁnds relevant for his/her
own recognition task. Using the detected objects and parts in pgM, X-ToM Explainer
provides visual explanations to the user, as shown in Figure 3. This process allows the
machine to infer what the user sees and iteratively update pgUinM, and thus select an
8


## Page 9


Figure 3: An example of the ﬁrst phase of an X-ToM game aimed at estimating pgUinM: The user is shown
a blurred image and given a task to recognize if the person in the image is running or walking. X-ToM has
access to the original (unblurred) image and pgM. The user then asks questions regarding objects and parts
in the image. Using the detections in pgM, X-ToM provides visual explanations as “bubbles” that reveal the
corresponding image parts in the blurred image. The generated explanations are used to update pgUinM.
optimal explanation at every turn of the game (see Section 2.3). Optimal explanations
generated by the Explainer are the key to maximize the human trust in the machine.
The second phase is speciﬁcally designed for evaluating whether the explanation pro-
vided in the ﬁrst phase helps the user understand the system behaviors. The Evaluator
shows a set of original (unblurred) images to the user that are similar to (but different
from) the ones used in the ﬁrst phase of the game (i.e., the set of images shows the
same class of objects or human activity). The user is then given a task to predict in
each image the locations of objects and parts that would be detected by the machine
(i.e., in pgM) according to his/her understanding of the machine’s behaviors. Based on
the human predictions, the Evaluator estimates pgMinU and quantiﬁes human trust in
the machine by comparing pgMinU and pgM (see Section 2.4).
9


## Page 10


2.2. X-ToM Performer (for Image Interpretation)
In this paper, the visual tasks involve detecting and localizing human body parts,
identifying their poses and attributes, and recognizing human actions from a given
image. The AOG for this visual domain uses AND nodes to represent decompositions
of human body parts into subparts, and OR nodes for alternative decompositions. Each
node is characterized by attributes that pertain to the corresponding human body part,
including the pose and action of the entire body. Also, edges in the AOG capture
hierarchical and contextual relationships of the human body parts.
Our AOG-based performer uses three inference processes α, β and γ at each node.
Figure 3 shows an example part of the AOG relevant for human body pose estima-
tion [39]. The α process detects nodes (i.e., human body parts) of the AOG directly
based on image features, without taking advantage of the surrounding context. The β
process infers nodes of the AOG by binding the previously detected children nodes in a
bottom-up fashion, where the children nodes have been detected by the α process (e.g.,
detecting human’s upper body from the detected right arm, torso, and left arm). Note
that the β process is robust to partial object occlusions as it can infer an object from its
detected parts. The γ process infers a node of the AOG top-down from its previously
detected parent nodes, where the parents have been detected by the α process (e.g.,
detecting human’s right leg from the detected outline of the lower body). The parent
node passes contextual information so that the performer can detect the presence of an
object or part from its surround. Note that the γ process is robust to variations in scale
at which objects appear in images.
2.3. X-ToM Explainer (for Explanation Generation)
The explainer, in the ﬁrst phase of the game, makes the underlying α, β, and γ in-
ference process of the performer more transparent to the human through a collaborative
dialog. At one end, the explainer is provided access to an image and the performer’s
inference result pgM on that image. At the other end, the human is presented a blurred
version of the same image, and asked to recognize a body part, or pose, or human
action depicted (e.g., whether the person is running or walking). To solve the task,
the human may ask the explainer various “what”, “where” and “how” questions (e.g.,
10


## Page 11


Figure 4: Illustration of the ﬁrst phase in X-ToM game. The human is asked to solve the task “Is the person
in the image walking or running?”. The human may ask questions related to body parts and body poses.
The machine reveals a bubble (of various sizes and scales) for each of those questions. The ﬁgure shows
examples of explanations generated using α, β and γ processes and the updated inferred user’s mind after
each explanation.
“Where is the left arm in the image”). We make the assumption that the human will
always ask questions that are related to the task at hand so as to solve it efﬁciently. The
explainer answers these questions using pgM and justiﬁes the answers by showing the
corresponding visual explanations in the image (as illustrated in Figure 4).
11


## Page 12


As visual explanations, we use “bubbles” [40], where each bubble reveals a circular
part of the blurred image to the human. The bubbles coincide with relevant image parts
for answering the question from the human, as inferred by the performer in pgM. For
example, a bubble may unblur the person’s left leg in the blurred image, since that
image part has been estimated in pgM as relevant for recognizing the human action
“running” occurring in the image.
Following the “principle of least collaborative effort” [41] and the aforementioned
ﬁndings [7] that explanations should not overwhelm the human, our X-ToM explainer
utilizes pgM and pgUinM (i.e., the contextual and hierarchical relationships explicitly
modeled in the AOG) for controlling the depth and breadth of explanations. To enable
this control, each bubble is characterized by a number of parameters, including the
amount of image reveal (i.e., the unblurring level), size, and location in the image, to
name a few. We use reinforcement learning to train the explainer to optimize these
parameters and thus provide optimal visual explanations.
2.4. X-ToM Evaluator (for Trust Estimation)
The second phase of the X-ToM game serves to assess the effect of the explainer
on the human’s understanding of the performer. This assessment is conducted by the
evaluator. The human is presented with a set of (unblurred) images that are different
from those used in the ﬁrst phase. For every image, the evaluator asks the human to
predict the performer’s output. The evaluator poses multiple-choice questions and the
user clicks on one or more answers (see Appendix 5.2 for more details on evaluator
interface and questions). As shown in Figure 5, we design these questions to capture
different aspects of human’s understanding of α, β and γ inference processes in the
performer. Based on responses from the human, the evaluator estimates pgMinU. By
comparing pgMinU with the actual machine’s mind pgM (generated by the performer),
we have deﬁned the following qualitative and quantitative metrics to quantitatively
assess human trust [14, 42, 15, 43] in the performer:
Quantitative Metrics:
(1) Justiﬁed Positive and Negative Trust: It is possible for humans to feel positive
trust with respect to certain tasks, while feeling negative trust (i.e. mistrust) on some
12


## Page 13


Figure 5: An example of second phase of X-ToM game where we estimate pgMinU and also quantitatively
compute justiﬁed trust.
other tasks. The positive and negative trust can be a mixture of justiﬁed and unjustiﬁed
trust [14, 15]. We compute justiﬁed positive trust (JPT) and negative trust (JNT) as
follows:
JPT = 1
N
X
i
X
z=α,β,γ
∆JPT(i, z),
∆JPT(i, z) = ∥pgMinU
i,z,+ ∩pgM
i,+∥
∥pgM
i,+∥
,
JNT = 1
N
X
i
X
z=α,β,γ
∆JNT(i, z),
∆JNT(i, z) = ∥pgMinU
i,z,−∩pgM
i,−∥
∥pgM
i,−∥
,
13


## Page 14


where N is the total number of games played. z is the type of inference process.
∆JPT(i, z), ∆JNT(i, z) denote the justiﬁed positive and negative trust gained in the
i-th turn of a game on the z inference process respectively. pgMinU
i,z,+
denotes nodes in
pgMinU
i
for which the user thinks the performer is able to accurately detect in the image
using the z inference process. Similarly, pgMinU
i,z,−denotes nodes in pgMinU
i
for which
the user thinks the performer would fail to detect in the image using the z inference
process. ∥pg∥is the size of pg. Symbol ∩denote the graph intersection of all nodes
and edges from two pg’s.
(2) Reliance: Reliance (Rc) captures the extent to which a human can accurately
predict the performer’s inference results without over- or under-estimation. In other
words, Reliance is proportional to the sum of JPT and JNT.
Rc = 1
N
X
i
X
z=α,β,γ
∆Rc(i, z),
∆Rc(i, z) = ∥pgMinU
i,z
∩pgM
i,z∥
∥pgM
i ∥
.
Qualitative Metrics:
(3) Explanation Satisfaction (ES). We measure users feeling of satisfaction at having
achieved an understanding of the machine in terms of usefulness, sufﬁciency, appro-
priated detail, conﬁdence, accuracy, and consistency. We ask them to rate each of these
metrics on a Likert scale of 0 to 9.
3. Learning X-ToM Explainer Policy
Given the following input: image I, task T assigned to the human, dialog history
hi of a sequence of generated bubbles, and question from the user qi selected from
a ﬁnite set of allowed questions Q(T) for task T, the explainer estimates an optimal
explanation ei at dialog turn i as
ei = arg max
e
U
 e | pgM, pgUinM
i
, qi, hi, T, I; θ

14


## Page 15


Figure 6:
Left: The Machine interprets the image I as PgM; Middle: Hierarchical representation of
the bubble using the four parameters: explanation content (bcnt), explanation attention (bact), explanation
acts (batt) and explanation discourse (batt); Right: The Human receives visual explanations – bubbles –
optimized by the X-ToM Explainer.
where U denotes the utility function parameterized by θ. The set of questions
Q(T) is automatically generated from all concepts (objects, object parts, human activ-
ities, object attributes, etc.) that may appear in the image and are also modeled by the
Performer. During interaction, the user is prompted to ask a question from this list1.
As deﬁned earlier, pgUinM
i
denotes the current estimate of human’s mind, which
is an empty graph without nodes and edges at the beginning of the X-ToM game. At
every turn in the dialog, the explainer infers and updates pgUinM
i
by maximizing its
posterior distribution based on hi, T and qi. Using a Bayesian approach, we deﬁne the
posterior of pgUinM
i
as
p
 pgUinM
i
| hi, qi, T

∝
p
 qi | hi, pgUinM
i
, T

p
 hi | pgUinM
i
, T

p
 pgUinM
i
, T

1A NLU component can be added to map users’ free-form natural language questions to the list of
interpretable questions.
15


## Page 16


where p
 pgUinM
i
, T

is speciﬁed as a uniform prior. The likelihoods p
 qi | hi, , pgUinM
i
, T

and p
 hi | pgUinM
i
, T

are estimated based on the frequency of occurrence of the ques-
tion q = qi and the dialog history h = hi over many X-ToM games played with human
users. After updating pgUinM
i
, the selection of an optimal bubble, i.e., explanation
ei, is cast as a sequential decision-making problem and formalized using reinforce-
ment learning (RL). Below we specify the state, actions, reward, and policy of the RL
framework.
RL State (si). The state of the explainer at dialog turn i consists of pgM, pgUinM
i
, qi,
and hi.
RL Action (ai). The action space consists of all possible bubbles that can be generated
from pgM so that they reveal relevant image parts in the blurred image to the human.
Each bubble b is characterized by the following four groups of parameters, as illus-
trated in Figure 6:
(a) Explanation Content, bcnt, is deﬁned as the amount of visual information con-
tained in the bubble. Our X-ToM uses the Gaussian scale-space [44] for measuring
bcnt. Speciﬁcally, we model “space” as a Gaussian with variance σ2
1 governing the
length of the radius (i.e., spatial size) of the bubble. Also, we model “scale” as a Gaus-
sian with variance σ2
2 governing the amount of image unblur that the bubble reveals to
the user. Given σ2
1 and σ2
2, we compute bcnt
i
as the differential entropy
bcnt = 1 + 1
2 log(4π2σ2
1σ2
2)
Intuitively, a bubble with large “space” (i.e., large size) and large “scale” (i.e.,
high resolution) reveals a lot of information about the image. Conversely, a bubble
with small “space” and “scale” reveals very little evidence. If the explainer always
chose bubbles with small “space” and “scale”, it would lead to inefﬁcient dialogue for
solving the task. On the other hand, if the explainer always chose bubbles with large
space and scale, it would distract the human with unnecessary information and make
it difﬁcult for the human to understand the machine’s internal representation and in-
ference2. Thus, the explainer’s goal is to ﬁnd the bubble with an optimal bcnt. In this
2For example, showing a very large bubble for revealing Left-Wrist will also reveal Left-Elbow to the
16


## Page 17


paper, we discretize “space” and “scale” of bubbles using σ1 ∈{1.15, 3.15, 4.5}, and
σ2 ∈{1, 9, 15}.
(b) Explanation Acts, bact, parametrizes the three types of visual explanations (i.e.,
bubbles) that can be presented to the human, corresponding to the three inference pro-
cesses in our AOG-based performer. Speciﬁcally, bact can be: α, β, or γ explanation
act. Note that using β and γ explanation acts (i.e., bottom-up and top-down inference
processes of the performer) allows for increasing depth of explanations.
(c) Explanation Attention, batt, indexes a particular human body part from pgM that
is the current focus of the dialog with the human. In the paper, the AOG explicitly
models human body parts and their subparts, where pgM infers only a subset of those
appearing in the image.
(d) Explanation Discourse, bdis, parametrizes discourse relations of the bubbles gen-
erated along the dialog with the human. In this paper, we account for the dialog dis-
course for enforcing coherence among the explanations. In our experiments, we found
the following ﬁve discourse relations [45, 41] to be sufﬁcient and helpful:
1. Elaboration.
If bubble bi+1 provides additional details (e.g., by increasing
“scale” or “space”) relative to the previous bubbles hi = b1...i, then bi+1 re-
lates to the dialog history hi with the elaboration relationship.
2. Sequence. If the explanation attention batt of bubble bi+1 is not part of the
dialog history hi, then bi+1 relates to hi with the sequence relationship.
3. Recurrence. If bubble bi+1 already exists in hi, then the discourse relationship
between bi+1 and hi is called recurrence.
4. Restatement. If the dialog history hi already contains a bubble with the same
explanation attention batt as bi+1, then bi+1 relates to hi with the restatement
human. This makes it harder for human to understand whether the machine is capable of detecting the exact
location of Left-Wrist in the image. In addition, although larger bubbles can potentially minimize the number
of turns, they transmit a large amount of information from machine to human. This effect may not be obvious
in the current experimental set up, but will be signiﬁcant in the situation where information to be transmitted
is through text. Larger bubbles will correspond to longer textual descriptions.
17


## Page 18


relationship.
5. Summary is a special case of the elaboration relationship. If an attention node
of pgM has been already explained in the dialog history hi, and bi+1 has the
same explanation attention but corresponds to a lower resolution and larger size
bubble than the one in hi, then bi+1 relates to hi with the summary relationship.
RL Reward (ri) Our reward function aims to maximize the success rate (ss), user
conﬁdence (cf), user satisfaction (sf) and minimize the cost (Ci) over the total number
of bubbles. We estimate the cost of generating bubbles b1,b2,...,bi as
Ci =
i
X
j=1
1
bcnt
j
RL Reward (ri) is expressed in terms of a user feedback and cost associated with
selecting the bubbles. At each dialog turn i, after choosing bi, the explainer collects
the following feedback from the user:
1. Success (ssi): The user is asked to solve the task based on {bi, hi}. The user’s
success indicates that the machine’s dialog with the user had a high utility and
the explanations made by the machine make sense and can help the user reach
an understanding of the image. Therefore, if the user solves the task correctly,
the explainer is rewarded with ssi = 1; otherwise, ssi = -1.
2. User conﬁdence (cfi): It is possible that user might solve the task by chance
without really understanding the task. We therefore additionally ask the user to
report their conﬁdence in solving the task on a scale of 1 to 5.
3. User satisfaction (sfi): We ask the user to rate the ordering of bubbles generated
in the dialog, and their relevance for solving the task on a scale of 1 to 5.
To compute ri, we also estimate the cost function Ci of generating bubbles b1,b2,...,bi,
deﬁned as
Ci =
i
X
j=1
1
bcnt
j
,
(1)
18


## Page 19


where bcnt is computed as follows:
bcnt = 1 + 1
2 log(4π2σ2
1σ2
2).
(2)
Intuitively, a large Ci indicates that explanation content of the bubbles revealed is
high.
Our reward function aims to maximize the success rate (ss), user conﬁdence (cf),
user satisfaction (sf) and minimize the cost (Ci) over the total number of bubbles. We
estimate the cost of generating bubbles b1,b2,...,bi as
ri = 1
i exp(ssi cfi sfi
Ci
).
(3)
RL Policy and Training. The explainer operates under a stochastic policy, π (ai|si; θ),
which samples optimal bubbles conditioned on the state. This policy is learned by
a standard recurrent neural network, called Long-Short Term Memory (LSTM) [46].
In this paper we use a 2-layer LSTM parameterized by θ. Input to the LSTM is a
feature vector representing the state si – speciﬁcally, a binary indicator vector of the
AOG nodes and edges present in pgM and pgUinM
i
, as well as indices of the ques-
tion qi and bubbles generated in hi. The LSTM’s output is the predicted quadruple
(bcnt, bact, batt, bdis) of bi+1. Thus, the goal of the policy learning is to estimate the
LSTM parameters θ.
We use actor-critic with experience replay for policy optimization [47]. The train-
ing objective is to ﬁnd π (ai|si; θ) that maximizes the expected reward J(θ) over all
possible bubble sequences given a starting state. The gradient of the objective function
has the following form:
∇θJ(θ) = E[∇θ log πθ (ai|si; θ) A (si, ai)]
(4)
where A (si, ai) = Q (si, ai) −V (si) is the advantage function [48]. Q (si, ai)
is the standard Q-function, and V (si) is the baseline function aimed at reducing the
variance of the estimated gradient. We use the same speciﬁcations of Q (si, ai) and
V (si) as in [48]. As in [48], we sample the dialog experiences randomly from the
replay pool for training.
19


## Page 20


4. Experiments
We deployed the X-ToM game on the Amazon Mechanical Turk (AMT) and trained
the X-ToM Explainer through the interactions with turkers. All the turkers have a
bachelors degree or higher. We used three visual recognition tasks in our experiments,
namely, human body parts identiﬁcation, pose estimation, and action identiﬁcation. We
used 1000 images randomly selected from Extended Leeds Sports (LSP) dataset [49].
Each image is used in all the three tasks. During training, each trial consists of one
X-ToM game where a turker solves a given task on a given image. We restrict Turkers
from solving a task on an image more than once. In total, about 2400 unique workers
contributed in our experiments.
We performed off-policy updates after every 200 trials, using Adam optimizer [50]
with a learning rate of 0.001 and gradients were clipped at [-5.0, 5.0] to avoid explo-
sion. We used ϵ-greedy policy, which was annealed from 0.6 to 0.0. We stopped the
training once the model converged. In our case, the X-ToM policy model converged
after interacting with 3500 turkers. All our data and code will be made publicly avail-
able.
Elaboration
Sequence
Recurrence
Restatement
Summary
26%
48.7%
12.6%
5.1%
7.6%
Table 1: Distribution of observed discourse relations in the test trials
The trained X-ToM Explainer was applied to an additional 500 X-ToM games with
AMT turkers for testing. Table 1 shows the percentage of discourse relations among
bubbles found in the test interactions. As can be seen, the discourse relation sequence
dominates other relations. This indicates that the X-ToM’s most common explanation
strategy is to prefer a bubble containing new evidence (that was not already shown to
the user). Furthermore, the experiment has shown that 55.3% of the bubbles in the
test trials were generated using α explanation act, 23.1% using β explanation act, and
21.6% using γ explanation act. The high percentage of β and γ explanation acts indi-
20


## Page 21


cate that contextual evidence is not only helpful for the performer to detect but also for
the explainer to explain.
4.1. AMT Evaluation of X-ToM Explainer
We conducted an ablation study to quantify the importance of taking the inferred
human’s mind into account for generating optimal explanations, i.e., the ablated model
does not explicitly represent and infer pgUinM. Similar to X-ToM, the ablated model
was also deployed and trained on AMT. The trained ablated model was again applied
to an additional 500 X-ToM games with AMT turkers for testing. Table 2 compares X-
ToM Explainer with the ablated model in terms of objective measures such as average
success rate (ss), average number of bubbles, average rewards (r). X-ToM Explainer
signiﬁcantly outperforms the ablated model (p < 0.01) in terms of the overall reward.
Although the success rates of both models are similar, the ablated model is found to
use a signiﬁcantly larger number of bubbles, which leads to lower overall reward.
Model
#test trials
ss
#bubbles
r
X-ToM
500
81.3%
10.5
0.91
Ablated Model
500
77.1%
28
0.42
Human Strategy
100
78.9%
6
0.62
Table 2: Comparison of X-ToM with ablated and human baselines
Using an additional 100 X-ToM games on AMT, we further compare the explana-
tions generated by our X-ToM Explainer with the explanations annotated by humans.
We asked three graduate students (not the authors), to select the most appropriate bub-
bles for a given task. Bubbles that have been agreed upon by these three subjects were
taken as the best explanations for the given task and image. In terms of maximizing the
reward, we found that X-ToM Explainer performed signiﬁcantly better than the human
strategy of bubble selection (p < 0.01). However, we found that the average dialog
length in the human explanations is 6, while the average dialogue length observed in
the X-ToM explanations is 10.5, indicating that there is a possibility to further improve
the quality of the X-ToM explanations. We leave this for future exploration.
21


## Page 22


4.2. Human Subject Evaluation on Justiﬁed Trust
Using X-ToM Evaluator, we conduct human subject experiments to assess the ef-
fectiveness of the X-ToM Explainer, that is trained on AMT, in increasing human trust
through explanations. We recruited 120 human subjects from our institution’s Psy-
chology subject pool 3. These subjects have no background on computer vision, deep
learning and NLP (see Appendix 5.1 for more details). We applied between-subject
design and randomly assigned each subject into one of the three groups. One group
used X-ToM Explainer, and two groups used the following two baselines respectively:
• ΩQA: we measure the gains in human trust only by revealing the answers for the
tasks without providing any explanations to the human.
• ΩSalience: in addition to the answers, we also provide saliency maps generated
using attribution techniques to the human as explanations [27, 28].
Within each group, each subject will ﬁrst go through an introduction phase where
we introduce the tasks to the subjects. Next, they will go through familiarization phase
where the subjects become familiar with the machine’s underlying inference process
(Performer), followed by a testing phase where we apply our trust metrics and assess
their trust in the underlying Performer.
Figure 7 compares the justiﬁed positive trust (JPT), justiﬁed negative trust (JPT),
and Reliance (Rc) of X-ToM with the baselines. As we can see, JPT, JNT and Rc
values of X-ToM are signiﬁcantly higher than ΩQA and ΩSalience (p < 0.01). Also,
it should be noted that attribution techniques (ΩSalience) did not perform any better
than the ΩQA baseline where no explanations are provided to the user. This could
be attributed to the fact that, though saliency maps help human subjects in localizing
the region in the image based on which the performer made a decision, they do not
necessarily reﬂect the underlying inference mechanism. In contrast, X-ToM Explainer
makes the underlying inference processes (α, β, γ) more explicit and transparent and
also provides explanations tailored for individual user’s perception and understanding.
3These experiments were reviewed and approved by our institution’s IRB.
22


## Page 23


Figure 7: Gain in Justiﬁed Positive Trust, Justiﬁed Negative Trust and Reliance: X-ToM vs baselines (QA,
Saliency Maps). Error bars denote standard errors of the means.
Therefore X-ToM leads to the signiﬁcantly higher values of JPT, JNT and Rc. This is
one of the key results of our work, given the popularity of attribution techniques as the
state-of-the-art explanations.
Figure 8 shows the average explanation satisfaction rates obtained from each of
the three groups. As we can see, subjects in X-ToM experiment group found that
explanations were highly useful, sufﬁcient and detailed compared to the baselines (p <
0.01). Interestingly, we did not ﬁnd signiﬁcant differences across the three groups
in terms of other satisfaction measures: conﬁdence, understandability, accuracy and
consistency. We leave this observation for future exploration
4.3. Gain in Reliance over time
We hypothesized that human trust and reliance in machine might improve over
time. This is because, it can be harder for humans to fully understand the machine’s
underlying inference process in one single session. Therefore, we conduct an addi-
tional experiment with eight human subjects where the subjects’ reliance is measured
23


## Page 24


Figure 8: Explanation Satisfaction: X-ToM vs baselines (QA, Saliency Maps). Error bars denote standard
errors of the means.
Figure 9: Gain in Reliance over sessions w.r.t α, β and γ processes
24


## Page 25


Figure 10: Top-3 best explanations generated with and without using X-ToM.
after every session. The results are shown in Figure 9. As we expected, subjects’ re-
liance increased over time. Speciﬁcally, reliance with respect to α inference process
signiﬁcantly improved only after 2.5 sessions. Reliance with respect to β and γ infer-
ence processes signiﬁcantly improved after 4.5 sessions. It is clearly evident that, with
more sessions, it is possible to further improve human reliance in AI system.
4.4. Case Study
Figure 10 shows examples where the top-3 best explanations preferred by X-ToM
are compared against the top-3 explanations generated by the attribution techniques.
The ﬁrst column shows the input image for the task. The second column shows all the
evidence (i.e., explanations in the form of bubbles, highlighted in yellow color) used in
the machine’s inference about the task. The thicker the bubble, the higher is its inﬂu-
ence, for the machine, in interpreting the image. As we can see, attribution techniques
chose the explanations only based on how inﬂuential they are for the machine in rec-
ognizing the image (third column). In contrast, since X-ToM maximizes the utility of
25


## Page 26


explanations based on both inﬂuence values and user’s model, explanations selected by
the X-ToM (fourth column) are diverse and are more intuitive for humans to understand
and solve the task efﬁciently. For example, for the ﬁrst image, to aid the human user in
solving the task ‘Is the person in the image walking’, X-ToM generates the explanation
bubbles based on left arm, right arm and lower body of the person, whereas attribu-
tion techniques generate the top-3 bubbles only based on right arm which clearly is not
sufﬁcient for the user to successfully solve the task.
Figure 11: Qualitative Reliance. Error bars denote standard errors of the means.
In addition to the quantitative and qualitative metrics discussed in section 2.5, we
also measure the following metrics for comparing our X-ToM framework with the base-
lines:
• Response Time: We record the time taken by the human subject in answering
evaluator questions. Figure 12 shows the average response times (in milliseconds
per question) for each of the three groups (X-ToM, QA and Saliency Maps). We
expected the participants in X-ToM group to take less time to respond compared
to the baselines. However, we ﬁnd no signiﬁcant difference in the response times
across the three groups.
26


## Page 27


Figure 12: Response Times (in milliseconds per question). Error bars denote standard errors of the means.
• Subjective Evaluation of Reliance: We collect subjective Reliance values (on
a Likert scale of 0 to 9) from the subjects in the three groups. The results are
shown in Figure 11. These results are consistent with our quantitative reliance
measures. It may be noted that subjects’ qualitative reliance in Saliency Maps is
lower compared to the QA baseline.
5. Conclusions
This paper presents X-ToM – a new framework for Explainable AI (XAI) and hu-
man trust evaluation based on the Theory-of-Mind (ToM). X-ToM generates expla-
nations in a dialog by explicitly modeling, learning, and inferring three mental states
based on And-Or Graphs – namely, machine’s mind, human’s mind as inferred by the
machine, and machine’s mind as inferred by the human. This allows for a principled
formulation of human trust in the machine. For the task of visual recognition, we pro-
posed a novel, collaborative task-solving game that can be used for collecting training
data and thus learning the three mental states, as well as a testbed for quantitative eval-
uation of explainable vision systems. We demonstrated the superiority of X-ToM in
gaining human trust relative to baselines.
27


## Page 28


6. Acknowledgement
The work is supported by DARPA XAI N66001-17-2-4029.
References
References
[1] E. T. Chancey, J. P. Bliss, A. B. Proaps, P. Madhavan, The role of trust as a
mediator between system characteristics and response behaviors, Human factors
57 (6) (2015) 947–958.
[2] V. Gulshan, L. Peng, M. Coram, M. C. Stumpe, D. Wu, A. Narayanaswamy,
S. Venugopalan, K. Widner, T. Madams, J. Cuadros, et al., Development and
validation of a deep learning algorithm for detection of diabetic retinopathy in
retinal fundus photographs, Jama 316 (22) (2016) 2402–2410.
[3] J. B. Lyons, M. A. Clark, A. R. Wagner, M. J. Schuelke, Certiﬁable trust in au-
tonomous systems: Making the intractable tangible., AI Magazine 38 (3).
[4] V. Mnih, K. Kavukcuoglu, D. Silver, A. Graves, I. Antonoglou, D. Wierstra, M. A.
Riedmiller, Playing atari with deep reinforcement learning, CoRR abs/1312.5602.
arXiv:1312.5602.
URL http://arxiv.org/abs/1312.5602
[5] Z. C. Lipton, The mythos of model interpretability, in: ICML Workshop on Hu-
man Interpretability in Machine Learning, 2016.
[6] M. T. Ribeiro, S. Singh, C. Guestrin, Why should i trust you?: Explaining the
predictions of any classiﬁer, in: Proceedings of the 22nd ACM SIGKDD Inter-
national Conference on Knowledge Discovery and Data Mining, ACM, 2016, pp.
1135–1144.
[7] T. Miller, Explanation in artiﬁcial intelligence: Insights from the social sciences,
Artiﬁcial Intelligence.
28


## Page 29


[8] S. Yang, Q. Gao, S. Saba-Sadiya, J. Chai, Commonsense justiﬁcation for action
explanation, in: Proceedings of the 2018 Conference on Empirical Methods in
Natural Language Processing, 2018, pp. 2627–2637.
[9] M. Sundararajan, A. Taly, Q. Yan, Axiomatic attribution for deep networks, 34th
International Conference on Machine Learning.
[10] R. Ramprasaath, D. Abhishek, V. Ramakrishna, C. Michael, P. Devi, B. Dhruv,
Grad-cam: Why did you say that? visual explanations from deep networks via
gradient-based localization, CVPR 2016.
[11] M. D. Zeiler, R. Fergus, Visualizing and understanding convolutional networks,
in: European conference on computer vision, Springer, 2014, pp. 818–833.
[12] D. Smilkov, N. Thorat, B. Kim, F. Vi´egas, M. Wattenberg, Smoothgrad: removing
noise by adding noise, arXiv preprint arXiv:1706.03825.
[13] B. Kim, C. Rudin, J. A. Shah, The bayesian case model: A generative approach
for case-based reasoning and prototype classiﬁcation, in: Advances in Neural
Information Processing Systems, 2014, pp. 1952–1960.
[14] R. Hoffman, A taxonomy of emergent trusting in the humanmachine relationship.,
Cognitive systems engineering: The future for a changing world.
[15] R. R. Hoffman, S. T. Mueller, G. Klein, J. Litman, Metrics for explainable ai:
Challenges and prospects, arXiv preprint arXiv:1812.04608.
[16] Q. Zhang, Y. Nian Wu, S.-C. Zhu, Interpretable convolutional neural networks,
in: Proceedings of the IEEE Conference on Computer Vision and Pattern Recog-
nition, 2018, pp. 8827–8836.
[17] S. Jain, B. C. Wallace, Attention is not explanation, Proceedings of the 2019
Conference of the North American Chapter of the Association for Computational
Linguistics: Human Language Technologies (NAACL)arXiv:1902.10186.
URL http://arxiv.org/abs/1902.10186
29


## Page 30


[18] H. H. Clark, E. F. Schaefer, Contributing to discourse, Cognitive science 13 (2)
(1989) 259–294.
[19] S. Devin, R. Alami, An implemented theory of mind to improve human-
robot shared plans execution, in: Human-Robot Interaction (HRI), 2016 11th
ACM/IEEE International Conference on, IEEE, 2016, pp. 319–326.
[20] A. I. Goldman, Theory of Mind, The Oxford handbook of philosophy of cognitive
science, 2012.
[21] D. Premack, G. Woodruff, Does the chimpanzee have a theory of mind?, Behav-
ioral and brain sciences 1 (4) (1978) 515–526.
[22] D. Erhan, Y. Bengio, A. Courville, P. Vincent, Visualizing higher-layer features
of a deep network, Technical report, University of Montreal 1341 (3) (2009) 1.
[23] L. A. Hendricks, Z. Akata, M. Rohrbach, J. Donahue, B. Schiele, T. Darrell,
Generating visual explanations, in: European Conference on Computer Vision,
Springer, 2016, pp. 3–19.
[24] R. Greiner, B. Poulin, P. Lu, J. Anvik, Z. Lu, C. Macdonell, D. Wishart, R. Eisner,
D. Szafron, Explaining naive bayes classiﬁcations.
[25] A. Karpathy, J. Johnson, L. Fei-Fei, Visualizing and understanding recurrent net-
works, arXiv preprint arXiv:1506.02078.
[26] H. Strobelt, S. Gehrmann, B. Huber, H. Pﬁster, A. M. Rush, Visual anal-
ysis of hidden state dynamics in recurrent neural networks, arXiv preprint
arXiv:1606.07461.
[27] B. Zhou, A. Khosla, A. Lapedriza, A. Oliva, A. Torralba, Learning deep fea-
tures for discriminative localization, in: Computer Vision and Pattern Recogni-
tion (CVPR), 2016 IEEE Conference on, IEEE, 2016, pp. 2921–2929.
[28] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, D. Batra, Grad-
cam: Visual explanations from deep networks via gradient-based localization,
ICCV.
30


## Page 31


[29] A. Datta, A. Datta, A. D. Procaccia, Y. Zick, Inﬂuence in classiﬁcation via coop-
erative game theory., in: IJCAI, 2015, pp. 511–517.
[30] C. Brinton, A framework for explanation of machine learning decisions, in:
IJCAI-17 Workshop on Explainable AI (XAI), p. 14.
[31] L. v. d. Maaten, G. Hinton, Visualizing data using t-sne, Journal of machine learn-
ing research 9 (Nov) (2008) 2579–2605.
[32] Q. Zhang, Y. N. Wu, S.-C. Zhu, Interpretable convolutional neural networks, The
IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (2018)
8827–8836.
[33] A. Stone, H. Wang, M. Stark, Y. Liu, D. S. Phoenix, D. George, Teaching com-
positionality to cnns, CVPR.
[34] B. Kim, M. Wattenberg, J. Gilmer, C. Cai, J. Wexler, F. Viegas, et al., Inter-
pretability beyond feature attribution: Quantitative testing with concept activa-
tion vectors (tcav), in: International Conference on Machine Learning, 2018, pp.
2673–2682.
[35] A. Dhurandhar, P.-Y. Chen, R. Luss, C.-C. Tu, P. Ting, K. Shanmugam, P. Das,
Explanations based on the missing: Towards contrastive explanations with per-
tinent negatives, in: Advances in Neural Information Processing Systems, 2018,
pp. 592–603.
[36] Y. Goyal, Z. Wu, J. Ernst, D. Batra, D. Parikh, S. Lee, Counterfactual visual
explanations, in: ICML 2019, 2019.
[37] D. J. Hilton, Conversational processes and causal explanation., Psychological
Bulletin 107 (1) (1990) 65.
[38] T. Lombrozo, The structure and function of explanations, Trends in cognitive
sciences 10 (10) (2006) 464–470.
31


## Page 32


[39] S. Park, B. X. Nie, S.-C. Zhu, Attribute and-or grammar for joint parsing of hu-
man attributes, part and pose, IEEE Trans. on Pattern Analysis and Machine In-
telligence (TPAMI) (2018) 1555–1569.
[40] F. Gosselin, P. G. Schyns, Bubbles: a technique to reveal the use of information
in recognition tasks, Vision research 41 (17) (2001) 2261–2271.
[41] H. H. Clark, D. Wilkes-Gibbs, Referring as a collaborative process, Cognition
22 (1) (1986) 1–39.
[42] R. R. Hoffman, P. A. Hancock, J. M. Bradshaw, Metrics, metrics, metrics, part 2:
Universal metrics?, IEEE Intelligent Systems 25 (6) (2010) 93–97.
[43] T. Miller, Explanation in artiﬁcial intelligence: Insights from the social sciences,
Artiﬁcial Intelligence.
[44] A. P. Witkin, Scale-space ﬁltering, in: Readings in Computer Vision, Elsevier,
1987, pp. 329–332.
[45] L. Carlson, D. Marcu, M. E. Okurowski, Building a discourse-tagged corpus in
the framework of rhetorical structure theory, in: Current and new directions in
discourse and dialogue, Springer, 2003, pp. 85–112.
[46] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural computation
9 (8) (1997) 1735–1780.
[47] Z. Wang, V. Bapst, N. Heess, V. Mnih, R. Munos, K. Kavukcuoglu, N. de Fre-
itas, Sample efﬁcient actor-critic with experience replay, Proceedings of the 5th
International Conference on Learning Representations, ICLR.
[48] R. S. Sutton, D. A. McAllester, S. P. Singh, Y. Mansour, Policy gradient methods
for reinforcement learning with function approximation, in: Advances in neural
information processing systems, 2000, pp. 1057–1063.
[49] S. Johnson, M. Everingham, Clustered pose and nonlinear appearance models for
human pose estimation., in: BMVC, Vol. 2, 2010, p. 5.
32


## Page 33


[50] D. P. Kingma, J. Ba, Adam: A method for stochastic optimization, International
Conference on Learning Representations (ICLR).
33


## Page 34


7. Appendix
7.1. Evaluation with Psychology Subject Pool
Figure 13 shows the statistics (Age, First Language, Gender) of the 120 human
subjects, recruited from our institution’s Psychology subject pool.
Figure 13: Statistics (based on Age, First Language and Gender) of the 120 human subjects, from Psychology
subject pool, participated in our study.
7.2. X-ToM Evaluator Interface and Questions
Speciﬁcally, there are two main types of evaluator questions about the users predic-
tion: (1) whether the Performer would successfully or incorrectly detect objects, parts
and other concepts encoded by AOG; and (2) which image parts are most inﬂuential
for the Performers successful or incorrect object detection. For example, the evalua-
tor’s questions include “which parts of the image are most important for the machine
to recognize that the person is running”, and “which small part of image contributes
most to inferring the surrounding larger part of image”. Figures 14 to 16 show few
sample screenshots (from our web interface) of the exact questions, on the detection of
the body part “Left-Arm”, that we pose to the subjects.
34


## Page 35


Figure 14: Sample evaluator questions
35


## Page 36


Figure 15: Sample evaluator questions
Figure 16: Sample evaluator questions
36

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1909_06907v1_x_tom_explaining_with_theory_of_mind_for_gaining_justified_human_trust
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1909_06907V1_X_TOM_EXPLAINING_WITH_THEORY_OF_MIND_FOR_GAINING_JUSTIFIED_HUMAN_TRUST.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
