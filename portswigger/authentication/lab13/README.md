# Lab: Broken brute-force protection, multiple credentials per request

Description : This lab is vulnerable due to a logic flaw in its brute-force protection.

End Goal : To solve the lab, brute-force Carlos's password, then access his account page.

creds : victim's username `carlos`

Analysis :

- after third attempt to enter invalid credentials -> locking us out
- the backend process the value of pramaeters when send in array as well
- we could test this vulnerability in OTPs (2fa) as well
