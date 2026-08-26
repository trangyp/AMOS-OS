---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1812.09490v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1812.09490v3_Aztarna__a_footprinting_tool_for_robots

> Source: 1812.09490v3_Aztarna__a_footprinting_tool_for_robots.pdf

> Pages: 25

---


## Page 1


AZ
TAR
NA
A footprinting tool for robots
W H I T E  PA P E R
R O B O T  C Y B E R S E C U R I T Y
arXiv:1812.09490v3  [cs.CR]  21 Sep 2019


## Page 2


aztarna, a footprinting tool for robots
Víctor Mayoral Vilches, Gorka Olalde Mendia, Xabier Perez Baskaran,
Alejandro Hernández Cordero, Lander Usategui San Juan, Endika Gil-Uriarte,
Odei Olalde Saez de Urabain and Laura Alzola Kirschgens
Alias Robotics S.L.
Vitoria-Gasteiz, Araba - Álava
Spain
September 24, 2019
Abstract
Industry 4.0 is changing the commonly held assumption that robots are to be deployed in closed and
isolated networks. When analyzed from a security point of view, the global picture is disheartening:
robotics industry has not seriously allocated effort to follow good security practices in the robots pro-
duced. Instead, most manufacturers keep forwarding the problem to the end-users of these machines.
As learned in previous technological revolutions, such as at the dawn of PCs or smartphones, action
needs to be taken in time to avoid disastrous consequences. In an attempt to provide the robotics and
security communities with the right tools to perform assessments, in this paper we present aztarna,
a footprinting tool for robotics.
We discuss how such tool can facilitate the process of identifying
vestiges of different robots, while maintaining an extensible structure aimed for future ﬁngerprinting
extensions. With this contribution, we aim to raise awareness and interest of the robotics community,
robot manufacturers and robot end-users on the need of starting global actions to embrace security.
We open source the tool and disclose preliminary results that demonstrate the current insecurity land-
scape in industry.
We argue that the robotic ecosystem is in need of generating a robot security
community, conscious about good practices and empowered by the right tools.
1
Introduction
Robotics is claimed to be the next technological revolution, and an onset of a new era, dominated by in-
telligent entities that contribute to human development. Nowadays, robots are no longer only deployed
in research oriented organizations, but increasingly handle big amounts of personal and industrial data,
perform a variety of automated tasks in industrial scenarios or help humans handle the most hazardous
activities. Lately, robot cybersecurity is under question, because recent research shown out the insecu-
rity status of the state of the art in the robotics era [1, 2] and underlined how downstream implications
of vulnerable robots are surpassing those of conventional Information Technologies [3]. Some laudable
efforts have pointed out an array of internet-exposed robots [4] that are easily accessible for a remote
user by searching for a speciﬁc pattern, namely a robot footprint.
The example provided by the authors is just a plain particular snapshot of the dooming stage of inse-
curity of robotics, down to more restrictive scenarios, such as industry, professional environments or
simulations and gamiﬁcation platforms [5]. The authors in [4] mention that the results were surprising
for themselves. However, they do not provide additional details or resources to reproduce the method
disclosed in the research paper, nor dig more on the nature of the ﬁndings and downstream implica-
tions.
2


## Page 3


Footprinting, also known as reconnaissance is the blueprinting of the security proﬁle of a digital sys-
tem and its organization, undertaken in a methodological manner. To get this information, typically,
a security analyst might use various tools and technologies such as whois, nslookup, traceroute,
enumerators or pinging. When applied to robotics, we deﬁne robot footprinting as the technique used
for gathering information about robots and the entities they belong to. This information becomes very
useful when performing security analysis over speciﬁc systems.
While footprinting is often understood as a mechanism to obtain network information about a digital
system in a generalized manner and using common tools, ﬁngerprinting implies ﬁne tuning the net-
working requests to elicit a speciﬁc signature response from the target device. The procedure allows
to obtain additional information such as the Operating System, its version, speciﬁc libraries deployed,
etc. The boundary between both aspects, footprinting and ﬁngerprinting, is often unclear for new digi-
tal systems since one requires the other and depends on the tools available. When looking at robotics,
we notice that neither footprinting nor ﬁngerpriting tools have been made available. The direct impli-
cation of this fact is that the security researcher, in all cases, needs to develop its own tools.
In an attempt to provide the robotics and security communities with the right tools to perform as-
sessments, we discuss aztarna, a security tool that enables robot footprinting. We discuss how such
tool can facilitate the process of identifying blueprints of different robots, while maintaining a extensi-
ble structure aimed for future ﬁngerprinting extensions. Section 2 will introduce some of the prior work
and results available. Section 3 will present the aztarna tool, discuss its structure, supported robotic
technologies and demonstrate its capabilities through several examples. Section 4 will describe the
results obtained while experimenting with aztarna. Finally, section 5 will provide some remarks and
share a few pointers towards extensions of aztarna meant for robot ﬁngerprinting.
2
Previous work
Reconaissance practice is very common in an increasing number of ﬁelds of interest, such as websites,
with tactics that contribute to a pre-attack phase. Several reconaissance tactiques have arised in the
past decades, some of them soundly noticeable, such as massive port scans, whereas others stay unno-
ticed, below the radar. Internet-wide scans in search for connected machines is a well known practice
in the ﬁeld of cybersecurity, with several ﬁrst order platforms and tools that help to simplify the pro-
cess. This is the case of Shodan.io[6], which comprises all the results found by different background
scans that are recurrently running in dedicated servers.
Numerous studies have focused upon Industrial Control Systems[7] and some other related practices
such as Supervisory Control And Data Acquisition (SCADA) control systems. However, not many scans
have focused on robots. The work published by the RoboSec project team[8], with robots of a partic-
ular manufacturer in industrial environments, is the positive exception. Yet, the emerging popularity
of collaborative robots, which often bring new architectures, as well as the advent of popular robotics
frameworks, such as the Robot Operating System (ROS), deserve careful study. At the time of writ-
ing, the most pioneering study in the area has been performed by a team of researchers from Brown
University [4], mainly reporting a proto-footprinting method arising from the ﬁndings of ROS instances
and robots around the world. The results presented by this team exploited the default conﬁguration of
the ROS master, appointed at the 11311 port and available across the Internet.
As introduced above, to the best of our knowledge, the concept of footprinting is diffuse and domain
speciﬁc in the cybersecurity context. Some researchers claim that the footprinting process is com-
pletely passive, by using information publicly available through third party sources. Others empower
both active or passive means of collecting useful information for any target as a reconnaissance step
of an attack [9]. In the case of ﬁngerprinting, the existing literature refers to it as "determining the
3


## Page 4


nature of the target by comparing signs provided by the responses of the target against databases or
known responses that determine the OS or the application in use". In case of web technologies, user
ﬁngerprinting could refer to the techniques of indistinctly determining the user, through a signature or
ﬁngerprint generated by his/her browsing activity and via signs left by the browser and OS in use[10].
When applying this to the context of robotics, given that the target scope is not a complete organiza-
tion, but a speciﬁc set of devices in that organization1, the meaning of footprinting and ﬁngerprinting
changes accordingly. In this context, footprinting could mean obtaining all the possible information
from a single robot or group of robots, whereas ﬁngerprinting could be denoted as obtaining infor-
mation that can unequivocally identify a single robot device, e.g. a serial number, its OS version or
particular details about its robotics framework layout and conﬁguration.
The present piece of research aims to improve, systematize and extend the results of previous studies
[8, 4] while empowering security researchers with robot footprinting tools. We target ROS as well as
other relevant and more secure robot setups, such as Secure ROS (SROS) or ROS 2. Beyond robotics
frameworks, our work also targets other robots that do not necessarily employ these popular middle-
wares. Throughout the following sections, we disclose and describe an open source robot footprinting
tool named aztarna, that can be used to reproduce our work and allows for future extensions thanks
to its architecture. We discuss such modular architecture and present the initial set-of-supported robot
technologies. Ultimately, we discuss against a security by obscurity approach and instead advocate
for hacker-tested robot security. While by no means Alias Robotics encourages or promotes unautho-
rized tampering of running robotic systems.
Instead we value the importance to empower security
researchers and raise security-awareness among roboticists, by releasing an robot security auditing
tool.
3
aztarna
Robot target
Security researcher: aztarna
Phase 1
Phase 1
Scan and analyze
Phase 2
Phase 2
Footprint
Phase 3
Phase 3
Fingerprint (outside of the scope)
Figure 1: Sequence diagram of aztarna.
In Basque language, aztarna means blueprint or mark, in its various forms and meanings. Those
include footprint (aztarna in Basque) and ﬁngerprint (hatz-aztarna). Even in such an ancient language,
1Note that we understand robots as cyber-physical systems composed by at least three different elements, sensors to perceive
the world, actuators to have a physical impact on it and cognition devices which coordinate the information from sensors and
command actuators.
4


## Page 5


this same word may be used to name marks upon a given surface and also describe vestiges appertain-
ing to a concrete organism or entity. Thus, the pre-romanic language was accurate at the time when
deﬁning a word that adheres very well to the deﬁnition of robot footprinting; which basically stands for
the information gathering on the reconnaissance phase. Thereafter, particular identiﬁcation deepens
into each particular robot through a process that requires crafting speciﬁc requests. Such process,
known as ﬁngerprinting deepens into unique identiﬁers or features of a particular robot, e.g. OS, li-
braries, versions or particular communication middlewares signatures.
Motivated by the lack of dedicated tooling for security research in the ﬁeld of robotics, we have devel-
oped aztarna, a tool aimed to help in the detection and scan of robots and robot technologies (including
software components) on a network. The tool, developed in Python 3, helps to search for connected
robots and gathers some information from those found.
Figure 1 illustrates the philosophy behind the aztarna tool. There are three well identiﬁed phases
that may repeat for each target. For the purpose of this article, our work will focus on the ﬁrst two
phases -scanning and footprinting-, leaving ﬁngerprinting for future work. The architecture of aztarna
has been designed to favour its extension towards more and more robotic technologies. The struc-
ture of the ﬁles within the tool is illustrated in listing 1 where lines 14, 16 and 18 show three folders
that contain robot technology-speciﬁc code for its footprinting, namely robot adapters. Further exten-
sions can follow a similar pattern and implement the corresponding functions enabling additional robot
technology.
1
aztarna/
2
Dockerfile
3
README.md
4
aztarna
5
init__.py
6
__main__.py
7
cmd.py
8
commons.py
9
helpers.py
10
ros
11
init__.py
12
commons.py
13
helpers.py
14
ros
15
...
16
sros
17
...
18
industrialrouters
19
helpers.py
20
scanner.py
21
...
22
docs
23
Makefile
24
...
25
...
Listing 1: aztarna code structure, simpliﬁed version.
aztarna has different work modes that allow to use the tool in different scenarios, and together with
other tools. The robot footprinting tool provides ﬂexibility when deciding on the hosts to scan, which
5


## Page 6


can be loaded from an input ﬁle, determined by a network IP range, or even loaded from stdin as part
of a pipe. This allows to use aztarna in conjunction with tools aimed for massive scans such as [11]
ZMap, to scan vast amounts of hosts, even the whole Internet network range. Regarding the ports to
scan, the tool also allows to choose between a single port, a range of ports or a port list.
For large scan performance improvement, aztarna provides a basic and a extended mode of scan.
With the same purpose, extensive usage of asynchronous development has been used, with the help of
Python AsyncIO. This allows the application to handle a big number of concurrent connections without
the usage of threads, and improves the performance substantially in comparison to them.
The results provided by aztarna can be exported to standard CSV ﬁles, containing all the data gathered
from the nodes. This allows to employ results for future analysis. The output ﬁle contains a common
structure including all the ﬁndings, that when exported to third party tools provide ways to ﬁlter the
results by resource type, names, addresses, and therefore, by found robots. The usage of aztarna is
straightforward, as all the different behaviours are deﬁned by command line parameters, which are
described when calling the tool with no parameters.
In the following section we will brieﬂy cover aztarna’s robot adapters, the abstraction used to support
additional robot technologies. We will discuss the structure of a robot adapter and introduce a few
examples.
3.1
Robot adapters
Similar to what happened in the computer industry, there is a plurality of robot manufacturers, each us-
ing its own hardware and software. As a tool to footprint robots and robot-related technology, aztarna
provides a common skeleton that can easily be extended to support new software or hardware robot
components. New components are extended via robot adapters, abstractions that enlarge the base
class RobotAdapter. Robot adapters provide the methods to footprint the corresponding robot technol-
ogy and are typically organized in folders.
The sections below describe some of the supported robots and robot components within aztarna.
3.1.1
Robot Operating System (ROS) adapter
In the case of ROS, the connection is made directly to the master via XMLRPC, from which all informa-
tion sent by nodes is inferred. This information consists on nodes, topics, services, parameters and all
the interactions between them, including subscriptions and publications.
Figure 2 provides insight on the Phases 1 and 2 of aztarna for ROS2.
The usage of the aztarna’s ROS robot adapter is demonstrated in Listing 2. The tool is invoked with
the -t ROS ﬂag, indicating that the robot adapter should use ROS one. Furthermore, ﬂags -p and -a
mean the range of ports and addresses to be scanned.
Listing 2 mainly represents Figure’s 2 Phase 1: Scan and analyze.
Making use of the ROS Master
API, aztarna sends getsystemstate() requests to the corresponding ports and addresses. Based on
the responses received, the tool analyses the information and determines which host-port combination
contains a ROS Master.
aztarna can also be launched with additional ﬂags that allow the tool to perform footprinting actions.
In particular and as depicted in Figure 2 Phase 2: Footprint, when using the aztarna’s ﬂag -e, more
information about a particular ROS host can be obtained through the exploitation of the ROS Master
2Logic implemented and available at https://github.com/aliasrobotics/aztarna/tree/master/aztarna/ros/ros
6


## Page 7


Robot target
Security researcher: aztarna
Invoke getsystemstate()
Return basic footprint
Phase 1
Phase 1
Scan and analyze
Fetch nodes URI through lookupNodes()
Fetch list of topics through getTopicTypes()
Node 1
Node 1
Fetch nodes URI through lookupNodes()
Fetch list of topics through getTopicTypes()
Node N
Node N
Phase 2
Phase 2
Footprint
Figure 2: Sequence diagram of a aztarna scanning a ROS target.
API. Listing 3 shows en example.
When combined with the ROS robot adapter, aztarna provides security researchers the tools to inspect
and footprint ROS deployments across different networks. Moreover, the tool can be conjoint with other
Linux commands to perform complete analysis over particular systems. Listing 4 provides an example
of how aztarna can be used to ﬁnd unmodiﬁed ROS instances in particular machines using its loopback
virtual network interface.
7


## Page 8


1
root@3c22d4bbf4e1:/# aztarna -t ROS -p 11311-11320 -a 127.0.0.1
2
root@432b0c5f61cc:~/aztarna# aztarna -t ROS -p 11311-11320 -a 127.0.0.1
3
[-] Error connecting to host Address: 127.0.0.1: Cannot connect to host 127.0.0.1:11315 ssl:None [Connection refused]
4
Not a ROS host
5
[-] Error connecting to host Address: 127.0.0.1: Cannot connect to host 127.0.0.1:11312 ssl:None [Connection refused]
6
Not a ROS host
7
...
8
[+] ROS Host found at 127.0.0.1:11317
9
[+] ROS Host found at 127.0.0.1:11311
Listing 2: aztarna using the ROS robot adapter.
1
root@aa6b6d7f9bd3:/# aztarna -t ROS -p 11311 -a 127.0.0.1 -e
2
[+] ROS Host found at 127.0.0.1:11311
3
4
Node: /rosout XMLRPCUri: \protect\vrule width0pt\protect\href{http://aa6b6d7f9bd3:39719}{http://aa6b6d7f9bd3:39719}
5
6
Published topics:
7
* /rosout_agg(Type: rosgraph_msgs/Log)
8
9
Subscribed topics:
10
* /rosout(Type: rosgraph_msgs/Log)
11
12
Services:
13
* /rosout/set_logger_level
14
* /rosout/get_loggers
15
16
CommunicationROS 0:
17
- Publishers:
18
- Topic: /rosout(Type: rosgraph_msgs/Log)
19
- Subscribers:
20
/rosout XMLRPCUri: \protect\vrule width0pt\protect\href{http://aa6b6d7f9bd3:39719}{http://aa6b6d7f9bd
21
22
CommunicationROS 1:
23
- Publishers:
24
/rosout XMLRPCUri: \protect\vrule width0pt\protect\href{http://aa6b6d7f9bd3:39719}{http://aa6b6d7f9bd
25
- Topic: /rosout_agg(Type: rosgraph_msgs/Log)
26
- Subscribers:
Listing 3: aztarna using ROS robot adapter to perform footprinting (Phase 2 from Figure 2)
8


## Page 9


1
root@bc6af321d62e:/# nmap -p 1-65535 127.0.0.1 | grep open | awk '{print $1}' | sed "s*/tcp**" | \
2
sed "s/^/aztarna -t ROS -p /" | sed "s/$/ -a 127.0.0.1/" | bash
3
[+] ROS Host found at 127.0.0.1:11311
4
[+] ROS Host found at 127.0.0.1:11317
5
[-] Error connecting to host 127.0.0.1:38069 -> Unknown error
6
Not a ROS host
7
[-] Error connecting to host 127.0.0.1:38793 -> Unknown error
8
Not a ROS host
9
[-] Error connecting to host 127.0.0.1:45665 -> <type 'exceptions.Exception'>:method "getSystemState" is not supported
10
Not a ROS host
11
[-] Error connecting to host 127.0.0.1:46499 -> <type 'exceptions.Exception'>:method "getSystemState" is not supported
12
Not a ROS host
13
...
Listing 4: aztarna’s use case which checks for all ROS instances in the loopback virtual interface of a
given machine
9


## Page 10


3.1.2
Secure ROS (SROS) adapter
Robot target
Security researcher: aztarna
Client Hello
Phase 1
Phase 1
Scan
Server Certiﬁcate
Client Certiﬁcate Request
Server Hello Done
Phase 2
Phase 2
Fingerprinting
Disconnect TCP session
Phase 2
Phase 2
Close Connection
Figure 3: Sequence diagram of a aztarna performing the scan and ﬁngerprinting phases for SROS.
In the case of SROS, as the connection to the master is not possible due to the requirement of a client
certiﬁcate, the policies that are publicly available in the certiﬁcate presented by the server are used[12]
to gather information. These policies come in the form of standard x509 certiﬁcate policies and consist
of an unique object identiﬁer(OID), as well as in an optional classiﬁer[13], being able to introduce wild-
card characters in order to cover a group of target objects.
1
X509v3 Certificate Policies: critical
2
Policy: 1.2.3.4.5.6.7.8.9.1.1
3
CPS: /rosout
4
Policy: 1.2.3.4.5.6.7.8.9.2.1
5
CPS: /rosout
6
CPS: /rosout_agg
7
Policy: 1.2.3.4.5.6.7.8.9.3.2
8
CPS: **
9
Policy: 1.2.3.4.5.6.7.8.9.4.1
10
CPS: /rosoutpy/get_loggers
11
CPS: /rosoutpy/set_logger_level
12
Policy: 1.2.3.4.5.6.7.8.9.5.1
13
CPS: /enable_statistics
14
CPS: /tcp_keepalive
15
CPS: /use_sim_time
16
Policy: 1.2.3.4.5.6.7.8.9.6.2
17
CPS: **
18
Listing 5: Certiﬁcate policies present in rosout.py node certiﬁcate
Policies on SROS are deﬁned to specify which topics a node can subscribe or publish to, which services
it can call, as well as which parameters can it read or write.
10


## Page 11


Each of this policies consist of a unique OID for each of the nodes and types of policies, as well as
multiple values for each of the policies. An example of the policies for the rosout.py node is shown in
Listing 5.
As the standard libraries available for managing TLS connections in Python do not support obtaining
the server certiﬁcate in those cases where the connection is not completed, manual handling of the
connection is required. For that purpose, Scapy[14] library is used, along with the TLS support layer
available in the library.
In the case of the SROS adapter, it is no possible to infer the information only from the master, as the
policies are unique for each node certiﬁcate. To obtain all the information about the system, a port
scan on the host is required to determine the active nodes.
For each of these nodes, a TLS connection is performed by which the policies are obtained. The poli-
cies for each of the nodes show the resources that the given node has allowed or denied the access to.
These resources include publication or subscription to topics, calls to services and read or modiﬁcation
of parameters. Due to the extended timespan required to scan SROS hosts, the -e ﬂag has special note-
worthiness. Launching a plain scan will result only in scanning the master node, whereas launching
the scan with the -e ﬂag will cause to perform the port scan and connection to each of the found ports.
Apart from the information provided by the certiﬁcate policies, valuable information is also acquired
from the certiﬁcate subject ﬁelds. It is a common practice for organizations to set valid information re-
garding to the organization itself, as well as for the person or the organization in charge of issuing the
certiﬁcates. This data is considered very valuable in reconnaissance scenarios. In the ﬁeld of interest,
this subject could identify the owner corporation of the found robot, as well as the person responsible
for the secure conﬁguration of the robots, which could ease the effort required to determine a possible
target for social-engineering attack in the case of a malicious actor.
Listing 6 shows an excerpt of the output showing the subject and issuer information for the certiﬁcate
chain of the Google website.
1
bash-3.2$ openssl s_client -connect www.google.com:443
2
CONNECTED(00000008)
3
depth=2 OU = GlobalSign Root CA - R2, O = GlobalSign, CN = GlobalSign
4
verify return:1
5
depth=1 C = US, O = Google Trust Services, CN = Google Internet Authority G3
6
verify return:1
7
depth=0 C = US, ST = California, L = Mountain View, O = Google LLC, CN = www.google.com
8
verify return:1
Listing 6: OpenSSL call fetching Google website certiﬁcate issuer information.
In the case of SROS, apart of fetching the subject information, a check is performed in order to deter-
mine if the demo setup is being used.
The certiﬁcates issued by the demo setup provided by SROS always contain the same values as the
issuer, which causes them to be easily recognizable, specially given that the setup includes a typo on
the State ﬁeld, calling it Sate, as shown in Listing 7
11


## Page 12


1
bash-3.2$ openssl s_client -connect 127.0.0.1:11311
2
CONNECTED(00000006)
3
depth=2 ST = Sate, O = Organization, C = ZZ, OU = Organizational Unit, CN = root, L = Locality
4
verify error:num=19:self signed certificate in certificate chain
5
verify return:0
Listing 7: OpenSSL call showing SROS demo setup certiﬁcate.
While not a issue by itself, the usage of the demo setup could give an insight on the security posture of
a robot user. It could also be a good metric to deﬁne if the system is for testing purposes or in a real
production environment.
In order to perform a scan with aztarna in search for SROS based systems, the -t SROS argument is
used. This type of scan searches for a master running SROS, establishes a connection for collecting
the server certiﬁcate and ﬁnally recovers the data from this certiﬁcate. In this case, given that the
master doesn’t have any policy information, only the information regarding to the certiﬁcate subject is
gathered and the check for the demo setup is performed. In Listing 8, the output of an example scan is
shown.
1
bash-3.2$ ./aztarna -t SROS -a 192.168.64.131
2
Connecting to 192.168.64.131:11311
3
[+] SROS host found!!!
4
192.168.64.131:11311
5
Node name: master
6
Port: 11311
7
Demo CA Used: True
Listing 8: aztarna using SROS robot adapter to perform a basic footprinting scan.
For the purpose of gathering information regarding to all the nodes in the system, an extended scan
must be performed. The extended scan comprises a full scan of the target host, in which all the ports
are checked for existing nodes.
For performing the scan, in the ﬁrst place, the presence of a SROS master is checked in the selected
ports, or in the default 11311 port, if not speciﬁed. If a SROS master is found, the tool performs a
full port scan on the target host seeking the presence of nodes. For each found port, the tool attempts
to establish a TLS connection and gather server certiﬁcates.
In the same manner, for each of the
successfully collected certiﬁcates, the node policies and subject information are collected. Due to the
time required and the noise generated during the performance of a full port scan, this scan is only
recommended for a low number of target hosts. A simpliﬁed example with the output of one extended
scan is shown in Listing 9.
12


## Page 13


1
bash-3.2$ ./aztarna -t SROS -a 192.168.64.131 -e
2
Connecting to 192.168.64.131:11311
3
[+] SROS host found!!!
4
Scanning host 192.168.64.131:39189
5
Scanning host 192.168.64.131:35383
6
...
7
Scanning host 192.168.64.131:38429
8
Scanning host 192.168.64.131:11310
9
...
10
(IPv4Address('192.168.64.131'), 41369, None)
11
(IPv4Address('192.168.64.131'), 11310, [X.509 Cert. Subject:/C=ZZ/ST=Sate/L=Locality/
12
O=Organization/OU=Organizational Unit/CN=keyserver,
13
Issuer:/C=ZZ/ST=Sate/L=Locality/O=Organization/OU=Organizational Unit/CN=master])
14
...
15
192.168.64.131:11311
16
Node name: master
17
Port: 11311
18
Demo CA Used: True
19
20
Node name: talker
21
Port:
22
Demo CA Used: True
23
Policies:
24
Type: Subscriptable topics
25
Permission: False
26
Values:
27
b'**'
28
29
Type: Publishable topics
30
Permission: False
31
Values:
32
b'/chatter'
33
b'/rosout'
34
35
Type: Unknown
36
Permission: False
37
Values:
38
b'**'
39
40
Type: Executable services
41
Permission: False
42
Values:
43
b'/talker/get_loggers'
44
b'/talker/set_logger_level'
45
46
Type: Readable parameters
47
Permission: False
48
Values:
49
b'/use_sim_time'
50
51
...
Listing 9: aztarna using SROS robot adapter to perform an extended footprinting scan.
13


## Page 14


3.1.3
Industrial routers
Industrial router target
Security researcher: aztarna
HTTP Request
HTTP Response containing headers
Phase 1
Phase 1
Scan and identiﬁcation
HTTP Request
HTTP 401 Unauthorized response
HTTP basic authentication response
HTTP 200 OK Response
Phase 2
Phase 2
Authentication
Figure 4: aztarna performing identiﬁcation and authentication phases for an industrial router.
Direct Internet exposure may seem unrealistic in industrial environments where an external attacker
can tamper critical conﬁguration data and modify the behaviour of robots. Yet, there exist cases where
industrial routers are reachable from outside their operating network. Some of them use default cre-
dentials or even worse, unrestricted access.
There is a new trend in industrial robots where a connection is opened to the open internet so as to
get, to name a few, over-the-air updates, maintenance or monitoring.
These routers allow users to
connect to the robot as if you were on a local network. The number of robots connected to the internet
is increasing, fact that exposes robots to cyber attacks. In principle, industrial robots were designed
to be isolated, but The Internet of the things (IoT) and the Industrial Internet of the Things (IIoT) have
evolved to give internet access to robots, making this system a potential target for cyber attackers.
Following the programming approach explained in section 3.1 a Robot Adapter has been implemented
for industrial routers. The selected router brands are Westermo, Moxa, Sierra Wireless and eWON.
As commonly the web consoles for this routers reside on widely used ports, such as standard 80 and
443 ports, the idea of scanning the whole internet in search of these turns unbearable. Taking this
argument into account, two different strategies are taken, one based on local network host sweeping
and the other based on the whole internet scanning (Taking advantage of the Shodan API [6]).
Local Network footprinting
This approach is meant for scenarios where the aztarna tool is run
in local networks. In this scenario, the range of available hosts is reduced, meaning that scans on the
cited ports are feasible. The usage of aztarna’s industrial robot adapter is demonstrated in Listing 10.
The tool is run indicating it should search for web services on ports 80 and 5001 respectively.
1
$ aztarna -t IROUTERS -a 192.168.1.0/24 -p 80,5001
2
[+] eWON router in \protect\vrule width0pt\protect\href{http://192.168.1.10:80}{http://192.168.1.10:80} is not secure
3
[+] Westermo router in \protect\vrule width0pt\protect\href{http://192.168.1.11:5001}{http://192.168.1.11:5001} is secure
Listing 10: aztarna using IROUTERS robot adapter to perform a footprinting scan.
14


## Page 15


When possible industrial routers are found, the results are split into two groups: Secure and Not
Secure. Secure means that the router is not accessible with default credentials and Not Secure means
that the router is accessible due to default credential usage or even an unrestricted open access. The
technique used for detecting router types consists of grabbing and analyzing the HTTP headers present
in the router’s response message:
• Westermo: These routers responses contains a ﬁeld called WWW-Authenticate which describes
the router’s model Westermo ADSL-350.
HTTP/1.1 401 Unauthorized
Server: GoAhead-Webs
Date: Mon Nov 26 01:07:08 2018
WWW-Authenticate: Basic realm="Westermo ADSL-350"
Pragma: no-cache
Cache-Control: no-cache
Content-Type: text/html
• eWON: These routers Server response header ﬁeld directly indicates the router type::
HTTP/1.1 302 Redirect
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Server: eWON
Date: Sun Nov 25 21:05:53 2018 GMT
Connection: close
Pragma: no-cache
Cache-Control: no-cache,max-age=0,must-revalidate
Content-Type: text/html
• Moxa: In the case of Moxa routers, two well differentiated versions exist, each one with dif-
ferent interface and server versions.
Old Moxa Routers return a Server header detailing the
MoxaHttp/1.0 versions, while newer ones return a server ﬁeld with a value of MoxaHttp/2.2. This
two versions differ in the way that the authentication is performed, which will be described on
later sections.
HTTP/1.1 200 OK
Date: Wed, 19 Feb 2003 09:00:00 GMT
Server: MoxaHttp/1.0
Pragma: no-cache
Cache-Control: no-cache
Content-type: text/html
Content-length: 34273
HTTP/1.1 200 OK
Date: Mon, 03 Mar 2008 08:00:00 GMT
Server: MoxaHttp/2.2
Pragma: no-cache
Cache-Control: no-cache
Content-Type: text/html
Connection: close
Transfer-Encoding: chunked
• Sierra Wireless: Sierra Wireless routers expose an identifying Server ﬁeld in the header as well,
independently from the router version.
15


## Page 16


HTTP/1.1 200 OK
Date: Mon, 03 Mar 2008 08:00:00 GMT
Server: MoxaHttp/2.2
Pragma: no-cache
Cache-Control: no-cache
Content-Type: text/html
Connection: close
Transfer-Encoding: chunked
Shodan based footprinting
Contrary to ROS machines, which don’t run in well known ports, the
connection to industrial routers is usually done in widely used HTTP(80) and HTTPS(443) ports. In this
scenario, a manual internet scan for the given ports is impractical, due to the high number of results
and false positives obtained. To overcome this issue, the Shodan API has been employed. Shodan is
a internet wide scanning platform, in which different crawlers continuously index and store found de-
vices on the internet[6]. These devices can then be retrieved by the use of queries. In this case, part
of the work is done by aztarna. The detection of each of the router models based on the HTTP request
headers, is leveraged to the Shodan API. This scan returns an already ﬁltered set of valid router devices
which the tool is able to handle.
To run a full evaluation for each of the industrial router models, aztarna performs a set of actions to
obtain the data. First and as mentioned in the paragraph above, the tool employs Shodan to perform
the ﬁrst ﬁltering of targets and retrieve their addresses and ports. Once the target acquisition is done,
for each of the industrial routers, a default credentials check is performed.
This check employs a
set of default credentials harvested from manufacturer documentation and other sources. For each
of the credentials, a log-in attempt is made, and successful attempts registered.
Finally, additional
metadata for the scanned address is obtained with the mediation of the Whois database. For each of
the addresses, the country and ASN description are stored.
Password checking
for each of the router models is considered one of the vital steps in the as-
sessment. The metric of how much routers have default credentials or no authentication at all gives
a clear insight on the security posture of the industry against menaces arising from this internet con-
nected devices.
For evaluating if a router is using default credentials, different login attempts are
made to each of the router with passwords that have been documented by the manufacturer or by
other sources[15] being used as defaults.
Each router model follows a different schema for authentication, being basic HTTP authentication the
most used by manufacturers. This type of authentication is the easiest to check among the tested ones,
as the HTTP response code reveals if the login attempt has been successful or not, a 200(OK) code
meaning a successful login attempt, and a 401(Unauthorized) code showing a failed login attempt, as
shown on the example workﬂow ﬁgure ??. Manufacturers not using basic authentication implement
various types of HTML forms for user login, some of them including certain types of challenges and
client side hashing of passwords.
• Westermo Routers present a basic HTTP authentication scheme. The router does not provide
any unauthenticated page, so the base url (/) is adequate for checking the credentials.
• Ewon Routers present a basic HTTP authentication scheme.
In contrast with the Westermo
routers, this type of routers do allow unauthenticated access to certain status pages.
As the
pages requiring authentication vary depending of the router model, a common path has been
required to be determined. On empirical research, the /Ast/MainAst.shtm path has been elected
as requiring authentication for all the tested router models.
16


## Page 17


• Moxa Routers present varying authentication schemas depending on the version of the server. In
both cases, an HTML form is employed, being a password only form in MoxaHttp1.0 routers, and
a user and password form in MoxaHttp2.0 routers. These routers, however, present the option of
not having any password conﬁgured, giving direct access to the router web console in this case.
For checking the validity of the entered credentials, as well as the lack of authentication, different
text outputs provided as responses to the login are compared.
– MoxaHttp1.0 routers present a password only form in cases requiring authentication.
Upon connection by the client, the router sends a random FakeChallenge ﬁeld that is set
on the client as a variable by the usage of JavaScript. At the moment of submitting the en-
tered password, the client creates a MD5 hash of the entered password. This password, in
conjunction with the FakeChallenge ﬁeld, is then sent to the router via a GET request, as
parameters to the /home.htm path.
Password: cd7fb6d7e51b920b59ef1a6d310ac18e
Submit: Submit
token_text:
FakeChallenge: 28F87D79B5CF8608662E50F2ED7555CC4606E62DA647D103ED80007EB7D2320A
– MoxaHttp2.0 routers present a user and password form in cases requiring authentication.
Upon connection by the client, the router sends a random FakeChallenge ﬁeld in form of a
hidden input ﬁeld in the HTML form. A second hidden HTML image input ﬁeld captures the
position of the login button. When submitting the password, on the client, the password hash
is obtained ﬁrst using the MD5 algorithm. This password hash is then sent in conjunction
with the FakeChallenge ﬁeld and the coordinates of the login button, in a POST request
made to the base path.
Username: admin
Password:
MD5Password: 1cf153be978cb3
FakeChallenge: 956901051
Submit.x: 45
Submit.y: 24
• Sierra Wireless routers present a HTML form in which the entered credentials are sent by an
underlying XML request handler. When entering a credential, the client sends a XML encoded
POST request to the /xml/Connect.xml path. This request includes both the username and pass-
word without any kind of encryption. Upon checking the validity of the credentials, the routers
sends well deﬁned XML responses with a message detailing if the login has been successful. This
message is used as the method for checking the validity of the login in the scanner.
<request xmlns="urn:acemanager">
<connect>
<login>user</login>
<password><![CDATA[password]]></password>
</connect>
</request>
Extensibility for other models
As happens for the various models of robots, extensibility has
also been kept in mind when developing the IndustrialRouterAdapter. This scanner eases the in-
clusion of new industrial router models, by providing a base IndustrialRouterScanner class that can
be extended for the various needs of each model. The scanners being used are then deﬁned in the
router_scanner_types class variable present in the IndustrialRouterAdapter class.
17


## Page 18


For the addition of the new model, the IndustrialRouterScanner class is extended, and the possible_headers,
default_credentials and router_cls variables deﬁned.
The possible_headers ﬁeld deﬁnes the HTTP headers that identify the router as being of the deﬁned
model, while the default_credentials and the router_cls variables deﬁne the list of credentials to
be tested, and the router class to be created as a result of a positive router ﬁnd.
This base class provides a default method for testing credentials in HTTP basic authentication scenar-
ios. In order to support other authentication schemes, the check_default_password is required to be
extended. The newly created class is then included in the mentioned router_scanner_types list in
order to be used by the adapter.
4
Results
For this study, different scans have been launched in search for robots and connected industrial routers.
While in the case of ROS and SROS devices, direct, internet wide scans have been performed, in
the case of the industrial routers, Shodan.io[6] has been employed in order to cover the full internet
spectrum. In the following sections, each of the scan methodology and the results are described.
4.1
ROS and SROS robots
During the research, two different global scans of the full internet address space have been performed.
This scans have ﬁrst searched for open ROS Master (11311) ports, and then aztarna has been used to
check that these found hosts actually correspond to machines running ROS or SROS. Finally, the results
provided by aztarna have followed a manual analysis to determine the nature of the found system and
its location, among any other information that could be useful for the ongoing research.
For the initial scan for open ports, in an effort to improve the scan speed, the help of the ZMap tool has
been required. ZMap is a tool optimized for massive scans, that has the ability send up to 14.2 million
packets per second[16], which in scans that only send one packet, such as the TCP SYN scan used in
this research, translated to 14.2 million IP, addresses checked per second. This leads to performing a
full internet scan in less than 5 minutes.
In the case of this study, the lack of dedicated hardware has leveraged to slower scan rates, which
have caused the scan to span to a week. To run the scan, 5 different virtual machines, running Ubuntu
18.04, each of them with 4 cores and 8Gb of RAM, deployed in well known cloud providers, have been
used. The packet rate has been empirically chosen at 800pps, as higher rates showed packet drops
that affected the scan effectiveness negatively.
To evenly distribute the work between the different nodes, the sharding capabilities that zmap provides
have been used. These capabilities allow to divide the address space to search for each of the nodes,
then converging the results.
After this ﬁrst selection and target recollection process, aztarna has been used to determine the valid-
ity of the nodes found. For this, two scans have been launched with aztarna, one for ROS, in extended
mode, and another one for SROS, in standard mode, as the complete host scan is time expensive to
complete and could be interpreted as a phase preliminary to an attack by the target due to the port
scan that is performed. In this case, a single machine has been used to perform both scans, as this
scans are required to scan a lower number of possible targets. File output has been chosen to further
analyze the data.
18


## Page 19


With the obtained data, manual analysis and ﬁltering has been done, in order to determine the nature
of the found robots, using the found topics and communications as indications to determine the model,
purpose, and to determine if the instance is working as a simulated environment or not.
Table 1: Scan Results for ROS systems by country.
Scan 1
Scan 2
Country
Empty
Real
Simulation
Total
Empty
Real
Simulation
Total
AU
0
1
0
1
0
1
0
1
CA
4
1
0
5
0
1
1
2
CN
2
0
0
2
3
2
2
7
CZ
0
0
0
0
2
0
0
2
DE
0
0
0
0
1
0
1
2
ES
1
0
0
1
4
0
0
4
EU
0
0
0
0
0
1
0
1
GR
0
0
0
0
1
4
0
5
HK
2
2
0
4
2
0
0
2
IT
1
0
0
1
4
1
0
5
JP
2
0
0
2
1
0
0
1
KR
5
0
3
8
6
4
6
16
NL
1
0
0
1
1
0
0
1
SE
1
0
0
1
0
0
0
0
SG
0
0
0
0
1
0
0
1
TW
2
0
0
2
2
0
2
4
US
21
7
0
28
25
22
5
52
Grand Total
42
11
3
56
53
36
17
106
Figure 5: Example of industrial, trash classiﬁcation robot, found with aztarna
4.2
Industrial Routers
For industrial routers, a single internet wide scan has been launched, using Shodan in order to deter-
mine the test targets by the deﬁned values to query. This scan has revealed a vast amount of connected
devices, many of them using default, well known credentials, or having no authentication mechanisms
19


## Page 20


at all. For this scan, routers from Ewon, Moxa, Westermo and Sierra Wireless manufactures have been
taken into account. This manufacturers represent the majority of industrial routers present in the in-
dustry. As it can be seen on table 2, from the returned 61265 results from Shodan, 26801 have been
determined as answering to connections, and from this routers, a total of 8958 routers have been de-
termined to be conﬁgured with default credentials or no authentication, which represents a 33% of the
analyzed routers.
The difference between the results returned by Shodan and by the then alive routers is presumably
caused by the usage of dynamic IP addressing in the connections utilized by the routers. As mentioned
before, Shodan utilizes a variety of crawlers that periodically scan the internet searching for connected
devices. The time difference between the scan by Shodan and the scan by aztarna may affect the de-
tection of the devices. On an empirical basis, some of the devices that were being individually analyzed
stopped answering in a time-span of 8 hours, showing a change in the assigned IP address.
The resulting router quantity, as well as the proportion of the routers conﬁgured with default creden-
tials, vs the ones with changed credentials is detailed on table 4.2, as well as in the included proportion
7 and quantity 6 heat maps by country. These results show that United States is the country show-
ing the highest number of connected devices (14755), followed by Canada (1869) and Russia(1120).
Most countries follow a similar balance between correctly conﬁgured and misconﬁgured devices, being
Colombia, with 26 connected devices and with 100% of the devices using default credentials, the most
insecure country. Thailand follows the ranking with 54 devices, showing 93% of them using default
credentials. From the countries with a higher number of connected devices, France stands out in the
proportion of misconﬁgured devices, having a total of 416 devices, with 261 of them(63%) conﬁgured
with default credentials.
Table 2: Scan results for industrial routers by manufacturer
Type
Detected
Alive
Default password
Ewon
4465
983
359
Moxa
13291
6549
971
Westermo
4602
1393
279
Sierra Wireless
38907
17876
7400
Grand Total
61265
26801
9009
Table 3: Scan results for industrial routers by country
Country
Routers
Default Credentials
Changed credentials
Proportion
US
14755
5383
9372
36%
CA
1869
767
1102
41%
RU
1120
201
919
18%
PL
706
59
647
8%
TW
702
197
505
28%
ES
664
356
308
54%
IL
660
393
267
60%
GB
639
158
481
25%
IT
556
169
387
30%
SE
453
149
304
33%
FR
416
261
155
63%
AU
395
87
308
22%
DK
333
57
276
17%
DE
238
42
196
18%
20


## Page 21


Table 3: Scan results for industrial routers by country
Country
Routers
Default Credentials
Changed credentials
Proportion
NL
219
31
188
14%
TR
209
60
149
29%
RO
204
39
165
19%
CN
190
8
182
4%
AT
174
31
143
18%
CL
171
32
139
19%
SK
165
20
145
12%
CH
162
26
136
16%
NO
131
17
114
13%
FI
118
36
82
31%
PT
96
27
69
28%
KR
88
57
31
65%
CZ
84
10
74
12%
HK
83
10
73
12%
BR
73
25
48
34%
EE
64
11
53
17%
IS
64
12
52
19%
LT
60
9
51
15%
JP
58
2
56
3%
KZ
55
6
49
11%
TH
54
45
9
83%
HU
52
10
42
19%
BG
51
5
46
10%
MY
46
34
12
74%
BY
41
16
25
39%
BE
34
5
29
15%
AM
33
8
25
24%
MA
32
13
19
41%
IN
31
5
26
16%
UA
30
0
30
0%
LV
30
0
30
0%
SG
29
2
27
7%
Others
393
120
273
30%
Grand Total
26801
9009
17792
34%
21


## Page 22


Figure 6: Industrial router quantity by country
Figure 7: Proportion of industrial routers using no authentication or default credentials. From 0 (0%, blue) of the devices
using default credentials, to 1 (100%, red) of the devices using default credentials
5
Remarks and future work
ROS was born as a research framework for robotics development. Now, it’s being gradually replaced
by its second version, ROS 2. This new version has taken a massive architectural shift, that will require
a separate reconnaissance rationale. ROS 2 technology is based on the DDS (Data Distribution Service)
standard, which allows ROS 2 based systems to communicate in a low latency, extremely reliable and
distributed environment[17]. ROS 2 security is currently under discussion.
Apart from ROS, some robot manufacturers tend to develop their own exclusive programming APIs.
Although ROS is becoming the de facto standard in robot programming, there is a set of proprietary
tools being extensively used by leading robotic companies. One example is ABB’s RobAPI [18], a REST
based programming library.
22


## Page 23


Extensions of aztarna towards ﬁngerprinting are also expected. Examples of such extensions include
determining the speciﬁc ﬁrmware version in robots, discovering third-party libraries used and their
versions (e.g. robot middleware version, communication infrastructure, etc.). In industrial environ-
ments, robots commonly use industrial communication protocols. These can be both standardized (e.g.
EtherCAT, PROFINET) or proprietary (e.g. ABB’s MMS, Beckhoffs’s ADS/AMS). The ability to dissect
and understand these protocols is itself useful for footprinting purposes.
With regards to unprotected industrial routers in this work, there are other models that could be de-
tected in a similar fashion as the ones presented in subsection 3.1.3, just by looking at their HTTP
response headers, but are not included within the present version of aztarna. Other techniques to lo-
cate vulnerable industrial routers include the FTP port scanning and banner grabbing, which is demon-
strated in [8] are not explored in the present version. These include Sierra Wireless and Digi among
others [8], widely used in industrial environments.
Industrial routers pose an entry point for robots that are located on the network behind the industrial
router, which is usually directly connected to the device. This is more evident in the cases of routers
exposing default passwords. Most of these routers have reported vulnerabilities and ﬂaws that are sub-
ject to update by users. Furthermore, given that most industrial routers provide means to establishing
VPN connections, both in server and client mode, tunnels to a protected network behind the routers
are a very likely attack vector The automation of this processes could allow researchers to audit the
devices that are behind of the router, as well as the router security itself, providing a better insight on
the nature of the target. This process will be part of the industrial routers ﬁngerprinting phase, as we
pretend to go deep exploring new vulnerabilities.
With the retrieved information, we aim to reinforce the awareness of the robot users community we
advocate in favour of secure and tested industrial networks to avoid the dangers of targeted attacks
towards robots. Finally, we encourage the manufacturers to address a security by design policy.
Overall, we conclude that aztarna responds to the need of auditing robot security. As ROS is becoming
the de facto standard in robot programming, more and more robots are being exposed everyday. The
footprinting techniques on ROS are specially dangerous, because once detected and footprinted, ROS
powered systems are inherently vulnerable.
Existing robot security mitigations, such as SROS, are
not used extensively. The present study reports mainly research robots aligned with prior art, but we
have reported the footprinting of professional robots as well. We have discovered an array of internet-
connected unprotected industrial routers, that could potentially host robots. There is an unresolved
gap in robotics cybersecurity which would greatly beneﬁt from releasing the ﬁrst auditing tools.
6
Acknowledgments
This research has been partially funded by the Basque Government, throughout the Business Develop-
ment Agency of the Basque Country (SPRI) through the Ekintzaile 2018 program and EU H2020 Robot
Union Program through the Grant Agreement nº 779967. Special thanks to BIC Araba and the Basque
Cybersecurity Centre (BCSC) for the support provided.
References
[1] V. Mayoral Vilches, L. Alzola Kirschgens, A. Bilbao Calvo, A. Hernández Cordero, R. Izquierdo
Pisón, D. Mayoral Vilches, A. Muñiz Rosas, G. Olalde Mendia, L. Usategi San Juan, I. Zamalloa
23


## Page 24


Ugarte, E. Gil-Uriarte, E. Tews, and A. Peter, “Introducing the robot security framework (rsf), a
standardized methodology to perform security assessments in robotics,” ArXiv e-prints, Jun. 2018.
[2] V. Mayoral Vilches, E. Gil-Uriarte, I. Zamalloa Ugarte, G. Olalde Mendia, R. Izquierdo Pisón, L. Al-
zola Kirschgens, A. Bilbao Calvo, A. Hernández Cordero, L. Apa, and C. Cerrudo, “Towards an
open standard for assessing the severity of robot security vulnerabilities, the Robot Vulnerability
Scoring System (RVSS),” ArXiv e-prints, Jul. 2018.
[3] L. Alzola Kirschgens, I. Zamalloa Ugarte, E. Gil Uriarte, A. Muñiz Rosas, and V. Mayoral Vilches,
“Robot hazards: from safety to security,” ArXiv e-prints, Jun. 2018.
[4] N. DeMarinis, S. Tellex, V. Kemerlis, G. Konidaris, and R. Fonseca, “Scanning the Internet for ROS:
A View of Security in Robotics Research,” 2018.
[5] G. Olalde Mendia, L. Usategui San Juan, X. Perez Bascaran, A. Bilbao Calvo, A. Hernández
Cordero, I. Zamalloa Ugarte, A. Muñiz Rosas, D. Mayoral Vilches, U. Ayucar Carbajo, L. Alzola
Kirschgens, V. Mayoral Vilches, and E. Gil-Uriarte, “Robotics CTF (RCTF), a playground for robot
hacking,” ArXiv e-prints, Oct. 2018.
[6] “The search engine for the internet of things.” [Online]. Available: https://www.shodan.io/
[7] A. Mirian, Z. Ma, D. Adrian, M. Tischer, T. Chuenchujit, T. Yardley, R. Berthier, J. Mason,
Z. Durumeric, J. A. Halderman, and M. Bailey, “An internet-wide view of ICS devices,” in
2016 14th Annual Conference on Privacy, Security and Trust (PST).
IEEE, dec 2016. [Online].
Available: https://doi.org/10.1109/pst.2016.7906943
[8] F. Maggi, D. Quarta, M. Pogliani, M. Polino, A. M. Zanchettin, S. Zanero, and P. Di Milano, “Rogue
Robots: Testing the Limits of an Industrial Robot’s Security,” Tech. Rep.
[9] J. P. McGreevy, “Footprinting: What Is It, Who Should Do It, and Why?” SANS Institute, Monterrey,
Tech. Rep., 2002. [Online]. Available: https://www.sans.org/reading-room/whitepapers/auditing/
footprinting-it-it-why-62
[10] P. Laperdrix,
W. Rudametkin,
and B. Baudry,
“Beauty and the Beast:
Diverting modern
web
browsers
to
build
unique
browser
ﬁngerprints,”
in
37th
IEEE
Symposium
on
Security and Privacy (S&P 2016), San Jose, United States, May 2016. [Online]. Available:
https://hal.inria.fr/hal-01285470
[11] Z. Durumeric, E. Wustrow, and J. A. Halderman, “ZMap: Fast Internet-wide Scanning and Its
Security Applications,” Proceedings of the 22nd USENIX Security Symposium, no. August, pp.
605–619, 2013. [Online]. Available: https://zmap.io/paper.pdf
[12] R. White, G. Caiazza, H. Christensen, and A. Cortesi, “SROS1: Using and Developing Secure
ROS1 Systems.” [Online]. Available: https://doi.org/10.1007/978-3-319-91590-6{_}11
[13] D.
Cooper,
S.
Santesson,
S.
Farrell,
S.
Boeyen,
R.
Housley,
and
W.
Polk,
“Internet
x.509
public
key
infrastructure
certiﬁcate
and
certiﬁcate
revocation
list
(crl)
proﬁle,”
Internet Requests for Comments,
RFC Editor,
RFC 5280,
May 2008. [Online]. Available:
https://www.rfc-editor.org/rfc/rfc5280.txt
[14] P. Biondi, “Scapy.” [Online]. Available: https://scapy.net/
[15] Scadastrangelove,
“scadastrangelove/scadapass,”
Nov
2016.
[Online].
Available:
https:
//github.com/scadastrangelove/SCADAPASS
[16] D.
Adrian,
Z.
Durumeric,
G.
Singh,
and
J.
A.
Halderman,
“Zippier
ZMap
:
Internet-
Wide Scanning at 10 Gbps,”
Usenix Woot,
no. August,
p. 8,
2014. [Online]. Available:
http://dl.acm.org/citation.cfm?id=2671293.2671301
24


## Page 25


[17] O. M. Group, “What is dds?” https://www.omgwiki.org/dds/what-is-dds-3/, 2018, accessed: 2018-
12-01.
[18] ABB, “Api reference,” http://developercenter.robotstudio.com/webservice/api_reference, 2016, ac-
cessed: 2018-12-03.
25

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]