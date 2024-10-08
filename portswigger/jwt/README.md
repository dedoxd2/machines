# JWT Attacks

## this is test cases u may try when testing JWT

1- Change the username or change any sensitive data in the claims(lab1)
2- try the none algorithm attack(lab2)
3- u might try to brute force the secret key ("alg": "HS256" -> weak algorithm could be brute forced)(lab3)
4- embeded jwk , create a jwk and embeded it into ur token(lab4)
5- try to add jku to the headers and use this key to sign ur key (lab5)
6- if the key_id is used to points to the secret key on the file system make it points to null , then use a key it's value is base64 encoding of null then sign ur token with it (lab6)
