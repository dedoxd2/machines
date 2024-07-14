# Lab: CSRF where Referer validation depends on header being present

This lab's email change functionality is vulnerable to CSRF. It attempts to block cross domain requests but has an insecure fallback.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: ```wiener:peter```


Analysis:

Vunlerable parameter -> email change functionality
Goal -> exploit CSRF to change email address



In order for a CSRF attack to be possible:
    - A relevant Action : change users email
    - Cookie-based session handling: session cookie
    - No unpredictable request parameters

Testing Referer header for CSRF attacks:
1. remove the Refere header