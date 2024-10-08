# Lab: Password brute-force via password change

Description : This lab's password change functionality makes it vulnerable to brute-force attacks

End Goal : brute-force Carlos's account and access his "My account" page.

creds : `wiener:peter`, victim's username `carlos`

Analysis :

- sending current password wrong with 2 matching new passwords -> locks us out
- while sending current password wrong with 2 not matching new passwords -> just says that our current password is wrong with no lock out
