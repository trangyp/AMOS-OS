---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1107.2715v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1107.2715v1_Stereo_pairs_in_Astrophysics

> Source: 1107.2715v1_Stereo_pairs_in_Astrophysics.pdf

> Pages: 16

---


## Page 1


Stereo pairs in Astrophysics
Fr´ed´eric Vogt1 and Alexander Y. Wagner1
Abstract
Stereoscopic visualization is seldom used in Astro-
physical publications and presentations compared to
other scientiﬁc ﬁelds, e.g., Biochemistry, where it has
been recognized as a valuable tool for decades.
We
put forth the view that stereo pairs can be a useful
tool for the Astrophysics community in communicat-
ing a truer representation of astrophysical data. Here,
we review the main theoretical aspects of stereoscopy,
and present a tutorial to easily create stereo pairs us-
ing Python. We then describe how stereo pairs pro-
vide a way to incorporate 3D data in 2D publications
of standard journals.
We illustrate the use of stereo
pairs with one conceptual and two Astrophysical sci-
ence examples: an integral ﬁeld spectroscopy study of
a supernova remnant, and numerical simulations of a
relativistic AGN jet.
We also use these examples to
make the case that stereo pairs are not merely an os-
tentatious way to present data, but an enhancement
in the communication of scientiﬁc results in publica-
tions because they provide the reader with a realistic
view of multi-dimensional data, be it of observational
or theoretical nature. In recognition of the ongoing 3D
expansion in the commercial sector, we advocate an in-
creased use of stereo pairs in Astrophysics publications
and presentations as a ﬁrst step towards new interactive
and multi-dimensional publication methods.
Keywords Data Analysis and Techniques – Tutorial;
Stereoscopy – Stereo pairs
Fr´ed´eric Vogt and Alexander Y. Wagner
1Mount Stromlo and Siding Spring Observatories, Research
School of Astronomy and Astrophysics, Australian National Uni-
versity, Cotter Road, Weston Creek, ACT 2611, Australia.
1 Introduction
Stereoscopy consists in giving a depth perception out of
2D material to the viewer, and the concept behind it is
fairly simple: it requires sending distinct and carefully
chosen images to each eye, without one eye noticing
the images intended for the other. The notion of depth
perception, or stereopsis, has been discussed as early
as A.D. 280 by Euclid (Okoshi 1976). While there has
been some experimentation using sketching techniques
before 1800 (Norling 1953), the invention of photogra-
phy by Niepce (Smith 1877; Perrier 1934) in the be-
ginning of the 19th Century marked the real start of
extensive experimentation with stereoscopy.
Wheat-
stone (1838) assembled one of the earliest known stereo-
scopes, but Brewster is usually attributed the construc-
tion of the ﬁrst practical viewing device, now referred
to as the Brewster stereoscope (Norling 1953).
As predicted by Scripture (1899), stereoscopy en-
countered quite a strong success in these early times,
when stereoscopes where made widely available, be-
cause the production of stereo pairs become easier as
photographic techniques evolved.
Darrah (1977) dis-
cusses these early ages (from 1851 to 1935) of stere-
oscopy in depth, and we refer the interested reader to
his work for a detailed overview of the various applica-
tions of stereo pairs in those times.
Although the principle behind stereoscopy has re-
mained the same ever since, there have been regular
improvements to the methods of production and visu-
alization. In fact, the interest in stereoscopy has been
closely linked to the development of both imaging and
visualization techniques (Okoshi 1976), and peaks of
interest arose as new production and/or visualization
tools were invented.
Beside the evolution of photo-
graphic techniques, the advent of computers and their
ability to produce accurate and detailed stereo pairs
represents one such development which resulted in a
peak of interest for stereoscopy that started in the 70’.
arXiv:1107.2715v1  [astro-ph.IM]  14 Jul 2011


## Page 2


2
Several viewing devices have also been developed
over the years, with one common aim: increasing the
comfort and simplicity of stereoscopy for the viewer.
In comparison to individual stereographs, the develop-
ment of specialized glasses (red-blue, polarised, shutter-
type) made stereo pairs easier to visualise. Lately, new
stereoscopic technologies are being integrated into con-
sumer products at a fast pace; movies, televisions, gam-
ing consoles, cell phones, advertisement panels, and so
on. Stereoscopy has become especially popular in the
movie industry in the past few years with the advent
of digital 3D cinemas. One should nonetheless not for-
get that stereo movies themselves are not recent: The
Power of Love, in anaglyph 3D, ﬁrst aired in 1922 (Zone
2007).
In the scientiﬁc community, stereoscopy has been
known and used in the past, but the extent to which
it has been exploited in the presentation of data diﬀers
from ﬁeld to ﬁeld. In Astrophysics, stereoscopy has not
been used extensively, despite the multi-dimensional
nature of many data sets. Often, a data cube is sliced
or projected in order to obtain 2D publishable pictures
and graphs.
The issue of displaying and publishing
multi-dimensional data sets has been identiﬁed in the
past, and some interesting (non-stereoscopic) solutions
have been proposed. Cosmologists working on the time
evolution of the large scale structures in the Universe
using 3D movies to illustrate their simulations results
is one example (e.g. Holliman 2010). Recently, Barnes
and Fluke (2008) described how documents in an Adobe
Portable Document Format (.pdf) are now able to con-
tain animated 3D models, and described how this can
be used to create interactive 3D graphs. In addition,
Barnes et al. (2006) developed a 3D plotting library
speciﬁcally tailored to the needs of the Astrophysics
community. Fluke et al. (2006) also discuss and present
alternative advanced image displays which might po-
tentially take on a more signiﬁcant place within the
Astrophysics community in the future.
Yet, stereoscopic techniques are not unknown to As-
trophysicists.
Planetary scientists, for example, use
red-blue anaglyphs. In the case of Mars (e.g. Neukum
et al. 2004; Keszthelyi et al. 2008), several probes
and remote sensing satellites were equipped with spe-
cial stereo cameras, for example the European Space
Agency Mars Express satellite and its High Resolu-
tion Stereo Camera Experiment (Jaumann et al. 2007),
the Mars Reconnaissance Orbiter and its High Reso-
lution Imaging Science Experiment (HiRISE) camera
(McEwen et al. 2007), the Phoenix lander and its Sur-
face Stereo Imager (SSI) (Lemmon et al. 2008) or the
imager for the Mars Pathﬁnder (MPI) mission (Smith
et al. 1997).
Stereo pairs are another type of stereoscopic solu-
tion that has been employed to accommodate multi-
dimensional data sets in publications. One of the ﬁrst
Astronomical stereo pairs published depicted the Moon
and was created as early as 1862 by L.M. Rutherford
(Darrah 1977).
By taking two subsequent images of
the Moon with a six days interval, he obtained a strong
enough change in orientation to induce a reasonable
feeling of depth. More recently, the advent of comput-
ers expanded the possible applications of stereo pairs
in Astrophysics. For example, Yahil (1980) used them
to display the position of the galaxies in the Revised
Shapley-Ames Catalog; Martinet and Magnenat (1981)
and Martinet et al. (1981) used stereo pairs to illustrate
the shape of invariant surfaces in their study of dynam-
ical problems with 3 degrees of freedom; van de Wey-
gaert and Icke (1989) and Icke and van de Weygaert
(1991) created stereo pairs to illustrate the Voronoi
model they used to describe the asymptotic distribu-
tion of the cosmic mass on 10-200 Mpc scales; Rhee et
al. (1991) produced stereo pairs to show a 3D map of
their sample of Abell clusters; Koutchmy and Moloden-
skii (1992) published a stereo pair of the Solar Corona
during the 1991 Solar eclipse; Sofue (1994) illustrated
the stripping of the LMC HI and molecular clouds; Sel-
man et al. (1999a,b) created stereo pairs of the colour-
magnitude diagrams of the ionizing cluster 30 Doradus;
Sirko et al. (2004) used stereo pairs to display the 3D
position of the blue horizontal-branch (BHB) stars dis-
covered in the SDSS (York et al. 2000) spectroscopic
survey; and Vogt and Dopita (2010) and Vogt and Do-
pita (2011) used stereo pairs in complement to their in-
teractive 3D maps of the oxygen-rich material in SNR
1E 0102.2-7219 and SNR N132D. These examples do
not represent an exhaustive list of all the work that has
been published using stereo pairs in Astrophysics, but
illustrate the wealth of topics that can proﬁt and make
use of this technique.
Nonetheless, the use of stereo pairs in Astrophysics
is less prevalent than in other ﬁelds. In Biochemistry,
for example, they have been an important tool to pub-
lish the 3D shapes of molecules from the beginning of
the computer-era (e.g. Hamilton 1970; Hardman and
Ainsworth 1973) until today (e.g Pujadas and Palau
2001; Landsberg et al. 2006; Xiang et al. 2010).
We believe that stereo pairs are a valuable tool in As-
trophysics too, which recent 3D innovations may help
renew. In other words, we argue that stereoscopy has a
great but under-exploited potential for the publication
of multi-dimensional Astrophysical data sets and can
be a valuable complement to more standard plotting
methods, especially with today’s computing abilities.
In Sec. 2, after introducing the free-viewing technique,


## Page 3


3
we discuss the various theoretical ways to construct a
stereo pair. In Sect. 3, we present our trade-oﬀmethod
to eﬃciently create stereo pairs of data cubes using
Python.
We then illustrate the unique features of
stereo pairs as compared to standard plots in three dif-
ferent examples in Sect. 4: a conceptual one in Sect. 4.1,
one based on observational data in Sect. 4.2 and one
based on theoretical data in Sect. 4.3, for which the use
of stereo pairs provides critical scientiﬁc information.
We discuss the role that stereo pairs can play regarding
future developments of 3D visualization techniques in
Sec. 5, and summarize our conclusions in Sect. 6.
2 A theoretical overview of stereo pairs
Several terms, such as stereoscopy, stereopsis, stereo
pairs and stereograms, are used throughout the liter-
ature, sometimes with slightly diﬀerent meanings. To
avoid confusion in this article, we refer to; stereopsis as
the depth perception reconstructed by the brain, stere-
oscopy as the science of inducing depth perception us-
ing 2D material of any type, stereograms as any type of
image capable of inducing a depth feeling when viewed
with the proper material, and stereo pair as a speciﬁc
type of stereogram, where the left hand side (the image
for the left eye; LHS) and right hand side (the image
for the right eye; RHS) images are located side-by-side.
2.1 Visualizing a stereo pair: the free-viewing
technique
At any time, our brain interprets the simultaneous im-
ages from each of our eyes, combines them and auto-
matically reconstructs a 3D image. The reconstruction
algorithm is completely unconscious, and it feels nat-
ural to see our environment in 3D. If one looks at a
structure at a distance of ∼60 cm for example, it will
be seen by the right eye as if it had been rotated by ∼5
degrees as compared to the left eye’s view. Hence, the
very same 3D feeling can be achieved by sending two
diﬀerent 2D pictures of the same object to the left and
right eye, if the pictures are taken from two diﬀerent
view angles.
As long as the brain believes that it is
looking at a real object, its automatic 3D reconstruc-
tion algorithm will work. The main challenge is to be
able to provide a diﬀerent image to each eye without
the other noticing it.
As we mentioned previously in Sect. 1, several tech-
niques exist to achieve this goal, such as stereoscopes,
glasses, or auto-stereoscopic screens (for which no
glasses are required). Depending on the visualization
technique, stereoscopic images carry diﬀerent names :
anaglyphs (red-blue, polarized) need to be looked at us-
ing the appropriate glasses; stereo pairs, and autostere-
ograms (Tyler and Clarke 1990) require the so-called
free-viewing technique. This latter way of looking at
stereo pairs has the advantage that it does not require
any special equipment, provided that the stereo pair
is in the correct format. This advantage makes it the
best method to visualize stereo pairs in publications,
as a majority of the readers accessing the article in its
online or printed version will be able to directly get a
feeling of depth. With the left and right images side-
by-side, it is up to the reader to have each eye looking
at one image only, thus recreating the 3D feeling. Ob-
viously, this requires the reader to be familiar with the
technique. However, the extended usage of stereo pairs
in other ﬁelds, as mentioned in Sect. 1, gives us conﬁ-
dence that this fact should not represent an obstacle to
the popularization of stereo pairs in Astrophysics. The
web oﬀers a vast resource of examples for training one’s
ability to see the 3D images from stereo pairs rapidly,
and many websites provide tutorials and suggestions on
how to make it work 1.
There are two ways to look at stereo pairs : par-
allel and cross-eyed. The names refer to the required
orientation of the eyes, which depends on the position
of the LHS and RHS images within the pair: parallel
viewing requires the LHS image to be on the left (and
the RHS image on the right) while cross-eyed requires
them to be swapped. Whether one technique is more
comfortable than the other is a matter of personal opin-
ion and training. In Fig. 1, we present for comparison
two stereo pairs of the same object - two intersecting
spheres of diﬀerent radius - from the same viewpoint.
The top pair is designed for parallel viewing, while the
bottom one requires the cross-eyed technique to be vi-
sualized properly.
Looking at a stereo pair for the ﬁrst time can be
quite challenging and there exists several ways to make
it work. After experimenting with some students and
astronomers of the Mount Stromlo Observatory, many
having no previous experience with stereo pairs, we pro-
vide some suggestions that might help when looking at
a stereo pair for the ﬁrst time :
Parallel viewing : Holding the printed page in front
of you, look at the horizon. Once in focus, lift up the
page so that the stereo pair reaches the level of your
eyes, but without adjusting the focus onto the page
- the focus remains at the horizon, however, your
attention is on the page. If done correctly, the left
and right images will merge into a central 3D image
1for
example
http://spdbv.vital-
it.ch/TheMolecularLevel/0Help/StereoView.html#con


## Page 4


4
Fig. 1 : Parallel (top) and cross-eyed (bottom) stereo
pairs of two intersecting spheres of diﬀerent radii.
of the double sphere. If your eyes focus on the page
when you movie it up, try to relax them. If you ﬁnd
it diﬃcult to see the 3D image (so that you can read
the axis labels), it might help to convince yourself
that you are looking at something real.
Cross-eyed viewing : Place the printed page on a
ﬂat surface, and position your head straight above
the stereo pair. Bring one ﬁnger in between the page
and your eyes, so that its tip is located just below
the pair, in the middle. Focusing on your ﬁnger tip
will merge the background left and right images into
a central 3D one. If they do not merge properly, try
adjusting the height of your ﬁnger. The last step con-
sist in removing the ﬁnger while keeping the central
3D image of the stereo pair, and might require some
concentration/practice.
For both techniques, the alignment of the head is
important - a slight rotation will have for consequence
that the LHS and RHS will not overlap properly when
merging them. With some experience, stereo pairs can
be viewed on paper as well as on a computer screen.
Our own experience as well as that of astronomers and
students at the Mount Stromlo Observatory show that
getting the eyes in the correct position becomes eas-
ier with practice, ultimately becoming almost an auto-
matic adjustment.
In this article, we shall only use stereo pairs designed
for parallel viewing, which is the most comfortable and
natural technique for most of the people we have asked
around us.
Note that looking at a stereo pair with
the wrong technique will have the consequence of re-
verting the depth axis (i.e. ﬂipping the object back to
front). While using the appropriate viewing technique
is recommended, this fact nevertheless enables people
more comfortable with the cross-eyed technique to ob-
tain a 3D impression of every stereo pairs within this
article. Generally, stereo pairs in Biochemistry publica-
tions are of the parallel type, a tradition which is most
likely a remnant of the necessity to accommodate the
use of viewing devices in the 70’s, as described by Smith
(1971). There is however no ﬁxed rules, and the stereo
pair constructed by Sirko et al. (2004) of the position
of BHB stars in the SDSS spectroscopic survey is for
example a cross-eyed pair.
2.2 Constructing a stereo pair: the Toe-in and Oﬀset
methods
There exist two main techniques to build a stereo pair,
depending on the projection method used to obtain the
left and right images. The ﬁrst one, known as the Toe-
in method, mimics the human eyes’ behaviour, and is
in that sense the most obvious technique. The concept,
illustrated in Fig. 2, is as follows : the LHS and RHS
projections of the 3D scene are created by projecting
it along two view vectors rotated by δ0 =∼2-5◦along
the azimuthal angle. The value of δ0 is somewhat ar-
bitrary, and a higher angle will result in an increased
depth perception for the viewer. Our own experimenta-
tions, as well as various online tutorials, indicate that a
value of δ0 =5◦works well. This freedom in the choice
of δ0 is also reﬂected in Biochemistry stereo pairs, for
which several values are being used throughout the lit-
erature; 2◦(Hayman 1987), 3◦(Berry and Baker 2010),
5◦(Robinson 1989; Stockert 1994), 6◦(Hayman 1987;
Stockert 1994) and 10◦(Stockert 1994).
Fig. 2 : Geometry for the construction of Oﬀset (left)
and Toe-in (right) stereo pairs. LHS and RHS projec-
tions of the original 3D data set are created along two
diﬀerent view vectors.
There are several issues with the Toe-in method, one
of the principal being vertical parallax due to keyston-
ing.
Because the projections are taken at an angle,


## Page 5


5
successive planes perpendicular to the viewer will be
slightly distorted. The distortion is inverted in the LHS
and RHS images. As a result, when merging the two
images, there will be a mismatch in the outer points,
resulting in a blurred image. It should be noted that
keystoning is closely related to the distance of the cam-
era to the object, and is more important when being
close from the 3D scene.
The second issue with the
Toe-in method lies in the fact that the eyes will have
to adjust from a convergent to a divergent position in
order to scan the depth dimension. For extended ob-
jects this can result in strong discomfort for the viewers,
and even an impossibility to merge the left and right
images if the converging/diverging angle becomes too
important. Woods et al. (1993) discuss the various dis-
tortions present in stereo pairs in great details, and we
refer the interested reader to his article for more details.
The Oﬀset (or Oﬀ-axis) method addresses and solves
the problems of the Toe-in projection, and is in that
sense sometimes considered to be more correct. In this
case, the LHS and RHS cameras look at the 3D scene
in parallel directions, and oﬀset by a distance η. This
method does not create any keystoning, and ensures
that the eyes remain in the same position when scan-
ning the depth dimension of the reconstructed 3D pic-
ture. An illustration of the method is shown in Fig. 2.
One of the inherent drawbacks of this method is that
the outside regions of the LHS and RHS ﬁelds do not
overlap - and hence must be taken oﬀthe ﬁnal image.
Choosing between the Toe-in and the Oﬀset method
to create stereo pairs is entirely up to the creator of
the pair. As we will discuss in the next Section, the
Toe-in method can provide excellent stereo pairs un-
der certain circumstances ; the stereo pairs shown in
Fig. 1 have for example been created using the Toe-in
projection method, and in the Biochemistry literature,
many tutorials describing the creation of stereo pairs
use the Toe-in method (e.g. Hayman 1987; Robinson
1989; Stockert 1994; Berry and Baker 2010). Further-
more, sometimes, intrinsic limitations of the software
or programming language used to create the stereo pair
might require a trade-oﬀbetween feasibility and qual-
ity, as we will show in Sec. 3.
The last step required to construct a stereo pair con-
sists in placing the LHS and RHS images side-by-side.
The distance between the two images is not critical.
This reﬂect the fact that the interpupillary distance
is not uniform across the population, but varies with
age, gender, and race.
Speciﬁcally, Dodgson (2004)
mentions a mean interpupillary distance of 63 mm for
adults, with the vast majority lying within a 50-75 mm
range. In this article, we have used point-to-point sep-
arations (between the LHS and RHS images) ranging
from 3.5 cm to 5 cm depending on the stereo pair, and
it is a matter of personal opinion as to which value is
most comfortable. Increasing the inter-image distance
above 6 cm is not advisable, as the stereo pair might
become harder to visualize for people with a smaller
interpupillary distance than average.
3 Constructing a stereo pair : a
Python/Matplotlib solution
For stereo pairs to be recognized as a valuable tool by
the Astrophysics community requires them to be ex-
tremely easy to create, implement and link to the data
set. Let us consider the 3D data set used to produce
Fig. 1, which can be seen as a cloud of points in 3D
space. There exist many methods in order to easily pro-
duce stereo pairs from such a data cube, and it would
be impossible to list them all here. Some commercial
software packages can produce stereo pairs with a single
mouse click - the stereo pairs shown in Sec. 4.3 were for
example produced with the VisIt software.
Alterna-
tively, many scientists have developed their own soft-
ware, speciﬁcally tailored to their own data type and
format. Such customized or commercial software are
capable of creating excellent stereo pairs, and are usu-
ally designed well enough not to have too steep learning
curves.
Here, we propose an alternative, oﬀ-the-shelf, eﬃ-
cient way to produce stereo pairs using the program-
ming language Python. This method, which we will
refer to as the simpliﬁed Toe-in (sTi) is based on our
own experimentation, and is extremely straightforward
to implement, even for people with little/no experience
with this language. Furthermore, creating stereo pairs
with Python grants access to a large collection of non-
plotting modules to work on the data cube beforehand.
This provides the more advanced user with the free-
dom to potentially reduce, sort, ﬁt and clean the data
set before creating a stereo pair - a strong advantage as
compared to commercial software which often requires
speciﬁc input, and does not enable direct data interac-
tion.
Our sTi method is based on the Toe-in projection
described previously, but accounts for current limita-
tion in the Matplotlib plotting module, in which
several projection parameters are currently hard-coded
and cannot be accessed easily. The required functions
are located within the mplot3d toolkit2, and are de-
signed to create a 2D projection out of a 3D scene.
2see the online documentation for a detailed description :
http://matplotlib.sourceforge.net/mpl toolkits/mplot3d/index.html


## Page 6


6
Speciﬁcally, the Axes3D instance, creating the plot-
ting area, takes in two parameters, the elevation θ and
the azimuth φ, both in degrees. Creating an sTi stereo
pair is then a 3-steps process :
1: Create two side-by-side (using subplot) plots, each
with the Axes3D instance.
2: For a viewpoint located at (φ0;θ0), set the left plot
viewpoint to (φ0 −2.5◦;θ0) and the right plot view-
point to (φ0 + 2.5◦;θ0)
3: Print the data using the appropriate mplot3d func-
tion, such as scatter3D for a cloud of points, or
contour3D for isosurfaces.
This method is a trade-oﬀ: Toe-in or Oﬀset stereo
pairs cannot presently be created with Matplotlib
easily, unlike sTi stereo pairs. Especially, implement-
ing the Toe-in method requires the modiﬁcation of the
source code of the Axes3d function3.
But the sTi simplicity comes at a price. For view-
points with no elevation (θ0 = 0◦), the sTi method
is identical to the Toe-in technique.
However, errors
both in the LHS/RHS images orientation, as well as
in their azimuthal separation, are introduced with in-
creasing values of |θ0|. For completeness, we describe
those issues in detail in the Appendix A, and compare
sTi stereo pairs with Toe-in and Oﬀset stereo pairs for
diﬀerent elevations.
The comparisons show that the
sTi method delivers very similar results to the Toe-in
method for elevation as high as |θ0| ∼50◦. Beyond this
limit, the depth perception is reduced compared to the
Toe-in method. Comparing with the Oﬀset method re-
veals that the 3D structure of the object is increased
and better revealed in the sTi method, which makes
the latter more suitable for the publication of multi-
dimensional data sets. In other words, if the object ap-
pears, with the Oﬀset technique, to be popping out of
the screen, it does not contain itself much depth infor-
mation. Peterka et al. (2009) reached a similar conclu-
sion when building a stereoscopic movie of 3D simula-
tions of a core-collapse supernova (Blondin et al. 2003)
: ” [The Oﬀset technique] ... created a plausible fac-
simile of 3D. However, the trained observer noticed the
ﬂatness in the center of the sphere, and we did not want
to rely on 2D depth cues such as lighting and shading to
convey 3D information.” Hence, the Toe-in, and in our
case the sTi technique, is recommended for the creation
of stereo pairs in Astrophysics. It is:
• more eﬃcient at providing a depth structure to the
data as compared to the Oﬀset method.
3We hope to eventually include our source code update in an
upcoming release of Matplotlib. In the meantime, a copy of
our modiﬁed Axes3d function, that enables the creation of Toe-
in stereo pairs, can be obtained from fvogt@mso.anu.edu.au
• easier to implement in Python than the proper Toe-
in method (which requires the modiﬁcation of the
source code).
The hard-coded parameters within mplot3d cause
no visible vertical parallax or other visual defects in sTi
stereo pairs.
We have asked some students and astronomers at the
Mount Stromlo Observatory to test our sTi stereo pairs.
None of them found the sTi pairs more tiring or diﬃcult
to visualize, with a very satisfactory depth impression.
Most of them also noted that even if the depth percep-
tion in sTi pairs is degraded beyond |θ0| ∼50◦com-
pared to Toe-in pairs, it does not vanishes completely.
In that sense, our suggested sTi method can be used for
any viewpoint with satisfactory depth impression and
reasonable comfort for the viewer.
4 Application examples for stereo pairs
We illustrate the role that stereoscopy, in the form
of stereo pairs, can play in a publication with three
examples; conceptual, observational, and theoretical.
Clearly, the range of applications for stereoscopy in
Astrophysics is much larger than those we are about
to present, and the publications mentioned in Sec. 1
highlight the fact that stereo pairs can be used for al-
most any type of multi-dimensional data set, e.g., 3D
maps and structures, 3D iso-surfaces, N-body simula-
tions and trajectories, cosmological simulations, mag-
netic and other ﬁeld maps, 3D function ﬁtting, color-
magnitude diagrams, hydrodynamic simulations and
complex (e.g. turbulent) structures.
4.1 Conceptual example: intersecting spheres
As mentioned in Section 1, stereoscopy, in this case in
the form of stereo pairs, is diﬀerent from standard plots
in that it transmits a feeling of depth to the viewer. Let
us illustrate this advantage with a practical example.
In Fig. 3, we present three stereo pairs of the same
object, two intersecting spheres of diﬀerent radius. In
each case, the two spheres’ symmetry axis is in the XZ
plane, and tilted by 45 degrees with respect to the Z
axis.
Several observations can be made at this point.
First, stereo pairs work both in color or greyscale. Sec-
ond, stereo pairs provide the reader with a true feeling
of depth, and unambiguously convey the orientation of
the structure. In the case of this double-sphere, the use
of a stereo pair removes the ambiguity that arises when
looking at a single image only, in which case the spheres
could be seen as being oriented in the XZ or YZ plane.


## Page 7


7
Fig. 3 : Stereo pairs of two intersecting spheres of dif-
ferent radius, shown in black and white (top) and color
(middle and bottom). In each case, the two spheres ori-
entation axis is in a XZ plane, and tilted at 45 degrees
with respect to the Z axis. The orientation is best re-
vealed in the 3D reconstruction using the free-viewing
technique.
The use of colors may also help lift the orientation de-
generacy: in the bottom pair, plotting the green sphere
above the pink one does suggest that the axis lies in the
XZ plane. However, in some cases, it might not always
be possible to deﬁne the order in which the objects are
plotted (or printed) by color. In the middle pair, we
have intentionally plotted the pink sphere above the
green, which then suggest, when looking at only one of
the image, that the rotational axis lies in a YZ plane.
In that case, stereo viewing is perfect to correct this
wrong feeling. In 3D, the middle pair looks essentially
identical to the bottom one, with the rotational axis
lying in the XZ plane (i.e. the big, green sphere is on
top in all three cases). While this example is rather
simple, it nevertheless illustrates some key advantages
that stereo pairs have over single projected images. We
reinforce this point with stereo pairs of more complex
shapes presented in the next sections.
4.2 Observational example : SNR N132D in the LMC
Vogt and Dopita (2011) used the Wide Field Spec-
trograph (Dopita et al. 2007, 2010) at Siding Spring
Observatory to image the Young Supernova Remnant
(YSNR) N132D located in the Large Magellanic Cloud
(LMC). The initial data cube axis units are (X [arcsec],
Y [arcsec], λ [˚A]), and by studying the [O III] forbidden
line at λ5007 ˚A, and its blue- and red-shifted features,
they can identify the oxygen-rich knots in the YSNR,
and obtain their radial velocities. The data cube axes
are then transformed to (X[arcsec], Y[arcsec], vr [km
s−1]). Assuming a distance to the LMC of 50 kpc (from
van den Bergh 1999), and an age of ∼2500 years, they
transformed their third data cube axis to a spatial di-
mension. Thus, they obtained an accurate 3D spatial
map with axes (X [pc], Y [pc], Z [pc]) of the oxygen-rich
ﬁlaments in SNR N132D. Stereo pairs of this 3D map
are shown in Fig. 4.
Fig. 4 : 3D stereoscopic maps of the oxygen rich ejecta
in SNR N132D, viewed from the NNE and +10◦eleva-
tion with respect to the plane of the sky (top), and from
the NNW and +10◦elevation (bottom). The scales are
given in pc. Adapted from Vogt and Dopita (2011).
Stereo pairs are one very useful way to fully under-
stand the true nature of this SNR. Vogt and Dopita
(2011) have used projections of their 3D map, that
showed the clumpy structure of the ejecta, as well as
hints of the ring-like structure of the ejecta. They also
created an interactive 3D map, that enables the reader
to zoom, pan, rotate and ﬂy around and through their
3D map. Stereo pairs, together with those others visu-
alization methods, conﬁrmed the presence of the ring
structure, and ruled out any perspective eﬀects due to
the projection of the 3D map on a 2D plane. The stereo


## Page 8


8
pairs are very eﬃcient in showing this ring to the reader,
compared to, e.g., a montage of slices. This is a big ad-
vantage in the case of SNR N132D, for which the actual
shape of the ejecta has been subject to interpretation
since the discovery of the remnant (see Lasker 1980;
Morse et al. 1995; Vogt and Dopita 2011). Everyone
can see the ring, and the impression of depth given by
stereo pairs is a valuable complement to the interactive
3D map.
Those stereo pairs have been created with Python
using the sTi technique described in Sect. 3. The whole
code, that takes as an input the data cube in a .ﬁts
format, contains less than 50 lines, of which only 10 are
actually responsible for plotting the data.
4.3 Theoretical example: relativistic AGN jets and
fractal clouds
Stereo pairs can also be used for the visualization of the-
oretical data sets. In this example, we use stereoscopy
to reveal the structure of a simulated relativistic Ac-
tive Galactic Nucleus (AGN) jet (Wagner and Bicknell
2011). The jet simulations were grid-based hydrody-
namic simulations which produced multivariate data of
thermodynamic quantities, e.g., density, temperature,
pressure, velocity components and tracers, as functions
of 3 rectilinear spatial coordinates. The resolution of
the simulations was 5123 cells, each cell representing
a physical volume of (2pc)3. Volume rendered images
of the double jet structure are shown in the two stereo
pairs, Fig. 5 and Fig. 6. In these renderings, the ray-
traced variable was proportional to the 1.8th power of
the density and the tracer variable of the jet, which is
a measure of the radio emissivity of a jet plasma.
Figure 5 shows that stereo pairs do not necessarily
need to be made up of square images. In this case, the
upright rectangular stereo pair allows one to inspect
the 3D structure of the jet along the full length of its
propagation axis. In particular, one can see the defor-
mations of the central jet stream as it becomes unstable
due deceleration and entrainment in the lobes (Bicknell
1984). The structure of the jet lobes along the line of
sight is also clearer in the stereo pairs than in either of
the 2D images on their own. In the edge-on stereo pairs
of Fig. 6, the use of stereoscopy enables one to iden-
tify the locations of lower and higher concentrations of
jet plasma within the volume of the lobe.
Globally,
one obtains a less ambiguous picture of the true shape
and structural characteristics of the complex ﬂow. The
viewer obtains a strong sense of depth in the image,
despite the contracted view at small angles of the line
of sight to the jet axis. The relativistic AGN jet sim-
ulation were performed with the FLASH code (Fryxell
Fig. 5 : Volume rendered side view of a simulated
relativistic AGN jet.
Fig. 6 : Edge-on view of the same simulated jet shown
in Fig. 5.
et al. 2000). The stereo pairs were produced with the
VisIt software, developed at the Lawrence Livermore
National Laboratory4. VisIt has a built-in stereo out-
put.
As a further example for the visualization of theo-
retical data beneﬁting from stereoscopy, Fig. 7 shows a
stereo pair of fractal clouds. These were generated with
the procedure outlined by Lewis and Austin (2002).
The procedure creates a spatially fractal distribution
in cloud pixels that simultaneously obeys a single-point
4VisIt is freely available at: https://wci.llnl.gov/codes/visit/home.html


## Page 9


9
log-normal probability density function in cloud den-
sity. On certain scales, fractal structure and log-normal
single point statistics are characteristic of atmospheric
(Barker et al. 1996) and interstellar (Federrath et al.
2009) clouds, and 3D data sets such as those depicted
in Fig. 7 may be used as initial conditions in hydrody-
namical simulations (Saxton et al. 2005; Sutherland and
Bicknell 2007). Such fractal structures usually prove
diﬃcult to visualize. The use of stereo pairs provides
an enhanced depth perception and thereby a clearer
view of the relative positions of the clouds. The fractal
outlines are more obvious, even interior to the clouds.
Fig. 7 : Stereo pair of fractal clouds, viewed from
within.
5 Future prospects for stereoscopy
In the previous Sections, we have described how stere-
oscopy, in the form of stereo pairs, can be a power-
ful tool for publishing multi-dimensional data sets. As
of today, stereoscopy is the most widely accepted tech-
nique for the capture and display of 3D content (Sharif
et al. 2011), whereas other methods, such as hologra-
phy (e.g. Smith 1975; Ackermann and Eichler 2007),
are considered very promising, but, as of now, harder
to implement on a large scale. In that sense, we believe
that stereo pairs can play a major role in the future
of data visualization in Astrophysics (and any ﬁeld of
Science), by providing researchers today with a simple
way to explore, discover, imagine, identify, and share
new stereoscopy-based analysis methods of their data,
methods that will then be ready for implementation in
exquisite interactive, immersive, high-end visualization
tools tomorrow.
Such immersive 3D visualization technologies, both
for the scientiﬁc and non-scientiﬁc community, still ap-
pears rather cubersome to use and implement, and of-
ten require oﬀ-the-shelf, custom software and setup.
But technology is moving at a fast pace.
For exam-
ple, working with and sharing data sets in 3D on tele-
visions and hand-held devices might become common-
place fairly soon, as such devices are already easily
available on the market.
The idea of 3D television
is rather old, with early experiments on stereo TV as
early as 1920, and the ﬁrst 3D TV broadcast occurring
in 1980 (Onural et al. 2006). Yet, very recently, the
rapid re-appearance of 3D televisions (and 3D hand-
held devices) lead Sherman et al. (2010) to state that
immersive 3D visualization technologies are now well
in the so-called slope of enlightment within the Hype’s
cycle (Fenn and Raskino 2008) of new technologies, the
last step before reaching a more productive phase. So
far, one of the main issues slowing down the expansion
of 3D television on the market is most probably the
lack of 3D content to be displayed on those devices, a
key factor for success (Sharif et al. 2011). This is also
true for scientiﬁc applications of this technology, and
a wider usage of stereo pairs may help scientists iden-
tify in what ways 3D TV could soon play a signiﬁcant
role in their research. Once the need will have been
clearly and widely identiﬁed, there is no doubt that the
yet missing standardized application programming in-
terface (API) and software links between scientiﬁc data
sets and already existing hardware will be rapidly im-
plemented. In short, we believe that stereo pairs, an
old and well documented tool (which can now be easily
implemented), could help scientists keep an open mind,
and potentially shape the future of multi-dimensional
data visualization and analysis.
6 Summary
We have discussed the concept of stereo pairs and high-
lighted their potential beneﬁts for the Astrophysics
community. First, we presented the free-viewing tech-
nique and provided advice to easily visualize both par-
allel and cross-eyed stereo pairs for the ﬁrst time. We
then argued that stereo pairs can be easily produced
and reproduced on a computer screen or on printed ma-
terial with most of the usual programming languages or
software used nowadays within the Astrophysics com-
munity.
In particular, we have introduced and de-
scribed an alternative, oﬀ-the-shelf, easy way to pro-
duce high quality stereo pairs with Python, which we
refer to as the simpliﬁed Toe-in method.
This tech-
nique adapts the oﬃcial Toe-in procedure taking into
account the current limitation of Python plotting abil-
ities, without aﬀecting on the quality of the stereo pairs.
Speciﬁcally, no vertical parallax can be detected in the
resulting stereo pairs. Testing our sTi stereo pairs on
several students and astronomers at the Mount Stromlo
Observatory revealed that they represent a good trade-
oﬀ, by being able to convey a satisfactory feeling of
depth from any viewpoint, and by being as eﬀective


## Page 10


10
as standard Toe-in stereo pairs with an elevation lower
that |θ0| ∼50◦. The tests also revealed that sTi stereo
pairs provide more depth structure around the data it-
self as compared to their equivalent Oﬀset stereo pairs,
and that the sTi method is in that respect more appro-
priate for creating stereo pairs in Astrophysics, a fact
already observed by Peterka et al. (2009).
We have then used three examples, one idealized
and two realistic, with which we have presented var-
ious types of stereo pairs, highlighted several aspects of
stereoscopic visualization, and identiﬁed the main ben-
eﬁts of using stereo pairs as a complement to more stan-
dard plotting techniques in a publication. First, they
are a polyvalent tool that is adaptable to one’s needs;
their shape, size, and color can be adapted to best re-
veal the 3D data set without impacting the ability to
transmit a depth perception to the viewer.
Second,
they proﬁt any multivariate data set, observational or
theoretical, and potentially beneﬁt diﬀerent genres of
studies (e.g., of both the theoretical and observational
kind). Third, they greatly facilitate the communication
of complex 3D shapes. Especially, where a text descrip-
tion might be subject to interpretation, stereo pairs can
force upon the viewer a unique view of the data set,
thereby avoiding misconceptions. This is possibly the
main factor that should dictate the use of stereoscopy
in publications and presentations.
For all these reasons, stereo pairs should be consid-
ered a valuable tool for the Astrophysics community -
a ﬁeld where most data sets are multidimensional and
multivariate, and where stereo pairs can be applied to
many diﬀerent sub-topics, but always with the common
aim of simplifying, clarifying, and eliminating miscon-
ceptions. The evolution of informatics has made stereo
pairs aesthetic, useful, and straightforward to produce.
We are convinced that they have a promising future,
given the rapid evolution of 3D visualization hardware
and techniques, e.g. 3D televisions. Although we still
lack a standardized API and user-friendly software to
couple the stereo images to the display devices, these
will likely be provided as soon as the need is identiﬁed.
Sharing astrophysical data sets in 3D on hand-held de-
vices might sound futuristic. Nonetheless, stereo pairs
can already be easily stacked into a movie, and played
during a talk in a lecture theatre equipped with 3D pro-
jection abilities, enabling the audience to experience a
glimpse of the 3D future for Astrophysics. In conclu-
sion, we are convinced that the ideas conceived through
the ongoing 3D trend currently occurring in the non-
scientiﬁc community can and ought to be used in Astro-
physics. Stereo pairs are a good way to start opening
our minds today.
Acknowledgements
We thank the referee for his/her comments that
helped greatly improve this paper. This research has
made use of NASA’s Astrophysics Data System. Part
of this research was undertaken on the NCI National Fa-
cility at the Australian National University and some
software used in this work were in part developed by
the DOE-supported ASC / Alliance Center for Astro-
physical Thermonuclear Flashes at the University of
Chicago.
References
Ackermann, G.K., Eichler, J.: Holography: a Practical Ap-
proach. Wiley-VCH Verlag GmbH & Co. KGaA, Wein-
heim (2007)
Barker, H.W., Wiellicki, B.A., Parker, L.: A Parametriza-
tion for Computing Grid-Averaged Solar Fluxes for In-
homogeneous Marine Boundary Layer Clouds. Part II:
Validation Using Satellite Data. Journal of Atmospheric
Sciences 53, 2304-2316 (1996)
Barnes, D.G., Fluke, C.J., Bourke, P.D., Parry, O.T.: An
Advanced, Three-Dimensional Plotting Library for As-
tronomy. Publications of the Astronomical Society of Aus-
tralia 23, 82-93 (2006)
Barnes, D.G., Fluke, C.J.: Incorporating interactive three-
dimensional graphics in astronomy research papers. New
Astronomy 13, 599-605 (2008)
van den Bergh, S.: The Magellanic Clouds, Past, Present
and Future - A Summary of IAU Symposium No. 190.
New Views of the Magellanic Clouds 190, 569 (1999)
Berry, C., Baker, M.D.: Inside Protein Structures, Teaching
in Three Dimensions. Biochemistry and Molecular Biol-
ogy Education 38, 425-429 (2010)
Bicknell, G.V.: A model for the surface brightness of a tur-
bulent low Mach number jet. I - Theoretical development
and application to 3C 31. Astrophys. J. 286, 68-87 (1984)
Blondin, J.M., Mezzacappa, A., DeMarina, C.: Stability of
Standing Accretion Shocks, with an eye towards Core-
Collapse Supernovae. Astrophys. J. 584, 971-980 (2003)
Darrah, W.C.:
The World of Stereographs. Land Yacht
Press, Nashville, Tennessee (1977)
Dodgson, N.A.: Variation and extrema of the human inter-
pupillary distance. Proc. SPIE 5291: Stereoscopic Dis-
plays and Virtual Reality Systems XI, 36-46 (2010)
Dopita, M., Hart, J., McGregor, P., Oates, P., Bloxham, G.,
Jones, D.: The Wide Field Spectrograph (WiFeS). Astro-
phys. Space Sci. 310, 255-268 (2007)
Dopita, M., Rhee, J., Farage, C., McGregor, P., Blox-
ham, G., Green, A., Roberts, B., Nielson, J., Wilson, G.,
Young, P., Firth, P., Busarello, G., Merluzzi, P.: The
Wide Field Spectrograph (WiFeS): Performance and Data
Reduction. Astrophys. Space Sci. 327, 245-257 (2010)
Federrath, C., Klessen, R.S., Schmidt, W.:
The Fractal
Density Structure in Supersonic Isothermal Turbulence:
Solenoidal Versus Compressive Energy Injection. Astro-
phys. J. 692, 364-374 (2009)
Fenn, J., Raskino, M.: Mastering the Hype Cycle; How to
Choose the Right Innovation at the Right Time. Harvard
Business Press, Boston (2008)


## Page 11


11
Fryxell, B., Olson, K., Ricker, P., Timmes, F.X., Zin-
gale, M., Lamb, D.Q., MacNeice, P., Rosner, R., Tru-
ran, J.W., Tufo, H.: FLASH: An Adaptive Mesh Hydro-
dynamics Code for Modeling Astrophysical Thermonu-
clear Flashes. Astrophys. J. Suppl. Ser. 131, 273-334
(2000)
Fluke, C.J., Bourke, P.D., O’Donovan, D.: Future Direc-
tions in Astronomy Visualization. PASA 23, 12-24 (2006)
Hamilton, W.C.: The Revolution in Crystallography. Sci-
ence 169, 133-141 (1970)
Hardman, K.D., Ainswort, C.F.:
Binding of Nonpolar
Molecules by Crystalline Concanavalin-A. Biochemistry
12, 4442-4448 (1973)
Hayman, H.J.G.: The Mounting of Stereo Slides for Project-
ing Molecular Models. Journal of Chemical Education 64,
1041-1042 (1987)
Holliman, N.: Cosmic origins: experiences making a stereo-
scopic 3D movie. Proc. SPIE 7524: Stereoscopic Displays
and Applications XXI, (2010)
Icke, V., van de Weygaert, R.: The galaxy distribution as a
Voronoi foam. Q. J. R. Astron. Soc. 32, 85-112 (1991)
Jaumann, R., Neukum, G., Behnke, T., Duxbury, T.C.,
Eichentopf, K., Flohrer, J., Gasselt, S.V., Giese, B.,
Gwinner, K., Hauber, E., Hoﬀmann, H., Hoﬀmeister, A.,
K¨ohler, U., Matz, K.-D., McCord, T.B., Mertens, V.,
Oberst, J., Pischel, R., Reiss, D., Ress, E., Roatsch, T.,
Saiger, P.,
Scholten, F.,
Schwarz, G.,
Stephan, K.,
W¨ahlisch, M., the HRSC Co-Investigator Team1: The
high-resolution stereo camera (HRSC) experiment on
Mars Express: Instrument aspects and experiment con-
duct from interplanetary cruise through the nominal mis-
sion. Planet. Space Sci. 55, 928-952 (2007)
Keszthelyi, L., Jaeger, W., McEwen, A., Tornabene, L.,
Beyer, R.A., Dundas, C., Milazzo, M.: High Resolution
Imaging Science Experiment (HiRISE) images of volcanic
terrains from the ﬁrst 6 months of the Mars Reconnais-
sance Orbiter Primary Science Phase. Journal of Geo-
physical Research (Planets) 113, 4005 (2008)
Koutchmy, S. Molodenskii, M.M.: Three-dimensional image
of the solar corona from white-light observations of the
1991 eclipse. Nature 360, 717-719 (1992)
Landsberg, M.J., Moran-Jones, K., Smith, R.: Molecular
recognition of an RNA traﬃcking element by hetero-
geneous nuclear ribonucleoprotein A2. Biochemistry 45,
3943-3951 (2006)
Lasker, B.M.: Studies of N132 D - A supernova remnant in
the LMC. II - The rapidly moving material. Astrophys. J.
237, 765-768 (1980)
Lemmon, M.T., Smith, P.H., Shinohara, C., Tanner, R.,
Woida, P., Shaw, A., Hughes, J., Reynolds, R., Woida, R.,
Penegor, J., Oquest, C., Hviid, S.F., Madsen, M.B.,
Olsen, M., Leer, K., Drube, L., Morris, R.V., Britt, D.T.:
The Phoenix Surface Stereo Imager (SSI) Investigation.
Lunar and Planetary Institute Science Conference Ab-
stracts 39, 2156 (2008)
Lewis, G.M., Austin, P.H.: An Iterative Method for Gener-
ating Scaling Log-Normal Simulations. 11th Conference
on Atmospheric Radiation, 123-126 (2002)
Martinet, L., Magnenat, P.: Invariant surfaces and orbital
behaviour in dynamical systems with 3 degrees of free-
dom. Astron. Astrophys. 96, 68-77 (1981)
Martinet, L., Magnenat, P., Verhulst, F.: On the Number
of Isolating Integrals in Resonant Systems with 3-Degrees
of Freedom. Celestial Mechanics 25, 93-99 (1981)
McEwen, A.S., Eliason, E.M., Bergstrom, J.W., Bridges, N.T.,
Hansen, C.J., Delamere, W.A., Grant, J.A., Gulick, V.C.,
Herkenhoﬀ, K.E., Keszthelyi, L., Kirk, R.L., Mellon, M.T.,
Squyres, S.W., Thomas, N., Weitz, C.M.:
Mars Re-
connaissance Orbiter’s High Resolution Imaging Science
Experiment (HiRISE). Journal of Geophysical Research
(Planets) 112, 5 (2007)
Morse, J.A., Winkler, P.F., Kirshner, R.P.: Spatially Re-
solved Kinematics and Longslit Spectroscopy of the
Young, Oxygen-Rich Supernova Remnant N132D in the
Large Magellanic Cloud. Astron. J. 109, 2104 (1995)
Neukum, G., Jaumann, R., Hoﬀmann, H., Hauber, E.,
Head, J.W., Basilevsky, A.T., Ivanov, B.A., Werner, S.C.,
van Gasselt, S., Murray, J.B., McCord, T., HRSC Co-
Investigator Team:
Recent and episodic volcanic and
glacial activity on Mars revealed by the High Resolution
Stereo Camera. Nature 432, 971-979 (2004)
Norling, J.A.: The Stereoscopic Art - A Reprint Journal of
the Society of the Motion Picture and Television Engi-
neers ITS 60, 268-308 (1953)
Okoshi, T.: Three-Dimensional Imaging Techniques. Aca-
demic Press Inc., New York, New York (1976)
Onural, L., Sikora, T., Ostermann, J., Smolic, A., Civan-
lar, M.R., Watson, J.: An Assessment of 3DTV Tech-
nologies. NAB BEC Proceedings, 456-467 (2006)
Perrier, G.: Le Centenaire de Niepce. L’Astronomie 48, 77-
86 (1934)
Peterka, T., Ross, R., Yu, H., Ma, K., Kooima, R., Gi-
rado, J.: Autostereoscopic Display of Large-Scale Scitifc
Visualization. Proc. SPIE 7237: Stereoscopic Displays
and Applications XX (2009)
Pujadas, G., Palau, J. : Molecular mimicry of substrate
oxygen atoms by water molecules in the β-amylase active
site. Protein Science 10, 1645-1657 (2001)
Rhee, G.F.R.N., van Haarlem, M.P., Katgert, P.: A study
of the elongation of Abell clusters. II - A sample of 107
rich clusters. Astron. Astrophys. Suppl. Ser. 91, 513-554
(1991)
Robinson, T.: Making Stereo Pair Views with Molecular
Editor. Journal of Chemical Education 66, A62 (1989)
Saxton, C.J., Bicknell, G.V., Sutherland, R.S., Midgley, S.:
Interactions of jets with inhomogeneous cloudy media.
Mon. Not. R. Astron. Soc. 359, 781-800 (2005)
Scripture, E.W.: Anaglyphs and Stereoscopic Projection.
Science 10, 185-187 (1899)
Selman, F., Melnick, J., Bosch, G., Terlevich, R.: The ion-
izing cluster of 30 Doradus. I. Internal reddening from
NTT photometry and multi-object spectroscopy. Astron.
Astrophys. 341, 98-109 (1999)
Selman, F., Melnick, J., Bosch, G., Terlevich, R.: The ioniz-
ing cluster of 30 Doradus. III. Star-formation history and
initial mass function. Astron. Astrophys. 347, 532-549
(1999)
Sharif, L., Sharif, N., Ahmed, M.: 3-D Television. Interna-
tional Journal of Research and Reviews in Information
Sciences 1, 39-41 (2011)


## Page 12


12
Sherman, W.R., O’Leary, P., Whiting, E.T., Grover, S.,
Wernert, E.A.: IQ-Station: A Low Cost Portable Immer-
sive Environment. Proceedings of the International Sym-
posium on Visual Computing 2, 361-372 (2010)
Sirko, E., Goodman, J., Knapp, G.R., Brinkmann, J.,
Ivezi´c, ˇZ., Knerr, E.J., Schlegel, D., Schneider, D.P.,
York, D.G.: Blue Horizontal-Branch Stars in the Sloan
Digital Sky Survey. I. Sample Selection and Structure in
the Galactic Halo. Astron. J. 127, 899-913 (2004)
Smith, J.: The discoverer of photography. Nature 16, 501
(1877)
Smith, I.: Stereoviewing: Visual Aids for Stereochemistry
and Macromolecular Structures. Royal Institute of Chem-
istry Reviews 4, 19-33 (1971)
Smith, H.M.: Principles of Holography. John Wiley & Sons,
New York (1975)
Smith, P.H., Tomasko, M.G., Britt, D., Crowe, D.G.,
Reid, R., Keller, H.U., Thomas, N., Gliem, F., Ruef-
fer, P., Sullivan, R., Greeley, R., Knudsen, J.M., Mad-
sen, M.B., Gunnlaugsson, H.P., Hviid, S.F., Goetz, W.,
Soderblom, L.A., Gaddis, L., Kirk, R.: The imager for
Mars Pathﬁnder experiment. J. Geophys. Res. 102, 4003-
4026 (1997)
Sofue, Y.: Fate of the Magellanic Stream. Publ. Astron. Soc.
Jpn. 46, 431-440 (1994)
Stockert, J.C.: Stereoscopy of Computer-Drawn Molecular
Structures. Biochemical Education 22, 23-25 (1994)
Sutherland, R.S., Bicknell, G.V.: Interactions of a Light
Hypersonic Jet with a Nonuniform Interstellar Medium.
Astrophys. J. Suppl. Ser. 173, 37-69 (2007)
Tyler, C.W., Clarke, M.B.: Autostereogram. SPIE Confer-
ence Series 1256, 182-197 (1990)
Vogt, F., Dopita, M.A.: The Cas A-like SNR 1E 0102.2-7219
in the Small Magellanic Cloud: An Asymmetric Bipolar
Explosion. Astrophys. J. 721, 587-606 (2010)
Vogt, F., Dopita, M.A.: The 3D structure of N132D in the
LMC: a late-stage young supernova remnant. Astrophys.
Space Sci. 331, 521-535 (2011)
Wagner, A.Y., Bicknell, G.V.: Relativistic Jet Feedback in
Evolving Galaxies. Astrophys. J. 728, 29 (2011)
van de Weygaert, R., Icke, V.: Fragmenting the universe.
II - Voronoi vertices as Abell clusters. Astron. Astrophys.
213, 1-9 (1989)
Wheatstone, C.: Contributions to the Physiology of Vision.
Part the First. On Some Remarkable, and Hitherto Unob-
served, Phenomena of Binocular Vision. Royal Society of
London Philosophical Transactions Series I 128, 371-394
(1838)
Woods, A., Docherty, T., Koch, R.: Image Distortions in
Stereoscopic Videa Systems. Proc. SPIE 1915: Stereo-
scopic Displays and Applications IV, 36-48 (1993)
Xiang, K., Nagaike, T., Xiang, S., Turgay, K., Beh, M.M.,
Manley, J.L,
Tong, L: Crystal structure of the human
symlekin-Ssu72-CTD phosphopeptide complex. Nature
467, 729-733 (2010)
Yahil, A., Sandage, A., Tammann, G.A.: The velocity ﬁeld
of bright nearby galaxies. III - The distribution in space
of galaxies within 80 megaparsecs - The north galactic
density anomaly. Astrophys. J. 242, 448-468 (1980)
York , D.G., Adelman , J., Anderson , Jr., J.E., Anderson
, S.F., Annis , J., Bahcall , N.A., Bakken , J.A., Bark-
houser , R., Bastian , S., Berman , E., Boroski , W.N.,
Bracker , S., Briegel , C., Briggs , J.W., Brinkmann , J.,
Brunner , R., Burles , S., Carey , L., Carr , M.A., Cas-
tander , F.J., Chen , B., Colestock , P.L., Connolly , A.J.,
Crocker , J.H., Csabai , I., Czarapata , P.C., Davis , J.E.,
Doi , M., Dombeck , T., Eisenstein , D., Ellman , N.,
Elms , B.R., Evans , M.L., Fan , X., Federwitz , G.R.,
Fiscelli , L., Friedman , S., Frieman , J.A., Fukugita , M.,
Gillespie , B., Gunn , J.E., Gurbani , V.K., de Haas , E.,
Haldeman , M., Harris , F.H., Hayes , J., Heckman , T.M.,
Hennessy , G.S., Hindsley , R.B., Holm , S., Holmgren
, D.J., Huang , C.-h., Hull , C., Husby , D., Ichikawa
, S.-I., Ichikawa , T., Ivezi´c , ˇZ., Kent , S., Kim , R.S.J.,
Kinney , E., Klaene , M., Kleinman , A.N., Kleinman , S.,
Knapp , G.R., Korienek , J., Kron , R.G., Kunszt , P.Z.,
Lamb , D.Q., Lee , B., Leger , R.F., Limmongkol , S.,
Lindenmeyer , C., Long , D.C., Loomis , C., Loveday , J.,
Lucinio , R., Lupton , R.H., MacKinnon , B., Mannery
, E.J., Mantsch , P.M., Margon , B., McGehee , P., McKay
, T.A., Meiksin , A., Merelli , A., Monet , D.G., Munn
, J.A., Narayanan , V.K., Nash , T., Neilsen , E., Neswold
, R., Newberg , H.J., Nichol , R.C., Nicinski , T., Nonino
, M., Okada , N., Okamura , S., Ostriker , J.P., Owen , R.,
Pauls , A.G., Peoples , J., Peterson , R.L., Petravick , D.,
Pier , J.R., Pope , A., Pordes , R., Prosapio , A., Rechen-
macher , R., Quinn , T.R., Richards , G.T., Richmond
, M.W., Rivetta , C.H., Rockosi , C.M., Ruthmansdor-
fer , K., Sandford , D., Schlegel , D.J., Schneider , D.P.,
Sekiguchi , M., Sergey , G., Shimasaku , K., Siegmund
, W.A., Smee , S., Smith , J.A., Snedden , S., Stone , R.,
Stoughton , C., Strauss , M.A., Stubbs , C., SubbaRao
, M., Szalay , A.S., Szapudi , I., Szokoly , G.P., Thakar
, A.R. Tremonti , C., Tucker , D.L., Uomoto , A., Van-
den Berk , D., Vogeley , M.S. Waddell , P., Wang , S.-i.,
Watanabe , M., Weinberg , D.H., Yanny , B., Yasuda
, N.: The Sloan Digital Sky Survey: Technical Summary.
Astron. J.120, 1579-1587 (2000)
Zone, R.: Stereoscopic cinema and the origins of 3-D ﬁlm,
1838-1952. The University Press of Kentucky, Lexington,
Kentucky (2007)
This 2-column preprint was prepared with the AAS LATEX macros
v5.2.


## Page 13


13
A Simpliﬁed Toe-in, Toe-in and Oﬀset : a comparison of diﬀerent stereo pairs creation methods
with Python.
We have introduced the simpliﬁed Toe-in (sTi) method, described in Sect. 3, as an alternative to the oﬃcial
Toe-in and Oﬀset methods for creating stereo pairs.
The sTi method accounts for the current limitations of
Matplotlib, the Python plotting library. The main limitation lies in the fact that the viewpoint towards a 3D
plot is deﬁned by only two parameters, the azimuth φ and the elevation θ. This makes it impossible to create
proper Toe-in or Oﬀset stereo pairs directly, for reasons highlighted below (see Appendix A.1). Nonetheless, our
sTi stereo pairs provide an excellent depth perception, especially when −50◦≤θ ≤50◦, and are not more diﬃcult
or tiring to visualize as compared to their equivelent Toe-in stereo pairs, according to our small survey of Mount
Stromlo students and astronomers.
In Appendix A.4, we provide a comparison chart of sTi, Toe-in and Oﬀset stereo pairs for varying elevations.
But let us start by describing the issues of sTi stereo pairs, and the required Python code updates to create
Toe-in and Oﬀset stereo pairs.
A.1 sTi stereo pairs
As we deﬁned in Sec. 3, the LHS and RHS projection viewpoints for the sTi method are located at SL(φ0 −δ0
2 ; θ0)
and SR(φ0 + δ0
2 ; θ0), with 2.5◦≤δ0 ≤5◦the opening angle in between the LHS and RHS viewpoint. A schematic
of the situation in shown in Fig. 8, which shows the location of the viewpoints on the visualization sphere. By
default in Matplotlib, the sphere is centred on the middle of the data set, and its radius is ten times the size of
the data set.
This deﬁnition of the sTi LHS and RHS viewpoints makes it easy to use the Axes3D instance, which can take
the elevation and azimuth as parameters. However, it introduces two mistakes compared to the oﬃcial Toe-in
method :
1. The distance in between the SL and SR points, measured along the Great Circle to which they belong (the red
line in Fig. 8), is decreasing with increasing elevation.
2. The orientation of the LHS and RHS views, which by default are oriented towards the z-axis (i.e. along the
orange lines) is :
• not parallel between the LHS and RHS viewpoints.
• not perpendicular to the red great Circle (as it ought to be).
• varying with elevation.
In other words, with increasing elevation, the sTi LHS and RHS projection points will move along the orange
lines, slowly merging towards each other - the cause of the diminishing feeling of depth beyond ±50◦. The mismatch
in the view rotation, increasing from 0 to δ0/2 at θ0 = 90◦for each view, is however small enough at any elevation
not to be very noticeable.
A.2 Toe-in stereo pairs
To produce Toe-in stereo pairs, we have updated the source code of the Axes3d instance of the mplot3d toolkit,
so as to be able to rotate the projection orientation around the view axis. Using spherical trigonometry, one can
show that for a central viewpoint P(φ0; θ0), the LHS and RHS projection need to be made from the position
TL(φ0 −δ1
2 ; θ1) and TR(φ0 + δ1
2 ; θ1) with a respective rotation of ϵT and −ϵT around the view axis, where :
θ1
=
π
2 −arccos

cos(δ0
2 ) cos(π
2 −θ0)

(A1)
δ1
=
2 × arccos

cos(δ0
2 ) −cos(π
2 −θ0) cos(π
2 −θ1)

·
1
sin( π
2 −θ0) sin( π
2 −θ1)

(A2)
ϵT
=
sin(π
2 −θ0) ·
1
sin( π
2 −θ1)
(A3)
The TL and TR viewpoints are shown in Fig. 8. They will move along the light blue lines, always keeping a
ﬁxed δ0 separation at any elevation, as measured along the Great Circle they belong to (dark blue line). The


## Page 14


14
Fig. 8 : Global (left) and close-up (right) schematics depicting the LHS and RHS camera positions for both an
sTi (points SL and SR) and Toe-in (points TL and TR) stereo pair. The viewpoints associated with the sTi method
(resp. Toe-in method) move along the orange (respect. light blue) line with varying elevation.
rotation error ±ϵT of the views (initially oriented along the purple line, but which is corrected by the introduction
of a rotation matrix within the plotting source code) increases with elevation, and is as high as 90◦for θ0 = 90◦.
Because the sTi viewpoints converge towards each other at high elevations, their respective projection’s rotation
error remains small ( ∼δ0/2) compared to the Toe-in projections - and hence for high elevations we do not require
an update of the plotting source code to produce comfortable sTi stereo pairs!
A.3 Oﬀsets stereo pairs
Implementing the Oﬀset method is more complicated in Python, and requires much more involved modiﬁcations
of the plotting code. Instead, we adopted the following, more simplistic, approach. We applied the following
transformation to our data cube :
(x; y; z)
→
(x −η sin(φ0); y + η cos(φ0); z)
(A4)
(x; y; z)
→
(x + η sin(φ0); y −η cos(φ0); z)
(A5)
where η is a scale factor deﬁning the intensity of the oﬀset. In words, we apply a linear translation to the data,
perpendicular to the view axis. This method has the disadvantage to disconnect the data from the axes, however,
it is enough to get an idea of the quality of Oﬀset stereo pairs (and observe that the data itself has less depth
content than in Toe-in stereo pairs).
A.4 Comparison table : sTi vs Toe-in vs Oﬀset stereo pairs
In Fig. 9 and Fig. 10, we present stereo pairs produced with Python using the sTi, Toe-in, and Oﬀset method
described previously. Furthermore, we also include a control stereo pair, where we have set identical LHS and RHS
images, and that consequently contains no depth information at all. We are aware that by looking long enough at
those stereo pairs, the brain will start inducing a wrong depth perception, not directly present in the image5; the
control stereo pair hence tests that one does not guess, rather than see, depth information. All stereo pairs have
been produced at an azimuth φ0 = 45◦, and varying values for the elevation θ0 ∈[0◦; 20◦; 50◦; 80◦]. In every case,
the green (big) sphere is on top, and the symmetry axis of the system lies in the XZ plane.
Comparing the Oﬀset and Toe-in stereo pairs ﬁrst, one notices that, as expected, the double sphere structure
appears to hover over the axes (located further away) in the former ones.
This a direct consequence of our
5having the stereo pairs in color might also induce some additional depth perception for this comparative study, but we decided that
they might help the non-experienced stereo pairs user to see and feel our conclusions - the main aim of this Appendix.


## Page 15


15
Fig. 9 : STi, Toe-in, Oﬀset and control stereo pairs for an azimuth φ0 = 45◦and elevations θ0 = 0◦and θ0 = 20◦.
simplistic implementation of the Oﬀset method - it is accurate for the data points, but not for the background
axes. Nonetheless, focusing on the double-sphere structure itself, it has noticeably less depth elongation in the
case of the Oﬀset method. In the Toe-in stereo pairs, not only do the axes wrap around the data points nicely,
but the data points themselves appear with a strong feeling of depth. In that sense, we believe the Toe-in method
to be much more appropriate for the publication of Astrophysical data cubes, as it provides more depth structure
to the data itself.
Comparing the sTi stereo pairs with their equivalent Toe-in pairs, it can be seen that depth perception within
the sTi image is gradually degraded as the elevation increases. As mentioned above, this is due to the fact that
the LHS and RHS sTi projection viewpoints gradually move towards each other at higher elevation. Nonetheless,
some degree of depth perception is present, even as high as θ0 = 80◦. The diﬀerent orientation of the LHS and
RHS images are also staying small, and hence do not need to be corrected by any modiﬁcation of the Matplotlib
source code. In summary, our suggested sTi plotting method, if theoretically not correct, nevertheless appears in
practice to provide (very) satisfactory results, and can be directly implemented using Python, Matplotlib and
mplot3d.
The experienced Python user might ﬁnd it easy to update his source code to create correct Toe-in stereo pairs.
We intend to include our code update in future releases of Matplotlib. Until we manage to do so, we are
happy to provide our source code modiﬁcations to the interested user directly (which does not require extensive
knowledge of Python to be implemented); simply contact F.V. at fvogt@mso.anu.edu.au.


## Page 16


16
Fig. 10 : Idem as Fig. 9, but for θ0 = 50◦and θ0 = 80◦

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]