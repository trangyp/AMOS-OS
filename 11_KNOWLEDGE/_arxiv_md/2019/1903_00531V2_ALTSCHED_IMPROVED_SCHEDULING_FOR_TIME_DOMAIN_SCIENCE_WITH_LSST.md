---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.00531v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1903.00531v2_ALTSched__Improved_Scheduling_for_Time-Domain_Science_with_LSST

> Source: 1903.00531v2_ALTSched__Improved_Scheduling_for_Time-Domain_Science_with_LSST.pdf

> Pages: 18

---


## Page 1


Draft version July 17, 2019
Typeset using LATEX default style in AASTeX62
ALTSched: Improved Scheduling for Time-Domain Science with LSST
Daniel Rothchild,1 Christopher Stubbs,2 and Peter Yoachim3
1Department of Electrical Engineering and Computer Science, University of California, Berkeley
2Department of Physics, Center for Astrophysics, Harvard University
3Department of Astronomy, University of Washington
ABSTRACT
Telescope scheduling is the task of determining the best sequence of observations (pointings and ﬁlter
choices) for a survey system. Because it is computationally intractable to optimize over all possible
multi-year sequences of observations, schedulers use heuristics to pick the best observation at a given
time. A greedy scheduler selects the next observation by choosing whichever one maximizes a scalar
merit function, which serves as a proxy for the scientiﬁc goals of the telescope. This sort of bottom-up
approach for scheduling is not guaranteed to produce a schedule for which the sum of merit over all
observations is maximized. As an alternative to greedy schedulers, we introduce ALTSched, which
takes a top-down approach to scheduling. Instead of considering only the next observation, ALTSched
makes global decisions about which area of sky and which ﬁlter to observe in, and then reﬁnes these
decisions into a sequence of observations taken along the meridian to maximize SNR. We implement
ALTSched for the Large Synoptic Survey Telescope (LSST), and show that it equals or outperforms
the baseline greedy scheduler in essentially all quantitative performance metrics. Due to its simplicity,
our implementation is considerably faster than OpSim, the simulated greedy scheduler currently used
by the LSST Project: a full ten year survey can be simulated in 4 minutes, as opposed to tens of
hours for OpSim. LSST’s hardware is ﬁxed, so improving the scheduling algorithm is one of the only
remaining ways to optimize LSST’s performance. We see ALTSched as a prototype scheduler that
gives a lower bound on the performance achievable by LSST.
1. INTRODUCTION
LSST is a large ground-based survey system scheduled to begin operations in 2022. With the capability to survey the
entire southern sky in 6 bands about once a week, LSST will enable time-domain astronomy at an unprecedented scale.
The telescope was designed with four primary science goals in mind: to understand dark matter and dark energy;
to catalog the solar system; to study the structure and formation of the Milky Way; and, perhaps most uniquely
suited to LSST’s particular characteristics, to explore the large frontier of time-domain astronomy. These science goals
motivate a range of competing technical metrics that LSST should optimize. Presenting a full list of science cases for
LSST and accompanying technical metrics is beyond the scope of this paper; we refer readers to the LSST observing
strategy whitepaper (LSST Science Collaborations et al. 2017). Here we present only a few representative examples
(with science cases in parentheses), which we believe are especially sensitive to scheduling decisions:
Corresponding author: Daniel Rothchild
drothchild@berkeley.edu
arXiv:1903.00531v2  [astro-ph.IM]  16 Jul 2019


## Page 2


2
long observing seasons (parallax
measurements, AGN variability,
few-months-long transients)
⇐⇒
high cadence (faster transients, better
characterization of light curves)
large survey area (large-scale structure, weak
lensing, galaxy/star surveys)
⇐⇒
higher co-added depth (studying fainter
objects)
few ﬁlter changes (maximize survey eﬃciency)
⇐⇒
many ﬁlter changes (obtain nightly colors for
variables & transients)
large overlap between neighboring
observations (rapid revisits for very fast
transients)
⇐⇒
small overlap between neighboring
observations (cover a larger area per unit time)
multiple observations per ﬁeld per night
(link asteroids, probe ~hour-scale variability)
⇐⇒
one observation per ﬁeld per night
(transients that don’t change in ~1 hour)
With the LSST Project well into the construction phase, the system’s hardware characteristics (aperture, ﬁeld size,
slew rate, ﬁeld of view, sensor quantum eﬃciency...) are ﬁxed. Apart from actively engineering the weather in Chile,
the only remaining opportunities to extract additional performance from the LSST system are in the scheduler and in
the data reduction pipeline. LSST’s existing scheduler, called OpSim, is a greedy algorithm: it chooses the next ﬁeld
to observe by maximizing a scalar merit function intended as a proxy for the scientiﬁc merit of observing the ﬁeld.
This approach is appealing in its apparent simplicity, but as we show below, even after over a decade of development,
OpSim under-performs on many science metrics, particularly in the time-domain science so critical to LSST’s mission.
We argue here that the fault lies not in any implementation detail, but rather in the fundamental nature of greedy
algorithms: because they make scheduling decisions only one or a few observations in advance, the parameters of the
algorithm give scientists little or no control over many 10-year global properties of the schedule.
To remedy this, we introduce and analyze an alternative scheduling algorithm, ALTSched, which makes scheduling
decisions with a top-down hierarchical approach, instead of using a purely bottom-up local merit function. We defer a
full description of ALTSched to Section 3, but simply put, our algorithm ﬁrst decides which region of sky to observe
(nightly), then which particular area and ﬁlter to use (hourly), and only then which individual pointings to observe
(minute-scale). In contrast, OpSim chooses every next observation ab initio, with no planning horizon larger than 30
seconds and no global strategy except what is encoded indirectly through the merit function.
One major advantage of ALTSched is that the parameters of the algorithm directly control ﬁnal properties of
the schedule. For example, ALTSched observes either the Northern or Southern sky each night. Because LSST
can observe about half of the sky each night, we can obtain a universal 2-day revisit cadence simply by assigning
even-numbered nights to the Northern sky and odd-numbered nights to the Southern sky. Diﬀerent cadences (e.g.
with some 1- and 3-day revisits) are equally simple with a diﬀerent pattern of North and South. Importantly, there
is no known way to similarly modify this distribution of revisit times in OpSim, except by adjusting the weights and
penalties of the merit function speciﬁcally to mimic the exact behavior of ALTSched.
As of the writing of this paper, the LSST Project is planning to run a suite of OpSim simulations in order to choose
a ﬁnal observing strategy for LSST. One point of this paper is to argue that optimizing over the parameters of OpSim
in this way will not yield an optimal survey strategy. Taking the example above one step further before giving a fuller
analysis in 4, the gaps between observations to a particular sky pixel resemble an exponential distribution for every
OpSim run we have analyzed, over a wide range of OpSim’s parameters. An exponential distribution of revisit times
is consistent with the timing of observations following a random process. In ALTSched, the shape of this distribution
can be easily controlled. Instead of running more and more OpSim simulations, we therefore advocate exploring how
OpSim can be made to reproduce the survey strategy of ALTSched, and how ALTSched’s cadence can be further
improved.
In the sections that follow, we ﬁrst summarize the LSST baseline scheduler and the tools used to assess the scientiﬁc
performance of various alternatives. We then describe the implementation of our alternative scheduler, ALTSched,
and make quantitative performance comparisons to the LSST baseline. We close with a discussion and some suggestions
for future work.


## Page 3


3
2. OpSim
To provide context for ALTSched, the algorithm we propose below, we ﬁrst introduce LSST’s current baseline
scheduling algorithm.1
LSST’s current scheduler is part of a package called the Operations Simulator (OpSim) (Delgado & Reuter 2016).
OpSim uses a greedy algorithm to choose ﬁelds based on a proposal system, where abstractions of diﬀerent scientiﬁc
proposals give a score for each candidate ﬁeld, and the scheduler chooses the ﬁeld with the highest combined score,
or merit. OpSim considers a number of criteria in its merit function, including time since last observation, co-added
depth achieved thus far, airmass and sky brightness at the proposed pointing, slew time to reach the pointing, etc.
For a full description of the complex merit function used for minion 1016, we refer readers to Delgado et al. (2014,
§5). Once an observation is chosen and executed, the merit scores are recalculated for every candidate ﬁeld, and the
process repeats. The parameters of OpSim are the weights and penalties associated with the various inputs to the
merit function. Although easily interpretable in the context of local decision making, these parameters have no simple
connection to many of the scheduling decisions we actually want to make: the average and distribution of season
lengths and of revisit times; the colors (or lack thereof) obtained during a single night; the uniformity of light curve
sampling over time; etc. In contrast, as we show below, ALTSched’s parameters directly control these properties.
Included with OpSim is a module that simulates the system hardware, weather, seeing conditions, and downtime.
For fairness of comparison, ALTSched uses the exact same calculations, though we re-implement the simulator to
improve computational eﬃciency. In particular, we obey all physical constraints on the telescope, including making no
observations below LSST’s minimum elevation or in the zenith avoidance area, accounting for readout time, shutter
time, slew speed, settle time, optics correction time, and ﬁlter change time, only using 5 of LSST’s 6 band-pass ﬁlters
per night, etc. Taking slew time as an example: both OpSim and ALTSched use the same slew calculation, described
in Delgado et al. (2014, §6). In short, the slew time is calculated assuming uniform accelerated motion of the telescope
mount and dome, plus some settle time.
To compare simulated surveys, the LSST Project has developed a useful suite of analysis tools, the Metrics Analysis
Framework (MAF), that can evaluate candidate schedules by computing various performance metrics of interest (Jones
et al. 2014). Examples include the number of type Ia supernova light curves that meet certain criteria, the distribution
of co-added depths over the observed region, the anticipated uncertainty in parallax and proper motion measurements.
This framework is critical for the fair evaluation of simulated surveys.
A number of OpSim runs, or simulated surveys, have been released by the Project. At the time this work was
carried out, the baseline simulated survey was minion 1016, and we compare our results to those of minion 1016.
Later versions of OpSim have improved on a number of metrics, but all runs we have analyzed since minion 1016
suﬀer from poor time-domain performance. For example, none of the cadences released with the recent whitepaper
call recover even half as many well-sampled SNIa without eliminating visit pairs or changing the exposure time (where
“well-sampled” is as deﬁned below). And to our knowledge, no OpSim or feature-scheduler run at all has exceeded
ALTSched in this metric. Results for minion 1016 are presented in more depth in Section 4.
Several alternatives to OpSim have also been proposed.
Naghib et al. (2016) frame the scheduling problem as
a Markovian decision process.
Ridgway (2015) proposes scheduling LSST by dividing observing into blocks that
are observed (and then reobserved) in an optimal manner. Ridgway’s proposal is similar in spirit to the algorithm
developed and described in this paper.
3. ALTSched
In this section, we introduce ALTSched, an alternative scheduling algorithm for LSST. In the next section, we
introduce a number of metrics, and demonstrate quantitatively that ALTSched equals or outperforms the existing
OpSim baseline minion 1016 on these metrics.
3.1. ALTSched Algorithm
ALTSched is a deterministic scheduling algorithm: in a given night, it does not adapt to current weather or seeing
conditions. Although in principle, adjusting a schedule to take prevailing weather conditions into account should only
improve a scheduler, we justify our decision to use a non-adaptive algorithm in three ways: 1) maintaining a consistent
1 The LSST scheduler is undergoing continual development, and the version of OpSim described and compared with in this article has
been superseded, but it was the baseline plan at the time this work was completed.


## Page 4


4
0
20
40
60
80
100
120
140
160
180
Distance to the moon (degrees)
0
5000
10000
15000
20000
25000
Count
u
g
r
i
z
y
Figure 1. Histogram of angular distance between ALTSched’s observations and the moon. Only a small fraction of observations
fall closer than 30◦to the moon, and of those, a number occur when the moon is only slightly illuminated.
cadence – i.e. avoiding long observation gaps – is diﬃcult to do if the scheduler aggressively avoids regions with poorer
observing conditions, since by random chance, some regions will go unobserved for a long time; 2) the best seeing
tends to occur on the meridian (at minimum airmass), which is where ALTSched observes anyway; 3) one strength
of ALTSched is that it achieves such high performance even without dynamically reacting to observing conditions.
We only expect our performance to improve with the judicious addition of poor-weather avoidance.
The algorithm itself is remarkably simple. Each night, it chooses whether to observe the Northern or Southern sky
based on which region has received fewer visits so far, and then during the night it scans North and South of the
meridian, taking 30-second exposures and then slewing by approximately one ﬁeld width. LSST is on an alt/az mount,
and so has a zenith-avoidance area. To observe the region of sky that passes over zenith, we therefore periodically
scan to the East and West over that region. Each N/S scan is repeated twice in order to obtain two observations per
night, separated by roughly 30-60 minutes. Before repeating a scan, we change ﬁlters so that every ﬁeld is visited in
two bands per night. We refer readers to the video in the supplementary material; the scanning strategy is much more
easily explained visually than in text.
The exact pointings used are drawn from a ﬁxed tiling that is randomly rotated by much more than a ﬁeld size each
night. If a pointing is not used in a given night, it is saved for use in a later night, so that gaps do not persist. The
ﬁxed tiling is chosen as a solution to the Thomson charge-distribution problem for N = 3500 (Thomson 1904).
3.2. Moon Avoidance
One deﬁciency in ALTSched is that it contains no provision for avoiding the moon. minion 1016 uses a conservative
avoidance radius of 30◦. This corresponds to 7% of the celestial sphere, so about 7% of observations should fall within
this avoidance zone. However, 30◦is likely too conservative in times near a new moon and in the redder ﬁlters. We
therefore expect only a few percent of observations to be problematically close to the moon. For observations that fall
too close to the moon, the simulated sky brightness is very high, leading to a low limiting depth for those observations.
So any metric depending on depth should only improve by adding a moon-avoidance module to ALTSched. Figure
1 shows histograms of the angular distance between ALTSched’s observations and the moon. Note that ALTSched
avoids observing in the u and g bands at all when the moon is up and bright, so there are few or no observations in u
or g closer than 30◦to the moon.
3.3. Filter Allocation


## Page 5


5
Most simulated surveys of LSST assume that the telescope will visit each ﬁeld twice per night, with a separation of
∼30 −60 minutes, in order to link asteroid observations. To improve the cadence in each band, ALTSched usually
carries out these two visits in diﬀerent ﬁlters. To accomplish this with a minimal number of ﬁlter changes, we divide
observations into blocks that take ∼30 −60 minutes to observe, and we visit each block twice back-to-back, changing
ﬁlters before revisiting a block (but not between the revisit of a block and the ﬁrst visit to the subsequent block). The
video in the supplementary materials demonstrates this ﬁlter allocation strategy. On average, we execute 11.4 ﬁlter
changes per night, compared to minion 1016’s 4.3. This adds 1.3 seconds to our average slew time over minion 1016,
and allows us to double cadence in each band.
Our ﬁlter allocation strategy is designed such that, in theory, visits to every sky pixel will cycle through the six
ﬁlters in order. Assigning numbers 1 through 6 to LSST’s 6 bandpass ﬁlters (ugrizy), and using arithmetic modulo
6, we start a night in some ﬁlter i, and during the night, before every revisit block, we switch from ﬁlter k to ﬁlter
k + 1. The next night starts in ﬁlter i + 1 and the process repeats, ensuring that visits to each pixel cycle through all
six ﬁlters. In the ideal case, every sky pixel gets a visit in every band once every 6 nights (2 bands every 2 nights,
since we alternate observations between the northern and southern sky).
However, many factors cause us to deviate from this ideal strategy. First, we don’t want a uniform distribution of
total number of visits over ﬁlters, so we replace some observations in, say, the y band, with more in r instead. Second,
we observe y and z preferentially in twilight, since these bands are less sensitive to high sky brightness. Third, we
avoid using u or g when the moon is up and bright. And lastly, the ﬁlter changer can only ﬁt 5 of LSST’s 6 ﬁlters, so
only 5 ﬁlters can be used in a single night. In each of these cases, if a ﬁlter is “not allowed” during a time when the
cyclic allocation strategy would have scheduled it, we simply use some other ﬁlter instead. Besides these intentional
deviations, weather and downtime also cause us to deviate from this ideal strategy in ways that are less predictable.
Overall, ALTSched’s ﬁlter allocation strategy ensures that the per-band cadence is much more regular than in
minion 1016 (as shown below), but there is likely much room for improvement by designing a strategy that more
intelligently takes the four deviations from ideal described above into account.
4. METRICS & RESULTS
As laid out in Section 1, the science drivers of LSST motivate a wide range of technical metrics, many of which
are in tension with each other. Broadly speaking, LSST’s science goals fall into two categories: those that depend
mainly on the ﬁnal co-added images (static science), and those that depend mainly on the temporal distribution
of visits throughout the survey (time-domain science). A full list of results on a variety of metrics is available at
http://altsched.rothchild.me:8080. Here we highlight a small subset of these metrics that are particularly sensitive to
scheduling decisions, especially those where ALTSched and minion 1016 achieve diﬀerent results.
4.1. Static Science
A number of science drivers (e.g. galaxy/star surveys, large-scale structure measurements) use co-added images,
and are largely insensitive to the exact distribution of visits over time. A wide range of static science is enabled by
achieving a higher ﬁnal co-added depth in each band. We therefore use co-added depth as a chief metric for static
science. Single-visit depths and full 10-year co-added depths are shown for both schedulers in Table 1. Since diﬀerent
survey strategies may allocate visits across ﬁlters diﬀerently, we summarize the total co-added performance across
bands with the eﬀective survey time metric Teff. Given design limiting depths Mf for a 30-second exposure in ﬁlter
f ∈F, the eﬀective survey time of a series of exposures E = (mi, fi) which achieved a 5σ limiting depth mi in ﬁlter
fi is given by
Teff =
X
(mi,fi)∈E
30 sec. × 100.8(mi−Mfi).
The 5σ limiting depth of an exposure is computed taking into consideration the sky brightness, seeing, and airmass,
as described in equation 6 of Ivezic et al. (2008). Design depths Mf for LSST are shown in Table 1. These design
depths assume an airmass of 1, r-band seeing of 0.7 arcsec (FWHM), and r-band sky brightness of 21 mag/arcsec2.
In practice, observations are taken under worse conditions, so the total Teff is surprisingly low for a 10-year survey.
Two related metrics are the average slew time (including ﬁlter changes), and the open-shutter fraction, deﬁned as:
OSF =
Texp
Texp + Tslew + Tshutter + Treadout


## Page 6


6
u
g
r
i
z
y
Design (Ideal) Single-Visit Depths
23.9
25.0
24.7
24.0
23.3
22.1
Median Single-Visit Depth (minion 1016)
23.09
24.51
24.05
23.45
22.71
21.78
Median Single-Visit Depth (ALTSched)
23.21
24.50
23.93
23.49
22.90
21.91
Median Co-added Depth (minion 1016)
25.48
27.02
27.03
26.46
25.65
24.73
Median Co-added Depth (ALTSched)
25.61
27.03
27.04
26.35
25.93
24.31
Table 1. The ﬁrst row shows the design speciﬁcation for single-visit 5σ limiting depths for LSST’s six broad-band ﬁlters under
ideal observing conditions (in magnitudes). These depths assume airmass of 1, r-band seeing of 0.7, arcsec (FWHM), and r-band
sky brightness of 21 mag/arcsec2. Sunsequent rows show the actual median single-visit depths achieved by minion 1016 and
ALTSched, and the median (over sky pixels) 10-year co-added depths.
Teff
OSF
Avg. Slew
minion 1016
333 days
0.72
7.4a
ALTSched
329 days
0.69
11.1
aThe average slew time reported elsewhere for minion 1016 is 6.8 seconds. However, the current version of the LSST software stack, which
we use for ALTSched, produces a value of 7.4, which is the value that is comparable to the 11.1 seconds we report for ALTSched.
Table 2.
Teff, open-shutter fraction, and average slew time of minion 1016 and ALTSched.
ALTSched matches min-
ion 1016’s Teff despite higher slew times because we observe on the meridian, boosting SNR of each observation.
Figure 2. Number of visits as a function of alt/az (North is up, East is right, zenith is center, and the horizon is shown as a bold
line). minion 1016 exhibits an East bias, where observations are preferentially taken at high airmass in the East. ALTSched
stays close to the meridian except near azimuth, where LSST’s alt/az mount prevents observations directly on the meridian.
where Texp is the exposure time, and Treadout consists of any intermediate readout time between back-to-back “snaps”
during the same visit (the readout after the last snap is included in the slew time). Both minion 1016 and ALTSched
divide 30-second visits into 2 15-second snaps for cosmic-ray rejection.
Maximizing Teff is one motivation for ALTSched’s meridian-scanning strategy, since observing ﬁelds at their
minimum airmass yields the highest 5σ depth. Results for these three metrics are shown in Table 2. Despite achieving
a lower OSF and higher average slew time, ALTSched reaches approximately the same Teff as minion 1016,
since minion 1016 observes oﬀthe meridian, as shown in Figure 2. In particular, in LSST’s wide-fast-deep region,
minion 1016 achieves a mean (median) airmass of 1.22 (1.21) compared to ALTSched’s 1.12 (1.09). minion 1016’s
mean (median) normalized airmass – i.e. the airmass of an observation divided by the minimum airmass that ﬁeld
could have been observed at – is 1.16 (1.14) compared to 1.05 (1.01) for ALTSched. ALTSched suﬀers from a higher
slew time for three reasons: ﬁrst, because we change ﬁlters much more often than minion 1016 in order to obtain
same-night colors for nearly every visit; second, because our scanning strategy is simple and could be optimized for
faster slews; and third, because our sky tiling is spaced farther apart than the tiling used in OpSim.


## Page 7


7
0
50
100
150
200
250
300
350
400
l
10
1
100
101
102
103
104
l(l + 1)Cl/(2 )
minion_1016, no dither
minion_1016, random dithers
ALTSched
Figure 3. Angular power spectra of the number of visits to a sky pixel for a region of LSST’s wide-fast-deep region that
excludes any deep drilling ﬁelds and the galactic plane. Even after applying random dithers to OpSim’s ﬁxed ﬁelds, ALTSched
increases uniformity over minion 1016 at most angular scales.
Another important consideration for static science is that of survey uniformity. In particular, weak lensing and
large-scale structure measurements depend sensitively on the uniformity of co-added depth across the sky (Awan et al.
2016). OpSim uses a set of ﬁxed ﬁeld centers, and attempts to mitigate the resulting imprint on the co-added depth
maps by dithering around those ﬁeld centers. However, every dithering strategy tried thus far still leaves a discernible
imprint on the ﬁnal co-added depth maps. Instead of dithering, ALTSched eliminates ﬁxed ﬁelds entirely. We use
a ﬁxed tiling for the entire survey, but every night, we randomly rotate this tiling by much more than a ﬁeld size.
Pointings not visited in a night are scheduled in a subsequent night, so gaps in the tiling pattern do not persist. To
measure survey uniformity, we include angular power spectra of the number of visits to a sky pixel, shown in Figure
3. ALTSched’s tiling strategy reduces power at most angular scales, including around ℓ≈150, where cosmological
probes are particularly sensitive.
Unlike any strategy using ﬁxed ﬁelds with dithering, our method admits simple analysis that yields an expression
for the uniformity in number of visits to a sky pixel. For the ﬁxed tiling used throughout the survey, let Ω0,1,2 be the
areas of sky covered by 0, 1, and 2 pointings, respectively. Assume no sky pixels are observed more than twice, so the
total area covered by the tiling Ω= Ω0 + Ω1 + Ω2. Then the standard deviation of number of visits to a sky pixel
using our strategy – i.e. after applying the randomly-rotated tiling n times – is
σ =
v
u
u
tn
 
Ω1 + 4Ω2
Ω
−
Ω1 + 2Ω2
Ω
2!
.
See Appendix C for a brief derivation. Note that this expression does not depend on the tiling itself – only on the Ωi.
In order to minimize slew time while maintaining an even cadence, we choose a tiling with the ﬁelds evenly spaced and
with Ω2 ≈0. Even with Ω2 ≈0, we achieve some fast revisits due to pointings held over from previous nights, which
will overlap randomly with the current night’s pointings. To make the ﬁelds “evenly spaced”, we draw pointings from
a solution to the Thomson charge-distribution problem for N = 3500 Thomson (1904). See Figure 4 for a visualization
of our tiling. Adjusting N changes the density of the tiling, which controls the tradeoﬀbetween the frequency of rapid
revisits and the area observed per night.
4.2. Time-Domain Science
Optimizing time-domain science is much more about managing tradeoﬀs between diﬀerent science cases than max-
imizing certain quantities.
We argue in this section that 1) the parameters of ALTSched directly control these
tradeoﬀs, whereas in OpSim, the tradeoﬀs are diﬃcult or impossible to control, and 2) the ALTSched simulation
analyzed in this paper enables a wider range of science cases than minion 1016.


## Page 8


8
Figure 4. Tiling used by ALTSched projected using the Mollweide (equal-area) projection. Blue indicates no visits to that
sky pixel, green indicates a single visit, and red indicates two visits. Note that, since the tiling is randomly rotated each night,
the gaps in the tiling do not persist across nights.
Most existing simulations assume that LSST will carry out pairs of visits separated by ∼30 −60 minutes (to link
asteroid observations), and will take 30-second exposures during each visit. Some OpSim simulations have been run
to explore deviating from these assumptions, but here we take them as given. In this section, we explore how the
distribution of visits over time aﬀects time-domain science tradeoﬀs, and describe how these tradeoﬀs can be controlled
in ALTSched and OpSim.
One fundamental tradeoﬀin time-domain science is between the mean season length and the mean inter-night gap
(or mean cadence), which is the mean duration between consecutive visits to a sky pixel. Controlling this tradeoﬀwith
ALTSched is simple: instead of scanning along the meridian, the scheduler can start the night either East (shorter
season/higher mean cadence) or West (longer season/lower mean cadence) of the meridian, and slowly move West/East
over the course of the night. In contrast, there is no direct way to control this tradeoﬀwith a greedy scheduler like
OpSim. The simplest way would be to relax the airmass/hour angle penalty and hope that the scheduler makes full
use of the additional area it can use. However, this is exactly what minion 1016 does, and instead of increasing the
season length, it simply observes at a higher, but mostly ﬁxed, airmass (see Figure 2). Alternatively, one could adjust
the penalty on the hour angle throughout the night in order to persuade the scheduler to start observing in, say, the
East, and then move over to the West by the end of the night. This might achieve the desired result, but would require
tuning of weights just in order to reproduce the simple behavior already achieved by ALTSched.
In practice, we observe along the meridian throughout the night, since we don’t see an advantage in changing the
season length/mean cadence at the expense of lowering SNR by observing at higher airmass. Because minion 1016
observes at a wider hour angle range, and therefore has a slightly longer season length, one might worry that ALTSched
suﬀers in parallax performance. However, this is not the case, as shown in Figure 5.
Although the mean inter-night gap is largely determined by observing eﬃciency and the season length, as described
above, the actual distribution of inter-night gaps, measured with an inter-night gap histogram, is much more sensitive
to the scheduling algorithm. This metric, though often disregarded, has a large impact on the quality of the light-
curves LSST will measure. To get an intuitive sense for how the scheduling algorithm can aﬀect the inter-night gap
histogram, consider Figure 6, which shows, for a randomly chosen sky pixel, the cadences achieved by minion 1016
and ALTSched. Notice that minion 1016 often observes this pixel many times in quick succession, and then goes
many days without any re-observations. In contrast, ALTSched observes this pixel with a much more regular cadence.
This intuition is quantiﬁed with histograms of the gaps between consecutive visits to a sky pixel, shown in Figures 7
and 8.
Controlling the inter-night gap histogram with ALTSched is also simple. Changing the mean season length/mean
cadence as described above yields a simple scaling of the histogram in the x-axis. And the location of the peak can be
tuned either by changing the number of visits to a ﬁeld per night, or by employing a rolling cadence. Both options are
directly controllable in ALTSched. The sharpness of the peak can also be controlled, simply by judiciously choosing
which nights the telescope observes North vs. South. In the default version of ALTSched, the scheduler observes


## Page 9


9
Figure 5. Parallax precision for an r = 24 magnitude star (without refraction), using either minion 1016 (left) or ALTSched
(right). Lower is better.
59750
59800
59850
59900
59950
MJD
21.0
21.5
22.0
22.5
23.0
23.5
24.0
24.5
25.0
5-sigma depth
minion_1016: RA/Dec = 0.0 / -50.0 degrees
u
g
r
i
z
y
59750
59800
59850
59900
59950
MJD
21.0
21.5
22.0
22.5
23.0
23.5
24.0
24.5
25.0
25.5
5-sigma depth
ALTSched: RA/Dec = 0.0 / -50.0 degrees
u
g
r
i
z
y
Figure 6. 5σ depth vs time for an arbitrarily chosen RA/Dec for minion 1016 (left) and ALTSched (right). These plots are
typical for each scheduler for LSST’s wide-fast-deep region. The two plots have approximately the same number of visits (94
for minion 1016 vs. 97 for ALTSched), but ALTSched spreads the visits more uniformly over time.
1
2
3
4
5
6
7
8
9
Inter-Night Visit Gap (days)
0
50
100
150
200
250
Count
minion_1016: all bands
>9
minion_1016
1
2
3
4
5
6
7
8
9
Inter-Night Visit Gap (days)
0
50
100
150
200
250
Count
ALTSched: all bands
>9
ALTSched
Figure 7. Histogram of inter-night visit gaps to a sky pixel in minion 1016 and in ALTSched, for visits in any ﬁlter. The
mean inter-night gap is roughly conserved, since both schedulers have a similar total number of visits. But by alternating
between observing the northern and southern skies, ALTSched suppresses 1-night revisits, which signiﬁcantly reduces longer
gaps. The diﬀerence between the two schedulers is even more striking than these plots indicate, since most of the remaining
long gaps in ALTSched are attributable to downtime, weather, and season gaps.


## Page 10


10
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
minion_1016: u band
>19
minion_1016
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
ALTSched: u band
>19
ALTSched
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
minion_1016: r band
>19
minion_1016
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
ALTSched: r band
>19
ALTSched
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
minion_1016: z band
>19
minion_1016
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
ALTSched: z band
>19
ALTSched
Figure 8. Per-band inter-night visit gap histograms for minion 1016 and ALTSched, for the u, r, and z bands. Since both
ALTSched and minion 1016 defer u observations to dark time, we only see a small gain relative to minion 1016 in the u band.
Histograms for g, i, and y are similar, and are deferred to Appendix B.
North and South on alternating nights, yielding a sharp peak in the inter-night gap histogram at 2 days. However,
choosing a repeating sequence such as N N S N S S N S would yield a ﬂatter peak at 2 days, with half the histogram
mass at 2 days, and the other half distributed between 1 and 3 days. In contrast, every inter-night gap histogram
we have measured from an OpSim simulation (even for simulations released after minion 1016) has looked roughly
exponential. Note that an exponential distribution of inter-night gaps is consistent with an unconstrained stochastic
process about the mean. We infer from this that none of the tunable parameters in OpSim explored so far have a
discernible impact on the shape of the inter-night gap histogram.
Many science cases for LSST rely on approximately month-long transients (supernovae, kilonovae, tidal disruption
events, etc.). For these science cases, we expect that multi-week long gaps will severely reduce the quality of light
curves, without a commensurate increase in quality from the higher rate of sampling over small sections of the light
curve. This intuition is borne out in simulations, run by Nicolas Regnault, Philippe Gris, and the Paris Supernovae
Cosmology Team, of the number of well-sampled type Ia supernovae diﬀerent simulated schedules would obtain (per-
sonal communication). As shown in Table 3, ALTSched achieves an eightfold increase in the number of well-sampled
SNeIa, and also an increase of 0.07 in the maximum redshift at which the type-Ia supernova sample is complete.
Although these simulations are for SNeIa in particular, we expect similar results to hold for other transients. For ex-
ample, Cowperthwaite et al. (2019) ﬁnd that ALTSched achieves a nearly 2x increase in the number of serendipitous


## Page 11


11
NSNe
Avg. zmax
minion 1016
47,000
0.30
ALTSched
366,000
0.37
Table 3. Results from simulations run by Nicolas Regnault, Philippe Gris, and the Paris Supernova Cosmology Team (personal
communication). NSNe is the number of well-sampled type-Ia supernovae (SNeIa) in the redshift-limited sample. Here, a SN
is well-sampled if the light curve has (considering only griz observations): 1) ≥1 visit every 4 days; 2) > 1 visit in [-20, -10]
days (restframe); 3) > 1 visit in [+35, +45] days (restframe); and 4) σcolor < 0.04. zmax is the maximum redshift at which the
sample of SNeIa is complete, and the average in “Avg. zmax” is taken over sky pixels.
Figure 9. Histogram of the fraction of nights in which a sky pixel was visited in at least two diﬀerent bands. Only nights when
two or more exposures were achieved at a sky pixel are included in the calculation. By observing nearly all ﬁelds in two bands
instead of only one in a given night, ALTSched doubles the observing cadence in each band.
kilonovae discoveries compared to minion 1016. Similarly, Goldstein et al. (2018) ﬁnd that ALTSched discovers
lensed supernovae earlier than minion 1016, enabling faster spectroscopic follow-up.
ALTSched achieves more favorable inter-night gap histograms than minion 1016 for two main reasons. The band-
agnostic gaps (Figure 7) are improved because ALTSched alternates between observing the northern and southern
skies each night, suppressing 1-day revisit gaps. Because the mean cadence is approximately conserved across schedulers
with similar numbers of total visits, this by necessity eliminates most of the long gaps, which are so detrimental for
transient characterization. The per-band gaps (Figure 8) are improved since we carry out the two visits each sky pixel
receives per night in diﬀerent ﬁlters, doubling the cadence in each band (see Figure 9).
Although in this paper we advocate looking at the entire inter-night gap histogram, it is more common within LSST
scheduling to present histograms of the median inter-night gap. We present these histograms in Appendix A.
So far, we have considered only the inter-night gaps between visits.
However, the histogram of gaps between
observations to a sky pixel within a given night is also an important metric. In order to sample transients at a large
range of time-scales, both ALTSched and minion 1016 revisit each ﬁeld after 30 −60 minutes. In addition, both
schedulers carry out some number of “rapid revisits,” which are spaced less than a minute apart. minion 1016 carries
out more rapid revisits than ALTSched, and the frequency can be adjusted in either scheduler by changing the ﬁeld
tiling density: a tiling with more overlaps between adjacent pointings yields more ~30-second revisits. We therefore
omit further analysis of rapid revisits.
5. SCHEDULERS USED FOR OTHER SKY SURVEY PROJECTS
The scheduling principles we describe in this paper apply to any ground-based telescope able to image a large sky
area per unit time. Such telescopes include LSST (Ivezic et al. 2008), Palomar Transient Factory (PTF) (Rau et al.
2009), Zwicky Transient Facility (ZTF) (Smith et al. 2014), Pan-STARRS1 (Chambers et al. 2016), SkyMapper (Keller
et al. 2007), the Dark Energy Survey (DES) (The Dark Energy Survey Collaboration 2005), and others. Scheduling
software has been developed for each of these telescopes, but often only limited information about these schedulers
can be found in the literature. Broadly speaking, most schedulers are greedy algorithms like OpSim: they choose each


## Page 12


12
observation as the night progresses based on where the telescope is currently pointing and on current or predicted
observing conditions. In general, greedy algorithms are guaranteed to maximize merit in the long term in only the
simplest of problems, and telescope scheduling is not one of those problems. To see why, consider a scenario where
every ﬁeld north of the telescope has a merit score of, say, 5, and every ﬁeld south of the telescope has a merit score of
4. Fields directly overhead have very low merit. If the telescope happens to be pointing in the South and long slews
are penalized, then a greedy algorithm will call for observing in the South the entire night, even though the globally
optimal policy would be to slew to the North at the very beginning and observe there for the rest of the night.
The schedulers used for PTF (Law et al. 2009), PanSTARRS1 (Chambers & Denneau 2008), and, as we understand
it, DES (Neilsen & Annis 2013), are all greedy algorithms. Similarly to LSST, these surveys include a wide-area
component which receives multiple epochs in several bands, and we suspect that the challenges in time-domain science
faced by greedy algorithms for LSST apply to these surveys as well. ZTF uses a diﬀerent scheduling algorithm, which
schedules an entire night at a time by solving an integer program designed to maximize observing eﬃciency, subject
to constraints on when and how often each ﬁeld needs to be observed (Bellm et al. 2019). Las Cumbres Observatory
uses a similar algorithm (Saunders & Lampoudi 2014). For LSST, this approach is challenging for a few reasons: the
overhead for each observation varies considerably (a few seconds to 2 minutes); in order to achieve a more uniform sky
coverage, LSST may not use ﬁxed ﬁelds at all; and the large number of ﬁelds and observations per night may render
the integer program intractable to solve repeatedly during a night when weather changes.
6. CONCLUSIONS, AND FUTURE DIRECTIONS
As we have described in this article, ALTSched gives survey designers much more control over global survey
characteristics than a greedy algorithm. However, certain limitations caused by our algorithm’s simplicity leave room
for improvement in the more local scheduling decisions: ALTSched does not avoid taking exposures near the moon; it
does not avoid poor seeing conditions or clouds; and it makes slews that are longer than necessary. These problems are
not insurmountable, and because they strictly worsen ALTSched’s performance on metrics, we view these limitations
optimistically as opportunities to extract even more science performance from LSST.
Between now and the beginning of full operations, the LSST Project plans to ﬁnd an optimal survey strategy by
running a large number of OpSim simulations, and to choose whichever yields the best compromise between science
cases. We want to stress that the best survey strategy that can be found with this procedure is likely to under-perform
on a number of time-domain metrics, since the parameters of OpSim don’t give much control over the survey’s cadence.
Instead, we advocate for combining the advantages of ALTSched (global schedule characteristics) with those of
OpSim (sensible local scheduling decisions). We see two ways to combine forces. The simplest is to simulate surveys
that switch back and forth between the two algorithms. When ALTSched tries to observe the moon, switch to a
greedy algorithm that knows not to; at the end of every month, spend a day or two using a greedy algorithm to
even up co-added depth across the sky; when clouds are present, use the greedy algorithm exclusively. Strategies like
these should have minimal impact on the favorable properties of ALTSched, while also largely rectifying some of its
limitations. Another way forward is to combine the two algorithms directly, by using a greedy scheduler whose merit
function has been speciﬁcally engineered to reproduce ALTSched for large-scale decisions (which region of the sky to
observe; which ﬁlter to use), but where more local scheduling decisions can be made by lower-order terms in the merit
function.
In parallel, we encourage the LSST science community to continue using ALTSched as a tool to demonstrate
the minimum performance that LSST is capable of.
We developed most of ALTSched over a few months, and
many opportunities for improvement remain: ﬁnding a scanning pattern that minimizes slew times; making more
intelligent ﬁlter choices; adapting throughout the night to avoid deviating from the meridian; recovering more gracefully
from downtime; using separate tilings per-ﬁlter to increase homogeneity; etc. Making improvements like these, and
combining ALTSched with OpSim as described above, is what we believe will ﬁnd the best survey strategy available
in the limited time remaining before full operations commence.
We are thankful to numerous members of the LSST Project team for extensive conversations about scheduling
choices and system characteristics. Stubbs and Rothchild acknowledge support from the US Department of Energy
under grant DE-SC0007881, and from Harvard University. Yoachim acknowledges funding from the LSST Corporation.


## Page 13


13
Software: astropy(Robitailleetal.2013),MetricsAnalysisFramework(Jonesetal.2014)


## Page 14


14
REFERENCES
Awan, H., Gawiser, E., Kurczynski, P., et al. 2016, The
Astrophysical Journal, 829, 50. https:
//doi.org/10.3847%2F0004-637x%2F829%2F1%2F50
Bellm, E., Kulkarni, S., & Graham, M. 2019, in American
Astronomical Society Meeting Abstracts, Vol. 233,
American Astronomical Society Meeting Abstracts #233,
#363.08
Chambers, K. C., & Denneau, L. J. 2008, PS1 Design
Reference Mission, doi:10.5281/zenodo.199860.
https://doi.org/10.5281/zenodo.199860
Chambers, K. C., Magnier, E. A., Metcalfe, N., et al. 2016,
ArXiv e-prints, arXiv:1612.05560
Cowperthwaite, P. S., Villar, V. A., Scolnic, D. M., &
Berger, E. 2019, The Astrophysical Journal, 874, 88.
https://doi.org/10.3847%2F1538-4357%2Fab07b6
Delgado, F., & Reuter, M. A. 2016, in Observatory
Operations: Strategies, Processes, and Systems VI, Vol.
9910, International Society for Optics and Photonics,
991013
Delgado, F., Saha, A., Chandrasekharan, S., et al. 2014, in
Modeling, Systems Engineering, and Project
Management for Astronomy VI, Vol. 9150, International
Society for Optics and Photonics, 915015
Goldstein, D. A., Nugent, P. E., & Goobar, A. 2018, arXiv
preprint arXiv:1809.10147
Ivezic, Z., Tyson, J. A., Abel, B., et al. 2008, ArXiv
e-prints, arXiv:0805.2366
Jones, R. L., Yoachim, P., Chandrasekharan, S., et al. 2014,
in Observatory Operations: Strategies, Processes, and
Systems V, Vol. 9149, International Society for Optics
and Photonics, 91490B
Keller, S. C., Schmidt, B. P., Bessell, M. S., et al. 2007,
PASA, 24, 1
Law, N. M., Kulkarni, S. R., Dekany, R. G., et al. 2009,
Publications of the Astronomical Society of the Paciﬁc,
121, 1395
LSST Science Collaborations, Marshall, P., Anguita, T.,
et al. 2017, ArXiv e-prints, arXiv:1708.04058.
https://doi.org/10.5281/zenodo.842712
Naghib, E., Vanderbei, R. J., & Stubbs, C. 2016, in
Proc. SPIE, Vol. 9910, Observatory Operations:
Strategies, Processes, and Systems VI, 991011
Neilsen, E., & Annis, J. 2013, ObsTac: automated
execution of Dark Energy Survey observing tactics.,
Tech. rep., Fermi National Accelerator Lab.(FNAL),
Batavia, IL (United States)
Rau, A., Kulkarni, S. R., Law, N. M., et al. 2009, PASP,
121, 1334
Ridgway, S. T. 2015, An Optimized Cadence for LSST: The
Optimum Unit Method, Tech. Rep. 17818, LSST
Robitaille, T. P., Tollerud, E. J., Greenﬁeld, P., et al. 2013,
Astronomy & Astrophysics, 558, A33
Saunders, E., & Lampoudi, S. 2014, in The Third
Hot-wiring the Transient Universe Workshop, ed. P. R.
Wozniak, M. J. Graham, A. A. Mahabal, & R. Seaman,
117–123
Smith, R. M., Dekany, R. G., Bebek, C., et al. 2014, in
Proc. SPIE, Vol. 9147, Ground-based and Airborne
Instrumentation for Astronomy V, 914779
The Dark Energy Survey Collaboration. 2005, ArXiv
Astrophysics e-prints, astro-ph/0510346
Thomson, J. J. 1904, The London, Edinburgh, and Dublin
Philosophical Magazine and Journal of Science, 7, 237


## Page 15


15
Appendices
A. MEDIAN INTER-NIGHT GAPS
Here we present histograms of the median inter-night gap between consecutive visits to a sky pixel.
Because
minion 1016 and ALTSched have a similar total number of visits available per unit area, the mean (and therefore,
roughly speaking, the median) inter-night gap should be ﬁxed (Figure 10). We expect a two-fold reduction in the
per-band median inter-night gaps (Figures 11 & 12) because ALTSched observes each ﬁeld in two ﬁlters per night
instead of minion 1016’s single ﬁlter.
We see additional improvement beyond these predictions because minion 1016 sometimes observes the same ﬁeld
more than twice per night, thus incurring additional long inter-night gaps. minion 1016 also has a slightly longer
season length since it observes at a wider range of airmasses. For the u band, the improvement is actually less than
twofold because both ALTSched and minion 1016 cluster observations in the u band around times with low lunar
brightness.
Figure 10. Histogram of median inter-night visit gaps to a sky pixel in minion 1016 and in ALTSched, for visits in any ﬁlter.
minion 1016 has slightly longer observing gaps because it eﬀectively has a longer season duration and because it observes some
ﬁelds more than twice per night.
B. INTER-NIGHT GAPS
In Figure 13, we include histograms of the typical inter-night gap between observations to a sky pixel in the g, i,
and y bands (deferred from the text).
C. UNIFORMITY DERIVATION
Consider a survey that observes only at pointings drawn from some ﬁxed sky tiling. Let the area not covered by any
pointing be Ω0, the area covered by exactly one pointing be Ω1, and the area covered by exactly two pointings be Ω2.
Assume no part of the sky is covered by three or more ﬁelds – i.e. that the total sky area Ω= Ω0 + Ω1 + Ω2. If this
tiling is observed once, the mean number of times a sky pixel will be observed is
µf = Ω1 + 2Ω2
Ω
and the RMS ﬂuctuation in number of visits to a pixel is
σf =
r
1
Ω(Ω0(µf)2 + Ω1(1 −µf)2 + Ω2(2 −µf)2)
=
s
Ω1 + 4Ω2
Ω
−
Ω1 + 2Ω2
Ω
2
.


## Page 16


16
Figure 11. Per-band median inter-night visit gaps for minion 1016 and ALTSched, for the u, g, and r bands. ALTSched
achieves considerably better median gaps, primarily because it executes pairs of observations taken in a single night in diﬀerent
ﬁlters, eﬀectively doubling the per-band cadence in each band.
If the tiling is observed N times without rotation or dithering, the ﬁnal average and standard deviation in number
of visits will be Nµf and Nσf.
To reduce the standard deviation, we can simply rotate the tiling by some random amount each time it is observed.
If we do this N times, then by the central limit theorem, the probability distribution of number of visits to each sky
pixel is normal with mean
µr = Nµf = N
Ω1 + 2Ω2
Ω



## Page 17


17
Figure 12. Same as Figure 11, but for the i, z, and y bands.
and standard deviation
σr = N σf
√
N
= σf
√
N =
v
u
u
tN
 
Ω1 + 4Ω2
Ω
−
Ω1 + 2Ω2
Ω
2!
.


## Page 18


18
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
minion_1016: g band
>19
minion_1016
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
ALTSched: g band
>19
ALTSched
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
minion_1016: i band
>19
minion_1016
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
ALTSched: i band
>19
ALTSched
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
minion_1016: y band
>19
minion_1016
2
4
6
8
10
12
14
16
18
Inter-Night Visit Gap (days)
0
10
20
30
40
50
60
Count
ALTSched: y band
>19
ALTSched
Figure 13. Per-band inter-night visit gap histograms for minion 1016 and ALTSched, for the g, i, and y bands.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]