# Lab: Username enumeration via response timing (Not Done yet)

Description : This lab is vulnerable to username enumeration using its response times

End Goal : To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

credentials :  `wiener:peter`

Analyisis :

- trying to login with invalid credentials takes less 500 millis
- valid credentials takes max 200 milisecs
- when the password is too big it takes above 500 milisecs
- after couple of attempts it locks out us , to bypass that we just use `X-Forwarded-For: num++` , increament the number every time we get locked out
