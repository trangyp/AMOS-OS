---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.01304v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1909.01304v1_Detecting_Compromised_Implicit_Association_Test_Results_Using_Supervised_Learnin

> Source: 1909.01304v1_Detecting_Compromised_Implicit_Association_Test_Results_Using_Supervised_Learnin.pdf

> Pages: 6

---


## Page 1


Detecting Compromised Implicit Association Test
Results Using Supervised Learning
Brendon Boldt
Marist College
Poughkeepsie, NY, USA
brendon.boldt@gmail.com
Zack While
University of Massachusetts Amherst
Amherst, MA, USA
zwhile@cs.umass.edu
Eric Breimer
Siena College
Loudonville, NY, USA
ebreimer@siena.edu
Abstract—An implicit association test is a human psychological
test used to measure subconscious associations. While widely
recognized by psychologists as an effective tool in measuring
attitudes and biases, the validity of the results can be compro-
mised if a subject does not follow the instructions or attempts
to manipulate the outcome. Compared to previous work, we
collect training data using a more generalized methodology. We
train a variety of different classiﬁers to identify a participant’s
ﬁrst attempt versus a second possibly compromised attempt.
To compromise the second attempt, participants are shown
their score and are instructed to change it using one of ﬁve
randomly selected deception methods. Compared to previous
work, our methodology demonstrates a more robust and practical
framework for accurately identifying a wide variety of deception
techniques applicable to the IAT.
Index Terms—implicit association test, psychology application,
supervised learning, machine learning
I. BACKGROUND AND MOTIVATION
A. Implicit Association Test
An implicit association test (IAT) is a human cognitive test
that measures subconscious association between concepts and
attributes [7]. For example, in our experiment, the concepts
are computer science are biology, and the attributes are male
and female. In our example, a positive IAT score indicates
that a participant associates computer science with male and
biology with female, whereas a negative scores indicates
the participant associates computer science with female and
biology with male. Scores close to zero indicate weak or
neutral associations.
Participants are shown items (typically words or images)
on the center of a web page. Each item represents one of
the concepts or attributes. For example, in our experiment,
ﬁrst names such as James and Mary are used to represent the
attributes male and female and words such as Internet and
habitat are used to represent the concepts computer science
and biology.
© 2018 IEEE. Personal use of this material is permitted. Permission from
IEEE must be obtained for all other uses, in any current or future media,
including reprinting/republishing this material for advertising or promotional
purposes, creating new collective works, for resale or redistribution to servers
or lists, or reuse of any copyrighted component of this work in other works.
Special thanks to P. Assumpcao, F. Bassey, E. Da Silva, T. Donnelly, I.
Gomes, Y. Machado, K. Malone-Miller, L. Silva, and C. Snyder for their
early contributions to this project. Research funded by the 2016 NSF REU
program through Siena College.
An IAT is divided into practice blocks, which familiarize
the participant with the items, and critical blocks, which test
the participant’s ability to correctly and quickly categorize
the items. In each block, concepts, attributes, or both are
assigned to the left and right side in different conﬁgurations
(see [6]). When a participant is shown an item, they must press
a keyboard key with either their left or right index ﬁnger to
match the item with the correct concept or attribute.
The key principle of an IAT is that if a participant naturally
associates a concept with an attribute, they will be able to
match items more quickly and with fewer errors when the
concept and attribute are paired on the same side. Conversely,
if a participant disassociates a concept with an attribute,
their response will typically be slower and more prone to
error when the concept and attribute are paired on the same
side. The difference in response time and error rate between
concept-attribute pairing is recognized by psychologists as a
good measure of implicit or subconscious association. Implicit
association is often different than self-reported association and
detecting this difference is considered valuable to understand-
ing biases, attitudes, and mental processes. [9, 10, 11, 2]
By one survey, IATs accounted for 50% of implicit bias
measurements in social cognition research and since the time
of the survey has remained an inﬂuential measurement tool.
[13, 3]
B. Faking, Deceiving, and Compromising IAT Results
The validity of IAT results can be compromised in many
different ways. Participants may not correctly follow the in-
structions or may become distracted during critical blocks. Par-
ticipants can deliberately make errors or delay/accelerate their
response time in order to alter their IAT score. Participants
can modify their response patterns through concentration or
by physical modiﬁcation such as changing their hand position.
It is possible for the same participant to produce test results
that show signiﬁcantly different or contradictory outcomes.
For example, a participant’s ﬁrst IAT attempt could show a
strong association between computer science and male but
a subsequent attempt could show a very weak association
or the opposite association, i.e., strong association between
computer science and female. One of the goals of tools
measuring implicit (subconscious) bias like an IAT is to rule
out conscious or controlled responding. A critical problem is
arXiv:1909.01304v1  [cs.HC]  3 Sep 2019


## Page 2


that participants who are familiar with IATs can potentially
control results and deceptively obtain that does not reﬂect their
natural implicit association.
Previous psychological studies have developed simple mea-
sures for identifying participants who faked their results. By
examining the difference between the average response time of
the fastest critical block in a natural IAT and average response
time of the slowest critical block in a faked IAT, researchers
[4] averaged 75% accuracy in identifying faked attempts. By
examining the ratio between average response time for the
fastest critical block and the corresponding practice blocks,
researchers [1] achieved 80% accuracy. While these indices
accurately identify scores that were faked by slowing down,
more recent work [15] found that these indices fail to identify
other deception strategies.
While many IAT faking strategies have been studied [16, 12,
5], research in detecting IAT faking [17, 1, 4, 14] focus on only
one or two deception strategies. To obtain training data for
analysis, researchers (i) use surveys to prune out participants
who are familiar with IATs, (ii) use direct observation to
prune out participants who are not following the instructions
correctly, and (iii) use aggregate data and cutoffs to prune
out participants who cannot signiﬁcantly alter their IAT score
when instructed to do so. Thus, researchers are analyzing data
consisting of only veriﬁed natural attempts and successfully
faked attempts, which will have signiﬁcant statistical differ-
ences. Thus, these studies give practitioners false conﬁdence
that determining the validity of IAT results is a simple and
easily solved problem.
When one considers scenarios with subjects who cannot be
surveyed or observed, who may not be following the correct
instructions, or who may be employing a wide variety of
effective or ineffective deception strategies, the problem of
determining IAT validity is more challenging. In this paper we
focus on experiments that do not necessarily rely on the the aid
of direct observation, prior knowledge about the participants,
or selective data pruning.
II. METHODOLOGY
A. IAT Implementation
While IAT data is publicly available, it was important to
obtain very speciﬁc training data to capture a variety of
different deception techniques. Thus, we implemented our own
online IAT to match the block conﬁguration and improved
scoring algorithm described in Greenwald et al. [8].
We chose computer science and biology as the two concepts,
and male and female as the two attributes. We selected these
concepts and attributes because they reﬂect a well-known
stereotype where it is reasonable to accept association between
computer science and male. Following the best practices
described in Greenwald et al. [9], we selected words (see Table
I) to represent the concepts and attributes.
Concept/Attribute
Items
Computer Science
Apps, Computer, Algorithm, Database,
Internet, Programming, Software, Technology
Biology
Nature, Life, Photosynthesis, Habitat, Organs,
Plants, Species, Protein
Male
James, John, Robert, Michael, William, David,
Richard, Joseph
Female
Mary, Patricia, Jennifer, Elizabeth, Linda,
Barbara, Susan, Margaret
TABLE I: Items used for concepts and attributes
#
Description of deception strategy
1
Make about 10 errors intentionally
2
Say “one Mississippi” before pressing the appropriate key
3
Put your hands in your lap between keypresses
4
Cross your hands on the keyboard
5
Touch your nose before pressing the appropriate key
TABLE II: Five deception strategies
B. Participants and Deception Strategies
With the approval of our institutional review board1, we
solicited participation by contacting friends and colleagues
via direct email and private Facebook messaging. Participants
were directed to a webpage where they were presented with an
informed consent agreement. Those who agreed to participate
were asked to complete a short demographic survey, which was
not used in this speciﬁc study, followed by the IAT described
above. After completing the IAT (ﬁrst attempt), participants
were shown their score and whether they associated computer
science with male (positive score) or computer science with
female (negative score). Afterwards, participants were pre-
sented with an infographic that describes one of ﬁve randomly-
selected deception strategies for altering one’s score.
Table II summarizes the ﬁve deception strategies and Fig. 1
shows an example infographic. Each presented infographic is
customized to describe when to use the deception strategy in
order to alter one’s score on the second attempt. For example,
if a participant’s ﬁrst attempt score is positive, the instructions
(if followed) will yield a negative score. Conversely, if a
participant’s ﬁrst attempt score is negative, following the
instructions will yield a positive score on the second attempt.
C. Method Goals
Out methodology is designed to generate two classes of
IAT attempts: The ﬁrst attempt is where participants take
our speciﬁc IAT for the ﬁrst time and the second attempt, is
where participants have been previously shown (i) their ﬁrst
attempt score, (ii) the association indicated by their score, and
(iii) instructions on how to alter their score to achieve the
opposite association. Unlike previous studies [17, 1, 4, 14],
we did not exclude ﬁrst attempts based on survey answers or
direct observation nor did we exclude second attempts that did
1IRB# 05-16-005


## Page 3


(a) Instructions to disassociate computer science and male using
error manipulation.
Fig. 1: Infographic Examples
not produce a signiﬁcantly different score, i.e., unsuccessful
faking/deception. We only removed attempts that were incom-
plete, i.e., the participant quit before ﬁnishing all the blocks
in the two IAT attempts.
While pruning the data based on direct observation and
expert knowledge yields training data that is more accurate
in terms of identifying natural implicit reaction vs. truly faked
responses, consider that direct observation is challenging when
administering online IATs and that participants might not be
truthful when asked about previous IAT knowledge. Our goal
is to show that previous methodologies may not be effective
when applied to more realistic data and that a machine learning
approach is needed to more accurately classify IAT results.
III. IAT ATTRIBUTES AND DETECTING SECOND
ATTEMPTS
An IAT records a participants key press response times and
errors in categorizing 200 items. The items are presented in
seven blocks where each block represents a screen conﬁgura-
tion with different concepts, attributes, or both paired on the
right and left side. Three of the blocks (80 presented items)
are practice blocks that only include concepts or attributes to
help familiarize the participant with the items and the correct
classiﬁcations. Four of the blocks (120 presented items) are
critical blocks where both concepts and attributes are paired
together on each side. In critical blocks, the user’s response
time and accuracy are used to determine their IAT score. In
our experiment, all ﬁve of the presented deception strategies
instruct the participant to use a delaying technique during
the two critical blocks (60 presented items) which paired the
naturally associated concepts. If the participant successfully
employs that strategy, their score will be altered.
Note that some participants may not employ the strategy at
all, i.e., they may forget what to do on the second attempt. In
principle, these second attempts could be considered natural
Attempt
Response Time
Error Rate
Score
First
0.802 (0.113)
0.069 (0.054)
0.395 (0.373)
Second
0.844 (0.168)
0.096 (0.066)
0.010 (0.500)
p-value
0.0075
0.0006
< 0.0001
TABLE III: Mean value and standard deviation for the critical
blocks of ﬁrst and second attempts; p-value indicating the
signiﬁcance of the difference between the ﬁrst and second
attempts
ﬁrst attempts since the participant is not altering their behav-
ior. However, participants’ response time and accuracy may
change on the second attempt. Participants are more familiar
with the items so response time and error rate could decrease,
but they are also more fatigued and it may be harder to
concentrate. Nonetheless, it may be possible to detect second
attempts from response differences regardless of whether or
not the deception strategy is being used effectively. Also, note
that some participants may employ the strategy during the
wrong block conﬁgurations. If the strategy is employed during
practice blocks, it will not impact their IAT score at all, but
it will impact response time and accuracy. If the strategy is
employed during the wrong critical blocks, it would exaggerate
the score, i.e, strengthen association rather than reverse it.
Again, it may be possible to detect second attempts even if
the deception strategy is being improperly employed.
It is important to note that second attempts do not necessar-
ily represent deception. Instead, they represent a more general
and diverse class of IATs that are potentially compromised.
Correctly classifying ﬁrst attempts vs. second attempts is likely
more challenging than classifying veriﬁed natural attempts vs.
effectively faked attempts.
IV. RESULTS AND DISCUSSION
A. Overview
Out of approximately 200 solicited participants, 108 agreed
to the informed consent and 67 completed all trials in both
their ﬁrst and second IAT attempts. Table III shows the mean
and standard deviation of the response times, error rates, and
IAT scores for both the ﬁrst and second IAT attempts among
the 67 full participants. The last row shows the p-value of a
two-tailed dependent t-test for paired samples. These values
indicate a strong statistical difference between the ﬁrst and
second attempts.
On the ﬁrst attempt, the average IAT score was 0.395 and
87% (58 out of 67) participants scored above zero indicating
that our participants tend to associate computer science with
male. The information presented to the participants after the
ﬁrst attempt had a signiﬁcant impact on altering the second
attempt. The mean score decreased to 0.010 and only 52%
(35 out of 67) participants scored above zero indicating a
signiﬁcant change to neutral association. Overall 51 out of 67
participants were able to alter their score by at least 1 standard
deviation opposite their initial association.


## Page 4


ML Method
Unpruned (n = 154)
Pruned (n = 102)
Naive Bayes
0.721
0.735
SVM
0.728
0.779
Logistic
0.747
0.716
Multilayer Perceptron
0.719
0.812
Simple Logistic
0.700
0.764
JRip
0.675
0.712
Random Forest
0.678
0.745
TABLE IV: Results of various machine learning methods.
Pruning the data entailed of removing deception attempts that
resulted in a < 1 SD score change.
B. Comparing Multiple Machine Learning Methods
IAT Score data as well as individual trial times were
exported from the website; using the IAT package2 and basic
functions in R, multiple features were calculated for each
of the seven blocks, including the percent of errors, percent
of responses faster than 300ms, ﬁve-number summary, and
skewness. Using these measures, we made two subsets of the
dataset: an unpruned set consisting of all IAT attempts and
a pruned set of all ﬁrst attempts and only second attempts
which reversed the score from the ﬁrst attempt. We deﬁned
a successfully reversed score as a second IAT attempt that
changed by at least one standard deviation toward the opposite
direction of the initial attempt. The ﬁnal datasets did not
contain the score associated with the IAT attempt as this would
assume prior knowledge of the true score of the attempt.
We performed feature selection on both subsets, and any
attribute with a correlation value above 0.75 was subsequently
removed. Removing the correlated attributes would allow for
faster training times and eliminated any features that would
not contribute to the models. For each subset, we used 7
distinct machine learning algorithms provided by Weka (using
the default parameters): naive Bayes, support vector machines,
multinomial logistic regression, multilayer perceptron, simple
logistic regression, propositional rule learner (JRip), and ran-
dom forest. Training and testing was done using leave-one-
out cross-validation. Table IV shows the weighted F1 scores
across each subset and with each ML method. We used F1
scores as a comparative metric because it is more robust in
comparison with accuracy, especially when looking at datasets
where classes are not equally distributed.
On the unpruned data, multinomial logistic performed the
best achieving an F1 score of 0.75 followed closely by naive
bayes, SVM, and multilayer perceptron. The multilayer per-
ceptron performed the best on the pruned data achieving an F1
score of 0.81. All models, with the exception of multinomial
logistic, performed better on the pruned data. Overall, the
more complex models (i.e., SVM and multilayer perceptron)
performed the best across the pruned and unpruned data.
It is important to note the model performances on both
the pruned and unpruned data since they address similar but
2https://cran.r-project.org/web/packages/IAT/index.html
distinct tasks: the unpruned data looks to identify unnatural
or compromised IATs (ones that have not been taken honestly
and for the ﬁrst time) while the pruned data seeks to identify
only those who successfully reverse their score. Which one
of these is relevant would depend on the intended use of the
model.
C. Deeper Investigation with Muti-Layer Perceptrons
In order to more closely investigate whether there were more
subtle complexities, we used a multilayer perceptron (MLP)
built in TensorFlow to more ﬁnely control the neural network
in order to see if offered any signiﬁcant gains in F1 score over
the other methods.
The MLPs were tested with 10-fold as well as leave-one-out
cross-validation with similar results. After approximately 50
epochs of training, the MLP would show signiﬁcantly lower
training costs than on unseen test cases due to overﬁtting
on the training data; despite this, increases in performance
occurred until about 200 epochs. Even with methods of reg-
ularization including reducing the hidden layer nodes, adding
dropout, and including weight decay in the cost metric failed
to signiﬁcantly reduce overﬁtting in the neural net. One likely
cause of overﬁtting is the small training set size. We found
adding a second hidden layer did not alter the performance of
the MLP and would only worsen overﬁtting. Normalizing the
input datasets signiﬁcantly improved the performance of the
MLP.
Using a perceptron with one hidden layer written in Ten-
sorFlow speciﬁcally with 13 hidden nodes and a 0.7 keep
probability (for dropout) attained an F1 score of 0.78 on the
unpruned data after 200 epochs (using a 0.5 threshold for the
F1 score). This F1 score outperformed all of the Weka models.
The TensorFlow MLP was able to match but not exceed the
Weka MLP with an F1 score of 0.81 on the pruned data.
Although pruning improved the performance of the model,
the MLP does not rely on pruning for effective prediction.
While we speciﬁcally compared F1 scores, accuracies for the
TensorFlow MLP fell in the 0.7 to 0.8 range.
D. Comparison to Previous Methods of Detection
As a point of comparison, we implemented the top-
performing method of faking detection presented in Agosta
et al. [1] which is based off of the ratio of response times of
the fastest pair of critical blocks to those of the corresponding
practice blocks. Table V shows our top performing model (the
TensorFlow MLP) compared against the ratio-based model
both on the unpruned and pruned data. Tweaking the threshold
ratio for faked/non-faked IATs did not signiﬁcantly alter the
F1 score.
The ratio-based model showed accuracies of 70% or lower
as opposed to 80% as presented in Agosta et al. [1] sug-
gesting that it might not be robust against different deception
strategies. Our machine learning models demonstrate better
robustness to different deception methods by signiﬁcantly
outperforming the ratio-based model.


## Page 5


Model
F1 Unpruned
F1 Pruned
MLP
0.78
0.81
Ratio
0.64
0.58
TABLE V: F1 scores for TensorFlow MLP and ratio-based
method from [1]
V. CONCLUSION
Simple data analysis revealed that 51 out of 67 participants
were able to signiﬁcantly alter their score with only brief
training on how to do so. This clearly motivates the need for
a way to detect compromised IATs as they are not difﬁcult to
deceive.
We found that more complex models such as SVM and
MLP perform slightly better the simpler models we tested.
This suggests that there might be some nuances in the data that
require a more sophisticated model to detect. Yet the fact that
an MLP overﬁts quickly on the data even with regularization
suggests that more data would be needed to make full use of
the model.
With F1 scores (along with accuracy, precision, and recall)
in the 0.7 to 0.8 range, the models we trained would not
prove accurate enough to determine if a single IAT attempt
was honest or not (e.g., 1 in 5 attempts is a false positive or a
false negative). Yet the models could still provide an accurate
assessment of the quality of a large set of IAT attempts, which
would still prove useful in research applications in psychology
and cognitive science. Furthermore, while our models provide
comparable performance to previous attempts to identify faked
IATs, using machine learning to do so offers a more robust
solution regardless of the use of pruning or the method of
deception.
Future work in this area of research could address two main
issues. First, it could determine whether more data is able to
improve the performance of more complex machine learning
models. Second, it could address whether a model trained on
data from one IAT could be applied directly to another IAT
or if each IAT must have a model trained only on that IAT.
Overall, the task of detecting unnaturally taken IATs is
well suited for machine learning as it is a well deﬁned
classiﬁcation problem supported by a rich array of data points
and aggregate metrics. That being said, the nature of obtaining
data directly from human subjects can present two challenges.
First, machine learning models perform better with a large
volume of data, yet obtaining data from human subjects
is time-consuming and requires a relatively large amount
of effort. Second, the veracity of the data will always be
in question; this is exaggerated by the fact that IATs rely
very heavily on honest, natural responses which can never
be undisputedly veriﬁed. Despite this, we have developed a
method of identifying compromised IATs that is robust in the
face of multiple different deception strategies.
REFERENCES
[1] S. Agosta, V. Ghirardi, C. Zogmaister, U. Castiello, and
G. Sartori. Detecting Fakers of the autobiographical IAT.
Applied Cognitive Psychology, 25:1299–1306, 2010.
[2] John A. Bargh. Social psychology and the unconscious:
The automaticity of higher mental processes. Psychology
Press, 2013.
[3] Dimensions
by
Digital
Science.
Publication
per
year
for
“implicit
association
test”.
2018.
URL
https://app.dimensions.ai/analytics/publication/
viz/overview-publications?search text=implicit%
20association%20test.
[4] D. Cvencek, A. Greenwald, A. Brown, N. Gray, and
R Snowden. Faking of the Implicit Association Test Is
Statistically Detectable and Partly Correctable. Basic and
Applied Social Psychology, 32:302–314, 2010.
[5] K. Fiedler and M. Bluemke. Faking the IAT: Aided and
Unaided Response Control on the Implicit Association
Tests.
Basic and Applied Social Psychology, 27:307–
316, 2010.
[6] A. G. Greenwald and M. R. Banaji.
Implicit social
cognition: Attitudes, self-esteem, and stereotypes. Psy-
chological Review, 102:4–27, 1995.
[7] A. G. Greenwald, D. E. McGhee, and J. L. Schwartz.
Measuring individual differences in implicit cognition:
the implicit association test. Journal of Personality and
Social Psychology, 74:1464–1480, 1998.
[8] A. G. Greenwald, M. R. Banaji, and B. A. Nosek.
Understanding and using the Implicit Association Test: I.
An improved scoring algorithm. Journal of Personality
and Social Psychology, 85:197–216, 2003.
[9] A. G. Greenwald, M. R. Banaji, and B. A. Nosek.
Understanding and using the Implicit Association Test:
II. Method variables and construct validity. Journal of
Personality and Social Psychology, 31:166–180, 2005.
[10] A. G. Greenwald, T. A. Poehlman, E. L. Uhlmann, and
M. R. Banaji.
Understanding and using the Implicit
Association Test: III. Meta-analysis of predictive validity.
Personality and Social Psychology Bulletin, 97:17–41,
2009.
[11] W. Hofmann, B. Gawronski, T. Gschwendner, H. Le,
and M. Schmitt.
A Meta-Analysis on the Correlation
Between the Implicit Association Test and Explicit Self-
Report Measures.
Personality and Social Psychology
Bulletin, 31:1369–1385, 2005.
[12] M. McDaniel, M. Beier, A. Perkins, S. Goggin, and
B. Frankel.
An assessment of the fakeability of self-
report and implicit personality measures.
Journal of
Research in Personality, 43:682–685, 2009.
[13] Brian Nosek, Carlee Beth Hawkins, and Rebecca S Fra-
zier. Implicit social cognition: From measures to mecha-
nisms. Trends in cognitive sciences, 15:152–9, 03 2011.
[14] J. R¨ohner and E. Torsten. Trying to separate the wheat
from the chaff: Construct- and faking-related variance on
the Implicit Association Test (IAT). Behavior Research


## Page 6


Methods, 48:243–258, 2015.
[15] J. R¨ohner, M. Schr¨oder-Ab´e, and A. Sch¨utz. What do
fakers actually do to fake the IAT? An investigation
of faking strategies under different faking conditions.
Journal of Research in Personality, 47:330–338, 2013.
[16] M. Steffens. Is the Implicit Association Test Immune to
Faking? Experimental Psychology, 51:165–179, 2004.
[17] S. Stieger, A. G¨oritz, A. Hergovich, and M. Voracek.
Intentional faking of the single category Implicit Associa-
tion Test and the Implicit Association Test. Psychological
Reports, 109:219–230, 2011.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1909_01304v1_detecting_compromised_implicit_association_test_results_using_supervised_learnin
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1909_01304V1_DETECTING_COMPROMISED_IMPLICIT_ASSOCIATION_TEST_RESULTS_USING_SUPERVISED_LEARNIN.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
