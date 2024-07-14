# Lab: CSRF where token is not tied to user session

This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't integrated into the site's session handling system.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You have two accounts on the application that you can use to help design your attack. The credentials are as follows:

- ```wiener:peter```
- ```carlos:montoya```
-----

Analysis: 
In order for a CSRF attack to be possible:

- A relevant action: change a users email
- Cokkie-based session handling: session cookie
- No unpredictable request parameters: csrf token is not tied to user session


Testing CSRF TOkens:
 
1. Remove the CSRF toekn and see if application accepts request
2. Change the request from POST to GET
3. See if CSRF token is tied to user session