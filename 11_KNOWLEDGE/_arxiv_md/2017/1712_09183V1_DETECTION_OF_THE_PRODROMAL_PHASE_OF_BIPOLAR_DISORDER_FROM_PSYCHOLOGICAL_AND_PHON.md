---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1712.09183v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1712.09183v1_Detection_of_the_Prodromal_Phase_of_Bipolar_Disorder_from_Psychological_and_Phon

> Source: 1712.09183v1_Detection_of_the_Prodromal_Phase_of_Bipolar_Disorder_from_Psychological_and_Phon.pdf

> Pages: 10

---


## Page 1


Detection of the Prodromal Phase of Bipolar Disorder from
Psychological and Phonological Aspects in Social Media
Yen-Hao Huang
National Tsing Hua University
Hsinchu, Taiwan
yenhao0218@gmail.com
Lin-Hung Wei
National Tsing Hua University
Hsinchu, Taiwan
adeline80916@gmail.com
Yi-Shin Chen
National Tsing Hua University
Hsinchu, Taiwan
yishin@gmail.com
ABSTRACT
Seven out of ten people with bipolar disorder are initially
misdiagnosed and thirty percent of individuals with bipolar
disorder will commit suicide. Identifying the early phases of
the disorder is one of the key components for reducing the
full development of the disorder. In this study, we aim at
leveraging the data from social media to design predictive
models, which utilize the psychological and phonological fea-
tures, to determine the onset period of bipolar disorder and
provide insights on its prodrome. This study makes these dis-
coveries possible by employing a novel data collection process,
coined as Time-specific Subconscious Crowdsourcing, which
helps collect a reliable dataset that supplements diagnosis
information from people suffering from bipolar disorder. Our
experimental results demonstrate that the proposed models
could greatly contribute to the regular assessments of people
with bipolar disorder, which is important in the primary care
setting.
KEYWORDS
Bipolar Disorder Detection, Mental Disorder, Prodromal
Phrase, Emotion Analysis, Sentiment Analysis, Phonology,
Social Media
1
INTRODUCTION
Bipolar disorder (BD) is a common mental illness charac-
terized by recurrent episodes of mania/hypomania and de-
pression, which is found among all ages, races, ethnic groups
and social classes. The regular assessment of people with
BD is an important part of its treatment, though it may be
very time-consuming [21]. There are many beneficial treat-
ments for the patients, particularly for delaying relapses. The
identification of early symptoms is significant for allowing
early intervention and reducing the multiple adverse conse-
quences of a full-blown episode. Despite the importance of
the detection of prodromal symptoms, there are very few
studies that have actually examined the ability of relatives to
detect these symptoms in BD patients. [20] For the purpose
of early treatment, the challenge leads to: how to identify
the prodrome period of BD. Current studies are thus
aimed at detecting prodromes and analyzing the prodromal
symptoms of manic recurrence in clinics.
With regards to the symptom of social isolation, people
are increasingly turning to popular social media, such as
Facebook and Twitter, to share their illness experiences or
seek advice from others with similar mental health conditions.
As the information is being shared in public, people are
subconsciously providing rich contents about their states
of mind. In this paper, we refer to this sharing and data
collection as time-specific subconscious crowdsourcing.
In this study, we carefully look at patients who have been
diagnosed with BD and who explicitly indicate the diagnosis
and time of diagnosis on Twitter. Our goal is to both predict
whether BD rises on a given period of time, and to discover
the prodromal period for BD. It’s important to clarify that
our goal doesn’t seek to offer a diagnosis but rather to make
a prediction of which users are likely to be suffering from the
BD. The main contributions of our work are:
∙Introducing the concept of time-specific subconscious
crowdsourcing, which can aid in locating the social
network behavior data of BD patients with the corre-
sponding time of diagnosis.
∙A BD assessment mechanism that differentiates be-
tween prodromal symptoms and acute symptoms.
∙Introducing the phonological features into the assess-
ment mechanism, which allows for the possibility to
assess patients through text only.
∙An automatic recognition approach that detects the
possible prodromal period for BD.
2
RELATED WORK
Social media resources have been widely utilized by researchers
to study mental health issues. The following literature em-
phasizes on data collection and feature engineering, including
subject recruitment, manual data collection, data collection
applications, keyword matching, and combined approaches.
The clinical approach for mental disorders and prodrome
studies are also discussed in this section.
Subject recruitment: Based on customized question-
naires and contact with subjects, Park et al. [15] recruited
participants for the Center for Epidemiologic Studies Depres-
sion scale(CES-D) [17] and provided their Twitter data. By
analyzing the information contained in tweets, participants
were divided into normal and depressive groups based on
their scores on CES-D. An approach like this one requires ex-
pensive costs to acquire data and conduct the questionnaire.
Manual and automatic data collecting: Moreno et
al. [14] collected data via the Facebook profiles of college stu-
dents reviewed by two investigators. They aimed at revealing
the relationship between demographic factors and depression.
Similarly, in our work, we invest on manual efforts to collect
and properly annotate our dataset. In addition, there are
many applications built on top of social networks that provide
free services where users may need to input their credentials
arXiv:1712.09183v1  [cs.IR]  26 Dec 2017


## Page 2


and profile information in exchange for interesting analytics
or insights. These applications need to be well-designed to
attract users, otherwise it is difficult to focus on a specific
type of user.
Keywords matching: Coppersmith et al. [8] made use
of regular expressions in social media posts. For instance, a
user who states “I was diagnosed with X” is identified as a
patient who has mental illness X. With this approach, people
diagnosed with different illnesses are collected separately.
Although this keyword matching provides a higher precision
with regards to detecting true positives, the strict filter makes
the number of matched users very small. In our approach, we
also employ keyword matching, but the keywords are more
flexible. Additionally, Coppersmith et al. [8, 9, 12] focused
on linguistic features and patterns of life features (specific
for social network behaviors) to build a predictive model for
mental disorders.
Combined approach: Some previous studies have com-
bined the above approaches to accumulate desirable data. De
Choudhury [10] used a two-stage approach to collect Twitter
data from mothers of newborns. First, the mothers were se-
lected by matching keywords related to birth announcements
in tweets. Second, the manual verification task was delegated
to Amazon’s Mechanical Turk to improve the reliability of
data. For postpartum depression, a statistical model was built
by using linguistic features, a social graph, and engagement
in social networking websites.
Subconscious crowdsourcing: Chang et al. [7] focused
on collecting high-quantity data. Their approach combines
manual and automatic efforts by manually filtering possible
mentally ill users from patient participation groups and user
profiles on Twitter. With this approach, highly self-aware
users are selected, which is not one of our objectives. Inspired
by Chang et al.s’ approach, however, we take the advantage
of keyword matching to maximize the resources found on
Twitter.
Clinical approach: For the study of prodromal features
there have been several retrospective works [5, 13] that have
found that the majority of BD patients experience symptoms
such as episodic mood changes, irritability, or impulsivity
before the onset of the first episode of BD. Sahoo et al. [18]
tracked the recurrence of patients, proceeded with the self-
diagnosis of DSM-IV (The Diagnostic and Statistical Manual
of Mental Disorders, Fourth Edition), and pointed out the
difficulty of patients’ self-awareness. Meter et al. [22] also
surveyed prodromes and underlined the importance of a
sleeping monitor, physical activity, and family attention.
The previously mentioned findings certainly support the
existence of a prodromal phase. Nevertheless, these stud-
ies may have been influenced by a recall bias. Furthermore,
most clinical studies mainly focus on patients found in hospi-
tals, which cost substantially and leave the problem of late
diagnosis unsolved.
Among the aforementioned researches on social media,
none focus on the detection of the acute and prodromal phases
of a mental disorder. Clinical researchers have dived into
the details of prodromes, providing many traceable features.
However, for some recurrent mental disorders, it is difficult
to closely monitor the mental status of a patient in person
after they leave the clinic, even though regular assessment is
important in a primary care setting. In our work, we commit
to seeking resources on social media platforms and propose an
approach using linguistics, behavioral, and clinical features.
3
METHODOLOGY
3.1
Overviews
The objective of this paper is to recognize the prodromal
phases of bipolar disorder by linguistic and phonological
features. Given a user at a specific time as the input, the
recognition system can perform a regular assessment of BD.
The problem is formally defined as follows:
Definition 1 (Problem Statement). Given a specific time 𝑠,
a time frame 𝛼, and a user 𝑘, we can collect a set of tweets
Γ(𝑘)
𝑠,𝛼= {𝜔(𝑘)
𝑡
| 𝑡∈[𝑠−𝛼, 𝑠]} and derive the model 𝑓with
the objective to map the set Γ(𝑘)
𝑠,𝛼to a BD onset probability
𝑙(𝑘)
𝑠,𝛼= 𝑓(Γ(𝑘)
𝑠,𝛼), which is a number in [0, 1], where 0 denotes
no onset of BD and 1 denotes a full onset.
Since BD is a recurrent mental illness and the onset symp-
toms are intermittent on a monthly basis, identifying its
possible prodromal phases from social media data becomes
a challenging task. Our solution introduces the time of di-
agnosis of the illness to our recognition model. The time
of diagnosis specifies the exact date when the person was
diagnosed as a patient with BD by a certified psychiatrist.
Based on the discussion above, assumption 1 is made.
Assumption 1. When people are diagnosed with BD, the
signs and symptoms are observable.
Our proposed prodromal recognition method is called Ill-
ness Behavior Inference. Its core contribution is the BD onset
predictive model(BDOPM), a supervised learning process that
predicts the BD onset probability given the following infor-
mation: time 𝑠, user 𝑘, tweets Γ(𝑘)
𝑠,𝛼, time frame 𝛼, and is
optimized by the time of diagnosis 𝜏(𝑘).
Not only is this predictive model able to capture the acute
phases of bipolar disorder, but can also recognize the different
behaviors for a BD patient over time given a time of diagnosis
indicator 𝜏. The construction of the BD onset predictive
model is divided into five stages:
(1) Time-specific Subconscious Crowdsourcing
(2) Time-domain Modeling
(3) Psychological Feature Extraction
(4) Phonological Feature Extraction
(5) Model Construction and Evaluation
3.2
Time-specific Subconscious
Crowdsourcing
As social media reflect a mirror aspect of real life, people
widely share their feelings, moods, and opinions on them.
The subconscious crowdsourcing [7], as implied by the term
subconscious, indicates that people are unaware and subcon-
sciously providing information, including their mental status.
2


## Page 3


Users with mental illnesses share their common experiences,
such as mania behavior or relapses of an illness. This behavior
represents the concept of the term crowdsourcing. We can
reduce the cost of data collection by accessing information
that is richly stored in social media platforms.
Since our task is to cope with the recurrent characteristic
of BD, every user cannot be regarded as an onset patient
with BD the whole time. In this stage, we provide four steps
for retrieving and collecting a list of BD patients and their
time of diagnosis 𝜏by combining automatic matching with
manual efforts.
3.2.1
Target Seeking. To efficiently retrieve the targeting
dataset without losing too much information, we perform
an automatic process—a minimum keyword search—on the
platform to obtain related information, followed by labeling
with the search keys. The minimum keyword search procedure
is formally defined below and utilized to collect the BD user
data.
Definition 2 (Minimum Keyword Search). Let Twitter be
composed of a set of tweets Γ = {𝜔} and tweet 𝜔be composed
of a set of 𝑛-grams V𝑛=1
𝜔
= {𝑣𝜔| 𝑣𝜔∈𝜔}. We then select a set
of unigrams Φ as filter keys. Given the search function 𝑔(Γ, Φ),
it returns a set of candidate tweets ΓΦ = {𝜔| Φ ⊆V𝑛=1
𝜔
}.
To search for users with BD, the keywords diagnosed
and bipolar are utilized to perform the minimum search on
Twitter. Twitter users who have mentioned these keywords
in at least one tweet will be selected as users with BD and
the corresponding tweet(s) will be collected as diagnosis
tweet statements. Different to Coppersmith et al.’s keyword
approach [8], our minimum search provides more flexible
filtering, which leads to more tweet matches and more BD
candidates on Twitter.
3.2.2
Time of Diagnosis Identification. After the previous
step is completed, we have collected many possible BD users.
This dataset of users and tweets, however, may contain a
lot of noise. An additional filtering step is thus required. In
our case, which is to target the onset periods, we further
modify the minimum keyword search in order to retrieve
every time-related diagnosis tweet ΓΦ = {𝜔| (Φ ∩V𝜔) ̸= ∅}
with time-related keywords, such as today, last, months, etc.
A manual step is required here to estimate the time of
diagnosis 𝜏more precisely. For example, with the keywords
“diagnosed” and “bipolar”, we may get a tweet like “I was
diagnosed Bipolar Disorder last year this month”. In this
example, we are able to obtain not only the BD user but also
their time of diagnosis. The time of diagnosis confirms that
the user is a real BD user, indicates a more precise onset
period, and reduces the chance to extract wrong features by
processing the tweets in the non-onset period.
To make the diagnosis more precisely, the diagnosis tweets
are filtered manually by the criteria that if it is able to
recognize that the twitter user are diagnosed on which year
and month. In this case, the unclear diagnosis tweets such
as “I was diagnosed Bipolar Disorder last year” or “I was
diagnosed Bipolar Disorder few months ago” are deleted,
because their diagnosed time are not clear enough.
The tweet author 𝑘of a qualified tweet is following ex-
tracted, in which the 𝜏of the tweet can be estimated. The
output of this step is a set of qualified BD users K(𝑏) associ-
ated with their time of diagnosis 𝜏(𝑘).
3.2.3
Tweet Re-collection. We download all tweets Γ(𝑘),
𝑘∈K𝑏from Twitter. In our case, we also retrieve each user’s
timezone and location information if available.
3.2.4
Language Filter and Active User Filter. Our method
focuses on English content, for which reason any user who
has more than 50 percent of their posts containing hyperlinks
or other languages are removed. Additionally, only users with
more than 100 tweets are included, as they are assumed to
be more active users.
In order to optimize the BDOPM stage, the complement
dataset (non-BD users) needs to be collected. The user IDs of
Twitter are randomly sampled using the Twitter Streaming
API for several months of data. These randomly-sampled
users are labled as regular users K(𝑟) (non-BD) and their
corresponding time of diagnosis is set to 𝜏(𝑘) = 0, 𝑘∈K(𝑟).
Subsequently, the tweets of each selected ID are downloaded,
and denoted as Γ(𝑘) = 0, 𝑘∈K(𝑟).
3.3
Illness Period Modeling
For the purpose of onset detection, and owing to the recurrent
nature of BD, we aim to find the most likely periods where
BD is onset by partitioning the tweets into time periods.
Based on Assumption 1, the 𝜏and the length of time 𝛼are
applied to identify the possible acute phase. The illness’s
acute phase is formally defined as:
Definition 3 (Bipolar Disorder Onset Period). The acute
phase is given as S𝜏
𝛼= {𝑡| 𝑡∈[𝜏−𝛼, 𝜏]}.
For demonstration purposes, the concept is illustrated in
Figure 1, assuming a BD onset period of two months, (i.e.,
𝛼= 2). After the possible onset period 𝛼is defined, the
user’s tweets are extracted as Γ(𝑘)
𝜏,𝛼= {𝜔𝑡| 𝑡∈S𝜏
𝛼} and are
considered as the BD onset training data. For non-BD users,
the tweets during period 𝛼are treated as the training data
for regular users. That is, the specific time 𝑠in Definition 1
is set to be the 𝜏for the model-training step for the best
approximation to the BD onset behavior.
3.4
Psychological Feature Extraction
In order to recognize a case of BD, the BDOPM is customized
to detect the following clinical exhibitions:
(1) Rapid cycling between moods. (2) High energy, over
talking, and tendency towards anger. (3) Lessened need for
sleep. (4) Cyclical depression or mania.
As discussed in the related work, there are various types of
linguistic and behavioral features that are important for BD
onset detection. In this step, two main types of psychological
3


## Page 4


Diagnosed time 𝝉
𝜶months
𝜶= 2 months
Figure 1: Illness Period Modeling
features are introduced: (1) Word-level features and BD
Pattern of Life features.
3.4.1
Word-level Features. With respect to the linguis-
tic features for BD, the Character n-gram language fea-
tures(CLF) and LIWC metrics are designed to capture it.
The CLF utilizes 𝑛-grams to measure the comment words
or phrases used by users. The tf-idf is utilized in our score-
calculating method, the 𝑡𝑓is the frequency of an 𝑛-gram and
the document 𝑑of 𝑑𝑓is defined as each particular twitter
user 𝑘. The formula for the tf-idf is thus given as:
𝑡𝑓𝑖𝑑𝑓(𝑘,𝜏,𝛼)
𝑣𝑛
= 𝑓𝑟𝑒𝑞(𝑘,𝜏,𝛼)
𝑣𝑛
× log
𝐾
1 + 𝑓𝑟𝑒𝑞(𝐾,𝜏,𝛼)
𝑣𝑛
(1)
The 𝑓𝑟𝑒𝑞(𝑘)
𝑣𝑛is the frequency of n-gram 𝑣𝑛, which is 𝑛∈{1, 2}
for a specific user 𝑘. The 𝐾denotes the total number of users
in the dataset, and 𝑓𝑟𝑒𝑞(𝐾,𝛼)
𝑣𝑛
denotes the number of user
whose tweets contain the terms of 𝑣𝑛. The resulting tf-idf
vectors are then normalized by the Euclidean norm:
𝑡𝑓𝑖𝑑𝑓(𝑘,𝜏,𝛼)
𝑣𝑛
𝑛𝑜𝑟𝑚=
𝑡𝑓𝑖𝑑𝑓(𝑘,𝜏,𝛼)
𝑣𝑛
√︁
(𝑡𝑓𝑖𝑑𝑓(1,𝜏,𝛼)
𝑣𝑛
)2, . . . , (𝑡𝑓𝑖𝑑𝑓(𝐾,𝜏,𝛼)
𝑣𝑛
)2
(2)
The LIWC features are designed to capture the psycho-
logical terms frequently used by a BD user. The words that
are related to psychological terms (e.g., emotion, affection,
and depression) are selected to represent the features. Based
on the dictionary obtained from the Linguistic Inquiry and
Word Count (LIWC) [16] lexicon, we then calculated the
ratio of each category (64 in total) for each user. The LIWC
score of category 𝑐𝑖for a given user 𝑘is defined as follows:
𝐿𝐼𝑊𝐶(𝑘,𝜏,𝛼)
𝑐𝑖
=
𝑓𝑟𝑒𝑞𝑐𝑖,Γ(𝑘)
𝜏,𝛼
𝑓𝑟𝑒𝑞Γ(𝑘)
𝜏,𝛼
(3)
The LIWC scores are finally normalized by the total number
of user tweets |Γ(𝑘)
𝜏,𝛼|.
3.4.2
Bipolar Disorder Pattern of Life Features (BDPLF).
To capture the features of the BD onset period in the psy-
chological aspect, we propose customized BD pattern of life
features (BDPLF), inferred from [7, 8]. The PLF is designed
to represent psychological features, such as emotional pat-
terns and the behavioral tendency of users by measuring
polarity, emotion, and social interactions. To construct the
full BDPLF, there are five categories:
∙Age and Gender: Sit et al. [21] studied the gender
effects on BD, indicating that women with BD are more
likely to have Bipolar Disorder(Type II) symptoms
than men. We make use of the age and gender predictor
proposed by Sap et al. [19], which is based on lexica in
social media.
∙Mood Polarity Features: Owing to the fact that
BD patients experience rapid mood changes, sentiment
analysis is firstly adapted to obtain the sentiment po-
larity portrayed by each user’s tweets Γ(𝑘). To obtain
the sentiment of tweets, the online tool Sentiment140 is
used, based on Go et al.’s work [11]. The tool classifies
the contents of tweets into three polarity categories:
positive, negative, and neutral. We further partition
those three categories into five different sub-features:
positive ratio, negative ratio, positive combo, negative
combo, and flips ratio.
∙Emotional Scores: Beyond the sentiments, an emo-
tion detection tool proposed by Argueta et al. [1] is
employed to classify the tweets into eight emotion cate-
gories: joy, surprise, anticipation, trust, sadness, disgust,
anger, and fear. The emotion classification results are
further transformed into emotion scores as follows:
𝑒𝑠𝑒𝑖,Γ(𝑘)
𝜏,𝛼=
𝑒𝑖,Γ(𝑘)
𝜏,𝛼
𝑒𝑐𝑜𝑢𝑛𝑡
(4)
where 𝑒𝑖is the 𝑖th emotion and 𝑒𝑐𝑜𝑢𝑛𝑡is the total
number of emotions.
∙Social Features: Social features are designed to cap-
ture a user’s interaction with other users on the social
media platform and how frequently they engage on
Twitter. There are five designed social features, of
which the basic four are tweeting frequency, mention
ratio, frequent mentions, and unique mentions.
∙Insomnia and Over-Talking Features: Our ap-
proach considers two additional social features to cap-
ture the sleep disturbance and over-talking symptoms:
– Late Tweet Frequency The less-sleep symptom is
a prominent characteristic of BD. In order to capture
this feature, our approach performs a timezone con-
version step to convert UTC time to each user’s local
time based on their timezone and location to make
sure the user’s tweeting time is recorded correctly.
This feature is determined by the daily frequency of
posts that a user posts between midnight and 6:00
am in their local time.
– Tweet Rate Difference For the over-talking fea-
ture, this feature is designed to capture the difference
in tweeting behavior from individuals. First, we seg-
ment each user’s tweets based on a slide window
approach. Next, for each segmentation period, we
calculate the average tweet frequency per day. The
4


## Page 5


maximum tweeting rate difference is the max differ-
ence of the tweet frequency for each given user.
From the features listed above, the bipolar disorder pattern
of life feature scores 𝐵𝐷𝑃𝐿𝐹𝑠are formally illustrated as
follows:
𝐵𝐷𝑃𝐿𝐹𝑠(𝑘,𝜏,𝛼)
𝜉𝑚
= 𝐵𝐷𝑃𝐿𝐹𝜉𝑚(Γ(𝑘)
𝜏,𝛼)
(5)
where 𝜉𝑚denotes each sub-feature in BDPLF, and 𝐵𝐷𝑃𝐿𝐹𝜉𝑚
denotes the sub-functions for the sub-features, which return
the corresponding feature scores.
3.5
Phonological Feature Extraction
For phonological features, we consider that words have their
own energy. People in different states have distinct tendencies
to use words. Generally, people who use more high-energy
words are usually in states of excitement or anger. Contrast-
ingly, people who are in states of powerlessness or helplessness
use more low-energy words. People who suffer from depres-
sion show powerlessness more often than ordinary people
do.
As a BD patient is encountered with mania or hypermania
symptoms, they will tend to reveal high energy, talk more,
and have a tendency for anger. When the illness is onset,
the expressions of a BD patient will be especially influenced
by these symptoms and leave emotions in the expression
interface, such as in tweets. The Energy of Words feature
is thus designed to capture the mania expression based on
Assumption 2.
Assumption 2. Writing is accompanied by reading in the
brain. Words carry their own energy, that is, when people try
to write a word, people simultaneously read that word in their
brains. The energy of a person can therefore be inferred by
the statement at the moment they were writing.
Formally, we define the key concept of how the energy of
words are measured as follows:
Definition 4 (Energy Score). The Energy Score 𝑒𝑠𝑣is the
energy of a word. It can be expressed as 𝑒𝑠𝑣= 𝐸𝑆(𝑣), where
𝑣denotes a specific word and 𝐸𝑆denotes the Energy Score
Function.
Definition 5 (Energy Score Function). The Energy Score
Function 𝐸𝑆(𝑣) = 𝑃𝐹(𝐼𝑃𝐴(𝑣)), where 𝐼𝑃𝐴(𝑣) represents
the function that converts a word 𝑣to its IPA form. 𝑃𝐹
denotes the function that returns phonological feature scores
in the IPA form.
In the following sections, we give details to clarify the
entire process of how to quantify the Energy Score step by
step in Definition 5.
3.5.1
Pronunciation Standardization. To standardize the
pronunciation of each alphabet 𝑎𝑖, a standardization method
denoted IPA Standardization Function 𝐼𝑃𝐴(𝑣), shown in
Definition 5, is performed to transfer English words into their
IPA (International Phonetic Alphabet) form[3]. The table
of IPA phonetic transcriptions of consonants and vowels is
shown in Figures 2a and 2b. Each IPA symbol is a phoneme,
which is one of the units of sound that distinguish one word
from another. Hence, the IPA standardization function is
defined below to transfer a word to its transcription.
Definition 6 (IPA Standardization Function). Let P be a set
of phonemes and 𝑝𝑗be a phoneme, where 𝑝𝑗∈P. The IPA of
a word 𝑣is denoted as P𝑣= 𝐼𝑃𝐴(𝑣), where P𝑣= {𝑝1, ..., 𝑝𝐽}.
A word goes through the IPA Transcription Function,
which outputs its transcription consisting of a sequence of
phonemes. For instance, given the word 𝑣= “folder”, it is
able to retrieve the output P𝑣= through 𝐼𝑃𝐴(𝑣), where
P𝑣= {f, oU, l, d, @, r}.
3.5.2
Phonological Feature Score (PF Score). In this sub-
section, the phonological features of phonemes are utilized to
define how much energy a word carried. There are two steps
for the Phonological Feature Score Function to be completed:
First, let’s define the energy score of each phoneme 𝑝𝑗.
From the existing phonological feature systems, the eSPE
(extended Sound Pattern of English) [6] is introduced to
describe the phonological features of phonemes. The eSPE
consists of 21 binary features. It describes what kinds of artic-
ulators and which part of positions are used during speaking.
In our work, 19 features from the eSPE are chosen, with the
exception of “voiced” and “silence”. The eSPE shows that each
phoneme corresponds to some phonological feature, such as
vowel, fricative, nasal and so on. The notations of positive
and negative represent independently if a phoneme has the
corresponding feature or not. For instance, the phoneme “oU”
has phonological features vowel, high, mid, back, continuant,
round, and tense.
Instead of using binary features directly, these relative
phonological features are grouped into the following 8 cate-
gories based on characteristics of phonology. Additionally, the
corresponding scores are assigned according to their difficulty
of pronunciation:
∙Oral Cavity (𝑂𝐶): the phonological features of an-
terior, back and approxim., with scores 𝑑𝑠𝑂𝐶1, 𝑑𝑠𝑂𝐶2,
𝑑𝑠𝑂𝐶3.
∙Mouth Openness (𝑀𝑂): the phonological features
of high, mid and low, with scores 𝑑𝑠𝑀𝑂1, 𝑑𝑠𝑀𝑂2, 𝑑𝑠𝑀𝑂3.
∙Obstruent (𝑂𝑏𝑠): the phonological features of con-
tinuant, labial, fricative and stop, with scores 𝑑𝑠𝑂𝑏𝑠1,
𝑑𝑠𝑂𝑏𝑠2, 𝑑𝑠𝑂𝑏𝑠3.
∙Tongue Position (𝑇𝑃): the phonological features of
coronal, dental and retroflex, with scores 𝑑𝑠𝑇𝑃1, 𝑑𝑠𝑇𝑃2,
𝑑𝑠𝑇𝑃3.
∙Resonance (𝑅𝑒𝑠): the phonological features of nasal,
glottal and velar, with scores 𝑑𝑠𝑅𝑒𝑠1, 𝑑𝑠𝑅𝑒𝑠2, 𝑑𝑠𝑅𝑒𝑠3.
∙Vowel (𝑉𝑜𝑤): the phonological feature of vowel itself
with the score 𝑑𝑠𝑉𝑜𝑤1.
∙Round (𝑅𝑜𝑢): the phonological feature of round itself
with the score 𝑑𝑠𝑅𝑜𝑢1.
∙Tense (𝑇𝑒𝑛): the phonological feature of tense itself
with the score 𝑑𝑠𝑇𝑒𝑛1.
5


## Page 6


(a) IPA Consonants Table
(b) IPA Vowels Table
Figure 2: The International Phonetic Alphabet (IPA)[3], an alphabetic system of phonetic notation based
primarily on the Latin alphabet. It was devised by the International Phonetic Association as a standardized
representation of the sounds of spoken language.
The total scores of each category are denoted as 𝑑𝑠𝑂𝐶, 𝑑𝑠𝑀𝑂,
𝑑𝑠𝑂𝑏𝑠, 𝑑𝑠𝑇𝑃, 𝑑𝑠𝑅𝑒𝑠, 𝑑𝑠𝑉𝑜𝑤, 𝑑𝑠𝑅𝑜𝑢and 𝑑𝑠𝑇𝑒𝑛, by summing
up the scores of their sub-features. Based on these categories,
the phonological score for each phoneme is vectorized as :
𝑝𝑓𝑝𝑗= |𝑑𝑠1
𝑑𝑠2
. . .
𝑑𝑠8|
where each element corresponds to the scores of each category.
To calculate word energy, the Phonological Feature Score
Function is formulated as follows:
𝑃𝐹(P𝑣) =
𝐽
∑︁
𝑗=1
𝑝𝑓𝑝𝑗
(6)
where each element of 𝑃𝐹(𝑃𝑣) denotes the corresponding
scores of each category. The energy of a user is finally repre-
sented as:
𝑒𝑢(𝑘)
𝜏,𝛼=
∑︀𝑒𝑠(𝑘,𝜏,𝛼)
𝑣
𝑣𝑐𝑜𝑢𝑛𝑡
= 𝐸𝑆(𝑣|𝑣∈V𝑛=1
𝜏,𝛼)
|V𝑛=1
𝜏,𝛼|
(7)
where V𝑛=1
𝜏,𝛼denotes a set of single words decomposed from all
the tweets in Γ(𝑘)
𝜏,𝛼. The energy 𝑒𝑢of a user is final normalized
using the total frequency of words 𝑣𝑐𝑜𝑢𝑛𝑡.
3.6
Model Training and Evaluation
In this work, an ensemble supervised machine learning ap-
proach, Random Forest Classifier, has been empirically chosen
to be our training model ˆ𝑓, as it is resistant to overfitting and
is able to perform both classification and regression tasks.
With the feature extraction steps described previously, the
BD onset probability can be represented as:
𝑙(𝑘)
𝜏,𝛼= 𝑓(Γ(𝑘)
𝜏,𝛼) = ˆ𝑓(ℎ(Γ(𝑘)
𝜏,𝛼)),
(8)
where ℎdenotes the feature extraction functions, which are
word-level (CLF and LIWC), pattern of life, and phonological
feature functions. In order to compare feature performance,
the BDOPM is trained for each of the five types using differ-
ent features, which are word-level(character n-gram language
model(CLM) and LIWC model), bipolar disorder pattern of
life model and phonological model:
𝑙(𝑘)
𝜏,𝛼=
⎧
⎪
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎪
⎩
ˆ𝑓𝑡𝑓𝑖𝑑𝑓(𝑡𝑓𝑖𝑑𝑓(𝑘,𝜏,𝛼)
𝑣𝑛
)
ˆ𝑓𝑙𝑖𝑤𝑐(𝐿𝐼𝑊𝐶(𝑘,𝜏,𝛼)
𝑐𝑖
)
ˆ𝑓𝐵𝐷𝑃𝐿𝐹(𝐵𝐷𝑃𝐿𝐹𝑠(𝑘,𝜏,𝛼)
𝜉𝑚
)
ˆ𝑓𝑒𝑢(𝑒𝑢(𝑘)
𝜏,𝛼)
ˆ𝑓𝐵𝐷𝑃𝐿𝐹&𝑒𝑢(𝐵𝐷𝑃𝐿𝐹𝑠(𝑘,𝜏,𝛼)
𝜉𝑚
∪𝑒𝑢(𝑘)
𝜏,𝛼)
(9)
To measure the performance of our approach, we emphasize
on whether the predictive model is able to distinguish a given
user is in a BD onset period or not. To evaluate our model, we
use 10-fold cross validation, and measure the model’s overall
precision and recall. Additionally, a psychiatrist evaluation
is conducted in our work for qualitative analysis.
4
PRODROME RECOGNITION
The definition of the prodrome stage is made below and a
prodrome recognition approach is proposed to locate the
possible prodromal period for BD. The prodromal period
generally refers to the time interval between the onset of the
first prodromal symptom and the onset of the characteristic
signs/symptoms of the fully developed illness.
In order to capture the prodromal period, our approach
is able to reveal the onset probability for each user through
BDOPM. In this step, a week by week sliding window ap-
proach is adopted to construct a bipolar disorder onset time-
line, which presents onset probabilities along time.
Definition 7 (Sliding Window Segmentation). Let a time
segmentation sequence 𝜓(𝑘,𝛼)
𝑞
= {𝑡| 𝑡∈[𝑠(𝑘)
𝑞
−𝛼, 𝑠(𝑘)
𝑞]} be
in ascending order, where 𝑠(𝑘)
𝑞
is the given time for user
𝑘. The objective of the segmentation algorithm is to iter-
ate over 𝜓(𝑘,𝛼)
𝑞
with 𝑠(𝑘)
𝑞
minus 1 week for each iteration
𝑠(𝑘)
𝑄, 𝑠(𝑘)
𝑄−1, . . . , 𝑠(𝑘)
𝑞, . . . , 𝑠(𝑘)
1
and output the user’s time seg-
mentation sequence Ψ(𝑘,𝛼) = {𝜓(𝑘,𝛼)
1
, . . . , 𝜓(𝑘,𝛼)
𝑄
},
6


## Page 7


With a user’s time segmentation set Ψ(𝑘,𝛼), the onset
probability 𝑙(𝑘)
𝑠,𝛼for each time segmentation 𝜓(𝑘,𝛼)
𝑞
can be
represented as 𝑙(𝑘,𝛼)
𝜓𝑞
.
Definition 8 (Bipolar Disorder Onset Timeline). The Bipo-
lar Disorder Onset Timeline consists of a sequence of BD
onset probabilities L(𝑘,𝛼)
Ψ
= {𝑙(𝑘,𝛼)
𝜓𝑞
}.
Definition 9 (Prodromal Period). The prodromal periods
of a user are S(𝑘) = {𝑡| 𝑡∈𝜓(𝑘,𝛼)
𝑞
∪𝜓(𝑘,𝛼)
𝑞+1 ∪, . . .}, 𝑙(𝑘,𝛼)
𝜓𝑞
∈
[𝑙𝑙𝑜𝑤𝑒𝑟, 𝑙𝑢𝑝𝑝𝑒𝑟], where 𝑙𝑙𝑜𝑤𝑒𝑟and 𝑙𝑢𝑝𝑝𝑒𝑟are the lower and upper
bounds, respectively, for no onset and onset probabilities.
Given the bipolar disorder onset timeline and Definition 9
above, our model then infers the prodromal period through
Algorithm 1.
Algorithm 1: Prodromal Period Locating
INPUT L(𝑘,𝛼)
Ψ
and Ψ(𝑘,𝛼);
qualifiedProdrome = new Array() ;
candidateProdrome = ∅;
𝑙𝑙𝑜𝑤𝑒𝑟= not onset probability ;
𝑙𝑢𝑝𝑝𝑒𝑟= onset probability ;
forall BD onset probability 𝑙(𝑘,𝛼)
𝜓
in L(𝑘,𝛼)
Ψ
do
if
𝑙(𝑘,𝛼)
𝜓
between 𝑙𝑙𝑜𝑤𝑒𝑟and 𝑙𝑢𝑝𝑝𝑒𝑟then
candidateProdrome = candidateProdrome ∪𝜓;
else if
𝑙(𝑘,𝛼)
𝜓
> 𝑙𝑢𝑝𝑝𝑒𝑟and Length(
candidateProdrome) > 0 then
qualifiedProdrome append candidateProdrome ;
candidateProdrome = ∅;
end
RETURN qualifiedProdrome ;
5
EXPERIMENTS
5.1
Onset Prediction Performance
5.1.1
Experimental Setup. Time-specific subconscious crowd-
sourcing is applied to collect the dataset. About 10,000 tweet
statements were collected from Twitter and then filtered by
the keywords “diagnosed” and “bipolar” from Oct., 2006 to
Dec., 2016. Owing to the fact that the time of diagnosis could
be expressed in various ways besides natural language pro-
cessing approaches, it was manually labeled when mentioned
in tweets. Moreover, self-diagnosed users were removed to
ensure reliability. After applying the previous filter, 406 users
remained. In order to calibrate the tweet time to the user’s
local time, the users’ timezones and locations, which are
public on Twitter, were also collected. Based on the time of
diagnosis, we collected user tweets between the time of diag-
nosis and one year before. These tweets became our positive
class in the training process. Random samples of users were
obtained using the Twitter Streaming API and REST API,
which then became our negative class in the final training
dataset.
For illness period modeling, the time frame is set to be
𝛼∈{2, 3, 6, 9, 12} months. A dataset is modeled for each 𝛼,
and active user filtering is applied in this step. The dataset
for model evaluation is summarized in Table 1.
Groups
Users
Tweets
Average tweets
Regular (2 months)
260
67485
259
Bipolar (2 months)
133
136837
1028
Regular (3 months)
257
89141
346
Bipolar (3 months)
135
226460
1677
Regular (6 months)
267
136481
511
Bipolar (6 months)
124
353559
2851
Regular (9 months)
289
170380
589
Bipolar (9 months)
117
481392
4114
Regular (12 months)
295
207008
701
Bipolar (12 months)
111
586656
5285
Table 1: The total number of accounts and tweets
for different groups of users and the group of users
after illness period modeling.
The data collection approach, time-specific subconscious
crowdsourcing(TSC), is first compared with the subconscious
crowdsourcing(SC) (Chang et al. [7] 2016). For model per-
formance evaluation, we compare BDOPM with 3 baselines :
(1) PLF approach (Chang et al. [7] 2016) which consisted of
Age and Gender(AG), Social(Soc), Emotion(Emot), and Po-
larity(Pol) features (2) CLM approach(Coppersmith et al.[8]
2014, Chang et al. [7] 2016) (3) LIWC approach (Coppersmith
et al.[8, 12] 2014).
5.1.2
Dataset Collection Approach Comparison. The dif-
ference between the datasets collected by subconscious crowd-
sourcing (SC) and our approach - Time-specific subconscious
crowdsourcing (TSC) is first compared in the experiment.
Two random forest classifiers were built, corresponding to the
CLF for both datasets. With this tree based classifier, the
most frequent words for each dataset were further extracted
and plotted on a word cloud as shown in Fig. 3.
Figure 3: SC Wordcloud
It can be appreciated in Fig. 3 that many frequent words
in SC are part of the terminology of BD symptoms, such as
mania, psych, PTSD, BPD, etc.
7


## Page 8


Figure 4: TSC Wordcloud
On the contrary, in Fig. 4, the most frequent words from
TSC are closer to daily conversation phrases. The data col-
lection for SC is done from users who follow BD-related
fan pages. Consequently, among all users, those followers
are more aware to their mental illness states; hence, they
have higher tendency to share knowledge of BD. It is worth
pointing out that most users were not aware of their mental
status before being diagnosed with BD. The words or phrases
they used were consequently less related to BD symptoms.
As compared to SC, our approach collected user data based
on whether they mentioned being diagnosed with BD or not.
The coverage of our approach is more balanced than that of
TSC, which collects more ordinary people.
5.1.3
Single Category Features Performance for Psycho-
logical and Phonological Features. Each single category in
our proposed features, BDPLF and Phonological features,
are evaluated separately. Among the features, social(Soc)
and mood polarity(Pol) features performed much better at
𝛼= {2, 3} months than during other periods. This implies
that when BD is onset, the mood polarity and social be-
haviors become much more significant. For emotion(Emot)
and phonological(Phon) features, they also perform well at
𝛼= {9, 12}. To further experiment on pure text features,
we not only eliminated the social features, as they funda-
mentally required social interaction, but also removed the
mood polarity(Pol) category, since it requires time interval
information.
For the age and gender(AG) and insomnia(LT) and over-
talking(TRD) features, the major reason for having a lower
performance is that there are less then 3 sub-features in this
category, while the other categories have more. In the next
section, we present further feature ensemble experiments to
examine these features.
5.1.4
Bipolar Disorder Onset Prediction Model Performance.
To compare the performance of the models proposed, we used
10-fold cross validation to measure the overall precision and
recall. To assess and interpret the performance of each clas-
sification model and each selected time period, the overall
performance is summarized in Table 3. In general, all of the
ensemble features performed well in the onset detection task.
The ensemble of Phonological features and BPLF, which is
the integration of our proposed features with BD-customized
features from original Pattern of Life(PLF), performed the
Features(#DIM) 2 mths 3 mths 6 mths 9 mths 12 mths
AG(2)
0.475
0.503
0.445
0.434
0.383
Pol(5)
0.911
0.893
0.843
0.836
0.803
Emot(8)
0.893
0.895
0.908
0.917
0.896
Soc(4)
0.941
0.913
0.845
0.834
0.786
LT(1)
0.645
0.589
0.554
0.504
0.513
TRD(1)
0.570
0.638
0.626
0.615
0.654
Phon(8)
0.889
0.880
0.802
0.838
0.821
Table 2: Average Precision of Single Feature Perfor-
mance
best. This ensemble successfully captured the BD features
in phonological patterns and user engagement (Soc) metrics,
besides the sentiment and emotions portrayed in user tweets.
The CLM had a lower performance based on what was dis-
cussed in the previous section. That is, when dealing with
unaware patients, the classifier is not able to recognize BD.
Similarly, the LIWC model only depends on psychological
words and does not offer enough information in order to
detect BD.
As can be seen in Table 3, the models trained on three
months of user data performed the best, which also indicates
that BD features are more obvious when the time period is 2
to 3 months before diagnosis. Rapid cycling bipolar disorder,
from DSM-IV, is defined as a pattern of presentation accom-
panied by 4 or more mood episodes in a 12-month period,
with a typical course of mania or hypomania followed by
depression or vice versa. These episodes must be demarcated
by a full or partial remission lasting at least 2 months or
by a switch to a mood state of opposite polarity[2]. These 2
to 3 month periods also match clinical observations, which
indicates that our model and dataset have a high reliability.
Without taking all of the user data into consideration,
the model was able to perform well even when dealing with
short-time data. Furthermore, this 2–3 month time period
is considered to be the best size for a time-frame of BD
prodrome detection. We thus set the time frame to 𝛼= 2
months.
The pure text model is further evaluated in this step. The
goal of this experiment is to provide foresight for the potential
patterns in human natural expressions. In this experiment,
age and gender(AG), emotion(Emot), and phonological(Phon)
features are treated in ensemble as pure text features and
we construct a predictive model through them. The LIWC
features and CLF are not considered as pure text features,
because they already have a high dimension of features, which
are 64 and over 1000 dimensions.
The performance of the pure text ensemble model is shown
in the bottom of Table 3. It can be observed in the table that
the model reaches an average precision near to 0.9 without
phonological features. With the involvement of phonological
features, the performance of the model improved by 7% and
reached around 0.96 when the time frame was 𝛼= {2, 3},
which is almost competitive with the social involved model.
8


## Page 9


Features (#DIM)
2 mths 3 mths 6 mths 9 mths 12 mths
LIWC(64)
0.430
0.391
0.377
0.403
0.372
CLF(1000+)
0.934
0.927
0.866
0.840
0.809
PLF(19)
0.977
0.979
0.967 0.975
0.967
LT+PLF(20)
0.976
0.981
0.965
0.971
0.960
TRD+PLF(20)
0.978
0.978 0.971 0.977
0.961
BDPLF(21)
0.981
0.981
0.968
0.973
0.970
Phon+PLF(27)
0.977 0.985 0.966
0.974
0.961
Phon+LT+PLF(28)
0.976
0.982
0.964
0.972
0.962
Phon+TRD+PLF(28) 0.983 0.983 0.971 0.964
0.958
Phon+BDPLF(29)
0.984 0.983 0.969
0.968
0.965
Emot+AG(10)
0.904
0.904
0.873
0.909
0.885
Emot+Phon(18)
0.948
0.947
0.935
0.938
0.924
Emot+AG+Phon(20) 0.950
0.950
0.937
0.940
0.917
Table 3: Average Precision of Model Performance
Moreover, the pure text model is also valuable because of
the efforts reduced in processing steps and data collection
with little performance loss for the BD onset detection task.
Generally, each classifier for each time period performed
better as the dataset segmentation was closer to the time of
diagnosis, especially for the CLM. For this classifier, Figure 5
shows that the average precision moved from 0.809 to 0.934
as the time frame 𝛼moved from 12 months to 2 months.
Figure 5: Average Precision Curve (CLM)
The improved performance from time to time indicates
that for the same group of regular and BD users, the word
expression feature changes differently. Words and phrases in
the CLM reflect the linguistic styles of BD and regular users,
which provides useful information about how BD patients are
responding with respect to their mental state. For instance,
in Figure 4, besides the negative words that reveal a negative
state for a BD user, we are able to infer that he/she is getting
overwhelmed in the life, which is one of the symptoms of BD.
Figure 6: Bipolar Disorder Onset Timeline
Based on the classifier, we segment user social data based
on the time dimension in sliding windows approach and pre-
dict the BD onset probability for each segment. The prodrome
filter approach can detect the signs of initial prodrome. For
example, Figure 6 is one of the results, the boxed periods are
the most possible initial prodromal periods identified by the
proposed technique.
5.2
Psychologist Evaluation
In this experiment, 90 samples of user social behaviors are
extracted, where each time period lasts for 2 months. Among
these 90 samples, 1/3 are classified as onset by BDOPM, 1/3
are classified as no-onset by BDOPM, and 1/3 are extracted
from regular user behaviors and classified as no-onset. A web
interface is provided to visualize these data. 8 psychologists
are involved in the blind-test experiment to assign assess-
ments (i.e., having BD symptoms or not) to those samples.
Each sample is assessed by more than three psychologists.
Agreement Onset BD Not Onset BD Not Onset Regular
Majority
0.429
1.00
1.00
One Onset
0.815
0.857
0.926
Table 4: Accuracy for Agreement Evaluation
Onset BD
Not Onset BD
Not Onset Regular
0.37
0.45
0.75
Table 5: Agreement Rates between Psychologists
Table 4 demonstrates that BDOPM achieves high accuracy
in most cases. For majority agreement, the accuracy of BD
onset prediction is 0.429 owing to the various diagnosed
standards among the psychologists. Table 5 shows that only
37% of onset data among the opinions from the psychologists
obtain exactly the same labels. This could be due to that the
same symptom is found in many kinds of illness.
Nearly half of the patients with BD have major depres-
sion, while roughly one-quarter to one-third of them are
9


## Page 10


diagnosed as borderline personality disorder, post-traumatic
stress disorder (PTSD), generalized anxiety, and social phobia
were each diagnosed in roughly one-quarter to one-third [23].
Burgess [4] also indicates there are almost 70% of BD patients
have been misdiagnosed more than 3 times before receiving
their correct diagnosis. Due to the similarity of symptoms
shared by several mental disorders, chances of the majority of
the psychologists agree the user as BD are low under the con-
dition that based only on the text without a comprehensive
diagnostic interview. Therefore, we give a relaxing criterion
that the user is considered as BD if one of the psychologists
agree that the user is BD.
Under this relaxing criterion, the users that have never
been diagnosed BD may exhibit BD-like behaviors, such as
over-talk, anxiety, or struggle with the negative or angry
experiences.
In summary, from different types of data, our model is
able to distinguish the possible onset behavior and reach a
high precision under the relaxing criterion.
6
CONCLUSION
In this research, time-specific subconscious crowdsourcing, a
novel data collection approach is proposed, which is capable
to filter out not only highly self-aware but also general BD
users on social media. With this approach, the time spent
on diagnosis of illness could also be the key to identify the
possible signs of the initial prodrome. The result shows that
the pattern of life features combined with our extending
features, e.g., insomnia and over-talk feature, provide a great
performance on detecting the BD onset period.
Furthermore, we introduce a novel phonological feature,
which focuses on the energy of words based on the evidence
of phonology. By simply employing phonological feature with
pure text ensemble model (i.e., the model without any social
media features), the classifier can achieve more than 91%
precision. The proposed model also has achieve high accuracy
in the onset detection task.
The time influence-CLM indicates that the word choices of
users can reflect the corresponding mental states. With this
observation, it increases the possibility to perform regular
assessment on people based on the simple writing.
REFERENCES
[1] Carlos Argueta, Elvis Saravia, and Yi-Shin Chen. 2015. Unsuper-
vised graph-based patterns extraction for emotion classification. In
Advances in Social Networks Analysis and Mining (ASONAM),
2015 IEEE/ACM International Conference on. IEEE, 336–341.
[2] American Psychiatric Association et al. 2013. Diagnostic and
statistical manual of mental disorders (DSM-5®). American
Psychiatric Pub.
[3] International Phonetic Association. [n. d.]. International Phonetic
Alphabet. ([n. d.]). https://www.internationalphoneticassociation.
org
[4] Melody Ballard. 2006. The bipolar handbook: Real-life questions
with up-to-date answers. (2006).
[5] M Berk, S Dodd, P Callaly, L Berk, P Fitzgerald, AR De Castella,
S Filia, K Filia, S Tahtalian, F Biffin, et al. 2007. History of
illness prior to a diagnosis of bipolar disorder or schizoaffective
disorder. Journal of affective disorders 103, 1 (2007), 181–186.
[6] Miloš Cerňak, Štefan Beňuš, and Alexandros Lazaridis. 2017.
Speech vocoding for laboratory phonology. Computer Speech &
Language 42 (2017), 100–121.
[7] Chun-Hao Chang, Elvis Saravia, and Yi-Shin Chen. 2016. Subcon-
scious Crowdsourcing: A feasible data collection mechanism for
mental disorder detection on social media. In Advances in Social
Networks Analysis and Mining (ASONAM), 2016 IEEE/ACM
International Conference on. IEEE, 374–379.
[8] Glen Coppersmith, Mark Dredze, and Craig Harman. 2014. Quan-
tifying mental health signals in Twitter. In Proceedings of the
Workshop on Computational Linguistics and Clinical Psychol-
ogy: From Linguistic Signal to Clinical Reality. 51–60.
[9] Glen Coppersmith, Mark Dredze, Craig Harman, and Kristy
Hollingshead. 2015. From ADHD to SAD: Analyzing the Language
of Mental Health on Twitter through Self-Reported Diagnoses..
In CLPsych@ HLT-NAACL. 1–10.
[10] Munmun De Choudhury, Michael Gamon, Scott Counts, and Eric
Horvitz. 2013. Predicting Depression via Social Media. ICWSM
13 (2013), 1–10.
[11] Alec Go, Richa Bhayani, and Lei Huang. 2009. Twitter sentiment
classification using distant supervision. CS224N Project Report,
Stanford 1, 2009 (2009), 12.
[12] Glen A Coppersmith Craig T Harman and Mark H Dredze. 2014.
Measuring post traumatic stress disorder in Twitter. In ICWSM
(2014).
[13] Oliver D Howes, Samuel Lim, George Theologos, Alison R Yung,
Guy M Goodwin, and Philip McGuire. 2011. A comprehensive re-
view and model of putative prodromal features of bipolar affective
disorder. Psychological medicine 41, 8 (2011), 1567–1577.
[14] Megan A Moreno, Lauren A Jelenchick, Katie G Egan, Elizabeth
Cox, Henry Young, Kerry E Gannon, and Tara Becker. 2011. Feel-
ing bad on Facebook: Depression disclosures by college students
on a social networking site. Depression and anxiety 28, 6 (2011),
447–455.
[15] Minsu Park, Chiyoung Cha, and Meeyoung Cha. 2012. Depres-
sive moods of users portrayed in Twitter. In Proceedings of the
ACM SIGKDD Workshop on healthcare informatics (HI-KDD),
Vol. 2012. ACM New York, NY, 1–8.
[16] James W Pennebaker, Roger J Booth, and Martha E Francis.
2007. LIWC2007: Linguistic inquiry and word count. Austin,
Texas: liwc. net (2007).
[17] Lenore Sawyer Radloff. 1977. The CES-D scale: A self-report
depression scale for research in the general population. Applied
psychological measurement 1, 3 (1977), 385–401.
[18] MK Sahoo, S Chakrabarti, and P Kulhara. 2012. Detection of
prodromal symptoms of relapse in mania & unipolar depression
by relatives & patients. The Indian journal of medical research
135, 2 (2012), 177.
[19] Maarten Sap, Gregory Park, Johannes Eichstaedt, Margaret Kern,
David Stillwell, Michal Kosinski, Lyle Ungar, and Hansen Andrew
Schwartz. 2014.
Developing age and gender predictive lexica
over social media. In Proceedings of the 2014 Conference on
Empirical Methods in Natural Language Processing (EMNLP).
1146–1151.
[20] Pilar Sierra, Lorenzo Livianos, Sergio Arques, Javier Castelló,
and Luis Rojo. 2007. Prodromal symptoms to relapse in bipolar
disorder. Australian & New Zealand Journal of Psychiatry 41,
5 (2007), 385–391.
[21] Dorothy Sit. 2004. Women and bipolar disorder across the life
span. Journal of the American Medical Women’s Association
(1972) 59, 2 (2004), 91.
[22] Anna R Van Meter, Coty Burke, Eric A Youngstrom, Gianni L
Faedda, and Christoph U Correll. 2016. The bipolar prodrome:
meta-analysis of symptom prevalence prior to initial or recurrent
mood episodes. Journal of the American Academy of Child &
Adolescent Psychiatry 55, 7 (2016), 543–555.
[23] Mark Zimmerman, Camilo J Ruggero, Iwona Chelminski, and
Diane Young. 2010. Psychiatric diagnoses in patients previously
overdiagnosed with bipolar disorder.
The Journal of clinical
psychiatry 71, 1 (2010), 26–31.
10

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]