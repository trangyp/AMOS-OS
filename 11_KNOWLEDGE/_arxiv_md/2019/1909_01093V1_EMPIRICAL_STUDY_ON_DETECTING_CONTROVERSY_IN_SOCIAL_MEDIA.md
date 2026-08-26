---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.01093v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1909.01093v1_Empirical_Study_on_Detecting_Controversy_in_Social_Media

> Source: 1909.01093v1_Empirical_Study_on_Detecting_Controversy_in_Social_Media.pdf

> Pages: 4

---


## Page 1


arXiv:1909.01093v1  [cs.SI]  25 Aug 2019
Empirical Study on Detecting Controversy in Social Media∗
Azadeh Nematzadeh†
S&P Global
New York, NY, USA
azadeh.nematzadeh@spglobal.com
Grace Bang†
S&P Global
New York, NY, USA
grace.bang@spglobal.com
Xiaomo Liu†
S&P Global
New York, NY, USA
xiaomo.liu@spglobal.com
Zhiqiang Ma†
S&P Global
New York, NY, USA
zhiqiang.ma@spglobal.com
ABSTRACT
Companies and ﬁnancial investors are paying increasing attention
to social consciousness in developing their corporate strategies
and making investment decisions to support a sustainable econ-
omy for the future. Public discussion on incidents and events—
controversies—of companies can provide valuable insights on how
well the company operates with regards to social consciousness
and indicate the company’s overall operational capability. How-
ever, there are challenges in evaluating the degree of a company’s
social consciousness and environmental sustainability due to the
lack of systematic data. We introduce a system that utilizes Twit-
ter data to detect and monitor controversial events and show their
impact on market volatility. In our study, controversial events are
identiﬁed from clustered tweets that share the same 5W terms and
sentiment polarities of these clusters. Credible news links inside
the event tweets are used to validate the truth of the event. A case
study on the Starbucks Philadelphia arrests shows that this method
can provide the desired functionality.
KEYWORDS
Social Media Mining, Controversy Detection, Market Performance
1
INTRODUCTION
The ﬁnancial performance of a corporationis correlated with its so-
cial responsibility such as whether their products are environmen-
tally friendly, manufacturing safety procedures protect against ac-
cidents, or they use child labors in its third world country factories.
Consumers care about these factors when making purchasing deci-
sions in the supermarkets and investors integrate environmental,
social and governance factors, known as ESG1, in their investment
decision-making. It has been shown that corporations ﬁnancial re-
sults have a positive correlation with their sustainability business
model and the ESG investment methodology can help reduce port-
folio risk and generate competitive returns2. However, one barrier
for ESG evaluation is the lack of relatively complete and central-
ized information source. Currently, ESG analysts leverage ﬁnan-
cial reports to collect the the necessary data for proper evaluation
∗This work is accepted and presented in the 2nd KDD Workshop on Anomaly Detec-
tion in Finance, August 5, 2019, Anchorage, Alaska, USA.
†The authors contributed equally to this work, listed in the alphabetical order.
1https://www.spglobal.com/en/capabilities/esg-evaluation
2https://www.forbes.com/sites/georgkell/2018/07/11/the-remarkable-rise-of-esg
such as greenhouse gas emissions or discrimination lawsuits, but
this data is inconsistent and latent. In this study, we consider social
media a crowdsourcing data feed to be a new data source for this
task.
Social media applications such as Twitter oﬀer users a platform
to share and disseminate almost any content about various events
such as sports, music, and controversial events as well. The content
produced through these platforms not only facilitates the spread of
information but can also provides meaningful signals about the in-
ﬂuence of the events. A large number of responses to an issue on
Twitter could inform the public about the signiﬁcance of an event,
widen the scope of the event, and bring more public attention in-
side and outside the social media circle.
We deﬁne a controversial event for a business entity as a cred-
ible and newsworthy incident that has the potential to impact an
entity in its ﬁnancial performance and operation, for example, an
incident caused by an employee or a representative of the entity
that has the potential to hurt the trust of the public to its brand.
Such an incident can demonstrate a potential gap in its risk man-
agement framework and policy execution, and eventually hurt the
interest and trust of its stakeholders’.
Controversial events trigger a large cascade of discussion on so-
cial media platforms. The broad connectivity between people prop-
agates their opinions into trending topics that could eﬀect the com-
pany ﬁnancially and operationally. In certain cases, the responsible
entity can be forced to take actions, e.g., to recall its product, which
can impose a large ﬁnancial burden on the entity. For instance, in
the Takata air bag scandal, the event was discussed widely on Twit-
ter after the New York Times published a comprehensive article on
its defective air bag products in 2014. Takata was forced to recall
nearly 50 million air bag and ﬁled bankruptcy in June 2017.
To this end, we propose a controversial event detection system
utilizing Twitter data. We focus on controversial events which are
credible and newsworthy. Twitter data were collected on a given
company and various attributes of each tweet were extracted. We
verify the credibility of the event by validating the URLs appear-
ing in tweets come from credible news sources. We utilize tweets
attributes to detect events speciﬁc to the given company and the
sentiment of the event to measure the controversy. Relationship
between a burst of an entity controversial event and the entity mar-
ket performance data was qualitatively assessed in our case study,
where we found its potential impact on the equity value.


## Page 2


Azadeh Nematzadeh, Grace Bang, Xiaomo Liu, and Zhiqiang Ma
2
RELATED WORK
There have been a few studies on assessing sustainability of enti-
ties. The UN Commission on Sustainable Development (CSD) pub-
lished a list of about 140 indicators on various dimensions of sus-
tainability [3]. In [5], Singh et al. reviewed various methodolo-
gies, indicators, and indices on sustainability assessment, which
includes environmental and social domains. All the data, on which
the assessments were conducted, mentioned in their works are pro-
cessed datasets, and some of them are collected from company an-
nual reports and publications, newspaper clips, and management
interviews. They stated that the large number of indicators or in-
dices raises the need of data collection. Our work uses the social
media data as a new alternative data source to complement the
traditional data collection.
Event detection on social media has been a popular research
topic for years. Reuters Tracer [2] is reported as an application
built for the journalists to detect news leads in Twitter before the
news becomes known to the public. Petrovic et al. [4] presented
a locality-sensitive hashing based ﬁrst story detection algorithm
with a new variance reduction strategy to improve the performance.
In [6], the signal of a tweet word is built with wavelet analysis
and a event is detected by clustering words with similar signal pat-
terns of burst. [1] describes a detection and analysis system named
TEDAS which concentrates on Crime and Disaster related Events
(CDE). TEDAS classiﬁes if a tweet is a CDE tweet, predicts its geo-
location if missing, and ranks and returns important tweets when
user queries in the system. TEDAS treats a tweet as an event if the
tweet qualiﬁes, while our deﬁnition of an event is diﬀerent, where
an event is a group of tweets discussing a same theme.
3
CONTROVERSY DETECTION IN SOCIAL
MEDIA
In this section, we describe the main components of our contro-
versy detection system.
3.1
Data collection
The system uses Twitter’s ﬁltered streaming API to collect rele-
vant tweets data. The data collection pipeline accepts a comma-
separated list of phrases as ﬁltering parameters, that the API uses
to determine which tweets will be retained from the stream. Once
the system receives data from the API, it then separates postings
by companies and runs the downstream process on the separated
data streams individually.
3.2
Feature engineering
The data collection pipeline collects tweet postings for a given en-
tity. For each incoming posting, the system also stores the follow-
ing attributes: posting_id, creation_time, text, language, source, URLs,
and hashtags.
The system parses the text attributeof each tweet. Part-of-speech
(POS) tagging and named entity recognition (NER) algorithm are
applied to each tweet and terms that are tagged as proper nouns,
verbs, and entities are stored. If two proper nouns are next to each
other, the system merges them as one proper noun phrase. Enti-
ties such as person names, organizations, locations from tweets
are the key elements in describing an event and distinguishing it
from other events, and are often used by news professionals to de-
scribe the complete story of an event. The verbs from POS tagging
mainly represent what and why information, while NER helps to
identify where, when, and who information. They capture the ma-
jor aspects of an event, named who, what, where, when, and why
(5W). Besides that, the sentiment of each tweet is assessed too.
The system crawls the URLs in a posting and veriﬁes whether
the link comes from one or more credible news sources. More specif-
ically, the system may consider the following to be examples of
credible news sources: 1) a news outlet that has, and consistently
applies, journalistic standards in its reporting or 2) an authoritative
government agency not acting in a political capacity. Determining
whether a source is a credible news source depends on the context
of the event.
Based on all the extracted features, the system can build a tweet
vector, which includes the following features: tweet id, creation
time, source, hashtags, entity/proper nouns, verbs, sentiment, and
news links.
3.3
Event detection
When a new tweet is received in the data pipeline, it either forms a
new cluster or it will be added to an existing cluster. A new tweet
will be added to an existing cluster if it is suﬃciently similar to one
of the existing clusters based on its distance to the cluster average
vector. If more than one cluster is applicable, the cluster that has
the highest similarity to the new tweet is picked. If a new tweet
is not added to any existing clusters, it would form a new cluster.
A candidate event is a cluster that has at least ﬁve tweets. Algo-
rithm 1 summarizes our event detection method and the following
controversy identiﬁcation method.
3.4
Controversy identiﬁcation
An event can be controversial if the public expresses dissenting
opinions, usually associated with negative sentiments to it. The
system ﬁlters out irrelevant events and noise from the established
controversial events using the following metrics:
• The burstiness of an event: To detect the burstiness of an
event, the system detects the volume of tweets per time pe-
riod, e.g., per day, for the entity in question. An event is
ﬂagged when the velocity of the volume increase exceeds a
threshold.
• Newsworthiness detection: The system counts the total num-
ber of unique veriﬁed news links in each cluster and log that
count as a newsworthiness metric.
• Sentiment: For each cluster, its overall sentiment score is
quantiﬁed by the mean of the sentiment scores among all
tweets.
Candidate events are ranked based on these metrics, and high ranked
events are considered controversial events.
4
CASE STUDY - STARBUCKS CONTROVERSY
In this section, we provide a case study of our model on a Starbucks
controversial event captured in the system. We validated the event


## Page 3


Empirical Study on Detecting Controversy in Social Media
Figure 1: Event clusters and the sentiment polarity score along the timeline.
Algorithm 1 Outline of the controversy detection algorithm
Require: Tx = {t1, ...,tn} is a stream of tweets about company x
1: procedure Controversy(Tx)
2:
for each t ∈Tx do
⊲(event detection)
3:
f (t) ←TweetFeature(t)
4:
Dt ←∅
5:
for each ei ∈E do
⊲E current event clusters
6:
f (e) ←ClusterFeature(E)
7:
dt(i) ←Distance(t,ei)
⊲compute distance
8:
Dt ←{Dt ,dt (i)}
9:
end for
10:
i ←argmini(Dt )
⊲ﬁnd the closet cluster i
11:
if dt(i) < D then
⊲D is merge threshold
12:
merge t in ei
13:
else
14:
E ←{E, {t}}
⊲{t} is singleton cluster
15:
end if
16:
end for
17:
E ←{ei |l(ei) > N,ei ∈E}
⊲N is min cluster size as
event
18:
for each ei ∈E do
⊲(controversy identiﬁcation)
19:
B(ei) ←Bustiness(ei)
20:
N (ei) ←Newsworthiness(ei)
21:
for each t ∈ei do
22:
S(t) ←SentimentClassify(t)
23:
end for
24:
S(ei) ←AVG(S(t))
⊲compute event level sentiment
25:
C ←S(ei) < 0 ∧B(ei) ∧N (ei)
⊲combined
controversy score
26:
end for
return C
⊲C is controversial events set
27: end procedure
with the Wikipedia page of Starbucks3 and the major new agen-
cies reports. After the event was detected, its impact was further
assessed by linking to the market equity data.
On April 12th, 2018, an incident occurredin a Starbucks in Philadel-
phia, PA. Two African-American men were arrested by the police
oﬃcials inside that Starbucks. It was reported that the two were
denied to access the restroom by the store staﬀbecause they did
not make any purchase. While waiting at the table, they were told
by the staﬀto leave as they were not making any purchase. They
did not comply and thus the store manager called the police and
reported that they are trespassing. The two were arrested by the
oﬃcials but released afterwards without any pressed charges. The
scene of the arresting was posted on Twitter and quickly garnered
public attention. The video had been viewed more than three mil-
lions times in a couple of days and the major local and national
news agencies like CNN, NPR, and NYTIMES followed the devel-
opment of the story.
The public outrage originating from the social media universe
swiftly triggered a series of chain reaction in the physical world.
Protesters gathered together inside and outside the Starbucks store
to demand the manager be ﬁred. Several days later, the CEO of the
Starbucks issued a public apology for the incident on an ABC’s
program and stated that he would like to meet the men to show
them compassion. To remedy the bad outcome of the event, Star-
bucks closed its 8,000 stores in the U.S. on May 29th for racial-bias
training for its 175K employees. A ﬁnancial settlement was also
established between the two men and Starbucks corporation. This
event garnered a serious public relations crisis for Starbucks.
Figure 1 shows the event clusters for six days sampled between
April 10th and April 20th. Given the diﬃculty in showing all of the
tweets that were clustered, we use the volume of key POS tagged
words (5Ws) detected in the cluster of tweets to approximate the
3https://en.wikipedia.org/wiki/Criticism_of_Starbucks#Philadelphia_arrests


## Page 4


Azadeh Nematzadeh, Grace Bang, Xiaomo Liu, and Zhiqiang Ma
Figure 3: Histogram of Starbucks stock price daily changes
Figure 2: Starbucks stock price and NASDAQ index between
April 11th 2018 and April 20th 2018.
event content. The keywords on the top of each bar reveal aspects
of the event cluster. This controversial Starbucks event was cap-
tured in our system on April 13th, one day after the event occurred.
Prior to the event, the discussion themes about Starbucks (clusters)
on Twitter were more random and included topics such as Star-
bucks gift card, barista, coﬀee as shown on 04/11/2018. The size of
the clusters and the total volume of the tweets per day is compa-
rably small. The ﬁrst event cluster the system detected associates
with the keyword ‘black’, where twitter users mentioned ‘[...] ar-
rested for being Black’. After the event, the volume of the tweets
per day surged multiple times more than before and kept climbing
for about a week as the event was developing. The system clearly
uncovers the events by being able to pinpoint the clustering key-
words ‘black men’, ‘philly’, ‘CEO’, ‘close’, etc. The sentiment scores
of the discussion in the clusters for each day are shown on the top
part of Figure 1. The sentiment score is in a range of -2 to +2, -2
standing for very negative, 0 for neutral, and +2 for very positive.
As the ﬁgure shows, twitter users’ attitude turned from neutral to
negative post the Starbucks event occurrence. The quick turn of
sentiment polarity serves as an measurement of the event being
controversy. Through the validation of the domain of the URLs
quoted in the clustered tweets, the authentication of the event is
veriﬁed. All of the elements of this event indicate that a contro-
versy, speciﬁcally, a social related controversy, has occurred.
We also did a qualitative study on the Starbucks (SBUX) stock
movement during this event. Figure 2 is the daily percentage change
of SBUX and NASDAQ index between April 11th and April 20th.
SBUX did not follow the upward trend of the whole market before
April 17th, and then its change on April 20th, −1.7%, is quite sig-
niﬁcant from historical norms. We collected the historical 52 week
stock prices prior to this event and calculated the daily stock price
change. The distribution of the daily price change of the previous
52 weeks is Figure 3 with a mean µ = 4.9e −5 and standard de-
viation σ = 0.0091. The 1.7% down almost equals to two standard
deviations below the mean. Our observation is that plausibly, there
was a negative aftereﬀect from the event of the notable decline in
Starbucks stock price due to the major public relations crisis.
5
CONCLUSIONS
We present the use of Twitter as a new data source to detect con-
troversial events for business entities. Each tweet is represented by
a vector comprising name entities and verbs mentioned in the raw
tweet text. Events can be identiﬁed by grouping similar tweets in
the vector space, the size and burstiness of the event, and the senti-
ment polarities. This system is a data-driven controversy monitor-
ing tool that sifts through large volumes of Twitter data. It provides
investors with data on key insights on social consciousness, which
allows investors to make more informed investment decisions. The
direction of our future work is to: 1) develop a quantitative mea-
sure on the event impact on the equity market; 2) identify the rel-
evance of the events to entities’ operations; 3) extract post-event
mitigation actions from the entities.
REFERENCES
[1] R. Li, K. H. Lei, R. Khadiwala, and K. C. Chang. 2012. TEDAS: A Twitter-based
Event Detection and Analysis System. In 2012 IEEE 28th International Conference
on Data Engineering. 1273–1276.
[2] Xiaomo Liu, Quanzhi Li, Armineh Nourbakhsh, Rui Fang, Merine Thomas, Ka-
jsa Anderson, Russ Kociuba, Mark Vedder, Steven Pomerville, Ramdev Wudali,
Robert Martin, John Duprey, Arun Vachher, William Keenan, and Sameena Shah.
2016. Reuters Tracer: A Large Scale System of Detecting & Verifying Real-Time
News Events from Twitter. In Proceedings of the 25th ACM International on Confer-
ence on Information and Knowledge Management (CIKM ’16). ACM, Indianapolis,
Indiana, USA, 207–216.
[3] The UN Commission on Sustainable Development (CSD). 2007.
Indica-
tors of Sustainable Development: Guidelines and Methodologies, Third Ed.
https://sustainabledevelopment.un.org/content/documents/guidelines.pdf
[4] Saša Petrović, Miles Osborne, and Victor Lavrenko. 2010. Streaming First Story
Detection with Application to Twitter. In The 2010 Annual Conference of the North
American Chapter of the Association for Computational Linguistics (HLT ’10). As-
sociation for Computational Linguistics, Stroudsburg, PA, USA, 181–189.
[5] Rajesh Kumar Singha, H.R. Murty, S.K. Gupta, and A.K. Dikshit. 2009.
An
overview of sustainability assessment methodologies. Ecological Indicators 9, 2
(2009), 189–212.
[6] Jianshu Weng and Bu-Sung Lee. 2011. Event Detection in Twitter. In International
AAAI Conference on Web and Social Media. 401–408.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]