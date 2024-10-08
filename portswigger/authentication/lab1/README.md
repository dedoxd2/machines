# Lab: Username enumeration via different responses

This lab is vulnerable to username enumeration and password brute-force attacks. I

End Goal :  To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

Analysis :

- First in the script i was trying to brute map the all passwords to all users but , it took so long (complixty O(N*M) where: N= number of usernames , M: Number of passwords ) as the book was saying (it's the prefered way to do it )
- but i changed it instead of starting with specific passwd i started with specific username and if the username is valid then , im gonna test it with all passwords , if not -> just break the loop and test for another username
