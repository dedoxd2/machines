# Lab: Exploiting XSS to perform CSRF

This lab contains a stored XSS vulnerability in the blog comments function. To solve the lab, exploit the vulnerability to perform a CSRF attack and change the email address of someone who views the blog post comments.

You can log in to your own account using the following credentials: wiener:peter

----

Analysis :

- The comment function doesn't have any protection to , it's an easy xss

- Changing Email function have a static  csrf token , knew that from sending the same request over and over!!

- The comment form also have the same static csrf token from changing mail functionality!!

to exploit those vulnerabilities we need to

1- GET request to `/my-account`
2- extract the `CSRF` token (let's try to make it harder)
3- POST `/my-account/change-email` with the new email + CSRF Token
4- but for further maintaining the attack we need to grap the username for the users who is viewing our exploit
