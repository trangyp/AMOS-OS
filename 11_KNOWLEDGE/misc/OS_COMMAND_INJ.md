---
title: OS COMMAND INJ
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# OS Command Inj
What is it?
* aka shell injection
* execute OS commands on server running the application
* Exploit trust relationships to pivot attack to other systems in org

Executing Arbitrary Commands
* Identify when a shell command is being executed, insert something in it
* & echo aiwefwlguh &
   	* echo will echo in the output (to test where output is displayed)
   	* & is seperator -> command is executed after
   	* Good way of checking if there are systems in place
      		* If echo was executed
      		* if the whole thing was executed

Useful Commands
* whoami = name of current user
* uname -a = OS (linux)
* ver = OS (windows)
* ifconfig = network config (add an “ /all” at the end for windows)
* netstat -an = network connections
* ps -ef = Running processes (linux)
* tasklist = Runing processes (windows)

Prevention
* never call out OS commands from application layer
   	* Always another way of doing this
* If unavoidable : input validation!
   	* Allowlists
   	* insure it is correct datatype (e.g. phone number is integer)
   	* no whitespace or other syntax (alphanumeric)
* Don't bother trying to sanitise input by escaping shell matacharacters, there are so many ways around it

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
