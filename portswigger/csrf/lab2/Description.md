# Lab: CSRF where token validation depends on request method

This lab's email change functionality is vulnerable to CSRF. It attempts to block CSRF attacks, but only applies defenses to certain types of requests.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: ```wiener:peter```


### Analysis :
- Relevant action -> changing the email
- the server identifies the user using cookie ```Cookie: session=PNlqwnbaO5UDzzJYAkQWh6CAlWmdLuoj```
- there is a csrf token and the server validating but , when i have tried to change the method from ```POST``` to ```GET``` the server didn't even ask for the csrf token

- recomendation for metigating this bug :
    - just disable the GET method