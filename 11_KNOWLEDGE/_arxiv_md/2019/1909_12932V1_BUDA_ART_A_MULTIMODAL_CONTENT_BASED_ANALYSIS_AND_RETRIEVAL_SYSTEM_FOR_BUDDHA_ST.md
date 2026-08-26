---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.12932v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1909.12932v1_BUDA_ART__A_Multimodal_Content-Based_Analysis_and_Retrieval_System_for_Buddha_St

> Source: 1909.12932v1_BUDA_ART__A_Multimodal_Content-Based_Analysis_and_Retrieval_System_for_Buddha_St.pdf

> Pages: 3

---


## Page 1


BUDA.ART: A Multimodal Content-Based Analysis
and Retrieval System for Buddha Statues
Benjamin Renoust, Matheus Oliveira Franca,
Jacob Chan, Van Le, Ayaka Uesaka,
Yuta Nakashima, Hajime Nagahara
renoust@ids.osaka-u.ac.jp
Institute for Datability Science, Osaka University
Osaka, Japan
Jueren Wang
Yutaka Fujioka
fujioka@let.osaka-u.ac.jp
Graduate School of Letters, Osaka University
Osaka, Japan
Figure 1: An overview of the BUDA.ART system, from search, to exploration and 3D visualization.
ABSTRACT
We introduce BUDA.ART, a system designed to assist researchers
in Art History, to explore and analyze an archive of pictures of
Buddha statues. The system combines different CBIR and classical
retrieval techniques to assemble 2D pictures, 3D statue scans and
meta-data, that is focused on the Buddha facial characteristics. We
build the system from an archive of 50,000 Buddhism pictures,
identify unique Buddha statues, extract contextual information,
and provide specific facial embedding to first index the archive. The
system allows for mobile, on-site search, and to explore similarities
of statues in the archive. In addition, we provide search visualization
and 3D analysis of the statues.
CCS CONCEPTS
• Information systems →Search interfaces; Multimedia and
multimodal retrieval; Data cleaning; • Human-centered com-
puting →Visualization systems and tools; • Applied com-
puting →Fine arts.
KEYWORDS
Art History, Multimedia Database, Search system, 2D, 3D
Permission to make digital or hard copies of part or all of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
MM ’19, October 21–25, 2019, Nice, France
© 2019 Copyright held by the owner/author(s).
ACM ISBN 978-1-4503-6889-6/19/10.
https://doi.org/10.1145/3343031.3350591
1
INTRODUCTION
The spread and evolution of Buddhism across Asia is the topic of
many books [19, 27]. Multiple theories are confronting on which
path(s) this spread took place across the Asian subcontinent, reach-
ing the coasts of the Japanese archipelago along the Silk Road [15,
19, 21, 27]. Buddhism brought many works of art and their rules so
that local people would craft new artworks by themselves. giving
their identity to the resulting style [16]. Nowadays, only a few ex-
perts can identify these works subjective to their own knowledge,
sometimes disputing explanations [10].
In order to investigate Buddhism at a large scale, we analyze a
large archive of Buddhism related documents through the produced
art. To do so, we focus on the representation of Buddha, which
is central to Buddhism art. Although their exist statues of many
different types, their construction respects canons1 which have
been normalized over the centuries. Despite the rules, time and
travels allowed for quite an evolution among the style of statues,
and aligning many of these statues may allow us to capture the
traces of this evolution [26].
Using modern face detection and recognition [24], we focus on
the faces of Buddha. Our experts have accumulated a large amount
of photos and pictures related to Buddhism, that they cannot bring
with them every time they visit a temple or museum, even less hav-
ing an overview of their collection. Statues are 3D objects but 2D
pictures usually poorly convey their spatial structure. So we build
BUDA.ART (for Buddha Archive Anaysis and Retrieval, Fig. 1)
a web-based system that combines and deliver all three aspects:
knowledge/metadata, 2D pictures, and 3D structure, such that ex-
perts can query, search, and explore Buddha statues even on field.
1A canon of art refers to a universal set of rules and principles establishing the funda-
mentals and/or optimal.
arXiv:1909.12932v1  [cs.CV]  17 Sep 2019


## Page 2


Such a retrieval system allows to explore a query space similarly to
Barthel’s map [1], while it shares components of a CBIR [7], it also
provides hyperlinking as in for news video [5], with new dedicated
classifiers and 3D structure analysis for Buddha statues.
2
DATA PREPROCESSING
Our co-authors, experts in Art History from the Graduate School of
Letters, have accumulated over 50,000 pictures of all kinds (about
500GB in total) in a semi-organized manner. They have been cap-
tured under many conditions, mainly: museum collection pieces
acquired with standard methods, on-site captures in museum or
temple, carefully captured Buddhist art treasures, outside field trips,
and scans of dedicated literature.
This is real data “in-the-wild”: multiple size and formats; picture
redundancy; not all pictures contain Buddha statues; a same statue
can be taken across many angles and lights; multiple statues or
subpictures in one picture; pictures can be a detail of larger artifact;
this detail itself can be representation of Buddha. The pictures are
not annotated (nor localized in EXIF), but they may be attached to
indirect contextual information: it may be in their filename, or in
their folders (over 1.7k different folders). We could extract some
amount of contextual knowledge from this structure.
We first cleaned the dataset by removing near-duplicates using
VGG16 [20] embeddings, and used a t-SNE [11] 2D projection to
visualize the space of the remaining pictures ( 20k pictures, of
which 10k with a duplicate), so we could easily remove all non-
relevant pictures. We created chains of pictures based on their
creation order and cosine similarity to assign them to single Buddha
statues. Similar (or duplicate) pictures were matched across chains
(and folders) in an nearest neighbor graph to assemble same statues
spread in different folders. A final round of manual annotation of
this graph visualization allowed us to identify 3685 unique Buddha
statues, among them we consider 804 statues with at least 5 pictures
covering 17k pictures.
We extracted text content from 1.7k folder names and filenames,
filtered locations and era when available, thus bringing context
metadata when possible to the 804 statues. We automatically recov-
ered 366 statue with types, 672 with country, 461 with regions, and
460 with cities in which the statues were taken, 113 with countries,
104 with regions and 102 with cities of origin of the statues, 98 with
construction eras, and 89 with temples.
For this archive, we first mined faces with the Faster R-CNN [22],
and manually corrected all annotations to form a ground truth of
1847 face pictures for the selected statues, that we used to fine tune
the faster R-NN model (included RPN + VGG16) initially trained
on Imagenet [3]. We additionally use the VGGFace2 [2] trained
ResNet50 [8] model fine-tuned with our ground truth to compute
face embedding.
3
RETRIEVAL AND ANALYSIS
We may now build the retrieval system to support experts when
confronting statues. It is based on top of elasticsearch [4] for text-
based search and exploration (that is full text search from our
extracted metadata, image path, and other user defined properties),
and an image similarity search, as proposed by FAISS [9] for image
search and comparison. To further extend search, two types of
Figure 2: Label prediction and structure analysis.
embeddings are used: full image embeddings with Imagenet-trained
VGG16 [20] help to search pictures from their global information
(for example, statues of similar shapes); face-dedicated embeddings
with our fine-tuned ResNet50 [8] to search for statues by their face
and propose label prediction from our classifier [17] (Fig. 2a).
Users may then search statues by text or image and face (Fig. 1,
a,b). Any face present in the uploaded picture is automatically sear-
ched using our Faster R-CNN model [22]. Users can additionally
manually input a search area. Individual access to the results pre-
sents all the properties of a statues, all other pictures, such that
experts may even edit this information. Each element of results
(image or text) is hyperlinked so it may become a new search
element and support user exploratory search.
A neighborhood map is also created for users to explore the full
content of the database (Fig. 1, c), as well as the neighborhood of a
search result. This neighborhood map is built on top of a UMAP [12]
projection of all image embeddings that constitute the search results
(or all the database).
Acquiring 3D scans is not scalable, but our experts wish to inves-
tigate the 3D structure of the faces. We offer to interpolate Buddha
faces in a 3D model using joint reconstruction and dense align-
ment [6] (Fig. 1, d). The 3D model allows us to further explore facial
landmarks, and historical facial proportions [17] (Fig. 2b).
The search system is built on a client-server architecture, on
the server side, a python Flask [18] framework encapsulates ac-
cess to all the deep neural network models, elasticsearch [4], and
FAISS [9]. The neighborhood map is made using UMAP [12] and
WebGL [13] with PixPlot [25]. The 3D representation is built on
top of three.js [14]. The web interface is built on top of UIdeck[23].
Our system is responsive so users can query it on-site from a simple
snapshot to a Buddha statue taken with any mobile device.
4
CONCLUSION
We presented a database construction down to search interface
creation of 2D and 3D representations of Buddha statues. The sys-
tem demonstrates easy on-line search of specific Buddha statues,
following user defined criteria and different picture representation,
with a query space visualization. We also demonstrate label pre-
diction, 3D reconstruction of statues, comparison, and highlight
structural feature. Experts can then query the database on-field
with a simple smart phone. The upcoming future work will add a
recommendation system based on nearest-neighbor search for each
result. We will also deploy analysis of Buddha-statue specific 3D
features on-the-fly, and add online comparison of 3D models.
Acknowledgement: Supported by JSPS KAKENHI #18H03571.


## Page 3


REFERENCES
[1] Kai Uwe Barthel, Nico Hezel, and Klaus Jung. 2017. Visually browsing millions
of images using image graphs. In Proceedings of the 2017 ACM on International
Conference on Multimedia Retrieval. ACM, 475–479.
[2] Qiong Cao, Li Shen, Weidi Xie, Omkar M Parkhi, and Andrew Zisserman. 2018.
Vggface2: A dataset for recognising faces across pose and age. In 2018 13th IEEE
International Conference on Automatic Face & Gesture Recognition (FG 2018). IEEE,
67–74.
[3] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. 2009. Imagenet:
A large-scale hierarchical image database. In 2009 IEEE conference on computer
vision and pattern recognition. Ieee, 248–255.
[4] Manda Sai Divya and Shiv Kumar Goyal. 2013. ElasticSearch: An advanced and
quick search technique to handle voluminous data. Compusoft 2, 6 (2013), 171.
[5] Maria Eskevich, Huynh Nguyen, Mathilde Sahuguet, and Benoit Huet. 2015.
Hyper video browser: Search and hyperlinking in broadcast media. In Proceedings
of the 23rd ACM international conference on Multimedia. ACM, 817–818.
[6] Yao Feng, Fan Wu, Xiaohu Shao, Yanfeng Wang, and Xi Zhou. 2018. Joint 3d face
reconstruction and dense alignment with position map regression network. In
Proceedings of the European Conference on Computer Vision (ECCV). 534–551.
[7] Paula Gomez Duran, Eva Mohedano, Kevin McGuinness, Xavier Giró Nieto,
and Noel O’Connor. 2018. Demonstration of an open source framework for
qualitative evaluation of CBIR systems. In Proceedings of 2018 ACM Multimedia
Conference, Seoul, Republic of Korea, October 22-26, 2018 (MMâĂŹ18). Association
for Computing Machinery (ACM), 1256–1257.
[8] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual
learning for image recognition. In Proceedings of the IEEE conference on computer
vision and pattern recognition. 770–778.
[9] Jeff Johnson, Matthijs Douze, and Hervé Jégou. 2017. Billion-scale similarity
search with GPUs. arXiv preprint arXiv:1702.08734 (2017).
[10] Ayano Kubo and Masakatsu Murakami. 2011. Dojidaibusshi tono hikaku niy-
oru kaikeisakuhin no tokucho nitsuite- yoshiki to horyo kara miru. IPSJ SIG
Computers and the Humanities (CH) 1 (2011), 1–6.
[11] Laurens van der Maaten and Geoffrey Hinton. 2008. Visualizing data using t-SNE.
Journal of machine learning research 9, Nov (2008), 2579–2605.
[12] Leland McInnes, John Healy, and James Melville. 2018. Umap: Uniform man-
ifold approximation and projection for dimension reduction. arXiv preprint
arXiv:1802.03426 (2018).
[13] Mozilla Foundation. 2011. WebGL. https://developer.mozilla.org/en-US/docs/
Web/API/WebGL_API Last accessed: 2019-05-20.
[14] Mr.Doob. 2011. three.js. http://threejs.org Last accessed: 2019-05-20.
[15] Takashi Nabata. 1986. Bukkyodenrai to butsuzo no densetsu. Otani Gakuho 65, 4
(1986), p1–16.
[16] Kocho Nishimura and Kozo Ogawa. 1987. Butsuzo no miwakekata. (1987).
[17] Benjamin Renoust, Matheus Oliveira Franca, Jacob Chan, Noa Garcia, Van Le,
Ayaka Uesaka, Yuta Nakashima, Hajime Nagahara, Jueren Wang, and Yutaka
Fujioka. 2019. Historical and Modern Features for Buddha Statue Classification. In
Proceedings of 2019 ACM Multimedia Conference, SUMAC Workshop. Association
for Computing Machinery (ACM), 1–8.
[18] Armin Ronacher. 2010. Flask. http://flask.pocoo.org Last accessed: 2019-05-20.
[19] Masumi Shimizu. 2013. Butsuzo no kao -Katachi to hyojo wo yomu. Iwanami
Shinsho.
[20] Karen Simonyan and Andrew Zisserman. 2014. Very deep convolutional networks
for large-scale image recognition. arXiv preprint arXiv:1409.1556 (2014).
[21] Hiromichi Soejima and Felice Fischer. 2008. A Guide to Japanese Buddhist Sculp-
ture. Ikeda Shoten.
[22] Xudong Sun, Pengcheng Wu, and Steven CH Hoi. 2018. Face detection using
deep learning: An improved faster RCNN approach. Neurocomputing 299 (2018),
42–50.
[23] UIdeck. 2014. UIdeck. https://uideck.com Last accessed: 2019-05-20.
[24] Nannan Wang, Xinbo Gao, Dacheng Tao, Heng Yang, and Xuelong Li. 2018. Facial
feature point detection: A comprehensive survey. Neurocomputing 275 (2018),
50–65.
[25] Yale DHLab. 2017. PixPlot. http://dhlab.yale.edu/projects/pixplot/ Last accessed:
2019-05-20.
[26] Osamu Yamada. 2014.
Chokokubunkazai ni mirareru zugakutekikaishaku.
Taikaigakujutsukoenrombunshu (2014), 23–28.
[27] Tsutomu Yamamoto. 2006. Butsuzo no himitsu. Asahi Shuppansha.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]