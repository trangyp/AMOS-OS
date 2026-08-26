---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.00149v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1910.00149v3_Fame_and_Ultrafame__Measuring_and_comparing_daily_levels_of__being_talked_about_

> Source: 1910.00149v3_Fame_and_Ultrafame__Measuring_and_comparing_daily_levels_of__being_talked_about_.pdf

> Pages: 31

---


## Page 1


Fame and Ultrafame: Measuring and comparing daily levels of ‘being talked about’ for
United States’ presidents, their rivals, God, countries, and K-pop
Peter Sheridan Dodds,1, 2, ∗Joshua R. Minot,1 Michael V. Arnold,1 Thayer Alshaabi,1 Jane Lydia
Adams,1 David Rushing Dewhurst,1 Andrew J. Reagan,3 and Christopher M. Danforth1, 2
1Computational Story Lab, Vermont Complex Systems Center,
MassMutual Center of Excellence for Complex Systems and Data Science,
Vermont Advanced Computing Core, University of Vermont, Burlington, VT 05401.
2Department of Mathematics & Statistics, University of Vermont, Burlington, VT 05401.
3MassMutual Data Science, Amherst, MA 01002.
(Dated: November 2, 2021)
When building a global brand of any kind—a political actor, clothing style, or belief system—
developing widespread awareness is a primary goal. Short of knowing any of the stories or products
of a brand, being talked about in whatever fashion—raw fame—is, as Oscar Wilde would have it,
better than not being talked about at all. Here, we measure, examine, and contrast the day-to-day
raw fame dynamics on Twitter for US Presidents and major US Presidential candidates from 2008 to
2020: Barack Obama, John McCain, Mitt Romney, Hillary Clinton, Donald Trump, and Joe Biden.
We assign “lexical fame” to be the number and (Zipﬁan) rank of the (lowercased) mentions made
for each individual across all languages. We show that all ﬁve political ﬁgures have at some point
reached extraordinary volume levels of what we deﬁne to be “lexical ultrafame”: An overall rank of
approximately 300 or less which is largely the realm of function words and demarcated by the highly
stable rank of ‘god’. By this measure, ‘trump’ has become enduringly ultrafamous, from the 2016
election on. We use typical ranks for country names and function words as standards to improve
perception of scale. We quantify relative fame rates and ﬁnd that in the eight weeks leading up
the 2008 and 2012 elections, ‘obama’ held a 1000:757 volume ratio over ‘mccain’ and 1000:892 over
‘romney’, well short of the 1000:544 and 1000:504 volumes favoring ‘trump’ over ‘hillary’ and ‘biden’
in the 8 weeks leading up to the 2016 and 2020 elections. Finally, we track how only one other entity
has more sustained ultrafame than ‘trump’ on Twitter: The K-pop (Korean pop) band BTS. We
chart the dramatic rise of BTS, ﬁnding their Twitter handle ‘@bts twt’ has been able to compete
with ‘a’ and ‘the’, reaching a rank of three at the day scale and a rank of one at the quarter-hour
scale. Our ﬁndings for BTS more generally point to K-pop’s growing economic, social, and political
power.
I.
INTRODUCTION
“It is silly of you, for there is only one thing in
the world worse than being talked about, and
that is not being talked about.”
— Oscar Wilde, The Picture of Dorian Gray [1].
“Being talked about” is the essence of fame, a word
that accurately encodes this most basic of sociological
mechanisms as it traces back to the Latin f¯ama (“speak”)
with φ´ημη (ph´¯em¯e, “talk”) as its Greek cognate.
Achieving widespread awareness is arguably the prima-
ry goal of any people-centric enterprise seeking to scale.
Of course any such enterprise will want the valence of
fame to be positive, and for “talk” to be self-sustaining.
Examples abound. To take just one, in the sphere of
sport, Lance Armstrong’s archetypal fall-from-grace fol-
lowed a global expansion of awareness of cancer research,
the Tour de France, and cycling. Armstrong himself
became famous as an eight-fold kill-the-monster hero,
ﬁrst conquering cancer then the Tour seven times in a
row, all ending with a televised confession of betrayal to
Oprah.
∗peter.dodds@uvm.edu
We also know that fame is profoundly a social con-
struct, a complex mix of system randomness, an indi-
vidual’s luck, timing, history, and, to the extent that it
exists at all in a given ﬁeld, inherent quality [2–4]. From
the perspective of collective evaluation of cultural enti-
ties, the existence and perceived importance of ranked
lists of anything (wealthy individuals, songs, books, col-
leges, cities, countries) leaves social systems vulnerable
to those unethical actors who would seek fame. Know-
ing that “getting the word out there” is the foundation-
al work allows system-level manipulation by individuals
or organizations pretending to be at or near the top of
such lists by gaming myriad sociotechnical algorithms
(many/some “people are saying” [5, 6], payola [7], “John
Barron” [8–10]).
In politics, a key polling question concerns whether
or not an interviewee has heard of a candidate at all—
shorn of sentiment and story. While some polls show that
increases in awareness correspond to increases in favor-
ability, politicians trace out many paths in awareness-
favorability space.
For example, as we show in Fig. 1, a series of polls
carried out by Monmouth University during the ﬁrst
ﬁve months of 2019 [11] revealed a strong correla-
tion between awareness of and favorability toward 24
potential Democratic candidates for the 2020 presiden-
Typeset by REVTEX
arXiv:1910.00149v3  [physics.soc-ph]  29 Oct 2021


## Page 2


2
20
30
40
50
60
70
80
90
100
0
10
20
30
40
50
60
70
80
FIG. 1. Comparison of awareness and relative favorability for
24 democratic candidates for the democratic nominee in the
2020 US presidential election, showing a strong positive cor-
relation (Spearman correlation coeﬃcient rs=0.949). Details:
The data comes from four polls carried out by Monmouth
University from 2019/01 to 2019/05 [11]. We compute a can-
didate’s relative favorability as normalized by the subset of
respondents who have heard of that candidate. Not all can-
didates were included in all polls resulting in 58 data points
(instead of 96). We acknowledge that the varying numbers
of polls per candidate calls for a more sophisticated analy-
sis than simple correlation, but our aim is simply to show
a clear example of well correlated awareness and favorability.
See Fig. 2 for a counterexample. For readability, we only show
a subset of unique names, and arrange these left and right so
that one end of the text is close to the relevant data point.
tial election (Spearman correlation coeﬃcient: rs=0.949).
The awareness extremes were for Joe Biden, who regis-
tered 1% of those polled saying they had not heard of
him (2019/05), and 67% saying the same of Marianne
Williamson (2019/03).
By contrast, as we show in Fig. 2, US presidents pro-
vide a powerful example as ﬁgures with extremely high
global awareness levels while receiving a wide variation of
approval over time and across demographics [12]. Never-
theless and as for many other cultural and social spheres,
achieving widespread “brand awareness” in politics is an
order zero undertaking.
Our intention with Figs. 1 and 2 is to show that while
simple awareness can indeed correlate with favorability
as a brand grows, this is not a general truth.
So, while exploring mechanisms, sentiment, narratives,
and other aspects of fame are all necessary [2–4, 13–17],
we will here concern ourselves with Wildean raw fame—
the state of being talked about—for US presidents and
20
30
40
50
60
70
80
90
100
FIG. 2. Histograms of favorability ratings from Gallup polls
for US presidents taken from Franklin Roosevelt through
to Donald Trump [12]. The rightmost histogram represents
a combined average with each president’s ratings equally
weighted. We do not have data for awareness levels but for
US presidents we can reasonably assert that the percentage
will be uniformly high. In contrast to the strong correlation
between awareness and favorability in Fig. 1, we see that
high-awareness political ﬁgures can certainly achieve a wide
range of favorability ratings. With our focus in this paper
on awareness—raw fame—we oﬀer this ﬁgure as a tempering
exhibit. Polls run from 1941/07/22 through to 2020/12/17.
Trump has had the lowest variation in favorability (vari-
ance σ2=3.05, 2.5 to 97.5 percentile covering 14.0 favorability
points) while Truman has the highest (variance σ2=16.0, 2.5
to 97.5 percentile covering 63.1 favorability points). Trump
is also the only president to have not registered an above 50
favorability rating in Gallup polls.
their main rivals.
We focus on the major political ﬁgures involved in the
US presidential elections of 2008, 2012, 2016, and 2020,
and the encompassing time frame: Barack Obama, John
McCain, Mitt Romney, Hillary Clinton, Donald Trump,
and Joe Biden (see Tab. I).
As we will show for these political ﬁgures, Trump has
enjoyed singularly transcendent fame—what we will call
lexical ultrafame—within our time period of interest.
Trump has only been overmatched by one other entity of
any kind: The K-pop (Korean pop) band BTS [18], and
we ﬁnd that we are obliged to include them in our analy-
ses. BTS’s ultrafame more generally reﬂects the real pow-
er that K-pop and K-pop fandom has attained as a global
cultural, social, and political force [19–22]. Extraordinar-
ily, both Trump and BTS have occupied levels of lexi-
cal fame that the most basic function words of language
occupy. To give a sense of what we will uncover, the medi-
an rank (which we explain below) for the word ‘trump’


## Page 3


3
Political ﬁgure: Position:
1-grams (dominant 1-gram in bold):
Barack Obama US president from 2009/01 to 2017/01 barack, obama, @barackobama
John McCain
Republican Party nominee in 2008
john, mccain, @sejohnmccain
Mitt Romney
Republican Party nominee in 2012
mitt, romney, @mittromney
Hillary Clinton Democratic Party nominee in 2016
hillary, clinton, @hillaryclinton
Donald Trump US president from 2017/01 to present
donald, trump, @realdonaldtrump
Joe Biden
Democratic Party nominee in 2020
joe, biden, @joebiden
TABLE I. The six political ﬁgures whose fame we trace and compare via Twitter mentions. To quantify fame, we measure the
rank and count dynamics for three 1-grams for each political ﬁgure: First name, last name, and Twitter handle. The 1-grams in
bold are the on-average, unambiguous 1-gram with the highest count referring to the political ﬁgure. We also follow the lexical
fame of the K-pop band BTS [18] per their Twitter handle @bts twt.
during Trump’s presidency has been around r=180, akin
to that of words like ‘after’, ‘would’, and ‘man’, while
the median rank for BTS’s Twitter handle, ‘@bts twt’,
has tracked near r=90, a rank typical of the words ‘has’,
‘more’, and ‘da’.
There are many ways to gauge fame such as direct
polls, mentions on social media, and rates of internet
searches. While including an array of distinct measures
would be ideal, we limit ourselves here to the social media
platform that is Twitter. We will thus endeavor to per-
form our analyses with great care for one well-deﬁned, if
sprawling, realm of public discourse.
To be explicit, Twitter is of course just one large online
space that provides a single source of text data for mea-
suring the relative prevalence of terms. While we would
argue that Twitter is notable for its reach and observed
impact on social and political systems, we would nev-
er suggest that measurements of fame derived from the
platform are all encompassing. As will show, our mea-
surement of day-scale fame time series on Twitter func-
tions well for generating computationally-aided histori-
cal timelines. It is our hope that our in-depth analysis of
fame on Twitter will serve as a touch point for other mea-
surements of fame (e.g., using Google Trends, Wikipedia,
books, etc.).
For our purposes here, we will deﬁne lexical fame of any
given entity by the daily counts and Zipﬁan ranks for 1-
grams (words, hashtags, user handles, etc.) pertaining to
that entity. For example, Barack Obama’s lexical fame
will be registered by counts and ranks for ‘barack’, ‘oba-
ma’, and ‘@barackobama’. For a few 1-grams on speciﬁc
days, we will report on fame levels at the 15 minute time
scale. We also limit ourselves to 1-grams, reserving full
analyses of n-grams for n ≥2 for future work, though we
will mention a few observations for 2-grams for speciﬁc
days.
We deliver the remainder of our paper as follows. In
Sec. II we describe our Twitter data set and the data-
wrangling part of our analysis, reserving details for Sec. V
at the end. We present our core results in Sec. III. In
Sec. III A, we ﬁrst examine time series and histograms for
ranks of Twitter mentions for our six political ﬁgures and
the K-pop band BTS. In Sec. III B, we then make com-
parative analyses of mentions across ﬁgures and across
calendar years and the eight weeks leading up to the
US elections. Our work is observational and descriptive—
a fundamental aspect of basic science—and we will not
move toward prediction here. We close with concluding
remarks in Sec. IV. We have also constructed our ﬁgures
and captions to be as self-contained as possible for those
readers who may not wish to read the main text, and by
inclusion, this sentence.
II.
DATA AND PREPARATORY TREATMENT
A.
Description of Twitter data set and rationale
for use
We measure the daily fame of political ﬁgures as
reﬂected by mentions on the social media platform Twit-
ter. We have collected roughly 10% of all public tweets
starting on 2008/09/09 through to 2021/10/24, allowing
us to explore fame dynamics around the last three US
presidential elections.
Twitter has a number of well known beneﬁts and draw-
backs. First, a few of the stronger positives. We have
essentially real-time temporal resolution for a massive
scale of messages. Standardization of hashtags have made
for powerful codifying of issues (e.g., #metoo), and for-
malization of retweets, favorites, and replies allow us to
follow the reaction to individual tweets in detail. Though
accounts can be made private, Twitter is by default
public-facing and largely engaged with such an under-
standing by its users. The world’s languages, and not just
the dominant ones, are all present on Twitter, allowing
for potentially rich cultural and linguistic explorations.
Negatives for Twitter are also on oﬀer in good num-
ber. Twitter is not used uniformly by all people around
the world, with users skewing younger and democrat-


## Page 4


4
ic, and engaging at a wide range of rates, and with
strong user bases in, for example, the US, Japan, and
Brazil [? ]. Geolocation and demographic features have
typically been publically available for a small fraction of
tweets (less than 1% for the former). Geolocation has
been uneven in nature (latitude-longitude versus place
name), and was removed entirely as a feature for users in
2019 though metadata in photos could still encode loca-
tion. Algorithmically generated content is prevalent (e.g.,
“bots”) and problematic for the both the service and
users [23]. The changing nature of how Twitter presents
information to user through algorithmic feeds and trend-
ing story pages only adds further complexity.
In the middle lies the evident issue that tweets, and
cleverly constructed subsets of tweets, do not perfect-
ly represent all the ideas, viewpoints, and utterances of
people of whatever category one may want to study. The
collective voice of Twitter is a discordant symphony of
the expressions, reactions, and ampliﬁcations of individu-
als, news outlets, corporations, fan bases, celebrities, and
automatic accounts of all alignments. The ampliﬁcation
processes are rich-get-richer mechanisms [24, 25] made
possible by follower networks, external media’s embed-
ding of tweets, and Twitter’s own system of curating and
presenting trending stories.
We know that as a whole Twitter strongly follows
major events [26–28] and can successfully be used as an
indirect polling system [26, 29–31]. Twitter has also risen
in prominence in the political sphere, particularly with
the usage of the platform by the former US president,
Donald Trump. In turbulent times, recalling what major
events occurred and in what order temporally can be
challenging—“chronopathy”—and we have been able to
use Twitter to generate computational timelines around
Trump [28]. With daily (and sub-day) resolution of lexi-
cal fame, we ﬁnd here that we are able, by inspection, to
tie rank dynamics to speciﬁc events.
Like other global social media giants of today, Twitter
has the potential to create real impact at all scales. Of
many examples, one thematically related to our study
here is the identiﬁcation of President Trump’s tweets
as having an eﬀect on prices of Treasury bonds, lead-
ing JP Morgan Chase to create a covfefe-fueled “Volfefe
index” [32] (see also [33]). Entwining news, politics, mar-
kets, patriotism issues, and belief, a 2013 hacked tweet
from the Associated Press’s Twitter account suggesting
that the White House had been bombed and Obama was
injured, leading to an immediate drop in the market [34].
Although the story was quickly corrected, this one hacked
tweet caused the evaporation of $136 billion in a few min-
utes. One more example, this time showing the power of
a celebrity’s oﬀ-handed remark: On February 21, Kylie
Jenner, tweeted, and we quote, “sooo does anyone else
not open Snapchat anymore? Or is it just me. . . ugh this
is so sad” [35]. Subsequent to this single tweet—though
we do not here claim causality—Snapchat’s shares deﬂat-
ed 6% in value ($1.3 billion).
We are not implying that Twitter is solely dominated
by individual tweets. Words, phrases, and hashtags that
reﬂect major events and stories going on in the world
will be produced and ampliﬁed collectively (e.g., ‘coron-
avirus’, #blacklivesmatter) [31].
In short, Twitter is a large-scale, temporally ﬁne-
grained source of written text containing meaningful sig-
natures that can powerfully aﬀect society and the world.
Even shorter, Twitter is Twitter.
B.
Preparation of Twitter data set for analysis
To explore raw fame and ultrafame, we take our entire
Twitter corpus and process tweets into 1-grams. While
keeping the parsing as simple as possible, we make some
choices such as discarding emojis, excluding languages
that do not use whitespace, and adjusting all letters
to lower case for languages where two cases exist (e.g.,
counts for ‘god’ include counts for ‘God’, ‘GOD’, ‘god’,
etc.) (see Methods for full details, Sec. V). Such parsing
is evidently not an activity that humans could perform,
and even if they could, reading (or perhaps more accu-
rately, absorbing) a stream of 50 million tweets a day
could well be harmful (we note that animal Twitter is
generally uplifting though).
For each day, we determine usage frequency for all 1-
grams appearing on that day. We also create the resul-
tant Zipf distribution [36], ranking 1-grams by descend-
ing order of counts, denoting rank by r.
In what follows, we ﬁrst use 1-gram ranks. As such, we
do not need to be concerned with the extremely heavy
tails of frequency and Zipf distributions for Twitter, and
concomitant worries about subsampling given our cor-
pus’s approximate 10%-of-all-tweets character. (i.e., we
are, not unreasonably, not assured by Twitter that our
subset is exactly 10% of all tweets). We note that rates
of 1-gram appearance for 1-grams that are not too rare
are quantities we can measure well by simple normaliza-
tion of frequencies by the sum of all counts. The phrase
“not too rare” would have to be considered carefully for
studying very low fame 1-grams. But such rates are not of
importance here as, again, we will only work with ranks,
counts, and rates of a small set of prominent entities.
For the core of our analysis, we extract the ranks and
counts for names and Twitter handles for our six political
ﬁgures (see Tab. I), along with two 1-grams which will
prove to be of value and interest: ‘god’ and the Twitter
handle for the K-pop band BTS, ‘@bts twt’.
The ﬁve male politicians are all dominantly referred
to by their last names, while Hillary Clinton’s strongest
1-gram referent is ‘hillary’. One partial reasons for this
would be that Clinton shares a last name with her hus-
band, former US president Bill Clinton, and the use of
at least her ﬁrst name has long been a practical choice
for clarity. But referring to a person by ﬁrst name ver-
sus last name is a not uncommon instantiation of gender
bias [37, 38], and has been identiﬁed in media coverage
for Clinton in the 2008 democratic primary [39]. Still, for


## Page 5


5
our present study, six is a small sample from which we
cannot generalize (a separate comprehensive study cer-
tainly could be a topic of another paper); we want to be
clear that we are simply taking what the data from Twit-
ter gives us. We can at least note that this naming bias
is not completely pervasive with major political ﬁgures.
The 1-gram ‘bernie’ dominates for Bernie Sanders for
example. A separate issue is McCain’s ﬁrst name John,
which is a poor referent. As we will see, the movement
of ‘john’ against a background level of the name is dis-
cernible, though this is a minor issue. In future work, we
will be able to explore 2-grams and 3-grams but we set
that analysis outside of our present scope.
To better help communicate 1-gram rank, we also
determine median daily rank for two subsets of 1-grams
in 2018: (1) Function words with median rank r ≤1000;
(2) Names of countries and territories including identi-
ﬁable component words (e.g., ‘america’) for r > 1000.
For these anchor words, we do not look outside of Twit-
ter because there is no one special Zipf distribution for
language. If we considered Reddit or Google Books, for
example, we would use anchors that worked within the
context of those corpora. We also acknowledge that being
based on Twitter as a whole, these ranks will tend toward
a US-centric view of the world from a particular period
of history, but we nevertheless believe they generally pro-
vide useful footholds for all readers. A few examples are:
‘a’ with r=1,
‘and’ with r=6,
‘la’ with r=16,
‘there’ with r=162,
‘porque’ with r=323,
‘friend’ with r=539,
‘america’ with r=990,
‘england’ with r=6,718,
‘guatemala’ with r=27,775,
‘ﬁji’ with r=104,091, and
‘niue’ with r=1,062,883, the least famous country
with a four letter name [40].
Finally, we operationalize the concept of ultrafame
within the context of Twitter. Broadly speaking, we will
consider a 1-gram to have achieved lexical ultrafame if it
is competing with the basic function words of a language
(or languages). Upon inspection of the typical function
words that tend to have the highest daily counts, we ﬁnd
a remarkably stable presence for one non-function word:
‘god’. As we have done for function words and names
of counties above, we use ‘god’ as an lexical ultrafame
boundary because it is sensible within the context of
Twitter.
We are not claiming that ‘god’ is the only 1-gram that
could serve this role, but it is an eﬀective choice for oﬀer-
ing a consistent reference point as we describe the preva-
lence of other 1-grams. Indeed, we could choose other
benchmarks but our work is not meant to be an exhaus-
tive study of establishing reference points.
The rank for ‘god’ hovers around 300, showing very
low volatility (see Sec. III A, Fig. 3, Fig. A1, and Tab. A9
for year-scale data). For the time period of 2008/09/09–
2020/12/31, the median rank for ‘god’ is rgod = 303. The
ﬁrst and third quartiles for the rank of ‘god’ are 281 and
330, the 2.5% and 97.5% percentiles are 237 and 383, and
the overall high and low ranks are 134 and 529.
We will ascribe lexical ultrafame to any 1-gram with
rank r ≤rgod = 303.
III.
RESULTS
A.
Dynamics of lexical fame and ultrafame
We chart the 2008–2019 daily rank time series for our
six political ﬁgures, ‘@bts twt’, and ‘god’ in Fig. 3, and
show corresponding histograms and ultrafame rates in
the companion ﬁgures, Figs. 4 and Fig. 5. Per Tab. I,
the 1-grams we track for the political ﬁgures are ‘oba-
ma’, ‘mccain’, ‘romney’, ‘hillary’, and ‘trump’. We dis-
cuss these three connected ﬁgures together.
We make a number of structural elements consistent
across Figs. 3 and 4.
First, except Figs. 3H and 3I, we show all ranks on a
logarithmic scale with limits of r = 1 and 106.
Second, in all nine plots of Fig. 3, we mark the thresh-
old of lexical ultrafame using dotted horizontal lines at
the median rank rgod = 303. We visually demonstrate
the stability of ‘god’ in Fig. 3G, conﬁrming that ‘god’
experiences little rank turbulence [41], as reported by
the statistics at the end of preceding section. We simi-
larly include a dotted line for the rank of ‘god’ in Fig. 4.
We more roughly locate what we call the “lexical abyss”
in Figs. 3 and 4. We suggest the lexical abyss begins to
appear for ranks in the hundreds of thousands, where we
have descended well below the levels populated by com-
monly misspelled words to ﬁnd a wild ecology of strange
lexical creatures.
Third, we indicate US presidential election dates by
vertical dashed lines. In Figs. 3A–G, these are for
2008/11/04, 2012/11/06, and 2016/11/08. In Figs. 3H
and 3I, the ‘obama’ and ‘trump’ rank time series are time-
shifted for direct comparison and the day of the election
is set as day number 0.
Fourth, in Figs. 3A–G, we annotate the date of the
overall highest (most talked about) and lowest ranks for
the reference 1-grams. These dates are also highlighted
in Fig. 4, where we provide example 1-grams typically
found at those ranks.
Fifth and last, in Appendix B, we provide tables of
extreme dates for the political ﬁgures, ‘@bts twt’, and


## Page 6


6
0
200
400
600
800
1000
1200
1400
1600
1800
1
1000
2000
3000
4000
5000
FIG. 3. A–G. Temporal lexical fame on Twitter at the day scale for US presidents, US presidential candidates,
the K-pop BTS, and the word ‘god’ for the time period 2008/09/09 through to 2021/10/24. We deﬁne the lexical
fame of a word as its Zipﬁan rank r based on descending raw usage frequency (see Data and Methods, Secs. II and V). We
display lexical fame on a logarithmic scale covering six orders of magnitude. For the presidents and presidential candidates, we
show time series of the most dominant word used to refer to them out of their ﬁrst name, last name, and Twitter handle (see
Sec. III B and Figs. 6 and 7 for relative usage rates). See Fig. 4 for violin plots corresponding to time series in A–F, and Fig. A1
for the same time series presented in a wide format. We indicate the three US presidential elections occurring within the time
period by vertical dashed lines, and the dates of the highest and lowest lexical fame on all time series. In all panels A–I, the
dotted horizontal line at a word rank of r = 303 registers the global median rank for the word ‘god’ through to 2021/12/31
(panel G), and we consider ranks above 303 to be in the realm of lexical ultrafame. The time series are varied: ‘obama’ has
remained relatively famous throughout; ‘mccain’ and ‘romney’ have low, noisy fame outside of their candidacy periods; ‘hillary’
has remained high post the 2016 election; and ‘trump’ has achieved enduring lexical ultrafame, competing with basic function
words. The band BTS, which most often appears through their Twitter handle, @bts twt, has followed an exponential climb
into a class of lexical ultrafame unto itself, exceeding even that of ‘trump’. I. Comparison of the lexical fame of ‘obama’
and ‘trump’ on Twitter relative to the date of their respective elections in 2008 and 2016 as marked by the
vertical dashed line at d = 0. We also include 50 days before each election. Because ‘obama’ and ‘trump’ are so prominent
on Twitter during these time periods, we are able to display word rank r on a linear scale, rather than the logarithmic one of
panels A–G. □Fix this to go through to end of 2020 only The 1-gram ‘trump’ is remarkable for both its ultrafame level of
rank (median of 191, 2016/06/01–2021/10/24) and consistency. Post inauguration, ‘trump’ never falls below a rank of r = 1541
(which occurred on 2021/04/21). The word ‘obama’ slowly drops in rank in the ﬁrst few years of Obama’s presidency before
stabilizing, and overall shows a great deal more volatility in linear rank than ‘trump’.


## Page 7


7
FIG. 4. Violin plots of lexical fame for US presidents, US presidential candidates, and the K-pop BTS, summa-
rizing the time series of Fig. 3 for 2008/09/09 through to 2020/12/31. The disks on the left provide a scale for word rank at half
decades, with the internal dark gray area proportional to inverse rank. As a guide, the example words for each disk are aligned
with their approximate median word rank for the year 2018, and switch from function words (‘a’, ‘in’, . . . ) to country or region
names (‘america’, ‘argentina’, . . . ). Consistent with Fig. 3, we mark the the lexical ultrafame threshold with a dotted line at
the rank of ‘god’ (note that r = [105/2] = 316 is close to rgod = 303). We indicate the highest and lowest ranks along with the
dates they were attained. We annotate medians for the whole time period, with the exception of the terms ‘hillary’ and ‘trump’,
for which we show medians for before 2015/12/31 and after 2016/06/01, end dates included. For high, low, and median ranks,
we show either function or country words which had similar median ranks in 2018. For Presidents and candidates, only ‘trump’
maintains lexical ultrafame over years (median 191, post 2016/10/01). The highest lexical fame achieved was by the Twitter
handle of the band BTS, @bts twt, reaching a rank of 3 on 2018/05/20, matching the 2018 median rank of the word one of the
most basic English function words: ‘to’.
‘god’. We list the top 10 and bottom 5 rank days for the
entire time span (Tab. A1) as well as at the scale of each
calendar year (Tabs. A2–A9).
We discuss the time series and histograms for the six
political ﬁgures and BTS as displayed in Figs. 3A–3F
and Fig. 4 in order. We then remark on the comparison
of time series for ‘obama’ and ‘trump’ in Figs. 3H and 3I.
Lexical fame dynamics for ‘obama’:
The lexical fame time series for ‘obama’ can be broken
down into two main phases:
1. Starting from a lexical ultrafame heights of Oba-
ma’s 2008 campaign and election, a gradual decline
in being talked about into 2011; and
2. From the middle of 2011 to 2020/06, a largely
steady state with an ultrafame shock for the 2012
election, a minor, years-wide cusp centered around
the 2016 election, and a resurgence around the
COVID-19 pandemic and the Black Lives Matter


## Page 8


8
FIG. 5. Annual levels of ultrafame: Percentage of days per calendar year each 1-gram was ranked above (or
equal to) rgod = 303. Sustained ultrafame is rare. Only 1-grams associated with Trump and BTS have achieved enduring
ultrafame across years. We round percentages to the nearest 0.1 percent, and render 0.0% in a light gray. Both 2008 and 2021
are for part of those years only (2008/09/09–2021/10/24, inclusive).
protests that followed the murder of George Floyd
in Minnesota on 2020/05/25.
As
our
historical
Twitter
data
set
begins
on
2008/09/09, we have on hand just short of two months
of tweets leading up to the election of Obama for his ﬁrst
term. The time series for the 1-gram ‘obama’ starts high,
achieving its highest ever rank of r=14—a level typically
held by the word ‘me’—attained on the date of Obama’s
ﬁrst election, 2008/11/04 (Fig. 4).
At the sub-day time scale of quarter hours, ‘obama’
rose to be ranked ﬁrst among all words, incredibly beat-
ing out ‘the’ and ‘a’. This peak rank for ‘obama’ came
in the 11:00 pm to 11:15 pm time frame on the night of
the election (US Eastern Standard Time). To reach such
heights in a Zipf distribution may seem unfathomable,
and we will oﬀer explanations later in the paper after we
consider ‘@bts twt’.
The overall lowest rank day for ‘obama’ was on
Christmas Day in the third year of Obama’s presidency
(2011/12/25) where the 1-gram dropped to r = 5, 970,
about that of ‘malaysia’ (Fig. 4). (Generally, we see that
major holidays take precedence over politics.) We see
that after a gradual decay in rank, ‘obama’ resurges
abruptly for the 2012 election, and even more abrupt-
ly collapses post re-election—a spike when viewed from
the level of a decade. After level years in 2013 and 2014,
‘obama’ slowly increases in fame again, taking on import
once again around 2016. Post the 2016 election, ‘obama’
has remained high in rank, showing no evident loss of
fame.
In strong contrast to the ﬁve other political ﬁgures we
examine here, lexical fame for ‘obama’ has proved steady,
durable, and relatively high on Twitter, with a median
rank of 1,720 akin to that of ‘uk’, and a unimodal his-
togram (Fig. 4). But in terms of ultrafame, ‘obama’ has
been ranked above ‘god’ on only 2.5% of all days. Per
Fig. 5, ‘obama’ was ultrafamous on 54.4% of the days in
the last four months of 2008, 6.9% of all days in 2009,
and then at most 2.2% for all subsequent years. Oba-
ma was talked about during what would be his year of
re-election (2.2%, 2012) and then at the end of his sec-
ond term (2.0%, 2016) and then the ﬁrst year of Trump’s
presidency (2.2%, 2017). From there, the gradual decline
in the rank of ‘obama’ (Fig. 3A), has meant that in 2019
(2009/01/01 through to 2021/10/24), ‘obama’ has not
once been ultrafamous. Fig. 5 gives a ﬁrst glimpse of the


## Page 9


9
relative dominance of ﬁrst names, last names, and Twit-
ter handles. We see that ‘barack’ and ‘@barackobama’ are
well behind the ultrafame of ‘obama’ with only ‘barack’
registering in 2008 and 2009.
The overall top 10 dates for ‘obama’ (listed in Tab. A1)
all fall on or close to election dates and inauguration
dates. High points at year scales for ‘obama’ (Tab. A2)
are largely tied to political events even when Obama
was not the central actor, e.g., Trump’s election in 2016
(r=90) and inauguration in 2017 (r=95).
In 2018, Obama’s high ranks occurred on Septem-
ber 7 (r=237), 8 (r=265), and 9 (r=381), and were
due to a speech he gave at the University of Illinois at
Urbana-Champaign where he appeared to attack Presi-
dent Trump (“How hard can that be? Saying that Nazis
are bad.”) [42]. The highest rank for ‘obama’ in 2019
was only r=685, the only year in our data set for which
Obama registered zero days of lexical ultrafame.
In 2020, ‘obama’ has spiked on several occasions, ris-
ing to prominence in reaction to the dominant news of
the COVID-19 pandemic and the Black Lives Matter
protests. Obama described the White House’s response
to the COVID-19 pandemic as an “absolute chaotic dis-
aster” in a private call [43] on 2020/05/08, and the
reporting and ampliﬁcation of this story drove Obama’s
name up for more than a week with a high of r=284
on 2020/05/11. Five days after George Floyd’s mur-
der, ‘obama’ spiked again with r=467 on 2020/07/30,
with the volume of stories around the Black Lives Mat-
ter protests limiting the jump. During the Democratic
National Convention, Obama’s name reached highs of
r=371 on 2020/08/18 and r=350 on 2020/08/20, with
the ﬁrst date being due to Michelle Obama’s speech.
At the not-being-talked-about end of the spectrum, the
lowest two days for ‘obama’ fell on New Year’s Day in
2014 and 2015 (r=5,254 and 5,970). Consistently across
1-grams, we see low rank days often occur on dates of
major holidays or non-political events (Tab. A2).
Lexical fame dynamics for ‘mccain’:
We see in Fig. 3B that the time series for ‘mccain’ encom-
passes four main phases:
1. Candidate for president in 2008;
2. US senator;
3. Trump presidency; and
4. Death and legacy.
The rank for ‘mccain’ is highest around the 2008 elec-
tion, with a top rank of r=31 (equivalent to the usual
rank of the function word ‘at’). Occurring on 2008/09/26,
this high water mark for ‘mccain’ was due to interest in
the ﬁrst presidential debate, held at the University of
Mississippi. In 2008, ‘mccain’ was ultrafamous on 39.5%
of recorded days (c.f., 54.4% for ‘obama’, Fig. 5). On
election day, ‘mccain’ was still easily ultrafamous but
it would be only the 1-gram’s fourth-most talked about
date of the year (2008/11/04, r=54).
Across the entire time frame, McCain’s 1-gram fame
level is similar to that of ‘ﬁnland’ (r=41,371) with a
low point on par with ‘sicily’ (2013/12/25, r=250,740)
(Fig. 4). Like ‘obama’, the lexical fame of ‘mccain’ col-
lapsed over time renders a unimodal histogram. Ranking
above ‘god’ on only 1.0% of all days, outside of 2008
‘mccain’ was brieﬂy ultrafamous again in only 2017 and
2018 with rates of 0.3% and 1.1%.
Immediately post election, we see a sharp drop for
‘mccain’ followed by a slow decay in rank over the ensuing
second-phase years, ﬂattening out through 2013–2015.
The lowest-highest rank for ‘mccain’ in a calendar year
was 12,988 in 2014 (Tab. A3). Throughout the Oba-
ma presidency, McCain was often talked about when he
spoke out about decisions made by the Obama adminis-
tration. For example, the second most talked about day
for ‘mccain’ in 2016 arose on 2016/06/16 when McCain
suggested that Obama’s foreign policy led to the Pulse
nightclub shooting Orlando (r=3,491; Tab. A3).
Starting in 2015, leading up to and elevating through
the 2016 election, the time series for ‘mccain’ enters a
third stage which is one of high ﬂuctuations as it begins
to track McCain’s increasingly antagonistic relationship
with President Trump. The incipient event appears to
have been Trump’s dismissal of McCain’s record as pris-
oner of war in Vietnam [44]—“He’s not a war hero. He’s
a war hero because he was captured. I like people who
weren’t captured”—which led to the most talked about
sequence of days in 2015 for ‘mccain’ (peak: 2015/07/18,
r = 2, 557). (We note that some of the later mentions
of ‘mccain’ will be due to McCain’s daughter Meghan
McCain, a public ﬁgure herself by this time.)
Marking the transition into a fourth phase, the high-
est rank for ‘mccain’ in 2016 fell on Election Day
(2016/11/08, r=2,383). McCain had won re-election to
the US senate himself, and his withdrawn support for
Trump took on heightened salience with Trump’s win.
In 2017, McCain’s thumbs-down vote against in the
senate to defeat a bill to end the Aﬀordable Care Act
generated a return to the realm of lexical ultrafame for
the ﬁrst time since 2008 (2017/07/28, r=252; Tab. A3).
In 2018, his death on August 25 led to a series of
lexical ultrafame days (2018/08/25, r=190; 2018/08/26,
r=128). The only top-10 day in 2018 that was not relat-
ed to McCain’s passing came on 2018/05/11 when Kelly
Sadler, a White House aide, was reported to have said
that McCain’s opinion on Gina Haspel’s nomination for
CIA director was irrelevant because “he’s dying anyway.”
After McCain’s death, ‘mccain’ has remained a Twitter
1-gram staple, in part due to Trump maintaining what
had emphatically become an argument in which only one
side could engage. The high rank of r=603 on 2019/03/20
was due to Trump [45] who took aim at McCain in a
speech on manufacturing jobs: “I have to be honest: I’ve
never liked him much” [45]. In early September 2020,
‘mccain’ reached r=955 after Jeﬀrey Goldberg’s pub-


## Page 10


10
lished article in the Atlantic which reported that Trump
had disparaged US military service members and veter-
ans [46].
Lexical fame dynamics for ‘romney’:
As we did for ‘mccain’, we can identify four phases for
the time series for ‘romney’ in Fig. 3C:
1. Abiding in the lexical abyss: Low fame through to
the end of 2010;
2. A mostly uniform build to the 2012 election;
3. Through to the 2016 election, a regime of fame
higher and less volatile than the ﬁrst phase; and
4. A return to the lexical abyss, characteristic of the
ﬁrst phase.
Romney’s 1-gram has the lowest overall median rank of
the six political ﬁgures, tantamount to that of ‘haiti’ and
again produces a unimodal histogram (r=62,673, Fig. 4).
The low and high points for ‘romney’ bookend the two-
year-long second phase of his fame time series. Romney’s
1-gram rose from the lexical abyss dwelling of r=813,435
(similar to ‘guangxi’) on 2010/08/15 to an ultrafamous
r=33 (similar to the function word ‘your’) on the 2012
election day (2012/11/06).
The 1-gram ‘romney’ was ultrafamous on 0.1% of all
days in our study—a total of only 6 days with rromney ≤
rgod = 303. Per Fig. 5 and Tab. A1, all of these days
occurred around the 2012 election (1.7% of 2012).
In the third phase of the time series, ‘romney’ slowly
gains fame as the 2016 election approaches, spiking on
a few isolated occasions, and then once again in 2019.
Unlike ‘obama’ and ‘mccain’, two of the top 10 over-
all days for ‘romney’ do not fall around election dates
directly involving Romney. In Tab. A1, the 7th and 10th
ranked days for ‘romney’ are 2020/02/05 and 2019/01/02
(r=457). Further, outside of 2012, these are only two of
four days on which ‘romney’ was ranked in the top 1000
1-grams.
Like McCain, Romney had had contentious public
interactions with Trump, and we see the cause of both of
these two major spikes was Romney speaking out against
Trump. On 2016/03/03, Romney gave a speech at the
University of Utah in which he attacked (then potential
nominee) Trump calling him a ‘fraud’ and asked voters
to strategically vote against him [47]. Almost three years
later on 2019/01/01, having been elected a senator for
Utah two months prior, Romney published a stir-causing
opinion piece in the Washington Post regarding his neg-
ative view of Trump’s character [48]. On 2020/02/05,
Romney’s lone Republican vote in the Senate to con-
vict Trump on one impeachment charge again abrupt-
ly elevated Romney’s name (r=288). All of these spikes
evaporated, leaving no evident residual.
Lexical fame dynamics for ‘hillary’:
The lexical fame time series for Hillary Clinton’s dom-
inant 1-gram ‘hillary’ in Fig. 3D traverses three major
phases:
1. A gradual initial decay to a stable moderate lexical
fame through the end of 2014;
2. Two year build towards the 2016 election;
3. A new lexical fame regime, above that of the ﬁrst
phase, relatively stable but gradually falling away.
Our time frame begins after Clinton’s unsuccessful
campaign for the Democratic presidential nomination for
the 2008 election, and the starting point for ‘hillary’
comes part way into a consequent drop in lexical fame.
As Obama’s Secretary of State during his ﬁrst term,
Clinton maintained a degree of public prominence that
slowed a fall towards the lexical abyss. Until the year
2015, ‘hillary’ was ranked in the top 1000 on a solitary
day, the one on which the possibility of her becoming
Secretary of State was made public (2008/11/14, r=910,
Tab. A5). The nadir for the 1-gram ‘hillary’ landed on
2012/12/25, Christmas Day (r=71,445, similar to that
of ‘rwanda’; Fig. 4 and Tab. A5).
The second phase for ‘hillary’ is a two-year linear
ascent in log10 r starting 2015/01. There are a few spikes
during this period, notably the day Clinton declared her
candidacy (2015/04/12, r=662, Tab. A5; and the ﬁrst
Democratic debate (2015/10/13, r=446, Tab. A5)
After a vacation lull at the end of 2015, the ﬁrst half of
2016 saw ‘hillary’ jump and maintain a high fame level
of around a rank of r=1,000. Once Clinton became the
Democratic nominee, ‘hillary’ once again began to climb
in rank. The ﬁrst presidential debate (held at Hofstra
University) between Clinton and Trump led to the third
highest rank overall for ‘hillary’ and the ﬁrst time Clin-
ton’s 1-gram had achieved lexical ultrafame (2016/09/26,
r=89, Tab. A1).
The second phase for ‘hillary’ ends with Clinton’s loss
in the 2016 election, the date of which would prove
to be the all-time top rank for ‘hillary’ (2016/11/08,
r=50, Tab. A1). A rank of 50—the typical return for the
word ‘was’ (Fig. 5)—is lower than that achieved by both
‘mccain’ and ‘romney’, and is possibly in part to ‘hillary’
being one of several 1-gram’s used to refer to Clinton.
Indeed, the day of the 2016 election would be the high
rank for ‘clinton’ over the entire time frame (r=99).
The year 2016 is the only year in which ‘hillary’ would
achieve any level of lexical ultrafame (10.7% of all days
in 2016, Fig. 5). Both ‘clinton’ and ‘@hillaryclinton’ were
also ultrafamous (7.9% and 1.1%). All told, ‘hillary’ was
ultrafamous on 0.8% of all days over the entire period of
study, all of them contained in 2016.
After the election, ‘hillary’ falls abruptly, a shock
transition to the third phase of Clinton’s lexical fame.
In the three following years, ‘hillary’ trends gradually
downwards, reﬂected in the high ranks for 2017, 2018,


## Page 11


11
2019, and 2020: r=536 on 2017/11/03, following book-
delivered accusations by Donna Brazile that Clinton con-
trolled the Democratic National Committee; r=713 on
2018/07/16, apparently due to remarks by Russian Pres-
ident Vladimir Putin in a meeting with Trump in Helsin-
ki, in which he stated that he wanted Trump to win;
r=528 on 2019/10/19, arising in part from the conclu-
sion of a State Department investigation into Clinton’s
email server usage, as well as Clinton suggesting that
Tulsi Gabbard was being groomed by Russia; and r=933
on 2020/02/01, after Rashida Tlaib booed Clinton at a
Bernie Sanders rally in Iowa.
But Clinton’s lexical fame moved to a substantially
higher level relative to the ﬁrst phase. The typical ranks
for the ﬁrst and third phases for ‘hillary’ roughly diﬀer by
an order of magnitude (see Fig. 4). Before 2015/12/31,
the median rank for ‘hillary’ was r=23,829, on par with
‘greece’. Post 2016/10/01, the median rank has elevated
to 3,139, matching the level of ‘argentina’.
Such a clear shift in levels of being talked about is
not what we saw for ‘romney’ for which we have before-
and after-election phases that match in statistical char-
acter (we do not have data for ‘mccain’ prior to the 2008
election). Clinton has been talked about much more in a
stage of her career where she has no public position than
an earlier one where she was Secretary of State for the
US.
The two distinct quasi-stationary regimes for ‘hillary’
lead to a bimodal histogram in Fig. 4, in contrast to the
unimodal histograms of ‘obama’, ‘mccain’, and ‘romney’.
Lexical fame dynamics for ‘trump’:
The top 10 ranked dates for ‘trump’ fall, as we might
expect, on or adjacent to the presidential debates in
2016, the 2016 election, and Trump’s 2017 inauguration
(Tab. A1). There is however much other structure to dis-
cern, and we work through the rich details of the lexical
fame time series for ‘trump’, which has four major phases
(Fig. 3E):
1. A brief initial increase in lexical fame reaching a
cusp centered around August of 2009;
2. A slow, birtherism-punctuated descent into the lex-
ical abyss running into 2015;
3. Starting with a shock transition on 2015/06/15, an
upward trajectory until the 2016 election;
4. The Trump presidency, a period where the word
‘trump’ has established an enduring level of lexical
ultrafame.
The ﬁrst phase for ‘trump’ sees a rise to a cusp point
with ranks in the 3000s. Of the one-day spikes (see
Fig. 3E and Tab. A1), stories that failed to persist, we see
a range of causes that are political and business-related.
On 2008/10/15, ‘trump’ reached a high for 2008 of
r=5,249, following his statement in a CNN interview with
Wolf Blitzer that Nancy Pelosi should have impeached
President George W. Bush over the Iraq War [49] (Trump
was a registered Democrat into 2009).
The highest point for ‘trump’ over the ﬁrst few years
fell on 2009/05/12, when the 1-gram reached r=1,668
after Trump asserted that Carrie Prejean could keep
her title, Miss California USA, after she publically
said she did not support same-sex marriage enraging
pageant judge Perez Hilton and, more broadly, the inter-
net [50]. Less than a month later, Trump would be
involved in ﬁring Prejean for shirking duties set out by
her contract [51], making for another spike (r=3,670,
2009/06/10).
The second highest rank for ‘trump’ in 2009, r=3,227,
came on what was very much a bad news day: On
2009/02/17, Trump Entertainment Resorts and nine
related Trump companies all ﬁled for bankruptcy [52].
The cusp marking the transition from the ﬁrst to the
second phase for ‘trump’ appears to match with the 2008
Miss Universe pageant held in the Bahamas. (r=3,617,
2009/08/23). After this point, ‘trump’ goes into a long,
slow descent, interrupted by occasional spikes and one
strong resurgence which traces Trump’s major role in the
birther conspiracy theory movement which claimed that
Obama was not born in the United States [53], and his
non-unconnected consideration of a presidential run for
the 2012 election.
In Fig. 3E we see ‘trump’ break from its downward
trend in the second half of 2010, build rapidly to a high
rank of r=734 on 2011/04/27, (the day on which Obama
released his long form birth certiﬁcate), and then drop
sharply shortly thereafter. The rank r=734 would be the
highest overall for ‘trump’ until 2015.
On 2011/04/30, Trump was extensively mocked at
the White House Correspondents’ Dinner by president
Obama and the host Seth Meyers. The following day,
2011/05/01, the rank for ‘trump’ reached back up to
r=829, the only other date ‘trump’ would make the top
1000 until 2015.
A few weeks later, on 2011/05/16, Trump announced
that he would not seek the republican nomination;
‘trump’ jumped back up to r=1,629, and then fell back
into what would become an ambient six-year long down-
ward trend. Looking back, ‘trump’ had enjoyed half a
year of being talked about more and more, albeit with
strongly disjoint story frames of successful tycoon or blus-
tering buﬀoon.
From mid 2011 to mid 2015, ‘trump’ inhabited the lex-
ical abyss, ﬁnding a ‘tanzania’-equivalent low point of
r=81,022 on 2013/10/26. The lack-of-fame problems for
‘trump’ were strongest in 2014 where the highest rank for
the untalked-about ‘trump’ was r=13,069 on 2014/09/29
(Tab. A6). There were a few spikes for ‘trump’ during
this time period, two of note around the 2012 election
(r=1,627 on 2012/10/24 and r=1,921 on 2012/11/07).
The third phase begins with a shock transition on
2015/06/16, the day Trump announced his candidacy.
The 1-gram ‘trump’ jumped from r=24,772 the day


## Page 12


12
before up to r=621. Just ﬁve days before, ‘trump’ was
at r=41,090. From not being able to break into the top
10,000 1-grams in 2014, ‘trump’ now reached well inside
the top 1,000 on many dates in 2015. On 2015/12/08,
‘trump’ was ranked 231. Having been ranked as low as
70,230 in 2015, ‘trump’ would not fall below 1,297 in 2016
(Tab. A6).
Post declaration of candidacy, ‘trump’ rises steadily
for the next 17 months, peaking at r = 12—normally
where the word ‘is’ is—the day after the 2016 election
(2016/11/09).
In 25 of 192 quarter hour intervals on 2016/11/08 and
2016/11/09, ‘trump’ was ranked a staggering 4th over-
all, mostly in the late hours of election day and early
morning hours of the following day. The highest rank
‘hillary’ achieved during these two days was 22nd. This
peak came in the quarter hour starting at 9 pm on the
night of the election (2016/11/08), before ‘hillary’ began
to drop down as Trump started to become perceived as
the likely winner.
After a minor relative draw down post election,
‘trump’ surges again at Trump’s inauguration (r=20,
2017/01/20). The time series for ‘trump’ then settles into
an a scoreboard-shattering fourth phase, a stable, low-
volatility ultrafamous regime (Fig. 3E).
During the fourth phase, Trump’s presidency, a few
dates stand out (Tab. A6). These dates have largely been
highly controversial, diverse in nature, and of course, gen-
erative of enormous coverage and reaction. We will report
on distinct events that lifted ‘trump’ to the top 10 rank
for each calendar year.
In 2017, the 8th most talked about day for ‘trump’
and the only non-inauguration related day in the top
10 for that year (2017/08/15, r=62), fell on the Tues-
day after the Charlottesville white supremacist rally on
August 11 and 12, and the death of protester Heather
Heyer on August 12. On that Tuesday, Trump present-
ed what would be a third statement of his regarding the
violence, a walking back of a walking back, best captured
by his assertion that there were “very ﬁne people on both
sides”.
In 2018, ‘trump’ peaked at r=63 on 2018/07/16, the
date of the Russian-United States summit in Helsinki
when Putin expressed his preference for Trump.
On 2018/01/12, a rank of r=89 (4th highest for 2018),
followed from Trump being reported as saying that fewer
immigrants should come from “shithole” countries, and
more from places like Norway [54].
On 2018/06/20 (r=92, 5th highest for 2018), Trump
signed an Executive Order to end forced separation of
migrant families.
The North Korea-United States summit in Singapore
was held on 2018/06/12, delivered ‘trump’ to a rank of
r=95, the 6th highest for 2018.
Trump’s ﬁrst State of the Union address on 2018/01/30
elevated ‘trump’ to r=105, 9th highest for the year.
The highest rank day in 2019 was 2019/12/18 (r=67),
and the third highest the day after (r=89).
The second highest rank day in 2019 was 2019/09/25.
On 2019/09/24, Nancy Pelosi, the Speaker of the
House, announced that impeachment proceedings would
begin against Trump. Three relevant 1-grams that had
their highest ever ranks to date on 2019/09/25 were
‘ukraine’ (r=264), ‘transcript’ (r=306), and ‘whistle-
blower’ (r=700).
Earlier in the year on 2019/01/25, Trump signed a bill
to reopen government after a prolonged shutdown, back-
ing down over demands to fund the US-Mexico border
wall. On that day, ‘trump’ reached a high that would last
until the impeachment inquiry with r=112. Three other
related dates in January were also days of high ranks for
‘trump’.
The start of a second summit with Kim Jong Un, this
time in Hanoi, provided the another high ranked day on
2019/02/27 (r=114).
Trump’s attacks on four congresswomen, coupled with
“Send her back” chants at his rallies, provided the further
highly ranked days of 2019 (2019/07/18, r=122).
One relatively low controversy date that stood out was
2019/02/05 on which Trump gave his second State of the
Union address, leading to a rank of 125 for ‘trump’.
For the whole time span, ‘trump’ has been ultrafa-
mous on 33.9% of all days. After ﬁrst experiencing lexi-
cal ultrafame in 2015 (0.6%), the ‘trump’ shock in 2016
lead to 49.0% of days being ultrafamous in that year
(Fig. 5). In 2017, 2018, and 2019, ‘trump’ stayed extreme-
ly high, with ultrafame rates of 98.3%, 93.4%, and 92.1%.
Trump’s low ranks during his presidency help show the
persistence of fame: r=384 on 2017/12/25, r=405 on
2018/09/23, and r=385 on 2019/09/01. We also see the
rise of @realdonaldtrump, with ultrafame levels in 2017,
2018, and 2019 of 26.5%, 41.1%, and 60.7%.
The year of 2020 has been unarguably tumultuous
across the world. The COVID-19 pandemic has been the
globally dominant story. In the US and with ramiﬁca-
tions abroad, the murder of George Floyd and the ensu-
ing Black Lives Matter protests have been the only other
major sustained story.
In 2020, the dates surrounding the US presidential elec-
tion (2020/11/04), the contentious ﬁrst debate with Joe
Biden (2020/09/29), and Trump’s contraction of COVID-
19 (2020/10/02) would prove to be the high points for
‘trump’ (see Tab. A6).
Adding in the unrest leading up to and following the
2020 election, in part instigated by Trump’s rhetoric,
‘trump’ has been mentioned at sustained rates higher
than ever before. After starting the year at a rank of
r=294 on New Year’s Day, the day-scale rank of ‘trump’
did not fallen below 302, meaning that ‘trump’ sustained
ultrafame for the entirety of 2020 (Tab. A6). Trump’s
handle ‘@realdonaldtrump’ continued to grow in usage
(through retweets and mentions) ending with an ultra-
fame rate of 90.2% (Fig. 5).
Trump’s Twitter handle is the only one for the six
political ﬁgures that ever earns sustained ultrafame. We
discuss how Twitter handles function further below when


## Page 13


13
we make sense of the fame of @bts twt.
We have made separate analyses of Zipf distribu-
tions for a day of Twitter versus the same day with
retweets excluded. While removing retweets dropped
‘trump’ in rankings, we observed the opposite for ‘@real-
donaldtrump’. Trump’s Twitter handle appears then to
be involved more strongly in replies and fresh mentions
than retweets.
For the start of 2021, the violent incursion into the US
Capitol by Trump supporters has lifted rates of ‘trump’
even higher. The ban of Trump’s account though means
that his handle’s counts would be 0 from 2021/01/09
on. Post the Capitol insurrection and ban, ‘trump’ fell
in rank to around r=1000, where it remained roughly
through the end of 2021/05. How long Trump will stay
so central to the discourse on Twitter is unpredictable.
Like ‘hillary’, the histogram for ‘trump’ is bimodal
(Fig. 4). Before 2015/12/31, the median rank for ‘trump’
was r=22,046, the level of ‘afghanistan’.
But unlike ‘hillary’ or any of the other political ﬁg-
ures, the level ‘trump’ reaches and holds in the fourth
phase of the fame time series is that of ultrafame. From
2016/10/01 to 2020/12/31, the median rank for ‘trump’
was r=179, on par with the typical rank of the word
‘after’. Beyond the scales of country 1-grams, such a rank
is typical of the function word ‘say’.
Lexical fame dynamics for ‘biden’:
The 1-gram ‘biden’ travels through three large-scale
phases:
1. An exponential fall from 2008 through 2012;
2. A generally stable period of low rank from 2012
through to the end of 2018, with modest cusps
around the 2012 and 2016 US presidential elections
(see Figs. 3 and A1).
3. After a jump at the start of 2019, an exponen-
tial rise through to the 2020 US presidential elec-
tion, with the early suggestion of a cusp peaking on
2020/11/07.
We record just a few observations regarding ‘biden’,
leaving analysis of his social media imprint as president
to future work.
The high point for ‘biden’ comes on the Saturday
(2020/11/07) after the Tuesday 2020 US presidential
election, when the race was called in his favor by most
major news outlets in. Up until 2020, ‘biden’ had only
experienced 3 days of ultrafame. In 2020, the median rank
for ‘biden’ was 683, akin to that of the word ‘army’. The
ultrafame rate for ‘biden’ in 2020 was 23.8%, which is
the highest level for a full year across our data set for all
ﬁgures except Trump.
Biden’s volume rises on Twitter through the Demo-
cratic primaries, due to incidents that led to and includ-
ing the impeachment of Trump over Trump’s election
interference involving Ukraine, and then again with
the 2020 election itself. The ﬁrst presidential candidate
debate was the overall high point until that time for
‘biden’, eclipsed by the post election general acknowl-
edgment of his victory.
We note that as for the ﬁrst ﬁve political ﬁgures, fam-
ily members being mentioned online add to their promi-
nence. For Biden, his sons Beau and Hunter and his wife
Jill have been discussed online
Lexical fame dynamics for ‘@bts twt’:
We come to the extraordinary lexical fame time series
for the seven-member K-pop band BTS, as carried by
their Twitter handle, ‘@bts twt’ (Fig. 3F). BTS’s emer-
gence, fame, and now central role in the K-pop industry
has been studied from a few angles by others [19–22].
Purposefully fostered by South Korea’s Ministry of Cul-
ture in the 1990s, South Korea’s development and export
of cultural products led to the “Korean Wave” expand-
ing across Asia in the 2000s [55, 56], and then a global
explosion in the 2010s. BTS’s fame has translated into
real money, and they have substantially impacted the
South Korean economy as well as sales for the global
music industry [22].
The main phases for BTS’s lexical fame are:
1. Spending the ﬁrst half of 2013 in the lexical abyss;
2. A ruthless march towards the realm of lexical ultra-
fame from mid 2013 through to the end of 2017;
3. Lexical ultrafame from the start of 2018 to May
2019.
4. A gradual drop from May 2019 while still maintain-
ing lexical ultrafame, and then a resurgence in the
middle of 2020.
After breaching the top 106 of 1-grams on 2012/12/22,
‘@bts twt’ remained in the lexical abyss and did not
break the r=105 mark until around the time BTS
released their debut album ‘2 Cool 4 Skool’ and single
‘No More Dream’ on 2013/06/12.
Though the reception of BTS’s ﬁrst album and sin-
gles did not much portend for global success—on Korean
charts, ‘2 Cool 4 Skool’ reached #5, the lead song would
only reach #124, and the band’s second single failed com-
mercially [57]—the band had entered what would become
the second phase of their lexical fame. The ascent of
‘@bts twt’ to lexical ultrafame is linear in log10 r and
thus exponential in r (Fig. 3F).
In 2014, the median rank for ‘@bts twt’ was at the level
of ‘pakistan’ (r=5,065, Fig. 4). By 2016, the median rank
had climbed to 804, on par with the word ‘hit’. For 2018
and 2019, the third phase of ‘@bts twt’, BTS’s handle
stabilized around a standard usually held by the word
‘they’ (r=67).
The highest ranks for ‘@bts twt’ for each calendar year
even more strongly show the explosion of BTS’s lexi-
cal fame (Tab. A8): r=967 on 2014/12/31, r=176 on
2015/12/29, r=99 on 2016/12/29, r=9 on 2017/05/21,


## Page 14


14
to the almost incomprehensible r=3 on 2018/05/20, and
then dropping to highs of 12 and 17 in 2019 and 2020. For
comparison, the function word ‘of’ is on average ranked
9th, and ‘to’ is on average ranked 3rd, with only ‘a’ and
‘the’ above at ranks 1 and 2.
If we descend below the day scale, we ﬁnd that at
the level of ﬁfteen minute time intervals on 2018/05/20,
‘@bts twt’ was in fact ranked ﬁrst overall in 17 out of 96
quarter hours. perhaps a reﬂection of a truly global dedi-
cated fan base, perhaps a testament to the gameability of
Twitter, it remains that a non-function word being able
to beat out all other 1-grams for lexical fame on a global
social media platform with myriad competing entities is
a truly remarkable phenomenon.
For 2019, the highest rank for ‘@bts twt’ slipped to
r=12 (2019/05/01). Overall, BTS’s handle has been
ranked in the top 10 1-grams on 6 days (Tab. A1).
The calendar year lexical ultrafame rates for ‘@bts twt’
again show their astonishing rise (Fig. 5): 0.6% in 2015,
8.2% in 2016, 50.6% in 2017, 100% in both 2018 and
2019, and then slightly dropping to 98.9% in 2020. The
lowest ranks in 2018 and 2019 for ‘@bts twt’ were 267 and
257 (Tab. A8). Running from 2012/12/22 to 2021/10/24,
‘@bts twt’ was ultrafamous on 50.0% of all days.
How can an entity compete against the most basic
function words of a language? While Coke did once assert
itself to be ‘it’, a marketing goal of making the word ‘coke’
be used as much as the word ‘it’ would be (hopefully)
laughed out the door. A rank of 3 for a non-function
word would not be normal for, say, a typical book. In
Moby Dick, a deeply cetacean-rich text, ‘whale’ is the
most frequent non-function word and is ranked 28th.
But Twitter is a complicated melange of text. At times,
sub-populations take on the character of a chanting, echo-
ing crowd. In general, retweets, replies, and mentions all
combine to drive up counts of Twitter handles. Fandoms
are especially capable of harnessing the mechanisms of
social media [58, 59]. BTS’s fan club, ARMY, is a globally
formidable following, and most tweets from the account
@bts twt rapidly garner massive numbers of interactions,
far exceeding that of US political ﬁgures.
While some degree of the activity around @bts twt
may be algorithmic in nature—as is true for any major
ﬁgures on Twitter—we leave such quantiﬁcation to other
work as we are focused on the overall observables of the
system.
The high ranks of 9, 3, and 12 for ‘@bts twt’ in 2017,
2018, and 2019 are tied to the annual Billboard Music
Awards. BTS won Top Social Artist in each of these three
years, ending Justin Bieber’s winning streak from the
award’s inception in 2011 to 2016. (Three of the ﬁve nom-
inees in 2019 were K-pop bands.) On the day ‘@bts twt’
was ranked 3rd (2018/05/20), the hashtag ‘#ivotebtsbb-
mas’ reached r=7 (bbmas = Billboard Music Awards),
reﬂecting the eﬀorts of ARMY. In 2019, BTS won Bill-
board’s music award for Top Duo/Group, the ﬁrst year
in which they were nominated.
Lexical fame dynamics for ‘obama’ vs. ‘trump’:
In bridging to the next section on relative fame rates,
we move on from our discussion of individual fame
dynamics by returning to Fig. 3 to consider two side-
by-side comparisons of ‘obama’ and ‘trump’.
In Fig. 3H, we overlay the lexical fame time series for
‘obama’ and ‘trump’ with the ﬁrst term election days for
both presidents shifted to day number 0. We show rank
on a linear scale rather than logarithmic, and include the
‘god’ line for ultrafame once again.
Fig. 3H shows that ‘obama’ and ‘trump’ follow time
series of divergent character. Per our analysis of ‘trump’,
the 1-gram ‘trump’ remains ultrafamously high through
around 1500 days, falling below ‘god’ on less than 10% of
days, and showing very little volatility on a linear scale.
By contrast, ‘obama’ falls away steadily through Oba-
ma’s ﬁrst term, and shows much greater ﬂuctuations. We
again see that ‘trump’ is constantly a dominant feature
of Twitter’s story-space, whereas ‘obama’, while ‘uk’-
level famous, experiences a much more variable intensity.
There are days oﬀfor ‘obama’ but not for ‘trump’ (and
never for ‘@bts twt’).
B.
Direct comparisons of lexical fame
We turn now to lexical fame comparisons of 1-grams
with each other and themselves, within and across time
frames. To do so, we must move to considering normal-
ized counts rather than ranks. Our aim is to be able to
estimate relative numbers of mentions. For example, in
processing tweets from 2016, we want to be able to deter-
mine how many mentions of ‘hillary’ we should expect
for every 1000 mentions of ‘trump’, and what would be
equivalent number of mentions of ‘obama’ and ‘mccain’
in 2008, ‘@bts twt’ in 2018, and so on.
We take some care to address the complications aris-
ing from the extremely heavy-tailed Zipf distributions
produced by Twitter. With ranks, we did not have to
concern ourselves with the nature of the rare, that is, the
tails of highly skewed distributions. (We of course derived
ranks from counts which are less informative than proper-
ly normalized relative frequencies.) We argue that we can
meaningfully interpret normalized counts as rates rather
than probabilities.
To measure rates of 1-grams, we would seem to need
the total number of 1-grams per time interval of inter-
est, which we will continue to take here to be the day
scale. We would appear to have a problem in that we do
not know these overall counts of all 1-grams as we only
know that our data set comprises approximately, and not
exactly, 10% of all tweets per day. But again this is only
a problem for the tail of our distributions. For non-rare
words, we are able to accurately compute rates by nor-
malizing counts by the total number of 1-grams we ﬁnd
we have on hand per day. More data will only modify the
tails of the distributions that we are able to deduce for
our subset of all tweets (we note that the hapax legomena


## Page 15


15
FIG. 6. Relative median rates of lexical fame for pres-
idents and major candidates in the eight weeks lead-
ing up to the 2008, 2012, and 2016 elections, normal-
ized across terms and years using a ‘god’ as an anchor (see
Sec. III B). By median rate, the most talked about relatively
was ‘obama’ in 2008. We choose to set ‘obama’ in 2008 to have
an anchoring base rate of 1000 (light text, dark gray bar). In
processing a stream of tweets in a given time frame, for every
1000 ‘obama’s encountered in 2008, all other numbers show
the relative median rate of the number of expected mentions.
For example, a relative count of ‘mccain’ in 2008 shows ‘oba-
ma’ had a roughly 4:3 advantage on Twitter (1000:757). The
2012 election was much less talked about with ‘obama’ drop-
ping to 141, with roughly a 9:8 advantage over his opponent
‘romney’ (132:117). In 2016, ‘trump’ outpaced ‘hillary’ by a
much stronger ratio of nearly 2:1 (656:357). At a relative medi-
an rate of 656, ‘trump’ in 2016 was relatively less talked about
than ‘obama’ in 2008 pre-election, in part due to the much
increased volume of Twitter. Over the three elections, only in
2016 did the handles of the candidates, ‘@hillaryclinton’ and
‘@realdonaldtrump’, garner substantial mentions. We include
‘@bts twt’ and ‘god’ for comparisons.
for our daily Twitter Zipf distributions are largely Twit-
ter handles). There are substantive ramiﬁcations here
for computing fundamental whole-distribution measures,
from simple statistics such as moments to quantities such
as the Gini coeﬃcient and Shannon’s entropy [60]. Here,
we are able to continue on our way with our focus being
on 1-grams that are for the most part non-rare.
We generate our rate analysis in two steps. We explain
how as we present our last two main ﬁgures. In Fig. 6, for
the 8 weeks leading up to the last three elections, we show
relative median rates for the ﬁrst name, last name, and
Twitter handle of all six political ﬁgures, BTS’s Twitter
handle, and ‘god’. In Fig. 7, we show relative rates for
the same 1-grams at the scale of the calendar years 2008
through to 2019, inclusive, and for days on which we have
data.
We introduce some notation to aid our explanation.
On date d, we write the number of counts of term τ as
Nτ,d,
(1)
and the rate of term τ, the normalized count, as:
Rτ,d =
Nτ,d
P
τ ′ Nτ ′,d
,
(2)
where the sum is over all unique terms observed on
date d. In general, we will use D to represent a set of
days with a suitable subscript. For example, we write
Dy for the set of days in year y. So, for the year 2018,
D2018 = {2018/01/01, 2018/01/02, . . . , 2018/12/31}. For
the 8 weeks leading up the US presidential elec-
tion in 2016, we would write D8w pre-2016 election
=
{2016/09/13, 2016/09/14, . . . , 2016/11/07}.
For each 1-gram τ and each time frame D, we compute
the median daily rate. (We note that the median is invari-
ant under logarithmic transformation.) For example, for
‘trump’ in 2017, we would determine
medd∈D2017 R‘trump’,d,
(3)
where we use med to denote the median operator.
To now make comparisons across time periods inter-
pretable, we renormalize all values so that the maximum
median rate for all political ﬁgure 1-grams is 1000, round-
ing to the nearest integer. The maximum median rate is
Rmax = max
τ,D medd∈D Rτ,d,
(4)
where τ and D range across the political ﬁgures’ 1-grams
and the time frames being compared. So, for example,
the relative median rate for ‘trump’ in 2019 would be:
Rrel
‘trump’,D2019 = 1000
Rmax medd∈D2019 R‘trump’,d.
(5)
We add that if we were interested only in comparing
median rates of 1-grams within the same time frame, we
could do so without computing rates at all. For example,
for a time frame D, we could compute the median of daily
ratios of counts for any two 1-grams. It is only when we
want to compare across diﬀerent time ranges that we
must properly include rates.
We can now properly discuss Figs. 6 and 7. The lexical
fame balance for the three pre-election periods in Fig. 6
have distinct characteristics. For 2008, ‘obama’ held a
1000:757 advantage over ‘mccain’ (roughly 4:3) and both
were relatively more talked about than any other politi-
cal ﬁgure later on (ﬁrst column of Fig. 6). (We note that


## Page 16


16
FIG. 7. Relative median rates of lexical fame for Presidents Obama and Trump and major candidates at the
level of years. Using the same approach as Fig. 6, we determine ‘trump’ in 2017 to have the highest median rate and set that
term to be the standard with a rate of 1000 (light text, dark gray bar). In 2018, the second year of his presidency, ‘trump’
declined modestly to 873. The corresponding years for ‘obama’ give 367 and 151, both well below ‘trump’ and showing a steep
ﬁrst year to second year decline. We again include ‘@bts twt’ and ‘god’. After Twitter’s early growth, we see ‘god’ stabilize
from 2014 on. The rapid growth of ‘@bts twt’ brings the handle to a median relative median rate of 2489 in 2018, registering an
almost 3:1 ratio over ‘trump’ in the same year (2489:865). We note that this relative median rate comparison ﬁgure may seem
similar in appearance to that of Fig. 5, but the conception and underlying calculations are diﬀerent, and are worth examining
separately. The year 2021 is partial with data running through to 2021/10/24.
the common name ‘john’ was inﬂated by McCain’s fame.)
We may speculate that ‘obama’ led all three pre-elections
in fame in part because Twitter had a smaller user base
in 2008 than in 2012 and 2016, and so there was less
competition for lexical fame across all topics. Automat-
ically generated content due to bots was also likely less
prevalent.
For the 2012 election, ‘obama’ again had an advantage
of lexical fame, trimmed somewhat to 132:117 over ‘rom-
ney’ (equivalently 1000:892, roughly 9:8, second column
of Fig. 6). A much stronger distinction is that both ‘oba-
ma’ and ‘romney’ consumed far less lexical fame space,
with a relative median rate of 1000 dropping to 132 for
‘obama’, a factor of more than 7 lower than before the
2008 election.
Pre-election Twitter for 2016 shows ‘trump’ outpacing
‘hillary’ and ‘clinton’ by almost a 2:1 ratio at 656:357
(equivalently 1000:544, third column of Fig. 6). Both
Clinton and Trump’s Twitter handles also rise in lexi-
cal fame, in strong contrast to the handles of the other
three political ﬁgures, an eﬀect of increased mentions and
retweeting.
In short, while ‘trump’ was relatively less talked about
than ‘obama’ in the lead up to their respective ﬁrst elec-
tions by a 656:1000 ratio (roughly 2:3), references to
Trump dominated those of his opponent Clinton well
ahead of the smaller margins held by references to Oba-
ma over McCain and Romney.
In Fig. 7, we expand the same analysis out to the full
time span of our Twitter data set, broken into calendar
years. While for the full data set, we have established
much with the time series in Fig. 3 and the histograms
in Fig. 4, the relative median rates in Fig. 7 allow us to
gather further insight with hard numbers.
For political ﬁgures, the most prevalent 1-gram is now
‘trump’ in 2017, the ﬁrst year of Trump’s presidency, and
we set that median rate to a standard of 1000.
Overall, we again see the overwhelming dominance of
‘trump’ against the 1-grams of the other ﬁve political
ﬁgures. In the ﬁnal months of 2008, ‘obama’ performs
strongly with a relative median rate of 898, carries a rel-
ative median rate of 379 through 2009, but then falls and
holds around a relative median rate 100 to 150 there-
after, well below ‘trump’. In 2016 as a whole, ‘trump’
outweighed ‘hillary’ in mentions by a ratio of nearly 7:2
(592:170).


## Page 17


17
From
2015,
Trump’s
Twitter
handle
‘@realdon-
aldtrump’ has continued to rise in lexical fame, even while
‘trump’ has gradually waned from the 2017 peak. Barely
apparent in 2014 with a relative median rate of 2, ‘@real-
donaldtrump’ reaches 627 in 2019, nearing the level of
‘trump’ at 768. Due to increases in mentions, retweets,
and replies, we suggest that changes in user norms and
modiﬁcations in Twitter’s platform mechanisms are two
possible aspects of what might explain such a shift in how
users reference Trump on Twitter.
Trump’s abrupt rise out of the lexical abyss is again on
display in Fig. 7. From a low peak relative median rate
of 20 in 2009 (relative to 1000 ‘trump’s in 2017), ‘trump’
fell to 4, 3, and 3 in 2012, 2013, and 2014, barely a blip.
If the Trump’s campaign goal was to Make America talk
about Donald Trump Again, then it has been a great
success.
Finally, while Trump’s lexical fame is clear, BTS
soundly beats all with relative median rates of ‘@bts twt’
reaching nearly 2,500 in 2018 and just below 2,000 in 2019
(in netspeak, ‘@bts twt’ >>> ‘trump’).
IV.
CONCLUDING REMARKS
We have explored in depth the daily lexical fame for
six major US political ﬁgures—Barack Obama, John
McCain, Mitt Romney, Hillary Clinton, and Donald
Trump—from 2008 to 2019 covering three presidential
elections. Because of the extraordinary being-talked-
about levels that US political ﬁgures have achieved, most
especially Trump, we have found that we needed to con-
ceive of lexical ultrafame, above ‘god’ fame. From a
branding and language point of view, our ﬁndings that
‘trump’ has been competing with function words over the
last few years should be shocking. As we suggested in the
main text, an advertising company promising that their
campaign will elevate a brand to the level of the word
‘say’ or ‘they’ (par medians for ‘trump’ and ‘@bts twt’
in the last few years)—and have days rising to compete
with the word ‘is’ and ‘to’—would, we would hope, strug-
gle to be taken seriously.
It should seem preposterous—even in the face of a glob-
al fan club, even with the possible use of bots and algo-
rithmic manipulation of Twitter—that any non-function
word could be ranked third on a single day, as famous as
the word ‘to’. But ‘@bts twt’ did just this on May 20 in
2018, even rising to be ranked ﬁrst within quarter hour
periods of the day. The collective text of Twitter and
similar kinds of social media is distinguished from that
of other kinds of corpora because of explicit referencing
and ampliﬁcation processes. For Twitter, these process-
es are automatically hyperlinked handles and retweets.
The retweet mechanism builds in social contagion and
is adjacent to renown (to name again) and reclaim (to
shout again).
We have focused on one major source in Twitter for
two major reasons, and which we can now better defend.
First, Twitter provides for a measurable reﬂection of
global events and trends, as our ready identiﬁcations of
many major events in lexical fame time series demon-
strates. Twitter is, however imperfectly, entrained with
aspects of the real world. Music and sport arguably
dominate—indeed they seem to form part of a resting
state of the Twitterverse—but politics and world events
are richly represented.
Second, with Twitter we have temporal resolution
available in principle at the level of a second, though
here the day scale has served as our ideal time scale for
a time frame lasting over a decade. In contrast to tra-
ditional polls, which we are in no way endeavoring to
replace but rather complement, we have a massive time
series database to draw on, which we consequently feel is
deserving of a focused analysis.
In terms of future work, we have examined in depth
only lexical fame at a daily resolution for a small set
of 1-grams; much more can be done. Detailed investiga-
tions of thoughtfully curated sets of competing 1-grams
will always be on oﬀer. Other clear directions to follow
would be analogous to those taken for search terms by,
for example, Google Trends (https://trends.google.com/
trends/?geo=US). Of course, care must always be taken
with large-scale temporal corpora which may suﬀer from
issues of misrepresentation (e.g., not including book sales
or retweets), uneven composition, cross-contamination,
and other problems [31, 61–63].
Considering 2-grams and 3-grams is also a natural next
step, though we caution that 2-grams and 3-grams will
not immediately solve issues of name disambiguation.
Famous individuals are referred to in a range of ways and
comparing 1-grams with, say, 2-grams is work that must
be done with care. Ideally, we would break language into
semantically intact phrases but we do not yet have a com-
monly agreed upon approach [64]. For the present work,
we have sought to overcome the limitations of 1-grams by
considering three essential ones for each individual: ﬁrst
name, last name, Twitter handle.
We have here taken the content of all tweets in our
database as being of equal weight. Separating out algo-
rithmically generated tweets would be of evident val-
ue [23, 65, 66], as would separating retweets from “fresh”
tweets, and dividing tweets up by language, and any com-
bination of these factorings.
We emphasize that daily ranks give lower bounds on
ranks for sub-day time scales. BTS’s handle ‘@bts twt’
was ranked 3rd on 2018/05/20 but may have, absurdly,
held the silver or even gold medal for some period of
time during that day. More generally, a full exploration
of time series at, say, minute, 15 minutes, or hour scales
for whatever topics of interest would generate another
level of fame dynamics resolution.
Finally, our work here is but one contribution to what
we believe is an emerging, post-disciplinary, data-driven
science of stories. Faithfully determining what was talked
about years after the fact is an enormously challenging
enterprise in itself, and the diﬃculty of such enables the


## Page 18


18
intentional creation and uncontrolled emergence of false
narratives. Here, we have been able to examine a elemen-
tary part of history by following raw Wildean fame—
albeit extruded though Twitter—and thereby quantify
how much and for how long events mattered. In the lexi-
cal fame time series of political ﬁgures, we have seen some
fundamental types of the shapes of history, the signatures
of sociotechnical time series: stasis, noise, spikes, cusps,
and shocks [67]. A data-driven categorization of the
shapes and motifs of the full ecology of rank time series
for Twitter would hold much promise for understanding
and possibly predicting sociotechnical time series, and in
the long run, stories.
V.
DATA AND METHODS
Our Twitter database comprises roughly 10% of all
tweets from spans 2008/09/09–2021/10/24. We separate
tweets into 1-grams by breaking at whitespace using a
regular expression. Certain edge cases may result in the
production of 1-grams from non-whitespace delimited
sequences; these cases are relatively rare and we did not
ﬁnd them to signiﬁcantly aﬀect the quality of our parsed
data.
We found we were obliged to ﬁlter out scriptio conintua
languages (languages that do not use spaces to delineate
words). we removed common characters from Japanese,
Thai, Chinese, and Korean.
After preliminary testing, we found Chinese and
Japanese characters to present the biggest challenges
in terms of the high number of unique, very long (>
100 characters) strings. We accomplished the removal of
these characters by running a regular expression to ﬁnd
characters in the unicode ranges for the most commonly
used Japanese and Chinese characters. Because charac-
ter ranges for Chinese, Japanese, and Korean (CJK) are
shared, we found it necessary to remove the whole CJK
range. The regular expression we used for this step was:
[\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF
\u4E00-\u9FCC\u4E00-\u9FFF\u3000-\u303F
\u3040-\u309F\u30A0-\u30FF\u0E00-\u0E7F]+
For this study, we also discarded emojis.
We then parse tweet bodies using a regular expression
designed to capture semantically meaningful 1-grams in
a principled manner, while limiting the artifacts of our
design choices in the resulting data set. Our regular
expression for breaking on whitespace was:
(https?:\/\/\w+\.\S+)|
([\w\@\#\’\’\&\]\*\-\/\[\=]+)
The expression breaks down into two groups. The ﬁrst
group of the regular expression is for capturing URLs.
This group captures http and https links with arbi-
trary characters after the domain name extension. The
results of the URL group capture retain case sensitivi-
ty since many links (especially those from link shorten-
ing services) are case sensitive. The second group cap-
tures words, hashtags, handles, and similar collections
of characters. Hyphenated words/phrases, contractions,
and expressions with slashes are allowed (thus, includ-
ing many common date formats as 1-grams). We do not
impose restrictions on the number of times allowed punc-
tuation can repeat (e.g. “state-of-the-art” will be consid-
ered a 1-gram). The results of the second group are all
converted to lowercase before counting their occurrence.
With 1-grams extracted, we converted all Latin letters
in 1-grams to lowercase. Finally we removed the 1-grams
‘rt’, ‘https’, ‘http’, ‘//t’, ‘-’, and ‘t’.
We take days as based on US Eastern Standard Time.
For each day, we construct Zipf distributions by ranking
1-grams in order of descending counts [36].
As we discuss in Sec. II B, because an entity may be
referred to in more than one way, and sometimes in many
ways, our simple measure of lexical fame aﬀords a low-
er bound. For example, during his two terms in oﬃce,
Obama would be indicated by ‘obama’, ‘@barackobama’,
‘#obama’, ‘potus’, or ‘#presidentobama’. Here, we take
the most common single word for each person or entity
of interest. Evidently, working with n-grams beyond indi-
vidual terms would allow for more complete measures of
fame, and would be necessary for names that are ambigu-
ous referents (e.g., ‘bush’).
For all ﬁgures, we used MATLAB Release R2019a.
ACKNOWLEDGMENTS
The authors appreciate comments from Ryan Gal-
lagher, Lewis Mitchell, and Aimee Picchi. The authors
are grateful for support from the Massachusetts Mutual
Life Insurance Company, and the computational facili-
ties provided by the Vermont Advanced Computing Core.
PSD and CMD were supported by NSF Grant No. IIS-
1447634.
[1] O. Wilde.
The Picture of Dorian Gray.
Lippincott’s
Monthly Magazine, 1890.
[2] M. J. Salganik, P. S. Dodds, and D. J. Watts. An exper-
imental study of inequality and unpredictability in an
artiﬁcial cultural market. Science, 311:854–856, 2006.
[3] M. J. Salganik and D. J. Watts. Leading the herd astray:
An experimental study of self-fulﬁlling prophecies in an
artiﬁcial cultural market.
Social Psychology Quarterl,
71:338–355, 2008.


## Page 19


19
[4] P.
S.
Dodds.
Homo
Narrativus
and
the
trou-
ble
with
fame.
Nautilus
Magazine,
2013.
http://nautil.us/issue/5/fame/homo-narrativus-and-
the-trouble-with-fame.
[5] J. A. Cookson, S. K. Moon, and J. Noh. Some people say:
Linguistic imprecision in corporate disclosures. Available
at SSRN 3152460, 2018.
[6] Weasel word. Wikipedia, 2019. https://en.wikipedia.org/
w/index.php?title=Weasel word&oldid=916478547.
[7] R. H. Coase. Payola in radio and television broadcasting.
The Journal of Law and Economics, 22(2):269–328, 1979.
[8] J. Greenberg. Trump lied to me about his wealth to get
onto the Forbes 400. Here are the tapes. Opinion Piece,
Washington Post, 2018.
[9] C. Borchers.
The amazing story of Donald Trump’s
old spokesman, john barron — who was actually Donald
Trump himself. Opinion Piece, Washington Post, 2016.
[10] Pseudonyms
of
Donald
Trump.
Wikipedia,
2019.
https://en.wikipedia.org/w/index.php?title=
Pseudonyms of Donald Trump&oldid=918247421;
Accessed on 2019/09/29.
[11] P. Murray. Monmouth university polling institute: Dems
prefer electability in 2020, 2019.
Question 25; Avail-
able
online
at
https://www.monmouth.edu/polling-
institute/reports/monmouthpoll us 020419/;
Accessed
on 2019/08/08.
[12] J. T. Woolley and G. Peters. The american presidency
project.
Santa Barbara, CA. Available online at http:
// www.presidency.ucsb.edu/ ; Accessed on 2019/09/15,
2008.
[13] S. Rosen. The economics of superstars. Am. Econ. Rev.,
71:845–858, 1981.
[14] M. Adler.
Stardom and talent.
American Economic
Review, pages 208–212, 1985.
[15] M. Balinski and R. Laraki. A theory of measuring, elect-
ing, and ranking. Proc. Natl. Acad. Sci., 104(21):8720–
8725, 2007.
[16] P. Laureti, L. Moret, and Y.-C. Zhang. Aggregating par-
tial, local evaluations to achieve global ranking. Physica
A, 345(3–4):705–712, 2004.
[17] I. D. Chase, C. Tovey, D. Spangler-Martin, and M. Man-
fredonia.
Individual diﬀerences versus social dynamics
in the formation of animal dominance hierarchies. Proc.
Natl. Acad. Sci., 99(8):5744–5749, 2002.
[18] BTS stands for Bangtan Sonyeondan (Korean: 방탄
소년단; Hanja: 防彈少年團), English: “Bulletproof Boy
Scouts”.
[19] A. Aisyah. Korean-English language translational action
of K-pop social media content: A case study on Bang-
tan Sonyeondan’s (BTS) oﬃcial Twitter. 3L: Language,
Linguistics, Literature®, 23, 2017.
[20] J. Dal Yong. An analysis of the Korean wave as transna-
tional popular culture: North American youth engage
through social media as TV becomes obsolete.
Inter-
national Journal of Communication, 12:404–422, 2018.
[21] C. S. Anderson. Global south korea and the k-pop phe-
nomenon. In Oxford Research Encyclopedia of Literature.
Oxford, 2018.
[22] BTS
(band):
Impact
and
inﬂuence.
Wikipedia,
2019.
https://en.wikipedia.org/w/index.php?title=
Identity Evropa&oldid=934670726#Activities; Accessed
on 2019/09/30.
[23] E. Ferrara, O. Varol, C. Davis, F. Menczer, and A. Flam-
mini. The rise of social bots. Commun. ACM, 59(7):96–
104, June 2016.
[24] H. A. Simon. On a class of skew distribution functions.
Biometrika, 42(3-4):425–440, 12 1955.
[25] D. D. S. Price. A general theory of bibliometric and other
cumulative advantage processes. Journal of the American
Society for Information Science, pages 292–306, 1976.
[26] P. S. Dodds, K. D. Harris, I. M. Kloumann, C. A. Bliss,
and C. M. Danforth. Temporal patterns of happiness and
information in a global social network: Hedonometrics
and Twitter. PLoS ONE, 6:e26752, 2011.
[27] H. Becker, M. Naaman, and L. Gravano. Beyond trend-
ing topics: Real-world event identiﬁcation on Twitter.
In Fifth international AAAI conference on weblogs and
social media, 2011.
[28] P. S. Dodds, J. R. Minot, M. V. Arnold, T. Alshaabi,
J.
L.
Adams,
A.
J.
Reagan,
and
C.
M.
Dan-
forth.
Computational
timeline
reconstruction
of
the
stories
surrounding
Trump:
Story
turbulence,
narrative control, and collective chronopathy, 2020.
https://arxiv.org/abs/2008.07301.
[29] E. M. Cody, A. J. Reagan, P. S. Dodds, and C. M. Dan-
forth. Public opinion polling with Twitter, 2016. Avail-
able online at https://arxiv.org/abs/1608.02024.
[30] T. Alshaabi, D. R. Dewhurst, J. R. Minot, M. V. Arnold,
J. L. Adams, C. M. Danforth, and P. S. Dodds.
The
growing ampliﬁcation of social media: Measuring tempo-
ral and social contagion dynamics for over 150 languages
on Twitter for 2009–2020. EPJ Data Science, 10:15, 2021.
[31] T. Alshaabi, J. L. Adams, M. V. Arnold, J. R. Minot,
D. R. Dewhurst, A. J. Reagan, C. M. Danforth, and
P. S. Dodds.
Storywrangler: A massive exploratorium
for sociolinguistic, cultural, socioeconomic, and political
timelines using Twitter. Science Advances, 7:eabe6534,
2021.
[32] Volfefe
index.
Wikipedia,
2019.
https://en.
wikipedia.org/w/index.php?title=Volfefe index&oldid=
917667858; Accessed on 2019/09/30.
[33] I. Clarke and J. Grieve. Stylistic variation on the Donald
Trump Twitter account: A linguistic analysis of tweets
posted between 2009 and 2018. PLOS ONE, 14:1–27, 09
2019.
[34] D.
ElBoghdady.
Market
quavers
after
fake
AP
tweet says Obama was hurt in White House explo-
sions.
Washington Post, 2013.
Available online at
https://www.washingtonpost.com/business/economy/
market-quavers-after-fake-ap-tweet-says-obama-was-
hurt-in-white-house-explosions/2013/04/23/d96d2dc6-
ac4d-11e2-a8b9-2a63d75b5459 story.html; Accessed on
2019/09/30.
[35] S. Levin.
‘we’re watching a company explode’: is
Snapchat becoming irrelevant?
The Guardian, 2018.
Available
online
at
https://www.theguardian.com/
technology/2018/feb/23/snapchat-redesign-scandal-
kylie-jenner-what-went-wrong; Accessed on 2019/09/30.
[36] G. K. Zipf. Human Behaviour and the Principle of Least-
Eﬀort. Addison-Wesley, Cambridge, MA, 1949.
[37] H. A. Takiﬀ, D. T. Sanchez, and T. L. Stewart. What’s
in a name? The status implications of students’ terms
of address for male and female professors. Psychology of
Women Quarterly, 25(2):134–144, 2001.
[38] J. A. Files, A. P. Mayer, M. G. Ko, P. Friedrich, M. Jenk-
ins, M. J. Bryan, S. Vegunta, C. M. Wittich, M. A. Lyle,
R. Melikian, et al.
Speaker introductions at internal
medicine grand rounds: Forms of address reveal gender


## Page 20


20
bias. Journal of Women’s Health, 26(5):413–419, 2017.
[39] J. E. Uscinski and L. J. Goren. What’s in a name? Cover-
age of senator Hillary Clinton during the 2008 democrat-
ic primary. Political Research Quarterly, 64(4):884–896,
2011.
[40] 2018. Discussion with S. V. Scarpino, Quebec City, QC,
Canada.
[41] E. A. Pechenick, C. M. Danforth, and P. S. Dodds. Is lan-
guage evolution grinding to a halt? The scaling of lexical
turbulence in English ﬁction suggests it is not. Journal
of Computational Science, 21:24–37, 2017.
[42] Read transcript of former President Obama’s speech,
blasting President Trump.
USA Today, 2018/09/07.
Available
online
at
https://www.usatoday.com/
story/news/politics/elections/2018/09/07/president-
barack-obamas-speech-transcript-slamming-trump/
1225554002/.
[43] Obama
says
White
House
response
to
coro-
navirus
has
been
’absolute
chaotic
disaster’.
USA
Today,
2018/09/07.
Available
online
at
https://www.cnn.com/2020/05/09/politics/obama-
trump-coronavirus-response-ﬂynn-case/index.html.
[44] J.
Martin
and
A.
Rappeport.
Donald
Trump
says
John
McCain
is
no
war
hero,
setting
oﬀ
another storm.
New York Times, 2015.
Avail-
able online at https://www.nytimes.com/2015/07/19/
us/politics/trump-belittles-mccains-war-record.html.
[45] M. Haberman, A. Karni, and M. Tackett.
Months
after John McCain’s death, Trump keeps feud with
him alive.
New York Times, 2019.
Available online
at
https://www.nytimes.com/2019/03/20/us/politics/
trump-john-mccain.html; Accessed on 2019/09/15.
[46] J. Goldberg.
Trump: Americans who died in war are
‘losers’ and ‘suckers’, 2020/09/03.
Available online at
https://www.theatlantic.com/politics/archive/2020/
09/trump-americans-who-died-at-war-are-losers-and-
suckers/615997/.
[47] M.
Romney.
Wikipedia,
2016.
Accessed
on
2019/09/10;
https://en.wikipedia.org/w/index.php?
title=Mitt Romney%27s 2016 anti-Trump speech&
oldid=910068210.
[48] M. Romney.
Mitt Romney: The President shapes the
public character of the nation. Trump’s character falls
short. Opinion Piece, Washington Post, 2019. January
1;
https://www.washingtonpost.com/opinions/mitt-
romney-the-president-shapes-the-public-character-of-
the-nation-trumps-character-falls-short/2019/01/01/
37a3c8c2-0d1a-11e9-8938-5898adc28fa2 story.html.
[49] J. Greenberg. It’s true: Donald Trump once supported
impeaching George W. Bush. Politifact, 2016. Available
online
at
https://www.politifact.com/truth-o-meter/
statements/2016/feb/16/our-principles-pac/anti-trump-
ad-says-he-backed-impeaching-bush/;
Accessed
on
2019/09/15.
[50] K. Q. Seelye. Miss California USA will keep her title. New
York Times, 2009.
Available at https://www.nytimes.
com/2009/05/13/us/13beauty.html.
[51] J. McKinley. Donald trump ﬁres miss california. New
York Times, 2009.
Available at https://www.nytimes.
com/2009/06/11/us/11pageant.html.
[52] C.
Cliﬀord.
Trump
casino
group
in
bankrupt-
cy.
CNN,
2009.
Available
online
at:
https:
//money.cnn.com/2009/02/17/news/companies/
trump entertainment/index.htm;
Accessed
on
2019/09/15.
[53] Barack
Obama
citizenship
conspiracy
theories.
Wikipedia,
2019.
https://en.wikipedia.org/w/index.
php?title=Barack Obama citizenship conspiracy
theories&oldid=915849426.
[54] J. Dawsey.
Trump derides protections for immigrants
from ‘shithole’ countries.
Washington Post, 2018.
Available online at https://www.washingtonpost.com/
politics/trump-attacks-protections-for-immigrants-
from-shithole-countries-in-oval-oﬃce-meeting/2018/01/
11/bfc0725c-f711-11e7-91af-31ac729add94 story.html;
Accessed on 2019/09/15.
[55] W. Ryoo.
Globalization, or the logic of cultural
hybridization: The case of the Korean wave. Asian Jour-
nal of Communication, 19:137–151, 2009.
[56] D. Jin. New Korean Wave: Transnational cultural power
in the age of social media. University of Illinois press,
2016.
[57] BTS.
Wikipedia, 2019.
Available online at https:
//en.wikipedia.org/w/index.php?title=BTS (band)
&oldid=915205302; Accessed on 2019/09/11.
[58] T. Highﬁeld, S. Harrington, and A. Bruns. Twitter as a
technology for audiencing and fandom: The #eurovision
phenomenon.
Information, Communication & Society,
16(3):315–339, 2013.
[59] K. Yoon.
Transnational fandom in the making: K-
pop fans in Vancouver.
International Communication
Gazette, 81(2):176–192, 2019.
[60] C. E. Shannon.
A mathematical theory of communi-
cation. The Bell System Tech. J., 27:379–423,623–656,
1948.
[61] J.-B. Michel, Y. K. Shen, A. P. Aiden, A. Veres, M. K.
Gray, The Google Books Team, J. P. Pickett, D. Hoiberg,
D. Clancy, P. Norvig, J. Orwant, S. Pinker, M. A. Nowak,
and E. A. Lieberman. Quantitative analysis of culture
using millions of digitized books.
Science Magazine,
331:176–182, 2011.
[62] D. Lazer, R. Kennedy, G. King, and A. Vespignani. The
parable of Google Flu: Traps in Big Data analysis. Sci-
ence, 343:1203–1205, 2014.
[63] E. A. Pechenick, C. M. Danforth, and P. S. Dodds. Char-
acterizing the google books corpus: Strong limits to infer-
ences of socio-cultural and linguistic evolution.
PLoS
ONE, 10:e0137041, 2015.
[64] J. R. Williams, P. R. Lessard, S. Desu, E. M. Clark, J. P.
Bagrow, C. M. Danforth, and P. S. Dodds. Zipf’s law
holds for phrases, not words. Nature Scientiﬁc Reports,
5:12209, 2015.
[65] E. M. Clark, C. A. Jones, J. R. Williams, A. N. Kur-
ti, M. C. Norotsky, C. M. Danforth, and P. S. Dodds.
Vaporous marketing: Uncovering pervasive electronic
cigarette advertisements on Twitter. Available online at
http://arxiv.org/abs/1508.01843, 2015.
[66] C. A. Davis, O. Varol, E. Ferrara, A. Flammini, and
F. Menczer. Botornot: A system to evaluate social bots.
In Proceedings of the 25th International Conference Com-
panion on World Wide Web, pages 273–274. Internation-
al World Wide Web Conferences Steering Committee,
2016.
[67] D. R. Dewhurst, T. Alshaabi, D. Kiley, M. V. Arnold,
J. R. Minot, C. M. Danforth, and P. S. Dodds.
The
shocklet transform: A decomposition method for the
identiﬁcation of local, mechanism-driven dynamics in
sociotechnical time series, 2019.
Available online at


## Page 21


21
https://arxiv.org/abs/1906.11710.


## Page 22


22
Appendix A: Time series
-50  0
100
200
300
400
500
600
700
800
900
1000
1100
1200
1300
1400
1500
1600
1700
1800
1
1000
2000
3000
4000
5000
FIG. A1. The same set of time series shown in Fig. 3 rendered in wide format. While overall comparisons between time series
may be more diﬃcult, the detailed history presented by each time series may be more easily examined. Tabs. A2–A9 list the
top 10 and bottom 5 dates for each 1-gram in each year along with year-scale medians ranks.


## Page 23


23
Appendix B: Extreme dates
The following pages present tables showing the top 10 and
bottom 5 dates for the ranks of the main 1-grams, ﬁrst for
overall period of study 2008/09/09 through to 2021/10/24
in Tab. A1, and then at the year scale for each 1-gram in
Tabs. A2–A8.
‘obama’
‘mccain’
‘romney’
1. 2008/11/04: 14
1. 2008/09/26: 31
1. 2012/11/06: 33
2. 2008/11/05: 15
2. 2008/10/07: 40
2. 2012/10/03: 63
3. 2012/11/06: 20
3. 2008/10/15: 46
3. 2012/10/16: 63
4. 2009/01/20: 24
4. 2008/11/04: 54
4. 2012/10/22: 104
5. 2008/09/26: 44
5. 2008/09/27: 74
5. 2012/11/07: 170
6. 2008/11/03: 44
6. 2008/10/16: 84
6. 2012/11/05: 250
7. 2012/11/07: 52
7. 2008/10/08: 94
7. 2020/02/05: 288
8. 2008/10/07: 55
8. 2008/11/02: 94
8. 2012/10/04: 328
9. 2008/11/01: 55
9. 2008/09/24: 99
9. 2012/10/17: 389
10. 2008/11/02: 57
10. 2008/11/03: 106
10. 2019/01/02: 457
· · ·
· · ·
· · ·
4770. 2021/10/09: 18,735
4770. 2021/07/10: 241,159
4760. 2010/08/08: 449,099
4771. 2021/07/24: 18,823
4771. 2021/04/18: 243,851
4761. 2010/11/26: 451,241
4772. 2021/10/02: 19,236
4772. 2021/10/13: 244,127
4762. 2010/09/03: 464,323
4773. 2021/07/31: 20,020
4773. 2013/12/25: 250,740
4763. 2010/08/11: 540,384
4774. 2021/05/14: 20,104
4774. 2021/03/21: 283,921
4764. 2010/08/15: 813,435
‘hillary’
‘trump’
‘biden’
‘@bts twt’
1. 2016/11/08: 50
1. 2016/11/09: 11
1. 2020/11/07: 24
1. 2018/05/20: 3
2. 2016/11/09: 77
2. 2016/11/08: 15
2. 2020/11/04: 36
2. 2018/05/15: 4
3. 2016/09/26: 89
3. 2016/11/10: 19
3. 2020/09/29: 52
3. 2018/05/14: 6
4. 2016/10/09: 91
4. 2020/11/04: 21
4. 2020/11/06: 54
4. 2018/05/16: 8
5. 2016/10/19: 110
5. 2016/10/09: 22
5. 2020/10/22: 57
5. 2018/05/18: 8
6. 2016/09/27: 127
6. 2020/11/07: 26
6. 2020/09/30: 59
6. 2017/05/21: 9
7. 2016/11/07: 130
7. 2016/09/26: 27
7. 2020/11/05: 59
7. 2021/05/23: 10
8. 2016/10/20: 132
8. 2020/11/05: 27
8. 2021/01/20: 59
8. 2017/05/01: 11
9. 2016/10/10: 138
9. 2021/01/06: 27
9. 2020/11/03: 69
9. 2018/05/17: 11
10. 2016/11/10: 157
10. 2020/09/29: 28
10. 2020/11/08: 69
10. 2018/05/19: 11
· · ·
· · ·
· · ·
· · ·
4770. 2011/10/09: 64,733
4770. 2014/08/23: 76,435
4770. 2012/12/25: 223,911
3178. 2013/04/27: 882,731
4771. 2013/03/02: 64,804
4771. 2014/07/27: 77,186
4771. 2011/09/25: 224,846
3179. 2013/01/20: 882,966
4772. 2013/12/25: 66,346
4772. 2013/11/17: 78,219
4772. 2012/04/08: 246,425
3180. 2013/02/10: 929,849
4773. 2012/12/24: 67,635
4773. 2013/11/16: 79,322
4773. 2012/12/15: 263,322
3181. 2013/01/09: 952,557
4774. 2012/12/25: 71,445
4774. 2013/10/26: 81,022
4774. 2011/11/24: 274,352
3182. 2013/02/25: 986,266
TABLE A1. Overall top 10 and bottom 5 rank days for the main 1-grams we track. Time range covered: 2008/09/09
through to 2021/10/24.


## Page 24


24
‘obama’: 2008
‘obama’: 2009
‘obama’: 2010
‘obama’: 2011
‘obama’: 2012
median rank = 278
median rank = 636
median rank = 1,462
median rank = 2,316
median rank = 2,029
∼‘into’
∼‘army’
∼‘uk’
∼‘russia’
∼‘korea’
1. 2008/11/04: 14
1. 2009/01/20: 24
1. 2010/11/09: 101
1. 2011/05/02: 148
1. 2012/11/06: 20
2. 2008/11/05: 15
2. 2009/01/21: 57
2. 2010/01/27: 256
2. 2011/05/01: 179
2. 2012/11/07: 52
3. 2008/09/26: 44
3. 2009/10/09: 76
3. 2010/01/28: 417
3. 2011/01/25: 376
3. 2012/10/03: 66
4. 2008/11/03: 44
4. 2009/01/22: 98
4. 2010/03/22: 439
4. 2011/03/19: 528
4. 2012/10/16: 66
5. 2008/10/07: 55
5. 2009/01/19: 105
5. 2010/11/08: 455
5. 2011/03/20: 608
5. 2012/10/22: 115
6. 2008/11/01: 55
6. 2009/01/18: 137
6. 2010/11/10: 484
6. 2011/04/27: 671
6. 2012/09/06: 167
7. 2008/11/02: 57
7. 2009/01/23: 142
7. 2010/03/23: 516
7. 2011/05/04: 684
7. 2012/11/05: 176
8. 2008/11/06: 58
8. 2009/01/17: 155
8. 2010/01/29: 543
8. 2011/03/21: 691
8. 2012/01/24: 285
9. 2008/10/15: 61
9. 2009/02/24: 155
9. 2010/03/21: 585
9. 2011/05/03: 714
9. 2012/09/04: 334
10. 2008/10/29: 64
10. 2009/01/24: 172
10. 2010/11/03: 585
10. 2011/09/08: 746
10. 2012/10/04: 356
· · ·
· · ·
· · ·
· · ·
· · ·
110. 2008/12/29: 673
343. 2009/12/27: 1,391
361. 2010/12/26: 3,191
361. 2011/11/25: 4,626
362. 2012/02/12: 3,853
111. 2008/11/29: 705
344. 2009/11/22: 1,394
362. 2010/12/24: 3,204
362. 2011/12/24: 4,777
363. 2012/12/23: 4,132
112. 2008/12/31: 721
345. 2009/11/29: 1,442
363. 2010/10/03: 3,347
363. 2011/11/27: 4,802
364. 2012/04/08: 4,643
113. 2008/11/28: 767
346. 2009/12/26: 1,508
364. 2010/12/25: 3,580
364. 2011/12/26: 5,132
365. 2012/12/24: 4,694
114. 2008/12/25: 800
347. 2009/12/25: 1,538
365. 2010/12/31: 4,085
365. 2011/12/25: 5,970
366. 2012/12/25: 5,254
‘obama’: 2013
‘obama’: 2014
‘obama’: 2015
‘obama’: 2016
‘obama’: 2017
median rank = 2,467
median rank = 2,182
median rank = 1,862
median rank = 1,237
median rank = 1,195
∼‘france’
∼‘china’
∼‘japan’
∼‘america’
∼‘america’
1. 2013/01/21: 262
1. 2014/01/28: 484
1. 2015/01/20: 297
1. 2016/11/09: 90
1. 2017/01/20: 95
2. 2013/12/10: 511
2. 2014/11/20: 574
2. 2015/06/26: 320
2. 2016/11/10: 136
2. 2017/01/10: 143
3. 2013/02/12: 572
3. 2014/11/24: 621
3. 2015/04/11: 473
3. 2016/11/08: 155
3. 2017/01/11: 148
4. 2013/08/31: 678
4. 2014/12/17: 622
4. 2015/11/16: 558
4. 2016/11/11: 161
4. 2017/03/04: 153
5. 2013/10/01: 741
5. 2014/11/21: 682
5. 2015/01/21: 631
5. 2016/11/12: 260
5. 2017/03/05: 220
6. 2013/09/10: 769
6. 2014/11/05: 738
6. 2015/12/06: 722
6. 2016/11/13: 272
6. 2017/01/21: 230
7. 2013/01/16: 971
7. 2014/09/10: 752
7. 2015/11/13: 746
7. 2016/01/12: 276
7. 2017/01/12: 236
8. 2013/04/15: 993
8. 2014/12/19: 837
8. 2015/11/18: 798
8. 2016/03/23: 282
8. 2017/01/19: 257
9. 2013/01/22: 1,101
9. 2014/08/14: 907
9. 2015/01/25: 852
9. 2016/11/14: 325
9. 2017/01/17: 314
10. 2013/09/04: 1,156
10. 2014/09/11: 963
10. 2015/01/27: 872
10. 2016/07/27: 343
10. 2017/01/18: 363
· · ·
· · ·
· · ·
· · ·
· · ·
361. 2013/04/13: 4,475
361. 2014/04/20: 3,971
361. 2015/05/02: 3,834
362. 2016/02/29: 2,593
361. 2017/11/10: 2,502
362. 2013/06/02: 4,475
362. 2014/04/05: 4,041
362. 2015/05/07: 3,911
363. 2016/02/28: 2,613
362. 2017/05/14: 2,557
363. 2013/03/31: 4,595
363. 2014/11/28: 4,042
363. 2015/01/03: 4,076
364. 2016/04/08: 2,619
363. 2017/04/16: 2,573
364. 2013/12/25: 4,673
364. 2014/12/14: 4,051
364. 2015/05/03: 4,243
365. 2016/04/17: 2,867
364. 2017/09/11: 3,003
365. 2013/04/14: 5,086
365. 2014/01/01: 4,340
365. 2015/01/01: 4,318
366. 2016/04/09: 2,983
365. 2017/09/10: 3,285
‘obama’: 2018
‘obama’: 2019
‘obama’: 2020
‘obama’: 2021
median rank = 1,488
median rank = 1,790
median rank = 1,856
median rank = 9,896
∼‘uk’
∼‘india’
∼‘japan’
∼‘spain’
1. 2018/09/07: 237
1. 2019/08/06: 685
1. 2020/05/11: 284
1. 2021/01/20: 484
2. 2018/09/08: 263
2. 2019/02/19: 815
2. 2020/08/20: 350
2. 2021/01/21: 1,497
3. 2018/09/09: 381
3. 2019/10/27: 826
3. 2020/08/18: 371
3. 2021/01/17: 1,879
4. 2018/07/17: 448
4. 2019/03/26: 843
4. 2020/05/12: 389
4. 2021/08/08: 1,881
5. 2018/09/10: 483
5. 2019/02/18: 902
5. 2020/05/13: 394
5. 2021/01/07: 1,905
6. 2018/10/24: 485
6. 2019/08/05: 902
6. 2020/05/10: 395
6. 2021/01/22: 2,030
7. 2018/02/07: 543
7. 2019/10/30: 920
7. 2020/05/16: 419
7. 2021/01/06: 2,096
8. 2018/09/01: 570
8. 2019/10/25: 944
8. 2020/05/17: 429
8. 2021/01/18: 2,310
9. 2018/07/18: 572
9. 2019/04/26: 971
9. 2020/05/14: 453
9. 2021/01/09: 2,326
10. 2018/07/14: 573
10. 2019/11/16: 994
10. 2020/07/30: 467
10. 2021/01/08: 2,398
· · ·
· · ·
· · ·
· · ·
361. 2018/02/26: 3,221
361. 2019/12/01: 3,729
362. 2020/03/30: 4,545
291. 2021/10/09: 18,735
362. 2018/09/29: 3,423
362. 2019/02/06: 3,818
363. 2020/12/09: 4,545
292. 2021/07/24: 18,823
363. 2018/09/23: 3,471
363. 2019/11/30: 3,845
364. 2020/12/22: 4,707
293. 2021/10/02: 19,236
364. 2018/09/27: 3,595
364. 2019/03/03: 3,928
365. 2020/03/19: 4,744
294. 2021/07/31: 20,020
365. 2018/09/28: 3,981
365. 2019/01/31: 4,092
366. 2020/03/20: 5,222
295. 2021/05/14: 20,104
TABLE A2. Median rank and overall top 10 and bottom 5 rank days for each calendar year for ‘obama’. Time
range covered: 2008/09/09 through to 2021/10/24.


## Page 25


25
‘mccain’: 2008
‘mccain’: 2009
‘mccain’: 2010
‘mccain’: 2011
‘mccain’: 2012
median rank = 436
median rank = 12,132
median rank = 27,543
median rank = 57,529
median rank = 60,220
∼‘birthday’
∼‘singapore’
∼‘netherlands’
∼‘nepal’
∼‘libya’
1. 2008/09/26: 31
1. 2009/01/20: 2,219
1. 2010/02/25: 2,844
1. 2011/04/22: 5,475
1. 2012/11/14: 6,259
2. 2008/10/07: 40
2. 2009/03/09: 2,308
2. 2010/03/26: 4,335
2. 2011/01/25: 7,719
2. 2012/11/15: 6,426
3. 2008/10/15: 46
3. 2009/03/16: 2,676
3. 2010/01/21: 4,431
3. 2011/07/30: 11,911
3. 2012/01/04: 8,612
4. 2008/11/04: 54
4. 2009/02/24: 2,677
4. 2010/12/18: 5,021
4. 2011/07/28: 12,222
4. 2012/11/06: 9,202
5. 2008/09/27: 74
5. 2009/01/19: 2,774
5. 2010/08/25: 5,719
5. 2011/05/12: 12,533
5. 2012/01/24: 9,270
6. 2008/10/16: 84
6. 2009/03/17: 3,368
6. 2010/01/20: 6,022
6. 2011/09/19: 13,909
6. 2012/08/29: 9,352
7. 2008/10/08: 94
7. 2009/09/09: 3,510
7. 2010/01/27: 7,261
7. 2011/06/21: 15,102
7. 2012/03/05: 12,163
8. 2008/11/02: 94
8. 2009/03/03: 4,026
8. 2010/02/15: 7,263
8. 2011/01/08: 15,669
8. 2012/11/07: 12,427
9. 2008/09/24: 99
9. 2009/01/23: 4,069
9. 2010/01/23: 7,712
9. 2011/07/27: 16,520
9. 2012/11/16: 12,655
10. 2008/11/03: 106
10. 2009/08/25: 4,204
10. 2010/03/22: 7,763
10. 2011/05/14: 16,907
10. 2012/11/27: 13,511
· · ·
· · ·
· · ·
· · ·
· · ·
110. 2008/11/28: 11,208
343. 2009/12/31: 32,733
361. 2010/12/29: 74,177
361. 2011/09/05: 109,745
362. 2012/05/13: 142,257
111. 2008/12/17: 11,604
344. 2009/12/29: 33,107
362. 2010/12/30: 77,260
362. 2011/07/23: 111,659
363. 2012/07/01: 145,447
112. 2008/12/24: 11,895
345. 2009/10/07: 38,820
363. 2010/11/26: 78,685
363. 2011/07/24: 112,608
364. 2012/12/23: 148,507
113. 2008/12/23: 12,083
346. 2009/11/27: 38,847
364. 2010/10/24: 79,385
364. 2011/10/08: 118,100
365. 2012/12/24: 167,073
114. 2008/12/25: 16,193
347. 2009/12/25: 59,496
365. 2010/12/26: 82,727
365. 2011/12/25: 133,236
366. 2012/12/25: 220,687
‘mccain’: 2013
‘mccain’: 2014
‘mccain’: 2015
‘mccain’: 2016
‘mccain’: 2017
median rank = 68,106
median rank = 82,135
median rank = 83,352
median rank = 48,429
median rank = 12,100
∼‘lebanon’
∼‘tanzania’
∼‘bahamas’
∼‘maldives’
∼‘singapore’
1. 2013/09/03: 6,075
1. 2014/09/10: 12,988
1. 2015/07/18: 2,557
1. 2016/10/08: 2,383
1. 2017/07/28: 252
2. 2013/03/07: 6,247
2. 2014/06/13: 15,370
2. 2015/07/20: 2,702
2. 2016/06/16: 3,491
2. 2017/07/25: 386
3. 2013/09/04: 6,361
3. 2014/09/11: 16,018
3. 2015/07/19: 2,722
3. 2016/08/01: 4,304
3. 2017/07/20: 609
4. 2013/03/08: 9,548
4. 2014/08/12: 18,260
4. 2015/07/21: 6,959
4. 2016/12/12: 4,431
4. 2017/07/19: 677
5. 2013/09/25: 10,319
5. 2014/01/10: 18,870
5. 2015/10/12: 12,697
5. 2016/08/02: 4,611
5. 2017/09/22: 699
6. 2013/09/06: 12,454
6. 2014/12/09: 22,078
6. 2015/07/22: 15,497
6. 2016/12/11: 5,138
6. 2017/06/08: 715
7. 2013/09/02: 13,242
7. 2014/06/14: 24,667
7. 2015/01/29: 16,241
7. 2016/05/03: 5,541
7. 2017/07/26: 1,057
8. 2013/01/31: 13,297
8. 2014/03/03: 25,663
8. 2015/10/13: 17,308
8. 2016/10/11: 5,998
8. 2017/10/17: 1,102
9. 2013/09/19: 13,541
9. 2014/07/17: 26,036
9. 2015/07/25: 19,278
9. 2016/10/09: 6,712
9. 2017/09/23: 1,224
10. 2013/05/27: 13,801
10. 2014/02/18: 26,102
10. 2015/07/23: 21,117
10. 2016/12/31: 7,374
10. 2017/07/29: 1,269
· · ·
· · ·
· · ·
· · ·
· · ·
361. 2013/11/28: 204,083
361. 2014/12/26: 188,132
361. 2015/05/03: 176,827
362. 2016/04/24: 124,361
361. 2017/04/28: 58,729
362. 2013/11/30: 208,817
362. 2014/05/24: 192,300
362. 2015/12/25: 187,901
363. 2016/01/02: 124,848
362. 2017/04/22: 61,945
363. 2013/12/08: 209,145
363. 2014/12/24: 197,104
363. 2015/05/17: 209,434
364. 2016/04/16: 125,016
363. 2017/07/08: 68,297
364. 2013/12/26: 212,893
364. 2014/04/20: 235,769
364. 2015/03/07: 209,811
365. 2016/10/02: 126,921
364. 2017/05/07: 88,681
365. 2013/12/25: 250,740
365. 2014/05/25: 240,792
365. 2015/06/07: 222,288
366. 2016/04/17: 133,408
365. 2017/04/29: 102,715
‘mccain’: 2018
‘mccain’: 2019
‘mccain’: 2020
‘mccain’: 2021
median rank = 22,991
median rank = 33,799
median rank = 45,639
median rank = 71,511
∼‘egypt’
∼‘honduras’
∼‘kuwait’
∼‘rwanda’
1. 2018/08/26: 128
1. 2019/03/20: 603
1. 2020/09/04: 955
1. 2021/02/22: 4,753
2. 2018/08/25: 190
2. 2019/03/21: 698
2. 2020/09/23: 2,146
2. 2021/01/24: 7,046
3. 2018/08/27: 227
3. 2019/03/17: 871
3. 2020/09/05: 2,344
3. 2021/01/03: 7,058
4. 2018/09/01: 258
4. 2019/05/30: 1,122
4. 2020/09/22: 3,079
4. 2021/03/24: 7,928
5. 2018/09/02: 483
5. 2019/03/19: 1,699
5. 2020/09/03: 3,233
5. 2021/07/01: 8,343
6. 2018/08/28: 703
6. 2019/03/22: 1,711
6. 2020/08/18: 3,572
6. 2021/01/09: 9,620
7. 2018/05/11: 946
7. 2019/03/18: 1,816
7. 2020/11/06: 3,948
7. 2021/02/23: 9,622
8. 2018/09/03: 1,097
8. 2019/12/26: 2,003
8. 2020/11/04: 3,982
8. 2021/10/19: 10,036
9. 2018/08/31: 1,105
9. 2019/12/27: 2,231
9. 2020/07/30: 4,352
9. 2021/02/01: 10,370
10. 2018/08/24: 1,118
10. 2019/07/18: 2,569
10. 2020/09/06: 4,743
10. 2021/08/25: 11,755
· · ·
· · ·
· · ·
· · ·
361. 2018/12/08: 97,532
361. 2019/11/28: 120,034
362. 2020/04/04: 139,705
291. 2021/09/19: 234,194
362. 2018/11/24: 97,581
362. 2019/09/01: 131,454
363. 2020/03/19: 144,217
292. 2021/07/10: 241,159
363. 2018/10/14: 103,733
363. 2019/11/30: 135,694
364. 2020/03/21: 148,593
293. 2021/04/18: 243,851
364. 2018/01/26: 105,016
364. 2019/09/02: 141,429
365. 2020/03/27: 161,513
294. 2021/10/13: 244,127
365. 2018/11/25: 109,784
365. 2019/02/03: 151,097
366. 2020/04/05: 162,264
295. 2021/03/21: 283,921
TABLE A3. Median rank and overall top 10 and bottom 5 rank days for each calendar year for ‘mccain’. Time
range covered: 2008/09/09 through to 2021/10/24.


## Page 26


26
‘romney’: 2008
‘romney’: 2009
‘romney’: 2010
‘romney’: 2011
‘romney’: 2012
median rank = 31,576
median rank = 55,925
median rank = 100,056
median rank = 27,898
median rank = 4,333
∼‘ukraine’
∼‘sudan’
∼‘cameroon’
∼‘poland’
∼‘colombia’
1. 2008/11/19: 3,575
1. 2009/02/28: 5,911
1. 2010/02/19: 8,488
1. 2011/10/11: 2,628
1. 2012/11/06: 33
2. 2008/11/20: 8,512
2. 2009/03/01: 8,691
2. 2010/02/18: 9,627
2. 2011/10/18: 2,817
2. 2012/10/03: 63
3. 2008/10/15: 8,557
3. 2009/02/06: 10,400
3. 2010/04/10: 10,361
3. 2011/12/15: 3,228
3. 2012/10/16: 63
4. 2008/09/29: 10,771
4. 2009/02/27: 11,300
4. 2010/02/20: 11,730
4. 2011/06/02: 3,857
4. 2012/10/22: 104
5. 2008/11/03: 10,931
5. 2009/07/20: 12,086
5. 2010/02/16: 13,215
5. 2011/08/11: 3,941
5. 2012/11/07: 170
6. 2008/11/01: 11,283
6. 2009/07/03: 12,430
6. 2010/03/03: 14,000
6. 2011/09/22: 3,957
6. 2012/11/05: 250
7. 2008/09/15: 11,535
7. 2009/09/19: 12,884
7. 2010/01/19: 15,319
7. 2011/12/10: 4,085
7. 2012/10/04: 328
8. 2008/12/08: 11,817
8. 2009/06/14: 13,042
8. 2010/04/11: 15,550
8. 2011/09/12: 4,203
8. 2012/10/17: 389
9. 2008/12/14: 13,154
9. 2009/06/01: 14,343
9. 2010/03/02: 15,638
9. 2011/11/22: 4,704
9. 2012/10/23: 540
10. 2008/09/09: 14,239
10. 2009/08/20: 15,042
10. 2010/02/23: 16,092
10. 2011/06/13: 4,750
10. 2012/11/04: 587
· · ·
· · ·
· · ·
· · ·
· · ·
109. 2008/12/02: 237,233
335. 2009/10/25: 248,997
360. 2010/08/08: 449,099
361. 2011/02/20: 164,043
362. 2012/12/29: 29,452
110. 2008/12/30: 289,261
336. 2009/01/06: 272,074
361. 2010/11/26: 451,241
362. 2011/01/15: 171,409
363. 2012/12/28: 29,474
111. 2008/09/20: 300,879
337. 2009/03/08: 279,411
362. 2010/09/03: 464,323
363. 2011/01/08: 183,393
364. 2012/12/22: 29,868
112. 2008/09/10: 317,501
338. 2009/12/09: 287,444
363. 2010/08/11: 540,384
364. 2011/01/18: 183,978
365. 2012/12/15: 32,601
113. 2008/09/19: 331,363
339. 2009/12/22: 301,241
364. 2010/08/15: 813,435
365. 2011/01/01: 228,408
366. 2012/12/25: 35,184
‘romney’: 2013
‘romney’: 2014
‘romney’: 2015
‘romney’: 2016
‘romney’: 2017
median rank = 59,848
median rank = 81,318
median rank = 84,400
median rank = 36,875
median rank = 109,926
∼‘libya’
∼‘tanzania’
∼‘bahamas’
∼‘bangladesh’
∼‘cambodia’
1. 2013/01/21: 4,594
1. 2014/01/05: 18,801
1. 2015/01/30: 2,789
1. 2016/03/03: 460
1. 2017/08/18: 3,572
2. 2013/03/03: 9,049
2. 2014/01/25: 22,539
2. 2015/01/09: 9,052
2. 2016/03/04: 2,155
2. 2017/08/16: 5,431
3. 2013/02/03: 12,687
3. 2014/10/14: 23,710
3. 2015/05/16: 9,571
3. 2016/11/25: 2,296
3. 2017/12/06: 6,058
4. 2013/03/04: 13,646
4. 2014/03/03: 24,007
4. 2015/06/20: 9,675
4. 2016/11/08: 2,302
4. 2017/11/10: 6,373
5. 2013/03/15: 14,344
5. 2014/06/15: 24,555
5. 2015/01/13: 10,657
5. 2016/11/23: 2,549
5. 2017/12/05: 6,686
6. 2013/02/12: 15,865
6. 2014/09/07: 25,752
6. 2015/05/15: 11,431
6. 2016/11/30: 2,735
6. 2017/08/19: 8,083
7. 2013/03/13: 18,537
7. 2014/05/09: 27,123
7. 2015/01/17: 12,105
7. 2016/11/09: 3,221
7. 2017/12/04: 8,663
8. 2013/12/31: 19,357
8. 2014/01/24: 27,728
8. 2015/01/14: 13,445
8. 2016/11/24: 3,291
8. 2017/08/17: 9,728
9. 2013/11/03: 19,607
9. 2014/03/18: 28,216
9. 2015/01/31: 14,881
9. 2016/03/02: 3,381
9. 2017/11/11: 14,285
10. 2013/01/01: 20,268
10. 2014/06/12: 28,294
10. 2015/01/16: 15,326
10. 2016/11/27: 3,487
10. 2017/09/11: 18,114
· · ·
· · ·
· · ·
· · ·
· · ·
361. 2013/11/28: 120,308
361. 2014/09/20: 163,954
361. 2015/03/08: 179,715
362. 2016/12/24: 138,293
361. 2017/05/21: 253,351
362. 2013/12/22: 122,178
362. 2014/05/25: 166,930
362. 2015/05/02: 183,777
363. 2016/12/27: 139,817
362. 2017/10/03: 268,755
363. 2013/12/24: 123,132
363. 2014/11/25: 168,038
363. 2015/05/24: 192,989
364. 2016/12/29: 143,017
363. 2017/10/14: 282,555
364. 2013/12/28: 123,181
364. 2014/09/21: 169,677
364. 2015/05/03: 212,805
365. 2016/01/02: 143,955
364. 2017/12/25: 290,062
365. 2013/12/23: 133,922
365. 2014/11/23: 179,574
365. 2015/03/09: 220,302
366. 2016/12/25: 145,813
365. 2017/10/01: 331,807
‘romney’: 2018
‘romney’: 2019
‘romney’: 2020
‘romney’: 2021
median rank = 102,733
median rank = 56,724
median rank = 36,905
median rank = 104,398
∼‘serbia’
∼‘nepal’
∼‘bangladesh’
∼‘ﬁji’
1. 2018/01/02: 2,052
1. 2019/01/02: 457
1. 2020/02/05: 288
1. 2021/01/06: 1,566
2. 2018/02/16: 3,802
2. 2019/10/05: 968
2. 2020/02/06: 713
2. 2021/01/03: 2,822
3. 2018/02/20: 4,305
3. 2019/10/06: 1,381
3. 2020/09/22: 1,179
3. 2021/02/10: 3,127
4. 2018/04/22: 4,445
4. 2019/01/03: 1,520
4. 2020/06/07: 1,549
4. 2021/01/02: 3,597
5. 2018/01/03: 4,469
5. 2019/10/21: 1,715
5. 2020/01/31: 1,716
5. 2021/02/13: 3,621
6. 2018/04/24: 7,071
6. 2019/04/20: 1,951
6. 2020/07/11: 1,783
6. 2021/05/02: 3,960
7. 2018/03/05: 7,171
7. 2019/10/04: 2,660
7. 2020/02/07: 1,901
7. 2021/01/24: 4,771
8. 2018/02/19: 8,576
8. 2019/04/19: 2,935
8. 2020/06/08: 2,395
8. 2021/01/05: 4,793
9. 2018/06/27: 9,871
9. 2019/01/01: 3,040
9. 2020/01/27: 2,469
9. 2021/01/07: 4,925
10. 2018/02/17: 10,717
10. 2019/10/07: 3,204
10. 2020/11/20: 2,774
10. 2021/02/11: 6,864
· · ·
· · ·
· · ·
· · ·
361. 2018/07/29: 281,189
361. 2019/07/10: 212,718
362. 2020/04/25: 134,400
291. 2021/04/07: 264,099
362. 2018/08/05: 286,269
362. 2019/02/13: 213,194
363. 2020/03/31: 135,777
292. 2021/09/08: 280,442
363. 2018/12/28: 317,186
363. 2019/09/01: 225,726
364. 2020/01/03: 148,910
293. 2021/08/20: 299,271
364. 2018/12/05: 318,783
364. 2019/04/03: 235,546
365. 2020/01/04: 181,931
294. 2021/08/03: 308,540
365. 2018/12/09: 321,224
365. 2019/04/14: 246,341
366. 2020/04/02: 210,910
295. 2021/10/17: 325,147
TABLE A4. Median rank and overall top 10 and bottom 5 rank days for each calendar year for ‘romney’. Time
range covered: 2008/09/09 through to 2021/10/24.


## Page 27


27
‘hillary’: 2008
‘hillary’: 2009
‘hillary’: 2010
‘hillary’: 2011
‘hillary’: 2012
median rank = 6,182
median rank = 13,448
median rank = 24,602
median rank = 33,766
median rank = 34,585
∼‘malaysia’
∼‘ecuador’
∼‘wales’
∼‘bolivia’
∼‘honduras’
1. 2008/11/14: 910
1. 2009/01/13: 1,669
1. 2010/01/21: 5,180
1. 2011/08/14: 3,161
1. 2012/12/30: 4,402
2. 2008/11/21: 1,016
2. 2009/01/21: 1,925
2. 2010/03/03: 5,985
2. 2011/01/01: 7,674
2. 2012/10/16: 4,950
3. 2008/12/01: 1,213
3. 2009/01/22: 2,049
3. 2010/01/16: 6,319
3. 2011/08/15: 8,249
3. 2012/12/31: 5,116
4. 2008/09/14: 1,383
4. 2009/03/02: 2,870
4. 2010/03/02: 7,268
4. 2011/06/09: 9,181
4. 2012/12/15: 5,946
5. 2008/11/18: 1,780
5. 2009/01/20: 3,001
5. 2010/02/15: 7,430
5. 2011/01/30: 9,349
5. 2012/10/15: 7,809
6. 2008/11/12: 1,795
6. 2009/08/11: 3,190
6. 2010/11/29: 9,087
6. 2011/03/16: 9,600
6. 2012/09/03: 8,595
7. 2008/09/13: 2,030
7. 2009/03/07: 3,297
7. 2010/01/22: 9,321
7. 2011/01/28: 9,679
7. 2012/09/05: 9,213
8. 2008/11/13: 2,297
8. 2009/02/20: 3,586
8. 2010/02/24: 9,342
8. 2011/05/09: 10,093
8. 2012/10/26: 9,807
9. 2008/11/17: 2,535
9. 2009/02/24: 3,659
9. 2010/01/13: 9,542
9. 2011/11/01: 10,234
9. 2012/01/24: 10,062
10. 2008/09/10: 2,622
10. 2009/01/23: 3,763
10. 2010/03/22: 9,646
10. 2011/02/27: 10,348
10. 2012/09/04: 10,337
· · ·
· · ·
· · ·
· · ·
· · ·
110. 2008/11/28: 14,023
343. 2009/11/28: 31,050
361. 2010/12/21: 48,726
361. 2011/11/26: 57,923
362. 2012/02/11: 60,841
111. 2008/12/25: 14,474
344. 2009/12/25: 33,335
362. 2010/11/24: 49,149
362. 2011/11/24: 58,329
363. 2012/02/09: 62,126
112. 2008/12/20: 14,975
345. 2009/12/23: 34,341
363. 2010/11/14: 51,234
363. 2011/12/25: 59,738
364. 2012/03/25: 62,879
113. 2008/12/21: 15,603
346. 2009/11/23: 36,036
364. 2010/11/25: 52,996
364. 2011/11/06: 59,801
365. 2012/12/24: 67,635
114. 2008/12/13: 18,477
347. 2009/11/26: 42,087
365. 2010/12/24: 61,848
365. 2011/10/09: 64,733
366. 2012/12/25: 71,445
‘hillary’: 2013
‘hillary’: 2014
‘hillary’: 2015
‘hillary’: 2016
‘hillary’: 2017
median rank = 35,140
median rank = 24,488
median rank = 6,014
median rank = 1,140
median rank = 2,661
∼‘malta’
∼‘wales’
∼‘malaysia’
∼‘america’
∼‘france’
1. 2013/01/23: 2,475
1. 2014/06/10: 3,594
1. 2015/10/13: 446
1. 2016/11/08: 50
1. 2017/11/03: 536
2. 2013/01/24: 6,883
2. 2014/04/11: 5,182
2. 2015/04/12: 662
2. 2016/11/09: 77
2. 2017/10/30: 605
3. 2013/02/01: 6,998
3. 2014/06/17: 5,304
3. 2015/10/22: 854
3. 2016/09/26: 89
3. 2017/09/13: 654
4. 2013/03/18: 7,251
4. 2014/06/09: 5,670
4. 2015/04/13: 1,068
4. 2016/10/09: 91
4. 2017/11/02: 670
5. 2013/01/02: 7,539
5. 2014/06/11: 7,058
5. 2015/10/14: 1,170
5. 2016/10/19: 110
5. 2017/10/25: 688
6. 2013/05/08: 7,955
6. 2014/04/10: 7,680
6. 2015/12/19: 1,206
6. 2016/09/27: 127
6. 2017/01/20: 696
7. 2013/01/29: 10,952
7. 2014/06/18: 7,740
7. 2015/04/14: 1,533
7. 2016/11/07: 130
7. 2017/11/04: 708
8. 2013/05/09: 11,133
8. 2014/06/12: 8,454
8. 2015/11/14: 1,687
8. 2016/10/20: 132
8. 2017/10/26: 709
9. 2013/05/10: 11,209
9. 2014/06/23: 8,770
9. 2015/04/21: 1,782
9. 2016/10/10: 138
9. 2017/09/12: 801
10. 2013/01/25: 11,236
10. 2014/06/16: 8,874
10. 2015/12/20: 1,804
10. 2016/11/10: 157
10. 2017/06/01: 859
· · ·
· · ·
· · ·
· · ·
· · ·
361. 2013/03/03: 60,786
361. 2014/03/27: 49,541
361. 2015/01/17: 40,311
362. 2016/12/26: 3,710
361. 2017/07/01: 5,435
362. 2013/04/21: 61,766
362. 2014/10/04: 49,691
362. 2015/01/18: 41,476
363. 2016/12/25: 3,734
362. 2017/04/27: 5,437
363. 2013/04/19: 62,263
363. 2014/12/27: 51,427
363. 2015/01/04: 41,824
364. 2016/01/01: 3,969
363. 2017/04/16: 5,618
364. 2013/03/02: 64,804
364. 2014/12/26: 56,748
364. 2015/01/02: 44,119
365. 2016/12/30: 4,231
364. 2017/08/22: 5,647
365. 2013/12/25: 66,346
365. 2014/12/25: 56,900
365. 2015/01/25: 44,401
366. 2016/12/29: 4,375
365. 2017/05/01: 6,683
‘hillary’: 2018
‘hillary’: 2019
‘hillary’: 2020
‘hillary’: 2021
median rank = 3,154
median rank = 4,394
median rank = 5,629
median rank = 28,082
∼‘argentina’
∼‘colombia’
∼‘nigeria’
∼‘poland’
1. 2018/07/16: 713
1. 2019/10/19: 528
1. 2020/10/07: 761
1. 2021/01/20: 4,490
2. 2018/10/24: 723
2. 2019/10/18: 823
2. 2020/02/01: 933
2. 2021/01/27: 4,821
3. 2018/01/29: 906
3. 2019/10/20: 891
3. 2020/01/21: 1,086
3. 2021/01/26: 5,518
4. 2018/02/02: 1,048
4. 2019/10/09: 1,140
4. 2020/09/29: 1,142
4. 2021/01/22: 5,658
5. 2018/10/10: 1,049
5. 2019/10/21: 1,186
5. 2020/10/06: 1,213
5. 2021/01/08: 5,820
6. 2018/07/17: 1,057
6. 2019/04/24: 1,394
6. 2020/10/09: 1,406
6. 2021/01/06: 5,836
7. 2018/03/13: 1,100
7. 2019/09/25: 1,433
7. 2020/01/22: 1,499
7. 2021/01/19: 5,920
8. 2018/06/14: 1,165
8. 2019/10/22: 1,554
8. 2020/08/19: 1,571
8. 2021/01/09: 6,036
9. 2018/06/15: 1,197
9. 2019/09/29: 1,570
9. 2020/03/03: 1,599
9. 2021/09/02: 6,183
10. 2018/12/05: 1,239
10. 2019/10/25: 1,599
10. 2020/03/02: 1,756
10. 2021/01/04: 6,415
· · ·
· · ·
· · ·
· · ·
361. 2018/12/24: 6,619
361. 2019/07/22: 8,125
362. 2020/09/03: 14,972
291. 2021/04/11: 55,012
362. 2018/12/20: 6,649
362. 2019/07/17: 8,243
363. 2020/12/27: 15,428
292. 2021/04/26: 55,023
363. 2018/12/23: 6,709
363. 2019/08/06: 8,288
364. 2020/12/26: 16,254
293. 2021/04/10: 55,471
364. 2018/11/02: 6,727
364. 2019/09/04: 8,362
365. 2020/12/25: 16,387
294. 2021/04/24: 57,078
365. 2018/12/25: 9,619
365. 2019/08/04: 8,653
366. 2020/12/05: 16,908
295. 2021/04/12: 60,070
TABLE A5. Median rank and overall top 10 and bottom 5 rank days for each calendar year for ‘hillary’. Time
range covered: 2008/09/09 through to 2021/10/24.


## Page 28


28
‘trump’: 2008
‘trump’: 2009
‘trump’: 2010
‘trump’: 2011
‘trump’: 2012
median rank = 17,082
median rank = 7,903
median rank = 14,966
median rank = 18,403
median rank = 30,539
∼‘vietnam’
∼‘iran’
∼‘kenya’
∼‘sweden’
∼‘qatar’
1. 2008/10/15: 5,249
1. 2009/05/12: 1,668
1. 2010/01/08: 4,954
1. 2011/04/27: 734
1. 2012/10/24: 1,627
2. 2008/09/18: 5,969
2. 2009/02/17: 3,227
2. 2010/09/09: 6,602
2. 2011/05/01: 829
2. 2012/11/07: 1,921
3. 2008/12/01: 7,074
3. 2009/08/23: 3,617
3. 2010/01/09: 6,717
3. 2011/05/02: 1,097
3. 2012/02/02: 3,081
4. 2008/11/03: 9,773
4. 2009/08/10: 3,663
4. 2010/01/01: 7,233
4. 2011/04/28: 1,533
4. 2012/10/25: 3,672
5. 2008/10/29: 10,238
5. 2009/06/10: 3,670
5. 2010/08/23: 7,252
5. 2011/05/16: 1,629
5. 2012/11/06: 3,936
6. 2008/10/01: 10,608
6. 2009/06/16: 3,709
6. 2010/02/04: 7,384
6. 2011/04/30: 2,235
6. 2012/05/29: 5,487
7. 2008/09/29: 10,651
7. 2009/09/06: 3,729
7. 2010/01/02: 7,728
7. 2011/04/29: 2,402
7. 2012/12/19: 7,474
8. 2008/09/24: 11,086
8. 2009/06/22: 3,746
8. 2010/01/04: 7,758
8. 2011/04/07: 2,991
8. 2012/11/08: 7,483
9. 2008/11/04: 11,534
9. 2009/08/11: 3,799
9. 2010/01/03: 7,947
9. 2011/04/26: 3,337
9. 2012/05/30: 7,764
10. 2008/12/18: 11,588
10. 2009/09/05: 3,882
10. 2010/01/10: 8,007
10. 2011/04/19: 3,422
10. 2012/10/26: 7,876
· · ·
· · ·
· · ·
· · ·
· · ·
110. 2008/09/10: 32,204
343. 2009/01/31: 24,889
361. 2010/11/15: 24,274
361. 2011/10/09: 32,002
362. 2012/09/02: 53,328
111. 2008/09/14: 32,486
344. 2009/01/16: 28,079
362. 2010/11/14: 24,470
362. 2011/11/12: 32,245
363. 2012/12/23: 53,439
112. 2008/09/13: 34,699
345. 2009/02/03: 28,736
363. 2010/10/31: 25,056
363. 2011/11/10: 32,355
364. 2012/12/30: 55,196
113. 2008/10/05: 35,238
346. 2009/01/17: 30,325
364. 2010/10/03: 26,500
364. 2011/11/26: 33,796
365. 2012/12/16: 56,494
114. 2008/12/23: 36,433
347. 2009/01/01: 32,208
365. 2010/10/22: 30,992
365. 2011/11/11: 35,165
366. 2012/10/06: 57,032
‘trump’: 2013
‘trump’: 2014
‘trump’: 2015
‘trump’: 2016
‘trump’: 2017
median rank = 44,982
median rank = 50,332
median rank = 2,465
median rank = 310
median rank = 161
∼‘panama’
∼‘myanmar’
∼‘france’
∼‘bts’
∼‘make’
1. 2013/01/31: 9,358
1. 2014/09/29: 13,069
1. 2015/12/08: 231
1. 2016/11/09: 11
1. 2017/01/20: 29
2. 2013/08/26: 11,411
2. 2014/12/07: 16,983
2. 2015/09/16: 277
2. 2016/11/08: 15
2. 2017/01/21: 37
3. 2013/08/25: 13,078
3. 2014/09/09: 18,183
3. 2015/12/09: 319
3. 2016/11/10: 19
3. 2017/01/30: 55
4. 2013/02/27: 17,309
4. 2014/04/15: 20,071
4. 2015/08/06: 356
4. 2016/10/09: 22
4. 2017/01/29: 58
5. 2013/03/06: 17,694
5. 2014/12/17: 21,503
5. 2015/12/15: 377
5. 2016/09/26: 27
5. 2017/01/22: 60
6. 2013/06/01: 18,782
6. 2014/10/17: 21,529
6. 2015/12/10: 427
6. 2016/10/19: 38
6. 2017/01/28: 61
7. 2013/02/25: 19,323
7. 2014/12/16: 22,067
7. 2015/08/26: 473
7. 2016/11/11: 40
7. 2017/01/25: 62
8. 2013/02/01: 19,789
8. 2014/03/06: 22,330
8. 2015/12/11: 515
8. 2016/10/08: 45
8. 2017/08/15: 62
9. 2013/03/19: 19,940
9. 2014/09/16: 23,032
9. 2015/12/07: 527
9. 2016/10/10: 48
9. 2017/01/26: 63
10. 2013/05/03: 20,647
10. 2014/04/01: 23,090
10. 2015/08/25: 594
10. 2016/09/27: 54
10. 2017/01/31: 63
· · ·
· · ·
· · ·
· · ·
· · ·
361. 2013/08/03: 73,434
361. 2014/05/25: 74,344
361. 2015/04/03: 59,988
362. 2016/01/04: 1,120
361. 2017/01/01: 320
362. 2013/11/24: 75,049
362. 2014/07/19: 75,600
362. 2015/05/24: 60,385
363. 2016/01/06: 1,143
362. 2017/09/09: 326
363. 2013/11/17: 78,219
363. 2014/07/25: 75,672
363. 2015/02/08: 64,066
364. 2016/01/10: 1,143
363. 2017/09/10: 335
364. 2013/11/16: 79,322
364. 2014/08/23: 76,435
364. 2015/03/29: 67,198
365. 2016/01/01: 1,276
364. 2017/05/06: 343
365. 2013/10/26: 81,022
365. 2014/07/27: 77,186
365. 2015/04/04: 70,230
366. 2016/01/11: 1,297
365. 2017/12/25: 384
‘trump’: 2018
‘trump’: 2019
‘trump’: 2020
‘trump’: 2021
median rank = 203
median rank = 219
median rank = 155
median rank = 804
∼‘trump’
∼‘je’
∼‘only’
∼‘exo’
1. 2018/07/16: 63
1. 2019/12/18: 67
1. 2020/11/04: 21
1. 2021/01/06: 27
2. 2018/07/13: 87
2. 2019/09/25: 84
2. 2020/11/07: 26
2. 2021/01/07: 29
3. 2018/07/17: 87
3. 2019/12/19: 89
3. 2020/11/05: 27
3. 2021/01/08: 38
4. 2018/01/12: 89
4. 2019/10/17: 97
4. 2020/09/29: 28
4. 2021/01/09: 53
5. 2018/06/20: 92
5. 2019/10/07: 102
5. 2020/11/03: 30
5. 2021/01/20: 57
6. 2018/06/12: 95
6. 2019/09/24: 105
6. 2020/10/02: 32
6. 2021/01/13: 61
7. 2018/11/07: 100
7. 2019/10/10: 107
7. 2020/11/06: 33
7. 2021/01/10: 70
8. 2018/06/11: 104
8. 2019/10/27: 107
8. 2020/09/30: 38
8. 2021/01/11: 75
9. 2018/01/30: 105
9. 2019/10/09: 108
9. 2020/11/02: 49
9. 2021/01/12: 80
10. 2018/07/18: 108
10. 2019/10/03: 110
10. 2020/06/01: 50
10. 2021/01/14: 90
· · ·
· · ·
· · ·
· · ·
361. 2018/02/25: 362
361. 2019/02/10: 371
362. 2020/05/01: 280
291. 2021/10/01: 1,419
362. 2018/12/31: 364
362. 2019/03/16: 371
363. 2020/05/10: 282
292. 2021/08/03: 1,453
363. 2018/09/29: 392
363. 2019/09/14: 376
364. 2020/05/02: 284
293. 2021/04/22: 1,486
364. 2018/09/28: 397
364. 2019/09/01: 385
365. 2020/01/01: 294
294. 2021/10/03: 1,514
365. 2018/09/23: 405
365. 2019/12/25: 430
366. 2020/12/31: 302
295. 2021/04/21: 1,541
TABLE A6. Median rank and overall top 10 and bottom 5 rank days for each calendar year for ‘trump’. Time
range covered: 2008/09/09 through to 2021/10/24.


## Page 29


29
‘biden’: 2008
‘biden’: 2009
‘biden’: 2010
‘biden’: 2011
‘biden’: 2012
median rank = 2,906
median rank = 16,703
median rank = 33,648
median rank = 62,474
median rank = 61,765
∼‘argentina’
∼‘vietnam’
∼‘bolivia’
∼‘haiti’
∼‘haiti’
1. 2008/10/02: 86
1. 2009/01/20: 775
1. 2010/03/23: 1,759
1. 2011/01/25: 4,137
1. 2012/10/11: 154
2. 2008/10/03: 163
2. 2009/02/07: 1,772
2. 2010/02/14: 3,012
2. 2011/01/28: 6,183
2. 2012/10/12: 746
3. 2008/09/26: 692
3. 2009/04/30: 1,805
3. 2010/03/24: 4,029
3. 2011/08/01: 9,726
3. 2012/09/06: 1,412
4. 2008/09/27: 820
4. 2009/02/24: 2,141
4. 2010/01/27: 4,071
4. 2011/01/10: 13,072
4. 2012/10/13: 4,041
5. 2008/10/04: 925
5. 2009/01/19: 2,148
5. 2010/01/23: 5,144
5. 2011/01/12: 13,187
5. 2012/10/16: 4,409
6. 2008/10/01: 965
6. 2009/01/10: 2,367
6. 2010/03/09: 5,313
6. 2011/08/02: 13,470
6. 2012/11/07: 4,897
7. 2008/10/26: 1,076
7. 2009/05/01: 2,866
7. 2010/03/10: 5,883
7. 2011/04/13: 13,895
7. 2012/11/06: 5,206
8. 2008/09/28: 1,101
8. 2009/01/21: 2,940
8. 2010/02/15: 5,958
8. 2011/04/14: 15,983
8. 2012/01/24: 5,567
9. 2008/10/21: 1,149
9. 2009/07/05: 3,018
9. 2010/02/17: 7,188
9. 2011/03/23: 16,007
9. 2012/08/11: 5,774
10. 2008/09/30: 1,175
10. 2009/02/25: 3,395
10. 2010/01/08: 7,403
10. 2011/08/21: 16,469
10. 2012/08/15: 6,225
· · ·
· · ·
· · ·
· · ·
· · ·
110. 2008/12/13: 22,564
343. 2009/12/27: 66,954
361. 2010/08/01: 100,385
361. 2011/12/17: 197,704
362. 2012/12/16: 207,221
111. 2008/11/29: 24,958
344. 2009/12/08: 68,077
362. 2010/04/18: 102,370
362. 2011/09/18: 207,308
363. 2012/12/14: 217,675
112. 2008/12/08: 24,973
345. 2009/12/21: 77,523
363. 2010/08/29: 103,355
363. 2011/08/14: 210,452
364. 2012/12/25: 223,911
113. 2008/12/18: 26,122
346. 2009/12/30: 78,160
364. 2010/05/23: 116,193
364. 2011/09/25: 224,846
365. 2012/04/08: 246,425
114. 2008/12/25: 26,148
347. 2009/11/29: 103,801
365. 2010/08/14: 140,612
365. 2011/11/24: 274,352
366. 2012/12/15: 263,322
‘biden’: 2013
‘biden’: 2014
‘biden’: 2015
‘biden’: 2016
‘biden’: 2017
median rank = 66,948
median rank = 65,371
median rank = 50,396
median rank = 30,047
median rank = 47,706
∼‘lebanon’
∼‘lebanon’
∼‘myanmar’
∼‘qatar’
∼‘maldives’
1. 2013/01/21: 4,171
1. 2014/01/28: 4,372
1. 2015/10/21: 1,276
1. 2016/11/12: 368
1. 2017/01/12: 440
2. 2013/02/12: 5,795
2. 2014/10/04: 7,027
2. 2015/05/30: 2,282
2. 2016/11/13: 368
2. 2017/11/20: 930
3. 2013/01/10: 7,828
3. 2014/04/22: 7,759
3. 2015/05/31: 2,329
3. 2016/11/11: 459
3. 2017/01/13: 1,064
4. 2013/01/20: 8,705
4. 2014/10/06: 11,095
4. 2015/01/20: 3,982
4. 2016/11/14: 704
4. 2017/01/20: 1,085
5. 2013/01/11: 11,434
5. 2014/10/05: 12,753
5. 2015/10/13: 4,454
5. 2016/07/27: 1,073
5. 2017/01/14: 1,647
6. 2013/01/09: 11,484
6. 2014/06/16: 12,868
6. 2015/06/06: 4,725
6. 2016/11/15: 1,113
6. 2017/01/11: 1,878
7. 2013/12/04: 14,052
7. 2014/09/03: 13,076
7. 2015/10/19: 5,295
7. 2016/11/10: 1,515
7. 2017/11/21: 2,056
8. 2013/01/16: 14,367
8. 2014/10/17: 13,217
8. 2015/09/11: 5,910
8. 2016/11/16: 1,557
8. 2017/11/14: 2,446
9. 2013/01/24: 17,328
9. 2014/10/07: 14,147
9. 2015/10/20: 6,047
9. 2016/11/18: 1,833
9. 2017/01/10: 2,550
10. 2013/01/04: 17,717
10. 2014/11/04: 14,631
10. 2015/08/24: 6,451
10. 2016/11/09: 1,987
10. 2017/01/21: 2,553
· · ·
· · ·
· · ·
· · ·
· · ·
361. 2013/07/04: 180,247
361. 2014/01/04: 173,263
361. 2015/05/12: 169,385
362. 2016/02/21: 123,337
361. 2017/05/10: 163,312
362. 2013/10/19: 181,324
362. 2014/01/19: 188,511
362. 2015/04/04: 173,674
363. 2016/01/04: 142,992
362. 2017/07/21: 167,845
363. 2013/07/08: 184,742
363. 2014/05/25: 189,314
363. 2015/04/05: 176,441
364. 2016/01/02: 173,532
363. 2017/06/30: 174,606
364. 2013/07/07: 197,104
364. 2014/02/22: 191,427
364. 2015/05/24: 194,785
365. 2016/01/03: 192,145
364. 2017/07/09: 176,624
365. 2013/07/12: 206,605
365. 2014/04/06: 193,917
365. 2015/12/21: 210,770
366. 2016/01/01: 196,663
365. 2017/07/14: 186,035
‘biden’: 2018
‘biden’: 2019
‘biden’: 2020
‘biden’: 2021
median rank = 40,538
median rank = 3,643
median rank = 683
median rank = 849
∼‘austria’
∼‘indonesia’
∼‘army’
∼‘exo’
1. 2018/03/22: 851
1. 2019/09/25: 342
1. 2020/11/07: 24
1. 2021/01/20: 59
2. 2018/03/23: 2,130
2. 2019/04/25: 422
2. 2020/11/04: 36
2. 2021/01/21: 84
3. 2018/03/24: 2,879
3. 2019/11/20: 539
3. 2020/09/29: 52
3. 2021/01/22: 120
4. 2018/10/25: 3,472
4. 2019/10/15: 563
4. 2020/11/06: 54
4. 2021/08/16: 131
5. 2018/08/30: 3,499
5. 2019/09/24: 573
5. 2020/10/22: 57
5. 2021/01/23: 170
6. 2018/09/26: 4,690
6. 2019/10/03: 612
6. 2020/09/30: 59
6. 2021/08/26: 175
7. 2018/12/04: 4,909
7. 2019/06/27: 625
7. 2020/11/05: 59
7. 2021/08/15: 216
8. 2018/09/17: 5,163
8. 2019/06/28: 627
8. 2020/11/03: 69
8. 2021/08/31: 224
9. 2018/09/25: 5,232
9. 2019/09/26: 640
9. 2020/11/08: 69
9. 2021/01/24: 229
10. 2018/09/16: 5,354
10. 2019/09/21: 661
10. 2020/11/09: 83
10. 2021/01/19: 241
· · ·
· · ·
· · ·
· · ·
361. 2018/08/19: 144,172
361. 2019/01/17: 49,174
362. 2020/01/09: 3,623
291. 2021/08/08: 1,736
362. 2018/04/29: 145,049
362. 2019/02/08: 51,218
363. 2020/01/08: 3,673
292. 2021/07/11: 1,823
363. 2018/01/20: 146,267
363. 2019/01/30: 54,088
364. 2020/01/05: 3,701
293. 2021/05/09: 1,879
364. 2018/05/17: 147,944
364. 2019/01/20: 61,160
365. 2020/01/10: 4,004
294. 2021/05/23: 2,094
365. 2018/02/03: 165,685
365. 2019/01/31: 63,196
366. 2020/01/11: 4,264
295. 2021/08/03: 2,266
TABLE A7. Median rank and overall top 10 and bottom 5 rank days for each calendar year for ‘biden’. Time
range covered: 2008/09/09 through to 2021/10/24.


## Page 30


30
‘@bts twt’: 2013
‘@bts twt’: 2014
‘@bts twt’: 2015
‘@bts twt’: 2016
‘@bts twt’: 2017
median rank = 22,140
median rank = 5,114
median rank = 1,568
median rank = 806
median rank = 299
∼‘afghanistan’
∼‘pakistan’
∼‘uk’
∼‘exo’
∼‘bts’
1. 2013/12/03: 4,217
1. 2014/12/31: 967
1. 2015/12/29: 176
1. 2016/12/29: 99
1. 2017/05/21: 9
2. 2013/12/31: 4,384
2. 2014/12/29: 979
2. 2015/12/31: 260
2. 2016/12/26: 110
2. 2017/05/01: 11
3. 2013/11/30: 4,393
3. 2014/12/23: 1,357
3. 2015/12/30: 359
3. 2016/11/19: 127
3. 2017/05/20: 13
4. 2013/12/29: 4,559
4. 2014/12/26: 1,405
4. 2015/12/03: 368
4. 2016/12/02: 134
4. 2017/05/02: 14
5. 2013/11/14: 5,778
5. 2014/08/31: 1,417
5. 2015/12/11: 368
5. 2016/12/30: 137
5. 2017/05/04: 14
6. 2013/10/12: 5,842
6. 2014/12/07: 1,454
6. 2015/11/07: 386
6. 2016/09/11: 158
6. 2017/05/05: 15
7. 2013/11/27: 5,883
7. 2014/12/03: 1,471
7. 2015/09/11: 414
7. 2016/08/31: 162
7. 2017/05/03: 16
8. 2013/11/28: 6,129
8. 2014/12/20: 1,474
8. 2015/12/21: 415
8. 2016/02/17: 167
8. 2017/05/06: 18
9. 2013/12/02: 6,296
9. 2014/12/24: 1,482
9. 2015/10/12: 416
9. 2016/05/12: 173
9. 2017/05/19: 18
10. 2013/12/01: 6,413
10. 2014/10/12: 1,575
10. 2015/11/29: 420
10. 2016/05/07: 174
10. 2017/05/07: 19
· · ·
· · ·
· · ·
· · ·
· · ·
319. 2013/04/27: 882,731
361. 2014/01/22: 20,076
361. 2015/04/09: 6,064
362. 2016/02/25: 2,770
361. 2017/02/10: 1,347
320. 2013/01/20: 882,966
362. 2014/04/18: 21,239
362. 2015/04/14: 6,657
363. 2016/09/28: 2,869
362. 2017/03/15: 1,394
321. 2013/02/10: 929,849
363. 2014/04/23: 21,270
363. 2015/04/16: 6,805
364. 2016/09/29: 2,893
363. 2017/01/11: 1,506
322. 2013/01/09: 952,557
364. 2014/04/19: 22,663
364. 2015/02/21: 6,899
365. 2016/04/12: 3,209
364. 2017/03/16: 1,783
323. 2013/02/25: 986,266
365. 2014/04/20: 25,221
365. 2015/04/13: 7,150
366. 2016/09/27: 3,210
365. 2017/01/31: 1,893
‘@bts twt’: 2018
‘@bts twt’: 2019
‘@bts twt’: 2020
‘@bts twt’: 2021
median rank = 61
median rank = 93
median rank = 121
median rank = 120
∼‘by’
∼‘more’
∼‘go’
∼‘go’
1. 2018/05/20: 3
1. 2019/05/01: 12
1. 2020/11/22: 17
1. 2021/05/23: 10
2. 2018/05/15: 4
2. 2019/04/22: 13
2. 2020/08/31: 20
2. 2021/05/19: 17
3. 2018/05/14: 6
3. 2019/04/24: 15
3. 2020/11/24: 24
3. 2021/05/10: 19
4. 2018/05/16: 8
4. 2019/02/10: 17
4. 2020/12/06: 25
4. 2021/05/21: 19
5. 2018/05/18: 8
5. 2019/03/16: 18
5. 2020/08/07: 26
5. 2021/03/14: 22
6. 2018/05/17: 11
6. 2019/04/23: 18
6. 2020/08/21: 28
6. 2021/05/11: 23
7. 2018/05/19: 11
7. 2019/04/28: 18
7. 2020/10/12: 28
7. 2021/09/20: 25
8. 2018/01/25: 14
8. 2019/04/29: 18
8. 2020/12/03: 32
8. 2021/05/12: 27
9. 2018/12/14: 14
9. 2019/03/02: 19
9. 2020/07/28: 33
9. 2021/05/18: 28
10. 2018/02/25: 15
10. 2019/04/25: 19
10. 2020/12/05: 38
10. 2021/06/14: 29
· · ·
· · ·
· · ·
· · ·
361. 2018/03/27: 215
361. 2019/08/22: 233
362. 2020/03/28: 300
291. 2021/10/17: 390
362. 2018/03/29: 222
362. 2019/12/11: 246
363. 2020/05/28: 320
292. 2021/10/21: 390
363. 2018/01/03: 234
363. 2019/08/28: 257
364. 2020/05/29: 323
293. 2021/10/10: 395
364. 2018/01/08: 255
364. 2019/12/21: 260
365. 2020/06/01: 330
294. 2021/10/09: 396
365. 2018/01/05: 267
365. 2019/12/18: 274
366. 2020/03/24: 335
295. 2021/09/17: 410
TABLE A8.
Median rank and overall top 10 and bottom 5 rank days for each calendar year for ‘@bts twt’
(2013–2020). Time range covered: 2008/09/09 through to 2021/10/24. Note that BTS was ranked lower than 106 on some
days of 2013.


## Page 31


31
‘god’: 2008
‘god’: 2009
‘god’: 2010
‘god’: 2011
‘god’: 2012
median rank = 376
median rank = 294
median rank = 340
median rank = 329
median rank = 273
∼‘vote’
∼‘bts’
∼‘vote’
∼‘bts’
∼‘were’
1. 2008/11/05: 239
1. 2009/10/20: 136
1. 2010/04/26: 229
1. 2011/03/11: 188
1. 2012/11/22: 205
2. 2008/12/18: 256
2. 2009/03/31: 194
2. 2010/09/11: 229
2. 2011/09/11: 215
2. 2012/12/24: 209
3. 2008/12/25: 269
3. 2009/07/04: 202
3. 2010/04/25: 236
3. 2011/12/25: 226
3. 2012/02/18: 210
4. 2008/11/27: 298
4. 2009/04/12: 210
4. 2010/01/01: 238
4. 2011/12/24: 229
4. 2012/12/14: 210
5. 2008/12/24: 302
5. 2009/09/11: 211
5. 2010/01/13: 239
5. 2011/11/24: 230
5. 2012/11/06: 212
6. 2008/11/04: 307
6. 2009/06/25: 214
6. 2010/02/27: 244
6. 2011/12/31: 235
6. 2012/04/08: 216
7. 2008/09/21: 310
7. 2009/12/25: 215
7. 2010/04/04: 247
7. 2011/09/21: 238
7. 2012/11/07: 222
8. 2008/11/16: 310
8. 2009/11/26: 222
8. 2010/01/14: 250
8. 2011/12/11: 240
8. 2012/01/01: 225
9. 2008/10/12: 319
9. 2009/06/28: 226
9. 2010/12/25: 251
9. 2011/12/18: 250
9. 2012/12/31: 230
10. 2008/09/28: 320
10. 2009/12/24: 230
10. 2010/01/10: 252
10. 2011/11/20: 253
10. 2012/08/07: 232
· · ·
· · ·
· · ·
· · ·
· · ·
110. 2008/09/10: 409
343. 2009/01/26: 382
361. 2010/07/03: 396
361. 2011/02/12: 386
362. 2012/03/24: 308
111. 2008/09/16: 411
344. 2009/01/02: 385
362. 2010/12/29: 396
362. 2011/05/28: 388
363. 2012/03/31: 311
112. 2008/11/17: 411
345. 2009/02/03: 385
363. 2010/07/02: 401
363. 2011/02/14: 389
364. 2012/02/04: 312
113. 2008/09/15: 412
346. 2009/03/09: 395
364. 2010/09/06: 415
364. 2011/01/29: 391
365. 2012/06/09: 315
114. 2008/11/12: 529
347. 2009/03/20: 417
365. 2010/12/28: 424
365. 2011/02/19: 391
366. 2012/05/05: 321
‘god’: 2013
‘god’: 2014
‘god’: 2015
‘god’: 2016
‘god’: 2017
median rank = 292
median rank = 326
median rank = 304
median rank = 297
median rank = 300
∼‘bts’
∼‘bts’
∼‘bts’
∼‘bts’
∼‘bts’
1. 2013/03/31: 216
1. 2014/07/12: 134
1. 2015/10/24: 188
1. 2016/11/09: 204
1. 2017/08/28: 205
2. 2013/02/03: 221
2. 2014/01/26: 233
2. 2015/06/26: 211
2. 2016/12/31: 214
2. 2017/08/27: 221
3. 2013/02/10: 228
3. 2014/04/20: 242
3. 2015/09/26: 213
3. 2016/12/25: 233
3. 2017/01/20: 229
4. 2013/04/15: 228
4. 2014/01/19: 249
4. 2015/10/23: 214
4. 2016/07/08: 236
4. 2017/08/29: 229
5. 2013/08/25: 230
5. 2014/01/24: 254
5. 2015/12/24: 232
5. 2016/11/08: 238
5. 2017/04/16: 234
6. 2013/07/13: 232
6. 2014/09/21: 255
6. 2015/09/25: 236
6. 2016/01/01: 239
6. 2017/10/06: 235
7. 2013/12/24: 233
7. 2014/01/01: 260
7. 2015/10/11: 238
7. 2016/01/10: 244
7. 2017/01/01: 241
8. 2013/01/01: 234
8. 2014/07/07: 262
8. 2015/12/31: 241
8. 2016/12/30: 248
8. 2017/07/04: 241
9. 2013/07/14: 235
9. 2014/08/01: 264
9. 2015/09/27: 243
9. 2016/03/27: 250
9. 2017/11/06: 245
10. 2013/01/20: 240
10. 2014/05/28: 269
10. 2015/10/12: 243
10. 2016/10/27: 251
10. 2017/11/08: 246
· · ·
· · ·
· · ·
· · ·
· · ·
361. 2013/12/07: 353
361. 2014/12/19: 396
361. 2015/03/07: 403
362. 2016/12/03: 344
361. 2017/01/25: 351
362. 2013/12/27: 362
362. 2014/11/15: 401
362. 2015/02/14: 405
363. 2016/12/02: 345
362. 2017/09/16: 352
363. 2013/12/26: 365
363. 2014/12/13: 402
363. 2015/02/13: 407
364. 2016/08/05: 353
363. 2017/06/08: 354
364. 2013/12/21: 368
364. 2014/11/08: 411
364. 2015/03/27: 408
365. 2016/11/18: 358
364. 2017/12/01: 362
365. 2013/11/29: 369
365. 2014/11/28: 411
365. 2015/02/20: 413
366. 2016/11/19: 362
365. 2017/12/16: 366
‘god’: 2018
‘god’: 2019
‘god’: 2020
‘god’: 2021
median rank = 295
median rank = 294
median rank = 306
median rank = 359
∼‘bts’
∼‘bts’
∼‘bts’
∼‘vote’
1. 2018/07/13: 188
1. 2019/05/12: 186
1. 2020/10/20: 176
1. 2021/01/01: 229
2. 2018/11/06: 205
2. 2019/03/24: 202
2. 2020/01/26: 186
2. 2021/01/20: 252
3. 2018/07/14: 217
3. 2019/04/19: 205
3. 2020/04/12: 197
3. 2021/04/18: 255
4. 2018/06/18: 218
4. 2019/04/18: 208
4. 2020/10/21: 204
4. 2021/06/12: 268
5. 2018/09/01: 218
5. 2019/02/08: 216
5. 2020/10/11: 210
5. 2021/03/16: 283
6. 2018/04/20: 220
6. 2019/08/11: 216
6. 2020/12/31: 213
6. 2021/02/10: 284
7. 2018/09/18: 221
7. 2019/11/03: 217
7. 2020/12/25: 216
7. 2021/07/21: 284
8. 2018/10/06: 221
8. 2019/02/09: 225
8. 2020/01/01: 218
8. 2021/09/14: 284
9. 2018/09/16: 229
9. 2019/10/06: 225
9. 2020/12/24: 218
9. 2021/04/20: 285
10. 2018/07/17: 234
10. 2019/03/31: 228
10. 2020/07/04: 224
10. 2021/06/13: 285
· · ·
· · ·
· · ·
· · ·
361. 2018/04/14: 350
361. 2019/01/24: 349
362. 2020/02/28: 375
291. 2021/08/31: 418
362. 2018/02/17: 359
362. 2019/12/13: 351
363. 2020/02/27: 377
292. 2021/10/08: 424
363. 2018/02/16: 361
363. 2019/07/01: 360
364. 2020/03/14: 380
293. 2021/07/26: 427
364. 2018/01/29: 366
364. 2019/11/13: 364
365. 2020/06/08: 382
294. 2021/05/10: 429
365. 2018/01/25: 375
365. 2019/10/24: 365
366. 2020/06/11: 383
295. 2021/05/04: 435
TABLE A9. Time range covered: 2013/01/01 through to 2021/10/24. Median rank and overall top 10 and bottom 5
rank days for each calendar year for ‘god’.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1910_00149v3_fame_and_ultrafame_measuring_and_comparing_daily_levels_of_being_talked_about
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1910_00149V3_FAME_AND_ULTRAFAME_MEASURING_AND_COMPARING_DAILY_LEVELS_OF_BEING_TALKED_ABOUT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
