# Lab: Information disclosure in error messages

Descirption : This lab's verbose error messages reveal that it is using a vulnerable version of a third-party framework. To solve the lab, obtain and submit the version number of this framework.

Analysis :

Spidering the web app noticing that it only takes 2 user inputs

1. is the product id in this endpoint `/product?productId=1`
2. the other one is the `session cookie` , entering aribitary input raises 500 error
