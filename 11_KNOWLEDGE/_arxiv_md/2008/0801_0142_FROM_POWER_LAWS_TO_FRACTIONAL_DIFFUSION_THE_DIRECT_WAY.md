---
canon-group: reference
rscf-state: source-claim
arxiv_id: 801.0142
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0801.0142_From_Power_Laws_to_Fractional_Diffusion__the_Direct_Way

> Source: 0801.0142_From_Power_Laws_to_Fractional_Diffusion__the_Direct_Way.pdf

> Pages: 12

---


## Page 1


arXiv:0801.0142v1  [math.PR]  30 Dec 2007
FRACALMO PRE-PRINT www.fracalmo.org
Paper published in
Vietnam Journal of Mathematics, Vol. 32 (SI), 65-75 (2004)
From Power Laws to Fractional Diﬀusion:
the Direct Way
Rudolf GORENFLO(1) and Entsar A.A ABDEL-REHIM (2)
(1) Fachbereich Mathematik & Informatik
Erstes Mathematisches Institut, Freie Universit¨at Berlin,
Arnimallee 3, D-14195 Berlin, Germany
E-mail: gorenflo@mi.fu-berlin.de
(2) On leave from Department of Mathematics and Computer Science,
Faculty of Science, Suez Canal University, Egypt
Abstract
Starting from the model of continuous time random walk (Montroll
and Weiss 1965) that can also be considered as a compound renewal pro-
cess we focus our interest on random walks in which the probability dis-
tributions of the waiting times and jumps have fat tails characterized by
power laws with exponent between 0 and 1 for the waiting times, between
0 and 2 for the jumps. By stating the relevant lemmata (of Tauber type)
for the distribution functions we need not distinguish between continuous
and discrete space and time. We will see that by a well-scaled passage
to the diﬀusion limit diﬀusion processes fractional in time as well as in
space are obtained. The corresponding equation of evolution is a linear
partial pseudo-diﬀerential equation with fractional derivatives in time and
in space, the orders being equal to the above exponents. Such processes
are enjoying increasing popularity in applications in physics, chemistry,
ﬁnance and other ﬁelds, and their behaviour can be well approximated
and visualized by simulation via various types of random walks. For their
explicit solutions there are available integral representations that allow to
investigate their detailed structure. For ease of presentation we restrict
attention to the spatially one-dimensional symmetric situation.
MSC 2000: 26A33, 33E12, 45E10, 45K05, 60F05, 60G50, 60J60
Keywords: continuous time random walks, asymptotics of Fourier and
Laplace transforms, convergence in law, well-scaled passage to the diﬀu-
sion limit, Mittag-Leﬄer function.
1


## Page 2


1
Introduction: concepts and notations
We consider spatially one-dimensional random walks of the following basic struc-
ture.
A particle (or a wanderer) starting at the time instant t = 0 at the
space point x = 0 makes jumps of random size Xk in random instants tk,
k ∈N = {1, 2, 3, · · ·}, 0 < t1 < t2 · · · →∞. For convenience we set t0 = 0.
Then in the time interval tn ≤t < tn+1 the particle is sitting in the point
x = Sn :=
nP
k=1
Xk. We assume the jumps to be independent identically dis-
tributed (iid) random variables, all having the same probability distribution as
a generic real random variable X , called the jump. Likewise we assume the
waiting times Tk := tk−tk−1 to be iid random variables, all equal in distribution
to a generic non-negative random variable T , called the waiting time. So, this
process is what in mathematical literature is called a compound (or cumulative)
renewal process [5]. We denote the distribution functions of the waiting time T
and the jump X by Φ and W, respectively, by
P(T ≤t) = Φ(t) , 0 ≤t < ∞; P(X ≤x) = W(x) , −∞< x < ∞.
Conveniently using the language of generalized functions in the sense of [8] or
[30] we introduce the (generalized) probability densities φ and w, so that
Φ(t) =
t
Z
0
φ(t′)dt′ , 0 ≤t < ∞; W(x) =
x
Z
−∞
w(x′)dx′ , −∞< x < ∞.
Denoting for time instant t the probability density to ﬁnd the particle in point
x by p(x, t) we then have, by conditioning on the last jump before t and using
the delta function δ(x), for 0 ≤t < ∞and −∞< x < ∞the integral equation
(see [24]) of continuous time random walk
p(x, t) = δ(x)(1 −Φ(t)) +
t
Z
0
{
∞
Z
−∞
w(x −x′)p(x′, t′)dx′} φ(t −t′)dt′ .
(1.1)
For the cumulative function P(x, t) =
xR
−∞
p(x′, t) dx′ we have, with the Heaviside
step function H(x), the equation
P(x, t) = H(x)(1 −Φ(t)) +
t
Z
0
{
∞
Z
−∞
W(x −x′)dP(x′, t′)} dΦ(t −t′) .
(1.2)
To proceed further we use the machinery of the transforms of Laplace and
Fourier. The general formulas for s ≥0, −∞< κ < ∞are
eg(s) =
∞
Z
0
e−stg(t)dt =
∞
Z
0
e−stdG(t) ; bf(κ) =
∞
Z
−∞
eiκxf(x)dx =
∞
Z
−∞
eiκxdF(x) .
2


## Page 3


Essentially applying these formulas to probability densities with 0 ≤t < ∞and
−∞< x < ∞we can safely take the Laplace variable s as real and non-negative.
Furthermore we will work with convolutions of (generalized) functions, namely
with the Laplace convolution and the Fourier convolution:
(g1 ∗g2)(t) =
∞
Z
0
g1(t′)g2(t −t′)dt′ ; (f1 ∗f2)(x) =
∞
Z
−∞
f1(x′)f2(x −x′)dx′ .
Then, applying the transforms of Fourier and Laplace in succession to the equa-
tion (1.1) and using the well-known operational rules, we arrive at the relation
bep(κ, s) = 1 −eφ(s)
s
+ eφ(s) bw(κ)bep(κ, s) ,
(1.3)
which leads to the famous Montroll-Weiss equation, see [24],
bep(κ, s) = 1 −˜φ(s)
s
1
1 −bw(κ)˜φ(s)
.
(1.4)
This equation can alternatively be derived from the Cox formula, see [5] chapter
8 formula (4), describing the process as subordination of a random walk to a
renewal process. By inverting the transforms one can, in principle, ﬁnd the
evolution p(x, t) of the sojourn density for time t running from zero to inﬁnity.
Our aim is to show that under appropriate assumptions of power laws for the
distribution functions Φ(t), t ≥0, and W(x), −∞< x < ∞, under observance
of a scaling relation between the positive parameters h and τ the re-scaled
random walk Sn(h) =
nP
k=1
hXk happening at the instants tn(τ) =
nP
k=1
τTk (with
S0(h) = 0, t0(τ) = 0 ) weakly (or in law) tends, for h and τ tending to zero,
to a process obeying the space-time fractional diﬀusion equation. Speciﬁcally,
we will show that the sojourn probability density ph,τ(x, t) tends weakly to the
solution u(x, t) of the Cauchy problem for t > 0 and x ∈R
D
t ∗
β u(x, t) = Rα u(x, t) , u(x, 0) = δ(x) .
(1.5)
Here 0 < α ≤2, 0 < β ≤1. The fractional Riesz derivative Rα (in space) is
deﬁned as follows: the Fourier transform of Rαf(x) is −|κ|α bf(κ) for a suﬃciently
well-behaved function f(x).
Compare [6], [25], [26].
The Caputo fractional
derivative (in time) can be deﬁned through its image in the Laplace transform
domain.
The Laplace transform of D
t ∗
β g(t) is sβeg(s) −sβ−1g(0).
We have
D
t ∗
β g(t) = dg(t)
dt
for β = 1 but
D
t ∗
β g(t) =
1
Γ(1 −β){ d
dt
t
Z
0
(t −t′)−βg(t′)dt′ −t−βg(0)} for 0 < β < 1 ,
3


## Page 4


compare [10]. In the Fourier-Laplace domain the Cauchy problem (1.5) appears
in the form sβbeu(κ, s) −sβ−1 = −|κ|αbeu(κ, s) from which we obtain
beu(κ, s) =
sβ−1
sβ + |κ|α , s > 0 , κ ∈R .
(1.6)
Let us refer to [18] for the analytical theory of representing the function
u(x, t) , namely the fundamental solution of the space-time fractional diﬀusion
equation, in dependence on the parameters α and β.
To carry out the passage to the diﬀusion limit we state in Section 2 two MAS-
TER LEMMATA and four simpliﬁcations relating the asymptotic behaviours of
the distribution functions W(x) and Φ(t) near inﬁnity to the asymptotic be-
haviour of their Laplace and Fourier transforms near zero. Section 3 is devoted
to the actual passage to the diﬀusion limit, in Section 4 some examples are
presented, and a few historical comments are given in Section 5.
2
Six lemmata
Deﬁnition: As in [3] we call a positive measurable function ν, deﬁned on some
neighbourhood [x∗, ∞) of inﬁnity , slowly varying if ν(ax)/ν(x) →1 as x →∞
for every a > 0. Examples: (logx)γ with γ ∈R and exp (
logx
loglogx).
MASTER LEMMA 1: Assume W(x) increasing, W(−∞) = 0, W(∞) = 1,
symmetry
R
(−∞,−x)
dW(x′) =
R
(x,∞)
dW(x′) for x ≥0, let L be a slowly varying
function and assume either (a) or (b).
(a) σ2 :=
∞
R
−∞
x2dW(x) < ∞, labelled as α = 2 ,
(b)
R
(x,∞)
dW(x) ∼bα−1x−αL(x) for x →∞, α ∈(0, 2) and b > 0.
Then, with
µ = σ2
2 and L(x) ≡1 in case (a), µ =
bπ
Γ(α + 1)sin(απ/2) in case (b) , (2.1)
we have the asymptotics 1 −bw(κ) ∼µ|κ|αL(|κ|−1) for κ →0.
Comments The proof can be distilled from Chapter 8 of [3]. In some sense
this lemma is a partial reformulation (with a constant corrected) of Gnedenko’s
theorem on the domain of attraction of stable probability laws, see [9].
MASTER LEMMA 2: Assume Φ(t) increasing, Φ(0) = 0, Φ(∞) = 1, let
M be a slowly varying function and assume either (A) or (B).
(A) ρ :=
∞
R
0
tdΦ(t) < ∞, labelled as β = 1,
(B)
R
(t,∞)
dΦ(t) ∼cβ−1t−βM(t) for t →∞, β ∈(0, 1) and c > 0.
4


## Page 5


Then, with
λ = ρ and M(t) ≡1 in case (A), λ = cΓ(1 −β)
β
in case (B) ,
(2.2)
we have the asymptotics 1 −eφ(s) ∼λsβM(s−1) for 0 < s →0.
Comments This lemma is a special case of Karamata’s theorem of 1931. A
proof can be found in the book [3]. In the case of existing non-generalized func-
tions as densities the Master Lemmata imply the two following (convenient)
C-Lemmata (by integration it can be shown that the assumptions of the Master
Lemmata are met). See [12]. For the fully equidistant discrete case the two
D-Lemmata are useful. See [15].
C-Lemma 1 (for jump densities): Assume w(x) ≥0, w(x) = w(−x) for x ∈R,
∞
R
−∞
w(x)dx = 1 and either (a) or (b).
(a) σ2 :=
∞
R
−∞
x2w(x)dx < ∞, labelled as α = 2,
(b) w(x) ∼b|x|−(α+1) for |x| →∞, α ∈(0, 2) and b > 0.
Then with µ as in (2.1), we have the asymptotics
1 −bw(κ) ∼µ|κ|α for κ →0 .
(2.3)
C-Lemma 2 (for waiting time densities): Assume φ(t) ≥0 for t > 0,
∞
R
0
φ(t)dt =
1, and either (A) or (B).
(A) ρ :=
∞
R
0
tφ(t)dt < ∞, labelled as β = 1,
(B) φ(t) ∼ct−(β+1) for t →∞, β ∈(0, 1) and c > 0.
Then with λ as in (2.2), we have the asymptotics
1 −eφ(s) ∼λsβ .
(2.4)
D-Lemma 1:
Assume pk ≥0,
∞
P
−∞
pk = 1, symmetry pk = p−k for all integers
k ∈Z, and either (a) or (b).
(a) σ2 :=
∞
P
−∞
k2pk < ∞, labelled as α = 2,
(b) pk ∼b|k|−(α+1) for |k| →∞, α ∈(0, 2) and b > 0.
Then with µ as in (2.1) we have the asymptotics (2.3).
D-Lemma 2: Assume cn ≥0,
∞
P
n=1
cn = 1 and either (A) or (B).
(A) ρ :=
∞
P
1
ncn < ∞, labelled as β = 1,
(B) cn ∼cn−(β+1) for n →∞, β ∈(0, 1) and c > 0.
Then with λ as in (2.2) we have the asymptotics (2.4).
5


## Page 6


3
Well-scaled passage to the diﬀusion limit
As already indicated in the Introduction, we multiply the jumps Xk by a factor
h, the waiting times Tk by a factor τ. So, we get a transformed random walk
Sn(h) =
nP
k=1
hXk with jump instants tn(τ) =
nP
k=1
τTk that we now investigate
with the aim of passing to the limit h →0, τ →0 under a scaling relation
between h and τ yet to be established, assuming that the conditions of Master
Lemma 1 and Master Lemma 2 are fulﬁlled. As it is convenient to work in the
Fourier-Laplace domain we note that the density φτ(t) of the reduced waiting
times τTk and the density wh(x) of the reduced jumps hXk are φτ(t) = φ(t/τ)/τ,
t ≥0 ; wh(x) = w(x/h)/h, −∞< x < ∞.
The corresponding transforms
are simply f
φτ(s) = eφ(sτ), c
wh(κ) = bw(κh). We are interested in the sojourn
probability density ph,τ(x, t) of the particle subject to the transformed random
walk. In analogy to the Montroll-Weiss equation (1.4) we get
beph,τ(κ, s) = 1 −eφτ(s)
s
1
1 −bwh(κ)eφτ(s)
= 1 −eφ(τs)
s
1
1 −bw(hκ)eφ(sτ)
.
(3.1)
Considering now s and κ ﬁxed and ̸= 0 we ﬁnd for h →0, τ →0 from the
Master Lemmata (replacing there κ by κh, s by sτ ) by a trivial calculation,
omitting asymptotically negligible terms and using the slow variation property
L(1/(κh)) ∼L(1/h), M(1/(sτ)) ∼M(1/τ), the asymptotics (3.2) with (3.3).
beph,τ(κ, s) =
λτ βsβ−1M(1/τ)
µ(h|κ|)αL(1/h) + λ(τs)βM(1/τ) =
sβ−1
r(h, τ)|κ|α + sβ ,
(3.2)
r(h, τ) = µhαL(1/h)
λτ βM(1/τ) .
(3.3)
So we see that for every ﬁxed real κ ̸= 0 and positive s
beph,τ(κ, s) →
sβ−1
|κ|α + sβ = beu(κ, s) ,
(3.4)
as h and τ tend to zero under the scaling relation r(h, τ) ≡1. Comparing with
(1.6) we recognize here beu(κ, s) as the combined Fourier-Laplace transform of the
solution to the Cauchy problem (1.5). Invoking now the continuity theorems
of probability theory (compare [7]) we see that the time-parameterized sojourn
probability density converges weakly (or in law) to the solution of the Cauchy
problem (1.5). We state this result at the following theorem.
Theorem: Assume the probability laws for the jumps Xk and the waiting
times Tk to fulﬁll the conditions of the Master Lemmata 1 and 2, respectively.
Replace the jumps by hXk, the waiting times τTk. Then for h (and consequently
τ) tending to zero the solution ph,τ(x, t) of the rescaled integral equation (1.1)
(the densities there to be decorated with indices h and τ) converges weakly to
the solution of the Cauchy problem (1.5), in other words: to the fundamental
solution of the space-time fractional diﬀusion equation D
t ∗
β u(x, t) = Rα u(x, t).
6


## Page 7


4
Examples of random walks
Let us ﬁrst consider the space-time fractional diﬀusion equation more closely
with regard to special choices of the parameters α and β. In the very particular
case α = 2, β = 1 it reduces to the classical diﬀusion equation ∂u
∂t = ∂2u
∂x2 . In
the case α = 2, 0 < β < 1 we have the time-fractional diﬀusion equation inves-
tigated in 1989 [28]. In the case 0 < α < 2, β = 1 we have the space-fractional
diﬀusion equation for which the fundamental solution is a symmetric strictly sta-
ble probability density evolving in time. Whereas the time-fractional case α = 2,
0 < β < 1 exhibits subdiﬀusive behaviour, we have superdiﬀusive behaviour, if
0 < α < 2. All this can be deduced from the Fourier-Laplace representation
(1.6) by observing that the variance ⟨(x(t))2⟩= (σ(t))2 =
∞
R
−∞
x2u(x, t)dx of
the position x(t) of a diﬀusing particle is given as −∂2
∂κ2 bu(κ, t)|κ=0. Using the
Mittag-Leﬄer function Eβ(z) =
∞
P
n=0
zn
Γ(1+nβ) (see [10]) we ﬁnd by Laplace inver-
sion the convergent series bu(κ, t) = Eβ(−|κ|αtβ) = 1 −|κ|αtβ
Γ(1+β) + |κ|2αt2β
Γ(1+2β) −+ · · ·
from which for t > 0 we get (σ(t))2 =
2tβ
Γ(1+β) if α = 2, (σ(t))2 = ∞if 0 < α < 2.
Now we present two concrete random walk models, for both assuming 0 <
α < 2, 0 < β < 1. The ﬁrst example is in continuous time and continuous
space. From [4] we got the idea that it is advantageous to work with functions
W(x) and Φ(t) that can elementary be inverted. This is useful to produce from
[0, 1)-uniformly distributed pseudo-random numbers the jumps and the waiting
times in simulations. We take, compare [11] and [20],
W(x) = 1
2 + 1
2(−1)sign(x)
|x|α
1 + |x|α , Φ(t) = 1 −
1
1 + Γ(1 −β)tβ .
Then we have case (b) of MASTER LEMMA 1 with b = α/2 and L(x) ≡1, and
case (B) of MASTER LEMMA 2 with c = 1/|Γ(−β)|, M(t) ≡1.
In the second example time and space are equidistantly discretized. We take
p0 = 0, pk = b|k|−(α+1) for 0 ̸= k ∈Z, cn = cn−(β+1) for n ∈N, and set
w(x) =
∞
P
−∞
pkδ(x −k), φ(t) =
∞
P
k=1
ckδ(t −k) (compare with[15]). We have case
(b) of D-Lemma 1, case (B) of D-Lemma 2 and identify readily (with ζ(z) de-
noting Riemann’s zeta function) b =
1
2ζ(α+1) and c =
1
ζ(β+1). The sequences
p1, p2, p3, · · · and c1, c2, c3, · · · have the nice property of being completely mono-
tone. The excluded border cases α = 2 and β = 1 are singular.
To convey to the reader a feeling for fractional diﬀusion we present a few
graphical results of approximating random walks, simulated according to the
ﬁrst example.
They show in sequence the case of Brownian motion (classi-
cal diﬀusion), time-fractional diﬀusion, space-fractional diﬀusion, space-time-
fractional diﬀusion.
Note that for α = 2, we use the jump density w(x) =
1
√
2π exp(−x2
2 ), for
β = 1 the waiting time density φ(t) = exp(−t). For 0 < α < 2 and 0 < β < 1
7


## Page 8


we take the jump distribution W(x) and the waiting time distribution Φ(t),
both as in the ﬁrst example.
Observe some long waiting times in the case 0 < β < 1 and some long jumps
in the case 0 < α < 2.
0
200
400
600
800
1000
T
0
5
10
15
20
25
30
X
a=2,b=1
Figure 1: normal diﬀusion
0
50
100
150
200
250
300
T
-100
-80
-60
-40
-20
0
X
a=2,b=0.75
Figure 2: time-fractional
0
2000
4000
6000
8000
10000
T
-1500
-1000
-500
0
500
1000
1500
X
a=1.25,b=1
Figure 3: space-fractional
0
25
50
75
100
125
150
T
-1250
-1000
-750
-500
-250
0
250
500
X
a=1.5,b=.75
Figure 4: space-time frac-
tional
8


## Page 9


5
Comments, suggestions and conclusions
The theory of compound renewal processes, also called renewal processes with
reward, in physics and other natural sciences called continuous time random
walks (though space and time need not be continuous) began to ﬂourish in
the middle of the sixties of the past century, let us quote [24] and [5].
We
cannot give here a comprehensive survey of relevant literature, so we ask all not
mentioned contributors to forgive us this surely biased account. For larger lists
of references and more competent appreciation of achievements and applications
we recommend [2] and [23]. As an early pioneer Balakrishnan [1] deserves to
be put into light. He has, in 1985, found the time-fractional diﬀusion equation
(α = 2 , 0 < β < 1) as the properly scaled diﬀusion limit for some random
walks with power law waiting time.
At that time, four years before in [28]
the basic analytic theory was developed, the name fractional diﬀusion was not
yet common, and so was not used in [1], hence Balakrishnan did not ﬁnd the
resonance he would have deserved. A decisive step forward occurred in [17] in
1995. Hilfer and Anton, roughly speaking, showed among other things that by
taking the Mittag-Leﬄer waiting time density −d
dtEβ(−tβ) the basic equation of
continuous time random walk can be transformed to a time-fractional evolution
equation for the sojourn probability density. Thus they have essentially found
the time-fractional generalization of the Kolmogorov-Feller evolution equation
for the compound Poisson process which e.g. is treated in [7]. However, already
in [1] appears the waiting time density whose Laplace transform is (1 + sβ)−1
as playing a distinct role, but was not recognized as a function of Mittag-Leﬄer
type (such functions too long having been insuﬃciently known). Gorenﬂo and
Mainardi and co-authors have, beginning in 1998, published several papers on
various types of approximating random walks for space-fractional and space-
time fractional diﬀusion processes of which we quote [11], [12], [13] and [15],
furthermore some papers (stressing the relevance of the Mittag-Leﬄer waiting
time) motivated by applications to ﬁnance: [27], [20], [14]. In [14] the space-
time fractional diﬀusion equation is obtained as a diﬀusion limit of the time-
fractionalized Kolmogorov-Feller equation
D
t ∗
β p(x, t) = −p(x, t) +
∞
Z
−∞
w(x −x′)p(x′, t)dx′ .
(5.1)
The publications [18] and [19] are devoted to analytic treatment via integral
representations of the evolving probability densities that solve the (spatially one-
dimensional) space-time fractional diﬀusion equation. An important concept in
fractional diﬀusion processes is the concept of subordination (see, e.g. [22] and
[21]).
By our way of relating the scaling parameters in the passage to the
limit we circumvent this concept. Let us mention again [12]. There we have
based our scaled transition to the limit on two lemmata for the asymptotics
of the transforms of the densities whereas here we work with the MASTER
LEMMATA for the distribution functions, motivated by [9]. This, of course, is
more general and allows discrete and continuous probabilities and mixtures of
9


## Page 10


them. However, in not so general situations the other lemmata may be simpler
to apply (as we have done in [15] for the fully discrete case with regular grids).
In [29], in contrast to our treatment in [12] and here, the scaling is not done
via the individual steps in space and time but directly in the distributions of
waiting times and jumps. However, this is equivalent to our way. Let us in this
context say a few words to the essential statement of [16]. There Hilfer shows
that a power law for the waiting time is not suﬃcient for getting in the limit a
fractional diﬀusion process with the fractional time derivative having the same
order as the power law. This seemingly negative result, however, does not hit
the theory expanded here in our paper. In Hilfer’s counter-example the passage
to the diﬀusion limit is not well-scaled in our sense; in fact, in it are hidden two
diﬀerent scalings. Thus [16] may inspire to investigate systematically continuous
time random walks that can be scaled in more than one way.
Let us, as a ﬁnal statement, say that the case of non-symmetric jump dis-
tributions (bypassed in our paper) can analogously be studied, and let us also
hint to [31].
Acknowledgments This work has partially been carried out in the frame of
the INTAS project 00-0847. The second named author is grateful for the grant
provided by the government of Arab Republic of Egypt. We are grateful to F.
Mainardi and E. Scalas for fruitful discussions on the subject. The ﬁrst named
author thanks R. Hilfer for a preprint of [16] and for inspiring discussions.
References
[1] V. Balakrishnan: Anomalous diﬀusion in one dimension. Physica 132A
(1985), 569–580.
[2] E. Barkai: CTRW pathways to fractional diﬀusion. Chemical Physics 284
(2002), 13–27. Special Issue on Strange Kinetics, Guest Editors: R. Hilfer,
R. Metzler, A. Blumen, J. Klafter.
[3] N. H. Bingham, C. M. Goldie and J. L. Teugels: Regular Variation. Cam-
bridge University Press, Cambridge 1987.
[4] A. V. Chechkin and V. Yu. Gonchar: A model for persistent L´evy motion.
Physica A 277 (2000), 312–326.
[5] D. R. Cox: Renewal Theory. Methuen, London 1967.
[6] W. Feller: On a generalization of Marcel Riesz’ potentials and the semi-
groups generated by them. Meddelanden Lunds Universitets Matematiska
Seminarium, Lund 1952, pp. 73–81.
[7] W. Feller: An Introduction to Probability Theory and its Applications,
Vol. 2. Wiley, New York 1971.
10


## Page 11


[8] I. M. Gel`fand and G. E. Shilov: Generalized Functions, Volume I. Aca-
demic Press, New York and London 1964. Translated from the Russian.
[9] B. V. Gnedenko and A. N. Kolmogorov: Limit distributions for Sums of
Independent Random Variables. Addison-Wesley, Cambridge/Mass. 1954.
Translated form the Russian.
[10] R. Gorenﬂo and F. Mainardi: Fractional calculus: integral and diﬀerential
equations of fractional order. In: A. Carpinteri and F. Mainardi (editors):
Fractals and Fractional Calculus in Continuum Mechanics, Springer-Verlag,
Wien 1997, pp. 223–276. [E-Print: http://www.fracalmo.org]
[11] R. Gorenﬂo and F. Mainardi: Random walk models approximating sym-
metric space-fractional diﬀusion processes. In: J. Elschner, I. Gohberg and
B. Silbermann (editors): Problems in Mathematical Physics, Birkh¨auser-
Verlag, Basel 2001, pp. 120–145.
[12] R. Gorenﬂo and F. Mainardi: Non-Markovian random walk models, scaling
and diﬀusion limits. In: Ole E. Barndorﬀ-Nielsen: Mini-proceedings: 2nd
MaPhySto Conference on Le’vy Processes: Theory and Applications (Jan-
uary 2002. Miscellanea no. 22, August 2002, pp.120–128. ISSN 1398–5957.
MaPhySto: Center for Mathematics and Stochastics, Aarhus, Denmark.
[13] R. Gorenﬂo and F. Mainardi: Fractional diﬀusion processes: probability
distributions and continuous time random walk. In: G. Rangarajan and
M. Ding (Editors): Processes with Long Range Correlations, pp.148–166.
Lecture Notes in Physics, No. 621 Springer Verlag, Berlin 2003. [E-Print:
http://arxiv.org/abs/0709.3990]
[14] R. Gorenﬂo, F. Mainardi, E. Scalas and M. Raberto: Fractional calculus
and continuous-time ﬁnance III; the diﬀusion limit. In: M. Kohlmann and
S. Tang (editors): Mathematical Finance, Birkh¨auser-Verlag, Basel 2001,
pp. 171–180.
[15] R. Gorenﬂo and A. Vivoli: Fully discrete random walks for space-time
fractional diﬀusion equations. In: M. D. Ortigueira and J. A. Tenreiro
Machado (guest editors): Fractional Signal Processing and Applications.
Signal Processing 83 No. 11 (2003), Special Issue, pp. 2411–2420.
[16] R. Hilfer: On fractional diﬀusion and continuous time random walks, Phys-
ica A 329 (2003) 35–40.
[17] R. Hilfer and L. Anton: Fractional master equation and fractal time random
walk. Physical Review E 51 (1995), R848–R851.
[18] F.
Mainardi,
Yu.
Luchko
and
G.
Pagnini:
The
fundamental
solution
of
the
space-time
fractional
diﬀusion
equation.
Frac-
tional Calculus and Applied Analysis 2 (2001),
153–192. [E-Print:
http://arxiv.org/abs/cond-mat/0702419]
11


## Page 12


[19] F. Mainardi, G. Pagnini and R. Gorenﬂo: Probability distributions as so-
lutions to fractional diﬀusion equations. In: Mini-proceedings as [12], pp.
197–205.
[20] F. Mainardi, M. Raberto, R. Gorenﬂo and E. Scalas: Fractional calculus
and continuous-time ﬁnance II: the waiting-time distribution. Physica A
287 (2000), 468–481.
[21] M. M. Meerschaert, D. A. Benson, H.-P. Scheﬄer, B. Baeumer: Stochastic
solution of space-time fractional diﬀusion equation. Physical Review E 65
(2002), 041103-1–041103-4.
[22] M. M. Meerschaert and H.-P. Scheﬄer: Limit Distributions for Sums of
Independent Random Variables. Heavy Tails in Theory and Practice. John
Wiley and Sons, New York 2001.
[23] R. Metzler and J. Klafter: The random walk’s guide to anomalous diﬀusion:
a fractional dynamics approach. Physics Reports 339 (2000), 1–77.
[24] E. W. Montroll and G. H. Weiss: Random walks on lattices, II. Journal of
Mathematical Physics 6 (1965), pp. 167–181.
[25] B. Rubin: Fractional Integrals and Potentials. Addison Wesley Longman,
Harlow/Essex (England) 1996.
[26] S. G. Samko, A. A. Kilbas and O. I. Marichev: Fractional Integrals and
Derivatives: Theory and Applications. Gordon and Breach, New York 1993.
Translated from the Russian edition (Minsk 1987).
[27] E. Scalas, R. Gorenﬂo and F. Mainardi: Fractional calculus and continuous-
time ﬁnance. Physica A 284 (2000), 376–384.
[28] W. R. Schneider and W. Wyss: Fractional diﬀusion and wave equations. J.
Math. Phys. 30 (1989), 134–144.
[29] V. V. Uchaikin and V. V. Saenko: Stochastic solution of partial diﬀerential
equations of fractional order. Siberian Journal of Numerical Mathematics
6 (2003), 197–203.
[30] A. H. Zemanian: Distribution Theory and Transform Analysis. Dover Pub-
lications, New York 1987 (slightly corrected republication of the McGraw-
Hill edition, New York 1965.
[31] Recommendation:
For more literature related to fractional diﬀusion
see also the WEB site devoted to FRActional CALculus MOdelling:
http://www.fracalmo.org
12

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]
