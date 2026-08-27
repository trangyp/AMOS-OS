---
tags: [misc]
---
# SSRF
What is it?
* induce server-side application to make HTTP requests to domain of attackers choosing
* maker server make connection back to itself, other web services within organisation or third party stuff.

Impact?
* Result in unauthorised actions/access
* May allow attacker to perform arbitrary command execution (OS COM INJ topic)

Finding Hidden Attack surface for SSRF Vulnerabilities
* Mostly easy to spot (traffic involves request parameters)
* Partial URL's in requests
   	* Sometimes app places hostname or partial URL in request parameters
   	* then incorporated server side.
   	* Hard unless you know the entire URL
* URLs within Data formats
   	* XML, if server processing, could be subject to XXE
* Referer Header
   	* If server side analystics software tracks visitors -> might visit your dody site

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
