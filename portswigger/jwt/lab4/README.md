# Lab: JWT authentication bypass via jwk header injection

Description : This lab uses a JWT-based mechanism for handling sessions. The server supports the jwk parameter in the JWT header. This is sometimes used to embed the correct verification key directly in the token. However, it fails to check whether the provided key came from a trusted source.

End Goal : privilage escalation (access admin panel)

creds : `wiener:peter`

Analysis :

- in this lab we created a jwk
- then we embeded it inside our token
- we manipulated our data and the server used our embeded jwk to verify our token
