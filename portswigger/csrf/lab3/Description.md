# Lab: CSRF where token validation depends on token being present

This lab's email change functionality is vulnerable to CSRF.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: ```wiener:peter```
<br>

### Analysis

explanasion : why this bug occured here ?
<br>
<br>
answer:  because the server side only validating the ```CSRF Token``` when only it exists , which means if u :

- have added arbitrary value -> returns 400 Bad request "Inavlid CSRF token"
- removed the value from the csrf parameter ```email=test%40gmail.com&csrf``` -> returns Bad request 400 "Missing parameter 'csrf'"
- but if u have removed the whole parameter ```email=test%40gmail.com``` -> returns 302 Found BINGO!
