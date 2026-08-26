---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1610.03452v5
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1610.03452v5_Kek__Cucks__and_God_Emperor_Trump__A_Measurement_Study_of_4chan_s_Politically_In

> Source: 1610.03452v5_Kek__Cucks__and_God_Emperor_Trump__A_Measurement_Study_of_4chan_s_Politically_In.pdf

> Pages: 15

---


## Page 1


Kek, Cucks, and God Emperor Trump: A Measurement Study of
4chan’s Politically Incorrect Forum and Its Effects on the Web∗
Gabriel Emile Hine‡, Jeremiah Onaolapo†, Emiliano De Cristofaro†, Nicolas Kourtellis♯,
Ilias Leontiadis♯, Riginos Samaras⋆, Gianluca Stringhini†, Jeremy Blackburn♯
‡Roma Tre University
†University College London
♯Telefonica Research
⋆Cyprus University of Technology
gabriel.hine@uniroma3.it, {j.onaolapo,e.decristofaro,g.stringhini}@cs.ucl.ac.uk,
{nicolas.kourtellis,ilias.leontiadis,jeremy.blackburn}@telefonica.com, ri.samaras@edu.cut.ac.cy
Abstract
The discussion-board site 4chan has been part of the Internet’s
dark underbelly since its inception, and recent political events
have put it increasingly in the spotlight. In particular, /pol/,
the “Politically Incorrect” board, has been a central ﬁgure in
the outlandish 2016 US election season, as it has often been
linked to the alt-right movement and its rhetoric of hate and
racism. However, 4chan remains relatively unstudied by the
scientiﬁc community: little is known about its user base, the
content it generates, and how it affects other parts of the Web.
In this paper, we start addressing this gap by analyzing /pol/
along several axes, using a dataset of over 8M posts we col-
lected over two and a half months. First, we perform a general
characterization, showing that /pol/ users are well distributed
around the world and that 4chan’s unique features encourage
fresh discussions. We also analyze content, ﬁnding, for in-
stance, that YouTube links and hate speech are predominant
on /pol/. Overall, our analysis not only provides the ﬁrst mea-
surement study of /pol/, but also insight into online harassment
and hate speech trends in social media.
1
Introduction
The Web has become an increasingly impactful source for new
“culture” [4], producing novel jargon, new celebrities, and dis-
ruptive social phenomena. At the same time, serious threats
have also materialized, including the increase in hate speech
and abusive behavior [7, 20]. In a way, the Internet’s global
communication capabilities, as well as the platforms built on
top of them, often enable previously isolated, and possibly os-
tracized, members of fringe political groups and ideologies to
gather, converse, organize, as well as execute and spread their
agenda [28].
Over the past decade, 4chan.org has emerged as one of the
most impactful generators of online culture. Created in 2003
by Christopher Poole (aka ‘moot’), and acquired by Hiroyuki
Nishimura in 2015, 4chan is an imageboard site, built around a
∗A shorter version of this paper appears in the Proceedings of the 11th In-
ternational AAAI Conference on Web and Social Media (ICWSM’17). Please
cite the ICWSM’17 paper. Corresponding author: blackburn@uab.edu.
typical discussion bulletin-board model. An “original poster”
(OP) creates a new thread by making a post, with a single
image attached, to a board with a particular interest focus.
Other users can reply, with or without images, and add ref-
erences to previous posts, quote text, etc. Its key features in-
clude anonymity, as no identity is associated with posts, and
ephemerality, i.e., threads are periodically pruned [6]. 4chan
is a highly inﬂuential ecosystem: it gave birth not only to sig-
niﬁcant chunks of Internet culture and memes,1 but also pro-
vided a highly visible platform to movements like Anonymous
and the alt-right ideology. Although it has also led to posi-
tive actions (e.g., catching animal abusers), it is generally con-
sidered one of the darkest corners of the Internet, ﬁlled with
hate speech, pornography, trolling, and even murder confes-
sions [17]. 4chan also often acts as a platform for coordi-
nating denial of service attacks [2] and aggression on other
sites [1]. However, despite its inﬂuence and increased media
attention [5, 16], 4chan remains largely unstudied, which mo-
tivates the need for systematic analyses of its ecosystem.
In this paper, we start addressing this gap, presenting a lon-
gitudinal study of one sub-community, namely, /pol/, the “Po-
litically Incorrect” board. To some extent, /pol/ is considered
a containment board, allowing generally distasteful content –
even by 4chan standards – to be discussed without disturbing
the operations of other boards, with many of its posters sub-
scribing to the alt-right and exhibiting characteristics of xeno-
phobia, social conservatism, racism, and, generally speaking,
hate. We present a multi-faceted, ﬁrst-of-its-kind analysis of
/pol/, using a dataset of 8M posts from over 216K conver-
sation threads collected over a 2.5-month period. First, we
perform a general characterization of /pol/, focusing on post-
ing behavior and on how 4chan’s unique features inﬂuence the
way discussions proceed. Next, we explore the types of con-
tent shared on /pol/, including third-party links and images, the
use of hate speech, and differences in discussion topics at the
country level. Finally, we show that /pol/’s hate-ﬁlled vitriol
is not contained within /pol/, or even 4chan, by measuring its
effects on conversations taking place on other platforms, such
1For readers unfamiliar with memes, we suggest a review of the documentary
available at https://www.youtube.com/watch?v=dQw4w9WgXcQ.
1
arXiv:1610.03452v5  [cs.SI]  1 Oct 2017


## Page 2


as YouTube, via a phenomenon called “raids.”
Contributions. In summary, this paper makes several con-
tributions. First, we provide a large scale analysis of /pol/’s
posting behavior, showing the impact of 4chan’s unique fea-
tures, that /pol/ users are spread around the world, and that,
although posters remain anonymous, /pol/ is ﬁlled with many
different voices. Next, we show that /pol/ users post many links
to YouTube videos, tend to favor “right-wing” news sources,
and post a large amount of unique images. Finally, we pro-
vide evidence that there are numerous instances of individual
YouTube videos being “raided,” and provide a ﬁrst metric for
measuring such activity.
Paper Organization. The rest of the paper is organized as fol-
lows. Next section provides an overview of 4chan and its main
characteristics, then, Section 3 reviews related work, while
Section 4 discusses our dataset. Then, Section 5 and Section 6
present, respectively, a general characterization and a content
analysis of /pol/. Finally, we analyze raids toward other ser-
vices in Section 7, while the paper concludes in Section 8.
2
4chan
4chan.org is an imageboard site. A user, the “original poster”
(OP), creates a new thread by posting a message, with an im-
age attached, to a board with a particular topic. Other users
can also post in the thread, with or without images, and refer
to previous posts by replying to or quoting portions of it.
Boards. As of January 2017, 4chan features 69 boards, split
into 7 high level categories, e.g., Japanese Culture (9 boards)
or Adult (13 boards). In this paper, we focus on /pol/, the “Po-
litically Incorrect” board.2 Figure 1 shows four typical /pol/
threads. Besides the content, the ﬁgure also illustrates the re-
ply feature (‘»12345’ is a reply to post ‘12345’), as well as
other concepts discussed below. Aiming to create a baseline to
compare /pol/ to, we also collect posts from two other boards:
“Sports” (/sp/) and “International” (/int/). The former focuses
on sports and athletics, the latter on cultures, languages, etc.
We choose these two since they are considered “safe-for-work”
boards, and are, according to 4chan rules, more heavily mod-
erated, but also because they display the country ﬂag of the OP,
which we discuss next.
Anonymity. Users do not need an account to read/write posts.
Anonymity is the default (and preferred) behavior, but users
can enter a name along with their posts, even though they can
change it with each post if they wish. Naturally, anonymity
here is meant to be with respect to other users, not the site or
the authorities, unless using Tor or similar tools.3
Tripcodes (hashes of user-supplied passwords) can be used
to “link” threads from the same user across time, providing a
way to verify pseudo-identity. On some boards, intra-thread
trolling led to the introduction of poster IDs. Within a thread
2http://boards.4chan.org/pol/
3In fact, moot (4chan’s creator) reported turning server logs and other records
over to the FBI. See http://www.thesmokinggun.com/buster/fbi/turns-out-
4chan-not-lawless-it-seems.
Figure 1: Examples of typical /pol/ threads.
(A) illustrates the
derogatory use of “cuck” in response to a Bernie Sanders image; (B)
a casual call for genocide with an image of a woman’s cleavage and
a “humorous” response; (C) /pol/’s fears that a withdrawal of Hillary
Clinton would guarantee Trump’s loss; (D) shows Kek, the “God” of
memes, via which /pol/ “believes” they inﬂuence reality.
(and only that thread), each poster is given a unique ID that
appears along with their post, using a combination of cookies
and IP tracking. This preserves anonymity, but mitigates low-
effort sock puppeteering. To the best of our knowledge, /pol/ is
currently the only board with poster IDs enabled.
Flags. /pol/, /sp/, and /int/ also include, along with each post,
the ﬂag of the country the user posted from, based on IP geo-
location. This is meant to reduce the ability to “troll” users by,
e.g., claiming to be from a country where an event is happening
(even though geo-location can obviously be manipulated using
VPNs and proxies).
Ephemerality.
Each board has a ﬁnite catalog of threads.
Threads are pruned after a relatively short period of time via a
“bumping system.” Threads with the most recent post appear
ﬁrst, and creating a new thread results in the one with the least
recent post getting removed. A post in a thread keeps it alive
by bumping it up, however, to prevent a thread from never get-
ting purged, 4chan implements bump and image limits. After a
thread is bumped N times or has M images posted to it (with
N and M being board-dependent), new posts will no longer
bump it up. Originally, when a thread fell out of the catalog, it
was permanently gone, however, an archive system for a sub-
set of boards has recently been implemented: once a thread is
purged, its ﬁnal state is archived for a relatively short period of
time – currently seven days.
2


## Page 3


Moderation. 4chan’s moderation policy is generally lax, es-
pecially on /pol/. So-called janitors, volunteers periodically
recruited from the user base, can prune posts and threads, as
well as recommend users to be banned by more “senior” 4chan
employees. Generally speaking, although janitors are not well
respected by 4chan users and are often mocked for their per-
ceived love for power, they do contribute to 4chan’s continu-
ing operation, by volunteering work on a site that is somewhat
struggling to stay solvent [29].
3
Related Work
While 4chan constantly attracts considerable interest in the
popular press [5, 16], there is very little scientiﬁc work ana-
lyzing its ecosystem. To the best of our knowledge, the only
measurement of 4chan is the work by [6], who study the “ran-
dom” board on 4chan (/b/), the original and most active board.
Using a dataset of 5.5M posts from almost 500K threads col-
lected over a two-week period, they focus on analyzing the
anonymity and ephemerality characteristics of 4chan. They
ﬁnd that over 90% of posts are made by anonymous users, and,
similar to our ﬁndings, that the “bump” system affects threads’
evolution, as the median lifetime of a /b/ thread is only 3.9mins
(and 9.1mins on average). Our work differs from [6] in several
aspects. First, their study is focused on one board (/b/) in a
self-contained fashion, while we also measure how /pol/ af-
fects the rest of the Web (e.g., via raids). Second, their content
analysis is primarily limited to a typology of thread types. Via
manual labeling of a small sample, they determined that 7%
of posts on /b/ are a “call for action,” which includes raiding
behavior. In contrast, our analysis goes deeper, looking at post
contents and raiding in a quantitative manner. Finally, using
some of the features unique to /pol/, /int/, and /sp/, we are also
able to get a glimpse of 4chan’s user demographics, which is
only speculated about in [6].
[23] analyze the inﬂuence of anonymity on aggression and
obscene lexicon by comparing a few anonymous forums and
social networks. They focus on Russian-language platforms,
and also include 2M words from 4chan, ﬁnding no correlation
between anonymity and aggression. In follow-up work [24],
4chan posts are also used to evaluate automatic verbal aggres-
sion detection tools.
Other researchers have also analyzed social media plat-
forms, besides 4chan, characterized by (semi-)anonymity
and/or ephemerality. [9] study the differences between con-
tent posted on anonymous and non-anonymous social me-
dia, showing that linguistic differences between Whisper posts
(anonymous) and Twitter (non-anonymous) are signiﬁcant,
and they train classiﬁers to discriminate them (with 73% accu-
racy). [22] analyze users’ anonymity choices during their ac-
tivity on Quora, identifying categories of questions for which
users are more likely to seek anonymity. They also perform an
analysis of Twitter to study the prevalence and behavior of so-
called “anonymous” and “identiﬁable” users, as classiﬁed by
Amazon Mechanical Turk workers, and ﬁnd a correlation be-
/pol/
/sp/
/int/
Total
Threads
216,783
14,402
24,873
256,058
Posts
8,284,823
1,189,736
1,418,566
10,893,125
Table 1: Number of threads and posts crawled for each board.
tween content sensitivity and a user’s choice to be anonymous.
[15] analyze user behavior on Ask.fm by building an “interac-
tion graph” between 30K proﬁles. They characterize users in
terms of positive/negative behavior and in-degree/out-degree,
and analyze the relationships between these factors.
Another line of work focuses on detecting hate speech. [11]
propose a word embedding based detection tool for hate
speech on Yahoo Finance. [20] also perform hate speech de-
tection on Yahoo Finance and News data, using a supervised
classiﬁcation methodology. [8] characterize anti-social behav-
ior in comments sections of a few popular websites and predict
accounts on those sites that will exhibit anti-social behavior.
Although we observe some similar behavior from /pol/ users,
our work is focused more on understanding the platform and
organization of semi-organized campaigns of anti-social be-
havior, rather than identifying particular users exhibiting such
behavior.
4
Datasets
On June 30, 2016, we started crawling 4chan using its JSON
API.4 We retrieve /pol/’s thread catalog every 5 minutes and
compare the threads that are currently live to those in the pre-
viously obtained catalog. For each thread that has been purged,
we retrieve a full copy from 4chan’s archive, which allows us
to obtain the full/ﬁnal contents of a thread. For each post in a
thread, the API returns, among other things, the post’s number,
its author (e.g., “Anonymous”), timestamp, and contents of the
post (escaped HTML). Although our crawler does not save im-
ages, the API also includes image metadata, e.g., the name the
image is uploaded with, dimensions (width and height), ﬁle
size, and an MD5 hash of the image. On August 6, 2016 we
also started crawling /sp/, 4chan’s sports board, and on August
10, 2016 /int/, the international board. Table 1 provides a high
level overview of our datasets. We note that for about 6% of
the threads, the crawler gets a 404 error: from a manual in-
spection, it seems that this is due to “janitors” (i.e., volunteer
moderators) removing threads for violating rules.
The analysis presented in this paper considers data crawled
until September 12, 2016, except for the raids analysis pre-
sented later on, where we considered threads and YouTube
comments up to Sept. 25. We also use a set of 60,040,275
tweets from Sept. 18 to Oct. 5, 2016 for a brief comparison in
hate speech usage. We note that our datasets are available to
other researchers upon request.
Ethical considerations. Our study has obtained approval by
the designated ethics ofﬁcer at UCL. We note that 4chan posts
are typically anonymous, however, analysis of the activity gen-
4https://github.com/4chan/4chan-API
3


## Page 4


●●
●●
●●●●●●
●
●
●
●●
●●
●
●
●●
●●
●
●
●
●
●●
●●●●
●●
●●
●●●●●●●●
●
●
●●●●
●
●●
●
●●
●●
●●●
●
●●
●●
●●●●
●
●●●●●
●●●●●
●●
●●●●●●●●
●
●●●●●●●
●●●●
●
●●
●●●●●●●●
●
●
●
●
●●●
●●●●
●●●●●
●
●
●
●
●●●
●
●●●●●●
●
●●●
●●●●
●
●
●●●●●●●●●●
●●●
0
50
100
150
0
50
100
150
Hour of week
Average number of new threads created
board
●
/int/
/pol/
/sp/
Figure 2: Average number of new threads per hour of the week.
erated by links on 4chan to other services could be potentially
used to de-anonymize users. To this end, we followed standard
ethical guidelines [25], encrypting data at rest, and making no
attempt to de-anonymize users. We are also aware that con-
tent posted on /pol/ is often highly offensive, however, we do
not censor content in order to provide a comprehensive analy-
sis of /pol/, but warn readers that the rest of this paper features
language likely to be upsetting.
5
General Characterization
5.1
Posting Activity in /pol/
Our ﬁrst step is a high-level examination of posting activ-
ity. In Figure 2, we plot the average number of new threads
created per hour of the week, showing that /pol/ users create
one order of magnitude more threads than /int/ and /sp/ users at
nearly all hours of the day. Then, Figure 3 reports the number
of new threads created per country, normalized by the coun-
try’s Internet-using population.5 Although the US dominates
in total thread creation (visible by the timing of the diurnal pat-
terns from Figure 2), the top 5 countries in terms of threads per
capita are New Zealand, Canada, Ireland, Finland, and Aus-
tralia. 4chan is primarily an English speaking board, and in-
deed nearly every post on /pol/ is in English, but we still ﬁnd
that many non-English speaking countries – e.g., France, Ger-
many, Spain, Portugal, and several Eastern European countries
– are represented. This suggests that although /pol/ is consid-
ered an “ideological backwater,” it is surprisingly diverse in
terms of international participation.
Next, in Figure 4, we plot the distribution of the number
of posts per thread on /pol/, /int/, and /sp/, reporting both the
cumulative distribution function (CDF) and the complemen-
tary CDF (CCDF). All three boards are skewed to the right,
exhibiting quite different means (38.4, 57.1, and 82.9 for /pol/,
/int/, and /sp/, respectively) and medians (7.0, 12.0, 12.0) – i.e.,
there are a few threads with a substantially higher number of
posts. One likely explanation for the average length of /sp/
threads being larger is that users on /sp/ make “game threads”
where they discuss a professional sports game live, while it is
5Obtained from http://www.internetlivestats.com/internet-users/
4.64e−08
0.000506
Figure 3: Heat map of the number of new /pol/ threads created per
country, normalized by Internet-using population.
The darker the
country, the more participation in /pol/ it has, relative to its real-world
Internet using population.
0.00
0.25
0.50
0.75
1.00
1
10
100
1000
Number of posts per thread
CDF
10−5
10−4
10−3
10−2
10−1
100
0
250
500
750
1000
Number of posts per thread
CCDF
board
/int/
/pol/
/sp/
Figure 4: Distributions of the number of posts per thread on /pol/,
/int/, and /sp/. We plot both the CDF and CCDF to show both typical
threads as well as threads that reach the bump limit. Note that the
bump limit for /pol/ and /int/ is 300 at the time of this writing, while
for /sp/ it is 500.
being played. The effects of the bump limit are evident on all
three boards. The bump limit is designed to ensure that fresh
content is always available, and Figure 4 demonstrates this: ex-
tremely popular threads have their lives cut short earlier than
the overall distribution would imply and are eventually purged.
We then investigate how much content actually violates the
rules of the board. In Figure 5, we plot the CDF of the max-
imum number of posts per thread observed via the /pol/ cata-
log, but for which we later receive a 404 error when retrieving
the archived version – i.e., threads that have been deleted by
a janitor or moved to another board. Surprisingly, there are
many “popular” threads that are deleted, as the median num-
ber of posts in a deleted /pol/ thread is around 20, as opposed
to 7 for the threads that are successfully archived. For /int/,
the median number of posts in a deleted thread (5) is appre-
ciably lower than in archived threads (12). This difference is
likely due to: 1) /int/ moving much slower than /pol/, so there is
enough time to delete threads before they become overly pop-
ular, and/or 2) /pol/’s relatively lax moderation policy, which
allows borderline threads to generate many posts before they
end up “ofﬁcially” violating the rules of the board.
4


## Page 5


0.00
0.25
0.50
0.75
1.00
10
1000
Maximum number of posts per non−archived thread observed
CDF
board
/int/
/pol/
/sp/
Figure 5: CDF of the number of posts for non-
archived threads (i.e., likely deleted).
0.00
0.25
0.50
0.75
1.00
10
100
1000
Number of posts
CDF
board
/int/
/pol/
/sp/
Figure 6: CDF of the number of posts per
unique tripcode.
10−5
10−4
10−3
10−2
10−1
100
100
101
102
Number of posters per thread
CCDF
Bump limit reached?
No
Yes
Figure 7: CCDF of the number of unique
posters per thread.
5.2
Tripcodes, Poster IDs, and Replies
Next, we aim to shed light on 4chan’s user base. This task
is not trivial, since, due to the site’s anonymous and ephemeral
nature, it is hard to build a uniﬁed network of user interac-
tions. However, we leverage 4chan’s pseudo-identifying at-
tributes – i.e., the use of tripcodes and poster IDs – to pro-
vide an overview of both micro-level interactions and individ-
ual poster behavior over time.
Overall, we ﬁnd 188,849 posts with a tripcode attached
across /pol/ (128,839 posts), /sp/ (42,431), and /int/ (17,578)
– out of the 10.89M total posts in our dataset (Table 1). Note
that unique tripcodes do not necessarily correspond to unique
users, since users can use any number of tripcodes. Figure 6
plots the CDF of posts per unique tripcode, for each of the
three boards, showing that the median and mean are 6.50 and
36.08, respectively. We observe that 25% of tripcodes (over
30% on /int/) are only used once, and that, although /pol/ has
many more posts overall, /sp/ has more active “tripcode users”
– about 17% of tripcodes on /sp/ are associated to at least 100
posts, compared to about 7% on /pol/.
Arguably, the closest we can get to estimating how unique
users are engaged in 4chan threads is via poster IDs. Unfor-
tunately, these are not available from the JSON API once a
thread is archived, and we decided to use them only a few
weeks into our data collection. However, since the HTML ver-
sion of archived threads does include poster IDs, we started
collecting HTML on August 17, 2016, obtaining it for the last
72,725 (33%) threads in our dataset.
Figure 7 plots the CCDF of the number of unique users per
/pol/ thread, broken up into threads that reached the bump limit
and those that did not. The median and mean number of unique
posters in threads that reached the bump limit was 134.0 and
139.6, respectively.
For typical threads (those that did not
reach the bump limit), the median and mean is much lower –
i.e., 5.0 and 14.76 unique posters per thread. This shows that,
even though 4chan is anonymous, the most popular threads
have “many voices.” Also recall that, in 4chan, replying to a
particular post entails users referencing another post number N
by adding »N in their post, and the standard UIs then treat it as
a reply. This is different from simply posting in a thread: users
are directly replying to a speciﬁc post (not necessarily the post
the OP started the thread with), with the caveat that one can
0.00
0.25
0.50
0.75
1.00
1
10
Average number of replies received on a per−country basis
CDF
Board
/int/
/pol/
/sp/
Figure 8: Distribution of the average number of replies received per
country, per board.
reply to the same post multiple times and to multiple posts at
the same time.
We look at this reply functionality in 4chan to assess how
engaged users are with each other. First, we ﬁnd that 50-60%
of posts never receive a direct reply across all three boards
(/int/: 49%, /pol/: 57%, /sp/: 60%). Taking the posts with no
replies into account, we see that on average /pol/ (0.83) and
/int/ (0.80) have many more replies per post than /sp/ (0.64),
however, the standard deviation on /pol/ is much higher (/pol/:
2.55, /int/: 1.29, /sp/: 1.25).
Next, in Figure 8, we plot the CDF of the average number of
replies per poster per board, aggregated by the country of the
poster, i.e., the distribution of mean replies per country. The
top-10 countries (with at least 1,000 posts) per average num-
ber of replies – Table 2 lets us zoom on the tail end of this
“replies-per-post” per country distribution. On average, while
/pol/ posts are likely to receive more replies than /sp/ and /int/
posts, the distribution is heavily skewed towards certain coun-
tries. Although deeper analysis of these differences is beyond
the scope of this paper, we highlight that, for some of the coun-
tries, the “rare ﬂag” meme may be responsible for receiving
more replies. I.e., users will respond to a post by an uncom-
monly seen ﬂag. For other countries, e.g., Turkey or Israel, it
might be the case that these are either of particular interest to
/pol/, or are quite adept at trolling /pol/ into replies (we note
that our dataset covers the 2016 Turkish coup attempt and /pol/
has a love/hate relationship with Israel).
Finally, we note that, unlike many other social media plat-
5


## Page 6


/pol/
/int/
/sp/
Country
Avg. Replies
Country
Avg. Replies
Country
Avg. Replies
China
1.57
Thailand
1.13
Slovenia
0.91
Pakistan
1.42
Algeria
1.12
Japan
0.84
Japan
1.35
Jordan
1.04
Bulgaria
0.81
Egypt
1.33
S. Korea
1.02
Sweden
0.75
Tri. & Tob.
1.28
Ukraine
1.00
Israel
0.74
Israel
1.27
Viet Nam
0.97
Argentina
0.72
S. Korea
1.20
Tunisia
0.97
India
0.72
Turkey
1.18
Israel
0.97
Greece
0.72
UAE
1.20
Hong Kong
0.92
Puerto Rico
0.70
Bangladesh
1.15
Macedonia
0.91
Australia
0.68
Table 2: The top 10 countries (with at least 1,000 posts) in terms of
direct replies received per post for each board in our dataset.
forms, there is no other interaction system applied to posts on
4chan besides replies (e.g., no liking, upvoting, starring, etc.).
Thus, the only way for a user to receive validation from (or re-
ally any sort of direct interaction with) other users is to entice
them to reply, which might encourage users to craft as inﬂam-
matory or controversial posts as possible.
6
Analyzing Content
In this section, we present an exploratory analysis of the con-
tent posted on /pol/. First, we analyze the types of media (links
and images) shared on the board, then, we study the use of hate
words, and show how /pol/ users can be clustered into mean-
ingful geo-political regions via the wording of their posts.
6.1
Media Analysis
Links. As expected, we ﬁnd that /pol/ users often post links
to external content, e.g., to share and comment on news and
events. (As we discuss later, they also do so to identify and
coordinate targets for hate attacks on other platforms.)
To
study the nature of the URLs posted on /pol/, we use McAfee
SiteAdvisor,6 which, given a URL, returns its category – e.g.,
“Entertainment” or “Social Networking.” We also measure the
popularity of the linked websites, using Alexa ranking.7 Fig-
ure 9 plots the distribution of categories of URLs posted in
/pol/, showing that “Streaming Media” and “Media Sharing”
are the most common, with YouTube playing a key role. In-
terestingly, for some categories, URLs mostly belong to very
popular domains, while others, e.g., “General News,” include
a large number of less popular sites.
The website most linked to on /pol/ is YouTube, with over an
order of magnitude more URLs posted than the next two sites,
Wikipedia and Twitter, followed by Archive.is, a site that lets
users take on-demand “snapshots” of a website, which is of-
ten used on /pol/ to record content – e.g., tweets, blog posts,
or news stories – users feel might get deleted. The 5th and 6th
most popular domains are Wikileaks and pastebin, followed by
DonaldJTrump.com. Next, news sites start appearing, includ-
ing the DailyMail and Breitbart, which are right-wing lean-
ing news outlets. It is interesting to observe that some of the
most popular news sites on a global level, e.g., CNN, BBC,
6https://www.siteadvisor.com/
7http://www.alexa.com/
Streaming
Media
Media
Sharing
General
News
Blogs EntertainmentPolitics
Education Internet
Services
Social
Networking
Personal
Storage
0
20000
40000
60000
80000
100000
120000
140000
160000
180000
Unranked
Top 1M
Top 100k
Top 1K
Top 10
Figure 9: Distribution of different categories of URLs posted in /pol/,
together with the Alexa ranking of their domain.
and The Guardian, appear well outside the top-10 most com-
mon domains. On a board like /pol/, which is meant to focus
on politics and current events, this underlines the polarization
of opinions expressed by its users.
Images. 4chan was designed as an imageboard site, where
users share images along with a message. Therefore, although
some content will naturally be “reposted” (in fact, memes are
almost by deﬁnition going to be posted numerous times [12]),
we expect /pol/ to generate large amounts of original content.
To this end, we count the number of unique images posted on
/pol/ during our observation period, ﬁnding 1,003,785 unique
images (almost 800GB) out of a total 2,210,972 images (45%).
We also plot the CCDF of the number of posts in which each
unique image appears, using the image hash (obtained from
the JSON API) as a unique identiﬁer, in Figure 10. Although
the plot is only a lower bound on image reuse (it only cap-
tures exact reposts), we note that the majority (about 70%) of
images are only posted once, and nearly 95% no more than 5
times. That said, there is a very long tail, i.e., a few select im-
ages become what we might deem “successful memes.” This is
line with 4chan’s reputation for creating memes, and a meme
is such only if it is seen many times. Indeed, the most popu-
lar image on /pol/ appears 838 times in our dataset, depicting
what we might consider the least rare “Pepe ” – see Figure 13.
Note that the Pepe the Frog meme was recently declared a hate
symbol by the Anti-Defamation League [3], but of the 10 Pepe
images appearing in the top 25 most popular images on /pol/,
none seem to have an obvious link to hate. While Figure 13 is
clearly the most common of Pepes, we have included a collec-
tion of somewhat rarer Pepes in Appendix A.
Even with a conservative estimation, we ﬁnd that /pol/ users
posted over 1M unique images in 2.5 months, the majority of
which were either original content or sourced from outside
/pol/. This seems to conﬁrm that the constant production of
new content may be one of the reasons /pol/ is at the heart of
the hate movement on the Internet [26].
6.2
Text Analysis
Hate speech. /pol/ is generally considered a “hateful” ecosys-
tem, however, quantifying hate is a non-trivial task. One pos-
sible approach is to perform sentiment analysis [21] over the
6


## Page 7


10−6
10−5
10−4
10−3
10−2
10−1
100
100
101
102
103
Number of posts an image appeared in
CCDF
Figure 10: CCDF of the number of posts ex-
act duplicate images appeared in on /pol/.
Figure 11: Percentage of posts on /pol/ the
top 15 most popular hate words appear in.
Cluster Terms
1: trump, nigger, american, jew, women, latinos, spanish
2: turkey, coup, erdogan, muslim, syria, assad, kurd
3: russia, trump, war, jew, muslim, putin, nato
4: india, muslim, pakistan, women, trump, arab, islam
5: jew, israel, trump, black, nigger, christian, muslim
6: women, nigger, trump, german, america, western, asian
7: trump, women, muslim, nigger, jew, german, eu, immigr
8: trump, white, black, hillari, nigger, jew, women, american
Figure 12: World map colored by content analy-
sis based clustering.
Figure 13: The most popular image on /pol/ during our collection
period, perhaps the least rare Pepe.
posts in order to identify positive vs. negative attitude, but this
is difﬁcult since the majority of /pol/ posts (about 84%) are
either neutral or negative. As a consequence, to identify hate-
ful posts we use the hatebase dictionary, a crowdsourced list
of more than 1,000 terms from around the world that indicate
hate when referring to a third person.8 We also use the NLTK
framework9 to identify these words in various forms (e.g., “re-
tard” vs “retarded”). Our dictionary-based approach identi-
ﬁes posts that contain hateful terms, but there might be cases
where the context might not exactly be “hateful” (e.g., ironic
usage). Moreover, hatebase is a crowdsourced database, and
is not perfect. To this end, we manually examine the list and
remove a few of the words that are clearly ambiguous or ex-
tremely context-sensitive (e.g., “india” is a variant of “indio,”
used in Mexico to refer to someone of Afro-Mexican origin,
but is likely to be a false positive confused with the country
India in our dataset). Nevertheless, given the nature of /pol/,
the vast majority of posts likely use these terms in a hateful
manner.
Despite these caveats, we can use this approach to provide
an idea of how prevalent hate speech is on /pol/. We ﬁnd that
12% of /pol/ posts contain hateful terms, which is substantially
higher than in /sp/ (6.3%) and /int/ (7.3%). In comparison,
analyzing our sample of tweets reveals just how substantially
different /pol/ is from other social media: only 2.2% contained
a hate word. In Figure 11, we also report the percentage of
/pol/ posts in which the top 15 most “popular” hate words from
8https://www.hatebase.org
9http://www.nltk.org
the hatebase dictionary appear. “Nigger” is the most popular
hate word, used in more than 2% of posts, while “faggot” and
“retard” appear in over 1% of posts. To get an idea of the mag-
nitude of hate, consider that “nigger” appears in 265K posts,
i.e., about 120 posts an hour. After the top 3 hate words, there
is a sharp drop in usage, although we see a variety of slurs.
These include “goy,” which is a derogatory word used by Jew-
ish people to refer to non-Jewish people. In our experience,
however, we note that “goy” is used in an inverted fashion on
/pol/, i.e., posters call other posters “goys” to imply that they
are submitting to Jewish “manipulation” and “trickery.”
Country Analysis. Next, we explored how hate speech differs
by country. We observe clear differences in the use of hate
speech, ranging from around 4.15% (e.g., in Indonesia, Arab
countries, etc.) to around 30% of posts (e.g., China, Bahamas,
Cyprus), while the majority of the 239 countries in our dataset
feature hate speech in 8%–12% of their posts.
Figure 14 plots a heat map of the percentage of posts that
contain hate speech per country with at least 1,000 posts on
/pol/. Countries are placed into seven equally populated bins
and colored from blue to red depending on the percentage of
their posts contain a hate word from the hatebase dictionary.
Note that some of the most “hateful” countries (e.g., Ba-
hamas and Zimbabwe) might be overrepresented due to the
use of proxies in those countries. Zimbabwe is of particular
interest to /pol/ users because of its history as the unrecognized
state of Rhodesia.
To understand whether the country ﬂag has any meaning, we
run a term frequency-inverse document frequency (TF-IDF)
analysis to identify topics that are used per country. We re-
move all countries that have less than 1,000 posts, as this elim-
inates the most obvious potential proxy locations. After re-
moving stop words and performing stemming, we build TF-
IDF vectors for each of the remaining 98 countries, represent-
ing the frequencies with which different words are used, but
down-weighted by the general frequency of each word across
all countries. When examining the TF-IDF vectors, although
we cannot deﬁnitively exclude the presence of proxied users,
we see that the majority of posts from countries seem to match
geographically, e.g., posters from the US talk about Trump and
the elections more than posters from South America, users in
the UK talk about Brexit, those from Greece about the eco-
7


## Page 8


4.15
9.82
12.5
30.7
Figure 14: Heat map showing the percentage of posts with hate
speech per country. [Best viewed in color.]
nomic and immigration crisis, and people from Turkey about
the attempted coup in July 2016.
Clustering. To provide more evidence for the conclusion that
/pol/ is geo-politically diverse, we perform some basic text
classiﬁcation and evaluate whether or not different parts of the
world are talking about “similar” topics. We apply spectral
clustering over the vectors using the Eigengap heuristic [19]
to automatically identify the number of target clusters. In Fig-
ure 12, we present a world map colored according to the 8 clus-
ters generated. Indeed, we see the formation of geo-political
“blocks.” Most of Western Europe is clustered together, and
so are USA and Canada, while the Balkans are in a cluster
with Russia. One possible limitation stemming from our spec-
tral clustering is its sensitivity to the total number of countries
we are attempting to cluster. Indeed, we ﬁnd that, by ﬁlter-
ing out fewer countries based on number of posts, the clusters
do change. For instance, if we do not ﬁlter any country out,
France is clustered with former French colonies and territories,
Spain with South America, and a few of the Nordic countries
ﬂip between the Western Europe and the North American clus-
ters. Additionally, while /pol/ posts are almost exclusively in
English, certain phrasings, misspellings, etc. from non native
speakers might also inﬂuence the clustering. That said, the
overall picture remains consistent: the ﬂags associated with
/pol/ posts are meaningful in terms of the topics those posts
talk about.
7
Raids Against Other Services
As discussed previously, /pol/ is often used to post links to
other sites: some are posted to initiate discussion or provide
additional commentary, but others serve to call /pol/ users to
certain coordinated actions, including attempts to skew post-
debate polls [10] as well as “raids” [1].
Broadly speaking, a raid is an attempt to disrupt another site,
not from a network perspective (as in a DDoS attack), but from
a content point of view. I.e., raids are not an attempt to directly
attack a 3rd party service itself, but rather to disrupt the com-
munity that calls that service home. Raids on /pol/ are semi-
organized: we anecdotally observe a number of calls for ac-
tion [6] consisting of a link to a target – e.g., a YouTube video
Sep 02 2016
Sep 09 2016
Sep 16 2016
Sep 23 2016
Sep 30 2016
date
0
1
2
3
4
5
% of posts
kike­norm
nigger­norm
skype­norm
google­norm
Figure 15: The effects of Operation Google within /pol/.
or a Twitter hashtag – and the text “you know what to do,”
prompting other 4chan users to start harassing the target. The
thread itself often becomes an aggregation point with screen-
shots of the target’s reaction, sharing of sock puppet accounts
used to harass, etc.
In this section, we study how raids on YouTube work. We
show that synchronization between /pol/ threads and YouTube
comments is correlated with an increase in hate speech in
the YouTube comments. We further show evidence that the
synchronization is correlated with a high degree of overlap
in YouTube commenters. First, however, we discuss a case
study of a very broad-target raid, attempting to mess with anti-
trolling tools by substituting racially charged words with com-
pany names, e.g., “googles.”
7.1
Case Study: “Operation Google”
We now present with a case study of a very broad-target
raid, attempting to mess with anti-trolling tools by substituting
racially charged words with company names, e.g., “googles.”
On September 22, 2016, a thread on /pol/ called for the exe-
cution of so-called “Operation Google,” in response to Google
announcing the introduction of anti-trolling machine learning
based technology [13] and similar initiatives on Twitter [14].
It was proposed to poison these by using, e.g., “Google” in-
stead of “nigger” and “Skype” for “kike,” calling other users
to disrupt social media sites like Twitter, and also recommend-
ing using certain hashtags, e.g., #worthlessgoogs and #google-
hangout. By examining the impact of Operation Google on
both /pol/ and Twitter, we aim to gain useful insight into just
how efﬁcient and effective the /pol/ community is in acting in
a coordinated manner.
In Figure 15, we plot the normalized usage of the speciﬁc
replacements called for in the Operation Google post. The
effects within /pol/ are quite evident: on Sep 22 we see the
word “google” appearing at over 5 times its normal rate, while
“Skype” appears at almost double its normal rate. To some ex-
tent, this illustrates how quickly /pol/ can execute on a raid, but
also how short of an attention span its users have: by Sep 26
the burst in usage of Google and Skype had died down. While
we still see elevated usages of “Google” and “Skype,” there
is no discernible change in the usage of “nigger” or “kike,”
8


## Page 9


18­09­2016
19­09­2016
20­09­2016
21­09­2016
22­09­2016
23­09­2016
24­09­2016
25­09­2016
26­09­2016
27­09­2016
28­09­2016
29­09­2016
30­09­2016
01­10­2016
02­10­2016
03­10­2016
04­10­2016
05­10­2016
day
0.00000
0.00002
0.00004
0.00006
0.00008
0.00010
0.00012
0.00014
0.00016
% of tweets
dumbgoogles
worthlessgoogs
googlesgonnagoog
googleriots
googlehangout
Figure 16: The effects of “Operation Google” on Twitter.
but these replacement words do seem to have become part of
/pol/’s vernacular.
Next, we investigate the effects of Operation Google out-
side of /pol/, counting how many tweets in our 60M tweet
dataset (see Section 4) contain the hashtags #worthless-
googs, #googlehangout, #googleriots, #googlesgonnagoog,
and #dumbgoogles in Figure 16. (Recall that our dataset con-
sists of a 1% sample of all public tweets from Sep 18 to Oct
5, 2016.) Figure 17 provides two example tweets from our
dataset that contain Operation Google hashtags. As expected,
the ﬁrst instances of those hashtags, speciﬁcally, #googleriots
and #dumbgoogles, appear on Sep 22. On Sep 23, we also see
#worthlessgoogs and, on later days, the rest of the hashtags.
Overall, Sep 23 features the highest hashtag activity during our
observation period. While this does indicate an attempt to in-
stigate censorship evasion on Twitter, the percentage of tweets
containing these hashtags shows that Operation Google’s im-
pact was much more prevalent on /pol/ itself than on Twitter.
For example, on Sep. 23, #dumbgoogles appears in only 5 out
3M tweets (0.00016%) in our dataset for that day, despite it
being the most “popular” hashtag (among the ones involved in
Operation Google) on the most “active” day. Incidentally, this
is somewhat at odds with the level of media coverage around
Operation Google [18].
7.2
Spreading Hate on YouTube
As discussed in our literature review, we still have limited
insight into how trolls operate, and in particular how forces
outside the control of targeted services organize and coordi-
nate their actions. To this end, we set out to investigate the
connection between /pol/ threads and YouTube comments. We
focus on YouTube since 1) it accounts for the majority of me-
dia links posted on /pol/, and 2) it is experiencing an increase
in hateful comments, prompting Google to announce the (not
uncontroversial) YouTube Heroes program [30].
We examine the comments from 19,568 YouTube videos
linked to by 10,809 /pol/ threads to look for raiding behavior at
scale. Note that ﬁnding evidence of raids on YouTube (or any
other service) is not an easy task, considering that explicit calls
(a)
(b)
Figure 17: Two tweets featuring Operation Google hashtags in com-
bination with other racist memes.
for raids are an offense that can get users banned.10 Therefore,
rather than looking for a particular trigger on /pol/, we look for
elevated activity in comments on YouTube videos linked from
/pol/. In a nutshell, we expect raids to exhibit synchronized ac-
tivity between comments in a /pol/ thread a YouTube link ap-
pears in and the amount of comments it receives on YouTube.
We also expect the rate of hateful comments to increase after a
link is posted on /pol/.
7.3
Activity Modeling
To model synchronized activities, we use signal process-
ing techniques.
First, we introduce some notation: Let x
be a /pol/ thread, and y the set of comments to a YouTube
video linked from x. We denote with

ti
x|i = 1, ..Nx
	
and

tj
y|j = 1, ..Ny
	
, respectively, the set of timestamps of posts
in x and y. Since the lifetime of /pol/ threads is quite dynamic,
we shift and normalize the time axis for both

ti
x
	
and

tj
y
	
,
so that t = 0 corresponds to when the video was ﬁrst linked
and t = 1 to the last post in the /pol/ thread:
t ←
t −tyt
tlast −tyt .
In other words, we normalize to the duration of the /pol/
thread’s lifetime. We consider only /pol/ posts that occur af-
ter the YouTube mention, while, for computational complexity
reasons, we consider only YouTube comments that occurred
10Recall that, since there are no accounts on 4chan, bans are based on ses-
sion/cookies or IP addresses/ranges, with the latter causing VPN/proxies to
be banned often.
9


## Page 10


−2
−1
0
1
2
0
1
2
3
normalized time
%
Figure 18: Distribution of the distance (in normalized thread life-
time) of the highest peak of activity in YouTube comments and the
/pol/ thread they appear in. t = 0 denotes the time when video was
ﬁrst mentioned, and t = 1 the last related post in the thread.
within the (normalized) [−10, +10] period, which accounts for
35% of YouTube comments in our dataset.
From the list of YouTube comment timestamps, we compute
the corresponding Probability Density Function (PDF) using
the Kernel Density Estimator method [27], and estimate the
position of the absolute maximum of the distribution. In Fig-
ure 18, we plot the distribution of the distance between the
highest peak in YouTube commenting activity and the /pol/
post linking to the video. We observe that 14% of the YouTube
videos experience a peak in activity during the period they are
discussed on /pol/. In many cases, /pol/ seems to have a strong
inﬂuence on YouTube activity, suggesting that the YouTube
link posted on /pol/ might have a triggering behavior, even
though this analysis does not necessarily provide evidence of
a raid taking place.
However, if a raid is taking place, then the comments on
both /pol/ and YouTube are likely to be “synchronized.” Con-
sider, for instance, the extreme case where some users that see
the YouTube link on a /pol/ thread comment on both YouTube
and and the /pol/ thread simultaneously: the two set of times-
tamps would be perfectly synchronized. In practice, we mea-
sure the synchronization, in terms of delay between activi-
ties, using cross-correlation to estimate the lag between two
signals. In practice, cross-correlation slides one signal with
respect to the other and calculates the dot product (i.e., the
matching) between the two signals for each possible lag. The
estimated lag is the one that maximizes the matching between
the signals. We represent the sequences as signals (x(t) and
y(t)), using Dirac delta distributions δ(·). Speciﬁcally, we ex-
pand x(t) and y(t) into trains of Dirac delta distributions:
x(t) =
Nx
X
i=1
δ

t −ti
x

; y(t) =
Ny
X
j=1
δ

t −tj
y

and we calculate c(t), the continuous time cross-correlation
between the two series11 as:
c(t) =
Z ∞
−∞
x(t + τ)y(τ)dτ =
Nx
X
i=1
Ny
X
j=1
δ

t −

tj
y −ti
x

11Since timestamp resolution is 1s, this is equivalent to a discrete-time cross-
correlation with 1s binning, but the closed form solution lets us compute it
much more efﬁciently.
0
0.5
1
1.5
2
·10−2
−4
−2
0
2
4
hate comments per second
synchronization lag 105(s)
Figure 19: Hateful YouTube comments vs synchronization lag be-
tween /pol/ threads and corresponding YouTube comments.
Each
point is a /pol/ thread. The hateful comments count refers to just
those within the thread lifetime ([0,+1])
The resulting cross-correlation is also a Dirac delta train,
representing the set of all possible inter-arrival times between
elements from the two sets.
If y(t) is the version of x(t) shifted by ∆T (or at least con-
tains a shifted version of x(t)), with each sample delayed with
a slightly different time lag, c(t) will be characterized by a
high concentration of pulses around ∆T. As in the peak activ-
ity detection, we can estimate the more likely lag by comput-
ing the associated PDF function ˆc(t) by means of the Kernel
Density Estimator method [27], and then compute the global
maximum:
ˆc(t) =
Z ∞
−∞
c(t + τ)k(τ)dτ;
ˆ
∆T = arg max
t
ˆc(t)
where k(t) is the kernel smoothing function (typically a zero-
mean Gaussian function).12
7.4
Evidence of Raids
Building on the above insights, we provide large-scale evi-
dence of raids. If a raid is taking place, we expect the estimated
lag ∆T to be close to zero, and we can validate this by looking
at the content of the YouTube comments.
Figure 19 plots the relationship between the number of hate-
ful comments on YouTube that occur within the /pol/ thread
lifetime (i.e., containing at least one word from the hate-
base dictionary) and the synchronization lag between the /pol/
thread and the YouTube comments. The trend is quite clear:
as the rate of hateful comments on YouTube increases, the
synchronization lag between /pol/ and YouTube comments de-
creases. This shows that almost all YouTube videos affected
by (detected) hateful comments during the /pol/ thread lifetime
are likely related to raids.
Figure 20 plots the CDF of the absolute value of the syn-
chronization lag between /pol/ threads and comments on the
corresponding YouTube videos. We distinguish between com-
ments with a higher percentage of comments containing hate
words during the life of the thread from those with more before
12ˆc(t) is also the cross-correlation between the PDF functions related to x(t)
and y(t).
10


## Page 11


0
0.2
0.4
0.6
0.8
1
·105
0
0.5
1
Synchronization Lag (s)
eCDF
hate in [0 +1]≤hate in [-1 0]
hate in [0 +1]>hate in [-1 0]
Figure 20: CDF of synchronization lag between /pol/ threads and
YouTube comments, distinguishing between threads with YouTube
videos containing higher hate comments percentage in the [0 +1] pe-
riod or [-1 0].
0
0.2
0.4
0.6
0.8
−4
−2
0
2
4
maximum Jaccard index
synchronization lag 105(s)
Figure 21: Maximum Jaccard Index of a YouTube video and all oth-
ers vs synchronization lag between /pol/ threads and corresponding
YouTube comments. Note the high correlation between overlap and
synchronization lag.
the thread. In other words, we compare threads where /pol/ ap-
pears to have a negative impact vs. those where they do not.
From the plot, we observe that the YouTube comments with
more hate speech during the /pol/ thread’s lifetime are signif-
icantly (p < 0.01 with a 2-sample Kolmogorov-Smirnov test)
more synchronized with the /pol/ thread itself.
Finally, to further show that /pol/ is raiding YouTube videos,
we can look at the authors of YouTube comments. We ar-
gue that, unlike the anonymous venue of /pol/, raids on a ser-
vice like YouTube will leave evidence via account usage, and
that the same raiding YouTube accounts will likely be used
by /pol/ users more than once. Indeed, while it is moderately
easy to create a new YouTube account, there is still some ef-
fort involved. Troll accounts might also be cultivated for use
over time, gaining some reputation as they go along. Perhaps
more importantly, while less anonymous than /pol/, YouTube
accounts are still only identiﬁed by a proﬁle name and do not
truly reveal the identity of the user.
To measure this, we compute the overlap (Jaccard index) of
commenters in each YouTube video. In Figure 21 we plot the
synchronization lag as a function of the maximum overlap be-
tween a given video and all others. From the ﬁgure we observe
that if a YouTube video has relatively high overlap with at least
one other YouTube video, it also highly synchronized with its
corresponding /pol/ thread, indicative of a raid taking place.
8
Discussion & Conclusion
This paper presented the ﬁrst large-scale study of /pol/, 4chan’s
politically incorrect board, arguably the most controversial one
owing to its links to the alt-right movement and its unconven-
tional support to Donald Trump’s 2016 presidential campaign.
First, we provided a general characterization, comparing ac-
tivity on /pol/ to two other boards on 4chan, /sp/ (“sports”) and
/int/ (“international”). We showed that each of the boards ex-
hibits different behaviors with respect to thread creation and
posts. We looked at the impact of “bump limits” on discourse,
ﬁnding that it results in fresh content on a consistent basis.
We used the country ﬂag feature present on the three boards
and found that, while Americans dominate the conversation
in terms of absolute numbers, many other countries (both na-
tive English speaking and not) are well represented in terms of
posts per capita. We also showed differences in the maturity of
threads with respect to moderators’ actions across the boards.
Next, we examined the content posted to /pol/, ﬁnding that
the majority of links posted to the board point to YouTube.
We also saw that /pol/ contains many more links to tabloid
and right-wing leaning news outlets than mainstream sites. By
looking at metadata associated with posted images, we learned
that most content on 4chan is quite unique: 70% of the 1M
unique images in our dataset were posted only once and 95%
less than 5 times. In fact, /pol/’s ability to ﬁnd or produce orig-
inal content is likely one of the reasons it is thought to be at
the center of hate on the web.
Finally, we studied “raiding” behavior by looking for ev-
idence of /pol/’s hateful impact on YouTube comments. We
used signal processing techniques to discover that peaks of
commenting activity on YouTube tend to occur within the life-
time of the thread they were posted to on /pol/.
Next, we
used cross-correlation to estimate the synchronization lag be-
tween /pol/ threads and comments on linked YouTube videos.
Here, we found that as the synchronization lag approaches
zero, there is an increase in the rate of comments with hate
words on the linked YouTube comments. Finally, we saw that
if two YouTube videos’ comments had many common authors
they were likely to be highly synchronized, indicating potential
raider accounts. This evidence suggests that, while not neces-
sarily explicitly called for (and in fact, against /pol/’s rules),
/pol/ users are performing raids in an attempt to disrupt the
community of YouTube users.
Overall, our analysis provides not only the ﬁrst measure-
ment study of /pol/, but also insight into the continued growth
of hate and extremism trends on social media, and prompts a
few interesting problems for future research. Naturally, how-
ever, our work is not without limitations. First, although the
Hatebase dataset we used is an invaluable resource for hate
speech analysis, the usage of “hate” words may be context-
dependent, and we leave it to future work to investigate how to
distinguish context (e.g., by recognizing sarcasm or trolling).
Also, our ﬂag based country analysis may have been inﬂu-
enced by the use of VPNs/proxies: although this does not
affect the validity of our results, it calls for a more in-depth
11


## Page 12


analysis of language and posting behavior. Finally, while we
showed quantitative evidence that raids are taking place, we do
not claim an ability to classify them as there are many layers
of subtlety in how raiding behavior might be exhibited. How-
ever, we are conﬁdent that our ﬁndings can serve as a founda-
tion for interesting and valuable future work exploring fringe
groups like the alt-right, hate speech, and online harassment
campaigns.
Acknowledgments. We wish to thank Andri Ioannou and De-
spoina Chatzakou for their help and feedback, and Timothy
Quinn for providing access to the Hatebase API. This research
is supported by the European Union’s H2020-MSCA-RISE
grant “ENCASE” (GA No. 691025) and by the EPSRC un-
der grant EP/N008448/1. Jeremiah Onaolapo was supported
by the Petroleum Technology Development Fund (PTDF).
References
[1] F. Alfonso. 4chan celebrates Independence Day by spamming
popular Tumblr tags.
http://www.dailydot.com/news/4chan-
tumblr-independence-day/, 2014.
[2] N. Anderson.
4chan tries to change life outside the base-
ment
via
DDoS
attacks.
http://arstechnica.com/tech-
policy/2010/09/4chan-tries-to-change-life-outside-the-
basement-via-ddos-attacks/, 2010.
[3] Anti-Defamation League. Pepe the Frog. http://www.adl.org/
combating-hate/hate-on-display/c/pepe-the-frog.html, 2016.
[4] Aspen Institute. How the internet and social media are changing
culture.
http://www.aspeninstitute.cz/en/article/4-2014-how-
the-internet-and-social-media-are-changing-culture/, 2014.
[5] J. Bartlett. 4chan: the role of anonymity in the meme-generating
cesspool of the web.
http://www.wired.co.uk/article/4chan-
happy-birthday, 2016.
[6] M. S. Bernstein, A. Monroy-Hernández, D. Harry, P. André,
K. Panovich, and G. Vargas. 4chan and /b/: An Analysis of
Anonymity and Ephemerality in a Large Online Community. In
ICWSM, 2011.
[7] J. Blackburn and H. Kwak. STFU NOOB! Predicting Crowd-
sourced Decisions on Toxic Behavior in Online Games.
In
WWW, 2014.
[8] J. Cheng, C. Danescu-Niculescu-Mizil, and J. Leskovec. Anti-
social behavior in online discussion communities. In ICWSM,
2015.
[9] D. Correa, L. A. Silva, M. Mondal, F. Benevenuto, and K. P.
Gummadi. The Many Shades of Anonymity: Characterizing
Anonymous Social Media Content. In ICWSM, 2015.
[10] A.
Couts
and
A.
Powell.
4chan
and
Reddit
bom-
barded
debate
polls
to
declare
Trump
the
winner.
http://www.dailydot.com/layer8/trump-clinton-debate-online-
polls-4chan-the-donald/, 2016.
[11] N. Djuric, J. Zhou, R. Morris, M. Grbovic, V. Radosavljevic,
and N. Bhamidipati. Hate speech detection with comment em-
beddings. In WWW, 2015.
[12] E.
Ferrara,
M.
JafariAsbagh,
O.
Varol,
V.
Qazvinian,
F. Menczer, and A. Flammini. Clustering memes in social me-
dia. In ASONAM, Aug 2013.
[13] A. Greenberg. Inside Google’s Internet Justice League and Its
AI-Powered War on Trolls.
https://www.wired.com/2016/09/
inside-googles-internet-justice-league-ai-powered-war-trolls/,
2016.
[14] A.
Horowitz
Satlin.
Anti-Semitic
Trolls
Threaten
To
Take
Twitter
Down
With
Them.
http://www.
hufﬁngtonpost.com/entry/twitter-bullying-anti-semitism_
us_580876d1e4b0b994d4c47e94, 2016.
[15] H. Hosseinmardi, A. Ghasemianlangroodi, R. Han, Q. Lv, and
S. Mishra.
Analyzing Negative User Behavior in a Semi-
anonymous Social Network. In ASONAM, 2014.
[16] M. Ingram. Here’s Why You Shouldn’t Trust Those Online Polls
That Say Trump Won. http://for.tn/2dk74pG, 2016.
[17] A. Johnson and P. Helsel. 4chan Murder Suspect David Kalac
Surrenders to Police. http://nbcnews.to/2dHNcuO, 2016.
[18] C. McGoogan.
Internet trolls replace racist slurs with code-
words to avoid censorship.
http://www.telegraph.co.uk/
technology/2016/10/03/internet-trolls-replace-racist-slurs-
with-online-codewords-to-av/, 2016.
[19] A. Y. Ng, M. I. Jordan, Y. Weiss, et al. On spectral clustering:
Analysis and an algorithm. Advances in neural information pro-
cessing systems, 2:849–856, 2002.
[20] C. Nobata, J. Tetreault, A. Thomas, Y. Mehdad, and Y. Chang.
Abusive Language Detection in Online User Content. In WWW,
pages 145–153, 2016.
[21] B. Pang and L. Lee. Opinion mining and sentiment analysis.
Foundations and trends in information retrieval, 2:1–135, 2008.
[22] S. T. Peddinti, A. Korolova, E. Bursztein, and G. Sampemane.
Cloak and Swagger: Understanding data sensitivity through the
lens of user anonymity. In IEEE Security & Privacy, 2014.
[23] R. Potapova and D. Gordeev.
Determination of the Internet
Anonymity Inﬂuence on the Level of Aggression and Usage of
Obscene Lexis. ArXiv e-prints, Oct. 2015.
[24] R. Potapova and D. Gordeev. Detecting state of aggression in
sentences using CNN. CoRR, abs/1604.06650, 2016.
[25] C. M. Rivers and B. L. Lewis. Ethical research standards in a
world of big data. F1000Research, 2014.
[26] J. Siegel.
Dylann Roof,
4chan,
and the New Online
Racism, 2015. http://www.thedailybeast.com/articles/2015/06/
29/dylann-roof-4chan-and-the-new-online-racism.html.
[27] B. W. Silverman.
Density estimation for statistics and data
analysis, volume 26. CRC press, 1986.
[28] J. Stein.
How Trolls Are Ruining the Internet.
http://ti.me/
2bzZa9y, 2016.
[29] N. Wolf. Future of 4chan uncertain as controversial site faces
ﬁnancial woes. https://www.theguardian.com/technology/2016/
oct/04/4chan-website-ﬁnancial-trouble-martin-shkreli, 2016.
[30] YouTube Ofﬁcial Blog. Growing our Trusted Flagger program
into YouTube Heroes.
https://youtube.googleblog.com/2016/
09/growing-our-trusted-ﬂagger-program.html, 2016.
Appendix
A
Rare Pepes
In this Section we display some of our rare Pepe collection.
12


## Page 13


Figure 22: A somewhat rare, modern Pepe, which much like the
Bayeux Tapestry records the historic rise of /pol/.
Figure 23: A (French?) Pepe wearing a beret, smoking a cigarette,
and playing an accordion.
Figure 24: An extremely common Pepe commissioned by CNN to
commemorate Pepe’s recognition as a hate symbol.
Figure 25: An (unfortunately) ultra rare Pepe eating a delicious Pub-
lix Deli Sub Sandwich.
13


## Page 14


Figure 26: An ironic Pepe depiction of Hillary Clinton.
Figure 27: A Pepe Julian Asange dangling a USB full of Democratic
National Convention secrets.
Figure 28: What we believe to be a Pepe re-interpretation of Goya’s
“Saturn Devouring His Son.”
Figure 29: A very comfy Pepe.
14


## Page 15


Figure 30: A mischievous witch Pepe.
Figure 31: The now “iconic” Trump Pepe.
15

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1610_03452v5_kek_cucks_and_god_emperor_trump_a_measurement_study_of_4chan_s_politically_in
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1610_03452V5_KEK_CUCKS_AND_GOD_EMPEROR_TRUMP_A_MEASUREMENT_STUDY_OF_4CHAN_S_POLITICALLY_IN.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
