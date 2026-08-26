---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.01388v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1811.01388v2_Web_Security_Investigation_through_Penetration_Tests__A_Case_study_of_an_Educati

> Source: 1811.01388v2_Web_Security_Investigation_through_Penetration_Tests__A_Case_study_of_an_Educati.pdf

> Pages: 4

---


## Page 1


Web Security Investigation through Penetration
Tests: A Case study of an Educational Institution
Portal
D. Omeiza and J. Owusu-Tweneboah
Carnegie Mellon University - Africa
Kigali, Rwanda
{domeiza, jowusu}@africa.cmu.edu
Abstract—Web security has become an important subject;
many companies and organizations are becoming more security
conscious as they build web applications to render online services
and increase web presence. Unfortunately, many of these web
applications are still susceptible to threats as they lack strong
immunity to malicious attacks. This poses potential danger to
the users of the sites and could also affect operations of the
organizations or companies concerned. Educational institutions
are not left out, their portals and websites hold vital information
whose integrity is of utmost importance. Taking Carnegie Mellon
University Africa’s internship portal as case study, we carried out
penetration tests to investigate web vulnerabilities and proffered
possible remedies to the discovered vulnerabilities. Our result
will inform educational institutions on better website security
practices, especially in the African domain.
Index Terms—Pentesting, Penetration Testing, Nmap, Metas-
ploit, BurpSuite framework.
I. INTRODUCTION
About 24 million malware incidents targeting Africa were
observed in 2016 [1]. As the internet community expands,
web threats are on the rise and it is difﬁcult to provide
patches that aid in solving all security vulnerabilities. A
vulnerability is a ﬂaw or weakness in a systems design,
implementation or operation that could be exploited to violate
the systems security. A vulnerability is also a combination
of three elements which involve the system ﬂaw, attacker
accessibility to the ﬂaw and attacker efﬁciency to exploit
the ﬂaw [2]. Studies have shown that ﬁrewalls and anti-virus
programs are not sufﬁcient to provide effective system security
[2]. There are attacks such as cross site scripting and many
others which affect websites. Cross site scripting refers to the
injection of malicious scripts into a legitimate website [3].
We investigate vulnerabilities and the safety level of students
and companies data on the internship portal of Carnegie
Mellon University Africa (CMUA). 1 The internship portal
was purposely built to grant access to companies to upload
internship vacancies available. Students can access the portal
and are able to view company details, see vacancies available
and get information on the application procedures. Students
upload conﬁdential information on the website. Thus, this site
represents a modestly complex site with multiple types of
data and different stakeholders. Understanding vulnerabilities
1https://cmu-r.secure.force.com/Careers/InternshipHomePage
will inform the CMUA Information Technology team, website
administrators in other educational institutions, and anyone
with knowledge on security policies and systems with the kind
of security measures to put in place in their systems to avoid
users data compromise.
In this work, penetration tests were carried out on the
website to identify vulnerability of the website. However,
attack recovery mechanisms were not investigated in this work.
Penetration testing examines the behavior of systems under
extreme conditions to identify their weaknesses and vulner-
abilities. Penetration testing can highlight issues in security
using a variety of tools which are able to analyze the system,
while others attack the system to exploit vulnerabilities. Pene-
tration testing involves gathering information about the target
system before the test (reconnaissance), identifying possible
entry points, attempting to break in and reporting the ﬁndings
[4]. Types of penetration tests include; external test, internal
test, blind test and double-blind test. The choice depends on
the environment where the test will be run. In this paper, we
focus on external. External test aims to examine if illegitimate
people can gain unauthorized access and what level of access
can be gained while internal test simulates an attack from the
inside behind the ﬁrewall by an authorized user with standard
access privileges.
II. IMPORTANCE AND PRIOR WORK
In related papers, authors mentioned how malicious attack-
ers can edit customers information, how to perform tests to
discover vulnerabilities and how to protect against attacks.
A. Why secure web applications?
[5] discussed web application security and the different
techniques that can be used to establish potential vulnerabili-
ties a web application might have. From the authors research,
they found that the growth and evolution of the internet
have impacted the way we generate and communicate many
sensitive information. The authors mentioned that e-commerce
sites which produce data can be stolen or altered if they do
not have the necessary safety measures for handling their use.
The fact that computers worldwide are susceptible to attack
by hackers or crackers able to compromise computer systems
and steal valuable or delete a large part of the computers
arXiv:1811.01388v2  [cs.CR]  8 Nov 2018


## Page 2


information is an issue which needs to be investigated. Some
common attacks on web application mentioned by the authors
include semantic URL; where the attacker modiﬁes the URL
to perform actions that are not originally planned to be handled
properly by the server, cross-site scripting; which allows code
injection by malicious web users, where false requests are sent
using special tools and cross-site request forgery; which allows
the attacker to send HTTP requests at will from the victims
machine. This situation is essential to know if these systems
and data networks are protected from any kind of intrusion. It
is important that web applications are not only designed for
the objectives for which they were created but they must also
be designed to take care of the data and information generated
in them.
B. What kind of tests should be performed on websites?
[4] presented different aspects of penetration testing includ-
ing tools, attack methodologies and defense strategies. Differ-
ent penetration tests were performed using a private network,
devices and virtualized systems and tools. The authors per-
formed attacks such as smartphone penetration testing, hacking
phones Bluetooth, trafﬁc snifﬁng, man-in-the-middle attack,
spying and hacking remote PC via IP and open ports using
advanced port scanner. The authors purpose was to explain the
use of penetration testing and share concepts for understanding
the test. Tools within the Kali Linux suite were used. The
result showed a success rate of 14.29% for a man-in-the-
middle attack, and a remote PC hacking. The researchers also
corroborated the fact that anti-viruses and anti-malware are
not sufﬁcient anymore to ensure security. They also expressed
how important systems like weather systems could be easily
violated through penetration testing tools.
[6] presented an efﬁcient integrated penetration testing tool
to detect ﬁve of the top ten web application vulnerabilities to
date. They also pointed out issues accompanied with some
penetration testing tools. Issues such as generation of high
rates of false positives/negatives, efﬁciency, performance and
reliability of the results are concerns while using systems like
Acunetix, ZAP and w3af for penetration testing. From their
research, they gathered that lightweight penetration testing ap-
proaches which generate extremely low false positive/negative
rates are required. Their Web Guardia (an integrated penetra-
tion testing system to detect web application vulnerabilities) is
able to crawl through a given target web application and detect
vulnerabilities such as SQLI, XSS, Unvalidated Redirects and
Forwards, Insecure Direct Object References and Security
Misconﬁgurations. Their tool uses a simple architecture which
involves crawling, attacking analyzing and reporting modules.
From their research, it was discovered that the use of Web
Guardia can keep the generation of false positives and nega-
tives at a minimum level because it is technically unfeasible
to completely avoid generation of false positives and false
negatives.
C. How to mitigate Web Security Attacks?
Protecting shared assets from unauthorized users has be-
come more than necessity. [3] demonstrated that ﬁrewalls,
antivirus software, Windows Defender and other prevention
techniques will not sufﬁce in preventing attacks. The authors
examined different aspects of penetration testing to determine
vulnerable applications and hosts using the Nmap and Metas-
ploit frameworks. A virtualized system was used that included
different versions of Windows and Linux OS. The results
showed that tools such as Nmap and the Metasploit framework
are effective tools for the discovery of open holes in a defense
system or network. The test results indicated that vulnerable
programs are the main source of the problem. Also, creating
patches is not a good ﬁx because same types of vulnerabilities
are exploited daily through code injection, remote access, and
denial of service.
[7] identiﬁed web defacement as one of the most common
attacks on websites. The authors explained that there has been
a gentle decline in the number of web defacement from 2013
to 2017. They proposed a Web Defacement and Intrusion
Monitoring Tool (WDIMT) that could rapidly identify altered
or deleted web pages. The proposed tool will also be used to
regenerate the original content of a website after the website
has been defaced, this is one of the strongest points of
WDIMT. The tool uses four major commands to perform tasks,
which are: Initialize, verify, force, and delete. Upon executing
these commands, the WDIMT detects any defacement that
may have occurred or is currently in progress. If defacement
is noticed it re-uploads the original content of that web page.
This tool may help to reduce the numbers and effects of web
defacement attacks.
III. METHODOLOGY
Fig. 1. A high-level view of the step followed.
Fig.1 above shows the conceptual view of the approach
adopted. In getting a clue to how safe user data in Carnegie
Mellon University Africas internship portal is, the answers to
the following questions will be helpful. Is CMUA internship
system secure? Are there vulnerabilities, and how severe are
the vulnerabilities? How easy (in terms of time and resources
committed) is it for an attacker to penetrate and compromise
the system? The answers will be made clear in our results.
The educational institutions as the targeted audience in this
research will stand to beneﬁt from the outcome of the research


## Page 3


and may take actions where necessary to ensure maximum
security.
The work involved the use of BurpSuite for penetration
testing of the selected website to investigate the degree of
security of data in the website. Vulnerabilities discovered after
the scan were classiﬁed by level of severity and certainty. In
details we discuss the chosen tool, scope of the work, and
approach.
A. Tool Employed
After analyzing the pros and the cons of existing pene-
tration testing tools, BurpSuite was identiﬁed as the most
suitable tool in the context of this research. BurpSuite is a
cross-platform java application with several Web Application
Security or penetration testing tools bundled into it to make
a single suite. Reasons for choosing BurpSuite is that it is
easier to use, and basic tests do not require the writing of
scripts. BurpSuite makes processes like intercept behavior
conﬁgurations, application walk through, automated scanning
and initial pilfering easier. Also, Kali Linux operating system
comes with BurpSuite’s free edition installed.
B. Scope
We limit this work to external penetration test operations
which involve, scanning the website for SQL injection, cross-
site scripting and other common vulnerabilities.
C. Approach
To investigate security through penetration testing on the in-
ternship portal, an approach that involved the use of BurpSuite
for website scanning was used. The BurpSuite application
can run on both Linux and Windows operating system. It
provides functionalities for easy setup and automated scan.
Below are some of the features contained in BurpSuite as
provided from BurpSuites documentation. Some of these tools
will be employed in this research.
• Spider: This can be used for automatically crawling an
application, to discover its content and functionality.
• Scanner: This is used to automatically scan HTTP re-
quests to ﬁnd security vulnerabilities.
• Intruder: This allows you to perform customized auto-
mated attacks, to carry out all kinds of testing tasks.
• Repeater: This is used to manually modify and reissue
individual HTTP requests over and over.
• Sequencer: This is used to analyze the quality of random-
ness in an application’s session tokens.
• Decoder: This lets you transform bits of application data
using common encoding and decoding schemes.
• Comparer: This is used to perform a visual comparison
of bits of application data to ﬁnd interesting differences.
The spider, scanner where explicitly used in our test op-
erations, other features where employed implicitly during
the run process.
Fig. 2 shows details of the steps (step 1 to step 7) we
followed in using BurpSuite for the vulnerability analysis
of the portal.
Fig. 2. A high-level view of the step followed.
TABLE I
ISSUES WITH SEVERITY AND CONFIDENCE LEVEL.
IV. PENETRATION TESTING RESULT AND DISCUSSION
After scanning with BurpSuite, 16 certain low severity
issues were discovered as shown in Table 1 below.
The conﬁdence level indicates BurpSuites certainty of the
issues discovered. The severity level indicates the impact a
vulnerability has on the system if exploited. Vulnerabilities are
hereby listed with corresponding remediation where necessary.
A. Input returned in response (reﬂected)
There were two instances of this issue. It affected the Home
and Contacts page of the website. This issue could lead to
client-side vulnerabilities such as cross site scripting, open
redirection, content spooﬁng and response header injection.
In a case such as this, server-side vulnerabilities like SQL
injection is easier. This vulnerability could be further classiﬁed
as Improper Input Validation which leads to unintended inputs
and Improper Encoding or Escaping of output which leads to
the structure of the message not been preserved.
Remediation: Input should not be echoed at the applica-
tions response.
B. Cross-domain Referrer leakage
There were three instances of this issue which occurred at
the Contacts, Home and root page. The vulnerability was clas-
siﬁed as Information Exposure vulnerability in the Common
Vulnerabilities and Exposure (CVE) list.
Remediation: Applications should never transmit any sen-
sitive information within the URL query string. In addition to
being leaked in the Referrer header, such information may be


## Page 4


logged in various locations and may be visible on-screen to
untrusted parties.
C. Cross-domain script include
This occurs when an application includes scripts from
an external domain. The script is executed by the browser
within the security context of the invoking application and can
function as the applications own script and has access rights to
the application data and perform actions within the context of
the current user. The vulnerability was classiﬁed as Inclusion
of functionality from untrusted control sphere vulnerability in
the CVE list.
Remediation: Scripts should not be included from untrusted
domains. Applications that consider the use of third-party
scripts should copy the contents of the scripts to their own
domain else re-implement the scripts functionality within the
application code.
D. Password with autocomplete enabled
There were two instances of this issue on the site. It
occurred on the root page and the careers page. This function
can be conﬁgured by the user and by applications that employ
user credentials. This functionality allows the storage of user
credentials on the local computer and is retrieved on future
visits to the same application. The stored credentials can be
captured by an attacker who gains control over the users
computer. The vulnerability was classiﬁed as Inclusion of
functionality from untrusted control sphere vulnerability in the
CVE list.
Remediation: Include the attribute autocomplete=”off”
within the FORM tag (to protect all form ﬁelds) or within
the relevant INPUT tags (to protect speciﬁc individual ﬁelds).
E. Browser cross-site scripting ﬁlter disabled
Some browsers, including Internet Explorer, contain built-
in ﬁlters designed to protect against cross-site scripting (XSS)
attacks. Applications can instruct browsers to disable this ﬁlter
by setting the following response header: X-XSS-Protection:
0. This behavior does not in itself constitute a vulnerability;
in some cases, XSS ﬁlters may themselves be leveraged to
perform attacks against application users. However, in typical
situations, XSS ﬁlters do provide basic protection for appli-
cation users against some XSS vulnerabilities in applications.
The presence of this header should be reviewed to establish
whether it affects the application’s security posture.
Remediation: Review whether the application needs to
disable XSS ﬁlters. In most cases you can gain the protec-
tion provided by XSS ﬁlters without the associated risks by
using the following response header: X-XSS-Protection: 1;
mode=block
F. Client-side HTTP parameter pollution (reﬂected)
Client-side HTTP parameter pollution (HPP) vulnerabilities
arise when an application embeds user input in URLs in
an unsafe manner. An attacker can use this vulnerability to
construct a URL that, if visited by another application user,
will modify URLs within the response by inserting additional
query string parameters and sometimes overriding existing
ones. This may result in links and forms having unexpected
side effects. For example, it may be possible to modify an
invitation form using HPP so that the invitation is delivered
to an unexpected recipient.
Remediation: Ensure that user input is URL-encoded be-
fore it is embedded in a URL.
G. Email addresses disclosed
The presence of email addresses within application re-
sponses does not necessarily constitute a security vulnerabil-
ity. Email addresses may appear intentionally within contact
information, and many applications (such as web mail) include
arbitrary third-party email addresses within their core content.
Remediation: Consider removing any email addresses that
are unnecessary. Provide a form that generates the email
server-side, protected by a CAPTCHA if necessary.
H. Cacheable HTTPS response
Remediation: Applications should return caching directives
instructing browsers not to store local copies of any sensitive
data. Often, this can be achieved by conﬁguring the web server
to prevent caching for relevant paths within the web root.
V. CONCLUSION
On investigating web security on educational institution web
portal, Carnegie Mellon Africas internship portal was analyzed
externally for vulnerabilities to determine the safety of user
data on the site. The result from this analysis explains that the
level of security of user data on the website is not sufﬁcient.
Although in context, the issues discovered are of low severity,
the combination of such low severity issues become serious
and demand attention. Remedies have been proffered for the
vulnerabilities discovered. This stands to inform educational
institutions on measures to assure secure websites and portals.
Future work involves exploitation of XSS vulnerabilities by
launching XSS attacks on a similar portal.
REFERENCES
[1] V. Appiah, I. KoﬁNti, and O. Nyarko-Boateng, Investigating websites
and web application vulnerabilities: Webmasters Perspective, Int. J.
Appl. Inf. Syst., vol. 12, no. 3, pp. 1015, 2017.
[2] S. P. Kadam, B. Mahajan, M. Patanwala, P. Sanas, and S. Vidyarthi,
Automated Wi-Fi penetration testing, Int. Conf. Electr. Electron. Optim.
Tech. ICEEOT 2016, pp. 10921096, 2016.
[3] O. Aslan and R. Samet, Mitigating cyber security attacks by being aware
of aulnerabilities and bugs, 2017 Int. Conf. Cyberworlds, pp. 222225,
2017. Suhl, Eds. New York: Academic, 1963, pp. 271-350.
[4] M. Denis, C. Zena, and T. Hayajneh, Penetration testing: Concepts,
attack methods, and defense strategies, 2016 IEEE Long Isl. Syst. Appl.
Technol. Conf. LISAT 2016, 2016.
[5] R. E. Lopez De Jimenez, Pentesting on web applications using ethical
hacking, 2016 IEEE 36th Central American and Panama Convention
(CONCAPAN XXXVI), no. 503, 2016.
[6] N. M. Vithanage and N. Jeyamohan, WebGuardia - An integrated
penetration testing system to detect web application vulnerabilities, Proc.
2016 IEEE Int. Conf. Wirel. Commun. Signal Process. Networking,
WiSPNET 2016, pp. 221227, 2016.
[7] M. Masango, F. Mouton, P. Antony, and B. Mangoale, Web Defacement
and Intrusion Monitoring Tool: WDIMT, 2017 International Conference
on Cyberworlds (CW), 2017.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]