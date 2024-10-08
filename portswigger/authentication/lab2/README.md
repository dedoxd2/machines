# Lab: 2FA simple bypass

Description : This lab's two-factor authentication can be bypassed. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, access Carlos's account page.

Creds : `wiener:peter` , `carlos:montoya`

Analysis :

- since the OTP expires after one wrong trial so it's not an option to brute force it
- instead of brute forcing or trying to response manipulation , i just simply wento `/my-account?id=carlos` after i loged in
