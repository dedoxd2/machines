# Lab: 2FA broken logic

Description : This lab's two-factor authentication is vulnerable due to its flawed logic

End Goal : To solve the lab, access Carlos's account page. (login as `carlos`)

creds: `wiener:peter` , victim's username `carlos`

Analysis :

- notice the cookie with value of the usrename in the `/login2` after entering valid username and password
- change it to victim username `Cookie: verify=carlos`
- send get request with this cookie to `/login2`, to triger back end to send OTP to the victim
- brute force it !! (don't forget to set the cookie)
