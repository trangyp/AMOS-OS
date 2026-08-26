---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1711.08774v4
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1711.08774v4_Nanopore_Sequencing_Technology_and_Tools_for_Genome_Assembly__Computational_Anal

> Source: 1711.08774v4_Nanopore_Sequencing_Technology_and_Tools_for_Genome_Assembly__Computational_Anal.pdf

> Pages: 16

---


## Page 1


arXiv:1711.08774v4  [q-bio.GN]  6 Mar 2018
Nanopore Sequencing Technology and Tools for
Genome Assembly: Computational Analysis of the
Current State, Bottlenecks and Future Directions
Damla Senol Cali 1,∗, Jeremie S. Kim 1,3, Saugata Ghose 1, Can Alkan 2∗
and Onur Mutlu 3,1∗
1Department of Electrical and Computer Engineering, Carnegie Mellon University, Pittsburgh, PA, USA
2Department of Computer Engineering, Bilkent University, Bilkent, Ankara,Turkey
3Department of Computer Science, Systems Group, ETH Zürich, Zürich, Switzerland
∗To whom correspondence should be addressed.
Abstract
Nanopore sequencing technology has the potential to render other sequencing technologies obsolete with its ability to
generate long reads and provide portability. However, high error rates of the technology pose a challenge while generating
accurate genome assemblies. The tools used for nanopore sequence analysis are of critical importance as they should
overcome the high error rates of the technology. Our goal in this work is to comprehensively analyze current publicly available
tools for nanopore sequence analysis to understand their advantages, disadvantages, and performance bottlenecks. It is
important to understand where the current tools do not perform well to develop better tools. To this end, we 1) analyze the
multiple steps and the associated tools in the genome assembly pipeline using nanopore sequence data, and 2) provide
guidelines for determining the appropriate tools for each step. Based on our analyses, we make four key observations: 1) The
choice of the tool for basecalling plays a critical role in overcoming the high error rates of nanopore sequencing technology.
2) Read-to-read overlap ﬁnding tools, GraphMap and Minimap, perform similarly in terms of accuracy. However, Minimap
has a lower memory usage and it is faster than GraphMap. 3) There is a trade-off between accuracy and performance when
deciding on the appropriate tool for the assembly step. The fast but less accurate assembler Miniasm can be used for quick
initial assembly, and further polishing can be applied on top of it to increase the accuracy, which leads to faster overall
assembly. 4) The state-of-the-art polishing tool, Racon, generates high-quality consensus sequences while providing a
signiﬁcant speedup over another polishing tool, Nanopolish. We analyze various combinations of different tools and expose
the tradeoffs between accuracy, performance, memory usage and scalability. We conclude that our observations can guide
researchers and practitioners in making conscious and effective choices for each step of the genome assembly pipeline
using nanopore sequence data. Also, with the help of bottlenecks we have found, developers can improve the current tools
or build new ones that are both accurate and fast, in order to overcome the high error rates of the nanopore sequencing
technology.
Keywords: Nanopore sequencing, genome sequencing, genome analysis, assembly, mapping
1 Introduction
Next-generation sequencing (NGS) technologies have revolutionized
and dominated the genome sequencing market since 2005, due to their
ability to generate massive amounts of data at a faster speed and lower
cost[1–3]. Theexistenceofsuccessfulcomputationaltools thatcanprocess
and analyze such large amounts of data quickly and accurately is critically
important to take advantage of NGS technologies in science, medicine and
technology.
Since the whole genome of most organisms cannot be sequenced all at
once, the genome is broken into smaller fragments. After each fragment
is sequenced, small pieces of DNA sequences (i.e., reads) are generated.
These reads can then be analyzed following two different approaches:
read mapping and de novo assembly. Read mapping is the process of
aligning the reads against the reference genome to detect variations in
the sequenced genome. De novo assembly is the method of combining the
reads to construct the original sequence when a reference genome does not
exist [4]. Due to the repetitive regions in the genome, the short-read length
of the most dominant NGS technologies (e.g., 100-150 bp reads) causes
errors and ambiguities for read mapping [5, 6], and poses computational
challenges and accuracy problems to de novo assembly [7]. Repetitive
sequences are usually longer than the length of a short read and an entire
repetitive sequence cannot be spanned by a single short read. Thus, short
reads lead to highly-fragmented, incomplete assemblies [7–9]. However,
a long read can span an entire repetitive sequence and enable continuous
and complete assemblies. The demand for sequencing technologies that
can produce longer reads has resulted in the emergence of even newer
alternative sequencing technologies.
1


## Page 2


2
Senol Cali et al.
Nanopore sequencing technology [10] is one example of such
technologies that can produce long read lengths. Nanopore sequencing
is an emerging and a promising single-molecule DNA sequencing
technology, which exhibits many attractive qualities, and in time, it could
potentiallysurpass currentsequencingtechnologies. Nanoporesequencing
promises high sequencing throughput, low cost, and longer read length,
and it does not require an ampliﬁcation step before the sequencing process
[11–14].
Using biological nanopores for DNA sequencing was ﬁrst proposed in
the 1990s [15], but the ﬁrst nanopore sequencing device, MinION [16],
was only recently (in May 2014) made commercially available by Oxford
Nanopore Technologies (ONT). MinION is an inexpensive, pocket-sized,
portable, high-throughput sequencing apparatus that produces data in
real-time. These properties enable new potential applications of genome
sequencing, such as rapid surveillance of Ebola, Zika or other epidemics
[17], near-patient testing [18], and other applications that require real-
time data analysis. In addition, the MinION technology has two major
advantages. First, it is capable of generating ultra-long reads (e.g., 882
kilobasepairs orlonger[19, 20]). MinION’s longreads greatly simplify the
genome assembly process by decreasing the computational requirements
[8, 21]. Second, it is small and portable. MinION is named as the ﬁrst
DNA sequencing device used in outer space to help the detection of life
elsewhere in the universe with the help of its size and portability [22]. With
the help of continuous updates to the MinION device and the nanopore
chemistry, the ﬁrst nanopore human reference genome was generated by
using only MinION devices [19].
Nanopores are suitable for sequencing because they:
• Do not require any labeling of the DNA or nucleotide for detection
during sequencing,
• Rely on the electronic or chemical structure of the different nucleotides
for identiﬁcation,
• Allow sequencing very long reads, and
• Provide portability, low cost, and high throughput.
Despite all these advantageous characteristics, nanopore sequencing
has one major drawback: high error rates. In May 2016, ONT released a
new version of MinION with a new nanopore chemistry called R9 [23], to
provide higher accuracy and higher speed, which replaced the previous
version R7. Although the R9 chemistry improves the data accuracy,
the improvements are not enough for cutting-edge applications. Thus,
nanopore sequence analysis tools have a critical role to overcome high
error rates and to take better advantage of the technology. Also, faster
tools are critically needed to 1) take better advantage of the real-time data
production capability of MinION and 2) enable real-time data analysis.
Our goal in this work is to comprehensively analyze current publicly-
available tools for nanopore sequence analysis1 to understand their
advantages, disadvantages, and bottlenecks. It is important to understand
where the current tools do not perform well, to develop better tools. To this
end, we analyze the tools associated with the multiple steps in the genome
assembly pipeline using nanopore sequence data in terms of accuracy,
speed, memory efﬁciency, and scalability.
2 Genome Assembly Pipeline Using Nanopore
Sequence Data
We evaluate the genome assembly pipeline using nanopore sequence
data. Figure 1 shows each step of the pipeline and lists the associated
existing tools for each step that we analyze.
1 We note that our manuscript presents a checkpoint of the state-of-the-art
tools at the time the manuscript was submitted. This is a fast moving ﬁeld,
but we hope that our analysis is useful, and we expect that the fundamental
conclusions and recommendations we make are independent of the exact
versions of the tools.
Basecalling 
Tools: Metrichor, Nanonet, Scrappie, Nanocall, DeepNano 
Read-to-Read Overlap Finding 
Tools: GraphMap, Minimap 
Assembly 
Tools: Canu, Miniasm 
Read Mapping 
Tools: BWA-MEM, Minimap, (GraphMap) 
Raw signal 
data 
Assembly 
DNA reads 
Overlaps 
Draft assembly 
Improved 
assembly 
Polishing 
Tools: Nanopolish, Racon 
Mappings of reads 
against draft 
assembly 
Figure 1. The analyzed genome assembly pipeline using nanopore
sequence data, with its ﬁve steps and the associated tools for each
step.
The output of MinION is raw signal data that represents changes
in electric current when a DNA strand passes through nanopore. Thus,
the pipeline starts with the raw signal data. The ﬁrst step, basecalling,
translates this raw signal output of MinION into bases (A, C, G, T)
to generate DNA reads. The second step computes all pairwise read
alignments or sufﬁx-preﬁx matches between each pair of reads, called
read-to-read overlaps. Overlap-layout-consensus (OLC) algorithms are
used for the assembly of nanopore sequencing reads since OLC-algorithms
perform better with longer error-prone reads [24]. OLC-based assembly
algorithms generate an overlap graph, where each node denotes a read and
each edge represents the sufﬁx-preﬁx match between the corresponding
two nodes. The third pipeline step, genome assembly, traverses this overlap
graph, producing the layout of the reads and then constructing a draft
assembly. To increase the accuracy of the assembly, further polishing, i.e.,
post-assembly error correction, may be required. The fourth step of the
pipeline is mapping the original basecalled reads to the generated draft
assembly from the previous step (i.e., read mapping). The ﬁfth and ﬁnal
step of the pipeline is polishing the assembly with the help of mappings
from the previous step.
We next introduce the state-of-the-art tools used for each step.
2.1
Basecalling
When a strand of DNA passes through the nanopore (which is called
the translocation of the strand through the nanopore), it causes drops in
the electric current passing between the walls of the pore. The amount
of change in the current depends on the type of base passing through
the pore. Basecalling, the initial step of the entire pipeline, translates the
raw signal output of the nanopore sequencer into bases (A, C, G, T) to
generate DNA reads. Most of the current basecallers divide the raw current
signal into discrete blocks, which are called events. After event-detection,
each event is decoded into a most-likely set of bases. In the ideal case,
each consecutive event should differ by one base. However, in practice,
this is not the case because of the non-stable speed of the translocation.
Also, determining the correct length of the homopolymers (i.e., repeating
stretches of one kind of base, e.g., AAAAAAA) is challenging. Both of
these problems make deletions the dominant error of nanopore sequencing
[25, 26]. Thus, basecalling is the most important step of the pipeline that
plays a critical role in decreasing the error rate.
Weanalyzeﬁvestate-of-the-art basecallingtools inthis paper (Table1).
For a detailed comparison of these and other basecallers (including
Albacore [27], which is not freely available, and Chiron [28]), we refer
the reader to an ongoing basecaller comparison study [29]. Note that this
ongoing study does not capture the accuracy and performance of the entire
genome assembly pipeline using nanopore sequence data.
Metrichor
Metrichor [30] is ONT’s cloud-based basecaller, and its source code is
not publicly available. Before the R9 update, Metrichor was using Hidden


## Page 3


3
Markov Models (HMM) [31] for basecalling [23]. After the R9 update,
it started using recurrent neural networks (RNN) [32, 33] for basecalling
[23].
Nanonet
Nanonet [34] has also been developed by ONT, and it is available
on Github [35]. Since Metrichor requires an Internet connection and
its source code is not available, Nanonet is an ofﬂine and open-source
alternative for Metrichor. Nanonet is implemented in Python. It also uses
RNN for basecalling [34]. The tool supports multi-threading by sharing the
computation needed to call each single read between concurrent threads.
In other words, only one read is called at a time.
Scrappie
Scrappie [36] is the newest proprietary basecaller developed by ONT.
It is named as the ﬁrst basecaller that explicitly addresses basecalling
errors in homopolymer regions. In order to determine the correct length
of homopolymers, Scrappie performs transducer-based basecalling [25].
For versions R9.4 and R9.5, Scrappie can perform basecalling with the
raw current signal, without requiring event detection. It is a C-based local
basecaller and is still under development [25].
Nanocall
Nanocall [37] uses Hidden Markov Models for basecalling, and it
is independently developed by a research group. It was released before
the R9 update when Metrichor was also using an HMM-based approach
for basecalling, to provide the ﬁrst ofﬂine and open-source alternative
for Metrichor. However, after the R9 update, when Metrichor started
to perform basecalling with a more powerful RNN-based approach,
Nanocall’s accuracyfellshort ofMetrichor’s accuracy [38]. Thus, although
Nanocall supports R9 and upper versions of nanopore data, its usefulness
is limited [38]. Nanocall is a C++-based command-line tool. It supports
multi-threading where each thread performs basecalling for different
groups of raw reads.
DeepNano
DeepNano [39] is also independently developed by a research group
before the R9 update. It uses an RNN-based approach to perform
basecalling. Thus, it is considered to be the ﬁrst RNN-based basecaller.
DeepNano is implemented in Python. It does not have multi-threading
support.
2.2
Read-to-Read Overlap Finding
Previous genome assembly methods designed for accurate and short
reads (i.e., de Bruijn graph (DBG) approach [43, 44]) are not suitable for
nanopore reads because of the high error rates of the current nanopore
sequencing devices [9, 26, 45, 46]. Instead, overlap-layout-consensus
(OLC) algorithms [47] are used for nanopore sequencing reads since
they perform better with longer, error-prone reads. OLC-based assembly
algorithms start with ﬁnding the read-to-read overlaps, which is the second
step of the pipeline. Read-to-read overlap is deﬁned to be a common
sequence between two reads [46]. GraphMap [40] and Minimap [41] are
the commonly-used state-of-the-art tools for this step (Table 2).
GraphMap
GraphMap ﬁrst partitions the entire read dataset into k-length
substrings (i.e. k-mers), and then creates a hash table. GraphMap uses
gapped k-mers, i.e., k-mers that can contain insertions or deletions (indels)
[40, 48]. In the hash table, for each k-mer entry, three pieces of information
arestored: 1)k-merstring, 2)theindexoftheread, and3)thepositioninthe
read where the corresponding k-mer comes from. GraphMap detects the
overlaps by ﬁnding the k-mer similarity between any two given reads. Due
to this design, GraphMap is a highly sensitive and accurate tool for error-
prone long reads. It is a command-line tool written in C++. GraphMap is
used for both 1) read-to-read overlap ﬁnding with the graphmap owler
command and 2) read mapping with the graphmap align command.
Minimap
Minimap also partitions the entire read dataset into k-mers, but instead
of creating a hash table for the full set of k-mers, it ﬁnds the minimum
representative set of k-mers, called minimizers, and creates a hash table
with only these minimizers. Minimap ﬁnds the overlaps between two reads
by ﬁnding minimizer similarity. The goals of using minimizers are to 1)
reduce the storage requirement of the tool by storing fewer k-mers and
2) accelerate the overlap ﬁnding process by reducing the search span.
Minimap also sorts k-mers for cache efﬁciency. Minimap is fast and cache-
efﬁcient, and it does not lose any sensitivity by storing minimizers since
the chosen minimizers can represent the whole set of k-mers. Minimap
is a command-line tool written in C. Like GraphMap, it can both 1) ﬁnd
overlaps between two read sets and 2) map a set of reads to a full genome.
2.3
Genome Assembly
After ﬁnding the read-to-read overlaps,
OLC-based assembly
algorithms generate an overlap graph. Genome assembly is performed
by traversing this graph, producing the layout of the reads and then
constructing a draft assembly. Canu [42] and Miniasm [41] are the
commonly-used error-prone long-read assemblers (Table 3).
Canu
Canu performs error-correction as the initial step of its own pipeline. It
ﬁnds the overlaps of the raw uncorrected reads and uses them for the error-
correction. The purpose of error-correction is to improve the accuracy of
the bases in the reads [42, 49]. After the error-correction step, Canu ﬁnds
overlaps between corrected reads and constructs a draft assembly after an
additional trimming step. However, error-correction is a computationally
expensive step. In its own pipeline, Canu implements its own read-to-read
overlap ﬁnding tool such that the users do not need to perform that step
explicitly before running Canu. Most of the steps in the Canu pipeline
are multi-threaded. Canu detects the resources that are available in the
computer before starting its pipeline and automatically assigns number of
threads, numberofprocesses andamountofmemory basedon the available
resources and the assembled genome’s estimated size.
Miniasm
Miniasm skips the error-correction step since it is computationally
expensive. It constructs a draft assembly from the uncorrected read
overlaps computed in the previous step. Although Miniasm lowers
computational cost and thus accelerates and simpliﬁes assembly by doing
so, the accuracy of the draft assembly depends directly on the accuracy of
Table 1. State-of-the-art nanopore basecalling tools.
Tool
Strategy
Multi-threading Support
Source
Reference
Metrichor
Recurrent Neural Network
(cloud-based)
https://metrichor.com/
[30]
Nanonet
Recurrent Neural Network
with -jobs parameter
https://github.com/nanoporetech/nanonet
[34]
Scrappie
Recurrent Neural Network
with export OMP_NUM_THREADS command
https://github.com/nanoporetech/scrappie
[36]
Nanocall
Hidden Markov Model
with –threads parameter
https://github.com/mateidavid/nanocall
[37]
DeepNano Recurrent Neural Network
no support; split dataset and run it in parallel
https://bitbucket.org/vboza/deepnano
[39]


## Page 4


4
Senol Cali et al.
Table 2. State-of-the-art read-to-read overlap ﬁnding tools.
Tool
Strategy
Multi-threading Support
Source
Reference
GraphMap k-mer similarity
with –threads parameter
https://github.com/isovic/graphmap
[40]
Minimap
minimizer similarity
with -t parameter
https://github.com/lh3/minimap
[41]
Note: Both GraphMap and Minimap also have read mapping functionality.
Table 3. State-of-the-art assembly tools.
Tool
Strategy
Multi-threading Support
Source
Reference
Canu
OLC with error correction
auto conﬁguration
https://github.com/marbl/canu
[42]
Miniasm
OLC without error correction
no support
https://github.com/lh3/miniasm
[41]
the uncorrected basecalled reads. Thus, further polishing may be necessary
for these draft assemblies. Miniasm does not support multi-threading.
2.4
Read Mapping and Polishing
In order to increase the accuracy of the assembly, especially for the
rapid assembly methods like Miniasm, which do not have the error-
correction step, further polishing may be required. Polishing, i.e., post-
assembly error-correction, improves the accuracy of the draft assembly by
mapping the reads to the assembly and changing the assembly to increase
local similarity with the reads [26, 51, 52]. The ﬁrst step of polishing is
mapping the basecalled reads to the generated draft assembly from the
previous step. One of the most commonly-used long read mappers for
nanopore data is BWA-MEM [50]. Read-to-read overlap ﬁnding tools,
GraphMap and Minimap (Section 2.2), can also be used for this step,
since they also have a read mapping mode (Table 4).
After aligning the basecalled reads to the draft assembly, the ﬁnal
polishing of the assembly can be performed with Nanopolish [51] or Racon
[52] (Table 5).
Nanopolish
Nanopolish uses the raw signal data of reads along with the mappings
from the previous step to improve the assembly base quality by evaluating
and maximizing the probabilities for each base with a Hidden Markov
Model-based approach [51]. It can increase the accuracy of the draft
assembly by correcting the homopolymer-rich parts of the genome.
Although this approach can increase the accuracy signiﬁcantly,
it
is computationally expensive, and thus time consuming. Nanopolish
developers recommend BWA-MEM as the read mapper before running
Nanopolish [53].
Racon
Racon constructs partial order alignment graphs [52, 54] in order to
ﬁnd a consensus sequence between the reads and the draft assembly. After
dividing the sequence into segments, Racon tries to ﬁnd the best alignment
to increase the accuracy of the draft assembly. Racon is a fast polishing
tool, but it does not promise a high increase in accuracy as Nanopolish
promises. However, multiple iterations of Racon runs or a combination
of Racon and Nanopolish runs can improve accuracy signiﬁcantly. Racon
developers recommend Minimap as the read mapper to use before running
Racon, since Minimap is both fast and sensitive [52].
3 Experimental Methodology
3.1
Dataset
In this work, we use Escherichia coli genome data as the test case,
sequenced using the MinION with an R9 ﬂowcell [55].
MinION sequencing has two types of workﬂows. In the 1D workﬂow,
only the template strand of the double-stranded DNA is sequenced. In
contrast, in the 2D workﬂow, with the help of a hairpin ligation, both the
template and complement strands pass through the pore and are sequenced.
After the release of R9 chemistry, 1D data became very usable in contrast
to previous chemistries. Thus, we perform the analysis of the tools on 1D
data.
MinION outputs one ﬁle in the fast5 format for each read. The fast5 ﬁle
format is a hierarchical data format, capable of storing both raw signal data
and basecalled data returned by Metrichor. This dataset includes 164,472
reads, i.e., fast5 ﬁles. Since all these ﬁles include both raw signal data
and basecalled reads, we can use this dataset for both 1) using the local
basecallers to convert raw signal data into the basecalled reads and 2) using
the already basecalled reads by Metrichor.
3.2
Evaluation Systems
In this work, for accuracy and performance evaluations of different
tools, we use three separate systems with different speciﬁcations. We use
the ﬁrst computer in the ﬁrst part of the analysis, accuracy analysis. We
use the second and third computers in the second part of the analysis,
performance analysis, to compare the scalability of the analyzed tools in
the two machines with different speciﬁcations (Table 6).
We choose the ﬁrst system for evaluation since it has a larger memory
capacity than a usual server and, with the help of a large number of
cores, the tasks can be parallelized easily in order to get the output data
quickly. We choose the second system, called desktop, since it represents
a commonly-used desktop server. We choose the third system, called big-
mem, because of its large memory capacity. This big-mem system can be
useful for those who would like to get results more quickly.
Table 4. State-of-the-art read mapping tools.
Tool
Strategy
Multi-threading Support
Source
Reference
BWA-MEM
Burrows-Wheeler Transform (BWT)
with -t parameter
http://bio-bwa.sourceforge.net
[50]
GraphMap
k-mer similarity
with –threads parameter
https://github.com/isovic/graphmap
[40]
Minimap
minimizer similarity
with -t parameter
https://github.com/lh3/minimap
[41]
Table 5. State-of-the-art polishing tools.
Tool
Strategy
Multi-threading Support
Source
Reference
Nanopolish
Hidden Markov Model
with –threads and -P parameters
https://github.com/jts/nanopolish
[51]
Racon
Partial order alignment graph
with –threads parameter
https://github.com/isovic/racon
[52]


## Page 5


5
Table 6. Speciﬁcations of evaluation systems.
Name
Model
CPU Speciﬁcations
Main Memory Speciﬁcations
NUMA* Speciﬁcations
System 1
40-core Intel®Xeon®
E5-2630 v4 CPU
@ 2.20GHz
20 physical cores
2 threads per core
40 logical cores with hyper-threading**
128GB DDR4
2 channels, 2 ranks/channel
Speed: 2400MHz
2 NUMA nodes, each with 10 physical
cores, 64GB of memory and an 25MB
of last level cache (LLC)
System 2
(desktop)
8-core Intel®Core
i7-2600 CPU
@ 3.40GHz
4 physical cores
2 threads per core
8 logical cores with hyper-threading**
16GB DDR3
2 channels, 2 ranks/channel
Speed: 1333MHz
1 NUMA node, with 4 physical cores,
16GB of memory and an 8MB of LLC
System 3
(big-mem)
80-core Intel®Xeon®
E7-4850 CPU
@ 2.00GHz
40 physical cores
2 threads per core
80 logical cores with hyper-threading**
1TB DDR3
8 channels, 4 ranks/channel
Speed: 1066MHz
4 NUMA nodes, each with 10 physical
cores, 256GB of memory and an
24MB of LLC
* NUMA (Non-Uniform Memory Access) is a computer memory design, where a processor accesses its local memory faster (i.e., with lower latency)
than a non-local memory (i.e., memory local to another processor in another NUMA node). A NUMA node is composed of the local memory and the
CPU cores (See Observation 6 in Section 4.1 for detail).
** Hyper-threading is Intel’s simultaneous multithreading (SMT) implementation (See Observation 5 in Section 4.1 for detail).
3.3
Accuracy Metrics
We compare each draft assembly generated after the assembly step
and each improved assembly generated after the polishing step with the
reference genome, by using the dnadiff command under the MUMmer
package[56]. Weusesixmetrics tomeasureaccuracy, as deﬁnedinTable7:
1) number of bases in the assembly, 2) number of contigs, 3) average
identity, 4) coverage, 5) number of mismatches, and 6) number of indels.
3.4
Performance Metrics
We analyze the performance of each tool by running the associated
command-line of each tool with the /usr/bin/time -v command.
We use four metrics to quantify performance as deﬁned in Table 8: 1) wall
clock time, 2) CPU time, 3) peak memory usage, and 4) parallel speedup.
4 Results and Analysis
In this section, we present our results obtained by analyzing the
performance of different tools for each step in the genome assembly
pipeline using nanopore sequence data in terms of accuracy and
performance, using all the metrics we provide in Table 7 and Table 8.
Additionally, Table 9 shows the tool version, the executed command, and
the output of each analyzed tool. We divide our analysis into three main
parts.
In the ﬁrst part of our analysis, we examine the ﬁrst three steps of
the pipeline (cf. Figure 1). To this end, we ﬁrst execute each basecalling
tool (i.e., one of Nanonet, Scrappie, Nanocall or DeepNano). Since
Metrichor is a cloud-based tool and its source code is not available, we
cannot execute Metrichor and get the performance metrics for it. After
recording the performance metrics for each basecaller run, we execute
either GraphMap or Minimap followed by Miniasm, or Canu itself, and
record the performance metrics for each run. We obtain a draft assembly
for each combination of these basecalling, read-to-read overlap ﬁnding
and assembly tools. For each draft assembly, we assess its accuracy by
comparingtheresultingdraftassemblywith the existingreferencegenome.
We show the accuracy results in Table 10. We show the performance results
in Table 11. We will refer to these tables in Sections 4.1 – 4.3.
In the second part of our analysis, we examine the last two steps of the
pipeline (cf. Figure 1). To this end, for each obtained draft assembly, we
execute each possible combination of different read mappers (i.e., BWA-
MEM or Minimap) and different polishers (i.e., Nanopolish or Racon),
and record the performance metrics for each step (i.e., read mapping and
polishing). We obtain a polished assembly after each run, and assess its
accuracy by comparing it with the existing reference genome. For these
two analyses, we use the ﬁrst system, which has 40 logical cores, and
execute each tool using 40 threads, which is the possible maximum number
Table 7. Accuracy metrics.
Metric Name
Deﬁnition
Preferred Values
Number of bases
Total number of bases in the assembly
≃Length of reference genome
Number of contigs
Total number of segments in the assembly
Lower (≃1)
Average identity
Percentage similarity between the assembly and the reference genome
Higher (≃100%)
Coverage
Ratio of the number of aligned bases in the reference genome to the length of reference
genome
Higher (≃100%)
Number of mismatches
Total number of single-base differences between the assembly and the reference genome
Lower (≃0)
Number of indels
Total number of insertions and deletions between the assembly and the reference genome
Lower (≃0)
Table 8. Performance metrics.
Metric Name
Deﬁnition
Preferred Values
Wall clock time
Elapsed time from the start of a program to the end
Lower
CPU time
Total amount of time the CPU spends in user mode (i.e., to run the program’s code) and
kernel mode (i.e., to execute system calls made by the program)*
Lower
Peak memory usage
Maximum amount of memory used by a program during its whole lifetime
Lower
Parallel speedup
Ratio of the time to run a program with 1 thread to the time to run it with N threads
Higher
* If wall clock time < CPU time for a speciﬁc program, it means that the program runs in parallel.


## Page 6


6
Senol Cali et al.
Table 9. Versions, commands to execute, and outputs for each analyzed tool.
Command*
Output
Basecalling Tools
Nanonet–v2.0
nanonetcall fast5_dir/ --jobs N --chemistry r9
reads.fasta
Scrappie–v1.0.1
(1)export OMP_NUM_THREADS=N
(2)scrappie events --segmentation Segment_Linear:split_hairpin
(2)fast5_dir/ ...
reads.fasta
Nanocall–v0.7.4
nanocall -t N fast5_dir/
reads.fasta
DeepNano–e8a621e
python basecall.py –directory fast5_dir/ --chemistry r9
reads.fasta
Read-to-Read Overlap Finding Tools
GraphMap–v0.5.2
graphmap owler -L paf -t N -r reads.fasta -d reads.fasta
overlaps.paf
Minimap–v0.2
minimap -Sw5 -L100 -m0 -tN reads.fasta reads.fasta
overlaps.paf
Assembly Finding Tools
Canu–v1.6
canu -p ecoli -d canu-ecoli genomeSize=4.6m -nanopore-raw
reads.fasta
draftAssembly.fasta
Miniasm–v0.2
miniasm -f reads.fasta overlaps.paf
draftAssembly.gfa –>
draftAssembly.fasta
Read Mapping Tools
BWA-MEM–0.7.15
(1)bwa index draftAssembly.fasta
(2)bwa mem -x ont2d -t N draftAssembly.fasta reads.fasta
mappings.sam –>
–> mappings.bam
Minimap–v0.2
minimap -tN draftAssembly.fasta reads.fasta
mappings.paf
Polishing Tools
Nanopolish–v0.7.1
(1)python nanopolish_makerange.py draftAssembly.fasta | parallel -P M
(2)nanopolish variants --consensus polished.{1}.fa -w {1}
(2)-r reads.fasta -b mappings.bam -g draftAssembly.fasta -t N
(3)python nanopolish_merge.py polished.*.fa
polished.fasta
Racon–v0.5.0
racon (–sam) –bq -1 -t N reads.fastq mappings.paf/(mappings.sam)
draftAssembly.fasta
polished.fasta
* N corresponds to the number of threads and M corresponds to the number of parallel jobs.
of threads for that particular machine. We show the accuracy results in
Table 12. We show the performance results in Table 13. We will refer to
these tables in Section 4.4.
In the third part of our analysis, we assess the scalability of all of
the tools that have multi-threading support. For this purpose, we use the
second and third systems to compare the scalability of these tools on two
different system conﬁgurations. For each tool, we change the number of
threads and observe the corresponding change in speed, memory usage,
and parallel speedup. These results are depicted in Figures 2 – 6, and we
will refer to them throughout Sections 4.1 – 4.4.
Sections 4.1 – 4.4 describe the major observations we make for each of
theﬁvesteps ofthe pipeline (cf. Figure1)basedonour extensive evaluation
results.
4.1
Basecalling Tools
As we discuss in Section 2.1, ONT’s basecallers Metrichor, Nanonet
and Scrappie, and another basecaller developed by Boza et al. (2017),
DeepNano, use Recurrent Neural Networks (RNNs) for basecalling
whereas Nanocall developed by David et al. (2016) uses Hidden Markov
Models (HMM) for basecalling.
Accuracy
Using RNNs is a more powerful basecalling approach than using
HMMs since an RNN 1) does not make any assumptions about sequence
length [57] and 2) is not affected by the repeats in the sequence [37, 39, 57].
However, it is still challenging to determine the correct length of the
homopolymers even with an RNN.
In order to compare the accuracy of the analyzed basecallers, we group
the accuracy results by each basecalling tool and compare them according
to the deﬁned accuracy metrics.
According to this analysis and the accuracy results shown in Table 10,
we make the following key observation.
Observation 1: The pipelines that start with Metrichor, Nanonet,
or Scrappie as the basecaller have similar identity and coverage trends
among all of the evaluated scenarios (i.e., tool combinations for the ﬁrst
three steps), but Scrappie has a lower number of mismatches and indels.
However, Nanocall and DeepNano cannot reach these three basecallers’
accuracies: they have lower identity and lower coverage.
Since Nanonet is the local version of Metrichor,
Nanonet and
Metrichor’s similar accuracy trends are expected. In addition to the power
of the RNN-based approach, Scrappie tries to solve the homopolymer
basecalling problem.
Although Scrappie is in an early stage of
development, it leads to a smaller number of indels than Metrichor or
Nanonet. Nanocall’s poor accuracy results are due to the simple HMM-
based approach it uses. Although DeepNano performs better than Nanocall
with the help of its RNN-based approach, it results in a higher number of
indels and a lower coverage of the reference genome.
Performance
RNN and HMM are computationally-intensive algorithms. In HMM-
based basecalling, the Viterbi algorithm [58] is used for decoding. The
Viterbi algorithm is a sequential technique and its computation cannot
currently be parallelized with multithreading. However, in RNN-based
basecalling, multiple threads can work on different sections of the
neural network and thus RNN computation can be parallelized with
multithreading.
In order to measure and compare the performance of the selected
basecallers, we ﬁrst compare the recorded wall clock time, CPU time and
memory usage metrics of each scenario for the ﬁrst step of the pipeline.


## Page 7


7
Table 10. Accuracy analysis results using different tools for the ﬁrst three steps of the pipeline.
Number of
Bases
Number of
Contigs
Identity
(%)
Coverage
(%)
Number of
Mismatches
Number of
Indels
1
Metrichor + —
+ Canu
4,609,499
1
98.05
99.92
12,378
76,990
2
Metrichor + Minimap
+ Miniasm
4,402,675
1
87.71
94.85
249,096
372,704
3
Metrichor + GraphMap + Miniasm
4,500,155
2
86.22
96.95
237,747
360,199
4
Nanonet
+ —
+ Canu
4,581,728
1
97.92
99.97
11,971
83,248
5
Nanonet
+ Minimap
+ Miniasm
4,350,175
1
85.50
92.76
237,518
394,852
6
Nanonet
+ GraphMap + Miniasm
4,272,545
1
85.36
91.16
232,748
389,968
7
Scrappie
+ —
+ Canu
4,614,149
1
98.46
99.90
6,777
63,597
8
Scrappie
+ Minimap
+ Miniasm
4,877,399
8
86.94
90.04
184,669
363,025
9
Scrappie
+ GraphMap + Miniasm
4,368,417
1
86.78
89.86
189,192
372,245
10
Nanocall
+ —
+ Canu
1,299,808
86
93.33
28.93
21,985
61,217
11
Nanocall
+ Minimap
+ Miniasm
4,492,964
5
80.52
42.92
177,589
221,092
12
Nanocall
+ GraphMap + Miniasm
4,429,390
3
80.51
41.32
171,455
213,435
13
DeepNano + —
+ Canu
7,151,596
106
92.75
99.16
38,803
211,551
14
DeepNano + Minimap
+ Miniasm
4,252,525
1
82.38
65.00
199,122
335,761
15
DeepNano + GraphMap + Miniasm
4,251,548
1
82.39
64.92
197,914
335,064
Table 11. Performance analysis results for the ﬁrst three steps of the pipeline.
Step 1:
Basecaller
Step 2:
Read-to-Read Overlap Finder
Step 3:
Assembly
Wall
Clock
Time
(h:m:s)
CPU Time
(h:m:s)
Memory
Usage
(GB)
Wall
Clock
Time
(h:m:s)
CPU Time
(h:m:s)
Memory
Usage
(GB)
Wall
Clock
Time
(h:m:s)
CPU Time
(h:m:s)
Memory
Usage
(GB)
1
Metrichor + —
+ Canu
—*
—*
—*
—
—
—
44:12:31
502:18:56
5.76
2
Metrichor + Minimap
+ Miniasm
2:15
41:37
12.30
1:09
1:09
1.96
3
Metrichor + GraphMap + Miniasm
6:14
1:52:57
56.58
1:05
1:05
1.82
4
Nanonet
+ —
+ Canu
17:52:42
714:21:45
1.89
—
—
—
11:32:40
129:07:16
5.27
5
Nanonet
+ Minimap
+ Miniasm
1:13
18:55
9.45
33
33
0.69
6
Nanonet
+ GraphMap + Miniasm
3:18
48:27
29.16
32
32
0.65
7
Scrappie
+ —
+ Canu
3:11:41
126:19:06
13.36
—
—
—
33:47:41
385:51:23
5.75
8
Scrappie
+ Minimap
+ Miniasm
2:52
1:10:26
12.40
1:29
1:29
1.98
9
Scrappie
+ GraphMap + Miniasm
7:26
2:16:02
38.31
1:23
1:23
1.87
10
Nanocall
+ —
+ Canu
47:04:53
1857:37:56
37.73
—
—
—
1:35:23
27:58:29
3.77
11
Nanocall
+ Minimap
+ Miniasm
1:15
16:08
12.19
20
20
0.47
12
Nanocall
+ GraphMap + Miniasm
5:14
1:09:04
56.78
16
16
0.30
13
DeepNano + —
+ Canu
23:54:34
811:14:29
8.38
—
—
—
1:15:48
17:31:07
3.61
14
DeepNano + Minimap
+ Miniasm
1:50
24:30
11.71
1:03
1:03
1.31
15
DeepNano + GraphMap + Miniasm
5:18
1:17:06
54.64
58
58
1.10
* We cannot get the performance metrics for Metrichor since its source code is not available for us to run the tool by ourselves.
Based on the results provided in Table 11, we make the following key
observation.
Observation 2: RNN-based Nanonet and DeepNano are 2.6x and
2.3x faster than HMM-based Nanocall, respectively. Although Scrappie
is also an RNN-based tool, it is 5.7x faster than Nanonet due to its C
implementation as opposed to Nanonet’s Python implementation.
For a deeper understanding of these tools’ advantages, disadvantages
and bottlenecks, we also perform a scalability analysis for each basecaller
by running it on the desktop server and the big-mem server separately,
with 1, 2, 4, 8 (maximum for the desktop server), 16, 32, 40, 64
and 80 (maximum for the big-mem server) threads, and measuring the
performance metrics for each conﬁguration. Metrichor and DeepNano are
not included in this analysis because Metrichor is a cloud-based tool and
its source code is not available for us to change its number of threads, and
DeepNano does not support multi-threading. Figure 2 shows the speed,
memory usage and parallel speedup results of our evaluations. We make
four observations.
Observation 3: When we compare desktop’s and big-mem’s single
thread performance, we observe that desktop is approximately 2x faster
than big-mem (cf. Figure 2a and 2b).
This is mainly because of desktop’s higher CPU frequency (see Table
6). It is an indication that all of these three tools are computationally
expensive. Larger memory capacity or larger Last-Level Cache (LLC)
capacity of big-mem cannot make up for the higher CPU speed in desktop
when there is only one thread.
Observation 4: Scrappie and Nanocall have a linear increase in
memory usage when number of threads increases. In contrast, Nanonet
has a constant memory usage for all evaluated thread units (cf. Figure 2c
and 2d).
In Scrappie and Nanocall, each thread performs the basecalling for
different groups of raw reads. Thus, each thread allocates its own memory
spaceforthecorrespondingdata. This causes thelinearincrease in memory
usage when the level of parallelism increases. In Nanonet, all of the threads


## Page 8


8
Senol Cali et al.
!"#
!
"
#
$
%
&
!
#
%
'
(
)*+*,,-,./0--120
3245-+.67.89+-*1:
!$#
!%#
!
"
#!
#"
$!
$"
%!
%"
&!
&"
!
$!
&!
'!
(!
)*+*,,-,./0--120
3245-+.67.89+-*1:
!&#
!'#
!(#
!"#$%&'()*)!+#,(-.&/).0$%(
!"#$%&'()1)!+#,(-.&/).0$%(
!"#$%&'()1)!+#,(-.&/).0$%(
!"#$%&'()*)!+#,(-.&/).0$%(
2)3456)
70'%
1)2)3456)
70'%
!
"!!!
#!!!!
#"!!!
$!!!!
$"!!!
%!!!!
%"!!!
!
$
&
'
(
)*++,-+./0,1234,564/7
893:4;,.<,1=;4*>6
8*?./*++,@6A,8*?.?4B,@6A,C/;*DD24,E>460B.D
!
"
#
$
%
&!
&"
&#
&$
!
"
#
$
%
'()*+,(-./0+12)3(+4567
89-:(/+.;+<=/()>2
!
"!!!!
#!!!!
$!!!!
%!!!!
&!!!!
'!!!!
(!!!!
!
#!
%!
'!
)!
*+,,-.,/01-2345-67508
9:4;5<-/=-2><5+?7
9+@/0+,,-A7B-9+@/@5C-A7B-D0<+EE35-F;3GH454
!
"!
#!
$!
%!
&!!
&"!
&#!
&$!
!
"!
#!
$!
%!
'()*+,(-./0+12)3(+4567
89-:(/+.;+<=/()>2
8*?./*++
8*?.?4B
C/;*DD24
Figure 2. Scalability results of Nanocall, Nanonet and Scrappie.
Wall clock time (a, b), peak memory usage (c, d), and parallel speedup (e, f) results obtained on the desktop and big-mem systems. The left column (a, c,
e) shows the results from the desktop system and the right column (b, d, f) shows the results from the big-mem system.
share the computation of each read, and thus memory usage is not affected
by the amount of thread parallelism.
Observation 5: When the number of threads exceeds the number
of physical cores, the simultaneous multithreading overhead prevents
continuedlinear speedup of Nanonet, ScrappieandNanocall (cf. Figure2e
and 2f).
Simultaneous multithreading (SMT) (i.e., running more than one
thread per physical core [59–66]), or more speciﬁcally Intel’s hyper-
threading (i.e., since we use Intel’s hyper-threading enabled machines
(see Table 6)) helps to decrease the total runtime but it does not provide a
linear speedup with the number of threads because of the CPU-intensive
workload of Scrappie, Nanocall and Nanonet. If the threads executed
are CPU-bound and do not wait for the memory or I/O requests, hyper-
threading does not provide linear speedup due to the contention it causes
in the shared resources for the computation. This phenomenon has been
analyzed extensively in other application domains [59–61].
Observation 6: Data sharing between threads degrades the parallel
speedup of Nanonet when cores from multiple NUMA nodes take role in
the computation (cf. Figure 2f).
In Nanonet, data is shared between threads and each thread performs
different computations on the same data. There are 4 NUMA nodes in
big-mem (cf. Table 6), and when data is shared between multiple NUMA
nodes, this negatively affects the speedup of Nanonet because accessing
the data located in another node (i.e., non-local memory) requires longer
latency than accessing the data located in local memory. When multiple
NUMA nodes start taking role in the computation, Nanocall performs
better in terms of scalability since it does not require data sharing between
different threads.
Summary. Based on the observations we make about the analyzed
basecalling tools, we conclude that the choice of the tool for this step
plays an important role to overcome the high error rates of nanopore
sequencingtechnology. BasecallingwithRecurrent Neural Networks (e.g.,
Metrichor, Nanonet, Scrappie) provides higher accuracy and higher speed
than basecalling with Hidden Markov Models, and the newest basecaller
of ONT, Scrappie, also has the potential to overcome the homopolymer
basecalling problem.
4.2
Read-to-Read Overlap Finding Tools
As we discuss in Section 2.2, GraphMap and Minimap are the
commonly-used tools for this step. GraphMap ﬁnds the overlaps using k-
mer similarity, whereas Minimap ﬁnds them by using minimizers instead
of the full set of k-mers.
Accuracy
As done in GraphMap, ﬁnding the overlaps with the help of full set
of k-mers is a highly-sensitive and accurate approach. However, it is
also resource-intensive. For this reason, instead of the full set of k-mers,
Minimap uses a minimum representative set of k-mers, minimizers, as an
alternative approach for ﬁnding the overlaps.
In order to compare the accuracy of these two approaches, we
categorize the results in Table 10 based on read-to-read overlap ﬁnding
tools. In other words, we look at the rows with the same basecaller
(i.e., red-labeled tools) and same assembler (i.e., green-labeled tools) but
different read-to-read overlap ﬁnder (i.e., blue-labeled tools). After that,
we compare them according to the deﬁned accuracy metrics. We make the
following major observation.
Observation 7: Pipelines with GraphMap or Minimap end up with
similar values for identity, coverage, number of indels and mismatches.


## Page 9


9
Thus, either of these read-to-read overlap ﬁnding tools can be used in
the second step of the nanopore sequencing assembly pipeline to achieve
similar accuracy.
Minimap and GraphMap do not have a signiﬁcantly different effect on
the accuracy of the generated draft assemblies. This is because Minimap
does not lose any sensitivity by storing minimizers instead of the full set
of k-mers.
Performance
In order to compare the performance of GraphMap and Minimap, we
categorize the results in Table 11 based on read-to-read overlap ﬁnding
tools, in a similar way we describe the results in Table 10 for the accuracy
analysis. We also perform a scalability analysis for each of these tools by
running them on the big-mem server with 1, 2, 4, 8, 16, 32, 40, 64 and
80 threads, and measuring the performance metrics. Because of the high
memory usage of GraphMap, data necessary for the tool does not ﬁt in the
memory of the desktop server and the GraphMap job exits due to a bad
memory allocation exception. Thus, we could not perform the scalability
analysis of GraphMap in the desktop server.
Figure 3 depicts the speed, memory usage and parallel speedup results
of the scalability analysis for GraphMap and Minimap. We make the
following three observations according to the results from Table 11 and
Figure 3.
Observation 8: The memory usage of both GraphMap and Minimap
is dependent on the hash table size but independent of number of threads.
Minimap requires 4.6x less memory than GraphMap, on average.
!"#
!$#
!
"!
#!
$!
%!
&!
'!
!
#!
%!
'!
(!
)*+,-.*/012-34+5*-6789
:;/<*1-0=->?1*+@4
!
"
#
$
%
&!
&"
&#
!
"!
#!
$!
%!
'()(**+*,-.++/0.
1023+),45,67)+(/8
!%#
!
"!!!
#!!!
$!!!
%!!!
&!!!
'!!!
!
#!
%!
'!
(!
)*++,-+./0,1234,564/7
893:4;,.<,1=;4*>6
?2@23*A,B6C,D;*A=?*A,E:2FG343
!"#$
%"&$
9:;:2(.
>)(.79(.
Figure 3. Scalability results of Minimap and GraphMap.
Wall clock time (a), peak memory usage (b), and parallel speedup (c)
results obtained on the big-mem system.
This is mainly because Minimap stores only minimizers instead of all
k-mers. Storing the full set of k-mers in GraphMap requires a larger hash
table, and thus higher memory usage than Minimap. The high amount of
memory requirement causes GraphMap to not run on our desktop system
for none of the selected number of thread units.
Observation 9: Minimap is 2.5x faster than GraphMap, on average,
across different scenarios in Table 11.
Since GraphMap stores all k-mers, GraphMap needs to scan its very
large dataset while ﬁnding the overlaps between two reads. However, in
Minimap, the size of dataset that needs to be scanned is greatly shrunk
by storing minimizers, as we describe in Observation 8. Thus, Minimap
performs much less computation, leading to its 2.5x speedup. Another
indication of the different memory usage and its effect on the speed
of computation is the Last-Level Cache (LLC) miss rates of these two
tools. The LLC miss rate of Minimap is 36% whereas the LLC miss
rate of GraphMap is 55%. Since the size of data needed by GraphMap
is much larger than the LLC size, GraphMap experiences LLC misses
more frequently. As a result, GraphMap stalls for longer, waiting for data
accesses from main memory, which negatively affects the speed of the
tool.
Observation 10: Minimap is more scalable than GraphMap. However,
after 32 threads, there is a decrease in the parallel speedup of Minimap
(cf. Figure 3c).
Becauseofits lowercomputationalworkload andlowermemoryusage,
we ﬁnd that Minimap is more scalable than GraphMap. However, in
Minimap, threads that ﬁnish their work wait for the other active threads
to ﬁnish their workloads, before starting new work, in order to prevent
higher memory usage. Because of this, when the number of threads
reaches a high number (i.e., 32 in Figure 3c), synchronization overhead
greatly increases, causing the parallel speedup to reduce. GraphMap
does not suffer from such a synchronization bottleneck and hence does
not experience a decrease in speedup. However, GraphMap’s speedup
saturates when the number of threads reaches a high number due to data
sharing between threads.
Summary. According to the observations we make about GraphMap
and Minimap, we conclude that storing minimizers instead of all k-mers, as
donebyMinimap, does notaffecttheoverallaccuracy oftheﬁrstthreesteps
of the pipeline. Moreover, by storing minimizers, Minimap has a much
lower memory usage and thus much higher performance than GraphMap.
4.3
Assembly Tools
As we discuss in Section 2.3, Canu and Miniasm are the commonly-
used tools for this step.2
Accuracy
In order to compare the accuracy of these two tools, we categorize
the results in Table 10 based on assembly tools. We make the following
observation.
Observation 11: Canu provides higher accuracy than Miniasm, with
the help of the error-correction step that is present in its own pipeline.
Performance
In order to compare the performance of Canu and Miniasm, we
categorize the results in Table 11 based on assembly tools, in a way similar
to what we did in Table 10 for the accuracy analysis. We could not perform
a scalability analysis for these tools since Canu has an auto-conﬁguration
mechanism for each sub-step of its own pipeline, which does not allow
us to change the number of threads, and Miniasm does not support multi-
threading. We make the following observation according to the results in
Table 11.
2 In addition, we attempted to evaluate MECAT [67], another assembler.
We were unable to draw any meaningful conclusions from MECAT, as its
memory usage exceeds the 1TB available in our big-mem system.


## Page 10


10
Senol Cali et al.
Observation 12: Canu is much more computationally intensive and
greatly (i.e., by 1096.3x) slower than Miniasm, because of its very
expensive error-correction step.
Summary. According to the observations we make about Canu and
Miniasm, there is a tradeoff between accuracy and performance when
deciding on the appropriate tool for this step. Canu produces highly
accurate assemblies but it is resource intensive and slow. In contrast,
Miniasm is a very fast assembler but it cannot produce as accurate draft
assemblies as Canu. We suggest that Miniasm can potentially be used for
fast initial analysis and then further polishing can be applied in the next
step in order to produce higher-quality assemblies.
4.4
Read Mapping and Polishing Tools
As we discuss in Section 2.4, further polishing may be required for
improving the accuracy of the low-quality draft assemblies. For this
purpose, after aligning the reads to the generated draft assembly with
BWA-MEM or Minimap,3,4 one can use Nanopolish or Racon to perform
polishing and obtain improved assemblies (i.e., consensus sequences).
3 We do not discuss these tools in great detail here since they perform
read mapping, which is commonly analyzed and relatively well understood
(e.g., see [68–86]).
4 Minimap2[87]is arecently-releasedsuccessortoMinimap. Wecompare
Minimap2 to BWA-MEM and to Minimap, and make two observations.
First, Minimap2 signiﬁcantly outperforms BWA-MEM. Since Minimap2
can produce SAM alignments (which BWA-MEM produces), we can
replace BWA-MEM with Minimap2 in future genome assembly pipelines.
Second, Minimap2 has similar accuracy and performance compared
to Minimap. This is because Minimap2 and Minimap employ similar
indexing and seeding algorithms [87], and the new features of Minimap2
(more accurate chaining,
base-level alignment,
support for spliced
alignment) are not used in the pipeline we analyze. As a result, our ﬁndings
for Minimap generally remain the same for Minimap2.
Nanopolish accepts mappings only in Sequence Alignment/Map (SAM)
format [88] and it works only with draft assemblies generated with
the Metrichor-basecalled reads. On the other hand, Racon accepts
both Pairwise Mapping format (PAF) mappings [41] and SAM-format
mappings, but it requires the input reads and draft assembly ﬁles to be
in fastq format [89], which includes quality scores. However, by using the
-bq -1 parameter, it is possible to disable the ﬁltering used in Racon,
whichrequires qualityscores. Sinceourbasecalledreads areinfastaformat
[90], in our experiments, we convert these fasta ﬁles into fastq ﬁles and
disable the ﬁltering with the corresponding parameter.
BWA-MEM generates mappings in SAM format whereas Minimap
generates mappings inPAF format. SinceNanopolishrequires SAM format
input, we generate the mappings only with BWA-MEM and use them for
Nanopolish polishing, in our analysis. On the other hand, since Racon
accepts both formats, we generate the mappings and the overlaps with
both BWA-MEM and Minimap, respectively, and use them for Racon
polishing, in our analysis.
Accuracy
Table 12 presents the accuracy metrics results for Nanopolish (i.e.,
Rows 1-3) and Racon (i.e., Rows 4-23) pipelines. Based on these results,
we make two observations.
Observation 13: Both Nanopolish and Racon signiﬁcantly increase
the accuracy of the draft assemblies.
For example, Nanopolish increases the identity and coverage of the
draft assembly generated with the Metrichor+Minimap+Miniasm pipeline
from 87.71% and 94.85% (Row 2 of Table 10), respectively, to 92.33% and
96.31% (Row 2 of Table 12). Similarly, Racon increases them to 97.70%
and 99.91% (Rows 6–7 of Table 12), respectively.
Observation 14: For Racon, the choice of read mapper does not affect
the accuracy of the polishing step.
We observe that using BWA-MEM or Minimap to generate the
mappings for Racon results in almost identical accuracy metric results. For
example, when we use BWA-MEM before Racon for the draft assembly
Table 12. Accuracy analysis results for the full pipeline with a focus on the last two steps.
Number of
Bases
Number of
Contigs
Identity
(%)
Coverage
(%)
Number of
Mismatches
Number of
Indels
1
Metrichor + —
+ Canu
+ BWA-MEM
+ Nanopolish
4,683,072
1
99.48
99.93
8,198
15,581
2
Metrichor + Minimap
+ Miniasm+ BWA-MEM
+ Nanopolish
4,540,352
1
92.33
96.31
162,884
182,965
3
Metrichor + GraphMap + Miniasm+ BWA-MEM
+ Nanopolish
4,637,916
2
92.38
95.80
159,206
180,603
4
Metrichor + —
+ Canu
+ BWA-MEM
+ Racon
4,650,502
1
98.46
100.00
18,036
51,842
5
Metrichor + —
+ Canu
+ Minimap
+ Racon
4,648,710
1
98.45
100.00
17,906
52,168
6
Metrichor + Minimap
+ Miniasm+ BWA-MEM
+ Racon
4,598,267
1
97.70
99.91
24,014
82,906
7
Metrichor + Minimap
+ Miniasm+ Minimap
+ Racon
4,600,109
1
97.78
100.00
23,339
79,721
8
Nanonet
+ —
+ Canu
+ BWA-MEM
+ Racon
4,622,285
1
98.48
100.00
16,872
52,509
9
Nanonet
+ —
+ Canu
+ Minimap
+ Racon
4,620,597
1
98.49
100.00
16,874
52,232
10 Nanonet
+ Minimap
+ Miniasm+ BWA-MEM
+ Racon
4,593,402
1
98.01
99.97
20,322
72,284
11 Nanonet
+ Minimap
+ Miniasm+ Minimap
+ Racon
4,592,907
1
98.04
100.00
20,170
70,705
12 Scrappie
+ —
+ Canu
+ BWA-MEM
+ Racon
4,673,871
1
98.40
99.98
13,583
60,612
13 Scrappie
+ —
+ Canu
+ Minimap
+ Racon
4,673,606
1
98.40
99.98
13,798
60,423
14 Scrappie
+ Minimap
+ Miniasm+ BWA-MEM
+ Racon
5,157,041
8
97.87
99.80
18,085
78,492
15 Scrappie
+ Minimap
+ Miniasm+ Minimap
+ Racon
5,156,375
8
97.87
99.94
17,922
77,807
16 Nanocall
+ —
+ Canu
+ BWA-MEM
+ Racon
1,383,851
86
93.49
28.82
19,057
65,244
17 Nanocall
+ —
+ Canu
+ Minimap
+ Racon
1,367,834
86
94.43
28.74
15,610
55,275
18 Nanocall
+ Minimap
+ Miniasm+ BWA-MEM
+ Racon
4,707,961
5
90.75
97.11
91,502
347,005
19 Nanocall
+ Minimap
+ Miniasm+ Minimap
+ Racon
4,673,069
5
92.23
97.10
72,646
291,918
20 DeepNano + —
+ Canu
+ BWA-MEM
+ Racon
7,429,290
106
96.46
99.24
27,811
102,682
21 DeepNano + —
+ Canu
+ Minimap
+ Racon
7,404,454
106
96.03
99.21
34,023
110,640
22 DeepNano + Minimap
+ Miniasm+ BWA-MEM
+ Racon
4,566,253
1
96.76
99.86
25,791
125,386
23 DeepNano + Minimap
+ Miniasm+ Minimap
+ Racon
4,571,810
1
96.90
99.97
24,994
119,519


## Page 11


11
Table 13. Performance analysis results for the full pipeline with a focus on the last two steps.
Step 4: Read Mapper
Step 5: Polisher
Wall
Clock
Time
(h:m:s)
CPU Time
(h:m:s)
Memory
Usage
(GB)
Wall
Clock
Time
(h:m:s)
CPU Time
(h:m:s)
Memory
Usage
(GB)
1
Metrichor
+ —
+ Canu
+ BWA-MEM
+ Nanopolish
24:43
15:47:21
5.26
5:51:00
191:18:52
13.38
2
Metrichor
+ Minimap
+ Miniasm + BWA-MEM
+ Nanopolish
12:33
7:50:54
3.75
122:52:00
4458:36:10
31.36
3
Metrichor
+ GraphMap + Miniasm + BWA-MEM
+ Nanopolish
12:47
7:57:58
3.60
129:46:00
4799:03:51
31.31
4
Metrichor
+ —
+ Canu
+ BWA-MEM
+ Racon
24:20
15:43:40
6.60
14:44
9:09:22
8.11
5
Metrichor
+ —
+ Canu
+ Minimap
+ Racon
3
1:35
0.26
15:12
9:45:33
14.55
6
Metrichor
+ Minimap
+ Miniasm + BWA-MEM
+ Racon
12:10
7:48:10
5.19
15:43
9:33:39
9.98
7
Metrichor
+ Minimap
+ Miniasm + Minimap
+ Racon
3
1:24
0.26
20:28
8:57:40
18.24
8
Nanonet
+ —
+ Canu
+ BWA-MEM
+ Racon
9:08
5:53:18
4.84
6:33
4:02:10
4.47
9
Nanonet
+ —
+ Canu
+ Minimap
+ Racon
2
54
0.26
6:45
4:17:26
7.93
10
Nanonet
+ Minimap
+ Miniasm + BWA-MEM
+ Racon
4:40
2:58:02
3.88
7:08
4:19:30
5.35
11
Nanonet
+ Minimap
+ Miniasm + Minimap
+ Racon
2
46
0.26
7:01
4:18:48
9.53
12
Scrappie
+ —
+ Canu
+ BWA-MEM
+ Racon
33:41
21:11:06
8.66
13:32
8:24:44
7.58
13
Scrappie
+ —
+ Canu
+ Minimap
+ Racon
3
1:39
0.27
18:45
7:43:17
13.20
14
Scrappie
+ Minimap
+ Miniasm + BWA-MEM
+ Racon
22:41
14:31:00
6.08
14:37
8:53:59
9.50
15
Scrappie
+ Minimap
+ Miniasm + Minimap
+ Racon
3
1:27
0.27
15:10
9:02:45
12.72
16
Nanocall
+ —
+ Canu
+ BWA-MEM
+ Racon
4:52
3:01:15
3.80
11:07
3:26:52
5.63
17
Nanocall
+ —
+ Canu
+ Minimap
+ Racon
3
1:16
0.22
7:28
2:50:35
3.62
18
Nanocall
+ Minimap
+ Miniasm + BWA-MEM
+ Racon
16:06
10:27:20
5.06
18:56
11:32:45
11.47
19
Nanocall
+ Minimap
+ Miniasm + Minimap
+ Racon
4
1:18
0.26
11:49
7:08:59
10.98
20
DeepNano
+ —
+ Canu
+ BWA-MEM
+ Racon
17:36
11:30:20
4.43
12:48
7:13:04
8.88
21
DeepNano
+ —
+ Canu
+ Minimap
+ Racon
3
1:24
0.28
11:39
6:55:01
3.73
22
DeepNano
+ Minimap
+ Miniasm + BWA-MEM
+ Racon
8:15
5:22:29
4.11
14:16
8:34:32
10.30
23
DeepNano
+ Minimap
+ Miniasm + Minimap
+ Racon
3
1:10
0.26
xxx:12:29
xxx7:55:32
17.11
!
"!!!
#!!!
$!!!
%!!!
&!!!!
&"!!!
&#!!!
&$!!!
!
"
#
$
%
'())*+),-.*/012*342-5
671829*,:*/;92(<4
='>?@A@*B4C*@0D01(E*F<24.G,E
!
!"#
$
$"#
%
!
%
&
'
(
)*+,-.*/012-34+5*-6789
:;/<*1-0=->?1*+@4
!
"
#
$
%
&
'
!
#
%
'
(
)*+*,,-,./0--120
3245-+.67.89+-*1:
!"#
!$#
!%#
!
"!!!
#!!!!
#"!!!
$!!!!
$"!!!
%!!!!
%"!!!
!
$!
&!
'!
(!
)*++,-+./0,1234,564/7
893:4;,.<,1=;4*>6
?)@ABCB,D6E,B2F23*G,H:2IA343
!
"
#
$
%
&!
&"
!
"!
#!
$!
%!
'()*+,(-./0+12)3(+4567
89-:(/+.;+<=/()>2
!&#
!
"
#!
#"
$!
$"
%!
%"
!
$!
&!
'!
(!
)*+*,,-,./0--120
3245-+.67.89+-*1:
!'#
!(#
!"#$%&'()*)!+#,(-.&/).0$%(
!"#$%&'()1)!+#,(-.&/).0$%(
234567
893567
::25;7
='>?@A@
@0D01(E
Figure 4. Scalability results of BWA-MEM and Minimap.
Wall clock time (a, b), peak memory usage (c, d), and parallel speedup (e, f) results obtained on the desktop and big-mem systems. The left column (a, c,
e) shows the results from the desktop system and the right column (b, d, f) shows the results from the big-mem system.


## Page 12


12
Senol Cali et al.
generated with the Metrichor + Canu pipeline (Row 4 of Table 12), Racon
results with 98.46% identity, 100.00% coverage, 18,036 mismatches and
51,842 indels. When we use Minimap, instead (Row 5 of Table 12), Racon
results with 98.45% identity, 100.00% coverage, 17,096 mismatches and
52,168 indels, which is almost identical to the BWA-MEM results.
Performance
In the ﬁrst part of the performance analysis for Nanopolish, we divide
the draft assemblies into 50kb-segments and polish 4 of these segments in
parallel with 10 threads for each segment. For Racon, each draft assembly
is polished using 40 threads, but the tool, by default, divides the input
sequence into windows of 20kb length. Table 13 presents the performance
results for Nanopolish (i.e., Rows 1-3) and Racon (i.e., Rows 4-23)
pipelines. Based on these results, we make the following two observations.
Observation 15: Nanopolish is computationally much more intensive
and thus greatly slower than Racon.
Nanopolish runs take days to complete whereas Racon runs take
minutes.
This is mainly because Nanopolish works on each base
individually, whereas Racon works on the windows. Since each window
is much longer (i.e., 20kb) than a single base, the computational workload
is greatly smaller in Racon. Also, Racon only uses the mappings/overlaps
for polishing, whereas Nanopolish uses raw signal data and an HMM-
based approach in order to generate the consensus sequence, which is
computationally more expensive.
Observation 16: BWA-MEM is computationally more expensive than
Minimap.
Although the choice of BWA-MEM and Minimap for the read mapping
step does not affect the accuracy of the polishing step, these two tools have
a signiﬁcant difference in performance.
For a deeper performance analysis of these read mapping and polishing
tools, we perform a scalability analysis for each read mapper and each
polisher by running them on the desktop system and the big-mem system
separately, with 1, 2, 4, 8 (maximum for desktop server), 16, 32, 40, 64 and
80(maximum forbig-mem server)threads, andmeasuringtheperformance
metrics. Figure 4 shows the the speed, memory usage and parallel speedup
of BWA-MEM and Minimap. We make two observations.
Observation 17: On both systems, Minimap is greatly faster than
BWA-MEM (cf. Figure 4a and 4b). However, when the number of
threads reaches high value, Minimap’s performance degrades due to the
synchronization overhead between its threads (cf. Figure 4f).
On the desktop system, Minimap is 332.0x faster than BWA-MEM, on
average (see Figure 4a). On the big-mem system, Minimap is 294.6x and
179.6x faster than BWA-MEM, on average, when the number of threads is
smaller and greater than 32, respectively. This is due to the synchronization
overhead that increases with the number of threads used in Minimap (see
Observation10). As wealsoshow inFigure4f, Minimap’s speedupreduces
when the number of threads exceeds 32, which is another indication of the
synchronization overhead that causes Minimap to slow down.
Observation 18: Minimap’s memory usage is independent of the
number of threads and stays constant. In contrast, BWA-MEM’s memory
usage increases linearly with the number of threads (cf. Figure 4c and 4d).
In Minimap, memory usage is dependent on the hash table size and is
independentofnumberofthreads(seeObservation8). Incontrast, inBWA-
MEM, each thread separately performs computation for different groups
of reads (as in Scrappie and Nanocall, see Observation 4). This causes
the linear increase in memory usage of BWA-MEM when the number of
threads increases.
Figure5shows thescalabilityresults forRacononthe big-mem system.
We obtain the results on both of the systems. However, we only show the
results for the big-mem system since the results for both of the systems
are similar. We separately test the tool by using PAF mappings and SAM
mappings. Based on the results, we make the following observation.
!
"!!!
#!!!!
#"!!!
$!!!!
!
$!
%!
&!
'!
()**+,*-./+0123+453.6
78293:+-;+0<:3)=5
>).-?+@91AB232
!
"
#!
#"
$!
!
$!
%!
&!
'!
()*+,-)./01,23*4),5678
9:.;)0,/<,=>0)*?3
!
"
#!
#"
$!
$"
!
$!
%!
&!
'!
()*)++,+-./,,01/
2134,*-56-78*,)09
A>B8-/)6
A>B8-9)3
!"#
!$#
!%#
!"#$%
Figure 5. Scalability results of Racon.
Wall clock time (a), peak memory usage (b), and parallel speedup (c)
results obtained on the big-mem system.
Observation 19: Racon’s memory usage is independent of the number
of threads for both PAF mode and SAM mode. However, the memory
usage of PAF mode is 1.86x higher than the memory usage of SAM mode,
on average (cf. Figure 5b).
The memory usage of Racon depends on the number of mappings
received from the fourth step since Racon performs polishing by using
these mappings. Racon’s memory usage is higher for the PAF mode
because the number of mappings stored in the PAF ﬁles is greater than
the number of mappings stored in the SAM ﬁles (i.e., 1.4x). However,
using PAF mappings or SAM mappings do not signiﬁcantly affect the
speed (see Figure 5a) and the parallel speedup (see Figure 5c) of Racon.
Figure 6 shows the scalability results for Nanopolish. We test the
tool by separately using a 25kb and a 50kb segment length to assess the
scalability of the tool with respect to the segment length, in addition to
the scalability with respect to the number of threads. We measure the
performance metrics. We only show the results for the big-mem system
since the results for both of the systems are similar. Based on the results,
we make the following observation.
Observation 20: Nanopolish’s memory usage is independent of the
numberofthreads. However, itsmemoryusageindependentonthesegment
length (cf. Figure 6b).
The memory usage of Nanopolish is not affected by the number of
threads. However, it is dependent on the segment length. Nanopolish uses
more memory for longer segments. When the segment length is doubled
from 25kb to 50kb, the increase in the memory usage (i.e., 2.7x) is greater


## Page 13


13
!
!"#
$
$"#
%
%"#
!
%!
&!
'!
(!
)*+,-.*/012-34+5*-6789
:;/<*1-0=->?1*+@4
!
"!!!
#!!!
$!!!
%!!!
&!!!
'!!!
(!!!
!
#!
%!
'!
)!
*+,,-.,/01-2345-67508
9:4;5<-/=-2><5+?7
9+@/A/,37>B;3CD454
">?3
>!?3
!
"
#
$
%
&!
&"
!
"!
#!
$!
%!
'()(**+*,-.++/0.
1023+),45,67)+(/8
!"#$%&'()*)!+#,(-.&/).0$%( !"#$%&'()1)!+#,(-.&/).0$%(
!"#$%&'()*)!+#,(-.&/).0$%( !"#$%&'()1)!+#,(-.&/).0$%(
2345
2345
!"#
!$#
!%#
Figure 6. Scalability results of Nanopolish.
Wall clock time (a), peak memory usage (b), and parallel speedup (c)
results obtained on the big-mem system.
than 2.0x. This is because the memory usage of Nanopolish depends both
on the length of the segment and the number of read mappings that map
to this segment. For both of the segments, the memory usage also affects
the speed. The Nanopolish run for the 25kb-segment is 2.7x faster than the
run for the 50kb-segment (see Figure 6a).
Observation 21: Nanopolish’s performance greatly degrades when
the number of threads exceeds the number of physical cores (cf. Figure 6c).
Hyper-threading causes a slowdown for Nanopolish because of the
CPU-intensive workload of Nanopolish and the resulting high contention
in the shared resources between the threads executing on the same core,
as we discuss in Observation 5.
Summary. Based on the observations we make about tools for the
optional last two steps of the pipeline, we conclude that further polishing
can signiﬁcantly increase the accuracy of the assemblies. Since BWA-
MEM and Nanopolish are more resource-intensive than Minimap and
Racon, pipelines with Minimap and Racon can provide a signiﬁcant
speedup compared to the pipelines with BWA-MEM and Nanopolish,
while resulting with high-quality consensus sequences.
5 Recommendations
Recommendations for Tool Users
Based on the results we have collected and observations we have
made for each step of the genome assembly pipeline using nanopore
sequence data and the associated tools, we make the following major
recommendations for the current and future tool users.
• ONT’s basecalling tools, Metrichor, Nanonet, and Scrappie, are the
best choices for the basecalling step in terms of both accuracy and
performance. Among these tools, Scrappie is the newest, fastest and
most accurate basecaller. Thus, we recommend using Scrappie for the
basecalling step (See analysis in Section 4.1).
• For the read-to-read overlap ﬁnding step, Minimap is faster than
GraphMap, and it requires low memory. Also, it has similar accuracy
to GraphMap. Thus, we recommend Minimap for the read-to-read
overlap ﬁnding step (See analysis in Section 4.2).
• For the assembly step, if execution time is not an important concern,
we recommend using Canu since it produces much more accurate
assemblies. However, for a fast initial analysis, we recommend using
Miniasm since it is fast and its accuracy can be increased with
an additional polishing step. If Miniasm is used for assembly, we
deﬁnitely recommend further polishing to increase the accuracy of the
ﬁnal assembly (See analysis in Section 4.3). Even though polishing
takes a similar amount of time if we use Miniasm or Canu, the accuracy
improvements are much smaller for a genome assembled using Canu.
We hope that future work can improve the performance of polishing
when the assembled genome already has high accuracy, to reduce the
execution time of the overall assembly pipeline.
• For the polishing step, we recommend using Racon since it is
much faster than Nanopolish. Racon also produces highly-accurate
assemblies (See analysis in Section 4.4).
• In the future, laptops may become a popular platform for running
genome assembly tools, as the portability of a laptop makes it a
good ﬁt for in-ﬁeld analysis. Compared to the desktop and server
platforms that we use to test our pipelines, a laptop has even greater
memory constraints and lower computational power, and we must
factor in limited battery life when evaluating the tools. Based on the
scalability studies we perform using our desktop and server platforms,
we would likely recommend using Minimap followed by Miniasm for
the assembly step, and Minimap followed by Racon for the polishing
step, when performing assembly on a laptop. These three tools use
relatively low amounts of memory, and execute quickly, which we
expect would make the tools a good ﬁt for the various constraints
of a laptop. Despite their low memory usage and fast execution, our
recommended pipeline can produce high-quality assemblies that are
suitable for fast initial in-ﬁeld analyses. We leave it to future work
to quantitatively study the genome assembly pipeline using nanopore
sequence data on laptops and other mobile devices.
Recommendations for Tool Developers
Based on our analyses, we make the following recommendations for
the tool developers.
• The choice of language to implement the tool plays a crucial role
regarding the overall performance of the tool. For example, although
the basecallers Scrappie and Nanonet belong to the same family (i.e.,
they both use the more accurate RNNs for basecalling), Scrappie
is signiﬁcantly faster than Nanonet since Scrappie is implemented
in C whereas Nanonet is implemented in Python (See analysis in
Section 4.1).
• Memory usage is an important factor that greatly affects the
performance and the usability of the tool. While developing new tools
or improving the current ones, the developers should be aware of
the memory hierarchy. Data structure choices that can minimize the
memory requirements and cache-efﬁcient algorithms have a positive
impact on the overall performance of the tools. Keeping memory usage
in check with the number of threads can enable not only a usable (i.e.,
runnable on machines with relatively small memories) tool but also a
fast one. For example, we ﬁnd that GraphMap cannot even run with a


## Page 14


14
Senol Cali et al.
single-thread in our desktop machine due to excessively high memory
usage (See analyses in Sections 4.1– 4.4).
• Scalability of the tool with the number of cores/threads is an important
requirement. It is important to make the tool efﬁciently parallelized to
decrease the overall runtime. Design choices should be made wisely
while considering the possible overheads that parallelization can add.
For example, we ﬁnd that the parallel speedup of Minimap reduces
when the number of threads reaches a high number due to a large
increase in the overhead of synchronization between threads (See
analyses in Sections 4.1– 4.4).
• Since parallelizing the tool can increase the memory usage, dividing
the input data into batches, or limiting the memory usage of each
thread, or dividing the computation instead of dividing the dataset
between simultaneous threads can prevent large increases in memory
usage, while providing performance beneﬁts from parallelization. For
example, in Nanonet, all of the threads share the computation of each
read, and thus memory usage is not affected by the amount of thread
parallelism. As a result, Nanonet’s usability is not limited to machines
with relatively larger memories (See analyses in Sections 4.1– 4.4).
6 Conclusion
We analyze the multiple steps and the associated state-of-the-art tools
inthegenomeassemblypipelineusingnanoporesequence data5 interms of
accuracy, speed, memory efﬁciency and scalability. We make four major
conclusions based on our experimental analyses of the whole pipeline.
First, the basecalling tools with higher accuracy and performance, like
Scrappie, can overcome the major drawback of nanopore sequencing
technology, i.e., high error rates. Second, the read-to-read overlap ﬁnding
tools, Minimap and GraphMap, perform similarly in terms of accuracy.
However, Minimap performs better than GraphMap in terms of speed
and memory usage by storing only minimizers instead of all k-mers, and
GraphMap is not scalable when running on machines with relatively small
memories. Third, the fast but less accurate assembler Miniasm can be used
for a very fast initial assembly, and further polishing can be applied on top
of it to increase the accuracy of the ﬁnal assembly. Fourth, a state-of-the-art
polishing tool, Racon, generates high-quality consensus sequences while
providing a signiﬁcant speedup over another polishing tool, Nanopolish.
We hope and believe that our observations and analyses will guide
researchers andpractitioners tomake conscious andeffectivechoices while
deciding between different tools for each step of the genome assembly
pipeline using nanopore sequence data. We also hope that the bottlenecks
or the effects of design choices we have found and exposed can help
developers in building new tools or improving the current ones.
Key Points
To our knowledge, this is the ﬁrst work that analyzes state-of-the-art
tools associated with each step of the genome assembly pipeline using
sequence data generated with nanopore sequencing, a promising new
sequencing technology.
The key contributions are:
1. We analyze the tools in multiple dimensions that are important for
both developers and users/practitioners: accuracy, performance, memory
usage and scalability.
2. We reveal new bottlenecks and tradeoffs that different combinations
of tools lead to, based on our extensive experimental analyses.
3. We provide guidelines for both practitioners, such that they can
determine the appropriate tools and tool combinations that can satisfy
5 We leave it to future work to quantitatively study tools for different
applications of nanopore sequencing, such as variant calling, detection of
base modiﬁcations (i.e., methylation studies [91]), and pathogen detection.
their goals, and tool developers, such that they can make design choices
to improve current and future tools.
4. We show that tools that are aware of the memory hierarchy have a
better overall performance and scalability, and they are more usable than
the tools that do not keep memory usage in check with the number of
threads.
5. We show that basecalling is the most important step of the pipeline
to overcome the high error rates of nanopore sequencing technology.
6. We show that there is a tradeoff between accuracy and performance
when choosing the tool for the assembly step. Miniasm, coupled with an
additional polishing step can lead to faster overall assembly than using
Canu itself, while producing high-quality assemblies.
Acknowledgments
We thank Jared Simpson and David Matei for their feedback and help
with the questions about the tools. Posters describing earlier stages of the
work in this paper were presented at PSB 2017 and ISMB-ECCB 2017.
We thank the poster session attendees for their feedback on the works.
We especially thank Adam M. Phillippy and Mile Šiki´c for their feedback
during the poster sessions. We also thank developers of Nanonet and Racon
for answering our questions on GitHub.
Funding
This work was supported by a grant from the National Institutes of
Health to O.M. and C.A. (HG006004); an installation grant from the
European Molecular Biology Organization to C.A. (EMBO-IG 2521); and
gifts from Google, Intel, Samsung, and VMware.
Author Details
Damla Senol Cali is a PhD student in the Department of Electrical
and Computer Engineering at Carnegie Mellon University. Her research
interests are in computational methods for the analysis of NGS and
nanopore sequencing data, and computer architecture.
Jeremie S. Kim is a PhD student in the Department of Electrical
and Computer Engineering at Carnegie Mellon University and in the
Department of Computer Science at ETH Zürich. His research interests
are in computer architecture and hardware accelerators for bioinformatics
applications.
Saugata Ghose, PhD, is a Systems Scientist in the Department of
Electrical and Computer Engineering at Carnegie Mellon University. His
research interests are in several aspects of computer architecture, with
a signiﬁcant focus on designing architecture-aware and systems-aware
memory and storage.
Can Alkan, PhD, is an Assistant Professor in the Department of
Computer Engineering at Bilkent University. His research interests are in
combinatorial algorithms for bioinformatics and computational biology.
Onur Mutlu, PhD, is a Professor in the Department of Computer
Science at ETH Zürich. He is also an Adjunct Professor in the Department
of Electrical and Computer Engineering at Carnegie Mellon University.
His research interests are in computer architecture, systems, security and
bioinformatics.
References
[1] Erwin L Van Dijk, Hélène Auger, Yan Jaszczyszyn, et al.
Ten
years of next-generation sequencing technology. Trends in Genetics,
30(9):418–426, 2014.
[2] Hongyi Xin, Donghyuk Lee, Farhad Hormozdiari, et al. Accelerating
read mapping with FastHASH. BMC Genomics, 14(1), 2013.
[3] Jay Shendure,
Shankar Balasubramanian,
George M Church,
et al.
DNA sequencing at 40: past, present and future.
Nature,
550(7676):345–353, 2017.


## Page 15


15
[4] Karyn Meltz Steinberg, Valerie A Schneider, Can Alkan, et al.
Building and improving reference genome assemblies. Proceedings
of the IEEE, 105(3):422–435, 2017.
[5] Todd J Treangen and Steven L Salzberg.
Repetitive DNA and
next-generation sequencing: computational challenges and solutions.
Nature Reviews Genetics, 13(1), 2011.
[6] Can Firtina and Can Alkan. On genomic repeats and reproducibility.
Bioinformatics, 32(15):2243–2247, 2016.
[7] Can Alkan, Saba Sajjadian, and Evan E Eichler. Limitations of next-
generation genome sequence assembly. Nature Methods, 8(1):61–65,
2011.
[8] Hengyun Lu, Francesca Giordano, and Zemin Ning.
Oxford
Nanopore MinION sequencing and genome assembly. Genomics,
Proteomics & Bioinformatics, 14(5):265–279, 2016.
[9] Alberto Magi, Roberto Semeraro, Alessandra Mingrino, et al.
Nanopore sequencing data analysis: state of the art, applications and
challenges. Brieﬁngs in Bioinformatics, 2017.
[10] James Clarke, Hai-Chen Wu, Lakmal Jayasinghe, et al. Continuous
base identiﬁcation for single-molecule nanopore DNA sequencing.
Nature Nanotechnology, 4(4):265–270, 2009.
[11] Vivien Marx. Nanopores: a sequencer in your backpack. Nature
Methods, 12(11), 2015.
[12] Daniel Branton,
David W Deamer,
Andre Marziali,
et al.
The potential and challenges of nanopore sequencing.
Nature
Biotechnology, 26(10):1146–1153, 2008.
[13] Thomas Laver,
J Harrison,
PA O’neill,
et al.
Assessing
the performance of the Oxford Nanopore Technologies MinION.
Biomolecular Detection and Quantiﬁcation, 3:1–8, 2015.
[14] Camilla LC Ip, Matthew Loose, John R Tyson, et al.
MinION
Analysis and Reference Consortium: Phase 1 data release and
analysis. F1000Research, 4, 2015.
[15] John J Kasianowicz,
Eric Brandin,
Daniel Branton,
et al.
Characterization of individual polynucleotide molecules using a
membrane channel.
Proceedings of the National Academy of
Sciences, 93(24):13770–13773, 1996.
[16] MinION,
Oxford
Nanopore
Technologies.
https://
nanoporetech.com/products/minion, 2017.
[17] Joshua Quick, Nicholas J Loman, Sophie Duraffour, et al. Real-
time, portable genome sequencing for Ebola surveillance. Nature,
530(7589), 2016.
[18] Joshua Quick, Aaron R Quinlan, and Nicholas J Loman. A reference
bacterial genome dataset generated on the MinION portable single-
molecule nanopore sequencer. Gigascience, 3(1), 2014.
[19] Miten Jain, Sergey Koren, Josh Quick, et al. Nanopore sequencing
and assembly of a human genome with ultra-long reads. bioRxiv,
2017.
[20] Nicholas J Loman.
Thar she blows! Ultra long read method
for nanopore sequencing. http://lab.loman.net/2017/03/
09/ultrareads-for-nanopore/, 2017.
[21] Mohammed-Amin Madoui, Stefan Engelen, Corinne Cruaud, et al.
Genome assembly using Nanopore-guided long and error-free DNA
reads. BMC Genomics, 16(1), 2015.
[22] First DNA Sequencing in Space a Game Changer.
https:
//www.nasa.gov/mission_pages/station/research/
news/dna_sequencing, 2017.
[23] Update: New R9 nanopore for faster, more accurate sequencing, and
new ten minute preparation kit. https://nanoporetech.com/
about-us/news/update-new-r9-nanopore-faster-
more-accurate-sequencing-and-new-ten-minute-
preparation, 2017.
[24] Mihai Pop.
Genome assembly reborn:
recent computational
challenges. Brieﬁngs in Bioinformatics, 10(4):354–366, 2009.
[25] Clive Brown Technical Update:
GridION X5 - The Sequel.
https://nanoporetech.com/resource-centre/
videos/gridion-x5-sequel, 2017.
[26] Carlos Victor de Lannoy, Dick de Ridder, and Judith Risse.
A
sequencer coming of age: de novo genome assembly using MinION
reads. bioRxiv, 2017.
[27] New basecaller now performs ’raw basecalling’,
for improved
sequencing accuracy. https://nanoporetech.com/about-
us/news/new-basecaller-now-performs-raw-
basecalling-improved-sequencing-accuracy, 2017.
[28] Haotien Teng, Michael B Hall, Tania Duarte, et al.
Chiron:
Translating nanopore raw signal directly into nucleotide sequence
using deep learning. bioRxiv, page 179531, 2017.
[29] Ryan R Wick, Louise M Judd, and Kathryn E Holt. Comparison
of Oxford Nanopore basecalling tools. https://github.com/
rrwick/Basecalling-comparison, 2017.
[30] Metrichor,
Oxford
Nanopore
Technologies.
https:
//nanoporetech.com/products/metrichor, 2017.
[31] Sean R Eddy. Hidden markov models. Current Opinion in Structural
Biology, 6(3):361–365, 1996.
[32] Mike Schuster and Kuldip K Paliwal. Bidirectional recurrent neural
networks. IEEE Transactions on Signal Processing, 45(11):2673–
2681, 1997.
[33] Barak A Pearlmutter. Learning state space trajectories in recurrent
neural networks. Neural Computation, 1(2):263–269, 2008.
[34] Nanonet,
Oxford
Nanopore
Technologies.
https://
github.com/nanoporetech/nanonet, 2017.
[35] Nanonet:
First
Generation
RNN
Basecaller.
https://
github.com/nanoporetech/nanonet.
[36] Scrappie,
Oxford
Nanopore
Technologies.
https://
github.com/nanoporetech/scrappie, 2017.
[37] Matei David, Lewis Jonathan Dursi, Delia Yao, et al.
Nanocall:
an open source basecaller for Oxford Nanopore sequencing data.
Bioinformatics, 33(1):49–55, 2016.
[38] Nanocall:
An
Oxford
Nanopore
Basecaller.
https://
github.com/mateidavid/nanocall, 2017.
[39] Vladimír Boža, Broˇna Brejová, and Tomáš Vinaˇr. DeepNano: Deep
recurrent neural networks for base calling in MinION nanopore reads.
PloS One, 12(6), 2017.
[40] Ivan Sovi´c, Mile Šiki´c, Andreas Wilm, et al.
Fast and sensitive
mapping of nanopore sequencing reads with GraphMap.
Nature
Communications, 7, 2016.
[41] Heng Li. Minimap and Miniasm: fast mapping and de novo assembly
for noisy long sequences. Bioinformatics, 32(14):2103–2110, 2016.
[42] Sergey Koren, Brian P Walenz, Konstantin Berlin, et al.
Canu:
scalable and accurate long-read assembly via adaptive k-mer
weighting and repeat separation. Genome Research, 27(5):722–736,
2017.
[43] Pavel A Pevzner, Haixu Tang, and Michael S Waterman. An Eulerian
path approach to DNA fragment assembly.
Proceedings of the
National Academy of Sciences, 98(17):9748–9753, 2001.
[44] Phillip EC Compeau, Pavel A Pevzner, and Glenn Tesler. How to
apply de Bruijn graphs to genome assembly. Nature Biotechnology,
29(11):987–991, 2011.
[45] Sergey Koren, Gregory P Harhay, Timothy PL Smith, et al. Reducing
assembly complexity of microbial genomes with single-molecule
sequencing. Genome Biology, 14(9), 2013.
[46] Justin Chu, Hamid Mohamadi, René L Warren, et al. Innovations
and challenges in detecting long read overlaps: an evaluation of the
state-of-the-art. Bioinformatics, 33(8):1261–1270, 2016.
[47] Zhenyu Li, Yanxiang Chen, Desheng Mu, et al. Comparison of the
two major classes of assembly algorithms: overlap–layout–consensus
and de-bruijn-graph. Brieﬁngs in Functional Genomics, 11(1):25–37,
2012.
[48] Stefan Burkhardt and Juha Kärkkäinen. Better ﬁltering with gapped
q-grams. Fundamenta Informaticae, 56(1-2):51–70, 2003.
[49] Canu
Tutorial.
http://canu.readthedocs.io/en/
latest/tutorial.html, 2017.
[50] Heng Li. Aligning sequence reads, clone sequences and assembly
contigs with BWA-MEM. arXiv preprint arXiv:1303.3997, 2013.
[51] Nicholas J Loman, Joshua Quick, and Jared T Simpson. A complete
bacterial genome assembled de novo using only nanopore sequencing
data. Nature Methods, 12(8):733–735, 2015.


## Page 16


16
Senol Cali et al.
[52] Robert Vaser, Ivan Sovi´c, Niranjan Nagarajan, et al. Fast and accurate
de novo genome assembly from long uncorrected reads. Genome
Research, 27(5):737–746, 2017.
[53] Nanopolish. https://github.com/jts/nanopolish.
[54] Christopher Lee, Catherine Grasso, and Mark F Sharlow. Multiple
sequence alignment using partial order graphs.
Bioinformatics,
18(3):452–464, 2002.
[55] Nicholas J Loman.
Nanopore R9 rapid run data release.
http://lab.loman.net/2016/07/30/nanopore-r9-
data-release/, 2017.
[56] MUMmer 3.x.
https://github.com/garviz/MUMmer,
2017.
[57] Ilya Sutskever, Oriol Vinyals, and Quoc V Le. Sequence to sequence
learning with neural networks. In Proceedings of the Advances in
Neural Information Processing Systems, pages 3104–3112. Neural
Information Processing Systems Foundation, 2014.
[58] G David Forney. The Viterbi algorithm. Proceedings of the IEEE,
61(3):268–278, 1973.
[59] Debbie Marr, Frank Binns, D Hill, et al. Hyper-threading technology
in the NetBurst® microarchitecture. 14th Hot Chips, 2002.
[60] William Magro,
Paul Petersen,
and Sanjiv Shah.
Hyper-
threading technology: impact on compute-intensive workloads. Intel
Technology Journal, 6(1), 2002.
[61] Nathan Tuck and Dean M. Tullsen.
Initial observations of the
simultaneous multithreading Pentium 4 processor. In Proceedings
of the 12th International Conference on Parallel Architectures and
Compilation Techniques, PACT, Washington, DC, USA, 2003. IEEE
Computer Society.
[62] Dean M. Tullsen, Susan J. Eggers, and Henry M. Levy. Simultaneous
multithreading: Maximizing on-chip parallelism. In Proceedings of
the 22nd Annual International Symposium on Computer Architecture,
ISCA, New York, NY, USA, 1995. ACM.
[63] Susan J Eggers, Joel S Emer, Henry M Levy, et al. Simultaneous
multithreading: A platform for next-generation processors.
IEEE
Micro, 17(5):12–19, 1997.
[64] Dean M Tullsen, Susan J Eggers, Joel S Emer, et al. Exploiting
choice: Instruction fetch and issue on an implementable simultaneous
multithreading processor.
In Proceedings of the 23rd Annual
International Symposium on Computer Architecture, ISCA, pages
191–202, New York, NY, USA, 1996. ACM.
[65] Wayne Yamamoto and Mario Nemirovsky. Increasing superscalar
performance through multistreaming. In Proceedings of the Working
Conference on Parallel Architectures and Compilation Techniques,
PACT, pages 49–58, Manchester, UK, 1995. IFIP Working Group on
Algol.
[66] Hiroaki Hirata, Kozo Kimura, Satoshi Nagamine, et al.
An
elementary processor architecture with simultaneous instruction
issuing from multiple threads. In Proceedings of the 19th Annual
International Symposium on Computer Architecture, ISCA, pages
136–145, New York, NY, USA, 1992. ACM.
[67] Chuan-Le Xiao, Ying Chen, Shang-Qian Xie, et al. MECAT: fast
mapping, error correction, and de novo assembly for single-molecule
sequencing reads. Nature Methods, 14(11):1072, 2017.
[68] Heng Li and Richard Durbin. Fast and accurate short read alignment
with Burrows–Wheeler transform.
Bioinformatics, 25(14):1754–
1760, 2009.
[69] Ben Langmead, Cole Trapnell, Mihai Pop, et al.
Ultrafast and
memory-efﬁcient alignment of short DNA sequences to the human
genome. Genome Biology, 10(3), 2009.
[70] Can Alkan,
Jeffrey M Kidd,
Tomas Marques-Bonet,
et al.
Personalized copy number and segmental duplication maps using
next-generation sequencing.
Nature Genetics, 41(10):1061–1067,
2009.
[71] Faraz Hach, Fereydoun Hormozdiari, Can Alkan, et al. mrsFAST: a
cache-oblivious algorithm for short-read mapping. Nature Methods,
7(8):576–577, 2010.
[72] Michael C Schatz. CloudBurst: highly sensitive read mapping with
MapReduce. Bioinformatics, 25(11):1363–1369, 2009.
[73] Heng Li, Jue Ruan, and Richard Durbin.
Mapping short DNA
sequencing reads and calling variants using mapping quality scores.
Genome Research, 18(11):1851–1858, 2008.
[74] Jeremie S Kim, Damla Senol Cali, Hongyi Xin, et al. GRIM-Filter:
Fast seed location ﬁltering in DNA read mapping using Processing-
in-Memory technologies. BMC Genomics, 2018, in press.
[75] Hongyi Xin,
John Greth,
John Emmons,
et al.
Shifted
Hamming distance: a fast and accurate SIMD-friendly ﬁlter to
accelerate alignment veriﬁcation in read mapping. Bioinformatics,
31(10):1553–1560, 2015.
[76] Mohammed Alser, Hasan Hassan, Hongyi Xin, et al. GateKeeper:
a new hardware architecture for accelerating pre-alignment in DNA
short read mapping. Bioinformatics, 33(21):3355–3363, 2017.
[77] Mohammed Alser, Onur Mutlu, and Can Alkan.
MAGNET:
understanding and improving the accuracy of genome pre-alignment
ﬁltering. IPSI Transactions on Internet Research, 13(2), 2017.
[78] David Weese, Anne-Katrin Emde, Tobias Rausch, et al. RazerS-
fast read mapping with sensitivity control.
Genome Research,
19(9):1646–1654, 2009.
[79] Wan-Ping Lee, Michael P Stromberg, Alistair Ward, et al. MOSAIK:
a hash-based algorithm for accurate next-generation sequencing
short-read mapping. PloS One, 9(3), 2014.
[80] Stephen M Rumble, Phil Lacroute, Adrian V Dalca, et al. SHRiMP:
accurate mapping of short color-space reads. PLoS Computational
Biology, 5(5), 2009.
[81] Matei David, Misko Dzamba, Dan Lister, et al. SHRiMP2: sensitive
yet practical short read mapping. Bioinformatics, 27(7):1011–1012,
2011.
[82] Ayat Hatem, Doruk Bozda˘g, Amanda E Toland, et al. Benchmarking
short sequence mapping tools. BMC Bioinformatics, 14(1), 2013.
[83] Corey B Olson, Maria Kim, Cooper Clauson, et al.
Hardware
acceleration of short read mapping.
In Proceedings of the 20th
Annual International Symposium on Field-Programmable Custom
Computing Machines (FCCM), pages 161–168. IEEE Computer
Society, 2012.
[84] Nuno A Fonseca, Johan Rung, Alvis Brazma, et al. Tools for mapping
high-throughput sequencing data.
Bioinformatics, 28(24):3169–
3177, 2012.
[85] Heng Li and Richard Durbin. Fast and accurate long-read alignment
with Burrows–Wheeler transform. Bioinformatics, 26(5):589–595,
2010.
[86] Enrico Siragusa, David Weese, and Knut Reinert. Fast and accurate
read mapping with approximate seeds and multiple backtracking.
Nucleic Acids Research, 41(7), 2013.
[87] HengLi. Minimap2: fastpairwisealignmentforlongDNAsequences.
arXiv Preprint arXiv 1708.01492, 2017.
[88] Heng Li, Bob Handsaker, Alec Wysoker, et al.
The sequence
alignment/map format and SAMtools. Bioinformatics, 25(16):2078–
2079, 2009.
[89] Peter JA Cock, Christopher J Fields, Naohisa Goto, et al.
The
Sanger FASTQ ﬁle format for sequences with quality scores, and
the Solexa/Illumina FASTQ variants.
Nucleic Acids Research,
38(6):1767–1771, 2009.
[90] William R Pearson and David J Lipman. Improved tools for biological
sequence comparison.
Proceedings of the National Academy of
Sciences, 85(8):2444–2448, 1988.
[91] Jared T Simpson, Rachael E Workman, PC Zuzarte, et al. Detecting
DNA cytosine methylation using nanopore sequencing.
Nature
Methods, 14(4):407, 2017.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1711_08774v4_nanopore_sequencing_technology_and_tools_for_genome_assembly_computational_anal
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1711_08774V4_NANOPORE_SEQUENCING_TECHNOLOGY_AND_TOOLS_FOR_GENOME_ASSEMBLY_COMPUTATIONAL_ANAL.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
