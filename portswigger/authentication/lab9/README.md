# Lab: Brute-forcing a stay-logged-in cookie

Description : This lab allows users to stay logged in even after they close their browser session. The cookie used to provide this functionality is vulnerable to brute-forcing.

End Goal :  To solve the lab, brute-force Carlos's cookie to gain access to his "My account" page.

creds : `wiener:peter`, victim's username `carlos`

Analysis:

- after loging in notice cookie `stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw`
- it's encoded as base64 and it's value is username:hash of password using md5 algorithm
